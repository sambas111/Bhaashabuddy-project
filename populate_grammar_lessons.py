#!/usr/bin/env python3
"""
Populate all 33 Meitei grammar sub-lessons (IDs 510-542) with
topic-relevant sentences: English | Manipuri (Meitei Mayek) | Transliteration.

Sources: manipurian.blogspot.com, languageshome.com, manipuri.fandom.com,
         en.wikipedia.org/wiki/Meitei_grammar, omniglot.com
"""
import json, sys
from pathlib import Path

BASE = Path(__file__).parent.resolve()

# ── Mayek → Roman transliterator (from upgrade_meitei_sentence_tables.py) ──
INDEPENDENT = {"ꯑ": "a", "ꯏ": "i", "ꯎ": "u"}
CONSONANTS_M = {
    "ꯀ": "k", "ꯁ": "s", "ꯂ": "l", "ꯃ": "m", "ꯄ": "p", "ꯅ": "n",
    "ꯆ": "ch", "ꯇ": "t", "ꯈ": "kh", "ꯉ": "ng", "ꯊ": "th", "ꯋ": "w",
    "ꯌ": "y", "ꯍ": "h", "ꯐ": "ph", "ꯒ": "g", "ꯓ": "jh", "ꯔ": "r",
    "ꯕ": "b", "ꯖ": "j", "ꯗ": "d", "ꯘ": "gh", "ꯙ": "dh", "ꯚ": "bh",
}
LONSUM_M = {"ꯛ": "k", "ꯜ": "l", "ꯝ": "m", "ꯞ": "p", "ꯟ": "n", "ꯠ": "t", "ꯡ": "ng", "ꯢ": "i"}
VOWEL_SIGNS_M = {"ꯥ": "aa", "ꯤ": "i", "ꯨ": "u", "ꯦ": "e", "ꯣ": "o", "ꯧ": "ou", "ꯩ": "ei", "ꯪ": "ng"}
DIGITS_M = {"꯰": "0", "꯱": "1", "꯲": "2", "꯳": "3", "꯴": "4", "꯵": "5", "꯶": "6", "꯷": "7", "꯸": "8", "꯹": "9"}
PUNCT_M = {"꯫": ".", "꯬": "!"}
APUN = "꯭"

def mayek_to_roman(text):
    out = []; i = 0
    while i < len(text):
        ch = text[i]
        if ch in DIGITS_M: out.append(DIGITS_M[ch])
        elif ch in PUNCT_M: out.append(PUNCT_M[ch])
        elif ch.isspace(): out.append(ch)
        elif ch in INDEPENDENT:
            if i+1 < len(text) and text[i+1] in VOWEL_SIGNS_M:
                s = text[i+1]
                out.append(("ang" if s == "ꯪ" else VOWEL_SIGNS_M[s]) if ch == "ꯑ" else (INDEPENDENT[ch] + ("ng" if s == "ꯪ" else VOWEL_SIGNS_M[s])))
                i += 1
            else:
                out.append(INDEPENDENT[ch])
        elif ch in CONSONANTS_M:
            base = CONSONANTS_M[ch]
            if i+1 < len(text) and text[i+1] == APUN: out.append(base); i += 1
            elif i+1 < len(text) and text[i+1] in VOWEL_SIGNS_M:
                s = text[i+1]; out.append(base + ("ang" if s == "ꯪ" else VOWEL_SIGNS_M[s])); i += 1
            else: out.append(base + "a")
        elif ch in VOWEL_SIGNS_M: out.append("ang" if ch == "ꯪ" else VOWEL_SIGNS_M[ch])
        elif ch in LONSUM_M: out.append(LONSUM_M[ch])
        elif ch == APUN: pass
        else: out.append(ch)
        i += 1
    r = "".join(out)
    for old, new in [("  ", " "), (" .", "."), (" !", "!"), (" ?", "?")]:
        r = r.replace(old, new)
    return r.strip()


# ── All 33 lessons: each has (English, Meitei Mayek) pairs ──
# The transliteration column is auto-generated via mayek_to_roman()

