# -*- coding: utf-8 -*-
"""
Rich Hindi phrase / structure lessons (543–596): blocks + tables.
Standard spoken Hindi; IAST-style romanization.
"""

from __future__ import annotations

from hindi_grammar_chapters import _p, _t


def _l(content: str, intro: str, blocks: list[dict]) -> dict:
    return {"content": content, "intro": intro, "blocks": blocks}


# --- 543–570 ---


def chapter_543() -> dict:
    return _l(
        "Near future and intention: जा रहा हूँ, वाला है, करने वाला हूँ — English ‘going to’.",
        "Spoken Hindi uses progressive + जाना or वाला + noun/verb for planned action.",
        [
            _p("Patterns", "मैं अभी निकल रहा हूँ = I’m going (to leave). कल जाना है = have to / will go."),
            _t(
                "Going to / about to",
                [
                    ["I am going to leave now", "मैं अभी निकलने वाला हूँ", "main abhī nikalne vālā hū̃"],
                    ["We are going to eat", "हम खाने वाले हैं", "ham khāne vāle haiṃ"],
                    ["She is going to call", "वह फोन करने वाली है", "vah phon karne vālī hai"],
                    ["It is going to rain", "बारिश होने वाली है", "bāriś hone vālī hai"],
                    ["I am going to Delhi tomorrow", "मैं कल दिल्ली जा रहा हूँ", "main kal dillī jā rahā hū̃"],
                    ["They are going to start", "वे शुरू करने वाले हैं", "ve śurū karne vāle haiṃ"],
                    ["We are not going to wait", "हम इंतज़ार नहीं करने वाले", "ham intazār nahī̃ karne vāle"],
                    ["He is going to pay", "वह भुगतान करने वाला है", "vah bhugtān karne vālā hai"],
                    ["I was going to tell you", "मैं आपको बताने वाला था", "main āpko batāne vālā thā"],
                    ["What are you going to do?", "आप क्या करने वाले हैं?", "āp kyā karne vāle haiṃ?"],
                    ["Nothing is going to change", "कुछ बदलने वाला नहीं है", "kuch badalne vālā nahī̃ hai"],
                    ["I am going to try", "मैं कोशिश करने वाला हूँ", "main kośiś karne vālā hū̃"],
                    ["We are going to meet", "हम मिलने वाले हैं", "ham milne vāle haiṃ"],
                    ["The train is about to leave", "ट्रेन छूटने वाली है", "ṭren chūṭne vālī hai"],
                    ["I am going for a walk", "मैं टहलने जा रहा हूँ", "main ṭahalne jā rahā hū̃"],
                    ["Plans are going to fail", "योजनाएँ फेल होने वाली हैं", "yojnāeṃ phel hone vālī haiṃ"],
                ],
            ),
        ],
    )


def chapter_544() -> dict:
    return _l(
        "Habitual past: करता था / करती थी / करते थे — ‘used to’.",
        "Also: पहले … हुआ करता था for ‘there used to be’.",
        [
            _p("Pattern", "Imperfect past + था/थी/थे marks repeated or former habit."),
            _t(
                "Used to",
                [
                    ["I used to live there", "मैं वहाँ रहता था", "main vahā̃ rahatā thā"],
                    ["She used to sing", "वह गाती थी", "vah gātī thī"],
                    ["We used to play here", "हम यहाँ खेलते थे", "ham yahā̃ khelte the"],
                    ["He used to smoke", "वह सिगरेट पीता था", "vah sigreṭ pītā thā"],
                    ["They used to visit us", "वे हमसे मिलने आते थे", "ve ham se milne āte the"],
                    ["There used to be a well", "पहले यहाँ कुआँ हुआ करता था", "pahle yahā̃ kuā̃ huā kartā thā"],
                    ["I used to think so", "मैं ऐसा सोचता था", "main aisā socatā thā"],
                    ["It used to be cheap", "यह सस्ता हुआ करता था", "yah sustā huā kartā thā"],
                    ["We used to walk to school", "हम पैदल स्कूल जाते थे", "ham paidal skūl jāte the"],
                    ["She used to teach", "वह पढ़ाती थी", "vah paṛhātī thī"],
                    ["I did not use to like it", "मुझे यह पहले पसंद नहीं था", "mujhe yah pahle pasand nahī̃ thā"],
                    ["He used to work nights", "वह रात में काम करता था", "vah rāt mẽ kām kartā thā"],
                    ["We used to meet often", "हम अक्सर मिलते थे", "ham aksar milte the"],
                    ["The bus used to stop here", "बस यहाँ रुका करती थी", "bas yahā̃ rukā kartī thī"],
                    ["I used to know him", "मैं उसे जानता था", "main use jāntā thā"],
                    ["Things used to be simple", "बातें सरल हुआ करती थीं", "bāteṃ saral huā kartī thī̃"],
                ],
            ),
        ],
    )


def chapter_545() -> dict:
    return _l(
        "Older/literary habit: करा करते थे, हुआ करता था — same ‘used to’, more narrative tone.",
        "Common in stories: खाया करते थे, देखा करती थी.",
        [
            _p("Style", "Verb stem + आ / या + करना + past imperfect — marks repeated past action."),
            _t(
                "Old-style ‘used to’",
                [
                    ["People used to gather", "लोग इकट्ठा हुआ करते थे", "log ikaṭṭhā huā karte the"],
                    ["Grandma used to tell stories", "दादी कहानियाँ सुनाया करती थीं", "dādī kahāniā̃ sunāyā kartī thī̃"],
                    ["He used to visit daily", "वह रोज़ आया करते थे", "vah roz āyā karte the"],
                    ["We used to eat together", "हम साथ खाया करते थे", "ham sāth khāyā karte the"],
                    ["She used to cry often", "वह अक्सर रोया करती थी", "vah aksar royā kartī thī"],
                    ["Birds used to chirp", "पक्षी चहचहाया करते थे", "pakṣī cahcahāyā karte the"],
                    ["There used to be fairs", "मेले लगा करते थे", "mele lagā karte the"],
                    ["He used to read aloud", "वह ज़ोर से पढ़ा करते थे", "vah zor se paṛhā karte the"],
                    ["We used to fear darkness", "हम अंधेरे से डरा करते थे", "ham andhere se ḍarā karte the"],
                    ["She used to sing in temple", "वह मंदिर में गाया करती थी", "vah mandir mẽ gāyā kartī thī"],
                    ["Children used to play outside", "बच्चे बाहर खेला करते थे", "bacce bāhar khelā karte the"],
                    ["He used to forget", "वह भूला करते थे", "vah bhūlā karte the"],
                    ["We used to save money", "हम पैसे बचाया करते थे", "ham paise bacāyā karte the"],
                    ["Rain used to come early", "बारिश जल्दी आया करती थी", "bāriś jaldī āyā kartī thī"],
                    ["I used to believe that", "मैं ऐसा माना करता था", "main aisā mānā kartā thā"],
                    ["Traders used to pass by", "व्यापारी गुज़रा करते थे", "vyāpārī guzarā karte the"],
                ],
            ),
        ],
    )


def chapter_546() -> dict:
    return _l(
        "Conditionals: अगर / यदि … तो / तो फिर — ‘if … then’.",
        "Spoken Hindi prefers अगर; तो can be omitted in quick speech.",
        [
            _p("Pattern", "अगर तुम आओगे, तो हम खाएँगे — if you come, we will eat."),
            _t(
                "If–then",
                [
                    ["If it rains, we will stay", "अगर बारिश हुई तो हम रुकेंगे", "agar bāriś huī to ham rukeṅge"],
                    ["If you are free, call me", "अगर तुम फुरसत में हो तो फोन करना", "agar tum fursat mẽ ho to phon karnā"],
                    ["If he comes, tell me", "अगर वह आए तो मुझे बताना", "agar vah ā.e to mujhe batānā"],
                    ["If not, I will leave", "वरना मैं चला जाऊँगा", "varnā main calā jāū̃gā"],
                    ["If I knew, I would say", "अगर मुझे पता होता तो मैं कहता", "agar mujhe patā hotā to main kahtā"],
                    ["If you had asked", "अगर तुमने पूछा होता", "agar tumne pūchā hotā"],
                    ["Then we will see", "तो फिर देखेंगे", "to phir dekheṅge"],
                    ["If she agrees, we start", "अगर वह माने तो शुरू करते हैं", "agar vah māne to śurū karte haiṃ"],
                    ["If there is time", "अगर समय हो तो", "agar samay ho to"],
                    ["If possible", "अगर हो सके तो", "agar ho sake to"],
                    ["If you want", "अगर तुम चाहो तो", "agar tum cāho to"],
                    ["If I am wrong, correct me", "अगर मैं गलत हूँ तो सुधारो", "agar main galat hū̃ to sudhāro"],
                    ["If they come, welcome them", "अगर वे आएं तो स्वागत करो", "agar ve āeṃ to svāgat karo"],
                    ["If the shop is open", "अगर दुकान खुली हो", "agar dukān khulī ho"],
                    ["If you don't mind", "अगर बुरा न मानो तो", "agar burā na māno to"],
                    ["If everything is fine", "अगर सब ठीक हो तो", "agar sab ṭhīk ho to"],
                ],
            ),
        ],
    )


def chapter_547() -> dict:
    return _l(
        "Verb + postposition: ध्यान देना ‘pay attention to’, इंतज़ार करना ‘wait for’, विश्वास करना ‘trust’.",
        "The postposition (पर, में, का, से) is fixed with each verb.",
        [
            _p("Learn chunks", "इंतज़ार + का: किताब का इंतज़ार — wait for the book."),
            _t(
                "Verbs with postpositions",
                [
                    ["wait for the bus", "बस का इंतज़ार करना", "bas kā intazār karnā"],
                    ["believe in God", "भगवान पर विश्वास करना", "bhagvān par viśvās karnā"],
                    ["depend on you", "आप पर निर्भर रहना", "āp par nirbhar rahnā"],
                    ["think about it", "इसके बारे में सोचना", "is ke bāre mẽ socnā"],
                    ["laugh at someone", "किसी का मज़ाक उड़ाना", "kisī kā mazāk uṛānā"],
                    ["listen to music", "संगीत सुनना", "saṅgīt sunnā"],
                    ["look at the photo", "फ़ोटो देखना", "phoṭo dekhnā"],
                    ["search for keys", "चाबी ढूँढना", "cābī ḍhū̃ḍhnā"],
                    ["worry about money", "पैसे की चिंता करना", "paise kī cintā karnā"],
                    ["agree with him", "उससे सहमत होना", "us se sahamat honā"],
                    ["shout at children", "बच्चों पर चिल्लाना", "baccõ par cillānā"],
                    ["apply for a job", "नौकरी के लिए आवेदन करना", "naukarī ke lie āvedan karnā"],
                    ["I am waiting for you", "मैं आपका इंतज़ार कर रहा हूँ", "main āpkā intazār kar rahā hū̃"],
                    ["She believes in hard work", "वह मेहनत पर विश्वास करती है", "vah mehnat par viśvās kartī hai"],
                    ["We thought about it", "हमने इसके बारे में सोचा", "hamne is ke bāre mẽ socā"],
                    ["Do not laugh at him", "उसका मज़ाक मत उड़ाओ", "uskā mazāk mat uṛāo"],
                ],
            ),
        ],
    )


def chapter_548() -> dict:
    return _l(
        "Adjectives agree in gender/number: बड़ा / बड़ी / बड़े; comparative often with से.",
        "Attributive: अच्छी किताब; predicative: किताब अच्छी है.",
        [
            _p("Basics", "Color, size, quality — place before noun or use with है."),
            _t(
                "Adjectives",
                [
                    ["a red car", "लाल गाड़ी", "lāl gāṛī"],
                    ["a big house", "बड़ा घर", "baṛā ghar"],
                    ["good children", "अच्छे बच्चे", "acche bacce"],
                    ["this is expensive", "यह महँगा है", "yah mahṅgā hai"],
                    ["she is intelligent", "वह होशियार है", "vah hośiyār hai"],
                    ["fresh fruit", "ताज़ा फल", "tājā phal"],
                    ["cold water", "ठंडा पानी", "thaṃḍā pānī"],
                    ["happy family", "खुश परिवार", "khush parivār"],
                    ["tired eyes", "थकी आँखें", "thakī ā̃kheṃ"],
                    ["easy question", "आसान सवाल", "āsān savāl"],
                    ["The room is dark", "कमरा अँधेरा है", "kamrā aṃdherā hai"],
                    ["Those books are new", "वे किताबें नई हैं", "ve kitābeṃ naī haiṃ"],
                    ["He is taller than me", "वह मुझसे लंबा है", "vah mujh se laṃbā hai"],
                    ["This is the best", "यह सबसे अच्छा है", "yah sab se acchā hai"],
                    ["bitter medicine", "कड़वी दवा", "kaṛvī davā"],
                    ["slow traffic", "धीमी यातायात", "dhīmī yātāyāt"],
                ],
            ),
        ],
    )


