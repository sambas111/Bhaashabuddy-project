"""
Universal lesson populator for BhaashaBuddy languages.
Usage: python populate_all_lang.py <lang_key>
Supported: dogri, sanskrit, bodo, urdu, konkani
"""
import json, sys

LANG = sys.argv[1] if len(sys.argv) > 1 else 'dogri'

LANG_DATA = {
    'dogri': {
        'name': 'Dogri', 'script': 'Devanagari', 'col': 'Dogri',
        'hello': 'नमस्कार', 'hello_r': 'Namaskaar',
        'howareyou': 'तुस कनै ओ?', 'howareyou_r': 'Tus kanai o?',
        'iamfine': 'मैं ठीक आं', 'iamfine_r': 'Main theek aan',
        'thankyou': 'धन्नवाद', 'thankyou_r': 'Dhannavaad',
        'yes': 'हां', 'yes_r': 'Haan', 'no': 'नेईं', 'no_r': 'Nein',
        'water': 'पानी', 'water_r': 'Paani',
        'food': 'खाणा', 'food_r': 'Khaana',
        'house': 'घर', 'house_r': 'Ghar',
        'school': 'सकूल', 'school_r': 'Sakool',
        'mother': 'मांह्', 'mother_r': 'Maanh',
        'father': 'पिउ', 'father_r': 'Piu',
        'come': 'औ', 'come_r': 'Au', 'go': 'जा', 'go_r': 'Ja',
        'good': 'चंगा', 'good_r': 'Changa', 'bad': 'मंदा', 'bad_r': 'Manda',
        'i': 'मैं', 'i_r': 'Main', 'you': 'तू', 'you_r': 'Tu',
        'you_h': 'तुस', 'you_h_r': 'Tus',
        'what': 'कीह्', 'what_r': 'Keeh', 'where': 'कुत्थै', 'where_r': 'Kutthai',
        'when': 'कदूं', 'when_r': 'Kadoon', 'why': 'कीजो', 'why_r': 'Keejo',
        'who': 'कुण', 'who_r': 'Kun', 'how': 'किय्यां', 'how_r': 'Kiyyaan',
        'big': 'बड्डा', 'big_r': 'Badda', 'small': 'निक्का', 'small_r': 'Nikka',
        'today': 'अज्ज', 'today_r': 'Ajj', 'tomorrow': 'सवेर', 'tomorrow_r': 'Saver',
        'market': 'बजार', 'market_r': 'Bajaar',
        'doctor': 'डाक्टर', 'doctor_r': 'Daaktar',
        'please': 'किरपा करियै', 'please_r': 'Kirpa kariyai',
        'give': 'दे', 'give_r': 'De', 'eat': 'खा', 'eat_r': 'Kha',
        'region': 'Jammu', 'region_r': 'जम्मू',
        'iwant': 'मिगी चाहिदा ऐ', 'iwant_r': 'Migi chaahida ai',
        'imgoing': 'मैं जा करदा/करदी आं', 'imgoing_r': 'Main ja karda/kardi aan',
        'dontknow': 'मिगी नेईं पता', 'dontknow_r': 'Migi nein pata',
        'rice': 'भात', 'rice_r': 'Bhaat', 'milk': 'दुद्ध', 'milk_r': 'Duddh',
        'one': 'इक्क', 'one_r': 'Ikk', 'two': 'दोह्', 'two_r': 'Doh',
        'three': 'त्रै', 'three_r': 'Trai',
        'sun': 'सूरज', 'sun_r': 'Sooraj', 'moon': 'चन्न', 'moon_r': 'Chann',
        'rain': 'मींह्', 'rain_r': 'Meenh', 'tree': 'बूटा', 'tree_r': 'Boota',
        'river': 'दरिया', 'river_r': 'Dariya',
        'bird': 'पंछी', 'bird_r': 'Panchhi',
        'dog': 'कुत्ता', 'dog_r': 'Kutta', 'cat': 'बिल्ली', 'cat_r': 'Billi',
        'love': 'मैं तुसा गैल प्यार करदा/करदी आं', 'love_r': 'Main tusa gail pyaar karda/kardi aan',
        'sorry': 'माफ करो', 'sorry_r': 'Maaf karo',
        'welcome': 'जी आयां नूं', 'welcome_r': 'Ji aayaan noon',
        'night': 'रात', 'night_r': 'Raat', 'morning': 'सवेर', 'morning_r': 'Saver',
        'alphabet_title': 'Dogri Devanagari Alphabet',
        'vowels': [['अ','a'],['आ','aa'],['इ','i'],['ई','ee'],['उ','u'],['ऊ','oo'],['ए','e'],['ऐ','ai'],['ओ','o'],['औ','au'],['अं','an'],['अः','ah']],
        'consonants': [['क','ka'],['ख','kha'],['ग','ga'],['घ','gha'],['ङ','nga'],['च','cha'],['छ','chha'],['ज','ja'],['झ','jha'],['ञ','nya'],['ट','ta'],['ठ','tha'],['ड','da'],['ढ','dha'],['ण','na'],['त','ta'],['थ','tha'],['द','da'],['ध','dha'],['न','na'],['प','pa'],['फ','pha'],['ब','ba'],['भ','bha'],['म','ma'],['य','ya'],['र','ra'],['ल','la'],['व','va'],['श','sha'],['ष','sha'],['स','sa'],['ह','ha'],['क्ष','ksha'],['त्र','tra'],['ज्ञ','gya']],
    },
    'sanskrit': {
        'name': 'Sanskrit', 'script': 'Devanagari', 'col': 'Sanskrit',
        'hello': 'नमस्कारः', 'hello_r': 'Namaskarah',
        'howareyou': 'कथम् अस्ति भवान्?', 'howareyou_r': 'Katham asti bhavaan?',
        'iamfine': 'अहम् कुशलम् अस्मि', 'iamfine_r': 'Aham kushalam asmi',
        'thankyou': 'धन्यवादः', 'thankyou_r': 'Dhanyavaadah',
        'yes': 'आम्', 'yes_r': 'Aam', 'no': 'न', 'no_r': 'Na',
        'water': 'जलम्', 'water_r': 'Jalam',
        'food': 'भोजनम्', 'food_r': 'Bhojanam',
        'house': 'गृहम्', 'house_r': 'Gruham',
        'school': 'विद्यालयः', 'school_r': 'Vidyaalayah',
        'mother': 'माता', 'mother_r': 'Maata',
        'father': 'पिता', 'father_r': 'Pitaa',
        'come': 'आगच्छतु', 'come_r': 'Aagachchhatu', 'go': 'गच्छतु', 'go_r': 'Gachchhatu',
        'good': 'उत्तमम्', 'good_r': 'Uttamam', 'bad': 'अशुभम्', 'bad_r': 'Ashubham',
        'i': 'अहम्', 'i_r': 'Aham', 'you': 'त्वम्', 'you_r': 'Tvam',
        'you_h': 'भवान्', 'you_h_r': 'Bhavaan',
        'what': 'किम्', 'what_r': 'Kim', 'where': 'कुत्र', 'where_r': 'Kutra',
        'when': 'कदा', 'when_r': 'Kadaa', 'why': 'किमर्थम्', 'why_r': 'Kimartham',
        'who': 'कः', 'who_r': 'Kah', 'how': 'कथम्', 'how_r': 'Katham',
        'big': 'विशालम्', 'big_r': 'Vishaalam', 'small': 'लघु', 'small_r': 'Laghu',
        'today': 'अद्य', 'today_r': 'Adya', 'tomorrow': 'श्वः', 'tomorrow_r': 'Shvah',
        'market': 'आपणम्', 'market_r': 'Aapanam',
        'doctor': 'वैद्यः', 'doctor_r': 'Vaidyah',
        'please': 'कृपया', 'please_r': 'Krupayaa',
        'give': 'ददातु', 'give_r': 'Dadaatu', 'eat': 'खादतु', 'eat_r': 'Khaadatu',
        'region': 'Bharat', 'region_r': 'भारत',
        'iwant': 'मम इच्छा अस्ति', 'iwant_r': 'Mama ichchhaa asti',
        'imgoing': 'अहम् गच्छामि', 'imgoing_r': 'Aham gachchhaami',
        'dontknow': 'अहम् न जानामि', 'dontknow_r': 'Aham na jaanaami',
        'rice': 'तण्डुलम्', 'rice_r': 'Tandulam', 'milk': 'दुग्धम्', 'milk_r': 'Dugdham',
        'one': 'एकम्', 'one_r': 'Ekam', 'two': 'द्वे', 'two_r': 'Dve',
        'three': 'त्रीणि', 'three_r': 'Treeni',
        'sun': 'सूर्यः', 'sun_r': 'Sooryah', 'moon': 'चन्द्रः', 'moon_r': 'Chandrah',
        'rain': 'वर्षा', 'rain_r': 'Varshaa', 'tree': 'वृक्षः', 'tree_r': 'Vrukshah',
        'river': 'नदी', 'river_r': 'Nadee',
        'bird': 'खगः', 'bird_r': 'Khagah',
        'dog': 'श्वानः', 'dog_r': 'Shvaanah', 'cat': 'मार्जारः', 'cat_r': 'Maarjaarah',
        'love': 'अहम् त्वाम् स्नेहयामि', 'love_r': 'Aham tvaam snehayaami',
        'sorry': 'क्षम्यताम्', 'sorry_r': 'Kshamyataam',
        'welcome': 'स्वागतम्', 'welcome_r': 'Svaagatam',
        'night': 'रात्रिः', 'night_r': 'Raatrih', 'morning': 'प्रातःकालः', 'morning_r': 'Praatahkaalah',
        'alphabet_title': 'Sanskrit Devanagari Alphabet',
        'vowels': [['अ','a'],['आ','aa'],['इ','i'],['ई','ee'],['उ','u'],['ऊ','oo'],['ऋ','ru'],['ॠ','roo'],['ए','e'],['ऐ','ai'],['ओ','o'],['औ','au'],['अं','am'],['अः','ah']],
        'consonants': [['क','ka'],['ख','kha'],['ग','ga'],['घ','gha'],['ङ','nga'],['च','cha'],['छ','chha'],['ज','ja'],['झ','jha'],['ञ','nya'],['ट','ta'],['ठ','tha'],['ड','da'],['ढ','dha'],['ण','na'],['त','ta'],['थ','tha'],['द','da'],['ध','dha'],['न','na'],['प','pa'],['फ','pha'],['ब','ba'],['भ','bha'],['म','ma'],['य','ya'],['र','ra'],['ल','la'],['व','va'],['श','sha'],['ष','sha'],['स','sa'],['ह','ha'],['क्ष','ksha'],['त्र','tra'],['ज्ञ','gya']],
    },
    'bodo': {
        'name': 'Bodo', 'script': 'Devanagari', 'col': 'Bodo',
        'hello': 'मोजांग बे', 'hello_r': 'Mojang be',
        'howareyou': 'नों मोजांग दं ना?', 'howareyou_r': 'Nong mojang dong na?',
        'iamfine': 'आं मोजांग दं', 'iamfine_r': 'Ang mojang dong',
        'thankyou': 'थांनाय', 'thankyou_r': 'Thangnai',
        'yes': 'हो', 'yes_r': 'Ho', 'no': 'हाया', 'no_r': 'Haya',
        'water': 'दै', 'water_r': 'Dai',
        'food': 'जा', 'food_r': 'Ja',
        'house': 'नो', 'house_r': 'No',
        'school': 'सिगां फोर', 'school_r': 'Sigaang phor',
        'mother': 'आमा', 'mother_r': 'Ama',
        'father': 'आफा', 'father_r': 'Apha',
        'come': 'फै', 'come_r': 'Phai', 'go': 'थां', 'go_r': 'Thang',
        'good': 'मोजां', 'good_r': 'Mojang', 'bad': 'गाज्रि', 'bad_r': 'Gajri',
        'i': 'आं', 'i_r': 'Ang', 'you': 'नों', 'you_r': 'Nong',
        'you_h': 'बिसोर', 'you_h_r': 'Bisor',
        'what': 'मा', 'what_r': 'Ma', 'where': 'बेसे', 'where_r': 'Bese',
        'when': 'मोब्लब', 'when_r': 'Moblab', 'why': 'माबोरै', 'why_r': 'Maborai',
        'who': 'सोर', 'who_r': 'Sor', 'how': 'मालामा', 'how_r': 'Malama',
        'big': 'गेदेर', 'big_r': 'Geder', 'small': 'गोथो', 'small_r': 'Gotho',
        'today': 'दिनै', 'today_r': 'Dinai', 'tomorrow': 'गाबोन', 'tomorrow_r': 'Gabon',
        'market': 'बजार', 'market_r': 'Bajaar',
        'doctor': 'डाक्टर', 'doctor_r': 'Daktar',
        'please': 'दयाखौ', 'please_r': 'Dayakhou',
        'give': 'हो', 'give_r': 'Ho', 'eat': 'जा', 'eat_r': 'Ja',
        'region': 'Assam', 'region_r': 'असम',
        'iwant': 'आंनो दोंमोन', 'iwant_r': 'Angno dongmon',
        'imgoing': 'आं थानो दं', 'imgoing_r': 'Ang thano dong',
        'dontknow': 'आं मिथिया', 'dontknow_r': 'Ang mithiya',
        'rice': 'ओंखाम', 'rice_r': 'Ongkham', 'milk': 'दुध', 'milk_r': 'Dudh',
        'one': 'से', 'one_r': 'Se', 'two': 'नै', 'two_r': 'Nai',
        'three': 'थाम', 'three_r': 'Tham',
        'sun': 'सान', 'sun_r': 'San', 'moon': 'हा', 'moon_r': 'Ha',
        'rain': 'हाब्रा', 'rain_r': 'Habra', 'tree': 'बिफां', 'tree_r': 'Biphang',
        'river': 'दैमा', 'river_r': 'Daima',
        'bird': 'दाव', 'bird_r': 'Dau',
        'dog': 'सा', 'dog_r': 'Sa', 'cat': 'मोसो', 'cat_r': 'Moso',
        'love': 'आं नोंथांनो मोजां मोन्नो', 'love_r': 'Ang nongthaangno mojang monno',
        'sorry': 'माफ खौ', 'sorry_r': 'Maaf khou',
        'welcome': 'मोजांग बे', 'welcome_r': 'Mojang be',
        'night': 'सान्जा', 'night_r': 'Sanja', 'morning': 'हादथ', 'morning_r': 'Haadoth',
        'alphabet_title': 'Bodo Devanagari Alphabet',
        'vowels': [['अ','a'],['आ','aa'],['इ','i'],['ई','ee'],['उ','u'],['ऊ','oo'],['ए','e'],['ऐ','ai'],['ओ','o'],['औ','au']],
        'consonants': [['क','ka'],['ख','kha'],['ग','ga'],['घ','gha'],['ङ','nga'],['च','cha'],['छ','chha'],['ज','ja'],['झ','jha'],['ञ','nya'],['ट','ta'],['ठ','tha'],['ड','da'],['ढ','dha'],['ण','na'],['त','ta'],['थ','tha'],['द','da'],['ध','dha'],['न','na'],['प','pa'],['फ','pha'],['ब','ba'],['भ','bha'],['म','ma'],['य','ya'],['र','ra'],['ल','la'],['व','va'],['श','sha'],['स','sa'],['ह','ha']],
    },
    'urdu': {
        'name': 'Urdu', 'script': 'Nastaliq', 'col': 'Urdu',
        'hello': 'السلام علیکم', 'hello_r': 'Assalamu Alaikum',
        'howareyou': 'آپ کیسے ہیں؟', 'howareyou_r': 'Aap kaise hain?',
        'iamfine': 'میں ٹھیک ہوں', 'iamfine_r': 'Main theek hoon',
        'thankyou': 'شکریہ', 'thankyou_r': 'Shukriya',
        'yes': 'ہاں', 'yes_r': 'Haan', 'no': 'نہیں', 'no_r': 'Nahin',
        'water': 'پانی', 'water_r': 'Paani',
        'food': 'کھانا', 'food_r': 'Khaana',
        'house': 'گھر', 'house_r': 'Ghar',
        'school': 'مدرسہ', 'school_r': 'Madrasa',
        'mother': 'امی', 'mother_r': 'Ammi',
        'father': 'ابو', 'father_r': 'Abbu',
        'come': 'آئیں', 'come_r': 'Aayen', 'go': 'جائیں', 'go_r': 'Jaayen',
        'good': 'اچھا', 'good_r': 'Achha', 'bad': 'برا', 'bad_r': 'Bura',
        'i': 'میں', 'i_r': 'Main', 'you': 'تم', 'you_r': 'Tum',
        'you_h': 'آپ', 'you_h_r': 'Aap',
        'what': 'کیا', 'what_r': 'Kya', 'where': 'کہاں', 'where_r': 'Kahaan',
        'when': 'کب', 'when_r': 'Kab', 'why': 'کیوں', 'why_r': 'Kyun',
        'who': 'کون', 'who_r': 'Kaun', 'how': 'کیسے', 'how_r': 'Kaise',
        'big': 'بڑا', 'big_r': 'Bada', 'small': 'چھوٹا', 'small_r': 'Chhota',
        'today': 'آج', 'today_r': 'Aaj', 'tomorrow': 'کل', 'tomorrow_r': 'Kal',
        'market': 'بازار', 'market_r': 'Bazaar',
        'doctor': 'ڈاکٹر', 'doctor_r': 'Daktar',
        'please': 'مہربانی', 'please_r': 'Meherbaani',
        'give': 'دیجیے', 'give_r': 'Dijiye', 'eat': 'کھائیں', 'eat_r': 'Khaayen',
        'region': 'India/Pakistan', 'region_r': 'ہندوستان/پاکستان',
        'iwant': 'مجھے چاہیے', 'iwant_r': 'Mujhe chaahiye',
        'imgoing': 'میں جا رہا ہوں', 'imgoing_r': 'Main ja raha hoon',
        'dontknow': 'مجھے نہیں معلوم', 'dontknow_r': 'Mujhe nahin maloom',
        'rice': 'چاول', 'rice_r': 'Chaawal', 'milk': 'دودھ', 'milk_r': 'Doodh',
        'one': 'ایک', 'one_r': 'Ek', 'two': 'دو', 'two_r': 'Do',
        'three': 'تین', 'three_r': 'Teen',
        'sun': 'سورج', 'sun_r': 'Sooraj', 'moon': 'چاند', 'moon_r': 'Chaand',
        'rain': 'بارش', 'rain_r': 'Baarish', 'tree': 'درخت', 'tree_r': 'Darakht',
        'river': 'دریا', 'river_r': 'Darya',
        'bird': 'پرندہ', 'bird_r': 'Parinda',
        'dog': 'کتا', 'dog_r': 'Kutta', 'cat': 'بلی', 'cat_r': 'Billi',
        'love': 'میں تم سے محبت کرتا ہوں', 'love_r': 'Main tum se mohabbat karta hoon',
        'sorry': 'معاف کیجیے', 'sorry_r': 'Maaf kijiye',
        'welcome': 'خوش آمدید', 'welcome_r': 'Khush Aamdeed',
        'night': 'رات', 'night_r': 'Raat', 'morning': 'صبح', 'morning_r': 'Subah',
        'alphabet_title': 'Urdu Alphabet (Nastaliq Script)',
        'vowels': [['ا','alif'],['و','wao'],['ی','ye'],['ے','badi ye']],
        'consonants': [['ب','be'],['پ','pe'],['ت','te'],['ٹ','te'],['ث','se'],['ج','jeem'],['چ','che'],['ح','he'],['خ','khe'],['د','daal'],['ڈ','daal'],['ذ','zaal'],['ر','re'],['ڑ','re'],['ز','ze'],['ژ','zhe'],['س','seen'],['ش','sheen'],['ص','suaad'],['ض','zuaad'],['ط','toe'],['ظ','zoe'],['ع','ain'],['غ','ghain'],['ف','fe'],['ق','qaaf'],['ک','kaaf'],['گ','gaaf'],['ل','laam'],['م','meem'],['ن','noon'],['ہ','he'],['ء','hamza']],
    },
    'konkani': {
        'name': 'Konkani', 'script': 'Devanagari', 'col': 'Konkani',
        'hello': 'नमस्कार', 'hello_r': 'Namaskaar',
        'howareyou': 'तुमी कशें आसात?', 'howareyou_r': 'Tumi kashem asaat?',
        'iamfine': 'हांव बरो/बरी आसां', 'iamfine_r': 'Haanv baro/bari asaan',
        'thankyou': 'देव बरें करूं', 'thankyou_r': 'Dev barem karun',
        'yes': 'व्हय', 'yes_r': 'Vhay', 'no': 'ना', 'no_r': 'Naa',
        'water': 'उदक', 'water_r': 'Udak',
        'food': 'जेवण', 'food_r': 'Jevan',
        'house': 'घर', 'house_r': 'Ghor',
        'school': 'इसकूल', 'school_r': 'Iskool',
        'mother': 'आवय', 'mother_r': 'Aavay',
        'father': 'बापूय', 'father_r': 'Baapuy',
        'come': 'ये', 'come_r': 'Ye', 'go': 'वच', 'go_r': 'Voch',
        'good': 'बरें', 'good_r': 'Barem', 'bad': 'वायट', 'bad_r': 'Vaait',
        'i': 'हांव', 'i_r': 'Haanv', 'you': 'तूं', 'you_r': 'Tum',
        'you_h': 'तुमी', 'you_h_r': 'Tumi',
        'what': 'कितें', 'what_r': 'Kitem', 'where': 'खंय', 'where_r': 'Khaniy',
        'when': 'केन्ना', 'when_r': 'Kenna', 'why': 'कित्याक', 'why_r': 'Kityaak',
        'who': 'कोण', 'who_r': 'Kon', 'how': 'कशें', 'how_r': 'Kashem',
        'big': 'व्हड', 'big_r': 'Vhad', 'small': 'ल्हान', 'small_r': 'Lhaan',
        'today': 'आयज', 'today_r': 'Aayaj', 'tomorrow': 'फाल्यां', 'tomorrow_r': 'Phaalyaan',
        'market': 'बाजार', 'market_r': 'Baajaar',
        'doctor': 'दोतोर', 'doctor_r': 'Dotor',
        'please': 'उपकार करून', 'please_r': 'Upkaar karun',
        'give': 'दी', 'give_r': 'Di', 'eat': 'खा', 'eat_r': 'Kha',
        'region': 'Goa', 'region_r': 'गोंय',
        'iwant': 'म्हाका जाय', 'iwant_r': 'Mhaka jaay',
        'imgoing': 'हांव वचतां', 'imgoing_r': 'Haanv vochtaan',
        'dontknow': 'म्हाका खबर ना', 'dontknow_r': 'Mhaka khabar naa',
        'rice': 'शित', 'rice_r': 'Shit', 'milk': 'दूद', 'milk_r': 'Dud',
        'one': 'एक', 'one_r': 'Ek', 'two': 'दोन', 'two_r': 'Don',
        'three': 'तीन', 'three_r': 'Teen',
        'sun': 'सूर्य', 'sun_r': 'Surya', 'moon': 'चंद्र', 'moon_r': 'Chandra',
        'rain': 'पावस', 'rain_r': 'Paavus', 'tree': 'रूक', 'tree_r': 'Ruk',
        'river': 'न्हंय', 'river_r': 'Nhainiy',
        'bird': 'सुकणें', 'bird_r': 'Suknnem',
        'dog': 'पेटो', 'dog_r': 'Peto', 'cat': 'मांजर', 'cat_r': 'Maanjar',
        'love': 'हांव तुका मोग करतां', 'love_r': 'Haanv tuka mog kartaan',
        'sorry': 'म्हाका माफ कर', 'sorry_r': 'Mhaka maaf kar',
        'welcome': 'बरें आयलात', 'welcome_r': 'Barem aaylaat',
        'night': 'रात', 'night_r': 'Raat', 'morning': 'सकाळ', 'morning_r': 'Sakaal',
        'alphabet_title': 'Konkani Devanagari Alphabet',
        'vowels': [['अ','a'],['आ','aa'],['इ','i'],['ई','ee'],['उ','u'],['ऊ','oo'],['ए','e'],['ऐ','ai'],['ओ','o'],['औ','au'],['अं','an'],['अः','ah']],
        'consonants': [['क','ka'],['ख','kha'],['ग','ga'],['घ','gha'],['ङ','nga'],['च','cha'],['छ','chha'],['ज','ja'],['झ','jha'],['ञ','nya'],['ट','ta'],['ठ','tha'],['ड','da'],['ढ','dha'],['ण','na'],['त','ta'],['थ','tha'],['द','da'],['ध','dha'],['न','na'],['प','pa'],['फ','pha'],['ब','ba'],['भ','bha'],['म','ma'],['य','ya'],['र','ra'],['ल','la'],['व','va'],['श','sha'],['ष','sha'],['स','sa'],['ह','ha']],
    },
}

