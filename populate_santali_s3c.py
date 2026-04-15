import json

d = json.load(open('data_santali.json', 'r', encoding='utf-8'))

LESSONS = {}

LESSONS[579] = [
    ["May you be happy", "ᱟᱢ ᱨᱟᱹᱥᱠᱟᱹ ᱨᱮ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "am raska re taheny me"],
    ["May he succeed", "ᱩᱱᱤ ᱡᱤᱛ ᱮᱢ ᱢᱟ", "uni jit em ma"],
    ["May she get well soon", "ᱩᱱᱤ ᱡᱟᱞᱫᱤ ᱵᱷᱟᱞᱮ ᱦᱩᱭ ᱮᱢ ᱢᱟ", "uni jaldi bhale huy em ma"],
    ["May it rain", "ᱫᱟᱜ ᱫᱟᱹᱲ ᱮᱢ ᱢᱟ", "dag dar em ma"],
    ["May peace prevail", "ᱥᱟᱱᱛᱤ ᱛᱟᱦᱮᱸᱱ ᱮᱢ ᱢᱟ", "santi taheny em ma"],
    ["May God bless you", "ᱢᱟᱨᱟᱝ ᱵᱩᱨᱩ ᱟᱢ ᱠᱮ ᱫᱩᱣᱟᱹ ᱮᱢ ᱢᱟ", "marang buru am ke duwa em ma"],
    ["May they come safe", "ᱩᱱᱠᱩ ᱵᱷᱟᱞᱮ ᱦᱤᱡᱩᱜ ᱮᱢ ᱢᱟ", "unku bhale hijug em ma"],
    ["May you live long", "ᱟᱢ ᱡᱟᱱᱟᱝ ᱡᱤᱣᱤ ᱛᱟᱦᱮᱸᱱ ᱮᱢ ᱢᱟ", "am janang jiwi taheny em ma"],
    ["May the festival be good", "ᱯᱚᱨᱚᱵ ᱵᱷᱟᱞᱮ ᱦᱩᱭ ᱮᱢ ᱢᱟ", "porob bhale huy em ma"],
    ["May we meet again", "ᱟᱞᱮ ᱟᱨ ᱢᱤᱫ ᱫᱤᱱ ᱧᱮᱞᱚᱜ ᱮᱢ ᱢᱟ", "ale ar mid din nyelog em ma"],
    ["May children study well", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱵᱷᱟᱞᱮ ᱯᱟᱲᱦᱟᱣ ᱮᱢ ᱢᱟ", "gidra ko bhale parhaw em ma"],
    ["May the crop grow well", "ᱡᱚ ᱵᱷᱟᱞᱮ ᱵᱚᱞᱚ ᱮᱢ ᱢᱟ", "jo bhale bolo em ma"],
    ["May you find your way", "ᱟᱢ ᱟᱢᱟᱜ ᱨᱟᱦᱟ ᱧᱟᱢ ᱮᱢ ᱢᱟ", "am amag raha nyam em ma"],
    ["May he recover quickly", "ᱩᱱᱤ ᱡᱟᱞᱫᱤ ᱵᱷᱟᱞᱮ ᱦᱩᱭ ᱮᱢ ᱢᱟ", "uni jaldi bhale huy em ma"],
    ["May our village prosper", "ᱟᱞᱮᱭᱟᱜ ᱟᱹᱛᱩ ᱵᱷᱟᱞᱮ ᱛᱟᱦᱮᱸᱱ ᱮᱢ ᱢᱟ", "aleyag atu bhale taheny em ma"],
    ["May you do well in exams", "ᱟᱢ ᱯᱚᱨᱤᱠᱷᱟ ᱨᱮ ᱵᱷᱟᱞᱮ ᱠᱮᱫ ᱮᱢ ᱢᱟ", "am porikha re bhale ked em ma"],
    ["May the sun shine", "ᱥᱤᱧ ᱡᱟᱞᱟᱜ ᱮᱢ ᱢᱟ", "sing jalag em ma"],
    ["May all be well", "ᱡᱚᱛᱚ ᱵᱷᱟᱞᱮ ᱦᱩᱭ ᱮᱢ ᱢᱟ", "joto bhale huy em ma"]
]

LESSONS[580] = [
    ["I made him eat", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱡᱚᱢ ᱤᱪᱤ ᱮᱱᱟ", "inj uni ke jom ichi ena"],
    ["She made the child sleep", "ᱩᱱᱤ ᱜᱤᱫᱽᱨᱟᱹ ᱠᱮ ᱧᱤᱫ ᱤᱪᱤ ᱮᱱᱟ", "uni gidra ke nyid ichi ena"],
    ["Father made me study", "ᱟᱯᱟ ᱤᱧ ᱠᱮ ᱯᱟᱲᱦᱟᱣ ᱤᱪᱤ ᱮᱱᱟ", "apa inj ke parhaw ichi ena"],
    ["Mother made him bathe", "ᱟᱭᱚ ᱩᱱᱤ ᱠᱮ ᱡᱩ ᱤᱪᱤ ᱮᱱᱟ", "ayo uni ke ju ichi ena"],
    ["Teacher made students write", "ᱯᱟᱲᱦᱟᱣᱮᱫ ᱪᱟᱴᱟᱨ ᱠᱚ ᱠᱮ ᱚᱞ ᱤᱪᱤ ᱮᱱᱟ", "parhawed chatar ko ke ol ichi ena"],
    ["He made them work", "ᱩᱱᱤ ᱩᱱᱠᱩ ᱠᱮ ᱠᱟᱹᱢᱤ ᱤᱪᱤ ᱮᱱᱟ", "uni unku ke kami ichi ena"],
    ["She made me laugh", "ᱩᱱᱤ ᱤᱧ ᱠᱮ ᱞᱟᱸᱫᱟ ᱤᱪᱤ ᱮᱱᱟ", "uni inj ke landa ichi ena"],
    ["I will make him come", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱦᱤᱡᱩᱜ ᱤᱪᱤ ᱟ", "inj uni ke hijug ichi a"],
    ["She made them sit down", "ᱩᱱᱤ ᱩᱱᱠᱩ ᱠᱮ ᱫᱩᱲᱩᱵ ᱤᱪᱤ ᱮᱱᱟ", "uni unku ke durub ichi ena"],
    ["He made the dog run", "ᱩᱱᱤ ᱥᱮᱛᱟ ᱠᱮ ᱫᱟᱹᱲ ᱤᱪᱤ ᱮᱱᱟ", "uni seta ke dar ichi ena"],
    ["I made them understand", "ᱤᱧ ᱩᱱᱠᱩ ᱠᱮ ᱵᱩᱡᱷᱟᱹᱣ ᱤᱪᱤ ᱮᱱᱟ", "inj unku ke bujhaw ichi ena"],
    ["Father made us go", "ᱟᱯᱟ ᱟᱞᱮ ᱠᱮ ᱥᱮᱱ ᱤᱪᱤ ᱮᱱᱟ", "apa ale ke sen ichi ena"],
    ["She made children sing", "ᱩᱱᱤ ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱠᱮ ᱥᱮᱨᱮᱧ ᱤᱪᱤ ᱮᱱᱟ", "uni gidra ko ke sereny ichi ena"],
    ["I made them dance", "ᱤᱧ ᱩᱱᱠᱩ ᱠᱮ ᱮᱱᱮᱡ ᱤᱪᱤ ᱮᱱᱟ", "inj unku ke enej ichi ena"],
    ["He made her wait", "ᱩᱱᱤ ᱩᱱᱤ ᱠᱮ ᱡᱚᱜᱟᱹᱣ ᱤᱪᱤ ᱮᱱᱟ", "uni uni ke jogaw ichi ena"],
    ["Teacher made us read", "ᱯᱟᱲᱦᱟᱣᱮᱫ ᱟᱞᱮ ᱠᱮ ᱯᱟᱲᱦᱟᱣ ᱤᱪᱤ ᱮᱱᱟ", "parhawed ale ke parhaw ichi ena"],
    ["I will make him read", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱯᱟᱲᱦᱟᱣ ᱤᱪᱤ ᱟ", "inj uni ke parhaw ichi a"],
    ["Mother made us wake up", "ᱟᱭᱚ ᱟᱞᱮ ᱠᱮ ᱪᱟᱹᱞᱩ ᱤᱪᱤ ᱮᱱᱟ", "ayo ale ke chalu ichi ena"]
]

LESSONS[581] = [
    ["Somewhere", "ᱚᱠᱟ ᱫᱮ", "oka de"],
    ["Somehow", "ᱚᱠᱟ ᱞᱮᱠᱟ ᱫᱮ", "oka leka de"],
    ["Sometime", "ᱚᱠᱟ ᱵᱮᱞᱟ ᱫᱮ", "oka bela de"],
    ["Someone", "ᱚᱠᱚᱭ ᱫᱮ", "okoy de"],
    ["Something", "ᱡᱟᱦᱟᱸ ᱫᱮ", "jahang de"],
    ["Anywhere", "ᱡᱟᱦᱟᱸ ᱡᱟᱭᱜᱟ ᱨᱮ", "jahang jayga re"],
    ["Anyhow", "ᱡᱟᱦᱟᱸ ᱞᱮᱠᱟ", "jahang leka"],
    ["Anytime", "ᱡᱟᱦᱟᱸ ᱵᱮᱞᱟ ᱨᱮ", "jahang bela re"],
    ["Anyone", "ᱡᱟᱦᱟᱸ ᱦᱚᱲ", "jahang hor"],
    ["Anything", "ᱡᱟᱦᱟᱸ ᱡᱤᱱᱤᱥ", "jahang jinis"],
    ["Nobody", "ᱡᱟᱦᱟᱸ ᱵᱟᱝ", "jahang bang"],
    ["Nothing", "ᱡᱟᱦᱟᱸ ᱵᱟᱝ", "jahang bang"],
    ["Nowhere", "ᱡᱟᱦᱟᱸ ᱡᱟᱭᱜᱟ ᱵᱟᱝ", "jahang jayga bang"],
    ["Everywhere", "ᱡᱚᱛᱚ ᱡᱟᱭᱜᱟ ᱨᱮ", "joto jayga re"],
    ["Everyone", "ᱡᱚᱛᱚ ᱦᱚᱲ", "joto hor"],
    ["Everything", "ᱡᱚᱛᱚ ᱡᱤᱱᱤᱥ", "joto jinis"],
    ["Always", "ᱡᱟᱦᱟᱸᱱᱟᱜ", "jahanag"],
    ["Never", "ᱡᱟᱦᱟᱸᱱᱟᱜ ᱵᱟᱝ", "jahanag bang"]
]

LESSONS[582] = [
    ["I have a book", "ᱤᱧᱟᱜ ᱯᱩᱛᱷᱤ ᱢᱮᱱᱟᱜ ᱟ", "injag puthi menag a"],
    ["You have money", "ᱟᱢᱟᱜ ᱴᱟᱠᱟ ᱢᱮᱱᱟᱜ ᱟ", "amag taka menag a"],
    ["He has a house", "ᱩᱱᱤᱭᱟᱜ ᱚᱲᱟᱜ ᱢᱮᱱᱟᱜ ᱟ", "uniag orag menag a"],
    ["She has two children", "ᱩᱱᱤᱭᱟᱜ ᱵᱟᱨ ᱜᱤᱫᱽᱨᱟᱹ ᱢᱮᱱᱟᱜ ᱟ", "uniag bar gidra menag a"],
    ["We have a farm", "ᱟᱞᱮᱭᱟᱜ ᱜᱟᱰᱟ ᱢᱮᱱᱟᱜ ᱟ", "aleyag gada menag a"],
    ["They have many trees", "ᱩᱱᱠᱩᱭᱟᱜ ᱟᱹᱰᱤ ᱫᱟᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "unkuag adi dare menag a"],
    ["I don't have money", "ᱤᱧᱟᱜ ᱴᱟᱠᱟ ᱵᱟᱝ ᱢᱮᱱᱟᱜ ᱟ", "injag taka bang menag a"],
    ["He has a brother", "ᱩᱱᱤᱭᱟᱜ ᱦᱟᱯᱲᱟᱢ ᱢᱮᱱᱟᱜ ᱟ", "uniag hapram menag a"],
    ["I have a sister", "ᱤᱧᱟᱜ ᱢᱤᱥᱤ ᱢᱮᱱᱟᱜ ᱟ", "injag misi menag a"],
    ["She has a good voice", "ᱩᱱᱤᱭᱟᱜ ᱵᱷᱟᱞᱮ ᱜᱟᱞᱟ ᱢᱮᱱᱟᱜ ᱟ", "uniag bhale gala menag a"],
    ["Do you have time?", "ᱟᱢᱟᱜ ᱵᱮᱞᱟ ᱢᱮᱱᱟᱜ ᱟ?", "amag bela menag a?"],
    ["He has a vehicle", "ᱩᱱᱤᱭᱟᱜ ᱜᱟᱰᱤ ᱢᱮᱱᱟᱜ ᱟ", "uniag gadi menag a"],
    ["I have friends", "ᱤᱧᱟᱜ ᱥᱟᱶᱛᱟ ᱢᱮᱱᱟᱜ ᱟ", "injag sawta menag a"],
    ["We have a beautiful village", "ᱟᱞᱮᱭᱟᱜ ᱥᱚᱢᱵᱷᱟᱨ ᱟᱹᱛᱩ ᱢᱮᱱᱟᱜ ᱟ", "aleyag sombhar atu menag a"],
    ["She has three brothers", "ᱩᱱᱤᱭᱟᱜ ᱯᱮ ᱦᱟᱯᱲᱟᱢ ᱢᱮᱱᱟᱜ ᱟ", "uniag pe hapram menag a"],
    ["They don't have food", "ᱩᱱᱠᱩᱭᱟᱜ ᱡᱚᱢ ᱵᱟᱝ ᱢᱮᱱᱟᱜ ᱟ", "unkuag jom bang menag a"],
    ["I have a dog", "ᱤᱧᱟᱜ ᱥᱮᱛᱟ ᱢᱮᱱᱟᱜ ᱟ", "injag seta menag a"],
    ["Do you have a pen?", "ᱟᱢᱟᱜ ᱠᱟᱞᱟᱢ ᱢᱮᱱᱟᱜ ᱟ?", "amag kalam menag a?"]
]

LESSONS[583] = [
    ["What does this mean?", "ᱱᱚᱣᱟ ᱪᱮᱫ ᱢᱟᱱᱮ?", "nowa ced mane?"],
    ["What is the meaning of this word?", "ᱱᱚᱣᱟ ᱨᱚᱲ ᱟᱜ ᱢᱟᱱᱮ ᱪᱮᱫ?", "nowa ror ag mane ced?"],
    ["I mean to say", "ᱤᱧ ᱨᱚᱲ ᱥᱟᱱᱟᱢ ᱟ", "inj ror sanam a"],
    ["It means 'water'", "ᱚᱱᱟ ᱢᱟᱱᱮ 'ᱫᱟᱜ'", "ona mane 'dag'"],
    ["What does 'johar' mean?", "'ᱡᱚᱦᱟᱨ' ᱢᱟᱱᱮ ᱪᱮᱫ?", "'johar' mane ced?"],
    ["It means 'hello'", "ᱚᱱᱟ ᱢᱟᱱᱮ 'ᱡᱚᱦᱟᱨ'", "ona mane 'johar'"],
    ["What do you mean?", "ᱟᱢᱟᱜ ᱢᱟᱱᱮ ᱪᱮᱫ?", "amag mane ced?"],
    ["I don't understand the meaning", "ᱤᱧ ᱢᱟᱱᱮ ᱵᱟᱝ ᱵᱩᱡᱷᱟᱹᱣ ᱟ", "inj mane bang bujhaw a"],
    ["What is the meaning of 'disom'?", "'ᱫᱤᱥᱚᱢ' ᱢᱟᱱᱮ ᱪᱮᱫ?", "'disom' mane ced?"],
    ["'Disom' means 'country'", "'ᱫᱤᱥᱚᱢ' ᱢᱟᱱᱮ 'ᱫᱤᱥᱚᱢ'", "'disom' mane 'country'"],
    ["This sentence means...", "ᱱᱚᱣᱟ ᱵᱟᱠᱤᱭᱟ ᱢᱟᱱᱮ...", "nowa bakiya mane..."],
    ["He didn't mean that", "ᱩᱱᱤ ᱚᱱᱟ ᱢᱟᱱᱮ ᱵᱟᱝ ᱨᱚᱲ ᱮᱱᱟ", "uni ona mane bang ror ena"],
    ["Tell me the meaning", "ᱤᱧ ᱠᱮ ᱢᱟᱱᱮ ᱨᱚᱲ ᱢᱮ", "inj ke mane ror me"],
    ["What is 'baha' in English?", "'ᱵᱟᱦᱟ' ᱤᱧᱜᱞᱤᱥ ᱨᱮ ᱪᱮᱫ?", "'baha' Inglis re ced?"],
    ["'Baha' means 'flower'", "'ᱵᱟᱦᱟ' ᱢᱟᱱᱮ 'flower'", "'baha' mane 'flower'"],
    ["Can you explain the meaning?", "ᱟᱢ ᱢᱟᱱᱮ ᱵᱩᱡᱷᱟᱹᱣ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am mane bujhaw dareyam ma?"],
    ["I know its meaning", "ᱤᱧ ᱚᱱᱟ ᱢᱟᱱᱮ ᱵᱟᱰᱟᱭ ᱟ", "inj ona mane baday a"],
    ["This word has many meanings", "ᱱᱚᱣᱟ ᱨᱚᱲ ᱟᱜ ᱟᱹᱰᱤ ᱢᱟᱱᱮ ᱢᱮᱱᱟᱜ ᱟ", "nowa ror ag adi mane menag a"]
]

LESSONS[584] = [
    ["And", "ᱟᱨ", "ar"],
    ["But", "ᱢᱮᱱᱠᱷᱟᱱ", "menkhan"],
    ["Because", "ᱪᱮᱫ ᱞᱟᱜᱤᱫ", "ced lagid"],
    ["So / Therefore", "ᱚᱱᱟ ᱞᱟᱜᱤᱫ", "ona lagid"],
    ["I went and he came", "ᱤᱧ ᱥᱮᱱ ᱮᱱᱟ ᱟᱨ ᱩᱱᱤ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "inj sen ena ar uni hijug ena"],
    ["I want to go but I can't", "ᱤᱧ ᱥᱮᱱ ᱥᱟᱱᱟᱢ ᱟ ᱢᱮᱱᱠᱷᱟᱱ ᱵᱟᱝ ᱫᱟᱲᱮᱭᱟᱜ ᱟ", "inj sen sanam a menkhan bang dareyag a"],
    ["He didn't come because he was sick", "ᱩᱱᱤ ᱵᱟᱝ ᱦᱤᱡᱩᱜ ᱮᱱᱟ ᱪᱮᱫ ᱞᱟᱜᱤᱫ ᱩᱱᱤ ᱨᱚᱜ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni bang hijug ena ced lagid uni rog taheny e"],
    ["It rained, so I stayed home", "ᱫᱟᱜ ᱫᱟᱹᱲ ᱮᱱᱟ ᱚᱱᱟ ᱞᱟᱜᱤᱫ ᱤᱧ ᱚᱲᱟᱜ ᱨᱮ ᱛᱟᱦᱮᱸᱱ ᱟ", "dag dar ena ona lagid inj orag re taheny a"],
    ["Although he is tired, he works", "ᱩᱱᱤ ᱛᱷᱟᱠᱟᱣ ᱢᱮᱱᱠᱷᱟᱱ ᱩᱱᱤ ᱠᱟᱹᱢᱤ ᱠᱮᱫ ᱮ", "uni thakaw menkhan uni kami ked e"],
    ["He is poor but honest", "ᱩᱱᱤ ᱜᱟᱨᱤᱵ ᱢᱮᱱᱠᱷᱟᱱ ᱥᱟᱹᱨᱤ ᱦᱚᱲ ᱠᱟᱱᱟ", "uni garib menkhan sari hor kana"],
    ["She sings and dances", "ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱟᱨ ᱮᱱᱮᱡ ᱮ", "uni sereny ar enej e"],
    ["I studied hard so I passed", "ᱤᱧ ᱟᱹᱰᱤ ᱯᱟᱲᱦᱟᱣ ᱮᱱᱟ ᱚᱱᱟ ᱞᱟᱜᱤᱫ ᱤᱧ ᱯᱟᱥ ᱮᱱᱟ", "inj adi parhaw ena ona lagid inj pas ena"],
    ["Though it was cold, we went", "ᱫᱷᱤᱨᱤ ᱢᱮᱱᱠᱷᱟᱱ ᱟᱞᱮ ᱥᱮᱱ ᱮᱱᱟ", "dhiri menkhan ale sen ena"],
    ["I like tea and she likes milk", "ᱤᱧ ᱪᱟᱹ ᱨᱟᱹᱥᱠᱟᱹ ᱟ ᱟᱨ ᱩᱱᱤ ᱫᱩᱫᱷ ᱨᱟᱹᱥᱠᱟᱹ ᱮ", "inj cha raska a ar uni dudh raska e"],
    ["He went early because he had work", "ᱩᱱᱤ ᱟᱜᱮ ᱥᱮᱱ ᱮᱱᱟ ᱪᱮᱫ ᱞᱟᱜᱤᱫ ᱩᱱᱤᱭᱟᱜ ᱠᱟᱹᱢᱤ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni age sen ena ced lagid uniag kami taheny e"],
    ["Still (yet)", "ᱟᱫᱚ ᱦᱚᱭ", "ado hoy"],
    ["Although small, he is strong", "ᱦᱩᱰᱤᱧ ᱢᱮᱱᱠᱷᱟᱱ ᱩᱱᱤ ᱡᱚᱨ ᱠᱟᱱᱟ", "huding menkhan uni jor kana"],
    ["She is young but wise", "ᱩᱱᱤ ᱦᱩᱰᱤᱧ ᱢᱮᱱᱠᱷᱟᱱ ᱵᱩᱫᱷᱤ ᱠᱟᱱᱟ", "uni huding menkhan budhi kana"]
]

LESSONS[585] = [
    ["Or", "ᱵᱟᱝᱠᱷᱟᱱ", "bangkhan"],
    ["Either...or", "ᱵᱟᱝᱠᱷᱟᱱ...ᱵᱟᱝᱠᱷᱟᱱ", "bangkhan...bangkhan"],
    ["If", "ᱨᱮᱫᱚ", "redo"],
    ["Tea or milk?", "ᱪᱟᱹ ᱵᱟᱝᱠᱷᱟᱱ ᱫᱩᱫᱷ?", "cha bangkhan dudh?"],
    ["Either he will come or she will", "ᱩᱱᱤ ᱵᱟᱝᱠᱷᱟᱱ ᱩᱱᱤ ᱦᱤᱡᱩᱜ ᱮ", "uni bangkhan uni hijug e"],
    ["If you come, I will go", "ᱟᱢ ᱦᱤᱡᱩᱜ ᱨᱮᱫᱚ ᱤᱧ ᱥᱮᱱ ᱟ", "am hijug redo inj sen a"],
    ["In case it rains, take an umbrella", "ᱫᱟᱜ ᱫᱟᱹᱲ ᱨᱮᱫᱚ ᱪᱷᱟᱛᱟ ᱤᱫᱤ ᱢᱮ", "dag dar redo chhata idi me"],
    ["Neither this nor that", "ᱱᱚᱣᱟ ᱵᱟᱝ ᱟᱨ ᱚᱱᱟ ᱵᱟᱝ", "nowa bang ar ona bang"],
    ["You can have rice or bread", "ᱟᱢ ᱫᱟᱹᱠ ᱵᱟᱝᱠᱷᱟᱱ ᱨᱩᱴᱤ ᱡᱚᱢ ᱫᱟᱲᱮᱭᱟᱢ", "am dak bangkhan ruti jom dareyam"],
    ["If provided with help, I can finish", "ᱥᱟᱹᱜᱟᱹᱭ ᱧᱟᱢ ᱨᱮᱫᱚ ᱤᱧ ᱛᱮᱭᱟᱨ ᱫᱟᱲᱮᱭᱟᱜ ᱟ", "sagay nyam redo inj teyar dareyag a"],
    ["Go or stay, it's your choice", "ᱥᱮᱱ ᱵᱟᱝᱠᱷᱟᱱ ᱛᱟᱦᱮᱸᱱ, ᱟᱢᱟᱜ ᱢᱚᱱᱮ", "sen bangkhan taheny, amag mone"],
    ["If you study, you will pass", "ᱟᱢ ᱯᱟᱲᱦᱟᱣ ᱨᱮᱫᱚ ᱟᱢ ᱯᱟᱥ ᱟᱢ", "am parhaw redo am pas am"],
    ["Neither he nor I went", "ᱩᱱᱤ ᱵᱟᱝ ᱟᱨ ᱤᱧ ᱵᱟᱝ ᱥᱮᱱ ᱮᱱᱟ", "uni bang ar inj bang sen ena"],
    ["In case of emergency, call me", "ᱥᱮᱱᱫᱨᱟ ᱨᱮᱫᱚ ᱤᱧ ᱠᱮ ᱠᱩᱞ ᱢᱮ", "sendra redo inj ke kul me"],
    ["Is it morning or evening?", "ᱥᱮᱛᱟᱜ ᱵᱟᱝᱠᱷᱟᱱ ᱧᱤᱸᱫᱟ?", "setag bangkhan nyinda?"],
    ["Buy this or that", "ᱱᱚᱣᱟ ᱵᱟᱝᱠᱷᱟᱱ ᱚᱱᱟ ᱠᱤᱱ ᱢᱮ", "nowa bangkhan ona kin me"],
    ["If he agrees, start work", "ᱩᱱᱤ ᱢᱟᱱᱟᱣ ᱨᱮᱫᱚ ᱠᱟᱹᱢᱤ ᱪᱟᱞᱩ ᱢᱮ", "uni manaw redo kami chalu me"],
    ["Shall we walk or take the bus?", "ᱟᱞᱮ ᱥᱟᱞᱟᱜ ᱵᱟᱝᱠᱷᱟᱱ ᱵᱟᱥ ᱤᱫᱤ?", "ale salag bangkhan bas idi?"]
]

LESSONS[586] = [
    ["After eating, I rested", "ᱡᱚᱢ ᱛᱟᱭᱚᱢ ᱤᱧ ᱥᱮᱨᱮᱧ ᱮᱱᱟ", "jom tayom inj sereny ena"],
    ["Then he came", "ᱛᱟᱭᱚᱢ ᱩᱱᱤ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "tayom uni hijug ena"],
    ["As far as I know", "ᱤᱧᱟᱜ ᱵᱟᱰᱟᱭ ᱞᱮᱠᱟ", "injag baday leka"],
    ["As long as you are here", "ᱟᱢ ᱱᱮᱛᱟᱨ ᱛᱟᱦᱮᱸᱱ ᱞᱮᱠᱟ", "am netar taheny leka"],
    ["As if he knew everything", "ᱩᱱᱤ ᱡᱚᱛᱚ ᱵᱟᱰᱟᱭ ᱞᱮᱠᱟ", "uni joto baday leka"],
    ["After studying, she went to sleep", "ᱯᱟᱲᱦᱟᱣ ᱛᱟᱭᱚᱢ ᱩᱱᱤ ᱧᱤᱫ ᱮᱱᱟ", "parhaw tayom uni nyid ena"],
    ["First eat, then go", "ᱟᱜᱮ ᱡᱚᱢ ᱢᱮ ᱛᱟᱭᱚᱢ ᱥᱮᱱ ᱢᱮ", "age jom me tayom sen me"],
    ["As far as the eye can see", "ᱢᱮᱫ ᱧᱮᱞ ᱫᱟᱲᱮ ᱞᱮᱠᱟ", "med nyel dare leka"],
    ["As long as there is life", "ᱡᱤᱣᱤ ᱢᱮᱱᱟᱜ ᱞᱮᱠᱟ", "jiwi menag leka"],
    ["After the rain stopped, we went", "ᱫᱟᱜ ᱛᱷᱤᱨ ᱛᱟᱭᱚᱢ ᱟᱞᱮ ᱥᱮᱱ ᱮᱱᱟ", "dag thir tayom ale sen ena"],
    ["Then I understood", "ᱛᱟᱭᱚᱢ ᱤᱧ ᱵᱩᱡᱷᱟᱹᱣ ᱮᱱᱟ", "tayom inj bujhaw ena"],
    ["As if nothing happened", "ᱡᱟᱦᱟᱸ ᱵᱟᱝ ᱦᱩᱭ ᱞᱮᱠᱟ", "jahang bang huy leka"],
    ["After he left, she cried", "ᱩᱱᱤ ᱥᱮᱱ ᱛᱟᱭᱚᱢ ᱩᱱᱤ ᱨᱟᱹᱢ ᱮᱱᱟ", "uni sen tayom uni ram ena"],
    ["As far as the mountain", "ᱵᱩᱨᱩ ᱛᱮ ᱞᱮᱠᱟ", "buru te leka"],
    ["First read, then write", "ᱟᱜᱮ ᱯᱟᱲᱦᱟᱣ ᱢᱮ ᱛᱟᱭᱚᱢ ᱚᱞ ᱢᱮ", "age parhaw me tayom ol me"],
    ["As long as I can remember", "ᱤᱧ ᱩᱢ ᱫᱟᱲᱮ ᱞᱮᱠᱟ", "inj um dare leka"],
    ["After cooking, she rested", "ᱨᱟᱸᱰᱷᱟ ᱛᱟᱭᱚᱢ ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱮᱱᱟ", "randha tayom uni sereny ena"],
    ["As if it would rain", "ᱫᱟᱜ ᱫᱟᱹᱲ ᱞᱮᱠᱟ", "dag dar leka"]
]

LESSONS[587] = [
    ["As soon as he came, we left", "ᱩᱱᱤ ᱦᱤᱡᱩᱜ ᱞᱮᱠᱟ ᱟᱞᱮ ᱥᱮᱱ ᱮᱱᱟ", "uni hijug leka ale sen ena"],
    ["Once I finish, I will come", "ᱤᱧ ᱛᱮᱭᱟᱨ ᱞᱮᱠᱟ ᱤᱧ ᱦᱤᱡᱩᱜ ᱟ", "inj teyar leka inj hijug a"],
    ["Rather than walking, take the bus", "ᱥᱟᱞᱟᱜ ᱠᱷᱚᱱ ᱵᱟᱥ ᱤᱫᱤ ᱢᱮ", "salag khon bas idi me"],
    ["Instead of tea, give me water", "ᱪᱟᱹ ᱡᱟᱭᱜᱟ ᱨᱮ ᱫᱟᱜ ᱮᱢ ᱢᱮ", "cha jayga re dag em me"],
    ["So that he can understand", "ᱩᱱᱤ ᱵᱩᱡᱷᱟᱹᱣ ᱫᱟᱲᱮ ᱞᱟᱜᱤᱫ", "uni bujhaw dare lagid"],
    ["As soon as it rains, come inside", "ᱫᱟᱜ ᱫᱟᱹᱲ ᱞᱮᱠᱟ ᱵᱷᱤᱛᱤᱨ ᱦᱤᱡᱩᱜ ᱢᱮ", "dag dar leka bhitir hijug me"],
    ["Once you learn, you won't forget", "ᱟᱢ ᱥᱮᱪᱮᱫ ᱞᱮᱠᱟ ᱟᱢ ᱵᱟᱝ ᱦᱮᱡ ᱠᱟᱹ ᱟᱢ", "am seced leka am bang hej ka am"],
    ["Rather than fighting, let's talk", "ᱞᱟᱲᱟᱭ ᱠᱷᱚᱱ ᱨᱚᱲ ᱟᱞᱮ", "laray khon ror ale"],
    ["Instead of rice, eat bread", "ᱫᱟᱹᱠ ᱡᱟᱭᱜᱟ ᱨᱮ ᱨᱩᱴᱤ ᱡᱚᱢ ᱢᱮ", "dak jayga re ruti jom me"],
    ["So that children can study", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱯᱟᱲᱦᱟᱣ ᱫᱟᱲᱮ ᱞᱟᱜᱤᱫ", "gidra ko parhaw dare lagid"],
    ["As soon as morning came", "ᱥᱮᱛᱟᱜ ᱦᱩᱭ ᱞᱮᱠᱟ", "setag huy leka"],
    ["Once he agreed, we started", "ᱩᱱᱤ ᱢᱟᱱᱟᱣ ᱞᱮᱠᱟ ᱟᱞᱮ ᱪᱟᱞᱩ ᱮᱱᱟ", "uni manaw leka ale chalu ena"],
    ["Rather than buying, make it", "ᱠᱤᱱ ᱠᱷᱚᱱ ᱛᱮᱭᱟᱨ ᱢᱮ", "kin khon teyar me"],
    ["Instead of sleeping, study", "ᱧᱤᱫ ᱡᱟᱭᱜᱟ ᱨᱮ ᱯᱟᱲᱦᱟᱣ ᱢᱮ", "nyid jayga re parhaw me"],
    ["So that we can finish", "ᱟᱞᱮ ᱛᱮᱭᱟᱨ ᱫᱟᱲᱮ ᱞᱟᱜᱤᱫ", "ale teyar dare lagid"],
    ["As soon as I saw him", "ᱤᱧ ᱩᱱᱤ ᱠᱮ ᱧᱮᱞ ᱞᱮᱠᱟ", "inj uni ke nyel leka"],
    ["Once started, don't stop", "ᱪᱟᱞᱩ ᱞᱮᱠᱟ ᱛᱷᱤᱨ ᱡᱷᱤᱡ ᱢᱮ", "chalu leka thir jhij me"],
    ["Rather than crying, try again", "ᱨᱟᱹᱢ ᱠᱷᱚᱱ ᱟᱨ ᱢᱤᱫ ᱪᱮᱥᱴᱟ ᱢᱮ", "ram khon ar mid chesta me"]
]

LESSONS[588] = [
    ["And", "ᱟᱨ", "ar"],
    ["But / However", "ᱢᱮᱱᱠᱷᱟᱱ", "menkhan"],
    ["Because", "ᱪᱮᱫ ᱞᱟᱜᱤᱫ", "ced lagid"],
    ["So / Therefore", "ᱚᱱᱟ ᱞᱟᱜᱤᱫ", "ona lagid"],
    ["Or", "ᱵᱟᱝᱠᱷᱟᱱ", "bangkhan"],
    ["If", "ᱨᱮᱫᱚ", "redo"],
    ["Then / After that", "ᱛᱟᱭᱚᱢ", "tayom"],
    ["Although / Even though", "ᱢᱮᱱᱠᱷᱟᱱ ᱦᱚᱭ", "menkhan hoy"],
    ["Still / Yet", "ᱟᱫᱚ ᱦᱚᱭ", "ado hoy"],
    ["As / Like", "ᱞᱮᱠᱟ", "leka"],
    ["That (conjunction)", "ᱡᱟᱦᱟᱸ", "jahang"],
    ["While / When", "ᱵᱮᱞᱟ ᱨᱮ", "bela re"],
    ["Until", "ᱛᱮ ᱞᱮᱠᱟ", "te leka"],
    ["Before", "ᱟᱜᱮ", "age"],
    ["After", "ᱛᱟᱭᱚᱢ", "tayom"],
    ["Instead of", "ᱡᱟᱭᱜᱟ ᱨᱮ", "jayga re"],
    ["In order to / So that", "ᱞᱟᱜᱤᱫ", "lagid"],
    ["As soon as", "ᱞᱮᱠᱟ (immediately after)", "leka"]
]

LESSONS[589] = [
    ["I went and he came", "ᱤᱧ ᱥᱮᱱ ᱮᱱᱟ ᱟᱨ ᱩᱱᱤ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "inj sen ena ar uni hijug ena"],
    ["She cooked and I ate", "ᱩᱱᱤ ᱨᱟᱸᱰᱷᱟ ᱮᱱᱟ ᱟᱨ ᱤᱧ ᱡᱚᱢ ᱮᱱᱟ", "uni randha ena ar inj jom ena"],
    ["He studied because he wanted to pass", "ᱩᱱᱤ ᱯᱟᱲᱦᱟᱣ ᱮᱱᱟ ᱪᱮᱫ ᱞᱟᱜᱤᱫ ᱩᱱᱤ ᱯᱟᱥ ᱥᱟᱱᱟᱢ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni parhaw ena ced lagid uni pas sanam taheny e"],
    ["It was cold but we went", "ᱫᱷᱤᱨᱤ ᱛᱟᱦᱮᱸᱱ ᱟ ᱢᱮᱱᱠᱷᱟᱱ ᱟᱞᱮ ᱥᱮᱱ ᱮᱱᱟ", "dhiri taheny a menkhan ale sen ena"],
    ["Mother cooked and father ate", "ᱟᱭᱚ ᱨᱟᱸᱰᱷᱟ ᱮᱱᱟ ᱟᱨ ᱟᱯᱟ ᱡᱚᱢ ᱮᱱᱟ", "ayo randha ena ar apa jom ena"],
    ["He runs fast so he always wins", "ᱩᱱᱤ ᱡᱚᱨ ᱫᱟᱹᱲ ᱮ ᱚᱱᱟ ᱞᱟᱜᱤᱫ ᱩᱱᱤ ᱡᱟᱦᱟᱸᱱᱟᱜ ᱡᱤᱛ ᱮ", "uni jor dar e ona lagid uni jahanag jit e"],
    ["When I reached home, it was dark", "ᱤᱧ ᱚᱲᱟᱜ ᱦᱤᱡᱩᱜ ᱵᱮᱞᱟ ᱧᱩᱛ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj orag hijug bela nyut taheny a"],
    ["Although he is young, he is wise", "ᱩᱱᱤ ᱦᱩᱰᱤᱧ ᱢᱮᱱᱠᱷᱟᱱ ᱩᱱᱤ ᱵᱩᱫᱷᱤ ᱠᱟᱱᱟ", "uni huding menkhan uni budhi kana"],
    ["She left before I arrived", "ᱤᱧ ᱦᱤᱡᱩᱜ ᱟᱜᱮ ᱩᱱᱤ ᱥᱮᱱ ᱮᱱᱟ", "inj hijug age uni sen ena"],
    ["I will go after the rain stops", "ᱫᱟᱜ ᱛᱷᱤᱨ ᱛᱟᱭᱚᱢ ᱤᱧ ᱥᱮᱱ ᱟ", "dag thir tayom inj sen a"],
    ["He is rich but unhappy", "ᱩᱱᱤ ᱫᱷᱚᱱᱤ ᱢᱮᱱᱠᱷᱟᱱ ᱨᱟᱹᱥᱠᱟᱹ ᱵᱟᱝ ᱠᱟᱱᱟ", "uni dhoni menkhan raska bang kana"],
    ["She wrote and he read", "ᱩᱱᱤ ᱚᱞ ᱮᱱᱟ ᱟᱨ ᱩᱱᱤ ᱯᱟᱲᱦᱟᱣ ᱮᱱᱟ", "uni ol ena ar uni parhaw ena"],
    ["We went to the market and bought vegetables", "ᱟᱞᱮ ᱵᱟᱡᱟᱨ ᱥᱮᱱ ᱮᱱᱟ ᱟᱨ ᱥᱟᱜ ᱠᱤᱱ ᱮᱱᱟ", "ale bajar sen ena ar sag kin ena"],
    ["He was sick so he didn't come", "ᱩᱱᱤ ᱨᱚᱜ ᱛᱟᱦᱮᱸᱱ ᱮ ᱚᱱᱟ ᱞᱟᱜᱤᱫ ᱵᱟᱝ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "uni rog taheny e ona lagid bang hijug ena"],
    ["I will come if you call", "ᱟᱢ ᱠᱩᱞ ᱨᱮᱫᱚ ᱤᱧ ᱦᱤᱡᱩᱜ ᱟ", "am kul redo inj hijug a"],
    ["She sang while he played", "ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱮᱱᱟ ᱵᱮᱞᱟ ᱩᱱᱤ ᱮᱱᱮᱡ ᱮᱱᱟ", "uni sereny ena bela uni enej ena"],
    ["Eat rice or bread", "ᱫᱟᱹᱠ ᱵᱟᱝᱠᱷᱟᱱ ᱨᱩᱴᱤ ᱡᱚᱢ ᱢᱮ", "dak bangkhan ruti jom me"],
    ["I study so that I learn", "ᱤᱧ ᱯᱟᱲᱦᱟᱣ ᱟᱭᱟ ᱥᱮᱪᱮᱫ ᱞᱟᱜᱤᱫ", "inj parhaw aya seced lagid"]
]

# 590-596 remaining
LESSONS[590] = [
    ["He came running", "ᱩᱱᱤ ᱫᱟᱹᱲ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "uni dar hijug ena"],
    ["She left crying", "ᱩᱱᱤ ᱨᱟᱹᱢ ᱥᱮᱱ ᱮᱱᱟ", "uni ram sen ena"],
    ["He sat down to eat", "ᱩᱱᱤ ᱡᱚᱢ ᱞᱟᱜᱤᱫ ᱫᱩᱲᱩᱵ ᱮᱱᱟ", "uni jom lagid durub ena"],
    ["She finished cooking", "ᱩᱱᱤ ᱨᱟᱸᱰᱷᱟ ᱛᱮᱭᱟᱨ ᱮᱱᱟ", "uni randha teyar ena"],
    ["He started speaking", "ᱩᱱᱤ ᱨᱚᱲ ᱪᱟᱞᱩ ᱮᱱᱟ", "uni ror chalu ena"],
    ["She went to sleep", "ᱩᱱᱤ ᱧᱤᱫ ᱥᱮᱱ ᱮᱱᱟ", "uni nyid sen ena"],
    ["He fell down walking", "ᱩᱱᱤ ᱥᱟᱞᱟᱜ ᱩᱭᱩᱜ ᱮᱱᱟ", "uni salag uyug ena"],
    ["I went out to see", "ᱤᱧ ᱧᱮᱞ ᱞᱟᱜᱤᱫ ᱵᱟᱦᱨᱮ ᱥᱮᱱ ᱮᱱᱟ", "inj nyel lagid bahre sen ena"],
    ["She kept on singing", "ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni sereny taheny e"],
    ["He got up to leave", "ᱩᱱᱤ ᱥᱮᱱ ᱞᱟᱜᱤᱫ ᱛᱤᱧᱜᱩ ᱮᱱᱟ", "uni sen lagid tingu ena"],
    ["She came back singing", "ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱨᱩᱣᱟᱹᱲ ᱮᱱᱟ", "uni sereny ruwar ena"],
    ["He stayed sitting", "ᱩᱱᱤ ᱫᱩᱲᱩᱵ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni durub taheny e"],
    ["I stopped reading", "ᱤᱧ ᱯᱟᱲᱦᱟᱣ ᱛᱷᱤᱨ ᱮᱱᱟ", "inj parhaw thir ena"],
    ["She went to buy", "ᱩᱱᱤ ᱠᱤᱱ ᱥᱮᱱ ᱮᱱᱟ", "uni kin sen ena"],
    ["He came to help", "ᱩᱱᱤ ᱥᱟᱹᱜᱟᱹᱭ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "uni sagay hijug ena"],
    ["She started to cry", "ᱩᱱᱤ ᱨᱟᱹᱢ ᱪᱟᱞᱩ ᱮᱱᱟ", "uni ram chalu ena"],
    ["I went to bring water", "ᱤᱧ ᱫᱟᱜ ᱟᱹᱜᱩ ᱥᱮᱱ ᱮᱱᱟ", "inj dag agu sen ena"],
    ["He kept watching", "ᱩᱱᱤ ᱧᱮᱞ ᱛᱟᱦᱮᱸᱱ ᱮ", "uni nyel taheny e"]
]

LESSONS[591] = [
    ["The food was eaten by him", "ᱡᱚᱢ ᱩᱱᱤ ᱠᱷᱚᱱ ᱡᱚᱢ ᱦᱩᱭ ᱮᱱᱟ", "jom uni khon jom huy ena"],
    ["The book was read by her", "ᱯᱩᱛᱷᱤ ᱩᱱᱤ ᱠᱷᱚᱱ ᱯᱟᱲᱦᱟᱣ ᱦᱩᱭ ᱮᱱᱟ", "puthi uni khon parhaw huy ena"],
    ["The letter was written", "ᱪᱤᱴᱷᱤ ᱚᱞ ᱦᱩᱭ ᱮᱱᱟ", "chithi ol huy ena"],
    ["The tree was cut", "ᱫᱟᱨᱮ ᱛᱚᱞ ᱦᱩᱭ ᱮᱱᱟ", "dare tol huy ena"],
    ["The house was built", "ᱚᱲᱟᱜ ᱛᱮᱭᱟᱨ ᱦᱩᱭ ᱮᱱᱟ", "orag teyar huy ena"],
    ["The song was sung by children", "ᱥᱮᱨᱮᱧ ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱠᱷᱚᱱ ᱥᱮᱨᱮᱧ ᱦᱩᱭ ᱮᱱᱟ", "sereny gidra ko khon sereny huy ena"],
    ["The door was opened", "ᱫᱩᱣᱟᱹᱨ ᱡᱷᱤᱡ ᱦᱩᱭ ᱮᱱᱟ", "duwar jhij huy ena"],
    ["The work was done", "ᱠᱟᱹᱢᱤ ᱛᱮᱭᱟᱨ ᱦᱩᱭ ᱮᱱᱟ", "kami teyar huy ena"],
    ["Rice was cooked", "ᱫᱟᱹᱠ ᱨᱟᱸᱰᱷᱟ ᱦᱩᱭ ᱮᱱᱟ", "dak randha huy ena"],
    ["The clothes were washed", "ᱠᱟᱹᱯᱲᱟ ᱡᱩ ᱦᱩᱭ ᱮᱱᱟ", "kapra ju huy ena"],
    ["The field was plowed", "ᱜᱟᱰᱟ ᱡᱚᱛ ᱦᱩᱭ ᱮᱱᱟ", "gada jot huy ena"],
    ["The milk was drunk", "ᱫᱩᱫᱷ ᱧᱩ ᱦᱩᱭ ᱮᱱᱟ", "dudh nyu huy ena"],
    ["Water was brought", "ᱫᱟᱜ ᱟᱹᱜᱩ ᱦᱩᱭ ᱮᱱᱟ", "dag agu huy ena"],
    ["The meeting was held", "ᱵᱮᱱᱫᱚᱵᱚᱥᱛ ᱦᱩᱭ ᱮᱱᱟ", "bendobost huy ena"],
    ["The festival was celebrated", "ᱯᱚᱨᱚᱵ ᱢᱟᱱᱟᱣ ᱦᱩᱭ ᱮᱱᱟ", "porob manaw huy ena"],
    ["The fish was caught", "ᱢᱟᱹᱪᱷᱟ ᱫᱟᱹᱲ ᱦᱩᱭ ᱮᱱᱟ", "machha dar huy ena"],
    ["The money was paid", "ᱴᱟᱠᱟ ᱮᱢ ᱦᱩᱭ ᱮᱱᱟ", "taka em huy ena"],
    ["The road was built", "ᱨᱟᱦᱟ ᱛᱮᱭᱟᱨ ᱦᱩᱭ ᱮᱱᱟ", "raha teyar huy ena"]
]

LESSONS[592] = [
    ["The rice is being cooked", "ᱫᱟᱹᱠ ᱨᱟᱸᱰᱷᱟ ᱦᱩᱭ ᱢᱮᱱᱟᱜ ᱟ", "dak randha huy menag a"],
    ["The book is being read", "ᱯᱩᱛᱷᱤ ᱯᱟᱲᱦᱟᱣ ᱦᱩᱭ ᱢᱮᱱᱟᱜ ᱟ", "puthi parhaw huy menag a"],
    ["The work will be done", "ᱠᱟᱹᱢᱤ ᱛᱮᱭᱟᱨ ᱦᱩᱭ ᱟ", "kami teyar huy a"],
    ["The food will be served", "ᱡᱚᱢ ᱮᱢ ᱦᱩᱭ ᱟ", "jom em huy a"],
    ["The letter is being written", "ᱪᱤᱴᱷᱤ ᱚᱞ ᱦᱩᱭ ᱢᱮᱱᱟᱜ ᱟ", "chithi ol huy menag a"],
    ["The house is being cleaned", "ᱚᱲᱟᱜ ᱥᱟᱯᱷᱟ ᱦᱩᱭ ᱢᱮᱱᱟᱜ ᱟ", "orag sapha huy menag a"],
    ["The tree will be planted", "ᱫᱟᱨᱮ ᱛᱟᱞᱟ ᱦᱩᱭ ᱟ", "dare tala huy a"],
    ["The song is being sung", "ᱥᱮᱨᱮᱧ ᱦᱩᱭ ᱢᱮᱱᱟᱜ ᱟ", "sereny huy menag a"],
    ["The money will be returned", "ᱴᱟᱠᱟ ᱨᱩᱣᱟᱹᱲ ᱦᱩᱭ ᱟ", "taka ruwar huy a"],
    ["Clothes are being washed", "ᱠᱟᱹᱯᱲᱟ ᱡᱩ ᱦᱩᱭ ᱢᱮᱱᱟᱜ ᱟ", "kapra ju huy menag a"],
    ["The road is being repaired", "ᱨᱟᱦᱟ ᱛᱮᱭᱟᱨ ᱦᱩᱭ ᱢᱮᱱᱟᱜ ᱟ", "raha teyar huy menag a"],
    ["Tea is being made", "ᱪᱟᱹ ᱛᱮᱭᱟᱨ ᱦᱩᱭ ᱢᱮᱱᱟᱜ ᱟ", "cha teyar huy menag a"],
    ["The door is being closed", "ᱫᱩᱣᱟᱹᱨ ᱫᱟᱸᱰ ᱦᱩᱭ ᱢᱮᱱᱟᱜ ᱟ", "duwar dand huy menag a"],
    ["The field will be harvested", "ᱜᱟᱰᱟ ᱠᱟᱴ ᱦᱩᱭ ᱟ", "gada kat huy a"],
    ["The festival will be celebrated", "ᱯᱚᱨᱚᱵ ᱢᱟᱱᱟᱣ ᱦᱩᱭ ᱟ", "porob manaw huy a"],
    ["Fish is being caught", "ᱢᱟᱹᱪᱷᱟ ᱫᱟᱹᱲ ᱦᱩᱭ ᱢᱮᱱᱟᱜ ᱟ", "machha dar huy menag a"],
    ["The exam will be held", "ᱯᱚᱨᱤᱠᱷᱟ ᱦᱩᱭ ᱟ", "porikha huy a"],
    ["Vegetables are being sold", "ᱥᱟᱜ ᱵᱮᱪᱟᱣ ᱦᱩᱭ ᱢᱮᱱᱟᱜ ᱟ", "sag becaw huy menag a"]
]

LESSONS[593] = [
    ["I feel happy", "ᱤᱧ ᱨᱟᱹᱥᱠᱟᱹ ᱢᱚᱱᱮ ᱟ", "inj raska mone a"],
    ["I feel sad", "ᱤᱧ ᱫᱩᱠᱷ ᱢᱚᱱᱮ ᱟ", "inj dukh mone a"],
    ["I feel tired", "ᱤᱧ ᱛᱷᱟᱠᱟᱣ ᱢᱚᱱᱮ ᱟ", "inj thakaw mone a"],
    ["I think he is right", "ᱤᱧ ᱢᱚᱱᱮ ᱟ ᱩᱱᱤ ᱵᱷᱟᱞᱮ ᱠᱟᱱᱟ", "inj mone a uni bhale kana"],
    ["I think it will rain", "ᱤᱧ ᱢᱚᱱᱮ ᱟ ᱫᱟᱜ ᱫᱟᱹᱲ ᱟ", "inj mone a dag dar a"],
    ["She feels cold", "ᱩᱱᱤ ᱫᱷᱤᱨᱤ ᱢᱚᱱᱮ ᱮ", "uni dhiri mone e"],
    ["He thinks he can do it", "ᱩᱱᱤ ᱢᱚᱱᱮ ᱮ ᱩᱱᱤ ᱫᱟᱲᱮ ᱮ", "uni mone e uni dare e"],
    ["I feel hungry", "ᱤᱧ ᱱᱮᱞᱦᱟ ᱢᱚᱱᱮ ᱟ", "inj nelha mone a"],
    ["I think we should go", "ᱤᱧ ᱢᱚᱱᱮ ᱟ ᱟᱞᱮ ᱥᱮᱱ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "inj mone a ale sen lagid ale"],
    ["She feels lonely", "ᱩᱱᱤ ᱮᱠᱞᱟ ᱢᱚᱱᱮ ᱮ", "uni ekla mone e"],
    ["I feel scared", "ᱤᱧ ᱵᱚᱨ ᱢᱚᱱᱮ ᱟ", "inj bor mone a"],
    ["He thinks she is kind", "ᱩᱱᱤ ᱢᱚᱱᱮ ᱮ ᱩᱱᱤ ᱵᱷᱟᱞᱮ ᱦᱚᱲ ᱠᱟᱱᱟ", "uni mone e uni bhale hor kana"],
    ["I feel better now", "ᱤᱧ ᱱᱤᱛ ᱵᱷᱟᱞᱮ ᱢᱚᱱᱮ ᱟ", "inj nit bhale mone a"],
    ["She thinks it is true", "ᱩᱱᱤ ᱢᱚᱱᱮ ᱮ ᱚᱱᱟ ᱥᱟᱹᱨᱤ ᱠᱟᱱᱟ", "uni mone e ona sari kana"],
    ["I feel proud", "ᱤᱧ ᱜᱚᱨᱵ ᱢᱚᱱᱮ ᱟ", "inj gorb mone a"],
    ["He feels angry", "ᱩᱱᱤ ᱨᱤᱥ ᱢᱚᱱᱮ ᱮ", "uni ris mone e"],
    ["I don't think so", "ᱤᱧ ᱚᱱᱟ ᱵᱟᱝ ᱢᱚᱱᱮ ᱟ", "inj ona bang mone a"],
    ["She feels sleepy", "ᱩᱱᱤ ᱧᱤᱫ ᱢᱚᱱᱮ ᱮ", "uni nyid mone e"]
]

LESSONS[594] = [
    ["Actions speak louder than words", "ᱠᱟᱹᱢᱤ ᱨᱚᱲ ᱠᱷᱚᱱ ᱢᱟᱨᱟᱝ ᱠᱟᱱᱟ", "kami ror khon marang kana"],
    ["Where there's a will, there's a way", "ᱢᱚᱱᱮ ᱢᱮᱱᱟᱜ ᱨᱮᱫᱚ ᱨᱟᱦᱟ ᱢᱮᱱᱟᱜ ᱟ", "mone menag redo raha menag a"],
    ["Drop by drop fills the pot", "ᱛᱤᱯᱟᱹ ᱛᱤᱯᱟᱹ ᱜᱟᱜᱲᱤ ᱵᱷᱚᱨᱛᱤ ᱮ", "tipa tipa gagri bhorti e"],
    ["United we stand, divided we fall", "ᱥᱟᱶᱛᱮ ᱛᱤᱧᱜᱩ ᱟᱞᱮ, ᱵᱟᱲᱟᱭ ᱩᱭᱩᱜ ᱟᱞᱮ", "sawte tingu ale, baray uyug ale"],
    ["Slow and steady wins the race", "ᱟᱹᱭᱥᱛᱮ ᱟᱨ ᱛᱷᱤᱨ ᱡᱤᱛ ᱮ", "ayste ar thir jit e"],
    ["Empty vessels make the most noise", "ᱠᱷᱟᱞᱤ ᱜᱟᱜᱲᱤ ᱟᱹᱰᱤ ᱫᱟᱸᱜ ᱮ", "khali gagri adi dang e"],
    ["A friend in need is a friend indeed", "ᱫᱩᱠᱷ ᱨᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱥᱟᱹᱨᱤ ᱥᱟᱶᱛᱟ ᱠᱟᱱᱟ", "dukh re sagay sari sawta kana"],
    ["Strike while the iron is hot", "ᱞᱚᱦᱟ ᱫᱩᱨᱩᱵ ᱵᱮᱞᱟ ᱨᱮ ᱫᱟᱹᱲ ᱢᱮ", "loha durub bela re dar me"],
    ["Don't count your chickens before they hatch", "ᱟᱜᱮ ᱠᱷᱚᱱ ᱵᱟᱝ ᱜᱟᱱ ᱢᱮ", "age khon bang gan me"],
    ["Where there is smoke, there is fire", "ᱫᱷᱩᱣᱟᱸ ᱢᱮᱱᱟᱜ ᱨᱮᱫᱚ ᱥᱮᱸᱜᱮᱞ ᱢᱮᱱᱟᱜ ᱟ", "dhuwan menag redo sengel menag a"],
    ["Practice makes perfect", "ᱟᱵᱷᱤᱭᱟᱥ ᱵᱷᱟᱞᱮ ᱠᱮᱫ ᱮ", "abhiyas bhale ked e"],
    ["Every cloud has a silver lining", "ᱡᱚᱛᱚ ᱨᱤᱢᱤᱞ ᱨᱮ ᱡᱟᱞᱟᱜ ᱢᱮᱱᱟᱜ ᱟ", "joto rimil re jalag menag a"],
    ["The early bird catches the worm", "ᱟᱜᱮ ᱪᱮᱨᱮ ᱡᱚᱢ ᱧᱟᱢ ᱮ", "age cere jom nyam e"],
    ["Haste makes waste", "ᱡᱟᱞᱫᱤ ᱨᱮ ᱵᱟᱝ ᱵᱷᱟᱞᱮ ᱦᱩᱭ ᱟ", "jaldi re bang bhale huy a"],
    ["Blood is thicker than water", "ᱢᱟᱹᱭᱟᱢ ᱫᱟᱜ ᱠᱷᱚᱱ ᱢᱚᱴᱟ ᱠᱟᱱᱟ", "mayam dag khon mota kana"],
    ["Honesty is the best policy", "ᱥᱟᱹᱨᱤ ᱡᱚᱛᱚ ᱠᱷᱚᱱ ᱵᱷᱟᱞᱮ ᱨᱟᱦᱟ ᱠᱟᱱᱟ", "sari joto khon bhale raha kana"],
    ["One tree does not make a forest", "ᱢᱤᱫ ᱫᱟᱨᱮ ᱵᱤᱨ ᱵᱟᱝ ᱛᱮᱭᱟᱨ ᱮ", "mid dare bir bang teyar e"],
    ["Knowledge is power", "ᱵᱤᱫᱭᱟ ᱡᱚᱨ ᱠᱟᱱᱟ", "bidya jor kana"]
]

LESSONS[595] = [
    ["Don't cry over spilled milk", "ᱩᱭᱩᱜ ᱫᱩᱫᱷ ᱞᱟᱜᱤᱫ ᱵᱟᱝ ᱨᱟᱹᱢ ᱢᱮ", "uyug dudh lagid bang ram me"],
    ["Look before you leap", "ᱩᱪᱟᱹᱲ ᱟᱜᱮ ᱧᱮᱞ ᱢᱮ", "uchar age nyel me"],
    ["Two wrongs don't make a right", "ᱵᱟᱨ ᱯᱩᱨᱟᱹ ᱵᱷᱟᱞᱮ ᱵᱟᱝ ᱛᱮᱭᱟᱨ ᱮ", "bar pura bhale bang teyar e"],
    ["When in Rome, do as Romans do", "ᱚᱱᱟ ᱫᱤᱥᱚᱢ ᱨᱮ ᱚᱱᱟ ᱞᱮᱠᱟ ᱠᱮᱫ ᱢᱮ", "ona disom re ona leka ked me"],
    ["The pen is mightier than the sword", "ᱠᱟᱞᱟᱢ ᱛᱟᱞᱣᱟᱨ ᱠᱷᱚᱱ ᱡᱚᱨ ᱠᱟᱱᱟ", "kalam talwar khon jor kana"],
    ["Don't put all eggs in one basket", "ᱡᱚᱛᱚ ᱵᱤᱸᱰᱤ ᱢᱤᱫ ᱵᱟᱠᱥᱚ ᱨᱮ ᱡᱷᱤᱡ ᱫᱚᱦᱚ ᱢᱮ", "joto bindi mid bakso re jhij doho me"],
    ["Charity begins at home", "ᱫᱟᱱ ᱚᱲᱟᱜ ᱠᱷᱚᱱ ᱪᱟᱞᱩ ᱟ", "dan orag khon chalu a"],
    ["Time and tide wait for none", "ᱵᱮᱞᱟ ᱡᱟᱦᱟᱸ ᱞᱟᱜᱤᱫ ᱵᱟᱝ ᱡᱚᱜᱟᱹᱣ ᱟ", "bela jahang lagid bang jogaw a"],
    ["Necessity is the mother of invention", "ᱞᱟᱜᱤᱫ ᱱᱟᱣᱟ ᱡᱤᱱᱤᱥ ᱛᱮᱭᱟᱨ ᱟᱭᱚ ᱠᱟᱱᱟ", "lagid nawa jinis teyar ayo kana"],
    ["All that glitters is not gold", "ᱡᱚᱛᱚ ᱡᱟᱞᱟᱜ ᱥᱚᱱᱟ ᱵᱟᱝ ᱠᱟᱱᱟ", "joto jalag sona bang kana"],
    ["Rome was not built in a day", "ᱢᱟᱨᱟᱝ ᱠᱟᱹᱢᱤ ᱢᱤᱫ ᱫᱤᱱ ᱨᱮ ᱵᱟᱝ ᱛᱮᱭᱟᱨ ᱟ", "marang kami mid din re bang teyar a"],
    ["A stitch in time saves nine", "ᱵᱮᱞᱟ ᱨᱮ ᱢᱤᱫ ᱥᱮᱞᱮᱫ ᱟᱹᱰᱤ ᱵᱟᱸᱪᱟᱣ ᱟ", "bela re mid seled adi banchaw a"],
    ["Better late than never", "ᱞᱮᱴ ᱵᱟᱝ ᱠᱷᱚᱱ ᱵᱷᱟᱞᱮ ᱠᱟᱱᱟ", "let bang khon bhale kana"],
    ["God helps those who help themselves", "ᱢᱟᱨᱟᱝ ᱵᱩᱨᱩ ᱚᱱᱟ ᱦᱚᱲ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱮ ᱚᱠᱚᱭ ᱟᱯᱱᱟᱨ ᱥᱟᱹᱜᱟᱹᱭ ᱮ", "marang buru ona hor ke sagay e okoy apnar sagay e"],
    ["Old is gold", "ᱢᱟᱨᱟᱝ ᱥᱚᱱᱟ ᱞᱮᱠᱟ ᱠᱟᱱᱟ", "marang sona leka kana"],
    ["Money doesn't grow on trees", "ᱴᱟᱠᱟ ᱫᱟᱨᱮ ᱨᱮ ᱵᱟᱝ ᱵᱚᱞᱚ ᱟ", "taka dare re bang bolo a"],
    ["No pain, no gain", "ᱫᱩᱠᱷ ᱵᱟᱝ ᱨᱮᱫᱚ ᱥᱩᱠᱷ ᱵᱟᱝ", "dukh bang redo sukh bang"],
    ["Too many cooks spoil the broth", "ᱟᱹᱰᱤ ᱨᱟᱸᱰᱷᱟᱱᱤ ᱡᱚᱢ ᱯᱩᱨᱟᱹ ᱮ", "adi randhani jom pura e"]
]

LESSONS[596] = [
    ["If I had money, I would buy a house", "ᱤᱧᱟᱜ ᱴᱟᱠᱟ ᱢᱮᱱᱟᱜ ᱨᱮᱫᱚ ᱤᱧ ᱚᱲᱟᱜ ᱠᱤᱱ ᱟ", "injag taka menag redo inj orag kin a"],
    ["If she had studied, she would have passed", "ᱩᱱᱤ ᱯᱟᱲᱦᱟᱣ ᱨᱮᱫᱚ ᱩᱱᱤ ᱯᱟᱥ ᱮ", "uni parhaw redo uni pas e"],
    ["If it hadn't rained, we would have gone", "ᱫᱟᱜ ᱵᱟᱝ ᱫᱟᱹᱲ ᱨᱮᱫᱚ ᱟᱞᱮ ᱥᱮᱱ ᱟᱞᱮ", "dag bang dar redo ale sen ale"],
    ["If he had come, I would have helped", "ᱩᱱᱤ ᱦᱤᱡᱩᱜ ᱨᱮᱫᱚ ᱤᱧ ᱥᱟᱹᱜᱟᱹᱭ ᱟ", "uni hijug redo inj sagay a"],
    ["If I knew the answer, I would tell you", "ᱤᱧ ᱡᱟᱣᱟᱵ ᱵᱟᱰᱟᱭ ᱨᱮᱫᱚ ᱤᱧ ᱟᱢ ᱠᱮ ᱨᱚᱲ ᱟ", "inj jawab baday redo inj am ke ror a"],
    ["If I were you, I would go", "ᱤᱧ ᱟᱢ ᱞᱮᱠᱟ ᱨᱮᱫᱚ ᱤᱧ ᱥᱮᱱ ᱟ", "inj am leka redo inj sen a"],
    ["If they had invited us, we would have come", "ᱩᱱᱠᱩ ᱟᱞᱮ ᱠᱮ ᱠᱩᱞ ᱨᱮᱫᱚ ᱟᱞᱮ ᱦᱤᱡᱩᱜ ᱟᱞᱮ", "unku ale ke kul redo ale hijug ale"],
    ["If the bus was on time, I wouldn't be late", "ᱵᱟᱥ ᱵᱮᱞᱟ ᱨᱮ ᱨᱮᱫᱚ ᱤᱧ ᱞᱮᱴ ᱵᱟᱝ ᱟ", "bas bela re redo inj let bang a"],
    ["If I had a car, I would drive", "ᱤᱧᱟᱜ ᱜᱟᱰᱤ ᱢᱮᱱᱟᱜ ᱨᱮᱫᱚ ᱤᱧ ᱪᱟᱞᱟᱣ ᱟ", "injag gadi menag redo inj chalaw a"],
    ["If she could sing, she would join", "ᱩᱱᱤ ᱥᱮᱨᱮᱧ ᱫᱟᱲᱮ ᱨᱮᱫᱚ ᱩᱱᱤ ᱥᱟᱶᱛᱮ ᱮ", "uni sereny dare redo uni sawte e"],
    ["If we had food, we would eat", "ᱟᱞᱮᱭᱟᱜ ᱡᱚᱢ ᱢᱮᱱᱟᱜ ᱨᱮᱫᱚ ᱟᱞᱮ ᱡᱚᱢ ᱟᱞᱮ", "aleyag jom menag redo ale jom ale"],
    ["If the weather was good, we would go out", "ᱵᱮᱞᱟ ᱵᱷᱟᱞᱮ ᱨᱮᱫᱚ ᱟᱞᱮ ᱵᱟᱦᱨᱮ ᱥᱮᱱ ᱟᱞᱮ", "bela bhale redo ale bahre sen ale"],
    ["If he spoke Santali, I would understand", "ᱩᱱᱤ ᱥᱟᱱᱛᱟᱲᱤ ᱨᱚᱲ ᱨᱮᱫᱚ ᱤᱧ ᱵᱩᱡᱷᱟᱹᱣ ᱟ", "uni santari ror redo inj bujhaw a"],
    ["If I had time, I would read", "ᱤᱧᱟᱜ ᱵᱮᱞᱟ ᱢᱮᱱᱟᱜ ᱨᱮᱫᱚ ᱤᱧ ᱯᱟᱲᱦᱟᱣ ᱟ", "injag bela menag redo inj parhaw a"],
    ["If father agreed, we would celebrate", "ᱟᱯᱟ ᱢᱟᱱᱟᱣ ᱨᱮᱫᱚ ᱟᱞᱮ ᱢᱟᱱᱟᱣ ᱟᱞᱮ", "apa manaw redo ale manaw ale"],
    ["If she helped, we would finish faster", "ᱩᱱᱤ ᱥᱟᱹᱜᱟᱹᱭ ᱨᱮᱫᱚ ᱟᱞᱮ ᱡᱟᱞᱫᱤ ᱛᱮᱭᱟᱨ ᱟᱞᱮ", "uni sagay redo ale jaldi teyar ale"],
    ["If we could fly, we would reach quickly", "ᱟᱞᱮ ᱩᱰᱟᱹᱣ ᱫᱟᱲᱮ ᱨᱮᱫᱚ ᱡᱟᱞᱫᱤ ᱦᱤᱡᱩᱜ ᱟᱞᱮ", "ale udaw dare redo jaldi hijug ale"],
    ["If I were rich, I would help the poor", "ᱤᱧ ᱫᱷᱚᱱᱤ ᱨᱮᱫᱚ ᱤᱧ ᱜᱟᱨᱤᱵ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱟ", "inj dhoni redo inj garib ke sagay a"]
]

for ch in d:
    if ch['id'] in LESSONS:
        ch['blocks'] = [{"type": "table", "columns": ["English", "Santali (Ol Chiki)", "Transliteration"], "rows": LESSONS[ch['id']]}]

open('data_santali.json', 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('Section 3c (579-596) populated')
