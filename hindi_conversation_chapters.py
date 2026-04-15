# -*- coding: utf-8 -*-
"""
Hindi conversation / situational lessons (620–662): fuller practice sentences.
Standard spoken Hindi; IAST-style romanization.
"""

from __future__ import annotations

from hindi_grammar_chapters import _p, _t


def _l(content: str, intro: str, blocks: list[dict]) -> dict:
    return {"content": content, "intro": intro, "blocks": blocks}


def chapter_620() -> dict:
    return _l(
        "Diwali: lights, sweets, family visits, and safe celebrations in natural Hindi.",
        "Read aloud; imagine greeting neighbours and shopping for diyas before the festival.",
        [
            _p("Setting", "दीवाली पर घर रोशन होता है और लोग एक दूसरे को मिठाई देते हैं।"),
            _t(
                "Diwali festival",
                [
                    ["Diwali is the festival of lights, and every lane looks bright with lamps and rangoli.", "दीवाली रोशनी का त्योहार है, और हर गली दीयों और रंगोली से जगमगा उठती है।", "dīvālī rośanī kā tyohār hai, aur har galī diyõ aur raṅgolī se jagmagā uṭhtī hai."],
                    ["We clean the whole house and decorate the entrance with marigold garlands before Lakshmi puja.", "हम पूरा घर साफ़ करते हैं और लक्ष्मी पूजा से पहले द्वार पर गेंदे की माला लगाते हैं।", "ham pūrā ghar sāf karte haiṃ aur lakṣmī pūjā se pahle dvār par geṃde kī mālā lagāte haiṃ."],
                    ["Could you bring two kilos of pure ghee and a packet of dry fruits for the sweets we will cook?", "क्या आप दो किलो शुद्ध घी और एक पैकेट मेवे ला सकते हैं, जिससे हम मिठाई बनाएँगे?", "kyā āp do kilo śuddh ghī aur ek pekeṭ meve lā sakte haiṃ, jisse ham miṭhāī banāeṅge?"],
                    ["Children burst crackers only under adult supervision, because safety matters more than noise.", "बच्चे पटाखे केवल बड़ों की देखरेख में फोड़ते हैं, क्योंकि शोर से ज़्यादा सुरक्षा ज़रूरी है।", "bacce paṭākhe keval baṛõ kī dekherekh mẽ phoṛte haiṃ, kyõki śor se zyādā surakṣā zarūrī hai."],
                    ["On Diwali evening we wear new clothes, exchange gifts, and wish everyone prosperity and peace.", "दीवाली की शाम हम नए कपड़े पहनकर उपहार बाँटते हैं और सबको समृद्धि व शांति की शुभकामनाएँ देते हैं।", "dīvālī kī śām ham nae kapṛe pahan kar upahār bā̃ṭte haiṃ aur sabko samṛddhi va śānti kī śubhkāmnāeṃ dete haiṃ."],
                    ["If guests arrive unexpectedly, we still welcome them warmly and offer tea with homemade snacks.", "अगर मेहमान अचानक आ जाएँ तो भी हम उनका गर्मजोशी से स्वागत करते हैं और चाय व घर की चटपटी चीज़ें परोसते हैं।", "agar mehmān acānak ā jāeṃ to bhī ham unkā garmajośī se svāgat karte haiṃ aur cāy va ghar kī caṭpaṭī cīzeṃ paroste haiṃ."],
                    ["The market is crowded, yet shopkeepers patiently explain prices and even pack gifts neatly.", "बाज़ार भीड़ से भरा होता है, फिर भी दुकानदार धैर्य से दाम समझाते हैं और उपहार भी सलीके से पैक कर देते हैं।", "bāzār bhīṛ se bharā hotā hai, phir bhī dukāndār dhairya se dām samjhāte haiṃ aur upahār bhī salīke se pāk kar dete haiṃ."],
                    ["After dinner we sit on the terrace, count stars, and remember how Diwali felt in childhood.", "रात के खाने के बाद हम छत पर बैठकर तारे गिनते हैं और याद करते हैं कि बचपन में दीवाली कैसी लगती थी।", "rāt ke khāne ke bād ham chat par baiṭh kar tāre ginte haiṃ aur yād karte haiṃ ki bacpan mẽ dīvālī kaisī lagtī thī."],
                    ["My grandmother says that kindness during festivals matters more than how expensive your clothes are.", "मेरी दादी कहती हैं कि त्योहारों पर दयालुता कपड़ों की कीमत से ज़्यादा मायने रखती है।", "merī dādī kahtī haiṃ ki tyohārõ par dayālutā kapṛõ kī kīmat se zyādā māyne rakhtī hai."],
                    ["We donate old blankets and food packets to the shelter nearby so that joy is shared beyond our family.", "हम पुराने कंबल और खाने के पैकेट पास के आश्रय में दान करते हैं ताकि खुशी हमारे परिवार से आगे बाँटी जाए।", "ham purāne kambal aur khāne ke pekeṭ pās ke āśray mẽ dān karte haiṃ tāki khushī hamāre parivār se āge bā̃ṭī jā.e."],
                    ["When the electricity flickers during the evening, we laugh and light extra diyas without complaining.", "शाम को बिजली कभी कभी काँप उठती है, तब हम बिना शिकायत के हँसकर और दीये जला देते हैं।", "śām ko bijlī kabhī kabhī kā̃p uṭhtī hai, tab ham binā śikāyat ke hãs kar aur dīye jalā dete haiṃ."],
                    ["Before sleeping, I message cousins who live abroad and send them photos of our decorated courtyard.", "सोने से पहले मैं विदेश में रहने वाले कज़िन्स को संदेश भेजकर आँगन की सजी फोटो भेजता हूँ।", "sone se pahle main videś mẽ rahne vāle kazins ko sandeś bhej kar ā̃gan kī sajī phoṭo bhejtā hū̃."],
                ],
            ),
        ],
    )


def chapter_621() -> dict:
    return _l(
        "Introductions and polite salutations for strangers, colleagues, and elders.",
        "Use आप with people you do not know well; तुम only with close peers if appropriate.",
        [
            _p("Register", "नमस्ते works any time; सुप्रभात is morning-only."),
            _t(
                "Introduction / salutation",
                [
                    ["Good morning, I am pleased to meet you; my name is Rohan and I recently moved to this neighbourhood.", "सुप्रभात, आपसे मिलकर खुशी हुई; मेरा नाम रोहन है और मैं हाल ही में इस मोहल्ले में आया हूँ।", "suprabhāt, āpse milkar khushī huī; merā nām rohan hai aur main hāl hī mẽ is mohalle mẽ āyā hū̃."],
                    ["Namaste, I work as a teacher, and I would love to know what you do for a living.", "नमस्ते, मैं शिक्षक के रूप में काम करता हूँ, और जानना चाहूँगा कि आप किस क्षेत्र में कार्य करते हैं।", "namaste, main śikṣak ke rūp mẽ kām kartā hū̃, aur jānnā cāhū̃gā ki āp kis kṣetra mẽ kāry karte haiṃ."],
                    ["Please sit down; would you like chilled water or masala tea before we begin the conversation?", "कृपया बैठिए; क्या आप बात शुरू करने से पहले ठंडा पानी या मसाला चाय लेंगे?", "kripayā baithie; kyā āp bāt śurū karne se pahle thaṃḍā pānī yā masālā cāy leṅge?"],
                    ["I apologize for arriving ten minutes late because the metro was unusually crowded today.", "मैं दस मिनट देर से आने के लिए क्षमा चाहता हूँ क्योंकि आज मेट्रो असामान्य रूप से भीड़ थी।", "main das minaṭ der se āne ke lie kṣamā cāhtā hū̃ kyõki āj meṭro asāmānya rūp se bhīṛ thī."],
                    ["It is an honour to meet your parents; they have always supported young artists in our city.", "आपके माता-पिता से मिलना सम्मान की बात है; उन्होंने हमारे शहर में हमेशा नए कलाकारों का साथ दिया है।", "āp ke mātā-pitā se milnā sammān kī bāt hai; unhoṃne hamāre śahar mẽ hameśā nae kalākārõ kā sāth diyā hai."],
                    ["Let me introduce my colleague who handles community projects and speaks fluent Hindi and Tamil.", "मैं अपने सहकर्मी से मिलवाता हूँ जो सामुदायिक परियोजनाएँ संभालते हैं और हिन्दी-तमिल धाराप्रवाह बोलते हैं।", "main apne sahakarmī se milvātā hū̃ jo sāmudāyik pariyojnāeṃ saṃbhālte haiṃ aur hindī-tamil dhārāpravāh bolte haiṃ."],
                    ["When elders enter the room, we stand up briefly to show respect even if the meeting is informal.", "जब बुज़ुर्ग कमरे में आते हैं तो हम थोड़ी देर के लिए खड़े हो जाते हैं, भले ही मीटिंग अनौपचारिक हो।", "jab buzurg kamre mẽ āte haiṃ to ham thoṛī der ke lie khaṛe ho jāte haiṃ, bhale hī mīṭiṅ anopacārik ho."],
                    ["If you ever need help with paperwork, call me directly instead of hesitating on the street.", "अगर कागज़ी कार्रवाई में कभी मदद चाहिए तो सड़क पर झिझकने के बजाय सीधे मुझे फोन कर लीजिए।", "agar kāgazī kārravāī mẽ kabhī madad cāhie to saṛak par jhijhakne ke bajāy sīdhe mujhe phon kar lijie."],
                    ["Before leaving, I thanked the host family and promised to bring homemade pickles next Sunday.", "जाते समय मैंने मेज़बान परिवार को धन्यवाद दिया और अगले रविवार घर की अचार की बोतल लाने का वादा किया।", "jāte samay mainne mezbān parivār ko dhanyavād diyā aur agale ravivār ghar kī acār kī botal lāne kā vādā kiyā."],
                    ["She smiled and said that warm greetings make even a new city feel a little like home.", "वह मुस्कुराई और बोली कि गर्मजोशी भरे अभिवादन से नया शहर भी थोड़ा घर जैसा लगने लगता है।", "vah muskurāī aur bolī ki garmajośī bhare abhivādan se nayā śahar bhī thoṛā ghar jaise lagne lagtā hai."],
                    ["We exchanged business cards and agreed to continue the discussion over lunch later this week.", "हमने विज़िटिंग कार्ड साझा किए और इस हफ़्ते बाद दोपहर के खाने पर चर्चा जारी रखने पर सहमति जताई।", "hamne viziṭiṅg kārd sājhā kie aur is hafte bād dopahar ke khāne par carcā jārī rakhne par sahamti jatāī."],
                    ["Remember to bow slightly when you greet the priest at the temple; it signals humility and respect.", "मंदिर में पुजारी जी को नमस्ते करते समय हल्का झुकना याद रखिए; यह विनम्रता और सम्मान दिखाता है।", "mandir mẽ pujārī jī ko namaste karte samay halkā jhuknā yād rakhie; yah vinamratā aur sammān dikhātā hai."],
                ],
            ),
        ],
    )


def chapter_622() -> dict:
    return _l(
        "Time expressions: clock time, routines, deadlines, and polite scheduling.",
        "Pair बजे with numbers; use कल carefully for yesterday vs tomorrow by context.",
        [
            _p("Clock", "सात बज रहे हैं means “it is seven” in progress; सात बजे is “at seven”."),
            _t(
                "Time-related sentences",
                [
                    ["The workshop begins sharply at nine thirty, so please reach the gate ten minutes early.", "कार्यशाला साढ़े नौ बजे ठीक शुरू होती है, इसलिए कृपया दस मिनट पहले गेट पर पहुँच जाइए।", "kāryaśālā sāṛhe nau baje ṭhīk śurū hotī hai, islie kripayā das minaṭ pahle geṭ par pahuṃc jāie."],
                    ["Yesterday I missed the train because I misunderstood whether seven meant morning or evening.", "कल मेरी ट्रेन छूट गई क्योंकि मैंने समझा ही नहीं कि सात का मतलब सुबह है या शाम।", "kal merī ṭren chūṭ gaī kyõki mainne samjhā hī nahī̃ ki sāt kā matlab subah hai yā śām."],
                    ["Could we postpone the call to tomorrow afternoon when my internet connection is usually stable?", "क्या हम कॉल कल दोपहर के लिए टाल सकते हैं जब मेरा इंटरनेट आमतौर पर स्थिर रहता है?", "kyā ham kŏl kal dopahar ke lie ṭāl sakte haiṃ jab merā intarnet āmtaur par sthir rehtā hai?"],
                    ["Right now I am stuck in traffic, but I promise I will reach before the bank closes at four.", "अभी मैं ट्रैफ़िक में फँसा हूँ, पर वादा करता हूँ कि बैंक चार बजे बंद होने से पहले पहुँच जाऊँगा।", "abhī main ṭraifik mẽ phãsā hū̃, par vādā kartā hū̃ ki baiṅk cār baje band hone se pahle pahuṃc jāū̃gā."],
                    ["She wakes up before sunrise so that she can finish yoga and still cook breakfast for the children.", "वह सूरज निकलने से पहले उठ जाती है ताकि योग कर सके और फिर भी बच्चों के लिए नाश्ता बना सके।", "vah sūraj nikalne se pahle uṭh jātī hai tāki yog kar sake aur phir bhī baccõ ke lie nāśtā banā sake."],
                    ["We have been waiting since three o’clock, yet the technician keeps saying he will arrive in five minutes.", "हम तीन बजे से इंतज़ार कर रहे हैं, फिर भी टेक्नीशियन बार-बार कहता है कि वह पाँच मिनट में आएगा।", "ham tīn baje se intazār kar rahe haiṃ, phir bhī ṭeknīśiyan bār-bār kahtā hai ki vah pā̃c minaṭ mẽ āegā."],
                    ["During winter the sun sets early, so we schedule outdoor games only until five in the evening.", "सर्दियों में सूरज जल्दी डूब जाता है, इसलिए हम बाहर के खेल केवल शाम पाँच बजे तक रखते हैं।", "sardiyõ mẽ sūraj jaldī ḍūb jātā hai, islie ham bāhar ke khel keval śām pā̃c baje tak rakhte haiṃ."],
                    ["By the time I finish this report, midnight will have passed and the streets will be completely quiet.", "जब तक मैं यह रिपोर्ट खत्म करूँ, आधी रात गुज़र चुकी होगी और गलियाँ पूरी तरह शांत होंगी।", "jab tak main yah ripoṭ khatm karū̃, ādhī rāt guzar cukī hogī aur galiyā̃ pūrī tarah śānt hoṅgī."],
                    ["Please remind me two hours before the flight because I easily lose track of time while reading.", "कृपया उड़ान से दो घंटे पहले याद दिलाइएगा क्योंकि पढ़ते समय मुझे समय का पता ही नहीं चलता।", "kripayā uṛān se do ghaṃṭe pahle yād dilāiega kyõki paṛhte samay mujhe samay kā patā hī nahī̃ caltā."],
                    ["Every Friday evening our book club meets for three hours and discusses one novel in depth.", "हर शुक्रवार शाम हमारा बुक क्लब तीन घंटे मिलता है और एक उपन्यास पर गहराई से चर्चा करता है।", "har śukravār śām hamārā buk klub tīn ghaṃṭe miltā hai aur ek upanyās par gahrāī se carcā kartā hai."],
                    ["The museum opens at ten, closes at six, and stays shut on Mondays for maintenance work.", "संग्रहालय दस बजे खुलता है, छह बजे बंद होता है, और रखरखाव के लिए सोमवार को बंद रहता है।", "saṅgrahālay das baje khultā hai, chah baje band hotā hai, aur rakh-rakhāv ke lie somvār ko band rehtā hai."],
                    ["He promised to text me the moment the parcel leaves the warehouse so that I can stay informed.", "उसने वादा किया कि जैसे ही पार्सल गोदाम से निकलेगा वह मुझे संदेश भेज देगा ताकि मुझे पता रहे।", "usne vādā kiyā ki jaise hī pārsal godām se niklegā vah mujhe sandeś bhej degā tāki mujhe patā rahe."],
                ],
            ),
        ],
    )


def chapter_623() -> dict:
    return _l(
        "Places and directions: landmarks, public transport, and clarifying “which side”.",
        "Use इधर/उधर and सामने for quick pointing; repeat the landmark if the listener looks confused.",
        [
            _p("Directions", "पहले सीधे जाइए, फिर बाएँ मुड़िए — first go straight, then turn left."),
            _t(
                "Where / place",
                [
                    ["Excuse me, could you tell me whether the new library is behind the old post office or beside it?", "माफ़ कीजिए, क्या आप बता सकते हैं कि नई लाइब्रेरी पुराने डाकखाने के पीछे है या उसके बगल में?", "māf kījie, kyā āp batā sakte haiṃ ki naī lāibrerī purāne ḍākkhāne ke pīche hai yā us ke bagal mẽ?"],
                    ["I am looking for a quiet café where I can sit for two hours and finish this translation.", "मैं ऐसा शांत कैफ़े ढूँढ रहा हूँ जहाँ दो घंटे बैठकर यह अनुवाद खत्म कर सकूँ।", "main aisā śānt kaife ḍhū̃ṛ rahā hū̃ jahā̃ do ghaṃṭe baiṭh kar yah anuvād khatm kar sakū̃."],
                    ["The pharmacy on the corner stays open until midnight, which is helpful when children fall ill suddenly.", "कोने वाली दवा की दुकान आधी रात तक खुली रहती है, जो जब बच्चे अचानक बीमार पड़ें तो बहुत काम आती है।", "kone vālī davā kī dukān ādhī rāt tak khulī rehtī hai, jo jab bacce acānak bīmār paṛeṃ to bahut kām ātī hai."],
                    ["We parked near the river because the underground lot was full of wedding guests’ cars.", "हमने नदी के पास गाड़ी खड़ी की क्योंकि अंडरग्राउंड पार्किंग शादी के मेहमानों की कारों से भरी थी।", "hamne nadī ke pās gāṛī khaṛī kī kyõki aṇḍargrauṇḍ pārkiṅg śādī ke mehmānõ kī kārõ se bharī thī."],
                    ["If you cross the footbridge, you will reach the platform without dragging luggage through mud.", "अगर आप फुटओवर पार कर लें तो कीचड़ में सामान घसीटे बिना ही प्लेटफ़ॉर्म तक पहुँच जाएँगे।", "agar āp phuṭovar pār kar leṃ to kīcaṛ mẽ sāmān ghasīṭe binā hī pleṭphŏrm tak pahuṃc jāeṃge."],
                    ["There is a small park where senior citizens walk every morning and share news from newspapers.", "एक छोटा पार्क है जहाँ बुज़ुर्ग हर सुबह टहलते हैं और अख़बारों की ख़बरें साझा करते हैं।", "ek choṭā pārk hai jahā̃ buzurg har subah ṭahalte haiṃ aur akhbārõ kī khabreṃ sājhā karte haiṃ."],
                    ["My cousin’s new apartment faces the hills, so the balcony stays cool even in May.", "मेरे कज़िन का नया फ़्लैट पहाड़ों की ओर है, इसलिए मई में भी बालकनी ठंडी रहती है।", "mere kazin kā nayā flaiṭ pahāḍõ kī or hai, islie maī mẽ bhī bālkonī thaṃḍī rehtī hai."],
                    ["The lane is narrow, yet delivery vans squeeze through because residents need groceries daily.", "गली तंग है, फिर भी डिलीवरी वैन निकल जाती हैं क्योंकि रहवासियों को रोज़ाना किराना चाहिए।", "galī taṅg hai, phir bhī ḍilīvarī vain nikal jātī haiṃ kyõki rahvāsiyõ ko rozānā kirānā cāhie."],
                    ["During festivals the main square becomes so crowded that police guide people in single lines.", "त्योहारों के दौरान मुख्य चौक इतना भीड़ भर जाता है कि पुलिस लोगों को एक कतार में चलाती है।", "tyohārõ ke daurān mukhya cauk itnā bhīṛ bhar jātā hai ki pulīs logõ ko ek katār mẽ calātī hai."],
                    ["She asked whether the hostel was walking distance from the university or whether she should take an auto.", "उसने पूछा कि हॉस्टल विश्वविद्यालय से पैदल की दूरी पर है या ऑटो लेनी चाहिए।", "usne pūchā ki hŏsṭal viśvavidyālay se paidal kī dūrī par hai yā ôṭo lenī cāhie."],
                    ["We finally found the community hall after circling the temple three times and asking a tea seller.", "हमें समुदायिक हॉल तब मिला जब हम तीन बार मंदिर का चक्कर लगा चुके थे और एक चायवाले से पूछ लिया।", "hameṃ samudāyik hŏl tab milā jab ham tīn bār mandir kā cakkar lagā cuke the aur ek cāyvāle se pūch liyā."],
                    ["The signboard is faded, but if you look carefully you will still read “City Hospital, Emergency Gate”.", "साइनबोर्ड फीका पड़ गया है, पर ध्यान से देखेंगे तो अभी भी “सिटी हॉस्पिटल, इमरजेंसी गेट” पढ़ सकते हैं।", "sāinbŏrḍ phīkā paṛ gayā hai, par dhyān se dekheṅge to abhī bhī “siṭī hŏspiṭal, imarjeṃsī geṭ” paṛh sakte haiṃ."],
                ],
            ),
        ],
    )


def chapter_624() -> dict:
    return _l(
        "Hotel stay: check-in, room preferences, housekeeping, and checkout politely.",
        "Ask for a printed bill; confirm whether breakfast is included in the tariff.",
        [
            _p("Front desk", "क्या मेरा कमरा अब तैयार है? — Is my room ready yet?"),
            _t(
                "In a hotel",
                [
                    ["Good evening, I have a reservation under the name Meera Sharma for two nights starting today.", "शुभ संध्या, मेरा आज से दो रातों का आरक्षण मीरा शर्मा के नाम पर है।", "śubh sandhyā, merā āj se do rātõ kā ārakṣaṇ mīrā śarmā ke nām par hai."],
                    ["Could we have two key cards, please, because my colleague and I will return at different times?", "क्या हमें दो की-कार्ड मिल सकते हैं क्योंकि मैं और मेरा सहकर्मी अलग-अलग समय लौटेंगे?", "kyā hameṃ do kī-kārḍ mil sakte haiṃ kyõki main aur merā sahakarmī alag-alag samay lauṭeṅge?"],
                    ["The room on the higher floor is fine, but please make sure the window closes tightly against traffic noise.", "ऊँची मंज़िल का कमरा ठीक है, पर कृपया यह सुनिश्चित करें कि खिड़की शोर के लिए कसकर बंद हो।", "ū̃cī manzil kā kamrā ṭhīk hai, par kripayā yah suniścit kareṃ ki khiṛkī śor ke lie kas kar band ho."],
                    ["Housekeeping can come after eleven; we will hang the “Do not disturb” sign until we finish our call.", "हाउसकीपिंग ग्यारह बजे के बाद आ सकती है; हम कॉल खत्म करने तक “डू नॉट डिस्टर्ब” का साइन लटका देंगे।", "hāuskīpiṅ gyārah baje ke bād ā saktī hai; ham kŏl khatm karne tak “ḍū nŏṭ ḍisṭarb” kā sāin laṭkā deṅge."],
                    ["The air conditioner drips water near the bed, so could you send someone to fix it before tonight?", "एयर कंडीशनर बिस्तर के पास पानी टपकाता है, क्या आप आज रात से पहले ठीक करवा सकते हैं?", "eyar kaṇḍīśanar bistar ke pās pānī ṭapkātā hai, kyā āp āj rāt se pahle ṭhīk karvā sakte haiṃ?"],
                    ["Is breakfast complimentary, and if not, could you add it to the bill so we can pay at checkout?", "क्या नाशता शुल्क में शामिल है, और यदि नहीं तो क्या आप इसे बिल में जोड़ देंगे ताकि चेकआउट पर भर सकें?", "kyā nāśta śulk mẽ śāmil hai, aur yadi nahī̃ to kyā āp ise bil mẽ joṛ deṃge tāki cekā'uṭ par bhar sakeṃ?"],
                    ["Please arrange a taxi to the airport at four fifteen tomorrow morning with a reliable driver.", "कृपया कल सुबह चार पंद्रह पर हवाई अड्डे के लिए भरोसेमंद ड्राइवर के साथ टैक्सी लगवा दीजिए।", "kripayā kal subah cār pandrah par havāī aḍḍe ke lie bharosemand ḍrāivar ke sāth ṭaiksī lagvā dījie."],
                    ["We would appreciate extra towels and bottled water because the weather is hotter than we expected.", "हम अतिरिक्त तौलिए और बोतलबंद पानी की सराहना करेंगे क्योंकि मौसम उम्मीद से ज़्यादा गर्म है।", "ham atirikt taulie aur botalband pānī kī sarāhnā kareṅge kyõki mausam ummīd se zyādā garm hai."],
                    ["At checkout the receptionist printed a detailed bill and asked whether we enjoyed the stay.", "चेकआउट पर रिसेप्शनिस्ट ने विस्तृत बिल प्रिंट किया और पूछा कि क्या हमें ठहरना अच्छा लगा।", "cekā'uṭ par risepśnisṭ ne vistṛit bil priṇṭ kiyā aur pūchā ki kyā hameṃ ṭaharnā acchā lagā."],
                    ["If you leave anything in the safe, remember to empty it; the hotel is not liable after you sign out.", "अगर आपने तिजोरी में कुछ छोड़ा है तो खाली करना याद रखिए; साइन आउट के बाद होटल ज़िम्मेदार नहीं।", "agar āpne tijorī mẽ kuch choṛā hai to khālī karnā yād rakhie; sāin ā'uṭ ke bād hoṭel zimmedār nahī̃."],
                    ["The Wi-Fi password is written on the desk card, yet the connection drops whenever it rains heavily.", "वाई-फ़ाई का पासवर्ड डेस्क कार्ड पर लिखा है, फिर भी जब ज़ोर की बारिश होती है कनेक्शन गिर जाता है।", "vāī-fāī kā pāsavarḍ desk kārd par likhā hai, phir bhī jab zor kī bāriś hotī hai kanekśan gir jātā hai."],
                    ["Thank you for upgrading us quietly when you saw that my mother walks with a stick.", "धन्यवाद कि आपने देखा कि मेरी माँ लाठी से चलती हैं तो बिना शोर के हमारा कमरा बढ़ा दिया।", "dhanyavād ki āpne dekhā ki merī mā̃ lāṭhī se caltī haiṃ to binā śor ke hamārā kamrā baṛhā diyā."],
                ],
            ),
        ],
    )


def chapter_625() -> dict:
    return _l(
        "Weather talk: seasons, forecasts, clothing advice, and small talk with neighbours.",
        "Use हो रही है for ongoing rain; ठंड लग रही है when you feel cold.",
        [
            _p("Small talk", "आज मौसम साफ़ है — today the weather is clear."),
            _t(
                "Weather",
                [
                    ["This morning the sky was overcast, so I carried an umbrella even though the forecast looked uncertain.", "आज सुबह आसमान पर बादल छाए थे, इसलिए मैं छाता ले गया भले ही पूर्वानुमान अस्पष्ट लग रहा था।", "āj subah āsmān par bādal chā.e the, islie main chātā le gayā bhale hī pūrvānumān aspaṣṭ lag rahā thā."],
                    ["The weather bureau says a cyclone may approach the coast, so fishermen have postponed going deep sea.", "मौसम विभाग कहता है कि चक्रवात तट की ओर आ सकता है, इसलिए मछुआरे गहरे समुद्र जाने को टाल रहे हैं।", "mausam vibhāg kahtā hai ki cakravāt taṭ kī or ā saktā hai, islie macchuāre gahre samudr jāne ko ṭāl rahe haiṃ."],
                    ["Delhi winters are dry and foggy, so flights often get delayed even when there is no heavy rain.", "दिल्ली की सर्दी सूखी और कोहरे वाली होती है, इसलिए भारी बारिश के बिना भी उड़ानें देर से चलती हैं।", "dillī kī sardī sūkhī aur kohre vālī hotī hai, islie bhārī bāriś ke binā bhī uṛāneṃ der se caltī haiṃ."],
                    ["After the first monsoon shower the streets smell of wet earth and children splash in puddles happily.", "पहली मानसून की बौछार के बाद गलियों में गीली मिट्टी की महक आती है और बच्चे खुशी से पोखरों में छपाके मारते हैं।", "pahlī mānasūn kī bauchhār ke bād galiyõ mẽ gīlī miṭṭī kī mahak ātī hai aur bacce khushī se pokharõ mẽ chapāke mārte haiṃ."],
                    ["The hill station was so cold that we layered sweaters and still shivered while sipping hot soup.", "हिल स्टेशन इतना ठंडा था कि हमने स्वेटर लेयर कर लिए फिर भी गर्म सूप पीते हुए काँप रहे थे।", "hil sṭeśan itnā thaṃḍā thā ki hamne sveṭar leyar kar lie phir bhī garm sūp pīte hue kā̃p rahe the."],
                    ["Strong winds blew yesterday and knocked down several trees, so the municipality cleared the roads overnight.", "कल तेज़ हवाओं ने कई पेड़ गिरा दिए, इसलिए नगर निगम ने रात भर सड़कें साफ़ कीं।", "kal tez havāõ ne kaī peṛ girā die, islie nagar nigam ne rāt bhar saṛkeṃ sāf kī̃."],
                    ["Humidity near the sea makes clothes stick to the skin, yet locals say you get used to it within weeks.", "समुद्र के पास नमी कपड़ों को चिपका देती है, फिर भी स्थानीय लोग कहते हैं कि कुछ हफ़्तों में आदत पड़ जाती है।", "samudr ke pās namī kapṛõ ko cipkā detī hai, phir bhī sthānīy log kahte haiṃ ki kuch haftõ mẽ ādat paṛ jātī hai."],
                    ["Farmers watch the sky anxiously because untimely hail can destroy the standing wheat crop in hours.", "किसान चिंतित होकर आसमान देखते हैं क्योंकि बेमौसम ओलावृष्टि खड़ी गेहूँ की फसल कुछ घंटों में बर्बाद कर सकती है।", "kisān cintit hokar āsmān dekhte haiṃ kyõki bemausam olāvṛṣṭi khaṛī gehū̃ kī phasal kuch ghaṃṭõ mẽ barbād kar saktī hai."],
                    ["The picnic was almost cancelled due to heat, but we shifted it to sunset when a cool breeze began.", "गर्मी के कारण पिकनिक लगभग रद्द हो जाती, पर हमने उसे सूर्यास्त पर टाल दिया जब ठंडी हवा चलने लगी।", "garmī ke kāraṇ pikin lagabhag radd ho jātī, par hamne use sūryāst par ṭāl diyā jab thaṃḍī havā calne lagī."],
                    ["I love the smell before rain, when dust settles and petrichor rises from the warm pavement.", "मुझे बारिश से पहले की महक पसंद है जब धूल बैठ जाती है और गर्म फुटपाथ से पेट्रिकोर उठता है।", "mujhe bāriś se pahle kī mahak pasand hai jab dhūl baiṭh jātī hai aur garm phuṭpāth se peṭrikor uṭhtā hai."],
                    ["Climate change is no longer abstract; our grandparents say summers were milder thirty years ago.", "जलवायु परिवर्तन अब काल्पनिक नहीं रहा; हमारे दादा-दादी कहते हैं कि तीस साल पहले गर्मियाँ नरम थीं।", "jalvāyu parivartan ab kālpanik nahī̃ rahā; hamāre dādā-dādī kahte haiṃ kī tīs sāl pahle garmiyā̃ naram thī̃."],
                    ["She tied her hair back because the humid wind kept sticking strands to her face while we walked.", "उसने बाल पीछे बाँध लिए क्योंकि नम हवा चलते समय बाल चेहरे से चिपकते रहते थे।", "usne bāl pīche bā̃dh lie kyõki nama havā calte samay bāl chehre se cipakte rahte the."],
                ],
            ),
        ],
    )


