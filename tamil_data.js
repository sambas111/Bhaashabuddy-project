// Tamil phrases & dictionary – for Phrases and Words sections (like Marathi/Kannada)
const TAMIL_PHRASES = {
  greetings: {
    name: "Greetings",
    color: "#2B6CB0",
    icon: "👋",
    phrases: [
      { en: "Hello / Hi", mr: "வணக்கம்", roman: "vaṇakkam", hint: "Universal greeting" },
      { en: "Good morning", mr: "காலை வணக்கம்", roman: "kālai vaṇakkam", hint: "" },
      { en: "Good afternoon", mr: "மதிய வணக்கம்", roman: "matiya vaṇakkam", hint: "" },
      { en: "Good evening", mr: "மாலை வணக்கம்", roman: "mālai vaṇakkam", hint: "" },
      { en: "Good night", mr: "இரவு வணக்கம்", roman: "iravu vaṇakkam", hint: "" },
      { en: "How are you?", mr: "எப்படி இருக்கிறீர்கள்?", roman: "eppaṭi irukkiṟīrkaḷā?", hint: "" },
      { en: "I am fine", mr: "நான் நன்றாக இருக்கிறேன்", roman: "nāṉ naṉṟāka irukkiṟēṉ", hint: "" },
      { en: "What is your name?", mr: "உங்கள் பெயர் என்ன?", roman: "uṅkaḷ peyar eṉṉa?", hint: "" },
      { en: "My name is...", mr: "என் பெயர் ...", roman: "eṉ peyar ...", hint: "" },
      { en: "Nice to meet you", mr: "உங்களை சந்தித்து மகிழ்ச்சி", roman: "uṅkaḷai cantittu makiḻcci", hint: "" },
      { en: "Thank you", mr: "நன்றி", roman: "naṉṟi", hint: "Very common" },
      { en: "Please", mr: "தயவு செய்து", roman: "tayavu ceytu", hint: "" },
      { en: "Sorry / Excuse me", mr: "மன்னிக்கவும்", roman: "maṉṉikkavum", hint: "" },
      { en: "Welcome", mr: "நல்வரவு", roman: "nalvaravu", hint: "" },
      { en: "Goodbye", mr: "சென்று வருகிறேன்", roman: "ceṉṟu varukiṟēṉ", hint: "" },
      { en: "See you later", mr: "பிறகு பார்ப்போம்", roman: "piṟaku pārppōm", hint: "" },
      { en: "Take care", mr: "கவனமாக இருங்கள்", roman: "kavaṉamāka iruṅkaḷ", hint: "" },
      { en: "Happy Birthday", mr: "பிறந்தநாள் வாழ்த்துக்கள்", roman: "piṟantanāḷ vāḻttukkaḷ", hint: "" },
      { en: "Happy Diwali", mr: "தீபாவளி வாழ்த்துக்கள்", roman: "tīpāvaḷi vāḻttukkaḷ", hint: "" },
      { en: "Congratulations", mr: "வாழ்த்துக்கள்", roman: "vāḻttukkaḷ", hint: "" },
      { en: "I love you", mr: "நான் உன்னை நேசிக்கிறேன்", roman: "nāṉ uṉṉai nēcikkiṟēṉ", hint: "" },
      { en: "Get well soon", mr: "விரைவில் குணமடையுங்கள்", roman: "viraivil kuṇamaṭaiyuṅkaḷ", hint: "" },
      { en: "Good luck", mr: "அதிர்ஷ்டம்", roman: "atirṣṭam", hint: "" }
    ]
  },
  travel: {
    name: "Travel",
    color: "#D69E2E",
    icon: "🚗",
    phrases: [
      { en: "Take me to the railway station", mr: "என்னை ரயில் நிலையத்திற்கு அழைத்துச் செல்லுங்கள்", roman: "eṉṉai rayil nilaiyattiṟku aḻaittuc celluṅkaḷ", hint: "" },
      { en: "How much to the market?", mr: "சந்தைக்கு எவ்வளவு?", roman: "cantaikku evvaḷavu?", hint: "" },
      { en: "Stop here", mr: "இங்கே நிறுத்துங்கள்", roman: "iṅkē niṟuttuṅkaḷ", hint: "" },
      { en: "Go straight", mr: "நேராக போங்கள்", roman: "nērāka pōṅkaḷ", hint: "" },
      { en: "Turn left", mr: "இடது பக்கம் திரும்புங்கள்", roman: "iṭatu pakkam tirumpuṅkaḷ", hint: "" },
      { en: "Turn right", mr: "வலது பக்கம் திரும்புங்கள்", roman: "valatu pakkam tirumpuṅkaḷ", hint: "" },
      { en: "Where is the hotel?", mr: "ஹோட்டல் எங்கே?", roman: "hōṭṭal eṅkē?", hint: "" },
      { en: "I need a room", mr: "எனக்கு அறை தேவை", roman: "eṉakku aṟai tēvai", hint: "" },
      { en: "Where is the bathroom?", mr: "குளியலறை எங்கே?", roman: "kuḷiyalaṟai eṅkē?", hint: "" },
      { en: "Bon voyage", mr: "இனிய பயணம்", roman: "iṉiya payaṇam", hint: "" },
      { en: "Welcome to Tamil Nadu", mr: "தமிழ்நாட்டிற்கு வரவேற்கிறோம்", roman: "tamiḻnāṭṭiṟku varavēṟkiṟōm", hint: "" }
    ]
  },
  food: {
    name: "Food & Drink",
    color: "#C05621",
    icon: "🍽️",
    phrases: [
      { en: "Water", mr: "தண்ணீர்", roman: "taṇṇīr", hint: "" },
      { en: "Food", mr: "உணவு", roman: "uṇavu", hint: "" },
      { en: "Rice", mr: "சோறு", roman: "cōṟu", hint: "" },
      { en: "I am hungry", mr: "எனக்கு பசி", roman: "eṉakku paci", hint: "" },
      { en: "I am thirsty", mr: "எனக்கு தாகம்", roman: "eṉakku tākam", hint: "" },
      { en: "Please give me water", mr: "தயவு செய்து தண்ணீர் கொடுங்கள்", roman: "tayavu ceytu taṇṇīr koṭuṅkaḷ", hint: "" },
      { en: "The food is good", mr: "உணவு நல்லது", roman: "uṇavu nallatu", hint: "" },
      { en: "I am vegetarian", mr: "நான் சைவம்", roman: "nāṉ caivam", hint: "" },
      { en: "Bill please", mr: "பில் கொடுங்கள்", roman: "pil koṭuṅkaḷ", hint: "" },
      { en: "Thank you for the meal", mr: "உணவுக்கு நன்றி", roman: "uṇavukku naṉṟi", hint: "" },
      { en: "Mango", mr: "மாம்பழம்", roman: "māmpaḻam", hint: "" },
      { en: "Banana", mr: "வாழைப்பழம்", roman: "vāḻaippaḻam", hint: "" },
      { en: "Coffee", mr: "காபி", roman: "kāpi", hint: "" },
      { en: "Tea", mr: "டீ", roman: "ṭī", hint: "" }
    ]
  },
  shopping: {
    name: "Shopping",
    color: "#805AD5",
    icon: "🛒",
    phrases: [
      { en: "How much is this?", mr: "இதன் விலை எவ்வளவு?", roman: "itaṉ vilai evvaḷavu?", hint: "" },
      { en: "It is too expensive", mr: "மிகவும் விலை அதிகம்", roman: "mikavum vilai atikam", hint: "" },
      { en: "Can you reduce the price?", mr: "விலையைக் குறைக்க முடியுமா?", roman: "vilaiyaik kuṟaikka muṭiyumā?", hint: "" },
      { en: "I need a kilo of rice", mr: "எனக்கு ஒரு கிலோ அரிசி தேவை", roman: "eṉakku oru kilō arici tēvai", hint: "" },
      { en: "Do you have change?", mr: "சில்லறை உள்ளதா?", roman: "cillaṟai uḷḷatā?", hint: "" },
      { en: "Give me a bill", mr: "பில் கொடுங்கள்", roman: "pil koṭuṅkaḷ", hint: "" }
    ]
  },
  emergency: {
    name: "Emergency",
    color: "#E53E3E",
    icon: "🆘",
    phrases: [
      { en: "Help!", mr: "உதவுங்கள்!", roman: "utavuṅkaḷ!", hint: "" },
      { en: "Stop!", mr: "நில்லுங்கள்!", roman: "nilluṅkaḷ!", hint: "" },
      { en: "Call the police!", mr: "காவலர்களை அழைக்கவும்!", roman: "kāvalarkaḷai aḻaikkavum!", hint: "" },
      { en: "I need a doctor", mr: "எனக்கு டாக்டர் தேவை", roman: "eṉakku ṭākṭar tēvai", hint: "" },
      { en: "Where is the hospital?", mr: "மருத்துவமனை எங்கே?", roman: "maruttuvamaṉai eṅkē?", hint: "" },
      { en: "Fire!", mr: "தீ!", roman: "tī!", hint: "" }
    ]
  },
  numbers: {
    name: "Numbers",
    color: "#38A169",
    icon: "#",
    phrases: [
      { en: "One", mr: "ஒன்று", roman: "oṉṟu", hint: "" },
      { en: "Two", mr: "இரண்டு", roman: "iraṇṭu", hint: "" },
      { en: "Three", mr: "மூன்று", roman: "mūṉṟu", hint: "" },
      { en: "Four", mr: "நான்கு", roman: "nāṉku", hint: "" },
      { en: "Five", mr: "ஐந்து", roman: "aintu", hint: "" },
      { en: "Ten", mr: "பத்து", roman: "pattu", hint: "" },
      { en: "Hundred", mr: "நூறு", roman: "nūṟu", hint: "" },
      { en: "Thousand", mr: "ஆயிரம்", roman: "āyiram", hint: "" }
    ]
  },
  reading: {
    name: "Reading",
    color: "#2C5282",
    icon: "📖",
    phrases: [
      { en: "Book", mr: "புத்தகம்", roman: "puttakam", hint: "" },
      { en: "I am reading", mr: "நான் படிக்கிறேன்", roman: "nāṉ paṭikkiṟēṉ", hint: "" },
      { en: "Do you speak Tamil?", mr: "நீங்கள் தமிழ் பேசுவீர்களா?", roman: "nīṅkaḷ tamiḻ pēcuvīrkaḷā?", hint: "" },
      { en: "Yes, a little", mr: "கொஞ்சம் பேசுவேன்", roman: "koñcam pēcuvēṉ", hint: "" },
      { en: "I don't understand", mr: "எனக்குப் புரியவில்லை", roman: "eṉakkup puriyavillai", hint: "" },
      { en: "Please speak slowly", mr: "மெதுவாகப் பேசுங்கள்", roman: "metuvākap pēcuṅkaḷ", hint: "" },
      { en: "Please repeat", mr: "மீண்டும் சொல்லுங்கள்", roman: "mīṇṭum colluṅkaḷ", hint: "" }
    ]
  },
  writing: {
    name: "Writing",
    color: "#744210",
    icon: "✏️",
    phrases: [
      { en: "To write", mr: "எழுது", roman: "eḻutu", hint: "" },
      { en: "Please write it down", mr: "எழுதிக் கொடுங்கள்", roman: "eḻutik koṭuṅkaḷ", hint: "" },
      { en: "Letter", mr: "கடிதம்", roman: "kaṭitam", hint: "" },
      { en: "Pen", mr: "பேனா", roman: "pēṉā", hint: "" }
    ]
  },
  animals: {
    name: "Animals & Nature",
    color: "#276749",
    icon: "🐕",
    phrases: [
      { en: "Dog", mr: "நாய்", roman: "nāy", hint: "" },
      { en: "Cat", mr: "பூனை", roman: "pūṉai", hint: "" },
      { en: "Cow", mr: "பசு", roman: "pacu", hint: "" },
      { en: "Bird", mr: "பறவை", roman: "paṟavai", hint: "" },
      { en: "Elephant", mr: "யானை", roman: "yāṉai", hint: "" },
      { en: "Peacock", mr: "மயில்", roman: "mayil", hint: "" }
    ]
  },
  dailyLife: {
    name: "Daily Life",
    color: "#2B6CB0",
    icon: "🏠",
    phrases: [
      { en: "House", mr: "வீடு", roman: "vīṭu", hint: "" },
      { en: "Today", mr: "இன்று", roman: "iṉṟu", hint: "" },
      { en: "Tomorrow", mr: "நாளை", roman: "nāḷai", hint: "" },
      { en: "Yesterday", mr: "நேற்று", roman: "nēṟṟu", hint: "" },
      { en: "What time is it?", mr: "என்ன மணி?", roman: "eṉṉa maṇi?", hint: "" },
      { en: "I am going to office", mr: "நான் அலுவலகத்திற்குப் போகிறேன்", roman: "nāṉ aluvalakattiṟkup pōkiṟēṉ", hint: "" },
      { en: "Where do you live?", mr: "நீங்கள் எங்கே வசிக்கிறீர்கள்?", roman: "nīṅkaḷ eṅkē vacikkiṟīrkaḷā?", hint: "" },
      { en: "I live in Chennai", mr: "நான் சென்னையில் வசிக்கிறேன்", roman: "nāṉ ceṉṉaiyil vacikkiṟēṉ", hint: "" }
    ]
  },
  environment: {
    name: "Environment & Weather",
    color: "#2F855A",
    icon: "🌤️",
    phrases: [
      { en: "How is the weather today?", mr: "இன்று வானிலை எப்படி?", roman: "iṉṟu vāṉilai eppaṭi?", hint: "" },
      { en: "It is raining", mr: "மழை பெய்துகொண்டிருக்கிறது", roman: "maḻai peytukoṇṭirukkiṟatu", hint: "" },
      { en: "It is hot", mr: "சூடாக உள்ளது", roman: "cūṭāka uḷḷatu", hint: "" },
      { en: "It is cold", mr: "குளிராக உள்ளது", roman: "kuḷirāka uḷḷatu", hint: "" },
      { en: "Sun", mr: "சூரியன்", roman: "cūriyaṉ", hint: "" },
      { en: "Water", mr: "தண்ணீர்", roman: "taṇṇīr", hint: "" }
    ]
  },
  health: {
    name: "Health",
    color: "#C53030",
    icon: "🏥",
    phrases: [
      { en: "I have a headache", mr: "எனக்கு தலைவலி", roman: "eṉakku talaivali", hint: "" },
      { en: "I have fever", mr: "எனக்கு காய்ச்சல்", roman: "eṉakku kāyccal", hint: "" },
      { en: "I have stomach pain", mr: "எனக்கு வயிறு வலி", roman: "eṉakku vayiṟu vali", hint: "" },
      { en: "Doctor", mr: "மருத்துவர்", roman: "maruttuvar", hint: "" },
      { en: "Medicine", mr: "மருந்து", roman: "maruntu", hint: "" },
      { en: "Hospital", mr: "மருத்துவமனை", roman: "maruttuvamaṉai", hint: "" }
    ]
  },
  schoolWork: {
    name: "School & Work",
    color: "#553C9A",
    icon: "📚",
    phrases: [
      { en: "Teacher", mr: "ஆசிரியர்", roman: "āciriyar", hint: "" },
      { en: "Student", mr: "மாணவர்", roman: "māṇavar", hint: "" },
      { en: "I am working", mr: "நான் வேலை செய்கிறேன்", roman: "nāṉ vēlai ceykiṟēṉ", hint: "" },
      { en: "Office", mr: "அலுவலகம்", roman: "aluvalakam", hint: "" },
      { en: "Meeting", mr: "கூட்டம்", roman: "kūṭṭam", hint: "" }
    ]
  },
  socialInteractions: {
    name: "Social & People",
    color: "#B7791F",
    icon: "👥",
    phrases: [
      { en: "Friend", mr: "நண்பர்", roman: "naṇpar", hint: "" },
      { en: "Family", mr: "குடும்பம்", roman: "kuṭumpam", hint: "" },
      { en: "Father", mr: "அப்பா", roman: "appā", hint: "" },
      { en: "Mother", mr: "அம்மா", roman: "ammā", hint: "" },
      { en: "Brother", mr: "அண்ணா / தம்பி", roman: "aṇṇā / tampi", hint: "" },
      { en: "Sister", mr: "அக்கா / தங்கை", roman: "akkā / taṅkai", hint: "" }
    ]
  },
  time: {
    name: "Time & Dates",
    color: "#2C5282",
    icon: "🕐",
    phrases: [
      { en: "Morning", mr: "காலை", roman: "kālai", hint: "" },
      { en: "Evening", mr: "மாலை", roman: "mālai", hint: "" },
      { en: "Night", mr: "இரவு", roman: "iravu", hint: "" },
      { en: "Monday", mr: "திங்கட்கிழமை", roman: "tiṅkaṭkiḻamai", hint: "" },
      { en: "Week", mr: "வாரம்", roman: "vāram", hint: "" },
      { en: "Year", mr: "வருடம்", roman: "varuṭam", hint: "" }
    ]
  },
  tourism: {
    name: "Travel & Tourism",
    color: "#2B6CB0",
    icon: "🗺️",
    phrases: [
      { en: "Temple", mr: "கோயில்", roman: "kōyil", hint: "" },
      { en: "Where is the bus stop?", mr: "பஸ் நிறுத்தம் எங்கே?", roman: "pas niṟuttam eṅkē?", hint: "" },
      { en: "Ticket", mr: "டிக்கெட்", roman: "ṭikkeṭ", hint: "" }
    ]
  },
  transportation: {
    name: "Transportation",
    color: "#2D3748",
    icon: "🚌",
    phrases: [
      { en: "Bus", mr: "பஸ்", roman: "pas", hint: "" },
      { en: "Train", mr: "ரயில்", roman: "rayil", hint: "" },
      { en: "Car", mr: "கார்", roman: "kār", hint: "" },
      { en: "Auto", mr: "ஆட்டோ", roman: "āṭṭō", hint: "" },
      { en: "Where is the station?", mr: "நிலையம் எங்கே?", roman: "nilaiyam eṅkē?", hint: "" }
    ]
  }
};

