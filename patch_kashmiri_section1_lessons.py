# -*- coding: utf-8 -*-
"""
Populate Kashmiri lessons 501–509 (section 1.1–1.9): 20 rows per English/Kashmiri table.

Each row must align: English = natural translation of the Kashmiri line (not a grammar
lecture with mismatched Kashmiri). Phrases from public phrasebooks and common learner
Roman (Omniglot Kashmiri phrases, Wikivoyage Kashmiri phrasebook; grammar-style lines
as in Spoken Kashmiri / O. N. Koul materials).

Run: py -3 patch_kashmiri_section1_lessons.py
"""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data_kashmiri.json"

# --- 1.1 (501): two tables × 20 — conversational phrases (Omniglot-style) ---

L501_VOWEL_EXAMPLES = [
    ["Welcome.", "वलिव", "Waliv"],
    ["Hello — Namaskār (Hindu greeting).", "नमस्कार", "Namaskār"],
    ["Peace be upon you — Assalām ‘alaikum.", "असलामु अलैकुम", "Assalām ‘alaikum"],
    ["Hello — Aadaab.", "आदाब", "Aadaab"],
    ["How are you?", "तोहय छिवा वारय?", "Tohy ch'ivaa vaarai?"],
    ["Fine, thank you — and you?", "वारय, शुकिया । त’ तीहय?", "Waaray, shukriyaa tiu tohy?"],
    ["It’s been a long time — we didn’t meet!", "वरिया काल गव न म्येलनसि!", "Variya kaal gov na myelnasi!"],
    ["What is your name?", "त्वहि क्या छु नाव?", "Twahi kyaa ch'u naav?"],
    ["My name is …", "मे छु नाव …", "Ma chho naw …"],
    ["Where are you from?", "त्वहि कतिक छु?", "Tvahi katika chu?"],
    ["Pleased to meet you.", "मे सप’ज़ खोशी त्वहि मीलिध ।", "Me sapiuz k'oshee twahu meelit'"],
    ["Good night.", "शबे खैर ।", "Shabey k'eūr"],
    ["Good luck! — Inshaallah (to Muslims).", "इंशाल्लाह", "Inshaallaah"],
    ["Good luck! — Vārakāra (to Hindus).", "वारकार", "Vārakāra"],
    ["Cheers! — Good health!", "ज़ुव थवुन ठीक", "Zuv thavun theek"],
    ["Have a safe journey (Muslims).", "नैर ख़ौदायस हवाल", "Nair khaudaayas havaal"],
    ["Have a safe journey (Hindus).", "नैर भगवानस हवाल", "Nair bhagavaanas havaal"],
    ["Do you understand?", "त्वहि छा फिकिरि तरान?", "Tvahi chaa phikiri taraan?"],
    ["I understand.", "आऊई समझ", "Aaooee samajh"],
    ["I don’t understand (said by a man).", "ब’ छुस न’ ज़ानान ।", "Biu ch'us niu zaanaan"],
]

