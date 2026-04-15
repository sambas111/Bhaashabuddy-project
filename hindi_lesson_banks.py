# -*- coding: utf-8 -*-
"""
Curated Hindi lesson rows: English | Devanagari | IAST-style romanization.
Pedagogy aligned with lesson titles (standard beginner Hindi; see e.g. UT Austin Hindi,
Preply Hindi grammar guides, Omniglot Devanagari). Each chapter returns 18 rows (15–20 range).
"""

from __future__ import annotations

N = 18  # target rows per lesson


def _rows(*triplets: tuple[str, str, str]) -> list[list[str]]:
    out = [[a, b, c] for (a, b, c) in triplets]
    assert 15 <= len(out) <= 22, len(out)
    return out


# --- Shared pools for conversation chapters (620–662) by keyword in title ---
def _pool_greetings() -> list[tuple[str, str, str]]:
    return [
        ("Hello", "नमस्ते", "namaste"),
        ("Good morning", "सुप्रभात", "suprabhāt"),
        ("Good evening", "शुभ संध्या", "śubha sandhyā"),
        ("How are you?", "आप कैसे हैं?", "āp kaise hain?"),
        ("I am fine, thank you", "मैं ठीक हूँ, धन्यवाद", "main ṭhīk hū̃, dhanyavād"),
        ("What is your name?", "आपका नाम क्या है?", "āpkā nām kyā hai?"),
        ("My name is Rahul", "मेरा नाम राहुल है", "merā nām rāhul hai"),
        ("Nice to meet you", "आप से मिलकर खुशी हुई", "āp se milkar khushī huī"),
        ("See you tomorrow", "कल मिलते हैं", "kal milte hain"),
        ("Welcome", "स्वागत है", "svāgat hai"),
        ("Please sit", "कृपया बैठिए", "kripayā baithiye"),
        ("Thank you very much", "बहुत धन्यवाद", "bahut dhanyavād"),
        ("Excuse me", "माफ़ कीजिए", "māf kījie"),
        ("Goodbye", "अलविदा", "alvidā"),
        ("Have a nice day", "आपका दिन शुभ हो", "āpkā din śubh ho"),
        ("I am glad to see you", "आपको देखकर खुशी हुई", "āpko dekhkar khushī huī"),
        ("Where are you from?", "आप कहाँ से हैं?", "āp kahā̃ se hain?"),
        ("I am from Delhi", "मैं दिल्ली से हूँ", "main dillī se hū̃"),
    ]


def _pool_hotel() -> list[tuple[str, str, str]]:
    return [
        ("I have a reservation", "मेरा आरक्षण है", "merā ārakṣaṇ hai"),
        ("A single room, please", "एक एकल कमरा, कृपया", "ek ekal kamrā, kripayā"),
        ("What is the room rate?", "कमरे का किराया क्या है?", "kamre kā kirāyā kyā hai?"),
        ("Is breakfast included?", "नाश्ता शामिल है?", "nāśtā śāmil hai?"),
        ("May I see the room?", "क्या मैं कमरा देख सकता हूँ?", "kyā main kamrā dekh saktā hū̃?"),
        ("The AC is not working", "एसी काम नहीं कर रहा", "īsī kām nahī̃ kar rahā"),
        ("Please send housekeeping", "कृपया हाउसकीपिंग भेजिए", "kripayā hāuskīpiṅg bhejie"),
        ("What time is checkout?", "चेकआउट का समय क्या है?", "chekā'uṭ kā samay kyā hai?"),
        ("I need an extra towel", "मुझे एक अतिरिक्त तौलिया चाहिए", "mujhe ek atirikt tauliyā cāhie"),
        ("Where is the lift?", "लिफ़्ट कहाँ है?", "lipṭ kahā̃ hai?"),
        ("Please call a taxi", "कृपया टैक्सी बुलाइए", "kripayā ṭaiksī bulāie"),
        ("The Wi‑Fi password?", "वाई‑फ़ाई पासवर्ड क्या है?", "vāī-fāī pāsavaṛ kyā hai?"),
        ("I would like to extend my stay", "मैं अपना ठहराव बढ़ाना चाहता हूँ", "main apnā ṭaharāv baṛhānā cāhatā hū̃"),
        ("Is there hot water?", "गर्म पानी है?", "garm pānī hai?"),
        ("The room key, please", "कमरे की चाबी, कृपया", "kamre kī cābī, kripayā"),
        ("This is too noisy", "यह बहुत शोर है", "yah bahut śor hai"),
        ("I am checking out now", "मैं अब चेकआउट कर रहा हूँ", "main ab chekā'uṭ kar rahā hū̃"),
        ("Please prepare the bill", "कृपया बिल तैयार करें", "kripayā bil taiyār karẽ"),
    ]


def _pool_doctor() -> list[tuple[str, str, str]]:
    return [
        ("I have a fever", "मुझे बुखार है", "mujhe bukhār hai"),
        ("My head hurts", "मेरे सिर में दर्द है", "mere sir mẽ dard hai"),
        ("Since when?", "कब से?", "kab se?"),
        ("Take this medicine twice a day", "यह दवा दिन में दो बार लें", "yah davā din mẽ do bār lẽ"),
        ("Drink plenty of water", "खूब पानी पिएँ", "khūb pānī piẽ"),
        ("I need a blood test", "मुझे रक्त जाँच चाहिए", "mujhe rakt jā̃c cāhie"),
        ("Do you have allergies?", "क्या आपको एलर्जी है?", "kyā āpko elarjī hai?"),
        ("Rest for two days", "दो दिन आराम करें", "do din ārām karẽ"),
        ("Follow‑up after a week", "एक सप्ताह बाद फिर आइए", "ek saptāh bād phir āie"),
        ("The pain is sharp", "दर्द तेज़ है", "dard tez hai"),
        ("I feel nauseous", "मुझे उल्टी जैसा लग रहा है", "mujhe ulṭī jaisā lag rahā hai"),
        ("Open your mouth", "मुँह खोलिए", "mũh kholie"),
        ("Blood pressure is normal", "ब्लड प्रेशर सामान्य है", "blaḍ preśar sāmānya hai"),
        ("Avoid oily food", "तला हुआ खाना कम खाएँ", "talā huā khānā kam khāẽ"),
        ("Take paracetamol if needed", "ज़रूरत हो तो पैरासिटामॉल लें", "zarūrat ho to pairāsiṭāmॉl lẽ"),
        ("I need a medical certificate", "मुझे मेडिकल सर्टिफिकेट चाहिए", "mujhe meḍikal sarṭiphikeṭ cāhie"),
        ("When should I come again?", "मुझे फिर कब आना चाहिए?", "mujhe phir kab ānā cāhie?"),
        ("Thank you, doctor", "धन्यवाद, डॉक्टर", "dhanyavād, ḍॉkṭar"),
    ]


