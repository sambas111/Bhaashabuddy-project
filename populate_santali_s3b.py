import json

d = json.load(open('data_santali.json', 'r', encoding='utf-8'))

LESSONS = {}

# 561 - Sentences using "would"
LESSONS[561] = [
    ["I would go if you come", "ᱟᱢ ᱦᱤᱡᱩᱜ ᱨᱮᱫᱚ ᱤᱧ ᱥᱮᱱ ᱟ", "am hijug redo inj sen a"],
    ["He would help if asked", "ᱩᱱᱤ ᱠᱮ ᱠᱩᱞᱤ ᱨᱮᱫᱚ ᱩᱱᱤ ᱥᱟᱹᱜᱟᱹᱭ ᱮ", "uni ke kuli redo uni sagay e"],
    ["She would come tomorrow", "ᱩᱱᱤ ᱜᱟᱯᱟ ᱦᱤᱡᱩᱜ ᱮ", "uni gapa hijug e"],
    ["I would like some tea", "ᱤᱧ ᱪᱟᱹ ᱥᱟᱱᱟᱢ ᱟ", "inj cha sanam a"],
    ["We would celebrate if it stops raining", "ᱫᱟᱜ ᱛᱷᱤᱨ ᱨᱮᱫᱚ ᱟᱞᱮ ᱢᱟᱱᱟᱣ ᱟᱞᱮ", "dag thir redo ale manaw ale"],
    ["He would study if teacher came", "ᱯᱟᱲᱦᱟᱣᱮᱫ ᱦᱤᱡᱩᱜ ᱨᱮᱫᱚ ᱩᱱᱤ ᱯᱟᱲᱦᱟᱣ ᱮ", "parhawed hijug redo uni parhaw e"],
    ["She would cook if we bring ingredients", "ᱟᱞᱮ ᱡᱤᱱᱤᱥ ᱟᱹᱜᱩ ᱨᱮᱫᱚ ᱩᱱᱤ ᱨᱟᱸᱰᱷᱟ ᱮ", "ale jinis agu redo uni randha e"],
    ["I would come if I had time", "ᱤᱧᱟᱜ ᱵᱮᱞᱟ ᱢᱮᱱᱟᱜ ᱨᱮᱫᱚ ᱤᱧ ᱦᱤᱡᱩᱜ ᱟ", "injag bela menag redo inj hijug a"],
    ["Would you like to eat?", "ᱟᱢ ᱡᱚᱢ ᱥᱟᱱᱟᱢ ᱟᱢ?", "am jom sanam am?"],
    ["He would speak Santali if he knew", "ᱩᱱᱤ ᱵᱟᱰᱟᱭ ᱨᱮᱫᱚ ᱩᱱᱤ ᱥᱟᱱᱛᱟᱲᱤ ᱨᱚᱲ ᱮ", "uni baday redo uni santari ror e"],
    ["I would buy if the price was less", "ᱫᱟᱢ ᱠᱚᱢ ᱨᱮᱫᱚ ᱤᱧ ᱠᱤᱱ ᱟ", "dam kom redo inj kin a"],
    ["She would rest if she was tired", "ᱩᱱᱤ ᱛᱷᱟᱠᱟᱣ ᱨᱮᱫᱚ ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱮ", "uni thakaw redo uni sereny e"],
    ["Would you help me?", "ᱟᱢ ᱤᱧ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱟᱢ?", "am inj ke sagay am?"],
    ["I would be happy if you came", "ᱟᱢ ᱦᱤᱡᱩᱜ ᱨᱮᱫᱚ ᱤᱧ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "am hijug redo inj raska a"],
    ["They would dance at the festival", "ᱩᱱᱠᱩ ᱯᱚᱨᱚᱵ ᱨᱮ ᱮᱱᱮᱡ ᱠᱚ", "unku porob re enej ko"],
    ["I would write a letter", "ᱤᱧ ᱪᱤᱴᱷᱤ ᱚᱞ ᱟ", "inj chithi ol a"],
    ["She would sing if you asked", "ᱟᱢ ᱠᱩᱞᱤ ᱨᱮᱫᱚ ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱮ", "am kuli redo uni sereny e"],
    ["We would visit the village", "ᱟᱞᱮ ᱟᱹᱛᱩ ᱥᱮᱱ ᱟᱞᱮ", "ale atu sen ale"]
]

# 562 - "To Understand" & "To come to know"
LESSONS[562] = [
    ["I understand", "ᱤᱧ ᱵᱩᱡᱷᱟᱹᱣ ᱟ", "inj bujhaw a"],
    ["I don't understand", "ᱤᱧ ᱵᱟᱝ ᱵᱩᱡᱷᱟᱹᱣ ᱟ", "inj bang bujhaw a"],
    ["Do you understand?", "ᱟᱢ ᱵᱩᱡᱷᱟᱹᱣ ᱟᱢ?", "am bujhaw am?"],
    ["He understood everything", "ᱩᱱᱤ ᱡᱚᱛᱚ ᱵᱩᱡᱷᱟᱹᱣ ᱮᱱᱟ", "uni joto bujhaw ena"],
    ["She didn't understand", "ᱩᱱᱤ ᱵᱟᱝ ᱵᱩᱡᱷᱟᱹᱣ ᱮᱱᱟ", "uni bang bujhaw ena"],
    ["I came to know the truth", "ᱤᱧ ᱥᱟᱹᱨᱤ ᱵᱟᱰᱟᱭ ᱮᱱᱟ", "inj sari baday ena"],
    ["He came to know later", "ᱩᱱᱤ ᱛᱟᱭᱚᱢ ᱵᱟᱰᱟᱭ ᱮᱱᱟ", "uni tayom baday ena"],
    ["I understand Santali", "ᱤᱧ ᱥᱟᱱᱛᱟᱲᱤ ᱵᱩᱡᱷᱟᱹᱣ ᱟ", "inj santari bujhaw a"],
    ["She understood the problem", "ᱩᱱᱤ ᱢᱩᱥᱠᱤᱞ ᱵᱩᱡᱷᱟᱹᱣ ᱮᱱᱟ", "uni muskil bujhaw ena"],
    ["He will understand", "ᱩᱱᱤ ᱵᱩᱡᱷᱟᱹᱣ ᱮ", "uni bujhaw e"],
    ["I came to know about the festival", "ᱤᱧ ᱯᱚᱨᱚᱵ ᱵᱟᱰᱟᱭ ᱮᱱᱟ", "inj porob baday ena"],
    ["They understood the lesson", "ᱩᱱᱠᱩ ᱯᱟᱲᱦᱟᱣ ᱵᱩᱡᱷᱟᱹᱣ ᱮᱱᱟ", "unku parhaw bujhaw ena"],
    ["Please understand me", "ᱤᱧᱟᱜ ᱠᱟᱹᱛᱷᱟ ᱵᱩᱡᱷᱟᱹᱣ ᱢᱮ", "injag katha bujhaw me"],
    ["He cannot understand Hindi", "ᱩᱱᱤ ᱦᱤᱱᱫᱤ ᱵᱟᱝ ᱵᱩᱡᱷᱟᱹᱣ ᱮ", "uni Hindi bang bujhaw e"],
    ["I understood what you said", "ᱤᱧ ᱟᱢᱟᱜ ᱠᱟᱹᱛᱷᱟ ᱵᱩᱡᱷᱟᱹᱣ ᱮᱱᱟ", "inj amag katha bujhaw ena"],
    ["She came to know about him", "ᱩᱱᱤ ᱩᱱᱤ ᱵᱤᱥᱚᱭ ᱵᱟᱰᱟᱭ ᱮᱱᱟ", "uni uni bisoy baday ena"],
    ["Can you understand this?", "ᱟᱢ ᱱᱚᱣᱟ ᱵᱩᱡᱷᱟᱹᱣ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am nowa bujhaw dareyam ma?"],
    ["Now I understand clearly", "ᱱᱤᱛ ᱤᱧ ᱵᱷᱟᱞᱮ ᱵᱩᱡᱷᱟᱹᱣ ᱟ", "nit inj bhale bujhaw a"]
]

# 563 - Add a question tag
LESSONS[563] = [
    ["You are coming, aren't you?", "ᱟᱢ ᱦᱤᱡᱩᱜ ᱟᱢ, ᱦᱟᱛᱤᱭᱟᱸ?", "am hijug am, hatiyaan?"],
    ["He went, didn't he?", "ᱩᱱᱤ ᱥᱮᱱ ᱮᱱᱟ, ᱦᱟᱛᱤᱭᱟᱸ?", "uni sen ena, hatiyaan?"],
    ["This is good, isn't it?", "ᱱᱚᱣᱟ ᱵᱷᱟᱞᱮ ᱠᱟᱱᱟ, ᱦᱟᱛᱤᱭᱟᱸ?", "nowa bhale kana, hatiyaan?"],
    ["She cooked food, didn't she?", "ᱩᱱᱤ ᱡᱚᱢ ᱨᱟᱸᱰᱷᱟ ᱮᱱᱟ, ᱦᱟᱛᱤᱭᱟᱸ?", "uni jom randha ena, hatiyaan?"],
    ["It will rain, won't it?", "ᱫᱟᱜ ᱫᱟᱹᱲ ᱟ, ᱦᱟᱛᱤᱭᱟᱸ?", "dag dar a, hatiyaan?"],
    ["You know this, don't you?", "ᱟᱢ ᱱᱚᱣᱟ ᱵᱟᱰᱟᱭ ᱟᱢ, ᱦᱟᱛᱤᱭᱟᱸ?", "am nowa baday am, hatiyaan?"],
    ["They are playing, aren't they?", "ᱩᱱᱠᱩ ᱮᱱᱮᱡ ᱢᱮᱱᱟᱜ ᱟ, ᱦᱟᱛᱤᱭᱟᱸ?", "unku enej menag a, hatiyaan?"],
    ["Father will come, won't he?", "ᱟᱯᱟ ᱦᱤᱡᱩᱜ ᱮ, ᱦᱟᱛᱤᱭᱟᱸ?", "apa hijug e, hatiyaan?"],
    ["You ate, didn't you?", "ᱟᱢ ᱡᱚᱢ ᱮᱱᱟ, ᱦᱟᱛᱤᱭᱟᱸ?", "am jom ena, hatiyaan?"],
    ["The food is ready, isn't it?", "ᱡᱚᱢ ᱛᱮᱭᱟᱨ ᱢᱮᱱᱟᱜ ᱟ, ᱦᱟᱛᱤᱭᱟᱸ?", "jom teyar menag a, hatiyaan?"],
    ["She sings well, doesn't she?", "ᱩᱱᱤ ᱵᱷᱟᱞᱮ ᱥᱮᱨᱮᱧ ᱮ, ᱦᱟᱛᱤᱭᱟᱸ?", "uni bhale sereny e, hatiyaan?"],
    ["We will meet again, won't we?", "ᱟᱞᱮ ᱧᱮᱞᱚᱜ ᱟᱞᱮ, ᱦᱟᱛᱤᱭᱟᱸ?", "ale nyelog ale, hatiyaan?"],
    ["He is a good person, isn't he?", "ᱩᱱᱤ ᱵᱷᱟᱞᱮ ᱦᱚᱲ ᱠᱟᱱᱟ, ᱦᱟᱛᱤᱭᱟᱸ?", "uni bhale hor kana, hatiyaan?"],
    ["The water is cold, isn't it?", "ᱫᱟᱜ ᱫᱷᱤᱨᱤ ᱠᱟᱱᱟ, ᱦᱟᱛᱤᱭᱟᱸ?", "dag dhiri kana, hatiyaan?"],
    ["You will help me, won't you?", "ᱟᱢ ᱤᱧ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱟᱢ, ᱦᱟᱛᱤᱭᱟᱸ?", "am inj ke sagay am, hatiyaan?"],
    ["Children are playing, right?", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱮᱱᱮᱡ ᱢᱮᱱᱟᱜ ᱟ, ᱦᱟᱛᱤᱭᱟᱸ?", "gidra ko enej menag a, hatiyaan?"],
    ["This is your book, right?", "ᱱᱚᱣᱟ ᱟᱢᱟᱜ ᱯᱩᱛᱷᱤ ᱠᱟᱱᱟ, ᱦᱟᱛᱤᱭᱟᱸ?", "nowa amag puthi kana, hatiyaan?"],
    ["Mother will cook, won't she?", "ᱟᱭᱚ ᱨᱟᱸᱰᱷᱟ ᱮ, ᱦᱟᱛᱤᱭᱟᱸ?", "ayo randha e, hatiyaan?"]
]

# 564-578 (remaining pattern lessons)
LESSONS[564] = [
    ["I remember you", "ᱤᱧ ᱟᱢ ᱠᱮ ᱩᱢ ᱟᱭᱟ", "inj am ke um aya"],
    ["I don't remember", "ᱤᱧ ᱵᱟᱝ ᱩᱢ ᱟ", "inj bang um a"],
    ["Do you remember?", "ᱟᱢ ᱩᱢ ᱟᱢ?", "am um am?"],
    ["He remembers the story", "ᱩᱱᱤ ᱠᱟᱹᱦᱱᱤ ᱩᱢ ᱟᱫ ᱮ", "uni kahni um ad e"],
    ["She remembered her village", "ᱩᱱᱤ ᱩᱱᱤᱭᱟᱜ ᱟᱹᱛᱩ ᱩᱢ ᱮᱱᱟ", "uni uniag atu um ena"],
    ["I always remember my mother", "ᱤᱧ ᱡᱟᱦᱟᱸᱱᱟᱜ ᱤᱧᱟᱜ ᱟᱭᱚ ᱠᱮ ᱩᱢ ᱟᱭᱟ", "inj jahanag injag ayo ke um aya"],
    ["Please remember this", "ᱱᱚᱣᱟ ᱩᱢ ᱢᱮ", "nowa um me"],
    ["He forgot (did not remember)", "ᱩᱱᱤ ᱵᱟᱝ ᱩᱢ ᱮᱱᱟ", "uni bang um ena"],
    ["I will remember you", "ᱤᱧ ᱟᱢ ᱠᱮ ᱩᱢ ᱟ", "inj am ke um a"],
    ["She remembers the song", "ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱩᱢ ᱟᱫ ᱮ", "uni sereny um ad e"],
    ["Don't forget your book", "ᱟᱢᱟᱜ ᱯᱩᱛᱷᱤ ᱩᱢ ᱢᱮ", "amag puthi um me"],
    ["I remember the festival", "ᱤᱧ ᱯᱚᱨᱚᱵ ᱩᱢ ᱟ", "inj porob um a"],
    ["He remembered everyone", "ᱩᱱᱤ ᱡᱚᱛᱚ ᱠᱮ ᱩᱢ ᱮᱱᱟ", "uni joto ke um ena"],
    ["They don't remember the way", "ᱩᱱᱠᱩ ᱨᱟᱦᱟ ᱵᱟᱝ ᱩᱢ ᱠᱚ", "unku raha bang um ko"],
    ["I remember my childhood", "ᱤᱧ ᱤᱧᱟᱜ ᱜᱤᱫᱽᱨᱟᱹ ᱵᱮᱞᱟ ᱩᱢ ᱟ", "inj injag gidra bela um a"],
    ["Please don't forget me", "ᱤᱧ ᱠᱮ ᱩᱢ ᱢᱮ", "inj ke um me"],
    ["She will always remember", "ᱩᱱᱤ ᱡᱟᱦᱟᱸᱱᱟᱜ ᱩᱢ ᱮ", "uni jahanag um e"],
    ["I remember what you said", "ᱤᱧ ᱟᱢᱟᱜ ᱠᱟᱹᱛᱷᱟ ᱩᱢ ᱟ", "inj amag katha um a"]
]

LESSONS[565] = [
    ["I want to eat", "ᱤᱧ ᱡᱚᱢ ᱥᱟᱱᱟᱢ ᱟ", "inj jom sanam a"],
    ["I want to go", "ᱤᱧ ᱥᱮᱱ ᱥᱟᱱᱟᱢ ᱟ", "inj sen sanam a"],
    ["I want to sleep", "ᱤᱧ ᱧᱤᱫ ᱥᱟᱱᱟᱢ ᱟ", "inj nyid sanam a"],
    ["I want to read", "ᱤᱧ ᱯᱟᱲᱦᱟᱣ ᱥᱟᱱᱟᱢ ᱟ", "inj parhaw sanam a"],
    ["I want to write", "ᱤᱧ ᱚᱞ ᱥᱟᱱᱟᱢ ᱟ", "inj ol sanam a"],
    ["I need to study", "ᱤᱧ ᱯᱟᱲᱦᱟᱣ ᱞᱟᱜᱤᱫ ᱟ", "inj parhaw lagid a"],
    ["I need to work", "ᱤᱧ ᱠᱟᱹᱢᱤ ᱞᱟᱜᱤᱫ ᱟ", "inj kami lagid a"],
    ["I want to learn Santali", "ᱤᱧ ᱥᱟᱱᱛᱟᱲᱤ ᱥᱮᱪᱮᱫ ᱥᱟᱱᱟᱢ ᱟ", "inj santari seced sanam a"],
    ["I want to sing", "ᱤᱧ ᱥᱮᱨᱮᱧ ᱥᱟᱱᱟᱢ ᱟ", "inj sereny sanam a"],
    ["I need to drink water", "ᱤᱧ ᱫᱟᱜ ᱧᱩ ᱞᱟᱜᱤᱫ ᱟ", "inj dag nyu lagid a"],
    ["I want to help", "ᱤᱧ ᱥᱟᱹᱜᱟᱹᱭ ᱥᱟᱱᱟᱢ ᱟ", "inj sagay sanam a"],
    ["I want to see the village", "ᱤᱧ ᱟᱹᱛᱩ ᱧᱮᱞ ᱥᱟᱱᱟᱢ ᱟ", "inj atu nyel sanam a"],
    ["I need to rest", "ᱤᱧ ᱥᱮᱨᱮᱧ ᱞᱟᱜᱤᱫ ᱟ", "inj sereny lagid a"],
    ["I want to buy", "ᱤᱧ ᱠᱤᱱ ᱥᱟᱱᱟᱢ ᱟ", "inj kin sanam a"],
    ["I need to call", "ᱤᱧ ᱠᱩᱞ ᱞᱟᱜᱤᱫ ᱟ", "inj kul lagid a"],
    ["I want to dance", "ᱤᱧ ᱮᱱᱮᱡ ᱥᱟᱱᱟᱢ ᱟ", "inj enej sanam a"],
    ["I want to play", "ᱤᱧ ᱮᱱᱮᱡ ᱥᱟᱱᱟᱢ ᱟ", "inj enej sanam a"],
    ["I want to cook", "ᱤᱧ ᱨᱟᱸᱰᱷᱟ ᱥᱟᱱᱟᱢ ᱟ", "inj randha sanam a"]
]

LESSONS[566] = [
    ["He wants to go", "ᱩᱱᱤ ᱥᱮᱱ ᱥᱟᱱᱟᱢ ᱮ", "uni sen sanam e"],
    ["She wants to eat", "ᱩᱱᱤ ᱡᱚᱢ ᱥᱟᱱᱟᱢ ᱮ", "uni jom sanam e"],
    ["They want to play", "ᱩᱱᱠᱩ ᱮᱱᱮᱡ ᱥᱟᱱᱟᱢ ᱠᱚ", "unku enej sanam ko"],
    ["Father wants to rest", "ᱟᱯᱟ ᱥᱮᱨᱮᱧ ᱥᱟᱱᱟᱢ ᱮ", "apa sereny sanam e"],
    ["Mother wants to cook", "ᱟᱭᱚ ᱨᱟᱸᱰᱷᱟ ᱥᱟᱱᱟᱢ ᱮ", "ayo randha sanam e"],
    ["Children want milk", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱫᱩᱫᱷ ᱥᱟᱱᱟᱢ ᱠᱚ", "gidra ko dudh sanam ko"],
    ["He doesn't want to come", "ᱩᱱᱤ ᱵᱟᱝ ᱦᱤᱡᱩᱜ ᱥᱟᱱᱟᱢ ᱮ", "uni bang hijug sanam e"],
    ["She wants to learn", "ᱩᱱᱤ ᱥᱮᱪᱮᱫ ᱥᱟᱱᱟᱢ ᱮ", "uni seced sanam e"],
    ["They want to help", "ᱩᱱᱠᱩ ᱥᱟᱹᱜᱟᱹᱭ ᱥᱟᱱᱟᱢ ᱠᱚ", "unku sagay sanam ko"],
    ["He wants water", "ᱩᱱᱤ ᱫᱟᱜ ᱥᱟᱱᱟᱢ ᱮ", "uni dag sanam e"],
    ["She wants to speak", "ᱩᱱᱤ ᱨᱚᱲ ᱥᱟᱱᱟᱢ ᱮ", "uni ror sanam e"],
    ["The child wants a toy", "ᱜᱤᱫᱽᱨᱟᱹ ᱮᱱᱮᱡ ᱡᱤᱱᱤᱥ ᱥᱟᱱᱟᱢ ᱮ", "gidra enej jinis sanam e"],
    ["He wants to study more", "ᱩᱱᱤ ᱟᱨ ᱯᱟᱲᱦᱟᱣ ᱥᱟᱱᱟᱢ ᱮ", "uni ar parhaw sanam e"],
    ["She doesn't want tea", "ᱩᱱᱤ ᱪᱟᱹ ᱵᱟᱝ ᱥᱟᱱᱟᱢ ᱮ", "uni cha bang sanam e"],
    ["Teacher wants silence", "ᱯᱟᱲᱦᱟᱣᱮᱫ ᱛᱤᱥᱤᱧ ᱥᱟᱱᱟᱢ ᱮ", "parhawed tising sanam e"],
    ["They want to celebrate", "ᱩᱱᱠᱩ ᱢᱟᱱᱟᱣ ᱥᱟᱱᱟᱢ ᱠᱚ", "unku manaw sanam ko"],
    ["He wants to go home", "ᱩᱱᱤ ᱚᱲᱟᱜ ᱥᱮᱱ ᱥᱟᱱᱟᱢ ᱮ", "uni orag sen sanam e"],
    ["She wants to write", "ᱩᱱᱤ ᱚᱞ ᱥᱟᱱᱟᱢ ᱮ", "uni ol sanam e"]
]

LESSONS[567] = [
    ["I was supposed to go", "ᱤᱧ ᱥᱮᱱ ᱞᱟᱜᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj sen lagid taheny a"],
    ["He was supposed to come", "ᱩᱱᱤ ᱦᱤᱡᱩᱜ ᱞᱟᱜᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni hijug lagid taheny e"],
    ["She was supposed to cook", "ᱩᱱᱤ ᱨᱟᱸᱰᱷᱟ ᱞᱟᱜᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni randha lagid taheny e"],
    ["We were supposed to study", "ᱟᱞᱮ ᱯᱟᱲᱦᱟᱣ ᱞᱟᱜᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱟᱞᱮ", "ale parhaw lagid taheny ale"],
    ["They were supposed to help", "ᱩᱱᱠᱩ ᱥᱟᱹᱜᱟᱹᱭ ᱞᱟᱜᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "unku sagay lagid taheny ko"],
    ["You are supposed to be there", "ᱟᱢ ᱚᱱᱫᱮ ᱛᱟᱦᱮᱸᱱ ᱞᱟᱜᱤᱫ ᱟᱢ", "am onde taheny lagid am"],
    ["He is supposed to finish today", "ᱩᱱᱤ ᱟᱡ ᱛᱮᱭᱟᱨ ᱞᱟᱜᱤᱫ ᱮ", "uni aj teyar lagid e"],
    ["I was supposed to call", "ᱤᱧ ᱠᱩᱞ ᱞᱟᱜᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj kul lagid taheny a"],
    ["She was supposed to bring food", "ᱩᱱᱤ ᱡᱚᱢ ᱟᱹᱜᱩ ᱞᱟᱜᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni jom agu lagid taheny e"],
    ["We are supposed to meet", "ᱟᱞᱮ ᱧᱮᱞᱚᱜ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "ale nyelog lagid ale"],
    ["He was supposed to pay", "ᱩᱱᱤ ᱴᱟᱠᱟ ᱮᱢ ᱞᱟᱜᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni taka em lagid taheny e"],
    ["I am supposed to go early", "ᱤᱧ ᱟᱜᱮ ᱥᱮᱱ ᱞᱟᱜᱤᱫ ᱟ", "inj age sen lagid a"],
    ["She is supposed to teach", "ᱩᱱᱤ ᱯᱟᱲᱦᱟᱣ ᱞᱟᱜᱤᱫ ᱮ", "uni parhaw lagid e"],
    ["They were supposed to celebrate", "ᱩᱱᱠᱩ ᱢᱟᱱᱟᱣ ᱞᱟᱜᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "unku manaw lagid taheny ko"],
    ["I was supposed to write a letter", "ᱤᱧ ᱪᱤᱴᱷᱤ ᱚᱞ ᱞᱟᱜᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj chithi ol lagid taheny a"],
    ["He was supposed to return today", "ᱩᱱᱤ ᱟᱡ ᱨᱩᱣᱟᱹᱲ ᱞᱟᱜᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni aj ruwar lagid taheny e"],
    ["We are supposed to sing", "ᱟᱞᱮ ᱥᱮᱨᱮᱧ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "ale sereny lagid ale"],
    ["She was supposed to buy clothes", "ᱩᱱᱤ ᱠᱟᱹᱯᱲᱟ ᱠᱤᱱ ᱞᱟᱜᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni kapra kin lagid taheny e"]
]

LESSONS[568] = [
    ["I like to eat fish", "ᱤᱧ ᱢᱟᱹᱪᱷᱟ ᱡᱚᱢ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "inj machha jom raska a"],
    ["He likes to play football", "ᱩᱱᱤ ᱯᱷᱩᱴᱵᱚᱞ ᱮᱱᱮᱡ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "uni phutbol enej raska e"],
    ["She likes to sing songs", "ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "uni sereny raska e"],
    ["I like to read books", "ᱤᱧ ᱯᱩᱛᱷᱤ ᱯᱟᱲᱦᱟᱣ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "inj puthi parhaw raska a"],
    ["They like to dance", "ᱩᱱᱠᱩ ᱮᱱᱮᱡ ᱨᱟᱹᱥᱠᱟᱹ ᱠᱚ", "unku enej raska ko"],
    ["She likes to walk in the forest", "ᱩᱱᱤ ᱵᱤᱨ ᱨᱮ ᱥᱟᱞᱟᱜ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "uni bir re salag raska e"],
    ["He likes to study", "ᱩᱱᱤ ᱯᱟᱲᱦᱟᱣ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "uni parhaw raska e"],
    ["I like to help others", "ᱤᱧ ᱮᱴᱟᱜ ᱦᱚᱲ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "inj etag hor ke sagay raska a"],
    ["Children like to play games", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱮᱱᱮᱡ ᱨᱟᱹᱥᱠᱟᱹ ᱠᱚ", "gidra ko enej raska ko"],
    ["She likes to cook sweets", "ᱩᱱᱤ ᱡᱤᱞᱤᱯᱤ ᱨᱟᱸᱰᱷᱟ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "uni jilipi randha raska e"],
    ["He likes to travel", "ᱩᱱᱤ ᱵᱮᱲᱟ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "uni bera raska e"],
    ["I like to watch movies", "ᱤᱧ ᱮᱱᱮᱡ ᱧᱮᱞ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "inj enej nyel raska a"],
    ["She likes to write poems", "ᱩᱱᱤ ᱠᱟᱹᱵᱤᱛᱟ ᱚᱞ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "uni kabita ol raska e"],
    ["We like to celebrate together", "ᱟᱞᱮ ᱥᱟᱶᱛᱮ ᱢᱟᱱᱟᱣ ᱨᱟᱹᱥᱠᱟᱹ ᱟᱞᱮ", "ale sawte manaw raska ale"],
    ["He likes to listen to music", "ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱟᱹᱭᱠᱟᱹᱣ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "uni sereny aykaw raska e"],
    ["I don't like to fight", "ᱤᱧ ᱞᱟᱲᱟᱭ ᱵᱟᱝ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "inj laray bang raska a"],
    ["She likes to teach children", "ᱩᱱᱤ ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱠᱮ ᱯᱟᱲᱦᱟᱣ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "uni gidra ko ke parhaw raska e"],
    ["They like to swim in the river", "ᱩᱱᱠᱩ ᱜᱟᱰᱟ ᱨᱮ ᱫᱟᱹᱲ ᱨᱟᱹᱥᱠᱟᱹ ᱠᱚ", "unku gada re dar raska ko"]
]

LESSONS[569] = [
    ["I told him (verb uses 'ke')", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱨᱚᱲ ᱮᱱᱟ", "inj uni ke ror ena"],
    ["He gave me (verb uses 'ke')", "ᱩᱱᱤ ᱤᱧ ᱠᱮ ᱮᱢ ᱮᱱᱟ", "uni inj ke em ena"],
    ["She showed them", "ᱩᱱᱤ ᱩᱱᱠᱩ ᱠᱮ ᱫᱮᱠᱷᱟᱣ ᱮᱱᱟ", "uni unku ke dekhaw ena"],
    ["I asked him", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱠᱩᱞᱤ ᱮᱱᱟ", "inj uni ke kuli ena"],
    ["She taught me", "ᱩᱱᱤ ᱤᱧ ᱠᱮ ᱯᱟᱲᱦᱟᱣ ᱮᱱᱟ", "uni inj ke parhaw ena"],
    ["He called her", "ᱩᱱᱤ ᱩᱱᱤ ᱠᱮ ᱠᱩᱞ ᱮᱱᱟ", "uni uni ke kul ena"],
    ["I will tell you", "ᱤᱧ ᱟᱢ ᱠᱮ ᱨᱚᱲ ᱟ", "inj am ke ror a"],
    ["She sent him a letter", "ᱩᱱᱤ ᱩᱱᱤ ᱠᱮ ᱪᱤᱴᱷᱤ ᱯᱟᱴᱷᱟᱣ ᱮᱱᱟ", "uni uni ke chithi pathaw ena"],
    ["Mother feeds the child", "ᱟᱭᱚ ᱜᱤᱫᱽᱨᱟᱹ ᱠᱮ ᱡᱚᱢ ᱮᱢ ᱟᱫ ᱮ", "ayo gidra ke jom em ad e"],
    ["He brought me food", "ᱩᱱᱤ ᱤᱧ ᱠᱮ ᱡᱚᱢ ᱟᱹᱜᱩ ᱮᱱᱟ", "uni inj ke jom agu ena"],
    ["She will help them", "ᱩᱱᱤ ᱩᱱᱠᱩ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱮ", "uni unku ke sagay e"],
    ["I will give you the book", "ᱤᱧ ᱟᱢ ᱠᱮ ᱯᱩᱛᱷᱤ ᱮᱢ ᱟ", "inj am ke puthi em a"],
    ["He invited us", "ᱩᱱᱤ ᱟᱞᱮ ᱠᱮ ᱠᱩᱞ ᱮᱱᱟ", "uni ale ke kul ena"],
    ["She thanked me", "ᱩᱱᱤ ᱤᱧ ᱠᱮ ᱥᱮᱨᱢᱟ ᱮᱱᱟ", "uni inj ke serma ena"],
    ["Father told us a story", "ᱟᱯᱟ ᱟᱞᱮ ᱠᱮ ᱠᱟᱹᱦᱱᱤ ᱨᱚᱲ ᱮᱱᱟ", "apa ale ke kahni ror ena"],
    ["I sold it to him", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱵᱮᱪᱟᱣ ᱮᱱᱟ", "inj uni ke becaw ena"],
    ["She will bring me water", "ᱩᱱᱤ ᱤᱧ ᱠᱮ ᱫᱟᱜ ᱟᱹᱜᱩ ᱮ", "uni inj ke dag agu e"],
    ["He lent me money", "ᱩᱱᱤ ᱤᱧ ᱠᱮ ᱴᱟᱠᱟ ᱮᱢ ᱮᱱᱟ", "uni inj ke taka em ena"]
]

LESSONS[570] = [
    ["I'm going (short form)", "ᱤᱧ ᱥᱮᱱ ᱟᱭᱟ → ᱥᱮᱱ'ᱭᱟ", "inj sen aya → sen'ya"],
    ["Are you coming?", "ᱟᱢ ᱦᱤᱡᱩᱜ ᱟᱢ? → ᱦᱤᱡᱩᱜ'ᱢ?", "am hijug am? → hijug'm?"],
    ["I don't know", "ᱤᱧ ᱵᱟᱝ ᱵᱟᱰᱟᱭ ᱟ → ᱵᱟᱝ ᱵᱟᱰᱟᱭ", "inj bang baday a → bang baday"],
    ["It's fine", "ᱵᱷᱟᱞᱮ ᱢᱮᱱᱟᱜ ᱟ → ᱵᱷᱟᱞᱮ'ᱜ ᱟ", "bhale menag a → bhale'g a"],
    ["What happened?", "ᱪᱮᱫ ᱦᱩᱭ ᱮᱱᱟ → ᱪᱮᱫ ᱦᱩᱭ'ᱱᱟ", "ced huy ena → ced huy'na"],
    ["Where are you going?", "ᱟᱢ ᱚᱠᱟ ᱥᱮᱱ ᱟᱢ? → ᱚᱠᱟ ᱥᱮᱱ'ᱢ?", "am oka sen am? → oka sen'm?"],
    ["Give me", "ᱤᱧ ᱠᱮ ᱮᱢ ᱢᱮ → ᱮᱢ'ᱢᱮ", "inj ke em me → em'me"],
    ["Did you eat?", "ᱟᱢ ᱡᱚᱢ ᱮᱱᱟ? → ᱡᱚᱢ'ᱱᱟ?", "am jom ena? → jom'na?"],
    ["Come here", "ᱱᱮᱛᱟᱨ ᱦᱤᱡᱩᱜ ᱢᱮ → ᱱᱮᱛᱟᱨ ᱦᱤᱡᱩᱜ'ᱢᱮ", "netar hijug me → netar hijug'me"],
    ["I'll come", "ᱤᱧ ᱦᱤᱡᱩᱜ ᱟ → ᱦᱤᱡᱩᱜ'ᱟ", "inj hijug a → hijug'a"],
    ["Let's go", "ᱟᱞᱮ ᱥᱮᱱ ᱟᱞᱮ → ᱥᱮᱱ'ᱞᱮ", "ale sen ale → sen'le"],
    ["Is it?", "ᱠᱟᱱᱟ? → 'ᱱᱟ?", "kana? → 'na?"],
    ["No, it's not", "ᱵᱟᱝ, ᱵᱟᱝ ᱠᱟᱱᱟ → ᱵᱟᱝ'ᱱᱟ", "bang, bang kana → bang'na"],
    ["What do you want?", "ᱟᱢ ᱪᱮᱫ ᱥᱟᱱᱟᱢ ᱟᱢ? → ᱪᱮᱫ ᱥᱟᱱᱟᱢ'ᱢ?", "am ced sanam am? → ced sanam'm?"],
    ["I didn't go", "ᱤᱧ ᱵᱟᱝ ᱥᱮᱱ ᱮᱱᱟ → ᱵᱟᱝ ᱥᱮᱱ'ᱱᱟ", "inj bang sen ena → bang sen'na"],
    ["He has come", "ᱩᱱᱤ ᱦᱤᱡᱩᱜ ᱮᱱᱟ → ᱦᱤᱡᱩᱜ'ᱱᱟ ᱮ", "uni hijug ena → hijug'na e"],
    ["Sit down", "ᱫᱩᱲᱩᱵ ᱢᱮ → ᱫᱩᱲᱩᱵ'ᱢᱮ", "durub me → durub'me"],
    ["You ate, right?", "ᱟᱢ ᱡᱚᱢ ᱮᱱᱟ, ᱦᱟᱛᱤᱭᱟᱸ? → ᱡᱚᱢ'ᱱᱟ?", "am jom ena, hatiyaan? → jom'na?"]
]

LESSONS[571] = [
    ["Happy Baha (Spring Festival)", "ᱵᱟᱦᱟ ᱯᱚᱨᱚᱵ ᱨᱟᱹᱥᱠᱟᱹ ᱢᱟ", "baha porob raska ma"],
    ["Happy Sohrai (Harvest Festival)", "ᱥᱚᱦᱨᱟᱭ ᱯᱚᱨᱚᱵ ᱨᱟᱹᱥᱠᱟᱹ ᱢᱟ", "sohray porob raska ma"],
    ["Happy Dasain / Diwali", "ᱫᱤᱯᱟᱹᱵᱷᱤ ᱯᱚᱨᱚᱵ ᱨᱟᱹᱥᱠᱟᱹ ᱢᱟ", "dipabhi porob raska ma"],
    ["Happy New Year", "ᱱᱟᱣᱟ ᱥᱮᱨᱢᱟ ᱨᱟᱹᱥᱠᱟᱹ ᱢᱟ", "nawa serma raska ma"],
    ["Johar! (Santali greeting)", "ᱡᱚᱦᱟᱨ!", "johar!"],
    ["Blessings to you", "ᱟᱢ ᱠᱮ ᱫᱩᱣᱟᱹ ᱢᱟ", "am ke duwa ma"],
    ["May you be happy", "ᱟᱢ ᱨᱟᱹᱥᱠᱟᱹ ᱨᱮ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "am raska re taheny me"],
    ["Long live our language", "ᱟᱞᱮᱭᱟᱜ ᱯᱟᱹᱨᱥᱤ ᱡᱟᱦᱟᱸᱱᱟᱜ ᱛᱟᱦᱮᱸᱱ ᱢᱟ", "aleyag parsi jahanag taheny ma"],
    ["Victory to Santali!", "ᱡᱚᱦᱟᱨ ᱥᱟᱱᱛᱟᱲ!", "johar santar!"],
    ["Long live the motherland", "ᱫᱤᱥᱚᱢ ᱡᱟᱦᱟᱸᱱᱟᱜ ᱛᱟᱦᱮᱸᱱ ᱢᱟ", "disom jahanag taheny ma"],
    ["May God bless you", "ᱢᱟᱨᱟᱝ ᱵᱩᱨᱩ ᱟᱢ ᱠᱮ ᱫᱩᱣᱟᱹ ᱢᱟ", "marang buru am ke duwa ma"],
    ["Welcome to our village", "ᱟᱞᱮᱭᱟᱜ ᱟᱹᱛᱩ ᱨᱮ ᱡᱚᱦᱟᱨ ᱢᱟ", "aleyag atu re johar ma"],
    ["May you have a long life", "ᱟᱢ ᱡᱟᱱᱟᱝ ᱡᱤᱣᱤ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "am janang jiwi taheny me"],
    ["Hul Johar! (Revolutionary greeting)", "ᱦᱩᱞ ᱡᱚᱦᱟᱨ!", "hul johar!"],
    ["Happy birthday", "ᱡᱟᱱᱟᱢ ᱫᱤᱱ ᱨᱟᱹᱥᱠᱟᱹ ᱢᱟ", "janam din raska ma"],
    ["Happy Independence Day", "ᱥᱚᱛᱟᱱᱛᱨᱟ ᱫᱤᱱ ᱨᱟᱹᱥᱠᱟᱹ ᱢᱟ", "sotantra din raska ma"],
    ["Happy Republic Day", "ᱜᱚᱱᱛᱚᱱᱛᱨᱟ ᱫᱤᱱ ᱨᱟᱹᱥᱠᱟᱹ ᱢᱟ", "gontontantra din raska ma"],
    ["May peace prevail", "ᱥᱟᱱᱛᱤ ᱛᱟᱦᱮᱸᱱ ᱢᱟ", "santi taheny ma"]
]

LESSONS[572] = [
    ["Get up and go", "ᱛᱤᱧᱜᱩ ᱟᱨ ᱥᱮᱱ ᱢᱮ", "tingu ar sen me"],
    ["Eat and drink", "ᱡᱚᱢ ᱟᱨ ᱧᱩ ᱢᱮ", "jom ar nyu me"],
    ["Come and sit", "ᱦᱤᱡᱩᱜ ᱟᱨ ᱫᱩᱲᱩᱵ ᱢᱮ", "hijug ar durub me"],
    ["Read and write", "ᱯᱟᱲᱦᱟᱣ ᱟᱨ ᱚᱞ ᱢᱮ", "parhaw ar ol me"],
    ["Listen and understand", "ᱟᱹᱭᱠᱟᱹᱣ ᱟᱨ ᱵᱩᱡᱷᱟᱹᱣ ᱢᱮ", "aykaw ar bujhaw me"],
    ["Run and catch", "ᱫᱟᱹᱲ ᱟᱨ ᱟᱹᱜᱩ ᱢᱮ", "dar ar agu me"],
    ["Think and decide", "ᱢᱚᱱᱮ ᱟᱨ ᱛᱮᱭᱟᱨ ᱢᱮ", "mone ar teyar me"],
    ["Wash and cook", "ᱡᱩ ᱟᱨ ᱨᱟᱸᱰᱷᱟ ᱢᱮ", "ju ar randha me"],
    ["Take and give", "ᱤᱫᱤ ᱟᱨ ᱮᱢ ᱢᱮ", "idi ar em me"],
    ["Speak and explain", "ᱨᱚᱲ ᱟᱨ ᱵᱩᱡᱷᱟᱹᱣ ᱢᱮ", "ror ar bujhaw me"],
    ["Wake up and study", "ᱪᱟᱹᱞᱩ ᱟᱨ ᱯᱟᱲᱦᱟᱣ ᱢᱮ", "chalu ar parhaw me"],
    ["Go and see", "ᱥᱮᱱ ᱟᱨ ᱧᱮᱞ ᱢᱮ", "sen ar nyel me"],
    ["Buy and bring", "ᱠᱤᱱ ᱟᱨ ᱟᱹᱜᱩ ᱢᱮ", "kin ar agu me"],
    ["Sing and dance", "ᱥᱮᱨᱮᱧ ᱟᱨ ᱮᱱᱮᱡ ᱢᱮ", "sereny ar enej me"],
    ["Ask and learn", "ᱠᱩᱞᱤ ᱟᱨ ᱥᱮᱪᱮᱫ ᱢᱮ", "kuli ar seced me"],
    ["Cut and eat", "ᱛᱚᱞ ᱟᱨ ᱡᱚᱢ ᱢᱮ", "tol ar jom me"],
    ["Walk and explore", "ᱥᱟᱞᱟᱜ ᱟᱨ ᱧᱮᱞ ᱢᱮ", "salag ar nyel me"],
    ["Plant and grow", "ᱛᱟᱞᱟ ᱟᱨ ᱵᱚᱞᱚ ᱢᱮ", "tala ar bolo me"]
]

LESSONS[573] = [
    ["Hey brother!", "ᱮ ᱦᱟᱯᱲᱟᱢ!", "e hapram!"],
    ["Hey sister!", "ᱮ ᱢᱤᱥᱤ!", "e misi!"],
    ["Oh father!", "ᱮ ᱟᱯᱟ!", "e apa!"],
    ["Oh mother!", "ᱮ ᱟᱭᱚ!", "e ayo!"],
    ["Hey friend!", "ᱮ ᱥᱟᱶᱛᱟ!", "e sawta!"],
    ["Hey child!", "ᱮ ᱜᱤᱫᱽᱨᱟᱹ!", "e gidra!"],
    ["Dear teacher", "ᱮ ᱯᱟᱲᱦᱟᱣᱮᱫ!", "e parhawed!"],
    ["Hey boy!", "ᱮ ᱠᱚᱲᱟ!", "e kora!"],
    ["Hey girl!", "ᱮ ᱠᱩᱲᱤ!", "e kuri!"],
    ["Oh grandfather!", "ᱮ ᱵᱟᱵᱟ!", "e baba!"],
    ["Oh grandmother!", "ᱮ ᱟᱡᱤ!", "e aji!"],
    ["Hey elder brother!", "ᱮ ᱵᱚᱭᱦᱟ!", "e boyha!"],
    ["Hey elder sister!", "ᱮ ᱵᱟᱭ!", "e bay!"],
    ["Oh village headman!", "ᱮ ᱢᱟᱹᱧᱡᱷᱤ!", "e manjhi!"],
    ["Hey uncle!", "ᱮ ᱠᱟᱠᱟ!", "e kaka!"],
    ["Hey aunty!", "ᱮ ᱠᱟᱠᱤ!", "e kaki!"],
    ["Oh dear!", "ᱮ ᱫᱩᱞᱟᱹᱲ!", "e dular!"],
    ["Everyone!", "ᱮ ᱡᱚᱛᱚ ᱦᱚᱲ!", "e joto hor!"]
]

LESSONS[574] = [
    ["Wow!", "ᱵᱟᱦ!", "bah!"],
    ["Oh no!", "ᱟᱦᱟ!", "aha!"],
    ["Alas!", "ᱦᱟᱭ!", "hay!"],
    ["Wonderful!", "ᱵᱟᱦ, ᱥᱚᱢᱵᱷᱟᱨ!", "bah, sombhar!"],
    ["How beautiful!", "ᱟᱹᱰᱤ ᱥᱚᱢᱵᱷᱟᱨ!", "adi sombhar!"],
    ["How sad!", "ᱟᱹᱰᱤ ᱫᱩᱠᱷ!", "adi dukh!"],
    ["What a surprise!", "ᱟᱹᱰᱤ ᱵᱤᱥᱢᱟᱭ!", "adi bismay!"],
    ["How nice!", "ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ!", "adi bhale!"],
    ["Thank God!", "ᱢᱟᱨᱟᱝ ᱵᱩᱨᱩ ᱥᱮᱨᱢᱟ!", "marang buru serma!"],
    ["What a pity!", "ᱟᱹᱰᱤ ᱫᱩᱠᱷ ᱢᱟ!", "adi dukh ma!"],
    ["Bravo!", "ᱵᱷᱟᱞᱮ ᱠᱮᱫ'ᱢ!", "bhale ked'm!"],
    ["Oh God!", "ᱮ ᱢᱟᱨᱟᱝ ᱵᱩᱨᱩ!", "e marang buru!"],
    ["What happened!", "ᱪᱮᱫ ᱦᱩᱭ ᱮᱱᱟ!", "ced huy ena!"],
    ["Great job!", "ᱵᱷᱟᱞᱮ ᱠᱟᱹᱢᱤ!", "bhale kami!"],
    ["How tasty!", "ᱟᱹᱰᱤ ᱫᱷᱟᱹᱨᱤ!", "adi dhari!"],
    ["Unbelievable!", "ᱵᱷᱟᱨᱥᱟ ᱵᱟᱝ ᱠᱟᱱᱟ!", "bharsa bang kana!"],
    ["So hot!", "ᱟᱹᱰᱤ ᱫᱩᱨᱩᱵ!", "adi durub!"],
    ["How big!", "ᱟᱹᱰᱤ ᱢᱟᱨᱟᱝ!", "adi marang!"]
]

LESSONS[575] = [
    ["May I come in?", "ᱤᱧ ᱵᱷᱤᱛᱤᱨ ᱦᱤᱡᱩᱜ ᱫᱟᱲᱮᱭᱟᱜ ᱢᱟ?", "inj bhitir hijug dareyag ma?"],
    ["Can you help me?", "ᱟᱢ ᱤᱧ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am inj ke sagay dareyam ma?"],
    ["May I sit here?", "ᱤᱧ ᱱᱮᱛᱟᱨ ᱫᱩᱲᱩᱵ ᱫᱟᱲᱮᱭᱟᱜ ᱢᱟ?", "inj netar durub dareyag ma?"],
    ["Can you give me water?", "ᱟᱢ ᱤᱧ ᱠᱮ ᱫᱟᱜ ᱮᱢ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am inj ke dag em dareyam ma?"],
    ["May I speak?", "ᱤᱧ ᱨᱚᱲ ᱫᱟᱲᱮᱭᱟᱜ ᱢᱟ?", "inj ror dareyag ma?"],
    ["Can you show me the way?", "ᱟᱢ ᱤᱧ ᱠᱮ ᱨᱟᱦᱟ ᱫᱮᱠᱷᱟᱣ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am inj ke raha dekhaw dareyam ma?"],
    ["May I borrow your book?", "ᱤᱧ ᱟᱢᱟᱜ ᱯᱩᱛᱷᱤ ᱤᱫᱤ ᱫᱟᱲᱮᱭᱟᱜ ᱢᱟ?", "inj amag puthi idi dareyag ma?"],
    ["Can you wait a moment?", "ᱟᱢ ᱟᱹᱛᱩ ᱦᱮᱞᱟ ᱡᱚᱜᱟᱹᱣ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am atu hela jogaw dareyam ma?"],
    ["May I go now?", "ᱤᱧ ᱱᱤᱛ ᱥᱮᱱ ᱫᱟᱲᱮᱭᱟᱜ ᱢᱟ?", "inj nit sen dareyag ma?"],
    ["Can you repeat that?", "ᱟᱢ ᱟᱨ ᱢᱤᱫ ᱨᱚᱲ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am ar mid ror dareyam ma?"],
    ["May I use this?", "ᱤᱧ ᱱᱚᱣᱟ ᱵᱮᱵᱷᱟᱨ ᱫᱟᱲᱮᱭᱟᱜ ᱢᱟ?", "inj nowa bebhar dareyag ma?"],
    ["Can you come tomorrow?", "ᱟᱢ ᱜᱟᱯᱟ ᱦᱤᱡᱩᱜ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am gapa hijug dareyam ma?"],
    ["May I ask a question?", "ᱤᱧ ᱢᱤᱫ ᱠᱩᱞᱤ ᱠᱩᱞᱤ ᱫᱟᱲᱮᱭᱟᱜ ᱢᱟ?", "inj mid kuli kuli dareyag ma?"],
    ["Can you speak Santali?", "ᱟᱢ ᱥᱟᱱᱛᱟᱲᱤ ᱨᱚᱲ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am santari ror dareyam ma?"],
    ["May I close the window?", "ᱤᱧ ᱡᱷᱚᱨᱠᱟ ᱫᱟᱸᱰ ᱫᱟᱲᱮᱭᱟᱜ ᱢᱟ?", "inj jhorka dand dareyag ma?"],
    ["Can you teach me?", "ᱟᱢ ᱤᱧ ᱠᱮ ᱯᱟᱲᱦᱟᱣ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am inj ke parhaw dareyam ma?"],
    ["May I take your leave?", "ᱤᱧ ᱥᱮᱱ ᱫᱟᱲᱮᱭᱟᱜ ᱢᱟ?", "inj sen dareyag ma?"],
    ["Can you call him?", "ᱟᱢ ᱩᱱᱤ ᱠᱮ ᱠᱩᱞ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am uni ke kul dareyam ma?"]
]

LESSONS[576] = [
    ["It may rain today", "ᱟᱡ ᱫᱟᱜ ᱫᱟᱹᱲ ᱟᱠᱟᱫ ᱟ", "aj dag dar akad a"],
    ["He may come tomorrow", "ᱩᱱᱤ ᱜᱟᱯᱟ ᱦᱤᱡᱩᱜ ᱟᱠᱟᱫ ᱮ", "uni gapa hijug akad e"],
    ["She might be at home", "ᱩᱱᱤ ᱚᱲᱟᱜ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟᱠᱟᱫ ᱮ", "uni orag re menag akad e"],
    ["I might go to the market", "ᱤᱧ ᱵᱟᱡᱟᱨ ᱥᱮᱱ ᱟᱠᱟᱫ ᱟ", "inj bajar sen akad a"],
    ["They may not come", "ᱩᱱᱠᱩ ᱵᱟᱝ ᱦᱤᱡᱩᱜ ᱟᱠᱟᱫ ᱠᱚ", "unku bang hijug akad ko"],
    ["It might be cold today", "ᱟᱡ ᱫᱷᱤᱨᱤ ᱦᱩᱭ ᱟᱠᱟᱫ ᱟ", "aj dhiri huy akad a"],
    ["She may be sleeping", "ᱩᱱᱤ ᱧᱤᱫ ᱢᱮᱱᱟᱜ ᱟᱠᱟᱫ ᱮ", "uni nyid menag akad e"],
    ["He might help us", "ᱩᱱᱤ ᱟᱞᱮ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱟᱠᱟᱫ ᱮ", "uni ale ke sagay akad e"],
    ["The bus may be late", "ᱵᱟᱥ ᱞᱮᱴ ᱦᱩᱭ ᱟᱠᱟᱫ ᱟ", "bas let huy akad a"],
    ["I may not understand", "ᱤᱧ ᱵᱟᱝ ᱵᱩᱡᱷᱟᱹᱣ ᱟᱠᱟᱫ ᱟ", "inj bang bujhaw akad a"],
    ["Father may return late", "ᱟᱯᱟ ᱞᱮᱴ ᱨᱩᱣᱟᱹᱲ ᱟᱠᱟᱫ ᱮ", "apa let ruwar akad e"],
    ["She might know the answer", "ᱩᱱᱤ ᱡᱟᱣᱟᱵ ᱵᱟᱰᱟᱭ ᱟᱠᱟᱫ ᱮ", "uni jawab baday akad e"],
    ["We may go to the festival", "ᱟᱞᱮ ᱯᱚᱨᱚᱵ ᱥᱮᱱ ᱟᱠᱟᱫ ᱟᱞᱮ", "ale porob sen akad ale"],
    ["It might happen", "ᱦᱩᱭ ᱟᱠᱟᱫ ᱟ", "huy akad a"],
    ["He may call you", "ᱩᱱᱤ ᱟᱢ ᱠᱮ ᱠᱩᱞ ᱟᱠᱟᱫ ᱮ", "uni am ke kul akad e"],
    ["She might not come today", "ᱩᱱᱤ ᱟᱡ ᱵᱟᱝ ᱦᱤᱡᱩᱜ ᱟᱠᱟᱫ ᱮ", "uni aj bang hijug akad e"],
    ["We might be late", "ᱟᱞᱮ ᱞᱮᱴ ᱦᱩᱭ ᱟᱠᱟᱫ ᱟᱞᱮ", "ale let huy akad ale"],
    ["I may forget", "ᱤᱧ ᱵᱟᱝ ᱩᱢ ᱟᱠᱟᱫ ᱟ", "inj bang um akad a"]
]

LESSONS[577] = [
    ["Written (from write)", "ᱚᱞ ᱟᱠᱟᱫ", "ol akad"],
    ["Cooked (from cook)", "ᱨᱟᱸᱰᱷᱟ ᱟᱠᱟᱫ", "randha akad"],
    ["Broken (from break)", "ᱵᱷᱟᱸᱜᱟ ᱟᱠᱟᱫ", "bhanga akad"],
    ["Read (from read)", "ᱯᱟᱲᱦᱟᱣ ᱟᱠᱟᱫ", "parhaw akad"],
    ["Washed (from wash)", "ᱡᱩ ᱟᱠᱟᱫ", "ju akad"],
    ["A cooked meal", "ᱨᱟᱸᱰᱷᱟ ᱡᱚᱢ", "randha jom"],
    ["A written letter", "ᱚᱞ ᱪᱤᱴᱷᱤ", "ol chithi"],
    ["A broken pot", "ᱵᱷᱟᱸᱜᱟ ᱜᱟᱜᱲᱤ", "bhanga gagri"],
    ["A finished work", "ᱛᱮᱭᱟᱨ ᱠᱟᱹᱢᱤ", "teyar kami"],
    ["A planted tree", "ᱛᱟᱞᱟ ᱫᱟᱨᱮ", "tala dare"],
    ["Dried fish", "ᱥᱩᱠᱩ ᱢᱟᱹᱪᱷᱟ", "suku machha"],
    ["A lost person", "ᱵᱟᱲᱟᱭ ᱦᱚᱲ", "baray hor"],
    ["A closed door", "ᱫᱟᱸᱰ ᱫᱩᱣᱟᱹᱨ", "dand duwar"],
    ["An opened book", "ᱡᱷᱤᱡ ᱯᱩᱛᱷᱤ", "jhij puthi"],
    ["Ripe fruit", "ᱯᱚᱢ ᱥᱤᱨᱢᱟ", "pom sirma"],
    ["A tired person", "ᱛᱷᱟᱠᱟᱣ ᱦᱚᱲ", "thakaw hor"],
    ["A sleeping child", "ᱧᱤᱫ ᱜᱤᱫᱽᱨᱟᱹ", "nyid gidra"],
    ["Fallen leaves", "ᱩᱭᱩᱜ ᱥᱟᱠᱟᱢ", "uyug sakam"]
]

LESSONS[578] = [
    ["Upper / above", "ᱪᱮᱛᱟᱱ", "cetan"],
    ["Lower / below", "ᱞᱟᱛᱟᱨ", "latar"],
    ["Inner / inside", "ᱵᱷᱤᱛᱤᱨ", "bhitir"],
    ["Outer / outside", "ᱵᱟᱦᱨᱮ", "bahre"],
    ["Front", "ᱥᱟᱹᱢᱟᱹᱝ", "samang"],
    ["Back / behind", "ᱯᱤᱪᱷᱟ", "pichha"],
    ["Side / beside", "ᱜᱚᱲᱟ", "gora"],
    ["Near", "ᱱᱮᱰᱟ", "neda"],
    ["Far", "ᱫᱩᱨ", "dur"],
    ["The upper room", "ᱪᱮᱛᱟᱱ ᱠᱚᱴᱷᱟ", "cetan kotha"],
    ["The lower field", "ᱞᱟᱛᱟᱨ ᱜᱟᱰᱟ", "latar gada"],
    ["The inner room", "ᱵᱷᱤᱛᱤᱨ ᱠᱚᱴᱷᱟ", "bhitir kotha"],
    ["The outside world", "ᱵᱟᱦᱨᱮ ᱫᱤᱥᱚᱢ", "bahre disom"],
    ["The front door", "ᱥᱟᱹᱢᱟᱹᱝ ᱫᱩᱣᱟᱹᱨ", "samang duwar"],
    ["The back garden", "ᱯᱤᱪᱷᱟ ᱵᱟᱜᱤᱪᱟ", "pichha bagicha"],
    ["The nearby village", "ᱱᱮᱰᱟ ᱟᱹᱛᱩ", "neda atu"],
    ["The faraway hills", "ᱫᱩᱨ ᱵᱩᱨᱩ", "dur buru"],
    ["The side path", "ᱜᱚᱲᱟ ᱨᱟᱦᱟ", "gora raha"]
]

for ch in d:
    if ch['id'] in LESSONS:
        ch['blocks'] = [{"type": "table", "columns": ["English", "Santali (Ol Chiki)", "Transliteration"], "rows": LESSONS[ch['id']]}]

open('data_santali.json', 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('Section 3b (561-578) populated')
