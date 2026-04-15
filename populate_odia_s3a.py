import json

d = json.load(open('data_odia.json', 'r', encoding='utf-8'))

LESSONS = {}

# 543: "This is..." / "That is..." patterns
LESSONS[543] = {
    "url": "\"This is / That is\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["This is a book", "ଏହା ଏକ ବହି", "eha eka bahi"],
                ["That is a house", "ସେଇଟା ଏକ ଘର", "seita eka ghara"],
                ["This is my mother", "ଏ ମୋ ମା", "e mo maa"],
                ["That is your father", "ସେ ତୁମ ବାପା", "se tuma bapa"],
                ["This is very good", "ଏହା ବହୁତ ଭଲ", "eha bahut bhala"],
                ["That is a school", "ସେଇଟା ଏକ ସ୍କୁଲ", "seita eka school"],
                ["This is my friend", "ଏ ମୋ ବନ୍ଧୁ", "e mo bandhu"],
                ["That is a temple", "ସେଇଟା ଏକ ମନ୍ଦିର", "seita eka mandira"],
                ["This is water", "ଏହା ପାଣି", "eha pani"],
                ["That is milk", "ସେଇଟା କ୍ଷୀର", "seita kshira"],
                ["This is a new shirt", "ଏହା ଏକ ନୂଆ ଜାମା", "eha eka nua jama"],
                ["That is an old tree", "ସେଇଟା ଏକ ପୁରୁଣା ଗଛ", "seita eka puruna gachha"],
                ["This is hot tea", "ଏହା ଗରମ ଚା", "eha garama cha"],
                ["That is cold water", "ସେଇଟା ଥଣ୍ଡା ପାଣି", "seita thanda pani"],
                ["This is my village", "ଏହା ମୋ ଗାଁ", "eha mo gaan"],
                ["That is a big market", "ସେଇଟା ଏକ ବଡ଼ ବଜାର", "seita eka bada bajara"],
                ["This is the right way", "ଏହା ସଠିକ ରାସ୍ତା", "eha sathika rasta"],
                ["That is a beautiful flower", "ସେଇଟା ଏକ ସୁନ୍ଦର ଫୁଲ", "seita eka sundara phula"]
            ]
        }
    ]
}

# 544: "I want..." patterns (ମୁଁ ଚାହେଁ...)
LESSONS[544] = {
    "url": "\"I want\" (ମୁଁ ଚାହେଁ) patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["I want water", "ମୁଁ ପାଣି ଚାହେଁ", "mun pani chahen"],
                ["I want to eat", "ମୁଁ ଖାଇବାକୁ ଚାହେଁ", "mun khaibaku chahen"],
                ["I want to go home", "ମୁଁ ଘରକୁ ଯିବାକୁ ଚାହେଁ", "mun gharaku jibaku chahen"],
                ["I want to sleep", "ମୁଁ ଶୋଇବାକୁ ଚାହେଁ", "mun shoibaku chahen"],
                ["I want tea", "ମୁଁ ଚା ଚାହେଁ", "mun cha chahen"],
                ["I want to learn Odia", "ମୁଁ ଓଡ଼ିଆ ଶିଖିବାକୁ ଚାହେଁ", "mun odia shikhibaku chahen"],
                ["I want a new book", "ମୁଁ ଏକ ନୂଆ ବହି ଚାହେଁ", "mun eka nua bahi chahen"],
                ["I want to talk to you", "ମୁଁ ତୁମ ସହ କଥା ହେବାକୁ ଚାହେଁ", "mun tuma saha katha hebaku chahen"],
                ["I want to rest", "ମୁଁ ବିଶ୍ରାମ ନେବାକୁ ଚାହେଁ", "mun bishrama nebaku chahen"],
                ["I want to play", "ମୁଁ ଖେଳିବାକୁ ଚାହେଁ", "mun khelibaku chahen"],
                ["I want to buy vegetables", "ମୁଁ ପରିବା କିଣିବାକୁ ଚାହେଁ", "mun pariba kinibaku chahen"],
                ["I want to see the sea", "ମୁଁ ସମୁଦ୍ର ଦେଖିବାକୁ ଚାହେଁ", "mun samudra dekhibaku chahen"],
                ["I want to help you", "ମୁଁ ତୁମକୁ ସାହାଯ୍ୟ କରିବାକୁ ଚାହେଁ", "mun tumaku sahajya karibaku chahen"],
                ["I want rice", "ମୁଁ ଭାତ ଚାହେଁ", "mun bhata chahen"],
                ["I want to work", "ମୁଁ କାମ କରିବାକୁ ଚାହେଁ", "mun kama karibaku chahen"],
                ["I want to go to Puri", "ମୁଁ ପୁରୀ ଯିବାକୁ ଚାହେଁ", "mun Puri jibaku chahen"],
                ["I want to read the newspaper", "ମୁଁ ଖବରକାଗଜ ପଢ଼ିବାକୁ ଚାହେଁ", "mun khabarakagaja padhibaku chahen"],
                ["I want to meet him", "ମୁଁ ତାଙ୍କୁ ଭେଟିବାକୁ ଚାହେଁ", "mun tanku bhetibaku chahen"]
            ]
        }
    ]
}

