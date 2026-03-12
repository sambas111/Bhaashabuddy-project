#!/usr/bin/env python3
"""Add Telugu vocabulary and conversation practice chapters to data_telugu.json"""
import json

# New chapters 798-850 (some replace existing, most are new)
NEW_CHAPTERS = [
    # 798 - List of Body parts (replace current 798)
    {"id": 798, "title": "List of Body parts in Telugu", "url": "#", "content": "Body parts vocabulary in Telugu.", "intro": "Learn body part names with example sentences.",
     "tables": [{"heading": "Body Parts", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["head", "తల", "tala"], ["eye", "కన్ను", "kannu"], ["ear", "చెవి", "cevi"], ["nose", "ముక్కు", "mukku"],
                         ["mouth", "నోరు", "nōru"], ["hand", "చెయ్యి", "ceyyi"], ["leg", "కాలు", "kālu"], ["heart", "గుండె", "guṇḍe"],
                         ["stomach", "కడుపు", "kaḍupu"], ["finger", "వేలు", "vēlu"], ["tongue", "నాలుక", "nāluka"], ["teeth", "పంటలు", "paṇṭalu"]]},
               {"heading": "Example sentences", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["My head is hurting.", "నా తల నొప్పిగా ఉంది.", "nā tala noppigā undi."],
                         ["Wash your hands.", "చేతులు కడుక్కోండి.", "cētulu kaḍukkōṇḍi."]]}]},
    # 799 - Greetings & Basics
    {"id": 799, "title": "Greetings & Basics in Telugu", "url": "#", "content": "Greetings and basic phrases.", "intro": "Essential greetings for everyday conversation.",
     "tables": [{"heading": "Greetings", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["Hello / Namaste", "నమస్తే", "namastē"], ["Good morning", "శుభోదయం", "śubhōdayaṃ"], ["Thank you", "ధన్యవాదాలు", "dhanyavādālu"],
                         ["Please", "దయచేసి", "dayacēsi"], ["Yes", "అవును", "avunu"], ["No", "కాదు", "kādu"], ["Welcome", "స్వాగతం", "svāgataṃ"], ["Good bye", "వీడ్కోలు", "vīḍkōlu"]]},
               {"heading": "Example sentences", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["Hello, how are you?", "నమస్తే, ఎలా ఉన్నారు?", "namastē, elā unnāru?"],
                         ["I am fine, thank you.", "నేను బాగున్నాను, ధన్యవాదాలు.", "nēnu bāgunnānu, dhanyavādālu."]]}]},
    # 800 - Frequently used words
    {"id": 800, "title": "Frequently used words – Miscellaneous in Telugu", "url": "#", "content": "Common everyday words.", "intro": "Useful words for daily use.",
     "tables": [{"heading": "Common words", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["thing", "వస్తువు", "vastuvu"], ["place", "చోటు", "cōṭu"], ["way", "దారి", "dāri"], ["time", "సమయం", "samayaṃ"],
                         ["day", "రోజు", "rōju"], ["work", "పని", "pani"], ["water", "నీరు", "nīru"], ["food", "ఆహారం", "āhāraṃ"],
                         ["house", "ఇల్లు", "illu"], ["money", "డబ్బు", "ḍabbu"], ["help", "సహాయం", "sahāyaṃ"], ["name", "పేరు", "pēru"]]}]},
    # 801 - Relations
    {"id": 801, "title": "Relations in Telugu", "url": "#", "content": "Family and kinship terms.", "intro": "Words for family relationships.",
     "tables": [{"heading": "Relations", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["father", "నాన్న", "nānna"], ["mother", "అమ్మ", "amma"], ["elder brother", "అన్నయ్య", "annayya"], ["younger brother", "తమ్ముడు", "tammuḍu"],
                         ["elder sister", "అక్క", "akka"], ["younger sister", "చెల్లి", "celli"], ["husband", "భర్త", "bharta"], ["wife", "భార్య", "bhārya"],
                         ["son", "కొడుకు", "koḍuku"], ["daughter", "కూతురు", "kūturu"], ["grandfather", "తాతయ్య", "tātayya"], ["grandmother", "అమ్మమ్మ", "ammamma"]]}]},
    # 802 - Numbers Part 1
    {"id": 802, "title": "Numbers in Telugu – Part 1", "url": "#", "content": "Numbers 0-100.", "intro": "Learn to count in Telugu.",
     "tables": [{"heading": "Numbers 0-20", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["zero", "సున్నా", "sunnā"], ["one", "ఒక్కటి", "okkaṭi"], ["two", "రెండు", "reṇḍu"], ["three", "మూడు", "mūḍu"],
                         ["four", "నాలుగు", "nālugu"], ["five", "ఐదు", "aidu"], ["six", "ఆరు", "āru"], ["seven", "ఏడు", "ēḍu"],
                         ["eight", "ఎనిమిది", "enimidi"], ["nine", "తొమ్మిది", "tommidi"], ["ten", "పది", "padi"], ["twenty", "ఇరవై", "iravai"]]}]},
    # 803 - Numbers Part 2
    {"id": 803, "title": "Numbers in Telugu – Part 2", "url": "#", "content": "Numbers 30-1000.", "intro": "Continue learning numbers.",
     "tables": [{"heading": "Numbers 30-1000", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["thirty", "ముప్పై", "muppai"], ["forty", "నలభై", "nalabhai"], ["fifty", "యాబై", "yābai"], ["sixty", "అరవై", "aravai"],
                         ["seventy", "డెబ్బై", "debbai"], ["eighty", "ఎనభై", "enabhai"], ["ninety", "తొంభై", "tombhai"], ["hundred", "వంద", "vanda"],
                         ["thousand", "వెయ్యి", "veyyi"], ["lakh", "లక్ష", "lakṣa"]]}]},
    # 804 - Fractional numbers
    {"id": 804, "title": "Fractional numbers, sequence, percentage in Telugu", "url": "#", "content": "Fractions and percentages.", "intro": "Learn fractions and sequences.",
     "tables": [{"heading": "Fractions & more", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["half", "సగం", "sagaṃ"], ["quarter", "క్వార్టర్", "kvārṭar"], ["first", "మొదటి", "modaṭi"], ["second", "రెండవ", "reṇḍava"],
                         ["third", "మూడవ", "mūḍava"], ["percent", "శాతం", "śātaṃ"], ["double", "రెట్టింపు", "reṭṭiṃpu"]]}]},
    # 805 - Verbs Part 1
    {"id": 805, "title": "Frequently used verbs in Telugu – Part 1", "url": "#", "content": "Common verbs.", "intro": "Essential verbs for daily use.",
     "tables": [{"heading": "Verbs", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["to be", "ఉండు", "uṇḍu"], ["to have", "కలిగి ఉండు", "kaligi uṇḍu"], ["to do", "చేయు", "cēyu"], ["to say", "చెప్పు", "ceppu"],
                         ["to go", "వెళ్ళు", "veḷḷu"], ["to come", "రా", "rā"], ["to see", "చూచు", "cūcu"], ["to know", "తెలుసు", "telusu"]]}]},
    # 806 - Verbs Part 2
    {"id": 806, "title": "Frequently used verbs in Telugu – Part 2", "url": "#", "content": "More common verbs.", "intro": "Continue learning verbs.",
     "tables": [{"heading": "Verbs", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["to get", "పొందు", "poṇdu"], ["to make", "చేయు", "cēyu"], ["to think", "ఆలోచించు", "ālōcin̄cu"], ["to take", "తీసుకొను", "tīsukonu"],
                         ["to tell", "చెప్పు", "ceppu"], ["to ask", "అడుగు", "aḍugu"], ["to find", "కనుగొను", "kanugonu"], ["to feel", "అనుభవించు", "anubhavin̄cu"]]}]},
    # 807 - Verbs Part 3
    {"id": 807, "title": "Frequently used verbs in Telugu – Part 3", "url": "#", "content": "Action verbs.", "intro": "More action verbs.",
     "tables": [{"heading": "Verbs", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["to eat", "తిను", "tinu"], ["to drink", "త్రాగు", "trāgu"], ["to sleep", "నిద్రపోవు", "nidrapōvu"], ["to read", "చదువు", "caduvu"],
                         ["to write", "రాయు", "rāyu"], ["to buy", "కొను", "konu"], ["to sell", "అమ్ము", "ammu"], ["to give", "ఇచ్చు", "iccu"]]}]},
    # 808 - Verbs Part 4
    {"id": 808, "title": "Frequently used verbs in Telugu – Part 4", "url": "#", "content": "More verbs.", "intro": "Additional useful verbs.",
     "tables": [{"heading": "Verbs", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["to open", "తెరుచు", "terucu"], ["to close", "మూయు", "mūyu"], ["to sit", "కూర్చొను", "kūrconu"], ["to stand", "నిలబడు", "nilabaḍu"],
                         ["to run", "పరుగెత్తు", "parugettu"], ["to walk", "నడుచు", "naḍucu"], ["to speak", "మాట్లాడు", "māṭlāḍu"], ["to listen", "విను", "vinu"]]}]},
    # 809 - పెట్టడం verb
    {"id": 809, "title": "పెట్టడం (peṭṭaḍaṃ) – one verb, multiple meanings in Telugu", "url": "#", "content": "Verb పెట్టడం has many uses.", "intro": "Learn the various meanings of పెట్టడం.",
     "tables": [{"heading": "Uses of పెట్టడం", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["to put/place", "పెట్టు", "peṭṭu"], ["to wear (ornaments)", "పెట్టుకొను", "peṭṭukonu"], ["to apply (cream)", "పెట్టు", "peṭṭu"],
                         ["to switch on", "పెట్టు", "peṭṭu"], ["to start", "పెట్టు", "peṭṭu"], ["to bet", "పెట్టు", "peṭṭu"]]}]},
    # 810 - చేయడం verb
    {"id": 810, "title": "చేయడం (cēyaḍaṃ) – one verb, multiple meanings in Telugu", "url": "#", "content": "Verb చేయడం has many uses.", "intro": "Learn the various meanings of చేయడం.",
     "tables": [{"heading": "Uses of చేయడం", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["to do", "చేయు", "cēyu"], ["to make", "చేయు", "cēyu"], ["to cook", "వంట చేయు", "vaṇṭa cēyu"], ["to work", "పని చేయు", "pani cēyu"],
                         ["to help", "సహాయం చేయు", "sahāyaṃ cēyu"], ["to try", "ప్రయత్నం చేయు", "prayatnaṃ cēyu"]]}]},
    # 811 - Adjectives
    {"id": 811, "title": "List of Telugu Adjectives – Part 1", "url": "#", "content": "Common adjectives.", "intro": "Descriptive words in Telugu.",
     "tables": [{"heading": "Adjectives", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["good", "మంచి", "maṃci"], ["bad", "చెడ్డ", "ceḍḍa"], ["big", "పెద్ద", "pedda"], ["small", "చిన్న", "cinna"],
                         ["long", "పొడవైన", "poḍavaina"], ["short", "చిన్న", "cinna"], ["hot", "వేడి", "vēḍi"], ["cold", "చలి", "cali"],
                         ["beautiful", "అందమైన", "andaṃaina"], ["new", "కొత్త", "kotta"], ["old", "పాత", "pāta"]]}]},
    # 812 - Adverbs Part 1
    {"id": 812, "title": "Adverbs in Telugu – Part 1", "url": "#", "content": "Adverbs of time and place.", "intro": "Words that describe when and where.",
     "tables": [{"heading": "Adverbs", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["today", "ఈ రోజు", "ī rōju"], ["tomorrow", "రేపు", "rēpu"], ["yesterday", "నిన్న", "ninna"], ["now", "ఇప్పుడు", "ippuḍu"],
                         ["here", "ఇక్కడ", "ikkaḍa"], ["there", "అక్కడ", "akkaḍa"], ["always", "ఎప్పుడూ", "eppuḍū"], ["never", "ఎప్పుడూ కాదు", "eppuḍū kādu"],
                         ["often", "తరచుగా", "taracugā"], ["slowly", "నెమ్మదిగా", "nemmadigā"], ["fast", "వేగంగా", "vēgaṃgā"]]}]},
    # 813 - List of adverbs
    {"id": 813, "title": "List of adverbs in Telugu", "url": "#", "content": "More adverbs.", "intro": "Additional adverbs.",
     "tables": [{"heading": "Adverbs", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["very", "చాలా", "cālā"], ["much", "ఎక్కువ", "ekkuva"], ["little", "కొంచెం", "koncaṃ"], ["enough", "సరిపోతుంది", "saripōtundi"],
                         ["also", "కూడా", "kūḍā"], ["only", "మాత్రమే", "mātramē"], ["even", "కూడా", "kūḍā"], ["still", "ఇంకా", "iṃkā"]]}]},
    # 814 - Vegetables
    {"id": 814, "title": "List of vegetable names in Telugu", "url": "#", "content": "Vegetable names in Telugu.", "intro": "Common vegetables.",
     "tables": [{"heading": "Vegetables", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["tomato", "టమాటా", "ṭamāṭā"], ["potato", "బంగాళాదుంప", "baṃgāḷāduṃpa"], ["onion", "ఉల్లిపాయ", "ullipāya"], ["brinjal", "వంకాయ", "vaṃkāya"],
                         ["lady's finger", "బెండకాయ", "beṇḍakāya"], ["cucumber", "దోసకాయ", "dōsakāya"], ["carrot", "కారెట్", "kāreṭ"], ["beans", "బీన్స్", "bīns"],
                         ["pumpkin", "గుమ్మడికాయ", "gummaḍikāya"], ["bitter gourd", "కాకరకాయ", "kākarakāya"], ["chilli", "మిరపకాయ", "mirapakāya"], ["spinach", "పాలకూర", "pālakūra"]]}]},
    # 815 - Fruits
    {"id": 815, "title": "List of names of fruits in Telugu", "url": "#", "content": "Fruit names in Telugu.", "intro": "Common fruits.",
     "tables": [{"heading": "Fruits", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["mango", "మామిడిపండు", "māmiḍipaṇḍu"], ["banana", "అరటిపండు", "araṭipaṇḍu"], ["apple", "ఆపిల్", "āpil"], ["orange", "కమలపండు", "kamalapaṇḍu"],
                         ["grapes", "ద్రాక్ష", "drākṣa"], ["papaya", "బొప్పాయ", "boppāya"], ["guava", "జామ", "jāma"], ["watermelon", "పుచ్చకాయ", "puccakāya"],
                         ["pomegranate", "దానిమ్మ", "dānimma"], ["lemon", "నిమ్మకాయ", "nimmakāya"], ["coconut", "కొబ్బరి", "kobbari"]]}]},
    # 816 - Birds
    {"id": 816, "title": "List of names of birds in Telugu", "url": "#", "content": "Bird names in Telugu.", "intro": "Common birds.",
     "tables": [{"heading": "Birds", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["parrot", "చిలక", "cilaka"], ["crow", "కాకి", "kāki"], ["peacock", "నెమలి", "nemali"], ["pigeon", "పావురం", "pāvuraṃ"],
                         ["hen", "కోడి", "kōḍi"], ["duck", "బాతు", "bātu"], ["eagle", "గద్ద", "gadda"], ["owl", "గుడ్లగూబ", "guḍlagūba"],
                         ["sparrow", "పిచ్చుక", "piccuka"]]}]},
    # 817 - Insects
    {"id": 817, "title": "List of names of insects in Telugu", "url": "#", "content": "Insect names in Telugu.", "intro": "Common insects.",
     "tables": [{"heading": "Insects", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["ant", "చీమ", "cīma"], ["bee", "తేనెటీగ", "tēneṭīga"], ["mosquito", "దోమ", "dōma"], ["butterfly", "సీతాకోకచిలక", "sītākōkacilaka"],
                         ["housefly", "ఈగ", "īga"], ["spider", "సాలెపీడ", "sālepīḍa"], ["cockroach", "బొద్దింక", "boddin̄ka"]]}]},
    # 818 - Colours
    {"id": 818, "title": "List of names of colours in Telugu", "url": "#", "content": "Colour names in Telugu.", "intro": "Common colours.",
     "tables": [{"heading": "Colours", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["red", "ఎర్ర", "erra"], ["blue", "నీలం", "nīlaṃ"], ["green", "పచ్చ", "pacca"], ["yellow", "పసుపు", "pasupu"],
                         ["white", "తెలుపు", "telupu"], ["black", "నలుపు", "nalupu"], ["orange", "నారింజ", "nārin̄ja"], ["pink", "గులాబీ", "gulābī"],
                         ["brown", "పింగలం", "piṃgalaṃ"]]}]},
    # 819 - Flowers
    {"id": 819, "title": "List of names of flowers in Telugu", "url": "#", "content": "Flower names in Telugu.", "intro": "Common flowers.",
     "tables": [{"heading": "Flowers", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["rose", "గులాబీ", "gulābī"], ["jasmine", "మల్లె", "malle"], ["hibiscus", "మందారం", "maṃdāraṃ"], ["lotus", "పద్మం", "padmaṃ"],
                         ["marigold", "బంతిపువ్వు", "baṃtipuvvu"], ["sunflower", "పొద్దుతిరుగుడు", "poddutiruguḍu"], ["chrysanthemum", "చామంతి", "cāmaṃti"]]}]},
    # 820 - Animals
    {"id": 820, "title": "List of names of animals in Telugu", "url": "#", "content": "Animal names in Telugu.", "intro": "Common animals.",
     "tables": [{"heading": "Animals", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["dog", "కుక్క", "kukka"], ["cat", "పిల్లి", "pilli"], ["cow", "ఆవు", "āvu"], ["goat", "మేక", "mēka"],
                         ["horse", "గుర్రం", "gurraṃ"], ["elephant", "ఏనుగు", "ēnugu"], ["tiger", "పులి", "puli"], ["lion", "సింహం", "siṃhaṃ"],
                         ["monkey", "కోతి", "kōti"], ["snake", "పాము", "pāmu"], ["rabbit", "కుందేలు", "kuṃdēlu"]]}]},
    # 821 - Food & Drink
    {"id": 821, "title": "Food & Drink in Telugu", "url": "#", "content": "Food and drink vocabulary.", "intro": "Essential food vocabulary.",
     "tables": [{"heading": "Food & Drink", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["rice", "బియ్యం", "biyyaṃ"], ["bread", "రొట్టె", "roṭṭe"], ["milk", "పాలు", "pālu"], ["water", "నీరు", "nīru"],
                         ["tea", "టీ", "ṭī"], ["coffee", "కాఫీ", "kāphī"], ["salt", "ఉప్పు", "uppu"], ["sugar", "చక్కెర", "cakkera"],
                         ["eat", "తిను", "tinu"], ["drink", "త్రాగు", "trāgu"]]},
               {"heading": "Example sentences", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["I eat rice every day.", "నేను ప్రతి రోజు బియ్యం తింటాను.", "nēnu prati rōju biyyam tiṇṭānu."],
                         ["Do you drink tea?", "మీరు టీ తాగుతారా?", "mīru ṭī tāgutārā?"]]}]},
    # 822 - Daily Life, Time, Transportation
    {"id": 822, "title": "Daily Life, Time, Transportation in Telugu", "url": "#", "content": "Combined vocabulary.", "intro": "Words for daily life, time and transport.",
     "tables": [{"heading": "Daily Life & Time", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["house", "ఇల్లు", "illu"], ["work", "పని", "pani"], ["today", "ఈ రోజు", "ī rōju"], ["tomorrow", "రేపు", "rēpu"],
                         ["Monday", "సోమవారం", "sōmavāraṃ"], ["hour", "గంట", "gaṇṭa"]]},
               {"heading": "Transportation", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["bus", "బస్సు", "bassu"], ["train", "రైలు", "railu"], ["car", "కారు", "kāru"], ["auto", "ఆటో", "āṭō"],
                         ["to go", "వెళ్ళు", "veḷḷu"], ["to come", "రా", "rā"]]}]},
    # 823 - Shopping, Travel, Emergency
    {"id": 823, "title": "Shopping, Travel, Emergency in Telugu", "url": "#", "content": "Shopping and emergency vocabulary.", "intro": "Useful for shopping and emergencies.",
     "tables": [{"heading": "Shopping & Travel", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["shop", "దుకాణం", "dukāṇaṃ"], ["price", "ధర", "dhara"], ["how much", "ఎంత", "eṃta"], ["hotel", "హోటల్", "hōṭal"],
                         ["ticket", "టికెట్", "ṭikeṭ"]]},
               {"heading": "Emergency", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["help", "సహాయం", "sahāyaṃ"], ["police", "పోలీసు", "pōlīsu"], ["doctor", "డాక్టర్", "ḍākṭar"],
                         ["I need help", "నాకు సహాయం కావాలి", "nāku sahāyaṃ kāvāli"]]}]},
    # 824 - Miscellaneous
    {"id": 824, "title": "Frequently used or common words in Telugu – Miscellaneous", "url": "#", "content": "Miscellaneous common words.", "intro": "More everyday words.",
     "tables": [{"heading": "Common words", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1,
                "rows": [["all", "అన్ని", "anni"], ["many", "చాలా", "cālā"], ["few", "కొన్ని", "konni"], ["some", "కొంత", "koṃta"],
                         ["other", "ఇతర", "itara"], ["same", "అదే", "adē"], ["different", "వేరే", "vērē"], ["right", "కుడి", "kuḍi"],
                         ["left", "ఎడమ", "eḍama"], ["near", "దగ్గర", "daggara"], ["far", "దూరం", "dūraṃ"]]}]},
]