def _pool_traffic() -> list[tuple[str, str, str]]:
    return [
        ("Please show your licence", "कृपया अपना लाइसेंस दिखाइए", "kripayā apnā laisens dikhāie"),
        ("You were speeding", "आपने ओवरस्पीड की", "āpne overspīḍ kī"),
        ("This is a one‑way road", "यह एकतरफ़ा सड़क है", "yah ekataraphā saṛak hai"),
        ("Wear your seat belt", "सीट बेल्ट लगाइए", "sīṭ belṭ lagāie"),
        ("Do not use mobile while driving", "गाड़ी चलाते समय मोबाइल न चलाएँ", "gāṛī calāte samay mobāil na calāẽ"),
        ("Your papers, please", "आपके कागज़ात, कृपया", "āp ke kāgazāt, kripayā"),
        ("Pay the fine here", "जुर्माना यहीं भरें", "jurmānā yahī̃ bharẽ"),
        ("I did not see the signal", "मुझे सिग्नल नहीं दिखा", "mujhe signl nahī̃ dikhā"),
        ("Park in the designated area", "निर्धारित स्थान पर पार्क करें", "nirdhārit sthān par pār̄k karẽ"),
        ("Helmet is mandatory", "हेलमेट अनिवार्य है", "helmeṭ anivārya hai"),
        ("Slow down near the school", "स्कूल के पास धीमे चलें", "skūl ke pās dhīme calẽ"),
        ("This is an emergency vehicle", "यह आपातकालीन वाहन है", "yah āpātkālīn vāhan hai"),
        ("Turn on the indicator", "इंडिकेटर जलाइए", "iṇḍikeṭar jalāie"),
        ("Do not drink and drive", "पीकर गाड़ी न चलाएँ", "pīkar gāṛī na calāẽ"),
        ("Your vehicle registration?", "आपके वाहन का पंजीकरण?", "āp ke vāhan kā pañjīkaraṇ?"),
        ("Follow traffic rules", "यातायात के नियम मानें", "yātāyāt ke niyam mānẽ"),
        ("I will be careful next time", "अगली बार सावधान रहूँगा", "aglī bār sāvdhān rahū̃gā"),
        ("Thank you, officer", "धन्यवाद, अधिकारी जी", "dhanyavād, adhikārī jī"),
    ]


def _pool_general() -> list[tuple[str, str, str]]:
    return [
        ("I understand", "मुझे समझ आ गया", "mujhe samajh ā gayā"),
        ("Please repeat", "कृपया दोहराइए", "kripayā dohrāie"),
        ("I do not know", "मुझे नहीं पता", "mujhe nahī̃ patā"),
        ("How much does it cost?", "यह कितने का है?", "yah kitne kā hai?"),
        ("Where is the station?", "स्टेशन कहाँ है?", "sṭeśan kahā̃ hai?"),
        ("I need help", "मुझे मदद चाहिए", "mujhe madad cāhie"),
        ("What time is it?", "क्या समय हुआ?", "kyā samay huā?"),
        ("I am learning Hindi", "मैं हिन्दी सीख रहा हूँ", "main hindī sīkh rahā hū̃"),
        ("Speak slowly, please", "धीरे बोलिए, कृपया", "dhīre bolie, kripayā"),
        ("I like this place", "मुझे यह जगह पसंद है", "mujhe yah jagah pasand hai"),
        ("It is very hot today", "आज बहुत गर्मी है", "āj bahut garmī hai"),
        ("Let us go", "चलिए", "calie"),
        ("Wait a moment", "एक मिनट रुकिए", "ek minaṭ rukie"),
        ("I agree", "मैं सहमत हूँ", "main sahamat hū̃"),
        ("That is correct", "यह सही है", "yah sahī hai"),
        ("I will try", "मैं कोशिश करूँगा", "main kośiś karū̃gā"),
        ("No problem", "कोई बात नहीं", "koī bāt nahī̃"),
        ("See you soon", "फिर मिलेंगे", "phir mileṅge"),
    ]


def _pick_conversation_rows(title: str) -> list[list[str]]:
    t = title.lower()
    pool: list[tuple[str, str, str]] = []
    if any(x in t for x in ("hotel", "room", "checkout")):
        pool = _pool_hotel()
    elif any(x in t for x in ("doctor", "patient", "medical")):
        pool = _pool_doctor()
    elif any(x in t for x in ("traffic", "police", "fine", "licence")):
        pool = _pool_traffic()
    elif any(
        x in t
        for x in (
            "introduction",
            "salutation",
            "greeting",
            "diwali",
            "festival",
            "republic",
            "women",
        )
    ):
        pool = _pool_greetings()
    else:
        pool = _pool_greetings()[:12] + _pool_general()[:6]
    return _rows(*pool[:N])


# --- Per-chapter exact banks (501–619): grammar + script + phrases + vocab ---
EXACT: dict[int, list[list[str]]] = {}


def _register(cid: int, triplets: tuple[tuple[str, str, str], ...]) -> None:
    EXACT[cid] = _rows(*triplets)


# 501 Hindi script – alphabets
_register(
    501,
    (
        ("Vowel अ (short a)", "अ", "a"),
        ("Vowel आ (long ā)", "आ", "ā"),
        ("Vowel इ (i)", "इ", "i"),
        ("Vowel ई (ī)", "ई", "ī"),
        ("Vowel उ (u)", "उ", "u"),
        ("Vowel ऊ (ū)", "ऊ", "ū"),
        ("Vowel ए (e)", "ए", "e"),
        ("Vowel ऐ (ai)", "ऐ", "ai"),
        ("Vowel ओ (o)", "ओ", "o"),
        ("Vowel औ (au)", "औ", "au"),
        ("Consonant क (ka)", "क", "ka"),
        ("Consonant च (ca)", "च", "ca"),
        ("Consonant त (ta)", "त", "ta"),
        ("Consonant प (pa)", "प", "pa"),
        ("Consonant र (ra)", "र", "ra"),
        ("Consonant ल (la)", "ल", "la"),
        ("Consonant स (sa)", "स", "sa"),
        ("Consonant ह (ha)", "ह", "ha"),
    ),
)

# 502 vowels & consonants – pronunciation in context
_register(
    502,
    (
        ("Water", "पानी", "pānī"),
        ("Milk", "दूध", "dūdh"),
        ("Fire", "आग", "āg"),
        ("Sun", "सूरज", "sūraj"),
        ("Moon", "चाँद", "cā̃d"),
        ("Star", "तारा", "tārā"),
        ("House", "घर", "ghar"),
        ("Book", "किताब", "kitāb"),
        ("School", "स्कूल", "skūl"),
        ("Friend", "दोस्त", "dost"),
        ("Mother", "माँ", "mā̃"),
        ("Father", "पिता", "pitā"),
        ("Brother", "भाई", "bhāī"),
        ("Sister", "बहन", "behan"),
        ("Good", "अच्छा", "acchā"),
        ("Bad", "बुरा", "burā"),
        ("Big", "बड़ा", "baṛā"),
        ("Small", "छोटा", "choṭā"),
    ),
)

# 503 Barakhadi (sample consonant + vowel marks)
_register(
    503,
    (
        ("ka + ā = kā", "का", "kā"),
        ("ka + i = ki", "कि", "ki"),
        ("ka + ī = kī", "की", "kī"),
        ("ka + u = ku", "कु", "ku"),
        ("ka + ū = kū", "कू", "kū"),
        ("ka + e = ke", "के", "ke"),
        ("ka + ai = kai", "कै", "kai"),
        ("ka + o = ko", "को", "ko"),
        ("ka + au = kau", "कौ", "kau"),
        ("ga + ā = gā", "गा", "gā"),
        ("ga + i = gi", "गि", "gi"),
        ("ca + ā = cā", "चा", "cā"),
        ("ca + u = cu", "चु", "cu"),
        ("ta + ā = tā", "ता", "tā"),
        ("ta + i = ti", "ति", "ti"),
        ("pa + ā = pā", "पा", "pā"),
        ("na + ā = nā", "ना", "nā"),
        ("ma + ā = mā", "मा", "mā"),
    ),
)

