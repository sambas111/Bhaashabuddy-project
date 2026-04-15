import json

d = json.load(open('data_santali.json', 'r', encoding='utf-8'))

LESSONS = {}

# 597 - Body parts
LESSONS[597] = [
    ["head", "ᱛᱚᱞᱟ", "tola"],
    ["eye", "ᱢᱮᱫ", "med"],
    ["ear", "ᱞᱩᱛᱩᱨ", "lutur"],
    ["nose", "ᱢᱩᱸᱦ", "munh"],
    ["mouth", "ᱢᱚᱪᱟ", "mocha"],
    ["hand", "ᱛᱤᱸ", "ting"],
    ["leg", "ᱠᱟᱴᱟ", "kata"],
    ["stomach", "ᱞᱟᱜ", "lag"],
    ["back", "ᱛᱟᱹᱭᱱᱚᱢ", "taynom"],
    ["neck", "ᱦᱚᱛᱚᱜ", "hotog"],
    ["tooth", "ᱫᱟᱹᱛ", "dat"],
    ["hair", "ᱩᱵ", "ub"],
    ["face", "ᱢᱩᱦᱟᱹᱴ", "muhat"],
    ["finger", "ᱟᱸᱜᱩᱞᱤ", "anguli"],
    ["knee", "ᱛᱤᱸᱡᱚᱸᱜᱟ", "tingjonga"],
    ["chest", "ᱪᱟᱹᱛᱤ", "chati"],
    ["skin", "ᱪᱟᱢᱲᱟ", "chamra"],
    ["tongue", "ᱟᱞᱟᱝ", "alang"],
]

# 598 - Miscellaneous words
LESSONS[598] = [
    ["day", "ᱫᱤᱱ", "din"],
    ["night", "ᱧᱤᱸᱫᱟ", "nyinda"],
    ["sky", "ᱥᱮᱨᱢᱟ", "serma"],
    ["earth", "ᱫᱷᱟᱹᱨᱛᱤ", "dharti"],
    ["fire", "ᱥᱮᱸᱜᱮᱞ", "sengel"],
    ["wind", "ᱦᱚᱭᱚ", "hoyo"],
    ["rain", "ᱫᱟᱜ", "dag"],
    ["cloud", "ᱨᱤᱢᱤᱞ", "rimil"],
    ["river", "ᱜᱟᱰ", "gad"],
    ["mountain", "ᱵᱩᱨᱩ", "buru"],
    ["tree", "ᱫᱟᱨᱮ", "dare"],
    ["flower", "ᱵᱟᱦᱟ", "baha"],
    ["stone", "ᱫᱤᱨᱤ", "diri"],
    ["road", "ᱦᱚᱨᱟ", "hora"],
    ["house", "ᱚᱲᱟᱜ", "orag"],
    ["door", "ᱫᱩᱟᱹᱨ", "duar"],
    ["forest", "ᱵᱤᱨ", "bir"],
    ["field", "ᱞᱚᱛᱟᱨ", "lotar"],
]

# 599 - Relations
LESSONS[599] = [
    ["father", "ᱟᱯᱟ", "apa"],
    ["mother", "ᱟᱭᱚ", "ayo"],
    ["brother", "ᱦᱟᱯᱲᱟᱢ", "hapram"],
    ["sister", "ᱢᱤᱥᱤ", "misi"],
    ["grandfather", "ᱵᱟᱵᱟ", "baba"],
    ["grandmother", "ᱟᱡᱤ", "aji"],
    ["son", "ᱦᱚᱯᱚᱱ", "hopon"],
    ["daughter", "ᱢᱤᱡᱩ", "miju"],
    ["wife", "ᱮᱨᱟ", "era"],
    ["husband", "ᱠᱚᱲᱟ", "kora"],
    ["uncle", "ᱠᱟᱠᱟ", "kaka"],
    ["aunt", "ᱠᱟᱠᱤ", "kaki"],
    ["child", "ᱜᱤᱫᱽᱨᱟᱹ", "gidra"],
    ["friend", "ᱥᱟᱶᱛᱟ", "sawta"],
    ["son-in-law", "ᱡᱟᱣᱟᱭ", "jaway"],
    ["daughter-in-law", "ᱵᱚᱦᱩ", "bohu"],
    ["elder brother", "ᱵᱚᱭᱦᱟ", "boyha"],
    ["younger sister", "ᱵᱚᱱ", "bon"],
]

