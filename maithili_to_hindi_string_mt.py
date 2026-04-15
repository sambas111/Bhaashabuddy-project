#!/usr/bin/env python3
"""
Build data_hindi.json from data_maithili.json by translating unique string values
that contain Devanagari (Google Translate via deep-translator). English-only strings
get Maithili→Hindi label fixes only. Preserves JSON structure.

Usage:
  python maithili_to_hindi_string_mt.py
  python maithili_to_hindi_string_mt.py --limit-strings 80
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

BASE = Path(__file__).parent.resolve()
SRC = BASE / "data_maithili.json"
OUT = BASE / "data_hindi.json"

DEVA = re.compile(r"[\u0900-\u097F]")


def walk_collect(obj, acc: set[str]):
    if isinstance(obj, str):
        acc.add(obj)
    elif isinstance(obj, dict):
        for v in obj.values():
            walk_collect(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            walk_collect(v, acc)


def walk_replace(obj, mapping: dict[str, str]):
    if isinstance(obj, str):
        return mapping.get(obj, obj)
    if isinstance(obj, dict):
        return {k: walk_replace(v, mapping) for k, v in obj.items()}
    if isinstance(obj, list):
        return [walk_replace(v, mapping) for v in obj]
    return obj


def label_normalize(s: str) -> str:
    for old, new in [
        ("Maithili", "Hindi"),
        ("मैथिली", "हिन्दी"),
        ("(Maithili)", "(Hindi)"),
    ]:
        s = s.replace(old, new)
    return s


def should_translate(s: str) -> bool:
    s = s.strip()
    if not s:
        return False
    if not DEVA.search(s):
        return False
    if s.startswith("http://") or s.startswith("https://"):
        return False
    return True


def map_string(s: str, mapping_tr: dict[str, str]) -> str:
    ns = label_normalize(s)
    if should_translate(ns):
        return mapping_tr.get(ns, ns)
    return ns


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=SRC)
    parser.add_argument("--output", type=Path, default=OUT)
    parser.add_argument("--limit-strings", type=int, default=0, help="Max Devanagari strings (0=all)")
    parser.add_argument("--sleep", type=float, default=0.25)
    args = parser.parse_args()

    try:
        from deep_translator import GoogleTranslator
    except ImportError:
        print("pip install deep-translator", file=sys.stderr)
        sys.exit(1)

    data = json.loads(args.input.read_text(encoding="utf-8"))
    unique: set[str] = set()
    for ch in data:
        walk_collect(ch, unique)

    norm_set = {label_normalize(s) for s in unique}
    to_translate = sorted(ns for ns in norm_set if should_translate(ns))
    if args.limit_strings:
        to_translate = to_translate[: args.limit_strings]

    print(f"Translating {len(to_translate)} unique Devanagari strings to Hindi...")

    tr = GoogleTranslator(source="auto", target="hi")
    mapping_tr: dict[str, str] = {}
    for i, s in enumerate(to_translate):
        if i % 100 == 0:
            print(f"  {i}/{len(to_translate)}")
        try:
            hi = tr.translate(s)
            mapping_tr[s] = hi if hi else s
        except Exception as e:
            print(f"  warn: {e!r}", file=sys.stderr)
            mapping_tr[s] = s
        time.sleep(args.sleep)

    per_original: dict[str, str] = {}
    for s in unique:
        per_original[s] = map_string(s, mapping_tr)

    out_data = walk_replace(data, per_original)
    args.output.write_text(json.dumps(out_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
