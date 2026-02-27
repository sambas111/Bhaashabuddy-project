#!/usr/bin/env python3
"""
Build sectioned dictionary from flat dictionary or extracted_phrases.json.
Words are classified into sections: reading, writing, numbers, animals, food, etc.
Output: dictionary_marathi.json (sectioned) for use with translate_pipeline.

Usage:
  python build_dictionary_sections.py                    # from app.js DICTIONARY
  python build_dictionary_sections.py --from extracted_phrases.json
"""

import json
import re
from pathlib import Path

BASE = Path(__file__).parent

# Section names (matches phrase categories)
SECTION_NAMES = {
    "greetings": "Greetings & Basics",
    "reading": "Reading",
    "writing": "Writing & Script",
    "numbers": "Numbers",
    "animals": "Animals & Nature",
    "dailyLife": "Daily Life",
    "environment": "Environment & Weather",
    "food": "Food & Drink",
    "health": "Health & Body",
    "schoolWork": "School & Work",
    "socialInteractions": "Social & People",
    "time": "Time & Dates",
    "tourism": "Travel & Tourism",
    "transportation": "Transportation",
    "travel": "Travel",
    "shopping": "Shopping",
    "emergency": "Emergency",
}

# Keywords to classify English words into sections (order matters - first match wins)
SECTION_KEYWORDS = {
    "greetings": ["hello", "hi", "thank", "please", "sorry", "name", "meet", "goodbye", "welcome", "wish", "blessing"],
    "reading": ["read", "book", "library", "text", "letter", "word", "sentence", "paragraph", "page"],
    "writing": ["write", "digit", "alphabet", "script", "consonant", "vowel", "barakhadi", "handwriting", "mark", "bracket"],
    "numbers": ["number", "digit", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "hundred", "thousand", "fraction", "percentage", "count", "first", "second", "third"],
    "animals": ["animal", "bird", "fish", "dog", "cat", "insect", "body part", "head", "eye", "ear", "nose", "hand",
                "leg", "finger", "heart", "brain", "hair", "face", "mouth", "tooth", "tongue"],
    "food": ["food", "eat", "drink", "water", "rice", "vegetable", "fruit", "mango", "meal", "lunch", "breakfast",
             "dinner", "tea", "milk", "bread", "sugar", "salt", "spice", "kitchen"],
    "health": ["doctor", "hospital", "medicine", "patient", "body", "health", "sick", "pain", "fever", "cough"],
    "environment": ["weather", "rain", "sun", "cloud", "wind", "hot", "cold", "tree", "flower", "plant", "sky"],
    "time": ["time", "day", "night", "morning", "evening", "today", "tomorrow", "yesterday", "week", "month", "year",
             "hour", "minute", "second", "eclipse"],
    "transportation": ["bus", "car", "train", "road", "station", "traffic", "police", "driver", "taxi", "rickshaw"],
    "transport": ["bus", "car", "train", "road", "station", "traffic", "police", "driver", "taxi", "rickshaw"],
    "travel": ["travel", "tour", "address", "temple", "tourist", "visit", "go", "come"],
    "tourism": ["temple", "tourist", "visit", "tour", "singapore"],
    "shopping": ["shop", "market", "buy", "sell", "grocery", "vegetable market", "money", "price"],
    "emergency": ["emergency", "police", "help", "doctor", "hospital"],
    "schoolWork": ["school", "teacher", "student", "work", "study", "interview", "bank", "engineer", "software"],
    "socialInteractions": ["friend", "mother", "father", "brother", "sister", "family", "parent", "phone", "housemaid",
                          "aadhar", "republic", "friend"],
}


def classify_word(en: str) -> str:
    """Classify a word into a section based on English text."""
    en_lower = en.lower().strip()
    for section, keywords in SECTION_KEYWORDS.items():
        if any(kw in en_lower for kw in keywords):
            return section
    return "dailyLife"


def extract_from_app_js():
    """Extract DICTIONARY from app.js."""
    app_path = BASE / "app.js"
    if not app_path.exists():
        return None
    content = app_path.read_text(encoding="utf-8")
    # Match: const DICTIONARY = [ ... ];
    match = re.search(r"const DICTIONARY\s*=\s*\[([\s\S]*?)\]\s*;", content)
    if not match:
        return None
    arr_str = "[" + match.group(1) + "]"
    arr_str = re.sub(r"(?<=[,{\[])\s*(\w+)\s*:", lambda m: f'"{m.group(1)}":', arr_str)
    arr_str = re.sub(r",\s*([}\]])", r"\1", arr_str)
    try:
        return json.loads(arr_str)
    except json.JSONDecodeError:
        return None


def build_from_flat(entries: list) -> dict:
    """Build sectioned dictionary from flat list."""
    sections = {}
    for entry in entries:
        en = entry.get("en", "")
        section = classify_word(en)
        if section not in sections:
            sections[section] = {"name": SECTION_NAMES.get(section, section), "words": []}
        sections[section]["words"].append(entry)
    # Sort sections by canonical order
    order = list(SECTION_NAMES.keys())
    sorted_sections = {}
    for section_id in order:
        if section_id in sections:
            sorted_sections[section_id] = sections[section_id]
    for section_id in sections:
        if section_id not in sorted_sections:
            sorted_sections[section_id] = sections[section_id]
    return sorted_sections


def build_from_extracted(extracted_path: Path) -> dict:
    """Build sectioned dictionary from extracted_phrases.json (by_category has section info)."""
    with open(extracted_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    by_category = data.get("by_category", {})
    sections = {}
    seen = set()  # (en, mr) for dedup
    for cat_id, phrases in by_category.items():
        if cat_id not in sections:
            sections[cat_id] = {"name": SECTION_NAMES.get(cat_id, cat_id), "words": []}
        for p in phrases:
            key = (p.get("en", "").lower(), p.get("mr", ""))
            if key in seen:
                continue
            seen.add(key)
            entry = {"en": p.get("en", ""), "mr": p.get("mr", ""), "roman": p.get("roman", "")}
            sections[cat_id]["words"].append(entry)
    return sections


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Build sectioned dictionary")
    parser.add_argument("--from", dest="source", default="app", help="app | extracted_phrases.json")
    parser.add_argument("--output", "-o", default="dictionary_marathi.json", help="Output file")
    args = parser.parse_args()

    if args.source == "app":
        entries = extract_from_app_js()
        if not entries:
            print("Could not extract DICTIONARY from app.js")
            return
        sections = build_from_flat(entries)
    else:
        src_path = BASE / args.source
        if not src_path.exists():
            print(f"Source not found: {src_path}")
            return
        sections = build_from_extracted(src_path)

    out_path = BASE / args.output
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(sections, f, ensure_ascii=False, indent=2)
    total = sum(len(s["words"]) for s in sections.values())
    print(f"Built {len(sections)} sections, {total} words -> {out_path}")
    for sec_id, sec_data in sections.items():
        print(f"  {sec_id}: {len(sec_data['words'])} words")


if __name__ == "__main__":
    main()
