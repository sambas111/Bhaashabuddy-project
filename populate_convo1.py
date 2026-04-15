#!/usr/bin/env python3
"""Populate conversation lessons 620-641 (5.1-5.22) with topic-relevant sentences."""
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

# ━━━ 620: Diwali Festival ━━━
620: {
    "heading": "Diwali Festival sentences",
    "rows": [
        ("Happy Diwali!", "ꯗꯤꯋꯥꯂꯤꯒꯤ ꯌꯥꯏꯐ ꯐꯕ ꯄꯤꯔꯛꯄꯤꯌꯨ!"),
        ("Diwali is the festival of lights.", "ꯗꯤꯋꯥꯂꯤ ꯑꯁꯤ ꯃꯩꯒꯤ ꯊꯧꯔꯝꯅꯤ꯫"),
        ("We light lamps on Diwali.", "ꯑꯩꯈꯣꯏ ꯗꯤꯋꯥꯂꯤꯗ ꯃꯩꯆꯥꯛ ꯊꯥꯏ꯫"),
        ("Children burst firecrackers.", "ꯑꯉꯥꯡꯁꯤꯡ ꯐꯠꯐꯠ ꯊꯥꯏ꯫"),
        ("We clean our house before Diwali.", "ꯗꯤꯋꯥꯂꯤꯒꯤ ꯃꯃꯥꯡꯗ ꯑꯩꯈꯣꯏ ꯌꯨꯝ ꯁꯦꯡꯗꯣꯛꯏ꯫"),
        ("Mother makes sweets.", "ꯏꯃꯥ ꯑꯊꯨꯝꯕ ꯁꯥꯏ꯫"),
        ("We wear new clothes.", "ꯑꯩꯈꯣꯏ ꯑꯍꯥꯟꯕ ꯐꯤ ꯁꯦꯠꯏ꯫"),
        ("Diwali is celebrated in October or November.", "ꯗꯤꯋꯥꯂꯤ ꯑꯁꯤ ꯑꯣꯛꯇꯣꯕꯔ ꯅꯠꯔꯒ ꯅꯚꯦꯝꯕꯔꯗ ꯄꯥꯡꯊꯣꯛꯏ꯫"),
        ("People pray to Goddess Lakshmi.", "ꯃꯤꯑꯣꯏꯁꯤꯡ ꯂꯛꯁ꯭ꯃꯤꯗ ꯈꯨꯔꯨꯝꯖꯔꯤ꯫"),
        ("We decorate our house with lights.", "ꯑꯩꯈꯣꯏ ꯌꯨꯝ ꯃꯩꯅ ꯁꯖꯤꯟꯏ꯫"),
        ("I love Diwali very much.", "ꯑꯩ ꯗꯤꯋꯥꯂꯤꯕꯨ ꯌꯥꯝꯅ ꯅꯨꯡꯁꯤ꯫"),
        ("We share sweets with neighbours.", "ꯑꯩꯈꯣꯏ ꯌꯨꯝꯊꯡꯒꯤ ꯃꯤꯑꯣꯏꯁꯤꯡꯒ ꯑꯊꯨꯝꯕ ꯁꯩꯅꯏ꯫"),
        ("Rangoli looks beautiful.", "ꯔꯉꯒꯣꯂꯤ ꯑꯁꯤ ꯐꯖꯏ꯫"),
        ("This is my favourite festival.", "ꯃꯁꯤ ꯑꯩꯒꯤ ꯅꯨꯡꯁꯤꯠꯄ ꯊꯧꯔꯝꯅꯤ꯫"),
        ("The night sky looks bright.", "ꯑꯍꯤꯡꯒꯤ ꯑꯇꯤꯌꯥ ꯌꯥꯝꯅ ꯊꯣꯏꯅ ꯎꯏ꯫"),
        ("We visit our relatives.", "ꯑꯩꯈꯣꯏ ꯑꯩꯈꯣꯏꯒꯤ ꯏꯅꯗꯣꯝꯁꯤꯡꯗ ꯆꯠꯏ꯫"),
        ("Diwali brings happiness.", "ꯗꯤꯋꯥꯂꯤꯅ ꯍꯔꯥꯎ ꯄꯨꯔꯛꯏ꯫"),
    ],
},

# ━━━ 621: Introduction / Salutation ━━━
621: {
    "heading": "Introduction & Salutation sentences",
    "rows": [
        ("Hello!", "ꯍꯦꯜꯂꯣ!"),
        ("Good morning.", "ꯑꯌꯨꯛꯀꯤ ꯅꯨꯃꯤꯗꯥꯡ꯫"),
        ("How are you?", "ꯅꯈꯣꯏ ꯀꯝꯗꯧꯔꯤ?"),
        ("I am fine.", "ꯑꯩ ꯐꯖꯩ꯫"),
        ("What is your name?", "ꯅꯈꯣꯏꯒꯤ ꯃꯃꯤꯡ ꯀꯔꯤꯅꯣ?"),
        ("My name is Tomba.", "ꯑꯩꯒꯤ ꯃꯃꯤꯡ ꯇꯣꯝꯕꯅꯤ꯫"),
        ("Where are you from?", "ꯅꯈꯣꯏ ꯀꯗꯥꯏꯗꯒꯤꯅꯣ?"),
        ("I am from Imphal.", "ꯑꯩ ꯏꯝꯐꯥꯜꯗꯒꯤꯅꯤ꯫"),
        ("Nice to meet you.", "ꯅꯈꯣꯏꯒ ꯎꯅꯕ ꯐꯖꯩ꯫"),
        ("Welcome!", "ꯑꯣꯛꯆꯔꯤ!"),
        ("Please sit down.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯐꯝꯕꯤꯌꯨ꯫"),
        ("Thank you.", "ꯊꯥꯒꯠꯆꯔꯤ꯫"),
        ("Goodbye.", "ꯅꯨꯡꯁꯤꯠꯅ ꯆꯠꯃꯤꯟꯅꯕꯤꯌꯨ꯫"),
        ("See you again.", "ꯑꯃꯨꯛ ꯎꯅꯒꯅꯤ꯫"),
        ("How old are you?", "ꯅꯈꯣꯏꯒꯤ ꯆꯍꯤ ꯀꯌꯥꯅꯣ?"),
        ("I am twenty years old.", "ꯑꯩꯒꯤ ꯆꯍꯤ ꯀꯨꯜꯅꯤ꯫"),
        ("What do you do?", "ꯅꯈꯣꯏ ꯀꯔꯤ ꯇꯧꯔꯤꯕꯅꯣ?"),
    ],
},

# ━━━ 622: Time Related ━━━
622: {
    "heading": "Time related sentences",
    "rows": [
        ("What time is it?", "ꯍꯧꯖꯤꯛ ꯄꯨꯡ ꯀꯌꯥ ꯇꯥꯔꯛꯂꯤꯕꯅꯣ?"),
        ("It is ten o'clock.", "ꯍꯧꯖꯤꯛ ꯄꯨꯡ ꯇꯔꯥ ꯇꯥꯔꯛꯂꯤ꯫"),
        ("It is morning now.", "ꯍꯧꯖꯤꯛ ꯑꯌꯨꯛꯅꯤ꯫"),
        ("It is afternoon now.", "ꯍꯧꯖꯤꯛ ꯅꯨꯃꯤꯠ ꯌꯨꯡꯕꯅꯤ꯫"),
        ("It is evening.", "ꯍꯧꯖꯤꯛ ꯅꯨꯃꯗꯥꯡ ꯑꯣꯋꯥꯏꯔꯝꯅꯤ꯫"),
        ("It is night.", "ꯍꯧꯖꯤꯛ ꯑꯍꯤꯡꯅꯤ꯫"),
        ("Today is Monday.", "ꯉꯁꯤ ꯅꯣꯡꯃꯥꯏꯖꯤꯡꯅꯤ꯫"),
        ("Yesterday was Sunday.", "ꯉꯔꯥꯡ ꯅꯣꯡꯃꯄꯟꯕꯅꯤ꯫"),
        ("Tomorrow is Tuesday.", "ꯍꯌꯦꯡ ꯂꯩꯄꯥꯛꯄꯣꯛꯄꯅꯤ꯫"),
        ("What day is today?", "ꯉꯁꯤ ꯀꯔꯤ ꯅꯨꯃꯤꯠꯅꯣ?"),
        ("I woke up early today.", "ꯑꯩ ꯉꯁꯤ ꯉꯟꯅ ꯊꯥꯎꯈꯤ꯫"),
        ("I go to school at eight.", "ꯑꯩ ꯄꯨꯡ ꯅꯤꯄꯥꯜꯗ ꯁ꯭ꯀꯨꯜꯗ ꯆꯠꯏ꯫"),
        ("Lunch is at twelve.", "ꯅꯨꯃꯤꯗꯥꯡꯒꯤ ꯆꯤꯟꯖꯥꯛ ꯄꯨꯡ ꯇꯔꯥ ꯅꯤꯊꯣꯢꯗꯅꯤ꯫"),
        ("I sleep at ten at night.", "ꯑꯩ ꯑꯍꯤꯡ ꯄꯨꯡ ꯇꯔꯥꯗ ꯇꯨꯝꯏ꯫"),
        ("Come at five o'clock.", "ꯄꯨꯡ ꯃꯉꯥꯗ ꯂꯥꯛꯎ꯫"),
        ("It is getting late.", "ꯑꯊꯦꯡ ꯇꯥꯔꯛꯂꯤ꯫"),
        ("Wait for a moment.", "ꯈꯔ ꯂꯨꯕꯤꯌꯨ꯫"),
    ],
},

