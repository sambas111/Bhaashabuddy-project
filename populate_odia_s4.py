import json

d = json.load(open('data_odia.json', 'r', encoding='utf-8'))

LESSONS = {}

# 597 - Body parts
LESSONS[597] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Head", "ମୁଣ୍ଡ", "Munda"],
                ["Eye", "ଆଖି", "Aakhi"],
                ["Ear", "କାନ", "Kaana"],
                ["Nose", "ନାକ", "Naaka"],
                ["Mouth", "ପାଟି", "Paati"],
                ["Tongue", "ଜିଭ", "Jibha"],
                ["Tooth", "ଦାନ୍ତ", "Daanta"],
                ["Hand", "ହାତ", "Haata"],
                ["Finger", "ଆଙ୍ଗୁଳି", "Aanguli"],
                ["Leg", "ଗୋଡ଼", "Goda"],
                ["Stomach", "ପେଟ", "Peta"],
                ["Back", "ପିଠି", "Pithi"],
                ["Chest", "ଛାତି", "Chhaati"],
                ["Shoulder", "କାନ୍ଧ", "Kaandha"],
                ["Neck", "ବେକ", "Beka"],
                ["Face", "ମୁହଁ", "Muhaan"],
                ["Hair", "ଚୁଟି", "Chuti"],
                ["Heart", "ହୃଦୟ", "Hrudaya"]
            ]
        }
    ]
}

# 598 - Miscellaneous common words
LESSONS[598] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Water", "ପାଣି", "Paani"],
                ["Fire", "ନିଆଁ", "Niaan"],
                ["Air", "ବାୟୁ", "Baayu"],
                ["Earth", "ପୃଥିବୀ", "Pruthivi"],
                ["Sky", "ଆକାଶ", "Aakaasha"],
                ["Sun", "ସୂର୍ଯ୍ୟ", "Surya"],
                ["Moon", "ଚନ୍ଦ୍ର", "Chandra"],
                ["Star", "ତାରା", "Taaraa"],
                ["Rain", "ବର୍ଷା", "Barshaa"],
                ["Road", "ରାସ୍ତା", "Raastaa"],
                ["House", "ଘର", "Ghara"],
                ["Door", "କବାଟ", "Kabaata"],
                ["Window", "ଝରକା", "Jharakaa"],
                ["Food", "ଖାଦ୍ୟ", "Khaadya"],
                ["Sleep", "ନିଦ", "Nida"],
                ["Work", "କାମ", "Kaama"],
                ["Name", "ନାମ", "Naama"],
                ["Time", "ସମୟ", "Samaya"]
            ]
        }
    ]
}

# 599 - Family relations
LESSONS[599] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Father", "ବାପା", "Baapaa"],
                ["Mother", "ମା", "Maa"],
                ["Brother", "ଭାଇ", "Bhaai"],
                ["Sister", "ଭଉଣୀ", "Bhauni"],
                ["Son", "ପୁଅ", "Pua"],
                ["Daughter", "ଝିଅ", "Jhia"],
                ["Grandfather", "ଆଜା", "Aajaa"],
                ["Grandmother", "ଆଈ", "Aai"],
                ["Uncle (father's brother)", "ବଡ଼ବାପା / ଛୋଟବାପା", "Badabaapaa / Chhotabaapaa"],
                ["Aunt (father's sister)", "ପିସୀ", "Pisi"],
                ["Uncle (mother's brother)", "ମାମୁଁ", "Maamun"],
                ["Aunt (mother's sister)", "ମାଉସୀ", "Mausi"],
                ["Husband", "ସ୍ୱାମୀ", "Swaami"],
                ["Wife", "ସ୍ତ୍ରୀ", "Stri"],
                ["Father-in-law", "ଶ୍ୱଶୁର", "Shwashura"],
                ["Mother-in-law", "ଶାଶୁ", "Shaashu"],
                ["Nephew", "ଭଣିଜା", "Bhanijaa"],
                ["Niece", "ଭଣିଜି", "Bhaniji"]
            ]
        }
    ]
}

