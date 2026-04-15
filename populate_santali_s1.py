import json

d = json.load(open('data_santali.json', 'r', encoding='utf-8'))

LESSONS = {}

# 501 - Ol Chiki Script alphabet and basic letters
LESSONS[501] = {
    "blocks": [
        {
            "type": "grid",
            "columns": ["Ol Chiki Letter", "Name", "Transliteration"],
            "rows": [
                ["ᱚ", "Ol", "o"],
                ["ᱟ", "Ag", "a"],
                ["ᱠ", "Ak", "k"],
                ["ᱡ", "Aj", "j"],
                ["ᱢ", "Am", "m"],
                ["ᱣ", "Aw", "w"],
                ["ᱤ", "Li", "i"],
                ["ᱥ", "Is", "s"],
                ["ᱦ", "Ah", "h"],
                ["ᱧ", "Iny", "ny"],
                ["ᱨ", "Ir", "r"],
                ["ᱩ", "Lu", "u"],
                ["ᱪ", "Uch", "c"],
                ["ᱫ", "Ud", "d"],
                ["ᱬ", "Unn", "nn"],
                ["ᱭ", "Uy", "y"],
                ["ᱮ", "Le", "e"],
                ["ᱯ", "Ep", "p"],
                ["ᱰ", "Udd", "dd"],
                ["ᱱ", "En", "n"],
                ["ᱲ", "Err", "rr"],
                ["ᱳ", "Oh", "oh"],
                ["ᱴ", "At", "t (retroflex)"],
                ["ᱵ", "Agg", "b"],
                ["ᱶ", "Phaarkaa", "(visarga)"],
                ["ᱷ", "Ahad", "(aspiration mark)"],
                ["ᱸ", "Mu Tudag", "(nasalization)"],
                ["ᱹ", "Gaahlaa Tudag", "(length mark)"],
                ["ᱺ", "Mu-Gaahlaa Tudag", "(nasal + length)"],
                ["ᱻ", "Relaa", "(separator)"]
            ]
        }
    ]
}

# 502 - Independent vowels, consonants and pronunciation
LESSONS[502] = {
    "blocks": [
        {
            "type": "grid",
            "columns": ["Vowel", "Name", "Pronunciation"],
            "rows": [
                ["ᱚ", "Ol", "o as in 'hot'"],
                ["ᱟ", "Ag", "a as in 'father'"],
                ["ᱤ", "Li", "i as in 'bit'"],
                ["ᱩ", "Lu", "u as in 'put'"],
                ["ᱮ", "Le", "e as in 'bed'"],
                ["ᱳ", "Oh", "o as in 'go'"]
            ]
        },
        {
            "type": "grid",
            "columns": ["Consonant", "Name", "Pronunciation"],
            "rows": [
                ["ᱠ", "Ak", "k as in 'kite'"],
                ["ᱡ", "Aj", "j as in 'jam'"],
                ["ᱢ", "Am", "m as in 'man'"],
                ["ᱣ", "Aw", "w as in 'water'"],
                ["ᱥ", "Is", "s as in 'sun'"],
                ["ᱦ", "Ah", "h as in 'hat'"],
                ["ᱧ", "Iny", "ny as in 'canyon'"],
                ["ᱨ", "Ir", "r as in 'run'"],
                ["ᱪ", "Uch", "ch as in 'chair'"],
                ["ᱫ", "Ud", "d as in 'dog'"],
                ["ᱬ", "Unn", "retroflex nn"],
                ["ᱭ", "Uy", "y as in 'yes'"],
                ["ᱯ", "Ep", "p as in 'pot'"],
                ["ᱰ", "Udd", "retroflex dd"],
                ["ᱱ", "En", "n as in 'no'"],
                ["ᱲ", "Err", "retroflex rr"],
                ["ᱴ", "At", "retroflex t"],
                ["ᱵ", "Agg", "b as in 'boy'"]
            ]
        }
    ]
}