# 504 pronunciation problems (retroflex vs dental)
_register(
    504,
    (
        ("Ta (dental त)", "त", "ta"),
        ("Ṭa (retroflex ट)", "ट", "ṭa"),
        ("Tha (थ)", "थ", "tha"),
        ("Ṭha (ठ)", "ठ", "ṭha"),
        ("Da (द)", "द", "da"),
        ("Ḍa (ड)", "ड", "ḍa"),
        ("Dha (ध)", "ध", "dha"),
        ("Ḍha (ढ)", "ढ", "ḍha"),
        ("Example: four (char)", "चार", "cār"),
        ("Example: four (ṭār colloquial avoided)", "चार", "cār"),
        ("Rice (cāwal)", "चावल", "cāwal"),
        ("Branch (ḍāl)", "डाल", "ḍāl"),
        ("Practice: त vs ट", "तल / टल", "tala / ṭala"),
        ("Practice: द vs ड", "दिन / डिब्बा", "din / ḍibbā"),
        ("Nasal anusvara before क", "अंक", "aṅk"),
        ("Half न in हिन्दी", "हिन्दी", "hindī"),
        ("Listen and repeat slowly", "धीरे धीरे दोहराइए", "dhīre dhīre dohrāie"),
        ("Minimal pair practice helps", "न्यूनतम जोड़े अभ्यास करें", "nyūnatam joḍe abhyās karẽ"),
    ),
)

# 505 Anusvara
_register(
    505,
    (
        ("King", "राजा", "rājā"),
        ("Path", "पंथ", "panth"),
        ("Moment", "क्षण", "kṣaṇ"),
        ("Ganges (Gangā)", "गंगा", "gaṅgā"),
        ("Lamp", "दीपक", "dīpak"),
        ("Temple", "मंदिर", "mandir"),
        ("Example: aṅ + k", "अंक", "aṅk"),
        ("Example: gaṅ + gā", "गंगा", "gaṅgā"),
        ("Hindi grammar book", "हिन्दी व्याकरण की पुस्तक", "hindī vyākaraṇ kī pustak"),
        ("Practice: aṃ in mantra", "ॐ", "oṃ"),
        ("Nasal before च", "अंचल", "aṅcal"),
        ("Sound like 'n' before velars", "कंठ", "kaṇṭha"),
        ("Pronounce clearly", "स्पष्ट उच्चारण करें", "spaṣṭ uccāraṇ karẽ"),
        ("Listen to native audio", "मूल वक्ता सुनें", "mūl vaktā suṇẽ"),
        ("Compare: अ / अं", "अग्नि / अंक", "agni / aṅk"),
        ("Common word: Hindi", "हिन्दी", "hindī"),
        ("Common word: thanks", "धन्यवाद", "dhanyavād"),
        ("Repeat after the speaker", "वक्ता के पीछे दोहराएँ", "vaktā ke pīche dohrāẽ"),
    ),
)

# 506–508 conjuncts (samples)
_register(
    506,
    (
        ("School", "स्कूल", "skūl"),
        ("Student", "विद्यार्थी", "vidyārthī"),
        ("Question", "प्रश्न", "praśn"),
        ("Answer", "उत्तर", "uttar"),
        ("Practice", "अभ्यास", "abhyās"),
        ("Writing", "लेखन", "lekhan"),
        ("Reading", "पठन", "paṭhan"),
        ("Teacher", "शिक्षक", "śikṣak"),
        ("Book", "पुस्तक", "pustak"),
        ("Notebook", "कॉपी", "kॉpī"),
        ("Pen", "कलम", "kalam"),
        ("Blackboard", "श्यामपट", "śyāmapaṭ"),
        ("Homework", "गृहकार्य", "gṛhakārya"),
        ("Examination", "परीक्षा", "parīkṣā"),
        ("Result", "परिणाम", "pariṇām"),
        ("Classroom", "कक्षा", "kakṣā"),
        ("Library", "पुस्तकालय", "pustakālaya"),
        ("University", "विश्वविद्यालय", "viśvavidyālaya"),
    ),
)

_register(
    507,
    (
        ("Road", "सड़क", "saṛak"),
        ("Train", "रेल", "rel"),
        ("Railway station", "रेलवे स्टेशन", "relve sṭeśan"),
        ("Ticket", "टिकट", "tikaṭ"),
        ("Platform", "प्लेटफ़ॉर्म", "pleṭphॉrm"),
        ("Car", "कार", "kār"),
        ("Bus", "बस", "bas"),
        ("Bicycle", "साइकिल", "sāikil"),
        ("River", "नदी", "nadī"),
        ("Bridge", "पुल", "pul"),
        ("Tree", "पेड़", "peṛ"),
        ("Leaf", "पत्ता", "pattā"),
        ("Flower", "फूल", "phūl"),
        ("Garden", "बगीचा", "bagīcā"),
        ("Market", "बाज़ार", "bāzār"),
        ("Shop", "दुकान", "dukān"),
        ("Money", "पैसा", "paisā"),
        ("Price", "कीमत", "kīmat"),
    ),
)

_register(
    508,
    (
        ("Hand", "हाथ", "hāth"),
        ("Finger", "ऊँगली", "ū̃galī"),
        ("Heart", "हृदय", "hṛdaya"),
        ("Happiness", "खुशी", "khushī"),
        ("Horse", "घोड़ा", "ghoṛā"),
        ("Ghost (story)", "भूत", "bhūt"),
        ("Yesterday", "कल", "kal"),
        ("Today", "आज", "āj"),
        ("Tomorrow", "कल", "kal"),
        ("Night", "रात", "rāt"),
        ("Morning", "सुबह", "subah"),
        ("Evening", "शाम", "śām"),
        ("Hour", "घंटा", "ghaṇṭā"),
        ("Minute", "मिनट", "minaṭ"),
        ("Week", "सप्ताह", "saptāh"),
        ("Month", "महीना", "mahīnā"),
        ("Year", "साल", "sāl"),
        ("Birthday", "जन्मदिन", "janmadin"),
    ),
)

_register(
    509,
    (
        ("Self", "स्वयं", "svayaṃ"),
        ("Own", "अपना", "apanā"),
        ("Rule", "नियम", "niyam"),
        ("Exception", "अपवाद", "apavād"),
        ("Special case", "विशेष स्थिति", "viśeṣ sthiti"),
        ("Learn conjuncts gradually", "संयुक्ताक्षर क्रमिक सीखें", "saṃyuktākṣara kramik sīkhẽ"),
        ("Write each word thrice", "प्रत्येक शब्द तीन बार लिखें", "pratyek śabd tīn bār likhẽ"),
        ("Read aloud daily", "प्रतिदिन ज़ोर से पढ़ें", "pratidin zor se paṛhẽ"),
        ("Hindi spelling", "हिन्दी वर्तनी", "hindī vartanī"),
        ("Dictionary use", "शब्दकोश का उपयोग", "śabdakoś kā upayog"),
        ("Practice sheet", "अभ्यास पत्र", "abhyās patra"),
        ("Teacher's example", "शिक्षक का उदाहरण", "śikṣak kā udāharaṇ"),
        ("Student copy", "छात्र प्रतिलिपि", "chātra pratilipi"),
        ("Correct mistakes", "गलतियाँ सुधारें", "galatiyā̃ sudhārẽ"),
        ("Listen carefully", "ध्यान से सुनें", "dhyān se suṇẽ"),
        ("Repeat difficult clusters", "कठिन समूह दोहराएँ", "kaṭhin samūh dohrāẽ"),
        ("Progress slowly", "धीरे धीरे प्रगति", "dhīre dhīre pragati"),
        ("Keep practicing", "अभ्यास जारी रखें", "abhyās jārī rakhẽ"),
    ),
)

