#!/usr/bin/env python3
"""
Build lessons_structure_gujarati.json from data_gujarati.json.
Maps user's sublesson titles to chapter IDs (by order - same as scrape order).
"""

import json
from pathlib import Path

USER_LESSONS = {
    "Introductory Lessons": [
        "Welcome to world of Gujarati",
        "Tips to Learn Gujarati (rather any new language)",
    ],
    "Gujarati Script – Writing & Pronunciation": [
        "Alphabets in Gujarati Script",
        "Gujarati Barakhadi/Barakshari",
        "Pronunciation of Anusvar અનુસ્વાર in Gujarati",
        "Combining consonants in Gujarati ગુજરાતી જોડાક્ષર",
        "Combining consonants with ર(r)-ગુજરાતી જોડાક્ષર Part 2",
        "Combining consonants with હ(h)-ગુજરાતી જોડાક્ષર Part 3",
        "Special or separate symbols for combined consonants ગુજરાતી જોડાક્ષર- part 4",
    ],
    "Sentence formation rules in different tenses & pronouns forms": [
        "Pronouns and Articles in Gujarati",
        "Working with Nouns,Genders and plurals in Gujarati",
        "ઓ-ઈ-ઉં-આ-ઈ-આં (o-I-uM-A-I-AM ) યો-ઈ-યું-યા-ઈ-યાં ( yo-I-yuM-yA-I-yAM ) rule",
        "Using plurals to indicate respect આદરાર્થી બહુવચન (AdarArthI bahuvachan )",
        "Verbs in Gujarati",
        "Simple Present Tense of \"To Be\" in Gujarati",
        "Simple Present Tense in Gujarati",
        "Simple Future Tense in Gujarati",
        "Simple Past Tense of \"To Be\" in Gujarati",
        "Simple Past tense in Gujarati – Part 1",
        "Simple Past tense in Gujarati – Part 2",
        "Present Continuous tense in Gujarati",
        "Past Continuous Tense in Gujarati",
        "Future Continuous tense in Gujarati",
        "Negative Sentence in Simple Present tense in Gujarati",
        "Negative Sentence in present continuous tense in Gujarati",
        "Negative sentence in simple past tense in Gujarati",
        "Negative sentence in past continuous tense in Gujarati",
        "Negative sentences in simple future tense in Gujarati",
        "Negative Sentence in future continuous tense in Gujarati",
        "Present-Past-Future Perfect Tense in Gujarati",
        "Past /Present/Future Perfect Continuous tense in Gujarati",
        "Commands / Imperative statements in Gujarati",
        "Saying My/His/Her in Gujarati",
        "Preposition \"TO\" in Gujarati",
        "Sentences with person or human being as object",
        "Asking questions in Gujarati – Part 1",
        "Asking WH questions in Gujarati",
        "Learn Prepositions in Gujarati Language",
        "Prepositions with nouns in Gujarati",
        "Cases in Gujarati. વિભક્તિ Vibhakti and વિભક્તિ પ્રત્યય vibhakti prtatyay in Gujarati",
        "Asking WH-questions with prepositions in Gujarati",
        "Adjectives in Gujarati",
    ],
    "Phrases & other sentence structures": [
        "Using phrase \"to keep doing\" in Gujarati",
        "Using verb \"To want\" in Gujarati",
        "Using verb \"To Know\" in Gujarati",
        "Saying \"To come to know\" in Gujarati",
        "Using \"To Understand\" in Gujarati",
        "Using \"To Like\" in Gujarati",
        "Using \"Going to\" phrase in Gujarati",
        "Using verb \"Can/To be able to\" in Gujarati",
        "Using verb \"To remember\" in Gujarati",
        "Using \"To Want\" \"To Need\" with other verbs in Gujarati",
        "Using \"Should\" in Gujarati",
        "Sentences using \"would\" in Gujarati",
        "Saying phrase \"must\" \"have to\" in Gujarati",
        "Prepositions with verbs in Gujarati",
        "Using \"Let\" and \"Shall we\" in Gujarati",
        "Saying \"To Become\" \"To Happen\" in Gujarati",
        "Asking permission and requesting someone \"May I\" \"Can you\" etc.",
        "Comparison and degrees of comparison in Gujarati",
        "Sentence using \"If-Then\" in Gujarati",
        "Simple future tense in conditional statements",
        "Sentence using \"Used to\" phrase in Gujarati",
        "Which-That / What-That sentences in Gujarati",
        "Using \"To Feel\" & \"To think\" in Gujarati",
        "Add a question tag in Gujarati",
        "To emphasize word using-જ(j)-in Gujarati",
        "Showing uncertainty using May, Might in Gujarati",
        "Using \"To mean\". How to ask meaning in Gujarati",
        "\"To have\" to indicate possession and relation in Gujarati",
        "Adjectives made from verbs in Gujarati",
        "Generalizing words – somewhere somehow anything anybody etc. – in Gujarati",
        "Adverbs in Gujarati",
        "Using \"like\" to indicate similarity in Gujarati",
        "Active voice and Passive voice in Gujarati",
        "Phrase \"To Make Someone do something\" in Gujarati",
        "Using \"May\" to express wish in Gujarati",
    ],
    "Vocabulary": [
        "Time related words in Gujarati",
        "Numbers in Gujarati – Part 1",
        "Numbers in Gujarati – Part 2",
        "Fractional numbers, sequence, percentage in Gujarati",
        "Conjunctions in Gujarati – Part 1 And,But,Because,So,That,Although,Though,Still,Yet",
        "Conjunctions in Gujarati – Part 2 As,As well as,Or, Neither, Nor, If,in case, provided",
        "Conjunctions in Gujarati- Part 3 After, then,As far as, As long as,As if, As though",
        "Conjunctions in Gujarati Part-4 As Soon as, Once,Rather Than, Instead of,So that,Whereas,Whether or not,also",
        "List of conjunctions in Gujarati",
        "List of Body parts in Gujarati",
        "Relations in Gujarati",
    ],
    "Conversation practice": [
        "Simple Sentences in Gujarati – Introduction/Salutation",
        "Simple Gujarati Sentences Where Place Related",
        "Asking address in Gujarati",
        "Greeting,Wishes,Blessings,Slogans in Gujarati",
        "Simple Gujarati Sentences – In Hotel",
        "Simple Gujarati conversation – Grocery shop",
        "Simple Gujarati Conversation-at-bus stop and in bus",
        "Simple Gujarati conversation – Rickshaw/Taxi driver",
        "Simple Gujarati Conversation – Software Engineers",
        "Simple Gujarati Conversation – Doctor-Patient",
        "Simple Gujarati Conversation – Teacher & Students",
        "Simple Gujarati Conversation – Informal phone conversation",
        "Simple Gujarati conversation-at Vegetable Market",
        "Simple Gujarati conversation-with traffic police",
        "Simple Gujarati sentences – Weather related",
        "Simple Gujarati Conversation – Interview in Gujarati",
        "Simple Gujarati conversation – with housemaid",
        "I Love you In Gujarati. Proposing someone in Gujarati",
        "Simple Gujarati conversation: Linking AADHAR card to mobile number",
    ],
    "Additional resources": [
        "Type Gujarati in Roman. Gujarati transliteration",
    ],
}