# 503 - Vowel signs with consonants
LESSONS[503] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Santali (Ol Chiki)", "Transliteration"],
            "rows": [
                ["ᱠ + ᱚ = ᱠᱚ", "ᱠᱚ (ko)", "ko"],
                ["ᱠ + ᱟ = ᱠᱟ", "ᱠᱟ (ka)", "ka"],
                ["ᱠ + ᱤ = ᱠᱤ", "ᱠᱤ (ki)", "ki"],
                ["ᱠ + ᱩ = ᱠᱩ", "ᱠᱩ (ku)", "ku"],
                ["ᱠ + ᱮ = ᱠᱮ", "ᱠᱮ (ke)", "ke"],
                ["ᱡ + ᱚ = ᱡᱚ", "ᱡᱚ (jo)", "jo"],
                ["ᱡ + ᱟ = ᱡᱟ", "ᱡᱟ (ja)", "ja"],
                ["ᱡ + ᱤ = ᱡᱤ", "ᱡᱤ (ji)", "ji"],
                ["ᱡ + ᱩ = ᱡᱩ", "ᱡᱩ (ju)", "ju"],
                ["ᱡ + ᱮ = ᱡᱮ", "ᱡᱮ (je)", "je"],
                ["ᱢ + ᱚ = ᱢᱚ", "ᱢᱚ (mo)", "mo"],
                ["ᱢ + ᱟ = ᱢᱟ", "ᱢᱟ (ma)", "ma"],
                ["ᱢ + ᱤ = ᱢᱤ", "ᱢᱤ (mi)", "mi"],
                ["ᱥ + ᱚ = ᱥᱚ", "ᱥᱚ (so)", "so"],
                ["ᱥ + ᱟ = ᱥᱟ", "ᱥᱟ (sa)", "sa"],
                ["ᱦ + ᱚ = ᱦᱚ", "ᱦᱚ (ho)", "ho"],
                ["ᱦ + ᱟ = ᱦᱟ", "ᱦᱟ (ha)", "ha"],
                ["ᱫ + ᱚ = ᱫᱚ", "ᱫᱚ (do)", "do"],
                ["ᱫ + ᱟ = ᱫᱟ", "ᱫᱟ (da)", "da"]
            ]
        }
    ]
}

# 504 - Common pronunciation issues
LESSONS[504] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Santali (Ol Chiki)", "Transliteration"],
            "rows": [
                ["Aspirated 'k' sound", "ᱠᱷ (kh)", "kh"],
                ["Aspirated 'g' sound", "ᱜᱷ (gh)", "gh"],
                ["Aspirated 'ch' sound", "ᱪᱷ (chh)", "chh"],
                ["Aspirated 'j' sound", "ᱡᱷ (jh)", "jh"],
                ["Aspirated 't' sound", "ᱛᱷ (th)", "th"],
                ["Aspirated 'd' sound", "ᱫᱷ (dh)", "dh"],
                ["Aspirated 'p' sound", "ᱯᱷ (ph)", "ph"],
                ["Aspirated 'b' sound", "ᱵᱷ (bh)", "bh"],
                ["Glottal stop (checked consonant)", "ᱠᱽ (k')", "k'"],
                ["Nasal 'n' before 'g'", "ᱸᱜ (ng)", "ng"],
                ["Water (short 'a')", "ᱫᱟᱜ (dag)", "dag"],
                ["Rice / food", "ᱫᱟᱹᱠ (dak)", "dak"],
                ["Forest", "ᱵᱤᱨ (bir)", "bir"],
                ["Hill / mountain", "ᱵᱩᱨᱩ (buru)", "buru"],
                ["House", "ᱚᱲᱟᱜ (orag)", "orag"],
                ["Village", "ᱟᱹᱛᱩ (atu)", "atu"],
                ["Person", "ᱦᱚᱲ (hor)", "hor"],
                ["Language", "ᱯᱟᱹᱨᱥᱤ (parsi)", "parsi"]
            ]
        }
    ]
}

