# -*- coding: utf-8 -*-
"""
Rich Hindi grammar lessons (510–542): paragraphs + example tables (Maithili-style blocks).
Standard spoken Hindi; IAST-style romanization.
"""

from __future__ import annotations

HDR = ["English", "Hindi", "Transliteration"]


def _p(heading: str, content: str) -> dict:
    return {"type": "paragraph", "heading": heading, "content": content}


def _t(heading: str, rows: list[list[str]]) -> dict:
    return {
        "type": "table",
        "heading": heading,
        "headers": HDR,
        "speakCol": 1,
        "rows": rows,
    }


def _lesson(content: str, intro: str, blocks: list[dict]) -> dict:
    return {"content": content, "intro": intro, "blocks": blocks}


# --- 510–519 ---


def chapter_510() -> dict:
    return _lesson(
        "Personal pronouns (मैं, हम, तुम, आप, वह, वे) and demonstratives (यह, वह); no indefinite article.",
        "आप is polite 'you'; तुम is informal. यह/वह agree with what you point at.",
        [
            _p("Quick guide", "Verbs agree with the subject in gender and number. Use आप + plural verb forms for respect."),
            _t(
                "Pronouns (subject)",
                [
                    ["I", "मैं", "main"],
                    ["we", "हम", "ham"],
                    ["you (informal)", "तुम", "tum"],
                    ["you (polite)", "आप", "āp"],
                    ["he / she / it", "वह", "vah"],
                    ["they", "वे", "ve"],
                    ["this", "यह", "yah"],
                    ["that", "वह / वो", "vah / vo"],
                    ["my (m. object)", "मेरा", "merā"],
                    ["my (f.)", "मेरी", "merī"],
                    ["our", "हमारा", "hamārā"],
                    ["your (polite)", "आपका", "āpkā"],
                    ["his / her", "उसका", "uskā"],
                    ["their", "उनका", "unkā"],
                    ["I am a student", "मैं छात्र हूँ", "main chātra hū̃"],
                    ["We are ready", "हम तैयार हैं", "ham taiyār haiṃ"],
                    ["You (polite) are kind", "आप दयालु हैं", "āp dayālu haiṃ"],
                    ["This is my book", "यह मेरी किताब है", "yah merī kitāb hai"],
                    ["That is his house", "वह उसका घर है", "vah uskā ghar hai"],
                ],
            ),
        ],
    )


def chapter_511() -> dict:
    return _lesson(
        "Plural verb forms and plural pronouns (आप लोग, वे लोग) often mark respect, even when speaking to one person.",
        "In Hindi, honorific address may use plural agreement: आप कहाँ जा रहे हैं?",
        [
            _p("Respect pattern", "Use आप with plural auxiliary: हैं, करते हैं, जा रहे हैं — not *आप है."),
            _t(
                "Respectful / plural-style sentences",
                [
                    ["How are you all?", "आप सब कैसे हैं?", "āp sab kaise haiṃ?"],
                    ["Please sit", "कृपया बैठिए", "kripayā baithie"],
                    ["You are welcome", "आपका स्वागत है", "āpkā svāgat hai"],
                    ["What do you need?", "आपको क्या चाहिए?", "āpko kyā cāhie?"],
                    ["We respect teachers", "हम शिक्षकों का सम्मान करते हैं", "ham śikṣkõ kā sammān karte haiṃ"],
                    ["They are elders", "वे बुज़ुर्ग हैं", "ve buzurg haiṃ"],
                    ["Greetings to everyone", "सभी को नमस्ते", "sabhī ko namaste"],
                    ["Your health is important", "आपका स्वास्थ्य महत्वपूर्ण है", "āpkā svāsthya mahatvpūrṇ hai"],
                    ["May I help you?", "क्या मैं आपकी मदद कर सकता हूँ?", "kyā main āpkī madad kar saktā hū̃?"],
                    ["Please come in", "कृपया अंदर आइए", "kripayā andar āie"],
                    ["Have tea", "चाय लीजिए", "cāy lījie"],
                    ["Thank you, sir", "धन्यवाद, सर", "dhanyavād, sar"],
                    ["We wish you well", "हम आपकी भलाई चाहते हैं", "ham āpkī bhalāī cāhte haiṃ"],
                    ["Your children study well", "आपके बच्चे अच्छा पढ़ते हैं", "āp ke bacche acchā paṛhte haiṃ"],
                    ["Everyone may go", "सब जा सकते हैं", "sab jā sakte haiṃ"],
                    ["Speak politely", "विनम्रता से बोलिए", "vinamratā se bolie"],
                ],
            ),
        ],
    )


def chapter_512() -> dict:
    return _lesson(
        "Hindi verbs often end in -ना (infinitive): जाना, करना, खाना. Stem + tense endings carry agreement.",
        "Learn common roots first; tense markers (ता, रहा, गया) attach to the stem.",
        [
            _p("Infinitives", "Use करना 'to do', जाना 'to go', देखना 'to see', खाना 'to eat', पीना 'to drink', पढ़ना 'to read', सोना 'to sleep'."),
            _t(
                "Infinitives and short sentences",
                [
                    ["to go", "जाना", "jānā"],
                    ["to come", "आना", "ānā"],
                    ["to do", "करना", "karnā"],
                    ["to eat", "खाना", "khānā"],
                    ["to drink", "पीना", "pīnā"],
                    ["to read", "पढ़ना", "paṛhnā"],
                    ["to write", "लिखना", "likhnā"],
                    ["to speak", "बोलना", "bolnā"],
                    ["to listen", "सुनना", "sunnā"],
                    ["to see", "देखना", "dekhnā"],
                    ["to give", "देना", "denā"],
                    ["to take", "लेना", "lenā"],
                    ["I want to eat", "मुझे खाना है", "mujhe khānā hai"],
                    ["We have to go", "हमें जाना है", "hameṃ jānā hai"],
                    ["She likes to sing", "उसे गाना पसंद है", "use gānā pasand hai"],
                    ["They know how to swim", "उन्हें तैरना आता है", "unheṃ tairnā ātā hai"],
                    ["He forgot to call", "उसे फोन करना भूल गया", "use phon karnā bhūl gayā"],
                ],
            ),
        ],
    )


def chapter_513() -> dict:
    return _lesson(
        "Simple present for habits and facts: stem + ता/ती/ते + है/हैं (and हूँ for मैं).",
        "मैं जाता हूँ (m.), मैं जाती हूँ (f.); हम करते हैं; वह पढ़ता है / पढ़ती है.",
        [
            _p("Pattern", "Subject + verb stem + ता/ती/ते + है/हैं/हूँ according to gender and person."),
            _t(
                "Habitual present",
                [
                    ["I go to school", "मैं स्कूल जाता हूँ", "main skūl jātā hū̃"],
                    ["She reads the news", "वह समाचार पढ़ती है", "vah samācār paṛhtī hai"],
                    ["We speak Hindi", "हम हिन्दी बोलते हैं", "ham hindī bolte haiṃ"],
                    ["He plays cricket", "वह क्रिकेट खेलता है", "vah krikeṭ kheltā hai"],
                    ["They live in Delhi", "वे दिल्ली में रहते हैं", "ve dillī mẽ rahte haiṃ"],
                    ["I drink tea", "मैं चाय पीता हूँ", "main cāy pītā hū̃"],
                    ["You work here", "आप यहाँ काम करते हैं", "āp yahā̃ kām karte haiṃ"],
                    ["Birds fly", "पक्षी उड़ते हैं", "pakṣī uṛte haiṃ"],
                    ["The sun rises", "सूरज उगता है", "sūraj ugtā hai"],
                    ["I know this", "मैं यह जानता हूँ", "main yah jāntā hū̃"],
                    ["Children play", "बच्चे खेलते हैं", "bacce khelte haiṃ"],
                    ["It rains in July", "जुलाई में बारिश होती है", "julāī mẽ bāriś hotī hai"],
                    ["We help people", "हम लोगों की मदद करते हैं", "ham logõ kī madad karte haiṃ"],
                    ["She teaches Hindi", "वह हिन्दी पढ़ाती है", "vah hindī paṛhātī hai"],
                    ["I like music", "मुझे संगीत पसंद है", "mujhe saṅgīt pasand hai"],
                    ["He drives carefully", "वह सावधानी से गाड़ी चलाता है", "vah sāvdhānī se gāṛī calātā hai"],
                ],
            ),
        ],
    )


