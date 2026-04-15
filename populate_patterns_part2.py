#!/usr/bin/env python3
"""Populate pattern lessons 571-596 (3.29-3.54) with topic-relevant sentences."""
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

# ━━━ 571: Greetings, Wishes, Blessings, Slogans ━━━
571: {
    "heading": "Greetings and wishes examples",
    "rows": [
        ("Hello", "ꯈꯨꯔꯨꯝꯖꯔꯤ꯫"),
        ("Good morning", "ꯈꯨꯔꯨꯝꯖꯔꯤ꯫"),
        ("Good evening", "ꯅꯨꯃꯤꯗꯪ ꯐꯖꯩ꯫"),
        ("Good night", "ꯒꯨꯗ ꯅꯥꯏꯠ꯫"),
        ("Happy birthday", "ꯅꯤꯡꯊꯧ ꯄꯥꯟꯕ ꯐꯖꯩ꯫"),
        ("Happy new year", "ꯆꯩꯔꯥꯑꯣꯕ ꯑꯅꯧꯕ ꯐꯖꯩ꯫"),
        ("Congratulations", "ꯅꯨꯡꯉꯥꯏꯕ ꯐꯣꯡꯗꯣꯛꯆꯔꯤ꯫"),
        ("Thank you very much", "ꯍꯥꯏꯅꯤꯡꯉꯥꯏ ꯂꯩꯇꯅ ꯊꯥꯒꯠꯆꯔꯤ꯫"),
        ("Welcome", "ꯇꯔꯥꯝꯅ ꯑꯣꯛꯆꯔꯤ꯫"),
        ("Goodbye", "ꯆꯠꯂꯨꯈꯤꯒꯦ꯫"),
        ("Take care", "ꯐꯖꯅ ꯂꯩꯌꯨ꯫"),
        ("God bless you", "ꯃꯔꯥꯏꯕꯛꯅ ꯌꯥꯏꯐ ꯄꯤꯕꯤꯌꯨ꯫"),
        ("Long live Manipur", "ꯃꯅꯤꯄꯨꯔ ꯆꯤꯔꯒꯅꯤ꯫"),
        ("Good luck", "ꯀꯥꯏꯕꯛ ꯐꯕ ꯑꯣꯏꯌꯨ꯫"),
        ("Best wishes", "ꯈꯋꯥꯏꯗꯒꯤ ꯐꯕ ꯄꯥꯎꯇꯥꯛ꯫"),
        ("Get well soon", "ꯌꯥꯝꯅ ꯊꯨꯅ ꯅꯥꯕ ꯐꯕ ꯑꯣꯏꯔꯣ꯫"),
        ("See you again", "ꯑꯃꯨꯛ ꯎꯅꯅꯁꯤ꯫"),
    ],
},

# ━━━ 572: Compound verbs / Phrases ━━━
572: {
    "heading": "Compound verb examples",
    "rows": [
        ("Sit down (phamdu)", "ꯐꯝꯗꯨ꯫"),
        ("Stand up (lepthok)", "ꯂꯦꯞꯊꯣꯛ꯫"),
        ("Get up (hakthok)", "ꯍꯛꯊꯣꯛ꯫"),
        ("Come back (hannalak)", "ꯍꯟꯅ ꯂꯥꯛꯂꯣ꯫"),
        ("Go out (thokchatlou)", "ꯊꯣꯛꯆꯠꯂꯣ꯫"),
        ("Pick up (thangat)", "ꯊꯪꯒꯠꯂꯣ꯫"),
        ("Put down (thindok)", "ꯊꯤꯟꯗꯣꯛꯂꯣ꯫"),
        ("Throw away (thaktharok)", "ꯊꯛꯊꯔꯣꯛꯂꯣ꯫"),
        ("Run away (chelthok)", "ꯆꯦꯜꯊꯣꯛꯂꯣ꯫"),
        ("Give back (hannapibiu)", "ꯍꯟꯅ ꯄꯤꯕꯤꯌꯨ꯫"),
        ("He sat down", "ꯃꯍꯥꯛ ꯐꯝꯗꯨꯂꯦ꯫"),
        ("She stood up", "ꯃꯍꯥꯛ ꯂꯦꯞꯊꯣꯛꯂꯦ꯫"),
        ("I came back", "ꯑꯩ ꯍꯟꯅ ꯂꯥꯛꯂꯦ꯫"),
        ("He got up early", "ꯃꯍꯥꯛ ꯊꯨꯅ ꯍꯛꯊꯣꯛꯂꯦ꯫"),
        ("She picked it up", "ꯃꯍꯥꯛ ꯃꯗꯨ ꯊꯪꯒꯠꯂꯦ꯫"),
        ("Go away from here", "ꯑꯁꯤꯗꯒꯤ ꯆꯠꯊꯣꯛꯂꯣ꯫"),
        ("They ran away", "ꯃꯈꯣꯏ ꯆꯦꯜꯊꯣꯛꯂꯦ꯫"),
    ],
},

# ━━━ 573: Calling / Addressing someone ━━━
573: {
    "heading": "Addressing someone examples",
    "rows": [
        ("Elder brother", "ꯏꯌꯝꯕ / ꯇꯃꯣ / ꯗ"),
        ("Elder sister", "ꯏꯆꯦ / ꯆꯦ"),
        ("Younger brother", "ꯏꯅꯥꯑꯣꯄ"),
        ("Younger sister", "ꯏꯅꯥꯑꯣꯅꯨꯄꯤ"),
        ("Father", "ꯏꯄꯥ / ꯄꯥꯄ"),
        ("Mother", "ꯏꯃꯥ / ꯃꯃꯥ"),
        ("Sir (respectful)", "ꯏꯕꯨꯉꯣ"),
        ("Madam (respectful)", "ꯏꯕꯦꯝꯃꯥ"),
        ("Friend", "ꯃꯔꯨꯞ"),
        ("Teacher", "ꯑꯣꯖꯥ"),
        ("Hey, elder brother!", "ꯍꯩ ꯗ!"),
        ("Excuse me, sir", "ꯏꯕꯨꯉꯣ, ꯑꯃꯨꯛꯇ ꯉꯥꯛꯄꯤꯚꯨ꯫"),
        ("Mother, I'm hungry", "ꯏꯃꯥ, ꯑꯩ ꯆꯥꯛ ꯈꯣꯡ ꯍꯥꯝꯏ꯫"),
        ("Father, where are you?", "ꯏꯄꯥ, ꯅꯪ ꯀꯗꯥꯏꯗ ꯂꯩꯕꯒꯦ?"),
        ("Sister, come here", "ꯏꯆꯦ, ꯑꯁꯤꯗ ꯂꯥꯀꯎ꯫"),
        ("Friends, let's go", "ꯃꯔꯨꯞꯁꯤꯡ, ꯆꯠꯂꯁꯤ꯫"),
        ("Teacher, I have a question", "ꯑꯣꯖꯥ, ꯑꯩꯗ ꯋꯥꯍꯪ ꯑꯃ ꯂꯩꯏ꯫"),
    ],
},

# ━━━ 574: Exclamations ━━━
574: {
    "heading": "Exclamation examples",
    "rows": [
        ("Wow!", "ꯑꯣ!"),
        ("Oh no!", "ꯑꯣ ꯅꯠꯇꯦ!"),
        ("Amazing!", "ꯌꯥꯝꯅ ꯐꯔꯦ!"),
        ("How beautiful!", "ꯀꯔꯝꯅ ꯐꯖꯩꯕꯒꯦ!"),
        ("What a shame!", "ꯌꯥꯝꯅ ꯏꯀꯥꯏꯗꯦ!"),
        ("Help!", "ꯇꯦꯡꯕꯥꯡꯕ!"),
        ("Stop!", "ꯅꯤꯡꯊꯤꯌꯨ!"),
        ("Fire!", "ꯃꯩ!"),
        ("Be careful!", "ꯆꯦꯛꯁꯤꯟꯅ ꯂꯩꯌꯨ!"),
        ("What happened!", "ꯀꯔꯤ ꯑꯣꯏꯈꯔꯦ!"),
        ("How nice!", "ꯀꯔꯝꯅ ꯐꯔꯦꯕꯒꯦ!"),
        ("Very good!", "ꯌꯥꯝꯅ ꯐꯔꯦ!"),
        ("What nonsense!", "ꯀꯔꯤ ꯍꯥꯏꯔꯤꯕꯒꯦ!"),
        ("How sad!", "ꯀꯔꯝꯅ ꯋꯥꯈꯜꯕꯒꯦ!"),
        ("Hurry up!", "ꯊꯨꯅ ꯇꯧꯌꯨ!"),
        ("Well done!", "ꯅꯤꯉꯡꯤꯅ ꯄꯥꯉꯡꯣꯡꯂꯦ!"),
        ("Look out!", "ꯌꯦꯡꯕꯤꯌꯨ!"),
    ],
},

