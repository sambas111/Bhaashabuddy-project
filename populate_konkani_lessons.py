#!/usr/bin/env python3
"""Populate Konkani lessons (chapter IDs 501–662) in data_konkani.json from curated banks."""
import json
from pathlib import Path

from konkani_lesson_assembler import build_lessons_dict

BASE = Path(__file__).parent.resolve()


def load_titles():
    s = json.loads((BASE / "lessons_structure_konkani.json").read_text(encoding="utf-8"))
    out = {}
    for ml in s["majorLessons"]:
        for sub in ml["sublessons"]:
            out[sub["chapterId"]] = sub["title"]
    return out


def main():
    titles = load_titles()
    lessons = build_lessons_dict()
    path = BASE / "data_konkani.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    updated = 0
    for ch in data:
        cid = ch["id"]
        if cid not in lessons:
            continue
        title = titles.get(cid, ch.get("title") or ch.get("url", ""))
        ch["url"] = title
        ch["title"] = title
        ch["blocks"] = [{
            "type": "table",
            "columns": ["English", "Konkani", "Transliteration"],
            "rows": lessons[cid],
        }]
        updated += 1
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {updated} lessons (501-662) in data_konkani.json")


if __name__ == "__main__":
    main()
