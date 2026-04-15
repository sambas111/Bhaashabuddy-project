#!/usr/bin/env python3
"""Populate pattern lessons 543-570 (3.1-3.28) with topic-relevant sentences."""
import json, sys
from pathlib import Path

BASE = Path(__file__).parent.resolve()

# ── Mayek→Roman transliterator ──
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

# ━━━ 543: "Going to" ━━━
543: {
    "heading": "\"Going to\" phrase examples",
    "rows": [
        ("I am going to eat", "ꯑꯩ ꯆꯥꯒꯅꯤ꯫"),
        ("He is going to come", "ꯃꯍꯥꯛ ꯂꯥꯛꯀꯅꯤ꯫"),
        ("She is going to sleep", "ꯃꯍꯥꯛ ꯇꯨꯝꯒꯅꯤ꯫"),
        ("We are going to play", "ꯑꯩꯈꯣꯏ ꯁꯥꯒꯅꯤ꯫"),
        ("They are going to study", "ꯃꯈꯣꯏ ꯇꯝꯒꯅꯤ꯫"),
        ("I am going to cook food", "ꯑꯩ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯒꯅꯤ꯫"),
        ("He is going to write a letter", "ꯃꯍꯥꯛ ꯆꯤꯠꯊꯤ ꯏꯒꯅꯤ꯫"),
        ("She is going to buy a dress", "ꯃꯍꯥꯛ ꯐꯤ ꯑꯃ ꯂꯩꯒꯅꯤ꯫"),
        ("We are going to watch a movie", "ꯑꯩꯈꯣꯏ ꯐꯤꯜꯝ ꯌꯦꯡꯒꯅꯤ꯫"),
        ("I am going to go to school", "ꯑꯩ ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯀꯅꯤ꯫"),
        ("He is going to drink water", "ꯃꯍꯥꯛ ꯏꯁꯤꯡ ꯊꯛꯀꯅꯤ꯫"),
        ("She is going to read the book", "ꯃꯍꯥꯛ ꯂꯥꯏꯔꯤꯛ ꯄꯕꯒꯅꯤ꯫"),
        ("Are you going to come tomorrow?", "ꯅꯪ ꯍꯌꯦꯡ ꯂꯥꯛꯀꯗ꯭ꯔ?"),
        ("I am going to meet my friend", "ꯑꯩ ꯑꯩꯒꯤ ꯃꯔꯨꯞꯕꯨ ꯎꯅꯒꯅꯤ꯫"),
        ("They are going to build a house", "ꯃꯈꯣꯏ ꯌꯨꯝ ꯑꯃ ꯁꯥꯒꯅꯤ꯫"),
        ("We are going to leave now", "ꯑꯩꯈꯣꯏ ꯍꯧꯖꯤꯛ ꯆꯠꯀꯅꯤ꯫"),
        ("I am going to learn Meitei", "ꯑꯩ ꯃꯩꯇꯩꯂꯣꯟ ꯇꯝꯒꯅꯤ꯫"),
    ],
},

