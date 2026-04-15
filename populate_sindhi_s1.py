import json, sys

TRANSLITERATION = {
    'ا': 'a/aa', 'آ': 'aa', 'ب': 'b', 'ٻ': 'bb', 'ڀ': 'bh',
    'پ': 'p', 'ت': 't', 'ٿ': 'th', 'ٽ': 'tt', 'ٺ': 'tth',
    'ث': 's', 'ج': 'j', 'جهه': 'jh', 'ڄ': 'jj', 'چ': 'ch',
    'ڇ': 'chh', 'ح': 'h', 'خ': 'kh', 'د': 'd', 'ڊ': 'dd',
    'ڌ': 'dh', 'ڍ': 'ddh', 'ذ': 'z', 'ر': 'r', 'ڙ': 'rr',
    'ز': 'z', 'ژ': 'zh', 'س': 's', 'ش': 'sh', 'ص': 's',
    'ض': 'z', 'ط': 't', 'ظ': 'z', 'ع': 'a', 'غ': 'gh',
    'ف': 'f', 'ق': 'q', 'ڪ': 'k', 'ک': 'k', 'گ': 'g',
    'ڳ': 'gg', 'ل': 'l', 'م': 'm', 'ن': 'n', 'ڻ': 'nn',
    'ں': 'n', 'و': 'w/o', 'ه': 'h', 'ھ': 'h', 'ء': "'",
    'ي': 'y/ee', 'ی': 'y', 'ئ': 'y/ai', 'ة': 'ah',
    'َ': 'a', 'ِ': 'i', 'ُ': 'u', 'ّ': '(double)',
}

def transliterate(sindhi_text):
    out = []
    for ch in sindhi_text:
        if ch in TRANSLITERATION:
            out.append(TRANSLITERATION[ch])
        elif ch == ' ':
            out.append(' ')
        elif ch.isascii():
            out.append(ch)
    return ''.join(out)

lessons = {}

# 501 - Sindhi Alphabets - Arabic Script
lessons[501] = {
    "grid": {
        "heading": "Sindhi Alphabet Chart",
        "headers": ["Letter", "Transliteration"],
        "speakCol": 0,
        "rows": [
            ["ا", "alif (a/aa)"], ["آ", "aa"], ["ب", "be (b)"], ["ٻ", "bbe (bb)"],
            ["ڀ", "bhe (bh)"], ["پ", "pe (p)"], ["ت", "te (t)"], ["ٿ", "the (th)"],
            ["ٽ", "tte (tt)"], ["ٺ", "tthe (tth)"], ["ث", "se (s)"], ["ج", "jeem (j)"],
            ["ڄ", "jje (jj)"], ["چ", "che (ch)"], ["ڇ", "chhe (chh)"], ["ح", "he (h)"],
            ["خ", "khe (kh)"], ["د", "daal (d)"], ["ڊ", "ddaal (dd)"], ["ڌ", "dhaal (dh)"],
            ["ڍ", "ddhaal (ddh)"], ["ذ", "zaal (z)"], ["ر", "re (r)"], ["ڙ", "rre (rr)"],
            ["ز", "ze (z)"], ["ژ", "zhe (zh)"], ["س", "seen (s)"], ["ش", "sheen (sh)"],
            ["ص", "swaad (s)"], ["ض", "zwaad (z)"], ["ط", "toe (t)"], ["ظ", "zoe (z)"],
            ["ع", "ain (a)"], ["غ", "ghain (gh)"], ["ف", "fe (f)"], ["ق", "qaaf (q)"],
            ["ڪ", "kaaf (k)"], ["ک", "kaaf (k)"], ["گ", "gaaf (g)"], ["ڳ", "ggaaf (gg)"],
            ["ل", "laam (l)"], ["م", "meem (m)"], ["ن", "noon (n)"], ["ڻ", "nnoon (nn)"],
            ["ں", "noon ghunna (n)"], ["و", "waao (w/o)"], ["ه", "he (h)"],
            ["ھ", "do chashmi he (h)"], ["ء", "hamza (')"], ["ي", "ye (y/ee)"],
            ["ی", "ye (y)"], ["ئ", "hamza ye (y/ai)"]
        ]
    },
    "table": {
        "heading": "Practice words with Sindhi letters",
        "headers": ["English", "Sindhi", "Transliteration"],
        "speakCol": 1,
        "rows": [
            ["Water", "پاڻي", "Paani"], ["Book", "ڪتاب", "Kitaab"],
            ["House", "گهر", "Ghar"], ["Mother", "ماءُ", "Maau"],
            ["Father", "پيءُ", "Piyu"], ["Brother", "ڀاءُ", "Bhaau"],
            ["Sister", "ڀيڻ", "Bhain"], ["Child", "ٻار", "Baar"],
            ["Bread", "ماني", "Maani"], ["Sun", "سج", "Suju"],
            ["Moon", "چنڊ", "Chand"], ["Star", "تارو", "Taaro"],
            ["Tree", "وڻ", "Wann"], ["Flower", "گل", "Gul"],
            ["Earth", "ڌرتي", "Dharti"], ["Sky", "آسمان", "Aasmaan"],
            ["River", "ندي", "Nadi"], ["Fire", "باهه", "Baahh"],
            ["Eye", "اک", "Akh"], ["Hand", "هٿ", "Hath"]
        ]
    }
}

