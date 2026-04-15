# -*- coding: utf-8 -*-
"""
Build data_kashmiri.json from data_nepali.json shape, replacing lesson text and
table rows with Kashmiri material sourced from published phrase lists and grammar
references — not ad-hoc English-to-Kashmiri translation.

Primary public references used for gloss + Kashmiri lines:
  https://www.omniglot.com/language/phrases/kashmiri.htm
  https://en.wikivoyage.org/wiki/Kashmiri_phrasebook
  https://upasnakakroo.co/2017/02/12/kashmiri-phrases/ (proverb / mirror line)
Grammar-style examples (Roman as in widely cited pedagogical materials):
  Omkar N. Koul / Spoken Kashmiri–style sentences (present/future/aux chu, etc.)

Run: py -3 generate_kashmiri_data.py
"""
from __future__ import annotations

import copy
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "data_nepali.json"
OUT = ROOT / "data_kashmiri.json"

# Tags help pick rows for a lesson title (lowercased substring match).
# Phrases: English gloss, Kashmiri (Devanagari where standard / from sources), Roman Kashmiri
# Sources noted in comments — keep pedagogical variety and medium-length lines where possible.

PHRASE_BANK: list[tuple[str, str, str, frozenset[str]]] = [
    # Lesson 501 — lexical examples (phrasebook / Omniglot glosses; Devanagari as in public tables)
    ("Welcome — word.", "वलिव", "Waliv", frozenset({"501", "alphabet"})),
    ("Thank you — word.", "शुकिया", "Shukriya", frozenset({"501", "alphabet"})),
    ("Please — word.", "मेहरबॅानी", "Meharbeūnee", frozenset({"501", "alphabet"})),
    ("Sorry — word.", "माफ कॅरिव", "Maap' keuriv", frozenset({"501", "alphabet"})),
    ("Yes — word.", "आ", "Aa", frozenset({"501", "alphabet"})),
    ("No — word.", "ना", "Na", frozenset({"501", "alphabet"})),
    ("Hello — Namaskar.", "नमस्कार", "Namaskār", frozenset({"501", "alphabet"})),
    ("Peace — Assalām ‘alaikum.", "असलामु अलैकुम", "Assalām ‘alaikum", frozenset({"501", "alphabet"})),
    ("Good night — phrase.", "शबे खैर", "Shabey k'eūr", frozenset({"501", "alphabet"})),
    ("How are you? — phrase.", "तोहय छिवा वारय?", "Tohy ch'ivaa vaarai?", frozenset({"501", "alphabet"})),
    ("What is your name? — phrase.", "त्वहि क्या छु नाव?", "Twahi kyaa ch'u naav?", frozenset({"501", "alphabet"})),
    ("I understand — phrase.", "आऊई समझ", "Aaooee samajh", frozenset({"501", "alphabet"})),
    ("I don’t understand — phrase.", "ब’ छुस न’ ज़ानान", "Biu ch'us niu zaanaan", frozenset({"501", "alphabet"})),
    ("Where is the toilet? — phrase.", "टायलेट कति छि?", "Ṭaaylet kati ch'u!", frozenset({"501", "alphabet"})),
    ("How much is this? — phrase.", "यि का’तिस छु?", "Yi keūtis ch'u", frozenset({"501", "alphabet"})),
    # Omniglot + common phrasebook forms
    ("Welcome.", "वलिव", "Waliv", frozenset({"greeting", "basics", "571"})),
    ("Hello — Namaskar (to Hindus).", "नमस्कार", "Namaskār", frozenset({"greeting", "basics", "571"})),
    ("Peace be upon you — to Muslims.", "असलामु अलैकुम", "Assalām ‘alaikum", frozenset({"greeting", "571"})),
    ("How are you?", "तोहय छिवा वारय?", "Tohy ch'ivaa vaarai?", frozenset({"greeting", "basics", "528", "571"})),
    ("Fine, thank you — and you?", "वारय, शुकिया । त’ तीहय?", "Waaray, shukriyaa tiu tohy?", frozenset({"greeting", "571"})),
    ("Long time no see!", "वरिया काल गव न म्येलनसि!", "Variya kaal gov na myelnasi!", frozenset({"greeting", "571"})),
    ("What is your name?", "त्वहि क्या छु नाव?", "Twahi kyaa ch'u naav?", frozenset({"greeting", "basics", "510", "571"})),
    ("My name is …", "मे छु नाव …", "Ma chho naw …", frozenset({"greeting", "basics", "571"})),
    ("Where are you from?", "त्वहि कतिक छु?", "Tvahi katika chu?", frozenset({"greeting", "basics", "528"})),
    ("Pleased to meet you.", "मे सप’ज़ खोशी त्वहि मीलिध ।", "Me sapiuz k'oshee twahu meelit'", frozenset({"greeting", "571"})),
    ("Good night.", "शबे खैर ।", "Shabey k'eūr", frozenset({"greeting", "571"})),
    ("Goodbye — Khuda hafiz (Muslim).", "खुदा हाफिज़", "Khuda hāfiz", frozenset({"greeting", "571"})),
    ("Goodbye — Namaskar (Hindus).", "नमस्कार", "Namaskār", frozenset({"greeting", "571"})),
    ("Good luck — Inshaallah (Muslims).", "इंशाल्लाह", "Inshaallaah", frozenset({"greeting", "571"})),
    ("Good luck — Vārakāra (Hindus).", "वारकार", "Vārakāra", frozenset({"greeting", "571"})),
    ("Cheers! Good health!", "ज़ुव थवुन ठीक", "Zuv thavun theek", frozenset({"greeting", "571"})),
    ("Have a safe journey (Muslims).", "नैर ख़ौदायस हवाल", "Nair khaudaayas havaal", frozenset({"greeting", "571"})),
    ("Have a safe journey (Hindus).", "नैर भगवानस हवाल", "Nair bhagavaanas havaal", frozenset({"greeting", "571"})),
    ("Do you understand?", "त्वहि छा फिकिरि तरान?", "Tvahi chaa phikiri taraan?", frozenset({"562", "understand"})),
    ("I understand.", "आऊई समझ", "Aaooee samajh", frozenset({"562", "understand"})),
    ("I don’t understand (m).", "ब’ छुस न’ ज़ानान ।", "Biu ch'us niu zaanaan", frozenset({"562", "understand"})),
    ("I don’t know.", "मे छु न पै", "Me chhu ne pai", frozenset({"556", "know"})),
    ("Yes.", "आ", "Aa", frozenset({"basics", "529"})),
    ("No.", "ना", "Na", frozenset({"basics", "529"})),
    ("Maybe.", "शायद", "Shayed", frozenset({"576", "uncertain"})),
    ("Please speak more slowly.", "तोहय हेकिवा वार’ वार’ वॅनिव ।", "Tohy hekivaa vaariu vaariu veuniv", frozenset({"559", "request", "575"})),
    ("Please say that again.", "तोहय हेकिवा दुबार’ वॅनिथ ।", "Tohy hekivaa dubaariu veunit'", frozenset({"575", "request"})),
    ("Please write it down.", "यि लिखिव", "Yi Likhiv", frozenset({"575", "request"})),
    ("Do you speak English?", "तोहय छिवा अंगरीज़ी बोलान?", "Tohy chivā angrīzī bolān", frozenset({"528", "basics"})),
    ("Do you speak Kashmiri?", "त्स्के छुके कॉशुर बोलान?", "Tske chhuke Koshur bolaan?", frozenset({"528", "basics"})),
    ("Yes, a little (reply).", "आ, थोडा स", "Aa, thoda sa", frozenset({"528"})),
    ("How much is this?", "यि का’तिस छु?", "Yi keūtis ch'u", frozenset({"547", "basics"})),
    ("Sorry.", "माफ कॅरिव ।", "Maap' keuriv", frozenset({"basics", "571"})),
    ("Please.", "मेहरबॅानी ।", "Meharbeūnee", frozenset({"request", "575"})),
    ("Thank you.", "शुकिया", "Shukriya", frozenset({"greeting", "basics", "571"})),
    ("Where is the toilet?", "टायलेट कति छि?", "Ṭaaylet kati ch'u!", frozenset({"547", "basics"})),
    ("Excuse me — to get past.", "वथ त्रॅाविव ।", "Vat' treūviv", frozenset({"575"})),
    ("Help!", "मदथ करिव!", "Madatha kariva!", frozenset({"574", "exclamation"})),
    ("Stop!", "ठहर!", "Ṭeuhar!", frozenset({"574", "exclamation"})),
    ("Fire!", "नार!", "Naar!", frozenset({"574", "exclamation"})),
    ("Call the police!", "बुलॅाविव पुलीस!", "Buleūviv pulees!", frozenset({"574", "exclamation"})),
    ("Go away!", "च़ल!", "Tsa!", frozenset({"574", "exclamation"})),
    ("Get well soon.", "गचिव ठीक जल्द", "Gachiv theek jald", frozenset({"greeting", "571"})),
    ("Congratulations!", "पोश्ते मुबारक", "Poshte Mubarak", frozenset({"greeting", "571"})),
    ("Happy birthday!", "त्स्के छुय वोहुरवोद मुबारक!", "Tske chhuy wohurwod mubarak!", frozenset({"greeting", "571"})),
    ("Happy New Year / Christmas greeting.", "नवरेह मुबारक", "Navreh mubarak", frozenset({"greeting", "571"})),
    ("One language is never enough.", "अख़ ज़बान छु न ज़न्ह काफ़ी", "Akh zabaan chhu na zanh kaefi", frozenset({"idiom", "594"})),
    # Wikivoyage — Basics / Problems / Time / Directions (medium lines)
    ("Hello — informal.", "हलो", "halo", frozenset({"greeting", "basics"})),
    ("How are you? (variant)", "तोह छिव वॅरी?", "Toh chiv väri", frozenset({"greeting"})),
    ("Fine, thank you — polite.", "आहँस, मेहरबानी", "Ähansa, Me-Hur-Ba-e-Ni", frozenset({"greeting", "571"})),
    ("What is your name? (variant)", "चे क्या छुय नाव?", "Çê kyāh chuy nāv", frozenset({"greeting", "528"})),
    ("My name is _____.", "बे छुस _____", "Be chus _____", frozenset({"greeting", "528"})),
    ("Nice to meet you.", "तोहि मेल्यिथ गायि म वारय खुश्ति", "Tö-hi Mel-Yiţh Gā-Yi Ma War-Yah Kush-Ti", frozenset({"greeting", "571"})),
    ("Please — Balai lagai.", "बलै लगै", "Ba-Lai La-Gai", frozenset({"request", "575"})),
    ("Thank you — Meharbaeni.", "मेहरबाइनी", "Me-Hur-Ba-e-Ni", frozenset({"greeting", "571"})),
    ("Yes — Ên.", "एन्", "Ên", frozenset({"basics"})),
    ("I can’t speak Kashmiri.", "मे चुने कॅशुर तगान", "Mê chunė käshur tagān", frozenset({"528", "549"})),
    ("Do you speak English?", "चे चुखे अंग्रीज़ बोलान?", "Çė chukhė aņgrīz bolān", frozenset({"528", "549"})),
    ("I don’t understand.", "मे चुने फिक्री तगान", "Mê chunė phikrī tagān", frozenset({"562", "understand"})),
    ("What is this?", "यि क्या छु?", "Yi Kyāh chu?", frozenset({"558", "basics"})),
    ("What do you want?", "चे क्या गछिय?", "Çê Kyāh gaçhiy?", frozenset({"550", "want"})),
    ("What time is it?", "वखेत क्या आव?", "Vakhėt kyāh āv?", frozenset({"537", "time"})),
    ("It is five o’clock.", "वखेत छु पाँचि बजि", "Vakhėt chu pāņçi baji", frozenset({"537", "time"})),
    ("Where does the bus leave from?", "बस कति पॅथि छि नेरान?", "Bas kati pêţhė chi nerān?", frozenset({"547", "travel"})),
    ("Left.", "खोवुर", "Kho-vur", frozenset({"547", "direction"})),
    ("Right.", "दछ्यन", "Daçhyan", frozenset({"547", "direction"})),
    ("How many kilometres?", "कच किलोमितर दूर?", "Kaç kilomitar dūr?", frozenset({"547", "travel"})),
    ("How far is the city?", "शहर कोताह दूर छु?", "Shāhr kotāh dūr chu?", frozenset({"547", "travel"})),
    ("Where is the taxi?", "टैक्सी कति छु?", "Taxi kati chu?", frozenset({"547", "travel"})),
    ("Where is the hotel?", "होटल कति छु?", "Hotel kati chu?", frozenset({"547", "travel"})),
    ("Where is the restaurant?", "रेस्टोरेंट कति छु?", "Restaurant kati chu?", frozenset({"547", "travel"})),
    ("How much is it?", "यि कोताह छु?", "Yi kotāh chu?", frozenset({"547", "basics"})),
    ("Who is the officer here?", "येति कुस छु अफ़सर?", "Yêti kus chu aphsar?", frozenset({"559", "formal"})),
    # Numbers — Wikivoyage
    ("Zero.", "सिफ़र", "Siphar", frozenset({"number", "501"})),
    ("One.", "अख", "Akh", frozenset({"number", "501"})),
    ("Two.", "ज़े", "Zė", frozenset({"number", "501"})),
    ("Three.", "त्रे", "Trê", frozenset({"number", "501"})),
    ("Four.", "चोर", "Çor", frozenset({"number", "501"})),
    ("Five.", "पाँच", "Pāņçh", frozenset({"number", "501"})),
    ("Ten.", "दाह", "Dāh", frozenset({"number", "501"})),
    # Colors — Wikivoyage
    ("Black.", "क्रूहुन", "Krūhun", frozenset({"548", "color"})),
    ("White.", "सफ़ेद", "Saphed", frozenset({"548", "color"})),
    ("Red.", "वोज़ुल", "Vözul", frozenset({"548", "color"})),
    ("Green.", "सबेज़", "Sabėz", frozenset({"548", "color"})),
    ("Blue.", "न्यूल", "Ņyūl", frozenset({"548", "color"})),
    ("Yellow.", "ल्योदुर", "Lyōdur", frozenset({"548", "color"})),
    # Textbook-style grammar examples (Roman widely cited; see Omkar N. Koul / Spoken Kashmiri materials)
    ("I am going to the market.", "ब चुस बाज़ार गतशान", "b chus ba:zar gatsha:n", frozenset({"present", "continuous", "543", "515"})),
    ("You are reading a book.", "त्स चुख / चाख किताब परान", "ts chukh / chakh kita:b para:n", frozenset({"present", "continuous", "515"})),
    ("He is drinking tea.", "सु चु / स च चाय चेवान", "su chu / s cha ca:y ceva:n", frozenset({"present", "continuous", "515"})),
    ("He is a doctor.", "सु चु दक्तर", "su chu daktar", frozenset({"present", "514", "be"})),
    ("She is tall.", "स च ज़ीत", "s cha zi:t", frozenset({"present", "514", "548"})),
    ("I will eat food.", "बि खामि बाति", "bi kh'ami bati", frozenset({"future", "516", "543"})),
    ("I will stay in Delhi.", "बि रोज़ि दिलि", "bi ro:zi dili", frozenset({"future", "516"})),
    ("I cannot go to Delhi.", "ब हेक न दिलि गतशिथ", "b hek n dili gətshith", frozenset({"future", "549", "cannot"})),
    ("He can read this book.", "तिम हेकन यि किताब परिथ", "tim hekan yi kita:b pərith", frozenset({"549", "can"})),
    # Proverb — koshur.org style (quoted in collections; medium length)
    ("Our hearts are like a mirror — as you see me, so I appear to you.", "दिल ब दिल गव आईनह, युथ वुछहम, त्यथ वुछय", "Dil ba dil gav aínah; yuth wuchham, tyuth wuchchay", frozenset({"proverb", "idiom", "594", "552"})),
    # Kashmiri Phrases blog (Upasna Kakroo) — one classic line
    ("Hearts are mirrors: the way you look at me, so I will look at you.", "दिल ब दिल गव आईनह", "Dil ba dil gav aínah", frozenset({"idiom", "594"})),
    ("I love you (common phrase).", "त्स्के छुक म्योन जिगुर", "Tske chhuk myon jigur", frozenset({"560", "like"})),
    ("I miss you.", "मे छु च्योन याद यिवान", "Me chhu chyon yaad yiwaan", frozenset({"560", "like"})),
    ("I miss you — variant.", "मे छु च्योन याद यिवान", "Me chhu chyon yaad yiwaan", frozenset({"560"})),
    ("Reply to thank you: don’t mention it.", "कीहीन छु न परवाै", "Kiheen chhu ne parvaai", frozenset({"greeting", "571"})),
    ("Do you come here often? (m)", "चे छुक यिवान योर वरिया?", "Che chhuk yiwan yor variya?", frozenset({"528"})),
    ("Do you come here often? (f)", "चे छिक यिवान योर वरिया?", "Che chhik yiwan yor variya?", frozenset({"528"})),
    ("Would you like to dance with me?", "चन ख़ा डांस म्यांन साइथ?", "Chan khha dance minan sith?", frozenset({"528", "request"})),
    ("This gentleman will pay for everything.", "ये मर्द दी सॅर्सि हत्र पोंस", "Ye mard dee saersi hatra pons", frozenset({"559", "formal"})),
    ("How do you say … in Kashmiri?", "… उस किथ पॅथ छे दपान कशिर मंज़?", "... us kith paeth chhe dapaan kashir manz?", frozenset({"583", "583", "meaning"})),
    ("Speak to me in Kashmiri.", "चे कर मे साथ कशिर पॅथ कथ", "Che kar mae seath kashir peth kath", frozenset({"528", "559"})),
    ("Do you speak a language other than Kashmiri?", "तोहि छुव दोयुम भाषा तगान?", "Tohi chhuv doyum bhasha tagaan?", frozenset({"528"})),
    ("Leave me alone!", "चे त्र मे कुनिज़ोन!", "Che tra mae kunizon!", frozenset({"574"})),
    # Extra medium lines for variety (Omniglot / phrasebook tone)
    ("My hovercraft is full of eels (humorous phrasebook).", "म्योन होवरक्राफ्ट छु ईलव सीथ भरिथ", "Myon hovercraaft chhu eelav seeth bharith", frozenset({"idiom", "594"})),
    ("I am going to the market — present continuous.", "ब चुस बाज़ार गतशान", "b chus ba:zar gatsha:n", frozenset({"543", "going"})),
    ("Please speak slowly — again.", "तोहय हेकिवा वार’ वार’ वॅनिव ।", "Tohy hekivaa vaariu vaariu veuniv", frozenset({"575", "request"})),
    ("Where are you from?", "त्वहि कतिक छु?", "Tvahi katika chu?", frozenset({"greeting", "528"})),
    ("I am from … (m).", "ब’ छुस … रोज़ां …", "Biu ch'us ... rozaan", frozenset({"greeting", "528"})),
    ("I am from … (f).", "ब’ छस … रोज़ां …", "Biu ch'as ... rozaan", frozenset({"greeting", "528"})),
]

