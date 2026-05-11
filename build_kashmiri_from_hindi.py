#!/usr/bin/env python3
"""
Rebuild kashmiri_data.js to mirror the Hindi/Maithili phrase+word sets (same English keys).

- `mr`: English→Kashmiri via MyMemory (langpair en|ks). Google Translate does not expose `ks`
  on the public/mobile API; MyMemory returns Devanagari suitable for the app's Kashmiri tab.
- `roman`: Devanagari → IAST (indic-transliteration), matching other Devanagari-script *_data.js.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time

import requests

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from indic_transliteration.sanscript import DEVANAGARI, IAST, transliterate

ROOT = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = os.path.join(ROOT, "_kashmiri_translate_cache.json")
HINDI_PATH = os.path.join(ROOT, "hindi_data.js")
OUT_PATH = os.path.join(ROOT, "kashmiri_data.js")

MYMEMORY_GET = "https://api.mymemory.translated.net/get"
SESSION = requests.Session()
SESSION.headers.update(
    {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }
)

# Hand-checked Kashmiri (lesson bank); MyMemory often misses low-resource phrasing.
FIX_MAITHILI_MR = "त्स्के छुके मैथिली बोलान?"
FIX_MAITHILI_ROMAN = "Tske chuke maithilī bolāna?"

if os.path.isfile(CACHE_PATH):
    with open(CACHE_PATH, "r", encoding="utf-8") as f:
        cache: dict[str, list[str]] = json.load(f)
else:
    cache = {}

SAVE_EVERY = 50
TRANSLATE_RETRIES = 6
# MyMemory throttling; stay under typical anonymous limits.
SLEEP_BASE = 0.35


def save_cache():
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=0)


def mm_translate(en: str) -> str:
    if not en.strip():
        return ""
    last_err: Exception | None = None
    for attempt in range(TRANSLATE_RETRIES):
        time.sleep(SLEEP_BASE + attempt * 0.45)
        try:
            r = SESSION.get(
                MYMEMORY_GET,
                params={"q": en, "langpair": "en|ks"},
                timeout=60,
            )
            r.raise_for_status()
            data = r.json()
            if data.get("responseStatus") != 200:
                continue
            block = data.get("responseData") or {}
            out = (block.get("translatedText") or "").strip()
            if out and out.lower() != en.strip().lower():
                return out
            if out and out == en:
                return ""
        except Exception as e:
            last_err = e
            print("MyMemory error:", repr(en)[:60], "attempt", attempt + 1, e, flush=True)
    if last_err:
        print("give up:", repr(en)[:72], last_err, flush=True)
    return ""


def romanize_dev(dev_text: str) -> str:
    if not dev_text.strip():
        return ""
    try:
        rom = transliterate(dev_text, DEVANAGARI, IAST)
        if rom and rom[0].islower():
            rom = rom[0].upper() + rom[1:]
        return rom
    except Exception as e:
        print("translit error:", repr(dev_text)[:60], e, flush=True)
        return ""


def prune_identity_cache_entries() -> int:
    bad = [k for k, v in cache.items() if isinstance(v, list) and len(v) >= 1 and v[0] == k]
    for k in bad:
        del cache[k]
    return len(bad)


def translate_pair(en: str) -> tuple[str, str]:
    if en in cache:
        return cache[en][0], cache[en][1]
    ks_txt = mm_translate(en)
    if not ks_txt:
        ks_txt = en
    rom = romanize_dev(ks_txt) if ks_txt != en else ""
    cache[en] = [ks_txt, rom]
    if len(cache) % SAVE_EVERY == 0:
        save_cache()
        print("…cached", len(cache), "strings", flush=True)
    return ks_txt, rom


pat = re.compile(
    r"\{ en: (\"(?:\\.|[^\"\\])*\"), mr: (\"(?:\\.|[^\"\\])*\"), roman: (\"(?:\\.|[^\"\\])*\")(, hint: \"\")? \}"
)


def repl(m: re.Match) -> str:
    en = json.loads(m.group(1))
    ks_t, rom = translate_pair(en)
    hint = m.group(4) or ""
    return (
        "{ en: "
        + json.dumps(en, ensure_ascii=False)
        + ", mr: "
        + json.dumps(ks_t, ensure_ascii=False)
        + ", roman: "
        + json.dumps(rom, ensure_ascii=False)
        + hint
        + " }"
    )


fix_maithili_pat = re.compile(
    r'\{ en: "Do you speak Maithili\?", mr: (\"(?:\\.|[^\"\\])*\"), '
    r'roman: (\"(?:\\.|[^\"\\])*\")(, hint: \"\")? \}'
)


def fix_maithili_question_safe(text: str) -> str:
    def _sub(_m: re.Match) -> str:
        hint = _m.group(3) or ""
        return (
            '{ en: "Do you speak Maithili?", mr: '
            + json.dumps(FIX_MAITHILI_MR, ensure_ascii=False)
            + ", roman: "
            + json.dumps(FIX_MAITHILI_ROMAN, ensure_ascii=False)
            + hint
            + " }"
        )

    return fix_maithili_pat.sub(_sub, text)


def main():
    pruned = prune_identity_cache_entries()
    if pruned:
        save_cache()
        print("pruned identity (untranslated) cache entries:", pruned, flush=True)

    with open(HINDI_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    matches = pat.findall(text)
    print("objects to translate:", len(matches), "(MyMemory en|ks per unique English)", flush=True)

    updated = pat.sub(repl, text)
    updated = updated.replace("const HINDI_PHRASES", "const KASHMIRI_PHRASES")
    updated = updated.replace("const HINDI_DICTIONARY", "const KASHMIRI_DICTIONARY")
    updated = updated.replace("Hindi phrases", "Kashmiri phrases")
    updated = updated.replace("data_hindi.json", "data_kashmiri.json")
    updated = fix_maithili_question_safe(updated)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    save_cache()
    print("wrote", OUT_PATH, "| cache entries:", len(cache), flush=True)


if __name__ == "__main__":
    main()