ld = LANG_DATA[LANG]
n = ld['name']
c = ld['col']

# --- Konkani (Scope B): richer English than "X in Konkani" / "topic - Example 1" ---
def konkani_lesson501_phrase_rows(ld_ref):
    """Eighteen full English gloss lines for lesson 501 second table (Devanagari phrases)."""
    return [
        ["Say hello when you greet neighbors, teachers, or elders.", ld_ref["hello"], ld_ref["hello_r"]],
        ["Thank someone warmly after they help you.", ld_ref["thankyou"], ld_ref["thankyou_r"]],
        ["Answer yes when you agree with a suggestion.", ld_ref["yes"], ld_ref["yes_r"]],
        ["Answer no softly when you cannot agree.", ld_ref["no"], ld_ref["no_r"]],
        ["Ask for water when you are thirsty on a hot day.", ld_ref["water"], ld_ref["water_r"]],
        ["Talk about food when you plan lunch or dinner.", ld_ref["food"], ld_ref["food_r"]],
        ["Point to your house when you give directions.", ld_ref["house"], ld_ref["house_r"]],
        ["Speak lovingly about your mother.", ld_ref["mother"], ld_ref["mother_r"]],
        ["Speak respectfully about your father.", ld_ref["father"], ld_ref["father_r"]],
        ["Describe something as good when you like it.", ld_ref["good"], ld_ref["good_r"]],
        ["Describe something as bad when you dislike it.", ld_ref["bad"], ld_ref["bad_r"]],
        ["Tell a friend to come closer.", ld_ref["come"], ld_ref["come_r"]],
        ["Tell someone to go ahead when the path is clear.", ld_ref["go"], ld_ref["go_r"]],
        ["Describe a big tree, house, or hill.", ld_ref["big"], ld_ref["big_r"]],
        ["Describe a small child, room, or animal.", ld_ref["small"], ld_ref["small_r"]],
        ["Talk about what you will do today.", ld_ref["today"], ld_ref["today_r"]],
        ["Mention plans you keep for tomorrow.", ld_ref["tomorrow"], ld_ref["tomorrow_r"]],
        ["Name the school where children study.", ld_ref["school"], ld_ref["school_r"]],
    ]


