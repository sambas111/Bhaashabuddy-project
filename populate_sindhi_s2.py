import json

lessons = {}

lessons[510] = {
    "heading": "Pronouns and Articles in Sindhi",
    "rows": [
        ["I am here", "مان هتي آهيان", "Maan hite aahiyaan"],
        ["You are good", "توهان سٺا آهيو", "Tawhan suthaa aahiyo"],
        ["He is my friend", "هو منهنجو دوست آهي", "Hoo muhhinjo dost aahi"],
        ["She is my sister", "هوءَ منهنجي ڀيڻ آهي", "Hooa muhhinji bhain aahi"],
        ["We are students", "اسين شاگرد آهيون", "Aseen shaagird aahiyoon"],
        ["They are coming", "اهي اچي رهيا آهن", "Ahee achi rahiyaa aahan"],
        ["This is my book", "هي منهنجي ڪتاب آهي", "Hee muhhinji kitaab aahi"],
        ["That is your house", "اهو توهان جو گهر آهي", "Aho tawhan jo ghar aahi"],
        ["Who is he?", "هو ڪير آهي؟", "Hoo keer aahi?"],
        ["What is this?", "هي ڇا آهي؟", "Hee chhaa aahi?"],
        ["I am a teacher", "مان استاد آهيان", "Maan ustaad aahiyaan"],
        ["You are my brother", "توهان منهنجو ڀاءُ آهيو", "Tawhan muhhinjo bhaau aahiyo"],
        ["These are flowers", "هي گل آهن", "Hee gul aahan"],
        ["Those are trees", "اهي وڻ آهن", "Ahee wann aahan"],
        ["I am from Sindh", "مان سنڌ مان آهيان", "Maan Sindh maan aahiyaan"],
        ["She is a doctor", "هوءَ ڊاڪٽر آهي", "Hooa doctor aahi"],
        ["We are happy", "اسين خوش آهيون", "Aseen khush aahiyoon"],
        ["He is tall", "هو ڊگهو آهي", "Hoo ddagho aahi"],
    ]
}

lessons[511] = {
    "heading": "Using plurals to indicate respect in Sindhi",
    "rows": [
        ["You (respectful) are kind", "توهان مهربان آهيو", "Tawhan meherbaan aahiyo"],
        ["Please come (respectful)", "مهرباني ڪري اچو", "Meherbaani kari acho"],
        ["Please sit down", "مهرباني ڪري ويهي رهو", "Meherbaani kari weihi raho"],
        ["You (informal) are good", "تون سٺو آهين", "Toon sutho aahin"],
        ["Come here (informal)", "تون هتي اچ", "Toon hite ach"],
        ["Father is coming", "پيءُ اچي رهيو آهي", "Piyu achi rahiyo aahi"],
        ["Mother told us", "ماءُ اسان کي چيو", "Maau asaan khe chiyo"],
        ["Sir, please come", "صاحب، مهرباني ڪري اچو", "Sahib, meherbaani kari acho"],
        ["Madam, please sit", "بيگم صاحبه، مهرباني ڪري ويهي رهو", "Begum sahiba, meherbaani kari weihi raho"],
        ["Teacher told us to read", "استاد اسان کي پڙهڻ لاءِ چيو", "Ustaad asaan khe parhann laai chiyo"],
        ["They (respectful) have arrived", "اهي اچي ويا آهن", "Ahee achi wiyaa aahan"],
        ["Elder brother is at home", "وڏو ڀاءُ گهر ۾ آهي", "Waddo bhaau ghar me aahi"],
        ["Please tell me", "مهرباني ڪري مون کي ٻڌايو", "Meherbaani kari moon khe buddhaaio"],
        ["You (formal) are welcome", "توهان جي ڀلي ڪري آيا", "Tawhan ji bhali kari aayaa"],
        ["Grandfather is wise", "ڏاڏو عقلمند آهي", "Ddaado aqlmand aahi"],
        ["Grandmother told a story", "ڏاڏي ڪهاڻي ٻڌائي", "Ddaadi kahaani buddhaai"],
        ["Please forgive me", "مهرباني ڪري مون کي معاف ڪريو", "Meherbaani kari moon khe maaf kariyo"],
        ["Please have food", "مهرباني ڪري کاڌو کائو", "Meherbaani kari khaadho khaao"],
    ]
}

lessons[512] = {
    "heading": "Verbs in Sindhi",
    "rows": [
        ["I eat", "مان کائان ٿو", "Maan khaaiyaan tho"],
        ["You go", "توهان وڃو ٿا", "Tawhan wacho thaa"],
        ["He reads", "هو پڙهي ٿو", "Hoo parhi tho"],
        ["She writes", "هوءَ لکي ٿي", "Hooa likhi thee"],
        ["We play", "اسين کيڏون ٿا", "Aseen kheeddoon thaa"],
        ["They run", "اهي ڊوڙن ٿا", "Ahee ddoran thaa"],
        ["I drink water", "مان پاڻي پيئان ٿو", "Maan paani piyaan tho"],
        ["He sleeps", "هو سمهي ٿو", "Hoo sumhi tho"],
        ["She cooks food", "هوءَ کاڌو پچائي ٿي", "Hooa khaadho pachaai thee"],
        ["I speak Sindhi", "مان سنڌي ڳالهايان ٿو", "Maan Sindhi gaalhaaiyaan tho"],
        ["You listen carefully", "توهان غور سان ٻڌو ٿا", "Tawhan ghour saan budho thaa"],
        ["We study together", "اسين گڏجي پڙهون ٿا", "Aseen gadji parhoon thaa"],
        ["They sing songs", "اهي گيت ڳائين ٿا", "Ahee geet gaain thaa"],
        ["He works hard", "هو محنت ڪري ٿو", "Hoo mehnat kari tho"],
        ["She teaches children", "هوءَ ٻارن کي پڙهائي ٿي", "Hooa baarann khe parhaai thee"],
        ["I walk every day", "مان روز هلان ٿو", "Maan roz halaan tho"],
        ["You sit here", "توهان هتي ويهو ٿا", "Tawhan hite weiho thaa"],
        ["They dance at weddings", "اهي شاديءَ تي ناچين ٿا", "Ahee shaadiya ti naacheen thaa"],
    ]
}

lessons[513] = {
    "heading": "Simple Present Tense in Sindhi",
    "rows": [
        ["I go to school", "مان اسڪول وڃان ٿو", "Maan school wachaan tho"],
        ["He eats food", "هو کاڌو کائي ٿو", "Hoo khaadho khaai tho"],
        ["She reads books", "هوءَ ڪتابون پڙهي ٿي", "Hooa kitaaboon parhi thee"],
        ["We drink milk", "اسين کير پيئون ٿا", "Aseen kheer piyoon thaa"],
        ["They work in the field", "اهي کيت ۾ ڪم ڪن ٿا", "Ahee khet me kam kan thaa"],
        ["I write letters", "مان خط لکان ٿو", "Maan khat likhaan tho"],
        ["You speak the truth", "توهان سچ ڳالهايو ٿا", "Tawhan sach gaalhaaio thaa"],
        ["He teaches well", "هو سٺي طرح پڙهائي ٿو", "Hoo suthi tarah parhaai tho"],
        ["She sings beautifully", "هوءَ سهڻو ڳائي ٿي", "Hooa suhno gaai thee"],
        ["We live in this city", "اسين هن شهر ۾ رهون ٿا", "Aseen han shahar me rahoon thaa"],
        ["They play cricket", "اهي ڪرڪيٽ کيڏين ٿا", "Ahee cricket kheddeen thaa"],
        ["I love my country", "مان پنهنجي ملڪ سان پيار ڪيان ٿو", "Maan panhinji mulk saan pyaar kiyaan tho"],
        ["He comes every day", "هو روز اچي ٿو", "Hoo roz achi tho"],
        ["She helps everyone", "هوءَ سڀني جي مدد ڪري ٿي", "Hooa sabhni ji madad kari thee"],
        ["We understand Sindhi", "اسين سنڌي سمجهون ٿا", "Aseen Sindhi samjhoon thaa"],
        ["They sell fruits", "اهي ميوا وڪرين ٿا", "Ahee mewaa wikreen thaa"],
        ["I cook dinner", "مان رات جو کاڌو پچايان ٿو", "Maan raat jo khaadho pachaiyaan tho"],
        ["You study hard", "توهان محنت سان پڙهو ٿا", "Tawhan mehnat saan parho thaa"],
    ]
}