# 600 - Numbers Part 1 (1–18)
LESSONS[600] = [
    ["1 (one)", "ᱢᱤᱫ", "mid"],
    ["2 (two)", "ᱵᱟᱨ", "bar"],
    ["3 (three)", "ᱯᱮ", "pe"],
    ["4 (four)", "ᱯᱩᱱ", "pun"],
    ["5 (five)", "ᱢᱚᱬᱮ", "mone"],
    ["6 (six)", "ᱛᱩᱨᱩᱭ", "turuy"],
    ["7 (seven)", "ᱮᱭᱟᱭ", "eyay"],
    ["8 (eight)", "ᱤᱨᱟᱞ", "iral"],
    ["9 (nine)", "ᱟᱨᱮ", "are"],
    ["10 (ten)", "ᱜᱮᱞ", "gel"],
    ["11 (eleven)", "ᱜᱮᱞ ᱢᱤᱫ", "gel mid"],
    ["12 (twelve)", "ᱜᱮᱞ ᱵᱟᱨ", "gel bar"],
    ["13 (thirteen)", "ᱜᱮᱞ ᱯᱮ", "gel pe"],
    ["14 (fourteen)", "ᱜᱮᱞ ᱯᱩᱱ", "gel pun"],
    ["15 (fifteen)", "ᱜᱮᱞ ᱢᱚᱬᱮ", "gel mone"],
    ["16 (sixteen)", "ᱜᱮᱞ ᱛᱩᱨᱩᱭ", "gel turuy"],
    ["17 (seventeen)", "ᱜᱮᱞ ᱮᱭᱟᱭ", "gel eyay"],
    ["18 (eighteen)", "ᱜᱮᱞ ᱤᱨᱟᱞ", "gel iral"],
]

# 601 - Numbers Part 2 (19–10000)
LESSONS[601] = [
    ["19 (nineteen)", "ᱜᱮᱞ ᱟᱨᱮ", "gel are"],
    ["20 (twenty)", "ᱦᱤᱥᱤ", "hisi"],
    ["30 (thirty)", "ᱦᱤᱥᱤ ᱜᱮᱞ", "hisi gel"],
    ["40 (forty)", "ᱵᱟᱨ ᱦᱤᱥᱤ", "bar hisi"],
    ["50 (fifty)", "ᱵᱟᱨ ᱦᱤᱥᱤ ᱜᱮᱞ", "bar hisi gel"],
    ["60 (sixty)", "ᱯᱮ ᱦᱤᱥᱤ", "pe hisi"],
    ["70 (seventy)", "ᱯᱮ ᱦᱤᱥᱤ ᱜᱮᱞ", "pe hisi gel"],
    ["80 (eighty)", "ᱯᱩᱱ ᱦᱤᱥᱤ", "pun hisi"],
    ["90 (ninety)", "ᱯᱩᱱ ᱦᱤᱥᱤ ᱜᱮᱞ", "pun hisi gel"],
    ["100 (hundred)", "ᱢᱤᱫ ᱥᱟᱹᱭ", "mid say"],
    ["200 (two hundred)", "ᱵᱟᱨ ᱥᱟᱹᱭ", "bar say"],
    ["300 (three hundred)", "ᱯᱮ ᱥᱟᱹᱭ", "pe say"],
    ["400 (four hundred)", "ᱯᱩᱱ ᱥᱟᱹᱭ", "pun say"],
    ["500 (five hundred)", "ᱢᱚᱬᱮ ᱥᱟᱹᱭ", "mone say"],
    ["600 (six hundred)", "ᱛᱩᱨᱩᱭ ᱥᱟᱹᱭ", "turuy say"],
    ["700 (seven hundred)", "ᱮᱭᱟᱭ ᱥᱟᱹᱭ", "eyay say"],
    ["1000 (thousand)", "ᱢᱤᱫ ᱦᱟᱡᱟᱨ", "mid hajar"],
    ["10000 (ten thousand)", "ᱜᱮᱞ ᱦᱟᱡᱟᱨ", "gel hajar"],
]

