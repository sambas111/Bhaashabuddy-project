// Odia phrases & dictionary – for Phrases and Words sections (separate from Lessons)
// Max 30 phrases/words per set. Use "Topic Set 1", "Topic Set 2", etc. when adding more.
const ODIA_PHRASES = {
  greetings_1: {
    name: "Greetings Set 1",
    color: "#2B6CB0",
    icon: "👋",
    phrases: [
      { en: "Hello", mr: "ନମସ୍କାର", roman: "Namaskāra", hint: "" },
      { en: "Good morning", mr: "ସୁପ୍ରଭାତ", roman: "Suprabhāta", hint: "" },
      { en: "Good afternoon", mr: "ଶୁଭ ଅପରାହ୍ନ", roman: "Shubha aparāhna", hint: "" },
      { en: "Good evening", mr: "ଶୁଭ ସନ୍ଧ୍ୟା", roman: "Shubha sandhyā", hint: "" },
      { en: "Good night", mr: "ଶୁଭ ରାତ୍ରି", roman: "Shubha rātri", hint: "" },
      { en: "Welcome", mr: "ସ୍ୱାଗତମ୍", roman: "Svāgatam", hint: "" },
      { en: "How are you?", mr: "ଆପଣ କେମିତି ଅଛନ୍ତି?", roman: "Āpaṇa kemiti achanti?", hint: "" },
      { en: "I am fine", mr: "ମୁଁ ଭଲ ଅଛି", roman: "Mun bhala achhi", hint: "" },
      { en: "What is your name?", mr: "ଆପଣଙ୍କ ନାମ କ'ଣ?", roman: "Āpaṇanka nāma kaṇa?", hint: "" },
      { en: "My name is...", mr: "ମୋ ନାମ ... ", roman: "Mo nāma ...", hint: "" },
      { en: "Nice to meet you", mr: "ଆପଣଙ୍କୁ ଭେଟି ଖୁସି ଲାଗିଲା", roman: "Āpaṇanku bheṭi khusi lāgilā", hint: "" },
      { en: "Thank you", mr: "ଧନ୍ୟବାଦ", roman: "Dhanyabāda", hint: "" },
      { en: "Please", mr: "ଦୟାକରି", roman: "Dayākari", hint: "" },
      { en: "Sorry", mr: "କ୍ଷମା କରନ୍ତୁ", roman: "Kshamā karantu", hint: "" },
      { en: "Goodbye", mr: "ବିଦାୟ", roman: "Bidāya", hint: "" },
      { en: "See you again", mr: "ପୁଣି ଭେଟ ହେବ", roman: "Puṇi bheṭa heba", hint: "" },
      { en: "Take care", mr: "ଯତ୍ନ ନିଅନ୍ତୁ", roman: "Yatna niantu", hint: "" },
      { en: "I love you", mr: "ମୁଁ ତୁମକୁ ଭଲ ପାଏ", roman: "Mun tumaku bhala pāe", hint: "" }
    ]
  },
  travel_1: {
    name: "Travel Set 1",
    color: "#38A169",
    icon: "🚌",
    phrases: [
      { en: "Where is the station?", mr: "ଷ୍ଟେସନ କେଉଁଠି?", roman: "Sṭesana keunṭhi?", hint: "" },
      { en: "Take me to the station", mr: "ମୋତେ ଷ୍ଟେସନ ନେଇ ଯାଅ", roman: "Mote sṭesana nei yāa", hint: "" },
      { en: "How far is it?", mr: "ଏହା କେତେ ଦୂର?", roman: "Ehā kete dūra?", hint: "" },
      { en: "I want to go to...", mr: "ମୁଁ ... କୁ ଯିବାକୁ ଚାହେଁ", roman: "Mun ... ku yibāku chāhen", hint: "" },
      { en: "Where is the bus stop?", mr: "ବସ୍ ଷ୍ଟପ୍ କେଉଁଠି?", roman: "Bas sṭap keunṭhi?", hint: "" },
      { en: "How much is the ticket?", mr: "ଟିକେଟ୍ କେତେ?", roman: "Ṭikeṭ kete?", hint: "" },
      { en: "When does the train leave?", mr: "ଟ୍ରେନ୍ କେବେ ଛାଡ଼ିବ?", roman: "Ṭren kebe chhāḍiba?", hint: "" },
      { en: "Is this the right way?", mr: "ଏହା ଠିକ୍ ରାସ୍ତା ନା?", roman: "Ehā ṭhik rāstā nā?", hint: "" },
      { en: "Please stop here", mr: "ଦୟାକରି ଏଠି ରଖନ୍ତୁ", roman: "Dayākari eṭhi rakhantu", hint: "" },
      { en: "Turn left", mr: "ବାମ ପଟକୁ ଯାଅ", roman: "Bāma paṭaku yāa", hint: "" },
      { en: "Turn right", mr: "ଡାହାଣ ପଟକୁ ଯାଅ", roman: "Ḍāhāṇa paṭaku yāa", hint: "" },
      { en: "Go straight", mr: "ସିଧା ଯାଅ", roman: "Sidhā yāa", hint: "" },
      { en: "I am lost", mr: "ମୁଁ ହଜିଯାଇଛି", roman: "Mun hajiyāichhi", hint: "" },
      { en: "Where is the hotel?", mr: "ହୋଟେଲ କେଉଁଠି?", roman: "Hoṭela keunṭhi?", hint: "" },
      { en: "I need a room", mr: "ମୋତେ ଗୋଟିଏ ଘର ଦରକାର", roman: "Mote goṭie ghara darakāra", hint: "" },
      { en: "Where is the airport?", mr: "ବିମାନ ବନ୍ଦର କେଉଁଠି?", roman: "Bimāna bandara keunṭhi?", hint: "" },
      { en: "Call a taxi", mr: "ଗୋଟିଏ ଟ୍ୟାକ୍ସି ଡାକ", roman: "Goṭie ṭyāksi ḍāka", hint: "" },
      { en: "I want to book a ticket", mr: "ମୁଁ ଟିକେଟ୍ ବୁକ୍ କରିବାକୁ ଚାହେଁ", roman: "Mun ṭikeṭ buk karibāku chāhen", hint: "" }
    ]
  },
  food_1: {
    name: "Food & Dining Set 1",
    color: "#DD6B20",
    icon: "🍛",
    phrases: [
      { en: "I am hungry", mr: "ମୋର ଭୋକ ଲାଗିଛି", roman: "Mora bhoka lāgichhi", hint: "" },
      { en: "I am thirsty", mr: "ମୋର ତୃଷା ଲାଗିଛି", roman: "Mora trushā lāgichhi", hint: "" },
      { en: "Give me water", mr: "ମୋତେ ପାଣି ଦିଅ", roman: "Mote pāṇi dia", hint: "" },
      { en: "What is this dish?", mr: "ଏହା କେଉଁ ଖାଦ୍ୟ?", roman: "Ehā keun khādya?", hint: "" },
      { en: "I want rice", mr: "ମୁଁ ଭାତ ଚାହେଁ", roman: "Mun bhāta chāhen", hint: "" },
      { en: "Give me dal", mr: "ମୋତେ ଡାଲି ଦିଅ", roman: "Mote ḍāli dia", hint: "" },
      { en: "The food is delicious", mr: "ଖାଦ୍ୟ ବହୁତ ସ୍ୱାଦିଷ୍ଟ", roman: "Khādya bahuta svādiṣṭa", hint: "" },
      { en: "I want tea", mr: "ମୁଁ ଚା' ଚାହେଁ", roman: "Mun chā chāhen", hint: "" },
      { en: "Bring the bill", mr: "ବିଲ୍ ଆଣନ୍ତୁ", roman: "Bil āṇantu", hint: "" },
      { en: "I am vegetarian", mr: "ମୁଁ ନିରାମିଷ ଖାଏ", roman: "Mun nirāmiṣa khāe", hint: "" },
      { en: "No spicy food", mr: "ଝାଳ ଖାଦ୍ୟ ନୁହେଁ", roman: "Jhāḷa khādya nuhen", hint: "" },
      { en: "Give me more", mr: "ଆଉ ଟିକେ ଦିଅ", roman: "Āu ṭike dia", hint: "" },
      { en: "It is very tasty", mr: "ଏହା ବହୁତ ସୁସ୍ୱାଦୁ", roman: "Ehā bahuta susvādu", hint: "" },
      { en: "I want sweets", mr: "ମୁଁ ମିଠା ଚାହେଁ", roman: "Mun miṭhā chāhen", hint: "" },
      { en: "Where is a restaurant?", mr: "ଖାଦ୍ୟ ଦୋକାନ କେଉଁଠି?", roman: "Khādya dokāna keunṭhi?", hint: "" },
      { en: "One plate please", mr: "ଗୋଟିଏ ପ୍ଲେଟ୍ ଦିଅ", roman: "Goṭie pleṭ dia", hint: "" },
      { en: "I do not eat fish", mr: "ମୁଁ ମାଛ ଖାଏ ନାହିଁ", roman: "Mun māchha khāe nāhin", hint: "" },
      { en: "Give me a glass of milk", mr: "ମୋତେ ଏକ ଗ୍ଲାସ୍ କ୍ଷୀର ଦିଅ", roman: "Mote eka glās kshīra dia", hint: "" }
    ]
  },
  daily_1: {
    name: "Daily Life Set 1",
    color: "#805AD5",
    icon: "🏠",
    phrases: [
      { en: "What time is it?", mr: "ବେଳ କେତେ ହେଲା?", roman: "Beḷa kete helā?", hint: "" },
      { en: "I have to go to work", mr: "ମୋତେ କାମକୁ ଯିବାକୁ ହେବ", roman: "Mote kāmaku yibāku heba", hint: "" },
      { en: "Where is the market?", mr: "ବଜାର କେଉଁଠି?", roman: "Bajāra keunṭhi?", hint: "" },
      { en: "I need to wash clothes", mr: "ମୋତେ ଲୁଗା ଧୋଇବାକୁ ହେବ", roman: "Mote lugā dhoibāku heba", hint: "" },
      { en: "Switch on the light", mr: "ଲାଇଟ୍ ଜଳାଅ", roman: "Lāiṭ jalāa", hint: "" },
      { en: "Switch off the fan", mr: "ପଙ୍ଖା ବନ୍ଦ କର", roman: "Pankhā banda kara", hint: "" },
      { en: "Close the door", mr: "କବାଟ ବନ୍ଦ କର", roman: "Kabāṭa banda kara", hint: "" },
      { en: "Open the window", mr: "ଝରକା ଖୋଲ", roman: "Jharakā khola", hint: "" },
      { en: "I am going to school", mr: "ମୁଁ ସ୍କୁଲ ଯାଉଛି", roman: "Mun skul yāuchhi", hint: "" },
      { en: "It is raining", mr: "ବର୍ଷା ହେଉଛି", roman: "Barshā heuchhi", hint: "" },
      { en: "It is very hot", mr: "ବହୁତ ଗରମ ଲାଗୁଛି", roman: "Bahuta garama lāguchhi", hint: "" },
      { en: "It is very cold", mr: "ବହୁତ ଥଣ୍ଡା ଲାଗୁଛି", roman: "Bahuta thaṇḍā lāguchhi", hint: "" },
      { en: "I am tired", mr: "ମୁଁ ଥକି ଗଲି", roman: "Mun thaki gali", hint: "" },
      { en: "I am sleepy", mr: "ମୋର ନିଦ ଲାଗୁଛି", roman: "Mora nida lāguchhi", hint: "" },
      { en: "Wake up early", mr: "ଲୋ ସକାଳୁ ଉଠ", roman: "Lo sakāḷu uṭha", hint: "" },
      { en: "Let us go for a walk", mr: "ଚାଲ ବୁଲିବାକୁ ଯିବା", roman: "Chāla bulibāku yibā", hint: "" },
      { en: "Today is Sunday", mr: "ଆଜି ରବିବାର", roman: "Āji rabibāra", hint: "" },
      { en: "I will come tomorrow", mr: "ମୁଁ କାଲି ଆସିବି", roman: "Mun kāli āsibi", hint: "" }
    ]
  },
  shopping_1: {
    name: "Shopping Set 1",
    color: "#D69E2E",
    icon: "🛒",
    phrases: [
      { en: "How much does this cost?", mr: "ଏହାର ଦାମ କେତେ?", roman: "Ehāra dāma kete?", hint: "" },
      { en: "It is too expensive", mr: "ଏହା ବହୁତ ଦାମୀ", roman: "Ehā bahuta dāmī", hint: "" },
      { en: "Give me a discount", mr: "ଟିକେ କମ୍ କରନ୍ତୁ", roman: "Ṭike kam karantu", hint: "" },
      { en: "I want to buy this", mr: "ମୁଁ ଏହା କିଣିବାକୁ ଚାହେଁ", roman: "Mun ehā kiṇibāku chāhen", hint: "" },
      { en: "Show me another one", mr: "ଆଉ ଗୋଟିଏ ଦେଖାନ୍ତୁ", roman: "Āu goṭie dekhāntu", hint: "" },
      { en: "Do you have a bigger size?", mr: "ଆଉ ବଡ଼ ସାଇଜ୍ ଅଛି କି?", roman: "Āu baḍa sāij achhi ki?", hint: "" },
      { en: "I will pay in cash", mr: "ମୁଁ ନଗଦ ଦେବି", roman: "Mun nagada debi", hint: "" },
      { en: "Do you accept UPI?", mr: "ଆପଣ UPI ନିଅନ୍ତି କି?", roman: "Āpaṇa UPI nianti ki?", hint: "" },
      { en: "Give me a bag", mr: "ମୋତେ ଗୋଟିଏ ବ୍ୟାଗ୍ ଦିଅ", roman: "Mote goṭie byāg dia", hint: "" },
      { en: "Where is the billing counter?", mr: "ବିଲ୍ କାଉଣ୍ଟର କେଉଁଠି?", roman: "Bil kāuṇṭara keunṭhi?", hint: "" },
      { en: "I do not need this", mr: "ମୋତେ ଏହା ଦରକାର ନାହିଁ", roman: "Mote ehā darakāra nāhin", hint: "" },
      { en: "Can I try this on?", mr: "ମୁଁ ଏହା ପିନ୍ଧି ଦେଖିପାରିବି କି?", roman: "Mun ehā pindhi dekhipāribi ki?", hint: "" },
      { en: "What is the final price?", mr: "ଶେଷ ଦାମ କେତେ?", roman: "Shesha dāma kete?", hint: "" },
      { en: "Pack this properly", mr: "ଏହା ଭଲ ଭାବରେ ପ୍ୟାକ୍ କରନ୍ତୁ", roman: "Ehā bhala bhābare pyāk karantu", hint: "" },
      { en: "Where is the vegetable shop?", mr: "ପରିବା ଦୋକାନ କେଉଁଠି?", roman: "Paribā dokāna keunṭhi?", hint: "" },
      { en: "Give me one kilo of potatoes", mr: "ମୋତେ ଏକ କେଜି ଆଳୁ ଦିଅ", roman: "Mote eka keji āḷu dia", hint: "" },
      { en: "Is this fresh?", mr: "ଏହା ତାଜା ନା?", roman: "Ehā tājā nā?", hint: "" },
      { en: "I will come back later", mr: "ମୁଁ ପରେ ଆସିବି", roman: "Mun pare āsibi", hint: "" }
    ]
  },
  emergency_1: {
    name: "Emergency Set 1",
    color: "#E53E3E",
    icon: "🚨",
    phrases: [
      { en: "Help!", mr: "ସାହାଯ୍ୟ କରନ୍ତୁ!", roman: "Sāhāyya karantu!", hint: "" },
      { en: "Call the police", mr: "ପୋଲିସ୍ ଡାକନ୍ତୁ", roman: "Polis ḍākantu", hint: "" },
      { en: "Call an ambulance", mr: "ଆମ୍ବୁଲାନ୍ସ ଡାକନ୍ତୁ", roman: "Āmbulāns ḍākantu", hint: "" },
      { en: "I need a doctor", mr: "ମୋତେ ଡାକ୍ତର ଦରକାର", roman: "Mote ḍāktara darakāra", hint: "" },
      { en: "I am hurt", mr: "ମୋର ଆଘାତ ଲାଗିଛି", roman: "Mora āghāta lāgichhi", hint: "" },
      { en: "There is a fire", mr: "ନିଆଁ ଲାଗିଛି", roman: "Niān lāgichhi", hint: "" },
      { en: "I lost my wallet", mr: "ମୋ ପର୍ସ ହଜିଯାଇଛି", roman: "Mo parsa hajiyāichhi", hint: "" },
      { en: "Someone stole my bag", mr: "କେହି ମୋ ବ୍ୟାଗ୍ ଚୋରି କରିଛି", roman: "Kehi mo byāg chori karichhi", hint: "" },
      { en: "Where is the hospital?", mr: "ଡାକ୍ତରଖାନା କେଉଁଠି?", roman: "Ḍāktarakhānā keunṭhi?", hint: "" },
      { en: "I have a fever", mr: "ମୋର ଜ୍ୱର ହୋଇଛି", roman: "Mora jvara hoichhi", hint: "" },
      { en: "My head hurts", mr: "ମୋ ମୁଣ୍ଡ ବିନ୍ଧୁଛି", roman: "Mo muṇḍa bindhuchhi", hint: "" },
      { en: "I have stomach pain", mr: "ମୋ ପେଟ ବିନ୍ଧୁଛି", roman: "Mo peṭa bindhuchhi", hint: "" },
      { en: "I am allergic to...", mr: "ମୋର ... ରେ ଆଲର୍ଜି ଅଛି", roman: "Mora ... re ālarji achhi", hint: "" },
      { en: "Where is the pharmacy?", mr: "ଔଷଧ ଦୋକାନ କେଉଁଠି?", roman: "Aushadha dokāna keunṭhi?", hint: "" },
      { en: "I need medicine", mr: "ମୋତେ ଔଷଧ ଦରକାର", roman: "Mote aushadha darakāra", hint: "" },
      { en: "Please help me", mr: "ଦୟାକରି ମୋତେ ସାହାଯ୍ୟ କରନ୍ତୁ", roman: "Dayākari mote sāhāyya karantu", hint: "" },
      { en: "It is an emergency", mr: "ଏହା ଜରୁରୀ ଅବସ୍ଥା", roman: "Ehā jarurī abasthā", hint: "" },
      { en: "Take me to the hospital", mr: "ମୋତେ ଡାକ୍ତରଖାନା ନେଇ ଯାଅ", roman: "Mote ḍāktarakhānā nei yāa", hint: "" }
    ]
  }
};