lessons[514] = {
    "heading": "Simple Present Tense of 'To Be' in Sindhi",
    "rows": [
        ["I am a student", "مان شاگرد آهيان", "Maan shaagird aahiyaan"],
        ["You are my friend", "توهان منهنجو دوست آهيو", "Tawhan muhhinjo dost aahiyo"],
        ["He is a doctor", "هو ڊاڪٽر آهي", "Hoo doctor aahi"],
        ["She is beautiful", "هوءَ سهڻي آهي", "Hooa suhni aahi"],
        ["We are teachers", "اسين استاد آهيون", "Aseen ustaad aahiyoon"],
        ["They are farmers", "اهي هاري آهن", "Ahee haari aahan"],
        ["This is a pen", "هي قلم آهي", "Hee qalam aahi"],
        ["That is a table", "اهو ميز آهي", "Aho mez aahi"],
        ["The weather is good", "موسم سٺو آهي", "Mosam sutho aahi"],
        ["The food is ready", "کاڌو تيار آهي", "Khaadho tayyaar aahi"],
        ["I am happy today", "مان اڄ خوش آهيان", "Maan aaj khush aahiyaan"],
        ["He is at home", "هو گهر ۾ آهي", "Hoo ghar me aahi"],
        ["She is in the garden", "هوءَ باغ ۾ آهي", "Hooa baagh me aahi"],
        ["We are ready", "اسين تيار آهيون", "Aseen tayyaar aahiyoon"],
        ["They are busy", "اهي مصروف آهن", "Ahee masroof aahan"],
        ["The book is on the table", "ڪتاب ميز تي آهي", "Kitaab mez te aahi"],
        ["It is cold today", "اڄ ٿڌ آهي", "Aaj thadh aahi"],
        ["You are right", "توهان صحيح آهيو", "Tawhan sahih aahiyo"],
    ]
}

lessons[515] = {
    "heading": "Present Continuous Tense in Sindhi",
    "rows": [
        ["I am eating", "مان کائي رهيو آهيان", "Maan khaai rahiyo aahiyaan"],
        ["He is reading", "هو پڙهي رهيو آهي", "Hoo parhi rahiyo aahi"],
        ["She is cooking", "هوءَ پچائي رهي آهي", "Hooa pachaai rahi aahi"],
        ["We are playing", "اسين کيڏي رهيا آهيون", "Aseen kheddi rahiyaa aahiyoon"],
        ["They are studying", "اهي پڙهي رهيا آهن", "Ahee parhi rahiyaa aahan"],
        ["I am going to market", "مان بازار وڃي رهيو آهيان", "Maan bazaar wachi rahiyo aahiyaan"],
        ["He is writing a letter", "هو خط لکي رهيو آهي", "Hoo khat likhi rahiyo aahi"],
        ["She is singing a song", "هوءَ گيت ڳائي رهي آهي", "Hooa geet gaai rahi aahi"],
        ["We are watching TV", "اسين ٽي وي ڏسي رهيا آهيون", "Aseen TV disi rahiyaa aahiyoon"],
        ["They are working", "اهي ڪم ڪري رهيا آهن", "Ahee kam kari rahiyaa aahan"],
        ["I am drinking tea", "مان چانهه پي رهيو آهيان", "Maan chaanhh pi rahiyo aahiyaan"],
        ["He is running fast", "هو تيز ڊوڙي رهيو آهي", "Hoo tez ddori rahiyo aahi"],
        ["She is teaching", "هوءَ پڙهائي رهي آهي", "Hooa parhaai rahi aahi"],
        ["We are learning Sindhi", "اسين سنڌي سکي رهيا آهيون", "Aseen Sindhi sikhi rahiyaa aahiyoon"],
        ["They are sleeping", "اهي سمهي رهيا آهن", "Ahee sumhi rahiyaa aahan"],
        ["I am waiting for you", "مان توهان جو انتظار ڪري رهيو آهيان", "Maan tawhan jo intezaar kari rahiyo aahiyaan"],
        ["He is talking on phone", "هو فون تي ڳالهائي رهيو آهي", "Hoo phone te gaalhaayi rahiyo aahi"],
        ["She is dancing", "هوءَ ناچي رهي آهي", "Hooa naachi rahi aahi"],
    ]
}

lessons[516] = {
    "heading": "Simple Future Tense in Sindhi",
    "rows": [
        ["I will go tomorrow", "مان سڀاڻي ويندس", "Maan sabhaani windas"],
        ["He will come", "هو ايندو", "Hoo aindo"],
        ["She will cook food", "هوءَ کاڌو پچائيندي", "Hooa khaadho pachaindi"],
        ["We will study", "اسين پڙهنداسين", "Aseen parhandaasin"],
        ["They will play", "اهي کيڏندا", "Ahee kheddandaa"],
        ["I will write a letter", "مان خط لکندس", "Maan khat likhandas"],
        ["He will read the book", "هو ڪتاب پڙهندو", "Hoo kitaab parhando"],
        ["She will sing", "هوءَ ڳائيندي", "Hooa gaaindi"],
        ["We will win the match", "اسين ميچ کٽنداسين", "Aseen match khatandaasin"],
        ["They will help us", "اهي اسان جي مدد ڪندا", "Ahee asaan ji madad kandaa"],
        ["I will learn Sindhi", "مان سنڌي سکندس", "Maan Sindhi sikhandas"],
        ["You will understand", "توهان سمجهندؤ", "Tawhan samjhandau"],
        ["He will work hard", "هو محنت ڪندو", "Hoo mehnat kando"],
        ["She will teach us", "هوءَ اسان کي پڙهائيندي", "Hooa asaan khe parhaindi"],
        ["We will go to the temple", "اسين مندر ويندا سين", "Aseen mandir windaa sin"],
        ["They will return home", "اهي گهر واپس ايندا", "Ahee ghar waapas aindaa"],
        ["I will buy vegetables", "مان ڀاڄيون خريد ڪندس", "Maan bhaajiyoon khareed kandas"],
        ["He will call you", "هو توهان کي فون ڪندو", "Hoo tawhan khe phone kando"],
    ]
}

lessons[517] = {
    "heading": "Future Continuous Tense in Sindhi",
    "rows": [
        ["I will be going", "مان وڃي رهيو هوندس", "Maan wachi rahiyo hondas"],
        ["He will be reading", "هو پڙهي رهيو هوندو", "Hoo parhi rahiyo hondo"],
        ["She will be cooking", "هوءَ پچائي رهي هوندي", "Hooa pachaai rahi hondi"],
        ["We will be studying", "اسين پڙهي رهيا هونداسين", "Aseen parhi rahiyaa hondaasin"],
        ["They will be playing", "اهي کيڏي رهيا هوندا", "Ahee kheddi rahiyaa hondaa"],
        ["I will be waiting", "مان انتظار ڪري رهيو هوندس", "Maan intezaar kari rahiyo hondas"],
        ["He will be working", "هو ڪم ڪري رهيو هوندو", "Hoo kam kari rahiyo hondo"],
        ["She will be singing", "هوءَ ڳائي رهي هوندي", "Hooa gaai rahi hondi"],
        ["We will be traveling", "اسين سفر ڪري رهيا هونداسين", "Aseen safar kari rahiyaa hondaasin"],
        ["They will be sleeping", "اهي سمهي رهيا هوندا", "Ahee sumhi rahiyaa hondaa"],
        ["I will be eating at that time", "مان ان وقت کائي رهيو هوندس", "Maan un waqt khaai rahiyo hondas"],
        ["He will be running", "هو ڊوڙي رهيو هوندو", "Hoo ddori rahiyo hondo"],
        ["She will be teaching", "هوءَ پڙهائي رهي هوندي", "Hooa parhaai rahi hondi"],
        ["We will be watching the game", "اسين راند ڏسي رهيا هونداسين", "Aseen raand disi rahiyaa hondaasin"],
        ["They will be dancing", "اهي ناچي رهيا هوندا", "Ahee naachi rahiyaa hondaa"],
        ["I will be driving", "مان ڳاڏي هلائي رهيو هوندس", "Maan gaadi halaai rahiyo hondas"],
        ["He will be writing", "هو لکي رهيو هوندو", "Hoo likhi rahiyo hondo"],
        ["She will be listening to music", "هوءَ موسيقي ٻڌي رهي هوندي", "Hooa moseeqi budhi rahi hondi"],
    ]
}

