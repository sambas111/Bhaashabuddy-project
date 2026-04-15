# -*- coding: utf-8 -*-
"""
Lesson 5 (chapters 620–662): one topic-tagged bank per sublesson title.
Sources: Omniglot Kashmiri phrases (https://www.omniglot.com/language/phrases/kashmiri.htm),
koshur.org learner patterns, and curated lines aligned with kashmiri_sentence_banks.py style.
English lines are prefixed with the scenario so rows match each sublesson title.
"""
from __future__ import annotations

from kashmiri_sentence_banks import (
    DIWALI,
    DAILY,
    ECLIPSE_DRILLS,
    FAMILY,
    FOOD,
    GREETINGS,
    HEALTH,
    IDIOMS,
    JOKES_LIGHT_DRILLS,
    NUMBERS,
    POSSESSION,
    PRESENT,
    QUESTIONS,
    READING_DRILLS,
    REPUBLIC_DAY_DRILLS,
    SHOPPING,
    SOCIAL_MEDIA_DRILLS,
    TRAVEL,
    WOMENS_DAY_DRILLS,
    QUARREL_HOME_DRILLS,
)

T = tuple[str, str, str]


def _tag(tag: str, rows: list[T]) -> list[T]:
    return [(f"({tag}) {e}", ks, ro) for e, ks, ro in rows]


def _take(n: int, rows: list[T]) -> list[T]:
    if len(rows) < n:
        raise ValueError(f"need {n} rows, got {len(rows)}")
    return rows[:n]


# --- Padding / scenario-specific lines (same orthography style as project banks) ---

_EXTRA_DIWALI: list[T] = [
    ("May your home glow this Diwali.", "तुहन्द घर यि दिवालि उजाल", "Tuhand ghar yi diva:li uja:l"),
    ("We greet everyone at Diwali.", "असि सब खॅ दिवालि मुबारक", "Asi sab khə diva:li muba:rak"),
    ("Diwali brings joy to children.", "दिवालि लड़कि खॅ ख़ुशि", "Diva:li la:r'ki khə khushi"),
    ("We light lamps on the balcony.", "असि बालकनी पॅथ दिव लग", "Asi ba:lakani pəth div lag"),
    ("Happy Diwali to the whole family.", "पूरॅ कुटुंब खॅ दिवालि मुबारक", "Pu:re kutumb khə diva:li muba:rak"),
]

_EXTRA_HOTEL: list[T] = [
    ("Do you have a vacant room?", "क्या छु ख़ालि कमर?", "Kya chu kha:li kamar?"),
    ("I want a room for one night.", "मे छु एक रात खॅ कमर", "Me chhu ek ra:t khə kamar"),
    ("Please give me the room key.", "मेहरबानी कमर चाबि द्यिव", "Meharba:ni kamar cha:bi dyiv"),
    ("Is hot water available?", "गरम आब छु?", "Garam a:b chu?"),
    ("What time is breakfast?", "नाश्तॅ कति वख्त?", "Na:shte kati vakht?"),
    ("I will check out tomorrow.", "ब सुबह चॅक आउट", "B subah chek aut"),
    ("Please keep my luggage safe.", "म्योन समान सुरक्षित रख", "M'on sama:n surakshiṭ rakh"),
    ("The AC is not working.", "एसि न चल", "Esi na chal"),
    ("Call housekeeping, please.", "हाउसकीपिंग बुलाव", "Hauski:piṅg bula:v"),
    ("Where is the dining hall?", "डाइनिंग हॉल कति?", "Da:iniṅ ho:l kati?"),
]

_EXTRA_WEATHER: list[T] = [
    ("It is very hot today.", "आज चु बॊहुत गरम", "A:j chu bohut garam"),
    ("Cold wind is blowing.", "सर्द हवा चल", "Sard hava: chal"),
    ("It may rain in the evening.", "शाम पानी पड़ सक", "Sha:m pa:ni paṛ sak"),
    ("The sky is cloudy today.", "आज आसमान मॅग", "A:j a:asma:n mæg"),
    ("Winter is severe in Kashmir.", "कशीर मंज सर्दि सख्त", "Kashi:r manz sardi sakht"),
    ("Wear a warm shawl.", "गरम शॉल पॅहन", "Garam sho:l pəhen"),
    ("The weather is pleasant.", "मौसम चु सॊन्द", "Mausam chu sond"),
    ("Fog on the road.", "रस्त मंज कोहरा", "Rast manz kohra:"),
    ("Summer heat is tiring.", "गर्मि थकावट", "Garmi thaka:vat"),
    ("It snowed on the hills.", "पहाड़ पॅ बर्फ", "Paha:ṛ pe barf"),
    ("Take an umbrella.", "छाता लॅ", "Cha:ta lə"),
    ("The forecast says rain.", "ख़बर छु पानि", "Khabar chu pa:ni"),
]

_EXTRA_POLICE: list[T] = [
    ("Good morning, officer.", "सुबह बरॊ, साहब", "Subah baro, sa:hab"),
    ("Here is my driving licence.", "यि म्योन लाइसॅन्स", "Yi m'on la:isəns"),
    ("I was not speeding.", "ब न चुस तॅज़", "B na chus təz"),
    ("Seat belt is fastened.", "सॅट बॅल्ट लाग", "Seṭ bəlṭ la:g"),
    ("Sorry for the mistake.", "माफ गलति खॅ", "Ma:f galati khə"),
    ("Where should I park?", "पार्क कति कर?", "Pa:rk kati kar?"),
    ("Is this a one-way road?", "यि एक-वे रस्त?", "Yi ek-ve rast?"),
    ("I will follow traffic rules.", "ब ट्रॅफिक नियम मान", "B ṭre:fik niyam ma:n"),
    ("Helmet is on my head.", "हॅल्मॅट म्योन सर", "Həlməṭ m'on sar"),
    ("Documents are in the glove box.", "कागज़ ग्लॉव बॉक्स", "Ka:ghz glo:v bo:ks"),
    ("May I go now?", "मे आज़ि वच हेक?", "Me a:zi vach hek?"),
    ("Thank you for your guidance.", "शुक्रिया हिदायत खॅ", "Shukriya hida:yat khə"),
]