# 600 - Numbers part 1 (1-50)
LESSONS[600] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["One (1)", "ଏକ", "Eka"],
                ["Two (2)", "ଦୁଇ", "Dui"],
                ["Three (3)", "ତିନି", "Tini"],
                ["Four (4)", "ଚାରି", "Chaari"],
                ["Five (5)", "ପାଞ୍ଚ", "Paancha"],
                ["Six (6)", "ଛଅ", "Chhaa"],
                ["Seven (7)", "ସାତ", "Saata"],
                ["Eight (8)", "ଆଠ", "Aatha"],
                ["Nine (9)", "ନଅ", "Naa"],
                ["Ten (10)", "ଦଶ", "Dasha"],
                ["Eleven (11)", "ଏଗାର", "Egaara"],
                ["Twelve (12)", "ବାର", "Baara"],
                ["Fifteen (15)", "ପନ୍ଦର", "Pandara"],
                ["Twenty (20)", "କୋଡ଼ିଏ", "Kodie"],
                ["Twenty-five (25)", "ପଚିଶ", "Pachisha"],
                ["Thirty (30)", "ତିରିଶ", "Tirisha"],
                ["Forty (40)", "ଚାଳିଶ", "Chaalisha"],
                ["Fifty (50)", "ପଚାଶ", "Pachaasha"]
            ]
        }
    ]
}

# 601 - Numbers part 2 (50-100, ordinals)
LESSONS[601] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Sixty (60)", "ଷାଠିଏ", "Shaathie"],
                ["Seventy (70)", "ସତୁରୀ", "Saturi"],
                ["Eighty (80)", "ଅଶୀ", "Ashi"],
                ["Ninety (90)", "ନବେ", "Nabe"],
                ["Hundred (100)", "ଶହ", "Shaha"],
                ["Thousand (1000)", "ହଜାର", "Hajaara"],
                ["Lakh (100,000)", "ଲକ୍ଷ", "Laksha"],
                ["First", "ପ୍ରଥମ", "Prathama"],
                ["Second", "ଦ୍ୱିତୀୟ", "Dwitiya"],
                ["Third", "ତୃତୀୟ", "Trutiya"],
                ["Fourth", "ଚତୁର୍ଥ", "Chaturtha"],
                ["Fifth", "ପଞ୍ଚମ", "Panchama"],
                ["Sixth", "ଷଷ୍ଠ", "Shashtha"],
                ["Seventh", "ସପ୍ତମ", "Saptama"],
                ["Eighth", "ଅଷ୍ଟମ", "Ashtama"],
                ["Ninth", "ନବମ", "Nabama"],
                ["Tenth", "ଦଶମ", "Dashama"],
                ["Last", "ଶେଷ", "Shesha"]
            ]
        }
    ]
}

# 602 - Fractions and measures
LESSONS[602] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Half", "ଅଧା", "Adhaa"],
                ["Quarter", "ଚଉଥାଇ", "Chauthaai"],
                ["Three-quarters", "ପୌଣ", "Pauna"],
                ["One and a half", "ଡେଢ଼", "Dedha"],
                ["Two and a half", "ଆଢ଼େଇ", "Aadhei"],
                ["Double", "ଦୁଗୁଣ", "Duguna"],
                ["Kilogram", "କିଲୋଗ୍ରାମ", "Kilogram"],
                ["Litre", "ଲିଟର", "Litara"],
                ["Metre", "ମିଟର", "Mitara"],
                ["Inch", "ଇଞ୍ଚ", "Incha"],
                ["Dozen", "ଡଜନ", "Dajana"],
                ["Pair", "ଯୋଡ଼ା", "Jodaa"],
                ["A little", "ଟିକେ", "Tike"],
                ["Much / many", "ବହୁତ", "Bahuta"],
                ["All", "ସବୁ", "Sabu"],
                ["Some", "କିଛି", "Kichhi"],
                ["More", "ଅଧିକ", "Adhika"],
                ["Less", "କମ୍", "Kam"]
            ]
        }
    ]
}

