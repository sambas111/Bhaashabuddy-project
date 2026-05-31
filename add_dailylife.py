#!/usr/bin/env python3
"""
Insert a cleaned "Daily Life" category block into a *_data.js source file
(Hindi or Maithili). Reads _dailylife_clean.json, translates English -> target
script via Google, romanizes Devanagari -> IAST, and adds:
  - dailylife_1..N to <CONST>_PHRASES   (phrase rows, with hint)
  - dailylife_1..M to <CONST>_DICTIONARY (word rows, no hint)

Usage: python add_dailylife.py hindi|maithili
"""
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

CONFIG = {
    "hindi": dict(code="hi", const="HINDI", file="hindi_data.js", cache="_dailylife_hi_cache.json"),
    "maithili": dict(code="mai", const="MAITHILI", file="maithili_data.js", cache="_dailylife_mai_cache.json"),
}

PHRASE_CAP = 700
WORD_CAP = 300
CHUNK = 30
COLOR = "#553C9A"
ICON = "\U0001F3E0"  # 🏠
RETRIES = 6


def romanize(dev: str) -> str:
    rom = transliterate(dev, DEVANAGARI, IAST)
    if rom and rom[0].islower():
        rom = rom[0].upper() + rom[1:]
    return rom


def main():
    lang = sys.argv[1]
    cfg = CONFIG[lang]
    translator = GoogleTranslator(source="en", target=cfg["code"])
    cache_path = os.path.join(ROOT, cfg["cache"])
    cache = {}
    if os.path.isfile(cache_path):
        cache = json.load(open(cache_path, encoding="utf-8"))

    dl = json.load(open(os.path.join(ROOT, "_dailylife_clean.json"), encoding="utf-8"))
    phrases_en = dl["phrases"][:PHRASE_CAP]
    words_en = dl["words"][:WORD_CAP]
    print(f"{lang}: {len(phrases_en)} phrases + {len(words_en)} words")

    def save():
        json.dump(cache, open(cache_path, "w", encoding="utf-8"), ensure_ascii=False, indent=0)

    def translate(en: str):
        if en in cache:
            return cache[en][0], cache[en][1]
        mr = en
        for attempt in range(RETRIES):
            time.sleep(0.1 + attempt * 0.5)
            try:
                mr = translator.translate(en)
                break
            except Exception as e:
                print("translate error:", repr(en)[:60], attempt + 1, e, flush=True)
        rom = romanize(mr) if mr and mr != en else ""
        cache[en] = [mr, rom]
        if len(cache) % 50 == 0:
            save()
            print("…cached", len(cache), flush=True)
        return mr, rom

    def fmt_row(en, with_hint):
        mr, rom = translate(en)
        base = (
            "      { en: " + json.dumps(en, ensure_ascii=False)
            + ", mr: " + json.dumps(mr, ensure_ascii=False)
            + ", roman: " + json.dumps(rom, ensure_ascii=False)
        )
        return base + (', hint: "" }' if with_hint else " }")

    def build_blocks(items, with_hint, kind):
        blocks = []
        for i in range(0, len(items), CHUNK):
            chunk = items[i:i + CHUNK]
            setno = i // CHUNK + 1
            rows = ",\n".join(fmt_row(en, with_hint) for en in chunk)
            header = (
                f"  dailylife_{setno}: {{\n"
                f"    name: \"Daily Life Set {setno}\",\n"
                f"    color: \"{COLOR}\",\n"
                f"    icon: \"{ICON}\",\n"
                f"    {kind}: [\n{rows}\n    ]\n  }}"
            )
            blocks.append(header)
        return blocks

    phrase_blocks = build_blocks(phrases_en, True, "phrases")
    word_blocks = build_blocks(words_en, False, "words")
    save()

    path = os.path.join(ROOT, cfg["file"])
    content = open(path, encoding="utf-8").read()
    const = cfg["const"]

    # Insert phrase blocks before the close of <CONST>_PHRASES
    phrases_anchor = f"\n  }}\n}};\n\nconst {const}_DICTIONARY = {{"
    if phrases_anchor not in content:
        raise SystemExit("phrases anchor not found in " + cfg["file"])
    phrases_repl = "\n  },\n" + ",\n".join(phrase_blocks) + f"\n}};\n\nconst {const}_DICTIONARY = {{"
    content = content.replace(phrases_anchor, phrases_repl, 1)

    # Insert word blocks before the final close of <CONST>_DICTIONARY (last "  }\n};")
    idx = content.rfind("\n  }\n};")
    if idx == -1:
        raise SystemExit("dictionary anchor not found in " + cfg["file"])
    words_repl = "\n  },\n" + ",\n".join(word_blocks) + "\n};"
    content = content[:idx] + words_repl + content[idx + len("\n  }\n};"):]

    open(path, "w", encoding="utf-8").write(content)
    save()
    print(f"updated {cfg['file']}: +{len(phrase_blocks)} phrase sets, +{len(word_blocks)} word sets")


if __name__ == "__main__":
    main()
