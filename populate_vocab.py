#!/usr/bin/env python3
"""Populate vocabulary lessons 597-619 (4.1-4.23) with topic-relevant word/sentence tables."""
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

# ━━━ 597: Body parts ━━━
597: {
    "heading": "Body parts in Meitei",
    "rows": [
        ("Head", "ꯀꯣꯛ"),
        ("Hair", "ꯁꯝ"),
        ("Forehead", "ꯂꯥꯏꯄꯥꯛ"),
        ("Face", "ꯃꯥꯏ"),
        ("Eye", "ꯃꯤꯠ"),
        ("Eyebrow", "ꯄꯥ"),
        ("Ear", "ꯅꯥꯀꯣꯡ"),
        ("Nose", "ꯅꯥꯇꯣꯟ"),
        ("Lips", "ꯆꯤꯟ"),
        ("Teeth", "ꯌꯥ"),
        ("Tongue", "ꯂꯩ"),
        ("Cheeks", "ꯈꯖꯥꯢ"),
        ("Neck", "ꯈꯧ"),
        ("Chest", "ꯊꯕꯥꯛ"),
        ("Belly / Stomach", "ꯄꯨꯛ"),
        ("Hand / Arm", "ꯈꯨꯠ"),
        ("Palm", "ꯈꯨꯕꯥꯛ"),
        ("Finger", "ꯈꯨꯠꯁꯥ"),
        ("Leg / Foot", "ꯈꯣꯡ"),
        ("Knee", "ꯈꯨ"),
        ("Sole of foot", "ꯈꯣꯡꯄꯥꯛ"),
        ("Bone", "ꯁꯔꯨ"),
        ("Skin", "ꯎꯟ"),
        ("Blood", "ꯏ"),
        ("Heart", "ꯊꯃꯣꯏ"),
        ("Body", "ꯍꯛꯆꯥꯡ"),
    ],
},

# ━━━ 598: Frequently used words – Misc ━━━
598: {
    "heading": "Frequently used words – Miscellaneous",
    "rows": [
        ("House", "ꯌꯨꯝ"),
        ("Room", "ꯀꯥ"),
        ("Door", "ꯊꯣꯡ"),
        ("Window", "ꯊꯣꯡꯅꯥꯎ"),
        ("Road", "ꯂꯝꯕꯤ"),
        ("Village", "ꯈꯨꯟ"),
        ("School", "ꯂꯥꯏꯔꯤꯛꯁꯡ"),
        ("Book", "ꯂꯥꯏꯔꯤꯛ"),
        ("Paper", "ꯆꯦ"),
        ("Fire", "ꯃꯩ"),
        ("Water", "ꯏꯁꯤꯡ"),
        ("Air", "ꯅꯨꯡꯁꯤꯠ"),
        ("Sky", "ꯑꯇꯤꯌꯥ"),
        ("Sun", "ꯅꯨꯃꯤꯠ"),
        ("Moon", "ꯊꯥ"),
        ("Rain", "ꯅꯣꯡ"),
        ("Cloud", "ꯂꯥꯏꯆꯤꯜ"),
        ("Mountain", "ꯆꯤꯡ"),
        ("River", "ꯇꯨꯔꯦꯟ"),
        ("Stone", "ꯅꯨꯡ"),
    ],
},

# ━━━ 599: Relations ━━━
599: {
    "heading": "Family relations in Meitei",
    "rows": [
        ("Father", "ꯃꯄꯥ"),
        ("Mother", "ꯃꯃꯥ"),
        ("Son", "ꯃꯆꯥ ꯅꯨꯄꯥ"),
        ("Daughter", "ꯃꯆꯥ ꯅꯨꯄꯤ"),
        ("Elder brother", "ꯃꯌꯥꯝꯕ"),
        ("Younger brother", "ꯃꯅꯥꯎ ꯅꯨꯄꯥ"),
        ("Elder sister", "ꯃꯆꯦ"),
        ("Younger sister", "ꯃꯆꯜ"),
        ("Grandfather", "ꯃꯄꯨ"),
        ("Grandmother", "ꯃꯕꯣꯛ"),
        ("Uncle", "ꯃꯄꯟ"),
        ("Aunt (father's sister)", "ꯃꯅꯦ"),
        ("Aunt (mother's sister)", "ꯃꯗꯣꯝꯆꯥ"),
        ("Husband", "ꯃꯋꯥ"),
        ("Wife", "ꯃꯇꯨ"),
        ("Nephew", "ꯃꯃꯥꯛ"),
        ("Niece", "ꯃꯃꯧ"),
        ("Father-in-law", "ꯃꯀꯨ"),
        ("Mother-in-law", "ꯃꯅꯦꯝ"),
        ("My father", "ꯏꯄꯥ"),
        ("My mother", "ꯏꯃꯥ"),
        ("My elder brother", "ꯏꯌꯥꯝꯕ"),
        ("My elder sister", "ꯏꯆꯦ"),
    ],
},