# 545: "I am going to..." patterns
LESSONS[545] = {
    "url": "\"I am going to\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["I am going to eat", "ମୁଁ ଖାଇବାକୁ ଯାଉଛି", "mun khaibaku jauchhi"],
                ["I am going to school", "ମୁଁ ସ୍କୁଲକୁ ଯାଉଛି", "mun schoolku jauchhi"],
                ["I am going to sleep now", "ମୁଁ ଏବେ ଶୋଇବାକୁ ଯାଉଛି", "mun ebe shoibaku jauchhi"],
                ["I am going to cook", "ମୁଁ ରାନ୍ଧିବାକୁ ଯାଉଛି", "mun randhibaku jauchhi"],
                ["I am going to the market", "ମୁଁ ବଜାରକୁ ଯାଉଛି", "mun bajaraku jauchhi"],
                ["I am going to study", "ମୁଁ ପଢ଼ିବାକୁ ଯାଉଛି", "mun padhibaku jauchhi"],
                ["I am going to call him", "ମୁଁ ତାଙ୍କୁ ଡାକିବାକୁ ଯାଉଛି", "mun tanku dakibaku jauchhi"],
                ["I am going to wash clothes", "ମୁଁ ଲୁଗା ଧୋଇବାକୁ ଯାଉଛି", "mun luga dhoibaku jauchhi"],
                ["I am going to write a letter", "ମୁଁ ଏକ ଚିଠି ଲେଖିବାକୁ ଯାଉଛି", "mun eka chithi lekhibaku jauchhi"],
                ["I am going to take a bath", "ମୁଁ ଗାଧୋଇବାକୁ ଯାଉଛି", "mun gadhoibaku jauchhi"],
                ["I am going to watch a movie", "ମୁଁ ସିନେମା ଦେଖିବାକୁ ଯାଉଛି", "mun cinema dekhibaku jauchhi"],
                ["I am going to drink water", "ମୁଁ ପାଣି ପିଇବାକୁ ଯାଉଛି", "mun pani piibaku jauchhi"],
                ["I am going to buy rice", "ମୁଁ ଚାଉଳ କିଣିବାକୁ ଯାଉଛି", "mun chaula kinibaku jauchhi"],
                ["I am going to the hospital", "ମୁଁ ଡାକ୍ତରଖାନାକୁ ଯାଉଛି", "mun daktarakhanaku jauchhi"],
                ["I am going to play cricket", "ମୁଁ କ୍ରିକେଟ ଖେଳିବାକୁ ଯାଉଛି", "mun cricket khelibaku jauchhi"],
                ["I am going to sing a song", "ମୁଁ ଏକ ଗୀତ ଗାଇବାକୁ ଯାଉଛି", "mun eka gita gaibaku jauchhi"],
                ["I am going to tell the truth", "ମୁଁ ସତ କହିବାକୁ ଯାଉଛି", "mun sata kahibaku jauchhi"],
                ["I am going to finish the work", "ମୁଁ କାମ ସାରିବାକୁ ଯାଉଛି", "mun kama saribaku jauchhi"]
            ]
        }
    ]
}

# 546: "Can you...?" patterns
LESSONS[546] = {
    "url": "\"Can you...?\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Can you help me?", "ତୁମେ ମୋତେ ସାହାଯ୍ୟ କରିପାରିବ କି?", "tume mote sahajya karipariba ki?"],
                ["Can you speak Odia?", "ତୁମେ ଓଡ଼ିଆ କହିପାରିବ କି?", "tume odia kahipariba ki?"],
                ["Can you come tomorrow?", "ତୁମେ ଆସନ୍ତାକାଲି ଆସିପାରିବ କି?", "tume asantakali asipariba ki?"],
                ["Can you open the door?", "ତୁମେ କବାଟ ଖୋଲିପାରିବ କି?", "tume kabata kholipariba ki?"],
                ["Can you give me water?", "ତୁମେ ମୋତେ ପାଣି ଦେଇପାରିବ କି?", "tume mote pani deipariba ki?"],
                ["Can you drive a car?", "ତୁମେ ଗାଡ଼ି ଚଳାଇ ପାରିବ କି?", "tume gadi chalai pariba ki?"],
                ["Can you read this?", "ତୁମେ ଏହା ପଢ଼ିପାରିବ କି?", "tume eha padhipariba ki?"],
                ["Can you wait a moment?", "ତୁମେ ଟିକେ ଅପେକ୍ଷା କରିପାରିବ କି?", "tume tike apeksha karipariba ki?"],
                ["Can you cook rice?", "ତୁମେ ଭାତ ରାନ୍ଧିପାରିବ କି?", "tume bhata randhipariba ki?"],
                ["Can you write in Odia?", "ତୁମେ ଓଡ଼ିଆରେ ଲେଖିପାରିବ କି?", "tume odiare lekhipariba ki?"],
                ["Can you sing a song?", "ତୁମେ ଏକ ଗୀତ ଗାଇପାରିବ କି?", "tume eka gita gaipariba ki?"],
                ["Can you carry this bag?", "ତୁମେ ଏହି ବ୍ୟାଗ ବୋହିପାରିବ କି?", "tume ehi bag bohipariba ki?"],
                ["Can you teach me?", "ତୁମେ ମୋତେ ଶିଖାଇ ପାରିବ କି?", "tume mote shikhai pariba ki?"],
                ["Can you tell me the way?", "ତୁମେ ମୋତେ ରାସ୍ତା କହିପାରିବ କି?", "tume mote rasta kahipariba ki?"],
                ["Can you call a doctor?", "ତୁମେ ଜଣେ ଡାକ୍ତର ଡାକିପାରିବ କି?", "tume jane daktar dakipariba ki?"],
                ["Can you close the window?", "ତୁମେ ଝରକା ବନ୍ଦ କରିପାରିବ କି?", "tume jharaka banda karipariba ki?"],
                ["Can you hear me?", "ତୁମେ ମୋ କଥା ଶୁଣିପାରୁଛ କି?", "tume mo katha shuniparuchha ki?"],
                ["Can you understand this?", "ତୁମେ ଏହା ବୁଝିପାରୁଛ କି?", "tume eha bujiparuchha ki?"]
            ]
        }
    ]
}

