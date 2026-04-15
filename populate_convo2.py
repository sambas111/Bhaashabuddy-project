#!/usr/bin/env python3
"""Populate conversation lessons 642-662 (5.23-5.43) with topic-relevant sentences."""
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

# ━━━ 642: In Bank ━━━
642: {
    "heading": "Conversation in a Bank",
    "rows": [
        ("I want to open an account.", "ꯑꯩ ꯑꯦꯀꯥꯎꯟꯠ ꯑꯃ ꯍꯥꯡꯅꯤꯡꯏ꯫"),
        ("What type of account?", "ꯀꯔꯤ ꯃꯈꯜꯒꯤ ꯑꯦꯀꯥꯎꯟꯠꯅꯣ?"),
        ("I want a savings account.", "ꯑꯩ ꯁꯦꯚꯤꯡꯁ ꯑꯦꯀꯥꯎꯟꯠ ꯄꯥꯝꯅꯩ꯫"),
        ("Please fill this form.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯐꯣꯔꯝ ꯑꯁꯤ ꯐꯤꯜ ꯇꯧꯕꯤꯌꯨ꯫"),
        ("I need to deposit money.", "ꯑꯩ ꯁꯦꯜ ꯗꯤꯄꯣꯖꯤꯠ ꯇꯧꯅꯤꯡꯏ꯫"),
        ("I want to withdraw money.", "ꯑꯩ ꯁꯦꯜ ꯂꯧꯊꯣꯛꯅꯤꯡꯏ꯫"),
        ("What is my balance?", "ꯑꯩꯒꯤ ꯕꯦꯂꯦꯟꯁ ꯀꯌꯥꯅꯣ?"),
        ("I want to transfer money.", "ꯑꯩ ꯁꯦꯜ ꯇ꯭ꯔꯥꯟꯁꯐꯔ ꯇꯧꯅꯤꯡꯏ꯫"),
        ("Please give me a cheque book.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯆꯦꯛ ꯕꯨꯛ ꯑꯃ ꯄꯤꯕꯤꯌꯨ꯫"),
        ("I forgot my PIN.", "ꯑꯩ ꯑꯩꯒꯤ ꯄꯤꯟ ꯀꯥꯎꯊꯣꯛꯈꯤ꯫"),
        ("My ATM card is blocked.", "ꯑꯩꯒꯤ ꯑꯦꯇꯤꯑꯦꯝ ꯀꯥꯔ꯭ꯗ ꯕ꯭ꯂꯣꯛ ꯇꯧꯔꯦ꯫"),
        ("I need a new passbook.", "ꯑꯩ ꯄꯥꯁꯕꯨꯛ ꯑꯍꯥꯟꯕ ꯑꯃ ꯃꯊꯧ ꯇꯥꯏ꯫"),
        ("Where is the ATM?", "ꯑꯦꯇꯤꯑꯦꯝ ꯀꯗꯥꯏꯗꯅꯣ?"),
        ("Please update my passbook.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯑꯩꯒꯤ ꯄꯥꯁꯕꯨꯛ ꯑꯞꯗꯦꯠ ꯇꯧꯕꯤꯌꯨ꯫"),
        ("Sign here please.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯑꯁꯤꯗ ꯁꯥꯏꯟ ꯇꯧꯕꯤꯌꯨ꯫"),
        ("Is internet banking available?", "ꯏꯟꯇꯔꯅꯦꯠ ꯕꯦꯡꯀꯤꯡ ꯐꯡꯒꯗꯕꯔꯥ?"),
        ("Thank you for your help.", "ꯃꯇꯦꯡ ꯄꯥꯡꯕꯤꯔꯛꯄꯗ ꯊꯥꯒꯠꯆꯔꯤ꯫"),
    ],
},

# ━━━ 643: Temple Visit ━━━
643: {
    "heading": "Enquiry about Temple Visit",
    "rows": [
        ("Where is the nearest temple?", "ꯑꯅꯥꯛꯇꯒꯤ ꯂꯥꯏꯁꯡ ꯀꯗꯥꯏꯗꯅꯣ?"),
        ("What time does the temple open?", "ꯂꯥꯏꯁꯡ ꯄꯨꯡ ꯀꯌꯥꯗ ꯍꯥꯡꯕꯅꯣ?"),
        ("The temple opens at six.", "ꯂꯥꯏꯁꯡ ꯄꯨꯡ ꯇꯔꯨꯛꯇ ꯍꯥꯡꯏ꯫"),
        ("Is there a dress code?", "ꯐꯤ ꯁꯦꯠꯄꯒꯤ ꯅꯤꯌꯝ ꯂꯩꯕꯔꯥ?"),
        ("Can we take photos inside?", "ꯃꯅꯨꯡꯗ ꯐꯣꯇꯣ ꯂꯧꯕ ꯌꯥꯕꯔꯥ?"),
        ("Remove your shoes here.", "ꯅꯈꯣꯏꯒꯤ ꯈꯣꯡꯎꯞ ꯑꯁꯤꯗ ꯊꯣꯛꯄꯤꯌꯨ꯫"),
        ("The temple is very old.", "ꯂꯥꯏꯁꯡ ꯑꯁꯤ ꯌꯥꯝꯅ ꯑꯔꯤꯕꯅꯤ꯫"),
        ("It is a beautiful temple.", "ꯃꯁꯤ ꯌꯥꯝꯅ ꯐꯖꯕ ꯂꯥꯏꯁꯡꯅꯤ꯫"),
        ("There is a festival tomorrow.", "ꯍꯌꯦꯡ ꯊꯧꯔꯝ ꯑꯃ ꯂꯩꯒꯅꯤ꯫"),
        ("Many people come to pray.", "ꯃꯤꯑꯣꯏ ꯃꯌꯥꯝ ꯈꯨꯔꯨꯝꯖꯕ ꯂꯥꯛꯏ꯫"),
        ("Where can we offer flowers?", "ꯑꯩꯈꯣꯏ ꯂꯩ ꯀꯗꯥꯏꯗ ꯀꯠꯊꯣꯛꯒꯅꯤ?"),
        ("The prasad is distributed at noon.", "ꯄ꯭ꯔꯁꯥꯗ ꯅꯨꯃꯤꯗꯥꯡꯗ ꯌꯦꯛꯏ꯫"),
        ("This temple is famous.", "ꯂꯥꯏꯁꯡ ꯑꯁꯤ ꯃꯃꯤꯡ ꯆꯠꯅꯕꯅꯤ꯫"),
        ("I come here every week.", "ꯑꯩ ꯑꯁꯤꯗ ꯆꯌꯣꯟ ꯈꯨꯗꯤꯡ ꯂꯥꯛꯏ꯫"),
        ("The priests are very kind.", "ꯃꯩꯕ ꯑꯁꯤꯡ ꯌꯥꯝꯅ ꯐꯕꯅꯤ꯫"),
        ("Let us pray together.", "ꯂꯣꯏꯅꯅ ꯈꯨꯔꯨꯝꯖꯔꯁꯤ꯫"),
        ("Peace be with you.", "ꯅꯈꯣꯏꯗ ꯂꯩꯔꯕꯁꯤꯡ ꯂꯩꯕꯤꯌꯨ꯫"),
    ],
},