def chapter_514() -> dict:
    return _lesson(
        "Copula होना 'to be': है, हैं, हूँ, हो; negative नहीं है.",
        "मैं छात्र हूँ; तुम हो; वह है; वे हैं; यह किताब है.",
        [
            _p("Forms", "हूँ (1sg), हो (2sg informal), है (3sg), हैं (2 polite & plural, 3pl); past: था थी थे थीं."),
            _t(
                "Present 'to be'",
                [
                    ["I am ready", "मैं तैयार हूँ", "main taiyār hū̃"],
                    ["You are here (तुम)", "तुम यहाँ हो", "tum yahā̃ ho"],
                    ["You are kind (आप)", "आप दयालु हैं", "āp dayālu haiṃ"],
                    ["He is a doctor", "वह डॉक्टर है", "vah ḍokṭar hai"],
                    ["She is a teacher", "वह शिक्षिका है", "vah śikṣikā hai"],
                    ["We are friends", "हम दोस्त हैं", "ham dost haiṃ"],
                    ["They are students", "वे छात्र हैं", "ve chātra haiṃ"],
                    ["This is true", "यह सच है", "yah sac hai"],
                    ["That is false", "वह झूठ है", "vah jhūṭh hai"],
                    ["It is cold", "ठंड है", "thaṃḍ hai"],
                    ["There is time", "समय है", "samay hai"],
                    ["I am not tired", "मैं थका नहीं हूँ", "main thakā nahī̃ hū̃"],
                    ["This is not mine", "यह मेरा नहीं है", "yah merā nahī̃ hai"],
                    ["Are you sure?", "क्या आप निश्चित हैं?", "kyā āp niścit haiṃ?"],
                    ["We are Indians", "हम भारतीय हैं", "ham bhāratīy haiṃ"],
                    ["The keys are here", "चाबियाँ यहाँ हैं", "cābiyā̃ yahā̃ haiṃ"],
                ],
            ),
        ],
    )


def chapter_515() -> dict:
    return _lesson(
        "Ongoing action: stem + रहा / रही / रहे + है / हैं / हूँ.",
        "मैं पढ़ रहा हूँ; वे खेल रहे हैं; बारिश हो रही है.",
        [
            _p("Pattern", "रह + gender ending + auxiliary for progressive aspect."),
            _t(
                "Present continuous",
                [
                    ["I am reading", "मैं पढ़ रहा हूँ", "main paṛh rahā hū̃"],
                    ["She is cooking", "वह खाना बना रही है", "vah khānā banā rahī hai"],
                    ["They are playing", "वे खेल रहे हैं", "ve khel rahe haiṃ"],
                    ["We are waiting", "हम इंतज़ार कर रहे हैं", "ham intazār kar rahe haiṃ"],
                    ["He is driving", "वह गाड़ी चला रहा है", "vah gāṛī calā rahā hai"],
                    ["It is raining", "बारिश हो रही है", "bāriś ho rahī hai"],
                    ["I am learning Hindi", "मैं हिन्दी सीख रहा हूँ", "main hindī sīkh rahā hū̃"],
                    ["Are you coming?", "क्या आप आ रहे हैं?", "kyā āp ā rahe haiṃ?"],
                    ["The train is arriving", "ट्रेन आ रही है", "ṭren ā rahī hai"],
                    ["Who is calling?", "कौन फोन कर रहा है?", "kaun phon kar rahā hai?"],
                    ["Children are studying", "बच्चे पढ़ रहे हैं", "bacce paṛh rahe haiṃ"],
                    ["I am writing", "मैं लिख रहा हूँ", "main likh rahā hū̃"],
                    ["She is singing", "वह गा रही है", "vah gā rahī hai"],
                    ["We are talking", "हम बात कर रहे हैं", "ham bāt kar rahe haiṃ"],
                    ["Sun is setting", "सूरज डूब रहा है", "sūraj ḍūb rahā hai"],
                    ["I am not sleeping", "मैं सो नहीं रहा", "main so nahī̃ rahā"],
                ],
            ),
        ],
    )


def chapter_516() -> dict:
    return _lesson(
        "Future: गा / गी / गे with होगा / होगी / होगे — or simple future with -एगा / -एगी / -एगे on stem.",
        "मैं जाऊँगा; वह आएगी; हम करेंगे.",
        [
            _p("Common future", "Spoken Hindi often uses -गा series: मैं खाऊँगा, तुम जाओगे, वह लिखेगी."),
            _t(
                "Simple future",
                [
                    ["I will go", "मैं जाऊँगा", "main jāū̃gā"],
                    ["We will come", "हम आएँगे", "ham āeṅge"],
                    ["She will call", "वह फोन करेगी", "vah phon karegī"],
                    ["They will return", "वे लौटेंगे", "ve lauṭeṅge"],
                    ["It will rain tomorrow", "कल बारिश होगी", "kal bāriś hogī"],
                    ["I will study", "मैं पढ़ूँगा", "main paṛhū̃gā"],
                    ["You will succeed", "आप सफल होंगे", "āp saphal hoṅge"],
                    ["He will pay", "वह भुगतान करेगा", "vah bhugtān karegā"],
                    ["We will meet soon", "हम जल्द मिलेंगे", "ham jald mileṅge"],
                    ["I will not leave", "मैं नहीं जाऊँगा", "main nahī̃ jāū̃gā"],
                    ["Will you help?", "क्या आप मदद करेंगे?", "kyā āp madad kareṅge?"],
                    ["She will sing", "वह गाएगी", "vah gāegī"],
                    ["They will agree", "वे सहमत होंगे", "ve sahamat hoṅge"],
                    ["He will arrive late", "वह देर से आएगा", "vah der se āegā"],
                    ["We will win", "हम जीतेंगे", "ham jīteṅge"],
                    ["Everything will be fine", "सब ठीक होगा", "sab ṭhīk hogā"],
                ],
            ),
        ],
    )


def chapter_517() -> dict:
    return _lesson(
        "Future progressive: रहा होगा / रही होगी / रहे होंगे — action will be in progress.",
        "तब तक मैं पढ़ रहा होऊँगा — by then I will be studying.",
        [
            _p("Usage", "Often for arrangements or predicted ongoing states at a future time."),
            _t(
                "Future continuous",
                [
                    ["I will be working", "मैं काम कर रहा होऊँगा", "main kām kar rahā hoū̃gā"],
                    ["She will be traveling", "वह यात्रा कर रही होगी", "vah yātrā kar rahī hogī"],
                    ["They will be waiting", "वे इंतज़ार कर रहे होंगे", "ve intazār kar rahe hoṅge"],
                    ["We will be eating", "हम खा रहे होंगे", "ham khā rahe hoṅge"],
                    ["He will be sleeping", "वह सो रहा होगा", "vah so rahā hogā"],
                    ["It will be raining", "बारिश हो रही होगी", "bāriś ho rahī hogī"],
                    ["By evening I will be free", "शाम तक मैं फुरसत में होऊँगा", "śām tak main fursat mẽ hoū̃gā"],
                    ["Tomorrow this time I will be flying", "कल इस समय मैं उड़ रहा होऊँगा", "kal is samay main uṛ rahā hoū̃gā"],
                    ["Kids will be playing", "बच्चे खेल रहे होंगे", "bacce khel rahe hoṅge"],
                    ["She will be teaching", "वह पढ़ा रही होगी", "vah paṛhā rahī hogī"],
                    ["We will be watching", "हम देख रहे होंगे", "ham dekh rahe hoṅge"],
                    ["Train will be leaving", "ट्रेन चल रही होगी", "ṭren cal rahī hogī"],
                    ["I will be calling you", "मैं आपको फोन कर रहा होऊँगा", "main āpko phon kar rahā hoū̃gā"],
                    ["They will be building", "वे बना रहे होंगे", "ve banā rahe hoṅge"],
                    ["He will be fixing it", "वह ठीक कर रहा होगा", "vah ṭhīk kar rahā hogā"],
                    ["Sun will be rising", "सूरज उग रहा होगा", "sūraj ug rahā hogā"],
                ],
            ),
        ],
    )


