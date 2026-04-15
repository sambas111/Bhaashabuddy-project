import json

lessons = {}

lessons[543] = {
    "heading": "Sentences using 'Going to' phrase in Sindhi",
    "rows": [
        ["I am going to eat", "مان کائڻ وارو آهيان", "Maan khaainann waaro aahiyaan"],
        ["He is going to study", "هو پڙهڻ وارو آهي", "Hoo parhann waaro aahi"],
        ["She is going to cook", "هوءَ پچائڻ واري آهي", "Hooa pachaainann waari aahi"],
        ["We are going to play", "اسين کيڏڻ وارا آهيون", "Aseen kheddann waaraa aahiyoon"],
        ["They are going to leave", "اهي هلڻ وارا آهن", "Ahee halann waaraa aahan"],
        ["I am going to sleep now", "مان هاڻي سمهڻ وارو آهيان", "Maan haani sumhann waaro aahiyaan"],
        ["He is going to buy a car", "هو ڪار خريد ڪرڻ وارو آهي", "Hoo kaar khareed karann waaro aahi"],
        ["She is going to sing", "هوءَ ڳائڻ واري آهي", "Hooa gaainann waari aahi"],
        ["We are going to visit the temple", "اسين مندر وڃڻ وارا آهيون", "Aseen mandir wachann waaraa aahiyoon"],
        ["It is going to rain", "مينهن پوڻ وارو آهي", "Meenhan ponn waaro aahi"],
        ["I am going to call him", "مان هن کي فون ڪرڻ وارو آهيان", "Maan hun khe phone karann waaro aahiyaan"],
        ["He is going to write a letter", "هو خط لکڻ وارو آهي", "Hoo khat likhann waaro aahi"],
        ["She is going to teach", "هوءَ پڙهائڻ واري آهي", "Hooa parhaainann waari aahi"],
        ["We are going to finish the work", "اسين ڪم ختم ڪرڻ وارا آهيون", "Aseen kam khatam karann waaraa aahiyoon"],
        ["They are going to travel", "اهي سفر ڪرڻ وارا آهن", "Ahee safar karann waaraa aahan"],
        ["I am going to learn Sindhi", "مان سنڌي سکڻ وارو آهيان", "Maan Sindhi sikhann waaro aahiyaan"],
        ["He is going to start a business", "هو ڪاروبار شروع ڪرڻ وارو آهي", "Hoo kaarobaar shuroo karann waaro aahi"],
        ["She is going to run in the race", "هوءَ دوڙ ۾ ڊوڙڻ واري آهي", "Hooa dorr me ddorann waari aahi"],
    ]
}

lessons[544] = {
    "heading": "Sentences using 'Used to' phrase in Sindhi",
    "rows": [
        ["I used to go to school", "مان اسڪول وڃندو هوس", "Maan school wachando hos"],
        ["He used to play cricket", "هو ڪرڪيٽ کيڏندو هو", "Hoo cricket kheddando ho"],
        ["She used to cook every day", "هوءَ روز پچائيندي هئي", "Hooa roz pachaindi hui"],
        ["We used to study together", "اسين گڏجي پڙهندا هئاسين", "Aseen gadji parhandaa huaasin"],
        ["They used to live here", "اهي هتي رهندا هئا", "Ahee hite rahandaa huaa"],
        ["I used to walk in the morning", "مان صبح جو هلندو هوس", "Maan subha jo halando hos"],
        ["He used to read a lot", "هو ڏاڍو پڙهندو هو", "Hoo ddaadho parhando ho"],
        ["She used to sing songs", "هوءَ گيت ڳائيندي هئي", "Hooa geet gaaindi hui"],
        ["We used to swim in the river", "اسين ندي ۾ ترندا هئاسين", "Aseen nadi me tarandaa huaasin"],
        ["They used to visit us", "اهي اسان وٽ ايندا هئا", "Ahee asaan watt aindaa huaa"],
        ["I used to drink milk daily", "مان روز کير پيئندو هوس", "Maan roz kheer piyando hos"],
        ["He used to help everyone", "هو سڀني جي مدد ڪندو هو", "Hoo sabhni ji madad kando ho"],
        ["She used to dance well", "هوءَ سٺو ناچيندي هئي", "Hooa sutho naachindi hui"],
        ["We used to watch movies together", "اسين گڏجي فلمون ڏسندا هئاسين", "Aseen gadji filmoon disandaa huaasin"],
        ["They used to grow vegetables", "اهي ڀاڄيون اُگائيندا هئا", "Ahee bhaajiyoon ugaaindaa huaa"],
        ["I used to write poems", "مان نظمون لکندو هوس", "Maan nazmoon likhando hos"],
        ["He used to teach us", "هو اسان کي پڙهائيندو هو", "Hoo asaan khe parhaindo ho"],
        ["She used to travel often", "هوءَ اڪثر سفر ڪندي هئي", "Hooa aksar safar kandi hui"],
    ]
}

