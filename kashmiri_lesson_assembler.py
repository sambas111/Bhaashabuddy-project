# Assembles per-chapter lesson rows from kashmiri_sentence_banks for populate_kashmiri_lessons.py
from __future__ import annotations

import json
from pathlib import Path

from kashmiri_chapter_routes import CHAPTER_TO_BANKS
from kashmiri_sentence_banks import (
    BANK_REGISTRY,
    ROWS_PER_LESSON,
    target_row_count,
)


def _merge_bank_names(names: list[str], n: int = ROWS_PER_LESSON) -> list[list[str]]:
    """Combine named banks; dedupe by English; pad by cycling if needed."""
    rows: list[list[str]] = []
    seen: set[str] = set()
    for name in names:
        for row in BANK_REGISTRY.get(name, []):
            en = row[0]
            if en in seen:
                continue
            seen.add(en)
            rows.append([row[0], row[1], row[2]])
            if len(rows) >= n:
                return rows
    # pad
    flat: list[list[str]] = []
    for name in names:
        flat.extend([list(r) for r in BANK_REGISTRY.get(name, [])])
    if not flat:
        flat = [list(r) for r in BANK_REGISTRY["GREETINGS"]]
    i = 0
    while len(rows) < n:
        r = flat[i % len(flat)]
        rows.append([r[0], r[1], r[2]])
        i += 1
    return rows[:n]


def _route_banks(title: str, chapter_id: int) -> list[str]:
    """Prefer explicit per-sublesson routes (title-aligned); fallback to keyword heuristics."""
    if chapter_id in CHAPTER_TO_BANKS:
        return list(CHAPTER_TO_BANKS[chapter_id])

    return _route_banks_fallback(title, chapter_id)