# Ensure we have enough variety: duplicate bank with alternate tags for weak matches
def score_row(title: str, lesson_id: int, tags: frozenset[str]) -> int:
    t = title.lower()
    lid = str(lesson_id)
    s = 0
    if lid in tags:
        s += 50
    if lesson_id == 501 and "501" in tags:
        s += 45
    if "alphabet" in t and "501" in tags:
        s += 35
    if "greeting" in tags and any(x in t for x in ("greeting", "wishes", "blessing", "571")):
        s += 40
    if "request" in tags and "request" in t:
        s += 35
    if "exclamation" in tags and "exclamation" in t:
        s += 35
    if "present" in tags or "continuous" in tags:
        if "present" in t or "continuous" in t or "515" in lid:
            s += 30
    if "future" in tags and ("future" in t or "516" in t or "going" in t):
        s += 30
    if "can" in tags and ("can" in t or "able" in t or "549" in lid):
        s += 30
    if "understand" in tags and ("understand" in t or "562" in lid):
        s += 30
    if "know" in tags and ("know" in t or "556" in lid):
        s += 25
    if "time" in tags and ("time" in t or "537" in lid):
        s += 25
    if "color" in tags and ("adjective" in t or "548" in lid):
        s += 25
    if "direction" in tags or "travel" in tags:
        if "preposition" in t or "547" in lid or "travel" in t:
            s += 20
    if "idiom" in tags and ("idiom" in t or "594" in lid or "595" in lid):
        s += 30
    if "proverb" in tags:
        s += 20
    if "basics" in tags:
        s += 5
    return s


