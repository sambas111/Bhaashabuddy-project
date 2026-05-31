"""Build a cleaned Daily Life English set from extracted_phrases.json.

Output: _dailylife_clean.json with {"phrases": [...en...], "words": [...en...]}.
- Only well-formed English (latin letters, no Devanagari junk).
- Dedup (case-insensitive) and drop anything already present in hindi_data.js.
- Split into phrases (multi-word / sentence) vs words (1-2 short tokens).
"""
import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")

DEV = re.compile(r"[\u0900-\u097F]")
LETTER = re.compile(r"[A-Za-z]")
# acceptable english chars: letters, spaces, common punctuation
OK_CHARS = re.compile(r"^[A-Za-z0-9 ,.\-'?!:;()/&%\"]+$")


def is_clean_english(s: str) -> bool:
    s = s.strip()
    if len(s) < 2 or len(s) > 120:
        return False
    if DEV.search(s):
        return False
    if not LETTER.search(s):
        return False
    # must be mostly ascii latin
    if not OK_CHARS.match(s):
        return False
    # at least half the chars are letters/space
    letters = sum(c.isalpha() or c.isspace() for c in s)
    if letters / len(s) < 0.6:
        return False
    return True


def existing_english_keys() -> set:
    t = open("hindi_data.js", encoding="utf-8").read()
    keys = set()
    for m in re.finditer(r"\{ en: (\"(?:\\.|[^\"\\])*\")", t):
        keys.add(json.loads(m.group(1)).strip().lower())
    return keys


def main():
    data = json.load(open("extracted_phrases.json", encoding="utf-8"))
    existing = existing_english_keys()
    print("existing hindi_data English keys:", len(existing))

    dl = data["by_category"].get("dailyLife", [])
    dict_entries = data.get("dictionary_entries", [])
    print("raw dailyLife phrases:", len(dl), "| raw dictionary entries:", len(dict_entries))

    seen = set(existing)
    phrases, words = [], []

    # Phrases: from dailyLife category (sentences / multi-word)
    for p in dl:
        en = (p.get("en") or "").strip()
        if not is_clean_english(en):
            continue
        key = en.lower()
        if key in seen:
            continue
        seen.add(key)
        # classify
        if len(en.split()) >= 3:
            phrases.append(en)
        else:
            words.append(en)

    # Words: from dictionary entries (typically single words / short)
    for e in dict_entries:
        en = (e.get("en") or "").strip()
        if not is_clean_english(en):
            continue
        key = en.lower()
        if key in seen:
            continue
        seen.add(key)
        if len(en.split()) >= 3:
            phrases.append(en)
        else:
            words.append(en)

    print("clean phrases:", len(phrases), "| clean words:", len(words))
    print("\nsample phrases:", phrases[:12])
    print("\nsample words:", words[:20])

    json.dump({"phrases": phrases, "words": words},
              open("_dailylife_clean.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("\nwrote _dailylife_clean.json")


if __name__ == "__main__":
    main()
