# -*- coding: utf-8 -*-
"""
Hindi vocabulary lessons (597–619): themed word lists + short usage notes.
Standard spoken Hindi; IAST-style romanization.
"""

from __future__ import annotations

from hindi_grammar_chapters import _p, _t


def _l(content: str, intro: str, blocks: list[dict]) -> dict:
    return {"content": content, "intro": intro, "blocks": blocks}


# --- 597–608 ---


def chapter_597() -> dict:
    return _l(
        "Common body-part nouns (singular); many pair with मेरा/मेरी for possession.",
        "Learn the word, then use in short sentences: मेरा सिर दर्द कर रहा है.",
        [
            _p("Tip", "Gender matters for possessives: मेरा हाथ (m.), मेरी आँख (f.)."),
            _t(
                "Body parts",
                [
                    ["head", "सिर", "sir"],
                    ["hair", "बाल", "bāl"],
                    ["face", "चेहरा", "chehrā"],
                    ["eye", "आँख", "ā̃kh"],
                    ["ear", "कान", "kān"],
                    ["nose", "नाक", "nāk"],
                    ["mouth", "मुँह", "mũh"],
                    ["tooth / teeth", "दाँत", "dā̃t"],
                    ["tongue", "जीभ", "jībh"],
                    ["neck", "गला", "galā"],
                    ["shoulder", "कंधा", "kandhā"],
                    ["hand", "हाथ", "hāth"],
                    ["finger", "उँगली", "ũgalī"],
                    ["stomach / belly", "पेट", "peṭ"],
                    ["leg", "टाँग", "tā̃g"],
                    ["foot", "पैर", "pair"],
                ],
            ),
        ],
    )


def chapter_598() -> dict:
    return _l(
        "High-frequency nouns and adjectives for daily talk: things, places, people, time.",
        "Use these in your own mini-sentences to remember them.",
        [
            _p("Mix", "These appear constantly in conversation and reading."),
            _t(
                "Miscellaneous words",
                [
                    ["thing", "चीज़", "cīz"],
                    ["place", "जगह", "jagah"],
                    ["work", "काम", "kām"],
                    ["time", "समय / वक़्त", "samay / vaqt"],
                    ["money", "पैसा", "paisā"],
                    ["water", "पानी", "pānī"],
                    ["food", "खाना", "khānā"],
                    ["house / home", "घर", "ghar"],
                    ["road", "सड़क", "saṛak"],
                    ["city", "शहर", "śahar"],
                    ["shop", "दुकान", "dukān"],
                    ["friend", "दोस्त", "dost"],
                    ["problem", "समस्या", "samasyā"],
                    ["easy", "आसान", "āsān"],
                    ["difficult", "मुश्किल", "muśkil"],
                    ["good", "अच्छा", "acchā"],
                ],
            ),
        ],
    )


def chapter_599() -> dict:
    return _l(
        "Family and relations; जी adds respect: माता जी, पिता जी.",
        "ससुराल — in-laws’ side; मायका — maternal home (common speech).",
        [
            _p("Usage", "Address with relation + जी to elders."),
            _t(
                "Relations",
                [
                    ["father", "पिता / बाप", "pitā / bāp"],
                    ["mother", "माता / माँ", "mātā / mā̃"],
                    ["husband", "पति / शौहर", "pati / śauhar"],
                    ["wife", "पत्नी / बीवी", "patnī / bīvī"],
                    ["son", "बेटा", "beṭā"],
                    ["daughter", "बेटी", "beṭī"],
                    ["brother", "भाई", "bhāī"],
                    ["sister", "बहन", "bahan"],
                    ["elder brother", "भैया / बड़ा भाई", "bhaiyā / baṛā bhāī"],
                    ["younger brother", "छोटा भाई", "choṭā bhāī"],
                    ["uncle (father’s brother)", "चाचा", "cācā"],
                    ["aunt (uncle’s wife)", "चाची", "cācī"],
                    ["maternal uncle", "मामा", "māmā"],
                    ["maternal aunt", "मामी", "māmī"],
                    ["grandfather", "दादा", "dādā"],
                    ["grandmother", "दादी", "dādī"],
                ],
            ),
        ],
    )


