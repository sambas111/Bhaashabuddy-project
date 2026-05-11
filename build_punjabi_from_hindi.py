#!/usr/bin/env python3
"""
Rebuild punjabi_data.js to mirror the Hindi/Maithili phrase+word sets (same English keys).
Uses deep-translator (English→Punjabi) + indic-transliteration Gurmukhi → IAST for `roman`.
"""
import json
import os
import re
import sys
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from deep_translator import GoogleTranslator
from indic_transliteration.sanscript import GURMUKHI, IAST, transliterate

ROOT = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = os.path.join(ROOT, "_punjabi_translate_cache.json")
HINDI_PATH = os.path.join(ROOT, "hindi_data.js")
OUT_PATH = os.path.join(ROOT, "punjabi_data.js")

translator = GoogleTranslator(source="en", target="pa")

if os.path.isfile(CACHE_PATH):
    with open(CACHE_PATH, "r", encoding="utf-8") as f:
        cache = json.load(f)
else:
    cache: dict[str, list[str]] = {}

SAVE_EVERY = 75
TRANSLATE_RETRIES = 6


def save_cache():
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=0)


def romanize_pa(pa: str) -> str:
    rom = transliterate(pa, GURMUKHI, IAST)
    if rom and rom[0].islower():
        rom = rom[0].upper() + rom[1:]
    return rom


def prune_identity_cache_entries() -> int:
    bad = [k for k, v in cache.items() if isinstance(v, list) and len(v) >= 1 and v[0] == k]
    for k in bad:
        del cache[k]
    return len(bad)


def translate_pair(en: str) -> tuple[str, str]:
    if en in cache:
        return cache[en][0], cache[en][1]
    pa = en
    for attempt in range(TRANSLATE_RETRIES):
        time.sleep(0.1 + attempt * 0.55)
        try:
            pa = translator.translate(en)
            break
        except Exception as e:
            print("translate error:", repr(en)[:72], "attempt", attempt + 1, e, flush=True)
    try:
        rom = romanize_pa(pa)
    except Exception as e:
        print("translit error:", repr(en)[:60], repr(pa)[:60], e, flush=True)
        rom = ""
    cache[en] = [pa, rom]
    if len(cache) % SAVE_EVERY == 0:
        save_cache()
        print("…cached", len(cache), "strings", flush=True)
    return pa, rom


pat = re.compile(
    r"\{ en: (\"(?:\\.|[^\"\\])*\"), mr: (\"(?:\\.|[^\"\\])*\"), roman: (\"(?:\\.|[^\"\\])*\")(, hint: \"\")? \}"
)


def repl(m: re.Match) -> str:
    en = json.loads(m.group(1))
    pa_t, rom = translate_pair(en)
    hint = m.group(4) or ""
    return (
        "{ en: "
        + json.dumps(en, ensure_ascii=False)
        + ", mr: "
        + json.dumps(pa_t, ensure_ascii=False)
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
    pa_q = "ਕੀ ਤੁਸੀ ਪੰਜਾਬੀ ਬੋਲ ਸਕਦੇ ਹੋ?"
    rom_q = romanize_pa(pa_q)

    def _sub(_m: re.Match) -> str:
        hint = _m.group(3) or ""
        return (
            '{ en: "Do you speak Maithili?", mr: '
            + json.dumps(pa_q, ensure_ascii=False)
            + ", roman: "
            + json.dumps(rom_q, ensure_ascii=False)
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
    print("objects to translate:", len(matches), flush=True)

    updated = pat.sub(repl, text)
    updated = updated.replace("const HINDI_PHRASES", "const PUNJABI_PHRASES")
    updated = updated.replace("const HINDI_DICTIONARY", "const PUNJABI_DICTIONARY")
    updated = updated.replace("Hindi phrases", "Punjabi phrases")
    updated = updated.replace("data_hindi.json", "data_punjabi.json")
    updated = fix_maithili_question_safe(updated)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    save_cache()
    print("wrote", OUT_PATH, "| cache entries:", len(cache), flush=True)


if __name__ == "__main__":
    main()