_EXTRA_RICKSHAW: list[T] = [
    ("Take me to Lal Chowk.", "मे लाल चौक पॅठ", "Me la:l chau:k pəṭh"),
    ("How much till the airport?", "हवाई अड्डॅ तॅक कति?", "Hava:i aḍḍe tək kati?"),
    ("Please use the meter.", "मॅटर लगाव", "Meṭar laga:v"),
    ("Stop near the gate.", "दरवाजॅ लागि थांब", "Darva:ze la:gi tha:mb"),
    ("I will pay by UPI.", "ब युपीआय सॅथ दॅ", "B yupia:i səth de"),
    ("Drive slowly on bumps.", "स्पीड ब्रॅकर हलुई", "Spi:d bre:kar halui"),
    ("Wait five minutes.", "पाँच मिनट ठाह", "Pa:ñch minaṭ Tha:h"),
    ("Is this the shortest route?", "यि छु लॊट रस्त?", "Yi chu loṭ rast?"),
    ("Drop me at the hospital.", "हॉस्पिटल सॅथ उतार", "Ho:sṭital səth uta:r"),
    ("Keep the change.", "खुल्ला रख", "Khulla rakh"),
]

_EXTRA_SOFTWARE: list[T] = [
    ("We have a stand-up at ten.", "असि दॅह वख्त मीटिंग", "Asi dəh vakht mi:ṭiṅg"),
    ("Please review my pull request.", "पुल रिक्वॅस्ट दॅख", "Pul rikvest de:kh"),
    ("The server is down.", "सर्वर बंद", "Sarvar band"),
    ("I will push the fix tonight.", "आज रात फिक्स पुश", "A:j ra:t fiks push"),
    ("Let us pair-program this bug.", "यि बग पॅर प्रोग्रॅम", "Yi bag pe:r progræm"),
    ("The build passed on CI.", "बिल्ड सीआय पॅ पास", "Bilḍ sia:i pe pa:s"),
    ("I need admin access.", "मे छु एडमिन ऐक्सॅस", "Me chhu edmin aiksəs"),
    ("Share your screen.", "स्क्रीन वांट", "Skri:n va:nṭ"),
    ("The client called twice.", "क्लाइंट दो वार फोन", "Kla:iṅt do va:r fon"),
    ("We deploy on Friday.", "असि जुमॅ डिप्लॉय", "Asi jume ḍiplo:i"),
    ("Password must be strong.", "पासवर्ड मज़बूत", "Pa:svo:rḍ mazbu:t"),
    ("I am in a video call.", "ब चुस विडियो कॉल", "B chus viḍiyo ko:l"),
]

_EXTRA_PHONE: list[T] = [
    ("Hello, it is me.", "हॅलॊ, ब छु", "Həlo, b chu"),
    ("Can you hear me?", "त्स मे आश हेकिव?", "Ts me a:sh hekiv?"),
    ("The signal is weak.", "सिगनल कमज़ोर", "Signal kamzor"),
    ("I will call you back.", "ब फिर फोन कर", "B phir fon kar"),
    ("My battery is low.", "बॅटॅरी कम", "Bəṭeri kam"),
    ("Speak a little louder.", "थोड़ उंच उलाव", "Tho:r unch ula:v"),
    ("Wrong number.", "गलत नंबर", "Galat nambar"),
    ("I am on the road.", "ब चुस रस्त", "B chus rast"),
    ("Text me the address.", "पता टॅक्स्ट कर", "Pata ṭekst kar"),
    ("Got WhatsApp?", "व्हाट्सऐप छु?", "Vha:ṭsaip chu?"),
    ("FaceTime later?", "फॅसटाइम पॅथ?", "Fæsṭa:m pəth?"),
    ("Sorry, wrong person.", "माफ, गलत शख्स", "Ma:f, galat shakhs"),
]

_EXTRA_LOVE: list[T] = [
    ("I love you (common phrase).", "त्स छुख म्योन जिगर", "Ts chukh m'on jigar"),
    ("You mean a lot to me.", "त्स छु मॅ बॊहुत", "Ts chu mə bohut"),
    ("May I walk with you?", "मे तुहन्द सॅथ चल हेक?", "Me tuhand səth chal hek?"),
    ("I respect your family.", "मे कर तुहन्द कुटुंब इज़्ज़त", "Me kar tuhand kutumb izzat"),
    ("Your smile is beautiful.", "तुहन्द मुस्कान सॊन्द", "Tuhand muska:n sond"),
    ("I think of you often.", "ब कर तुहन्द बॊहुत याद", "B kar tuhand bohut ya:d"),
    ("Will you marry me?", "त्स मॅ सॅथ बॅयाह?", "Ts mə səth bəya:h?"),
    ("I want to meet your parents.", "मे तुहन्द मॊज बॊब मिलुन", "Me tuhand moj bob milun"),
    ("You are very kind.", "त्स छुख बॊहुत नेक", "Ts chukh bohut nek"),
    ("Let us take it slowly.", "हलुई हलुई", "Halui halui"),
    ("I am serious about us.", "असि बारॅ सच", "Asi ba:re sach"),
    ("God bless you.", "ख़ुदा सलामत रखे", "Khuda: sala:mat rakhe"),
]

