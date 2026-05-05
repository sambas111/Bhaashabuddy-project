#!/usr/bin/env python3
"""
Rebuild bengali_data.js to mirror the Hindi/Maithili phrase+word sets (same English keys).
Uses deep-translator (English→Bengali) + indic-transliteration Bengali → IAST for `roman`.
"""
import json
import os
import re
import time

from deep_translator import GoogleTranslator
from indic_transliteration.sanscript import BENGALI, IAST, transliterate

ROOT = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = os.path.join(ROOT, "_bengali_translate_cache.json")
HINDI_PATH = os.path.join(ROOT, "hindi_data.js")
OUT_PATH = os.path.join(ROOT, "bengali_data.js")

translator = GoogleTranslator(source="en", target="bn")

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


def romanize_bn(bn: str) -> str:
    rom = transliterate(bn, BENGALI, IAST)
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
    bn = en
    for attempt in range(TRANSLATE_RETRIES):
        time.sleep(0.1 + attempt * 0.55)
        try:
            bn = translator.translate(en)
            break
        except Exception as e:
            print("translate error:", repr(en)[:72], "attempt", attempt + 1, e)
    try:
        rom = romanize_bn(bn)
    except Exception as e:
        print("translit error:", repr(en)[:60], repr(bn)[:60], e)
        rom = ""
    cache[en] = [bn, rom]
    if len(cache) % SAVE_EVERY == 0:
        save_cache()
        print("…cached", len(cache), "strings")
    return bn, rom


pat = re.compile(
    r"\{ en: (\"(?:\\.|[^\"\\])*\"), mr: (\"(?:\\.|[^\"\\])*\"), roman: (\"(?:\\.|[^\"\\])*\")(, hint: \"\")? \}"
)


def repl(m: re.Match) -> str:
    en = json.loads(m.group(1))
    bn_t, rom = translate_pair(en)
    hint = m.group(4) or ""
    return (
        "{ en: "
        + json.dumps(en, ensure_ascii=False)
        + ", mr: "
        + json.dumps(bn_t, ensure_ascii=False)
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
    bn_q = "আপনি কি বাংলা বলতে পারেন?"
    rom_q = romanize_bn(bn_q)

    def _sub(_m: re.Match) -> str:
        hint = _m.group(3) or ""
        return (
            '{ en: "Do you speak Maithili?", mr: '
            + json.dumps(bn_q, ensure_ascii=False)
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
        print("pruned identity (untranslated) cache entries:", pruned)

    with open(HINDI_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    matches = pat.findall(text)
    print("objects to translate:", len(matches))

    updated = pat.sub(repl, text)
    updated = updated.replace("const HINDI_PHRASES", "const BENGALI_PHRASES")
    updated = updated.replace("const HINDI_DICTIONARY", "const BENGALI_DICTIONARY")
    updated = updated.replace("Hindi phrases", "Bengali phrases")
    updated = updated.replace("data_hindi.json", "data_bengali.json")
    updated = fix_maithili_question_safe(updated)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    save_cache()
    print("wrote", OUT_PATH, "| cache entries:", len(cache))


if __name__ == "__main__":
    main()