lessons[518] = {
    "heading": "Simple Past Tense in Sindhi – Part 1 (Verbs without object)",
    "rows": [
        ["I went", "مان ويس", "Maan wis"],
        ["He came", "هو آيو", "Hoo aayo"],
        ["She ran", "هوءَ ڊوڙي", "Hooa ddori"],
        ["We sat", "اسين ويٺا سين", "Aseen weithaa sin"],
        ["They slept", "اهي سمهي ويا", "Ahee sumhi wiyaa"],
        ["I walked", "مان هليس", "Maan halis"],
        ["He stood up", "هو بيٺو ٿيو", "Hoo bethho thiyo"],
        ["She cried", "هوءَ رُئي", "Hooa rui"],
        ["We laughed", "اسين هنسيا سين", "Aseen hansiyaa sin"],
        ["They danced", "اهي ناچيا", "Ahee naachiyaa"],
        ["I fell down", "مان ڪري پيس", "Maan kari pis"],
        ["He swam", "هو ترنو ڪيائين", "Hoo tarano kiyaaeen"],
        ["She sang", "هوءَ ڳايو", "Hooa gaaio"],
        ["We played", "اسين کيڏيا سين", "Aseen kheddiyaa sin"],
        ["They returned", "اهي واپس آيا", "Ahee waapas aayaa"],
        ["I reached home", "مان گهر پهتس", "Maan ghar pahutas"],
        ["He woke up early", "هو جلدي اُٿيو", "Hoo jaldi uthiyo"],
        ["She spoke", "هوءَ ڳالهايو", "Hooa gaalhaaio"],
    ]
}

lessons[519] = {
    "heading": "Simple Past Tense in Sindhi – Part 2 (Verbs with object)",
    "rows": [
        ["I ate food", "مون کاڌو کاڌو", "Moon khaadho khaadho"],
        ["He read the book", "هن ڪتاب پڙهي", "Hun kitaab parhi"],
        ["She wrote a letter", "هنيءَ خط لکيو", "Huniya khat likhiyo"],
        ["We drank milk", "اسان کير پيئي", "Asaan kheer piyi"],
        ["They bought vegetables", "انهن ڀاڄيون خريد ڪيون", "Unhan bhaajiyoon khareed kiyoon"],
        ["I saw the movie", "مون فلم ڏٺي", "Moon film ddithi"],
        ["He gave money", "هن پئسا ڏنا", "Hun paisa ddina"],
        ["She cooked rice", "هنيءَ چانور پچايا", "Huniya chaanwar pachaiyaa"],
        ["We sold the house", "اسان گهر وڪرو", "Asaan ghar wikro"],
        ["They heard the news", "انهن خبر ٻڌي", "Unhan khabar buddhi"],
        ["I opened the door", "مون دروازو کوليو", "Moon darwaazo kholiyo"],
        ["He closed the window", "هن دري بند ڪئي", "Hun dari band kai"],
        ["She made tea", "هنيءَ چانهه ٺاهي", "Huniya chaanhh thaahi"],
        ["We planted a tree", "اسان وڻ لڳايو", "Asaan wann lagaaio"],
        ["They washed clothes", "انهن ڪپڙا ڌوئا", "Unhan kapra dhoiyaa"],
        ["I caught the ball", "مون بال پڪڙيو", "Moon ball pakarriyo"],
        ["He broke the glass", "هن گلاس ڀڃيو", "Hun glass bhaajiyo"],
        ["She found the key", "هنيءَ چاٻي ڳولي", "Huniya chaabi ggoli"],
    ]
}

lessons[520] = {
    "heading": "Simple Past Tense – Past tense of 'to be' in Sindhi",
    "rows": [
        ["I was a student", "مان شاگرد هئس", "Maan shaagird huas"],
        ["You were here", "توهان هتي هئا", "Tawhan hite huaa"],
        ["He was a doctor", "هو ڊاڪٽر هو", "Hoo doctor ho"],
        ["She was happy", "هوءَ خوش هئي", "Hooa khush hui"],
        ["We were at home", "اسين گهر ۾ هئاسين", "Aseen ghar me huaasin"],
        ["They were tired", "اهي ٿڪل هئا", "Ahee thakal huaa"],
        ["The weather was good", "موسم سٺو هو", "Mosam sutho ho"],
        ["The food was delicious", "کاڌو مزيدار هو", "Khaadho mazidaar ho"],
        ["I was sick yesterday", "مان ڪالهه بيمار هئس", "Maan kaalh beemaar huas"],
        ["He was in the market", "هو بازار ۾ هو", "Hoo bazaar me ho"],
        ["She was a teacher before", "هوءَ پهريان استاد هئي", "Hooa pahriyaan ustaad hui"],
        ["We were friends", "اسين دوست هئاسين", "Aseen dost huaasin"],
        ["They were busy", "اهي مصروف هئا", "Ahee masroof huaa"],
        ["It was raining", "مينهن پئي رهيو هو", "Meenhan paee rahiyo ho"],
        ["The book was on the table", "ڪتاب ميز تي هئي", "Kitaab mez te hui"],
        ["I was waiting for you", "مان توهان جو انتظار ڪري رهيو هئس", "Maan tawhan jo intezaar kari rahiyo huas"],
        ["He was sleeping", "هو سمهي رهيو هو", "Hoo sumhi rahiyo ho"],
        ["She was cooking food", "هوءَ کاڌو پچائي رهي هئي", "Hooa khaadho pachaai rahi hui"],
    ]
}

lessons[521] = {
    "heading": "Exceptional Verbs in Sindhi which change in past tense",
    "rows": [
        ["I went (go → ويس)", "مان ويس", "Maan wis"],
        ["He came (come → آيو)", "هو آيو", "Hoo aayo"],
        ["She gave (give → ڏنو)", "هنيءَ ڏنو", "Huniya ddino"],
        ["We took (take → ورتو)", "اسان ورتو", "Asaan warto"],
        ["They did (do → ڪيو)", "انهن ڪيو", "Unhan kiyo"],
        ["I said (say → چيو)", "مون چيو", "Moon chiyo"],
        ["He saw (see → ڏٺو)", "هن ڏٺو", "Hun dditho"],
        ["She heard (hear → ٻڌو)", "هنيءَ ٻڌو", "Huniya buddho"],
        ["We ate (eat → کاڌو)", "اسان کاڌو", "Asaan khaadho"],
        ["They drank (drink → پيئي)", "انهن پيئي", "Unhan piyi"],
        ["I was (be → هئس)", "مان هئس", "Maan huas"],
        ["He sat (sit → ويٺو)", "هو ويٺو", "Hoo weitho"],
        ["She stood (stand → بيٺي)", "هوءَ بيٺي", "Hooa bethi"],
        ["We slept (sleep → سمهيا)", "اسين سمهيا سين", "Aseen sumhiyaa sin"],
        ["They ran (run → ڊوڙيا)", "اهي ڊوڙيا", "Ahee ddoriyaa"],
        ["I bought (buy → خريد ڪيو)", "مون خريد ڪيو", "Moon khareed kiyo"],
        ["He sold (sell → وڪرو)", "هن وڪرو", "Hun wikro"],
        ["She died (die → مري وئي)", "هوءَ مري وئي", "Hooa mari wai"],
    ]
}

lessons[522] = {
    "heading": "Past Continuous Tense in Sindhi",
    "rows": [
        ["I was eating", "مان کائي رهيو هئس", "Maan khaai rahiyo huas"],
        ["He was reading", "هو پڙهي رهيو هو", "Hoo parhi rahiyo ho"],
        ["She was cooking", "هوءَ پچائي رهي هئي", "Hooa pachaai rahi hui"],
        ["We were playing", "اسين کيڏي رهيا هئاسين", "Aseen kheddi rahiyaa huaasin"],
        ["They were studying", "اهي پڙهي رهيا هئا", "Ahee parhi rahiyaa huaa"],
        ["I was going to market", "مان بازار وڃي رهيو هئس", "Maan bazaar wachi rahiyo huas"],
        ["He was writing", "هو لکي رهيو هو", "Hoo likhi rahiyo ho"],
        ["She was singing", "هوءَ ڳائي رهي هئي", "Hooa gaai rahi hui"],
        ["We were watching", "اسين ڏسي رهيا هئاسين", "Aseen disi rahiyaa huaasin"],
        ["They were sleeping", "اهي سمهي رهيا هئا", "Ahee sumhi rahiyaa huaa"],
        ["I was waiting for bus", "مان بس جو انتظار ڪري رهيو هئس", "Maan bus jo intezaar kari rahiyo huas"],
        ["He was talking on phone", "هو فون تي ڳالهائي رهيو هو", "Hoo phone te gaalhaayi rahiyo ho"],
        ["She was dancing", "هوءَ ناچي رهي هئي", "Hooa naachi rahi hui"],
        ["We were working hard", "اسين محنت ڪري رهيا هئاسين", "Aseen mehnat kari rahiyaa huaasin"],
        ["They were running", "اهي ڊوڙي رهيا هئا", "Ahee ddori rahiyaa huaa"],
        ["I was learning Sindhi", "مان سنڌي سکي رهيو هئس", "Maan Sindhi sikhi rahiyo huas"],
        ["He was driving", "هو ڳاڏي هلائي رهيو هو", "Hoo gaadi halaai rahiyo ho"],
        ["She was teaching", "هوءَ پڙهائي رهي هئي", "Hooa parhaai rahi hui"],
    ]
}