# 602 - Fractions, ordinals, percentages
LESSONS[602] = [
    ["half", "ᱟᱹᱫᱷᱟ", "adha"],
    ["quarter", "ᱯᱟᱣᱟ", "pawa"],
    ["three-quarters", "ᱛᱤᱱ ᱯᱟᱣᱟ", "tin pawa"],
    ["first", "ᱯᱟᱦᱤᱞᱟ", "pahila"],
    ["second", "ᱫᱩᱥᱟᱨ", "dusar"],
    ["third", "ᱛᱮᱥᱟᱨ", "tesar"],
    ["fourth", "ᱪᱟᱹᱨ ᱱᱚᱢᱵᱚᱨ", "char nombor"],
    ["fifth", "ᱢᱚᱬᱮ ᱱᱚᱢᱵᱚᱨ", "mone nombor"],
    ["one-third", "ᱯᱮ ᱦᱤᱥᱟ ᱢᱤᱫ", "pe hisa mid"],
    ["two-thirds", "ᱯᱮ ᱦᱤᱥᱟ ᱵᱟᱨ", "pe hisa bar"],
    ["ten percent", "ᱜᱮᱞ ᱯᱟᱨᱥᱮᱱᱴ", "gel parsent"],
    ["twenty percent", "ᱦᱤᱥᱤ ᱯᱟᱨᱥᱮᱱᱴ", "hisi parsent"],
    ["fifty percent", "ᱵᱟᱨ ᱦᱤᱥᱤ ᱜᱮᱞ ᱯᱟᱨᱥᱮᱱᱴ", "bar hisi gel parsent"],
    ["hundred percent", "ᱢᱤᱫ ᱥᱟᱹᱭ ᱯᱟᱨᱥᱮᱱᱴ", "mid say parsent"],
    ["one and a half", "ᱰᱮᱲ", "der"],
    ["double / twice", "ᱵᱟᱨᱤᱭᱟ", "bariya"],
    ["thrice", "ᱯᱮ ᱵᱟᱨᱤᱭᱟ", "pe bariya"],
    ["last", "ᱢᱩᱪᱟᱹᱫ", "muchad"],
]

# 603 - Frequently used verbs Part 1
LESSONS[603] = [
    ["go", "ᱥᱮᱱ", "sen"],
    ["come", "ᱦᱤᱡᱩᱜ", "hijug"],
    ["eat", "ᱡᱚᱢ", "jom"],
    ["drink", "ᱧᱩ", "nyu"],
    ["see", "ᱧᱮᱞ", "nyel"],
    ["hear", "ᱟᱹᱭᱠᱟᱹᱣ", "aykaw"],
    ["speak", "ᱨᱚᱲ", "ror"],
    ["write", "ᱚᱞ", "ol"],
    ["read", "ᱯᱟᱲᱦᱟᱣ", "parhaw"],
    ["run", "ᱫᱟᱹᱲ", "dar"],
    ["sleep", "ᱧᱤᱫ", "nyid"],
    ["give", "ᱮᱢ", "em"],
    ["buy", "ᱠᱤᱱ", "kin"],
    ["sell", "ᱵᱮᱪᱟᱣ", "becaw"],
    ["bring", "ᱟᱹᱜᱩ", "agu"],
    ["call", "ᱠᱩᱞ", "kul"],
    ["sit", "ᱫᱩᱲᱩᱵ", "durub"],
    ["stand", "ᱛᱤᱧᱜᱩ", "tingu"],
]

# 604 - Frequently used verbs Part 2
LESSONS[604] = [
    ["walk", "ᱥᱟᱞᱟᱜ", "salag"],
    ["cry", "ᱨᱟᱹᱢ", "ram"],
    ["laugh", "ᱞᱟᱸᱫᱟ", "landa"],
    ["think", "ᱩᱢᱩᱱ", "umun"],
    ["know", "ᱵᱟᱰᱟᱭ", "baday"],
    ["want", "ᱞᱟᱜᱤᱫ", "lagid"],
    ["like", "ᱥᱩᱠ", "suk"],
    ["love", "ᱫᱩᱞᱟᱹᱲ", "dular"],
    ["fear", "ᱵᱚᱲ", "bor"],
    ["work", "ᱠᱟᱹᱢᱤ", "kami"],
    ["play", "ᱮᱱᱮᱡ", "enej"],
    ["sing", "ᱥᱮᱨᱮᱧ", "sereny"],
    ["dance", "ᱮᱱᱮᱪ", "enech"],
    ["wash", "ᱯᱟᱭᱲᱟ", "payra"],
    ["cook", "ᱨᱟᱸᱫ", "rand"],
    ["cut", "ᱛᱟᱹᱥ", "tas"],
    ["open", "ᱡᱷᱤᱡ", "jhij"],
    ["close", "ᱵᱚᱱᱫ", "bond"],
]