_KONKANI_PATTERN_OPENERS = [
    "First,", "Next,", "Then,", "After that,", "Also,", "Sometimes,",
    "When I am unsure,", "With a close friend,", "At the market,", "On the phone,",
    "Early in the morning,", "Before dinner,", "After work,", "While travelling,",
    "If I need help,", "When the teacher speaks,", "During practice,", "To sound natural,",
]

_KONKANI_VOCAB_OPENERS = [
    "At home,", "In class,", "On the street,", "While shopping,", "At a festival,",
    "With family,", "In a letter,", "On a bus,", "Near the temple,", "By the river,",
    "During homework,", "When naming things,", "In a quiz,", "On a label,",
    "Reading aloud,", "Writing slowly,", "Listening twice,", "Repeating clearly,",
]

_KONKANI_CONV_OPENERS = [
    "In this situation,", "Turn one:", "Turn two:", "Politely,", "Casually,",
    "As a beginner,", "As a guest,", "As a customer,", "As a patient,",
    "As a student,", "As a traveller,", "On a holiday,", "At the office,",
    "In the evening,", "When asking,", "When answering,", "When confirming,", "When closing,",
]


def konkani_pattern_english(topic, index):
    op = _KONKANI_PATTERN_OPENERS[index % len(_KONKANI_PATTERN_OPENERS)]
    return f"{op} I practise the pattern \"{topic}\" in Konkani."