# 603 - Common verbs
LESSONS[603] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["To eat", "ଖାଇବା", "Khaaibaa"],
                ["To drink", "ପିଇବା", "Piibaa"],
                ["To go", "ଯିବା", "Jibaa"],
                ["To come", "ଆସିବା", "Aasibaa"],
                ["To speak", "କହିବା", "Kahibaa"],
                ["To hear", "ଶୁଣିବା", "Shunibaa"],
                ["To see", "ଦେଖିବା", "Dekhibaa"],
                ["To read", "ପଢ଼ିବା", "Padhibaa"],
                ["To write", "ଲେଖିବା", "Lekhibaa"],
                ["To sleep", "ଶୋଇବା", "Shoibaa"],
                ["To sit", "ବସିବା", "Basibaa"],
                ["To stand", "ଠିଆ ହେବା", "Thia hebaa"],
                ["To walk", "ଚାଲିବା", "Chaalibaa"],
                ["To run", "ଦୌଡ଼ିବା", "Daudibaa"],
                ["To give", "ଦେବା", "Debaa"],
                ["To take", "ନେବା", "Nebaa"],
                ["To do", "କରିବା", "Karibaa"],
                ["To know", "ଜାଣିବା", "Jaanibaa"]
            ]
        }
    ]
}

# 604 - Adjectives
LESSONS[604] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Big", "ବଡ଼", "Bada"],
                ["Small", "ଛୋଟ", "Chhota"],
                ["Good", "ଭଲ", "Bhala"],
                ["Bad", "ଖରାପ", "Kharaapa"],
                ["Hot", "ଗରମ", "Garama"],
                ["Cold", "ଥଣ୍ଡା", "Thandaa"],
                ["New", "ନୂଆ", "Nuaa"],
                ["Old", "ପୁରୁଣା", "Purunaa"],
                ["Beautiful", "ସୁନ୍ଦର", "Sundara"],
                ["Ugly", "କୁରୂପା", "Kurupaa"],
                ["Long", "ଲମ୍ବା", "Lambaa"],
                ["Short", "ଛୋଟ", "Chhota"],
                ["Heavy", "ଭାରି", "Bhaari"],
                ["Light", "ହାଲୁକା", "Haalukaa"],
                ["Sweet", "ମିଠା", "Mithaa"],
                ["Sour", "ଖଟା", "Khataa"],
                ["Soft", "ନରମ", "Narama"],
                ["Hard", "କଠିନ", "Kathina"]
            ]
        }
    ]
}

# 605 - Adverbs
LESSONS[605] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Here", "ଏଠାରେ", "Ethaare"],
                ["There", "ସେଠାରେ", "Sethaare"],
                ["Now", "ଏବେ", "Ebe"],
                ["Then", "ସେତେବେଳେ", "Setebele"],
                ["Today", "ଆଜି", "Aaji"],
                ["Tomorrow", "କାଲି", "Kaali"],
                ["Yesterday", "ଗତକାଲି", "Gatakaali"],
                ["Quickly", "ଶୀଘ୍ର", "Shighra"],
                ["Slowly", "ଧୀରେ", "Dhire"],
                ["Always", "ସବୁବେଳେ", "Sabubele"],
                ["Never", "କେବେ ନାହିଁ", "Kebe naaheen"],
                ["Very", "ବହୁତ", "Bahuta"],
                ["Again", "ପୁଣି", "Puni"],
                ["Together", "ଏକାଠି", "Ekaathi"],
                ["Alone", "ଏକୁଟିଆ", "Ekutiaa"],
                ["Above", "ଉପରେ", "Upare"],
                ["Below", "ତଳେ", "Tale"],
                ["Inside", "ଭିତରେ", "Bhitare"]
            ]
        }
    ]
}

