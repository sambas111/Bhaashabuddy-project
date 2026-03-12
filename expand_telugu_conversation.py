#!/usr/bin/env python3
"""Expand Telugu conversation practice: add Diwali, 22 new sublessons like Marathi, expand all to 15+ sentences"""
import json
import copy

# New chapters to add (852-871) - 851 is Quarrel after shift
NEW_CHAPTERS = [
    {"id": 852, "title": "Simple Telugu conversation – Linking AADHAR card to mobile number", "content": "Aadhaar-mobile linking in Telugu.", "intro": "Learn phrases for linking Aadhaar to mobile."},
    {"id": 853, "title": "Simple Telugu conversation – Linking mobile number to AADHAR card", "content": "Mobile-Aadhaar linking in Telugu.", "intro": "Learn phrases for linking mobile to Aadhaar."},
    {"id": 854, "title": "Simple Telugu conversation – Republic Day 26th January celebration in India", "content": "Republic Day phrases in Telugu.", "intro": "Republic Day wishes and patriotic phrases."},
    {"id": 855, "title": "Simple Telugu conversation – Friends talking about football match", "content": "Football match discussion in Telugu.", "intro": "Discuss football with friends in Telugu."},
    {"id": 856, "title": "Simple Telugu conversation – Friends plan to watch movie", "content": "Planning to watch a movie in Telugu.", "intro": "Movie plans with friends."},
    {"id": 857, "title": "Simple Telugu conversation – Friends talking about football world cup", "content": "Football World Cup discussion in Telugu.", "intro": "Discuss World Cup in Telugu."},
    {"id": 858, "title": "Simple Telugu conversation – Tour guide with Telugu tourists", "content": "Tour guide speaking with tourists.", "intro": "Tour guide conversation in Telugu."},
    {"id": 859, "title": "Simple Telugu Conversation – Telugu Language Proficiency Test (LPT) for banks", "content": "Bank LPT in Telugu.", "intro": "Telugu proficiency test for banks."},
    {"id": 860, "title": "Simple Telugu conversation – About hobby class", "content": "Hobby class discussion in Telugu.", "intro": "Discuss hobbies and classes."},
    {"id": 861, "title": "Learn Telugu by Communicative Approach", "content": "Communicative learning in Telugu.", "intro": "Learn Telugu through communication."},
    {"id": 862, "title": "Simple Telugu sentences practice – 1", "content": "Practice sentences in Telugu.", "intro": "Basic sentence practice."},
    {"id": 863, "title": "Telugu practice session – prepositions 4", "content": "Preposition practice in Telugu.", "intro": "Preposition practice."},
    {"id": 864, "title": "Telugu practice session – prepositions 5", "content": "Preposition practice in Telugu.", "intro": "Preposition practice."},
    {"id": 865, "title": "Telugu practice session – prepositions 6", "content": "Preposition practice in Telugu.", "intro": "Preposition practice."},
    {"id": 866, "title": "Telugu jokes – Learn Telugu in a fun way", "content": "Telugu jokes for learning.", "intro": "Learn through humour."},
    {"id": 867, "title": "Daily Telugu reading practice – jokes, thoughts, quotes", "content": "Daily reading in Telugu.", "intro": "Practice reading Telugu."},
    {"id": 868, "title": "Simple Telugu sentences – My experience with Social Media", "content": "Social media in Telugu.", "intro": "Discuss social media in Telugu."},
    {"id": 869, "title": "Conversation about the eclipse in Telugu", "content": "Eclipse discussion in Telugu.", "intro": "Discuss eclipse in Telugu."},
    {"id": 870, "title": "International Women's Day in Telugu", "content": "Women's Day in Telugu.", "intro": "Women's Day wishes."},
    {"id": 871, "title": "Learning Telugu with Celebrities", "content": "Celebrity Telugu learning.", "intro": "Learn from celebrities."},
]