lessons[545] = {
    "heading": "Sentences using 'Used to' – old style in Sindhi",
    "rows": [
        ["People used to travel on horses", "ماڻهو گهوڙن تي سفر ڪندا هئا", "Maanho ghorran te safar kandaa huaa"],
        ["Kings used to rule", "بادشاهه حڪومت ڪندا هئا", "Baadshaah hukoomat kandaa huaa"],
        ["Women used to grind wheat", "عورتون کاٺي پيهنديون هيون", "Auratoon khaati pehandiyoon hiyoon"],
        ["Farmers used to plow with oxen", "هاري ڍاکن سان هل هلائيندا هئا", "Haari ddhaakan saan hal halaaindaa huaa"],
        ["Children used to play outside", "ٻار ٻاهر کيڏندا هئا", "Baar baahar kheddandaa huaa"],
        ["We used to light oil lamps", "اسين تيل جا چراغ ٻاريندا هئاسين", "Aseen tel jaa chiraagh baarindaa huaasin"],
        ["They used to walk long distances", "اهي ڊگها رستا هلندا هئا", "Ahee ddaghaa rastaa halandaa huaa"],
        ["People used to tell stories at night", "ماڻهو رات جو ڪهاڻيون ٻڌائيندا هئا", "Maanho raat jo kahaaniyoon buddhaaindaa huaa"],
        ["Elders used to teach morals", "وڏيرا سبق سکائيندا هئا", "Waderaa sabaq sikhaaindaa huaa"],
        ["Women used to make butter at home", "عورتون گهر ۾ مکڻ ٺاهينديون هيون", "Auratoon ghar me makhan thaahindiyoon hiyoon"],
        ["Traders used to carry goods on camels", "واپاري اٺن تي سامان کڻندا هئا", "Waapaari uthan te saamaan khinandaa huaa"],
        ["Villages used to be very peaceful", "ڳوٺ ڏاڍا پرامن هئا", "Ggoth ddaadhaa puraman huaa"],
        ["People used to live simply", "ماڻهو سادي زندگي گذاريندا هئا", "Maanho saadi zindagi guzaarindaa huaa"],
        ["Children used to learn from nature", "ٻار قدرت کان سکندا هئا", "Baar qudrat khaan sikhandaa huaa"],
        ["Weddings used to last seven days", "شاديون ست ڏينهن هلنديون هيون", "Shaadiyoon sat dinhan halandiyoon hiyoon"],
        ["People used to write with ink", "ماڻهو سياهي سان لکندا هئا", "Maanho siyaahi saan likhandaa huaa"],
        ["Rivers used to be very clean", "نديون ڏاڍيون صاف هيون", "Nadiyoon ddaadhiyoon saaf hiyoon"],
        ["Markets used to close early", "بازار جلدي بند ٿيندا هئا", "Bazaar jaldi band thindaa huaa"],
    ]
}

lessons[546] = {
    "heading": "Sentences using 'If-Then' in Sindhi",
    "rows": [
        ["If you study, you will pass", "جيڪڏهن توهان پڙهندؤ ته پاس ٿيندؤ", "Jekadhan tawhan parhandau ta paas thindau"],
        ["If it rains, we will stay home", "جيڪڏهن مينهن پوندو ته اسين گهر رهنداسين", "Jekadhan meenhan pondo ta aseen ghar rahandaasin"],
        ["If he comes, I will tell him", "جيڪڏهن هو ايندو ته مان هن کي ٻڌائيندس", "Jekadhan hoo aindo ta maan hun khe buddhaaindas"],
        ["If she cooks, I will eat", "جيڪڏهن هوءَ پچائيندي ته مان کائيندس", "Jekadhan hooa pachaindi ta maan khaayindas"],
        ["If you work hard, you will succeed", "جيڪڏهن توهان محنت ڪندؤ ته ڪامياب ٿيندؤ", "Jekadhan tawhan mehnat kandau ta kaamiyaab thindau"],
        ["If I had money, I would buy a car", "جيڪڏهن منهنجي وٽ پئسا هجن ها ته ڪار خريد ڪريها", "Jekadhan muhhinji watt paisa hujan haa ta kaar khareed karihaa"],
        ["If she had time, she would come", "جيڪڏهن هنيءَ وٽ وقت هجي ها ته اچي ها", "Jekadhan huniya watt waqt huji haa ta achi haa"],
        ["If we try, we can do it", "جيڪڏهن اسين ڪوشش ڪريون ته ڪري سگهون ٿا", "Jekadhan aseen koshish kariyoon ta kari saghoon thaa"],
        ["If it is cold, wear a jacket", "جيڪڏهن ٿڌ هجي ته جيڪيٽ پيريو", "Jekadhan thadh huji ta jacket periyo"],
        ["If you are hungry, eat food", "جيڪڏهن توهان کي بک لڳي هجي ته کاڌو کائو", "Jekadhan tawhan khe bhuk lagi huji ta khaadho khaao"],
        ["If he calls, answer the phone", "جيڪڏهن هو فون ڪري ته فون کوليو", "Jekadhan hoo phone kari ta phone kholiyo"],
        ["If you need help, ask me", "جيڪڏهن توهان کي مدد گهرجي ته مون کان پڇو", "Jekadhan tawhan khe madad ghuruji ta moon khaan pucho"],
        ["If they agree, we will start", "جيڪڏهن اهي راضي هجن ته اسين شروع ڪنداسين", "Jekadhan ahee raazi hujan ta aseen shuroo kandaasin"],
        ["If I wake up early, I will exercise", "جيڪڏهن مان جلدي اُٿندس ته ورزش ڪندس", "Jekadhan maan jaldi uthandas ta warzish kandas"],
        ["If she studies well, she will get a job", "جيڪڏهن هوءَ سٺي طرح پڙهندي ته نوڪري ملندي", "Jekadhan hooa suthi tarah parhandi ta naukri milandi"],
        ["If we plant trees, the earth will be green", "جيڪڏهن اسين وڻ لڳايون ته ڌرتي هريالي ٿيندي", "Jekadhan aseen wann lagaayoon ta dharti hariyaali thindi"],
        ["If you are late, they will leave", "جيڪڏهن توهان دير ڪندؤ ته اهي هلي ويندا", "Jekadhan tawhan der kandau ta ahee hali windaa"],
        ["If he practices, he will improve", "جيڪڏهن هو مشق ڪندو ته بهتر ٿيندو", "Jekadhan hoo mashq kando ta behtar thindo"],
    ]
}