# Conversation practice chapters 825-850
CONV_CHAPTERS = [
    (825, "Sankranti Festival in Telugu", "Sankranti (Makara Sankranti) is a major harvest festival in Telugu states.",
     [["Happy Sankranti!", "సంక్రాంతి శుభాకాంక్షలు!", "saṃkrāṃti śubhākāṃkṣalu!"], ["We fly kites on Sankranti.", "మేము సంక్రాంతి నాడు గాలిపటాలు ఎగురవేస్తాము.", "mēmu saṃkrāṃti nāḍu gālipaṭālu eguravēstāmu."], ["Eat pongal on Sankranti.", "సంక్రాంతి నాడు పొంగల్ తినండి.", "saṃkrāṃti nāḍu poṃgal tiṇaṇḍi."]]),
    (826, "Simple Sentences in Telugu – Introduction/Salutation", "Introduction and greeting sentences.",
     [["My name is Ravi.", "నా పేరు రవి.", "nā pēru ravi."], ["What is your name?", "మీ పేరు ఏమిటి?", "mī pēru ēmiṭi?"], ["Nice to meet you.", "మిమ్మల్ని కలవడం సంతోషం.", "mimmalni kalavaḍaṃ saṃtōṣaṃ."], ["I am from Hyderabad.", "నేను హైదరాబాద్ నుండి వచ్చాను.", "nēnu haidarābād nuṇḍi vaccānu."]]),
    (827, "Simple Telugu Sentences – Time Related", "Time-related sentences.",
     [["What time is it?", "ఇప్పుడు సమయం ఎంత?", "ippuḍu samayaṃ eṃta?"], ["It is five o'clock.", "ఐదు గంటలయింది.", "aidu gaṇṭalayindi."], ["I will come tomorrow.", "నేను రేపు వస్తాను.", "nēnu rēpu vastānu."], ["We meet every Sunday.", "మేము ప్రతి ఆదివారం కలుసుకుంటాము.", "mēmu prati ādivāraṃ kalusukuṃtāmu."]]),
    (828, "Simple Telugu Sentences – Where/Place Related", "Place and direction sentences.",
     [["Where is the hospital?", "ఆసుపత్రి ఎక్కడ ఉంది?", "āsupatri ekkaḍa uṇdi?"], ["It is near the temple.", "అది దేవాలయం దగ్గర ఉంది.", "adi dēvālayaṃ daggara uṇdi."], ["Go straight and turn left.", "నేరుగా వెళ్ళి ఎడమకు తిరగండి.", "nērugā veḷḷi eḍamaku tiragaṇḍi."]]),
    (829, "Simple Telugu Sentences – In Hotel", "Hotel and accommodation sentences.",
     [["I would like to book a room.", "నాకు ఒక గది బుక్ చేయాలని ఉంది.", "nāku oka gadi buk cēyālani uṇdi."], ["How much per night?", "ఒక రాత్రికి ఎంత?", "oka rātrike eṃta?"], ["Where is the bathroom?", "బాత్రూమ్ ఎక్కడ ఉంది?", "bātrūm ekkaḍa uṇdi?"]]),
    (830, "Simple Telugu sentences – Weather related", "Weather-related sentences.",
     [["Today it is very hot.", "ఈ రోజు చాలా వేడిగా ఉంది.", "ī rōju cālā vēḍigā uṇdi."], ["It is raining.", "వర్షం పడుతోంది.", "varṣaṃ paḍutōndi."], ["The weather is nice.", "వాతావరణం బాగుంది.", "vātāvaraṇaṃ bāguṇdi."]]),
    (831, "Telugu conversation – with traffic police", "Conversation with traffic police.",
     [["Sir, where did I go wrong?", "సార్, నేను ఎక్కడ తప్పు చేశాను?", "sār, nēnu ekkaḍa tappu cēśānu?"], ["Please show your license.", "దయచేసి మీ లైసెన్స్ చూపించండి.", "dayacēsi mī laisens cūpin̄caṇḍi."], ["I am sorry, I will be careful.", "క్షమించండి, జాగ్రత్తగా ఉంటాను.", "kṣamin̄caṇḍi, jāgrattagā uṃṭānu."]]),
    (832, "Simple Telugu conversation – Auto/Taxi driver", "Conversation with auto or taxi driver.",
     [["Take me to the railway station.", "నన్ను రైల్వే స్టేషన్ కి తీసుకెళ్ళండి.", "nannu railvē sṭēṣan ki tīsukeḷḷaṇḍi."], ["How much to the airport?", "విమానాశ్రయం కి ఎంత?", "vimānāśrayaṃ ki eṃta?"], ["Please use the meter.", "దయచేసి మీటర్ వాడండి.", "dayacēsi mīṭar vāḍaṇḍi."]]),
    (833, "Simple Telugu Conversation – Software Engineers", "Conversation between software engineers.",
     [["What project are you working on?", "మీరు ఏ ప్రాజెక్ట్ పై పని చేస్తున్నారు?", "mīru ē prājekṭ pai pani cēstunnāru?"], ["The deadline is next week.", "డెడ్‌లైన్ వచ్చే వారం.", "ḍed-lain vaccē vāraṃ."], ["Let us have a meeting tomorrow.", "రేపు మీటింగ్ చేద్దాం.", "rēpu mīṭiṅg cēddāṃ."]]),
    (834, "Simple Telugu conversation – Grocery shop", "Conversation at grocery shop.",
     [["Do you have rice?", "మీకు బియ్యం ఉందా?", "mīku biyyaṃ uṇdā?"], ["Give me two kilos of onions.", "నాకు రెండు కిలోల ఉల్లిపాయలు ఇవ్వండి.", "nāku reṇḍu kilōla ullipāyalu ivvaṇḍi."], ["How much is the total?", "మొత్తం ఎంత?", "mottaṃ eṃta?"]]),
    (835, "Simple Telugu Conversation – Doctor-Patient", "Doctor-patient conversation.",
     [["Doctor, I have fever.", "డాక్టర్ గారు, నాకు జ్వరం వచ్చింది.", "ḍākṭar gāru, nāku jvaraṃ vaccindi."], ["Since when?", "ఎప్పటి నుండి?", "eppaṭi nuṇḍi?"], ["Take this medicine twice a day.", "ఈ మందు రోజుకు రెండుసార్లు తీసుకోండి.", "ī maṇdu rōjuku reṇḍusārlu tīsukōṇḍi."]]),
    (836, "Simple Telugu Conversation – Teacher & Students", "Teacher and student conversation.",
     [["Students, open your books.", "విద్యార్థులారా, పుస్తకాలు తెరవండి.", "vidyārthulārā, pustakālu teravaṇḍi."], ["Do you understand?", "మీకు అర్థమైందా?", "mīku arthamaindā?"], ["Yes, teacher.", "అవును సార్.", "avunu sār."]]),
    (837, "Simple Telugu conversation – Informal phone conversation", "Informal phone conversation.",
     [["Hello, who is this?", "హలో, ఎవరు?", "halō, evaru?"], ["This is Suresh.", "ఇది సురేష్.", "idi surēṣ."], ["Can we meet tomorrow?", "రేపు కలుసుకోవచ్చా?", "rēpu kalusukōvaccā?"]]),
    (838, "Simple Telugu conversation – Vegetable Market", "Conversation at vegetable market.",
     [["How much for a kilo of tomatoes?", "టమాటా కిలో ఎంత?", "ṭamāṭā kilō eṃta?"], ["Twenty rupees.", "ఇరవై రూపాయలు.", "iravai rūpāyalu."], ["Give me fresh vegetables.", "తాజా కూరగాయలు ఇవ్వండి.", "tājā kūragāyalu ivvaṇḍi."]]),
    (839, "Simple Telugu Conversation – at bus stop and in bus", "Bus stop and bus conversation.",
     [["Does this bus go to Secunderabad?", "ఈ బస్సు సికింద్రాబాద్ కి వెళ్తుందా?", "ī bassu sikin̄drābād ki veḷtundā?"], ["Yes, get in.", "అవును, ఎక్కండి.", "avunu, ekkaṇḍi."], ["One ticket please.", "ఒక టికెట్ దయచేసి.", "oka ṭikeṭ dayacēsi."]]),
    (840, "Asking address in Telugu", "How to ask for address.",
     [["Where is MG Road?", "ఎంజీ రోడ్ ఎక్కడ ఉంది?", "eṃjī rōḍ ekkaḍa uṇdi?"], ["Can you tell me the way?", "దారి చెప్పగలరా?", "dāri ceppagalarā?"], ["It is near the park.", "అది పార్క్ దగ్గర ఉంది.", "adi pārk daggara uṇdi."]]),
    (841, "I Love you in Telugu – Proposing someone", "Expressing love in Telugu.",
     [["I love you.", "నేను నిన్ను ప్రేమిస్తున్నాను.", "nēnu ninnu prēmistunnānu."], ["Will you marry me?", "నన్ను వివాహం చేసుకుంటారా?", "nannu vivāhaṃ cēsukuṃtārā?"], ["You are very special to me.", "నాకు మీరు చాలా ప్రత్యేకం.", "nāku mīru cālā pratyēkaṃ."]]),
    (842, "Simple Telugu Conversation – Interview", "Job interview conversation.",
     [["Tell me about yourself.", "మీ గురించి చెప్పండి.", "mī gurin̄ci ceppaṇḍi."], ["What are your strengths?", "మీ బలాలు ఏమిటి?", "mī balālu ēmiṭi?"], ["When can you join?", "మీరు ఎప్పుడు జాయిన్ అవుతారు?", "mīru eppuḍu jāyin avutāru?"]]),
    (843, "Simple Telugu conversation – with housemaid", "Conversation with housemaid.",
     [["Please clean the house today.", "దయచేసి ఈ రోజు ఇల్లు శుభ్రం చేయండి.", "dayacēsi ī rōju illu śubhraṃ cēyaṇḍi."], ["When will you come?", "మీరు ఎప్పుడు వస్తారు?", "mīru eppuḍu vastāru?"], ["I will come at nine.", "నేను తొమ్మిది గంటలకు వస్తాను.", "nēnu tommidi gaṇṭlaku vastānu."]]),
    (844, "Simple Telugu conversation – In Bank", "Bank conversation.",
     [["I want to open an account.", "నాకు ఖాతా తెరవాలని ఉంది.", "nāku khātā teravālani uṇdi."], ["Please fill this form.", "దయచేసి ఈ ఫారం పూరించండి.", "dayacēsi ī phāraṃ pūrin̄caṇḍi."], ["What is the interest rate?", "వడ్డీ రేటు ఎంత?", "vaḍḍī rēṭu eṃta?"]]),
    (845, "Simple Telugu conversation – Enquiry about Temple Visit", "Temple visit enquiry.",
     [["What time does the temple open?", "దేవాలయం ఎప్పుడు తెరుస్తారు?", "dēvālayaṃ eppuḍu terustāru?"], ["Darshan is from 6 AM to 12 PM.", "దర్శనం ఉదయం 6 నుండి మధ్యాహ్నం 12 వరకు.", "darśanaṃ udayaṃ 6 nuṇḍi madhyāhnaṃ 12 varaku."]]),
    (846, "Simple Telugu conversation – with friend's parents at lunch table", "Lunch table conversation.",
     [["The food is delicious.", "ఆహారం చాలా రుచిగా ఉంది.", "āhāraṃ cālā rucigā uṇdi."], ["Please have some more.", "మరికొంత తీసుకోండి.", "marikoṃta tīsukōṇḍi."], ["Thank you for the meal.", "భోజనానికి ధన్యవాదాలు.", "bhōjanāniki dhanyavādālu."]]),
    (847, "Simple Telugu conversation – Friends talking about food and meal", "Friends discussing food.",
     [["What did you eat for lunch?", "మధ్యాహ్న భోజనానికి ఏమి తిన్నారు?", "madhyāhna bhōjanāniki ēmi tinnāru?"], ["I had biryani.", "నేను బిర్యాని తిన్నాను.", "nēnu biryāni tinnānu."], ["Let us go to a restaurant.", "రెస్టారెంట్ కి వెళ్దాం.", "resṭāreṇṭ ki veḷddāṃ."]]),
    (848, "Frequently used sentences in Telugu – miscellaneous", "Miscellaneous common sentences.",
     [["I don't know.", "నాకు తెలియదు.", "nāku teliyadu."], ["No problem.", "ప్రాబ్లమ్ లేదు.", "prāblam lēdu."], ["It's okay.", "సరే.", "sare."], ["Wait a minute.", "ఒక నిమిషం వేచి ఉండండి.", "oka nimiṣaṃ vēci uṇḍaṇḍi."]]),
    (849, "Frequently used sentences in Telugu – miscellaneous part 2", "More miscellaneous sentences.",
     [["I agree.", "నేను అంగీకరిస్తాను.", "nēnu aṃgīkaristānu."], ["I disagree.", "నేను అంగీకరించను.", "nēnu aṃgīkarin̄canu."], ["That's right.", "అది సరి.", "adi sari."], ["I think so.", "నేను అలా అనుకుంటున్నాను.", "nēnu alā anukuṃtunnānu."]]),
    (850, "Simple Telugu conversation – Quarrel at home", "Quarrel at home.",
     [["Why are you shouting?", "ఎందుకు అరుస్తున్నావు?", "eṃduku arustunnāvu?"], ["I am sorry.", "క్షమించండి.", "kṣamin̄caṇḍi."], ["Let us not fight.", "మనం పోరాడకూడదు.", "manaṃ pōrāḍakūḍadu."]]),
]

def main():
    with open("data_telugu.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Find index of first vocab chapter (798)
    idx_798 = next(i for i, ch in enumerate(data) if ch.get("id") == 798)
    # Remove old chapters 798-812
    data = [ch for ch in data if ch.get("id", 0) < 798 or ch.get("id", 0) > 812]
    # Find new insertion point (after chapter 797)
    idx_insert = next(i for i, ch in enumerate(data) if ch.get("id") == 797) + 1
    
    # Build new chapters
    new_chapters = []
    for ch in NEW_CHAPTERS:
        new_chapters.append(ch)
    
    for (cid, title, intro, rows) in CONV_CHAPTERS:
        new_chapters.append({
            "id": cid, "title": title, "url": "#", "content": intro, "intro": intro,
            "tables": [{"heading": "Conversation", "headers": ["English", "Telugu", "Transliteration"], "speakCol": 1, "rows": rows}]
        })
    
    # Insert new chapters
    for ch in reversed(new_chapters):
        data.insert(idx_insert, ch)
    
    with open("data_telugu.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("Added", len(new_chapters), "chapters to data_telugu.json")

if __name__ == "__main__":
    main()
