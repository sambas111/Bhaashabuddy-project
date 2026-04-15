import json

d = json.load(open('data_odia.json', 'r', encoding='utf-8'))

LESSONS = {}

# 501 - Odia Alphabets – Odia Script (vowels and consonants grid)
LESSONS[501] = {
    "blocks": [
        {
            "type": "grid",
            "columns": ["Letter", "Transliteration"],
            "rows": [
                ["ଅ", "a"],
                ["ଆ", "aa"],
                ["ଇ", "i"],
                ["ଈ", "ee"],
                ["ଉ", "u"],
                ["ଊ", "oo"],
                ["ଋ", "ru"],
                ["ଏ", "e"],
                ["ଐ", "ai"],
                ["ଓ", "o"],
                ["ଔ", "au"],
                ["କ", "ka"],
                ["ଖ", "kha"],
                ["ଗ", "ga"],
                ["ଘ", "gha"],
                ["ଙ", "nga"],
                ["ଚ", "cha"],
                ["ଛ", "chha"],
                ["ଜ", "ja"],
                ["ଝ", "jha"],
                ["ଞ", "nya"],
                ["ଟ", "ta (retroflex)"],
                ["ଠ", "tha (retroflex)"],
                ["ଡ", "da (retroflex)"],
                ["ଢ", "dha (retroflex)"],
                ["ଣ", "na (retroflex)"],
                ["ତ", "ta (dental)"],
                ["ଥ", "tha (dental)"],
                ["ଦ", "da (dental)"],
                ["ଧ", "dha (dental)"],
                ["ନ", "na (dental)"],
                ["ପ", "pa"],
                ["ଫ", "pha"],
                ["ବ", "ba"],
                ["ଭ", "bha"],
                ["ମ", "ma"],
                ["ଯ", "ya"],
                ["ର", "ra"],
                ["ଲ", "la"],
                ["ଶ", "sha (palatal)"],
                ["ଷ", "sha (retroflex)"],
                ["ସ", "sa (dental)"],
                ["ହ", "ha"],
                ["ଳ", "la (retroflex)"],
                ["କ୍ଷ", "ksha"],
                ["ଜ୍ଞ", "gnya"]
            ]
        },
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Mother", "ମା", "maa"],
                ["Father", "ବାପା", "baapaa"],
                ["Water", "ପାଣି", "paani"],
                ["Rice", "ଭାତ", "bhaata"],
                ["House", "ଘର", "ghara"],
                ["Tree", "ଗଛ", "gachha"],
                ["Flower", "ଫୁଲ", "phula"],
                ["Sun", "ସୂର୍ଯ୍ୟ", "suuryya"],
                ["Moon", "ଚନ୍ଦ୍ର", "chandra"],
                ["Eye", "ଆଖି", "aakhi"],
                ["Hand", "ହାତ", "haata"],
                ["Leg", "ଗୋଡ", "goda"],
                ["Fish", "ମାଛ", "maachha"],
                ["Bird", "ଚିଡ଼ିଆ", "chidiaa"],
                ["Book", "ବହି", "bahi"],
                ["Earth", "ପୃଥିବୀ", "pruthibee"],
                ["Sky", "ଆକାଶ", "aakaasha"],
                ["Name", "ନାମ", "naama"]
            ]
        }
    ]
}

# 502 - Vowels, Consonants in Odia and their pronunciation
LESSONS[502] = {
    "blocks": [
        {
            "type": "grid",
            "columns": ["Letter", "Transliteration"],
            "rows": [
                ["ଅ", "a as in 'about'"],
                ["ଆ", "aa as in 'father'"],
                ["ଇ", "i as in 'sit'"],
                ["ଈ", "ee as in 'feet'"],
                ["ଉ", "u as in 'put'"],
                ["ଊ", "oo as in 'boot'"],
                ["ଋ", "ru as in 'rude' (short)"],
                ["ଏ", "e as in 'bed'"],
                ["ଐ", "ai as in 'aisle'"],
                ["ଓ", "o as in 'go'"],
                ["ଔ", "au as in 'cow'"]
            ]
        },
        {
            "type": "grid",
            "columns": ["Letter", "Transliteration"],
            "rows": [
                ["କ ଖ ଗ ଘ ଙ", "ka-varga (velar group)"],
                ["ଚ ଛ ଜ ଝ ଞ", "cha-varga (palatal group)"],
                ["ଟ ଠ ଡ ଢ ଣ", "ta-varga (retroflex group)"],
                ["ତ ଥ ଦ ଧ ନ", "ta-varga (dental group)"],
                ["ପ ଫ ବ ଭ ମ", "pa-varga (labial group)"],
                ["ଯ ର ଲ ଶ ଷ ସ ହ ଳ", "antahstha & ushma (semi-vowels & sibilants)"]
            ]
        },
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Mango", "ଆମ୍ବ", "aamba"],
                ["Banana", "କଦଳୀ", "kadalee"],
                ["Cow", "ଗାଈ", "gaaee"],
                ["Dog", "କୁକୁର", "kukura"],
                ["Cat", "ବିଲେଇ", "bilei"],
                ["Elephant", "ହାତୀ", "haatee"],
                ["Tiger", "ବାଘ", "baagha"],
                ["River", "ନଦୀ", "nadee"],
                ["Mountain", "ପର୍ବତ", "parbata"],
                ["Rain", "ବର୍ଷା", "barshaa"],
                ["Wind", "ପବନ", "pabana"],
                ["Fire", "ନିଆଁ", "niaan"],
                ["Child", "ପିଲା", "pilaa"],
                ["Girl", "ଝିଅ", "jhia"],
                ["Boy", "ପୁଅ", "pua"],
                ["Friend", "ବନ୍ଧୁ", "bandhu"],
                ["Teacher", "ଶିକ୍ଷକ", "shikshaka"],
                ["School", "ବିଦ୍ୟାଳୟ", "bidyaalaya"]
            ]
        }
    ]
}