lessons[547] = {
    "heading": "Prepositions with Verbs in Sindhi",
    "rows": [
        ["Look at the bird", "پکيءَ کي ڏسو", "Pakhiya khe diso"],
        ["Listen to the song", "گيت ٻُڌو", "Geet buddho"],
        ["Think about it", "ان بابت سوچو", "Un baabat socho"],
        ["Wait for the bus", "بس جو انتظار ڪريو", "Bus jo intezaar kariyo"],
        ["Talk about the topic", "موضوع بابت ڳالهايو", "Mauzu baabat gaalhaaio"],
        ["Ask for help", "مدد لاءِ پڇو", "Madad laai pucho"],
        ["Agree with him", "هن سان متفق ٿيو", "Hun saan muttafiq thiyo"],
        ["Believe in yourself", "پنهنجي تي يقين رکو", "Panhinji te yaqeen rakho"],
        ["Depend on others", "ٻين تي ڀروسو ڪريو", "Been te bharoso kariyo"],
        ["Laugh at the joke", "لطيفي تي هنسو", "Lateefi te hanso"],
        ["Worry about exams", "امتحان جي فڪر ڪريو", "Imtehaan ji fikr kariyo"],
        ["Complain about the noise", "شور جي شڪايت ڪريو", "Shor ji shikaayat kariyo"],
        ["Apologize for the mistake", "غلطي لاءِ معافي وٺو", "Ghalti laai maafi wutho"],
        ["Insist on going", "وڃڻ تي اصرار ڪريو", "Wachann te israar kariyo"],
        ["Concentrate on your studies", "پنهنجي پڙهائيءَ تي ڌيان ڏيو", "Panhinji parhaai ya te dhyaan diyo"],
        ["He lives with his family", "هو پنهنجي خاندان سان رهي ٿو", "Hoo panhinji khaandaan saan rahi tho"],
        ["Prepare for the exam", "امتحان لاءِ تياري ڪريو", "Imtehaan laai tayyaari kariyo"],
        ["Dream about success", "ڪاميابي جو خواب ڏسو", "Kaamiyaabi jo khwaab diso"],
    ]
}

lessons[548] = {
    "heading": "Adjectives in Sindhi",
    "rows": [
        ["The big house", "وڏو گهر", "Waddo ghar"],
        ["A beautiful garden", "سهڻو باغ", "Suhno baagh"],
        ["The hot tea", "گرم چانهه", "Garam chaanhh"],
        ["A cold day", "ٿڌو ڏينهن", "Thadho dinhan"],
        ["The old man", "پراڻو ماڻهو", "Paraano maanho"],
        ["A young girl", "نوجوان ڇوڪري", "Naujawaan chhokri"],
        ["The tall tree", "ڊگهو وڻ", "Ddagho wann"],
        ["A short road", "ننڍو رستو", "Nandho rasto"],
        ["The sweet mango", "مٺو انب", "Mitho anab"],
        ["A sour fruit", "کٽو ميوو", "Khato mewo"],
        ["The clean water", "صاف پاڻي", "Saaf paani"],
        ["A dirty street", "ميلي گلي", "Meli gali"],
        ["The wise teacher", "عقلمند استاد", "Aqlmand ustaad"],
        ["A rich man", "مالدار ماڻهو", "Maaldaar maanho"],
        ["The brave soldier", "بهادر فوجي", "Bahaadar fauji"],
        ["A lazy student", "سُست شاگرد", "Sust shaagird"],
        ["The dark night", "اونداهي رات", "Oondaahi raat"],
        ["A bright day", "روشن ڏينهن", "Roshan dinhan"],
    ]
}