# ━━━ 600: Numbers Part 1 (1-20) ━━━
600: {
    "heading": "Numbers in Meitei – Part 1",
    "rows": [
        ("1 – One", "꯱ – ꯑꯃ"),
        ("2 – Two", "꯲ – ꯑꯅꯤ"),
        ("3 – Three", "꯳ – ꯑꯍꯨꯝ"),
        ("4 – Four", "꯴ – ꯃꯔꯤ"),
        ("5 – Five", "꯵ – ꯃꯉꯥ"),
        ("6 – Six", "꯶ – ꯇꯔꯨꯛ"),
        ("7 – Seven", "꯷ – ꯇꯔꯦꯠ"),
        ("8 – Eight", "꯸ – ꯅꯤꯄꯥꯜ"),
        ("9 – Nine", "꯹ – ꯃꯥꯄꯜ"),
        ("10 – Ten", "꯱꯰ – ꯇꯔꯥ"),
        ("11 – Eleven", "꯱꯱ – ꯇꯔꯥ ꯃꯥꯊꯣꯢ"),
        ("12 – Twelve", "꯱꯲ – ꯇꯔꯥ ꯅꯤꯊꯣꯢ"),
        ("13 – Thirteen", "꯱꯳ – ꯇꯔꯥ ꯍꯨꯝꯗꯣꯢ"),
        ("14 – Fourteen", "꯱꯴ – ꯇꯔꯥ ꯃꯔꯤ"),
        ("15 – Fifteen", "꯱꯵ – ꯇꯔꯥ ꯃꯉꯥ"),
        ("16 – Sixteen", "꯱꯶ – ꯇꯔꯥ ꯇꯔꯨꯛ"),
        ("17 – Seventeen", "꯱꯷ – ꯇꯔꯥ ꯇꯔꯦꯠ"),
        ("18 – Eighteen", "꯱꯸ – ꯇꯔꯥ ꯅꯤꯄꯥꯜ"),
        ("19 – Nineteen", "꯱꯹ – ꯇꯔꯥ ꯃꯥꯄꯜ"),
        ("20 – Twenty", "꯲꯰ – ꯀꯨꯜ"),
    ],
},

# ━━━ 601: Numbers Part 2 (20+) ━━━
601: {
    "heading": "Numbers in Meitei – Part 2",
    "rows": [
        ("21 – Twenty-one", "꯲꯱ – ꯀꯨꯟ ꯃꯥꯊꯣꯢ"),
        ("22 – Twenty-two", "꯲꯲ – ꯀꯨꯟ ꯅꯤꯊꯣꯢ"),
        ("23 – Twenty-three", "꯲꯳ – ꯀꯨꯟ ꯍꯨꯝꯗꯣꯢ"),
        ("30 – Thirty", "꯳꯰ – ꯀꯨꯟꯊ꯭ꯔꯥ"),
        ("40 – Forty", "꯴꯰ – ꯅꯤꯝꯐꯨ"),
        ("50 – Fifty", "꯵꯰ – ꯌꯥꯡꯈꯩ"),
        ("60 – Sixty", "꯶꯰ – ꯍꯨꯝꯐꯨ"),
        ("70 – Seventy", "꯷꯰ – ꯍꯨꯝꯗ꯭ꯔꯥ"),
        ("80 – Eighty", "꯸꯰ – ꯃꯔꯤꯐꯨ"),
        ("90 – Ninety", "꯹꯰ – ꯃꯧꯗ꯭ꯔꯥ"),
        ("100 – Hundred", "꯱꯰꯰ – ꯆꯥ ꯑꯃ"),
        ("200 – Two hundred", "꯲꯰꯰ – ꯆꯥ ꯑꯅꯤ"),
        ("300 – Three hundred", "꯳꯰꯰ – ꯆꯥ ꯑꯍꯨꯝ"),
        ("1000 – Thousand", "꯱꯰꯰꯰ – ꯂꯤꯁꯤꯡ ꯑꯃ"),
        ("2000 – Two thousand", "꯲꯰꯰꯰ – ꯂꯤꯁꯤꯡ ꯑꯅꯤ"),
        ("10000 – Ten thousand", "꯱꯰꯰꯰꯰ – ꯂꯤꯁꯤꯡ ꯇꯔꯥ"),
        ("100000 – Lakh", "꯱꯰꯰꯰꯰꯰ – ꯂꯤꯆꯥ ꯑꯃ"),
    ],
},