def chapter_518() -> dict:
    return _lesson(
        "Past intransitive / without explicit object: गया / गई / गए + agreement; sometimes simple past stem.",
        "मैं गया; वह आई; हम सो गए.",
        [
            _p("Part 1", "Many verbs use perfective participle + auxiliary in past narrative: चला गया, आ गई."),
            _t(
                "Past (no direct object focus)",
                [
                    ["I went yesterday", "मैं कल गया", "main kal gayā"],
                    ["She came late", "वह देर से आई", "vah der se āī"],
                    ["We slept early", "हम जल्दी सो गए", "ham jaldī so ga.e"],
                    ["He fell", "वह गिर गया", "vah gir gayā"],
                    ["They ran", "वे दौड़े", "ve dauṛe"],
                    ["I woke up", "मैं उठ गया", "main uṭh gayā"],
                    ["Birds flew away", "पक्षी उड़ गए", "pakṣī uṛ ga.e"],
                    ["It rained", "बारिश हुई", "bāriś huī"],
                    ["We arrived", "हम पहुँचे", "ham pahuṃce"],
                    ["She smiled", "वह मुस्कुराई", "vah muskurāī"],
                    ["I forgot", "मैं भूल गया", "main bhūl gayā"],
                    ["He stood up", "वह खड़ा हो गया", "vah khaṛā ho gayā"],
                    ["We laughed", "हम हँसे", "ham hãse"],
                    ["Sun rose", "सूरज उगा", "sūraj ugā"],
                    ["Night fell", "रात हो गई", "rāt ho gaī"],
                    ["I did not go", "मैं नहीं गया", "main nahī̃ gayā"],
                ],
            ),
        ],
    )


def chapter_519() -> dict:
    return _lesson(
        "With transitive verbs in past: agent takes ने and verb agrees with object: मैंने किताब पढ़ी.",
        "ने marks the doer; main verb often past participle agreeing with object.",
        [
            _p("ने construction", "मैंने खाना खाया; उसने पत्र लिखा; हमने फ़िल्म देखी."),
            _t(
                "Past with object (ने)",
                [
                    ["I saw him", "मैंने उसे देखा", "mainne use dekhā"],
                    ["She wrote a letter", "उसने पत्र लिखा", "usne patr likhā"],
                    ["We bought vegetables", "हमने सब्ज़ी खरीदी", "hamne sabzī kharīdī"],
                    ["He opened the door", "उसने दरवाज़ा खोला", "usne darvāzā kholā"],
                    ["They built a house", "उन्होंने घर बनाया", "unhoṃne ghar banāyā"],
                    ["I read the paper", "मैंने अख़बार पढ़ा", "mainne akhbār paṛhā"],
                    ["You helped us", "आपने हमारी मदद की", "āpne hamārī madad kī"],
                    ["She closed the window", "उसने खिड़की बंद की", "usne khiṛkī band kī"],
                    ["We watched TV", "हमने टीवी देखा", "hamne ṭīvī dekhā"],
                    ["He paid the bill", "उसने बिल भरा", "usne bil bharā"],
                    ["I sent an email", "मैंने ईमेल भेजा", "mainne īmel bhejā"],
                    ["They answered", "उन्होंने जवाब दिया", "unhoṃne javāb diyā"],
                    ["I did not see", "मैंने नहीं देखा", "mainne nahī̃ dekhā"],
                    ["She cooked food", "उसने खाना बनाया", "usne khānā banāyā"],
                    ["We chose seats", "हमने सीटें चुनीं", "hamne sīṭeṃ cunī̃"],
                    ["He fixed the tyre", "उसने टायर ठीक किया", "usne ṭāyar ṭhīk kiyā"],
                ],
            ),
        ],
    )


def chapter_520() -> dict:
    return _lesson(
        "Past of होना: था (m.sg), थी (f.sg), थे (m.pl / polite), थीं (f.pl).",
        "मैं थका हुआ था; वह बीमार थी; हम खुश थे.",
        [
            _p("Negation", "नहीं था / नहीं थी — was not."),
            _t(
                "Past 'to be'",
                [
                    ["I was tired", "मैं थका हुआ था", "main thakā huā thā"],
                    ["You were right", "आप सही थे", "āp sahī the"],
                    ["He was ill", "वह बीमार था", "vah bīmār thā"],
                    ["She was happy", "वह खुश थी", "vah khush thī"],
                    ["We were students", "हम छात्र थे", "ham chātra the"],
                    ["They were late", "वे देर से थे", "ve der se the"],
                    ["It was cold", "ठंड थी", "thaṃḍ thī"],
                    ["There was a problem", "एक समस्या थी", "ek samasyā thī"],
                    ["I was not ready", "मैं तैयार नहीं था", "main taiyār nahī̃ thā"],
                    ["Were you there?", "क्या आप वहाँ थे?", "kyā āp vahā̃ the?"],
                    ["The shop was closed", "दुकान बंद थी", "dukān band thī"],
                    ["We were friends", "हम दोस्त थे", "ham dost the"],
                    ["It was raining", "बारिश हो रही थी", "bāriś ho rahī thī"],
                    ["I was at home", "मैं घर पर था", "main ghar par thā"],
                    ["They were angry", "वे नाराज़ थे", "ve nārāz the"],
                    ["Time was short", "समय कम था", "samay kam thā"],
                ],
            ),
        ],
    )


def chapter_521() -> dict:
    return _lesson(
        "Some verbs have suppletive or irregular past stems: गया from जाना, आया from आना, दिया from देना, लिया from लेना.",
        "Memorize common pairs; patterns differ slightly in perfective.",
        [
            _p("Examples", "गया/गई/गए; आया/आई/आए; दिया/दी/दिए; लिया/ली/लिए."),
            _t(
                "Exceptional past forms",
                [
                    ["I went", "मैं गया", "main gayā"],
                    ["She came", "वह आई", "vah āī"],
                    ["He gave", "उसने दिया", "usne diyā"],
                    ["We took", "हमने लिया", "hamne liyā"],
                    ["They went", "वे गए", "ve ga.e"],
                    ["I sat", "मैं बैठ गया", "main baiṭh gayā"],
                    ["She lay down", "वह लेट गई", "vah leṭ gaī"],
                    ["He died", "वह मर गया", "vah mar gayā"],
                    ["We met", "हम मिले", "ham mile"],
                    ["I said", "मैंने कहा", "mainne kahā"],
                    ["She did", "उसने किया", "usne kiyā"],
                    ["They saw", "उन्होंने देखा", "unhoṃne dekhā"],
                    ["I could (was able)", "मैं कर सका", "main kar sakā"],
                    ["He fell asleep", "वह सो गया", "vah so gayā"],
                    ["We forgot", "हम भूल गए", "ham bhūl ga.e"],
                    ["She understood", "वह समझ गई", "vah samajh gaī"],
                ],
            ),
        ],
    )


def chapter_522() -> dict:
    return _lesson(
        "Past continuous: was/were + -ing → रहा था / रही थी / रहे थे.",
        "मैं पढ़ रहा था; बारिश हो रही थी.",
        [
            _p("Pattern", "Progressive participle + past tense of होना."),
            _t(
                "Past continuous",
                [
                    ["I was reading", "मैं पढ़ रहा था", "main paṛh rahā thā"],
                    ["She was cooking", "वह खाना बना रही थी", "vah khānā banā rahī thī"],
                    ["They were playing", "वे खेल रहे थे", "ve khel rahe the"],
                    ["We were waiting", "हम इंतज़ार कर रहे थे", "ham intazār kar rahe the"],
                    ["He was driving", "वह गाड़ी चला रहा था", "vah gāṛī calā rahā thā"],
                    ["It was snowing", "बर्फ़बारी हो रही थी", "barfabārī ho rahī thī"],
                    ["Birds were singing", "पक्षी गा रहे थे", "pakṣī gā rahe the"],
                    ["Children were crying", "बच्चे रो रहे थे", "bacce ro rahe the"],
                    ["Phone was ringing", "फोन बज रहा था", "phon baj rahā thā"],
                    ["Sun was setting", "सूरज डूब रहा था", "sūraj ḍūb rahā thā"],
                    ["I was thinking", "मैं सोच रहा था", "main soc rahā thā"],
                    ["We were talking", "हम बात कर रहे थे", "ham bāt kar rahe the"],
                    ["Train was leaving", "ट्रेन चल रही थी", "ṭren cal rahī thī"],
                    ["He was sleeping", "वह सो रहा था", "vah so rahā thā"],
                    ["They were building", "वे बना रहे थे", "ve banā rahe the"],
                    ["I was not listening", "मैं सुन नहीं रहा था", "main sun nahī̃ rahā thā"],
                ],
            ),
        ],
    )