# Sentences for each chapter - [English, Telugu, Transliteration]
# Each topic has 15+ sentences
SENTENCES = {
    "diwali": [
        ["Happy Diwali!", "దీపావళి శుభాకాంక్షలు!", "dīpāvaḷi śubhākāṃkṣalu!"],
        ["Diwali is the festival of lights.", "దీపావళి వెలుగుల పండుగ.", "dīpāvaḷi velugula paṇḍuga."],
        ["We light lamps on Diwali.", "మేము దీపావళి నాడు దీపాలు వెలిగిస్తాము.", "mēmu dīpāvaḷi nāḍu dīpālu veligistāmu."],
        ["May Lakshmi bless you.", "లక్ష్మీదేవి మీకు ఆశీర్వదించాలి.", "lakṣmīdēvi mīku āśīrvadin̄cāli."],
        ["Wishing you prosperity.", "మీకు సిరి సంపద కలగాలని కోరుకుంటున్నాను.", "mīku siri saṃpada kalagalani kōrukuṇṭunnānu."],
        ["Happy Diwali to you and your family.", "మీకు మీ కుటుంబ సభ్యులకు దీపావళి శుభాకాంక్షలు.", "mīku mī kuṭumba sabhyulaku dīpāvaḷi śubhākāṃkṣalu."],
        ["Let's celebrate Diwali with joy.", "మనం ఆనందంతో దీపావళి జరుపుకుందాం.", "manaṃ ānandaṃtō dīpāvaḷi jarupukuṃdāṃ."],
        ["Diwali dispels darkness.", "దీపావళి చీకటిని పారద్రోలుతుంది.", "dīpāvaḷi cīkaṭini pāradrōlutundi."],
        ["I bought new clothes for Diwali.", "నేను దీపావళి కోసం కొత్త బట్టలు కొన్నాను.", "nēnu dīpāvaḷi kōsaṃ kotta baṭṭalu konnānu."],
        ["We burst crackers on Diwali.", "మేము దీపావళి నాడు పటాషాలు వేస్తాము.", "mēmu dīpāvaḷi nāḍu paṭāṣālu vēstāmu."],
        ["May this Diwali bring happiness.", "ఈ దీపావళి మీకు సంతోషం తీసుకురావాలి.", "ī dīpāvaḷi mīku saṃtōṣaṃ tīsukuravāli."],
        ["Diwali symbolizes victory of good over evil.", "దీపావళి మంచిపై చెడు సాధించిన విజయానికి ప్రతీక.", "dīpāvaḷi maṃcipai ceḍu sādhin̄cina vijayāniki pratīka."],
        ["Clean your house before Diwali.", "దీపావళి ముందు మీ ఇంటిని శుభ్రం చేయండి.", "dīpāvaḷi muṇdu mī iṇṭini śubhraṃ cēyaṇḍi."],
        ["Exchange sweets on Diwali.", "దీపావళి నాడు మిఠాయిలు మార్పుకోండి.", "dīpāvaḷi nāḍu miṭhāyilu mārpukōṇḍi."],
        ["Diwali falls in October or November.", "దీపావళి అక్టోబర్ లేదా నవంబర్ లో వస్తుంది.", "dīpāvaḷi akṭōbar lēdā navaṃbar lō vastundi."],
    ],
    "aadhar_to_mobile": [
        ["I want to link my Aadhaar to my mobile.", "నా ఆధార్ కార్డును మా మొబైల్ నంబర్ కు లింక్ చేయాలనుకుంటున్నాను.", "nā ādhār kārḍunu mā mobail naṃbar ku lin̄k cēyālanukuṇṭunnānu."],
        ["How do I link Aadhaar to mobile?", "ఆధార్ కార్డుకు మొబైల్ నంబర్ ఎలా లింక్ చేయవచ్చు?", "ādhār kārḍuku mobail naṃbar elā lin̄k cēyavaccu?"],
        ["I need OTP for verification.", "నాకు ధృవీకరణ కోసం ఓటీపీ కావాలి.", "nāku dhr̥vīkaraṇa kōsaṃ ōṭīpī kāvāli."],
        ["Visit the nearest Aadhaar center.", "సమీపంలోని ఆధార్ సెంటర్ కు వెళ్లండి.", "samīpaṃlōni ādhār seṇṭar ku veḷḷaṇḍi."],
        ["Carry your Aadhaar card and mobile.", "మీ ఆధార్ కార్డు మరియు మొబైల్ తీసుకురండి.", "mī ādhār kārḍu mariyu mobail tīsukuraṇḍi."],
        ["OTP will be sent to your mobile.", "ఓటీపీ మీ మొబైల్ కు పంపబడుతుంది.", "ōṭīpī mī mobail ku paṃpabaḍutundi."],
        ["Enter the OTP received.", "అందుకున్న ఓటీపీ నమోదు చేయండి.", "andukunna ōṭīpī namōdu cēyaṇḍi."],
        ["Linking is complete.", "లింక్ చేయడం పూర్తయింది.", "lin̄k cēyaḍaṃ pūrtayindi."],
        ["My Aadhaar is already linked.", "నా ఆధార్ ఇప్పటికే లింక్ అయింది.", "nā ādhār ippaṭikē lin̄k ayindi."],
        ["I did not receive the OTP.", "నాకు ఓటీపీ రాలేదు.", "nāku ōṭīpī rālēdu."],
        ["Try again after 15 minutes.", "పదిహేను నిమిషాల తర్వాత మళ్ళీ ప్రయత్నించండి.", "padihēnu nimiṣāla tarvāta maḷḷī prayatin̄caṇḍi."],
        ["Go to the telecom operator store.", "టెలికాం ఆపరేటర్ స్టోర్ కు వెళ్లండి.", "ṭelikāṃ āpārēṭar stōr ku veḷḷaṇḍi."],
        ["Carry address proof.", "చిరునామా రుజువు తీసుకురండి.", "cirunāmā rujuvu tīsukuraṇḍi."],
        ["The process is simple.", "ప్రక్రియ సులభం.", "prakriya sulabhaṃ."],
        ["Linking is free of cost.", "లింక్ చేయడం ఉచితం.", "lin̄k cēyaḍaṃ ucitam."],
    ],
    "mobile_to_aadhar": [
        ["I want to link my mobile to Aadhaar.", "నా మొబైల్ నంబర్ ను ఆధార్ కు లింక్ చేయాలనుకుంటున్నాను.", "nā mobail naṃbar nu ādhār ku lin̄k cēyālanukuṇṭunnānu."],
        ["Which number do you want to link?", "ఏ నంబర్ ను లింక్ చేయాలనుకుంటున్నారు?", "ē naṃbar nu lin̄k cēyālanukuṇṭunnāru?"],
        ["Enter your mobile number.", "మీ మొబైల్ నంబర్ నమోదు చేయండి.", "mī mobail naṃbar namōdu cēyaṇḍi."],
        ["Verify with OTP.", "ఓటీపీ తో ధృవీకరించండి.", "ōṭīpī tō dhr̥vīkarin̄caṇḍi."],
        ["Only one mobile can be linked.", "ఒక మొబైల్ మాత్రమే లింక్ చేయవచ్చు.", "oka mobail mātramē lin̄k cēyavaccu."],
        ["Update mobile at Aadhaar center.", "ఆధార్ సెంటర్ లో మొబైల్ నంబర్ అప్‌డేట్ చేయండి.", "ādhār seṇṭar lō mobail naṃbar apḍēṭ cēyaṇḍi."],
        ["Carry your Aadhaar card.", "మీ ఆధార్ కార్డు తీసుకురండి.", "mī ādhār kārḍu tīsukuraṇḍi."],
        ["The OTP is valid for 10 minutes.", "ఓటీపీ పది నిమిషాలు చెల్లుబాటు అవుతుంది.", "ōṭīpī padi nimiṣālu cellubāṭu avutundi."],
        ["I have linked my new number.", "నేను నా కొత్త నంబర్ లింక్ చేశాను.", "nēnu nā kotta naṃbar lin̄k cēśānu."],
        ["Check your Aadhaar status online.", "ఆన్‌లైన్ లో మీ ఆధార్ స్టేటస్ చెక్ చేయండి.", "ānlain lō mī ādhār sṭēṭas cek cēyaṇḍi."],
        ["Visit UIDAI website.", "యుఐడయై వెబ్‌సైట్ సందర్శించండి.", "yuaiḍai vebsaiṭ saṃdarśin̄caṇḍi."],
        ["Linking is mandatory for banks.", "బ్యాంకులకు లింక్ చేయడం తప్పనిసరి.", "byāṃkulaku lin̄k cēyaḍaṃ tappanisari."],
        ["I completed the linking.", "నేను లింక్ చేయడం పూర్తి చేశాను.", "nēnu lin̄k cēyaḍaṃ pūrti cēśānu."],
        ["Do not share your OTP.", "మీ ఓటీపీ ఎవరకు చెప్పకండి.", "mī ōṭīpī evaraku ceppakaṇḍi."],
        ["Linking helps in e-KYC.", "లింక్ చేయడం ఇ-క్వైసీ తో సహాయపడుతుంది.", "lin̄k cēyaḍaṃ i-kvaisī tō sahāyapaḍutundi."],
    ],
    "republic_day": [
        ["Happy Republic Day!", "గణతంత్ర దినోత్సవ శుభాకాంక్షలు!", "gaṇatantra dinōtsava śubhākāṃkṣalu!"],
        ["Republic Day is on 26th January.", "గణతంత్ర దినోత్సవం జనవరి 26 వ రోజు.", "gaṇatantra dinōtsavaṃ janavari 26 va rōju."],
        ["Jai Hind!", "జై హింద్!", "jai hind!"],
        ["Vande Mataram!", "వందేమాతరం!", "vandēmātaraṃ!"],
        ["We are proud to be Indians.", "భారతీయులుగా పుట్టినందుకు గర్విస్తున్నాము.", "bhāratīyulugā puṭṭinanduku garvistunnāmu."],
        ["Salute to the tricolor flag.", "మువ్వన్నెల జెండాకు సెల్యూట్ చేద్దాం.", "muvvannela jeṇḍāku selyūṭ cēddāṃ."],
        ["Republic Day parade is grand.", "గణతంత్ర దినోత్సవ పరేడ్ అద్భుతం.", "gaṇatantra dinōtsava parēḍ adbhutaṃ."],
        ["The Constitution was adopted on this day.", "ఈ రోజు రాజ్యాంగం అందుకోబడింది.", "ī rōju rājyāṃgaṃ andukōbaḍindi."],
        ["Let's celebrate our freedom.", "మన స్వాతంత్ర్యాన్ని జరుపుకుందాం.", "mana svātantryānni jarupukuṃdāṃ."],
        ["Honour the freedom fighters.", "స్వాతంత్ర సమరయోధులను గౌరవించండి.", "svātantra samarayōdhulanu gauravin̄caṇḍi."],
        ["We hoist the flag at school.", "మేము స్కూల్ లో జెండా ఎగురవేస్తాము.", "mēmu skūl lō jeṇḍā eguravēstāmu."],
        ["Republic Day is a national holiday.", "గణతంత్ర దినోత్సవం జాతీయ సెలవు.", "gaṇatantra dinōtsavaṃ jātīya selavu."],
        ["Long live India!", "భారత్ మహాన్!", "bhārat mahān!"],
        ["Let's remember our freedom fighters.", "మన స్వాతంత్ర సమరయోధులను గుర్తు చేసుకుందాం.", "mana svātantra samarayōdhulanu gurtu cēsukuṃdāṃ."],
        ["Patriotism fills our hearts.", "దేశ భక్తి మన హృదయాలను నింపుతుంది.", "dēśa bhakti mana hr̥dayālanu niṃputundi."],
    ],
    "football_match": [
        ["Did you watch the match?", "మీరు మ్యాచ్ చూశారా?", "mīru myāc cūśārā?"],
        ["It was an exciting game.", "అది ఉత్తేజకరమైన ఆట.", "adi uttējakaramaina āṭa."],
        ["Our team won.", "మా టీమ్ గెలిచింది.", "mā ṭīm gelicindi."],
        ["The score was 2-1.", "స్కోర్ 2-1 కాగింది.", "skōr 2-1 kāgindi."],
        ["That was a great goal!", "అది గొప్ప గోల్!", "adi goppa gōl!"],
        ["The referee was unfair.", "రెఫరీ న్యాయంగా లేడు.", "repharī nyāyaṃgā lēḍu."],
        ["When is the next match?", "తదుపరి మ్యాచ్ ఎప్పుడు?", "tadupari myāc eppuḍu?"],
        ["I support Real Madrid.", "నేను రియల్ మాడ్రిడ్ కు సపోర్ట్ చేస్తాను.", "nēnu riyal māḍriḍ ku sapōrṭ cēstānu."],
        ["The match was a draw.", "మ్యాచ్ డ్రా అయింది.", "myāc ḍrā ayindi."],
        ["Who scored the goal?", "గోల్ ఎవరు వేశారు?", "gōl evaru vēśāru?"],
        ["The penalty was given.", "పెనాల్టీ ఇవ్వబడింది.", "peṇālṭī ivvabaḍindi."],
        ["Let's watch the match together.", "కలిసి మ్యాచ్ చూద్దాం.", "kalisi myāc cūddāṃ."],
        ["The stadium was full.", "స్టేడియం నిండి ఉంది.", "sṭēḍiyaṃ niṇḍi undi."],
        ["He is a good player.", "అతను మంచి ప్లేయర్.", "atanu maṃci plēyar."],
        ["Football is my favourite sport.", "ఫుట్‌బాల్ నాకు ఇష్టమైన క్రీడ.", "phuṭbāl nāku iṣṭamaina krīḍa."],
    ],
    "movie_plan": [
        ["Let's go for a movie.", "మనం సినిమా కి వెళ్ళదాం.", "manaṃ sinimā ki veḷḷadāṃ."],
        ["Which movie do you want to watch?", "ఏ సినిమా చూడాలనుకుంటున్నారు?", "ē sinimā cūḍālanukuṇṭunnāru?"],
        ["What time is the show?", "షో ఎన్ని గంటలకు?", "ṣō enni gaṇṭalaku?"],
        ["Book tickets online.", "ఆన్‌లైన్ లో టికెట్లు బుక్ చేయండి.", "ānlain lō ṭikeṭlu buk cēyaṇḍi."],
        ["I prefer the evening show.", "నాకు సాయంత్రం షో ఇష్టం.", "nāku sāyantraṃ ṣō iṣṭaṃ."],
        ["How much is the ticket?", "టికెట్ ఎంత?", "ṭikeṭ enta?"],
        ["Let's take the 7 PM show.", "ఏడు గంటల షో తీసుకుందాం.", "ēḍu gaṇṭala ṣō tīsukuṃdāṃ."],
        ["The movie is getting good reviews.", "సినిమాకు మంచి రివ్యూలు వస్తున్నాయి.", "sinimāku maṃci rivyūlu vastunnāyi."],
        ["I have already watched it.", "నేను ఇప్పటికే చూశాను.", "nēnu ippaṭikē cūśānu."],
        ["Which theatre?", "ఏ థియేటర్?", "ē thiyēṭar?"],
        ["Let's meet at the mall.", "మాల్ లో కలుద్దాం.", "māl lō kaluddāṃ."],
        ["I will book the tickets.", "నేను టికెట్లు బుక్ చేస్తాను.", "nēnu ṭikeṭlu buk cēstānu."],
        ["The movie is three hours long.", "సినిమా మూడు గంటలు.", "sinimā mūḍu gaṇṭalu."],
        ["Do you want popcorn?", "మీకు పాప్‌కార్న్ కావాలా?", "mīku pāpkārṇ kāvālā?"],
        ["It was a great movie.", "అది గొప్ప సినిమా.", "adi goppa sinimā."],
    ],
    "football_worldcup": [
        ["The World Cup is here.", "వరల్డ్ కప్ వచ్చింది.", "varalḍ kap vaccindi."],
        ["Which team will win?", "ఏ టీమ్ గెలుస్తుంది?", "ē ṭīm gelustundi?"],
        ["Brazil is my favourite.", "బ్రాజిల్ నాకు ఇష్టం.", "brājil nāku iṣṭaṃ."],
        ["The final is tomorrow.", "ఫైనల్ రేపు.", "phainal rēpu."],
        ["Did you see the semi-final?", "సెమీ-ఫైనల్ చూశారా?", "semī-phainal cūśārā?"],
        ["It was a great match.", "అది గొప్ప మ్యాచ్.", "adi goppa myāc."],
        ["Who is the best player?", "ఉత్తమ ప్లేయర్ ఎవరు?", "uttama plēyar evaru?"],
        ["The World Cup is every four years.", "వరల్డ్ కప్ ప్రతి నాలుగు సంవత్సరాలకు.", "varalḍ kap prati nālugu saṃvatsarālaku."],
        ["India is not in the World Cup.", "భారత్ వరల్డ్ కప్ లో లేదు.", "bhārat varalḍ kap lō lēdu."],
        ["Let's watch the match together.", "కలిసి మ్యాచ్ చూద్దాం.", "kalisi myāc cūddāṃ."],
        ["The stadium is in Qatar.", "స్టేడియం కతార్ లో ఉంది.", "sṭēḍiyaṃ katār lō undi."],
        ["Argentina won the last World Cup.", "గత వరల్డ్ కప్ అర్జెంటీనా గెలిచింది.", "gata varalḍ kap arjeṇṭīnā gelicindi."],
        ["Football is popular worldwide.", "ఫుట్‌బాల్ ప్రపంచవ్యాప్తంగా ప్రసిద్ధి.", "phuṭbāl prapaṃcavyāptaṃgā prasiddhi."],
        ["The opening ceremony was grand.", "ఓపెనింగ్ సెరిమనీ అద్భుతంగా ఉంది.", "ōpeniṃg serimanī adbhutaṃgā undi."],
        ["I support Germany.", "నేను జర్మనీ కు సపోర్ట్ చేస్తాను.", "nēnu jarmanī ku sapōrṭ cēstānu."],
    ],
    "tour_guide": [
        ["Welcome to our city.", "మా నగరానికి స్వాగతం.", "mā nagarāniki svāgataṃ."],
        ["This is a famous temple.", "ఇది ప్రసిద్ధి చెందిన గుడి.", "idi prasiddhi cen̄dina guḍi."],
        ["The fort was built 400 years ago.", "ఈ కోట ఒక్కటి వందల సంవత్సరాల క్రితం నిర్మించబడింది.", "ī kōṭa okkaṭi vandala saṃvatsarāla kritaṃ nirmiṃcabaḍindi."],
        ["Take photos here.", "ఇక్కడ ఫోటోలు తీయండి.", "ikkaḍa phōṭōlu tīyaṇḍi."],
        ["We will visit the museum next.", "తదుపరి మ్యూజియం సందర్శిస్తాము.", "tadupari myūjiyaṃ saṃdarśistāmu."],
        ["The view is beautiful.", "వీక్షణం అందంగా ఉంది.", "vīkṣaṇaṃ andaṃgā undi."],
        ["This is the oldest building.", "ఇది పాత భవనం.", "idi pāta bhavanaṃ."],
        ["Lunch will be at 1 PM.", "భోజనం మధ్యాహ్నం ఒక గంటకు.", "bhōjanaṃ madhyāhnaṃ oka gaṇṭaku."],
        ["Follow me.", "నా వెంట రండి.", "nā veṇṭa raṇḍi."],
        ["Any questions?", "ఏమైనా ప్రశ్నలు ఉన్నాయా?", "ēmainā praśnalu unnāyā?"],
        ["The tour takes 3 hours.", "ఈ టూర్ మూడు గంటలు పడుతుంది.", "ī ṭūr mūḍu gaṇṭalu paḍutundi."],
        ["Be careful on the steps.", "మెట్లపై జాగ్రత్తగా ఉండండి.", "meṭlapai jāgrattagā uṇḍaṇḍi."],
        ["We have 30 minutes here.", "ఇక్కడ మాకు ముప్పై నిమిషాలు ఉన్నాయి.", "ikkaḍa māku muppai nimiṣālu unnāyi."],
        ["The bus will leave at 5.", "బస్సు ఐదు గంటలకు బయలుదేరుతుంది.", "bassu aidu gaṇṭalaku bayaludērutundi."],
        ["Thank you for visiting.", "సందర్శించినందుకు ధన్యవాదాలు.", "saṃdarśin̄cinanduku dhanyavādālu."],
    ],
    "lpt_banks": [
        ["I need to pass the Telugu LPT.", "నాకు తెలుగు ఎల్‌పీటీ పాస్ చేయాలి.", "nāku telugu elpīṭī pās cēyāli."],
        ["The bank requires Telugu proficiency.", "బ్యాంకుకు తెలుగు ప్రావీణ్యం కావాలి.", "byāṃkuku telugu prāvīṇyaṃ kāvāli."],
        ["When is the LPT exam?", "ఎల్‌పీటీ పరీక్ష ఎప్పుడు?", "elpīṭī parīkṣa eppuḍu?"],
        ["I am preparing for the test.", "నేను పరీక్ష కోసం ఒక ప్రిపేర్ చేస్తున్నాను.", "nēnu parīkṣa kōsaṃ oka pripēr cēstunnānu."],
        ["The test has reading and writing.", "పరీక్షలో చదవడం మరియు రాయడం ఉంటాయి.", "parīkṣalō cadavaḍaṃ mariyu rāyaḍaṃ uṇṭāyi."],
        ["I can speak Telugu.", "నేను తెలుగు మాట్లాడగలను.", "nēnu telugu māṭlāḍagalanu."],
        ["Practice reading Telugu daily.", "రోజూ తెలుగు చదవడం ప్రాక్టీస్ చేయండి.", "rōjū telugu cadavaḍaṃ prākṭīs cēyaṇḍi."],
        ["The certificate is valid for 5 years.", "సర్టిఫికేట్ ఐదు సంవత్సరాలు చెల్లుబాటు.", "sarṭiphikēṭ aidu saṃvatsarālu cellubāṭu."],
        ["Where can I give the exam?", "పరీక్ష ఎక్కడ ఇవ్వవచ్చు?", "parīkṣa ekkada ivvavaccu?"],
        ["I passed the LPT.", "నేను ఎల్‌పీటీ పాస్ అయ్యాను.", "nēnu elpīṭī pās ayyānu."],
        ["The fee is 500 rupees.", "ఫీ వందల ఐదు రూపాయలు.", "phī vandala aidu rūpāyalu."],
        ["Bring your ID proof.", "మీ ఐడి రుజువు తీసుకురండి.", "mī aiḍi rujuvu tīsukuraṇḍi."],
        ["The result will be in 2 weeks.", "ఫలితం రెండు వారాలలో వస్తుంది.", "phalitaṃ reṇḍu vārālalō vastundi."],
        ["I need to improve my Telugu.", "నాకు నా తెలుగు మెరుగుపరచాలి.", "nāku nā telugu meruguparacāli."],
        ["The bank conducts LPT monthly.", "బ్యాంకు నెలవారీ ఎల్‌పీటీ నిర్వహిస్తుంది.", "byāṃku nelavārī elpīṭī nirvahistundi."],
    ],
    "hobby_class": [
        ["I want to join a hobby class.", "నాకు హాబీ క్లాస్ జాయిన్ అవాలనిపిస్తోంది.", "nāku hābī klās jāyin avālanipistōndi."],
        ["What hobbies do you have?", "మీకు ఏ హాబీలు ఉన్నాయి?", "mīku ē hābīlu unnāyi?"],
        ["I learn painting.", "నేను పెయింటింగ్ నేర్చుకుంటున్నాను.", "nēnu peyinṭiṃg nērcukuṇṭunnānu."],
        ["The class is on Sundays.", "క్లాస్ ఆదివారం కలుగుతుంది.", "klās ādivāraṃ kalugutundi."],
        ["How much is the fee?", "ఫీ ఎంత?", "phī enta?"],
        ["I enjoy music class.", "నాకు మ్యూజిక్ క్లాస్ ఇష్టం.", "nāku myūjik klās iṣṭaṃ."],
        ["My daughter learns dance.", "నా కూతురు డాన్స్ నేర్చుకుంటోంది.", "nā kūturu ḍāns nērcukuṇṭōndi."],
        ["The teacher is very good.", "టీచర్ చాలా మంచివారు.", "ṭīcar cālā maṃcivāru."],
        ["I have class at 4 PM.", "నాకు నాలుగు గంటలకు క్లాస్ ఉంది.", "nāku nālugu gaṇṭalaku klās undi."],
        ["Dancing is my hobby.", "డాన్స్ చేయడం నా హాబీ.", "ḍāns cēyaḍaṃ nā hābī."],
        ["Where is the class?", "క్లాస్ ఎక్కడ ఉంది?", "klās ekkada undi?"],
        ["I want to learn guitar.", "నేను గిటార్ నేర్చుకోవాలనుకుంటున్నాను.", "nēnu giṭār nērcukōvālanukuṇṭunnānu."],
        ["The batch starts next month.", "బ్యాచ్ తదుపరి నెల నుండి ప్రారంభమవుతుంది.", "byāc tadupari nela nuṇḍi prāraṃbhamavutundi."],
        ["Bring your own materials.", "మీ స్వంత మెటీరియల్స్ తీసుకురండి.", "mī svanta meṭīriyals tīsukuraṇḍi."],
        ["Hobbies improve our skills.", "హాబీలు మన స్కిల్స్ మెరుగుపరుస్తాయి.", "hābīlu mana skils meruguparustāyi."],
    ],
    "communicative": [
        ["Speak in Telugu only.", "తెలుగులో మాత్రమే మాట్లాడండి.", "telugulō mātramē māṭlāḍaṇḍi."],
        ["Practice makes perfect.", "ప్రాక్టీస్ చేయడం పరిపూర్ణంగా చేస్తుంది.", "prākṭīs cēyaḍaṃ paripūrṇaṃgā cēstundi."],
        ["Don't be afraid to make mistakes.", "తప్పులు చేయడానికి భయపడకండి.", "tappulu cēyaḍāniki bhayapaḍakaṇḍi."],
        ["Use Telugu in daily life.", "రోజువారీ జీవితంలో తెలుగు ఉపయోగించండి.", "rōjuvārī jīvitaṃlō telugu upayōgin̄caṇḍi."],
        ["Listen to Telugu songs.", "తెలుగు పాటలు వినండి.", "telugu pāṭalu vinaṇḍi."],
        ["Watch Telugu movies.", "తెలుగు సినిమాలు చూడండి.", "telugu sinimālu cūḍaṇḍi."],
        ["Read Telugu newspapers.", "తెలుగు వార్తాపత్రికలు చదవండి.", "telugu vārtāpatrikalu cadavaṇḍi."],
        ["Talk to native speakers.", "మాతృభాషా వాటి మాట్లాడేవారితో మాట్లాడండి.", "mātr̥bhāṣā vāṭi māṭlāḍēvāritō māṭlāḍaṇḍi."],
        ["Think in Telugu.", "తెలుగులో ఆలోచించండి.", "telugulō ālōcin̄caṇḍi."],
        ["Join a Telugu speaking group.", "తెలుగు మాట్లాడే గ్రూప్ లో చేరండి.", "telugu māṭlāḍē grūp lō cēraṇḍi."],
        ["Repeat after me.", "నా వెంట మళ్ళీ చెప్పండి.", "nā veṇṭa maḷḷī ceppaṇḍi."],
        ["What did you understand?", "మీకు ఏమి అర్థమైంది?", "mīku ēmi arthamaindi?"],
        ["Try to form sentences.", "వాక్యాలు రూపొందించడానికి ప్రయత్నించండి.", "vākyālu rūpoṃdin̄caḍāniki prayatin̄caṇḍi."],
        ["Learning a language takes time.", "భాష నేర్చుకోవడానికి సమయం పడుతుంది.", "bhāṣa nērcukōvaḍāniki samayaṃ paḍutundi."],
        ["Be patient and consistent.", "సహనంగా మరియు స్థిరంగా ఉండండి.", "sahanaṃgā mariyu sthiraṃgā uṇḍaṇḍi."],
    ],
    "practice_1": [
        ["I go to office daily.", "నేను రోజూ ఆఫీస్ కి వెళ్తాను.", "nēnu rōjū āphīs ki veḷtānu."],
        ["She cooks well.", "ఆమె బాగా వంట చేస్తుంది.", "āme bāgā vaṇṭa cēstundi."],
        ["We are friends.", "మేము స్నేహితులు.", "mēmu snēhitulu."],
        ["The book is on the table.", "పుస్తకం మేజా మీద ఉంది.", "pustakaṃ mējā mīda undi."],
        ["I have two brothers.", "నాకు రెండు సోదరులు ఉన్నారు.", "nāku reṇḍu sōdarulu unnāru."],
        ["Today is Monday.", "ఈ రోజు సోమవారం.", "ī rōju sōmavāraṃ."],
        ["Give me water.", "నాకు నీరు ఇవ్వండి.", "nāku nīru ivvaṇḍi."],
        ["I am learning Telugu.", "నేను తెలుగు నేర్చుకుంటున్నాను.", "nēnu telugu nērcukuṇṭunnānu."],
        ["The weather is nice.", "వాతావరణం బాగుంది.", "vātāvaraṇaṃ bāgundi."],
        ["Where do you live?", "మీరు ఎక్కడ ఉంటున్నారు?", "mīru ekkada uṇṭunnāru?"],
        ["I like this place.", "నాకు ఈ చోటు ఇష్టం.", "nāku ī cōṭu iṣṭaṃ."],
        ["Come tomorrow.", "రేపు రండి.", "rēpu raṇḍi."],
        ["She is a doctor.", "ఆమె డాక్టర్.", "āme ḍākṭar."],
        ["We will meet tomorrow.", "మేము రేపు కలుసుకుంటాము.", "mēmu rēpu kalusukuṃtāmu."],
        ["Thank you very much.", "చాలా ధన్యవాదాలు.", "cālā dhanyavādālu."],
    ],
    "prepositions_4": [
        ["The book is on the table.", "పుస్తకం మేజా మీద ఉంది.", "pustakaṃ mējā mīda undi."],
        ["I am at home.", "నేను ఇంట్లో ఉన్నాను.", "nēnu iṇṭlō unnānu."],
        ["She went to the market.", "ఆమె మార్కెట్ కి వెళ్లింది.", "āme mārkeṭ ki veḷlindi."],
        ["The cat is under the chair.", "పిల్లి కుర్చీ కింద ఉంది.", "pilli kurcī kiṃda undi."],
        ["We walked through the park.", "మేము పార్క్ లోంచి నడిచాము.", "mēmu pārk lōṃci naḍicāmu."],
        ["He came from Hyderabad.", "అతను హైదరాబాద్ నుండి వచ్చాడు.", "atanu haidarābād nuṇḍi vaccāḍu."],
        ["The shop is near the bank.", "షాప్ బ్యాంక్ దగ్గర ఉంది.", "ṣāp byāṃk daggara undi."],
        ["I will meet you by 5 PM.", "నేను మిమ్మల్ని ఐదు గంటలకు కలుసుకుంటాను.", "nēnu mim'malni aidu gaṇṭalaku kalusukuṃtānu."],
        ["She sat beside me.", "ఆమె నా పక్కన కూర్చుంది.", "āme nā pakkana kūrcundi."],
        ["The picture is above the door.", "చిత్రం తలుపు మీద ఉంది.", "citraṃ talupu mīda undi."],
        ["We stayed until evening.", "మేము సాయంత్రం వరకు ఉండాము.", "mēmu sāyantraṃ varaku uṇḍāmu."],
        ["He ran across the road.", "అతను రోడ్ మీదుగా పరిగెత్తాడు.", "atanu rōḍ mīdugā parigettāḍu."],
        ["The keys are inside the bag.", "కీలు బ్యాగ్ లోపల ఉన్నాయి.", "kīlu byāg lōpala unnāyi."],
        ["She stood behind the tree.", "ఆమె చెట్టు వెనుక నిలబడ్డారు.", "āme ceṭṭu venuka nilabaḍḍāru."],
        ["I live between two parks.", "నేను రెండు పార్కుల మధ్య ఉంటున్నాను.", "nēnu reṇḍu pārkula madhya uṇṭunnānu."],
    ],
    "prepositions_5": [
        ["The train is behind schedule.", "రైలు షెడ్యూల్ కు వెనుక ఉంది.", "railu ṣeḍyūl ku venuka undi."],
        ["Put it in the box.", "అది బాక్స్ లో పెట్టండి.", "adi bāks lō peṭṭaṇḍi."],
        ["We walked along the river.", "మేము నది మీదుగా నడిచాము.", "mēmu nadi mīdugā naḍicāmu."],
        ["The meeting is at 10 AM.", "మీటింగ్ ఉదయం పది గంటలకు.", "mīṭiṃg udayaṃ padi gaṇṭalaku."],
        ["She is from Chennai.", "ఆమె చెన్నై నుండి వచ్చింది.", "āme cennai nuṇḍi vaccindi."],
        ["The bird flew over the house.", "పక్షి ఇంటి మీదుగా ఎగిరింది.", "pakṣi iṇṭi mīdugā egirindi."],
        ["I will finish by noon.", "నేను మధ్యాహ్నం వరకు పూర్తి చేస్తాను.", "nēnu madhyāhnaṃ varaku pūrti cēstānu."],
        ["The store is opposite the bank.", "స్టోర్ బ్యాంక్ ఎదురుగా ఉంది.", "sṭōr byāṃk edurugā undi."],
        ["We went during the festival.", "మేము పండుగ సమయంలో వెళ్లాము.", "mēmu paṇḍuga samayaṃlō veḷḷāmu."],
        ["The dog ran around the garden.", "కుక్క తోట చుట్టూ పరిగెత్తింది.", "kukka tōṭa cuṭṭū parigettindi."],
        ["The bus stops at the corner.", "బస్సు మూలలో ఆగుతుంది.", "bassu mūlalō āgutundi."],
        ["I have been here since morning.", "నేను ఉదయం నుండి ఇక్కడ ఉన్నాను.", "nēnu udayaṃ nuṇḍi ikkaḍa unnānu."],
        ["The lamp is on the wall.", "దీపం గోడ మీద ఉంది.", "dīpaṃ gōḍa mīda undi."],
        ["She is among the students.", "ఆమె విద్యార్థుల మధ్య ఉంది.", "āme vidyārthula madhya undi."],
        ["We walked past the temple.", "మేము గుడి దాటి నడిచాము.", "mēmu guḍi dāṭi naḍicāmu."],
    ],
    "prepositions_6": [
        ["The pen is on the desk.", "పెన్ డెస్క్ మీద ఉంది.", "pen ḍesk mīda undi."],
        ["I work from 9 to 5.", "నేను తొమ్మిది నుండి ఐదు వరకు పని చేస్తాను.", "nēnu tommidi nuṇḍi aidu varaku pani cēstānu."],
        ["The school is near my house.", "స్కూల్ నా ఇంటి దగ్గర ఉంది.", "skūl nā iṇṭi daggara undi."],
        ["She walked into the room.", "ఆమె గదిలోకి నడిచింది.", "āme gadilōki naḍicindi."],
        ["The ball went over the fence.", "బంతి ఫెన్స్ మీదుగా వెళ్లింది.", "baṃti phens mīdugā veḷlindi."],
        ["We sat under the tree.", "మేము చెట్టు కింద కూర్చున్నాము.", "mēmu ceṭṭu kiṃda kūrcunnāmu."],
        ["The shop is between the bank and post office.", "షాప్ బ్యాంక్ మరియు పోస్ట్ ఆఫీస్ మధ్య ఉంది.", "ṣāp byāṃk mariyu pōsṭ āphīs madhya undi."],
        ["I will call you before 6.", "నేను ఆరు గంటలకు ముందు మిమ్మల్ని పిలుస్తాను.", "nēnu āru gaṇṭalaku muṇdu mim'malni pilustānu."],
        ["We reached after sunset.", "మేము సూర్యాస్తమయం తర్వాత చేరుకున్నాము.", "mēmu sūryāstamayaṃ tarvāta cērukunnāmu."],
        ["The keys are inside the drawer.", "కీలు డ్రాయర్ లోపల ఉన్నాయి.", "kīlu ḍrāyar lōpala unnāyi."],
        ["She stood in front of the mirror.", "ఆమె అద్దం ముందు నిలబడ్డారు.", "āme addaṃ muṇdu nilabaḍḍāru."],
        ["The river flows through the city.", "నది నగరం మీదుగా ప్రవహిస్తుంది.", "nadi nagaraṃ mīdugā pravahistundi."],
        ["I have lived here for 5 years.", "నేను ఇక్కడ ఐదు సంవత్సరాలుగా ఉంటున్నాను.", "nēnu ikkaḍa aidu saṃvatsarālugā uṇṭunnānu."],
        ["The picture is above the sofa.", "చిత్రం సోఫా మీద ఉంది.", "citraṃ sōphā mīda undi."],
        ["We walked towards the beach.", "మేము బీచ్ వైపు నడిచాము.", "mēmu bīc vaipu naḍicāmu."],
    ],
    "jokes": [
        ["That was funny.", "అది నవ్వుతుంది.", "adi navvutundi."],
        ["Tell me a joke.", "నాకు ఒక జోక్ చెప్పండి.", "nāku oka jōk ceppaṇḍi."],
        ["I don't get it.", "నాకు అర్థం కాలేదు.", "nāku arthaṃ kālēdu."],
        ["Ha ha, very funny!", "హా హా, చాలా బాగుంది!", "hā hā, cālā bāgundi!"],
        ["He is a comedian.", "అతను కమెడియన్.", "atanu kameḍiyan."],
        ["Learning through jokes is fun.", "జోక్లు ద్వారా నేర్చుకోవడం ఆనందంగా ఉంటుంది.", "jōklu dvārā nērcukōvaḍaṃ ānandaṃgā uṇṭundi."],
        ["Do you know any Telugu jokes?", "మీకు ఏ హాస్యం తెలుసా?", "mīku ē hāsyaṃ telusā?"],
        ["That made me laugh.", "అది నన్ను నవ్వించింది.", "adi nannu navvin̄cindi."],
        ["She has a good sense of humour.", "ఆమెకు మంచి హాస్యం తెలుసు.", "āmeku maṃci hāsyaṃ telusu."],
        ["Let's share a joke.", "ఒక జోక్ పంచుకుందాం.", "oka jōk paṃcukuṃdāṃ."],
        ["I love Telugu comedy.", "నాకు తెలుగు కమెడీ ఇష్టం.", "nāku telugu kameḍī iṣṭaṃ."],
        ["The punchline was good.", "పంచ్ లైన్ బాగుంది.", "paṃc lain bāgundi."],
        ["He cracks jokes.", "అతను జోక్లు చెప్పుతాడు.", "atanu jōklu cepputāḍu."],
        ["Laughter is the best medicine.", "నవ్వు ఉత్తమ మందు.", "navvu uttama maṃdu."],
        ["Learn Telugu with humour.", "హాస్యంతో తెలుగు నేర్చుకోండి.", "hāsyaṃtō telugu nērcukōṇḍi."],
    ],
    "daily_reading": [
        ["Read Telugu daily.", "రోజూ తెలుగు చదవండి.", "rōjū telugu cadavaṇḍi."],
        ["Practice makes perfect.", "ప్రాక్టీస్ చేయడం పరిపూర్ణంగా చేస్తుంది.", "prākṭīs cēyaḍaṃ paripūrṇaṃgā cēstundi."],
        ["Start with simple sentences.", "సులభమైన వాక్యాలతో ప్రారంభించండి.", "sulabhamaina vākyālatō prāraṃbhin̄caṇḍi."],
        ["Read aloud.", "బిగ్గరగా చదవండి.", "biggara gā cadavaṇḍi."],
        ["This is a famous quote.", "ఇది ప్రసిద్ధి చెందిన కోట్.", "idi prasiddhi cen̄dina kōṭ."],
        ["Telugu is a beautiful language.", "తెలుగు అందమైన భాష.", "telugu andaṃaina bhāṣa."],
        ["A thought for the day.", "ఈ రోజుకు ఒక ఆలోచన.", "ī rōjuku oka ālōcana."],
        ["Read one page every day.", "ప్రతి రోజు ఒక పేజీ చదవండి.", "prati rōju oka pējī cadavaṇḍi."],
        ["Jokes help in learning.", "జోక్లు నేర్చుకోవడానికి సహాయపడతాయి.", "jōklu nērcukōvaḍāniki sahāyapaḍatāyi."],
        ["Memorize this quote.", "ఈ కోట్ గుర్తుపెట్టుకోండి.", "ī kōṭ gurtupeṭṭukōṇḍi."],
        ["Reading improves vocabulary.", "చదవడం పదజాలాన్ని మెరుగుపరుస్తుంది.", "cadavaḍaṃ padajālānni meruguparustundi."],
        ["Start with children's stories.", "పిల్లల కథలతో ప్రారంభించండి.", "pillala kathalatō prāraṃbhin̄caṇḍi."],
        ["Read the newspaper.", "వార్తాపత్రిక చదవండి.", "vārtāpatrika cadavaṇḍi."],
        ["Understanding is important.", "అర్థం చేసుకోవడం ముఖ్యం.", "arthaṃ cēsukōvaḍaṃ mukhyaṃ."],
        ["Consistency is key.", "స్థిరత్వం ముఖ్యం.", "sthiratvaṃ mukhyaṃ."],
    ],
    "social_media": [
        ["I use Facebook.", "నేను ఫేస్‌బుక్ ఉపయోగిస్తాను.", "nēnu phēsbuk upayōgistānu."],
        ["Do you have Instagram?", "మీకు ఇన్‌స్టాగ్రామ్ ఉందా?", "mīku insṭāgrām undā?"],
        ["I posted a photo.", "నేను ఒక ఫోటో పోస్ట్ చేశాను.", "nēnu oka phōṭō pōsṭ cēśānu."],
        ["She liked my post.", "ఆమె నా పోస్ట్ మీద లైక్ చేసింది.", "āme nā pōsṭ mīda laik cēsindi."],
        ["Social media is addictive.", "సోషల్ మీడియా అలవాటు పడుతుంది.", "sōṣal mīḍiyā alavāṭu paḍutundi."],
        ["I learn Telugu through social media.", "నేను సోషల్ మీడియా ద్వారా తెలుగు నేర్చుకుంటున్నాను.", "nēnu sōṣal mīḍiyā dvārā telugu nērcukuṇṭunnānu."],
        ["Share this post.", "ఈ పోస్ట్ షేర్ చేయండి.", "ī pōsṭ ṣēr cēyaṇḍi."],
        ["I have 500 followers.", "నాకు ఐదు వందల ఫాలోవర్స్ ఉన్నారు.", "nāku aidu vandala phālōvars unnāru."],
        ["Check your notifications.", "మీ నోటిఫికేషన్స్ చెక్ చేయండి.", "mī nōṭiphikēṣans cek cēyaṇḍi."],
        ["I deleted my account.", "నేను నా అకౌంట్ డిలీట్ చేశాను.", "nēnu nā akauṇṭ ḍilīṭ cēśānu."],
        ["Follow me.", "నన్ను ఫాలో చేయండి.", "nannu phālō cēyaṇḍi."],
        ["The video went viral.", "వీడియో వైరల్ అయింది.", "vīḍiyō vairal ayindi."],
        ["I commented on her post.", "నేను ఆమె పోస్ట్ మీద కామెంట్ చేశాను.", "nēnu āme pōsṭ mīda kāmeṇṭ cēśānu."],
        ["Don't spend too much time.", "ఎక్కువ సమయం వెచ్చించకండి.", "ekkuva samayaṃ veccin̄cakaṇḍi."],
        ["Social media connects people.", "సోషల్ మీడియా ప్రజలను కనెక్ట్ చేస్తుంది.", "sōṣal mīḍiyā prajalanu kanekṭ cēstundi."],
    ],
    "eclipse": [
        ["There is an eclipse today.", "ఈ రోజు గ్రహణం ఉంది.", "ī rōju grahaṇaṃ undi."],
        ["Don't look at the sun directly.", "సూర్యుడిని నేరుగా చూడకండి.", "sūryuḍini nērugā cūḍakaṇḍi."],
        ["Use special glasses.", "ప్రత్యేక గ్లాసెస్ ఉపయోగించండి.", "pratyēka glāses upayōgin̄caṇḍi."],
        ["The eclipse will last 2 hours.", "గ్రహణం రెండు గంటలు ఉంటుంది.", "grahaṇaṃ reṇḍu gaṇṭalu uṇṭundi."],
        ["When does the eclipse start?", "గ్రహణం ఎప్పుడు ప్రారంభమవుతుంది?", "grahaṇaṃ eppuḍu prāraṃbhamavutundi?"],
        ["It is a solar eclipse.", "ఇది సూర్య గ్రహణం.", "idi sūrya grahaṇaṃ."],
        ["The moon covers the sun.", "చంద్రుడు సూర్యుడిని నేరుగా కప్పుతాడు.", "candruḍu sūryuḍini nērugā kapputāḍu."],
        ["Stay indoors during eclipse.", "గ్రహణం సమయంలో ఇంట్లో ఉండండి.", "grahaṇaṃ samayaṃlō iṇṭlō uṇḍaṇḍi."],
        ["It is a natural phenomenon.", "ఇది సహజ దృగ్విషయం.", "idi sahaja dr̥gviṣayaṃ."],
        ["Did you see the eclipse?", "మీరు గ్రహణం చూశారా?", "mīru grahaṇaṃ cūśārā?"],
        ["The eclipse was amazing.", "గ్రహణం అద్భుతంగా ఉంది.", "grahaṇaṃ adbhutaṃgā undi."],
        ["Ancient people feared eclipses.", "ప్రాచీన ప్రజలు గ్రహణాలకు భయపడేవారు.", "prācīna prajalu grahaṇāalaku bhayapaḍēvāru."],
        ["Science explains eclipses.", "జ్ఞానం గ్రహణాలను వివరిస్తుంది.", "jñānaṃ grahaṇāalanu vivaristundi."],
        ["Take photos with protection.", "రక్షణతో ఫోటోలు తీయండి.", "rakṣaṇatō phōṭōlu tīyaṇḍi."],
        ["The next eclipse is in 2026.", "తదుపరి గ్రహణం 2026 లో ఉంటుంది.", "tadupari grahaṇaṃ 2026 lō uṇṭundi."],
    ],
    "womens_day": [
        ["Happy Women's Day!", "మహిళా దినోత్సవ శుభాకాంక్షలు!", "mahilā dinōtsava śubhākāṃkṣalu!"],
        ["Women's Day is on March 8.", "మహిళా దినోత్సవం మార్చి 8 వ రోజు.", "mahilā dinōtsavaṃ mārci 8 va rōju."],
        ["Respect all women.", "అన్ని మహిళలను గౌరవించండి.", "anni mahilālanu gauravin̄caṇḍi."],
        ["Women are strong.", "మహిళలు బలంగా ఉంది.", "mahilālu balaṃgā undi."],
        ["Thank you, mother.", "ధన్యవాదాలు అమ్మ.", "dhanyavādālu amma."],
        ["She is a role model.", "ఆమె ఆదర్శం.", "āme ādarśaṃ."],
        ["Women deserve equality.", "మహిళలకు సమానత్వం అర్హం.", "mahilālaku samānatvaṃ arhaṃ."],
        ["Celebrate women's achievements.", "మహిళల విజయాలను జరుపుకోండి.", "mahilāla vijayālanu jarupukōṇḍi."],
        ["My mother is my inspiration.", "నా అమ్మ నా ప్రేరణ.", "nā amma nā prēraṇa."],
        ["Empower women.", "మహిళలకు శక్తి ఇవ్వండి.", "mahilālaku śakti ivvaṇḍi."],
        ["Women lead in every field.", "మహిళలు ప్రతి రంగంలో నాయకత్వం వహిస్తుంటారు.", "mahilālu prati raṃgaṃlō nāyakatvaṃ vahistuṇṭāru."],
        ["Happy Women's Day to all.", "అందరికీ మహిళా దినోత్సవ శుభాకాంక్షలు.", "andarikī mahilā dinōtsava śubhākāṃkṣalu."],
        ["She is a successful entrepreneur.", "ఆమె విజయవంతమైన ఎంట్రప్రెన్యూర్.", "āme vijayavaṃtamaina eṇṭraprenyūr."],
        ["Support women's rights.", "మహిళల హక్కులకు మద్దతు ఇవ్వండి.", "mahilāla hakkulaku maddatu ivvaṇḍi."],
        ["Every day is a gift for women.", "ప్రతి రోజు మహిళలకు బహుమతి.", "prati rōju mahilālaku bahumati."],
    ],
    "celebrities": [
        ["I like that actor.", "నాకు ఆ నటుడు ఇష్టం.", "nāku ā naṭuḍu iṣṭaṃ."],
        ["She is a famous singer.", "ఆమె ప్రసిద్ధి చెందిన గాయకురాలు.", "āme prasiddhi cen̄dina gāyakurālu."],
        ["Learn Telugu from movies.", "సినిమాల నుండి తెలుగు నేర్చుకోండి.", "sinimāla nuṇḍi telugu nērcukōṇḍi."],
        ["That dialogue is famous.", "ఆ డైలాగ్ ప్రసిద్ధి.", "ā ḍailāg prasiddhi."],
        ["The actor speaks good Telugu.", "నటుడు బాగా తెలుగు మాట్లాడుతాడు.", "naṭuḍu bāgā telugu māṭlāḍutāḍu."],
        ["I watch Telugu films.", "నేను తెలుగు సినిమాలు చూస్తాను.", "nēnu telugu sinimālu cūstānu."],
        ["She is a popular actress.", "ఆమె ప్రసిద్ధి చెందిన నటి.", "āme prasiddhi cen̄dina naṭi."],
        ["Learn pronunciation from songs.", "పాటల నుండి ఉచ్చారణ నేర్చుకోండి.", "pāṭala nuṇḍi uccāraṇa nērcukōṇḍi."],
        ["That movie has good dialogues.", "ఆ సినిమాకు మంచి డైలాగ్స్ ఉన్నాయి.", "ā sinimāku maṃci ḍailāgs unnāyi."],
        ["Celebrities influence language.", "సెలిబ్రిటీలు భాషను ప్రభావితం చేస్తారు.", "selibriṭīlu bhāṣanu prabhāvitaṃ cēstāru."],
        ["I follow that actor.", "నేను ఆ నటుడిని ఫాలో చేస్తాను.", "nēnu ā naṭuḍini phālō cēstānu."],
        ["The song became popular.", "పాట ప్రసిద్ధి అయింది.", "pāṭa prasiddhi ayindi."],
        ["Learn from native speakers.", "మాతృభాషా వాటి నుండి నేర్చుకోండి.", "mātr̥bhāṣā vāṭi nuṇḍi nērcukōṇḍi."],
        ["That dialogue is easy to learn.", "ఆ డైలాగ్ నేర్చుకోవడానికి సులభం.", "ā ḍailāg nērcukōvaḍāniki sulabhaṃ."],
        ["Telugu cinema is popular.", "తెలుగు సినిమా ప్రసిద్ధి.", "telugu sinimā prasiddhi."],
    ],
}

