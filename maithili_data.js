// Maithili phrases & dictionary – for Phrases and Words sections (separate from Lessons)
const MAITHILI_PHRASES = {
  greetings: {
    name: "Greetings & Introduction",
    color: "#2B6CB0",
    icon: "👋",
    phrases: [
      { en: "Hello", mr: "नमस्कार", roman: "Namaskār", hint: "" },
      { en: "Good morning", mr: "सुप्रभात", roman: "Suprabhāt", hint: "" },
      { en: "Good afternoon", mr: "शुभ दुपहरिया", roman: "Shubh duphariyā", hint: "" },
      { en: "Good evening", mr: "शुभ सान्झ", roman: "Shubh sānjh", hint: "" },
      { en: "Good night", mr: "शुभ रात", roman: "Shubh rāt", hint: "" },
      { en: "Welcome", mr: "स्वागतम्", roman: "Svāgatam", hint: "" },
      { en: "How are you?", mr: "अहाँ केहन छी?", roman: "Aanha kēhan chhi?", hint: "" },
      { en: "I am fine", mr: "हम नीक छी", roman: "Hum nik chhi", hint: "" },
      { en: "What is your name?", mr: "अहाँक नाम की अछि?", roman: "Aanhak nām ki achhi?", hint: "" },
      { en: "My name is...", mr: "हमर नाम ... अछि", roman: "Hamar nām ... achhi", hint: "" },
      { en: "Nice to meet you", mr: "अहाँ सँ भेट क' खुशी भेल", roman: "Aanha sa bhet ka khushī bhel", hint: "" },
      { en: "Thank you", mr: "धन्यवाद", roman: "Dhan'yavād", hint: "" },
      { en: "Please", mr: "कृपया", roman: "Kripayā", hint: "" },
      { en: "Sorry", mr: "क्षमा करू", roman: "Kshamā karū", hint: "" },
      { en: "Goodbye", mr: "अलविदा", roman: "Alvidā", hint: "" },
      { en: "See you", mr: "फेर भेट होय", roman: "Pher bhet hōy", hint: "" },
      { en: "Take care", mr: "ध्यान रखू", roman: "Dhyān rakhū", hint: "" },
      { en: "Happy Birthday", mr: "जन्मदिन को शुभकामना", roman: "Janmadin kō shubhakāmanā", hint: "" },
      { en: "Happy Diwali", mr: "दीपावली को शुभकामना", roman: "Dīpāvalī kō shubhakāmanā", hint: "" },
      { en: "I love you", mr: "हम अहाँ सँ प्रेम करैत छी", roman: "Hum aanha sa prem karait chhi", hint: "" },
      { en: "Get well soon", mr: "जल्दी नीक होऊ", roman: "Jaldī nik hōū", hint: "" }
    ]
  },
  travel: {
    name: "Travel & Directions",
    color: "#D69E2E",
    icon: "🚗",
    phrases: [
      { en: "Where is the station?", mr: "स्टेशन कतय अछि?", roman: "Sṭeshan katay achhi?", hint: "" },
      { en: "Take me to the station", mr: "हमरा स्टेशन ल' जाऊ", roman: "Hamrā sṭeshan la jāū", hint: "" },
      { en: "Where is the hospital?", mr: "अस्पताल कतय अछि?", roman: "Aspatāl katay achhi?", hint: "" },
      { en: "Go straight", mr: "सीधा जाऊ", roman: "Sīdhā jāū", hint: "" },
      { en: "Turn left", mr: "बामा मुड़ू", roman: "Bāmā muṛū", hint: "" },
      { en: "Turn right", mr: "दाहिना मुड़ू", roman: "Dāhinā muṛū", hint: "" },
      { en: "Stop here", mr: "एतय रोकू", roman: "Etay rōkū", hint: "" },
      { en: "How far is it?", mr: "कतेक दूर अछि?", roman: "Katek dūr achhi?", hint: "" },
      { en: "I am lost", mr: "हम रास्ता भुलल छी", roman: "Hum rāstā bhulal chhi", hint: "" },
      { en: "Where is the toilet?", mr: "शौचालय कतय अछि?", roman: "Shauchālay katay achhi?", hint: "" },
      { en: "Bon voyage", mr: "अहाँक यात्रा शुभ होय", roman: "Aanhak yātrā shubh hōy", hint: "" }
    ]
  },
  food: {
    name: "Food & Drink",
    color: "#C05621",
    icon: "🍽️",
    phrases: [
      { en: "Water", mr: "पानी", roman: "Pānī", hint: "" },
      { en: "Food", mr: "खेनाई", roman: "Khenāi", hint: "" },
      { en: "I am hungry", mr: "हमरा भूख लागैत छी", roman: "Hamrā bhūkh lagait chhi", hint: "" },
      { en: "Cooked rice", mr: "भात", roman: "Bhāt", hint: "" },
      { en: "Tea", mr: "चाय", roman: "Chāy", hint: "" },
      { en: "Coffee", mr: "कॉफी", roman: "Kŏphī", hint: "" },
      { en: "Please give me water", mr: "कृपया पानी देऊ", roman: "Kripayā pānī deū", hint: "" },
      { en: "The food is delicious", mr: "खेनाई बहुत नीक अछि", roman: "Khenāi bahut nik achhi", hint: "" },
      { en: "I am vegetarian", mr: "हम शाकाहारी छी", roman: "Hum shākāhārī chhi", hint: "" },
      { en: "Bill please", mr: "बिल देऊ", roman: "Bil deū", hint: "" },
      { en: "Have a nice meal", mr: "अहाँक भोजन नीक होय", roman: "Aanhak bhōjan nik hōy", hint: "" }
    ]
  },
  shopping: {
    name: "Shopping",
    color: "#805AD5",
    icon: "🛒",
    phrases: [
      { en: "How much is this?", mr: "ई कतेक अछि?", roman: "I katek achhi?", hint: "" },
      { en: "That's too expensive", mr: "ओ बहुत महग अछि", roman: "O bahut mahag achhi", hint: "" },
      { en: "Cheap", mr: "सस्ता", roman: "Sastā", hint: "" },
      { en: "Give me one kg rice", mr: "हमरा एक किलो चावल देऊ", roman: "Hamrā ek kilō chāval deū", hint: "" },
      { en: "Do you have a bag?", mr: "अहाँक थैला अछि?", roman: "Aanhak thailā achhi?", hint: "" },
      { en: "OK I'll take it", mr: "ठीक अछि हम ई ल' लेत छी", roman: "Ṭhīk achhi hum i la let chhi", hint: "" }
    ]
  },
  emergency: {
    name: "Emergency",
    color: "#E53E3E",
    icon: "🆘",
    phrases: [
      { en: "Help!", mr: "कानि मदद करू!", roman: "Kāni madad karū!", hint: "" },
      { en: "Stop!", mr: "रुकू!", roman: "Rukū!", hint: "" },
      { en: "Call the police!", mr: "पुलिस केँ फोन करू!", roman: "Pulis kẽ phōn karū!", hint: "" },
      { en: "Fire!", mr: "आगि!", roman: "Āgi!", hint: "" },
      { en: "I need a doctor", mr: "हमरा एक डॉक्टर चाही", roman: "Hamrā ek ḍŏkṭar chāhī", hint: "" },
      { en: "I'm sick", mr: "हम बिमार छी", roman: "Hum bimār chhi", hint: "" },
      { en: "It's an emergency", mr: "ई आपातकाल अछि", roman: "I āpātakāl achhi", hint: "" }
    ]
  },
  time: {
    name: "Time & Days",
    color: "#38A169",
    icon: "🕐",
    phrases: [
      { en: "What time is it?", mr: "कतेक बजल अछि?", roman: "Katek bajal achhi?", hint: "" },
      { en: "Morning", mr: "भिन्सर", roman: "Bhinsar", hint: "" },
      { en: "Evening", mr: "सान्झ", roman: "Sānjh", hint: "" },
      { en: "Night", mr: "रात", roman: "Rāt", hint: "" },
      { en: "Today", mr: "आज", roman: "Āj", hint: "" },
      { en: "Tomorrow", mr: "काल्हि", roman: "Kālhi", hint: "" },
      { en: "Yesterday", mr: "काल्हि", roman: "Kālhi", hint: "" },
      { en: "Now", mr: "अखन", roman: "Akhan", hint: "" },
      { en: "Sunday", mr: "रविवार", roman: "Ravivār", hint: "" },
      { en: "Monday", mr: "सोमवार", roman: "Sōmavār", hint: "" }
    ]
  },
  common: {
    name: "Common Phrases",
    color: "#2C5282",
    icon: "💬",
    phrases: [
      { en: "Yes", mr: "हाँ", roman: "Hā̃", hint: "" },
      { en: "No", mr: "नहि", roman: "Nahi", hint: "" },
      { en: "Please speak slowly", mr: "कृपया धीरे सँ बजू", roman: "Kripayā dhīre sa bajū", hint: "" },
      { en: "I don't understand", mr: "हम नहि बुझैत छी", roman: "Hum nahi bujhait chhi", hint: "" },
      { en: "Do you speak Maithili?", mr: "अहाँ मैथिली बजैत छी?", roman: "Aanha Maithilī bajait chhi?", hint: "" },
      { en: "No problem", mr: "कोनो समस्या नहि", roman: "Kono samasyā nahi", hint: "" },
      { en: "I agree", mr: "हम सहमत छी", roman: "Hum sahmat chhi", hint: "" },
      { en: "Come in", mr: "अंदर आऊ", roman: "Aṃdar āū", hint: "" },
      { en: "Have you eaten?", mr: "की अहाँ खा लेल छी?", roman: "Ki aanha khā lel chhi?", hint: "" },
      { en: "We are happy", mr: "हम खुश छी", roman: "Hum khush chhi", hint: "" }
    ]
  }
};