def chapter_600() -> dict:
    return _l(
        "Cardinals 0–10 and teens; बीस, तीस for tens up to ninety in speech patterns.",
        "एक, दो, तीन … दस; ग्यारह … उन्नीस.",
        [
            _p("Part 1", "Spell aloud; pair with counting objects: तीन किताबें."),
            _t(
                "Numbers – Part 1",
                [
                    ["zero", "शून्य / ज़ीरो", "śūnya / zīro"],
                    ["one", "एक", "ek"],
                    ["two", "दो", "do"],
                    ["three", "तीन", "tīn"],
                    ["four", "चार", "cār"],
                    ["five", "पाँच", "pā̃c"],
                    ["six", "छह", "chah"],
                    ["seven", "सात", "sāt"],
                    ["eight", "आठ", "āṭh"],
                    ["nine", "नौ", "nau"],
                    ["ten", "दस", "das"],
                    ["eleven", "ग्यारह", "gyārah"],
                    ["twelve", "बारह", "bārah"],
                    ["thirteen", "तेरह", "terah"],
                    ["nineteen", "उन्नीस", "unnīs"],
                    ["twenty", "बीस", "bīs"],
                ],
            ),
        ],
    )


def chapter_601() -> dict:
    return _l(
        "Tens, hundreds, thousands; लाख and करोड़ for large amounts.",
        "Read prices and years: दो हज़ार छब्बीस.",
        [
            _p("Part 2", "Combine: इक्कीस (21), पैंतीस (35), सौ (100)."),
            _t(
                "Numbers – Part 2",
                [
                    ["thirty", "तीस", "tīs"],
                    ["forty", "चालीस", "cālīs"],
                    ["fifty", "पचास", "pacās"],
                    ["sixty", "साठ", "sāṭh"],
                    ["seventy", "सत्तर", "sattar"],
                    ["eighty", "अस्सी", "assī"],
                    ["ninety", "नब्बे", "nabbe"],
                    ["hundred", "सौ", "sau"],
                    ["two hundred", "दो सौ", "do sau"],
                    ["thousand", "हज़ार", "hazār"],
                    ["ten thousand", "दस हज़ार", "das hazār"],
                    ["hundred thousand / lakh", "लाख", "lākh"],
                    ["ten million / crore", "करोड़", "karoṛ"],
                    ["half (adjective)", "आधा", "ādhā"],
                    ["double", "दोगुना", "dogunā"],
                    ["first (ordinal)", "पहला", "pahlā"],
                ],
            ),
        ],
    )


def chapter_602() -> dict:
    return _l(
        "Fractions: आधा, चौथाई; sequence: पहला, दूसरा; percentage: प्रतिशत.",
        "तीन बटे चार — three fourths (in math style).",
        [
            _p("Everyday", "आधा किलो — half a kilo; पचास प्रतिशत — fifty percent."),
            _t(
                "Fractions, sequence, percent",
                [
                    ["half", "आधा", "ādhā"],
                    ["one fourth", "चौथाई", "cauthāī"],
                    ["three fourths", "तीन चौथाई", "tīn cauthāī"],
                    ["one third", "एक तिहाई", "ek tihāī"],
                    ["double", "दोगुना", "dogunā"],
                    ["first", "पहला", "pahlā"],
                    ["second", "दूसरा", "dūsrā"],
                    ["third", "तीसरा", "tīsrā"],
                    ["last", "आख़िरी / अंतिम", "āxirii / antim"],
                    ["next", "अगला", "aglā"],
                    ["previous", "पिछला", "pichlā"],
                    ["percent", "प्रतिशत", "pratiśat"],
                    ["fifty percent", "पचास प्रतिशत", "pacās pratiśat"],
                    ["number in line", "क्रमांक", "kramāṅk"],
                    ["once", "एक बार", "ek bār"],
                    ["twice", "दो बार", "do bār"],
                ],
            ),
        ],
    )