# 606 - Vegetables
LESSONS[606] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Potato", "ଆଳୁ", "Aalu"],
                ["Tomato", "ଟମାଟୋ", "Tamaato"],
                ["Onion", "ପିଆଜ", "Piaaja"],
                ["Brinjal", "ବାଇଗଣ", "Baaigana"],
                ["Cauliflower", "ଫୁଲକୋବି", "Phulkobi"],
                ["Cabbage", "ବନ୍ଧାକୋବି", "Bandhaakobi"],
                ["Spinach", "ପାଳଙ୍ଗ", "Paalanga"],
                ["Pumpkin", "କଖାରୁ", "Kakhaaru"],
                ["Bitter gourd", "କଲରା", "Kalaraa"],
                ["Bottle gourd", "ଲାଉ", "Laau"],
                ["Radish", "ମୂଳା", "Mulaa"],
                ["Carrot", "ଗାଜର", "Gaajara"],
                ["Okra", "ଭେଣ୍ଡି", "Bhendi"],
                ["Pea", "ମଟର", "Matara"],
                ["Drumstick", "ସଜନା", "Sajanaa"],
                ["Green chilli", "ଲଙ୍କା", "Lankaa"],
                ["Garlic", "ରସୁଣ", "Rasuna"],
                ["Ginger", "ଅଦା", "Adaa"]
            ]
        }
    ]
}

# 607 - Fruits
LESSONS[607] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Mango", "ଆମ୍ବ", "Aamba"],
                ["Banana", "କଦଳୀ", "Kadali"],
                ["Coconut", "ନଡ଼ିଆ", "Nadiaa"],
                ["Jackfruit", "ପଣସ", "Panasa"],
                ["Papaya", "ଅମୃତଭଣ୍ଡା", "Amrutabhandaa"],
                ["Guava", "ପିଜୁଳି", "Pijuli"],
                ["Lemon", "ଲେମ୍ବୁ", "Lembu"],
                ["Watermelon", "ତରଭୁଜ", "Tarabhuja"],
                ["Pomegranate", "ଡାଳିମ୍ବ", "Daalimba"],
                ["Grape", "ଅଙ୍ଗୁର", "Angura"],
                ["Apple", "ସେଓ", "Seo"],
                ["Orange", "କମଳା", "Kamalaa"],
                ["Pineapple", "ସପୁରୀ", "Sapuri"],
                ["Litchi", "ଲିଚୁ", "Lichu"],
                ["Wood apple", "କଇଁଥ", "Kaintha"],
                ["Sugarcane", "ଆଖୁ", "Aakhu"],
                ["Date", "ଖଜୁରୀ", "Khajuri"],
                ["Custard apple", "ଆତା", "Aataa"]
            ]
        }
    ]
}

# 608 - Birds
LESSONS[608] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Crow", "କାଉ", "Kaau"],
                ["Sparrow", "ଚଟିଆ", "Chatiaa"],
                ["Parrot", "ଶୁଆ", "Shuaa"],
                ["Pigeon", "କପୋତ", "Kapota"],
                ["Peacock", "ମୟୂର", "Mayura"],
                ["Owl", "ପେଚା", "Pechaa"],
                ["Eagle", "ଚିଲ", "Chila"],
                ["Swan", "ହଂସ", "Hansa"],
                ["Cuckoo", "କୋଇଲି", "Koili"],
                ["Hen", "କୁକୁଡ଼ା", "Kukudaa"],
                ["Duck", "ବତକ", "Bataka"],
                ["Crane", "ବଗ", "Baga"],
                ["Woodpecker", "କଠବୁଡ଼ା", "Kathabudaa"],
                ["Kingfisher", "ମାଛରଙ୍କା", "Maachharankaa"],
                ["Mynah", "ଶାରୀ", "Shaari"],
                ["Vulture", "ଶକୁନି", "Shakuni"],
                ["Kite", "ଚିଲିକା", "Chilikaa"],
                ["Heron", "ବକ", "Baka"]
            ]
        }
    ]
}

