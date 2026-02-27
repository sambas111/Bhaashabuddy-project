#!/usr/bin/env python3
"""Read extracted_kannada.json and write kannada_data.js for Phrases and Dictionary."""

import json
from pathlib import Path

BASE = Path(__file__).parent

CATEGORY_META = {
    "greetings": ("Greetings", "#2B6CB0", "👋"),
    "travel": ("Travel", "#D69E2E", "🚗"),
    "food": ("Food & Drink", "#C05621", "🍽️"),
    "shopping": ("Shopping", "#805AD5", "🛍️"),
    "emergency": ("Emergency", "#E53E3E", "🚨"),
    "numbers": ("Numbers", "#38A169", "🔢"),
    "reading": ("Reading", "#4A5568", "📖"),
    "writing": ("Writing", "#2C5282", "✏️"),
    "animals": ("Animals & Nature", "#744210", "🐾"),
    "dailyLife": ("Daily Life", "#553C9A", "🏠"),
    "environment": ("Environment", "#276749", "🌿"),
    "health": ("Health", "#C53030", "🏥"),
    "schoolWork": ("School & Work", "#2B6CB0", "💼"),
    "socialInteractions": ("Social", "#9F7AEA", "👥"),
    "time": ("Time", "#3182CE", "🕐"),
    "tourism": ("Tourism", "#D69E2E", "🗺️"),
    "transportation": ("Transportation", "#2D3748", "🚌"),
}

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

def esc(s):
    if s is None:
        return ""
    return str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r")

def phrase_js(p):
    return f'{{ en: "{esc(p["en"])}", mr: "{esc(p["mr"])}", roman: "{esc(p["roman"])}", hint: "" }}'

def word_js(w):
    return f'{{ en: "{esc(w["en"])}", mr: "{esc(w["mr"])}", roman: "{esc(w["roman"])}" }}'

def main():
    with open(BASE / "extracted_kannada.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    by_category = data.get("by_category", {})
    by_section = data.get("by_section", {})

    # Build KANNADA_PHRASES - all categories in fixed order
    cat_order = list(CATEGORY_META.keys())
    lines = ["// Kannada phrases & dictionary - extracted from lessons\nconst KANNADA_PHRASES = {"]
    for cat in cat_order:
        name, color, icon = CATEGORY_META[cat]
        phrases = by_category.get(cat, [])
        lines.append(f'  {cat}: {{')
        lines.append(f'    name: "{name}",')
        lines.append(f'    color: "{color}",')
        lines.append(f'    icon: "{icon}",')
        lines.append('    phrases: [')
        for p in phrases:
            lines.append("      " + phrase_js(p) + ",")
        if phrases:
            lines[-1] = lines[-1].rstrip(",")  # remove trailing comma
        lines.append("    ]")
        lines.append("  },")
    lines[-1] = "  }"  # last category no comma
    lines.append("};")
    lines.append("")
    # Build KANNADA_DICTIONARY - sections
    all_sections = list(dict.fromkeys(list(CATEGORY_META.keys()) + list(by_section.keys())))
    sections_with_data = [(s, SECTION_NAMES.get(s, s), by_section.get(s, [])) for s in all_sections]
    lines.append("const KANNADA_DICTIONARY = {")
    for i, (sec, name, words) in enumerate(sections_with_data):
        lines.append(f'  {sec}: {{')
        lines.append(f'    name: "{name}",')
        lines.append('    words: [')
        for w in words:
            lines.append("      " + word_js(w) + ",")
        if words:
            lines[-1] = lines[-1].rstrip(",")
        lines.append("    ]")
        lines.append("  }" + ("," if i < len(sections_with_data) - 1 else ""))
    lines.append("};")
    out = "\n".join(lines)
    with open(BASE / "kannada_data.js", "w", encoding="utf-8") as f:
        f.write(out)
    print("Wrote kannada_data.js")

if __name__ == "__main__":
    main()