# 503 - Odia Barakhadi: Symbols for vowels with consonants
LESSONS[503] = {
    "blocks": [
        {
            "type": "grid",
            "columns": ["Letter", "Transliteration"],
            "rows": [
                ["କ", "ka"],
                ["କା", "kaa"],
                ["କି", "ki"],
                ["କୀ", "kee"],
                ["କୁ", "ku"],
                ["କୂ", "koo"],
                ["କୃ", "kru"],
                ["କେ", "ke"],
                ["କୈ", "kai"],
                ["କୋ", "ko"],
                ["କୌ", "kau"],
                ["ଗ", "ga"],
                ["ଗା", "gaa"],
                ["ଗି", "gi"],
                ["ଗୀ", "gee"],
                ["ଗୁ", "gu"],
                ["ଗୂ", "goo"],
                ["ଗେ", "ge"],
                ["ଗୋ", "go"],
                ["ପ", "pa"],
                ["ପା", "paa"],
                ["ପି", "pi"],
                ["ପୀ", "pee"],
                ["ପୁ", "pu"],
                ["ପୂ", "poo"],
                ["ପେ", "pe"],
                ["ପୋ", "po"],
                ["ତ", "ta"],
                ["ତା", "taa"],
                ["ତି", "ti"],
                ["ତୀ", "tee"],
                ["ତୁ", "tu"],
                ["ତୂ", "too"],
                ["ତେ", "te"],
                ["ତୋ", "to"]
            ]
        },
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Ear", "କାନ", "kaana"],
                ["Work", "କାମ", "kaama"],
                ["Paper", "କାଗଜ", "kaagaja"],
                ["Cloth", "କାପଡ଼", "kaapada"],
                ["Story", "ଗପ", "gapa"],
                ["Song", "ଗୀତ", "geeta"],
                ["Village", "ଗାଁ", "gaaan"],
                ["Foot", "ଗୋଡ", "goda"],
                ["Leaf", "ପତ୍ର", "patra"],
                ["Road", "ପଥ", "patha"],
                ["Fruit", "ଫଳ", "phala"],
                ["Star", "ତାରା", "taaraa"],
                ["Lock", "ତାଲା", "taalaa"],
                ["Oil", "ତେଲ", "tela"],
                ["Three", "ତିନି", "tini"],
                ["Below", "ତଳ", "tala"],
                ["Tooth", "ଦାନ୍ତ", "daanta"],
                ["Milk", "କ୍ଷୀର", "ksheera"]
            ]
        }
    ]
}

# 504 - Frequently faced pronunciation problems in Odia
LESSONS[504] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["ଣ vs ନ: Heat", "ଘରଣୀ (mistress of house)", "gharanee"],
                ["ଣ vs ନ: Nose", "ନାକ", "naaka"],
                ["ଷ vs ସ: Six", "ଷଡ଼", "shada"],
                ["ଷ vs ସ: Thread", "ସୂତା", "sootaa"],
                ["ଶ vs ସ: Sleep", "ଶୋଇବା", "shoibaa"],
                ["ଶ vs ସ: Gold", "ସୁନା", "sunaa"],
                ["ଡ vs ଦ: Call", "ଡାକିବା", "daakibaa"],
                ["ଡ vs ଦ: Give", "ଦେବା", "debaa"],
                ["Aspirated: ଖ (eat)", "ଖାଇବା", "khaaibaa"],
                ["Aspirated: ଘ (house)", "ଘର", "ghara"],
                ["Aspirated: ଛ (umbrella)", "ଛତା", "chhataa"],
                ["Aspirated: ଝ (storm)", "ଝଡ଼", "jhada"],
                ["Aspirated: ଠ (cold)", "ଥଣ୍ଡା", "thandaa"],
                ["Aspirated: ଧ (money)", "ଧନ", "dhana"],
                ["Aspirated: ଫ (fruit)", "ଫଳ", "phala"],
                ["Aspirated: ଭ (rice)", "ଭାତ", "bhaata"],
                ["ଳ (retroflex la): Time", "କାଳ", "kaala"],
                ["ଲ (dental la): Red", "ଲାଲ", "laala"]
            ]
        }
    ]
}

