"""Unique Bengali rows per sublesson: 18 lines each (15–20 range).
Grammar/phrase 532–596 and conversation 620–662 use disjoint pools so no sentence repeats across lessons.

Sentence types follow common Bengali pedagogy: declarative (SOV), interrogative (কী/কোথায়/কখন),
yes–no questions, imperative/polite request, and negative or conditional patterns — see e.g. Bengali
sentence structure and sentence-type overviews (Vaia; English-bangla.com kinds of sentence)."""
from __future__ import annotations

# --- Pools for combinatorial unique lines (Bengali must stay natural) ---
_SUBJ = ["আমি", "তুমি", "সে", "আমরা", "তোমরা", "তারা", "বাবা", "মা", "ভাই", "বোন"]
_PLACE = [
    "বাড়িতে",
    "স্কুলে",
    "বাজারে",
    "অফিসে",
    "মাঠে",
    "হাসপাতালে",
    "স্টেশনে",
    "বাসে",
    "ট্রেনে",
    "দোকানে",
]
_TIME = ["আজ", "কাল", "সকালে", "বিকেলে", "রাতে", "এখন", "পরে", "আগে"]
_V_GO = ["যাই", "আসি", "ফিরি", "দাঁড়াই", "বসি", "হাঁটি"]
_V_DO = ["খাই", "দেখি", "পড়ি", "লিখি", "বলি", "শুনি", "করি", "চাই", "বুঝি", "খুঁজি"]
_OBJ = [
    "ভাত",
    "রুটি",
    "চা",
    "জল",
    "বই",
    "খবর",
    "কাজ",
    "সাহায্য",
    "সময়",
    "টাকা",
]

_SUBJ_EN = {
    "আমি": "I",
    "তুমি": "You",
    "সে": "He",
    "আমরা": "We",
    "তোমরা": "You all",
    "তারা": "They",
    "বাবা": "Father",
    "মা": "Mother",
    "ভাই": "Brother",
    "বোন": "Sister",
}
_OBJ_EN = {
    "ভাত": "rice",
    "রুটি": "bread",
    "চা": "tea",
    "জল": "water",
    "বই": "the book",
    "খবর": "the news",
    "কাজ": "the work",
    "সাহায্য": "help",
    "সময়": "time",
    "টাকা": "money",
}
_TIME_EN = {
    "আজ": "today",
    "কাল": "tomorrow",
    "সকালে": "in the morning",
    "বিকেলে": "in the evening",
    "রাতে": "at night",
    "এখন": "now",
    "পরে": "later",
    "আগে": "earlier",
}
# Present-tense English (simple present / habitual); third person gets -s where needed
_V_EN = {
    "খাই": ("eat", "eats"),
    "দেখি": ("see", "sees"),
    "পড়ি": ("read", "reads"),
    "লিখি": ("write", "writes"),
    "বলি": ("say", "says"),
    "শুনি": ("hear", "hears"),
    "করি": ("do", "does"),
    "চাই": ("want", "wants"),
    "বুঝি": ("understand", "understands"),
    "খুঁজি": ("look for", "looks for"),
}
_THIRD = {"সে", "বাবা", "মা", "ভাই", "বোন"}


def _en_verb_agree(subj: str, v: str) -> str:
    pair = _V_EN[v]
    return pair[1] if subj in _THIRD else pair[0]


def _roman_subj(s: str) -> str:
    m = {
        "আমি": "Āmi",
        "তুমি": "Tumi",
        "সে": "Sē",
        "আমরা": "Āmrā",
        "তোমরা": "Tōmrā",
        "তারা": "Tārā",
        "বাবা": "Bābā",
        "মা": "Mā",
        "ভাই": "Bhāi",
        "বোন": "Bōn",
    }
    return m.get(s, s)


def _roman_v(v: str) -> str:
    return v[0].upper() + v[1:] if v else v


_PLACE_EN = {
    "বাড়িতে": "home",
    "স্কুলে": "school",
    "বাজারে": "the market",
    "অফিসে": "the office",
    "মাঠে": "the field",
    "হাসপাতালে": "the hospital",
    "স্টেশনে": "the station",
    "বাসে": "the bus",
    "ট্রেনে": "the train",
    "দোকানে": "the shop",
}
_V_GO_EN = {
    "যাই": ("go", "goes"),
    "আসি": ("come", "comes"),
    "ফিরি": ("return", "returns"),
    "দাঁড়াই": ("stand", "stands"),
    "বসি": ("sit", "sits"),
    "হাঁটি": ("walk", "walks"),
}


def _go_agree(subj: str, v: str) -> str:
    p = _V_GO_EN[v]
    return p[1] if subj in _THIRD else p[0]