def chapter_603() -> dict:
    return _l(
        "Core verbs for daily actions: movement, basic transitives.",
        "Memorize infinitive + present stem pattern later; here, the citation form.",
        [
            _p("Part 1", "जाना, आना, करना, देना, लेना, खाना, पीना."),
            _t(
                "Verbs – Part 1",
                [
                    ["to go", "जाना", "jānā"],
                    ["to come", "आना", "ānā"],
                    ["to do", "करना", "karnā"],
                    ["to give", "देना", "denā"],
                    ["to take", "लेना", "lenā"],
                    ["to eat", "खाना", "khānā"],
                    ["to drink", "पीना", "pīnā"],
                    ["to sleep", "सोना", "sonā"],
                    ["to wake", "उठना", "uṭhnā"],
                    ["to sit", "बैठना", "baiṭhnā"],
                    ["to stand", "खड़े होना", "khaṛe honā"],
                    ["to walk", "चलना", "calnā"],
                    ["to run", "दौड़ना", "dauṛnā"],
                    ["to see", "देखना", "dekhnā"],
                    ["to hear", "सुनना", "sunnā"],
                    ["to speak", "बोलना", "bolnā"],
                ],
            ),
        ],
    )


def chapter_604() -> dict:
    return _l(
        "Verbs for learning, work, and communication.",
        "Part 2 builds on Part 1 for classroom and office contexts.",
        [
            _p("Part 2", "Use with ने objects where transitive: पढ़ना, लिखना."),
            _t(
                "Verbs – Part 2",
                [
                    ["to read", "पढ़ना", "paṛhnā"],
                    ["to write", "लिखना", "likhnā"],
                    ["to teach", "पढ़ाना", "paṛhānā"],
                    ["to learn", "सीखना", "sīkhnā"],
                    ["to ask", "पूछना", "pūchnā"],
                    ["to answer", "जवाब देना", "javāb denā"],
                    ["to understand", "समझना", "samajhnā"],
                    ["to explain", "समझाना", "samjhānā"],
                    ["to work", "काम करना", "kām karnā"],
                    ["to open", "खोलना", "kholnā"],
                    ["to close", "बंद करना", "band karnā"],
                    ["to buy", "खरीदना", "kharīdnā"],
                    ["to sell", "बेचना", "becnā"],
                    ["to pay", "भुगतान करना", "bhugtān karnā"],
                    ["to wait", "इंतज़ार करना", "intazār karnā"],
                    ["to help", "मदद करना", "madad karnā"],
                ],
            ),
        ],
    )


def chapter_605() -> dict:
    return _l(
        "Verbs of thought, feeling, and change; many pair with को or से.",
        "Part 3 for inner states and social verbs.",
        [
            _p("Part 3", "लगना, चाहिए, पसंद — often with dative experiencer."),
            _t(
                "Verbs – Part 3",
                [
                    ["to think", "सोचना", "socnā"],
                    ["to feel", "महसूस करना", "mahasūs karnā"],
                    ["to like", "पसंद करना", "pasand karnā"],
                    ["to love", "प्यार करना", "pyār karnā"],
                    ["to hate", "नफ़रत करना", "nafrat karnā"],
                    ["to hope", "आशा करना", "āśā karnā"],
                    ["to fear", "डरना", "ḍarnā"],
                    ["to forget", "भूलना", "bhūlnā"],
                    ["to remember", "याद करना", "yād karnā"],
                    ["to try", "कोशिश करना", "kośiś karnā"],
                    ["to begin", "शुरू करना", "śurū karnā"],
                    ["to finish", "खत्म करना", "khatm karnā"],
                    ["to change", "बदलना", "badalnā"],
                    ["to become", "बनना / हो जाना", "bannā / ho jānā"],
                    ["to stay", "रहना", "rahnā"],
                    ["to leave", "जाना / छोड़ना", "jānā / choṛnā"],
                ],
            ),
        ],
    )