_EXTRA_INTERVIEW: list[T] = [
    ("Tell me about yourself.", "अपनॅ बारॅ उलाव", "Apne ba:re ula:v"),
    ("Why do you want this job?", "यि काम क्या खात्रि?", "Yi ka:m kya kha:tri?"),
    ("My experience is five years.", "म्योन तजुर्बॅ पाँच बॅ", "M'on tajurbe pa:ñch bə"),
    ("I graduated from university.", "युनिवर्सिटि पॅ पास", "Yunivərsiṭi pe pa:s"),
    ("I can join next month.", "अगलॅ महिनॅ मिल", "Agle mahine mil"),
    ("Expected salary?", "उम्मीद मॅ तनख़्वाह?", "Ummi:d mə tanakhwa:h?"),
    ("I am a team player.", "ब चुस टीम खॅलाड़", "B chus ṭi:m kheḷa:ṛ"),
    ("Strengths and weaknesses?", "ताकत आ कमज़ोरि?", "Ta:qat a kamzori?"),
    ("Thank you for this opportunity.", "शुक्रिया मौकॅ खॅ", "Shukriya mauke khə"),
    ("May I ask a question?", "एक सवाल पूछ हेक?", "Ek sava:l pu:ch hek?"),
    ("I will work with honesty.", "दियानत सॅथ काम", "Diya:nat səth ka:m"),
    ("Good morning, interviewers.", "सुबह बरॊ", "Subah baro"),
]

_EXTRA_MAID: list[T] = [
    ("Please clean the kitchen today.", "आज रसोइ साफ कर", "A:j rasoi sa:f kar"),
    ("Wash the clothes tomorrow.", "फालॅ कपड़ धो", "Fa:le kapaṛ dho"),
    ("Iron my shirt.", "म्योन कमीज इस्त्री", "M'on kami:j istri:"),
    ("The floor needs mopping.", "फ़र्श धोन जाय", "Farsh dhon ja:y"),
    ("Take Sunday off.", "रविवार आराम", "Ravi:va:r a:ra:m"),
    ("I will pay on the first.", "मे दॅ पॅहलॅ तारिख", "Me de pəhle ta:rikh"),
    ("Be careful with glass.", "काँच सॅथ सावधान", "Kã:ch səth sa:vdha:n"),
    ("Lock the door when you leave.", "वच वख्त दरवाज़ बंद", "Vach vakht darva:z band"),
    ("Vegetables are in the fridge.", "सब्ज़ि फ्रिज", "Sabzi frij"),
    ("Call me if you need money.", "पैसॅ जाय तॊ फोन", "Paise ja:y to fon"),
    ("Rest for an hour after lunch.", "दपॅहर पॅथ आराम", "Dapehar pəth a:ra:m"),
    ("Thank you for your help.", "शुक्रिया मदद खॅ", "Shukriya madad khə"),
]

_EXTRA_AADHAR_MOBILE: list[T] = [
    ("I want to link Aadhaar to my mobile.", "मे आधार मोबाइल सॅथ जोड़ुन", "Me a:dha:r moba:i səth jo:ṛun"),
    ("Here is my Aadhaar number.", "यि म्योन आधार नंबर", "Yi m'on a:dha:r nambar"),
    ("OTP came on the phone.", "ओटीपी फोन पॅ आय", "Oṭipi fon pe a:y"),
    ("The SIM is in my name.", "सिम छु म्योन नाव", "Sim chu m'on na:v"),
    ("Please verify with fingerprint.", "उंगल सॅथ पक्क कर", "Ungal səth pakk kar"),
    ("The centre is crowded.", "सॅंटर मंज भीड़", "Seṅṭar manz bhi:ṛ"),
    ("Take a token and wait.", "टोकॅन लॅ ठाह", "To:kən lə Tha:h"),
    ("Is the linking done?", "जोड़ गय?", "Jo:ṛ gay?"),
    ("I need a confirmation SMS.", "पुष्टि एसएमएस", "Puṣṭi esemes"),
    ("They asked for a photocopy.", "फोटोकॉपि मॅंग", "Fotoko:pi mæṅg"),
    ("Biometric failed twice.", "बायॊमॅट्रिक दो वार फेल", "Ba:yomeṭrik do va:r fel"),
    ("Come back next week.", "अगलॅ हफ़्तॅ यि", "Agle hafte yi"),
]

_EXTRA_MOBILE_AADHAR: list[T] = [
    ("I want to link my mobile to Aadhaar.", "मे मोबाइल आधार सॅथ जोड़ाव", "Me moba:i a:dha:r səth jo:ṛa:v"),
    ("The mobile must be registered.", "मोबाइल रॅजिस्टर्ड", "Moba:i rejisṭərḍ"),
    ("Same number for five years?", "पाँच बॅ हॊइ नंबर?", "Pa:ñch bə hoi nambar?"),
    ("Carry original ID.", "असल पहचान पत्र", "Asal pahcha:n patra"),
    ("The shop verified OTP.", "दुकान नॅ ओटीपी ठीक", "Duka:n ne Oṭipi thi:k"),
    ("Recharge pack is active.", "रिचार्ज पॅक चाल", "Richa:rj pe:k cha:l"),
    ("Update address if wrong.", "पता गलत तॊ बदल", "Pata galat to badal"),
    ("Customer care helped.", "कस्टमर कॅयर मदद", "Kasṭamar kear madad"),
    ("Do not share OTP.", "ओटीपी न वांट", "Oṭipi na va:nṭ"),
    ("SIM swap needs caution.", "सिम बदल सावधान", "Sim badal sa:vdha:n"),
    ("Linking is free of charge.", "जोड़ मुफ़्त", "Jo:ṛ muft"),
    ("SMS confirmation received.", "एसएमएस पुष्टि आय", "Esemes puṣṭi a:y"),
]