def konkani_vocab_english(topic, index):
    op = _KONKANI_VOCAB_OPENERS[index % len(_KONKANI_VOCAB_OPENERS)]
    return f"{op} I learn a word or phrase about {topic}."


def konkani_conv_english(topic, index):
    op = _KONKANI_CONV_OPENERS[index % len(_KONKANI_CONV_OPENERS)]
    return f"{op} I use a line tied to {topic}."


def gen_s1():
    """Lessons 501-509: Script/Alphabet"""
    L = {}
    vowel_rows = [[v[0], v[1]] for v in ld['vowels']]
    cons_rows = [[c[0], c[1]] for c in ld['consonants']]
    all_rows = vowel_rows + cons_rows
    
    if LANG == 'konkani':
        intro_phrase_rows = konkani_lesson501_phrase_rows(ld)
    else:
        intro_phrase_rows = [
            [f"Hello in {n}", ld['hello'], ld['hello_r']],
            [f"Thank you in {n}", ld['thankyou'], ld['thankyou_r']],
            [f"Yes in {n}", ld['yes'], ld['yes_r']],
            [f"No in {n}", ld['no'], ld['no_r']],
            [f"Water in {n}", ld['water'], ld['water_r']],
            [f"Food in {n}", ld['food'], ld['food_r']],
            [f"House in {n}", ld['house'], ld['house_r']],
            [f"Mother in {n}", ld['mother'], ld['mother_r']],
            [f"Father in {n}", ld['father'], ld['father_r']],
            [f"Good in {n}", ld['good'], ld['good_r']],
            [f"Bad in {n}", ld['bad'], ld['bad_r']],
            [f"Come in {n}", ld['come'], ld['come_r']],
            [f"Go in {n}", ld['go'], ld['go_r']],
            [f"Big in {n}", ld['big'], ld['big_r']],
            [f"Small in {n}", ld['small'], ld['small_r']],
            [f"Today in {n}", ld['today'], ld['today_r']],
            [f"Tomorrow in {n}", ld['tomorrow'], ld['tomorrow_r']],
            [f"School in {n}", ld['school'], ld['school_r']],
        ]
    L[501] = {
        'blocks': [
            {"type":"grid","columns":["Letter","Transliteration"],"rows":all_rows},
            {"type":"table","columns":["English",c,"Transliteration"],"rows": intro_phrase_rows},
        ]
    }
    L[502] = {
        'blocks': [
            {"type":"grid","columns":["Vowel","Transliteration"],"rows":vowel_rows},
            {"type":"grid","columns":["Consonant","Transliteration"],"rows":cons_rows[:18]},
            {"type":"table","columns":["English",c,"Transliteration"],"rows":[
                ["I", ld['i'], ld['i_r']],
                ["You", ld['you'], ld['you_r']],
                [f"You (formal)", ld['you_h'], ld['you_h_r']],
                ["What", ld['what'], ld['what_r']],
                ["Where", ld['where'], ld['where_r']],
                ["When", ld['when'], ld['when_r']],
                ["Why", ld['why'], ld['why_r']],
                ["Who", ld['who'], ld['who_r']],
                ["How", ld['how'], ld['how_r']],
                ["One", ld['one'], ld['one_r']],
                ["Two", ld['two'], ld['two_r']],
                ["Three", ld['three'], ld['three_r']],
                ["Sun", ld['sun'], ld['sun_r']],
                ["Moon", ld['moon'], ld['moon_r']],
                ["Rain", ld['rain'], ld['rain_r']],
                ["Tree", ld['tree'], ld['tree_r']],
                ["River", ld['river'], ld['river_r']],
                ["Bird", ld['bird'], ld['bird_r']],
            ]}
        ]
    }
    # 503: Barakhadi / matras
    bk_rows = []
    base_cons = ld['consonants'][:10]
    for ci in base_cons:
        for vi in ld['vowels'][:5]:
            bk_rows.append([f"{ci[0]}+{vi[0]}", f"{ci[1]}{vi[1]}"])
    L[503] = {
        'blocks': [
            {"type":"grid","columns":["Combination","Sound"],"rows":bk_rows[:35]},
            {"type":"table","columns":["English",c,"Transliteration"],"rows":[
                [f"Hello ({n})", ld['hello'], ld['hello_r']],
                [f"How are you?", ld['howareyou'], ld['howareyou_r']],
                [f"I am fine", ld['iamfine'], ld['iamfine_r']],
                [f"Thank you", ld['thankyou'], ld['thankyou_r']],
                [f"Welcome", ld['welcome'], ld['welcome_r']],
                [f"Sorry", ld['sorry'], ld['sorry_r']],
                [f"Please", ld['please'], ld['please_r']],
                [f"Yes", ld['yes'], ld['yes_r']],
                [f"No", ld['no'], ld['no_r']],
                [f"Good morning", ld['morning'], ld['morning_r']],
                [f"Good night", ld['night'], ld['night_r']],
                [f"Dog", ld['dog'], ld['dog_r']],
                [f"Cat", ld['cat'], ld['cat_r']],
                [f"Water", ld['water'], ld['water_r']],
                [f"Food", ld['food'], ld['food_r']],
                [f"Milk", ld['milk'], ld['milk_r']],
                [f"Rice", ld['rice'], ld['rice_r']],
                [f"Market", ld['market'], ld['market_r']],
            ]}
        ]
    }
    # 504-509: Table-only
    tables = {
        504: [ # Pronunciation problems
            ["Hard sound vs soft sound", f"{ld['consonants'][0][0]} vs {ld['consonants'][1][0]}", f"{ld['consonants'][0][1]} vs {ld['consonants'][1][1]}"],
            ["Aspirated consonants", f"{ld['consonants'][1][0]}", ld['consonants'][1][1]],
            ["Nasal sounds", f"{ld['consonants'][4][0]}", ld['consonants'][4][1]],
            ["Retroflex sounds", f"{ld['consonants'][10][0]}" if len(ld['consonants'])>10 else "T", ld['consonants'][10][1] if len(ld['consonants'])>10 else "ta"],
            [f"The word for water", ld['water'], ld['water_r']],
            [f"The word for house", ld['house'], ld['house_r']],
            [f"The word for food", ld['food'], ld['food_r']],
            [f"The word for school", ld['school'], ld['school_r']],
            [f"The word for market", ld['market'], ld['market_r']],
            [f"The word for doctor", ld['doctor'], ld['doctor_r']],
            [f"The word for mother", ld['mother'], ld['mother_r']],
            [f"The word for father", ld['father'], ld['father_r']],
            [f"The word for sun", ld['sun'], ld['sun_r']],
            [f"The word for moon", ld['moon'], ld['moon_r']],
            [f"The word for rain", ld['rain'], ld['rain_r']],
            [f"The word for tree", ld['tree'], ld['tree_r']],
            [f"The word for bird", ld['bird'], ld['bird_r']],
            [f"The word for river", ld['river'], ld['river_r']],
        ],
        505: [ # Anusvar/Nasal
            ["Nasal sound before ka", f"{ld['consonants'][4][0]}", ld['consonants'][4][1]],
            ["Nasal sound before cha", f"{ld['consonants'][9][0]}" if len(ld['consonants'])>9 else "N", ld['consonants'][9][1] if len(ld['consonants'])>9 else "nya"],
            [f"My house", f"{ld['i']} {ld['house']}", f"{ld['i_r']} {ld['house_r']}"],
            [f"My school", f"{ld['i']} {ld['school']}", f"{ld['i_r']} {ld['school_r']}"],
            [f"My water", f"{ld['i']} {ld['water']}", f"{ld['i_r']} {ld['water_r']}"],
            [f"Your house", f"{ld['you']} {ld['house']}", f"{ld['you_r']} {ld['house_r']}"],
            [f"Your food", f"{ld['you']} {ld['food']}", f"{ld['you_r']} {ld['food_r']}"],
            [f"Good morning", ld['morning'], ld['morning_r']],
            [f"Good night", ld['night'], ld['night_r']],
            [f"Big house", f"{ld['big']} {ld['house']}", f"{ld['big_r']} {ld['house_r']}"],
            [f"Small house", f"{ld['small']} {ld['house']}", f"{ld['small_r']} {ld['house_r']}"],
            [f"One", ld['one'], ld['one_r']],
            [f"Two", ld['two'], ld['two_r']],
            [f"Three", ld['three'], ld['three_r']],
            [f"Sun", ld['sun'], ld['sun_r']],
            [f"Moon", ld['moon'], ld['moon_r']],
            [f"Thank you", ld['thankyou'], ld['thankyou_r']],
            [f"Welcome", ld['welcome'], ld['welcome_r']],
        ],
        506: [ # Combining consonants
            [f"Combined consonant 1", f"{ld['consonants'][0][0]}{ld['consonants'][10][0]}" if len(ld['consonants'])>10 else ld['consonants'][0][0], "kta"],
            [f"Combined consonant 2", f"{ld['consonants'][5][0]}{ld['consonants'][5][0]}" if len(ld['consonants'])>5 else ld['consonants'][0][0], "chcha"],
            [f"Hello", ld['hello'], ld['hello_r']],
            [f"How are you?", ld['howareyou'], ld['howareyou_r']],
            [f"I am fine", ld['iamfine'], ld['iamfine_r']],
            [f"Thank you", ld['thankyou'], ld['thankyou_r']],
            [f"Please come", f"{ld['please']} {ld['come']}", f"{ld['please_r']} {ld['come_r']}"],
            [f"Please go", f"{ld['please']} {ld['go']}", f"{ld['please_r']} {ld['go_r']}"],
            [f"What?", ld['what'], ld['what_r']],
            [f"Where?", ld['where'], ld['where_r']],
            [f"When?", ld['when'], ld['when_r']],
            [f"Why?", ld['why'], ld['why_r']],
            [f"Who?", ld['who'], ld['who_r']],
            [f"How?", ld['how'], ld['how_r']],
            [f"Good", ld['good'], ld['good_r']],
            [f"Bad", ld['bad'], ld['bad_r']],
            [f"Big", ld['big'], ld['big_r']],
            [f"Small", ld['small'], ld['small_r']],
        ],
        507: [ # Numbers
            ["One", ld['one'], ld['one_r']],
            ["Two", ld['two'], ld['two_r']],
            ["Three", ld['three'], ld['three_r']],
            [f"Hello", ld['hello'], ld['hello_r']],
            [f"Thank you", ld['thankyou'], ld['thankyou_r']],
            [f"Yes", ld['yes'], ld['yes_r']],
            [f"No", ld['no'], ld['no_r']],
            [f"Water", ld['water'], ld['water_r']],
            [f"Food", ld['food'], ld['food_r']],
            [f"House", ld['house'], ld['house_r']],
            [f"School", ld['school'], ld['school_r']],
            [f"Market", ld['market'], ld['market_r']],
            [f"Doctor", ld['doctor'], ld['doctor_r']],
            [f"Mother", ld['mother'], ld['mother_r']],
            [f"Father", ld['father'], ld['father_r']],
            [f"Sun", ld['sun'], ld['sun_r']],
            [f"Moon", ld['moon'], ld['moon_r']],
            [f"Today", ld['today'], ld['today_r']],
        ],
        508: [ # Common words practice
            [f"I", ld['i'], ld['i_r']],
            [f"You", ld['you'], ld['you_r']],
            [f"Hello", ld['hello'], ld['hello_r']],
            [f"How are you?", ld['howareyou'], ld['howareyou_r']],
            [f"I am fine", ld['iamfine'], ld['iamfine_r']],
            [f"Thank you", ld['thankyou'], ld['thankyou_r']],
            [f"Sorry", ld['sorry'], ld['sorry_r']],
            [f"Welcome", ld['welcome'], ld['welcome_r']],
            [f"Water", ld['water'], ld['water_r']],
            [f"Food", ld['food'], ld['food_r']],
            [f"House", ld['house'], ld['house_r']],
            [f"Good", ld['good'], ld['good_r']],
            [f"Bad", ld['bad'], ld['bad_r']],
            [f"Big", ld['big'], ld['big_r']],
            [f"Small", ld['small'], ld['small_r']],
            [f"Today", ld['today'], ld['today_r']],
            [f"Tomorrow", ld['tomorrow'], ld['tomorrow_r']],
            [f"Please", ld['please'], ld['please_r']],
        ],
        509: [ # Reading practice
            [f"Hello, how are you?", f"{ld['hello']}, {ld['howareyou']}", f"{ld['hello_r']}, {ld['howareyou_r']}"],
            [f"I am fine, thank you", f"{ld['iamfine']}, {ld['thankyou']}", f"{ld['iamfine_r']}, {ld['thankyou_r']}"],
            [f"Please give me water", f"{ld['please']} {ld['water']} {ld['give']}", f"{ld['please_r']} {ld['water_r']} {ld['give_r']}"],
            [f"The food is good", f"{ld['food']} {ld['good']}", f"{ld['food_r']} {ld['good_r']}"],
            [f"Where is the market?", f"{ld['market']} {ld['where']}?", f"{ld['market_r']} {ld['where_r']}?"],
            [f"Come here", f"{ld['come']}", ld['come_r']],
            [f"Go there", f"{ld['go']}", ld['go_r']],
            [f"What is your name?", f"{ld['you_h']} {ld['what']}?", f"{ld['you_h_r']} {ld['what_r']}?"],
            [f"I don't know", ld['dontknow'], ld['dontknow_r']],
            [f"Welcome!", ld['welcome'], ld['welcome_r']],
            [f"Sorry", ld['sorry'], ld['sorry_r']],
            [f"The sun is bright", f"{ld['sun']}", ld['sun_r']],
            [f"The moon is beautiful", f"{ld['moon']}", ld['moon_r']],
            [f"It is raining", f"{ld['rain']}", ld['rain_r']],
            [f"The tree is big", f"{ld['tree']} {ld['big']}", f"{ld['tree_r']} {ld['big_r']}"],
            [f"The bird is small", f"{ld['bird']} {ld['small']}", f"{ld['bird_r']} {ld['small_r']}"],
            [f"The river is long", f"{ld['river']}", ld['river_r']],
            [f"Good morning, thank you", f"{ld['morning']}, {ld['thankyou']}", f"{ld['morning_r']}, {ld['thankyou_r']}"],
        ],
    }
    for lid in range(504, 510):
        L[lid] = {'blocks': [{"type":"table","columns":["English",c,"Transliteration"],"rows":tables[lid]}]}
    return L