def chapter_606() -> dict:
    return _l(
        "Verbs for cleaning, fixing, technology, and travel.",
        "Part 4 rounds out household and modern life.",
        [
            _p("Part 4", "Many are noun + करना: फोन करना."),
            _t(
                "Verbs – Part 4",
                [
                    ["to clean", "साफ़ करना", "sāf karnā"],
                    ["to wash", "धोना", "dhonā"],
                    ["to cook", "खाना बनाना", "khānā banānā"],
                    ["to cut", "काटना", "kāṭnā"],
                    ["to break", "तोड़ना", "toṛnā"],
                    ["to fix / repair", "ठीक करना", "ṭhīk karnā"],
                    ["to send", "भेजना", "bhejna"],
                    ["to receive", "पाना / मिलना", "pānā / milnā"],
                    ["to call (phone)", "फोन करना", "phon karnā"],
                    ["to message", "मैसेज करना", "meśej karnā"],
                    ["to search", "ढूँढना", "ḍhū̃ḍhnā"],
                    ["to drive", "गाड़ी चलाना", "gāṛī calānā"],
                    ["to ride", "सवारी करना", "savārī karnā"],
                    ["to fly", "उड़ना", "uṛnā"],
                    ["to swim", "तैरना", "tairnā"],
                    ["to meet", "मिलना", "milnā"],
                ],
            ),
        ],
    )


def chapter_607() -> dict:
    return _l(
        "Hindi लाना ‘to bring’ and देना ‘to give’ — many compounds and senses (cf. Magahi/Maithili लावब / देब).",
        "लाना: physical bring + metaphorical ‘produce’; देना: give + permit + light-verb completion.",
        [
            _p("लाना", "लाना, ले आना — e.g. पैसा लाओ, किताब ले आओ (bring money, bring the book)."),
            _p("देना", "दे देना finish; बता देना tell; मार देना strike (idiomatic)."),
            _t(
                "लाना / देना — multiple meanings",
                [
                    ["bring (here)", "लाना", "lānā"],
                    ["bring along", "साथ लाना", "sāth lānā"],
                    ["fetch", "ला देना", "lā denā"],
                    ["give", "देना", "denā"],
                    ["give away", "दे देना / बाँट देना", "de denā / bā̃ṭ denā"],
                    ["tell / inform", "बता देना", "batā denā"],
                    ["hand over", "सौंप देना", "sauṃp denā"],
                    ["grant permission", "अनुमति देना", "anumati denā"],
                    ["give a scolding", "डाँट देना", "ḍā̃ṭ denā"],
                    ["give trouble", "परेशानी देना", "pareśānī denā"],
                    ["add (completion)", "कर देना", "kar denā"],
                    ["I brought sweets", "मैं मिठाई लाया", "main miṭhāī lāyā"],
                    ["Give me water", "मुझे पानी दो", "mujhe pānī do"],
                    ["He gave his word", "उसने वचन दिया", "usne vacan diyā"],
                    ["Bring the file tomorrow", "कल फ़ाइल लाना", "kal phāil lānā"],
                ],
            ),
        ],
    )


def chapter_608() -> dict:
    return _l(
        "Hindi लगना — many senses: attach, suit, feel, seem, cost (cf. Magahi/Maithili लागब).",
        "Experiencer often dative: मुझे ठंड लग रही है.",
        [
            _p("Common frames", "लगना + को: time/schedule; लगना + पर: blame; लगना + की: seem."),
            _t(
                "लगना — multiple meanings",
                [
                    ["to be attached / stick", "लगना", "lagnā"],
                    ["to feel (cold, fear)", "लगना", "lagnā"],
                    ["to seem / appear", "लगना", "lagnā"],
                    ["to suit (clothes)", "अच्छा लगना", "acchā lagnā"],
                    ["to cost", "लगना", "lagnā"],
                    ["to begin (intrans.)", "लगना", "lagnā"],
                    ["I feel cold", "मुझे ठंड लग रही है", "mujhe thaṃḍ lag rahī hai"],
                    ["It seems good", "अच्छा लगता है", "acchā lagtā hai"],
                    ["This shirt suits you", "यह शर्ट आप पर अच्छी लगेगी", "yah śarṭ āpar acchī lagegī"],
                    ["How much did it cost?", "कितने का लगा?", "kitne kā lagā?"],
                    ["The movie started", "फ़िल्म लग गई", "film lag gaī"],
                    ["I am allergic (it affects me)", "मुझे एलर्जी लगती है", "mujhe elarjī lagtī hai"],
                    ["He got blamed", "उस पर दोष लगा", "us par doṣ lagā"],
                    ["I miss home", "मुझे घर की याद लग रही है", "mujhe ghar kī yād lag rahī hai"],
                    ["Namesake / relation", "नाम लगना", "nām lagnā"],
                    ["It doesn’t fit", "यह फिट नहीं लग रहा", "yah phiṭ nahī̃ lag rahā"],
                ],
            ),
        ],
    )


