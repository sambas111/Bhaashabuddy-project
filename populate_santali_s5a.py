import json

d = json.load(open('data_santali.json', 'r', encoding='utf-8'))

LESSONS = {}

# 620 - Diwali Festival
LESSONS[620] = [
    ["Happy Diwali!", "ᱫᱤᱯᱟᱹᱵᱷᱤ ᱯᱚᱨᱚᱵ ᱨᱟᱹᱥᱠᱟᱹ ᱢᱟ!", "dipabhi porob raska ma!"],
    ["We celebrate Diwali with joy", "ᱟᱞᱮ ᱫᱤᱯᱟᱹᱵᱷᱤ ᱨᱟᱹᱥᱠᱟᱹ ᱨᱮ ᱢᱟᱱᱟᱣ ᱟᱞᱮ", "ale dipabhi raska re manaw ale"],
    ["We light lamps at home", "ᱟᱞᱮ ᱚᱲᱟᱜ ᱨᱮ ᱫᱤᱭᱟ ᱡᱟᱞᱟᱣ ᱟᱞᱮ", "ale orag re diya jalaw ale"],
    ["Children burst firecrackers", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱯᱟᱴᱠᱟ ᱯᱷᱩᱴᱟᱣ ᱠᱚ", "gidra ko patka phutaw ko"],
    ["Mother makes sweets", "ᱟᱭᱚ ᱡᱤᱞᱤᱯᱤ ᱛᱮᱭᱟᱨ ᱟᱫ ᱮ", "ayo jilipi teyar ad e"],
    ["We clean the house before Diwali", "ᱫᱤᱯᱟᱹᱵᱷᱤ ᱟᱜᱮ ᱟᱞᱮ ᱚᱲᱟᱜ ᱥᱟᱯᱷᱟ ᱟᱞᱮ", "dipabhi age ale orag sapha ale"],
    ["The whole village is decorated", "ᱥᱟᱹᱨᱟᱹ ᱟᱹᱛᱩ ᱥᱚᱢᱵᱷᱟᱨ ᱢᱮᱱᱟᱜ ᱟ", "sara atu sombhar menag a"],
    ["We wear new clothes", "ᱟᱞᱮ ᱱᱟᱣᱟ ᱠᱟᱹᱯᱲᱟ ᱫᱚᱦᱚ ᱟᱞᱮ", "ale nawa kapra doho ale"],
    ["Friends and family come together", "ᱥᱟᱶᱛᱟ ᱟᱨ ᱯᱟᱹᱨᱤᱵᱟᱨ ᱥᱟᱶᱛᱮ ᱦᱤᱡᱩᱜ ᱠᱚ", "sawta ar paribar sawte hijug ko"],
    ["We share sweets with neighbours", "ᱟᱞᱮ ᱜᱚᱲᱟ ᱦᱚᱲ ᱥᱟᱶ ᱡᱤᱞᱤᱯᱤ ᱮᱢ ᱟᱞᱮ", "ale gora hor saw jilipi em ale"],
    ["Diwali is the festival of lights", "ᱫᱤᱯᱟᱹᱵᱷᱤ ᱡᱟᱞᱟᱜ ᱯᱚᱨᱚᱵ ᱠᱟᱱᱟ", "dipabhi jalag porob kana"],
    ["We pray for prosperity", "ᱟᱞᱮ ᱵᱷᱟᱞᱮ ᱞᱟᱜᱤᱫ ᱵᱤᱱᱛᱤ ᱟᱞᱮ", "ale bhale lagid binti ale"],
    ["The sky is full of fireworks", "ᱥᱮᱨᱢᱟ ᱯᱟᱴᱠᱟ ᱛᱮ ᱵᱷᱚᱨᱛᱤ ᱢᱮᱱᱟᱜ ᱟ", "serma patka te bhorti menag a"],
    ["We eat together as a family", "ᱟᱞᱮ ᱯᱟᱹᱨᱤᱵᱟᱨ ᱥᱟᱶᱛᱮ ᱡᱚᱢ ᱟᱞᱮ", "ale paribar sawte jom ale"],
    ["May this Diwali bring happiness", "ᱱᱚᱣᱟ ᱫᱤᱯᱟᱹᱵᱷᱤ ᱨᱟᱹᱥᱠᱟᱹ ᱟᱹᱜᱩ ᱮᱢ ᱢᱟ", "nowa dipabhi raska agu em ma"],
    ["Rangoli is made at the door", "ᱫᱩᱣᱟᱹᱨ ᱨᱮ ᱨᱟᱸᱜᱚᱞᱤ ᱛᱮᱭᱟᱨ ᱦᱩᱭ ᱟ", "duwar re rangoli teyar huy a"],
    ["Diwali comes every year", "ᱫᱤᱯᱟᱹᱵᱷᱤ ᱥᱮᱨᱢᱟ ᱥᱮᱨᱢᱟ ᱦᱤᱡᱩᱜ ᱟ", "dipabhi serma serma hijug a"],
    ["We enjoy Diwali very much", "ᱟᱞᱮ ᱫᱤᱯᱟᱹᱵᱷᱤ ᱟᱹᱰᱤ ᱨᱟᱹᱥᱠᱟᱹ ᱟᱞᱮ", "ale dipabhi adi raska ale"]
]

# 621 - Simple Sentences Introduction/Salutation
LESSONS[621] = [
    ["Hello! Greetings!", "ᱡᱚᱦᱟᱨ!", "johar!"],
    ["How are you?", "ᱟᱢ ᱚᱠᱟ ᱠᱟᱱᱟ?", "am oka kana?"],
    ["I am fine", "ᱤᱧ ᱵᱟᱝ ᱢᱮᱱᱟᱜ ᱟ", "inj bang menag a"],
    ["What is your name?", "ᱟᱢᱟᱜ ᱧᱩᱛᱩᱢ ᱪᱮᱫ?", "amag nyutum ced?"],
    ["My name is Soren", "ᱤᱧᱟᱜ ᱧᱩᱛᱩᱢ ᱥᱚᱨᱮᱱ", "injag nyutum Soren"],
    ["Where are you from?", "ᱟᱢ ᱚᱠᱟ ᱠᱷᱚᱱ ᱠᱟᱱᱟ?", "am oka khon kana?"],
    ["I am from Jharkhand", "ᱤᱧ ᱡᱷᱟᱨᱠᱷᱚᱸᱰ ᱠᱷᱚᱱ ᱠᱟᱱᱟ", "inj Jharkhand khon kana"],
    ["Nice to meet you", "ᱟᱢ ᱥᱟᱶ ᱧᱮᱞᱚᱜ ᱨᱟᱹᱥᱠᱟᱹ ᱮᱱᱟ", "am saw nyelog raska ena"],
    ["Please come in", "ᱦᱮᱡ ᱵᱷᱤᱛᱤᱨ ᱦᱤᱡᱩᱜ ᱢᱮ", "hej bhitir hijug me"],
    ["Please sit down", "ᱦᱮᱡ ᱫᱩᱲᱩᱵ ᱢᱮ", "hej durub me"],
    ["How is your family?", "ᱟᱢᱟᱜ ᱯᱟᱹᱨᱤᱵᱟᱨ ᱚᱠᱟ ᱠᱟᱱᱟ?", "amag paribar oka kana?"],
    ["Everyone is well", "ᱡᱚᱛᱚ ᱵᱷᱟᱞᱮ ᱢᱮᱱᱟᱜ ᱟ", "joto bhale menag a"],
    ["What do you do?", "ᱟᱢ ᱪᱮᱫ ᱠᱟᱹᱢᱤ ᱠᱮᱫ ᱟᱢ?", "am ced kami ked am?"],
    ["I am a teacher", "ᱤᱧ ᱢᱤᱫ ᱯᱟᱲᱦᱟᱣᱮᱫ ᱠᱟᱱᱟ", "inj mid parhawed kana"],
    ["Thank you very much", "ᱥᱮᱨᱢᱟ ᱫᱟᱲᱮᱭᱟᱜ ᱢᱟ", "serma dareyag ma"],
    ["Goodbye, go well", "ᱡᱚᱦᱟᱨ, ᱵᱷᱟᱞᱮ ᱥᱮᱱ ᱢᱮ", "johar, bhale sen me"],
    ["See you again", "ᱟᱨ ᱢᱤᱫ ᱫᱤᱱ ᱧᱮᱞᱚᱜ ᱟᱞᱮ", "ar mid din nyelog ale"],
    ["May you be well", "ᱟᱢ ᱵᱷᱟᱞᱮ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "am bhale taheny me"]
]

# 622 - Time Related
LESSONS[622] = [
    ["What time is it?", "ᱚᱛᱚ ᱵᱮᱞᱟ ᱦᱩᱭ ᱮᱱᱟ?", "oto bela huy ena?"],
    ["It is morning", "ᱥᱮᱛᱟᱜ ᱦᱩᱭ ᱮᱱᱟ", "setag huy ena"],
    ["It is afternoon", "ᱛᱤᱠᱤᱱ ᱦᱩᱭ ᱮᱱᱟ", "tikin huy ena"],
    ["It is evening now", "ᱱᱤᱛ ᱧᱤᱸᱫᱟ ᱦᱩᱭ ᱮᱱᱟ", "nit nyinda huy ena"],
    ["I wake up early in the morning", "ᱤᱧ ᱥᱮᱛᱟᱜ ᱟᱜᱮ ᱪᱟᱹᱞᱩ ᱟᱭᱟ", "inj setag age chalu aya"],
    ["I go to school at 8 o'clock", "ᱤᱧ ᱤᱨᱟᱞ ᱵᱮᱞᱟ ᱥᱠᱩᱞ ᱥᱮᱱ ᱟᱭᱟ", "inj iral bela skul sen aya"],
    ["Lunch is at noon", "ᱛᱤᱠᱤᱱ ᱨᱮ ᱡᱚᱢ ᱡᱚᱢ", "tikin re jom jom"],
    ["I come home at 5", "ᱤᱧ ᱢᱚᱬᱮ ᱵᱮᱞᱟ ᱚᱲᱟᱜ ᱨᱩᱣᱟᱹᱲ ᱟᱭᱟ", "inj mone bela orag ruwar aya"],
    ["I sleep at night", "ᱤᱧ ᱧᱤᱸᱫᱟ ᱨᱮ ᱧᱤᱫ ᱟᱭᱟ", "inj nyinda re nyid aya"],
    ["Today is Monday", "ᱟᱡ ᱥᱚᱢᱵᱟᱨ ᱠᱟᱱᱟ", "aj sombar kana"],
    ["Tomorrow is a holiday", "ᱜᱟᱯᱟ ᱪᱷᱩᱴᱴᱤ ᱠᱟᱱᱟ", "gapa chhutti kana"],
    ["Yesterday I went to the market", "ᱜᱟᱞᱟ ᱤᱧ ᱵᱟᱡᱟᱨ ᱥᱮᱱ ᱮᱱᱟ", "gala inj bajar sen ena"],
    ["It's getting late", "ᱞᱮᱴ ᱦᱩᱭ ᱢᱮᱱᱟᱜ ᱟ", "let huy menag a"],
    ["Come on time", "ᱵᱮᱞᱟ ᱨᱮ ᱦᱤᱡᱩᱜ ᱢᱮ", "bela re hijug me"],
    ["I don't have time today", "ᱟᱡ ᱤᱧᱟᱜ ᱵᱮᱞᱟ ᱵᱟᱝ ᱢᱮᱱᱟᱜ ᱟ", "aj injag bela bang menag a"],
    ["Wait a moment", "ᱟᱹᱛᱩ ᱦᱮᱞᱟ ᱡᱚᱜᱟᱹᱣ ᱢᱮ", "atu hela jogaw me"],
    ["How long will it take?", "ᱚᱛᱚ ᱵᱮᱞᱟ ᱞᱟᱜᱤᱫ ᱟ?", "oto bela lagid a?"],
    ["Time is very important", "ᱵᱮᱞᱟ ᱟᱹᱰᱤ ᱫᱚᱨᱠᱟᱨ ᱠᱟᱱᱟ", "bela adi dorkar kana"]
]

# 623 - Where/Place Related
LESSONS[623] = [
    ["Where are you going?", "ᱟᱢ ᱚᱠᱟ ᱥᱮᱱ ᱟᱢ?", "am oka sen am?"],
    ["I am going home", "ᱤᱧ ᱚᱲᱟᱜ ᱥᱮᱱ ᱟᱭᱟ", "inj orag sen aya"],
    ["Where is the market?", "ᱵᱟᱡᱟᱨ ᱚᱠᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ?", "bajar oka re menag a?"],
    ["The market is near the school", "ᱵᱟᱡᱟᱨ ᱥᱠᱩᱞ ᱱᱮᱰᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "bajar skul neda re menag a"],
    ["Where is the hospital?", "ᱦᱟᱥᱯᱟᱛᱟᱞ ᱚᱠᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ?", "haspatal oka re menag a?"],
    ["Go straight then turn left", "ᱥᱤᱫᱷᱟ ᱥᱮᱱ ᱢᱮ ᱛᱟᱭᱚᱢ ᱞᱮᱯᱷᱴ ᱢᱩᱲᱩᱜ ᱢᱮ", "sidha sen me tayom left murug me"],
    ["How far is the village?", "ᱟᱹᱛᱩ ᱚᱛᱚ ᱫᱩᱨ ᱢᱮᱱᱟᱜ ᱟ?", "atu oto dur menag a?"],
    ["It is very close", "ᱟᱹᱰᱤ ᱱᱮᱰᱟ ᱢᱮᱱᱟᱜ ᱟ", "adi neda menag a"],
    ["It is far from here", "ᱱᱮᱛᱟᱨ ᱠᱷᱚᱱ ᱫᱩᱨ ᱢᱮᱱᱟᱜ ᱟ", "netar khon dur menag a"],
    ["Is there a bus stop nearby?", "ᱱᱮᱰᱟ ᱨᱮ ᱵᱟᱥ ᱥᱴᱚᱯ ᱢᱮᱱᱟᱜ ᱟ?", "neda re bas stop menag a?"],
    ["Where do you live?", "ᱟᱢ ᱚᱠᱟ ᱨᱮ ᱛᱟᱦᱮᱸᱱ ᱟᱢ?", "am oka re taheny am?"],
    ["I live in Dumka", "ᱤᱧ ᱫᱩᱢᱠᱟ ᱨᱮ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj Dumka re taheny a"],
    ["This place is very beautiful", "ᱱᱚᱣᱟ ᱡᱟᱭᱜᱟ ᱟᱹᱰᱤ ᱥᱚᱢᱵᱷᱟᱨ ᱢᱮᱱᱟᱜ ᱟ", "nowa jayga adi sombhar menag a"],
    ["Which road goes to the station?", "ᱚᱠᱟ ᱨᱟᱦᱟ ᱥᱴᱮᱥᱚᱱ ᱛᱮ ᱥᱮᱱ ᱟ?", "oka raha steson te sen a?"],
    ["The temple is on the hill", "ᱛᱷᱟᱱ ᱵᱩᱨᱩ ᱪᱮᱛᱟᱱ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "than buru cetan re menag a"],
    ["There is a river behind the village", "ᱟᱹᱛᱩ ᱯᱤᱪᱷᱟ ᱨᱮ ᱜᱟᱰᱟ ᱢᱮᱱᱟᱜ ᱟ", "atu pichha re gada menag a"],
    ["I have never been there", "ᱤᱧ ᱡᱟᱦᱟᱸᱱᱟᱜ ᱚᱱᱫᱮ ᱵᱟᱝ ᱥᱮᱱ ᱮᱱᱟ", "inj jahanag onde bang sen ena"],
    ["Show me the way", "ᱤᱧ ᱠᱮ ᱨᱟᱦᱟ ᱫᱮᱠᱷᱟᱣ ᱢᱮ", "inj ke raha dekhaw me"]
]

# 624 - In Hotel
LESSONS[624] = [
    ["Do you have a room available?", "ᱟᱢᱟᱜ ᱠᱚᱴᱷᱟ ᱢᱮᱱᱟᱜ ᱟ?", "amag kotha menag a?"],
    ["I need a room for one night", "ᱤᱧ ᱢᱤᱫ ᱧᱤᱸᱫᱟ ᱞᱟᱜᱤᱫ ᱠᱚᱴᱷᱟ ᱥᱟᱱᱟᱢ ᱟ", "inj mid nyinda lagid kotha sanam a"],
    ["How much is the room charge?", "ᱠᱚᱴᱷᱟ ᱟᱜ ᱫᱟᱢ ᱚᱛᱚ?", "kotha ag dam oto?"],
    ["Please give me the key", "ᱦᱮᱡ ᱤᱧ ᱠᱮ ᱪᱟᱵᱤ ᱮᱢ ᱢᱮ", "hej inj ke chabi em me"],
    ["Is breakfast included?", "ᱥᱮᱛᱟᱜ ᱡᱚᱢ ᱥᱟᱶᱛᱮ ᱢᱮᱱᱟᱜ ᱟ?", "setag jom sawte menag a?"],
    ["The room is clean", "ᱠᱚᱴᱷᱟ ᱥᱟᱯᱷᱟ ᱢᱮᱱᱟᱜ ᱟ", "kotha sapha menag a"],
    ["Please bring water", "ᱦᱮᱡ ᱫᱟᱜ ᱟᱹᱜᱩ ᱢᱮ", "hej dag agu me"],
    ["I want to order food", "ᱤᱧ ᱡᱚᱢ ᱚᱨᱰᱟᱨ ᱥᱟᱱᱟᱢ ᱟ", "inj jom order sanam a"],
    ["Please give me the menu", "ᱦᱮᱡ ᱢᱮᱱᱩ ᱮᱢ ᱢᱮ", "hej menu em me"],
    ["I want rice and vegetables", "ᱤᱧ ᱫᱟᱹᱠ ᱟᱨ ᱥᱟᱜ ᱥᱟᱱᱟᱢ ᱟ", "inj dak ar sag sanam a"],
    ["The food was very tasty", "ᱡᱚᱢ ᱟᱹᱰᱤ ᱫᱷᱟᱹᱨᱤ ᱛᱟᱦᱮᱸᱱ ᱟ", "jom adi dhari taheny a"],
    ["Please bring the bill", "ᱦᱮᱡ ᱵᱤᱞ ᱟᱹᱜᱩ ᱢᱮ", "hej bil agu me"],
    ["I am checking out tomorrow", "ᱤᱧ ᱜᱟᱯᱟ ᱪᱮᱠ ᱟᱣᱩᱴ ᱟ", "inj gapa check out a"],
    ["Is there WiFi here?", "ᱱᱮᱛᱟᱨ ᱣᱟᱭᱯᱷᱟᱭ ᱢᱮᱱᱟᱜ ᱟ?", "netar WiFi menag a?"],
    ["Can I get an extra blanket?", "ᱤᱧ ᱟᱨ ᱢᱤᱫ ᱠᱟᱸᱵᱚᱞ ᱧᱟᱢ ᱫᱟᱲᱮᱭᱟᱜ ᱢᱟ?", "inj ar mid kambol nyam dareyag ma?"],
    ["Please clean the room", "ᱦᱮᱡ ᱠᱚᱴᱷᱟ ᱥᱟᱯᱷᱟ ᱢᱮ", "hej kotha sapha me"],
    ["Thank you for the service", "ᱥᱮᱨᱢᱟ ᱟᱢᱟᱜ ᱥᱮᱵᱟ ᱞᱟᱜᱤᱫ", "serma amag seba lagid"],
    ["I had a good stay", "ᱤᱧᱟᱜ ᱵᱷᱟᱞᱮ ᱛᱟᱦᱮᱸᱱ ᱮᱱᱟ", "injag bhale taheny ena"]
]

# 625 - Weather Related
LESSONS[625] = [
    ["How is the weather today?", "ᱟᱡ ᱵᱮᱞᱟ ᱚᱠᱟ ᱢᱮᱱᱟᱜ ᱟ?", "aj bela oka menag a?"],
    ["It is very hot today", "ᱟᱡ ᱟᱹᱰᱤ ᱫᱩᱨᱩᱵ ᱢᱮᱱᱟᱜ ᱟ", "aj adi durub menag a"],
    ["It is cold today", "ᱟᱡ ᱫᱷᱤᱨᱤ ᱢᱮᱱᱟᱜ ᱟ", "aj dhiri menag a"],
    ["It is raining", "ᱫᱟᱜ ᱫᱟᱹᱲ ᱢᱮᱱᱟᱜ ᱟ", "dag dar menag a"],
    ["The rain has stopped", "ᱫᱟᱜ ᱛᱷᱤᱨ ᱮᱱᱟ", "dag thir ena"],
    ["The sky is cloudy", "ᱥᱮᱨᱢᱟ ᱨᱤᱢᱤᱞ ᱢᱮᱱᱟᱜ ᱟ", "serma rimil menag a"],
    ["The sun is shining", "ᱥᱤᱧ ᱡᱟᱞᱟᱜ ᱢᱮᱱᱟᱜ ᱟ", "sing jalag menag a"],
    ["The wind is blowing strongly", "ᱦᱚᱭᱚ ᱡᱚᱨ ᱪᱟᱞᱟᱜ ᱢᱮᱱᱟᱜ ᱟ", "hoyo jor chalag menag a"],
    ["It might rain tomorrow", "ᱜᱟᱯᱟ ᱫᱟᱜ ᱫᱟᱹᱲ ᱟᱠᱟᱫ ᱟ", "gapa dag dar akad a"],
    ["Take an umbrella", "ᱪᱷᱟᱛᱟ ᱤᱫᱤ ᱢᱮ", "chhata idi me"],
    ["The summer is very hot here", "ᱱᱮᱛᱟᱨ ᱜᱤᱥᱢᱟ ᱟᱹᱰᱤ ᱫᱩᱨᱩᱵ ᱟ", "netar gisma adi durub a"],
    ["Winter is approaching", "ᱡᱟᱲ ᱦᱤᱡᱩᱜ ᱢᱮᱱᱟᱜ ᱟ", "jar hijug menag a"],
    ["I like rainy season", "ᱤᱧ ᱫᱟᱜ ᱫᱟᱹᱲ ᱵᱮᱞᱟ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "inj dag dar bela raska a"],
    ["It is pleasant weather", "ᱵᱮᱞᱟ ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ ᱢᱮᱱᱟᱜ ᱟ", "bela adi bhale menag a"],
    ["There was a storm yesterday", "ᱜᱟᱞᱟ ᱟᱸᱫᱷᱤ ᱛᱟᱦᱮᱸᱱ ᱟ", "gala andhi taheny a"],
    ["The river floods in monsoon", "ᱵᱟᱨᱥᱟ ᱨᱮ ᱜᱟᱰᱟ ᱫᱟᱜ ᱵᱟᱦᱟ ᱟ", "barsa re gada dag baha a"],
    ["Wear warm clothes", "ᱜᱚᱨᱚᱢ ᱠᱟᱹᱯᱲᱟ ᱫᱚᱦᱚ ᱢᱮ", "gorom kapra doho me"],
    ["The fog is thick this morning", "ᱟᱡ ᱥᱮᱛᱟᱜ ᱟᱹᱰᱤ ᱠᱩᱭᱟᱸᱥᱟ ᱢᱮᱱᱟᱜ ᱟ", "aj setag adi kuyansa menag a"]
]

# 626 - Traffic Police
LESSONS[626] = [
    ["Good morning, officer", "ᱡᱚᱦᱟᱨ ᱥᱟᱦᱮᱵ", "johar saheb"],
    ["Please show your license", "ᱦᱮᱡ ᱟᱢᱟᱜ ᱞᱟᱤᱥᱮᱱᱥ ᱫᱮᱠᱷᱟᱣ ᱢᱮ", "hej amag license dekhaw me"],
    ["Here is my driving license", "ᱱᱚᱣᱟ ᱤᱧᱟᱜ ᱰᱨᱟᱭᱵᱷᱤᱝ ᱞᱟᱤᱥᱮᱱᱥ", "nowa injag driving license"],
    ["You were driving too fast", "ᱟᱢ ᱟᱹᱰᱤ ᱡᱚᱨ ᱪᱟᱞᱟᱣ ᱛᱟᱦᱮᱸᱱ ᱟᱢ", "am adi jor chalaw taheny am"],
    ["I am sorry, I will be careful", "ᱢᱟᱹᱧᱡᱷᱤ, ᱤᱧ ᱥᱟᱵᱫᱷᱟᱱ ᱛᱟᱦᱮᱸᱱ ᱟ", "manjhi, inj sabdhan taheny a"],
    ["Where is the traffic signal?", "ᱴᱨᱟᱯᱷᱤᱠ ᱥᱤᱜᱱᱟᱞ ᱚᱠᱟ ᱨᱮ?", "traffic signal oka re?"],
    ["Stop at the red light", "ᱟᱨᱟᱜ ᱵᱟᱛᱤ ᱨᱮ ᱛᱷᱤᱨ ᱢᱮ", "arag bati re thir me"],
    ["Wear your helmet", "ᱦᱮᱞᱢᱮᱴ ᱫᱚᱦᱚ ᱢᱮ", "helmet doho me"],
    ["Wear your seatbelt", "ᱥᱤᱴᱵᱮᱞᱴ ᱫᱚᱦᱚ ᱢᱮ", "seatbelt doho me"],
    ["This road is one-way", "ᱱᱚᱣᱟ ᱨᱟᱦᱟ ᱢᱤᱫ ᱫᱤᱥᱟ ᱨᱟᱦᱟ ᱠᱟᱱᱟ", "nowa raha mid disa raha kana"],
    ["You cannot park here", "ᱟᱢ ᱱᱮᱛᱟᱨ ᱜᱟᱰᱤ ᱵᱟᱝ ᱫᱚᱦᱚ ᱫᱟᱲᱮᱭᱟᱢ", "am netar gadi bang doho dareyam"],
    ["The road is blocked", "ᱨᱟᱦᱟ ᱵᱚᱱᱫ ᱢᱮᱱᱟᱜ ᱟ", "raha bond menag a"],
    ["Take the alternative route", "ᱟᱨ ᱢᱤᱫ ᱨᱟᱦᱟ ᱤᱫᱤ ᱢᱮ", "ar mid raha idi me"],
    ["How much is the fine?", "ᱡᱩᱨᱤᱢᱟᱱᱟ ᱚᱛᱚ?", "jurimana oto?"],
    ["I will not break the rule again", "ᱤᱧ ᱟᱨ ᱱᱤᱭᱚᱢ ᱵᱟᱝ ᱵᱷᱟᱸᱜᱟ ᱟ", "inj ar niyom bang bhanga a"],
    ["Drive safely", "ᱥᱟᱵᱫᱷᱟᱱ ᱞᱮᱠᱟ ᱪᱟᱞᱟᱣ ᱢᱮ", "sabdhan leka chalaw me"],
    ["Follow the traffic rules", "ᱴᱨᱟᱯᱷᱤᱠ ᱱᱤᱭᱚᱢ ᱢᱟᱱ ᱢᱮ", "traffic niyom man me"],
    ["Thank you officer, I will be careful", "ᱥᱮᱨᱢᱟ ᱥᱟᱦᱮᱵ, ᱤᱧ ᱥᱟᱵᱫᱷᱟᱱ ᱛᱟᱦᱮᱸᱱ ᱟ", "serma saheb, inj sabdhan taheny a"]
]

# 627 - Rickshaw/Taxi Driver
LESSONS[627] = [
    ["I need a rickshaw", "ᱤᱧ ᱨᱤᱠᱥᱟ ᱥᱟᱱᱟᱢ ᱟ", "inj riksa sanam a"],
    ["Where do you want to go?", "ᱟᱢ ᱚᱠᱟ ᱥᱮᱱ ᱥᱟᱱᱟᱢ ᱟᱢ?", "am oka sen sanam am?"],
    ["Take me to the bus stand", "ᱤᱧ ᱠᱮ ᱵᱟᱥ ᱥᱴᱮᱱᱰ ᱥᱮᱱ ᱢᱮ", "inj ke bas stand sen me"],
    ["How much will you charge?", "ᱟᱢ ᱚᱛᱚ ᱴᱟᱠᱟ ᱤᱫᱤ ᱟᱢ?", "am oto taka idi am?"],
    ["That is too much", "ᱚᱱᱟ ᱟᱹᱰᱤ ᱟᱛᱚ ᱢᱮᱱᱟᱜ ᱟ", "ona adi ato menag a"],
    ["Please go faster", "ᱦᱮᱡ ᱡᱚᱨ ᱥᱮᱱ ᱢᱮ", "hej jor sen me"],
    ["Please drive slowly", "ᱦᱮᱡ ᱟᱹᱭᱥᱛᱮ ᱪᱟᱞᱟᱣ ᱢᱮ", "hej ayste chalaw me"],
    ["Stop here please", "ᱦᱮᱡ ᱱᱮᱛᱟᱨ ᱛᱷᱤᱨ ᱢᱮ", "hej netar thir me"],
    ["Turn right at the next crossing", "ᱟᱜᱤᱞᱟ ᱢᱚᱲ ᱨᱮ ᱨᱟᱤᱴ ᱢᱩᱲᱩᱜ ᱢᱮ", "agila mor re right murug me"],
    ["How far is the station?", "ᱥᱴᱮᱥᱚᱱ ᱚᱛᱚ ᱫᱩᱨ ᱢᱮᱱᱟᱜ ᱟ?", "steson oto dur menag a?"],
    ["It will take 15 minutes", "ᱜᱮᱞ ᱢᱚᱬᱮ ᱢᱤᱱᱤᱴ ᱞᱟᱜᱤᱫ ᱟ", "gel mone minit lagid a"],
    ["Can you wait here?", "ᱟᱢ ᱱᱮᱛᱟᱨ ᱡᱚᱜᱟᱹᱣ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am netar jogaw dareyam ma?"],
    ["I will come back in 10 minutes", "ᱤᱧ ᱜᱮᱞ ᱢᱤᱱᱤᱴ ᱨᱮ ᱨᱩᱣᱟᱹᱲ ᱟ", "inj gel minit re ruwar a"],
    ["Keep the change", "ᱵᱟᱠᱤ ᱴᱟᱠᱟ ᱟᱢᱟᱜ ᱤᱫᱤ ᱢᱮ", "baki taka amag idi me"],
    ["Thank you for the ride", "ᱥᱮᱨᱢᱟ ᱟᱢᱟᱜ ᱥᱮᱵᱟ ᱞᱟᱜᱤᱫ", "serma amag seba lagid"],
    ["The road has a lot of traffic", "ᱨᱟᱦᱟ ᱨᱮ ᱟᱹᱰᱤ ᱜᱟᱰᱤ ᱢᱮᱱᱟᱜ ᱟ", "raha re adi gadi menag a"],
    ["Take the shortcut", "ᱪᱤᱯᱤᱴ ᱨᱟᱦᱟ ᱤᱫᱤ ᱢᱮ", "chipit raha idi me"],
    ["We have reached, stop here", "ᱟᱞᱮ ᱦᱤᱡᱩᱜ ᱮᱱᱟ, ᱱᱮᱛᱟᱨ ᱛᱷᱤᱨ ᱢᱮ", "ale hijug ena, netar thir me"]
]

# 628 - Software Engineers
LESSONS[628] = [
    ["I work in a software company", "ᱤᱧ ᱥᱚᱯᱷᱴᱣᱮᱭᱟᱨ ᱠᱚᱢᱯᱟᱱᱤ ᱨᱮ ᱠᱟᱹᱢᱤ ᱠᱮᱫ ᱟᱭᱟ", "inj software company re kami ked aya"],
    ["What project are you working on?", "ᱟᱢ ᱚᱠᱟ ᱯᱨᱚᱡᱮᱠᱴ ᱨᱮ ᱠᱟᱹᱢᱤ ᱟᱢ?", "am oka project re kami am?"],
    ["I am a developer", "ᱤᱧ ᱢᱤᱫ ᱰᱮᱵᱷᱮᱞᱚᱯᱟᱨ ᱠᱟᱱᱟ", "inj mid developer kana"],
    ["The deadline is tomorrow", "ᱰᱮᱰᱞᱟᱤᱱ ᱜᱟᱯᱟ ᱠᱟᱱᱟ", "deadline gapa kana"],
    ["Let us have a meeting", "ᱟᱞᱮ ᱢᱤᱴᱤᱝ ᱠᱮᱫ ᱟᱞᱮ", "ale meeting ked ale"],
    ["I need to fix this bug", "ᱤᱧ ᱱᱚᱣᱟ ᱵᱟᱜ ᱛᱷᱤᱨ ᱞᱟᱜᱤᱫ ᱟ", "inj nowa bug thir lagid a"],
    ["The code is working now", "ᱠᱚᱰ ᱱᱤᱛ ᱠᱟᱹᱢᱤ ᱢᱮᱱᱟᱜ ᱟ", "code nit kami menag a"],
    ["Can you review my code?", "ᱟᱢ ᱤᱧᱟᱜ ᱠᱚᱰ ᱧᱮᱞ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am injag code nyel dareyam ma?"],
    ["I will deploy it today", "ᱤᱧ ᱟᱡ ᱰᱤᱯᱞᱚᱭ ᱟ", "inj aj deploy a"],
    ["Work from home is convenient", "ᱚᱲᱟᱜ ᱠᱷᱚᱱ ᱠᱟᱹᱢᱤ ᱵᱷᱟᱞᱮ ᱢᱮᱱᱟᱜ ᱟ", "orag khon kami bhale menag a"],
    ["I have a team meeting at 3", "ᱤᱧᱟᱜ ᱯᱮ ᱵᱮᱞᱟ ᱴᱤᱢ ᱢᱤᱴᱤᱝ ᱢᱮᱱᱟᱜ ᱟ", "injag pe bela team meeting menag a"],
    ["The server is down", "ᱥᱟᱨᱵᱷᱟᱨ ᱵᱚᱱᱫ ᱢᱮᱱᱟᱜ ᱟ", "server bond menag a"],
    ["I am learning a new technology", "ᱤᱧ ᱱᱟᱣᱟ ᱴᱮᱠᱱᱚᱞᱚᱡᱤ ᱥᱮᱪᱮᱫ ᱟᱭᱟ", "inj nawa technology seced aya"],
    ["Let me check the database", "ᱤᱧ ᱰᱮᱴᱟᱵᱮᱥ ᱧᱮᱞ ᱟ", "inj database nyel a"],
    ["The client is happy with the work", "ᱠᱞᱟᱤᱱᱴ ᱠᱟᱹᱢᱤ ᱨᱟᱹᱥᱠᱟᱹ ᱢᱮᱱᱟᱜ ᱟ", "client kami raska menag a"],
    ["I need a laptop for coding", "ᱤᱧ ᱠᱚᱰᱤᱝ ᱞᱟᱜᱤᱫ ᱞᱮᱯᱴᱚᱯ ᱥᱟᱱᱟᱢ ᱟ", "inj coding lagid laptop sanam a"],
    ["What is your salary?", "ᱟᱢᱟᱜ ᱛᱚᱞᱟᱵ ᱚᱛᱚ?", "amag tolab oto?"],
    ["I love my job", "ᱤᱧ ᱤᱧᱟᱜ ᱠᱟᱹᱢᱤ ᱫᱩᱞᱟᱹᱲ ᱟᱭᱟ", "inj injag kami dular aya"]
]

# 629 - Grocery Shop
LESSONS[629] = [
    ["I need some rice", "ᱤᱧ ᱠᱟᱛᱮ ᱫᱟᱹᱠ ᱥᱟᱱᱟᱢ ᱟ", "inj kate dak sanam a"],
    ["Give me one kilo of sugar", "ᱢᱤᱫ ᱠᱤᱞᱚ ᱪᱤᱱᱤ ᱮᱢ ᱢᱮ", "mid kilo chini em me"],
    ["How much is the oil?", "ᱛᱮᱞ ᱚᱛᱚ ᱠᱟᱱᱟ?", "tel oto kana?"],
    ["Give me half kilo of salt", "ᱟᱹᱫᱷᱟ ᱠᱤᱞᱚ ᱱᱩᱱ ᱮᱢ ᱢᱮ", "adha kilo nun em me"],
    ["I need tea leaves", "ᱤᱧ ᱪᱟᱹ ᱯᱟᱹᱛᱤ ᱥᱟᱱᱟᱢ ᱟ", "inj cha pati sanam a"],
    ["Do you have turmeric?", "ᱟᱢᱟᱜ ᱦᱟᱞᱫᱤ ᱢᱮᱱᱟᱜ ᱟ?", "amag haldi menag a?"],
    ["Give me two packets of biscuits", "ᱵᱟᱨ ᱯᱮᱠᱮᱴ ᱵᱤᱥᱠᱤᱴ ᱮᱢ ᱢᱮ", "bar peket biskit em me"],
    ["How much is the total?", "ᱡᱚᱛᱚ ᱚᱛᱚ ᱦᱩᱭ ᱮᱱᱟ?", "joto oto huy ena?"],
    ["Do you have change?", "ᱟᱢᱟᱜ ᱵᱟᱠᱤ ᱴᱟᱠᱟ ᱢᱮᱱᱟᱜ ᱟ?", "amag baki taka menag a?"],
    ["Give me fresh milk", "ᱱᱟᱣᱟ ᱫᱩᱫᱷ ᱮᱢ ᱢᱮ", "nawa dudh em me"],
    ["I need soap and toothpaste", "ᱤᱧ ᱥᱟᱵᱩᱱ ᱟᱨ ᱢᱟᱡᱚᱱ ᱥᱟᱱᱟᱢ ᱟ", "inj sabun ar majon sanam a"],
    ["Is this fresh?", "ᱱᱚᱣᱟ ᱱᱟᱣᱟ ᱠᱟᱱᱟ?", "nowa nawa kana?"],
    ["Give me a bag", "ᱢᱤᱫ ᱛᱷᱮᱞᱤ ᱮᱢ ᱢᱮ", "mid theli em me"],
    ["I need matchsticks", "ᱤᱧ ᱫᱤᱭᱟᱥᱞᱟᱭ ᱥᱟᱱᱟᱢ ᱟ", "inj diyaslay sanam a"],
    ["Do you sell eggs?", "ᱟᱢ ᱵᱤᱸᱰᱤ ᱵᱮᱪᱟᱣ ᱟᱢ?", "am bindi becaw am?"],
    ["Give me one dozen eggs", "ᱢᱤᱫ ᱫᱚᱡᱚᱱ ᱵᱤᱸᱰᱤ ᱮᱢ ᱢᱮ", "mid dojon bindi em me"],
    ["Here is the money", "ᱱᱚᱣᱟ ᱴᱟᱠᱟ ᱤᱫᱤ ᱢᱮ", "nowa taka idi me"],
    ["Thank you, goodbye", "ᱥᱮᱨᱢᱟ, ᱡᱚᱦᱟᱨ", "serma, johar"]
]

# 630 - Doctor-Patient
LESSONS[630] = [
    ["Doctor, I am not feeling well", "ᱰᱚᱠᱴᱚᱨ, ᱤᱧ ᱵᱷᱟᱞᱮ ᱵᱟᱝ ᱢᱮᱱᱟᱜ ᱟ", "doktor, inj bhale bang menag a"],
    ["What is the problem?", "ᱪᱮᱫ ᱦᱩᱭ ᱮᱱᱟ?", "ced huy ena?"],
    ["I have a headache", "ᱤᱧᱟᱜ ᱛᱚᱞᱟ ᱰᱟᱦᱟ ᱢᱮᱱᱟᱜ ᱟ", "injag tola daha menag a"],
    ["I have a fever", "ᱤᱧᱟᱜ ᱡᱚᱨ ᱢᱮᱱᱟᱜ ᱟ", "injag jor menag a"],
    ["I have a stomach ache", "ᱤᱧᱟᱜ ᱞᱟᱜ ᱰᱟᱦᱟ ᱢᱮᱱᱟᱜ ᱟ", "injag lag daha menag a"],
    ["Since when are you sick?", "ᱟᱢ ᱚᱠᱟ ᱠᱷᱚᱱ ᱨᱚᱜ ᱢᱮᱱᱟᱜ ᱟ?", "am oka khon rog menag a?"],
    ["Since two days", "ᱵᱟᱨ ᱫᱤᱱ ᱠᱷᱚᱱ", "bar din khon"],
    ["Let me check your temperature", "ᱤᱧ ᱟᱢᱟᱜ ᱡᱚᱨ ᱧᱮᱞ ᱟ", "inj amag jor nyel a"],
    ["Take this medicine three times a day", "ᱱᱚᱣᱟ ᱟᱜ ᱫᱤᱱ ᱨᱮ ᱯᱮ ᱫᱷᱟᱣ ᱧᱩ ᱢᱮ", "nowa ag din re pe dhaw nyu me"],
    ["Drink plenty of water", "ᱟᱹᱰᱤ ᱫᱟᱜ ᱧᱩ ᱢᱮ", "adi dag nyu me"],
    ["Take rest for two days", "ᱵᱟᱨ ᱫᱤᱱ ᱥᱮᱨᱮᱧ ᱢᱮ", "bar din sereny me"],
    ["Do I need any tests?", "ᱤᱧ ᱴᱮᱥᱴ ᱞᱟᱜᱤᱫ ᱟ?", "inj test lagid a?"],
    ["Yes, get a blood test done", "ᱦᱮᱡ, ᱢᱟᱹᱭᱟᱢ ᱴᱮᱥᱴ ᱠᱮᱫ ᱢᱮ", "hej, mayam test ked me"],
    ["I have cough and cold", "ᱤᱧᱟᱜ ᱦᱩᱸᱥᱩᱢ ᱟᱨ ᱠᱷᱩᱥᱤ ᱢᱮᱱᱟᱜ ᱟ", "injag hunsum ar khusi menag a"],
    ["Avoid oily food", "ᱛᱮᱞ ᱡᱚᱢ ᱡᱷᱤᱡ ᱡᱚᱢ ᱢᱮ", "tel jom jhij jom me"],
    ["Come back after three days", "ᱯᱮ ᱫᱤᱱ ᱛᱟᱭᱚᱢ ᱟᱨ ᱦᱤᱡᱩᱜ ᱢᱮ", "pe din tayom ar hijug me"],
    ["You will get better soon", "ᱟᱢ ᱡᱟᱞᱫᱤ ᱵᱷᱟᱞᱮ ᱦᱩᱭ ᱟᱢ", "am jaldi bhale huy am"],
    ["Thank you doctor", "ᱥᱮᱨᱢᱟ ᱰᱚᱠᱴᱚᱨ", "serma doktor"]
]

# 631 - Teacher & Students
LESSONS[631] = [
    ["Good morning teacher", "ᱡᱚᱦᱟᱨ ᱯᱟᱲᱦᱟᱣᱮᱫ", "johar parhawed"],
    ["Good morning children", "ᱡᱚᱦᱟᱨ ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ", "johar gidra ko"],
    ["Open your books to page 10", "ᱟᱢᱟᱜ ᱯᱩᱛᱷᱤ ᱜᱮᱞ ᱯᱮᱡ ᱨᱮ ᱡᱷᱤᱡ ᱢᱮ", "amag puthi gel pej re jhij me"],
    ["Read this lesson carefully", "ᱱᱚᱣᱟ ᱯᱟᱲᱦᱟᱣ ᱵᱷᱟᱞᱮ ᱞᱮᱠᱟ ᱯᱟᱲᱦᱟᱣ ᱢᱮ", "nowa parhaw bhale leka parhaw me"],
    ["Who knows the answer?", "ᱚᱠᱚᱭ ᱡᱟᱣᱟᱵ ᱵᱟᱰᱟᱭ ᱮ?", "okoy jawab baday e?"],
    ["I know teacher!", "ᱤᱧ ᱵᱟᱰᱟᱭ ᱟ ᱯᱟᱲᱦᱟᱣᱮᱫ!", "inj baday a parhawed!"],
    ["Very good! Well done!", "ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ!", "adi bhale!"],
    ["Write this in your notebook", "ᱱᱚᱣᱟ ᱟᱢᱟᱜ ᱠᱚᱯᱤ ᱨᱮ ᱚᱞ ᱢᱮ", "nowa amag kopi re ol me"],
    ["Do you understand?", "ᱟᱢᱠᱚ ᱵᱩᱡᱷᱟᱹᱣ ᱮᱱᱟ?", "amko bujhaw ena?"],
    ["Yes teacher, we understand", "ᱦᱮᱡ ᱯᱟᱲᱦᱟᱣᱮᱫ, ᱟᱞᱮ ᱵᱩᱡᱷᱟᱹᱣ ᱮᱱᱟ", "hej parhawed, ale bujhaw ena"],
    ["Complete your homework", "ᱟᱢᱟᱜ ᱜᱟᱲ ᱠᱟᱹᱢᱤ ᱛᱮᱭᱟᱨ ᱢᱮ", "amag gar kami teyar me"],
    ["The exam is next week", "ᱟᱜᱤᱞᱟ ᱦᱟᱯᱛᱟ ᱨᱮ ᱯᱚᱨᱤᱠᱷᱟ ᱢᱮᱱᱟᱜ ᱟ", "agila hapta re porikha menag a"],
    ["Study well for the exam", "ᱯᱚᱨᱤᱠᱷᱟ ᱞᱟᱜᱤᱫ ᱵᱷᱟᱞᱮ ᱯᱟᱲᱦᱟᱣ ᱢᱮ", "porikha lagid bhale parhaw me"],
    ["Raise your hand to answer", "ᱡᱟᱣᱟᱵ ᱮᱢ ᱞᱟᱜᱤᱫ ᱛᱤᱸ ᱴᱷᱟᱲᱟᱣ ᱢᱮ", "jawab em lagid ting tharaw me"],
    ["Please be quiet", "ᱦᱮᱡ ᱛᱤᱥᱤᱧ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "hej tising taheny me"],
    ["The class is over", "ᱠᱞᱟᱥ ᱛᱮᱭᱟᱨ ᱮᱱᱟ", "class teyar ena"],
    ["Thank you teacher", "ᱥᱮᱨᱢᱟ ᱯᱟᱲᱦᱟᱣᱮᱫ", "serma parhawed"],
    ["See you tomorrow", "ᱜᱟᱯᱟ ᱧᱮᱞᱚᱜ ᱟᱞᱮ", "gapa nyelog ale"]
]

# 632 - Informal Phone Conversation
LESSONS[632] = [
    ["Hello, who is speaking?", "ᱡᱚᱦᱟᱨ, ᱚᱠᱚᱭ ᱨᱚᱲ ᱟᱢ?", "johar, okoy ror am?"],
    ["It's me, Soren", "ᱤᱧ ᱥᱚᱨᱮᱱ ᱨᱚᱲ ᱟᱭᱟ", "inj Soren ror aya"],
    ["How are you?", "ᱟᱢ ᱚᱠᱟ ᱠᱟᱱᱟ?", "am oka kana?"],
    ["I am good, what about you?", "ᱤᱧ ᱵᱷᱟᱞᱮ ᱢᱮᱱᱟᱜ ᱟ, ᱟᱢ?", "inj bhale menag a, am?"],
    ["Where are you now?", "ᱟᱢ ᱱᱤᱛ ᱚᱠᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟᱢ?", "am nit oka re menag am?"],
    ["I am at home", "ᱤᱧ ᱚᱲᱟᱜ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "inj orag re menag a"],
    ["Can we meet tomorrow?", "ᱟᱞᱮ ᱜᱟᱯᱟ ᱧᱮᱞᱚᱜ ᱫᱟᱲᱮ ᱟᱞᱮ?", "ale gapa nyelog dare ale?"],
    ["Yes, let's meet at the market", "ᱦᱮᱡ, ᱵᱟᱡᱟᱨ ᱨᱮ ᱧᱮᱞᱚᱜ ᱟᱞᱮ", "hej, bajar re nyelog ale"],
    ["What time should I come?", "ᱤᱧ ᱚᱛᱚ ᱵᱮᱞᱟ ᱦᱤᱡᱩᱜ ᱟ?", "inj oto bela hijug a?"],
    ["Come at 4 o'clock", "ᱯᱩᱱ ᱵᱮᱞᱟ ᱦᱤᱡᱩᱜ ᱢᱮ", "pun bela hijug me"],
    ["Okay, I will come", "ᱵᱷᱟᱞᱮ, ᱤᱧ ᱦᱤᱡᱩᱜ ᱟ", "bhale, inj hijug a"],
    ["Did you eat?", "ᱟᱢ ᱡᱚᱢ ᱮᱱᱟ?", "am jom ena?"],
    ["Not yet, I will eat now", "ᱟᱫᱚ ᱵᱟᱝ, ᱱᱤᱛ ᱡᱚᱢ ᱟ", "ado bang, nit jom a"],
    ["I called to tell you something", "ᱤᱧ ᱟᱢ ᱠᱮ ᱡᱟᱦᱟᱸ ᱨᱚᱲ ᱞᱟᱜᱤᱫ ᱠᱩᱞ ᱮᱱᱟ", "inj am ke jahang ror lagid kul ena"],
    ["Tell me, what is it?", "ᱨᱚᱲ ᱢᱮ, ᱪᱮᱫ ᱠᱟᱱᱟ?", "ror me, ced kana?"],
    ["I will tell you when we meet", "ᱟᱞᱮ ᱧᱮᱞᱚᱜ ᱵᱮᱞᱟ ᱨᱚᱲ ᱟ", "ale nyelog bela ror a"],
    ["Okay, bye then", "ᱵᱷᱟᱞᱮ, ᱡᱚᱦᱟᱨ ᱛᱟᱭᱚᱢ", "bhale, johar tayom"],
    ["Bye, take care", "ᱡᱚᱦᱟᱨ, ᱵᱷᱟᱞᱮ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "johar, bhale taheny me"]
]

# 633 - Vegetable Market
LESSONS[633] = [
    ["How much are the potatoes?", "ᱟᱹᱞᱩ ᱚᱛᱚ ᱠᱟᱱᱟ?", "alu oto kana?"],
    ["Give me two kilos of onion", "ᱵᱟᱨ ᱠᱤᱞᱚ ᱯᱤᱭᱟᱡ ᱮᱢ ᱢᱮ", "bar kilo piyaj em me"],
    ["These tomatoes are fresh", "ᱱᱚᱣᱟ ᱴᱟᱢᱟᱴᱚ ᱱᱟᱣᱟ ᱢᱮᱱᱟᱜ ᱟ", "nowa tamato nawa menag a"],
    ["Give me half kilo spinach", "ᱟᱹᱫᱷᱟ ᱠᱤᱞᱚ ᱯᱟᱞᱟᱠ ᱮᱢ ᱢᱮ", "adha kilo palak em me"],
    ["Do you have green chillies?", "ᱟᱢᱟᱜ ᱞᱚᱸᱠᱟ ᱢᱟᱹᱨᱥᱟᱹ ᱢᱮᱱᱟᱜ ᱟ?", "amag lonka marsa menag a?"],
    ["The brinjal is very nice", "ᱵᱟᱭᱜᱚᱱ ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ ᱢᱮᱱᱟᱜ ᱟ", "baygon adi bhale menag a"],
    ["Is this cabbage fresh?", "ᱱᱚᱣᱟ ᱵᱟᱸᱫᱷᱟ ᱠᱚᱯᱤ ᱱᱟᱣᱟ ᱠᱟᱱᱟ?", "nowa bandha kopi nawa kana?"],
    ["Give me some coriander leaves", "ᱠᱟᱛᱮ ᱫᱷᱟᱱᱤᱭᱟ ᱮᱢ ᱢᱮ", "kate dhaniya em me"],
    ["How much for all of this?", "ᱡᱚᱛᱚ ᱚᱛᱚ ᱦᱩᱭ ᱮᱱᱟ?", "joto oto huy ena?"],
    ["That is too expensive", "ᱚᱱᱟ ᱟᱹᱰᱤ ᱟᱛᱚ ᱢᱮᱱᱟᱜ ᱟ", "ona adi ato menag a"],
    ["Please give a good price", "ᱦᱮᱡ ᱵᱷᱟᱞᱮ ᱫᱟᱢ ᱮᱢ ᱢᱮ", "hej bhale dam em me"],
    ["Give me some ginger too", "ᱠᱟᱛᱮ ᱟᱹᱫᱟ ᱦᱚᱭ ᱮᱢ ᱢᱮ", "kate ada hoy em me"],
    ["I also need garlic", "ᱤᱧ ᱞᱟᱥᱩᱱ ᱦᱚᱭ ᱥᱟᱱᱟᱢ ᱟ", "inj lasun hoy sanam a"],
    ["Put it in the bag", "ᱛᱷᱮᱞᱤ ᱨᱮ ᱫᱚᱦᱚ ᱢᱮ", "theli re doho me"],
    ["Here is the money", "ᱱᱚᱣᱟ ᱴᱟᱠᱟ ᱤᱫᱤ ᱢᱮ", "nowa taka idi me"],
    ["Give me the change", "ᱵᱟᱠᱤ ᱴᱟᱠᱟ ᱮᱢ ᱢᱮ", "baki taka em me"],
    ["I will come again tomorrow", "ᱤᱧ ᱜᱟᱯᱟ ᱟᱨ ᱦᱤᱡᱩᱜ ᱟ", "inj gapa ar hijug a"],
    ["Thank you brother", "ᱥᱮᱨᱢᱟ ᱦᱟᱯᱲᱟᱢ", "serma hapram"]
]

# 634 - Bus Stop and in Bus
LESSONS[634] = [
    ["Which bus goes to Ranchi?", "ᱚᱠᱟ ᱵᱟᱥ ᱨᱟᱸᱪᱤ ᱥᱮᱱ ᱟ?", "oka bas Ranchi sen a?"],
    ["When does the next bus come?", "ᱟᱜᱤᱞᱟ ᱵᱟᱥ ᱚᱠᱟ ᱵᱮᱞᱟ ᱦᱤᱡᱩᱜ ᱟ?", "agila bas oka bela hijug a?"],
    ["One ticket to Dumka please", "ᱢᱤᱫ ᱴᱤᱠᱤᱴ ᱫᱩᱢᱠᱟ ᱞᱟᱜᱤᱫ", "mid tikit Dumka lagid"],
    ["How much is the fare?", "ᱴᱤᱠᱤᱴ ᱚᱛᱚ ᱠᱟᱱᱟ?", "tikit oto kana?"],
    ["Is this seat empty?", "ᱱᱚᱣᱟ ᱡᱟᱭᱜᱟ ᱠᱷᱟᱞᱤ ᱢᱮᱱᱟᱜ ᱟ?", "nowa jayga khali menag a?"],
    ["Yes, please sit", "ᱦᱮᱡ, ᱫᱩᱲᱩᱵ ᱢᱮ", "hej, durub me"],
    ["Where does this bus stop?", "ᱱᱚᱣᱟ ᱵᱟᱥ ᱚᱠᱟ ᱛᱷᱤᱨ ᱟ?", "nowa bas oka thir a?"],
    ["Please tell me when Dumka comes", "ᱦᱮᱡ ᱫᱩᱢᱠᱟ ᱦᱤᱡᱩᱜ ᱵᱮᱞᱟ ᱤᱧ ᱠᱮ ᱨᱚᱲ ᱢᱮ", "hej Dumka hijug bela inj ke ror me"],
    ["The bus is very crowded", "ᱵᱟᱥ ᱟᱹᱰᱤ ᱵᱷᱤᱲ ᱢᱮᱱᱟᱜ ᱟ", "bas adi bhir menag a"],
    ["How long is the journey?", "ᱥᱟᱯᱷᱟᱨ ᱚᱛᱚ ᱵᱮᱞᱟ ᱞᱟᱜᱤᱫ ᱟ?", "saphar oto bela lagid a?"],
    ["About three hours", "ᱯᱮ ᱜᱷᱚᱱᱴᱟ ᱞᱮᱠᱟ", "pe ghonta leka"],
    ["The bus has arrived", "ᱵᱟᱥ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "bas hijug ena"],
    ["Let's get on the bus", "ᱟᱞᱮ ᱵᱟᱥ ᱨᱮ ᱪᱟᱲᱷᱟᱣ ᱟᱞᱮ", "ale bas re charhaw ale"],
    ["Please move inside", "ᱦᱮᱡ ᱵᱷᱤᱛᱤᱨ ᱥᱮᱱ ᱢᱮ", "hej bhitir sen me"],
    ["Stop, I need to get off here", "ᱛᱷᱤᱨ ᱢᱮ, ᱤᱧ ᱱᱮᱛᱟᱨ ᱤᱡᱩᱜ ᱟ", "thir me, inj netar ijug a"],
    ["We have reached Dumka", "ᱟᱞᱮ ᱫᱩᱢᱠᱟ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "ale Dumka hijug ena"],
    ["The bus is late today", "ᱟᱡ ᱵᱟᱥ ᱞᱮᱴ ᱢᱮᱱᱟᱜ ᱟ", "aj bas let menag a"],
    ["Is there a direct bus?", "ᱥᱤᱫᱷᱟ ᱵᱟᱥ ᱢᱮᱱᱟᱜ ᱟ?", "sidha bas menag a?"]
]

# 635 - Asking Address
LESSONS[635] = [
    ["Excuse me, can you help me?", "ᱢᱟᱹᱧᱡᱷᱤ, ᱟᱢ ᱤᱧ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "manjhi, am inj ke sagay dareyam ma?"],
    ["I am looking for this address", "ᱤᱧ ᱱᱚᱣᱟ ᱴᱷᱤᱠᱟᱱᱟ ᱥᱮᱱᱫᱨᱟ ᱢᱮᱱᱟᱜ ᱟ", "inj nowa thikana sendra menag a"],
    ["Where is this place?", "ᱱᱚᱣᱟ ᱡᱟᱭᱜᱟ ᱚᱠᱟ ᱨᱮ?", "nowa jayga oka re?"],
    ["Go straight from here", "ᱱᱮᱛᱟᱨ ᱠᱷᱚᱱ ᱥᱤᱫᱷᱟ ᱥᱮᱱ ᱢᱮ", "netar khon sidha sen me"],
    ["Turn left at the crossing", "ᱢᱚᱲ ᱨᱮ ᱞᱮᱯᱷᱴ ᱢᱩᱲᱩᱜ ᱢᱮ", "mor re left murug me"],
    ["Turn right after the temple", "ᱛᱷᱟᱱ ᱛᱟᱭᱚᱢ ᱨᱟᱤᱴ ᱢᱩᱲᱩᱜ ᱢᱮ", "than tayom right murug me"],
    ["It is about 500 meters ahead", "ᱚᱱᱟ ᱢᱚᱬᱮ ᱥᱟᱹᱭ ᱢᱤᱴᱟᱨ ᱟᱜᱮ ᱢᱮᱱᱟᱜ ᱟ", "ona mone say mitar age menag a"],
    ["It is near the school", "ᱚᱱᱟ ᱥᱠᱩᱞ ᱱᱮᱰᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "ona skul neda re menag a"],
    ["Is it far from here?", "ᱱᱮᱛᱟᱨ ᱠᱷᱚᱱ ᱫᱩᱨ ᱢᱮᱱᱟᱜ ᱟ?", "netar khon dur menag a?"],
    ["No, it is very close", "ᱵᱟᱝ, ᱟᱹᱰᱤ ᱱᱮᱰᱟ ᱢᱮᱱᱟᱜ ᱟ", "bang, adi neda menag a"],
    ["You can walk there", "ᱟᱢ ᱥᱟᱞᱟᱜ ᱥᱮᱱ ᱫᱟᱲᱮᱭᱟᱢ", "am salag sen dareyam"],
    ["Ask anyone, they will tell you", "ᱡᱟᱦᱟᱸ ᱠᱮ ᱠᱩᱞᱤ ᱢᱮ, ᱩᱱᱠᱩ ᱨᱚᱲ ᱠᱚ", "jahang ke kuli me, unku ror ko"],
    ["The blue house on the right side", "ᱨᱟᱤᱴ ᱨᱮ ᱱᱤᱞ ᱚᱲᱟᱜ", "right re nil orag"],
    ["I can see it now", "ᱤᱧ ᱱᱤᱛ ᱧᱮᱞ ᱫᱟᱲᱮᱭᱟᱜ ᱟ", "inj nit nyel dareyag a"],
    ["Thank you for your help", "ᱥᱮᱨᱢᱟ ᱟᱢᱟᱜ ᱥᱟᱹᱜᱟᱹᱭ ᱞᱟᱜᱤᱫ", "serma amag sagay lagid"],
    ["You are welcome", "ᱦᱮᱡ ᱵᱟᱝ", "hej bang"],
    ["Can you write the address for me?", "ᱟᱢ ᱤᱧ ᱞᱟᱜᱤᱫ ᱴᱷᱤᱠᱟᱱᱟ ᱚᱞ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am inj lagid thikana ol dareyam ma?"],
    ["Take the first lane on the left", "ᱯᱟᱦᱤᱞᱟ ᱜᱟᱞᱤ ᱞᱮᱯᱷᱴ ᱨᱮ ᱤᱫᱤ ᱢᱮ", "pahila gali left re idi me"]
]

# 636 - I Love You / Proposing
LESSONS[636] = [
    ["I love you", "ᱤᱧ ᱟᱢ ᱠᱮ ᱫᱩᱞᱟᱹᱲ ᱟᱭᱟ", "inj am ke dular aya"],
    ["You are very beautiful", "ᱟᱢ ᱟᱹᱰᱤ ᱥᱚᱢᱵᱷᱟᱨ ᱢᱮᱱᱟᱜ ᱟ", "am adi sombhar menag a"],
    ["I think about you always", "ᱤᱧ ᱡᱟᱦᱟᱸᱱᱟᱜ ᱟᱢ ᱠᱮ ᱢᱚᱱᱮ ᱟᱭᱟ", "inj jahanag am ke mone aya"],
    ["Will you be my friend?", "ᱟᱢ ᱤᱧᱟᱜ ᱥᱟᱶᱛᱟ ᱦᱩᱭ ᱟᱢ?", "am injag sawta huy am?"],
    ["You make me happy", "ᱟᱢ ᱤᱧ ᱠᱮ ᱨᱟᱹᱥᱠᱟᱹ ᱮᱢ ᱟᱢ", "am inj ke raska em am"],
    ["I cannot live without you", "ᱤᱧ ᱟᱢ ᱵᱟᱜᱮ ᱵᱟᱝ ᱛᱟᱦᱮᱸᱱ ᱫᱟᱲᱮᱭᱟᱜ ᱟ", "inj am bage bang taheny dareyag a"],
    ["You are my life", "ᱟᱢ ᱤᱧᱟᱜ ᱡᱤᱣᱤ ᱠᱟᱱᱟ", "am injag jiwi kana"],
    ["I love you from my heart", "ᱤᱧ ᱤᱧᱟᱜ ᱢᱚᱱᱮ ᱠᱷᱚᱱ ᱟᱢ ᱠᱮ ᱫᱩᱞᱟᱹᱲ ᱟᱭᱟ", "inj injag mone khon am ke dular aya"],
    ["Will you marry me?", "ᱟᱢ ᱤᱧ ᱥᱟᱶ ᱵᱟᱯᱞᱟ ᱟᱢ?", "am inj saw bapla am?"],
    ["My heart beats for you", "ᱤᱧᱟᱜ ᱢᱚᱱᱮ ᱟᱢ ᱞᱟᱜᱤᱫ ᱫᱟᱹᱲ ᱟ", "injag mone am lagid dar a"],
    ["You are very special to me", "ᱟᱢ ᱤᱧ ᱞᱟᱜᱤᱫ ᱟᱹᱰᱤ ᱵᱤᱥᱮᱥ ᱠᱟᱱᱟ", "am inj lagid adi bises kana"],
    ["I miss you", "ᱤᱧ ᱟᱢ ᱠᱮ ᱩᱢ ᱟᱭᱟ", "inj am ke um aya"],
    ["Your smile is beautiful", "ᱟᱢᱟᱜ ᱞᱟᱸᱫᱟ ᱥᱚᱢᱵᱷᱟᱨ ᱢᱮᱱᱟᱜ ᱟ", "amag landa sombhar menag a"],
    ["I have loved you for a long time", "ᱤᱧ ᱟᱹᱰᱤ ᱫᱤᱱ ᱠᱷᱚᱱ ᱟᱢ ᱠᱮ ᱫᱩᱞᱟᱹᱲ ᱟᱭᱟ", "inj adi din khon am ke dular aya"],
    ["Do you love me?", "ᱟᱢ ᱤᱧ ᱠᱮ ᱫᱩᱞᱟᱹᱲ ᱟᱢ?", "am inj ke dular am?"],
    ["I will always be with you", "ᱤᱧ ᱡᱟᱦᱟᱸᱱᱟᱜ ᱟᱢ ᱥᱟᱶ ᱛᱟᱦᱮᱸᱱ ᱟ", "inj jahanag am saw taheny a"],
    ["You are the moon of my life", "ᱟᱢ ᱤᱧᱟᱜ ᱡᱤᱣᱤ ᱟᱜ ᱪᱟᱸᱫᱚ ᱠᱟᱱᱟ", "am injag jiwi ag chando kana"],
    ["I promise to love you forever", "ᱤᱧ ᱡᱟᱦᱟᱸᱱᱟᱜ ᱟᱢ ᱠᱮ ᱫᱩᱞᱟᱹᱲ ᱠᱟᱹᱛᱷᱟ ᱮᱢ ᱟ", "inj jahanag am ke dular katha em a"]
]

# 637 - Interview
LESSONS[637] = [
    ["Good morning, please have a seat", "ᱡᱚᱦᱟᱨ, ᱦᱮᱡ ᱫᱩᱲᱩᱵ ᱢᱮ", "johar, hej durub me"],
    ["Tell me about yourself", "ᱟᱢᱟᱜ ᱵᱤᱥᱚᱭ ᱨᱚᱲ ᱢᱮ", "amag bisoy ror me"],
    ["My name is Murmu", "ᱤᱧᱟᱜ ᱧᱩᱛᱩᱢ ᱢᱩᱨᱢᱩ", "injag nyutum Murmu"],
    ["What is your qualification?", "ᱟᱢᱟᱜ ᱯᱟᱲᱦᱟᱣ ᱪᱮᱫ ᱠᱟᱱᱟ?", "amag parhaw ced kana?"],
    ["I have completed my graduation", "ᱤᱧ ᱜᱨᱟᱡᱩᱮᱥᱚᱱ ᱛᱮᱭᱟᱨ ᱮᱱᱟ", "inj graduation teyar ena"],
    ["Do you have any experience?", "ᱟᱢᱟᱜ ᱟᱱᱩᱵᱷᱚᱵ ᱢᱮᱱᱟᱜ ᱟ?", "amag anubhob menag a?"],
    ["I have two years of experience", "ᱤᱧᱟᱜ ᱵᱟᱨ ᱥᱮᱨᱢᱟ ᱟᱱᱩᱵᱷᱚᱵ ᱢᱮᱱᱟᱜ ᱟ", "injag bar serma anubhob menag a"],
    ["Why do you want this job?", "ᱟᱢ ᱱᱚᱣᱟ ᱠᱟᱹᱢᱤ ᱪᱮᱫ ᱞᱟᱜᱤᱫ ᱥᱟᱱᱟᱢ ᱟᱢ?", "am nowa kami ced lagid sanam am?"],
    ["I want to grow in my career", "ᱤᱧ ᱤᱧᱟᱜ ᱠᱟᱹᱢᱤ ᱨᱮ ᱵᱚᱞᱚ ᱥᱟᱱᱟᱢ ᱟ", "inj injag kami re bolo sanam a"],
    ["What are your strengths?", "ᱟᱢᱟᱜ ᱡᱚᱨ ᱪᱮᱫ ᱠᱟᱱᱟ?", "amag jor ced kana?"],
    ["I am hardworking and honest", "ᱤᱧ ᱟᱹᱰᱤ ᱠᱟᱹᱢᱤ ᱟᱨ ᱥᱟᱹᱨᱤ ᱠᱟᱱᱟ", "inj adi kami ar sari kana"],
    ["Can you speak English?", "ᱟᱢ ᱤᱧᱜᱞᱤᱥ ᱨᱚᱲ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am Inglis ror dareyam ma?"],
    ["Yes, I can speak English and Santali", "ᱦᱮᱡ, ᱤᱧ ᱤᱧᱜᱞᱤᱥ ᱟᱨ ᱥᱟᱱᱛᱟᱲᱤ ᱨᱚᱲ ᱫᱟᱲᱮᱭᱟᱜ ᱟ", "hej, inj Inglis ar santari ror dareyag a"],
    ["When can you start?", "ᱟᱢ ᱚᱠᱟ ᱠᱷᱚᱱ ᱠᱟᱹᱢᱤ ᱪᱟᱞᱩ ᱫᱟᱲᱮᱭᱟᱢ?", "am oka khon kami chalu dareyam?"],
    ["I can start immediately", "ᱤᱧ ᱱᱤᱛ ᱠᱷᱚᱱ ᱪᱟᱞᱩ ᱫᱟᱲᱮᱭᱟᱜ ᱟ", "inj nit khon chalu dareyag a"],
    ["We will let you know the result", "ᱟᱞᱮ ᱟᱢ ᱠᱮ ᱨᱤᱡᱟᱞᱴ ᱨᱚᱲ ᱟᱞᱮ", "ale am ke result ror ale"],
    ["Thank you for the opportunity", "ᱥᱮᱨᱢᱟ ᱱᱚᱣᱟ ᱢᱚᱠᱟ ᱞᱟᱜᱤᱫ", "serma nowa moka lagid"],
    ["I hope to hear from you soon", "ᱤᱧ ᱡᱟᱞᱫᱤ ᱡᱟᱣᱟᱵ ᱧᱟᱢ ᱟᱥᱟ ᱟ", "inj jaldi jawab nyam asa a"]
]

# 638 - Housemaid
LESSONS[638] = [
    ["Please come on time every day", "ᱫᱤᱱ ᱫᱤᱱ ᱵᱮᱞᱟ ᱨᱮ ᱦᱤᱡᱩᱜ ᱢᱮ", "din din bela re hijug me"],
    ["Clean the floor first", "ᱟᱜᱮ ᱡᱟᱢᱤᱱ ᱥᱟᱯᱷᱟ ᱢᱮ", "age jamin sapha me"],
    ["Wash the dishes", "ᱵᱟᱥᱚᱱ ᱡᱩ ᱢᱮ", "bason ju me"],
    ["Please wash the clothes", "ᱦᱮᱡ ᱠᱟᱹᱯᱲᱟ ᱡᱩ ᱢᱮ", "hej kapra ju me"],
    ["Cook the rice", "ᱫᱟᱹᱠ ᱨᱟᱸᱰᱷᱟ ᱢᱮ", "dak randha me"],
    ["Sweep the courtyard", "ᱟᱸᱜᱟᱱ ᱡᱷᱟᱲᱩ ᱢᱮ", "angan jharu me"],
    ["Bring water from the well", "ᱤᱸᱫ ᱠᱷᱚᱱ ᱫᱟᱜ ᱟᱹᱜᱩ ᱢᱮ", "ind khon dag agu me"],
    ["Did you finish the work?", "ᱟᱢ ᱠᱟᱹᱢᱤ ᱛᱮᱭᱟᱨ ᱮᱱᱟ?", "am kami teyar ena?"],
    ["Yes, I have finished everything", "ᱦᱮᱡ, ᱤᱧ ᱡᱚᱛᱚ ᱛᱮᱭᱟᱨ ᱮᱱᱟ", "hej, inj joto teyar ena"],
    ["Please iron the clothes", "ᱦᱮᱡ ᱠᱟᱹᱯᱲᱟ ᱤᱥᱛᱤᱨᱤ ᱢᱮ", "hej kapra istiri me"],
    ["You may go now", "ᱟᱢ ᱱᱤᱛ ᱥᱮᱱ ᱫᱟᱲᱮᱭᱟᱢ", "am nit sen dareyam"],
    ["I will come tomorrow also", "ᱤᱧ ᱜᱟᱯᱟ ᱦᱚᱭ ᱦᱤᱡᱩᱜ ᱟ", "inj gapa hoy hijug a"],
    ["Take your salary", "ᱟᱢᱟᱜ ᱛᱚᱞᱟᱵ ᱤᱫᱤ ᱢᱮ", "amag tolab idi me"],
    ["Tomorrow is a holiday, don't come", "ᱜᱟᱯᱟ ᱪᱷᱩᱴᱴᱤ ᱢᱮᱱᱟᱜ ᱟ, ᱡᱷᱤᱡ ᱦᱤᱡᱩᱜ ᱢᱮ", "gapa chhutti menag a, jhij hijug me"],
    ["Clean the rooms properly", "ᱠᱚᱴᱷᱟ ᱠᱚ ᱵᱷᱟᱞᱮ ᱞᱮᱠᱟ ᱥᱟᱯᱷᱟ ᱢᱮ", "kotha ko bhale leka sapha me"],
    ["The kitchen needs cleaning", "ᱨᱟᱸᱰᱷᱟ ᱠᱚᱴᱷᱟ ᱥᱟᱯᱷᱟ ᱞᱟᱜᱤᱫ ᱟ", "randha kotha sapha lagid a"],
    ["Please water the plants", "ᱦᱮᱡ ᱫᱟᱨᱮ ᱠᱚ ᱨᱮ ᱫᱟᱜ ᱮᱢ ᱢᱮ", "hej dare ko re dag em me"],
    ["Thank you for your work", "ᱥᱮᱨᱢᱟ ᱟᱢᱟᱜ ᱠᱟᱹᱢᱤ ᱞᱟᱜᱤᱫ", "serma amag kami lagid"]
]

# 639 - Linking AADHAR to mobile
LESSONS[639] = [
    ["I want to link my AADHAR to mobile", "ᱤᱧ ᱤᱧᱟᱜ ᱟᱫᱷᱟᱨ ᱢᱚᱵᱟᱤᱞ ᱥᱟᱶ ᱡᱩᱲᱟᱣ ᱥᱟᱱᱟᱢ ᱟ", "inj injag aadhar mobile saw juraw sanam a"],
    ["Please come to the centre", "ᱦᱮᱡ ᱥᱮᱱᱴᱟᱨ ᱨᱮ ᱦᱤᱡᱩᱜ ᱢᱮ", "hej center re hijug me"],
    ["Bring your AADHAR card", "ᱟᱢᱟᱜ ᱟᱫᱷᱟᱨ ᱠᱟᱨᱰ ᱟᱹᱜᱩ ᱢᱮ", "amag aadhar card agu me"],
    ["What is your mobile number?", "ᱟᱢᱟᱜ ᱢᱚᱵᱟᱤᱞ ᱱᱚᱢᱵᱚᱨ ᱪᱮᱫ?", "amag mobile number ced?"],
    ["Give me your AADHAR number", "ᱟᱢᱟᱜ ᱟᱫᱷᱟᱨ ᱱᱚᱢᱵᱚᱨ ᱮᱢ ᱢᱮ", "amag aadhar number em me"],
    ["Place your finger on the scanner", "ᱟᱢᱟᱜ ᱟᱸᱜᱩᱞᱤ ᱥᱠᱮᱱᱟᱨ ᱨᱮ ᱫᱚᱦᱚ ᱢᱮ", "amag anguli scanner re doho me"],
    ["Your fingerprint was verified", "ᱟᱢᱟᱜ ᱟᱸᱜᱩᱞᱤ ᱪᱤᱱᱷᱟᱹ ᱵᱷᱮᱨᱤᱯᱷᱟᱭ ᱦᱩᱭ ᱮᱱᱟ", "amag anguli cinha verify huy ena"],
    ["You will receive an OTP", "ᱟᱢ ᱢᱤᱫ ᱚᱴᱤᱯᱤ ᱧᱟᱢ ᱟᱢ", "am mid OTP nyam am"],
    ["Please enter the OTP", "ᱦᱮᱡ ᱚᱴᱤᱯᱤ ᱫᱚᱦᱚ ᱢᱮ", "hej OTP doho me"],
    ["Your AADHAR is now linked", "ᱟᱢᱟᱜ ᱟᱫᱷᱟᱨ ᱱᱤᱛ ᱡᱩᱲᱟᱣ ᱦᱩᱭ ᱮᱱᱟ", "amag aadhar nit juraw huy ena"],
    ["Is there any charge for this?", "ᱱᱚᱣᱟ ᱞᱟᱜᱤᱫ ᱴᱟᱠᱟ ᱞᱟᱜᱤᱫ ᱟ?", "nowa lagid taka lagid a?"],
    ["No, it is free of cost", "ᱵᱟᱝ, ᱱᱚᱣᱟ ᱯᱷᱨᱤ ᱠᱟᱱᱟ", "bang, nowa free kana"],
    ["How long does it take?", "ᱚᱛᱚ ᱵᱮᱞᱟ ᱞᱟᱜᱤᱫ ᱟ?", "oto bela lagid a?"],
    ["It takes only five minutes", "ᱢᱚᱬᱮ ᱢᱤᱱᱤᱴ ᱞᱟᱜᱤᱫ ᱟ", "mone minit lagid a"],
    ["Keep this receipt safely", "ᱱᱚᱣᱟ ᱨᱮᱥᱤᱫ ᱵᱷᱟᱞᱮ ᱞᱮᱠᱟ ᱫᱚᱦᱚ ᱢᱮ", "nowa resid bhale leka doho me"],
    ["Thank you for your help", "ᱥᱮᱨᱢᱟ ᱟᱢᱟᱜ ᱥᱟᱹᱜᱟᱹᱭ ᱞᱟᱜᱤᱫ", "serma amag sagay lagid"],
    ["Now my mobile is linked to AADHAR", "ᱱᱤᱛ ᱤᱧᱟᱜ ᱢᱚᱵᱟᱤᱞ ᱟᱫᱷᱟᱨ ᱥᱟᱶ ᱡᱩᱲᱟᱣ ᱮᱱᱟ", "nit injag mobile aadhar saw juraw ena"],
    ["Do I need to come again?", "ᱤᱧ ᱟᱨ ᱦᱤᱡᱩᱜ ᱞᱟᱜᱤᱫ ᱟ?", "inj ar hijug lagid a?"]
]

# 640 - Mobile number to AADHAR
LESSONS[640] = [
    ["I need to update my mobile number", "ᱤᱧ ᱤᱧᱟᱜ ᱢᱚᱵᱟᱤᱞ ᱱᱚᱢᱵᱚᱨ ᱵᱚᱫᱚᱞ ᱥᱟᱱᱟᱢ ᱟ", "inj injag mobile number bodol sanam a"],
    ["My old number is not working", "ᱤᱧᱟᱜ ᱢᱟᱨᱟᱝ ᱱᱚᱢᱵᱚᱨ ᱵᱟᱝ ᱪᱟᱞᱟᱜ ᱟ", "injag marang number bang chalag a"],
    ["Please bring your AADHAR card", "ᱦᱮᱡ ᱟᱢᱟᱜ ᱟᱫᱷᱟᱨ ᱠᱟᱨᱰ ᱟᱹᱜᱩ ᱢᱮ", "hej amag aadhar card agu me"],
    ["Bring the new SIM card", "ᱱᱟᱣᱟ ᱥᱤᱢ ᱠᱟᱨᱰ ᱟᱹᱜᱩ ᱢᱮ", "nawa SIM card agu me"],
    ["Fill this form", "ᱱᱚᱣᱟ ᱯᱷᱚᱨᱢ ᱵᱷᱚᱨᱛᱤ ᱢᱮ", "nowa form bhorti me"],
    ["Write your new mobile number here", "ᱟᱢᱟᱜ ᱱᱟᱣᱟ ᱢᱚᱵᱟᱤᱞ ᱱᱚᱢᱵᱚᱨ ᱱᱮᱛᱟᱨ ᱚᱞ ᱢᱮ", "amag nawa mobile number netar ol me"],
    ["Place your thumb for verification", "ᱟᱸᱜᱩᱞᱤ ᱵᱷᱮᱨᱤᱯᱷᱟᱭ ᱞᱟᱜᱤᱫ ᱫᱚᱦᱚ ᱢᱮ", "anguli verify lagid doho me"],
    ["Your identity has been verified", "ᱟᱢᱟᱜ ᱯᱚᱦᱪᱟᱱ ᱵᱷᱮᱨᱤᱯᱷᱟᱭ ᱦᱩᱭ ᱮᱱᱟ", "amag pohchan verify huy ena"],
    ["An OTP will be sent to new number", "ᱱᱟᱣᱟ ᱱᱚᱢᱵᱚᱨ ᱨᱮ ᱚᱴᱤᱯᱤ ᱥᱮᱱ ᱟ", "nawa number re OTP sen a"],
    ["Enter the OTP here", "ᱱᱮᱛᱟᱨ ᱚᱴᱤᱯᱤ ᱫᱚᱦᱚ ᱢᱮ", "netar OTP doho me"],
    ["Your number has been updated", "ᱟᱢᱟᱜ ᱱᱚᱢᱵᱚᱨ ᱵᱚᱫᱚᱞ ᱦᱩᱭ ᱮᱱᱟ", "amag number bodol huy ena"],
    ["It will take 24 hours to activate", "ᱵᱟᱨ ᱫᱤᱱ ᱛᱟᱞᱟ ᱪᱟᱞᱩ ᱦᱩᱭ ᱟ", "bar din tala chalu huy a"],
    ["Keep the acknowledgment slip", "ᱨᱮᱥᱤᱫ ᱥᱟᱶ ᱫᱚᱦᱚ ᱢᱮ", "resid saw doho me"],
    ["Is there any problem with this process?", "ᱱᱚᱣᱟ ᱨᱮ ᱡᱟᱦᱟᱸ ᱢᱩᱥᱠᱤᱞ ᱢᱮᱱᱟᱜ ᱟ?", "nowa re jahang muskil menag a?"],
    ["No problem, it is a simple process", "ᱡᱟᱦᱟᱸ ᱢᱩᱥᱠᱤᱞ ᱵᱟᱝ, ᱥᱚᱡᱷᱟ ᱠᱟᱹᱢᱤ ᱠᱟᱱᱟ", "jahang muskil bang, sojha kami kana"],
    ["Can I do it online?", "ᱤᱧ ᱚᱱᱞᱟᱤᱱ ᱫᱟᱲᱮᱭᱟᱜ ᱢᱟ?", "inj online dareyag ma?"],
    ["Yes, you can do it from the website", "ᱦᱮᱡ, ᱟᱢ ᱣᱮᱵᱥᱟᱤᱴ ᱠᱷᱚᱱ ᱫᱟᱲᱮᱭᱟᱢ", "hej, am website khon dareyam"],
    ["Thank you for the information", "ᱥᱮᱨᱢᱟ ᱡᱟᱱᱠᱟᱨᱤ ᱞᱟᱜᱤᱫ", "serma jankari lagid"]
]

# 641 - Republic Day
LESSONS[641] = [
    ["Happy Republic Day!", "ᱜᱚᱱᱛᱚᱱᱛᱨᱟ ᱫᱤᱱ ᱨᱟᱹᱥᱠᱟᱹ ᱢᱟ!", "gontontantra din raska ma!"],
    ["Today is 26th January", "ᱟᱡ ᱵᱟᱨ ᱦᱤᱥᱤ ᱛᱩᱨᱩᱭ ᱡᱟᱱᱩᱣᱟᱨᱤ ᱠᱟᱱᱟ", "aj bar hisi turuy January kana"],
    ["We celebrate Republic Day every year", "ᱟᱞᱮ ᱥᱮᱨᱢᱟ ᱥᱮᱨᱢᱟ ᱜᱚᱱᱛᱚᱱᱛᱨᱟ ᱫᱤᱱ ᱢᱟᱱᱟᱣ ᱟᱞᱮ", "ale serma serma gontontantra din manaw ale"],
    ["The flag is hoisted in school", "ᱥᱠᱩᱞ ᱨᱮ ᱡᱷᱚᱸᱰᱟ ᱴᱷᱟᱲᱟᱣ ᱦᱩᱭ ᱟ", "skul re jhonda tharaw huy a"],
    ["Children sing the national anthem", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱨᱟᱥᱴᱨᱤᱭ ᱥᱮᱨᱮᱧ ᱥᱮᱨᱮᱧ ᱠᱚ", "gidra ko rastriya sereny sereny ko"],
    ["There is a parade in Delhi", "ᱫᱤᱞᱞᱤ ᱨᱮ ᱯᱨᱮᱰ ᱦᱩᱭ ᱟ", "Dilli re parade huy a"],
    ["Our Constitution was adopted on this day", "ᱱᱚᱣᱟ ᱫᱤᱱ ᱨᱮ ᱥᱚᱸᱵᱤᱫᱷᱟᱱ ᱪᱟᱞᱩ ᱦᱩᱭ ᱮᱱᱟ", "nowa din re sombidhan chalu huy ena"],
    ["We are proud of our country", "ᱟᱞᱮ ᱟᱞᱮᱭᱟᱜ ᱫᱤᱥᱚᱢ ᱞᱟᱜᱤᱫ ᱜᱚᱨᱵ ᱟᱞᱮ", "ale aleyag disom lagid gorb ale"],
    ["India became a republic in 1950", "ᱵᱷᱟᱨᱚᱛ ᱜᱚᱱᱛᱚᱱᱛᱨᱟ 1950 ᱨᱮ ᱦᱩᱭ ᱮᱱᱟ", "Bharat gontontantra 1950 re huy ena"],
    ["Sweets are distributed in school", "ᱥᱠᱩᱞ ᱨᱮ ᱡᱤᱞᱤᱯᱤ ᱮᱢ ᱦᱩᱭ ᱟ", "skul re jilipi em huy a"],
    ["We should love our country", "ᱟᱞᱮ ᱟᱞᱮᱭᱟᱜ ᱫᱤᱥᱚᱢ ᱫᱩᱞᱟᱹᱲ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "ale aleyag disom dular lagid ale"],
    ["Freedom fighters sacrificed for us", "ᱥᱚᱛᱟᱱᱛᱨᱟ ᱥᱮᱱᱟᱱᱤ ᱟᱞᱮ ᱞᱟᱜᱤᱫ ᱡᱤᱣᱤ ᱮᱢ ᱮᱱᱟ", "sotantra senani ale lagid jiwi em ena"],
    ["Students give cultural performances", "ᱪᱟᱴᱟᱨ ᱠᱚ ᱥᱟᱸᱥᱠᱨᱤᱛᱤᱠ ᱮᱱᱮᱡ ᱫᱮᱠᱷᱟᱣ ᱠᱚ", "chatar ko sanskritik enej dekhaw ko"],
    ["Let us salute our nation", "ᱟᱞᱮ ᱟᱞᱮᱭᱟᱜ ᱫᱤᱥᱚᱢ ᱠᱮ ᱡᱚᱦᱟᱨ ᱟᱞᱮ", "ale aleyag disom ke johar ale"],
    ["Unity in diversity is our strength", "ᱵᱷᱤᱱᱱᱚᱛᱟ ᱨᱮ ᱮᱠᱛᱟ ᱟᱞᱮᱭᱟᱜ ᱡᱚᱨ ᱠᱟᱱᱟ", "bhinnota re ekta aleyag jor kana"],
    ["Jai Hind! Long live India!", "ᱡᱟᱭ ᱦᱤᱱᱫ! ᱵᱷᱟᱨᱚᱛ ᱡᱟᱦᱟᱸᱱᱟᱜ ᱛᱟᱦᱮᱸᱱ ᱢᱟ!", "Jay Hind! Bharat jahanag taheny ma!"],
    ["We celebrate with pride and joy", "ᱟᱞᱮ ᱜᱚᱨᱵ ᱟᱨ ᱨᱟᱹᱥᱠᱟᱹ ᱥᱟᱶ ᱢᱟᱱᱟᱣ ᱟᱞᱮ", "ale gorb ar raska saw manaw ale"],
    ["May our country always prosper", "ᱟᱞᱮᱭᱟᱜ ᱫᱤᱥᱚᱢ ᱡᱟᱦᱟᱸᱱᱟᱜ ᱵᱷᱟᱞᱮ ᱛᱟᱦᱮᱸᱱ ᱢᱟ", "aleyag disom jahanag bhale taheny ma"]
]

for ch in d:
    if ch['id'] in LESSONS:
        ch['blocks'] = [{"type": "table", "columns": ["English", "Santali (Ol Chiki)", "Transliteration"], "rows": LESSONS[ch['id']]}]

open('data_santali.json', 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('Section 5a (620-641) populated - 22 lessons')