def chapter_549() -> dict:
    return _l(
        "Ability: सकना conjugated — कर सकता हूँ; ‘can’ for permission often क्या … सकता हूँ?",
        "नहीं सकता = cannot (ability); मत = don’t (permission).",
        [
            _p("Pattern", "Infinitive + सकना: पढ़ सकते हैं — can read."),
            _t(
                "Can / be able to",
                [
                    ["I can swim", "मैं तैर सकता हूँ", "main tair saktā hū̃"],
                    ["She can drive", "वह गाड़ी चला सकती है", "vah gāṛī calā saktī hai"],
                    ["We cannot come today", "हम आज नहीं आ सकते", "ham āj nahī̃ ā sakte"],
                    ["Can you help?", "क्या आप मदद कर सकते हैं?", "kyā āp madad kar sakte haiṃ?"],
                    ["He could not sleep", "वह सो नहीं सका", "vah so nahī̃ sakā"],
                    ["I will be able to finish", "मैं खत्म कर सकूँगा", "main khatm kar sakū̃gā"],
                    ["They can speak Hindi", "वे हिन्दी बोल सकते हैं", "ve hindī bol sakte haiṃ"],
                    ["Could you repeat?", "क्या आप दोहरा सकते हैं?", "kyā āp dohrā sakte haiṃ?"],
                    ["I can’t hear you", "मैं आपकी आवाज़ नहीं सुन सकता", "main āpkī āvāz nahī̃ sun saktā"],
                    ["She was able to escape", "वह बच निकल सकी", "vah bac nikal sakī"],
                    ["Nothing can stop us", "कुछ हमें रोक नहीं सकता", "kuch hameṃ rok nahī̃ saktā"],
                    ["Can I sit here?", "क्या मैं यहाँ बैठ सकता हूँ?", "kyā main yahā̃ baiṭh saktā hū̃?"],
                    ["You may go (allowed)", "आप जा सकते हैं", "āp jā sakte haiṃ"],
                    ["I couldn’t understand", "मैं समझ नहीं सका", "main samajh nahī̃ sakā"],
                    ["We can try again", "हम फिर कोशिश कर सकते हैं", "ham phir kośiś kar sakte haiṃ"],
                    ["He can’t afford it", "वह यह खरीद नहीं सकता", "vah yah kharīd nahī̃ saktā"],
                ],
            ),
        ],
    )


def chapter_550() -> dict:
    return _l(
        "Need: चाहिए (invariable); want: चाहना — मुझे पानी चाहिए, मैं जाना चाहता हूँ.",
        "चाहिए follows dative subject: हमें आराम चाहिए.",
        [
            _p("Contrast", "मुझे खाना चाहिए = I need / should have food. मैं खाना चाहता हूँ = I want to eat."),
            _t(
                "Want / need",
                [
                    ["I need water", "मुझे पानी चाहिए", "mujhe pānī cāhie"],
                    ["I want to sleep", "मैं सोना चाहता हूँ", "main sonā cāhtā hū̃"],
                    ["She needs rest", "उसे आराम चाहिए", "use ārām cāhie"],
                    ["We want peace", "हम शांति चाहते हैं", "ham śānti cāhte haiṃ"],
                    ["Do you need anything?", "आपको कुछ चाहिए?", "āpko kuch cāhie?"],
                    ["I don’t want trouble", "मुझे झगड़ा नहीं चाहिए", "mujhe jhagaṛā nahī̃ cāhie"],
                    ["He wants to leave", "वह जाना चाहता है", "vah jānā cāhtā hai"],
                    ["Children need love", "बच्चों को प्यार चाहिए", "baccõ ko pyār cāhie"],
                    ["I needed your help", "मुझे आपकी मदद चाहिए थी", "mujhe āpkī madad cāhie thī"],
                    ["They want tickets", "उन्हें टिकट चाहिए", "unheṃ ṭikaṭ cāhie"],
                    ["I want nothing", "मुझे कुछ नहीं चाहिए", "mujhe kuch nahī̃ cāhie"],
                    ["You should rest", "आपको आराम चाहिए", "āpko ārām cāhie"],
                    ["She wants him to stay", "वह चाहती है कि वह रुके", "vah cāhtī hai ki vah ruke"],
                    ["We need time", "हमें समय चाहिए", "hameṃ samay cāhie"],
                    ["I want to learn Hindi", "मैं हिन्दी सीखना चाहता हूँ", "main hindī sīkhnā cāhtā hū̃"],
                    ["He doesn’t need money", "उसे पैसे नहीं चाहिए", "use paise nahī̃ cāhie"],
                ],
            ),
        ],
    )


def chapter_551() -> dict:
    return _l(
        "Become: बन जाना, हो जाना; happen: होना, घटित होना.",
        "मौसम ठंडा हो गया — the weather became cold.",
        [
            _p("Usage", "Adjective + हो जाना; profession + बनना: डॉक्टर बनना."),
            _t(
                "Become / happen",
                [
                    ["He became a doctor", "वह डॉक्टर बन गया", "vah ḍokṭar ban gayā"],
                    ["It became dark", "अँधेरा हो गया", "aṃdherā ho gayā"],
                    ["She got angry", "वह नाराज़ हो गई", "vah nārāz ho gaī"],
                    ["What happened?", "क्या हुआ?", "kyā huā?"],
                    ["Nothing happened", "कुछ नहीं हुआ", "kuch nahī̃ huā"],
                    ["The plan failed", "योजना फेल हो गई", "yojanā phel ho gaī"],
                    ["I became tired", "मैं थक गया", "main thak gayā"],
                    ["Life became easier", "जीवन आसान हो गया", "jīvan āsān ho gayā"],
                    ["It may happen again", "यह फिर हो सकता है", "yah phir ho saktā hai"],
                    ["Suddenly it rained", "अचानक बारिश हो गई", "acānak bāriś ho gaī"],
                    ["He turned pale", "वह पीला पड़ गया", "vah pīlā paṛ gayā"],
                    ["She became famous", "वह प्रसिद्ध हो गई", "vah prasiddh ho gaī"],
                    ["Things happen", "बातें होती हैं", "bāteṃ hotī haiṃ"],
                    ["Don’t let it happen", "ऐसा होने मत दो", "aisā hone mat do"],
                    ["The meeting will happen tomorrow", "मीटिंग कल होगी", "mīṭiṅ kal hogī"],
                    ["He became rich", "वह अमीर बन गया", "vah amīr ban gayā"],
                ],
            ),
        ],
    )


def chapter_552() -> dict:
    return _l(
        "Soft obligation: चाहिए / अच्छा होगा / …ना चाहिए — ‘should’.",
        "Advice: आपको आराम करना चाहिए — you should rest.",
        [
            _p("Pattern", "Dative + verb + चाहिए; or अच्छा रहेगा for ‘it would be better’."),
            _t(
                "Should",
                [
                    ["You should sleep early", "आपको जल्दी सोना चाहिए", "āpko jaldī sonā cāhie"],
                    ["We should leave now", "हमें अभी चलना चाहिए", "hameṃ abhī calnā cāhie"],
                    ["He should see a doctor", "उसे डॉक्टर को दिखाना चाहिए", "use ḍokṭar ko dikhānā cāhie"],
                    ["You shouldn’t worry", "आपको चिंता नहीं करनी चाहिए", "āpko cintā nahī̃ karnī cāhie"],
                    ["It would be better to wait", "इंतज़ार करना अच्छा रहेगा", "intazār karnā acchā rahegā"],
                    ["She should apologize", "उसे माफ़ी माँगनी चाहिए", "use māfī māṅgnī cāhie"],
                    ["We should try", "हमें कोशिश करनी चाहिए", "hameṃ kośiś karnī cāhie"],
                    ["I should have told you", "मुझे आपको बताना चाहिए था", "mujhe āpko batānā cāhie thā"],
                    ["Children should respect elders", "बच्चों को बड़ों का सम्मान करना चाहिए", "baccõ ko baṛõ kā sammān karnā cāhie"],
                    ["You should read this", "आपको यह पढ़ना चाहिए", "āpko yah paṛhnā cāhie"],
                    ["We shouldn’t waste time", "हमें समय बर्बाद नहीं करना चाहिए", "hameṃ samay barbād nahī̃ karnā cāhie"],
                    ["It should be easy", "यह आसान होना चाहिए", "yah āsān honā cāhie"],
                    ["He should be here", "उसे यहाँ होना चाहिए", "use yahā̃ honā cāhie"],
                    ["Maybe you should ask", "शायद आपको पूछना चाहिए", "śāyad āpko pūchnā cāhie"],
                    ["They should know", "उन्हें पता होना चाहिए", "unheṃ patā honā cāhie"],
                    ["I should go", "मुझे जाना चाहिए", "mujhe jānā cāhie"],
                ],
            ),
        ],
    )


def chapter_553() -> dict:
    return _l(
        "Strong obligation: पड़ना ‘have to’, ज़रूरी है, अनिवार्य है — ‘must’.",
        "मुझे जाना पड़ा — I had to go.",
        [
            _p("Pattern", "Dative + infinitive + पड़ना; future पड़ेगा for ‘will have to’."),
            _t(
                "Must / have to",
                [
                    ["I have to work", "मुझे काम करना पड़ता है", "mujhe kām karnā paṛtā hai"],
                    ["You must follow rules", "आपको नियम मानने पड़ेंगे", "āpko niyam mānne paṛeṅge"],
                    ["We had to wait", "हमें इंतज़ार करना पड़ा", "hameṃ intazār karnā paṛā"],
                    ["She must pay fine", "उसे जुर्माना भरना पड़ेगा", "use jurmānā bharnā paṛegā"],
                    ["It is necessary", "यह ज़रूरी है", "yah zarūrī hai"],
                    ["I must leave now", "मुझे अभी जाना ही पड़ेगा", "mujhe abhī jānā hī paṛegā"],
                    ["They have to decide", "उन्हें फैसला करना पड़ेगा", "unheṃ faislā karnā paṛegā"],
                    ["You must not smoke here", "यहाँ सिगरेट पीना मना है", "yahā̃ sigreṭ pīnā manā hai"],
                    ["We must hurry", "हमें जल्दी करनी पड़ेगी", "hameṃ jaldī karnī paṛegī"],
                    ["He had to apologize", "उसे माफ़ी माँगनी पड़ी", "use māfī māṅgnī paṛī"],
                    ["I need to finish this", "मुझे यह खत्म करना ही पड़ेगा", "mujhe yah khatm karnā hī paṛegā"],
                    ["Everyone must come", "सबको आना ही पड़ेगा", "sabko ānā hī paṛegā"],
                    ["Rules must be followed", "नियमों का पालन करना पड़ता है", "niyamõ kā pālan karnā paṛtā hai"],
                    ["I am forced to agree", "मुझे मानना पड़ रहा है", "mujhe mānnā paṛ rahā hai"],
                    ["You have to sign", "आपको हस्ताक्षर करने पड़ेंगे", "āpko hastākṣar karne paṛeṅge"],
                    ["We must not give up", "हमें हार नहीं माननी पड़ेगी", "hameṃ hār nahī̃ mānnī paṛegī"],
                ],
            ),
        ],
    )


def chapter_554() -> dict:
    return _l(
        "Continuative: करते रहना, जाते रहना — ‘keep (on) doing’.",
        "Also: लगे रहो — keep at it (imperative).",
        [
            _p("Pattern", "Present habitual stem + ते रहना for sustained action."),
            _t(
                "Keep doing",
                [
                    ["Keep trying", "कोशिश करते रहो", "kośiś karte raho"],
                    ["He kept talking", "वह बोलते रहा", "vah bolte rahā"],
                    ["We kept walking", "हम चलते रहे", "ham calte rahe"],
                    ["Don’t keep silent", "चुप चाप मत रहो", "cup cāp mat raho"],
                    ["She kept smiling", "वह मुस्कुराती रही", "vah muskurātī rahī"],
                    ["Rain kept falling", "बारिश गिरती रही", "bāriś giratī rahī"],
                    ["Keep reading", "पढ़ते रहिए", "paṛhte rahie"],
                    ["They kept waiting", "वे इंतज़ार करते रहे", "ve intazār karte rahe"],
                    ["I kept thinking", "मैं सोचता रहा", "main socatā rahā"],
                    ["Keep your health", "सेहत का ध्यान रखते रहो", "sehat kā dhyān rakhte raho"],
                    ["The baby kept crying", "बच्चा रोता रहा", "baccā rotā rahā"],
                    ["We must keep moving", "हम चलते रहना चाहिए", "ham calte rehnā cāhie"],
                    ["He kept denying", "वह इनकार करता रहा", "vah inkār kartā rahā"],
                    ["Keep practicing daily", "रोज़ अभ्यास करते रहो", "roz abhyās karte raho"],
                    ["She kept calling", "वह फोन करती रही", "vah phon kartī rahī"],
                    ["Don’t keep postponing", "टालते मत रहो", "ṭālte mat raho"],
                ],
            ),
        ],
    )


def chapter_555() -> dict:
    return _l(
        "Comparison: A से B ज़्यादा; superlative: सबसे; equality: जितना … उतना.",
        "बड़ा, बड़ा, सबसे बड़ा — big, bigger, biggest (context + से).",
        [
            _p("Degrees", "यह मुझसे लंबा है — taller than me. सबसे सस्ता — cheapest."),
            _t(
                "Comparison",
                [
                    ["bigger than me", "मुझसे बड़ा", "mujh se baṛā"],
                    ["the tallest", "सबसे लंबा", "sab se laṃbā"],
                    ["better than before", "पहले से बेहतर", "pahle se behtar"],
                    ["the best city", "सबसे अच्छा शहर", "sab se acchā śahar"],
                    ["less expensive", "कम महँगा", "kam mahṅgā"],
                    ["as much as possible", "जितना हो सके", "jitnā ho sake"],
                    ["She is smarter than him", "वह उससे होशियार है", "vah us se hośiyār hai"],
                    ["This is worse", "यह बुरा है", "yah burā hai"],
                    ["He runs fastest", "वह सबसे तेज़ दौड़ता है", "vah sab se tez dauṛtā hai"],
                    ["almost the same", "लगभग वही", "lagbhag vahī"],
                    ["not as good", "उतना अच्छा नहीं", "utnā acchā nahī̃"],
                    ["older than me", "मुझसे बड़ा", "mujh se baṛā"],
                    ["the smallest child", "सबसे छोटा बच्चा", "sab se choṭā baccā"],
                    ["more important", "ज़्यादा ज़रूरी", "zyādā zarūrī"],
                    ["too costly", "बहुत महँगा", "bahut mahṅgā"],
                    ["easier than this", "इससे आसान", "is se āsān"],
                ],
            ),
        ],
    )