# 605 - Frequently used verbs Part 3
LESSONS[605] = [
    ["ask", "ᱠᱩᱞᱤ", "kuli"],
    ["answer", "ᱛᱮᱞᱟ", "tela"],
    ["wait", "ᱛᱟᱹᱧ", "tang"],
    ["search", "ᱥᱟᱸᱜᱤᱧ", "sanging"],
    ["find", "ᱧᱟᱢ", "nyam"],
    ["keep", "ᱫᱚᱦᱚ", "doho"],
    ["take", "ᱤᱫᱤ", "idi"],
    ["send", "ᱠᱩᱞᱟᱣ", "kulaw"],
    ["break", "ᱯᱷᱟᱲᱟᱣ", "pharaw"],
    ["build", "ᱵᱟᱱᱟᱣ", "banaw"],
    ["dig", "ᱛᱩᱲ", "tur"],
    ["plant", "ᱨᱚᱯᱚᱫ", "ropod"],
    ["catch", "ᱟᱹᱰᱤ", "adi"],
    ["throw", "ᱜᱟᱰ", "gad"],
    ["pull", "ᱜᱚᱡ", "goj"],
    ["push", "ᱫᱮᱞ", "del"],
    ["lift", "ᱪᱩᱠᱟᱣ", "chukaw"],
    ["drop", "ᱚᱡᱟᱜ", "ojag"],
]

# 606 - Frequently used verbs Part 4
LESSONS[606] = [
    ["tell", "ᱟᱞᱚ", "alo"],
    ["show", "ᱫᱮᱠᱷᱟᱣ", "dekhaw"],
    ["help", "ᱜᱚᱲᱚ", "goro"],
    ["fight", "ᱞᱟᱲᱟᱭ", "laray"],
    ["win", "ᱡᱤᱛᱟᱣ", "jitaw"],
    ["lose", "ᱦᱟᱨᱟᱣ", "haraw"],
    ["live", "ᱛᱟᱹᱦᱮᱸᱱ", "tahen"],
    ["die", "ᱜᱚᱪ", "goch"],
    ["fly", "ᱩᱲᱩᱜ", "urug"],
    ["swim", "ᱩᱭᱦᱟᱹᱨ", "uyhar"],
    ["climb", "ᱪᱟᱰᱟᱣ", "chadaw"],
    ["hide", "ᱞᱩᱠᱟᱣ", "lukaw"],
    ["pray", "ᱵᱤᱱᱛᱤ", "binti"],
    ["fall", "ᱩᱞᱟᱹᱠ", "ulak"],
    ["return", "ᱨᱩᱣᱟᱹᱲ", "ruwar"],
    ["count", "ᱞᱮᱠᱷᱟ", "lekha"],
    ["teach", "ᱚᱞᱮᱫ", "oled"],
    ["wear", "ᱥᱟᱡᱟᱣ", "sajaw"],
]

# 607 - One verb, multiple meanings Part 1
LESSONS[607] = [
    ["see", "ᱧᱮᱞ", "nyel"],
    ["look at", "ᱧᱮᱞ", "nyel"],
    ["watch", "ᱧᱮᱞ", "nyel"],
    ["go", "ᱥᱮᱱ", "sen"],
    ["depart", "ᱥᱮᱱ", "sen"],
    ["move away", "ᱥᱮᱱ", "sen"],
    ["eat", "ᱡᱚᱢ", "jom"],
    ["consume", "ᱡᱚᱢ", "jom"],
    ["dine", "ᱡᱚᱢ", "jom"],
    ["speak", "ᱨᱚᱲ", "ror"],
    ["say", "ᱨᱚᱲ", "ror"],
    ["talk", "ᱨᱚᱲ", "ror"],
    ["keep", "ᱫᱚᱦᱚ", "doho"],
    ["put", "ᱫᱚᱦᱚ", "doho"],
    ["place", "ᱫᱚᱦᱚ", "doho"],
    ["give", "ᱮᱢ", "em"],
    ["offer", "ᱮᱢ", "em"],
    ["hand over", "ᱮᱢ", "em"],
]

# 608 - One verb, multiple meanings Part 2
LESSONS[608] = [
    ["call", "ᱠᱩᱞ", "kul"],
    ["summon", "ᱠᱩᱞ", "kul"],
    ["invite", "ᱠᱩᱞ", "kul"],
    ["run", "ᱫᱟᱹᱲ", "dar"],
    ["rush", "ᱫᱟᱹᱲ", "dar"],
    ["flee", "ᱫᱟᱹᱲ", "dar"],
    ["write", "ᱚᱞ", "ol"],
    ["compose", "ᱚᱞ", "ol"],
    ["inscribe", "ᱚᱞ", "ol"],
    ["drink", "ᱧᱩ", "nyu"],
    ["sip", "ᱧᱩ", "nyu"],
    ["swallow", "ᱧᱩ", "nyu"],
    ["buy", "ᱠᱤᱱ", "kin"],
    ["purchase", "ᱠᱤᱱ", "kin"],
    ["acquire", "ᱠᱤᱱ", "kin"],
    ["come", "ᱦᱤᱡᱩᱜ", "hijug"],
    ["arrive", "ᱦᱤᱡᱩᱜ", "hijug"],
    ["reach", "ᱦᱤᱡᱩᱜ", "hijug"],
]