_EXTRA_BANK: list[T] = [
    ("I want to open an account.", "मे खातॅ खोलुन", "Me kha:te kholun"),
    ("What is the minimum balance?", "कम असल बॅलॅन्स?", "Kam asal bələns?"),
    ("Please fill this form.", "यि फॉर्म भर", "Yi fo:rm bhar"),
    ("I need a cheque book.", "चॅक बुक जाय", "Chek buk ja:y"),
    ("Where is the ATM?", "एटीएम कति?", "Eṭiem kati?"),
    ("Withdraw ten thousand rupees.", "दॅह हॅज़ार रुपय काड", "Dəh həza:r rupay ka:aḍ"),
    ("Deposit this cash.", "यि नगद जमा", "Yi nagad jama:"),
    ("What is my account number?", "म्योन खातॅ नंबर?", "M'on kha:te nambar?"),
    ("I forgot my PIN.", "ब बिसर पिन", "B bisar pin"),
    ("The bank is closed today.", "आज बैंक बंद", "A:j baiṅk band"),
    ("Please stamp this document.", "यि दस्तॅवॅज़ मॊहर", "Yi dastəvejz mohar"),
    ("Interest rate for savings?", "बचत पॅ ब्याज़?", "Bachat pe bya:j?"),
]

_EXTRA_TEMPLE: list[T] = [
    ("What time is the aarti?", "आरति कति वख्त?", "A:arti kati vakht?"),
    ("Where do we leave shoes?", "जूता कति सॅटॅ?", "Ju:ta kati səṭe?"),
    ("Is photography allowed?", "फोटो मंज़ूर?", "Fo:to manzu:r?"),
    ("Prasad is distributed after puja.", "पूजॅ पॅथ प्रसाद", "Pu:je pəth prasa:d"),
    ("The temple is very old.", "मंदिर चु पुरान", "Mandir chu pura:n"),
    ("We ring the bell.", "असि घंटॅ वजाव", "Asi ghaṇṭe vaja:v"),
    ("May I enter the sanctum?", "गर्भगृह मंज यि हेक?", "Garbhagṛh manz yi hek?"),
    ("Donations go to the trust.", "दान ट्रस्ट", "Da:n ṭrasṭ"),
    ("Holy water is offered.", "चरणामृत दॅ", "Chara:na:mṛit de"),
    ("Festivals are crowded here.", "त्योहार मंज भीड़", "Tyoha:r manz bhi:ṛ"),
    ("Respect silence inside.", "अंदर शांत", "Andar sha:nt"),
    ("We came for darshan.", "असि दॅर्शन खॅ", "Asi de:rshan khə"),
]

_EXTRA_FOOTBALL: list[T] = [
    ("Which team won?", "कुस टीम जित?", "Kus ṭi:m jit?"),
    ("The match was exciting.", "मॅच रॊमांचक", "Mæch roma:nchak"),
    ("He scored a goal.", "सु गोल मार", "Su gol ma:r"),
    ("Offside — bad luck!", "ऑफसाइड — बॅ किस्मत!", "O:fsa:iḍ — bə kismat!"),
    ("Extra time begins.", "एक्स्ट्रा टाइम शुरू", "Ekstra ṭa:m shuru:"),
    ("The referee blew the whistle.", "रॅफॅरी सिटि वजाव", "Refəri siṭi vaja:v"),
    ("We support our club.", "असि सॅथ क्लब", "Asi səth klub"),
    ("Penalty shootout!", "पॅनॅल्टि!", "Pənəlṭi!"),
    ("The stadium was full.", "स्टॅडियम भर", "Sṭeḍiyam bhar"),
    ("They played well.", "तिम खॅल बरो", "Tim khe:l baro"),
    ("Next match on Sunday.", "अगलॅ मॅच रविवार", "Agle mæch ravi:va:r"),
    ("I watched on TV.", "ब दॅख टीवि", "B de:kh ṭi:vi"),
]

_EXTRA_MOVIE: list[T] = [
    ("Which film is playing?", "कुस फिल्म चल?", "Kus film chal?"),
    ("Two tickets for the night show.", "रात शो खॅ दो टिकट", "Ra:t sho khə do ṭikaṭ"),
    ("The hall is air-conditioned.", "हॉल चु एसि", "Ho:l chu esi"),
    ("Popcorn and cold drink.", "पॉपकॉर्न आ ठंड पेय", "Po:pko:rn a thaṇḍ pey"),
    ("The movie was long.", "फिल्म चु लंब", "Film chu lamb"),
    ("Interval after one hour.", "एक घंटॅ पॅथ इंटरवल", "Ek ghaṇṭe pəth iṭarval"),
    ("Who is the hero?", "हिरॊ कुस?", "Hiro kus?"),
    ("Reviews were mixed.", "रिव्यु मिलॅ-जुलॅ", "Rivy'u mile-jule"),
    ("Let us book online.", "ऑनलाइन बुक", "Onlain buk"),
    ("Seat number twelve.", "बॅहवॅ नंबर", "Bəhve nambar"),
    ("Do not use phone inside.", "अंदर फोन न", "Andar fon na"),
    ("The climax was emotional.", "आख़िर भावुक", "A:khir bha:vuk"),
]