def chapter_556() -> dict:
    return _l(
        "Know facts: पता होना; know people/skills: जानना; ‘I know how’: आना.",
        "मुझे पता है; मैं उसे जानता हूँ; मुझे तैरना आता है.",
        [
            _p("Frames", "पता चलना = find out; मालूम होना = be known."),
            _t(
                "To know",
                [
                    ["I know the answer", "मुझे जवाब पता है", "mujhe javāb patā hai"],
                    ["I know him well", "मैं उसे अच्छी तरह जानता हूँ", "main use acchī tarah jāntā hū̃"],
                    ["She knows Hindi", "उसे हिन्दी आती है", "use hindī ātī hai"],
                    ["I don’t know", "मुझे नहीं पता", "mujhe nahī̃ patā"],
                    ["Who knows?", "कौन जाने?", "kaun jāne?"],
                    ["I knew it already", "मुझे पहले से पता था", "mujhe pahle se patā thā"],
                    ["Let me know", "मुझे बता देना", "mujhe batā denā"],
                    ["He knows the way", "उसे रास्ता पता है", "use rāstā patā hai"],
                    ["We know the truth", "हमें सच पता है", "hameṃ sac patā hai"],
                    ["I got to know yesterday", "मुझे कल पता चला", "mujhe kal patā calā"],
                    ["Do you know her?", "क्या तुम उसे जानते हो?", "kyā tum use jānte ho?"],
                    ["I know how to cook", "मुझे खाना बनाना आता है", "mujhe khānā banānā ātā hai"],
                    ["Nobody knew", "किसी को पता नहीं था", "kisī ko patā nahī̃ thā"],
                    ["I want to know why", "मुझे जानना है क्यों", "mujhe jānnā hai kyõ"],
                    ["She knows everything", "उसे सब पता है", "use sab patā hai"],
                    ["Knowledge is power", "ज्ञान शक्ति है", "jñān śakti hai"],
                ],
            ),
        ],
    )


def chapter_557() -> dict:
    return _l(
        "Let’s: चलो …; polite suggestion: चलिए; Shall we?: चलें? आगे बढ़ें?",
        "देखते हैं — let’s see (we’ll see).",
        [
            _p("Hortative", "चलो खाते हैं — let’s eat. मैं करने दूँ — let me do it."),
            _t(
                "Let / Shall we",
                [
                    ["Let’s go", "चलो चलें", "calo caleṃ"],
                    ["Let’s eat", "चलो खाते हैं", "calo khāte haiṃ"],
                    ["Shall we start?", "शुरू करें?", "śurū kareṃ?"],
                    ["Let him speak", "उसे बोलने दो", "use bolne do"],
                    ["Let me try", "मैं कोशिश कर लूँ", "main kośiś kar lū̃"],
                    ["Don’t let them in", "उन्हें अंदर मत आने दो", "unheṃ andar mat āne do"],
                    ["Let’s wait", "चलो इंतज़ार करते हैं", "calo intazār karte haiṃ"],
                    ["Shall we leave?", "चलें?", "caleṃ?"],
                    ["Let it be", "रहने दो", "rahne do"],
                    ["Let’s see tomorrow", "कल देखते हैं", "kal dekhte haiṃ"],
                    ["Allow me to explain", "मुझे समझाने दीजिए", "mujhe samjhāne dījie"],
                    ["Let’s not fight", "झगड़ा मत करो", "jhagaṛā mat karo"],
                    ["We should let them decide", "उन्हें फैसला करने दें", "unheṃ faislā karne deṃ"],
                    ["Let’s meet at five", "पाँच बजे मिलते हैं", "pā̃c baje milte haiṃ"],
                    ["May I come in?", "क्या मैं अंदर आ सकता हूँ?", "kyā main andar ā saktā hū̃?"],
                    ["Let’s hope for the best", "अच्छे की आशा करते हैं", "acche kī āśā karte haiṃ"],
                ],
            ),
        ],
    )


def chapter_558() -> dict:
    return _l(
        "Relative clauses: जो … वह/वे — ‘the one who …’ / ‘what …’.",
        "जो किताब मैंने पढ़ी वह अच्छी थी — the book that I read was good.",
        [
            _p("Pattern", "जो introduces the clause; correlative वह/वे picks up the head."),
            _t(
                "Which-that / what-that",
                [
                    ["The boy who came", "जो लड़का आया", "jo laṛkā āyā"],
                    ["What you said is true", "जो तुमने कहा वह सच है", "jo tumne kahā vah sac hai"],
                    ["The house that I bought", "जो घर मैंने खरीदा", "jo ghar mainne kharīdā"],
                    ["I know what he wants", "मुझे पता है वह क्या चाहता है", "mujhe patā hai vah kyā cāhtā hai"],
                    ["The people who work here", "जो लोग यहाँ काम करते हैं", "jo log yahā̃ kām karte haiṃ"],
                    ["Whatever happens", "जो होगा देखा जाएगा", "jo hogā dekhā jāegā"],
                    ["The reason why I came", "जिस वजह से मैं आया", "jis vajah se main āyā"],
                    ["That is what I meant", "मेरा मतलब यही था", "merā matlab yahī thā"],
                    ["She saw what we did", "उसने देखा जो हमने किया", "usne dekhā jo hamne kiyā"],
                    ["The book which you gave", "जो किताब तुमने दी", "jo kitāb tumne dī"],
                    ["I remember where we met", "मुझे याद है जहाँ हम मिले", "mujhe yād hai jahā̃ ham mile"],
                    ["Tell me who called", "बताओ किसने फोन किया", "batāo kisne phon kiyā"],
                    ["Nothing that he says", "जो वह कहता है कुछ नहीं", "jo vah kahtā hai kuch nahī̃"],
                    ["The way she walks", "जिस तरह वह चलती है", "jis tarah vah caltī hai"],
                    ["All that glitters", "जो चमकता है", "jo camaktā hai"],
                    ["This is the same pen I lost", "यह वही कलम है जो खो गई", "yah vahī kalam hai jo kho gaī"],
                ],
            ),
        ],
    )


def chapter_559() -> dict:
    return _l(
        "Formal tone: कृपया + polite imperative; passive-style: किया जाए; निर्देशानुसार — as instructed.",
        "Documents: उपरोक्त अनुसार पालन करें — comply as above.",
        [
            _p("Register", "कृपया + verb + इए; कृपया ध्यान दें — please note."),
            _t(
                "Formal instructions",
                [
                    ["Please submit by Monday", "कृपया सोमवार तक जमा करें", "kripayā somvār tak jamā kareṃ"],
                    ["Kindly sign here", "कृपया यहाँ हस्ताक्षर करें", "kripayā yahā̃ hastākṣar kareṃ"],
                    ["Please do not smoke", "कृपया धूम्रपान न करें", "kripayā dhūmrapān na kareṃ"],
                    ["Follow the rules", "नियमों का पालन करें", "niyamõ kā pālan kareṃ"],
                    ["Report to the office", "कार्यालय में रिपोर्ट करें", "kāryālay mẽ ripoṭ kareṃ"],
                    ["Please wait in line", "कृपया कतार में प्रतीक्षा करें", "kripayā katār mẽ pratīkṣā kareṃ"],
                    ["Employees must wear ID", "कर्मचारी पहचान पत्र अवश्य पहनें", "karmacārī pahcān patr avaśy pahaneṃ"],
                    ["This should be completed", "यह पूर्ण किया जाना चाहिए", "yah pūrṇ kiyā jānā cāhie"],
                    ["Please find attached", "संलग्न देखें", "sannagn dekheṃ"],
                    ["For any query contact us", "किसी प्रश्न के लिए संपर्क करें", "kisī praśn ke lie sampark kareṃ"],
                    ["Maintain silence", "मौन रखें", "maun rakheṃ"],
                    ["Enter after permission", "अनुमति के बाद प्रवेश करें", "anumati ke bād praveś kareṃ"],
                    ["Please verify details", "कृपया विवरण सत्यापित करें", "kripayā vivaraṇ satyāpit kareṃ"],
                    ["Meeting is compulsory", "बैठक अनिवार्य है", "baiṭhak anivāry hai"],
                    ["Dress code applies", "पोशाक संहिता लागू है", "pośāk saṃhitā lāgū hai"],
                    ["Thank you for cooperation", "सहयोग के लिए धन्यवाद", "sahayog ke lie dhanyavād"],
                ],
            ),
        ],
    )


def chapter_560() -> dict:
    return _l(
        "Liking: पसंद है + dative subject; पसंद करना for ‘to like (doing)’.",
        "मुझे संगीत पसंद है — I like music.",
        [
            _p("Pattern", "मुझे चाय पसंद नहीं — I don’t like tea."),
            _t(
                "To like",
                [
                    ["I like music", "मुझे संगीत पसंद है", "mujhe saṅgīt pasand hai"],
                    ["She likes movies", "उसे फ़िल्में पसंद हैं", "use filmeṃ pasand haiṃ"],
                    ["I don’t like lies", "मुझे झूठ पसंद नहीं", "mujhe jhūṭh pasand nahī̃"],
                    ["Do you like spicy food?", "क्या आपको मसालेदार खाना पसंद है?", "kyā āpko masāledār khānā pasand hai?"],
                    ["We like this place", "हमें यह जगह पसंद है", "hameṃ yah jagah pasand hai"],
                    ["He likes to read", "उसे पढ़ना पसंद है", "use paṛhnā pasand hai"],
                    ["I liked the song", "मुझे गाना पसंद आया", "mujhe gānā pasand āyā"],
                    ["Children like sweets", "बच्चों को मिठाई पसंद है", "baccõ ko miṭhāī pasand hai"],
                    ["I prefer tea to coffee", "मुझे चाय कॉफ़ी से ज़्यादा पसंद है", "mujhe cāy kŏfī se zyādā pasand hai"],
                    ["Nobody likes waiting", "किसी को इंतज़ार पसंद नहीं", "kisī ko intazār pasand nahī̃"],
                    ["She likes him", "उसे वह पसंद है", "use vah pasand hai"],
                    ["I like walking", "मुझे टहलना पसंद है", "mujhe ṭahalnā pasand hai"],
                    ["They like your idea", "उन्हें आपका विचार पसंद है", "unheṃ āpkā vicār pasand hai"],
                    ["I used to like it", "मुझे पहले पसंद था", "mujhe pahle pasand thā"],
                    ["How do you like Delhi?", "आपको दिल्ली कैसी लगी?", "āpko dillī kaisī lagī?"],
                    ["I love this book", "मुझे यह किताब बहुत पसंद है", "mujhe yah kitāb bahut pasand hai"],
                ],
            ),
        ],
    )


def chapter_561() -> dict:
    return _l(
        "Habitual ‘would’: कहता था, जाते थे; polite ‘would like’: चाहूँगा; conditional: होता तो.",
        "मैं सोचता था = I would think (used to). मैं आऊँगा = I will come; मैं आना चाहूँगा = I would like to come.",
        [
            _p("Soft requests", "क्या आप मदद करेंगे? — would you help? (future polite)."),
            _t(
                "Would",
                [
                    ["I would visit every week", "मैं हर हफ़्ते जाता था", "main har haftā jātā thā"],
                    ["She would sing for us", "वह हमारे लिए गाती थी", "vah hamāre lie gātī thī"],
                    ["Would you sit?", "क्या आप बैठेंगे?", "kyā āp baiṭheṃge?"],
                    ["I would like tea", "मुझे चाय चाहिए / मैं चाय लूँगा", "mujhe cāhie / main cāy lū̃gā"],
                    ["I would have come", "मैं आ जाता", "main ā jātā"],
                    ["If I were you, I would wait", "मैं आपकी जगह होता तो इंतज़ार करता", "main āpkī jagah hotā to intazār kartā"],
                    ["He would never agree", "वह कभी नहीं मानता था", "vah kabhī nahī̃ māntā thā"],
                    ["Would you mind closing?", "क्या आप बंद कर देंगे?", "kyā āp band kar deṃge?"],
                    ["We would meet often", "हम अक्सर मिलते थे", "ham aksar milte the"],
                    ["That would be fine", "वह ठीक रहेगा", "vah ṭhīk rahegā"],
                    ["I would rather walk", "मैं पैदल ही जाना चाहूँगा", "main paidal hī jānā cāhū̃gā"],
                    ["She said she would call", "उसने कहा वह फोन करेगी", "usne kahā vah phon karegī"],
                    ["It would rain often", "अक्सर बारिश होती थी", "aksar bāriś hotī thī"],
                    ["Would that be possible?", "क्या यह संभव होगा?", "kyā yah saṃbhav hogā?"],
                    ["I would never forget", "मैं कभी नहीं भूलूँगा", "main kabhī nahī̃ bhūlū̃gā"],
                    ["They would help always", "वे हमेशा मदद करते थे", "ve hameśā madad karte the"],
                ],
            ),
        ],
    )