lessons[523] = {
    "heading": "Present/Past/Future Perfect Tense in Sindhi",
    "rows": [
        ["I have eaten", "مان کائي چڪو آهيان", "Maan khaai chuko aahiyaan"],
        ["He has read the book", "هو ڪتاب پڙهي چڪو آهي", "Hoo kitaab parhi chuko aahi"],
        ["She has cooked food", "هوءَ کاڌو پچائي چڪي آهي", "Hooa khaadho pachaai chuki aahi"],
        ["We have finished work", "اسين ڪم ختم ڪري چڪا آهيون", "Aseen kam khatam kari chukaa aahiyoon"],
        ["They have gone home", "اهي گهر وڃي چڪا آهن", "Ahee ghar wachi chukaa aahan"],
        ["I had already eaten", "مان اڳ ۾ ئي کائي چڪو هئس", "Maan agg me ee khaai chuko huas"],
        ["He had already left", "هو اڳ ۾ ئي هلي ويو هو", "Hoo agg me ee hali wiyo ho"],
        ["She had already slept", "هوءَ اڳ ۾ ئي سمهي وئي هئي", "Hooa agg me ee sumhi wai hui"],
        ["We had already finished", "اسين اڳ ۾ ئي ختم ڪري چڪا هئاسين", "Aseen agg me ee khatam kari chukaa huaasin"],
        ["They had already arrived", "اهي اڳ ۾ ئي اچي چڪا هئا", "Ahee agg me ee achi chukaa huaa"],
        ["I will have finished by then", "مان ان وقت تائين ختم ڪري چڪندس", "Maan un waqt taaeen khatam kari chukandas"],
        ["He will have returned", "هو واپس اچي چڪندو", "Hoo waapas achi chukando"],
        ["She will have cooked", "هوءَ پچائي چڪندي", "Hooa pachaai chukandi"],
        ["We will have studied", "اسين پڙهي چڪنداسين", "Aseen parhi chukandaasin"],
        ["They will have left", "اهي هلي وڃي چڪندا", "Ahee hali wachi chukandaa"],
        ["I have seen that movie", "مان اها فلم ڏسي چڪو آهيان", "Maan ahaa film disi chuko aahiyaan"],
        ["He has written the letter", "هو خط لکي چڪو آهي", "Hoo khat likhi chuko aahi"],
        ["She has learned Sindhi", "هوءَ سنڌي سکي چڪي آهي", "Hooa Sindhi sikhi chuki aahi"],
    ]
}

lessons[524] = {
    "heading": "Learn Prepositions in Sindhi",
    "rows": [
        ["The book is on the table", "ڪتاب ميز تي آهي", "Kitaab mez te aahi"],
        ["The cat is under the chair", "ٻلي ڪرسي هيٺ آهي", "Billi kursi heth aahi"],
        ["He is in the room", "هو ڪمري ۾ آهي", "Hoo kamre me aahi"],
        ["She is near the door", "هوءَ دروازي ويجهو آهي", "Hooa darwaazi wejho aahi"],
        ["We are in front of the house", "اسين گهر جي اڳيان آهيون", "Aseen ghar ji aggiyaan aahiyoon"],
        ["They are behind the wall", "اهي ديوار جي پويان آهن", "Ahee deewaar ji poyaan aahan"],
        ["The shop is between the bank and school", "دڪان بئنڪ ۽ اسڪول جي وچ ۾ آهي", "Dukaan bank ain school ji wach me aahi"],
        ["He walked along the river", "هو ندي سان گڏ هليو", "Hoo nadi saan gadd haliyo"],
        ["She sat beside me", "هوءَ منهنجي ڀرسان ويٺي", "Hooa muhhinji bharsaan weithi"],
        ["Go towards the market", "بازار طرف وڃو", "Bazaar taraf wacho"],
        ["He came from school", "هو اسڪول مان آيو", "Hoo school maan aayo"],
        ["She went to the garden", "هوءَ باغ ڏانهن وئي", "Hooa baagh ddaanhan wai"],
        ["The ball is above the cupboard", "بال الماري مٿي آهي", "Ball almaari mathi aahi"],
        ["Come with me", "منهنجي سان اچو", "Muhhinji saan acho"],
        ["He is outside the house", "هو گهر جي ٻاهر آهي", "Hoo ghar ji baahar aahi"],
        ["She is inside the room", "هوءَ ڪمري جي اندر آهي", "Hooa kamre ji andar aahi"],
        ["Walk around the garden", "باغ جي چوڌاري هلو", "Baagh ji chaudhaari halo"],
        ["We will meet after lunch", "اسين ماني کان پوءِ ملنداسين", "Aseen maani khaan poee milandaasin"],
    ]
}

lessons[525] = {
    "heading": "Preposition 'TO' in Sindhi",
    "rows": [
        ["I go to school", "مان اسڪول وڃان ٿو", "Maan school wachaan tho"],
        ["He went to the market", "هو بازار ويو", "Hoo bazaar wiyo"],
        ["She came to my house", "هوءَ منهنجي گهر آئي", "Hooa muhhinji ghar aai"],
        ["Give this to him", "هي هن کي ڏيو", "Hee hun khe diyo"],
        ["Talk to the teacher", "استاد سان ڳالهايو", "Ustaad saan gaalhaaio"],
        ["I gave the book to her", "مون ڪتاب هنيءَ کي ڏني", "Moon kitaab huniya khe ddini"],
        ["We went to the temple", "اسين مندر ويا سين", "Aseen mandir wiyaa sin"],
        ["They came to our village", "اهي اسان جي ڳوٺ آيا", "Ahee asaan ji ggoth aayaa"],
        ["Write a letter to your friend", "پنهنجي دوست کي خط لکو", "Panhinji dost khe khat likho"],
        ["She listened to the song", "هنيءَ گيت ٻڌو", "Huniya geet buddho"],
        ["He spoke to the principal", "هن پرنسپال سان ڳالهايو", "Hun principal saan gaalhaaio"],
        ["I went to the doctor", "مان ڊاڪٽر وٽ ويس", "Maan doctor watt wis"],
        ["She went to her mother", "هوءَ پنهنجي ماءُ وٽ وئي", "Hooa panhinji maau watt wai"],
        ["Take this to the kitchen", "هي رسوئيخاني ۾ وٺي وڃو", "Hee rasoi khaani me wuthi wacho"],
        ["Send the letter to the office", "خط آفيس ڏانهن موڪليو", "Khat office ddaanhan mokliyo"],
        ["Go to the right", "ساڄي طرف وڃو", "Saaji taraf wacho"],
        ["Come to the garden", "باغ ۾ اچو", "Baagh me acho"],
        ["I will go to Karachi", "مان ڪراچي ويندس", "Maan Karachi windas"],
    ]
}