# 505 - Final consonants, lonsum forms and nasalization
LESSONS[505] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Santali (Ol Chiki)", "Transliteration"],
            "rows": [
                ["Nasal mark (Mu Tudag)", "ᱸ added to vowel", "nasalization marker"],
                ["Length mark (Gaahlaa Tudag)", "ᱹ added after consonant", "lengthens preceding vowel"],
                ["Checked final -k", "ᱫᱟᱹᱠ (rice)", "dak"],
                ["Checked final -g", "ᱫᱟᱜ (water)", "dag"],
                ["Checked final -t", "ᱦᱟᱴ (market)", "hat"],
                ["Checked final -d", "ᱢᱟᱫ (alcohol)", "mad"],
                ["Checked final -p", "ᱟᱹᱯ (mango)", "ap"],
                ["Checked final -b", "ᱫᱩᱵ (grass)", "dub"],
                ["Nasal final -n", "ᱢᱟᱱ (respect)", "man"],
                ["Nasal final -m", "ᱱᱟᱢ (name)", "nam"],
                ["Nasal final -ng", "ᱫᱟᱸᱜ (big drum)", "dang"],
                ["Sun", "ᱥᱤᱧ (sing)", "sing"],
                ["Moon", "ᱪᱟᱸᱫᱚ (chando)", "chando"],
                ["Star", "ᱤᱯᱤᱞ (ipil)", "ipil"],
                ["Flower", "ᱵᱟᱦᱟ (baha)", "baha"],
                ["Tree", "ᱫᱟᱨᱮ (dare)", "dare"],
                ["Fish", "ᱢᱟᱹᱪᱷᱟ (machha)", "machha"],
                ["Land / country", "ᱫᱤᱥᱚᱢ (disom)", "disom"]
            ]
        }
    ]
}

# 506 - Combining signs and syllable formation
LESSONS[506] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Santali (Ol Chiki)", "Transliteration"],
            "rows": [
                ["Two-syllable: house", "ᱚᱲᱟᱜ (o-rag)", "orag"],
                ["Two-syllable: village", "ᱟᱹᱛᱩ (a-tu)", "atu"],
                ["Two-syllable: water", "ᱫᱟᱜ (dag)", "dag"],
                ["Three-syllable: country", "ᱫᱤᱥᱚᱢ (di-som)", "disom"],
                ["Three-syllable: person", "ᱢᱟᱹᱱᱢᱤ (man-mi)", "manmi"],
                ["Three-syllable: language", "ᱯᱟᱹᱨᱥᱤ (par-si)", "parsi"],
                ["Compound: festival", "ᱵᱟᱦᱟ ᱯᱚᱨᱚᱵ (baha porob)", "baha porob"],
                ["Compound: school", "ᱚᱞ ᱚᱲᱟᱜ (ol orag)", "ol orag"],
                ["Compound: teacher", "ᱯᱟᱲᱦᱟᱣᱮᱫ (parhawed)", "parhawed"],
                ["Three-syllable: morning", "ᱥᱮᱛᱟᱜ (se-tag)", "setag"],
                ["Syllable: forest", "ᱵᱤᱨ (bir)", "bir"],
                ["Syllable: mountain", "ᱵᱩᱨᱩ (bu-ru)", "buru"],
                ["Compound: market day", "ᱦᱟᱹᱴᱤᱧ ᱢᱟᱦᱟᱸ (hating mahang)", "hating mahang"],
                ["Compound: headman", "ᱢᱟᱹᱧᱡᱷᱤ (manjhi)", "manjhi"],
                ["Three-syllable: evening", "ᱧᱤᱸᱫᱟ (nyin-da)", "nyinda"],
                ["Two-syllable: child", "ᱜᱤᱫᱽᱨᱟᱹ (gid-ra)", "gidra"],
                ["Two-syllable: song", "ᱥᱮᱨᱮᱧ (se-reny)", "sereny"],
                ["Three-syllable: beautiful", "ᱥᱚᱢᱵᱷᱟᱨ (sombhar)", "sombhar"]
            ]
        }
    ]
}