L501_EXAMPLE_SENTENCES = [
    ["Yes.", "आ", "Aa"],
    ["No.", "ना", "Na"],
    ["Maybe.", "शायद", "Shayed"],
    ["I don’t know.", "मे छु ने पै", "Me chhu ne pai"],
    ["Please speak more slowly.", "तोहय हेकिवा वार’ वार’ वॅनिव ।", "Tohy hekivaa vaariu vaariu veuniv"],
    ["Please say that again.", "तोहय हेकिवा दुबार’ वॅनिथ ।", "Tohy hekivaa dubaariu veunit'"],
    ["Please write it down.", "यि लिखिव", "Yi Likhiv"],
    ["Do you speak English?", "तोहय छिवा अंगरीज़ी बोलान?", "Tohy chivā angrīzī bolān"],
    ["Do you speak Kashmiri?", "त्स्के छुके कॉशुर बोलान?", "Tske chhuke Koshur bolaan?"],
    ["Yes, a little.", "आ, थोडा स", "Aa, thoda sa"],
    ["How much is this?", "यि का’तिस छु?", "Yi keūtis ch'u"],
    ["Sorry.", "माफ कॅरिव ।", "Maap' keuriv"],
    ["Please.", "मेहरबॅानी ।", "Meharbeūnee"],
    ["Thank you.", "शुकिया", "Shukriya"],
    ["Don’t mention it (reply to thanks).", "कीहीन छु न परवाई", "Kiheen chhu ne parvaai"],
    ["Where is the toilet?", "टायलेट कति छि?", "Ṭaaylet kati ch'u!"],
    ["I miss you.", "मे छु च्योन याद यिवान", "Me chhu chyon yaad yiwaan"],
    ["I love you.", "त्स्के छुक म्योन जिगुर", "Tske chhuk myon jigur"],
    ["Get well soon.", "गचिव ठीक जल्द", "Gachiv theek jald"],
    ["Congratulations!", "पोश्ते मुबारक", "Poshte Mubarak"],
]

# --- 1.2 (502): spoken-style + textbook grammar lines; English = translation ---

L502_VOWEL_USE = [
    ["I am going to the market.", "ब चुस बाज़ार गतशान", "b chus ba:zar gatsha:n"],
    ["You are reading a book.", "त्स चुख किताब परान", "ts chukh kita:b para:n"],
    ["He is drinking tea.", "सु चु चाय चेवान", "su chu ca:y ceva:n"],
    ["He is a doctor.", "सु चु दक्तर", "su chu daktar"],
    ["She is tall.", "स च ज़ीत", "s cha zi:t"],
    ["I will eat food.", "बि खामि बाति", "bi kh'ami bati"],
    ["I will stay in Delhi.", "बि रोज़ि दिलि", "bi ro:zi dili"],
    ["I cannot go to Delhi.", "ब हेक न दिलि गतशिथ", "b hek n dili gətshith"],
    ["He can read this book.", "तिम हेकन यि किताब परिथ", "tim hekan yi kita:b pərith"],
    ["Welcome.", "वलिव", "Waliv"],
    ["How are you?", "तोहय छिवा वारय?", "Tohy ch'ivaa vaarai?"],
    ["What is your name?", "त्वहि क्या छु नाव?", "Twahi kyaa ch'u naav?"],
    ["Thank you.", "शुकिया", "Shukriya"],
    ["Please.", "मेहरबॅानी ।", "Meharbeūnee"],
    ["I understand.", "आऊई समझ", "Aaooee samajh"],
    ["Please speak more slowly.", "तोहय हेकिवा वार’ वार’ वॅनिव ।", "Tohy hekivaa vaariu vaariu veuniv"],
    ["Do you speak Kashmiri?", "त्स्के छुके कॉशुर बोलान?", "Tske chhuke Koshur bolaan?"],
    ["Where is the toilet?", "टायलेट कति छि?", "Ṭaaylet kati ch'u!"],
    ["Help!", "मदथ करिव!", "Madatha kariva!"],
    ["Stop!", "ठहर!", "Ṭeuhar!"],
]