lessons[526] = {
    "heading": "Sentences with person or living things as object in Sindhi",
    "rows": [
        ["I saw him", "مون هن کي ڏٺو", "Moon hun khe dditho"],
        ["She called me", "هنيءَ مون کي سڏيو", "Huniya moon khe sadiyo"],
        ["He helped his friend", "هن پنهنجي دوست جي مدد ڪئي", "Hun panhinji dost ji madad kai"],
        ["We met the teacher", "اسان استاد سان مليا سين", "Asaan ustaad saan miliyaa sin"],
        ["They brought the child", "انهن ٻار کي آندو", "Unhan baar khe aando"],
        ["I told my mother", "مون پنهنجي ماءُ کي ٻڌايو", "Moon panhinji maau khe buddhaaio"],
        ["She loves her brother", "هوءَ پنهنجي ڀاءُ سان پيار ڪري ٿي", "Hooa panhinji bhaau saan pyaar kari thee"],
        ["He teaches children", "هو ٻارن کي پڙهائي ٿو", "Hoo baarann khe parhaai tho"],
        ["We invited our neighbors", "اسان پنهنجن پاڙيسرين کي سڏيو", "Asaan panhinjan paarisareen khe sadiyo"],
        ["They praised the player", "انهن رانديگر جي ساراهه ڪئي", "Unhan raandigir ji saaraah kai"],
        ["I sent my brother", "مون پنهنجي ڀاءُ کي موڪليو", "Moon panhinji bhaau khe mokliyo"],
        ["She asked her father", "هنيءَ پنهنجي پيءُ کان پڇيو", "Huniya panhinji piyu khaan puchiyo"],
        ["He recognized the man", "هن ماڻهوءَ کي سڃاتو", "Hun maanhuya khe sanjaato"],
        ["We thanked the doctor", "اسان ڊاڪٽر جي مهرباني ڪيائين", "Asaan doctor ji meherbaani kiyaaeen"],
        ["They forgave the boy", "انهن ڇوڪري کي معاف ڪيو", "Unhan chhokri khe maaf kiyo"],
        ["I greeted my grandfather", "مون پنهنجي ڏاڏي کي سلام ڪيو", "Moon panhinji ddaadi khe salaam kiyo"],
        ["She visited her aunt", "هوءَ پنهنجي خالي وٽ وئي", "Hooa panhinji khaali watt wai"],
        ["He followed the guide", "هو گائيڊ جي پٺيان هليو", "Hoo guide ji pathiyaan haliyo"],
    ]
}

lessons[527] = {
    "heading": "Saying My/His/Her in Sindhi",
    "rows": [
        ["My house", "منهنجو گهر", "Muhhinjo ghar"],
        ["Your book", "توهان جي ڪتاب", "Tawhan ji kitaab"],
        ["His car", "هن جي ڪار", "Hun ji kaar"],
        ["Her name", "هنيءَ جو نالو", "Huniya jo naalo"],
        ["Our school", "اسان جو اسڪول", "Asaan jo school"],
        ["Their village", "انهن جو ڳوٺ", "Unhan jo ggoth"],
        ["My mother is kind", "منهنجي ماءُ مهربان آهي", "Muhhinji maau meherbaan aahi"],
        ["His father is a farmer", "هن جو پيءُ هاري آهي", "Hun jo piyu haari aahi"],
        ["Her brother is a doctor", "هنيءَ جو ڀاءُ ڊاڪٽر آهي", "Huniya jo bhaau doctor aahi"],
        ["Our teacher is strict", "اسان جو استاد سخت آهي", "Asaan jo ustaad sakht aahi"],
        ["Their house is big", "انهن جو گهر وڏو آهي", "Unhan jo ghar waddo aahi"],
        ["My friend's name is Ali", "منهنجي دوست جو نالو علي آهي", "Muhhinji dost jo naalo Ali aahi"],
        ["Your country is beautiful", "توهان جو ملڪ سهڻو آهي", "Tawhan jo mulk suhno aahi"],
        ["His work is done", "هن جو ڪم ٿي ويو", "Hun jo kam thi wiyo"],
        ["Her dream is to be a teacher", "هنيءَ جو خواب استاد ٿيڻ آهي", "Huniya jo khwaab ustaad thinn aahi"],
        ["Our garden has flowers", "اسان جي باغ ۾ گل آهن", "Asaan ji baagh me gul aahan"],
        ["Their children study well", "انهن جا ٻار سٺي طرح پڙهن ٿا", "Unhan jaa baar suthi tarah parhan thaa"],
        ["My eyes are tired", "منهنجيون اکيون ٿڪل آهن", "Muhhinjiyoon akhiyoon thakal aahan"],
    ]
}

lessons[528] = {
    "heading": "Basic questions and 'WH' questions in Sindhi",
    "rows": [
        ["What is this?", "هي ڇا آهي؟", "Hee chhaa aahi?"],
        ["Who are you?", "توهان ڪير آهيو؟", "Tawhan keer aahiyo?"],
        ["Where do you live?", "توهان ڪٿي رهو ٿا؟", "Tawhan kithe raho thaa?"],
        ["When will you come?", "توهان ڪڏهن ايندؤ؟", "Tawhan kadhan aindau?"],
        ["Why are you late?", "توهان دير سان ڇو آيا؟", "Tawhan der saan chho aayaa?"],
        ["How are you?", "توهان ڪيئن آهيو؟", "Tawhan kiyan aahiyo?"],
        ["Which book do you want?", "توهان ڪهڙي ڪتاب چاهيو ٿا؟", "Tawhan kahri kitaab chaahiyo thaa?"],
        ["Whose pen is this?", "هي ڪنهن جو قلم آهي؟", "Hee kunhan jo qalam aahi?"],
        ["How much does it cost?", "هن جي قيمت ڪيتري آهي؟", "Hun ji qeemat kitri aahi?"],
        ["How many people came?", "ڪيترا ماڻهو آيا؟", "Kitraa maanho aayaa?"],
        ["What time is it?", "ڪيترا وڳا ٿيا آهن؟", "Kitraa waga thiyaa aahan?"],
        ["Where is the hospital?", "اسپتال ڪٿي آهي؟", "Aspataal kithe aahi?"],
        ["Why did you go?", "توهان ڇو ويا؟", "Tawhan chho wiyaa?"],
        ["How do you do this?", "توهان هي ڪيئن ڪريو ٿا؟", "Tawhan hee kiyan kariyo thaa?"],
        ["Which way should I go?", "مون ڪهڙي رستي وڃڻ گهرجي؟", "Moon kahri raste wachann ghuruji?"],
        ["Who told you?", "توهان کي ڪنهن ٻڌايو؟", "Tawhan khe kunhan buddhaaio?"],
        ["What happened?", "ڇا ٿيو؟", "Chhaa thiyo?"],
        ["When did he leave?", "هو ڪڏهن هليو ويو؟", "Hoo kadhan haliyo wiyo?"],
    ]
}

lessons[529] = {
    "heading": "Negative Sentences – Present tense in Sindhi",
    "rows": [
        ["I do not go", "مان نٿو وڃان", "Maan natho wachaan"],
        ["He does not eat", "هو نٿو کائي", "Hoo natho khaai"],
        ["She does not read", "هوءَ نٿي پڙهي", "Hooa nathi parhi"],
        ["We do not play", "اسين نٿا کيڏون", "Aseen nathaa kheddoon"],
        ["They do not come", "اهي نٿا اچن", "Ahee nathaa achan"],
        ["I do not like this", "مون کي هي پسند ناهي", "Moon khe hee pasand naahi"],
        ["He does not speak Sindhi", "هو سنڌي نٿو ڳالهائي", "Hoo Sindhi natho gaalhaayi"],
        ["She does not cook", "هوءَ نٿي پچائي", "Hooa nathi pachaai"],
        ["We do not understand", "اسين نٿا سمجهون", "Aseen nathaa samjhoon"],
        ["They do not study", "اهي نٿا پڙهن", "Ahee nathaa parhan"],
        ["I am not a teacher", "مان استاد ناهيان", "Maan ustaad naahiyaan"],
        ["He is not here", "هو هتي ناهي", "Hoo hite naahi"],
        ["She is not happy", "هوءَ خوش ناهي", "Hooa khush naahi"],
        ["We are not ready", "اسين تيار ناهيون", "Aseen tayyaar naahiyoon"],
        ["They are not tired", "اهي ٿڪل ناهن", "Ahee thakal naahan"],
        ["I do not want tea", "مون کي چانهه نه گهرجي", "Moon khe chaanhh na ghuruji"],
        ["He does not know", "هو نٿو ڄاڻي", "Hoo natho jaani"],
        ["This is not correct", "هي صحيح ناهي", "Hee sahih naahi"],
    ]
}

lessons[530] = {
    "heading": "Negative Sentences – Past tense in Sindhi",
    "rows": [
        ["I did not go", "مان نه ويس", "Maan na wis"],
        ["He did not come", "هو نه آيو", "Hoo na aayo"],
        ["She did not eat", "هنيءَ نه کاڌو", "Huniya na khaadho"],
        ["We did not play", "اسين نه کيڏيا سين", "Aseen na kheddiyaa sin"],
        ["They did not study", "انهن نه پڙهيو", "Unhan na parhiyo"],
        ["I did not see him", "مون هن کي نه ڏٺو", "Moon hun khe na dditho"],
        ["He did not write the letter", "هن خط نه لکيو", "Hun khat na likhiyo"],
        ["She did not cook today", "هنيءَ اڄ نه پچايو", "Huniya aaj na pachaaiyo"],
        ["We did not hear the news", "اسان خبر نه ٻڌي", "Asaan khabar na buddhi"],
        ["They did not help", "انهن مدد نه ڪئي", "Unhan madad na kai"],
        ["I was not at home", "مان گهر ۾ نه هئس", "Maan ghar me na huas"],
        ["He was not sleeping", "هو نه سمهي رهيو هو", "Hoo na sumhi rahiyo ho"],
        ["She was not there", "هوءَ اتي نه هئي", "Hooa ute na hui"],
        ["We were not late", "اسين دير سان نه هئاسين", "Aseen der saan na huaasin"],
        ["They did not bring anything", "انهن ڪجهه نه آندو", "Unhan kujh na aando"],
        ["I did not say that", "مون اهو نه چيو", "Moon aho na chiyo"],
        ["He did not buy the book", "هن ڪتاب خريد نه ڪئي", "Hun kitaab khareed na kai"],
        ["She did not call me", "هنيءَ مون کي نه سڏيو", "Huniya moon khe na sadiyo"],
    ]
}