# ━━━ 602: Fractional, sequence, percentage ━━━
602: {
    "heading": "Fractional numbers, sequence & percentage",
    "rows": [
        ("Quarter", "ꯃꯁꯨꯡ"),
        ("Half", "ꯇꯡꯈꯥꯏ"),
        ("The whole", "ꯃꯄꯨꯝ"),
        ("First", "ꯑꯍꯥꯅꯕ"),
        ("Second", "ꯑꯅꯤꯁꯨꯕ"),
        ("Third", "ꯑꯍꯨꯝꯁꯨꯕ"),
        ("Fourth", "ꯃꯔꯤꯁꯨꯕ"),
        ("Fifth", "ꯃꯉꯥꯁꯨꯕ"),
        ("Sixth", "ꯇꯔꯨꯛꯁꯨꯕ"),
        ("Seventh", "ꯇꯔꯦꯠꯁꯨꯕ"),
        ("Eighth", "ꯅꯤꯄꯥꯜꯁꯨꯕ"),
        ("Ninth", "ꯃꯥꯄꯜꯁꯨꯕ"),
        ("Tenth", "ꯇꯔꯥꯁꯨꯕ"),
        ("One and a half", "ꯑꯃ ꯇꯡꯈꯥꯏ"),
        ("Two and a half", "ꯑꯅꯤ ꯇꯡꯈꯥꯏ"),
        ("Ten percent", "ꯆꯥꯗ ꯇꯔꯥ"),
        ("Fifty percent", "ꯆꯥꯗ ꯌꯥꯡꯈꯩ"),
        ("Hundred percent", "ꯆꯥꯗ ꯆꯥ ꯑꯃ"),
    ],
},

# ━━━ 603: Frequently used verbs Part 1 ━━━
603: {
    "heading": "Frequently used verbs – Part 1",
    "rows": [
        ("To eat", "ꯆꯥꯕ"),
        ("To drink", "ꯊꯥꯕ"),
        ("To go", "ꯆꯠꯄ"),
        ("To come", "ꯂꯥꯛꯄ"),
        ("To see / look", "ꯌꯦꯡꯕ"),
        ("To hear / listen", "ꯇꯥꯕ"),
        ("To speak / talk", "ꯋꯥ ꯉꯥꯡꯕ"),
        ("To write", "ꯏꯕ"),
        ("To read", "ꯄꯥꯕ"),
        ("To sleep", "ꯇꯨꯝꯕ"),
        ("To sit", "ꯐꯝꯕ"),
        ("To stand", "ꯂꯦꯞꯄ"),
        ("To run", "ꯆꯦꯟꯕ"),
        ("To walk", "ꯆꯠꯊꯣꯛꯄ"),
        ("To give", "ꯄꯤꯕ"),
        ("To take", "ꯂꯧꯕ"),
        ("To do / make", "ꯇꯧꯕ"),
        ("To know", "ꯈꯉꯕ"),
    ],
},

# ━━━ 604: Frequently used verbs Part 2 ━━━
604: {
    "heading": "Frequently used verbs – Part 2",
    "rows": [
        ("To cry", "ꯀꯞꯄ"),
        ("To laugh / smile", "ꯅꯣꯛꯄ"),
        ("To sing", "ꯏꯁꯩ ꯁꯥꯕ"),
        ("To dance", "ꯖꯥꯒꯣꯏ ꯁꯥꯕ"),
        ("To cook", "ꯁꯥꯕ"),
        ("To wash", "ꯀꯥꯡꯕ"),
        ("To buy", "ꯂꯩꯕ"),
        ("To sell", "ꯌꯣꯟꯕ"),
        ("To open", "ꯍꯥꯡꯕ"),
        ("To close", "ꯊꯤꯡꯕ"),
        ("To ask", "ꯍꯪꯕ"),
        ("To answer", "ꯄꯥꯎꯈꯨꯝ ꯄꯤꯕ"),
        ("To fly", "ꯄꯥꯝꯕ"),
        ("To swim", "ꯋꯥꯡꯕ"),
        ("To play", "ꯁꯥꯅꯕ"),
        ("To work", "ꯊꯧꯔꯝ ꯇꯧꯕ"),
        ("To bring", "ꯄꯨꯔꯛꯄ"),
        ("To send", "ꯊꯥꯕ"),
    ],
},