def main():
    base = Path(__file__).parent
    data_path = base / "data_gujarati.json"
    output_path = base / "lessons_structure_gujarati.json"

    if not data_path.exists():
        print(f"Run scrape_gujarati_lessons.py first to create {data_path}")
        return

    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Chapters indexed by id; map sublesson titles to chapter ids
    chapters_by_id = {ch["id"]: ch for ch in data}
    ch_by_title = {ch["title"].strip().lower(): ch["id"] for ch in data}

    def find_chapter_id(sub_title):
        t = sub_title.strip().lower()
        if t in ch_by_title:
            return ch_by_title[t]
        for ct, cid in ch_by_title.items():
            if t in ct or ct in t:
                return cid
        return None

    major_lessons = []
    used_ids = set()
    fallback_idx = 0

    for major_name, sublessons in USER_LESSONS.items():
        sublesson_list = []
        for sub_title in sublessons:
            cid = find_chapter_id(sub_title)
            if cid is None or cid in used_ids:
                while fallback_idx < len(data) and data[fallback_idx]["id"] in used_ids:
                    fallback_idx += 1
                cid = data[fallback_idx]["id"] if fallback_idx < len(data) else None
                fallback_idx += 1
            if cid:
                used_ids.add(cid)
            sublesson_list.append({"title": sub_title, "chapterId": cid})

        major_lessons.append({"name": major_name, "sublessons": sublesson_list})

    result = {"majorLessons": major_lessons}
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"Written {output_path}")


if __name__ == "__main__":
    main()