def _route_banks_fallback(title: str, chapter_id: int) -> list[str]:
    t = title.lower()

    # --- Lesson 1: Script (501–509) — READING_DRILLS first for full-sentence script practice ---
    if 501 <= chapter_id <= 509:
        if chapter_id == 501:
            return ["READING_DRILLS", "SCRIPT_PRONUNCIATION", "GREETINGS", "DAILY"]
        if chapter_id == 502:
            return ["READING_DRILLS", "SCRIPT_PRONUNCIATION", "PRONOUNS", "NUMBERS"]
        if chapter_id == 503:
            return ["READING_DRILLS", "SCRIPT_PRONUNCIATION", "PRESENT", "GREETINGS"]
        if chapter_id == 504:
            return ["READING_DRILLS", "SCRIPT_PRONUNCIATION", "DAILY", "QUESTIONS"]
        if chapter_id == 505:
            return ["READING_DRILLS", "SCRIPT_PRONUNCIATION", "NEGATIVE", "GREETINGS"]
        if chapter_id == 506:
            return ["READING_DRILLS", "SCRIPT_PRONUNCIATION", "PRESENT", "FOOD"]
        if chapter_id == 507:
            return ["READING_DRILLS", "SCRIPT_PRONUNCIATION", "TRAVEL", "DAILY"]
        if chapter_id == 508:
            return ["READING_DRILLS", "SCRIPT_PRONUNCIATION", "FAMILY", "GREETINGS"]
        return ["READING_DRILLS", "SCRIPT_PRONUNCIATION", "IDIOMS", "DAILY"]

    # --- Lesson 2: Grammar (510–542) ---
    if 510 <= chapter_id <= 542:
        if "pronoun" in t or "articles" in t:
            return ["PRONOUNS", "POSSESSION", "QUESTIONS", "PRESENT"]
        if "plural" in t and "respect" in t:
            return ["PRONOUNS", "PRESENT", "GREETINGS"]
        if "verb" in t and "exceptional" not in t and "causative" not in t and "prepositions with verbs" not in t:
            return ["PRESENT", "PAST", "FUTURE", "QUESTIONS"]
        if "simple present" in t and "to be" not in t:
            return ["PRESENT", "DAILY", "FOOD"]
        if "to be" in t or ("present tense of" in t):
            return ["PRESENT", "PRONOUNS", "QUESTIONS"]
        if "continuous" in t:
            return ["PRESENT", "DAILY", "PAST"]
        if "future" in t and "perfect" not in t and "continuous" not in t:
            return ["FUTURE", "PRESENT", "DAILY"]
        if "future continuous" in t:
            return ["FUTURE", "PRESENT", "DAILY"]
        if "past" in t and "continuous" not in t and "perfect" not in t:
            return ["PAST", "PRESENT", "NEGATIVE"]
        if "past continuous" in t:
            return ["PAST", "PRESENT", "DAILY"]
        if "perfect" in t:
            return ["PAST", "FUTURE", "PRESENT"]
        if "preposition" in t and "noun" in t:
            return ["TRAVEL", "POSSESSION", "DAILY"]
        if "preposition" in t and '"to"' in t:
            return ["TRAVEL", "DAILY", "QUESTIONS"]
        if "preposition" in t or "prepositions with similar" in t:
            return ["TRAVEL", "SHOPPING", "DAILY"]
        if "object" in t and "living" in t:
            return ["PRESENT", "PRONOUNS", "QUESTIONS"]
        if "my" in t or "his" in t or "her" in t:
            return ["POSSESSION", "PRONOUNS", "FAMILY"]
        if "wh" in t or "basic questions" in t:
            return ["QUESTIONS", "PRONOUNS", "PRESENT"]
        if "negative" in t:
            return ["NEGATIVE", "PRESENT", "FUTURE"]
        if "gender" in t or "plural" in t:
            return ["PRONOUNS", "PRESENT", "FAMILY"]
        if "cases" in t or "विभक्ति" in title:
            return ["POSSESSION", "PRONOUNS", "TRAVEL"]
        if "imperative" in t or "commands" in t:
            return ["PRESENT", "QUESTIONS", "DAILY"]
        if "time related" in t:
            return ["DAILY", "NUMBERS", "PRESENT"]
        if "causative" in t:
            return ["PRESENT", "PAST", "IDIOMS"]
        if "gender-number" in t or "agreement" in t:
            return ["PRONOUNS", "PRESENT", "PAST"]
        if "no/not" in t or "don't want" in t:
            return ["NEGATIVE", "POSSESSION", "PRESENT"]
        return ["PRESENT", "PAST", "FUTURE", "QUESTIONS", "PRONOUNS"]

    # --- Lesson 3: Phrases & structures (543–596) ---
    if 543 <= chapter_id <= 596:
        if "going to" in t:
            return ["FUTURE", "DAILY", "TRAVEL"]
        if "used to" in t:
            return ["PAST", "DAILY", "IDIOMS"]
        if "if-then" in t or "if then" in t:
            return ["FUTURE", "QUESTIONS", "IDIOMS"]
        if "preposition" in t and "verb" in t:
            return ["TRAVEL", "PRESENT", "DAILY"]
        if "adjective" in t:
            return ["PRESENT", "DAILY", "SHOPPING"]
        if "can" in t or "able" in t:
            return ["QUESTIONS", "PRESENT", "DAILY"]
        if "want" in t or "need" in t:
            return ["POSSESSION", "FOOD", "DAILY"]
        if "become" in t or "happen" in t:
            return ["PRESENT", "IDIOMS", "DAILY"]
        if "should" in t or "must" in t or "have to" in t:
            return ["DAILY", "NEGATIVE", "FUTURE"]
        if "keep doing" in t:
            return ["PRESENT", "PAST", "DAILY"]
        if "comparison" in t or "degrees" in t:
            return ["PRESENT", "SHOPPING", "DAILY"]
        if "know" in t:
            return ["QUESTIONS", "PRESENT", "NEGATIVE"]
        if "let" in t or "shall we" in t:
            return ["DAILY", "FUTURE", "GREETINGS"]
        if "which-that" in t or "what-that" in t:
            return ["QUESTIONS", "PRESENT", "DAILY"]
        if "instructions" in t or "formally" in t:
            return ["DAILY", "GREETINGS", "PRESENT"]
        if "like" in t:
            return ["FOOD", "DAILY", "PRESENT"]
        if "would" in t:
            return ["PAST", "FUTURE", "DAILY"]
        if "understand" in t or "come to know" in t:
            return ["QUESTIONS", "PRESENT", "IDIOMS"]
        if "question tag" in t:
            return ["QUESTIONS", "PRESENT", "NEGATIVE"]
        if "remember" in t:
            return ["PAST", "PRESENT", "DAILY"]
        if "supposed to" in t:
            return ["DAILY", "FUTURE", "PRESENT"]
        if "short forms" in t or "spoken" in t:
            return ["GREETINGS", "DAILY", "IDIOMS"]
        if "greeting" in t or "wishes" in t or "blessings" in t:
            return ["GREETINGS", "IDIOMS", "FAMILY"]
        if "compound" in t:
            return ["IDIOMS", "PRESENT", "DAILY"]
        if "addressing" in t or "calling" in t:
            return ["FAMILY", "GREETINGS", "PRONOUNS"]
        if "exclamation" in t:
            return ["IDIOMS", "GREETINGS", "DAILY"]
        if "may i" in t or "can you" in t or "request" in t:
            return ["QUESTIONS", "GREETINGS", "DAILY"]
        if "uncertainty" in t or "might" in t:
            return ["QUESTIONS", "FUTURE", "DAILY"]
        if "adjective" in t and "verb" in t:
            return ["PRESENT", "PAST", "DAILY"]
        if "passive" in t:
            return ["PAST", "PRESENT", "NEGATIVE"]
        if "feel" in t or "think" in t:
            return ["HEALTH", "IDIOMS", "DAILY"]
        if "idiom" in t:
            return ["IDIOMS", "GREETINGS", "DAILY"]
        if "conjunction" in t or "combining sentences" in t:
            return ["IDIOMS", "DAILY", "PRESENT"]
        if "generalizing" in t or "somewhere" in t:
            return ["TRAVEL", "QUESTIONS", "DAILY"]
        if "to have" in t or "possession" in t:
            return ["POSSESSION", "FAMILY", "DAILY"]
        if "to mean" in t:
            return ["QUESTIONS", "PRESENT", "DAILY"]
        return ["GREETINGS", "IDIOMS", "PRESENT", "DAILY", "QUESTIONS"]

    # --- Lesson 4: Vocabulary (597–619) ---
    if 597 <= chapter_id <= 619:
        if "body" in t:
            return ["BODY", "HEALTH", "DAILY"]
        if "miscellaneous" in t and "frequently" in t:
            return ["DAILY", "FOOD", "TRAVEL", "SHOPPING"]
        if "relation" in t:
            return ["FAMILY", "GREETINGS", "POSSESSION"]
        if "number" in t and "fraction" not in t:
            return ["NUMBERS", "DAILY", "SHOPPING"]
        if "fraction" in t or "percentage" in t:
            return ["NUMBERS", "SHOPPING", "DAILY"]
        if "verb" in t and "frequently" in t:
            return ["PRESENT", "PAST", "DAILY"]
        if "लावब" in title or "देब" in title or "लागब" in title:
            return ["PRESENT", "PAST", "IDIOMS"]
        if "adjective" in t:
            return ["PRESENT", "SHOPPING", "DAILY"]
        if "adverb" in t:
            return ["PRESENT", "DAILY", "QUESTIONS"]
        if "vegetable" in t:
            return ["FOOD", "SHOPPING", "DAILY"]
        if "fruit" in t:
            return ["FOOD", "DAILY", "SHOPPING"]
        if "bird" in t or "insect" in t:
            return ["DAILY", "BODY", "NUMBERS"]
        if "colour" in t or "color" in t:
            return ["SHOPPING", "PRESENT", "DAILY"]
        if "flower" in t:
            return ["DAILY", "FAMILY", "GREETINGS"]
        if "animal" in t:
            return ["DAILY", "FAMILY", "BODY"]
        return ["DAILY", "FOOD", "FAMILY", "NUMBERS", "BODY"]

    # --- Lesson 5: Conversation (620–662) ---
    if 620 <= chapter_id <= 662:
        if "diwali" in t:
            return ["DIWALI", "GREETINGS", "FAMILY"]
        if "introduction" in t or "salutation" in t:
            return ["GREETINGS", "FAMILY", "DAILY"]
        if "time" in t:
            return ["DAILY", "NUMBERS", "GREETINGS"]
        if "where" in t or "place" in t:
            return ["TRAVEL", "QUESTIONS", "DAILY"]
        if "hotel" in t:
            return ["TRAVEL", "FOOD", "SHOPPING"]
        if "weather" in t:
            return ["DAILY", "IDIOMS", "TRAVEL"]
        if "traffic" in t or "police" in t:
            return ["TRAVEL", "QUESTIONS", "DAILY"]
        if "rickshaw" in t or "taxi" in t:
            return ["TRAVEL", "SHOPPING", "DAILY"]
        if "software" in t or "engineer" in t:
            return ["DAILY", "QUESTIONS", "PRESENT"]
        if "grocery" in t or "vegetable market" in t:
            return ["SHOPPING", "FOOD", "DAILY"]
        if "doctor" in t or "patient" in t:
            return ["HEALTH", "QUESTIONS", "DAILY"]
        if "teacher" in t or "students" in t:
            return ["PRESENT", "QUESTIONS", "GREETINGS"]
        if "phone" in t:
            return ["GREETINGS", "DAILY", "QUESTIONS"]
        if "bus" in t:
            return ["TRAVEL", "SHOPPING", "DAILY"]
        if "address" in t:
            return ["TRAVEL", "QUESTIONS", "DAILY"]
        if "love" in t or "proposing" in t:
            return ["GREETINGS", "IDIOMS", "FAMILY"]
        if "interview" in t:
            return ["QUESTIONS", "PRESENT", "DAILY"]
        if "housemaid" in t:
            return ["DAILY", "FAMILY", "GREETINGS"]
        if "aadhar" in t or "mobile" in t:
            return ["DAILY", "QUESTIONS", "PRESENT"]
        if "republic" in t:
            return ["GREETINGS", "IDIOMS", "DAILY"]
        if "bank" in t:
            return ["SHOPPING", "DAILY", "QUESTIONS"]
        if "temple" in t:
            return ["TRAVEL", "GREETINGS", "FAMILY"]
        if "lunch" in t or "parents" in t:
            return ["FOOD", "FAMILY", "GREETINGS"]
        if "football" in t or "movie" in t or "world cup" in t:
            return ["DAILY", "PRESENT", "IDIOMS"]
        if "tour" in t or "tourist" in t:
            return ["TRAVEL", "GREETINGS", "SHOPPING"]
        if "proficiency" in t or "bank" in t:
            return ["QUESTIONS", "PRESENT", "DAILY"]
        if "food" in t and "lunch" in t:
            return ["FOOD", "FAMILY", "DAILY"]
        if "hobby" in t:
            return ["DAILY", "PRESENT", "IDIOMS"]
        if "frequently used" in t or "miscellaneous" in t:
            return ["GREETINGS", "DAILY", "IDIOMS", "TRAVEL"]
        if "communicative" in t:
            return ["GREETINGS", "DAILY", "QUESTIONS", "PRESENT"]
        if "practice" in t and "sentence" in t:
            return ["DAILY", "PRESENT", "GREETINGS"]
        if "preposition" in t and "practice" in t:
            return ["TRAVEL", "DAILY", "QUESTIONS"]
        if "jokes" in t or "fun" in t:
            return ["IDIOMS", "GREETINGS", "DAILY"]
        if "reading" in t or "quotes" in t:
            return ["IDIOMS", "DAILY", "GREETINGS"]
        if "social media" in t:
            return ["DAILY", "PRESENT", "QUESTIONS"]
        if "eclipse" in t:
            return ["DAILY", "IDIOMS", "QUESTIONS"]
        if "women" in t:
            return ["GREETINGS", "FAMILY", "IDIOMS"]
        if "quarrel" in t:
            return ["NEGATIVE", "FAMILY", "DAILY"]
        return ["GREETINGS", "DAILY", "TRAVEL", "FOOD", "HEALTH", "IDIOMS"]

    return ["GREETINGS", "DAILY", "PRESENT"]


def build_lessons_dict(structure_path: Path | None = None) -> dict[int, list[list[str]]]:
    base = structure_path or (Path(__file__).resolve().parent / "lessons_structure_kashmiri.json")
    data = json.loads(base.read_text(encoding="utf-8-sig"))
    out: dict[int, list[list[str]]] = {}
    for ml in data["majorLessons"]:
        for sub in ml["sublessons"]:
            cid = sub["chapterId"]
            title = sub["title"]
            banks = _route_banks(title, cid)
            out[cid] = _merge_bank_names(banks, target_row_count(cid))
    return out


if __name__ == "__main__":
    L = build_lessons_dict()
    print("lessons", len(L), "sample 501 rows", len(L[501]))