# ━━━ 623: Where / Place Related ━━━
623: {
    "heading": "Where / Place related sentences",
    "rows": [
        ("Where is the market?", "ꯀꯩꯊꯦꯜ ꯀꯗꯥꯏꯗꯅꯣ?"),
        ("The market is nearby.", "ꯀꯩꯊꯦꯜ ꯑꯁꯤ ꯑꯅꯥꯛꯇꯗ ꯂꯩ꯫"),
        ("Where do you live?", "ꯅꯈꯣꯏ ꯀꯗꯥꯏꯗ ꯂꯩꯔꯤꯕꯅꯣ?"),
        ("I live in Imphal.", "ꯑꯩ ꯏꯝꯐꯥꯜꯗ ꯂꯩꯔꯤ꯫"),
        ("Where is the hospital?", "ꯂꯝꯗꯝ ꯀꯗꯥꯏꯗꯅꯣ?"),
        ("The hospital is on the main road.", "ꯂꯝꯗꯝ ꯂꯝꯕꯤ ꯑꯆꯧꯕꯗ ꯂꯩ꯫"),
        ("Go straight ahead.", "ꯑꯆꯨꯝꯕ ꯆꯠꯂꯨ꯫"),
        ("Turn left.", "ꯁꯦꯡꯗ ꯀꯣꯟꯂꯨ꯫"),
        ("Turn right.", "ꯌꯦꯠꯗ ꯀꯣꯟꯂꯨ꯫"),
        ("It is far from here.", "ꯃꯁꯤ ꯑꯁꯤꯗꯒꯤ ꯊꯥꯞꯅ ꯂꯩ꯫"),
        ("It is very close.", "ꯃꯁꯤ ꯌꯥꯝꯅ ꯑꯅꯥꯛꯇꯗ ꯂꯩ꯫"),
        ("Where is the bus stop?", "ꯕꯁ ꯂꯦꯞꯐꯝ ꯀꯗꯥꯏꯗꯅꯣ?"),
        ("The temple is behind the school.", "ꯂꯥꯏꯁꯡ ꯑꯁꯤ ꯁ꯭ꯀꯨꯜꯒꯤ ꯃꯇꯨꯡꯗ ꯂꯩ꯫"),
        ("My house is near the river.", "ꯑꯩꯒꯤ ꯌꯨꯝ ꯇꯨꯔꯦꯟꯒꯤ ꯑꯅꯥꯛꯇꯗ ꯂꯩ꯫"),
        ("Where are you going?", "ꯅꯈꯣꯏ ꯀꯗꯥꯏꯗ ꯆꯠꯂꯤꯕꯅꯣ?"),
        ("I am going to the office.", "ꯑꯩ ꯑꯣꯐꯤꯁꯇ ꯆꯠꯂꯤ꯫"),
        ("This place is beautiful.", "ꯃꯐꯝ ꯑꯁꯤ ꯐꯖꯩ꯫"),
    ],
},