lessons[549] = {
    "heading": "Using verb 'Can/To be able to' in Sindhi",
    "rows": [
        ["I can speak Sindhi", "مان سنڌي ڳالهائي سگهان ٿو", "Maan Sindhi gaalhaayi saghaan tho"],
        ["He can run fast", "هو تيز ڊوڙي سگهي ٿو", "Hoo tez ddori saghi tho"],
        ["She can cook well", "هوءَ سٺو پچائي سگهي ٿي", "Hooa sutho pachaai saghi thee"],
        ["We can swim", "اسين تري سگهون ٿا", "Aseen tari saghoon thaa"],
        ["They can play football", "اهي فٽبال کيڏي سگهن ٿا", "Ahee football kheddi saghan thaa"],
        ["I can read this book", "مان هي ڪتاب پڙهي سگهان ٿو", "Maan hee kitaab parhi saghaan tho"],
        ["He can drive a car", "هو ڪار هلائي سگهي ٿو", "Hoo kaar halaai saghi tho"],
        ["She can sing beautifully", "هوءَ سهڻو ڳائي سگهي ٿي", "Hooa suhno gaai saghi thee"],
        ["Can you help me?", "ڇا توهان منهنجي مدد ڪري سگهو ٿا؟", "Chhaa tawhan muhhinji madad kari sagho thaa?"],
        ["Can he come tomorrow?", "ڇا هو سڀاڻي اچي سگهي ٿو؟", "Chhaa hoo sabhaani achi saghi tho?"],
        ["I cannot understand", "مان نٿو سمجهي سگهان", "Maan natho samjhi saghaan"],
        ["He cannot lift this", "هو هي نٿو کڻي سگهي", "Hoo hee natho khini saghi"],
        ["She cannot come today", "هوءَ اڄ نٿي اچي سگهي", "Hooa aaj nathi achi saghi"],
        ["We could not finish", "اسين ختم نه ڪري سگهيا سين", "Aseen khatam na kari saghiyaa sin"],
        ["I will be able to do it", "مان ڪري سگهندس", "Maan kari saghandas"],
        ["He will be able to pass", "هو پاس ٿي سگهندو", "Hoo paas thi saghando"],
        ["She will not be able to come", "هوءَ اچي نه سگهندي", "Hooa achi na saghandi"],
        ["Can you speak English?", "ڇا توهان انگريزي ڳالهائي سگهو ٿا؟", "Chhaa tawhan Angrezi gaalhaayi sagho thaa?"],
    ]
}

lessons[550] = {
    "heading": "Using verb 'To Want/To Need' in Sindhi",
    "rows": [
        ["I want water", "مون کي پاڻي گهرجي", "Moon khe paani ghuruji"],
        ["He wants food", "هن کي کاڌو گهرجي", "Hun khe khaadho ghuruji"],
        ["She wants a book", "هنيءَ کي ڪتاب گهرجي", "Huniya khe kitaab ghuruji"],
        ["We need help", "اسان کي مدد گهرجي", "Asaan khe madad ghuruji"],
        ["They want money", "انهن کي پئسا گهرجن", "Unhan khe paisa ghurjan"],
        ["I want to go home", "مان گهر وڃڻ چاهيان ٿو", "Maan ghar wachann chaahiyaan tho"],
        ["He wants to study", "هو پڙهڻ چاهي ٿو", "Hoo parhann chaahi tho"],
        ["She wants to sleep", "هوءَ سمهڻ چاهي ٿي", "Hooa sumhann chaahi thee"],
        ["We want to learn Sindhi", "اسين سنڌي سکڻ چاهيون ٿا", "Aseen Sindhi sikhann chaahiyoon thaa"],
        ["They want to play", "اهي کيڏڻ چاهين ٿا", "Ahee kheddann chaahin thaa"],
        ["I need a doctor", "مون کي ڊاڪٽر گهرجي", "Moon khe doctor ghuruji"],
        ["He needs rest", "هن کي آرام گهرجي", "Hun khe aaraam ghuruji"],
        ["She needs time", "هنيءَ کي وقت گهرجي", "Huniya khe waqt ghuruji"],
        ["We need more space", "اسان کي وڌيڪ جاءِ گهرجي", "Asaan khe wadhik jaai ghuruji"],
        ["I don't want tea", "مون کي چانهه نه گهرجي", "Moon khe chaanhh na ghuruji"],
        ["He doesn't want to go", "هو وڃڻ نٿو چاهي", "Hoo wachann natho chaahi"],
        ["She doesn't need anything", "هنيءَ کي ڪجهه نه گهرجي", "Huniya khe kujh na ghuruji"],
        ["What do you want?", "توهان کي ڇا گهرجي؟", "Tawhan khe chhaa ghuruji?"],
    ]
}

lessons[551] = {
    "heading": "Verb 'To Become/To Happen' in Sindhi",
    "rows": [
        ["He became a doctor", "هو ڊاڪٽر ٿيو", "Hoo doctor thiyo"],
        ["She became happy", "هوءَ خوش ٿي", "Hooa khush thi"],
        ["What happened?", "ڇا ٿيو؟", "Chhaa thiyo?"],
        ["An accident happened", "حادثو ٿيو", "Haadso thiyo"],
        ["It became cold", "ٿڌ ٿي وئي", "Thadh thi wai"],
        ["He will become a teacher", "هو استاد ٿيندو", "Hoo ustaad thindo"],
        ["She became sad", "هوءَ اداس ٿي وئي", "Hooa udaas thi wai"],
        ["The work is done", "ڪم ٿي ويو", "Kam thi wiyo"],
        ["It is getting dark", "اونداهي ٿي رهي آهي", "Oondaahi thi rahi aahi"],
        ["He became famous", "هو مشهور ٿيو", "Hoo mashhoor thiyo"],
        ["She became angry", "هوءَ ناراض ٿي وئي", "Hooa naaraaz thi wai"],
        ["What will happen tomorrow?", "سڀاڻي ڇا ٿيندو؟", "Sabhaani chhaa thindo?"],
        ["Nothing happened", "ڪجهه نه ٿيو", "Kujh na thiyo"],
        ["He became rich", "هو مالدار ٿيو", "Hoo maaldaar thiyo"],
        ["It became morning", "صبح ٿي وئي", "Subha thi wai"],
        ["She became a singer", "هوءَ ڳائڻي ٿي وئي", "Hooa gaaini thi wai"],
        ["Everything is happening well", "سڀ ڪجهه سٺو ٿي رهيو آهي", "Sabh kujh sutho thi rahiyo aahi"],
        ["The dream came true", "خواب پورو ٿيو", "Khwaab pooro thiyo"],
    ]
}