# ━━━ 605: Frequently used verbs Part 3 ━━━
605: {
    "heading": "Frequently used verbs – Part 3",
    "rows": [
        ("To think", "ꯈꯟꯕ"),
        ("To understand", "ꯈꯉꯖꯕ"),
        ("To forget", "ꯀꯥꯎꯊꯣꯛꯄ"),
        ("To remember", "ꯅꯤꯡꯁꯤꯡꯕ"),
        ("To teach", "ꯇꯝꯍꯟꯕ"),
        ("To learn", "ꯇꯝꯕ"),
        ("To love", "ꯅꯨꯡꯁꯤꯕ"),
        ("To hate", "ꯄꯥꯝꯅꯕ"),
        ("To wait", "ꯂꯨꯕ"),
        ("To search / find", "ꯊꯤꯖꯤꯟꯕ"),
        ("To wear (clothes)", "ꯁꯦꯠꯄ"),
        ("To cut", "ꯁꯥꯠꯄ"),
        ("To break", "ꯉꯥꯛꯄ"),
        ("To fall", "ꯂꯧꯕ"),
        ("To grow", "ꯆꯥꯎꯈꯠꯄ"),
        ("To die", "ꯁꯤꯕ"),
        ("To live", "ꯍꯤꯡꯕ"),
        ("To put / keep", "ꯊꯝꯕ"),
    ],
},

# ━━━ 606: Frequently used verbs Part 4 ━━━
606: {
    "heading": "Frequently used verbs – Part 4",
    "rows": [
        ("To pick up", "ꯄꯨꯊꯣꯛꯄ"),
        ("To throw", "ꯊꯥꯛꯄ"),
        ("To push", "ꯊꯨꯝꯕ"),
        ("To pull", "ꯀꯥꯏꯕ"),
        ("To enter", "ꯆꯡꯕ"),
        ("To leave / exit", "ꯊꯣꯛꯄ"),
        ("To touch", "ꯁꯤꯟꯕ"),
        ("To smell", "ꯅꯥꯝꯕ"),
        ("To bite", "ꯆꯦꯛꯄ"),
        ("To climb", "ꯀꯥꯕ"),
        ("To count", "ꯃꯁꯤꯡ ꯁꯤꯕ"),
        ("To begin / start", "ꯍꯧꯕ"),
        ("To finish / end", "ꯂꯣꯏꯕ"),
        ("To return / come back", "ꯍꯟꯕ"),
        ("To show", "ꯎꯠꯄ"),
        ("To hide", "ꯂꯨꯝꯕ"),
        ("To fill", "ꯊꯥꯕ"),
        ("To mix", "ꯁꯤꯟꯅꯕ"),
    ],
},

# ━━━ 607: One verb multiple meanings Part 1 ━━━
607: {
    "heading": "One verb, multiple meanings – Part 1",
    "rows": [
        ("ꯊꯥꯕ – To drink", "ꯏꯁꯤꯡ ꯊꯥꯎ – Drink water"),
        ("ꯊꯥꯕ – To fill", "ꯏꯁꯤꯡ ꯊꯥꯎ – Fill water"),
        ("ꯊꯥꯕ – To send", "ꯆꯤꯠꯊꯤ ꯊꯥꯎ – Send a letter"),
        ("ꯂꯧꯕ – To take", "ꯂꯥꯏꯔꯤꯛ ꯂꯧꯎ – Take the book"),
        ("ꯂꯧꯕ – To accept", "ꯄꯤꯕꯝ ꯂꯧꯎ – Accept the gift"),
        ("ꯂꯧꯕ – To marry", "ꯅꯨꯄꯤ ꯂꯧꯕ – To marry a woman"),
        ("ꯁꯥꯕ – To cook", "ꯆꯤꯟꯖꯥꯛ ꯁꯥꯎ – Cook food"),
        ("ꯁꯥꯕ – To sing", "ꯏꯁꯩ ꯁꯥꯎ – Sing a song"),
        ("ꯁꯥꯕ – To play (instrument)", "ꯄꯦꯅꯥ ꯁꯥꯎ – Play the pena"),
        ("ꯇꯧꯕ – To do", "ꯊꯧꯔꯝ ꯇꯧꯎ – Do work"),
        ("ꯇꯧꯕ – To make", "ꯆꯤꯟꯖꯥꯛ ꯇꯧꯎ – Make food"),
        ("ꯄꯤꯕ – To give", "ꯑꯩꯗ ꯄꯤꯎ – Give to me"),
        ("ꯄꯤꯕ – To tell", "ꯑꯩꯗ ꯍꯥꯏꯄꯤꯎ – Tell me"),
        ("ꯆꯠꯄ – To go", "ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯂꯨ – Go to school"),
        ("ꯆꯠꯄ – To work / function", "ꯃꯁꯤꯟ ꯆꯠꯂꯤ – The machine works"),
        ("ꯈꯉꯕ – To know", "ꯑꯩ ꯈꯉꯏ – I know"),
        ("ꯈꯉꯕ – To recognise", "ꯑꯩ ꯈꯉꯖꯩ – I recognise"),
    ],
},