# 502 - Vowels, Consonants and pronunciation
lessons[502] = {
    "grid": {
        "heading": "Sindhi Vowel Sounds",
        "headers": ["Letter/Mark", "Transliteration"],
        "speakCol": 0,
        "rows": [
            ["اَ", "a (short)"], ["آ", "aa (long)"], ["اِ", "i (short)"],
            ["اي", "ee (long)"], ["اُ", "u (short)"], ["او", "oo (long)"],
            ["اي", "ai/e"], ["او", "au/o"],
            ["ا", "alif – carrier"], ["و", "waao – w/o sound"],
            ["ي", "ye – y/ee sound"], ["ی", "ye – y sound"]
        ]
    },
    "table": {
        "heading": "Vowel sounds in Sindhi words",
        "headers": ["English", "Sindhi", "Transliteration"],
        "speakCol": 1,
        "rows": [
            ["Come", "اچو", "Acho"], ["Mango", "انب", "Anab"],
            ["Today", "اڄ", "Aaj"], ["Pomegranate", "انار", "Anaar"],
            ["Eye", "اک", "Akh"], ["This", "هي", "Hee"],
            ["That", "اهو", "Aho"], ["He/She", "هو", "Hoo"],
            ["Camel", "اٺ", "Uth"], ["Milk", "کير", "Kheer"],
            ["Own", "پنهنجو", "Panhinjo"], ["Heart", "دل", "Dil"],
            ["Nose", "نڪ", "Nak"], ["Ear", "ڪن", "Kan"],
            ["Mouth", "وات", "Waat"], ["Teeth", "ڏند", "Ddand"],
            ["Tongue", "زبان", "Zabaan"], ["Face", "منهن", "Munhan"],
            ["Body", "جسم", "Jism"], ["Knee", "ڳوڏو", "Ggodho"]
        ]
    }
}

# 503 - Vowel signs with consonants (Barakhadi equivalent)
lessons[503] = {
    "grid": {
        "heading": "Sindhi Vowel Signs (Diacritics)",
        "headers": ["Letter/Mark", "Transliteration"],
        "speakCol": 0,
        "rows": [
            ["بَ", "ba"], ["بِ", "bi"], ["بُ", "bu"],
            ["پَ", "pa"], ["پِ", "pi"], ["پُ", "pu"],
            ["تَ", "ta"], ["تِ", "ti"], ["تُ", "tu"],
            ["جَ", "ja"], ["جِ", "ji"], ["جُ", "ju"],
            ["دَ", "da"], ["دِ", "di"], ["دُ", "du"],
            ["سَ", "sa"], ["سِ", "si"], ["سُ", "su"],
            ["ڪَ", "ka"], ["ڪِ", "ki"], ["ڪُ", "ku"],
            ["مَ", "ma"], ["مِ", "mi"], ["مُ", "mu"],
            ["نَ", "na"], ["نِ", "ni"], ["نُ", "nu"]
        ]
    },
    "table": {
        "heading": "Words showing vowel sign usage",
        "headers": ["English", "Sindhi", "Transliteration"],
        "speakCol": 1,
        "rows": [
            ["Word", "لفظ", "Lafz"], ["Pen", "قلم", "Qalam"],
            ["Knowledge", "علم", "Ilm"], ["World", "دنيا", "Duniyaa"],
            ["Country", "ملڪ", "Mulk"], ["Language", "ٻولي", "Boli"],
            ["Name", "نالو", "Naalo"], ["Work", "ڪم", "Kamu"],
            ["Door", "دروازو", "Darwaazo"], ["Window", "دري", "Dari"],
            ["Roof", "ڇت", "Chhat"], ["Wall", "ديوار", "Deewaar"],
            ["Floor", "فرش", "Farsh"], ["Path", "رستو", "Rasto"],
            ["Garden", "باغ", "Baagh"], ["Farm", "کيت", "Khet"],
            ["Pond", "ٽوبو", "Ttobo"], ["Well", "ڪُهو", "Kuho"],
            ["Bridge", "پل", "Pul"], ["Mountain", "جبل", "Jabal"]
        ]
    }
}