# --- 609–619 ---


def chapter_609() -> dict:
    return _l(
        "Common adjectives for size, quality, age, and judgment.",
        "Agree with noun: बड़ा लड़का, बड़ी लड़की.",
        [
            _p("Part 1", "नया/पुराना, अच्छा/बुरा — opposites in daily speech."),
            _t(
                "Adjectives – Part 1",
                [
                    ["big", "बड़ा", "baṛā"],
                    ["small", "छोटा", "choṭā"],
                    ["long", "लंबा", "laṃbā"],
                    ["short", "छोटा / नाटा", "choṭā / nāṭā"],
                    ["tall", "लंबा", "laṃbā"],
                    ["wide", "चौड़ा", "cauṛā"],
                    ["narrow", "पतला", "patlā"],
                    ["heavy", "भारी", "bhārī"],
                    ["light (weight)", "हल्का", "halkā"],
                    ["new", "नया", "nayā"],
                    ["old (thing)", "पुराना", "purānā"],
                    ["good", "अच्छा", "acchā"],
                    ["bad", "बुरा", "burā"],
                    ["beautiful", "सुंदर", "sundar"],
                    ["clean", "साफ़", "sāf"],
                    ["dirty", "गंदा", "gandā"],
                ],
            ),
        ],
    )


def chapter_610() -> dict:
    return _l(
        "Adverbs of manner: how something happens — धीरे, जल्दी, अचानक.",
        "Often end in -े when modifying verbs: धीरे बोलो.",
        [
            _p("Part 1", "Place मैं/यहाँ; time अभी/कल with verbs."),
            _t(
                "Adverbs – Part 1",
                [
                    ["slowly", "धीरे", "dhīre"],
                    ["quickly", "जल्दी / तेज़ी से", "jaldī / tezī se"],
                    ["suddenly", "अचानक", "acānak"],
                    ["carefully", "ध्यान से", "dhyān se"],
                    ["together", "साथ में", "sāth mẽ"],
                    ["alone", "अकेले", "akele"],
                    ["maybe", "शायद", "śāyad"],
                    ["certainly", "निश्चित रूप से", "niścit rūp se"],
                    ["always", "हमेशा", "hameśā"],
                    ["often", "अक्सर", "aksar"],
                    ["sometimes", "कभी-कभी", "kabhī-kabhī"],
                    ["never", "कभी नहीं", "kabhī nahī̃"],
                    ["today", "आज", "āj"],
                    ["tomorrow", "कल", "kal"],
                    ["yesterday", "कल", "kal"],
                    ["now", "अभी", "abhī"],
                ],
            ),
        ],
    )