# ━━━ 608: One verb multiple meanings Part 2 ━━━
608: {
    "heading": "One verb, multiple meanings – Part 2",
    "rows": [
        ("ꯍꯧꯕ – To start", "ꯊꯧꯔꯝ ꯍꯧꯔꯦ – Start the work"),
        ("ꯍꯧꯕ – To bark", "ꯍꯨꯏ ꯍꯧꯔꯦ – The dog barks"),
        ("ꯐꯝꯕ – To sit", "ꯃꯐꯝꯗ ꯐꯝꯎ – Sit in the place"),
        ("ꯐꯝꯕ – To stay / live", "ꯃꯐꯝꯗ ꯐꯝꯂꯤ – He lives there"),
        ("ꯆꯡꯕ – To enter", "ꯌꯨꯝꯗ ꯆꯡꯎ – Enter the house"),
        ("ꯆꯡꯕ – To climb", "ꯆꯤꯡꯗ ꯆꯡꯎ – Climb the hill"),
        ("ꯊꯣꯛꯄ – To exit", "ꯌꯨꯝꯗꯒꯤ ꯊꯣꯛꯂꯨ – Exit the house"),
        ("ꯊꯣꯛꯄ – To remove", "ꯐꯤ ꯊꯣꯛꯂꯨ – Remove the cloth"),
        ("ꯌꯦꯡꯕ – To see", "ꯐꯤꯜꯝ ꯌꯦꯡꯎ – Watch a movie"),
        ("ꯌꯦꯡꯕ – To look after", "ꯃꯆꯥ ꯌꯦꯡꯁꯤꯟꯎ – Look after the child"),
        ("ꯇꯥꯕ – To hear", "ꯏꯁꯩ ꯇꯥꯎ – Hear a song"),
        ("ꯇꯥꯕ – To feel", "ꯅꯥ ꯇꯥꯏ – I feel pain"),
        ("ꯄꯥꯕ – To read", "ꯂꯥꯏꯔꯤꯛ ꯄꯥꯎ – Read a book"),
        ("ꯄꯥꯕ – To study", "ꯇꯝꯕ ꯄꯥꯎ – Study the lesson"),
        ("ꯍꯟꯕ – To return", "ꯌꯨꯝꯗ ꯍꯟꯂꯨ – Return home"),
        ("ꯍꯟꯕ – To repeat", "ꯑꯃꯨꯛ ꯍꯟꯅ ꯍꯥꯏꯎ – Say it once more"),
        ("ꯂꯩꯕ – To buy", "ꯐꯤ ꯂꯩꯎ – Buy cloth"),
    ],
},

# ━━━ 609: Adjectives Part 1 ━━━
609: {
    "heading": "Meitei adjectives – Part 1",
    "rows": [
        ("Big / Large", "ꯑꯆꯧꯕ"),
        ("Small", "ꯑꯄꯤꯛꯄ"),
        ("Good", "ꯑꯐꯕ"),
        ("Bad", "ꯐꯇꯕ"),
        ("Beautiful / Pretty", "ꯐꯖꯕ"),
        ("Ugly", "ꯑꯊꯤꯕ"),
        ("New", "ꯑꯍꯥꯟꯕ"),
        ("Old", "ꯑꯃꯟꯕ"),
        ("Long / Tall", "ꯑꯁꯥꯡꯕ"),
        ("Short", "ꯑꯇꯦꯟꯕ"),
        ("Hot", "ꯑꯁꯥꯕ"),
        ("Cold", "ꯑꯏꯡꯕ"),
        ("Sweet", "ꯑꯊꯨꯝꯕ"),
        ("Sour / Acid", "ꯑꯁꯤꯟꯕ"),
        ("Bitter", "ꯑꯈꯥꯕ"),
        ("Heavy", "ꯑꯂꯨꯝꯕ"),
        ("Light (not heavy)", "ꯏꯌꯡꯕ"),
        ("Clean", "ꯑꯁꯦꯡꯕ"),
        ("Dirty", "ꯑꯅꯩꯕ"),
        ("Strong", "ꯑꯀꯟꯕ"),
    ],
},

