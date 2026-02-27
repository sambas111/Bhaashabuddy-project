#!/usr/bin/env python3
"""
Extract phrases and words from Kannada lessons (data_kannada.json) and
lessons_structure_kannada.json. Group by category like Marathi for Phrases
and by section for Dictionary (Words).
Output: extracted_kannada.json and optionally generate JS for app.js.
"""

import json
import re
from pathlib import Path

BASE = Path(__file__).parent

# Same category mapping as Marathi (extract_phrases_from_lessons.py)
TOPIC_MAP = {
    "Kannada Script - Writing & Pronunciation": "writing",
    "Sentence formation rules in different tenses & pronouns forms": "dailyLife",
    "Phrases & other sentence structures": "dailyLife",
    "Vocabulary": "dailyLife",
    "Conversation practice": "dailyLife",
}

SUBLESSON_KEYWORDS = {
    "greetings": ["greeting", "welcome", "wish", "blessing", "diwali", "salutation", "introduction", "namaste", "hello"],
    "travel": ["travel", "taxi", "rickshaw", "station", "tour", "address"],
    "food": ["food", "meal", "lunch", "hotel", "vegetable", "fruit", "eat", "dining", "grocery"],
    "shopping": ["shopping", "grocery", "market", "buy"],
    "emergency": ["emergency", "police", "help", "doctor"],
    "numbers": ["number", "fraction", "percentage", "sequence"],
    "reading": ["reading", "book", "library"],
    "writing": ["writing", "script", "alphabet", "pronunciation", "consonant", "vowel", "barakhadi"],
    "animals": ["animal", "bird", "insect", "body part", "colour", "flower"],
    "dailyLife": ["sentence", "tense", "verb", "grammar", "preposition", "conversation", "miscellaneous", "practice", "joke", "quote"],
    "environment": ["weather"],
    "health": ["doctor", "hospital", "patient", "body"],
    "schoolWork": ["teacher", "student", "interview", "bank", "software", "engineer"],
    "socialInteractions": ["friend", "parent", "phone", "housemaid", "aadhar", "republic"],
    "time": ["time", "eclipse", "women"],
    "tourism": ["temple", "tourist"],
    "transportation": ["bus", "traffic", "transport"],
}

SECTION_KEYWORDS = {
    "greetings": ["hello", "hi", "thank", "please", "sorry", "name", "meet", "goodbye", "welcome", "wish", "blessing", "namaskar"],
    "reading": ["read", "book", "library", "text", "letter", "word", "sentence"],
    "writing": ["write", "alphabet", "script", "consonant", "vowel", "barakhadi"],
    "numbers": ["number", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "hundred", "thousand"],
    "animals": ["animal", "bird", "dog", "cat", "insect", "head", "eye", "ear", "nose", "hand", "leg", "body"],
    "food": ["food", "eat", "drink", "water", "rice", "vegetable", "fruit", "mango", "meal", "tea", "milk"],
    "health": ["doctor", "hospital", "medicine", "patient", "body", "health", "pain", "fever"],
    "environment": ["weather", "rain", "sun", "tree", "flower", "sky"],
    "time": ["time", "day", "night", "morning", "today", "tomorrow", "yesterday", "week", "month", "year"],
    "transportation": ["bus", "car", "train", "road", "station", "traffic", "taxi", "rickshaw"],
    "travel": ["travel", "tour", "address", "temple", "tourist", "visit"],
    "shopping": ["shop", "market", "buy", "sell", "grocery", "money", "price"],
    "emergency": ["emergency", "police", "help"],
    "schoolWork": ["school", "teacher", "student", "work", "interview", "bank", "engineer"],
    "socialInteractions": ["friend", "mother", "father", "brother", "sister", "family", "parent"],
}

CATEGORY_NAMES = {
    "greetings": "Greetings",
    "travel": "Travel",
    "food": "Food & Drink",
    "shopping": "Shopping",
    "emergency": "Emergency",
    "numbers": "Numbers",
    "reading": "Reading",
    "writing": "Writing",
    "animals": "Animals & Nature",
    "dailyLife": "Daily Life",
    "environment": "Environment",
    "health": "Health",
    "schoolWork": "School & Work",
    "socialInteractions": "Social",
    "time": "Time",
    "tourism": "Tourism",
    "transportation": "Transportation",
}

def has_kannada_script(s: str) -> bool:
    return bool(re.search(r"[\u0C80-\u0CFF]", s))

def has_roman(s: str) -> bool:
    if not s or has_kannada_script(s):
        return False
    return bool(re.search(r"[a-zA-Z]", s))

def get_category_for_lesson(major_name: str, sublesson_title: str) -> str:
    title_lower = sublesson_title.lower()
    for cat, keywords in SUBLESSON_KEYWORDS.items():
        if any(kw in title_lower for kw in keywords):
            return cat
    return TOPIC_MAP.get(major_name, "dailyLife")