def pick_rows(title: str, lesson_id: int, n: int) -> list[list[str]]:
    ranked: list[tuple[int, tuple[str, str, str, frozenset[str]]]] = []
    for row in PHRASE_BANK:
        en, ks, tr, tags = row
        sc = score_row(title, lesson_id, tags)
        ranked.append((sc, row))
    ranked.sort(key=lambda x: -x[0])
    out: list[list[str]] = []
    seen = set()
    for sc, row in ranked:
        en, ks, tr, _ = row
        if en in seen:
            continue
        if sc > 0 or len(out) < n:
            out.append([en, ks, tr])
            seen.add(en)
        if len(out) >= n:
            break
    # Fallback: fill from full bank
    i = 0
    while len(out) < n:
        en, ks, tr, _ = PHRASE_BANK[i % len(PHRASE_BANK)]
        i += 1
        if en in seen:
            continue
        out.append([en, ks, tr])
        seen.add(en)
    return out[:n]


def transform_lesson(lesson: dict) -> dict:
    lesson = copy.deepcopy(lesson)
    lid = lesson.get("id", 0)
    title = lesson.get("title", "")

    lesson["title"] = title.replace("Nepali", "Kashmiri")
    if "content" in lesson:
        lesson["content"] = (
            lesson["content"]
            .replace("Nepali", "Kashmiri")
            .replace("नेपाली", "कॉशुर (Kashmiri)")
        )
    if "intro" in lesson:
        lesson["intro"] = (
            lesson["intro"]
            .replace("Nepali", "Kashmiri")
            .replace("नेपाली", "कॉशुर")
        )

    for key in ("tables", "blocks"):
        arr = lesson.get(key)
        if not arr:
            continue
        for block in arr:
            if block.get("heading"):
                block["heading"] = block["heading"].replace("Nepali", "Kashmiri")
            headers = list(block.get("headers") or [])
            rows = block.get("rows") or []
            if not rows:
                continue
            if "Nepali" in headers:
                block["headers"] = ["Kashmiri" if h == "Nepali" else h for h in headers]
                headers = list(block["headers"])
            if headers == ["English", "Kashmiri", "Transliteration"]:
                block["rows"] = pick_rows(title, lid, len(rows))
            elif headers == ["Letter", "Transliteration"]:
                continue

    return lesson


def main() -> None:
    data = json.loads(SRC.read_text(encoding="utf-8"))
    out = [transform_lesson(l) for l in data]
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Wrote", OUT, "lessons:", len(out))


if __name__ == "__main__":
    main()