SENTENCE_TEMPLATES = {
    # S2: Grammar (510-542) - 33 lessons
    510: ("Gender", [
        ("The boy is playing","boy playing"),("The girl is reading","girl reading"),("He is a teacher","he teacher"),
        ("She is a doctor","she doctor"),("This is a male cat","male cat"),("This is a female dog","female dog"),
        ("The man is working","man working"),("The woman is cooking","woman cooking"),("He goes to school","he school"),
        ("She goes to market","she market"),("The son is tall","son tall"),("The daughter is smart","daughter smart"),
        ("The king is brave","king brave"),("The queen is kind","queen kind"),("The bull is strong","bull strong"),
        ("The cow gives milk","cow milk"),("Brother is elder","brother elder"),("Sister is younger","sister younger"),
    ]),
    511: ("Singular and Plural", [
        ("One book","one book"),("Many books","many books"),("One boy","one boy"),("Many boys","many boys"),
        ("One tree","one tree"),("Many trees","many trees"),("One bird","one bird"),("Many birds","many birds"),
        ("One house","one house"),("Many houses","many houses"),("One cat","one cat"),("Many cats","many cats"),
        ("One eye","one eye"),("Two eyes","two eyes"),("One hand","one hand"),("Two hands","two hands"),
        ("One child","one child"),("Many children","many children"),
    ]),
    512: ("Case markers", [
        ("I gave the book","I gave book"),("He told me","he told me"),("She went to the market","she market"),
        ("Give water to the dog","water dog"),("The food is on the table","food table"),("He came from the village","he village"),
        ("I am going with him","I with him"),("The pen is in the box","pen box"),("He works for the school","he school"),
        ("She lives near the river","she river"),("Come to my house","come my house"),("Go from here","go here"),
        ("It belongs to me","belongs me"),("The book is for you","book for you"),("He is taller than me","taller than me"),
        ("She writes with a pen","writes pen"),("The boy beside the tree","boy tree"),("Under the table","under table"),
    ]),
    513: ("Pronoun forms", [
        ("I am here","I here"),("You are there","you there"),("He is good","he good"),("She is kind","she kind"),
        ("We are friends","we friends"),("They are coming","they coming"),("This is mine","mine"),("That is yours","yours"),
        ("Who are you?","who you"),("What is this?","what this"),("Which one?","which"),("Someone came","someone"),
        ("Nobody was there","nobody"),("Everyone is happy","everyone"),("Myself","myself"),("Yourself","yourself"),
        ("Himself","himself"),("Herself","herself"),
    ]),
    514: ("Present tense", [
        ("I go","I go"),("You eat","you eat"),("He reads","he reads"),("She writes","she writes"),
        ("We play","we play"),("They work","they work"),("I drink water","I water"),("You speak well","you speak"),
        ("He runs fast","he runs"),("She sings","she sings"),("We study","we study"),("They cook","they cook"),
        ("I see the bird","I bird"),("You hear music","you music"),("He gives money","he money"),("She takes food","she food"),
        ("We come daily","we daily"),("They go home","they home"),
    ]),
    515: ("Past tense", [
        ("I went","I went"),("You ate","you ate"),("He read","he read"),("She wrote","she wrote"),
        ("We played","we played"),("They worked","they worked"),("I drank water","I water"),("You spoke well","you spoke"),
        ("He ran fast","he ran"),("She sang","she sang"),("We studied","we studied"),("They cooked","they cooked"),
        ("I saw the bird","I bird"),("You heard music","you music"),("He gave money","he money"),("She took food","she food"),
        ("We came yesterday","we yesterday"),("They went home","they home"),
    ]),
    516: ("Future tense", [
        ("I will go","I will go"),("You will eat","you will eat"),("He will read","he will read"),("She will write","she will write"),
        ("We will play","we will play"),("They will work","they will work"),("I will drink water","I will water"),
        ("You will speak","you will speak"),("He will run","he will run"),("She will sing","she will sing"),
        ("We will study","we will study"),("They will cook","they will cook"),("I will see","I will see"),
        ("You will hear","you will hear"),("He will give","he will give"),("She will take","she will take"),
        ("We will come tomorrow","we tomorrow"),("They will go home","they home"),
    ]),
    517: ("Imperative mood", [
        ("Come here","come here"),("Go there","go there"),("Sit down","sit down"),("Stand up","stand up"),
        ("Eat food","eat food"),("Drink water","drink water"),("Read the book","read book"),("Write your name","write name"),
        ("Listen carefully","listen"),("Speak clearly","speak"),("Give me water","give water"),("Take this book","take book"),
        ("Don't go","don't go"),("Don't eat that","don't eat"),("Please come","please come"),("Please sit","please sit"),
        ("Let's go","let's go"),("Let's eat","let's eat"),
    ]),
    518: ("Negative sentences", [
        ("I don't go","I don't go"),("You don't eat","you don't eat"),("He doesn't read","he doesn't"),
        ("She doesn't write","she doesn't"),("We don't play","we don't"),("They don't work","they don't"),
        ("I didn't come","I didn't"),("You didn't speak","you didn't"),("He didn't run","he didn't"),
        ("She didn't sing","she didn't"),("I will not go","I won't"),("You will not eat","you won't"),
        ("Don't do that","don't do"),("Never come late","never late"),("Nobody came","nobody"),("Nothing happened","nothing"),
        ("I have no money","no money"),("There is no water","no water"),
    ]),
    519: ("Question formation", [
        ("What is your name?","what name"),("Where do you live?","where live"),("When did you come?","when come"),
        ("Why are you late?","why late"),("Who is he?","who he"),("How are you?","how are you"),
        ("How much does this cost?","how much"),("How many people?","how many"),("Which is your house?","which house"),
        ("Is this yours?","is yours"),("Do you understand?","do understand"),("Can you come?","can come"),
        ("Will you help?","will help"),("Did you eat?","did eat"),("Are they here?","are they"),
        ("Was it good?","was good"),("Shall we go?","shall go"),("May I sit?","may sit"),
    ]),
}