# 505 - Pronunciation of Anusvar in Odia
LESSONS[505] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Part / portion", "ଅଂଶ", "ansha"],
                ["Number", "ସଂଖ୍ୟା", "sankhyaa"],
                ["Music / song", "ସଂଗୀତ", "sangeeta"],
                ["World", "ସଂସାର", "sansaara"],
                ["Organization", "ସଂଗଠନ", "sangathana"],
                ["Doubt", "ସନ୍ଦେହ", "sandeha"],
                ["Message", "ସନ୍ଦେଶ", "sandesha"],
                ["Relation", "ସମ୍ବନ୍ଧ", "sambandha"],
                ["Complete", "ସମ୍ପୂର୍ଣ୍ଣ", "sampoorna"],
                ["Possible", "ସମ୍ଭବ", "sambhaba"],
                ["Collection", "ସଂଗ୍ରହ", "sangraha"],
                ["Sanskrit", "ସଂସ୍କୃତ", "sanskruta"],
                ["Contact", "ସଂଯୋଗ", "sanyoga"],
                ["Constitution", "ସଂବିଧାନ", "sambidhana"],
                ["Sandalwood", "ଚନ୍ଦନ", "chandana"],
                ["Happiness", "ଆନନ୍ଦ", "aananda"],
                ["Temple", "ମନ୍ଦିର", "mandira"],
                ["Chandelier / lamp", "ଚଂଦ୍ର", "chandra"]
            ]
        }
    ]
}

# 506 - Combining consonants in Odia (Yukta-akshara)
LESSONS[506] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["ক্ত: Devotion", "ଭକ୍ତ", "bhakta"],
                ["ସ୍ତ: Place", "ସ୍ଥାନ", "sthaana"],
                ["ନ୍ତ: End", "ଅନ୍ତ", "anta"],
                ["କ୍ଷ: Forgiveness", "କ୍ଷମା", "kshamaa"],
                ["ଜ୍ଞ: Knowledge", "ଜ୍ଞାନ", "gyaana"],
                ["ତ୍ର: Three", "ତ୍ରିଶୂଳ", "trishoola"],
                ["ସ୍କ: School", "ସ୍କୁଲ", "skula"],
                ["ପ୍ର: Question", "ପ୍ରଶ୍ନ", "prashna"],
                ["ଦ୍ର: Liquid", "ଦ୍ରବ", "draba"],
                ["ସ୍ତ୍ର: Woman", "ସ୍ତ୍ରୀ", "stree"],
                ["ଙ୍କ: Doubt", "ଆଶଙ୍କା", "aashankaa"],
                ["ଞ୍ଚ: Region", "ଅଞ୍ଚଳ", "anchala"],
                ["ଣ୍ଡ: Egg", "ଅଣ୍ଡା", "andaa"],
                ["ନ୍ଦ: Joy", "ଆନନ୍ଦ", "aananda"],
                ["ମ୍ବ: Mango", "ଆମ୍ବ", "aamba"],
                ["ଦ୍ଧ: Milk", "ଦୁଗ୍ଧ", "dugdha"],
                ["ତ୍ତ: Principle", "ତତ୍ତ୍ୱ", "tattwa"],
                ["ଶ୍ର: Labour", "ଶ୍ରମ", "shrama"]
            ]
        }
    ]
}