# ━━━ 610: Adverbs Part 1 ━━━
610: {
    "heading": "Adverbs in Meitei – Part 1",
    "rows": [
        ("How", "ꯀꯔꯝꯅ"),
        ("Where?", "ꯀꯗꯥꯏ?"),
        ("Why?", "ꯀꯔꯤ?"),
        ("From where?", "ꯀꯗꯥꯏꯗꯒꯤ?"),
        ("Below", "ꯃꯈꯥꯗ"),
        ("Behind", "ꯃꯇꯨꯡꯗ"),
        ("Daily", "ꯅꯨꯃꯤꯠ ꯈꯨꯗꯤꯡ"),
        ("Early", "ꯉꯟꯅ"),
        ("Elsewhere", "ꯃꯐꯝ ꯑꯃꯗ"),
        ("Here", "ꯑꯁꯤꯗ"),
        ("There", "ꯑꯗ"),
        ("Together", "ꯂꯣꯏꯅꯅ"),
        ("Now", "ꯍꯧꯖꯤꯛ"),
        ("Often", "ꯍꯟꯅ ꯍꯟꯅ"),
        ("Quickly", "ꯊꯨꯅ"),
        ("Outside", "ꯃꯄꯥꯟ"),
        ("Perhaps", "ꯀꯔꯤꯒꯨꯝꯕ"),
        ("Yes", "ꯍꯣꯏ"),
        ("No", "ꯅꯠꯇꯦ"),
        ("Well", "ꯐꯩ"),
    ],
},

# ━━━ 611: List of adverbs ━━━
611: {
    "heading": "More adverbs in Meitei",
    "rows": [
        ("Very / Much", "ꯌꯥꯝꯅ"),
        ("A little", "ꯈꯖꯤꯛꯇ"),
        ("Sometimes", "ꯀꯔꯤꯀꯔꯤꯒꯨꯝꯕꯗ"),
        ("Somewhere", "ꯀꯔꯤꯒꯨꯝꯕ ꯃꯐꯝꯗ"),
        ("Yearly", "ꯆꯍꯤ ꯈꯨꯗꯤꯡ"),
        ("Monthly", "ꯊꯥꯀꯨꯗꯤꯡꯗ"),
        ("Slowly", "ꯁꯦꯟꯅ"),
        ("Again", "ꯑꯃꯨꯛ ꯍꯟꯅ"),
        ("Always", "ꯃꯇꯝ ꯄꯨꯝꯕꯗ"),
        ("Never", "ꯀꯩꯗꯧꯡꯗ ꯅꯠꯇꯦ"),
        ("Already", "ꯍꯧꯖꯤꯛꯇꯒꯤ ꯃꯃꯥꯡꯗ"),
        ("Suddenly", "ꯈꯉꯗꯅ"),
        ("Alone", "ꯑꯃꯠꯇ"),
        ("Loudly", "ꯀꯥꯡꯂꯣꯟꯅ"),
        ("Softly / Gently", "ꯅꯣꯛꯅ"),
        ("Correctly", "ꯑꯆꯨꯝꯕꯅ"),
        ("Usually", "ꯃꯤꯌꯥꯝꯅ"),
        ("Immediately", "ꯈꯨꯗꯝ ꯈꯨꯗꯝꯗ"),
    ],
},

# ━━━ 612: Vegetables ━━━
612: {
    "heading": "Vegetable names in Meitei",
    "rows": [
        ("Onion", "ꯇꯤꯂꯧ"),
        ("Garlic", "ꯆꯅꯝ"),
        ("Ginger", "ꯁꯤꯡ"),
        ("Peas", "ꯍꯥꯋꯥꯏ ꯃꯉꯟ"),
        ("Green chilli", "ꯃꯔꯣꯛ ꯑꯇꯦꯛꯄ"),
        ("Dried chilli", "ꯃꯔꯣꯛ ꯑꯀꯡꯕ"),
        ("Potato", "ꯑꯂꯨ"),
        ("Tomato", "ꯈꯥꯃꯦꯟ ꯑꯈꯥꯕꯤ"),
        ("Brinjal / Eggplant", "ꯈꯥꯃꯦꯟ"),
        ("Cabbage", "ꯀꯣꯕꯤ"),
        ("Cauliflower", "ꯀꯣꯕꯤ ꯂꯩ"),
        ("Spinach", "ꯄꯥꯂꯛ"),
        ("Pumpkin", "ꯃꯩꯊꯣꯡ"),
        ("Bottle gourd", "ꯈꯣꯡꯂꯥꯏ"),
        ("Bamboo shoot", "ꯎꯁꯣꯏ"),
        ("Mushroom", "ꯎꯌꯦꯟ"),
        ("Radish", "ꯂꯐꯨ"),
        ("Turmeric", "ꯌꯩꯅꯡ"),
    ],
},