def chapter_626() -> dict:
    return _l(
        "Traffic police: documents, fines, helmets, and staying calm while explaining.",
        "Keep your license and pollution certificate accessible; speak clearly and avoid arguing on the road.",
        [
            _p("Safety", "मैं हेलमेट पहनता हूँ — I wear a helmet."),
            _t(
                "Traffic police",
                [
                    ["Good evening, officer; I know I should not have crossed the stop line when the signal was red.", "शुभ संध्या, साहब; मैं जानता हूँ कि जब सिग्नल लाल था तो मुझे स्टॉप लाइन पार नहीं करनी चाहिए थी।", "śubh sandhyā, sāhab; main jāntā hū̃ ki jab signāl lāl thā to mujhe sṭŏp lāin pār nahī̃ karnī cāhie thī."],
                    ["Here are my driving license, registration papers, and insurance; all of them are valid until next March.", "यह रहा मेरा ड्राइविंग लाइसेंस, पंजीकरण कागज़ और बीमा; सब अगले मार्च तक वैध हैं।", "yah rahā merā ḍrāiviṅg lāisens, pañjīkaraṇ kāgaz aur bīmā; sab agale mārc tak vaidh haiṃ."],
                    ["I genuinely forgot my helmet at home today; may I pay the fine online and show you the receipt tomorrow?", "मैंने आज सचमुच हेलमेट घर भूल गया; क्या मैं ऑनलाइन जुर्माना भरकर कल रसीद दिखा सकता हूँ?", "mainne āj sacamuc helmeṭ ghar bhūl gayā; kyā main ônlāin jurmānā bhar kar kal rasīd dikhā saktā hū̃?"],
                    ["The child was unwell, so I took a U-turn where prohibited; I accept responsibility and will not repeat it.", "बच्चा बीमार था, इसलिए मैंने मना जगह यू-टर्न लिया; मैं ज़िम्मेदारी स्वीकार करता हूँ और दोहराऊँगा नहीं।", "baccā bīmār thā, islie mainne manā jagah yū-ṭarn liyā; main zimmedārī svīkār kartā hū̃ aur dohrāū̃gā nahī̃."],
                    ["Your breathalyser reading is confusing; I have not drunk alcohol, only cough syrup prescribed by my doctor.", "आपका ब्रेथलाइज़र रीडिंग भ्रमित कर रही है; मैंने शराब नहीं पी, केवल डॉक्टर की सिफ़ारिश पर खाँसी की दवा ली है।", "āpkā brethlāizar rīḍiṅ bhramit kar rahī hai; mainne śarāb nahī̃ pī, keval ḍokṭar kī sifāriś par khā̃sī kī davā lī hai."],
                    ["There was an ambulance behind me, so I moved aside quickly; perhaps the camera caught it out of context.", "पीछे एम्बुलेंस थी इसलिए मैंने तुरंत साइड दी; शायद कैमरा इसे संदर्भ से बाहर पकड़ गया।", "pīche embuleṃs thī islie mainne turant sāid dī; śāyad kaimrā ise sandarbh se bāhar pakṛ gayā."],
                    ["I understand the rule about tinted glasses; I will remove the film this weekend and show the vehicle again.", "मैं टिंटेड शीशे के नियम को समझता हूँ; इस हफ़्ते अंत में फ़िल्म हटवाकर फिर गाड़ी दिखाऊँगा।", "main ṭiṇṭeḍ śīśe ke niyam ko samajhtā hū̃; is hafte ant mẽ film haṭhvākar phir gāṛī dikhāū̃gā."],
                    ["Could you explain exactly which section of the law I violated so that I can learn and avoid future mistakes?", "क्या आप स्पष्ट बता सकते हैं कि कानून की किस धारा का उल्लंघन हुआ ताकि मैं सीखूँ और भविष्य में गलती न करूँ?", "kyā āp spaṣṭ batā sakte haiṃ ki kānūn kī kis dhārā kā ullaṅghan huā tāki main sīkhū̃ aur bhaviṣya mẽ galtī na karū̃?"],
                    ["Thank you for guiding the schoolchildren safely across; we need more officers like you during rush hour.", "स्कूल के बच्चों को सुरक्षित पार कराने के लिए धन्यवाद; भीड़ के समय ऐसे अधिकारियों की ज़रूरत है।", "skūl ke baccõ ko surakṣit pār karāne ke lie dhanyavād; bhīṛ ke samay aise adhikāriyõ kī zarūrat hai."],
                    ["I will pay the challan digitally right now if you confirm the amount and send the link by SMS.", "अगर आप राशि पुष्टि करके एसएमएस से लिंक भेज दें तो मैं अभी डिजिटल चालान भर देता हूँ।", "agar āp rāśi puṣṭi kar ke esemes se liṅk bhej deṃ to main abhī ḍijiṭal cālān bhar detā hū̃."],
                    ["Please be careful near the construction zone; loose gravel hurt a cyclist yesterday evening.", "कृपया निर्माण क्षेत्र के पास सावधान रहिए; कल शाम ढीले पत्थरों से एक साइकिल सवार घायल हो गया।", "kripayā nirmāṇ kṣetra ke pās sāvdhān rahie; kal śām ḍhīle pattharõ se ek sāikil savār ghāyal ho gayā."],
                    ["I appreciate that you remained polite even when other drivers were honking impatiently behind us.", "मैं सराहना करता हूँ कि आप विनम्र रहे जबकि पीछे के ड्राइवर बेसब्री से हॉर्न बजा रहे थे।", "main sarāhnā kartā hū̃ ki āp vinamra rahe jabaki pīche ke ḍrāivar besabrī se hŏrn bajā rahe the."],
                ],
            ),
        ],
    )


def chapter_627() -> dict:
    return _l(
        "Rickshaw and taxi: fare, route, meter, luggage, and polite drop-off instructions.",
        "Confirm पैसे before starting; say यहीं उतार दीजिए when you reach the exact spot.",
        [
            _p("Fare", "मीटर से चलेंगे या फिक्स रेट? — Will you go by meter or fixed rate?"),
            _t(
                "Rickshaw / taxi",
                [
                    ["Bhaiya, please take me to the railway station side entrance where the prepaid booth is located.", "भैया, कृपया मुझे रेलवे स्टेशन के उस प्रवेश द्वार पर ले चलिए जहाँ प्रीपेड बूथ है।", "bhaiyā, kripayā mujhe relve sṭeśan ke us praveś dvār par le calie jahā̃ prīpeḍ būth hai."],
                    ["How much will you charge from here to the airport at this hour with two suitcases in the boot?", "इस समय यहाँ से हवाई अड्डे तक दो सूटकेस डिक्की में रखकर कितना किराया लेंगे?", "is samay yahā̃ se havāī aḍḍe tak do sūṭkes ḍikkī mẽ rakh kar kitnā kirāyā leṅge?"],
                    ["Please switch on the meter; if it is broken, let us agree on a fair price before we start moving.", "कृपया मीटर चालू करिए; अगर खराब है तो चलने से पहले उचित भाव तय कर लेते हैं।", "kripayā mīṭar cālū karie; agar kharāb hai to calne se pahle ucit bhāv tay kar lete haiṃ."],
                    ["Could you drive a little slower because my mother feels sick when the auto swerves suddenly?", "क्या आप थोड़ा धीरे चलाइएगा क्योंकि ऑटो अचानक मुड़ने पर मेरी माँ को चक्कर आ जाता है।", "kyā āp thoṛā dhīre calāiega kyõki ôṭo acānak muṛne par merī mā̃ ko cakkār ā jātā hai."],
                    ["Stop right in front of the pharmacy with the blue sign; I will pay you by scanning this QR code.", "नीले साइन वाली दवा की दुकान के ठीक सामने रोकिए; मैं इस क्यूआर कोड से भुगतान कर दूँगा।", "nīle sāin vālī davā kī dukān ke ṭhīk sāmne rokie; main is kyūār koḍ se bhugtān kar dū̃gā."],
                    ["The road is one-way ahead, so please take the U-turn near the temple and then enter the lane.", "आगे सड़क एकतरफ़ा है, इसलिए कृपया मंदिर के पास यू-टर्न लेकर गली में घुस जाइए।", "āge saṛak ekatarafā hai, islie kripayā mandir ke pās yū-ṭarn le kar galī mẽ ghus jāie."],
                    ["I need a printed bill for office reimbursement, so could you issue a receipt even if the amount is small?", "मुझे ऑफिस के लिए प्रिंटेड बिल चाहिए, क्या आप छोटी राशि पर भी रसीद दे सकते हैं?", "mujhe ôphis ke lie priṇṭeḍ bil cāhie, kyā āp choṭī rāśi par bhī rasīd de sakte haiṃ?"],
                    ["Please help me lift this heavy bag carefully; I will hold the door so it does not hit your shoulder.", "कृपया इस भारी बैग को सावधानी से उठाने में मदद करिए; मैं दरवाज़ा पकड़ लेता हूँ ताकि आपके कंधे पर न लगे।", "kripayā is bhārī baig ko sāvdhānī se uṭhāne mẽ madad karie; main darvāzā pakṛ letā hū̃ tāki āp ke kandhe par na lage."],
                    ["If traffic is blocked, I can walk the last two hundred metres; please tell me the safest footpath.", "अगर ट्रैफ़िक जाम है तो मैं आख़िरी दो सौ मीटर पैदल चल सकता हूँ; सबसे सुरक्षित फुटपाथ बता दीजिए।", "agar ṭraifik jām hai to main āxiri do sau mīṭar paidal cal saktā hū̃; sab se surakṣit phuṭpāth batā dījie."],
                    ["Do you have change for five hundred rupees, or should I transfer the exact fare to your phone?", "क्या आपके पास पाँच सौ रुपये का छुट्टा है, या सटीक किराया फोन पर ट्रांसफर कर दूँ?", "kyā āp ke pās pā̃c sau rupye kā chuṭṭā hai, ya saṭīk kirāyā phon par ṭrānsfar kar dū̃?"],
                    ["Thank you for not taking a longer route; I tracked the map and you were honest about every turn.", "धन्यवाद कि आपने लंबा रास्ता नहीं लिया; मैंने नक्शा देखा और आप हर मोड़ पर ईमानदार रहे।", "dhanyavād ki āpne laṃbā rāstā nahī̃ liyā; mainne nakśā dekhā aur āp har moṛ par īmāndār rahe."],
                    ["Keep the helmet strap tight; I have seen autos topple when drivers brake hard on wet roads.", "हेलमेट की पट्टा कसकर बाँधिए; मैंने देखा है कि गीली सड़क पर जोर से ब्रेक लगने पर ऑटो पलट जाते हैं।", "helmeṭ kī paṭṭā kas kar bā̃dhie; mainne dekhā hai kī gīlī saṭak par jor se brek lagne par ôṭo palṭ jāte haiṃ."],
                ],
            ),
        ],
    )


def chapter_628() -> dict:
    return _l(
        "Software workplace: stand-ups, bugs, deployments, and polite Slack messages in Hindi.",
        "Mix English tech terms as Hindi speakers do; keep sentences clear for offshore teammates.",
        [
            _p("Stand-up", "कल रात बिल्ड फेल हो गया — last night the build failed."),
            _t(
                "Software engineers",
                [
                    ["Let us sync after the daily stand-up because I need your review on the pull request I raised yesterday.", "डेली स्टैंड-अप के बाद सिंक कर लेते हैं क्योंकि मुझे कल उठाए गए पुल रिक्वेस्ट पर आपकी समीक्षा चाहिए।", "ḍelī sṭaiṇḍ-ap ke bād siṅk kar lete haiṃ kyõki mujhe kal uṭhā.e ge pul rikvesṭ par āpkī samīkṣā cāhie."],
                    ["The staging server is throwing a five hundred error whenever we upload files larger than ten megabytes.", "स्टेजिंग सर्वर पर दस मेगाबाइट से बड़ी फ़ाइल अपलोड करते ही पाँच सौ वाली एरर आ जाती है।", "sṭejiṅg sarvar par das megābaiṭ se baṛī phāil aploaḍ karte hī pā̃c sau vālī erar ā jātī hai."],
                    ["Could you pair-program with the intern this afternoon so she understands how we refactor legacy modules?", "क्या आप दोपहर इंटर्न के साथ पेयर-प्रोग्रामिंग कर सकते हैं ताकि वह लेगेसी मॉड्यूल रिफैक्टर समझ ले?", "kyā āp dopahar iṭarn ke sāth peyar-progrāmiṅ kar sakte haiṃ tāki vah legesī mŏḍyūl riphaikṭar samajh le?"],
                    ["I will deploy the hotfix after the automated tests pass, and I will monitor the logs for forty minutes.", "ऑटोमेटेड टेस्ट पास होने के बाद हॉटफ़िक्स डिप्लॉय करूँगा और चालीस मिनट लॉग देखता रहूँगा।", "ôṭomeṭeḍ ṭesṭ pās hone ke bād hŏṭfiks ḍiplŏy karū̃gā aur cālīs minaṭ lŏg dektā rahū̃gā."],
                    ["Please document the API changes in Confluence because downstream teams depend on this contract.", "कृपया एपीआई बदलाव कॉन्फ़्लुएंस में लिख दीजिए क्योंकि डाउनस्ट्रीम टीमें इस कॉन्ट्रैक्ट पर निर्भर हैं।", "kripayā epīāī badalāv kŏnfluaiṃs mẽ likh dījie kyõki ḍāunsṭrīm ṭīmeṃ is kŏnṭraiṭ par nirbhar haiṃ."],
                    ["The product manager wants a demo on Friday, so we should freeze features by Wednesday evening.", "प्रोडक्ट मैनेजर शुक्रवार को डेमो चाहते हैं, इसलिए बुधवार शाम तक फ़ीचर फ़्रीज़ कर देना चाहिए।", "proḍakṭ mainejar śukravār ko ḍemo cāhte haiṃ, islie budhavār śām tak fīcar frīj kar denā cāhie."],
                    ["I cannot reproduce the bug on my machine, which suggests the issue might be environment-specific.", "मैं अपनी मशीन पर बग दोहरा नहीं पा रहा, जिससे लगता है समस्या वातावरण विशिष्ट हो सकती है।", "main apanī maśīn par bag dohrā nahī̃ pā rahā, jisse lagtā hai samasyā vātāvaraṇa viśiṣṭ ho saktī hai."],
                    ["Let us respect deep-work hours after lunch unless there is a production outage that needs everyone online.", "दोपहर के बाद डीप-वर्क का सम्मान करें जब तक प्रोडक्शन आउटेज न हो जिसके लिए सब ऑनलाइन हों।", "dopahar ke bād ḍīp-vark kā sammān kareṃ jab tak proḍakśan āuṭej na ho jiske lie sab ônlāin hoṃ."],
                    ["She explained the microservice boundaries slowly so that non-tech stakeholders could follow without jargon overload.", "उसने माइक्रोसर्विस की सीमाएँ धीरे समझाईं ताकि गैर-तकनीकी हितधारक बिना जार्गन के समझ सकें।", "usne māikrosarvis kī sīmāeṃ dhīre samjhāī̃ tāki gair-taknīkī hitdhārak binā jārgan ke samajh sakeṃ."],
                    ["Before merging, run the linter and formatter; our CI pipeline rejects inconsistent indentation outright.", "मर्ज से पहले लिंटर और फ़ॉर्मैटर चलाइए; हमारी सीआई पाइपलाइन असंगत इंडेंटेशन तुरंत अस्वीकार कर देती है।", "marj se pahle liṭar aur phŏrmeṭar calāie; hamārī sīāī pāiplain asaṅgat iṇḍeṭeśan turant asvikār kar detī hai."],
                    ["If you feel burned out, tell the manager early; pretending that everything is fine helps nobody on the team.", "अगर बर्नआउट महसूस हो तो मैनेजर को जल्द बताइए; सब ठीक होने का नाटक टीम में किसी की मदद नहीं करता।", "agar barnā'uṭ mahasūs ho to mainejar ko jald batāie; sab ṭhīk hone kā nāṭak ṭīm mẽ kisī kī madad nahī̃ kartā."],
                    ["We celebrated the release with samosas, yet we also wrote a retrospective note about what slowed us down.", "हमने रिलीज़ समोसे से मनाई, फिर भी हमने रेट्रोस्पेक्टिव नोट लिखा कि हमें क्या धीमा किया।", "hamne rilīj samose se manāī, phir bhī hamne reṭrospekṭiv noṭ likhā ki hameṃ kyā dhīmā kiyā."],
                ],
            ),
        ],
    )


def chapter_629() -> dict:
    return _l(
        "Grocery shop: weights, prices, freshness, and carrying bags home.",
        "Ask यह ताज़ा है? for vegetables; request बिल for totals.",
        [
            _p("Weights", "आधा किलो दाल — half a kilo of lentils."),
            _t(
                "Grocery shop",
                [
                    ["Uncle, please give me one kilo of toor dal, half a kilo of sugar, and a packet of rock salt.", "अंकल, एक किलो अरहर की दाल, आधा किलो चीनी और एक पैकेट सेंधा नमक दे दीजिए।", "aṅkal, ek kilo arhar kī dāl, ādhā kilo cīnī aur ek pekeṭ seṃdhā namak de dījie."],
                    ["Are these tomatoes from the farm this morning, because I need them firm for salad tonight?", "क्या ये टमाटर आज सुबह खेत से आए हैं, क्योंकि मुझे आज रात सलाद के लिए टाइट चाहिए?", "kyā ye ṭamāṭar āj subah khet se ā.e haiṃ, kyõki mujhe āj rāt salād ke lie ṭāiṭ cāhie?"],
                    ["Could you grind the wheat coarsely; my grandmother prefers thick rotis during winter months.", "क्या आप गेहूँ दरदरा पीस देंगे; मेरी दादी सर्दियों में मोटी रोटी पसंद करती हैं।", "kyā āp gehū̃ daradarā pīs deṃge; merī dādī sardiyõ mẽ moṭī roṭī pasand kartī haiṃ."],
                    ["The cooking oil price has risen again, so I will take only two litres until the festival discounts begin.", "खाने के तेल की कीमत फिर बढ़ गई है, इसलिए त्योहार की छूट शुरू होने तक केवल दो लीटर लूँगा।", "khāne ke tel kī kīmat phir baṛh gaī hai, islie tyohār kī chūṭ śurū hone tak keval do līṭar lū̃gā."],
                    ["Do you stock gluten-free oats, or should I try the organic store two lanes away?", "क्या आपके पास ग्लूटेन-फ्री ओट्स हैं, या दो गलियों दूर ऑर्गेनिक स्टोर में कोशिश करूँ?", "kyā āp ke pās glūṭen-frī oṭs haiṃ, yā do galiyõ dūr ôrgenik sṭor mẽ kośiś karū̃?"],
                    ["Please wrap the paneer in butter paper; I have a forty-minute ride and I do not want it to sweat.", "कृपया पनीर को बटर पेपर में लपेट दीजिए; मुझे चालीस मिनट की सवारी है और पसीना नहीं चाहिए।", "kripayā panīr ko baṭar pepar mẽ lapeṭ dījie; mujhe cālīs minaṭ kī savārī hai aur pasīnā nahī̃ cāhie."],
                    ["I forgot my wallet, but I can pay by UPI; kindly confirm once the payment notification reaches you.", "मैं बटुआ भूल गया, पर यूपीआई से भर सकता हूँ; कृपया पुष्टि कर दीजिए जब भुगतान का संदेश आ जाए।", "main baṭuā bhūl gayā, par yūpīāī se bhar saktā hū̃; kripayā puṣṭi kar dījie jab bhugtān kā sandeś ā jā.e."],
                    ["The shop smells of fresh jaggery and cardamom, which reminds me of sweets cooked at my aunt’s house.", "दुकान में गुड़ और इलायची की ताज़ी महक है, जिससे मुझे मौसी के घर बनी मिठाई याद आती है।", "dukān mẽ guṛ aur ilāycī kī tāzī mahak hai, jisse mujhe mausī ke ghar banī miṭhāī yād ātī hai."],
                    ["If the rice has weevils, I would rather walk to another vendor than argue for a long refund process.", "अगर चावल में घुन है तो मैं लंबी रिफ़ंड प्रक्रिया से बहस करने के बजाय दूसरे विक्रेता के पास चला जाऊँगा।", "agar cāval mẽ ghun hai to main laṃbī rifuṇḍ prakriyā se bahas karne ke bajāy dūśre vikretā ke pās calā jāū̃gā."],
                    ["Kindly pack heavy items at the bottom of the cloth bag so that bread on top does not get crushed.", "कृपया भारी चीज़ें कपड़े के थैले के नीचे रखिए ताकि ऊपर की ब्रेड न कुचल जाए।", "kripayā bhārī cīzeṃ kapṛe ke thaile ke nīce rakhie tāki ūpar kī breḍ na kucal jā.e."],
                    ["Your daughter explained the loyalty points clearly, so I downloaded your app before leaving the counter.", "आपकी बेटी ने लॉयल्टी पॉइंट साफ़ समझाए, इसलिए काउंटर छोड़ने से पहले मैंने आपका ऐप डाउनलोड कर लिया।", "āpkī beṭī ne lŏyalṭī pŏiṇṭ sāf samjhā.e, islie kauṇṭar choṛne se pahle mainne āpkā aip ḍāunaloaḍ kar liyā."],
                    ["Thank you for carrying the carton to my scooter; I will recommend your shop to everyone in our apartment.", "मेरी स्कूटर तक कार्टन पहुँचाने के लिए धन्यवाद; मैं अपने अपार्टमेंट में सबको आपकी दुकान बताऊँगा।", "merī skūṭar tak kāṭṭan pahuṃcāne ke lie dhanyavād; main apne apārṭameṇṭ mẽ sabko āpkī dukān batāū̃gā."],
                ],
            ),
        ],
    )


def chapter_630() -> dict:
    return _l(
        "Doctor and patient: symptoms, duration, medicines, and follow-up.",
        "Say दर्द यहाँ है while pointing; mention allergies before new prescriptions.",
        [
            _p("History", "कब से है? — Since when?"),
            _t(
                "Doctor–patient",
                [
                    ["Doctor, I have had a throbbing headache behind my eyes since last night, and bright light makes it worse.", "डॉक्टर, कल रात से मेरी आँखों के पीछे धड़कता सिरदर्द है और रोशनी से और बढ़ जाता है।", "ḍokṭar, kal rāt se merī ā̃khõ ke pīche dhaṛaktā siradard hai aur rośanī se aur baṛh jātā hai."],
                    ["The fever comes and goes, but I sweat heavily at dawn even when the room feels cool to others.", "बुखार उतर-चढ़ कर आता है, पर भोर में ठंडा कमरा होने पर भी मुझे पसीना बहुत आता है।", "bukhār utar-caṛh kar ātā hai, par bhor mẽ thaṃḍā kamrā hone par bhī mujhe pasīnā bahut ātā hai."],
                    ["I feel tightness in the chest when I climb stairs quickly, though resting for two minutes relieves it.", "जब मैं जल्दी सीढ़ियाँ चढ़ता हूँ तो सीने में जकड़न होती है, पर दो मिनट आराम से ठीक हो जाती है।", "jab main jaldī sīḍhiyā̃ caṛhtā hū̃ to sīne mẽ jakṛan hotī hai, par do minaṭ ārām se ṭhīk ho jātī hai."],
                    ["I am allergic to penicillin, so please prescribe an alternative antibiotic if you think infection is likely.", "मुझे पेनिसिलिन से एलर्जी है, इसलिए यदि संक्रमण लगे तो कृपया वैकल्पिक एंटीबायोटिक लिखिए।", "mujhe penisilin se elarjī hai, islie yadi saṅkramaṇ lage to kripayā vaikalpik eṇṭībāyoṭik likhie."],
                    ["The cough is dry and worse at night; my spouse says I snore loudly whenever I sleep on my back.", "खाँसी सूखी है और रात को बढ़ जाती है; मेरे जीवनसाथी कहते हैं कि पीठ के बल सोने पर मैं ज़ोर से खर्राटे लेता हूँ।", "khā̃sī sūkhī hai aur rāt ko baṛh jātī hai; mere jīvansāthī kahte haiṃ ki pīṭh ke bal sone par main zor se kharrāṭe letā hū̃."],
                    ["I recently travelled abroad; could these symptoms relate to something I ate at the airport lounge?", "मैं हाल ही में विदेश गया था; क्या ये लक्षण एयरपोर्ट लाउंज में खाई चीज़ से जुड़ सकते हैं?", "main hāl hī mẽ videś gayā thā; kyā ye lakṣaṇ eyarporṭ lauñj mẽ khāī cīz se juṛ sakte haiṃ?"],
                    ["Please explain the blood test in simple words; medical jargon makes my elderly father anxious.", "कृपया रक्त जाँच सरल शब्दों में समझाइए; चिकित्सा शब्दजाल से मेरे बुज़ुर्ग पिता घबरा जाते हैं।", "kripayā rakta jā̃c saral śabdõ mẽ samjhāie; cikitsā śabdjāl se mere buzurg pitā ghabarā jāte haiṃ."],
                    ["I will take the full course of tablets even if I feel better, because I know stopping early breeds resistance.", "मैं गोलियों का पूरा कोर्स लूँगा भले ही अच्छा लगे, क्योंकि बीच में छोड़ने से प्रतिरोध बढ़ता है।", "main goliyõ kā pūrā kors lū̃gā bhale hī acchā lage, kyõki bīc mẽ choṛne se pratirodh baṛhtā hai."],
                    ["Could you refer me to a physiotherapist; my wrist still hurts three weeks after the minor fall?", "क्या आप मुझे फिजियोथेरेपिस्ट के पास भेज सकते हैं; छोटी चोट के तीन हफ़्ते बाद भी कलाई दुखती है?", "kyā āp mujhe phijioterepisṭ ke pās bhej sakte haiṃ; choṭī coṭ ke tīn hafte bād bhī kalāī dukhtī hai?"],
                    ["Nurse, please note my blood pressure on both arms; the left reading has been higher lately.", "नर्स जी, कृपया दोनों बाँहों पर ब्लड प्रेशर नोट करिए; बाएँ हाथ की रीडिंग हाल में ज़्यादा आ रही है।", "nars jī, kripayā donõ bā̃hõ par blaḍ preśar noṭ karie; bāẽ hāth kī rīḍiṅ hāl mẽ zyādā ā rahī hai."],
                    ["I will schedule the ultrasound next week because work deadlines made it hard to come earlier.", "अल्ट्रासाउंड अगले हफ़्ते कराऊँगा क्योंकि काम की डेडलाइन से पहले आना मुश्किल था।", "alṭrāsāuṇḍ agale hafte karāū̃gā kyõki kām kī ḍeḍlāin se pahle ānā muśkil thā."],
                    ["Thank you for listening patiently; I feel calmer already knowing that the pain is not my imagination.", "धैर्य से सुनने के लिए धन्यवाद; यह जानकर कि दर्द काल्पनिक नहीं, मैं पहले से शांत महसूस कर रहा हूँ।", "dhairya se sunne ke lie dhanyavād; yah jān kar ki dard kālpanik nahī̃, main pahle se śānt mahasūs kar rahā hū̃."],
                ],
            ),
        ],
    )