const MAITHILI_DICTIONARY = {
  greetings: {
    name: "Greetings & Basics",
    words: [
      { en: "Hello", mr: "नमस्कार", roman: "Namaskār" },
      { en: "Thank you", mr: "धन्यवाद", roman: "Dhan'yavād" },
      { en: "Please", mr: "कृपया", roman: "Kripayā" },
      { en: "Yes", mr: "हाँ", roman: "Hā̃" },
      { en: "No", mr: "नहि", roman: "Nahi" },
      { en: "Sorry", mr: "क्षमा करू", roman: "Kshamā karū" },
      { en: "Welcome", mr: "स्वागतम्", roman: "Svāgatam" },
      { en: "Name", mr: "नाम", roman: "Nām" },
      { en: "Good", mr: "नीक", roman: "Nīk" },
      { en: "Bad", mr: "बुरा", roman: "Burā" }
    ]
  },
  travel: {
    name: "Travel & Directions",
    words: [
      { en: "Street", mr: "रस्ता", roman: "Rastā" },
      { en: "Left", mr: "बामा", roman: "Bāmā" },
      { en: "Right", mr: "दाहिना", roman: "Dāhinā" },
      { en: "Here", mr: "एतय", roman: "Etay" },
      { en: "There", mr: "ओतय", roman: "Otay" },
      { en: "Near", mr: "नजिक", roman: "Najik" },
      { en: "Far", mr: "दूर", roman: "Dūr" },
      { en: "North", mr: "उत्तर", roman: "Uttar" },
      { en: "South", mr: "दक्षिण", roman: "Dakshiṇ" },
      { en: "East", mr: "पूरब", roman: "Pūrab" },
      { en: "West", mr: "पश्चिम", roman: "Pashchim" }
    ]
  },
  food: {
    name: "Food & Drink",
    words: [
      { en: "Water", mr: "पानी", roman: "Pānī" },
      { en: "Food", mr: "खेनाई", roman: "Khenāi" },
      { en: "Rice", mr: "चावल", roman: "Chāval" },
      { en: "Lentils", mr: "दाल", roman: "Dāl" },
      { en: "Bread", mr: "पावरोटी", roman: "Pāvrōṭī" },
      { en: "Tea", mr: "चाय", roman: "Chāy" },
      { en: "Coffee", mr: "कॉफी", roman: "Kŏphī" },
      { en: "Salt", mr: "नुन", roman: "Nun" },
      { en: "Sugar", mr: "चीनी", roman: "Chīnī" },
      { en: "Milk", mr: "दूध", roman: "Dūdh" },
      { en: "Vegetable", mr: "सब्जी", roman: "Sabjī" },
      { en: "Fruit", mr: "फल", roman: "Phal" }
    ]
  },
  body: {
    name: "Body Parts",
    words: [
      { en: "Head", mr: "माथा", roman: "Māthā" },
      { en: "Eye", mr: "आँख", roman: "Ā̃kh" },
      { en: "Hand", mr: "हाथ", roman: "Hāth" },
      { en: "Foot", mr: "पैर", roman: "Pair" },
      { en: "Heart", mr: "दिल", roman: "Dil" },
      { en: "Face", mr: "मुख", roman: "Mukh" },
      { en: "Hair", mr: "केश", roman: "Kesh" },
      { en: "Stomach", mr: "पेट", roman: "Peṭ" },
      { en: "Back", mr: "पीठ", roman: "Pīṭh" },
      { en: "Neck", mr: "गरदन", roman: "Garadan" }
    ]
  },
  family: {
    name: "Family & Relations",
    words: [
      { en: "Father", mr: "बाबू", roman: "Bābū" },
      { en: "Mother", mr: "मां", roman: "Mān" },
      { en: "Brother", mr: "भाई", roman: "Bhāī" },
      { en: "Sister", mr: "बहिन", roman: "Bahin" },
      { en: "Son", mr: "बेटा", roman: "Beṭā" },
      { en: "Daughter", mr: "धिया", roman: "Dhiyā" },
      { en: "Husband", mr: "पति", roman: "Pati" },
      { en: "Wife", mr: "पत्नी", roman: "Patnī" },
      { en: "Friend", mr: "मित्र", roman: "Mitra" },
      { en: "Family", mr: "परिवार", roman: "Parivār" },
      { en: "Child", mr: "नेना", roman: "Nēnā" }
    ]
  },
  numbers: {
    name: "Numbers",
    words: [
      { en: "One", mr: "एक", roman: "Ek" },
      { en: "Two", mr: "दू", roman: "Dū" },
      { en: "Three", mr: "तीन", roman: "Tīn" },
      { en: "Four", mr: "चार", roman: "Chār" },
      { en: "Five", mr: "पाँच", roman: "Pā̃ch" },
      { en: "Ten", mr: "दस", roman: "Das" },
      { en: "Twenty", mr: "बीस", roman: "Bīs" },
      { en: "Hundred", mr: "सय", roman: "Say" },
      { en: "Thousand", mr: "हजार", roman: "Hajār" }
    ]
  },
  home: {
    name: "Home & Daily",
    words: [
      { en: "House", mr: "घर", roman: "Ghar" },
      { en: "Day", mr: "दिन", roman: "Din" },
      { en: "Time", mr: "समय", roman: "Samay" },
      { en: "Work", mr: "काज", roman: "Kāj" },
      { en: "Water", mr: "पानी", roman: "Pānī" },
      { en: "Sleep", mr: "निंद", roman: "Niṃd" },
      { en: "Eat", mr: "खाउ", roman: "Khāu" },
      { en: "Come", mr: "आब", roman: "Āb" },
      { en: "Go", mr: "जाब", roman: "Jāb" },
      { en: "See", mr: "देखब", roman: "Dekhab" },
      { en: "Give", mr: "देब", roman: "Deb" },
      { en: "Take", mr: "ल'ब", roman: "La'b" }
    ]
  },
  nature: {
    name: "Nature & Animals",
    words: [
      { en: "Sun", mr: "सूरज", roman: "Sūraj" },
      { en: "Moon", mr: "चंदा", roman: "Chaṃdā" },
      { en: "Rain", mr: "बरखा", roman: "Barkhā" },
      { en: "Dog", mr: "कुकुर", roman: "Kukur" },
      { en: "Cat", mr: "बिराली", roman: "Birālī" },
      { en: "Cow", mr: "गाई", roman: "Gāī" },
      { en: "Bird", mr: "चिरई", roman: "Chiraī" },
      { en: "Fish", mr: "माछ", roman: "Māch" },
      { en: "Tree", mr: "गाछ", roman: "Gāch" },
      { en: "Flower", mr: "फूल", roman: "Phūl" }
    ]
  },
  colours: {
    name: "Colours",
    words: [
      { en: "Red", mr: "लाल", roman: "Lāl" },
      { en: "Blue", mr: "नीला", roman: "Nīlā" },
      { en: "Green", mr: "हरियर", roman: "Hariyar" },
      { en: "Yellow", mr: "पीयर", roman: "Pīyar" },
      { en: "White", mr: "उज्जर", roman: "Ujjar" },
      { en: "Black", mr: "काला", roman: "Kālā" },
      { en: "Colour", mr: "रंग", roman: "Raṃg" }
    ]
  },
  questions: {
    name: "Questions & Common",
    words: [
      { en: "What", mr: "की", roman: "Kī" },
      { en: "Who", mr: "कोन", roman: "Kōn" },
      { en: "Where", mr: "कतय", roman: "Katay" },
      { en: "When", mr: "कखन", roman: "Kakhan" },
      { en: "Why", mr: "किएक", roman: "Kiek" },
      { en: "How", mr: "केन", roman: "Kēn" },
      { en: "This", mr: "ई", roman: "Ī" },
      { en: "That", mr: "ओ", roman: "O" },
      { en: "Problem", mr: "समस्या", roman: "Samasyā" },
      { en: "Help", mr: "सहायता", roman: "Sahāyatā" }
    ]
  }
};