# 547: "Please give me..." patterns
LESSONS[547] = {
    "url": "\"Please give me\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Please give me water", "ଦୟାକରି ମୋତେ ପାଣି ଦିଅ", "dayakari mote pani dia"],
                ["Please give me a pen", "ଦୟାକରି ମୋତେ ଏକ କଲମ ଦିଅ", "dayakari mote eka kalama dia"],
                ["Please give me rice", "ଦୟାକରି ମୋତେ ଭାତ ଦିଅ", "dayakari mote bhata dia"],
                ["Please give me some time", "ଦୟାକରି ମୋତେ ଟିକେ ସମୟ ଦିଅ", "dayakari mote tike samaya dia"],
                ["Please give me the book", "ଦୟାକରି ମୋତେ ବହିଟି ଦିଅ", "dayakari mote bahiti dia"],
                ["Please give me tea", "ଦୟାକରି ମୋତେ ଚା ଦିଅ", "dayakari mote cha dia"],
                ["Please give me one plate", "ଦୟାକରି ମୋତେ ଗୋଟିଏ ଥାଳି ଦିଅ", "dayakari mote gotie thali dia"],
                ["Please give me your number", "ଦୟାକରି ମୋତେ ତୁମ ନମ୍ବର ଦିଅ", "dayakari mote tuma number dia"],
                ["Please give me medicine", "ଦୟାକରି ମୋତେ ଔଷଧ ଦିଅ", "dayakari mote aushadha dia"],
                ["Please give me a glass of milk", "ଦୟାକରି ମୋତେ ଏକ ଗ୍ଲାସ କ୍ଷୀର ଦିଅ", "dayakari mote eka glass kshira dia"],
                ["Please give me the key", "ଦୟାକରି ମୋତେ ଚାବି ଦିଅ", "dayakari mote chabi dia"],
                ["Please give me a towel", "ଦୟାକରି ମୋତେ ଏକ ଟାଉଲ ଦିଅ", "dayakari mote eka towel dia"],
                ["Please give me your address", "ଦୟାକରି ମୋତେ ତୁମ ଠିକଣା ଦିଅ", "dayakari mote tuma thikana dia"],
                ["Please give me a chair", "ଦୟାକରି ମୋତେ ଗୋଟିଏ ଚୌକି ଦିଅ", "dayakari mote gotie chauki dia"],
                ["Please give me salt", "ଦୟାକରି ମୋତେ ଲୁଣ ଦିଅ", "dayakari mote luna dia"],
                ["Please give me some money", "ଦୟାକରି ମୋତେ ଟିକେ ଟଙ୍କା ଦିଅ", "dayakari mote tike tanka dia"],
                ["Please give me a blanket", "ଦୟାକରି ମୋତେ ଏକ କମ୍ବଳ ଦିଅ", "dayakari mote eka kambala dia"],
                ["Please give me one chance", "ଦୟାକରି ମୋତେ ଗୋଟିଏ ସୁଯୋଗ ଦିଅ", "dayakari mote gotie sujoga dia"]
            ]
        }
    ]
}

# 548: "Where is...?" patterns
LESSONS[548] = {
    "url": "\"Where is...?\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Where is the bus stop?", "ବସ୍ ଷ୍ଟପ୍ କେଉଁଠି?", "bus stop keunthi?"],
                ["Where is the hospital?", "ଡାକ୍ତରଖାନା କେଉଁଠି?", "daktarakhana keunthi?"],
                ["Where is the market?", "ବଜାର କେଉଁଠି?", "bajara keunthi?"],
                ["Where is your house?", "ତୁମ ଘର କେଉଁଠି?", "tuma ghara keunthi?"],
                ["Where is the railway station?", "ରେଳ ଷ୍ଟେସନ କେଉଁଠି?", "rel station keunthi?"],
                ["Where is the bathroom?", "ବାଥରୁମ କେଉଁଠି?", "bathroom keunthi?"],
                ["Where is my bag?", "ମୋ ବ୍ୟାଗ କେଉଁଠି?", "mo bag keunthi?"],
                ["Where is the temple?", "ମନ୍ଦିର କେଉଁଠି?", "mandira keunthi?"],
                ["Where is the school?", "ସ୍କୁଲ କେଉଁଠି?", "school keunthi?"],
                ["Where is the police station?", "ଥାନା କେଉଁଠି?", "thana keunthi?"],
                ["Where is the post office?", "ଡାକଘର କେଉଁଠି?", "dakghara keunthi?"],
                ["Where is the bank?", "ବ୍ୟାଙ୍କ କେଉଁଠି?", "bank keunthi?"],
                ["Where is the restaurant?", "ଖାଦ୍ୟ ଦୋକାନ କେଉଁଠି?", "khadya dokana keunthi?"],
                ["Where is the medicine shop?", "ଔଷଧ ଦୋକାନ କେଉଁଠି?", "aushadha dokana keunthi?"],
                ["Where is the key?", "ଚାବି କେଉଁଠି?", "chabi keunthi?"],
                ["Where is the airport?", "ବିମାନ ବନ୍ଦର କେଉଁଠି?", "bimana bandara keunthi?"],
                ["Where is the park?", "ବଗିଚା କେଉଁଠି?", "bagicha keunthi?"],
                ["Where is the library?", "ପୁସ୍ତକାଳୟ କେଉଁଠି?", "pustakaalaya keunthi?"]
            ]
        }
    ]
}

# 549: "How much/many...?" patterns
LESSONS[549] = {
    "url": "\"How much / How many\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["How much is this?", "ଏହାର ଦାମ କେତେ?", "ehara dama kete?"],
                ["How many people are there?", "କେତେ ଲୋକ ଅଛନ୍ତି?", "kete loka achhanti?"],
                ["How much water do you want?", "ତୁମେ କେତେ ପାଣି ଚାହଁ?", "tume kete pani chahan?"],
                ["How many children do you have?", "ତୁମର କେତେ ପିଲା ଅଛନ୍ତି?", "tumara kete pila achhanti?"],
                ["How much time will it take?", "କେତେ ସମୟ ଲାଗିବ?", "kete samaya lagiba?"],
                ["How many books are there?", "କେତେ ବହି ଅଛି?", "kete bahi achhi?"],
                ["How much sugar do you want?", "ତୁମେ କେତେ ଚିନି ଚାହଁ?", "tume kete chini chahan?"],
                ["How many days will you stay?", "ତୁମେ କେତେ ଦିନ ରହିବ?", "tume kete dina rahiba?"],
                ["How much does this cost?", "ଏହାର ମୂଲ୍ୟ କେତେ?", "ehara mulya kete?"],
                ["How many rooms are there?", "କେତେ ଗୋଟି ରୁମ ଅଛି?", "kete goti room achhi?"],
                ["How much rice should I cook?", "ମୁଁ କେତେ ଭାତ ରାନ୍ଧିବି?", "mun kete bhata randhihi?"],
                ["How many brothers do you have?", "ତୁମର କେତେ ଭାଇ ଅଛନ୍ତି?", "tumara kete bhai achhanti?"],
                ["How much milk is left?", "କେତେ କ୍ଷୀର ଅଛି?", "kete kshira achhi?"],
                ["How many tickets do we need?", "ଆମକୁ କେତେ ଟିକେଟ ଦରକାର?", "amaku kete ticket darakara?"],
                ["How much salt should I add?", "ମୁଁ କେତେ ଲୁଣ ଦେବି?", "mun kete luna debi?"],
                ["How many students passed?", "କେତେ ଛାତ୍ର ପାସ ହେଲେ?", "kete chhaatra pasa hele?"],
                ["How much flour do we need?", "ଆମକୁ କେତେ ମଇଦା ଦରକାର?", "amaku kete maida darakara?"],
                ["How many hours will you work?", "ତୁମେ କେତେ ଘଣ୍ଟା କାମ କରିବ?", "tume kete ghanta kama kariba?"]
            ]
        }
    ]
}

