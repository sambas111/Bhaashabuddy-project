#!/usr/bin/env python3
"""
Batch translate to all 22 Indic languages.
Uses translate_config.yaml for backend. Creates data_{lang}.json, phrases_{lang}.json, dictionary_{lang}.json for each.

Usage:
  python translate_all.py                    # All languages
  python translate_all.py --languages kannada,tamil,telugu
  python translate_all.py --limit 2         # Test with 2 chapters
"""

import argparse
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent

INDIC_LANGUAGES = [
    "kannada", "tamil", "telugu", "hindi", "gujarati", "bengali", "malayalam",
    "marathi", "odia", "punjabi", "assamese", "nepali", "sanskrit", "urdu",
    "sindhi", "konkani", "maithili", "manipuri", "bodo", "dogri", "kashmiri", "santali"
]


def main():
    parser = argparse.ArgumentParser(description="Batch translate to multiple languages")
    parser.add_argument("--languages", "-l", help="Comma-separated list (default: all)")
    parser.add_argument("--limit", "-n", type=int, help="Limit chapters per language (for testing)")
    parser.add_argument("--backend", "-b", default="groq", help="groq | indic_trans2")
    parser.add_argument("--phrases", action="store_true", default=True, help="Include phrases (default: try to load)")
    parser.add_argument("--no-phrases", action="store_true", help="Skip phrases")
    parser.add_argument("--dictionary", action="store_true", default=True, help="Include dictionary")
    parser.add_argument("--no-dictionary", action="store_true", help="Skip dictionary")
    args = parser.parse_args()

    langs = args.languages.split(",") if args.languages else INDIC_LANGUAGES
    langs = [l.strip().lower() for l in langs if l.strip()]

    phrases_opt = [] if args.no_phrases else ["-p", "phrases_marathi.json"]
    dict_opt = [] if args.no_dictionary else ["-d", "dictionary_marathi.json"]

    for lang in langs:
        if lang == "marathi":
            print(f"Skipping {lang} (source language)")
            continue
        print(f"\n=== Translating to {lang} ===")
        cmd = [sys.executable, str(BASE / "translate_pipeline.py"), "-t", lang, "-b", args.backend]
        if args.limit:
            cmd.extend(["--limit", str(args.limit)])
        cmd.extend(phrases_opt)
        cmd.extend(dict_opt)
        subprocess.run(cmd, cwd=BASE)
    print("\nDone.")


if __name__ == "__main__":
    main()