def chapter_611() -> dict:
    return _l(
        "More adverbs: degree, frequency, doubt, and sentence adverbs.",
        "बहुत, बिल्कुल, वाकई — intensity and emphasis.",
        [
            _p("List", "Stack after verb or before adjective: बहुत अच्छा."),
            _t(
                "Adverbs (broader list)",
                [
                    ["very", "बहुत", "bahut"],
                    ["too (much)", "बहुत ज़्यादा", "bahut zyādā"],
                    ["quite", "काफ़ी", "kāfī"],
                    ["completely", "पूरी तरह", "pūrī tarah"],
                    ["almost", "लगभग", "lagbhag"],
                    ["only", "केवल / सिर्फ़", "keval / sirf"],
                    ["also", "भी", "bhī"],
                    ["even", "भी / तक", "bhī / tak"],
                    ["perhaps", "शायद", "śāyad"],
                    ["definitely", "ज़रूर", "zarūr"],
                    ["probably", "शायद", "śāyad"],
                    ["really", "सच में / वाकई", "sac mẽ / vākai"],
                    ["anyway", "वैसे भी", "vaise bhī"],
                    ["instead", "इसके बजाय", "iske bajāy"],
                    ["therefore", "इसलिए", "islie"],
                    ["however", "हालाँकि", "hālãki"],
                ],
            ),
        ],
    )


def chapter_612() -> dict:
    return _l(
        "Common vegetables on the plate and in the market.",
        "Gender varies: आलू (m.), भिंडी (f.); learn with measure: एक किलो टमाटर.",
        [
            _p("Cooking", "प्याज़, लहसुन, अदरक — base of many curries."),
            _t(
                "Vegetables",
                [
                    ["potato", "आलू", "ālū"],
                    ["onion", "प्याज़", "pyāz"],
                    ["tomato", "टमाटर", "ṭamāṭar"],
                    ["carrot", "गाजर", "gājar"],
                    ["cauliflower", "फूलगोभी", "phūlgobhī"],
                    ["cabbage", "पत्ता गोभी", "pattā gobhī"],
                    ["okra", "भिंडी", "bhiṃḍī"],
                    ["eggplant", "बैंगन", "baiṅgan"],
                    ["spinach", "पालक", "pālak"],
                    ["peas", "मटर", "maṭar"],
                    ["beans", "बीन्स / सेम", "bīns / sem"],
                    ["pumpkin", "कद्दू", "kaddū"],
                    ["bottle gourd", "लौकी", "laukī"],
                    ["radish", "मूली", "mūlī"],
                    ["chilli", "मिर्च", "mirc"],
                    ["garlic", "लहसुन", "lahsun"],
                ],
            ),
        ],
    )


def chapter_613() -> dict:
    return _l(
        "Fruit names; many loanwords are common in Hindi markets.",
        "सेब, केला — everyday; अनार, संतरा — seasonal favorites.",
        [
            _p("Note", "केला is banana; नारियल is coconut."),
            _t(
                "Fruits",
                [
                    ["mango", "आम", "ām"],
                    ["banana", "केला", "kelā"],
                    ["apple", "सेब", "seb"],
                    ["orange", "संतरा", "santarā"],
                    ["grapes", "अंगूर", "aṅgūr"],
                    ["pomegranate", "अनार", "anār"],
                    ["guava", "अमरूद", "amrūd"],
                    ["papaya", "पपीता", "papītā"],
                    ["watermelon", "तरबूज़", "tarbūz"],
                    ["muskmelon", "खरबूज़", "kharbūz"],
                    ["coconut", "नारियल", "nāriyal"],
                    ["lemon", "नींबू", "nī̃bū"],
                    ["sweet lime", "मौसम्बी", "mausambī"],
                    ["pear", "नाशपाती", "nāśpātī"],
                    ["plum / berry (context)", "बेर", "ber"],
                    ["strawberry", "स्ट्रॉबेरी", "sṭrŏberī"],
                ],
            ),
        ],
    )