# ━━━ 544: "Used to" ━━━
544: {
    "heading": "\"Used to\" phrase examples",
    "rows": [
        ("I used to eat rice", "ꯑꯩ ꯆꯥꯛ ꯆꯥꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("He used to go to school", "ꯃꯍꯥꯛ ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("She used to sing songs", "ꯃꯍꯥꯛ ꯏꯁꯩ ꯁꯀꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("We used to play here", "ꯑꯩꯈꯣꯏ ꯑꯁꯤꯗ ꯁꯥꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("They used to live in Imphal", "ꯃꯈꯣꯏ ꯏꯝꯐꯥꯜꯗ ꯂꯩꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("I used to read every day", "ꯑꯩ ꯅꯨꯃꯤꯠ ꯈꯨꯗꯤꯡꯃꯛ ꯄꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("He used to walk to school", "ꯃꯍꯥꯛ ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("She used to cook well", "ꯃꯍꯥꯛ ꯐꯖꯅ ꯁꯥꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("I used to drink tea", "ꯑꯩ ꯆꯥ ꯊꯛꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("He used to teach Meitei", "ꯃꯍꯥꯛ ꯃꯩꯇꯩꯂꯣꯟ ꯇꯝꯍꯟꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("She used to sleep early", "ꯃꯍꯥꯛ ꯊꯨꯅ ꯇꯨꯝꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("We used to watch movies", "ꯑꯩꯈꯣꯏ ꯐꯤꯜꯝ ꯌꯦꯡꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("They used to come here", "ꯃꯈꯣꯏ ꯑꯁꯤꯗ ꯂꯥꯛꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("I used to run in the morning", "ꯑꯩ ꯅꯨꯃꯤꯠ ꯊꯣꯛꯇ ꯆꯦꯜꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("He used to help his mother", "ꯃꯍꯥꯛ ꯃꯍꯥꯛꯀꯤ ꯏꯃꯥꯕꯨ ꯃꯇꯦꯡ ꯄꯥꯡꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("We used to study together", "ꯑꯩꯈꯣꯏ ꯄꯨꯟꯁꯤ ꯇꯝꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("I used to write letters", "ꯑꯩ ꯆꯤꯠꯊꯤ ꯏꯕ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
    ],
},

# ━━━ 545: "Used to" old style ━━━
545: {
    "heading": "\"Used to\" old style examples",
    "rows": [
        ("I used to eat (old)", "ꯑꯩ ꯆꯥꯕꯤ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("He used to go (old)", "ꯃꯍꯥꯛ ꯆꯠꯂꯝꯃꯤ꯫"),
        ("She used to sing (old)", "ꯃꯍꯥꯛ ꯏꯁꯩ ꯁꯀꯂꯝꯃꯤ꯫"),
        ("We used to play (old)", "ꯑꯩꯈꯣꯏ ꯁꯥꯂꯝꯃꯤ꯫"),
        ("They used to come (old)", "ꯃꯈꯣꯏ ꯂꯥꯛꯂꯝꯃꯤ꯫"),
        ("I used to read (old)", "ꯑꯩ ꯄꯕꯤ ꯑꯣꯏꯔꯝꯃꯤ꯫"),
        ("He used to sleep early (old)", "ꯃꯍꯥꯛ ꯊꯨꯅ ꯇꯨꯝꯂꯝꯃꯤ꯫"),
        ("She used to teach (old)", "ꯃꯍꯥꯛ ꯇꯝꯍꯟꯂꯝꯃꯤ꯫"),
        ("We used to run (old)", "ꯑꯩꯈꯣꯏ ꯆꯦꯜꯂꯝꯃꯤ꯫"),
        ("They used to sit here (old)", "ꯃꯈꯣꯏ ꯑꯁꯤꯗ ꯐꯝꯂꯝꯃꯤ꯫"),
        ("I used to drink tea (old)", "ꯑꯩ ꯆꯥ ꯊꯛꯂꯝꯃꯤ꯫"),
        ("He used to write poems (old)", "ꯃꯍꯥꯛ ꯁꯩꯔꯦꯡ ꯏꯂꯝꯃꯤ꯫"),
        ("She used to cook rice (old)", "ꯃꯍꯥꯛ ꯆꯥꯛ ꯁꯥꯂꯝꯃꯤ꯫"),
        ("We used to live there (old)", "ꯑꯩꯈꯣꯏ ꯑꯗꯨꯗ ꯂꯩꯂꯝꯃꯤ꯫"),
        ("He used to help people (old)", "ꯃꯍꯥꯛ ꯃꯤꯁꯤꯡꯕꯨ ꯃꯇꯦꯡ ꯄꯥꯡꯂꯝꯃꯤ꯫"),
        ("She used to walk slowly (old)", "ꯃꯍꯥꯛ ꯇꯞꯅ ꯆꯠꯂꯝꯃꯤ꯫"),
        ("They used to work hard (old)", "ꯃꯈꯣꯏ ꯍꯥꯏꯅ ꯊꯕꯛ ꯇꯧꯂꯝꯃꯤ꯫"),
    ],
},

# ━━━ 546: If-Then ━━━
546: {
    "heading": "\"If-Then\" sentence examples",
    "rows": [
        ("If you come, I will go", "ꯅꯪ ꯂꯥꯛꯂꯕꯗꯤ, ꯑꯩ ꯆꯠꯀꯅꯤ꯫"),
        ("If it rains, I will stay home", "ꯅꯣꯡ ꯇꯥꯛꯂꯕꯗꯤ, ꯑꯩ ꯌꯨꯝꯗ ꯂꯩꯒꯅꯤ꯫"),
        ("If he studies, he will pass", "ꯃꯍꯥꯛ ꯇꯝꯂꯕꯗꯤ, ꯃꯍꯥꯛ ꯄꯥꯁ ꯇꯧꯒꯅꯤ꯫"),
        ("If she cooks, we will eat", "ꯃꯍꯥꯛ ꯁꯥꯂꯕꯗꯤ, ꯑꯩꯈꯣꯏ ꯆꯥꯒꯅꯤ꯫"),
        ("If I have money, I will buy it", "ꯑꯩꯗ ꯄꯥꯏꯁꯥ ꯂꯩꯔꯕꯗꯤ, ꯑꯩ ꯂꯩꯒꯅꯤ꯫"),
        ("If you work hard, you will win", "ꯅꯪ ꯍꯥꯏꯅ ꯊꯕꯛ ꯇꯧꯂꯕꯗꯤ, ꯅꯪ ꯃꯥꯏꯄꯥꯛꯀꯅꯤ꯫"),
        ("If they help, we will finish", "ꯃꯈꯣꯏ ꯃꯇꯦꯡ ꯄꯥꯡꯂꯕꯗꯤ, ꯑꯩꯈꯣꯏ ꯂꯣꯏꯁꯤꯜꯒꯅꯤ꯫"),
        ("If he calls, tell me", "ꯃꯍꯥꯛ ꯀꯧꯂꯕꯗꯤ, ꯑꯩꯕꯨ ꯍꯥꯏꯕꯤꯌꯨ꯫"),
        ("If I am late, don't wait", "ꯑꯩ ꯊꯦꯡꯂꯕꯗꯤ, ꯉꯥꯏꯔꯣꯏꯌꯨ꯫"),
        ("If she comes early, we will go", "ꯃꯍꯥꯛ ꯊꯨꯅ ꯂꯥꯛꯂꯕꯗꯤ, ꯑꯩꯈꯣꯏ ꯆꯠꯀꯅꯤ꯫"),
        ("If you eat, you will be strong", "ꯅꯪ ꯆꯥꯂꯕꯗꯤ, ꯅꯪ ꯁꯦꯡꯂꯝ ꯑꯣꯏꯒꯅꯤ꯫"),
        ("If he comes, I will be happy", "ꯃꯍꯥꯛ ꯂꯥꯛꯂꯕꯗꯤ, ꯑꯩ ꯅꯨꯡꯉꯥꯏꯒꯅꯤ꯫"),
        ("If I know, I will tell you", "ꯑꯩ ꯈꯪꯂꯕꯗꯤ, ꯅꯪꯗ ꯍꯥꯏꯒꯅꯤ꯫"),
        ("If we go now, we will reach early", "ꯑꯩꯈꯣꯏ ꯍꯧꯖꯤꯛ ꯆꯠꯂꯕꯗꯤ, ꯊꯨꯅ ꯊꯨꯡꯒꯅꯤ꯫"),
        ("If you sleep early, wake up early", "ꯅꯪ ꯊꯨꯅ ꯇꯨꯝꯂꯕꯗꯤ, ꯊꯨꯅ ꯍꯛꯂꯣ꯫"),
        ("If they don't come, we will leave", "ꯃꯈꯣꯏ ꯂꯥꯛꯇꯗꯤ, ꯑꯩꯈꯣꯏ ꯆꯠꯀꯅꯤ꯫"),
        ("If she reads, she will understand", "ꯃꯍꯥꯛ ꯄꯂꯕꯗꯤ, ꯃꯍꯥꯛ ꯈꯪꯒꯅꯤ꯫"),
    ],
},

# ━━━ 547: Prepositions with Verbs ━━━
547: {
    "heading": "Prepositions with verb examples",
    "rows": [
        ("Go to school", "ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯂꯣ꯫"),
        ("Come from home", "ꯌꯨꯝ ꯗꯒꯤ ꯂꯥꯛꯂꯣ꯫"),
        ("Sit on the chair", "ꯆꯦꯌꯔꯗ ꯐꯝꯃꯨ꯫"),
        ("Walk with me", "ꯑꯩꯒ ꯆꯠꯂꯣ꯫"),
        ("Look at this", "ꯃꯁꯤꯕꯨ ꯌꯦꯡꯕꯤꯌꯨ꯫"),
        ("Listen to the teacher", "ꯑꯣꯖꯥꯒꯤ ꯋꯥ ꯇꯕꯤꯌꯨ꯫"),
        ("Write with a pen", "ꯀꯂꯝꯅ ꯏꯌꯨ꯫"),
        ("Speak in Meitei", "ꯃꯩꯇꯩꯂꯣꯟꯗ ꯉꯥꯡꯕꯤꯌꯨ꯫"),
        ("Wait for the bus", "ꯕꯁ ꯉꯥꯏꯕꯤꯌꯨ꯫"),
        ("Run to the field", "ꯃꯐꯝꯗ ꯆꯦꯜꯂꯣ꯫"),
        ("Live in Manipur", "ꯃꯅꯤꯄꯨꯔꯗ ꯂꯩꯌꯨ꯫"),
        ("Think about this", "ꯃꯁꯤꯒꯤ ꯃꯇꯥꯡꯗ ꯋꯥꯈꯜ ꯂꯧꯌꯨ꯫"),
        ("I went to the market", "ꯑꯩ ꯀꯩꯊꯦꯜꯗ ꯆꯠꯂꯦ꯫"),
        ("She came with her friend", "ꯃꯍꯥꯛ ꯃꯍꯥꯛꯀꯤ ꯃꯔꯨꯞꯒ ꯂꯥꯛꯂꯦ꯫"),
        ("He is looking for a book", "ꯃꯍꯥꯛ ꯂꯥꯏꯔꯤꯛ ꯑꯃ ꯊꯤꯔꯝꯃꯤ꯫"),
        ("I will talk to him", "ꯑꯩ ꯃꯍꯥꯛꯒ ꯋꯥꯔꯤ ꯁꯥꯅꯒꯅꯤ꯫"),
        ("We played in the garden", "ꯑꯩꯈꯣꯏ ꯃꯐꯝꯗ ꯁꯥꯈꯔꯦ꯫"),
    ],
},

# ━━━ 548: Adjectives ━━━
548: {
    "heading": "Adjective examples",
    "rows": [
        ("Good (phaba)", "ꯐꯕ"),
        ("Bad (athiba)", "ꯑꯊꯤꯕ"),
        ("Big (achouba)", "ꯑꯆꯧꯕ"),
        ("Small (aningba)", "ꯑꯅꯤꯡꯕ"),
        ("Beautiful (phajaba)", "ꯐꯖꯕ"),
        ("New (anouba)", "ꯑꯅꯧꯕ"),
        ("Old (arumba)", "ꯑꯔꯨꯝꯕ"),
        ("Hot (angaoba)", "ꯑꯉꯥꯑꯣꯕ"),
        ("Cold (khangba)", "ꯈꯪꯕ"),
        ("The house is big", "ꯌꯨꯝ ꯑꯗꯨ ꯑꯆꯧꯕꯅꯤ꯫"),
        ("The flower is beautiful", "ꯂꯩ ꯑꯗꯨ ꯐꯖꯕꯅꯤ꯫"),
        ("The food is hot", "ꯆꯤꯟꯖꯥꯛ ꯑꯗꯨ ꯑꯉꯥꯑꯣꯕꯅꯤ꯫"),
        ("She is a good girl", "ꯃꯍꯥꯛ ꯐꯕꯤ ꯅꯨꯄꯤꯃꯆꯥ ꯑꯃꯅꯤ꯫"),
        ("He is a tall boy", "ꯃꯍꯥꯛ ꯁꯪ ꯅꯨꯄꯃꯆꯥ ꯑꯃꯅꯤ꯫"),
        ("This is a new book", "ꯃꯁꯤ ꯑꯅꯧꯕ ꯂꯥꯏꯔꯤꯛ ꯑꯃꯅꯤ꯫"),
        ("The water is cold", "ꯏꯁꯤꯡ ꯑꯗꯨ ꯈꯪꯕꯅꯤ꯫"),
        ("The old man came", "ꯑꯔꯨꯝꯕ ꯅꯨꯄ ꯑꯗꯨ ꯂꯥꯛꯂꯦ꯫"),
    ],
},

# ━━━ 549: Can / To be able to ━━━
549: {
    "heading": "\"Can\" / ability examples",
    "rows": [
        ("I can eat", "ꯑꯩ ꯆꯥꯕ ꯉꯝꯃꯤ꯫"),
        ("He can run fast", "ꯃꯍꯥꯛ ꯊꯨꯅ ꯆꯦꯜꯕ ꯉꯝꯃꯤ꯫"),
        ("She can read Meitei Mayek", "ꯃꯍꯥꯛ ꯃꯩꯇꯩ ꯃꯌꯦꯛ ꯄꯕ ꯉꯝꯃꯤ꯫"),
        ("We can speak Manipuri", "ꯑꯩꯈꯣꯏ ꯃꯩꯇꯩꯂꯣꯟ ꯉꯥꯡꯕ ꯉꯝꯃꯤ꯫"),
        ("They can sing well", "ꯃꯈꯣꯏ ꯐꯖꯅ ꯏꯁꯩ ꯁꯀꯕ ꯉꯝꯃꯤ꯫"),
        ("I cannot swim", "ꯑꯩ ꯏꯁꯤꯡꯗ ꯂꯨꯝꯕ ꯉꯝꯗꯦ꯫"),
        ("He cannot come today", "ꯃꯍꯥꯛ ꯉꯁꯤ ꯂꯥꯛꯕ ꯉꯝꯗꯦ꯫"),
        ("Can you write the exam?", "ꯅꯍꯥꯛ ꯄꯔꯤꯈꯥ ꯊꯕ ꯉꯝꯒꯗ꯭ꯔ?"),
        ("Can you lift this box?", "ꯃꯁꯤꯒꯤ ꯕꯣꯛꯁ ꯊꯪꯒꯠꯄ ꯉꯝꯕ꯭ꯔ?"),
        ("I can cook food", "ꯑꯩ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯕ ꯉꯝꯃꯤ꯫"),
        ("She can drive a car", "ꯃꯍꯥꯛ ꯒꯥꯔꯤ ꯊꯧꯕ ꯉꯝꯃꯤ꯫"),
        ("We can do this", "ꯑꯩꯈꯣꯏ ꯃꯁꯤ ꯇꯧꯕ ꯉꯝꯃꯤ꯫"),
        ("He cannot see without glasses", "ꯃꯍꯥꯛ ꯁꯦꯛꯇꯅ ꯌꯦꯡꯕ ꯉꯝꯗꯦ꯫"),
        ("They can play football", "ꯃꯈꯣꯏ ꯐꯨꯠꯕꯣꯜ ꯁꯥꯕ ꯉꯝꯃꯤ꯫"),
        ("Can you help me?", "ꯑꯩꯕꯨ ꯃꯇꯦꯡ ꯄꯥꯡꯕ ꯉꯃꯒꯗ꯭ꯔ?"),
        ("I can understand Meitei", "ꯑꯩ ꯃꯩꯇꯩꯂꯣꯟ ꯈꯪꯕ ꯉꯝꯃꯤ꯫"),
        ("She can dance well", "ꯃꯍꯥꯛ ꯐꯖꯅ ꯖꯒꯣꯏ ꯁꯥꯕ ꯉꯝꯃꯤ꯫"),
    ],
},

# ━━━ 550: To Want / To Need ━━━
550: {
    "heading": "\"Want\" / \"Need\" examples",
    "rows": [
        ("I want water", "ꯑꯩ ꯏꯁꯤꯡ ꯄꯝꯃꯤ꯫"),
        ("He wants food", "ꯃꯍꯥꯛ ꯆꯤꯟꯖꯥꯛ ꯄꯝꯃꯤ꯫"),
        ("She wants a book", "ꯃꯍꯥꯛ ꯂꯥꯏꯔꯤꯛ ꯑꯃ ꯄꯝꯃꯤ꯫"),
        ("I need help", "ꯑꯩꯗ ꯃꯇꯦꯡ ꯃꯔꯤ꯫"),
        ("He needs money", "ꯃꯍꯥꯛꯗ ꯄꯥꯏꯁꯥ ꯃꯔꯤ꯫"),
        ("I don't want tea", "ꯑꯩ ꯆꯥ ꯄꯝꯗꯦ꯫"),
        ("She doesn't want that", "ꯃꯍꯥꯛ ꯃꯗꯨ ꯄꯝꯗꯦ꯫"),
        ("Do you want rice?", "ꯅꯪ ꯆꯥꯛ ꯄꯝꯕ꯭ꯔ?"),
        ("I want to go home", "ꯑꯩ ꯌꯨꯝꯗ ꯆꯠꯅꯤꯡꯉꯩ꯫"),
        ("He wants to sleep", "ꯃꯍꯥꯛ ꯇꯨꯝꯅꯤꯡꯉꯩ꯫"),
        ("She wants to eat", "ꯃꯍꯥꯛ ꯆꯥꯅꯤꯡꯉꯩ꯫"),
        ("We need a doctor", "ꯑꯩꯈꯣꯏꯗ ꯗꯣꯛꯇꯔ ꯑꯃ ꯃꯔꯤ꯫"),
        ("I don't need this", "ꯑꯩꯗ ꯃꯁꯤ ꯃꯔꯣꯏ꯫"),
        ("He doesn't need money", "ꯃꯍꯥꯛꯗ ꯄꯥꯏꯁꯥ ꯃꯔꯣꯏ꯫"),
        ("What do you want?", "ꯅꯪ ꯀꯔꯤ ꯄꯝꯕꯒꯦ?"),
        ("I want a glass of water", "ꯑꯩ ꯏꯁꯤꯡ ꯒ꯭ꯂꯥꯁ ꯑꯃ ꯄꯝꯃꯤ꯫"),
        ("She needs rest", "ꯃꯍꯥꯛꯗ ꯂꯣꯏꯅ ꯃꯔꯤ꯫"),
    ],
},

# ━━━ 551: To Become / To Happen ━━━
551: {
    "heading": "\"To become\" / \"to happen\" examples",
    "rows": [
        ("He became a teacher", "ꯃꯍꯥꯛ ꯑꯣꯖꯥ ꯑꯣꯏꯂꯦ꯫"),
        ("She became a doctor", "ꯃꯍꯥꯛ ꯗꯣꯛꯇꯔ ꯑꯣꯏꯂꯦ꯫"),
        ("It became cold", "ꯃꯗꯨ ꯈꯪ ꯑꯣꯏꯂꯦ꯫"),
        ("What happened?", "ꯀꯔꯤ ꯑꯣꯏꯈꯔꯦ?"),
        ("Nothing happened", "ꯀꯔꯤꯁꯨ ꯑꯣꯏꯈꯔꯗꯦ꯫"),
        ("An accident happened", "ꯑꯦꯛꯁꯤꯗꯦꯟꯠ ꯑꯃ ꯑꯣꯏꯈꯔꯦ꯫"),
        ("He became angry", "ꯃꯍꯥꯛ ꯁꯥꯅꯕ ꯑꯣꯏꯂꯦ꯫"),
        ("She became happy", "ꯃꯍꯥꯛ ꯅꯨꯡꯉꯥꯏꯕ ꯑꯣꯏꯂꯦ꯫"),
        ("The flower became dry", "ꯂꯩ ꯑꯗꯨ ꯀꯪ ꯑꯣꯏꯂꯦ꯫"),
        ("I will become a teacher", "ꯑꯩ ꯑꯣꯖꯥ ꯑꯣꯏꯒꯅꯤ꯫"),
        ("What will happen?", "ꯀꯔꯤ ꯑꯣꯏꯒꯅꯤ?"),
        ("It happened yesterday", "ꯃꯗꯨ ꯉꯔꯪ ꯑꯣꯏꯈꯔꯦ꯫"),
        ("It will become good", "ꯃꯗꯨ ꯐꯕ ꯑꯣꯏꯒꯅꯤ꯫"),
        ("He is becoming tall", "ꯃꯍꯥꯛ ꯁꯪ ꯑꯣꯏꯔꯤ꯫"),
        ("She became famous", "ꯃꯍꯥꯛ ꯃꯤꯡ ꯂꯩꯕ ꯑꯣꯏꯂꯦ꯫"),
        ("The food became cold", "ꯆꯤꯟꯖꯥꯛ ꯑꯗꯨ ꯈꯪ ꯑꯣꯏꯂꯦ꯫"),
        ("I want to become a singer", "ꯑꯩ ꯏꯁꯩ ꯁꯀꯄ ꯑꯣꯏꯅꯤꯡꯉꯩ꯫"),
    ],
},

# ━━━ 552: Should ━━━
552: {
    "heading": "\"Should\" examples",
    "rows": [
        ("I should go", "ꯑꯩ ꯆꯠꯀꯗꯕꯅꯤ꯫"),
        ("You should eat", "ꯅꯪ ꯆꯥꯀꯗꯕꯅꯤ꯫"),
        ("He should study", "ꯃꯍꯥꯛ ꯇꯝꯀꯗꯕꯅꯤ꯫"),
        ("She should sleep early", "ꯃꯍꯥꯛ ꯊꯨꯅ ꯇꯨꯝꯀꯗꯕꯅꯤ꯫"),
        ("We should help them", "ꯑꯩꯈꯣꯏ ꯃꯈꯣꯏꯕꯨ ꯃꯇꯦꯡ ꯄꯥꯡꯀꯗꯕꯅꯤ꯫"),
        ("You should speak slowly", "ꯅꯪ ꯇꯞꯅ ꯉꯥꯡꯀꯗꯕꯅꯤ꯫"),
        ("He should come on time", "ꯃꯍꯥꯛ ꯃꯇꯝꯗ ꯂꯥꯛꯀꯗꯕꯅꯤ꯫"),
        ("She should read more", "ꯃꯍꯥꯛ ꯍꯦꯟꯅ ꯄꯀꯗꯕꯅꯤ꯫"),
        ("We should not waste time", "ꯑꯩꯈꯣꯏ ꯃꯇꯝ ꯃꯪꯍꯟꯔꯣꯏꯗꯕꯅꯤ꯫"),
        ("You should not lie", "ꯅꯪ ꯏꯀꯥꯏ ꯍꯥꯏꯔꯣꯏꯗꯕꯅꯤ꯫"),
        ("He should drink water", "ꯃꯍꯥꯛ ꯏꯁꯤꯡ ꯊꯛꯀꯗꯕꯅꯤ꯫"),
        ("What should I do?", "ꯑꯩ ꯀꯔꯤ ꯇꯧ ꯍꯥꯏꯔꯤꯅꯣ?"),
        ("She should cook dinner", "ꯃꯍꯥꯛ ꯅꯨꯃꯤꯗꯪ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯀꯗꯕꯅꯤ꯫"),
        ("I should learn Meitei", "ꯑꯩ ꯃꯩꯇꯩꯂꯣꯟ ꯇꯝꯀꯗꯕꯅꯤ꯫"),
        ("You should rest now", "ꯅꯪ ꯍꯧꯖꯤꯛ ꯂꯣꯏꯅ ꯂꯩꯀꯗꯕꯅꯤ꯫"),
        ("He should be careful", "ꯃꯍꯥꯛ ꯆꯦꯛꯁꯤꯟꯅ ꯂꯩꯀꯗꯕꯅꯤ꯫"),
        ("We should go together", "ꯑꯩꯈꯣꯏ ꯄꯨꯟꯁꯤ ꯆꯠꯀꯗꯕꯅꯤ꯫"),
    ],
},

# ━━━ 553: Must / Have to ━━━
553: {
    "heading": "\"Must\" / \"have to\" examples",
    "rows": [
        ("I must go now", "ꯑꯩ ꯍꯧꯖꯤꯛ ꯆꯠꯀꯗꯕꯅꯤ꯫"),
        ("He must study hard", "ꯃꯍꯥꯛ ꯍꯥꯏꯅ ꯇꯝꯀꯗꯕꯅꯤ꯫"),
        ("She has to cook food", "ꯃꯍꯥꯛ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯀꯗꯕꯅꯤ꯫"),
        ("We have to finish this", "ꯑꯩꯈꯣꯏ ꯃꯁꯤ ꯂꯣꯏꯁꯤꯜꯀꯗꯕꯅꯤ꯫"),
        ("You must come tomorrow", "ꯅꯪ ꯍꯌꯦꯡ ꯂꯥꯛꯀꯗꯕꯅꯤ꯫"),
        ("He has to pay the money", "ꯃꯍꯥꯛ ꯄꯥꯏꯁꯥ ꯄꯤꯀꯗꯕꯅꯤ꯫"),
        ("She must take medicine", "ꯃꯍꯥꯛ ꯂꯥꯌ ꯆꯥꯀꯗꯕꯅꯤ꯫"),
        ("I have to work today", "ꯑꯩ ꯉꯁꯤ ꯊꯕꯛ ꯇꯧꯀꯗꯕꯅꯤ꯫"),
        ("We must listen to elders", "ꯑꯩꯈꯣꯏ ꯑꯆꯧꯕꯁꯤꯡꯒꯤ ꯋꯥ ꯇꯀꯗꯕꯅꯤ꯫"),
        ("He must write the letter", "ꯃꯍꯥꯛ ꯆꯤꯠꯊꯤ ꯏꯀꯗꯕꯅꯤ꯫"),
        ("You have to wake up early", "ꯅꯪ ꯊꯨꯅ ꯍꯛꯀꯗꯕꯅꯤ꯫"),
        ("She has to go to the hospital", "ꯃꯍꯥꯛ ꯍꯣꯁ꯭ꯄꯤꯇꯜꯗ ꯆꯠꯀꯗꯕꯅꯤ꯫"),
        ("I must tell the truth", "ꯑꯩ ꯑꯆꯨꯝꯕ ꯍꯥꯏꯀꯗꯕꯅꯤ꯫"),
        ("They have to leave now", "ꯃꯈꯣꯏ ꯍꯧꯖꯤꯛ ꯆꯠꯀꯗꯕꯅꯤ꯫"),
        ("He must not be late", "ꯃꯍꯥꯛ ꯊꯦꯡꯔꯣꯏꯗꯕꯅꯤ꯫"),
        ("We have to buy food", "ꯑꯩꯈꯣꯏ ꯆꯤꯟꯖꯥꯛ ꯂꯩꯀꯗꯕꯅꯤ꯫"),
        ("I must go to school", "ꯑꯩ ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯀꯗꯕꯅꯤ꯫"),
    ],
},

# ━━━ 554: "To keep doing" ━━━
554: {
    "heading": "\"Keep doing\" examples",
    "rows": [
        ("Keep eating", "ꯆꯥꯔꯛꯅꯕꯤꯌꯨ꯫"),
        ("Keep reading", "ꯄꯕꯔꯛꯅꯕꯤꯌꯨ꯫"),
        ("Keep walking", "ꯆꯠꯔꯛꯅꯕꯤꯌꯨ꯫"),
        ("Keep studying", "ꯇꯝꯔꯛꯅꯕꯤꯌꯨ꯫"),
        ("Keep working", "ꯊꯕꯛ ꯇꯧꯔꯛꯅꯕꯤꯌꯨ꯫"),
        ("I keep eating rice", "ꯑꯩ ꯆꯥꯛ ꯆꯥꯔꯛꯂꯤ꯫"),
        ("He keeps going there", "ꯃꯍꯥꯛ ꯑꯗꯨꯗ ꯆꯠꯔꯛꯂꯤ꯫"),
        ("She keeps singing", "ꯃꯍꯥꯛ ꯏꯁꯩ ꯁꯀꯔꯛꯂꯤ꯫"),
        ("We keep trying", "ꯑꯩꯈꯣꯏ ꯍꯣꯠꯅꯔꯛꯂꯤ꯫"),
        ("They keep coming late", "ꯃꯈꯣꯏ ꯊꯦꯡꯅ ꯂꯥꯛꯔꯛꯂꯤ꯫"),
        ("I kept running", "ꯑꯩ ꯆꯦꯜꯔꯛꯂꯦ꯫"),
        ("He kept writing", "ꯃꯍꯥꯛ ꯏꯔꯛꯂꯦ꯫"),
        ("She kept cooking", "ꯃꯍꯥꯛ ꯁꯥꯔꯛꯂꯦ꯫"),
        ("We kept playing", "ꯑꯩꯈꯣꯏ ꯁꯥꯔꯛꯂꯦ꯫"),
        ("Don't keep waiting", "ꯉꯥꯏꯔꯛꯂꯣꯌꯨ꯫"),
        ("Keep learning Meitei", "ꯃꯩꯇꯩꯂꯣꯟ ꯇꯝꯔꯛꯅꯕꯤꯌꯨ꯫"),
        ("He keeps forgetting", "ꯃꯍꯥꯛ ꯀꯞꯔꯛꯂꯤ꯫"),
    ],
},

# ━━━ 555: Comparison ━━━
555: {
    "heading": "Comparison examples",
    "rows": [
        ("He is taller than me", "ꯃꯍꯥꯛ ꯑꯩꯗꯒꯤ ꯁꯪꯅꯤ꯫"),
        ("She is more beautiful than her", "ꯃꯍꯥꯛ ꯃꯍꯥꯛꯗꯒꯤ ꯐꯖꯕꯤꯅꯤ꯫"),
        ("This book is bigger than that", "ꯂꯥꯏꯔꯤꯛ ꯑꯁꯤ ꯃꯗꯨꯗꯒꯤ ꯑꯆꯧꯕꯅꯤ꯫"),
        ("Imphal is bigger than Ukhrul", "ꯏꯝꯐꯥꯜ ꯎꯈꯔꯨꯜꯗꯒꯤ ꯑꯆꯧꯕꯅꯤ꯫"),
        ("He is the tallest in class", "ꯃꯍꯥꯛ ꯀ꯭ꯂꯥꯁꯇ ꯈꯋꯥꯏꯗꯒꯤ ꯁꯪꯅꯤ꯫"),
        ("This is the best book", "ꯃꯁꯤ ꯈꯋꯥꯏꯗꯒꯤ ꯐꯕ ꯂꯥꯏꯔꯤꯛꯅꯤ꯫"),
        ("She runs faster than him", "ꯃꯍꯥꯛ ꯃꯍꯥꯛꯗꯒꯤ ꯊꯨꯅ ꯆꯦꯜꯂꯤ꯫"),
        ("Which is the sweetest fruit?", "ꯈꯋꯥꯏꯗꯒꯤ ꯊꯨꯝꯕ ꯍꯩ ꯀꯔꯝꯕꯅꯣ?"),
        ("He is as tall as his brother", "ꯃꯍꯥꯛ ꯃꯍꯥꯛꯀꯤ ꯏꯌꯝꯕꯒꯨꯝꯅ ꯁꯪꯅꯤ꯫"),
        ("This food is better than that", "ꯆꯤꯟꯖꯥꯛ ꯑꯁꯤ ꯃꯗꯨꯗꯒꯤ ꯐꯅꯤ꯫"),
        ("She is the most beautiful", "ꯃꯍꯥꯛ ꯈꯋꯥꯏꯗꯒꯤ ꯐꯖꯕꯤꯅꯤ꯫"),
        ("My house is smaller than yours", "ꯑꯩꯒꯤ ꯌꯨꯝ ꯅꯪꯒꯤꯗꯒꯤ ꯑꯅꯤꯡꯕꯅꯤ꯫"),
        ("He is older than me", "ꯃꯍꯥꯛ ꯑꯩꯗꯒꯤ ꯑꯔꯨꯝꯕꯅꯤ꯫"),
        ("This is the cheapest one", "ꯃꯁꯤ ꯈꯋꯥꯏꯗꯒꯤ ꯃꯃꯜ ꯍꯦꯛꯇꯅꯤ꯫"),
        ("He is stronger than her", "ꯃꯍꯥꯛ ꯃꯍꯥꯛꯗꯒꯤ ꯁꯦꯡꯂꯝꯅꯤ꯫"),
        ("Which newspaper is the best?", "ꯈꯋꯥꯏꯗꯒꯤ ꯐꯕ ꯈꯕꯔ ꯀꯔꯤꯅꯣ?"),
        ("Today is hotter than yesterday", "ꯉꯁꯤ ꯉꯔꯪꯗꯒꯤ ꯑꯉꯥꯑꯣꯕꯅꯤ꯫"),
    ],
},

# ━━━ 556: To Know ━━━
556: {
    "heading": "\"To know\" examples",
    "rows": [
        ("I know", "ꯑꯩ ꯈꯪꯏ꯫"),
        ("I don't know", "ꯑꯩ ꯈꯪꯗꯦ꯫"),
        ("He knows the answer", "ꯃꯍꯥꯛ ꯄꯥꯑꯣꯈꯨꯝ ꯈꯪꯏ꯫"),
        ("She doesn't know the way", "ꯃꯍꯥꯛ ꯂꯝꯕꯤ ꯈꯪꯗꯦ꯫"),
        ("Do you know him?", "ꯅꯪ ꯃꯍꯥꯛꯄꯨ ꯈꯪꯕ꯭ꯔ?"),
        ("I know how to cook", "ꯑꯩ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯕ ꯈꯪꯏ꯫"),
        ("He knows Manipuri", "ꯃꯍꯥꯛ ꯃꯩꯇꯩꯂꯣꯟ ꯈꯪꯏ꯫"),
        ("She knows where he went", "ꯃꯍꯥꯛ ꯀꯗꯥꯏꯗ ꯆꯠꯂꯦ ꯃꯗꯨ ꯈꯪꯏ꯫"),
        ("I didn't know that", "ꯑꯩ ꯃꯗꯨ ꯈꯪꯈꯔꯗꯦ꯫"),
        ("He didn't know the truth", "ꯃꯍꯥꯛ ꯑꯆꯨꯝꯕ ꯈꯪꯈꯔꯗꯦ꯫"),
        ("Do you know this place?", "ꯅꯪ ꯃꯐꯝ ꯑꯁꯤ ꯈꯪꯕ꯭ꯔ?"),
        ("I know his name", "ꯑꯩ ꯃꯍꯥꯛꯀꯤ ꯃꯤꯡ ꯈꯪꯏ꯫"),
        ("She knows how to drive", "ꯃꯍꯥꯛ ꯒꯥꯔꯤ ꯊꯧꯕ ꯈꯪꯏ꯫"),
        ("They know each other", "ꯃꯈꯣꯏ ꯑꯃꯃ ꯈꯪꯅꯏ꯫"),
        ("I will know tomorrow", "ꯑꯩ ꯍꯌꯦꯡ ꯈꯪꯒꯅꯤ꯫"),
        ("Nobody knows the answer", "ꯀꯅꯃꯛ ꯄꯥꯑꯣꯈꯨꯝ ꯈꯪꯗꯦ꯫"),
        ("I know you are right", "ꯅꯪ ꯑꯆꯨꯝꯕ ꯍꯥꯏꯔꯤ ꯃꯗꯨ ꯑꯩ ꯈꯪꯏ꯫"),
    ],
},

# ━━━ 557: Let / Shall we ━━━
557: {
    "heading": "\"Let\" / \"Shall we\" examples",
    "rows": [
        ("Let's go", "ꯆꯠꯂꯁꯤ꯫"),
        ("Let's eat", "ꯆꯥꯂꯁꯤ꯫"),
        ("Let's play", "ꯁꯥꯂꯁꯤ꯫"),
        ("Let him come", "ꯃꯍꯥꯛꯄꯨ ꯂꯥꯀꯎ꯫"),
        ("Let her speak", "ꯃꯍꯥꯛꯄꯨ ꯉꯥꯡꯍꯜꯂꯨ꯫"),
        ("Let me try", "ꯑꯩꯕꯨ ꯍꯣꯠꯅꯍꯜꯂꯨ꯫"),
        ("Shall we go?", "ꯑꯩꯈꯣꯏ ꯆꯠꯀꯗ꯭ꯔ?"),
        ("Shall we eat?", "ꯑꯩꯈꯣꯏ ꯆꯥꯀꯗ꯭ꯔ?"),
        ("Let's read together", "ꯄꯨꯟꯁꯤ ꯄꯂꯁꯤ꯫"),
        ("Let them play", "ꯃꯈꯣꯏꯕꯨ ꯁꯥꯍꯜꯂꯨ꯫"),
        ("Let's go home", "ꯌꯨꯝꯗ ꯆꯠꯂꯁꯤ꯫"),
        ("Let me sleep", "ꯑꯩꯕꯨ ꯇꯨꯝꯍꯜꯂꯨ꯫"),
        ("Shall we watch a movie?", "ꯑꯩꯈꯣꯏ ꯐꯤꯜꯝ ꯌꯦꯡꯀꯗ꯭ꯔ?"),
        ("Let's meet tomorrow", "ꯍꯌꯦꯡ ꯎꯅꯅꯁꯤ꯫"),
        ("Let's cook together", "ꯄꯨꯟꯁꯤ ꯁꯥꯂꯁꯤ꯫"),
        ("Shall we start?", "ꯑꯩꯈꯣꯏ ꯍꯧꯀꯗ꯭ꯔ?"),
        ("Let's learn Meitei", "ꯃꯩꯇꯩꯂꯣꯟ ꯇꯝꯂꯁꯤ꯫"),
    ],
},

# ━━━ 558: Which-That / What-That ━━━
558: {
    "heading": "Which-That / What-That examples",
    "rows": [
        ("The book that I read", "ꯑꯩ ꯄꯈꯔꯕ ꯂꯥꯏꯔꯤꯛ ꯑꯗꯨ"),
        ("The man who came yesterday", "ꯉꯔꯪ ꯂꯥꯛꯂꯕ ꯅꯨꯄ ꯑꯗꯨ"),
        ("The food that she cooked", "ꯃꯍꯥꯛ ꯁꯥꯈꯔꯕ ꯆꯤꯟꯖꯥꯛ ꯑꯗꯨ"),
        ("The place where he lives", "ꯃꯍꯥꯛ ꯂꯩꯕ ꯃꯐꯝ ꯑꯗꯨ"),
        ("What he said is true", "ꯃꯍꯥꯛ ꯍꯥꯏꯈꯔꯕ ꯑꯗꯨ ꯑꯆꯨꯝꯕꯅꯤ꯫"),
        ("The song that she sang", "ꯃꯍꯥꯛ ꯁꯀꯈꯔꯕ ꯏꯁꯩ ꯑꯗꯨ"),
        ("The teacher who teaches us", "ꯑꯩꯈꯣꯏꯕꯨ ꯇꯝꯍꯟꯕ ꯑꯣꯖꯥ ꯑꯗꯨ"),
        ("What I want is peace", "ꯑꯩ ꯄꯝꯕ ꯑꯗꯨ ꯅꯤꯡꯊꯤꯖꯅꯤ꯫"),
        ("The dress that she bought", "ꯃꯍꯥꯛ ꯂꯩꯈꯔꯕ ꯐꯤ ꯑꯗꯨ"),
        ("The house that he built", "ꯃꯍꯥꯛ ꯁꯥꯈꯔꯕ ꯌꯨꯝ ꯑꯗꯨ"),
        ("What you said is wrong", "ꯅꯪ ꯍꯥꯏꯈꯔꯕ ꯑꯗꯨ ꯑꯆꯨꯝꯕ ꯅꯠꯇꯦ꯫"),
        ("The child who cried", "ꯀꯞꯈꯔꯕ ꯑꯅꯧꯕ ꯑꯗꯨ"),
        ("The water that I drank", "ꯑꯩ ꯊꯛꯈꯔꯕ ꯏꯁꯤꯡ ꯑꯗꯨ"),
        ("That which is good is rare", "ꯐꯕ ꯑꯗꯨ ꯌꯥꯝꯅ ꯈꯪꯕ ꯐꯥꯑꯣꯏꯗꯦ꯫"),
        ("The movie that we saw", "ꯑꯩꯈꯣꯏ ꯌꯦꯡꯈꯔꯕ ꯐꯤꯜꯝ ꯑꯗꯨ"),
        ("What happened was unexpected", "ꯑꯣꯏꯈꯔꯕ ꯑꯗꯨ ꯈꯪꯈꯔꯗꯕꯅꯤ꯫"),
        ("The friend who helped me", "ꯑꯩꯕꯨ ꯃꯇꯦꯡ ꯄꯥꯡꯈꯔꯕ ꯃꯔꯨꯞ ꯑꯗꯨ"),
    ],
},

# ━━━ 559: Formal instructions ━━━
559: {
    "heading": "Formal instruction examples",
    "rows": [
        ("Please sit down", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯐꯝꯕꯤꯌꯨ꯫"),
        ("Please write your name", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯅꯪꯒꯤ ꯃꯤꯡ ꯏꯕꯤꯌꯨ꯫"),
        ("Please read this", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯃꯁꯤ ꯄꯕꯤꯌꯨ꯫"),
        ("Please come in", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯂꯥꯀꯄꯤꯌꯨ꯫"),
        ("Please open your book", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯅꯪꯒꯤ ꯂꯥꯏꯔꯤꯛ ꯍꯪꯗꯣꯛꯕꯤꯌꯨ꯫"),
        ("Please close the door", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯊꯣꯡ ꯊꯤꯡꯕꯤꯌꯨ꯫"),
        ("Please listen carefully", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯆꯦꯛꯁꯤꯟꯅ ꯇꯕꯤꯌꯨ꯫"),
        ("Please speak louder", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯈꯣꯡꯖꯦꯜ ꯈꯣꯡꯖꯦꯜ ꯉꯥꯡꯕꯤꯌꯨ꯫"),
        ("Please wait a moment", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯑꯃꯨꯛꯇ ꯉꯥꯏꯕꯤꯌꯨ꯫"),
        ("Please fill this form", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯐꯣꯔꯝ ꯑꯁꯤ ꯊꯥꯕꯤꯌꯨ꯫"),
        ("Please stand in line", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯂꯥꯏꯟꯗ ꯂꯦꯞꯕꯤꯌꯨ꯫"),
        ("Please show your ID", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯅꯪꯒꯤ ꯑꯥꯏꯗꯤ ꯎꯠꯕꯤꯌꯨ꯫"),
        ("Please turn off your phone", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯅꯪꯒꯤ ꯐꯣꯟ ꯊꯤꯡꯕꯤꯌꯨ꯫"),
        ("Please take your seat", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯅꯪꯒꯤ ꯃꯐꯝꯗ ꯐꯝꯕꯤꯌꯨ꯫"),
        ("Please repeat after me", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯑꯩꯒꯤ ꯃꯇꯨꯡꯏꯟꯅ ꯍꯥꯏꯕꯤꯌꯨ꯫"),
        ("Please be quiet", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯀꯥꯡꯂꯧꯟꯕꯤꯌꯨ꯫"),
        ("Please answer the question", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯋꯥꯍꯪ ꯑꯗꯨ ꯄꯥꯑꯣꯈꯨꯝ ꯄꯤꯕꯤꯌꯨ꯫"),
    ],
},

# ━━━ 560: To Like ━━━
560: {
    "heading": "\"To like\" examples",
    "rows": [
        ("I like this", "ꯑꯩ ꯃꯁꯤ ꯄꯝꯖꯩ꯫"),
        ("He likes Manipur", "ꯃꯍꯥꯛ ꯃꯅꯤꯄꯨꯔ ꯄꯝꯖꯩ꯫"),
        ("She likes flowers", "ꯃꯍꯥꯛ ꯂꯩ ꯄꯝꯖꯩ꯫"),
        ("I like tea", "ꯑꯩ ꯆꯥ ꯄꯝꯖꯩ꯫"),
        ("We like this food", "ꯑꯩꯈꯣꯏ ꯆꯤꯟꯖꯥꯛ ꯑꯁꯤ ꯄꯝꯖꯩ꯫"),
        ("They like football", "ꯃꯈꯣꯏ ꯐꯨꯠꯕꯣꯜ ꯄꯝꯖꯩ꯫"),
        ("I don't like this", "ꯑꯩ ꯃꯁꯤ ꯄꯝꯗꯦ꯫"),
        ("He doesn't like tea", "ꯃꯍꯥꯛ ꯆꯥ ꯄꯝꯗꯦ꯫"),
        ("Do you like Manipuri food?", "ꯅꯪ ꯃꯅꯤꯄꯨꯔꯤ ꯆꯤꯟꯖꯥꯛ ꯄꯝꯖꯩꯕ꯭ꯔ?"),
        ("I like reading books", "ꯑꯩ ꯂꯥꯏꯔꯤꯛ ꯄꯕ ꯄꯝꯖꯩ꯫"),
        ("She likes singing songs", "ꯃꯍꯥꯛ ꯏꯁꯩ ꯁꯀꯕ ꯄꯝꯖꯩ꯫"),
        ("He liked the movie", "ꯃꯍꯥꯛ ꯐꯤꯜꯝ ꯑꯗꯨ ꯄꯝꯖꯩꯈꯔꯦ꯫"),
        ("I liked the food", "ꯑꯩ ꯆꯤꯟꯖꯥꯛ ꯑꯗꯨ ꯄꯝꯖꯩꯈꯔꯦ꯫"),
        ("What do you like?", "ꯅꯪ ꯀꯔꯤ ꯄꯝꯖꯩꯕꯒꯦ?"),
        ("I like my mother's cooking", "ꯑꯩ ꯑꯩꯒꯤ ꯏꯃꯥꯒꯤ ꯆꯤꯟꯖꯥꯛ ꯄꯝꯖꯩ꯫"),
        ("We like this place", "ꯑꯩꯈꯣꯏ ꯃꯐꯝ ꯑꯁꯤ ꯄꯝꯖꯩ꯫"),
        ("She likes to dance", "ꯃꯍꯥꯛ ꯖꯒꯣꯏ ꯁꯥꯕ ꯄꯝꯖꯩ꯫"),
    ],
},

# ━━━ 561: Would ━━━
561: {
    "heading": "\"Would\" examples",
    "rows": [
        ("I would go", "ꯑꯩ ꯆꯠꯅꯤꯡꯉꯩ꯫"),
        ("He would come", "ꯃꯍꯥꯛ ꯂꯥꯛꯅꯤꯡꯉꯩ꯫"),
        ("She would eat", "ꯃꯍꯥꯛ ꯆꯥꯅꯤꯡꯉꯩ꯫"),
        ("I would like tea", "ꯑꯩ ꯆꯥ ꯑꯃ ꯄꯝꯅꯤꯡꯉꯩ꯫"),
        ("He would help if he could", "ꯃꯍꯥꯛ ꯉꯝꯂꯕꯗꯤ ꯃꯇꯦꯡ ꯄꯥꯡꯅꯤꯡꯉꯩ꯫"),
        ("Would you come with me?", "ꯅꯪ ꯑꯩꯒ ꯂꯥꯛꯅꯤꯡꯉꯩꯕ꯭ꯔ?"),
        ("I would not do that", "ꯑꯩ ꯃꯗꯨ ꯇꯧꯅꯤꯡꯉꯩꯗꯦ꯫"),
        ("She would cook if asked", "ꯍꯥꯏꯂꯕꯗꯤ ꯃꯍꯥꯛ ꯁꯥꯅꯤꯡꯉꯩ꯫"),
        ("Would you like to join?", "ꯅꯪ ꯁꯔꯨꯛ ꯌꯥꯅꯤꯡꯉꯩꯕ꯭ꯔ?"),
        ("I would have gone", "ꯑꯩ ꯆꯠꯅꯤꯡꯉꯩꯔꯝꯃꯤ꯫"),
        ("He would have helped", "ꯃꯍꯥꯛ ꯃꯇꯦꯡ ꯄꯥꯡꯅꯤꯡꯉꯩꯔꯝꯃꯤ꯫"),
        ("She would sing at parties", "ꯃꯍꯥꯛ ꯄꯥꯔꯇꯤꯗ ꯏꯁꯩ ꯁꯀꯅꯤꯡꯉꯩ꯫"),
        ("Would you mind closing the door?", "ꯊꯣꯡ ꯊꯤꯡꯕ ꯉꯝꯒꯗ꯭ꯔ?"),
        ("I would buy if I had money", "ꯄꯥꯏꯁꯥ ꯂꯩꯔꯕꯗꯤ ꯑꯩ ꯂꯩꯅꯤꯡꯉꯩ꯫"),
        ("She would be happy", "ꯃꯍꯥꯛ ꯅꯨꯡꯉꯥꯏꯅꯤꯡꯉꯩ꯫"),
        ("He would always come early", "ꯃꯍꯥꯛ ꯃꯇꯝ ꯄꯨꯝꯕꯗ ꯊꯨꯅ ꯂꯥꯛꯅꯤꯡꯉꯩ꯫"),
        ("Would you like more water?", "ꯅꯪ ꯍꯦꯟꯅ ꯏꯁꯤꯡ ꯄꯝꯅꯤꯡꯉꯩꯕ꯭ꯔ?"),
    ],
},

# ━━━ 562: To Understand / To come to know ━━━
562: {
    "heading": "\"Understand\" / \"come to know\" examples",
    "rows": [
        ("I understand", "ꯑꯩ ꯈꯪꯏ꯫"),
        ("I don't understand", "ꯑꯩ ꯈꯪꯗꯦ꯫"),
        ("He understood the lesson", "ꯃꯍꯥꯛ ꯂꯦꯁꯟ ꯑꯗꯨ ꯈꯪꯈꯔꯦ꯫"),
        ("She came to know the truth", "ꯃꯍꯥꯛ ꯑꯆꯨꯝꯕ ꯈꯪꯂꯦ꯫"),
        ("Do you understand?", "ꯅꯪ ꯈꯪꯕ꯭ꯔ?"),
        ("I didn't understand", "ꯑꯩ ꯈꯪꯈꯔꯗꯦ꯫"),
        ("He will understand later", "ꯃꯍꯥꯛ ꯃꯇꯨꯡꯗ ꯈꯪꯒꯅꯤ꯫"),
        ("She came to know about it", "ꯃꯍꯥꯛ ꯃꯗꯨꯒꯤ ꯃꯇꯥꯡꯗ ꯈꯪꯂꯦ꯫"),
        ("Please try to understand", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯈꯪꯅꯕ ꯍꯣꯠꯅꯕꯤꯌꯨ꯫"),
        ("I came to know yesterday", "ꯑꯩ ꯉꯔꯪ ꯈꯪꯂꯦ꯫"),
        ("We understand Meitei", "ꯑꯩꯈꯣꯏ ꯃꯩꯇꯩꯂꯣꯟ ꯈꯪꯏ꯫"),
        ("He doesn't understand English", "ꯃꯍꯥꯛ ꯏꯪꯂꯤꯁ ꯈꯪꯗꯦ꯫"),
        ("She understood everything", "ꯃꯍꯥꯛ ꯄꯨꯝꯅꯃꯛ ꯈꯪꯈꯔꯦ꯫"),
        ("I will come to know soon", "ꯑꯩ ꯌꯥꯝꯅ ꯊꯨꯅ ꯈꯪꯒꯅꯤ꯫"),
        ("Please make me understand", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯑꯩꯕꯨ ꯈꯪꯍꯜꯕꯤꯌꯨ꯫"),
        ("I understand what you said", "ꯅꯪ ꯍꯥꯏꯈꯔꯕ ꯑꯗꯨ ꯑꯩ ꯈꯪꯏ꯫"),
        ("Nobody understood the question", "ꯀꯅꯃꯛ ꯋꯥꯍꯪ ꯑꯗꯨ ꯈꯪꯈꯔꯗꯦ꯫"),
    ],
},

# ━━━ 563: Question tags ━━━
563: {
    "heading": "Question tag examples",
    "rows": [
        ("He came, didn't he?", "ꯃꯍꯥꯛ ꯂꯥꯛꯂꯦ, ꯅꯠꯇ꯭ꯔ?"),
        ("She is beautiful, isn't she?", "ꯃꯍꯥꯛ ꯐꯖꯩ, ꯅꯠꯇ꯭ꯔ?"),
        ("You are coming, right?", "ꯅꯪ ꯂꯥꯛꯔꯤ, ꯅꯠꯇ꯭ꯔ?"),
        ("This is good, isn't it?", "ꯃꯁꯤ ꯐꯖꯩ, ꯅꯠꯇ꯭ꯔ?"),
        ("They went, didn't they?", "ꯃꯈꯣꯏ ꯆꯠꯂꯦ, ꯅꯠꯇ꯭ꯔ?"),
        ("He can swim, can't he?", "ꯃꯍꯥꯛ ꯂꯨꯝꯕ ꯉꯝꯃꯤ, ꯅꯠꯇ꯭ꯔ?"),
        ("She will come, won't she?", "ꯃꯍꯥꯛ ꯂꯥꯛꯀꯅꯤ, ꯅꯠꯇ꯭ꯔ?"),
        ("You know him, don't you?", "ꯅꯪ ꯃꯍꯥꯛꯄꯨ ꯈꯪꯏ, ꯅꯠꯇ꯭ꯔ?"),
        ("It rained, didn't it?", "ꯅꯣꯡ ꯇꯥꯛꯂꯦ, ꯅꯠꯇ꯭ꯔ?"),
        ("We won, didn't we?", "ꯑꯩꯈꯣꯏ ꯃꯥꯏꯄꯥꯛꯂꯦ, ꯅꯠꯇ꯭ꯔ?"),
        ("He is a teacher, isn't he?", "ꯃꯍꯥꯛ ꯑꯣꯖꯥꯅꯤ, ꯅꯠꯇ꯭ꯔ?"),
        ("She cooks well, doesn't she?", "ꯃꯍꯥꯛ ꯐꯖꯅ ꯁꯥꯏ, ꯅꯠꯇ꯭ꯔ?"),
        ("This food is tasty, isn't it?", "ꯆꯤꯟꯖꯥꯛ ꯑꯁꯤ ꯅꯨꯡꯉꯥꯏ, ꯅꯠꯇ꯭ꯔ?"),
        ("He didn't come, did he?", "ꯃꯍꯥꯛ ꯂꯥꯛꯈꯔꯗꯦ, ꯂꯥꯛꯂꯕ꯭ꯔ?"),
        ("You like tea, don't you?", "ꯅꯪ ꯆꯥ ꯄꯝꯖꯩ, ꯅꯠꯇ꯭ꯔ?"),
        ("She isn't coming, is she?", "ꯃꯍꯥꯛ ꯂꯥꯛꯇꯦ, ꯂꯥꯛꯔꯤꯕ꯭ꯔ?"),
        ("It is hot today, isn't it?", "ꯉꯁꯤ ꯑꯉꯥꯑꯣꯏ, ꯅꯠꯇ꯭ꯔ?"),
    ],
},

# ━━━ 564: To Remember ━━━
564: {
    "heading": "\"To remember\" examples",
    "rows": [
        ("I remember", "ꯑꯩ ꯅꯤꯡꯁꯤꯡꯏ꯫"),
        ("I don't remember", "ꯑꯩ ꯅꯤꯡꯁꯤꯡꯗꯦ꯫"),
        ("He remembers my name", "ꯃꯍꯥꯛ ꯑꯩꯒꯤ ꯃꯤꯡ ꯅꯤꯡꯁꯤꯡꯏ꯫"),
        ("She doesn't remember the way", "ꯃꯍꯥꯛ ꯂꯝꯕꯤ ꯅꯤꯡꯁꯤꯡꯗꯦ꯫"),
        ("Do you remember me?", "ꯅꯪ ꯑꯩꯕꯨ ꯅꯤꯡꯁꯤꯡꯕ꯭ꯔ?"),
        ("I remembered yesterday", "ꯑꯩ ꯉꯔꯪ ꯅꯤꯡꯁꯤꯡꯈꯔꯦ꯫"),
        ("He will remember", "ꯃꯍꯥꯛ ꯅꯤꯡꯁꯤꯡꯒꯅꯤ꯫"),
        ("Please remember this", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯃꯁꯤ ꯅꯤꯡꯁꯤꯡꯕꯤꯌꯨ꯫"),
        ("I can't remember his name", "ꯑꯩ ꯃꯍꯥꯛꯀꯤ ꯃꯤꯡ ꯅꯤꯡꯁꯤꯡꯗꯦ꯫"),
        ("She remembered the song", "ꯃꯍꯥꯛ ꯏꯁꯩ ꯑꯗꯨ ꯅꯤꯡꯁꯤꯡꯈꯔꯦ꯫"),
        ("Remember to bring the book", "ꯂꯥꯏꯔꯤꯛ ꯄꯨꯔꯛꯕ ꯅꯤꯡꯁꯤꯡꯕꯤꯌꯨ꯫"),
        ("I always remember my mother", "ꯑꯩ ꯃꯇꯝ ꯄꯨꯝꯕꯗ ꯑꯩꯒꯤ ꯏꯃꯥꯕꯨ ꯅꯤꯡꯁꯤꯡꯏ꯫"),
        ("He forgot but then remembered", "ꯃꯍꯥꯛ ꯀꯞꯈꯔꯦ ꯑꯗꯨꯕꯨ ꯃꯇꯨꯡꯗ ꯅꯤꯡꯁꯤꯡꯈꯔꯦ꯫"),
        ("Do you remember this place?", "ꯅꯪ ꯃꯐꯝ ꯑꯁꯤ ꯅꯤꯡꯁꯤꯡꯕ꯭ꯔ?"),
        ("I will always remember you", "ꯑꯩ ꯃꯇꯝ ꯄꯨꯝꯕꯗ ꯅꯪꯕꯨ ꯅꯤꯡꯁꯤꯡꯒꯅꯤ꯫"),
        ("She can't remember anything", "ꯃꯍꯥꯛ ꯀꯔꯤꯁꯨ ꯅꯤꯡꯁꯤꯡꯗꯦ꯫"),
        ("Remember what I told you", "ꯑꯩ ꯍꯥꯏꯈꯔꯕ ꯑꯗꯨ ꯅꯤꯡꯁꯤꯡꯕꯤꯌꯨ꯫"),
    ],
},

# ━━━ 565: Want/Need + other verb ━━━
565: {
    "heading": "\"Want/Need\" + verb examples",
    "rows": [
        ("I want to eat", "ꯑꯩ ꯆꯥꯅꯤꯡꯉꯩ꯫"),
        ("He wants to go", "ꯃꯍꯥꯛ ꯆꯠꯅꯤꯡꯉꯩ꯫"),
        ("She wants to sleep", "ꯃꯍꯥꯛ ꯇꯨꯝꯅꯤꯡꯉꯩ꯫"),
        ("I want to read a book", "ꯑꯩ ꯂꯥꯏꯔꯤꯛ ꯄꯅꯤꯡꯉꯩ꯫"),
        ("He wants to drink water", "ꯃꯍꯥꯛ ꯏꯁꯤꯡ ꯊꯛꯅꯤꯡꯉꯩ꯫"),
        ("She wants to sing", "ꯃꯍꯥꯛ ꯏꯁꯩ ꯁꯀꯅꯤꯡꯉꯩ꯫"),
        ("I need to work", "ꯑꯩ ꯊꯕꯛ ꯇꯧꯀꯗꯕꯅꯤ꯫"),
        ("He needs to study", "ꯃꯍꯥꯛ ꯇꯝꯀꯗꯕꯅꯤ꯫"),
        ("I don't want to go", "ꯑꯩ ꯆꯠꯄ ꯄꯝꯗꯦ꯫"),
        ("She doesn't want to eat", "ꯃꯍꯥꯛ ꯆꯥꯕ ꯄꯝꯗꯦ꯫"),
        ("Do you want to come?", "ꯅꯪ ꯂꯥꯛꯅꯤꯡꯉꯩꯕ꯭ꯔ?"),
        ("I want to learn Meitei", "ꯑꯩ ꯃꯩꯇꯩꯂꯣꯟ ꯇꯝꯅꯤꯡꯉꯩ꯫"),
        ("He wants to help you", "ꯃꯍꯥꯛ ꯅꯪꯕꯨ ꯃꯇꯦꯡ ꯄꯥꯡꯅꯤꯡꯉꯩ꯫"),
        ("She needs to rest", "ꯃꯍꯥꯛ ꯂꯣꯏꯅ ꯂꯩꯀꯗꯕꯅꯤ꯫"),
        ("I want to go home", "ꯑꯩ ꯌꯨꯝꯗ ꯆꯠꯅꯤꯡꯉꯩ꯫"),
        ("He needs to see a doctor", "ꯃꯍꯥꯛ ꯗꯣꯛꯇꯔ ꯎꯀꯗꯕꯅꯤ꯫"),
        ("We want to play", "ꯑꯩꯈꯣꯏ ꯁꯥꯅꯤꯡꯉꯩ꯫"),
    ],
},

# ━━━ 566: Want + other person ━━━
566: {
    "heading": "\"Want\" + another person examples",
    "rows": [
        ("I want him to come", "ꯑꯩ ꯃꯍꯥꯛꯄꯨ ꯂꯥꯛꯅꯤꯡꯉꯩ꯫"),
        ("I want her to eat", "ꯑꯩ ꯃꯍꯥꯛꯄꯨ ꯆꯥꯅꯤꯡꯉꯩ꯫"),
        ("He wants me to go", "ꯃꯍꯥꯛ ꯑꯩꯕꯨ ꯆꯠꯅꯤꯡꯉꯩ꯫"),
        ("She wants you to study", "ꯃꯍꯥꯛ ꯅꯪꯕꯨ ꯇꯝꯅꯤꯡꯉꯩ꯫"),
        ("I want them to play", "ꯑꯩ ꯃꯈꯣꯏꯕꯨ ꯁꯥꯅꯤꯡꯉꯩ꯫"),
        ("He wants her to cook", "ꯃꯍꯥꯛ ꯃꯍꯥꯛꯄꯨ ꯁꯥꯅꯤꯡꯉꯩ꯫"),
        ("I want you to help me", "ꯑꯩ ꯅꯪꯕꯨ ꯑꯩꯗ ꯃꯇꯦꯡ ꯄꯥꯡꯅꯤꯡꯉꯩ꯫"),
        ("She wants him to read", "ꯃꯍꯥꯛ ꯃꯍꯥꯛꯄꯨ ꯄꯅꯤꯡꯉꯩ꯫"),
        ("I want the child to sleep", "ꯑꯩ ꯑꯅꯧꯕꯕꯨ ꯇꯨꯝꯅꯤꯡꯉꯩ꯫"),
        ("He wants us to come", "ꯃꯍꯥꯛ ꯑꯩꯈꯣꯏꯕꯨ ꯂꯥꯛꯅꯤꯡꯉꯩ꯫"),
        ("Mother wants children to eat", "ꯏꯃꯥꯅ ꯑꯅꯧꯕꯁꯤꯡꯕꯨ ꯆꯥꯅꯤꯡꯉꯩ꯫"),
        ("Teacher wants us to read", "ꯑꯣꯖꯥꯅ ꯑꯩꯈꯣꯏꯕꯨ ꯄꯅꯤꯡꯉꯩ꯫"),
        ("I don't want him to go", "ꯑꯩ ꯃꯍꯥꯛꯄꯨ ꯆꯠꯅꯤꯡꯉꯩꯗꯦ꯫"),
        ("She doesn't want me to leave", "ꯃꯍꯥꯛ ꯑꯩꯕꯨ ꯆꯠꯅꯤꯡꯉꯩꯗꯦ꯫"),
        ("Do you want me to come?", "ꯅꯪ ꯑꯩꯕꯨ ꯂꯥꯛꯅꯤꯡꯉꯩꯕ꯭ꯔ?"),
        ("I want you to be happy", "ꯑꯩ ꯅꯪꯕꯨ ꯅꯨꯡꯉꯥꯏꯅꯤꯡꯉꯩ꯫"),
        ("Father wants son to study", "ꯏꯄꯥꯅ ꯃꯆꯥꯕꯨ ꯇꯝꯅꯤꯡꯉꯩ꯫"),
    ],
},

# ━━━ 567: Supposed to ━━━
567: {
    "heading": "\"Supposed to\" examples",
    "rows": [
        ("I am supposed to go", "ꯑꯩ ꯆꯠꯀꯗꯕꯅꯤ꯫"),
        ("He is supposed to come", "ꯃꯍꯥꯛ ꯂꯥꯛꯀꯗꯕꯅꯤ꯫"),
        ("She is supposed to cook", "ꯃꯍꯥꯛ ꯁꯥꯀꯗꯕꯅꯤ꯫"),
        ("We are supposed to study", "ꯑꯩꯈꯣꯏ ꯇꯝꯀꯗꯕꯅꯤ꯫"),
        ("They are supposed to come today", "ꯃꯈꯣꯏ ꯉꯁꯤ ꯂꯥꯛꯀꯗꯕꯅꯤ꯫"),
        ("He was supposed to call me", "ꯃꯍꯥꯛ ꯑꯩꯕꯨ ꯀꯧꯀꯗꯕꯅꯤ꯫"),
        ("She is supposed to write the letter", "ꯃꯍꯥꯛ ꯆꯤꯠꯊꯤ ꯏꯀꯗꯕꯅꯤ꯫"),
        ("You are supposed to finish this", "ꯅꯪ ꯃꯁꯤ ꯂꯣꯏꯁꯤꯜꯀꯗꯕꯅꯤ꯫"),
        ("I am supposed to bring food", "ꯑꯩ ꯆꯤꯟꯖꯥꯛ ꯄꯨꯀꯗꯕꯅꯤ꯫"),
        ("He is supposed to pay", "ꯃꯍꯥꯛ ꯄꯤꯀꯗꯕꯅꯤ꯫"),
        ("We were supposed to meet", "ꯑꯩꯈꯣꯏ ꯎꯅꯀꯗꯕꯅꯤ꯫"),
        ("She was supposed to come early", "ꯃꯍꯥꯛ ꯊꯨꯅ ꯂꯥꯛꯀꯗꯕꯅꯤ꯫"),
        ("He is not supposed to eat that", "ꯃꯍꯥꯛ ꯃꯗꯨ ꯆꯥꯔꯣꯏꯗꯕꯅꯤ꯫"),
        ("You are supposed to wait", "ꯅꯪ ꯉꯥꯏꯀꯗꯕꯅꯤ꯫"),
        ("I was supposed to help them", "ꯑꯩ ꯃꯈꯣꯏꯕꯨ ꯃꯇꯦꯡ ꯄꯥꯡꯀꯗꯕꯅꯤ꯫"),
        ("They are supposed to leave now", "ꯃꯈꯣꯏ ꯍꯧꯖꯤꯛ ꯆꯠꯀꯗꯕꯅꯤ꯫"),
        ("He is supposed to teach us", "ꯃꯍꯥꯛ ꯑꯩꯈꯣꯏꯕꯨ ꯇꯝꯍꯟꯀꯗꯕꯅꯤ꯫"),
    ],
},

# ━━━ 568: To Like + verb ━━━
568: {
    "heading": "\"Like\" + verb examples",
    "rows": [
        ("I like to eat", "ꯑꯩ ꯆꯥꯕ ꯄꯝꯖꯩ꯫"),
        ("He likes to sing", "ꯃꯍꯥꯛ ꯏꯁꯩ ꯁꯀꯕ ꯄꯝꯖꯩ꯫"),
        ("She likes to dance", "ꯃꯍꯥꯛ ꯖꯒꯣꯏ ꯁꯥꯕ ꯄꯝꯖꯩ꯫"),
        ("I like to read books", "ꯑꯩ ꯂꯥꯏꯔꯤꯛ ꯄꯕ ꯄꯝꯖꯩ꯫"),
        ("He likes to play football", "ꯃꯍꯥꯛ ꯐꯨꯠꯕꯣꯜ ꯁꯥꯕ ꯄꯝꯖꯩ꯫"),
        ("She likes to cook", "ꯃꯍꯥꯛ ꯁꯥꯕ ꯄꯝꯖꯩ꯫"),
        ("I don't like to run", "ꯑꯩ ꯆꯦꯜꯕ ꯄꯝꯗꯦ꯫"),
        ("He doesn't like to study", "ꯃꯍꯥꯛ ꯇꯝꯕ ꯄꯝꯗꯦ꯫"),
        ("She likes to write poems", "ꯃꯍꯥꯛ ꯁꯩꯔꯦꯡ ꯏꯕ ꯄꯝꯖꯩ꯫"),
        ("I like to walk in the evening", "ꯑꯩ ꯅꯨꯃꯤꯗꯪ ꯆꯠꯕ ꯄꯝꯖꯩ꯫"),
        ("He likes to swim", "ꯃꯍꯥꯛ ꯏꯁꯤꯡꯗ ꯂꯨꯝꯕ ꯄꯝꯖꯩ꯫"),
        ("She likes to watch movies", "ꯃꯍꯥꯛ ꯐꯤꯜꯝ ꯌꯦꯡꯕ ꯄꯝꯖꯩ꯫"),
        ("I like to sleep early", "ꯑꯩ ꯊꯨꯅ ꯇꯨꯝꯕ ꯄꯝꯖꯩ꯫"),
        ("He likes to drive", "ꯃꯍꯥꯛ ꯒꯥꯔꯤ ꯊꯧꯕ ꯄꯝꯖꯩ꯫"),
        ("Do you like to travel?", "ꯅꯪ ꯈꯣꯡꯆꯠ ꯇꯧꯕ ꯄꯝꯖꯩꯕ꯭ꯔ?"),
        ("They like to play together", "ꯃꯈꯣꯏ ꯄꯨꯟꯁꯤ ꯁꯥꯕ ꯄꯝꯖꯩ꯫"),
        ("I like to speak Meitei", "ꯑꯩ ꯃꯩꯇꯩꯂꯣꯟ ꯉꯥꯡꯕ ꯄꯝꯖꯩ꯫"),
    ],
},

# ━━━ 569: Verbs + preposition "To" + subject/object ━━━
569: {
    "heading": "Verb + \"To\" preposition examples",
    "rows": [
        ("I told him to come", "ꯑꯩꯅ ꯃꯍꯥꯛꯄꯨ ꯂꯥꯛꯂꯣ ꯍꯥꯏꯈꯔꯦ꯫"),
        ("She asked me to go", "ꯃꯍꯥꯛꯅ ꯑꯩꯕꯨ ꯆꯠꯂꯣ ꯍꯥꯏꯈꯔꯦ꯫"),
        ("He forced me to eat", "ꯃꯍꯥꯛꯅ ꯑꯩꯕꯨ ꯆꯥꯍꯜꯂꯦ꯫"),
        ("I helped him to study", "ꯑꯩꯅ ꯃꯍꯥꯛꯄꯨ ꯇꯝꯕꯗ ꯃꯇꯦꯡ ꯄꯥꯡꯈꯔꯦ꯫"),
        ("She taught me to cook", "ꯃꯍꯥꯛꯅ ꯑꯩꯕꯨ ꯁꯥꯕ ꯇꯝꯍꯟꯈꯔꯦ꯫"),
        ("He told her to wait", "ꯃꯍꯥꯛꯅ ꯃꯍꯥꯛꯄꯨ ꯉꯥꯏꯕꯤꯌꯨ ꯍꯥꯏꯈꯔꯦ꯫"),
        ("Mother told children to sleep", "ꯏꯃꯥꯅ ꯑꯅꯧꯕꯁꯤꯡꯕꯨ ꯇꯨꯝꯃꯨ ꯍꯥꯏꯈꯔꯦ꯫"),
        ("Teacher told us to read", "ꯑꯣꯖꯥꯅ ꯑꯩꯈꯣꯏꯕꯨ ꯄꯕꯤꯌꯨ ꯍꯥꯏꯈꯔꯦ꯫"),
        ("I asked him to write", "ꯑꯩꯅ ꯃꯍꯥꯛꯄꯨ ꯏꯌꯨ ꯍꯥꯏꯈꯔꯦ꯫"),
        ("She told me to sit", "ꯃꯍꯥꯛꯅ ꯑꯩꯕꯨ ꯐꯝꯃꯨ ꯍꯥꯏꯈꯔꯦ꯫"),
        ("He allowed me to go", "ꯃꯍꯥꯛꯅ ꯑꯩꯕꯨ ꯆꯠꯍꯜꯂꯦ꯫"),
        ("I invited him to come", "ꯑꯩꯅ ꯃꯍꯥꯛꯄꯨ ꯂꯥꯛꯂꯣ ꯀꯧꯈꯔꯦ꯫"),
        ("She reminded me to bring it", "ꯃꯍꯥꯛꯅ ꯑꯩꯕꯨ ꯃꯗꯨ ꯄꯨꯔꯛꯕ ꯅꯤꯡꯁꯤꯡꯍꯜꯂꯦ꯫"),
        ("Father told son to study", "ꯏꯄꯥꯅ ꯃꯆꯥꯕꯨ ꯇꯝꯂꯣ ꯍꯥꯏꯈꯔꯦ꯫"),
        ("Doctor told me to rest", "ꯗꯣꯛꯇꯔꯅ ꯑꯩꯕꯨ ꯂꯣꯏꯅ ꯂꯩꯌꯨ ꯍꯥꯏꯈꯔꯦ꯫"),
        ("I told them to be quiet", "ꯑꯩꯅ ꯃꯈꯣꯏꯕꯨ ꯀꯥꯡꯂꯧꯟꯕꯤꯌꯨ ꯍꯥꯏꯈꯔꯦ꯫"),
        ("He asked me to help", "ꯃꯍꯥꯛꯅ ꯑꯩꯕꯨ ꯃꯇꯦꯡ ꯄꯥꯡꯕꯤꯌꯨ ꯍꯥꯏꯈꯔꯦ꯫"),
    ],
},

# ━━━ 570: Short forms in spoken Meitei ━━━
570: {
    "heading": "Short/spoken form examples",
    "rows": [
        ("I am fine → Fine", "ꯑꯩ ꯅꯨꯉꯥꯏꯔꯤ → ꯅꯨꯉꯥꯏꯔꯤ"),
        ("What are you doing? (short)", "ꯀꯔꯤ ꯇꯧꯔꯤꯕꯒꯦ?"),
        ("Where are you going? (short)", "ꯀꯗꯣꯝꯗ ꯆꯠꯔꯤꯕꯒꯦ?"),
        ("Come here (casual)", "ꯑꯁꯤꯗ ꯂꯥꯀꯎ꯫"),
        ("Let's go (casual)", "ꯆꯠꯂꯁꯤ꯫"),
        ("No, no (emphatic)", "ꯅꯠꯇꯦ ꯅꯠꯇꯦ꯫"),
        ("OK / Yes (casual)", "ꯍꯣꯏ꯫"),
        ("That's enough", "ꯌꯥꯔꯦ꯫"),
        ("Don't want (blunt)", "ꯄꯝꯗꯦ꯫"),
        ("Don't know (casual)", "ꯈꯪꯗꯦ꯫"),
        ("Understand? (short)", "ꯈꯪꯕꯔ?"),
        ("Very good (casual)", "ꯌꯥꯝꯅ ꯐꯔꯦ꯫"),
        ("Nothing much", "ꯀꯦꯝ ꯂꯩꯇꯦ꯫"),
        ("Wait a bit", "ꯑꯃꯨꯛꯇ ꯉꯥꯏꯈꯣ꯫"),
        ("I'll come (short)", "ꯂꯥꯛꯀꯦ꯫"),
        ("Bye / I'm going", "ꯆꯠꯂꯨꯈꯤꯒꯦ꯫"),
        ("Really? (surprise)", "ꯑꯆꯨꯝꯕꯅꯣ?"),
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
        rows = []
        for eng, mayek in lesson["rows"]:
            rows.append([eng, mayek, m2r(mayek)])
        new_table = {
            "type": "table",
            "heading": lesson["heading"],
            "headers": ["English", "Manipuri", "Transliteration"],
            "speakCol": 1,
            "rows": rows,
        }
        # Keep ONLY tables, remove paragraphs/intro/content
        chapter["blocks"] = [new_table]
        chapter.pop("intro", None)
        chapter.pop("content", None)
        updated += 1
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sys.stdout.buffer.write(f"Updated {updated} pattern lessons (543-570) in data_meitei.json\n".encode("utf-8"))

if __name__ == "__main__":
    main()