def chapter_523() -> dict:
    return _lesson(
        "Perfect: चुका / चुकी / चुके + है/हैं/था — completed action with present/past auxiliary.",
        "मैं खा चुका हूँ; वह जा चुकी थी.",
        [
            _p("Also", "ले लिया, कर दिया express completed 'completive' aspect."),
            _t(
                "Perfect tense",
                [
                    ["I have eaten", "मैं खा चुका हूँ", "main khā cukā hū̃"],
                    ["She has left", "वह जा चुकी है", "vah jā cukī hai"],
                    ["We have finished", "हम खत्म कर चुके हैं", "ham khatm kar cuke haiṃ"],
                    ["They had arrived", "वे आ चुके थे", "ve ā cuke the"],
                    ["I had seen", "मैं देख चुका था", "main dekh cukā thā"],
                    ["Have you read?", "क्या आप पढ़ चुके हैं?", "kyā āp paṛh cuke haiṃ?"],
                    ["He has paid", "वह भुगतान कर चुका है", "vah bhugtān kar cukā hai"],
                    ["We had met before", "हम पहले मिल चुके थे", "ham pahle mil cuke the"],
                    ["By then I will have left", "तब तक मैं जा चुका होऊँगा", "tab tak main jā cukā hoū̃gā"],
                    ["She has cooked", "वह बना चुकी है", "vah banā cukī hai"],
                    ["I have lost my key", "मैं चाबी खो चुका हूँ", "main cābī kho cukā hū̃"],
                    ["They have agreed", "वे सहमत हो चुके हैं", "ve sahamat ho cuke haiṃ"],
                    ["It has started", "यह शुरू हो चुका है", "yah śurū ho cukā hai"],
                    ["We have tried", "हम कोशिश कर चुके हैं", "ham kośiś kar cuke haiṃ"],
                    ["He had said", "उसने कह दिया था", "usne kah diyā thā"],
                    ["I will have eaten", "मैं खा चुका होऊँगा", "main khā cukā hoū̃gā"],
                ],
            ),
        ],
    )


def chapter_524() -> dict:
    return _lesson(
        "Postpositions (so-called prepositions): में, पर, से, को, के लिए, के पास — noun + postposition.",
        "Hindi places relation words after the noun: घर में, मेज़ पर, दिल्ली से.",
        [
            _p("Core set", "को marks direct/indirect object in many frames; से 'from/with/by'; में 'in/at'; पर 'on/at'."),
            _t(
                "Common postpositions",
                [
                    ["in the house", "घर में", "ghar mẽ"],
                    ["on the table", "मेज़ पर", "mez par"],
                    ["from Delhi", "दिल्ली से", "dillī se"],
                    ["to him (object)", "उसको", "usko"],
                    ["for mother", "माँ के लिए", "mā̃ ke lie"],
                    ["near the park", "पार्क के पास", "pārk ke pās"],
                    ["under the tree", "पेड़ के नीचे", "peṛ ke nīce"],
                    ["behind the car", "गाड़ी के पीछे", "gāṛī ke pīche"],
                    ["between us", "हमारे बीच", "hamāre bīc"],
                    ["until evening", "शाम तक", "śām tak"],
                    ["since morning", "सुबह से", "subah se"],
                    ["without sugar", "बिना चीनी के", "binā cīnī ke"],
                    ["with friends", "दोस्तों के साथ", "dostõ ke sāth"],
                    ["I am at home", "मैं घर पर हूँ", "main ghar par hū̃"],
                    ["Book is on the chair", "किताब कुर्सी पर है", "kitāb kursī par hai"],
                    ["Water in the bottle", "बोतल में पानी", "botal mẽ pānī"],
                    ["She went to school", "वह स्कूल गई", "vah skūl gaī"],
                ],
            ),
        ],
    )


def chapter_525() -> dict:
    return _lesson(
        "English 'to' (direction, recipient, purpose) often maps to को, में, की ओर, or infinitive + के लिए.",
        "मैं दिल्ली जा रहा हूँ; उसे पत्र लिखो; यह तुम्हारे लिए है.",
        [
            _p("Direction vs dative", "Place names: दिल्ली जाना. Person as goal: उसको देना. Purpose: पढ़ने के लिए."),
            _t(
                "‘To’ in Hindi",
                [
                    ["I am going to Mumbai", "मैं मुंबई जा रहा हूँ", "main muṃbaī jā rahā hū̃"],
                    ["Give water to him", "उसे पानी दो", "use pānī do"],
                    ["Talk to her", "उससे बात करो", "us se bāt karo"],
                    ["This letter is to father", "यह पत्र पिताजी के लिए है", "yah patr pitājī ke lie hai"],
                    ["Turn to the left", "बाएँ मुड़ो", "bāẽ muṛo"],
                    ["Road to the station", "स्टेशन की ओर सड़क", "sṭeśan kī or saṛak"],
                    ["I explained to them", "मैंने उन्हें समझाया", "mainne unheṃ samjhāyā"],
                    ["Send this to me", "यह मुझे भेजो", "yah mujhe bhejo"],
                    ["Key to the lock", "ताले की चाबी", "tāle kī cābī"],
                    ["Thanks to you", "आपकी वजह से", "āpkī vajah se"],
                    ["Admission to college", "कॉलेज में दाखिला", "kŏlej mẽ dākhilā"],
                    ["I go to work", "मैं काम पर जाता हूँ", "main kām par jātā hū̃"],
                    ["Listen to music", "संगीत सुनो", "saṅgīt suno"],
                    ["Welcome to India", "भारत में आपका स्वागत है", "bhārat mẽ āpkā svāgat hai"],
                    ["From door to door", "दरवाज़े से दरवाज़े तक", "darvāze se darvāze tak"],
                    ["I promised to help", "मैंने मदद करने का वादा किया", "mainne madad karne kā vādā kiyā"],
                ],
            ),
        ],
    )


def chapter_526() -> dict:
    return _lesson(
        "Animate objects take को: मैंने उसे देखा. Some verbs use से for person-source.",
        "को marks the person affected; contrast with inanimate direct objects in ने-constructions.",
        [
            _p("People as objects", "उसको बुलाओ; मैं तुम्हें जानता हूँ; हम उन्हें मिलेंगे."),
            _t(
                "Person / animate object",
                [
                    ["I saw her", "मैंने उसे देखा", "mainne use dekhā"],
                    ["Call him", "उसे बुलाओ", "use bulāo"],
                    ["Help them", "उनकी मदद करो", "unkī madad karo"],
                    ["I know you", "मैं आपको जानता हूँ", "main āpko jāntā hū̃"],
                    ["We met them", "हम उनसे मिले", "ham un se mile"],
                    ["She teaches children", "वह बच्चों को पढ़ाती है", "vah baccõ ko paṛhātī hai"],
                    ["Give food to the dog", "कुत्ते को खाना दो", "kutte ko khānā do"],
                    ["I told mother", "मैंने माँ को बताया", "mainne mā̃ ko batāyā"],
                    ["They invited us", "उन्होंने हमें बुलाया", "unhoṃne hameṃ bulāyā"],
                    ["Find me a doctor", "मुझे डॉक्टर ढूँढो", "mujhe ḍokṭar ḍhū̃ḍho"],
                    ["I love my city", "मुझे अपना शहर पसंद है", "mujhe apnā śahar pasand hai"],
                    ["Respect elders", "बुज़ुर्गों का सम्मान करो", "buzurgõ kā sammān karo"],
                    ["He introduced me", "उसने मुझे परिचय कराया", "usne mujhe paricay karāyā"],
                    ["We trust you", "हम आप पर भरोसा करते हैं", "ham āp par bharosā karte haiṃ"],
                    ["She waved at me", "उसने मुझे हाथ हिलाया", "usne mujhe hāth hilāyā"],
                    ["Do not hurt anyone", "किसी को चोट मत पहुँचाओ", "kisī ko coṭ mat pahuṃcāo"],
                ],
            ),
        ],
    )