# 504 - Pronunciation problems (Arabic Script)
lessons[504] = {
    "table": {
        "heading": "Commonly confused Sindhi sounds",
        "headers": ["English", "Sindhi", "Transliteration"],
        "speakCol": 1,
        "rows": [
            ["Knife (with ڪ)", "ڇري", "Chhuri"],
            ["Do (with ڪ)", "ڪريو", "Kariyo"],
            ["Pull (with ک)", "کڻو", "Khino"],
            ["Eat (with ک)", "کائو", "Khaaio"],
            ["Village (with ڳ)", "ڳوٺ", "Ggoth"],
            ["Talk (with ڳ)", "ڳالهايو", "Ggaalhaaio"],
            ["Horse (with گ)", "گهوڙو", "Ghorho"],
            ["Sing (with گ)", "ڳايو", "Ggaaio"],
            ["Big (with ڊ)", "وڏو", "Waddo"],
            ["See (with ڏ)", "ڏسو", "Ddiso"],
            ["Child (with ٻ)", "ٻار", "Baar"],
            ["Tell (with ب)", "ٻڌايو", "Buddhaaio"],
            ["Rain (with ن)", "مينهن", "Meenhan"],
            ["Nose (with ن)", "نڪ", "Nak"],
            ["Neck (with ڻ)", "ڳچي", "Ggachi"],
            ["Tooth (with ڏ)", "ڏند", "Ddand"],
            ["Foot (with پ)", "پير", "Peer"],
            ["River (with ن)", "ندي", "Nadi"],
            ["Stomach (with پ)", "پيٽ", "Pet"],
            ["Head (with م)", "مٿو", "Matho"]
        ]
    }
}

# 505 - Nasalization and Nunation
lessons[505] = {
    "grid": {
        "heading": "Nasalized sounds in Sindhi",
        "headers": ["Letter", "Transliteration"],
        "speakCol": 0,
        "rows": [
            ["ں", "noon ghunna (nasal n)"],
            ["ن", "noon (full n)"],
            ["ڻ", "retroflexed nn"],
            ["نَ", "na"], ["نِ", "ni"], ["نُ", "nu"],
            ["ڻَ", "nna"], ["ڻِ", "nni"], ["ڻُ", "nnu"],
            ["ں (word-end)", "nasal ending"]
        ]
    },
    "table": {
        "heading": "Words with nasalized sounds",
        "headers": ["English", "Sindhi", "Transliteration"],
        "speakCol": 1,
        "rows": [
            ["Rain", "مينهن", "Meenhan"], ["People", "ماڻهو", "Maanho"],
            ["Eye", "اک", "Akh"], ["Nose", "نڪ", "Nak"],
            ["Tooth", "ڏند", "Ddand"], ["Own", "پنهنجو", "Panhinjo"],
            ["Face", "منهن", "Munhan"], ["Ear", "ڪن", "Kan"],
            ["Navel", "ڏنڊ", "Ddandd"], ["Bone", "هڏ", "Hadd"],
            ["Leaf", "پن", "Pan"], ["Day", "ڏينهن", "Dinhan"],
            ["Neck", "ڳچي", "Ggachi"], ["Grain", "ڏاڻو", "Ddaano"],
            ["Arrow", "تير", "Teer"], ["Deep", "اونهو", "Oonho"],
            ["Where", "ڪٿي", "Kithe"], ["When", "ڪڏهن", "Kadhan"],
            ["Someone", "ڪو", "Ko"], ["Everywhere", "هر هنڌ", "Har handh"]
        ]
    }
}

# 506 - Combining consonants in Sindhi
lessons[506] = {
    "table": {
        "heading": "Combined consonant forms in Sindhi",
        "headers": ["English", "Sindhi", "Transliteration"],
        "speakCol": 1,
        "rows": [
            ["Knowledge", "علم", "Ilm"], ["Patience", "صبر", "Sabr"],
            ["Truth", "سچ", "Sach"], ["Thought", "فڪر", "Fikr"],
            ["Prayer", "نماز", "Namaaz"], ["Thanks", "شڪريه", "Shukriya"],
            ["Fast (speed)", "تيز", "Tez"], ["Simple", "سادو", "Saado"],
            ["Smart", "هوشيار", "Hoshiyaar"], ["Tall", "ڊگهو", "Ddagho"],
            ["Short", "ننڍو", "Nandho"], ["Fat", "ٿلهو", "Thulho"],
            ["Thin", "پتلو", "Patlo"], ["Strong", "مضبوط", "Mazboot"],
            ["Weak", "ڪمزور", "Kamzor"], ["Clean", "صاف", "Saaf"],
            ["Dirty", "ميلو", "Melo"], ["Slow", "سُست", "Sust"],
            ["Beautiful", "سهڻو", "Suhno"], ["Ugly", "بدصورت", "Badsoorat"]
        ]
    }
}

