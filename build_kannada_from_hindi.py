#!/usr/bin/env python3
"""
Rebuild kannada_data.js to mirror the Hindi/Maithili phrase+word sets (same English keys).
Uses deep-translator (English→Kannada) + indic-transliteration → IAST for `roman` field.
"""
import json
import os
import re
import time

from deep_translator import GoogleTranslator
from indic_transliteration.sanscript import IAST, KANNADA, transliterate

ROOT = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = os.path.join(ROOT, "_kannada_translate_cache.json")
HINDI_PATH = os.path.join(ROOT, "hindi_data.js")
OUT_PATH = os.path.join(ROOT, "kannada_data.js")

translator = GoogleTranslator(source="en", target="kn")

if os.path.isfile(CACHE_PATH):
    with open(CACHE_PATH, "r", encoding="utf-8") as f:
        cache = json.load(f)
else:
    cache: dict[str, list[str]] = {}

SAVE_EVERY = 75


def save_cache():
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=0)


def romanize_kn(kn: str) -> str:
    rom = transliterate(kn, KANNADA, IAST)
    if rom and rom[0].islower():
        rom = rom[0].upper() + rom[1:]
    return rom


def translate_pair(en: str) -> tuple[str, str]:
    if en in cache:
        return cache[en][0], cache[en][1]
    time.sleep(0.08)
    try:
        kn = translator.translate(en)
    except Exception as e:
        print("translate error:", repr(en)[:80], e)
        kn = en
    try:
        rom = romanize_kn(kn)
    except Exception as e:
        print("translit error:", repr(en)[:60], repr(kn)[:60], e)
        rom = ""
    cache[en] = [kn, rom]
    if len(cache) % SAVE_EVERY == 0:
        save_cache()
        print("…cached", len(cache), "strings")
    return kn, rom


pat = re.compile(
    r"\{ en: (\"(?:\\.|[^\"\\])*\"), mr: (\"(?:\\.|[^\"\\])*\"), roman: (\"(?:\\.|[^\"\\])*\")(, hint: \"\")? \}"
)


def repl(m: re.Match) -> str:
    en = json.loads(m.group(1))
    kn, rom = translate_pair(en)
    hint = m.group(4) or ""
    return (
        "{ en: "
        + json.dumps(en, ensure_ascii=False)
        + ", mr: "
        + json.dumps(kn, ensure_ascii=False)
        + ", roman: "
        + json.dumps(rom, ensure_ascii=False)
        + hint
        + " }"
    )


fix_maithili_pat = re.compile(
    r'\{ en: "Do you speak Maithili\?", mr: "((?:\\.|[^"\\])*)", roman: "((?:\\.|[^"\\])*)"(, hint: "")? \}'
)


def fix_maithili_question(text: str) -> str:
    """Keep English key; localize the Kannada question (same pattern as hindi_data.js)."""

    def _sub(m: re.Match) -> str:
        hint = m.group(3) or ""
        kn2 = "ನೀವು ಕನ್ನಡ ಮಾತನಾಡುತ್ತೀರಾ?"
        rom2 = romanize_kn(kn2)
        return (
            '{ en: "Do you speak Maithili?", mr: '
            + json.dumps(kn2, ensure_ascii=False)
            + ", roman: "
            + json.dumps(rom2, ensure_ascii=False)
            + hint
            + " }"
        )

    return fix_maithili_pat.sub(_sub, text)


def main():
    with open(HINDI_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    matches = pat.findall(text)
    print("objects to translate:", len(matches))

    updated = pat.sub(repl, text)
    updated = updated.replace("const HINDI_PHRASES", "const KANNADA_PHRASES")
    updated = updated.replace("const HINDI_DICTIONARY", "const KANNADA_DICTIONARY")
    updated = updated.replace("Hindi phrases", "Kannada phrases")
    updated = updated.replace("data_hindi.json", "data_kannada.json")
    updated = fix_maithili_question(updated)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    save_cache()
    print("wrote", OUT_PATH, "| cache entries:", len(cache))


if __name__ == "__main__":
    main()
