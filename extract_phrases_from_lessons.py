#!/usr/bin/env python3
"""
Extract English, Marathi, and Transliteration from reformatted Marathi lessons
and add them to:
  1) Phrases section in app.js (organized by topic)
  2) Words/Dictionary section in app.js
"""

import json
import re
from pathlib import Path

BASE = Path(__file__).parent

# Map major lesson names and sublesson title keywords to phrase category IDs
TOPIC_MAP = {
    # Major lesson -> default category
    "Introductory lessons": "greetings",
    "Marathi Script - Writing & Pronunciation": "writing",
    "Sentence formation rules in different tenses & pronouns forms": "dailyLife",
    "Phrases & other sentence structures": "dailyLife",
    "Vocabulary": "dailyLife",
    "Conversation practice": "dailyLife",
}

# Sublesson title keywords -> override category
SUBLESSON_KEYWORDS = {
    "greetings": ["greeting", "welcome", "wish", "blessing", "diwali", "salutation", "introduction"],
    "travel": ["travel", "taxi", "rickshaw", "station", "tour", "singapore", "address"],
    "food": ["food", "meal", "lunch", "hotel", "vegetable", "fruit", "eat", "dining"],
    "shopping": ["shopping", "grocery", "market", "buy"],
    "emergency": ["emergency", "police", "help", "doctor"],
    "numbers": ["number", "fraction", "percentage", "sequence"],
    "reading": ["reading", "book", "library"],
    "writing": ["writing", "script", "alphabet", "pronunciation", "consonant", "vowel", "barakhadi"],
    "animals": ["animal", "bird", "insect", "body part"],
    "dailyLife": ["sentence", "tense", "verb", "grammar", "preposition", "conversation", "miscellaneous", "practice", "joke", "quote"],
    "environment": ["weather"],
    "health": ["doctor", "hospital", "patient", "body"],
    "schoolWork": ["teacher", "student", "interview", "bank", "software", "engineer"],
    "socialInteractions": ["friend", "parent", "phone", "housemaid", "aadhar", "republic"],
    "time": ["time", "eclipse", "women"],
    "tourism": ["temple", "tourist"],
    "transportation": ["bus", "traffic", "transport"],
}

def get_category_for_lesson(major_name: str, sublesson_title: str) -> str:
    """Determine phrase category from major lesson and sublesson title."""
    title_lower = sublesson_title.lower()
    for cat, keywords in SUBLESSON_KEYWORDS.items():
        if any(kw in title_lower for kw in keywords):
            return cat
    return TOPIC_MAP.get(major_name, "dailyLife")

def has_devanagari(s: str) -> bool:
    """Check if string contains Devanagari characters."""
    return bool(re.search(r'[\u0900-\u097F]', s))

def has_transliteration(s: str) -> bool:
    """Check if string looks like transliteration (roman letters, no Devanagari)."""
    if not s or has_devanagari(s):
        return False
    return bool(re.search(r'[a-zA-Z]', s))

def extract_from_table(block: dict) -> list[dict]:
    """Extract phrases from a table block. Returns list of {en, mr, roman}."""
    headers = block.get("headers", [])
    rows = block.get("rows", [])
    if not headers or not rows:
        return []

    # Find column indices for English, Marathi, Transliteration
    headers_lower = [str(h).lower() for h in headers]
    eng_idx = None
    mr_idx = None
    trans_idx = None

    for i, h in enumerate(headers_lower):
        if "english" in h:
            eng_idx = i
        elif "marathi" in h or "मराठी" in h or "म.ए" in h or "म.ब" in h or "स्त्री" in h or "न.ए" in h or "न.ब" in h:
            if mr_idx is None:
                mr_idx = i
        elif "translit" in h or "transliteration" in h:
            if trans_idx is None:
                trans_idx = i

    # If we have exact "English", "Marathi", "Transliteration" - use those
    if eng_idx is None:
        for i, h in enumerate(headers_lower):
            if h == "english":
                eng_idx = i
                break
    if mr_idx is None:
        for i, h in enumerate(headers_lower):
            if h == "marathi":
                mr_idx = i
                break
    if trans_idx is None:
        for i, h in enumerate(headers_lower):
            if "translit" in h or h == "transliteration":
                trans_idx = i
                break

    # For tables with many columns (e.g. Gender forms), use first Eng, first Mr, first Trans
    if eng_idx is not None and mr_idx is not None and trans_idx is not None:
        pass
    elif eng_idx == 0 and len(headers) >= 3:
        # Assume order: English, Marathi, Transliteration
        mr_idx = 1
        trans_idx = 2
    else:
        return []

    phrases = []
    seen = set()

    for row in rows:
        if not isinstance(row, (list, tuple)) or len(row) <= max(eng_idx, mr_idx, trans_idx):
            continue
        en = str(row[eng_idx]).strip() if eng_idx < len(row) else ""
        mr = str(row[mr_idx]).strip() if mr_idx < len(row) else ""
        roman = str(row[trans_idx]).strip() if trans_idx < len(row) else ""

        # Validate: need all three, Marathi should have Devanagari, roman should not
        if not en or not mr or not roman:
            continue
        if not has_devanagari(mr):
            continue
        if has_devanagari(roman):
            continue
        # Skip very short or rule-like entries
        if len(en) < 2 or len(mr) < 2:
            continue
        # Deduplicate by (en, mr)
        key = (en.lower(), mr)
        if key in seen:
            continue
        seen.add(key)

        phrases.append({"en": en, "mr": mr, "roman": roman, "hint": ""})

    return phrases