def classify_word(en: str) -> str:
    en_lower = en.lower().strip()
    for section, keywords in SECTION_KEYWORDS.items():
        if any(kw in en_lower for kw in keywords):
            return section
    return "dailyLife"

def extract_from_table(block: dict) -> list[dict]:
    """Extract {en, mr, roman} from a table block. mr = Kannada script."""
    headers = block.get("headers", [])
    rows = block.get("rows", [])
    if not headers or not rows:
        return []

    headers_lower = [str(h).lower() for h in headers]
    eng_idx = mr_idx = trans_idx = None
    for i, h in enumerate(headers_lower):
        if "english" in h:
            eng_idx = i
        elif "kannada" in h or "ಕನ್ನಡ" in h:
            mr_idx = i
        elif "translit" in h or "transliteration" in h:
            trans_idx = i

    if eng_idx is None and len(headers) >= 3:
        eng_idx, mr_idx, trans_idx = 0, 1, 2
    if eng_idx is None or mr_idx is None or trans_idx is None:
        return []

    phrases = []
    seen = set()
    for row in rows:
        if not isinstance(row, (list, tuple)) or len(row) <= max(eng_idx, mr_idx, trans_idx):
            continue
        en = str(row[eng_idx]).strip() if eng_idx < len(row) else ""
        mr = str(row[mr_idx]).strip() if mr_idx < len(row) else ""
        roman = str(row[trans_idx]).strip() if trans_idx < len(row) else ""
        if not en or not mr or not roman:
            continue
        if not has_kannada_script(mr):
            continue
        if has_kannada_script(roman):
            continue
        if len(en) < 2 or len(mr) < 2:
            continue
        key = (en.lower(), mr)
        if key in seen:
            continue
        seen.add(key)
        phrases.append({"en": en, "mr": mr, "roman": roman, "hint": ""})
    return phrases

def extract_from_lesson(lesson: dict) -> list[dict]:
    out = []
    # blocks
    for blk in lesson.get("blocks", []):
        if blk.get("type") == "table":
            out.extend(extract_from_table(blk))
    # top-level tables (e.g. chapter 301)
    for tbl in lesson.get("tables", []):
        out.extend(extract_from_table(tbl))
    return out

def main():
    with open(BASE / "lessons_structure_kannada.json", "r", encoding="utf-8") as f:
        structure = json.load(f)
    with open(BASE / "data_kannada.json", "r", encoding="utf-8") as f:
        lessons_data = json.load(f)

    lessons_by_id = {int(l["id"]): l for l in lessons_data if "id" in l}
    by_category = {}
    all_entries = []
    seen_phrase_key = set()
    stats = {"lessons_processed": 0, "phrases_extracted": 0}

    for major in structure.get("majorLessons", []):
        major_name = major.get("name", "")
        for sub in major.get("sublessons", []):
            ch_id = sub.get("chapterId")
            title = sub.get("title", "")
            lesson = lessons_by_id.get(ch_id)
            if not lesson:
                continue
            stats["lessons_processed"] += 1
            phrases = extract_from_lesson(lesson)
            if not phrases:
                continue
            cat = get_category_for_lesson(major_name, title)
            if cat not in by_category:
                by_category[cat] = []
            for p in phrases:
                key = (p["en"].lower(), p["mr"])
                if key in seen_phrase_key:
                    continue
                seen_phrase_key.add(key)
                by_category[cat].append(p)
                stats["phrases_extracted"] += 1
                all_entries.append({"en": p["en"], "mr": p["mr"], "roman": p["roman"]})

    # Dedupe within category
    for cat in by_category:
        seen = set()
        unique = []
        for p in by_category[cat]:
            k = (p["en"].lower(), p["mr"])
            if k not in seen:
                seen.add(k)
                unique.append(p)
        by_category[cat] = unique

    # Dictionary by section
    by_section = {}
    seen_mr = set()
    for e in all_entries:
        if e["mr"] in seen_mr:
            continue
        seen_mr.add(e["mr"])
        sec = classify_word(e["en"])
        if sec not in by_section:
            by_section[sec] = []
        by_section[sec].append({"en": e["en"], "mr": e["mr"], "roman": e["roman"]})

    out = {
        "by_category": by_category,
        "by_section": by_section,
        "stats": stats,
    }
    with open(BASE / "extracted_kannada.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"Processed {stats['lessons_processed']} lessons, extracted {stats['phrases_extracted']} phrases")
    for cat in sorted(by_category.keys(), key=lambda c: -len(by_category[c])):
        print(f"  {cat}: {len(by_category[cat])} phrases")
    print("\nDictionary sections:")
    for sec in sorted(by_section.keys(), key=lambda s: -len(by_section[s])):
        print(f"  {sec}: {len(by_section[sec])} words")
    print(f"\nWrote extracted_kannada.json")
    return out

if __name__ == "__main__":
    main()