lessons[531] = {
    "heading": "Negative Sentence – Future Tense in Sindhi",
    "rows": [
        ["I will not go", "مان نه ويندس", "Maan na windas"],
        ["He will not come", "هو نه ايندو", "Hoo na aindo"],
        ["She will not cook", "هوءَ نه پچائيندي", "Hooa na pachaindi"],
        ["We will not study tomorrow", "اسين سڀاڻي نه پڙهنداسين", "Aseen sabhaani na parhandaasin"],
        ["They will not play", "اهي نه کيڏندا", "Ahee na kheddandaa"],
        ["I will not eat this", "مان هي نه کائيندس", "Maan hee na khaayindas"],
        ["He will not write", "هو نه لکندو", "Hoo na likhando"],
        ["She will not go there", "هوءَ اتي نه ويندي", "Hooa ute na windi"],
        ["We will not forget", "اسين نه وسرنداسين", "Aseen na wisrandaasin"],
        ["They will not help", "اهي مدد نه ڪندا", "Ahee madad na kandaa"],
        ["I will not be late", "مان دير نه ڪندس", "Maan der na kandas"],
        ["He will not buy it", "هو اهو خريد نه ڪندو", "Hoo aho khareed na kando"],
        ["She will not call", "هوءَ فون نه ڪندي", "Hooa phone na kandi"],
        ["We will not lose hope", "اسين اميد نه ڇڏنداسين", "Aseen umeed na chhadandaasin"],
        ["They will not return", "اهي واپس نه ايندا", "Ahee waapas na aindaa"],
        ["I will never lie", "مان ڪڏهن به ڪوڙ نه ڳالهائيندس", "Maan kadhan bhi koorr na gaalhaaindas"],
        ["He will not give up", "هو نه ڇڏيندو", "Hoo na chhadindo"],
        ["She will not stop trying", "هوءَ ڪوشش ڇڏڻ نه ڪندي", "Hooa koshish chhadann na kandi"],
    ]
}

lessons[532] = {
    "heading": "Working with nouns – Gender & Plurals in Sindhi",
    "rows": [
        ["One boy", "هڪ ڇوڪرو", "Hik chhokro"],
        ["Many boys", "ڪيترائي ڇوڪرا", "Kitraaee chhokraa"],
        ["One girl", "هڪ ڇوڪري", "Hik chhokri"],
        ["Many girls", "ڪيتريون ئي ڇوڪريون", "Kitriyoon ee chhokriyoon"],
        ["One book", "هڪ ڪتاب", "Hik kitaab"],
        ["Many books", "ڪيتريون ئي ڪتابون", "Kitriyoon ee kitaaboon"],
        ["One tree", "هڪ وڻ", "Hik wann"],
        ["Many trees", "ڪيترائي وڻ", "Kitraaee wann"],
        ["One flower", "هڪ گل", "Hik gul"],
        ["Many flowers", "ڪيترائي گل", "Kitraaee gul"],
        ["The big house (masc)", "وڏو گهر", "Waddo ghar"],
        ["The big houses", "وڏا گهر", "Waddaa ghar"],
        ["The small girl (fem)", "ننڍي ڇوڪري", "Nandhi chhokri"],
        ["The small girls", "ننڍيون ڇوڪريون", "Nandhiyoon chhokriyoon"],
        ["A good man", "سٺو ماڻهو", "Sutho maanho"],
        ["Good men", "سٺا ماڻهو", "Suthaa maanho"],
        ["A new pen", "نئون قلم", "Naon qalam"],
        ["New pens", "نوان قلم", "Nawaan qalam"],
    ]
}

lessons[533] = {
    "heading": "Working with nouns – Prepositions in Sindhi",
    "rows": [
        ["The book on the table", "ميز تي ڪتاب", "Mez te kitaab"],
        ["The pen in the bag", "ٿيلهي ۾ قلم", "Thailhi me qalam"],
        ["Water in the glass", "گلاس ۾ پاڻي", "Glass me paani"],
        ["The boy under the tree", "وڻ هيٺ ڇوڪرو", "Wann heth chhokro"],
        ["Flowers in the garden", "باغ ۾ گل", "Baagh me gul"],
        ["Birds on the tree", "وڻ تي پکي", "Wann te pakhi"],
        ["Fish in the river", "ندي ۾ مڇي", "Nadi me machhi"],
        ["The cat near the door", "دروازي ويجهو ٻلي", "Darwaazi wejho billi"],
        ["The child behind the wall", "ديوار جي پويان ٻار", "Deewaar ji poyaan baar"],
        ["Stars in the sky", "آسمان ۾ تارا", "Aasmaan me taaraa"],
        ["People in the market", "بازار ۾ ماڻهو", "Bazaar me maanho"],
        ["The teacher in the class", "ڪلاس ۾ استاد", "Class me ustaad"],
        ["Food on the plate", "ٿاري ۾ کاڌو", "Thaari me khaadho"],
        ["The cow in the field", "کيت ۾ ڳئون", "Khet me gaoon"],
        ["The car on the road", "رستي تي ڪار", "Raste te kaar"],
        ["The picture on the wall", "ديوار تي تصوير", "Deewaar te tasweer"],
        ["Milk in the pot", "ڏيڪچي ۾ کير", "Ddekchi me kheer"],
        ["Children in the school", "اسڪول ۾ ٻار", "School me baar"],
    ]
}

lessons[534] = {
    "heading": "Prepositions with similar pronunciation or meanings in Sindhi",
    "rows": [
        ["On the table (تي)", "ميز تي", "Mez te"],
        ["At that time (تي)", "ان وقت تي", "Un waqt te"],
        ["In the room (۾)", "ڪمري ۾", "Kamre me"],
        ["Inside the box (اندر)", "صندوق جي اندر", "Sanduuq ji andar"],
        ["From Karachi (مان)", "ڪراچي مان", "Karachi maan"],
        ["By him (کان)", "هن کان", "Hun khaan"],
        ["Near the house (ويجهو)", "گهر ويجهو", "Ghar wejho"],
        ["Close to me (ويجهو)", "منهنجي ويجهو", "Muhhinji wejho"],
        ["Towards the school (طرف)", "اسڪول طرف", "School taraf"],
        ["In front of (اڳيان)", "اڳيان", "Aggiyaan"],
        ["Behind (پويان)", "پويان", "Poyaan"],
        ["Above (مٿي)", "مٿي", "Mathi"],
        ["Below (هيٺ)", "هيٺ", "Heth"],
        ["Between two houses (وچ ۾)", "ٻن گهرن جي وچ ۾", "Ban gharan ji wach me"],
        ["Until tomorrow (تائين)", "سڀاڻي تائين", "Sabhaani taaeen"],
        ["Without water (بغير)", "پاڻي بغير", "Paani baghair"],
        ["For me (لاءِ)", "منهنجي لاءِ", "Muhhinji laai"],
        ["With him (سان)", "هن سان", "Hun saan"],
    ]
}