def chapter_527() -> dict:
    return _lesson(
        "Possessive: मेरा/मेरी/मेरे, तुम्हारा, आपका, उसका, हमारा — agree with the thing possessed.",
        "मेरी किताब; मेरा घर; मेरे दोस्त.",
        [
            _p("Agreement", "Possessive adjective matches gender/number of the possessed noun, not always the owner."),
            _t(
                "My / his / her",
                [
                    ["my book (f.)", "मेरी किताब", "merī kitāb"],
                    ["my brother", "मेरा भाई", "merā bhāī"],
                    ["my friends", "मेरे दोस्त", "mere dost"],
                    ["your house (polite)", "आपका घर", "āpkā ghar"],
                    ["his car", "उसकी गाड़ी", "uskī gāṛī"],
                    ["her idea", "उसका विचार", "uskā vicār"],
                    ["our school", "हमारा स्कूल", "hamārā skūl"],
                    ["their problem", "उनकी समस्या", "unkī samasyā"],
                    ["This is my bag", "यह मेरा बैग है", "yah merā baig hai"],
                    ["That is his phone", "वह उसका फोन है", "vah uskā phon hai"],
                    ["Her mother is kind", "उसकी माँ दयालु हैं", "uskī mā̃ dayālu haiṃ"],
                    ["Our teacher speaks well", "हमारे शिक्षक अच्छा बोलते हैं", "hamāre śikṣak acchā bolte haiṃ"],
                    ["Your children study", "आपके बच्चे पढ़ते हैं", "āp ke bacche paṛhte haiṃ"],
                    ["I lost my keys", "मेरी चाबियाँ खो गईं", "merī cābiyā̃ kho gaī̃"],
                    ["His opinion matters", "उसकी राय मायने रखती है", "uskī rāy māyne rakhtī hai"],
                    ["Their village is small", "उनका गाँव छोटा है", "unkā gā̃v choṭā hai"],
                ],
            ),
        ],
    )


def chapter_528() -> dict:
    return _lesson(
        "Yes/no: क्या …? Tag questions: ना?, है ना? WH: कौन, क्या, कब, कहाँ, क्यों, कैसे.",
        "क्या आप ठीक हैं? आप कहाँ रहते हैं?",
        [
            _p("Politeness", "Use आप + plural verb in questions to strangers and elders."),
            _t(
                "Questions",
                [
                    ["Are you ready?", "क्या आप तैयार हैं?", "kyā āp taiyār haiṃ?"],
                    ["Is this yours?", "क्या यह आपका है?", "kyā yah āpkā hai?"],
                    ["Do you speak Hindi?", "क्या आप हिन्दी बोलते हैं?", "kyā āp hindī bolte haiṃ?"],
                    ["Who is he?", "वह कौन है?", "vah kaun hai?"],
                    ["What is this?", "यह क्या है?", "yah kyā hai?"],
                    ["When will you come?", "आप कब आएँगे?", "āp kab āeṅge?"],
                    ["Where do you live?", "आप कहाँ रहते हैं?", "āp kahā̃ rahte haiṃ?"],
                    ["Why are you late?", "आप देर से क्यों हैं?", "āp der se kyõ haiṃ?"],
                    ["How did you come?", "आप कैसे आए?", "āp kaise ā.e?"],
                    ["Which book?", "कौन सी किताब?", "kaun sī kitāb?"],
                    ["How many?", "कितने?", "kitne?"],
                    ["How much money?", "कितने पैसे?", "kitne paise?"],
                    ["Right?", "ठीक है ना?", "ṭhīk hai nā?"],
                    ["You will come, won't you?", "आप आओगे, है ना?", "āp āoge, hai nā?"],
                    ["May I ask something?", "क्या मैं कुछ पूछ सकता हूँ?", "kyā main kuch pūch saktā hū̃?"],
                    ["What time is it?", "कितने बजे हैं?", "kitne baje haiṃ?"],
                ],
            ),
        ],
    )


def chapter_529() -> dict:
    return _lesson(
        "Negation with नहीं before verb; नहीं है for 'is not'; मत for imperative 'don't'.",
        "मैं नहीं जा रहा; यह सच नहीं है.",
        [
            _p("Present", "नहीं + finite verb; sometimes न … नहीं for emphasis."),
            _t(
                "Negative (present)",
                [
                    ["I do not know", "मुझे नहीं पता", "mujhe nahī̃ patā"],
                    ["She does not eat meat", "वह माँस नहीं खाती", "vah mā̃s nahī̃ khātī"],
                    ["We are not afraid", "हम डरे नहीं हैं", "ham ḍare nahī̃ haiṃ"],
                    ["He is not here", "वह यहाँ नहीं है", "vah yahā̃ nahī̃ hai"],
                    ["This is not easy", "यह आसान नहीं है", "yah āsān nahī̃ hai"],
                    ["I do not like it", "मुझे यह पसंद नहीं", "mujhe yah pasand nahī̃"],
                    ["They do not agree", "वे सहमत नहीं हैं", "ve sahamat nahī̃ haiṃ"],
                    ["I am not going", "मैं नहीं जा रहा", "main nahī̃ jā rahā"],
                    ["We do not have time", "हमारे पास समय नहीं है", "hamāre pās samay nahī̃ hai"],
                    ["It does not work", "यह काम नहीं करता", "yah kām nahī̃ kartā"],
                    ["I cannot swim", "मैं तैर नहीं सकता", "main tair nahī̃ saktā"],
                    ["She is not angry", "वह नाराज़ नहीं है", "vah nārāz nahī̃ hai"],
                    ["We do not understand", "हम समझते नहीं हैं", "ham samajhte nahī̃ haiṃ"],
                    ["He does not drive", "वह गाड़ी नहीं चलाता", "vah gāṛī nahī̃ calātā"],
                    ["I do not need money", "मुझे पैसे नहीं चाहिए", "mujhe paise nahī̃ cāhie"],
                    ["Not today", "आज नहीं", "āj nahī̃"],
                ],
            ),
        ],
    )


def chapter_530() -> dict:
    return _lesson(
        "Past negation: नहीं + past form; नहीं था for 'was not'; ने … नहीं for completed actions.",
        "मैं नहीं गया; उसने नहीं देखा.",
        [
            _p("Pattern", "Same placement as present: verb carries negation."),
            _t(
                "Negative (past)",
                [
                    ["I did not go", "मैं नहीं गया", "main nahī̃ gayā"],
                    ["She did not come", "वह नहीं आई", "vah nahī̃ āī"],
                    ["We did not eat", "हमने नहीं खाया", "hamne nahī̃ khāyā"],
                    ["He did not call", "उसने फोन नहीं किया", "usne phon nahī̃ kiyā"],
                    ["They did not agree", "उन्होंने हाँ नहीं कहा", "unhoṃne hā̃ nahī̃ kahā"],
                    ["I was not there", "मैं वहाँ नहीं था", "main vahā̃ nahī̃ thā"],
                    ["It was not cold", "ठंड नहीं थी", "thaṃḍ nahī̃ thī"],
                    ["We were not ready", "हम तैयार नहीं थे", "ham taiyār nahī̃ the"],
                    ["She did not know", "उसे नहीं पता था", "use nahī̃ patā thā"],
                    ["I did not see you", "मैंने आपको नहीं देखा", "mainne āpko nahī̃ dekhā"],
                    ["He did not pay", "उसने भुगतान नहीं किया", "usne bhugtān nahī̃ kiyā"],
                    ["They did not wait", "उन्होंने इंतज़ार नहीं किया", "unhoṃne intazār nahī̃ kiyā"],
                    ["I did not forget", "मैं भूला नहीं", "main bhūlā nahī̃"],
                    ["We did not win", "हम जीते नहीं", "ham jīte nahī̃"],
                    ["She did not answer", "उसने जवाब नहीं दिया", "usne javāb nahī̃ diyā"],
                    ["It did not happen", "यह नहीं हुआ", "yah nahī̃ huā"],
                ],
            ),
        ],
    )