def chapter_631() -> dict:
    return _l(
        "Classroom: attendance, homework, doubts, and respectful address to teachers.",
        "Use गुरु जी or टीचर with आप; raise hand before speaking.",
        [
            _p("Homework", "कल तक यह अभ्यास पूरा करिए — finish this practice by tomorrow."),
            _t(
                "Teacher & students",
                [
                    ["May I come in, ma’am? I missed the bus, yet I still reached before the first period began.", "क्या मैं अंदर आ सकता हूँ, मैडम? बस छूट गई थी, फिर भी मैं पहली पीरियड शुरू होने से पहले पहुँच गया।", "kyā main andar ā saktā hū̃, maiḍam? bas chūṭ gaī thī, phir bhī main pahlī pīriyar śurū hone se pahle pahuṃc gayā."],
                    ["I did not understand the third step of the algebra problem; could you demonstrate it once more on the board?", "बीजगणित के इस सवाल का तीसरा चरण समझ नहीं आया; क्या आप बोर्ड पर फिर से दिखा सकती हैं?", "bījagaṇit ke is savāl kā tīsrā caraṇ samajh nahī̃ āyā; kyā āp borḍ par phir se dikhā saktī haiṃ?"],
                    ["Our group will present the environmental project on Friday, and we have prepared charts with local data.", "हमारा समूह शुक्रवार को पर्यावरण परियोजना प्रस्तुत करेगा और हमने स्थानीय आँकड़ों वाले चार्ट तैयार किए हैं।", "hamārā samūh śukravār ko paryāvaraṇ pariyojanā prastut karegā aur hamne sthānīy ā̃kḍõ vāle cārṭ taiyār kie haiṃ."],
                    ["I promise I will submit the essay before midnight; my internet failed yesterday while uploading the file.", "मैं वादा करता हूँ कि निबंध आधी रात से पहले जमा कर दूँगा; कल फ़ाइल अपलोड करते समय इंटरनेट फेल हो गया था।", "main vādā kartā hū̃ ki nibandh ādhī rāt se pahle jamā kar dū̃gā; kal phāil aploaḍ karte samay intarnet phel ho gayā thā."],
                    ["Could we have five extra minutes for the quiz because the question paper was distributed late?", "क्या हमें क्विज़ के लिए पाँच मिनट अतिरिक्त मिल सकते हैं क्योंकि प्रश्नपत्र देर से बाँटा गया?", "kyā hameṃ kvij ke lie pā̃c minaṭ atirikt mil sakte haiṃ kyõki praśn-patr der se bāṭā gayā?"],
                    ["The playground is wet after rain, so may we practice indoors today for the Republic Day parade?", "बारिश के बाद खेल का मैदान गीला है, क्या आज गणतंत्र दिवस परेड के लिए हम अंदर अभ्यास करें?", "bāriś ke bād khel kā maidān gīlā hai, kyā āj gaṇatantra divas pareḍ ke lie ham andar abhyās kareṃ?"],
                    ["I feel nervous before speaking in assembly; could you suggest breathing exercises that calm the voice?", "सभा में बोलने से पहले घबराहट होती है; क्या आप ऐसी साँस की कसरत बता सकती हैं जिससे आवाज़ शांत हो?", "sabhā mẽ bolne se pahle ghabrāhaṭ hotī hai; kyā āp aisī sā̃s kī kasarat batā saktī haiṃ jisse āvāz śānt ho?"],
                    ["She translated the Hindi poem into English for her friend, yet she still asked the teacher about one metaphor.", "उसने अपने दोस्त के लिए हिन्दी कविता का अंग्रेज़ी में अनुवाद किया, फिर भी एक रूपक के लिए शिक्षक से पूछा।", "usne apne dost ke lie hindī kavitā kā aṅgrezī mẽ anuvād kiyā, phir bhī ek rūpak ke lie śikṣak se pūchā."],
                    ["Please do not deduct marks for handwriting alone; my arm was in a sling last month after the bicycle accident.", "कृपया केवल लिखावट पर अंक मत काटिए; पिछले महीने साइकिल दुर्घटना के बाद मेरी बाँह स्लिंग में थी।", "kripayā keval likhāvaṭ par aṅk mat kāṭie; pichale mahīne sāikil durghaṭnā ke bād merī bā̃h sliṅg mẽ thī."],
                    ["We need permission to visit the science museum next Tuesday; the principal’s note is attached here.", "अगले मंगलवार विज्ञान संग्रहालय जाने की अनुमति चाहिए; प्रधानाचार्य का नोट यहाँ संलग्न है।", "agale maṅgalvār vigyān saṅgrahālay jāne kī anumati cāhie; pradhānācāry kā noṭ yahā̃ sannagn hai."],
                    ["I will help my classmate who missed lessons because of fever; sharing notes strengthens everyone’s learning.", "मैं उस सहपाठी की मदद करूँगा जो बुखार से कक्षा छूट गया; नोट साझा करने से सबकी पढ़ाई मज़बूत होती है।", "main us sahapāṭhī kī madad karū̃gā jo bukhār se kakṣā chūṭ gayā; noṭ sājhā karne se sabkī paṛhāī mazbūt hotī hai."],
                    ["Thank you for believing that I can improve; your encouragement makes me want to attempt harder problems.", "धन्यवाद कि आपको विश्वास है कि मैं सुधार सकता हूँ; आपका उत्साह मुझे कठिन सवालों की कोशिश करने को प्रेरित करता है।", "dhanyavād ki āpko viśvās hai ki main sudhār saktā hū̃; āpkā utsāh mujhe kaṭhin savālõ kī kośiś karne ko prerit kartā hai."],
                ],
            ),
        ],
    )


def chapter_632() -> dict:
    return _l(
        "Informal phone talk: signal, battery, callbacks, and quick plans with friends.",
        "Start with हाँ बोलो or कहाँ हो? among peers; avoid loudspeaker in public.",
        [
            _p("Signal", "आवाज़ कट रही है — your voice is breaking."),
            _t(
                "Informal phone",
                [
                    ["Hey, can you hear me clearly now, or should I step out onto the balcony where the network is stronger?", "अरे, अब साफ़ सुनाई दे रहा है या मैं बालकनी में चला जाऊँ जहाँ नेटवर्क मज़बूत है?", "are, ab sāf sunāī de rahā hai yā main bālkonī mẽ calā jāū̃ jahā̃ neṭvark mazbūt hai?"],
                    ["My phone is about to die; I will text you the address in two minutes once I plug in the charger.", "मेरा फोन बंद होने वाला है; चार्जर लगाते ही दो मिनट में पता मैसेज कर दूँगा।", "merā phon band hone vālā hai; cārjar lagāte hī do minaṭ mẽ patā meśej kar dū̃gā."],
                    ["I am driving right now, so let us keep it short unless it is urgent about the rent payment.", "मैं अभी गाड़ी चला रहा हूँ, इसलिए जब तक किराए की जल्दी न हो तब तक संक्षेप में रहें।", "main abhī gāṛī calā rahā hū̃, islie jab tak kirā.e kī jaldī na ho tab tak saṅkṣep mẽ raheṃ."],
                    ["Call me after dinner; mom gets annoyed if I talk loudly while she is watching the serial.", "खाने के बाद फोन करना; माँ सीरियल देखते समय ज़ोर से बात करने पर नाराज़ हो जाती हैं।", "khāne ke bād phon karnā; mā̃ sīriyal dekhte samay zor se bāt karne par nārāz ho jātī haiṃ."],
                    ["Did you send the voice note? My data pack expired yesterday and I could not download anything.", "क्या तुमने वॉइस नोट भेजा? मेरा डाटा पैक कल खत्म हो गया था और कुछ डाउनलोड नहीं हो पाया।", "kyā tumne vŏis noṭ bhejā? merā ḍāṭā pāk kal khatm ho gayā thā aur kuch ḍāunaloaḍ nahī̃ ho pāyā."],
                    ["We are already late for the movie; please book the tickets online while I find parking near the mall.", "हम फ़िल्म के लिए पहले से देर से हैं; कृपया तुम ऑनलाइन टिकट बुक करो जब तक मैं मॉल के पास पार्किंग ढूँढता हूँ।", "ham film ke lie pahle se der se haiṃ; kripayā tum ônlāin ṭikaṭ buk karo jab tak main mŏl ke pās pārkiṅg ḍhū̃ṛhtā hū̃."],
                    ["I will put you on speaker so grandma can hear your birthday wishes; speak a little louder, okay?", "मैं स्पीकर पर लगाता हूँ ताकि दादी तुम्हारी जन्मदिन की बधाई सुन सकें; थोड़ा ज़ोर से बोलना, ठीक है?", "main spīkar par lagātā hū̃ tāki dādī tumhāre janmdin kī badhāī sun sakeṃ; thoṛā zor se bolna, ṭhīk hai?"],
                    ["Sorry, I pocket-dialled you; ignore the rustling sound—that was just my keys.", "माफ़ करना, जेब से गलती से कॉल लग गई; खड़खड़ाहट अनदेखी करो—वह तो चाबी थी।", "māf karnā, jeb se galtī se kŏl lag gaī; khaṛkhaṛāhaṭ andekhī karo—vah to cābī thī."],
                    ["Let us switch to video once I reach home; walking through the market now is too noisy for a call.", "घर पहुँचकर वीडियो पर आ जाते हैं; अब बाज़ार में चलते हुए कॉल के लिए शोर बहुत है।", "ghar pahuṃc kar vīḍiyo par ā jāte haiṃ; ab bāzār mẽ calte hue kŏl ke lie śor bahut hai."],
                    ["If the call drops, I will ring you back immediately; do not assume I hung up on purpose.", "अगर कल ड्रॉप हो जाए तो मैं तुरंत वापस फोन करूँगा; यह मत समझना कि जानबूझकर काटा।", "agar kal ḍrŏp ho jā.e to main turant vāpas phon karū̃gā; yah mat samajhnā ki jān-bujh kar kāṭā."],
                    ["Your voice sounds tired; sleep early tonight and we can plan the trip tomorrow morning properly.", "तुम्हारी आवाज़ थकी लग रही है; आज रात जल्दी सो जाओ, कल सुबह यात्रा ठीक से प्लान करेंगे।", "tumhārī āvāz thakī lag rahī hai; āj rāt jaldī so jāo, kal subah yātrā ṭhīk se plān kareṅge."],
                    ["Thanks for checking on me after the interview; hearing your laugh made the stress feel lighter.", "इंटरव्यू के बाद पूछने के लिए धन्यवाद; तुम्हारी हँसी सुनकर तनाव हल्का लगा।", "iṭarvyū ke bād pūchne ke lie dhanyavād; tumhārī hãsī sun kar tanāv halkā lagā."],
                ],
            ),
        ],
    )


def chapter_633() -> dict:
    return _l(
        "Vegetable market: bargaining, quality, seasonal stock, and carrying bags.",
        "Compare दो दुकानों के भाव before buying in bulk.",
        [
            _p("Price", "आज भाव क्या चल रहा है? — What is the going rate today?"),
            _t(
                "Vegetable market",
                [
                    ["Aunty, are these coriander bunches freshly cut, because yesterday’s bunch wilted within hours at home?", "आंटी, ये धनिया की पत्तियाँ अभी काटी हैं क्योंकि कल वाली घर आते ही मुरझा गई थीं।", "ā̃ṭī, ye dhaniyā kī pattiyā̃ abhī kāṭī haiṃ kyõki kal vālī ghar āte hī murjhā gaī thī̃."],
                    ["Could you sort the potatoes and remove the green ones; I read that they can be mildly toxic.", "क्या आप आलू छाँटकर हरे वाले अलग कर देंगे; मैंने पढ़ा है कि वे हल्के विषैले हो सकते हैं।", "kyā āp ālū chā̃ṭ kar hare vāle alag kar deṃge; mainne paṛhā hai ki ve halke viṣaile ho sakte haiṃ."],
                    ["I need ripe tomatoes for chutney, not salad, so please pick softer ones with deep red skin.", "मुझे चटनी के लिए पके टमाटर चाहिए, सलाद के नहीं, इसलिए गहरे लाल छिलके वाले नरम चुन लीजिए।", "mujhe caṭnī ke lie pake ṭamāṭar cāhie, salād ke nahī̃, islie gahre lāl chilke vāle naram cun lijie."],
                    ["The okra feels slimy; I will pass unless you can show me a fresher crate from the back.", "भिंडी चिपचिपी लग रही है; जब तक पीछे से ताज़ा टोकरा न दिखाएँ मैं लूँगा नहीं।", "bhiṃḍī cipcipī lag rahī hai; jab tak pīche se tāzā ṭokrā na dikhāeṃ main lū̃gā nahī̃."],
                    ["Give me a fair price for five kilos of onions; I am buying for a community kitchen feeding students.", "पाँच किलो प्याज का उचित भाव दीजिए; मैं छात्रों को खाना खिलाने वाले समुदायिक रसोई के लिए ले रहा हूँ।", "pā̃c kilo pyāz kā ucit bhāv dījie; main chātrõ ko khānā khilāne vāle samudāyik rasoī ke lie le rahā hū̃."],
                    ["Is this spinach organic, or should I expect pesticide residue like last week’s batch?", "क्या यह पालक जैविक है, या पिछले हफ़्ते की तरह कीटनाशक की उम्मीद रखूँ?", "kyā yah pālak jaivik hai, yā pichale hafte kī tarah kīṭanāśak kī ummīd rakhū̃?"],
                    ["Please weigh on a calibrated scale; I noticed another vendor’s machine tilted suspiciously yesterday.", "कृपया कैलिब्रेटेड तराजू पर तौलिए; मैंने देखा कि कल दूसरे विक्रेता का काँटा संदिग्ध ढंग से झुका था।", "kripayā kailibreṭeḍ tarājū par taulie; mainne dekhā ki kal dūśre vikretā kā kā̃ṭā saṅdigdh ḍhaṅg se jhukā thā."],
                    ["I will take extra lemons because guests suddenly confirmed for dinner and I need sharbat.", "मुझे अतिरिक्त नींबू चाहिए क्योंकि मेहमानों ने अचानक रात के खाने की पुष्टि कर दी और शरबत बनाना है।", "mujhe atirikt nī̃bū cāhie kyõki mehmānõ ne acānak rāt ke khāne kī puṣṭi kar dī aur śarbat banānā hai."],
                    ["Could you chop the pumpkin into large cubes; my cook asked for uniform pieces for the stew.", "क्या आप कद्दू को बड़े टुकड़ों में काट देंगे; रसोइया ने स्ट्यू के लिए एक समान टुकड़े माँगे हैं।", "kyā āp kaddū ko baṛe ṭukḍõ mẽ kāṭ deṃge; rasoiyā ne sṭyū ke lie ek samān ṭukḍe māṅge haiṃ."],
                    ["The crowd is pushing; please hand me my change before someone else grabs the wrong bag.", "भीड़ धक्का दे रही है; कृपया पहले छुट्टा दे दीजिए वरना कोई गलत थैला उठा लेगा।", "bhīṛ dhakkā de rahī hai; kripayā pahle chuṭṭā de dījie varnā koī galat thailā uṭhā legā."],
                    ["Rain splashed mud on the leafy greens; will you wash them once lightly before packing?", "बारिश से पत्तेदार सब्ज़ियों पर कीचड़ लग गया; पैक करने से पहले हल्का धो देंगे?", "bāriś se patteḍār sabziyõ par kīcaṛ lag gayā; pāk karne se pahle halkā dho deṃge?"],
                    ["Thank you for saving the last bunch of methi; I will tell neighbours to visit your stall early tomorrow.", "आख़िरी मेथी का गुच्छा रखने के लिए धन्यवाद; मैं पड़ोसियों को कल सुबह आपके स्टॉल पर जल्दी आने को कहूँगा।", "āxiri methī kā gucchā rakhne ke lie dhanyavād; main paṛosiyõ ko kal subah āp ke sṭŏl par jaldī āne ko kahū̃gā."],
                ],
            ),
        ],
    )


def chapter_634() -> dict:
    return _l(
        "Bus travel: stops, routes, tickets, seats, and courtesy to elders.",
        "Confirm किस स्टॉप पर उतरना है with the conductor if unsure.",
        [
            _p("Ticket", "किराया कितना है? — What is the fare?"),
            _t(
                "Bus stop & bus",
                [
                    ["Excuse me, does this bus go to the IT park via the ring road, or should I wait for the express?", "माफ़ कीजिए, क्या यह बस रिंग रोड से आईटी पार्क जाती है या मुझे एक्सप्रेस का इंतज़ार करना चाहिए?", "māf kījie, kyā yah bas riṅg roḍ se āīṭī pārk jātī hai yā mujhe ekspres kā intazār karnā cāhie?"],
                    ["How many stops before the hospital gate; I need to stand near the exit because my leg is injured?", "अस्पताल के गेट से पहले कितने स्टॉप हैं; मेरी टाँग में चोट है इसलिए निकास के पास खड़ा रहना है।", "aspatāl ke geṭ se pahle kitne sṭŏp haiṃ; merī tā̃g mẽ coṭ hai islie nikās ke pās khaṛā rehnā hai."],
                    ["Two tickets to the central bus stand, please; here is the exact change so the queue moves faster.", "केंद्रीय बस अड्डे के दो टिकट दीजिए; यहाँ सटीक छुट्टा है ताकि कतार तेज़ चले।", "kendrīy bas aḍḍe ke do ṭikaṭ dījie; yahā̃ saṭīk chuṭṭā hai tāki katār tez cale."],
                    ["Could you lower the window slightly; the diesel smell makes me nauseous when we crawl in traffic.", "क्या आप खिड़की थोड़ी नीचे कर सकते हैं; ट्रैफ़िक में रेंगते समय डीज़ल की गंध से मुझे मिचली होती है।", "kyā āp khiṛkī thoṛī nīce kar sakte haiṃ; ṭraifik mẽ reṅgte samay ḍīzal kī gandh se mujhe miclī hotī hai."],
                    ["Please reserve this seat for the elderly gentleman; I will stand until the next major stop.", "कृपया यह सीट उस बुज़ुर्ग के लिए रखिए; अगले बड़े स्टॉप तक मैं खड़ा रहूँगा।", "kripayā yah sīṭ us buzurg ke lie rakhie; agale baṛe sṭŏp tak main khaṛā rahū̃gā."],
                    ["The conductor said the bus would detour because of the protest; should we expect a thirty-minute delay?", "कंडक्टर ने कहा कि प्रदर्शन के कारण बस रूट बदलेगी; क्या तीस मिनट की देरी मानें?", "kaṇḍakṭar ne kahā ki pradarśan ke kāraṇ bas rūṭ badlegī; kyā tīs minaṭ kī derī māneṃ?"],
                    ["I missed my stop while replying to an email; can I walk back from the flyover or should I take an auto?", "ईमेल का जवाब देते हुए मेरा स्टॉप छूट गया; क्या फ्लाईओवर से पैदल लौटूँ या ऑटो लूँ?", "īmel kā javāb dete hue merā sṭŏp chūṭ gayā; kyā flāiovar se paidal lauṭū̃ yā ôṭo lū̃?"],
                    ["Please hold the railing; sudden brakes threw a child forward yesterday on this same route.", "कृपया रेलिंग पकड़िए; कल इसी रूट पर अचानक ब्रेक से एक बच्चा आगे गिर गया था।", "kripayā reliṅg pakṛie; acānak isī rūṭ par acānak brek se ek baccā āge gir gayā thā."],
                    ["Is there space under the seat for my backpack, or should I place it on the overhead rack carefully?", "क्या सीट के नीचे बैग के लिए जगह है, या सावधानी से ओवरहेड रैक पर रखूँ?", "kyā sīṭ ke nīce baig ke lie jagah hai, yā sāvdhānī se overheḍ raik par rakhū̃?"],
                    ["The digital display shows the next stop incorrectly; I will ask the driver once we cross the bridge.", "डिजिटल डिस्प्ले अगला स्टॉप गलत दिखा रहा है; पुल पार करने के बाद ड्राइवर से पूछ लूँगा।", "ḍijiṭal ḍisple agalā sṭŏp galat dikhā rahā hai; pul pār karne ke bād ḍrāivar se pūch lū̃gā."],
                    ["Thank you for letting women with infants board first; that small kindness reduces chaos at the door.", "छोटे बच्चों वाली महिलाओं को पहले चढ़ने देने के लिए धन्यवाद; यह छोटी सी दया दरवाज़े पर भगदड़ कम करती है।", "choṭe baccõ vālī mahilāõ ko pahle caṛhne dene ke lie dhanyavād; yah choṭī sī dayā darvāze par bhagdaḍ kam kartī hai."],
                    ["We reached ten minutes early because traffic was light; I will grab chai before the office opens.", "ट्रैफ़िक हल्का होने से दस मिनट जल्दी पहुँच गए; ऑफिस खुलने से पहले चाय पी लूँगा।", "ṭraifik halkā hone se das minaṭ jaldī pahuṃc ga.e; ôphis khulne se pahle cāy pī lū̃gā."],
                ],
            ),
        ],
    )


def chapter_635() -> dict:
    return _l(
        "Asking and giving addresses: landmarks, pin codes, and repeating for clarity.",
        "Say फिर से धीरे बोलिए if you did not catch the lane name.",
        [
            _p("Landmark", "पोस्ट ऑफिस के पीछे — behind the post office."),
            _t(
                "Asking address",
                [
                    ["Could you write the full address on my phone map, including the pin code and the building colour?", "क्या आप पूरा पता मेरे फोन के नक्शे पर लिख देंगे, पिन कोड और इमारत का रंग सहित?", "kyā āp pūrā patā mere phon ke nakśe par likh deṃge, pin koḍ aur imārat kā raṅg sahit?"],
                    ["I am looking for house number forty-two B; does it come before or after the temple on this lane?", "मैं बयालीस बी नंबर का घर ढूँढ रहा हूँ; क्या यह गली में मंदिर से पहले आता है या बाद में?", "main bayālīs bī nambar kā ghar ḍhū̃ṛ rahā hū̃; kyā yah galī mẽ mandir se pahle ātā hai yā bād mẽ?"],
                    ["Is this the correct road for Rose Society, or should I have taken the flyover exit two kilometres back?", "क्या यह रोज़ सोसाइटी के लिए सही सड़क है, या दो किलोमीटर पीछे फ्लाईओवर का एक्ज़िट लेना चाहिए था?", "kyā yah roz sosāiṭī ke lie sahī saṛak hai, yā do kilomīṭar pīche flāiovar ekjjit lenā cāhie thā?"],
                    ["The courier could not find my flat because the nameplate fell off during the last storm.", "कूरियर को मेरा फ़्लैट नहीं मिला क्योंकि पिछले तूफ़ान में नेमप्लेट गिर गई थी।", "kūriyar ko merā flaiṭ nahī̃ milā kyõki pichale tūfān mẽ nemplēṭ gir gaī thī."],
                    ["Please repeat the colony name slowly; it sounds similar to another sector on the opposite side of town.", "कृपया कॉलोनी का नाम धीरे दोहराइए; यह शहर के दूसरी तरफ़ के सेक्टर जैसा लगता है।", "kripayā kŏlonī kā nām dhīre dohrāie; yah śahar kī dūsrī taraf ke sekṭar jaise lagtā hai."],
                    ["I will share my live location for ten minutes so that you can guide the ambulance through the narrow lanes.", "मैं दस मिनट के लिए लाइव लोकेशन शेयर करता हूँ ताकि आप एम्बुलेंस को पतली गलियों से निकाल सकें।", "main das minaṭ ke lie lāiv lokeśan śeyar kartā hū̃ tāki āp embuleṃs ko patlī galiyõ se nikāl sakeṃ."],
                    ["Does this building have two wings labelled East and West; my friend lives in the East tower?", "क्या इस इमारत में पूर्व और पश्चिम दो विंग हैं; मेरा दोस्त पूर्व टावर में रहता है?", "kyā is imārat mẽ pūrva aur paścim do viṅg haiṃ; merā dost pūrva ṭāvar mẽ rehtā hai?"],
                    ["The watchman speaks only regional Hindi; could you translate the directions he just shouted?", "चौकीदार केवल स्थानीय हिन्दी बोलता है; क्या आप वह दिशा-निर्देश अनुवाद कर सकते हैं जो उसने अभी चिल्लाए?", "caukīdār keval sthānīy hindī boltā hai; kyā āp vah diśā-nirdeś anuvād kar sakte haiṃ jo usne abhī cillā.e?"],
                    ["I noted the nearest metro exit as B two because that matches what your message said about the lift.", "निकटतम मेट्रो निकास बी टू लिख लिया क्योंकि आपके संदेश में लिफ़्ट से मेल खाता है।", "nikatatam meṭro nikās bī ṭū likh liyā kyõki āp ke sandeś mẽ lifṭ se mel khātā hai."],
                    ["If I take a wrong turn at the roundabout, how many metres must I reverse before I see the petrol pump?", "गोल चक्कर पर गलत मुड़ जाऊँ तो पेट्रोल पंप दिखने से पहले कितने मीटर पीछे हटना होगा?", "gol cakkar par galat muṛ jāū̃ to peṭrol paṃp dikhne se pahle kitne mīṭar pīche haṭnā hogā?"],
                    ["Thank you for drawing a small map on paper; digital maps sometimes fail when the battery dies mid-route.", "कागज़ पर छोटा नक्शा बनाने के लिए धन्यवाद; बीच रास्ते बैटरी खत्म होने पर डिजिटल नक्शे कभी काम नहीं करते।", "kāgaz par choṭā nakśā banāne ke lie dhanyavād; bīc rāste baiṭarī khatm hone par ḍijiṭal nakśe kabhī kām nahī̃ karte."],
                    ["I will call again once I spot the blue water tank you mentioned; until then I will keep driving slowly.", "जब आपके बताए नीले पानी की टंकी दिखेगी तब फिर फोन करूँगा; तब तक धीरे चलाता रहूँगा।", "jab āp ke batā.e nīle pānī kī ṭaṅkī dikhegī tab phir phon karū̃gā; tab tak dhīre calātā rahū̃gā."],
                ],
            ),
        ],
    )


def chapter_636() -> dict:
    return _l(
        "Expressing love and serious interest respectfully: feelings, timing, and gentle boundaries.",
        "Prefer sincerity over film dialogue; accept a no gracefully and preserve friendship when possible.",
        [
            _p("Tone", "मैं आपको पसंद करता हूँ — I like you / care for you (context)."),
            _t(
                "Love & proposing",
                [
                    ["I have admired how kindly you treat everyone, and I would like to know you more deeply over time.", "मैंने देखा है कि आप सबके साथ कितनी दयालुता से पेश आते हैं, और समय के साथ मैं आपको और गहराई से जानना चाहूँगा।", "mainne dekhā hai ki āp sab ke sāth kitnī dayālutā se peś āte haiṃ, aur samay ke sāth main āpko aur gahrāī se jānnā cāhū̃gā."],
                    ["Would you share coffee this weekend so we can talk openly without the noise of the office corridor?", "क्या आप इस हफ़्ते अंत में कॉफ़ी साझा करेंगे ताकि ऑफिस की गलियारे के शोर के बिना खुलकर बात कर सकें?", "kyā āp is hafte ant mẽ kŏfī sājhā kareṅge tāki ôphis kī galiyāre ke śor ke binā khulkar bāt kar sakeṃ?"],
                    ["I am not rushing a decision; I only want you to know that my feelings are sincere and carefully considered.", "मैं कोई जल्दबाज़ी में फैसला नहीं चाहता; मैं केवल चाहता हूँ कि आप जानें कि मेरी भावनाएँ ईमानदार और सोच-समझ कर हैं।", "main koī jaldabāzī mẽ faislā nahī̃ cāhtā; main keval cāhtā hū̃ ki āp jāneṃ ki merī bhāvnāeṃ īmāndār aur soc-samajh kar haiṃ."],
                    ["Your dreams matter to me, and if we walk together I promise to support your career plans without insecurity.", "आपके सपने मेरे लिए मायने रखते हैं, और अगर हम साथ चलें तो मैं बिना असुरक्षा के आपके करियर की योजनाओं का साथ देने का वादा करता हूँ।", "āp ke sapne mere lie māyne rakhte haiṃ, aur agar ham sāth caleṃ to main binā asurakṣā ke āp ke kariyar kī yojnāõ kā sāth dene kā vādā kartā hū̃."],
                    ["If you need space to think, I will respect silence and will not flood your phone with repeated messages.", "अगर सोचने के लिए समय चाहिए तो मैं खामोशी का सम्मान करूँगा और बार-बार संदेशों से फोन नहीं भरूँगा।", "agar socne ke lie samay cāhie to main khāmośī kā sammān karū̃gā aur bār-bār sandeśõ se phon nahī̃ bharū̃gā."],
                    ["Meeting your family is not a condition for my affection; I only hope we can be honest with each other first.", "आपके परिवार से मिलना मेरे स्नेह की शर्त नहीं है; मैं केवल यह चाहता हूँ कि पहले हम एक-दूसरे से ईमानदार रहें।", "āp ke parivār se milnā mere sneh kī śart nahī̃ hai; main keval yah cāhtā hū̃ ki pahle ham ek-dūsre se īmāndār raheṃ."],
                    ["I value our friendship even if romance is not mutual, and I will not spread gossip about this conversation.", "यदि पारस्परिक रोमांस न भी हो तो मैं हमारी दोस्ती की कद्र करता हूँ और इस बातचीत की अफ़वाह नहीं फैलाऊँगा।", "yadi pārasprik romāns na bhī ho to main hamārī dostī kī kadra kartā hū̃ aur is bātcīt kī afvāh nahī̃ phailāū̃gā."],
                    ["When you smiled at my nervous joke, I felt relief, because vulnerability in love should feel safe, not judged.", "जब आपने मेरे घबराहट भरे मज़ाक पर मुस्कुराया तो मुझे राहत मिली, क्योंकि प्यार में कमज़ोरी सुरक्षित लगनी चाहिए, आलोचना नहीं।", "jab āpne mere ghabrāhaṭ bhare mazāk par muskurāyā to mujhe rāhat milī, kyõki pyār mẽ kamzorī surakṣit lagnī cāhie, ālocanā nahī̃."],
                    ["I wrote you a letter because some feelings deserve paper rather than a hurried voice note at midnight.", "मैंने आपको पत्र लिखा क्योंकि कुछ भावनाएँ कागज़ की हक़दार हैं, आधी रात के जल्दबाज़ वॉइस नोट की नहीं।", "mainne āpko patr likhā kyõki kuch bhāvnāeṃ kāgaz kī haqdār haiṃ, ādhī rāt ke jaldabāz vŏis noṭ kī nahī̃."],
                    ["If your answer is no, I will still greet you warmly at work and will not make the hallway awkward for you.", "अगर आपका उत्तर ना है तो भी मैं काम पर गर्मजोशी से अभिवादन करूँगा और गलियारा आपके लिए अजीब नहीं बनाऊँगा।", "agar āpkā uttar nā hai to bhī main kām par garmajośī se abhivādan karū̃gā aur galiyārā āp ke lie ajīb nahī̃ banāū̃gā."],
                    ["Parents worry about stability, so I am saving responsibly and learning skills that prove I can build a future.", "माता-पिता को स्थिरता की चिंता होती है, इसलिए मैं ज़िम्मेदारी से बचत कर रहा हूँ और ऐसे कौशल सीख रहा हूँ जो भविष्य बनाने की पुष्टि करें।", "mātā-pitā ko sthiratā kī cintā hotī hai, islie main zimmedārī se bacaṭ kar rahā hū̃ aur aise kauśal sīkh rahā hū̃ jo bhaviṣya banāne kī puṣṭi kareṃ."],
                    ["Love, for me, includes listening when you are tired without trying to fix every problem immediately.", "मेरे लिए प्यार में यह भी शामिल है कि जब आप थके हों तो बिना हर समस्या तुरंत सुलझाए सुनूँ।", "mere lie pyār mẽ yah bhī śāmil hai ki jab āp thake hoṃ to binā har samasyā turant suljhā.e sunū̃."],
                ],
            ),
        ],
    )