_EXTRA_WORLDCUP: list[T] = [
    ("Which countries qualified?", "कुस मुल्क क्वालिफाइ?", "Kus mulk kwa:lifai?"),
    ("The final is on Sunday.", "फाइनल रविवार", "Fa:nal ravi:va:r"),
    ("They defended well.", "तिम डिफॅन्ड बरो", "Tim ḍifənd baro"),
    ("Penalty in the box!", "बॉक्स मंज पॅनॅल्टि!", "Bo:ks manj pənəlṭi!"),
    ("The crowd chanted.", "हजूम चिल्लाव", "Haju:m chilla:v"),
    ("VAR checked the goal.", "वीएआर खोल गोल", "Vi:a:r khol gol"),
    ("National anthem before match.", "क़ौमि गीत पॅहलॅ", "Qaumi gi:t pəhle"),
    ("Injury time added.", "इंजरी टाइम", "Injari ṭa:m"),
    ("We watched at a café.", "कॅफॅ मंज दॅख", "Kæfe manz de:kh"),
    ("Overtime — still equal!", "ओवरटाइम — बराबर!", "Ovarṭa:m — bara:bar!"),
    ("Champions lift the cup.", "चॅम्पियन कप उठाव", "Che:mpiyan kap uṭha:v"),
    ("Better luck next time.", "अगलॅ वख्त बरो", "Agle vakht baro"),
]

_EXTRA_TOUR: list[T] = [
    ("Welcome to Kashmir.", "कशीर मंज इस्तक़्बाल", "Kashi:r manz istiqba:l"),
    ("This lake is Dal Lake.", "यि छु डल झील", "Yi chu Dal jhi:l"),
    ("We will visit the garden tomorrow.", "फालॅ बाग मिल", "Fa:le ba:g mil"),
    ("Please take photos here.", "यि फोटो खिच", "Yi fo:to khich"),
    ("The shikara ride costs this much.", "शिकारॅ भाड़ा यि", "Shika:re bha:ṛa yi"),
    ("Respect local customs.", "रिवायत इज़्ज़त", "Riva:yat izzat"),
    ("Do not litter.", "कचरा न सॅटॅ", "Kachra na səṭe"),
    ("Try the local food.", "लॊकल खान चख", "Lokal kha:n chakh"),
    ("Winter is cold — dress warm.", "सर्दि गरम कपड़", "Sardi garam kapaṛ"),
    ("This is a handicraft shop.", "यि हॅंडिक्राफ्ट दुकान", "Yi hæṇḍikra:fṭ duka:n"),
    ("We return by evening.", "शाम वापस", "Sha:m va:pas"),
    ("Thank you for visiting.", "शुक्रिया मुलॅक़ात", "Shukriya mula:qa:t"),
]

_EXTRA_BANK_TEST: list[T] = [
    ("Read this passage aloud.", "यि परॅ उच्चार", "Yi pare uchcha:r"),
    ("Choose the correct option.", "सही चुन", "Sahi: chun"),
    ("Translate into Kashmiri.", "कॉशुर मंज उनवाद", "Ko:shur manz unva:d"),
    ("Time allowed: thirty minutes.", "वख्त: त्रॅह मिनट", "Vakht: trə minaṭ"),
    ("Do not use a dictionary.", "डिक्शनरी न", "Ḍikshanari na"),
    ("Write a short essay.", "लॊट निबंध", "Loṭ nibandh"),
    ("Grammar section follows.", "ग्रॅमर हिस्सॅ", "Græmar hisse"),
    ("Listening test next.", "आशुन टॅस्ट", "A:shun ṭesṭ"),
    ("Spell this word.", "यि शब्द हिजॅ", "Yi shabd hije"),
    ("Formal letter format.", "रॊसमि चिट्ठि", "Rosmi chiṭṭhi"),
    ("Marks will be announced later.", "नंबर पॅथ बयान", "Nambar pəth baya:n"),
    ("Thank you — you may leave.", "शुक्रिया — वच सक", "Shukriya — vach sak"),
]

_EXTRA_FOOD_LUNCH: list[T] = [
    ("Lunch is ready.", "दपॅहर खान तैयार", "Dapehar kha:n taiya:r"),
    ("Please pass the rice.", "शाल वांट", "Sha:l va:nṭ"),
    ("This curry is mild.", "यि सालन हल्क", "Yi sa:lan halk"),
    ("I do not eat onion today.", "आज प्याज़ न खा", "A:j pya:z na kha:"),
    ("More salad, please.", "सॅलॅड होर", "Səleḍ hor"),
    ("Water for everyone.", "सब खॅ आब", "Sab khə a:b"),
    ("The dessert was sweet.", "मिठाइ मिठ", "Miṭha:i miṭh"),
    ("Help yourself.", "अपनॅ खा", "Apne kha:"),
    ("Thanks for the meal.", "खानॅ खॅ शुक्रिया", "Kha:ne khə shukriya"),
    ("I am full.", "ब पेट भर", "B peṭ bhar"),
    ("Clear the plates.", "प्लॅट उठाव", "Pleṭ uṭha:v"),
    ("Who cooked today?", "आज कुस शिज?", "A:j kus shij?"),
]