def chapter_562() -> dict:
    return _l(
        "Understand: समझना; realize/learn: समझ आना, पता चलना — ‘come to know’.",
        "मुझे समझ आ गया — I understood / it dawned on me.",
        [
            _p("Frames", "बात समझ में आई — I got the point. मालूम पड़ा — I found out."),
            _t(
                "Understand / come to know",
                [
                    ["I understand Hindi", "मैं हिन्दी समझता हूँ", "main hindī samajhtā hū̃"],
                    ["Do you understand?", "क्या समझे?", "kyā samjhe?"],
                    ["I didn’t understand", "मुझे समझ नहीं आया", "mujhe samajh nahī̃ āyā"],
                    ["Suddenly I understood", "अचानक मुझे समझ आ गया", "acānak mujhe samajh ā gayā"],
                    ["I came to know yesterday", "मुझे कल पता चला", "mujhe kal patā calā"],
                    ["She explained until I understood", "उसने समझाया जब तक मैं समझ न गया", "usne samjhāyā jab tak main samajh na gayā"],
                    ["I get your point", "मेरी समझ में आ गया", "merī samajh mẽ ā gayā"],
                    ["He pretends not to understand", "वह समझने का नाटक करता है", "vah samajhne kā nāṭak kartā hai"],
                    ["We understand each other", "हम एक दूसरे को समझते हैं", "ham ek dūsre ko samajhte haiṃ"],
                    ["It is hard to understand", "समझना मुश्किल है", "samajhnā muśkil hai"],
                    ["I realized my mistake", "मुझे अपनी गलती समझ आई", "mujhe apanī galtī samajh āī"],
                    ["Nobody told me", "मुझे किसी ने नहीं बताया", "mujhe kisī ne nahī̃ batāyā"],
                    ["I heard the news", "मुझे ख़बर मिल गई", "mujhe khabar mil gaī"],
                    ["Now I know the truth", "अब मुझे सच पता है", "ab mujhe sac patā hai"],
                    ["Explain again", "फिर से समझाइए", "phir se samjhāie"],
                    ["I misunderstood you", "मैंने आपको गलत समझा", "mainne āpko galat samjhā"],
                ],
            ),
        ],
    )


def chapter_563() -> dict:
    return _l(
        "Tags: ना?, है ना?, नहीं? — seeking confirmation.",
        "तुम आओगे ना? — you’ll come, right?",
        [
            _p("Tone", "है ना softens statements: अच्छा है ना — it’s nice, isn’t it."),
            _t(
                "Question tags",
                [
                    ["You will come, right?", "तुम आओगे ना?", "tum āoge nā?"],
                    ["It’s good, isn’t it?", "अच्छा है ना?", "acchā hai nā?"],
                    ["You know him, don’t you?", "तुम उसे जानते हो ना?", "tum use jānte ho nā?"],
                    ["Let’s go, okay?", "चलो ना?", "calo nā?"],
                    ["You aren’t angry, right?", "तुम नाराज़ नहीं हो ना?", "tum nārāz nahī̃ ho nā?"],
                    ["She can drive, can’t she?", "वह गाड़ी चला लेती है ना?", "vah gāṛī calā letī hai nā?"],
                    ["We met before, no?", "हम पहले मिले हैं ना?", "ham pahle mile haiṃ nā?"],
                    ["It’s true, isn’t it?", "सच है ना?", "sac hai nā?"],
                    ["Don’t forget, okay?", "भूलना मत ना", "bhūlnā mat nā"],
                    ["You’re joking, right?", "मज़ाक कर रहे हो ना?", "mazāk kar rahe ho nā?"],
                    ["Everything is fine, no?", "सब ठीक है ना?", "sab ṭhīk hai nā?"],
                    ["He will pay, won’t he?", "वह दे देगा ना?", "vah de degā nā?"],
                    ["See you tomorrow, yeah?", "कल मिलते हैं ना?", "kal milte haiṃ nā?"],
                    ["You understand, right?", "समझ गए ना?", "samajh ga.e nā?"],
                    ["It’s expensive, huh?", "महँगा है ना?", "mahṅgā hai nā?"],
                    ["We’re friends, aren’t we?", "हम दोस्त हैं ना?", "ham dost haiṃ nā?"],
                ],
            ),
        ],
    )


def chapter_564() -> dict:
    return _l(
        "Remember: याद रखना; forget: भूल जाना; remind: याद दिलाना.",
        "मुझे याद है — I remember; मुझे भूल गया — I forgot.",
        [
            _p("Frames", "याद आना = to come to mind; याद दिलाना = remind."),
            _t(
                "To remember",
                [
                    ["I remember your name", "मुझे आपका नाम याद है", "mujhe āpkā nām yād hai"],
                    ["I forgot the keys", "मुझे चाबी भूल गई", "mujhe cābī bhūl gaī"],
                    ["Please remind me", "मुझे याद दिला देना", "mujhe yād dilā denā"],
                    ["I can’t remember", "मुझे याद नहीं आ रहा", "mujhe yād nahī̃ ā rahā"],
                    ["Suddenly I remembered", "अचानक मुझे याद आया", "acānak mujhe yād āyā"],
                    ["Don’t forget to call", "फोन करना मत भूलना", "phon karnā mat bhūlnā"],
                    ["I remember that day", "मुझे वह दिन याद है", "mujhe vah din yād hai"],
                    ["She remembers everything", "उसे सब याद रहता है", "use sab yād rehtā hai"],
                    ["This song reminds me of home", "यह गाना मुझे घर की याद दिलाता है", "yah gānā mujhe ghar kī yād dilātā hai"],
                    ["I will never forget", "मैं कभी नहीं भूलूँगा", "main kabhī nahī̃ bhūlū̃gā"],
                    ["Write it down or you’ll forget", "लिख लो वरना भूल जाओगे", "likh lo varnā bhūl jāoge"],
                    ["I forgot what he said", "मुझे भूल गया उसने क्या कहा", "mujhe bhūl gayā usne kyā kahā"],
                    ["Memories fade", "यादें धुंधली हो जाती हैं", "yādeṃ dhundhlī ho jātī haiṃ"],
                    ["Remember to lock", "ताला लगाना याद रखना", "tālā lagānā yād rakhna"],
                    ["I remember seeing him", "मुझे याद है मैंने उसे देखा", "mujhe yād hai mainne use dekhā"],
                    ["Forget the past", "भूतकाल भूल जाओ", "bhūtkāl bhūl jāo"],
                ],
            ),
        ],
    )


def chapter_565() -> dict:
    return _l(
        "Want + infinitive: जाना चाहता हूँ; need + infinitive: जाना पड़ेगा.",
        "चाहती है कि मैं जाऊँ — she wants me to go.",
        [
            _p("Chains", "मैं खाना बनाना चाहता हूँ — I want to cook."),
            _t(
                "Want/need + other verbs",
                [
                    ["I want to learn", "मैं सीखना चाहता हूँ", "main sīkhnā cāhtā hū̃"],
                    ["We need to hurry", "हमें जल्दी करनी है", "hameṃ jaldī karnī hai"],
                    ["She wants to rest", "वह आराम करना चाहती है", "vah ārām karnā cāhtī hai"],
                    ["I don’t want to fight", "मैं झगड़ा नहीं करना चाहता", "main jhagaṛā nahī̃ karnā cāhtā"],
                    ["He needs to decide", "उसे फैसला करना है", "use faislā karnā hai"],
                    ["They want to leave", "वे जाना चाहते हैं", "ve jānā cāhte haiṃ"],
                    ["I wanted to ask", "मैं पूछना चाहता था", "main pūchnā cāhtā thā"],
                    ["You should want to improve", "आपको सुधार चाहिए", "āpko sudhār cāhie"],
                    ["We need to save money", "हमें पैसे बचाने हैं", "hameṃ paise bacāne haiṃ"],
                    ["I feel like sleeping", "मुझे सोने का मन है", "mujhe sone kā man hai"],
                    ["She refuses to come", "वह आने से इनकार करती है", "vah āne se inkār kartī hai"],
                    ["I am willing to help", "मैं मदद करने को तैयार हूँ", "main madad karne ko taiyār hū̃"],
                    ["He pretends to know", "वह जानने का नाटक करता है", "vah jānn kā nāṭak kartā hai"],
                    ["We hope to win", "हम जीतने की आशा रखते हैं", "ham jītne kī āśā rakhte haiṃ"],
                    ["I need to finish today", "मुझे आज ही खत्म करना है", "mujhe āj hī khatm karnā hai"],
                    ["They want us to wait", "वे चाहते हैं कि हम इंतज़ार करें", "ve cāhte haiṃ ki ham intazār kareṃ"],
                ],
            ),
        ],
    )


def chapter_566() -> dict:
    return _l(
        "Want for another person: चाहता है कि + clause; or dative: मैं चाहता हूँ कि वह आए.",
        "माँ चाहती हैं कि मैं पढ़ूँ — mother wants me to study.",
        [
            _p("Subjunctive-style", "कि introduces what someone wants someone else to do."),
            _t(
                "Want (other person)",
                [
                    ["I want you to stay", "मैं चाहता हूँ कि तुम रुको", "main cāhtā hū̃ ki tum ruko"],
                    ["She wants him to call", "वह चाहती है कि वह फोन करे", "vah cāhtī hai ki vah phon kare"],
                    ["Parents want children to study", "माता-पिता चाहते हैं बच्चे पढ़ें", "mātā-pitā cāhte haiṃ bacche paṛheṃ"],
                    ["We want them to agree", "हम चाहते हैं वे मान जाएँ", "ham cāhte haiṃ ve mān jāeṃ"],
                    ["He doesn’t want me to go", "वह नहीं चाहता मैं जाऊँ", "vah nahī̃ cāhtā main jāū̃"],
                    ["I wanted her to win", "मैं चाहता था वह जीते", "main cāhtā thā vah jīte"],
                    ["Boss wants work done", "मालिक चाहता है काम हो", "mālik cāhtā hai kām ho"],
                    ["They want us to wait", "वे चाहते हैं हम इंतज़ार करें", "ve cāhte haiṃ ham intazār kareṃ"],
                    ["Who wants me to leave?", "कौन चाहता है मैं जाऊँ?", "kaun cāhtā hai main jāū̃?"],
                    ["I only want peace", "मैं केवल शांति चाहता हूँ", "main keval śānti cāhtā hū̃"],
                    ["She wants the truth", "वह सच चाहती है", "vah sac cāhtī hai"],
                    ["We want everyone safe", "हम चाहते हैं सब सुरक्षित रहें", "ham cāhte haiṃ sab surakṣit raheṃ"],
                    ["He wants me to understand", "वह चाहता है मैं समझूँ", "vah cāhtā hai main samjhū̃"],
                    ["I want nothing from you", "मुझे आपसे कुछ नहीं चाहिए", "mujhe āpse kuch nahī̃ cāhie"],
                    ["They want her to sing", "वे चाहते हैं वह गाए", "ve cāhte haiṃ vah gā.e"],
                    ["God willing", "ख़ुदा करे", "xudā kare"],
                ],
            ),
        ],
    )


def chapter_567() -> dict:
    return _l(
        "Expectation: होना चाहिए tha — was supposed to; नियत था — planned.",
        "मुझे वहाँ होना चाहिए था — I was supposed to be there.",
        [
            _p("Pattern", "चाहिए था for unmet expectation; वाला था for ‘was going to’."),
            _t(
                "Supposed to",
                [
                    ["I was supposed to call", "मुझे फोन करना चाहिए था", "mujhe phon karnā cāhie thā"],
                    ["The train was supposed to arrive", "ट्रेन आनी चाहिए थी", "ṭren ānī cāhie thī"],
                    ["We are supposed to follow this", "हमें यह मानना चाहिए", "hameṃ yah mānnā cāhie"],
                    ["He was supposed to pay", "उसे भुगतान करना चाहिए था", "use bhugtān karnā cāhie thā"],
                    ["What was I supposed to do?", "मुझे क्या करना चाहिए था?", "mujhe kyā karnā cāhie thā?"],
                    ["You’re not supposed to park here", "यहाँ पार्किंग मना है", "yahā̃ pārkiṅg manā hai"],
                    ["It was supposed to rain", "बारिश होनी चाहिए थी", "bāriś honī cāhie thī"],
                    ["We were supposed to meet", "हमें मिलना चाहिए था", "hameṃ milnā cāhie thā"],
                    ["The meeting is supposed to start", "मीटिंग शुरू होनी चाहिए", "mīṭiṅ śurū honī cāhie"],
                    ["I thought it was supposed to be easy", "मुझे लगा यह आसान होगा", "mujhe lagā yah āsān hogā"],
                    ["They were supposed to help", "उन्हें मदद करनी चाहिए थी", "unheṃ madad karnī cāhie thī"],
                    ["Am I supposed to sign?", "क्या मुझे हस्ताक्षर करने हैं?", "kyā mujhe hastākṣar karne haiṃ?"],
                    ["This was supposed to work", "यह काम करना चाहिए था", "yah kām karnā cāhie thā"],
                    ["Nobody told me I was supposed to come", "किसी ने नहीं कहा मुझे आना था", "kisī ne nahī̃ kahā mujhe ānā thā"],
                    ["You’re supposed to be resting", "आपको आराम करना चाहिए", "āpko ārām karnā cāhie"],
                    ["We’re supposed to leave early", "हमें जल्दी निकलना है", "hameṃ jaldī nikalnā hai"],
                ],
            ),
        ],
    )


def chapter_568() -> dict:
    return _l(
        "Like + gerund: पसंद है … करना; enjoy doing: मज़ा आना.",
        "मुझे दौड़ना पसंद है — I like running.",
        [
            _p("Pattern", "Infinitive as noun: पढ़ना पसंद है."),
            _t(
                "Like + verbs",
                [
                    ["I like swimming", "मुझे तैरना पसंद है", "mujhe tairnā pasand hai"],
                    ["She likes dancing", "उसे नाचना पसंद है", "use nācnā pasand hai"],
                    ["We like traveling", "हमें घूमना पसंद है", "hameṃ ghūmnā pasand hai"],
                    ["I don’t like waiting", "मुझे इंतज़ार पसंद नहीं", "mujhe intazār pasand nahī̃"],
                    ["He likes cooking for friends", "उसे दोस्तों के लिए खाना बनाना पसंद है", "use dostõ ke lie khānā banānā pasand hai"],
                    ["I enjoy reading novels", "मुझे उपन्यास पढ़ने में मज़ा आता है", "mujhe upanyās paṛhne mẽ mazā ātā hai"],
                    ["Kids love playing", "बच्चों को खेलना पसंद है", "baccõ ko khelnā pasand hai"],
                    ["I prefer walking to driving", "मुझे चलाना गाड़ी चलाने से ज़्यादा पसंद है", "mujhe calānā gāṛī calāne se zyādā pasand hai"],
                    ["She likes to sing softly", "उसे धीरे गाना पसंद है", "use dhīre gānā pasand hai"],
                    ["We liked watching that film", "हमें वह फ़िल्म देखना पसंद आया", "hameṃ vah film dekhna pasand āyā"],
                    ["I hate lying", "मुझे झूठ बोलना पसंद नहीं", "mujhe jhūṭh bolna pasand nahī̃"],
                    ["They like helping", "उन्हें मदद करना पसंद है", "unheṃ madad karnā pasand hai"],
                    ["Do you like working here?", "क्या आपको यहाँ काम करना पसंद है?", "kyā āpko yahā̃ kām karnā pasand hai?"],
                    ["I like how you teach", "मुझे आपका पढ़ाना पसंद है", "mujhe āpkā paṛhānā pasand hai"],
                    ["She doesn’t like getting up early", "उसे जल्दी उठना पसंद नहीं", "use jaldī uṭhnā pasand nahī̃"],
                    ["We love hearing your stories", "हमें आपकी कहानियाँ सुनना पसंद है", "hameṃ āpkī kahāniā̃ sunnā pasand hai"],
                ],
            ),
        ],
    )


