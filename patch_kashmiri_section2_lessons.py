# -*- coding: utf-8 -*-
"""
Populate Kashmiri lessons 510–542 (section 2.1–2.33): ~15 rows per English/Kashmiri table (from kashmiri_s2_lesson_data_a/b).

Content is topic-aligned per sublesson; English glosses match the Kashmiri line. Primary
linguistic source: O. N. Koul, *The Kashmiri Language: A Grammatical Sketch*
(ikashmir.net/onkoul/pdf/TheKashmiriLanguage.pdf), with phrasebook lines (Omniglot /
Wikivoyage) for natural fillers.

Re-run after generate_kashmiri_data.py if that overwrites JSON.

Run: py -3 patch_kashmiri_section2_lessons.py
"""
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

from kashmiri_s2_data import PATCH

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data_kashmiri.json"


def patch_block(block: dict, lesson_id: int) -> bool:
    heading = block.get("heading") or ""
    m = PATCH.get(lesson_id)
    if not m or heading not in m:
        return False
    if block.get("headers") != ["English", "Kashmiri", "Transliteration"]:
        return False
    rows = m[heading]
    block["rows"] = [list(r) for r in rows]
    return True


def patch_lesson(lesson: dict) -> None:
    lid = lesson.get("id")
    if lid not in PATCH:
        return
    for key in ("tables", "blocks"):
        arr = lesson.get(key)
        if not arr:
            continue
        for block in arr:
            if isinstance(block, dict):
                patch_block(block, lid)


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    data = deepcopy(data)
    n = 0
    for lesson in data:
        before = json.dumps(lesson, ensure_ascii=False, sort_keys=True)
        patch_lesson(lesson)
        if json.dumps(lesson, ensure_ascii=False, sort_keys=True) != before:
            n += 1
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Patched", n, "lessons in", DATA)


if __name__ == "__main__":
    main()