def _gp_declarative(gi: int) -> tuple[str, str, str]:
    """Simple declarative (habitual present) with natural English gloss."""
    a = _SUBJ[gi % 10]
    c = _OBJ[(gi // 10) % 10]
    b = _V_DO[(gi // 100) % 10]
    t = _TIME[(gi // 1000) % 8]
    bn = f"{a} {t} {c} {b}।"
    subj = _SUBJ_EN[a]
    ven = _en_verb_agree(a, b)
    obj = _OBJ_EN[c]
    timep = _TIME_EN[t]
    en = f"{subj} {ven} {obj} {timep}."
    rom = f"{_roman_subj(a)} {t} {c} {_roman_v(b)}."
    return (en, bn, rom)


def _gp_wh_question(gi: int) -> tuple[str, str, str]:
    """WH-questions (কোথায়, কখন, কী, কেন)."""
    slot = gi // 5
    o = _OBJ[slot % 10]
    p = _PLACE[(slot // 10) % 10]
    s = _SUBJ[(slot // 3) % 10]
    k = slot % 5
    if k == 0:
        bn = f"{o}টা কোথায়?"
        en = f"Where is the {_OBJ_EN[o]}?"
        rom = f"{o}ṭā kōthāy?"
    elif k == 1:
        sp = _SUBJ[3 + (slot % 5)]
        bn = f"{sp} কোথায় গেল?"
        en = f"Where did {_SUBJ_EN[sp]} go?"
        rom = f"{_roman_subj(sp)} kōthāy gēl?"
    elif k == 2:
        bn = f"আমরা কখন {p} যাব?"
        en = f"When shall we go to {_PLACE_EN[p]}?"
        rom = f"Āmrā kôkhon {p} jābo?"
    elif k == 3:
        opts = [
            ("Why the delay?", "কেন দেরি হলো?", "Kēn dēri hōlō?"),
            ("Why so late?", "কেন এত দেরি?", "Kēn ētō dēri?"),
            ("What is the reason?", "কারণ কী?", "Kāraṇ ki?"),
            ("How much is the fare?", "ভাড়া কত?", "Bhāṛā kôt?"),
            ("Whose bag is this?", "এটা কার ব্যাগ?", "Ēṭā kār bẽg?"),
        ]
        en, bn, rom = opts[slot % len(opts)]
    else:
        opts = [
            ("What is happening here?", "কী হচ্ছে এখানে?", "Ki hochchhe ēkhāne?"),
            ("What should we do?", "আমরা কী করব?", "Āmrā ki korbo?"),
            ("Which bus goes there?", "কোন বাস ওখানে যায়?", "Kōn bās ōkhāne jāy?"),
            ("How far is it?", "কত দূর?", "Kôt dūr?"),
            ("Who is coming?", "কে আসছে?", "Kē āschhe?"),
        ]
        en, bn, rom = opts[slot % len(opts)]
    return (en, bn, rom)


def _gp_yes_no_question(gi: int) -> tuple[str, str, str]:
    """Polar questions (কি … ?) with natural English."""
    slot = gi // 5
    a = _SUBJ[slot % 10]
    c = _OBJ[(slot // 10) % 10]
    b = _V_DO[(slot // 100) % 10]
    t = _TIME[(slot // 1000) % 8]
    bn = f"{a} কি {t} {c} {b}?"
    ven = _V_EN[b][0]
    obj = _OBJ_EN[c]
    timep = _TIME_EN[t]
    if a == "আমি":
        en = f"Do I {ven} {obj} {timep}?"
    elif a == "তুমি":
        en = f"Do you {ven} {obj} {timep}?"
    elif a in ("তোমরা",):
        en = f"Do you all {ven} {obj} {timep}?"
    elif a == "আমরা":
        en = f"Do we {ven} {obj} {timep}?"
    elif a == "তারা":
        en = f"Do they {ven} {obj} {timep}?"
    elif a == "সে":
        en = f"Does he {ven} {obj} {timep}?"
    else:
        en = f"Does {_SUBJ_EN[a]} {ven} {obj} {timep}?"
    rom = f"{_roman_subj(a)} ki {t} {c} {b}?"
    return (en, bn, rom)


def _gp_imperative_row(gi: int) -> tuple[str, str, str]:
    """Polite imperatives and requests; (en, bn, rom) order."""
    slot = gi // 5
    o = _OBJ[slot % 10]
    p = _PLACE[(slot // 10) % 10]
    pick = (slot * 11 + (slot // 7)) % 16
    rows = [
        ("Please sit down.", "দয়া করে বসুন।", "Dôya kōre bôsun."),
        ("Please wait a moment.", "একটু অপেক্ষা করুন।", "Ekoṭu ôpekhshā kôrun."),
        ("Open the door.", "দরজা খুলুন।", "Dôrjā khulun."),
        ("Listen quietly.", "চুপ করে শুনুন।", "Chup kōre shunun."),
        (f"Please pass the {_OBJ_EN[o]}.", f"{o}টা দিন।", f"{o}ṭā din."),
        (f"Please go to {_PLACE_EN[p]}.", f"{p} যান।", f"{p} jān."),
        ("Please come here.", "এখানে আসুন।", "Ēkhāne āsun."),
        ("Please speak slowly.", "ধীরে বলুন।", "Dhīre bôlun."),
        ("Please write clearly.", "স্পষ্ট লিখুন।", "Spôshṭo likhun."),
        ("Please read aloud.", "জোরে পড়ুন।", "Jōre pōṛun."),
        ("Please stand in line.", "লাইনে দাঁড়ান।", "Lāine dãṛān."),
        ("Please show your ticket.", "টিকিট দেখান।", "Ṭikiṭ dēkhān."),
        ("Please turn left.", "বাঁ দিকে মোড় দিন।", "Bã dikē mōṛ din."),
        ("Please keep quiet.", "নীরব থাকুন।", "Nīrob thākun."),
        ("Please help me.", "আমাকে সাহায্য করুন।", "Āmākē sāhājjo kôrun."),
        ("Please call later.", "পরে ফোন করুন।", "Pōre phōn kôrun."),
    ]
    en, bn, rom = rows[pick % len(rows)]
    return (en, bn, rom)


def _gp_negative_or_conditional(gi: int) -> tuple[str, str, str]:
    """Negation or simple conditional (যদি … তবে …)."""
    slot = gi // 5
    k = slot % 4
    if k == 0:
        a = _SUBJ[slot % 10]
        p = _PLACE[(slot // 10) % 10]
        bn = f"{a} {p} যাব না।"
        en = f"{_SUBJ_EN[a]} will not go to {_PLACE_EN[p]}."
        rom = f"{_roman_subj(a)} {p} jābo nā."
    elif k == 1:
        opts = [
            ("I did not understand.", "আমি বুঝিনি।", "Āmi bujhini."),
            ("I did not hear.", "আমি শুনিনি।", "Āmi shunini."),
            ("He did not come.", "সে আসেনি।", "Sē āsēni."),
            ("We did not agree.", "আমরা রাজি হইনি।", "Āmrā rāji hoini."),
            ("They will not leave.", "তারা যাবে না।", "Tārā jābe nā."),
            ("She cannot come today.", "সে আজ আসতে পারবে না।", "Sē āj āste pārbe nā."),
            ("I will not forget.", "আমি ভুলব না।", "Āmi bhulbo nā."),
            ("Do not run here.", "এখানে দৌড়ো না।", "Ēkhāne douṛō nā."),
        ]
        en, bn, rom = opts[slot % len(opts)]
    elif k == 2:
        opts = [
            ("If it rains, we will stay.", "বৃষ্টি হলে আমরা থাকব।", "Briṣṭi hōle āmrā thākbo."),
            ("If you come, call me.", "তুমি এলে আমাকে ডাকো।", "Tumi ēle āmākē ḍākō."),
            ("If there is time, we will go.", "সময় থাকলে যাব।", "Somoy thākle jābo."),
            ("Unless you try, you will not learn.", "চেষ্টা না করলে শিখবে না।", "Chēṣṭā nā korlē shikhbe nā."),
        ]
        en, bn, rom = opts[slot % len(opts)]
    else:
        opts = [
            ("I will call when there is time.", "সময় হলে ফোন করব।", "Somoy hōle phōn korbo."),
            ("Tell me when you arrive.", "পৌঁছালে বলো।", "Poũchhālē bōlō."),
            ("We will eat after work.", "কাজ শেষে খাব।", "Kāj shēshē khāb."),
            ("Come before evening.", "সন্ধ্যার আগে এসো।", "Sondhyār āgē ēsō."),
        ]
        en, bn, rom = opts[slot % len(opts)]
    return (en, bn, rom)


def _grammar_practice_line(gi: int) -> tuple[str, str, str]:
    """Rotate sentence types; English matches Bengali (no generic drill labels)."""
    k = gi % 5
    if k == 0:
        return _gp_declarative(gi)
    if k == 1:
        return _gp_wh_question(gi)
    if k == 2:
        return _gp_yes_no_question(gi)
    if k == 3:
        return _gp_imperative_row(gi)
    return _gp_negative_or_conditional(gi)


def _cv_movement_decl(gi: int) -> tuple[str, str, str]:
    """Declarative movement with natural English."""
    a = _SUBJ[(gi * 2) % len(_SUBJ)]
    p = _PLACE[gi % len(_PLACE)]
    v = _V_GO[gi % len(_V_GO)]
    tm = _TIME[(gi // 7) % len(_TIME)]
    bn = f"{a} {tm} {p} {v}।"
    ven = _go_agree(a, v)
    subj = _SUBJ_EN[a]
    pl = _PLACE_EN[p]
    tim = _TIME_EN[tm]
    if p == "বাড়িতে":
        en = f"{subj} {ven} home {tim}."
    elif p in ("বাসে", "ট্রেনে"):
        en = f"{subj} {ven} on {pl} {tim}."
    else:
        en = f"{subj} {ven} to {pl} {tim}."
    rom = f"{_roman_subj(a)} {tm} {p} {v}."
    return (en, bn, rom)


def _cv_question_offer(gi: int) -> tuple[str, str, str]:
    """Questions and offers for travel / movement contexts."""
    slot = gi // 5
    p = _PLACE[slot % len(_PLACE)]
    rows = [
        ("Where are you going?", "তুমি কোথায় যাচ্ছ?", "Tumi kōthāy jāchchho?"),
        ("When does the bus leave?", "বাস কখন ছাড়ে?", "Bās kôkhon chhāṛe?"),
        ("Shall we walk?", "আমরা কি হেঁটে যাব?", "Āmrā ki hẽṭe jābo?"),
        ("Is the station far?", "স্টেশন কি দূরে?", "Sṭēshon ki dūre?"),
        ("Can you drop me here?", "আমাকে এখানে নামিয়ে দেবেন?", "Āmākē ēkhāne nāmiyē deben?"),
        (f"Let us meet near {_PLACE_EN[p]}.", f"চলো {p} কাছে দেখা করি।", f"Chōlō {p} kāchhe dēkhā kori."),
        ("Which way to the market?", "বাজার কোন দিকে?", "Bājār kôn dikē?"),
        ("Is this the right bus?", "এই বাসটা ঠিক?", "Ei bāsṭā ṭhik?"),
        ("How much is the ticket?", "টিকিট কত?", "Ṭikiṭ kôt?"),
        ("Is there a seat free?", "খালি আসন আছে?", "Khāli āsôn āchhe?"),
        ("Could you speak slower?", "একটু আস্তে বলবেন?", "Ekoṭu āste bōlben?"),
        ("Where do I get down?", "কোথায় নামব?", "Kōthāy nāmobo?"),
        ("Does this road go to the station?", "এই রাস্তা স্টেশন যায়?", "Ei rāstā sṭēshon jāy?"),
        ("Can we get a taxi?", "ট্যাক্সি পাব?", "Ṭyāksi pāb?"),
        ("Is the shop open now?", "দোকান এখন খোলা?", "Dokān ēkhon khōlā?"),
        ("Where is the ticket counter?", "টিকিট কাউন্টার কোথায়?", "Ṭikiṭ kaunṭār kōthāy?"),
    ]
    en, bn, rom = rows[slot % len(rows)]
    return (en, bn, rom)


def _conversation_practice_line(gi: int) -> tuple[str, str, str]:
    """Movement declaratives and situational questions; natural English."""
    if gi % 2 == 0:
        return _cv_movement_decl(gi)
    return _cv_question_offer(gi)


def _combo_line(global_idx: int, style: str) -> tuple[str, str, str]:
    """Backward-compatible name: grammar/phrase or conversation fill lines."""
    if style == "gp":
        return _grammar_practice_line(global_idx)
    return _conversation_practice_line(global_idx)


def _topic_openers_grammar(cid: int) -> list[tuple[str, str, str]]:
    """First 3–5 lines tailored to lesson theme (unique English per cid)."""
    t = {
        532: [
            ("The boys are playing in the field.", "ছেলেরা মাঠে খেলছে।", "Chēlērā māṭhe khelchhe."),
            ("The girls are reading books.", "মেয়েরা বই পড়ছে।", "Mēẏērā bôi pōṛchhe."),
            ("We are students.", "আমরা ছাত্র।", "Āmrā chātrô."),
        ],
        533: [
            ("The book is on the table.", "বইটা টেবিলের উপরে।", "Bôiṭā ṭēbilēr upore."),
            ("He lives in Kolkata.", "সে কলকাতায় থাকে।", "Sē Kolkātāy thākē."),
            ("Come with me.", "আমার সঙ্গে এসো।", "Āmār songe ēsō."),
        ],
        534: [
            ("Near the bank.", "ব্যাংকের কাছে।", "Bēṅkēr kāchhe."),
            ("Far from home.", "বাড়ি থেকে দূরে।", "Bāṛi theke dūre."),
            ("Between two houses.", "দুই বাড়ির মাঝে।", "Dui bāṛir mājhe."),
        ],
        535: [
            ("I give him a book.", "আমি তাকে বই দিই।", "Āmi tākē bôi dii."),
            ("This is for you.", "এটা তোমার জন্য।", "Ēṭā tōmār jônyo."),
            ("From Kolkata to Delhi.", "কলকাতা থেকে দিল্লি।", "Kolkātā theke Dilli."),
        ],
        536: [
            ("Please sit down.", "দয়া করে বসুন।", "Dôya kōre bôsun."),
            ("Open the door.", "দরজা খুলুন।", "Dôrjā khulun."),
            ("Don't run here.", "এখানে দৌড়াবেন না।", "Ēkhāne douṛāben nā."),
        ],
        537: [
            ("What time is it?", "কটা বাজে?", "Koṭā bāje?"),
            ("Tomorrow morning.", "আগামীকাল সকালে।", "Āgāmīkāl sākālē."),
            ("Last week I was busy.", "গত সপ্তাহে আমি ব্যস্ত ছিলাম।", "Gôtô soptāhē āmi bēsto chhilām."),
        ],
        538: [
            ("He made me laugh.", "সে আমাকে হাসাল।", "Sē āmākē hāsāl."),
            ("She teaches children.", "সে বাচ্চাদের পড়ায়।", "Sē bāchchādēr pōṛāy."),
            ("Get the work done.", "কাজ শেষ করান।", "Kāj shēsh korān."),
        ],
        539: [
            ("Those boys are tall.", "ওই ছেলেরা লম্বা।", "Ōi chēlērā lombā."),
            ("These girls are clever.", "এই মেয়েরা চালাক।", "Ei mēẏērā chālāk."),
            ("We are ready.", "আমরা প্রস্তুত।", "Āmrā prôstut."),
        ],
        540: [
            ("I have finished.", "আমি শেষ করেছি।", "Āmi shēsh korechhi."),
            ("They had left.", "তারা চলে গিয়েছিল।", "Tārā chōlē giyēchil."),
            ("By then we will go.", "তখন আমরা যাব।", "Tokhon āmrā jābo."),
        ],
        541: [
            ("I was reading then.", "তখন আমি পড়ছিলাম।", "Tokhon āmi pōṛchilām."),
            ("She has been singing.", "সে গাইছিল।", "Sē gāichhil."),
            ("We will have eaten.", "আমরা খেয়ে ফেলব।", "Āmrā khēye phelbo."),
        ],
        542: [
            ("I do not want rice.", "আমি ভাত চাই না।", "Āmi bhāt chāi nā."),
            ("I don't need it.", "আমার দরকার নেই।", "Āmār dôrkār nēi."),
            ("No, thanks.", "না, ধন্যবাদ।", "Nā, dhonyobād."),
        ],
    }
    base = t.get(
        cid,
        [
            (f"Lesson {cid} example A.", f"আমি পাঠ {cid} অনুশীলন করি।", f"Āmi pāṭh {cid} ônushīlon kori."),
            (f"Lesson {cid} example B.", f"এটি পাঠ {cid} এর বাক্য।", f"Eṭi pāṭh {cid} er bākya."),
            (f"Lesson {cid} example C.", f"বাংলা শিখতে ভালো লাগে।", f"Bāṅlā shikhte bhālō lāgē."),
        ],
    )
    return base


def _topic_openers_phrase(cid: int) -> list[tuple[str, str, str]]:
    """Thematic openers for phrase-structure lessons (543–596)."""
    themes: dict[int, list[tuple[str, str, str]]] = {
        543: [
            ("I am going to eat.", "আমি খেতে যাচ্ছি।", "Āmi khete jāchchhi."),
            ("She is going to sing.", "সে গাইতে যাচ্ছে।", "Sē gāite jāchchhe."),
            ("We are going to leave.", "আমরা চলে যাচ্ছি।", "Āmrā chōlē jāchchhi."),
        ],
        544: [
            ("I used to play here.", "আমি এখানে খেলতাম।", "Āmi ēkhāne kheltām."),
            ("He used to read a lot.", "সে অনেক পড়ত।", "Sē ônek pōṛtō."),
            ("They used to live there.", "তারা সেখানে থাকত।", "Tārā shēkhāne thāktō."),
        ],
        545: [
            ("Earlier people walked more.", "আগে মানুষ বেশি হাঁটত।", "Āgē mānuṣ bēshi hãṭtō."),
            ("In childhood I swam often.", "ছোটবেলায় আমি প্রায় সাঁতার কাটতাম।", "Choṭobēlāẏ āmi prāẏ sãtār kāṭtām."),
            ("They used to walk slowly.", "তারা ধীরে ধীরে হাঁটত।", "Tārā dhīre dhīre hãṭtō."),
        ],
        546: [
            ("If it rains, I will stay.", "বৃষ্টি হলে আমি থাকব।", "Briṣṭi hōle āmi thākbo."),
            ("If you come, call me.", "তুমি এলে আমাকে ডাকো।", "Tumi ēle āmākē ḍākō."),
            ("If he agrees, we will start.", "সে রাজি হলে শুরু করব।", "Sē rāji hōle shuru korbo."),
        ],
        547: [
            ("I depend on you.", "আমি তোমার উপর নির্ভর করি।", "Āmi tōmār upor nirbhor kori."),
            ("Think about the plan.", "পরিকল্পনা নিয়ে ভাবো।", "Pôrikolponā niyē bhābō."),
            ("Wait for the bus.", "বাসের জন্য অপেক্ষা করো।", "Bāser jônyo ôpekhshā kōrō."),
        ],
        548: [
            ("This flower is beautiful.", "এই ফুলটা সুন্দর।", "Ei phulṭā sundor."),
            ("The water is cold.", "জলটা ঠান্ডা।", "Jolṭā ṭhāṇḍā."),
            ("His idea is good.", "তার ধারণা ভালো।", "Tār dhārôṇā bhālō."),
        ],
        549: [
            ("I can swim.", "আমি সাঁতার কাটতে পারি।", "Āmi sãtār kāṭte pāri."),
            ("Can you help?", "তুমি কি সাহায্য করতে পারো?", "Tumi ki sāhājjo korte pārō?"),
            ("She cannot come today.", "সে আজ আসতে পারবে না।", "Sē āj āste pārbe nā."),
        ],
        550: [
            ("I want water.", "আমার জল চাই।", "Āmār jol chāi."),
            ("We need rest.", "আমাদের বিশ্রাম দরকার।", "Āmādēr bishrām dôrkār."),
            ("He wants to sleep.", "সে ঘুমাতে চায়।", "Sē ghumāte chāy."),
        ],
    }
    _551 = {
        551: [
            ("It became dark.", "অন্ধকার হয়ে গেল।", "Ôndhokār hōye gēl."),
            ("What happened?", "কী হয়েছে?", "Ki hōyēchhe?"),
            ("The festival will happen soon.", "উৎসব শীঘ্রই হবে।", "Utsôb shīghroi hōbe."),
        ],
        552: [
            ("You should rest.", "তোমার বিশ্রাম নেওয়া উচিত।", "Tōmār bishrām nēōẏā uchit."),
            ("We should help.", "আমাদের সাহায্য করা উচিত।", "Āmādēr sāhājjo korā uchit."),
            ("Children should study.", "বাচ্চাদের পড়া উচিত।", "Bāchchādēr pōṛā uchit."),
        ],
        553: [
            ("I must go now.", "আমাকে এখন যেতেই হবে।", "Āmākē ēkhon jētēi hōbe."),
            ("You must bring the ticket.", "আপনাকে টিকিট আনতে হবে।", "Āpnākē ṭikiṭ ānte hōbe."),
            ("We have to finish today.", "আজই শেষ করতে হবে।", "Āji shēsh korte hōbe."),
        ],
        554: [
            ("It kept raining.", "বৃষ্টি হতে হতে চলছিল।", "Briṣṭi hote hote cholchhil."),
            ("He kept talking.", "সে বলতে বলতে চলেছিল।", "Sē bolte bolte chhil."),
            ("She kept trying.", "সে চেষ্টা করতে করতে চলেছিল।", "Sē chēṣṭā korte korte chhil."),
        ],
        555: [
            ("This is bigger than that.", "এটা ওটার চেয়ে বড়।", "Ēṭā ōṭār cheye boṛ."),
            ("She is the tallest.", "সে সবচেয়ে লম্বা।", "Sē sôbcheye lombā."),
            ("He runs faster.", "সে দ্রুত দৌড়ায়।", "Sē drut douṛāy."),
        ],
        556: [
            ("I know the answer.", "আমি উত্তর জানি।", "Āmi uttor jāni."),
            ("Do you know him?", "তুমি কি তাকে চেনো?", "Tumi ki tākē chēnō?"),
            ("Nobody knew the truth.", "কেউ সত্যি জানত না।", "Kēu sôtyi jāntō nā."),
        ],
        557: [
            ("Let us go.", "চলো যাই।", "Chōlō jāi."),
            ("Let him speak.", "তাকে বলতে দিন।", "Tākē bolte din."),
            ("Shall we start?", "আমরা কি শুরু করব?", "Āmrā ki shuru korbo?"),
        ],
        558: [
            ("The book that I bought.", "যে বইটা কিনেছি।", "Jē bôiṭā kinechhi."),
            ("Tell me what you want.", "তুমি কী চাও বলো।", "Tumi ki chāo bōlō."),
            ("I know that he came.", "আমি জানি সে এসেছে।", "Āmi jāni sē ēsechhe."),
        ],
        559: [
            ("Please sign here.", "দয়া করে এখানে সই করুন।", "Dôya kōre ēkhāne sôi kôrun."),
            ("Kindly wait outside.", "অনুগ্রহ করে বাইরে অপেক্ষা করুন।", "Ônugrôh kôre bāire ôpekhshā kôrun."),
            ("Do not smoke here.", "এখানে ধূমপান করবেন না।", "Ēkhāne dhūmpān kôrben nā."),
        ],
        560: [
            ("I like music.", "আমার গান পছন্দ।", "Āmār gān pôchondo."),
            ("She likes to draw.", "সে ছবি আঁকতে পছন্দ করে।", "Sē chobi ãkte pôchondo kōre."),
            ("We like this place.", "আমাদের এই জায়গাটা ভালো লাগে।", "Āmādēr ei jāẏgāṭā bhālō lāgē."),
        ],
        561: [
            ("I would visit every week.", "আমি প্রতি সপ্তাহে যেতাম।", "Āmi prôti soptāhē jētām."),
            ("He would read at night.", "সে রাতে পড়ত।", "Sē rātē pōṛtō."),
            ("They would help us.", "তারা আমাদের সাহায্য করত।", "Tārā āmādēr sāhājjo kortō."),
        ],
        562: [
            ("I understand Bengali now.", "আমি এখন বাংলা বুঝি।", "Āmi ēkhon bāṅlā bujhi."),
            ("Suddenly I came to know.", "হঠাৎ জানতে পারলাম।", "Hoṭāt jānte pārlām."),
            ("Did you understand the rule?", "তুমি নিয়মটা বুঝেছো?", "Tumi niyomṭā bujhechho?"),
        ],
        563: [
            ("You are coming, aren't you?", "তুমি আসছো, তো?", "Tumi āschho, tō?"),
            ("It is nice, isn't it?", "ভালো, তাই না?", "Bhālō, tāi nā?"),
            ("He can swim, can't he?", "সে সাঁতার কাটতে পারে, না?", "Sē sãtār kāṭte pārē, nā?"),
        ],
        564: [
            ("Remember your keys.", "চাবি মনে রাখো।", "Chābi mōne rākho."),
            ("I forgot the date.", "আমি তারিখ ভুলে গেছি।", "Āmi tārikh bhule gēchhi."),
            ("Please remind me tomorrow.", "কাল মনে করিয়ে দিও।", "Kāl mōne koriyē dio."),
        ],
        565: [
            ("I want to learn.", "আমি শিখতে চাই।", "Āmi shikhte chāi."),
            ("She wants to leave early.", "সে তাড়াতাড়ি যেতে চায়।", "Sē ṭāṛāṭāṛi jēte chāy."),
            ("We want to book tickets.", "আমরা টিকিট কাটতে চাই।", "Āmrā ṭikiṭ kāṭte chāi."),
        ],
        566: [
            ("I want you to read this.", "আমি চাই তুমি এটা পড়ো।", "Āmi chāi tumi ēṭā pōṛō."),
            ("Mother wants him to sleep.", "মা চায় সে ঘুমাক।", "Mā chāy sē ghumāk."),
            ("They want us to wait.", "তারা চায় আমরা অপেক্ষা করি।", "Tārā chāy āmrā ôpekhshā kori."),
        ],
        567: [
            ("We were supposed to meet.", "আমাদের দেখা হওয়ার কথা ছিল।", "Āmādēr dēkhā hōẏār kōthā chhil."),
            ("The train was due at five.", "ট্রেন পাঁচটায় আসার কথা ছিল।", "Ṭrēn pā̃choṭāy āsār kōthā chhil."),
            ("He was supposed to call.", "তাকে ফোন করার কথা ছিল।", "Tākē phōn korār kōthā chhil."),
        ],
        568: [
            ("I like to sing songs.", "আমার গান গাইতে ভালো লাগে।", "Āmār gān gāite bhālō lāgē."),
            ("She likes to cook rice.", "সে ভাত রান্না করতে পছন্দ করে।", "Sē bhāt rānnā korte pôchondo kōre."),
            ("We like walking in the park.", "আমাদের পার্কে হাঁটতে ভালো লাগে।", "Āmādēr pāṛke hãṭte bhālō lāgē."),
        ],
        569: [
            ("I need a pen.", "আমার কলম লাগে।", "Āmār kolom lāgē."),
            ("This book belongs to her.", "এই বইটা তার।", "Ei bôiṭā tār."),
            ("Money matters here.", "এখানে টাকা লাগে।", "Ēkhāne ṭākā lāgē."),
        ],
        570: [
            ("What are you doing?", "কী করছো?", "Ki korchho?"),
            ("Come here!", "এদিকে এসো!", "Ēdikē ēsō!"),
            ("Can't now.", "এখন পারি না।", "Ēkhon pāri nā."),
        ],
        571: [
            ("Happy birthday!", "শুভ জন্মদিন!", "Shubh jônmodin!"),
            ("Good morning!", "সুপ্রভাত!", "Suprobhāt!"),
            ("Many happy returns!", "আরও অনেক হোক!", "Ārō ônek hōk!"),
        ],
        572: [
            ("I will finish eating.", "খেয়ে নেব।", "Khēye nebo."),
            ("He looked carefully.", "খেয়াল করে দেখল।", "Khēẏāl kōre dēkhlo."),
            ("We went and saw.", "গিয়ে দেখলাম।", "Giyē dēkhlām."),
        ],
        573: [
            ("Sister, listen.", "দিদি, শোনো।", "Didi, shōnō."),
            ("Brother, wait.", "ভাই, একটু দাঁড়াও।", "Bhāi, ekoṭu dãṛāo."),
            ("Uncle, come in.", "কাকা, ভিতরে আসুন।", "Kākā, bhitore āsun."),
        ],
        574: [
            ("How beautiful!", "কী সুন্দর!", "Ki sundor!"),
            ("Oh no!", "ওহ্!", "Oh!"),
            ("What a surprise!", "কী আশ্চর্য!", "Ki āshchôrjo!"),
        ],
        575: [
            ("May I come in?", "আমি কি ভিতরে আসতে পারি?", "Āmi ki bhitore āste pāri?"),
            ("Can you help me?", "আপনি কি আমাকে সাহায্য করবেন?", "Āpni ki āmākē sāhājjo kōrben?"),
            ("Could you repeat that?", "আবার বলবেন?", "Ābār bōlben?"),
        ],
        576: [
            ("It might rain.", "বৃষ্টি হতে পারে।", "Briṣṭi hote pārē."),
            ("He might be late.", "সে দেরি করতে পারে।", "Sē dēri korte pārē."),
            ("She might not come.", "সে নাও আসতে পারে।", "Sē nāo āste pārē."),
        ],
        577: [
            ("A broken chair.", "ভাঙা চেয়ার।", "Bhāṅā cheẏār."),
            ("Boiled rice.", "সিদ্ধ ভাত।", "Siddho bhāt."),
            ("Written letter.", "লেখা চিঠি।", "Lēkhā chiṭhi."),
        ],
        578: [
            ("The roof above.", "উপরের ছাদ।", "Uporēr chād."),
            ("The floor below.", "নিচের মেঝে।", "Nīchēr mējē."),
            ("The shop across the road.", "রাস্তার ওপারের দোকান।", "Rāstār opārēr dokān."),
        ],
        579: [
            ("May you be well!", "ভালো থেকো!", "Bhālō thekō!"),
            ("May peace prevail!", "শান্তি হোক!", "Shānti hōk!"),
            ("I hope you win.", "আশা করি জিতবে।", "Āshā kori jitbe."),
        ],
        580: [
            ("I made him laugh.", "আমি তাকে হাসালাম।", "Āmi tākē hāsālām."),
            ("She fed the child.", "সে বাচ্চাকে খাইয়ে দিল।", "Sē bāchchākē khāẏe dil."),
            ("Get it printed.", "ছাপিয়ে নিন।", "Chāpiyē nin."),
        ],
        581: [
            ("Someone called.", "কেউ ডেকেছিল।", "Kēu ḍēkēchil."),
            ("I looked everywhere.", "আমি সব জায়গায় খুঁজেছি।", "Āmi sôb jāẏgāẏ khujhechhi."),
            ("Nothing is easy.", "কিছুই সহজ নয়।", "Kichhui sôhoj nôy."),
        ],
        582: [
            ("I have two brothers.", "আমার দুই ভাই আছে।", "Āmār dui bhāi āchhe."),
            ("She has a bicycle.", "তার একটি সাইকেল আছে।", "Tār ekti sāikel āchhe."),
            ("We have time today.", "আজ আমাদের সময় আছে।", "Āj āmādēr somoy āchhe."),
        ],
        583: [
            ("What does this mean?", "এর মানে কী?", "Er mānē ki?"),
            ("Explain the word.", "শব্দটা বোঝান।", "Shôbdoṭā bōjhān."),
            ("I meant to say sorry.", "আমি দুঃখিত বলতে চেয়েছিলাম।", "Āmi duhkhito bolte cheẏechhilām."),
        ],
        584: [
            ("Tea and biscuits.", "চা এবং বিস্কুট।", "Chā ebông biskuṭ."),
            ("But it is late.", "কিন্তু দেরি হয়ে গেছে।", "Kintu dēri hōye gēchhe."),
            ("Because it rained.", "কারণ বৃষ্টি হয়েছিল।", "Kāraṇ briṣṭi hōyēchil."),
        ],
        585: [
            ("Coffee or tea?", "কফি নাকি চা?", "Kôfi nāki chā?"),
            ("Neither this nor that.", "না এটা না ওটা।", "Nā ēṭā nā ōṭā."),
            ("If you agree, we go.", "তুমি রাজি হলে যাব।", "Tumi rāji hōle jābo."),
        ],
        586: [
            ("As you wish.", "যেমন ইচ্ছা।", "Jēmon icchā."),
            ("Although it is hard.", "যদিও কঠিন।", "Jôdio kôṭhin."),
            ("As long as you stay.", "যতক্ষণ তুমি থাকবে।", "Jôtôkhôn tumi thākbe."),
        ],
        587: [
            ("As soon as he arrived.", "সে এসেই।", "Sē ēsei."),
            ("Once you finish, call.", "একবার শেষ হলে ফোন করো।", "Ekbār shēsh hōle phōn kōrō."),
            ("So that we can rest.", "যেন আমরা বিশ্রাম নিতে পারি।", "Jēn āmrā bishrām nite pāri."),
        ],
        588: [
            ("And, also, then.", "এবং, আর, তারপর।", "Ebông, ār, tārpor."),
            ("But, however.", "কিন্তু, তবু।", "Kintu, tubu."),
            ("Therefore, hence.", "সুতরাং, তাই।", "Sutarāṅ, tāi."),
        ],
        589: [
            ("Join the two sentences.", "দুটো বাক্য জোড়া দাও।", "Duṭō bākya jōṛā dāo."),
            ("Use a connector.", "সংযোজক ব্যবহার করো।", "Songjojôk bôbohār kōrō."),
            ("Read the paragraph aloud.", "অনুচ্ছেদ জোরে পড়ো।", "Ônuchchhēd jōre pōṛō."),
        ],
        590: [
            ("He sat down suddenly.", "হঠাৎ বসে পড়ল।", "Hoṭāt bōse pōṛlo."),
            ("She stood up slowly.", "ধীরে ধীরে উঠল।", "Dhīre dhīre uṭhlo."),
            ("We looked around.", "আমরা চারদিকে তাকালাম।", "Āmrā chārdikē tākālām."),
        ],
        591: [
            ("Rice is cooked here.", "এখানে ভাত রান্না হয়।", "Ēkhāne bhāt rānnā hōy."),
            ("The letter was sent.", "চিঠি পাঠানো হয়েছিল।", "Chiṭhi pāṭhānō hōyēchil."),
            ("Work is done by us.", "কাজ আমাদের দ্বারা হয়।", "Kāj āmādēr dwārā hōy."),
        ],
        592: [
            ("The door was opened.", "দরজা খোলা হয়েছিল।", "Dôrjā khōlā hōyēchil."),
            ("It will be finished tomorrow.", "কাল শেষ হবে।", "Kāl shēsh hōbe."),
            ("The song was sung well.", "গানটা ভালো গাওয়া হয়েছে।", "Gānṭā bhālō gāōẏā hōyēchhe."),
        ],
        593: [
            ("I feel cold.", "ঠান্ডা লাগছে।", "Ṭhāṇḍā lāgchhe."),
            ("I think it will rain.", "মনে হয় বৃষ্টি হবে।", "Mōnē hōy briṣṭi hōbe."),
            ("She feels tired.", "সে ক্লান্ত বোধ করছে।", "Sē klānto bōdh korchhe."),
        ],
        594: [
            ("Birds of a feather flock together.", "চোরে চোরে মাসতুতো ভাই।", "Chōre chōre māstutō bhāi."),
            ("Strike while the iron is hot.", "সুযোগ বুঝে কাজ করো।", "Sujōg bujhe kāj kōrō."),
            ("All's well that ends well.", "শেষ ভালো তো সব ভালো।", "Shēsh bhālō tō sôb bhālō."),
        ],
        595: [
            ("Better late than never.", "দেরি হলেও না হওয়ার চেয়ে ভালো।", "Dēri hōleō nā hōẏār cheye bhālō."),
            ("Look before you leap.", "আগে ভাবো তারপর করো।", "Āgē bhābō tārpor kōrō."),
            ("Honesty is the best policy.", "সততাই সেরা নীতি।", "Sôtôtāi sērā nīti."),
        ],
        596: [
            ("If you study, you will pass.", "পড়লে পাস করবে।", "Pōṛlē pās korbe."),
            ("Unless you try, you won't know.", "চেষ্টা না করলে জানবে না।", "Chēṣṭā nā korlē jānbe nā."),
            ("Had I known, I would have come.", "জানলে আসতাম।", "Jānlē āsām."),
        ],
    }
    if cid in _551:
        return _551[cid]
    if cid in themes:
        return themes[cid]
    return [
        (f"Phrase lesson {cid}: pattern one.", f"পাঠ {cid} এর প্রথম ধরন।", f"Pāṭh {cid} er prôthom dhôron."),
        (f"Phrase lesson {cid}: pattern two.", f"পাঠ {cid} এর দ্বিতীয় ধরন।", f"Pāṭh {cid} er dwitīẏo dhôron."),
        (f"Phrase lesson {cid}: pattern three.", f"পাঠ {cid} এর তৃতীয় ধরন।", f"Pāṭh {cid} er tr̥tīẏo dhôron."),
    ]


def grammar_phrase_rows() -> dict[int, list[tuple[str, str, str]]]:
    """532–596: 18 tuples per chapter; fill lines avoid repeating Bengali within grammar/phrase block."""
    seen_bn: set[str] = set()
    out: dict[int, list[tuple[str, str, str]]] = {}
    for cid in range(532, 597):
        lines: list[tuple[str, str, str]] = []
        if cid <= 542:
            lines.extend(_topic_openers_grammar(cid))
        else:
            lines.extend(_topic_openers_phrase(cid))
        for t in lines:
            seen_bn.add(t[1])
        start = (cid - 532) * 18
        gi = start + len(lines)
        guard = 0
        while len(lines) < 18 and guard < 4000:
            cand = _combo_line(gi, "gp")
            if cand[1] not in seen_bn:
                seen_bn.add(cand[1])
                lines.append(cand)
            gi += 1
            guard += 1
        if len(lines) < 18:
            raise RuntimeError(f"Could not fill 18 unique Bengali lines for chapter {cid}")
        out[cid] = lines[:18]
    return out


def extend_conversation_to_18(cid: int, leads: list[tuple[str, str, str]]) -> list[tuple[str, str, str]]:
    """Append practice lines so each conversation lesson has 18 rows; unique Bengali within the lesson."""
    seen_bn = {t[1] for t in leads}
    out = list(leads)
    base_off = 28000 + (cid - 620) * 32
    gi = base_off + len(out)
    guard = 0
    while len(out) < 18 and guard < 6000:
        cand = _combo_line(gi, "cv")
        if cand[1] not in seen_bn:
            seen_bn.add(cand[1])
            out.append(cand)
        gi += 1
        guard += 1
    if len(out) < 18:
        raise RuntimeError(f"Could not fill 18 unique Bengali lines for conversation chapter {cid}")
    return out[:18]


def expand_vocab_pairs(pairs: list[tuple[str, str, str]], target_min: int = 18) -> list[tuple[str, str, str]]:
    """Pad vocabulary word lists to at least target_min rows with extra common words."""
    if len(pairs) >= target_min:
        return pairs
    extra = [
        ("word", "শব্দ", "shôbdô"),
        ("sentence", "বাক্য", "bākya"),
        ("language", "ভাষা", "bhāṣā"),
        ("teacher", "শিক্ষক", "shikkhôk"),
        ("student", "ছাত্র", "chātrô"),
        ("city", "শহর", "shôhor"),
        ("village", "গ্রাম", "grām"),
        ("road", "রাস্তা", "rāstā"),
        ("market", "বাজার", "bājār"),
        ("shop", "দোকান", "dokān"),
        ("price", "দাম", "dām"),
        ("morning", "সকাল", "sākāl"),
        ("evening", "সন্ধ্যা", "sondhyā"),
        ("night", "রাত", "rāt"),
        ("week", "সপ্তাহ", "soptāh"),
        ("month", "মাস", "mās"),
        ("year", "বছর", "bôchhor"),
        ("question", "প্রশ্ন", "prôshno"),
        ("answer", "উত্তর", "uttor"),
        ("please wait", "অনুগ্রহ করে অপেক্ষা করুন", "ônugrôh kôre ôpekhshā kôrun"),
    ]
    out = list(pairs)
    i = 0
    while len(out) < target_min and i < len(extra):
        if extra[i][0] not in [x[0] for x in out]:
            out.append(extra[i])
        i += 1
    return out[:target_min] if target_min else out
