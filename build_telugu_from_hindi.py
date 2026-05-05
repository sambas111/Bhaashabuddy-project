#!/usr/bin/env python3
"""
Rebuild telugu_data.js to mirror the Hindi/Maithili phrase+word sets (same English keys).
Uses deep-translator (English→Telugu) + indic-transliteration → IAST for `roman` field.
"""
import json
import os
import re
import time

from deep_translator import GoogleTranslator
from indic_transliteration.sanscript import IAST, TELUGU, transliterate

ROOT = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = os.path.join(ROOT, "_telugu_translate_cache.json")
HINDI_PATH = os.path.join(ROOT, "hindi_data.js")
OUT_PATH = os.path.join(ROOT, "telugu_data.js")

translator = GoogleTranslator(source="en", target="te")

if os.path.isfile(CACHE_PATH):
    with open(CACHE_PATH, "r", encoding="utf-8") as f:
        cache = json.load(f)
else:
    cache: dict[str, list[str]] = {}

SAVE_EVERY = 75


def save_cache():
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=0)


def romanize_te(te: str) -> str:
    rom = transliterate(te, TELUGU, IAST)
    if rom and rom[0].islower():
        rom = rom[0].upper() + rom[1:]
    return rom


def translate_pair(en: str) -> tuple[str, str]:
    if en in cache:
        return cache[en][0], cache[en][1]
    time.sleep(0.08)
    try:
        te = translator.translate(en)
    except Exception as e:
        print("translate error:", repr(en)[:80], e)
        te = en
    try:
        rom = romanize_te(te)
    except Exception as e:
        print("translit error:", repr(en)[:60], repr(te)[:60], e)
        rom = ""
    cache[en] = [te, rom]
    if len(cache) % SAVE_EVERY == 0:
        save_cache()
        print("…cached", len(cache), "strings")
    return te, rom


pat = re.compile(
    r"\{ en: (\"(?:\\.|[^\"\\])*\"), mr: (\"(?:\\.|[^\"\\])*\"), roman: (\"(?:\\.|[^\"\\])*\")(, hint: \"\")? \}"
)


def repl(m: re.Match) -> str:
    en = json.loads(m.group(1))
    te, rom = translate_pair(en)
    hint = m.group(4) or ""
    return (
        "{ en: "
        + json.dumps(en, ensure_ascii=False)
        + ", mr: "
        + json.dumps(te, ensure_ascii=False)
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
    te2 = "మీరు తెలుగు మాట్లాడగలరా?"
    rom2 = romanize_te(te2)

    def _sub(_m: re.Match) -> str:
        hint = _m.group(3) or ""
        return (
            '{ en: "Do you speak Maithili?", mr: '
            + json.dumps(te2, ensure_ascii=False)
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
    updated = updated.replace("const HINDI_PHRASES", "const TELUGU_PHRASES")
    updated = updated.replace("const HINDI_DICTIONARY", "const TELUGU_DICTIONARY")
    updated = updated.replace("Hindi phrases", "Telugu phrases")
    updated = updated.replace("data_hindi.json", "data_telugu.json")
    updated = fix_maithili_question_safe(updated)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    save_cache()
    print("wrote", OUT_PATH, "| cache entries:", len(cache))


if __name__ == "__main__":
    main()