LESSONS = {

# ━━━ 510: Pronouns and Articles ━━━
510: {
    "heading": "Pronoun and article examples",
    "rows": [
        ("I", "ꯑꯩ"),
        ("You (informal)", "ꯅꯪ"),
        ("You (respectful)", "ꯅꯍꯥꯛ"),
        ("He / She", "ꯃꯍꯥꯛ"),
        ("We", "ꯑꯩꯈꯣꯏ"),
        ("They", "ꯃꯈꯣꯏ"),
        ("This", "ꯃꯁꯤ"),
        ("That", "ꯃꯗꯨ"),
        ("What is your name?", "ꯅꯪꯒꯤ ꯃꯤꯡ ꯀꯔꯤ ꯀꯧꯋꯤ?"),
        ("My name is Tomba", "ꯑꯩꯒꯤ ꯃꯤꯡ ꯇꯣꯝꯕ ꯀꯧꯏ"),
        ("I am a student", "ꯑꯩꯍꯥꯛ ꯃꯍꯩꯔꯣꯌ ꯑꯃꯅꯤ꯫"),
        ("He is a teacher", "ꯃꯍꯥꯛ ꯑꯣꯖꯥ ꯑꯃꯅꯤ꯫"),
        ("This is my book", "ꯃꯁꯤ ꯑꯩꯒꯤ ꯂꯥꯏꯔꯤꯛꯅꯤ꯫"),
        ("That is your pen", "ꯃꯗꯨ ꯅꯪꯒꯤ ꯀꯂꯝꯅꯤ꯫"),
        ("We are happy", "ꯑꯩꯈꯣꯌ ꯅꯨꯡꯉꯥꯏꯕꯥ ꯐꯥꯑꯣꯏ꯫"),
        ("They went to school", "ꯃꯈꯣꯏ ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯂꯨꯏ꯫"),
        ("She is beautiful", "ꯃꯍꯥꯛ ꯐꯖꯩ꯫"),
    ],
},

# ━━━ 511: Using plurals to indicate respect ━━━
511: {
    "heading": "Respectful plural examples",
    "rows": [
        ("You (very respectful)", "ꯑꯗꯣꯝ"),
        ("How are you, sir?", "ꯑꯗꯣꯝ ꯀꯝꯗꯧꯔꯤꯒꯦ?"),
        ("Please come", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯂꯥꯛꯕꯤꯌꯨ꯫"),
        ("Please sit down", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯐꯝꯕꯤꯌꯨ꯫"),
        ("Please tell me", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯑꯩꯕꯨ ꯍꯥꯏꯕꯤꯌꯨ꯫"),
        ("Elders are respected", "ꯏꯕꯨꯉꯣ ꯏꯕꯦꯝꯃꯥ ꯏꯀꯥꯏꯈꯨꯝꯅꯕ꯫"),
        ("Come, sir", "ꯑꯗꯣꯝ ꯂꯥꯛꯕꯤꯌꯨ꯫"),
        ("Please wait", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯉꯥꯏꯕꯤꯌꯨ꯫"),
        ("They all came", "ꯃꯈꯣꯏ ꯄꯨꯝꯅꯃꯛ ꯂꯥꯛꯂꯦ꯫"),
        ("We all are fine", "ꯑꯩꯈꯣꯏ ꯄꯨꯝꯅꯃꯛ ꯅꯨꯉꯥꯏꯔꯤ꯫"),
        ("Respected sir/madam", "ꯏꯕꯨꯉꯣ / ꯏꯕꯦꯝꯃꯥ"),
        ("You (formal) are a teacher", "ꯑꯗꯣꯝ ꯑꯣꯖꯥ ꯑꯃꯅꯤ꯫"),
        ("Please speak slowly", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯇꯞꯅꯥ ꯋꯥ ꯉꯥꯡꯕꯤꯌꯨ꯫"),
        ("You all are welcome", "ꯑꯗꯣꯝꯁꯤꯡ ꯇꯔꯥꯝꯅ ꯑꯣꯛꯆꯔꯤ꯫"),
        ("Thank you very much", "ꯍꯥꯏꯅꯤꯡꯉꯥꯏ ꯂꯩꯇꯅ ꯊꯥꯒꯠꯆꯔꯤ꯫"),
        ("Please say that again", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯑꯃꯨꯛ ꯍꯟꯅꯥ ꯍꯥꯌꯕꯤꯌꯨ꯫"),
        ("Sit here, please", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯑꯁꯤꯗ ꯐꯝꯕꯤꯌꯨ꯫"),
    ],
},

# ━━━ 512: Verbs ━━━
512: {
    "heading": "Basic verb examples",
    "rows": [
        ("Come", "ꯂꯥꯛꯂꯣ"),
        ("Go", "ꯆꯠꯂꯣ"),
        ("Eat", "ꯆꯥꯔꯣ"),
        ("Drink", "ꯊꯛꯂꯣ"),
        ("Sit", "ꯐꯝꯃꯨ"),
        ("Walk", "ꯆꯠꯂꯨ"),
        ("Run", "ꯆꯦꯜꯂꯣ"),
        ("Sleep", "ꯇꯨꯝꯃꯨ"),
        ("Write", "ꯏꯌꯨ"),
        ("Read", "ꯄꯕꯤꯌꯨ"),
        ("Open", "ꯍꯪꯗꯣꯛꯂꯣ"),
        ("I want to go", "ꯑꯩ ꯆꯠꯂꯒꯦ꯫"),
        ("He goes to school", "ꯃꯍꯥꯛ ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯂꯤ꯫"),
        ("She eats rice", "ꯃꯍꯥꯛ ꯆꯥꯛ ꯆꯥꯔꯤ꯫"),
        ("We drink water", "ꯑꯩꯈꯣꯏ ꯏꯁꯤꯡ ꯊꯛꯂꯤ꯫"),
        ("They sleep at night", "ꯃꯈꯣꯏ ꯅꯨꯡꯊꯤꯜꯗ ꯇꯨꯝꯃꯤ꯫"),
        ("I read a book", "ꯑꯩ ꯂꯥꯏꯔꯤꯛ ꯄꯕꯤ꯫"),
    ],
},

# ━━━ 513: Simple Present Tense ━━━
513: {
    "heading": "Simple present tense examples",
    "rows": [
        ("I eat rice", "ꯑꯩ ꯆꯥꯛ ꯆꯥꯏ꯫"),
        ("He goes to school", "ꯃꯍꯥꯛ ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯂꯤ꯫"),
        ("She reads a book", "ꯃꯍꯥꯛ ꯂꯥꯏꯔꯤꯛ ꯄꯕꯤ꯫"),
        ("We play football", "ꯑꯩꯈꯣꯏ ꯐꯨꯠꯕꯣꯜ ꯁꯥꯏ꯫"),
        ("They come every day", "ꯃꯈꯣꯏ ꯅꯨꯃꯤꯠ ꯈꯨꯗꯤꯡꯃꯛ ꯂꯥꯛꯂꯤ꯫"),
        ("You speak Manipuri", "ꯅꯪ ꯃꯩꯇꯩꯂꯣꯟ ꯉꯥꯡꯏ꯫"),
        ("I drink tea", "ꯑꯩ ꯆꯥ ꯊꯛꯂꯤ꯫"),
        ("He writes well", "ꯃꯍꯥꯛ ꯐꯖꯅ ꯏꯏ꯫"),
        ("She walks fast", "ꯃꯍꯥꯛ ꯊꯨꯅ ꯆꯠꯂꯤ꯫"),
        ("We study Meitei", "ꯑꯩꯈꯣꯏ ꯃꯩꯇꯩꯂꯣꯟ ꯇꯝꯏ꯫"),
        ("They sell fruit", "ꯃꯈꯣꯏ ꯍꯩ ꯌꯣꯛꯂꯤ꯫"),
        ("I work every day", "ꯑꯩ ꯅꯨꯃꯤꯠ ꯈꯨꯗꯤꯡꯃꯛ ꯊꯕꯛ ꯇꯧꯏ꯫"),
        ("He loves his mother", "ꯃꯍꯥꯛ ꯃꯍꯥꯛꯀꯤ ꯏꯃꯥꯕꯨ ꯅꯨꯡꯁꯤ꯫"),
        ("She teaches children", "ꯃꯍꯥꯛ ꯑꯅꯧꯕꯁꯤꯡꯕꯨ ꯇꯝꯍꯟꯕꯤ꯫"),
        ("I know the answer", "ꯑꯩ ꯄꯥꯑꯣꯈꯨꯝ ꯈꯪꯏ꯫"),
        ("We live in Manipur", "ꯑꯩꯈꯣꯏ ꯃꯅꯤꯄꯨꯔꯗ ꯂꯩꯏ꯫"),
        ("He speaks English", "ꯃꯍꯥꯛ ꯏꯪꯂꯤꯁ ꯉꯥꯡꯏ꯫"),
    ],
},

# ━━━ 514: Simple Present of "To Be" ━━━
514: {
    "heading": "\"To be\" present tense examples",
    "rows": [
        ("I am a student", "ꯑꯩꯍꯥꯛ ꯃꯍꯩꯔꯣꯌ ꯑꯃꯅꯤ꯫"),
        ("You are a teacher", "ꯅꯍꯥꯛ ꯑꯣꯖꯥ ꯑꯃꯅꯤ꯫"),
        ("He is my friend", "ꯃꯍꯥꯛ ꯑꯩꯒꯤ ꯃꯔꯨꯞꯅꯤ꯫"),
        ("She is beautiful", "ꯃꯍꯥꯛ ꯐꯖꯩ꯫"),
        ("This is a book", "ꯃꯁꯤ ꯂꯥꯏꯔꯤꯛ ꯑꯃꯅꯤ꯫"),
        ("That is my house", "ꯃꯗꯨ ꯑꯩꯒꯤ ꯌꯨꯝꯅꯤ꯫"),
        ("We are Manipuri", "ꯑꯩꯈꯣꯏ ꯃꯅꯤꯄꯨꯔꯤꯅꯤ꯫"),
        ("They are happy", "ꯃꯈꯣꯏ ꯅꯨꯡꯉꯥꯏꯕꯅꯤ꯫"),
        ("It is good", "ꯃꯁꯤ ꯐꯖꯩ꯫"),
        ("Imphal is the capital", "ꯏꯝꯐꯥꯜ ꯀꯦꯞꯏꯇꯜꯅꯤ꯫"),
        ("I am fine", "ꯑꯩꯍꯥꯛ ꯅꯨꯉꯥꯏꯔꯤ꯫"),
        ("It is a flower", "ꯃꯁꯤ ꯂꯩ ꯑꯃꯅꯤ꯫"),
        ("He is tall", "ꯃꯍꯥꯛ ꯁꯪꯅꯤ꯫"),
        ("She is a doctor", "ꯃꯍꯥꯛ ꯗꯣꯛꯇꯔ ꯑꯃꯅꯤ꯫"),
        ("This is water", "ꯃꯁꯤ ꯏꯁꯤꯡꯅꯤ꯫"),
        ("That is my pen", "ꯃꯗꯨ ꯑꯩꯒꯤ ꯀꯂꯝꯅꯤ꯫"),
        ("I am from Manipur", "ꯑꯩ ꯃꯅꯤꯄꯨꯔ ꯗꯒꯤꯅꯤ꯫"),
    ],
},

# ━━━ 515: Present Continuous ━━━
515: {
    "heading": "Present continuous examples",
    "rows": [
        ("I am eating rice", "ꯑꯩ ꯆꯥꯛ ꯆꯥꯔꯝꯃꯤ꯫"),
        ("He is eating an apple", "ꯃꯍꯥꯛ ꯁꯦꯝ ꯑꯃ ꯆꯥꯔꯝꯃꯤ꯫"),
        ("She is reading a book", "ꯃꯍꯥꯛ ꯂꯥꯏꯔꯤꯛ ꯄꯕꯔꯝꯃꯤ꯫"),
        ("We are playing", "ꯑꯩꯈꯣꯏ ꯁꯥꯔꯝꯃꯤ꯫"),
        ("They are going home", "ꯃꯈꯣꯏ ꯌꯨꯝꯗ ꯆꯠꯔꯝꯃꯤ꯫"),
        ("You are writing", "ꯅꯪ ꯏꯔꯝꯃꯤ꯫"),
        ("I am drinking water", "ꯑꯩ ꯏꯁꯤꯡ ꯊꯛꯔꯝꯃꯤ꯫"),
        ("He is sleeping", "ꯃꯍꯥꯛ ꯇꯨꯝꯔꯝꯃꯤ꯫"),
        ("She is cooking food", "ꯃꯍꯥꯛ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯔꯝꯃꯤ꯫"),
        ("We are learning Meitei", "ꯑꯩꯈꯣꯏ ꯃꯩꯇꯩꯂꯣꯟ ꯇꯝꯔꯝꯃꯤ꯫"),
        ("They are watching a movie", "ꯃꯈꯣꯏ ꯐꯤꯜꯝ ꯌꯦꯡꯔꯝꯃꯤ꯫"),
        ("I am walking to school", "ꯑꯩ ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯔꯝꯃꯤ꯫"),
        ("He is running fast", "ꯃꯍꯥꯛ ꯊꯨꯅ ꯆꯦꯜꯔꯝꯃꯤ꯫"),
        ("She is singing a song", "ꯃꯍꯥꯛ ꯏꯁꯩ ꯁꯀꯔꯝꯃꯤ꯫"),
        ("We are waiting here", "ꯑꯩꯈꯣꯏ ꯑꯁꯤꯗ ꯉꯥꯏꯔꯝꯃꯤ꯫"),
        ("What are you doing?", "ꯅꯪ ꯀꯔꯤ ꯇꯧꯔꯤꯕꯒꯦ?"),
        ("I am speaking Manipuri", "ꯑꯩ ꯃꯩꯇꯩꯂꯣꯟ ꯉꯥꯡꯔꯝꯃꯤ꯫"),
    ],
},

# ━━━ 516: Simple Future Tense ━━━
516: {
    "heading": "Simple future tense examples",
    "rows": [
        ("I will eat", "ꯑꯩ ꯆꯥꯒꯅꯤ꯫"),
        ("He will come", "ꯃꯍꯥꯛ ꯂꯥꯛꯀꯅꯤ꯫"),
        ("She will go", "ꯃꯍꯥꯛ ꯆꯠꯀꯅꯤ꯫"),
        ("We will play", "ꯑꯩꯈꯣꯏ ꯁꯥꯒꯅꯤ꯫"),
        ("They will study", "ꯃꯈꯣꯏ ꯇꯝꯒꯅꯤ꯫"),
        ("You will write", "ꯅꯪ ꯏꯒꯅꯤ꯫"),
        ("I will go tomorrow", "ꯑꯩ ꯍꯌꯦꯡ ꯆꯠꯀꯅꯤ꯫"),
        ("He will eat rice", "ꯃꯍꯥꯛ ꯆꯥꯛ ꯆꯥꯒꯅꯤ꯫"),
        ("She will read the book", "ꯃꯍꯥꯛ ꯂꯥꯏꯔꯤꯛ ꯄꯕꯒꯅꯤ꯫"),
        ("We will come back", "ꯑꯩꯈꯣꯏ ꯍꯟꯅ ꯂꯥꯛꯀꯅꯤ꯫"),
        ("They will sleep early", "ꯃꯈꯣꯏ ꯊꯨꯅ ꯇꯨꯝꯒꯅꯤ꯫"),
        ("I will drink water", "ꯑꯩ ꯏꯁꯤꯡ ꯊꯛꯀꯅꯤ꯫"),
        ("He will go to Imphal", "ꯃꯍꯥꯛ ꯏꯝꯐꯥꯜꯗ ꯆꯠꯀꯅꯤ꯫"),
        ("She will cook food", "ꯃꯍꯥꯛ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯒꯅꯤ꯫"),
        ("Will you come with me?", "ꯅꯪ ꯑꯩꯒ ꯂꯥꯛꯀꯗ꯭ꯔ?"),
        ("I will learn Meitei", "ꯑꯩ ꯃꯩꯇꯩꯂꯣꯟ ꯇꯝꯒꯅꯤ꯫"),
        ("We will meet tomorrow", "ꯑꯩꯈꯣꯏ ꯍꯌꯦꯡ ꯎꯅꯅꯁꯤ꯫"),
    ],
},

# ━━━ 517: Future Continuous Tense ━━━
517: {
    "heading": "Future continuous tense examples",
    "rows": [
        ("I will be eating", "ꯑꯩ ꯆꯥꯔꯝꯒꯅꯤ꯫"),
        ("He will be coming", "ꯃꯍꯥꯛ ꯂꯥꯛꯔꯝꯒꯅꯤ꯫"),
        ("She will be going", "ꯃꯍꯥꯛ ꯆꯠꯔꯝꯒꯅꯤ꯫"),
        ("We will be playing", "ꯑꯩꯈꯣꯏ ꯁꯥꯔꯝꯒꯅꯤ꯫"),
        ("They will be studying", "ꯃꯈꯣꯏ ꯇꯝꯔꯝꯒꯅꯤ꯫"),
        ("You will be writing", "ꯅꯪ ꯏꯔꯝꯒꯅꯤ꯫"),
        ("I will be sleeping at that time", "ꯑꯩ ꯃꯇꯝ ꯑꯗꯨꯗ ꯇꯨꯝꯔꯝꯒꯅꯤ꯫"),
        ("He will be working tomorrow", "ꯃꯍꯥꯛ ꯍꯌꯦꯡ ꯊꯕꯛ ꯇꯧꯔꯝꯒꯅꯤ꯫"),
        ("She will be cooking dinner", "ꯃꯍꯥꯛ ꯅꯨꯃꯤꯗꯪ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯔꯝꯒꯅꯤ꯫"),
        ("We will be learning Meitei", "ꯑꯩꯈꯣꯏ ꯃꯩꯇꯩꯂꯣꯟ ꯇꯝꯔꯝꯒꯅꯤ꯫"),
        ("They will be watching", "ꯃꯈꯣꯏ ꯌꯦꯡꯔꯝꯒꯅꯤ꯫"),
        ("I will be reading at 5 o'clock", "ꯑꯩ ꯵ ꯐꯨꯡꯒ ꯄꯕꯔꯝꯒꯅꯤ꯫"),
        ("He will be running in the field", "ꯃꯍꯥꯛ ꯃꯐꯝꯗ ꯆꯦꯜꯔꯝꯒꯅꯤ꯫"),
        ("She will be singing", "ꯃꯍꯥꯛ ꯏꯁꯩ ꯁꯀꯔꯝꯒꯅꯤ꯫"),
        ("We will be waiting for you", "ꯑꯩꯈꯣꯏ ꯅꯪꯕꯨ ꯉꯥꯏꯔꯝꯒꯅꯤ꯫"),
        ("I will be walking home", "ꯑꯩ ꯌꯨꯝꯗ ꯆꯠꯔꯝꯒꯅꯤ꯫"),
        ("They will be dancing", "ꯃꯈꯣꯏ ꯖꯒꯣꯏ ꯁꯥꯔꯝꯒꯅꯤ꯫"),
    ],
},

# ━━━ 518: Simple Past – Part 1 (Verbs without object) ━━━
518: {
    "heading": "Past tense (no object) examples",
    "rows": [
        ("I came", "ꯑꯩ ꯂꯥꯛꯂꯦ꯫"),
        ("He went", "ꯃꯍꯥꯛ ꯆꯠꯂꯦ꯫"),
        ("She slept", "ꯃꯍꯥꯛ ꯇꯨꯝꯂꯦ꯫"),
        ("We ran", "ꯑꯩꯈꯣꯏ ꯆꯦꯜꯂꯦ꯫"),
        ("They sat", "ꯃꯈꯣꯏ ꯐꯝꯂꯦ꯫"),
        ("I walked", "ꯑꯩ ꯆꯠꯂꯦ꯫"),
        ("He stood up", "ꯃꯍꯥꯛ ꯂꯦꯞꯂꯦ꯫"),
        ("She cried", "ꯃꯍꯥꯛ ꯀꯞꯂꯦ꯫"),
        ("They laughed", "ꯃꯈꯣꯏ ꯅꯣꯛꯂꯦ꯫"),
        ("I fell", "ꯑꯩ ꯇꯥꯛꯂꯦ꯫"),
        ("He came yesterday", "ꯃꯍꯥꯛ ꯉꯔꯪ ꯂꯥꯛꯂꯦ꯫"),
        ("She went home", "ꯃꯍꯥꯛ ꯌꯨꯝꯗ ꯆꯠꯂꯦ꯫"),
        ("We played yesterday", "ꯑꯩꯈꯣꯏ ꯉꯔꯪ ꯁꯥꯂꯦ꯫"),
        ("They arrived today", "ꯃꯈꯣꯏ ꯉꯁꯤ ꯊꯨꯡꯂꯦ꯫"),
        ("He slept the whole night", "ꯃꯍꯥꯛ ꯅꯨꯡꯗꯪ ꯆꯨꯞꯄ ꯇꯨꯝꯃꯤ꯫"),
        ("She came by bus", "ꯃꯍꯥꯛ ꯕꯁꯗ ꯂꯥꯛꯂꯦ꯫"),
        ("I stayed at home", "ꯑꯩ ꯌꯨꯝꯗ ꯂꯩꯂꯦ꯫"),
    ],
},

# ━━━ 519: Simple Past – Part 2 (Verbs with object) ━━━
519: {
    "heading": "Past tense (with object) examples",
    "rows": [
        ("He ate an apple", "ꯃꯍꯥꯛ ꯁꯦꯝ ꯑꯃ ꯆꯥꯈꯔꯦ꯫"),
        ("She wrote a letter", "ꯃꯍꯥꯛ ꯆꯤꯠꯊꯤ ꯑꯃ ꯏꯈꯔꯦ꯫"),
        ("I saw the film", "ꯑꯩ ꯐꯤꯜꯝ ꯑꯗꯨ ꯌꯦꯡꯈꯔꯦ꯫"),
        ("He drank water", "ꯃꯍꯥꯛ ꯏꯁꯤꯡ ꯊꯛꯈꯔꯦ꯫"),
        ("She bought a dress", "ꯃꯍꯥꯛ ꯐꯤ ꯑꯃ ꯂꯧꯈꯔꯦ꯫"),
        ("They cooked food", "ꯃꯈꯣꯏ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯈꯔꯦ꯫"),
        ("I read a book", "ꯑꯩ ꯂꯥꯏꯔꯤꯛ ꯄꯈꯔꯦ꯫"),
        ("He broke the glass", "ꯃꯍꯥꯛ ꯒ꯭ꯂꯥꯁ ꯑꯗꯨ ꯀꯤꯈꯔꯦ꯫"),
        ("She closed the door", "ꯃꯍꯥꯛ ꯊꯣꯡ ꯑꯗꯨ ꯊꯤꯡꯈꯔꯦ꯫"),
        ("We cleaned the house", "ꯑꯩꯈꯣꯏ ꯌꯨꯝ ꯑꯗꯨ ꯁꯦꯡꯗꯣꯛꯈꯔꯦ꯫"),
        ("They carried the bag", "ꯃꯈꯣꯏ ꯈꯥꯑꯣ ꯑꯗꯨ ꯄꯨꯈꯔꯦ꯫"),
        ("I gave him money", "ꯑꯩꯅ ꯃꯍꯥꯛꯄꯨ ꯄꯥꯏꯁꯥ ꯄꯤꯈꯔꯦ꯫"),
        ("He told a story", "ꯃꯍꯥꯛꯅ ꯋꯥꯔꯤ ꯑꯃ ꯂꯤꯈꯔꯦ꯫"),
        ("She opened the window", "ꯃꯍꯥꯛ ꯇꯛꯅꯩꯕꯥꯛ ꯍꯪꯗꯣꯛꯈꯔꯦ꯫"),
        ("We planted a tree", "ꯑꯩꯈꯣꯏ ꯎꯄꯥꯜ ꯑꯃ ꯂꯧꯈꯔꯦ꯫"),
        ("He wrote well in the exam", "ꯃꯍꯥꯛ ꯄꯔꯤꯈꯥ ꯐꯖꯅ ꯏꯔꯝꯈꯤ꯫"),
        ("I played a game", "ꯑꯩ ꯁꯅꯥ ꯑꯃ ꯁꯥꯈꯔꯦ꯫"),
    ],
},

# ━━━ 520: Simple Past – Part 3 (Past tense of "to be") ━━━
520: {
    "heading": "Past \"to be\" examples",
    "rows": [
        ("I was a student", "ꯑꯩ ꯃꯍꯩꯔꯣꯌ ꯑꯃ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("He was a teacher", "ꯃꯍꯥꯛ ꯑꯣꯖꯥ ꯑꯃ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("She was happy", "ꯃꯍꯥꯛ ꯅꯨꯡꯉꯥꯏꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("It was good", "ꯃꯗꯨ ꯐꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("We were friends", "ꯑꯩꯈꯣꯏ ꯃꯔꯨꯞ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("They were at home", "ꯃꯈꯣꯏ ꯌꯨꯝꯗ ꯂꯩꯔꯝꯃꯤ꯫"),
        ("He was brave", "ꯃꯍꯥꯛ ꯊꯧꯅ ꯐꯔꯝꯃꯤ꯫"),
        ("She was a doctor", "ꯃꯍꯥꯛ ꯗꯣꯛꯇꯔ ꯑꯃ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("The weather was cold", "ꯅꯨꯡꯁꯤꯠꯅꯨꯡꯁ ꯀꯧꯈꯤ꯫"),
        ("I was at school", "ꯑꯩ ꯁ꯭ꯀꯨꯜꯗ ꯂꯩꯔꯝꯃꯤ꯫"),
        ("He was tall", "ꯃꯍꯥꯛ ꯁꯪ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("She was tired", "ꯃꯍꯥꯛ ꯊꯕꯛ ꯋꯥꯈꯔꯝꯃꯤ꯫"),
        ("It was very good", "ꯃꯁꯤ ꯌꯥꯝꯅ ꯐꯔꯦ꯫"),
        ("They were hungry", "ꯃꯈꯣꯏ ꯆꯥꯛ ꯈꯣꯡ ꯂꯥꯛꯂꯦ꯫"),
        ("I was in Imphal", "ꯑꯩ ꯏꯝꯐꯥꯜꯗ ꯂꯩꯔꯝꯃꯤ꯫"),
        ("We were playing", "ꯑꯩꯈꯣꯏ ꯁꯥꯔꯝꯃꯤ꯫"),
        ("He was kind", "ꯃꯍꯥꯛ ꯅꯤꯡꯊꯤꯖ ꯐꯔꯝꯃꯤ꯫"),
    ],
},

# ━━━ 521: Exceptional Verbs that change in past tense ━━━
521: {
    "heading": "Exceptional past tense verb examples",
    "rows": [
        ("I ate (root: cha-)", "ꯑꯩ ꯆꯥꯈꯔꯦ꯫"),
        ("I saw (root: yeng-)", "ꯑꯩ ꯌꯦꯡꯈꯔꯦ꯫"),
        ("I heard (root: ta-)", "ꯑꯩ ꯇꯥꯈꯔꯦ꯫"),
        ("He died (root: shi-)", "ꯃꯍꯥꯛ ꯁꯤꯈꯔꯦ꯫"),
        ("She gave (root: pi-)", "ꯃꯍꯥꯛ ꯄꯤꯈꯔꯦ꯫"),
        ("He got (root: phang-)", "ꯃꯍꯥꯛ ꯐꯪꯈꯔꯦ꯫"),
        ("She took (root: lou-)", "ꯃꯍꯥꯛ ꯂꯧꯈꯔꯦ꯫"),
        ("I threw (root: thak-)", "ꯑꯩ ꯊꯛꯈꯔꯦ꯫"),
        ("He broke (root: ki-)", "ꯃꯍꯥꯛ ꯀꯤꯈꯔꯦ꯫"),
        ("She brought (root: pu-)", "ꯃꯍꯥꯛ ꯄꯨꯈꯔꯦ꯫"),
        ("I caught (root: phang-)", "ꯑꯩ ꯐꯪꯈꯔꯦ꯫"),
        ("He sold (root: yok-)", "ꯃꯍꯥꯛ ꯌꯣꯛꯈꯔꯦ꯫"),
        ("She wore (root: shon-)", "ꯃꯍꯥꯛ ꯁꯣꯟꯈꯔꯦ꯫"),
        ("I woke up (root: hak-)", "ꯑꯩ ꯍꯛꯈꯔꯦ꯫"),
        ("He forgot (root: kap-)", "ꯃꯍꯥꯛ ꯀꯞꯈꯔꯦ꯫"),
        ("They fought (root: phun-)", "ꯃꯈꯣꯏ ꯐꯨꯟꯈꯔꯦ꯫"),
        ("I kept (root: thin-)", "ꯑꯩ ꯊꯤꯟꯈꯔꯦ꯫"),
    ],
},

# ━━━ 522: Past Continuous ━━━
522: {
    "heading": "Past continuous examples",
    "rows": [
        ("I was eating", "ꯑꯩ ꯆꯥꯔꯝꯃꯤ꯫"),
        ("He was going", "ꯃꯍꯥꯛ ꯆꯠꯔꯝꯃꯤ꯫"),
        ("She was sleeping", "ꯃꯍꯥꯛ ꯇꯨꯝꯔꯝꯃꯤ꯫"),
        ("We were playing", "ꯑꯩꯈꯣꯏ ꯁꯥꯔꯝꯃꯤ꯫"),
        ("They were reading", "ꯃꯈꯣꯏ ꯄꯕꯔꯝꯃꯤ꯫"),
        ("You were writing", "ꯅꯪ ꯏꯔꯝꯃꯤ꯫"),
        ("I was cooking food", "ꯑꯩ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯔꯝꯃꯤ꯫"),
        ("He was working yesterday", "ꯃꯍꯥꯛ ꯉꯔꯪ ꯊꯕꯛ ꯇꯧꯔꯝꯃꯤ꯫"),
        ("She was singing", "ꯃꯍꯥꯛ ꯏꯁꯩ ꯁꯀꯔꯝꯃꯤ꯫"),
        ("We were talking", "ꯑꯩꯈꯣꯏ ꯋꯥꯔꯤ ꯁꯥꯅꯔꯝꯃꯤ꯫"),
        ("They were running", "ꯃꯈꯣꯏ ꯆꯦꯜꯔꯝꯃꯤ꯫"),
        ("I was studying at night", "ꯑꯩ ꯅꯨꯡꯊꯤꯜꯗ ꯇꯝꯔꯝꯃꯤ꯫"),
        ("He was driving the car", "ꯃꯍꯥꯛ ꯒꯥꯔꯤ ꯊꯧꯔꯝꯃꯤ꯫"),
        ("She was washing clothes", "ꯃꯍꯥꯛ ꯐꯤ ꯀꯨꯝꯔꯝꯃꯤ꯫"),
        ("We were waiting for the bus", "ꯑꯩꯈꯣꯏ ꯕꯁ ꯉꯥꯏꯔꯝꯃꯤ꯫"),
        ("They were dancing", "ꯃꯈꯣꯏ ꯖꯒꯣꯏ ꯁꯥꯔꯝꯃꯤ꯫"),
        ("I was watching TV", "ꯑꯩ ꯇꯤꯚꯤ ꯌꯦꯡꯔꯝꯃꯤ꯫"),
    ],
},

# ━━━ 523: Present/Past/Future Perfect Tense ━━━
523: {
    "heading": "Perfect tense examples",
    "rows": [
        ("I have eaten", "ꯑꯩ ꯆꯥꯔꯦ꯫"),
        ("He has come", "ꯃꯍꯥꯛ ꯂꯥꯛꯂꯦ꯫"),
        ("She has gone", "ꯃꯍꯥꯛ ꯆꯠꯂꯦ꯫"),
        ("We have finished", "ꯑꯩꯈꯣꯏ ꯂꯣꯏꯁꯤꯜꯂꯦ꯫"),
        ("They have arrived", "ꯃꯈꯣꯏ ꯊꯨꯡꯂꯦ꯫"),
        ("I had eaten before he came", "ꯃꯍꯥꯛ ꯂꯥꯛꯇ꯭ꯔꯤꯉꯩꯗ ꯑꯩ ꯆꯥꯈꯔꯦ꯫"),
        ("He had gone before I arrived", "ꯑꯩ ꯊꯨꯡꯇ꯭ꯔꯤꯉꯩꯗ ꯃꯍꯥꯛ ꯆꯠꯈꯔꯦ꯫"),
        ("She had already slept", "ꯃꯍꯥꯛ ꯍꯧꯖꯤꯛ ꯇꯨꯝꯈꯔꯦ꯫"),
        ("I will have eaten by then", "ꯃꯇꯝ ꯑꯗꯨ ꯐꯥꯑꯣꯒꯅꯤ ꯑꯩ ꯆꯥꯈꯔꯒꯅꯤ꯫"),
        ("He will have finished", "ꯃꯍꯥꯛ ꯂꯣꯏꯁꯤꯜꯈꯔꯒꯅꯤ꯫"),
        ("She has read the book", "ꯃꯍꯥꯛ ꯂꯥꯏꯔꯤꯛ ꯑꯗꯨ ꯄꯈꯔꯦ꯫"),
        ("We have seen the movie", "ꯑꯩꯈꯣꯏ ꯐꯤꯜꯝ ꯑꯗꯨ ꯌꯦꯡꯈꯔꯦ꯫"),
        ("He has eaten rice", "ꯃꯍꯥꯛ ꯆꯥꯛ ꯆꯥꯈꯔꯦ꯫"),
        ("They have already left", "ꯃꯈꯣꯏ ꯍꯧꯖꯤꯛ ꯆꯠꯈꯔꯦ꯫"),
        ("I had written the letter", "ꯑꯩ ꯆꯤꯠꯊꯤ ꯑꯗꯨ ꯏꯈꯔꯦ꯫"),
        ("She will have come by evening", "ꯅꯨꯃꯤꯗꯪ ꯐꯥꯑꯣꯒꯅꯤ ꯃꯍꯥꯛ ꯂꯥꯛꯈꯔꯒꯅꯤ꯫"),
        ("He has done the work", "ꯃꯍꯥꯛ ꯊꯕꯛ ꯑꯗꯨ ꯇꯧꯈꯔꯦ꯫"),
    ],
},

# ━━━ 524: Learn Prepositions ━━━
524: {
    "heading": "Preposition examples",
    "rows": [
        ("I am at home", "ꯑꯩ ꯌꯨꯝꯗ ꯂꯩꯏ꯫"),
        ("He is in school", "ꯃꯍꯥꯛ ꯁ꯭ꯀꯨꯜꯗ ꯂꯩꯏ꯫"),
        ("She is from Imphal", "ꯃꯍꯥꯛ ꯏꯝꯐꯥꯜ ꯗꯒꯤꯅꯤ꯫"),
        ("The book is on the table", "ꯂꯥꯏꯔꯤꯛ ꯑꯗꯨ ꯇꯦꯕꯜ ꯃꯊꯛꯇ ꯂꯩꯏ꯫"),
        ("Come with me", "ꯑꯩꯒ ꯂꯥꯛꯂꯣ꯫"),
        ("Go to the market", "ꯀꯩꯊꯦꯜꯗ ꯆꯠꯂꯣ꯫"),
        ("Water is in the glass", "ꯏꯁꯤꯡ ꯒ꯭ꯂꯥꯁꯇ ꯂꯩꯏ꯫"),
        ("He came from Delhi", "ꯃꯍꯥꯛ ꯗꯦꯜꯍꯤ ꯗꯒꯤ ꯂꯥꯛꯂꯦ꯫"),
        ("Give the pen to me", "ꯑꯩꯗ ꯀꯂꯝ ꯑꯗꯨ ꯄꯤꯌꯨ꯫"),
        ("I went with my friend", "ꯑꯩ ꯑꯩꯒꯤ ꯃꯔꯨꯞꯒ ꯆꯠꯂꯦ꯫"),
        ("She sat on the chair", "ꯃꯍꯥꯛ ꯆꯦꯌꯔꯗ ꯐꯝꯂꯦ꯫"),
        ("The cat is under the table", "ꯍꯧꯗꯣꯡ ꯇꯦꯕꯜ ꯃꯈꯥꯗ ꯂꯩꯏ꯫"),
        ("I came from the office", "ꯑꯩ ꯑꯣꯐꯤꯁ ꯗꯒꯤ ꯂꯥꯛꯂꯦ꯫"),
        ("He lives near the river", "ꯃꯍꯥꯛ ꯇꯨꯔꯦꯜ ꯅꯛꯇ ꯂꯩꯏ꯫"),
        ("Put it inside the bag", "ꯈꯥꯑꯣ ꯃꯅꯨꯡꯗ ꯊꯤꯟꯕꯤꯌꯨ꯫"),
        ("She walked behind him", "ꯃꯍꯥꯛ ꯃꯍꯥꯛꯀꯤ ꯃꯅꯨꯡꯗ ꯆꯠꯂꯦ꯫"),
        ("The bird is on the tree", "ꯎꯆꯦꯛ ꯎꯄꯥꯜ ꯃꯊꯛꯇ ꯂꯩꯏ꯫"),
    ],
},

# ━━━ 525: Preposition "TO" ━━━
525: {
    "heading": "\"TO\" preposition examples",
    "rows": [
        ("I go to school", "ꯑꯩ ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯂꯤ꯫"),
        ("He went to the market", "ꯃꯍꯥꯛ ꯀꯩꯊꯦꯜꯗ ꯆꯠꯂꯦ꯫"),
        ("She came to my house", "ꯃꯍꯥꯛ ꯑꯩꯒꯤ ꯌꯨꯝꯗ ꯂꯥꯛꯂꯦ꯫"),
        ("We went to the temple", "ꯑꯩꯈꯣꯏ ꯂꯥꯏꯔꯦꯝꯕꯤꯗ ꯆꯠꯂꯦ꯫"),
        ("They went to the mosque", "ꯃꯈꯣꯏ ꯃꯣꯁ꯭ꯀꯗ ꯆꯠꯂꯨꯏ꯫"),
        ("Give this to him", "ꯃꯍꯥꯛꯗ ꯃꯁꯤ ꯄꯤꯌꯨ꯫"),
        ("I gave money to the shopkeeper", "ꯑꯩꯅ ꯗꯨꯀꯥꯟꯗꯥꯔꯗ ꯄꯥꯏꯁꯥ ꯄꯤꯈꯔꯦ꯫"),
        ("Come to my office", "ꯑꯩꯒꯤ ꯑꯣꯐꯤꯁꯇ ꯂꯥꯛꯂꯣ꯫"),
        ("He walked to the river", "ꯃꯍꯥꯛ ꯇꯨꯔꯦꯜꯗ ꯆꯠꯂꯦ꯫"),
        ("She went to the hospital", "ꯃꯍꯥꯛ ꯍꯣꯁ꯭ꯄꯤꯇꯜꯗ ꯆꯠꯂꯦ꯫"),
        ("I want to go to Manipur", "ꯑꯩ ꯃꯅꯤꯄꯨꯔꯗ ꯆꯠꯅꯤꯡꯉꯩ꯫"),
        ("Listen to the teacher", "ꯑꯣꯖꯥꯗ ꯇꯕꯤꯌꯨ꯫"),
        ("Go to the airport", "ꯑꯦꯌꯔꯄꯣꯔꯇꯇ ꯆꯠꯂꯣ꯫"),
        ("She told this to me", "ꯃꯍꯥꯛꯅ ꯑꯩꯗ ꯃꯁꯤ ꯍꯥꯏꯈꯔꯦ꯫"),
        ("We go to school every day", "ꯑꯩꯈꯣꯏ ꯅꯨꯃꯤꯠ ꯈꯨꯗꯤꯡꯃꯛ ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯂꯤ꯫"),
        ("How do I go to the airport?", "ꯑꯦꯌꯔꯄꯣꯔꯇꯇ ꯀꯔꯝꯅ ꯆꯠꯀꯅꯤ?"),
        ("I want to go to university", "ꯑꯩ ꯌꯨꯅꯤꯚꯔꯁꯤꯇꯤꯗ ꯆꯠꯅꯤꯡꯉꯩ꯫"),
    ],
},

# ━━━ 526: Person/living thing as object ━━━
526: {
    "heading": "Person as object (-bu) examples",
    "rows": [
        ("I love you", "ꯑꯩꯅ ꯅꯪꯕꯨ ꯅꯨꯡꯁꯤ꯫"),
        ("He called her", "ꯃꯍꯥꯛꯅ ꯃꯍꯥꯛꯄꯨ ꯀꯧꯈꯔꯦ꯫"),
        ("She saw him", "ꯃꯍꯥꯛꯅ ꯃꯍꯥꯛꯄꯨ ꯎꯈꯔꯦ꯫"),
        ("I told him", "ꯑꯩꯅ ꯃꯍꯥꯛꯄꯨ ꯍꯥꯏꯈꯔꯦ꯫"),
        ("He gave her a gift", "ꯃꯍꯥꯛꯅ ꯃꯍꯥꯛꯄꯨ ꯀꯥꯅꯥꯃꯛ ꯄꯤꯈꯔꯦ꯫"),
        ("I am waiting for you", "ꯑꯩ ꯅꯪꯕꯨ ꯉꯥꯏꯔꯤ꯫"),
        ("She helped the children", "ꯃꯍꯥꯛꯅ ꯑꯅꯧꯕꯁꯤꯡꯕꯨ ꯃꯇꯦꯡ ꯄꯥꯡꯈꯔꯦ꯫"),
        ("He hit the boy", "ꯃꯍꯥꯛꯅ ꯅꯨꯄꯃꯆꯥꯕꯨ ꯁꯥꯈꯔꯦ꯫"),
        ("I sent the teacher", "ꯑꯩꯅ ꯑꯣꯖꯥꯕꯨ ꯊꯥꯈꯔꯦ꯫"),
        ("She taught the students", "ꯃꯍꯥꯛꯅ ꯃꯍꯩꯔꯣꯌꯁꯤꯡꯕꯨ ꯇꯝꯍꯟꯈꯔꯦ꯫"),
        ("He brought the child", "ꯃꯍꯥꯛꯅ ꯑꯅꯧꯕ ꯑꯗꯨꯕꯨ ꯄꯨꯈꯔꯦ꯫"),
        ("I asked my friend", "ꯑꯩꯅ ꯑꯩꯒꯤ ꯃꯔꯨꯞꯕꯨ ꯍꯪꯈꯔꯦ꯫"),
        ("She took the dog", "ꯃꯍꯥꯛꯅ ꯍꯨꯏꯕꯨ ꯄꯨꯈꯔꯦ꯫"),
        ("He met the doctor", "ꯃꯍꯥꯛꯅ ꯗꯣꯛꯇꯔꯕꯨ ꯎꯈꯔꯦ꯫"),
        ("We invited the guests", "ꯑꯩꯈꯣꯏꯅ ꯈꯣꯉꯖꯤꯜꯁꯤꯡꯕꯨ ꯀꯧꯈꯔꯦ꯫"),
        ("Whom should I contact?", "ꯀꯅꯕꯨ ꯀꯣꯟꯇꯦꯛ ꯇꯧꯗꯣꯅꯣ?"),
        ("I respect my parents", "ꯑꯩꯅ ꯑꯩꯒꯤ ꯏꯄꯨꯏꯃꯕꯨ ꯏꯀꯥꯏꯈꯨꯝꯅꯏ꯫"),
    ],
},

# ━━━ 527: Saying My/His/Her ━━━
527: {
    "heading": "Possessive pronoun examples",
    "rows": [
        ("My name", "ꯑꯩꯒꯤ ꯃꯤꯡ"),
        ("Your name", "ꯅꯪꯒꯤ ꯃꯤꯡ"),
        ("His/Her name", "ꯃꯍꯥꯛꯀꯤ ꯃꯤꯡ"),
        ("Our house", "ꯑꯩꯈꯣꯏꯒꯤ ꯌꯨꯝ"),
        ("Their school", "ꯃꯈꯣꯏꯒꯤ ꯁ꯭ꯀꯨꯜ"),
        ("My book is here", "ꯑꯩꯒꯤ ꯂꯥꯏꯔꯤꯛ ꯑꯁꯤꯗ ꯂꯩꯏ꯫"),
        ("His father is a teacher", "ꯃꯍꯥꯛꯀꯤ ꯏꯄꯥ ꯑꯣꯖꯥ ꯑꯃꯅꯤ꯫"),
        ("Her dress is new", "ꯃꯍꯥꯛꯀꯤ ꯐꯤ ꯑꯅꯧꯕꯅꯤ꯫"),
        ("Your pen is on the table", "ꯅꯪꯒꯤ ꯀꯂꯝ ꯇꯦꯕꯜꯗ ꯂꯩꯏ꯫"),
        ("My mother cooks well", "ꯑꯩꯒꯤ ꯏꯃꯥ ꯐꯖꯅ ꯁꯥꯏ꯫"),
        ("His house is big", "ꯃꯍꯥꯛꯀꯤ ꯌꯨꯝ ꯑꯆꯧꯕꯅꯤ꯫"),
        ("Her sister came yesterday", "ꯃꯍꯥꯛꯀꯤ ꯏꯆꯦ ꯉꯔꯪ ꯂꯥꯛꯂꯦ꯫"),
        ("Our language is Meiteilon", "ꯑꯩꯈꯣꯏꯒꯤ ꯂꯣꯟ ꯃꯩꯇꯩꯂꯣꯟꯅꯤ꯫"),
        ("Their children study well", "ꯃꯈꯣꯏꯒꯤ ꯑꯅꯧꯕꯁꯤꯡ ꯐꯖꯅ ꯇꯝꯏ꯫"),
        ("My friend is kind", "ꯑꯩꯒꯤ ꯃꯔꯨꯞ ꯅꯤꯡꯊꯤꯖꯅꯤ꯫"),
        ("Your favourite colour?", "ꯅꯍꯥꯛꯀꯤ ꯑꯄꯝꯕ ꯃꯆꯨ ꯀꯔꯤꯅꯣ?"),
        ("His bag is heavy", "ꯃꯍꯥꯛꯀꯤ ꯈꯥꯑꯣ ꯑꯊꯣꯌꯕꯅꯤ꯫"),
    ],
},

# ━━━ 528: WH Questions ━━━
528: {
    "heading": "WH question examples",
    "rows": [
        ("What is your name?", "ꯅꯪꯒꯤ ꯃꯤꯡ ꯀꯔꯤ ꯀꯧꯋꯤ?"),
        ("What did you do?", "ꯅꯪꯅ ꯀꯔꯤ ꯇꯧꯔꯤꯕ?"),
        ("What should I do?", "ꯑꯩ ꯀꯔꯤ ꯇꯧ ꯍꯥꯏꯔꯤꯅꯣ?"),
        ("Why did you come?", "ꯅꯍꯥꯛ ꯀꯔꯤꯒꯤ ꯂꯥꯛꯂꯤꯕꯅꯣ?"),
        ("Why did you sleep?", "ꯅꯍꯥꯛ ꯀꯔꯤꯒꯤ ꯇꯨꯝꯂꯤꯕꯅꯣ?"),
        ("Where did you come from?", "ꯅꯍꯛ ꯀꯗꯥꯏꯗꯒꯤꯅꯣ?"),
        ("Where is the manager's cabin?", "ꯃꯦꯅꯦꯖꯔꯒꯤ ꯀꯦꯕꯤꯟ ꯀꯗꯣꯝꯗꯅꯣ?"),
        ("Where should I go?", "ꯀꯗꯣꯝꯗ ꯆꯠꯀꯗꯣꯏꯅꯣ?"),
        ("How did you come?", "ꯅꯍꯥꯛ ꯀꯔꯝꯅ ꯂꯥꯛꯄꯅꯣ?"),
        ("How are you?", "ꯅꯍꯥꯛ ꯀꯝꯗꯧꯔꯤꯒꯦ?"),
        ("How much is this?", "ꯃꯁꯤ ꯀꯌ ꯄꯤꯕꯒꯦ?"),
        ("How many apples?", "ꯁꯦꯝ ꯀꯌ ꯂꯩꯒꯦ?"),
        ("Which is your favourite colour?", "ꯅꯍꯥꯛꯀꯤ ꯑꯄꯝꯕ ꯃꯆꯨ ꯀꯔꯤꯅꯣ?"),
        ("Which room did you sleep in?", "ꯀꯔꯝꯕ ꯀꯗ ꯇꯨꯝꯒꯦ?"),
        ("Who is he?", "ꯃꯍꯥꯛ ꯀꯅꯅꯣ?"),
        ("Whom should I contact?", "ꯀꯅꯕꯨ ꯀꯣꯟꯇꯦꯛ ꯇꯧꯗꯣꯅꯣ?"),
        ("When will you come?", "ꯅꯪ ꯀꯗꯥꯏꯗ ꯂꯥꯛꯀꯅꯤ?"),
    ],
},

# ━━━ 529: Negative – Present ━━━
529: {
    "heading": "Negative present tense examples",
    "rows": [
        ("I don't eat meat", "ꯑꯩ ꯁꯥ ꯆꯥꯗꯦ꯫"),
        ("He doesn't go to school", "ꯃꯍꯥꯛ ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯗꯦ꯫"),
        ("She doesn't read", "ꯃꯍꯥꯛ ꯄꯗꯦ꯫"),
        ("We don't play today", "ꯑꯩꯈꯣꯏ ꯉꯁꯤ ꯁꯥꯗꯦ꯫"),
        ("They don't come here", "ꯃꯈꯣꯏ ꯑꯁꯤꯗ ꯂꯥꯛꯇꯦ꯫"),
        ("I don't understand", "ꯑꯩ ꯈꯪꯗꯦ꯫"),
        ("He doesn't speak Meitei", "ꯃꯍꯥꯛ ꯃꯩꯇꯩꯂꯣꯟ ꯉꯥꯡꯗꯦ꯫"),
        ("She doesn't like tea", "ꯃꯍꯥꯛ ꯆꯥ ꯄꯝꯗꯦ꯫"),
        ("We don't want that", "ꯑꯩꯈꯣꯏ ꯃꯗꯨ ꯄꯝꯗꯦ꯫"),
        ("I don't know", "ꯑꯩ ꯈꯪꯗꯦ꯫"),
        ("He doesn't work here", "ꯃꯍꯥꯛ ꯑꯁꯤꯗ ꯊꯕꯛ ꯇꯧꯗꯦ꯫"),
        ("She is not at home", "ꯃꯍꯥꯛ ꯌꯨꯝꯗ ꯂꯩꯇꯦ꯫"),
        ("I don't love him", "ꯑꯩ ꯃꯍꯥꯛꯄꯨ ꯅꯨꯡꯁꯤꯗꯦ꯫"),
        ("This is not correct", "ꯃꯁꯤ ꯑꯆꯨꯝꯕ ꯅꯠꯇꯦ꯫"),
        ("He is not a teacher", "ꯃꯍꯥꯛ ꯑꯣꯖꯥ ꯅꯠꯇꯦ꯫"),
        ("I don't drive", "ꯑꯩ ꯒꯥꯔꯤ ꯊꯧꯗꯦ꯫"),
        ("They don't listen", "ꯃꯈꯣꯏ ꯇꯗꯦ꯫"),
    ],
},

# ━━━ 530: Negative – Past ━━━
530: {
    "heading": "Negative past tense examples",
    "rows": [
        ("I didn't eat", "ꯑꯩ ꯆꯥꯈꯔꯗꯦ꯫"),
        ("He didn't come", "ꯃꯍꯥꯛ ꯂꯥꯛꯈꯔꯗꯦ꯫"),
        ("She didn't go", "ꯃꯍꯥꯛ ꯆꯠꯈꯔꯗꯦ꯫"),
        ("We didn't play", "ꯑꯩꯈꯣꯏ ꯁꯥꯈꯔꯗꯦ꯫"),
        ("They didn't come yesterday", "ꯃꯈꯣꯏ ꯉꯔꯪ ꯂꯥꯛꯈꯔꯗꯦ꯫"),
        ("I didn't sleep well", "ꯑꯩ ꯐꯖꯅ ꯇꯨꯝꯈꯔꯗꯦ꯫"),
        ("He didn't write the letter", "ꯃꯍꯥꯛ ꯆꯤꯠꯊꯤ ꯏꯈꯔꯗꯦ꯫"),
        ("She didn't read the book", "ꯃꯍꯥꯛ ꯂꯥꯏꯔꯤꯛ ꯄꯈꯔꯗꯦ꯫"),
        ("We didn't see the film", "ꯑꯩꯈꯣꯏ ꯐꯤꯜꯝ ꯌꯦꯡꯈꯔꯗꯦ꯫"),
        ("I didn't tell him", "ꯑꯩꯅ ꯃꯍꯥꯛꯄꯨ ꯍꯥꯏꯈꯔꯗꯦ꯫"),
        ("He didn't bring the bag", "ꯃꯍꯥꯛꯅ ꯈꯥꯑꯣ ꯄꯨꯈꯔꯗꯦ꯫"),
        ("She didn't pay the money", "ꯃꯍꯥꯛꯅ ꯄꯥꯏꯁꯥ ꯄꯤꯈꯔꯗꯦ꯫"),
        ("They didn't sit there", "ꯃꯈꯣꯏ ꯑꯗꯨꯗ ꯐꯝꯈꯔꯗꯦ꯫"),
        ("I didn't know the answer", "ꯑꯩ ꯄꯥꯑꯣꯈꯨꯝ ꯈꯪꯈꯔꯗꯦ꯫"),
        ("He didn't call me", "ꯃꯍꯥꯛꯅ ꯑꯩꯕꯨ ꯀꯧꯈꯔꯗꯦ꯫"),
        ("We didn't finish the work", "ꯑꯩꯈꯣꯏ ꯊꯕꯛ ꯂꯣꯏꯁꯤꯜꯈꯔꯗꯦ꯫"),
        ("She didn't cook today", "ꯃꯍꯥꯛ ꯉꯁꯤ ꯁꯥꯈꯔꯗꯦ꯫"),
    ],
},

# ━━━ 531: Negative – Future ━━━
531: {
    "heading": "Negative future tense examples",
    "rows": [
        ("I will not eat", "ꯑꯩ ꯆꯥꯔꯣꯏ꯫"),
        ("He will not come", "ꯃꯍꯥꯛ ꯂꯥꯛꯔꯣꯏ꯫"),
        ("She will not go", "ꯃꯍꯥꯛ ꯆꯠꯔꯣꯏ꯫"),
        ("We will not play", "ꯑꯩꯈꯣꯏ ꯁꯥꯔꯣꯏ꯫"),
        ("They will not come tomorrow", "ꯃꯈꯣꯏ ꯍꯌꯦꯡ ꯂꯥꯛꯔꯣꯏ꯫"),
        ("I will not drink tea", "ꯑꯩ ꯆꯥ ꯊꯛꯔꯣꯏ꯫"),
        ("He will not write the exam", "ꯃꯍꯥꯛ ꯄꯔꯤꯈꯥ ꯏꯔꯣꯏ꯫"),
        ("She will not cook dinner", "ꯃꯍꯥꯛ ꯅꯨꯃꯤꯗꯪ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯔꯣꯏ꯫"),
        ("We will not forget you", "ꯑꯩꯈꯣꯏ ꯅꯪꯕꯨ ꯀꯞꯔꯣꯏ꯫"),
        ("I will not sleep late", "ꯑꯩ ꯊꯦꯡꯅ ꯇꯨꯝꯔꯣꯏ꯫"),
        ("He will not sell the house", "ꯃꯍꯥꯛ ꯌꯨꯝ ꯌꯣꯛꯔꯣꯏ꯫"),
        ("She will not tell anyone", "ꯃꯍꯥꯛ ꯀꯅꯃꯛꯄꯨ ꯍꯥꯏꯔꯣꯏ꯫"),
        ("They will not wait", "ꯃꯈꯣꯏ ꯉꯥꯏꯔꯣꯏ꯫"),
        ("I will not buy this", "ꯑꯩ ꯃꯁꯤ ꯂꯩꯔꯣꯏ꯫"),
        ("He will not drive today", "ꯃꯍꯥꯛ ꯉꯁꯤ ꯒꯥꯔꯤ ꯊꯧꯔꯣꯏ꯫"),
        ("We will not go without you", "ꯑꯩꯈꯣꯏ ꯅꯪ ꯅꯠꯇꯅ ꯆꯠꯔꯣꯏ꯫"),
        ("She will not accept this", "ꯃꯍꯥꯛ ꯃꯁꯤ ꯂꯧꯔꯣꯏ꯫"),
    ],
},

# ━━━ 532: Gender & Plurals ━━━
532: {
    "heading": "Gender and plural examples",
    "rows": [
        ("Man (male)", "ꯅꯨꯄ"),
        ("Woman (female)", "ꯅꯨꯄꯤ"),
        ("Boy", "ꯅꯨꯄꯃꯆꯥ"),
        ("Girl", "ꯅꯨꯄꯤ ꯃꯆꯥ"),
        ("Children (plural -sing)", "ꯑꯅꯧꯕꯁꯤꯡ"),
        ("Boys (plural)", "ꯅꯨꯄꯃꯆꯥꯁꯤꯡ"),
        ("Girls (plural)", "ꯅꯨꯄꯤ ꯃꯆꯥꯁꯤꯡ"),
        ("Teachers (plural)", "ꯑꯣꯖꯥꯁꯤꯡ"),
        ("The boys are playing", "ꯅꯨꯄꯃꯆꯥꯁꯤꯡ ꯁꯥꯔꯝꯃꯤ꯫"),
        ("The girls are studying", "ꯅꯨꯄꯤ ꯃꯆꯥꯁꯤꯡ ꯇꯝꯔꯝꯃꯤ꯫"),
        ("The children came", "ꯑꯅꯧꯕꯁꯤꯡ ꯂꯥꯛꯂꯦ꯫"),
        ("Elder brother", "ꯏꯌꯝꯕ"),
        ("Elder sister", "ꯏꯆꯦ"),
        ("Younger brother", "ꯏꯅꯥꯑꯣꯄ"),
        ("Younger sister", "ꯏꯅꯥꯑꯣꯅꯨꯄꯤ"),
        ("Father and mother", "ꯏꯄꯥ ꯑꯃꯁꯨꯡ ꯏꯃꯥ"),
        ("The teachers are kind", "ꯑꯣꯖꯥꯁꯤꯡ ꯅꯤꯡꯊꯤꯖꯅꯤ꯫"),
    ],
},

# ━━━ 533: Nouns with Prepositions ━━━
533: {
    "heading": "Nouns with preposition examples",
    "rows": [
        ("In the house", "ꯌꯨꯝꯗ"),
        ("At school", "ꯁ꯭ꯀꯨꯜꯗ"),
        ("From Imphal", "ꯏꯝꯐꯥꯜ ꯗꯒꯤ"),
        ("Of the teacher", "ꯑꯣꯖꯥꯒꯤ"),
        ("With my friend", "ꯑꯩꯒꯤ ꯃꯔꯨꯞꯒ"),
        ("The book on the table", "ꯇꯦꯕꯜ ꯃꯊꯛꯇ ꯂꯥꯏꯔꯤꯛ"),
        ("I came from the market", "ꯑꯩ ꯀꯩꯊꯦꯜ ꯗꯒꯤ ꯂꯥꯛꯂꯦ꯫"),
        ("He is at the office", "ꯃꯍꯥꯛ ꯑꯣꯐꯤꯁꯗ ꯂꯩꯏ꯫"),
        ("She went with her sister", "ꯃꯍꯥꯛ ꯃꯍꯥꯛꯀꯤ ꯏꯆꯦꯒ ꯆꯠꯂꯦ꯫"),
        ("The children of the school", "ꯁ꯭ꯀꯨꯜꯒꯤ ꯑꯅꯧꯕꯁꯤꯡ"),
        ("Water in the river", "ꯇꯨꯔꯦꯜꯗ ꯏꯁꯤꯡ"),
        ("Food on the plate", "ꯊꯥꯜꯗ ꯆꯤꯟꯖꯥꯛ"),
        ("The flower in the garden", "ꯃꯐꯝꯗ ꯂꯩ"),
        ("He is from Ukhrul", "ꯃꯍꯥꯛ ꯎꯈꯔꯨꯜ ꯗꯒꯤꯅꯤ꯫"),
        ("I walked with my brother", "ꯑꯩ ꯑꯩꯒꯤ ꯏꯌꯝꯕꯒ ꯆꯠꯂꯦ꯫"),
        ("The pen of the student", "ꯃꯍꯩꯔꯣꯌꯒꯤ ꯀꯂꯝ"),
        ("She sat on the floor", "ꯃꯍꯥꯛ ꯂꯃꯗ ꯐꯝꯂꯦ꯫"),
    ],
},

# ━━━ 534: Similar prepositions ━━━
534: {
    "heading": "Similar preposition examples",
    "rows": [
        ("In the house (-da)", "ꯌꯨꯝꯗ"),
        ("At school (-ta)", "ꯁ꯭ꯀꯨꯜꯇ"),
        ("-da and -ta both mean 'in/at'", "'-ꯗ' ꯑꯃꯁꯨꯡ '-ꯇ' ꯑꯅꯤꯃꯛ 'ꯗ' ꯍꯥꯏꯕꯅꯤ"),
        ("Of the teacher (-gi)", "ꯑꯣꯖꯥꯒꯤ"),
        ("Of the book (-ki)", "ꯂꯥꯏꯔꯤꯛꯀꯤ"),
        ("-gi and -ki both mean 'of'", "'-ꯒꯤ' ꯑꯃꯁꯨꯡ '-ꯀꯤ' ꯑꯅꯤꯃꯛ 'ꯒꯤ' ꯍꯥꯏꯕꯅꯤ"),
        ("From Imphal (-dagi)", "ꯏꯝꯐꯥꯜ ꯗꯒꯤ"),
        ("From here (-dagi)", "ꯑꯁꯤ ꯗꯒꯤ"),
        ("He is in the room (-da)", "ꯃꯍꯥꯛ ꯔꯨꯝꯗ ꯂꯩꯏ꯫"),
        ("She is at the temple (-ta)", "ꯃꯍꯥꯛ ꯂꯥꯏꯔꯦꯝꯕꯤꯇ ꯂꯩꯏ꯫"),
        ("My friend's house (-gi)", "ꯑꯩꯒꯤ ꯃꯔꯨꯞꯒꯤ ꯌꯨꯝ"),
        ("This book's page (-ki)", "ꯂꯥꯏꯔꯤꯛ ꯑꯁꯤꯒꯤ ꯃꯐꯝ"),
        ("I came from home (-dagi)", "ꯑꯩ ꯌꯨꯝ ꯗꯒꯤ ꯂꯥꯛꯂꯦ꯫"),
        ("He came from the river", "ꯃꯍꯥꯛ ꯇꯨꯔꯦꯜ ꯗꯒꯤ ꯂꯥꯛꯂꯦ꯫"),
        ("With my mother (-ga)", "ꯑꯩꯒꯤ ꯏꯃꯥꯒ"),
        ("By car (-na)", "ꯒꯥꯔꯤꯅ"),
        ("I went by bus (-na)", "ꯑꯩ ꯕꯁꯅ ꯆꯠꯂꯦ꯫"),
    ],
},

# ━━━ 535: Cases ━━━
535: {
    "heading": "Case marker examples",
    "rows": [
        ("Nominative: He goes", "ꯃꯍꯥꯛ ꯆꯠꯂꯤ꯫"),
        ("Accusative: I see him (-bu)", "ꯑꯩꯅ ꯃꯍꯥꯛꯄꯨ ꯎꯏ꯫"),
        ("Genitive: My book (-gi)", "ꯑꯩꯒꯤ ꯂꯥꯏꯔꯤꯛ"),
        ("Dative: Give to me (-da)", "ꯑꯩꯗ ꯄꯤꯌꯨ꯫"),
        ("Ablative: From Imphal (-dagi)", "ꯏꯝꯐꯥꯜ ꯗꯒꯤ"),
        ("Instrumental: By car (-na)", "ꯒꯥꯔꯤꯅ"),
        ("Comitative: With friend (-ga)", "ꯃꯔꯨꯞꯒ"),
        ("Locative: In the house (-da)", "ꯌꯨꯝꯗ"),
        ("I gave the book to him", "ꯑꯩꯅ ꯃꯍꯥꯛꯗ ꯂꯥꯏꯔꯤꯛ ꯄꯤꯈꯔꯦ꯫"),
        ("He hit him with a stick (-na)", "ꯃꯍꯥꯛꯅ ꯃꯍꯥꯛꯄꯨ ꯎꯆꯦꯛꯅ ꯁꯥꯈꯔꯦ꯫"),
        ("She came from Delhi", "ꯃꯍꯥꯛ ꯗꯦꯜꯍꯤ ꯗꯒꯤ ꯂꯥꯛꯂꯦ꯫"),
        ("The teacher's book (-ki)", "ꯑꯣꯖꯥꯒꯤ ꯂꯥꯏꯔꯤꯛ"),
        ("I went with my mother (-ga)", "ꯑꯩ ꯑꯩꯒꯤ ꯏꯃꯥꯒ ꯆꯠꯂꯦ꯫"),
        ("He lives in Manipur (-da)", "ꯃꯍꯥꯛ ꯃꯅꯤꯄꯨꯔꯗ ꯂꯩꯏ꯫"),
        ("She called the boy (-bu)", "ꯃꯍꯥꯛꯅ ꯅꯨꯄꯃꯆꯥꯕꯨ ꯀꯧꯈꯔꯦ꯫"),
        ("By the boys of the school", "ꯁ꯭ꯀꯨꯜꯒꯤ ꯅꯨꯄꯃꯆꯥꯁꯤꯡꯅ"),
        ("The children are at home (-da)", "ꯑꯅꯧꯕꯁꯤꯡ ꯌꯨꯝꯗ ꯂꯩꯏ꯫"),
    ],
},

# ━━━ 536: Commands / Imperative ━━━
536: {
    "heading": "Command and imperative examples",
    "rows": [
        ("Come!", "ꯂꯥꯀꯎ!"),
        ("Go!", "ꯆꯠꯂꯣ!"),
        ("Sit down!", "ꯐꯝꯃꯨ!"),
        ("Eat!", "ꯆꯥꯔꯣ!"),
        ("Drink water!", "ꯏꯁꯤꯡ ꯊꯛꯂꯣ!"),
        ("Read the book!", "ꯂꯥꯏꯔꯤꯛ ꯄꯕꯤꯌꯨ!"),
        ("Write your name!", "ꯅꯪꯒꯤ ꯃꯤꯡ ꯏꯌꯨ!"),
        ("Open the door!", "ꯊꯣꯡ ꯍꯪꯗꯣꯛꯂꯣ!"),
        ("Close the window!", "ꯇꯛꯅꯩꯕꯥꯛ ꯊꯤꯡꯕꯤꯌꯨ!"),
        ("Run fast!", "ꯊꯨꯅ ꯆꯦꯜꯂꯣ!"),
        ("Go straight ahead!", "ꯆꯨꯝꯗ꯭ꯔꯤꯡ ꯆꯠꯂꯣ!"),
        ("Turn left!", "ꯑꯣꯏꯗ ꯆꯠꯂꯣ!"),
        ("Turn right!", "ꯌꯦꯠꯇ ꯆꯠꯂꯣ!"),
        ("Please come in", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯂꯥꯀꯄꯤꯌꯨ꯫"),
        ("Don't go!", "ꯆꯠꯂꯣꯌꯨ!"),
        ("Please wait for me", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯑꯩꯕꯨ ꯉꯥꯏꯕꯤꯌꯨ꯫"),
        ("Take care!", "ꯐꯖꯅ ꯂꯩꯌꯨ!"),
    ],
},

# ━━━ 537: Time related words ━━━
537: {
    "heading": "Time-related word examples",
    "rows": [
        ("Today", "ꯉꯁꯤ"),
        ("Yesterday", "ꯉꯔꯪ"),
        ("Tomorrow", "ꯍꯌꯦꯡ"),
        ("Morning", "ꯅꯨꯃꯤꯠ ꯊꯣꯛꯇ꯭ꯔꯤꯉꯩꯗ"),
        ("Evening", "ꯅꯨꯃꯤꯗꯪ"),
        ("Night", "ꯅꯨꯡꯊꯤꯜ"),
        ("Now", "ꯍꯧꯖꯤꯛ"),
        ("Later", "ꯃꯇꯨꯡꯗ"),
        ("Always", "ꯃꯇꯝ ꯄꯨꯝꯕꯗ"),
        ("I came yesterday", "ꯑꯩ ꯉꯔꯪ ꯂꯥꯛꯂꯦ꯫"),
        ("He will come tomorrow", "ꯃꯍꯥꯛ ꯍꯌꯦꯡ ꯂꯥꯛꯀꯅꯤ꯫"),
        ("She is here now", "ꯃꯍꯥꯛ ꯍꯧꯖꯤꯛ ꯑꯁꯤꯗ ꯂꯩꯏ꯫"),
        ("I will meet you in the evening", "ꯑꯩ ꯅꯨꯃꯤꯗꯪ ꯅꯪꯕꯨ ꯎꯅꯅꯁꯤ꯫"),
        ("We study every day", "ꯑꯩꯈꯣꯏ ꯅꯨꯃꯤꯠ ꯈꯨꯗꯤꯡꯃꯛ ꯇꯝꯏ꯫"),
        ("He slept last night", "ꯃꯍꯥꯛ ꯉꯔꯪ ꯅꯨꯡꯊꯤꯜꯗ ꯇꯨꯝꯂꯦ꯫"),
        ("Come tomorrow morning", "ꯍꯌꯦꯡ ꯅꯨꯃꯤꯠ ꯊꯣꯛꯇ ꯂꯥꯛꯂꯣ꯫"),
        ("What time is it?", "ꯀꯔꯤꯒꯤ ꯇꯥꯏꯝ ꯑꯣꯏꯔꯤꯕꯒꯦ?"),
    ],
},

# ━━━ 538: Causative Verbs ━━━
538: {
    "heading": "Causative verb examples",
    "rows": [
        ("I eat → I make (him) eat", "ꯑꯩ ꯆꯥꯏ → ꯑꯩ ꯆꯥꯍꯜꯂꯤ"),
        ("He reads → I make him read", "ꯃꯍꯥꯛ ꯄꯏ → ꯑꯩ ꯃꯍꯥꯛꯄꯨ ꯄꯍꯜꯂꯤ"),
        ("She goes → I make her go", "ꯃꯍꯥꯛ ꯆꯠꯂꯤ → ꯑꯩ ꯃꯍꯥꯛꯄꯨ ꯆꯠꯍꯜꯂꯤ"),
        ("He writes → I make him write", "ꯃꯍꯥꯛ ꯏꯏ → ꯑꯩ ꯃꯍꯥꯛꯄꯨ ꯏꯍꯜꯂꯤ"),
        ("She sleeps → I make her sleep", "ꯃꯍꯥꯛ ꯇꯨꯝꯃꯤ → ꯑꯩ ꯃꯍꯥꯛꯄꯨ ꯇꯨꯝꯍꯜꯂꯤ"),
        ("The mother feeds the child", "ꯏꯃꯥꯅ ꯑꯅꯧꯕꯕꯨ ꯆꯥꯍꯜꯂꯤ꯫"),
        ("The teacher makes students read", "ꯑꯣꯖꯥꯅ ꯃꯍꯩꯔꯣꯌꯁꯤꯡꯕꯨ ꯄꯍꯜꯂꯤ꯫"),
        ("I made him sit", "ꯑꯩꯅ ꯃꯍꯥꯛꯄꯨ ꯐꯝꯍꯜꯂꯦ꯫"),
        ("She made the children study", "ꯃꯍꯥꯛꯅ ꯑꯅꯧꯕꯁꯤꯡꯕꯨ ꯇꯝꯍꯜꯂꯦ꯫"),
        ("He made me write the letter", "ꯃꯍꯥꯛꯅ ꯑꯩꯕꯨ ꯆꯤꯠꯊꯤ ꯏꯍꯜꯂꯦ꯫"),
        ("I will make him come", "ꯑꯩ ꯃꯍꯥꯛꯄꯨ ꯂꯥꯛꯍꯜꯒꯅꯤ꯫"),
        ("She will make them go", "ꯃꯍꯥꯛꯅ ꯃꯈꯣꯏꯕꯨ ꯆꯠꯍꯜꯒꯅꯤ꯫"),
        ("Mother makes child drink milk", "ꯏꯃꯥꯅ ꯑꯅꯧꯕꯕꯨ ꯁꯪꯒꯣꯝ ꯊꯛꯍꯜꯂꯤ꯫"),
        ("Don't make me run", "ꯑꯩꯕꯨ ꯆꯦꯜꯍꯜꯂꯣꯌꯨ꯫"),
        ("He made me laugh", "ꯃꯍꯥꯛꯅ ꯑꯩꯕꯨ ꯅꯣꯛꯍꯜꯂꯦ꯫"),
        ("I will make her cook", "ꯑꯩ ꯃꯍꯥꯛꯄꯨ ꯁꯥꯍꯜꯒꯅꯤ꯫"),
        ("The father makes son study", "ꯏꯄꯥꯅ ꯃꯆꯥꯕꯨ ꯇꯝꯍꯜꯂꯤ꯫"),
    ],
},

# ━━━ 539: Gender-number agreement ━━━
539: {
    "heading": "Gender-number agreement examples",
    "rows": [
        ("The boy is tall", "ꯅꯨꯄꯃꯆꯥ ꯁꯪꯅꯤ꯫"),
        ("The girl is tall", "ꯅꯨꯄꯤꯃꯆꯥ ꯁꯪꯅꯤ꯫"),
        ("The boys are playing", "ꯅꯨꯄꯃꯆꯥꯁꯤꯡ ꯁꯥꯔꯝꯃꯤ꯫"),
        ("The girls are playing", "ꯅꯨꯄꯤꯃꯆꯥꯁꯤꯡ ꯁꯥꯔꯝꯃꯤ꯫"),
        ("He is a good boy", "ꯃꯍꯥꯛ ꯐꯕ ꯅꯨꯄꯃꯆꯥ ꯑꯃꯅꯤ꯫"),
        ("She is a good girl", "ꯃꯍꯥꯛ ꯐꯕꯤ ꯅꯨꯄꯤꯃꯆꯥ ꯑꯃꯅꯤ꯫"),
        ("The man came", "ꯅꯨꯄ ꯑꯗꯨ ꯂꯥꯛꯂꯦ꯫"),
        ("The woman came", "ꯅꯨꯄꯤ ꯑꯗꯨ ꯂꯥꯛꯂꯦ꯫"),
        ("The men are here", "ꯅꯨꯄꯁꯤꯡ ꯑꯁꯤꯗ ꯂꯩꯏ꯫"),
        ("The women are here", "ꯅꯨꯄꯤꯁꯤꯡ ꯑꯁꯤꯗ ꯂꯩꯏ꯫"),
        ("He is beautiful (phajaba)", "ꯃꯍꯥꯛ ꯐꯖꯕ꯫"),
        ("She is beautiful (phajabi)", "ꯃꯍꯥꯛ ꯐꯖꯕꯤ꯫"),
        ("Big man (achouba)", "ꯅꯨꯄ ꯑꯆꯧꯕ"),
        ("Big woman (achoubi)", "ꯅꯨꯄꯤ ꯑꯆꯧꯕꯤ"),
        ("The children are studying", "ꯑꯅꯧꯕꯁꯤꯡ ꯇꯝꯔꯝꯃꯤ꯫"),
        ("New man (anouba)", "ꯅꯨꯄ ꯑꯅꯧꯕ"),
        ("New woman (anoubi)", "ꯅꯨꯄꯤ ꯑꯅꯧꯕꯤ"),
    ],
},

# ━━━ 540: Perfect Tense – Second Style ━━━
540: {
    "heading": "Perfect tense (2nd style) examples",
    "rows": [
        ("I have eaten (alt.)", "ꯑꯩ ꯆꯥꯂꯦ꯫"),
        ("He has come (alt.)", "ꯃꯍꯥꯛ ꯂꯥꯛꯇ꯭ꯔꯦ꯫"),
        ("She has gone (alt.)", "ꯃꯍꯥꯛ ꯆꯠꯇ꯭ꯔꯦ꯫"),
        ("We have finished (alt.)", "ꯑꯩꯈꯣꯏ ꯂꯣꯏꯁꯤꯟꯇ꯭ꯔꯦ꯫"),
        ("They have arrived (alt.)", "ꯃꯈꯣꯏ ꯊꯨꯡꯇ꯭ꯔꯦ꯫"),
        ("I had eaten before", "ꯑꯩ ꯃꯃꯥꯡꯗ ꯆꯥꯈꯔꯃꯤ꯫"),
        ("He had gone already", "ꯃꯍꯥꯛ ꯍꯧꯖꯤꯛ ꯆꯠꯈꯔꯃꯤ꯫"),
        ("She had slept", "ꯃꯍꯥꯛ ꯇꯨꯝꯈꯔꯃꯤ꯫"),
        ("I will have eaten by tomorrow", "ꯑꯩ ꯍꯌꯦꯡ ꯐꯥꯑꯣꯒꯅꯤ ꯆꯥꯈꯔꯝꯃꯤ꯫"),
        ("He will have left", "ꯃꯍꯥꯛ ꯆꯠꯈꯔꯝꯃꯤ꯫"),
        ("She had read the book", "ꯃꯍꯥꯛ ꯂꯥꯏꯔꯤꯛ ꯄꯈꯔꯃꯤ꯫"),
        ("We had done the work", "ꯑꯩꯈꯣꯏ ꯊꯕꯛ ꯇꯧꯈꯔꯃꯤ꯫"),
        ("They have written already", "ꯃꯈꯣꯏ ꯍꯧꯖꯤꯛ ꯏꯈꯔꯃꯤ꯫"),
        ("I had seen the movie", "ꯑꯩ ꯐꯤꯜꯝ ꯌꯦꯡꯈꯔꯃꯤ꯫"),
        ("He has drunk the water", "ꯃꯍꯥꯛ ꯏꯁꯤꯡ ꯊꯛꯈꯔꯃꯤ꯫"),
        ("She has cooked the food", "ꯃꯍꯥꯛ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯈꯔꯃꯤ꯫"),
        ("We will have come back", "ꯑꯩꯈꯣꯏ ꯍꯟꯅ ꯂꯥꯛꯈꯔꯝꯃꯤ꯫"),
    ],
},

# ━━━ 541: Perfect Continuous ━━━
541: {
    "heading": "Perfect continuous examples",
    "rows": [
        ("I have been eating", "ꯑꯩ ꯆꯥꯔꯛꯂꯦ꯫"),
        ("He has been going", "ꯃꯍꯥꯛ ꯆꯠꯔꯛꯂꯦ꯫"),
        ("She has been reading", "ꯃꯍꯥꯛ ꯄꯕꯔꯛꯂꯦ꯫"),
        ("We have been studying", "ꯑꯩꯈꯣꯏ ꯇꯝꯔꯛꯂꯦ꯫"),
        ("They have been playing", "ꯃꯈꯣꯏ ꯁꯥꯔꯛꯂꯦ꯫"),
        ("I had been sleeping", "ꯑꯩ ꯇꯨꯝꯔꯛꯂꯦ꯫"),
        ("He had been working all day", "ꯃꯍꯥꯛ ꯅꯨꯃꯤꯠ ꯄꯨꯝꯕꯗ ꯊꯕꯛ ꯇꯧꯔꯛꯂꯦ꯫"),
        ("She had been cooking", "ꯃꯍꯥꯛ ꯁꯥꯔꯛꯂꯦ꯫"),
        ("I will have been studying", "ꯑꯩ ꯇꯝꯔꯛꯀꯅꯤ꯫"),
        ("He will have been running", "ꯃꯍꯥꯛ ꯆꯦꯜꯔꯛꯀꯅꯤ꯫"),
        ("I have been waiting for you", "ꯑꯩ ꯅꯪꯕꯨ ꯉꯥꯏꯔꯛꯂꯦ꯫"),
        ("She has been living here", "ꯃꯍꯥꯛ ꯑꯁꯤꯗ ꯂꯩꯔꯛꯂꯦ꯫"),
        ("He has been teaching", "ꯃꯍꯥꯛ ꯇꯝꯍꯟꯔꯛꯂꯦ꯫"),
        ("We had been walking for hours", "ꯑꯩꯈꯣꯏ ꯄꯨꯡ ꯀꯌꯗ ꯆꯠꯔꯛꯂꯦ꯫"),
        ("They have been writing", "ꯃꯈꯣꯏ ꯏꯔꯛꯂꯦ꯫"),
        ("I will have been living here", "ꯑꯩ ꯑꯁꯤꯗ ꯂꯩꯔꯛꯀꯅꯤ꯫"),
        ("She had been singing", "ꯃꯍꯥꯛ ꯏꯁꯩ ꯁꯀꯔꯛꯂꯦ꯫"),
    ],
},

# ━━━ 542: "no/not" vs "don't want" ━━━
542: {
    "heading": "\"No/not\" vs \"don't want\" examples",
    "rows": [
        ("No (natte)", "ꯅꯠꯇꯦ"),
        ("Don't want (pamde)", "ꯄꯝꯗꯦ"),
        ("He is not a teacher", "ꯃꯍꯥꯛ ꯑꯣꯖꯥ ꯅꯠꯇꯦ꯫"),
        ("I don't want tea", "ꯑꯩ ꯆꯥ ꯄꯝꯗꯦ꯫"),
        ("This is not correct", "ꯃꯁꯤ ꯑꯆꯨꯝꯕ ꯅꯠꯇꯦ꯫"),
        ("I don't want to go", "ꯑꯩ ꯆꯠꯄ ꯄꯝꯗꯦ꯫"),
        ("She is not at home", "ꯃꯍꯥꯛ ꯌꯨꯝꯗ ꯂꯩꯇꯦ꯫"),
        ("He doesn't want food", "ꯃꯍꯥꯛ ꯆꯤꯟꯖꯥꯛ ꯄꯝꯗꯦ꯫"),
        ("It is not a book", "ꯃꯁꯤ ꯂꯥꯏꯔꯤꯛ ꯅꯠꯇꯦ꯫"),
        ("I don't want money", "ꯑꯩ ꯄꯥꯏꯁꯥ ꯄꯝꯗꯦ꯫"),
        ("That is not my house", "ꯃꯗꯨ ꯑꯩꯒꯤ ꯌꯨꯝ ꯅꯠꯇꯦ꯫"),
        ("She doesn't want to eat", "ꯃꯍꯥꯛ ꯆꯥꯕ ꯄꯝꯗꯦ꯫"),
        ("He is not coming", "ꯃꯍꯥꯛ ꯂꯥꯛꯇꯦ꯫"),
        ("I don't want to sleep", "ꯑꯩ ꯇꯨꯝꯕ ꯄꯝꯗꯦ꯫"),
        ("This is not water", "ꯃꯁꯤ ꯏꯁꯤꯡ ꯅꯠꯇꯦ꯫"),
        ("She doesn't want to study", "ꯃꯍꯥꯛ ꯇꯝꯕ ꯄꯝꯗꯦ꯫"),
        ("No, that is wrong", "ꯅꯠꯇꯦ, ꯃꯗꯨ ꯑꯆꯨꯝꯕꯅꯤ꯫"),
    ],
},

}  # end LESSONS


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
            translit = mayek_to_roman(mayek)
            rows_with_translit.append([eng, mayek, translit])

        new_table = {
            "type": "table",
            "heading": lesson["heading"],
            "headers": ["English", "Manipuri", "Transliteration"],
            "speakCol": 1,
            "rows": rows_with_translit,
        }

        blocks = chapter.get("blocks", [])
        blocks = [b for b in blocks if not (
            b.get("type") == "table" and
            b.get("heading") in ("Practice sentences", lesson["heading"],
                                  "Starter pronouns")
        )]
        blocks.append(new_table)
        chapter["blocks"] = blocks
        updated += 1

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sys.stdout.buffer.write(f"Updated {updated} grammar lessons (510-542) in data_meitei.json\n".encode("utf-8"))


if __name__ == "__main__":
    main()