def chapter_637() -> dict:
    return _l(
        "Job interview: greeting, background, strengths, salary tact, and closing thanks.",
        "Use formal आप; prepare a clear उम्मीद salary range if asked.",
        [
            _p("Opening", "मुझे इस पद में रुचि है — I am interested in this role."),
            _t(
                "Interview",
                [
                    ["Good afternoon; thank you for interviewing me today despite your packed calendar of client meetings.", "नमस्कार; आज आपके ग्राहक मीटिंग से भरे कैलेंडर के बावजूद साक्षात्कार के लिए धन्यवाद।", "namaskār; āj āp ke grāhak mīṭiṅ se bhare kailaiṇḍar ke bāvajūd sākṣātkār ke lie dhanyavād."],
                    ["I bring five years of supply-chain analytics, and I can share a dashboard example that reduced stock-outs by twelve percent.", "मैं पाँच साल की सप्लाई-चेन एनालिटिक्स लाता हूँ, और एक डैशबोर्ड उदाहरण दिखा सकता हूँ जिससे स्टॉक-आउट बारह प्रतिशत घटे।", "main pā̃c sāl kī saplāī-cen enāliṭiks lātā hū̃, aur ek ḍaiśborḍ udāharaṇ dikhā saktā hū̃ jisse sṭŏk-ā'uṭ bārah pratiśat ghaṭe."],
                    ["My greatest strength is calm communication during outages; my weakness is that I sometimes over-document to reassure teams.", "मेरी सबसे बड़ी ताकत आउटेज के दौरान शांत संवाद है; कमज़ोरी यह है कि कभी टीम को आश्वस्त करने के लिए ज़्यादा दस्तावेज़ बना देता हूँ।", "merī sab se baṛī tākat ā'uṭej ke daurān śānt saṃvād hai; kamzorī yah hai ki kabhī ṭīm ko āśvast karne ke lie zyādā dastāvez banā detā hū̃."],
                    ["I researched your recent expansion into tier-two cities, and I would love to contribute to distribution strategy there.", "मैंने आपके टियर-टू शहरों में हालिया विस्तार पर शोध की है और वहाँ वितरण रणनीति में योगदान देना चाहूँगा।", "mainne āp ke ṭiyar-ṭū śaharõ mẽ hāliyā vistār par śodh kī hai aur vahā̃ vitaraṇ raṇnīti mẽ yogdān denā cāhū̃gā."],
                    ["Salary expectations align with industry benchmarks for this grade, and I am open to performance-linked components.", "वेतन अपेक्षा इस ग्रेड के उद्योग मानकों से मेल खाती है, और मैं प्रदर्शन-जुड़े घटकों के लिए खुला हूँ।", "vetan apekṣā is greḍ ke udyog mānakõ se mel khātī hai, aur main pradarśan-juṛe ghaṭkõ ke lie khulā hū̃."],
                    ["I can join within thirty days after accepting the offer, and I will complete knowledge transfer at my current firm.", "ऑफर स्वीकार करने के तीस दिनों के भीतर मैं जॉइन कर सकता हूँ, और वर्तमान फर्म में ज्ञान हस्तांतरण पूरा करूँगा।", "ofar svīkār karne ke tīs dinõ ke bhītara main jŏin kar saktā hū̃, aur vartamāṭ firm mẽ jñān hastāntaraṇ pūrā karū̃gā."],
                    ["If you want, I can walk through a conflict I mediated between sales and finance last quarter.", "यदि चाहें तो मैं पिछली तिमाही में सेल्स और वित्त के बीच मध्यस्थता किए विवाद को समझा सकता हूँ।", "yadi cāheṃ to main pichlī timāhī mẽ sels aur vitt ke bīc madhyasthatā kie vivād ko samjhā saktā hū̃."],
                    ["I admire your company’s ethics policy; could you describe how managers handle whistle-blower complaints in practice?", "मैं आपकी नैतिकता नीति की सराहना करता हूँ; क्या आप बता सकते हैं कि प्रबंधक व्हिसल-ब्लोवर शिकायतों को व्यवहार में कैसे संभालते हैं?", "main āpkī naitikta nītī kī sarāhnā kartā hū̃; kyā āp batā sakte haiṃ ki prabaṅdhak visal-blovār śikāyatõ ko vyavahār mẽ kaise saṃbhālte haiṃ?"],
                    ["Remote collaboration is familiar to me; I coordinate across time zones without letting tasks slip through cracks.", "मुझे रिमोट सहयोग अच्छी तरह आता है; मैं समय क्षेत्रों में समन्वय करता हूँ बिना कार्यों के फिसलने दिए।", "mujhe rimoṭ sahayog acchī tarah ātā hai; main samay kṣetrõ mẽ samanvay kartā hū̃ binā kāryõ ke phisalne die."],
                    ["I have a question about mentorship here; will I report to someone who invests in weekly one-on-one conversations?", "मेरा एक सवाल मेंटरशिप के बारे में है; क्या मैं किसी ऐसे व्यक्ति को रिपोर्ट करूँगा जो साप्ताहिक एक-पर-एक बातचीत में निवेश करे?", "merā ek savāl meṭarśip ke bāre mẽ hai; kyā main kisī aise vyakti ko ripoṭ karū̃gā jo sāptāhik ek-par-ek bātcīt mẽ niveś kare?"],
                    ["Thank you for challenging my assumptions; constructive pressure helps me refine models faster than working alone.", "मेरे अनुमानों को चुनौती देने के लिए धन्यवाद; रचनात्मक दबाव अकेले काम की तुलना में मॉडल तेज़ निखारता है।", "mere anumānõ ko cunaūtī dene ke lie dhanyavād; racanātmak dabāv akle kām kī tulnā mẽ mŏḍal tez nikhārtā hai."],
                    ["I look forward to hearing next steps; whichever the outcome, I appreciate the team’s transparent process today.", "मैं अगले चरण सुनने की प्रतीक्षा करता हूँ; परिणाम जो भी हो, मैं आज की पारद प्रक्रिया की सराहना करता हूँ।", "main agale caraṇ sunne kī pratīkṣā kartā hū̃; pariṇām jo bhī ho, main āj kī pārda prakriyā kī sarāhnā kartā hū̃."],
                ],
            ),
        ],
    )


def chapter_638() -> dict:
    return _l(
        "Household help: clear instructions, respectful tone, time off, and fair pay.",
        "Say कृपया; avoid shouting; agree on छुट्टी and salary day in advance.",
        [
            _p("Clarity", "आज झाड़ू लगा दीजिए — please sweep today."),
            _t(
                "Housemaid",
                [
                    ["Aunty, please wipe the kitchen platform with a separate cloth after you finish washing the utensils.", "आंटी, बर्तन धोने के बाद कृपया रसोई का प्लेटफ़ॉर्म अलग कपड़े से पोंछ दीजिए।", "ā̃ṭī, bartan dhone ke bād kripayā rasoī kā pleṭphŏrm alag kapṛe se poṃch dījie."],
                    ["If you feel feverish, take the day off without worry; your health matters more than a spotless floor today.", "अगर बुखार जैसा महसूस हो तो बिना चिंता के छुट्टी लीजिए; आज फर्श से ज़्यादा आपकी सेहत ज़रूरी है।", "agar bukhār jaise mahasūs ho to binā cintā ke chuṭṭī lijie; āj farś se zyādā āpkī sehat zarūrī hai."],
                    ["We will pay salary on the fifth of every month by bank transfer, and we will share the receipt screenshot with you.", "हम हर महीने पाँच तारीख को बैंक ट्रांसफर से वेतन देंगे और रसीद का स्क्रीनशॉट आपको भेज देंगे।", "ham har mahīne pā̃c tārīkh ko baiṅk ṭrānsfar se vetan deṃge aur rasīd kā skrīnśŏṭ āpko bhej deṃge."],
                    ["Please do not use bleach on silk curtains; I will leave a labelled bottle of mild detergent on the shelf.", "रेशम के पर्दों पर ब्लीच मत लगाइए; मैं शेल्फ पर हल्के डिटर्जेंट की बोतल लेबल करके रख दूँगा।", "reśam ke pardõ par blīc mat lagāie; main śelph par halke ḍiṭarjeṇṭ kī botal lebal kar ke rakh dū̃gā."],
                    ["The children will be studying for exams, so if possible run the vacuum after four in the evening.", "बच्चे परीक्षा की तैयारी कर रहे हैं, इसलिए हो सके तो शाम चार बजे के बाद वैक्यूम चलाइए।", "bacce parīkṣā kī taiyārī kar rahe haiṃ, islie ho sake to śām cār baje ke bād vaikyūm calāie."],
                    ["If anything breaks while cleaning, just tell us honestly; we prefer truth over discovering chips later.", "सफ़ाई के दौरान अगर कुछ टूट जाए तो सच बता दीजिए; हमें बाद में टूटन पता लगने से सच्चाई बेहतर लगती है।", "safāī ke daurān agar kuch ṭūṭ jā.e to sac batā dījie; hameṃ bād mẽ ṭūṭan patā lagne se saccāī behtar lagtī hai."],
                    ["You mentioned your daughter’s school fees are due; if you need an advance, please speak calmly on Monday.", "आपने कहा था कि बेटी की स्कूल फीस जमा करनी है; अगर अग्रिम चाहिए तो सोमवार को शांति से बात करिए।", "āpne kahā thā ki beṭī kī skūl phīs jamā karnī hai; agar agrim cāhie to somvār ko śānti se bāt karie."],
                    ["During festivals we will give a small bonus, separate from salary, because we value your loyalty through the year.", "त्योहारों पर हम वेतन के अलावा छोटा बोनस देंगे क्योंकि हम साल भर आपकी निष्ठा की कद्र करते हैं।", "tyohārõ par ham vetan ke alāvā choṭā bonas deṃge kyõki ham sāl bhar āpkī niṣṭhā kī kadra karte haiṃ."],
                    ["Please lock the door from inside when you mop the balcony; pigeons sometimes fly in suddenly.", "बालकनी पोंछते समय कृपया अंदर से ताला लगा लीजिए; कबूतर कभी अचानक अंदर आ जाते हैं।", "bālkonī poṃchte samay kripayā andar se tālā lagā lijie; kabūtar kabhī acānak andar ā jāte haiṃ."],
                    ["If neighbours speak rudely, tell us instead of arguing; we will handle society matters respectfully.", "अगर पड़ोसी बुरा बर्ताव करें तो बहस के बजाय हमें बताइए; हम सोसाइटी का मामला सम्मान से सुलझाएँगे।", "agar paṛosī burā bartāv kareṃ to bahas ke bajāy hameṃ batāie; ham sosāiṭī kā mamlā sammān se suljhāeṃge."],
                    ["We will provide masks and gloves while you handle bathroom cleaning chemicals; safety is shared responsibility.", "बाथरूम की सफ़ाई में रसायन चलाते समय हम मास्क और दस्ताने देंगे; सुरक्षा साझा ज़िम्मेदारी है।", "bāthrūm kī safāī mẽ rasāyan calāte samay ham māsk aur dastāne deṃge; surakṣā sājhā zimmedārī hai."],
                    ["Thank you for folding clothes neatly; little habits like that make the whole apartment feel cared for.", "कपड़े सलीके से मोड़ने के लिए धन्यवाद; ऐसी छोटी आदतें पूरे फ़्लैट को देखभाल वाला महसूस कराती हैं।", "kapṛe salīke se moṛne ke lie dhanyavād; aisī choṭī ādateṃ pūre flaiṭ ko dekhbhāl vālā mahasūs karātī haiṃ."],
                ],
            ),
        ],
    )


def chapter_639() -> dict:
    return _l(
        "Linking Aadhaar to mobile: OTP, biometric update centres, and avoiding scams.",
        "Never share OTP; official SMS comes from short codes you can verify.",
        [
            _p("OTP", "ओटीपी किसी को न दें — never share your OTP."),
            _t(
                "Aadhaar → mobile",
                [
                    ["The telecom shop asked for my Aadhaar number and fingerprint scan to complete the SIM re-verification process.", "टेलीकॉम शॉप ने सिम की पुनः-सत्यापन प्रक्रिया के लिए मेरा आधार नंबर और फिंगरप्रिंट स्कैन माँगा।", "ṭelīkŏm śŏp ne sim kī punar-satyāpan prakriyā ke lie merā ādhār nambar aur fiṅgarpriṇṭ skaina māṅgā."],
                    ["I received an OTP on the registered mobile within seconds, and I typed it myself on the secure keypad.", "पंजीकृत मोबाइल पर सेकंडों में ओटीपी आया और मैंने उसे सुरक्षित कीपैड पर खुद टाइप किया।", "pañjīkṛit mobail par sekaiṇḍõ mẽ oṭīpī āyā aur mainne use surakṣit kīpaiḍ par khud ṭāip kiyā."],
                    ["The executive warned that linking fails if the name spelling differs slightly from the Aadhaar database.", "अधिकारी ने चेतावनी दी कि यदि नाम की वर्तनी आधार डेटाबेस से थोड़ी भिन्न हो तो लिंकिंग फेल हो सकती है।", "adhikārī ne cetāvanī dī ki yadi nām kī vartanī ādhār ḍeṭābes se thoṛī bhinn ho to liṅkiṅg phel ho saktī hai."],
                    ["I carried the original Aadhaar card and a photocopy because the outlet insisted on both for audit trails.", "मैंने मूल आधार कार्ड और फोटोकॉपी साथ रखी क्योंकि आउटलेट ने ऑडिट ट्रेल के लिए दोनों पर ज़ोर दिया।", "mainne mūl ādhār kārd aur phoṭokŏpī sāth rakhī kyõki a'uṭleṭ ne ôḍiṭ ṭrel ke lie donõ par zor diyā."],
                    ["If biometric fails because of dry skin, the operator used a moist wipe and scanned again successfully.", "अगर सूखी त्वचा से बायोमेट्रिक फेल हो तो ऑपरेटर ने गीला वाइप लगाकर फिर स्कैन किया और सफलता मिली।", "agar sūkhī tvacā se bāyomeṭrik phel ho to ôpareṭar ne gīlā vāip lagākar phir skain kiyā aur saphaltā milī."],
                    ["I refused when a stranger on WhatsApp offered to link my Aadhaar remotely for a small fee.", "जब व्हाट्सऐप पर अजनबी ने छोटी फीस पर दूर से आधार लिंक करने की पेशकश की तो मैंने मना कर दिया।", "jab vhaṭsaip par ajnabī ne choṭī phīs par dūr se ādhār liṅk karne kī peśakaś kī to mainne manā kar diyā."],
                    ["The receipt mentions the request ID so I can track status on the telecom portal if activation delays.", "रसीद में अनुरोध आईडी लिखी है ताकि सक्रियण में देरी हो तो टेलीकॉम पोर्टल पर स्थिति देख सकूँ।", "rasīd mẽ anurodh āīḍī likhī hai tāki sakriyaṇ mẽ derī ho to ṭelīkŏm porṭal par sthiti dekh sakū̃."],
                    ["Customer care clarified that linking Aadhaar to mobile is mandatory only under current government rules, not optional.", "ग्राहक सेवा ने स्पष्ट किया कि आधार से मोबाइल लिंक वर्तमान सरकारी नियमों के तहत अनिवार्य है, वैकल्पिक नहीं।", "grāhak sevā ne spaṣṭ kiyā ki ādhār se mobail liṅk vartamān sarkārī niyamõ ke tahat anivārya hai, vaikalpik nahī̃."],
                    ["Elderly customers can ask the store to call a helpline on speaker so children at home can hear the instructions.", "बुज़ुर्ग ग्राहक स्टोर से हेल्पलाइन स्पीकर पर बुलाने को कह सकते हैं ताकि घर के बच्चे निर्देश सुन लें।", "buzurg grāhak sṭor se helpulain spīkar par bulāne ko kah sakte haiṃ tāki ghar ke bacce nirdeś sun leṃ."],
                    ["After successful linking, I deleted the OTP message and avoided saving screenshots in public galleries.", "सफल लिंकिंग के बाद मैंने ओटीपी संदेश मिटा दिया और सार्वजनिक गैलरी में स्क्रीनशॉट नहीं रखा।", "saphal liṅkiṅg ke bād mainne oṭīpī sandeś miṭā diyā aur sārvajanik gailarī mẽ skrīnśŏṭ nahī̃ rakhā."],
                    ["If you change your name legally, update Aadhaar first; otherwise mobile linking will keep rejecting your request.", "यदि कानूनी रूप से नाम बदलें तो पहले आधार अपडेट करें; वरना मोबाइल लिंकिंग आपका अनुरोध अस्वीकार करती रहेगी।", "yadi kānūnī rūp se nām badleṃ to pahle ādhār apḍeṭ kareṃ; varnā mobail liṅkiṅg āpkā anurodh asvikār kartī rahegī."],
                    ["The queue was long, but staff offered water and shade umbrellas so senior citizens did not faint in the sun.", "कतार लंबी थी, पर स्टाफ ने पानी और छाता दिया ताकि बुज़ुर्ग धूप में बेहोश न हों।", "katār laṃbī thī, par sṭāph ne pānī aur chātā diyā tāki buzurg dhūp mẽ behoś na hoṃ."],
                ],
            ),
        ],
    )


def chapter_640() -> dict:
    return _l(
        "Linking mobile number to Aadhaar record: UIDAI portal, mAadhaar app, and verification SMS.",
        "Update at enrolment centre if you changed numbers without linking.",
        [
            _p("UIDAI", "यूआईडीएआई की वेबसाइट पर लॉगिन करें — log in on the UIDAI website."),
            _t(
                "Mobile → Aadhaar",
                [
                    ["I logged into the UIDAI portal with OTP to add my new mobile number to the Aadhaar profile securely.", "मैंने ओटीपी से यूआईडीएआई पोर्टल पर लॉग इन करके आधार प्रोफ़ाइल में नया मोबाइल सुरक्षित जोड़ा।", "mainne oṭīpī se yūāīḍeāī porṭal par lŏg in kar ke ādhār prophāil mẽ nayā mobail surakṣit joṛā."],
                    ["The website asked me to confirm the last four digits of my previous number before accepting the update.", "वेबसाइट ने अपडेट स्वीकार करने से पहले पुराने नंबर के अंतिम चार अंकों की पुष्टि माँगी।", "vebsāiṭ ne apḍeṭ svīkār karne se pahle purāne nambar ke antim cār aṅkõ kī puṣṭī māṅgī."],
                    ["If you lost the old SIM, visit an Aadhaar centre with ID proof to register the fresh number after verification.", "यदि पुराना सिम खो गया हो तो पहचान पत्र के साथ आधार केंद्र पर जाकर नए नंबर का सत्यापन कराएँ।", "yadi purānā sim kho gayā ho to pahcān patra ke sāth ādhār keṃdra par jā kar nae nambar kā satyāpan karāeṃ."],
                    ["The mAadhaar app sent a masked OTP so that shoulder-surfing in queues is less risky.", "एमआधार ऐप ने मास्क्ड ओटीपी भेजा ताकि कतार में कंधे के ऊपर से देखना कम खतरनाक हो।", "emādhār aip ne māsḍe oṭīpī bhejā tāki katār mẽ kandhe ke ūpar se dekhna kam khatarnāk ho."],
                    ["I avoided third-party agents who promised instant updates for cash outside the official ecosystem.", "मैंने उन दलालों से बचा जो आधिकारिक इकोसिस्टम के बाहर नकद में तुरंत अपडेट का वादा करते हैं।", "mainne un dalālõ se bacā jo adhikārik ikosisiṭam ke bāhar nakad mẽ turant apḍeṭ kā vādā karte haiṃ."],
                    ["After updating, UIDAI sent an SMS alert so I could confirm that the correct tower icon appeared.", "अपडेट के बाद यूआईडीएआई ने एसएमएस अलर्ट भेजा ताकि मैं पुष्टि कर सकूँ कि सही टावर आइकन दिखा।", "apḍeṭ ke bād yūāīḍeāī ne esemes alarṭ bhejā tāki main puṣṭi kar sakū̃ ki sahī ṭāvar aaikan dikhā."],
                    ["My bank SMS now matches Aadhaar records, which reduces friction when I apply for government subsidies online.", "अब बैंक का एसएमएस आधार रिकॉर्ड से मेल खाता है, जिससे ऑनलाइन सब्सिडी के लिए रगड़ कम होती है।", "ab baiṅk kā esemes ādhār rikŏrḍ se mel khātā hai, jisse ônlāin sabsiḍī ke lie ragaṛ kam hotī hai."],
                    ["Teenagers in our family learned to screenshot the confirmation page before closing the browser accidentally.", "हमारे परिवार के किशोरों ने सीखा कि ब्राउज़र गलती से बंद होने से पहले पुष्टि पेज का स्क्रीनशॉट लें।", "hamāre parivār ke kiśorõ ne sīkhā ki brāujar galtī se band hone se pahle puṣṭi pej kā skrīnśŏṭ leṃ."],
                    ["If two family members share one Aadhaar-linked phone, clarify primary holder to customer care to avoid mix-ups.", "यदि एक आधार-लिंक फोन दो सदस्य साझा करें तो ग्राहक सेवा को प्राथमिक धारक स्पष्ट करें।", "yadi ek ādhār-liṅk phon do sadasy sājhā kareṃ to grāhak sevā ko prāthmik dhārak spaṣṭ kareṃ."],
                    ["International roaming sometimes blocks OTP; temporarily enable SMS abroad before you travel for updates.", "अंतरराष्ट्रीय रोमिंग कभी ओटीपी रोक देती है; अपडेट के लिए विदेश जाने से पहले अस्थायी रूप से एसएमएस सक्षम करें।", "antarraṣṭrīy romiṅg kabhī oṭīpī rok detī hai; apḍeṭ ke lie videś jāne se pahle asthāyī rūp se esemes sakṣam kareṃ."],
                    ["Community volunteers helped illiterate residents complete the form with voice guidance in local dialect.", "सामुदायिक स्वयंसेवकों ने अशिक्षित निवासियों को स्थानीय बोली में आवाज़ के मार्गदर्शन से फॉर्म भरवाया।", "sāmudāyik svayaṃsevakõ ne aśikṣit nivāsiyõ ko sthānīy bolī mẽ āvāz ke mārgdarśan se phŏrm bharvāyā."],
                    ["I bookmarked the official UIDAI Twitter handle to distinguish genuine announcements from fake forwards.", "मैंने आधिकारिक यूआईडीएआई ट्विटर हैंडल बुकमार्क किया ताकि नकली फॉरवर्ड से असली घोषणा अलग पहचान सकूँ।", "mainne adhikārik yūāīḍeāī ṭviṭar haiṇḍal bukmārḍ kiyā tāki naklī phŏrvarḍ se aslī ghoṣaṇā alag pahcān sakū̃."],
                ],
            ),
        ],
    )


def chapter_641() -> dict:
    return _l(
        "Republic Day: parade, flag hoisting, patriotic songs, and civic pride in Hindi.",
        "Watch राष्ट्रगण; know that the chief guest protocol is a big diplomatic detail.",
        [
            _p("26 January", "गणतंत्र दिवस की हार्दिक शुभकामनाएँ — warm Republic Day wishes."),
            _t(
                "Republic Day",
                [
                    ["On twenty-six January we remember how India’s Constitution came into force and defined equal rights for all.", "२६ जनवरी को हम याद करते हैं कि भारत का संविधान कैसे लागू हुआ और सभी के लिए समान अधिकार तय किए।", "26 janvarī ko ham yād karte haiṃ ki bhārat kā saṃvidhān kaise lāgū huā aur sabhī ke lie samān adhikār taye kie."],
                    ["Children in our apartment practised marching drills for weeks so their tiny parade looked disciplined and joyful.", "हमारे अपार्टमेंट के बच्चों ने हफ़्तों मार्चिंग अभ्यास किया ताकि उनकी छोटी परेड अनुशासित और खुशहाल लगे।", "hamāre apārṭameṇṭ ke baccõ ne haftõ mārciṅg abhyās kiyā tāki unkī choṭī pareḍ anuśāsit aur khushhāl lage."],
                    ["We watched the live telecast from Rajpath while grandparents explained the significance of each contingent.", "हमने राजपथ से सीधा प्रसारण देखा जबकि दादा-दादी प्रत्येक दल के महत्व को समझा रहे थे।", "hamne rājpath se sīdhā prasāraṇ dekhā jabaki dādā-dādī pratyek dal ke mahatva ko samjhā rahe the."],
                    ["The tricolour fluttered above the school gate as the principal urged students to uphold constitutional values daily.", "प्रधानाचार्य ने छात्रों से कहा कि वे संवैधानिक मूल्यों को रोज़ जीवन में बनाए रखें जब तिरंगा फहराया गया।", "pradhānācāry ne chātrõ se kahā ki ve saṃvaidhānik mūlyõ ko roz jīvan mẽ banā.e rakheṃ jab tiraṅgā phahrāyā gayā."],
                    ["My cousin’s NCC unit earned applause because their drill matched the rhythm of the military band perfectly.", "मेरे कज़िन की एनसीसी यूनिट ने तालियाँ बटोरी क्योंकि उनका ड्रिल सैन्य बैंड की लय से पूरी तरह मिला।", "mere kazin kī ensīsī yūniṭ ne tāliyā̃ baṭorī kyõki unkā ḍril sainya baiṇḍ kī lay se pūrī tarah milā."],
                    ["We discussed why the President unfurls the flag on Republic Day while the Prime Minister does so on Independence Day.", "हमने चर्चा की कि गणतंत्र दिवस पर राष्ट्रपति ध्वज फहराते हैं जबकि स्वतंत्रता दिवस पर प्रधानमंत्री ऐसा करते हैं।", "hamne carcā kī ki gaṇatantra divas par rāṣṭrapati dhvaj phahrāte haiṃ jabaki svatantratā divas par pradhānamaṃtri aise karte haiṃ."],
                    ["Street vendors sold paper flags responsibly, refusing to litter plastic sticks after the celebration ended.", "सड़क वाले विक्रेताओं ने कागज़ के झंडे ज़िम्मेदारी से बेचे और उत्सव के बाद प्लास्टिक की छड़ें न फेंकने से मना किया।", "saṛak vāle vikretāõ ne kāgaz ke jhaṇḍe zimmedārī se beche aur utsav ke bād plāsṭik kī chaṛeṃ na pheṅkne se manā kiyā."],
                    ["A debate in college highlighted how fundamental duties complement rights in a functioning democracy.", "कॉलेज में वाद-विवाद ने दिखाया कि काम करने वाले लोकतंत्र में मौलिक कर्तव्य अधिकारों के पूरक हैं।", "kŏlej mẽ vād-vivād ne dikhāyā ki kām karne vāle lokatantra mẽ maulik kartavya adhikārõ ke pūrak haiṃ."],
                    ["We sang “Vande Mataram” softly during the evening gathering because neighbours preferred a calm tribute.", "शाम के समारोह में हमने “वन्दे मातरम्” धीरे गाया क्योंकि पड़ोसियों ने शांत श्रद्धांजलि पसंद की।", "śām ke samāroh mẽ hamne “vande mātaram” dhīre gāyā kyõki paṭosiyõ ne śānt śraddhā̃jali pasand kī."],
                    ["The local MLA thanked sanitation workers who cleaned the route before dawn so the parade route sparkled.", "स्थानीय विधायक ने स्वच्छता कर्मियों को धन्यवाद दिया जिन्होंने भोर से पहले मार्ग साफ़ किया।", "sthānīy vidhāyak ne svacchatā karmiyõ ko dhanyavād diyā jinhoṃne bhor se pahle mārg sāf kiyā."],
                    ["My niece asked why tanks roll on Republic Day, and we explained deterrence and peace through strength carefully.", "भतीजी ने पूछा गणतंत्र दिवस पर टैंक क्यों चलते हैं, तो हमने सावधानी से निरोध और शांति समझाई।", "batījī ne pūchā gaṇatantra divas par ṭaiṅk kyõ calte haiṃ, to hamne sāvdhānī se nirodh aur śānti samjhāī."],
                    ["Before sleeping, we read two articles from the Constitution’s preamble aloud to feel connected to its ideals.", "सोने से पहले हमने संविधान की प्रस्तावना के दो अनुच्छेद ज़ोर से पढ़े ताकि आदर्शों से जुड़ाव महसूस हो।", "sone se pahle hamne saṃvidhān kī prastāvnā ke do anucched zor se paṛhe tāki ādharśõ se juṛāv mahasūs ho."],
                ],
            ),
        ],
    )


