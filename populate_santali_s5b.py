import json

d = json.load(open('data_santali.json', 'r', encoding='utf-8'))

LESSONS = {}

# 642 - In Bank
LESSONS[642] = [
    ["I want to open a bank account", "ᱤᱧ ᱵᱮᱸᱠ ᱠᱷᱟᱛᱟ ᱡᱷᱤᱡ ᱥᱟᱱᱟᱢ ᱟ", "inj bank khata jhij sanam a"],
    ["Please fill this form", "ᱦᱮᱡ ᱱᱚᱣᱟ ᱯᱷᱚᱨᱢ ᱵᱷᱚᱨᱛᱤ ᱢᱮ", "hej nowa form bhorti me"],
    ["I need a savings account", "ᱤᱧ ᱵᱟᱸᱪᱟᱣ ᱠᱷᱟᱛᱟ ᱥᱟᱱᱟᱢ ᱟ", "inj banchaw khata sanam a"],
    ["What documents are required?", "ᱚᱠᱟ ᱠᱟᱜᱚᱡ ᱞᱟᱜᱤᱫ ᱟ?", "oka kagoj lagid a?"],
    ["Bring your AADHAR and PAN card", "ᱟᱢᱟᱜ ᱟᱫᱷᱟᱨ ᱟᱨ ᱯᱮᱱ ᱠᱟᱨᱰ ᱟᱹᱜᱩ ᱢᱮ", "amag aadhar ar PAN card agu me"],
    ["I want to deposit money", "ᱤᱧ ᱴᱟᱠᱟ ᱡᱚᱢᱟ ᱥᱟᱱᱟᱢ ᱟ", "inj taka joma sanam a"],
    ["I want to withdraw money", "ᱤᱧ ᱴᱟᱠᱟ ᱠᱟᱲᱷᱟ ᱥᱟᱱᱟᱢ ᱟ", "inj taka karha sanam a"],
    ["Please check my balance", "ᱦᱮᱡ ᱤᱧᱟᱜ ᱵᱮᱞᱮᱱᱥ ᱧᱮᱞ ᱢᱮ", "hej injag balance nyel me"],
    ["I need a cheque book", "ᱤᱧ ᱪᱮᱠ ᱵᱩᱠ ᱥᱟᱱᱟᱢ ᱟ", "inj cheque book sanam a"],
    ["My ATM card is blocked", "ᱤᱧᱟᱜ ᱮᱴᱤᱮᱢ ᱠᱟᱨᱰ ᱵᱞᱚᱠ ᱦᱩᱭ ᱮᱱᱟ", "injag ATM card block huy ena"],
    ["I want to transfer money", "ᱤᱧ ᱴᱟᱠᱟ ᱴᱨᱟᱱᱥᱯᱷᱟᱨ ᱥᱟᱱᱟᱢ ᱟ", "inj taka transfer sanam a"],
    ["What is the interest rate?", "ᱵᱤᱭᱟᱡ ᱫᱚᱨ ᱚᱛᱚ?", "biyaj dor oto?"],
    ["I want a fixed deposit", "ᱤᱧ ᱯᱷᱤᱠᱥᱰ ᱰᱤᱯᱚᱡᱤᱴ ᱥᱟᱱᱟᱢ ᱟ", "inj fixed deposit sanam a"],
    ["Please update my passbook", "ᱦᱮᱡ ᱤᱧᱟᱜ ᱯᱟᱥᱵᱩᱠ ᱟᱯᱰᱮᱴ ᱢᱮ", "hej injag passbook update me"],
    ["Where is the ATM?", "ᱮᱴᱤᱮᱢ ᱚᱠᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ?", "ATM oka re menag a?"],
    ["I want a loan for my house", "ᱤᱧ ᱚᱲᱟᱜ ᱞᱟᱜᱤᱫ ᱞᱚᱱ ᱥᱟᱱᱟᱢ ᱟ", "inj orag lagid loan sanam a"],
    ["Sign here please", "ᱦᱮᱡ ᱱᱮᱛᱟᱨ ᱫᱥᱠᱷᱚᱛ ᱢᱮ", "hej netar daskhot me"],
    ["Thank you for your help", "ᱥᱮᱨᱢᱟ ᱟᱢᱟᱜ ᱥᱟᱹᱜᱟᱹᱭ ᱞᱟᱜᱤᱫ", "serma amag sagay lagid"]
]