lessons[552] = {
    "heading": "Using 'Should' in Sindhi",
    "rows": [
        ["You should study", "توهان کي پڙهڻ گهرجي", "Tawhan khe parhann ghuruji"],
        ["He should go", "هن کي وڃڻ گهرجي", "Hun khe wachann ghuruji"],
        ["She should eat", "هنيءَ کي کائڻ گهرجي", "Huniya khe khaainann ghuruji"],
        ["We should help others", "اسان کي ٻين جي مدد ڪرڻ گهرجي", "Asaan khe been ji madad karann ghuruji"],
        ["They should listen", "انهن کي ٻُڌڻ گهرجي", "Unhan khe budhann ghuruji"],
        ["You should speak the truth", "توهان کي سچ ڳالهائڻ گهرجي", "Tawhan khe sach gaalhaaynann ghuruji"],
        ["He should work hard", "هن کي محنت ڪرڻ گهرجي", "Hun khe mehnat karann ghuruji"],
        ["She should rest", "هنيءَ کي آرام ڪرڻ گهرجي", "Huniya khe aaraam karann ghuruji"],
        ["We should save water", "اسان کي پاڻي بچائڻ گهرجي", "Asaan khe paani bachaaynann ghuruji"],
        ["You should not lie", "توهان کي ڪوڙ نه ڳالهائڻ گهرجي", "Tawhan khe koorr na gaalhaaynann ghuruji"],
        ["He should not be lazy", "هن کي سُست نه ٿيڻ گهرجي", "Hun khe sust na thinn ghuruji"],
        ["We should exercise daily", "اسان کي روز ورزش ڪرڻ گهرجي", "Asaan khe roz warzish karann ghuruji"],
        ["They should come on time", "انهن کي وقت تي اچڻ گهرجي", "Unhan khe waqt te achann ghuruji"],
        ["You should drink more water", "توهان کي وڌيڪ پاڻي پيئڻ گهرجي", "Tawhan khe wadhik paani piyann ghuruji"],
        ["She should learn from mistakes", "هنيءَ کي غلطين مان سکڻ گهرجي", "Huniya khe ghaltiyaan maan sikhann ghuruji"],
        ["He should respect elders", "هن کي وڏيرن جو احترام ڪرڻ گهرجي", "Hun khe waderan jo ihtiraam karann ghuruji"],
        ["We should protect the environment", "اسان کي ماحول جي حفاظت ڪرڻ گهرجي", "Asaan khe maahol ji hifaazat karann ghuruji"],
        ["You should be polite", "توهان کي شائسته ٿيڻ گهرجي", "Tawhan khe shaaista thinn ghuruji"],
    ]
}

lessons[553] = {
    "heading": "Using 'Must'/'to have to' in Sindhi",
    "rows": [
        ["I must go now", "مون کي هاڻي وڃڻو آهي", "Moon khe haani wachano aahi"],
        ["He must study", "هن کي پڙهڻو آهي", "Hun khe parhano aahi"],
        ["She must cook food", "هنيءَ کي کاڌو پچائڻو آهي", "Huniya khe khaadho pachaainano aahi"],
        ["We must finish the work", "اسان کي ڪم ختم ڪرڻو آهي", "Asaan khe kam khatam karano aahi"],
        ["They must come tomorrow", "انهن کي سڀاڻي اچڻو آهي", "Unhan khe sabhaani achano aahi"],
        ["I have to wake up early", "مون کي جلدي اُٿڻو آهي", "Moon khe jaldi uthano aahi"],
        ["He has to go to the office", "هن کي آفيس وڃڻو آهي", "Hun khe office wachano aahi"],
        ["She has to buy vegetables", "هنيءَ کي ڀاڄيون خريد ڪرڻيون آهن", "Huniya khe bhaajiyoon khareed karaniyoon aahan"],
        ["We have to pay the bill", "اسان کي بل ڏيڻو آهي", "Asaan khe bill dinno aahi"],
        ["They have to attend the meeting", "انهن کي ميٽنگ ۾ وڃڻو آهي", "Unhan khe meeting me wachano aahi"],
        ["You must speak the truth", "توهان کي سچ ڳالهائڻو آهي", "Tawhan khe sach gaalhaaynano aahi"],
        ["I must complete my homework", "مون کي پنهنجو ڪم مڪمل ڪرڻو آهي", "Moon khe panhinjo kam mukammal karano aahi"],
        ["He must take the medicine", "هن کي دوا کائڻي آهي", "Hun khe dawaa khaainani aahi"],
        ["She must return the book", "هنيءَ کي ڪتاب واپس ڪرڻي آهي", "Huniya khe kitaab waapas karani aahi"],
        ["We must leave now", "اسان کي هاڻي هلڻو آهي", "Asaan khe haani halano aahi"],
        ["They must follow the rules", "انهن کي قاعدن تي عمل ڪرڻو آهي", "Unhan khe qaaidan te amal karano aahi"],
        ["You have to be patient", "توهان کي صبر ڪرڻو آهي", "Tawhan khe sabr karano aahi"],
        ["I must help my friend", "مون کي پنهنجي دوست جي مدد ڪرڻي آهي", "Moon khe panhinji dost ji madad karani aahi"],
    ]
}