# 609 - Insects
LESSONS[609] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Ant", "ପିମ୍ପୁଡ଼ି", "Pimpudi"],
                ["Mosquito", "ମଶା", "Mashaa"],
                ["Fly", "ମାଛି", "Maachhi"],
                ["Butterfly", "ପ୍ରଜାପତି", "Prajaapati"],
                ["Spider", "ମାକୁନ୍ଦା", "Maakundaa"],
                ["Bee", "ମହୁମାଛି", "Mahumaachhi"],
                ["Cockroach", "ଝିଟିପିଟି", "Jhitipiti"],
                ["Grasshopper", "ଫଟିଙ୍ଗା", "Phatingaa"],
                ["Beetle", "ଗୋବର ପୋକ", "Gobara poka"],
                ["Scorpion", "କଇଁଛ", "Kaainchha"],
                ["Earthworm", "କେନ୍ଦୁଆ", "Kenduaa"],
                ["Centipede", "ଖାଉରା", "Khaauraa"],
                ["Termite", "ଉଇ", "Ui"],
                ["Louse", "ଉକୁଣି", "Ukuni"],
                ["Bug", "ପୋକ", "Poka"],
                ["Dragonfly", "ଗଣ୍ଡାରୀ", "Gandaari"],
                ["Caterpillar", "ଶୁଆପୋକ", "Shuaapoka"],
                ["Firefly", "ଜୋନାକୀ ପୋକ", "Jonaaki poka"]
            ]
        }
    ]
}

# 610 - Colours
LESSONS[610] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Red", "ଲାଲ", "Laala"],
                ["Blue", "ନୀଳ", "Nila"],
                ["Green", "ସବୁଜ", "Sabuja"],
                ["Yellow", "ହଳଦିଆ", "Haladiaa"],
                ["White", "ଧଳା", "Dhalaa"],
                ["Black", "କଳା", "Kalaa"],
                ["Orange", "କମଳା", "Kamalaa"],
                ["Pink", "ଗୋଲାପି", "Golaapi"],
                ["Purple", "ବାଇଗଣୀ", "Baaigani"],
                ["Brown", "ବାଦାମୀ", "Baadaami"],
                ["Grey", "ଧୂସର", "Dhusara"],
                ["Golden", "ସୁନେଲୀ", "Suneli"],
                ["Silver", "ରୂପାଳୀ", "Rupaali"],
                ["Maroon", "ଗାଢ଼ ଲାଲ", "Gaadha laala"],
                ["Sky blue", "ଆକାଶୀ", "Aakaashi"],
                ["Saffron", "କେଶରୀ", "Keshari"],
                ["Cream", "କ୍ରିମ୍", "Krim"],
                ["Dark", "ଗାଢ଼", "Gaadha"]
            ]
        }
    ]
}

# 611 - Flowers
LESSONS[611] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Rose", "ଗୋଲାପ", "Golaapa"],
                ["Lotus", "ପଦ୍ମ", "Padma"],
                ["Jasmine", "ମଲ୍ଲୀ", "Malli"],
                ["Marigold", "ଗେନ୍ଦା", "Gendaa"],
                ["Hibiscus", "ମନ୍ଦାର", "Mandaara"],
                ["Sunflower", "ସୂର୍ଯ୍ୟମୁଖୀ", "Suryamukhi"],
                ["Lily", "କୁମୁଦ", "Kumuda"],
                ["Champa", "ଚମ୍ପା", "Champaa"],
                ["Night jasmine", "ଶେଫାଳୀ", "Shephaali"],
                ["Bougainvillea", "କାଗଜ ଫୁଲ", "Kaagaja phula"],
                ["Oleander", "କରବୀର", "Karabira"],
                ["Tuberose", "ରଜନୀଗନ୍ଧା", "Rajanigandhaa"],
                ["Chrysanthemum", "ଚନ୍ଦ୍ରମଲ୍ଲିକା", "Chandramallikaa"],
                ["Plumeria", "କଳା ଚମ୍ପା", "Kalaa champaa"],
                ["Magnolia", "ଚମ୍ପକ", "Champaka"],
                ["Palash", "ପଳାଶ", "Palaasha"],
                ["Aparajita", "ଅପରାଜିତା", "Aparaajitaa"],
                ["Bakul", "ବକୁଳ", "Bakula"]
            ]
        }
    ]
}