const ODIA_DICTIONARY = {
  basics_1: {
    name: "Basic Words Set 1",
    words: [
      { en: "I", mr: "ମୁଁ", roman: "Mun" },
      { en: "You (formal)", mr: "ଆପଣ", roman: "Āpaṇa" },
      { en: "You (informal)", mr: "ତୁମେ", roman: "Tume" },
      { en: "He", mr: "ସେ", roman: "Se" },
      { en: "She", mr: "ସେ", roman: "Se" },
      { en: "We", mr: "ଆମେ", roman: "Āme" },
      { en: "They", mr: "ସେମାନେ", roman: "Semāne" },
      { en: "House", mr: "ଘର", roman: "Ghara" },
      { en: "Water", mr: "ପାଣି", roman: "Pāṇi" },
      { en: "Food", mr: "ଖାଦ୍ୟ", roman: "Khādya" },
      { en: "Village", mr: "ଗାଁ", roman: "Gān" },
      { en: "Morning", mr: "ସକାଳ", roman: "Sakāḷa" },
      { en: "Today", mr: "ଆଜି", roman: "Āji" },
      { en: "Tomorrow", mr: "କାଲି", roman: "Kāli" },
      { en: "Yesterday", mr: "ଗତକାଲି", roman: "Gatakāli" },
      { en: "Night", mr: "ରାତି", roman: "Rāti" },
      { en: "Day", mr: "ଦିନ", roman: "Dina" },
      { en: "Person", mr: "ବ୍ୟକ୍ତି", roman: "Byakti" },
      { en: "Child", mr: "ପିଲା", roman: "Pilā" },
      { en: "Road", mr: "ରାସ୍ତା", roman: "Rāstā" }
    ]
  },
  family_1: {
    name: "Family & People Set 1",
    words: [
      { en: "Mother", mr: "ମା", roman: "Mā" },
      { en: "Father", mr: "ବାପା", roman: "Bāpā" },
      { en: "Brother", mr: "ଭାଇ", roman: "Bhāi" },
      { en: "Sister", mr: "ଭଉଣୀ", roman: "Bhauṇī" },
      { en: "Son", mr: "ପୁଅ", roman: "Pua" },
      { en: "Daughter", mr: "ଝିଅ", roman: "Jhia" },
      { en: "Grandfather", mr: "ବାପା ବାପା", roman: "Bāpā bāpā" },
      { en: "Grandmother", mr: "ବଡ଼ ମା", roman: "Baḍa mā" },
      { en: "Husband", mr: "ସ୍ୱାମୀ", roman: "Svāmī" },
      { en: "Wife", mr: "ସ୍ତ୍ରୀ", roman: "Strī" },
      { en: "Friend", mr: "ବନ୍ଧୁ", roman: "Bandhu" }
    ]
  },
  verbs_1: {
    name: "Common Verbs Set 1",
    words: [
      { en: "To go", mr: "ଯିବା", roman: "Yibā" },
      { en: "To come", mr: "ଆସିବା", roman: "Āsibā" },
      { en: "To eat", mr: "ଖାଇବା", roman: "Khāibā" },
      { en: "To drink", mr: "ପିଇବା", roman: "Piibā" },
      { en: "To speak", mr: "କହିବା", roman: "Kahibā" },
      { en: "To listen", mr: "ଶୁଣିବା", roman: "Shuṇibā" },
      { en: "To see", mr: "ଦେଖିବା", roman: "Dekhibā" },
      { en: "To do", mr: "କରିବା", roman: "Karibā" },
      { en: "To give", mr: "ଦେବା", roman: "Debā" },
      { en: "To take", mr: "ନେବା", roman: "Nebā" },
      { en: "To read", mr: "ପଢ଼ିବା", roman: "Paḍhibā" },
      { en: "To write", mr: "ଲେଖିବା", roman: "Lekhibā" },
      { en: "To sleep", mr: "ଶୋଇବା", roman: "Shoibā" },
      { en: "To sit", mr: "ବସିବା", roman: "Basibā" },
      { en: "To stand", mr: "ଠିଆ ହେବା", roman: "Ṭhiā hebā" },
      { en: "To run", mr: "ଦୌଡ଼ିବା", roman: "Dauḍibā" }
    ]
  },
  common_1: {
    name: "Common Words Set 1",
    words: [
      { en: "Yes", mr: "ହଁ", roman: "Han" },
      { en: "No", mr: "ନା", roman: "Nā" },
      { en: "Good", mr: "ଭଲ", roman: "Bhala" },
      { en: "Bad", mr: "ଖରାପ", roman: "Kharāpa" },
      { en: "Big", mr: "ବଡ଼", roman: "Baḍa" },
      { en: "Small", mr: "ଛୋଟ", roman: "Chhoṭa" },
      { en: "New", mr: "ନୂଆ", roman: "Nūā" },
      { en: "Old", mr: "ପୁରୁଣା", roman: "Puruṇā" },
      { en: "Hot", mr: "ଗରମ", roman: "Garama" },
      { en: "Cold", mr: "ଥଣ୍ଡା", roman: "Thaṇḍā" },
      { en: "Beautiful", mr: "ସୁନ୍ଦର", roman: "Sundara" },
      { en: "Fast", mr: "ଶୀଘ୍ର", roman: "Shīghra" },
      { en: "Slow", mr: "ଧୀରେ", roman: "Dhīre" },
      { en: "Near", mr: "ନିକଟ", roman: "Nikaṭa" },
      { en: "Far", mr: "ଦୂର", roman: "Dūra" },
      { en: "Here", mr: "ଏଠି", roman: "Eṭhi" },
      { en: "There", mr: "ସେଠି", roman: "Seṭhi" },
      { en: "Now", mr: "ଏବେ", roman: "Ebe" },
      { en: "Much / Many", mr: "ବହୁତ", roman: "Bahuta" }
    ]
  },
  nature_1: {
    name: "Nature & Food Set 1",
    words: [
      { en: "Sun", mr: "ସୂର୍ଯ୍ୟ", roman: "Sūryya" },
      { en: "Moon", mr: "ଚନ୍ଦ୍ର", roman: "Chandra" },
      { en: "Star", mr: "ତାରା", roman: "Tārā" },
      { en: "Sky", mr: "ଆକାଶ", roman: "Ākāsha" },
      { en: "Rain", mr: "ବର୍ଷା", roman: "Barshā" },
      { en: "Wind", mr: "ପବନ", roman: "Pabana" },
      { en: "River", mr: "ନଦୀ", roman: "Nadī" },
      { en: "Mountain", mr: "ପର୍ବତ", roman: "Parbata" },
      { en: "Tree", mr: "ଗଛ", roman: "Gachha" },
      { en: "Flower", mr: "ଫୁଲ", roman: "Phula" },
      { en: "Earth", mr: "ପୃଥିବୀ", roman: "Prithībī" },
      { en: "Rice", mr: "ଭାତ", roman: "Bhāta" },
      { en: "Dal", mr: "ଡାଲି", roman: "Ḍāli" },
      { en: "Vegetable", mr: "ପରିବା", roman: "Paribā" },
      { en: "Fish", mr: "ମାଛ", roman: "Māchha" },
      { en: "Milk", mr: "କ୍ଷୀର", roman: "Kshīra" },
      { en: "Salt", mr: "ଲୁଣ", roman: "Luṇa" },
      { en: "Sugar", mr: "ଚିନି", roman: "Chini" },
      { en: "Fruit", mr: "ଫଳ", roman: "Phaḷa" },
      { en: "Mango", mr: "ଆମ୍ବ", roman: "Āmba" }
    ]
  },
  everyday_1: {
    name: "Everyday Items Set 1",
    words: [
      { en: "Book", mr: "ବହି", roman: "Bahi" },
      { en: "Pen", mr: "କଲମ", roman: "Kalama" },
      { en: "Phone", mr: "ଫୋନ୍", roman: "Phon" },
      { en: "Clothes", mr: "ଲୁଗା", roman: "Lugā" },
      { en: "Shoes", mr: "ଜୋତା", roman: "Jotā" },
      { en: "Money", mr: "ଟଙ୍କା", roman: "Ṭankā" },
      { en: "Chair", mr: "ଚୌକି", roman: "Chauki" },
      { en: "Table", mr: "ଟେବୁଲ", roman: "Ṭebula" },
      { en: "Plate", mr: "ଥାଳି", roman: "Thāḷi" },
      { en: "Glass", mr: "ଗ୍ଲାସ୍", roman: "Glās" },
      { en: "Bed", mr: "ବିଛଣା", roman: "Bichhṇā" },
      { en: "Key", mr: "ଚାବି", roman: "Chābi" }
    ]
  }
};