L502_CONSONANT_USE = [
    ["Our hearts are like mirrors — as you see me, so I appear to you.", "दिल ब दिल गव आईनह, युथ वुछहम, त्यथ वुछय", "Dil ba dil gav aínah; yuth wuchham, tyuth wuchchay"],
    ["One language is never enough.", "अख़ ज़बान छु न ज़न्ह काफ़ी", "Akh zabaan chhu na zanh kaefi"],
    ["Goodbye — Khuda hāfiz.", "खुदा हाफिज़", "Khuda hāfiz"],
    ["Goodbye — Namaskār.", "नमस्कार", "Namaskār"],
    ["Goodbye — Alvidā.", "अलवीदा", "Alvidā"],
    ["Happy New Year / festive greeting.", "नवरेह मुबारक", "Navreh mubarak"],
    ["Happy birthday!", "त्स्के छुय वोहुरवोद मुबारक!", "Tske chhuy wohurwod mubarak!"],
    ["Excuse me — to get past someone.", "वथ त्रॅाविव ।", "Vat' treūviv"],
    ["Excuse me — to get attention.", "यपॅारय ।", "Yapeūry"],
    ["Would you like to dance with me?", "च्अ करख़ा डांस म्यांन साइथ?", "Chan khha dance minan sith?"],
    ["Do you come here often? (to a man)", "चे छुक यिवान योर वरिया?", "Che chhuk yiwan yor variya?"],
    ["Do you come here often? (to a woman)", "चे छिक यिवान योर वरिया?", "Che chhik yiwan yor variya?"],
    ["This gentleman will pay for everything.", "ये मर्द दी सॅर्सि हत्र पोंस", "Ye mard dee saersi hatra pons"],
    ["How do you say … in Kashmiri?", "… उस किथ पॅथ छे दपान कशिर मंज़?", "... us kith paeth chhe dapaan kashir manz?"],
    ["Speak to me in Kashmiri.", "चे कर मे साथ कशिर पॅथ कथ", "Che kar mae seath kashir peth kath"],
    ["Leave me alone!", "चे त्र मे कुनिज़ोन!", "Che tra mae kunizon!"],
    ["Go away!", "च़ल!", "Tsa!"],
    ["Call the police!", "बुलॅाविव पुलीस!", "Buleūviv pulees!"],
    ["Fire!", "नार!", "Naar!"],
    ["My hovercraft is full of eels.", "म्योन होवरक्राफ्ट छु ईलव सीथ भरिथ", "Myon hovercraaft chhu eelav seeth bharith"],
]

# --- 1.3 (503): same high-quality sentences; reading matras in running text ---

L503_MATRAS = [
    ["Welcome.", "वलिव", "Waliv"],
    ["Thank you.", "शुकिया", "Shukriya"],
    ["How are you?", "तोहय छिवा वारय?", "Tohy ch'ivaa vaarai?"],
    ["What is your name?", "त्वहि क्या छु नाव?", "Twahi kyaa ch'u naav?"],
    ["My name is …", "मे छु नाव …", "Ma chho naw …"],
    ["Where are you from?", "त्वहि कतिक छु?", "Tvahi katika chu?"],
    ["I understand.", "आऊई समझ", "Aaooee samajh"],
    ["I don’t understand (man).", "ब’ छुस न’ ज़ानान ।", "Biu ch'us niu zaanaan"],
    ["Please speak more slowly.", "तोहय हेकिवा वार’ वार’ वॅनिव ।", "Tohy hekivaa vaariu vaariu veuniv"],
    ["Do you speak English?", "तोहय छिवा अंगरीज़ी बोलान?", "Tohy chivā angrīzī bolān"],
    ["Do you speak Kashmiri?", "त्स्के छुके कॉशुर बोलान?", "Tske chhuke Koshur bolaan?"],
    ["How much is this?", "यि का’तिस छु?", "Yi keūtis ch'u"],
    ["Where is the toilet?", "टायलेट कति छि?", "Ṭaaylet kati ch'u!"],
    ["Sorry.", "माफ कॅरिव ।", "Maap' keuriv"],
    ["Please.", "मेहरबॅानी ।", "Meharbeūnee"],
    ["Good night.", "शबे खैर ।", "Shabey k'eūr"],
    ["I am going to the market.", "ब चुस बाज़ार गतशान", "b chus ba:zar gatsha:n"],
    ["He is a doctor.", "सु चु दक्तर", "su chu daktar"],
    ["I will eat food.", "बि खामि बाति", "bi kh'ami bati"],
    ["He can read this book.", "तिम हेकन यि किताब परिथ", "tim hekan yi kita:b pərith"],
]

# --- 1.4 (504): natural lines + a few short words for sound practice (English = gloss) ---