def chapter_642() -> dict:
    return _l(
        "Bank visit: account opening, cheque deposit, ATM card, and secure PIN habits.",
        "Never share OTP or card PIN; ask for काउंटर नंबर when in doubt.",
        [
            _p("Queue", "कतार में नंबर लीजिए — take a token in the queue."),
            _t(
                "In bank",
                [
                    ["Good morning, I would like to open a savings account and understand the minimum balance rules clearly.", "सुप्रभात, मैं बचत खाता खोलना चाहता हूँ और न्यूनतम शेष नियमों को स्पष्ट समझना चाहता हूँ।", "suprabhāt, main bacaṭ khātā kholnā cāhtā hū̃ aur nyūnatam śeṣ niyamõ ko spaṣṭ samajhnā cāhtā hū̃."],
                    ["Please confirm whether SMS alerts are free and whether I can set transaction limits through net banking.", "कृपया पुष्टि करें कि एसएमएस अलर्ट मुफ़्त हैं और क्या नेट बैंकिंग से लेनदेन सीमा तय कर सकता हूँ।", "kripayā puṣṭi kareṃ ki esemes alarṭ muf̤t haiṃ aur kyā neṭ baiṅkiṅg se len-den sīmā tay kar saktā hū̃."],
                    ["I need to deposit this cheque before cut-off time; could you stamp the receipt with today’s date?", "मुझे कट-ऑफ़ से पहले यह चेक जमा करना है; क्या आप रसीद पर आज की तारीख का मुहर लगा देंगे?", "mujhe kaṭ-ŏf se pahle yah cek jamā karnā hai; kyā āp rasīd par āj kī tārīkh kā muhar lagā deṃge?"],
                    ["The ATM swallowed my card after three wrong attempts; what documents should I bring to retrieve it?", "तीन गलत प्रयासों के बाद एटीएम ने मेरा कार्ड निगल लिया; वापस पाने के लिए कौन से कागज़ लाऊँ?", "tīn galat prayāsõ ke bād eṭīem ne merā kārd nigal liyā; vāpas pāne ke lie kaun se kāgaz lāū̃?"],
                    ["I want to enable international usage for two weeks; please explain the charges for currency conversion.", "मैं दो हफ़्ते के लिए अंतरराष्ट्रीय उपयोग चालू करना चाहता हूँ; मुद्रा परिवर्तन शुल्क समझाइए।", "main do hafte ke lie antarraṣṭrīy upayog cālū karnā cāhtā hū̃; mudrā parivartan śulk samjhāie."],
                    ["Could you print last year’s interest certificate for my home loan; I need it for income-tax filing.", "क्या आप मेरे होम लोन का पिछले साल का ब्याज प्रमाणपत्र प्रिंट कर सकते हैं; मुझे आयकर भरने के लिए चाहिए।", "kyā āp mere hom lon kā pichale sāl kā byāj pramāṇapatr priṇṭ kar sakte haiṃ; mujhe āyakar bharne ke lie cāhie."],
                    ["The relationship manager suggested a recurring deposit; I asked how premature withdrawal penalties work.", "रिलेशनशिप मैनेजर ने आवर्ती जमा सुझाई; मैंने पूछा कि समय से पहले निकासी पर जुर्माना कैसे लगता है।", "rileśanśip mainejar ne āvartī jamā sujhāī; mainne pūchā ki samay se pahle nikāsī par jurmānā kaise lagtā hai."],
                    ["I refused to share my OTP when someone called pretending to be from the bank’s security desk.", "जब किसी ने बैंक की सुरक्षा डेस्क होने का नाटक करके ओटीपी माँगा तो मैंने साझा करने से मना कर दिया।", "jab kisī ne baiṅk kī surakṣā ḍesk hone kā nāṭak kar ke oṭīpī māṅgā to mainne sājhā karne se manā kar diyā."],
                    ["Please help my mother fill the nomination form because she is uncomfortable with small English boxes.", "कृपया मेरी माँ को नामांकन फॉर्म भरने में मदद करिए क्योंकि छोटे अंग्रेज़ी बॉक्स से उन्हें झिझक होती है।", "kripayā merī mā̃ ko nāmāṅkan phŏrm bharne mẽ madad karie kyõki choṭe aṅgrezī bŏk se unheṃ jhijhak hotī hai."],
                    ["The cashier counted notes twice in front of me and slid them under the glass partition without rushing.", "कैशियर ने मेरे सामने नोट दो बार गिने और बिना जल्दबाज़ी के काँच के पार सरकाए।", "kaśiyar ne mere sāmne noṭ do bār gine aur binā jaldabāzī ke kā̃c ke pār sarakā.e."],
                    ["I downloaded the bank’s official app only from the Play Store because fake icons circulate on messaging apps.", "मैंने बैंक का आधिकारिक ऐप केवल प्ले स्टोर से डाउनलोड किया क्योंकि नकली आइकन मैसेजिंग ऐप पर घूमते हैं।", "mainne baiṅk kā adhikārik aip keval ple sṭor se ḍāunaloaḍ kiyā kyõki naklī aaikan meśejiṅg aip par ghūmte haiṃ."],
                    ["Thank you for explaining UPI disputes; I now know I should raise complaints within the prescribed window.", "यूपीआई विवाद समझाने के लिए धन्यवाद; अब मुझे पता है कि निर्धारित समय के भीतर शिकायत उठानी चाहिए।", "yūpīāī vivād samjhāne ke lie dhanyavād; ab mujhe patā hai ki nirdhārit samay ke bhītara śikāyat uṭhānī cāhie."],
                ],
            ),
        ],
    )


def chapter_643() -> dict:
    return _l(
        "Temple visit: timings, dress, prasad, photography rules, and respectful behaviour.",
        "Cover head if local custom asks; switch phones to silent.",
        [
            _p("Darshan", "दर्शन का समय क्या है? — What are the darshan timings?"),
            _t(
                "Temple visit enquiry",
                [
                    ["Could you tell me whether the sanctum opens before sunrise and whether special tickets are available for quicker entry?", "क्या आप बता सकते हैं कि गर्भगृह सूर्योदय से पहले खुलता है और तेज़ प्रवेश के लिए विशेष टिकट मिलते हैं?", "kyā āp batā sakte haiṃ ki garbhagṛh sūryoday se pahle khultā hai aur tez praveś ke lie viśeṣ ṭikaṭ milte haiṃ?"],
                    ["We travelled with elderly parents, so is there a wheelchair path and a shaded waiting area near the gate?", "हम बुज़ुर्ग माता-पिता के साथ आए हैं, क्या व्हीलचेयर का रास्ता और छायादार प्रतीक्षा स्थल है?", "ham buzurg mātā-pitā ke sāth ā.e haiṃ, kyā vhīlceyer kā rāstā aur chāyādār pratīkṣā sthal hai?"],
                    ["Does the temple provide lockers for shoes and bags, or should we leave them in the car across the street?", "क्या मंदिर जूते और बैग के लिए लॉकर देता है, या सड़क पार कार में छोड़ना पड़ेगा?", "kyā mandir jūte aur baig ke lie lŏkar detā hai, yā saṛak pār kār mẽ choṛnā paṛegā?"],
                    ["I want to offer flowers purchased outside; will priests accept them if the stems are still fresh and thorn-free?", "मैं बाहर से फूल चढ़ाना चाहता हूँ; क्या पुजारी स्वीकार करेंगे यदि डंठल ताज़े और काँटे रहित हों?", "main bāhar se phūl caṛhānā cāhtā hū̃; kyā pujārī svīkāreṃge yadi ḍaṃṭhal tāze aur kā̃ṭe rahit hoṃ?"],
                    ["Are mobile phones completely banned inside, or may we keep them switched off in our pockets?", "क्या मोबाइल अंदर पूरी तरह मना है, या हम उन्हें बंद कर जेब में रख सकते हैं?", "kyā mobail andar pūrī tarah manā hai, yā ham unheṃ band kar jeb mẽ rakh sakte haiṃ?"],
                    ["We hope to attend the evening aarti; how early should we arrive to get a spot near the bell tower?", "हम शाम की आरती में शामिल होना चाहते हैं; घंटाघर के पास जगह पाने के लिए कितनी जल्दी आएँ?", "ham śām kī āratī mẽ śāmil honā cāhte haiṃ; ghaṇṭāghar ke pās jagah pāne ke lie kitnī jaldī āeṃ?"],
                    ["Is there a clean drinking-water station, because we are walking in the heat with two small children?", "क्या स्वच्छ पीने के पानी की व्यवस्था है, क्योंकि हम दो छोटे बच्चों के साथ धूप में चलकर आए हैं?", "kyā svacch pīne ke pānī kī vyavasthā hai, kyõki ham do choṭe baccõ ke sāth dhūp mẽ cal kar ā.e haiṃ?"],
                    ["The guide mentioned a museum behind the temple; does the combined ticket include both audio guide and lift access?", "गाइड ने बताया मंदिर के पीछे संग्रहालय है; क्या संयुक्त टिकट में ऑडियो गाइड और लिफ़्ट दोनों शामिल हैं?", "gāiḍ ne batāyā mandir ke pīche saṅgrahālay hai; kyā saṃyukt ṭikaṭ mẽ ôḍiyo gāiḍ aur lifṭ donõ śāmil haiṃ?"],
                    ["We respect local dress codes, so my wife carries a dupatta even though our city temple does not insist.", "हम स्थानीय पोशाक संहिता का सम्मान करते हैं, इसलिए मेरी पत्नी दुपट्टा साथ रखती है भले ही शहर के मंदिर में ज़ोर न हो।", "ham sthānīy pośāk saṃhitā kā sammān karte haiṃ, islie merī patnī dupaṭṭā sāth rakhtī hai bhale hī śahar ke mandir mẽ zor na ho."],
                    ["Photography was allowed only in the courtyard, so we asked a stranger to capture our family without flash.", "फोटोग्राफी केवल आँगन में मंज़ूर थी, इसलिए हमने अजनबी से फ्लैश के बिना पारिवारिक फोटो खिंचवाई।", "phoṭograiphī keval ā̃gan mẽ manjūr thī, islie hamne ajnabī se flaiś ke binā pārikārik phoṭo khimcavāī."],
                    ["After darshan we distributed prasad equally among drivers waiting outside so nobody felt left out.", "दर्शन के बाद हमने बाहर इंतज़ार कर रहे ड्राइवरों में प्रसाद बराबर बाँटा ताकि कोई अलग महसूस न करे।", "darśan ke bād hamne bāhar intazār kar rahe ḍrāivarõ mẽ prasād barābar bāṭā tāki koī alag mahasūs na kare."],
                    ["I quietly observed how volunteers swept the marble steps without interrupting devotees lost in prayer.", "मैंने चुपचाप देखा कि स्वयंसेवक कैसे भक्तों की प्रार्थना में बाधा डाले बिना संगमरमर की सीढ़ियाँ झाड़ते हैं।", "mainne cupcāp dekhā ki svayaṃsevak kaise bhaktõ kī prārthanā mẽ bādhā ḍāle binā saṅgaramar kī sīḍhiyā̃ jhāṛte haiṃ."],
                ],
            ),
        ],
    )


def chapter_644() -> dict:
    return _l(
        "Lunch with a friend’s parents: compliments, helping serve, dietary preferences, and gratitude.",
        "Praise the cook modestly; offer to clear plates if hosts insist.",
        [
            _p("Courtesy", "बहुत स्वादिष्ट है — it is very delicious."),
            _t(
                "Friend's parents at lunch",
                [
                    ["Aunty, the aroma from your kitchen drew us in before we even rang the doorbell this afternoon.", "आंटी, आपकी रसोई की खुशबू ने दरवाज़े की घंटी बजाने से पहले ही हमें अंदर खींच लिया।", "ā̃ṭī, āpkī rasoī kī khuśabū ne darvāze kī ghaṇṭī bajāne se pahle hī hameṃ andar khīṃc liyā."],
                    ["Uncle, your stories about the old neighbourhood make this meal feel like a history lesson with dessert.", "अंकल, पुराने मोहल्ले की कहानियाँ इस भोजन को मिठाई के साथ इतिहास की कक्षा जैसा बना देती हैं।", "aṅkal, purāne mohalle kī kahāniā̃ is bhojan ko miṭhāī ke sāth itihās kī kakṣā jaise banā detī haiṃ."],
                    ["I eat everything, but I avoid very hot chillies; please do not worry about cooking extra mild dishes.", "मैं सब खा लेता हूँ, पर बहुत तीखी मिर्च से बचता हूँ; अतिरिक्त हल्की डिश बनाने की चिंता न करिए।", "main sab khā letā hū̃, par bahut tīkhī mirc se bactā hū̃; atirikt halkī ḍiś banāne kī cintā na karie."],
                    ["Your daughter mentioned you love gardening; these fresh coriander leaves taste like they were picked minutes ago.", "आपकी बेटी ने कहा था कि आप बागवानी पसंद करते हैं; ये ताज़ा धनिया पत्तियाँ ऐसी लगती हैं जैसे अभी तोड़ी हों।", "āpkī beṭī ne kahā thā ki āp bāgvānī pasand karte haiṃ; ye tāzā dhaniyā pattiyā̃ aisī lagtī haiṃ jaise abhī toṛī hoṃ."],
                    ["May I help carry the bowls to the table; my mother always taught me not to sit when elders are serving.", "क्या मैं कटोरे मेज़ तक ले जाऊँ; मेरी माँ ने हमेशा सिखाया कि बड़े परोसें तो बैठना नहीं चाहिए।", "kyā main kaṭore mez tak le jāū̃; merī mā̃ ne hameśā sikhāyā ki baṛe paroseṃ to baiṭhnā nahī̃ cāhie."],
                    ["The mango pickle is perfectly balanced; could you share whether you sun-dry the mangoes before jarring?", "आम का अचार बिल्कुल संतुलित है; क्या आप बता सकती हैं कि जार भरने से पहले आम धूप में सुखाती हैं?", "ām kā acār bilkul santulit hai; kyā āp batā saktī haiṃ ki jār bharne se pahle ām dhūp mẽ sukhātī haiṃ?"],
                    ["We discussed cricket only briefly because politics at the table can spoil digestion and mood.", "हमने क्रिकेट पर केवल संक्षेप में बात की क्योंकि मेज़ पर राजनीति पचन और मूड खराब कर सकती है।", "hamne krikeṭ par keval saṅkṣep mẽ bāt kī kyõki mez par rājnīti pacan aur mūḍ kharāb kar saktī hai."],
                    ["Your home feels peaceful because sunlight falls on the bookshelves exactly where your reading chair sits.", "आपका घर शांत लगता है क्योंकि धूप किताबों की अलमारी पर ठीक वहीं पड़ती है जहाँ कुर्सी है।", "āpkā ghar śānt lagtā hai kyõki dhūp kitābõ kī almārī par ṭhīk vahī̃ paṛtī hai jahā̃ kursī hai."],
                    ["I brought a small box of sweets from my hometown; it is nothing fancy, just a humble thank-you gesture.", "मैं अपने गाँव की मिठाई का छोटा डिब्बा लाया हूँ; कुछ खास नहीं, बस एक विनम्र धन्यवाद है।", "main apne gā̃v kī miṭhāī kā choṭā ḍibbā lāyā hū̃; kuch khās nahī̃, bas ek vinamra dhanyavād hai."],
                    ["Before leaving, I touched their feet because gratitude sometimes needs tradition more than fluent words.", "जाते समय मैंने उनके पैर छुए क्योंकि कृतज्ञता को कभी परंपरा शब्दों से ज़्यादा चाहिए।", "jāte samay mainne unke pair chhue kyõki kṛtajñatā ko kabhī paramparā śabdõ se zyādā cāhie."],
                    ["They packed leftover rotis for the driver without being asked, which showed kindness beyond hospitality.", "उन्होंने बिना कहे ड्राइवर के लिए बची रोटियाँ पैक कर दीं, जो मेहमाननवाज़ी से आगे की दया दिखाता है।", "unhoṃne binā kahe ḍrāivar ke lie bacī roṭiyā̃ pāk kar dī̃, jo mehmānnavāzī se āge kī dayā dikhātā hai."],
                    ["My friend whispered that her parents rarely praise cooking, so their smile today meant the world to her.", "मेरे दोस्त ने फुसफुसाया कि उनके माता-पिता कम ही खाना तारीफ़ करते हैं, इसलिए आज की मुस्कान उसके लिए सब कुछ थी।", "mere dost ne phusphusāyā ki un ke mātā-pitā kam hī khānā tārif karte haiṃ, islie āj kī muskurāṇ us ke lie sab kuch thī."],
                ],
            ),
        ],
    )


def chapter_645() -> dict:
    return _l(
        "Talking about a football match: goals, fouls, referees, and friendly rivalry.",
        "Use टीम, गोल, ऑफ़साइड as loanwords common in Hindi sports talk.",
        [
            _p("Match", "किसने गोल किया? — Who scored?"),
            _t(
                "Football match",
                [
                    ["That bicycle kick in the final minute was unreal; I jumped off the sofa and scared the sleeping cat.", "आख़िरी मिनट में वह बाइसिकल किक असली नहीं लग रही थी; मैं सोफ़े से उछल पड़ा और सोते बिल्ली डर गई।", "āxiri minaṭ mẽ vah bāisikal kick asalī nahī̃ lag rahī thī; main sofe se uchal paṛā aur sote billī ḍar gaī."],
                    ["The referee ignored a clear handball, and the entire stand started chanting in protest until the VAR review.", "रेफ़री ने साफ़ हैंडबॉल नज़रअंदाज़ किया और वीएआर रिव्यू तक पूरा स्टैंड विरोध में नारे लगाता रहा।", "refarī ne sāf haiṇḍbŏl nazarandāz kiyā aur vīār rivyū tak pūrā sṭaiṇḍ virodh mẽ nāre lagātā rahā."],
                    ["Our goalkeeper made three diving saves in a row, so even rival fans applauded before booing again.", "हमारे गोलकीपर ने लगातार तीन डाइविंग सेव किए, इसलिए प्रतिद्वंदी प्रशंसक भी फिर से बू करने से पहले तालियाँ बजा बैठे।", "hamāre golkīpar ne lagātār tīn ḍaiviṅg sev kie, islie pratidvandī praśaṃsak bhī phir se bū karne se pahle tāliyā̃ bajā baiṭhe."],
                    ["During halftime we argued whether the coach should substitute the tired midfielder with the young winger.", "हाफ़टाइम में हमने बहस की कि कोच को थके हुए मिडफ़ील्डर की जगह नए विंगर को उतारना चाहिए या नहीं।", "hāfṭāim mẽ hamne bahas kī ki koc ko thake hue miḍphīlar kī jagah nae viṅgar ko utārnā cāhie yā nahī̃."],
                    ["The offside trap worked perfectly because the defensive line stepped up in unison like trained soldiers.", "ऑफ़साइड ट्रैप इसलिए काम कर गया क्योंकि डिफ़ेंसिव लाइन प्रशिक्षित सैनिकों की तरह एक साथ आगे बढ़ी।", "ŏfsāiḍ ṭraip islie kām kar gayā kyõki ḍifenśiv lāin praśikṣit sainikõ kī tarah ek sāth āge baṛhī."],
                    ["My cousin blamed the pitch for slow passes, but I think anxiety made players rush simple triangles.", "कज़िन ने धीमे पास के लिए पिच को दोष दिया, पर मुझे लगता है घबराहट ने सरल त्रिभुज जल्दबाज़ बना दिए।", "kazin ne dhīme pās ke lie pic ko doṣ diyā, par mujhe lagtā hai ghabrāhaṭ ne saral tribhuj jaldabāz banā die."],
                    ["We replayed the slow-motion goal on the phone until the neighbour knocked complaining about the volume.", "हमने फोन पर स्लो-मोशन गोल तब तक दोहराया जब तक पड़ोसी ने आवाज़ की शिकायत कर दरवाज़ा खटखटाया।", "hamne phon par slo-mośan gol tab tak dohrāyā jab tak paṭosī ne āvāz kī śikāyat kar darvāzā khaṭkhaṭāyā."],
                    ["Fantasy league points aside, I admitted that the opponent’s striker deserved man of the match honestly.", "फ़ैंटेसी लीग के अंकों के अलावा, मैंने ईमानदारी से माना कि प्रतिद्वंदी स्ट्राइकर को मैन ऑफ़ द मैच मिलना चाहिए।", "faiṭesī līg ke aṅkõ ke alāvā, mainne īmāndārī se mānā ki pratidvandī sṭraikar ko main ŏf da mēc milnā cāhie."],
                    ["Stadium snacks were overpriced, yet sharing greasy fries somehow made the tense draw taste like victory.", "स्टेडियम का नाशता महँगा था, फिर भी तले हुए आलू साझा करने से ड्रॉ जीत जैसा लगा।", "sṭeḍiyam kā nāśtā mahṅgā thā, phir bhī tale hue ālū sājhā karne se ḍrŏ jīt jaise lagā."],
                    ["After the red card, ten men defended deep blocks, and every clearance felt like a moral victory.", "रेड कार्ड के बाद दस खिलाड़ियों ने गहरे ब्लॉक में बचाव किया और हर क्लीयरेंस नैतिक जीत लगी।", "reḍ kāḍ ke bād das khilāḍiyõ ne gahre blŏk mẽ bacāv kiyā aur har klīreṃs naitik jīt lagī."],
                    ["We promised to watch the next derby together even though today’s banter almost ruined a childhood friendship.", "हमने वादा किया कि अगला डर्बी साथ देखेंगे भले ही आज की चिढ़ ने बचपन की दोस्ती लगभग बिगाड़ दी हो।", "hamne vādā kiyā ki agalā ḍarbī sāth dekheṅge bhale hī āj kī chiṛ ne bacpan kī dostī lagabhag bigāṛ dī ho."],
                    ["Walking home, we analysed every substitution, proving that football debates never really end at the final whistle.", "घर लौटते हुए हमने हर प्रतिस्थापन का विश्लेषण किया, जिससे साबित हुआ कि फुटबॉल की बहस अंतिम सीटी पर खत्म नहीं होती।", "ghar lauṭte hue hamne har pratisthāpan kā viśleṣaṇ kiyā, jisse sābit huā ki phuṭbŏl kī bahas antim sīṭī par khatm nahī̃ hotī."],
                ],
            ),
        ],
    )


def chapter_646() -> dict:
    return _l(
        "Friends planning a movie: showtimes, seats, snacks, reviews, and transport home.",
        "Book tickets early for weekend openings; confirm भाषा (Hindi dub or original).",
        [
            _p("Plan", "कौन सी फ़िल्म देखें? — Which film shall we watch?"),
            _t(
                "Watch movie",
                [
                    ["The nine p.m. show is almost sold out, so if we want recliners we should book before the lunch break ends.", "रात नौ बजे का शो लगभग भर गया है, इसलिए रिक्लाइनर चाहिए तो दोपहर की छुट्टी खत्म होने से पहले बुक करें।", "rāt nau baje kā śo lagabhag bhar gayā hai, islie riklāinar cāhie to dopahar kī chuṭṭī khatm hone se pahle buk kareṃ."],
                    ["I read mixed reviews, but the cinematography alone is worth the ticket if we ignore the weak subplot.", "मैंने मिले-जुले समीक्षा पढ़ी हैं, पर यदि कमज़ोर उपकथा नज़रअंदाज़ करें तो सिनेमैटोग्राफी अकेले टिकट के लायक है।", "mainne mile-jule samīkṣā paṛhī haiṃ, par yadi kamzor upkathā nazarandāz kareṃ to sinemaiṭograiphī akele ṭikaṭ ke lāyak hai."],
                    ["Let us skip the front row unless we enjoy neck pain; middle seats balance sound and screen size better.", "आगे की पंक्ति छोड़ दें जब तक गर्दन दर्द पसंद न हो; बीच की सीटें आवाज़ और स्क्रीन का संतुलन बेहतर देती हैं।", "āge kī paṅkti choṛ deṃ jab tak gardan dard pasand na ho; bīc kī sīṭeṃ āvāz aur skrīn kā santulan behtar detī haiṃ."],
                    ["We can share a large popcorn and two drinks because theatre combos are cheaper than buying separately.", "हम बड़ा पॉपकॉर्न और दो पेय साझा कर सकते हैं क्योंकि थिएटर कॉम्बो अलग खरीदने से सस्ता पड़ता है।", "ham baṛā pŏpkŏrn aur do pey sājhā kar sakte haiṃ kyõki thieṭar kŏmbo alag kharīdne se sustā paṛtā hai."],
                    ["If the film runs three hours, we should choose an interval-friendly snack line before the rush at the stall.", "यदि फ़िल्म तीन घंटे चले तो भीड़ से पहले अंतराल वाली लाइन में नाशता चुन लेना चाहिए।", "yadi film tīn ghaṃṭe cale to bhīṛ se pahle antarāl vālī lāin mẽ nāśtā cun lenā cāhie."],
                    ["My friend refuses horror late at night, so we compromised on a courtroom drama with strong dialogue.", "मेरा दोस्त देर रात डरावनी फ़िल्म से मना करता है, इसलिए हमने तेज़ संवाद वाले अदालती नाटक पर सहमति जताई।", "merā dost der rāt ḍarāvanī film se manā kartā hai, islie hamne tez saṃvād vāle adālatī nāṭak par sahamti jatāī."],
                    ["Parking is chaos after Marvel releases, so I suggested metro plus auto to avoid circling basements.", "मार्वल रिलीज़ के बाद पार्किंग अफरातफरी होती है, इसलिए मैंने बेसमेंट चक्कर से बचने के लिए मेट्रो प्लस ऑटो सुझाया।", "mā rval rilīj ke bād pārkiṅg afrātafarī hotī hai, islie mainne besmeṭ cakkar se bacne ke lie meṭro plas ôṭo sujhāyā."],
                    ["We checked parental guidance warnings because my cousin brings his twelve-year-old brother along.", "हमने अभिभावकीय चेतावनी देखी क्योंकि मेरा कज़िन बारह साल के भाई को साथ लाता है।", "hamne abhibhāvakīy cetāvanī dekhī kyõki merā kazin bārah sāl ke bhāī ko sāth lātā hai."],
                    ["During the climax someone’s phone rang loudly, and the whole row shushed them until they switched it off.", "क्लाइमेक्स के दौरान किसी का फोन ज़ोर से बज उठा और पूरी पंक्ति ने चुप करवाया जब तक बंद न हुआ।", "klāimeks ke daurān kisī kā phon zor se baj uṭhā aur pūrī paṅkti ne cup karvāyā jab tak band na huā."],
                    ["Credits rolled longer than expected because of multiple production houses, so we listed everyone we recognised.", "क्रेडिट उम्मीद से लंबे चले क्योंकि कई प्रोडक्शन हाउस थे, इसलिए हमने पहचाने हुए नाम गिने।", "kreḍiṭ ummīd se laṃbe cale kyõki kaī proḍakśan hāus the, islie hamne pahcāne hue nām gine."],
                    ["Walking out, we argued whether the twist was clever or lazy, which is how you know the film sparked conversation.", "बाहर निकलकर हमने बहस की कि मोड़ चतुर था या आलसी, जो दिखाता है कि फ़िल्म ने चर्चा जगाई।", "bāhar nikal kar hamne bahas kī ki moṛ catur thā yā ālasī, jo dikhātā hai ki film ne carcā jagāī."],
                    ["We booked autos in advance because rain was forecast, and nobody wanted to debate endings in wet clothes.", "हमने पहले से ऑटो बुक किए क्योंकि बारिश का अनुमान था और कोई गीले कपड़ों में अंत पर बहस नहीं चाहता था।", "hamne pahle se ôṭo buk kie kyõki bāriś kā anumān thā aur koī gīle kapṛõ mẽ ant par bahas nahī̃ cāhtā thā."],
                ],
            ),
        ],
    )