# 609 - Adjectives
LESSONS[609] = [
    ["big", "ᱢᱟᱨᱟᱝ", "marang"],
    ["small", "ᱦᱩᱰᱤᱧ", "huding"],
    ["good", "ᱵᱷᱟᱞᱮ", "bhale"],
    ["bad", "ᱯᱩᱨᱟᱹ", "pura"],
    ["hot", "ᱛᱟᱛᱟ", "tata"],
    ["cold", "ᱫᱷᱤᱨᱤ", "dhiri"],
    ["beautiful", "ᱥᱚᱢᱵᱷᱟᱨ", "sombhar"],
    ["new", "ᱱᱟᱣᱟ", "nawa"],
    ["old", "ᱢᱟᱨᱟᱝ", "marang"],
    ["clean", "ᱥᱟᱯᱷᱟ", "sapha"],
    ["dirty", "ᱪᱤᱠᱟᱹᱱ", "chikan"],
    ["sweet", "ᱢᱤᱴᱷᱟᱹ", "mitha"],
    ["bitter", "ᱠᱟᱲᱟ", "kara"],
    ["tall", "ᱡᱟᱱᱟᱣ", "janaw"],
    ["short", "ᱠᱷᱟᱴᱚ", "khato"],
    ["heavy", "ᱵᱷᱟᱨᱤ", "bhari"],
    ["light (weight)", "ᱦᱟᱞᱠᱟ", "halka"],
    ["strong", "ᱡᱚᱨ", "jor"],
]

# 610 - Adverbs Part 1
LESSONS[610] = [
    ["quickly", "ᱡᱟᱞᱫᱤ", "jaldi"],
    ["slowly", "ᱟᱹᱭᱥᱛᱮ", "ayste"],
    ["here", "ᱱᱮᱛᱟᱨ", "netar"],
    ["there", "ᱚᱱᱫᱮ", "onde"],
    ["now", "ᱱᱤᱛ", "nit"],
    ["then", "ᱛᱟᱭᱚᱢ", "tayom"],
    ["always", "ᱡᱟᱦᱟᱸᱱᱟᱜ", "jahanag"],
    ["never", "ᱵᱟᱝᱢᱟ", "bangma"],
    ["today", "ᱛᱮᱦᱮᱧ", "tehenj"],
    ["tomorrow", "ᱜᱟᱯᱟ", "gapa"],
    ["yesterday", "ᱦᱚᱞᱟ", "hola"],
    ["very", "ᱟᱹᱰᱤ", "adi"],
    ["outside", "ᱵᱟᱦᱨᱮ", "bahre"],
    ["inside", "ᱵᱷᱤᱛᱨᱤ", "bhitri"],
    ["up", "ᱪᱮᱛᱟᱱ", "chetan"],
    ["down", "ᱞᱟᱛᱟᱨ", "latar"],
    ["together", "ᱥᱟᱸᱜᱮ", "sange"],
    ["much / many", "ᱦᱩᱭᱩᱜ", "huyug"],
]

# 611 - Adverbs Part 2
LESSONS[611] = [
    ["again", "ᱟᱹᱲᱤᱥ", "aris"],
    ["also", "ᱦᱚ", "ho"],
    ["only", "ᱠᱷᱟᱞᱤ", "khali"],
    ["perhaps", "ᱥᱟᱭᱫ", "sayd"],
    ["surely", "ᱡᱟᱨᱩᱨ", "jarur"],
    ["already", "ᱦᱟᱵᱤᱡ", "habij"],
    ["still", "ᱟᱹᱰᱤᱭᱟᱜ", "adiyag"],
    ["early", "ᱥᱮᱛᱟᱜ", "setag"],
    ["late", "ᱵᱮᱞᱟ", "bela"],
    ["far", "ᱫᱩᱨ", "dur"],
    ["near", "ᱱᱮᱰᱟ", "neda"],
    ["often", "ᱵᱟᱨ ᱵᱟᱨ", "bar bar"],
    ["alone", "ᱢᱤᱫᱛᱟᱱ", "midtan"],
    ["silently", "ᱪᱩᱯ", "chup"],
    ["loudly", "ᱡᱚᱨ ᱥᱮ", "jor se"],
    ["well", "ᱵᱷᱟᱞ ᱜᱮ", "bhal ge"],
    ["truly", "ᱥᱟᱹᱨᱤ", "sari"],
    ["enough", "ᱪᱟᱞᱟᱜ", "chalag"],
]