_EXTRA_HOBBY: list[T] = [
    ("I learn music on weekends.", "छुट्टि मंज संगीत", "Chuṭṭi manz sangi:t"),
    ("She takes painting class.", "स च पॅंटिंग क्लास", "S cha peṇṭiṅg kla:s"),
    ("We practise dance on Tuesday.", "मंगल खॅ नाच", "Mangal khə na:ch"),
    ("The guitar lesson is at six.", "छॅ वख्त गिटार", "Chə vakht giṭa:r"),
    ("He joined yoga.", "सु योग मिल", "Su yog mil"),
    ("Pottery is relaxing.", "कुम्हारि आराम", "Kumha:ri a:ra:m"),
    ("I read poetry at night.", "रात शायरि", "Ra:t sha:yari"),
    ("Photography club meets Sunday.", "फोटो क्लब रविवार", "Fo:to klub ravi:va:r"),
    ("Swimming pool is nearby.", "तैराकि पास", "Taira:ki pa:s"),
    ("Chess tournament next month.", "अगलॅ महिनॅ शतरंज", "Agle mahine shatarañj"),
    ("Knitting calms the mind.", "बुन दिमाग शांत", "Bun dima:g sha:nt"),
    ("Calligraphy needs patience.", "कॅलिग्रॅफि सब्र", "Kæligrafi sabr"),
]

_EXTRA_COMMUNICATIVE: list[T] = [
    ("Repeat after me.", "मॅ पॅथ दोहराव", "Mə pəth dohra:v"),
    ("Say it slowly.", "हलुई उलाव", "Halui ula:v"),
    ("Use the new word in a sentence.", "नव शब्द वाक्य मंज", "Nav shabd va:ky manz"),
    ("Ask your partner a question.", "साथि खॅ सवाल", "Sa:thi khə sava:l"),
    ("Listen before you answer.", "जवाब पॅहलॅ आशुन", "Java:b pəhle a:shun"),
    ("Do not fear mistakes.", "गलति खॅ न डर", "Galati khə na ḍar"),
    ("Try role-play.", "रोल प्लॅ कर", "Rol ple kar"),
    ("Gesture helps meaning.", "इशारॅ सॅथ मतलब", "Isha:re səth matlab"),
    ("Picture prompts vocabulary.", "तस्वीर शब्द", "Tasvi:r shabd"),
    ("Pair work for five minutes.", "जोड़ि पाँच मिनट", "Jo:ṛi pa:ñch minaṭ"),
    ("Teacher models first.", "मॅश्टर पॅहलॅ", "Məshṭar pəhle"),
    ("Self-correction is welcome.", "खुद ठीक कर", "Khud thi:k kar"),
]

_EXTRA_PREP: list[T] = [
    ("The book is on the table.", "किताब मेज़ पॅथ", "Kita:b mez pəth"),
    ("I sit in the room.", "ब कमर मंज बस", "B kamar manz bas"),
    ("Water is in the jug.", "आब जग मंज", "A:b jag manz"),
    ("He stands near the door.", "स दरवाजॅ लागि", "S darva:ze la:gi"),
    ("We walk on the road.", "असि रस्त पॅथ चल", "Asi rast pəth chal"),
    ("Birds fly over the lake.", "झील पॅथ परिंद", "Jhi:l pəth parind"),
    ("Keys are under the pillow.", "तकियॅ तॅ चाबि", "Takiye tə cha:bi"),
    ("She comes from school.", "स स्कूल पॅथ", "S sku:l pəth"),
    ("They go to the market.", "तिम बाज़ार", "Tim ba:zar"),
    ("I wait for the bus.", "ब बस खॅ ठाह", "B bas khə Tha:h"),
    ("Tea with sugar.", "चाय चीनी सॅथ", "Cha:y chi:ni səth"),
    ("Without fear.", "बॅ डर", "Bə ḍar"),
]

_EXTRA_HEALTH_MORE: list[T] = [
    ("The cough is dry.", "खॅंस सुख", "Khə̃s sukh"),
    ("Allergic to dust.", "धुळ खॅ एलर्जि", "Dhuḷ khə elarji"),
    ("Blood pressure is high.", "ब्लॅड प्रॅशर उंच", "Bleḍ pre:shar unch"),
    ("Take rest for three days.", "त्रॅ दिन आराम", "Trə din a:ra:m"),
    ("The wound is healing.", "ज़ख्म भर", "Zakhm bhar"),
]

_EXTRA_READING: list[T] = [
    ("A kind word heals.", "नेक उलाव शिफा", "Nek ula:v shifa:"),
    ("Patience builds skill.", "सब्र सॅथ हुनर", "Sabr səth hunar"),
    ("Read one page daily.", "हर दिन एक पन्न", "Har din ek panna"),
    ("Stories teach culture.", "कहानि संस्कृति", "Kaha:ni sanskṛti"),
    ("Poetry rhymes softly.", "नज़़्म नर्म", "Nazm narm"),
    ("Quotes guide thought.", "फ़िक्रॅ हिदायत", "Fikre hida:yat"),
    ("Smile while you read.", "वाच हँस", "Va:ch hãs"),
    ("Share what you learned.", "शिकॅ वांट", "Shike va:nṭ"),
    ("Books are friends.", "किताब दोस्त", "Kita:b do:st"),
    ("Silence helps focus.", "शांत ध्यान", "Sha:nt dhya:n"),
    ("Write your summary.", "खुलास लिख", "Khula:s likh"),
    ("Discuss in the group.", "ग्रुप मंज बहस", "Grup manz bahas"),
]

# Assemble 22-row banks (primary bank only per chapter — no mixed generic pools)

KS_CONV_620 = _take(22, _tag("Diwali", list(DIWALI) + _EXTRA_DIWALI))

KS_CONV_621 = _take(22, _tag("Introduction", list(GREETINGS)))