def chapter_569() -> dict:
    return _l(
        "Psychological verbs + को: समझ आना, पसंद आना, सूझना — experiencer subject often dative.",
        "मुझे यह पसंद आया — I liked it (it pleased me).",
        [
            _p("Agreement", "Sometimes the stimulus is subject: फ़िल्म अच्छी लगी."),
            _t(
                "Verb + to (experiencer)",
                [
                    ["I liked the movie", "मुझे फ़िल्म पसंद आई", "mujhe film pasand āī"],
                    ["The idea occurred to me", "मुझे विचार आया", "mujhe vicār āyā"],
                    ["It seems good to me", "मुझे अच्छा लगता है", "mujhe acchā lagtā hai"],
                    ["I find Hindi easy", "मुझे हिन्दी आसान लगती है", "mujhe hindī āsān lagtī hai"],
                    ["She feels cold", "उसे ठंड लग रही है", "use thaṃḍ lag rahī hai"],
                    ["I remembered suddenly", "मुझे अचानक याद आया", "mujhe acānak yād āyā"],
                    ["This suits you", "यह आप पर अच्छा लगेगा", "yah āpar acchā lagegā"],
                    ["I am afraid of dogs", "मुझे कुत्तों से डर लगता है", "mujhe kuttõ se ḍar lagtā hai"],
                    ["He feels proud", "उसे गर्व हो रहा है", "use garv ho rahā hai"],
                    ["We trust you", "हमें आप पर भरोसा है", "hameṃ āpar bharosā hai"],
                    ["I agree with you", "मेरी आपसे सहमति है", "merī āp se sahamti hai"],
                    ["It hurt me", "मुझे दर्द हुआ", "mujhe dard huā"],
                    ["She is angry at him", "उसे उस पर गुस्सा आया", "use us par gussā āyā"],
                    ["I don’t feel like eating", "मुझे खाने का मन नहीं", "mujhe khāne kā man nahī̃"],
                    ["That sounds fine", "वह ठीक लगता है", "vah ṭhīk lagtā hai"],
                    ["I understood the lesson", "मुझे पाठ समझ आया", "mujhe pāṭh samajh āyā"],
                ],
            ),
        ],
    )


def chapter_570() -> dict:
    return _l(
        "Colloquial shortenings: वो, फिर, अभी, बस, हाँ, ना; dropping मैं in fast speech.",
        "Spoken: मैंने→often मैं ने slurred; वह→वो.",
        [
            _p("Tips", "Learn to recognize वो, ऐसे, फिर भी in conversation."),
            _t(
                "Short forms",
                [
                    ["that / he / she (colloq.)", "वो", "vo"],
                    ["yes", "हाँ", "hā̃"],
                    ["okay / only", "बस", "bas"],
                    ["then / so", "फिर", "phir"],
                    ["now", "अभी", "abhī"],
                    ["like this", "ऐसे", "aise"],
                    ["nothing else", "और कुछ नहीं", "aur kuch nahī̃"],
                    ["I don’t know (casual)", "पता नहीं", "patā nahī̃"],
                    ["What’s up?", "क्या हाल है?", "kyā hāl hai?"],
                    ["See you", "फिर मिलेंगे", "phir mileṅge"],
                    ["Gotta go", "चलता हूँ", "caltā hū̃"],
                    ["No problem", "कोई नहीं", "koī nahī̃"],
                    ["Really?", "सच में?", "sac mẽ?"],
                    ["Let’s see", "देखते हैं", "dekhte haiṃ"],
                    ["I’m leaving (m.)", "मैं चलता हूँ", "main caltā hū̃"],
                    ["Where to? (casual)", "कहाँ को?", "kahā̃ ko?"],
                ],
            ),
        ],
    )


# --- 571–596 ---


def chapter_571() -> dict:
    return _l(
        "नमस्ते, नमस्कार; शुभकामनाएँ; जन्मदिन मुबारक; जय हिन्द — greetings and slogans.",
        "Time-based: सुप्रभात, शुभ रात्रि.",
        [
            _p("Occasions", "शादी की बधाई — wedding wishes; ईद मुबारक — festival greetings."),
            _t(
                "Greetings & wishes",
                [
                    ["Hello / Namaste", "नमस्ते", "namaste"],
                    ["Good morning", "सुप्रभात", "suprabhāt"],
                    ["Good night", "शुभ रात्रि", "śubh rātri"],
                    ["Happy birthday", "जन्मदिन मुबारक", "janmdin mubārak"],
                    ["Congratulations", "बधाई हो", "badhāī ho"],
                    ["Get well soon", "जल्दी ठीक हो जाओ", "jaldī ṭhīk ho jāo"],
                    ["Happy New Year", "नया साल मुबारक", "nayā sāl mubārak"],
                    ["Happy journey", "शुभ यात्रा", "śubh yātrā"],
                    ["May you prosper", "आप खुश रहें", "āp khush raheṃ"],
                    ["Long live India", "भारत माता की जय", "bhārat mātā kī jay"],
                    ["Victory to truth", "सत्यमेव जयते", "satyameva jayate"],
                    ["Welcome", "स्वागत है", "svāgat hai"],
                    ["Thank you", "धन्यवाद", "dhanyavād"],
                    ["Sorry", "माफ़ करें", "māf kareṃ"],
                    ["Good luck", "शुभकामनाएँ", "śubhkāmnāeṃ"],
                    ["Rest in peace", "भगवान आत्मा को शांति दे", "bhagvān ātmā ko śānti de"],
                ],
            ),
        ],
    )


def chapter_572() -> dict:
    return _l(
        "Light verbs: देना, लेना, जाना with main verb — कर देना, उठ लेना, चला जाना.",
        "Adds nuance: completion, benefit, movement.",
        [
            _p("Examples", "पढ़ लेना ‘read through’; खा लेना ‘eat up’; देख लेना ‘take a look’."),
            _t(
                "Compound verbs (phrases)",
                [
                    ["finish eating", "खा लेना", "khā lenā"],
                    ["read through", "पढ़ लेना", "paṛh lenā"],
                    ["throw away", "फेंक देना", "pheṅk denā"],
                    ["bring along", "ले आना", "le ānā"],
                    ["go away", "चला जाना", "calā jānā"],
                    ["sit down", "बैठ जाना", "baiṭh jānā"],
                    ["wake up", "उठ जाना", "uṭh jānā"],
                    ["look carefully", "देख लेना", "dekh lenā"],
                    ["I finished the work", "मैंने काम कर दिया", "mainne kām kar diyā"],
                    ["She fell asleep", "वह सो गई", "vah so gaī"],
                    ["We sold the car", "हमने गाड़ी बेच दी", "hamne gāṛī bec dī"],
                    ["He opened the door", "उसने दरवाज़ा खोल दिया", "usne darvāzā khol diyā"],
                    ["Take this", "यह ले लो", "yah le lo"],
                    ["Give it back", "वापस कर दो", "vāpas kar do"],
                    ["Come here", "यहाँ आ जाओ", "yahā̃ ā jāo"],
                    ["Don’t forget", "भूल मत जाना", "bhūl mat jānā"],
                ],
            ),
        ],
    )


def chapter_573() -> dict:
    return _l(
        "Titles: जी, साहब, जी; family: भैया, दीदी, चाचा; respectful: श्री, श्रीमती.",
        "आप + plural verb when addressing elders.",
        [
            _p("Politeness", "Teacher: अध्यापक जी; stranger: भैया/बहन."),
            _t(
                "Addressing people",
                [
                    ["sir (respect)", "साहब / जी", "sāhab / jī"],
                    ["brother (friendly)", "भैया", "bhaiyā"],
                    ["sister (friendly)", "दीदी", "dīdī"],
                    ["uncle", "चाचा / अंकल", "cācā / aṅkal"],
                    ["aunt", "चाची / आंटी", "cācī / āṃṭī"],
                    ["grandfather", "दादा", "dādā"],
                    ["grandmother", "दादी", "dādī"],
                    ["teacher", "गुरु जी / अध्यापक जी", "guru jī / adhyāpak jī"],
                    ["Excuse me, sir", "माफ़ कीजिए जी", "māf kījie jī"],
                    ["Listen, brother", "सुनो भैया", "suno bhaiyā"],
                    ["Mother, please", "माँ जी", "mā̃ jī"],
                    ["Doctor sahib", "डॉक्टर साहब", "ḍokṭar sāhab"],
                    ["Everyone", "सज्जनों", "sajjanõ"],
                    ["Ladies and gentlemen", "देवियों और सज्जनों", "deviyõ aur sajjanõ"],
                    ["Respected elders", "बुज़ुर्गों", "buzurgõ"],
                    ["Young man", "लड़के", "laṛke"],
                ],
            ),
        ],
    )


def chapter_574() -> dict:
    return _l(
        "Exclamations: अरे!, वाह!, हाय!, शाबाश!, अफ़सोस! — surprise, praise, pity.",
        "ओहो for mild surprise; अच्छा for ‘oh I see’.",
        [
            _p("Intensity", "अरे यार — friendly frustration."),
            _t(
                "Exclamations",
                [
                    ["Oh!", "अरे!", "are!"],
                    ["Wow!", "वाह!", "vāh!"],
                    ["Alas!", "हाय!", "hāy!"],
                    ["Bravo!", "शाबाश!", "śābāś!"],
                    ["What a pity!", "कितना बुरा!", "kitnā burā!"],
                    ["Ouch!", "ओह!", "oh!"],
                    ["Hey!", "अरे सुनो!", "are suno!"],
                    ["Really?!", "वाकई?!", "vākai?!"],
                    ["How beautiful!", "कितना सुंदर!", "kitnā sundar!"],
                    ["Thank heavens!", "शुक्र है!", "śukr hai!"],
                    ["What nonsense!", "क्या बकवास!", "kyā bakvās!"],
                    ["So sweet!", "कितना प्यारा!", "kitnā pyārā!"],
                    ["I’m shocked!", "हैरान हूँ!", "hairān hū̃!"],
                    ["Good grief!", "हे भगवान!", "he bhagvān!"],
                    ["Well done!", "बहुत बढ़िया!", "bahut baṛhiyā!"],
                    ["No way!", "कभी नहीं!", "kabhī nahī̃!"],
                ],
            ),
        ],
    )


def chapter_575() -> dict:
    return _l(
        "Polite requests: कृपया; क्या मैं …?; क्या आप … सकते हैं? — May I / Can you.",
        "मेरी एक विनती है — I have a humble request.",
        [
            _p("Softeners", "ज़रा … दीजिए — please give a little …"),
            _t(
                "Requests",
                [
                    ["May I come in?", "क्या मैं अंदर आ सकता हूँ?", "kyā main andar ā saktā hū̃?"],
                    ["Can you help me?", "क्या आप मेरी मदद कर सकते हैं?", "kyā āp merī madad kar sakte haiṃ?"],
                    ["Please pass the salt", "कृपया नमक दीजिए", "kripayā namak dījie"],
                    ["Could you repeat?", "क्या आप दोहरा सकते हैं?", "kyā āp dohrā sakte haiṃ?"],
                    ["Would you mind waiting?", "क्या आप थोड़ा इंतज़ार कर सकते हैं?", "kyā āp thoṛā intazār kar sakte haiṃ?"],
                    ["Please be quiet", "कृपया चुप रहिए", "kripayā cup rahie"],
                    ["May I ask something?", "क्या मैं कुछ पूछ सकता हूँ?", "kyā main kuch pūch saktā hū̃?"],
                    ["Lend me a pen", "कलम उधार दीजिए", "kalam udhār dījie"],
                    ["Please don’t smoke", "कृपया धूम्रपान न करें", "kripayā dhūmrapān na kareṃ"],
                    ["Can I pay later?", "क्या मैं बाद में भर सकता हूँ?", "kyā main bād mẽ bhar saktā hū̃?"],
                    ["Would you check this?", "क्या आप यह देख सकते हैं?", "kyā āp yah dekh sakte haiṃ?"],
                    ["Please forgive me", "कृपया मुझे माफ़ करें", "kripayā mujhe māf kareṃ"],
                    ["Could you call a taxi?", "क्या आप टैक्सी बुला सकते हैं?", "kyā āp ṭaiksī bulā sakte haiṃ?"],
                    ["May we sit here?", "क्या हम यहाँ बैठ सकते हैं?", "kyā ham yahā̃ baiṭh sakte haiṃ?"],
                    ["Please inform me", "कृपया मुझे सूचित करें", "kripayā mujhe sūcit kareṃ"],
                    ["Can you speak slowly?", "क्या आप धीरे बोल सकते हैं?", "kyā āp dhīre bol sakte haiṃ?"],
                ],
            ),
        ],
    )