def chapter_614() -> dict:
    return _l(
        "Common birds; some names are onomatopoeic or descriptive.",
        "कोयल — cuckoo; उल्लू — owl (also slang ‘fool’ in jokes).",
        [
            _p("Culture", "मोर is India’s national bird (peacock)."),
            _t(
                "Birds",
                [
                    ["crow", "कौवा", "kauvā"],
                    ["sparrow", "गौरैया", "gauraiyā"],
                    ["parrot", "तोता", "totā"],
                    ["peacock", "मोर", "mor"],
                    ["pigeon", "कबूतर", "kabūtar"],
                    ["eagle", "बाज़", "bāz"],
                    ["owl", "उल्लू", "ullū"],
                    ["duck", "बतख़", "batax"],
                    ["hen / chicken", "मुर्गी", "murgī"],
                    ["cuckoo", "कोयल", "koyal"],
                    ["swan", "हंस", "haṃs"],
                    ["crane (bird)", "सारस", "sāras"],
                    ["woodpecker", "कठफोड़वा", "kaṭphoṛavā"],
                    ["myna", "मैना", "mainā"],
                    ["bat (animal)", "चमगादड़", "camgādaṛ"],
                    ["kite (bird)", "चील", "cīl"],
                ],
            ),
        ],
    )


def chapter_615() -> dict:
    return _l(
        "Insects and small creatures; household pests and nature.",
        "Careful: कुछ जहरीले हो सकते हैं — some can be poisonous.",
        [
            _p("Home", "मक्खी, मच्छर — very common complaints."),
            _t(
                "Insects",
                [
                    ["ant", "चींटी", "cī̃ṭī"],
                    ["fly", "मक्खी", "makkī"],
                    ["mosquito", "मच्छर", "macchar"],
                    ["bee", "मधुमक्खी", "madhumakkī"],
                    ["butterfly", "तितली", "titlī"],
                    ["spider", "मकड़ी", "makaṛī"],
                    ["cockroach", "तिलचट्टा", "tilcaṭṭā"],
                    ["termite", "दीमक", "dīmak"],
                    ["beetle", "भृंग", "bhṛṅg"],
                    ["grasshopper", "टिड्डा", "ṭiḍḍā"],
                    ["worm", "कीड़ा", "kīṛā"],
                    ["louse", "जूँ", "jū̃"],
                    ["bedbug", "खटमल", "khaṭmal"],
                    ["firefly", "जुगनू", "juganū"],
                    ["dragonfly", "ड्रैगनफ्लाई", "ḍraignaflāī"],
                    ["caterpillar", "इल्ली", "illī"],
                ],
            ),
        ],
    )


def chapter_616() -> dict:
    return _l(
        "Basic colour words; combine with चमड़ा, कपड़ा: लाल रंग.",
        "गुलाबी, नारंगी — colours as adjectives before nouns.",
        [
            _p("Agreement", "लाल सेब, लाल किताबें — colour adjective often invariant in casual speech."),
            _t(
                "Colours",
                [
                    ["red", "लाल", "lāl"],
                    ["blue", "नीला", "nīlā"],
                    ["green", "हरा", "harā"],
                    ["yellow", "पीला", "pīlā"],
                    ["white", "सफ़ेद", "safed"],
                    ["black", "काला", "kālā"],
                    ["brown", "भूरा", "bhūrā"],
                    ["orange (colour)", "नारंगी", "nāraṅgī"],
                    ["pink", "गुलाबी", "gulābī"],
                    ["purple", "बैंगनी", "baiṅgnī"],
                    ["grey", "स्लेटी / धूसर", "slēṭī / dhūsar"],
                    ["golden", "सुनहरा", "sunaharā"],
                    ["silver", "चाँदी जैसा", "cā̃dī jaise"],
                    ["dark", "गहरा", "gahrā"],
                    ["light (shade)", "हल्का", "halkā"],
                    ["colour (noun)", "रंग", "raṅg"],
                ],
            ),
        ],
    )


