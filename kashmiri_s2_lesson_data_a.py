# -*- coding: utf-8 -*-
# Legacy: Kashmiri section 2 tables now use kashmiri_maithili_s2_pairs.py + _maithili_s2_english.json (see kashmiri_s2_data.py).
"""
Section 2.1–2.17 lesson rows (English, Kashmiri Devanagari, roman).
Aligned with O. N. Koul / Modern Kashmiri Grammar patterns; phrasebook checks (Wikivoyage, koshur.org).
"""
from __future__ import annotations

# Each value: list of (english, kashmiri_devanagari, roman) — 15 rows per lesson

DATA_A: dict[int, list[tuple[str, str, str]]] = {
    510: [
        (
            "When elders ask how I should be addressed in a formal introduction, I begin by giving my own name clearly and calmly.",
            "मे छु नाव …",
            "Ma chho naw …",
        ),
        (
            "If someone wants to know what people call you in daily speech, they may put this question to you in the middle of a polite chat.",
            "त्वहि क्या छु नाव?",
            "Twahi kyaa ch'u naav?",
        ),
        (
            "During a journey people often ask which town or village you regard as the place you originally come from.",
            "त्वहि कतिक छु?",
            "Tvahi katika chu?",
        ),
        (
            "Pointing at the wooden surface in front of us, we identify this object as the ordinary word speakers use for a table.",
            "यि चु मेज़",
            "yi chu me:z",
        ),
        (
            "Because the man wears a white coat, we whisper to each other, asking whether he is really a doctor or only a visitor.",
            "यि चा दक्तर?",
            "yi cha: da:ktar?",
        ),
        (
            "After watching him treat patients, everyone agrees that his profession is medicine and not some other trade.",
            "सु चु दक्तर",
            "su chu da:ktar",
        ),
        (
            "Describing a young woman, neighbours praise her appearance and her sharp mind in the same breath.",
            "स च ख़ूबसूरथ ती गाठिज कुड़",
            "s> cha khu:bsu:rath tI ga:Tij ku:r",
        ),
        (
            "While you explain a difficult rule, I lean forward and ask whether the sense of your words has reached my understanding.",
            "त्वहि छा फिकिरि तरान?",
            "Tvahi chaa phikiri taraan?",
        ),
        (
            "Once you repeat the sentence slowly, I nod and answer briefly that I have grasped what you intended to say.",
            "आऊई समझ",
            "Aaooee samajh",
        ),
        (
            "If the wording is still opaque, I admit honestly that I do not yet know the meaning you are trying to convey.",
            "ब’ छुस न’ ज़ानान ।",
            "Biu ch'us niu zaanaan",
        ),
        (
            "With the textbook open on the desk, you are the student who is actually doing the reading while others merely listen.",
            "त्स चुख किताब परान",
            "ts chukh kita:b para:n",
        ),
        (
            "Across the courtyard that respectable gentleman is the person everyone notices because he is absorbed in his book.",
            "सु चु किताब परान",
            "su chu kita:b para:n",
        ),
        (
            "The boy whose name appears first on the register is revising his lesson aloud in the corner of the room.",
            "असलाम चु किताब परान",
            "aslam chu kita:b para:n",
        ),
        (
            "Before the shops shut I hurry along the lane because I am on my way to the market to finish an errand.",
            "ब चुस बाज़ार गतशान",
            "b chus ba:zar gatsha:n",
        ),
        (
            "Peace be upon you.",
            "असलामु अलैकुम",
            "Assalām ‘alaikum",
        ),
    ],
    511: [
        (
            "When we speak politely about an elder’s journey, we say that he will travel to the capital for work.",
            "तोह गत्शिव दिलि",
            "toh' gAtshiv dili",
        ),
        (
            "Introducing him with full respect, we explain that he practises law and argues cases in the high court.",
            "हुम चि वकील",
            "hum chi vaki:l",
        ),
        (
            "Stressing his roots, we add that he belongs to the Kashmiri speech community and speaks the valley language at home.",
            "तिम चि कॅशिर",
            "tim chi kə:śir",
        ),
        (
            "In the clinic corridor we address the physician politely, telling him that we know he serves as a doctor here.",
            "तोह चिव दक्तर",
            "toh' chiv da:ktar",
        ),
        (
            "At lunchtime we ask respectfully whether he is eating his meal now or waiting for someone to join him.",
            "तोह चिव बात खेवान",
            "toh' chiv bat kheva:n",
        ),
        (
            "We enquire, using the same honorific frame, whether he is studying from a book or only skimming notes.",
            "त्स चुख किताब परान",
            "ts chukh kita:b para:n",
        ),
        (
            "A courteous greeting after a long absence asks after your health while the verb shows plural agreement on the addressee.",
            "तोहय छिवा वारय?",
            "Tohy ch'ivaa vaarai?",
        ),
        (
            "Because beginners cannot follow rapid speech, we beg you to slow your words and repeat each phrase gently.",
            "तोहय हेकिवा वार’ वार’ वॅनिव ।",
            "Tohy hekivaa vaariu vaariu veuniv",
        ),
        (
            "Meeting someone for the first time, we ask what name we ought to use when we speak to you in public.",
            "त्वहि क्या छु नाव?",
            "Twahi kyaa ch'u naav?",
        ),
        (
            "We ask which place you count as your home town so that we can place your story on the mental map of the valley.",
            "त्वहि कतिक छु?",
            "Tvahi katika chu?",
        ),
        (
            "When a stranger enters the room, we say sincerely that we are glad to see him after such a long separation.",
            "मे सप’ज़ खोशी त्वहि मीलिध ।",
            "Me sapiuz k'oshee twahu meelit'",
        ),
        (
            "Watching the gentleman reach for the bill, we predict that he himself will settle the entire account for the table.",
            "ये मर्द दी सॅर्सि हत्र पोंस",
            "Ye mard dee saersi hatra pons",
        ),
        (
            "To a man we ask how often he walks through this neighbourhood when he returns from his office in the evening.",
            "चे छुक यिवान योर वरिया?",
            "Che chhuk yiwan yor variya?",
        ),
        (
            "We put the same question to a woman, letting the verb show feminine agreement while the sense stays identical.",
            "चे छिक यिवान योर वरिया?",
            "Che chhik yiwan yor variya?",
        ),
        (
            "Ordinary third-person narration keeps singular agreement on the verb, which differs from the honorific plural pattern with tim.",
            "सु चु किताब परान",
            "su chu kita:b para:n",
        ),
    ],
    512: [
        (
            "The finite verb shows that he is completely absorbed in reading the textbook while the room around him grows quiet.",
            "सु चु किताब परान",
            "su chu kita:b para:n",
        ),
        (
            "Motion toward the market is expressed with the same imperfective shape that marks ongoing movement on foot.",
            "ब चुस बाज़ार गतशान",
            "b chus ba:zar gatsha:n",
        ),
        (
            "Second-person agreement on the auxiliary tells us plainly that you are the one who holds the book and reads it aloud.",
            "त्स चुख किताब परान",
            "ts chukh kita:b para:n",
        ),
        (
            "He lifts the cup again and again while others wait, because sipping tea is what he is doing at this moment.",
            "सु चु चाय चेवान",
            "su chu ca:y ceva:n",
        ),
        (
            "She mirrors his action politely, using feminine agreement to show that she too is drinking tea in the same way.",
            "स च चाय चेवान",
            "s cha ca:y ceva:n",
        ),
        (
            "Past motion followed by the infinitive ‘to see’ expresses purpose when we say that he went to watch the play.",
            "सु गव नाटख वुचिनि",
            "su gav na:Takh vuchini",
        ),
        (
            "The postposition khA:trI can spell ‘for the sake of seeing’ when it follows the infinitive after a verb of going.",
            "सु गव नाटख वुच्नी खात्री",
            "su gav na:Takh vuchnI khA:trI",
        ),
        (
            "The causative complex with von takes a dative causee and the infinitive of reading when I tell him to study.",
            "मे वन तामिस किताब परनी खात्री",
            "me von tAmis kita:b parnI khA:trI",
        ),
        (
            "Manner adverbs pile up before the verb when Aslam explains a point while smiling in a slow, reassuring way.",
            "असलाम चु असान असान कथी करान",
            "aslam chu asa:n asa:n kathI kara:n",
        ),
        (
            "A bare imperative built on kar closes the door at once when cold air is rushing through the passage.",
            "दरवाज़ी कर बंद",
            "darva:zI kar band",
        ),
        (
            "The proverb tells the child to act exactly in the way the elder’s words prescribe, neither more nor less.",
            "यिथीकिं बि वनय तिथीकिं कर",
            "yithIkIn' bI vanay tithIkIn' kar",
        ),
        (
            "Reduplication of the converb stresses manner when he arrived breathless from running hard along the lane.",
            "सु आव दोरान दोरान",
            "su a:v do:ra:n do:ra:n",
        ),
        (
            "The same device with weeping shows that he came all the way in tears without hiding his grief.",
            "सु आव वदान वदान",
            "su a:v vada:n vada:n",
        ),
        (
            "Two completed events line up in sequence when we say that he reached home and only then telephoned his friend.",
            "गरी वातिथ कर तमि टेलिफ़ोन",
            "garI vA:tith kor tami Teli:pho:n",
        ),
        (
            "The future stem attached to the first person promises eating when the meal is finally set on the cloth.",
            "बि खामि बाति",
            "bi kh'ami bati",
        ),
    ],
    513: [
        (
            "On ordinary days I never even open the newspaper because I dislike the noise of political headlines.",
            "बि चुस नी अख़बार परान",
            "bI chus nI akhba:r para:n",
        ),
        (
            "Illiteracy blocks him so completely that he cannot decipher letters, and people describe him as unschooled.",
            "सु हेकि नी पारिथ तिकाज़ि सु चु मुड़ी",
            "su heki nI pArith tik'a:zi su chu muDI",
        ),
        (
            "Cause precedes result in the explanation that because he never attended school he still cannot read a line.",
            "तिकाज़ि सु चु मुड़ी सु हेकि नी पारिथ",
            "tik'a:zi su chu muDI su heki nI pArith",
        ),
        (
            "Right now Aslam is in the middle of a chapter, for the simple present marks what he is habitually doing here.",
            "असलाम चु किताब परान",
            "aslam chu kita:b para:n",
        ),
        (
            "The boy we mean is the one who keeps reading aloud while the teacher paces behind the benches.",
            "सु चु किताब परान",
            "su chu kita:b para:n",
        ),
        (
            "While we talk I am walking toward the bazaar because the simple present can carry progressive motion.",
            "ब चुस बाज़ार गतशान",
            "b chus ba:zar gatsha:n",
        ),
        (
            "You keep turning pages as part of your lesson, and the auxiliary shows that the activity is ongoing.",
            "त्स चुख किताब परान",
            "ts chukh kita:b para:n",
        ),
        (
            "Location negation tells us that the laundry is not lying on the table where the host expected it.",
            "पलव चिनी मेज़स पेठ",
            "palav chinI me:zas peTh",
        ),
        (
            "We ask whether English is a language you use habitually in your office or only when outsiders appear.",
            "तोहय छिवा अंगरीज़ी बोलान?",
            "Tohy chivā angrīzī bolān",
        ),
        (
            "We check whether Koshur is still spoken in your home alongside Urdu or another household language.",
            "त्स्के छुके कॉशुर बोलान?",
            "Tske chhuke Koshur bolaan?",
        ),
        (
            "I signal agreement with a short formula when I want to say that I have followed every word of your advice.",
            "आऊई समझ",
            "Aaooee samajh",
        ),
        (
            "A male speaker denies comprehension with ni plus the imperfective of knowing when the text is too hard.",
            "ब’ छुस न’ ज़ानान ।",
            "Biu ch'us niu zaanaan",
        ),
        (
            "Pointing at an unfamiliar object, we ask what it could be called in ordinary Kashmiri speech.",
            "यि क्या छु?",
            "Yi Kyāh chu?",
        ),
        (
            "Before we bargain we need the price, so we ask how costly this cloth is in today’s market.",
            "यि का’तिस छु?",
            "Yi keūtis ch'u",
        ),
        (
            "A proverb reminds learners that mastering a language takes more than a single tongue learned by rote.",
            "अख़ ज़बान छु न ज़न्ह काफ़ी",
            "Akh zabaan chhu na zanh kaefi",
        ),
    ],
    514: [
        (
            "We identify the flat wooden surface in the middle of the room as a table, using the copula with a nominal predicate.",
            "यि चु मेज़",
            "yi chu me:z",
        ),
        (
            "The yes–no question with cha: asks whether the profession we guess at is really medicine or something else.",
            "यि चा दक्तर?",
            "yi cha: da:ktar?",
        ),
        (
            "Once the answer is given, we state plainly that his occupation is that of a physician trusted in the valley.",
            "सु चु दक्तर",
            "su chu da:ktar",
        ),
        (
            "Two stacked adjectives praise her appearance and her intelligence when we describe a clever young woman.",
            "स च ख़ूबसूरथ ती गाठिज कुड़",
            "s> cha khu:bsu:rath tI ga:Tij ku:r",
        ),
        (
            "The copula can anchor progressive reading, showing that ‘to be’ links the subject to an activity and not only to a noun.",
            "सु चु किताब परान",
            "su chu kita:b para:n",
        ),
        (
            "The named subject Aslam is the student who is reading, illustrating how proper nouns pattern like ‘he’.",
            "असलाम चु किताब परान",
            "aslam chu kita:b para:n",
        ),
        (
            "Stative height is predicated of her alone when we say that she is tall beside her classmates.",
            "स च ज़ीत",
            "s cha zi:t",
        ),
        (
            "A polite inquiry after health uses plural agreement on the addressee even when only one person stands before you.",
            "तोहय छिवा वारय?",
            "Tohy ch'ivaa vaarai?",
        ),
        (
            "We ask what label people attach to you when they introduce you in a meeting or on a form.",
            "त्वहि क्या छु नाव?",
            "Twahi kyaa ch'u naav?",
        ),
        (
            "Self-introduction opens with me chho naw and then supplies the name that friends actually use.",
            "मे छु नाव …",
            "Ma chho naw …",
        ),
        (
            "The question of origin asks which place you call home when you have lived in several towns.",
            "त्वहि कतिक छु?",
            "Tvahi katika chu?",
        ),
        (
            "The same copula carries progressive motion when I say that I am on the road to the market.",
            "ब चुस बाज़ार गतशान",
            "b chus ba:zar gatsha:n",
        ),
        (
            "You are the student whose book lies open, so second-person agreement ties the auxiliary to the reader.",
            "त्स चुख किताब परान",
            "ts chukh kita:b para:n",
        ),
        (
            "Present activity of sipping links the copula to an imperfective verb when he drinks tea during the break.",
            "सु चु चाय चेवान",
            "su chu ca:y ceva:n",
        ),
        (
            "We test whether my long explanation has gone through by asking if the thread of the argument is clear.",
            "त्वहि छा फिकिरि तरान?",
            "Tvahi chaa phikiri taraan?",
        ),
    ],
    515: [
        (
            "At this exact moment he is mid-page in the lesson, which shows how present continuous marks ongoing study.",
            "सु चु किताब परान",
            "su chu kita:b para:n",
        ),
        (
            "Aslam’s voice is steady because he is still reading the passage that the teacher assigned this morning.",
            "असलाम चु किताब परान",
            "aslam chu kita:b para:n",
        ),
        (
            "While we converse I am still walking toward the bazaar, so my motion overlaps with our talk.",
            "ब चुस बाज़ार गतशान",
            "b chus ba:zar gatsha:n",
        ),
        (
            "Your eyes stay on the printed page, which tells everyone that you are the reader we are waiting for.",
            "त्स चुख किताब परान",
            "ts chukh kita:b para:n",
        ),
        (
            "He keeps lifting the cup because drinking tea is precisely what he is doing instead of joining the debate.",
            "सु चु चाय चेवान",
            "su chu ca:y ceva:n",
        ),
        (
            "She mirrors him politely, and feminine agreement shows that she too is sipping tea in the same frame.",
            "स च चाय चेवान",
            "s cha ca:y ceva:n",
        ),
        (
            "Speech overlaps with a smile when Aslam explains gently, reduplicating manner adverbs before the verb.",
            "असलाम चु असान असान कथी करान",
            "aslam chu asa:n asa:n kathI kara:n",
        ),
        (
            "Long walking exhausts the traveller until step after step he tires and sits down on the stone seat.",
            "पकान पकान थोक सु ती बुठ पथर",
            "paka:n paka:n thok su tI bu':Th pathar",
        ),
        (
            "Meanwhile I keep stirring my tea while the argument at the other table grows louder and sharper.",
            "ब चुस चाय चेवान",
            "b chus ca:y ceva:n",
        ),
        (
            "Because he cannot read letters, people class him as unschooled even though he is quick with numbers.",
            "सु चु मुड़ी",
            "su chu muDI",
        ),
        (
            "Stative height sits beside activity when we say that she is tall and standing quietly by the door.",
            "स च ज़ीत",
            "s cha zi:t",
        ),
        (
            "His profession forms the background while we stress how often he is called to the clinic at night.",
            "सु चु दक्तर",
            "su chu da:ktar",
        ),
        (
            "Parallel motion repeats when I insist that I am still on the way to shop though the rain has begun.",
            "ब चुस बाज़ार गतशान",
            "b chus ba:zar gatsha:n",
        ),
        (
            "You are visibly engaged with the page, which is why the teacher leaves you undisturbed for a while.",
            "त्स चुख किताब परान",
            "ts chukh kita:b para:n",
        ),
        (
            "We check whether my explanation is getting across or whether I should rephrase the rule once more.",
            "त्वहि छा फिकिरि तरान?",
            "Tvahi chaa phikiri taraan?",
        ),
        (
            "Guests who step across the threshold are greeted with this short word of welcome while tea is being poured.",
            "वलिव",
            "Waliv",
        ),
    ],
    516: [
        (
            "The ticket is already booked, so we tell you politely that you will travel to Delhi on the night train.",
            "तोह गत्शिव दिलि",
            "toh' gAtshiv dili",
        ),
        (
            "The summer syllabus lists ten heavy volumes that you will finish before the examination week arrives.",
            "चि परख दाह किताबी",
            "tsI parakh dAh kita:bI",
        ),
        (
            "Our plan for the evening is fixed: you will sit through an entire film without leaving for tea.",
            "चि वुचख फ़िलिम",
            "tsI vuchakh philim",
        ),
        (
            "Object fronting stresses the pile of books when we say that those ten volumes—you will read every one.",
            "दाह किताबी परख",
            "dAh kita:bI parakh",
        ),
        (
            "The same device shifts attention to the screen when we announce that the film—you will watch it carefully.",
            "फ़िलिम वुचख",
            "philim vuchakh",
        ),
        (
            "We add a condition on meeting: come early tomorrow or I will leave alone without waiting at the gate.",
            "पगाह यिजि जलीद नति गत्शी बि कुनुय ज़ोन",
            "paga:h yizi jalId natI gatshI bI kunuy zon",
        ),
        (
            "Farmers say that if the monsoon rain falls in time, then the harvest in the fields will turn out well.",
            "अगर रूद पेयि, तेली बनि जान फसल",
            "agar ru:d peyi, teli bani ja:n phasIl",
        ),
        (
            "Reversing the clauses keeps the same meaning: a good crop depends on whether the rain arrives as hoped.",
            "तेली बनि जान फसल अगर रूद पेयि",
            "teli bani ja:n phasal agar ru:d peyi",
        ),
        (
            "After the quarrel nobody will open a conversation with him, which shows how a social freeze works.",
            "तामिस सीथ करि नी काह कथ",
            "tAmis sI:th' kari nI ka:~h kath",
        ),
        (
            "Betrayal means that he will offer his friends no help at all when they need him most.",
            "सु करि नी दोस्तन हिंदि खात्रि केह",
            "su kari nI do:stan hIndi khA:trI ke~h",
        ),
        (
            "When the food finally reaches the table I will eat my fill because hunger has been gnawing for hours.",
            "बि खामि बाति",
            "bi kh'ami bati",
        ),
        (
            "The job contract states that I will live in Delhi for a year, so my address will change completely.",
            "बि रोज़ि दिलि",
            "bi ro:zi dili",
        ),
        (
            "Visa trouble means I am not free to go to Delhi even though the invitation has already arrived.",
            "ब हेक न दिलि गतशिथ",
            "b hek n dili gətshith",
        ),
        (
            "Out of courtesy I will set out only after he has left, so our paths do not cross on the narrow stair.",
            "तामिसिंदि नेरनी पति गत्शी बि",
            "tAm'sIndi ne:rnI patI gatshI bI",
        ),
        (
            "At the bus station we ask which bay the coach uses because the crowd hides the signboard.",
            "बस कति पॅथि छि नेरान?",
            "Bas kati pêţhė chi nerān?",
        ),
    ],
    517: [
        (
            "This time next year he will still be drafting chapters, which illustrates progressive action stretching into the future.",
            "सु आसि किताब लेखान",
            "su a:si kita:b le:kha:n",
        ),
        (
            "Across tenses we can say that Salim is, was, or will be coached, framing teaching around one student.",
            "सु चु/ओस/आसि सलीमस परिनावान",
            "su chu/o:s/a:si sAli:mas parIna:va:n",
        ),
        (
            "The simple future still promises the same journey when we insist that you will certainly reach Delhi.",
            "तोह गत्शिव दिलि",
            "toh' gAtshiv dili",
        ),
        (
            "Coursework piles up, and we warn that you will still be reading those ten books when the season ends.",
            "चि परख दाह किताबी",
            "tsI parakh dAh kita:bI",
        ),
        (
            "Cinema night means you will be sitting through the screening until the credits finish rolling.",
            "चि वुचख फ़िलिम",
            "tsI vuchakh philim",
        ),
        (
            "When the dinner bell rings I will be eating because the progressive future overlaps with the call.",
            "बि खामि बाति",
            "bi kh'ami bati",
        ),
        (
            "During that posting I will be living in Delhi, so my mornings will belong to a different skyline.",
            "बि रोज़ि दिलि",
            "bi ro:zi dili",
        ),
        (
            "Be punctual tomorrow or you will find that I am leaving alone while the lane is still dark.",
            "पगाह यिजि जलीद नति गत्शी बि कुनुय ज़ोन",
            "paga:h yizi jalId natI gatshI bI kunuy zon",
        ),
        (
            "If the rain arrives on time, the fields will be turning green while we watch from the veranda.",
            "अगर रूद पेयि, तेली बनि जान फसल",
            "agar ru:d peyi, teli bani ja:n phasIl",
        ),
        (
            "People will be avoiding him entirely after the rumour spreads, which shows a drawn-out social reaction.",
            "तामिस सीथ करि नी काह कथ",
            "tAmis sI:th' kari nI ka:~h kath",
        ),
        (
            "He will be offering his friends no support at all, and the future continuous underlines the stubborn refusal.",
            "सु करि नी दोस्तन हिंदि खात्रि केह",
            "su kari nI do:stan hIndi khA:trI ke~h",
        ),
        (
            "We ask from which bay the bus will be pulling out when the platform is crowded with travellers.",
            "बस कति पॅथि छि नेरान?",
            "Bas kati pêţhė chi nerān?",
        ),
        (
            "Glancing at the watch, we wonder what hour the station clock will be showing when we arrive.",
            "वखेत क्या आव?",
            "Vakhėt kyāh āv?",
        ),
        (
            "While prices are still discussed in the present, we bargain knowing that tomorrow they may change.",
            "यि का’तिस छु?",
            "Yi keūtis ch'u",
        ),
        (
            "We ask whether Koshur will still be spoken in that meeting when guests from outside join the table.",
            "त्स्के छुके कॉशुर बोलान?",
            "Tske chhuke Koshur bolaan?",
        ),
    ],
    518: [
        (
            "We look back at the diary and ask whether his train actually arrived on the previous evening as planned.",
            "सु आवा रात?",
            "su a:va: ra:th",
        ),
        (
            "The statement plus tag settles the fact: he reached Delhi, and we treat that journey as closed.",
            "सु गव दिलि, गव ना?",
            "su gav dili, gav na:",
        ),
        (
            "Coordinated motion tells how I travelled to Delhi while my companion came along without a separate ticket.",
            "बि गोस दिलि ती म्योन दोस गव जोम",
            "bI go:s dili tI m'o:n do:s gav jom",
        ),
        (
            "Pleasant weather yesterday explains why I strolled outside instead of staying beside the stove.",
            "रात ओस जान मुसिम, अमि किं गोस बि चक्रस",
            "ra:th o:s ja:n mu:sim, ami kin' go:s bI cakras",
        ),
        (
            "Today’s oppressive warmth kept me from the bazaar because stepping into the sun felt unbearable.",
            "तिकाज़ि अज़ ओस गरिम अमिकिं गोस नी बि बाज़ार",
            "tik'a:zi az o:s garIm amikin' go:s nI bI ba:zar",
        ),
        (
            "Sheila’s journal shows that she did not visit any place at all yesterday evening when the curfew began.",
            "शीला गायि नी कुन रात",
            "shi:lI gAyi nI kun ra:th",
        ),
        (
            "The manner converb stresses how he entered while running hard, as if someone were chasing him.",
            "सु आव दोरान दोरान",
            "su a:v do:ra:n do:ra:n",
        ),
        (
            "The same pattern with weeping paints his arrival as an event framed by tears and silence.",
            "सु आव वदान वदान",
            "su a:v vada:n vada:n",
        ),
        (
            "I waited so long on the veranda that patience itself wore thin and I began to pace.",
            "बि आस प्रार प्रार तंग",
            "bI a:s prA:r' prA:r' tang",
        ),
        (
            "A WH-question on time asks at what moment you set out for the market before the shops closed.",
            "तोह कर गायिवी बाज़ार?",
            "toh' kar gAyivI ba:zar",
        ),
        (
            "The simple past of going appears when we report that he left for Delhi on business last week.",
            "सु गव दिलि",
            "su gav dili",
        ),
        (
            "I too completed the same journey without stopping elsewhere because the deadline was tight.",
            "बि गोस दिलि",
            "bI go:s dili",
        ),
        (
            "After the show ended he went simply to watch the drama, using the infinitive to spell his purpose.",
            "सु गव नाटख वुचिनि",
            "su gav na:Takh vuchini",
        ),
        (
            "Purpose is marked with khA:trI when we say that he travelled for the sake of seeing the play.",
            "सु गव नाटख वुच्नी खात्री",
            "su gav na:Takh vuchnI khA:trI",
        ),
        (
            "Flooding blocked the lane so completely that nobody from that hamlet could reach the city gate.",
            "तोर आव नी गतशनी",
            "to:r a:v nI gatshnI",
        ),
    ],
    519: [
        (
            "He drank tea only after he had skimmed the headlines, which orders two completed events in time.",
            "ताम चेयि चाय अख़बार पारिथ",
            "tAm' ceyi ca:y akhba:r pArith",
        ),
        (
            "From the chair he put a difficult question to the gathering while everyone leaned forward to listen.",
            "ताम प्रुत्श कुर्सी पेठ बिहिथ",
            "tAm' prutsh kursii peTh bihith",
        ),
        (
            "He broke down in tears while seated on the cot, and the ergative subject marks him as agent of weeping.",
            "ताम वोद कुर्सी पेठ बिहिथ",
            "tAm' vod kursii peTh bihith",
        ),
        (
            "Mohan wrote a letter and sent it to Radha, and the verb shape shows transitive past agreement.",
            "मोहनन लिच रादायि चिठ’",
            "mohnan li:ch ra:da:yi ciTh’",
        ),
        (
            "During the quarrel Mohan struck Salim with a stick, and the instrumental postposition names the means.",
            "मोहनन लोय सलीमस लोरी सीथ’",
            "mohnan lo:y sAli:mas lo:ri sI:t’",
        ),
        (
            "I told him plainly to read the book for the examination, using von with the dative and the infinitive.",
            "मे वन तामिस किताब परनी खात्री",
            "me von tAmis kita:b parnI khA:trI",
        ),
        (
            "The book was not read at all, and the passive-style wording keeps the volume itself in focus.",
            "किताब आयि नी परनी",
            "kita:b a:yi nI parnI",
        ),
        (
            "Shock sealed his throat until he could not speak a single coherent sentence in reply.",
            "ताम हेक नी कथ कारिथ",
            "tAm' hec nI kath kArith",
        ),
        (
            "His legs failed him on the slope, so he could not walk the steep lane to the shrine.",
            "सु होक नी पाकिथ",
            "su h'ok nI pAkith",
        ),
        (
            "He has never written a letter in his life, not even to a cousin who lives one house away.",
            "ताम चनि ज़ाह ज़िन्दगी मंज़ चिठ लिचमित्स",
            "tAm' chanI za:~h zindgi: manz ciTh' li:chmIts",
        ),
        (
            "After she reached home she rang him on the telephone, chaining two perfect events in order.",
            "गरी वातिथ कर तमि टेलिफ़ोन",
            "garI vA:tith kor tami Teli:pho:n",
        ),
        (
            "Someone else in the family wrote to Radha, which appears in the passive agreement on the letter.",
            "रादायि आयि चिठ लेखनी",
            "ra:da:yi a:yi ciTh' le:khnI",
        ),
        (
            "Salim was beaten with a stick, and the verb agrees with the sufferer while the stick names the instrument.",
            "सलीमस आव लायनी लोरी सीथ’",
            "sAli:mas a:v la:ynI lo:ri sI:t'",
        ),
        (
            "I read the book in one sitting, and first-person agreement reflects the feminine object kita:b.",
            "मे पारिथ किताब",
            "me pArith kita:b",
        ),
        (
            "When he pressed me at the door I did not give him the book because I still needed it myself.",
            "मे दित्सनस तामिस किताब",
            "me ditsnas tAmis kita:b",
        ),
        (
            "In front of the whole class Mohan handed Salim a pen so that he could copy the passage neatly.",
            "मोहनन दुट सलीमस कलम",
            "mohnan d'ut sAli:mas kalam",
        ),
    ],
}