def chapter_576() -> dict:
    return _l(
        "Uncertainty: शायद, हो सकता है, शक है — may / might.",
        "मुझे लगता है … for soft belief.",
        [
            _p("Hedging", "शायद बारिश हो — it might rain."),
            _t(
                "May / might",
                [
                    ["Maybe he will come", "शायद वह आएगा", "śāyad vah āegā"],
                    ["It might rain", "हो सकता है बारिश हो", "ho saktā hai bāriś ho"],
                    ["I doubt it", "मुझे शक है", "mujhe śak hai"],
                    ["Perhaps you are right", "शायद आप सही हैं", "śāyad āp sahī haiṃ"],
                    ["She might be late", "वह देर से आ सकती है", "vah der se ā saktī hai"],
                    ["We might cancel", "हो सकता है हम रद्द करें", "ho saktā hai ham radd kareṃ"],
                    ["I’m not sure", "मुझे यकीन नहीं", "mujhe yakīn nahī̃"],
                    ["It could be true", "यह सच हो सकता है", "yah sac ho saktā hai"],
                    ["He may not agree", "वह मान न भी सके", "vah mān na bhī sake"],
                    ["Might as well go", "चले जाते हैं", "cale jāte haiṃ"],
                    ["Probably yes", "शायद हाँ", "śāyad hā̃"],
                    ["Probably not", "शायद नहीं", "śāyad nahī̃"],
                    ["There might be traffic", "ट्रैफ़िक हो सकता है", "ṭraifik ho saktā hai"],
                    ["I might have been wrong", "शायद मैं गलत था", "śāyad main galat thā"],
                    ["Who knows?", "कौन जाने?", "kaun jāne?"],
                    ["Anything can happen", "कुछ भी हो सकता है", "kuch bhī ho saktā hai"],
                ],
            ),
        ],
    )


def chapter_577() -> dict:
    return _l(
        "Participial adjectives: खाया हुआ, बना हुआ, लिखा हुआ — eaten, ready-made, written.",
        "Often before noun: ताज़ा कटा हुआ सलाद.",
        [
            _p("Pattern", "Past participle + हुआ agrees with noun."),
            _t(
                "Adjectives from verbs",
                [
                    ["boiled water", "उबला हुआ पानी", "ublā huā pānī"],
                    ["fried food", "तला हुआ खाना", "talā huā khānā"],
                    ["written answer", "लिखा हुआ उत्तर", "likhā huā uttar"],
                    ["broken chair", "टूटी हुई कुर्सी", "ṭūṭī huī kursī"],
                    ["lost keys", "खोई हुई चाबियाँ", "khoī huī cābiyā̃"],
                    ["newly painted wall", "नया रंग की हुई दीवार", "nayā raṅg kī huī dīvār"],
                    ["packed bags", "बंद किया हुआ सामान", "band kiyā huā sāmān"],
                    ["signed paper", "दस्तख़त किया हुआ कागज़", "dastaxat kiyā huā kāgaz"],
                    ["used car", "पुरानी इस्तेमाल की हुई गाड़ी", "purānī istemāl kī huī gāṛī"],
                    ["washed clothes", "धुले हुए कपड़े", "dhule hue kapṛe"],
                    ["I want cold water", "मुझे ठंडा पानी चाहिए", "mujhe thaṃḍā pānī cāhie"],
                    ["Give me roasted nuts", "मुझे भुनी हुई मूँगफली दो", "mujhe bhunī huī mū̃gphalī do"],
                    ["This is imported", "यह आयात किया हुआ है", "yah āyāt kiyā huā hai"],
                    ["Freshly cooked rice", "अभी पका हुआ चावल", "abhī pakā huā cāval"],
                    ["Torn page", "फटा हुआ पन्ना", "phaṭā huā pannā"],
                    ["Hidden camera", "छिपा हुआ कैमरा", "chipā huā kaimrā"],
                ],
            ),
        ],
    )


def chapter_578() -> dict:
    return _l(
        "Locative compounds as adjectives: ऊपर वाला ‘upper’, अंदर का ‘inner’, बाहर का ‘outer’.",
        "पीछे वाला कमरा — the room at the back.",
        [
            _p("Usage", "वाला agrees: ऊपर वाली मंज़िल."),
            _t(
                "Adjectives from prepositions",
                [
                    ["the upstairs room", "ऊपर वाला कमरा", "ūpar vālā kamrā"],
                    ["inner door", "अंदर वाला दरवाज़ा", "andar vālā darvāzā"],
                    ["outer lane", "बाहर वाली गली", "bāhar vālī galī"],
                    ["front seat", "आगे वाली सीट", "āge vālī sīṭ"],
                    ["back seat", "पीछे वाली सीट", "pīche vālī sīṭ"],
                    ["left side", "बाएँ वाला", "bāẽ vālā"],
                    ["right side", "दाएँ वाला", "dāẽ vālā"],
                    ["middle one", "बीच वाला", "bīc vālā"],
                    ["corner shop", "कोने वाली दुकान", "kone vālī dukān"],
                    ["neighbor upstairs", "ऊपर वाले", "ūpar vāle"],
                    ["the man from Delhi", "दिल्ली वाला आदमी", "dillī vālā ādmī"],
                    ["inside pocket", "अंदर वाली जेब", "andar vālī jeb"],
                    ["street-side stall", "सड़क वाला ठेला", "saṛak vālā ṭhelā"],
                    ["that-side person", "उधर वाला", "udhar vālā"],
                    ["nearby shop", "पास वाली दुकान", "pās vālī dukān"],
                    ["across-the-road house", "सामने वाला घर", "sāmne vālā ghar"],
                ],
            ),
        ],
    )


def chapter_579() -> dict:
    return _l(
        "Wishes with भगवान करे, काश — May God … / I wish ….",
        "काश मैं वहाँ होता — I wish I were there.",
        [
            _p("Blessings", "ख़ुदा हाफ़िज़ — goodbye (God protect)."),
            _t(
                "May (wish)",
                [
                    ["May you live long", "आप दीर्घायु हों", "āp dīrghāyu hoṃ"],
                    ["May God bless you", "भगवान आपका भला करे", "bhagvān āpkā bhala kare"],
                    ["I wish you success", "आपको सफलता मिले", "āpko saphlatā mile"],
                    ["May peace prevail", "शांति बनी रहे", "śānti banī rahe"],
                    ["I wish I could fly", "काश मैं उड़ सकता", "kāś main uṛ saktā"],
                    ["May it not rain", "बारिश न हो", "bāriś na ho"],
                    ["God willing", "इंशा अल्लाह / भगवान करे", "iṃśā allāh / bhagvān kare"],
                    ["May your dreams come true", "आपके सपने पूरे हों", "āp ke sapne pūre hoṃ"],
                    ["Wish you a happy life", "सुखी जीवन की कामना", "sukhī jīvan kī kāmnā"],
                    ["May everyone be well", "सब ठीक रहें", "sab ṭhīk raheṃ"],
                    ["I hope you recover", "आप जल्दी ठीक हों", "āp jaldī ṭhīk hoṃ"],
                    ["May this festival bring joy", "यह त्योहार खुशियाँ लाए", "yah tyohār khushiyā̃ lā.e"],
                    ["If only he understood", "काश वह समझता", "kāś vah samajhtā"],
                    ["May truth win", "सत्य की जय हो", "satya kī jay ho"],
                    ["Bless the child", "बच्चे पर कृपा हो", "bacce par kṛpā ho"],
                    ["May we meet again", "फिर मिलें", "phir mileṃ"],
                ],
            ),
        ],
    )


def chapter_580() -> dict:
    return _l(
        "Causative: करवाना, बनवाना, दिखवाना — make/have someone do.",
        "मैंने उससे काम करवाया — I got the work done by him.",
        [
            _p("Double causative", "पढ़वाना ‘get taught’."),
            _t(
                "Make someone do",
                [
                    ["get the house painted", "घर रंग करवाना", "ghar raṅg karvānā"],
                    ["make him speak", "उससे बुलवाना", "us se bulvānā"],
                    ["I got a letter written", "मैंने पत्र लिखवाया", "mainne patr likhvāyā"],
                    ["She made the child study", "उसने बच्चे से पढ़वाया", "usne bacce se paṛhvāyā"],
                    ["We had food cooked", "हमने खाना बनवाया", "hamne khānā banvāyā"],
                    ["Get this copied", "इसकी कॉपी करवाओ", "iskī kŏpī karvāo"],
                    ["He made me run", "उसने मुझसे दौड़वाया", "usne mujh se dauṛvāyā"],
                    ["Have the tyre fixed", "टायर ठीक करवाओ", "ṭāyar ṭhīk karvāo"],
                    ["Mother got clothes stitched", "माँ ने कपड़े सिलवाए", "mā̃ ne kapṛe silvā.e"],
                    ["Boss got the report made", "बॉस ने रिपोर्ट बनवाई", "bŏs ne ripoṭ banvāī"],
                    ["Don’t make me repeat", "दोहरवाना मत", "dohravānā mat"],
                    ["I will get him to sign", "मैं उससे दस्तख़त करवाऊँगा", "main us se dastaxat karvāū̃gā"],
                    ["We showed the city", "हमने शहर दिखवाया", "hamne śahar dikhvāyā"],
                    ["Get the form filled", "फ़ॉर्म भरवाओ", "phŏrm bharvāo"],
                    ["He had me call", "उसने मुझसे फोन करवाया", "usne mujh se phon karvāyā"],
                    ["She makes everyone laugh", "वह सबसे हँसवाती है", "vah sab se hãsvātī hai"],
                ],
            ),
        ],
    )


def chapter_581() -> dict:
    return _l(
        "Indefinites: कहीं, किसी, कुछ, कोई — somewhere, someone, something, anyone.",
        "Negation: कुछ नहीं, कहीं नहीं.",
        [
            _p("Any-", "कोई भी, कुछ भी — anyone, anything (colloquial)."),
            _t(
                "Generalizing words",
                [
                    ["somewhere", "कहीं", "kahī̃"],
                    ["somehow", "किसी तरह", "kisī tarah"],
                    ["something", "कुछ", "kuch"],
                    ["someone", "कोई", "koī"],
                    ["anywhere", "कहीं भी", "kahī̃ bhī"],
                    ["anything", "कुछ भी", "kuch bhī"],
                    ["anyone", "कोई भी", "koī bhī"],
                    ["nothing", "कुछ नहीं", "kuch nahī̃"],
                    ["nowhere", "कहीं नहीं", "kahī̃ nahī̃"],
                    ["I saw someone", "मैंने किसी को देखा", "mainne kisī ko dekhā"],
                    ["Something is wrong", "कुछ गड़बड़ है", "kuch gaṛbaṛ hai"],
                    ["Come anytime", "कभी भी आना", "kabhī bhī ānā"],
                    ["Search everywhere", "हर जगह ढूँढो", "har jagah ḍhū̃ḍho"],
                    ["Nobody came", "कोई नहीं आया", "koī nahī̃ āyā"],
                    ["Nothing works", "कुछ काम नहीं करता", "kuch kām nahī̃ kartā"],
                    ["Maybe somewhere", "शायद कहीं", "śāyad kahī̃"],
                ],
            ),
        ],
    )


def chapter_582() -> dict:
    return _l(
        "Possession: के पास है; relationship: का / की — मेरा भाई, मेरी माँ.",
        "मेरे पास समय नहीं — I don’t have time.",
        [
            _p("Existential", "घर में कार है — there is a car at home."),
            _t(
                "Have (possession)",
                [
                    ["I have a car", "मेरे पास कार है", "mere pās kār hai"],
                    ["She has two children", "उसके दो बच्चे हैं", "us ke do bacce haiṃ"],
                    ["We have no money", "हमारे पास पैसे नहीं", "hamāre pās paise nahī̃"],
                    ["He has a fever", "उसे बुखार है", "use bukhār hai"],
                    ["Do you have time?", "क्या आपके पास समय है?", "kyā āp ke pās samay hai?"],
                    ["I have an idea", "मेरे पास एक विचार है", "mere pās ek vicār hai"],
                    ["They have land", "उनके पास ज़मीन है", "unk pās zamīn hai"],
                    ["I don’t have siblings", "मेरे कोई भाई-बहन नहीं", "mere koī bhāī-bahan nahī̃"],
                    ["She has long hair", "उसके लंबे बाल हैं", "us ke lambe bāl haiṃ"],
                    ["We had a dog", "हमारे पास कुत्ता था", "hamāre pās kuttā thā"],
                    ["He has courage", "उसमें हिम्मत है", "us mẽ himmat hai"],
                    ["I have a question", "मेरा एक सवाल है", "merā ek savāl hai"],
                    ["India has diversity", "भारत में विविधता है", "bhārat mẽ vividhatā hai"],
                    ["I have nothing to say", "मेरे पास कहने को कुछ नहीं", "mere pās kahne ko kuch nahī̃"],
                    ["She has a good heart", "उसका दिल अच्छा है", "uskā dil acchā hai"],
                    ["We have each other", "हम एक दूसरे के हैं", "ham ek dūsre ke haiṃ"],
                ],
            ),
        ],
    )