const TAMIL_DICTIONARY = {
  greetings: {
    name: "Greetings & Basics",
    words: [
      { en: "Hello", mr: "வணக்கம்", roman: "vaṇakkam" },
      { en: "Thank you", mr: "நன்றி", roman: "naṉṟi" },
      { en: "Please", mr: "தயவு செய்து", roman: "tayavu ceytu" },
      { en: "Yes", mr: "ஆமாம்", roman: "āmām" },
      { en: "No", mr: "இல்லை", roman: "illai" },
      { en: "Sorry", mr: "மன்னிக்கவும்", roman: "maṉṉikkavum" },
      { en: "Welcome", mr: "நல்வரவு", roman: "nalvaravu" },
      { en: "Name", mr: "பெயர்", roman: "peyar" },
      { en: "Good", mr: "நல்ல", roman: "nalla" },
      { en: "Bad", mr: "கெட்ட", roman: "keṭṭa" }
    ]
  },
  travel: {
    name: "Travel & Directions",
    words: [
      { en: "Way", mr: "வழி", roman: "vaḻi" },
      { en: "Place", mr: "இடம்", roman: "iṭam" },
      { en: "Here", mr: "இங்கே", roman: "iṅkē" },
      { en: "There", mr: "அங்கே", roman: "aṅkē" },
      { en: "Near", mr: "அருகில்", roman: "arukil" },
      { en: "Far", mr: "தூரம்", roman: "tūram" },
      { en: "Left", mr: "இடது", roman: "iṭatu" },
      { en: "Right", mr: "வலது", roman: "valatu" },
      { en: "Straight", mr: "நேராக", roman: "nērāka" }
    ]
  },
  food: {
    name: "Food & Drink",
    words: [
      { en: "Water", mr: "தண்ணீர்", roman: "taṇṇīr" },
      { en: "Food", mr: "உணவு", roman: "uṇavu" },
      { en: "Rice", mr: "சோறு", roman: "cōṟu" },
      { en: "Milk", mr: "பால்", roman: "pāl" },
      { en: "Coffee", mr: "காபி", roman: "kāpi" },
      { en: "Tea", mr: "டீ", roman: "ṭī" },
      { en: "Salt", mr: "உப்பு", roman: "uppu" },
      { en: "Sugar", mr: "சீனி", roman: "cīṉi" },
      { en: "Vegetable", mr: "காய்கறி", roman: "kāykaṟi" },
      { en: "Fruit", mr: "பழம்", roman: "paḻam" }
    ]
  },
  shopping: {
    name: "Shopping",
    words: [
      { en: "Money", mr: "பணம்", roman: "paṇam" },
      { en: "Price", mr: "விலை", roman: "vilai" },
      { en: "Shop", mr: "கடை", roman: "kaṭai" },
      { en: "Buy", mr: "வாங்கு", roman: "vāṅku" },
      { en: "Sell", mr: "விற்", roman: "viṟu" },
      { en: "Give", mr: "கொடு", roman: "koṭu" },
      { en: "Take", mr: "எடு", roman: "eṭu" }
    ]
  },
  emergency: {
    name: "Emergency",
    words: [
      { en: "Help", mr: "உதவி", roman: "utavi" },
      { en: "Police", mr: "காவலர்", roman: "kāvalar" },
      { en: "Doctor", mr: "மருத்துவர்", roman: "maruttuvar" },
      { en: "Hospital", mr: "மருத்துவமனை", roman: "maruttuvamaṉai" },
      { en: "Pain", mr: "வலி", roman: "vali" },
      { en: "Medicine", mr: "மருந்து", roman: "maruntu" }
    ]
  },
  numbers: {
    name: "Numbers",
    words: [
      { en: "One", mr: "ஒன்று", roman: "oṉṟu" },
      { en: "Two", mr: "இரண்டு", roman: "iraṇṭu" },
      { en: "Three", mr: "மூன்று", roman: "mūṉṟu" },
      { en: "Four", mr: "நான்கு", roman: "nāṉku" },
      { en: "Five", mr: "ஐந்து", roman: "aintu" },
      { en: "Six", mr: "ஆறு", roman: "āṟu" },
      { en: "Seven", mr: "ஏழு", roman: "ēḻu" },
      { en: "Eight", mr: "எட்டு", roman: "eṭṭu" },
      { en: "Nine", mr: "ஒன்பது", roman: "oṉpatu" },
      { en: "Ten", mr: "பத்து", roman: "pattu" }
    ]
  },
  reading: {
    name: "Reading & Language",
    words: [
      { en: "Book", mr: "புத்தகம்", roman: "puttakam" },
      { en: "Word", mr: "சொல்", roman: "col" },
      { en: "Language", mr: "மொழி", roman: "moḻi" },
      { en: "Tamil", mr: "தமிழ்", roman: "tamiḻ" },
      { en: "English", mr: "ஆங்கிலம்", roman: "āṅkilam" },
      { en: "To read", mr: "படி", roman: "paṭi" },
      { en: "To speak", mr: "பேசு", roman: "pēcu" },
      { en: "To understand", mr: "புரி", roman: "puri" }
    ]
  },
  writing: {
    name: "Writing & Script",
    words: [
      { en: "To write", mr: "எழுது", roman: "eḻutu" },
      { en: "Letter", mr: "கடிதம்", roman: "kaṭitam" },
      { en: "Pen", mr: "பேனா", roman: "pēṉā" },
      { en: "Paper", mr: "காகிதம்", roman: "kākitam" }
    ]
  },
  animals: {
    name: "Animals & Nature",
    words: [
      { en: "Dog", mr: "நாய்", roman: "nāy" },
      { en: "Cat", mr: "பூனை", roman: "pūṉai" },
      { en: "Cow", mr: "பசு", roman: "pacu" },
      { en: "Bird", mr: "பறவை", roman: "paṟavai" },
      { en: "Fish", mr: "மீன்", roman: "mīṉ" },
      { en: "Elephant", mr: "யானை", roman: "yāṉai" },
      { en: "Tree", mr: "மரம்", roman: "maram" },
      { en: "Flower", mr: "மலர்", roman: "malar" }
    ]
  },
  dailyLife: {
    name: "Daily Life",
    words: [
      { en: "House", mr: "வீடு", roman: "vīṭu" },
      { en: "Day", mr: "நாள்", roman: "nāḷ" },
      { en: "Work", mr: "வேலை", roman: "vēlai" },
      { en: "Time", mr: "நேரம்", roman: "nēram" },
      { en: "Today", mr: "இன்று", roman: "iṉṟu" },
      { en: "Tomorrow", mr: "நாளை", roman: "nāḷai" },
      { en: "Yesterday", mr: "நேற்று", roman: "nēṟṟu" },
      { en: "Now", mr: "இப்போது", roman: "ippōtu" }
    ]
  },
  environment: {
    name: "Environment & Weather",
    words: [
      { en: "Sun", mr: "சூரியன்", roman: "cūriyaṉ" },
      { en: "Rain", mr: "மழை", roman: "maḻai" },
      { en: "Hot", mr: "சூடு", roman: "cūṭu" },
      { en: "Cold", mr: "குளிர்", roman: "kuḷir" },
      { en: "Sky", mr: "வானம்", roman: "vāṉam" }
    ]
  },
  health: {
    name: "Health & Body",
    words: [
      { en: "Head", mr: "தலை", roman: "talai" },
      { en: "Eye", mr: "கண்", roman: "kaṇ" },
      { en: "Hand", mr: "கை", roman: "kai" },
      { en: "Foot", mr: "கால்", roman: "kāl" },
      { en: "Body", mr: "உடல்", roman: "uṭal" },
      { en: "Fever", mr: "காய்ச்சல்", roman: "kāyccal" },
      { en: "Headache", mr: "தலைவலி", roman: "talaivali" }
    ]
  },
  schoolWork: {
    name: "School & Work",
    words: [
      { en: "Teacher", mr: "ஆசிரியர்", roman: "āciriyar" },
      { en: "Student", mr: "மாணவர்", roman: "māṇavar" },
      { en: "Office", mr: "அலுவலகம்", roman: "aluvalakam" },
      { en: "Job", mr: "வேலை", roman: "vēlai" }
    ]
  },
  socialInteractions: {
    name: "Social & People",
    words: [
      { en: "Person", mr: "நபர்", roman: "napar" },
      { en: "People", mr: "மக்கள்", roman: "makkaḷ" },
      { en: "Friend", mr: "நண்பர்", roman: "naṇpar" },
      { en: "Family", mr: "குடும்பம்", roman: "kuṭumpam" },
      { en: "Father", mr: "அப்பா", roman: "appā" },
      { en: "Mother", mr: "அம்மா", roman: "ammā" },
      { en: "Brother", mr: "அண்ணா / தம்பி", roman: "aṇṇā / tampi" },
      { en: "Sister", mr: "அக்கா / தங்கை", roman: "akkā / taṅkai" }
    ]
  },
  time: {
    name: "Time & Dates",
    words: [
      { en: "Morning", mr: "காலை", roman: "kālai" },
      { en: "Evening", mr: "மாலை", roman: "mālai" },
      { en: "Night", mr: "இரவு", roman: "iravu" },
      { en: "Week", mr: "வாரம்", roman: "vāram" },
      { en: "Month", mr: "மாதம்", roman: "mātam" },
      { en: "Year", mr: "வருடம்", roman: "varuṭam" }
    ]
  },
  tourism: {
    name: "Travel & Tourism",
    words: [
      { en: "Temple", mr: "கோயில்", roman: "kōyil" },
      { en: "Hotel", mr: "ஹோட்டல்", roman: "hōṭṭal" },
      { en: "Ticket", mr: "டிக்கெட்", roman: "ṭikkeṭ" }
    ]
  },
  transportation: {
    name: "Transportation",
    words: [
      { en: "Bus", mr: "பஸ்", roman: "pas" },
      { en: "Train", mr: "ரயில்", roman: "rayil" },
      { en: "Car", mr: "கார்", roman: "kār" },
      { en: "Auto", mr: "ஆட்டோ", roman: "āṭṭō" },
      { en: "Road", mr: "சாலை", roman: "cālai" },
      { en: "Station", mr: "நிலையம்", roman: "nilaiyam" }
    ]
  }
};
