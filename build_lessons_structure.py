#!/usr/bin/env python3
"""
Build lessons_structure.json from data.json using fuzzy matching.
Matches user's sublesson titles to chapters in data.json.
"""

import json
import re
from pathlib import Path

# User's hierarchical list from the parent message
USER_LESSONS = {
    "Introductory lessons": [
        "Welcome to world of Marathi",
        "Tips to Learn Marathi (rather any new language)",
    ],
    "Marathi Script - Writing & Pronunciation": [
        "Marathi Alphabets Devanagari Alphabets",
        "Vowels, Consonants in Marathi and their pronunciation",
        "Marathi Barakahadi : Symbols for vowels with consonants",
        "Frequently faced pronunciation problems in Marathi (Devanagari)",
        "Pronunciation of Anusvar अनुस्वार",
        "Combining consonants in Marathi मराठी जोडाक्षरे",
        "Combining consonants with र(r)-मराठी जोडाक्षरे Part 2",
        "Combining consonants with ह(h)-मराठी जोडाक्षरे Part 3",
        "Special or separate symbols for combined consonants मराठी जोडाक्षरे- part 3",
    ],
    "Sentence formation rules in different tenses & pronouns forms": [
        "Pronouns and Articles in Marathi",
        "Using plurals to indicate respect आदरार्थी बहुवचन (AdarArthI bahuvachan )",
        "Verbs in Marathi",
        "Simple Present Tense in Marathi",
        "Simple Present Tense of \"To Be\" in Marathi",
        "Present Continuous Tense in Marathi",
        "Simple Future Tense in Marathi",
        "Future Continuous Tense in Marathi",
        "Simple Past Tense in Marathi – Part 1 (Verbs without noun)",
        "Simple Past Tense in Marathi – Part 2 (Verbs with object)",
        "Simple Past Tense in Marathi – Part 3 (Past tense of \"to be\")",
        "Exceptional Verbs in Marathi which change in past tense form",
        "Past Continuous Tense in Marathi",
        "Present/Past/Future Perfect Tense in Marathi",
        "Learn Prepositions in Marathi",
        "Preposition \"TO\" in Marathi",
        "Sentences with person or living things as object",
        "Saying My/His/Her in Marathi",
        "Basic questions and \"WH\" questions in Marathi",
        "Negative Sentences – Present tense in Marathi",
        "Negative Sentences – Past tense in Marathi",
        "Negative Sentence – Future Tense in Marathi",
        "Working with nouns – Gender & Plurals in Marathi",
        "Working with nouns – Prepositions in Marathi",
        "Prepositions with similar pronunciation or similar meanings",
        "Cases in Marathi. विभक्ति Vibhakti and विभक्तिप्रत्यय vibhaktiprtatyay in Marathi",
        "Commands / Imperative statements in Marathi",
        "Time related words",
        "Verbs indicating cause of action. Causative verb",
        "आ-ई-ए-ए-या-ई (A-I-e-e-yA-I) rule",
        "Past/Present/Future Perfect Tense – Second Style",
        "Past /Present/Future Perfect Continuous tense in Marathi",
        "Difference between नाही(nAhI) and नको (nako)",
    ],
    "Phrases & other sentence structures": [
        "Sentence using \"Going to\" phrase",
        "Sentence using \"Used to\" phrase",
        "Sentence using \"Used to\" phrase – old style",
        "Sentence using \"If-Then\"",
        "Prepositions with Verbs",
        "Adjectives in Marathi",
        "Using verb \"Can/To be able to\"",
        "Using verb To Want/To Need",
        "Verb \"To Become/To Happen\"",
        "Using \"Should\"",
        "Using \"Must\"/\"to be have to\"",
        "Using phrase \"to keep doing\"",
        "Comparison and degrees of comparison",
        "Using verb \"To Know\"",
        "Using \"Let\" and \"Shall we\"",
        "Which-That / What-That sentences",
        "Giving instructions formally",
        "Using \"To Like\"",
        "Sentences using \"would\" in Marathi",
        "\"To Understand\" & \"To come to know\"",
        "Add a question tag",
        "Using verb \"To remember\" in Marathi",
        "Using \"To Want\"/\"To Need\" with other verbs",
        "Using \"To Want\" with other person",
        "Using phrase \"supposed to\" in Marathi",
        "Using \"To Like\" with other verbs",
        "Verbs which use preposition \"To\" with subject and verb form as per object",
        "Short forms in spoken Marathi",
        "Greeting,Wishes,Blessings,Slogans in Marathi",
        "Abuse Cursing Swear-words in Marathi",
        "Compound verbs / Phrases in Marathi",
        "Calling or Addressing someone in Marathi",
        "Exclamations in Marathi",
        "Requesting-someone-\"May-I\",\"Can-you\" etc.",
        "Showing uncertainty using May, Might",
        "Adjectives made from verb",
        "Adjectives related to prepositions",
        "Using May to express wish",
        "Phrase \"To Make Someone do something\"",
        "To emphasize word using-च(ch)-in Marathi",
        "Generalizing words – somewhere somehow anything anybody etc.तरी(tarI) -ही(hI)",
        "\"To have\" to indicate possession and relation",
        "Using \"To mean\". How to ask meaning in Marathi",
        "Conjunctions in Marathi – Part 1 And,But,Because,So,That,Although,Though,Still,Yet",
        "Conjunctions in Marathi – Part 2 As,As well as,Or, Neither, Nor, If,in case, provided",
        "Conjunctions in Marathi – Part 3 After, then,As far as, As long as,As if, As though",
        "Conjunctions in Marathi Part-4 As Soon as, Once,Rather Than, Instead of,So that,Whereas,Whether or not,also",
        "List of Conjunctions in Marathi",
        "Combining sentences – change in form of verb असणे(asaNe)",
        "Compound verbs in Marathi",
        "Active Passive voice in Marathi",
        "Active Passive voice in Marathi – Style2",
        "Using \"To Feel\" & \"To think\"",
        "Idioms and Phrases in Marathi / different sentence formation in Marathi",
        "Idioms and Phrases in Marathi / different sentence formation in Marathi Part2",
        "Sentences using \"If-Then\" Style 2",
    ],
    "Vocabulary": [
        "List of Body parts in Marathi",
        "Frequently used words. Miscellenious",
        "Relations in Marathi",
        "Numbers in Marathi – Part 1",
        "Numbers in Marathi – Part 2",
        "Fractional numbers, sequence, percentage in Marathi",
        "Frequently used verbs in Marathi – Part 1",
        "Frequently used verbs in Marathi – Part 2",
        "Frequently used verbs in Marathi – Part 3",
        "Frequently used verbs in Marathi – Part 4",
        "लावणे(lAvaNe) – one verb, multiple meanings !!",
        "लागणे(lAgaNe) – one verb, multiple meanings !!",
        "List of Marathi Adjectives – Part 1",
        "Adverbs in Marathi – Part 1",
        "List of adverbs in Marathi",
        "List of vegetable names in Marathi",
        "List of names of fruits in Marathi",
        "List of names of birds in Marathi",
        "List of names of insects in Marathi",
        "List of name of colours in Marathi",
        "List of names of flowers in Marathi",
        "List of names of animals in Marathi",
        "Frequently used or common words in Marathi – Miscellaneous",
    ],
    "Conversation practice": [
        "Diwali Festival",
        "Simple Sentences in Marathi – Introduction/Salutation",
        "Simple Marathi Sentences – Time Related",
        "Simple Marathi Sentences – Where/Place Related",
        "Simple Marathi Sentences – In Hotel",
        "Simple Marathi sentences – Weather related",
        "Marathi conversation-with traffic police",
        "Simple Marathi conversation – Rickshaw/Taxi driver",
        "Simple Marathi Conversation – Software Engineers",
        "Simple Marathi conversation – Grocery shop",
        "Simple Marathi Conversation – Doctor-Patient",
        "Simple Marathi Conversation – Teacher & Students",
        "Simple Marathi conversation – Informal phone conversation",
        "Simple Marathi conversation-Vegetable Market",
        "Simple Marathi Conversation-at-bus stop and in bus",
        "Asking address in Marathi",
        "I Love you In Marathi. Proposing someone in Marathi",
        "Simple Marathi Conversation – Interview in Marathi",
        "Simple Marathi conversation – with housemaid",
        "Simple Marathi conversation: Linking AADHAR card to mobile number",
        "Simple Marathi conversation: Linking mobile number to AADHAR card",
        "Simple Marathi conversation : Republic Day 26th January celebration in India",
        "Simple Marathi conversation : In Bank",
        "Simple Marathi Conversation : Enquiry about Temple Visit",
        "Simple Marathi conversation : with friend's parents at lunch table",
        "Simple Marathi conversation : A friend talking with other about his football match",
        "Simple Marathi conversation : Friends plan to watch movie",
        "Simple Marathi conversation : Friends talking about football world cup",
        "Simple Marathi conversation – Tour guide in Singapore speaks with Marathi tourists",
        "Simple Marathi Conversation – Marathi Language Proficiency Test (LPT) for banks",
        "Simple Marathi conversation about food, lunch, meal",
        "Simple Marathi Conversation – About hobby class",
        "Frequently used sentences in Marathi – miscellaneous",
        "Frequently used sentences in Marathi – miscellaneous part 2",
        "Learn Marathi by Communicative Approach",
        "Simple Marathi sentences practice-1",
        "Marathi practice session 4 – prepositions",
        "Marathi practice session 5 – prepositions",
        "Marathi practice session 6 – prepositions",
        "Marathi jokes … Learn Marathi in a fun way",
        "Daily Marathi reading practise … Marathi jokes, thoughts, quotes",
        "Simple Marathi sentences – My experience with Social Media",
        "Conversation about the eclipse",
        "International Women's Day 2021",
        "Learning Marathi for #TejRan with Kaushik",
        "Learning Marathi with Celebrities and Kaushik",
        "Learn Marathi for Shiv Thakre Marathi BigBoss Winner BigBoss 16",
        "Simple Marathi conversation – Quarrel at home",
    ],
    "Additional resources": [
        "Practise Marathi online ! Let's talk on Skype or Hangout",
        "Using LearnMarathiWithKaushik.com to practice grammar rules",
        "\"Marathi Dictionary for Learners\" website and Android app on Gogle Play.",
        "Type Marathi in Roman Marathi transliteration",
    ],
}