# 510 Pronouns – standard Hindi
_register(
    510,
    (
        ("I", "मैं", "main"),
        ("We", "हम", "ham"),
        ("You (informal)", "तुम", "tum"),
        ("You (formal)", "आप", "āp"),
        ("He", "वह", "vah"),
        ("She", "वह", "vah"),
        ("They", "वे", "ve"),
        ("This (m.)", "यह", "yah"),
        ("That (m.)", "वह", "vah"),
        ("My name is…", "मेरा नाम … है", "merā nām … hai"),
        ("What is your name?", "आपका नाम क्या है?", "āpkā nām kyā hai?"),
        ("I am a student", "मैं विद्यार्थी हूँ", "main vidyārthī hū̃"),
        ("You are a teacher", "आप शिक्षक हैं", "āp śikṣak haiṃ"),
        ("This is my book", "यह मेरी किताब है", "yah merī kitāb hai"),
        ("That is my friend", "वह मेरा दोस्त है", "vah merā dost hai"),
        ("We are ready", "हम तैयार हैं", "ham taiyār haiṃ"),
        ("They are coming", "वे आ रहे हैं", "ve ā rahe haiṃ"),
        ("It is mine", "यह मेरा है", "yah merā hai"),
    ),
)

# 511 plural respect
_register(
    511,
    (
        ("You (respectful plural form)", "आप लोग", "āp log"),
        ("Please come in", "कृपया अंदर आइए", "kripayā andar āie"),
        ("Please sit", "कृपया बैठिए", "kripayā baithiye"),
        ("How are you all?", "आप सब कैसे हैं?", "āp sab kaise haiṃ?"),
        ("Thank you, elders", "धन्यवाद, बड़ों को", "dhanyavād, baṛõ ko"),
        ("We respect you", "हम आपका सम्मान करते हैं", "ham āpkā sammān karte haiṃ"),
        ("They are honorable guests", "वे माननीय अतिथि हैं", "ve mānānīya atithi haiṃ"),
        ("Please have tea", "कृपया चाय लीजिए", "kripayā cāy lījie"),
        ("With your permission", "आपकी अनुमति से", "āpkī anumati se"),
        ("Your health matters", "आपका स्वास्थ्य महत्वपूर्ण है", "āpkā svāsthya mahatvpūrṇ hai"),
        ("We wish you well", "हम आपकी भलाई चाहते हैं", "ham āpkī bhalāī cāhte haiṃ"),
        ("Please take rest", "कृपया आराम कीजिए", "kripayā ārām kījie"),
        ("May I help you?", "क्या मैं आपकी मदद कर सकता हूँ?", "kyā main āpkī madad kar saktā hū̃?"),
        ("Your children are bright", "आपके बच्चे होशियार हैं", "āp ke bacche hośiyār haiṃ"),
        ("We are grateful", "हम आभारी हैं", "ham ābhārī haiṃ"),
        ("Kindly forgive me", "कृपया मुझे क्षमा करें", "kripayā mujhe kṣamā karẽ"),
        ("Your order, please", "आपका आदेश, कृपया", "āpkā ādeś, kripayā"),
        ("Good evening, everyone", "शुभ संध्या, सभी को", "śubha sandhyā, sabhī ko"),
    ),
)

# 512 Verbs (infinitive / root forms)
_register(
    512,
    (
        ("to go", "जाना", "jānā"),
        ("to come", "आना", "ānā"),
        ("to eat", "खाना", "khānā"),
        ("to drink", "पीना", "pīnā"),
        ("to read", "पढ़ना", "paṛhnā"),
        ("to write", "लिखना", "likhnā"),
        ("to speak", "बोलना", "bolnā"),
        ("to listen", "सुनना", "sunnā"),
        ("to see", "देखना", "dekhnā"),
        ("to sleep", "सोना", "sonā"),
        ("to sit", "बैठना", "baiṭhnā"),
        ("to stand", "खड़े होना", "khaṛe honā"),
        ("to give", "देना", "denā"),
        ("to take", "लेना", "lenā"),
        ("to buy", "खरीदना", "kharīdnā"),
        ("to sell", "बेचना", "becnā"),
        ("to learn", "सीखना", "sīkhnā"),
        ("to teach", "सिखाना", "sikhānā"),
    ),
)


def _fallback_practice() -> list[tuple[str, str, str]]:
    return _pool_general()


