#!/usr/bin/env python3
import json
from pathlib import Path


BASE = Path(__file__).parent.resolve()


INDEPENDENT = {
    "ꯑ": "a",
    "ꯏ": "i",
    "ꯎ": "u",
}

CONSONANTS = {
    "ꯀ": "k",
    "ꯁ": "s",
    "ꯂ": "l",
    "ꯃ": "m",
    "ꯄ": "p",
    "ꯅ": "n",
    "ꯆ": "ch",
    "ꯇ": "t",
    "ꯈ": "kh",
    "ꯉ": "ng",
    "ꯊ": "th",
    "ꯋ": "w",
    "ꯌ": "y",
    "ꯍ": "h",
    "ꯐ": "ph",
    "ꯒ": "g",
    "ꯓ": "jh",
    "ꯔ": "r",
    "ꯕ": "b",
    "ꯖ": "j",
    "ꯗ": "d",
    "ꯘ": "gh",
    "ꯙ": "dh",
    "ꯚ": "bh",
}

LONSUM = {
    "ꯛ": "k",
    "ꯜ": "l",
    "ꯝ": "m",
    "ꯞ": "p",
    "ꯟ": "n",
    "ꯠ": "t",
    "ꯡ": "ng",
    "ꯢ": "i",
}

VOWEL_SIGNS = {
    "ꯥ": "aa",
    "ꯤ": "i",
    "ꯨ": "u",
    "ꯦ": "e",
    "ꯣ": "o",
    "ꯧ": "ou",
    "ꯩ": "ei",
    "ꯪ": "ng",
}

DIGITS = {
    "꯰": "0",
    "꯱": "1",
    "꯲": "2",
    "꯳": "3",
    "꯴": "4",
    "꯵": "5",
    "꯶": "6",
    "꯷": "7",
    "꯸": "8",
    "꯹": "9",
}

PUNCT = {
    "꯫": ".",
    "꯬": "!",
}

APUN = "꯭"


GENERAL_PACK = [
    "Welcome",
    "Thank you",
    "How are you?",
    "I am fine",
    "What is your name?",
    "My name is...",
    "I am a student",
    "You are a teacher",
    "This is my book",
    "This is my friend",
    "We are happy",
    "She is beautiful.",
    "Good idea",
    "Well done",
    "I don't understand",
    "Please speak slowly",
    "Please say that again",
    "Good morning",
]

SOCIAL_PACK = [
    "Welcome",
    "Thank you",
    "Please",
    "Sorry",
    "Excuse me",
    "How are you?",
    "I am fine",
    "I love you",
    "Take care",
    "I miss you",
    "No problem",
    "Get well soon",
    "No worries",
    "Congratulations",
    "Good luck",
    "See you",
    "Goodbye",
    "Good night",
]

TRAVEL_PACK = [
    "Excuse me",
    "How much is this?",
    "Where is the toilet?",
    "I'm lost",
    "Turn left",
    "Turn right",
    "Straight ahead",
    "How do I get to _____?",
    "...the train station?",
    "...the bus station?",
    "...the airport?",
    "Where can I find hotels?",
    "Where can I find restaurants?",
    "Can you show me on the map?",
    "I need your help",
    "Call the police!",
    "I need a doctor",
    "Can I use your phone?",
]

EMERGENCY_PACK = [
    "Help!",
    "Look out!",
    "Stop!",
    "Call the police!",
    "Police!",
    "Stop! Thief!",
    "I need your help",
    "It's an emergency",
    "I lost my bag",
    "I'm sick",
    "I've been injured",
    "I need a doctor",
    "Can I use your phone?",
    "I haven't done anything wrong",
    "It was a misunderstanding",
    "I want to talk to a lawyer",
    "Fire!",
    "I'm lost",
]

TIME_PACK = [
    "Good morning",
    "Good evening",
    "Good night",
    "How are you?",
    "I am fine",
    "What is your name?",
    "My name is...",
    "I will stay for one night",
    "What time is breakfast?",
    "Long time no see",
    "See you",
    "Have a nice day",
    "Have a nice meal",
    "Thank you",
    "Please",
    "Come in",
    "Please come in",
    "Good luck!",
]