def normalize(s):
    """Normalize string for comparison."""
    s = re.sub(r'[–-]', '-', s)  # normalize dashes
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s


def extract_keywords(s):
    """Extract significant words (skip common words)."""
    skip = {'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'of', 'and', 'or', 'etc'}
    words = re.findall(r'\b[a-zA-Z\u0900-\u097F]+\b', s.lower())
    return [w for w in words if w not in skip and len(w) > 1]


def is_part2(title):
    """Check if title refers to Part 2 (or Part2, Part 3, etc.)."""
    t = title.lower()
    return 'part 2' in t or 'part2' in t or 'part 3' in t or 'part3' in t


# Explicit overrides for ambiguous duplicates (sublesson_key -> chapter_id)
EXPLICIT_OVERRIDES = {
    "idioms and phrases in marathi / different sentence formation in marathi": 4,
    "idioms and phrases in marathi / different sentence formation in marathi part2": 83,
}


def match_sublesson(sublesson_title, chapters_by_id, used_ids):
    """
    Find best matching chapter for sublesson title.
    Fuzzy matching: exact match > title contains > keywords match.
    First match wins for duplicates. For Part 1/Part 2, match part number.
    """
    sub_norm = normalize(sublesson_title)
    if sub_norm in EXPLICIT_OVERRIDES:
        cid = EXPLICIT_OVERRIDES[sub_norm]
        if cid not in used_ids:
            return cid

    sub_keywords = set(extract_keywords(sublesson_title))
    sub_is_part2 = is_part2(sublesson_title)

    def score_part_match(ch_title):
        """Prefer same Part 1/Part 2 designation."""
        ch_is_part2 = is_part2(ch_title)
        return 1 if (sub_is_part2 == ch_is_part2) else 0

    # Try exact match first
    for ch in chapters_by_id.values():
        if ch['id'] in used_ids:
            continue
        if normalize(ch['title']) == sub_norm:
            return ch['id']

    # Try chapter title contains sublesson title (case insensitive)
    # For Part 1/Part 2, prefer chapter with matching part designation
    candidates = []
    for ch in chapters_by_id.values():
        if ch['id'] in used_ids:
            continue
        if sub_norm in normalize(ch['title']):
            candidates.append((ch['id'], score_part_match(ch['title'])))
    if candidates:
        candidates.sort(key=lambda x: (-x[1], x[0]))
        return candidates[0][0]

    # Try sublesson title contains key part of chapter title
    for ch in chapters_by_id.values():
        if ch['id'] in used_ids:
            continue
        ch_norm = normalize(ch['title'])
        if ch_norm in sub_norm:
            return ch['id']

    # Try keyword overlap (with Part match preference)
    best_match = None
    best_score = -1
    for ch in chapters_by_id.values():
        if ch['id'] in used_ids:
            continue
        ch_keywords = set(extract_keywords(ch['title']))
        overlap = len(sub_keywords & ch_keywords)
        part_bonus = score_part_match(ch['title']) * 10
        score = overlap + part_bonus
        if overlap >= 2 and score > best_score:
            best_score = score
            best_match = ch['id']

    if best_match:
        return best_match

    # Try partial match
    for ch in chapters_by_id.values():
        if ch['id'] in used_ids:
            continue
        ch_norm = normalize(ch['title'])
        if any(kw in ch_norm for kw in sub_keywords if len(kw) > 3):
            return ch['id']

    return None


def main():
    base = Path(__file__).parent
    data_path = base / "data.json"
    output_path = base / "lessons_structure.json"

    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    chapters_by_id = {ch["id"]: ch for ch in data}
    used_ids = set()

    major_lessons = []

    for major_name, sublessons in USER_LESSONS.items():
        sublesson_list = []
        for sub_title in sublessons:
            chapter_id = match_sublesson(sub_title, chapters_by_id, used_ids)
            if chapter_id is not None:
                used_ids.add(chapter_id)
            sublesson_list.append({
                "title": sub_title,
                "chapterId": chapter_id
            })

        major_lessons.append({
            "name": major_name,
            "sublessons": sublesson_list
        })

    result = {"majorLessons": major_lessons}

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Written {output_path}")
    unmatched = sum(1 for m in major_lessons for s in m["sublessons"] if s["chapterId"] is None)
    print(f"Total sublessons: {sum(len(m['sublessons']) for m in major_lessons)}")
    print(f"Unmatched: {unmatched}")


if __name__ == "__main__":
    main()