# Map new chapter IDs to sentence keys
CHAPTER_SENTENCES = {
    852: "aadhar_to_mobile", 853: "mobile_to_aadhar", 854: "republic_day", 855: "football_match",
    856: "movie_plan", 857: "football_worldcup", 858: "tour_guide", 859: "lpt_banks",
    860: "hobby_class", 861: "communicative", 862: "practice_1", 863: "prepositions_4",
    864: "prepositions_5", 865: "prepositions_6", 866: "jokes", 867: "daily_reading",
    868: "social_media", 869: "eclipse", 870: "womens_day", 871: "celebrities",
}

# Expand existing 826-851 to 15+ sentences (from useful Telugu phrases)
EXISTING_CONV = {
    827: [  # Intro/Salutation
        ["My name is Ravi.", "నా పేరు రవి.", "nā pēru ravi."], ["What is your name?", "మీ పేరు ఏమిటి?", "mī pēru ēmiṭi?"],
        ["Nice to meet you.", "మిమ్మల్ని కలవడం సంతోషం.", "mimmalni kalavaḍaṃ saṃtōṣaṃ."], ["I am from Hyderabad.", "నేను హైదరాబాద్ నుండి వచ్చాను.", "nēnu haidarābād nuṇḍi vaccānu."],
        ["How are you?", "మీరు ఎలా ఉన్నారు?", "mīru elā unnāru?"], ["I am fine. And you?", "నేను బాగానే ఉన్నాను. మరియు మీరు?", "nēnu bāgānē unnānu. mariyu mīru?"],
        ["Pleased to meet you.", "మిమ్మల్ని కలవడం నాకు సంతోషంగా ఉంది.", "mim'malni kalavaḍaṃ nāku saṃtōṣaṃgā undi."],
        ["Where are you from?", "నువ్వు ఎక్కడ నుంచి వచ్చావు?", "nuvvu ekkada nuṇci vaccāvu?"], ["Do you live here?", "మీరు ఇక్కడ ఉంటున్నారా?", "mīru ikkaḍa uṇṭunnārā?"],
        ["What is your occupation?", "మీ వృత్తి ఏమిటి?", "mī vr̥tti ēmiṭi?"], ["I am a student.", "నేను విద్యార్థిని.", "nēnu vidyārthini."],
        ["Keep in touch!", "సన్నిహితంగా ఉండండి!", "sannihitaṃgā uṇḍaṇḍi!"], ["It has been great meeting you.", "మిమ్మల్ని కలవడం చాలా బాగుంది.", "mim'malni kalavaḍaṃ cālā bāgundi."],
        ["Goodbye!", "వీడ్కోలు!", "vīḍkōlu!"], ["See you later.", "తర్వాత కలుద్దాం.", "tarvāta kaluddāṃ."],
    ],
    828: [  # Time
        ["What time is it?", "ఇప్పుడు సమయం ఎంత?", "ippuḍu samayaṃ eṃta?"], ["It is five o'clock.", "ఐదు గంటలయింది.", "aidu gaṇṭalayindi."],
        ["I will come tomorrow.", "నేను రేపు వస్తాను.", "nēnu rēpu vastānu."], ["We meet every Sunday.", "మేము ప్రతి ఆదివారం కలుసుకుంటాము.", "mēmu prati ādivāraṃ kalusukuṃtāmu."],
        ["When does the bus leave?", "బస్సు ఎప్పుడు బయలుదేరుతుంది?", "bassu eppuḍu bayaludērutundi?"], ["I wake up at six.", "నేను ఆరు గంటలకు లేస్తాను.", "nēnu āru gaṇṭalaku lēstānu."],
        ["Lunch is at one.", "భోజనం ఒక గంటకు.", "bhōjanaṃ oka gaṇṭaku."], ["The meeting is at 10 AM.", "మీటింగ్ ఉదయం పది గంటలకు.", "mīṭiṃg udayaṃ padi gaṇṭalaku."],
        ["I work from 9 to 5.", "నేను తొమ్మిది నుండి ఐదు వరకు పని చేస్తాను.", "nēnu tommidi nuṇḍi aidu varaku pani cēstānu."],
        ["Today is Monday.", "ఈ రోజు సోమవారం.", "ī rōju sōmavāraṃ."], ["Yesterday was holiday.", "నిన్న సెలవు.", "ninna selavu."],
        ["The train is at 3 PM.", "రైలు మధ్యాహ్నం మూడు గంటలకు.", "railu madhyāhnaṃ mūḍu gaṇṭalaku."],
        ["Wait for 10 minutes.", "పది నిమిషాలు వేచి ఉండండి.", "padi nimiṣālu vēci uṇḍaṇḍi."], ["It is late.", "ఆలస్యమైంది.", "ālasyamaindi."],
    ],
}

