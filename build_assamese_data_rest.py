# Remaining Bengali lessons 520–662 (grammar tail, phrases, vocab, conversation)
from assamese_lesson_helpers import ch, r, block_table, blk_para, H, S


def _b(cid, title, content, intro, rows, heading="Examples"):
    return ch(cid, title, content, intro, blocks=[block_table(heading, rows)])


def add_chapters_520_662(out):
    # 520–529
    out.append(
        ch(
            520,
            'Simple Past Tense in Bengali – Part 3 (Past tense of "to be")',
            "Was/were: ছিলাম, ছিলি, ছিল, ছিলেন.",
            "আমি ছিলাম (I was), সে ছিল (he/she was).",
            blocks=[
                block_table(
                    "Past of to be",
                    [
                        r("I was", "আমি ছিলাম", "Āmi chhilām"),
                        r("you were (inf.)", "তুমি ছিলি", "Tumi chhili"),
                        r("he/she was", "সে ছিল", "Sē chhil"),
                        r("you were (form.)", "আপনি ছিলেন", "Āpni chhilen"),
                        r("we were", "আমরা ছিলাম", "Āmrā chhilām"),
                        r("they were", "তারা ছিল", "Tārā chhil"),
                        r("I was at home", "আমি বাড়িতে ছিলাম", "Āmi bāṛite chhilām"),
                        r("It was good", "ভালো ছিল", "Bhālō chhil"),
                        r("That was yesterday", "সেটা গতকাল ছিল", "Sēṭā gôtokāl chhil"),
                        r("We were friends", "আমরা বন্ধু ছিলাম", "Āmrā bondhu chhilām"),
                        r("She was ill", "সে অসুস্থ ছিল", "Sē ôsustho chhil"),
                        r("He was late", "সে দেরিতে ছিল", "Sē dērite chhil"),
                        r("Were you there?", "তুমি সেখানে ছিলে?", "Tumi shēkhāne chhile?"),
                        r("I was busy", "আমি ব্যস্ত ছিলাম", "Āmi bēsto chhilām"),
                        r("They were happy", "তারা খুশি ছিল", "Tārā khushi chhil"),
                        r("They were students", "তারা ছাত্র ছিল", "Tārā chātrô chhil"),
                        r("I was ready", "আমি প্রস্তুত ছিলাম", "Āmi prôstut chhilām"),
                        r("It was cold", "ঠান্ডা ছিল", "Ṭhāṇḍā chhil"),
                    ],
                )
            ],
        )
    )
    out.append(
        _b(
            521,
            "Exceptional Verbs in Bengali which change in past tense form",
            "Some verbs have suppletive or irregular past: যাওয়া→গেল, আসা→এল, দেওয়া→দিল.",
            "Memorize common pairs.",
            [
                r("went", "গেল", "gēl"),
                r("came", "এল", "ēl"),
                r("gave", "দিল", "dil"),
                r("took", "নিল", "nil"),
                r("said", "বলল", "bôllō"),
                r("saw", "দেখল", "dēkhlō"),
                r("ate", "খেল", "khēl"),
                r("did", "করল", "korlō"),
                r("I went", "আমি গেলাম", "Āmi gēlām"),
                r("I came", "আমি এলাম", "Āmi ēlām"),
                r("I gave", "আমি দিলাম", "Āmi dilām"),
                r("he took", "সে নিল", "Sē nil"),
                r("she said", "সে বলল", "Sē bôllō"),
                r("we saw", "আমরা দেখলাম", "Āmrā dēkhlām"),
                r("they ate", "তারা খেল", "Tārā khēl"),
                r("I thought", "আমি ভাবলাম", "Āmi bhablām"),
                r("He fell", "সে পড়ল", "Sē pōṛlō"),
                r("We sat", "আমরা বসলাম", "Āmrā bôshlām"),
            ],
            "Irregular style",
        )
    )
    out.append(
        _b(
            522,
            "Past Continuous Tense in Bengali",
            "ছিল + করছিলাম pattern: আমি করছিলাম (I was doing).",
            "Common in narrative.",
            [
                r("I was doing", "আমি করছিলাম", "Āmi korchhilām"),
                r("you were doing", "তুমি করছিলে", "Tumi korchhile"),
                r("he was reading", "সে পড়ছিল", "Sē pōṛchhil"),
                r("she was cooking", "সে রান্না করছিল", "Sē rānnā korchhil"),
                r("we were waiting", "আমরা অপেক্ষা করছিলাম", "Āmrā ôpekhshā korchhilām"),
                r("they were talking", "তারা কথা বলছিল", "Tārā kōthā bolchhil"),
                r("It was raining", "বৃষ্টি পড়ছিল", "Briṣṭi pōṛchhil"),
                r("I was sleeping", "আমি ঘুমাচ্ছিলাম", "Āmi ghumāchchhilām"),
                r("He was driving", "সে গাড়ি চালাচ্ছিল", "Sē gāṛi chālāchchhil"),
                r("What were you doing?", "তুমি কী করছিলে?", "Tumi ki korchhile?"),
                r("I was at work", "আমি কাজে ছিলাম", "Āmi kāje chhilām"),
                r("We were late", "আমরা দেরি করছিলাম", "Āmrā dēri korchhilām"),
                r("Sun was setting", "সূর্য অস্ত যাচ্ছিল", "Sūryo ôsto jāchchhil"),
                r("Birds were singing", "পাখি গাইছিল", "Pākhi gāichhil"),
                r("Children were playing", "বাচ্চারা খেলছিল", "Bāchchārā khēlchhil"),
                r("I was thinking", "আমি ভাবছিলাম", "Āmi bhabchhilām"),
                r("The phone was ringing", "ফোন বাজছিল", "Phōn bājchhil"),
                r("You were right", "তুমি ঠিক বলছিলে", "Tumi ṭhik bolchhile"),
            ],
        )
    )
    out.append(
        _b(
            523,
            "Present/Past/Future Perfect Tense in Bengali",
            "Use করেছি / করেছিলাম / করব with auxiliary nuances; often same as English perfect with context.",
            "Colloquial: খেয়েছি (I have eaten).",
            [
                r("I have eaten", "আমি খেয়েছি", "Āmi khēyēchhi"),
                r("I had gone", "আমি গিয়েছিলাম", "Āmi giyēchhilām"),
                r("I will have done", "আমি করে ফেলব", "Āmi kōre phelbo"),
                r("He has come", "সে এসেছে", "Sē ēsechhe"),
                r("She has left", "সে চলে গেছে", "Sē chōlē gēchhe"),
                r("We have finished", "আমরা শেষ করেছি", "Āmrā shēsh korechhi"),
                r("They had arrived", "তারা পৌঁছেছিল", "Tārā poũchhēchhil"),
                r("I have seen", "আমি দেখেছি", "Āmi dēkhēchhi"),
                r("You have tried", "তুমি চেষ্টা করেছো", "Tumi chēṣṭā korechho"),
                r("By then I will have gone", "তখন আমি চলে যাব", "Tokhon āmi chōlē jābo"),
                r("Have you read?", "তুমি পড়েছো?", "Tumi pōṛechho?"),
                r("I had not known", "আমি জানতাম না", "Āmi jāntām nā"),
                r("She has learned", "সে শিখেছে", "Sē shikhēchhe"),
                r("We have agreed", "আমরা রাজি হয়েছি", "Āmrā rāji hōyechhi"),
                r("He will have left", "সে চলে যাবে", "Sē chōlē jābe"),
                r("I have understood", "আমি বুঝেছি", "Āmi bujhechhi"),
                r("They have gone", "তারা চলে গেছে", "Tārā chōlē gēchhe"),
                r("I had forgotten", "আমি ভুলে গিয়েছিলাম", "Āmi bhule giyēchilām"),
            ],
        )
    )
    out.append(
        _b(
            524,
            "Learn Prepositions in Bengali",
            "Common: এ (in), থেকে (from), সঙ্গে (with), উপরে (on), নিচে (under).",
            "Postpositions often follow noun: বাড়িতে (at home).",
            [
                r("in the house", "বাড়িতে", "bāṛite"),
                r("on the table", "টেবিলে", "ṭēbile"),
                r("under the tree", "গাছের নিচে", "gāchher nīche"),
                r("with me", "আমার সঙ্গে", "āmār songe"),
                r("from Kolkata", "কলকাতা থেকে", "Kolkātā theke"),
                r("to school", "স্কুলে", "sḳule"),
                r("near the bank", "ব্যাংকের কাছে", "bēṅkēr kāchhe"),
                r("between us", "আমাদের মধ্যে", "āmādēr môdhye"),
                r("before evening", "সন্ধ্যার আগে", "sondhyār āgē"),
                r("after lunch", "লাঞ্চের পরে", "lāñcher pōre"),
                r("without money", "টাকা ছাড়া", "ṭākā chhāṛā"),
                r("for you", "তোমার জন্য", "tōmār jônyo"),
                r("about this", "এটা নিয়ে", "ēṭā niyē"),
                r("inside the room", "ঘরের ভিতরে", "ghorer bhitore"),
                r("outside", "বাইরে", "bāire"),
                r("behind the house", "বাড়ির পিছনে", "bāṛir pichhōne"),
                r("in front of the school", "স্কুলের সামনে", "sḳulēr sāmne"),
                r("across the river", "নদীর ওপারে", "nodīr opārē"),
            ],
        )
    )
    out.append(
        _b(
            525,
            'Preposition "TO" in Bengali',
            "Goal/direction: এ (to place), কাছে (towards someone), এর দিকে (towards).",
            "যাওয়া takes destination in dative/locative style.",
            [
                r("go to school", "স্কুলে যাওয়া", "sḳule jāōyā"),
                r("come to me", "আমার কাছে আসা", "āmār kāchhe āsā"),
                r("give to him", "তাকে দেওয়া", "tākē dēōyā"),
                r("send to Delhi", "দিল্লি পাঠানো", "Dilli pāṭhānō"),
                r("talk to her", "তার সঙ্গে কথা বলা", "tār songe kōthā bolā"),
                r("listen to the news", "খবর শোনা", "khôbor shonā"),
                r("reply to the letter", "চিঠির জবাব দেওয়া", "chithir jobāb dēōyā"),
                r("equal to five", "পাঁচের সমান", "pā̃cher somān"),
                r("next to the shop", "দোকানের পাশে", "dokāner pāshe"),
                r("I go to work", "আমি কাজে যাই", "Āmi kāje jāi"),
                r("She came to us", "সে আমাদের কাছে এল", "Sē āmādēr kāchhe ēl"),
                r("Write to me", "আমাকে লেখো", "Āmākē likhō"),
                r("Point to the map", "মানচিত্রে দেখাও", "māncitre dēkhāō"),
                r("Stick to the plan", "পরিকল্পনায় থাকো", "pôrikolponāy thākō"),
                r("Road to the station", "স্টেশনের রাস্তা", "sṭēshonēr rāstā"),
                r("Bring it to me", "আমার কাছে এনে দাও", "Āmār kāchhe ēnē dāo"),
                r("I will go to you", "আমি তোমার কাছে যাব", "Āmi tōmār kāchhe jābo"),
                r("Send this to him", "এটা তাকে পাঠাও", "Ēṭā tākē pāṭhāo"),
            ],
        )
    )
    out.append(
        _b(
            526,
            "Sentences with person or living things as object in Bengali",
            "Animate objects take কে: আমি তাকে দেখি (I see him).",
            "Use করে for respect where needed.",
            [
                r("I see him", "আমি তাকে দেখি", "Āmi tākē dēkhi"),
                r("I know her", "আমি তাকে চিনি", "Āmi tākē chini"),
                r("We helped them", "আমরা তাদের সাহায্য করলাম", "Āmrā tādēr sāhājjo korlām"),
                r("Call the doctor", "ডাক্তারকে ডাকুন", "Ḍāktārke ḍākun"),
                r("Tell your mother", "তোমার মাকে বলো", "Tōmār mākē bōlō"),
                r("I met your brother", "আমি তোমার ভাইয়ের সাথে দেখা করলাম", "Āmi tōmār bhāiēr sāthe dēkhā korlām"),
                r("She loves the child", "সে বাচ্চাটিকে ভালোবাসে", "Sē bāchchāṭikē bhālōbāsē"),
                r("They invited us", "তারা আমাদের আমন্ত্রণ করল", "Tārā āmādēr āmôntroṇ korlō"),
                r("Find the teacher", "শিক্ষককে খুঁজুন", "Shikkhôkke khun̐jun"),
                r("I forgot him", "আমি তাকে ভুলে গেছি", "Āmi tākē bhulē gēchhi"),
                r("Help the old man", "বৃদ্ধকে সাহায্য করুন", "br̥ddhoke sāhājjo kôrun"),
                r("Show the guest", "অতিথিকে দেখান", "ôtithikē dēkhān"),
                r("Ask the officer", "অফিসারকে জিজ্ঞাসা করুন", "ôphisārke jijñāsā kôrun"),
                r("I trust you", "আমি তোমাকে বিশ্বাস করি", "Āmi tōmākē bishbās kori"),
                r("We remember them", "আমরা তাদের মনে রাখি", "Āmrā tādēr mōne rākhi"),
                r("I taught the child", "আমি বাচ্চাকে শিখিয়েছি", "Āmi bāchchākē shikhiyechhi"),
                r("He praised her", "সে তাকে প্রশংসা করল", "Sē tākē prôshôngsā korlō"),
                r("Find the nurse", "নার্সকে খুঁজুন", "Nārske khun̐jun"),
            ],
        )
    )
    out.append(
        _b(
            527,
            "Saying My/His/Her in Bengali",
            "Possessives: আমার, তোমার, তার, আপনার, আমাদের.",
            "Pronoun + noun: আমার বই (my book).",
            [
                r("my book", "আমার বই", "āmār bôi"),
                r("your pen", "তোমার কলম", "tōmār kolom"),
                r("his house", "তার বাড়ি", "tār bāṛi"),
                r("her mother", "তার মা", "tār mā"),
                r("our school", "আমাদের স্কুল", "āmādēr sḳul"),
                r("their car", "তাদের গাড়ি", "tādēr gāṛi"),
                r("my name", "আমার নাম", "āmār nām"),
                r("your address", "তোমার ঠিকানা", "tōmār ṭhikānā"),
                r("his idea", "তার ধারণা", "tār dhārôṇā"),
                r("her friend", "তার বন্ধু", "tār bondhu"),
                r("This is mine", "এটা আমার", "Ēṭā āmār"),
                r("That is yours", "ওটা তোমার", "Ōṭā tōmār"),
                r("Our teacher", "আমাদের শিক্ষক", "āmādēr shikkhôk"),
                r("Their problem", "তাদের সমস্যা", "tādēr shomosshā"),
                r("My parents", "আমার বাবা-মা", "āmār bābā-mā"),
                r("your sister", "তোমার বোন", "tōmār bōn"),
                r("his brother", "তার ভাই", "tār bhāi"),
                r("our village", "আমাদের গ্রাম", "āmādēr grām"),
            ],
        )
    )
    out.append(
        _b(
            528,
            'Basic questions and "WH" questions in Bengali',
            "কী, কে, কোথায়, কখন, কেন, কীভাবে.",
            "Question word often first: তুমি কোথায় যাও?",
            [
                r("What is this?", "এটা কী?", "Ēṭā ki?"),
                r("Who is he?", "সে কে?", "Sē kē?"),
                r("Where do you live?", "তুমি কোথায় থাকো?", "Tumi kōthāy thākō?"),
                r("When will you come?", "তুমি কখন আসবে?", "Tumi kôkhon āshbe?"),
                r("Why are you late?", "তুমি দেরি কেন?", "Tumi dēri kēn?"),
                r("How are you?", "তুমি কেমন আছো?", "Tumi kēmon āchho?"),
                r("How much?", "কত?", "Kôt?"),
                r("Which book?", "কোন বই?", "Kōn bôi?"),
                r("Whose bag?", "কার ব্যাগ?", "Kār bēg?"),
                r("What time?", "কটায়?", "Koṭāy?"),
                r("What happened?", "কী হয়েছে?", "Ki hōyēchhe?"),
                r("Do you know?", "তুমি জানো?", "Tumi jānō?"),
                r("Can you help?", "তুমি কি সাহায্য করতে পারো?", "Tumi ki sāhājjo korte pārō?"),
                r("Is it true?", "সেটা কি সত্যি?", "Sēṭā ki sôttyi?"),
                r("Any questions?", "কোনো প্রশ্ন?", "Kōnō prôshno?"),
                r("Where from?", "কোথা থেকে?", "Kōthā theke?"),
                r("How many?", "কয়টা?", "Kôyṭā?"),
                r("What for?", "কী জন্য?", "Ki jônyo?"),
            ],
        )
    )
    out.append(
        _b(
            529,
            "Negative Sentences – Present tense in Bengali",
            "না / নই / নেই: আমি যাই না (I don't go), নেই = there isn't.",
            "নই for copula negation in some contexts.",
            [
                r("I don't go", "আমি যাই না", "Āmi jāi nā"),
                r("I don't know", "আমি জানি না", "Āmi jāni nā"),
                r("I don't eat meat", "আমি মাংস খাই না", "Āmi māṅsō khāi nā"),
                r("He doesn't come", "সে আসে না", "Sē āse nā"),
                r("She doesn't speak", "সে বলে না", "Sē bōle nā"),
                r("We don't agree", "আমরা রাজি নই", "Āmrā rāji nôi"),
                r("They don't understand", "তারা বোঝে না", "Tārā bōjhe nā"),
                r("There is no time", "সময় নেই", "Somoy nēi"),
                r("No problem", "কোনো সমস্যা নেই", "Kōnō shomosshā nēi"),
                r("I don't want", "আমি চাই না", "Āmi chāi nā"),
                r("Don't worry", "চিন্তা করো না", "Chinta koro nā"),
                r("Don't shout", "চেঁচিয়ো না", "Chẽchiyō nā"),
                r("I am not tired", "আমি ক্লান্ত নই", "Āmi klānto nôi"),
                r("It is not far", "এটা দূর নয়", "Ēṭā dūr nôy"),
                r("We are not ready", "আমরা প্রস্তুত নই", "Āmrā prôstut nôi"),
                r("I don't like it", "আমার ভালো লাগে না", "Āmār bhālō lāgē nā"),
                r("He doesn't know", "সে জানে না", "Sē jānē nā"),
                r("I don't remember", "আমার মনে নেই", "Āmār mōne nēi"),
            ],
        )
    )
    out.append(
        _b(
            530,
            "Negative Sentences – Past tense in Bengali",
            "না / হয়নি: আমি যাইনি (I did not go).",
            "খাইনি (I did not eat).",
            [
                r("I did not go", "আমি যাইনি", "Āmi jāini"),
                r("I did not see", "আমি দেখিনি", "Āmi dēkhini"),
                r("He did not call", "সে ফোন করেনি", "Sē phōn kōreni"),
                r("We did not agree", "আমরা রাজি হইনি", "Āmrā rāji hoini"),
                r("She was not there", "সে সেখানে ছিল না", "Sē shēkhāne chhil nā"),
                r("They did not come", "তারা আসেনি", "Tārā āsēni"),
                r("I had no money", "আমার টাকা ছিল না", "Āmār ṭākā chhil nā"),
                r("It did not work", "কাজ হয়নি", "Kāj hōyni"),
                r("Nobody came", "কেউ আসেনি", "Keu āsēni"),
                r("I never said", "আমি বলিনি", "Āmi bolini"),
                r("He did not listen", "সে শোনেনি", "Sē shōnēni"),
                r("We could not finish", "আমরা শেষ করতে পারিনি", "Āmrā shēsh korte pārini"),
                r("She did not reply", "সে জবাব দিল না", "Sē jobāb dil nā"),
                r("No one knew", "কেউ জানত না", "Keu jānto nā"),
                r("I was not afraid", "আমি ভয় পাইনি", "Āmi bhôy pāini"),
                r("I did not eat", "আমি খাইনি", "Āmi khāini"),
                r("She did not reply", "সে উত্তর দিল না", "Sē uttor dil nā"),
                r("We did not know", "আমরা জানতাম না", "Āmrā jāntām nā"),
            ],
        )
    )
    out.append(
        _b(
            531,
            "Negative Sentence – Future Tense in Bengali",
            "Future negation: করব না, যাব না, হবে না.",
            "আমি আসব না (I will not come).",
            [
                r("I will not go", "আমি যাব না", "Āmi jābo nā"),
                r("I will not tell", "আমি বলব না", "Āmi bolbo nā"),
                r("He will not come", "সে আসবে না", "Sē āshbe nā"),
                r("We will not wait", "আমরা অপেক্ষা করব না", "Āmrā ôpekhshā korbo nā"),
                r("It will not rain", "বৃষ্টি হবে না", "Briṣṭi hōbe nā"),
                r("She will not agree", "সে রাজি হবে না", "Sē rāji hōbe nā"),
                r("They will not pay", "তারা দেবে না", "Tārā dēbe nā"),
                r("I will never forget", "আমি ভুলব না", "Āmi bhulbo nā"),
                r("Don't be late", "দেরি করবে না", "Dēri korbe nā"),
                r("We won't stop", "আমরা থামব না", "Āmrā thāmobo nā"),
                r("He won't leave", "সে যাবে না", "Sē jābe nā"),
                r("No one will know", "কেউ জানবে না", "Keu jānbe nā"),
                r("I won't give up", "আমি হার মানব না", "Āmi hār mānbo nā"),
                r("This won't work", "এটা হবে না", "Ēṭā hōbe nā"),
                r("Tomorrow I won't be free", "কাল আমি ফাঁকা থাকব না", "Kāl āmi phãkā thākbo nā"),
                r("I will not eat", "আমি খাব না", "Āmi khābo nā"),
                r("He will not go", "সে যাবে না", "Sē jābe nā"),
                r("We will not forget", "আমরা ভুলব না", "Āmrā bhulbo nā"),
            ],
        )
    )
    # 532–542: explicit topic tables (15–20 sentences each; see Vaia / standard Bangla grammar)
    out.append(
        _b(
            532,
            "Working with nouns – Gender & Plurals in Bengali",
            "Many nouns are unmarked for gender; humans and some animals use ছেলে/মেয়ে; plural often -রা or -গুলো.",
            "ছেলেরা খেলছে (the boys are playing); গরু (cow) has no natural gender suffix in the noun.",
            [
                r("the boy", "ছেলেটা", "chēlēṭā"),
                r("the girl", "মেয়েটা", "mēẏēṭā"),
                r("the boys", "ছেলেরা", "chēlērā"),
                r("the girls", "মেয়েরা", "mēẏērā"),
                r("the children", "বাচ্চারা", "bāchchārā"),
                r("the teachers", "শিক্ষকরা", "shikkhôkrā"),
                r("the students", "ছাত্ররা", "chātrôrā"),
                r("cows", "গরুগুলো", "gorugulō"),
                r("trees", "গাছগুলো", "gāchgulō"),
                r("books", "বইগুলো", "bôigulō"),
                r("The boys are playing", "ছেলেরা খেলছে", "Chēlērā khelchhe"),
                r("The girls are singing", "মেয়েরা গাইছে", "Mēẏērā gāichhe"),
                r("Those are my books", "ওগুলো আমার বই", "Ōgulō āmār bôi"),
                r("These flowers are beautiful", "এই ফুলগুলো সুন্দর", "Ei phulgulō sundor"),
                r("People are waiting", "মানুষজন অপেক্ষা করছে", "Mānuṣjôn ôpekhshā korchhe"),
                r("The sisters came", "বোনেরা এল", "Bōnērā ēl"),
                r("The brothers are tall", "ভাইয়েরা লম্বা", "Bhāiērā lombā"),
                r("Many students passed", "অনেক ছাত্র পাস করেছে", "Ônek chātrô pās korechhe"),
            ],
            "Gender & plural",
        )
    )
    out.append(
        _b(
            533,
            "Working with nouns – Prepositions in Bengali",
            "Postpositions follow the noun: বাড়িতে (at home), টেবিলের উপরে (on the table).",
            "Use এ/য়ে/te for locative and genitive chains as in textbooks.",
            [
                r("at home", "বাড়িতে", "bāṛite"),
                r("in the room", "ঘরে", "ghore"),
                r("on the table", "টেবিলের উপরে", "ṭēbilēr upore"),
                r("under the tree", "গাছের নিচে", "gāchher nīche"),
                r("near the bank", "ব্যাংকের কাছে", "bēṅkēr kāchhe"),
                r("between us", "আমাদের মধ্যে", "āmādēr môdhye"),
                r("before noon", "আগে দুপুর", "āgē dupur"),
                r("after school", "স্কুলের পর", "sḳulēr por"),
                r("The book is on the table", "বইটা টেবিলের উপরে", "Bôiṭā ṭēbilēr upore"),
                r("The cat is under the chair", "বিড়ালটা চেয়ারের নিচে", "Biṛālṭā cheẏārēr nīche"),
                r("I live in Kolkata", "আমি কলকাতায় থাকি", "Āmi Kolkātāy thāki"),
                r("He sits beside me", "সে আমার পাশে বসে", "Sē āmār pāshe bôse"),
                r("We met at the station", "আমরা স্টেশনে দেখা করলাম", "Āmrā sṭēshone dēkhā korlām"),
                r("The keys are in the bag", "চাবিগুলো ব্যাগে আছে", "Chābigulō bẽgē āchhe"),
                r("She works at the office", "সে অফিসে কাজ করে", "Sē ôphisē kāj kore"),
                r("Stand behind the door", "দরজার পিছনে দাঁড়াও", "Dôrjār pichhōne dãṛāo"),
                r("Wait in front of the gate", "দরজার সামনে দাঁড়াও", "Dôrjār sāmne dãṛāo"),
                r("The shop is across the road", "দোকানটা রাস্তার ওপারে", "Dokānṭā rāstār opārē"),
            ],
            "Nouns + postpositions",
        )
    )
    out.append(
        _b(
            534,
            "Prepositions with similar pronunciation or similar meanings in Bengali",
            "কাছে (near) vs পাশে (beside); উপরে (on top) vs ওপরে (above).",
            "Listen for minimal pairs in context.",
            [
                r("near the house", "বাড়ির কাছে", "bāṛir kāchhe"),
                r("beside the road", "রাস্তার পাশে", "rāstār pāshe"),
                r("on the roof", "ছাদের উপরে", "chādēr upore"),
                r("above the clouds", "মেঘের ওপরে", "mēghēr opārē"),
                r("under the bed", "বিছানার নিচে", "bichhānār nīche"),
                r("below the line", "লাইনের নিচে", "lāinēr nīche"),
                r("I live near the park", "আমি পার্কের কাছে থাকি", "Āmi pāṛkēr kāchhe thāki"),
                r("Sit beside me", "আমার পাশে বসো", "Āmār pāshe bôsō"),
                r("The lamp is on the roof", "ল্যাম্পটা ছাদের উপরে", "Lyāmṭā chādēr upore"),
                r("The plane flies above", "বিমান ওপর দিয়ে যায়", "Bimān opor diẏe jāy"),
                r("The dog is under the table", "কুকুরটা টেবিলের নিচে", "Kukurṭā ṭēbilēr nīche"),
                r("Sign below the line", "লাইনের নিচে সই করুন", "Lāinēr nīche sôi kôrun"),
                r("Shop near the station", "স্টেশনের কাছে দোকান", "Sṭēshonēr kāchhe dokān"),
                r("House beside the river", "নদীর পাশে বাড়ি", "Nodīr pāshe bāṛi"),
                r("Book on the shelf", "তাকের উপরে বই", "Tākēr upore bôi"),
                r("Picture above the door", "দরজার ওপরে ছবি", "Dôrjār opārē chobi"),
                r("Cat under the bed", "বিছানার নিচে বিড়াল", "Bichhānār nīche biṛāl"),
                r("Stand behind the car", "গাড়ির পিছনে দাঁড়াও", "Gāṛir pichhōne dãṛāo"),
            ],
            "Near / beside / on / above",
        )
    )
    out.append(
        _b(
            535,
            "Cases in Bengali (কারক)",
            "Sanskrit-style case labels: কর্তা (subject), কর্ম (object), করণ (instrument), etc.",
            "In spoken Bangla, postpositions often carry case-like meaning.",
            [
                r("I read a book (subject–object)", "আমি বই পড়ি", "Āmi bôi pōṛi"),
                r("He gave me a pen (dative)", "সে আমাকে কলম দিল", "Sē āmākē kolom dil"),
                r("With a knife (instrument)", "ছুরি দিয়ে", "churi diẏe"),
                r("From Kolkata (ablative)", "কলকাতা থেকে", "Kolkātā theke"),
                r("For you (benefactive)", "তোমার জন্য", "tōmār jônyo"),
                r("Of the house (genitive)", "বাড়ির", "bāṛir"),
                r("In the water (locative)", "জলে", "jole"),
                r("On the floor", "মেঝেতে", "mējēte"),
                r("I went with him", "আমি তার সঙ্গে গেলাম", "Āmi tār songe gēlām"),
                r("She wrote with a pen", "সে কলম দিয়ে লিখল", "Sē kolom diẏe likhlō"),
                r("Cut with scissors", "কাঁচি দিয়ে কাটো", "Kãchi diẏe kāṭō"),
                r("This is mother's book", "এটা মায়ের বই", "Ēṭā māẏēr bôi"),
                r("Water from the well", "কুয়ার জল", "kuẏār jol"),
                r("Gift for the child", "বাচ্চার জন্য উপহার", "bāchchār jônyo upohār"),
                r("He sits on the chair", "সে চেয়ারে বসে", "Sē cheẏāre bôse"),
                r("They live in Dhaka", "তারা ঢাকায় থাকে", "Tārā Ḍhākāy thākē"),
                r("I bought from the market", "আমি বাজার থেকে কিনলাম", "Āmi bājār theke kinlām"),
                r("She spoke about the plan", "সে পরিকল্পনা নিয়ে বলল", "Sē pôrikolponā niyē bôllō"),
            ],
            "কারক patterns",
        )
    )
    out.append(
        _b(
            536,
            "Commands / Imperative statements in Bengali",
            "Polite imperatives use -ুন; informal use -ো/ো: বসুন, বসো, যাও.",
            "Negative: করবেন না / করো না.",
            [
                r("Please sit", "বসুন", "Bôsun"),
                r("Please come in", "ভিতরে আসুন", "Bhitore āsun"),
                r("Please wait", "অপেক্ষা করুন", "Ôpekhshā kôrun"),
                r("Please eat", "খান", "Khān"),
                r("Go (informal)", "যাও", "Jāō"),
                r("Come here", "এদিকে এসো", "Ēdikē ēsō"),
                r("Listen", "শোনো", "Shōnō"),
                r("Don't run", "দৌড়ো না", "Douṛō nā"),
                r("Don't shout", "চেঁচিয়ো না", "Chẽchiyō nā"),
                r("Open the window", "জানলা খুলুন", "Jānlā khulun"),
                r("Close the door", "দরজা বন্ধ করুন", "Dôrjā bondho kôrun"),
                r("Show me your ticket", "টিকিটটা দেখান", "Ṭikiṭṭā dēkhān"),
                r("Write your name", "নাম লিখুন", "Nām likhun"),
                r("Tell the truth", "সত্যি বলুন", "Sôtyi bôlun"),
                r("Please hurry", "তাড়াতাড়ি করুন", "Ṭāṛāṭāṛi kôrun"),
                r("Help him", "তাকে সাহায্য করুন", "Tākē sāhājjo kôrun"),
                r("Let us go", "চলো যাই", "Chōlō jāi"),
                r("Be quiet", "চুপ করো", "Chup kōrō"),
            ],
            "Imperative",
        )
    )
    out.append(
        _b(
            537,
            "Time related words in Bengali",
            "আজ, কাল, গতকাল, পরশু; সকাল, দুপুর, বিকেল, রাত.",
            "Use করি / করব with time adverbs for habits and plans.",
            [
                r("today", "আজ", "āj"),
                r("tomorrow", "কাল", "kāl"),
                r("yesterday", "গতকাল", "gôtokāl"),
                r("day after tomorrow", "পরশু", "pôrôshu"),
                r("morning", "সকাল", "sākāl"),
                r("noon", "দুপুর", "dupur"),
                r("evening", "বিকেল", "bikēl"),
                r("night", "রাত", "rāt"),
                r("now", "এখন", "ēkhon"),
                r("later", "পরে", "pōre"),
                r("I will go tomorrow", "আমি কাল যাব", "Āmi kāl jābo"),
                r("I came yesterday", "আমি গতকাল এলাম", "Āmi gôtokāl ēlām"),
                r("See you the day after tomorrow", "পরশু দেখা হবে", "Pôrôshu dēkhā hōbe"),
                r("Morning tea", "সকালের চা", "Sākālēr chā"),
                r("Lunch at noon", "দুপুরে লাঞ্চ", "Dupurē lāñch"),
                r("Evening walk", "বিকেলে হাঁটা", "Bikēlē hãṭā"),
                r("Good night", "শুভ রাত্রি", "Shubh rātri"),
                r("What time is it?", "কটা বাজে?", "Koṭā bāje?"),
            ],
            "Time words",
        )
    )
    out.append(
        _b(
            538,
            "Verbs indicating cause of action (Causative verb) in Bengali",
            "Causative: খাইয়ে দেওয়া (feed / make eat), পড়ানো (teach / make read).",
            "Pattern: causative stem + দেওয়া / দেয়া in many patterns.",
            [
                r("to feed (make eat)", "খাইয়ে দেওয়া", "khāẏe dēōyā"),
                r("to make someone read", "পড়ানো", "pōṛānō"),
                r("to make someone sit", "বসানো", "bôsānō"),
                r("I fed the child", "আমি বাচ্চাকে খাইয়ে দিলাম", "Āmi bāchchākē khāẏe dilām"),
                r("She made him laugh", "সে তাকে হাসাল", "Sē tākē hāsāl"),
                r("He had the letter written", "সে চিঠি লিখিয়ে নিল", "Sē chiṭhi likhiyē nil"),
                r("Get the work done", "কাজ শেষ করান", "Kāj shēsh korān"),
                r("Mother made me study", "মা আমাকে পড়াল", "Mā āmākē pōṛāl"),
                r("I will get it printed", "আমি ছাপিয়ে নেব", "Āmi chāpiyē nebo"),
                r("Let the teacher explain", "শিক্ষককে বোঝান", "Shikkhôkke bōjhān"),
                r("She showed the way", "সে পথ দেখাল", "Sē poth dēkhāl"),
                r("He opened the door for me", "সে আমার জন্য দরজা খুলল", "Sē āmār jônyo dôrjā khullō"),
                r("We made them wait", "আমরা তাদের অপেক্ষা করালাম", "Āmrā tādēr ôpekhshā korālām"),
                r("Please make him sit", "তাকে বসান", "Tākē bôsān"),
                r("I will have food sent", "আমি খাবার পাঠাব", "Āmi khābār pāṭhābō"),
                r("She teaches the children", "সে বাচ্চাদের পড়ায়", "Sē bāchchādēr pōṛāy"),
                r("They made us leave", "তারা আমাদের চলে যেতে বলল", "Tārā āmādēr chōlē jēte bōllō"),
                r("Get the car ready", "গাড়ি প্রস্তুত করান", "Gāṛi prôstut korān"),
            ],
            "Causative",
        )
    )
    out.append(
        _b(
            539,
            "Gender-number agreement rule in Bengali",
            "Verbs often agree with honorific level; plural subjects may take plural agreement in some styles.",
            "ছেলেরা খেলছে (they play) — plural subject + collective verb form.",
            [
                r("The boy runs", "ছেলেটা দৌড়ায়", "Chēlēṭā douṛāy"),
                r("The boys run", "ছেলেরা দৌড়ায়", "Chēlērā douṛāy"),
                r("The girl sings", "মেয়েটা গায়", "Mēẏēṭā gāy"),
                r("The girls sing", "মেয়েরা গায়", "Mēẏērā gāy"),
                r("He is a doctor", "সে ডাক্তার", "Sē ḍāktār"),
                r("They are doctors", "তারা ডাক্তার", "Tārā ḍāktār"),
                r("She reads books", "সে বই পড়ে", "Sē bôi pōṛe"),
                r("They read books", "তারা বই পড়ে", "Tārā bôi pōṛe"),
                r("The cat sleeps", "বিড়ালটা ঘুমায়", "Biṛālṭā ghumāy"),
                r("The cats sleep", "বিড়ালগুলো ঘুমায়", "Biṛālgulō ghumāy"),
                r("You (form.) are kind", "আপনি দয়ালু", "Āpni dôyālu"),
                r("You (inf.) are kind", "তুমি দয়ালু", "Tumi dôyālu"),
                r("We are ready", "আমরা প্রস্তুত", "Āmrā prôstut"),
                r("They are late", "তারা দেরি করেছে", "Tārā dēri korechhe"),
                r("The team is strong", "দলটা শক্তিশালী", "Dôlṭā shktishālī"),
                r("The teams are strong", "দলগুলো শক্তিশালী", "Dôlgulō shôktishālī"),
                r("Brother and sister came", "ভাই ও বোন এল", "Bhāi o bōn ēl"),
                r("The brothers came", "ভাইয়েরা এল", "Bhāiērā ēl"),
            ],
            "Agreement",
        )
    )
    out.append(
        _b(
            540,
            "Past/Present/Future Perfect Tense – Second Style in Bengali",
            "Colloquial perfect: করেছি, করেছিলাম; future perfect style: করে ফেলব, করে নেব.",
            "Often matches English perfect with 'already' or 'by then'.",
            [
                r("I have done it", "আমি করে ফেলেছি", "Āmi kōre phelechhi"),
                r("I had already eaten", "আমি আগেই খেয়েছিলাম", "Āmi āgēi khēyēchilām"),
                r("She has left", "সে চলে গেছে", "Sē chōlē gēchhe"),
                r("We had met before", "আমরা আগে দেখা করেছিলাম", "Āmrā āgē dēkhā korechilām"),
                r("By then I will have finished", "তখন আমি শেষ করে ফেলব", "Tokhon āmi shēsh kōre phelbo"),
                r("He has not come yet", "সে এখনও আসেনি", "Sē ēkhonō āsēni"),
                r("I had forgotten", "আমি ভুলে গিয়েছিলাম", "Āmi bhule giyēchilām"),
                r("They have agreed", "তারা রাজি হয়েছে", "Tārā rāji hōyēchhe"),
                r("We have learned", "আমরা শিখেছি", "Āmrā shikhēchhi"),
                r("You have tried", "তুমি চেষ্টা করেছো", "Tumi chēṣṭā korechho"),
                r("By Monday I will have done it", "সোমবারের মধ্যে আমি করে ফেলব", "Sōmbārēr môdhye āmi kōre phelbo"),
                r("She had already read", "সে আগেই পড়েছিল", "Sē āgēi pōṛēchil"),
                r("I have paid", "আমি টাকা দিয়েছি", "Āmi ṭākā diẏechhi"),
                r("He had gone", "সে চলে গিয়েছিল", "Sē chōlē giyēchil"),
                r("We will have arrived", "আমরা পৌঁছে যাব", "Āmrā poũchhe jābo"),
                r("They have sold the house", "তারা বাড়ি বেচেছে", "Tārā bāṛi bēchēchhe"),
                r("I had no idea", "আমার ধারণা ছিল না", "Āmār dhārôṇā chhil nā"),
                r("It will have been done", "সেটা হয়ে যাবে", "Sēṭā hōye jābe"),
            ],
            "Perfect (style 2)",
        )
    )
    out.append(
        _b(
            541,
            "Past/Present/Future Perfect Continuous tense in Bengali",
            "Use করছিল + থাকা / করতে থাকা patterns: long duration up to a point.",
            "I had been reading / I have been working — often করছিলাম / করছিল + context.",
            [
                r("I was reading (ongoing past)", "আমি পড়ছিলাম", "Āmi pōṛchilām"),
                r("I had been waiting", "আমি অপেক্ষা করছিলাম", "Āmi ôpekhshā korchhilām"),
                r("She had been working", "সে কাজ করছিল", "Sē kāj korchhil"),
                r("we had been studying", "আমরা পড়ছিলাম", "Āmrā pōṛchilām"),
                r("They had been talking", "তারা কথা বলছিল", "Tārā kōthā bolchhil"),
                r("I have been learning", "আমি শিখছি", "Āmi shikhchhi"),
                r("He has been sick", "সে অসুস্থ ছিল", "Sē ôsustho chhil"),
                r("We have been friends", "আমরা বন্ধু ছিলাম", "Āmrā bondhu chhilām"),
                r("It had been raining", "বৃষ্টি পড়ছিল", "Briṣṭi pōṛchhil"),
                r("I will have been working", "আমি কাজ করতে থাকব", "Āmi kāj korte thākbo"),
                r("By then she will have been teaching", "তখন সে পড়াচ্ছিল", "Tokhon sē pōṛāchchhil"),
                r("I have been waiting long", "আমি অনেকক্ষণ ধরে অপেক্ষা করছি", "Āmi ônekkhôn dhôre ôpekhshā korchhi"),
                r("He had been driving", "সে গাড়ি চালাচ্ছিল", "Sē gāṛi chālāchchhil"),
                r("We have been trying", "আমরা চেষ্টা করছি", "Āmrā chēṣṭā korchhi"),
                r("They had been living there", "তারা সেখানে থাকত", "Tārā shēkhāne thāktō"),
                r("I have been thinking", "আমি ভাবছি", "Āmi bhabchhi"),
                r("She has been cooking", "সে রান্না করছে", "Sē rānnā korchhe"),
                r("The show had been running", "শো চলছিল", "Ō cholchhil"),
            ],
            "Perfect continuous",
        )
    )
    out.append(
        _b(
            542,
            'Difference between "no/not" and "don\'t want" in Bengali',
            "না negates verbs; চাই না = don't want; নেই = there isn't; নই = am not (copula).",
            "আমি যাই না (I don't go) vs আমি চাই না (I don't want it).",
            [
                r("I don't go", "আমি যাই না", "Āmi jāi nā"),
                r("I don't want", "আমি চাই না", "Āmi chāi nā"),
                r("I don't want rice", "আমি ভাত চাই না", "Āmi bhāt chāi nā"),
                r("I don't want to go", "আমি যেতে চাই না", "Āmi jēte chāi nā"),
                r("He doesn't come", "সে আসে না", "Sē āse nā"),
                r("He doesn't want to come", "সে আসতে চায় না", "Sē āste chāy nā"),
                r("There is no time", "সময় নেই", "Somoy nēi"),
                r("I am not tired", "আমি ক্লান্ত নই", "Āmi klānto nôi"),
                r("I don't like it", "আমার ভালো লাগে না", "Āmār bhālō lāgē nā"),
                r("We don't need it", "আমাদের দরকার নেই", "Āmādēr dôrkār nēi"),
                r("No, thanks", "না, ধন্যবাদ", "Nā, dhonyobād"),
                r("Don't do it", "করো না", "Korō nā"),
                r("I am not going", "আমি যাচ্ছি না", "Āmi jāchchhi nā"),
                r("She doesn't speak", "সে বলে না", "Sē bōle nā"),
                r("I don't eat meat", "আমি মাংস খাই না", "Āmi māṅsō khāi nā"),
                r("He doesn't want money", "সে টাকা চায় না", "Sē ṭākā chāy nā"),
                r("There is no problem", "কোনো সমস্যা নেই", "Kōnō shomosshā nēi"),
                r("I don't feel like it", "আমার ইচ্ছে হচ্ছে না", "Āmār icchē hochchhe nā"),
            ],
            "না vs চাই না",
        )
    )
    # 533–596: phrase patterns + grammar tail (from rest_b)
    from build_assamese_data_rest_b import add_chapters_532_596

    add_chapters_532_596(out)
    from build_assamese_data_rest_c import add_chapters_597_662

    add_chapters_597_662(out)