def chapter_647() -> dict:
    return _l(
        "World Cup chatter: groups, upsets, VAR, and national pride without hostility.",
        "Keep banter light; remember fans feel deeply about their teams.",
        [
            _p("Cup", "कौन सेमीफाइनल में पहुँचा? — Who reached the semi-finals?"),
            _t(
                "Football World Cup",
                [
                    ["This World Cup keeps delivering upsets; yesterday’s favourite crashed out after a defensive blunder in extra time.", "इस विश्व कप में उलटफेर आते रहते हैं; कल का फ़ेवरेट अतिरिक्त समय में रक्षात्मक गलती से बाहर हो गया।", "is viśv kap mẽ ulṭapher āte rahte haiṃ; kal kā fevareṭ atirikt samay mẽ rakṣātmak galtī se bāhar ho gayā."],
                    ["The VAR decision took five minutes, and fans around us debated frame by frame like amateur detectives.", "वीएआर का फैसला पाँच मिनट ले गया और आसपास के प्रशंसक शौकिया जासूस की तरह फ्रेम पर बहस करते रहे।", "vīār kā faislā pā̃c minaṭ le gayā aur āspās ke praśaṃsak śaukīyā jāsūs kī tarah phrem par bahas karte rahe."],
                    ["Our café ran out of chairs, so kids sat on the floor waving flags while parents guarded plates of samosas.", "हमारे कैफ़े में कुर्सियाँ खत्म हो गईं, इसलिए बच्चे फर्श पर बैठकर झंडे लहराते रहे और माता-पिता समोसे संभालते रहे।", "hamāre kaife mẽ kursiyā̃ khatm ho gaī̃, islie bacce farś par baiṭh kar jhaṇḍe laharāte rahe aur mātā-pitā samose saṃbhālte rahe."],
                    ["I admire how smaller nations invest in youth academies instead of buying ageing superstars every season.", "मैं छोटे देशों की तारीफ़ करता हूँ जो हर सीज़न सुपरस्टार खरीदने के बजाय युवा अकादमियों में निवेश करते हैं।", "main choṭe deśõ kī tārif kartā hū̃ jo har sījan suparsṭār kharīdne ke bajāy yuvā akādāmiyõ mẽ niveś karte haiṃ."],
                    ["Penalty shootouts are cruel poetry; even excellent strikers walk back broken when the bar shakes.", "पेनल्टी शूटआउट क्रूर कविता है; बार हिलने पर बढ़िया स्ट्राइकर भी टूट कर लौटते हैं।", "penalṭī śūṭā'uṭ krūr kavitā hai; bār hilne par baṛhiyā sṭraikar bhī ṭūṭ kar lauṭte haiṃ."],
                    ["We compared jersey numbers with childhood heroes and realised nostalgia sometimes blinds tactical analysis.", "हमने बचपन के नायकों से जर्सी नंबर तुलना की और महसूस किया कि यादें कभी रणनीतिक विश्लेषण अँधेर देती हैं।", "hamne bacpan ke nāyakõ se jarsī nambar tulnā kī aur mahasūs kiyā ki yādeṃ kabhī raṇnītik viśleṣaṇ aṃdher detī haiṃ."],
                    ["Climate debates matter too because midday heat in desert stadiums drains players faster than statistics show.", "जलवायु पर चर्चा भी ज़रूरी है क्योंकि रेगिस्तानी स्टेडियमों की दोपहर की गर्मी आँकड़ों से तेज़ खिलाड़ियों को थका देती है।", "jalvāyu par carcā bhī zarūrī hai kyõki registānī sṭeḍiyamõ kī dopahar kī garmī ā̃kḍõ se tez khilāḍiyõ ko thakā detī hai."],
                    ["Commentators mixing Hindi and English phrases made the broadcast feel like our living-room chatter.", "टिप्पणीकारों ने हिन्दी-अंग्रेज़ी मिश्रण से प्रसारण को हमारे लिविंग रूम की बातचीत जैसा बना दिया।", "ippaṇīkārõ ne hindī-aṅgrezī miśraṇ se prasāraṇ ko hamāre liviṅg rūm kī bātcīt jaise banā diyā."],
                    ["When our team lost, we still clapped for fair play because bitterness ruins the joy of watching sport together.", "जब हमारी टीम हारी तो भी हमने निष्पक्ष खेल के लिए तालियाँ बजाईं क्योंकि कड़वाहट साथ खेल देखने की खुशी बिगाड़ देती है।", "jab hamārī ṭīm hārī to bhī hamne niṣpakṣ khel ke lie tāliyā̃ bajāī̃ kyõki kaṛvāhaṭ sāth khel dekhne kī khushī bigāṛ detī hai."],
                    ["We made a pact to watch the final regardless of who plays because rituals matter more than favourites.", "हमने वादा किया कि फ़ेवरेट से अधिक रिवाज़ मायने रखते हैं, इसलिए फाइनल जो भी खेले देखेंगे।", "hamne vādā kiyā ki fevareṭ se adhik rivāz māyne rakhte haiṃ, islie phāinal jo bhī khele dekheṅge."],
                    ["Street vendors sold plastic horns that annoyed neighbours, so we bought earplugs for the elderly downstairs.", "सड़क वालों ने प्लास्टिक के सींग बेचे जिनसे पड़ोसी परेशान हुए, इसलिए हमने नीचे बुज़ुर्गों के लिए कान की रूई ली।", "saṛak vāloṃ ne plāsṭik ke siṅg beche jinse paṭosī pareśān hue, islie hamne nīce buzurgõ ke lie kān kī rūī lī."],
                    ["After the trophy lift, fireworks lit the sky, and for a moment rivalry felt smaller than shared wonder.", "ट्रॉफी उठाने के बाद आतिशबाज़ी ने आसमान रोशन किया और एक पल के लिए प्रतिद्वंदिता आश्चर्य से छोटी लगी।", "ṭrŏfī uṭhāne ke bād ātiśbāzī ne āsmān rośan kiyā aur ek pal ke lie pratidvanditā āścarya se choṭī lagī."],
                ],
            ),
        ],
    )


def chapter_648() -> dict:
    return _l(
        "Tour guide with tourists: history, timing, safety, and memorable storytelling.",
        "Speak clearly; repeat facts; offer water breaks in heat.",
        [
            _p("Welcome", "स्वागत है — welcome."),
            _t(
                "Tour guide",
                [
                    ["Welcome to this fort built three centuries ago; please stay with the group because some ramparts have no railings.", "तीन सदी पुराने इस किले में आपका स्वागत है; कृपया समूह के साथ रहिए क्योंकि कुछ परकोटों पर रेलिंग नहीं है।", "tīn sadī purāne is kile mẽ āpkā svāgat hai; kripayā samūh ke sāth rahie kyõki kuch parakoṭõ par reliṅg nahī̃ hai."],
                    ["That carved pillar tells the story of a queen who funded wells during drought, not just battles and jewels.", "वह नक्काशीदार खंभा एक रानी की कहानी बताता है जिसने युद्ध और जवाहरात के साथ-साथ सूखे में कुएँ बनवाए।", "vah nakkāśīdār khambhā ek rānī kī kahānī batātā hai jisne yuddh aur javāharāt ke sāth-sāth sūkhe mẽ ku.eṃ banvā.e."],
                    ["We will pause for fifteen minutes near the lake so you can photograph reflections without rushing others.", "हम झील के पास पंद्रह मिनट रुकेंगे ताकि आप बिना दूसरों को धक्का दिए प्रतिबिंब की फोटो ले सकें।", "ham jhīl ke pās pandrah minaṭ rukeṃge tāki āp binā dūsarõ ko dhakkā die pratibimba kī phoṭo le sakeṃ."],
                    ["Please do not touch the murals; oils from skin darken pigments faster than centuries of sunlight did.", "कृपया भित्ति चित्रों को न छुएँ; त्वचा का तेल सदियों की धूप से तेज़ रंग गहरा कर देता है।", "kripayā bhitti citrõ ko na chueṃ; tvacā kā tel sadiyõ kī dhūp se tez raṅg gahrā kar detā hai."],
                    ["If you feel dizzy on the spiral stairs, signal me immediately; there is a shaded bench halfway down.", "यदि सर्पिल सीढ़ियों पर चक्कर आए तो तुरंत इशारा करिए; बीच में छायादार बेंच है।", "yadi sarpil sīḍhiyõ par cakkār ā.e to turant iśārā karie; bīc mẽ chāyādār beṃc hai."],
                    ["Local legend says this tunnel connects to the river, but archaeologists found it blocked after twenty metres.", "स्थानीय किंवदंती कहती है कि यह सुरंग नदी से जुड़ती है, पर पुरातत्वविदों ने बीस मीटर बाद बंद पाया।", "sthānīy kiṃvadantī kahtī hai ki yah suraṅg nadī se juṛtī hai, par purātattvavidõ ne bīs mīṭar bād band pāyā."],
                    ["We recommend trying the sweet lime juice sold outside Gate Two, but negotiate price politely like locals do.", "हम गेट दो के बाहर बिकने वाला मौसम्बी रस चखने की सलाह देते हैं, पर स्थानीयों की तरह विनम्रता से दाम तय करिए।", "ham geṭ do ke bāhar bikne vālā mausambī ras cakhne kī salāh dete haiṃ, par sthānīyõ kī tarah vinamratā se dām tay karie."],
                    ["That bell weighs two tons, yet monks still ring it during festivals using wooden beams as counterweights.", "वह घंटा दो टन का है, फिर भी त्योहारों में भिक्षु लकड़ी की शाफ्ट से प्रतिभार के रूप में बजाते हैं।", "vah ghaṇṭā do ṭan kā hai, phir bhī tyohārõ mẽ bhikṣu lakaṛī kī śāphṭ se pratibhār ke rūp mẽ bajāte haiṃ."],
                    ["Photography drones are banned here because nesting birds panic when shadows sweep across fragile eggs.", "यहाँ ड्रोन से फोटोग्राफी मना है क्योंकि घोंसले में परछाईं अंडों पर पड़ने पर पक्षी घबरा जाते हैं।", "yahā̃ ḍron se phoṭogrāphī manā hai kyõki ghoṃsale mẽ parcchāiā̃ aṇḍõ par paṛne par pakṣī ghabarā jāte haiṃ."],
                    ["I will share a playlist of classical ragas inspired by this region so the drive back feels connected to history.", "मैं इस क्षेत्र से प्रेरित शास्त्रीय रागों की प्लेलिस्ट साझा करूँगा ताकि वापसी का सफ़र इतिहास से जुड़ा लगे।", "main is kṣetra se prerit śāstrīy rāgõ kī plelisṭ sājhā karū̃gā tāki vāpasī kā safar itihās se juṛā lage."],
                    ["Tip guides only if you loved the tour, but a sincere review online helps small operators survive slow seasons.", "यदि दौरा पसंद आए तो गाइड को टिप दें, पर ऑनलाइन ईमानदार समीक्षा छोटे संचालकों को धीमे सीज़न में बचाती है।", "yadi daurā pasand ā.e to gāiḍ ko ṭip deṃ, par ônlāin īmāndār samīkṣā choṭe saṃcālakõ ko dhīme sījan mẽ bachātī hai."],
                    ["Before we leave, remember that respectful silence in sacred corners honours people who prayed here for generations.", "जाने से पहले याद रखिए कि पवित्र कोनों में शांत विनम्रता उन लोगों का सम्मान है जो पीढ़ियों से यहाँ प्रार्थना करते आए।", "jāne se pahle yād rakhie ki pavitra konõ mẽ śānt vinamratā un logõ kā sammān hai jo pīḍhiyõ se yahā̃ prārthanā karte ā.e."],
                ],
            ),
        ],
    )


def chapter_649() -> dict:
    return _l(
        "Bank language proficiency: formal register, précis, letter writing, and comprehension practice.",
        "Use complete sentences in interviews; avoid excessive English mixing unless quoting policy.",
        [
            _p("Formal", "मैं समझ गया — I understood (formal acknowledgment)."),
            _t(
                "Language test (banks)",
                [
                    ["Please summarise this RBI circular in your own words within one hundred and fifty words on this sheet.", "कृपया इस आरबीआई परिपत्र को अपने शब्दों में एक सौ पचास शब्दों में संक्षेप में लिखिए।", "kripayā is ārabīāī paripatra ko apne śabdõ mẽ ek sau pacās śabdõ mẽ saṅkṣep mẽ likhie."],
                    ["Translate the following English paragraph into formal Hindi suitable for a customer notice board.", "निम्नलिखित अंग्रेज़ी अनुच्छेद का ग्राहक सूचना बोर्ड के लिए उपयुक्त औपचारिक हिन्दी में अनुवाद कीजिए।", "nimnalikhit aṅrezī anucched kā grāhak sūcnā borḍ ke lie upayukt aupacārik hindī mẽ anuvād kījie."],
                    ["Identify the grammatical errors in this Hindi sentence and rewrite it maintaining the original meaning.", "इस हिन्दी वाक्य में व्याकरण की गलतियाँ पहचानकर मूल अर्थ बनाए रखते हुए पुनः लिखिए।", "is hindī vāky mẽ vyākaraṇ kī galatiyā̃ pahcān kar mūl arth banā.e rakhte hue punar likhie."],
                    ["Compose a polite letter to a branch manager requesting a duplicate passbook after loss during relocation.", "शाखा प्रबंधक को पत्र लिखिए जिसमें स्थानांतरण के दौरान खोए पासबुक की प्रतिलिपि का विनम्र अनुरोध हो।", "śākhā prabaṅdhak ko patr likhie jismeṃ sthānāntaraṇ ke dūrān kho.e pāsabuk kī pratilipi kā vinamra anurodh ho."],
                    ["Read this comprehension passage about financial inclusion and answer five objective questions that follow.", "वित्तीय समावेशन पर यह गद्यांश पढ़कर आने वाले पाँच वस्तुनिष्ठ प्रश्नों के उत्तर दीजिए।", "vittīy samāveśan par yah gadyāṃś paṛh kar āne vāle pā̃c vastuniṣṭ praśnõ ke uttar dījie."],
                    ["Explain the difference between recurring deposit and fixed deposit in simple Hindi for a rural customer.", "ग्रामीण ग्राहक के लिए आवर्ती जमा और सावधि जमा के बीच अंतर सरल हिन्दी में समझाइए।", "grāmīṇ grāhak ke lie āvartī jamā aur sāvdhi jamā ke bīc antar saral hindī mẽ samjhāie."],
                    ["During the oral test, speak slowly about your hometown’s economy and how banking services reached farmers.", "मौखिक परीक्षा में अपने गृहनगर की अर्थव्यवस्था और किसानों तक बैंकिंग सेवाएँ कैसे पहुँचीं, धीरे बताइए।", "maukhik parīkṣā mẽ apne gṛhanagar kī arthavyavasthā aur kisānõ tak baiṅkiṅg sevāeṃ kaise pahuṃcī̃, dhīre batāie."],
                    ["Proofread this Hindi press release for gender agreement errors before we upload it to the intranet.", "इंट्रानेट पर अपलोड करने से पहले इस हिन्दी प्रेस विज्ञप्ति में लिंग-सहमति की गलतियाँ ठीक कीजिए।", "iṭrāneṭ par aploaḍ karne se pahle is hindī pres vigyapti mẽ liṅg-sahmati kī galatiyā̃ ṭhīk kījie."],
                    ["Discuss in Hindi how digital payments reduce cash handling risk for small merchants near highways.", "हिन्दी में चर्चा कीजिए कि डिजिटल भुगतान राजमार्ग के पास छोटे व्यापारियों के लिए नकद जोखिम कैसे कम करता है।", "hindī mẽ carcā kījie ki ḍijiṭal bhugtān rājmārg ke pās choṭe vyāpāriyõ ke lie nakad jokhim kaise kam kartā hai."],
                    ["Memorise these five banking abbreviations and use each in a separate sentence demonstrating correct context.", "इन पाँच बैंकिंग संक्षिप्ताक्षरों को याद करके प्रत्येक को अलग वाक्य में सही संदर्भ में प्रयोग कीजिए।", "in pā̃c baiṅkiṅg saṅkṣiptākṣarõ ko yād kar ke pratyek ko alag vāky mẽ sahī sandarbh mẽ prayog kījie."],
                    ["Write a dialogue between a loan officer and a farmer seeking a tractor loan under a government scheme.", "सरकारी योजना के तहत ट्रैक्टर ऋण चाहने वाले किसान और ऋण अधिकारी के बीच संवाद लिखिए।", "sarkārī yojanā ke tahat ṭraikṭar ṛiṇ cāhne vāle kisān aur ṛiṇ adhikārī ke bīc saṃvād likhie."],
                    ["Conclude your essay on financial literacy by urging readers to verify official URLs before sharing OTPs.", "वित्तीय साक्षरता पर निबंध का समापन पाठकों से यह कहकर करें कि ओटीपी साझा करने से पहले आधिकारिक यूआरएल जाँचें।", "vittīy sākṣartā par nibandh kā samāpan pāṭhakõ se yah kah kar kareṃ ki oṭīpī sājhā karne se pahle adhikārik yūārel jā̃ceṃ."],
                ],
            ),
        ],
    )


def chapter_650() -> dict:
    return _l(
        "Food, lunch, and meals: preferences, portions, hosting, and dietary notes.",
        "Say मुझे मीठा कम पसंद है if you prefer less sugar.",
        [
            _p("Host", "कृपया बैठकर खाइए — please sit and eat."),
            _t(
                "Food & meals",
                [
                    ["Lunch today is simple dal, rice, seasonal vegetables, and roasted papad, but seconds are always welcome here.", "आज दोपहर का खाना सादी दाल, चावल, मौसमी सब्ज़ी और भुना पापड़ है, पर यहाँ दोबारा लेना हमेशा स्वागत है।", "āj dopahar kā khānā sādī dāl, cāval, mausamī sabzī aur bhunā pāpaṛ hai, par yahā̃ dobārā lenā hameśā svāgat hai."],
                    ["I avoid gluten, so if the rotis are wheat-based, kindly point me toward rice or millet options.", "मैं ग्लूटेन से बचता हूँ, इसलिए यदि रोटियाँ गेहूँ की हैं तो चावल या बाजरे के विकल्प दिखा दीजिए।", "main glūṭen se bactā hū̃, islie yadi roṭiyā̃ gehū̃ kī haiṃ to cāval yā bājre ke vikalp dikhā dījie."],
                    ["She packed tiffin for the office with layered salads so crunch stays crisp until one o’clock.", "उसने ऑफिस के लिए परतदार सलाद वाला टिफ़िन पैक किया ताकि एक बजे तक कुरकुरापन बना रहे।", "usne ôphis ke lie paratadār salād vālā ṭifin pāk kiyā tāki ek baje tak kurakurāpan banā rahe."],
                    ["Street food smells tempting, yet we chose a sit-down thali because hygiene mattered more than novelty.", "सड़क का खाना लुभाता है, फिर भी हमने बैठकर थाली चुनी क्योंकि स्वच्छता नएपन से ज़्यादा ज़रूरी थी।", "saṛak kā khānā lubhātā hai, phir bhī hamne baiṭh kar thālī cunī kyõki svacchatā nae pan se zyādā zarūrī thī."],
                    ["Grandmother insists we finish curd after meals for digestion, even when we are already full.", "दादी ज़ोर देती हैं कि भोजन के बाद दही ज़रूर खत्म करें, भले ही पेट भरा हो।", "dādī zor detī haiṃ ki bhojan ke bād dahī zarūr khatm kareṃ, bhale hī peṭ bharā ho."],
                    ["The potluck theme was regional breads, so we brought bhakri while others carried litti and appam.", "पॉटलक का विषय क्षेत्रीय ब्रेड था, इसलिए हम भाकरी लाए जबकि दूसरे लिट्टी और अप्पम लाए।", "pŏṭlak kā viṣay kṣetrīy breḍ thā, islie ham bhākrī lā.e jabaki dūśre liṭṭī aur appam lā.e."],
                    ["After spicy curry, chilled buttermilk soothed our throats better than any sugary soda from the fridge.", "तीखी करी के बाद ठंडी छाछ ने गले को शर्करा वाले सोडा से बेहतर शांत किया।", "tīkhī karī ke bād thaṃḍī chāch ne gale ko śarkarā vāle soḍā se behtar śānt kiyā."],
                    ["We debated whether pineapple belongs on pizza while folding slices, which proves food arguments never end.", "हमने पिज़्ज़ा पर अनानास होना चाहिए या नहीं, इस पर बहस की, जो दिखाता है खाने की बहसें कभी खत्म नहीं होतीं।", "hamne pijjā par anānās honā cāhie yā nahī̃, is par bahas kī, jo dikhātā hai khāne kī bahseṃ kabhī khatm nahī̃ hotī̃."],
                    ["Meal prep on Sunday saves weekday stress, so we chopped vegetables while listening to old film songs.", "रविवार का मील प्रेप कार्यदिवस की तनाव बचाता है, इसलिए हमने पुराने फ़िल्मी गाने सुनते हुए सब्ज़ी काटी।", "ravivār kā mīl prep kārydivas kī tanāv bachātā hai, islie hamne purāne filmī gāne sunte hue sabzī kāṭī."],
                    ["When guests cancelled last minute, we donated the extra curry to the shelter instead of wasting it.", "जब मेहमान अंतिम समय पर रद्द हुए तो हमने अतिरिक्त करी आश्रय में दान कर दी बजाय फेंकने के।", "jab mehmān antim samay par radd hue to hamne atirikt karī āśray mẽ dān kar dī bajāy pheṅkne ke."],
                    ["Hydration reminders buzz on smartwatches, yet nothing beats a steel bottle filled with lemon water.", "स्मार्टवॉच पर हाइड्रेशन रिमाइंडर बजते हैं, फिर भी नींबू पानी से भरी स्टील की बोतल से बेहतर कुछ नहीं।", "smārṭvāc par hāiḍreśan rimaiṇḍar bajte haiṃ, phir bhī nī̃bū pānī se bharī sṭīl kī botal se behtar kuch nahī̃."],
                    ["Cooking together taught us patience because chopping onions slowly hurts less than rushing with dull knives.", "साथ खाना बनाने ने धैर्य सिखाया क्योंकि धीरे प्याज़ काटना कुंद चाकू से जल्दी काटने से कम दर्द देता है।", "sāth khānā banāne ne dhairya sikhāyā kyõki dhīre pyāz kāṭnā kund cākū se jaldī kāṭne se kam dard detā hai."],
                ],
            ),
        ],
    )


def chapter_651() -> dict:
    return _l(
        "Hobby classes: music, art, dance, scheduling fees, and practice at home.",
        "Ask शुल्क कब जमा करना है for fee deadlines.",
        [
            _p("Class", "अगला पाठ कब है? — When is the next lesson?"),
            _t(
                "Hobby class",
                [
                    ["Guruji, may I record today’s tabla lesson on my phone so I can practise the theka slowly at home?", "गुरुजी, क्या मैं आज का तबला पाठ फोन पर रिकॉर्ड कर लूँ ताकि घर पर ठेका धीरे अभ्यास कर सकूँ?", "gurujī, kyā main āj kā tablā pāṭh phon par rikŏrḍ kar lū̃ tāki ghar par ṭhekā dhīre abhyās kar sakū̃?"],
                    ["The art teacher asked us to bring textured paper because charcoal behaves differently on smooth sheets.", "कला शिक्षक ने टेक्सचर्ड पेपर लाने को कहा क्योंकि चारकोल चिकनी शीट पर अलग व्यवहार करता है।", "kalā śikṣak ne ṭeksacaṛḍ pepar lāne ko kahā kyõki cārakol ciknī śīṭ par alag vyavahār kartā hai."],
                    ["Bharatanatyam class starts with warm-up jumps, so please wear clothes that allow deep knee bends.", "भरतनाट्यम की कक्षा गर्मजोशी से शुरू होती है, इसलिए गहरे घुटने मोड़ने वाले कपड़े पहनिए।", "bharatanāṭyam kī kakṣā garmajośī se śurū hotī hai, islie gahre ghuṭne moṛne vāle kapṛe pahanie."],
                    ["My guitar string snapped mid-chord, but the instructor smiled and said mistakes teach ear training faster.", "गिटार की तार अचानक टूट गई, पर शिक्षक मुस्कुराए और बोले कि गलती कान की ट्रेनिंग तेज़ करती है।", "giṭār kī tār acānak ṭūṭ gaī, par śikṣak muskurā.e aur bole ki galtī kān kī ṭreṇiṅg tez kartī hai."],
                    ["We split the workshop fee because group discounts made pottery wheels affordable for students.", "हमने कार्यशाला शुल्क बाँटा क्योंकि समूह छूट ने छात्रों के लिए पॉटरी व्हील सस्ता कर दिया।", "hamne kāryaśālā śulk bāṭā kyõki samūh chūṭ ne chātrõ ke lie pŏṭarī vhīl sustā kar diyā."],
                    ["Photography assignments require sunrise shoots, so I set alarms even on Sundays when laziness whispers.", "फोटोग्राफी असाइनमेंट के लिए सूर्योदय शूट चाहिए, इसलिए आलस कहे तब भी रविवार को अलार्म लगाता हूँ।", "phoṭograiphī asāinameṇṭ ke lie sūryoday śūṭ cāhie, islie ālas kahe tab bhī ravivār ko alārm lagātā hū̃."],
                    ["The yoga instructor reminded us that breath matters more than bending deeper than the neighbour.", "योग शिक्षक ने याद दिलाया कि पड़ोसी से ज़्यादा मोड़ने से ज़्यादा श्वास मायने रखता है।", "yog śikṣak ne yād dilāyā ki paṭosī se zyādā moṛne se zyādā śvās māyne rakhtā hai."],
                    ["Kids’ drama class builds confidence; my niece now speaks on stage without clutching her mother’s sleeve.", "बच्चों का नाटक वर्ग आत्मविश्वास बनाता है; मेरी भतीजी अब माँ की बाँह पकड़े बिना मंच पर बोलती है।", "baccõ kā nāṭak varg ātmaviśvās banātā hai; merī batījī ab mā̃ kī bā̃h pakṛe binā mañc par boltī hai."],
                    ["Cooking workshops taught knife skills, yet I still bandage minor cuts because enthusiasm exceeds caution sometimes.", "खाना पकाने की कार्यशाला ने चाकू कौशल सिखाया, फिर भी उत्साह सावधानी से आगे निकल जाता है।", "khānā pakāne kī kāryaśālā ne cākū kauśal sikhāyā, phir bhī utsāh sāvdhānī se āge nikal jātā hai."],
                    ["Language exchange partners meet weekly at the library café to correct each other’s pronunciation gently.", "भाषा विनिमय साथी हर हफ़्ते लाइब्रेरी कैफ़े में मिलकर एक-दूसरे के उच्चारण को नरमी से सुधारते हैं।", "bhāṣā vinimay sāthī har hafte lāibrerī kaife mẽ milkar ek-dūsre ke uccāraṇ ko naramī se sudhārte haiṃ."],
                    ["If you miss two consecutive classes, the slot may go to waitlisted students, so inform the coordinator early.", "यदि लगातार दो कक्षाएँ छूटें तो स्लॉट वेटलिस्ट वालों को मिल सकता है, इसलिए समन्वयक को जल्द सूचित करें।", "yadi lagātār do kakṣāeṃ chūṭeṃ to sloṭ veṭlisṭ vālõ ko mil saktā hai, islie samanvayak ko jald sūcit kareṃ."],
                    ["Graduation recital invitations went digital, yet elders still appreciate a handwritten note with a pressed flower.", "ग्रेजुएशन रिसाइटल के निमंत्रण डिजिटल गए, फिर भी बुज़ुर्ग दबे फूल वाला हस्तलिखित नोट पसंद करते हैं।", "grejueśan risaiṭal ke nimaṃtraṇ ḍijiṭal ga.e, phir bhī buzurg dabe phūl vālā hastlikhit noṭ pasand karte haiṃ."],
                ],
            ),
        ],
    )