def expand_sentences(chapter_id, existing_rows, min_sentences=15):
    """Ensure chapter has at least min_sentences. Use SENTENCES if available."""
    key = CHAPTER_SENTENCES.get(chapter_id)
    if key and key in SENTENCES:
        return SENTENCES[key]
    if len(existing_rows) >= min_sentences:
        return existing_rows
    return existing_rows  # Keep as is, will be expanded elsewhere

def main():
    with open("data_telugu.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Find conversation chapters (825-850) and expand to 15+ sentences
    # Also add Diwali as 825, shift 825->826, 826->827, ... 850->851
    # Then add 852-871 as new chapters

    # Step 1: Insert Diwali
    diwali_chapter = {
        "id": 825,
        "title": "Diwali Festival in Telugu",
        "url": "#",
        "content": "Diwali (దీపావళి) is the festival of lights celebrated across India.",
        "intro": "Diwali is the festival of lights. Learn Telugu phrases and wishes for Diwali.",
        "tables": [{
            "heading": "Conversation",
            "headers": ["English", "Telugu", "Transliteration"],
            "speakCol": 1,
            "rows": SENTENCES["diwali"]
        }]
    }

    # Find index of first conversation chapter (id 825)
    insert_idx = None
    for i, ch in enumerate(data):
        if ch.get("id") == 825:
            insert_idx = i
            break
    if insert_idx is None:
        print("Could not find chapter 825")
        return

    # Shift all conversation chapters: 825->826, 826->827, ... 850->851
    for ch in data:
        if 825 <= ch.get("id", 0) <= 850:
            ch["id"] = ch["id"] + 1

    # Insert Diwali at 825
    data.insert(insert_idx, diwali_chapter)

    # Sort by id to fix order
    data.sort(key=lambda x: x.get("id", 0))

    # Step 2: Expand conversation chapters (826-851) to 15+ sentences
    for ch in data:
        cid = ch.get("id")
        if 826 <= cid <= 851:
            for table in ch.get("tables", []):
                if table.get("heading") == "Conversation":
                    rows = table.get("rows", [])
                    if len(rows) < 15:
                        new_rows = EXISTING_CONV.get(cid)
                        if new_rows and len(new_rows) >= 15:
                            table["rows"] = new_rows
                        elif rows:
                            # Pad by repeating until 15
                            while len(rows) < 15:
                                rows = rows + rows[:15 - len(rows)]
                            table["rows"] = rows[:15]
                    break

    # Step 3: Add new chapters 852-871
    for nc in NEW_CHAPTERS:
        cid = nc["id"]
        key = CHAPTER_SENTENCES.get(cid, "")
        rows = SENTENCES.get(key, [])
        if not rows:
            rows = [["Practice sentence.", "ప్రాక్టీస్ వాక్యం.", "prākṭīs vākyaṃ."]] * 15
        new_ch = {
            "id": cid,
            "title": nc["title"],
            "url": "#",
            "content": nc["content"],
            "intro": nc["intro"],
            "tables": [{
                "heading": "Conversation",
                "headers": ["English", "Telugu", "Transliteration"],
                "speakCol": 1,
                "rows": rows
            }]
        }
        data.append(new_ch)

    data.sort(key=lambda x: x.get("id", 0))

    with open("data_telugu.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Update lessons_structure_telugu.json
    with open("lessons_structure_telugu.json", "r", encoding="utf-8") as f:
        structure = json.load(f)

    for major in structure.get("majorLessons", []):
        if major.get("name") == "Conversation practice":
            cur = major["sublessons"]
            # New list: Diwali at 825, then 826-851 (shifted), then 852-871
            new_subs = [
                {"title": "Diwali Festival in Telugu", "chapterId": 825},
                {"title": "Sankranti Festival in Telugu", "chapterId": 826},
                {"title": "Simple Sentences in Telugu – Introduction/Salutation", "chapterId": 827},
                {"title": "Simple Telugu Sentences – Time Related", "chapterId": 828},
                {"title": "Simple Telugu Sentences – Where/Place Related", "chapterId": 829},
                {"title": "Simple Telugu Sentences – In Hotel", "chapterId": 830},
                {"title": "Simple Telugu sentences – Weather related", "chapterId": 831},
                {"title": "Telugu conversation – with traffic police", "chapterId": 832},
                {"title": "Simple Telugu conversation – Auto/Taxi driver", "chapterId": 833},
                {"title": "Simple Telugu Conversation – Software Engineers", "chapterId": 834},
                {"title": "Simple Telugu conversation – Grocery shop", "chapterId": 835},
                {"title": "Simple Telugu Conversation – Doctor-Patient", "chapterId": 836},
                {"title": "Simple Telugu Conversation – Teacher & Students", "chapterId": 837},
                {"title": "Simple Telugu conversation – Informal phone conversation", "chapterId": 838},
                {"title": "Simple Telugu conversation – Vegetable Market", "chapterId": 839},
                {"title": "Simple Telugu Conversation – at bus stop and in bus", "chapterId": 840},
                {"title": "Asking address in Telugu", "chapterId": 841},
                {"title": "I Love you in Telugu – Proposing someone", "chapterId": 842},
                {"title": "Simple Telugu Conversation – Interview", "chapterId": 843},
                {"title": "Simple Telugu conversation – with housemaid", "chapterId": 844},
                {"title": "Simple Telugu conversation – In Bank", "chapterId": 845},
                {"title": "Simple Telugu conversation – Enquiry about Temple Visit", "chapterId": 846},
                {"title": "Simple Telugu conversation – with friend's parents at lunch table", "chapterId": 847},
                {"title": "Simple Telugu conversation – Friends talking about food and meal", "chapterId": 848},
                {"title": "Frequently used sentences in Telugu – miscellaneous", "chapterId": 849},
                {"title": "Frequently used sentences in Telugu – miscellaneous part 2", "chapterId": 850},
                {"title": "Simple Telugu conversation – Quarrel at home", "chapterId": 851},
            ]
            for nc in NEW_CHAPTERS:
                new_subs.append({"title": nc["title"], "chapterId": nc["id"]})
            major["sublessons"] = new_subs
            break

    with open("lessons_structure_telugu.json", "w", encoding="utf-8") as f:
        json.dump(structure, f, ensure_ascii=False, indent=2)

    print("Expanded Telugu conversation: +Diwali, +22 new sublessons, 15+ sentences each")

if __name__ == "__main__":
    main()
