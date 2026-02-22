#!/usr/bin/env python3
"""Build Barakhadi table rows for data.json - same format as consonants alphabet grid."""

# Barakhadi chart: each consonant row has 15 symbols
# Order: अ आ इ ई उ ऊ ए ऐ ओ औ अं अः अॅ ऑ हलंत
# Transliteration suffixes: a A i I u U e ai o au aM aH ~a ~o (half = just consonant)

CONSONANTS = [
    ("क", "k"), ("ख", "kh"), ("ग", "g"), ("घ", "gh"),
    ("च", "ch"), ("छ", "chh"), ("ज", "j"), ("झ", "jh"),
    ("ट", "ṭ"), ("ठ", "ṭh"), ("ड", "ḍ"), ("ढ", "ḍh"), ("ण", "ṇ"),
    ("त", "t"), ("थ", "th"), ("द", "d"), ("ध", "dh"), ("न", "n"),
    ("प", "p"), ("फ", "ph"), ("ब", "b"), ("भ", "bh"), ("म", "m"),
    ("य", "y"), ("र", "r"), ("ल", "l"), ("व", "v"),
    ("श", "ś"), ("ष", "ṣ"), ("स", "s"), ("ह", "h"),
    ("ळ", "ḷ"), ("क्ष", "kṣ"), ("ज्ञ", "jñ"),
]

# Devanagari symbols per row (15 per consonant)
SYMBOLS = [
    "", "ा", "ि", "ी", "ु", "ू", "े", "ै", "ो", "ौ", "ं", "ः", "ॅ", "ॉ", "्\u200c"
]

# Roman suffixes for each of the 15
SUFFIXES = ["a", "A", "i", "I", "u", "U", "e", "ai", "o", "au", "aM", "aH", "~a", "~o", ""]

def build_rows():
    rows = []
    for dev, base in CONSONANTS:
        for sym, suf in zip(SYMBOLS, SUFFIXES):
            dev_char = dev + sym if sym else dev
            rom = base + suf
            rows.append([dev_char, rom])
    return rows

if __name__ == "__main__":
    import json
    rows = build_rows()
    with open("barakhadi_rows.json", "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