# 550: "I like..." patterns
LESSONS[550] = {
    "url": "\"I like\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["I like rice", "ମୋତେ ଭାତ ଭଲ ଲାଗେ", "mote bhata bhala lage"],
                ["I like to read books", "ମୋତେ ବହି ପଢ଼ିବାକୁ ଭଲ ଲାଗେ", "mote bahi padhibaku bhala lage"],
                ["I like this place", "ମୋତେ ଏହି ଜାଗା ଭଲ ଲାଗେ", "mote ehi jaga bhala lage"],
                ["I like mangoes", "ମୋତେ ଆମ୍ବ ଭଲ ଲାଗେ", "mote amba bhala lage"],
                ["I like singing", "ମୋତେ ଗୀତ ଗାଇବାକୁ ଭଲ ଲାଗେ", "mote gita gaibaku bhala lage"],
                ["I like playing cricket", "ମୋତେ କ୍ରିକେଟ ଖେଳିବାକୁ ଭଲ ଲାଗେ", "mote cricket khelibaku bhala lage"],
                ["I like Odia food", "ମୋତେ ଓଡ଼ିଆ ଖାଦ୍ୟ ଭଲ ଲାଗେ", "mote odia khadya bhala lage"],
                ["I like to travel", "ମୋତେ ବୁଲିବାକୁ ଭଲ ଲାଗେ", "mote bulibaku bhala lage"],
                ["I like the morning breeze", "ମୋତେ ସକାଳର ପବନ ଭଲ ଲାଗେ", "mote sakalara pabana bhala lage"],
                ["I like sweet things", "ମୋତେ ମିଠା ଜିନିଷ ଭଲ ଲାଗେ", "mote mitha jinisha bhala lage"],
                ["I like your cooking", "ମୋତେ ତୁମ ରନ୍ଧା ଭଲ ଲାଗେ", "mote tuma randha bhala lage"],
                ["I like watching movies", "ମୋତେ ସିନେମା ଦେଖିବାକୁ ଭଲ ଲାଗେ", "mote cinema dekhibaku bhala lage"],
                ["I like this song", "ମୋତେ ଏହି ଗୀତ ଭଲ ଲାଗେ", "mote ehi gita bhala lage"],
                ["I like to draw", "ମୋତେ ଛବି ଆଙ୍କିବାକୁ ଭଲ ଲାଗେ", "mote chhabi ankibaku bhala lage"],
                ["I like flowers", "ମୋତେ ଫୁଲ ଭଲ ଲାଗେ", "mote phula bhala lage"],
                ["I like the rain", "ମୋତେ ବର୍ଷା ଭଲ ଲାଗେ", "mote barsha bhala lage"],
                ["I like to dance", "ମୋତେ ନାଚିବାକୁ ଭଲ ଲାଗେ", "mote nachibaku bhala lage"],
                ["I like my village", "ମୋତେ ମୋ ଗାଁ ଭଲ ଲାଗେ", "mote mo gaan bhala lage"]
            ]
        }
    ]
}

# 551: "I don't..." patterns
LESSONS[551] = {
    "url": "\"I don't\" (negative) patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["I don't know", "ମୁଁ ଜାଣେ ନାହିଁ", "mun jane nahin"],
                ["I don't want this", "ମୁଁ ଏହା ଚାହେଁ ନାହିଁ", "mun eha chahen nahin"],
                ["I don't eat fish", "ମୁଁ ମାଛ ଖାଏ ନାହିଁ", "mun machha khae nahin"],
                ["I don't speak Hindi", "ମୁଁ ହିନ୍ଦୀ କହେ ନାହିଁ", "mun hindi kahe nahin"],
                ["I don't understand", "ମୁଁ ବୁଝେ ନାହିଁ", "mun buje nahin"],
                ["I don't have money", "ମୋ ପାଖରେ ଟଙ୍କା ନାହିଁ", "mo pakhare tanka nahin"],
                ["I don't like this", "ମୋତେ ଏହା ଭଲ ଲାଗେ ନାହିଁ", "mote eha bhala lage nahin"],
                ["I don't go there", "ମୁଁ ସେଠାକୁ ଯାଏ ନାହିଁ", "mun sethaku jae nahin"],
                ["I don't drink tea", "ମୁଁ ଚା ପିଏ ନାହିଁ", "mun cha pie nahin"],
                ["I don't remember", "ମୋ ମନେ ନାହିଁ", "mo mane nahin"],
                ["I don't believe that", "ମୁଁ ସେହା ବିଶ୍ୱାସ କରେ ନାହିଁ", "mun seha bishwasa kare nahin"],
                ["I don't have time", "ମୋ ପାଖରେ ସମୟ ନାହିଁ", "mo pakhare samaya nahin"],
                ["I don't watch TV", "ମୁଁ ଟିଭି ଦେଖେ ନାହିଁ", "mun TV dekhe nahin"],
                ["I don't smoke", "ମୁଁ ଧୂମପାନ କରେ ନାହିଁ", "mun dhumapana kare nahin"],
                ["I don't feel well", "ମୋ ଶରୀର ଭଲ ଲାଗୁ ନାହିଁ", "mo sharira bhala lagu nahin"],
                ["I don't play football", "ମୁଁ ଫୁଟବଲ ଖେଳେ ନାହିଁ", "mun football khele nahin"],
                ["I don't need help", "ମୋତେ ସାହାଯ୍ୟ ଦରକାର ନାହିଁ", "mote sahajya darakara nahin"],
                ["I don't sleep late", "ମୁଁ ଡେରିରେ ଶୋଏ ନାହିଁ", "mun derire shoe nahin"]
            ]
        }
    ]
}