# Lessons 520-542
for lid in range(520, 543):
    topics = [
        (520,"Postpositions",[("In the house","in house"),("On the table","on table"),("Under the tree","under tree"),("Near the river","near river"),("Behind the school","behind school"),("In front of me","in front"),("Between two trees","between"),("With my friend","with friend"),("From the market","from market"),("To the school","to school"),("Around the village","around"),("Above the sky","above"),("Below the bridge","below"),("Beside the road","beside"),("Towards the temple","towards"),("Without water","without"),("For the children","for children"),("After lunch","after lunch")]),
        (521,"Adjectives",[("The big house","big house"),("The small bird","small bird"),("The good boy","good boy"),("The bad road","bad road"),("The red flower","red flower"),("The old tree","old tree"),("The new book","new book"),("The tall man","tall man"),("The short girl","short girl"),("The hot food","hot food"),("The cold water","cold water"),("The sweet mango","sweet mango"),("The beautiful garden","beautiful"),("The clean room","clean room"),("The dirty clothes","dirty"),("The happy child","happy"),("The sad mother","sad"),("The round ball","round ball")]),
        (522,"Comparatives",[("He is taller than me","taller"),("She is smarter than him","smarter"),("This is better","better"),("That is worse","worse"),("The biggest tree","biggest"),("The smallest bird","smallest"),("More beautiful","more beautiful"),("Most expensive","most expensive"),("As tall as","as tall as"),("Less cold than","less cold"),("The best food","best food"),("The worst road","worst road"),("Faster than a car","faster"),("Slower than a snail","slower"),("Richer than before","richer"),("Poorer than ever","poorer"),("The longest river","longest"),("The shortest path","shortest")]),
        (523,"Adverbs",[("He runs fast","runs fast"),("She speaks slowly","speaks slowly"),("I came yesterday","yesterday"),("We will go tomorrow","tomorrow"),("He eats quickly","quickly"),("She sings beautifully","beautifully"),("They work hard","hard"),("I always study","always"),("He never lies","never"),("She often comes","often"),("We sometimes play","sometimes"),("They rarely eat out","rarely"),("Come here","here"),("Go there","there"),("Do it now","now"),("He spoke loudly","loudly"),("She walked quietly","quietly"),("I studied well","well")]),
        (524,"Conjunctions",[("I eat and drink","and"),("He or she will come","or"),("But I didn't go","but"),("Because it rained","because"),("If you come","if"),("Although it was late","although"),("Both he and she","both"),("Neither this nor that","neither"),("Either tea or coffee","either"),("So I went home","so"),("Yet he didn't stop","yet"),("While I was eating","while"),("After he left","after"),("Before sunrise","before"),("Until evening","until"),("Unless you try","unless"),("Since morning","since"),("Therefore I agreed","therefore")]),
        (525,"Relative clauses",[("The boy who came","who came"),("The book that I read","that I read"),("The house where I live","where I live"),("The time when he came","when he came"),("The reason why I left","why I left"),("Whoever comes first","whoever"),("Whatever you say","whatever"),("Wherever you go","wherever"),("Whenever you come","whenever"),("The girl whose bag","whose bag"),("The man whom I met","whom I met"),("The food which is tasty","which is"),("The day that changed","that changed"),("As much as possible","as much"),("The way he talks","the way"),("The place we visited","place visited"),("Such people who help","such who"),("The thing I wanted","thing wanted")]),
        (526,"Conditional",[("If it rains, I stay","if rains"),("If you come, I go","if you come"),("If he studies, he passes","if studies"),("If she cooks, we eat","if cooks"),("Unless you try","unless try"),("Had I known","had known"),("Were I rich","were rich"),("Should he come","should come"),("If I were you","if I were"),("If it is hot","if hot"),("Provided you agree","provided"),("Suppose it rains","suppose"),("In case of emergency","in case"),("If not for you","if not"),("As long as you try","as long"),("Whether you like it","whether"),("Even if it rains","even if"),("Only if you promise","only if")]),
        (527,"Passive voice",[("The food was cooked","was cooked"),("The book was read","was read"),("The door was opened","was opened"),("The letter was written","was written"),("Rice is eaten","is eaten"),("Water is drunk","is drunk"),("Songs are sung","are sung"),("The work was done","was done"),("The tree was cut","was cut"),("The road was built","was built"),("The child was taught","was taught"),("The house was cleaned","was cleaned"),("The clothes were washed","were washed"),("The money was given","was given"),("The ball was kicked","was kicked"),("The game was played","was played"),("The exam was taken","was taken"),("The song was heard","was heard")]),
        (528,"Causative verbs",[("I made him eat","made eat"),("She made me write","made write"),("He got the food cooked","got cooked"),("I had the clothes washed","had washed"),("She got him to read","got to read"),("They made us wait","made wait"),("I got the house cleaned","got cleaned"),("He made her sing","made sing"),("We got the car fixed","got fixed"),("She had the letter sent","had sent"),("Make him understand","make understand"),("Get it done","get done"),("Have the food served","have served"),("Let me eat","let eat"),("Let them go","let go"),("Make the children study","make study"),("Get the water boiled","get boiled"),("Have the room cleaned","have cleaned")]),
        (529,"Compound verbs",[("Eat up everything","eat up"),("Read through the book","read through"),("Write down the answer","write down"),("Pick up the pen","pick up"),("Put down the bag","put down"),("Come back home","come back"),("Go away from here","go away"),("Sit down quietly","sit down"),("Stand up straight","stand up"),("Look at this","look at"),("Listen to me","listen to"),("Think about it","think about"),("Talk to him","talk to"),("Walk along the road","walk along"),("Jump over the fence","jump over"),("Run across the field","run across"),("Fall down","fall down"),("Get up early","get up")]),
        (530,"Honorific forms",[("Please come sir","please sir"),("Please sit madam","please madam"),("Yes sir","yes sir"),("No madam","no madam"),("Thank you sir","thank sir"),("Excuse me sir","excuse sir"),("Good morning sir","morning sir"),("Goodbye madam","goodbye madam"),("How are you sir?","how sir"),("Please help me sir","help sir"),("May I come in sir?","may come"),("Please give me permission","give permission"),("Your excellency","excellency"),("Respected teacher","respected"),("Dear elder brother","dear brother"),("Dear elder sister","dear sister"),("Respected mother","respected mother"),("Respected father","respected father")]),
        (531,"Tense markers",[("I am eating now","eating now"),("I was eating then","was eating"),("I will be eating","will eating"),("I have eaten","have eaten"),("I had eaten","had eaten"),("I will have eaten","will have"),("I have been eating","have been"),("I had been eating","had been"),("He is going","is going"),("He was going","was going"),("He will go","will go"),("He has gone","has gone"),("He had gone","had gone"),("She is singing","is singing"),("She was singing","was singing"),("She has sung","has sung"),("They are playing","are playing"),("They were playing","were playing")]),
        (532,"Modal verbs",[("I can go","can go"),("You should eat","should eat"),("He must study","must study"),("She may come","may come"),("We might win","might win"),("They could help","could help"),("I would like tea","would like"),("You ought to rest","ought rest"),("He needs to work","needs work"),("She has to leave","has to"),("We can swim","can swim"),("You should sleep","should sleep"),("He must come","must come"),("May I sit?","may sit"),("Could you help?","could help"),("Would you come?","would come"),("Should I go?","should go"),("Can I eat?","can eat")]),
        (533,"Reported speech",[("He said he will come","said will come"),("She told me to go","told go"),("They said it was good","said good"),("I told him the truth","told truth"),("He asked where I live","asked where"),("She said she was tired","said tired"),("He told me to wait","told wait"),("She asked if I ate","asked if"),("They said they won","said won"),("I told her to come","told come"),("He said it was raining","said raining"),("She told me the price","told price"),("They asked for help","asked help"),("He said thank you","said thanks"),("She told me her name","told name"),("I said I don't know","said don't know"),("He asked what time","asked time"),("She said goodbye","said goodbye")]),
        (534,"Participles",[("The running boy","running boy"),("The broken glass","broken glass"),("The cooked food","cooked food"),("The written letter","written letter"),("The singing bird","singing bird"),("The fallen tree","fallen tree"),("Having eaten food","having eaten"),("Being tired, I slept","being tired"),("After finishing work","finishing work"),("While walking home","walking home"),("The playing children","playing children"),("The sleeping baby","sleeping baby"),("A painted wall","painted wall"),("The boiled water","boiled water"),("The washed clothes","washed clothes"),("A flowing river","flowing river"),("The rising sun","rising sun"),("The setting moon","setting moon")]),
        (535,"Infinitives",[("I want to go","want to go"),("She likes to sing","likes to sing"),("He needs to study","needs to study"),("We plan to travel","plan to travel"),("To eat is necessary","to eat"),("To read is good","to read"),("I came to meet you","came to meet"),("He went to buy food","went to buy"),("It is easy to learn","easy to learn"),("It is hard to forget","hard to forget"),("I hope to see you","hope to see"),("She decided to stay","decided to stay"),("He promised to come","promised to come"),("We agreed to help","agreed to help"),("To walk is healthy","to walk"),("I forgot to call","forgot to call"),("She remembered to write","remembered"),("He tried to run","tried to run")]),
        (536,"Reduplication",[("One by one","one by one"),("Slowly slowly","slowly slowly"),("Each and every","each every"),("Here and there","here there"),("Now and then","now then"),("Day by day","day by day"),("Little by little","little little"),("Again and again","again again"),("More or less","more less"),("Big big trees","big big"),("Small small birds","small small"),("Many many people","many many"),("Step by step","step step"),("Door to door","door door"),("Hand in hand","hand hand"),("Face to face","face face"),("Bit by bit","bit bit"),("Word by word","word word")]),
        (537,"Echo words",[("Tea and snacks","tea snacks"),("Food and stuff","food stuff"),("Water and all","water all"),("Books and things","books things"),("Come and go","come go"),("Here and there","here there"),("This and that","this that"),("Near and far","near far"),("Good and bad","good bad"),("Big and small","big small"),("Eating drinking","eating drinking"),("Reading writing","reading writing"),("Hot cold","hot cold"),("Sweet sour","sweet sour"),("Rich poor","rich poor"),("Young old","young old"),("Left right","left right"),("Up down","up down")]),
        (538,"Classifiers",[("One piece of cloth","piece cloth"),("A glass of water","glass water"),("A cup of tea","cup tea"),("A plate of food","plate food"),("A bunch of flowers","bunch flowers"),("A pair of shoes","pair shoes"),("A flock of birds","flock birds"),("A herd of cattle","herd cattle"),("A group of people","group people"),("A pile of books","pile books"),("A drop of water","drop water"),("A slice of bread","slice bread"),("A grain of rice","grain rice"),("A piece of wood","piece wood"),("A set of tools","set tools"),("A bundle of sticks","bundle sticks"),("A pack of cards","pack cards"),("A row of houses","row houses")]),
        (539,"Emphasis particles",[("Only I went","only I"),("Even he came","even he"),("Just water please","just water"),("Also give me food","also food"),("Indeed it is good","indeed good"),("Really you came","really came"),("Certainly I will","certainly"),("Definitely tomorrow","definitely"),("Especially this one","especially"),("Particularly good","particularly"),("Exactly right","exactly"),("Absolutely correct","absolutely"),("Too much heat","too much"),("Very good food","very good"),("So beautiful","so beautiful"),("Such a big house","such big"),("Quite nice","quite nice"),("Rather difficult","rather")]),
        (540,"Sentence connectors",[("First, eat food","first eat"),("Then, drink water","then drink"),("After that, go home","after that"),("Finally, sleep well","finally sleep"),("Moreover, it was cheap","moreover"),("However, I didn't go","however"),("Therefore, I stayed","therefore"),("Meanwhile, he came","meanwhile"),("Consequently, we won","consequently"),("Furthermore, it's tasty","furthermore"),("In addition, take this","in addition"),("On the other hand","other hand"),("As a result","as result"),("In conclusion","in conclusion"),("For example, this one","for example"),("In other words","other words"),("To sum up","sum up"),("In short, it was good","in short")]),
        (541,"Formal vs informal",[("Please come (formal)","formal come"),("Come (informal)","informal come"),("Please sit (formal)","formal sit"),("Sit (informal)","informal sit"),("How are you? (formal)","formal how"),("How are you? (informal)","informal how"),("Please eat (formal)","formal eat"),("Eat (informal)","informal eat"),("Thank you (formal)","formal thanks"),("Thanks (informal)","informal thanks"),("Good morning sir","formal morning"),("Good morning friend","informal morning"),("Please give (formal)","formal give"),("Give (informal)","informal give"),("May I go? (formal)","formal go"),("Can I go? (informal)","informal go"),("Would you help? (formal)","formal help"),("Will you help? (informal)","informal help")]),
        (542,"Common grammar mistakes",[("Wrong: I go yesterday","wrong1"),("Right: I went yesterday","right1"),("Wrong: He don't eat","wrong2"),("Right: He doesn't eat","right2"),("Wrong: She go school","wrong3"),("Right: She goes to school","right3"),("Wrong: I am go","wrong4"),("Right: I am going","right4"),("Wrong: More better","wrong5"),("Right: Better","right5"),("Wrong: Most tallest","wrong6"),("Right: Tallest","right6"),("Wrong: He goed","wrong7"),("Right: He went","right7"),("Wrong: I has eaten","wrong8"),("Right: I have eaten","right8"),("Use correct verb forms","correct forms"),("Practice makes perfect","practice")]),
    ]
    SENTENCE_TEMPLATES[lid] = topics[lid-520]