# 612 - Animals (domestic)
LESSONS[612] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Cow", "ଗାଈ", "Gaai"],
                ["Buffalo", "ମଇଁଷୀ", "Mainshi"],
                ["Goat", "ଛେଳି", "Chheli"],
                ["Sheep", "ମେଣ୍ଢା", "Mendhaa"],
                ["Horse", "ଘୋଡ଼ା", "Ghodaa"],
                ["Donkey", "ଗଧ", "Gadha"],
                ["Dog", "କୁକୁର", "Kukura"],
                ["Cat", "ବିଲେଇ", "Bilei"],
                ["Pig", "ଘୁଷୁରି", "Ghusuri"],
                ["Ox", "ବଳଦ", "Balada"],
                ["Calf", "ବାଛୁରି", "Baachhuri"],
                ["Hen", "କୁକୁଡ଼ା", "Kukudaa"],
                ["Rooster", "ତାମ୍ବା କୁକୁଡ଼ା", "Taambaa kukudaa"],
                ["Duck", "ବତକ", "Bataka"],
                ["Pigeon", "କପୋତ", "Kapota"],
                ["Rabbit", "ଖରଗୋଶ", "Kharagosha"],
                ["Camel", "ଓଟ", "Ota"],
                ["Elephant", "ହାତୀ", "Haati"]
            ]
        }
    ]
}

# 613 - Animals (wild)
LESSONS[613] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Tiger", "ବାଘ", "Baagha"],
                ["Lion", "ସିଂହ", "Sinha"],
                ["Leopard", "ଚିତାବାଘ", "Chitaabaagha"],
                ["Bear", "ଭାଲୁ", "Bhaalu"],
                ["Deer", "ହରିଣ", "Harina"],
                ["Monkey", "ମାଙ୍କଡ଼", "Maankada"],
                ["Fox", "ଲୋମଡ଼ି", "Lomadi"],
                ["Wolf", "ଗଣ୍ଡା", "Gandaa"],
                ["Crocodile", "କୁମ୍ଭୀର", "Kumbhira"],
                ["Snake", "ସାପ", "Saapa"],
                ["Tortoise", "କଇଁଛ", "Kaainchha"],
                ["Frog", "ବେଙ୍ଗ", "Benga"],
                ["Rhinoceros", "ଗଣ୍ଡା", "Gandaa"],
                ["Hyena", "ହେନା", "Henaa"],
                ["Jackal", "ଶିଆଳ", "Shiaala"],
                ["Porcupine", "ଶାଳ", "Shaala"],
                ["Mongoose", "ନେଉଳ", "Neula"],
                ["Squirrel", "ଖରିକୀରି", "Kharikiri"]
            ]
        }
    ]
}