def rows_by_title(cid: int, title: str) -> list[list[str]]:
    """18 Hindi rows matched to lesson title (keywords). Used when cid not in EXACT."""
    t = title.lower()

    if cid >= 620:
        return _pick_conversation_rows(title)

    # --- Grammar & phrases (513–596): match more specific phrases first ---
    if "simple present tense of" in t and "to be" in t:
        return _rows(
            ("I am here", "मैं यहाँ हूँ", "main yahā̃ hū̃"),
            ("You are kind", "आप दयालु हैं", "āp dayālu haiṃ"),
            ("He is tall", "वह लंबा है", "vah laṃbā hai"),
            ("She is wise", "वह बुद्धिमान है", "vah buddhimān hai"),
            ("We are friends", "हम दोस्त हैं", "ham dost haiṃ"),
            ("They are late", "वे देर से हैं", "ve der se haiṃ"),
            ("It is cold", "ठंड है", "thaṃḍ hai"),
            ("This is easy", "यह आसान है", "yah āsān hai"),
            ("That is true", "वह सच है", "vah sac hai"),
            ("I am not ready", "मैं तैयार नहीं हूँ", "main taiyār nahī̃ hū̃"),
            ("Are you sure?", "क्या आप निश्चित हैं?", "kyā āp niścit haiṃ?"),
            ("We are Indians", "हम भारतीय हैं", "ham bhāratīy haiṃ"),
            ("It is possible", "यह संभव है", "yah saṃbhav hai"),
            ("Time is short", "समय कम है", "samay kam hai"),
            ("This is important", "यह महत्वपूर्ण है", "yah mahatvpūrṇ hai"),
            ("I am happy", "मैं खुश हूँ", "main khush hū̃"),
            ("You are welcome", "आपका स्वागत है", "āpkā svāgat hai"),
            ("It is raining", "बारिश हो रही है", "bāriś ho rahī hai"),
        )

    if "present continuous" in t:
        return _rows(
            ("I am reading", "मैं पढ़ रहा हूँ", "main paṛh rahā hū̃"),
            ("She is singing", "वह गा रही है", "vah gā rahī hai"),
            ("They are playing", "वे खेल रहे हैं", "ve khel rahe haiṃ"),
            ("We are eating", "हम खा रहे हैं", "ham khā rahe haiṃ"),
            ("He is driving", "वह गाड़ी चला रहा है", "vah gāṛī calā rahā hai"),
            ("It is working", "यह काम कर रहा है", "yah kām kar rahā hai"),
            ("I am learning Hindi", "मैं हिन्दी सीख रहा हूँ", "main hindī sīkh rahā hū̃"),
            ("Are you coming?", "क्या आप आ रहे हैं?", "kyā āp ā rahe haiṃ?"),
            ("I am not going", "मैं नहीं जा रहा", "main nahī̃ jā rahā"),
            ("Who is calling?", "कौन फोन कर रहा है?", "kaun phon kar rahā hai?"),
            ("The train is arriving", "ट्रेन आ रही है", "ṭren ā rahī hai"),
            ("We are waiting", "हम इंतज़ार कर रहे हैं", "ham intazār kar rahe haiṃ"),
            ("It is getting dark", "अँधेरा हो रहा है", "ãdherā ho rahā hai"),
            ("Children are studying", "बच्चे पढ़ रहे हैं", "bacce paṛh rahe haiṃ"),
            ("I am writing a letter", "मैं पत्र लिख रहा हूँ", "main patr likh rahā hū̃"),
            ("She is cooking", "वह खाना बना रही है", "vah khānā banā rahī hai"),
            ("They are talking", "वे बात कर रहे हैं", "ve bāt kar rahe haiṃ"),
            ("Rain is falling", "बारिश हो रही है", "bāriś ho rahī hai"),
        )

    if "simple present tense" in t and "to be" not in t:
        return _rows(
            ("I go to school", "मैं स्कूल जाता हूँ", "main skūl jātā hū̃"),
            ("We speak Hindi", "हम हिन्दी बोलते हैं", "ham hindī bolte haiṃ"),
            ("She reads the news", "वह समाचार पढ़ती है", "vah samācār paṛhtī hai"),
            ("They live in Delhi", "वे दिल्ली में रहते हैं", "ve dillī mẽ rahte haiṃ"),
            ("He plays cricket", "वह क्रिकेट खेलता है", "vah krikeṭ kheltā hai"),
            ("I drink tea", "मैं चाय पीता हूँ", "main cāy pītā hū̃"),
            ("You work hard", "आप मेहनत करते हैं", "āp mehnat karte haiṃ"),
            ("Birds fly", "पक्षी उड़ते हैं", "pakṣī uṛte haiṃ"),
            ("Sun rises in the east", "सूर्य पूरब में उगता है", "sūrya pūrab mẽ ugtā hai"),
            ("I know this", "मैं यह जानता हूँ", "main yah jāntā hū̃"),
            ("We help others", "हम दूसरों की मदद करते हैं", "ham dūsrõ kī madad karte haiṃ"),
            ("She teaches Hindi", "वह हिन्दी पढ़ाती है", "vah hindī paṛhātī hai"),
            ("Children play", "बच्चे खेलते हैं", "bacce khelte haiṃ"),
            ("I like music", "मुझे संगीत पसंद है", "mujhe saṅgīt pasand hai"),
            ("He drives a car", "वह कार चलाता है", "vah kār calātā hai"),
            ("We eat at home", "हम घर पर खाते हैं", "ham ghar par khāte haiṃ"),
            ("It happens daily", "यह रोज़ होता है", "yah roz hotā hai"),
            ("They understand", "वे समझते हैं", "ve samajhte haiṃ"),
        )

    if "future continuous" in t:
        return _rows(
            ("I will be studying", "मैं पढ़ रहा होऊँगा", "main paṛh rahā hoū̃gā"),
            ("She will be working", "वह काम कर रही होगी", "vah kām kar rahī hogī"),
            ("We will be traveling", "हम यात्रा कर रहे होंगे", "ham yātrā kar rahe hoṅge"),
            ("They will be waiting", "वे इंतज़ार कर रहे होंगे", "ve intazār kar rahe hoṅge"),
            ("It will be raining", "बारिश हो रही होगी", "bāriś ho rahī hogī"),
            ("I will not be late", "मैं देर से नहीं होऊँगा", "main der se nahī̃ hoū̃gā"),
            ("He will be reading", "वह पढ़ रहा होगा", "vah paṛh rahā hogā"),
            ("We will be eating", "हम खा रहे होंगे", "ham khā rahe hoṅge"),
            ("Who will be speaking?", "कौन बोल रहा होगा?", "kaun bol rahā hogā?"),
            ("Tomorrow I will be free", "कल मैं फुरसत में होऊँगा", "kal main fursat mẽ hoū̃gā"),
            ("By then I will be ready", "तब तक मैं तैयार होऊँगा", "tab tak main taiyār hoū̃gā"),
            ("She will be singing", "वह गा रही होगी", "vah gā rahī hogī"),
            ("Kids will be sleeping", "बच्चे सो रहे होंगे", "bacce so rahe hoṅge"),
            ("Train will be leaving", "ट्रेन चल रही होगी", "ṭren cal rahī hogī"),
            ("I will be calling you", "मैं आपको फोन कर रहा होऊँगा", "main āpko phon kar rahā hoū̃gā"),
            ("We will be watching", "हम देख रहे होंगे", "ham dekh rahe hoṅge"),
            ("He will be fixing it", "वह ठीक कर रहा होगा", "vah ṭhīk kar rahā hogā"),
            ("They will be helping", "वे मदद कर रहे होंगे", "ve madad kar rahe hoṅge"),
        )

    if "simple future tense" in t:
        return _rows(
            ("I will go", "मैं जाऊँगा", "main jāū̃gā"),
            ("We will come", "हम आएँगे", "ham āeṅge"),
            ("She will call", "वह फोन करेगी", "vah phon karegī"),
            ("They will return", "वे लौटेंगे", "ve lauṭeṅge"),
            ("It will rain", "बारिश होगी", "bāriś hogī"),
            ("I will study", "मैं पढ़ूँगा", "main paṛhū̃gā"),
            ("You will succeed", "आप सफल होंगे", "āp saphal hoṅge"),
            ("He will pay", "वह भुगतान करेगा", "vah bhugtān karegā"),
            ("We will meet tomorrow", "हम कल मिलेंगे", "ham kal mileṅge"),
            ("I will not leave", "मैं नहीं जाऊँगा", "main nahī̃ jāū̃gā"),
            ("Will you help?", "क्या आप मदद करेंगे?", "kyā āp madad kareṅge?"),
            ("Sun will rise", "सूरज उगेगा", "sūraj ugegā"),
            ("She will sing", "वह गाएगी", "vah gāegī"),
            ("We will win", "हम जीतेंगे", "ham jīteṅge"),
            ("He will arrive soon", "वह जल्द आएगा", "vah jald āegā"),
            ("I will write", "मैं लिखूँगा", "main likhū̃gā"),
            ("They will agree", "वे सहमत होंगे", "ve sahamat hoṅge"),
            ("It will be fine", "सब ठीक होगा", "sab ṭhīk hogā"),
        )

    if "simple past" in t and "part 1" in t:
        return _rows(
            ("I went yesterday", "मैं कल गया", "main kal gayā"),
            ("We ate food", "हमने खाना खाया", "hamne khānā khāyā"),
            ("She came late", "वह देर से आई", "vah der se āī"),
            ("They slept early", "वे जल्दी सो गए", "ve jaldī so ga.e"),
            ("He read a book", "उसने किताब पढ़ी", "usne kitāb paṛhī"),
            ("I did not go", "मैं नहीं गया", "main nahī̃ gayā"),
            ("We saw the film", "हमने फ़िल्म देखी", "hamne film dekhī"),
            ("It rained", "बारिश हुई", "bāriś huī"),
            ("You spoke well", "आपने अच्छा बोला", "āpne acchā bolā"),
            ("I woke up early", "मैं जल्दी उठा", "main jaldī uṭhā"),
            ("They left", "वे चले गए", "ve cale ga.e"),
            ("He bought milk", "उसने दूध खरीदा", "usne dūdh kharīdā"),
            ("We met at six", "हम छह बजे मिले", "ham chah baje mile"),
            ("She smiled", "वह मुस्कुराई", "vah muskurāī"),
            ("I forgot", "मैं भूल गया", "main bhūl gayā"),
            ("Birds flew away", "पक्षी उड़ गए", "pakṣī uṛ ga.e"),
            ("He opened the door", "उसने दरवाज़ा खोला", "usne darvāzā kholā"),
            ("We finished work", "हमने काम खत्म किया", "hamne kām khatm kiyā"),
        )

    if "simple past" in t and "part 2" in t:
        return _rows(
            ("I saw him", "मैंने उसे देखा", "mainne use dekhā"),
            ("She wrote a letter", "उसने पत्र लिखा", "usne patr likhā"),
            ("We bought vegetables", "हमने सब्ज़ी खरीदी", "hamne sabzī kharīdī"),
            ("He opened the shop", "उसने दुकान खोली", "usne dukān kholī"),
            ("They built a house", "उन्होंने घर बनाया", "unhoṃne ghar banāyā"),
            ("I read the paper", "मैंने अख़बार पढ़ा", "mainne akhbār paṛhā"),
            ("She cooked food", "उसने खाना बनाया", "usne khānā banāyā"),
            ("We watched TV", "हमने टीवी देखा", "hamne ṭīvī dekhā"),
            ("He paid the bill", "उसने बिल भरा", "usne bil bharā"),
            ("I did not see", "मैंने नहीं देखा", "mainne nahī̃ dekhā"),
            ("They helped us", "उन्होंने हमारी मदद की", "unhoṃne hamārī madad kī"),
            ("She closed the window", "उसने खिड़की बंद की", "usne khiṛkī band kī"),
            ("We chose a seat", "हमने सीट चुनी", "hamne sīṭ cunī"),
            ("He answered correctly", "उसने सही जवाब दिया", "usne sahī javāb diyā"),
            ("I sent an email", "मैंने ईमेल भेजा", "mainne īmel bhejā"),
            ("She painted the wall", "उसने दीवार रंग की", "usne dīvār raṅg kī"),
            ("We ordered tea", "हमने चाय मँगवाई", "hamne cāy maṅgvāī"),
            ("He fixed the tyre", "उसने टायर ठीक किया", "usne ṭāyar ṭhīk kiyā"),
        )

    if "simple past" in t and "to be" in t:
        return _rows(
            ("I was tired", "मैं थका हुआ था", "main thakā huā thā"),
            ("You were right", "आप सही थे", "āp sahī the"),
            ("He was ill", "वह बीमार था", "vah bīmār thā"),
            ("She was happy", "वह खुश थी", "vah khush thī"),
            ("We were students", "हम छात्र थे", "ham chātra the"),
            ("They were late", "वे देर से थे", "ve der se the"),
            ("It was cold", "ठंड थी", "thaṃḍ thī"),
            ("There was a problem", "एक समस्या थी", "ek samasyā thī"),
            ("I was not ready", "मैं तैयार नहीं था", "main taiyār nahī̃ thā"),
            ("Were you there?", "क्या आप वहाँ थे?", "kyā āp vahā̃ the?"),
            ("The keys were lost", "चाबियाँ खो गई थीं", "cābiyā̃ kho ga.ī thī̃"),
            ("We were friends", "हम दोस्त थे", "ham dost the"),
            ("He was absent", "वह अनुपस्थित था", "vah anupasthit thā"),
            ("It was raining", "बारिश हो रही थी", "bāriś ho rahī thī"),
            ("I was at home", "मैं घर पर था", "main ghar par thā"),
            ("She was busy", "वह व्यस्त थी", "vah vyast thī"),
            ("They were angry", "वे नाराज़ थे", "ve nārāz the"),
            ("Time was short", "समय कम था", "samay kam thā"),
        )

    if "past continuous" in t:
        return _rows(
            ("I was reading", "मैं पढ़ रहा था", "main paṛh rahā thā"),
            ("She was cooking", "वह खाना बना रही थी", "vah khānā banā rahī thī"),
            ("They were playing", "वे खेल रहे थे", "ve khel rahe the"),
            ("It was snowing", "बर्फ़बारी हो रही थी", "barfabārī ho rahī thī"),
            ("We were waiting", "हम इंतज़ार कर रहे थे", "ham intazār kar rahe the"),
            ("He was driving fast", "वह तेज़ गाड़ी चला रहा था", "vah tez gāṛī calā rahā thā"),
            ("I was not listening", "मैं सुन नहीं रहा था", "main sun nahī̃ rahā thā"),
            ("Birds were singing", "पक्षी गा रहे थे", "pakṣī gā rahe the"),
            ("Children were crying", "बच्चे रो रहे थे", "bacce ro rahe the"),
            ("Phone was ringing", "फोन बज रहा था", "phon baj rahā thā"),
            ("Sun was setting", "सूरज डूब रहा था", "sūraj ḍūb rahā thā"),
            ("She was writing", "वह लिख रही थी", "vah likh rahī thī"),
            ("We were talking", "हम बात कर रहे थे", "ham bāt kar rahe the"),
            ("Train was leaving", "ट्रेन चल रही थी", "ṭren cal rahī thī"),
            ("He was sleeping", "वह सो रहा था", "vah so rahā thā"),
            ("I was thinking", "मैं सोच रहा था", "main soc rahā thā"),
            ("They were building", "वे बना रहे थे", "ve banā rahe the"),
            ("Rain was stopping", "बारिश रुक रही थी", "bāriś ruk rahī thī"),
        )

    if "perfect tense" in t or "present/past/future perfect" in t:
        return _rows(
            ("I have eaten", "मैं खा चुका हूँ", "main khā cukā hū̃"),
            ("She has left", "वह जा चुकी है", "vah jā cukī hai"),
            ("We have finished", "हम खत्म कर चुके हैं", "ham khatm kar cuke haiṃ"),
            ("They had arrived", "वे आ चुके थे", "ve ā cuke the"),
            ("I had seen", "मैं देख चुका था", "main dekh cukā thā"),
            ("He will have gone", "वह जा चुका होगा", "vah jā cukā hogā"),
            ("Have you read?", "क्या आप पढ़ चुके हैं?", "kyā āp paṛh cuke haiṃ?"),
            ("I have not slept", "मैं सो नहीं चुका", "main so nahī̃ cukā"),
            ("She has cooked", "वह बना चुकी है", "vah banā cukī hai"),
            ("We had met before", "हम पहले मिल चुके थे", "ham pahle mil cuke the"),
            ("By then I will have left", "तब तक मैं जा चुका होऊँगा", "tab tak main jā cukā hoū̃gā"),
            ("He has paid", "वह भुगतान कर चुका है", "vah bhugtān kar cukā hai"),
            ("I have lost my key", "मैं चाबी खो चुका हूँ", "main cābī kho cukā hū̃"),
            ("They have agreed", "वे सहमत हो चुके हैं", "ve sahamat ho cuke haiṃ"),
            ("It has started", "यह शुरू हो चुका है", "yah śurū ho cukā hai"),
            ("We have tried", "हम कोशिश कर चुके हैं", "ham kośiś kar cuke haiṃ"),
            ("She had warned", "वह चेतावनी दे चुकी थी", "vah cetāwanī de cukī thī"),
            ("I will have eaten", "मैं खा चुका होऊँगा", "main khā cukā hoū̃gā"),
        )

    if "negative" in t and "present" in t:
        return _rows(
            ("I do not go", "मैं नहीं जाता", "main nahī̃ jātā"),
            ("We do not eat meat", "हम माँस नहीं खाते", "ham mā̃s nahī̃ khāte"),
            ("She does not sing", "वह नहीं गाती", "vah nahī̃ gātī"),
            ("They do not know", "वे नहीं जानते", "ve nahī̃ jānte"),
            ("I do not like it", "मुझे यह पसंद नहीं", "mujhe yah pasand nahī̃"),
            ("He does not work here", "वह यहाँ काम नहीं करता", "vah yahā̃ kām nahī̃ kartā"),
            ("We do not agree", "हम सहमत नहीं हैं", "ham sahamat nahī̃ haiṃ"),
            ("It does not matter", "इससे कोई फर्क नहीं", "isse koī phark nahī̃"),
            ("I do not remember", "मुझे याद नहीं", "mujhe yād nahī̃"),
            ("She does not come", "वह नहीं आती", "vah nahī̃ ātī"),
            ("They do not listen", "वे नहीं सुनते", "ve nahī̃ sunte"),
            ("I do not have time", "मेरे पास समय नहीं", "mere pās samay nahī̃"),
            ("We do not sell this", "हम यह नहीं बेचते", "ham yah nahī̃ bechte"),
            ("He does not drive", "वह गाड़ी नहीं चलाता", "vah gāṛī nahī̃ calātā"),
            ("I do not understand", "मैं समझता नहीं", "main samajhtā nahī̃"),
            ("Birds do not fly at night", "पक्षी रात में नहीं उड़ते", "pakṣī rāt mẽ nahī̃ uṛte"),
            ("We do not cheat", "हम धोखा नहीं देते", "ham dhokhā nahī̃ dete"),
            ("She does not complain", "वह शिकायत नहीं करती", "vah śikāyat nahī̃ kartī"),
        )

    if "negative" in t and "past" in t:
        return _rows(
            ("I did not go", "मैं नहीं गया", "main nahī̃ gayā"),
            ("We did not see", "हमने नहीं देखा", "hamne nahī̃ dekhā"),
            ("She did not call", "उसने फोन नहीं किया", "usne phon nahī̃ kiyā"),
            ("They did not come", "वे नहीं आए", "ve nahī̃ ā.e"),
            ("He did not pay", "उसने भुगतान नहीं किया", "usne bhugtān nahī̃ kiyā"),
            ("I did not eat", "मैंने नहीं खाया", "mainne nahī̃ khāyā"),
            ("We did not know", "हमें नहीं पता था", "hameṃ nahī̃ patā thā"),
            ("It did not rain", "बारिश नहीं हुई", "bāriś nahī̃ huī"),
            ("She did not agree", "वह सहमत नहीं हुई", "vah sahamat nahī̃ huī"),
            ("They did not wait", "उन्होंने इंतज़ार नहीं किया", "unhoṃne intazār nahī̃ kiyā"),
            ("I did not forget", "मैं भूला नहीं", "main bhūlā nahī̃"),
            ("We did not win", "हम जीते नहीं", "ham jīte nahī̃"),
            ("He did not answer", "उसने जवाब नहीं दिया", "usne javāb nahī̃ diyā"),
            ("Birds did not sing", "पक्षियों ने नहीं गाया", "pakṣiyoṃ ne nahī̃ gāyā"),
            ("I did not sleep", "मैं सोया नहीं", "main soyā nahī̃"),
            ("She did not open", "उसने नहीं खोला", "usne nahī̃ kholā"),
            ("We did not finish", "हमने खत्म नहीं किया", "hamne khatm nahī̃ kiyā"),
            ("They did not stay", "वे ठहरे नहीं", "ve ṭhere nahī̃"),
        )

    if "negative" in t and "future" in t:
        return _rows(
            ("I will not go", "मैं नहीं जाऊँगा", "main nahī̃ jāū̃gā"),
            ("We will not leave", "हम नहीं जाएँगे", "ham nahī̃ jāeṅge"),
            ("She will not come", "वह नहीं आएगी", "vah nahī̃ āegī"),
            ("They will not agree", "वे सहमत नहीं होंगे", "ve sahamat nahī̃ hoṅge"),
            ("He will not pay", "वह भुगतान नहीं करेगा", "vah bhugtān nahī̃ karegā"),
            ("It will not work", "यह काम नहीं करेगा", "yah kām nahī̃ karegā"),
            ("I will not forget", "मैं नहीं भूलूँगा", "main nahī̃ bhūlū̃gā"),
            ("We will not lose", "हम हारेंगे नहीं", "ham hāreṅge nahī̃"),
            ("Rain will not stop", "बारिश नहीं रुकेगी", "bāriś nahī̃ rukegī"),
            ("She will not sing", "वह नहीं गाएगी", "vah nahī̃ gāegī"),
            ("They will not wait", "वे इंतज़ार नहीं करेंगे", "ve intazār nahī̃ kareṅge"),
            ("I will not buy", "मैं नहीं खरीदूँगा", "main nahī̃ kharīdū̃gā"),
            ("He will not drive", "वह गाड़ी नहीं चलाएगा", "vah gāṛī nahī̃ calāegā"),
            ("We will not sell", "हम नहीं बेचेंगे", "ham nahī̃ becheṅge"),
            ("I will not tell", "मैं नहीं बताऊँगा", "main nahī̃ batāū̃gā"),
            ("She will not complain", "वह शिकायत नहीं करेगी", "vah śikāyat nahī̃ karegī"),
            ("They will not return", "वे वापस नहीं आएँगे", "ve vāpas nahī̃ āeṅge"),
            ("We will not delay", "हम देर नहीं करेंगे", "ham der nahī̃ kareṅge"),
        )

    if "question" in t or "wh" in t:
        return _rows(
            ("What is this?", "यह क्या है?", "yah kyā hai?"),
            ("Who is he?", "वह कौन है?", "vah kaun hai?"),
            ("Where do you live?", "आप कहाँ रहते हैं?", "āp kahā̃ rahte haiṃ?"),
            ("When will you come?", "आप कब आएँगे?", "āp kab āeṅge?"),
            ("Why are you sad?", "आप उदास क्यों हैं?", "āp udās kyoṃ haiṃ?"),
            ("How much is it?", "यह कितने का है?", "yah kitne kā hai?"),
            ("Which book?", "कौन सी किताब?", "kaun sī kitāb?"),
            ("Whose pen is this?", "यह कलम किसकी है?", "yah kalam kiskī hai?"),
            ("How are you?", "आप कैसे हैं?", "āp kaise haiṃ?"),
            ("What time is it?", "क्या समय हुआ?", "kyā samay huā?"),
            ("Where is the station?", "स्टेशन कहाँ है?", "sṭeśan kahā̃ hai?"),
            ("Why did you go?", "आप क्यों गए?", "āp kyoṃ ga.e?"),
            ("How many people?", "कितने लोग?", "kitne log?"),
            ("What happened?", "क्या हुआ?", "kyā huā?"),
            ("Who called?", "किसने फोन किया?", "kisne phon kiyā?"),
            ("Where shall we meet?", "हम कहाँ मिलें?", "ham kahā̃ mileṃ?"),
            ("Which way?", "किस रास्ते?", "kis rāste?"),
            ("What do you want?", "आप क्या चाहते हैं?", "āp kyā cāhte haiṃ?"),
        )

    if "preposition" in t and "learn" in t:
        return _rows(
            ("on the table", "मेज़ पर", "mez par"),
            ("under the bed", "बिस्तर के नीचे", "bistar ke nīce"),
            ("in the room", "कमरे में", "kamre mẽ"),
            ("near the door", "दरवाज़े के पास", "darvāze ke pās"),
            ("far from here", "यहाँ से दूर", "yahā̃ se dūr"),
            ("between two trees", "दो पेड़ों के बीच", "do peṛõ ke bīc"),
            ("with my friend", "मेरे दोस्त के साथ", "mere dost ke sāth"),
            ("without money", "पैसे के बिना", "paise ke binā"),
            ("after lunch", "दोपहर के भोजन के बाद", "dopahar ke bhojan ke bād"),
            ("before sunset", "सूर्यास्त से पहले", "sūryāst se pahle"),
            ("towards the city", "शहर की ओर", "śahr kī or"),
            ("from Delhi", "दिल्ली से", "dillī se"),
            ("until tomorrow", "कल तक", "kal tak"),
            ("since Monday", "सोमवार से", "somvār se"),
            ("across the river", "नदी के पार", "nadī ke pār"),
            ("behind the house", "घर के पीछे", "ghar ke pīche"),
            ("inside the box", "डिब्बे के अंदर", "ḍibbe ke andar"),
            ("outside the gate", "गेट के बाहर", "geṭ ke bāhar"),
        )

    if "body" in t and "parts" in t:
        return _rows(
            ("Head", "सिर", "sir"),
            ("Eye", "आँख", "ā̃kh"),
            ("Ear", "कान", "kān"),
            ("Nose", "नाक", "nāk"),
            ("Mouth", "मुँह", "mũh"),
            ("Tooth", "दाँत", "dā̃t"),
            ("Hand", "हाथ", "hāth"),
            ("Finger", "ऊँगली", "ū̃galī"),
            ("Leg", "टाँग", "ṭā̃g"),
            ("Foot", "पैर", "pair"),
            ("Stomach", "पेट", "peṭ"),
            ("Back", "पीठ", "pīṭh"),
            ("Neck", "गर्दन", "gardan"),
            ("Hair", "बाल", "bāl"),
            ("Skin", "त्वचा", "tvacā"),
            ("Heart", "दिल", "dil"),
            ("Bone", "हड्डी", "haḍḍī"),
            ("Blood", "खून", "khūn"),
        )

    if "numbers" in t and "part 1" in t:
        return _rows(
            ("One", "एक", "ek"),
            ("Two", "दो", "do"),
            ("Three", "तीन", "tīn"),
            ("Four", "चार", "cār"),
            ("Five", "पाँच", "pā̃c"),
            ("Six", "छह", "chah"),
            ("Seven", "सात", "sāt"),
            ("Eight", "आठ", "āṭh"),
            ("Nine", "नौ", "nau"),
            ("Ten", "दस", "das"),
            ("Eleven", "ग्यारह", "gyārah"),
            ("Twelve", "बारह", "bārah"),
            ("Thirteen", "तेरह", "terah"),
            ("Fourteen", "चौदह", "caudah"),
            ("Fifteen", "पंद्रह", "pandrah"),
            ("Sixteen", "सोलह", "solah"),
            ("Seventeen", "सत्रह", "satrah"),
            ("Eighteen", "अठारह", "aṭhārah"),
        )

    if "numbers" in t and "part 2" in t:
        return _rows(
            ("Twenty", "बीस", "bīs"),
            ("Thirty", "तीस", "tīs"),
            ("Forty", "चालीस", "cālīs"),
            ("Fifty", "पचास", "pacās"),
            ("Sixty", "साठ", "sāṭh"),
            ("Seventy", "सत्तर", "sattar"),
            ("Eighty", "अस्सी", "assī"),
            ("Ninety", "नब्बे", "nabbe"),
            ("Hundred", "सौ", "sau"),
            ("Two hundred", "दो सौ", "do sau"),
            ("Thousand", "हज़ार", "hazār"),
            ("Ten thousand", "दस हज़ार", "das hazār"),
            ("Lakh", "लाख", "lākh"),
            ("Crore", "करोड़", "karoṛ"),
            ("First", "पहला", "pahlā"),
            ("Second", "दूसरा", "dūsrā"),
            ("Third", "तीसरा", "tīsrā"),
            ("Half", "आधा", "ādhā"),
        )

    if "vegetable" in t:
        return _rows(
            ("Potato", "आलू", "ālū"),
            ("Onion", "प्याज़", "pyāz"),
            ("Tomato", "टमाटर", "ṭamāṭar"),
            ("Carrot", "गाजर", "gājar"),
            ("Cabbage", "पत्ता गोभी", "pattā gobhī"),
            ("Cauliflower", "फूल गोभी", "phūl gobhī"),
            ("Brinjal", "बैंगन", "baiṅgan"),
            ("Ladyfinger", "भिंडी", "bhiṃḍī"),
            ("Spinach", "पालक", "pālak"),
            ("Peas", "मटर", "maṭar"),
            ("Beans", "सेम", "sem"),
            ("Cucumber", "खीरा", "khīrā"),
            ("Radish", "मूली", "mūlī"),
            ("Garlic", "लहसुन", "lahsun"),
            ("Ginger", "अदरक", "adrak"),
            ("Chilli", "मिर्च", "mirc"),
            ("Coriander", "धनिया", "dhaniyā"),
            ("Mint", "पुदीना", "pudīnā"),
        )

    if "fruits" in t:
        return _rows(
            ("Mango", "आम", "ām"),
            ("Banana", "केला", "kelā"),
            ("Apple", "सेब", "seb"),
            ("Orange", "संतरा", "santarā"),
            ("Grapes", "अंगूर", "aṅgūr"),
            ("Watermelon", "तरबूज़", "tarbūz"),
            ("Pomegranate", "अनार", "anār"),
            ("Guava", "अमरूद", "amrūd"),
            ("Papaya", "पपीता", "papītā"),
            ("Pineapple", "अनानास", "anānās"),
            ("Lemon", "नींबू", "nī̃bū"),
            ("Coconut", "नारियल", "nāriyal"),
            ("Cherry", "चेरी", "cerī"),
            ("Pear", "नाशपाती", "nāśpātī"),
            ("Plum", "आलूबुखारा", "ālūbukhārā"),
            ("Peach", "आड़ू", "āṛū"),
            ("Lychee", "लीची", "līcī"),
            ("Fig", "अंजीर", "aṅjīr"),
        )

    if "colours" in t:
        return _rows(
            ("Red", "लाल", "lāl"),
            ("Blue", "नीला", "nīlā"),
            ("Green", "हरा", "harā"),
            ("Yellow", "पीला", "pīlā"),
            ("White", "सफ़ेद", "safed"),
            ("Black", "काला", "kālā"),
            ("Orange (colour)", "नारंगी", "nāraṅgī"),
            ("Pink", "गुलाबी", "gulābī"),
            ("Brown", "भूरा", "bhūrā"),
            ("Grey", "स्लेटी", "sleṭī"),
            ("Purple", "बैंगनी", "baiṅgnī"),
            ("Golden", "सुनहरा", "sunaharā"),
            ("Silver", "चाँदी", "cā̃dī"),
            ("Dark", "गहरा", "gahrā"),
            ("Light", "हल्का", "halkā"),
            ("Bright", "चमकीला", "camkīlā"),
            ("Pale", "फीका", "phīkā"),
            ("Colourful", "रंगीन", "raṅgīn"),
        )

    # default: general Hindi practice
    return _rows(*_fallback_practice())


def get_lesson_rows(cid: int, title: str) -> list[list[str]]:
    if cid in EXACT:
        return EXACT[cid]
    return rows_by_title(cid, title)