# 612 - Vegetables
LESSONS[612] = [
    ["potato", "ᱟᱹᱞᱩ", "alu"],
    ["onion", "ᱯᱤᱭᱟᱡ", "piyaj"],
    ["tomato", "ᱴᱟᱢᱟᱴᱚ", "tamato"],
    ["brinjal", "ᱵᱟᱭᱜᱚᱱ", "baygon"],
    ["cabbage", "ᱵᱟᱸᱫᱷᱟ ᱠᱚᱯᱤ", "bandha kopi"],
    ["spinach", "ᱯᱟᱞᱟᱠ", "palak"],
    ["cauliflower", "ᱯᱷᱩᱞ ᱠᱚᱯᱤ", "phul kopi"],
    ["pumpkin", "ᱠᱚᱦᱲᱟ", "kohra"],
    ["radish", "ᱢᱩᱞᱟ", "mula"],
    ["carrot", "ᱜᱟᱡᱟᱨ", "gajar"],
    ["cucumber", "ᱠᱷᱤᱭᱟᱨᱤ", "khiyari"],
    ["okra / ladyfinger", "ᱵᱷᱤᱸᱰᱤ", "bhindi"],
    ["peas", "ᱢᱟᱴᱟᱨ", "matar"],
    ["beans", "ᱥᱮᱢ", "sem"],
    ["bitter gourd", "ᱠᱟᱨᱮᱞᱟ", "karela"],
    ["bottle gourd", "ᱞᱟᱩ", "lau"],
    ["ginger", "ᱟᱹᱫᱟ", "ada"],
    ["garlic", "ᱨᱟᱥᱩᱱ", "rasun"],
]

# 613 - Fruits
LESSONS[613] = [
    ["mango", "ᱟᱹᱢ", "am"],
    ["banana", "ᱠᱮᱞᱟ", "kela"],
    ["apple", "ᱥᱮᱵ", "seb"],
    ["guava", "ᱯᱮᱭᱟᱨᱟ", "peyara"],
    ["jackfruit", "ᱯᱷᱟᱱᱟᱥ", "phanas"],
    ["papaya", "ᱯᱟᱯᱟᱭᱟ", "papaya"],
    ["orange", "ᱠᱟᱢᱞᱟ", "kamla"],
    ["grape", "ᱟᱸᱜᱩᱨ", "angur"],
    ["watermelon", "ᱛᱟᱨᱵᱩᱡ", "tarbuj"],
    ["coconut", "ᱱᱟᱨᱤᱭᱟᱞ", "nariyal"],
    ["lemon", "ᱞᱮᱢᱵᱩ", "lembu"],
    ["pineapple", "ᱟᱱᱟᱨᱟᱥ", "anaras"],
    ["pomegranate", "ᱫᱟᱨᱤᱢ", "darim"],
    ["litchi", "ᱞᱤᱪᱤ", "lichi"],
    ["custard apple", "ᱥᱤᱛᱟᱯᱷᱟᱞ", "sitaphal"],
    ["date", "ᱠᱷᱟᱡᱩᱨ", "khajur"],
    ["plum", "ᱟᱹᱞᱩᱵᱩᱠᱷᱟᱨᱟ", "alu bukhara"],
    ["sugarcane", "ᱠᱩᱥᱤᱭᱟᱨ", "kusiyar"],
]

# 614 - Birds
LESSONS[614] = [
    ["crow", "ᱠᱟᱹᱜ", "kag"],
    ["parrot", "ᱛᱚᱛᱟ", "tota"],
    ["pigeon", "ᱯᱟᱨᱟ", "para"],
    ["eagle", "ᱪᱤᱞ", "chil"],
    ["sparrow", "ᱜᱟᱹᱩᱨᱟ", "gaura"],
    ["peacock", "ᱢᱟᱭᱩᱨ", "mayur"],
    ["cuckoo", "ᱠᱚᱮᱞ", "koel"],
    ["owl", "ᱠᱩᱠᱩ", "kuku"],
    ["hen", "ᱥᱤᱢ", "sim"],
    ["duck", "ᱦᱟᱸᱥ", "hans"],
    ["swan", "ᱦᱟᱸᱥ ᱨᱟᱡᱟ", "hans raja"],
    ["crane", "ᱵᱚᱜᱞᱟ", "bogla"],
    ["woodpecker", "ᱠᱟᱴᱷ ᱯᱷᱚᱨᱣᱟ", "kath phorwa"],
    ["kingfisher", "ᱢᱟᱪᱷᱨᱟᱸᱜᱟ", "machranga"],
    ["hawk", "ᱵᱟᱡ", "baj"],
    ["mynah", "ᱢᱮᱱᱟ", "mena"],
    ["vulture", "ᱜᱤᱫᱷ", "gidh"],
    ["heron", "ᱵᱟᱜᱩᱞᱟ", "bagula"],
]