def chapter_617() -> dict:
    return _l(
        "Flower names for gardens, worship, and festivals.",
        "गुलाब — rose; गेंदा — marigold (common in garlands).",
        [
            _p("Festivals", "फूलों की माला — flower garland."),
            _t(
                "Flowers",
                [
                    ["rose", "गुलाब", "gulāb"],
                    ["lotus", "कमल", "kamal"],
                    ["marigold", "गेंदा", "geṃdā"],
                    ["jasmine", "चमेली", "camelī"],
                    ["sunflower", "सूरजमुखी", "sūrajmukhī"],
                    ["hibiscus", "गुड़हल", "guṛhal"],
                    ["chrysanthemum", "गुलदाउदी", "guldaudī"],
                    ["lily", "कुमुदिनी", "kumudinī"],
                    ["tulip", "ट्यूलिप", "ṭyūlip"],
                    ["orchid", "आर्किड", "ārkiḍ"],
                    ["lavender (loan)", "लैवेंडर", "laiveṃḍar"],
                    ["daisy", "गुलबहार", "gulbahār"],
                    ["mogra (jasmine type)", "मोगरा", "mogrā"],
                    ["raat ki rani", "रात की रानी", "rāt kī rānī"],
                    ["bougainvillea", "बोगनविलिया", "boganviliyā"],
                    ["flower (general)", "फूल", "phūl"],
                ],
            ),
        ],
    )


def chapter_618() -> dict:
    return _l(
        "Common wild and domestic animals.",
        "भालू — bear; शेर — lion/tiger context in stories.",
        [
            _p("Farm", "गाय, भैंस, बकरी — milk animals."),
            _t(
                "Animals",
                [
                    ["dog", "कुत्ता", "kuttā"],
                    ["cat", "बिल्ली", "billī"],
                    ["cow", "गाय", "gāy"],
                    ["buffalo", "भैंस", "bhaiṃs"],
                    ["goat", "बकरी", "bakrī"],
                    ["horse", "घोड़ा", "ghoṛā"],
                    ["elephant", "हाथी", "hāthī"],
                    ["lion", "शेर", "śer"],
                    ["tiger", "बाघ", "bāgh"],
                    ["bear", "भालू", "bhālū"],
                    ["monkey", "बंदर", "bandar"],
                    ["rabbit", "खरगोश", "khargoś"],
                    ["deer", "हिरण", "hiraṇ"],
                    ["camel", "ऊँट", "ū̃ṭ"],
                    ["sheep", "भेड़", "bheṛ"],
                    ["donkey", "गधा", "gadhā"],
                ],
            ),
        ],
    )


def chapter_619() -> dict:
    return _l(
        "Extra high-frequency words: fillers, reactions, and handy nouns.",
        "Use with care: अच्छा as ‘okay/I see’ is extremely common.",
        [
            _p("Misc", "ठीक है, बस, वैसे — conversation glue."),
            _t(
                "Common words (misc.)",
                [
                    ["okay / I see", "अच्छा", "acchā"],
                    ["fine / alright", "ठीक है", "ṭhīk hai"],
                    ["enough", "बस", "bas"],
                    ["well / so", "तो", "to"],
                    ["by the way", "वैसे", "vaise"],
                    ["actually", "असल में", "asal mẽ"],
                    ["maybe", "शायद", "śāyad"],
                    ["again", "फिर", "phir"],
                    ["still", "अभी भी", "abhī bhī"],
                    ["already", "पहले ही", "pahle hī"],
                    ["together", "साथ", "sāth"],
                    ["alone", "अकेला", "akelā"],
                    ["everyone", "सब लोग", "sab log"],
                    ["someone", "कोई", "koī"],
                    ["something", "कुछ", "kuch"],
                    ["nothing", "कुछ नहीं", "kuch nahī̃"],
                ],
            ),
        ],
    )


_VOCAB = {
    597: chapter_597,
    598: chapter_598,
    599: chapter_599,
    600: chapter_600,
    601: chapter_601,
    602: chapter_602,
    603: chapter_603,
    604: chapter_604,
    605: chapter_605,
    606: chapter_606,
    607: chapter_607,
    608: chapter_608,
    609: chapter_609,
    610: chapter_610,
    611: chapter_611,
    612: chapter_612,
    613: chapter_613,
    614: chapter_614,
    615: chapter_615,
    616: chapter_616,
    617: chapter_617,
    618: chapter_618,
    619: chapter_619,
}


def get_vocabulary_chapter(chapter_id: int) -> dict | None:
    fn = _VOCAB.get(chapter_id)
    return fn() if fn else None