# 643 - Enquiry about Temple Visit
LESSONS[643] = [
    ["Where is the nearest temple?", "ᱱᱮᱰᱟ ᱛᱷᱟᱱ ᱚᱠᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ?", "neda than oka re menag a?"],
    ["How do we get there?", "ᱟᱞᱮ ᱚᱱᱫᱮ ᱚᱠᱟ ᱞᱮᱠᱟ ᱥᱮᱱ ᱟᱞᱮ?", "ale onde oka leka sen ale?"],
    ["What time does the temple open?", "ᱛᱷᱟᱱ ᱚᱛᱚ ᱵᱮᱞᱟ ᱡᱷᱤᱡ ᱟ?", "than oto bela jhij a?"],
    ["The temple opens at 6 in the morning", "ᱛᱷᱟᱱ ᱥᱮᱛᱟᱜ ᱛᱩᱨᱩᱭ ᱵᱮᱞᱟ ᱡᱷᱤᱡ ᱟ", "than setag turuy bela jhij a"],
    ["Is photography allowed?", "ᱯᱷᱚᱴᱚ ᱤᱫᱤ ᱫᱟᱲᱮᱭᱟᱜ ᱢᱟ?", "photo idi dareyag ma?"],
    ["Yes, but not inside the sanctum", "ᱦᱮᱡ, ᱢᱮᱱᱫᱚ ᱵᱷᱤᱛᱤᱨ ᱨᱮ ᱵᱟᱝ", "hej, mendo bhitir re bang"],
    ["Remove your shoes before entering", "ᱵᱷᱤᱛᱤᱨ ᱟᱜᱮ ᱡᱩᱛᱟ ᱠᱷᱩᱞᱟᱹᱣ ᱢᱮ", "bhitir age juta khulaw me"],
    ["The temple is on top of the hill", "ᱛᱷᱟᱱ ᱵᱩᱨᱩ ᱪᱮᱛᱟᱱ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "than buru cetan re menag a"],
    ["How many steps are there?", "ᱚᱛᱚ ᱥᱤᱲᱤ ᱢᱮᱱᱟᱜ ᱟ?", "oto siri menag a?"],
    ["About 200 steps", "ᱵᱟᱨ ᱥᱟᱹᱭ ᱥᱤᱲᱤ ᱞᱮᱠᱟ", "bar say siri leka"],
    ["When is the festival here?", "ᱱᱮᱛᱟᱨ ᱯᱚᱨᱚᱵ ᱚᱠᱟ ᱵᱮᱞᱟ?", "netar porob oka bela?"],
    ["The big festival is during Sarhul", "ᱢᱟᱨᱟᱝ ᱯᱚᱨᱚᱵ ᱥᱟᱨᱦᱩᱞ ᱵᱮᱞᱟ ᱦᱩᱭ ᱟ", "marang porob Sarhul bela huy a"],
    ["Many people come to pray", "ᱟᱹᱰᱤ ᱦᱚᱲ ᱵᱤᱱᱛᱤ ᱞᱟᱜᱤᱫ ᱦᱤᱡᱩᱜ ᱠᱚ", "adi hor binti lagid hijug ko"],
    ["The temple is very beautiful", "ᱛᱷᱟᱱ ᱟᱹᱰᱤ ᱥᱚᱢᱵᱷᱟᱨ ᱢᱮᱱᱟᱜ ᱟ", "than adi sombhar menag a"],
    ["We should respect all sacred places", "ᱟᱞᱮ ᱡᱚᱛᱚ ᱛᱷᱟᱱ ᱢᱟᱱ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "ale joto than man lagid ale"],
    ["Is there water available there?", "ᱚᱱᱫᱮ ᱫᱟᱜ ᱢᱮᱱᱟᱜ ᱟ?", "onde dag menag a?"],
    ["Let us go early morning", "ᱟᱞᱮ ᱥᱮᱛᱟᱜ ᱟᱜᱮ ᱥᱮᱱ ᱟᱞᱮ", "ale setag age sen ale"],
    ["This visit was very peaceful", "ᱱᱚᱣᱟ ᱥᱮᱱᱫᱨᱟ ᱟᱹᱰᱤ ᱥᱟᱸᱛᱤ ᱛᱟᱦᱮᱸᱱ ᱟ", "nowa sendra adi santi taheny a"]
]

# 644 - With friend's parents at lunch table
LESSONS[644] = [
    ["Greetings uncle and aunty", "ᱡᱚᱦᱟᱨ ᱵᱟᱵᱟ ᱟᱨ ᱟᱭᱚ", "johar baba ar ayo"],
    ["Please sit down and eat", "ᱦᱮᱡ ᱫᱩᱲᱩᱵ ᱢᱮ ᱟᱨ ᱡᱚᱢ ᱢᱮ", "hej durub me ar jom me"],
    ["The food looks delicious", "ᱡᱚᱢ ᱟᱹᱰᱤ ᱫᱷᱟᱹᱨᱤ ᱧᱮᱞᱚᱜ ᱟ", "jom adi dhari nyelog a"],
    ["Thank you for inviting me", "ᱤᱧ ᱠᱮ ᱠᱩᱞ ᱞᱟᱜᱤᱫ ᱥᱮᱨᱢᱟ", "inj ke kul lagid serma"],
    ["Do you like rice or roti?", "ᱟᱢ ᱫᱟᱹᱠ ᱧᱟᱢ ᱟᱢ ᱟᱨ ᱨᱚᱴᱤ?", "am dak nyam am ar roti?"],
    ["I will have rice please", "ᱤᱧ ᱫᱟᱹᱠ ᱡᱚᱢ ᱟ", "inj dak jom a"],
    ["Please have some more dal", "ᱦᱮᱡ ᱟᱨ ᱠᱟᱛᱮ ᱫᱟᱹᱞ ᱤᱫᱤ ᱢᱮ", "hej ar kate dal idi me"],
    ["The vegetables are very tasty", "ᱥᱟᱜ ᱟᱹᱰᱤ ᱫᱷᱟᱹᱨᱤ ᱢᱮᱱᱟᱜ ᱟ", "sag adi dhari menag a"],
    ["Aunty cooks very well", "ᱟᱭᱚ ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ ᱨᱟᱸᱰᱷᱟ ᱮ", "ayo adi bhale randha e"],
    ["Have some more, don't be shy", "ᱟᱨ ᱠᱟᱛᱮ ᱤᱫᱤ ᱢᱮ, ᱞᱟᱡ ᱡᱷᱤᱡ ᱢᱮ", "ar kate idi me, laj jhij me"],
    ["No thank you, I am full", "ᱵᱟᱝ ᱥᱮᱨᱢᱟ, ᱤᱧᱟᱜ ᱞᱟᱜ ᱵᱷᱚᱨᱛᱤ ᱮᱱᱟ", "bang serma, injag lag bhorti ena"],
    ["Would you like water?", "ᱟᱢ ᱫᱟᱜ ᱧᱩ ᱟᱢ?", "am dag nyu am?"],
    ["Yes please, give me some water", "ᱦᱮᱡ, ᱠᱟᱛᱮ ᱫᱟᱜ ᱮᱢ ᱢᱮ", "hej, kate dag em me"],
    ["What grade is your son in?", "ᱟᱢᱟᱜ ᱦᱚᱯᱚᱱ ᱚᱠᱟ ᱠᱞᱟᱥ ᱨᱮ?", "amag hopon oka class re?"],
    ["He is in 10th grade", "ᱩᱱᱤ ᱜᱮᱞ ᱠᱞᱟᱥ ᱨᱮ ᱢᱮᱱᱟᱜ ᱮ", "uni gel class re menag e"],
    ["You have a lovely home", "ᱟᱢᱟᱜ ᱚᱲᱟᱜ ᱟᱹᱰᱤ ᱥᱚᱢᱵᱷᱟᱨ ᱢᱮᱱᱟᱜ ᱟ", "amag orag adi sombhar menag a"],
    ["Thank you for the wonderful meal", "ᱥᱮᱨᱢᱟ ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ ᱡᱚᱢ ᱞᱟᱜᱤᱫ", "serma adi bhale jom lagid"],
    ["Please come to our house too", "ᱟᱢᱠᱚ ᱦᱚᱭ ᱟᱞᱮᱭᱟᱜ ᱚᱲᱟᱜ ᱦᱤᱡᱩᱜ ᱢᱮ", "amko hoy aleyag orag hijug me"]
]

# 645 - Friend talking about football match
LESSONS[645] = [
    ["Did you watch the match yesterday?", "ᱟᱢ ᱜᱟᱞᱟ ᱢᱮᱪ ᱧᱮᱞ ᱮᱱᱟ?", "am gala match nyel ena?"],
    ["Yes! It was an amazing game", "ᱦᱮᱡ! ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ ᱠᱷᱮᱞ ᱛᱟᱦᱮᱸᱱ ᱟ", "hej! adi bhale khel taheny a"],
    ["Who scored the first goal?", "ᱯᱟᱦᱤᱞᱟ ᱜᱚᱞ ᱚᱠᱚᱭ ᱠᱮᱫ ᱮ?", "pahila goal okoy ked e?"],
    ["The striker scored a brilliant goal", "ᱥᱴᱨᱟᱤᱠᱟᱨ ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ ᱜᱚᱞ ᱠᱮᱫ ᱮ", "striker adi bhale goal ked e"],
    ["The goalkeeper saved many shots", "ᱜᱚᱞᱠᱤᱯᱟᱨ ᱟᱹᱰᱤ ᱥᱚᱴ ᱵᱟᱸᱪᱟᱣ ᱮᱱᱟ", "goalkeeper adi shot banchaw ena"],
    ["What was the final score?", "ᱞᱟᱥᱴ ᱥᱠᱚᱨ ᱚᱛᱚ ᱛᱟᱦᱮᱸᱱ ᱟ?", "last score oto taheny a?"],
    ["It was 2-1", "ᱵᱟᱨ-ᱢᱤᱫ ᱛᱟᱦᱮᱸᱱ ᱟ", "bar-mid taheny a"],
    ["Which team do you support?", "ᱟᱢ ᱚᱠᱟ ᱴᱤᱢ ᱫᱩᱞᱟᱹᱲ ᱟᱢ?", "am oka team dular am?"],
    ["I support Mohun Bagan", "ᱤᱧ ᱢᱚᱦᱩᱱ ᱵᱟᱜᱟᱱ ᱫᱩᱞᱟᱹᱲ ᱟᱭᱟ", "inj Mohun Bagan dular aya"],
    ["The referee gave a penalty", "ᱨᱮᱯᱷᱨᱤ ᱯᱮᱱᱟᱞᱴᱤ ᱮᱢ ᱮᱱᱟ", "referee penalty em ena"],
    ["That was a red card foul", "ᱚᱱᱟ ᱨᱮᱰ ᱠᱟᱨᱰ ᱯᱷᱟᱣᱞ ᱛᱟᱦᱮᱸᱱ ᱟ", "ona red card foul taheny a"],
    ["The crowd was very excited", "ᱡᱚᱛᱚ ᱦᱚᱲ ᱟᱹᱰᱤ ᱨᱟᱹᱥᱠᱟᱹ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "joto hor adi raska taheny ko"],
    ["Let's go watch the next match", "ᱟᱞᱮ ᱟᱜᱤᱞᱟ ᱢᱮᱪ ᱧᱮᱞ ᱥᱮᱱ ᱟᱞᱮ", "ale agila match nyel sen ale"],
    ["Football is my favourite sport", "ᱯᱷᱩᱴᱵᱚᱞ ᱤᱧᱟᱜ ᱫᱩᱞᱟᱹᱲ ᱠᱷᱮᱞ ᱠᱟᱱᱟ", "football injag dular khel kana"],
    ["I play football every evening", "ᱤᱧ ᱫᱤᱱ ᱫᱤᱱ ᱧᱤᱸᱫᱟ ᱯᱷᱩᱴᱵᱚᱞ ᱠᱷᱮᱞ ᱟᱭᱟ", "inj din din nyinda football khel aya"],
    ["The match was very thrilling", "ᱢᱮᱪ ᱟᱹᱰᱤ ᱨᱚᱢᱟᱸᱪᱠᱟᱨ ᱛᱟᱦᱮᱸᱱ ᱟ", "match adi romanchkar taheny a"],
    ["We should play more sports", "ᱟᱞᱮ ᱟᱹᱰᱤ ᱠᱷᱮᱞ ᱠᱷᱮᱞ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "ale adi khel khel lagid ale"],
    ["The stadium was full of fans", "ᱥᱴᱮᱰᱤᱭᱚᱢ ᱯᱷᱮᱱ ᱛᱮ ᱵᱷᱚᱨᱛᱤ ᱛᱟᱦᱮᱸᱱ ᱟ", "stadium fan te bhorti taheny a"]
]

# 646 - Friends plan to watch movie
LESSONS[646] = [
    ["Let's go watch a movie", "ᱟᱞᱮ ᱥᱤᱱᱮᱢᱟ ᱧᱮᱞ ᱥᱮᱱ ᱟᱞᱮ", "ale cinema nyel sen ale"],
    ["Which movie should we watch?", "ᱟᱞᱮ ᱚᱠᱟ ᱥᱤᱱᱮᱢᱟ ᱧᱮᱞ ᱟᱞᱮ?", "ale oka cinema nyel ale?"],
    ["The new action movie is good", "ᱱᱟᱣᱟ ᱮᱠᱥᱚᱱ ᱯᱷᱤᱞᱢ ᱵᱷᱟᱞᱮ ᱢᱮᱱᱟᱜ ᱟ", "nawa action film bhale menag a"],
    ["What time does the show start?", "ᱥᱚ ᱚᱛᱚ ᱵᱮᱞᱟ ᱪᱟᱞᱩ ᱟ?", "show oto bela chalu a?"],
    ["The show is at 6 in the evening", "ᱥᱚ ᱧᱤᱸᱫᱟ ᱛᱩᱨᱩᱭ ᱵᱮᱞᱟ ᱢᱮᱱᱟᱜ ᱟ", "show nyinda turuy bela menag a"],
    ["How much is the ticket?", "ᱴᱤᱠᱤᱴ ᱚᱛᱚ ᱠᱟᱱᱟ?", "tikit oto kana?"],
    ["The ticket is 200 rupees", "ᱴᱤᱠᱤᱴ ᱵᱟᱨ ᱥᱟᱹᱭ ᱴᱟᱠᱟ ᱠᱟᱱᱟ", "tikit bar say taka kana"],
    ["Let's book online", "ᱟᱞᱮ ᱚᱱᱞᱟᱤᱱ ᱵᱩᱠ ᱠᱮᱫ ᱟᱞᱮ", "ale online book ked ale"],
    ["I'll buy the popcorn", "ᱤᱧ ᱯᱚᱯᱠᱚᱨᱱ ᱧᱟᱢ ᱟ", "inj popcorn nyam a"],
    ["Let's sit in the front row", "ᱟᱞᱮ ᱟᱜᱮ ᱥᱟᱨᱤ ᱨᱮ ᱫᱩᱲᱩᱵ ᱟᱞᱮ", "ale age sari re durub ale"],
    ["The movie has good reviews", "ᱯᱷᱤᱞᱢ ᱟᱜ ᱵᱷᱟᱞᱮ ᱨᱤᱵᱷᱤᱩ ᱢᱮᱱᱟᱜ ᱟ", "film ag bhale review menag a"],
    ["I heard the songs are great", "ᱤᱧ ᱟᱭᱠᱟᱣ ᱮᱱᱟ ᱥᱮᱨᱮᱧ ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ", "inj aykaw ena sereny adi bhale"],
    ["Let's meet at the mall at 5", "ᱟᱞᱮ ᱢᱚᱞ ᱨᱮ ᱢᱚᱬᱮ ᱵᱮᱞᱟ ᱧᱮᱞᱚᱜ ᱟᱞᱮ", "ale mol re mone bela nyelog ale"],
    ["Don't be late", "ᱞᱮᱴ ᱡᱷᱤᱡ ᱦᱩᱭ ᱢᱮ", "let jhij huy me"],
    ["The movie was amazing!", "ᱯᱷᱤᱞᱢ ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ ᱛᱟᱦᱮᱸᱱ ᱟ!", "film adi bhale taheny a!"],
    ["The hero acted very well", "ᱦᱤᱨᱚ ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ ᱮᱠᱴᱤᱝ ᱠᱮᱫ ᱮ", "hero adi bhale acting ked e"],
    ["Let's come again next week", "ᱟᱞᱮ ᱟᱜᱤᱞᱟ ᱦᱟᱯᱛᱟ ᱟᱨ ᱦᱤᱡᱩᱜ ᱟᱞᱮ", "ale agila hapta ar hijug ale"],
    ["That was a fun evening", "ᱟᱹᱰᱤ ᱨᱟᱹᱥᱠᱟᱹ ᱧᱤᱸᱫᱟ ᱛᱟᱦᱮᱸᱱ ᱟ", "adi raska nyinda taheny a"]
]

# 647 - Friends talking about football world cup
LESSONS[647] = [
    ["The FIFA World Cup is starting soon", "ᱯᱷᱤᱯᱷᱟ ᱣᱚᱨᱞᱰ ᱠᱟᱯ ᱡᱟᱞᱫᱤ ᱪᱟᱞᱩ ᱟ", "FIFA World Cup jaldi chalu a"],
    ["Which team will win?", "ᱚᱠᱟ ᱴᱤᱢ ᱡᱤᱛ ᱟ?", "oka team jit a?"],
    ["I think Brazil will win", "ᱤᱧᱟᱜ ᱢᱚᱱᱮ ᱵᱨᱟᱡᱤᱞ ᱡᱤᱛ ᱟ", "injag mone Brazil jit a"],
    ["Argentina is also very strong", "ᱟᱨᱡᱮᱱᱴᱤᱱᱟ ᱦᱚᱭ ᱟᱹᱰᱤ ᱡᱚᱨ ᱢᱮᱱᱟᱜ ᱟ", "Argentina hoy adi jor menag a"],
    ["Messi is the best player", "ᱢᱮᱥᱤ ᱥᱟᱹᱨᱤ ᱠᱷᱚᱱ ᱵᱷᱟᱞᱮ ᱠᱷᱮᱞᱚᱣᱟᱲ ᱠᱟᱱᱟ", "Messi sari khon bhale khelowar kana"],
    ["The matches are at night", "ᱢᱮᱪ ᱧᱤᱸᱫᱟ ᱨᱮ ᱦᱩᱭ ᱟ", "match nyinda re huy a"],
    ["Let's watch it together", "ᱟᱞᱮ ᱥᱟᱶᱛᱮ ᱧᱮᱞ ᱟᱞᱮ", "ale sawte nyel ale"],
    ["The opening ceremony is grand", "ᱡᱷᱤᱡ ᱥᱢᱟᱨᱚᱦ ᱟᱹᱰᱤ ᱢᱟᱨᱟᱝ ᱛᱟᱦᱮᱸᱱ ᱟ", "jhij smaroh adi marang taheny a"],
    ["India has not qualified yet", "ᱵᱷᱟᱨᱚᱛ ᱟᱫᱚ ᱵᱟᱝ ᱪᱷᱟᱸᱴ ᱦᱩᱭ ᱮᱱᱟ", "Bharat ado bang chhant huy ena"],
    ["Maybe one day India will play", "ᱢᱤᱫ ᱫᱤᱱ ᱵᱷᱟᱨᱚᱛ ᱦᱚᱭ ᱠᱷᱮᱞ ᱟ", "mid din Bharat hoy khel a"],
    ["The World Cup comes every 4 years", "ᱣᱚᱨᱞᱰ ᱠᱟᱯ ᱯᱩᱱ ᱥᱮᱨᱢᱟ ᱛᱟᱭᱚᱢ ᱦᱤᱡᱩᱜ ᱟ", "World Cup pun serma tayom hijug a"],
    ["The final will be exciting", "ᱯᱷᱟᱤᱱᱟᱞ ᱟᱹᱰᱤ ᱨᱚᱢᱟᱸᱪᱠᱟᱨ ᱦᱩᱭ ᱟ", "final adi romanchkar huy a"],
    ["Many goals were scored today", "ᱟᱡ ᱟᱹᱰᱤ ᱜᱚᱞ ᱦᱩᱭ ᱮᱱᱟ", "aj adi goal huy ena"],
    ["The match went to penalty shootout", "ᱢᱮᱪ ᱯᱮᱱᱟᱞᱴᱤ ᱥᱩᱴᱟᱣᱩᱴ ᱨᱮ ᱥᱮᱱ ᱮᱱᱟ", "match penalty shootout re sen ena"],
    ["What a thrilling match it was!", "ᱚᱛᱚ ᱨᱚᱢᱟᱸᱪᱠᱟᱨ ᱢᱮᱪ ᱛᱟᱦᱮᱸᱱ ᱟ!", "oto romanchkar match taheny a!"],
    ["Football unites the whole world", "ᱯᱷᱩᱴᱵᱚᱞ ᱥᱟᱹᱨᱟᱹ ᱫᱩᱱᱤᱭᱟ ᱡᱩᱲᱟᱣ ᱟ", "football sara duniya juraw a"],
    ["Let's celebrate the victory", "ᱟᱞᱮ ᱡᱤᱛ ᱢᱟᱱᱟᱣ ᱟᱞᱮ", "ale jit manaw ale"],
    ["I cannot wait for the next match", "ᱤᱧ ᱟᱜᱤᱞᱟ ᱢᱮᱪ ᱞᱟᱜᱤᱫ ᱵᱟᱝ ᱡᱚᱜᱟᱹᱣ ᱫᱟᱲᱮᱭᱟᱜ ᱟ", "inj agila match lagid bang jogaw dareyag a"]
]

# 648 - Tour guide with tourists
LESSONS[648] = [
    ["Welcome to Jharkhand!", "ᱡᱷᱟᱨᱠᱷᱚᱸᱰ ᱨᱮ ᱥᱟᱹᱜᱟᱹᱣ ᱢᱟ!", "Jharkhand re sagaw ma!"],
    ["This is a very ancient place", "ᱱᱚᱣᱟ ᱟᱹᱰᱤ ᱢᱟᱨᱟᱝ ᱡᱟᱭᱜᱟ ᱠᱟᱱᱟ", "nowa adi marang jayga kana"],
    ["This temple is 500 years old", "ᱱᱚᱣᱟ ᱛᱷᱟᱱ ᱢᱚᱬᱮ ᱥᱟᱹᱭ ᱥᱮᱨᱢᱟ ᱢᱟᱨᱟᱝ ᱠᱟᱱᱟ", "nowa than mone say serma marang kana"],
    ["Please follow me", "ᱦᱮᱡ ᱤᱧ ᱥᱟᱶ ᱦᱤᱡᱩᱜ ᱢᱮ", "hej inj saw hijug me"],
    ["Do not touch the statues", "ᱢᱩᱨᱛᱤ ᱠᱚ ᱡᱷᱤᱡ ᱛᱟᱵᱚᱱ ᱢᱮ", "murti ko jhij tabon me"],
    ["You can take photos here", "ᱟᱢ ᱱᱮᱛᱟᱨ ᱯᱷᱚᱴᱚ ᱤᱫᱤ ᱫᱟᱲᱮᱭᱟᱢ", "am netar photo idi dareyam"],
    ["This waterfall is very beautiful", "ᱱᱚᱣᱟ ᱡᱷᱟᱨᱱᱟ ᱟᱹᱰᱤ ᱥᱚᱢᱵᱷᱟᱨ ᱢᱮᱱᱟᱜ ᱟ", "nowa jharna adi sombhar menag a"],
    ["The Santali tribe lives here", "ᱱᱮᱛᱟᱨ ᱥᱟᱱᱛᱟᱲ ᱦᱚᱲ ᱛᱟᱦᱮᱸᱱ ᱠᱚ", "netar Santar hor taheny ko"],
    ["They have rich culture and traditions", "ᱩᱱᱠᱩᱟᱜ ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ ᱥᱚᱸᱥᱠᱨᱤᱛᱤ ᱢᱮᱱᱟᱜ ᱟ", "unkuag adi bhale sanskruti menag a"],
    ["This forest has many wild animals", "ᱱᱚᱣᱟ ᱵᱤᱨ ᱨᱮ ᱟᱹᱰᱤ ᱵᱤᱨ ᱡᱟᱱᱟᱣᱟᱨ ᱢᱮᱱᱟᱜ ᱟ", "nowa bir re adi bir janawar menag a"],
    ["The view from here is amazing", "ᱱᱮᱛᱟᱨ ᱠᱷᱚᱱ ᱧᱮᱞᱚᱜ ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ", "netar khon nyelog adi bhale"],
    ["We will stop here for lunch", "ᱟᱞᱮ ᱱᱮᱛᱟᱨ ᱡᱚᱢ ᱞᱟᱜᱤᱫ ᱛᱷᱤᱨ ᱟᱞᱮ", "ale netar jom lagid thir ale"],
    ["Do you have any questions?", "ᱟᱢᱟᱜ ᱡᱟᱦᱟᱸ ᱠᱩᱞᱤ ᱢᱮᱱᱟᱜ ᱟ?", "amag jahang kuli menag a?"],
    ["The bus will leave at 4 pm", "ᱵᱟᱥ ᱯᱩᱱ ᱵᱮᱞᱟ ᱥᱮᱱ ᱟ", "bas pun bela sen a"],
    ["Please be on time", "ᱦᱮᱡ ᱵᱮᱞᱟ ᱨᱮ ᱦᱤᱡᱩᱜ ᱢᱮ", "hej bela re hijug me"],
    ["I hope you enjoyed the tour", "ᱤᱧᱟᱜ ᱟᱥᱟ ᱟᱢᱟᱜ ᱨᱟᱹᱥᱠᱟᱹ ᱮᱱᱟ", "injag asa amag raska ena"],
    ["Thank you for visiting", "ᱥᱮᱨᱢᱟ ᱦᱤᱡᱩᱜ ᱞᱟᱜᱤᱫ", "serma hijug lagid"],
    ["Please come again!", "ᱦᱮᱡ ᱟᱨ ᱦᱤᱡᱩᱜ ᱢᱮ!", "hej ar hijug me!"]
]

# 649 - Language Proficiency Test for banks
LESSONS[649] = [
    ["I am here for the language test", "ᱤᱧ ᱯᱟᱹᱨᱥᱤ ᱴᱮᱥᱴ ᱞᱟᱜᱤᱫ ᱦᱤᱡᱩᱜ ᱮᱱᱟ", "inj parsi test lagid hijug ena"],
    ["Please show your admit card", "ᱦᱮᱡ ᱟᱢᱟᱜ ᱮᱰᱢᱤᱴ ᱠᱟᱨᱰ ᱫᱮᱠᱷᱟᱣ ᱢᱮ", "hej amag admit card dekhaw me"],
    ["The test is in Santali language", "ᱴᱮᱥᱴ ᱥᱟᱱᱛᱟᱲᱤ ᱯᱟᱹᱨᱥᱤ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "test santari parsi re menag a"],
    ["Can you read Ol Chiki script?", "ᱟᱢ ᱚᱞ ᱪᱤᱠᱤ ᱯᱟᱲᱦᱟᱣ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am Ol Chiki parhaw dareyam ma?"],
    ["Yes, I can read and write Santali", "ᱦᱮᱡ, ᱤᱧ ᱥᱟᱱᱛᱟᱲᱤ ᱯᱟᱲᱦᱟᱣ ᱟᱨ ᱚᱞ ᱫᱟᱲᱮᱭᱟᱜ ᱟ", "hej, inj santari parhaw ar ol dareyag a"],
    ["Write a letter in Santali", "ᱥᱟᱱᱛᱟᱲᱤ ᱨᱮ ᱢᱤᱫ ᱪᱤᱴᱷᱤ ᱚᱞ ᱢᱮ", "santari re mid chithi ol me"],
    ["Translate this sentence to Santali", "ᱱᱚᱣᱟ ᱠᱟᱹᱛᱷᱟ ᱥᱟᱱᱛᱟᱲᱤ ᱨᱮ ᱩᱞᱴᱟᱣ ᱢᱮ", "nowa katha santari re ultaw me"],
    ["Read this paragraph aloud", "ᱱᱚᱣᱟ ᱯᱮᱨᱟ ᱡᱚᱨ ᱨᱮ ᱯᱟᱲᱦᱟᱣ ᱢᱮ", "nowa para jor re parhaw me"],
    ["The test has reading and writing", "ᱴᱮᱥᱴ ᱨᱮ ᱯᱟᱲᱦᱟᱣ ᱟᱨ ᱚᱞ ᱢᱮᱱᱟᱜ ᱟ", "test re parhaw ar ol menag a"],
    ["You have one hour to complete", "ᱟᱢᱟᱜ ᱢᱤᱫ ᱜᱷᱚᱱᱴᱟ ᱢᱮᱱᱟᱜ ᱟ", "amag mid ghonta menag a"],
    ["Fill in the blanks", "ᱠᱷᱟᱞᱤ ᱡᱟᱭᱜᱟ ᱵᱷᱚᱨᱛᱤ ᱢᱮ", "khali jayga bhorti me"],
    ["Choose the correct answer", "ᱥᱟᱹᱨᱤ ᱡᱟᱣᱟᱵ ᱪᱷᱟᱸᱴ ᱢᱮ", "sari jawab chhant me"],
    ["This is a speaking test", "ᱱᱚᱣᱟ ᱨᱚᱲ ᱴᱮᱥᱴ ᱠᱟᱱᱟ", "nowa ror test kana"],
    ["Speak clearly and slowly", "ᱥᱚᱯᱷᱟ ᱟᱨ ᱟᱹᱭᱥᱛᱮ ᱨᱚᱲ ᱢᱮ", "sopha ar ayste ror me"],
    ["Your test is complete", "ᱟᱢᱟᱜ ᱴᱮᱥᱴ ᱛᱮᱭᱟᱨ ᱮᱱᱟ", "amag test teyar ena"],
    ["The results will come in a week", "ᱨᱤᱡᱟᱞᱴ ᱢᱤᱫ ᱦᱟᱯᱛᱟ ᱨᱮ ᱦᱤᱡᱩᱜ ᱟ", "result mid hapta re hijug a"],
    ["I passed the language test!", "ᱤᱧ ᱯᱟᱹᱨᱥᱤ ᱴᱮᱥᱴ ᱯᱟᱥ ᱮᱱᱟ!", "inj parsi test pass ena!"],
    ["Language skills are important for banking", "ᱵᱮᱸᱠ ᱞᱟᱜᱤᱫ ᱯᱟᱹᱨᱥᱤ ᱜᱤᱭᱟᱱ ᱫᱚᱨᱠᱟᱨ", "bank lagid parsi giyan dorkar"]
]

# 650 - About food, lunch, meal
LESSONS[650] = [
    ["I am hungry", "ᱤᱧᱟᱜ ᱞᱚᱠ ᱢᱮᱱᱟᱜ ᱟ", "injag lok menag a"],
    ["What will you eat today?", "ᱟᱢ ᱟᱡ ᱪᱮᱫ ᱡᱚᱢ ᱟᱢ?", "am aj ced jom am?"],
    ["I will eat rice and dal", "ᱤᱧ ᱫᱟᱹᱠ ᱟᱨ ᱫᱟᱹᱞ ᱡᱚᱢ ᱟ", "inj dak ar dal jom a"],
    ["The food is very delicious", "ᱡᱚᱢ ᱟᱹᱰᱤ ᱫᱷᱟᱹᱨᱤ ᱢᱮᱱᱟᱜ ᱟ", "jom adi dhari menag a"],
    ["I like fish curry", "ᱤᱧ ᱦᱟᱠᱩ ᱡᱷᱚᱞ ᱫᱩᱞᱟᱹᱲ ᱟᱭᱟ", "inj haku jhol dular aya"],
    ["Mother cooks very well", "ᱟᱭᱚ ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ ᱨᱟᱸᱰᱷᱟ ᱮ", "ayo adi bhale randha e"],
    ["Shall we eat together?", "ᱟᱞᱮ ᱥᱟᱶᱛᱮ ᱡᱚᱢ ᱟᱞᱮ?", "ale sawte jom ale?"],
    ["Wash your hands before eating", "ᱡᱚᱢ ᱟᱜᱮ ᱛᱤᱸ ᱡᱩ ᱢᱮ", "jom age ting ju me"],
    ["The chicken curry is spicy", "ᱥᱤᱢ ᱡᱷᱚᱞ ᱢᱟᱹᱨᱥᱟᱹ ᱢᱮᱱᱟᱜ ᱟ", "sim jhol marsa menag a"],
    ["Give me some more rice", "ᱤᱧ ᱠᱮ ᱟᱨ ᱠᱟᱛᱮ ᱫᱟᱹᱠ ᱮᱢ ᱢᱮ", "inj ke ar kate dak em me"],
    ["I don't eat meat", "ᱤᱧ ᱡᱤᱞ ᱵᱟᱝ ᱡᱚᱢ ᱟ", "inj jil bang jom a"],
    ["The vegetables are fresh", "ᱥᱟᱜ ᱱᱟᱣᱟ ᱢᱮᱱᱟᱜ ᱟ", "sag nawa menag a"],
    ["I want some pickle", "ᱤᱧ ᱠᱟᱛᱮ ᱟᱸᱵᱤᱞ ᱥᱟᱱᱟᱢ ᱟ", "inj kate ambil sanam a"],
    ["Drink water after eating", "ᱡᱚᱢ ᱛᱟᱭᱚᱢ ᱫᱟᱜ ᱧᱩ ᱢᱮ", "jom tayom dag nyu me"],
    ["The rice is not cooked properly", "ᱫᱟᱹᱠ ᱵᱷᱟᱞᱮ ᱵᱟᱝ ᱨᱟᱸᱰᱷᱟ ᱮᱱᱟ", "dak bhale bang randha ena"],
    ["I am full now", "ᱤᱧᱟᱜ ᱞᱟᱜ ᱵᱷᱚᱨᱛᱤ ᱮᱱᱟ", "injag lag bhorti ena"],
    ["Let's have tea after lunch", "ᱡᱚᱢ ᱛᱟᱭᱚᱢ ᱟᱞᱮ ᱪᱟᱹ ᱧᱩ ᱟᱞᱮ", "jom tayom ale cha nyu ale"],
    ["I will cook dinner tonight", "ᱤᱧ ᱟᱡ ᱧᱤᱸᱫᱟ ᱨᱟᱸᱰᱷᱟ ᱟ", "inj aj nyinda randha a"]
]

# 651 - About hobby class
LESSONS[651] = [
    ["What is your hobby?", "ᱟᱢᱟᱜ ᱥᱚᱠ ᱪᱮᱫ ᱠᱟᱱᱟ?", "amag sok ced kana?"],
    ["I like painting", "ᱤᱧ ᱪᱤᱛᱟᱨ ᱫᱩᱞᱟᱹᱲ ᱟᱭᱟ", "inj chitar dular aya"],
    ["I joined a music class", "ᱤᱧ ᱥᱮᱨᱮᱧ ᱠᱞᱟᱥ ᱨᱮ ᱧᱩᱛᱩᱢ ᱚᱞ ᱮᱱᱟ", "inj sereny class re nyutum ol ena"],
    ["Dancing is fun", "ᱮᱱᱮᱡ ᱟᱹᱰᱤ ᱨᱟᱹᱥᱠᱟᱹ ᱠᱟᱱᱟ", "enej adi raska kana"],
    ["I play guitar in my free time", "ᱤᱧ ᱠᱷᱟᱞᱤ ᱵᱮᱞᱟ ᱨᱮ ᱜᱤᱴᱟᱨ ᱵᱟᱡᱟᱣ ᱟᱭᱟ", "inj khali bela re guitar bajaw aya"],
    ["She teaches classical dance", "ᱩᱱᱤ ᱠᱞᱟᱥᱤᱠᱟᱞ ᱮᱱᱮᱡ ᱥᱤᱠᱷᱟᱣ ᱮ", "uni classical enej sikhaw e"],
    ["I want to learn singing", "ᱤᱧ ᱥᱮᱨᱮᱧ ᱥᱮᱪᱮᱫ ᱥᱟᱱᱟᱢ ᱟ", "inj sereny seced sanam a"],
    ["The class is every Saturday", "ᱠᱞᱟᱥ ᱥᱟᱱᱤᱪᱚᱨ ᱫᱤᱱ ᱦᱩᱭ ᱟ", "class sanichor din huy a"],
    ["I love reading books", "ᱤᱧ ᱯᱩᱛᱷᱤ ᱯᱟᱲᱦᱟᱣ ᱫᱩᱞᱟᱹᱲ ᱟᱭᱟ", "inj puthi parhaw dular aya"],
    ["Gardening is relaxing", "ᱵᱟᱜᱟᱱ ᱠᱟᱹᱢᱤ ᱟᱹᱰᱤ ᱥᱟᱸᱛᱤ ᱮᱢ ᱟ", "bagan kami adi santi em a"],
    ["I make crafts from bamboo", "ᱤᱧ ᱢᱟᱸ ᱠᱷᱚᱱ ᱦᱟᱛᱤᱭᱟᱨ ᱛᱮᱭᱟᱨ ᱟᱭᱟ", "inj mang khon hatiyar teyar aya"],
    ["Photography is my passion", "ᱯᱷᱚᱴᱚᱜᱨᱟᱯᱷᱤ ᱤᱧᱟᱜ ᱟᱹᱰᱤ ᱫᱩᱞᱟᱹᱲ ᱠᱟᱱᱟ", "photography injag adi dular kana"],
    ["I swim every morning", "ᱤᱧ ᱫᱤᱱ ᱫᱤᱱ ᱥᱮᱛᱟᱜ ᱫᱟᱜ ᱠᱩ ᱟᱭᱟ", "inj din din setag dag ku aya"],
    ["Cooking new dishes is exciting", "ᱱᱟᱣᱟ ᱡᱚᱢ ᱨᱟᱸᱰᱷᱟ ᱨᱟᱹᱥᱠᱟᱹ ᱠᱟᱱᱟ", "nawa jom randha raska kana"],
    ["I collect old coins", "ᱤᱧ ᱢᱟᱨᱟᱝ ᱥᱤᱠᱟ ᱡᱚᱜᱟᱹᱣ ᱟᱭᱟ", "inj marang sika jogaw aya"],
    ["Everyone should have a hobby", "ᱡᱚᱛᱚ ᱦᱚᱲ ᱟᱜ ᱢᱤᱫ ᱥᱚᱠ ᱛᱟᱦᱮᱸᱱ ᱞᱟᱜᱤᱫ ᱟ", "joto hor ag mid sok taheny lagid a"],
    ["Hobbies reduce stress", "ᱥᱚᱠ ᱪᱤᱱᱛᱟ ᱠᱚᱢ ᱮᱢ ᱟ", "sok chinta kom em a"],
    ["I enjoy my hobby class very much", "ᱤᱧ ᱤᱧᱟᱜ ᱥᱚᱠ ᱠᱞᱟᱥ ᱟᱹᱰᱤ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "inj injag sok class adi raska a"]
]

# 652 - Frequently used sentences miscellaneous
LESSONS[652] = [
    ["Please help me", "ᱦᱮᱡ ᱤᱧ ᱠᱮ ᱥᱟᱹᱜᱟᱹᱭ ᱢᱮ", "hej inj ke sagay me"],
    ["I don't understand", "ᱤᱧ ᱵᱟᱝ ᱵᱩᱡᱷᱟᱹᱣ ᱟ", "inj bang bujhaw a"],
    ["Please say that again", "ᱦᱮᱡ ᱟᱨ ᱢᱤᱫ ᱫᱷᱟᱣ ᱨᱚᱲ ᱢᱮ", "hej ar mid dhaw ror me"],
    ["I am sorry", "ᱢᱟᱹᱧᱡᱷᱤ", "manjhi"],
    ["It's okay, no problem", "ᱵᱷᱟᱞᱮ, ᱡᱟᱦᱟᱸ ᱢᱩᱥᱠᱤᱞ ᱵᱟᱝ", "bhale, jahang muskil bang"],
    ["Thank you very much", "ᱟᱹᱰᱤ ᱥᱮᱨᱢᱟ ᱢᱟ", "adi serma ma"],
    ["What is the price?", "ᱫᱟᱢ ᱚᱛᱚ?", "dam oto?"],
    ["I need water", "ᱤᱧ ᱫᱟᱜ ᱥᱟᱱᱟᱢ ᱟ", "inj dag sanam a"],
    ["Where is the bathroom?", "ᱵᱟᱛᱷᱨᱩᱢ ᱚᱠᱟ ᱨᱮ?", "bathroom oka re?"],
    ["I am lost", "ᱤᱧ ᱦᱤᱛᱟᱹᱣ ᱮᱱᱟ", "inj hitaw ena"],
    ["Can you speak slowly?", "ᱟᱢ ᱟᱹᱭᱥᱛᱮ ᱨᱚᱲ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am ayste ror dareyam ma?"],
    ["I am a student", "ᱤᱧ ᱢᱤᱫ ᱪᱟᱴᱟᱨ ᱠᱟᱱᱟ", "inj mid chatar kana"],
    ["I am learning Santali", "ᱤᱧ ᱥᱟᱱᱛᱟᱲᱤ ᱥᱮᱪᱮᱫ ᱟᱭᱟ", "inj santari seced aya"],
    ["This is beautiful", "ᱱᱚᱣᱟ ᱥᱚᱢᱵᱷᱟᱨ ᱢᱮᱱᱟᱜ ᱟ", "nowa sombhar menag a"],
    ["Be careful", "ᱥᱟᱵᱫᱷᱟᱱ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "sabdhan taheny me"],
    ["Come quickly", "ᱡᱟᱞᱫᱤ ᱦᱤᱡᱩᱜ ᱢᱮ", "jaldi hijug me"],
    ["I will try", "ᱤᱧ ᱪᱮᱥᱴᱟ ᱟ", "inj cesta a"],
    ["God bless you", "ᱢᱟᱨᱟᱝ ᱵᱩᱨᱩ ᱵᱷᱟᱞᱮ ᱮᱢ ᱟᱢ ᱢᱟ", "Marang Buru bhale em am ma"]
]

# 653 - Frequently used sentences miscellaneous part 2
LESSONS[653] = [
    ["What happened?", "ᱪᱮᱫ ᱦᱩᱭ ᱮᱱᱟ?", "ced huy ena?"],
    ["Nothing happened", "ᱡᱟᱦᱟᱸ ᱵᱟᱝ ᱦᱩᱭ ᱮᱱᱟ", "jahang bang huy ena"],
    ["I am happy today", "ᱤᱧ ᱟᱡ ᱨᱟᱹᱥᱠᱟᱹ ᱢᱮᱱᱟᱜ ᱟ", "inj aj raska menag a"],
    ["I am tired", "ᱤᱧᱟᱜ ᱚᱲᱟᱜ ᱰᱟᱠᱟ ᱮᱱᱟ", "injag orag daka ena"],
    ["Let's go together", "ᱟᱞᱮ ᱥᱟᱶᱛᱮ ᱥᱮᱱ ᱟᱞᱮ", "ale sawte sen ale"],
    ["Don't worry", "ᱪᱤᱱᱛᱟ ᱡᱷᱤᱡ ᱢᱮ", "chinta jhij me"],
    ["I will come back soon", "ᱤᱧ ᱡᱟᱞᱫᱤ ᱨᱩᱣᱟᱹᱲ ᱟ", "inj jaldi ruwar a"],
    ["Take care of yourself", "ᱟᱢ ᱟᱢᱟᱜ ᱫᱮᱠᱷᱟ ᱢᱮ", "am amag dekha me"],
    ["Have a good day", "ᱵᱷᱟᱞᱮ ᱫᱤᱱ ᱛᱟᱦᱮᱸᱱ ᱢᱟ", "bhale din taheny ma"],
    ["It is very nice", "ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ ᱢᱮᱱᱟᱜ ᱟ", "adi bhale menag a"],
    ["I don't know", "ᱤᱧ ᱵᱟᱝ ᱵᱟᱰᱟᱭ ᱟ", "inj bang baday a"],
    ["Do you know?", "ᱟᱢ ᱵᱟᱰᱟᱭ ᱟᱢ?", "am baday am?"],
    ["Tell me the truth", "ᱤᱧ ᱠᱮ ᱥᱟᱹᱨᱤ ᱠᱟᱹᱛᱷᱟ ᱨᱚᱲ ᱢᱮ", "inj ke sari katha ror me"],
    ["I promise", "ᱤᱧ ᱠᱟᱹᱛᱷᱟ ᱮᱢ ᱟᱭᱟ", "inj katha em aya"],
    ["Never give up", "ᱡᱟᱦᱟᱸᱱᱟᱜ ᱡᱷᱤᱡ ᱛᱟᱵᱚᱱ ᱢᱮ", "jahanag jhij tabon me"],
    ["Time heals everything", "ᱵᱮᱞᱟ ᱡᱚᱛᱚ ᱵᱷᱟᱞᱮ ᱮᱢ ᱟ", "bela joto bhale em a"],
    ["Believe in yourself", "ᱟᱢ ᱟᱢᱟᱜ ᱪᱮᱛᱟᱱ ᱵᱤᱥᱣᱟᱥ ᱢᱮ", "am amag cetan biswas me"],
    ["Hard work pays off", "ᱟᱹᱰᱤ ᱠᱟᱹᱢᱤ ᱯᱷᱚᱞ ᱮᱢ ᱟ", "adi kami phol em a"]
]

# 654 - Learn Santali by Communicative Approach
LESSONS[654] = [
    ["Can you teach me Santali?", "ᱟᱢ ᱤᱧ ᱠᱮ ᱥᱟᱱᱛᱟᱲᱤ ᱥᱤᱠᱷᱟᱣ ᱫᱟᱲᱮᱭᱟᱢ ᱢᱟ?", "am inj ke santari sikhaw dareyam ma?"],
    ["Yes, let's start with greetings", "ᱦᱮᱡ, ᱡᱚᱦᱟᱨ ᱠᱷᱚᱱ ᱪᱟᱞᱩ ᱟᱞᱮ", "hej, johar khon chalu ale"],
    ["How do you say 'water' in Santali?", "ᱥᱟᱱᱛᱟᱲᱤ ᱨᱮ 'ᱫᱟᱜ' ᱚᱠᱟ ᱞᱮᱠᱟ ᱨᱚᱲ ᱟ?", "santari re 'dag' oka leka ror a?"],
    ["Water is called 'dag' in Santali", "ᱥᱟᱱᱛᱟᱲᱤ ᱨᱮ ᱫᱟᱜ ᱠᱮ 'ᱫᱟᱜ' ᱨᱚᱲ ᱟ", "santari re water ke 'dag' ror a"],
    ["What does 'johar' mean?", "'ᱡᱚᱦᱟᱨ' ᱢᱟᱱᱮ ᱪᱮᱫ?", "'johar' mane ced?"],
    ["Johar means hello/greetings", "ᱡᱚᱦᱟᱨ ᱢᱟᱱᱮ ᱱᱟᱢᱟᱥᱠᱟᱨ", "johar mane namaskar"],
    ["Practice speaking every day", "ᱫᱤᱱ ᱫᱤᱱ ᱨᱚᱲ ᱟᱵᱷᱤᱭᱟᱥ ᱢᱮ", "din din ror abhiyas me"],
    ["Talk to Santali speakers", "ᱥᱟᱱᱛᱟᱲᱤ ᱨᱚᱲ ᱦᱚᱲ ᱥᱟᱶ ᱨᱚᱲ ᱢᱮ", "santari ror hor saw ror me"],
    ["Listen to Santali songs", "ᱥᱟᱱᱛᱟᱲᱤ ᱥᱮᱨᱮᱧ ᱟᱭᱠᱟᱣ ᱢᱮ", "santari sereny aykaw me"],
    ["Read Santali books", "ᱥᱟᱱᱛᱟᱲᱤ ᱯᱩᱛᱷᱤ ᱯᱟᱲᱦᱟᱣ ᱢᱮ", "santari puthi parhaw me"],
    ["Write sentences in Ol Chiki", "ᱚᱞ ᱪᱤᱠᱤ ᱨᱮ ᱠᱟᱹᱛᱷᱟ ᱚᱞ ᱢᱮ", "Ol Chiki re katha ol me"],
    ["Repeat after me", "ᱤᱧ ᱛᱟᱭᱚᱢ ᱨᱚᱲ ᱢᱮ", "inj tayom ror me"],
    ["You are improving quickly", "ᱟᱢ ᱡᱟᱞᱫᱤ ᱥᱮᱪᱮᱫ ᱟᱢ", "am jaldi seced am"],
    ["Don't be afraid to make mistakes", "ᱵᱷᱩᱞ ᱠᱮ ᱵᱚᱲ ᱡᱷᱤᱡ ᱢᱮ", "bhul ke bor jhij me"],
    ["Language learning takes time", "ᱯᱟᱹᱨᱥᱤ ᱥᱮᱪᱮᱫ ᱵᱮᱞᱟ ᱞᱟᱜᱤᱫ ᱟ", "parsi seced bela lagid a"],
    ["You speak Santali very well now", "ᱟᱢ ᱱᱤᱛ ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ ᱥᱟᱱᱛᱟᱲᱤ ᱨᱚᱲ ᱟᱢ", "am nit adi bhale santari ror am"],
    ["Keep practising daily", "ᱫᱤᱱ ᱫᱤᱱ ᱟᱵᱷᱤᱭᱟᱥ ᱢᱮ", "din din abhiyas me"],
    ["I enjoy learning this language", "ᱤᱧ ᱱᱚᱣᱟ ᱯᱟᱹᱨᱥᱤ ᱥᱮᱪᱮᱫ ᱨᱟᱹᱥᱠᱟᱹ ᱟ", "inj nowa parsi seced raska a"]
]

# 655 - Simple Santali sentences practice 1
LESSONS[655] = [
    ["The sun rises in the east", "ᱥᱤᱧ ᱯᱩᱨᱩᱵ ᱨᱮ ᱵᱟᱦᱟ ᱟ", "sing purub re baha a"],
    ["The bird is sitting on the tree", "ᱪᱮᱲᱮ ᱫᱟᱨᱮ ᱪᱮᱛᱟᱱ ᱨᱮ ᱫᱩᱲᱩᱵ ᱮᱱᱟ", "chere dare cetan re durub ena"],
    ["The river flows through the village", "ᱜᱟᱰᱟ ᱟᱹᱛᱩ ᱛᱟᱞᱟ ᱨᱮ ᱵᱟᱦᱟ ᱟ", "gada atu tala re baha a"],
    ["Children play in the field", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱢᱟᱭᱫᱟᱱ ᱨᱮ ᱠᱷᱮᱞ ᱠᱚ", "gidra ko maydan re khel ko"],
    ["The farmer ploughs the field", "ᱨᱟᱹᱭᱤᱡ ᱟᱹᱰᱤ ᱠᱩᱲᱤ ᱟ", "rayij adi kuri a"],
    ["I read a book every day", "ᱤᱧ ᱫᱤᱱ ᱫᱤᱱ ᱯᱩᱛᱷᱤ ᱯᱟᱲᱦᱟᱣ ᱟᱭᱟ", "inj din din puthi parhaw aya"],
    ["She sings very well", "ᱩᱱᱤ ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ ᱥᱮᱨᱮᱧ ᱮ", "uni adi bhale sereny e"],
    ["The cow gives milk", "ᱜᱟᱤ ᱫᱩᱫᱷ ᱮᱢ ᱟ", "gai dudh em a"],
    ["We go to school", "ᱟᱞᱮ ᱥᱠᱩᱞ ᱥᱮᱱ ᱟᱞᱮ", "ale skul sen ale"],
    ["The dog is barking", "ᱥᱮᱛᱟ ᱦᱩᱸᱠ ᱢᱮᱱᱟᱜ ᱟ", "seta hunk menag a"],
    ["Mother is cooking food", "ᱟᱭᱚ ᱡᱚᱢ ᱨᱟᱸᱰᱷᱟ ᱢᱮᱱᱟᱜ ᱮ", "ayo jom randha menag e"],
    ["Father is working in the field", "ᱟᱯᱟ ᱚᱲᱟᱜ ᱨᱮ ᱠᱟᱹᱢᱤ ᱢᱮᱱᱟᱜ ᱮ", "apa orag re kami menag e"],
    ["The sky is very blue", "ᱥᱮᱨᱢᱟ ᱟᱹᱰᱤ ᱱᱤᱞ ᱢᱮᱱᱟᱜ ᱟ", "serma adi nil menag a"],
    ["I like mangoes very much", "ᱤᱧ ᱩᱞ ᱟᱹᱰᱤ ᱫᱩᱞᱟᱹᱲ ᱟᱭᱟ", "inj ul adi dular aya"],
    ["The flower is red", "ᱵᱟᱦᱟ ᱟᱨᱟᱜ ᱢᱮᱱᱟᱜ ᱟ", "baha arag menag a"],
    ["The fish lives in water", "ᱦᱟᱠᱩ ᱫᱟᱜ ᱨᱮ ᱛᱟᱦᱮᱸᱱ ᱟ", "haku dag re taheny a"],
    ["My house is near the river", "ᱤᱧᱟᱜ ᱚᱲᱟᱜ ᱜᱟᱰᱟ ᱱᱮᱰᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "injag orag gada neda re menag a"],
    ["The moon comes at night", "ᱪᱟᱸᱫᱚ ᱧᱤᱸᱫᱟ ᱨᱮ ᱦᱤᱡᱩᱜ ᱟ", "chando nyinda re hijug a"]
]

# 656 - Prepositions practice
LESSONS[656] = [
    ["The book is on the table", "ᱯᱩᱛᱷᱤ ᱢᱮᱡ ᱪᱮᱛᱟᱱ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "puthi mej cetan re menag a"],
    ["The cat is under the bed", "ᱢᱤᱸᱫ ᱪᱚᱠᱤ ᱞᱟᱛᱟᱨ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "mind choki latar re menag a"],
    ["The ball is inside the box", "ᱜᱮᱸᱫ ᱵᱚᱠᱥ ᱵᱷᱤᱛᱤᱨ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "gend box bhitir re menag a"],
    ["The bird flew above the house", "ᱪᱮᱲᱮ ᱚᱲᱟᱜ ᱪᱮᱛᱟᱱ ᱩᱲᱟᱣ ᱮᱱᱟ", "chere orag cetan uraw ena"],
    ["The tree is behind the school", "ᱫᱟᱨᱮ ᱥᱠᱩᱞ ᱯᱤᱪᱷᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "dare skul pichha re menag a"],
    ["The market is in front of the temple", "ᱵᱟᱡᱟᱨ ᱛᱷᱟᱱ ᱟᱜᱮ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "bajar than age re menag a"],
    ["He is standing between two trees", "ᱩᱱᱤ ᱵᱟᱨ ᱫᱟᱨᱮ ᱛᱟᱞᱟ ᱨᱮ ᱛᱤᱝ ᱮᱱᱟ", "uni bar dare tala re ting ena"],
    ["The pen is beside the notebook", "ᱠᱟᱞᱚᱢ ᱠᱚᱯᱤ ᱱᱮᱰᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "kalom kopi neda re menag a"],
    ["Walk along the river", "ᱜᱟᱰᱟ ᱫᱷᱟᱨ ᱨᱮ ᱥᱟᱞᱟᱜ ᱢᱮ", "gada dhar re salag me"],
    ["The shop is across the road", "ᱫᱚᱠᱟᱱ ᱨᱟᱦᱟ ᱚᱛᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "dokan raha ota re menag a"],
    ["Come towards me", "ᱤᱧ ᱫᱤᱥᱟ ᱦᱤᱡᱩᱜ ᱢᱮ", "inj disa hijug me"],
    ["Go away from here", "ᱱᱮᱛᱟᱨ ᱠᱷᱚᱱ ᱥᱮᱱ ᱢᱮ", "netar khon sen me"],
    ["The picture is on the wall", "ᱪᱤᱛᱟᱨ ᱵᱷᱤᱛ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "chitar bhit re menag a"],
    ["The water is in the pot", "ᱫᱟᱜ ᱜᱷᱚᱲᱟ ᱵᱷᱤᱛᱤᱨ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "dag ghora bhitir re menag a"],
    ["He jumped over the fence", "ᱩᱱᱤ ᱵᱟᱨ ᱪᱮᱛᱟᱱ ᱠᱷᱚᱱ ᱩᱞ ᱮᱱᱟ", "uni bar cetan khon ul ena"],
    ["Sit near me", "ᱤᱧ ᱱᱮᱰᱟ ᱨᱮ ᱫᱩᱲᱩᱵ ᱢᱮ", "inj neda re durub me"],
    ["The child is among the flowers", "ᱜᱤᱫᱽᱨᱟᱹ ᱵᱟᱦᱟ ᱛᱟᱞᱟ ᱨᱮ ᱢᱮᱱᱟᱜ ᱮ", "gidra baha tala re menag e"],
    ["Through the forest we walked", "ᱵᱤᱨ ᱛᱟᱞᱟ ᱨᱮ ᱟᱞᱮ ᱥᱟᱞᱟᱜ ᱮᱱᱟ", "bir tala re ale salag ena"]
]

# 657 - Santali jokes
LESSONS[657] = [
    ["Let me tell you a funny story", "ᱤᱧ ᱟᱢ ᱠᱮ ᱢᱤᱫ ᱞᱟᱸᱫᱟ ᱠᱟᱹᱛᱷᱟ ᱨᱚᱲ ᱟ", "inj am ke mid landa katha ror a"],
    ["A boy asked his father for money", "ᱢᱤᱫ ᱠᱚᱲᱟ ᱟᱯᱟ ᱴᱷᱮᱱ ᱴᱟᱠᱟ ᱠᱩᱞᱤ ᱮᱱᱟ", "mid kora apa then taka kuli ena"],
    ["Father said, money doesn't grow on trees", "ᱟᱯᱟ ᱨᱚᱲ ᱮᱱᱟ, ᱴᱟᱠᱟ ᱫᱟᱨᱮ ᱨᱮ ᱵᱟᱝ ᱡᱚ ᱟ", "apa ror ena, taka dare re bang jo a"],
    ["The boy replied, then why do banks have branches?", "ᱠᱚᱲᱟ ᱨᱚᱲ ᱮᱱᱟ, ᱛᱟᱭᱚᱢ ᱵᱮᱸᱠ ᱟᱜ ᱫᱟᱞ ᱪᱮᱫ ᱞᱟᱜᱤᱫ ᱢᱮᱱᱟᱜ ᱟ?", "kora ror ena, tayom bank ag dal ced lagid menag a?"],
    ["Everyone laughed!", "ᱡᱚᱛᱚ ᱦᱚᱲ ᱞᱟᱸᱫᱟ ᱮᱱᱟ!", "joto hor landa ena!"],
    ["Teacher asked, what comes after Tuesday?", "ᱯᱟᱲᱦᱟᱣᱮᱫ ᱠᱩᱞᱤ ᱮᱱᱟ, ᱢᱚᱸᱜᱚᱞ ᱛᱟᱭᱚᱢ ᱪᱮᱫ ᱦᱤᱡᱩᱜ ᱟ?", "parhawed kuli ena, mongol tayom ced hijug a?"],
    ["The student said, Wednesday!", "ᱪᱟᱴᱟᱨ ᱨᱚᱲ ᱮᱱᱟ, ᱵᱩᱫᱷ!", "chatar ror ena, budh!"],
    ["Teacher said, I meant what comes after 2?", "ᱯᱟᱲᱦᱟᱣᱮᱫ ᱨᱚᱲ ᱮᱱᱟ, ᱤᱧᱟᱜ ᱢᱟᱱᱮ ᱵᱟᱨ ᱛᱟᱭᱚᱢ ᱪᱮᱫ?", "parhawed ror ena, injag mane bar tayom ced?"],
    ["The student replied, 3!", "ᱪᱟᱴᱟᱨ ᱨᱚᱲ ᱮᱱᱟ, ᱯᱮ!", "chatar ror ena, pe!"],
    ["Why did the tomato turn red?", "ᱴᱟᱢᱟᱴᱚ ᱪᱮᱫ ᱞᱟᱜᱤᱫ ᱟᱨᱟᱜ ᱦᱩᱭ ᱮᱱᱟ?", "tamato ced lagid arag huy ena?"],
    ["Because it saw the salad dressing!", "ᱪᱮᱫ ᱞᱟᱜᱤᱫ ᱢᱮᱱᱫᱚ ᱥᱟᱞᱟᱫ ᱠᱟᱹᱯᱲᱟ ᱫᱚᱦᱚ ᱧᱮᱞ ᱮᱱᱟ!", "ced lagid mendo salad kapra doho nyel ena!"],
    ["A man went to buy a clock", "ᱢᱤᱫ ᱦᱚᱲ ᱜᱷᱚᱲᱤ ᱧᱟᱢ ᱞᱟᱜᱤᱫ ᱥᱮᱱ ᱮᱱᱟ", "mid hor ghori nyam lagid sen ena"],
    ["He asked, does this clock run well?", "ᱩᱱᱤ ᱠᱩᱞᱤ ᱮᱱᱟ, ᱱᱚᱣᱟ ᱜᱷᱚᱲᱤ ᱵᱷᱟᱞᱮ ᱪᱟᱞᱟᱜ ᱟ?", "uni kuli ena, nowa ghori bhale chalag a?"],
    ["Shopkeeper said, no it can't, it has no legs!", "ᱫᱚᱠᱟᱱᱫᱟᱨ ᱨᱚᱲ ᱮᱱᱟ, ᱵᱟᱝ, ᱟᱜ ᱠᱟᱴᱟ ᱵᱟᱝ ᱢᱮᱱᱟᱜ ᱟ!", "dokandar ror ena, bang, ag kata bang menag a!"],
    ["Laughter is the best medicine", "ᱞᱟᱸᱫᱟ ᱥᱟᱹᱨᱤ ᱠᱷᱚᱱ ᱵᱷᱟᱞᱮ ᱟᱜ ᱠᱟᱱᱟ", "landa sari khon bhale ag kana"],
    ["Always smile and be happy", "ᱡᱟᱦᱟᱸᱱᱟᱜ ᱞᱟᱸᱫᱟ ᱟᱨ ᱨᱟᱹᱥᱠᱟᱹ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "jahanag landa ar raska taheny me"],
    ["Did you like the joke?", "ᱟᱢᱟᱜ ᱞᱟᱸᱫᱟ ᱠᱟᱹᱛᱷᱟ ᱵᱷᱟᱞᱮ ᱮᱱᱟ?", "amag landa katha bhale ena?"],
    ["Share jokes with friends", "ᱥᱟᱶᱛᱟ ᱥᱟᱶ ᱞᱟᱸᱫᱟ ᱠᱟᱹᱛᱷᱟ ᱨᱚᱲ ᱢᱮ", "sawta saw landa katha ror me"]
]

# 658 - Daily reading practice - jokes, thoughts, quotes
LESSONS[658] = [
    ["Knowledge is power", "ᱜᱤᱭᱟᱱ ᱡᱚᱨ ᱠᱟᱱᱟ", "giyan jor kana"],
    ["Unity is strength", "ᱮᱠᱛᱟ ᱡᱚᱨ ᱠᱟᱱᱟ", "ekta jor kana"],
    ["Education is the key to success", "ᱯᱟᱲᱦᱟᱣ ᱡᱤᱛ ᱟᱜ ᱪᱟᱵᱤ ᱠᱟᱱᱟ", "parhaw jit ag chabi kana"],
    ["Respect your elders", "ᱢᱟᱨᱟᱝ ᱦᱚᱲ ᱢᱟᱱ ᱢᱮ", "marang hor man me"],
    ["Love your language", "ᱟᱢᱟᱜ ᱯᱟᱹᱨᱥᱤ ᱫᱩᱞᱟᱹᱲ ᱢᱮ", "amag parsi dular me"],
    ["Nature is our mother", "ᱡᱟᱸᱜᱟ ᱟᱞᱮᱭᱟᱜ ᱟᱭᱚ ᱠᱟᱱᱟ", "janga aleyag ayo kana"],
    ["Honesty is the best policy", "ᱥᱟᱹᱨᱤ ᱥᱟᱹᱨᱤ ᱠᱷᱚᱱ ᱵᱷᱟᱞᱮ ᱱᱤᱛᱤ ᱠᱟᱱᱟ", "sari sari khon bhale niti kana"],
    ["Work hard, dream big", "ᱟᱹᱰᱤ ᱠᱟᱹᱢᱤ ᱢᱮ, ᱢᱟᱨᱟᱝ ᱥᱩᱯᱤᱱ ᱧᱮᱞ ᱢᱮ", "adi kami me, marang supin nyel me"],
    ["Together we can achieve anything", "ᱥᱟᱶᱛᱮ ᱟᱞᱮ ᱡᱚᱛᱚ ᱫᱟᱲᱮ ᱟᱞᱮ", "sawte ale joto dare ale"],
    ["Save water, save life", "ᱫᱟᱜ ᱵᱟᱸᱪᱟᱣ ᱢᱮ, ᱡᱤᱣᱤ ᱵᱟᱸᱪᱟᱣ ᱢᱮ", "dag banchaw me, jiwi banchaw me"],
    ["Plant trees for the future", "ᱟᱜᱤᱞᱟ ᱞᱟᱜᱤᱫ ᱫᱟᱨᱮ ᱨᱚᱦᱚᱲ ᱢᱮ", "agila lagid dare rohor me"],
    ["Every child has the right to education", "ᱡᱚᱛᱚ ᱜᱤᱫᱽᱨᱟᱹ ᱟᱜ ᱯᱟᱲᱦᱟᱣ ᱦᱚᱠ ᱢᱮᱱᱟᱜ ᱟ", "joto gidra ag parhaw hok menag a"],
    ["A smile costs nothing", "ᱞᱟᱸᱫᱟ ᱟᱜ ᱫᱟᱢ ᱵᱟᱝ ᱢᱮᱱᱟᱜ ᱟ", "landa ag dam bang menag a"],
    ["Actions speak louder than words", "ᱠᱟᱹᱢᱤ ᱠᱟᱹᱛᱷᱟ ᱠᱷᱚᱱ ᱡᱚᱨ ᱨᱚᱲ ᱟ", "kami katha khon jor ror a"],
    ["Peace begins with a smile", "ᱥᱟᱸᱛᱤ ᱞᱟᱸᱫᱟ ᱠᱷᱚᱱ ᱪᱟᱞᱩ ᱟ", "santi landa khon chalu a"],
    ["The future belongs to the brave", "ᱟᱜᱤᱞᱟ ᱵᱷᱤᱨ ᱦᱚᱲ ᱟᱜ ᱠᱟᱱᱟ", "agila bhir hor ag kana"],
    ["Read daily, grow daily", "ᱫᱤᱱ ᱫᱤᱱ ᱯᱟᱲᱦᱟᱣ ᱢᱮ, ᱫᱤᱱ ᱫᱤᱱ ᱵᱚᱞᱚ ᱢᱮ", "din din parhaw me, din din bolo me"],
    ["Your language is your identity", "ᱟᱢᱟᱜ ᱯᱟᱹᱨᱥᱤ ᱟᱢᱟᱜ ᱯᱚᱦᱪᱟᱱ ᱠᱟᱱᱟ", "amag parsi amag pohchan kana"]
]

# 659 - My experience with Social Media
LESSONS[659] = [
    ["I use social media every day", "ᱤᱧ ᱫᱤᱱ ᱫᱤᱱ ᱥᱚᱥᱤᱭᱟᱞ ᱢᱤᱰᱤᱭᱟ ᱵᱮᱵᱦᱟᱨ ᱟᱭᱟ", "inj din din social media bebhar aya"],
    ["I have accounts on Facebook and Instagram", "ᱤᱧᱟᱜ ᱯᱷᱮᱥᱵᱩᱠ ᱟᱨ ᱤᱱᱥᱴᱟᱜᱨᱟᱢ ᱨᱮ ᱮᱠᱟᱣᱩᱱᱴ ᱢᱮᱱᱟᱜ ᱟ", "injag Facebook ar Instagram re account menag a"],
    ["I share photos of my village", "ᱤᱧ ᱤᱧᱟᱜ ᱟᱹᱛᱩ ᱯᱷᱚᱴᱚ ᱥᱮᱭᱟᱨ ᱟᱭᱟ", "inj injag atu photo share aya"],
    ["Social media connects people", "ᱥᱚᱥᱤᱭᱟᱞ ᱢᱤᱰᱤᱭᱟ ᱦᱚᱲ ᱡᱩᱲᱟᱣ ᱟ", "social media hor juraw a"],
    ["I watch Santali videos online", "ᱤᱧ ᱚᱱᱞᱟᱤᱱ ᱥᱟᱱᱛᱟᱲᱤ ᱵᱷᱤᱰᱤᱭᱚ ᱧᱮᱞ ᱟᱭᱟ", "inj online santari video nyel aya"],
    ["Don't share personal information", "ᱟᱢᱟᱜ ᱵᱤᱥᱮᱥ ᱡᱟᱱᱠᱟᱨᱤ ᱡᱷᱤᱡ ᱥᱮᱭᱟᱨ ᱢᱮ", "amag bises jankari jhij share me"],
    ["Fake news is dangerous", "ᱡᱷᱩᱴ ᱠᱷᱚᱵᱚᱨ ᱵᱤᱯᱚᱫ ᱠᱟᱱᱟ", "jhut khobor bipod kana"],
    ["Use social media wisely", "ᱥᱚᱥᱤᱭᱟᱞ ᱢᱤᱰᱤᱭᱟ ᱵᱩᱫᱷᱤ ᱨᱮ ᱵᱮᱵᱦᱟᱨ ᱢᱮ", "social media budhi re bebhar me"],
    ["Too much screen time is bad", "ᱟᱹᱰᱤ ᱥᱠᱨᱤᱱ ᱵᱮᱞᱟ ᱵᱷᱟᱞᱮ ᱵᱟᱝ ᱠᱟᱱᱟ", "adi screen bela bhale bang kana"],
    ["I post in Ol Chiki script", "ᱤᱧ ᱚᱞ ᱪᱤᱠᱤ ᱨᱮ ᱯᱚᱥᱴ ᱟᱭᱟ", "inj Ol Chiki re post aya"],
    ["Many Santali groups are on Facebook", "ᱟᱹᱰᱤ ᱥᱟᱱᱛᱟᱲᱤ ᱜᱨᱩᱯ ᱯᱷᱮᱥᱵᱩᱠ ᱨᱮ ᱢᱮᱱᱟᱜ ᱟ", "adi santari group Facebook re menag a"],
    ["I read Santali news online", "ᱤᱧ ᱚᱱᱞᱟᱤᱱ ᱥᱟᱱᱛᱟᱲᱤ ᱠᱷᱚᱵᱚᱨ ᱯᱟᱲᱦᱟᱣ ᱟᱭᱟ", "inj online santari khobor parhaw aya"],
    ["Children should limit screen time", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱥᱠᱨᱤᱱ ᱵᱮᱞᱟ ᱠᱚᱢ ᱞᱟᱜᱤᱫ ᱟ", "gidra ko screen bela kom lagid a"],
    ["I made many friends online", "ᱤᱧ ᱟᱹᱰᱤ ᱥᱟᱶᱛᱟ ᱚᱱᱞᱟᱤᱱ ᱧᱟᱢ ᱮᱱᱟ", "inj adi sawta online nyam ena"],
    ["Be careful of online scams", "ᱚᱱᱞᱟᱤᱱ ᱵᱷᱤᱞ ᱠᱷᱚᱱ ᱥᱟᱵᱫᱷᱟᱱ ᱛᱟᱦᱮᱸᱱ ᱢᱮ", "online bhil khon sabdhan taheny me"],
    ["Social media is good for learning", "ᱥᱚᱥᱤᱭᱟᱞ ᱢᱤᱰᱤᱭᱟ ᱥᱮᱪᱮᱫ ᱞᱟᱜᱤᱫ ᱵᱷᱟᱞᱮ ᱠᱟᱱᱟ", "social media seced lagid bhale kana"],
    ["Don't believe everything you see online", "ᱚᱱᱞᱟᱤᱱ ᱡᱚᱛᱚ ᱡᱷᱤᱡ ᱵᱤᱥᱣᱟᱥ ᱢᱮ", "online joto jhij biswas me"],
    ["Use the internet for good purposes", "ᱤᱱᱴᱟᱨᱱᱮᱴ ᱵᱷᱟᱞᱮ ᱠᱟᱹᱢᱤ ᱞᱟᱜᱤᱫ ᱵᱮᱵᱦᱟᱨ ᱢᱮ", "internet bhale kami lagid bebhar me"]
]

# 660 - Conversation about the eclipse
LESSONS[660] = [
    ["Did you see the eclipse today?", "ᱟᱢ ᱟᱡ ᱜᱨᱚᱦᱚᱱ ᱧᱮᱞ ᱮᱱᱟ?", "am aj grohon nyel ena?"],
    ["Yes, it was a solar eclipse", "ᱦᱮᱡ, ᱥᱤᱧ ᱜᱨᱚᱦᱚᱱ ᱛᱟᱦᱮᱸᱱ ᱟ", "hej, sing grohon taheny a"],
    ["The sun was covered by the moon", "ᱥᱤᱧ ᱠᱮ ᱪᱟᱸᱫᱚ ᱰᱷᱟᱸᱯ ᱮᱱᱟ", "sing ke chando dhanp ena"],
    ["It became dark in daytime", "ᱥᱤᱧ ᱵᱮᱞᱟ ᱨᱮ ᱧᱩᱛ ᱦᱩᱭ ᱮᱱᱟ", "sing bela re nyut huy ena"],
    ["Don't look at the eclipse directly", "ᱜᱨᱚᱦᱚᱱ ᱥᱤᱫᱷᱟ ᱡᱷᱤᱡ ᱧᱮᱞ ᱢᱮ", "grohon sidha jhij nyel me"],
    ["Use special glasses to watch", "ᱧᱮᱞ ᱞᱟᱜᱤᱫ ᱵᱤᱥᱮᱥ ᱪᱚᱥᱢᱟ ᱵᱮᱵᱦᱟᱨ ᱢᱮ", "nyel lagid bises chosma bebhar me"],
    ["The eclipse lasted for two hours", "ᱜᱨᱚᱦᱚᱱ ᱵᱟᱨ ᱜᱷᱚᱱᱴᱟ ᱛᱟᱦᱮᱸᱱ ᱟ", "grohon bar ghonta taheny a"],
    ["It is a natural phenomenon", "ᱱᱚᱣᱟ ᱡᱟᱸᱜᱟ ᱟᱜ ᱜᱷᱚᱴᱱᱟ ᱠᱟᱱᱟ", "nowa janga ag ghotna kana"],
    ["Scientists study eclipses", "ᱵᱤᱜᱤᱟᱱᱤ ᱜᱨᱚᱦᱚᱱ ᱥᱮᱪᱮᱫ ᱠᱚ", "bigiani grohon seced ko"],
    ["The next eclipse will come next year", "ᱟᱜᱤᱞᱟ ᱜᱨᱚᱦᱚᱱ ᱟᱜᱤᱞᱟ ᱥᱮᱨᱢᱟ ᱦᱤᱡᱩᱜ ᱟ", "agila grohon agila serma hijug a"],
    ["A lunar eclipse happens at night", "ᱪᱟᱸᱫᱚ ᱜᱨᱚᱦᱚᱱ ᱧᱤᱸᱫᱟ ᱨᱮ ᱦᱩᱭ ᱟ", "chando grohon nyinda re huy a"],
    ["Old people tell many stories about eclipses", "ᱢᱟᱨᱟᱝ ᱦᱚᱲ ᱜᱨᱚᱦᱚᱱ ᱵᱤᱥᱚᱭ ᱟᱹᱰᱤ ᱠᱟᱹᱛᱷᱟ ᱨᱚᱲ ᱠᱚ", "marang hor grohon bisoy adi katha ror ko"],
    ["Some people beat drums during eclipse", "ᱠᱟᱛᱮ ᱦᱚᱲ ᱜᱨᱚᱦᱚᱱ ᱵᱮᱞᱟ ᱢᱟᱸᱫᱚᱞ ᱵᱟᱡᱟᱣ ᱠᱚ", "kate hor grohon bela mandol bajaw ko"],
    ["I took photos of the eclipse", "ᱤᱧ ᱜᱨᱚᱦᱚᱱ ᱯᱷᱚᱴᱚ ᱤᱫᱤ ᱮᱱᱟ", "inj grohon photo idi ena"],
    ["It was a wonderful experience", "ᱟᱹᱰᱤ ᱵᱷᱟᱞᱮ ᱟᱱᱩᱵᱷᱚᱵ ᱛᱟᱦᱮᱸᱱ ᱟ", "adi bhale anubhob taheny a"],
    ["The birds went quiet during the eclipse", "ᱜᱨᱚᱦᱚᱱ ᱵᱮᱞᱟ ᱪᱮᱲᱮ ᱛᱤᱥᱤᱧ ᱦᱩᱭ ᱮᱱᱟ", "grohon bela chere tising huy ena"],
    ["Eclipse is not something to be afraid of", "ᱜᱨᱚᱦᱚᱱ ᱵᱚᱲ ᱟᱜ ᱵᱟᱝ ᱠᱟᱱᱟ", "grohon bor ag bang kana"],
    ["Science explains everything", "ᱵᱤᱜᱤᱟᱱ ᱡᱚᱛᱚ ᱵᱩᱡᱷᱟᱹᱣ ᱮᱢ ᱟ", "bigian joto bujhaw em a"]
]

# 661 - International Women's Day
LESSONS[661] = [
    ["Happy Women's Day!", "ᱠᱩᱲᱤ ᱫᱤᱱ ᱨᱟᱹᱥᱠᱟᱹ ᱢᱟ!", "kuri din raska ma!"],
    ["Women are the strength of society", "ᱠᱩᱲᱤ ᱥᱚᱢᱟᱡ ᱟᱜ ᱡᱚᱨ ᱠᱟᱱᱟ", "kuri somaj ag jor kana"],
    ["We celebrate Women's Day on March 8", "ᱟᱞᱮ ᱤᱨᱟᱞ ᱢᱟᱨᱪ ᱨᱮ ᱠᱩᱲᱤ ᱫᱤᱱ ᱢᱟᱱᱟᱣ ᱟᱞᱮ", "ale iral March re kuri din manaw ale"],
    ["Every girl should go to school", "ᱡᱚᱛᱚ ᱠᱩᱲᱤ ᱥᱠᱩᱞ ᱥᱮᱱ ᱞᱟᱜᱤᱫ ᱟ", "joto kuri skul sen lagid a"],
    ["Women can do anything", "ᱠᱩᱲᱤ ᱡᱚᱛᱚ ᱫᱟᱲᱮ ᱠᱚ", "kuri joto dare ko"],
    ["Respect all women", "ᱡᱚᱛᱚ ᱠᱩᱲᱤ ᱢᱟᱱ ᱢᱮ", "joto kuri man me"],
    ["My mother is my hero", "ᱤᱧᱟᱜ ᱟᱭᱚ ᱤᱧᱟᱜ ᱦᱤᱨᱚ ᱠᱟᱱᱟ", "injag ayo injag hero kana"],
    ["Women work twice as hard", "ᱠᱩᱲᱤ ᱵᱟᱨ ᱜᱩᱬᱟ ᱠᱟᱹᱢᱤ ᱠᱮᱫ ᱠᱚ", "kuri bar guna kami ked ko"],
    ["Girls should be educated", "ᱠᱩᱲᱤ ᱯᱟᱲᱦᱟᱣ ᱞᱟᱜᱤᱫ ᱟ", "kuri parhaw lagid a"],
    ["Women are leaders too", "ᱠᱩᱲᱤ ᱦᱚᱭ ᱞᱤᱰᱟᱨ ᱠᱟᱱᱟ", "kuri hoy leader kana"],
    ["Equal rights for men and women", "ᱠᱚᱲᱟ ᱟᱨ ᱠᱩᱲᱤ ᱵᱟᱨᱟᱵᱚᱨ ᱦᱚᱠ", "kora ar kuri barabor hok"],
    ["Santali women are very hardworking", "ᱥᱟᱱᱛᱟᱲ ᱠᱩᱲᱤ ᱟᱹᱰᱤ ᱠᱟᱹᱢᱤ ᱮᱠᱷᱮᱱ ᱠᱟᱱᱟ", "Santar kuri adi kami ekhen kana"],
    ["Women in our village are strong", "ᱟᱞᱮᱭᱟᱜ ᱟᱹᱛᱩ ᱠᱩᱲᱤ ᱡᱚᱨ ᱢᱮᱱᱟᱜ ᱠᱚ", "aleyag atu kuri jor menag ko"],
    ["Support women's education", "ᱠᱩᱲᱤ ᱯᱟᱲᱦᱟᱣ ᱥᱟᱹᱜᱟᱹᱭ ᱢᱮ", "kuri parhaw sagay me"],
    ["Women are the backbone of the family", "ᱠᱩᱲᱤ ᱯᱟᱹᱨᱤᱵᱟᱨ ᱟᱜ ᱵᱩᱱᱤᱭᱟᱫ ᱠᱟᱱᱟ", "kuri paribar ag buniyad kana"],
    ["Let us all celebrate together", "ᱟᱞᱮ ᱡᱚᱛᱚ ᱥᱟᱶᱛᱮ ᱢᱟᱱᱟᱣ ᱟᱞᱮ", "ale joto sawte manaw ale"],
    ["Women bring change in society", "ᱠᱩᱲᱤ ᱥᱚᱢᱟᱡ ᱨᱮ ᱵᱚᱫᱚᱞ ᱟᱹᱜᱩ ᱠᱚ", "kuri somaj re bodol agu ko"],
    ["Salute to all the women!", "ᱡᱚᱛᱚ ᱠᱩᱲᱤ ᱠᱮ ᱡᱚᱦᱟᱨ!", "joto kuri ke johar!"]
]

# 662 - Quarrel at home
LESSONS[662] = [
    ["Why are you shouting?", "ᱟᱢ ᱪᱮᱫ ᱞᱟᱜᱤᱫ ᱦᱟᱸᱠ ᱟᱢ?", "am ced lagid hank am?"],
    ["Please stop fighting", "ᱦᱮᱡ ᱞᱟᱲᱟᱭ ᱵᱚᱱᱫ ᱢᱮ", "hej laray bond me"],
    ["You always blame me", "ᱟᱢ ᱡᱟᱦᱟᱸᱱᱟᱜ ᱤᱧ ᱠᱮ ᱫᱚᱥ ᱮᱢ ᱟᱢ", "am jahanag inj ke dos em am"],
    ["I didn't do anything wrong", "ᱤᱧ ᱡᱟᱦᱟᱸ ᱵᱷᱩᱞ ᱵᱟᱝ ᱠᱮᱫ ᱮᱱᱟ", "inj jahang bhul bang ked ena"],
    ["Let's talk calmly", "ᱟᱞᱮ ᱟᱹᱭᱥᱛᱮ ᱨᱚᱲ ᱟᱞᱮ", "ale ayste ror ale"],
    ["Don't raise your voice", "ᱟᱢᱟᱜ ᱟᱣᱟᱡ ᱡᱷᱤᱡ ᱵᱚᱞᱚ ᱢᱮ", "amag awaj jhij bolo me"],
    ["I am sorry for what I said", "ᱤᱧ ᱨᱚᱲ ᱞᱟᱜᱤᱫ ᱢᱟᱹᱧᱡᱷᱤ", "inj ror lagid manjhi"],
    ["It was a misunderstanding", "ᱚᱱᱟ ᱢᱤᱫ ᱵᱷᱩᱞ ᱵᱩᱡᱷᱟᱹᱣ ᱛᱟᱦᱮᱸᱱ ᱟ", "ona mid bhul bujhaw taheny a"],
    ["We should not fight", "ᱟᱞᱮ ᱞᱟᱲᱟᱭ ᱵᱟᱝ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "ale laray bang lagid ale"],
    ["Fighting hurts everyone", "ᱞᱟᱲᱟᱭ ᱡᱚᱛᱚ ᱦᱚᱲ ᱠᱮ ᱰᱟᱦᱟ ᱮᱢ ᱟ", "laray joto hor ke daha em a"],
    ["Forgive me please", "ᱦᱮᱡ ᱤᱧ ᱠᱮ ᱢᱟᱹᱧ ᱢᱮ", "hej inj ke many me"],
    ["I forgive you", "ᱤᱧ ᱟᱢ ᱠᱮ ᱢᱟᱹᱧ ᱮᱱᱟ", "inj am ke many ena"],
    ["Let's not argue about this", "ᱱᱚᱣᱟ ᱵᱤᱥᱚᱭ ᱞᱟᱲᱟᱭ ᱡᱷᱤᱡ ᱟᱞᱮ", "nowa bisoy laray jhij ale"],
    ["Children get scared when we fight", "ᱟᱞᱮ ᱞᱟᱲᱟᱭ ᱵᱮᱞᱟ ᱜᱤᱫᱽᱨᱟᱹ ᱵᱚᱲ ᱠᱚ", "ale laray bela gidra bor ko"],
    ["We should solve problems peacefully", "ᱟᱞᱮ ᱢᱩᱥᱠᱤᱞ ᱥᱟᱸᱛᱤ ᱨᱮ ᱛᱷᱤᱨ ᱞᱟᱜᱤᱫ ᱟᱞᱮ", "ale muskil santi re thir lagid ale"],
    ["I will try to be more patient", "ᱤᱧ ᱟᱨ ᱫᱷᱤᱨᱚᱡ ᱛᱟᱦᱮᱸᱱ ᱪᱮᱥᱴᱟ ᱟ", "inj ar dhiroj taheny cesta a"],
    ["Family should stay united", "ᱯᱟᱹᱨᱤᱵᱟᱨ ᱮᱠᱛᱟ ᱛᱟᱦᱮᱸᱱ ᱞᱟᱜᱤᱫ ᱟ", "paribar ekta taheny lagid a"],
    ["Let's hug and make up", "ᱟᱞᱮ ᱜᱟᱞᱚᱡ ᱠᱮᱫ ᱵᱷᱟᱞᱮ ᱦᱩᱭ ᱟᱞᱮ", "ale galoj ked bhale huy ale"]
]

for ch in d:
    if ch['id'] in LESSONS:
        ch['blocks'] = [{"type": "table", "columns": ["English", "Santali (Ol Chiki)", "Transliteration"], "rows": LESSONS[ch['id']]}]

open('data_santali.json', 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('Section 5b (642-662) populated - 21 lessons')