L504_PITFALLS = [
    ["Please speak more slowly.", "तोहय हेकिवा वार’ वार’ वॅनिव ।", "Tohy hekivaa vaariu vaariu veuniv"],
    ["I don’t understand (man).", "ब’ छुस न’ ज़ानान ।", "Biu ch'us niu zaanaan"],
    ["I don’t understand (woman).", "ब’ छस न’ ज़ानान ।", "Biu ch'as niu zaanaan"],
    ["Do you understand?", "त्वहि छा फिकिरि तरान?", "Tvahi chaa phikiri taraan?"],
    ["I understand.", "आऊई समझ", "Aaooee samajh"],
    ["How are you?", "तोहय छिवा वारय?", "Tohy ch'ivaa vaarai?"],
    ["What is your name?", "त्वहि क्या छु नाव?", "Twahi kyaa ch'u naav?"],
    ["Where are you from?", "त्वहि कतिक छु?", "Tvahi katika chu?"],
    ["Do you speak English?", "तोहय छिवा अंगरीज़ी बोलान?", "Tohy chivā angrīzī bolān"],
    ["Do you speak Kashmiri?", "त्स्के छुके कॉशुर बोलान?", "Tske chhuke Koshur bolaan?"],
    ["How much is this?", "यि का’तिस छु?", "Yi keūtis ch'u"],
    ["Where is the toilet?", "टायलेट कति छि?", "Ṭaaylet kati ch'u!"],
    ["Thank you.", "शुकिया", "Shukriya"],
    ["Please.", "मेहरबॅानी ।", "Meharbeūnee"],
    ["Sorry.", "माफ कॅरिव ।", "Maap' keuriv"],
    ["Welcome.", "वलिव", "Waliv"],
    ["Good night.", "शबे खैर ।", "Shabey k'eūr"],
    ["Help!", "मदथ करिव!", "Madatha kariva!"],
    ["Stop!", "ठहर!", "Ṭeuhar!"],
    ["Call the police!", "बुलॅाविव पुलीस!", "Buleūviv pulees!"],
]

# --- 1.5 (505): words with nasalisation / अं (Wikivoyage numbers + common words) ---

L505_ANUSVAR = [
    ["Five.", "पाँच", "pāñch"],
    ["Nine.", "नव", "nav"],
    ["Ten.", "दाह", "Dāh"],
    ["Country (Bharat).", "भारत", "bhārat"],
    ["Message.", "संदेश", "sandesh"],
    ["End / limit.", "अंत", "ant"],
    ["With / together.", "संग", "saṅg"],
    ["Body / limb.", "अंग", "anga"],
    ["Sanskrit (school subject).", "संस्कृत", "saṃskṛt"],
    ["Temple.", "मंदिर", "mandir"],
    ["Srinagar.", "श्रीनगर", "Shrīnagar"],
    ["White.", "सफ़ेद", "safed"],
    ["Fine / okay.", "ठीक", "ṭhīk"],
    ["Price.", "दाम", "dām"],
    ["Where? (in questions)", "कति", "kati"],
    ["Thank you.", "शुकिया", "Shukriya"],
    ["Hello — Namaskār.", "नमस्कार", "Namaskār"],
    ["Music.", "संगीत", "saṅgīt"],
    ["Culture.", "संस्कृति", "saṃskṛti"],
    ["Do you speak a language other than Kashmiri?", "तोहि छु दोयुम भाषा तगान?", "Tohi chhuv doyum bhasha tagaan?"],
]

# --- 1.6–1.9: English = translation of word or sentence; Devanagari shows target cluster ---