lessons[535] = {
    "heading": "Cases in Sindhi",
    "rows": [
        ["The boy reads (nominative)", "ڇوڪرو پڙهي ٿو", "Chhokro parhi tho"],
        ["I saw the boy (accusative)", "مون ڇوڪري کي ڏٺو", "Moon chhokri khe dditho"],
        ["Give the book to him (dative)", "ڪتاب هن کي ڏيو", "Kitaab hun khe diyo"],
        ["He wrote with a pen (instrumental)", "هن قلم سان لکيو", "Hun qalam saan likhiyo"],
        ["She came from school (ablative)", "هوءَ اسڪول مان آئي", "Hooa school maan aai"],
        ["This is the boy's book (possessive)", "هي ڇوڪري جي ڪتاب آهي", "Hee chhokri ji kitaab aahi"],
        ["The bird is on the tree (locative)", "پکي وڻ تي آهي", "Pakhi wann te aahi"],
        ["O boy! Come here (vocative)", "اي ڇوڪرا! هتي اچ", "Ai chhokraa! Hite ach"],
        ["The teacher teaches students", "استاد شاگردن کي پڙهائي ٿو", "Ustaad shaagirdan khe parhaai tho"],
        ["The girl's dress is beautiful", "ڇوڪري جو لباس سهڻو آهي", "Chhokri jo libaas suhno aahi"],
        ["He cut the fruit with a knife", "هن ڇري سان ميوو ڪٽيو", "Hun chhuri saan mewo katiyo"],
        ["The water flows from the mountain", "پاڻي جبل مان وهي ٿو", "Paani jabal maan wahi tho"],
        ["The book is in my bag", "ڪتاب منهنجي ٿيلهي ۾ آهي", "Kitaab muhhinji thailhi me aahi"],
        ["Father's love is great", "پيءُ جو پيار عظيم آهي", "Piyu jo pyaar azeem aahi"],
        ["She speaks with her friend", "هوءَ پنهنجي دوست سان ڳالهائي ٿي", "Hooa panhinji dost saan gaalhaayi thee"],
        ["The cat drank milk from the bowl", "ٻلي پياليءَ مان کير پيئي", "Billi piyaaliya maan kheer piyi"],
        ["Come from the other side", "ٻئي طرفان اچو", "Bee tarafaan acho"],
        ["O friend! Listen to me", "اي دوست! منهنجي ڳالهه ٻُڌو", "Ai dost! Muhhinji gaalh buddho"],
    ]
}

lessons[536] = {
    "heading": "Commands / Imperative statements in Sindhi",
    "rows": [
        ["Come here", "هتي اچو", "Hite acho"],
        ["Go there", "اتي وڃو", "Ute wacho"],
        ["Sit down", "ويهي رهو", "Weihi raho"],
        ["Stand up", "بيٺا ٿيو", "Bethaa thiyo"],
        ["Eat your food", "پنهنجو کاڌو کائو", "Panhinjo khaadho khaao"],
        ["Read the book", "ڪتاب پڙهو", "Kitaab parho"],
        ["Write your name", "پنهنجو نالو لکو", "Panhinjo naalo likho"],
        ["Open the door", "دروازو کوليو", "Darwaazo kholiyo"],
        ["Close the window", "دري بند ڪريو", "Dari band kariyo"],
        ["Listen carefully", "غور سان ٻُڌو", "Ghour saan buddho"],
        ["Speak the truth", "سچ ڳالهايو", "Sach gaalhaaio"],
        ["Don't lie", "ڪوڙ نه ڳالهايو", "Koorr na gaalhaaio"],
        ["Don't shout", "نه روئو", "Na roio"],
        ["Be quiet", "خاموش رهو", "Khaamosh raho"],
        ["Hurry up", "جلدي ڪريو", "Jaldi kariyo"],
        ["Wait here", "هتي انتظار ڪريو", "Hite intezaar kariyo"],
        ["Please help me", "مهرباني ڪري مدد ڪريو", "Meherbaani kari madad kariyo"],
        ["Don't forget", "نه وسريو", "Na wisriyo"],
    ]
}

lessons[537] = {
    "heading": "Time related words in Sindhi",
    "rows": [
        ["Today is Monday", "اڄ سومر آهي", "Aaj somar aahi"],
        ["Tomorrow is Tuesday", "سڀاڻي اڱارو آهي", "Sabhaani angaaro aahi"],
        ["Yesterday was Sunday", "ڪالهه آچر هو", "Kaalh aachar ho"],
        ["What time is it now?", "هاڻي ڪيترا وڳا ٿيا؟", "Haani kitraa waga thiyaa?"],
        ["It is ten o'clock", "ڏهه وڳا ٿيا آهن", "Dah waga thiyaa aahan"],
        ["In the morning", "صبح جو", "Subha jo"],
        ["In the afternoon", "ٻپهر جو", "Bapahir jo"],
        ["In the evening", "شام جو", "Shaam jo"],
        ["At night", "رات جو", "Raat jo"],
        ["This week", "هن هفتي", "Han hafte"],
        ["Last month", "گذريل مهيني", "Guzaril mahine"],
        ["Next year", "ايندڙ سال", "Aindarr saal"],
        ["A long time ago", "گهڻو وقت اڳ", "Ghano waqt agg"],
        ["Just now", "هاڻي ئي", "Haani ee"],
        ["Later", "پوءِ", "Poee"],
        ["Always", "هميشه", "Hamesha"],
        ["Sometimes", "ڪڏهن ڪڏهن", "Kadhan kadhan"],
        ["Never", "ڪڏهن به نه", "Kadhan bhi na"],
    ]
}

lessons[538] = {
    "heading": "Causative verbs in Sindhi",
    "rows": [
        ["I made him eat", "مون هن کي کارايو", "Moon hun khe khaaraaiyo"],
        ["She made the child sleep", "هنيءَ ٻار کي سمهارايو", "Huniya baar khe sumhaaraaiyo"],
        ["He got the work done", "هن ڪم ڪرايو", "Hun kam karaaiyo"],
        ["I got the letter written", "مون خط لکرايو", "Moon khat likhraaiyo"],
        ["She got the food cooked", "هنيءَ کاڌو پچرايو", "Huniya khaadho pachraaiyo"],
        ["He made them study", "هن انهن کي پڙهرايو", "Hun unhan khe parhraaiyo"],
        ["I got the house built", "مون گهر ٺهرايو", "Moon ghar thahraaiyo"],
        ["She got the clothes washed", "هنيءَ ڪپڙا ڌورايا", "Huniya kapraa dhoraaiyo"],
        ["He made me run", "هن مون کي ڊوڙايو", "Hun moon khe ddoraaiyo"],
        ["I made him understand", "مون هن کي سمجهايو", "Moon hun khe samjhaaio"],
        ["She got the car repaired", "هنيءَ ڪار مرمت ڪرائي", "Huniya kaar maramat karaai"],
        ["He got the room cleaned", "هن ڪمرو صاف ڪرايو", "Hun kamro saaf karaaiyo"],
        ["I got the tree cut", "مون وڻ ڪٽرايو", "Moon wann kattraaiyo"],
        ["She made them come", "هنيءَ انهن کي اچرايو", "Huniya unhan khe achraaiyo"],
        ["He got the book published", "هن ڪتاب ڇپرائي", "Hun kitaab chhapraai"],
        ["I got him taught", "مون هن کي پڙهرايو", "Moon hun khe parhraaiyo"],
        ["She made him drink water", "هنيءَ هن کي پاڻي پيرايو", "Huniya hun khe paani peeraaiyo"],
        ["He got the wall painted", "هن ديوار رنگرائي", "Hun deewaar rangaai"],
    ]
}

lessons[539] = {
    "heading": "Gender-number agreement rule in Sindhi",
    "rows": [
        ["The good boy (masc. sg.)", "سٺو ڇوڪرو", "Sutho chhokro"],
        ["The good boys (masc. pl.)", "سٺا ڇوڪرا", "Suthaa chhokraa"],
        ["The good girl (fem. sg.)", "سٺي ڇوڪري", "Suthi chhokri"],
        ["The good girls (fem. pl.)", "سٺيون ڇوڪريون", "Suthiyoon chhokriyoon"],
        ["He is tall", "هو ڊگهو آهي", "Hoo ddagho aahi"],
        ["She is tall", "هوءَ ڊگهي آهي", "Hooa ddaghi aahi"],
        ["They (m.) are tall", "اهي ڊگها آهن", "Ahee ddaghaa aahan"],
        ["They (f.) are tall", "اهي ڊگهيون آهن", "Ahee ddaghiyoon aahan"],
        ["A big house", "وڏو گهر", "Waddo ghar"],
        ["Big houses", "وڏا گهر", "Waddaa ghar"],
        ["A small pen", "ننڍو قلم", "Nandho qalam"],
        ["Small pens", "ننڍا قلم", "Nandhaa qalam"],
        ["A red flower", "ڳاڙهو گل", "Garrho gul"],
        ["Red flowers", "ڳاڙها گل", "Garrhaa gul"],
        ["The new car (fem.)", "نئين ڪار", "Naeen kaar"],
        ["New cars", "نيون ڪارون", "Nayoon kaaroon"],
        ["One child (masc.)", "هڪ ٻار", "Hik baar"],
        ["Many children", "ڪيترائي ٻار", "Kitraaee baar"],
    ]
}