# ━━━ 644: Friend's parents at lunch ━━━
644: {
    "heading": "With friend's parents at lunch table",
    "rows": [
        ("Good afternoon, uncle.", "ꯅꯨꯃꯤꯗꯥꯡꯒꯤ ꯅꯨꯃꯤꯗꯥꯡ, ꯏꯄꯟ꯫"),
        ("Come, sit with us.", "ꯂꯥꯛꯎ, ꯑꯩꯈꯣꯏꯒ ꯐꯝꯎ꯫"),
        ("The food smells delicious.", "ꯆꯤꯟꯖꯥꯛ ꯑꯁꯤ ꯌꯥꯝꯅ ꯐꯖꯕ ꯅꯥꯝꯅꯩ꯫"),
        ("Please help yourself.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯂꯧꯁꯤꯟꯅꯕꯤꯌꯨ꯫"),
        ("Would you like more rice?", "ꯆꯦꯡ ꯑꯃꯨꯛ ꯄꯥꯝꯅꯔꯥ?"),
        ("Yes, please.", "ꯍꯣꯏ, ꯆꯥꯅꯕꯤꯗꯨꯅ꯫"),
        ("The fish curry is very tasty.", "ꯉꯥ ꯑꯣꯠꯇꯤ ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("Aunty, you cook very well.", "ꯏꯅꯦ, ꯅꯈꯣꯏ ꯌꯥꯝꯅ ꯐꯖꯅ ꯁꯥꯏ꯫"),
        ("Thank you, eat more.", "ꯊꯥꯒꯠꯆꯔꯤ, ꯑꯃꯨꯛ ꯆꯥꯎ꯫"),
        ("What is your favourite food?", "ꯅꯈꯣꯏꯒꯤ ꯅꯨꯡꯁꯤꯠꯄ ꯆꯤꯟꯖꯥꯛ ꯀꯔꯤꯅꯣ?"),
        ("I like eromba very much.", "ꯑꯩ ꯏꯔꯣꯝꯕꯥ ꯌꯥꯝꯅ ꯅꯨꯡꯁꯤ꯫"),
        ("Have some sweets.", "ꯑꯊꯨꯝꯕ ꯈꯔ ꯆꯥꯎ꯫"),
        ("I am full now.", "ꯑꯩ ꯍꯧꯖꯤꯛ ꯐꯨꯔꯦ꯫"),
        ("The food was wonderful.", "ꯆꯤꯟꯖꯥꯛ ꯑꯁꯤ ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("Please have some water.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯏꯁꯤꯡ ꯈꯔ ꯊꯛꯄꯤꯌꯨ꯫"),
        ("Thank you for the meal.", "ꯆꯤꯟꯖꯥꯛ ꯄꯤꯕꯤꯔꯛꯄꯗ ꯊꯥꯒꯠꯆꯔꯤ꯫"),
        ("I will come again.", "ꯑꯩ ꯑꯃꯨꯛ ꯂꯥꯛꯀꯅꯤ꯫"),
    ],
},

# ━━━ 645: Football match ━━━
645: {
    "heading": "Friend talking about football match",
    "rows": [
        ("Did you watch the match yesterday?", "ꯅꯈꯣꯏ ꯉꯔꯥꯡꯒꯤ ꯃꯦꯆ ꯌꯦꯡꯈꯤꯕꯔꯥ?"),
        ("Yes, it was amazing!", "ꯍꯣꯏ, ꯌꯥꯝꯅ ꯐꯖꯩ!"),
        ("Who won the match?", "ꯀꯅ ꯃꯦꯆ ꯃꯥꯏꯈꯤꯕꯅꯣ?"),
        ("Our team won!", "ꯑꯩꯈꯣꯏꯒꯤ ꯇꯤꯝ ꯃꯥꯏꯈꯤ!"),
        ("The score was two to one.", "ꯁ꯭ꯀꯣꯔ ꯑꯅꯤ ꯑꯃ ꯑꯣꯏꯈꯤ꯫"),
        ("The goalkeeper played very well.", "ꯒꯣꯜꯀꯤꯄꯔ ꯌꯥꯝꯅ ꯐꯖꯅ ꯁꯥꯈꯤ꯫"),
        ("Who scored the goal?", "ꯀꯅ ꯒꯣꯜ ꯇꯧꯈꯤꯕꯅꯣ?"),
        ("The striker scored in the last minute.", "ꯁ꯭ꯠꯔꯥꯏꯀꯔꯅ ꯑꯔꯣꯏꯕ ꯃꯤꯅꯤꯠꯇ ꯒꯣꯜ ꯇꯧꯈꯤ꯫"),
        ("That was a great match.", "ꯃꯦꯆ ꯃꯁꯤ ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("The crowd was cheering loudly.", "ꯃꯤꯁꯤꯡ ꯌꯥꯝꯅ ꯀꯥꯡꯂꯣꯟꯅ ꯈꯣꯡꯆꯠ ꯄꯤꯈꯤ꯫"),
        ("When is the next match?", "ꯑꯇꯣꯞꯄ ꯃꯦꯆ ꯀꯗꯥꯏꯗꯅꯣ?"),
        ("Let us go watch together.", "ꯂꯣꯏꯅꯅ ꯌꯦꯡꯕ ꯆꯠꯁꯤ꯫"),
        ("I support this team.", "ꯑꯩ ꯇꯤꯝ ꯑꯁꯤ ꯁꯞꯣꯔ꯭ꯠ ꯇꯧꯏ꯫"),
        ("Football is my favourite sport.", "ꯐꯨꯕꯣꯜ ꯑꯩꯒꯤ ꯅꯨꯡꯁꯤꯠꯄ ꯁ꯭ꯄꯣꯔ꯭ꯠꯅꯤ꯫"),
        ("He got a red card.", "ꯃꯍꯥꯛ ꯑꯉꯥꯡꯕ ꯀꯥꯔ꯭ꯗ ꯐꯡꯈꯤ꯫"),
        ("The referee was fair.", "ꯔꯦꯐꯔꯤ ꯑꯁꯤ ꯑꯆꯨꯝꯕ ꯑꯣꯏꯈꯤ꯫"),
        ("We should play more football.", "ꯑꯩꯈꯣꯏ ꯐꯨꯕꯣꯜ ꯑꯃꯨꯛ ꯁꯥꯒꯗꯕꯅꯤ꯫"),
    ],
},

# ━━━ 646: Friends plan movie ━━━
646: {
    "heading": "Friends plan to watch movie",
    "rows": [
        ("Let us watch a movie today.", "ꯉꯁꯤ ꯐꯤꯜꯝ ꯑꯃ ꯌꯦꯡꯁꯤ꯫"),
        ("Which movie is good?", "ꯀꯔꯤ ꯐꯤꯜꯝ ꯐꯖꯕꯅꯣ?"),
        ("There is a new action movie.", "ꯑꯍꯥꯟꯕ ꯑꯦꯛꯁꯟ ꯐꯤꯜꯝ ꯑꯃ ꯂꯩꯔꯤ꯫"),
        ("What time is the show?", "ꯁꯣ ꯄꯨꯡ ꯀꯌꯥꯗꯅꯣ?"),
        ("The show is at seven.", "ꯁꯣ ꯄꯨꯡ ꯇꯔꯦꯠꯇꯅꯤ꯫"),
        ("Book the tickets online.", "ꯇꯤꯀꯦꯠ ꯑꯣꯟꯂꯥꯏꯟꯗ ꯕꯨꯛ ꯇꯧꯕꯤꯌꯨ꯫"),
        ("How much is one ticket?", "ꯇꯤꯀꯦꯠ ꯑꯃꯒꯤ ꯃꯃꯜ ꯀꯌꯥꯅꯣ?"),
        ("I will bring popcorn.", "ꯑꯩ ꯄꯣꯞꯀꯣꯔ꯭ꯟ ꯄꯨꯔꯛꯀꯅꯤ꯫"),
        ("Let us sit in the front.", "ꯃꯃꯥꯡꯗ ꯐꯝꯁꯤ꯫"),
        ("The movie starts soon.", "ꯐꯤꯜꯝ ꯊꯨꯅ ꯍꯧꯒꯅꯤ꯫"),
        ("Turn off your phone.", "ꯅꯈꯣꯏꯒꯤ ꯐꯣꯟ ꯀꯠꯊꯕꯤꯌꯨ꯫"),
        ("The hero is my favourite.", "ꯍꯤꯔꯣ ꯑꯗꯨ ꯑꯩꯒꯤ ꯅꯨꯡꯁꯤꯠꯄꯅꯤ꯫"),
        ("The song was beautiful.", "ꯏꯁꯩ ꯑꯗꯨ ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("Did you like the movie?", "ꯅꯈꯣꯏ ꯐꯤꯜꯝ ꯅꯨꯡꯁꯤꯈꯤꯕꯔꯥ?"),
        ("Yes, it was fantastic.", "ꯍꯣꯏ, ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("Let us watch another one next week.", "ꯑꯇꯣꯞꯄ ꯆꯌꯣꯟꯗ ꯑꯃꯨꯛ ꯌꯦꯡꯁꯤ꯫"),
        ("That was a good evening.", "ꯅꯨꯃꯗꯥꯡ ꯑꯣꯋꯥꯏꯔꯝ ꯑꯗꯨ ꯐꯖꯩ꯫"),
    ],
},

# ━━━ 647: Football world cup ━━━
647: {
    "heading": "Friends talking about football world cup",
    "rows": [
        ("The World Cup is starting!", "ꯋꯔ꯭ꯜꯗ ꯀꯞ ꯍꯧꯔꯤ!"),
        ("Which team will win?", "ꯀꯔꯤ ꯇꯤꯝ ꯃꯥꯏꯒꯅꯤ?"),
        ("I think Brazil will win.", "ꯑꯩꯅ ꯈꯟꯗ ꯕ꯭ꯔꯥꯖꯤꯜ ꯃꯥꯏꯒꯅꯤ꯫"),
        ("Argentina is also very strong.", "ꯑꯔ꯭ꯖꯦꯟꯇꯤꯅꯥ ꯃꯁꯨ ꯌꯥꯝꯅ ꯑꯀꯟꯕꯅꯤ꯫"),
        ("Who is your favourite player?", "ꯅꯈꯣꯏꯒꯤ ꯅꯨꯡꯁꯤꯠꯄ ꯄ꯭ꯂꯦꯌꯔ ꯀꯅꯅꯣ?"),
        ("I like Messi.", "ꯑꯩ ꯃꯦꯁꯤ ꯅꯨꯡꯁꯤ꯫"),
        ("The opening match was exciting.", "ꯍꯧꯈꯤꯕ ꯃꯦꯆ ꯌꯥꯝꯅ ꯈꯣꯡꯆꯠ ꯐꯖꯩ꯫"),
        ("Let us watch it together.", "ꯂꯣꯏꯅꯅ ꯌꯦꯡꯁꯤ꯫"),
        ("The stadium was full.", "ꯁ꯭ꯇꯦꯗꯤꯌꯝ ꯊꯨꯅ ꯐꯨꯔꯦ꯫"),
        ("What a beautiful goal!", "ꯌꯥꯝꯅ ꯐꯖꯕ ꯒꯣꯜ!"),
        ("The match went to penalty.", "ꯃꯦꯆ ꯄꯦꯅꯜꯇꯤꯗ ꯆꯠꯈꯤ꯫"),
        ("India should qualify next time.", "ꯏꯟꯗꯤꯌꯥ ꯑꯇꯣꯞꯄ ꯃꯇꯝꯗ ꯀ꯭ꯋꯥꯂꯤꯐꯥꯏ ꯇꯧꯒꯗꯕꯅꯤ꯫"),
        ("Football unites the world.", "ꯐꯨꯕꯣꯜꯅ ꯃꯥꯂꯦꯝ ꯄꯨꯝꯕ ꯄꯨꯟꯁꯤꯟꯏ꯫"),
        ("The final is next Sunday.", "ꯐꯥꯏꯅꯜ ꯑꯁꯤ ꯑꯇꯣꯞꯄ ꯅꯣꯡꯃꯄꯟꯕꯗꯅꯤ꯫"),
        ("I cannot wait for the final.", "ꯑꯩ ꯐꯥꯏꯅꯜ ꯂꯨꯕ ꯉꯝꯗꯦ꯫"),
        ("May the best team win.", "ꯈ꯭ꯋꯥꯏꯗꯒꯤ ꯐꯕ ꯇꯤꯝ ꯃꯥꯏꯕꯤꯌꯨ꯫"),
        ("It was a great tournament.", "ꯇꯧꯔ꯭ꯅꯃꯦꯟꯠ ꯑꯁꯤ ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
    ],
},

# ━━━ 648: Tour guide with tourists ━━━
648: {
    "heading": "Tour guide with tourists",
    "rows": [
        ("Welcome to Manipur!", "ꯃꯅꯤꯄꯨꯔꯗ ꯑꯣꯛꯆꯔꯤ!"),
        ("I am your tour guide.", "ꯑꯩ ꯅꯈꯣꯏꯒꯤ ꯇꯨꯔ ꯒꯥꯏꯗꯅꯤ꯫"),
        ("This is Kangla Fort.", "ꯃꯁꯤ ꯀꯡꯂꯥ ꯐꯣꯔ꯭ꯠꯅꯤ꯫"),
        ("It has a long history.", "ꯃꯁꯤꯒꯤ ꯋꯥꯔꯤ ꯑꯁꯥꯡꯕ ꯂꯩ꯫"),
        ("This lake is called Loktak.", "ꯄꯥꯠ ꯑꯁꯤꯕꯨ ꯂꯣꯛꯇꯥꯛ ꯀꯧꯏ꯫"),
        ("It is the largest freshwater lake.", "ꯃꯁꯤ ꯈ꯭ꯋꯥꯏꯗꯒꯤ ꯑꯆꯧꯕ ꯄꯥꯠꯅꯤ꯫"),
        ("You can see floating islands.", "ꯅꯈꯣꯏ ꯏꯁꯤꯡꯗ ꯇꯨꯡ ꯂꯩꯕ ꯌꯦꯡꯕ ꯌꯥꯏ꯫"),
        ("Take photos here.", "ꯑꯁꯤꯗ ꯐꯣꯇꯣ ꯂꯧꯕꯤꯌꯨ꯫"),
        ("Be careful on the steps.", "ꯈꯣꯡꯊꯥꯛꯇ ꯆꯦꯛꯁꯤꯟꯅ ꯂꯩꯕꯤꯌꯨ꯫"),
        ("We will have lunch here.", "ꯑꯩꯈꯣꯏ ꯑꯁꯤꯗ ꯅꯨꯃꯤꯗꯥꯡꯒꯤ ꯆꯤꯟꯖꯥꯛ ꯆꯥꯒꯅꯤ꯫"),
        ("Try the local food.", "ꯃꯐꯝ ꯑꯁꯤꯒꯤ ꯆꯤꯟꯖꯥꯛ ꯆꯥꯁꯤꯟꯕꯤꯌꯨ꯫"),
        ("The bus leaves at four.", "ꯕꯁ ꯄꯨꯡ ꯃꯔꯤꯗ ꯆꯠꯏ꯫"),
        ("Do not litter here.", "ꯑꯁꯤꯗ ꯂꯤꯛ ꯊꯥꯅꯨ꯫"),
        ("Enjoy your trip!", "ꯅꯈꯣꯏꯒꯤ ꯇꯨꯔ ꯐꯖꯅ ꯄꯥꯡꯊꯣꯛꯄꯤꯌꯨ!"),
        ("Manipur is the jewel of India.", "ꯃꯅꯤꯄꯨꯔ ꯑꯁꯤ ꯏꯟꯗꯤꯌꯥꯒꯤ ꯔꯠꯅꯅꯤ꯫"),
        ("Thank you for visiting.", "ꯂꯥꯛꯈꯤꯕꯗ ꯊꯥꯒꯠꯆꯔꯤ꯫"),
        ("Come again!", "ꯑꯃꯨꯛ ꯂꯥꯛꯄꯤꯌꯨ!"),
    ],
},

# ━━━ 649: Language Proficiency Test ━━━
649: {
    "heading": "Language Proficiency Test for banks",
    "rows": [
        ("I am here for the language test.", "ꯑꯩ ꯂꯣꯟ ꯇꯦꯁ꯭ꯠꯀꯤꯗꯃꯛ ꯂꯥꯛꯈꯤꯕꯅꯤ꯫"),
        ("Which language are you taking?", "ꯅꯈꯣꯏ ꯀꯔꯤ ꯂꯣꯟ ꯂꯧꯔꯤꯕꯅꯣ?"),
        ("I am taking the Meitei test.", "ꯑꯩ ꯃꯩꯇꯩ ꯂꯣꯟ ꯇꯦꯁ꯭ꯠ ꯂꯧꯔꯤ꯫"),
        ("Read this passage aloud.", "ꯄꯦꯁꯦꯖ ꯑꯁꯤ ꯀꯥꯡꯂꯣꯟꯅ ꯄꯥꯕꯤꯌꯨ꯫"),
        ("Write a paragraph in Meitei.", "ꯃꯩꯇꯩ ꯂꯣꯟꯗ ꯄꯦꯔꯥꯒ꯭ꯔꯥꯐ ꯑꯃ ꯏꯕꯤꯌꯨ꯫"),
        ("Translate this sentence.", "ꯋꯥꯍꯩ ꯑꯁꯤ ꯍꯣꯡꯗꯣꯛꯄꯤꯌꯨ꯫"),
        ("How many marks is the test?", "ꯇꯦꯁ꯭ꯠ ꯑꯁꯤ ꯃꯥꯔ꯭ꯛ ꯀꯌꯥꯅꯣ?"),
        ("The test is for hundred marks.", "ꯇꯦꯁ꯭ꯠ ꯑꯁꯤ ꯃꯥꯔ꯭ꯛ ꯆꯥ ꯑꯃꯅꯤ꯫"),
        ("You have one hour.", "ꯅꯈꯣꯏꯒꯤ ꯄꯨꯡ ꯑꯃ ꯂꯩ꯫"),
        ("Do not use a dictionary.", "ꯗꯤꯛꯁꯅꯔꯤ ꯁꯤꯖꯤꯟꯅꯅꯨ꯫"),
        ("Write clearly.", "ꯆꯦꯠꯅ ꯏꯕꯤꯌꯨ꯫"),
        ("Check your answers.", "ꯅꯈꯣꯏꯒꯤ ꯄꯥꯎꯈꯨꯝ ꯆꯦꯛ ꯇꯧꯕꯤꯌꯨ꯫"),
        ("Time is up.", "ꯃꯇꯝ ꯂꯣꯏꯔꯦ꯫"),
        ("Submit your paper.", "ꯅꯈꯣꯏꯒꯤ ꯄꯦꯄꯔ ꯄꯤꯕꯤꯌꯨ꯫"),
        ("Results will come in a week.", "ꯔꯤꯖꯜꯠ ꯆꯌꯣꯟ ꯑꯃꯗ ꯂꯥꯛꯀꯅꯤ꯫"),
        ("I hope I pass.", "ꯑꯩ ꯄꯥꯁ ꯇꯧꯕ ꯊꯥꯖꯩ꯫"),
        ("Good luck!", "ꯐꯕ ꯐꯡꯕꯤꯌꯨ!"),
    ],
},

# ━━━ 650: About food, lunch, meal ━━━
650: {
    "heading": "Conversation about food and meals",
    "rows": [
        ("Are you hungry?", "ꯅꯈꯣꯏ ꯆꯤꯟꯖꯥꯛ ꯂꯨꯏꯕꯔꯥ?"),
        ("Yes, I am very hungry.", "ꯍꯣꯏ, ꯑꯩ ꯌꯥꯝꯅ ꯆꯤꯟꯖꯥꯛ ꯂꯨꯏ꯫"),
        ("What is for lunch?", "ꯅꯨꯃꯤꯗꯥꯡꯒꯤ ꯆꯤꯟꯖꯥꯛ ꯀꯔꯤꯅꯣ?"),
        ("There is rice and dal.", "ꯆꯦꯡ ꯑꯃꯁꯨꯡ ꯗꯥꯜ ꯂꯩꯔꯤ꯫"),
        ("I want to eat fish.", "ꯑꯩ ꯉꯥ ꯆꯥꯅꯤꯡꯏ꯫"),
        ("The food is very spicy.", "ꯆꯤꯟꯖꯥꯛ ꯑꯁꯤ ꯌꯥꯝꯅ ꯍꯩꯏ꯫"),
        ("I do not eat meat.", "ꯑꯩ ꯁꯥ ꯆꯥꯗꯦ꯫"),
        ("I am vegetarian.", "ꯑꯩ ꯚꯦꯖꯤꯇꯦꯔꯤꯌꯟꯅꯤ꯫"),
        ("Can I have some water?", "ꯏꯁꯤꯡ ꯈꯔ ꯐꯡꯕ ꯌꯥꯕꯔꯥ?"),
        ("The tea is very sweet.", "ꯆꯥ ꯑꯁꯤ ꯌꯥꯝꯅ ꯑꯊꯨꯝꯕꯩ꯫"),
        ("Let us have dinner together.", "ꯂꯣꯏꯅꯅ ꯑꯍꯤꯡꯒꯤ ꯆꯤꯟꯖꯥꯛ ꯆꯥꯁꯤ꯫"),
        ("I cooked biryani today.", "ꯑꯩ ꯉꯁꯤ ꯕꯤꯔꯤꯌꯥꯅꯤ ꯁꯥꯈꯤ꯫"),
        ("Breakfast is ready.", "ꯑꯌꯨꯛꯀꯤ ꯆꯤꯟꯖꯥꯛ ꯁꯦꯝꯈꯤ꯫"),
        ("I love Manipuri eromba.", "ꯑꯩ ꯃꯅꯤꯄꯨꯔꯤ ꯏꯔꯣꯝꯕꯥ ꯅꯨꯡꯁꯤ꯫"),
        ("Let us try a new restaurant.", "ꯑꯍꯥꯟꯕ ꯔꯦꯁ꯭ꯇꯧꯔꯦꯟꯠ ꯑꯃ ꯆꯥꯁꯤꯟꯁꯤ꯫"),
        ("The food was delicious.", "ꯆꯤꯟꯖꯥꯛ ꯑꯁꯤ ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("I am full, thank you.", "ꯑꯩ ꯐꯨꯔꯦ, ꯊꯥꯒꯠꯆꯔꯤ꯫"),
    ],
},

# ━━━ 651: Hobby class ━━━
651: {
    "heading": "Conversation about hobby class",
    "rows": [
        ("What is your hobby?", "ꯅꯈꯣꯏꯒꯤ ꯍꯣꯕꯤ ꯀꯔꯤꯅꯣ?"),
        ("I like painting.", "ꯑꯩ ꯄꯦꯏꯟꯇꯤꯡ ꯅꯨꯡꯁꯤ꯫"),
        ("I learn music.", "ꯑꯩ ꯃꯌꯨꯖꯤꯛ ꯇꯝꯏ꯫"),
        ("I go to dance class.", "ꯑꯩ ꯗꯥꯟꯁ ꯀ꯭ꯂꯥꯁꯇ ꯆꯠꯏ꯫"),
        ("My hobby is reading.", "ꯑꯩꯒꯤ ꯍꯣꯕꯤ ꯂꯥꯏꯔꯤꯛ ꯄꯥꯕꯅꯤ꯫"),
        ("I enjoy cooking.", "ꯑꯩ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯕ ꯅꯨꯡꯁꯤ꯫"),
        ("She plays the pena.", "ꯃꯍꯥꯛ ꯄꯦꯅꯥ ꯁꯥꯏ꯫"),
        ("He likes photography.", "ꯃꯍꯥꯛ ꯐꯣꯇꯣꯒ꯭ꯔꯥꯐꯤ ꯅꯨꯡꯁꯤ꯫"),
        ("I joined a drawing class.", "ꯑꯩ ꯗ꯭ꯔꯣꯏꯡ ꯀ꯭ꯂꯥꯁꯇ ꯌꯥꯎꯈꯤ꯫"),
        ("Practice makes perfect.", "ꯄ꯭ꯔꯦꯛꯇꯤꯁ ꯇꯧꯕꯅ ꯐꯖꯍꯟꯏ꯫"),
        ("I paint every weekend.", "ꯑꯩ ꯋꯤꯀꯦꯟꯗ ꯈꯨꯗꯤꯡ ꯄꯦꯏꯟꯇꯤꯡ ꯇꯧꯏ꯫"),
        ("My teacher is very talented.", "ꯑꯩꯒꯤ ꯎꯖꯥꯕ ꯌꯥꯝꯅ ꯊꯧꯅ ꯂꯩꯕꯅꯤ꯫"),
        ("I want to learn singing.", "ꯑꯩ ꯏꯁꯩ ꯁꯥꯕ ꯇꯝꯅꯤꯡꯏ꯫"),
        ("Hobbies make life interesting.", "ꯍꯣꯕꯤꯅ ꯄꯨꯟꯁꯤꯕꯨ ꯐꯖꯍꯟꯏ꯫"),
        ("I have a class tomorrow.", "ꯑꯩꯒꯤ ꯀ꯭ꯂꯥꯁ ꯍꯌꯦꯡ ꯂꯩ꯫"),
        ("Let us go together.", "ꯂꯣꯏꯅꯅ ꯆꯠꯁꯤ꯫"),
        ("It is a fun activity.", "ꯃꯁꯤ ꯍꯔꯥꯎꯕ ꯊꯧꯔꯝꯅꯤ꯫"),
    ],
},

# ━━━ 652: Frequently used sentences misc ━━━
652: {
    "heading": "Frequently used sentences – miscellaneous",
    "rows": [
        ("I am going home.", "ꯑꯩ ꯌꯨꯝꯗ ꯆꯠꯂꯤ꯫"),
        ("Please wait a moment.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯈꯔ ꯂꯨꯕꯤꯌꯨ꯫"),
        ("I will come back soon.", "ꯑꯩ ꯊꯨꯅ ꯍꯟꯂꯛꯀꯅꯤ꯫"),
        ("What happened?", "ꯀꯔꯤ ꯑꯣꯏꯈꯤꯕꯅꯣ?"),
        ("Nothing happened.", "ꯀꯔꯤꯁꯨ ꯑꯣꯏꯈꯤꯗꯦ꯫"),
        ("It does not matter.", "ꯀꯔꯤꯁꯨ ꯑꯣꯏꯗꯦ꯫"),
        ("I do not know.", "ꯑꯩ ꯈꯉꯗꯦ꯫"),
        ("I forgot.", "ꯑꯩ ꯀꯥꯎꯊꯣꯛꯈꯤ꯫"),
        ("Please help me.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯑꯩꯕꯨ ꯃꯇꯦꯡ ꯄꯥꯡꯕꯤꯌꯨ꯫"),
        ("I am sorry.", "ꯄꯨꯛꯅꯤꯡ ꯆꯥꯏ꯫"),
        ("No problem.", "ꯋꯥꯈꯜ ꯂꯩꯇꯦ꯫"),
        ("I am tired.", "ꯑꯩ ꯁꯣꯛꯂꯦ꯫"),
        ("I am happy today.", "ꯑꯩ ꯉꯁꯤ ꯍꯔꯥꯎꯏ꯫"),
        ("Take care.", "ꯆꯦꯛꯁꯤꯟꯅ ꯂꯩꯕꯤꯌꯨ꯫"),
        ("Have a nice day.", "ꯅꯨꯃꯤꯠ ꯐꯕ ꯐꯡꯕꯤꯌꯨ꯫"),
        ("Let us go.", "ꯆꯠꯁꯤ꯫"),
        ("See you tomorrow.", "ꯍꯌꯦꯡ ꯎꯅꯒꯅꯤ꯫"),
    ],
},

# ━━━ 653: Frequently used sentences misc 2 ━━━
653: {
    "heading": "Frequently used sentences – miscellaneous part 2",
    "rows": [
        ("What is this?", "ꯃꯁꯤ ꯀꯔꯤꯅꯣ?"),
        ("How much does this cost?", "ꯃꯁꯤꯒꯤ ꯃꯃꯜ ꯀꯌꯥꯅꯣ?"),
        ("I need this.", "ꯑꯩ ꯃꯁꯤ ꯃꯊꯧ ꯇꯥꯏ꯫"),
        ("I do not need this.", "ꯑꯩ ꯃꯁꯤ ꯃꯊꯧ ꯇꯥꯗꯦ꯫"),
        ("Can you repeat that?", "ꯑꯃꯨꯛ ꯍꯟꯅ ꯍꯥꯏꯕ ꯌꯥꯕꯔꯥ?"),
        ("Please speak slowly.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯁꯦꯟꯅ ꯁꯦꯟꯅ ꯋꯥ ꯉꯥꯡꯕꯤꯌꯨ꯫"),
        ("I understand.", "ꯑꯩ ꯈꯉꯖꯩ꯫"),
        ("I do not understand.", "ꯑꯩ ꯈꯉꯖꯗꯦ꯫"),
        ("Where is the toilet?", "ꯕꯥꯊꯔꯨꯝ ꯀꯗꯥꯏꯗꯅꯣ?"),
        ("I am learning Meitei.", "ꯑꯩ ꯃꯩꯇꯩ ꯂꯣꯟ ꯇꯝꯔꯤ꯫"),
        ("You speak very well.", "ꯅꯈꯣꯏ ꯌꯥꯝꯅ ꯐꯖꯅ ꯋꯥ ꯉꯥꯡꯏ꯫"),
        ("Is anyone there?", "ꯀꯅ ꯑꯃ ꯂꯩꯕꯔꯥ?"),
        ("Come here.", "ꯑꯁꯤꯗ ꯂꯥꯛꯎ꯫"),
        ("Go there.", "ꯑꯗꯨꯗ ꯆꯠꯂꯨ꯫"),
        ("Sit here.", "ꯑꯁꯤꯗ ꯐꯝꯎ꯫"),
        ("Stand up.", "ꯂꯦꯞꯂꯨ꯫"),
        ("Be quiet.", "ꯀꯥꯡꯂꯣꯟ ꯁꯤꯟꯅꯨ꯫"),
    ],
},

# ━━━ 654: Communicative Approach ━━━
654: {
    "heading": "Learn Meitei by Communicative Approach",
    "rows": [
        ("Listen carefully.", "ꯆꯦꯛꯁꯤꯟꯅ ꯇꯥꯕꯤꯌꯨ꯫"),
        ("Repeat after me.", "ꯑꯩꯒꯤ ꯃꯇꯨꯡꯗ ꯍꯥꯏꯕꯤꯌꯨ꯫"),
        ("Say it again.", "ꯑꯃꯨꯛ ꯍꯟꯅ ꯍꯥꯏꯕꯤꯌꯨ꯫"),
        ("How do you say this in Meitei?", "ꯃꯁꯤꯕꯨ ꯃꯩꯇꯩ ꯂꯣꯟꯗ ꯀꯔꯝꯅ ꯍꯥꯏꯕꯅꯣ?"),
        ("What does this word mean?", "ꯋꯥꯍꯩ ꯑꯁꯤꯒꯤ ꯋꯥꯍꯡꯊꯣꯛ ꯀꯔꯤꯅꯣ?"),
        ("I did not understand.", "ꯑꯩ ꯈꯉꯖꯈꯤꯗꯦ꯫"),
        ("Please explain.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯈꯉꯍꯟꯕꯤꯌꯨ꯫"),
        ("Practice every day.", "ꯅꯨꯃꯤꯠ ꯈꯨꯗꯤꯡ ꯄ꯭ꯔꯦꯛꯇꯤꯁ ꯇꯧꯕꯤꯌꯨ꯫"),
        ("Read this sentence.", "ꯋꯥꯍꯩ ꯑꯁꯤ ꯄꯥꯕꯤꯌꯨ꯫"),
        ("Write this sentence.", "ꯋꯥꯍꯩ ꯑꯁꯤ ꯏꯕꯤꯌꯨ꯫"),
        ("Speak with your friends.", "ꯅꯈꯣꯏꯒꯤ ꯃꯔꯨꯞꯁꯤꯡꯒ ꯋꯥ ꯉꯥꯡꯕꯤꯌꯨ꯫"),
        ("Do not be afraid to make mistakes.", "ꯑꯆꯨꯝꯗꯕ ꯇꯧꯕꯗ ꯀꯤꯅꯨ꯫"),
        ("You are improving.", "ꯅꯈꯣꯏ ꯐꯖꯅ ꯆꯠꯂꯤ꯫"),
        ("Very good!", "ꯌꯥꯝꯅ ꯐꯖꯩ!"),
        ("Try once more.", "ꯑꯃꯨꯛ ꯍꯟꯅ ꯍꯣꯠꯅꯕꯤꯌꯨ꯫"),
        ("You did great.", "ꯅꯈꯣꯏ ꯐꯕ ꯇꯧꯔꯦ꯫"),
        ("Keep learning.", "ꯇꯝꯅ ꯆꯠꯃꯤꯟꯅꯕꯤꯌꯨ꯫"),
    ],
},

# ━━━ 655: Sentences practice 1 ━━━
655: {
    "heading": "Simple sentence practice – 1",
    "rows": [
        ("The sun rises in the east.", "ꯅꯨꯃꯤꯠ ꯃꯅꯤꯡ ꯊꯣꯡꯗꯒꯤ ꯊꯣꯛꯏ꯫"),
        ("Birds fly in the sky.", "ꯎꯆꯦꯛꯁꯤꯡ ꯑꯇꯤꯌꯥꯗ ꯄꯥꯝꯏ꯫"),
        ("The river flows.", "ꯇꯨꯔꯦꯟ ꯆꯠꯏ꯫"),
        ("Children play in the field.", "ꯑꯉꯥꯡꯁꯤꯡ ꯃꯐꯝꯗ ꯁꯥꯏ꯫"),
        ("Mother cooks food.", "ꯏꯃꯥ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯏ꯫"),
        ("Father goes to work.", "ꯏꯄꯥ ꯊꯧꯔꯝꯗ ꯆꯠꯏ꯫"),
        ("I drink water.", "ꯑꯩ ꯏꯁꯤꯡ ꯊꯛꯏ꯫"),
        ("She reads a book.", "ꯃꯍꯥꯛ ꯂꯥꯏꯔꯤꯛ ꯄꯥꯏ꯫"),
        ("He writes a letter.", "ꯃꯍꯥꯛ ꯆꯤꯠꯊꯤ ꯏꯏ꯫"),
        ("We go to school.", "ꯑꯩꯈꯣꯏ ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯏ꯫"),
        ("The dog is sleeping.", "ꯍꯨꯏ ꯇꯨꯝꯔꯤ꯫"),
        ("The cat drinks milk.", "ꯍꯧꯗꯣꯡ ꯁꯉꯣꯝ ꯊꯛꯏ꯫"),
        ("It is very cold.", "ꯌꯥꯝꯅ ꯑꯏꯡꯏ꯫"),
        ("The flowers are beautiful.", "ꯂꯩꯁꯤꯡ ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("I am eating rice.", "ꯑꯩ ꯆꯦꯡ ꯆꯥꯔꯤ꯫"),
        ("They are coming.", "ꯃꯈꯣꯏ ꯂꯥꯛꯔꯤ꯫"),
        ("The moon is bright.", "ꯊꯥ ꯊꯣꯏꯅ ꯊꯣꯛꯂꯤ꯫"),
    ],
},

# ━━━ 656: Prepositions practice ━━━
656: {
    "heading": "Prepositions practice session",
    "rows": [
        ("The book is on the table.", "ꯂꯥꯏꯔꯤꯛ ꯇꯦꯕꯜ ꯃꯊꯛꯇ ꯂꯩꯔꯤ꯫"),
        ("The cat is under the bed.", "ꯍꯧꯗꯣꯡ ꯐꯤꯔꯥꯜ ꯃꯈꯥꯗ ꯂꯩꯔꯤ꯫"),
        ("He is standing behind me.", "ꯃꯍꯥꯛ ꯑꯩꯒꯤ ꯃꯇꯨꯡꯗ ꯂꯦꯞꯔꯤ꯫"),
        ("She sits in front of me.", "ꯃꯍꯥꯛ ꯑꯩꯒꯤ ꯃꯃꯥꯡꯗ ꯐꯝꯔꯤ꯫"),
        ("The ball is between the chairs.", "ꯕꯣꯜ ꯑꯁꯤ ꯐꯝꯐꯝ ꯑꯅꯤꯒꯤ ꯃꯔꯛꯇ ꯂꯩꯔꯤ꯫"),
        ("I am going to the market.", "ꯑꯩ ꯀꯩꯊꯦꯜꯗ ꯆꯠꯂꯤ꯫"),
        ("He comes from Imphal.", "ꯃꯍꯥꯛ ꯏꯝꯐꯥꯜꯗꯒꯤ ꯂꯥꯛꯏ꯫"),
        ("The pen is inside the box.", "ꯄꯦꯟ ꯎꯄꯨ ꯃꯅꯨꯡꯗ ꯂꯩꯔꯤ꯫"),
        ("Go out of the room.", "ꯀꯥꯗꯒꯤ ꯃꯄꯥꯟꯗ ꯊꯣꯛꯂꯨ꯫"),
        ("The school is near the temple.", "ꯁ꯭ꯀꯨꯜ ꯂꯥꯏꯁꯡꯒꯤ ꯑꯅꯥꯛꯇꯗ ꯂꯩ꯫"),
        ("My house is far from here.", "ꯑꯩꯒꯤ ꯌꯨꯝ ꯑꯁꯤꯗꯒꯤ ꯊꯥꯞꯅ ꯂꯩ꯫"),
        ("Walk along the road.", "ꯂꯝꯕꯤ ꯇꯨꯝꯅ ꯆꯠꯂꯨ꯫"),
        ("Sit beside me.", "ꯑꯩꯒꯤ ꯃꯅꯥꯛꯇ ꯐꯝꯎ꯫"),
        ("The tree is above the house.", "ꯎꯄꯟ ꯌꯨꯝꯒꯤ ꯃꯊꯛꯇ ꯂꯩꯔꯤ꯫"),
        ("Keep it below the table.", "ꯇꯦꯕꯜꯒꯤ ꯃꯈꯥꯗ ꯊꯝꯎ꯫"),
        ("He walked across the bridge.", "ꯃꯍꯥꯛ ꯐꯨꯡꯒꯥ ꯂꯣꯟꯈꯤ꯫"),
        ("The bird is on the tree.", "ꯎꯆꯦꯛ ꯎꯄꯟ ꯃꯊꯛꯇ ꯂꯩꯔꯤ꯫"),
    ],
},

# ━━━ 657: Jokes ━━━
657: {
    "heading": "Meitei jokes – Learn in a fun way",
    "rows": [
        ("Why did you come late?", "ꯅꯈꯣꯏ ꯀꯔꯤꯒꯤꯗꯃꯛ ꯑꯊꯦꯡ ꯂꯥꯛꯈꯤꯕꯅꯣ?"),
        ("The bus was late, sir.", "ꯕꯁ ꯑꯊꯦꯡ ꯇꯥꯈꯤ, ꯁꯔ꯫"),
        ("Why did the chicken cross the road?", "ꯌꯦꯟ ꯀꯔꯤꯒꯤꯗꯃꯛ ꯂꯝꯕꯤ ꯂꯣꯟꯈꯤꯕꯅꯣ?"),
        ("To get to the other side!", "ꯑꯇꯣꯞꯄ ꯃꯄꯥꯛꯇ ꯆꯠꯅꯕꯅꯤ!"),
        ("Teacher, I lost my homework.", "ꯎꯖꯥꯕ, ꯑꯩꯒꯤ ꯌꯨꯝꯒꯤ ꯊꯧꯔꯝ ꯃꯥꯡꯈꯤ꯫"),
        ("Did the dog eat it?", "ꯍꯨꯏꯅ ꯆꯥꯈꯤꯕꯔꯥ?"),
        ("I have no dog!", "ꯑꯩꯒꯤ ꯍꯨꯏ ꯂꯩꯇꯦ!"),
        ("What is faster, hot or cold?", "ꯈ꯭ꯋꯥꯏꯗꯒꯤ ꯊꯨꯟꯕ ꯀꯔꯤꯅꯣ, ꯑꯁꯥꯕ ꯅꯠꯔꯒ ꯑꯏꯡꯕ?"),
        ("Hot, because you can catch cold!", "ꯑꯁꯥꯕ, ꯃꯔꯃꯗꯤ ꯑꯏꯡꯕ ꯐꯥꯡꯕ ꯌꯥꯏ!"),
        ("Why is six afraid of seven?", "ꯇꯔꯨꯛ ꯀꯔꯤꯒꯤꯗꯃꯛ ꯇꯔꯦꯠꯕꯨ ꯀꯤꯕꯅꯣ?"),
        ("Because seven ate nine!", "ꯃꯔꯃꯗꯤ ꯇꯔꯦꯠꯅ ꯃꯥꯄꯜ ꯆꯥꯈꯤ!"),
        ("What did one wall say to the other?", "ꯕꯥꯔꯤ ꯑꯃꯅ ꯑꯇꯣꯞꯄꯗ ꯀꯔꯤ ꯍꯥꯏꯈꯤꯕꯅꯣ?"),
        ("I will meet you at the corner!", "ꯀꯣꯟꯗ ꯎꯅꯒꯅꯤ!"),
        ("My brother talks in his sleep.", "ꯏꯅꯥꯎ ꯇꯨꯝꯕ ꯃꯇꯝꯗ ꯋꯥ ꯉꯥꯡꯏ꯫"),
        ("That is okay, he never talks when awake!", "ꯃꯁꯤ ꯐꯖꯩ, ꯊꯥꯎꯈꯤꯕ ꯃꯇꯝꯗ ꯀꯩꯗꯧꯡꯗ ꯋꯥ ꯉꯥꯡꯗꯦ!"),
        ("Laughter is the best medicine.", "ꯅꯣꯛꯄ ꯑꯁꯤ ꯈ꯭ꯋꯥꯏꯗꯒꯤ ꯐꯕ ꯍꯤꯗꯥꯛꯅꯤ꯫"),
        ("Laugh more, worry less.", "ꯑꯃꯨꯛ ꯅꯣꯛꯎ, ꯈꯟꯅ ꯍꯟꯊꯎ꯫"),
    ],
},

# ━━━ 658: Daily reading – jokes, thoughts, quotes ━━━
658: {
    "heading": "Daily reading – jokes, thoughts, quotes",
    "rows": [
        ("Knowledge is power.", "ꯈꯉꯕ ꯑꯁꯤ ꯄꯥꯋꯔꯅꯤ꯫"),
        ("Hard work brings success.", "ꯍꯣꯠꯅꯕꯅ ꯃꯥꯏꯄꯥꯛꯄ ꯄꯨꯔꯛꯏ꯫"),
        ("Never give up.", "ꯀꯩꯗꯧꯡꯗ ꯊꯥꯗꯣꯛꯅꯨ꯫"),
        ("Today is a beautiful day.", "ꯉꯁꯤ ꯐꯖꯕ ꯅꯨꯃꯤꯠꯅꯤ꯫"),
        ("Be kind to everyone.", "ꯃꯤꯄꯨꯝꯗ ꯐꯕ ꯑꯣꯏꯕꯤꯌꯨ꯫"),
        ("Time is precious.", "ꯃꯇꯝ ꯑꯁꯤ ꯃꯃꯜ ꯌꯥꯝꯏ꯫"),
        ("A friend in need is a friend indeed.", "ꯃꯊꯧ ꯇꯥꯕ ꯃꯇꯝꯒꯤ ꯃꯔꯨꯞ ꯑꯁꯤ ꯑꯆꯨꯝꯕ ꯃꯔꯨꯞꯅꯤ꯫"),
        ("The early bird catches the worm.", "ꯉꯟꯅ ꯊꯥꯎꯈꯤꯕ ꯎꯆꯦꯛꯅ ꯇꯤꯟꯊꯣꯛ ꯐꯡꯏ꯫"),
        ("Health is wealth.", "ꯍꯛꯆꯥꯡ ꯐꯕ ꯑꯁꯤ ꯂꯨꯄꯥꯅꯤ꯫"),
        ("Honesty is the best policy.", "ꯑꯆꯨꯝꯕ ꯑꯣꯏꯕ ꯑꯁꯤ ꯈ꯭ꯋꯥꯏꯗꯒꯤ ꯐꯕ ꯂꯝꯕꯤꯅꯤ꯫"),
        ("Respect your elders.", "ꯅꯈꯣꯏꯒꯤ ꯑꯅꯥꯕꯁꯤꯡꯕꯨ ꯏꯀꯥꯏ ꯈꯨꯝꯅꯕꯤꯌꯨ꯫"),
        ("Education opens doors.", "ꯇꯝꯕꯅ ꯊꯣꯡ ꯍꯥꯡꯏ꯫"),
        ("Love your motherland.", "ꯅꯈꯣꯏꯒꯤ ꯏꯃꯥ ꯂꯩꯄꯥꯛꯕꯨ ꯅꯨꯡꯁꯤꯕꯤꯌꯨ꯫"),
        ("Every day is a new beginning.", "ꯅꯨꯃꯤꯠ ꯈꯨꯗꯤꯡ ꯑꯍꯥꯟꯕ ꯃꯇꯝꯅꯤ꯫"),
        ("Where there is a will, there is a way.", "ꯄꯥꯝꯕ ꯂꯩꯔꯕꯗꯤ ꯂꯝꯕꯤ ꯂꯩ꯫"),
        ("Smile and the world smiles with you.", "ꯅꯣꯛꯄꯤꯌꯨ, ꯃꯥꯂꯦꯝ ꯄꯨꯝꯕ ꯅꯈꯣꯏꯒ ꯅꯣꯛꯀꯅꯤ꯫"),
        ("Dream big, work hard.", "ꯑꯆꯧꯕ ꯃꯡ ꯃꯥꯡꯕꯤꯌꯨ, ꯍꯣꯠꯅ ꯊꯧꯔꯝ ꯇꯧꯕꯤꯌꯨ꯫"),
    ],
},

# ━━━ 659: Social Media ━━━
659: {
    "heading": "Experience with Social Media",
    "rows": [
        ("I use social media every day.", "ꯑꯩ ꯁꯣꯁꯤꯌꯜ ꯃꯤꯗꯤꯌꯥ ꯅꯨꯃꯤꯠ ꯈꯨꯗꯤꯡ ꯁꯤꯖꯤꯟꯅꯏ꯫"),
        ("I posted a photo today.", "ꯑꯩ ꯉꯁꯤ ꯐꯣꯇꯣ ꯑꯃ ꯄꯣꯁ꯭ꯠ ꯇꯧꯈꯤ꯫"),
        ("How many likes did you get?", "ꯂꯥꯏꯛ ꯀꯌꯥ ꯐꯡꯈꯤꯕꯅꯣ?"),
        ("I got hundred likes.", "ꯑꯩ ꯂꯥꯏꯛ ꯆꯥ ꯑꯃ ꯐꯡꯈꯤ꯫"),
        ("That video went viral.", "ꯚꯤꯗꯤꯑꯣ ꯑꯗꯨ ꯚꯥꯏꯔꯜ ꯑꯣꯏꯈꯤ꯫"),
        ("I follow many pages.", "ꯑꯩ ꯄꯦꯖ ꯃꯌꯥꯝ ꯐꯣꯂꯣ ꯇꯧꯏ꯫"),
        ("Do not share fake news.", "ꯐꯦꯛ ꯅꯤꯎꯖ ꯁꯩꯅꯅꯨ꯫"),
        ("Be careful online.", "ꯑꯣꯟꯂꯥꯏꯟꯗ ꯆꯦꯛꯁꯤꯟꯅ ꯂꯩꯕꯤꯌꯨ꯫"),
        ("I made a new friend online.", "ꯑꯩ ꯑꯣꯟꯂꯥꯏꯟꯗ ꯃꯔꯨꯞ ꯑꯍꯥꯟꯕ ꯑꯃ ꯁꯦꯝꯈꯤ꯫"),
        ("Do not spend too much time.", "ꯃꯇꯝ ꯌꯥꯝꯅ ꯀꯠꯊꯅꯨ꯫"),
        ("I share my thoughts there.", "ꯑꯩ ꯑꯗꯨꯗ ꯑꯩꯒꯤ ꯋꯥꯈꯜ ꯁꯩꯅꯏ꯫"),
        ("Social media connects people.", "ꯁꯣꯁꯤꯌꯜ ꯃꯤꯗꯤꯌꯥꯅ ꯃꯤꯑꯣꯏꯁꯤꯡ ꯄꯨꯟꯁꯤꯟꯏ꯫"),
        ("I watched a cooking video.", "ꯑꯩ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯕꯒꯤ ꯚꯤꯗꯤꯑꯣ ꯌꯦꯡꯈꯤ꯫"),
        ("My profile has many followers.", "ꯑꯩꯒꯤ ꯄ꯭ꯔꯣꯐꯥꯏꯜꯗ ꯐꯣꯂꯣꯋꯔ ꯃꯌꯥꯝ ꯂꯩ꯫"),
        ("I deactivated my account.", "ꯑꯩ ꯑꯩꯒꯤ ꯑꯦꯀꯥꯎꯟꯠ ꯗꯤꯑꯦꯛꯇꯤꯚꯦꯠ ꯇꯧꯈꯤ꯫"),
        ("I prefer talking in person.", "ꯑꯩ ꯃꯤꯑꯣꯏꯒ ꯎꯅꯅ ꯋꯥ ꯉꯥꯡꯕ ꯅꯨꯡꯁꯤ꯫"),
        ("Use social media wisely.", "ꯁꯣꯁꯤꯌꯜ ꯃꯤꯗꯤꯌꯥ ꯑꯆꯨꯝꯕꯅ ꯁꯤꯖꯤꯟꯅꯕꯤꯌꯨ꯫"),
    ],
},

# ━━━ 660: Eclipse conversation ━━━
660: {
    "heading": "Conversation about the eclipse",
    "rows": [
        ("There is a solar eclipse today.", "ꯉꯁꯤ ꯅꯨꯃꯤꯠ ꯂꯨꯡꯕ ꯂꯩꯔꯤ꯫"),
        ("Do not look at the sun directly.", "ꯅꯨꯃꯤꯠ ꯑꯆꯨꯝꯕ ꯌꯦꯡꯅꯨ꯫"),
        ("Use special glasses.", "ꯃꯤꯠꯊꯨꯝ ꯑꯈꯟꯅꯕ ꯁꯤꯖꯤꯟꯅꯕꯤꯌꯨ꯫"),
        ("The moon covers the sun.", "ꯊꯥꯅ ꯅꯨꯃꯤꯠꯕꯨ ꯀꯣꯛꯏ꯫"),
        ("It is getting dark.", "ꯑꯃꯝꯕ ꯑꯣꯏꯔꯤ꯫"),
        ("This is amazing to watch.", "ꯃꯁꯤ ꯌꯦꯡꯕ ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("The eclipse lasts a few minutes.", "ꯅꯨꯃꯤꯠ ꯂꯨꯡꯕ ꯃꯤꯅꯤꯠ ꯈꯔ ꯆꯠꯏ꯫"),
        ("People are gathered outside.", "ꯃꯤꯑꯣꯏꯁꯤꯡ ꯃꯄꯥꯟꯗ ꯄꯨꯟꯈꯤ꯫"),
        ("A lunar eclipse happens at night.", "ꯊꯥ ꯂꯨꯡꯕ ꯑꯍꯤꯡꯗ ꯑꯣꯏ꯫"),
        ("It is a natural phenomenon.", "ꯃꯁꯤ ꯃꯁꯛ ꯃꯅꯥꯒꯤ ꯑꯣꯏꯕꯅꯤ꯫"),
        ("Did you see the eclipse?", "ꯅꯈꯣꯏ ꯅꯨꯃꯤꯠ ꯂꯨꯡꯕ ꯌꯦꯡꯈꯤꯕꯔꯥ?"),
        ("Yes, it was spectacular.", "ꯍꯣꯏ, ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("I took a photo of the eclipse.", "ꯑꯩ ꯅꯨꯃꯤꯠ ꯂꯨꯡꯕꯒꯤ ꯐꯣꯇꯣ ꯂꯧꯈꯤ꯫"),
        ("The next eclipse is in December.", "ꯑꯇꯣꯞꯄ ꯅꯨꯃꯤꯠ ꯂꯨꯡꯕ ꯗꯤꯁꯦꯝꯕꯔꯗꯅꯤ꯫"),
        ("Science explains eclipses.", "ꯁꯥꯏꯟꯁꯅ ꯅꯨꯃꯤꯠ ꯂꯨꯡꯕ ꯈꯉꯍꯟꯏ꯫"),
        ("It was my first eclipse.", "ꯃꯁꯤ ꯑꯩꯒꯤ ꯑꯍꯥꯅꯕ ꯅꯨꯃꯤꯠ ꯂꯨꯡꯕꯅꯤ꯫"),
        ("I am excited to see one.", "ꯑꯩ ꯌꯦꯡꯕ ꯌꯥꯝꯅ ꯄꯥꯝꯅꯩ꯫"),
    ],
},

# ━━━ 661: International Women's Day ━━━
661: {
    "heading": "International Women's Day",
    "rows": [
        ("Happy Women's Day!", "ꯅꯨꯄꯤꯒꯤ ꯅꯨꯃꯤꯠꯀꯤ ꯌꯥꯏꯐ ꯐꯕ ꯄꯤꯔꯛꯄꯤꯌꯨ!"),
        ("Today is 8th March.", "ꯉꯁꯤ ꯃꯥꯔ꯭ꯆ ꯅꯤꯄꯥꯜꯅꯤ꯫"),
        ("Women are strong.", "ꯅꯨꯄꯤꯁꯤꯡ ꯑꯀꯟꯕꯅꯤ꯫"),
        ("We respect all women.", "ꯑꯩꯈꯣꯏ ꯅꯨꯄꯤ ꯄꯨꯝꯕꯕꯨ ꯏꯀꯥꯏ ꯈꯨꯝꯅꯏ꯫"),
        ("Women can do anything.", "ꯅꯨꯄꯤꯁꯤꯡ ꯀꯔꯤꯁꯨ ꯇꯧꯕ ꯌꯥꯏ꯫"),
        ("My mother is my hero.", "ꯑꯩꯒꯤ ꯏꯃꯥ ꯑꯩꯒꯤ ꯍꯤꯔꯣꯅꯤ꯫"),
        ("Education is important for girls.", "ꯅꯨꯄꯤ ꯃꯆꯥꯒꯤꯗꯃꯛ ꯇꯝꯕ ꯃꯔꯨꯑꯣꯏꯅꯤ꯫"),
        ("Manipuri women are very talented.", "ꯃꯅꯤꯄꯨꯔꯤ ꯅꯨꯄꯤꯁꯤꯡ ꯌꯥꯝꯅ ꯊꯧꯅ ꯂꯩꯕꯅꯤ꯫"),
        ("She won the award.", "ꯃꯍꯥꯛ ꯑꯋꯥꯔ꯭ꯗ ꯃꯥꯏꯈꯤ꯫"),
        ("Let us celebrate women.", "ꯅꯨꯄꯤꯁꯤꯡꯕꯨ ꯄꯥꯡꯊꯣꯛꯁꯤ꯫"),
        ("Girls should study.", "ꯅꯨꯄꯤ ꯃꯆꯥꯁꯤꯡ ꯇꯝꯒꯗꯕꯅꯤ꯫"),
        ("Women deserve equal rights.", "ꯅꯨꯄꯤꯁꯤꯡ ꯑꯃꯠꯇ ꯍꯛ ꯐꯡꯒꯗꯕꯅꯤ꯫"),
        ("I admire strong women.", "ꯑꯩ ꯑꯀꯟꯕ ꯅꯨꯄꯤꯁꯤꯡꯕꯨ ꯏꯀꯥꯏ ꯈꯨꯝꯅꯩ꯫"),
        ("Thank you, mother.", "ꯊꯥꯒꯠꯆꯔꯤ, ꯏꯃꯥ꯫"),
        ("You are an inspiration.", "ꯅꯈꯣꯏ ꯊꯧꯒꯠꯍꯟꯕ ꯃꯤꯑꯣꯏꯅꯤ꯫"),
        ("We support women's empowerment.", "ꯑꯩꯈꯣꯏ ꯅꯨꯄꯤꯒꯤ ꯑꯀꯟꯕ ꯁꯞꯣꯔ꯭ꯠ ꯇꯧꯏ꯫"),
        ("Proud to be a woman.", "ꯅꯨꯄꯤ ꯑꯣꯏꯕꯗ ꯆꯥꯎꯊꯣꯛꯏ꯫"),
    ],
},

# ━━━ 662: Quarrel at home ━━━
662: {
    "heading": "Quarrel at home conversation",
    "rows": [
        ("Why are you shouting?", "ꯅꯈꯣꯏ ꯀꯔꯤꯒꯤꯗꯃꯛ ꯀꯥꯡꯂꯣꯟ ꯇꯧꯔꯤꯕꯅꯣ?"),
        ("I am not shouting.", "ꯑꯩ ꯀꯥꯡꯂꯣꯟ ꯇꯧꯗꯦ꯫"),
        ("You never listen to me.", "ꯅꯈꯣꯏ ꯑꯩꯒꯤ ꯋꯥ ꯀꯩꯗꯧꯡꯗ ꯇꯥꯗꯦ꯫"),
        ("I always listen.", "ꯑꯩ ꯃꯇꯝ ꯄꯨꯝꯕꯗ ꯇꯥꯏ꯫"),
        ("You broke my cup.", "ꯅꯈꯣꯏ ꯑꯩꯒꯤ ꯀꯞ ꯉꯥꯛꯈꯤ꯫"),
        ("I am sorry, it was an accident.", "ꯄꯨꯛꯅꯤꯡ ꯆꯥꯏ, ꯈꯉꯗꯅ ꯑꯣꯏꯈꯤꯕꯅꯤ꯫"),
        ("Do not fight.", "ꯈꯨꯟꯅꯥꯏ ꯇꯧꯅꯨ꯫"),
        ("Please forgive me.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯑꯩꯕꯨ ꯀꯣꯛꯍꯟꯄꯤꯌꯨ꯫"),
        ("I did not mean it.", "ꯑꯩꯅ ꯈꯉꯗꯅ ꯇꯧꯈꯤꯕꯅꯤ꯫"),
        ("Let us talk calmly.", "ꯁꯦꯟꯅ ꯁꯦꯟꯅ ꯋꯥ ꯉꯥꯡꯁꯤ꯫"),
        ("Stop arguing.", "ꯋꯥꯈꯣꯟ ꯇꯧꯕ ꯅꯥꯠꯄꯤꯌꯨ꯫"),
        ("I was wrong.", "ꯑꯩ ꯑꯆꯨꯝꯗꯦ꯫"),
        ("You were right.", "ꯅꯈꯣꯏ ꯑꯆꯨꯝꯕꯅꯤ꯫"),
        ("Let us not quarrel.", "ꯈꯨꯟꯅꯥꯏ ꯇꯧꯅꯗꯕꯅꯤ꯫"),
        ("Family is important.", "ꯏꯃꯨꯡ ꯃꯅꯨꯡ ꯃꯔꯨꯑꯣꯏꯅꯤ꯫"),
        ("I love you all.", "ꯑꯩ ꯅꯈꯣꯏ ꯃꯤꯄꯨꯝꯕꯨ ꯅꯨꯡꯁꯤ꯫"),
        ("Let us eat together.", "ꯂꯣꯏꯅꯅ ꯆꯤꯟꯖꯥꯛ ꯆꯥꯁꯤ꯫"),
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
    sys.stdout.buffer.write(f"Updated {updated} conversation lessons (642-662) in data_meitei.json\n".encode("utf-8"))

if __name__ == "__main__":
    main()