KS_CONV_622 = _take(
    22,
    _tag(
        "Time",
        list(DAILY)
        + [
            ("We meet again at five.", "पॅंच बॅ फिर मिल", "Pəñch bə phir mil"),
        ],
    ),
)

KS_CONV_623 = _take(22, _tag("Place", list(QUESTIONS) + list(TRAVEL)))

KS_CONV_624 = _take(22, _tag("Hotel", _EXTRA_HOTEL + list(TRAVEL)))

KS_CONV_625 = _take(22, _tag("Weather", _EXTRA_WEATHER + list(DAILY)))

KS_CONV_626 = _take(22, _tag("Traffic police", _EXTRA_POLICE + list(TRAVEL)))

KS_CONV_627 = _take(22, _tag("Rickshaw or taxi", _EXTRA_RICKSHAW + list(TRAVEL)))

KS_CONV_628 = _take(22, _tag("Software work", _EXTRA_SOFTWARE + list(PRESENT)))

KS_CONV_629 = _take(22, _tag("Grocery shop", list(FOOD) + list(SHOPPING)))

KS_CONV_630 = _take(22, _tag("Doctor and patient", list(HEALTH) + _EXTRA_HEALTH_MORE))

KS_CONV_631 = _take(
    22,
    _tag(
        "Teacher and students",
        list(PRESENT)
        + [
            ("Open your books.", "किताब खोल", "Kita:b khol"),
            ("Write the homework.", "होमवर्क लिख", "Homvark likh"),
            ("Raise your hand.", "हाथ उठाव", "Ha:th uṭha:v"),
            ("Listen to the lesson.", "सबॅक आशुन", "Sabe:k a:shun"),
            ("Answer in Kashmiri.", "कॉशुर मंज जवाब", "Ko:shur manz java:b"),
        ],
    ),
)

KS_CONV_632 = _take(22, _tag("Phone chat", _EXTRA_PHONE + list(GREETINGS)))

KS_CONV_633 = _take(22, _tag("Vegetable market", list(FOOD) + list(SHOPPING)))

KS_CONV_634 = _take(22, _tag("Bus travel", list(TRAVEL) + list(DAILY)))

KS_CONV_635 = _take(22, _tag("Asking address", list(QUESTIONS) + list(TRAVEL)))

KS_CONV_636 = _take(22, _tag("Love and proposing", _EXTRA_LOVE + list(FAMILY)))

KS_CONV_637 = _take(22, _tag("Interview", _EXTRA_INTERVIEW + list(PRESENT)))

KS_CONV_638 = _take(22, _tag("With house help", _EXTRA_MAID + list(DAILY)))

KS_CONV_639 = _take(22, _tag("Aadhaar to mobile", _EXTRA_AADHAR_MOBILE + list(POSSESSION)))

KS_CONV_640 = _take(22, _tag("Mobile to Aadhaar", _EXTRA_MOBILE_AADHAR + list(POSSESSION)))

KS_CONV_641 = _take(22, _tag("Republic Day", list(REPUBLIC_DAY_DRILLS) + [
    ("We honour the tricolour.", "असि तिरंग इज़्ज़त", "Asi tirang izzat"),
    ("The parade inspires us.", "परेड प्रेरणा", "Pareḍ praerana:"),
    ("Children sing patriotic songs.", "लड़कि दॅशभक्त गीत", "La:r'ki deshabhakht gi:t"),
    ("Freedom is precious.", "आज़ादि अनमोल", "A:za:di anmol"),
    ("We remember the martyrs.", "असि शहीद याद", "Asi shahi:d ya:d"),
]))

KS_CONV_642 = _take(22, _tag("In the bank", _EXTRA_BANK + list(POSSESSION)))

KS_CONV_643 = _take(22, _tag("Temple visit", _EXTRA_TEMPLE + list(TRAVEL)))

KS_CONV_644 = _take(22, _tag("Lunch with parents", list(FAMILY) + list(FOOD)))

KS_CONV_645 = _take(22, _tag("Football match", _EXTRA_FOOTBALL + list(PRESENT)))

KS_CONV_646 = _take(22, _tag("Watching a movie", _EXTRA_MOVIE + list(DAILY)))

KS_CONV_647 = _take(22, _tag("Football World Cup", _EXTRA_WORLDCUP + list(PRESENT)))

KS_CONV_648 = _take(22, _tag("Tour guide", _EXTRA_TOUR + list(TRAVEL)))

KS_CONV_649 = _take(22, _tag("Bank language test", _EXTRA_BANK_TEST + list(PRESENT)))

KS_CONV_650 = _take(22, _tag("Food and meals", _EXTRA_FOOD_LUNCH + list(FOOD)))

KS_CONV_651 = _take(22, _tag("Hobby class", _EXTRA_HOBBY + list(PRESENT)))

KS_CONV_652 = _take(22, _tag("Miscellaneous useful", list(IDIOMS) + list(GREETINGS)))

KS_CONV_653 = _take(22, _tag("Miscellaneous useful 2", list(DAILY) + list(IDIOMS)))

KS_CONV_654 = _take(22, _tag("Communicative approach", _EXTRA_COMMUNICATIVE + list(GREETINGS)))

KS_CONV_655 = _take(22, _tag("Practice sentences", list(READING_DRILLS) + list(PRESENT)))

KS_CONV_656 = _take(22, _tag("Prepositions", _EXTRA_PREP + list(TRAVEL)))

