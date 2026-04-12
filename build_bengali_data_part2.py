# Chapters 510–662 for data_bengali.json (grammar, phrases, vocab, conversation)
from bengali_lesson_helpers import ch, r, block_table, blk_para, H, S


def add_grammar_phrases_vocab_conv(out):
    # --- 510–519 pronouns & tenses (sample-rich tables) ---
    out.append(
        ch(
            510,
            "Pronouns and Articles in Bengali",
            "Bengali pronouns: আমি (I), তুমি (you informal), আপনি (you formal), সে (he/she), এ (this), ও (that).",
            "No definite article; demonstratives এ/ও/সে often do article-like work.",
            blocks=[
                block_table(
                    "Pronouns",
                    [
                        r("I", "আমি", "Āmi"),
                        r("you (informal)", "তুমি", "Tumi"),
                        r("you (formal)", "আপনি", "Āpni"),
                        r("he / she", "সে", "Sē"),
                        r("we", "আমরা", "Āmrā"),
                        r("you (pl.)", "তোমরা", "Tōmrā"),
                        r("they", "তারা", "Tārā"),
                        r("this", "এটা", "Ēṭā"),
                        r("that", "ওটা", "Ōṭā"),
                        r("who", "কে", "Kē"),
                        r("what", "কী", "Ki"),
                        r("whose", "কার", "Kār"),
                        r("my", "আমার", "Āmār"),
                        r("your", "তোমার / আপনার", "Tōmār / Āpār"),
                        r("his / her", "তার", "Tār"),
                        r("some / something", "কিছু", "Kichhu"),
                        r("everyone", "সবাই", "Sôbāi"),
                        r("he / she (hon., present)", "তিনি", "Tini"),
                    ],
                )
            ],
        )
    )
    out.append(
        ch(
            511,
            "Using plurals to indicate respect in Bengali",
            "Formal address often uses plural verb forms with আপনি or honorific third person (তিনি).",
            "তিনি যান (he/she goes - honorific) vs সে যায় (neutral).",
            blocks=[
                block_table(
                    "Respect forms",
                    [
                        r("You (formal) go", "আপনি যান", "Āpni jān"),
                        r("He (hon.) is", "তিনি আছেন", "Tini āchen"),
                        r("They (hon.) will come", "তারা আসবেন", "Tārā āsbēn"),
                        r("Please sit", "বসুন", "Bôsun"),
                        r("Please eat", "খান", "Khān"),
                        r("Good morning (sir)", "সুপ্রভাত", "Suprobhāt"),
                        r("How are you?", "আপনি কেমন আছেন?", "Āpni kēmon āchen?"),
                        r("I am fine", "আমি ভালো আছি", "Āmi bhālō āchi"),
                        r("Thank you", "ধন্যবাদ", "Dhonyobād"),
                        r("Welcome", "স্বাগতম", "Swāgotom"),
                        r("Respected teacher", "শ্রদ্ধেয় শিক্ষক", "Shrôddhyēyo shikkhôk"),
                        r("Elder brother", "দাদা", "Dādā"),
                        r("Elder sister", "দিদি", "Didi"),
                        r("Grandfather", "দাদু", "Dādu"),
                        r("Grandmother", "ঠাকুমা", "Ṭhākumā"),
                        r("You (form.) will read", "আপনি পড়বেন", "Āpni pōṛben"),
                        r("He (hon.) went", "তিনি গেলেন", "Tini gēlen"),
                        r("Please come in", "ভিতরে আসুন", "Bhitore āsun"),
                    ],
                )
            ],
        )
    )
    out.append(
        ch(
            512,
            "Verbs in Bengali",
            "Verbs take endings for tense and person: করি, করো, করে, করেন (present of 'do').",
            "Learn common roots: করা, যাওয়া, খাওয়া, দেখা, বলা.",
            blocks=[
                block_table(
                    "Common verbs",
                    [
                        r("to do", "করা", "korā"),
                        r("to go", "যাওয়া", "jāōyā"),
                        r("to come", "আসা", "āsā"),
                        r("to eat", "খাওয়া", "khāōyā"),
                        r("to see", "দেখা", "dēkhā"),
                        r("to say", "বলা", "bolā"),
                        r("to read", "পড়া", "pōṛā"),
                        r("to write", "লেখা", "lēkhā"),
                        r("to give", "দেওয়া", "dēōyā"),
                        r("to take", "নেওয়া", "nēōyā"),
                        r("to sleep", "ঘুমানো", "ghumānō"),
                        r("to know", "জানা", "jānā"),
                        r("to understand", "বোঝা", "bōjhā"),
                        r("to want", "চাওয়া", "chāōyā"),
                        r("to like", "পছন্দ করা", "pôchondo korā"),
                        r("to play", "খেলা", "khelā"),
                        r("to run", "দৌড়ানো", "douṛānō"),
                        r("to listen", "শোনা", "shonā"),
                    ],
                )
            ],
        )
    )
    out.append(
        ch(
            513,
            "Simple Present Tense in Bengali",
            "Present habitual: আমি করি, তুমি করো, সে করে, আপনি করেন.",
            "Use করি for I, করো for informal you, করেন for formal you/he/she honorific.",
            blocks=[
                block_table(
                    "Present (to do)",
                    [
                        r("I do", "আমি করি", "Āmi kori"),
                        r("you do (inf.)", "তুমি করো", "Tumi koro"),
                        r("he/she does", "সে করে", "Sē kore"),
                        r("you do (form.)", "আপনি করেন", "Āpni kôren"),
                        r("we do", "আমরা করি", "Āmrā kori"),
                        r("they do", "তারা করে", "Tārā kore"),
                        r("I read", "আমি পড়ি", "Āmi pōṛi"),
                        r("I eat", "আমি খাই", "Āmi khāi"),
                        r("I go", "আমি যাই", "Āmi jāi"),
                        r("I come", "আমি আসি", "Āmi āsi"),
                        r("I see", "আমি দেখি", "Āmi dēkhi"),
                        r("I say", "আমি বলি", "Āmi boli"),
                        r("I know", "আমি জানি", "Āmi jāni"),
                        r("I want", "আমি চাই", "Āmi chāi"),
                        r("I understand", "আমি বুঝি", "Āmi bujhi"),
                        r("they read", "তারা পড়ে", "Tārā pōṛe"),
                        r("you (pl.) do", "তোমরা করো", "Tōmrā koro"),
                        r("he plays", "সে খেলে", "Sē khēlē"),
                    ],
                )
            ],
        )
    )
    out.append(
        ch(
            514,
            'Simple Present Tense of "To Be" in Bengali',
            "Copula: আছি (I am), আছো (you inf.), আছে (he/she), আছেন (formal).",
            "Often omitted in equational sentences: সে ছাত্র (he student).",
            blocks=[
                block_table(
                    "To be (location/state)",
                    [
                        r("I am (here)", "আমি আছি", "Āmi āchi"),
                        r("you are (inf.)", "তুমি আছো", "Tumi āchho"),
                        r("he/she is", "সে আছে", "Sē āchhe"),
                        r("you are (form.)", "আপনি আছেন", "Āpni āchen"),
                        r("we are", "আমরা আছি", "Āmrā āchi"),
                        r("they are", "তারা আছে", "Tārā āchhe"),
                        r("I am fine", "আমি ভালো আছি", "Āmi bhālō āchi"),
                        r("It is good", "ভালো", "Bhālō"),
                        r("This is a book", "এটা বই", "Ēṭā bôi"),
                        r("That is a house", "ওটা বাড়ি", "Ōṭā bāṛi"),
                        r("I am a student", "আমি ছাত্র", "Āmi chātrô"),
                        r("She is a teacher", "সে শিক্ষিকা", "Sē shikkhikā"),
                        r("We are friends", "আমরা বন্ধু", "Āmrā bondhu"),
                        r("They are here", "তারা এখানে", "Tārā ēkhāne"),
                        r("Where are you?", "তুমি কোথায়?", "Tumi kōthāy?"),
                        r("Are you there?", "তুমি আছো?", "Tumi āchho?"),
                        r("I am here", "আমি এখানে আছি", "Āmi ēkhāne āchi"),
                        r("There is no problem", "কোনো সমস্যা নেই", "Kōnō shomosshā nēi"),
                    ],
                )
            ],
        )
    )
    out.append(
        ch(
            515,
            "Present Continuous Tense in Bengali",
            "Structure: আমি করছি (I am doing), তুমি করছো, সে করছে.",
            "Also: যাচ্ছি (I am going) from যাওয়া.",
            blocks=[
                block_table(
                    "Continuous",
                    [
                        r("I am doing", "আমি করছি", "Āmi korchhi"),
                        r("you are doing", "তুমি করছো", "Tumi korchho"),
                        r("he is doing", "সে করছে", "Sē korchhe"),
                        r("I am eating", "আমি খাচ্ছি", "Āmi khāchchhi"),
                        r("I am reading", "আমি পড়ছি", "Āmi pōṛchhi"),
                        r("I am going", "আমি যাচ্ছি", "Āmi jāchchhi"),
                        r("I am coming", "আমি আসছি", "Āmi āschhi"),
                        r("I am sleeping", "আমি ঘুমাচ্ছি", "Āmi ghumāchchhi"),
                        r("We are waiting", "আমরা অপেক্ষা করছি", "Āmrā ôpekhshā korchhi"),
                        r("They are talking", "তারা কথা বলছে", "Tārā kōthā bolchhe"),
                        r("It is raining", "বৃষ্টি পড়ছে", "Briṣṭi pōṛchhe"),
                        r("What are you doing?", "তুমি কী করছো?", "Tumi ki korchho?"),
                        r("I am working", "আমি কাজ করছি", "Āmi kāj korchhi"),
                        r("She is cooking", "সে রান্না করছে", "Sē rānnā korchhe"),
                        r("He is driving", "সে গাড়ি চালাচ্ছে", "Sē gāṛi chālāchchhe"),
                        r("We are leaving", "আমরা চলে যাচ্ছি", "Āmrā chōlē jāchchhi"),
                        r("I am listening", "আমি শুনছি", "Āmi shunchhi"),
                        r("They are studying", "তারা পড়ছে", "Tārā pōṛchhe"),
                    ],
                )
            ],
        )
    )
    out.append(
        ch(
            516,
            "Simple Future Tense in Bengali",
            "Future: করব (I will do), করবে (he/she), করবেন (formal).",
            "Also চলে যাবে (will go) patterns.",
            blocks=[
                block_table(
                    "Future",
                    [
                        r("I will do", "আমি করব", "Āmi korbo"),
                        r("you will do", "তুমি করবে", "Tumi korbe"),
                        r("he will do", "সে করবে", "Sē korbe"),
                        r("you will (form.)", "আপনি করবেন", "Āpni kôrben"),
                        r("we will go", "আমরা যাব", "Āmrā jābo"),
                        r("I will come", "আমি আসব", "Āmi āshbo"),
                        r("I will eat", "আমি খাব", "Āmi khābo"),
                        r("I will see", "আমি দেখব", "Āmi dēkhbō"),
                        r("It will rain", "বৃষ্টি হবে", "Briṣṭi hōbe"),
                        r("Tomorrow I will leave", "আমি কাল যাব", "Āmi kāl jābo"),
                        r("We will meet", "আমরা দেখা করব", "Āmrā dēkhā korbo"),
                        r("They will come", "তারা আসবে", "Tārā āshbe"),
                        r("I will help", "আমি সাহায্য করব", "Āmi sāhājjo korbo"),
                        r("She will call", "সে ফোন করবে", "Sē phōn korbe"),
                        r("Don't worry", "চিন্তা করবেন না", "Chinta kôrben nā"),
                        r("I will read", "আমি পড়ব", "Āmi pōṛbō"),
                        r("You will be fine", "তুমি ঠিক থাকবে", "Tumi ṭhik thākbe"),
                        r("We will meet again", "আমরা আবার দেখা করব", "Āmrā ābār dēkhā korbo"),
                    ],
                )
            ],
        )
    )
    out.append(
        ch(
            517,
            "Future Continuous Tense in Bengali",
            "Less common; often use future + সময় (time) or করতে থাকব.",
            "Colloquial: যাচ্ছি আবার (I will keep going).",
            blocks=[
                block_table(
                    "Future continuous style",
                    [
                        r("I will be working", "আমি কাজ করতে থাকব", "Āmi kāj korte thākbo"),
                        r("I will be reading", "আমি পড়তে থাকব", "Āmi pōṛte thākbo"),
                        r("He will be waiting", "সে অপেক্ষা করতে থাকবে", "Sē ôpekhshā korte thākbe"),
                        r("They will be coming", "তারা আসতে থাকবে", "Tārā āste thākbe"),
                        r("I will be there", "আমি সেখানে থাকব", "Āmi shēkhāne thākbo"),
                        r("We will be late", "আমরা দেরি করব", "Āmrā dēri korbo"),
                        r("It will be raining", "বৃষ্টি হচ্ছে থাকবে", "Briṣṭi hochchhe thākbe"),
                        r("She will be cooking", "সে রান্না করতে থাকবে", "Sē rānnā korte thākbe"),
                        r("I will keep trying", "আমি চেষ্টা করতে থাকব", "Āmi chēṣṭā korte thākbo"),
                        r("You will be fine", "তুমি ঠিক থাকবে", "Tumi ṭhik thākbe"),
                        r("This will continue", "এটা চলতে থাকবে", "Ēṭā cholte thākbe"),
                        r("Meeting will go on", "মিটিং চলবে", "Miṭiṃ cholbe"),
                        r("Train will be running", "ট্রেন চলবে", "Ṭrēn cholbe"),
                        r("I will be learning", "আমি শিখতে থাকব", "Āmi shikhte thākbo"),
                        r("We will be ready", "আমরা প্রস্তুত থাকব", "Āmrā prôstut thākbo"),
                        r("You will be waiting", "তুমি অপেক্ষা করতে থাকবে", "Tumi ôpekhshā korte thākbe"),
                        r("I will be there", "আমি সেখানে থাকব", "Āmi shēkhāne thākbo"),
                        r("It will be fine", "ঠিক হবে", "Ṭhik hōbe"),
                    ],
                )
            ],
        )
    )
    out.append(
        ch(
            518,
            'Simple Past Tense in Bengali – Part 1 (Verbs without object)',
            "Past: গেলাম (I went), গেলি (you inf.), গেল (he/she), গেলেন (formal).",
            "Intransitive past uses গেলাম pattern for যাওয়া.",
            blocks=[
                block_table(
                    "Past intransitive",
                    [
                        r("I went", "আমি গেলাম", "Āmi gēlām"),
                        r("you went (inf.)", "তুমি গেলি", "Tumi gēli"),
                        r("he went", "সে গেল", "Sē gēl"),
                        r("you went (form.)", "আপনি গেলেন", "Āpni gēlen"),
                        r("I came", "আমি এলাম", "Āmi ēlām"),
                        r("I slept", "আমি ঘুমালাম", "Āmi ghumālām"),
                        r("I sat", "আমি বসলাম", "Āmi bôshlām"),
                        r("I stood", "আমি দাঁড়ালাম", "Āmi dãṛālām"),
                        r("I ran", "আমি দৌড়ালাম", "Āmi douṛālām"),
                        r("We went", "আমরা গেলাম", "Āmrā gēlām"),
                        r("They came", "তারা এলো", "Tārā ēlō"),
                        r("He arrived", "সে পৌঁছাল", "Sē poũchhāl"),
                        r("When did you go?", "তুমি কখন গেলি?", "Tumi kôkhon gēli?"),
                        r("I went yesterday", "আমি গতকাল গেলাম", "Āmi gôtokāl gēlām"),
                        r("She left early", "সে তাড়াতাড়ি চলে গেল", "Sē ṭāṛāṭāṛi chōlē gēl"),
                        r("I fell", "আমি পড়ে গেলাম", "Āmi pōṛē gēlām"),
                        r("We slept", "আমরা ঘুমালাম", "Āmrā ghumālām"),
                        r("I returned", "আমি ফিরলাম", "Āmi phirlām"),
                    ],
                )
            ],
        )
    )
    out.append(
        ch(
            519,
            'Simple Past Tense in Bengali – Part 2 (Verbs with object)',
            "Transitive past often uses করেছিলাম / করলাম: আমি বইটি পড়লাম.",
            "Perfect style: আমি খেয়েছি (I have eaten).",
            blocks=[
                block_table(
                    "Past transitive",
                    [
                        r("I read the book", "আমি বইটি পড়লাম", "Āmi bôiṭi pōṛlām"),
                        r("I ate rice", "আমি ভাত খেলাম", "Āmi bhāt khēlām"),
                        r("I did the work", "আমি কাজ করলাম", "Āmi kāj korlām"),
                        r("I saw him", "আমি তাকে দেখলাম", "Āmi tākē dēkhlām"),
                        r("you wrote (inf.)", "তুমি লিখলে", "Tumi likhle"),
                        r("he bought", "সে কিনল", "Sē kinlō"),
                        r("she opened", "সে খুলল", "Sē khullō"),
                        r("we finished", "আমরা শেষ করলাম", "Āmrā shēsh korlām"),
                        r("they built", "তারা বানালো", "Tārā bānālō"),
                        r("I gave money", "আমি টাকা দিলাম", "Āmi ṭākā dilām"),
                        r("I took the bus", "আমি বাস নিলাম", "Āmi bās nilām"),
                        r("He closed the door", "সে দরজা বন্ধ করল", "Sē dôrjā bondho korlō"),
                        r("What did you do?", "তুমি কী করলে?", "Tumi ki korle?"),
                        r("I met him", "আমি তার সাথে দেখা করলাম", "Āmi tār sāthe dēkhā korlām"),
                        r("She called me", "সে আমাকে ফোন করল", "Sē āmākē phōn korlō"),
                        r("I drank water", "আমি জল খেলাম", "Āmi jol khēlām"),
                        r("I opened the door", "আমি দরজা খুললাম", "Āmi dôrjā khullām"),
                        r("She wrote a letter", "সে চিঠি লিখল", "Sē chiṭhi likhlō"),
                    ],
                )
            ],
        )
    )
    from build_bengali_data_rest import add_chapters_520_662

    add_chapters_520_662(out)