# 507 - Word-final forms and checked sounds
LESSONS[507] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Santali (Ol Chiki)", "Transliteration"],
            "rows": [
                ["See / look (open final)", "ᱧᱮᱞ (nyel)", "nyel"],
                ["Eat (open final)", "ᱡᱚᱢ (jom)", "jom"],
                ["Drink (nasal final)", "ᱧᱩ (nyu)", "nyu"],
                ["Go (open final)", "ᱥᱮᱱ (sen)", "sen"],
                ["Come (checked final)", "ᱦᱤᱡᱩᱜ (hijug)", "hijug"],
                ["Write (open final)", "ᱚᱞ (ol)", "ol"],
                ["Read / study", "ᱯᱟᱲᱦᱟᱣ (parhaw)", "parhaw"],
                ["Run (checked final)", "ᱫᱟᱹᱲ (dar)", "dar"],
                ["Give", "ᱮᱢ (em)", "em"],
                ["Buy (checked final)", "ᱠᱤᱱ (kin)", "kin"],
                ["Call", "ᱠᱩᱞ (kul)", "kul"],
                ["Sleep", "ᱧᱤᱫ (nyid)", "nyid"],
                ["Speak / say", "ᱨᱚᱲ (ror)", "ror"],
                ["Listen / hear", "ᱟᱹᱭᱠᱟᱹᱣ (aykaw)", "aykaw"],
                ["Sit", "ᱫᱩᱲᱩᱵ (durub)", "durub"],
                ["Stand", "ᱛᱤᱧᱜᱩ (tingu)", "tingu"],
                ["Do / make (work)", "ᱠᱟᱹᱢᱤ (kami)", "kami"],
                ["Bring", "ᱟᱹᱜᱩ (agu)", "agu"]
            ]
        }
    ]
}

# 508 - Loan sounds and extended letters
LESSONS[508] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Santali (Ol Chiki)", "Transliteration"],
            "rows": [
                ["Borrowed 'g' sound", "ᱜ (ga) – from Hindi/Bengali", "ga"],
                ["Borrowed 'f' sound", "ᱯᱷ (pha/fa) – English loans", "fa"],
                ["Borrowed 'z' sound", "ᱡᱽ (za) – English/Urdu loans", "za"],
                ["Borrowed 'th' sound", "ᱛᱷ (tha) – Hindi loans", "tha"],
                ["School (English loan)", "ᱥᱠᱩᱞ (skul)", "skul"],
                ["Bus (English loan)", "ᱵᱟᱥ (bas)", "bas"],
                ["Train (English loan)", "ᱨᱮᱞ (rel)", "rel"],
                ["Doctor (English loan)", "ᱰᱚᱠᱴᱚᱨ (doktor)", "doktor"],
                ["Police (English loan)", "ᱯᱩᱞᱤᱥ (pulis)", "pulis"],
                ["Phone (English loan)", "ᱯᱷᱚᱱ (phon)", "phon"],
                ["Television", "ᱴᱤᱵᱷᱤ (tibhi)", "tibhi"],
                ["Computer", "ᱠᱚᱢᱯᱩᱴᱟᱨ (kompuṭar)", "komputar"],
                ["Government (Hindi loan)", "ᱥᱚᱨᱠᱟᱨ (sorkar)", "sorkar"],
                ["Holiday (Hindi loan)", "ᱪᱷᱩᱴᱴᱤ (chhutti)", "chhutti"],
                ["Hospital", "ᱦᱟᱥᱯᱟᱛᱟᱞ (haspatal)", "haspatal"],
                ["Market", "ᱵᱟᱡᱟᱨ (bajar)", "bajar"],
                ["Paper", "ᱠᱟᱜᱚᱡ (kagoj)", "kagoj"],
                ["Book", "ᱯᱩᱛᱷᱤ (puthi)", "puthi"]
            ]
        }
    ]
}