def chapter_531() -> dict:
    return _lesson(
        "Future negation: नहीं + future verb; sometimes मत + future for strong refusal in speech.",
        "मैं नहीं जाऊँगा; वह नहीं करेगी.",
        [
            _p("Will not", "नहीं before the future auxiliary or -गा form."),
            _t(
                "Negative (future)",
                [
                    ["I will not go", "मैं नहीं जाऊँगा", "main nahī̃ jāū̃gā"],
                    ["She will not come", "वह नहीं आएगी", "vah nahī̃ āegī"],
                    ["We will not leave", "हम नहीं जाएँगे", "ham nahī̃ jāeṅge"],
                    ["He will not pay", "वह भुगतान नहीं करेगा", "vah bhugtān nahī̃ karegā"],
                    ["They will not agree", "वे सहमत नहीं होंगे", "ve sahamat nahī̃ hoṅge"],
                    ["It will not rain", "बारिश नहीं होगी", "bāriś nahī̃ hogī"],
                    ["I will not forget", "मैं नहीं भूलूँगा", "main nahī̃ bhūlū̃gā"],
                    ["We will not be late", "हम देर से नहीं होंगे", "ham der se nahī̃ hoṅge"],
                    ["He will not speak", "वह नहीं बोलेगा", "vah nahī̃ bolegā"],
                    ["She will not cook", "वह खाना नहीं बनाएगी", "vah khānā nahī̃ banāegī"],
                    ["I will not buy it", "मैं यह नहीं खरीदूँगा", "main yah nahī̃ kharīdū̃gā"],
                    ["They will not wait", "वे इंतज़ार नहीं करेंगे", "ve intazār nahī̃ kareṅge"],
                    ["We will not lose", "हम नहीं हारेंगे", "ham nahī̃ hāreṅge"],
                    ["He will not return", "वह वापस नहीं आएगा", "vah vāpas nahī̃ āegā"],
                    ["I will not tell", "मैं नहीं बताऊँगा", "main nahī̃ batāū̃gā"],
                    ["Tomorrow I will not work", "कल मैं काम नहीं करूँगा", "kal main kām nahī̃ karū̃gā"],
                ],
            ),
        ],
    )


def chapter_532() -> dict:
    return _lesson(
        "Nouns have gender (लिंग): masculine/feminine; plurals often -ए / ओं / याँ; learn patterns with common words.",
        "लड़का → लड़के; लड़की → लड़कियाँ; किताब → किताबें.",
        [
            _p("Agreement", "Adjectives and verbs often agree with noun gender/number."),
            _t(
                "Gender and plurals",
                [
                    ["boy / boys", "लड़का / लड़के", "laṛkā / laṛke"],
                    ["girl / girls", "लड़की / लड़कियाँ", "laṛkī / laṛkiyā̃"],
                    ["book / books", "किताब / किताबें", "kitāb / kitābeṃ"],
                    ["house / houses", "घर / घर", "ghar / ghar"],
                    ["teacher (m./f.)", "शिक्षक / शिक्षिका", "śikṣak / śikṣikā"],
                    ["friend / friends", "दोस्त / दोस्त", "dost / dost"],
                    ["car / cars", "गाड़ी / गाड़ियाँ", "gāṛī / gāṛiyā̃"],
                    ["dog / dogs", "कुत्ता / कुत्ते", "kuttā / kutte"],
                    ["tree / trees", "पेड़ / पेड़", "peṛ / peṛ"],
                    ["big (m./f.)", "बड़ा / बड़ी", "baṛā / baṛī"],
                    ["small (m./f.)", "छोटा / छोटी", "choṭā / choṭī"],
                    ["good (m./f.)", "अच्छा / अच्छी", "acchā / acchī"],
                    ["These boys play", "ये लड़के खेलते हैं", "ye laṛke khelte haiṃ"],
                    ["Those girls read", "वह लड़कियाँ पढ़ती हैं", "vah laṛkiyā̃ paṛhtī haiṃ"],
                    ["The books are new", "किताबें नई हैं", "kitābeṃ naī haiṃ"],
                ],
            ),
        ],
    )


def chapter_533() -> dict:
    return _lesson(
        "Noun + postposition frames: के साथ, के बिना, के बाद, के पहले, में, पर, से.",
        "घर के बाद; दोस्त के साथ; काम पर.",
        [
            _p("Chunks", "Learn fixed three-word chains: नाम के लिए, समय के साथ."),
            _t(
                "Nouns with postpositions",
                [
                    ["after lunch", "दोपहर के बाद", "dopahar ke bād"],
                    ["before the exam", "परीक्षा से पहले", "parīkṣā se pahle"],
                    ["with my brother", "मेरे भाई के साथ", "mere bhāī ke sāth"],
                    ["without money", "पैसे के बिना", "paise ke binā"],
                    ["on the roof", "छत पर", "chat par"],
                    ["in the kitchen", "रसोई में", "rasoī mẽ"],
                    ["from the market", "बाज़ार से", "bāzār se"],
                    ["for the children", "बच्चों के लिए", "baccõ ke lie"],
                    ["near the bank", "बैंक के पास", "baiṅk ke pās"],
                    ["between the lines", "लाइनों के बीच", "lāinõ ke bīc"],
                    ["during the rain", "बारिश के दौरान", "bāriś ke daurān"],
                    ["because of work", "काम की वजह से", "kām kī vajah se"],
                    ["I work at night", "मैं रात में काम करता हूँ", "main rāt mẽ kām kartā hū̃"],
                    ["She studies at home", "वह घर पर पढ़ती है", "vah ghar par paṛhtī hai"],
                    ["We eat after yoga", "हम योग के बाद खाते हैं", "ham yog ke bād khāte haiṃ"],
                    ["He left before me", "वह मुझसे पहले चला गया", "vah mujh se pahle calā gayā"],
                ],
            ),
        ],
    )


def chapter_534() -> dict:
    return _lesson(
        "Near-homophones: पर vs पर (stress), में vs मैं in speech; से vs सै in spelling.",
        "Listen: मैं घर में हूँ — मैं ≠ में.",
        [
            _p("Meaning pairs", "ऊपर 'above' vs ओपर 'upper' (rare); किनारा 'edge' vs किनारा place names — context."),
            _t(
                "Similar sound / sense",
                [
                    ["in (location)", "घर में", "ghar mẽ"],
                    ["I", "मैं", "main"],
                    ["on / but", "पर", "par"],
                    ["feather", "पर", "par"],
                    ["from / with", "से", "se"],
                    ["near", "पास", "pās"],
                    ["far", "दूर", "dūr"],
                    ["inside", "अंदर", "andar"],
                    ["outside", "बाहर", "bāhar"],
                    ["before (time)", "पहले", "pahle"],
                    ["after (time)", "बाद में", "bād mẽ"],
                    ["for (benefit)", "के लिए", "ke lie"],
                    ["because", "क्योंकि", "kyõki"],
                    ["therefore", "इसलिए", "islie"],
                    ["I am in the room", "मैं कमरे में हूँ", "main kamre mẽ hū̃"],
                    ["Book is on the table", "किताब मेज़ पर है", "kitāb mez par hai"],
                    ["Come with me", "मेरे साथ आओ", "mere sāth āo"],
                ],
            ),
        ],
    )