def chapter_583() -> dict:
    return _l(
        "Meaning: मतलब, अर्थ, मायने — ‘to mean’.",
        "क्या मतलब? — what do you mean? यह क्या है? — what is this called?",
        [
            _p("Asking", "इसका हिन्दी में क्या कहते हैं? — what’s this called in Hindi?"),
            _t(
                "To mean / ask meaning",
                [
                    ["What does this mean?", "इसका क्या मतलब है?", "iskā kyā matlab hai?"],
                    ["I mean …", "मेरा मतलब है …", "merā matlab hai …"],
                    ["It means peace", "इसका अर्थ शांति है", "iskārth śānti hai"],
                    ["I didn’t mean that", "मेरा वह मतलब नहीं था", "merā vah matlab nahī̃ thā"],
                    ["What is this called?", "इसे क्या कहते हैं?", "ise kyā kahte haiṃ?"],
                    ["How do you say … in Hindi?", "… को हिन्दी में क्या कहते हैं?", "… ko hindī mẽ kyā kahte haiṃ?"],
                    ["Explain the word", "शब्द समझाइए", "śabd samjhāie"],
                    ["In other words", "दूसरे शब्दों में", "dūśre śabdõ mẽ"],
                    ["Literally", "शाब्दिक रूप से", "śābdik rūp se"],
                    ["Figuratively", "लाक्षणिक रूप से", "lākṣaṇik rūp se"],
                    ["That depends on context", "यह संदर्भ पर निर्भर है", "yah sandarbh par nirbhar hai"],
                    ["I misunderstood the meaning", "मैंने अर्थ गलत समझा", "mainne arth galat samjhā"],
                    ["What is the sense here?", "यहाँ क्या भाव है?", "yahā̃ kyā bhāv hai?"],
                    ["It has many meanings", "इसके कई अर्थ हैं", "iske kaī arth haiṃ"],
                    ["By X I mean Y", "X से मेरा मतलब Y है", "X se merā matlab Y hai"],
                    ["Look it up in the dictionary", "शब्दकोश में देखो", "śabdkoś mẽ dekho"],
                ],
            ),
        ],
    )


def chapter_584() -> dict:
    return _l(
        "Part 1: और, लेकिन, क्योंकि, इसलिए, कि, हालाँकि, फिर भी, अभी तक.",
        "क्योंकि gives reason; इसलिए gives result.",
        [
            _p("Pairs", "हालाँकि … फिर भी — although … still."),
            _t(
                "Conjunctions 1",
                [
                    ["and", "और", "aur"],
                    ["but", "लेकिन / पर", "lekin / par"],
                    ["because", "क्योंकि", "kyõki"],
                    ["so / therefore", "इसलिए", "islie"],
                    ["that (complementizer)", "कि", "ki"],
                    ["although", "हालाँकि", "hālãki"],
                    ["though", "यद्यपि / फिर भी", "yadyapi / phir bhī"],
                    ["still", "फिर भी", "phir bhī"],
                    ["yet", "फिर भी / अभी तक", "phir bhī / abhī tak"],
                    ["I came because you called", "मैं आया क्योंकि तुमने बुलाया", "main āyā kyõki tumne bulāyā"],
                    ["It rained so we stayed", "बारिश हुई इसलिए हम रुके", "bāriś huī islie ham ruke"],
                    ["He is poor but honest", "वह गरीब है लेकिन ईमानदार है", "vah garīb hai lekin īmāndār hai"],
                    ["Although tired, he worked", "हालाँकि थका था, फिर भी काम किया", "hālãki thakā thā, phir bhī kām kiyā"],
                    ["I think that it is true", "मुझे लगता है कि यह सच है", "mujhe lagtā hai ki yah sac hai"],
                    ["She tried yet failed", "उसने कोशिश की फिर भी हार गई", "usne kośiś kī phir bhī hār gaī"],
                    ["Speak slowly and clearly", "धीरे और साफ़ बोलो", "dhīre aur sāf bolo"],
                ],
            ),
        ],
    )


def chapter_585() -> dict:
    return _l(
        "Part 2: जैसा, या, न तो … न, अगर, अगर … तो, यदि, शायद.",
        "Neither … nor: न तो … न.",
        [
            _p("Either/or", "या … या — either … or (emphatic)."),
            _t(
                "Conjunctions 2",
                [
                    ["as / like", "जैसा", "jaisā"],
                    ["or", "या", "yā"],
                    ["neither … nor", "न … न / न तो … न भी", "na … na / na to … na bhī"],
                    ["if", "अगर / यदि", "agar / yadi"],
                    ["in case", "अगर कहीं", "agar kahī̃"],
                    ["provided that", "बशर्ते कि", "baśarte ki"],
                    ["Tea or coffee?", "चाय या कॉफ़ी?", "cāy yā kŏfī?"],
                    ["Neither he nor I", "न वह न मैं", "na vah na main"],
                    ["As you wish", "जैसा आप चाहें", "jaisā āp cāheṃ"],
                    ["If it rains", "अगर बारिश हुई", "agar bāriś huī"],
                    ["In case you forget", "अगर कहीं भूल जाओ", "agar kahī̃ bhūl jāo"],
                    ["You may go provided you finish", "जा सकते हो बशर्ते खत्म करो", "jā sakte ho baśarte khatm karo"],
                    ["Neither yes nor no", "ना हाँ न ना", "na hā̃ na nā"],
                    ["Like father like son", "जैसा बाप वैसा बेटा", "jaisā bāp vaisā beṭā"],
                    ["If not today then tomorrow", "आज नहीं तो कल", "āj nahī̃ to kal"],
                    ["Call if needed", "ज़रूरत हो तो फोन करना", "zarūrat ho to phon karnā"],
                ],
            ),
        ],
    )


def chapter_586() -> dict:
    return _l(
        "Part 3: जब, तब, फिर, जहाँ तक, जब तक, मानो.",
        "जब तक … तब तक — as long as / until.",
        [
            _p("Sequence", "पहले … फिर — first … then."),
            _t(
                "Conjunctions 3",
                [
                    ["after", "के बाद", "ke bād"],
                    ["then", "फिर / तब", "phir / tab"],
                    ["as far as", "जहाँ तक", "jahā̃ tak"],
                    ["as long as", "जब तक", "jab tak"],
                    ["as if", "मानो / जैसे", "māno / jaise"],
                    ["When he came, I left", "जब वह आया तब मैं चला गया", "jab vah āyā tab main calā gayā"],
                    ["After eating, sleep", "खाने के बाद सो जाओ", "khāne ke bād so jāo"],
                    ["First work then play", "पहले काम फिर मज़ा", "pahle kām phir mazā"],
                    ["As far as I know", "जहाँ तक मुझे पता है", "jahā̃ tak mujhe patā hai"],
                    ["Wait until I return", "जब तक मैं न आऊँ तब तक रुको", "jab tak main na āū̃ tab tak ruko"],
                    ["He talks as if he knows", "वह ऐसे बोलता है मानो सब जानता हो", "vah aise boltā hai māno sab jāntā ho"],
                    ["As long as we are together", "जब तक हम साथ हैं", "jab tak ham sāth haiṃ"],
                    ["Then what happened?", "फिर क्या हुआ?", "phir kyā huā?"],
                    ["After that we met", "उसके बाद हम मिले", "us ke bād ham mile"],
                    ["As far as this matter", "जहाँ तक यह मामला है", "jahā̃ tak yah māmlā hai"],
                    ["She sings as if in a dream", "वह गाती है जैसे सपने में हो", "vah gātī hai jaise sapne mẽ ho"],
                ],
            ),
        ],
    )


def chapter_587() -> dict:
    return _l(
        "Part 4: जैसे ही, एक बार, बजाय, के बजाय, ताकि.",
        "ताकि expresses purpose — so that.",
        [
            _p("Rather than", "के बजाय — instead of."),
            _t(
                "Conjunctions 4",
                [
                    ["as soon as", "जैसे ही", "jaise hī"],
                    ["once", "एक बार जब", "ek bār jab"],
                    ["rather than", "के बजाय", "ke bajāy"],
                    ["instead of", "के स्थान पर", "ke sthān par"],
                    ["so that", "ताकि", "tāki"],
                    ["As soon as I saw", "जैसे ही मैंने देखा", "jaise hī mainne dekhā"],
                    ["Once you start, don’t stop", "एक बार शुरू किया तो रुको मत", "ek bār śurū kiyā to ruko mat"],
                    ["Walk rather than drive", "गाड़ी के बजाय पैदल चलो", "gāṛī ke bajāy paidal calo"],
                    ["Instead of fighting, talk", "झगड़े के बजाय बात करो", "jhagaṛe ke bajāy bāt karo"],
                    ["Study so that you pass", "पढ़ो ताकि पास हो जाओ", "paṛho tāki pās ho jāo"],
                    ["Call so that I know", "फोन करो ताकि मुझे पता चले", "phon karo tāki mujhe patā cale"],
                    ["As soon as possible", "जितनी जल्दी हो सके", "jitnī jaldī ho sake"],
                    ["Once in a while", "कभी-कभी", "kabhī-kabhī"],
                    ["Rather late than never", "देर आए दुरुस्त आए", "der ā.e durust ā.e"],
                    ["He left so that we could talk", "वह चला गया ताकि हम बात कर सकें", "vah calā gayā tāki ham bāt kar sakeṃ"],
                    ["Instead of this, try that", "इसके बजाय वह करो", "iske bajāy vah karo"],
                ],
            ),
        ],
    )


def chapter_588() -> dict:
    return _l(
        "Quick reference list of Hindi connectors for reading and writing.",
        "Group by function: addition, contrast, cause, time, condition.",
        [
            _p("Tip", "Read news editorials to see these in long sentences."),
            _t(
                "List of conjunctions",
                [
                    ["and", "और", "aur"],
                    ["but", "लेकिन / परंतु", "lekin / parantu"],
                    ["or", "या", "yā"],
                    ["because", "क्योंकि / चूँकि", "kyõki / cū̃ki"],
                    ["so", "इसलिए / अतः", "islie / ataḥ"],
                    ["if", "अगर / यदि", "agar / yadi"],
                    ["when", "जब", "jab"],
                    ["while", "जबकि / जिस दौरान", "jabaki / jis daurān"],
                    ["although", "हालाँकि", "hālãki"],
                    ["until", "जब तक", "jab tak"],
                    ["after", "के बाद", "ke bād"],
                    ["before", "से पहले", "se pahle"],
                    ["as soon as", "जैसे ही", "jaise hī"],
                    ["so that", "ताकि", "tāki"],
                    ["that", "कि", "ki"],
                    ["namely", "अर्थात्", "arthāt"],
                    ["either … or", "या … या", "yā … yā"],
                ],
            ),
        ],
    )


def chapter_589() -> dict:
    return _l(
        "Join clauses with shared subjects or conjunctive adverbs: फिर, इसलिए, इसके अलावा.",
        "Avoid comma splices; use और, लेकिन, क्योंकि.",
        [
            _p("Writing", "Short sentences + और for simple lists."),
            _t(
                "Combining sentences",
                [
                    ["I woke up and drank tea", "मैं उठा और चाय पी", "main uṭhā aur cāy pī"],
                    ["She sang and danced", "वह गाई और नाची", "vah gāī aur nācī"],
                    ["He is tired but happy", "वह थका है लेकिन खुश है", "vah thakā hai lekin khush hai"],
                    ["Because it rained, we stayed", "क्योंकि बारिश हुई, हम रुके", "kyõki bāriś huī, ham ruke"],
                    ["First study then play", "पहले पढ़ो फिर खेलो", "pahle paṛho phir khelo"],
                    ["Besides this, note that", "इसके अलावा ध्यान दें कि", "iske alāvā dhyān deṃ ki"],
                    ["In addition, we need time", "इसके साथ हमें समय चाहिए", "iske sāth hameṃ samay cāhie"],
                    ["However, it is costly", "हालाँकि यह महँगा है", "hālãki yah mahṅgā hai"],
                    ["Therefore we left", "इसलिए हम चले गए", "islie ham cal ga.e"],
                    ["Meanwhile, call him", "इस बीच उसे फोन करो", "is bīc use phon karo"],
                    ["Otherwise we will miss", "वरना छूट जाएगा", "varnā chūṭ jāegā"],
                    ["Not only … but also", "न केवल … बल्कि", "na keval … balki"],
                    ["Both A and B", "A और B दोनों", "A aur B donõ"],
                    ["Either A or B", "या तो A या B", "yā to A yā B"],
                    ["Neither A nor B", "न A न B", "na A na B"],
                ],
            ),
        ],
    )


def chapter_590() -> dict:
    return _l(
        "Systematic compound verbs: aspectual light verbs (ले, दे, उठ, बैठ, रख, डाल).",
        "Contrast with lesson ‘Compound verbs / Phrases’ (572): here, grammar names and patterns.",
        [
            _p("Drill", "Same stem + different light verb = different nuance."),
            _t(
                "Compound verbs (grammar)",
                [
                    ["complete (give)", "कर देना", "kar denā"],
                    ["take for oneself", "ले लेना", "le lenā"],
                    ["start suddenly", "उठ बैठना", "uṭh baiṭhnā"],
                    ["put away", "रख देना", "rakh denā"],
                    ["throw in", "डाल देना", "ḍāl denā"],
                    ["eat up", "खा लेना", "khā lenā"],
                    ["read through", "पढ़ लेना", "paṛh lenā"],
                    ["sell off", "बेच देना", "bec denā"],
                    ["I read it (completion)", "मैंने पढ़ लिया", "mainne paṛh liyā"],
                    ["He gave me (benefactive)", "उसने मुझे दे दिया", "usne mujhe de diyā"],
                    ["She suddenly stood", "वह उठ खड़ी हुई", "vah uṭh khaṛī huī"],
                    ["We set out", "हम निकल पड़े", "ham nikal paṛe"],
                    ["Don’t throw stones", "पत्थर मत फेंको", "patthar mat pheṅko"],
                    ["He kept talking", "वह बोलता रहा", "vah boltā rahā"],
                    ["Finish your food", "खाना खत्म कर लो", "khānā khatm kar lo"],
                    ["I paid in full", "मैंने पूरा भर दिया", "mainne pūrā bhar diyā"],
                ],
            ),
        ],
    )


