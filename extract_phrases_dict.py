#!/usr/bin/env python3
"""
Extract PHRASES and DICTIONARY from app.js to JSON files.
Output: phrases_marathi.json, dictionary_marathi.json
These can be used as input for the translation pipeline.
"""

import json
import re
from pathlib import Path

BASE = Path(__file__).parent
APP_JS = BASE / "app.js"


def extract_js_object(content: str, var_name: str) -> dict | list | None:
    """Extract a JavaScript object/array by finding the variable assignment."""
    pattern = rf"(?:const|let)\s+{var_name}\s*=\s*"
    match = re.search(pattern, content)
    if not match:
        return None
    start = match.end()
    depth = 0
    in_str = False
    escape = False
    quote = None
    i = start
    while i < len(content):
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
            elif c in "{[":
                depth += 1
            elif c in "}]":
                depth -= 1
                if depth == 0:
                    break
        else:
            if c == quote:
                in_str = False
        i += 1
    js_str = content[start : i + 1]
    # Convert JS to JSON: unquoted keys -> quoted keys (avoid double-quoting)
    def quote_key(m):
        key = m.group(1)
        return f'"{key}":'
    js_str = re.sub(r"(?<=[,{\[])\s*(\w+)\s*:", quote_key, js_str)
    # Fix first key in object: { key: -> { "key":
    js_str = re.sub(r"^\s*(\w+)\s*:", lambda m: f'"{m.group(1)}":', js_str, count=1)
    # Remove trailing commas before ] or }
    js_str = re.sub(r",\s*([}\]])", r"\1", js_str)
    try:
        return json.loads(js_str)
    except json.JSONDecodeError as e:
        # Try with json5 if available
        try:
            import json5
            return json5.loads(js_str)
        except ImportError:
            return None


def main():
    if not APP_JS.exists():
        print(f"app.js not found: {APP_JS}")
        return
    content = APP_JS.read_text(encoding="utf-8")
    phrases = extract_js_object(content, "PHRASES")
    if phrases:
        out = {}
        for cat_id, cat_data in phrases.items():
            if isinstance(cat_data, dict) and "phrases" in cat_data:
                out[cat_id] = {
                    "name": cat_data.get("name", cat_id),
                    "phrases": cat_data["phrases"],
                }
        path = BASE / "phrases_marathi.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        total = sum(len(c["phrases"]) for c in out.values())
        print(f"Saved {total} phrases to {path}")
    else:
        print("Could not extract PHRASES")
    dictionary = extract_js_object(content, "DICTIONARY")
    if dictionary:
        path = BASE / "dictionary_marathi.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(dictionary, f, ensure_ascii=False, indent=2)
        print(f"Saved {len(dictionary)} words to {path}")
    else:
        print("Could not extract DICTIONARY")


if __name__ == "__main__":
    main()