lessons[554] = {
    "heading": "Using phrase 'to keep doing' in Sindhi",
    "rows": [
        ["Keep reading", "پڙهندا رهو", "Parhandaa raho"],
        ["Keep working", "ڪم ڪندا رهو", "Kam kandaa raho"],
        ["Keep walking", "هلندا رهو", "Halandaa raho"],
        ["Keep trying", "ڪوشش ڪندا رهو", "Koshish kandaa raho"],
        ["He keeps studying", "هو پڙهندو رهي ٿو", "Hoo parhando rahi tho"],
        ["She keeps cooking", "هوءَ پچائيندي رهي ٿي", "Hooa pachaindi rahi thee"],
        ["We keep playing", "اسين کيڏندا رهون ٿا", "Aseen kheddandaa rahoon thaa"],
        ["They keep coming", "اهي ايندا رهن ٿا", "Ahee aindaa rahan thaa"],
        ["I will keep learning", "مان سکندو رهندس", "Maan sikhando rahandas"],
        ["He will keep running", "هو ڊوڙندو رهندو", "Hoo ddorando rahando"],
        ["She will keep teaching", "هوءَ پڙهائيندي رهندي", "Hooa parhaindi rahandi"],
        ["Keep smiling", "مسڪرائيندا رهو", "Muskuraaindaa raho"],
        ["Keep praying", "دعا ڪندا رهو", "Duaa kandaa raho"],
        ["Keep improving", "بهتر ٿيندا رهو", "Behtar thindaa raho"],
        ["He kept talking", "هو ڳالهائيندو رهيو", "Hoo gaalhaaindo rahiyo"],
        ["She kept singing", "هوءَ ڳائيندي رهي", "Hooa gaaindi rahi"],
        ["We kept working all night", "اسين سڄي رات ڪم ڪندا رهياسين", "Aseen saji raat kam kandaa rahiyaasin"],
        ["Don't keep waiting", "انتظار ڪندا نه رهو", "Intezaar kandaa na raho"],
    ]
}

lessons[555] = {
    "heading": "Comparison and degrees of comparison in Sindhi",
    "rows": [
        ["He is taller than me", "هو مون کان ڊگهو آهي", "Hoo moon khaan ddagho aahi"],
        ["She is smarter than him", "هوءَ هن کان وڌيڪ هوشيار آهي", "Hooa hun khaan wadhik hoshiyaar aahi"],
        ["This book is better than that", "هي ڪتاب ان کان بهتر آهي", "Hee kitaab un khaan behtar aahi"],
        ["He is the tallest in the class", "هو ڪلاس ۾ سڀ کان ڊگهو آهي", "Hoo class me sabh khaan ddagho aahi"],
        ["She is the most beautiful", "هوءَ سڀ کان وڌيڪ سهڻي آهي", "Hooa sabh khaan wadhik suhni aahi"],
        ["This is the best food", "هي سڀ کان بهترين کاڌو آهي", "Hee sabh khaan behatareen khaadho aahi"],
        ["My house is bigger than yours", "منهنجو گهر توهان جي کان وڏو آهي", "Muhhinjo ghar tawhan ji khaan waddo aahi"],
        ["He runs faster than me", "هو مون کان تيز ڊوڙي ٿو", "Hoo moon khaan tez ddori tho"],
        ["She sings better than him", "هوءَ هن کان بهتر ڳائي ٿي", "Hooa hun khaan behtar gaai thee"],
        ["This is the cheapest item", "هي سڀ کان سستي شئي آهي", "Hee sabh khaan sasti shai aahi"],
        ["He is older than his brother", "هو پنهنجي ڀاءُ کان وڏو آهي", "Hoo panhinji bhaau khaan waddo aahi"],
        ["She is younger than me", "هوءَ مون کان ننڍي آهي", "Hooa moon khaan nandhi aahi"],
        ["This road is longer", "هي رستو وڌيڪ ڊگهو آهي", "Hee rasto wadhik ddagho aahi"],
        ["The Indus is the longest river", "سنڌو سڀ کان ڊگهي ندي آهي", "Sindhu sabh khaan ddaghi nadi aahi"],
        ["He is as tall as his father", "هو پنهنجي پيءُ جيتري ڊگهائي آهي", "Hoo panhinji piyu jetri ddaghaaee aahi"],
        ["She is as smart as her sister", "هوءَ پنهنجي ڀيڻ جيتري هوشيار آهي", "Hooa panhinji bhain jetri hoshiyaar aahi"],
        ["This tea is hotter than that", "هي چانهه ان کان وڌيڪ گرم آهي", "Hee chaanhh un khaan wadhik garam aahi"],
        ["He is the strongest boy", "هو سڀ کان مضبوط ڇوڪرو آهي", "Hoo sabh khaan mazboot chhokro aahi"],
    ]
}

