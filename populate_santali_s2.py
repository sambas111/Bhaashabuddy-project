import json

d = json.load(open('data_santali.json', 'r', encoding='utf-8'))

LESSONS = {}

# 510 - Pronouns and Articles in Santali
LESSONS[510] = [
    ["I", "ᱤᱧ", "inj"],
    ["You (singular)", "ᱟᱢ", "am"],
    ["He / She", "ᱩᱱᱤ", "uni"],
    ["We (inclusive)", "ᱟᱞᱮ", "ale"],
    ["We (exclusive)", "ᱟᱵᱚ", "abo"],
    ["You (plural)", "ᱟᱯᱮ", "ape"],
    ["They (human)", "ᱩᱱᱠᱩ", "unku"],
    ["They (non-human)", "ᱚᱱᱟ ᱠᱚ", "ona ko"],
    ["This", "ᱱᱚᱣᱟ", "nowa"],
    ["That", "ᱚᱱᱟ", "ona"],
    ["These", "ᱱᱚᱣᱟ ᱠᱚ", "nowa ko"],
    ["Those", "ᱚᱱᱟ ᱠᱚ", "ona ko"],
    ["My / mine", "ᱤᱧᱟᱜ", "injag"],
    ["Your / yours", "ᱟᱢᱟᱜ", "amag"],
    ["His / her", "ᱩᱱᱤᱟᱜ", "uniag"],
    ["Our (inclusive)", "ᱟᱞᱮᱭᱟᱜ", "aleyag"],
    ["Our (exclusive)", "ᱟᱵᱚᱭᱟᱜ", "aboyag"],
    ["Their", "ᱩᱱᱠᱩᱭᱟᱜ", "unkuag"]
]