lessons[540] = {
    "heading": "Perfect Tense – Second Style in Sindhi",
    "rows": [
        ["I have gone", "مان هلي ويس", "Maan hali wis"],
        ["He has come", "هو اچي ويو آهي", "Hoo achi wiyo aahi"],
        ["She has eaten", "هوءَ کائي وئي آهي", "Hooa khaai wai aahi"],
        ["We have finished", "اسين ختم ڪري ڇڏيو آهي", "Aseen khatam kari chhadiyo aahi"],
        ["They have left", "اهي هلي ويا آهن", "Ahee hali wiyaa aahan"],
        ["I had gone there", "مان اتي هلي ويو هئس", "Maan ute hali wiyo huas"],
        ["He had come already", "هو اڳ ۾ ئي اچي ويو هو", "Hoo agg me ee achi wiyo ho"],
        ["She had cooked before", "هوءَ اڳ ۾ ئي پچائي وئي هئي", "Hooa agg me ee pachaai wai hui"],
        ["We had arrived early", "اسين جلدي اچي ويا هئاسين", "Aseen jaldi achi wiyaa huaasin"],
        ["They had already slept", "اهي اڳ ۾ ئي سمهي ويا هئا", "Ahee agg me ee sumhi wiyaa huaa"],
        ["I will have gone by then", "مان ان وقت تائين هلي ويندس", "Maan un waqt taaeen hali windas"],
        ["He will have come back", "هو واپس اچي ويندو", "Hoo waapas achi windo"],
        ["She will have finished cooking", "هوءَ پچائي وئي هوندي", "Hooa pachaai wai hondi"],
        ["We will have reached there", "اسين اتي پهچي ويندا سين", "Aseen ute pahchi windaa sin"],
        ["They will have left", "اهي هلي ويندا", "Ahee hali windaa"],
        ["The work has been done", "ڪم ٿي ويو آهي", "Kam thi wiyo aahi"],
        ["The food has been cooked", "کاڌو پچجي ويو آهي", "Khaadho pachji wiyo aahi"],
        ["All the books have been read", "سڀ ڪتابون پڙهجي ويون آهن", "Sabh kitaaboon parhji wiyoon aahan"],
    ]
}

lessons[541] = {
    "heading": "Perfect Continuous tense in Sindhi",
    "rows": [
        ["I have been studying for two hours", "مان ٻن ڪلاڪن کان پڙهي رهيو آهيان", "Maan ban klaakan khaan parhi rahiyo aahiyaan"],
        ["He has been working since morning", "هو صبح کان ڪم ڪري رهيو آهي", "Hoo subha khaan kam kari rahiyo aahi"],
        ["She has been cooking for an hour", "هوءَ هڪ ڪلاڪ کان پچائي رهي آهي", "Hooa hik klaak khaan pachaai rahi aahi"],
        ["We have been waiting since noon", "اسين ٻپهر کان انتظار ڪري رهيا آهيون", "Aseen bapahir khaan intezaar kari rahiyaa aahiyoon"],
        ["They have been playing all day", "اهي سڄو ڏينهن کيڏي رهيا آهن", "Ahee sajo dinhan kheddi rahiyaa aahan"],
        ["I had been reading for hours", "مان ڪيترن ڪلاڪن کان پڙهي رهيو هئس", "Maan kitran klaakan khaan parhi rahiyo huas"],
        ["He had been sleeping since evening", "هو شام کان سمهي رهيو هو", "Hoo shaam khaan sumhi rahiyo ho"],
        ["She had been teaching for years", "هوءَ ڪيترن سالن کان پڙهائي رهي هئي", "Hooa kitran saalan khaan parhaai rahi hui"],
        ["We had been traveling since morning", "اسين صبح کان سفر ڪري رهيا هئاسين", "Aseen subha khaan safar kari rahiyaa huaasin"],
        ["They had been farming all day", "اهي سڄو ڏينهن هاريءَ ڪري رهيا هئا", "Ahee sajo dinhan haariya kari rahiyaa huaa"],
        ["I will have been working for 5 years", "مان پنج سالن کان ڪم ڪري رهيو هوندس", "Maan panj saalan khaan kam kari rahiyo hondas"],
        ["He will have been studying for 3 hours", "هو ٽن ڪلاڪن کان پڙهي رهيو هوندو", "Hoo tan klaakan khaan parhi rahiyo hondo"],
        ["She will have been cooking since noon", "هوءَ ٻپهر کان پچائي رهي هوندي", "Hooa bapahir khaan pachaai rahi hondi"],
        ["We will have been living here for ten years", "اسين هتي ڏهن سالن کان رهي رهيا هونداسين", "Aseen hite dahan saalan khaan rahi rahiyaa hondaasin"],
        ["I have been learning Sindhi for 6 months", "مان ڇهن مهينن کان سنڌي سکي رهيو آهيان", "Maan chhan mahinan khaan Sindhi sikhi rahiyo aahiyaan"],
        ["She has been singing since childhood", "هوءَ ننپڻ کان ڳائي رهي آهي", "Hooa nanpann khaan gaai rahi aahi"],
        ["They have been living here for 20 years", "اهي هتي ويهن سالن کان رهي رهيا آهن", "Ahee hite weehan saalan khaan rahi rahiyaa aahan"],
        ["He has been driving for 3 hours", "هو ٽن ڪلاڪن کان ڳاڏي هلائي رهيو آهي", "Hoo tan klaakan khaan gaadi halaai rahiyo aahi"],
    ]
}

lessons[542] = {
    "heading": "Difference between 'no/not' and 'don't want' in Sindhi",
    "rows": [
        ["No, I don't want (نه گهرجي)", "نه، مون کي نه گهرجي", "Na, moon khe na ghuruji"],
        ["I don't want tea", "مون کي چانهه نه گهرجي", "Moon khe chaanhh na ghuruji"],
        ["He doesn't want to go (نٿو چاهي)", "هو وڃڻ نٿو چاهي", "Hoo wachann natho chaahi"],
        ["She doesn't want food", "هنيءَ کي کاڌو نه گهرجي", "Huniya khe khaadho na ghuruji"],
        ["I don't eat meat (نٿو)", "مان ماس نٿو کائان", "Maan maas natho khaaiyaan"],
        ["He doesn't speak English (نٿو)", "هو انگريزي نٿو ڳالهائي", "Hoo Angrezi natho gaalhaayi"],
        ["No, this is not mine", "نه، هي منهنجو ناهي", "Na, hee muhhinjo naahi"],
        ["I don't know (نٿو ڄاڻان)", "مان نٿو ڄاڻان", "Maan natho jaanaan"],
        ["She doesn't want to study", "هوءَ پڙهڻ نٿي چاهي", "Hooa parhann nathi chaahi"],
        ["We don't need anything", "اسان کي ڪجهه نه گهرجي", "Asaan khe kujh na ghuruji"],
        ["He doesn't want help", "هن کي مدد نه گهرجي", "Hun khe madad na ghuruji"],
        ["I don't want to sleep", "مون کي سمهڻ نه گهرجي", "Moon khe sumhann na ghuruji"],
        ["She doesn't like this", "هنيءَ کي هي پسند ناهي", "Huniya khe hee pasand naahi"],
        ["I don't have money", "منهنجي وٽ پئسا ناهن", "Muhhinji watt paisa naahan"],
        ["He doesn't understand", "هو نٿو سمجهي", "Hoo natho samjhi"],
        ["We don't want to be late", "اسان کي دير نه ٿيڻ گهرجي", "Asaan khe der na thinn ghuruji"],
        ["I don't want any problems", "مون کي ڪا مشڪل نه گهرجي", "Moon khe kaa mushkil na ghuruji"],
        ["No, I will not go", "نه، مان نه ويندس", "Na, maan na windas"],
    ]
}

# Load and update data
data = json.load(open('data_sindhi.json', 'r', encoding='utf-8'))
id_map = {ch['id']: ch for ch in data}

for lid, content in lessons.items():
    ch = id_map[lid]
    ch['blocks'] = [{
        "type": "table",
        "heading": content['heading'],
        "headers": ["English", "Sindhi", "Transliteration"],
        "speakCol": 1,
        "rows": content['rows']
    }]

with open('data_sindhi.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Section 2 (510-542) populated: {len(lessons)} lessons")
for lid in sorted(lessons.keys()):
    ch = id_map[lid]
    nr = len(ch['blocks'][0]['rows'])
    print(f"  {lid}: {nr} rows")