# 552: "Do you have...?" patterns
LESSONS[552] = {
    "url": "\"Do you have...?\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Do you have water?", "ତୁମ ପାଖରେ ପାଣି ଅଛି କି?", "tuma pakhare pani achhi ki?"],
                ["Do you have a pen?", "ତୁମ ପାଖରେ କଲମ ଅଛି କି?", "tuma pakhare kalama achhi ki?"],
                ["Do you have money?", "ତୁମ ପାଖରେ ଟଙ୍କା ଅଛି କି?", "tuma pakhare tanka achhi ki?"],
                ["Do you have time?", "ତୁମ ପାଖରେ ସମୟ ଅଛି କି?", "tuma pakhare samaya achhi ki?"],
                ["Do you have a phone?", "ତୁମ ପାଖରେ ଫୋନ ଅଛି କି?", "tuma pakhare phone achhi ki?"],
                ["Do you have a ticket?", "ତୁମ ପାଖରେ ଟିକେଟ ଅଛି କି?", "tuma pakhare ticket achhi ki?"],
                ["Do you have the key?", "ତୁମ ପାଖରେ ଚାବି ଅଛି କି?", "tuma pakhare chabi achhi ki?"],
                ["Do you have an umbrella?", "ତୁମ ପାଖରେ ଛତା ଅଛି କି?", "tuma pakhare chhata achhi ki?"],
                ["Do you have any questions?", "ତୁମର କିଛି ପ୍ରଶ୍ନ ଅଛି କି?", "tumara kichhi prashna achhi ki?"],
                ["Do you have brothers?", "ତୁମର ଭାଇ ଅଛନ୍ତି କି?", "tumara bhai achhanti ki?"],
                ["Do you have a car?", "ତୁମ ପାଖରେ ଗାଡ଼ି ଅଛି କି?", "tuma pakhare gadi achhi ki?"],
                ["Do you have sugar?", "ତୁମ ପାଖରେ ଚିନି ଅଛି କି?", "tuma pakhare chini achhi ki?"],
                ["Do you have a map?", "ତୁମ ପାଖରେ ମାନଚିତ୍ର ଅଛି କି?", "tuma pakhare manachitra achhi ki?"],
                ["Do you have medicine?", "ତୁମ ପାଖରେ ଔଷଧ ଅଛି କି?", "tuma pakhare aushadha achhi ki?"],
                ["Do you have a bag?", "ତୁମ ପାଖରେ ବ୍ୟାଗ ଅଛି କି?", "tuma pakhare bag achhi ki?"],
                ["Do you have change?", "ତୁମ ପାଖରେ ଖୁଚୁରା ଅଛି କି?", "tuma pakhare khuchura achhi ki?"],
                ["Do you have milk?", "ତୁମ ପାଖରେ କ୍ଷୀର ଅଛି କି?", "tuma pakhare kshira achhi ki?"],
                ["Do you have experience?", "ତୁମର ଅଭିଜ୍ଞତା ଅଛି କି?", "tumara abhijnata achhi ki?"]
            ]
        }
    ]
}

# 553: "I need..." patterns
LESSONS[553] = {
    "url": "\"I need\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["I need water", "ମୋତେ ପାଣି ଦରକାର", "mote pani darakara"],
                ["I need help", "ମୋତେ ସାହାଯ୍ୟ ଦରକାର", "mote sahajya darakara"],
                ["I need a doctor", "ମୋତେ ଜଣେ ଡାକ୍ତର ଦରକାର", "mote jane daktar darakara"],
                ["I need more time", "ମୋତେ ଆଉ ସମୟ ଦରକାର", "mote aau samaya darakara"],
                ["I need money", "ମୋତେ ଟଙ୍କା ଦରକାର", "mote tanka darakara"],
                ["I need a room", "ମୋତେ ଏକ ରୁମ ଦରକାର", "mote eka room darakara"],
                ["I need food", "ମୋତେ ଖାଦ୍ୟ ଦରକାର", "mote khadya darakara"],
                ["I need rest", "ମୋତେ ବିଶ୍ରାମ ଦରକାର", "mote bishrama darakara"],
                ["I need your advice", "ମୋତେ ତୁମ ପରାମର୍ଶ ଦରକାର", "mote tuma paramarsha darakara"],
                ["I need a ticket", "ମୋତେ ଏକ ଟିକେଟ ଦରକାର", "mote eka ticket darakara"],
                ["I need medicine", "ମୋତେ ଔଷଧ ଦରକାର", "mote aushadha darakara"],
                ["I need new clothes", "ମୋତେ ନୂଆ ଲୁଗା ଦରକାର", "mote nua luga darakara"],
                ["I need a pen", "ମୋତେ ଏକ କଲମ ଦରକାର", "mote eka kalama darakara"],
                ["I need to think", "ମୋତେ ଚିନ୍ତା କରିବାକୁ ଦରକାର", "mote chinta karibaku darakara"],
                ["I need your phone number", "ମୋତେ ତୁମ ଫୋନ ନମ୍ବର ଦରକାର", "mote tuma phone number darakara"],
                ["I need a taxi", "ମୋତେ ଏକ ଟ୍ୟାକ୍ସି ଦରକାର", "mote eka taxi darakara"],
                ["I need information", "ମୋତେ ତଥ୍ୟ ଦରକାର", "mote tathya darakara"],
                ["I need two chairs", "ମୋତେ ଦୁଇଟି ଚୌକି ଦରକାର", "mote duiti chauki darakara"]
            ]
        }
    ]
}