# 614 - Kitchen items
LESSONS[614] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Plate", "ଥାଳି", "Thaali"],
                ["Bowl", "ବାଟି", "Baati"],
                ["Glass", "ଗ୍ଲାସ", "Glaasa"],
                ["Spoon", "ଚାମଚ", "Chaamacha"],
                ["Knife", "ଛୁରୀ", "Chhuri"],
                ["Cooking pot", "ହାଣ୍ଡି", "Haandi"],
                ["Frying pan", "କଡ଼େଇ", "Kadei"],
                ["Ladle", "ଝୋଟା", "Jhotaa"],
                ["Sieve", "ଛଣା", "Chhanaa"],
                ["Mortar", "ଖଲ", "Khala"],
                ["Pestle", "ମୂସଳ", "Musala"],
                ["Rolling pin", "ଅପିନୁଆ", "Apinuaa"],
                ["Stove", "ଚୁଲ୍ହା", "Chulhaa"],
                ["Grinding stone", "ଶିଲ୍ ବାଟା", "Shil baataa"],
                ["Water pot", "କୁଣ୍ଡ", "Kunda"],
                ["Tray", "ଟ୍ରେ", "Tre"],
                ["Lid", "ଢାକୁଣୀ", "Dhaakuni"],
                ["Bucket", "ବାଲ୍ଟି", "Baalti"]
            ]
        }
    ]
}

# 615 - Clothing
LESSONS[615] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Saree", "ଶାଢ଼ୀ", "Shaadhi"],
                ["Dhoti", "ଧୋତି", "Dhoti"],
                ["Shirt", "ସାର୍ଟ", "Saarta"],
                ["Trousers", "ପ୍ୟାଣ୍ଟ", "Pyaanta"],
                ["Blouse", "ବ୍ଲାଉଜ", "Blaauja"],
                ["Shawl", "ଚାଦର", "Chaadara"],
                ["Turban", "ପଗଡ଼ୀ", "Pagadi"],
                ["Lungi", "ଲୁଙ୍ଗି", "Lungi"],
                ["Cap", "ଟୋପି", "Topi"],
                ["Shoes", "ଜୋତା", "Jotaa"],
                ["Sandals", "ଚପଲ", "Chapala"],
                ["Socks", "ମୋଜା", "Mojaa"],
                ["Belt", "ବେଲ୍ଟ", "Belta"],
                ["Scarf", "ମଫଲର", "Maphalara"],
                ["Petticoat", "ସାୟା", "Saayaa"],
                ["Undershirt", "ଗାଞ୍ଜି", "Gaanji"],
                ["Sweater", "ସ୍ୱେଟର", "Swetara"],
                ["Handkerchief", "ରୁମାଲ", "Rumaala"]
            ]
        }
    ]
}

# 616 - Musical instruments
LESSONS[616] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Drum", "ଢୋଲ", "Dhola"],
                ["Flute", "ବଂଶୀ", "Banshi"],
                ["Harmonium", "ହାର୍ମୋନିୟମ", "Haarmoniyam"],
                ["Tabla", "ତବଲା", "Tabalaa"],
                ["Sitar", "ସିତାର", "Sitaara"],
                ["Mridangam", "ମୃଦଙ୍ଗ", "Mrudanga"],
                ["Cymbals", "ଝାଞ୍ଜ", "Jhaanja"],
                ["Conch", "ଶଙ୍ଖ", "Shankha"],
                ["Veena", "ବୀଣା", "Binaa"],
                ["Gong", "ଘଣ୍ଟା", "Ghantaa"],
                ["Pakhawaj", "ପାଖୋୱାଜ", "Paakhowaaja"],
                ["Violin", "ବେହେଲା", "Behelaa"],
                ["Trumpet", "ତୁରହୀ", "Turahi"],
                ["Dholak", "ଢୋଲକ", "Dholaka"],
                ["Nagara", "ନଗାରା", "Nagaaraa"],
                ["Khol", "ଖୋଲ", "Khola"],
                ["Sarangi", "ସାରଙ୍ଗୀ", "Saarangi"],
                ["Bell", "ଘଣ୍ଟି", "Ghanti"]
            ]
        }
    ]
}

