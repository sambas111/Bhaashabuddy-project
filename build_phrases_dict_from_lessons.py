# -*- coding: utf-8 -*-
"""
Build *_data.js PHRASES + DICTIONARY sections from data_*.json lesson tables.
Used for languages without hand-curated phrasebooks or to backfill sparse sets.
"""
from __future__ import annotations

import json
import os
import re
import textwrap
from typing import Iterator

ROOT = os.path.dirname(os.path.abspath(__file__))

# (output_js_basename, data_json, const_prefix)
TARGETS = [
    ("nepali_data.js", "data_nepali.json", "NEPALI"),
    ("kashmiri_data.js", "data_kashmiri.json", "KASHMIRI"),
    ("punjabi_data.js", "data_punjabi.json", "PUNJABI"),
    ("bengali_data.js", "data_bengali.json", "BENGALI"),
    ("assamese_data.js", "data_assamese.json", "ASSAMESE"),
]


def looks_english(s: str) -> bool:
    s = s.strip()
    if len(s) < 2:
        return False
    # English row usually starts with Latin letter or digit
    return bool(re.match(r"^[A-Za-z0-9\"'(\[]", s))


def is_phrase_en(en: str) -> bool:
    """Treat fuller lines as phrasebook entries; gloss words go to dictionary."""
    en = en.strip()
    wc = len(en.split())
    if len(en) > 45:
        return True
    if wc >= 5:
        return True
    if en.endswith("?") and wc >= 4:
        return True
    if en.endswith(".") and wc >= 4:
        return True
    return False


def iter_rows_from_lesson(lesson: dict) -> Iterator[tuple[str, str, str]]:
    for tbl in lesson.get("tables") or []:
        rows = tbl.get("rows") or []
        for row in rows:
            if len(row) < 3:
                continue
            en, loc, rom = str(row[0]).strip(), str(row[1]).strip(), str(row[2]).strip()
            if not looks_english(en) or not loc:
                continue
            yield en, loc, rom

    for blk in lesson.get("blocks") or []:
        if blk.get("type") != "table":
            continue
        rows = blk.get("rows") or []
        for row in rows:
            if len(row) < 3:
                continue
            en, loc, rom = str(row[0]).strip(), str(row[1]).strip(), str(row[2]).strip()
            if not looks_english(en) or not loc:
                continue
            yield en, loc, rom


def collect_triplets(path: str) -> tuple[list[tuple[str, str, str]], list[tuple[str, str, str]]]:
    """Preserve lesson order (by chapter id) for natural phrase progression."""
    data = json.load(open(path, encoding="utf-8"))
    try:
        data = sorted(data, key=lambda x: int(x.get("id") or 0))
    except (TypeError, ValueError):
        pass
    seen: set[str] = set()
    phrases: list[tuple[str, str, str]] = []
    words: list[tuple[str, str, str]] = []
    for lesson in data:
        for en, loc, rom in iter_rows_from_lesson(lesson):
            key = en.lower()
            if key in seen:
                continue
            seen.add(key)
            if is_phrase_en(en):
                phrases.append((en, loc, rom))
            else:
                words.append((en, loc, rom))
    return phrases, words


PHRASE_CATS = [
    ("greetings_1", "Greetings", "#2B6CB0", "👋"),
    ("travel_1", "Travel", "#38A169", "🚌"),
    ("food_1", "Food", "#DD6B20", "🍛"),
    ("daily_1", "Daily life", "#805AD5", "🏠"),
    ("shopping_1", "Shopping", "#D69E2E", "🛒"),
    ("emergency_1", "Emergency", "#E53E3E", "🚨"),
]

DICT_SECS = [
    ("basics_1", "Basic words"),
    ("family_1", "Family"),
    ("verbs_1", "Common verbs"),
    ("nature_1", "Nature"),
]


def chunk_evenly(items: list, n_buckets: int, per_bucket: int) -> list[list]:
    """Take first n_buckets * per_bucket items, split into buckets."""
    cap = n_buckets * per_bucket
    items = items[:cap]
    out = [[] for _ in range(n_buckets)]
    for i, it in enumerate(items):
        out[i % n_buckets].append(it)
    return out


def js_escape_string(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def build_js(const: str, phrases: list[tuple], words: list[tuple]) -> str:
    per_cat = 16
    ph_buckets = chunk_evenly(phrases, len(PHRASE_CATS), per_cat)
    wd_buckets = chunk_evenly(words, len(DICT_SECS), 16)

    lines = [
        f"// Auto-generated from lesson JSON — Phrases & Words tabs",
        f"const {const}_PHRASES = " + "{",
    ]
    for i, (cid, title, color, icon) in enumerate(PHRASE_CATS):
        lines.append(f"  {cid}: {{")
        lines.append(f'    name: {js_escape_string(title)},')
        lines.append(f'    color: {js_escape_string(color)},')
        lines.append(f'    icon: {js_escape_string(icon)},')
        lines.append("    phrases: [")
        for en, mr, rom in ph_buckets[i]:
            lines.append(
                "      { en: "
                + js_escape_string(en)
                + ", mr: "
                + js_escape_string(mr)
                + ", roman: "
                + js_escape_string(rom)
                + ', hint: "" },'
            )
        lines.append("    ]")
        lines.append("  },")
    lines.append("};")
    lines.append("")
    lines.append(f"const {const}_DICTIONARY = " + "{")
    for i, (sid, sname) in enumerate(DICT_SECS):
        lines.append(f"  {sid}: {{")
        lines.append(f'    name: {js_escape_string(sname)},')
        lines.append("    words: [")
        for en, mr, rom in wd_buckets[i]:
            lines.append(
                "      { en: "
                + js_escape_string(en)
                + ", mr: "
                + js_escape_string(mr)
                + ", roman: "
                + js_escape_string(rom)
                + " },"
            )
        lines.append("    ]")
        lines.append("  },")
    lines.append("};")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    for out_name, data_name, const in TARGETS:
        path = os.path.join(ROOT, data_name)
        if not os.path.isfile(path):
            print("skip missing", path)
            continue
        phrases, words = collect_triplets(path)
        # If few "phrases" by heuristic, promote longer word rows
        if len(phrases) < 40:
            extra = [w for w in words if len(w[0].split()) >= 3]
            for t in extra:
                if t not in phrases:
                    phrases.append(t)
            words = [w for w in words if w not in phrases]
        text = build_js(const, phrases, words)
        out_path = os.path.join(ROOT, out_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(out_name, "phrases unique:", len(phrases), "words unique:", len(words), "->", out_path)


if __name__ == "__main__":
    main()
