# -*- coding: utf-8 -*-
"""
Full EKT rows (short English gloss, Kashmiri Devanagari, roman) for lessons where tables
were corrupted. English column is expanded at apply time via long_english().

Sources: Omniglot Kashmiri phrases, Wikivoyage phrasebook, festival lines (web).
"""
from __future__ import annotations

# lesson_id -> list of [short_english, kashmiri, roman]  (same order as data_maithili.json EMT)
LESSON_ROWS: dict[int, list[list[str]]] = {
    620: [
        [
            "Happy Diwali",
            "तोहि छुव दीवाली हुंज़ हत हत मुबारक",
            "Tohi chuv Diwaali hunz hath hath mubaarak",
        ],
        [
            "Happy Diwali to you",
            "तुहुंद दीवाली मुबारक",
            "Tuhund diwaali mubaarak",
        ],
        [
            "Let's light lamps",
            "आव दियां जलाव",
            "Aav diyaan jalaav",
        ],
        [
            "Diwali is a festival of lights",
            "दीवाली छु रोशनी हुंद त्योहार",
            "Diwaali chhu rooshani hund tayaar",
        ],
        [
            "We celebrate Diwali",
            "असि छि दीवाली मनावुन",
            "Asi chi diwaali manaavun",
        ],
        [
            "Clean the house before Diwali",
            "दीवाली पॅथ कर साफ कर",
            "Diwaali paeth kar saaf kar",
        ],
        [
            "Exchange sweets",
            "मिठाई बदलाव",
            "Mithaai badalaav",
        ],
        [
            "Worship Lakshmi",
            "लक्ष्मी पूजा कर",
            "Lakshmi puja kar",
        ],
        [
            "May prosperity come",
            "धन आव",
            "Dhan aav",
        ],
        [
            "Happy New Year",
            "नवरेह मुबारक",
            "Navreh mubaarak",
        ],
        [
            "Burn crackers",
            "पटाख जलाव",
            "Paataakh jalaav",
        ],
        [
            "Decorate the house",
            "कर सजाव",
            "Kar sajaa",
        ],
        [
            "Visit relatives",
            "रिश्तेदारन मंज गच्छ",
            "Rishtedaaran manz gachh",
        ],
        [
            "Give gifts",
            "तोहफ दियाव",
            "Tohaf diyaav",
        ],
        [
            "Enjoy the festival",
            "त्योहार मनाव कर मज़ कर",
            "Tayaar manaav kar maz kar",
        ],
        [
            "May your home shine with lamps and joy",
            "तुहुंद कर मंज दियां रोशन",
            "Tuhund kar manz diyaan roshan",
        ],
        [
            "Peace and happiness on Diwali to everyone",
            "दीवाली पॅथ सबन खातिर अमन",
            "Diwaali paeth saban khatir aman",
        ],
        [
            "Warm wishes for a bright festival",
            "रोशन त्योहार खातिर गरम मुबारक",
            "Roshan tayaar khatir garam mubaarak",
        ],
    ],
    621: [
        ["Hello", "नमस्कार", "Namaskaar"],
        ["Good morning", "सुबह बखैर", "Subah bakhair"],
        ["Good afternoon", "दोपहर हुंद सलाम", "Dopahar hund salaam"],
        ["Good evening", "शाम हुंद सलाम", "Shaam hund salaam"],
        ["Good night", "शबे खैर", "Shabey k'eūr"],
        ["What is your name?", "त्वहि क्या छु नाव?", "Twahi kyaa ch'u naav?"],
        ["My name is Rahul", "मे छु नाव राहुल", "Me chhu naav Ra:hul"],
        ["Nice to meet you", "मे सप’ज़ खोशी त्वहि मीलिध", "Me sapiuz k'oshee twahu meelit'"],
        ["How are you?", "तोहय छिवा वारय?", "Tohy ch'ivaa vaarai?"],
        ["I am fine", "मे छु ठीक", "Me chhu thi:k"],
        ["Where do you live?", "त्वहि कतिक छु?", "Tvahi katika chu?"],
        ["I live in Patna", "मे पटना मंज राम", "Me Pat'naa manz raam"],
        ["What do you do?", "त्वहि क्या करान छु?", "Tvahi kyaa karaan chu?"],
        ["I am a teacher", "मे छु मास्टर", "Me chhu ma:star"],
        ["Please sit", "मेहरबॅानी कर बॅजिव", "Meharbeūnee kar bejiv"],
        ["Thank you", "शुकिया", "Shukriya"],
        ["You're welcome", "किहीन छु नॅ परवाइ", "Kiheen chhu ne parvaai"],
        ["Welcome", "वलिव", "Waliv"],
        ["Hello (formal)", "आदाब", "Aadaab"],
        ["Long time no see", "वरिया काल गव न म्येलनसि", "Variya kaal gov na myelnasi"],
        [
            "Please speak more slowly",
            "तोहय हेकिवा वार’ वार’ वॅनिव",
            "Tohy hekivaa vaariu vaariu veuniv",
        ],
        ["Please say that again", "तोहय हेकिवा दुबार’ वॅनिथ", "Tohy hekivaa dubaariu veunit'"],
        ["Please write it down", "यि लिखिव", "Yi Likhiv"],
        ["Do you speak English?", "तोहय छिवा अंगरीज़ी बोलान?", "Tohy chivā angrīzī bolān"],
        ["Do you speak Kashmiri?", "त्स्के छुके कॉशुर बोलान?", "Tske chhuke Koshur bolaan?"],
        ["Yes a little", "आ, थोडा स", "Aa, thoḍaa sa"],
        ["I don't understand", "ब’ छुस न’ ज़ानान", "Biu ch'us niu zaanaan"],
        ["How much is this?", "यि का’तिस छु?", "Yi keūtis ch'u"],
        ["Where is the toilet?", "टायलेट कति छि?", "Ṭaaylet kati ch'u!"],
        ["Help!", "मदथ करिव!", "Madatha kariva!"],
        ["Stop!", "ठहर!", "Ṭeuhar!"],
        ["Call the police!", "बुलॅाविव पुलीस!", "Buleūviv pulees!"],
        ["Fire!", "नार!", "Naar!"],
        ["Get well soon", "गचिव ठीक जल्द", "Gachiv theek jald"],
        ["Leave me alone!", "चॅ कर मॅ कुनिज़ोन!", "Che tra mae kunizon!"],
        ["I miss you", "मे छु च्यों याद यिवान", "Me chhu chyon yaad yiwaan"],
        ["Have a nice meal", "कान वान मज़ कर", "Kaan vaan maz kar"],
        [
            "Bon voyage",
            "नैर ख़ौदायस हवाल",
            "Nair khaudaayas havaal",
        ],
        ["Cheers! Good health!", "ज़ुव थवुन ठीक", "Zuv thavun theek"],
        ["Birthday greetings", "त्स्के छुय वोहुरवोद मुबारक", "Tske chhuy wohurwod mubarak"],
        ["Christmas greetings", "नवरेह मुबारक", "Navreh mubaarak"],
        [
            "Speak to me in Kashmiri",
            "चॅ कर मॅ साथ कॅशिर पॅथ कथ",
            "Che kar mae seath kashir peth kath",
        ],
        [
            "How do you say ... in Kashmiri?",
            "... उस किथ पॅथ छॅ दपान कॅशिर मंज?",
            "... us kith paeth chhe dapaan kashir manz?",
        ],
        ["What is your name? (alt)", "तुहुंद नाव क्या हज़ छु?", "Tuhund naw kyah haz chu?"],
        ["My name is...", "मे छु नाव …", "Ma chho naw …"],
        ["I am fine (thik)", "मे छु ठीक", "Me chhu thi:k"],
        [
            "Pleased to meet you",
            "मे सप’ज़ खोशी त्वहि मीलिध",
            "Me sapiuz k'oshee twahu meelit'",
        ],
        ["Where are you from?", "त्वहि कतिक छु?", "Tvahi katika chu?"],
        ["I'm from...", "ब’ छुस ... रोज़ां", "Biu ch'us ... rozaan"],
        ["Goodbye (informal)", "खुदा हाफिज़", "Khuda hāfiz"],
        ["Yes (formal)", "आ", "Aa"],
        ["No (nai)", "ना", "Na"],
    ],
}
