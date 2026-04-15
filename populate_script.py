#!/usr/bin/env python3
"""Populate script/alphabet lessons 501-509 (1.1-1.9) – clean sentence/word tables."""
import json, sys
from pathlib import Path

BASE = Path(__file__).parent.resolve()

INDEPENDENT={"ꯑ":"a","ꯏ":"i","ꯎ":"u"}
CONSONANTS_M={"ꯀ":"k","ꯁ":"s","ꯂ":"l","ꯃ":"m","ꯄ":"p","ꯅ":"n","ꯆ":"ch","ꯇ":"t","ꯈ":"kh","ꯉ":"ng","ꯊ":"th","ꯋ":"w","ꯌ":"y","ꯍ":"h","ꯐ":"ph","ꯒ":"g","ꯓ":"jh","ꯔ":"r","ꯕ":"b","ꯖ":"j","ꯗ":"d","ꯘ":"gh","ꯙ":"dh","ꯚ":"bh"}
LONSUM_M={"ꯛ":"k","ꯜ":"l","ꯝ":"m","ꯞ":"p","ꯟ":"n","ꯠ":"t","ꯡ":"ng","ꯢ":"i"}
VOWEL_SIGNS_M={"ꯥ":"aa","ꯤ":"i","ꯨ":"u","ꯦ":"e","ꯣ":"o","ꯧ":"ou","ꯩ":"ei","ꯪ":"ng"}
DIGITS_M={"꯰":"0","꯱":"1","꯲":"2","꯳":"3","꯴":"4","꯵":"5","꯶":"6","꯷":"7","꯸":"8","꯹":"9"}
PUNCT_M={"꯫":".","꯬":"!"}
APUN="꯭"

def m2r(text):
    out=[];i=0
    while i<len(text):
        ch=text[i]
        if ch in DIGITS_M:out.append(DIGITS_M[ch])
        elif ch in PUNCT_M:out.append(PUNCT_M[ch])
        elif ch.isspace():out.append(ch)
        elif ch in INDEPENDENT:
            if i+1<len(text) and text[i+1] in VOWEL_SIGNS_M:
                s=text[i+1];out.append(("ang" if s=="ꯪ" else VOWEL_SIGNS_M[s]) if ch=="ꯑ" else (INDEPENDENT[ch]+("ng" if s=="ꯪ" else VOWEL_SIGNS_M[s])));i+=1
            else:out.append(INDEPENDENT[ch])
        elif ch in CONSONANTS_M:
            base=CONSONANTS_M[ch]
            if i+1<len(text) and text[i+1]==APUN:out.append(base);i+=1
            elif i+1<len(text) and text[i+1] in VOWEL_SIGNS_M:
                s=text[i+1];out.append(base+("ang" if s=="ꯪ" else VOWEL_SIGNS_M[s]));i+=1
            else:out.append(base+"a")
        elif ch in VOWEL_SIGNS_M:out.append("ang" if ch=="ꯪ" else VOWEL_SIGNS_M[ch])
        elif ch in LONSUM_M:out.append(LONSUM_M[ch])
        elif ch==APUN:pass
        else:out.append(ch)
        i+=1
    r="".join(out)
    for o,n in [("  "," "),(" .","."),(" !","!"),(" ?","?")]:r=r.replace(o,n)
    return r.strip()