# 507 - Combining consonants with ر (r)
lessons[507] = {
    "table": {
        "heading": "Consonant combinations with ر (r)",
        "headers": ["English", "Sindhi", "Transliteration"],
        "speakCol": 1,
        "rows": [
            ["Color", "رنگ", "Rang"], ["Road", "رستو", "Rasto"],
            ["King", "راجا", "Raajaa"], ["Night", "رات", "Raat"],
            ["Stay", "رهڻ", "Rahan"], ["Rope", "رسي", "Rasi"],
            ["Stop", "رُڪو", "Ruko"], ["Cry", "رُئو", "Ruio"],
            ["Custom", "رواج", "Riwaaj"], ["Secret", "راز", "Raaz"],
            ["Friend", "رفيق", "Rafeeq"], ["Permission", "رخصت", "Rukhsat"],
            ["Relationship", "رشتو", "Rishto"], ["Speed", "رفتار", "Raftaar"],
            ["Anger", "ڪاوڙ", "Kawarr"], ["Price", "قيمت", "Qeemat"],
            ["Winter", "سياري", "Siyaari"], ["Summer", "اونهاري", "Oonhaari"],
            ["Morning", "صبح", "Subha"], ["Bright", "روشن", "Roshan"]
        ]
    }
}

# 508 - Combining consonants with ه (h)
lessons[508] = {
    "table": {
        "heading": "Consonant combinations with ه (h)",
        "headers": ["English", "Sindhi", "Transliteration"],
        "speakCol": 1,
        "rows": [
            ["Hand", "هٿ", "Hath"], ["Bone", "هڏ", "Hadd"],
            ["Plow", "هل", "Hal"], ["Diamond", "هيرو", "Heero"],
            ["Air", "هوا", "Hawaa"], ["Every", "هر", "Har"],
            ["Green", "هريالو", "Hariyaalo"], ["Deer", "هرڻ", "Haran"],
            ["Courage", "همت", "Himmat"], ["Here", "هتي", "Hite"],
            ["Necklace", "هار", "Haar"], ["Weapon", "هٿيار", "Hathiyaar"],
            ["Week", "هفتو", "Hafto"], ["Lip", "هوٺ", "Hont"],
            ["Laugh", "هنسو", "Hanso"], ["Thousand", "هزار", "Hazaar"],
            ["Indian", "هندستاني", "Hindustani"], ["Sympathy", "همدردي", "Hamdardi"],
            ["Harmony", "هم آهنگي", "Ham Aahangi"], ["Strike", "هڙتال", "Hartaal"]
        ]
    }
}

# 509 - Special symbols for combined consonants
lessons[509] = {
    "table": {
        "heading": "Special combined consonant forms in Sindhi",
        "headers": ["English", "Sindhi", "Transliteration"],
        "speakCol": 1,
        "rows": [
            ["Blessing", "دعا", "Duaa"], ["Meaning", "معني", "Maani"],
            ["Meeting", "ملاقات", "Mulaaqaat"], ["Respect", "عزت", "Izzat"],
            ["Happiness", "خوشي", "Khushi"], ["Sadness", "اداسي", "Udaasi"],
            ["Dream", "خواب", "Khwaab"], ["Sleep", "ننڊ", "Nind"],
            ["Hunger", "بک", "Bhuk"], ["Thirst", "تمان", "Tamaan"],
            ["Question", "سوال", "Sawaal"], ["Answer", "جواب", "Jawaab"],
            ["Story", "ڪهاڻي", "Kahaani"], ["Song", "گيت", "Geet"],
            ["Dance", "ناچ", "Naach"], ["Music", "موسيقي", "Moseeqi"],
            ["Festival", "ميلو", "Melo"], ["Wedding", "شادي", "Shaadi"],
            ["Invitation", "دعوت", "Dawat"], ["Gift", "تحفو", "Tohfo"]
        ]
    }
}

# Load existing scaffold
data = json.load(open('data_sindhi.json', 'r', encoding='utf-8'))
id_map = {ch['id']: ch for ch in data}

for lid, content in lessons.items():
    ch = id_map[lid]
    ch['blocks'] = []
    if 'grid' in content:
        ch['blocks'].append({
            "type": "table",
            "heading": content['grid']['heading'],
            "headers": content['grid']['headers'],
            "speakCol": content['grid']['speakCol'],
            "rows": content['grid']['rows']
        })
    if 'table' in content:
        ch['blocks'].append({
            "type": "table",
            "heading": content['table']['heading'],
            "headers": content['table']['headers'],
            "speakCol": content['table']['speakCol'],
            "rows": content['table']['rows']
        })

with open('data_sindhi.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Section 1 (501-509) populated with grids and tables.")
for lid in sorted(lessons.keys()):
    ch = id_map[lid]
    nb = len(ch['blocks'])
    nr = sum(len(b['rows']) for b in ch['blocks'])
    print(f"  {lid}: {nb} block(s), {nr} rows total")
