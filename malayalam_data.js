// Malayalam phrases & dictionary – Phrases and Words tabs (lessons use data_malayalam.json)
// Phrases drawn from common Malayalam phrasebooks and learner resources (e.g. Omniglot, standard spoken Malayalam).

const MALAYALAM_PHRASES = {
  greetings_1: {
    name: "Greetings & politeness",
    color: "#2B6CB0",
    icon: "👋",
    phrases: [
      { en: "Hello / Namaste", mr: "നമസ്കാരം", roman: "namaskāram", hint: "Also നമസ്തേ (namastē) in speech" },
      { en: "Good morning", mr: "സുപ്രഭാതം", roman: "suprabhātam", hint: "" },
      { en: "Good evening", mr: "ശുഭ സന്ധ്യ", roman: "śubha sandhya", hint: "" },
      { en: "Good night", mr: "ശുഭ രാത്രി", roman: "śubha rātri", hint: "" },
      { en: "Welcome", mr: "സ്വാഗതം", roman: "svāgataṃ", hint: "" },
      { en: "How are you? (to one person, informal)", mr: "എങ്ങനെയുണ്ട് നിനക്ക്?", roman: "eṅṅaneyuṇṭu ninakku?", hint: "Literally: how is it for you?" },
      { en: "How are you all? (respectful / plural)", mr: "എങ്ങനെയുണ്ട് നിങ്ങൾക്ക്?", roman: "eṅṅaneyuṇṭu niṅṅaḷkku?", hint: "" },
      { en: "I am doing well / I am fine", mr: "നന്നായിരിക്കുന്നു", roman: "nannāyirikkunnu", hint: "Common reply to “How are you?”" },
      { en: "I am fine; there is no problem", mr: "എനിക്ക് സുഖമാണ്, ഒരു പ്രശ്നവുമില്ല", roman: "enikk sukhamāṇu, oru praśnavumilla", hint: "" },
      { en: "Thank you very much for your help", mr: "നിങ്ങളുടെ സഹായത്തിന് വളരെ നന്ദി", roman: "niṅṅaḷuṭe sahāyattin vaḷare nandi", hint: "" },
      { en: "Please (when asking a favour)", mr: "ദയവായി", roman: "dayavāyi", hint: "" },
      { en: "Excuse me / Sorry", mr: "ക്ഷമിക്കണം", roman: "kṣamikkaṇam", hint: "" },
      { en: "Yes", mr: "അതെ", roman: "ate", hint: "" },
      { en: "No", mr: "ഇല്ല", roman: "illa", hint: "" },
      { en: "See you again / Goodbye for now", mr: "വീണ്ടും കാണാം", roman: "vīṇṭuṁ kāṇāṁ", hint: "" },
      { en: "Have a nice day", mr: "നല്ല ദിവസം ആകട്ടെ", roman: "nalla divasaṁ ākaṭṭe", hint: "" }
    ]
  },
  introductions: {
    name: "Introducing yourself",
    color: "#38A169",
    icon: "🙂",
    phrases: [
      { en: "What is your name? (informal)", mr: "നിന്റെ പേരെന്താണ്?", roman: "ninṟe pēr entāṇ?", hint: "" },
      { en: "What is your name? (polite)", mr: "നിങ്ങളുടെ പേര് എന്താണ്?", roman: "niṅṅaḷuṭe pēr entāṇ?", hint: "" },
      { en: "My name is …", mr: "എന്റെ പേര് … ആണ്", roman: "enṟe pēr … āṇ", hint: "" },
      { en: "I am pleased to meet you", mr: "നിങ്ങളെ കണ്ടതിൽ എനിക്ക് സന്തോഷമുണ്ട്", roman: "niṅṅaḷe kaṇṭatil enikk saṁtōṣamuṇṭ", hint: "" },
      { en: "It has been a long time since we met", mr: "വളരെ നാളായി കണ്ടിട്ട്", roman: "vaḷare nāḷāyi kaṇṭiṭ", hint: "Idiom: “long time no see”" },
      { en: "Where are you from?", mr: "നിങ്ങൾ എവിടെ നിന്ന് വരുന്നത്?", roman: "niṅṅaḷ evide ninn varunnat?", hint: "" },
      { en: "I am from …", mr: "ഞാൻ … നിന്നാണ് വന്നത്", roman: "njān … ninnāṇ vannat", hint: "" },
      { en: "I live in …", mr: "ഞാൻ … ഇൽ താമസിക്കുന്നു", roman: "njān … il tāmasikkunnu", hint: "Insert city name before ഇൽ" },
      { en: "This is my friend; he speaks Malayalam very well", mr: "ഇത് എന്റെ സുഹൃത്താണ്; അവൻ മലയാളം നന്നായി പറയുന്നു", roman: "it enṟe suhr̥uttāṇ; avan malayāḷaṁ nannāyi paṛayunnu", hint: "" }
    ]
  },
  food_culture: {
    name: "Food & hospitality",
    color: "#DD6B20",
    icon: "🍚",
    phrases: [
      { en: "Have you eaten (rice)? (common caring question)", mr: "ചോറുണ്ടോ?", roman: "cōṟṟuṇṭō?", hint: "Cultural check-in, not only literal rice" },
      { en: "Yes, I have eaten; thank you", mr: "ഉണ്ട്, ഞാൻ കഴിച്ചു, നന്ദി", roman: "uṇṭ, njān kaḻiccu, nandi", hint: "" },
      { en: "Please sit; food will be ready soon", mr: "ഇരിക്കൂ, ഭക്ഷണം ഉടൻ തയ്യാറാകും", roman: "irikkhū, bhakṣaṇaṁ uṭan tayyārākuṁ", hint: "" },
      { en: "Enjoy your meal with good taste", mr: "രുചിയോടെ ഭക്ഷണം ആസ്വദിക്കാൻ കഴിയട്ടെ", roman: "ruciyōṭe bhakṣaṇaṁ āsvadikkaṁ kaḻiyaṭṭe", hint: "Said like “bon appétit”" },
      { en: "The food was very tasty; I liked it a lot", mr: "ഭക്ഷണം വളരെ രുചിയായിരുന്നു; എനിക്ക് വളരെ ഇഷ്ടപ്പെട്ടു", roman: "bhakṣaṇaṁ vaḷare ruciyāyirunnu; enikk vaḷare iṣṭappaṭṭu", hint: "" },
      { en: "I am vegetarian; I do not eat meat", mr: "ഞാൻ നിരാമിഷഭക്ഷണക്കാരനാണ്; മാംസം കഴിക്കില്ല", roman: "njān nirāmiṣabhakṣaṇakkāranāṇ; māṁsaṁ kaḻikkilla", hint: "Adjust gendered noun if needed" },
      { en: "Can I get some more water, please?", mr: "കുറച്ച് കൂടെ വെള്ളം കിട്ടുമോ, ദയവായി?", roman: "kureśśe kūṭe veḷḷaṁ kiṭṭumō, dayavāyi?", hint: "" }
    ]
  },
  communication: {
    name: "Understanding & clarification",
    color: "#805AD5",
    icon: "💬",
    phrases: [
      { en: "I do not understand what you said", mr: "നിങ്ങൾ പറഞ്ഞത് എനിക്ക് മനസ്സിലായില്ല", roman: "niṅṅaḷ paṟaññat enikk manassilāyilla", hint: "" },
      { en: "Please speak a little more slowly", mr: "മെല്ലെ പറയൂ, ദയവായി", roman: "melle paṛayū, dayavāyi", hint: "" },
      { en: "Could you say that once more?", mr: "ഒന്നുകൂടി പറയാമോ?", roman: "onnukūṭi paṛayāmō?", hint: "" },
      { en: "Do you speak English?", mr: "നിങ്ങൾ ഇംഗ്ലീഷ് സംസാരിക്കുമോ?", roman: "niṅṅaḷ iṅglīṣ saṁsārikkumō?", hint: "" },
      { en: "Do you speak Malayalam?", mr: "നിങ്ങൾ മലയാളം സംസാരിക്കുമോ?", roman: "niṅṅaḷ malayāḷaṁ saṁsārikkumō?", hint: "" },
      { en: "Yes, I speak Malayalam a little", mr: "ഓ, കുറച്ച് മലയാളം പറയാം", roman: "ō, kureśś malayāḷaṁ paṛayāṁ", hint: "" },
      { en: "I am still learning Malayalam", mr: "ഞാൻ ഇപ്പോഴും മലയാളം പഠിച്ചുകൊണ്ടിരിക്കുകയാണ്", roman: "njān ippōḻuṁ malayāḷaṁ paṭhiccukoṇṭirikkukayāṇ", hint: "" },
      { en: "How do you say this word in Malayalam?", mr: "ഈ വാക്ക് മലയാളത്തിൽ എങ്ങനെ പറയുന്നു?", roman: "ī vākku malayāḷattil eṅṅane paṛayunnu?", hint: "" }
    ]
  },
  travel_shopping: {
    name: "Travel & shopping",
    color: "#3182CE",
    icon: "🛒",
    phrases: [
      { en: "Where is the bus stand from here?", mr: "ഇവിടെ നിന്ന് ബസ് സ്റ്റാൻഡ് എവിടെയാണ്?", roman: "iviṭe ninn bas sṟṟāṇṭ evideyāṇ?", hint: "" },
      { en: "How much does this cost?", mr: "ഇതിന് എന്തു വിലയാണ്?", roman: "itinu entu vilayāṇ?", hint: "" },
      { en: "That is too expensive; can you reduce the price a little?", mr: "അത് വളരെ വില കൂടുതലാണ്; കുറച്ച് കുറയ്ക്കാമോ?", roman: "at vaḷare vila kūtutalāṇ; kureśś kuṛaykkāmō?", hint: "" },
      { en: "Where is the toilet?", mr: "ടോയ്‌ലറ്റ് എവിടെയാണ്?", roman: "ṭōyleṭṭ evideyāṇ?", hint: "Also: കക്കൂസ് എവിടെയാണ്?" },
      { en: "Please stop the vehicle here; I want to get down", mr: "വണ്ടി ഇവിടെ നിർത്തൂ; എനിക്ക് ഇറങ്ങണം", roman: "vaṇṭi ivide nirtthū; enikk iṟaṅṅaṁ", hint: "" },
      { en: "Have a safe and pleasant journey", mr: "യാത്ര ശുഭമാകട്ടെ", roman: "yātra śubhamākaṭṭe", hint: "" },
      { en: "Can you help me with this bag?", mr: "ഈ ബാഗിൽ സഹായിക്കാമോ?", roman: "ī bāgil sahāyikkāmō?", hint: "" }
    ]
  },
  wishes_emotions: {
    name: "Wishes & feelings",
    color: "#D69E2E",
    icon: "❤️",
    phrases: [
      { en: "Good luck; may things go well for you", mr: "ഭാഗ്യമുണ്ടാകട്ടെ; നല്ലതു വരട്ടെ", roman: "bhāgyamuṇṭākaṭṭe; nallatu varaṭṭe", hint: "" },
      { en: "Congratulations on your success", mr: "നിങ്ങളുടെ വിജയത്തിൽ അഭിനന്ദനങ്ങൾ", roman: "niṅṅaḷuṭe vijayattil abhinandaṅṅaḷ", hint: "" },
      { en: "Get well soon; take enough rest", mr: "വേഗം സുഖം പ്രാപിക്കുക; നന്നായി വിശ്രമിക്കുക", roman: "vēgaṁ sukhaṁ prāpikkuka; nannāyi viśramikkuka", hint: "" },
      { en: "I love you (to someone close)", mr: "ഞാൻ നിന്നെ സ്നേഹിക്കുന്നു", roman: "njān ninne snēhikkunnu", hint: "Context: close relationships" },
      { en: "Do not worry; everything will be fine", mr: "വിഷമിക്കേണ്ട; എല്ലാം ശരിയാകും", roman: "viṣamikkēṇṭa; ellāṁ śariyākuṁ", hint: "" },
      { en: "This place is very beautiful; I like Kerala", mr: "ഈ സ്ഥലം വളരെ മനോഹരമാണ്; എനിക്ക് കേരളം ഇഷ്ടമാണ്", roman: "ī sthalaṁ vaḷare manōharamāṇ; enikk kēraḷaṁ iṣṭamāṇ", hint: "" }
    ]
  }
};