# ━━━ 575: Requesting – May I, Can you ━━━
575: {
    "heading": "Request examples",
    "rows": [
        ("May I come in?", "ꯑꯩ ꯂꯥꯛꯕ ꯌꯥꯒꯗ꯭ꯔ?"),
        ("Can you help me?", "ꯑꯩꯕꯨ ꯃꯇꯦꯡ ꯄꯥꯡꯕ ꯉꯃꯒꯗ꯭ꯔ?"),
        ("May I sit here?", "ꯑꯩ ꯑꯁꯤꯗ ꯐꯝꯕ ꯌꯥꯒꯗ꯭ꯔ?"),
        ("Can you give me water?", "ꯑꯩꯗ ꯏꯁꯤꯡ ꯄꯤꯕ ꯉꯃꯒꯗ꯭ꯔ?"),
        ("May I speak?", "ꯑꯩ ꯉꯥꯡꯕ ꯌꯥꯒꯗ꯭ꯔ?"),
        ("Can you come tomorrow?", "ꯅꯪ ꯍꯌꯦꯡ ꯂꯥꯛꯕ ꯉꯃꯒꯗ꯭ꯔ?"),
        ("May I use your phone?", "ꯅꯪꯒꯤ ꯐꯣꯟ ꯁꯤꯖꯤꯟꯅꯕ ꯌꯥꯒꯗ꯭ꯔ?"),
        ("Can you tell me the way?", "ꯑꯩꯕꯨ ꯂꯝꯕꯤ ꯎꯠꯕ ꯉꯃꯒꯗ꯭ꯔ?"),
        ("May I ask a question?", "ꯑꯩ ꯋꯥꯍꯪ ꯑꯃ ꯍꯪꯕ ꯌꯥꯒꯗ꯭ꯔ?"),
        ("Can you open the door?", "ꯊꯣꯡ ꯍꯪꯗꯣꯛꯕ ꯉꯃꯒꯗ꯭ꯔ?"),
        ("May I take leave?", "ꯑꯩ ꯆꯠꯕ ꯌꯥꯒꯗ꯭ꯔ?"),
        ("Can you wait a moment?", "ꯑꯃꯨꯛꯇ ꯉꯥꯏꯕ ꯉꯃꯒꯗ꯭ꯔ?"),
        ("May I have some tea?", "ꯑꯩꯗ ꯆꯥ ꯈꯔ ꯄꯤꯕ ꯌꯥꯒꯗ꯭ꯔ?"),
        ("Can you write this?", "ꯃꯁꯤ ꯏꯕ ꯉꯃꯒꯗ꯭ꯔ?"),
        ("May I borrow your pen?", "ꯅꯪꯒꯤ ꯀꯂꯝ ꯁꯤꯖꯤꯟꯅꯕ ꯌꯥꯒꯗ꯭ꯔ?"),
        ("Can you speak Meitei?", "ꯅꯪ ꯃꯩꯇꯩꯂꯣꯟ ꯉꯥꯡꯕ ꯉꯃꯒꯗ꯭ꯔ?"),
        ("Could you please repeat?", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯑꯃꯨꯛ ꯍꯟꯅ ꯍꯥꯏꯕ ꯉꯃꯒꯗ꯭ꯔ?"),
    ],
},

# ━━━ 576: May, Might (uncertainty) ━━━
576: {
    "heading": "May / Might (uncertainty) examples",
    "rows": [
        ("He may come", "ꯃꯍꯥꯛ ꯂꯥꯛꯕ ꯌꯥꯏ꯫"),
        ("It may rain", "ꯅꯣꯡ ꯇꯥꯛꯕ ꯌꯥꯏ꯫"),
        ("She might go", "ꯃꯍꯥꯛ ꯆꯠꯕ ꯌꯥꯏ꯫"),
        ("I might be late", "ꯑꯩ ꯊꯦꯡꯕ ꯌꯥꯏ꯫"),
        ("He may not come", "ꯃꯍꯥꯛ ꯂꯥꯛꯇꯕ ꯌꯥꯏ꯫"),
        ("She might not come", "ꯃꯍꯥꯛ ꯂꯥꯛꯇꯕ ꯌꯥꯏ꯫"),
        ("It may be cold tomorrow", "ꯍꯌꯦꯡ ꯈꯪ ꯑꯣꯏꯕ ꯌꯥꯏ꯫"),
        ("He might come later", "ꯃꯍꯥꯛ ꯃꯇꯨꯡꯗ ꯂꯥꯛꯕ ꯌꯥꯏ꯫"),
        ("We may go tomorrow", "ꯑꯩꯈꯣꯏ ꯍꯌꯦꯡ ꯆꯠꯕ ꯌꯥꯏ꯫"),
        ("She may be busy", "ꯃꯍꯥꯛ ꯊꯕꯛ ꯆꯤꯜꯕ ꯌꯥꯏ꯫"),
        ("He might know the answer", "ꯃꯍꯥꯛ ꯄꯥꯑꯣꯈꯨꯝ ꯈꯪꯕ ꯌꯥꯏ꯫"),
        ("It may take time", "ꯃꯇꯝ ꯆꯪꯕ ꯌꯥꯏ꯫"),
        ("She might call you", "ꯃꯍꯥꯛ ꯅꯪꯕꯨ ꯀꯧꯕ ꯌꯥꯏ꯫"),
        ("We might win", "ꯑꯩꯈꯣꯏ ꯃꯥꯏꯄꯥꯛꯕ ꯌꯥꯏ꯫"),
        ("He may be sleeping", "ꯃꯍꯥꯛ ꯇꯨꯝꯔꯝꯃꯤꯕ ꯌꯥꯏ꯫"),
        ("I might forget", "ꯑꯩ ꯀꯞꯕ ꯌꯥꯏ꯫"),
        ("Maybe he will help", "ꯃꯍꯥꯛ ꯃꯇꯦꯡ ꯄꯥꯡꯕ ꯌꯥꯏ꯫"),
    ],
},

# ━━━ 577: Adjectives from verbs ━━━
577: {
    "heading": "Adjective from verb examples",
    "rows": [
        ("A running boy", "ꯆꯦꯜꯔꯤꯕ ꯅꯨꯄꯃꯆꯥ"),
        ("A sleeping child", "ꯇꯨꯝꯔꯤꯕ ꯑꯅꯧꯕ"),
        ("A singing girl", "ꯏꯁꯩ ꯁꯀꯔꯤꯕ ꯅꯨꯄꯤꯃꯆꯥ"),
        ("A broken glass", "ꯀꯤꯈꯔꯕ ꯒ꯭ꯂꯥꯁ"),
        ("Cooked food", "ꯁꯥꯈꯔꯕ ꯆꯤꯟꯖꯥꯛ"),
        ("Written letter", "ꯏꯈꯔꯕ ꯆꯤꯠꯊꯤ"),
        ("A boiling pot", "ꯄꯨꯛꯔꯤꯕ ꯈꯨꯗꯨꯝ"),
        ("A flying bird", "ꯄꯥꯏꯔꯤꯕ ꯎꯆꯦꯛ"),
        ("A fallen tree", "ꯇꯥꯛꯈꯔꯕ ꯎꯄꯥꯜ"),
        ("The crying child came", "ꯀꯞꯔꯤꯕ ꯑꯅꯧꯕ ꯂꯥꯛꯂꯦ꯫"),
        ("I ate the cooked rice", "ꯑꯩ ꯁꯥꯈꯔꯕ ꯆꯥꯛ ꯆꯥꯈꯔꯦ꯫"),
        ("He read the written letter", "ꯃꯍꯥꯛ ꯏꯈꯔꯕ ꯆꯤꯠꯊꯤ ꯄꯈꯔꯦ꯫"),
        ("She wore a dried dress", "ꯃꯍꯥꯛ ꯀꯪꯈꯔꯕ ꯐꯤ ꯁꯣꯟꯈꯔꯦ꯫"),
        ("The running dog fell", "ꯆꯦꯜꯔꯤꯕ ꯍꯨꯏ ꯇꯥꯛꯂꯦ꯫"),
        ("A burned house", "ꯃꯩ ꯀꯥꯈꯔꯕ ꯌꯨꯝ"),
        ("The closed door", "ꯊꯤꯡꯈꯔꯕ ꯊꯣꯡ"),
        ("An opened window", "ꯍꯪꯗꯣꯛꯈꯔꯕ ꯇꯛꯅꯩꯕꯥꯛ"),
    ],
},

# ━━━ 578: Adjectives from prepositions ━━━
578: {
    "heading": "Adjective from preposition examples",
    "rows": [
        ("Inside (manungda)", "ꯃꯅꯨꯡꯗ"),
        ("Outside (mapanda)", "ꯃꯄꯟꯗ"),
        ("Above (mathakta)", "ꯃꯊꯛꯇ"),
        ("Below (makhada)", "ꯃꯈꯥꯗ"),
        ("Near (nakta)", "ꯅꯛꯇ"),
        ("Far (lapna)", "ꯂꯞꯅ"),
        ("The inside room", "ꯃꯅꯨꯡꯒꯤ ꯔꯨꯝ"),
        ("The outside garden", "ꯃꯄꯟꯒꯤ ꯃꯐꯝ"),
        ("The upper floor", "ꯃꯊꯛꯀꯤ ꯃꯐꯝ"),
        ("The lower shelf", "ꯃꯈꯥꯒꯤ ꯃꯐꯝ"),
        ("The nearby school", "ꯅꯛꯀꯤ ꯁ꯭ꯀꯨꯜ"),
        ("The faraway village", "ꯂꯞꯅꯒꯤ ꯈꯨꯜ"),
        ("He is inside the house", "ꯃꯍꯥꯛ ꯌꯨꯝ ꯃꯅꯨꯡꯗ ꯂꯩꯏ꯫"),
        ("The cat is under the table", "ꯍꯧꯗꯣꯡ ꯇꯦꯕꯜ ꯃꯈꯥꯗ ꯂꯩꯏ꯫"),
        ("He lives nearby", "ꯃꯍꯥꯛ ꯅꯛꯇ ꯂꯩꯏ꯫"),
        ("The bird is above", "ꯎꯆꯦꯛ ꯃꯊꯛꯇ ꯂꯩꯏ꯫"),
        ("She went outside", "ꯃꯍꯥꯛ ꯃꯄꯟꯗ ꯆꯠꯂꯦ꯫"),
    ],
},

# ━━━ 579: May to express wish ━━━
579: {
    "heading": "May (wish) examples",
    "rows": [
        ("May you be happy", "ꯅꯪ ꯅꯨꯡꯉꯥꯏꯕ ꯑꯣꯏꯌꯨ꯫"),
        ("May God bless you", "ꯃꯔꯥꯏꯕꯛꯅ ꯌꯥꯏꯐ ꯄꯤꯕꯤꯌꯨ꯫"),
        ("May you live long", "ꯅꯪ ꯁꯨꯡ ꯍꯤꯡꯕꯤꯌꯨ꯫"),
        ("May you pass the exam", "ꯅꯪ ꯄꯔꯤꯈꯥ ꯄꯥꯁ ꯇꯧꯕꯤꯌꯨ꯫"),
        ("May you succeed", "ꯅꯪ ꯃꯥꯏꯄꯥꯛꯕꯤꯌꯨ꯫"),
        ("May we win", "ꯑꯩꯈꯣꯏ ꯃꯥꯏꯄꯥꯛꯕꯤꯌꯨ꯫"),
        ("May it rain today", "ꯉꯁꯤ ꯅꯣꯡ ꯇꯥꯛꯕꯤꯌꯨ꯫"),
        ("May she get well soon", "ꯃꯍꯥꯛ ꯊꯨꯅ ꯅꯥꯕ ꯐꯕ ꯑꯣꯏꯕꯤꯌꯨ꯫"),
        ("May he come on time", "ꯃꯍꯥꯛ ꯃꯇꯝꯗ ꯂꯥꯛꯕꯤꯌꯨ꯫"),
        ("May the country prosper", "ꯂꯩꯄꯥꯛ ꯑꯗꯨ ꯆꯧꯈꯠꯕꯤꯌꯨ꯫"),
        ("May your wish come true", "ꯅꯪꯒꯤ ꯄꯥꯝꯕ ꯑꯗꯨ ꯐꯨꯡꯕꯤꯌꯨ꯫"),
        ("May you have a safe journey", "ꯅꯪꯒꯤ ꯈꯣꯡꯆꯠ ꯐꯕ ꯑꯣꯏꯕꯤꯌꯨ꯫"),
        ("May they be safe", "ꯃꯈꯣꯏ ꯐꯖꯅ ꯂꯩꯕꯤꯌꯨ꯫"),
        ("May peace prevail", "ꯅꯤꯡꯊꯤꯖ ꯂꯩꯕꯤꯌꯨ꯫"),
        ("May all be well", "ꯄꯨꯝꯅꯃꯛ ꯐꯕ ꯑꯣꯏꯕꯤꯌꯨ꯫"),
        ("May you have a nice day", "ꯅꯪꯒꯤ ꯅꯨꯃꯤꯠ ꯐꯕ ꯑꯣꯏꯕꯤꯌꯨ꯫"),
        ("May we meet again", "ꯑꯩꯈꯣꯏ ꯑꯃꯨꯛ ꯎꯅꯕꯤꯌꯨ꯫"),
    ],
},

# ━━━ 580: Make someone do something ━━━
580: {
    "heading": "\"Make someone do\" examples",
    "rows": [
        ("I made him eat", "ꯑꯩꯅ ꯃꯍꯥꯛꯄꯨ ꯆꯥꯍꯜꯂꯦ꯫"),
        ("She made me go", "ꯃꯍꯥꯛꯅ ꯑꯩꯕꯨ ꯆꯠꯍꯜꯂꯦ꯫"),
        ("He made her sit", "ꯃꯍꯥꯛꯅ ꯃꯍꯥꯛꯄꯨ ꯐꯝꯍꯜꯂꯦ꯫"),
        ("Mother made child sleep", "ꯏꯃꯥꯅ ꯑꯅꯧꯕꯕꯨ ꯇꯨꯝꯍꯜꯂꯦ꯫"),
        ("Teacher made students read", "ꯑꯣꯖꯥꯅ ꯃꯍꯩꯔꯣꯌꯁꯤꯡꯕꯨ ꯄꯍꯜꯂꯦ꯫"),
        ("He made me laugh", "ꯃꯍꯥꯛꯅ ꯑꯩꯕꯨ ꯅꯣꯛꯍꯜꯂꯦ꯫"),
        ("She made him cry", "ꯃꯍꯥꯛꯅ ꯃꯍꯥꯛꯄꯨ ꯀꯞꯍꯜꯂꯦ꯫"),
        ("I will make him come", "ꯑꯩ ꯃꯍꯥꯛꯄꯨ ꯂꯥꯛꯍꯜꯒꯅꯤ꯫"),
        ("She made children drink milk", "ꯃꯍꯥꯛꯅ ꯑꯅꯧꯕꯁꯤꯡꯕꯨ ꯁꯪꯒꯣꯝ ꯊꯛꯍꯜꯂꯦ꯫"),
        ("Don't make me run", "ꯑꯩꯕꯨ ꯆꯦꯜꯍꯜꯂꯣꯌꯨ꯫"),
        ("He made me write", "ꯃꯍꯥꯛꯅ ꯑꯩꯕꯨ ꯏꯍꯜꯂꯦ꯫"),
        ("I will make her cook", "ꯑꯩ ꯃꯍꯥꯛꯄꯨ ꯁꯥꯍꯜꯒꯅꯤ꯫"),
        ("Father made son study", "ꯏꯄꯥꯅ ꯃꯆꯥꯕꯨ ꯇꯝꯍꯜꯂꯦ꯫"),
        ("She makes the baby eat", "ꯃꯍꯥꯛꯅ ꯑꯅꯧꯕꯕꯨ ꯆꯥꯍꯜꯂꯤ꯫"),
        ("Don't make him wait", "ꯃꯍꯥꯛꯄꯨ ꯉꯥꯏꯍꯜꯂꯣꯌꯨ꯫"),
        ("He made me understand", "ꯃꯍꯥꯛꯅ ꯑꯩꯕꯨ ꯈꯪꯍꯜꯂꯦ꯫"),
        ("I made them play", "ꯑꯩꯅ ꯃꯈꯣꯏꯕꯨ ꯁꯥꯍꯜꯂꯦ꯫"),
    ],
},

# ━━━ 581: Generalizing words ━━━
581: {
    "heading": "Generalizing word examples",
    "rows": [
        ("Somewhere", "ꯀꯗꯥꯏꯗꯁꯨ"),
        ("Somehow", "ꯀꯔꯝꯅꯁꯨ"),
        ("Something", "ꯀꯔꯤꯁꯨ"),
        ("Someone / Somebody", "ꯀꯅꯃꯛ"),
        ("Sometime", "ꯃꯇꯝ ꯑꯃꯗ"),
        ("Anywhere", "ꯀꯗꯥꯏꯗꯁꯨ"),
        ("Anything", "ꯀꯔꯤꯁꯨ"),
        ("Anybody", "ꯀꯅꯃꯛ"),
        ("Nowhere", "ꯀꯗꯥꯏꯗꯁꯨ ꯅꯠꯇꯦ"),
        ("Nothing", "ꯀꯔꯤꯁꯨ ꯅꯠꯇꯦ"),
        ("Nobody / No one", "ꯀꯅꯃꯛ ꯅꯠꯇꯦ"),
        ("Everywhere", "ꯃꯐꯝ ꯄꯨꯝꯕꯗ"),
        ("Something happened", "ꯀꯔꯤꯁꯨ ꯑꯃ ꯑꯣꯏꯈꯔꯦ꯫"),
        ("Someone came", "ꯀꯅꯃꯛ ꯑꯃ ꯂꯥꯛꯂꯦ꯫"),
        ("I will go somewhere", "ꯑꯩ ꯀꯗꯥꯏꯗꯁꯨ ꯆꯠꯀꯅꯤ꯫"),
        ("Nobody came today", "ꯉꯁꯤ ꯀꯅꯃꯛ ꯂꯥꯛꯈꯔꯗꯦ꯫"),
        ("Nothing happened", "ꯀꯔꯤꯁꯨ ꯑꯣꯏꯈꯔꯗꯦ꯫"),
    ],
},

# ━━━ 582: To have (possession) ━━━
582: {
    "heading": "\"To have\" (possession) examples",
    "rows": [
        ("I have a book", "ꯑꯩꯗ ꯂꯥꯏꯔꯤꯛ ꯑꯃ ꯂꯩꯏ꯫"),
        ("He has money", "ꯃꯍꯥꯛꯇ ꯄꯥꯏꯁꯥ ꯂꯩꯏ꯫"),
        ("She has a car", "ꯃꯍꯥꯛꯇ ꯒꯥꯔꯤ ꯑꯃ ꯂꯩꯏ꯫"),
        ("We have a house", "ꯑꯩꯈꯣꯏꯗ ꯌꯨꯝ ꯑꯃ ꯂꯩꯏ꯫"),
        ("They have children", "ꯃꯈꯣꯏꯗ ꯑꯅꯧꯕꯁꯤꯡ ꯂꯩꯏ꯫"),
        ("I don't have money", "ꯑꯩꯗ ꯄꯥꯏꯁꯥ ꯂꯩꯇꯦ꯫"),
        ("He doesn't have a pen", "ꯃꯍꯥꯛꯇ ꯀꯂꯝ ꯂꯩꯇꯦ꯫"),
        ("Do you have a phone?", "ꯅꯪꯗ ꯐꯣꯟ ꯂꯩꯕ꯭ꯔ?"),
        ("I have a sister", "ꯑꯩꯗ ꯏꯆꯦ ꯑꯃ ꯂꯩꯏ꯫"),
        ("He has many friends", "ꯃꯍꯥꯛꯇ ꯃꯔꯨꯞ ꯃꯌꯥꯝ ꯂꯩꯏ꯫"),
        ("She has two brothers", "ꯃꯍꯥꯛꯇ ꯏꯌꯝꯕ ꯑꯅꯤ ꯂꯩꯏ꯫"),
        ("I had a dog", "ꯑꯩꯗ ꯍꯨꯏ ꯑꯃ ꯂꯩꯔꯝꯃꯤ꯫"),
        ("He had a bicycle", "ꯃꯍꯥꯛꯇ ꯁꯥꯏꯀꯜ ꯑꯃ ꯂꯩꯔꯝꯃꯤ꯫"),
        ("I have no time", "ꯑꯩꯗ ꯃꯇꯝ ꯂꯩꯇꯦ꯫"),
        ("She has good health", "ꯃꯍꯥꯛꯇ ꯍꯛꯆꯥꯡ ꯐꯕ ꯂꯩꯏ꯫"),
        ("We don't have food", "ꯑꯩꯈꯣꯏꯗ ꯆꯤꯟꯖꯥꯛ ꯂꯩꯇꯦ꯫"),
        ("Do they have children?", "ꯃꯈꯣꯏꯗ ꯑꯅꯧꯕ ꯂꯩꯕ꯭ꯔ?"),
    ],
},

# ━━━ 583: To mean / How to ask meaning ━━━
583: {
    "heading": "\"To mean\" examples",
    "rows": [
        ("What does this mean?", "ꯃꯁꯤꯒꯤ ꯋꯥꯍꯟꯊꯣꯛ ꯀꯔꯤꯅꯣ?"),
        ("What does that word mean?", "ꯋꯥꯍꯩ ꯑꯗꯨꯒꯤ ꯋꯥꯍꯟꯊꯣꯛ ꯀꯔꯤꯅꯣ?"),
        ("It means 'good'", "ꯃꯗꯨꯒꯤ ꯋꯥꯍꯟꯊꯣꯛ 'ꯐꯕ' ꯍꯥꯏꯕꯅꯤ꯫"),
        ("I mean this", "ꯑꯩ ꯃꯁꯤ ꯍꯥꯏꯅꯤꯡꯉꯩ꯫"),
        ("What do you mean?", "ꯅꯪ ꯀꯔꯤ ꯍꯥꯏꯅꯤꯡꯉꯩꯕꯒꯦ?"),
        ("This word means 'water'", "ꯋꯥꯍꯩ ꯑꯁꯤꯒꯤ ꯋꯥꯍꯟꯊꯣꯛ 'ꯏꯁꯤꯡ' ꯅꯤ꯫"),
        ("How do you say ... in Meitei?", "ꯃꯩꯇꯩꯂꯣꯟꯗ ꯀꯔꯝꯅ ꯍꯥꯏꯒꯅꯤ ...?"),
        ("What is this called in Meitei?", "ꯃꯁꯤꯕꯨ ꯃꯩꯇꯩꯂꯣꯟꯗ ꯀꯔꯤ ꯀꯧꯕꯒꯦ?"),
        ("That means 'thank you'", "ꯃꯗꯨꯒꯤ ꯋꯥꯍꯟꯊꯣꯛ 'ꯊꯥꯒꯠꯆꯔꯤ' ꯅꯤ꯫"),
        ("I don't know the meaning", "ꯑꯩ ꯋꯥꯍꯟꯊꯣꯛ ꯈꯪꯗꯦ꯫"),
        ("What is the meaning of 'phajei'?", "'ꯐꯖꯩ' ꯍꯥꯏꯕꯁꯤ ꯀꯔꯤꯅꯣ?"),
        ("This means love", "ꯃꯁꯤꯒꯤ ꯋꯥꯍꯟꯊꯣꯛ ꯅꯨꯡꯁꯤꯕ ꯅꯤ꯫"),
        ("He said that means yes", "ꯃꯍꯥꯛ ꯃꯗꯨ ꯍꯣꯏ ꯍꯥꯏꯕꯅꯤ ꯍꯥꯏꯈꯔꯦ꯫"),
        ("Please tell me the meaning", "ꯆꯥꯅꯕꯤꯗꯨꯅꯥ ꯋꯥꯍꯟꯊꯣꯛ ꯍꯥꯏꯕꯤꯌꯨ꯫"),
        ("I understood the meaning", "ꯑꯩ ꯋꯥꯍꯟꯊꯣꯛ ꯈꯪꯈꯔꯦ꯫"),
        ("The word 'nungshi' means love", "'ꯅꯨꯡꯁꯤ' ꯍꯥꯏꯕꯁꯤ ꯅꯨꯡꯁꯤꯕ ꯅꯤ꯫"),
        ("That sentence means 'I am fine'", "ꯋꯥꯍꯩ ꯑꯗꯨꯒꯤ ꯋꯥꯍꯟꯊꯣꯛ 'ꯑꯩ ꯅꯨꯉꯥꯏꯔꯤ' ꯅꯤ꯫"),
    ],
},

# ━━━ 584: Conjunctions Part 1 ━━━
584: {
    "heading": "Conjunction examples (and, but, because, so)",
    "rows": [
        ("I ate and he drank", "ꯑꯩ ꯆꯥꯈꯔꯦ ꯑꯃꯁꯨꯡ ꯃꯍꯥꯛ ꯊꯛꯈꯔꯦ꯫"),
        ("She is beautiful but lazy", "ꯃꯍꯥꯛ ꯐꯖꯩ ꯑꯗꯨꯕꯨ ꯊꯕꯛ ꯇꯧꯗꯦ꯫"),
        ("I came because he called", "ꯃꯍꯥꯛ ꯀꯧꯈꯔꯕꯗꯒꯤ ꯑꯩ ꯂꯥꯛꯂꯦ꯫"),
        ("He was tired so he slept", "ꯃꯍꯥꯛ ꯋꯥꯈꯔꯕꯗꯒꯤ ꯇꯨꯝꯂꯦ꯫"),
        ("I know that he is coming", "ꯃꯍꯥꯛ ꯂꯥꯛꯔꯤ ꯃꯗꯨ ꯑꯩ ꯈꯪꯏ꯫"),
        ("Although it rained, I went", "ꯅꯣꯡ ꯇꯥꯛꯂꯕꯁꯨ ꯑꯩ ꯆꯠꯂꯦ꯫"),
        ("He is old, still he works", "ꯃꯍꯥꯛ ꯑꯔꯨꯝꯕꯅꯤ, ꯍꯥꯌꯕꯁꯨ ꯊꯕꯛ ꯇꯧꯏ꯫"),
        ("She studied, yet she failed", "ꯃꯍꯥꯛ ꯇꯝꯂꯦ, ꯍꯥꯌꯕꯁꯨ ꯐꯦꯜ ꯑꯣꯏꯂꯦ꯫"),
        ("He and she are friends", "ꯃꯍꯥꯛ ꯑꯃꯁꯨꯡ ꯃꯍꯥꯛ ꯃꯔꯨꯞꯅꯤ꯫"),
        ("I want tea but not coffee", "ꯑꯩ ꯆꯥ ꯄꯝꯃꯤ ꯑꯗꯨꯕꯨ ꯀꯣꯐꯤ ꯄꯝꯗꯦ꯫"),
        ("Because I was late, I ran", "ꯑꯩ ꯊꯦꯡꯈꯔꯕꯗꯒꯤ ꯆꯦꯜꯂꯦ꯫"),
        ("So I went home", "ꯃꯗꯨꯅ ꯑꯩ ꯌꯨꯝꯗ ꯆꯠꯂꯦ꯫"),
        ("He is poor but honest", "ꯃꯍꯥꯛ ꯂꯥꯏꯔꯕꯅꯤ ꯑꯗꯨꯕꯨ ꯑꯆꯨꯝꯕꯅꯤ꯫"),
        ("She cooks and he cleans", "ꯃꯍꯥꯛ ꯁꯥꯏ ꯑꯃꯁꯨꯡ ꯃꯍꯥꯛ ꯁꯦꯡꯗꯣꯛꯂꯤ꯫"),
        ("Although tired, she came", "ꯋꯥꯈꯔꯕꯁꯨ ꯃꯍꯥꯛ ꯂꯥꯛꯂꯦ꯫"),
        ("I like him because he is kind", "ꯃꯍꯥꯛ ꯅꯤꯡꯊꯤꯖ ꯑꯣꯏꯕꯗꯒꯤ ꯑꯩ ꯄꯝꯖꯩ꯫"),
        ("He is smart, yet humble", "ꯃꯍꯥꯛ ꯑꯆꯨꯝꯕꯅꯤ, ꯍꯥꯌꯕꯁꯨ ꯅꯨꯡꯉꯥꯏꯅꯤ꯫"),
    ],
},

# ━━━ 585: Conjunctions Part 2 ━━━
585: {
    "heading": "Conjunction examples (as, or, neither, nor, if)",
    "rows": [
        ("As I was going, I saw him", "ꯑꯩ ꯆꯠꯔꯤꯉꯩꯗ ꯃꯍꯥꯛꯄꯨ ꯎꯈꯔꯦ꯫"),
        ("Tea or coffee?", "ꯆꯥ ꯅꯠꯇ꯭ꯔꯒ ꯀꯣꯐꯤ?"),
        ("Neither he nor she came", "ꯃꯍꯥꯛꯁꯨ ꯂꯥꯛꯈꯔꯗꯦ ꯃꯍꯥꯛꯁꯨ ꯂꯥꯛꯈꯔꯗꯦ꯫"),
        ("If you come, I will go", "ꯅꯪ ꯂꯥꯛꯂꯕꯗꯤ, ꯑꯩ ꯆꯠꯀꯅꯤ꯫"),
        ("In case it rains, take umbrella", "ꯅꯣꯡ ꯇꯥꯛꯂꯕꯗꯤ, ꯁꯥꯇꯤꯟ ꯄꯨꯔꯛꯂꯣ꯫"),
        ("You can come provided you finish", "ꯅꯪ ꯂꯣꯏꯁꯤꯜꯂꯕꯗꯤ ꯂꯥꯛꯕ ꯌꯥꯏ꯫"),
        ("Do this or that", "ꯃꯁꯤ ꯅꯠꯇ꯭ꯔꯒ ꯃꯗꯨ ꯇꯧꯌꯨ꯫"),
        ("As you wish", "ꯅꯪ ꯄꯝꯕꯒꯨꯝꯅ꯫"),
        ("He doesn't eat nor drink", "ꯃꯍꯥꯛ ꯆꯥꯗꯦ ꯊꯛꯁꯨ ꯇꯧꯗꯦ꯫"),
        ("If I know, I will tell", "ꯑꯩ ꯈꯪꯂꯕꯗꯤ ꯍꯥꯏꯒꯅꯤ꯫"),
        ("Either he or she will come", "ꯃꯍꯥꯛ ꯅꯠꯇ꯭ꯔꯒ ꯃꯍꯥꯛ ꯂꯥꯛꯀꯅꯤ꯫"),
        ("As long as you are here, stay", "ꯅꯪ ꯑꯁꯤꯗ ꯂꯩꯔꯤꯉꯩꯃꯛ ꯂꯩꯌꯨ꯫"),
        ("If he asks, tell the truth", "ꯃꯍꯥꯛ ꯍꯪꯂꯕꯗꯤ ꯑꯆꯨꯝꯕ ꯍꯥꯏꯕꯤꯌꯨ꯫"),
        ("Neither good nor bad", "ꯐꯕꯁꯨ ꯅꯠꯇꯦ ꯑꯊꯤꯕꯁꯨ ꯅꯠꯇꯦ꯫"),
        ("In case I don't come, start without me", "ꯑꯩ ꯂꯥꯛꯇꯗꯤ ꯑꯩ ꯅꯠꯇꯅ ꯍꯧꯕꯤꯌꯨ꯫"),
        ("As he is a teacher, he teaches", "ꯃꯍꯥꯛ ꯑꯣꯖꯥ ꯑꯣꯏꯕꯗꯒꯤ ꯇꯝꯍꯟꯂꯤ꯫"),
        ("Come or stay, your choice", "ꯂꯥꯛꯂꯣ ꯅꯠꯇ꯭ꯔꯒ ꯂꯩꯌꯨ, ꯅꯪꯒꯤ ꯈꯟꯅꯕꯅꯤ꯫"),
    ],
},

# ━━━ 586: Conjunctions Part 3 ━━━
586: {
    "heading": "Conjunction examples (after, as far as, as if)",
    "rows": [
        ("After he came, we ate", "ꯃꯍꯥꯛ ꯂꯥꯛꯈꯔꯕ ꯃꯇꯨꯡꯗ ꯑꯩꯈꯣꯏ ꯆꯥꯈꯔꯦ꯫"),
        ("After eating, he slept", "ꯆꯥꯈꯔꯕ ꯃꯇꯨꯡꯗ ꯃꯍꯥꯛ ꯇꯨꯝꯂꯦ꯫"),
        ("Then I went home", "ꯃꯇꯨꯡꯗ ꯑꯩ ꯌꯨꯝꯗ ꯆꯠꯂꯦ꯫"),
        ("As far as I know", "ꯑꯩ ꯈꯪꯕ ꯃꯇꯨꯡꯗ"),
        ("As long as you are here", "ꯅꯪ ꯑꯁꯤꯗ ꯂꯩꯔꯤꯉꯩꯃꯛ"),
        ("He speaks as if he knows", "ꯃꯍꯥꯛ ꯈꯪꯕꯒꯨꯝꯅ ꯉꯥꯡꯏ꯫"),
        ("After school, I play", "ꯁ꯭ꯀꯨꯜ ꯂꯣꯏꯈꯔꯕ ꯃꯇꯨꯡꯗ ꯑꯩ ꯁꯥꯏ꯫"),
        ("Then he told the truth", "ꯃꯇꯨꯡꯗ ꯃꯍꯥꯛ ꯑꯆꯨꯝꯕ ꯍꯥꯏꯈꯔꯦ꯫"),
        ("As far as this road goes", "ꯂꯝꯕꯤ ꯑꯁꯤ ꯆꯠꯕ ꯃꯇꯨꯡꯗ"),
        ("As if nothing happened", "ꯀꯔꯤꯁꯨ ꯑꯣꯏꯈꯔꯗꯕꯒꯨꯝꯅ"),
        ("After the rain stopped, I went out", "ꯅꯣꯡ ꯅꯤꯡꯈꯔꯕ ꯃꯇꯨꯡꯗ ꯑꯩ ꯊꯣꯛꯆꯠꯂꯦ꯫"),
        ("She acted as if she didn't know", "ꯃꯍꯥꯛ ꯈꯪꯗꯕꯒꯨꯝꯅ ꯇꯧꯈꯔꯦ꯫"),
        ("As long as I live, I will remember", "ꯑꯩ ꯍꯤꯡꯔꯤꯉꯩꯃꯛ ꯅꯤꯡꯁꯤꯡꯒꯅꯤ꯫"),
        ("After eating, wash your hands", "ꯆꯥꯈꯔꯕ ꯃꯇꯨꯡꯗ ꯈꯨꯠ ꯀꯨꯝꯕꯤꯌꯨ꯫"),
        ("As far as I can see", "ꯑꯩ ꯌꯦꯡꯕ ꯉꯝꯕ ꯃꯇꯨꯡꯗ"),
        ("Then we will decide", "ꯃꯇꯨꯡꯗ ꯑꯩꯈꯣꯏ ꯈꯟꯅꯒꯅꯤ꯫"),
        ("She looks as if she is tired", "ꯃꯍꯥꯛ ꯋꯥꯈꯔꯕꯒꯨꯝꯅ ꯎꯏ꯫"),
    ],
},

# ━━━ 587: Conjunctions Part 4 ━━━
587: {
    "heading": "Conjunction examples (as soon as, once, rather than)",
    "rows": [
        ("As soon as he came, I left", "ꯃꯍꯥꯛ ꯂꯥꯛꯇ꯭ꯔꯤꯉꯩꯃꯛ ꯑꯩ ꯆꯠꯂꯦ꯫"),
        ("Once you finish, call me", "ꯅꯪ ꯂꯣꯏꯁꯤꯜꯇ꯭ꯔꯤꯉꯩꯃꯛ ꯑꯩꯕꯨ ꯀꯧꯕꯤꯌꯨ꯫"),
        ("Rather than sitting, walk", "ꯐꯝꯕꯗꯒꯤꯅ ꯆꯠꯂꯣ꯫"),
        ("Instead of tea, give me water", "ꯆꯥꯒꯤ ꯃꯍꯨꯠꯇ ꯑꯩꯗ ꯏꯁꯤꯡ ꯄꯤꯌꯨ꯫"),
        ("So that he can study", "ꯃꯍꯥꯛ ꯇꯝꯕ ꯉꯝꯅꯕ ꯃꯇꯨꯡꯗ"),
        ("As soon as it rains, stay inside", "ꯅꯣꯡ ꯇꯥꯛꯇ꯭ꯔꯤꯉꯩꯃꯛ ꯃꯅꯨꯡꯗ ꯂꯩꯌꯨ꯫"),
        ("Once I know, I will tell you", "ꯑꯩ ꯈꯪꯇ꯭ꯔꯤꯉꯩꯃꯛ ꯅꯪꯗ ꯍꯥꯏꯒꯅꯤ꯫"),
        ("Rather than crying, try again", "ꯀꯞꯕꯗꯒꯤꯅ ꯑꯃꯨꯛ ꯍꯣꯠꯅꯌꯨ꯫"),
        ("Instead of going, stay here", "ꯆꯠꯕꯗꯒꯤꯅ ꯑꯁꯤꯗ ꯂꯩꯌꯨ꯫"),
        ("So that we finish early", "ꯑꯩꯈꯣꯏ ꯊꯨꯅ ꯂꯣꯏꯁꯤꯜꯅꯕ ꯃꯇꯨꯡꯗ"),
        ("As soon as he woke up, he ate", "ꯃꯍꯥꯛ ꯍꯛꯇ꯭ꯔꯤꯉꯩꯃꯛ ꯆꯥꯈꯔꯦ꯫"),
        ("Once she arrives, start", "ꯃꯍꯥꯛ ꯊꯨꯡꯇ꯭ꯔꯤꯉꯩꯃꯛ ꯍꯧꯕꯤꯌꯨ꯫"),
        ("Rather than buying, make it", "ꯂꯩꯕꯗꯒꯤꯅ ꯁꯥꯌꯨ꯫"),
        ("Instead of sleeping, study", "ꯇꯨꯝꯕꯗꯒꯤꯅ ꯇꯝꯌꯨ꯫"),
        ("So that children can learn", "ꯑꯅꯧꯕꯁꯤꯡ ꯇꯝꯕ ꯉꯝꯅꯕ ꯃꯇꯨꯡꯗ"),
        ("As soon as possible", "ꯉꯝꯕ ꯃꯇꯨꯡꯗ ꯊꯨꯅ"),
        ("Once done, rest", "ꯂꯣꯏꯁꯤꯜꯇ꯭ꯔꯤꯉꯩꯃꯛ ꯂꯣꯏꯅ ꯂꯩꯌꯨ꯫"),
    ],
},

# ━━━ 588: List of conjunctions ━━━
588: {
    "heading": "Conjunction list",
    "rows": [
        ("And", "ꯑꯃꯁꯨꯡ"),
        ("But", "ꯑꯗꯨꯕꯨ"),
        ("Because", "-ꯕꯗꯒꯤ"),
        ("So / Therefore", "ꯃꯗꯨꯅ"),
        ("Or", "ꯅꯠꯇ꯭ꯔꯒ"),
        ("If", "-ꯂꯕꯗꯤ"),
        ("Although / Even though", "-ꯕꯁꯨ"),
        ("After", "-ꯈꯔꯕ ꯃꯇꯨꯡꯗ"),
        ("Before", "-ꯇ꯭ꯔꯤꯉꯩꯗ"),
        ("Then", "ꯃꯇꯨꯡꯗ"),
        ("As soon as", "-ꯇ꯭ꯔꯤꯉꯩꯃꯛ"),
        ("Rather than", "-ꯗꯒꯤꯅ"),
        ("Instead of", "-ꯒꯤ ꯃꯍꯨꯠꯇ"),
        ("He came and I went", "ꯃꯍꯥꯛ ꯂꯥꯛꯂꯦ ꯑꯃꯁꯨꯡ ꯑꯩ ꯆꯠꯂꯦ꯫"),
        ("She is smart but lazy", "ꯃꯍꯥꯛ ꯐꯕꯅꯤ ꯑꯗꯨꯕꯨ ꯊꯕꯛ ꯇꯧꯗꯦ꯫"),
        ("Because he is tired", "ꯃꯍꯥꯛ ꯋꯥꯈꯔꯕꯗꯒꯤ"),
        ("If they come, tell me", "ꯃꯈꯣꯏ ꯂꯥꯛꯂꯕꯗꯤ ꯑꯩꯕꯨ ꯍꯥꯏꯕꯤꯌꯨ꯫"),
    ],
},

# ━━━ 589: Combining sentences ━━━
589: {
    "heading": "Sentence combining examples",
    "rows": [
        ("He ate. Then he slept.", "ꯃꯍꯥꯛ ꯆꯥꯈꯔꯦ꯫ ꯃꯇꯨꯡꯗ ꯇꯨꯝꯂꯦ꯫"),
        ("He ate and then slept", "ꯃꯍꯥꯛ ꯆꯥꯈꯔꯦ ꯑꯃꯁꯨꯡ ꯃꯇꯨꯡꯗ ꯇꯨꯝꯂꯦ꯫"),
        ("She came. She cooked.", "ꯃꯍꯥꯛ ꯂꯥꯛꯂꯦ꯫ ꯃꯍꯥꯛ ꯁꯥꯈꯔꯦ꯫"),
        ("She came and cooked", "ꯃꯍꯥꯛ ꯂꯥꯛꯂꯦ ꯑꯃꯁꯨꯡ ꯁꯥꯈꯔꯦ꯫"),
        ("I was tired. I didn't go.", "ꯑꯩ ꯋꯥꯈꯔꯦ꯫ ꯑꯩ ꯆꯠꯈꯔꯗꯦ꯫"),
        ("Because I was tired, I didn't go", "ꯑꯩ ꯋꯥꯈꯔꯕꯗꯒꯤ ꯆꯠꯈꯔꯗꯦ꯫"),
        ("He studied. He passed.", "ꯃꯍꯥꯛ ꯇꯝꯂꯦ꯫ ꯃꯍꯥꯛ ꯄꯥꯁ ꯇꯧꯈꯔꯦ꯫"),
        ("He studied so he passed", "ꯃꯍꯥꯛ ꯇꯝꯂꯕꯗꯒꯤ ꯄꯥꯁ ꯇꯧꯈꯔꯦ꯫"),
        ("I like tea. I don't like coffee.", "ꯑꯩ ꯆꯥ ꯄꯝꯖꯩ꯫ ꯀꯣꯐꯤ ꯄꯝꯗꯦ꯫"),
        ("I like tea but not coffee", "ꯑꯩ ꯆꯥ ꯄꯝꯖꯩ ꯑꯗꯨꯕꯨ ꯀꯣꯐꯤ ꯄꯝꯗꯦ꯫"),
        ("It rained. We stayed home.", "ꯅꯣꯡ ꯇꯥꯛꯂꯦ꯫ ꯑꯩꯈꯣꯏ ꯌꯨꯝꯗ ꯂꯩꯈꯔꯦ꯫"),
        ("Since it rained, we stayed home", "ꯅꯣꯡ ꯇꯥꯛꯂꯕꯗꯒꯤ ꯑꯩꯈꯣꯏ ꯌꯨꯝꯗ ꯂꯩꯈꯔꯦ꯫"),
        ("She ran. She fell.", "ꯃꯍꯥꯛ ꯆꯦꯜꯂꯦ꯫ ꯃꯍꯥꯛ ꯇꯥꯛꯂꯦ꯫"),
        ("She ran and fell", "ꯃꯍꯥꯛ ꯆꯦꯜꯂꯦ ꯑꯃꯁꯨꯡ ꯇꯥꯛꯂꯦ꯫"),
        ("I will come. I will bring food.", "ꯑꯩ ꯂꯥꯛꯀꯅꯤ꯫ ꯆꯤꯟꯖꯥꯛ ꯄꯨꯒꯅꯤ꯫"),
        ("I will come and bring food", "ꯑꯩ ꯂꯥꯛꯀꯅꯤ ꯑꯃꯁꯨꯡ ꯆꯤꯟꯖꯥꯛ ꯄꯨꯒꯅꯤ꯫"),
        ("He is smart. He works hard.", "ꯃꯍꯥꯛ ꯐꯕꯅꯤ ꯑꯃꯁꯨꯡ ꯍꯥꯏꯅ ꯊꯕꯛ ꯇꯧꯏ꯫"),
    ],
},

# ━━━ 590: Compound verbs ━━━
590: {
    "heading": "Compound verb examples",
    "rows": [
        ("Come back", "ꯍꯟꯅ ꯂꯥꯛꯂꯣ꯫"),
        ("Go out", "ꯊꯣꯛꯆꯠꯂꯣ꯫"),
        ("Sit down", "ꯐꯝꯗꯨ꯫"),
        ("Stand up", "ꯂꯦꯞꯊꯣꯛ꯫"),
        ("Run away", "ꯆꯦꯜꯊꯣꯛ꯫"),
        ("Pick up", "ꯊꯪꯒꯠꯂꯣ꯫"),
        ("Put down", "ꯊꯤꯟꯗꯣꯛ꯫"),
        ("Throw away", "ꯊꯛꯊꯔꯣꯛ꯫"),
        ("I came back home", "ꯑꯩ ꯌꯨꯝꯗ ꯍꯟꯅ ꯂꯥꯛꯂꯦ꯫"),
        ("He went out", "ꯃꯍꯥꯛ ꯊꯣꯛꯆꯠꯂꯦ꯫"),
        ("She sat down", "ꯃꯍꯥꯛ ꯐꯝꯗꯨꯂꯦ꯫"),
        ("They stood up", "ꯃꯈꯣꯏ ꯂꯦꯞꯊꯣꯛꯂꯦ꯫"),
        ("The child ran away", "ꯑꯅꯧꯕ ꯑꯗꯨ ꯆꯦꯜꯊꯣꯛꯂꯦ꯫"),
        ("Pick up the pen", "ꯀꯂꯝ ꯊꯪꯒꯠꯂꯣ꯫"),
        ("Put down the bag", "ꯈꯥꯑꯣ ꯊꯤꯟꯗꯣꯛꯂꯣ꯫"),
        ("Throw away the trash", "ꯁꯦꯡꯗꯣꯛꯂꯣ꯫"),
        ("I will come back tomorrow", "ꯑꯩ ꯍꯌꯦꯡ ꯍꯟꯅ ꯂꯥꯛꯀꯅꯤ꯫"),
    ],
},

# ━━━ 591: Active-Passive voice ━━━
591: {
    "heading": "Active-Passive voice examples",
    "rows": [
        ("He eats rice (active)", "ꯃꯍꯥꯛ ꯆꯥꯛ ꯆꯥꯏ꯫"),
        ("Rice is eaten by him (passive)", "ꯆꯥꯛ ꯃꯍꯥꯛꯅ ꯆꯥꯏ꯫"),
        ("She reads a book (active)", "ꯃꯍꯥꯛ ꯂꯥꯏꯔꯤꯛ ꯄꯏ꯫"),
        ("The book is read by her (passive)", "ꯂꯥꯏꯔꯤꯛ ꯃꯍꯥꯛꯅ ꯄꯏ꯫"),
        ("He wrote a letter (active)", "ꯃꯍꯥꯛ ꯆꯤꯠꯊꯤ ꯏꯈꯔꯦ꯫"),
        ("The letter was written by him (passive)", "ꯆꯤꯠꯊꯤ ꯃꯍꯥꯛꯅ ꯏꯈꯔꯦ꯫"),
        ("She cooked food (active)", "ꯃꯍꯥꯛ ꯆꯤꯟꯖꯥꯛ ꯁꯥꯈꯔꯦ꯫"),
        ("Food was cooked by her (passive)", "ꯆꯤꯟꯖꯥꯛ ꯃꯍꯥꯛꯅ ꯁꯥꯈꯔꯦ꯫"),
        ("He broke the glass (active)", "ꯃꯍꯥꯛ ꯒ꯭ꯂꯥꯁ ꯀꯤꯈꯔꯦ꯫"),
        ("The glass was broken by him (passive)", "ꯒ꯭ꯂꯥꯁ ꯃꯍꯥꯛꯅ ꯀꯤꯈꯔꯦ꯫"),
        ("Teacher teaches students (active)", "ꯑꯣꯖꯥꯅ ꯃꯍꯩꯔꯣꯌꯁꯤꯡꯕꯨ ꯇꯝꯍꯟꯂꯤ꯫"),
        ("Students are taught by teacher (passive)", "ꯃꯍꯩꯔꯣꯌꯁꯤꯡ ꯑꯣꯖꯥꯅ ꯇꯝꯍꯟꯂꯤ꯫"),
        ("I saw the film (active)", "ꯑꯩ ꯐꯤꯜꯝ ꯌꯦꯡꯈꯔꯦ꯫"),
        ("The film was seen by me (passive)", "ꯐꯤꯜꯝ ꯑꯩꯅ ꯌꯦꯡꯈꯔꯦ꯫"),
        ("She cleaned the house (active)", "ꯃꯍꯥꯛ ꯌꯨꯝ ꯁꯦꯡꯗꯣꯛꯈꯔꯦ꯫"),
        ("The house was cleaned by her", "ꯌꯨꯝ ꯃꯍꯥꯛꯅ ꯁꯦꯡꯗꯣꯛꯈꯔꯦ꯫"),
        ("He opened the door (active)", "ꯃꯍꯥꯛ ꯊꯣꯡ ꯍꯪꯗꯣꯛꯈꯔꯦ꯫"),
    ],
},

# ━━━ 592: Active-Passive Style 2 ━━━
592: {
    "heading": "Active-Passive Style 2 examples",
    "rows": [
        ("The door was opened", "ꯊꯣꯡ ꯍꯪꯗꯣꯛꯈꯔꯦ꯫"),
        ("The food was eaten", "ꯆꯤꯟꯖꯥꯛ ꯆꯥꯈꯔꯦ꯫"),
        ("The book was read", "ꯂꯥꯏꯔꯤꯛ ꯄꯈꯔꯦ꯫"),
        ("The letter was written", "ꯆꯤꯠꯊꯤ ꯏꯈꯔꯦ꯫"),
        ("The window was closed", "ꯇꯛꯅꯩꯕꯥꯛ ꯊꯤꯡꯈꯔꯦ꯫"),
        ("The glass was broken", "ꯒ꯭ꯂꯥꯁ ꯀꯤꯈꯔꯦ꯫"),
        ("The rice was cooked", "ꯆꯥꯛ ꯁꯥꯈꯔꯦ꯫"),
        ("The work was done", "ꯊꯕꯛ ꯇꯧꯈꯔꯦ꯫"),
        ("The song was sung", "ꯏꯁꯩ ꯁꯀꯈꯔꯦ꯫"),
        ("The house was built", "ꯌꯨꯝ ꯁꯥꯈꯔꯦ꯫"),
        ("The game was played", "ꯁꯅꯥ ꯁꯥꯈꯔꯦ꯫"),
        ("The clothes were washed", "ꯐꯤ ꯀꯨꯝꯈꯔꯦ꯫"),
        ("The tree was planted", "ꯎꯄꯥꯜ ꯂꯧꯈꯔꯦ꯫"),
        ("The bag was carried", "ꯈꯥꯑꯣ ꯄꯨꯈꯔꯦ꯫"),
        ("The dress was bought", "ꯐꯤ ꯂꯩꯈꯔꯦ꯫"),
        ("The water was drunk", "ꯏꯁꯤꯡ ꯊꯛꯈꯔꯦ꯫"),
        ("The child was taught", "ꯑꯅꯧꯕ ꯇꯝꯍꯟꯈꯔꯦ꯫"),
    ],
},

# ━━━ 593: To Feel / To Think ━━━
593: {
    "heading": "\"To feel\" / \"to think\" examples",
    "rows": [
        ("I feel happy", "ꯑꯩ ꯅꯨꯡꯉꯥꯏ ꯐꯥꯑꯣꯏ꯫"),
        ("I feel sad", "ꯑꯩ ꯋꯥꯈꯜ ꯂꯩꯏ꯫"),
        ("He feels cold", "ꯃꯍꯥꯛ ꯈꯪ ꯐꯥꯑꯣꯏ꯫"),
        ("She feels hot", "ꯃꯍꯥꯛ ꯑꯉꯥꯑꯣ ꯐꯥꯑꯣꯏ꯫"),
        ("I feel tired", "ꯑꯩ ꯋꯥꯈꯜ ꯐꯥꯑꯣꯏ꯫"),
        ("I think he is right", "ꯑꯩ ꯃꯍꯥꯛ ꯑꯆꯨꯝꯕ ꯍꯥꯏꯔꯤ ꯋꯥꯈꯜ ꯂꯧꯏ꯫"),
        ("He thinks she is beautiful", "ꯃꯍꯥꯛ ꯃꯍꯥꯛ ꯐꯖꯩ ꯋꯥꯈꯜ ꯂꯧꯏ꯫"),
        ("I think it will rain", "ꯑꯩ ꯅꯣꯡ ꯇꯥꯛꯀꯅꯤ ꯋꯥꯈꯜ ꯂꯧꯏ꯫"),
        ("She thinks he is coming", "ꯃꯍꯥꯛ ꯃꯍꯥꯛ ꯂꯥꯛꯔꯤ ꯋꯥꯈꯜ ꯂꯧꯏ꯫"),
        ("I don't think so", "ꯑꯩ ꯃꯗꯨꯒꯨꯝꯅ ꯋꯥꯈꯜ ꯂꯧꯗꯦ꯫"),
        ("I feel hungry", "ꯑꯩ ꯆꯥꯛ ꯈꯣꯡ ꯍꯥꯝꯏ꯫"),
        ("He feels sorry", "ꯃꯍꯥꯛ ꯅꯨꯡꯉꯥꯏꯖꯩ ꯐꯥꯑꯣꯏ꯫"),
        ("What do you think?", "ꯅꯪ ꯀꯔꯤ ꯋꯥꯈꯜ ꯂꯧꯕꯒꯦ?"),
        ("I feel something is wrong", "ꯀꯔꯤꯁꯨ ꯑꯃ ꯑꯆꯨꯝꯕ ꯅꯠꯇꯦ ꯐꯥꯑꯣꯏ꯫"),
        ("She thinks about her mother", "ꯃꯍꯥꯛ ꯃꯍꯥꯛꯀꯤ ꯏꯃꯥꯕꯨ ꯋꯥꯈꯜ ꯂꯧꯏ꯫"),
        ("I don't feel well", "ꯑꯩ ꯅꯥꯕ ꯐꯕ ꯐꯥꯑꯣꯏꯗꯦ꯫"),
        ("He thinks he is right", "ꯃꯍꯥꯛ ꯃꯍꯥꯛ ꯑꯆꯨꯝꯕ ꯍꯥꯏꯔꯤ ꯋꯥꯈꯜ ꯂꯧꯏ꯫"),
    ],
},

# ━━━ 594: Idioms Part 1 ━━━
594: {
    "heading": "Idiom examples – Part 1",
    "rows": [
        ("To have an empty stomach", "ꯈꯣꯡ ꯂꯥꯛꯕ"),
        ("To be in trouble", "ꯑꯋꯥꯇꯕꯗ ꯂꯩꯕ"),
        ("To eat one's words", "ꯃꯍꯥꯛꯀꯤ ꯋꯥ ꯍꯟꯅ ꯂꯧꯕ"),
        ("To see red / To be angry", "ꯁꯥꯅꯕ"),
        ("To turn a blind eye", "ꯃꯤꯠ ꯊꯤꯡꯅ ꯂꯩꯕ"),
        ("Crocodile tears", "ꯏꯀꯥꯏ ꯀꯞꯕ"),
        ("To lend a hand", "ꯃꯇꯦꯡ ꯄꯥꯡꯕ"),
        ("Every cloud has a silver lining", "ꯃꯐꯝ ꯈꯨꯗꯤꯡꯃꯛꯇ ꯐꯕ ꯂꯩꯏ꯫"),
        ("He is hungry (idiom)", "ꯃꯍꯥꯛꯇ ꯈꯣꯡ ꯂꯥꯛꯂꯦ꯫"),
        ("She helped me (idiom)", "ꯃꯍꯥꯛꯅ ꯑꯩꯕꯨ ꯃꯇꯦꯡ ꯄꯥꯡꯈꯔꯦ꯫"),
        ("He turned a blind eye", "ꯃꯍꯥꯛ ꯃꯤꯠ ꯊꯤꯡꯅ ꯂꯩꯈꯔꯦ꯫"),
        ("Don't cry crocodile tears", "ꯏꯀꯥꯏ ꯀꯞꯂꯣꯌꯨ꯫"),
        ("Hard work pays off", "ꯍꯥꯏꯅ ꯊꯕꯛ ꯇꯧꯕꯅ ꯐꯨꯡꯏ꯫"),
        ("Practice makes perfect", "ꯍꯣꯠꯅꯕꯅ ꯐꯕ ꯑꯣꯏꯏ꯫"),
        ("Slow and steady wins the race", "ꯇꯞꯅ ꯑꯃꯁꯨꯡ ꯆꯦꯛꯁꯤꯟꯅ ꯃꯥꯏꯄꯥꯛꯂꯤ꯫"),
        ("He is in trouble", "ꯃꯍꯥꯛ ꯑꯋꯥꯇꯕꯗ ꯂꯩꯏ꯫"),
        ("She always lends a hand", "ꯃꯍꯥꯛ ꯃꯇꯝ ꯄꯨꯝꯕꯗ ꯃꯇꯦꯡ ꯄꯥꯡꯏ꯫"),
    ],
},

# ━━━ 595: Idioms Part 2 ━━━
595: {
    "heading": "Idiom examples – Part 2",
    "rows": [
        ("To keep one's word", "ꯋꯥ ꯊꯨꯕ"),
        ("To lose face / To be ashamed", "ꯃꯥꯏ ꯅꯣꯛꯕ"),
        ("To add fuel to fire", "ꯃꯩꯗ ꯁꯤꯡ ꯊꯕ"),
        ("To be on cloud nine", "ꯌꯥꯝꯅ ꯅꯨꯡꯉꯥꯏ ꯐꯥꯑꯣꯕ"),
        ("Break the ice", "ꯋꯥꯔꯤ ꯍꯧꯕ"),
        ("To bite the bullet", "ꯊꯧꯅ ꯐꯕ"),
        ("Actions speak louder than words", "ꯇꯧꯕꯅ ꯋꯥ ꯉꯥꯡꯕꯗꯒꯤ ꯐꯅꯤ꯫"),
        ("He kept his word", "ꯃꯍꯥꯛ ꯋꯥ ꯊꯨꯈꯔꯦ꯫"),
        ("She lost face", "ꯃꯍꯥꯛ ꯃꯥꯏ ꯅꯣꯛꯈꯔꯦ꯫"),
        ("Don't add fuel to fire", "ꯃꯩꯗ ꯁꯤꯡ ꯊꯂꯣꯌꯨ꯫"),
        ("He was on cloud nine", "ꯃꯍꯥꯛ ꯌꯥꯝꯅ ꯅꯨꯡꯉꯥꯏꯂꯦ꯫"),
        ("She broke the ice", "ꯃꯍꯥꯛ ꯋꯥꯔꯤ ꯍꯧꯈꯔꯦ꯫"),
        ("Don't put all eggs in one basket", "ꯃꯐꯝ ꯑꯃꯗ ꯄꯨꯝꯅꯃꯛ ꯊꯤꯟꯂꯣꯌꯨ꯫"),
        ("Better late than never", "ꯊꯦꯡꯕ ꯑꯗꯨꯕꯨ ꯅꯠꯇꯕꯗꯒꯤ ꯐꯅꯤ꯫"),
        ("A friend in need is a friend indeed", "ꯃꯔꯤ ꯃꯇꯝꯗ ꯃꯇꯦꯡ ꯄꯥꯡꯕ ꯃꯔꯨꯞ ꯑꯆꯨꯝꯕꯅꯤ꯫"),
        ("Every dog has its day", "ꯃꯤ ꯈꯨꯗꯤꯡꯃꯛꯇ ꯃꯇꯝ ꯂꯥꯛꯂꯤ꯫"),
        ("He bit the bullet", "ꯃꯍꯥꯛ ꯊꯧꯅ ꯐꯈꯔꯦ꯫"),
    ],
},

# ━━━ 596: If-Then Style 2 ━━━
596: {
    "heading": "\"If-Then\" Style 2 examples",
    "rows": [
        ("If I had money, I would buy it", "ꯑꯩꯗ ꯄꯥꯏꯁꯥ ꯂꯩꯔꯕꯗꯤ, ꯂꯩꯅꯤꯡꯉꯩ꯫"),
        ("If he had studied, he would have passed", "ꯃꯍꯥꯛ ꯇꯝꯂꯕꯗꯤ, ꯄꯥꯁ ꯇꯧꯅꯤꯡꯉꯩ꯫"),
        ("If she had come, we would have eaten", "ꯃꯍꯥꯛ ꯂꯥꯛꯂꯕꯗꯤ, ꯑꯩꯈꯣꯏ ꯆꯥꯅꯤꯡꯉꯩ꯫"),
        ("If it hadn't rained, I would have gone", "ꯅꯣꯡ ꯇꯥꯛꯈꯔꯗꯕꯗꯤ, ꯑꯩ ꯆꯠꯅꯤꯡꯉꯩ꯫"),
        ("If I were you, I would go", "ꯑꯩ ꯅꯪ ꯑꯣꯏꯔꯕꯗꯤ, ꯆꯠꯅꯤꯡꯉꯩ꯫"),
        ("If they had helped, we would have won", "ꯃꯈꯣꯏ ꯃꯇꯦꯡ ꯄꯥꯡꯂꯕꯗꯤ, ꯑꯩꯈꯣꯏ ꯃꯥꯏꯄꯥꯛꯅꯤꯡꯉꯩ꯫"),
        ("If he had called, I would have come", "ꯃꯍꯥꯛ ꯀꯧꯂꯕꯗꯤ, ꯑꯩ ꯂꯥꯛꯅꯤꯡꯉꯩ꯫"),
        ("If I had known, I would have told you", "ꯑꯩ ꯈꯪꯂꯕꯗꯤ, ꯅꯪꯗ ꯍꯥꯏꯅꯤꯡꯉꯩ꯫"),
        ("If she cooked, we would eat", "ꯃꯍꯥꯛ ꯁꯥꯂꯕꯗꯤ, ꯑꯩꯈꯣꯏ ꯆꯥꯅꯤꯡꯉꯩ꯫"),
        ("If he worked hard, he would succeed", "ꯃꯍꯥꯛ ꯍꯥꯏꯅ ꯊꯕꯛ ꯇꯧꯂꯕꯗꯤ, ꯃꯥꯏꯄꯥꯛꯅꯤꯡꯉꯩ꯫"),
        ("If I were a bird, I would fly", "ꯑꯩ ꯎꯆꯦꯛ ꯑꯣꯏꯔꯕꯗꯤ, ꯄꯥꯏꯅꯤꯡꯉꯩ꯫"),
        ("If she had asked, I would have helped", "ꯃꯍꯥꯛ ꯍꯪꯂꯕꯗꯤ, ꯑꯩ ꯃꯇꯦꯡ ꯄꯥꯡꯅꯤꯡꯉꯩ꯫"),
        ("If he had eaten, he wouldn't be hungry", "ꯃꯍꯥꯛ ꯆꯥꯂꯕꯗꯤ, ꯈꯣꯡ ꯂꯥꯛꯅꯤꯡꯉꯩꯗꯦ꯫"),
        ("If it were sunny, I would go out", "ꯅꯨꯃꯤꯠ ꯊꯣꯛꯂꯕꯗꯤ, ꯑꯩ ꯊꯣꯛꯆꯠꯅꯤꯡꯉꯩ꯫"),
        ("If I had woken up early, I wouldn't be late", "ꯑꯩ ꯊꯨꯅ ꯍꯛꯂꯕꯗꯤ, ꯊꯦꯡꯅꯤꯡꯉꯩꯗꯦ꯫"),
        ("If she had seen me, she would have called", "ꯃꯍꯥꯛ ꯑꯩꯕꯨ ꯎꯂꯕꯗꯤ, ꯀꯧꯅꯤꯡꯉꯩ꯫"),
        ("If we had time, we would play", "ꯑꯩꯈꯣꯏꯗ ꯃꯇꯝ ꯂꯩꯔꯕꯗꯤ, ꯁꯥꯅꯤꯡꯉꯩ꯫"),
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
        chapter["blocks"] = [new_table]
        chapter.pop("intro", None)
        chapter.pop("content", None)
        updated += 1
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sys.stdout.buffer.write(f"Updated {updated} pattern lessons (571-596) in data_meitei.json\n".encode("utf-8"))

if __name__ == "__main__":
    main()