def extract_from_lesson(lesson: dict) -> list[dict]:
    """Extract all phrases from a lesson's blocks."""
    blocks = lesson.get("blocks", [])
    if not blocks:
        return []
    out = []
    for b in blocks:
        if b.get("type") == "table":
            out.extend(extract_from_table(b))
    return out

def main():
    with open(BASE / "lessons_structure.json", "r", encoding="utf-8") as f:
        structure = json.load(f)

    with open(BASE / "data.json", "r", encoding="utf-8") as f:
        lessons_data = json.load(f)

    # Build id -> lesson lookup
    lessons_by_id = {int(l["id"]): l for l in lessons_data if "id" in l}

    # Collect phrases by category
    by_category = {}
    stats = {"lessons_processed": 0, "lessons_with_blocks": 0, "phrases_extracted": 0}

    for major in structure.get("majorLessons", []):
        major_name = major.get("name", "")
        for sub in major.get("sublessons", []):
            ch_id = sub.get("chapterId")
            title = sub.get("title", "")
            lesson = lessons_by_id.get(ch_id)
            if not lesson:
                continue
            stats["lessons_processed"] += 1
            if "blocks" not in lesson:
                continue
            stats["lessons_with_blocks"] += 1
            phrases = extract_from_lesson(lesson)
            if not phrases:
                continue
            cat = get_category_for_lesson(major_name, title)
            if cat not in by_category:
                by_category[cat] = []
            for p in phrases:
                by_category[cat].append(p)
                stats["phrases_extracted"] += 1

    # Deduplicate within each category (keep first occurrence)
    for cat in by_category:
        seen = set()
        unique = []
        for p in by_category[cat]:
            key = (p["en"].lower(), p["mr"])
            if key not in seen:
                seen.add(key)
                unique.append(p)
        by_category[cat] = unique

    # Load existing PHRASES from app.js to merge
    app_path = BASE / "app.js"
    with open(app_path, "r", encoding="utf-8") as f:
        app_content = f.read()

    # Find PHRASES object - extract it
    import re as re_mod
    # Match: const PHRASES = { ... };
    phr_match = re_mod.search(r"const PHRASES\s*=\s*(\{[\s\S]*?\n\}\s*);", app_content)
    if not phr_match:
        print("Could not find PHRASES in app.js")
        return
    phrases_str = phr_match.group(1)
    try:
        # Parse as JavaScript object - we need to handle the structure
        # Simpler: use a regex to find each category block and append
        pass
    except Exception:
        pass

    # Build flat list of all unique entries for dictionary (Words section)
    all_entries = []
    seen_mr = set()
    for phs in by_category.values():
        for p in phs:
            if p["mr"] not in seen_mr:
                seen_mr.add(p["mr"])
                all_entries.append({"en": p["en"], "mr": p["mr"], "roman": p["roman"]})
    stats["dictionary_extracted"] = len(all_entries)

    output = {
        "by_category": by_category,
        "dictionary_entries": all_entries,
        "stats": stats,
    }
    with open(BASE / "extracted_phrases.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Processed {stats['lessons_processed']} lessons, {stats['lessons_with_blocks']} with blocks")
    print(f"Extracted {stats['phrases_extracted']} phrases, {stats['dictionary_extracted']} dictionary entries")
    for cat, phs in sorted(by_category.items(), key=lambda x: -len(x[1])):
        print(f"  {cat}: {len(phs)} phrases")
    print(f"\nWrote extracted_phrases.json")

    # Now merge into app.js
    merge_into_app_js(BASE, by_category, app_path)
    merge_into_dictionary(BASE, all_entries, app_path)

