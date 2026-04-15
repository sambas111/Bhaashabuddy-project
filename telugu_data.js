// Telugu phrases & dictionary – Phrases and Words tabs (Lessons use data_telugu.json)
const TELUGU_PHRASES = {
  greetings_1: {
    name: "Telugu Greetings",
    color: "#2B6CB0",
    icon: "👋",
    phrases: [
      { en: "Hello / Namaste", mr: "నమస్తే", roman: "namastē", hint: "" },
      { en: "How are you? (formal)", mr: "మీరు ఎలా ఉన్నారు?", roman: "mīru elā unnāru?", hint: "" },
      { en: "How are you? (informal)", mr: "ఎలా ఉన్నావు?", roman: "elā unnāvu?", hint: "" },
      { en: "I am fine", mr: "నేను బాగున్నాను", roman: "nēnu bāgunnānu", hint: "" },
      { en: "Good morning", mr: "శుభోదయం", roman: "śubhōdayaṃ", hint: "" },
      { en: "Good evening", mr: "శుభ సాయంత్రం", roman: "śubha sāyantraṃ", hint: "" },
      { en: "Good night", mr: "శుభరాత్రి", roman: "śubharātri", hint: "" },
      { en: "What is your name?", mr: "మీ పేరు ఏమిటి?", roman: "mī pēru ēmiṭi?", hint: "" },
      { en: "My name is…", mr: "నా పేరు …", roman: "nā pēru …", hint: "" },
      { en: "Thank you", mr: "ధన్యవాదాలు", roman: "dhanyavādālu", hint: "" },
      { en: "Please", mr: "దయచేసి", roman: "dayacēsi", hint: "" },
      { en: "Sorry", mr: "క్షమించండి", roman: "kṣamin̄caṇḍi", hint: "" },
      { en: "Welcome", mr: "స్వాగతం", roman: "svāgataṃ", hint: "" },
      { en: "Nice to meet you", mr: "మిమ్మల్ని కలవడం సంతోషం", roman: "mimmalni kalavaḍaṃ saṃtōṣaṃ", hint: "" },
      { en: "See you again", mr: "మళ్లీ కలుద్దాం", roman: "mallī kaluddāṃ", hint: "" },
      { en: "Goodbye", mr: "వీడ్కోలు", roman: "vīḍkōlu", hint: "" },
      { en: "Come in", mr: "లోపలికి రండి", roman: "lōpaliki raṇḍi", hint: "" },
      { en: "Sit down", mr: "కూర్చోండి", roman: "kūrcōṇḍi", hint: "" }
    ]
  },
  travel_1: {
    name: "Travel",
    color: "#38A169",
    icon: "🚌",
    phrases: [
      { en: "Where is the bus stop?", mr: "బస్ స్టాప్ ఎక్కడ ఉంది?", roman: "bas sṭāp ekkaḍa undi?", hint: "" },
      { en: "Where is the railway station?", mr: "రైల్వే స్టేషన్ ఎక్కడ ఉంది?", roman: "railve sṭēṣan ekkaḍa undi?", hint: "" },
      { en: "I want to go to…", mr: "నేను … కి వెళ్ళాలి", roman: "nēnu … ki veḷḷāli", hint: "" },
      { en: "How far is it?", mr: "ఎంత దూరం?", roman: "eṃta dūraṃ?", hint: "" },
      { en: "One ticket to Hyderabad", mr: "హైదరాబాద్‌కు ఒక టిక్కెట్", roman: "haidarābāḍku oka ṭikkeṭ", hint: "" },
      { en: "Stop here", mr: "ఇక్కడ ఆపండి", roman: "ikkaḍa āpaṇḍi", hint: "" },
      { en: "Turn left", mr: "ఎడమవైపు తిరగండి", roman: "eḍamavaipu tiragaṇḍi", hint: "" },
      { en: "Turn right", mr: "కుడివైపు తిరగండి", roman: "kuḍivaipu tiragaṇḍi", hint: "" },
      { en: "Go straight", mr: "నేరుగా వెళ్ళండి", roman: "nērugā veḷḷaṇḍi", hint: "" },
      { en: "How much is the fare?", mr: "చార్జి ఎంత?", roman: "cārji eṃta?", hint: "" },
      { en: "I am lost", mr: "నాకు దారి తెలియడం లేదు", roman: "nāku dāri teliyaḍaṃ lēdu", hint: "" },
      { en: "Where is the hotel?", mr: "హోటల్ ఎక్కడ ఉంది?", roman: "hōṭal ekkaḍa undi?", hint: "" },
      { en: "Call a taxi", mr: "ఒక టాక్సీ పిలవండి", roman: "oka ṭāksī pilavaṇḍi", hint: "" },
      { en: "When does the train leave?", mr: "రైలు ఎప్పుడు బయలుదేరుతుంది?", roman: "railu eppuḍu bayaludērutundi?", hint: "" },
      { en: "Which platform?", mr: "ఏ ప్లాట్‌ఫారం?", roman: "ē plāṭphāraṃ?", hint: "" },
      { en: "Is this seat taken?", mr: "ఈ సీట్ ఖాళీగా ఉందా?", roman: "ī sīṭ khāḷīgā undā?", hint: "" }
    ]
  },
  food_1: {
    name: "Food",
    color: "#DD6B20",
    icon: "🍛",
    phrases: [
      { en: "I am hungry", mr: "నాకు ఆకలిగా ఉంది", roman: "nāku ākaligā undi", hint: "" },
      { en: "Give me water", mr: "నాకు నీరు ఇవ్వండి", roman: "nāku nīru ivvaṇḍi", hint: "" },
      { en: "The food is delicious", mr: "ఆహారం చాలా రుచిగా ఉంది", roman: "āhāraṃ cālā rucigā undi", hint: "" },
      { en: "I am vegetarian", mr: "నేను శాకాహారిని", roman: "nēnu śākāhārini", hint: "" },
      { en: "Not too spicy", mr: "ఎక్కువ మసాలా వేయొద్దు", roman: "ekkuva masālā veyoddu", hint: "" },
      { en: "Bring the bill", mr: "బిల్లు తీసుకురండి", roman: "billu tīsukuraṇḍi", hint: "" },
      { en: "Tea without sugar", mr: "చక్కెర లేకుండా టీ", roman: "cakkera lēkuṇḍā ṭī", hint: "" },
      { en: "What do you recommend?", mr: "మీరు ఏమి సిఫారసు చేస్తారు?", roman: "mīru ēmi siphārasu cēstāru?", hint: "" },
      { en: "One plate of rice", mr: "అన్నం ఒక ప్లేటు", roman: "annaṃ oka plēṭu", hint: "" },
      { en: "Is this pure veg?", mr: "ఇది శుద్ధ శాకాహారమా?", roman: "idi śuddha śākāhāramā?", hint: "" },
      { en: "Less oil, please", mr: "తక్కువ నూనె, దయచేసి", roman: "takkuva nūne, dayacēsi", hint: "" },
      { en: "Breakfast time?", mr: "ఉదయం భోజనం ఎప్పుడు?", roman: "udayaṃ bhōjanaṃ eppuḍu?", hint: "" },
      { en: "Table for two", mr: "ఇద్దరికి టేబుల్", roman: "iddariki ṭēbul", hint: "" },
      { en: "I would like juice", mr: "నాకు జ్యూస్ కావాలి", roman: "nāku jyūs kāvāli", hint: "" },
      { en: "Pack this to go", mr: "దీన్ని ప్యాక్ చేయండి", roman: "dīnni pyāk cēyaṇḍi", hint: "" }
    ]
  },
  daily_1: {
    name: "Daily life",
    color: "#805AD5",
    icon: "🏠",
    phrases: [
      { en: "What time is it?", mr: "ఇప్పుడు గంట ఎంత అయింది?", roman: "ippuḍu gaṇṭa eṃta ayindi?", hint: "" },
      { en: "Where do you live?", mr: "మీరు ఎక్కడ నివసిస్తారు?", roman: "mīru ekkaḍa nivasistāru?", hint: "" },
      { en: "I live in Hyderabad", mr: "నేను హైదరాబాద్‌లో నివసిస్తున్నాను", roman: "nēnu haidarābāḍlō nivasistunnānu", hint: "" },
      { en: "What work do you do?", mr: "మీరు ఏ పని చేస్తారు?", roman: "mīru ē pani cēstāru?", hint: "" },
      { en: "I need to go home", mr: "నేను ఇంటికి వెళ్ళాలి", roman: "nēnu iṇṭiki veḷḷāli", hint: "" },
      { en: "Open the door", mr: "తలుపు తెరవండి", roman: "talupu teravaṇḍi", hint: "" },
      { en: "Switch on the light", mr: "లైట్ వెలిగించండి", roman: "laiṭ veligiṃcaṇḍi", hint: "" },
      { en: "What day is today?", mr: "ఈ రోజు ఏ రోజు?", roman: "ī rōju ē rōju?", hint: "" },
      { en: "I am tired", mr: "నాకు అలసటగా ఉంది", roman: "nāku alasaṭagā undi", hint: "" },
      { en: "The weather is nice", mr: "వాతావరణం బాగుంది", roman: "vātāvaraṇaṃ bāgundi", hint: "" },
      { en: "It is very hot", mr: "చాలా వేడిగా ఉంది", roman: "cālā vēḍigā undi", hint: "" },
      { en: "Let us take a walk", mr: "సాయంకాలం నడుద్దాం", roman: "sāyaṃkālaṃ naḍuddāṃ", hint: "" },
      { en: "I will call you", mr: "నేను మీకు ఫోన్ చేస్తాను", roman: "nēnu mīku phōn cēstānu", hint: "" },
      { en: "Wake up", mr: "లేచండి", roman: "lēcaṇḍi", hint: "" },
      { en: "I will come tomorrow", mr: "నేను రేపు వస్తాను", roman: "nēnu rēpu vastānu", hint: "" }
    ]
  },
  shopping_1: {
    name: "Shopping",
    color: "#D69E2E",
    icon: "🛒",
    phrases: [
      { en: "How much does this cost?", mr: "దీని ధర ఎంత?", roman: "dīni dhara eṃta?", hint: "" },
      { en: "It is expensive", mr: "ఇది ఖరీదు", roman: "idi kharīdu", hint: "" },
      { en: "Lower the price, please", mr: "ధర తగ్గించండి, దయచేసి", roman: "dhara taggiṃcaṇḍi, dayacēsi", hint: "" },
      { en: "Show me that one", mr: "ఆది చూపించండి", roman: "ādi cūpiṃcaṇḍi", hint: "" },
      { en: "I want to buy this", mr: "దీన్ని కొనాలని ఉంది", roman: "dīnni konālani undi", hint: "" },
      { en: "Do you have change?", mr: "మార్పు ఉందా?", roman: "mārpu undā?", hint: "" },
      { en: "Where is the market?", mr: "మార్కెట్ ఎక్కడ ఉంది?", roman: "mārkeṭ ekkaḍa undi?", hint: "" },
      { en: "One kilogram of potatoes", mr: "బంగాళదుంప ఒక కిలో", roman: "baṃgāḷaduṃpa oka kilo", hint: "" },
      { en: "Give me a bag", mr: "ఒక సంచి ఇవ్వండి", roman: "oka saṃci ivvaṇḍi", hint: "" },
      { en: "Is the shop open?", mr: "దుకాణం తెరిచి ఉందా?", roman: "dukāṇaṃ terici undā?", hint: "" },
      { en: "Fresh vegetables", mr: "తాజా కూరగాయలు", roman: "tājā kūragāyalu", hint: "" },
      { en: "No plastic bag", mr: "ప్లాస్టిక్ బ్యాగ్ వద్దు", roman: "plāsṭik byāg vaddu", hint: "" },
      { en: "Receipt, please", mr: "రసీదు ఇవ్వండి", roman: "rasīdu ivvaṇḍi", hint: "" },
      { en: "Discount?", mr: "డిస్కౌంట్ ఉందా?", roman: "ḍiskauṇṭ undā?", hint: "" },
      { en: "Cash only", mr: "నగదు మాత్రమే", roman: "nagadu mātramē", hint: "" }
    ]
  },
  emergency_1: {
    name: "Emergency",
    color: "#E53E3E",
    icon: "🚨",
    phrases: [
      { en: "Help!", mr: "సహాయం!", roman: "sahāyaṃ!", hint: "" },
      { en: "Call the police", mr: "పోలీసులను పిలవండి", roman: "pōlīsulanu pilavaṇḍi", hint: "" },
      { en: "Call a doctor", mr: "డాక్టర్‌ను పిలవండి", roman: "ḍākṭarnu pilavaṇḍi", hint: "" },
      { en: "I need a hospital", mr: "నాకు ఆస్పత్రి కావాలి", roman: "nāku āspatri kāvāli", hint: "" },
      { en: "There is a fire", mr: "అగ్నిప్రమాదం జరిగింది", roman: "agnipramādaṃ jarigindi", hint: "" },
      { en: "Accident", mr: "ప్రమాదం జరిగింది", roman: "pramādaṃ jarigindi", hint: "" },
      { en: "I have chest pain", mr: "నా ఛాతీ నొప్పి", roman: "nā chātī noppi", hint: "" },
      { en: "Where is the pharmacy?", mr: "ఫార్మసీ ఎక్కడ ఉంది?", roman: "phārmasī ekkaḍa undi?", hint: "" },
      { en: "Ambulance", mr: "ఆంబులెన్స్", roman: "āṃbulens", hint: "" },
      { en: "Please help me", mr: "దయచేసి నాకు సహాయం చేయండి", roman: "dayacēsi nāku sahāyaṃ cēyaṇḍi", hint: "" },
      { en: "I lost my phone", mr: "నా ఫోన్ పోయింది", roman: "nā phōn pōyindi", hint: "" },
      { en: "Police station?", mr: "పోలీస్ స్టేషన్ ఎక్కడ?", roman: "pōlīs sṭēṣan ekkaḍa?", hint: "" },
      { en: "I feel dizzy", mr: "నాకు తిరుగుతోంది", roman: "nāku tirugutōndi", hint: "" },
      { en: "Bleeding", mr: "రక్తం కారుతోంది", roman: "raktaṃ kārutōndi", hint: "" },
      { en: "Emergency number", mr: "అత్యవసర నంబర్", roman: "atyavasara nambar", hint: "" }
    ]
  }
};