# ━━━ 613: Fruits ━━━
613: {
    "heading": "Names of fruits in Meitei",
    "rows": [
        ("Mango", "ꯍꯩꯅꯧ"),
        ("Banana", "ꯂꯐꯣꯏ"),
        ("Jackfruit", "ꯊꯩꯕꯣꯡ"),
        ("Pineapple", "ꯀꯦꯍꯨꯝ"),
        ("Plum", "ꯍꯩꯈꯥ"),
        ("Fig", "ꯍꯩꯕꯣꯡ"),
        ("Peach", "ꯆꯨꯝꯕ꯭ꯔꯥꯏ"),
        ("Papaya", "ꯑꯋꯥꯊꯕꯤ"),
        ("Guava", "ꯄꯦꯌꯥꯔꯥ"),
        ("Lemon / Lime", "ꯆꯝꯄ꯭ꯔꯥ"),
        ("Orange", "ꯀꯣꯝꯂꯥ"),
        ("Coconut", "ꯌꯨ"),
        ("Sugarcane", "ꯆꯨ"),
        ("Fruit (general)", "ꯍꯩ"),
        ("Fruit juice", "ꯍꯩ ꯃꯍꯤ"),
        ("Watermelon", "ꯋꯥꯇꯔꯃꯦꯂꯟ"),
        ("Pomegranate", "ꯑꯅꯥꯔ"),
    ],
},

# ━━━ 614: Birds ━━━
614: {
    "heading": "Names of birds in Meitei",
    "rows": [
        ("Bird", "ꯎꯆꯦꯛ"),
        ("Fowl / Hen", "ꯌꯦꯟ"),
        ("Duck", "ꯉꯥꯅꯨ"),
        ("Goose", "ꯀꯥꯡꯉꯥ"),
        ("Pigeon", "ꯈꯨꯅꯨ"),
        ("Parrot", "ꯇꯦꯟꯋꯥ"),
        ("Peacock", "ꯋꯥꯍꯣꯡ"),
        ("Crow", "ꯀꯥꯛ"),
        ("Sparrow", "ꯎꯆꯦꯛꯅꯠꯇꯣꯡ"),
        ("Eagle", "ꯃꯨꯌꯥꯏ"),
        ("Owl", "ꯍꯨꯇꯨꯝ"),
        ("Swan", "ꯍꯪꯁ"),
        ("Kingfisher", "ꯉꯥꯅꯨꯗꯨ"),
        ("Crane", "ꯂꯝꯒꯥꯡ"),
        ("Mynah", "ꯒꯣꯟꯒꯥꯡ"),
        ("Woodpecker", "ꯎꯈꯣꯛ"),
        ("Heron", "ꯅꯣꯡꯒꯥꯡ"),
    ],
},

# ━━━ 615: Insects ━━━
615: {
    "heading": "Names of insects in Meitei",
    "rows": [
        ("Insect (general)", "ꯇꯤꯟꯀꯥꯡ"),
        ("Butterfly", "ꯀꯨꯔꯥꯛ"),
        ("Mosquito", "ꯀꯥꯡ"),
        ("Ant", "ꯀꯥꯛꯆꯦꯡ"),
        ("Bee", "ꯈꯣꯏ"),
        ("Fly", "ꯍꯌꯤꯡ"),
        ("Spider", "ꯃꯤꯔꯡ"),
        ("Earthworm", "ꯇꯤꯟꯊꯣꯛ"),
        ("Snake", "ꯂꯤꯟ"),
        ("Water leech", "ꯇꯤꯟꯐꯥ"),
        ("Ground leech", "ꯀꯥꯛꯐꯥꯏ"),
        ("Scorpion", "ꯍꯨꯏꯆꯦꯡ"),
        ("Cockroach", "ꯁꯥꯒꯣꯟ"),
        ("Grasshopper", "ꯇꯤꯟꯍꯥꯎ"),
        ("Beetle", "ꯇꯤꯟꯒꯉ"),
        ("Caterpillar", "ꯍꯨꯂꯥꯡ"),
        ("Firefly", "ꯍꯨꯃꯩ"),
    ],
},

# ━━━ 616: Colours ━━━
616: {
    "heading": "Colours in Meitei",
    "rows": [
        ("Red", "ꯑꯉꯥꯡꯕ"),
        ("White", "ꯑꯉꯧꯕ"),
        ("Black", "ꯑꯃꯨꯕ"),
        ("Green", "ꯑꯁꯡꯕ"),
        ("Blue", "ꯍꯤꯒꯣꯛ"),
        ("Yellow", "ꯅꯥꯄꯨ"),
        ("Orange", "ꯃꯦꯃꯥꯟꯕ"),
        ("Purple", "ꯃꯉꯔꯥ ꯃꯆꯨ"),
        ("Pink", "ꯂꯩꯃꯆꯨ"),
        ("Brown", "ꯍꯤꯒꯣꯛ ꯑꯃꯨꯕ"),
        ("Grey", "ꯑꯉꯧꯕ ꯑꯃꯨꯕ"),
        ("Golden", "ꯁꯅꯥ ꯃꯆꯨ"),
        ("Silver", "ꯂꯨꯞ ꯃꯆꯨ"),
        ("Dark", "ꯑꯃꯝꯕ"),
        ("Light (colour)", "ꯊꯤꯡꯏ"),
        ("Bright", "ꯑꯉꯧꯕ"),
        ("Colour", "ꯃꯆꯨ"),
    ],
},