def merge_into_app_js(base: Path, by_category: dict, app_path: Path):
    """Merge extracted phrases into app.js PHRASES object."""
    with open(app_path, "r", encoding="utf-8") as f:
        content = f.read()

    # We need to append phrases to existing categories. The structure is:
    # categoryId: { name: "...", color: "...", icon: "...", phrases: [ {...}, ... ] }
    # We append to the phrases array of each category.

    for cat_id, new_phrases in by_category.items():
        if not new_phrases:
            continue
        # Find the phrases array for this category (only in PHRASES, not GUJARATI_PHRASES)
        # Pattern: cat_id: { ... phrases: [ ... ] }
        esc = re.escape(cat_id)
        pattern = r"(\s+" + esc + r"\s*:\s*\{[^}]*?phrases\s*:\s*\[)([\s\S]*?)(\]\s*\n\s*\})"
        match = re.search(pattern, content)
        if not match:
            # Category might not exist - we could add it, but for now skip
            print(f"  Category '{cat_id}' not found in app.js, skipping merge")
            continue

        prefix, existing_phrases, suffix = match.groups()
        # Deduplicate: don't add if mr already exists (Marathi is unique)
        existing_mr = set()
        for m in re.finditer(r'mr:\s*"((?:[^"\\]|\\.)*)"', existing_phrases):
            existing_mr.add(m.group(1))

        to_add = []
        for p in new_phrases:
            if p["mr"] in existing_mr:
                continue
            existing_mr.add(p["mr"])
            to_add.append(p)

        if not to_add:
            continue

        # Format new phrases as JS
        new_lines = []
        for p in to_add:
            en_esc = p["en"].replace('\\', '\\\\').replace('"', '\\"')
            mr_esc = p["mr"].replace('\\', '\\\\').replace('"', '\\"')
            roman_esc = p["roman"].replace('\\', '\\\\').replace('"', '\\"')
            new_lines.append(f'      {{ en: "{en_esc}", mr: "{mr_esc}", roman: "{roman_esc}", hint: "" }}')

        insert_text = ",\n" + ",\n".join(new_lines)
        # Insert before the closing ] of the phrases array
        old_block = prefix + existing_phrases + suffix
        # Add after last phrase in array - find the last },
        if existing_phrases.strip().endswith("}"):
            new_block = prefix + existing_phrases.rstrip() + insert_text + "\n    " + suffix
        else:
            new_block = prefix + existing_phrases + insert_text + "\n    " + suffix
        content = content.replace(match.group(0), new_block, 1)
        print(f"  Merged {len(to_add)} phrases into '{cat_id}'")

    with open(app_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("\nUpdated app.js (phrases)")


def merge_into_dictionary(base: Path, new_entries: list[dict], app_path: Path):
    """Merge extracted entries into DICTIONARY (Words section) in app.js."""
    with open(app_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find DICTIONARY array - Marathi one (before GUJARATI_PHRASES)
    pattern = r"(const DICTIONARY = \[)([\s\S]*?)(\]\s*;)"
    match = re.search(pattern, content)
    if not match:
        print("  Could not find DICTIONARY in app.js")
        return

    prefix, existing, suffix = match.groups()
    existing_mr = set(re.findall(r'mr:\s*"((?:[^"\\]|\\.)*)"', existing))

    to_add = []
    for e in new_entries:
        if e["mr"] in existing_mr:
            continue
        existing_mr.add(e["mr"])
        to_add.append(e)

    if not to_add:
        print("  No new dictionary entries to add")
        return

    new_lines = []
    for e in to_add:
        en_esc = e["en"].replace("\\", "\\\\").replace('"', '\\"')
        mr_esc = e["mr"].replace("\\", "\\\\").replace('"', '\\"')
        roman_esc = e["roman"].replace("\\", "\\\\").replace('"', '\\"')
        new_lines.append(f'  {{ en: "{en_esc}", mr: "{mr_esc}", roman: "{roman_esc}" }}')

    # Existing array ends with "},\n" - add new entries with leading newline
    insert_text = "\n" + ",\n".join(new_lines)
    if existing.strip().endswith("}"):
        new_block = prefix + existing.rstrip() + insert_text + "\n" + suffix
    else:
        new_block = prefix + existing + insert_text + "\n" + suffix

    content = content.replace(match.group(0), new_block, 1)
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Merged {len(to_add)} entries into DICTIONARY (Words)")


if __name__ == "__main__":
    main()
