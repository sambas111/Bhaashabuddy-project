#!/usr/bin/env python3
"""
Rebuild sindhi_data.js to mirror the Hindi/Maithili phrase+word sets (same English keys).
- `mr`: English→Sindhi (Arabic script) via Google Translate (`sd`).
- `roman`: Sindhi→Hindi (Devanagari) → IAST (same bridge pattern as Urdu).
"""
from __future__ import annotations

import json
import os
import re
import sys
import time

from deep_translator import GoogleTranslator
from indic_transliteration.sanscript import DEVANAGARI, IAST, transliterate

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = os.path.join(ROOT, "_sindhi_translate_cache.json")
HINDI_PATH = os.path.join(ROOT, "hindi_data.js")
OUT_PATH = os.path.join(ROOT, "sindhi_data.js")

translator_en_sd = GoogleTranslator(source="en", target="sd")
translator_sd_hi = GoogleTranslator(source="sd", target="hi")

if os.path.isfile(CACHE_PATH):
    with open(CACHE_PATH, "r", encoding="utf-8") as f:
        cache: dict[str, list[str]] = json.load(f)
else:
    cache = {}

SAVE_EVERY = 75
TRANSLATE_RETRIES = 6

FIX_MAITHILI_SD = "ڇا تون ميٿلي ڳالهائين ٿو؟"
FIX_MAITHILI_ROMAN = "Kyā āpa maithilī bolate haiṃ?"


def save_cache():
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=0)


def roman_from_sd(sd_text: str) -> str:
    if not (sd_text and sd_text.strip()):
        return ""
    hi = ""
    for attempt in range(TRANSLATE_RETRIES):
        time.sleep(0.06 + attempt * 0.35)
        try:
            hi = translator_sd_hi.translate(sd_text)
            break
        except Exception as e:
            print("sd->hi error:", repr(sd_text)[:50], "attempt", attempt + 1, e, flush=True)
    if not hi.strip():
        return ""
    try:
        rom = transliterate(hi, DEVANAGARI, IAST)
        if rom and rom[0].islower():
            rom = rom[0].upper() + rom[1:]
        return rom
    except Exception as e:
        print("roman translit error:", repr(sd_text)[:40], e, flush=True)
        return ""


def prune_identity_cache_entries() -> int:
    bad = [k for k, v in cache.items() if isinstance(v, list) and len(v) >= 1 and v[0] == k]
    for k in bad:
        del cache[k]
    return len(bad)


def translate_pair(en: str) -> tuple[str, str]:
    if en in cache:
        return cache[en][0], cache[en][1]
    sd = en
    for attempt in range(TRANSLATE_RETRIES):
        time.sleep(0.08 + attempt * 0.45)
        try:
            sd = translator_en_sd.translate(en)
            break
        except Exception as e:
            print("translate error:", repr(en)[:72], "attempt", attempt + 1, e, flush=True)
    rom = roman_from_sd(sd) if sd != en else ""
    cache[en] = [sd, rom]
    if len(cache) % SAVE_EVERY == 0:
        save_cache()
        print("…cached", len(cache), "strings", flush=True)
    return sd, rom


pat = re.compile(
    r"\{ en: (\"(?:\\.|[^\"\\])*\"), mr: (\"(?:\\.|[^\"\\])*\"), roman: (\"(?:\\.|[^\"\\])*\")(, hint: \"\")? \}"
)


def repl(m: re.Match) -> str:
    en = json.loads(m.group(1))
    sd_t, rom = translate_pair(en)
    hint = m.group(4) or ""
    return (
        "{ en: "
        + json.dumps(en, ensure_ascii=False)
        + ", mr: "
        + json.dumps(sd_t, ensure_ascii=False)
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
            + json.dumps(FIX_MAITHILI_SD, ensure_ascii=False)
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
    print("objects to translate:", len(matches), "(en→sd + sd→hi per unique English)", flush=True)

    updated = pat.sub(repl, text)
    updated = updated.replace("const HINDI_PHRASES", "const SINDHI_PHRASES")
    updated = updated.replace("const HINDI_DICTIONARY", "const SINDHI_DICTIONARY")
    updated = updated.replace("Hindi phrases", "Sindhi phrases")
    updated = updated.replace("data_hindi.json", "data_sindhi.json")
    updated = fix_maithili_question_safe(updated)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    save_cache()
    print("wrote", OUT_PATH, "| cache entries:", len(cache), flush=True)


if __name__ == "__main__":
    main()