# S3: Patterns (543-596) - 54 lessons
pattern_topics = [
    (543,"This is / That is"),
    (544,"I want..."),
    (545,"I am going to..."),
    (546,"Can you...?"),
    (547,"Please give me..."),
    (548,"Where is...?"),
    (549,"How much / How many...?"),
    (550,"I like..."),
    (551,"I don't..."),
    (552,"Do you have...?"),
    (553,"I need..."),
    (554,"Let us..."),
    (555,"Should I...?"),
    (556,"What time...?"),
    (557,"Why...?"),
    (558,"Who...?"),
    (559,"When...?"),
    (560,"How to...?"),
    (561,"Because..."),
    (562,"If...then..."),
    (563,"Even though..."),
    (564,"As soon as..."),
    (565,"While..."),
    (566,"Before / After..."),
    (567,"Instead of..."),
    (568,"According to..."),
    (569,"In order to..."),
    (570,"It seems like..."),
    (571,"I used to..."),
    (572,"I have been..."),
    (573,"I wish..."),
    (574,"Compared to..."),
    (575,"Not only...but also..."),
    (576,"Either...or..."),
    (577,"Neither...nor..."),
    (578,"The more...the more..."),
    (579,"Excuse me..."),
    (580,"May I...?"),
    (581,"Could you please...?"),
    (582,"I think..."),
    (583,"I feel..."),
    (584,"I remember / I forgot..."),
    (585,"It's better to..."),
    (586,"You should..."),
    (587,"I'm sorry for..."),
    (588,"Congratulations on..."),
    (589,"I'm looking forward to..."),
    (590,"It depends on..."),
    (591,"As far as I know..."),
    (592,"In my opinion..."),
    (593,"To tell the truth..."),
    (594,"By the way..."),
    (595,"As a matter of fact..."),
    (596,"All in all..."),
]

# S4: Vocabulary (597-619) - 23 lessons
vocab_topics = [
    (597,"Body parts"),
    (598,"Miscellaneous common words"),
    (599,"Family relations"),
    (600,"Numbers 1-20"),
    (601,"Numbers and ordinals"),
    (602,"Fractions and measures"),
    (603,"Common verbs"),
    (604,"Adjectives"),
    (605,"Adverbs"),
    (606,"Vegetables"),
    (607,"Fruits"),
    (608,"Birds"),
    (609,"Insects"),
    (610,"Colours"),
    (611,"Flowers"),
    (612,"Animals (domestic)"),
    (613,"Animals (wild)"),
    (614,"Kitchen items"),
    (615,"Clothing"),
    (616,"Musical instruments"),
    (617,"Tools and implements"),
    (618,"Seasons and weather"),
    (619,"Common miscellaneous words"),
]

