#!/usr/bin/env python3
"""
Rebuild santali_data.js to mirror the Hindi/Maithili phrase+word sets (same English keys).

- `mr`: English→Santali (Ol Chiki) via Google Translate mobile endpoint (?tl=sat). The
  `deep_translator` package does not register `sat`; we call the same URL it uses.
- `roman`: Santali→Hindi (Devanagari) on the same endpoint, then Devanagari→IAST.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from indic_transliteration.sanscript import DEVANAGARI, IAST, transliterate

ROOT = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = os.path.join(ROOT, "_santali_translate_cache.json")
HINDI_PATH = os.path.join(ROOT, "hindi_data.js")
OUT_PATH = os.path.join(ROOT, "santali_data.js")

SESSION = requests.Session()
SESSION.headers.update(
    {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }
)

GOOGLE_M = "https://translate.google.com/m"

# Hand-checked Ol Chiki + IAST-via-Hindi for the shared English key (stable if Google drifts)
FIX_MAITHILI_SAT = "ᱪᱮᱫ ᱟᱢ ᱥᱟᱱᱛᱟᱞᱤ ᱨᱚᱲ ᱮᱢ ᱵᱟᱰᱟᱭᱟ?"
FIX_MAITHILI_ROMAN = "Kyā āpa saṃtālī bolate haiṃ?"

if os.path.isfile(CACHE_PATH):
    with open(CACHE_PATH, "r", encoding="utf-8") as f:
        cache: dict[str, list[str]] = json.load(f)
else:
    cache = {}

SAVE_EVERY = 75
TRANSLATE_RETRIES = 6


def save_cache():
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=0)


def g_translate(sl: str, tl: str, text: str) -> str:
    if not text.strip():
        return ""
    r = SESSION.get(
        GOOGLE_M,
        params={"sl": sl, "tl": tl, "q": text},
        timeout=45,
    )
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    el = soup.find("div", class_="t0") or soup.find("div", class_="result-container")
    if not el:
        return ""
    return el.get_text(strip=True)


def roman_from_sat(sat_text: str) -> str:
    if not sat_text.strip():
        return ""
    hi = ""
    for attempt in range(TRANSLATE_RETRIES):
        time.sleep(0.06 + attempt * 0.35)
        try:
            hi = g_translate("sat", "hi", sat_text)
            if hi:
                break
        except Exception as e:
            print("sat->hi error:", repr(sat_text)[:45], "attempt", attempt + 1, e, flush=True)
    if not hi.strip():
        return ""
    try:
        rom = transliterate(hi, DEVANAGARI, IAST)
        if rom and rom[0].islower():
            rom = rom[0].upper() + rom[1:]
        return rom
    except Exception as e:
        print("roman translit:", e, flush=True)
        return ""


def prune_identity_cache_entries() -> int:
    bad = [k for k, v in cache.items() if isinstance(v, list) and len(v) >= 1 and v[0] == k]
    for k in bad:
        del cache[k]
    return len(bad)


def translate_pair(en: str) -> tuple[str, str]:
    if en in cache:
        return cache[en][0], cache[en][1]
    sat = en
    for attempt in range(TRANSLATE_RETRIES):
        time.sleep(0.1 + attempt * 0.45)
        try:
            sat = g_translate("en", "sat", en)
            if sat:
                break
        except Exception as e:
            print("translate error:", repr(en)[:72], "attempt", attempt + 1, e, flush=True)
    if sat == en:
        rom = ""
    else:
        rom = roman_from_sat(sat)
    cache[en] = [sat, rom]
    if len(cache) % SAVE_EVERY == 0:
        save_cache()
        print("…cached", len(cache), "strings", flush=True)
    return sat, rom


pat = re.compile(
    r"\{ en: (\"(?:\\.|[^\"\\])*\"), mr: (\"(?:\\.|[^\"\\])*\"), roman: (\"(?:\\.|[^\"\\])*\")(, hint: \"\")? \}"
)


def repl(m: re.Match) -> str:
    en = json.loads(m.group(1))
    sat_t, rom = translate_pair(en)
    hint = m.group(4) or ""
    return (
        "{ en: "
        + json.dumps(en, ensure_ascii=False)
        + ", mr: "
        + json.dumps(sat_t, ensure_ascii=False)
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
            + json.dumps(FIX_MAITHILI_SAT, ensure_ascii=False)
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
    print("objects to translate:", len(matches), "(en→sat + sat→hi per unique English)", flush=True)

    updated = pat.sub(repl, text)
    updated = updated.replace("const HINDI_PHRASES", "const SANTALI_PHRASES")
    updated = updated.replace("const HINDI_DICTIONARY", "const SANTALI_DICTIONARY")
    updated = updated.replace("Hindi phrases", "Santali phrases")
    updated = updated.replace("data_hindi.json", "data_santali.json")
    updated = fix_maithili_question_safe(updated)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    save_cache()
    print("wrote", OUT_PATH, "| cache entries:", len(cache), flush=True)


if __name__ == "__main__":
    main()