def chapter_591() -> dict:
    return _l(
        "Passive: किया गया, देखा जाता है — agent optional with से.",
        "यह किया गया — this was done.",
        [
            _p("Spoken preference", "Active is common; passive in news and formal style."),
            _t(
                "Active / passive",
                [
                    ["The work was done", "काम किया गया", "kām kiyā gayā"],
                    ["Hindi is spoken here", "यहाँ हिन्दी बोली जाती है", "yahā̃ hindī bolī jātī hai"],
                    ["The door was opened", "दरवाज़ा खोला गया", "darvāzā kholā gayā"],
                    ["It is being built", "यह बनाया जा रहा है", "yah banāyā jā rahā hai"],
                    ["Rules are followed", "नियम माने जाते हैं", "niyam māne jāte haiṃ"],
                    ["He was called", "उसे बुलाया गया", "use bulāyā gayā"],
                    ["Money was stolen", "पैसे चुराए गए", "paise curā.e ga.e"],
                    ["The letter was sent", "पत्र भेजा गया", "patr bhejā gayā"],
                    ["Mistakes were made", "गलतियाँ हुईं", "galtiyā̃ huī̃"],
                    ["The match will be played", "मैच खेला जाएगा", "mec khelā jāegā"],
                    ["This must be signed", "इस पर हस्ताक्षर करना होगा", "is par hastākṣar karnā hogā"],
                    ["Food is cooked daily", "रोज़ खाना बनाया जाता है", "roz khānā banāyā jātā hai"],
                    ["He was punished", "उसे सज़ा दी गई", "use sazā dī gaī"],
                    ["The bill was paid", "बिल भरा गया", "bil bharā gayā"],
                    ["News was announced", "ख़बर घोषित की गई", "khabar ghoṣit kī gaī"],
                    ["Problems are solved", "समस्याएँ सुलझाई जाती हैं", "samasyāeṃ suljhāī jātī haiṃ"],
                ],
            ),
        ],
    )


def chapter_592() -> dict:
    return _l(
        "Style 2: impersonal passives, जा सकता है, हो सकता है — ‘it can be done’.",
        "यहाँ धूम्रपान नहीं किया जा सकता.",
        [
            _p("Modals + passive", "Permission and possibility in formal signs."),
            _t(
                "Passive style 2",
                [
                    ["Smoking is not allowed", "धूम्रपान वर्जित है", "dhūmrapān varjit hai"],
                    ["Entry prohibited", "प्रवेश वर्जित", "praveś varjit"],
                    ["This cannot be undone", "यह वापस नहीं किया जा सकता", "yah vāpas nahī̃ kiyā jā saktā"],
                    ["Tickets may be booked online", "टिकट ऑनलाइन बुक की जा सकती हैं", "ṭikaṭ ônlāin buk kī jā saktī haiṃ"],
                    ["Applications are invited", "आवेदन आमंत्रित हैं", "āvedan āmantrit haiṃ"],
                    ["Results will be declared", "परिणाम घोषित किए जाएँगे", "pariṇām ghoṣit kie jāeṅge"],
                    ["Fine may be imposed", "जुर्माना लगाया जा सकता है", "jurmānā lagāyā jā saktā hai"],
                    ["Meeting has been postponed", "बैठक स्थगित कर दी गई", "baiṭhak sthagit kar dī gaī"],
                    ["Your request is under review", "आपका अनुरोध विचाराधीन है", "āpkā anurodh vicārādhīn hai"],
                    ["Payment shall be made in advance", "भुगतान अग्रिम किया जाएगा", "bhugtān agrim kiyā jāegā"],
                    ["Documents must be submitted", "दस्तावेज़ जमा करने होंगे", "dastāvez jamā karne hoṅge"],
                    ["It is hoped that …", "आशा है कि …", "āśā hai ki …"],
                    ["Visitors are requested to …", "आगंतुकों से अनुरोध है …", "āgantukõ se anurodh hai …"],
                    ["Goods once sold will not be returned", "बिका हुआ माल वापस नहीं होगा", "bikā huā māl vāpas nahī̃ hogā"],
                    ["Silence must be maintained", "मौन रखा जाए", "maun rakhā jā.e"],
                    ["This area is monitored", "इस क्षेत्र की निगरानी है", "is kṣetra kī nigārānī hai"],
                ],
            ),
        ],
    )


def chapter_593() -> dict:
    return _l(
        "Feel: महसूस करना, लगना; think: सोचना, समझना, लगता है.",
        "मुझे ठंड लग रही है — I feel cold.",
        [
            _p("Opinion", "मुझे लगता है कि … — I think that …"),
            _t(
                "Feel & think",
                [
                    ["I feel tired", "मैं थका महसूस कर रहा हूँ", "main thakā mahasūs kar rahā hū̃"],
                    ["I feel happy", "मुझे खुशी हो रही है", "mujhe khushī ho rahī hai"],
                    ["I think you are right", "मुझे लगता है आप सही हैं", "mujhe lagtā hai āp sahī haiṃ"],
                    ["What do you think?", "आप क्या सोचते हैं?", "āp kyā sochte haiṃ?"],
                    ["I don’t think so", "मुझे ऐसा नहीं लगता", "mujhe aisā nahī̃ lagtā"],
                    ["She thinks too much", "वह बहुत सोचती है", "vah bahut sochtī hai"],
                    ["I feel sorry for him", "मुझे उस पर तरस आता है", "mujhe us par taras ātā hai"],
                    ["It feels like rain", "ऐसा लगता है बारिश होगी", "aisā lagtā hai bāriś hogī"],
                    ["I believe in honesty", "मैं ईमानदारी में विश्वास करता हूँ", "main īmāndārī mẽ viśvās kartā hū̃"],
                    ["He feels nervous", "उसे घबराहट हो रही है", "use ghabrāhaṭ ho rahī hai"],
                    ["I thought you knew", "मैंने सोचा आपको पता है", "mainne socā āpko patā hai"],
                    ["Do you feel better?", "क्या आप बेहतर महसूस कर रहे हैं?", "kyā āp behtar mahasūs kar rahe haiṃ?"],
                    ["I feel like crying", "मुझे रोने का मन है", "mujhe rone kā man hai"],
                    ["She thinks about the future", "वह भविष्य के बारे में सोचती है", "vah bhaviṣy ke bāre mẽ sochtī hai"],
                    ["I feel gratitude", "मैं आभारी महसूस करता हूँ", "main ābhārī mahasūs kartā hū̃"],
                    ["That sounds strange to me", "मुझे अजीब लगता है", "mujhe ajīb lagtā hai"],
                ],
            ),
        ],
    )


def chapter_594() -> dict:
    return _l(
        "Idioms: हाथ पर हाथ धरे बैठे रहना; आँख में धूल झोंकना — sit idle; deceive.",
        "Learn fixed images; meaning is not literal.",
        [
            _p("Common", "दिल से — wholeheartedly; मुँह पर हाथ रखना — be shocked."),
            _t(
                "Idioms 1",
                [
                    ["to sit idle", "हाथ पर हाथ धरे बैठे रहना", "hāth par hāth dhare baiṭhe rehnā"],
                    ["to pull someone’s leg", "टाँग खींचना", "tā̃g khīṃcnā"],
                    ["eye-opener", "आँख खोल देने वाला", "ā̃kh khol dene vālā"],
                    ["heart to heart", "दिल की बात", "dil kī bāt"],
                    ["once in a blue moon", "कभी कभार", "kabhī kabhār"],
                    ["to cost an arm and a leg", "लूट लेना", "lūṭ lenā"],
                    ["to be broke", "कंगाल होना", "kaṅgāl honā"],
                    ["to get cold feet", "घबरा जाना", "ghabarā jānā"],
                    ["to spill the beans", "राज़ खोल देना", "rāz khol denā"],
                    ["better late than never", "देर आए दुरुस्त आए", "der ā.e durust ā.e"],
                    ["the last straw", "अंतिम सीमा", "antim sīmā"],
                    ["to turn a blind eye", "आँख बंद कर लेना", "ā̃kh band kar lenā"],
                    ["to add fuel to fire", "आग में घी डालना", "āg mẽ ghī ḍālnā"],
                    ["all’s well that ends well", "अंत भला तो सब भला", "ant bhala to sab bhala"],
                    ["between you and me", "दोनों के बीच की बात", "donõ ke bīc kī bāt"],
                    ["time flies", "समय पंख लगाकर उड़ जाता है", "samay paṅkh lagākar uṛ jātā hai"],
                ],
            ),
        ],
    )


def chapter_595() -> dict:
    return _l(
        "More idioms: मुँह की खाना; पैर पीछे खींचना — eat one’s words; back out.",
        "Regional variants exist; stick to widely understood forms.",
        [
            _p("Caution", "Some idioms are informal; avoid in formal letters."),
            _t(
                "Idioms 2",
                [
                    ["to eat one’s words", "अपने शब्द वापस लेना", "apne śab vāpas lenā"],
                    ["to back out", "पैर पीछे खींचना", "pair pīche khīṃcnā"],
                    ["to be in hot water", "मुसीबत में फँसना", "musībat mẽ phãsnā"],
                    ["to kill time", "समय बिताना", "samay bitānā"],
                    ["to hit the nail on the head", "बात सही पकड़ना", "bāt sahī pakṛnā"],
                    ["to be on cloud nine", "सातवें आसमान पर होना", "sātveṃ āsmān par honā"],
                    ["to cry over spilt milk", "बीत गई बातों का रोना", "bīt gaī bātõ kā ronā"],
                    ["to face the music", "सज़ा भुगतना", "sazā bhugatnā"],
                    ["to let the cat out of the bag", "भेद खोल देना", "bhed khol denā"],
                    ["to beat around the bush", "घुमाफिराकर बात करना", "ghumāphirākar bāt karnā"],
                    ["to pay through the nose", "ज़्यादा दाम देना", "zyādā dām denā"],
                    ["to have a chip on one’s shoulder", "हमेशा नाराज़ रहना", "hameśā nārāz rahnā"],
                    ["to read between the lines", "अर्थ समझना", "arth samajhnā"],
                    ["to throw in the towel", "हार मान लेना", "hār mān lenā"],
                    ["to get the ball rolling", "शुरुआत करना", "śuruāt karnā"],
                    ["the ball is in your court", "अब आपकी बारी है", "ab āpkī bārī hai"],
                ],
            ),
        ],
    )


def chapter_596() -> dict:
    return _l(
        "Style 2 conditionals: यदि … तो अन्यथा; नहीं तो — if not … then; otherwise.",
        "Formal यदि … अथवा — if … or else.",
        [
            _p("Mixed", "अगर तुम नहीं आओगे तो हम नहीं जाएँगे — conditional threat/promise."),
            _t(
                "If–then style 2",
                [
                    ["If you hurry, you will catch", "अगर जल्दी करोगे तो पकड़ लोगे", "agar jaldī karoge to pakṛ loge"],
                    ["Otherwise we cancel", "नहीं तो हम रद्द कर देंगे", "nahī̃ to ham radd kar deṃge"],
                    ["If not today, then tomorrow", "आज नहीं तो कल", "āj nahī̃ to kal"],
                    ["Unless you try, you won’t win", "जब तक कोशिश न करोगे जीतोगे नहीं", "jab tak kośiś na karoge jītoge nahī̃"],
                    ["If I were rich …", "अगर मैं अमीर होता …", "agar main amīr hotā …"],
                    ["Had you told me …", "अगर तुमने बताया होता …", "agar tumne batāyā hotā …"],
                    ["Whether rain or shine", "चाहे बारिश हो या धूप", "cāhe bāriś ho yā dhūp"],
                    ["If so, tell me", "अगर ऐसा है तो बताओ", "agar aisā hai to batāo"],
                    ["If not, leave it", "अगर नहीं तो छोड़ दो", "agar nahī̃ to choṛ do"],
                    ["In case of fire, run", "आग लगने पर भागो", "āg lagne par bhāgo"],
                    ["If everything fails", "अगर सब फेल हो जाए", "agar sab phel ho jā.e"],
                    ["Suppose he refuses", "मान लो वह मना कर दे", "mān lo vah manā kar de"],
                    ["If you agree, sign", "अगर सहमत हैं तो हस्ताक्षर करें", "agar sahamat haiṃ to hastākṣar kareṃ"],
                    ["Without effort, no gain", "मेहनत के बिना फल नहीं", "mehnat ke binā phal nahī̃"],
                    ["If it suits you", "अगर आपको ठीक लगे", "agar āpko ṭhīk lage"],
                    ["Then only we proceed", "तभी हम आगे बढ़ेंगे", "tabhī ham āge baṛheṅge"],
                ],
            ),
        ],
    )


_PHRASES = {
    543: chapter_543,
    544: chapter_544,
    545: chapter_545,
    546: chapter_546,
    547: chapter_547,
    548: chapter_548,
    549: chapter_549,
    550: chapter_550,
    551: chapter_551,
    552: chapter_552,
    553: chapter_553,
    554: chapter_554,
    555: chapter_555,
    556: chapter_556,
    557: chapter_557,
    558: chapter_558,
    559: chapter_559,
    560: chapter_560,
    561: chapter_561,
    562: chapter_562,
    563: chapter_563,
    564: chapter_564,
    565: chapter_565,
    566: chapter_566,
    567: chapter_567,
    568: chapter_568,
    569: chapter_569,
    570: chapter_570,
    571: chapter_571,
    572: chapter_572,
    573: chapter_573,
    574: chapter_574,
    575: chapter_575,
    576: chapter_576,
    577: chapter_577,
    578: chapter_578,
    579: chapter_579,
    580: chapter_580,
    581: chapter_581,
    582: chapter_582,
    583: chapter_583,
    584: chapter_584,
    585: chapter_585,
    586: chapter_586,
    587: chapter_587,
    588: chapter_588,
    589: chapter_589,
    590: chapter_590,
    591: chapter_591,
    592: chapter_592,
    593: chapter_593,
    594: chapter_594,
    595: chapter_595,
    596: chapter_596,
}


def get_phrases_chapter(chapter_id: int) -> dict | None:
    fn = _PHRASES.get(chapter_id)
    return fn() if fn else None