# 509 - Reading practice in Ol Chiki Script
LESSONS[509] = {
    "blocks": [
        {
            "type": "table",
            "columns": ["English", "Santali (Ol Chiki)", "Transliteration"],
            "rows": [
                ["Hello / Greetings", "ᱡᱚᱦᱟᱨ", "johar"],
                ["How are you?", "ᱟᱢ ᱚᱠᱟ ᱠᱟᱱᱟ?", "am oka kana?"],
                ["I am fine", "ᱤᱧ ᱵᱟᱝ ᱢᱮᱱᱟᱜ ᱟ", "inj bang menag a"],
                ["What is your name?", "ᱟᱢᱟᱜ ᱧᱩᱛᱩᱢ ᱪᱮᱫ?", "amag nyutum ced?"],
                ["My name is Soren", "ᱤᱧᱟᱜ ᱧᱩᱛᱩᱢ ᱥᱚᱨᱮᱱ", "injag nyutum Soren"],
                ["I go to school", "ᱤᱧ ᱥᱠᱩᱞ ᱥᱮᱱ ᱟᱭᱟ", "inj skul sen aya"],
                ["I eat rice", "ᱤᱧ ᱫᱟᱹᱠ ᱡᱚᱢ ᱟᱭᱟ", "inj dak jom aya"],
                ["Give me water", "ᱫᱟᱜ ᱮᱢ ᱢᱮ", "dag em me"],
                ["The sun is bright", "ᱥᱤᱧ ᱡᱟᱞᱟᱜ ᱢᱮᱱᱟᱜ ᱟ", "sing jalag menag a"],
                ["The moon is beautiful", "ᱪᱟᱸᱫᱚ ᱥᱚᱢᱵᱷᱟᱨ ᱢᱮᱱᱟᱜ ᱟ", "chando sombhar menag a"],
                ["I love my country", "ᱤᱧ ᱤᱧᱟᱜ ᱫᱤᱥᱚᱢ ᱫᱩᱞᱟᱹᱲ ᱟᱭᱟ", "inj injag disom dular aya"],
                ["Thank you very much", "ᱥᱮᱨᱢᱟ ᱫᱟᱲᱮᱭᱟᱜ ᱢᱟ", "serma dareyag ma"],
                ["Where are you going?", "ᱟᱢ ᱚᱠᱟ ᱥᱮᱱ ᱟᱢ?", "am oka sen am?"],
                ["I am going home", "ᱤᱧ ᱚᱲᱟᱜ ᱥᱮᱱ ᱟᱭᱟ", "inj orag sen aya"],
                ["Goodbye", "ᱡᱚᱦᱟᱨ, ᱥᱮᱱ ᱢᱮ", "johar, sen me"],
                ["The forest is green", "ᱵᱤᱨ ᱥᱟᱥᱟᱝ ᱢᱮᱱᱟᱜ ᱟ", "bir sasang menag a"],
                ["Children are playing", "ᱜᱤᱫᱽᱨᱟᱹ ᱠᱚ ᱮᱱᱮᱡ ᱟᱠᱟᱫᱟ", "gidra ko enej akada"],
                ["I read a book", "ᱤᱧ ᱯᱩᱛᱷᱤ ᱯᱟᱲᱦᱟᱣ ᱟᱭᱟ", "inj puthi parhaw aya"]
            ]
        }
    ]
}

for ch in d:
    if ch['id'] in LESSONS:
        ch['blocks'] = LESSONS[ch['id']]['blocks']

open('data_santali.json', 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('Section 1 (501-509) populated')