lessons[556] = {
    "heading": "Using verb 'To Know' in Sindhi",
    "rows": [
        ["I know Sindhi", "مان سنڌي ڄاڻان ٿو", "Maan Sindhi jaanaan tho"],
        ["He knows the way", "هو رستو ڄاڻي ٿو", "Hoo rasto jaani tho"],
        ["She knows how to cook", "هوءَ پچائڻ ڄاڻي ٿي", "Hooa pachaainann jaani thee"],
        ["We know each other", "اسين هڪ ٻئي کي ڄاڻون ٿا", "Aseen hik bee khe jaanoon thaa"],
        ["They know the truth", "اهي سچ ڄاڻن ٿا", "Ahee sach jaanan thaa"],
        ["I don't know", "مان نٿو ڄاڻان", "Maan natho jaanaan"],
        ["He doesn't know her", "هو هنيءَ کي نٿو ڄاڻي", "Hoo huniya khe natho jaani"],
        ["She doesn't know the answer", "هوءَ جواب نٿي ڄاڻي", "Hooa jawaab nathi jaani"],
        ["Do you know him?", "ڇا توهان هن کي ڄاڻو ٿا؟", "Chhaa tawhan hun khe jaano thaa?"],
        ["I knew the answer", "مان جواب ڄاڻندو هئس", "Maan jawaab jaanando huas"],
        ["He knew the truth", "هو سچ ڄاڻندو هو", "Hoo sach jaanando ho"],
        ["She knew about the plan", "هوءَ منصوبي بابت ڄاڻندي هئي", "Hooa mansoobe baabat jaanandi hui"],
        ["I will know soon", "مون کي جلدي خبر پوندي", "Moon khe jaldi khabar pondi"],
        ["Who knows the answer?", "ڪنهن کي جواب خبر آهي؟", "Kunhan khe jawaab khabar aahi?"],
        ["Everyone knows him", "سڀ هن کي ڄاڻن ٿا", "Sabh hun khe jaanan thaa"],
        ["I know how to swim", "مان ترنو ڄاڻان ٿو", "Maan tarano jaanaan tho"],
        ["She knows three languages", "هوءَ ٽي ٻوليون ڄاڻي ٿي", "Hooa tee boliyoon jaani thee"],
        ["He doesn't know how to drive", "هو ڳاڏي هلائڻ نٿو ڄاڻي", "Hoo gaadi halaainann natho jaani"],
    ]
}

lessons[557] = {
    "heading": "Using 'Let' and 'Shall we' in Sindhi",
    "rows": [
        ["Let me go", "مون کي وڃڻ ڏيو", "Moon khe wachann diyo"],
        ["Let him eat", "هن کي کائڻ ڏيو", "Hun khe khaainann diyo"],
        ["Let her sleep", "هنيءَ کي سمهڻ ڏيو", "Huniya khe sumhann diyo"],
        ["Let us study", "اسان کي پڙهڻ ڏيو", "Asaan khe parhann diyo"],
        ["Let them play", "انهن کي کيڏڻ ڏيو", "Unhan khe kheddann diyo"],
        ["Shall we go?", "ڇا اسين هلون؟", "Chhaa aseen haloon?"],
        ["Shall we eat?", "ڇا اسين کائون؟", "Chhaa aseen khaayoon?"],
        ["Shall we play?", "ڇا اسين کيڏون؟", "Chhaa aseen kheddoon?"],
        ["Let me try", "مون کي ڪوشش ڪرڻ ڏيو", "Moon khe koshish karann diyo"],
        ["Let him speak", "هن کي ڳالهائڻ ڏيو", "Hun khe gaalhaaynann diyo"],
        ["Let her decide", "هنيءَ کي فيصلو ڪرڻ ڏيو", "Huniya khe faislo karann diyo"],
        ["Shall we start?", "ڇا اسين شروع ڪريون؟", "Chhaa aseen shuroo kariyoon?"],
        ["Let me think", "مون کي سوچڻ ڏيو", "Moon khe sochann diyo"],
        ["Let them go home", "انهن کي گهر وڃڻ ڏيو", "Unhan khe ghar wachann diyo"],
        ["Shall we go to the market?", "ڇا اسين بازار هلون؟", "Chhaa aseen bazaar haloon?"],
        ["Let the children play", "ٻارن کي کيڏڻ ڏيو", "Baarann khe kheddann diyo"],
        ["Shall we have tea?", "ڇا اسين چانهه پيئون؟", "Chhaa aseen chaanhh piyoon?"],
        ["Let me help you", "مون کي توهان جي مدد ڪرڻ ڏيو", "Moon khe tawhan ji madad karann diyo"],
    ]
}