const TELUGU_DICTIONARY = {
  greetings: {
    name: "Greetings & Basics",
    words: [
      { en: "Hello / Namaste", mr: "నమస్తే", roman: "namastē" },
      { en: "Good morning", mr: "శుభోదయం", roman: "śubhōdayaṃ" },
      { en: "Good afternoon", mr: "శుభ మధ్యాహ్నం", roman: "śubha madhyāhnaṃ" },
      { en: "Good evening", mr: "శుభ సాయంత్రం", roman: "śubha sāyantraṃ" },
      { en: "Good night", mr: "శుభరాత్రి", roman: "śubharātri" },
      { en: "How are you? (informal)", mr: "ఎలా ఉన్నావు?", roman: "elā unnāvu?" },
      { en: "How are you? (formal/plural)", mr: "ఎలా ఉన్నారు?", roman: "elā unnāru?" },
      { en: "I am fine", mr: "నేను బాగున్నాను", roman: "nēnu bāgunnānu" },
      { en: "What is your name?", mr: "నీ పేరు ఏమిటి?", roman: "nī pēru ēmiṭi?" },
      { en: "My name is …", mr: "నా పేరు …", roman: "nā pēru …" },
      { en: "Thank you", mr: "ధన్యవాదాలు", roman: "dhanyavādālu" },
      { en: "Please", mr: "దయచేసి", roman: "dayacēsi" },
      { en: "Yes", mr: "అవును", roman: "avunu" },
      { en: "No", mr: "కాదు", roman: "kādu" },
      { en: "Excuse me / Sorry", mr: "క్షమించండి", roman: "kṣamin̄caṇḍi" },
      { en: "Welcome", mr: "స్వాగతం", roman: "svāgataṃ" },
      { en: "See you again", mr: "మళ్లీ కలుద్దాం", roman: "mallī kaluddāṃ" },
      { en: "Good bye", mr: "వీడ్కోలు", roman: "vīḍkōlu" },
      { en: "This (near, generic)", mr: "ఇది", roman: "idi" },
      { en: "That (far, generic)", mr: "అది", roman: "adi" }
    ]
  },
  reading: {
    name: "Reading",
    words: [
      { en: "book", mr: "పుస్తకం", roman: "pustakaṃ" },
      { en: "to read", mr: "చదువు", roman: "caduvu" },
      { en: "letter", mr: "అక్షరం", roman: "akṣaraṃ" },
      { en: "word", mr: "పదం", roman: "padaṃ" },
      { en: "sentence", mr: "వాక్యం", roman: "vākyaṃ" },
      { en: "story", mr: "కథ", roman: "katha" },
      { en: "newspaper", mr: "వార్తాపత్రిక", roman: "vārtāpatrika" },
      { en: "magazine", mr: "మ్యాగజైన్", roman: "myāgajain" },
      { en: "page", mr: "పేజీ", roman: "pējī" },
      { en: "paragraph", mr: "పేరా", roman: "pērā" }
    ]
  },
  writing: {
    name: "Writing & Script",
    words: [
      { en: "to write", mr: "రాయు", roman: "rāyu" },
      { en: "pen", mr: "పెన్", roman: "pen" },
      { en: "pencil", mr: "పెన్సిల్", roman: "pensil" },
      { en: "paper", mr: "కాగితం", roman: "kāgitaṃ" },
      { en: "notebook", mr: "నోట్బుక్", roman: "nōṭbuk" },
      { en: "script", mr: "లిపి", roman: "lipi" },
      { en: "alphabet", mr: "అక్షరమాల", roman: "akṣaramāla" },
      { en: "vowel", mr: "అచ్చు", roman: "accu" },
      { en: "consonant", mr: "హల్లు", roman: "hallu" },
      { en: "signature", mr: "సంతకం", roman: "saṃtakaṃ" }
    ]
  },
  numbers: {
    name: "Numbers",
    words: [
      { en: "zero", mr: "సున్నా", roman: "sunnā" },
      { en: "one", mr: "ఒక్కటి", roman: "okkaṭi" },
      { en: "two", mr: "రెండు", roman: "reṇḍu" },
      { en: "three", mr: "మూడు", roman: "mūḍu" },
      { en: "four", mr: "నాలుగు", roman: "nālugu" },
      { en: "five", mr: "ఐదు", roman: "aidu" },
      { en: "six", mr: "ఆరు", roman: "āru" },
      { en: "seven", mr: "ఏడు", roman: "ēḍu" },
      { en: "eight", mr: "ఎనిమిది", roman: "enimidi" },
      { en: "nine", mr: "తొమ్మిది", roman: "tommidi" },
      { en: "ten", mr: "పది", roman: "padi" },
      { en: "twenty", mr: "ఇరవై", roman: "iravai" },
      { en: "fifty", mr: "యాబై", roman: "yābai" },
      { en: "hundred", mr: "వంద", roman: "vanda" },
      { en: "thousand", mr: "వెయ్యి", roman: "veyyi" }
    ]
  },
  animals: {
    name: "Animals & Nature",
    words: [
      { en: "dog", mr: "కుక్క", roman: "kukka" },
      { en: "cat", mr: "పిల్లి", roman: "pilli" },
      { en: "cow", mr: "ఆవు", roman: "āvu" },
      { en: "buffalo", mr: "ఎద్దు", roman: "eddu" },
      { en: "goat", mr: "మేక", roman: "mēka" },
      { en: "sheep", mr: "గొర్రె", roman: "gorre" },
      { en: "horse", mr: "గుర్రం", roman: "gurraṃ" },
      { en: "elephant", mr: "ఏనుగు", roman: "ēnugu" },
      { en: "tiger", mr: "పులి", roman: "puli" },
      { en: "lion", mr: "సింహం", roman: "siṃhaṃ" },
      { en: "monkey", mr: "కోతి", roman: "kōti" },
      { en: "snake", mr: "పాము", roman: "pāmu" },
      { en: "bird", mr: "పక్షి", roman: "pakṣi" },
      { en: "fish", mr: "చేప", roman: "cēpa" },
      { en: "crocodile", mr: "మొసలి", roman: "mosali" }
    ]
  },
  dailyLife: {
    name: "Daily Life",
    words: [
      { en: "house", mr: "ఇల్లు", roman: "illu" },
      { en: "room", mr: "గది", roman: "gadi" },
      { en: "door", mr: "తలుపు", roman: "talupu" },
      { en: "window", mr: "కిటికీ", roman: "kiṭikī" },
      { en: "water", mr: "నీరు", roman: "nīru" },
      { en: "food", mr: "ఆహారం", roman: "āhāraṃ" },
      { en: "sleep", mr: "నిద్ర", roman: "nidra" },
      { en: "work", mr: "పని", roman: "pani" },
      { en: "money", mr: "డబ్బు", roman: "ḍabbu" },
      { en: "day", mr: "రోజు", roman: "rōju" },
      { en: "night", mr: "రాత్రి", roman: "rātri" },
      { en: "morning", mr: "ఉదయం", roman: "udayaṃ" },
      { en: "evening", mr: "సాయంత్రం", roman: "sāyantraṃ" },
      { en: "today", mr: "ఈ రోజు", roman: "ī rōju" },
      { en: "tomorrow", mr: "రేపు", roman: "rēpu" }
    ]
  },
  environment: {
    name: "Environment & Weather",
    words: [
      { en: "sun", mr: "సూర్యుడు", roman: "sūryuḍu" },
      { en: "moon", mr: "చంద్రుడు", roman: "candruḍu" },
      { en: "rain", mr: "వర్షం", roman: "varṣaṃ" },
      { en: "cloud", mr: "మేఘం", roman: "mēghaṃ" },
      { en: "wind", mr: "గాలి", roman: "gāli" },
      { en: "hot", mr: "వేడి", roman: "vēḍi" },
      { en: "cold", mr: "చలి", roman: "cali" },
      { en: "tree", mr: "చెట్టు", roman: "ceṭṭu" },
      { en: "flower", mr: "పువ్వు", roman: "puvvu" },
      { en: "earth", mr: "భూమి", roman: "bhūmi" }
    ]
  },
  food: {
    name: "Food & Drink",
    words: [
      { en: "rice", mr: "బియ్యం", roman: "biyyaṃ" },
      { en: "bread", mr: "రొట్టె", roman: "roṭṭe" },
      { en: "vegetable", mr: "కూరగాయలు", roman: "kūragāyalu" },
      { en: "fruit", mr: "పండు", roman: "paṇḍu" },
      { en: "milk", mr: "పాలు", roman: "pālu" },
      { en: "curd", mr: "పెరుగు", roman: "perugu" },
      { en: "salt", mr: "ఉప్పు", roman: "uppu" },
      { en: "sugar", mr: "చక్కెర", roman: "cakkera" },
      { en: "oil", mr: "నూనె", roman: "nūne" },
      { en: "water", mr: "నీరు", roman: "nīru" },
      { en: "tea", mr: "టీ", roman: "ṭī" },
      { en: "coffee", mr: "కాఫీ", roman: "kāphī" },
      { en: "eat", mr: "తిను", roman: "tinu" },
      { en: "drink", mr: "త్రాగు", roman: "trāgu" },
      { en: "cook", mr: "వంటచేయు", roman: "vaṇṭacēyu" }
    ]
  },
  health: {
    name: "Health & Body",
    words: [
      { en: "head", mr: "తల", roman: "tala" },
      { en: "eye", mr: "కన్ను", roman: "kannu" },
      { en: "ear", mr: "చెవి", roman: "cevi" },
      { en: "nose", mr: "ముక్కు", roman: "mukku" },
      { en: "mouth", mr: "నోరు", roman: "nōru" },
      { en: "hand", mr: "చెయ్యి", roman: "ceyyi" },
      { en: "leg", mr: "కాలు", roman: "kālu" },
      { en: "heart", mr: "గుండె", roman: "guṇḍe" },
      { en: "stomach", mr: "కడుపు", roman: "kaḍupu" },
      { en: "doctor", mr: "డాక్టర్", roman: "ḍākṭar" },
      { en: "medicine", mr: "మందు", roman: "mandu" },
      { en: "hospital", mr: "ఆసుపత్రి", roman: "āsupatri" },
      { en: "pain", mr: "నొప్పి", roman: "noppi" },
      { en: "fever", mr: "జ్వరం", roman: "jvaraṃ" }
    ]
  },
  schoolWork: {
    name: "School & Work",
    words: [
      { en: "school", mr: "బడి", roman: "baḍi" },
      { en: "teacher", mr: "ఉపాధ్యాయుడు", roman: "upādhyāyuḍu" },
      { en: "student", mr: "విద్యార్థి", roman: "vidyārthi" },
      { en: "to study", mr: "చదువు", roman: "caduvu" },
      { en: "exam", mr: "పరీక్ష", roman: "parīkṣa" },
      { en: "job", mr: "ఉద్యోగం", roman: "udyōgaṃ" },
      { en: "office", mr: "ఆఫీసు", roman: "āphīsu" },
      { en: "salary", mr: "జీతం", roman: "jītaṃ" },
      { en: "meeting", mr: "మీటింగ్", roman: "mīṭiṅg" },
      { en: "business", mr: "వ్యాపారం", roman: "vyāpāraṃ" }
    ]
  },
  socialInteractions: {
    name: "Social & People",
    words: [
      { en: "father", mr: "నాన్న", roman: "nānna" },
      { en: "mother", mr: "అమ్మ", roman: "amma" },
      { en: "brother", mr: "సోదరుడు", roman: "sōdaruḍu" },
      { en: "sister", mr: "సోదరి", roman: "sōdari" },
      { en: "friend", mr: "స్నేహితుడు", roman: "snēhituḍu" },
      { en: "child", mr: "బిడ్డ", roman: "biḍḍa" },
      { en: "man", mr: "మనిషి", roman: "maniṣi" },
      { en: "woman", mr: "అమ్మాయి", roman: "ammāyi" },
      { en: "family", mr: "కుటుంబం", roman: "kuṭuṃbaṃ" },
      { en: "name", mr: "పేరు", roman: "pēru" }
    ]
  },
  time: {
    name: "Time & Dates",
    words: [
      { en: "time", mr: "సమయం", roman: "samayaṃ" },
      { en: "hour", mr: "గంట", roman: "gaṇṭa" },
      { en: "minute", mr: "నిమిషం", roman: "nimiṣaṃ" },
      { en: "second", mr: "సెకను", roman: "sekannu" },
      { en: "Monday", mr: "సోమవారం", roman: "sōmavāraṃ" },
      { en: "Tuesday", mr: "మంగళవారం", roman: "maṃgaḷavāraṃ" },
      { en: "Wednesday", mr: "బుధవారం", roman: "budhavāraṃ" },
      { en: "Thursday", mr: "గురువారం", roman: "guruvāraṃ" },
      { en: "Friday", mr: "శుక్రవారం", roman: "śukravāraṃ" },
      { en: "Saturday", mr: "శనివారం", roman: "śanivāraṃ" },
      { en: "Sunday", mr: "ఆదివారం", roman: "ādivāraṃ" },
      { en: "week", mr: "వారం", roman: "vāraṃ" },
      { en: "month", mr: "నెల", roman: "nela" },
      { en: "year", mr: "సంవత్సరం", roman: "saṃvatsaraṃ" }
    ]
  },
  transportation: {
    name: "Transportation",
    words: [
      { en: "bus", mr: "బస్సు", roman: "bassu" },
      { en: "train", mr: "రైలు", roman: "railu" },
      { en: "car", mr: "కారు", roman: "kāru" },
      { en: "bicycle", mr: "సైకిల్", roman: "saikil" },
      { en: "auto", mr: "ఆటో", roman: "āṭō" },
      { en: "road", mr: "రోడ్", roman: "rōḍ" },
      { en: "station", mr: "స్టేషన్", roman: "sṭēṣan" },
      { en: "airport", mr: "విమానాశ్రయం", roman: "vimānāśrayaṃ" },
      { en: "to go", mr: "వెళ్ళు", roman: "veḷḷu" },
      { en: "to come", mr: "రా", roman: "rā" }
    ]
  },
  travel: {
    name: "Travel",
    words: [
      { en: "travel", mr: "ప్రయాణం", roman: "prayāṇaṃ" },
      { en: "ticket", mr: "టికెట్", roman: "ṭikeṭ" },
      { en: "hotel", mr: "హోటల్", roman: "hōṭal" },
      { en: "room", mr: "గది", roman: "gadi" },
      { en: "baggage", mr: "సామాను", roman: "sāmānu" },
      { en: "passport", mr: "పాస్పోర్ట్", roman: "pāspōrṭ" },
      { en: "where", mr: "ఎక్కడ", roman: "ekkaḍa" },
      { en: "here", mr: "ఇక్కడ", roman: "ikkaḍa" },
      { en: "there", mr: "అక్కడ", roman: "akkaḍa" },
      { en: "near", mr: "దగ్గర", roman: "daggara" }
    ]
  },
  shopping: {
    name: "Shopping",
    words: [
      { en: "shop", mr: "దుకాణం", roman: "dukāṇaṃ" },
      { en: "market", mr: "మార్కెట్", roman: "mārkeṭ" },
      { en: "price", mr: "ధర", roman: "dhara" },
      { en: "cheap", mr: "చౌక", roman: "cauka" },
      { en: "expensive", mr: "ఖరీదైన", roman: "kharīdaina" },
      { en: "to buy", mr: "కొను", roman: "konu" },
      { en: "to sell", mr: "అమ్ము", roman: "ammu" },
      { en: "how much", mr: "ఎంత", roman: "eṃta" },
      { en: "discount", mr: "డిస్కౌంట్", roman: "ḍiskauṇṭ" },
      { en: "bill", mr: "బిల్లు", roman: "billu" }
    ]
  },
  emergency: {
    name: "Emergency",
    words: [
      { en: "help", mr: "సహాయం", roman: "sahāyaṃ" },
      { en: "police", mr: "పోలీసు", roman: "pōlīsu" },
      { en: "fire", mr: "అగ్ని", roman: "agni" },
      { en: "danger", mr: "అపాయం", roman: "apāyaṃ" },
      { en: "stop", mr: "ఆపు", roman: "āpu" },
      { en: "call", mr: "కాల్ చేయు", roman: "kāl cēyu" },
      { en: "doctor", mr: "డాక్టర్", roman: "ḍākṭar" },
      { en: "ambulance", mr: "ఆంబులెన్స్", roman: "āṃbulens" },
      { en: "I need help", mr: "నాకు సహాయం కావాలి", roman: "nāku sahāyaṃ kāvāli" },
      { en: "emergency", mr: "అత్యవసరం", roman: "atyavasaraṃ" }
    ]
  }
};