# 554: "Let us..." patterns
LESSONS[554] = {
    "url": "\"Let us\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Let us go", "ଆସ ଯିବା", "aasa jiba"],
                ["Let us eat", "ଆସ ଖାଇବା", "aasa khaiba"],
                ["Let us sit here", "ଆସ ଏଠି ବସିବା", "aasa ethi basiba"],
                ["Let us play", "ଆସ ଖେଳିବା", "aasa kheliba"],
                ["Let us talk", "ଆସ କଥା ହେବା", "aasa katha heba"],
                ["Let us study together", "ଆସ ଏକାଠି ପଢ଼ିବା", "aasa ekathi padhiba"],
                ["Let us start the work", "ଆସ କାମ ଆରମ୍ଭ କରିବା", "aasa kama arambha kariba"],
                ["Let us go to the temple", "ଆସ ମନ୍ଦିରକୁ ଯିବା", "aasa mandiraku jiba"],
                ["Let us sing a song", "ଆସ ଏକ ଗୀତ ଗାଇବା", "aasa eka gita gaiba"],
                ["Let us help them", "ଆସ ସେମାନଙ୍କୁ ସାହାଯ୍ୟ କରିବା", "aasa semanunku sahajya kariba"],
                ["Let us cook together", "ଆସ ଏକାଠି ରାନ୍ଧିବା", "aasa ekathi randhiba"],
                ["Let us think about this", "ଆସ ଏହା ବିଷୟରେ ଚିନ୍ତା କରିବା", "aasa eha bishayare chinta kariba"],
                ["Let us clean the house", "ଆସ ଘର ସଫା କରିବା", "aasa ghara sapha kariba"],
                ["Let us rest now", "ଆସ ଏବେ ବିଶ୍ରାମ ନେବା", "aasa ebe bishrama neba"],
                ["Let us walk in the garden", "ଆସ ବଗିଚାରେ ବୁଲିବା", "aasa bagichare buliba"],
                ["Let us wait here", "ଆସ ଏଠି ଅପେକ୍ଷା କରିବା", "aasa ethi apeksha kariba"],
                ["Let us try again", "ଆସ ପୁଣି ଚେଷ୍ଟା କରିବା", "aasa puni cheshta kariba"],
                ["Let us celebrate", "ଆସ ପାଳନ କରିବା", "aasa palana kariba"]
            ]
        }
    ]
}

# 555: "Should I...?" patterns
LESSONS[555] = {
    "url": "\"Should I...?\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Should I come?", "ମୁଁ ଆସିବି କି?", "mun asibi ki?"],
                ["Should I wait?", "ମୁଁ ଅପେକ୍ଷା କରିବି କି?", "mun apeksha karibi ki?"],
                ["Should I call him?", "ମୁଁ ତାଙ୍କୁ ଡାକିବି କି?", "mun tanku dakibi ki?"],
                ["Should I close the door?", "ମୁଁ କବାଟ ବନ୍ଦ କରିବି କି?", "mun kabata banda karibi ki?"],
                ["Should I cook rice?", "ମୁଁ ଭାତ ରାନ୍ଧିବି କି?", "mun bhata randhihi ki?"],
                ["Should I go now?", "ମୁଁ ଏବେ ଯିବି କି?", "mun ebe jibi ki?"],
                ["Should I bring water?", "ମୁଁ ପାଣି ଆଣିବି କି?", "mun pani anibi ki?"],
                ["Should I buy this?", "ମୁଁ ଏହା କିଣିବି କି?", "mun eha kinibi ki?"],
                ["Should I speak in Odia?", "ମୁଁ ଓଡ଼ିଆରେ କହିବି କି?", "mun odiare kahibi ki?"],
                ["Should I sit here?", "ମୁଁ ଏଠି ବସିବି କି?", "mun ethi basibi ki?"],
                ["Should I write a letter?", "ମୁଁ ଚିଠି ଲେଖିବି କି?", "mun chithi lekhibi ki?"],
                ["Should I take a taxi?", "ମୁଁ ଟ୍ୟାକ୍ସି ନେବି କି?", "mun taxi nebi ki?"],
                ["Should I open the window?", "ମୁଁ ଝରକା ଖୋଲିବି କି?", "mun jharaka kholibi ki?"],
                ["Should I tell the truth?", "ମୁଁ ସତ କହିବି କି?", "mun sata kahibi ki?"],
                ["Should I help them?", "ମୁଁ ସେମାନଙ୍କୁ ସାହାଯ୍ୟ କରିବି କି?", "mun semanunku sahajya karibi ki?"],
                ["Should I start now?", "ମୁଁ ଏବେ ଆରମ୍ଭ କରିବି କି?", "mun ebe arambha karibi ki?"],
                ["Should I read this book?", "ମୁଁ ଏହି ବହି ପଢ଼ିବି କି?", "mun ehi bahi padhibi ki?"],
                ["Should I wash the clothes?", "ମୁଁ ଲୁଗା ଧୋଇବି କି?", "mun luga dhoibi ki?"]
            ]
        }
    ]
}