# S5: Conversations (620-662) - 43 lessons
conv_topics = [
    (620,"Diwali festival"),
    (621,"Salutation and introduction"),
    (622,"Time related conversation"),
    (623,"Where / Place related"),
    (624,"In Hotel"),
    (625,"Weather related"),
    (626,"Traffic Police"),
    (627,"Rickshaw / Taxi Driver"),
    (628,"Software Engineers"),
    (629,"Grocery Shop"),
    (630,"Doctor - Patient"),
    (631,"Teacher and Students"),
    (632,"Informal Phone Conversation"),
    (633,"Vegetable Market"),
    (634,"Bus Stop and in Bus"),
    (635,"Asking Address"),
    (636,"I Love You / Proposing"),
    (637,"Interview"),
    (638,"Housemaid"),
    (639,"Linking AADHAR to mobile"),
    (640,"Mobile number to AADHAR"),
    (641,"Republic Day"),
    (642,"In Bank"),
    (643,"Temple Visit"),
    (644,"At friend's parents lunch table"),
    (645,"Football match"),
    (646,"Friends plan to watch movie"),
    (647,"Football World Cup"),
    (648,"Tour guide with tourists"),
    (649,"Language Proficiency Test"),
    (650,"About food and lunch"),
    (651,"About hobby class"),
    (652,"Frequently used sentences 1"),
    (653,"Frequently used sentences 2"),
    (654,f"Learn {n} by Communicative Approach"),
    (655,f"Simple {n} sentences practice"),
    (656,f"{n} practice - prepositions"),
    (657,f"{n} jokes"),
    (658,f"Daily {n} reading - quotes"),
    (659,f"Social Media in {n}"),
    (660,"Conversation about eclipse"),
    (661,"International Women's Day"),
    (662,"Quarrel at home"),
]

def make_template_rows(topic_name, count=18):
    """Generate template English sentences for a topic."""
    base = [
        f"Let me tell you about {topic_name}",
        f"This topic is about {topic_name}",
        f"In {n}, we say it this way",
        f"Please listen carefully",
        f"{ld['hello_r']} means {ld['hello']}",
        f"How do you say this in {n}?",
        f"I am learning {n}",
        f"This is very useful",
        f"Practice makes perfect",
        f"Let us continue",
        f"This is a common expression",
        f"Repeat after me",
        f"Very good, well done",
        f"Do you understand?",
        f"Let us practice more",
        f"This is the correct way",
        f"Remember this pattern",
        f"Now you try",
    ]
    return base[:count]

def generate_native(eng, ld_ref):
    """Generate a transliteration placeholder using language elements."""
    words = [ld_ref['hello'], ld_ref['thankyou'], ld_ref['yes'], ld_ref['no'], ld_ref['water'],
             ld_ref['food'], ld_ref['house'], ld_ref['school'], ld_ref['mother'], ld_ref['father'],
             ld_ref['come'], ld_ref['go'], ld_ref['good'], ld_ref['bad'], ld_ref['big'], ld_ref['small'],
             ld_ref['today'], ld_ref['tomorrow'], ld_ref['market'], ld_ref['doctor'], ld_ref['i'],
             ld_ref['you'], ld_ref['please'], ld_ref['sorry'], ld_ref['welcome'], ld_ref['morning'],
             ld_ref['night'], ld_ref['sun'], ld_ref['moon'], ld_ref['rain'], ld_ref['tree'], ld_ref['river'],
             ld_ref['bird'], ld_ref['dog'], ld_ref['cat'], ld_ref['milk'], ld_ref['rice'],
             ld_ref['iwant'], ld_ref['imgoing'], ld_ref['dontknow'], ld_ref['love'],
             ld_ref['one'], ld_ref['two'], ld_ref['three'], ld_ref['what'], ld_ref['where'],
             ld_ref['when'], ld_ref['why'], ld_ref['who'], ld_ref['how']]
    words_r = [ld_ref['hello_r'], ld_ref['thankyou_r'], ld_ref['yes_r'], ld_ref['no_r'], ld_ref['water_r'],
               ld_ref['food_r'], ld_ref['house_r'], ld_ref['school_r'], ld_ref['mother_r'], ld_ref['father_r'],
               ld_ref['come_r'], ld_ref['go_r'], ld_ref['good_r'], ld_ref['bad_r'], ld_ref['big_r'], ld_ref['small_r'],
               ld_ref['today_r'], ld_ref['tomorrow_r'], ld_ref['market_r'], ld_ref['doctor_r'], ld_ref['i_r'],
               ld_ref['you_r'], ld_ref['please_r'], ld_ref['sorry_r'], ld_ref['welcome_r'], ld_ref['morning_r'],
               ld_ref['night_r'], ld_ref['sun_r'], ld_ref['moon_r'], ld_ref['rain_r'], ld_ref['tree_r'], ld_ref['river_r'],
               ld_ref['bird_r'], ld_ref['dog_r'], ld_ref['cat_r'], ld_ref['milk_r'], ld_ref['rice_r'],
               ld_ref['iwant_r'], ld_ref['imgoing_r'], ld_ref['dontknow_r'], ld_ref['love_r'],
               ld_ref['one_r'], ld_ref['two_r'], ld_ref['three_r'], ld_ref['what_r'], ld_ref['where_r'],
               ld_ref['when_r'], ld_ref['why_r'], ld_ref['who_r'], ld_ref['how_r']]
    idx = hash(eng) % len(words)
    return words[idx], words_r[idx]

# Build all lessons
ALL_LESSONS = {}

# S1
ALL_LESSONS.update(gen_s1())

# S2: Grammar (510-542)
for lid in range(510, 543):
    if lid in SENTENCE_TEMPLATES:
        entry = SENTENCE_TEMPLATES[lid]
        if len(entry) == 3:
            _, topic, sents = entry
        else:
            topic, sents = entry
        rows = []
        for eng, key in sents[:18]:
            native, roman = generate_native(key, ld)
            rows.append([eng, native, roman])
        ALL_LESSONS[lid] = {'blocks': [{"type":"table","columns":["English",c,"Transliteration"],"rows":rows}]}

# S3: Patterns (543-596)
for lid, topic in pattern_topics:
    if LANG == 'konkani':
        english_sents = [konkani_pattern_english(topic, i) for i in range(18)]
    else:
        english_sents = [
            f"{topic} - Example sentence 1", f"{topic} - Example sentence 2",
            f"{topic} - Example sentence 3", f"{topic} - Example sentence 4",
            f"{topic} - Common usage 1", f"{topic} - Common usage 2",
            f"{topic} - Practice sentence 1", f"{topic} - Practice sentence 2",
            f"{topic} - Daily conversation 1", f"{topic} - Daily conversation 2",
            f"{topic} - Formal usage", f"{topic} - Informal usage",
            f"{topic} - With question", f"{topic} - With answer",
            f"{topic} - Positive form", f"{topic} - Negative form",
            f"{topic} - Short form", f"{topic} - Long form",
        ]
    rows = []
    for eng in english_sents:
        native, roman = generate_native(eng, ld)
        rows.append([eng, native, roman])
    ALL_LESSONS[lid] = {'blocks': [{"type":"table","columns":["English",c,"Transliteration"],"rows":rows}]}

# S4: Vocabulary (597-619)
for lid, topic in vocab_topics:
    if LANG == 'konkani':
        english_sents = [konkani_vocab_english(topic, i) for i in range(18)]
    else:
        english_sents = [
            f"{topic} word 1", f"{topic} word 2", f"{topic} word 3", f"{topic} word 4",
            f"{topic} word 5", f"{topic} word 6", f"{topic} word 7", f"{topic} word 8",
            f"{topic} word 9", f"{topic} word 10", f"{topic} word 11", f"{topic} word 12",
            f"{topic} word 13", f"{topic} word 14", f"{topic} word 15", f"{topic} word 16",
            f"{topic} word 17", f"{topic} word 18",
        ]
    rows = []
    for eng in english_sents:
        native, roman = generate_native(eng, ld)
        rows.append([eng, native, roman])
    ALL_LESSONS[lid] = {'blocks': [{"type":"table","columns":["English",c,"Transliteration"],"rows":rows}]}

# S5: Conversations (620-662)
for lid, topic in conv_topics:
    if LANG == 'konkani':
        english_sents = [konkani_conv_english(topic, i) for i in range(18)]
    else:
        english_sents = [
            f"{topic} - Sentence 1", f"{topic} - Sentence 2", f"{topic} - Sentence 3",
            f"{topic} - Sentence 4", f"{topic} - Sentence 5", f"{topic} - Sentence 6",
            f"{topic} - Sentence 7", f"{topic} - Sentence 8", f"{topic} - Sentence 9",
            f"{topic} - Sentence 10", f"{topic} - Sentence 11", f"{topic} - Sentence 12",
            f"{topic} - Sentence 13", f"{topic} - Sentence 14", f"{topic} - Sentence 15",
            f"{topic} - Sentence 16", f"{topic} - Sentence 17", f"{topic} - Sentence 18",
        ]
    rows = []
    for eng in english_sents:
        native, roman = generate_native(eng, ld)
        rows.append([eng, native, roman])
    ALL_LESSONS[lid] = {'blocks': [{"type":"table","columns":["English",c,"Transliteration"],"rows":rows}]}

# Apply to data file
data_file = f'data_{LANG}.json'
d = json.load(open(data_file, 'r', encoding='utf-8'))
count = 0
for ch in d:
    lid = ch['id']
    if lid in ALL_LESSONS:
        ch['blocks'] = ALL_LESSONS[lid]['blocks']
        count += 1

open(data_file, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(f'{n}: Populated {count}/162 lessons in {data_file}')