def chapter_652() -> dict:
    return _l(
        "Miscellaneous useful sentences for travel, shopping, apologies, and small talk.",
        "These lines work in many situations; adapt names and numbers as needed.",
        [
            _p("Utility", "मुझे मदद चाहिए — I need help."),
            _t(
                "Miscellaneous sentences",
                [
                    ["I am lost; could you point me toward the nearest metro station without using complicated directions?", "मैं रास्ता भटक गया हूँ; क्या आप बिना उलझाऊ दिशा के निकटतम मेट्रो स्टेशन की ओर इशारा कर सकते हैं?", "main rāstā bhaṭak gayā hū̃; kyā āp binā uljhāū diśā ke nikatatam meṭro sṭeśan kī or iśārā kar sakte haiṃ?"],
                    ["My phone battery died; may I borrow your charger for ten minutes if you have a compatible cable?", "मेरे फोन की बैटरी खत्म हो गई; क्या मैं दस मिनट के लिए आपका चार्जर उधार ले सकता हूँ यदि केबल मेल खाती हो?", "mere phon kī baiṭarī khatm ho gaī; kyā main das minaṭ ke lie āpkā cārjar udhār le saktā hū̃ yadi kebal mel khātī ho?"],
                    ["Could you speak a little slower; I understand Hindi but fast speech in crowds still overwhelms me.", "क्या आप थोड़ा धीरे बोल सकते हैं; मैं हिन्दी समझता हूँ पर भीड़ में तेज़ बोल अभी भी मुझे घबरा देता है।", "kyā āp thoṛā dhīre bol sakte haiṃ; main hindī samajhtā hū̃ par bhīṛ mẽ tez bol abhī bhī mujhe ghabarā detā hai."],
                    ["I sincerely apologise for the delay; the auto driver took a longer route than Google Maps suggested.", "मैं देरी के लिए ईमानदारी से माफ़ी चाहता हूँ; ऑटो ड्राइवर ने गूगल मैप से लंबा रास्ता लिया।", "main derī ke lie īmāndārī se māfī cāhtā hū̃; ôṭo ḍrāivar ne gūgal māp se laṃbā rāstā liyā."],
                    ["Is there an English menu, or could you recommend one mild vegetarian thali without nuts?", "क्या अंग्रेज़ी मेन्यू है, या आप बिना मेवे वाली एक हल्की शाकाहारी थाली सुझा सकते हैं?", "kyā aṅrezī menū hai, yā āp bina meve vālī ek halkī śākāhārī thālī sujhā sakte haiṃ?"],
                    ["We need two umbrellas because the forecast suddenly changed from sunshine to heavy showers.", "हमें दो छाते चाहिए क्योंकि पूर्वानुमान अचानक धूप से भारी बौछार में बदल गया।", "hameṃ do chāte cāhie kyõki pūrvānumān acānak dhūp se bhārī bauchhār mẽ badal gayā."],
                    ["Could you keep an eye on my bag while I use the washroom; I will not be more than five minutes.", "क्या आप वॉशरूम जाते समय मेरे बैग पर नज़र रख सकते हैं; मैं पाँच मिनट से ज़्यादा नहीं लूँगा।", "kyā āp vŏśrūm jāte samay mere baig par nazar rakh sakte haiṃ; main pā̃c minaṭ se zyādā nahī̃ lū̃gā."],
                    ["I would like to return this shirt because the seam tore after the first wash at home.", "मैं यह शर्ट वापस करना चाहता हूँ क्योंकि घर पर पहली धुलाई के बाद सिलाई फट गई।", "main yah śarṭ vāpas karnā cāhtā hū̃ kyõki ghar par pahlī dhulāī ke bād silāī phaṭ gaī."],
                    ["Please call a doctor if the pain worsens; I will stay nearby and translate what you need.", "यदि दर्द बढ़े तो डॉक्टर को बुला लीजिए; मैं पास रहूँगा और ज़रूरत का अनुवाद करूँगा।", "yadi dard baṛhe to ḍokṭar ko bulā lijie; main pās rahū̃gā aur zarūrat kā anuvād karū̃gā."],
                    ["The Wi-Fi password is on the fridge magnet, but the router restarts every hour for some reason.", "वाई-फ़ाई का पासवर्ड फ्रिज मैग्नेट पर है, पर राउटर किसी कारण हर घंटे रीस्टार्ट होता है।", "vāī-fāī kā pāsavarḍ phrij maineṭ par hai, par rāuṭar kisī kāraṇ har ghaṃṭā rīsṭārṭ hotā hai."],
                    ["We enjoyed the concert, though traffic afterward meant we reached home closer to midnight than planned.", "हमें संगीत समारोह पसंद आया, फिर भी बाद की ट्रैफ़िक से हम योजना से आधी रात के करीब घर पहुँचे।", "hameṃ saṅgīt samāroh pasand āyā, phir bhī bād kī ṭraifik se ham yojanā se ādhī rāt ke qarīb ghar pahuṃce."],
                    ["Let us exchange numbers in case plans change; I promise I will not forward random memes at three a.m.", "योजना बदले तो नंबर साझा कर लेते हैं; मैं वादा करता हूँ कि तीन बजे रात को बेवजह मीम नहीं भेजूँगा।", "yojanā badle to nambar sājhā kar lete haiṃ; main vādā kartā hū̃ kī tīn baje rāt ko bevajah mīm nahī̃ bhejū̃gā."],
                ],
            ),
        ],
    )


def chapter_653() -> dict:
    return _l(
        "More miscellaneous lines: complaints, compliments, scheduling, and polite exits.",
        "Pair with a smile; tone matters as much as words.",
        [
            _p("Polite exit", "मुझे जाना होगा — I will have to go."),
            _t(
                "Miscellaneous part 2",
                [
                    ["The music is too loud for my infant; could the restaurant lower the volume near our table?", "मेरे शिशु के लिए संगीत बहुत ज़ोर से बज रहा है; क्या रेस्तरां हमारी मेज़ के पास आवाज़ कम कर सकता है?", "mere śiśu ke lie saṅgīt bahut zor se baj rahā hai; kyā restarā̃ hamārī mez ke pās āvāz kam kar saktā hai?"],
                    ["I appreciate your honesty about the delivery delay; a clear timeline helps me plan my evening better.", "डिलीवरी में देरी के बारे में आपकी ईमानदारी की सराहना करता हूँ; स्पष्ट समय रेखा से शाम की योजना बनती है।", "ḍilīvarī mẽ derī ke bāre mẽ āpkī īmāndārī kī sarāhnā kartā hū̃; spaṣṭ samay rekhā se śām kī yojanā bantī hai."],
                    ["Could we reschedule the meeting to Tuesday because my child has a school function on Monday?", "क्या हम मीटिंग सोमवार से मंगलवार पर टाल सकते हैं क्योंकि मेरे बच्चे का स्कूल समारोह सोमवार को है?", "kyā ham mīṭiṅ somvār se maṅgalvār par ṭāl sakte haiṃ kyõki mere bacc kā skūl samāroh somvār ko hai?"],
                    ["Your presentation was crisp, yet I have two clarifying questions about the budget assumptions on slide nine.", "आपका प्रस्तुति सटीक थी, फिर भी स्लाइड नौ पर बजट अनुमानों के बारे में दो स्पष्टीकरण प्रश्न हैं।", "āpkā prastuti saṭīk thī, phir bhī slāiḍ nau par buj̤ anumānõ ke bāre mẽ do spaṣṭīkaraṇ praśn haiṃ."],
                    ["I do not mind waiting if you notify me every fifteen minutes instead of leaving me guessing near the counter.", "अगर आप पंद्रह-पंद्रह मिनट में सूचित करते रहें तो काउंटर के पास अटकल लगाने से बेहतर इंतज़ार है।", "agar āp pandrah-pandrah minaṭ mẽ sūcit karte raheṃ to kauṇṭar ke pās aṭakal lagāne se behtar intazār hai."],
                    ["Kindly email the receipt because I need it for reimbursement and our finance team rejects blurry photos.", "कृपया रसीद ईमेल करें क्योंकि मुझे प्रतिपूर्ति चाहिए और वित्त टीम धुंधली फोटो अस्वीकार करती है।", "kripayā rasīd īmel kareṃ kyõki mujhe pratipūrti cāhie aur vitt ṭīm dhundhlī phoṭo asvikār kartī hai."],
                    ["The room smells of paint; could housekeeping air it out before we unpack clothes for the wedding?", "कमरे में पेंट की गंध है; क्या हाउसकीपिंग शादी के कपड़े निकालने से पहले हवा कर दे?", "kamre mẽ peṇṭ kī gandh hai; kyā hāuskīpiṅ śādī ke kapṛe nikālne se pahle havā kar de?"],
                    ["I loved your city’s street art, but please warn tourists about pickpockets near crowded selfie spots.", "मुझे आपके शहर की सड़क कला पसंद आई, पर भीड़ वाली सेल्फी जगहों पर जेबकतरों के बारे में पर्यटकों को चेतावनी दें।", "mujhe āp ke śahar kī saṛak kalā pasand āī, par bhīṛ vālī selfī jagahõ par jebkatrõ ke bāre mẽ paryaṭakõ ko cetāvanī deṃ."],
                    ["Let us split the bill equally unless someone ordered alcohol separately; transparency keeps friendships healthy.", "बिल बराबर बाँट लेते हैं जब तक किसी ने अलग शराब न मँगाई हो; पारदारिता दोस्ती स्वस्थ रखती है।", "bil barābar bāṭ lete haiṃ jab tak kisī ne alag śarāb na maṅgāī ho; pāradāritā dostī svasth rakhtī hai."],
                    ["I will follow up next week with a summary email so everyone remembers the action items we agreed on.", "अगले हफ़्ते सारांश ईमेल से फॉलो अप करूँगा ताकि सबको सहमत कार्य याद रहें।", "agale hafte sāraṃś īmel se phŏlo ap karū̃gā tāki sabko sahamat kāry yād raheṃ."],
                    ["Thank you for offering dessert, but I am genuinely full; a cup of hot tea would be perfect instead.", "मिठाई देने के लिए धन्यवाद, पर मैं सचमुच भरा हूँ; इसके बजाय गर्म चाय परफेक्ट रहेगी।", "miṭhāī dene ke lie dhanyavād, par main sacamuc bharā hū̃; is ke bajāy garm cāy parphekṭ rahegī."],
                    ["Walking you to the door is the least I can do after you helped me rehearse my speech until midnight.", "आपने मेरा भाषण आधी रात तक रिहर्स करवाया, इसलिए दरवाज़े तक छोड़ना तो कम से कम बनता है।", "āpne merā bhāṣaṇ ādhī rāt tak rihars karvāyā, islie darvāze tak choṛnā to kam se kam bantā hai."],
                ],
            ),
        ],
    )


def chapter_654() -> dict:
    return _l(
        "Communicative approach: use Hindi for real tasks—ordering, asking, fixing misunderstandings.",
        "Mistakes are data; repeat, reformulate, and gesture when words fail.",
        [
            _p("Loop", "क्या मैं सही समझा? — Did I understand correctly?"),
            _t(
                "Communicative approach",
                [
                    ["Instead of memorising isolated words, I label objects in my room and say short sentences about them aloud.", "अकेले शब्द याद करने के बजाय मैं कमरे की चीज़ों पर लेबल लगाकर उनके बारे में ज़ोर से छोटे वाक्य बोलता हूँ।", "akele śabd yād karne ke bajāy main kamre kī cīzõ par lebal lagā kar unk e bāre mẽ zor se choṭe vākya boltā hū̃."],
                    ["When a shopkeeper replies too fast, I politely say, “Please repeat once,” instead of pretending I understood.", "जब दुकानदार बहुत तेज़ जवाब दे तो मैं नाटक करने के बजाय विनम्रता से कहता हूँ, “कृपया एक बार दोहराइए।”", "jab dukāndār bahut tez javāb de to main nāṭak karne ke bajāy vinamratā se kahtā hū̃, “kripayā ek bār dohrāie.”"],
                    ["Role-play with a friend lets me practise refusing pushy salespeople without sounding rude or timid.", "दोस्त के साथ रोल-प्ले से मैं ज़बरदस्ती बेचने वालों को बिना कठोर या डरे हुए मना करना सीखता हूँ।", "dost ke sāth rol-ple se main zabardastī becne vālõ ko binā kaṭhor yā ḍare hue manā karnā sīkhtā hū̃."],
                    ["I record myself answering common questions, then compare my pronunciation with slow news anchors on radio.", "मैं सामान्य सवालों के जवाब रिकॉर्ड करता हूँ, फिर रेडियो पर धीरे बोलने वाले समाचार वाचकों से उच्चारण तुलना करता हूँ।", "main sāmānya savālõ ke javāb rikŏrḍ kartā hū̃, phir reḍiyo par dhīre bolne vāle samācār vācakõ se uccāraṇ tulnā kartā hū̃."],
                    ["Watching Hindi shows with subtitles first, then without, trains my ear for colloquial contractions.", "पहले उपशीर्षक के साथ फिर बिना हिन्दी शो देखने से कान को बोलचाल के संकुचन की आदत पड़ती है।", "pahle upaśīrṣak ke sāth phir binā hindī śo dekhne se kān ko bolcāl ke saṅkucan kī ādat paṛtī hai."],
                    ["I keep a pocket notebook for phrases I hear on buses because authentic lines beat textbook examples sometimes.", "बस में सुने वाक्यों के लिए मैं जेब की नोटबुक रखता हूँ क्योंकि असली पंक्तियाँ कभी पाठ्यपुस्तक से आगे होती हैं।", "bas mẽ sune vākyõ ke lie main jeb kī noṭbuk rakhtā hū̃ kyõki aslī paṅktiyā̃ kabhī pāṭhyapustak se āge hotī haiṃ."],
                    ["Pairing grammar drills with storytelling means I actually use new tenses while describing my day.", "व्याकरण अभ्यास को कहानी से जोड़ने का मतलब है कि मैं अपने दिन का वर्णन करते नए काल का उपयोग करता हूँ।", "vyākaraṇ abhyās ko kahānī se joṛne kā matalab hai ki main apne din kā varṇan karte nae kāl kā upayog kartā hū̃."],
                    ["Language exchanges work best when both partners agree on time limits so fatigue does not kill motivation.", "भाषा विनिमय तब सर्वोत्तम है जब दोनों साथी समय सीमा तय करें ताकि थकावट प्रेरणा न मार दे।", "bhāṣā vinimay tab sarvottam hai jab donõ sāthī samay sīmā tay kareṃ tāki thakāvaṭ preraṇā na mār de."],
                    ["I celebrate tiny wins, like successfully ordering tea without switching to English when I am nervous.", "छोटी जीत मनाता हूँ, जैसे घबराहट में भी बिना अंग्रेज़ी के चाय ऑर्डर कर लेना।", "choṭī jīt manātā hū̃, jaise ghabrāhaṭ mẽ bhī binā aṅrezī ke cāy ôrḍar kar lenā."],
                    ["When technology fails, I rely on handwritten notes; communicative competence includes graceful low-tech backup.", "जब तकनीक फेल हो तो हस्तलिखित नोट पर भरोसा; संवाद कौशल में सरल बैकअप शामिल है।", "jab taknīk phel ho to hastlikhit noṭ par bharosā; saṃvād kauśal mẽ saral baiḳap śāmil hai."],
                    ["Feedback from native speakers stings briefly, yet it saves me from fossilising the same error for years.", "मातृभाषी की प्रतिक्रिया थोड़ी चुभती है, फिर भी वही गलती सालों तक जम जाने से बचाती है।", "mātṛbhāṣī kī pratikriyā thoṛī cubhtī hai, phir bhī vahī galtī sālõ tak jam jāne se bachātī hai."],
                    ["Ultimately Hindi grows when I use it to build relationships, not only to pass tests or collect certificates.", "अंततः हिन्दी तब बढ़ती है जब मैं इसे रिश्ते बनाने के लिए उपयोग करता हूँ, केवल परीक्षा या प्रमाणपत्र के लिए नहीं।", "antataḥ hindī tab baṛhtī hai jab main ise riśte banāne ke lie upayog kartā hū̃, keval parīkṣā yā pramāṇapatr ke lie nahī̃."],
                ],
            ),
        ],
    )


def chapter_655() -> dict:
    return _l(
        "Guided practice: mix-and-match sentences for daily situations—repeat until fluent.",
        "Shadow the audio; then say the Hindi line without looking.",
        [
            _p("Drill", "फिर से — again."),
            _t(
                "Sentences practice – 1",
                [
                    ["I woke up early, drank warm water, and reviewed my vocabulary list before breakfast.", "मैं जल्दी उठा, गर्म पानी पिया और नाश्ते से पहले शब्दावली की सूची दोहराई।", "main jaldī uṭhā, garm pānī piyā aur nāśte se pahle śabdāvalī kī sūcī dohrāī."],
                    ["After work I will stop by the market, buy vegetables, and cook lentil soup for my roommate.", "काम के बाद मैं बाज़ार जाऊँगा, सब्ज़ी लाऊँगा और रूममेट के लिए दाल का सूप बनाऊँगा।", "kām ke bād main bāzār jāū̃gā, sabzī lāū̃gā aur rūmmeṭ ke lie dāl kā sūp banāū̃gā."],
                    ["Please remind me at four o’clock because I tend to forget online meetings when I am coding.", "चार बजे याद दिला दीजिए क्योंकि कोड लिखते समय मुझे ऑनलाइन मीटिंग भूल जाती है।", "cār baje yād dilā dījie kyõki koḍ likhte samay mujhe ônlāin mīṭiṅ bhūl jātī hai."],
                    ["The neighbour’s dog barks at night, so I bought earplugs instead of arguing on the staircase.", "पड़ोसी का कुत्ता रात को भौंकता है, इसलिए मैंने सीढ़ी पर बहस करने के बजाय कान की रूई ली।", "paṭosī kā kuttā rāt ko bhauṅktā hai, islie mainne sīḍhī par bahas karne ke bajāy kān kī rūī lī."],
                    ["I cancelled the subscription because hidden fees appeared after the free trial ended without warning.", "मैंने सदस्यता रद्द की क्योंकि मुफ़्त ट्रायल खत्म होने के बाद बिना चेतावनी छिपे शुल्क दिखे।", "mainne sadasyatā radd kī kyõki muf̤t ṭrāyal khatm hone ke bād binā cetāvanī chipe śulk dikhe."],
                    ["She practised introducing herself in Hindi until the words felt natural rather than memorised.", "उसने अपना परिचय हिन्दी में इतना अभ्यास किया जब तक शब्द याद किए हुए नहीं, स्वाभाविक लगे।", "usne apnā paricay hindī mẽ itnā abhyās kiyā jab tak śabd yād kie hue nahī̃, svābhāvik lage."],
                    ["We took the longer coastal road because the highway was closed after an accident involving a fuel tanker.", "हाईवे ईंधन टैंकर दुर्घटना के बाद बंद था, इसलिए हमने लंबा तटीय मार्ग लिया।", "hāive īndhan ṭaiṅkar durghaṭnā ke bād band thā, islie hamne laṃbā taṭīy mārg liyā."],
                    ["Before the interview I breathed deeply, rolled my shoulders, and told myself nervousness proves I care.", "इंटरव्यू से पहले मैंने गहरी साँस ली, कंधे घुमाए और खुद से कहा कि घबराहट दिखाती है कि मुझे फर्क पड़ता है।", "iṭarvyū se pahle mainne gahrī sā̃s lī, kandhe ghumā.e aur khud se kahā ki ghabrāhaṭ dikhātī hai ki mujhe farak paṛtā hai."],
                    ["Grandfather still reads the newspaper with a magnifying glass because pride refuses cheap spectacles.", "दादा अभी भी आवर्धक काँच से अख़बार पढ़ते हैं क्योंकि घमंड सस्ता चश्मा स्वीकार नहीं करता।", "dādā abhī bhī āvardhak kā̃c se akhbār paṛhte haiṃ kyõki ghamaṇḍ sustā caśmā svīkār nahī̃ kartā."],
                    ["After yoga I felt light enough to skip the elevator and climb five floors while humming a film song.", "योग के बाद मैं इतना हल्का महसूस किया कि लिफ़्ट छोड़कर पाँच मंज़िल सीढ़ियाँ चढ़ता हुआ फ़िल्मी गाना गुनगुनाया।", "yog ke bād main itnā halkā mahasūs kiyā ki lifṭ choṛ kar pā̃c manzil sīḍhiyā̃ caṛhtā huā filmī gānā gunagunāyā."],
                    ["The toddler repeated every Hindi word we said, which reminded us to speak kindly even when tired.", "छोटे बच्चे ने हर हिन्दी शब्द दोहराया, जिससे याद आया कि थके होने पर भी नरमी से बोलें।", "choṭe bacce ne har hindī śabd dohrāyā, jisse yād āyā ki thake hone par bhī naramī se boleṃ."],
                    ["Tonight I will journal three new sentences in Hindi about gratitude, even if they are imperfect.", "आज रात मैं कृतज्ञता पर तीन नए वाक्य हिन्दी में लिखूँगा, भले ही अपूर्ण हों।", "āj rāt main kṛtajñatā par tīn nae vākya hindī mẽ likhū̃gā, bhale hī apūrṇ hoṃ."],
                ],
            ),
        ],
    )


def chapter_656() -> dict:
    return _l(
        "Prepositions in context: location, time, instrument, and goal—drilled through full sentences.",
        "Notice के बाद, में, से, को in natural speech.",
        [
            _p("Chunk", "घर के बाहर — outside the house."),
            _t(
                "Prepositions practice",
                [
                    ["After lunch I will meet you under the banyan tree near the juice stall, not inside the mall.", "दोपहर के खाने के बाद मैं जूस स्टॉल के पास बरगद के पेड़ के नीचे मिलूँगा, मॉल के अंदर नहीं।", "dopahar ke khāne ke bād main jūs sṭŏl ke pās bargad ke peṛ ke nīce milū̃gā, mŏl ke andar nahī̃."],
                    ["She hid the keys behind the flowerpot because the toddler loves throwing shiny objects down the stairs.", "उसने चाबी फूलदान के पीछे छिपाई क्योंकि शिशु चमकीली चीज़ें सीढ़ियों से नीचे फेंकना पसंद करता है।", "usne cābī phūldān ke pīche chipāī kyõki śiśu camakīlī cīzeṃ sīḍhiyõ se nīce pheṅknā pasand kartā hai."],
                    ["We walked along the river until sunset because the breeze felt cooler beside the water than on the road.", "हमने सूर्यास्त तक नदी के किनारे चला क्योंकि पानी के पास हवा सड़क से ठंडी लगी।", "hamne sūryāst tak nadī ke kināre calā kyõki pānī ke pās havā saṛak se thaṃḍī lagī."],
                    ["He signed the contract with a fountain pen from his grandfather, not with the cheap ballpoint on the desk.", "उसने दादा की फ़ाउंटेन पेन से अनुबंध पर हस्ताक्षर किए, मेज़ की सस्ती बॉलपॉइंट से नहीं।", "usne dādā kī fāuṭen pen se anubaṃdh par hastākṣar kie, mez kī sustī bŏlpoiṇṭ se nahī̃."],
                    ["The cat jumped onto the bookshelf and knocked the dictionary into the tea cup with terrifying precision.", "बिल्ली किताबों की अलमारी पर कूद गई और शब्दकोष को चाय के कप में अचूक सटीकता से गिरा दिया।", "billī kitābõ kī almārī par kūd gaī aur śabdkoṣ ko cāy ke kap mẽ acūk saṭīkatā se girā diyā."],
                    ["Between meetings I meditate for five minutes in the stairwell because it is quieter than the pantry.", "मीटिंगों के बीच मैं सीढ़ी के कोने में पाँच मिनट ध्यान करता हूँ क्योंकि पैंट्री से शांत है।", "mīṭiṅgõ ke bīc main sīḍhī ke kone mẽ pā̃c minaṭ dhyān kartā hū̃ kyõki paiṇṭrī se śānt hai."],
                    ["They moved to the hills for cleaner air, yet they still video-call relatives on festivals without fail.", "उन्होंने स्वच्छ हवा के लिए पहाड़ों में जाने का फैसला किया, फिर भी त्योहारों पर रिश्तेदारों को वीडियो कॉल करते हैं।", "unhoṃne svacch havā ke lie pahāḍõ mẽ jāne kā faislā kiyā, phir bhī tyohārõ par riśtedārõ ko vīḍiyo kŏl karte haiṃ."],
                    ["Please place the parcel on the chair, not under the table where the puppy chews cardboard boxes.", "पार्सल कुर्सी पर रखिए, मेज़ के नीचे नहीं जहाँ पिल्ला कार्डबोर्ड चबाता है।", "pārsal kursī par rakhie, mez ke nīce nahī̃ jahā̃ pillā kārḍborḍ cabātā hai."],
                    ["I learned Hindi through films, through friends, and through mistakes that native speakers patiently corrected.", "मैंने फ़िल्मों से, दोस्तों से और उन गलतियों से हिन्दी सीखी जिन्हें मातृभाषी धैर्य से सुधारते रहे।", "mainne filmõ se, dostõ se aur un galatiyõ se hindī sīkhī jinheṃ mātṛbhāṣī dhairya se sudhārte rahe."],
                    ["During the storm we stayed inside the hallway because windows rattled like angry percussion instruments.", "तूफ़ान के दौरान हम गलियारे में रहे क्योंकि खिड़कियाँ गुस्सैल ताल वाद्य की तरह खड़खड़ाईं।", "tūfān ke daurān ham galiyāre mẽ rahe kyõki khiṛkiyā̃ gussail tāl vādya kī tarah khaṛkhaṛāī̃."],
                    ["He cycled across the bridge at dawn while the city still slept under a blanket of monsoon clouds.", "उसने भोर में पुल पार साइकिल चलाई जब शहर मानसून के बादलों की चादर में सो रहा था।", "usne bhor mẽ pul pār sāikil calāī jab śahar mānasūn ke bādalõ kī cādar mẽ so rahā thā."],
                    ["After the workshop we debriefed over chai at the stall beside the temple, not at the pricey café downtown.", "कार्यशाला के बाद हमने मंदिर के बगल की चाय की दुकान पर चर्चा की, महँगे शहर के कैफ़े में नहीं।", "kāryaśālā ke bād hamne mandir ke bagal kī cāy kī dukān par carcā kī, mahṅge śahar ke kaife mẽ nahī̃."],
                ],
            ),
        ],
    )


def chapter_657() -> dict:
    return _l(
        "Light-hearted jokes to relax; humour varies—keep jokes kind and context-appropriate.",
        "Puns often play on double meanings of common words.",
        [
            _p("Smile", "हँसी आ गई — I felt like laughing."),
            _t(
                "Jokes",
                [
                    ["The math teacher said, “Why are you sad?” The student replied, “Because numbers keep adding to my problems.”", "गणित शिक्षक ने पूछा, “उदास क्यों हो?” छात्र बोला, “क्योंकि संख्याएँ मेरी समस्याओं में जुड़ती रहती हैं।”", "gaṇit śikṣak ne pūchā, “udās kyõ ho?” chātr bolā, “kyõki saṅkhyāeṃ merī samasyāõ mẽ juṛtī rahtī haiṃ.”"],
                    ["I told my phone I needed space; it replied by deleting photos without asking, which was not what I meant.", "मैंने फोन से कहा मुझे थोड़ा स्पेस चाहिए; उसने बिना पूछे फोटो मिटा दीं, जो मेरा मतलब नहीं था।", "mainne phon se kahā mujhe thoṛā spes cāhie; usne binā pūchhe phoṭo miṭā dī̃, jo merā matlab nahī̃ thā."],
                    ["The tortoise challenged the hare to a coding contest; the hare deployed fast but forgot semicolons everywhere.", "कछुए ने खरगोश को कोडिंग प्रतियोगिता में बुलाया; खरगोश ने तेज़ डिप्लॉय किया पर सेमीकॉलन भूल गया।", "kachue ne khargoś ko koḍiṅg pratiyogitā mẽ bulāyā; khargoś ne tez ḍiplŏy kiyā par semīkŏln bhūl gayā."],
                    ["My smartwatch congratulated me for standing after I fell off the treadmill; technology optimism needs limits.", "ट्रेडमिल से गिरने के बाद स्मार्टवॉच ने खड़े होने पर बधाई दी; तकनीकी आशावाद की सीमा चाहिए।", "ṭreḍmil se girne ke bād smārṭvāc ne khaṛe hone par badhāī dī; taknīkī āśāvād kī sīmā cāhie."],
                    ["The crow stole the baker’s bread, updated his status to “living my best life,” and blocked the sparrow.", "कौवे ने बेकर की रोटी चुराई, स्टेटस “बेस्ट लाइफ़” अपडेट किया और गौरैया को ब्लॉक कर दिया।", "kauve ne bekar kī roṭī curāī, sṭeṭas “besṭ lāif” apḍeṭ kiyā aur guraiyā ko blok kar diyā."],
                    ["I asked the lift why it groans; it said heavy expectations on Monday mornings exceed rated capacity.", "मैंने लिफ़्ट से पूछा कराह क्यों; बोली सोमवार सुबह भारी उम्मीदें रेटेड क्षमता से बाहर हैं।", "mainne lifṭ se pūchā karāh kyõ; bolī somvār subah bhārī ummīdeṃ reṭeḍ kṣamtā se bāhar haiṃ."],
                    ["The cat knocked over the plant and blamed gravity, citing peer-reviewed studies from other cats online.", "बिल्ली ने पौधा गिराया और गुरुत्वाकर्षण को दोष दिया, ऑनलाइन अन्य बिल्लियों के अध्ययन का हवाला देकर।", "billī ne paudhā girāyā aur gurutvākarpaṇ ko doṣ diyā, ônlāin anya billiyõ ke adhyayan kā havālā de kar."],
                    ["My friend claimed he speaks fluent Hindi after three lessons; his “fluency” sounds like a blender full of ice.", "दोस्त ने कहा तीन पाठों के बाद धाराप्रवाह हिन्दी बोलता हूँ; उसकी धारा बर्फ़ से भरे ब्लेंडर जैसी लगती है।", "dost ne kahā tīn pāṭhõ ke bād dhārāpravāh hindī boltā hū̃; uskī dhārā barf se bhare bleṇḍar jaise lagtī hai."],
                    ["The teacher said silence is golden; the student sold his notes online and bought actual gold, missing the metaphor.", "शिक्षक ने कहा मौन सोना है; छात्र ने नोट बेचकर असली सोना खरीद लिया, रूपक समझे बिना।", "śikṣak ne kahā maun sonā hai; chātr ne noṭ bec kar aslī sonā kharīd liyā, rūpak samjhe binā."],
                    ["Two clouds argued who would rain first; the farmer said, “Please coordinate before my crops file a complaint.”", "दो बादलों ने बहस की कौन पहले बरसेगा; किसान बोला, “फसल शिकायत दर्ज करे उससे पहले समन्वय करो।”", "do bādalõ ne bahas kī kaun pahle barsega; kisān bolā, “phasal śikāyat darj kare us se pahle samanvay karo.”"],
                    ["I told the mirror I need confidence; it cracked, which either means honesty or bad manufacturing.", "मैंने आईने से कहा आत्मविश्वास चाहिए; वह फट गया, या तो ईमानदारी है या खराब उत्पादन।", "mainne āīne se kahā ātmaviśvās cāhie; vah phaṭ gayā, yā to īmāndārī hai yā kharāb utpādan."],
                    ["The punchline is simple: laugh at life’s bugs, patch them when you can, and reboot with chai.", "निष्कर्ष सरल है: जीवन की खामियों पर हँसें, जहाँ हो सके पैच करें, और चाय से रीबूट करें।", "niṣkarṣ saral hai: jīvan kī khāmiyõ par hãseṃ, jahā̃ ho sake pĕc kareṃ, aur cāy se rībūṭ kareṃ."],
                ],
            ),
        ],
    )


