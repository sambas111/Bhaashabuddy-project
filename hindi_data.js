// Hindi phrases & dictionary – Phrases and Words tabs (Lessons use data_hindi.json)
const HINDI_PHRASES = {
  greetings_1: {
    name: "Hindi Greetings",
    color: "#2B6CB0",
    icon: "👋",
    phrases: [
      { en: "Hello / Namaste", mr: "नमस्ते", roman: "Namaste", hint: "" },
      { en: "How are you? (formal)", mr: "आप कैसे हैं?", roman: "Āp kaise haiṃ?", hint: "" },
      { en: "I am fine", mr: "मैं ठीक हूँ", roman: "Main ṭhīk hū̃", hint: "" },
      { en: "Good morning", mr: "सुप्रभात", roman: "Suprabhāt", hint: "" },
      { en: "Good night", mr: "शुभ रात्रि", roman: "Śubh rātri", hint: "" },
      { en: "What is your name?", mr: "आपका नाम क्या है?", roman: "Āpkā nām kyā hai?", hint: "" },
      { en: "My name is…", mr: "मेरा नाम … है", roman: "Merā nām … hai", hint: "" },
      { en: "Thank you", mr: "धन्यवाद", roman: "Dhanyavād", hint: "" },
      { en: "Please", mr: "कृपया", roman: "Kripayā", hint: "" },
      { en: "Sorry", mr: "माफ़ कीजिए", roman: "Māf kījie", hint: "" },
      { en: "Welcome", mr: "स्वागत है", roman: "Svāgat hai", hint: "" },
      { en: "See you again", mr: "फिर मिलेंगे", roman: "Phir mileṅge", hint: "" },
      { en: "Nice to meet you", mr: "आप से मिलकर अच्छा लगा", roman: "Āp se milkar acchā lagā", hint: "" },
      { en: "Come in", mr: "अंदर आइए", roman: "Andar āie", hint: "" },
      { en: "Sit down", mr: "बैठिए", roman: "Baithie", hint: "" },
      { en: "Goodbye", mr: "अलविदा", roman: "Alvidā", hint: "" }
    ]
  },
  travel_1: {
    name: "Travel",
    color: "#38A169",
    icon: "🚌",
    phrases: [
      { en: "Where is the bus stop?", mr: "बस स्टॉप कहाँ है?", roman: "Bas sṭॉp kahā̃ hai?", hint: "" },
      { en: "Where is the railway station?", mr: "रेलवे स्टेशन कहाँ है?", roman: "Relve sṭeśan kahā̃ hai?", hint: "" },
      { en: "I want to go to…", mr: "मैं … जाना चाहता हूँ", roman: "Main … jānā cāhatā hū̃", hint: "" },
      { en: "How far is it?", mr: "यह कितनी दूर है?", roman: "Yah kitnī dūr hai?", hint: "" },
      { en: "One ticket to Delhi", mr: "दिल्ली का एक टिकट", roman: "Dillī kā ek ṭikaṭ", hint: "" },
      { en: "Stop here", mr: "यहीं रुकिए", roman: "Yahī̃ rukie", hint: "" },
      { en: "Turn left", mr: "बाएँ मुड़िए", roman: "Bāẽ muṛie", hint: "" },
      { en: "Turn right", mr: "दाएँ मुड़िए", roman: "Dāẽ muṛie", hint: "" },
      { en: "Go straight", mr: "सीधे जाइए", roman: "Sīdhe jāie", hint: "" },
      { en: "I am lost", mr: "मैं रास्ता भटक गया", roman: "Main rāstā bhaṭak gayā", hint: "" },
      { en: "How much is the fare?", mr: "किराया कितना है?", roman: "Kirāyā kitnā hai?", hint: "" },
      { en: "Where is the hotel?", mr: "होटल कहाँ है?", roman: "Hoṭal kahā̃ hai?", hint: "" },
      { en: "Call a taxi", mr: "टैक्सी बुलाइए", roman: "Ṭaiksī bulāie", hint: "" },
      { en: "Which platform?", mr: "कौन सा प्लेटफ़ॉर्म?", roman: "Kaun sā pleṭphॉrm?", hint: "" },
      { en: "When does the train leave?", mr: "ट्रेन कब चलेगी?", roman: "ṭren kab calegī?", hint: "" },
      { en: "Is this seat taken?", mr: "क्या यह सीट खाली है?", roman: "Kyā yah sīṭ khālī hai?", hint: "" }
    ]
  },
  food_1: {
    name: "Food",
    color: "#DD6B20",
    icon: "🍛",
    phrases: [
      { en: "I am hungry", mr: "मुझे भूख लगी है", roman: "Mujhe bhūkh lagī hai", hint: "" },
      { en: "Give me water", mr: "पानी दीजिए", roman: "Pānī dījie", hint: "" },
      { en: "The food is delicious", mr: "खाना बहुत स्वादिष्ट है", roman: "Khānā bahut svādiṣṭ hai", hint: "" },
      { en: "Bring the bill", mr: "बिल लाइए", roman: "Bil lāie", hint: "" },
      { en: "I am vegetarian", mr: "मैं शाकाहारी हूँ", roman: "Main śākāhārī hū̃", hint: "" },
      { en: "Not too spicy", mr: "ज़्यादा मसालेदार नहीं", roman: "Zyādā masāledār nahī̃", hint: "" },
      { en: "One plate of rice", mr: "चावल की एक प्लेट", roman: "Cāwal kī ek pleṭ", hint: "" },
      { en: "Tea without sugar", mr: "बिना चीनी की चाय", roman: "Binā cīnī kī cāy", hint: "" },
      { en: "What do you recommend?", mr: "आप क्या सुझाते हैं?", roman: "Āp kyā sujhāte haiṃ?", hint: "" },
      { en: "Pack this to go", mr: "यह पैक कर दीजिए", roman: "Yah paik kar dījie", hint: "" },
      { en: "The thali was good", mr: "थाली अच्छी थी", roman: "Thālī acchī thī", hint: "" },
      { en: "I would like juice", mr: "मुझे जूस चाहिए", roman: "Mujhe jūs cāhie", hint: "" },
      { en: "Is this pure veg?", mr: "क्या यह शुद्ध शाकाहारी है?", roman: "Kyā yah śuddh śākāhārī hai?", hint: "" },
      { en: "Less oil, please", mr: "कम तेल, कृपया", roman: "Kam tel, kripayā", hint: "" },
      { en: "Breakfast time?", mr: "नाश्ते का समय क्या है?", roman: "Nāste kā samay kyā hai?", hint: "" },
      { en: "Table for two", mr: "दो लोगों के लिए मेज़", roman: "Do logõ ke liye mez", hint: "" }
    ]
  },
  daily_1: {
    name: "Daily life",
    color: "#805AD5",
    icon: "🏠",
    phrases: [
      { en: "What time is it?", mr: "क्या समय हुआ है?", roman: "Kyā samay huā hai?", hint: "" },
      { en: "Where do you live?", mr: "आप कहाँ रहते हैं?", roman: "Āp kahā̃ rahte haiṃ?", hint: "" },
      { en: "I live in Mumbai", mr: "मैं मुंबई में रहता हूँ", roman: "Main mumbaī mẽ rahatā hū̃", hint: "" },
      { en: "What work do you do?", mr: "आप क्या काम करते हैं?", roman: "Āp kyā kām karte haiṃ?", hint: "" },
      { en: "I need to go home", mr: "मुझे घर जाना है", roman: "Mujhe ghar jānā hai", hint: "" },
      { en: "Open the door", mr: "दरवाज़ा खोलिए", roman: "Darvāzā kholie", hint: "" },
      { en: "Switch on the light", mr: "लाइट जलाइए", roman: "Lāiṭ jalāie", hint: "" },
      { en: "What day is today?", mr: "आज कौन सा दिन है?", roman: "Āj kaun sā din hai?", hint: "" },
      { en: "I am tired", mr: "मैं थक गया हूँ", roman: "Main thak gayā hū̃", hint: "" },
      { en: "Wake up", mr: "उठ जाइए", roman: "Uṭh jāie", hint: "" },
      { en: "I will come tomorrow", mr: "मैं कल आऊँगा", roman: "Main kal āū̃gā", hint: "" },
      { en: "The weather is nice", mr: "मौसम अच्छा है", roman: "Mausam acchā hai", hint: "" },
      { en: "It is very hot", mr: "बहुत गर्मी है", roman: "Bahut garmī hai", hint: "" },
      { en: "It is cold", mr: "ठंड है", roman: "Thaṃḍ hai", hint: "" },
      { en: "Let us take a walk", mr: "चलिए सैर करते हैं", roman: "Calie sair karte haiṃ", hint: "" },
      { en: "I will call you", mr: "मैं आपको फोन करूँगा", roman: "Main āpko phon karū̃gā", hint: "" }
    ]
  },
  shopping_1: {
    name: "Shopping",
    color: "#D69E2E",
    icon: "🛒",
    phrases: [
      { en: "How much does this cost?", mr: "यह कितने का है?", roman: "Yah kitne kā hai?", hint: "" },
      { en: "It is expensive", mr: "यह महँगा है", roman: "Yah mahṅgā hai", hint: "" },
      { en: "Lower the price, please", mr: "कीमत कम कीजिए", roman: "Kīmat kam kījie", hint: "" },
      { en: "Show me that one", mr: "वह दिखाइए", roman: "Vah dikhāie", hint: "" },
      { en: "I want to buy this", mr: "मैं यह खरीदना चाहता हूँ", roman: "Main yah kharīdnā cāhatā hū̃", hint: "" },
      { en: "Do you have change?", mr: "छुट्टे पैसे हैं?", roman: "Chhuṭṭe paise haiṃ?", hint: "" },
      { en: "Where is the market?", mr: "बाज़ार कहाँ है?", roman: "Bāzār kahā̃ hai?", hint: "" },
      { en: "One kilogram of potatoes", mr: "एक किलो आलू", roman: "Ek kilo ālū", hint: "" },
      { en: "Give me a bag", mr: "एक थैला दीजिए", roman: "Ek thailā dījie", hint: "" },
      { en: "I will pay by card", mr: "कार्ड से भुगतान करूँगा", roman: "Kārḍ se bhugtān karū̃gā", hint: "" },
      { en: "Is the shop open?", mr: "दुकान खुली है?", roman: "Dukān khulī hai?", hint: "" },
      { en: "Fresh vegetables", mr: "ताज़ी सब्ज़ियाँ", roman: "Tāzī sabziyā̃", hint: "" },
      { en: "No plastic bag", mr: "प्लास्टिक का थैला नहीं", roman: "Plāsṭik kā thailā nahī̃", hint: "" },
      { en: "Receipt, please", mr: "रसीद दीजिए", roman: "Rasīd dījie", hint: "" },
      { en: "Discount?", mr: "छूट मिलेगी?", roman: "Chhūṭ milegī?", hint: "" },
      { en: "Cash only", mr: "केवल नकद", roman: "Keval nakad", hint: "" }
    ]
  },
  emergency_1: {
    name: "Emergency",
    color: "#E53E3E",
    icon: "🚨",
    phrases: [
      { en: "Help!", mr: "बचाओ!", roman: "Bacāo!", hint: "" },
      { en: "Call the police", mr: "पुलिस को बुलाइए", roman: "Pulis ko bulāie", hint: "" },
      { en: "Call a doctor", mr: "डॉक्टर को बुलाइए", roman: "Ḍॉkṭar ko bulāie", hint: "" },
      { en: "I need a hospital", mr: "मुझे अस्पताल चाहिए", roman: "Mujhe aspatāl cāhie", hint: "" },
      { en: "There is a fire", mr: "आग लग गई है", roman: "Āg lag gaī hai", hint: "" },
      { en: "Accident", mr: "दुर्घटना हो गई", roman: "Durghaṭnā ho gaī", hint: "" },
      { en: "I have chest pain", mr: "मेरे सीने में दर्द है", roman: "Mere sīne mẽ dard hai", hint: "" },
      { en: "Allergic reaction", mr: "एलर्जी की प्रतिक्रिया", roman: "Elarjī kī pratikriyā", hint: "" },
      { en: "Where is the pharmacy?", mr: "दवा की दुकान कहाँ है?", roman: "Davā kī dukān kahā̃ hai?", hint: "" },
      { en: "Ambulance", mr: "एम्बुलेंस बुलाइए", roman: "Embuleṃs bulāie", hint: "" },
      { en: "I lost my phone", mr: "मेरा फोन खो गया", roman: "Merā phon kho gayā", hint: "" },
      { en: "Please help me", mr: "कृपया मेरी मदद करें", roman: "Kripayā merī madad kareṃ", hint: "" },
      { en: "Police station?", mr: "थाना कहाँ है?", roman: "Thānā kahā̃ hai?", hint: "" },
      { en: "I feel dizzy", mr: "मुझे चक्कर आ रहे हैं", roman: "Mujhe cakkar ā rahe haiṃ", hint: "" },
      { en: "Bleeding", mr: "खून बह रहा है", roman: "Khūn bah rahā hai", hint: "" },
      { en: "Emergency number", mr: "आपातकालीन नंबर", roman: "Āpātkālīn nambar", hint: "" }
    ]
  },
  social_1: {
    name: "Social media",
    color: "#3182CE",
    icon: "📱",
    phrases: [
      { en: "I use Facebook", mr: "मैं फेसबुक इस्तेमाल करता हूँ", roman: "Main Phēsbuk istemāl kartā hū̃", hint: "" },
      { en: "Do you have WhatsApp?", mr: "क्या आपके पास व्हाट्सऐप है?", roman: "Kyā āp ke pās Vhaṭsāip hai?", hint: "" },
      { en: "Send it to me on WhatsApp", mr: "व्हाट्सऐप पर मुझे भेज दीजिए", roman: "Vhaṭsāip par mujhe bhej dījie", hint: "" },
      { en: "I posted a photo", mr: "मैंने एक फोटो पोस्ट की", roman: "Mainne ek phoṭo posṭ kī", hint: "" },
      { en: "Like and share", mr: "लाइक और शेयर कीजिए", roman: "Lāik aur śeyar kījie", hint: "" },
      { en: "Too much screen time", mr: "स्क्रीन टाइम बहुत ज़्यादा", roman: "Skrīn ṭāim bahut zyādā", hint: "" },
      { en: "I deleted the app", mr: "मैंने ऐप हटा दिया", roman: "Mainne aip haṭā diyā", hint: "" },
      { en: "Check your notifications", mr: "अपनी सूचनाएँ देखिए", roman: "Apnī sūcnāeṃ dekhie", hint: "" },
      { en: "Follow me", mr: "कृपया मुझे फॉलो करें", roman: "Kripayā mujhe phŏlo kareṃ", hint: "" },
      { en: "Comment below", mr: "नीचे कमेंट कीजिए", roman: "Nīce kemenṭ kījie", hint: "" },
      { en: "Scroll down", mr: "नीचे स्क्रॉल कीजिए", roman: "Nīce skrŏl kījie", hint: "" }
    ]
  }
};