# ━━━ 617: Flowers ━━━
617: {
    "heading": "Names of flowers in Meitei",
    "rows": [
        ("Flower", "ꯂꯩ"),
        ("Flower bud", "ꯂꯩ ꯑꯄꯣꯝꯕ"),
        ("Lotus", "ꯊꯝꯕꯜ"),
        ("Rose", "ꯒꯨꯂꯥꯕ ꯂꯩ"),
        ("Marigold", "ꯉꯥꯔꯤ ꯂꯩ"),
        ("Jasmine", "ꯀꯨꯟꯗ ꯂꯩ"),
        ("Sunflower", "ꯅꯨꯃꯤꯠ ꯂꯩ"),
        ("Hibiscus", "ꯖꯕꯥ ꯂꯩ"),
        ("Lily", "ꯊꯔꯣꯏ"),
        ("Orchid", "ꯁꯤꯡꯈꯥ ꯂꯩ"),
        ("Champa", "ꯂꯩꯍꯧ"),
        ("Dahlia", "ꯗꯥꯍꯂꯤꯌꯥ ꯂꯩ"),
        ("Petal", "ꯃꯅꯥ"),
        ("Branch", "ꯄꯝꯕꯤ"),
        ("Leaf", "ꯃꯅꯥ"),
        ("Root", "ꯃꯔꯥ"),
        ("Grass", "ꯁꯖꯤꯛ"),
    ],
},

# ━━━ 618: Animals ━━━
618: {
    "heading": "Names of animals in Meitei",
    "rows": [
        ("Animal", "ꯁꯥ"),
        ("Dog", "ꯍꯨꯏ"),
        ("Cat", "ꯍꯧꯗꯣꯡ"),
        ("Cow", "ꯁꯟꯕꯤ"),
        ("Bull", "ꯀꯥꯎ"),
        ("Buffalo", "ꯏꯔꯣꯏ"),
        ("Goat", "ꯍꯃꯦꯡ"),
        ("Sheep", "ꯌꯥꯎ"),
        ("Pig", "ꯑꯣꯛ"),
        ("Horse", "ꯁꯥꯒꯣꯟ"),
        ("Elephant", "ꯁꯥꯃꯨ"),
        ("Tiger", "ꯀꯩ"),
        ("Lion", "ꯅꯣꯡꯁꯥ"),
        ("Deer", "ꯁꯖꯤ"),
        ("Monkey", "ꯌꯣꯡ"),
        ("Rat / Mouse", "ꯎꯆꯤ"),
        ("Rhinoceros", "ꯁꯥꯃꯨꯒꯟꯗꯥ"),
        ("Fish", "ꯉꯥ"),
    ],
},

# ━━━ 619: Common words – Misc ━━━
619: {
    "heading": "Frequently used common words – Miscellaneous",
    "rows": [
        ("Teacher", "ꯎꯖꯥꯕ"),
        ("Carpenter", "ꯎꯁꯥꯕ"),
        ("Blacksmith", "ꯊꯥꯡꯖꯕ"),
        ("Weaver", "ꯐꯤꯁꯥꯕ"),
        ("Washerman", "ꯐꯤꯁꯨꯕ"),
        ("Tailor", "ꯐꯨꯔꯤꯠꯇꯨꯕ"),
        ("Fisherman", "ꯉꯥꯇꯤꯕ"),
        ("Goldsmith", "ꯀꯣꯟꯁꯕ"),
        ("Milkman", "ꯁꯉꯣꯝ ꯁꯨꯝꯕ"),
        ("Spoon", "ꯈꯥꯕꯩ"),
        ("Basket", "ꯊꯨꯃꯨꯛ"),
        ("Box", "ꯎꯄꯨ"),
        ("Bag", "ꯈꯧ"),
        ("Broom", "ꯁꯨꯝꯆꯤꯠ"),
        ("Mat", "ꯐꯥꯛ"),
        ("Pillow", "ꯃꯣꯟ"),
        ("Mattress", "ꯃꯣꯟꯕꯥꯛ"),
        ("Key", "ꯁꯣ"),
        ("Lock", "ꯋꯥꯏꯈꯨ"),
        ("Rope", "ꯊꯧꯔꯤ ꯑꯆꯧꯕꯥ"),
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
    sys.stdout.buffer.write(f"Updated {updated} vocabulary lessons (597-619) in data_meitei.json\n".encode("utf-8"))

if __name__ == "__main__":
    main()