KS_CONV_657 = _take(22, _tag("Jokes", list(JOKES_LIGHT_DRILLS) + [
    ("That was funny!", "हो आस मॊज़ेदार!", "Ho a:s mozeda:r!"),
    ("Tell another joke.", "बॅ लॅट सुनाव", "Bə ləṭ suna:v"),
    ("We laughed a lot.", "असि बॊहुत हँस", "Asi bohut hãs"),
    ("Comedy lifts the mood.", "कॉमॅडि मूड बरो", "Komeḍi mu:ḍ baro"),
    ("Do not take it seriously.", "सिरियस न", "Siriyas na"),
    ("Humour needs timing.", "लॅट वख्त", "Ləṭ vakht"),
    ("Smile at life.", "ज़िंदगि हँस", "Zindagi hãs"),
]))

KS_CONV_658 = _take(22, _tag("Reading — thoughts and quotes", _EXTRA_READING + list(IDIOMS)))

KS_CONV_659 = _take(22, _tag("Social media", list(SOCIAL_MEDIA_DRILLS) + list(DAILY)))

KS_CONV_660 = _take(22, _tag("Eclipse", list(ECLIPSE_DRILLS) + [
    ("NASA explains the path.", "नासा रास्त बयान", "Na:sa: ra:st baya:n"),
    ("Use certified glasses only.", "सिर्फ सॅर्टिफाइड चश्मॅ", "Sirf sərṭifaiḍ cashme"),
    ("Children watch with teachers.", "लड़कि मॅश्टर सॅथ", "La:r'ki məshṭar səth"),
    ("The moon covers the sun slowly.", "चन्द्र सूरज धीरॅ", "Chandra su:raj dhi:re"),
    ("Experts give safety tips.", "मॅहरि सुरक्षा सलाह", "Məhri suraksha sala:h"),
    ("Do not use ordinary sunglasses.", "आम चश्मॅ न", "A:m cashme na"),
]))

KS_CONV_661 = _take(22, _tag("Women's Day", list(WOMENS_DAY_DRILLS) + [
    ("Her courage inspires everyone.", "स हिम्मत सब", "S himmat sab"),
    ("Equal pay for equal work.", "बराबर काम बराबर मॅहनत", "Bara:bar ka:m bara:bar mehnat"),
    ("We celebrate her success.", "स कामयाबि मनाव", "S ka:ma:bi mana:v"),
    ("She leads our community.", "स अगुवाइ समुदाय", "S aguva:i samuda:y"),
    ("Her voice deserves respect.", "स आवाज़ इज़्ज़त", "S a:wa:z izzat"),
    ("Today we thank every woman.", "आज असि शुक्रिया ख़वातिन", "A:j asi shukriya khava:tin"),
    ("She works and studies both.", "स काम कर आ शिक", "S ka:m kar a shik"),
]))

KS_CONV_662 = _take(22, _tag("Quarrel at home", list(QUARREL_HOME_DRILLS) + [
    ("Why shout in the kitchen?", "रसोइ मंज क्या चिल्ल?", "Rasoi manz kya chilla?"),
    ("The neighbours will hear.", "पड़ोसि आश", "Paḍosi a:sh"),
    ("Let us drink water and cool down.", "आब पी ठंड", "A:b pi thaṇḍ"),
    ("I am sorry — I was wrong.", "माफ — ब गलत", "Ma:f — b galat"),
    ("Family peace matters most.", "कुटुंब अमन अख़ज़", "Kutumb aman akhaz"),
]))

L5_BANK_REGISTRY: dict[str, list[T]] = {
    "KS_CONV_620": KS_CONV_620,
    "KS_CONV_621": KS_CONV_621,
    "KS_CONV_622": KS_CONV_622,
    "KS_CONV_623": KS_CONV_623,
    "KS_CONV_624": KS_CONV_624,
    "KS_CONV_625": KS_CONV_625,
    "KS_CONV_626": KS_CONV_626,
    "KS_CONV_627": KS_CONV_627,
    "KS_CONV_628": KS_CONV_628,
    "KS_CONV_629": KS_CONV_629,
    "KS_CONV_630": KS_CONV_630,
    "KS_CONV_631": KS_CONV_631,
    "KS_CONV_632": KS_CONV_632,
    "KS_CONV_633": KS_CONV_633,
    "KS_CONV_634": KS_CONV_634,
    "KS_CONV_635": KS_CONV_635,
    "KS_CONV_636": KS_CONV_636,
    "KS_CONV_637": KS_CONV_637,
    "KS_CONV_638": KS_CONV_638,
    "KS_CONV_639": KS_CONV_639,
    "KS_CONV_640": KS_CONV_640,
    "KS_CONV_641": KS_CONV_641,
    "KS_CONV_642": KS_CONV_642,
    "KS_CONV_643": KS_CONV_643,
    "KS_CONV_644": KS_CONV_644,
    "KS_CONV_645": KS_CONV_645,
    "KS_CONV_646": KS_CONV_646,
    "KS_CONV_647": KS_CONV_647,
    "KS_CONV_648": KS_CONV_648,
    "KS_CONV_649": KS_CONV_649,
    "KS_CONV_650": KS_CONV_650,
    "KS_CONV_651": KS_CONV_651,
    "KS_CONV_652": KS_CONV_652,
    "KS_CONV_653": KS_CONV_653,
    "KS_CONV_654": KS_CONV_654,
    "KS_CONV_655": KS_CONV_655,
    "KS_CONV_656": KS_CONV_656,
    "KS_CONV_657": KS_CONV_657,
    "KS_CONV_658": KS_CONV_658,
    "KS_CONV_659": KS_CONV_659,
    "KS_CONV_660": KS_CONV_660,
    "KS_CONV_661": KS_CONV_661,
    "KS_CONV_662": KS_CONV_662,
}
