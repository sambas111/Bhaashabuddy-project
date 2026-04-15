#!/usr/bin/env python3
"""Populate Bodo lessons (chapter IDs 501–662) in data_bodo.json."""
import json
from pathlib import Path

from bodo_lessons_s1 import LESSONS_S1
from bodo_lessons_s2a import LESSONS_S2A
from bodo_lessons_s2b import LESSONS_S2B
from bodo_lessons_s3a import LESSONS_S3A
from bodo_lessons_s3b import LESSONS_S3B
from bodo_lessons_s4 import LESSONS_S4
from bodo_lessons_s5a import LESSONS_S5A
from bodo_lessons_s5b import LESSONS_S5B

BASE = Path(__file__).parent.resolve()

LESSONS = {
    **LESSONS_S1,
    **LESSONS_S2A,
    **LESSONS_S2B,
    **LESSONS_S3A,
    **LESSONS_S3B,
    **LESSONS_S4,
    **LESSONS_S5A,
    **LESSONS_S5B,
}


def load_titles():
    s = json.loads((BASE / "lessons_structure_bodo.json").read_text(encoding="utf-8"))
    out = {}
    for ml in s["majorLessons"]:
        for sub in ml["sublessons"]:
            out[sub["chapterId"]] = sub["title"]
    return out


def main():
    titles = load_titles()
    path = BASE / "data_bodo.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    updated = 0
    for ch in data:
        cid = ch["id"]
        if cid not in LESSONS:
            continue
        title = titles.get(cid, ch.get("title") or ch.get("url", ""))
        ch["url"] = title
        ch["title"] = title
        ch["blocks"] = [{
            "type": "table",
            "columns": ["English", "Bodo", "Transliteration"],
            "rows": LESSONS[cid],
        }]
        updated += 1
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {updated} lessons (501-662) in data_bodo.json")


if __name__ == "__main__":
    main()