lessons[558] = {
    "heading": "Which-That / What-That sentences in Sindhi",
    "rows": [
        ["The book that I read was good", "جيڪا ڪتاب مون پڙهي سا سٺي هئي", "Jekaa kitaab moon parhi saa suthi hui"],
        ["The man who came was my friend", "جيڪو ماڻهو آيو سو منهنجو دوست هو", "Jeko maanho aayo so muhhinjo dost ho"],
        ["What you said is correct", "جيڪو توهان چيو سو صحيح آهي", "Jeko tawhan chiyo so sahih aahi"],
        ["The food that she cooked was delicious", "جيڪو کاڌو هنيءَ پچايو سو مزيدار هو", "Jeko khaadho huniya pachaaiyo so mazidaar ho"],
        ["Which house is yours?", "ڪهڙو گهر توهان جو آهي؟", "Kahro ghar tawhan jo aahi?"],
        ["That which is true will remain", "جيڪو سچ آهي سو قائم رهندو", "Jeko sach aahi so qaayim rahando"],
        ["The teacher who taught us was kind", "جيڪو استاد اسان کي پڙهايو سو مهربان هو", "Jeko ustaad asaan khe parhaaiyo so meherbaan ho"],
        ["What happened was unexpected", "جيڪو ٿيو سو غير متوقع هو", "Jeko thiyo so ghair mutawaqqa ho"],
        ["The river that flows here is the Indus", "جيڪا ندي هتي وهي ٿي سا سنڌو آهي", "Jekaa nadi hite wahi thee saa Sindhu aahi"],
        ["The song that she sang was beautiful", "جيڪو گيت هنيءَ ڳايو سو سهڻو هو", "Jeko geet huniya gaaiyo so suhno ho"],
        ["I believe what you say", "مان يقين ڪريان ٿو جيڪو توهان چوندا آهيو", "Maan yaqeen kariyaan tho jeko tawhan chondaa aahiyo"],
        ["The place where we met was peaceful", "جيڪي جاءِ اسين مليا سين سا پرامن هئي", "Jeki jaai aseen miliyaa sin saa puraman hui"],
        ["What he did was wrong", "جيڪو هن ڪيو سو غلط هو", "Jeko hun kiyo so ghalat ho"],
        ["The girl who won is talented", "جيڪا ڇوڪري کٽي سا ذهين آهي", "Jekaa chhokri khati saa zaheen aahi"],
        ["Which one do you like?", "توهان کي ڪهڙو پسند آهي؟", "Tawhan khe kahro pasand aahi?"],
        ["That which I feared happened", "جنهن جو مون کي ڊپ هو سو ئي ٿيو", "Junhan jo moon khe ddap ho so ee thiyo"],
        ["What she knows is useful", "جيڪو هوءَ ڄاڻي ٿي سو ڪارآمد آهي", "Jeko hooa jaani thee so kaaraamad aahi"],
        ["The car that he bought is new", "جيڪا ڪار هن خريد ڪئي سا نئين آهي", "Jekaa kaar hun khareed kai saa naeen aahi"],
    ]
}

lessons[559] = {
    "heading": "Giving instructions formally in Sindhi",
    "rows": [
        ["Please open the book to page 10", "مهرباني ڪري ڪتاب جو صفحو 10 کوليو", "Meherbaani kari kitaab jo safho 10 kholiyo"],
        ["Kindly fill out the form", "مهرباني ڪري فارم ڀريو", "Meherbaani kari form bhariyo"],
        ["Please submit your report by Friday", "مهرباني ڪري جمعي تائين رپورٽ جمع ڪرايو", "Meherbaani kari jumai taaeen report jamaa karaaiyo"],
        ["Kindly wait in the lobby", "مهرباني ڪري لابي ۾ انتظار ڪريو", "Meherbaani kari lobby me intezaar kariyo"],
        ["Please take your seat", "مهرباني ڪري پنهنجي جاءِ تي ويهي رهو", "Meherbaani kari panhinji jaai te weihi raho"],
        ["Kindly return the documents", "مهرباني ڪري دستاويز واپس ڪريو", "Meherbaani kari dastaawez waapas kariyo"],
        ["Please sign here", "مهرباني ڪري هتي دستخط ڪريو", "Meherbaani kari hite dastakhat kariyo"],
        ["Kindly maintain silence", "مهرباني ڪري خاموشي رکو", "Meherbaani kari khaamoshi rakho"],
        ["Please arrive on time", "مهرباني ڪري وقت تي اچو", "Meherbaani kari waqt te acho"],
        ["Kindly read the instructions carefully", "مهرباني ڪري هدايتون غور سان پڙهو", "Meherbaani kari hidaayatoon ghour saan parho"],
        ["Please bring your ID card", "مهرباني ڪري پنهنجو شناختي ڪارڊ آڻيو", "Meherbaani kari panhinjo shinaakhti card aaniyo"],
        ["Kindly switch off your phone", "مهرباني ڪري پنهنجو فون بند ڪريو", "Meherbaani kari panhinjo phone band kariyo"],
        ["Please do not litter", "مهرباني ڪري ڪچرو نه اُڇلو", "Meherbaani kari kachro na uchlo"],
        ["Kindly pay at the counter", "مهرباني ڪري ڪائونٽر تي ادائگي ڪريو", "Meherbaani kari counter te adaaigi kariyo"],
        ["Please stand in line", "مهرباني ڪري قطار ۾ بيٺا ٿيو", "Meherbaani kari qataar me bethaa thiyo"],
        ["Kindly cooperate with us", "مهرباني ڪري اسان سان تعاون ڪريو", "Meherbaani kari asaan saan taawon kariyo"],
        ["Please take care of the property", "مهرباني ڪري جائداد جو خيال رکو", "Meherbaani kari jaaidaad jo khiyaal rakho"],
        ["Kindly report to the reception", "مهرباني ڪري استقبال تي رپورٽ ڪريو", "Meherbaani kari istiqbaal te report kariyo"],
    ]
}

# 560-569 will continue in the next batch
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

print(f"Section 3a (543-559) populated: {len(lessons)} lessons")
for lid in sorted(lessons.keys()):
    nr = len(lessons[lid]['rows'])
    print(f"  {lid}: {nr} rows")