# 556: "What time...?" patterns
LESSONS[556] = {
    "url": "\"What time...?\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["What time is it?", "ବର୍ତ୍ତମାନ କେତେ ବେଳ?", "bartamana kete bela?"],
                ["What time does the train come?", "ଗାଡ଼ି କେତେ ବେଳେ ଆସେ?", "gadi kete bele aase?"],
                ["What time do you wake up?", "ତୁମେ କେତେ ବେଳେ ଉଠ?", "tume kete bele utha?"],
                ["What time does school start?", "ସ୍କୁଲ କେତେ ବେଳେ ଆରମ୍ଭ ହୁଏ?", "school kete bele arambha hue?"],
                ["What time will you come?", "ତୁମେ କେତେ ବେଳେ ଆସିବ?", "tume kete bele asiba?"],
                ["What time does the shop open?", "ଦୋକାନ କେତେ ବେଳେ ଖୋଲେ?", "dokana kete bele khole?"],
                ["What time do you eat lunch?", "ତୁମେ କେତେ ବେଳେ ଦିନର ଖାଦ୍ୟ ଖାଅ?", "tume kete bele dinara khadya khaa?"],
                ["What time does the bus leave?", "ବସ କେତେ ବେଳେ ଯାଏ?", "bus kete bele jae?"],
                ["What time will the movie start?", "ସିନେମା କେତେ ବେଳେ ଆରମ୍ଭ ହେବ?", "cinema kete bele arambha heba?"],
                ["What time did he arrive?", "ସେ କେତେ ବେଳେ ପହଞ୍ଚିଲା?", "se kete bele pahanchila?"],
                ["What time do you sleep?", "ତୁମେ କେତେ ବେଳେ ଶୋଅ?", "tume kete bele shoa?"],
                ["What time does the office close?", "ଅଫିସ କେତେ ବେଳେ ବନ୍ଦ ହୁଏ?", "office kete bele banda hue?"],
                ["What time should I come?", "ମୁଁ କେତେ ବେଳେ ଆସିବି?", "mun kete bele asibi?"],
                ["What time does the market open?", "ବଜାର କେତେ ବେଳେ ଖୋଲେ?", "bajara kete bele khole?"],
                ["What time is breakfast?", "ସକାଳ ଜଳଖିଆ କେତେ ବେଳେ?", "sakala jalakhia kete bele?"],
                ["What time does the flight depart?", "ବିମାନ କେତେ ବେଳେ ଯିବ?", "bimana kete bele jiba?"],
                ["What time did the rain start?", "ବର୍ଷା କେତେ ବେଳେ ଆରମ୍ଭ ହେଲା?", "barsha kete bele arambha hela?"],
                ["What time is dinner?", "ରାତି ଖାଣା କେତେ ବେଳେ?", "rati khana kete bele?"]
            ]
        }
    ]
}

# 557: "Why...?" patterns
LESSONS[557] = {
    "url": "\"Why...?\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Why are you late?", "ତୁମେ ଡେରି କାହିଁକି?", "tume deri kahinki?"],
                ["Why did you go?", "ତୁମେ କାହିଁକି ଗଲ?", "tume kahinki gala?"],
                ["Why is he crying?", "ସେ କାହିଁକି କାନ୍ଦୁଛି?", "se kahinki kanduchhi?"],
                ["Why are you angry?", "ତୁମେ କାହିଁକି ରାଗ କରୁଛ?", "tume kahinki raga karuchha?"],
                ["Why did you not come?", "ତୁମେ କାହିଁକି ଆସିଲ ନାହିଁ?", "tume kahinki asila nahin?"],
                ["Why is the shop closed?", "ଦୋକାନ କାହିଁକି ବନ୍ଦ?", "dokana kahinki banda?"],
                ["Why are you sad?", "ତୁମେ କାହିଁକି ଦୁଃଖିତ?", "tume kahinki duhkhita?"],
                ["Why is the water dirty?", "ପାଣି କାହିଁକି ମଇଳା?", "pani kahinki maila?"],
                ["Why did he leave?", "ସେ କାହିଁକି ଚାଲିଗଲା?", "se kahinki chaligala?"],
                ["Why are you laughing?", "ତୁମେ କାହିଁକି ହସୁଛ?", "tume kahinki hasuchha?"],
                ["Why is this so expensive?", "ଏହା କାହିଁକି ଏତେ ମହଙ୍ଗା?", "eha kahinki ete mahanga?"],
                ["Why did the train stop?", "ଗାଡ଼ି କାହିଁକି ଅଟକି ଗଲା?", "gadi kahinki ataki gala?"],
                ["Why are you not eating?", "ତୁମେ କାହିଁକି ଖାଉ ନାହିଁ?", "tume kahinki khau nahin?"],
                ["Why did you change your mind?", "ତୁମେ ମନ କାହିଁକି ବଦଳାଇଲ?", "tume mana kahinki badalaila?"],
                ["Why is it raining?", "ବର୍ଷା କାହିଁକି ହେଉଛି?", "barsha kahinki heuchhi?"],
                ["Why do you work so hard?", "ତୁମେ ଏତେ କଷ୍ଟ କାହିଁକି କର?", "tume ete kashta kahinki kara?"],
                ["Why didn't you tell me?", "ତୁମେ ମୋତେ କାହିଁକି କହିଲ ନାହିଁ?", "tume mote kahinki kahila nahin?"],
                ["Why is the road so bad?", "ରାସ୍ତା କାହିଁକି ଏତେ ଖରାପ?", "rasta kahinki ete kharapa?"]
            ]
        }
    ]
}

# 558: "Who...?" patterns
LESSONS[558] = {
    "url": "\"Who...?\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["Who are you?", "ତୁମେ କିଏ?", "tume kie?"],
                ["Who is he?", "ସେ କିଏ?", "se kie?"],
                ["Who came?", "କିଏ ଆସିଲା?", "kie asila?"],
                ["Who told you?", "ତୁମକୁ କିଏ କହିଲା?", "tumaku kie kahila?"],
                ["Who is at the door?", "କବାଟରେ କିଏ?", "kabatare kie?"],
                ["Who is your teacher?", "ତୁମ ଶିକ୍ଷକ କିଏ?", "tuma shikshaka kie?"],
                ["Who made this?", "ଏହା କିଏ ତିଆରି କଲା?", "eha kie tiari kala?"],
                ["Who is cooking?", "କିଏ ରାନ୍ଧୁଛି?", "kie randhuchhi?"],
                ["Who is calling?", "କିଏ ଡାକୁଛି?", "kie dakuchhi?"],
                ["Who will go?", "କିଏ ଯିବ?", "kie jiba?"],
                ["Who did this work?", "ଏ କାମ କିଏ କଲା?", "e kama kie kala?"],
                ["Who is your friend?", "ତୁମ ବନ୍ଧୁ କିଏ?", "tuma bandhu kie?"],
                ["Who lives here?", "ଏଠି କିଏ ରହେ?", "ethi kie rahe?"],
                ["Who wrote this book?", "ଏ ବହି କିଏ ଲେଖିଲା?", "e bahi kie lekhila?"],
                ["Who is the doctor?", "ଡାକ୍ତର କିଏ?", "daktar kie?"],
                ["Who broke the glass?", "ଗ୍ଲାସ କିଏ ଭାଙ୍ଗିଲା?", "glass kie bhangila?"],
                ["Who will drive?", "କିଏ ଗାଡ଼ି ଚଳାଇବ?", "kie gadi chalaiba?"],
                ["Who is singing?", "କିଏ ଗୀତ ଗାଉଛି?", "kie gita gauchhi?"]
            ]
        }
    ]
}