def transliterate_meitei(text):
    out = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch in DIGITS:
            out.append(DIGITS[ch])
        elif ch in PUNCT:
            out.append(PUNCT[ch])
        elif ch.isspace():
            out.append(ch)
        elif ch in INDEPENDENT:
            if i + 1 < len(text) and text[i + 1] in VOWEL_SIGNS:
                sign = text[i + 1]
                if ch == "ꯑ":
                    base = "ang" if sign == "ꯪ" else VOWEL_SIGNS[sign]
                else:
                    base = INDEPENDENT[ch] + ("ng" if sign == "ꯪ" else VOWEL_SIGNS[sign])
                out.append(base)
                i += 1
            else:
                out.append(INDEPENDENT[ch])
        elif ch in CONSONANTS:
            base = CONSONANTS[ch]
            if i + 1 < len(text) and text[i + 1] == APUN:
                out.append(base)
                i += 1
            elif i + 1 < len(text) and text[i + 1] in VOWEL_SIGNS:
                sign = text[i + 1]
                out.append(base + ("ang" if sign == "ꯪ" else VOWEL_SIGNS[sign]))
                i += 1
            else:
                out.append(base + "a")
        elif ch in VOWEL_SIGNS:
            out.append("ang" if ch == "ꯪ" else VOWEL_SIGNS[ch])
        elif ch in LONSUM:
            out.append(LONSUM[ch])
        elif ch == APUN:
            pass
        else:
            out.append(ch)
        i += 1

    roman = "".join(out)
    roman = roman.replace("  ", " ")
    roman = roman.replace(" .", ".")
    roman = roman.replace(" !", "!")
    roman = roman.replace(" ?", "?")
    return roman.strip()


def get_pack(title):
    t = title.lower()
    if any(k in t for k in ["doctor", "police", "emergency", "fire", "lost", "lawyer"]):
        return EMERGENCY_PACK
    if any(k in t for k in ["hotel", "bus", "taxi", "traffic", "address", "bank", "temple", "tour guide", "airport"]):
        return TRAVEL_PACK
    if any(k in t for k in ["time", "morning", "night", "day", "breakfast"]):
        return TIME_PACK
    if any(k in t for k in ["greeting", "wishes", "blessings", "friend", "love", "phone", "movie", "football", "quarrel", "social media"]):
        return SOCIAL_PACK
    return GENERAL_PACK


def build_rows(cache, pack):
    rows = []
    for english in pack:
        item = cache.get(english)
        if not item:
            continue
        meitei = item["mayek"]
        rows.append([english, meitei, transliterate_meitei(meitei)])
    return rows


def main():
    path = BASE / "data_meitei.json"
    cache_path = BASE / "meitei_translate_cache.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    cache = json.loads(cache_path.read_text(encoding="utf-8"))

    for chapter in data:
        pack = get_pack(chapter["title"])
        rows = build_rows(cache, pack)
        if len(rows) < 15:
            rows = build_rows(cache, GENERAL_PACK)

        practice_table = {
            "type": "table",
            "heading": "Practice sentences",
            "headers": ["English", "Manipuri", "Transliteration"],
            "speakCol": 1,
            "rows": rows,
        }

        if chapter.get("blocks"):
            chapter["blocks"] = [blk for blk in chapter["blocks"] if not (blk.get("type") == "table" and blk.get("heading") == "Practice sentences")]
            chapter["blocks"].append(practice_table)
        elif chapter.get("tables"):
            chapter["tables"] = [tbl for tbl in chapter["tables"] if tbl.get("heading") != "Practice sentences"]
            chapter["tables"].append(
                {
                    "heading": "Practice sentences",
                    "headers": ["English", "Manipuri", "Transliteration"],
                    "speakCol": 1,
                    "rows": rows,
                }
            )
        else:
            chapter["blocks"] = [practice_table]

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Added practice tables to", len(data), "Meitei chapters")


if __name__ == "__main__":
    main()