def chapter_535() -> dict:
    return _lesson(
        "विभक्ति: direct को; instrumental/ablative से; genitive का/की/के; locative में/पर.",
        "राम ने सीता को फल दिया — ने ergative, को object, का possession.",
        [
            _p("Spoken Hindi", "Postpositions do the job of Sanskrit cases; learn frames, not Sanskrit names."),
            _t(
                "Cases (overview)",
                [
                    ["Rama gave Sita fruit", "राम ने सीता को फल दिया", "rām ne sītā ko phal diyā"],
                    ["cut with a knife", "चाकू से काटो", "cākū se kāṭo"],
                    ["mother's saree", "माँ की साड़ी", "mā̃ kī sāṛī"],
                    ["in the city", "शहर में", "śahar mẽ"],
                    ["on the road", "सड़क पर", "saṛak par"],
                    ["from Mumbai", "मुंबई से", "muṃbaī se"],
                    ["for the child", "बच्चे के लिए", "bacce ke lie"],
                    ["until tomorrow", "कल तक", "kal tak"],
                    ["without you", "तुम्हारे बिना", "tumhāre binā"],
                    ["I saw the dog", "मैंने कुत्ते को देखा", "mainne kutte ko dekhā"],
                    ["written by her", "उसके द्वारा लिखा", "uske dvārā likhā"],
                    ["inside the box", "डिब्बे में", "ḍibbe mẽ"],
                    ["behind the house", "घर के पीछे", "ghar ke pīche"],
                    ["between us", "हमारे बीच", "hamāre bīc"],
                    ["because of rain", "बारिश की वजह से", "bāriś kī vajah se"],
                    ["according to rules", "नियमों के अनुसार", "niyamõ ke anusār"],
                ],
            ),
        ],
    )


def chapter_536() -> dict:
    return _lesson(
        "Imperatives: करो (informal), कीजिए (polite), मत करो 'don't'.",
        "आइए, बैठिए, देखिए — polite request forms.",
        [
            _p("Levels", "तुम करो; आप कीजिए; sometimes चलो for 'let's'."),
            _t(
                "Commands",
                [
                    ["Come here", "यहाँ आओ", "yahā̃ āo"],
                    ["Please sit", "कृपया बैठिए", "kripayā baithie"],
                    ["Listen carefully", "ध्यान से सुनो", "dhyān se suno"],
                    ["Open the door", "दरवाज़ा खोलो", "darvāzā kholo"],
                    ["Do not shout", "चिल्लाओ मत", "cillāo mat"],
                    ["Let's go", "चलो", "calo"],
                    ["Please wait", "कृपया इंतज़ार कीजिए", "kripayā intazār kījie"],
                    ["Write your name", "अपना नाम लिखो", "apnā nām likho"],
                    ["Bring water", "पानी लाओ", "pānī lāo"],
                    ["Do not worry", "चिंता मत करो", "cintā mat karo"],
                    ["Tell the truth", "सच बोलो", "sac bolo"],
                    ["Please help", "कृपया मदद कीजिए", "kripayā madad kījie"],
                    ["Stop here", "यहीं रुको", "yahī̃ ruko"],
                    ["Read aloud", "ज़ोर से पढ़ो", "zor se paṛho"],
                    ["Do not touch", "मत छुओ", "mat chuo"],
                    ["Have some tea", "चाय लीजिए", "cāy lījie"],
                ],
            ),
        ],
    )


def chapter_537() -> dict:
    return _lesson(
        "Time words: आज, कल, परसों, सुबह, शाम, बजे, घंटा, मिनट, हफ़्ता, महीना, साल.",
        "सुबह सात बजे; शाम को; अगले हफ़्ते.",
        [
            _p("Usage", "कल = yesterday or tomorrow by context; परसों = day after tomorrow / before."),
            _t(
                "Time expressions",
                [
                    ["today", "आज", "āj"],
                    ["tomorrow / yesterday", "कल", "kal"],
                    ["day after tomorrow", "परसों", "parsõ"],
                    ["morning", "सुबह", "subah"],
                    ["evening", "शाम", "śām"],
                    ["night", "रात", "rāt"],
                    ["o'clock", "बजे", "baje"],
                    ["hour", "घंटा", "ghaṃṭā"],
                    ["minute", "मिनट", "minaṭ"],
                    ["week", "हफ़्ता", "haftā"],
                    ["month", "महीना", "mahīnā"],
                    ["year", "साल", "sāl"],
                    ["now", "अभी", "abhī"],
                    ["later", "बाद में", "bād mẽ"],
                    ["early", "जल्दी", "jaldī"],
                    ["late", "देर", "der"],
                    ["I will come at 5", "मैं पाँच बजे आऊँगा", "main pā̃c baje āū̃gā"],
                    ["Meeting is tomorrow morning", "मीटिंग कल सुबह है", "mīṭiṅ kal subah hai"],
                ],
            ),
        ],
    )


def chapter_538() -> dict:
    return _lesson(
        "Causative: 'get X done' — बनवाना, पढ़वाना, दिखलाना; मैंने उससे काम करवाया.",
        "Double verbs add the sense of causing or having someone act.",
        [
            _p("Pattern", "Root + वा + ना: करवाना 'to get done', पढ़वाना 'to get taught'."),
            _t(
                "Causative verbs",
                [
                    ["to get built", "बनवाना", "banvānā"],
                    ["to get read (by someone)", "पढ़वाना", "paṛhvānā"],
                    ["to get shown", "दिखवाना", "dikhvānā"],
                    ["I got the room painted", "मैंने कमरा रंग करवाया", "mainne kamrā raṅg karvāyā"],
                    ["She made him study", "उसने उससे पढ़वाया", "usne us se paṛhvāyā"],
                    ["We had the car repaired", "हमने गाड़ी ठीक करवाई", "hamne gāṛī ṭhīk karvāī"],
                    ["He got a letter written", "उसने पत्र लिखवाया", "usne patr likhvāyā"],
                    ["Get the door opened", "दरवाज़ा खुलवाओ", "darvāzā khulvāo"],
                    ["I will get food cooked", "मैं खाना बनवाऊँगा", "main khānā banvāū̃gā"],
                    ["They had a house built", "उन्होंने घर बनवाया", "unhoṃne ghar banvāyā"],
                    ["Please get this copied", "इसकी कॉपी करवा लीजिए", "iskī kŏpī karvā lijie"],
                    ["Mother got clothes stitched", "माँ ने कपड़े सिलवाए", "mā̃ ne kapṛe silvā.e"],
                    ["I got my hair cut", "मैंने बाल कटवाए", "mainne bāl kaṭvā.e"],
                    ["He made me run", "उसने मुझसे दौड़वाया", "usne mujh se dauṛvāyā"],
                    ["We got tickets booked", "हमने टिकट बुक करवाए", "hamne ṭikaṭ buk karvā.e"],
                    ["She got the form filled", "उसने फ़ॉर्म भरवाया", "usne phŏrm bharvāyā"],
                ],
            ),
        ],
    )


def chapter_539() -> dict:
    return _lesson(
        "Agreement: verb/adjective match subject in intransitive clauses; with ने, verb may agree with object.",
        "लड़की गई; लड़के गए; मैंने किताब पढ़ी.",
        [
            _p("ने rule", "Transitive past: agent + ने + verb agreeing with object gender/number."),
            _t(
                "Gender-number agreement",
                [
                    ["The boy went", "लड़का गया", "laṛkā gayā"],
                    ["The girl went", "लड़की गई", "laṛkī gaī"],
                    ["The boys went", "लड़के गए", "laṛke ga.e"],
                    ["I read the book (f.)", "मैंने किताब पढ़ी", "mainne kitāb paṛhī"],
                    ["I read the letter (m.)", "मैंने पत्र पढ़ा", "mainne patr paṛhā"],
                    ["She opened doors (f.)", "उसने दरवाज़े खोले", "usne darvāze khole"],
                    ["We saw the film (f.)", "हमने फ़िल्म देखी", "hamne film dekhī"],
                    ["He bought apples (m.)", "उसने सेब खरीदे", "usne seb kharīde"],
                    ["They closed windows (f.)", "उन्होंने खिड़कियाँ बंद कीं", "unhoṃne khiṛkiyā̃ band kī̃"],
                    ["Good coffee (f.)", "अच्छी कॉफ़ी", "acchī kŏfī"],
                    ["Good boy (m.)", "अच्छा लड़का", "acchā laṛkā"],
                    ["She is happy (f.)", "वह खुश है", "vah khush hai"],
                    ["He is happy (m.)", "वह खुश है", "vah khush hai"],
                    ["We are ready (m.pl)", "हम तैयार हैं", "ham taiyār haiṃ"],
                    ["Respectful plural verb", "आप जाते हैं", "āp jāte haiṃ"],
                    ["These rules help clarity", "ये नियम स्पष्टता देते हैं", "ye niyam spaṣṭatā dete haiṃ"],
                ],
            ),
        ],
    )