L506_CLUSTERS = [
    ["Language.", "भाषा", "bhāṣā"],
    ["Work / karma.", "कर्म", "karma"],
    ["Country / province.", "प्रदेश", "pradeś"],
    ["Thing / substance.", "वस्तु", "vastu"],
    ["Temple.", "मंदिर", "mandir"],
    ["Number.", "नंबर", "nambar"],
    ["Koshur (Kashmiri).", "कॉशुर", "Koshur"],
    ["Welcome.", "वलिव", "Waliv"],
    ["Thank you.", "शुकिया", "Shukriya"],
    ["How are you?", "तोहय छिवा वारय?", "Tohy ch'ivaa vaarai?"],
    ["I understand.", "आऊई समझ", "Aaooee samajh"],
    ["Please speak more slowly.", "तोहय हेकिवा वार’ वार’ वॅनिव ।", "Tohy hekivaa vaariu vaariu veuniv"],
    ["Do you speak Kashmiri?", "त्स्के छुके कॉशुर बोलान?", "Tske chhuke Koshur bolaan?"],
    ["Where is the toilet?", "टायलेट कति छि?", "Ṭaaylet kati ch'u!"],
    ["Help!", "मदथ करिव!", "Madatha kariva!"],
    ["Stop!", "ठहर!", "Ṭeuhar!"],
    ["Sorry.", "माफ कॅरिव ।", "Maap' keuriv"],
    ["Good night.", "शबे खैर ।", "Shabey k'eūr"],
    ["I am going to the market.", "ब चुस बाज़ार गतशान", "b chus ba:zar gatsha:n"],
    ["He is a doctor.", "सु चु दक्तर", "su chu daktar"],
]

L507_R_CLUSTERS = [
    ["Order / sequence.", "क्रम", "krama"],
    ["Love / affection.", "प्रेम", "prem"],
    ["Three.", "त्रि", "tri"],
    ["Village.", "ग्राम", "grām"],
    ["Substance / matter.", "द्रव्य", "dravya"],
    ["Daily.", "प्रतिदिन", "pratidin"],
    ["Art.", "आर्ट", "ārṭ"],
    ["Snake.", "सर्प", "sarpa"],
    ["All / entire.", "सर्व", "sarva"],
    ["Aryan / noble.", "आर्य", "ārya"],
    ["Srinagar.", "श्रीनगर", "Shrīnagar"],
    ["Welcome.", "वलिव", "Waliv"],
    ["Thank you.", "शुकिया", "Shukriya"],
    ["How are you?", "तोहय छिवा वारय?", "Tohy ch'ivaa vaarai?"],
    ["What is your name?", "त्वहि क्या छु नाव?", "Twahi kyaa ch'u naav?"],
    ["Do you speak Kashmiri?", "त्स्के छुके कॉशुर बोलान?", "Tske chhuke Koshur bolaan?"],
    ["Please speak more slowly.", "तोहय हेकिवा वार’ वार’ वॅनिव ।", "Tohy hekivaa vaariu vaariu veuniv"],
    ["I understand.", "आऊई समझ", "Aaooee samajh"],
    ["Good night.", "शबे खैर ।", "Shabey k'eūr"],
    ["Congratulations!", "पोश्ते मुबारक", "Poshte Mubarak"],
]

L508_H_CLUSTERS = [
    ["Thank you (lit. god-granted).", "धन्यवाद", "dhanyavād"],
    ["Rice / meal.", "भात", "bhāt"],
    ["House.", "घर", "ghar"],
    ["Flag.", "झंडा", "jhaṇḍā"],
    ["Student.", "छात्र", "chātra"],
    ["Tired.", "थक", "thak"],
    ["Phone.", "फ़ोन", "fon"],
    ["Sorry — forgive me.", "माफ कॅरिव ।", "Maap' keuriv"],
    ["Welcome.", "वलिव", "Waliv"],
    ["Thank you.", "शुकिया", "Shukriya"],
    ["Please.", "मेहरबॅानी ।", "Meharbeūnee"],
    ["Good night.", "शबे खैर ।", "Shabey k'eūr"],
    ["Help!", "मदथ करिव!", "Madatha kariva!"],
    ["Stop!", "ठहर!", "Ṭeuhar!"],
    ["Fire!", "नार!", "Naar!"],
    ["How are you?", "तोहय छिवा वारय?", "Tohy ch'ivaa vaarai?"],
    ["Where is the toilet?", "टायलेट कति छि?", "Ṭaaylet kati ch'u!"],
    ["I understand.", "आऊई समझ", "Aaooee samajh"],
    ["Do you speak English?", "तोहय छिवा अंगरीज़ी बोलान?", "Tohy chivā angrīzī bolān"],
    ["Get well soon.", "गचिव ठीक जल्द", "Gachiv theek jald"],
]