LESSONS = {

# ━━━ 501: Meitei Mayek alphabet – each letter as a word ━━━
501: {
    "heading": "Meitei Mayek alphabet – basic letters",
    "rows": [
        ("Head", "ꯀꯣꯛ"),
        ("Hair", "ꯁꯝ"),
        ("Flower", "ꯂꯩ"),
        ("Eye", "ꯃꯤꯠ"),
        ("Eyebrow", "ꯄꯥ"),
        ("Ear", "ꯅꯥ"),
        ("Lip", "ꯆꯤꯟ"),
        ("Bridge", "ꯇꯤꯜ"),
        ("Leg", "ꯈꯣꯡ"),
        ("Fish", "ꯉꯥ"),
        ("Moon", "ꯊꯥ"),
        ("Water", "ꯋꯥ"),
        ("Teeth", "ꯌꯥ"),
        ("Hat", "ꯍꯨꯛ"),
        ("Skin", "ꯎꯟ"),
        ("Thread", "ꯏ"),
        ("Place", "ꯐꯝ"),
        ("Sky", "ꯑꯇꯤꯌꯥ"),
        ("Car", "ꯒꯥꯗꯤ"),
        ("Flag", "ꯓꯥꯟꯗꯥ"),
        ("Paddy", "ꯔꯣ"),
        ("Ball", "ꯕꯣꯜ"),
        ("Net", "ꯖꯥꯜ"),
        ("Wealth", "ꯗꯟ"),
        ("Bell", "ꯘꯣꯡ"),
        ("Drum", "ꯙꯣꯜ"),
        ("India", "ꯚꯥꯔꯠ"),
    ],
},

# ━━━ 502: Vowels and consonants – simple words ━━━
502: {
    "heading": "Vowels & consonants – example words",
    "rows": [
        ("About", "ꯑ"),
        ("Thread", "ꯏ"),
        ("Skin", "ꯎꯟ"),
        ("Head", "ꯀꯣꯛ"),
        ("Hair", "ꯁꯝ"),
        ("Flower", "ꯂꯩ"),
        ("Person", "ꯃꯤ"),
        ("Eyebrow", "ꯄꯥ"),
        ("Ear", "ꯅꯥ"),
        ("Tea", "ꯆꯥ"),
        ("Moon", "ꯊꯥ"),
        ("Water", "ꯋꯥ"),
        ("Teeth", "ꯌꯥ"),
        ("Fruit", "ꯍꯩ"),
        ("Cloth", "ꯐꯤ"),
        ("Gate", "ꯒꯦꯠ"),
        ("Rain", "ꯔꯤꯝꯔꯤꯝ"),
        ("Bus", "ꯕꯁ"),
        ("Jar", "ꯖꯥꯔ"),
        ("Day", "ꯗꯤꯟ"),
        ("Fire", "ꯃꯩ"),
        ("Belly", "ꯄꯨꯛ"),
        ("Language", "ꯂꯣꯟ"),
    ],
},

# ━━━ 503: Vowel signs with consonants – example words ━━━
503: {
    "heading": "Vowel signs with consonants – words",
    "rows": [
        ("Crow", "ꯀꯥꯎ"),
        ("Person", "ꯃꯤ"),
        ("Belly", "ꯄꯨꯛ"),
        ("Table", "ꯇꯦꯕꯜ"),
        ("Head", "ꯀꯣꯛ"),
        ("To take", "ꯂꯧꯕ"),
        ("Fire", "ꯃꯩ"),
        ("Value", "ꯁꯪ"),
        ("Ear", "ꯅꯥ"),
        ("Fruit", "ꯍꯩ"),
        ("Long / Tall", "ꯑꯁꯥꯡꯕ"),
        ("Eye", "ꯃꯤꯠ"),
        ("Cooked rice", "ꯆꯥꯛ"),
        ("Name", "ꯃꯃꯤꯡ"),
        ("Leg", "ꯈꯣꯡ"),
        ("Father", "ꯃꯄꯥ"),
        ("Mother", "ꯃꯃꯥ"),
        ("Stone", "ꯅꯨꯡ"),
    ],
},

# ━━━ 504: Pronunciation – similar sounding words ━━━
504: {
    "heading": "Similar sounding words – pronunciation",
    "rows": [
        ("Head", "ꯀꯣꯛ"),
        ("Leg", "ꯈꯣꯡ"),
        ("Eyebrow", "ꯄꯥ"),
        ("Cloth", "ꯐꯤ"),
        ("Moon", "ꯊꯥ"),
        ("Bridge", "ꯇꯤꯜ"),
        ("Bus", "ꯕꯁ"),
        ("India", "ꯚꯥꯔꯠ"),
        ("Dal", "ꯗꯥꯜ"),
        ("Wealth", "ꯙꯣꯟ"),
        ("Car", "ꯒꯥꯗꯤ"),
        ("Bell", "ꯘꯣꯡ"),
        ("Ear", "ꯅꯥ"),
        ("Fish", "ꯉꯥ"),
        ("Hair", "ꯁꯝ"),
        ("Lip", "ꯆꯤꯟ"),
        ("Animal", "ꯁꯥ"),
    ],
},

# ━━━ 505: Final consonants and nasals – words ━━━
505: {
    "heading": "Final consonants & nasal endings – words",
    "rows": [
        ("Head", "ꯀꯣꯛ"),
        ("Flower", "ꯂꯩ"),
        ("Hair", "ꯁꯝ"),
        ("Stand", "ꯂꯦꯞ"),
        ("Lip", "ꯆꯤꯟ"),
        ("Eye", "ꯃꯤꯠ"),
        ("Leg", "ꯈꯣꯡ"),
        ("Cooked rice", "ꯆꯥꯛ"),
        ("Tea", "ꯆꯥ"),
        ("Language", "ꯂꯣꯟ"),
        ("Stone", "ꯅꯨꯡ"),
        ("Belly", "ꯄꯨꯛ"),
        ("Seven", "ꯇꯔꯦꯠ"),
        ("Value", "ꯁꯪ"),
        ("Bamboo shoot", "ꯎꯁꯣꯏ"),
        ("Person", "ꯃꯤ"),
        ("Place", "ꯐꯝ"),
        ("Name", "ꯃꯃꯤꯡ"),
    ],
},

# ━━━ 506: Syllable formation – words broken into parts ━━━
506: {
    "heading": "Syllable formation – example words",
    "rows": [
        ("Eye", "ꯃꯤꯠ"),
        ("Leg", "ꯈꯣꯡ"),
        ("Stone", "ꯅꯨꯡ"),
        ("Fire", "ꯃꯩ"),
        ("Light", "ꯊꯣꯏ"),
        ("Belly", "ꯄꯨꯛ"),
        ("Flower", "ꯂꯩ"),
        ("Teeth", "ꯌꯥ"),
        ("School", "ꯁ꯭ꯀꯨꯜ"),
        ("Cooked rice", "ꯆꯥꯛ"),
        ("Head", "ꯀꯣꯛ"),
        ("Lip", "ꯆꯤꯟ"),
        ("Hair", "ꯁꯝ"),
        ("Father", "ꯃꯄꯥ"),
        ("Mother", "ꯃꯃꯥ"),
        ("Son", "ꯃꯆꯥ ꯅꯨꯄꯥ"),
        ("House", "ꯌꯨꯝ"),
        ("Water", "ꯏꯁꯤꯡ"),
    ],
},

# ━━━ 507: Checked vs open sounds – word pairs ━━━
507: {
    "heading": "Checked vs open sounds – word pairs",
    "rows": [
        ("Cooked rice", "ꯆꯥꯛ"),
        ("Tea", "ꯆꯥ"),
        ("To place", "ꯊꯥꯛ"),
        ("Moon", "ꯊꯥ"),
        ("To cut", "ꯁꯥꯠ"),
        ("Animal", "ꯁꯥ"),
        ("Stand", "ꯂꯦꯞ"),
        ("Flower", "ꯂꯩ"),
        ("Belly", "ꯄꯨꯛ"),
        ("Head", "ꯀꯣꯛ"),
        ("Eye", "ꯃꯤꯠ"),
        ("Person", "ꯃꯤ"),
        ("Hair", "ꯁꯝ"),
        ("Language", "ꯂꯣꯟ"),
        ("Leg", "ꯈꯣꯡ"),
        ("Seven", "ꯇꯔꯦꯠ"),
        ("Ear", "ꯅꯥ"),
    ],
},

# ━━━ 508: Loan words in Meitei Mayek ━━━
508: {
    "heading": "Loan words in Meitei Mayek",
    "rows": [
        ("Car", "ꯒꯥꯗꯤ"),
        ("Flag", "ꯓꯥꯟꯗꯥ"),
        ("Bell", "ꯘꯣꯡ"),
        ("Wealth", "ꯙꯣꯟ"),
        ("India", "ꯚꯥꯔꯠ"),
        ("Rose", "ꯒꯨꯂꯥꯕ"),
        ("Doctor", "ꯗꯣꯛꯇꯔ"),
        ("Bus", "ꯕꯁ"),
        ("School", "ꯁ꯭ꯀꯨꯜ"),
        ("Table", "ꯇꯦꯕꯜ"),
        ("Radio", "ꯔꯦꯗꯤꯑꯣ"),
        ("Phone", "ꯐꯣꯟ"),
        ("Bank", "ꯕꯦꯡꯛ"),
        ("Train", "ꯇ꯭ꯔꯦꯟ"),
        ("Computer", "ꯀꯝꯄꯤꯎꯇꯔ"),
        ("TV", "ꯇꯤꯚꯤ"),
        ("Hospital", "ꯂꯝꯗꯝ"),
    ],
},

# ━━━ 509: Reading practice – simple sentences ━━━
509: {
    "heading": "Reading practice – simple sentences",
    "rows": [
        ("My name is Tomba.", "ꯑꯩꯒꯤ ꯃꯃꯤꯡ ꯇꯣꯝꯕꯅꯤ꯫"),
        ("I live in Imphal.", "ꯑꯩ ꯏꯝꯐꯥꯜꯗ ꯂꯩꯔꯤ꯫"),
        ("Water is cold.", "ꯏꯁꯤꯡ ꯑꯏꯡꯏ꯫"),
        ("The sun is hot.", "ꯅꯨꯃꯤꯠ ꯑꯁꯥꯏ꯫"),
        ("I eat rice.", "ꯑꯩ ꯆꯦꯡ ꯆꯥꯏ꯫"),
        ("She reads a book.", "ꯃꯍꯥꯛ ꯂꯥꯏꯔꯤꯛ ꯄꯥꯏ꯫"),
        ("The flower is beautiful.", "ꯂꯩ ꯑꯁꯤ ꯐꯖꯩ꯫"),
        ("He goes to school.", "ꯃꯍꯥꯛ ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯏ꯫"),
        ("The fish is in the river.", "ꯉꯥ ꯇꯨꯔꯦꯟꯗ ꯂꯩꯔꯤ꯫"),
        ("Mother cooks food.", "ꯏꯃꯥ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯏ꯫"),
        ("Father goes to work.", "ꯏꯄꯥ ꯊꯧꯔꯝꯗ ꯆꯠꯏ꯫"),
        ("Children play outside.", "ꯑꯉꯥꯡꯁꯤꯡ ꯃꯄꯥꯟꯗ ꯁꯥꯏ꯫"),
        ("The dog is sleeping.", "ꯍꯨꯏ ꯇꯨꯝꯔꯤ꯫"),
        ("Today is Monday.", "ꯉꯁꯤ ꯅꯣꯡꯃꯥꯏꯖꯤꯡꯅꯤ꯫"),
        ("Manipur is beautiful.", "ꯃꯅꯤꯄꯨꯔ ꯐꯖꯩ꯫"),
        ("I love my country.", "ꯑꯩ ꯑꯩꯒꯤ ꯂꯩꯄꯥꯛꯕꯨ ꯅꯨꯡꯁꯤ꯫"),
        ("Good night.", "ꯑꯍꯤꯡꯒꯤ ꯐꯕ ꯐꯡꯕꯤꯌꯨ꯫"),
    ],
},

}

def main():
    path = BASE / "data_meitei.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    updated = 0
    for chapter in data:
        cid = chapter["id"]
        if cid not in LESSONS:
            continue
        lesson = LESSONS[cid]
        rows_with_translit = []
        for eng, mayek in lesson["rows"]:
            translit = m2r(mayek)
            rows_with_translit.append([eng, mayek, translit])
        new_table = {
            "type": "table",
            "heading": lesson["heading"],
            "headers": ["English", "Manipuri", "Transliteration"],
            "speakCol": 1,
            "rows": rows_with_translit,
        }
        chapter["blocks"] = [new_table]
        chapter.pop("intro", None)
        chapter.pop("content", None)
        updated += 1
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sys.stdout.buffer.write(f"Updated {updated} script lessons (501-509) in data_meitei.json\n".encode("utf-8"))

if __name__ == "__main__":
    main()
