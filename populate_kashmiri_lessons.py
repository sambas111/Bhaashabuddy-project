#!/usr/bin/env python3
"""Populate Kashmiri lessons (chapter IDs 501–662) in data_kashmiri.json from curated banks."""
import json
from pathlib import Path

from kashmiri_lesson_assembler import build_lessons_dict

BASE = Path(__file__).parent.resolve()


def load_titles():
    s = json.loads((BASE / "lessons_structure_kashmiri.json").read_text(encoding="utf-8-sig"))
    out = {}
    for ml in s["majorLessons"]:
        for sub in ml["sublessons"]:
            out[sub["chapterId"]] = sub["title"]
    return out


def main():
    titles = load_titles()
    lessons = build_lessons_dict()
    path = BASE / "data_kashmiri.json"
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    updated = 0
    for ch in data:
        cid = ch["id"]
        if cid not in lessons:
            continue
        title = titles.get(cid, ch.get("title") or ch.get("url", ""))
        ch["url"] = title
        ch["title"] = title
        ch["content"] = "Study the vocabulary and structures for this topic."
        ch["intro"] = (
            "Each row gives English, Kashmiri in Devanagari, and romanization. "
            "Read aloud and listen using the speaker where available."
        )
        ch["blocks"] = [
            {
                "type": "table",
                "columns": ["English", "Kashmiri", "Transliteration"],
                "rows": lessons[cid],
            }
        ]
        if "tables" in ch:
            del ch["tables"]
        updated += 1
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {updated} lessons (501-662) in data_kashmiri.json")


if __name__ == "__main__":
    main()
