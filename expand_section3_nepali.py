# -*- coding: utf-8 -*-
"""Replace lesson tables 543–596 with longer natural English / Nepali / transliteration rows."""
import json
from copy import deepcopy
from pathlib import Path

from section3_nepali_rows import ROWS

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data_nepali.json"


def apply_rows(data: list) -> None:
    for lesson in data:
        lid = lesson.get("id")
        if lid not in ROWS:
            continue
        new_rows = ROWS[lid]
        for block in lesson.get("blocks") or []:
            if block.get("type") != "table":
                continue
            if block.get("headers") != ["English", "Nepali", "Transliteration"]:
                continue
            old = block.get("rows") or []
            if len(old) != len(new_rows):
                raise ValueError(
                    f"Lesson {lid}: expected {len(new_rows)} rows, file has {len(old)}"
                )
            block["rows"] = [list(r) for r in new_rows]


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    data = deepcopy(data)
    apply_rows(data)
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated section 3 lessons (543–596) in", DATA)


if __name__ == "__main__":
    main()
