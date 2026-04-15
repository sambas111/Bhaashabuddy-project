#!/usr/bin/env python3
"""
Translate data_maithili.json lessons to standard Hindi (Devanagari + roman),
preserving English and JSON shape. Uses Groq (same stack as translate_pipeline.py).

Usage:
  set GROQ_API_KEY=...
  python translate_maithili_lessons_to_hindi.py
  python translate_maithili_lessons_to_hindi.py --limit 3
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

BASE = Path(__file__).parent.resolve()
INPUT_FILE = BASE / "data_maithili.json"
OUTPUT_FILE = BASE / "data_hindi.json"


def load_config():
    config_path = BASE / "translate_config.yaml"
    if not config_path.exists():
        return {}
    try:
        import yaml

        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except ImportError:
        return {}


def _prompt(chapter_json_str: str) -> str:
    return f"""You are a translator. You receive ONE lesson chapter as JSON from a Maithili language course. Your output must be the SAME lesson in structure, with only these replacements:

WHAT TO DO:
- Keep every English sentence, phrase, and word exactly as in the input. Do not translate English. Do not add any new English.
- Replace Maithili Devanagari with standard Hindi Devanagari (natural Hindi grammar and vocabulary).
- Replace Maithili-specific roman transliteration with Hindi IAST-style romanization matching the Hindi you wrote.
- In table headers and labels, use "Hindi" instead of "Maithili" where the input refers to the Maithili language column.

WHAT NOT TO DO:
- Do not add explanations, summaries, or commentary.
- Do not change "id" values. Keep the same keys, same number of blocks, tables, rows, and columns.
- Do not remove or add array elements.

OUTPUT: Return ONLY the complete chapter as a single valid JSON object. No markdown fences, no other text.

INPUT CHAPTER (JSON):
{chapter_json_str}

OUTPUT (JSON only):"""


def translate_chapter_with_groq(chapter: dict, model: str):
    try:
        from groq import Groq
    except ImportError:
        print("Install groq: pip install groq", file=sys.stderr)
        sys.exit(1)
    import os

    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("Set GROQ_API_KEY environment variable", file=sys.stderr)
        sys.exit(1)
    client = Groq(api_key=api_key)
    chapter_str = json.dumps(chapter, ensure_ascii=False, indent=2)
    prompt = _prompt(chapter_str)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    out = resp.choices[0].message.content.strip()
    if out.startswith("```"):
        out = re.sub(r"^```(?:json)?\s*", "", out)
        out = re.sub(r"\s*```\s*$", "", out)
    return json.loads(out)


def offline_maithili_to_hindi_stub(chapter: dict) -> dict:
    """When Groq is unavailable: copy chapter and replace Maithili→Hindi labels only (partial)."""
    s = json.dumps(chapter, ensure_ascii=False)
    for old, new in [
        ("Maithili", "Hindi"),
        ("मैथिली", "हिन्दी"),
        ("(Maithili)", "(Hindi)"),
        ("Maithili (", "Hindi ("),
    ]:
        s = s.replace(old, new)
    return json.loads(s)


def main():
    config = load_config()
    parser = argparse.ArgumentParser(description="Maithili lessons → Hindi JSON (Groq)")
    parser.add_argument("--input", "-i", type=Path, default=INPUT_FILE)
    parser.add_argument("--output", "-o", type=Path, default=OUTPUT_FILE)
    parser.add_argument("--limit", "-n", type=int, help="Translate only first N chapters")
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Skip Groq; copy Maithili with label substitutions only (not full translation)",
    )
    parser.add_argument("--sleep", type=float, default=0.35, help="Seconds between Groq calls")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Input not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    if args.limit:
        data = data[: args.limit]

    model = config.get("groq_model", "llama-3.3-70b-versatile")

    if args.offline:
        print("Offline mode: label substitution only (no Groq).")
        out = [offline_maithili_to_hindi_stub(ch) for ch in data]
    else:
        import os

        if not os.environ.get("GROQ_API_KEY"):
            print("GROQ_API_KEY not set; using offline stub for all chapters.", file=sys.stderr)
            out = [offline_maithili_to_hindi_stub(ch) for ch in data]
        else:
            print(f"Translating {len(data)} chapters to Hindi with Groq ({model})...")
            out = []
            for i, ch in enumerate(data):
                cid = ch.get("id")
                print(f"  {i + 1}/{len(data)} (id={cid})...")
                try:
                    tr = translate_chapter_with_groq(ch, model=model)
                    out.append(tr if tr is not None else offline_maithili_to_hindi_stub(ch))
                except Exception as e:
                    print(f"  Error id={cid}: {e}; using offline stub", file=sys.stderr)
                    out.append(offline_maithili_to_hindi_stub(ch))
                if args.sleep > 0:
                    time.sleep(args.sleep)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Saved {len(out)} chapters to {args.output}")


if __name__ == "__main__":
    main()