const HINDI_DICTIONARY = {
  basics_1: {
    name: "Basic words",
    words: [
      { en: "I", mr: "मैं", roman: "Main" },
      { en: "You (formal)", mr: "आप", roman: "Āp" },
      { en: "You (informal)", mr: "तुम", roman: "Tum" },
      { en: "He / She", mr: "वह", roman: "Vah" },
      { en: "We", mr: "हम", roman: "Ham" },
      { en: "They", mr: "वे", roman: "Ve" },
      { en: "House", mr: "घर", roman: "Ghar" },
      { en: "Water", mr: "पानी", roman: "Pānī" },
      { en: "Food", mr: "खाना", roman: "Khānā" },
      { en: "Today", mr: "आज", roman: "Āj" },
      { en: "Tomorrow", mr: "कल", roman: "Kal" },
      { en: "Yesterday", mr: "कल", roman: "Kal" },
      { en: "Yes", mr: "हाँ", roman: "Hā̃" },
      { en: "No", mr: "नहीं", roman: "Nahī̃" },
      { en: "Good", mr: "अच्छा", roman: "Acchā" },
      { en: "Bad", mr: "बुरा", roman: "Burā" },
      { en: "Big", mr: "बड़ा", roman: "Baṛā" },
      { en: "Small", mr: "छोटा", roman: "Choṭā" },
      { en: "Hot", mr: "गर्म", roman: "Garm" },
      { en: "Cold", mr: "ठंडा", roman: "Thaṃḍā" }
    ]
  },
  family_1: {
    name: "Family",
    words: [
      { en: "Mother", mr: "माँ", roman: "Mā̃" },
      { en: "Father", mr: "पिता", roman: "Pitā" },
      { en: "Brother", mr: "भाई", roman: "Bhāī" },
      { en: "Sister", mr: "बहन", roman: "Behan" },
      { en: "Son", mr: "बेटा", roman: "Beṭā" },
      { en: "Daughter", mr: "बेटी", roman: "Beṭī" },
      { en: "Husband", mr: "पति", roman: "Pati" },
      { en: "Wife", mr: "पत्नी", roman: "Patnī" },
      { en: "Grandfather", mr: "दादा", roman: "Dādā" },
      { en: "Grandmother", mr: "दादी", roman: "Dādī" },
      { en: "Friend", mr: "दोस्त", roman: "Dost" },
      { en: "Uncle (father's brother)", mr: "चाचा", roman: "Cācā" },
      { en: "Aunt", mr: "चाची", roman: "Cācī" }
    ]
  },
  verbs_1: {
    name: "Common verbs",
    words: [
      { en: "to go", mr: "जाना", roman: "Jānā" },
      { en: "to come", mr: "आना", roman: "Ānā" },
      { en: "to eat", mr: "खाना", roman: "Khānā" },
      { en: "to drink", mr: "पीना", roman: "Pīnā" },
      { en: "to speak", mr: "बोलना", roman: "Bolnā" },
      { en: "to listen", mr: "सुनना", roman: "Sunnā" },
      { en: "to see", mr: "देखना", roman: "Dekhnā" },
      { en: "to do", mr: "करना", roman: "Karnā" },
      { en: "to give", mr: "देना", roman: "Denā" },
      { en: "to take", mr: "लेना", roman: "Lenā" },
      { en: "to sit", mr: "बैठना", roman: "Baiṭhnā" },
      { en: "to sleep", mr: "सोना", roman: "Sonā" },
      { en: "to read", mr: "पढ़ना", roman: "Paṛhnā" },
      { en: "to write", mr: "लिखना", roman: "Likhnā" },
      { en: "to understand", mr: "समझना", roman: "Samajhnā" }
    ]
  },
  nature_1: {
    name: "Nature",
    words: [
      { en: "Sun", mr: "सूरज", roman: "Sūraj" },
      { en: "Moon", mr: "चाँद", roman: "Cā̃d" },
      { en: "Star", mr: "तारा", roman: "Tārā" },
      { en: "Sky", mr: "आसमान", roman: "Āsmān" },
      { en: "Rain", mr: "बारिश", roman: "Bāriś" },
      { en: "Wind", mr: "हवा", roman: "Havā" },
      { en: "Tree", mr: "पेड़", roman: "Peṛ" },
      { en: "Flower", mr: "फूल", roman: "Phūl" },
      { en: "River", mr: "नदी", roman: "Nadī" },
      { en: "Mountain", mr: "पहाड़", roman: "Pahāṛ" },
      { en: "Earth", mr: "धरती", roman: "Dhartī" },
      { en: "Fire", mr: "आग", roman: "Āg" }
    ]
  }
};