# 615 - Insects
LESSONS[615] = [
    ["ant", "ᱢᱩᱸᱢᱩᱸ", "munmun"],
    ["butterfly", "ᱯᱤᱸᱯᱤᱲᱤ", "pinpiri"],
    ["mosquito", "ᱢᱚᱪᱷᱟᱨ", "mochhar"],
    ["spider", "ᱡᱟᱹᱞᱟᱹ", "jala"],
    ["bee", "ᱢᱚᱦᱩ", "mohu"],
    ["fly", "ᱢᱟᱹᱪᱷᱤ", "machhi"],
    ["cockroach", "ᱛᱮᱞᱪᱟᱴᱴᱟ", "telchatta"],
    ["grasshopper", "ᱯᱷᱩᱫᱜᱟ", "phudga"],
    ["beetle", "ᱜᱩᱵᱲᱮᱞ", "gubrel"],
    ["worm", "ᱜᱚᱡᱚ", "gojo"],
    ["caterpillar", "ᱵᱟᱞᱩ", "balu"],
    ["centipede", "ᱠᱟᱱᱠᱷᱟᱡᱩᱨᱟ", "kankhajura"],
    ["scorpion", "ᱵᱤᱪᱷᱩ", "bichhu"],
    ["termite", "ᱩᱯᱨᱚᱡ", "uproj"],
    ["firefly", "ᱡᱩᱜᱱᱩ", "jugnu"],
    ["ladybug", "ᱨᱟᱸᱜᱤᱱ ᱯᱚᱠᱟ", "rangin poka"],
    ["moth", "ᱯᱟᱛᱟᱸᱜᱟ", "patanga"],
    ["cricket", "ᱡᱷᱤᱸᱜᱩᱨ", "jhingur"],
]

# 616 - Colours
LESSONS[616] = [
    ["red", "ᱟᱨᱟᱜ", "arag"],
    ["blue", "ᱱᱤᱞ", "nil"],
    ["green", "ᱥᱟᱥᱟᱝ", "sasang"],
    ["yellow", "ᱥᱟᱥᱟᱝ", "sasang"],
    ["white", "ᱯᱩᱸᱰ", "pund"],
    ["black", "ᱦᱮᱸᱫᱮ", "hende"],
    ["orange", "ᱥᱟᱸᱫᱩᱨᱤ", "sanduri"],
    ["pink", "ᱜᱩᱞᱟᱵᱤ", "gulabi"],
    ["brown", "ᱠᱷᱟᱭᱨᱤ", "khayri"],
    ["purple", "ᱵᱮᱸᱜᱱᱤ", "bengni"],
    ["grey", "ᱥᱞᱮᱴᱤ", "sleti"],
    ["golden", "ᱥᱚᱱᱟᱞᱤ", "sonali"],
    ["silver", "ᱨᱩᱯᱟᱞᱤ", "rupali"],
    ["maroon", "ᱢᱮᱨᱩᱱ", "merun"],
    ["sky blue", "ᱟᱥᱢᱟᱱᱤ", "asmani"],
    ["cream", "ᱠᱨᱤᱢ", "krim"],
    ["dark", "ᱟᱸᱫᱷᱟᱨ", "andhar"],
    ["light (colour)", "ᱦᱟᱞᱠᱟ", "halka"],
]