# 507 - Rules of writing numbers in Odia
LESSONS[507] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Zero (0)", "୦", "shunya"],
                ["One (1)", "୧", "eka"],
                ["Two (2)", "୨", "dui"],
                ["Three (3)", "୩", "tini"],
                ["Four (4)", "୪", "chaari"],
                ["Five (5)", "୫", "paancha"],
                ["Six (6)", "୬", "chha"],
                ["Seven (7)", "୭", "saata"],
                ["Eight (8)", "୮", "aatha"],
                ["Nine (9)", "୯", "na"],
                ["Ten (10)", "୧୦", "dasha"],
                ["Twenty (20)", "୨୦", "kodia"],
                ["Fifty (50)", "୫୦", "panchaasha"],
                ["Hundred (100)", "୧୦୦", "shaha"],
                ["Thousand (1000)", "୧୦୦୦", "hajaara"],
                ["First", "ପ୍ରଥମ", "prathama"],
                ["Second", "ଦ୍ୱିତୀୟ", "dwiteeya"],
                ["Third", "ତୃତୀୟ", "truteeya"]
            ]
        }
    ]
}

# 508 - Common words from Odia script practice
LESSONS[508] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Hello / Greetings", "ନମସ୍କାର", "namaskaara"],
                ["Thank you", "ଧନ୍ୟବାଦ", "dhanyabaada"],
                ["Please", "ଦୟାକରି", "dayaakari"],
                ["Sorry", "କ୍ଷମା କରନ୍ତୁ", "kshamaa karantu"],
                ["Yes", "ହଁ", "haan"],
                ["No", "ନା", "naa"],
                ["Good", "ଭଲ", "bhala"],
                ["Bad", "ଖରାପ", "kharaapa"],
                ["Big", "ବଡ଼", "bada"],
                ["Small", "ଛୋଟ", "chhota"],
                ["Today", "ଆଜି", "aaji"],
                ["Tomorrow", "କାଲି", "kaali"],
                ["Yesterday", "ଗତକାଲି", "gatakaali"],
                ["Food", "ଖାଦ୍ୟ", "khaadya"],
                ["Drink", "ପାନୀୟ", "paaneeya"],
                ["Family", "ପରିବାର", "paribaara"],
                ["Love", "ପ୍ରେମ", "prema"],
                ["Country", "ଦେଶ", "desha"]
            ]
        }
    ]
}

# 509 - Reading practice for Odia beginners
LESSONS[509] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Hello, how are you?", "ନମସ୍କାର, ଆପଣ କେମିତି ଅଛନ୍ତି?", "namaskaara, aapana kemiti achhanti?"],
                ["I am fine", "ମୁଁ ଭଲ ଅଛି", "mun bhala achhi"],
                ["What is your name?", "ଆପଣଙ୍କ ନାମ କ'ଣ?", "aapananka naama kana?"],
                ["My name is Rahul", "ମୋ ନାମ ରାହୁଲ", "mo naama Raahula"],
                ["I live in Odisha", "ମୁଁ ଓଡ଼ିଶାରେ ରହେ", "mun odishaare rahe"],
                ["I go to school", "ମୁଁ ସ୍କୁଲକୁ ଯାଏ", "mun skulaku yaae"],
                ["I eat rice", "ମୁଁ ଭାତ ଖାଏ", "mun bhaata khaae"],
                ["Give me water", "ମୋତେ ପାଣି ଦିଅ", "mote paani dia"],
                ["The sun is shining", "ସୂର୍ଯ୍ୟ ଉଜ୍ଜ୍ୱଳ ଅଛି", "suuryya ujjwala achhi"],
                ["The moon is beautiful", "ଚନ୍ଦ୍ର ସୁନ୍ଦର ଅଛି", "chandra sundara achhi"],
                ["I love my country", "ମୁଁ ମୋ ଦେଶକୁ ଭଲ ପାଏ", "mun mo deshaku bhala paae"],
                ["Thank you very much", "ଆପଣଙ୍କୁ ବହୁତ ଧନ୍ୟବାଦ", "aapananku bahuta dhanyabaada"],
                ["Where are you going?", "ଆପଣ କେଉଁଠାକୁ ଯାଉଛନ୍ତି?", "aapana keunthaaku yaauchhanti?"],
                ["I am going home", "ମୁଁ ଘରକୁ ଯାଉଛି", "mun gharaku yaauchchhi"],
                ["The flowers are beautiful", "ଫୁଲଗୁଡ଼ିକ ସୁନ୍ଦର", "phulagudika sundara"],
                ["Children are playing", "ପିଲାମାନେ ଖେଳୁଛନ୍ତି", "pilaamaane kheluchhanti"],
                ["I read a book", "ମୁଁ ଏକ ବହି ପଢ଼େ", "mun eka bahi padhe"],
                ["Odisha is my homeland", "ଓଡ଼ିଶା ମୋ ମାତୃଭୂମି", "odishaa mo maatrubbhoomi"]
            ]
        }
    ]
}

for ch in d:
    if ch['id'] in LESSONS:
        ch['blocks'] = LESSONS[ch['id']]['blocks']

open('data_odia.json', 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('Section 1 (501-509) populated for Odia')