L509_SPECIAL = [
    ["Letter (of the alphabet).", "अक्षर", "akṣara"],
    ["Three.", "त्रि", "tri"],
    ["Knowledge.", "ज्ञान", "jñān"],
    ["Nation.", "राष्ट्र", "rāṣṭra"],
    ["Letter / note.", "पत्र", "patra"],
    ["Friend.", "मित्र", "mitra"],
    ["Learning / education.", "विद्या", "vidyā"],
    ["Worthy / able.", "योग्य", "yogya"],
    ["Education / teaching.", "शिक्षा", "śikṣā"],
    ["Forgiveness.", "क्षमा", "kṣamā"],
    ["Wise / learned.", "ज्ञानी", "jñānī"],
    ["Triangle.", "त्रिकोण", "trikoṇ"],
    ["Teacher.", "शिक्षक", "śikṣaka"],
    ["Welcome.", "वलिव", "Waliv"],
    ["Thank you.", "शुकिया", "Shukriya"],
    ["How are you?", "तोहय छिवा वारय?", "Tohy ch'ivaa vaarai?"],
    ["I understand.", "आऊई समझ", "Aaooee samajh"],
    ["Please speak more slowly.", "तोहय हेकिवा वार’ वार’ वॅनिव ।", "Tohy hekivaa vaariu vaariu veuniv"],
    ["Do you speak Kashmiri?", "त्स्के छुके कॉशुर बोलान?", "Tske chhuke Koshur bolaan?"],
    ["Good night.", "शबे खैर ।", "Shabey k'eūr"],
]

PATCH = {
    501: {
        "Vowel usage examples": L501_VOWEL_EXAMPLES,
        "Example sentences using the alphabet": L501_EXAMPLE_SENTENCES,
    },
    502: {
        "Sentence examples – vowels in use": L502_VOWEL_USE,
        "Consonant pronunciation notes": L502_CONSONANT_USE,
    },
    503: {
        "Words and sentences using vowel signs": L503_MATRAS,
    },
    504: {
        "Practice sentences": L504_PITFALLS,
    },
    505: {
        "Words and sentences with Anusvar": L505_ANUSVAR,
    },
    506: {
        "Sentences using consonant combinations": L506_CLUSTERS,
    },
    507: {
        "Sentences with र clusters": L507_R_CLUSTERS,
    },
    508: {
        "Sentences with ह and aspirates": L508_H_CLUSTERS,
    },
    509: {
        "Sentences with special conjuncts": L509_SPECIAL,
    },
}


def patch_block(block: dict, lesson_id: int) -> bool:
    heading = block.get("heading") or ""
    m = PATCH.get(lesson_id)
    if not m or heading not in m:
        return False
    rows = m[heading]
    if block.get("headers") != ["English", "Kashmiri", "Transliteration"]:
        return False
    block["rows"] = [list(r) for r in rows]
    return True


def patch_lesson(lesson: dict) -> None:
    lid = lesson.get("id")
    if lid not in PATCH:
        return
    for key in ("tables", "blocks"):
        arr = lesson.get(key)
        if not arr:
            continue
        for block in arr:
            if isinstance(block, dict):
                patch_block(block, lid)


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    data = deepcopy(data)
    for lesson in data:
        patch_lesson(lesson)
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Patched section 1 lessons 501–509 in", DATA)


if __name__ == "__main__":
    main()