# ━━━ 624: In Hotel ━━━
624: {
    "heading": "Sentences in a Hotel",
    "rows": [
        ("Do you have a room available?", "ꯀꯥ ꯑꯃ ꯐꯡꯒꯗꯕ ꯂꯩꯕꯔꯥ?"),
        ("I want to book a room.", "ꯑꯩ ꯀꯥ ꯑꯃ ꯕꯨꯛ ꯇꯧꯅꯤꯡꯏ꯫"),
        ("How much is the room charge?", "ꯀꯥꯒꯤ ꯃꯃꯜ ꯀꯌꯥꯅꯣ?"),
        ("I need a room for two days.", "ꯑꯩ ꯅꯨꯃꯤꯠ ꯑꯅꯤꯒꯤꯗꯃꯛ ꯀꯥ ꯑꯃ ꯃꯊꯧ ꯇꯥꯏ꯫"),
        ("Please give me the key.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯁꯣ ꯄꯤꯕꯤꯌꯨ꯫"),
        ("Where is the dining hall?", "ꯆꯤꯟꯖꯥꯛ ꯆꯥꯐꯝ ꯀꯗꯥꯏꯗꯅꯣ?"),
        ("Please clean the room.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯀꯥ ꯁꯦꯡꯗꯣꯛꯄꯤꯌꯨ꯫"),
        ("The AC is not working.", "ꯑꯦꯁꯤ ꯆꯠꯇꯔꯤ꯫"),
        ("Please send hot water.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯏꯁꯤꯡ ꯐꯥꯕ ꯊꯥꯕꯤꯌꯨ꯫"),
        ("I want to check out.", "ꯑꯩ ꯆꯦꯛ ꯑꯥꯎꯠ ꯇꯧꯅꯤꯡꯏ꯫"),
        ("Can I have the bill?", "ꯕꯤꯜ ꯐꯡꯕ ꯌꯥꯕꯔꯥ?"),
        ("The food was delicious.", "ꯆꯤꯟꯖꯥꯛ ꯑꯁꯤ ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("Is breakfast included?", "ꯑꯌꯨꯛꯀꯤ ꯆꯤꯟꯖꯥꯛ ꯌꯥꯎꯔꯤꯕꯔꯥ?"),
        ("Where is the lift?", "ꯂꯤꯐ꯭ꯠ ꯀꯗꯥꯏꯗꯅꯣ?"),
        ("I need extra blankets.", "ꯑꯩ ꯀꯝꯕꯜ ꯑꯃꯨꯛ ꯃꯊꯧ ꯇꯥꯏ꯫"),
        ("The room is very nice.", "ꯀꯥ ꯑꯁꯤ ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("What time is checkout?", "ꯆꯦꯛ ꯑꯥꯎꯠ ꯄꯨꯡ ꯀꯌꯥꯗꯅꯣ?"),
    ],
},

# ━━━ 625: Weather related ━━━
625: {
    "heading": "Weather related sentences",
    "rows": [
        ("How is the weather today?", "ꯉꯁꯤ ꯅꯨꯡꯁꯤꯠ ꯀꯝꯗꯧꯔꯤ?"),
        ("It is very hot today.", "ꯉꯁꯤ ꯌꯥꯝꯅ ꯑꯁꯥꯏ꯫"),
        ("It is cold today.", "ꯉꯁꯤ ꯑꯏꯡꯏ꯫"),
        ("It is raining.", "ꯅꯣꯡ ꯁꯨꯏ꯫"),
        ("It might rain today.", "ꯉꯁꯤ ꯅꯣꯡ ꯁꯨꯒꯅꯤ꯫"),
        ("Take an umbrella.", "ꯁꯥꯇꯤꯟ ꯄꯨꯔꯛꯎ꯫"),
        ("The sky is cloudy.", "ꯑꯇꯤꯌꯥ ꯂꯥꯏꯆꯤꯜ ꯊꯥꯏ꯫"),
        ("The sun is shining.", "ꯅꯨꯃꯤꯠ ꯊꯣꯏꯅ ꯊꯣꯛꯂꯤ꯫"),
        ("There is fog in the morning.", "ꯑꯌꯨꯛꯇ ꯂꯥꯏꯆꯤꯜꯊꯥꯕ ꯂꯩꯔꯤ꯫"),
        ("The wind is blowing.", "ꯅꯨꯡꯁꯤꯠ ꯐꯩꯔꯤ꯫"),
        ("It is very pleasant.", "ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("Winter is coming.", "ꯋꯥꯡꯒꯣꯜ ꯂꯥꯛꯂꯤ꯫"),
        ("Summer is very hot here.", "ꯑꯁꯤꯗ ꯀꯨꯃ꯭ꯍꯩ ꯌꯥꯝꯅ ꯑꯁꯥꯏ꯫"),
        ("It stopped raining.", "ꯅꯣꯡ ꯅꯥꯠꯂꯦ꯫"),
        ("I like rainy season.", "ꯑꯩ ꯅꯣꯡꯒꯤ ꯃꯇꯝ ꯅꯨꯡꯁꯤ꯫"),
        ("There was a thunderstorm yesterday.", "ꯉꯔꯥꯡ ꯅꯣꯡꯊꯥꯡꯀꯨꯞꯄ ꯂꯩꯔꯝꯃꯤ꯫"),
        ("The weather is changing.", "ꯅꯨꯡꯁꯤꯠ ꯍꯣꯡꯗꯣꯛꯂꯤ꯫"),
    ],
},

# ━━━ 626: Traffic Police ━━━
626: {
    "heading": "Conversation with traffic police",
    "rows": [
        ("Show me your licence.", "ꯅꯈꯣꯏꯒꯤ ꯂꯥꯏꯁꯦꯟꯁ ꯎꯠꯄꯤꯌꯨ꯫"),
        ("Sir, here is my licence.", "ꯁꯔ, ꯑꯩꯒꯤ ꯂꯥꯏꯁꯦꯟꯁ ꯃꯁꯤꯅꯤ꯫"),
        ("You jumped the red light.", "ꯅꯈꯣꯏ ꯑꯉꯥꯡꯕ ꯃꯩ ꯂꯣꯟꯈꯤ꯫"),
        ("I am sorry, I did not see it.", "ꯄꯨꯛꯅꯤꯡ ꯆꯥꯏ, ꯑꯩ ꯌꯦꯡꯈꯤꯗꯦ꯫"),
        ("You were driving too fast.", "ꯅꯈꯣꯏ ꯌꯥꯝꯅ ꯊꯨꯅ ꯊꯨꯅ ꯆꯠꯈꯤ꯫"),
        ("Where is your helmet?", "ꯅꯈꯣꯏꯒꯤ ꯍꯦꯜꯃꯦꯠ ꯀꯗꯥꯏꯗꯅꯣ?"),
        ("I forgot it at home.", "ꯑꯩ ꯌꯨꯝꯗ ꯀꯥꯎꯊꯣꯛꯈꯤ꯫"),
        ("You have to pay a fine.", "ꯅꯈꯣꯏ ꯐꯥꯏꯟ ꯊꯤꯒꯗꯕꯅꯤ꯫"),
        ("How much is the fine?", "ꯐꯥꯏꯟ ꯀꯌꯥꯅꯣ?"),
        ("Please wear your seatbelt.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯁꯤꯠꯕꯦꯜꯠ ꯁꯦꯠꯄꯤꯌꯨ꯫"),
        ("Is this a no-parking zone?", "ꯃꯁꯤ ꯄꯥꯔ꯭ꯀꯤꯡ ꯌꯥꯗꯕ ꯃꯐꯝꯅꯤꯕꯔꯥ?"),
        ("Do not park here.", "ꯑꯁꯤꯗ ꯄꯥꯔ꯭ꯛ ꯇꯧꯅꯨ꯫"),
        ("Where is the nearest police station?", "ꯑꯅꯥꯛꯇꯒꯤ ꯄꯨꯂꯤꯁ ꯁ꯭ꯇꯦꯁꯟ ꯀꯗꯥꯏꯗꯅꯣ?"),
        ("I will be careful next time.", "ꯑꯩ ꯑꯃꯨꯛ ꯍꯟꯅ ꯆꯦꯛꯁꯤꯟꯒꯅꯤ꯫"),
        ("Follow the traffic rules.", "ꯇ꯭ꯔꯥꯐꯤꯛ ꯅꯤꯌꯝ ꯏꯟꯕꯤꯌꯨ꯫"),
        ("Drive slowly.", "ꯁꯦꯟꯅ ꯁꯦꯟꯅ ꯆꯠꯂꯨ꯫"),
        ("Thank you, officer.", "ꯊꯥꯒꯠꯆꯔꯤ, ꯑꯣꯐꯤꯁꯔ꯫"),
    ],
},

# ━━━ 627: Rickshaw/Taxi driver ━━━
627: {
    "heading": "Conversation with Rickshaw/Taxi",
    "rows": [
        ("Where do you want to go?", "ꯅꯈꯣꯏ ꯀꯗꯥꯏꯗ ꯆꯠꯅꯤꯡꯕꯅꯣ?"),
        ("Take me to the market.", "ꯀꯩꯊꯦꯜꯗ ꯄꯨꯔꯛꯕꯤꯌꯨ꯫"),
        ("How much will you charge?", "ꯀꯌꯥ ꯂꯧꯒꯅꯤꯅꯣ?"),
        ("That is too expensive.", "ꯃꯁꯤ ꯌꯥꯝꯅ ꯃꯃꯜ ꯌꯥꯝꯏ꯫"),
        ("Please reduce the fare.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯃꯃꯜ ꯍꯟꯊꯕꯤꯌꯨ꯫"),
        ("Go by the meter.", "ꯃꯤꯇꯔꯅ ꯆꯠꯄꯤꯌꯨ꯫"),
        ("Stop here.", "ꯑꯁꯤꯗ ꯂꯦꯞꯄꯤꯌꯨ꯫"),
        ("Please drive carefully.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯆꯦꯛꯁꯤꯟꯅ ꯆꯠꯄꯤꯌꯨ꯫"),
        ("How far is it?", "ꯃꯁꯤ ꯀꯌꯥ ꯊꯥꯞꯅꯅꯣ?"),
        ("It is about ten minutes.", "ꯃꯤꯅꯤꯠ ꯇꯔꯥꯔꯣꯝ ꯂꯩꯒꯅꯤ꯫"),
        ("Turn left at the signal.", "ꯁꯤꯒ꯭ꯅꯜꯗ ꯁꯦꯡꯗ ꯀꯣꯟꯄꯤꯌꯨ꯫"),
        ("Please wait for me.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯑꯩꯒꯤꯗꯃꯛ ꯂꯨꯕꯤꯌꯨ꯫"),
        ("I will come back in five minutes.", "ꯑꯩ ꯃꯤꯅꯤꯠ ꯃꯉꯥꯗ ꯍꯟꯂꯛꯀꯅꯤ꯫"),
        ("Keep the change.", "ꯆꯦꯟꯖ ꯊꯝꯕꯤꯌꯨ꯫"),
        ("Thank you, brother.", "ꯊꯥꯒꯠꯆꯔꯤ, ꯏꯌꯥꯝꯕ꯫"),
        ("Can you go faster?", "ꯑꯃꯨꯛ ꯊꯨꯅ ꯆꯠꯄ ꯌꯥꯕꯔꯥ?"),
        ("I am in a hurry.", "ꯑꯩ ꯌꯥꯝꯅ ꯊꯨꯅ ꯇꯥꯏ꯫"),
    ],
},

# ━━━ 628: Software Engineers ━━━
628: {
    "heading": "Conversation – Software Engineers",
    "rows": [
        ("What programming language do you use?", "ꯅꯈꯣꯏ ꯀꯔꯤ ꯄ꯭ꯔꯣꯒ꯭ꯔꯥꯃꯤꯡ ꯂꯦꯡꯒ꯭ꯋꯦꯖ ꯁꯤꯖꯤꯟꯅꯔꯤꯕꯅꯣ?"),
        ("I work with Python.", "ꯑꯩ ꯄꯥꯏꯊꯟꯗ ꯊꯧꯔꯝ ꯇꯧꯏ꯫"),
        ("There is a bug in the code.", "ꯀꯣꯗꯇ ꯕꯒ ꯑꯃ ꯂꯩꯔꯤ꯫"),
        ("Can you fix this error?", "ꯑꯦꯔꯔ ꯑꯁꯤ ꯐꯤꯛꯁ ꯇꯧꯕ ꯌꯥꯕꯔꯥ?"),
        ("The deadline is tomorrow.", "ꯗꯦꯗꯂꯥꯏꯟ ꯍꯌꯦꯡꯅꯤ꯫"),
        ("We have a meeting at three.", "ꯑꯩꯈꯣꯏꯒꯤ ꯃꯤꯇꯤꯡ ꯄꯨꯡ ꯑꯍꯨꯝꯗ ꯂꯩ꯫"),
        ("Please push the code.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯀꯣꯗ ꯄꯨꯁ ꯇꯧꯕꯤꯌꯨ꯫"),
        ("I am testing the application.", "ꯑꯩ ꯑꯦꯞ꯭ꯂꯤꯀꯦꯁꯟ ꯇꯦꯁ꯭ꯠ ꯇꯧꯔꯤ꯫"),
        ("The server is down.", "ꯁꯔ꯭ꯚꯔ ꯂꯩꯈꯤꯗꯦ꯫"),
        ("I need to update the database.", "ꯑꯩ ꯗꯦꯇꯥꯕꯦꯁ ꯑꯞꯗꯦꯠ ꯇꯧꯒꯗꯕꯅꯤ꯫"),
        ("This project is very interesting.", "ꯄ꯭ꯔꯣꯖꯦꯛꯠ ꯑꯁꯤ ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("Let us discuss the design.", "ꯗꯤꯖꯥꯏꯟ ꯈꯟꯅꯁꯤ꯫"),
        ("I will deploy it tonight.", "ꯑꯩ ꯉꯁꯤ ꯑꯍꯤꯡ ꯗꯤꯞ꯭ꯂꯣꯢ ꯇꯧꯒꯅꯤ꯫"),
        ("The website is loading slowly.", "ꯋꯦꯕꯁꯥꯏꯠ ꯑꯁꯤ ꯁꯦꯟꯅ ꯂꯣꯗ ꯇꯧꯔꯤ꯫"),
        ("We need more developers.", "ꯑꯩꯈꯣꯏ ꯗꯤꯚꯦꯂꯣꯄꯔ ꯑꯃꯨꯛ ꯃꯊꯧ ꯇꯥꯏ꯫"),
        ("The code review is done.", "ꯀꯣꯗ ꯔꯤꯚꯤꯎ ꯂꯣꯏꯔꯦ꯫"),
        ("Good work, everyone!", "ꯃꯤꯄꯨꯝ ꯐꯕ ꯊꯧꯔꯝ ꯇꯧꯔꯦ!"),
    ],
},

# ━━━ 629: Grocery shop ━━━
629: {
    "heading": "Conversation at Grocery shop",
    "rows": [
        ("Do you have rice?", "ꯆꯦꯡ ꯂꯩꯕꯔꯥ?"),
        ("Yes, how much do you need?", "ꯍꯣꯏ, ꯀꯌꯥ ꯃꯊꯧ ꯇꯥꯏ?"),
        ("Give me two kilos of rice.", "ꯆꯦꯡ ꯀꯤꯂꯣ ꯑꯅꯤ ꯄꯤꯕꯤꯌꯨ꯫"),
        ("I need sugar and salt.", "ꯑꯩ ꯆꯤꯅꯤ ꯑꯃꯁꯨꯡ ꯊꯨꯝ ꯃꯊꯧ ꯇꯥꯏ꯫"),
        ("How much does this cost?", "ꯃꯁꯤꯒꯤ ꯃꯃꯜ ꯀꯌꯥꯅꯣ?"),
        ("That is fifty rupees.", "ꯃꯁꯤ ꯔꯨꯄꯤ ꯌꯥꯡꯈꯩꯅꯤ꯫"),
        ("Do you have cooking oil?", "ꯊꯥꯎ ꯂꯩꯕꯔꯥ?"),
        ("Give me one packet of milk.", "ꯁꯉꯣꯝ ꯄꯥꯛꯀꯦꯠ ꯑꯃ ꯄꯤꯕꯤꯌꯨ꯫"),
        ("I also need eggs.", "ꯑꯩ ꯃꯅꯤꯞꯨꯛ ꯃꯊꯧ ꯇꯥꯏ꯫"),
        ("Is this fresh?", "ꯃꯁꯤ ꯑꯇꯦꯛꯄꯕꯔꯥ?"),
        ("Yes, it came today.", "ꯍꯣꯏ, ꯉꯁꯤ ꯂꯥꯛꯈꯤꯕꯅꯤ꯫"),
        ("What is the total?", "ꯄꯨꯝꯅꯃꯛ ꯀꯌꯥꯅꯣ?"),
        ("The total is three hundred.", "ꯄꯨꯝꯅꯃꯛ ꯔꯨꯄꯤ ꯆꯥ ꯑꯍꯨꯝꯅꯤ꯫"),
        ("Do you have a carry bag?", "ꯊꯧꯅꯥꯎ ꯂꯩꯕꯔꯥ?"),
        ("Here is your change.", "ꯅꯈꯣꯏꯒꯤ ꯆꯦꯟꯖ ꯃꯁꯤꯅꯤ꯫"),
        ("Thank you, come again.", "ꯊꯥꯒꯠꯆꯔꯤ, ꯑꯃꯨꯛ ꯂꯥꯛꯎ꯫"),
        ("I come here every week.", "ꯑꯩ ꯑꯁꯤꯗ ꯆꯌꯣꯟ ꯈꯨꯗꯤꯡ ꯂꯥꯛꯏ꯫"),
    ],
},

# ━━━ 630: Doctor-Patient ━━━
630: {
    "heading": "Doctor-Patient conversation",
    "rows": [
        ("Good morning, doctor.", "ꯗꯣꯛꯇꯔ, ꯑꯌꯨꯛꯀꯤ ꯅꯨꯃꯤꯗꯥꯡ꯫"),
        ("What is your problem?", "ꯅꯈꯣꯏꯒꯤ ꯋꯥꯈꯜ ꯀꯔꯤꯅꯣ?"),
        ("I have a headache.", "ꯑꯩꯒꯤ ꯀꯣꯛ ꯅꯥꯏ꯫"),
        ("I have a fever.", "ꯑꯩꯒꯤ ꯍꯛꯆꯥꯡ ꯐꯥꯏ꯫"),
        ("Since when do you have fever?", "ꯀꯗꯥꯏꯗꯒꯤꯅꯣ ꯐꯥꯔꯤꯕꯅꯣ?"),
        ("Since yesterday.", "ꯉꯔꯥꯡꯗꯒꯤꯅꯤ꯫"),
        ("Open your mouth.", "ꯃꯆꯤꯟꯕꯥꯜ ꯍꯥꯡꯕꯤꯌꯨ꯫"),
        ("I have a stomach ache.", "ꯑꯩꯒꯤ ꯄꯨꯛ ꯅꯥꯏ꯫"),
        ("Take this medicine twice a day.", "ꯍꯤꯗꯥꯛ ꯑꯁꯤ ꯅꯨꯃꯤꯠ ꯑꯃꯗ ꯑꯅꯤꯔꯛ ꯆꯥꯕꯤꯌꯨ꯫"),
        ("You need rest.", "ꯅꯈꯣꯏ ꯑꯔꯣꯟ ꯂꯩꯒꯗꯕꯅꯤ꯫"),
        ("Drink plenty of water.", "ꯏꯁꯤꯡ ꯌꯥꯝꯅ ꯊꯛꯕꯤꯌꯨ꯫"),
        ("Do not eat spicy food.", "ꯍꯩ ꯌꯥꯕ ꯆꯤꯟꯖꯥꯛ ꯆꯥꯅꯨ꯫"),
        ("Come again after three days.", "ꯅꯨꯃꯤꯠ ꯑꯍꯨꯝ ꯃꯇꯨꯡꯗ ꯑꯃꯨꯛ ꯂꯥꯛꯕꯤꯌꯨ꯫"),
        ("I feel better now.", "ꯑꯩ ꯍꯧꯖꯤꯛ ꯐꯖꯩ꯫"),
        ("Thank you, doctor.", "ꯊꯥꯒꯠꯆꯔꯤ, ꯗꯣꯛꯇꯔ꯫"),
        ("Get well soon.", "ꯊꯨꯅ ꯐꯖꯅꯕꯤꯌꯨ꯫"),
        ("Take care of your health.", "ꯅꯈꯣꯏꯒꯤ ꯍꯛꯆꯥꯡ ꯁꯦꯝꯒꯠꯄꯤꯌꯨ꯫"),
    ],
},

# ━━━ 631: Teacher & Students ━━━
631: {
    "heading": "Teacher & Students conversation",
    "rows": [
        ("Good morning, teacher.", "ꯑꯌꯨꯛꯀꯤ ꯅꯨꯃꯤꯗꯥꯡ, ꯎꯖꯥꯕ꯫"),
        ("Open your books.", "ꯂꯥꯏꯔꯤꯛ ꯍꯥꯡꯕꯤꯌꯨ꯫"),
        ("Turn to page ten.", "ꯂꯃꯥꯏ ꯇꯔꯥ ꯍꯥꯡꯕꯤꯌꯨ꯫"),
        ("Read the first paragraph.", "ꯑꯍꯥꯅꯕ ꯄꯦꯔꯥꯒ꯭ꯔꯥꯐ ꯄꯥꯕꯤꯌꯨ꯫"),
        ("Do you understand?", "ꯅꯈꯣꯏ ꯈꯉꯖꯔꯤꯕꯔꯥ?"),
        ("Yes, I understand.", "ꯍꯣꯏ, ꯑꯩ ꯈꯉꯖꯩ꯫"),
        ("No, I do not understand.", "ꯅꯠꯇꯦ, ꯑꯩ ꯈꯉꯖꯗꯦ꯫"),
        ("Please explain again.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯑꯃꯨꯛ ꯍꯟꯅ ꯈꯉꯍꯟꯄꯤꯌꯨ꯫"),
        ("Write this in your notebook.", "ꯃꯁꯤ ꯅꯣꯠꯕꯨꯛꯇ ꯏꯕꯤꯌꯨ꯫"),
        ("Who knows the answer?", "ꯀꯅꯅ ꯄꯥꯎꯈꯨꯝ ꯈꯉꯕꯅꯣ?"),
        ("I know the answer.", "ꯑꯩ ꯄꯥꯎꯈꯨꯝ ꯈꯉꯏ꯫"),
        ("Your homework is due tomorrow.", "ꯅꯈꯣꯏꯒꯤ ꯌꯨꯝꯒꯤ ꯊꯧꯔꯝ ꯍꯌꯦꯡꯅꯤ꯫"),
        ("The exam is next week.", "ꯏꯒ꯭ꯖꯥꯝ ꯑꯁꯤ ꯑꯇꯣꯞꯄ ꯆꯌꯣꯟꯗꯅꯤ꯫"),
        ("Study well for the exam.", "ꯏꯒ꯭ꯖꯥꯝꯒꯤꯗꯃꯛ ꯐꯖꯅ ꯇꯝꯕꯤꯌꯨ꯫"),
        ("May I go to the washroom?", "ꯑꯩ ꯕꯥꯊꯔꯨꯝꯗ ꯆꯠꯄ ꯌꯥꯕꯔꯥ?"),
        ("Class is over now.", "ꯀ꯭ꯂꯥꯁ ꯂꯣꯏꯔꯦ꯫"),
        ("Thank you, teacher.", "ꯊꯥꯒꯠꯆꯔꯤ, ꯎꯖꯥꯕ꯫"),
    ],
},

# ━━━ 632: Informal phone conversation ━━━
632: {
    "heading": "Informal phone conversation",
    "rows": [
        ("Hello, who is this?", "ꯍꯦꯜꯂꯣ, ꯀꯅꯅꯣ ꯃꯁꯤ?"),
        ("Hi, it is Tomba.", "ꯍꯥꯏ, ꯇꯣꯝꯕꯅꯤ ꯃꯁꯤ꯫"),
        ("How are you?", "ꯅꯈꯣꯏ ꯀꯝꯗꯧꯔꯤ?"),
        ("I am good, and you?", "ꯑꯩ ꯐꯖꯩ, ꯅꯈꯣꯏꯅꯣ?"),
        ("What are you doing?", "ꯀꯔꯤ ꯇꯧꯔꯤꯕꯅꯣ?"),
        ("I am watching TV.", "ꯑꯩ ꯇꯤꯚꯤ ꯌꯦꯡꯔꯤ꯫"),
        ("Are you free today?", "ꯅꯈꯣꯏ ꯉꯁꯤ ꯐ꯭ꯔꯤ ꯂꯩꯕꯔꯥ?"),
        ("Yes, I am free after lunch.", "ꯍꯣꯏ, ꯅꯨꯃꯤꯗꯥꯡꯒꯤ ꯆꯤꯟꯖꯥꯛ ꯃꯇꯨꯡꯗ ꯐ꯭ꯔꯤ ꯂꯩꯒꯅꯤ꯫"),
        ("Let us meet in the evening.", "ꯅꯨꯃꯗꯥꯡ ꯑꯣꯋꯥꯏꯔꯝꯗ ꯎꯅꯁꯤ꯫"),
        ("Where should we meet?", "ꯀꯗꯥꯏꯗ ꯎꯅꯒꯅꯤ?"),
        ("Let us meet at the park.", "ꯄꯥꯔ꯭ꯛꯇ ꯎꯅꯁꯤ꯫"),
        ("I will call you back.", "ꯑꯩ ꯅꯈꯣꯏꯕꯨ ꯑꯃꯨꯛ ꯀꯣꯜ ꯇꯧꯒꯅꯤ꯫"),
        ("My phone battery is low.", "ꯑꯩꯒꯤ ꯐꯣꯟ ꯕꯦꯇ꯭ꯔꯤ ꯂꯩꯈꯤꯗꯦ꯫"),
        ("Okay, talk to you later.", "ꯍꯣꯢꯅ, ꯃꯇꯨꯡꯗ ꯋꯥ ꯉꯥꯡꯒꯅꯤ꯫"),
        ("Say hello to everyone.", "ꯃꯤꯄꯨꯝꯗ ꯍꯦꯜꯂꯣ ꯍꯥꯏꯄꯤꯌꯨ꯫"),
        ("Bye, take care.", "ꯕꯥꯏ, ꯆꯦꯛꯁꯤꯟꯅ ꯂꯩꯕꯤꯌꯨ꯫"),
        ("I will message you.", "ꯑꯩ ꯅꯈꯣꯏꯕꯨ ꯃꯦꯁꯦꯖ ꯇꯧꯒꯅꯤ꯫"),
    ],
},

# ━━━ 633: Vegetable Market ━━━
633: {
    "heading": "Conversation at Vegetable Market",
    "rows": [
        ("How much are the tomatoes?", "ꯈꯥꯃꯦꯟ ꯑꯈꯥꯕꯤꯒꯤ ꯃꯃꯜ ꯀꯌꯥꯅꯣ?"),
        ("Fifty rupees per kilo.", "ꯀꯤꯂꯣ ꯑꯃꯗ ꯔꯨꯄꯤ ꯌꯥꯡꯈꯩꯅꯤ꯫"),
        ("Give me one kilo of potatoes.", "ꯑꯂꯨ ꯀꯤꯂꯣ ꯑꯃ ꯄꯤꯕꯤꯌꯨ꯫"),
        ("These onions look fresh.", "ꯇꯤꯂꯧ ꯑꯁꯤ ꯑꯇꯦꯛꯄ ꯃꯥꯟꯅꯩ꯫"),
        ("Do you have green chillies?", "ꯃꯔꯣꯛ ꯑꯇꯦꯛꯄ ꯂꯩꯕꯔꯥ?"),
        ("I need half kilo of peas.", "ꯑꯩ ꯍꯥꯋꯥꯏ ꯃꯉꯟ ꯍꯥꯐ ꯀꯤꯂꯣ ꯃꯊꯧ ꯇꯥꯏ꯫"),
        ("These vegetables are expensive.", "ꯉꯥꯡꯒꯣꯏ ꯑꯁꯤꯡ ꯃꯃꯜ ꯌꯥꯝꯏ꯫"),
        ("Please give a discount.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯃꯃꯜ ꯍꯟꯊꯕꯤꯌꯨ꯫"),
        ("Give me some coriander too.", "ꯄꯥꯛꯈꯣꯝ ꯈꯔ ꯄꯤꯕꯤꯌꯨ꯫"),
        ("How much for all of these?", "ꯃꯁꯤꯡ ꯄꯨꯝꯅꯃꯛ ꯀꯌꯥꯅꯣ?"),
        ("Two hundred rupees.", "ꯔꯨꯄꯤ ꯆꯥ ꯑꯅꯤꯅꯤ꯫"),
        ("The brinjals are very nice.", "ꯈꯥꯃꯦꯟ ꯑꯁꯤꯡ ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("I come here every day.", "ꯑꯩ ꯑꯁꯤꯗ ꯅꯨꯃꯤꯠ ꯈꯨꯗꯤꯡ ꯂꯥꯛꯏ꯫"),
        ("Pack these properly.", "ꯃꯁꯤꯡ ꯐꯖꯅ ꯄꯦꯛ ꯇꯧꯕꯤꯌꯨ꯫"),
        ("Do you have ginger?", "ꯁꯤꯡ ꯂꯩꯕꯔꯥ?"),
        ("Here is the money.", "ꯁꯦꯜ ꯃꯁꯤꯅꯤ꯫"),
        ("Thank you.", "ꯊꯥꯒꯠꯆꯔꯤ꯫"),
    ],
},

# ━━━ 634: Bus stop and in bus ━━━
634: {
    "heading": "Conversation at bus stop and in bus",
    "rows": [
        ("Which bus goes to Imphal?", "ꯏꯝꯐꯥꯜꯗ ꯆꯠꯄ ꯕꯁ ꯀꯗꯤꯅꯣ?"),
        ("Bus number five goes there.", "ꯕꯁ ꯅꯝꯕꯔ ꯃꯉꯥ ꯆꯠꯏ꯫"),
        ("When is the next bus?", "ꯑꯇꯣꯞꯄ ꯕꯁ ꯀꯗꯥꯏꯗ ꯂꯥꯛꯀꯅꯤ?"),
        ("The bus comes every fifteen minutes.", "ꯕꯁ ꯃꯤꯅꯤꯠ ꯇꯔꯥ ꯃꯉꯥ ꯈꯨꯗꯤꯡ ꯂꯥꯛꯏ꯫"),
        ("Is this seat empty?", "ꯐꯝꯐꯝ ꯑꯁꯤ ꯂꯨꯄ ꯂꯩꯕꯔꯥ?"),
        ("Yes, please sit.", "ꯍꯣꯏ, ꯐꯝꯕꯤꯌꯨ꯫"),
        ("How much is the ticket?", "ꯇꯤꯀꯦꯠꯀꯤ ꯃꯃꯜ ꯀꯌꯥꯅꯣ?"),
        ("Two tickets to Imphal.", "ꯏꯝꯐꯥꯜꯗ ꯆꯠꯄ ꯇꯤꯀꯦꯠ ꯑꯅꯤ꯫"),
        ("Please stop at the market.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯀꯩꯊꯦꯜꯗ ꯂꯦꯞꯄꯤꯌꯨ꯫"),
        ("Has the bus arrived?", "ꯕꯁ ꯂꯥꯛꯂꯤꯕꯔꯥ?"),
        ("The bus is late today.", "ꯕꯁ ꯉꯁꯤ ꯑꯊꯦꯡ ꯇꯥꯔꯤ꯫"),
        ("Move inside the bus.", "ꯕꯁ ꯃꯅꯨꯡꯗ ꯆꯡꯕꯤꯌꯨ꯫"),
        ("My stop is coming.", "ꯑꯩꯒꯤ ꯂꯦꯞꯐꯝ ꯂꯥꯛꯂꯤ꯫"),
        ("Please open the door.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯊꯣꯡ ꯍꯥꯡꯕꯤꯌꯨ꯫"),
        ("Thank you, driver.", "ꯊꯥꯒꯠꯆꯔꯤ, ꯗ꯭ꯔꯥꯏꯚꯔ꯫"),
        ("The bus is very crowded.", "ꯕꯁ ꯑꯁꯤ ꯌꯥꯝꯅ ꯃꯤ ꯃꯌꯥꯏ꯫"),
        ("I missed the bus.", "ꯑꯩ ꯕꯁ ꯂꯣꯟꯈꯤ꯫"),
    ],
},

# ━━━ 635: Asking address ━━━
635: {
    "heading": "Asking address sentences",
    "rows": [
        ("Excuse me, can you help?", "ꯄꯨꯛꯅꯤꯡ ꯆꯥꯏ, ꯃꯇꯦꯡ ꯄꯥꯡꯕ ꯌꯥꯕꯔꯥ?"),
        ("Where is this address?", "ꯑꯦꯗ꯭ꯔꯦꯁ ꯑꯁꯤ ꯀꯗꯥꯏꯗꯅꯣ?"),
        ("I am looking for this place.", "ꯑꯩ ꯃꯐꯝ ꯑꯁꯤ ꯊꯤꯖꯤꯟꯔꯤ꯫"),
        ("Go straight, then turn right.", "ꯑꯆꯨꯝꯕ ꯆꯠꯂꯨ, ꯃꯇꯨꯡꯗ ꯌꯦꯠꯗ ꯀꯣꯟꯂꯨ꯫"),
        ("Is it on this road?", "ꯃꯁꯤ ꯂꯝꯕꯤ ꯑꯁꯤꯗ ꯂꯩꯕꯔꯥ?"),
        ("It is the second house on the left.", "ꯃꯁꯤ ꯁꯦꯡꯗꯒꯤ ꯑꯅꯤꯁꯨꯕ ꯌꯨꯝꯅꯤ꯫"),
        ("How far is it from here?", "ꯑꯁꯤꯗꯒꯤ ꯀꯌꯥ ꯊꯥꯞꯅꯅꯣ?"),
        ("It is five minutes by walk.", "ꯆꯠꯅ ꯃꯤꯅꯤꯠ ꯃꯉꯥꯅꯤ꯫"),
        ("Can you show me on the map?", "ꯃꯦꯞꯇ ꯎꯠꯄ ꯌꯥꯕꯔꯥ?"),
        ("Is there a landmark nearby?", "ꯑꯅꯥꯛꯇꯗ ꯂꯦꯟꯗꯃꯥꯔ꯭ꯛ ꯂꯩꯕꯔꯥ?"),
        ("Yes, there is a temple.", "ꯍꯣꯏ, ꯂꯥꯏꯁꯡ ꯑꯃ ꯂꯩ꯫"),
        ("Cross the bridge.", "ꯐꯨꯡꯒꯥ ꯑꯁꯤ ꯂꯣꯟꯂꯨ꯫"),
        ("It is near the bank.", "ꯃꯁꯤ ꯕꯦꯡꯛꯀꯤ ꯑꯅꯥꯛꯇꯗ ꯂꯩ꯫"),
        ("You cannot miss it.", "ꯅꯈꯣꯏ ꯂꯣꯟꯕ ꯌꯥꯗꯦ꯫"),
        ("Thank you for your help.", "ꯃꯇꯦꯡ ꯄꯥꯡꯕꯤꯔꯛꯄꯗ ꯊꯥꯒꯠꯆꯔꯤ꯫"),
        ("I am lost.", "ꯑꯩ ꯂꯝꯕꯤ ꯃꯥꯡꯈꯤ꯫"),
        ("Can you take me there?", "ꯑꯩꯕꯨ ꯃꯐꯝ ꯑꯗꯨꯗ ꯄꯨꯔꯛꯄ ꯌꯥꯕꯔꯥ?"),
    ],
},

# ━━━ 636: I Love You / Proposing ━━━
636: {
    "heading": "Proposing / Love sentences",
    "rows": [
        ("I love you.", "ꯑꯩ ꯅꯈꯣꯏꯕꯨ ꯅꯨꯡꯁꯤ꯫"),
        ("I love you very much.", "ꯑꯩ ꯅꯈꯣꯏꯕꯨ ꯌꯥꯝꯅ ꯅꯨꯡꯁꯤ꯫"),
        ("You are very beautiful.", "ꯅꯈꯣꯏ ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("I think about you all the time.", "ꯑꯩ ꯅꯈꯣꯏꯕꯨ ꯃꯇꯝ ꯄꯨꯝꯕꯗ ꯈꯟꯏ꯫"),
        ("You are special to me.", "ꯅꯈꯣꯏ ꯑꯩꯒꯤꯗꯃꯛ ꯌꯥꯝꯅ ꯃꯔꯨꯑꯣꯏꯅꯤ꯫"),
        ("Will you marry me?", "ꯅꯈꯣꯏ ꯑꯩꯕꯨ ꯂꯧꯒꯗꯕꯔꯥ?"),
        ("I cannot live without you.", "ꯅꯈꯣꯏ ꯅꯠꯇꯅ ꯑꯩ ꯍꯤꯡꯕ ꯉꯝꯗꯦ꯫"),
        ("You make me happy.", "ꯅꯈꯣꯏꯅ ꯑꯩꯕꯨ ꯍꯔꯥꯎꯍꯟꯏ꯫"),
        ("I miss you.", "ꯑꯩ ꯅꯈꯣꯏꯕꯨ ꯅꯤꯡꯁꯤꯡꯏ꯫"),
        ("My heart beats for you.", "ꯑꯩꯒꯤ ꯊꯃꯣꯏ ꯅꯈꯣꯏꯒꯤꯗꯃꯛ ꯊꯤꯏ꯫"),
        ("I want to be with you forever.", "ꯑꯩ ꯅꯈꯣꯏꯒ ꯃꯇꯝ ꯄꯨꯝꯕꯗ ꯂꯩꯅꯤꯡꯏ꯫"),
        ("You are my life.", "ꯅꯈꯣꯏ ꯑꯩꯒꯤ ꯄꯨꯟꯁꯤꯅꯤ꯫"),
        ("I fell in love with you.", "ꯑꯩ ꯅꯈꯣꯏꯕꯨ ꯅꯨꯡꯁꯤꯈꯤ꯫"),
        ("Do you love me?", "ꯅꯈꯣꯏ ꯑꯩꯕꯨ ꯅꯨꯡꯁꯤꯕꯔꯥ?"),
        ("I will always love you.", "ꯑꯩ ꯅꯈꯣꯏꯕꯨ ꯃꯇꯝ ꯄꯨꯝꯕꯗ ꯅꯨꯡꯁꯤꯒꯅꯤ꯫"),
        ("You are the best.", "ꯅꯈꯣꯏ ꯈ꯭ꯋꯥꯏꯗꯒꯤ ꯐꯕꯅꯤ꯫"),
        ("Please say yes.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯍꯣꯏ ꯍꯥꯏꯕꯤꯌꯨ꯫"),
    ],
},

# ━━━ 637: Interview ━━━
637: {
    "heading": "Interview conversation",
    "rows": [
        ("Please come in and sit down.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯆꯡꯕꯤꯌꯨ ꯑꯃꯁꯨꯡ ꯐꯝꯕꯤꯌꯨ꯫"),
        ("Tell me about yourself.", "ꯅꯈꯣꯏꯒꯤ ꯃꯔꯝꯗ ꯍꯥꯏꯕꯤꯌꯨ꯫"),
        ("I completed my graduation last year.", "ꯑꯩ ꯃꯉꯥꯜ ꯆꯍꯤꯗ ꯒ꯭ꯔꯦꯖꯨꯌꯦꯁꯟ ꯂꯣꯏꯈꯤ꯫"),
        ("Why do you want this job?", "ꯅꯈꯣꯏ ꯊꯧꯔꯝ ꯑꯁꯤ ꯀꯔꯤꯒꯤꯗꯃꯛ ꯄꯥꯝꯅꯔꯤꯕꯅꯣ?"),
        ("I want to learn and grow.", "ꯑꯩ ꯇꯝꯅꯤꯡꯏ ꯑꯃꯁꯨꯡ ꯆꯥꯎꯈꯠꯅꯤꯡꯏ꯫"),
        ("What are your strengths?", "ꯅꯈꯣꯏꯒꯤ ꯑꯀꯟꯕ ꯃꯐꯝ ꯀꯔꯤꯅꯣ?"),
        ("I am hardworking and sincere.", "ꯑꯩ ꯍꯣꯠꯅꯈꯤꯕ ꯑꯃꯁꯨꯡ ꯆꯦꯠꯅ ꯇꯧꯏ꯫"),
        ("What is your expected salary?", "ꯅꯈꯣꯏꯒꯤ ꯂꯨꯄꯥ ꯀꯌꯥ ꯄꯥꯝꯅꯔꯤꯕꯅꯣ?"),
        ("When can you join?", "ꯅꯈꯣꯏ ꯀꯗꯥꯏꯗ ꯂꯥꯛꯄ ꯌꯥꯕꯅꯣ?"),
        ("I can join immediately.", "ꯑꯩ ꯈꯨꯗꯝ ꯈꯨꯗꯝꯗ ꯂꯥꯛꯄ ꯌꯥꯏ꯫"),
        ("Do you have any experience?", "ꯅꯈꯣꯏꯒꯤ ꯑꯦꯛꯁꯄꯤꯔꯤꯌꯦꯟꯁ ꯂꯩꯕꯔꯥ?"),
        ("I have two years experience.", "ꯑꯩꯒꯤ ꯆꯍꯤ ꯑꯅꯤꯒꯤ ꯑꯦꯛꯁꯄꯤꯔꯤꯌꯦꯟꯁ ꯂꯩ꯫"),
        ("Do you have any questions?", "ꯅꯈꯣꯏꯒꯤ ꯋꯥꯍꯡ ꯀꯔꯤꯅꯣ ꯂꯩꯕꯔꯥ?"),
        ("What are the working hours?", "ꯊꯧꯔꯝ ꯇꯧꯕꯒꯤ ꯃꯇꯝ ꯀꯌꯥꯅꯣ?"),
        ("We will let you know.", "ꯑꯩꯈꯣꯏ ꯅꯈꯣꯏꯕꯨ ꯈꯉꯍꯟꯒꯅꯤ꯫"),
        ("Thank you for the opportunity.", "ꯈꯨꯗꯣꯡꯆꯥꯗ ꯄꯤꯕꯤꯔꯛꯄꯗ ꯊꯥꯒꯠꯆꯔꯤ꯫"),
        ("It was nice meeting you.", "ꯅꯈꯣꯏꯒ ꯎꯅꯕ ꯐꯖꯩ꯫"),
    ],
},

# ━━━ 638: With Housemaid ━━━
638: {
    "heading": "Conversation with housemaid",
    "rows": [
        ("Please clean the house.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯌꯨꯝ ꯁꯦꯡꯗꯣꯛꯄꯤꯌꯨ꯫"),
        ("Sweep the floor.", "ꯂꯝꯕꯤ ꯁꯨꯝꯆꯤꯠꯅ ꯁꯦꯡꯗꯣꯛꯄꯤꯌꯨ꯫"),
        ("Mop the floor.", "ꯂꯝꯕꯤ ꯈꯥꯏꯕꯤꯌꯨ꯫"),
        ("Wash the dishes.", "ꯐꯨꯀꯥꯝ ꯀꯥꯡꯕꯤꯌꯨ꯫"),
        ("Did you wash the clothes?", "ꯐꯤ ꯀꯥꯡꯈꯤꯕꯔꯥ?"),
        ("Yes, I washed them.", "ꯍꯣꯏ, ꯀꯥꯡꯈꯤ꯫"),
        ("Iron the clothes.", "ꯐꯤ ꯏꯁ꯭ꯇ꯭ꯔꯤ ꯇꯧꯕꯤꯌꯨ꯫"),
        ("Clean the kitchen.", "ꯆꯥꯛꯁꯡ ꯁꯦꯡꯗꯣꯛꯄꯤꯌꯨ꯫"),
        ("Cook rice and dal.", "ꯆꯦꯡ ꯑꯃꯁꯨꯡ ꯗꯥꯜ ꯁꯥꯕꯤꯌꯨ꯫"),
        ("Water the plants.", "ꯄꯝꯕꯤꯁꯤꯡꯗ ꯏꯁꯤꯡ ꯊꯥꯕꯤꯌꯨ꯫"),
        ("When will you come tomorrow?", "ꯅꯈꯣꯏ ꯍꯌꯦꯡ ꯀꯗꯥꯏꯗ ꯂꯥꯛꯀꯅꯤ?"),
        ("I will come at eight.", "ꯑꯩ ꯄꯨꯡ ꯅꯤꯄꯥꯜꯗ ꯂꯥꯛꯀꯅꯤ꯫"),
        ("I need a day off.", "ꯑꯩ ꯅꯨꯃꯤꯠ ꯑꯃ ꯂꯤꯕ ꯃꯊꯧ ꯇꯥꯏ꯫"),
        ("Your salary is ready.", "ꯅꯈꯣꯏꯒꯤ ꯂꯨꯄꯥ ꯁꯦꯝꯈꯤ꯫"),
        ("Thank you, ma'am.", "ꯊꯥꯒꯠꯆꯔꯤ, ꯃꯦꯗꯝ꯫"),
        ("Please come on time.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯃꯇꯝꯗ ꯂꯥꯛꯄꯤꯌꯨ꯫"),
        ("You did a good job.", "ꯅꯈꯣꯏ ꯐꯕ ꯊꯧꯔꯝ ꯇꯧꯔꯦ꯫"),
    ],
},

# ━━━ 639: Linking AADHAR to mobile ━━━
639: {
    "heading": "Linking AADHAR card to mobile number",
    "rows": [
        ("I want to link my AADHAR to mobile.", "ꯑꯩ ꯑꯩꯒꯤ ꯑꯥꯗꯥꯔ ꯃꯣꯕꯥꯏꯜꯗ ꯂꯤꯡꯛ ꯇꯧꯅꯤꯡꯏ꯫"),
        ("Which mobile number do you want to link?", "ꯀꯔꯤ ꯃꯣꯕꯥꯏꯜ ꯅꯝꯕꯔ ꯂꯤꯡꯛ ꯇꯧꯅꯤꯡꯕꯅꯣ?"),
        ("This is my mobile number.", "ꯃꯁꯤ ꯑꯩꯒꯤ ꯃꯣꯕꯥꯏꯜ ꯅꯝꯕꯔꯅꯤ꯫"),
        ("Please give your AADHAR card.", "ꯆꯥꯅꯕꯤꯗꯨꯅ ꯅꯈꯣꯏꯒꯤ ꯑꯥꯗꯥꯔ ꯀꯥꯔ꯭ꯗ ꯄꯤꯕꯤꯌꯨ꯫"),
        ("I need to verify your fingerprint.", "ꯅꯈꯣꯏꯒꯤ ꯈꯨꯠꯁꯥ ꯆꯥꯞ ꯚꯦꯔꯤꯐꯥꯏ ꯇꯧꯒꯗꯕꯅꯤ꯫"),
        ("Place your finger here.", "ꯅꯈꯣꯏꯒꯤ ꯈꯨꯠꯁꯥ ꯑꯁꯤꯗ ꯊꯝꯕꯤꯌꯨ꯫"),
        ("Verification is successful.", "ꯚꯦꯔꯤꯐꯤꯀꯦꯁꯟ ꯂꯣꯏꯔꯦ꯫"),
        ("Your AADHAR is now linked.", "ꯅꯈꯣꯏꯒꯤ ꯑꯥꯗꯥꯔ ꯍꯧꯖꯤꯛ ꯂꯤꯡꯛ ꯇꯧꯔꯦ꯫"),
        ("You will get an SMS confirmation.", "ꯅꯈꯣꯏ ꯑꯦꯁꯑꯦꯃꯑꯦꯁ ꯀꯟꯐꯔ꯭ꯃꯦꯁꯟ ꯐꯡꯒꯅꯤ꯫"),
        ("How long will it take?", "ꯃꯇꯝ ꯀꯌꯥ ꯂꯩꯒꯅꯤ?"),
        ("It will take two minutes.", "ꯃꯤꯅꯤꯠ ꯑꯅꯤ ꯂꯩꯒꯅꯤ꯫"),
        ("Is there any charge?", "ꯁꯦꯜ ꯄꯤꯒꯗꯕ ꯂꯩꯕꯔꯥ?"),
        ("No, this service is free.", "ꯅꯠꯇꯦ, ꯁꯔ꯭ꯚꯤꯁ ꯑꯁꯤ ꯐ꯭ꯔꯤꯅꯤ꯫"),
        ("Thank you for your help.", "ꯃꯇꯦꯡ ꯄꯥꯡꯕꯤꯔꯛꯄꯗ ꯊꯥꯒꯠꯆꯔꯤ꯫"),
        ("Is my old number delinked?", "ꯑꯩꯒꯤ ꯑꯔꯤꯕ ꯅꯝꯕꯔ ꯗꯤꯂꯤꯡꯛ ꯇꯧꯔꯦꯕꯔꯥ?"),
        ("Yes, the old number is removed.", "ꯍꯣꯏ, ꯑꯔꯤꯕ ꯅꯝꯕꯔ ꯂꯧꯊꯣꯛꯂꯦ꯫"),
        ("Keep your AADHAR safe.", "ꯅꯈꯣꯏꯒꯤ ꯑꯥꯗꯥꯔ ꯆꯦꯛꯁꯤꯟꯅ ꯊꯝꯕꯤꯌꯨ꯫"),
    ],
},

# ━━━ 640: Linking mobile to AADHAR ━━━
640: {
    "heading": "Linking mobile number to AADHAR card",
    "rows": [
        ("I want to add my mobile to AADHAR.", "ꯑꯩ ꯑꯩꯒꯤ ꯃꯣꯕꯥꯏꯜ ꯑꯥꯗꯥꯔꯗ ꯌꯥꯎꯍꯟꯅꯤꯡꯏ꯫"),
        ("Go to the nearest AADHAR centre.", "ꯑꯅꯥꯛꯇꯒꯤ ꯑꯥꯗꯥꯔ ꯁꯦꯟꯇꯔꯗ ꯆꯠꯂꯨ꯫"),
        ("Bring your AADHAR card.", "ꯅꯈꯣꯏꯒꯤ ꯑꯥꯗꯥꯔ ꯀꯥꯔ꯭ꯗ ꯄꯨꯔꯛꯂꯨ꯫"),
        ("Bring an ID proof.", "ꯑꯥꯏꯗꯤ ꯄ꯭ꯔꯨꯐ ꯄꯨꯔꯛꯂꯨ꯫"),
        ("Fill this form.", "ꯐꯣꯔꯝ ꯑꯁꯤ ꯐꯤꯜ ꯇꯧꯕꯤꯌꯨ꯫"),
        ("Write your new mobile number.", "ꯅꯈꯣꯏꯒꯤ ꯑꯍꯥꯟꯕ ꯃꯣꯕꯥꯏꯜ ꯅꯝꯕꯔ ꯏꯕꯤꯌꯨ꯫"),
        ("Give your biometric.", "ꯅꯈꯣꯏꯒꯤ ꯕꯥꯏꯑꯣꯃꯦꯠꯔꯤꯛ ꯄꯤꯕꯤꯌꯨ꯫"),
        ("Your request is submitted.", "ꯅꯈꯣꯏꯒꯤ ꯔꯤꯀ꯭ꯋꯦꯁ꯭ꯠ ꯊꯥꯈꯤ꯫"),
        ("You will get an OTP.", "ꯅꯈꯣꯏ ꯑꯣꯇꯤꯄꯤ ꯑꯃ ꯐꯡꯒꯅꯤ꯫"),
        ("Enter the OTP here.", "ꯑꯣꯇꯤꯄꯤ ꯑꯁꯤꯗ ꯊꯝꯕꯤꯌꯨ꯫"),
        ("Update is successful.", "ꯑꯞꯗꯦꯠ ꯂꯣꯏꯔꯦ꯫"),
        ("It may take a few days.", "ꯅꯨꯃꯤꯠ ꯈꯔ ꯂꯩꯒꯅꯤ꯫"),
        ("Check the status online.", "ꯑꯣꯟꯂꯥꯏꯟꯗ ꯁ꯭ꯇꯦꯇꯁ ꯆꯦꯛ ꯇꯧꯕꯤꯌꯨ꯫"),
        ("Your mobile is now registered.", "ꯅꯈꯣꯏꯒꯤ ꯃꯣꯕꯥꯏꯜ ꯍꯧꯖꯤꯛ ꯔꯦꯖꯤꯁ꯭ꯇꯔ ꯇꯧꯔꯦ꯫"),
        ("Keep your receipt.", "ꯅꯈꯣꯏꯒꯤ ꯔꯤꯁꯤꯠ ꯊꯝꯕꯤꯌꯨ꯫"),
        ("This is important for banking.", "ꯃꯁꯤ ꯕꯦꯡꯀꯤꯡꯒꯤꯗꯃꯛ ꯃꯔꯨꯑꯣꯏꯅꯤ꯫"),
        ("Thank you.", "ꯊꯥꯒꯠꯆꯔꯤ꯫"),
    ],
},

# ━━━ 641: Republic Day celebration ━━━
641: {
    "heading": "Republic Day celebration conversation",
    "rows": [
        ("Happy Republic Day!", "ꯔꯤꯄꯕ꯭ꯂꯤꯛ ꯗꯦꯒꯤ ꯌꯥꯏꯐ ꯐꯕ ꯄꯤꯔꯛꯄꯤꯌꯨ!"),
        ("Today is 26th January.", "ꯉꯁꯤ ꯖꯥꯅꯨꯋꯥꯔꯤ ꯀꯨꯟ ꯇꯔꯨꯛꯅꯤ꯫"),
        ("It is our Republic Day.", "ꯃꯁꯤ ꯑꯩꯈꯣꯏꯒꯤ ꯔꯤꯄꯕ꯭ꯂꯤꯛ ꯗꯦꯅꯤ꯫"),
        ("The flag hoisting will begin.", "ꯐ꯭ꯂꯦꯒ ꯋꯥꯡꯕ ꯍꯧꯒꯅꯤ꯫"),
        ("Children are performing dances.", "ꯑꯉꯥꯡꯁꯤꯡ ꯖꯥꯒꯣꯏ ꯁꯥꯔꯤ꯫"),
        ("The parade looks amazing.", "ꯄꯦꯔꯦꯗ ꯑꯁꯤ ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("We should respect our country.", "ꯑꯩꯈꯣꯏ ꯑꯩꯈꯣꯏꯒꯤ ꯂꯩꯄꯥꯛꯕꯨ ꯏꯀꯥꯏ ꯈꯨꯝꯅꯒꯗꯕꯅꯤ꯫"),
        ("India became a republic in 1950.", "ꯏꯟꯗꯤꯌꯥ ꯆꯍꯤ ꯱꯹꯵꯰ ꯗ ꯔꯤꯄꯕ꯭ꯂꯤꯛ ꯑꯣꯏꯈꯤ꯫"),
        ("We sing the national anthem.", "ꯑꯩꯈꯣꯏ ꯔꯥꯁ꯭ꯠ꯭ꯔꯤꯌ ꯒꯤꯠ ꯁꯥꯏ꯫"),
        ("Students gave speeches.", "ꯃꯍꯩꯔꯣꯏꯁꯤꯡ ꯋꯥ ꯉꯥꯡꯈꯤ꯫"),
        ("We got sweets and snacks.", "ꯑꯩꯈꯣꯏ ꯑꯊꯨꯝꯕ ꯑꯃꯁꯨꯡ ꯆꯤꯟꯖꯥꯛ ꯐꯡꯈꯤ꯫"),
        ("I am proud to be Indian.", "ꯑꯩ ꯏꯟꯗꯤꯌꯥꯒꯤ ꯃꯤꯑꯣꯏ ꯑꯣꯏꯕꯗ ꯆꯥꯎꯊꯣꯛꯏ꯫"),
        ("Jai Hind!", "ꯖꯩ ꯍꯤꯟꯗ!"),
        ("The celebration was wonderful.", "ꯊꯧꯔꯝ ꯑꯁꯤ ꯌꯥꯝꯅ ꯐꯖꯩ꯫"),
        ("Let us work for our nation.", "ꯑꯩꯈꯣꯏꯒꯤ ꯂꯩꯄꯥꯛꯀꯤꯗꯃꯛ ꯊꯧꯔꯝ ꯇꯧꯁꯤ꯫"),
        ("Long live India!", "ꯏꯟꯗꯤꯌꯥ ꯍꯤꯡꯁꯤ!"),
        ("We are all equal.", "ꯑꯩꯈꯣꯏ ꯃꯤꯄꯨꯝ ꯑꯃꯠꯇꯅꯤ꯫"),
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
    sys.stdout.buffer.write(f"Updated {updated} conversation lessons (620-641) in data_meitei.json\n".encode("utf-8"))

if __name__ == "__main__":
    main()