# 511 - Using plurals to indicate respect
LESSONS[511] = [
    ["Father (respectful)", "ᱟᱯᱟ", "apa"],
    ["Mother (respectful)", "ᱟᱭᱚ", "ayo"],
    ["Grandfather", "ᱵᱟᱵᱟ", "baba"],
    ["Grandmother", "ᱟᱡᱤ", "aji"],
    ["Village head (respectful)", "ᱢᱟᱹᱧᱡᱷᱤ", "manjhi"],
    ["Elder brother (respectful)", "ᱵᱚᱭᱦᱟ", "boyha"],
    ["Elder sister (respectful)", "ᱵᱟᱭ", "bay"],
    ["Teacher (respectful)", "ᱯᱟᱲᱦᱟᱣᱮᱫ", "parhawed"],
    ["Please come (respectful)", "ᱦᱮᱡ ᱦᱤᱡᱩᱜ ᱢᱮ", "hej hijug me"],
    ["Please sit down (respectful)", "ᱦᱮᱡ ᱫᱩᱲᱩᱵ ᱢᱮ", "hej durub me"],
    ["Please eat (respectful)", "ᱦᱮᱡ ᱡᱚᱢ ᱢᱮ", "hej jom me"],
    ["They (elders) came", "ᱩᱱᱠᱩ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "unku hijug ena"],
    ["Father went to the market", "ᱟᱯᱟ ᱵᱟᱡᱟᱨ ᱥᱮᱱ ᱮᱱᱟ", "apa bajar sen ena"],
    ["Grandmother told a story", "ᱟᱡᱤ ᱠᱟᱹᱦᱱᱤ ᱨᱚᱲ ᱮᱱᱟ", "aji kahni ror ena"],
    ["Grandfather is resting", "ᱵᱟᱵᱟ ᱥᱮᱨᱮᱧ ᱢᱮᱱᱟᱜ ᱟ", "baba sereny menag a"],
    ["Teacher taught well", "ᱯᱟᱲᱦᱟᱣᱮᱫ ᱵᱷᱟᱞᱮ ᱯᱟᱲᱦᱟᱣ ᱮᱱᱟ", "parhawed bhale parhaw ena"],
    ["Elder sister is cooking", "ᱵᱟᱭ ᱨᱟᱸᱰᱷᱟ ᱢᱮᱱᱟᱜ ᱟ", "bay randha menag a"],
    ["The elders blessed us", "ᱢᱟᱨᱟᱝ ᱦᱚᱲ ᱠᱚ ᱟᱞᱮ ᱠᱮ ᱫᱩᱣᱟᱹ ᱮᱢ ᱮᱱᱟ", "marang hor ko ale ke duwa em ena"]
]

# 512 - Verbs in Santali
LESSONS[512] = [
    ["I go", "ᱤᱧ ᱥᱮᱱ ᱟᱭᱟ", "inj sen aya"],
    ["You eat", "ᱟᱢ ᱡᱚᱢ ᱟᱢ", "am jom am"],
    ["He sees", "ᱩᱱᱤ ᱧᱮᱞ ᱟᱫ ᱮ", "uni nyel ad e"],
    ["We write", "ᱟᱞᱮ ᱚᱞ ᱟᱞᱮ", "ale ol ale"],
    ["They run", "ᱩᱱᱠᱩ ᱫᱟᱹᱲ ᱟᱠᱟᱫᱟ", "unku dar akada"],
    ["I speak", "ᱤᱧ ᱨᱚᱲ ᱟᱭᱟ", "inj ror aya"],
    ["You read", "ᱟᱢ ᱯᱟᱲᱦᱟᱣ ᱟᱢ", "am parhaw am"],
    ["She listens", "ᱩᱱᱤ ᱟᱹᱭᱠᱟᱹᱣ ᱟᱫ ᱮ", "uni aykaw ad e"],
    ["We drink water", "ᱟᱞᱮ ᱫᱟᱜ ᱧᱩ ᱟᱞᱮ", "ale dag nyu ale"],
    ["They come", "ᱩᱱᱠᱩ ᱦᱤᱡᱩᱜ ᱟᱠᱟᱫᱟ", "unku hijug akada"],
    ["I sleep", "ᱤᱧ ᱧᱤᱫ ᱟᱭᱟ", "inj nyid aya"],
    ["You give", "ᱟᱢ ᱮᱢ ᱟᱢ", "am em am"],
    ["He works", "ᱩᱱᱤ ᱠᱟᱹᱢᱤ ᱠᱮᱫ ᱮ", "uni kami ked e"],
    ["I buy", "ᱤᱧ ᱠᱤᱱ ᱟᱭᱟ", "inj kin aya"],
    ["She brings", "ᱩᱱᱤ ᱟᱹᱜᱩ ᱟᱫ ᱮ", "uni agu ad e"],
    ["We call", "ᱟᱞᱮ ᱠᱩᱞ ᱟᱞᱮ", "ale kul ale"],
    ["They sit", "ᱩᱱᱠᱩ ᱫᱩᱲᱩᱵ ᱟᱠᱟᱫᱟ", "unku durub akada"],
    ["I learn", "ᱤᱧ ᱥᱮᱪᱮᱫ ᱟᱭᱟ", "inj seced aya"]
]

# 513 - Simple Present Tense
LESSONS[513] = [
    ["I go to school", "ᱤᱧ ᱥᱠᱩᱞ ᱥᱮᱱ ᱟᱭᱟ", "inj skul sen aya"],
    ["You eat rice", "ᱟᱢ ᱫᱟᱹᱠ ᱡᱚᱢ ᱟᱢ", "am dak jom am"],
    ["He reads a book", "ᱩᱱᱤ ᱯᱩᱛᱷᱤ ᱯᱟᱲᱦᱟᱣ ᱟᱫ ᱮ", "uni puthi parhaw ad e"],
    ["She drinks water", "ᱩᱱᱤ ᱫᱟᱜ ᱧᱩ ᱟᱫ ᱮ", "uni dag nyu ad e"],
    ["We go to the market", "ᱟᱞᱮ ᱵᱟᱡᱟᱨ ᱥᱮᱱ ᱟᱞᱮ", "ale bajar sen ale"],
    ["They play in the field", "ᱩᱱᱠᱩ ᱜᱟᱰᱟ ᱨᱮ ᱮᱱᱮᱡ ᱟᱠᱟᱫᱟ", "unku gada re enej akada"],
    ["I write a letter", "ᱤᱧ ᱪᱤᱴᱷᱤ ᱚᱞ ᱟᱭᱟ", "inj chithi ol aya"],
    ["You speak Santali", "ᱟᱢ ᱥᱟᱱᱛᱟᱲᱤ ᱨᱚᱲ ᱟᱢ", "am santari ror am"],
    ["Father works every day", "ᱟᱯᱟ ᱫᱤᱱ ᱫᱤᱱ ᱠᱟᱹᱢᱤ ᱠᱮᱫ ᱮ", "apa din din kami ked e"],
    ["Mother cooks food", "ᱟᱭᱚ ᱡᱚᱢ ᱨᱟᱸᱰᱷᱟ ᱟᱫ ᱮ", "ayo jom randha ad e"],
    ["The children study", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱯᱟᱲᱦᱟᱣ ᱟᱠᱟᱫᱟ", "gidra ko parhaw akada"],
    ["The bird flies", "ᱪᱮᱨᱮ ᱩᱰᱟᱹᱣ ᱟᱫ ᱮ", "cere udaw ad e"],
    ["The dog runs", "ᱥᱮᱛᱟ ᱫᱟᱹᱲ ᱟᱫ ᱮ", "seta dar ad e"],
    ["I live in the village", "ᱤᱧ ᱟᱹᱛᱩ ᱨᱮ ᱛᱟᱦᱮᱸᱱ ᱟᱭᱟ", "inj atu re taheny aya"],
    ["She sings a song", "ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱟᱫ ᱮ", "uni sereny ad e"],
    ["We love our country", "ᱟᱞᱮ ᱟᱞᱮᱭᱟᱜ ᱫᱤᱥᱚᱢ ᱫᱩᱞᱟᱹᱲ ᱟᱞᱮ", "ale aleyag disom dular ale"],
    ["I bathe in the morning", "ᱤᱧ ᱥᱮᱛᱟᱜ ᱨᱮ ᱡᱩ ᱟᱭᱟ", "inj setag re ju aya"],
    ["He walks to the field", "ᱩᱱᱤ ᱜᱟᱰᱟ ᱛᱮ ᱥᱟᱞᱟᱜ ᱟᱫ ᱮ", "uni gada te salag ad e"]
]

# 514 - Simple Present Tense of "To Be"
LESSONS[514] = [
    ["I am a student", "ᱤᱧ ᱢᱤᱫ ᱪᱟᱴᱟᱨ ᱠᱟᱱᱟ", "inj mid chatar kana"],
    ["You are a teacher", "ᱟᱢ ᱢᱤᱫ ᱯᱟᱲᱦᱟᱣᱮᱫ ᱠᱟᱱᱟ", "am mid parhawed kana"],
    ["He is a farmer", "ᱩᱱᱤ ᱢᱤᱫ ᱨᱟᱹᱭᱡ ᱠᱟᱱᱟ", "uni mid rayj kana"],
    ["She is at home", "ᱩᱱᱤ ᱚᱲᱟᱜ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "uni orag re menag a"],
    ["We are Santali people", "ᱟᱞᱮ ᱥᱟᱱᱛᱟᱲ ᱦᱚᱲ ᱠᱟᱱᱟ", "ale santar hor kana"],
    ["They are good people", "ᱩᱱᱠᱩ ᱵᱷᱟᱞᱮ ᱦᱚᱲ ᱠᱟᱱᱟ", "unku bhale hor kana"],
    ["I am happy", "ᱤᱧ ᱨᱟᱹᱥᱠᱟᱹ ᱢᱮᱱᱟᱜ ᱟ", "inj raska menag a"],
    ["You are tall", "ᱟᱢ ᱡᱟᱱᱟᱝ ᱠᱟᱱᱟ", "am janang kana"],
    ["It is hot today", "ᱟᱡ ᱫᱩᱨᱩᱵ ᱢᱮᱱᱟᱜ ᱟ", "aj durub menag a"],
    ["The food is ready", "ᱡᱚᱢ ᱦᱟᱹᱸᱰᱤ ᱮᱱᱟ", "jom handi ena"],
    ["This is my house", "ᱱᱚᱣᱟ ᱤᱧᱟᱜ ᱚᱲᱟᱜ ᱠᱟᱱᱟ", "nowa injag orag kana"],
    ["That is a big tree", "ᱚᱱᱟ ᱢᱤᱫ ᱢᱟᱨᱟᱝ ᱫᱟᱨᱮ ᱠᱟᱱᱟ", "ona mid marang dare kana"],
    ["The river is long", "ᱜᱟᱰᱟ ᱡᱟᱱᱟᱝ ᱢᱮᱱᱟᱜ ᱟ", "gada janang menag a"],
    ["I am from Jharkhand", "ᱤᱧ ᱡᱷᱟᱨᱠᱷᱚᱸᱰ ᱠᱷᱚᱱ ᱠᱟᱱᱟ", "inj Jharkhand khon kana"],
    ["This village is beautiful", "ᱱᱚᱣᱟ ᱟᱹᱛᱩ ᱥᱚᱢᱵᱷᱟᱨ ᱢᱮᱱᱟᱜ ᱟ", "nowa atu sombhar menag a"],
    ["He is my friend", "ᱩᱱᱤ ᱤᱧᱟᱜ ᱥᱟᱶᱛᱟ ᱠᱟᱱᱟ", "uni injag sawta kana"],
    ["The water is cold", "ᱫᱟᱜ ᱫᱷᱤᱨᱤ ᱢᱮᱱᱟᱜ ᱟ", "dag dhiri menag a"],
    ["We are brothers", "ᱟᱞᱮ ᱦᱟᱯᱲᱟᱢ ᱠᱟᱱᱟ", "ale hapram kana"]
]

# 515 - Present Continuous Tense
LESSONS[515] = [
    ["I am going", "ᱤᱧ ᱥᱮᱱ ᱟᱭᱟ", "inj sen aya"],
    ["You are eating", "ᱟᱢ ᱡᱚᱢ ᱟᱢ", "am jom am"],
    ["He is reading", "ᱩᱱᱤ ᱯᱟᱲᱦᱟᱣ ᱢᱮᱱᱟᱜ ᱟ", "uni parhaw menag a"],
    ["She is cooking", "ᱩᱱᱤ ᱨᱟᱸᱰᱷᱟ ᱢᱮᱱᱟᱜ ᱟ", "uni randha menag a"],
    ["We are studying", "ᱟᱞᱮ ᱯᱟᱲᱦᱟᱣ ᱢᱮᱱᱟᱜ ᱟ", "ale parhaw menag a"],
    ["They are playing", "ᱩᱱᱠᱩ ᱮᱱᱮᱡ ᱢᱮᱱᱟᱜ ᱟ", "unku enej menag a"],
    ["I am writing", "ᱤᱧ ᱚᱞ ᱢᱮᱱᱟᱜ ᱟ", "inj ol menag a"],
    ["The children are singing", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱥᱮᱨᱮᱧ ᱢᱮᱱᱟᱜ ᱟ", "gidra ko sereny menag a"],
    ["Mother is making tea", "ᱟᱭᱚ ᱪᱟᱹ ᱛᱮᱭᱟᱨ ᱢᱮᱱᱟᱜ ᱟ", "ayo cha teyar menag a"],
    ["Father is working", "ᱟᱯᱟ ᱠᱟᱹᱢᱤ ᱢᱮᱱᱟᱜ ᱟ", "apa kami menag a"],
    ["It is raining", "ᱫᱟᱜ ᱫᱟᱹᱲ ᱢᱮᱱᱟᱜ ᱟ", "dag dar menag a"],
    ["The bird is flying", "ᱪᱮᱨᱮ ᱩᱰᱟᱹᱣ ᱢᱮᱱᱟᱜ ᱟ", "cere udaw menag a"],
    ["I am listening to music", "ᱤᱧ ᱥᱮᱨᱮᱧ ᱟᱹᱭᱠᱟᱹᱣ ᱢᱮᱱᱟᱜ ᱟ", "inj sereny aykaw menag a"],
    ["They are walking", "ᱩᱱᱠᱩ ᱥᱟᱞᱟᱜ ᱢᱮᱱᱟᱜ ᱟ", "unku salag menag a"],
    ["She is sleeping", "ᱩᱱᱤ ᱧᱤᱫ ᱢᱮᱱᱟᱜ ᱟ", "uni nyid menag a"],
    ["I am drinking water", "ᱤᱧ ᱫᱟᱜ ᱧᱩ ᱢᱮᱱᱟᱜ ᱟ", "inj dag nyu menag a"],
    ["The dog is barking", "ᱥᱮᱛᱟ ᱦᱩᱠ ᱢᱮᱱᱟᱜ ᱟ", "seta huk menag a"],
    ["We are waiting", "ᱟᱞᱮ ᱡᱚᱜᱟᱹᱣ ᱢᱮᱱᱟᱜ ᱟ", "ale jogaw menag a"]
]

# 516 - Simple Future Tense
LESSONS[516] = [
    ["I will go", "ᱤᱧ ᱥᱮᱱ ᱟ", "inj sen a"],
    ["You will eat", "ᱟᱢ ᱡᱚᱢ ᱟᱢ", "am jom am"],
    ["He will come", "ᱩᱱᱤ ᱦᱤᱡᱩᱜ ᱟ", "uni hijug a"],
    ["She will cook", "ᱩᱱᱤ ᱨᱟᱸᱰᱷᱟ ᱮ", "uni randha e"],
    ["We will study", "ᱟᱞᱮ ᱯᱟᱲᱦᱟᱣ ᱟᱞᱮ", "ale parhaw ale"],
    ["They will play", "ᱩᱱᱠᱩ ᱮᱱᱮᱡ ᱟᱠᱟᱫᱟ", "unku enej akada"],
    ["I will write a letter", "ᱤᱧ ᱪᱤᱴᱷᱤ ᱚᱞ ᱟ", "inj chithi ol a"],
    ["I will go to the market tomorrow", "ᱤᱧ ᱜᱟᱯᱟ ᱵᱟᱡᱟᱨ ᱥᱮᱱ ᱟ", "inj gapa bajar sen a"],
    ["She will buy vegetables", "ᱩᱱᱤ ᱥᱟᱜ ᱠᱤᱱ ᱮ", "uni sag kin e"],
    ["Father will return home", "ᱟᱯᱟ ᱚᱲᱟᱜ ᱨᱩᱣᱟᱹᱲ ᱮ", "apa orag ruwar e"],
    ["The train will come at 5 o'clock", "ᱜᱟᱰᱤ ᱢᱚᱬᱮ ᱵᱮᱞᱟ ᱨᱮ ᱦᱤᱡᱩᱜ ᱟ", "gadi mone bela re hijug a"],
    ["I will speak in Santali", "ᱤᱧ ᱥᱟᱱᱛᱟᱲᱤ ᱨᱮ ᱨᱚᱲ ᱟ", "inj santari re ror a"],
    ["We will celebrate the festival", "ᱟᱞᱮ ᱯᱚᱨᱚᱵ ᱢᱟᱱᱟᱣ ᱟᱞᱮ", "ale porob manaw ale"],
    ["Children will go to school", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱥᱠᱩᱞ ᱥᱮᱱ ᱟᱠᱟᱫᱟ", "gidra ko skul sen akada"],
    ["It will rain tomorrow", "ᱜᱟᱯᱟ ᱫᱟᱜ ᱫᱟᱹᱲ ᱟ", "gapa dag dar a"],
    ["I will call you", "ᱤᱧ ᱟᱢ ᱠᱮ ᱠᱩᱞ ᱟ", "inj am ke kul a"],
    ["He will help me", "ᱩᱱᱤ ᱤᱧ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱮ", "uni inj ke sagay e"],
    ["We will meet again", "ᱟᱞᱮ ᱟᱨ ᱢᱤᱫ ᱫᱤᱱ ᱧᱮᱞᱚᱜ ᱟᱞᱮ", "ale ar mid din nyelog ale"]
]

# 517 - Future Continuous Tense
LESSONS[517] = [
    ["I will be going", "ᱤᱧ ᱥᱮᱱ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj sen taheny a"],
    ["You will be eating", "ᱟᱢ ᱡᱚᱢ ᱛᱟᱦᱮᱸᱱ ᱟᱢ", "am jom taheny am"],
    ["He will be studying", "ᱩᱱᱤ ᱯᱟᱲᱦᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni parhaw taheny e"],
    ["She will be cooking", "ᱩᱱᱤ ᱨᱟᱸᱰᱷᱟ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni randha taheny e"],
    ["We will be working", "ᱟᱞᱮ ᱠᱟᱹᱢᱤ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale kami taheny ale"],
    ["They will be playing", "ᱩᱱᱠᱩ ᱮᱱᱮᱡ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "unku enej taheny ko"],
    ["I will be waiting for you", "ᱤᱧ ᱟᱢ ᱠᱮ ᱡᱚᱜᱟᱹᱣ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj am ke jogaw taheny a"],
    ["She will be singing at the festival", "ᱩᱱᱤ ᱯᱚᱨᱚᱵ ᱨᱮ ᱥᱮᱨᱮᱧ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni porob re sereny taheny e"],
    ["Father will be resting", "ᱟᱯᱟ ᱥᱮᱨᱮᱧ ᱛᱟᱦᱮᱸᱱ ᱮ", "apa sereny taheny e"],
    ["The children will be sleeping", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱧᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "gidra ko nyid taheny ko"],
    ["I will be writing all day", "ᱤᱧ ᱥᱟᱹᱨᱟᱹ ᱫᱤᱱ ᱚᱞ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj sara din ol taheny a"],
    ["We will be celebrating", "ᱟᱞᱮ ᱢᱟᱱᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale manaw taheny ale"],
    ["He will be sitting there", "ᱩᱱᱤ ᱚᱱᱫᱮ ᱫᱩᱲᱩᱵ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni onde durub taheny e"],
    ["I will be reading this book", "ᱤᱧ ᱱᱚᱣᱟ ᱯᱩᱛᱷᱤ ᱯᱟᱲᱦᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj nowa puthi parhaw taheny a"],
    ["They will be dancing", "ᱩᱱᱠᱩ ᱮᱱᱮᱡ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "unku enej taheny ko"],
    ["Mother will be preparing food", "ᱟᱭᱚ ᱡᱚᱢ ᱛᱮᱭᱟᱨ ᱛᱟᱦᱮᱸᱱ ᱮ", "ayo jom teyar taheny e"],
    ["You will be learning Santali", "ᱟᱢ ᱥᱟᱱᱛᱟᱲᱤ ᱥᱮᱪᱮᱫ ᱛᱟᱦᱮᱸᱱ ᱟᱢ", "am santari seced taheny am"],
    ["She will be watching", "ᱩᱱᱤ ᱧᱮᱞ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni nyel taheny e"]
]

# 518 - Simple Past Tense Part 1 (Verbs without object)
LESSONS[518] = [
    ["I went", "ᱤᱧ ᱥᱮᱱ ᱮᱱᱟ", "inj sen ena"],
    ["You came", "ᱟᱢ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "am hijug ena"],
    ["He ran", "ᱩᱱᱤ ᱫᱟᱹᱲ ᱮᱱᱟ", "uni dar ena"],
    ["She slept", "ᱩᱱᱤ ᱧᱤᱫ ᱮᱱᱟ", "uni nyid ena"],
    ["We sat", "ᱟᱞᱮ ᱫᱩᱲᱩᱵ ᱮᱱᱟ", "ale durub ena"],
    ["They stood", "ᱩᱱᱠᱩ ᱛᱤᱧᱜᱩ ᱮᱱᱟ", "unku tingu ena"],
    ["I woke up", "ᱤᱧ ᱪᱟᱹᱞᱩ ᱮᱱᱟ", "inj chalu ena"],
    ["She fell down", "ᱩᱱᱤ ᱩᱭᱩᱜ ᱮᱱᱟ", "uni uyug ena"],
    ["He laughed", "ᱩᱱᱤ ᱞᱟᱸᱫᱟ ᱮᱱᱟ", "uni landa ena"],
    ["I cried", "ᱤᱧ ᱨᱟᱹᱢ ᱮᱱᱟ", "inj ram ena"],
    ["We walked", "ᱟᱞᱮ ᱥᱟᱞᱟᱜ ᱮᱱᱟ", "ale salag ena"],
    ["They danced", "ᱩᱱᱠᱩ ᱮᱱᱮᱡ ᱮᱱᱟ", "unku enej ena"],
    ["I returned home", "ᱤᱧ ᱚᱲᱟᱜ ᱨᱩᱣᱟᱹᱲ ᱮᱱᱟ", "inj orag ruwar ena"],
    ["He arrived yesterday", "ᱩᱱᱤ ᱜᱟᱞᱟ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "uni gala hijug ena"],
    ["The bird flew away", "ᱪᱮᱨᱮ ᱩᱰᱟᱹᱣ ᱮᱱᱟ", "cere udaw ena"],
    ["She sang", "ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱮᱱᱟ", "uni sereny ena"],
    ["I bathed", "ᱤᱧ ᱡᱩ ᱮᱱᱟ", "inj ju ena"],
    ["They left", "ᱩᱱᱠᱩ ᱪᱟᱞᱟᱜ ᱮᱱᱟ", "unku chalag ena"]
]

# 519 - Simple Past Tense Part 2 (Verbs with object)
LESSONS[519] = [
    ["I ate rice", "ᱤᱧ ᱫᱟᱹᱠ ᱡᱚᱢ ᱮᱱᱟ", "inj dak jom ena"],
    ["You drank water", "ᱟᱢ ᱫᱟᱜ ᱧᱩ ᱮᱱᱟ", "am dag nyu ena"],
    ["He read the book", "ᱩᱱᱤ ᱯᱩᱛᱷᱤ ᱯᱟᱲᱦᱟᱣ ᱮᱱᱟ", "uni puthi parhaw ena"],
    ["She wrote a letter", "ᱩᱱᱤ ᱪᱤᱴᱷᱤ ᱚᱞ ᱮᱱᱟ", "uni chithi ol ena"],
    ["I bought vegetables", "ᱤᱧ ᱥᱟᱜ ᱠᱤᱱ ᱮᱱᱟ", "inj sag kin ena"],
    ["He saw the bird", "ᱩᱱᱤ ᱪᱮᱨᱮ ᱧᱮᱞ ᱮᱱᱟ", "uni cere nyel ena"],
    ["She cooked food", "ᱩᱱᱤ ᱡᱚᱢ ᱨᱟᱸᱰᱷᱟ ᱮᱱᱟ", "uni jom randha ena"],
    ["We heard the song", "ᱟᱞᱮ ᱥᱮᱨᱮᱧ ᱟᱹᱭᱠᱟᱹᱣ ᱮᱱᱟ", "ale sereny aykaw ena"],
    ["They built a house", "ᱩᱱᱠᱩ ᱚᱲᱟᱜ ᱛᱮᱭᱟᱨ ᱮᱱᱟ", "unku orag teyar ena"],
    ["I gave him money", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱴᱟᱠᱟ ᱮᱢ ᱮᱱᱟ", "inj uni ke taka em ena"],
    ["She brought fruits", "ᱩᱱᱤ ᱥᱤᱨᱢᱟ ᱟᱹᱜᱩ ᱮᱱᱟ", "uni sirma agu ena"],
    ["He called his friend", "ᱩᱱᱤ ᱩᱱᱤᱭᱟᱜ ᱥᱟᱶᱛᱟ ᱠᱮ ᱠᱩᱞ ᱮᱱᱟ", "uni uniag sawta ke kul ena"],
    ["I told the truth", "ᱤᱧ ᱥᱟᱹᱨᱤ ᱨᱚᱲ ᱮᱱᱟ", "inj sari ror ena"],
    ["Mother made tea", "ᱟᱭᱚ ᱪᱟᱹ ᱛᱮᱭᱟᱨ ᱮᱱᱟ", "ayo cha teyar ena"],
    ["Father brought fish", "ᱟᱯᱟ ᱢᱟᱹᱪᱷᱟ ᱟᱹᱜᱩ ᱮᱱᱟ", "apa machha agu ena"],
    ["We planted trees", "ᱟᱞᱮ ᱫᱟᱨᱮ ᱛᱟᱞᱟ ᱮᱱᱟ", "ale dare tala ena"],
    ["He took the pen", "ᱩᱱᱤ ᱠᱟᱞᱟᱢ ᱤᱫᱤ ᱮᱱᱟ", "uni kalam idi ena"],
    ["She opened the door", "ᱩᱱᱤ ᱫᱩᱣᱟᱹᱨ ᱡᱷᱤᱡ ᱮᱱᱟ", "uni duwar jhij ena"]
]

# 520 - Simple Past Tense Part 3 (Past tense of "to be")
LESSONS[520] = [
    ["I was a student", "ᱤᱧ ᱢᱤᱫ ᱪᱟᱴᱟᱨ ᱛᱟᱦᱮᱸᱱ ᱠᱟᱱᱟ", "inj mid chatar taheny kana"],
    ["You were at home", "ᱟᱢ ᱚᱲᱟᱜ ᱨᱮ ᱛᱟᱦᱮᱸᱱ ᱟᱢ", "am orag re taheny am"],
    ["He was a farmer", "ᱩᱱᱤ ᱢᱤᱫ ᱨᱟᱹᱭᱡ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni mid rayj taheny e"],
    ["She was happy", "ᱩᱱᱤ ᱨᱟᱹᱥᱠᱟᱹ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni raska taheny e"],
    ["We were in the village", "ᱟᱞᱮ ᱟᱹᱛᱩ ᱨᱮ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale atu re taheny ale"],
    ["They were good friends", "ᱩᱱᱠᱩ ᱵᱷᱟᱞᱮ ᱥᱟᱶᱛᱟ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "unku bhale sawta taheny ko"],
    ["It was cold yesterday", "ᱜᱟᱞᱟ ᱫᱷᱤᱨᱤ ᱛᱟᱦᱮᱸᱱ ᱟ", "gala dhiri taheny a"],
    ["The food was hot", "ᱡᱚᱢ ᱫᱩᱨᱩᱵ ᱛᱟᱦᱮᱸᱱ ᱟ", "jom durub taheny a"],
    ["The road was long", "ᱨᱟᱦᱟ ᱡᱟᱱᱟᱝ ᱛᱟᱦᱮᱸᱱ ᱟ", "raha janang taheny a"],
    ["I was tired", "ᱤᱧ ᱛᱷᱟᱠᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj thakaw taheny a"],
    ["She was a teacher", "ᱩᱱᱤ ᱢᱤᱫ ᱯᱟᱲᱦᱟᱣᱮᱫ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni mid parhawed taheny e"],
    ["The tree was tall", "ᱫᱟᱨᱮ ᱡᱟᱱᱟᱝ ᱛᱟᱦᱮᱸᱱ ᱟ", "dare janang taheny a"],
    ["My house was small", "ᱤᱧᱟᱜ ᱚᱲᱟᱜ ᱦᱩᱰᱤᱧ ᱛᱟᱦᱮᱸᱱ ᱟ", "injag orag huding taheny a"],
    ["That day was special", "ᱚᱱᱟ ᱫᱤᱱ ᱵᱷᱟᱞᱮ ᱛᱟᱦᱮᱸᱱ ᱟ", "ona din bhale taheny a"],
    ["The festival was beautiful", "ᱯᱚᱨᱚᱵ ᱥᱚᱢᱵᱷᱟᱨ ᱛᱟᱦᱮᱸᱱ ᱟ", "porob sombhar taheny a"],
    ["We were brothers", "ᱟᱞᱮ ᱦᱟᱯᱲᱟᱢ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale hapram taheny ale"],
    ["The water was clean", "ᱫᱟᱜ ᱥᱟᱯᱷᱟ ᱛᱟᱦᱮᱸᱱ ᱟ", "dag sapha taheny a"],
    ["It was morning", "ᱥᱮᱛᱟᱜ ᱛᱟᱦᱮᱸᱱ ᱟ", "setag taheny a"]
]

# 521 - Exceptional Verbs
LESSONS[521] = [
    ["I know (verb changes)", "ᱤᱧ ᱵᱟᱰᱟᱭ ᱟ", "inj baday a"],
    ["I knew", "ᱤᱧ ᱵᱟᱰᱟᱭ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj baday taheny a"],
    ["I get / receive", "ᱤᱧ ᱧᱟᱢ ᱟᱭᱟ", "inj nyam aya"],
    ["I got / received", "ᱤᱧ ᱧᱟᱢ ᱮᱱᱟ", "inj nyam ena"],
    ["I make / do", "ᱤᱧ ᱠᱟᱹᱢᱤ ᱠᱮᱫ ᱟᱭᱟ", "inj kami ked aya"],
    ["I made / did", "ᱤᱧ ᱠᱟᱹᱢᱤ ᱠᱮᱫ ᱮᱱᱟ", "inj kami ked ena"],
    ["I understand", "ᱤᱧ ᱵᱩᱡᱷᱟᱹᱣ ᱟᱭᱟ", "inj bujhaw aya"],
    ["I understood", "ᱤᱧ ᱵᱩᱡᱷᱟᱹᱣ ᱮᱱᱟ", "inj bujhaw ena"],
    ["I think", "ᱤᱧ ᱢᱚᱱᱮ ᱠᱮᱫ ᱟᱭᱟ", "inj mone ked aya"],
    ["I thought", "ᱤᱧ ᱢᱚᱱᱮ ᱠᱮᱫ ᱮᱱᱟ", "inj mone ked ena"],
    ["I want", "ᱤᱧ ᱥᱟᱱᱟᱢ ᱟ", "inj sanam a"],
    ["I wanted", "ᱤᱧ ᱥᱟᱱᱟᱢ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj sanam taheny a"],
    ["I say / tell", "ᱤᱧ ᱨᱚᱲ ᱟᱭᱟ", "inj ror aya"],
    ["I said / told", "ᱤᱧ ᱨᱚᱲ ᱮᱱᱟ", "inj ror ena"],
    ["He can do", "ᱩᱱᱤ ᱫᱟᱲᱮ ᱮ", "uni dare e"],
    ["He could do", "ᱩᱱᱤ ᱫᱟᱲᱮ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni dare taheny e"],
    ["She remembers", "ᱩᱱᱤ ᱩᱢ ᱟᱫ ᱮ", "uni um ad e"],
    ["She remembered", "ᱩᱱᱤ ᱩᱢ ᱮᱱᱟ", "uni um ena"]
]

# 522 - Past Continuous Tense
LESSONS[522] = [
    ["I was going", "ᱤᱧ ᱥᱮᱱ ᱛᱟᱦᱮᱸᱱ ᱟᱭᱟ", "inj sen taheny aya"],
    ["You were eating", "ᱟᱢ ᱡᱚᱢ ᱛᱟᱦᱮᱸᱱ ᱟᱢ", "am jom taheny am"],
    ["He was reading", "ᱩᱱᱤ ᱯᱟᱲᱦᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni parhaw taheny e"],
    ["She was cooking", "ᱩᱱᱤ ᱨᱟᱸᱰᱷᱟ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni randha taheny e"],
    ["We were playing", "ᱟᱞᱮ ᱮᱱᱮᱡ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale enej taheny ale"],
    ["They were singing", "ᱩᱱᱠᱩ ᱥᱮᱨᱮᱧ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "unku sereny taheny ko"],
    ["I was sleeping when you came", "ᱟᱢ ᱦᱤᱡᱩᱜ ᱵᱮᱞᱟ ᱤᱧ ᱧᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱟ", "am hijug bela inj nyid taheny a"],
    ["It was raining heavily", "ᱫᱟᱜ ᱟᱹᱰᱤ ᱫᱟᱹᱲ ᱛᱟᱦᱮᱸᱱ ᱟ", "dag adi dar taheny a"],
    ["Mother was calling me", "ᱟᱭᱚ ᱤᱧ ᱠᱮ ᱠᱩᱞ ᱛᱟᱦᱮᱸᱱ ᱮ", "ayo inj ke kul taheny e"],
    ["Father was working in the field", "ᱟᱯᱟ ᱜᱟᱰᱟ ᱨᱮ ᱠᱟᱹᱢᱤ ᱛᱟᱦᱮᱸᱱ ᱮ", "apa gada re kami taheny e"],
    ["Children were studying", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱯᱟᱲᱦᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "gidra ko parhaw taheny ko"],
    ["The wind was blowing", "ᱦᱚᱭᱚ ᱪᱟᱞᱟᱜ ᱛᱟᱦᱮᱸᱱ ᱟ", "hoyo chalag taheny a"],
    ["She was waiting for me", "ᱩᱱᱤ ᱤᱧ ᱠᱮ ᱡᱚᱜᱟᱹᱣ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni inj ke jogaw taheny e"],
    ["I was writing a story", "ᱤᱧ ᱠᱟᱹᱦᱱᱤ ᱚᱞ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj kahni ol taheny a"],
    ["He was sitting under the tree", "ᱩᱱᱤ ᱫᱟᱨᱮ ᱞᱟᱛᱟᱨ ᱫᱩᱲᱩᱵ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni dare latar durub taheny e"],
    ["Birds were chirping", "ᱪᱮᱨᱮ ᱠᱚ ᱫᱟᱸᱜ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "cere ko dang taheny ko"],
    ["We were walking on the road", "ᱟᱞᱮ ᱨᱟᱦᱟ ᱨᱮ ᱥᱟᱞᱟᱜ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale raha re salag taheny ale"],
    ["The dog was barking", "ᱥᱮᱛᱟ ᱦᱩᱠ ᱛᱟᱦᱮᱸᱱ ᱮ", "seta huk taheny e"]
]

# 523 - Present/Past/Future Perfect Tense
LESSONS[523] = [
    ["I have eaten", "ᱤᱧ ᱡᱚᱢ ᱮᱱᱟ", "inj jom ena"],
    ["You have come", "ᱟᱢ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "am hijug ena"],
    ["He has gone", "ᱩᱱᱤ ᱥᱮᱱ ᱮᱱᱟ", "uni sen ena"],
    ["She has finished cooking", "ᱩᱱᱤ ᱨᱟᱸᱰᱷᱟ ᱛᱮᱭᱟᱨ ᱮᱱᱟ", "uni randha teyar ena"],
    ["We have studied", "ᱟᱞᱮ ᱯᱟᱲᱦᱟᱣ ᱮᱱᱟ", "ale parhaw ena"],
    ["I had eaten before he came", "ᱩᱱᱤ ᱦᱤᱡᱩᱜ ᱥᱤᱫ ᱤᱧ ᱡᱚᱢ ᱮᱱ ᱛᱟᱦᱮᱸᱱ ᱟ", "uni hijug sid inj jom en taheny a"],
    ["She had already left", "ᱩᱱᱤ ᱟᱫᱚ ᱥᱮᱱ ᱮᱱ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni ado sen en taheny e"],
    ["They had finished the work", "ᱩᱱᱠᱩ ᱠᱟᱹᱢᱤ ᱛᱮᱭᱟᱨ ᱮᱱ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "unku kami teyar en taheny ko"],
    ["I will have finished", "ᱤᱧ ᱛᱮᱭᱟᱨ ᱮᱱ ᱟ", "inj teyar en a"],
    ["She will have cooked by then", "ᱚᱱᱟ ᱵᱮᱞᱟ ᱨᱮ ᱩᱱᱤ ᱨᱟᱸᱰᱷᱟ ᱛᱮᱭᱟᱨ ᱮᱱ ᱮ", "ona bela re uni randha teyar en e"],
    ["I have written the letter", "ᱤᱧ ᱪᱤᱴᱷᱤ ᱚᱞ ᱮᱱᱟ", "inj chithi ol ena"],
    ["He has read the book", "ᱩᱱᱤ ᱯᱩᱛᱷᱤ ᱯᱟᱲᱦᱟᱣ ᱮᱱᱟ", "uni puthi parhaw ena"],
    ["We have built a house", "ᱟᱞᱮ ᱚᱲᱟᱜ ᱛᱮᱭᱟᱨ ᱮᱱᱟ", "ale orag teyar ena"],
    ["She has bought clothes", "ᱩᱱᱤ ᱠᱟᱹᱯᱲᱟ ᱠᱤᱱ ᱮᱱᱟ", "uni kapra kin ena"],
    ["They have planted trees", "ᱩᱱᱠᱩ ᱫᱟᱨᱮ ᱛᱟᱞᱟ ᱮᱱᱟ", "unku dare tala ena"],
    ["I had seen that movie", "ᱤᱧ ᱚᱱᱟ ᱮᱱᱮᱡ ᱧᱮᱞ ᱮᱱ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj ona enej nyel en taheny a"],
    ["He will have arrived by morning", "ᱥᱮᱛᱟᱜ ᱥᱤᱫ ᱩᱱᱤ ᱦᱤᱡᱩᱜ ᱮᱱ ᱮ", "setag sid uni hijug en e"],
    ["We have learned Santali", "ᱟᱞᱮ ᱥᱟᱱᱛᱟᱲᱤ ᱥᱮᱪᱮᱫ ᱮᱱᱟ", "ale santari seced ena"]
]

# 524 - Prepositions
LESSONS[524] = [
    ["In the house", "ᱚᱲᱟᱜ ᱨᱮ", "orag re"],
    ["On the table", "ᱴᱮᱵᱩᱞ ᱪᱮᱛᱟᱱ ᱨᱮ", "tebul cetan re"],
    ["Under the tree", "ᱫᱟᱨᱮ ᱞᱟᱛᱟᱨ ᱨᱮ", "dare latar re"],
    ["Near the river", "ᱜᱟᱰᱟ ᱱᱮᱰᱟ ᱨᱮ", "gada neda re"],
    ["Far from home", "ᱚᱲᱟᱜ ᱠᱷᱚᱱ ᱫᱩᱨ", "orag khon dur"],
    ["Behind the school", "ᱥᱠᱩᱞ ᱯᱤᱪᱷᱟ ᱨᱮ", "skul pichha re"],
    ["In front of the shop", "ᱫᱚᱠᱟᱱ ᱥᱟᱹᱢᱟᱹᱝ ᱨᱮ", "dokan samang re"],
    ["With my friend", "ᱤᱧᱟᱜ ᱥᱟᱶᱛᱟ ᱥᱟᱶ", "injag sawta saw"],
    ["From the village", "ᱟᱹᱛᱩ ᱠᱷᱚᱱ", "atu khon"],
    ["To the market", "ᱵᱟᱡᱟᱨ ᱛᱮ", "bajar te"],
    ["Between two hills", "ᱵᱟᱨ ᱵᱩᱨᱩ ᱛᱟᱞᱟ ᱨᱮ", "bar buru tala re"],
    ["Above the cloud", "ᱨᱤᱢᱤᱞ ᱪᱮᱛᱟᱱ ᱨᱮ", "rimil cetan re"],
    ["Beside the road", "ᱨᱟᱦᱟ ᱜᱚᱲᱟ ᱨᱮ", "raha gora re"],
    ["Inside the box", "ᱵᱟᱠᱥᱚ ᱵᱷᱤᱛᱤᱨ ᱨᱮ", "bakso bhitir re"],
    ["Outside the room", "ᱠᱚᱴᱷᱟ ᱵᱟᱦᱨᱮ", "kotha bahre"],
    ["Around the village", "ᱟᱹᱛᱩ ᱜᱚᱲᱟ ᱨᱮ", "atu gora re"],
    ["Towards the forest", "ᱵᱤᱨ ᱛᱮ", "bir te"],
    ["For my father", "ᱤᱧᱟᱜ ᱟᱯᱟ ᱞᱟᱜᱤᱫ", "injag apa lagid"]
]

# 525 - Preposition "TO"
LESSONS[525] = [
    ["I go to school", "ᱤᱧ ᱥᱠᱩᱞ ᱛᱮ ᱥᱮᱱ ᱟᱭᱟ", "inj skul te sen aya"],
    ["Come to me", "ᱤᱧ ᱛᱮ ᱦᱤᱡᱩᱜ ᱢᱮ", "inj te hijug me"],
    ["Give it to him", "ᱩᱱᱤ ᱠᱮ ᱮᱢ ᱢᱮ", "uni ke em me"],
    ["I said to her", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱨᱚᱲ ᱮᱱᱟ", "inj uni ke ror ena"],
    ["Go to the market", "ᱵᱟᱡᱟᱨ ᱛᱮ ᱥᱮᱱ ᱢᱮ", "bajar te sen me"],
    ["Talk to father", "ᱟᱯᱟ ᱥᱟᱶ ᱨᱚᱲ ᱢᱮ", "apa saw ror me"],
    ["Listen to me", "ᱤᱧᱟᱜ ᱠᱟᱹᱛᱷᱟ ᱟᱹᱭᱠᱟᱹᱣ ᱢᱮ", "injag katha aykaw me"],
    ["I walked to the river", "ᱤᱧ ᱜᱟᱰᱟ ᱛᱮ ᱥᱟᱞᱟᱜ ᱮᱱᱟ", "inj gada te salag ena"],
    ["Write to me", "ᱤᱧ ᱛᱮ ᱚᱞ ᱢᱮ", "inj te ol me"],
    ["She went to the hospital", "ᱩᱱᱤ ᱦᱟᱥᱯᱟᱛᱟᱞ ᱛᱮ ᱥᱮᱱ ᱮᱱᱟ", "uni haspatal te sen ena"],
    ["I want to go home", "ᱤᱧ ᱚᱲᱟᱜ ᱥᱮᱱ ᱥᱟᱱᱟᱢ ᱟ", "inj orag sen sanam a"],
    ["Bring water to me", "ᱤᱧ ᱞᱟᱜᱤᱫ ᱫᱟᱜ ᱟᱹᱜᱩ ᱢᱮ", "inj lagid dag agu me"],
    ["He went to Delhi", "ᱩᱱᱤ ᱫᱤᱞᱞᱤ ᱛᱮ ᱥᱮᱱ ᱮᱱᱟ", "uni Dilli te sen ena"],
    ["Call to everyone", "ᱡᱚᱛᱚ ᱠᱮ ᱠᱩᱞ ᱢᱮ", "joto ke kul me"],
    ["Send it to the village", "ᱟᱹᱛᱩ ᱛᱮ ᱯᱟᱴᱷᱟᱣ ᱢᱮ", "atu te pathaw me"],
    ["I spoke to the teacher", "ᱤᱧ ᱯᱟᱲᱦᱟᱣᱮᱫ ᱥᱟᱶ ᱨᱚᱲ ᱮᱱᱟ", "inj parhawed saw ror ena"],
    ["Please come to my house", "ᱤᱧᱟᱜ ᱚᱲᱟᱜ ᱛᱮ ᱦᱤᱡᱩᱜ ᱢᱮ", "injag orag te hijug me"],
    ["I want to learn Santali", "ᱤᱧ ᱥᱟᱱᱛᱟᱲᱤ ᱥᱮᱪᱮᱫ ᱥᱟᱱᱟᱢ ᱟ", "inj santari seced sanam a"]
]

# 526 - Sentences with person/living things as object
LESSONS[526] = [
    ["I saw him", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱧᱮᱞ ᱮᱱᱟ", "inj uni ke nyel ena"],
    ["He called me", "ᱩᱱᱤ ᱤᱧ ᱠᱮ ᱠᱩᱞ ᱮᱱᱟ", "uni inj ke kul ena"],
    ["She helped them", "ᱩᱱᱤ ᱩᱱᱠᱩ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱮᱱᱟ", "uni unku ke sagay ena"],
    ["I told her", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱨᱚᱲ ᱮᱱᱟ", "inj uni ke ror ena"],
    ["He loves his mother", "ᱩᱱᱤ ᱩᱱᱤᱭᱟᱜ ᱟᱭᱚ ᱠᱮ ᱫᱩᱞᱟᱹᱲ ᱟᱫ ᱮ", "uni uniag ayo ke dular ad e"],
    ["We met the teacher", "ᱟᱞᱮ ᱯᱟᱲᱦᱟᱣᱮᱫ ᱠᱮ ᱧᱮᱞ ᱮᱱᱟ", "ale parhawed ke nyel ena"],
    ["She fed the child", "ᱩᱱᱤ ᱜᱤᱫᱽᱨᱟᱹ ᱠᱮ ᱡᱚᱢ ᱮᱢ ᱮᱱᱟ", "uni gidra ke jom em ena"],
    ["I gave him the book", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱯᱩᱛᱷᱤ ᱮᱢ ᱮᱱᱟ", "inj uni ke puthi em ena"],
    ["He asked me", "ᱩᱱᱤ ᱤᱧ ᱠᱮ ᱠᱩᱞᱤ ᱮᱱᱟ", "uni inj ke kuli ena"],
    ["She hit the dog", "ᱩᱱᱤ ᱥᱮᱛᱟ ᱠᱮ ᱫᱟᱹᱲ ᱮᱱᱟ", "uni seta ke dar ena"],
    ["Mother woke the children", "ᱟᱭᱚ ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱠᱮ ᱪᱟᱹᱞᱩ ᱮᱱᱟ", "ayo gidra ko ke chalu ena"],
    ["Father taught us", "ᱟᱯᱟ ᱟᱞᱮ ᱠᱮ ᱯᱟᱲᱦᱟᱣ ᱮᱱᱟ", "apa ale ke parhaw ena"],
    ["I invited my friends", "ᱤᱧ ᱤᱧᱟᱜ ᱥᱟᱶᱛᱟ ᱠᱚ ᱠᱮ ᱠᱩᱞ ᱮᱱᱟ", "inj injag sawta ko ke kul ena"],
    ["He recognized me", "ᱩᱱᱤ ᱤᱧ ᱠᱮ ᱪᱤᱱᱷᱟᱹ ᱮᱱᱟ", "uni inj ke cinha ena"],
    ["They greeted the elder", "ᱩᱱᱠᱩ ᱢᱟᱨᱟᱝ ᱦᱚᱲ ᱠᱮ ᱡᱚᱦᱟᱨ ᱮᱱᱟ", "unku marang hor ke johar ena"],
    ["She brought the child", "ᱩᱱᱤ ᱜᱤᱫᱽᱨᱟᱹ ᱠᱮ ᱟᱹᱜᱩ ᱮᱱᱟ", "uni gidra ke agu ena"],
    ["We welcomed the guests", "ᱟᱞᱮ ᱨᱟᱹᱥᱤᱭᱟᱹ ᱠᱚ ᱠᱮ ᱡᱚᱦᱟᱨ ᱮᱱᱟ", "ale rasiya ko ke johar ena"],
    ["I trust you", "ᱤᱧ ᱟᱢ ᱠᱮ ᱵᱷᱟᱨᱥᱟ ᱠᱮᱫ ᱟᱭᱟ", "inj am ke bharsa ked aya"]
]

# 527 - Saying My/His/Her
LESSONS[527] = [
    ["My house", "ᱤᱧᱟᱜ ᱚᱲᱟᱜ", "injag orag"],
    ["Your book", "ᱟᱢᱟᱜ ᱯᱩᱛᱷᱤ", "amag puthi"],
    ["His/Her name", "ᱩᱱᱤᱭᱟᱜ ᱧᱩᱛᱩᱢ", "uniag nyutum"],
    ["Our village", "ᱟᱞᱮᱭᱟᱜ ᱟᱹᱛᱩ", "aleyag atu"],
    ["Their country", "ᱩᱱᱠᱩᱭᱟᱜ ᱫᱤᱥᱚᱢ", "unkuag disom"],
    ["My mother", "ᱤᱧᱟᱜ ᱟᱭᱚ", "injag ayo"],
    ["Your father", "ᱟᱢᱟᱜ ᱟᱯᱟ", "amag apa"],
    ["His friend", "ᱩᱱᱤᱭᱟᱜ ᱥᱟᱶᱛᱟ", "uniag sawta"],
    ["My school", "ᱤᱧᱟᱜ ᱥᱠᱩᱞ", "injag skul"],
    ["Your food", "ᱟᱢᱟᱜ ᱡᱚᱢ", "amag jom"],
    ["Her child", "ᱩᱱᱤᱭᱟᱜ ᱜᱤᱫᱽᱨᱟᱹ", "uniag gidra"],
    ["Our teacher", "ᱟᱞᱮᱭᱟᱜ ᱯᱟᱲᱦᱟᱣᱮᱫ", "aleyag parhawed"],
    ["Their song", "ᱩᱱᱠᱩᱭᱟᱜ ᱥᱮᱨᱮᱧ", "unkuag sereny"],
    ["My language", "ᱤᱧᱟᱜ ᱯᱟᱹᱨᱥᱤ", "injag parsi"],
    ["Your money", "ᱟᱢᱟᱜ ᱴᱟᱠᱟ", "amag taka"],
    ["His work", "ᱩᱱᱤᱭᱟᱜ ᱠᱟᱹᱢᱤ", "uniag kami"],
    ["My heart", "ᱤᱧᱟᱜ ᱢᱚᱱᱮ", "injag mone"],
    ["Our festival", "ᱟᱞᱮᱭᱟᱜ ᱯᱚᱨᱚᱵ", "aleyag porob"]
]

# 528 - Basic questions and WH questions
LESSONS[528] = [
    ["What is this?", "ᱱᱚᱣᱟ ᱪᱮᱫ ᱠᱟᱱᱟ?", "nowa ced kana?"],
    ["Who are you?", "ᱟᱢ ᱚᱠᱚᱭ ᱠᱟᱱᱟ?", "am okoy kana?"],
    ["Where is the market?", "ᱵᱟᱡᱟᱨ ᱚᱠᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ?", "bajar oka re menag a?"],
    ["When will you come?", "ᱟᱢ ᱚᱠᱟ ᱫᱤᱱ ᱦᱤᱡᱩᱜ ᱟᱢ?", "am oka din hijug am?"],
    ["Why did you go?", "ᱟᱢ ᱪᱮᱫ ᱞᱟᱜᱤᱫ ᱥᱮᱱ ᱮᱱᱟ?", "am ced lagid sen ena?"],
    ["How are you?", "ᱟᱢ ᱚᱠᱟ ᱠᱟᱱᱟ?", "am oka kana?"],
    ["How much is this?", "ᱱᱚᱣᱟ ᱚᱛᱚ ᱠᱟᱱᱟ?", "nowa oto kana?"],
    ["Which one do you want?", "ᱟᱢ ᱚᱠᱟ ᱥᱟᱱᱟᱢ ᱟᱢ?", "am oka sanam am?"],
    ["Whose book is this?", "ᱱᱚᱣᱟ ᱚᱠᱚᱭᱟᱜ ᱯᱩᱛᱷᱤ ᱠᱟᱱᱟ?", "nowa okoyag puthi kana?"],
    ["How many children are there?", "ᱚᱛᱚ ᱜᱤᱫᱽᱨᱟᱹ ᱢᱮᱱᱟᱜ ᱟ?", "oto gidra menag a?"],
    ["What do you eat?", "ᱟᱢ ᱪᱮᱫ ᱡᱚᱢ ᱟᱢ?", "am ced jom am?"],
    ["Where do you live?", "ᱟᱢ ᱚᱠᱟ ᱨᱮ ᱛᱟᱦᱮᱸᱱ ᱟᱢ?", "am oka re taheny am?"],
    ["Why are you crying?", "ᱟᱢ ᱪᱮᱫ ᱞᱟᱜᱤᱫ ᱨᱟᱹᱢ ᱟᱢ?", "am ced lagid ram am?"],
    ["When did he arrive?", "ᱩᱱᱤ ᱚᱠᱟ ᱫᱤᱱ ᱦᱤᱡᱩᱜ ᱮᱱᱟ?", "uni oka din hijug ena?"],
    ["Who is that person?", "ᱚᱱᱟ ᱦᱚᱲ ᱚᱠᱚᱭ ᱠᱟᱱᱟ?", "ona hor okoy kana?"],
    ["What is your name?", "ᱟᱢᱟᱜ ᱧᱩᱛᱩᱢ ᱪᱮᱫ?", "amag nyutum ced?"],
    ["How do I go there?", "ᱤᱧ ᱚᱱᱫᱮ ᱚᱠᱟ ᱞᱮᱠᱟ ᱥᱮᱱ ᱟ?", "inj onde oka leka sen a?"],
    ["Which village is yours?", "ᱟᱢᱟᱜ ᱟᱹᱛᱩ ᱚᱠᱟ ᱨᱮ?", "amag atu oka re?"]
]

# 529-542 remaining grammar lessons
LESSONS[529] = [
    ["I don't go", "ᱤᱧ ᱵᱟᱝ ᱥᱮᱱ ᱟᱭᱟ", "inj bang sen aya"],
    ["You don't eat", "ᱟᱢ ᱵᱟᱝ ᱡᱚᱢ ᱟᱢ", "am bang jom am"],
    ["He doesn't come", "ᱩᱱᱤ ᱵᱟᱝ ᱦᱤᱡᱩᱜ ᱮ", "uni bang hijug e"],
    ["She doesn't speak Santali", "ᱩᱱᱤ ᱥᱟᱱᱛᱟᱲᱤ ᱵᱟᱝ ᱨᱚᱲ ᱮ", "uni santari bang ror e"],
    ["We don't run", "ᱟᱞᱮ ᱵᱟᱝ ᱫᱟᱹᱲ ᱟᱞᱮ", "ale bang dar ale"],
    ["They don't study", "ᱩᱱᱠᱩ ᱵᱟᱝ ᱯᱟᱲᱦᱟᱣ ᱠᱚ", "unku bang parhaw ko"],
    ["I don't know", "ᱤᱧ ᱵᱟᱝ ᱵᱟᱰᱟᱭ ᱟ", "inj bang baday a"],
    ["She doesn't want tea", "ᱩᱱᱤ ᱪᱟᱹ ᱵᱟᱝ ᱥᱟᱱᱟᱢ ᱮ", "uni cha bang sanam e"],
    ["He doesn't write", "ᱩᱱᱤ ᱵᱟᱝ ᱚᱞ ᱮ", "uni bang ol e"],
    ["I don't understand", "ᱤᱧ ᱵᱟᱝ ᱵᱩᱡᱷᱟᱹᱣ ᱟ", "inj bang bujhaw a"],
    ["The children don't sleep early", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱥᱮᱛᱟᱜ ᱵᱟᱝ ᱧᱤᱫ ᱠᱚ", "gidra ko setag bang nyid ko"],
    ["He doesn't have money", "ᱩᱱᱤᱭᱟᱜ ᱴᱟᱠᱟ ᱵᱟᱝ ᱢᱮᱱᱟᱜ ᱟ", "uniag taka bang menag a"],
    ["I don't like this", "ᱤᱧ ᱱᱚᱣᱟ ᱵᱟᱝ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "inj nowa bang raska a"],
    ["She doesn't cook today", "ᱩᱱᱤ ᱟᱡ ᱵᱟᱝ ᱨᱟᱸᱰᱷᱟ ᱮ", "uni aj bang randha e"],
    ["Father doesn't drink tea", "ᱟᱯᱟ ᱪᱟᱹ ᱵᱟᱝ ᱧᱩ ᱮ", "apa cha bang nyu e"],
    ["We don't fight", "ᱟᱞᱮ ᱵᱟᱝ ᱞᱟᱲᱟᱭ ᱟᱞᱮ", "ale bang laray ale"],
    ["They don't believe", "ᱩᱱᱠᱩ ᱵᱟᱝ ᱵᱷᱟᱨᱥᱟ ᱠᱚ", "unku bang bharsa ko"],
    ["I don't play", "ᱤᱧ ᱵᱟᱝ ᱮᱱᱮᱡ ᱟᱭᱟ", "inj bang enej aya"]
]

LESSONS[530] = [
    ["I didn't go", "ᱤᱧ ᱵᱟᱝ ᱥᱮᱱ ᱮᱱᱟ", "inj bang sen ena"],
    ["You didn't come", "ᱟᱢ ᱵᱟᱝ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "am bang hijug ena"],
    ["He didn't eat", "ᱩᱱᱤ ᱵᱟᱝ ᱡᱚᱢ ᱮᱱᱟ", "uni bang jom ena"],
    ["She didn't study", "ᱩᱱᱤ ᱵᱟᱝ ᱯᱟᱲᱦᱟᱣ ᱮᱱᱟ", "uni bang parhaw ena"],
    ["We didn't play", "ᱟᱞᱮ ᱵᱟᱝ ᱮᱱᱮᱡ ᱮᱱᱟ", "ale bang enej ena"],
    ["They didn't come yesterday", "ᱩᱱᱠᱩ ᱜᱟᱞᱟ ᱵᱟᱝ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "unku gala bang hijug ena"],
    ["I didn't see him", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱵᱟᱝ ᱧᱮᱞ ᱮᱱᱟ", "inj uni ke bang nyel ena"],
    ["She didn't cook", "ᱩᱱᱤ ᱵᱟᱝ ᱨᱟᱸᱰᱷᱟ ᱮᱱᱟ", "uni bang randha ena"],
    ["He didn't write the letter", "ᱩᱱᱤ ᱪᱤᱴᱷᱤ ᱵᱟᱝ ᱚᱞ ᱮᱱᱟ", "uni chithi bang ol ena"],
    ["Father didn't return", "ᱟᱯᱟ ᱵᱟᱝ ᱨᱩᱣᱟᱹᱲ ᱮᱱᱟ", "apa bang ruwar ena"],
    ["Mother didn't call", "ᱟᱭᱚ ᱵᱟᱝ ᱠᱩᱞ ᱮᱱᱟ", "ayo bang kul ena"],
    ["I didn't buy anything", "ᱤᱧ ᱡᱚᱛᱚ ᱵᱟᱝ ᱠᱤᱱ ᱮᱱᱟ", "inj joto bang kin ena"],
    ["The rain didn't stop", "ᱫᱟᱜ ᱵᱟᱝ ᱛᱷᱤᱨ ᱮᱱᱟ", "dag bang thir ena"],
    ["He didn't understand", "ᱩᱱᱤ ᱵᱟᱝ ᱵᱩᱡᱷᱟᱹᱣ ᱮᱱᱟ", "uni bang bujhaw ena"],
    ["We didn't go to school", "ᱟᱞᱮ ᱥᱠᱩᱞ ᱵᱟᱝ ᱥᱮᱱ ᱮᱱᱟ", "ale skul bang sen ena"],
    ["She didn't tell me", "ᱩᱱᱤ ᱤᱧ ᱠᱮ ᱵᱟᱝ ᱨᱚᱲ ᱮᱱᱟ", "uni inj ke bang ror ena"],
    ["They didn't help", "ᱩᱱᱠᱩ ᱵᱟᱝ ᱥᱟᱹᱜᱟᱹᱭ ᱮᱱᱟ", "unku bang sagay ena"],
    ["I didn't sleep well", "ᱤᱧ ᱵᱷᱟᱞᱮ ᱵᱟᱝ ᱧᱤᱫ ᱮᱱᱟ", "inj bhale bang nyid ena"]
]

LESSONS[531] = [
    ["I will not go", "ᱤᱧ ᱵᱟᱝ ᱥᱮᱱ ᱟ", "inj bang sen a"],
    ["You will not come", "ᱟᱢ ᱵᱟᱝ ᱦᱤᱡᱩᱜ ᱟᱢ", "am bang hijug am"],
    ["He will not eat", "ᱩᱱᱤ ᱵᱟᱝ ᱡᱚᱢ ᱮ", "uni bang jom e"],
    ["She will not study", "ᱩᱱᱤ ᱵᱟᱝ ᱯᱟᱲᱦᱟᱣ ᱮ", "uni bang parhaw e"],
    ["We will not run", "ᱟᱞᱮ ᱵᱟᱝ ᱫᱟᱹᱲ ᱟᱞᱮ", "ale bang dar ale"],
    ["They will not work", "ᱩᱱᱠᱩ ᱵᱟᱝ ᱠᱟᱹᱢᱤ ᱠᱚ", "unku bang kami ko"],
    ["I will not forget", "ᱤᱧ ᱵᱟᱝ ᱦᱮᱡ ᱠᱟᱹ ᱟ", "inj bang hej ka a"],
    ["She will not cook today", "ᱩᱱᱤ ᱟᱡ ᱵᱟᱝ ᱨᱟᱸᱰᱷᱟ ᱮ", "uni aj bang randha e"],
    ["He will not call me", "ᱩᱱᱤ ᱤᱧ ᱠᱮ ᱵᱟᱝ ᱠᱩᱞ ᱮ", "uni inj ke bang kul e"],
    ["I will not buy that", "ᱤᱧ ᱚᱱᱟ ᱵᱟᱝ ᱠᱤᱱ ᱟ", "inj ona bang kin a"],
    ["We will not leave", "ᱟᱞᱮ ᱵᱟᱝ ᱪᱟᱞᱟᱜ ᱟᱞᱮ", "ale bang chalag ale"],
    ["Father will not come today", "ᱟᱯᱟ ᱟᱡ ᱵᱟᱝ ᱦᱤᱡᱩᱜ ᱮ", "apa aj bang hijug e"],
    ["The rain will not stop", "ᱫᱟᱜ ᱵᱟᱝ ᱛᱷᱤᱨ ᱟ", "dag bang thir a"],
    ["I will not fight", "ᱤᱧ ᱵᱟᱝ ᱞᱟᱲᱟᱭ ᱟ", "inj bang laray a"],
    ["She will not sell this", "ᱩᱱᱤ ᱱᱚᱣᱟ ᱵᱟᱝ ᱵᱮᱪᱟᱣ ᱮ", "uni nowa bang becaw e"],
    ["They will not sing", "ᱩᱱᱠᱩ ᱵᱟᱝ ᱥᱮᱨᱮᱧ ᱠᱚ", "unku bang sereny ko"],
    ["I will not tell anyone", "ᱤᱧ ᱡᱟᱦᱟᱸ ᱠᱮ ᱵᱟᱝ ᱨᱚᱲ ᱟ", "inj jahang ke bang ror a"],
    ["He will not return tomorrow", "ᱩᱱᱤ ᱜᱟᱯᱟ ᱵᱟᱝ ᱨᱩᱣᱟᱹᱲ ᱮ", "uni gapa bang ruwar e"]
]

LESSONS[532] = [
    ["Boy (male)", "ᱠᱚᱲᱟ", "kora"],
    ["Girl (female)", "ᱠᱩᱲᱤ", "kuri"],
    ["Man", "ᱦᱚᱲ ᱠᱚᱲᱟ", "hor kora"],
    ["Woman", "ᱦᱚᱲ ᱠᱩᱲᱤ", "hor kuri"],
    ["Cock (male chicken)", "ᱥᱤᱢ ᱠᱚᱲᱟ", "sim kora"],
    ["Hen (female chicken)", "ᱥᱤᱢ ᱠᱩᱲᱤ", "sim kuri"],
    ["One boy", "ᱢᱤᱫ ᱠᱚᱲᱟ", "mid kora"],
    ["Two boys", "ᱵᱟᱨ ᱠᱚᱲᱟ", "bar kora"],
    ["Many boys", "ᱟᱹᱰᱤ ᱠᱚᱲᱟ ᱠᱚ", "adi kora ko"],
    ["One house", "ᱢᱤᱫ ᱚᱲᱟᱜ", "mid orag"],
    ["Two houses", "ᱵᱟᱨ ᱚᱲᱟᱜ", "bar orag"],
    ["Many houses", "ᱟᱹᱰᱤ ᱚᱲᱟᱜ ᱠᱚ", "adi orag ko"],
    ["The children (plural marker ko)", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ", "gidra ko"],
    ["The trees (plural marker ko)", "ᱫᱟᱨᱮ ᱠᱚ", "dare ko"],
    ["All people", "ᱡᱚᱛᱚ ᱦᱚᱲ ᱠᱚ", "joto hor ko"],
    ["Some flowers", "ᱠᱟᱛᱮ ᱵᱟᱦᱟ ᱠᱚ", "kate baha ko"],
    ["Many birds", "ᱟᱹᱰᱤ ᱪᱮᱨᱮ ᱠᱚ", "adi cere ko"],
    ["Two eyes", "ᱵᱟᱨ ᱢᱮᱫ", "bar med"]
]

LESSONS[533] = [
    ["The book is on the table", "ᱯᱩᱛᱷᱤ ᱴᱮᱵᱩᱞ ᱪᱮᱛᱟᱱ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "puthi tebul cetan re menag a"],
    ["The cat is under the bed", "ᱢᱮᱭᱟᱫ ᱪᱚᱠᱤ ᱞᱟᱛᱟᱨ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "meyad choki latar re menag a"],
    ["He is inside the house", "ᱩᱱᱤ ᱚᱲᱟᱜ ᱵᱷᱤᱛᱤᱨ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "uni orag bhitir re menag a"],
    ["She is outside the house", "ᱩᱱᱤ ᱚᱲᱟᱜ ᱵᱟᱦᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "uni orag bahre menag a"],
    ["The shop is near the school", "ᱫᱚᱠᱟᱱ ᱥᱠᱩᱞ ᱱᱮᱰᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "dokan skul neda re menag a"],
    ["The river is far from here", "ᱜᱟᱰᱟ ᱱᱮᱛᱟᱨ ᱠᱷᱚᱱ ᱫᱩᱨ ᱢᱮᱱᱟᱜ ᱟ", "gada netar khon dur menag a"],
    ["The tree is behind the house", "ᱫᱟᱨᱮ ᱚᱲᱟᱜ ᱯᱤᱪᱷᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "dare orag pichha re menag a"],
    ["The bird is on the tree", "ᱪᱮᱨᱮ ᱫᱟᱨᱮ ᱪᱮᱛᱟᱱ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "cere dare cetan re menag a"],
    ["I sat beside him", "ᱤᱧ ᱩᱱᱤᱭᱟᱜ ᱜᱚᱲᱟ ᱨᱮ ᱫᱩᱲᱩᱵ ᱮᱱᱟ", "inj uniag gora re durub ena"],
    ["The flowers are in the garden", "ᱵᱟᱦᱟ ᱠᱚ ᱵᱟᱜᱤᱪᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "baha ko bagicha re menag a"],
    ["The fish is in the water", "ᱢᱟᱹᱪᱷᱟ ᱫᱟᱜ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "machha dag re menag a"],
    ["He is standing in front of the school", "ᱩᱱᱤ ᱥᱠᱩᱞ ᱥᱟᱹᱢᱟᱹᱝ ᱨᱮ ᱛᱤᱧᱜᱩ ᱢᱮᱱᱟᱜ ᱟ", "uni skul samang re tingu menag a"],
    ["Between the two villages", "ᱵᱟᱨ ᱟᱹᱛᱩ ᱛᱟᱞᱟ ᱨᱮ", "bar atu tala re"],
    ["The water is around the house", "ᱫᱟᱜ ᱚᱲᱟᱜ ᱜᱚᱲᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "dag orag gora re menag a"],
    ["I go to school from home", "ᱤᱧ ᱚᱲᱟᱜ ᱠᱷᱚᱱ ᱥᱠᱩᱞ ᱥᱮᱱ ᱟᱭᱟ", "inj orag khon skul sen aya"],
    ["She walks towards the market", "ᱩᱱᱤ ᱵᱟᱡᱟᱨ ᱛᱮ ᱥᱟᱞᱟᱜ ᱟᱫ ᱮ", "uni bajar te salag ad e"],
    ["We live above the shop", "ᱟᱞᱮ ᱫᱚᱠᱟᱱ ᱪᱮᱛᱟᱱ ᱨᱮ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale dokan cetan re taheny ale"],
    ["Put it below the table", "ᱴᱮᱵᱩᱞ ᱞᱟᱛᱟᱨ ᱨᱮ ᱫᱚᱦᱚ ᱢᱮ", "tebul latar re doho me"]
]

LESSONS[534] = [
    ["In / at (location)", "ᱨᱮ (re)", "re"],
    ["From (origin)", "ᱠᱷᱚᱱ (khon)", "khon"],
    ["To / towards", "ᱛᱮ (te)", "te"],
    ["With (accompaniment)", "ᱥᱟᱶ (saw)", "saw"],
    ["For (purpose)", "ᱞᱟᱜᱤᱫ (lagid)", "lagid"],
    ["I am in the house", "ᱤᱧ ᱚᱲᱟᱜ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "inj orag re menag a"],
    ["I came from the village", "ᱤᱧ ᱟᱹᱛᱩ ᱠᱷᱚᱱ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "inj atu khon hijug ena"],
    ["I go to school", "ᱤᱧ ᱥᱠᱩᱞ ᱛᱮ ᱥᱮᱱ ᱟᱭᱟ", "inj skul te sen aya"],
    ["Come with me", "ᱤᱧ ᱥᱟᱶ ᱦᱤᱡᱩᱜ ᱢᱮ", "inj saw hijug me"],
    ["This is for you", "ᱱᱚᱣᱟ ᱟᱢ ᱞᱟᱜᱤᱫ ᱠᱟᱱᱟ", "nowa am lagid kana"],
    ["On top of (upper surface)", "ᱪᱮᱛᱟᱱ ᱨᱮ (cetan re)", "cetan re"],
    ["Below / under", "ᱞᱟᱛᱟᱨ ᱨᱮ (latar re)", "latar re"],
    ["Behind", "ᱯᱤᱪᱷᱟ ᱨᱮ (pichha re)", "pichha re"],
    ["In front of", "ᱥᱟᱹᱢᱟᱹᱝ ᱨᱮ (samang re)", "samang re"],
    ["Beside / next to", "ᱜᱚᱲᱟ ᱨᱮ (gora re)", "gora re"],
    ["Inside", "ᱵᱷᱤᱛᱤᱨ ᱨᱮ (bhitir re)", "bhitir re"],
    ["Outside", "ᱵᱟᱦᱨᱮ (bahre)", "bahre"],
    ["Near", "ᱱᱮᱰᱟ ᱨᱮ (neda re)", "neda re"]
]

LESSONS[535] = [
    ["The boy ate rice (nominative)", "ᱠᱚᱲᱟ ᱫᱟᱹᱠ ᱡᱚᱢ ᱮᱱᱟ", "kora dak jom ena"],
    ["I gave him a book (dative)", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱯᱩᱛᱷᱤ ᱮᱢ ᱮᱱᱟ", "inj uni ke puthi em ena"],
    ["The dog of the boy (genitive)", "ᱠᱚᱲᱟᱭᱟᱜ ᱥᱮᱛᱟ", "korayag seta"],
    ["He went to the market (locative)", "ᱩᱱᱤ ᱵᱟᱡᱟᱨ ᱛᱮ ᱥᱮᱱ ᱮᱱᱟ", "uni bajar te sen ena"],
    ["She came from the village (ablative)", "ᱩᱱᱤ ᱟᱹᱛᱩ ᱠᱷᱚᱱ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "uni atu khon hijug ena"],
    ["He went with his father (instrumental)", "ᱩᱱᱤ ᱩᱱᱤᱭᱟᱜ ᱟᱯᱟ ᱥᱟᱶ ᱥᱮᱱ ᱮᱱᱟ", "uni uniag apa saw sen ena"],
    ["This book is for you", "ᱱᱚᱣᱟ ᱯᱩᱛᱷᱤ ᱟᱢ ᱞᱟᱜᱤᱫ ᱠᱟᱱᱟ", "nowa puthi am lagid kana"],
    ["I work in the field", "ᱤᱧ ᱜᱟᱰᱟ ᱨᱮ ᱠᱟᱹᱢᱤ ᱠᱮᱫ ᱟᱭᱟ", "inj gada re kami ked aya"],
    ["He cut with a knife", "ᱩᱱᱤ ᱪᱟᱠᱩ ᱛᱮ ᱛᱚᱞ ᱮᱱᱟ", "uni chaku te tol ena"],
    ["The child's toy", "ᱜᱤᱫᱽᱨᱟᱹ ᱭᱟᱜ ᱮᱱᱮᱡ ᱡᱤᱱᱤᱥ", "gidra yag enej jinis"],
    ["I called you (accusative)", "ᱤᱧ ᱟᱢ ᱠᱮ ᱠᱩᱞ ᱮᱱᱟ", "inj am ke kul ena"],
    ["She lives in the city", "ᱩᱱᱤ ᱥᱚᱦᱚᱨ ᱨᱮ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni sohor re taheny e"],
    ["Water flows from the mountain", "ᱫᱟᱜ ᱵᱩᱨᱩ ᱠᱷᱚᱱ ᱵᱟᱦᱟ ᱟ", "dag buru khon baha a"],
    ["The mother feeds the child", "ᱟᱭᱚ ᱜᱤᱫᱽᱨᱟᱹ ᱠᱮ ᱡᱚᱢ ᱮᱢ ᱟᱫ ᱮ", "ayo gidra ke jom em ad e"],
    ["He wrote with a pen", "ᱩᱱᱤ ᱠᱟᱞᱟᱢ ᱛᱮ ᱚᱞ ᱮᱱᱟ", "uni kalam te ol ena"],
    ["Her brother's house", "ᱩᱱᱤᱭᱟᱜ ᱦᱟᱯᱲᱟᱢ ᱭᱟᱜ ᱚᱲᱟᱜ", "uniag hapram yag orag"],
    ["I walked towards the hill", "ᱤᱧ ᱵᱩᱨᱩ ᱛᱮ ᱥᱟᱞᱟᱜ ᱮᱱᱟ", "inj buru te salag ena"],
    ["The cat sat on the wall", "ᱢᱮᱭᱟᱫ ᱵᱷᱤᱛ ᱪᱮᱛᱟᱱ ᱨᱮ ᱫᱩᱲᱩᱵ ᱮᱱᱟ", "meyad bhit cetan re durub ena"]
]

LESSONS[536] = [
    ["Go!", "ᱥᱮᱱ ᱢᱮ!", "sen me!"],
    ["Come!", "ᱦᱤᱡᱩᱜ ᱢᱮ!", "hijug me!"],
    ["Eat!", "ᱡᱚᱢ ᱢᱮ!", "jom me!"],
    ["Sit down!", "ᱫᱩᱲᱩᱵ ᱢᱮ!", "durub me!"],
    ["Stand up!", "ᱛᱤᱧᱜᱩ ᱢᱮ!", "tingu me!"],
    ["Write it!", "ᱚᱞ ᱢᱮ!", "ol me!"],
    ["Read the book!", "ᱯᱩᱛᱷᱤ ᱯᱟᱲᱦᱟᱣ ᱢᱮ!", "puthi parhaw me!"],
    ["Listen carefully!", "ᱵᱷᱟᱞᱮ ᱞᱮᱠᱟ ᱟᱹᱭᱠᱟᱹᱣ ᱢᱮ!", "bhale leka aykaw me!"],
    ["Don't go!", "ᱡᱷᱤᱡ ᱥᱮᱱ ᱢᱮ!", "jhij sen me!"],
    ["Don't eat that!", "ᱚᱱᱟ ᱡᱷᱤᱡ ᱡᱚᱢ ᱢᱮ!", "ona jhij jom me!"],
    ["Please help me", "ᱤᱧ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱢᱮ", "inj ke sagay me"],
    ["Give me water", "ᱫᱟᱜ ᱮᱢ ᱢᱮ", "dag em me"],
    ["Open the door", "ᱫᱩᱣᱟᱹᱨ ᱡᱷᱤᱡ ᱢᱮ", "duwar jhij me"],
    ["Close the window", "ᱡᱷᱚᱨᱠᱟ ᱫᱟᱸᱰ ᱢᱮ", "jhorka dand me"],
    ["Speak in Santali", "ᱥᱟᱱᱛᱟᱲᱤ ᱨᱮ ᱨᱚᱲ ᱢᱮ", "santari re ror me"],
    ["Bring the food", "ᱡᱚᱢ ᱟᱹᱜᱩ ᱢᱮ", "jom agu me"],
    ["Wait here", "ᱱᱮᱛᱟᱨ ᱡᱚᱜᱟᱹᱣ ᱢᱮ", "netar jogaw me"],
    ["Let's go together", "ᱟᱞᱮ ᱥᱟᱶᱛᱮ ᱥᱮᱱ ᱟᱞᱮ", "ale sawte sen ale"]
]

LESSONS[537] = [
    ["Today", "ᱟᱡ", "aj"],
    ["Yesterday", "ᱜᱟᱞᱟ", "gala"],
    ["Tomorrow", "ᱜᱟᱯᱟ", "gapa"],
    ["Day before yesterday", "ᱦᱚᱞᱟ", "hola"],
    ["Day after tomorrow", "ᱢᱟᱱᱤᱡ", "manij"],
    ["Morning", "ᱥᱮᱛᱟᱜ", "setag"],
    ["Afternoon", "ᱛᱤᱠᱤᱱ", "tikin"],
    ["Evening / night", "ᱧᱤᱸᱫᱟ", "nyinda"],
    ["Now", "ᱱᱤᱛ", "nit"],
    ["Then / at that time", "ᱚᱱᱟ ᱵᱮᱞᱟ ᱨᱮ", "ona bela re"],
    ["Always", "ᱡᱟᱦᱟᱸᱱᱟᱜ", "jahanag"],
    ["Sometimes", "ᱠᱟᱛᱮ ᱠᱟᱛᱮ", "kate kate"],
    ["Daily / every day", "ᱫᱤᱱ ᱫᱤᱱ", "din din"],
    ["Weekly", "ᱦᱟᱯᱛᱟ ᱦᱟᱯᱛᱟ", "hapta hapta"],
    ["Month", "ᱪᱟᱸᱫᱚ", "chando"],
    ["Year", "ᱥᱮᱨᱢᱟ", "serma"],
    ["Early / before", "ᱟᱜᱮ", "age"],
    ["Late / after", "ᱛᱟᱭᱚᱢ", "tayom"]
]

LESSONS[538] = [
    ["I made him eat", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱡᱚᱢ ᱤᱪᱤ ᱮᱱᱟ", "inj uni ke jom ichi ena"],
    ["She made the child sleep", "ᱩᱱᱤ ᱜᱤᱫᱽᱨᱟᱹ ᱠᱮ ᱧᱤᱫ ᱤᱪᱤ ᱮᱱᱟ", "uni gidra ke nyid ichi ena"],
    ["Father made me study", "ᱟᱯᱟ ᱤᱧ ᱠᱮ ᱯᱟᱲᱦᱟᱣ ᱤᱪᱤ ᱮᱱᱟ", "apa inj ke parhaw ichi ena"],
    ["He made them work", "ᱩᱱᱤ ᱩᱱᱠᱩ ᱠᱮ ᱠᱟᱹᱢᱤ ᱤᱪᱤ ᱮᱱᱟ", "uni unku ke kami ichi ena"],
    ["Mother made me wake up", "ᱟᱭᱚ ᱤᱧ ᱠᱮ ᱪᱟᱹᱞᱩ ᱤᱪᱤ ᱮᱱᱟ", "ayo inj ke chalu ichi ena"],
    ["I will make him come", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱦᱤᱡᱩᱜ ᱤᱪᱤ ᱟ", "inj uni ke hijug ichi a"],
    ["She will make tea", "ᱩᱱᱤ ᱪᱟᱹ ᱛᱮᱭᱟᱨ ᱤᱪᱤ ᱮ", "uni cha teyar ichi e"],
    ["Teacher made us write", "ᱯᱟᱲᱦᱟᱣᱮᱫ ᱟᱞᱮ ᱠᱮ ᱚᱞ ᱤᱪᱤ ᱮᱱᱟ", "parhawed ale ke ol ichi ena"],
    ["He made the dog run", "ᱩᱱᱤ ᱥᱮᱛᱟ ᱠᱮ ᱫᱟᱹᱲ ᱤᱪᱤ ᱮᱱᱟ", "uni seta ke dar ichi ena"],
    ["I made her understand", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱵᱩᱡᱷᱟᱹᱣ ᱤᱪᱤ ᱮᱱᱟ", "inj uni ke bujhaw ichi ena"],
    ["She made the children sing", "ᱩᱱᱤ ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱠᱮ ᱥᱮᱨᱮᱧ ᱤᱪᱤ ᱮᱱᱟ", "uni gidra ko ke sereny ichi ena"],
    ["Father made us go", "ᱟᱯᱟ ᱟᱞᱮ ᱠᱮ ᱥᱮᱱ ᱤᱪᱤ ᱮᱱᱟ", "apa ale ke sen ichi ena"],
    ["I will make him read", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱯᱟᱲᱦᱟᱣ ᱤᱪᱤ ᱟ", "inj uni ke parhaw ichi a"],
    ["She made me laugh", "ᱩᱱᱤ ᱤᱧ ᱠᱮ ᱞᱟᱸᱫᱟ ᱤᱪᱤ ᱮᱱᱟ", "uni inj ke landa ichi ena"],
    ["He made them sit", "ᱩᱱᱤ ᱩᱱᱠᱩ ᱠᱮ ᱫᱩᱲᱩᱵ ᱤᱪᱤ ᱮᱱᱟ", "uni unku ke durub ichi ena"],
    ["Teacher made students listen", "ᱯᱟᱲᱦᱟᱣᱮᱫ ᱪᱟᱴᱟᱨ ᱠᱚ ᱠᱮ ᱟᱹᱭᱠᱟᱹᱣ ᱤᱪᱤ ᱮᱱᱟ", "parhawed chatar ko ke aykaw ichi ena"],
    ["Mother made him bathe", "ᱟᱭᱚ ᱩᱱᱤ ᱠᱮ ᱡᱩ ᱤᱪᱤ ᱮᱱᱟ", "ayo uni ke ju ichi ena"],
    ["I made them dance", "ᱤᱧ ᱩᱱᱠᱩ ᱠᱮ ᱮᱱᱮᱡ ᱤᱪᱤ ᱮᱱᱟ", "inj unku ke enej ichi ena"]
]

LESSONS[539] = [
    ["The boy goes (masculine subject)", "ᱠᱚᱲᱟ ᱥᱮᱱ ᱟᱫ ᱮ", "kora sen ad e"],
    ["The girl goes (feminine subject)", "ᱠᱩᱲᱤ ᱥᱮᱱ ᱟᱫ ᱮ", "kuri sen ad e"],
    ["The boys go (plural)", "ᱠᱚᱲᱟ ᱠᱚ ᱥᱮᱱ ᱟᱠᱟᱫᱟ", "kora ko sen akada"],
    ["The girls go (plural)", "ᱠᱩᱲᱤ ᱠᱚ ᱥᱮᱱ ᱟᱠᱟᱫᱟ", "kuri ko sen akada"],
    ["He eats", "ᱩᱱᱤ ᱡᱚᱢ ᱟᱫ ᱮ", "uni jom ad e"],
    ["She eats", "ᱩᱱᱤ ᱡᱚᱢ ᱟᱫ ᱮ", "uni jom ad e"],
    ["They (humans) eat", "ᱩᱱᱠᱩ ᱡᱚᱢ ᱟᱠᱟᱫᱟ", "unku jom akada"],
    ["The child sings", "ᱜᱤᱫᱽᱨᱟᱹ ᱥᱮᱨᱮᱧ ᱟᱫ ᱮ", "gidra sereny ad e"],
    ["The children sing", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱥᱮᱨᱮᱧ ᱟᱠᱟᱫᱟ", "gidra ko sereny akada"],
    ["The bird flies", "ᱪᱮᱨᱮ ᱩᱰᱟᱹᱣ ᱟᱫ ᱮ", "cere udaw ad e"],
    ["The birds fly", "ᱪᱮᱨᱮ ᱠᱚ ᱩᱰᱟᱹᱣ ᱟᱠᱟᱫᱟ", "cere ko udaw akada"],
    ["Father works", "ᱟᱯᱟ ᱠᱟᱹᱢᱤ ᱠᱮᱫ ᱮ", "apa kami ked e"],
    ["Mother and father work", "ᱟᱭᱚ ᱟᱨ ᱟᱯᱟ ᱠᱟᱹᱢᱤ ᱠᱮᱫ ᱠᱚ", "ayo ar apa kami ked ko"],
    ["One tree stands", "ᱢᱤᱫ ᱫᱟᱨᱮ ᱛᱤᱧᱜᱩ ᱢᱮᱱᱟᱜ ᱟ", "mid dare tingu menag a"],
    ["Many trees stand", "ᱟᱹᱰᱤ ᱫᱟᱨᱮ ᱠᱚ ᱛᱤᱧᱜᱩ ᱢᱮᱱᱟᱜ ᱟ", "adi dare ko tingu menag a"],
    ["I and you went", "ᱤᱧ ᱟᱨ ᱟᱢ ᱥᱮᱱ ᱮᱱᱟ", "inj ar am sen ena"],
    ["The man speaks", "ᱦᱚᱲ ᱠᱚᱲᱟ ᱨᱚᱲ ᱟᱫ ᱮ", "hor kora ror ad e"],
    ["The women speak", "ᱦᱚᱲ ᱠᱩᱲᱤ ᱠᱚ ᱨᱚᱲ ᱟᱠᱟᱫᱟ", "hor kuri ko ror akada"]
]

LESSONS[540] = [
    ["I have eaten (second style)", "ᱤᱧ ᱡᱚᱢ ᱟᱠᱟᱫ ᱟ", "inj jom akad a"],
    ["You have gone", "ᱟᱢ ᱥᱮᱱ ᱟᱠᱟᱫ ᱟᱢ", "am sen akad am"],
    ["He has written", "ᱩᱱᱤ ᱚᱞ ᱟᱠᱟᱫ ᱮ", "uni ol akad e"],
    ["She has finished", "ᱩᱱᱤ ᱛᱮᱭᱟᱨ ᱟᱠᱟᱫ ᱮ", "uni teyar akad e"],
    ["We have come", "ᱟᱞᱮ ᱦᱤᱡᱩᱜ ᱟᱠᱟᱫ ᱟᱞᱮ", "ale hijug akad ale"],
    ["I had eaten (past perfect)", "ᱤᱧ ᱡᱚᱢ ᱟᱠᱟᱫ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj jom akad taheny a"],
    ["He had gone", "ᱩᱱᱤ ᱥᱮᱱ ᱟᱠᱟᱫ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni sen akad taheny e"],
    ["She had cooked", "ᱩᱱᱤ ᱨᱟᱸᱰᱷᱟ ᱟᱠᱟᱫ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni randha akad taheny e"],
    ["I will have eaten", "ᱤᱧ ᱡᱚᱢ ᱟᱠᱟᱫ ᱟ", "inj jom akad a"],
    ["They will have come", "ᱩᱱᱠᱩ ᱦᱤᱡᱩᱜ ᱟᱠᱟᱫ ᱠᱚ", "unku hijug akad ko"],
    ["I have studied everything", "ᱤᱧ ᱡᱚᱛᱚ ᱯᱟᱲᱦᱟᱣ ᱟᱠᱟᱫ ᱟ", "inj joto parhaw akad a"],
    ["He has seen the movie", "ᱩᱱᱤ ᱮᱱᱮᱡ ᱧᱮᱞ ᱟᱠᱟᱫ ᱮ", "uni enej nyel akad e"],
    ["She has bought clothes", "ᱩᱱᱤ ᱠᱟᱹᱯᱲᱟ ᱠᱤᱱ ᱟᱠᱟᱫ ᱮ", "uni kapra kin akad e"],
    ["We had learned Santali", "ᱟᱞᱮ ᱥᱟᱱᱛᱟᱲᱤ ᱥᱮᱪᱮᱫ ᱟᱠᱟᱫ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale santari seced akad taheny ale"],
    ["Father had returned", "ᱟᱯᱟ ᱨᱩᱣᱟᱹᱲ ᱟᱠᱟᱫ ᱛᱟᱦᱮᱸᱱ ᱮ", "apa ruwar akad taheny e"],
    ["I have done the work", "ᱤᱧ ᱠᱟᱹᱢᱤ ᱛᱮᱭᱟᱨ ᱟᱠᱟᱫ ᱟ", "inj kami teyar akad a"],
    ["They have built a house", "ᱩᱱᱠᱩ ᱚᱲᱟᱜ ᱛᱮᱭᱟᱨ ᱟᱠᱟᱫ ᱠᱚ", "unku orag teyar akad ko"],
    ["She has told the truth", "ᱩᱱᱤ ᱥᱟᱹᱨᱤ ᱨᱚᱲ ᱟᱠᱟᱫ ᱮ", "uni sari ror akad e"]
]

LESSONS[541] = [
    ["I have been eating", "ᱤᱧ ᱡᱚᱢ ᱛᱟᱦᱮᱸᱱ ᱟᱭᱟ", "inj jom taheny aya"],
    ["He has been studying", "ᱩᱱᱤ ᱯᱟᱲᱦᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni parhaw taheny e"],
    ["She has been cooking since morning", "ᱩᱱᱤ ᱥᱮᱛᱟᱜ ᱠᱷᱚᱱ ᱨᱟᱸᱰᱷᱟ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni setag khon randha taheny e"],
    ["I had been working all day", "ᱤᱧ ᱥᱟᱹᱨᱟᱹ ᱫᱤᱱ ᱠᱟᱹᱢᱤ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj sara din kami taheny a"],
    ["They had been playing", "ᱩᱱᱠᱩ ᱮᱱᱮᱡ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "unku enej taheny ko"],
    ["He had been reading for hours", "ᱩᱱᱤ ᱜᱷᱚᱱᱴᱟ ᱜᱷᱚᱱᱴᱟ ᱯᱟᱲᱦᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni ghonta ghonta parhaw taheny e"],
    ["I will have been living here", "ᱤᱧ ᱱᱮᱛᱟᱨ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj netar taheny a"],
    ["She will have been teaching", "ᱩᱱᱤ ᱯᱟᱲᱦᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni parhaw taheny e"],
    ["It has been raining", "ᱫᱟᱜ ᱫᱟᱹᱲ ᱛᱟᱦᱮᱸᱱ ᱟ", "dag dar taheny a"],
    ["I have been waiting long", "ᱤᱧ ᱟᱹᱰᱤ ᱡᱚᱜᱟᱹᱣ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj adi jogaw taheny a"],
    ["We have been learning Santali", "ᱟᱞᱮ ᱥᱟᱱᱛᱟᱲᱤ ᱥᱮᱪᱮᱫ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale santari seced taheny ale"],
    ["He has been sitting here", "ᱩᱱᱤ ᱱᱮᱛᱟᱨ ᱫᱩᱲᱩᱵ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni netar durub taheny e"],
    ["They have been dancing", "ᱩᱱᱠᱩ ᱮᱱᱮᱡ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "unku enej taheny ko"],
    ["Father had been working in the field", "ᱟᱯᱟ ᱜᱟᱰᱟ ᱨᱮ ᱠᱟᱹᱢᱤ ᱛᱟᱦᱮᱸᱱ ᱮ", "apa gada re kami taheny e"],
    ["She has been singing", "ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni sereny taheny e"],
    ["I had been sleeping", "ᱤᱧ ᱧᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj nyid taheny a"],
    ["We will have been celebrating", "ᱟᱞᱮ ᱢᱟᱱᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale manaw taheny ale"],
    ["The children had been playing all day", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱥᱟᱹᱨᱟᱹ ᱫᱤᱱ ᱮᱱᱮᱡ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "gidra ko sara din enej taheny ko"]
]

LESSONS[542] = [
    ["No", "ᱵᱟᱝ", "bang"],
    ["Not (negation)", "ᱵᱟᱝ", "bang"],
    ["Don't want", "ᱵᱟᱝ ᱥᱟᱱᱟᱢ", "bang sanam"],
    ["I don't go (negation)", "ᱤᱧ ᱵᱟᱝ ᱥᱮᱱ ᱟ", "inj bang sen a"],
    ["I don't want to go", "ᱤᱧ ᱵᱟᱝ ᱥᱮᱱ ᱥᱟᱱᱟᱢ ᱟ", "inj bang sen sanam a"],
    ["He doesn't eat", "ᱩᱱᱤ ᱵᱟᱝ ᱡᱚᱢ ᱮ", "uni bang jom e"],
    ["He doesn't want to eat", "ᱩᱱᱤ ᱵᱟᱝ ᱡᱚᱢ ᱥᱟᱱᱟᱢ ᱮ", "uni bang jom sanam e"],
    ["I'm not coming", "ᱤᱧ ᱵᱟᱝ ᱦᱤᱡᱩᱜ ᱟ", "inj bang hijug a"],
    ["I don't want to come", "ᱤᱧ ᱵᱟᱝ ᱦᱤᱡᱩᱜ ᱥᱟᱱᱟᱢ ᱟ", "inj bang hijug sanam a"],
    ["She doesn't speak", "ᱩᱱᱤ ᱵᱟᱝ ᱨᱚᱲ ᱮ", "uni bang ror e"],
    ["She doesn't want to speak", "ᱩᱱᱤ ᱵᱟᱝ ᱨᱚᱲ ᱥᱟᱱᱟᱢ ᱮ", "uni bang ror sanam e"],
    ["I don't know", "ᱤᱧ ᱵᱟᱝ ᱵᱟᱰᱟᱭ ᱟ", "inj bang baday a"],
    ["I don't want to know", "ᱤᱧ ᱵᱟᱝ ᱵᱟᱰᱟᱭ ᱥᱟᱱᱟᱢ ᱟ", "inj bang baday sanam a"],
    ["No, I won't go", "ᱵᱟᱝ, ᱤᱧ ᱵᱟᱝ ᱥᱮᱱ ᱟ", "bang, inj bang sen a"],
    ["I don't need it", "ᱤᱧ ᱵᱟᱝ ᱞᱟᱜᱤᱫ ᱟ", "inj bang lagid a"],
    ["I don't want it", "ᱤᱧ ᱵᱟᱝ ᱥᱟᱱᱟᱢ ᱟ", "inj bang sanam a"],
    ["They are not here", "ᱩᱱᱠᱩ ᱱᱮᱛᱟᱨ ᱵᱟᱝ ᱢᱮᱱᱟᱜ ᱟ", "unku netar bang menag a"],
    ["They don't want to stay", "ᱩᱱᱠᱩ ᱵᱟᱝ ᱛᱟᱦᱮᱸᱱ ᱥᱟᱱᱟᱢ ᱠᱚ", "unku bang taheny sanam ko"]
]

for ch in d:
    if ch['id'] in LESSONS:
        ch['blocks'] = [{"type": "table", "columns": ["English", "Santali (Ol Chiki)", "Transliteration"], "rows": LESSONS[ch['id']]}]

open('data_santali.json', 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('Section 2 (510-542) populated')
