#!/usr/bin/env python3
"""Populate Section 2 (IDs 510-542) of data_dogri.json — aligned with lessons_structure_dogri.json."""
import json
from pathlib import Path

from dogri_lessons_a import LESSONS_A
from dogri_lessons_b import LESSONS_B

BASE = Path(__file__).parent.resolve()

TITLE_BY_ID = {
    510: "Pronouns and Articles in Dogri",
    511: "Using plurals to indicate respect in Dogri",
    512: "Verbs in Dogri",
    513: "Simple Present Tense in Dogri",
    514: 'Simple Present Tense of "To Be" in Dogri',
    515: "Present Continuous Tense in Dogri",
    516: "Simple Future Tense in Dogri",
    517: "Future Continuous Tense in Dogri",
    518: 'Simple Past Tense in Dogri – Part 1 (Verbs without object)',
    519: 'Simple Past Tense in Dogri – Part 2 (Verbs with object)',
    520: 'Simple Past Tense in Dogri – Part 3 (Past tense of "to be")',
    521: "Exceptional Verbs in Dogri which change in past tense form",
    522: "Past Continuous Tense in Dogri",
    523: "Present/Past/Future Perfect Tense in Dogri",
    524: "Learn Prepositions in Dogri",
    525: 'Preposition "TO" in Dogri',
    526: "Sentences with person or living things as object in Dogri",
    527: "Saying My/His/Her in Dogri",
    528: 'Basic questions and "WH" questions in Dogri',
    529: "Negative Sentences – Present tense in Dogri",
    530: "Negative Sentences – Past tense in Dogri",
    531: "Negative Sentence – Future Tense in Dogri",
    532: "Working with nouns – Gender & Plurals in Dogri",
    533: "Working with nouns – Prepositions in Dogri",
    534: "Prepositions with similar pronunciation or similar meanings in Dogri",
    535: "Cases in Dogri (विभक्ति)",
    536: "Commands / Imperative statements in Dogri",
    537: "Time related words in Dogri",
    538: "Verbs indicating cause of action (Causative verb) in Dogri",
    539: "Gender-number agreement rule in Dogri",
    540: "Past/Present/Future Perfect Tense – Second Style in Dogri",
    541: "Past/Present/Future Perfect Continuous tense in Dogri",
    542: 'Difference between "no/not" and "don\'t want" in Dogri',
}

LESSONS = {**LESSONS_A, **LESSONS_B}


def main():
    path = BASE / "data_dogri.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    updated = 0
    for ch in data:
        cid = ch["id"]
        if cid not in LESSONS:
            continue
        title = TITLE_BY_ID.get(cid, ch.get("url", ""))
        ch["url"] = title
        ch["title"] = title
        ch["blocks"] = [{
            "type": "table",
            "columns": ["English", "Dogri", "Transliteration"],
            "rows": LESSONS[cid],
        }]
        updated += 1
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {updated} grammar lessons (510-542) in data_dogri.json")


if __name__ == "__main__":
    main()
