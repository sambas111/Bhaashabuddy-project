#!/usr/bin/env python3
"""Fill data_hindi.json lessons (501–662) with curated Hindi + transliteration rows from hindi_lesson_banks."""
import json
from pathlib import Path

from hindi_lesson_banks import get_lesson_rows
from hindi_grammar_chapters import get_grammar_chapter
from hindi_phrases_chapters import get_phrases_chapter
from hindi_script_chapters import get_script_chapter
from hindi_vocabulary_chapters import get_vocabulary_chapter
from hindi_conversation_chapters import get_conversation_chapter

BASE = Path(__file__).parent.resolve()


def load_titles():
    s = json.loads((BASE / "lessons_structure_hindi.json").read_text(encoding="utf-8"))
    out = {}
    for ml in s["majorLessons"]:
        for sub in ml["sublessons"]:
            out[sub["chapterId"]] = sub["title"]
    return out


def main():
    titles = load_titles()
    path = BASE / "data_hindi.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    updated = 0
    for ch in data:
        cid = ch.get("id")
        if cid not in titles:
            continue
        title = titles[cid]
        ch["url"] = title
        ch["title"] = title

        script = get_script_chapter(cid)
        if script:
            ch["content"] = script["content"]
            ch["intro"] = script["intro"]
            ch.pop("tables", None)
            ch.pop("blocks", None)
            if "tables" in script:
                ch["tables"] = script["tables"]
            if "blocks" in script:
                ch["blocks"] = script["blocks"]
            updated += 1
            continue

        grammar = get_grammar_chapter(cid)
        if grammar:
            ch["content"] = grammar["content"]
            ch["intro"] = grammar["intro"]
            ch.pop("tables", None)
            ch.pop("blocks", None)
            if "tables" in grammar:
                ch["tables"] = grammar["tables"]
            if "blocks" in grammar:
                ch["blocks"] = grammar["blocks"]
            updated += 1
            continue

        phrases = get_phrases_chapter(cid)
        if phrases:
            ch["content"] = phrases["content"]
            ch["intro"] = phrases["intro"]
            ch.pop("tables", None)
            ch.pop("blocks", None)
            if "tables" in phrases:
                ch["tables"] = phrases["tables"]
            if "blocks" in phrases:
                ch["blocks"] = phrases["blocks"]
            updated += 1
            continue

        vocab = get_vocabulary_chapter(cid)
        if vocab:
            ch["content"] = vocab["content"]
            ch["intro"] = vocab["intro"]
            ch.pop("tables", None)
            ch.pop("blocks", None)
            if "tables" in vocab:
                ch["tables"] = vocab["tables"]
            if "blocks" in vocab:
                ch["blocks"] = vocab["blocks"]
            updated += 1
            continue

        conversation = get_conversation_chapter(cid)
        if conversation:
            ch["content"] = conversation["content"]
            ch["intro"] = conversation["intro"]
            ch.pop("tables", None)
            ch.pop("blocks", None)
            if "tables" in conversation:
                ch["tables"] = conversation["tables"]
            if "blocks" in conversation:
                ch["blocks"] = conversation["blocks"]
            updated += 1
            continue

        rows = get_lesson_rows(cid, title)
        ch["content"] = (
            f"Practice sentences for: {title}. "
            "Each row has English, Hindi in Devanagari, and romanization. Read aloud and use audio where available."
        )
        ch["intro"] = (
            "These examples follow standard spoken Hindi. "
            "Transliteration uses a simple IAST-style romanization for learning."
        )
        ch["blocks"] = [
            {
                "type": "table",
                "heading": "Practice sentences",
                "headers": ["English", "Hindi", "Transliteration"],
                "speakCol": 1,
                "rows": rows,
            }
        ]
        if "tables" in ch:
            del ch["tables"]
        updated += 1
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {updated} Hindi lessons in data_hindi.json")


if __name__ == "__main__":
    main()