# 617 - Flowers
LESSONS[617] = [
    ["lotus", "ᱯᱚᱫᱚᱢ", "podom"],
    ["rose", "ᱜᱩᱞᱟᱯ", "gulap"],
    ["marigold", "ᱜᱮᱸᱫᱟ", "genda"],
    ["jasmine", "ᱡᱩᱦᱤ", "juhi"],
    ["sunflower", "ᱥᱩᱨᱡᱢᱩᱠᱷᱤ", "surjmukhi"],
    ["lily", "ᱠᱩᱢᱩᱫ", "kumud"],
    ["hibiscus", "ᱡᱟᱵᱟ", "jaba"],
    ["champa", "ᱪᱟᱸᱯᱟ", "champa"],
    ["dahlia", "ᱰᱮᱞᱤᱭᱟ", "deliya"],
    ["tube rose", "ᱨᱟᱡᱱᱤᱜᱟᱸᱫᱷᱟ", "rajnigandha"],
    ["oleander", "ᱠᱟᱸᱱᱮᱨ", "kaner"],
    ["chrysanthemum", "ᱪᱟᱸᱫᱢᱟᱞᱟ", "chandmala"],
    ["night jasmine", "ᱥᱤᱩᱞᱤ", "siuli"],
    ["palash", "ᱯᱟᱞᱟᱥ", "palas"],
    ["bougainvillea", "ᱵᱚᱜᱟᱱᱵᱤᱞᱟ", "boganvila"],
    ["plumeria", "ᱜᱩᱞᱟᱪᱤᱱ", "gulachin"],
    ["periwinkle", "ᱥᱟᱫᱟᱵᱟᱦᱟᱨ", "sadabahar"],
    ["mango blossom", "ᱢᱩᱧᱡᱩᱨ", "munjur"],
]

# 618 - Animals
LESSONS[618] = [
    ["cow", "ᱢᱟᱨᱟᱝ ᱢᱮᱭᱟᱫ", "marang meyad"],
    ["goat", "ᱢᱮᱨᱚᱢ", "merom"],
    ["dog", "ᱥᱮᱛᱟ", "seta"],
    ["cat", "ᱢᱮᱭᱟᱫ", "meyad"],
    ["horse", "ᱥᱟᱫᱚᱢ", "sadom"],
    ["elephant", "ᱦᱟᱛᱤ", "hati"],
    ["tiger", "ᱠᱩᱞ", "kul"],
    ["lion", "ᱥᱤᱧᱦ", "singh"],
    ["deer", "ᱵᱤᱫ", "bid"],
    ["monkey", "ᱵᱟᱱᱫᱚᱨ", "bandor"],
    ["buffalo", "ᱢᱩᱸᱰᱟ", "munda"],
    ["pig", "ᱥᱩᱠᱨᱤ", "sukri"],
    ["bear", "ᱵᱷᱟᱞᱩ", "bhalu"],
    ["fox", "ᱞᱚᱢᱵᱚ", "lombo"],
    ["rabbit", "ᱠᱷᱟᱨᱜᱚᱥ", "khargos"],
    ["snake", "ᱵᱤᱧ", "bing"],
    ["frog", "ᱫᱟᱫᱚᱨ", "dador"],
    ["fish", "ᱢᱟᱹᱪᱷᱟ", "machha"],
]

# 619 - Common miscellaneous words
LESSONS[619] = [
    ["sun", "ᱥᱤᱧ", "sing"],
    ["moon", "ᱪᱟᱸᱫᱚ", "chando"],
    ["star", "ᱤᱯᱤᱞ", "ipil"],
    ["friend", "ᱥᱟᱶᱛᱟ", "sawta"],
    ["enemy", "ᱵᱮᱨᱤ", "beri"],
    ["king", "ᱨᱟᱡᱟ", "raja"],
    ["god", "ᱢᱟᱨᱟᱝ ᱵᱩᱨᱩ", "marang buru"],
    ["village", "ᱟᱹᱛᱩ", "atu"],
    ["country", "ᱫᱤᱥᱚᱢ", "disom"],
    ["language", "ᱯᱟᱹᱨᱥᱤ", "parsi"],
    ["person", "ᱦᱚᱲ", "hor"],
    ["market", "ᱦᱟᱹᱴ", "hat"],
    ["book", "ᱯᱩᱛᱷᱤ", "puthi"],
    ["song", "ᱥᱮᱨᱮᱧ", "sereny"],
    ["festival", "ᱯᱚᱨᱚᱵ", "porob"],
    ["school", "ᱚᱞ ᱚᱲᱟᱜ", "ol orag"],
    ["food", "ᱡᱚᱢᱟᱜ", "jomag"],
    ["money", "ᱴᱟᱠᱟ", "taka"],
]

updated = 0
for ch in d:
    lid = ch['id']
    if lid in LESSONS:
        ch['blocks'] = [{
            "type": "table",
            "columns": ["English", "Santali (Ol Chiki)", "Transliteration"],
            "rows": LESSONS[lid]
        }]
        updated += 1

with open('data_santali.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')

print(f'Section 4 (597-619) populated: {updated} lessons updated')
for lid in sorted(LESSONS.keys()):
    count = len(LESSONS[lid])
    print(f'  Lesson {lid}: {count} rows')
