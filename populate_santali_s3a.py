import json

d = json.load(open('data_santali.json', 'r', encoding='utf-8'))

LESSONS = {}

# 543 - "Going to" phrase
LESSONS[543] = [
    ["I am going to eat", "ᱤᱧ ᱡᱚᱢ ᱥᱮᱱ ᱟᱭᱟ", "inj jom sen aya"],
    ["He is going to come", "ᱩᱱᱤ ᱦᱤᱡᱩᱜ ᱥᱮᱱ ᱟᱫ ᱮ", "uni hijug sen ad e"],
    ["She is going to cook", "ᱩᱱᱤ ᱨᱟᱸᱰᱷᱟ ᱥᱮᱱ ᱟᱫ ᱮ", "uni randha sen ad e"],
    ["We are going to study", "ᱟᱞᱮ ᱯᱟᱲᱦᱟᱣ ᱥᱮᱱ ᱟᱞᱮ", "ale parhaw sen ale"],
    ["They are going to play", "ᱩᱱᱠᱩ ᱮᱱᱮᱡ ᱥᱮᱱ ᱟᱠᱟᱫᱟ", "unku enej sen akada"],
    ["I am going to sleep", "ᱤᱧ ᱧᱤᱫ ᱥᱮᱱ ᱟᱭᱟ", "inj nyid sen aya"],
    ["He is going to write", "ᱩᱱᱤ ᱚᱞ ᱥᱮᱱ ᱟᱫ ᱮ", "uni ol sen ad e"],
    ["She is going to sing", "ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱥᱮᱱ ᱟᱫ ᱮ", "uni sereny sen ad e"],
    ["We are going to the market", "ᱟᱞᱮ ᱵᱟᱡᱟᱨ ᱥᱮᱱ ᱟᱞᱮ", "ale bajar sen ale"],
    ["I am going to buy clothes", "ᱤᱧ ᱠᱟᱹᱯᱲᱟ ᱠᱤᱱ ᱥᱮᱱ ᱟᱭᱟ", "inj kapra kin sen aya"],
    ["Father is going to return", "ᱟᱯᱟ ᱨᱩᱣᱟᱹᱲ ᱥᱮᱱ ᱮ", "apa ruwar sen e"],
    ["Children are going to school", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱥᱠᱩᱞ ᱥᱮᱱ ᱟᱠᱟᱫᱟ", "gidra ko skul sen akada"],
    ["It is going to rain", "ᱫᱟᱜ ᱫᱟᱹᱲ ᱥᱮᱱ ᱟ", "dag dar sen a"],
    ["I am going to help you", "ᱤᱧ ᱟᱢ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱥᱮᱱ ᱟ", "inj am ke sagay sen a"],
    ["She is going to tell a story", "ᱩᱱᱤ ᱠᱟᱹᱦᱱᱤ ᱨᱚᱲ ᱥᱮᱱ ᱟᱫ ᱮ", "uni kahni ror sen ad e"],
    ["We are going to celebrate", "ᱟᱞᱮ ᱢᱟᱱᱟᱣ ᱥᱮᱱ ᱟᱞᱮ", "ale manaw sen ale"],
    ["He is going to learn Santali", "ᱩᱱᱤ ᱥᱟᱱᱛᱟᱲᱤ ᱥᱮᱪᱮᱫ ᱥᱮᱱ ᱟᱫ ᱮ", "uni santari seced sen ad e"],
    ["I am going to call him", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱠᱩᱞ ᱥᱮᱱ ᱟ", "inj uni ke kul sen a"]
]

# 544 - "Used to" phrase
LESSONS[544] = [
    ["I used to go to school", "ᱤᱧ ᱥᱠᱩᱞ ᱥᱮᱱ ᱛᱟᱦᱮᱸᱱ ᱟᱭᱟ", "inj skul sen taheny aya"],
    ["He used to play every day", "ᱩᱱᱤ ᱫᱤᱱ ᱫᱤᱱ ᱮᱱᱮᱡ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni din din enej taheny e"],
    ["She used to cook well", "ᱩᱱᱤ ᱵᱷᱟᱞᱮ ᱨᱟᱸᱰᱷᱟ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni bhale randha taheny e"],
    ["We used to live in the village", "ᱟᱞᱮ ᱟᱹᱛᱩ ᱨᱮ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale atu re taheny ale"],
    ["They used to sing at festivals", "ᱩᱱᱠᱩ ᱯᱚᱨᱚᱵ ᱨᱮ ᱥᱮᱨᱮᱧ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "unku porob re sereny taheny ko"],
    ["Father used to tell stories", "ᱟᱯᱟ ᱠᱟᱹᱦᱱᱤ ᱨᱚᱲ ᱛᱟᱦᱮᱸᱱ ᱮ", "apa kahni ror taheny e"],
    ["I used to wake up early", "ᱤᱧ ᱥᱮᱛᱟᱜ ᱪᱟᱹᱞᱩ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj setag chalu taheny a"],
    ["She used to walk to school", "ᱩᱱᱤ ᱥᱠᱩᱞ ᱥᱟᱞᱟᱜ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni skul salag taheny e"],
    ["We used to play in the forest", "ᱟᱞᱮ ᱵᱤᱨ ᱨᱮ ᱮᱱᱮᱡ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale bir re enej taheny ale"],
    ["He used to fish in the river", "ᱩᱱᱤ ᱜᱟᱰᱟ ᱨᱮ ᱢᱟᱹᱪᱷᱟ ᱫᱟᱹᱲ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni gada re machha dar taheny e"],
    ["Grandmother used to make sweets", "ᱟᱡᱤ ᱡᱤᱞᱤᱯᱤ ᱛᱮᱭᱟᱨ ᱛᱟᱦᱮᱸᱱ ᱮ", "aji jilipi teyar taheny e"],
    ["I used to read books at night", "ᱤᱧ ᱧᱤᱸᱫᱟ ᱨᱮ ᱯᱩᱛᱷᱤ ᱯᱟᱲᱦᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj nyinda re puthi parhaw taheny a"],
    ["Children used to dance", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱮᱱᱮᱡ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "gidra ko enej taheny ko"],
    ["He used to work hard", "ᱩᱱᱤ ᱟᱹᱰᱤ ᱠᱟᱹᱢᱤ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni adi kami taheny e"],
    ["I used to drink milk every morning", "ᱤᱧ ᱫᱤᱱ ᱫᱤᱱ ᱥᱮᱛᱟᱜ ᱫᱩᱫᱷ ᱧᱩ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj din din setag dudh nyu taheny a"],
    ["Mother used to sing lullabies", "ᱟᱭᱚ ᱥᱮᱨᱮᱧ ᱛᱟᱦᱮᱸᱱ ᱮ", "ayo sereny taheny e"],
    ["We used to walk by the river", "ᱟᱞᱮ ᱜᱟᱰᱟ ᱜᱚᱲᱟ ᱨᱮ ᱥᱟᱞᱟᱜ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale gada gora re salag taheny ale"],
    ["They used to come every year", "ᱩᱱᱠᱩ ᱥᱮᱨᱢᱟ ᱥᱮᱨᱢᱟ ᱦᱤᱡᱩᱜ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "unku serma serma hijug taheny ko"]
]

# 545 - "Used to" old style
LESSONS[545] = [
    ["I used to study there", "ᱤᱧ ᱚᱱᱫᱮ ᱯᱟᱲᱦᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj onde parhaw taheny a"],
    ["He used to live in Ranchi", "ᱩᱱᱤ ᱨᱟᱸᱪᱤ ᱨᱮ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni Ranchi re taheny e"],
    ["She used to teach children", "ᱩᱱᱤ ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱠᱮ ᱯᱟᱲᱦᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni gidra ko ke parhaw taheny e"],
    ["We used to gather every evening", "ᱟᱞᱮ ᱧᱤᱸᱫᱟ ᱧᱤᱸᱫᱟ ᱡᱚᱴᱚᱜ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale nyinda nyinda jotog taheny ale"],
    ["Father used to farm this land", "ᱟᱯᱟ ᱱᱚᱣᱟ ᱜᱟᱰᱟ ᱨᱮ ᱠᱟᱹᱢᱤ ᱛᱟᱦᱮᱸᱱ ᱮ", "apa nowa gada re kami taheny e"],
    ["They used to sell vegetables", "ᱩᱱᱠᱩ ᱥᱟᱜ ᱵᱮᱪᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "unku sag becaw taheny ko"],
    ["I used to love this place", "ᱤᱧ ᱱᱚᱣᱟ ᱡᱟᱭᱜᱟ ᱫᱩᱞᱟᱹᱲ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj nowa jayga dular taheny a"],
    ["He used to write poems", "ᱩᱱᱤ ᱠᱟᱹᱵᱤᱛᱟ ᱚᱞ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni kabita ol taheny e"],
    ["She used to come by bus", "ᱩᱱᱤ ᱵᱟᱥ ᱛᱮ ᱦᱤᱡᱩᱜ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni bas te hijug taheny e"],
    ["We used to celebrate Baha festival", "ᱟᱞᱮ ᱵᱟᱦᱟ ᱯᱚᱨᱚᱵ ᱢᱟᱱᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale baha porob manaw taheny ale"],
    ["Children used to swim in the river", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱜᱟᱰᱟ ᱨᱮ ᱫᱟᱹᱲ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "gidra ko gada re dar taheny ko"],
    ["Grandfather used to hunt", "ᱵᱟᱵᱟ ᱥᱮᱱᱫᱨᱟ ᱛᱟᱦᱮᱸᱱ ᱮ", "baba sendra taheny e"],
    ["I used to help mother", "ᱤᱧ ᱟᱭᱚ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj ayo ke sagay taheny a"],
    ["She used to make handicrafts", "ᱩᱱᱤ ᱦᱟᱛ ᱠᱟᱹᱢᱤ ᱛᱮᱭᱟᱨ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni hat kami teyar taheny e"],
    ["He used to travel by train", "ᱩᱱᱤ ᱨᱮᱞ ᱛᱮ ᱥᱮᱱ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni rel te sen taheny e"],
    ["Mother used to weave cloth", "ᱟᱭᱚ ᱠᱟᱹᱯᱲᱟ ᱵᱩᱱ ᱛᱟᱦᱮᱸᱱ ᱮ", "ayo kapra bun taheny e"],
    ["We used to meet under the tree", "ᱟᱞᱮ ᱫᱟᱨᱮ ᱞᱟᱛᱟᱨ ᱧᱮᱞᱚᱜ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale dare latar nyelog taheny ale"],
    ["I used to speak only Santali", "ᱤᱧ ᱠᱷᱟᱞᱤ ᱥᱟᱱᱛᱟᱲᱤ ᱨᱚᱲ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj khali santari ror taheny a"]
]

# 546 - If-Then sentences
LESSONS[546] = [
    ["If you come, I will go", "ᱟᱢ ᱦᱤᱡᱩᱜ ᱨᱮᱫᱚ, ᱤᱧ ᱥᱮᱱ ᱟ", "am hijug redo, inj sen a"],
    ["If it rains, we won't go", "ᱫᱟᱜ ᱫᱟᱹᱲ ᱨᱮᱫᱚ, ᱟᱞᱮ ᱵᱟᱝ ᱥᱮᱱ ᱟᱞᱮ", "dag dar redo, ale bang sen ale"],
    ["If you study, you will pass", "ᱟᱢ ᱯᱟᱲᱦᱟᱣ ᱨᱮᱫᱚ, ᱟᱢ ᱯᱟᱥ ᱟᱢ", "am parhaw redo, am pas am"],
    ["If he calls, tell me", "ᱩᱱᱤ ᱠᱩᱞ ᱨᱮᱫᱚ, ᱤᱧ ᱠᱮ ᱨᱚᱲ ᱢᱮ", "uni kul redo, inj ke ror me"],
    ["If I have money, I will buy it", "ᱤᱧᱟᱜ ᱴᱟᱠᱟ ᱢᱮᱱᱟᱜ ᱨᱮᱫᱚ, ᱤᱧ ᱠᱤᱱ ᱟ", "injag taka menag redo, inj kin a"],
    ["If she cooks, we will eat", "ᱩᱱᱤ ᱨᱟᱸᱰᱷᱟ ᱨᱮᱫᱚ, ᱟᱞᱮ ᱡᱚᱢ ᱟᱞᱮ", "uni randha redo, ale jom ale"],
    ["If you work hard, you will succeed", "ᱟᱢ ᱟᱹᱰᱤ ᱠᱟᱹᱢᱤ ᱨᱮᱫᱚ, ᱟᱢ ᱡᱤᱛ ᱟᱢ", "am adi kami redo, am jit am"],
    ["If the bus comes, we will go", "ᱵᱟᱥ ᱦᱤᱡᱩᱜ ᱨᱮᱫᱚ, ᱟᱞᱮ ᱥᱮᱱ ᱟᱞᱮ", "bas hijug redo, ale sen ale"],
    ["If you want, take it", "ᱟᱢ ᱥᱟᱱᱟᱢ ᱨᱮᱫᱚ, ᱤᱫᱤ ᱢᱮ", "am sanam redo, idi me"],
    ["If it's cold, wear warm clothes", "ᱫᱷᱤᱨᱤ ᱨᱮᱫᱚ, ᱜᱚᱨᱚᱢ ᱠᱟᱹᱯᱲᱟ ᱫᱚᱦᱚ ᱢᱮ", "dhiri redo, gorom kapra doho me"],
    ["If you are hungry, eat", "ᱟᱢ ᱱᱮᱞᱦᱟ ᱨᱮᱫᱚ, ᱡᱚᱢ ᱢᱮ", "am nelha redo, jom me"],
    ["If he agrees, we will start", "ᱩᱱᱤ ᱢᱟᱱᱟᱣ ᱨᱮᱫᱚ, ᱟᱞᱮ ᱪᱟᱞᱩ ᱟᱞᱮ", "uni manaw redo, ale chalu ale"],
    ["If I finish early, I will come", "ᱤᱧ ᱟᱜᱮ ᱛᱮᱭᱟᱨ ᱨᱮᱫᱚ, ᱤᱧ ᱦᱤᱡᱩᱜ ᱟ", "inj age teyar redo, inj hijug a"],
    ["If they invite us, we will go", "ᱩᱱᱠᱩ ᱟᱞᱮ ᱠᱮ ᱠᱩᱞ ᱨᱮᱫᱚ, ᱟᱞᱮ ᱥᱮᱱ ᱟᱞᱮ", "unku ale ke kul redo, ale sen ale"],
    ["If you speak Santali, I understand", "ᱟᱢ ᱥᱟᱱᱛᱟᱲᱤ ᱨᱚᱲ ᱨᱮᱫᱚ, ᱤᱧ ᱵᱩᱡᱷᱟᱹᱣ ᱟ", "am santari ror redo, inj bujhaw a"],
    ["If father comes, we will celebrate", "ᱟᱯᱟ ᱦᱤᱡᱩᱜ ᱨᱮᱫᱚ, ᱟᱞᱮ ᱢᱟᱱᱟᱣ ᱟᱞᱮ", "apa hijug redo, ale manaw ale"],
    ["If there is time, let's rest", "ᱵᱮᱞᱟ ᱢᱮᱱᱟᱜ ᱨᱮᱫᱚ, ᱥᱮᱨᱮᱧ ᱟᱞᱮ", "bela menag redo, sereny ale"],
    ["If you help me, I will finish", "ᱟᱢ ᱤᱧ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱨᱮᱫᱚ, ᱤᱧ ᱛᱮᱭᱟᱨ ᱟ", "am inj ke sagay redo, inj teyar a"]
]

# 547 - Prepositions with Verbs
LESSONS[547] = [
    ["Go to the market", "ᱵᱟᱡᱟᱨ ᱛᱮ ᱥᱮᱱ ᱢᱮ", "bajar te sen me"],
    ["Come from the village", "ᱟᱹᱛᱩ ᱠᱷᱚᱱ ᱦᱤᱡᱩᱜ ᱢᱮ", "atu khon hijug me"],
    ["Sit on the chair", "ᱪᱚᱠᱤ ᱪᱮᱛᱟᱱ ᱫᱩᱲᱩᱵ ᱢᱮ", "choki cetan durub me"],
    ["Put in the box", "ᱵᱟᱠᱥᱚ ᱨᱮ ᱫᱚᱦᱚ ᱢᱮ", "bakso re doho me"],
    ["Walk with me", "ᱤᱧ ᱥᱟᱶ ᱥᱟᱞᱟᱜ ᱢᱮ", "inj saw salag me"],
    ["Run towards the hill", "ᱵᱩᱨᱩ ᱛᱮ ᱫᱟᱹᱲ ᱢᱮ", "buru te dar me"],
    ["I am looking at the sky", "ᱤᱧ ᱥᱮᱨᱢᱟ ᱛᱮ ᱧᱮᱞ ᱟᱭᱟ", "inj serma te nyel aya"],
    ["She lives near the school", "ᱩᱱᱤ ᱥᱠᱩᱞ ᱱᱮᱰᱟ ᱨᱮ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni skul neda re taheny e"],
    ["He jumped over the wall", "ᱩᱱᱤ ᱵᱷᱤᱛ ᱪᱮᱛᱟᱱ ᱠᱷᱚᱱ ᱩᱪᱟᱹᱲ ᱮᱱᱟ", "uni bhit cetan khon uchar ena"],
    ["I am standing behind the tree", "ᱤᱧ ᱫᱟᱨᱮ ᱯᱤᱪᱷᱟ ᱨᱮ ᱛᱤᱧᱜᱩ ᱟᱭᱟ", "inj dare pichha re tingu aya"],
    ["Walk along the road", "ᱨᱟᱦᱟ ᱛᱮ ᱥᱟᱞᱟᱜ ᱢᱮ", "raha te salag me"],
    ["She fell from the bed", "ᱩᱱᱤ ᱪᱚᱠᱤ ᱠᱷᱚᱱ ᱩᱭᱩᱜ ᱮᱱᱟ", "uni choki khon uyug ena"],
    ["Sit beside me", "ᱤᱧᱟᱜ ᱜᱚᱲᱟ ᱨᱮ ᱫᱩᱲᱩᱵ ᱢᱮ", "injag gora re durub me"],
    ["Look inside the room", "ᱠᱚᱴᱷᱟ ᱵᱷᱤᱛᱤᱨ ᱧᱮᱞ ᱢᱮ", "kotha bhitir nyel me"],
    ["He went outside", "ᱩᱱᱤ ᱵᱟᱦᱨᱮ ᱥᱮᱱ ᱮᱱᱟ", "uni bahre sen ena"],
    ["Take it from the table", "ᱴᱮᱵᱩᱞ ᱠᱷᱚᱱ ᱤᱫᱤ ᱢᱮ", "tebul khon idi me"],
    ["Write on the paper", "ᱠᱟᱜᱚᱡ ᱨᱮ ᱚᱞ ᱢᱮ", "kagoj re ol me"],
    ["I swim in the river", "ᱤᱧ ᱜᱟᱰᱟ ᱨᱮ ᱫᱟᱹᱲ ᱟᱭᱟ", "inj gada re dar aya"]
]

# 548 - Adjectives
LESSONS[548] = [
    ["Good", "ᱵᱷᱟᱞᱮ", "bhale"],
    ["Bad", "ᱯᱩᱨᱟᱹ", "pura"],
    ["Big", "ᱢᱟᱨᱟᱝ", "marang"],
    ["Small", "ᱦᱩᱰᱤᱧ", "huding"],
    ["Hot", "ᱫᱩᱨᱩᱵ", "durub"],
    ["Cold", "ᱫᱷᱤᱨᱤ", "dhiri"],
    ["Beautiful", "ᱥᱚᱢᱵᱷᱟᱨ", "sombhar"],
    ["New", "ᱱᱟᱣᱟ", "nawa"],
    ["Old (person)", "ᱵᱩᱲᱷᱟ", "burha"],
    ["Long / tall", "ᱡᱟᱱᱟᱝ", "janang"],
    ["Short", "ᱦᱩᱰᱤᱧ", "huding"],
    ["Clean", "ᱥᱟᱯᱷᱟ", "sapha"],
    ["Dirty", "ᱪᱤᱠᱟᱹᱱ", "chikan"],
    ["Strong", "ᱡᱚᱨ", "jor"],
    ["Weak", "ᱫᱩᱨᱵᱚᱞ", "durbol"],
    ["Happy / joyful", "ᱨᱟᱹᱥᱠᱟᱹ", "raska"],
    ["Sweet", "ᱢᱤᱴᱷᱟᱹ", "mitha"],
    ["Bitter", "ᱠᱟᱲᱟ", "kara"]
]

# 549 - Can / To be able to
LESSONS[549] = [
    ["I can go", "ᱤᱧ ᱥᱮᱱ ᱫᱟᱲᱮᱭᱟᱜ ᱟ", "inj sen dareyag a"],
    ["You can eat", "ᱟᱢ ᱡᱚᱢ ᱫᱟᱲᱮᱭᱟᱢ ᱟ", "am jom dareyam a"],
    ["He can read", "ᱩᱱᱤ ᱯᱟᱲᱦᱟᱣ ᱫᱟᱲᱮ ᱮ", "uni parhaw dare e"],
    ["She can cook", "ᱩᱱᱤ ᱨᱟᱸᱰᱷᱟ ᱫᱟᱲᱮ ᱮ", "uni randha dare e"],
    ["We can do it", "ᱟᱞᱮ ᱫᱟᱲᱮ ᱟᱞᱮ", "ale dare ale"],
    ["They can come", "ᱩᱱᱠᱩ ᱦᱤᱡᱩᱜ ᱫᱟᱲᱮ ᱠᱚ", "unku hijug dare ko"],
    ["I cannot go", "ᱤᱧ ᱵᱟᱝ ᱥᱮᱱ ᱫᱟᱲᱮᱭᱟᱜ ᱟ", "inj bang sen dareyag a"],
    ["He cannot swim", "ᱩᱱᱤ ᱵᱟᱝ ᱫᱟᱹᱲ ᱫᱟᱲᱮ ᱮ", "uni bang dar dare e"],
    ["Can you speak Santali?", "ᱟᱢ ᱥᱟᱱᱛᱟᱲᱤ ᱨᱚᱲ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am santari ror dareyam ma?"],
    ["I can write in Ol Chiki", "ᱤᱧ ᱚᱞ ᱪᱤᱠᱤ ᱨᱮ ᱚᱞ ᱫᱟᱲᱮᱭᱟᱜ ᱟ", "inj ol chiki re ol dareyag a"],
    ["She can sing well", "ᱩᱱᱤ ᱵᱷᱟᱞᱮ ᱥᱮᱨᱮᱧ ᱫᱟᱲᱮ ᱮ", "uni bhale sereny dare e"],
    ["Children can play", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱮᱱᱮᱡ ᱫᱟᱲᱮ ᱠᱚ", "gidra ko enej dare ko"],
    ["I can see the mountain", "ᱤᱧ ᱵᱩᱨᱩ ᱧᱮᱞ ᱫᱟᱲᱮᱭᱟᱜ ᱟ", "inj buru nyel dareyag a"],
    ["Can you help me?", "ᱟᱢ ᱤᱧ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am inj ke sagay dareyam ma?"],
    ["He can drive a car", "ᱩᱱᱤ ᱜᱟᱰᱤ ᱪᱟᱞᱟᱣ ᱫᱟᱲᱮ ᱮ", "uni gadi chalaw dare e"],
    ["She cannot understand Hindi", "ᱩᱱᱤ ᱦᱤᱱᱫᱤ ᱵᱟᱝ ᱵᱩᱡᱷᱟᱹᱣ ᱫᱟᱲᱮ ᱮ", "uni Hindi bang bujhaw dare e"],
    ["We can finish today", "ᱟᱞᱮ ᱟᱡ ᱛᱮᱭᱟᱨ ᱫᱟᱲᱮ ᱟᱞᱮ", "ale aj teyar dare ale"],
    ["I can hear you", "ᱤᱧ ᱟᱢᱟᱜ ᱠᱟᱹᱛᱷᱟ ᱟᱹᱭᱠᱟᱹᱣ ᱫᱟᱲᱮᱭᱟᱜ ᱟ", "inj amag katha aykaw dareyag a"]
]

# 550 - To Want / To Need
LESSONS[550] = [
    ["I want water", "ᱤᱧ ᱫᱟᱜ ᱥᱟᱱᱟᱢ ᱟ", "inj dag sanam a"],
    ["I want to eat", "ᱤᱧ ᱡᱚᱢ ᱥᱟᱱᱟᱢ ᱟ", "inj jom sanam a"],
    ["He wants a book", "ᱩᱱᱤ ᱯᱩᱛᱷᱤ ᱥᱟᱱᱟᱢ ᱮ", "uni puthi sanam e"],
    ["She wants to go", "ᱩᱱᱤ ᱥᱮᱱ ᱥᱟᱱᱟᱢ ᱮ", "uni sen sanam e"],
    ["We need help", "ᱟᱞᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "ale sagay lagid ale"],
    ["They need food", "ᱩᱱᱠᱩ ᱡᱚᱢ ᱞᱟᱜᱤᱫ ᱠᱚ", "unku jom lagid ko"],
    ["I need money", "ᱤᱧ ᱴᱟᱠᱟ ᱞᱟᱜᱤᱫ ᱟ", "inj taka lagid a"],
    ["I don't want this", "ᱤᱧ ᱱᱚᱣᱟ ᱵᱟᱝ ᱥᱟᱱᱟᱢ ᱟ", "inj nowa bang sanam a"],
    ["Do you want tea?", "ᱟᱢ ᱪᱟᱹ ᱥᱟᱱᱟᱢ ᱟᱢ?", "am cha sanam am?"],
    ["He doesn't want to come", "ᱩᱱᱤ ᱵᱟᱝ ᱦᱤᱡᱩᱜ ᱥᱟᱱᱟᱢ ᱮ", "uni bang hijug sanam e"],
    ["I want to learn Santali", "ᱤᱧ ᱥᱟᱱᱛᱟᱲᱤ ᱥᱮᱪᱮᱫ ᱥᱟᱱᱟᱢ ᱟ", "inj santari seced sanam a"],
    ["She wants to sleep", "ᱩᱱᱤ ᱧᱤᱫ ᱥᱟᱱᱟᱢ ᱮ", "uni nyid sanam e"],
    ["Children need milk", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱫᱩᱫᱷ ᱞᱟᱜᱤᱫ ᱠᱚ", "gidra ko dudh lagid ko"],
    ["I want to see the hill", "ᱤᱧ ᱵᱩᱨᱩ ᱧᱮᱞ ᱥᱟᱱᱟᱢ ᱟ", "inj buru nyel sanam a"],
    ["We need a house", "ᱟᱞᱮ ᱚᱲᱟᱜ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "ale orag lagid ale"],
    ["He wants to work here", "ᱩᱱᱤ ᱱᱮᱛᱟᱨ ᱠᱟᱹᱢᱤ ᱥᱟᱱᱟᱢ ᱮ", "uni netar kami sanam e"],
    ["I want new clothes", "ᱤᱧ ᱱᱟᱣᱟ ᱠᱟᱹᱯᱲᱟ ᱥᱟᱱᱟᱢ ᱟ", "inj nawa kapra sanam a"],
    ["Do you need help?", "ᱟᱢ ᱥᱟᱹᱜᱟᱹᱭ ᱞᱟᱜᱤᱫ ᱟᱢ?", "am sagay lagid am?"]
]

# 551 - To Become / To Happen
LESSONS[551] = [
    ["What happened?", "ᱪᱮᱫ ᱦᱩᱭ ᱮᱱᱟ?", "ced huy ena?"],
    ["It became cold", "ᱫᱷᱤᱨᱤ ᱦᱩᱭ ᱮᱱᱟ", "dhiri huy ena"],
    ["He became a teacher", "ᱩᱱᱤ ᱯᱟᱲᱦᱟᱣᱮᱫ ᱦᱩᱭ ᱮᱱᱟ", "uni parhawed huy ena"],
    ["It will happen", "ᱦᱩᱭ ᱟ", "huy a"],
    ["What is happening?", "ᱪᱮᱫ ᱦᱩᱭ ᱢᱮᱱᱟᱜ ᱟ?", "ced huy menag a?"],
    ["Nothing happened", "ᱡᱟᱦᱟᱸ ᱵᱟᱝ ᱦᱩᱭ ᱮᱱᱟ", "jahang bang huy ena"],
    ["I became happy", "ᱤᱧ ᱨᱟᱹᱥᱠᱟᱹ ᱦᱩᱭ ᱮᱱᱟ", "inj raska huy ena"],
    ["She became angry", "ᱩᱱᱤ ᱨᱤᱥ ᱦᱩᱭ ᱮᱱᱟ", "uni ris huy ena"],
    ["The day became hot", "ᱫᱤᱱ ᱫᱩᱨᱩᱵ ᱦᱩᱭ ᱮᱱᱟ", "din durub huy ena"],
    ["It became dark", "ᱧᱩᱛ ᱦᱩᱭ ᱮᱱᱟ", "nyut huy ena"],
    ["He became rich", "ᱩᱱᱤ ᱫᱷᱚᱱᱤ ᱦᱩᱭ ᱮᱱᱟ", "uni dhoni huy ena"],
    ["The flower bloomed", "ᱵᱟᱦᱟ ᱯᱷᱩᱞ ᱦᱩᱭ ᱮᱱᱟ", "baha phul huy ena"],
    ["It became morning", "ᱥᱮᱛᱟᱜ ᱦᱩᱭ ᱮᱱᱟ", "setag huy ena"],
    ["I became sick", "ᱤᱧ ᱨᱚᱜ ᱦᱩᱭ ᱮᱱᱟ", "inj rog huy ena"],
    ["Everything will be fine", "ᱡᱚᱛᱚ ᱵᱷᱟᱞᱮ ᱦᱩᱭ ᱟ", "joto bhale huy a"],
    ["She became sad", "ᱩᱱᱤ ᱫᱩᱠᱷ ᱦᱩᱭ ᱮᱱᱟ", "uni dukh huy ena"],
    ["The food got ready", "ᱡᱚᱢ ᱛᱮᱭᱟᱨ ᱦᱩᱭ ᱮᱱᱟ", "jom teyar huy ena"],
    ["The rain stopped (became finished)", "ᱫᱟᱜ ᱛᱷᱤᱨ ᱦᱩᱭ ᱮᱱᱟ", "dag thir huy ena"]
]

# 552 - Using "Should"
LESSONS[552] = [
    ["I should go", "ᱤᱧ ᱥᱮᱱ ᱞᱟᱜᱤᱫ ᱟ", "inj sen lagid a"],
    ["You should eat", "ᱟᱢ ᱡᱚᱢ ᱞᱟᱜᱤᱫ ᱟᱢ", "am jom lagid am"],
    ["He should study", "ᱩᱱᱤ ᱯᱟᱲᱦᱟᱣ ᱞᱟᱜᱤᱫ ᱮ", "uni parhaw lagid e"],
    ["She should rest", "ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱞᱟᱜᱤᱫ ᱮ", "uni sereny lagid e"],
    ["We should help each other", "ᱟᱞᱮ ᱢᱤᱫ ᱟᱨ ᱢᱤᱫ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "ale mid ar mid ke sagay lagid ale"],
    ["They should come early", "ᱩᱱᱠᱩ ᱟᱜᱮ ᱦᱤᱡᱩᱜ ᱞᱟᱜᱤᱫ ᱠᱚ", "unku age hijug lagid ko"],
    ["Children should study", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱯᱟᱲᱦᱟᱣ ᱞᱟᱜᱤᱫ ᱠᱚ", "gidra ko parhaw lagid ko"],
    ["You should speak Santali", "ᱟᱢ ᱥᱟᱱᱛᱟᱲᱤ ᱨᱚᱲ ᱞᱟᱜᱤᱫ ᱟᱢ", "am santari ror lagid am"],
    ["He should not lie", "ᱩᱱᱤ ᱵᱟᱝ ᱢᱤᱪᱷᱟᱹ ᱨᱚᱲ ᱞᱟᱜᱤᱫ ᱮ", "uni bang michha ror lagid e"],
    ["We should respect elders", "ᱟᱞᱮ ᱢᱟᱨᱟᱝ ᱦᱚᱲ ᱠᱮ ᱢᱟᱱ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "ale marang hor ke man lagid ale"],
    ["You should drink water", "ᱟᱢ ᱫᱟᱜ ᱧᱩ ᱞᱟᱜᱤᱫ ᱟᱢ", "am dag nyu lagid am"],
    ["I should not be late", "ᱤᱧ ᱵᱟᱝ ᱞᱮᱴ ᱞᱟᱜᱤᱫ ᱟ", "inj bang let lagid a"],
    ["She should write the letter", "ᱩᱱᱤ ᱪᱤᱴᱷᱤ ᱚᱞ ᱞᱟᱜᱤᱫ ᱮ", "uni chithi ol lagid e"],
    ["We should plant trees", "ᱟᱞᱮ ᱫᱟᱨᱮ ᱛᱟᱞᱟ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "ale dare tala lagid ale"],
    ["He should come today", "ᱩᱱᱤ ᱟᱡ ᱦᱤᱡᱩᱜ ᱞᱟᱜᱤᱫ ᱮ", "uni aj hijug lagid e"],
    ["You should not fight", "ᱟᱢ ᱵᱟᱝ ᱞᱟᱲᱟᱭ ᱞᱟᱜᱤᱫ ᱟᱢ", "am bang laray lagid am"],
    ["I should learn this", "ᱤᱧ ᱱᱚᱣᱟ ᱥᱮᱪᱮᱫ ᱞᱟᱜᱤᱫ ᱟ", "inj nowa seced lagid a"],
    ["They should return the book", "ᱩᱱᱠᱩ ᱯᱩᱛᱷᱤ ᱨᱩᱣᱟᱹᱲ ᱞᱟᱜᱤᱫ ᱠᱚ", "unku puthi ruwar lagid ko"]
]

# 553 - Using "Must"
LESSONS[553] = [
    ["I must go now", "ᱤᱧ ᱱᱤᱛ ᱥᱮᱱ ᱞᱟᱜᱤᱫ ᱟ", "inj nit sen lagid a"],
    ["You must eat food", "ᱟᱢ ᱡᱚᱢ ᱡᱚᱢ ᱞᱟᱜᱤᱫ ᱟᱢ", "am jom jom lagid am"],
    ["He must study hard", "ᱩᱱᱤ ᱟᱹᱰᱤ ᱯᱟᱲᱦᱟᱣ ᱞᱟᱜᱤᱫ ᱮ", "uni adi parhaw lagid e"],
    ["She must come on time", "ᱩᱱᱤ ᱵᱮᱞᱟ ᱨᱮ ᱦᱤᱡᱩᱜ ᱞᱟᱜᱤᱫ ᱮ", "uni bela re hijug lagid e"],
    ["We must finish this work", "ᱟᱞᱮ ᱱᱚᱣᱟ ᱠᱟᱹᱢᱤ ᱛᱮᱭᱟᱨ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "ale nowa kami teyar lagid ale"],
    ["They must obey the rules", "ᱩᱱᱠᱩ ᱱᱤᱭᱚᱢ ᱢᱟᱱ ᱞᱟᱜᱤᱫ ᱠᱚ", "unku niyom man lagid ko"],
    ["You must speak the truth", "ᱟᱢ ᱥᱟᱹᱨᱤ ᱨᱚᱲ ᱞᱟᱜᱤᱫ ᱟᱢ", "am sari ror lagid am"],
    ["I must return tomorrow", "ᱤᱧ ᱜᱟᱯᱟ ᱨᱩᱣᱟᱹᱲ ᱞᱟᱜᱤᱫ ᱟ", "inj gapa ruwar lagid a"],
    ["He must pay the money", "ᱩᱱᱤ ᱴᱟᱠᱟ ᱮᱢ ᱞᱟᱜᱤᱫ ᱮ", "uni taka em lagid e"],
    ["She must take medicine", "ᱩᱱᱤ ᱟᱜ ᱧᱩ ᱞᱟᱜᱤᱫ ᱮ", "uni ag nyu lagid e"],
    ["We must protect the forest", "ᱟᱞᱮ ᱵᱤᱨ ᱨᱟᱹᱠᱷᱟ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "ale bir rakha lagid ale"],
    ["Children must respect elders", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱢᱟᱨᱟᱝ ᱦᱚᱲ ᱠᱮ ᱢᱟᱱ ᱞᱟᱜᱤᱫ ᱠᱚ", "gidra ko marang hor ke man lagid ko"],
    ["You must not steal", "ᱟᱢ ᱪᱚᱨ ᱵᱟᱝ ᱞᱟᱜᱤᱫ ᱟᱢ", "am chor bang lagid am"],
    ["I must save water", "ᱤᱧ ᱫᱟᱜ ᱵᱟᱸᱪᱟᱣ ᱞᱟᱜᱤᱫ ᱟ", "inj dag banchaw lagid a"],
    ["She must attend school", "ᱩᱱᱤ ᱥᱠᱩᱞ ᱥᱮᱱ ᱞᱟᱜᱤᱫ ᱮ", "uni skul sen lagid e"],
    ["We must love our country", "ᱟᱞᱮ ᱟᱞᱮᱭᱟᱜ ᱫᱤᱥᱚᱢ ᱫᱩᱞᱟᱹᱲ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "ale aleyag disom dular lagid ale"],
    ["He must apologize", "ᱩᱱᱤ ᱢᱟᱹᱧᱡᱷᱤ ᱠᱩᱞᱤ ᱞᱟᱜᱤᱫ ᱮ", "uni manjhi kuli lagid e"],
    ["I must not forget", "ᱤᱧ ᱵᱟᱝ ᱦᱮᱡ ᱠᱟᱹ ᱞᱟᱜᱤᱫ ᱟ", "inj bang hej ka lagid a"]
]

# 554 - "To keep doing"
LESSONS[554] = [
    ["Keep going", "ᱥᱮᱱ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "sen taheny me"],
    ["Keep eating", "ᱡᱚᱢ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "jom taheny me"],
    ["Keep reading", "ᱯᱟᱲᱦᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "parhaw taheny me"],
    ["Keep working", "ᱠᱟᱹᱢᱤ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "kami taheny me"],
    ["He kept walking", "ᱩᱱᱤ ᱥᱟᱞᱟᱜ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni salag taheny e"],
    ["She kept singing", "ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni sereny taheny e"],
    ["I keep trying", "ᱤᱧ ᱪᱮᱥᱴᱟ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj chesta taheny a"],
    ["They kept waiting", "ᱩᱱᱠᱩ ᱡᱚᱜᱟᱹᱣ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "unku jogaw taheny ko"],
    ["Keep speaking Santali", "ᱥᱟᱱᱛᱟᱲᱤ ᱨᱚᱲ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "santari ror taheny me"],
    ["I kept writing all day", "ᱤᱧ ᱥᱟᱹᱨᱟᱹ ᱫᱤᱱ ᱚᱞ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj sara din ol taheny a"],
    ["She kept cooking", "ᱩᱱᱤ ᱨᱟᱸᱰᱷᱟ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni randha taheny e"],
    ["He kept running", "ᱩᱱᱤ ᱫᱟᱹᱲ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni dar taheny e"],
    ["Keep learning", "ᱥᱮᱪᱮᱫ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "seced taheny me"],
    ["I will keep coming", "ᱤᱧ ᱦᱤᱡᱩᱜ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj hijug taheny a"],
    ["She kept crying", "ᱩᱱᱤ ᱨᱟᱹᱢ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni ram taheny e"],
    ["Keep practicing", "ᱟᱵᱷᱤᱭᱟᱥ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "abhiyas taheny me"],
    ["He kept dancing", "ᱩᱱᱤ ᱮᱱᱮᱡ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni enej taheny e"],
    ["We will keep helping", "ᱟᱞᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale sagay taheny ale"]
]

# 555 - Comparison and degrees
LESSONS[555] = [
    ["He is taller than me", "ᱩᱱᱤ ᱤᱧ ᱠᱷᱚᱱ ᱡᱟᱱᱟᱝ ᱠᱟᱱᱟ", "uni inj khon janang kana"],
    ["This house is bigger", "ᱱᱚᱣᱟ ᱚᱲᱟᱜ ᱟᱹᱰᱤ ᱢᱟᱨᱟᱝ ᱠᱟᱱᱟ", "nowa orag adi marang kana"],
    ["She runs faster than him", "ᱩᱱᱤ ᱩᱱᱤ ᱠᱷᱚᱱ ᱡᱚᱨ ᱫᱟᱹᱲ ᱮ", "uni uni khon jor dar e"],
    ["This is the best food", "ᱱᱚᱣᱟ ᱡᱚᱛᱚ ᱠᱷᱚᱱ ᱵᱷᱟᱞᱮ ᱡᱚᱢ ᱠᱟᱱᱟ", "nowa joto khon bhale jom kana"],
    ["That hill is the tallest", "ᱚᱱᱟ ᱵᱩᱨᱩ ᱡᱚᱛᱚ ᱠᱷᱚᱱ ᱡᱟᱱᱟᱝ ᱠᱟᱱᱟ", "ona buru joto khon janang kana"],
    ["My village is more beautiful", "ᱤᱧᱟᱜ ᱟᱹᱛᱩ ᱟᱹᱰᱤ ᱥᱚᱢᱵᱷᱟᱨ ᱠᱟᱱᱟ", "injag atu adi sombhar kana"],
    ["He is stronger than me", "ᱩᱱᱤ ᱤᱧ ᱠᱷᱚᱱ ᱡᱚᱨ ᱠᱟᱱᱟ", "uni inj khon jor kana"],
    ["This river is longer", "ᱱᱚᱣᱟ ᱜᱟᱰᱟ ᱟᱹᱰᱤ ᱡᱟᱱᱟᱝ ᱠᱟᱱᱟ", "nowa gada adi janang kana"],
    ["She is the most intelligent", "ᱩᱱᱤ ᱡᱚᱛᱚ ᱠᱷᱚᱱ ᱵᱩᱫᱷᱤ ᱠᱟᱱᱟ", "uni joto khon budhi kana"],
    ["Today is hotter than yesterday", "ᱟᱡ ᱜᱟᱞᱟ ᱠᱷᱚᱱ ᱫᱩᱨᱩᱵ ᱠᱟᱱᱟ", "aj gala khon durub kana"],
    ["This book is thicker", "ᱱᱚᱣᱟ ᱯᱩᱛᱷᱤ ᱟᱹᱰᱤ ᱢᱚᱴᱟ ᱠᱟᱱᱟ", "nowa puthi adi mota kana"],
    ["Iron is harder than wood", "ᱞᱚᱦᱟ ᱫᱟᱨᱮ ᱠᱷᱚᱱ ᱡᱚᱨ ᱠᱟᱱᱟ", "loha dare khon jor kana"],
    ["She sings better than him", "ᱩᱱᱤ ᱩᱱᱤ ᱠᱷᱚᱱ ᱵᱷᱟᱞᱮ ᱥᱮᱨᱮᱧ ᱮ", "uni uni khon bhale sereny e"],
    ["This is the smallest house", "ᱱᱚᱣᱟ ᱡᱚᱛᱚ ᱠᱷᱚᱱ ᱦᱩᱰᱤᱧ ᱚᱲᱟᱜ ᱠᱟᱱᱟ", "nowa joto khon huding orag kana"],
    ["He eats more than me", "ᱩᱱᱤ ᱤᱧ ᱠᱷᱚᱱ ᱟᱹᱰᱤ ᱡᱚᱢ ᱮ", "uni inj khon adi jom e"],
    ["Mango is sweeter than guava", "ᱟᱹᱢ ᱯᱮᱭᱟᱨᱟ ᱠᱷᱚᱱ ᱢᱤᱴᱷᱟᱹ ᱠᱟᱱᱟ", "am peyara khon mitha kana"],
    ["This is as big as that", "ᱱᱚᱣᱟ ᱚᱱᱟ ᱞᱮᱠᱟ ᱢᱟᱨᱟᱝ ᱠᱟᱱᱟ", "nowa ona leka marang kana"],
    ["He is the oldest person here", "ᱩᱱᱤ ᱱᱮᱛᱟᱨ ᱡᱚᱛᱚ ᱠᱷᱚᱱ ᱵᱩᱲᱷᱟ ᱠᱟᱱᱟ", "uni netar joto khon burha kana"]
]

# 556 - Using "To Know"
LESSONS[556] = [
    ["I know", "ᱤᱧ ᱵᱟᱰᱟᱭ ᱟ", "inj baday a"],
    ["I don't know", "ᱤᱧ ᱵᱟᱝ ᱵᱟᱰᱟᱭ ᱟ", "inj bang baday a"],
    ["Do you know?", "ᱟᱢ ᱵᱟᱰᱟᱭ ᱟᱢ?", "am baday am?"],
    ["He knows the way", "ᱩᱱᱤ ᱨᱟᱦᱟ ᱵᱟᱰᱟᱭ ᱮ", "uni raha baday e"],
    ["She knows Santali", "ᱩᱱᱤ ᱥᱟᱱᱛᱟᱲᱤ ᱵᱟᱰᱟᱭ ᱮ", "uni santari baday e"],
    ["I know how to cook", "ᱤᱧ ᱨᱟᱸᱰᱷᱟ ᱵᱟᱰᱟᱭ ᱟ", "inj randha baday a"],
    ["He doesn't know how to swim", "ᱩᱱᱤ ᱫᱟᱹᱲ ᱵᱟᱝ ᱵᱟᱰᱟᱭ ᱮ", "uni dar bang baday e"],
    ["They know our village", "ᱩᱱᱠᱩ ᱟᱞᱮᱭᱟᱜ ᱟᱹᱛᱩ ᱵᱟᱰᱟᱭ ᱠᱚ", "unku aleyag atu baday ko"],
    ["I know this song", "ᱤᱧ ᱱᱚᱣᱟ ᱥᱮᱨᱮᱧ ᱵᱟᱰᱟᱭ ᱟ", "inj nowa sereny baday a"],
    ["She knows how to weave", "ᱩᱱᱤ ᱵᱩᱱ ᱵᱟᱰᱟᱭ ᱮ", "uni bun baday e"],
    ["I know his name", "ᱤᱧ ᱩᱱᱤᱭᱟᱜ ᱧᱩᱛᱩᱢ ᱵᱟᱰᱟᱭ ᱟ", "inj uniag nyutum baday a"],
    ["Do you know how to write Ol Chiki?", "ᱟᱢ ᱚᱞ ᱪᱤᱠᱤ ᱚᱞ ᱵᱟᱰᱟᱭ ᱟᱢ?", "am ol chiki ol baday am?"],
    ["He knows the answer", "ᱩᱱᱤ ᱡᱟᱣᱟᱵ ᱵᱟᱰᱟᱭ ᱮ", "uni jawab baday e"],
    ["I don't know the way to the village", "ᱤᱧ ᱟᱹᱛᱩ ᱨᱟᱦᱟ ᱵᱟᱝ ᱵᱟᱰᱟᱭ ᱟ", "inj atu raha bang baday a"],
    ["She knows how to dance", "ᱩᱱᱤ ᱮᱱᱮᱡ ᱵᱟᱰᱟᱭ ᱮ", "uni enej baday e"],
    ["We know this story", "ᱟᱞᱮ ᱱᱚᱣᱟ ᱠᱟᱹᱦᱱᱤ ᱵᱟᱰᱟᱭ ᱟᱞᱮ", "ale nowa kahni baday ale"],
    ["Nobody knows", "ᱡᱟᱦᱟᱸ ᱵᱟᱝ ᱵᱟᱰᱟᱭ", "jahang bang baday"],
    ["I got to know (came to know)", "ᱤᱧ ᱵᱟᱰᱟᱭ ᱮᱱᱟ", "inj baday ena"]
]

# 557 - Using "Let" and "Shall we"
LESSONS[557] = [
    ["Let me go", "ᱤᱧ ᱠᱮ ᱥᱮᱱ ᱮᱢ ᱢᱮ", "inj ke sen em me"],
    ["Let him eat", "ᱩᱱᱤ ᱠᱮ ᱡᱚᱢ ᱮᱢ ᱢᱮ", "uni ke jom em me"],
    ["Let her come", "ᱩᱱᱤ ᱠᱮ ᱦᱤᱡᱩᱜ ᱮᱢ ᱢᱮ", "uni ke hijug em me"],
    ["Let them play", "ᱩᱱᱠᱩ ᱠᱮ ᱮᱱᱮᱡ ᱮᱢ ᱢᱮ", "unku ke enej em me"],
    ["Shall we go?", "ᱟᱞᱮ ᱥᱮᱱ ᱟᱞᱮ?", "ale sen ale?"],
    ["Shall we eat?", "ᱟᱞᱮ ᱡᱚᱢ ᱟᱞᱮ?", "ale jom ale?"],
    ["Let's study together", "ᱟᱞᱮ ᱥᱟᱶᱛᱮ ᱯᱟᱲᱦᱟᱣ ᱟᱞᱮ", "ale sawte parhaw ale"],
    ["Let me rest", "ᱤᱧ ᱠᱮ ᱥᱮᱨᱮᱧ ᱮᱢ ᱢᱮ", "inj ke sereny em me"],
    ["Let the children play", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱠᱮ ᱮᱱᱮᱡ ᱮᱢ ᱢᱮ", "gidra ko ke enej em me"],
    ["Shall we dance?", "ᱟᱞᱮ ᱮᱱᱮᱡ ᱟᱞᱮ?", "ale enej ale?"],
    ["Let me try", "ᱤᱧ ᱠᱮ ᱪᱮᱥᱴᱟ ᱮᱢ ᱢᱮ", "inj ke chesta em me"],
    ["Let her speak", "ᱩᱱᱤ ᱠᱮ ᱨᱚᱲ ᱮᱢ ᱢᱮ", "uni ke ror em me"],
    ["Shall we sing?", "ᱟᱞᱮ ᱥᱮᱨᱮᱧ ᱟᱞᱮ?", "ale sereny ale?"],
    ["Let's go to the forest", "ᱟᱞᱮ ᱵᱤᱨ ᱥᱮᱱ ᱟᱞᱮ", "ale bir sen ale"],
    ["Let him write", "ᱩᱱᱤ ᱠᱮ ᱚᱞ ᱮᱢ ᱢᱮ", "uni ke ol em me"],
    ["Shall we celebrate?", "ᱟᱞᱮ ᱢᱟᱱᱟᱣ ᱟᱞᱮ?", "ale manaw ale?"],
    ["Let me think", "ᱤᱧ ᱠᱮ ᱢᱚᱱᱮ ᱮᱢ ᱢᱮ", "inj ke mone em me"],
    ["Let's help each other", "ᱟᱞᱮ ᱢᱤᱫ ᱟᱨ ᱢᱤᱫ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱟᱞᱮ", "ale mid ar mid ke sagay ale"]
]

# 558 - Which-That / What-That sentences
LESSONS[558] = [
    ["The man who came is my friend", "ᱚᱱᱟ ᱦᱚᱲ ᱚᱠᱚᱭ ᱦᱤᱡᱩᱜ ᱮᱱᱟ ᱩᱱᱤ ᱤᱧᱟᱜ ᱥᱟᱶᱛᱟ ᱠᱟᱱᱟ", "ona hor okoy hijug ena uni injag sawta kana"],
    ["The book that I read was good", "ᱚᱱᱟ ᱯᱩᱛᱷᱤ ᱡᱟᱦᱟᱸ ᱤᱧ ᱯᱟᱲᱦᱟᱣ ᱮᱱᱟ ᱚᱱᱟ ᱵᱷᱟᱞᱮ ᱛᱟᱦᱮᱸᱱ ᱟ", "ona puthi jahang inj parhaw ena ona bhale taheny a"],
    ["What I said is true", "ᱤᱧ ᱡᱟᱦᱟᱸ ᱨᱚᱲ ᱮᱱᱟ ᱚᱱᱟ ᱥᱟᱹᱨᱤ ᱠᱟᱱᱟ", "inj jahang ror ena ona sari kana"],
    ["The village where I was born is far", "ᱚᱱᱟ ᱟᱹᱛᱩ ᱚᱠᱟ ᱨᱮ ᱤᱧ ᱡᱟᱱᱟᱢ ᱦᱩᱭ ᱮᱱᱟ ᱚᱱᱟ ᱫᱩᱨ ᱠᱟᱱᱟ", "ona atu oka re inj janam huy ena ona dur kana"],
    ["That which is sweet tastes good", "ᱚᱱᱟ ᱡᱟᱦᱟᱸ ᱢᱤᱴᱷᱟᱹ ᱚᱱᱟ ᱵᱷᱟᱞᱮ ᱞᱟᱜᱟ", "ona jahang mitha ona bhale laga"],
    ["The person who helps is good", "ᱚᱱᱟ ᱦᱚᱲ ᱚᱠᱚᱭ ᱥᱟᱹᱜᱟᱹᱭ ᱮ ᱩᱱᱤ ᱵᱷᱟᱞᱮ ᱠᱟᱱᱟ", "ona hor okoy sagay e uni bhale kana"],
    ["The food that mother cooked was tasty", "ᱚᱱᱟ ᱡᱚᱢ ᱡᱟᱦᱟᱸ ᱟᱭᱚ ᱨᱟᱸᱰᱷᱟ ᱮᱱᱟ ᱚᱱᱟ ᱫᱷᱟᱹᱨᱤ ᱛᱟᱦᱮᱸᱱ ᱟ", "ona jom jahang ayo randha ena ona dhari taheny a"],
    ["Whatever you want, take it", "ᱟᱢ ᱡᱟᱦᱟᱸ ᱥᱟᱱᱟᱢ ᱟᱢ ᱚᱱᱟ ᱤᱫᱤ ᱢᱮ", "am jahang sanam am ona idi me"],
    ["The teacher who taught us was kind", "ᱚᱱᱟ ᱯᱟᱲᱦᱟᱣᱮᱫ ᱚᱠᱚᱭ ᱟᱞᱮ ᱠᱮ ᱯᱟᱲᱦᱟᱣ ᱮᱱᱟ ᱩᱱᱤ ᱵᱷᱟᱞᱮ ᱛᱟᱦᱮᱸᱱ ᱮ", "ona parhawed okoy ale ke parhaw ena uni bhale taheny e"],
    ["The house which is red is mine", "ᱚᱱᱟ ᱚᱲᱟᱜ ᱡᱟᱦᱟᱸ ᱟᱨᱟᱜ ᱚᱱᱟ ᱤᱧᱟᱜ ᱠᱟᱱᱟ", "ona orag jahang arag ona injag kana"],
    ["I know what happened", "ᱤᱧ ᱵᱟᱰᱟᱭ ᱟ ᱪᱮᱫ ᱦᱩᱭ ᱮᱱᱟ", "inj baday a ced huy ena"],
    ["The river that flows here is clean", "ᱚᱱᱟ ᱜᱟᱰᱟ ᱡᱟᱦᱟᱸ ᱱᱮᱛᱟᱨ ᱵᱟᱦᱟ ᱮ ᱚᱱᱟ ᱥᱟᱯᱷᱟ ᱠᱟᱱᱟ", "ona gada jahang netar baha e ona sapha kana"],
    ["Whoever comes, tell me", "ᱡᱟᱦᱟᱸ ᱦᱤᱡᱩᱜ ᱮ ᱤᱧ ᱠᱮ ᱨᱚᱲ ᱢᱮ", "jahang hijug e inj ke ror me"],
    ["What she said was right", "ᱩᱱᱤ ᱡᱟᱦᱟᱸ ᱨᱚᱲ ᱮᱱᱟ ᱚᱱᱟ ᱵᱷᱟᱞᱮ ᱛᱟᱦᱮᱸᱱ ᱟ", "uni jahang ror ena ona bhale taheny a"],
    ["The bird that sings is beautiful", "ᱚᱱᱟ ᱪᱮᱨᱮ ᱡᱟᱦᱟᱸ ᱥᱮᱨᱮᱧ ᱮ ᱚᱱᱟ ᱥᱚᱢᱵᱷᱟᱨ ᱠᱟᱱᱟ", "ona cere jahang sereny e ona sombhar kana"],
    ["Whatever he does, he does well", "ᱩᱱᱤ ᱡᱟᱦᱟᱸ ᱠᱟᱹᱢᱤ ᱠᱮᱫ ᱮ ᱵᱷᱟᱞᱮ ᱠᱮᱫ ᱮ", "uni jahang kami ked e bhale ked e"],
    ["The path that leads to the hill is narrow", "ᱚᱱᱟ ᱨᱟᱦᱟ ᱡᱟᱦᱟᱸ ᱵᱩᱨᱩ ᱛᱮ ᱥᱮᱱ ᱟ ᱚᱱᱟ ᱪᱤᱯᱤᱴ ᱠᱟᱱᱟ", "ona raha jahang buru te sen a ona chipit kana"],
    ["That which is mine is yours too", "ᱡᱟᱦᱟᱸ ᱤᱧᱟᱜ ᱠᱟᱱᱟ ᱚᱱᱟ ᱟᱢᱟᱜ ᱦᱚᱭ ᱠᱟᱱᱟ", "jahang injag kana ona amag hoy kana"]
]

# 559 - Giving instructions formally
LESSONS[559] = [
    ["Please sit down", "ᱦᱮᱡ ᱫᱩᱲᱩᱵ ᱢᱮ", "hej durub me"],
    ["Please listen carefully", "ᱦᱮᱡ ᱵᱷᱟᱞᱮ ᱞᱮᱠᱟ ᱟᱹᱭᱠᱟᱹᱣ ᱢᱮ", "hej bhale leka aykaw me"],
    ["Please read this aloud", "ᱱᱚᱣᱟ ᱡᱚᱨ ᱨᱮ ᱯᱟᱲᱦᱟᱣ ᱢᱮ", "nowa jor re parhaw me"],
    ["Please write your name", "ᱟᱢᱟᱜ ᱧᱩᱛᱩᱢ ᱚᱞ ᱢᱮ", "amag nyutum ol me"],
    ["Please open your books", "ᱟᱢᱟᱜ ᱯᱩᱛᱷᱤ ᱡᱷᱤᱡ ᱢᱮ", "amag puthi jhij me"],
    ["Please come on time", "ᱵᱮᱞᱟ ᱨᱮ ᱦᱤᱡᱩᱜ ᱢᱮ", "bela re hijug me"],
    ["Please be quiet", "ᱛᱤᱥᱤᱧ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "tising taheny me"],
    ["Please speak slowly", "ᱟᱹᱭᱥᱛᱮ ᱨᱚᱲ ᱢᱮ", "ayste ror me"],
    ["Please wait here", "ᱱᱮᱛᱟᱨ ᱡᱚᱜᱟᱹᱣ ᱢᱮ", "netar jogaw me"],
    ["Please close the door", "ᱫᱩᱣᱟᱹᱨ ᱫᱟᱸᱰ ᱢᱮ", "duwar dand me"],
    ["Please fill in the form", "ᱯᱷᱚᱨᱢ ᱵᱷᱚᱨᱛᱤ ᱢᱮ", "phorm bhorti me"],
    ["Please submit your assignment", "ᱟᱢᱟᱜ ᱠᱟᱹᱢᱤ ᱡᱚᱢᱟ ᱢᱮ", "amag kami joma me"],
    ["Please stand in a line", "ᱞᱟᱤᱱ ᱨᱮ ᱛᱤᱧᱜᱩ ᱢᱮ", "lain re tingu me"],
    ["Please answer the question", "ᱠᱩᱞᱤ ᱡᱟᱣᱟᱵ ᱮᱢ ᱢᱮ", "kuli jawab em me"],
    ["Please raise your hand", "ᱟᱢᱟᱜ ᱛᱤᱸ ᱴᱷᱟᱲᱟᱣ ᱢᱮ", "amag ting tharaw me"],
    ["Please show your ID", "ᱟᱢᱟᱜ ᱟᱭᱰᱤ ᱫᱮᱠᱷᱟᱣ ᱢᱮ", "amag ID dekhaw me"],
    ["Please take your seat", "ᱟᱢᱟᱜ ᱡᱟᱭᱜᱟ ᱨᱮ ᱫᱩᱲᱩᱵ ᱢᱮ", "amag jayga re durub me"],
    ["Please sign here", "ᱱᱮᱛᱟᱨ ᱥᱟᱭᱤᱱ ᱢᱮ", "netar sayin me"]
]

# 560 - Using "To Like"
LESSONS[560] = [
    ["I like this", "ᱤᱧ ᱱᱚᱣᱟ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "inj nowa raska a"],
    ["I like food", "ᱤᱧ ᱡᱚᱢ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "inj jom raska a"],
    ["He likes to play", "ᱩᱱᱤ ᱮᱱᱮᱡ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "uni enej raska e"],
    ["She likes flowers", "ᱩᱱᱤ ᱵᱟᱦᱟ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "uni baha raska e"],
    ["We like singing", "ᱟᱞᱮ ᱥᱮᱨᱮᱧ ᱨᱟᱹᱥᱠᱟᱹ ᱟᱞᱮ", "ale sereny raska ale"],
    ["They like festivals", "ᱩᱱᱠᱩ ᱯᱚᱨᱚᱵ ᱨᱟᱹᱥᱠᱟᱹ ᱠᱚ", "unku porob raska ko"],
    ["I don't like this", "ᱤᱧ ᱱᱚᱣᱟ ᱵᱟᱝ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "inj nowa bang raska a"],
    ["Do you like tea?", "ᱟᱢ ᱪᱟᱹ ᱨᱟᱹᱥᱠᱟᱹ ᱟᱢ?", "am cha raska am?"],
    ["Children like sweets", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱡᱤᱞᱤᱯᱤ ᱨᱟᱹᱥᱠᱟᱹ ᱠᱚ", "gidra ko jilipi raska ko"],
    ["I like rainy days", "ᱤᱧ ᱫᱟᱜ ᱫᱟᱹᱲ ᱫᱤᱱ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "inj dag dar din raska a"],
    ["She likes to dance", "ᱩᱱᱤ ᱮᱱᱮᱡ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "uni enej raska e"],
    ["He likes the forest", "ᱩᱱᱤ ᱵᱤᱨ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "uni bir raska e"],
    ["I like this village", "ᱤᱧ ᱱᱚᱣᱟ ᱟᱹᱛᱩ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "inj nowa atu raska a"],
    ["We like learning Santali", "ᱟᱞᱮ ᱥᱟᱱᱛᱟᱲᱤ ᱥᱮᱪᱮᱫ ᱨᱟᱹᱥᱠᱟᱹ ᱟᱞᱮ", "ale santari seced raska ale"],
    ["He doesn't like cold weather", "ᱩᱱᱤ ᱫᱷᱤᱨᱤ ᱵᱟᱝ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "uni dhiri bang raska e"],
    ["I like reading books", "ᱤᱧ ᱯᱩᱛᱷᱤ ᱯᱟᱲᱦᱟᱣ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "inj puthi parhaw raska a"],
    ["She likes to help people", "ᱩᱱᱤ ᱦᱚᱲ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "uni hor ke sagay raska e"],
    ["Do they like the song?", "ᱩᱱᱠᱩ ᱥᱮᱨᱮᱧ ᱨᱟᱹᱥᱠᱟᱹ ᱠᱚ?", "unku sereny raska ko?"]
]

for ch in d:
    if ch['id'] in LESSONS:
        ch['blocks'] = [{"type": "table", "columns": ["English", "Santali (Ol Chiki)", "Transliteration"], "rows": LESSONS[ch['id']]}]

open('data_santali.json', 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('Section 3a (543-560) populated')