def chapter_540() -> dict:
    return _lesson(
        "Second-style perfect: हो चुका है; or compound with रहा: पढ़ रहा हूँ — bookish/emphatic variants.",
        "Formal news: किया जा चुका है 'has been done'.",
        [
            _p("Note", "Spoken Hindi prefers चुका; written Hindi may use गया/आया compounds similarly."),
            _t(
                "Perfect — second style",
                [
                    ["Work has been completed", "काम पूरा हो चुका है", "kām pūrā ho cukā hai"],
                    ["The letter has been sent", "पत्र भेजा जा चुका है", "patr bhejā jā cukā hai"],
                    ["I have been informed", "मुझे सूचित कर दिया गया है", "mujhe sūcit kar diyā gayā hai"],
                    ["She had already eaten", "वह पहले ही खा चुकी थी", "vah pahle hī khā cukī thī"],
                    ["We had left", "हम जा चुके थे", "ham jā cuke the"],
                    ["They will have arrived", "वे पहुँच चुके होंगे", "ve pahuṃc cuke hoṅge"],
                    ["It has been decided", "यह तय हो चुका है", "yah tay ho cukā hai"],
                    ["I have been waiting", "मैं इंतज़ार कर रहा हूँ", "main intazār kar rahā hū̃"],
                    ["He has been working", "वह काम कर रहा है", "vah kām kar rahā hai"],
                    ["She has been studying", "वह पढ़ रही है", "vah paṛh rahī hai"],
                    ["We have been trying", "हम कोशिश कर रहे हैं", "ham kośiś kar rahe haiṃ"],
                    ["The issue has been raised", "मुद्दा उठा दिया गया है", "muddā uṭhā diyā gayā hai"],
                    ["Payment has been made", "भुगतान कर दिया गया है", "bhugtān kar diyā gayā hai"],
                    ["I had been ill", "मैं बीमार रहा था", "main bīmār rahā thā"],
                    ["They had been living there", "वे वहाँ रहते थे", "ve vahā̃ rahte the"],
                    ["By then I will have finished", "तब तक मैं खत्म कर चुका होऊँगा", "tab tak main khatm kar cukā hoū̃gā"],
                ],
            ),
        ],
    )


def chapter_541() -> dict:
    return _lesson(
        "Perfect continuous: रहा हूँ / रहा था with 'for/since' time: दो घंटे से पढ़ रहा हूँ.",
        "Emphasizes duration up to now/then.",
        [
            _p("Pattern", "Time phrase + से + progressive + auxiliary."),
            _t(
                "Perfect continuous",
                [
                    ["I have been reading for two hours", "मैं दो घंटे से पढ़ रहा हूँ", "main do ghaṃṭe se paṛh rahā hū̃"],
                    ["She has been singing", "वह गा रही है काफ़ी देर से", "vah gā rahī hai kāfī der se"],
                    ["We had been waiting", "हम इंतज़ार कर रहे थे", "ham intazār kar rahe the"],
                    ["They have been working since morning", "वे सुबह से काम कर रहे हैं", "ve subah se kām kar rahe haiṃ"],
                    ["He had been driving", "वह गाड़ी चला रहा था", "vah gāṛī calā rahā thā"],
                    ["I have been thinking", "मैं सोच रहा हूँ", "main soc rahā hū̃"],
                    ["It had been raining", "बारिश हो रही थी", "bāriś ho rahī thī"],
                    ["We will have been living here", "हम यहाँ रह रहे होंगे", "ham yahā̃ rah rahe hoṅge"],
                    ["She has been teaching for years", "वह सालों से पढ़ा रही है", "vah sālõ se paṛhā rahī hai"],
                    ["I was tired from walking", "मैं चलते चलते थक गया", "main calte calte thak gayā"],
                    ["He has been absent", "वह गायब है कुछ दिनों से", "vah gāyab hai kuch dinõ se"],
                    ["We have been friends", "हम दोस्त हैं बचपन से", "ham dost haiṃ bacpan se"],
                    ["The shop has been closed", "दुकान बंद है कल से", "dukān band hai kal se"],
                    ["I have been trying to call", "मैं फोन करने की कोशिश कर रहा हूँ", "main phon karne kī kośiś kar rahā hū̃"],
                    ["They had been arguing", "वे झगड़ रहे थे", "ve jhagaṛ rahe the"],
                    ["By May I will have been working", "मई तक मैं काम कर रहा होऊँगा", "maī tak main kām kar rahā hoū̃gā"],
                ],
            ),
        ],
    )


def chapter_542() -> dict:
    return _lesson(
        "नहीं negates fact; नहीं चाहिए / मन नहीं is 'don't want'; मत is imperative 'don't'.",
        "मुझे चाय नहीं चाहिए — I don't want tea. यह सच नहीं — it's not true.",
        [
            _p("Contrast", "नहीं खाता = does not eat; खाना नहीं चाहता = does not want to eat."),
            _t(
                "no / not vs don't want",
                [
                    ["I am not hungry", "मुझे भूख नहीं है", "mujhe bhūkh nahī̃ hai"],
                    ["I don't want food", "मुझे खाना नहीं चाहिए", "mujhe khānā nahī̃ cāhie"],
                    ["I don't like coffee", "मुझे कॉफ़ी पसंद नहीं", "mujhe kŏfī pasand nahī̃"],
                    ["I don't want coffee", "मुझे कॉफ़ी नहीं चाहिए", "mujhe kŏfī nahī̃ cāhie"],
                    ["He is not coming", "वह नहीं आ रहा", "vah nahī̃ ā rahā"],
                    ["He does not want to come", "वह नहीं आना चाहता", "vah nahī̃ ānā cāhtā"],
                    ["Not now", "अभी नहीं", "abhī nahī̃"],
                    ["I don't want it now", "मुझे अभी नहीं चाहिए", "mujhe abhī nahī̃ cāhie"],
                    ["This is not mine", "यह मेरा नहीं है", "yah merā nahī̃ hai"],
                    ["I don't want this", "मुझे यह नहीं चाहिए", "mujhe yah nahī̃ cāhie"],
                    ["She did not ask", "उसने नहीं पूछा", "usne nahī̃ pūchā"],
                    ["She did not want to ask", "वह पूछना नहीं चाहती थी", "vah pūchnā nahī̃ cāhtī thī"],
                    ["Don't go (command)", "मत जाओ", "mat jāo"],
                    ["I don't want you to go", "मैं नहीं चाहता कि तुम जाओ", "main nahī̃ cāhtā ki tum jāo"],
                    ["No problem", "कोई बात नहीं", "koī bāt nahī̃"],
                    ["I need nothing", "मुझे कुछ नहीं चाहिए", "mujhe kuch nahī̃ cāhie"],
                ],
            ),
        ],
    )


_GRAMMAR = {
    510: chapter_510,
    511: chapter_511,
    512: chapter_512,
    513: chapter_513,
    514: chapter_514,
    515: chapter_515,
    516: chapter_516,
    517: chapter_517,
    518: chapter_518,
    519: chapter_519,
    520: chapter_520,
    521: chapter_521,
    522: chapter_522,
    523: chapter_523,
    524: chapter_524,
    525: chapter_525,
    526: chapter_526,
    527: chapter_527,
    528: chapter_528,
    529: chapter_529,
    530: chapter_530,
    531: chapter_531,
    532: chapter_532,
    533: chapter_533,
    534: chapter_534,
    535: chapter_535,
    536: chapter_536,
    537: chapter_537,
    538: chapter_538,
    539: chapter_539,
    540: chapter_540,
    541: chapter_541,
    542: chapter_542,
}


def get_grammar_chapter(chapter_id: int) -> dict | None:
    fn = _GRAMMAR.get(chapter_id)
    return fn() if fn else None