const MALAYALAM_DICTIONARY = {
  greetings: {
    name: "Greetings & courtesy",
    words: [
      { en: "Hello / respect", mr: "നമസ്കാരം", roman: "namaskāram" },
      { en: "Thank you", mr: "നന്ദി", roman: "nandi" },
      { en: "You are welcome (reply)", mr: "സ്വാഗതം", roman: "svāgataṃ" },
      { en: "Please", mr: "ദയവായി", roman: "dayavāyi" },
      { en: "Sorry / excuse me", mr: "ക്ഷമിക്കണം", roman: "kṣamikkaṇam" },
      { en: "Yes", mr: "അതെ", roman: "ate" },
      { en: "No", mr: "ഇല്ല", roman: "illa" },
      { en: "Good morning", mr: "സുപ്രഭാതം", roman: "suprabhātam" },
      { en: "Good night", mr: "ശുഭ രാത്രി", roman: "śubha rātri" },
      { en: "How are you?", mr: "എങ്ങനെയുണ്ട്?", roman: "eṅṅaneyuṇṭ?" },
      { en: "Fine / well", mr: "സുഖം", roman: "sukhaṁ" }
    ]
  },
  people_family: {
    name: "People & family",
    words: [
      { en: "mother", mr: "അമ്മ", roman: "amma" },
      { en: "father", mr: "അച്ഛൻ", roman: "acchan" },
      { en: "elder brother", mr: "അണ്ണൻ", roman: "aṇṇan" },
      { en: "elder sister", mr: "ചേച്ചി", roman: "cēcci" },
      { en: "younger sibling", mr: "അനുജൻ / അനുജത്തി", roman: "anujan / anujatti" },
      { en: "friend", mr: "സുഹൃത്ത്", roman: "suhr̥tt" },
      { en: "child", mr: "കുട്ടി", roman: "kuṭṭi" },
      { en: "man", mr: "പുരുഷൻ", roman: "puruṣan" },
      { en: "woman", mr: "സ്ത്രീ", roman: "strī" },
      { en: "guest", mr: "അതിഥി", roman: "atithi" }
    ]
  },
  home_daily: {
    name: "Home & daily life",
    words: [
      { en: "house / home", mr: "വീട്", roman: "vīṭ" },
      { en: "room", mr: "മുറി", roman: "muṟi" },
      { en: "door", mr: "വാതിൽ", roman: "vātil" },
      { en: "window", mr: "ജനല്‍", roman: "janal" },
      { en: "water", mr: "വെള്ളം", roman: "veḷḷaṁ" },
      { en: "food / meal", mr: "ഭക്ഷണം", roman: "bhakṣaṇaṁ" },
      { en: "rice (cooked)", mr: "ചോറ്", roman: "cōṟ" },
      { en: "work", mr: "ജോലി", roman: "jōli" },
      { en: "sleep", mr: "ഉറക്കം", roman: "uṟakkaṁ" },
      { en: "today", mr: "ഇന്ന്", roman: "inn" },
      { en: "tomorrow", mr: "നാളെ", roman: "nāḷe" },
      { en: "yesterday", mr: "ഇന്നലെ", roman: "innale" }
    ]
  },
  travel: {
    name: "Travel & places",
    words: [
      { en: "road", mr: "പാത", roman: "pāta" },
      { en: "bus", mr: "ബസ്", roman: "bas" },
      { en: "train", mr: "ട്രെയിൻ", roman: "ṭreyin" },
      { en: "ticket", mr: "ടിക്കറ്റ്", roman: "ṭikkaṭ" },
      { en: "where", mr: "എവിടെ", roman: "evide" },
      { en: "here", mr: "ഇവിടെ", roman: "iviṭe" },
      { en: "there", mr: "അവിടെ", roman: "aviṭe" },
      { en: "near", mr: "അടുത്ത്", roman: "aṭutt" },
      { en: "far", mr: "അകലെ", roman: "akale" },
      { en: "left", mr: "ഇടത്", roman: "iṭat" },
      { en: "right", mr: "വലത്", roman: "valat" },
      { en: "straight ahead", mr: "നേരെ മുന്നോട്ട്", roman: "nēre munnōṭ" }
    ]
  },
  nature: {
    name: "Nature & weather",
    words: [
      { en: "sun", mr: "സൂര്യൻ", roman: "sūryan" },
      { en: "moon", mr: "ചന്ദ്രൻ", roman: "candran" },
      { en: "rain", mr: "മഴ", roman: "maḻa" },
      { en: "wind", mr: "കാറ്റ്", roman: "kāṭṭ" },
      { en: "tree", mr: "മരം", roman: "maraṁ" },
      { en: "flower", mr: "പൂവ്", roman: "pūv" },
      { en: "river", mr: "നദി", roman: "nadi" },
      { en: "sea", mr: "കടൽ", roman: "kaḍal" },
      { en: "hot (weather)", mr: "ചൂട്", roman: "cūṭ" },
      { en: "cold", mr: "തണുപ്പ്", roman: "taṇup" }
    ]
  },
  learning: {
    name: "Learning Malayalam",
    words: [
      { en: "Malayalam (language)", mr: "മലയാളം", roman: "malayāḷaṁ" },
      { en: "letter / script", mr: "അക്ഷരം", roman: "akṣaraṁ" },
      { en: "word", mr: "വാക്ക്", roman: "vākku" },
      { en: "sentence", mr: "വാക്യം", roman: "vākyaṁ" },
      { en: "to read", mr: "വായിക്കുക", roman: "vāyikkuka" },
      { en: "to write", mr: "എഴുതുക", roman: "eḻutuka" },
      { en: "to speak", mr: "പറയുക", roman: "paṛayuka" },
      { en: "meaning", mr: "അർത്ഥം", roman: "artthaṁ" },
      { en: "book", mr: "പുസ്തകം", roman: "pustakaṁ" },
      { en: "teacher", mr: "അധ്യാപകൻ", roman: "adhyāpakan" },
      { en: "student", mr: "വിദ്യാർത്ഥി", roman: "vidyārththi" }
    ]
  }
};