# 559: "When...?" patterns
LESSONS[559] = {
    "url": "\"When...?\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["When will you come?", "ତୁମେ କେବେ ଆସିବ?", "tume kebe asiba?"],
                ["When did he go?", "ସେ କେବେ ଗଲା?", "se kebe gala?"],
                ["When is the festival?", "ପର୍ବ କେବେ?", "parba kebe?"],
                ["When does school start?", "ସ୍କୁଲ କେବେ ଆରମ୍ଭ ହୁଏ?", "school kebe arambha hue?"],
                ["When will the rain stop?", "ବର୍ଷା କେବେ ବନ୍ଦ ହେବ?", "barsha kebe banda heba?"],
                ["When did you arrive?", "ତୁମେ କେବେ ପହଞ୍ଚିଲ?", "tume kebe pahanchila?"],
                ["When will you return?", "ତୁମେ କେବେ ଫେରିବ?", "tume kebe pheriba?"],
                ["When is the wedding?", "ବିବାହ କେବେ?", "bibaha kebe?"],
                ["When did you eat?", "ତୁମେ କେବେ ଖାଇଲ?", "tume kebe khaila?"],
                ["When will the doctor come?", "ଡାକ୍ତର କେବେ ଆସିବେ?", "daktar kebe asibe?"],
                ["When did this happen?", "ଏହା କେବେ ଘଟିଲା?", "eha kebe ghatila?"],
                ["When is your birthday?", "ତୁମ ଜନ୍ମଦିନ କେବେ?", "tuma janmadina kebe?"],
                ["When will the bus arrive?", "ବସ କେବେ ଆସିବ?", "bus kebe asiba?"],
                ["When did you learn Odia?", "ତୁମେ ଓଡ଼ିଆ କେବେ ଶିଖିଲ?", "tume odia kebe shikhila?"],
                ["When will you finish?", "ତୁମେ କେବେ ସାରିବ?", "tume kebe sariba?"],
                ["When is the exam?", "ପରୀକ୍ଷା କେବେ?", "pariksha kebe?"],
                ["When did the shop open?", "ଦୋକାନ କେବେ ଖୋଲିଲା?", "dokana kebe kholila?"],
                ["When should I come?", "ମୁଁ କେବେ ଆସିବି?", "mun kebe asibi?"]
            ]
        }
    ]
}

# 560: "How to...?" patterns
LESSONS[560] = {
    "url": "\"How to...?\" patterns in Odia",
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Odia", "Transliteration"],
            "rows": [
                ["How to say this in Odia?", "ଏହା ଓଡ଼ିଆରେ କିପରି କହିବ?", "eha odiare kipari kahiba?"],
                ["How to cook rice?", "ଭାତ କିପରି ରାନ୍ଧିବ?", "bhata kipari randhiba?"],
                ["How to go to Puri?", "ପୁରୀ କିପରି ଯିବ?", "Puri kipari jiba?"],
                ["How to learn Odia?", "ଓଡ଼ିଆ କିପରି ଶିଖିବ?", "odia kipari shikhiba?"],
                ["How to write a letter?", "ଚିଠି କିପରି ଲେଖିବ?", "chithi kipari lekhiba?"],
                ["How to use this phone?", "ଏହି ଫୋନ କିପରି ବ୍ୟବହାର କରିବ?", "ehi phone kipari byabahara kariba?"],
                ["How to open this door?", "ଏହି କବାଟ କିପରି ଖୋଲିବ?", "ehi kabata kipari kholiba?"],
                ["How to make tea?", "ଚା କିପରି ତିଆରି କରିବ?", "cha kipari tiari kariba?"],
                ["How to reach the station?", "ଷ୍ଟେସନ କିପରି ପହଞ୍ଚିବ?", "station kipari pahanchiba?"],
                ["How to book a ticket?", "ଟିକେଟ କିପରି କାଟିବ?", "ticket kipari katiba?"],
                ["How to swim?", "ପହଁରିବା କିପରି ଶିଖିବ?", "pahanriba kipari shikhiba?"],
                ["How to drive a car?", "ଗାଡ଼ି କିପରି ଚଳାଇବ?", "gadi kipari chalaiba?"],
                ["How to count in Odia?", "ଓଡ଼ିଆରେ କିପରି ଗଣିବ?", "odiare kipari ganiba?"],
                ["How to wash clothes?", "ଲୁଗା କିପରି ଧୋଇବ?", "luga kipari dhoiba?"],
                ["How to ask for directions?", "ରାସ୍ତା କିପରି ପଚାରିବ?", "rasta kipari pachariba?"],
                ["How to plant a tree?", "ଗଛ କିପରି ଲଗାଇବ?", "gachha kipari lagaiba?"],
                ["How to send a message?", "ସନ୍ଦେଶ କିପରି ପଠାଇବ?", "sandesha kipari pathaiba?"],
                ["How to introduce yourself?", "ନିଜ ପରିଚୟ କିପରି ଦେବ?", "nija parichaya kipari deba?"]
            ]
        }
    ]
}

# Apply lessons to the data
id_map = {item['id']: item for item in d}
updated = 0

for lid, content in LESSONS.items():
    if lid in id_map:
        id_map[lid]['url'] = content['url']
        id_map[lid]['blocks'] = content['blocks']
        updated += 1
        row_count = len(content['blocks'][0]['rows'])
        print(f"  Updated ID {lid}: {content['url']} ({row_count} rows)")
    else:
        d.append({"id": lid, "url": content['url'], "blocks": content['blocks']})
        updated += 1
        row_count = len(content['blocks'][0]['rows'])
        print(f"  Added ID {lid}: {content['url']} ({row_count} rows)")

with open('data_odia.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"\nDone! Updated {updated} lessons (IDs 543-560) in data_odia.json")
print(f"Total entries in data_odia.json: {len(d)}")