# 617 - Tools and implements
LESSONS[617] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Axe", "କୁରାଡ଼ି", "Kuraadi"],
                ["Hammer", "ହାତୁଡ଼ି", "Haatudi"],
                ["Plough", "ଲାଙ୍ଗଳ", "Laangala"],
                ["Sickle", "କାତି", "Kaati"],
                ["Saw", "କରତ", "Karata"],
                ["Spade", "କୋଦାଳ", "Kodaala"],
                ["Shovel", "ବେଲ୍ ଚା", "Bel chaa"],
                ["Needle", "ଛୁଞ୍ଚି", "Chhunchi"],
                ["Scissors", "କଇଁଚି", "Kainchi"],
                ["Rope", "ଦଉଡ଼ି", "Daudi"],
                ["Ladder", "ସିଡ଼ି", "Sidi"],
                ["Broom", "ଝାଡ଼ୁ", "Jhaadu"],
                ["Chisel", "ଛେନି", "Chheni"],
                ["Nail", "କିଳା", "Kilaa"],
                ["Hook", "ବନ୍ସୀ", "Bansi"],
                ["Yoke", "ଯୁଗଳ", "Jugala"],
                ["Fishing net", "ଜାଲ", "Jaala"],
                ["Wheel", "ଚକ", "Chaka"]
            ]
        }
    ]
}

# 618 - Seasons and weather
LESSONS[618] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Summer", "ଗ୍ରୀଷ୍ମ", "Grishma"],
                ["Rainy season", "ବର୍ଷା", "Barshaa"],
                ["Autumn", "ଶରତ", "Sharata"],
                ["Winter", "ଶୀତ", "Shita"],
                ["Spring", "ବସନ୍ତ", "Basanta"],
                ["Late autumn", "ହେମନ୍ତ", "Hemanta"],
                ["Rain", "ବୃଷ୍ଟି", "Brushti"],
                ["Cloud", "ମେଘ", "Megha"],
                ["Thunder", "ବଜ୍ର", "Bajra"],
                ["Lightning", "ବିଜୁଳୀ", "Bijuli"],
                ["Storm", "ଝଡ଼", "Jhada"],
                ["Flood", "ବନ୍ୟା", "Banyaa"],
                ["Drought", "ଖରା", "Kharaa"],
                ["Fog", "କୁହୁଡ଼ି", "Kuhudi"],
                ["Dew", "ଶିଶିର", "Shishira"],
                ["Hail", "ଶିଳାବୃଷ୍ଟି", "Shilaabrushti"],
                ["Wind", "ବାଉଳ", "Baauala"],
                ["Rainbow", "ଇନ୍ଦ୍ରଧନୁ", "Indradhanu"]
            ]
        }
    ]
}

# 619 - Common miscellaneous words
LESSONS[619] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Book", "ବହି", "Bahi"],
                ["Pen", "କଲମ", "Kalama"],
                ["School", "ବିଦ୍ୟାଳୟ", "Bidyaalaya"],
                ["Teacher", "ଶିକ୍ଷକ", "Shikshaka"],
                ["Student", "ଛାତ୍ର", "Chhaatra"],
                ["Market", "ବଜାର", "Bajaara"],
                ["Money", "ଟଙ୍କା", "Tankaa"],
                ["River", "ନଦୀ", "Nadi"],
                ["Mountain", "ପର୍ବତ", "Parbata"],
                ["Tree", "ଗଛ", "Gachha"],
                ["Flower", "ଫୁଲ", "Phula"],
                ["Song", "ଗୀତ", "Gita"],
                ["Dance", "ନାଚ", "Naacha"],
                ["Festival", "ପର୍ବ", "Parba"],
                ["Temple", "ମନ୍ଦିର", "Mandira"],
                ["Village", "ଗାଁ", "Gaan"],
                ["City", "ସହର", "Sahara"],
                ["Country", "ଦେଶ", "Desha"]
            ]
        }
    ]
}

for ch in d:
    if ch['id'] in LESSONS:
        ch['blocks'] = LESSONS[ch['id']]['blocks']

open('data_odia.json', 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(f'Section 4 (IDs 597-619, {len(LESSONS)} lessons) populated successfully.')
for lid in sorted(LESSONS.keys()):
    rows = LESSONS[lid]['blocks'][0]['rows']
    print(f'  ID {lid}: {len(rows)} rows')
