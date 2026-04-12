# -*- coding: utf-8 -*-
"""Build data_malayalam.json — mirrors lessons_structure_malayalam.json (501–662)."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent


def load_titles():
    with open(BASE / "lessons_structure_malayalam.json", encoding="utf-8") as f:
        d = json.load(f)
    titles = {}
    for m in d["majorLessons"]:
        for s in m["sublessons"]:
            titles[s["chapterId"]] = s["title"]
    return titles


def block_table(heading, rows, headers=None):
    h = headers or ["English", "Malayalam", "Transliteration"]
    return {
        "type": "table",
        "heading": heading,
        "headers": h,
        "speakCol": 1,
        "rows": rows,
    }


def chapter(cid, title, content, intro, blocks, tables=None):
    o = {
        "id": cid,
        "title": title,
        "url": "#",
        "content": content,
        "intro": intro,
    }
    if tables is not None:
        o["tables"] = tables
    if blocks is not None:
        o["blocks"] = blocks
    return o


def R(e, m, r):
    return [e, m, r]


# --- 501–509: script (Malayalam Lipi) ---
def ch501():
    return chapter(
        501,
        "Malayalam Alphabets – Malayalam Lipi",
        "Malayalam has 13 vowel letters and about 36 consonants; each consonant carries inherent /a/ unless a vowel sign (കുറി) is added.",
        "Read the vowels first, then sample words. Long vowels (ആ, ഈ, …) contrast with short ones and change meaning.",
        None,
        tables=[
            {
                "heading": "Vowels in Malayalam (സ്വരങ്ങൾ)",
                "headers": ["Letter", "Transliteration"],
                "speakCol": 1,
                "rows": [
                    ["അ", "a"],
                    ["ആ", "ā"],
                    ["ഇ", "i"],
                    ["ഈ", "ī"],
                    ["ഉ", "u"],
                    ["ഊ", "ū"],
                    ["ഋ", "ṛ"],
                    ["എ", "e"],
                    ["ഏ", "ē"],
                    ["ഐ", "ai"],
                    ["ഒ", "o"],
                    ["ഓ", "ō"],
                    ["ഔ", "au"],
                ],
            },
            {
                "heading": "Sample words",
                "headers": ["English", "Malayalam", "Transliteration"],
                "speakCol": 1,
                "rows": [
                    R("water", "വെള്ളം", "veḷḷaṁ"),
                    R("mother", "അമ്മ", "amma"),
                    R("father", "അച്ഛൻ", "acchan"),
                    R("house", "വീട്", "vīṭ"),
                    R("tree", "മരം", "maraṁ"),
                    R("book", "പുസ്തകം", "pustakaṁ"),
                    R("today", "ഇന്ന്", "inn"),
                    R("tomorrow", "നാളെ", "nāḷe"),
                    R("I", "ഞാൻ", "njān"),
                    R("you (sg.)", "നീ", "nī"),
                    R("he", "അവൻ", "avan"),
                    R("she", "അവൾ", "avaḷ"),
                    R("we", "ഞങ്ങൾ", "ñaṅṅaḷ"),
                    R("they", "അവർ", "avar"),
                    R("good", "നല്ല", "nalla"),
                    R("many", "ധാരാളം", "dhārāḷaṁ"),
                    R("one", "ഒന്ന്", "onn"),
                    R("two", "രണ്ട്", "raṇṭ"),
                ],
            },
        ],
    )


def ch502():
    rows = [
        R("The letter ക is pronounced like /ka/ with inherent /a/.", "ക കഥയിൽ ആദ്യത്തെ അക്ഷരമാണ്.", "ka kathayil ādyatte akṣaramāṇ."),
        R("Ta series: ട is alveolar /ṭa/; ത is dental /ta/.", "ടയും തയും ഉച്ചാരണത്തിൽ വ്യത്യാസമുണ്ട്.", "ṭayuṁ tayuṁ uccāraṇattil vyatyāsamuṇṭ."),
        R("Retroflex ണ contrasts with dental ന.", "ണ ന എന്നിവ വേറെ വേറെ ശബ്ദങ്ങളാണ്.", "ṇa na ennive veṛe veṛe śabdagaḷāṇ."),
        R("The letter റ is tapped or trilled /r/ in many dialects.", "റ അക്ഷരം പല പ്രദേശങ്ങളിലും വ്യത്യസ്തമായി ഉച്ചരിക്കപ്പെടുന്നു.", "ṟa akṣaraṁ pala pradēśaṅṅaḷiluṁ vyatystamāyi uccarikkappeṭunnu."),
        R("ങ and ഞ are nasals linked to velar and palatal classes.", "ങ ഞ എന്നിവ സംവൃത സ്വരങ്ങളുമായി ബന്ധപ്പെട്ട നാസിക്യങ്ങളാണ്.", "ṅa ña ennive saṁvr̥ta svaramaḷumāyi bandhappeṭṭa nāsikyaḷāṇ."),
        R("Doubling consonants (ക്‌ക) doubles the consonant sound.", "ഇരട്ടയക്ഷരങ്ങൾ വാക്കിന്റെ അർത്ഥം മാറ്റാം.", "iraṭṭayakṣaraṅṅaḷ vākkinṟe artthaṁ māṭṭāṁ."),
        R("Short /i/ vs long /ī/ appears in minimal pairs.", "കിടക്കുകയും കീടക്കുകയും വ്യത്യസ്ത അർത്ഥങ്ങളാണ്.", "kiṭakkukayuṁ kīṭakkukayuṁ vyatysta artthaṅṅaḷāṇ."),
        R("The vowel sign ി pulls left across some consonants.", "കി ഖി ഗി എന്നിവയിൽ വലത്തേക്ക് വളയുന്ന രൂപം ശ്രദ്ധിക്കുക.", "ki khi gi enniveyil valattēkku vaḷayunna rūpaṁ śraddhikkuka."),
        R("ഔ at word start is rare; learn common words like ഔഷധം.", "ഔഷധം പോലുള്ള പദങ്ങൾ പഠിക്കുക.", "auṣadhaṁ pōluḷḷa padaṅṅaḷ paṭhikkuka."),
        R("Schwa deletion: spoken Malayalam often drops final short vowels.", "സംസാരത്തിൽ അവസാന സ്വരങ്ങൾ വിട്ടുപോകുന്നത് സാധാരണമാണ്.", "saṁsāraṭṭil avasāna svaraṅṅaḷ viṭṭupōkunnat sādhāraṇamāṇ."),
        R("Loanwords keep Sanskrit clusters with conjunct letters.", "സംസ്കൃത പദങ്ങളിൽ കൂട്ടക്ഷരങ്ങൾ കാണാം.", "saṁskr̥ta padaṅṅaḷil kūṭṭakṣaraṅṅaḷ kāṇāṁ."),
        R("English loans adapt to Malayalam script phonologically.", "ബസ്, ടിക്കറ്റ് പോലുള്ള വാക്കുകൾ ലിപിയിൽ എഴുതാം.", "bas, ṭikkaṭṭ pōluḷḷa vākkukaḷ lipiyil eḻutāṁ."),
        R("Stress is not phonemic; rhythm follows syllable weight.", "ഉച്ചാരണത്തിൽ പ്രാധാന്യം അക്ഷരങ്ങളുടെ നീളത്തിനാണ്.", "uccāraṇattil prādhānyaṁ akṣaraṅṅaḷuṭe nīḷattināṇ."),
        R("The letter ഴ is a retroflex lateral not found in Hindi.", "ഴ മലയാളത്തിന്റെ പ്രത്യേകതയുള്ള ഒരു ക്ഷരമാണ്.", "ḻa malayāḷattinṟe pratyēkatayuḷḷa oru kṣaramāṇ."),
        R("Practice reading aloud to master aspiration and voicing.", "ഉച്ചരിച്ച് വായിക്കുന്നത് ഉച്ചാരണം മെച്ചപ്പെടുത്തും.", "uccaricc vāyikkunnat uccāraṇaṁ meccappeṭuttuṁ."),
        R("Children learn the അ അമ്മ sequence in school.", "അ അമ്മ എന്ന അക്ഷരമാല സ്കൂളിൽ പഠിക്കുന്നു.", "a amma enna akṣaramāla skūlil paṭhikkunnu."),
        R("Write each letter on paper several times.", "ഓരോ അക്ഷരവും കടലാസിൽ പല പ്രാവശ്യം എഴുതുക.", "ōrō akṣaravuṁ kaṭalāsil pala prāvaśyaṁ eḻutuka."),
        R("Listen to news bulletins for clear formal pronunciation.", "വാർത്താ വായന ഔപചാരിക ഉച്ചാരണം പഠിക്കാൻ സഹായിക്കും.", "vārtthā vāyana aupacārika uccāraṇaṁ paṭhikkān sahāyikkuṁ."),
    ]
    return chapter(
        502,
        "Vowels, Consonants in Malayalam and their pronunciation",
        "Consonants group into velars, palatals, retroflexes, dentals, and labials; Malayalam also has extra letters like റ, ഴ, ള.",
        "These example sentences mention pronunciation ideas you should practise with a teacher or audio.",
        [block_table("Pronunciation notes (full sentences)", rows)],
    )


def ch503():
    rows = [
        R("ka + ാ gives കാ as in കാല് (foot/leg).", "കാൽ എന്ന വാക്കിൽ ക + ാ കാണാം.", "kāl enna vākkil ka + ā kāṇāṁ."),
        R("ki is written കി (k + short i sign).", "കിളി പക്ഷി ഗ്രാമത്തിൽ കാണാം.", "kiḷi pakṣi grāmattil kāṇāṁ."),
        R("kī is കീ as in കീറ് (tear/slit).", "കീറ് മുറിച്ച് കളയണം.", "kīṟ muṟicc kaḷayaṇaṁ."),
        R("ku, kū: കുഞ്ഞ്, കൂട്.", "കുഞ്ഞിന് പാല് കൊടുക്കണം.", "kuññin pāl koṭukkaṇaṁ."),
        R("ke, kai: കേരളം, കൈ.", "കൈ കഴുകി ഭക്ഷണം കഴിക്കുക.", "kai kaḻuki bhakṣaṇaṁ kaḻikkuka."),
        R("ko, kau: കൊച്ച്, കൗമുദി.", "കൊച്ചുകുട്ടികൾ പാട്ട് പാടുന്നു.", "koccukuṭṭikaḷ pāṭṭ pāṭunnu."),
        R("Consonant + u: കു is below the line for ക.", "കുതിര വേഗത്തിൽ ഓടുന്നു.", "kutira vēgattil ōṭunnu."),
        R("Consonant + ū: കൂ — കൂടെ നടക്കാം.", "നമുക്ക് കൂടെ പോകാം.", "namukku kūṭe pōkāṁ."),
        R("rakar: ർ‍ക്ക gives rk cluster in സർക്കാർ.", "സർക്കാർ നിയമങ്ങൾ പാലിക്കണം.", "sarkkār niyamaṅṅaḷ pālikkaṇaṁ."),
        R("Half-u before യ: ക്യാമ്പസ്.", "ക്യാമ്പസിൽ പഠനം തുടരുന്നു.", "kyāmpasil paṭhanaṁ tuṭarunnu."),
        R("Practice: പ + ി = പി (day/time sense in പിറന്നാൾ).", "പിറന്നാൾ ആശംസകൾ നേരുന്നു.", "piṟannāḷ āśaṁsakaḷ nērunnu."),
        R("മ + എ = മെ as in മെതിയട.", "മെതിയട ഉപയോഗിച്ച് കളിക്കുന്നു.", "meyiyaṭ upayōgicc kaḷikkunnu."),
        R("വ + ഔ = വൗ in some loan styles.", "വൗച്ചർ ഉപയോഗിച്ച് വാങ്ങാം.", "vaucər upayōgicc vāṅṅāṁ."),
        R("Combine ച + ഈ: ചീഞ്ഞില്ലെങ്കിൽ നന്നായിരിക്കും.", "പഴം ചീഞ്ഞില്ലെങ്കിൽ കഴിക്കാം.", "paḻaṁ cīññillenkiḷ kaḻikkāṁ."),
        R("ട + ഊ: ടൂത്ത് പേസ്റ്റ് വാങ്ങി.", "ടൂത്ത് ബ്രഷ് വൃത്തിയാക്കുക.", "ṭūtt braṣ vr̥ttiyākkuka."),
        R("Barakhadi drills help fluent reading.", "ദിനവും അക്ഷരങ്ങൾ എഴുതി വായിക്കുക.", "dinavuṁ akṣaraṅṅaḷ eḻuti vāyikkuka."),
        R("Write നമസ്കാരം and split into syllables.", "നമസ്കാരം പറഞ്ഞ് ആരംഭിക്കാം.", "namaskāraṁ paṟaññu ārambhikkāṁ."),
        R("Trace conjuncts in നന്ദി and ധന്യവാദം.", "ധന്യവാദം പറയുന്നത് സൗഹൃദം കാണിക്കും.", "dhanyavādaṁ paṛayunnat sauhr̥daṁ kāṇikkuṁ."),
    ]
    return chapter(
        503,
        "Malayalam Barakhadi: Symbols for vowels with consonants",
        "Vowel signs (കുറി) attach to consonants: ക, കാ, കി, കീ, കു, കൂ, കെ, കേ, കൈ, കൊ, കോ, കൗ.",
        "Each row links a spelling pattern to a full Malayalam sentence using that pattern.",
        [block_table("Barakhadi-style examples", rows)],
    )


def ch504():
    rows = [
        R("Many learners confuse റ (r) and ഴ (ḻ).", "പഴം വാങ്ങുമ്പോൾ വാക്ക് വ്യക്തമായി പറയുക.", "paḻaṁ vāṅṅumbōḷ vākku vyaktamāyi paṛayuka."),
        R("Ta ട vs ഠ: minimal pairs need careful listening.", "കട്ടിൽ കട്ടിയിൽ നിന്ന് വ്യത്യാസമുണ്ട്.", "kaṭṭil kaṭṭiyil ninn vyatyāsamuṇṭ."),
        R("Dental ത vs retroflex ട in 'path' contexts.", "പാത തുറന്നു; വഴി സുരക്ഷിതമാണ്.", "pāta tuṟannu; vazhi surakṣitamāṇ."),
        R("Nasal ം before stops can sound like vowel nasalisation.", "ഗംഗയിലെ ജലം ശുദ്ധമാണ്.", "gaṁgayile jalaṁ śuddhamāṇ."),
        R("Double ന്ന is common in speech: ഇന്ന്, അന്ന്.", "ഇന്ന് കാലാവസ്ഥ നന്നായിരിക്കുന്നു.", "inn kālāvastha nannāyirikkunnu."),
        R("ങ్ఙ occurs in words like മാങ്ങ (mango).", "മാങ്ങ പഴുത്തതാണ്.", "māṅṅa paḻuttatāṇ."),
        R("Schwa with സ: സന്തോഷം ends clearly in -അം.", "സന്തോഷം പങ്കുവെക്കുന്നത് നല്ലതാണ്.", "saṁtōṣaṁ paṅṅkuvekkunnat nallatāṇ."),
        R("എ at word end in colloquial: പോകെ?", "ഇപ്പോൾ പോകെ, നാളെ വരാം.", "ippōḷ pōke, nāḷe varāṁ."),
        R("Glide യ് after vowels in ഐശ്വര്യം.", "ഐശ്വര്യം മനസ്സമാധാനം നൽകുന്നു.", "aiśvaryaṁ manassamādhānaṁ nalkunnu."),
        R("Retroflex ള in കള്ളം vs കല.", "കള്ളം പറയരുത്; സത്യം പറയുക.", "kaḷḷaṁ paṛayarut; satyaṁ paṛayuka."),
        R("Contrast ഈറ് (saw) and ഇറ് (descent).", "മരം മുറിക്കാൻ ഈറ് വേണം.", "maraṁ muṟikkān īṟ vēṇaṁ."),
        R("Practice minimal pairs: കരി, കാരി.", "കറി വേറെ, കാരി വേറെ അർത്ഥമാണ്.", "kaṛi veṛe, kāri veṛe artthamāṇ."),
        R("Listen for ന്റ cluster in വണ്ടി.", "വണ്ടി നിർത്തി ഇറങ്ങുക.", "vaṇṭi nirtthi iṟaṅṅuka."),
        R("ശ vs ഷ vs സ: ശരീരം, ഷട്, സമയം.", "ശരീരം സുഖമാണോ എന്ന് ചോദിക്കുക.", "śarīraṁ sukhamāṇō ennu cōdikkuka."),
        R("ഋ in Sanskrit loans: ഋഷി.", "ഋഷിമാർ മന്ത്രങ്ങൾ ചൊല്ലിയിരുന്നു.", "ṛṣimār mantraṅṅaḷ colliyirunnu."),
        R("Do not confuse ഔ (vowel) with conjunct ക്ഷ.", "ക്ഷമ നേടുന്നത് വലിയ ഗുണമാണ്.", "kṣama nēṭunnat valiya guṇamāṇ."),
        R("Record yourself and compare with radio Malayalam.", "ആകാശവാണിയിലെ വാർത്ത കേൾക്കുക.", "ākāśavāṇiyile vārttha kēḷkkuka."),
        R("Slow repetition fixes most pronunciation errors.", "മെല്ലെ വായിച്ചാൽ പിശകുകൾ കുറയും.", "melle vāyiccāl piśakukaḷ kuṛayuṁ."),
    ]
    return chapter(
        504,
        "Frequently faced pronunciation problems in Malayalam (Malayalam script)",
        "Retroflexes, length, and clusters distinguish many words that look similar in Roman typing.",
        "Use these contrastive sentences to drill difficult sounds with a mirror or teacher.",
        [block_table("Contrastive practice", rows)],
    )


def ch505():
    rows = [
        R("anusvara ം often nasalises the preceding vowel.", "ഗംഗാ നദി വിശുദ്ധമായി കരുതപ്പെടുന്നു.", "gaṁgā nadi viśuddhamāyi karutappeṭunnu."),
        R("ം before velars sounds like ṅ: അംഗം.", "അംഗം സംഘടനയിൽ സജീവമാണ്.", "aṁgaṁ saṁghaṭanayil sajīvamāṇ."),
        R("Candrabindu is not used in Malayalam like Hindi.", "മലയാളത്തിൽ ചന്ദ്രബിന്ദു ഉപയോഗമില്ല.", "malayāḷattil candrabindu upayōgamilla."),
        R("Double ങ്ങ in പൊങ്ങ് (rise).", "സൂര്യൻ കിഴക്കു പൊങ്ങി.", "sūryan kiḻakku poṅṅi."),
        R("ം in സംസ്കാരം links to Sanskrit anusvara rules.", "സംസ്കാരം സമൂഹത്തെ രൂപപ്പെടുത്തുന്നു.", "saṁskāraṁ samūhatte rūpappeṭuttunnu."),
        R("Word-final ം in അം", "ദുഃഖം പങ്കുവെക്കാതെ ഇരിക്കരുത്.", "duḥkhaṁ paṅṅkuvekkāte irukkarut."),
        R("Compare നം and ന് at suffix boundaries.", "ഭവനം വലുത്; ഭവനത്തിന് മുൻപിൽ പൂക്കൾ.", "bhavanaṁ valut; bhavanattin muṉpil pūkkaḷ."),
        R("Sandhi may hide the underlying ം in fast speech.", "വേഗത്തിൽ സംസാരിക്കുമ്പോൾ സന്ധി മാറും.", "vēgattil saṁsārikkumbōḷ sandhi māṟuṁ."),
        R("Learn to read നിങ്ങൾ with ങൾ cluster.", "നിങ്ങൾ എവിടെ നിന്നാണ്?", "niṅṅaḷ evide ninnāṇ?"),
        R("ം + consonant in compounds: സംയോജനം.", "സംയോജനം വിജയകരമായി.", "saṁyōjanaṁ vijayakaramāyi."),
        R("Poetry preserves older ം spellings.", "കവിതയിൽ ഛന്ദസ്സ് മനോഹരമാണ്.", "kavitayil chandas manōharamāṇ."),
        R("Children’s songs repeat ം rhymes.", "കുട്ടിപ്പാട്ടുകൾ ലയത്തിൽ മുഴങ്ങുന്നു.", "kuṭṭippāṭṭukaḷ layattil muḻaṅṅunnu."),
        R("Technical terms from English keep ം rarely.", "ടെക്നിക്കൽ പദങ്ങൾ മിശ്രിതമായി വരുന്നു.", "ṭeknikal padaṅṅaḷ miśritamāyi varunnu."),
        R("Check dictionary for ം vs ന് in verb forms.", "നടക്കുന്നു, നടക്കുന്നത് എന്നിവ ശ്രദ്ധിക്കുക.", "naṭakkunnu, naṭakkunnat enniva śraddhikkuka."),
        R("Mantras show Sanskrit ം clearly.", "മന്ത്രം ജപിക്കുമ്പോൾ ഉച്ചാരണം ശരിയാക്കുക.", "mantraṁ japikkumbōḷ uccāraṇaṁ śariyākkuka."),
        R("Place names: തിരുവനന്തപുരം.", "തിരുവനന്തപുരത്ത് മനോഹരമായ ക്ഷേത്രങ്ങളുണ്ട്.", "tiruvanantapuratt manōharamāya kṣētraṅṅaḷuṇṭ."),
        R("Practice spelling: ലക്ഷം, ദശലക്ഷം.", "ലക്ഷം രൂപ സമ്പാദിക്കാൻ കഠിനാധ്വാനം വേണം.", "lakṣaṁ rūpa sampādikkān kaṭhinādhvānaṁ vēṇaṁ."),
        R("Reading newspapers improves ം recognition.", "പത്രം വായിച്ചാൽ വാക്കുകൾ വ്യക്തമാകും.", "patraṁ vāyiccā vākkukaḷ vyaktamākuṁ."),
    ]
    return chapter(
        505,
        "Pronunciation of Anusvara (ം) and related symbols in Malayalam",
        "The anusvara ം nasalises or homorganically closes syllables; context changes the exact sound.",
        "Read aloud and match spelling to the nasal you actually produce.",
        [block_table("Nasal spelling in context", rows)],
    )


def ch506():
    rows = [
        R("ക്ല in സ്കൂൾ (school).", "സ്കൂളിൽ പഠനം തുടങ്ങി.", "skūlil paṭhanaṁ tuṭaṅṅi."),
        R("ക്ഷ in ക്ഷമ (forgiveness).", "ക്ഷമ ചോദിക്കുന്നത് മാന്യതയാണ്.", "kṣama cōdikkunnat mānyatayāṇ."),
        R("ജ്ഞ in വിജ്ഞാനം.", "വിജ്ഞാനം സമൂഹത്തെ മുന്നോട്ടു നയിക്കുന്നു.", "viññānaṁ samūhatte munnōṭṭu nayikkunnu."),
        R("സ്ത in സ്ത്രീ.", "സ്ത്രീകൾ സമൂഹത്തിന്റെ അടിസ്ഥാന ശക്തിയാണ്.", "strīkaḷ samūhattinṟe aḍisthāna śaktiyāṇ."),
        R("സ്മ in സ്മരണം.", "സ്മരണങ്ങൾ മനസ്സിൽ നിത്യം തെളിയുന്നു.", "smaraṇaṅṅaḷ manassil nityaṁ teḷiyunnu."),
        R("ദ്ധ in സാധ്ധ്യം.", "സാധ്യമായതെല്ലാം ശ്രമിച്ച് ചെയ്യുക.", "sādhyamāyatellāṁ śramicc ceyyuka."),
        R("ത്ഥ in പാത്ഥേയം.", "പാത്ഥേയം വ്യക്തമായി പറയുക.", "pāthyēyaṁ vyaktamāyi paṛayuka."),
        R("മ്പ in സമ്പത്ത്.", "സമ്പത്ത് സന്തോഷത്തിന് മാത്രമല്ല.", "sampatt saṁtōṣattin mātramalla."),
        R("ന്ദ in ആനന്ദം.", "ആനന്ദം പങ്കുവെക്കുന്നത് വർദ്ധിക്കും.", "ānandaṁ paṅṅkuvekkunnat varddhikkuṁ."),
        R("ന്ത in സന്തോഷം.", "സന്തോഷം ആരോഗ്യത്തിന് നല്ലതാണ്.", "saṁtōṣaṁ ārōgyattin nallatāṇ."),
        R("ര്ക്ക in വർക്ക് (work).", "വർക്ക് പൂർത്തിയാക്കാൻ സമയം വേണം.", "varkk pūrttiyākkān samayaṁ vēṇaṁ."),
        R("ല്പ in കല്പന.", "കല്പന സാക്ഷാത്ക്കാരം വേണം.", "kalpana sākṣātkkāraṁ vēṇaṁ."),
        R("ഷ്ട in ദൃഷ്ടി.", "ദൃഷ്ടി വ്യക്തമാക്കി സംസാരിക്കുക.", "dr̥ṣṭi vyaktamākki saṁsārikkuka."),
        R("Practice reading compound-heavy sentences.", "വാക്യങ്ങൾ വീണ്ടും വായിച്ച് പരിശീലിക്കുക.", "vākyaṅṅaḷ vīṇṭuṁ vāyicc pariśīlikkuka."),
        R("Split unknown words into known conjuncts.", "അജ്ഞാത പദങ്ങൾ നിഘണ്ടുവിൽ നോക്കുക.", "ajñāta padaṅṅaḷ nighaṇṭuvil nōkkuka."),
        R("Copy newspaper headlines to learn clusters.", "തലക്കെട്ടുകൾ വേഗത്തിൽ വായിക്കാൻ പഠിക്കുക.", "talakkaṭṭukaḷ vēgattil vāyikkān paṭhikkuka."),
        R("Write five new conjuncts you learnt today.", "ഇന്ന് പഠിച്ച കൂട്ടക്ഷരങ്ങൾ നോട്ടുപുസ്തകത്തിൽ എഴുതുക.", "inn paṭhicca kūṭṭakṣaraṅṅaḷ nōṭṭupustakattil eḻutuka."),
        R("Dictation from teacher improves cluster hearing.", "ഉച്ചാരണം കേട്ട് എഴുതുന്നത് പരിശീലനം നൽകും.", "uccāraṇaṁ kēṭṭ eḻutunna pariśīlanaṁ nalkuṁ."),
    ]
    return chapter(
        506,
        "Combining consonants in Malayalam (കൂട്ടക്ഷരം)",
        "Conjunct letters stack horizontally or use special subjoined forms.",
        "These sentences are rich in clusters; read slowly at first.",
        [block_table("Conjuncts in words", rows)],
    )


def ch507():
    rows = [
        R("ര്‍ combined: പ്രാർത്ഥന (prayer).", "പ്രാർത്ഥന മനസ്സിന് ശാന്തി നൽകും.", "prārththana manassin śānti nalkuṁ."),
        R("ഗ്ര in ഗ്രാമം.", "ഗ്രാമത്തിൽ ജീവിതം ശാന്തമാണ്.", "grāmattil jīvitaṁ śāntamāṇ."),
        R("ദ്ര in ദ്രാവിഡം.", "ദ്രാവിഡ ഭാഷകൾ തമിഴ്നാട്ടിൽ സമൃദ്ധമാണ്.", "drāviḍa bhāṣakaḷ tamizhnāṭṭil samr̥ddhamāṇ."),
        R("ശ്ര in ശ്രദ്ധ.", "ശ്രദ്ധിച്ച് വായിക്കുമ്പോൾ മനസ്സിലാകും.", "śraddhicc vāyikkumbōḷ manassilākuṁ."),
        R("ത്ര in പാത്രം.", "പാത്രം കഴുകി വെച്ച് ഭക്ഷണം നൽകുക.", "pātraṁ kaḻuki vecc bhakṣaṇaṁ nalkuka."),
        R("ര്യ in സംസ്കാര്യം.", "സംസ്കാര്യമായ ഭാഷ ഉപയോഗിക്കുക.", "saṁskāryamāya bhāṣ upayōgikkuka."),
        R("ര്വ in സർവ്വ (all).", "സർവ്വജനഹിതായ സർക്കാർ ആഗ്രഹിക്കുന്നു.", "sarvajanahitāya sarkkār āgrahikkunnu."),
        R("ര്മ in ധർമ്മം.", "ധർമ്മം പാലിക്കുന്നത് മാന്യതയാണ്.", "dharmmaṁ pālikkunna mānyatayāṇ."),
        R("ര്ദ in ബോർഡ്.", "ബോർഡിൽ എഴുതിയ നിർദ്ദേശങ്ങൾ പാലിക്കുക.", "bōril eḻutiya nirddēśaṅṅaḷ pālikkuka."),
        R("ര്ബ in സർബേ (loan style).", "സർബേ ക്ലബ്ബിൽ കായിക പരിശീലനം.", "sarbē klabbil kāyika pariśīlanaṁ."),
        R("ര്പ in ഹർപ്പ്.", "ഹർപ്പ് ശബ്ദം സംഗീതത്തിൽ മനോഹരമാണ്.", "harp śabdaṁ saṁgītattil manōharamāṇ."),
        R("ര്ശ in പർശ്വം.", "പർശ്വം വേദനയുണ്ടെങ്കിൽ ഡോക്ടറെ കാണുക.", "parśvaṁ vēdanayuṇṭeṅkiḷ ḍōkṭare kāṇuka."),
        R("ര്ഷ in വർഷം.", "ഈ വർഷം മഴ കൂടുതലായിരുന്നു.", "ī varṣaṁ maḻa kūtutalāyirunnu."),
        R("ര്സ in പാർസൽ.", "പാർസൽ വന്നു; വാതിൽ തുറന്നു.", "pārsal vannu; vātil tuṟannu."),
        R("ര്ട in പാർട്ട്.", "പാർട്ടിയിൽ സന്തോഷകരമായ സംഭാഷണം.", "pārṭṭiyil saṁtōṣakaramāya saṁbhāṣaṇaṁ."),
        R("ര്ഗ in rare loans; focus on common ര്‍ clusters.", "പൊതുവായ രൂപങ്ങൾ പഠിച്ച് വായിക്കുക.", "pōtuvāya rūpaṅṅaḷ paṭhicc vāyikkuka."),
        R("Double ര്‍ in some names: കേരളം.", "കേരളം സൗന്ദര്യത്തിന്റെ നാടാണ്.", "kēraḷaṁ saundaryattinṟe nāṭāṇ."),
        R("Practice: വരരുത്, പോകരുത് imperative forms.", "വിദ്യാലയത്തിൽ നിയമങ്ങൾ പാലിക്കണം.", "vidyālayattil niyamaṅṅaḷ pālikkaṇaṁ."),
    ]
    return chapter(
        507,
        "Combining consonants with ര (r) – Malayalam കൂട്ടക്ഷരം Part 2",
        "The reph and r-clusters behave differently from Hindi र; practise Malayalam spellings.",
        "Read each word, underline the ര cluster, then say the sentence.",
        [block_table("ര clusters", rows)],
    )


def ch508():
    rows = [
        R("ഹ്ര in ഹ്രസ്വം (short vowel).", "ഹ്രസ്വവും ദീർഘവും വേറെ വേറെ പഠിക്കുക.", "hrasvavum dīrghavum veṛe veṛe paṭhikkuka."),
        R("ഹ്ന in അഹ്നികം (ritual sense in learned words).", "പുരാതന ഗ്രന്ഥങ്ങളിൽ ഹ്ന സമുച്ചയം കാണാം.", "purātana granthaṅṅaḷil hna samuccayaṁ kāṇāṁ."),
        R("ഹ്മ in ബ്രഹ്മം.", "ബ്രഹ്മചര്യം ജീവിതത്തിൽ പ്രാധാന്യമുള്ളതാണ്.", "brahmacaryaṁ jīvitattil prādhānyamuḷḷatāṇ."),
        R("ഹ്യ in ദുഃഖം related forms.", "ദുഃഖം പങ്കിട്ടാൽ ലഘുവാകും.", "duḥkhaṁ paṅṅiṭṭā laghuvākuṁ."),
        R("ഹ്ല in minimal contexts; learn ഹല്‍ (plough).", "കൃഷിയിൽ ഹല്‍ ഉപയോഗിക്കുന്നു.", "kr̥ṣiyil hal upayōgikkunnu."),
        R("ഹ്വ in വഹ്വ് style loans.", "വാഹനം റോഡിൽ സാവധാനം ഓടിക്കുക.", "vāhanaṁ rōṭil sāvadhānaṁ ōṭikkuka."),
        R("ഹ് as pure aspiration before vowels.", "ഹാ, ഇത് നന്നായി!", "hā, it nannāyi!"),
        R("Compare ഹ and ഖ in spelling bees.", "ഖര ശബ്ദങ്ങൾ ഉച്ചരിക്കാൻ ശ്രമിക്കുക.", "khara śabdagaḷ uccarikkān śramikkuka."),
        R("ഹ in ഹൃദയം.", "ഹൃദയം ആരോഗ്യത്തിന് പ്രധാനമാണ്.", "hr̥dayaṁ ārōgyattin pradhānamāṇ."),
        R("ഹ in ഹിമം (snow/ice).", "ഹിമാലയത്തിൽ മഞ്ഞ് കാണാം.", "himālayattil maññ kāṇāṁ."),
        R("ഹ in ഹാസ്യം (humour).", "ഹാസ്യം ജീവിതത്തിൽ ആശ്വാസം നൽകുന്നു.", "hāsyaṁ jīvitattil āsvāsaṁ nalkunnu."),
        R("ഹ in ഹരിതം (green).", "ഹരിതകൃഷി ഭൂമിയെ സംരക്ഷിക്കുന്നു.", "haritakr̥ṣi bhūmiye saṁrakṣikkunnu."),
        R("ഹ in ഹനനം (destruction in formal register).", "ഹനനം ഒഴിവാക്കി സമാധാനം തേടുക.", "hananaṁ oḻivākki samādhānaṁ tēṭuka."),
        R("Practice: മോഹം, ദോഹം contrast.", "മോഹം വേണ്ട; യാഥാർത്ഥ്യം നോക്കുക.", "mōhaṁ vēṇṭa; yāthārthyaṁ nōkkuka."),
        R("ഹ with ള: rare; focus on common ഹ words.", "പാഠപുസ്തകത്തിൽ ഹ അക്ഷരം അടയാളപ്പെടുത്തുക.", "pāṭhapustakattil ha akṣaraṁ aḍayāḷappeṭuttuka."),
        R("Recite ഹരി ഓം if learning devotional style.", "ഭക്തിഗാനങ്ങൾ ഭാവപൂർണ്ണമായി പാടുക.", "bhaktigānaṅṅaḷ bhāvapūrṇṇamāyi pāṭuka."),
        R("Technical ഹ in ഹെൽമെറ്റ്.", "ഹെൽമെറ്റ് ധരിച്ച് സൈക്കിൾ ഓടിക്കുക.", "helmeṭṭ dharicc saikkal ōṭikkuka."),
        R("Write five words starting with ഹ.", "ഹതോത്സാഹം കാണിക്കാതെ പഠനം തുടരുക.", "hatōtsāhaṁ kāṇikkāṭe paṭhanaṁ tuṭaruka."),
    ]
    return chapter(
        508,
        "Combining consonants with ഹ (h) – Malayalam കൂട്ടക്ഷരം Part 3",
        "ഹ combines with vowels and occasionally with following consonants in Sanskrit loans.",
        "Focus on heart, snow, and humour vocabulary with ഹ.",
        [block_table("ഹ vocabulary in sentences", rows)],
    )


def ch509():
    rows = [
        R("ഴ്‍ല in ള്ള് cluster practice.", "പഴം വാങ്ങുമ്പോൾ നല്ലതു തിരഞ്ഞെടുക്കുക.", "paḻaṁ vāṅṅumbōḷ nallat tiraññeṭukkuka."),
        R("Separate ണ് and ഩ് in older orthography.", "ആധുനിക എഴുത്ത് ലളിതമാക്കി.", "ādhunika eḻutt laḷitamākki."),
        R("ക്‍ഷ in ക്ഷേത്രം.", "ക്ഷേത്രത്തിൽ നിശബ്ദത പാലിക്കുക.", "kṣētrattil niśabdata pālikkuka."),
        R("ഡ്‍ in English loans.", "റെയിൽവേ സ്റ്റേഷൻ അടുത്താണ്.", "reyilvē sṟṟēṣaṇ aṭuttāṇ."),
        R("Use chillu letters: ൻ, ർ, ൽ, ൾ, ൺ.", "വാതിൽ തുറന്ന് അകത്തേക്ക് കയറുക.", "vātil tuṟannu akattēkku kayaṟuka."),
        R("Chillu ൻ in അവൻ.", "അവൻ സ്കൂളിൽ പോയി.", "avan skūlil pōyi."),
        R("Chillu ൾ in അവൾ.", "അവൾ നൃത്തം അഭ്യസിക്കുന്നു.", "avaḷ nr̥ttaṁ abhyasikkunnu."),
        R("Numeric chillu ൺ in old texts for ണ്.", "പഴയ കൈയ്യെഴുത്ത് പഠിക്കാൻ ഗ്രന്ഥശാല സന്ദർശിക്കുക.", "paḻaya kaiyeḻutt paṭhikkān granthaśāla sandarśikkuka."),
        R("ZWNJ to break unwanted ligatures in digital text.", "കമ്പ്യൂട്ടറിൽ എഴുതുമ്പോൾ സിംബൾ ശ്രദ്ധിക്കുക.", "kampyūṭṭril eḻutumbōḷ siṁbal śraddhikkuka."),
        R("Compare ട്ട and ണ്ട in വണ്ടി.", "വണ്ടി നിർത്തി ടിക്കറ്റ് കാണിക്കുക.", "vaṇṭi nirtthi ṭikkaṭṭ kāṇikkuka."),
        R("ള്ള double ള in colloquial emphasis.", "വള്ളം കായലിൽ മുന്നോട്ട് പോകുന്നു.", "vaḷḷaṁ kāyalil munnōṭṭ pōkunnu."),
        R("ഞ്ച് cluster in പഞ്ചായത്ത്.", "പഞ്ചായത്ത് യോഗത്തിൽ പങ്കെടുക്കുക.", "pañcāyatt yōgattil paṅṅkeṭukkuka."),
        R("ന്റ് as in വണ്ടി spelled carefully.", "മൊബൈൽ റിപയർ ചെയ്യാൻ കടയിൽ ചെല്ലുക.", "mōbail ripar ceyyān kaṭayil celluka."),
        R("Special ligature ന്റ് in school primers.", "പ്രാഥമിക പാഠപുസ്തകം വായിക്കുക.", "prāthamika pāṭhapustakaṁ vāyikkuka."),
        R("Learn to type chillus on Malayalam keyboard.", "മലയാളം ടൈപ്പ് ചെയ്യാൻ സോഫ്റ്റ്‌വെയർ ഉപയോഗിക്കുക.", "malayāḷaṁ ṭaipp ceyyān sōphṭ‌veyar upayōgikkuka."),
        R("Handwriting joins some letters differently from print.", "എഴുത്ത് പരിശീലനം ദിനവും ചെയ്യുക.", "eḻutt pariśīlanaṁ dinavuṁ ceyyuka."),
        R("Compare printed and handwritten ക്ഷ.", "ക്ഷമയോടെ പഠിച്ചാൽ ലിപി മെച്ചപ്പെടും.", "kṣamayōṭe paṭhiccā lipi meccappeṭuṁ."),
        R("Celebrate mastering special symbols with a short essay.", "അക്ഷരങ്ങൾ അനായാസേന വായിക്കാൻ കഴിയുമ്പോൾ സന്തോഷം തോന്നും.", "akṣaraṅṅaḷ anāyāsēna vāyikkān kaḻiyumbōḷ saṁtōṣaṁ tōnnuṁ."),
    ]
    return chapter(
        509,
        "Special or separate symbols for combined consonants in Malayalam",
        "Chillu letters, reph, and explicit virama distinguish fine details in modern spelling.",
        "These sentences mix chillus, clusters, and everyday words.",
        [block_table("Special symbols in use", rows)],
    )


def _block_chapter(cid, title, rows, heading="Examples"):
    return chapter(
        cid,
        title,
        title,
        "Read each line aloud; the Malayalam column is the one to practise speaking.",
        [block_table(heading, rows)],
    )


def _stub_rows():
    """Placeholder until vocab/conversation modules fill 597–662."""
    from malayalam_lesson_content import R, _pad

    one = R(
        "This lesson’s full word list and dialogues will appear in a future update.",
        "ഈ പാഠത്തിന്റെ പൂർണ്ണ വാക്കുകളും സംഭാഷണങ്ങളും പിന്നീട് ചേർക്കും.",
        "ī pāṭhattinṟe pūrṇṇa vākkukaḷuṁ saṁbhāṣaṇakaḷuṁ piṇīṭ cērkuṁ.",
    )
    return _pad([one])


def main():
    import malayalam_remainder_data as mrd
    import malayalam_remainder_data2 as mrd2
    import malayalam_remainder_tail as mrt
    import malayalam_phrases_571_596 as ph571
    from malayalam_lesson_content import g510, g511, g512, g513, g514
    from malayalam_bulk_rows import rows515, rows516, rows517

    titles = load_titles()
    out = []

    for ch in (ch501, ch502, ch503, ch504, ch505, ch506, ch507, ch508, ch509):
        out.append(ch())

    out.append(_block_chapter(510, titles[510], g510()))
    out.append(_block_chapter(511, titles[511], g511()))
    out.append(_block_chapter(512, titles[512], g512()))
    out.append(_block_chapter(513, titles[513], g513()))
    out.append(_block_chapter(514, titles[514], g514()))
    out.append(_block_chapter(515, titles[515], rows515()))
    out.append(_block_chapter(516, titles[516], rows516()))
    out.append(_block_chapter(517, titles[517], rows517()))

    for cid in range(518, 543):
        out.append(_block_chapter(cid, titles[cid], getattr(mrd, "DATA%d" % cid)))
    for cid in range(543, 556):
        out.append(_block_chapter(cid, titles[cid], getattr(mrd2, "DATA%d" % cid)))
    for cid in range(556, 571):
        out.append(_block_chapter(cid, titles[cid], getattr(mrt, "DATA%d" % cid)))
    for cid in range(571, 597):
        out.append(_block_chapter(cid, titles[cid], getattr(ph571, "DATA%d" % cid)))

    for cid in range(597, 663):
        out.append(_block_chapter(cid, titles[cid], _stub_rows(), heading="Placeholder"))

    out.sort(key=lambda x: x["id"])
    out_path = BASE / "data_malayalam.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("Wrote", out_path, "with", len(out), "chapters (501–662).")


if __name__ == "__main__":
    main()
