#!/usr/bin/env python3
"""
Embed sectioned dictionary from dictionary_marathi.json into app.js.
Replaces the flat DICTIONARY array with sectioned format.

Run after: python build_dictionary_sections.py
"""

import json
import re
from pathlib import Path

BASE = Path(__file__).parent
APP_JS = BASE / "app.js"
DICT_JSON = BASE / "dictionary_marathi.json"


def js_escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def to_js_object(obj):
    """Convert Python dict to JavaScript object string."""
    if isinstance(obj, dict):
        parts = []
        for k, v in obj.items():
            parts.append(f'  "{k}": {to_js_object(v)}')
        return "{\n" + ",\n".join(parts) + "\n}"
    if isinstance(obj, list):
        parts = []
        for item in obj:
            parts.append(to_js_object(item))
        return "[\n" + ",\n".join(parts) + "\n]"
    if isinstance(obj, str):
        return json.dumps(obj)
    return str(obj)


def main():
    if not DICT_JSON.exists():
        print(f"Run build_dictionary_sections.py first to create {DICT_JSON}")
        return
    if not APP_JS.exists():
        print(f"app.js not found: {APP_JS}")
        return

    with open(DICT_JSON, "r", encoding="utf-8") as f:
        sections = json.load(f)

    content = APP_JS.read_text(encoding="utf-8")

    # Build JS string for sectioned dictionary
    js_sections = {}
    for sec_id, sec_data in sections.items():
        words_js = []
        for w in sec_data.get("words", []):
            en = js_escape(w.get("en", ""))
            mr = js_escape(w.get("mr", ""))
            roman = js_escape(w.get("roman", ""))
            words_js.append(f'    {{ en: "{en}", mr: "{mr}", roman: "{roman}" }}')
        js_sections[sec_id] = {
            "name": sec_data.get("name", sec_id),
            "words": "[\n" + ",\n".join(words_js) + "\n  ]"
        }

    # Build replacement - we need to match the exact pattern
    new_dict_parts = []
    for sec_id, sec_data in js_sections.items():
        new_dict_parts.append(f'  {sec_id}: {{\n    name: "{js_escape(sec_data["name"])}",\n    words: {sec_data["words"]}\n  }}')
    new_dict_str = "{\n" + ",\n".join(new_dict_parts) + "\n}"

    # Find const DICTIONARY = [ ... ];
    start_marker = "const DICTIONARY = "
    idx = content.find(start_marker)
    if idx < 0:
        print("Could not find DICTIONARY in app.js")
        return
    start = idx + len(start_marker)
    # Find matching ] - bracket depth
    depth = 0
    in_str = False
    quote = None
    escape = False
    i = start
    if content[start] == "[":
        depth = 1
        i = start + 1
    while i < len(content) and depth > 0:
        c = content[i]
        if escape:
            escape = False
            i += 1
            continue
        if c == "\\" and in_str:
            escape = True
            i += 1
            continue
        if not in_str:
            if c in '"\'':
                in_str = True
                quote = c
            elif c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
                if depth == 0:
                    break
        else:
            if c == quote:
                in_str = False
        i += 1
    end = i + 1
    # Include trailing ;
    while end < len(content) and content[end] in " \t\n":
        end += 1
    if end < len(content) and content[end] == ";":
        end += 1
    new_content = content[:idx] + start_marker + new_dict_str + ";\n" + content[end:]
    APP_JS.write_text(new_content, encoding="utf-8")
    print(f"Embedded sectioned dictionary into app.js ({len(sections)} sections)")


if __name__ == "__main__":
    main()