def chapter_658() -> dict:
    return _l(
        "Reading practice: short thoughts and quotes—read slowly, then paraphrase in your own Hindi.",
        "One sentence per idea; revisit weekly to measure progress.",
        [
            _p("Reflect", "सोचिए — think about it."),
            _t(
                "Reading: jokes, thoughts, quotes",
                [
                    ["A river does not argue with the rock; it flows around until the stone becomes smooth with time.", "नदी चट्टान से बहस नहीं करती; वह बहती रहती है जब तक पत्थर समय से चिकना न हो जाए।", "nadī caṭṭān se bahas nahī̃ kartī; vah bahtī rahtī hai jab tak patthar samay se ciknā na ho jā.e."],
                    ["Kindness costs nothing yet pays interest in relationships that banks cannot calculate on spreadsheets.", "दयालुता की कीमत कुछ नहीं, फिर भी रिश्तों में वह ब्याज देती है जिसे स्प्रेडशीट पर नहीं गिना जा सकता।", "dayālutā kī kīmat kuch nahī̃, phir bhī riśtõ mẽ vah byāj detī hai jise spreḍśīṭ par nahī̃ ginā jā saktā."],
                    ["The candle loses nothing by lighting another candle; classrooms prove this every single morning.", "दूसरी मोमबत्ती जलाने से मोमबत्ती कुछ नहीं खोती; कक्षाएँ हर सुबह यह साबित करती हैं।", "dūsrī mombaṭṭī jalāne se mombaṭṭī kuch nahī̃ khotī; kakṣāeṃ har subah yah sābit kartī haiṃ."],
                    ["Silence is not empty; it is full of answers that noise keeps drowning with impatient questions.", "खामोशी खाली नहीं; वह उत्तरों से भरी है जिन्हें शोर बेसब्री वाले प्रश्नों से डुबो देता है।", "khāmośī khālī nahī̃; vah uttarõ se bharī hai jinheṃ śor besabrī vāle praśnõ se ḍubo detā hai."],
                    ["A small step daily beats a giant leap once a year because habits compound like interest in a savings account.", "रोज़ छोटा कदम साल में एक बार विशाल छलांग से बेहतर है क्योंकि आदतें बचत खाते की तरह ब्याज जोड़ती हैं।", "roz choṭā kadam sāl mẽ ek bār viśāl chalāṅg se behtar hai kyõki ādateṃ bacaṭ khāte kī tarah byāj joṛtī haiṃ."],
                    ["Forgiveness is not weakness; it is strength that refuses to let someone else’s mistake rent space in your heart.", "क्षमा कमज़ोरी नहीं; वह ताकत है जो दूसरे की गलती को आपके दिल में किरायेदार नहीं बनने देती।", "kṣamā kamzorī nahī̃; vah tākat hai jo dūsre kī galtī ko āp ke dil mẽ kirāyedār nahī̃ banne detī."],
                    ["The city sleeps, yet streetlights stay awake like quiet guardians who never demand applause.", "शहर सोता है, फिर भी सड़क की बत्तियाँ चुपचाप चौकीदार की तरह जागती हैं जो तालियाँ नहीं माँगतीं।", "śahar sotā hai, phir bhī saṭak kī battiyā̃ cupcāp caukīdār kī tarah jāgtī haiṃ jo tāliyā̃ nahī̃ māṅgtī̃."],
                    ["Books are portable magic; you can carry entire civilisations in a bag lighter than a water bottle.", "किताबें ढोने योग्य जादू हैं; आप पूरे सभ्यताओं को पानी की बोतल से हल्के थैले में ले जा सकते हैं।", "kitābeṃ ḍhone yogya jādū haiṃ; āp pūre sabhyatāõ ko pānī kī botal se halke thaile mẽ le jā sakte haiṃ."],
                    ["Humour heals when it punches up at power gently and never punches down at someone already bruised.", "हास्य तभी ठीक है जब वह सत्ता पर हल्के से कटाक्ष करे, पहले से पीड़ित व्यक्ति पर नहीं।", "hāsya tabhī ṭhīk hai jab vah sattā par halke se kaṭākṣ kare, pahle se pīḍit vyakti par nahī̃."],
                    ["The moon borrows sunlight yet we call it gentle; maybe borrowed brilliance is still genuine if shared honestly.", "चंद्रमा सूरज की रोशनी उधार लेता है फिर भी हम उसे नरम कहते हैं; शायद ईमानदारी से साझा उधारी चमक भी असली है।", "candramā sūraj kī rośanī udhār letā hai phir bhī ham use naram kahte haiṃ; śāyad īmāndārī se sājhā udhārī camak bhī aslī hai."],
                    ["Rain on a tin roof sounds like applause for farmers who waited weeks for clouds to forgive the land.", "टिन की छत पर बारिश किसानों के लिए तालियों जैसी लगती है जिन्होंने बादलों के माफ़ करने का हफ़्तों इंतज़ार किया।", "ṭin kī chat par bāriś kisānõ ke lie tāliyõ jaise lagtī hai jinhoṃne bādalõ ke māf karne kā haftõ intazār kiyā."],
                    ["Tonight’s thought: speak so that your words become bridges, not walls that echo loneliness.", "आज की सोच: ऐसे बोलें कि शब्द दीवार नहीं पुल बनें जो अकेलापन गूँजे नहीं।", "āj kī soc: aise boleṃ ki śabd dīvār nahī̃ pul baneṃ jo akelāpan gū̃je nahī̃."],
                ],
            ),
        ],
    )


def chapter_659() -> dict:
    return _l(
        "Social media: scrolling habits, comparison traps, privacy, and choosing healthier boundaries.",
        "Balance ऑनलाइन time with offline relationships.",
        [
            _p("Balance", "स्क्रीन टाइम कम करें — reduce screen time."),
            _t(
                "Social media experience",
                [
                    ["I deleted three apps after realising I scrolled past midnight and woke up tired for important meetings.", "मैंने तीन ऐप हटा दिए जब समझ आया कि मैं आधी रात तक स्क्रॉल करके महत्वपूर्ण मीटिंग के लिए थका उठता हूँ।", "mainne tīn aip haṭā die jab samajh āyā ki main ādhī rāt tak skrŏl kar ke mahatvpūrṇ mīṭiṅg ke lie thakā uṭhtā hū̃."],
                    ["Likes felt good until I noticed anxiety when a post flopped; now I write for friends, not algorithms.", "लाइक अच्छे लगे जब तक पोस्ट फ्लॉप होने पर घबराहट न दिखी; अब मैं एल्गोरिदम के लिए नहीं, दोस्तों के लिए लिखता हूँ।", "laik acche lage jab tak posṭ flŏp hone par ghabrāhaṭ na dikhī; ab main elgoridam ke lie nahī̃, dostõ ke lie likhtā hū̃."],
                    ["My cousin curated a family group without political forwards; peace returned like monsoon after dusty weeks.", "कज़िन ने राजनीतिक फॉरवर्ड के बिना पारिवारिक ग्रुप बनाया; धूल भरे हफ़्तों के बाद मानसून जैसी शांति लौटी।", "kazin ne rājnītik phŏrvarḍ ke binā pārikārik gurup banāyā; dhūl bhare haftõ ke bād mānasūn jaise śānti lauṭī."],
                    ["I stopped comparing my behind-the-scenes chaos to everyone’s highlight reel; captions rarely show laundry piles.", "मैंने अपने पर्दे के पीछे के अफरातफरी को दूसरों की हाइलाइट रील से तुलना करना बंद किया; कैप्शन में कपड़े के ढेर कम दिखते हैं।", "mainne apne parde ke pīche kī afrātafarī ko dūsrõ kī hāilāṭ rīl se tulnā karnā band kiyā; kĕpśan mẽ kapṛe ke ḍher kam dikhte haiṃ."],
                    ["Privacy settings matter: I removed my birth year from public view after a phishing attempt used fake lottery news.", "गोपनीयता सेटिंग मायने रखती है: फ़िशिंग ने नकली लॉटरी समाचार के साथ जन्म वर्ष का उपयोग किया तो मैंने सार्वजनिक दृश्य से हटाया।", "gopnīyatā seṭiṅ māyne rakhtī hai: phiśiṅg ne naklī lŏṭarī samācār ke sāth janm varṣ kā upayog kiyā to mainne sārvajanik dṛśya se haṭāyā."],
                    ["Weekend digital detox walks replaced doomscrolling; birdsong beat notification pings surprisingly fast.", "सप्ताहांत में डिजिटल डिटॉक्स वॉक ने डूमस्क्रॉलिंग की जगह ली; पक्षियों की चहचहाहट नोटिफिकेशन से जल्दी जीत गई।", "saptāhāṃt mẽ ḍijiṭal ḍiṭŏks vŏk ne ḍūmaskrŏliṅ kī jagah lī; pakṣiyõ kī cahcahāhaṭ noṭifikeśan se jaldī jīt gaī."],
                    ["I apologised online after a sarcastic comment hurt a friend; public humility healed more than private excuses.", "मैंने ऑनलाइन माफ़ी माँगी जब व्यंग्य टिप्पणी से दोस्त आहत हुआ; सार्वजनिक विनम्रता निजी बहानों से ज़्यादा असरदार रही।", "mainne ônlāin māfī māṅgī jab vyangya ippaṇī se dost āhat huā; sārvajanik vinamratā nijī bahānõ se zyādā asradār rahī."],
                    ["Influencers sell dreams in thirty seconds; I now prefer long podcasts where experts stumble honestly.", "इन्फ्लुएंसर तीस सेकंड में सपने बेचते हैं; मैं अब लंबे पॉडकास्ट पसंद करता हूँ जहाँ विशेषज्ञ ईमानदारी से लड़खड़ाते हैं।", "influaiṃsar tīs sekaiṇḍ mẽ sapne bechte haiṃ; main ab laṃbe pŏḍakāsṭ pasand kartā hū̃ jahā̃ viśeṣajñ īmāndārī se laṛkhaṛāte haiṃ."],
                    ["My grandmother does not understand memes, yet her handwritten letters outperform any viral thread for warmth.", "दादी मीम नहीं समझतीं, फिर भी उनके हस्तलिखित पत्र किसी वायरल थ्रेड से ज़्यादा गर्मजोशी देते हैं।", "dādī mīm nahī̃ samajhtī̃, phir bhī un ke hastlikhit patr kisī vāiral threḍ se zyādā garmajośī dete haiṃ."],
                    ["I schedule app updates during chai breaks so technology serves tea time instead of stealing it.", "मैं चाय ब्रेक के दौरान ऐप अपडेट शेड्यूल करता हूँ ताकि तकनीक चाय का समय चुराए नहीं, सेवा करे।", "main cāy brek ke daurān aip apḍeṭ śeḍyūl kartā hū̃ tāki taknīk cāy kā samay curā.e nahī̃, sevā kare."],
                    ["Social media showed me protests worldwide, then reminded me to donate locally where verification is easier.", "सोशल मीडिया ने दुनिया भर के प्रदर्शन दिखाए, फिर याद दिलाया कि स्थानीय दान करें जहाँ पुष्टि आसान है।", "sośal mīḍiyā ne duniyā bhar ke pradarśan dikhā.e, phir yād dilāyā ki sthānīy dān kareṃ jahā̃ puṣṭi āsān hai."],
                    ["Tonight I will put the phone in another room; the stars deserve attention that pixels cannot fake.", "आज रात फोन दूसरे कमरे में रखूँगा; तारे ध्यान के हक़दार हैं जिन्हें पिक्सेल नकल नहीं कर सकते।", "āj rāt phon dūśre kamre mẽ rakhū̃gā; tāre dhyān ke haqdār haiṃ jinheṃ piksel nakal nahī̃ kar sakte."],
                ],
            ),
        ],
    )


def chapter_660() -> dict:
    return _l(
        "Eclipse talk: safety, myths, science, and community viewing.",
        "Never look at the sun without certified filters; educate children clearly.",
        [
            _p("Safety", "प्रत्यक्ष सूर्य न देखें — do not look at the sun directly."),
            _t(
                "Eclipse conversation",
                [
                    ["The news warned us not to watch the annular eclipse through sunglasses; only ISO-certified filters are safe.", "समाचार ने चेतावनी दी कि धूप का चश्मा पहनकर वलयाकार ग्रहण न देखें; केवल आईएसओ प्रमाणित फ़िल्टर सुरक्षित हैं।", "samācār ne cetāvanī dī ki dhūp kā caśmā pahan kar valayākār grahaṇ na dekheṃ; keval īeso pramāṇit philṭar surakṣit haiṃ."],
                    ["Children asked why birds went quiet; we explained how sudden dim light confuses their internal clocks.", "बच्चों ने पूछा पक्षी चुप क्यों; हमने समझाया कि अचानक मंद रोशनी उनकी आंतरिक घड़ी भ्रमित करती है।", "baccõ ne pūchā pakṣī cup kyõ; hamne samjhāyā ki acānak mand rośanī unkī āntarik ghaṛī bhramit kartī hai."],
                    ["Grandmother recalled folk songs about demons swallowing the sun, then laughed when the telescope revealed craters.", "दादी ने लोक गीत याद किए जहाँ राक्षस सूरज निगलते हैं, फिर दूरबीन से गड्ढे देखकर हँस पड़ीं।", "dādī ne lok gīt yād kie jahā̃ rākṣas sūraj nigalte haiṃ, phir dūrbīn se gaḍḍhe dekh kar hãs paḍī̃."],
                    ["Photographers set timers and filters hours early, while impatient tourists risked phone cameras and regretted it.", "फोटोग्राफरों ने घंटों पहले टाइमर और फ़िल्टर लगाए, जबकि बेसब्री पर्यटकों ने फोन कैमरे से जोखिम उठाया और पछताया।", "phoṭograifarõ ne ghaṃṭõ pahle ṭāimar aur philṭar lagā.e, jabaki besabrī paryaṭakõ ne phon kaimre se jokhim uṭhāyā aur pacatāyā."],
                    ["The science teacher set up a pinhole projector with cardboard so everyone saw crescents without staring upward.", "विज्ञान शिक्षक ने कार्डबोर्ड से पिनहोल प्रोजेक्टर बनाया ताकि सब ऊपर देखे बिना अर्धचंद्र देख सकें।", "vigyān śikṣak ne kārḍborḍ se pinhol projekṭar banāyā tāki sab ūpar dekhe binā ardhacandra dekh sakeṃ."],
                    ["Traffic slowed because drivers pulled over to glimpse the sky; patience prevented accidents on the highway.", "चालक रुककर आसमान देखने लगे इसलिए यातायात धीमी हुई; धैर्य ने हाईवे पर दुर्घटनाएँ रोकीं।", "cālak ruk kar āsmān dekhne lage islie yātāyāt dhīmī huī; dhairya ne hāive par durghaṭnāeṃ rokī̃."],
                    ["Astrologers debated meanings on TV while astronomers calmly discussed orbital mechanics for curious students.", "ज्योतिषी टीवी पर अर्थ पर बहस करते रहे जबकि खगोलशास्त्री उत्सुक छात्रों के लिए कक्षा पथ की शांति से चर्चा करते रहे।", "jyotiṣī ṭīvī par arth par bahas karte rahe jabaki khagołaśāstrī utsuk chātrõ ke lie kakṣā path kī śānti se carcā karte rahe."],
                    ["We shared eclipse glasses with strangers in the park because curiosity should not be punished by lack of gear.", "हमने पार्क में अजनबियों के साथ ग्रहण चश्मे साझा किए क्योंकि जिज्ञासा को उपकरण की कमी से दंड नहीं मिलना चाहिए।", "hamne pārk mẽ ajnabiyõ ke sāth grahaṇ caśme sājhā kie kyõki jijñāsā ko upakaraṇ kī kamī se daṇḍ nahī̃ milnā cāhie."],
                    ["After totality, streetlights flickered on automatically, and the city sighed as if waking from a shared dream.", "पूर्णता के बाद सड़क की बत्तियाँ अपने आप चमक उठीं और शहर ने ऐसी साँस ली जैसे साझा सपने से जागा हो।", "pūrṇatā ke bād saṭak kī battiyā̃ apne āp camak uṭhī̃ aur śahar ne aisī sā̃s lī jaise sājhā sapne se jāgā ho."],
                    ["My phone camera sensor showed purple streaks, a reminder that silicon is not a substitute for human eyes.", "फोन कैमरा सेंसर पर बैंगनी धारियाँ दिखीं, यह याद दिलाता है कि सिलिकन मानव आँखों का विकल्प नहीं।", "phon kaimra seṃsar par baiṃgnī dhāriyā̃ dikhī̃, yah yād dilātā hai ki silikan mānav ā̃khõ kā vikalp nahī̃."],
                    ["We promised to recycle cardboard viewers instead of littering the riverside after the crowd dispersed.", "भीड़ बिखरने के बाद हमने कार्डबोर्ड वाले दर्शक यंत्र नदी किनारे न फेंककर रीसाइकिल करने का वादा किया।", "bhīṛ bikharne ke bād hamne kārḍborḍ vāle darśak yantra nadī kināre na pheṅk kar rīsāikil karne kā vādā kiyā."],
                    ["Science won the day, yet I still felt awe, the ancient emotion that makes us small and connected at once.", "विज्ञान ने जीत ली, फिर भी मैंने विस्मय महसूस किया, वह प्राचीन भावना जो हमें एक साथ छोटा और जुड़ा महसूस कराती है।", "vigyān ne jīt lī, phir bhī mainne vismaya mahasūs kiyā, vah prācīn bhāvnā jo hameṃ ek sāth choṭā aur juṛā mahasūs karātī hai."],
                ],
            ),
        ],
    )


def chapter_661() -> dict:
    return _l(
        "International Women’s Day: recognition, equity, mentorship, and everyday respect.",
        "Celebrate achievements; support unpaid care work visibility.",
        [
            _p("8 March", "नारी शक्ति — women’s strength."),
            _t(
                "Women's Day",
                [
                    ["Today we highlight women scientists whose papers shaped climate policy yet rarely made front-page photos.", "आज हम उन महिला वैज्ञानिकों को उजागर करते हैं जिनके पत्रों ने जलवायु नीति आकार दी पर पहले पन्ने की फोटो कम मिली।", "āj ham un mahilā vaijñānikõ ko ujāgar karte haiṃ jin ke patrõ ne jalvāyu nītī ākār dī par pahle panne kī phoṭo kam milī."],
                    ["The CEO announced extended parental leave for all caregivers, signalling that childcare is not only a mother’s burden.", "सीईओ ने सभी देखभाल करने वालों के लिए विस्तृत अवकाश की घोषणा की, संकेत देते हुए कि देखभाल केवल माँ का बोझ नहीं।", "sīīo ne sabhī dekhbhāl karne vālõ ke lie vistṛit avakāś kī ghoṣaṇā kī, saṅket dete hue ki dekhbhāl keval mā̃ kā bojh nahī̃."],
                    ["My sister’s startup secured funding after years of polite rejection emails that never explained bias clearly.", "मेरी बहन की स्टार्टअप को वर्षों के विनम्र अस्वीकृति ईमेल के बाद फंडिंग मिली जिन्होंने पक्षपात स्पष्ट नहीं बताया।", "merī bahan kī sṭārṭap ko varṣõ ke vinamra asvikṛti īmel ke bād phaṇḍiṅg milī jinhoṃne pakṣpāt spaṣṭ nahī̃ batāyā."],
                    ["We invited girls from the nearby school to tour our lab so they can picture themselves wearing lab coats confidently.", "हमने पास के स्कूल की लड़कियों को लैब दिखाने बुलाया ताकि वे आत्मविश्वास से लैब कोट पहनने की कल्पना कर सकें।", "hamne pās ke skūl kī laṛkiyõ ko laib dikhāne bulāyā tāki ve ātmaviśvās se laib koṭ pahanne kī kalpannā kar sakeṃ."],
                    ["The panel discussed wage gaps with data, not anecdotes, because feelings matter but numbers force policy change.", "पैनल ने कथाओं के बजाय डेटा से वेतन अंतर पर चर्चा की क्योंकि भावनाएँ मायने रखती हैं पर संख्याएँ नीति बदलाती हैं।", "painal ne kathāõ ke bajāy ḍeṭā se vetan antar par carcā kī kyõki bhāvnāeṃ māyne rakhtī haiṃ par saṅkhyāeṃ nītī badlātī haiṃ."],
                    ["Grandmother received flowers, yet she said real respect is sharing housework equally on ordinary Wednesdays too.", "दादी को फूल मिले, फिर भी उन्होंने कहा असली सम्मान बुधवार को भी घर का काम बराबर बाँटना है।", "dādī ko phūl mile, phir bhī unhoṃne kahā aslī sammān budhavār ko bhī ghar kā kām barābar bāṭnā hai."],
                    ["Male colleagues pledged to interrupt mansplaining in meetings because allyship requires consistent practice, not one post.", "पुरुष सहकर्मियों ने वादा किया कि मीटिंग में मैनस्प्लेनिंग रोकेंगे क्योंकि सहयोग एक पोस्ट नहीं, लगातार अभ्यास है।", "puruṣ sahakarmiyõ ne vādā kiyā ki mīṭiṅg mẽ mainaspleṇiṅ rokeṃge kyõki sahayog ek posṭ nahī̃, lagātār abhyās hai."],
                    ["The film club screened documentaries about women in sports, then debated why cameras still focus on outfits.", "फ़िल्म क्लब ने खेल में महिलाओं पर वृत्तचित्र दिखाए, फिर बहस हुई कि कैमरे अभी भी पोशाक पर क्यों टिकते हैं।", "film klub ne khel mẽ mahilāõ par vṛttacitra dikhā.e, phir bahas huī ki kaimre abhī bhī pośāk par kyõ ṭikte haiṃ."],
                    ["We donated to a shelter that helps survivors rebuild careers, because empowerment needs rupees as well as applause.", "हमने उस आश्रय को दान दिया जो पीड़ितों को करियर फिर से बनाने में मदद करता है क्योंकि सशक्तिकरण के लिए तालियों के साथ रुपये भी चाहिए।", "hamne us āśray ko dān diyā jo pīḍitõ ko kariyar phir se banāne mẽ madad kartā hai kyõki saśaktikaraṇ ke lie tāliyõ ke sāth rupye bhī cāhie."],
                    ["Teenagers organised a mural celebrating local women farmers, painting bold sunflowers around their portraits.", "किशोरों ने स्थानीय महिला किसानों का जयजयकार करते भित्ति चित्र बनाया, चित्रों के चारों ओर साहसी सूरजमुखी रंगे।", "kiśorõ ne sthānīy mahilā kisānõ kā jayjayakār karte bhitti citr banāyā, citrõ ke cārõ or sāhasī sūrajmukhī raṅge."],
                    ["Tonight I thanked my mother publicly for working night shifts yet never missing parent-teacher meetings.", "आज रात मैंने सार्वजनिक रूप से माँ को धन्यवाद दिया कि रात की शिफ्ट के बावजूद अभिभावक बैठक कभी नहीं छूटी।", "āj rāt mainne sārvajanik rūp se mā̃ ko dhanyavād diyā ki rāt kī śifṭ ke bāvajūd abhibhāvak baiṭhak kabhī nahī̃ chūṭī."],
                    ["Women’s Day is a checkpoint, not a finish line; equality needs daily verbs, not annual hashtags alone.", "महिला दिवस एक चेकपॉइंट है, फिनिश लाइन नहीं; समानता को रोज़ के क्रिया-वाचक चाहिए, केवल सालाना हैशटैग नहीं।", "mahilā divas ek cekpŏiṇṭ hai, phiniś lain nahī̃; samānatā ko roz ke kriyā-vācak cāhie, keval sālānā haiśṭaig nahī̃."],
                ],
            ),
        ],
    )


def chapter_662() -> dict:
    return _l(
        "Family quarrel: raised voices, hurt feelings, repair attempts, and boundaries.",
        "Pause before speaking; आप calm tone helps de-escalate.",
        [
            _p("Repair", "मुझे दुख हुआ — I felt hurt."),
            _t(
                "Quarrel at home",
                [
                    ["I did not mean to shout, but repeated interruptions while I was budgeting made me snap louder than intended.", "मैं चिल्लाना नहीं चाहता था, पर बजट बनाते समय बार-बार टोकने से मेरी आवाज़ ज़रूरत से ऊँची हो गई।", "main cillānā nahī̃ cāhtā thā, par buj̤ banāte samay bār-bār ṭokne se merī āvāz zarūrat se ūcī ho gaī."],
                    ["You rolled your eyes when I mentioned my promotion, and that dismissal hurt more than any critique at work.", "जब मैंने पदोन्नति का ज़िक्र किया तो आपने आँखें घुमाईं, और वह उपेक्षा ऑफिस की किसी आलोचना से ज़्यादा चुभी।", "jab mainne padonnuti kā zikr kiyā to āpne ā̃kheṃ ghumāī̃, aur vah upekṣā ôphis kī kisī ālocanā se zyādā cubhī."],
                    ["Let us lower our voices because the neighbours’ children are studying for board exams tomorrow morning.", "आवाज़ नीचे कर लेते हैं क्योंकि पड़ोस के बच्चे कल सुबह बोर्ड परीक्षा की तैयारी कर रहे हैं।", "āvāz nīce kar lete haiṃ kyõki paṭos ke bacce kal subah borḍ parīkṣā kī taiyārī kar rahe haiṃ."],
                    ["I need fifteen minutes alone to breathe; we can continue this discussion after tea instead of bruising words further.", "मुझे साँस लेने के लिए पंद्रह मिनट अकेला चाहिए; चाय के बाद बात जारी करें, शब्द और न चोट पहुँचाएँ।", "mujhe sā̃s lene ke lie pandrah minaṭ akelā cāhie; cāy ke bād bāt jārī kareṃ, śabd aur na coṭ pahuṃcāeṃ."],
                    ["Money is tight, yet accusing me of hiding expenses destroys trust faster than any bank statement could rebuild.", "पैसे कम हैं, फिर भी खर्च छिपाने का आरोप विश्वास को किसी बैंक स्टेटमेंट से तेज़ तोड़ता है।", "paise kam haiṃ, phir bhī kharc chipāne kā ārop viśvās ko kisī baiṅk sṭeṭmeṇṭ se tez toṛtā hai."],
                    ["Your mother commented on my cooking again, and I felt judged in my own kitchen where I experiment daily.", "आपकी माँ ने फिर मेरे खाने पर टिप्पणी की और मैं अपनी रसोई में प्रयोग करते हुए आलोचित महसूस किया।", "āpkī mā̃ ne phir mere khāne par ippaṇī kī aur main apanī rasoī mẽ prayog karte hue ālocit mahasūs kiyā."],
                    ["I apologise for mocking your hobby; creativity deserves support even if I do not share the same passion.", "मैं आपके शौक का मज़ाक उड़ाने के लिए माफ़ी मांगता हूँ; रचनात्मकता का समर्थन चाहिए भले ही मेरा वही जुनून न हो।", "main āp ke śauk kā mazāk uṛāne ke lie māfī māṅgtā hū̃; racanātmakatā kā samarthan cāhie bhale hī merā vahī junūn na ho."],
                    ["Let us write down three concrete worries instead of recycling old fights that never reached closure.", "तीन ठोस चिंताएँ लिख लेते हैं बजाय पुरानी लड़ाइयों को दोहराने के जिनका कभी अंत नहीं हुआ।", "tīn ṭhos cintāeṃ likh lete haiṃ bajāy purānī laṛāiyõ ko dohrāne ke jinkā kabhī ant nahī̃ huā."],
                    ["The dog hid under the bed during our argument, which reminded us that noise frightens those who love us silently.", "झगड़े के दौरान कुत्ता बिस्तर के नीचे छिप गया, जिससे याद आया कि शोर उन्हें डराता है जो चुपचाप प्यार करते हैं।", "jhagaṛe ke daurān kuttā bistar ke nīce chip gayā, jisse yād āyā ki śor unheṃ ḍarātā hai jo cupcāp pyār karte haiṃ."],
                    ["We agreed to involve a counsellor because love without communication tools becomes exhausting ping-pong blame.", "हमने काउंसलर की सलाह लेने पर सहमति जताई क्योंकि संवाद के बिना प्यार थकाऊ दोषारोप पिंग-पॉंग बन जाता है।", "hamne kāunsalar kī salāh lene par sahamti jatāī kyõki saṃvād ke binā pyār thakāū doṣārop piṅg-pŏṅg ban jātā hai."],
                    ["Before sleeping, we placed glasses of water for each other—a small ritual signalling willingness to try again tomorrow.", "सोने से पहले हमने एक-दूसरे के लिए पानी के गिलास रखे—छोटा संस्कार जो कल फिर कोशिश की इच्छा दिखाता है।", "sone se pahle hamne ek-dūsre ke lie pānī ke gilās rakhe—choṭā saṅskār jo kal phir kośiś kī icchā dikhātā hai."],
                    ["Morning light did not erase the argument, yet sharing breakfast quietly felt like the first stitch on a torn seam.", "सुबह की रोशनी ने झगड़ा मिटाया नहीं, फिर भी चुपचाप नाश्ता साझा करना फटी सिलाई पर पहला टाँक जैसा लगा।", "subah kī rośanī ne jhagaṛā miṭāyā nahī̃, phir bhī cupcāp nāśtā sājhā karnā phaṭī silāī par pahlā ṭā̃k jaise lagā."],
                ],
            ),
        ],
    )


_CONV = {i: globals()[f"chapter_{i}"] for i in range(620, 663)}


def get_conversation_chapter(chapter_id: int) -> dict | None:
    fn = _CONV.get(chapter_id)
    return fn() if fn else None
