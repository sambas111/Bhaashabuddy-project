# -*- coding: utf-8 -*-
"""Row triples [English, Malayalam script, transliteration] for Malayalam lesson chapters 510–662."""
from __future__ import annotations


def R(e, m, r):
    return [e, m, r]


def _pad(rows, n=18):
    """Ensure exactly n rows (pad if short)."""
    pad_row = R(
        "I will read these sentences again tomorrow.",
        "ഞാൻ നാളെ ഈ വാക്യങ്ങൾ വീണ്ടും വായിക്കും.",
        "njān nāḷe ī vākyaṅṅaḷ vīṇṭuṁ vāyikkuṁ.",
    )
    while len(rows) < n:
        rows.append(pad_row)
    return rows[:n]


# --- 510–529: grammar foundations ---
def g510():
    return _pad(
        [
            R("I eat rice every day.", "ഞാൻ ദിവസവും ചോറ് കഴിക്കുന്നു.", "njān divasavuṁ cōṟ kaḻikkunnu."),
            R("What are you doing now?", "ഇപ്പോൾ നീ എന്ത് ചെയ്യുന്നു?", "ippōḷ nī ent ceyyunnu?"),
            R("Are you from Kerala?", "നിങ്ങൾ കേരളക്കാരാണോ?", "niṅṅaḷ kēraḷakkārāṇō?"),
            R("He works in a bank.", "അവൻ ബാങ്കിൽ ജോലി ചെയ്യുന്നു.", "avan bāṅkil jōli ceyyunnu."),
            R("She is a teacher.", "അവൾ അധ്യാപികയാണ്.", "avaḷ adhyāpikayāṇ."),
            R("We will go together tomorrow.", "നാളെ നമ്മൾ ഒരുമിച്ച് പോകും.", "nāḷe nammaḷ orumicc pōkuṁ."),
            R("They live in Kochi.", "അവർ കോച്ചിയിൽ താമസിക്കുന്നു.", "avar kōcciyil tāmasikkunnu."),
            R("Whose umbrella is this?", "ഇത് ആരുടെ കുടയാണ്?", "it āruṭe kuṭayāṇ?"),
            R("This is my house.", "ഇത് എന്റെ വീടാണ്.", "it enṟe vīṭāṇ."),
            R("That is your car.", "അത് നിന്റെ കാരാണ്.", "at ninṟe kārāṇ."),
            R("Our school is nearby.", "ഞങ്ങളുടെ സ്കൂൾ അടുത്താണ്.", "ñaṅṅaḷuṭe skūḷ aṭuttāṇ."),
            R("Someone left a book on the bench.", "ഒരാൾ ബെഞ്ചിൽ ഒരു പുസ്തകം വെച്ചുപോയി.", "orāḷ benčil oru pustakaṁ veccupōyi."),
            R("Give me one rupee.", "എനിക്ക് ഒരു രൂപ തരൂ.", "enikk oru rūpa tarū."),
            R("These are my books.", "ഇവ എന്റെ പുസ്തകങ്ങളാണ്.", "iva enṟe pustakaṅṅaḷāṇ."),
            R("Those are their bags.", "അവ അവരുടെ ബാഗുകളാണ്.", "ava avaruṭe bāgukaḷāṇ."),
            R("I do not know.", "എനിക്ക് അറിയില്ല.", "enikk aṟiyilla."),
            R("Where do you live?", "നീ എവിടെ താമസിക്കുന്നു?", "nī evide tāmasikkunnu?"),
            R("Who is that man?", "ആ മനുഷ്യൻ ആരാണ്?", "ā manuṣyan ārāṇ?"),
            R("We are students.", "ഞങ്ങൾ വിദ്യാർത്ഥികളാണ്.", "ñaṅṅaḷ vidyārththikaḷāṇ."),
            R("You speak Malayalam well.", "നിങ്ങൾ മലയാളം നന്നായി സംസാരിക്കുന്നു.", "niṅṅaḷ malayāḷaṁ nannāyi saṁsārikkunnu."),
        ],
        n=20,
    )


def g511():
    return _pad(
        [
            R("Please come in; we respect elders in this house.", "ദയവായി അകത്തേക്ക് വരൂ; ഈ വീട്ടിൽ വല്യമ്മമാരെ മാനിക്കുന്നു.", "dayavāyi akattēkku varū; ī vīṭṭil valyammamāre mānikkunnu."),
            R("We speak to our teachers with respect.", "അധ്യാപകരെ ബഹുമാനപൂർവം സംബോധിക്കുന്നു.", "adhyāpakare bahumānapūrvvaṁ saṁbōdhikkunnu."),
            R("We speak politely to strangers in shops.", "അപരിചിതരോട് കടയിൽ ബഹുമാനത്തോടെ സംസാരിക്കുന്നു.", "aparicitarōṭ kaṭayil bahumānattōṭe saṁsārikkunnu."),
            R("Children speak casually with friends and politely with their parents' friends.", "കുട്ടികൾ സുഹൃത്തുക്കൾക്കിടയിൽ “നീ” ഉപയോഗിക്കും; മാതാപിതാക്കളുടെ സുഹൃത്തുക്കളോട് “നിങ്ങൾ”.", "kuṭṭikaḷ suhr̥uttukkḷkkiṭayil “nī” upayōgikkum; mātāpitākkaḷuṭe suhr̥uttukkḷōṭ “niṅṅaḷ”."),
            R("You are coming tomorrow, are you not?", "നാളെ നിങ്ങൾ വരുന്നോ?", "nāḷe niṅṅaḷ varunnō?"),
            R("Many formal letters open with a respectful greeting.", "ഔപചാരിക കത്തുകൾ “ആദരവോടെ” എന്ന് തുടങ്ങുന്നു.", "aupacārika kathukaḷ “ādaravēṭe” ennu tuṭaṅṅunnu."),
            R("We do not call elders by their first name alone.", "മുതിർന്നവർ ഉള്ളപ്പോൾ പേര് മാത്രം വിളിക്കാതെ ശ്രദ്ധിക്കുന്നു.", "mutirnnavar uḷḷappōḷ pēr mātraṁ viḷikkāte śraddhikkunnu."),
            R("We call our parents with love and respect.", "“അമ്മേ”, “അച്ഛാ” എന്നിവ സ്നേഹവും ബഹുമാനവും സൂചിപ്പിക്കുന്നു.", "“amme”, “acchā” enniva snēhavuṁ bahumānavuṁ sūcippikkunnu."),
            R("Guests are offered the best seat in the room.", "അതിഥികൾക്ക് മുറിയിലെ മികച്ച ഇരിപ്പിടം നൽകുന്നു.", "atithikaḷkku muṟiyile mikacca irippiḍaṁ nalkunnu."),
            R("Some very formal speech uses an old polite word for you.", "“താങ്കൾ” എന്ന വാക്ക് ഔപചാരികയോ സാഹിത്യപരമോ ആയ സന്ദർഭങ്ങളിൽ.", "“tāṅṅaḷ” enna vākku aupacārikayō sāhityaparamō āya sandarbhaṅṅaḷil."),
            R("That person helped us carry the bags.", "അവർ ഞങ്ങളുടെ ബാഗുകൾ കയറ്റാൻ സഹായിച്ചു.", "avar ñaṅṅaḷuṭe bāgukaḷ kayṟṭān sahāyiccu."),
            R("Thank you; you helped us a lot.", "നന്ദി; നിങ്ങൾ ഞങ്ങളെ വളരെ സഹായിച്ചു.", "nandi; niṅṅaḷ ñaṅṅaḷe vaḷare sahāyiccu."),
            R("Students stand when the teacher enters the classroom.", "അധ്യാപകൻ പ്രവേശിക്കുമ്പോൾ വിദ്യാർത്ഥികൾ എഴുന്നേൽക്കുന്നു.", "adhyāpakan praveśikkumbōḷ vidyārththikaḷ eḻunnēlkkunnu."),
            R("Are you well, uncle?", "സുഖമാണോ, അമ്മാവനേ?", "sukhamāṇō, ammāvanē?"),
            R("Please pass the water bottle.", "ദയവായി വാട്ടർ ബോട്ടിൽ തരൂ.", "dayavāyi vaṭṭar bōṭṭil tarū."),
            R("We will open the hall at nine o’clock.", "നമ്മൾ ഹാൾ ഒമ്പത് മണിക്ക് തുറക്കും.", "nammaḷ hāḷ ompatu maṇik tuṟakkuᮂ."),
            R("Many people speak Malayalam with elders out of respect.", "മുതിർന്നവരോട് മലയാളം തിരഞ്ഞെടുക്കുന്നത് മര്യാദയാണ്.", "mutirnnavarōṭ malayāḷaṁ tiraññeṭukkunna maryādayāṇ."),
            R("I use polite words when I speak to my manager.", "മാനേജറോട് സംസാരിക്കുമ്പോൾ ഞാൻ മര്യാദയുള്ള വാക്കുകൾ ഉപയോഗിക്കുന്നു.", "mānejṟarōṭ saṁsārikkumbōḷ njān maryādayuḷḷa vākkukaḷ upayōgikkunnu."),
            R("Teacher, please write this on the board.", "അധ്യാപകരേ, ഇത് ബോർഡിൽ എഴുതുക.", "adhyāpakare, it bōrḍil eḻutuka."),
            R("Mother, are you well?", "അമ്മേ, നിങ്ങൾ സുഖമാണോ?", "amme, niṅṅaḷ sukhamāṇō?"),
        ],
        n=20,
    )


def g512():
    return _pad(
        [
            R("I walk every morning.", "ഞാൻ പ്രഭാതത്തിൽ നടക്കുന്നു.", "njān prabhātattil naṭakkunnu."),
            R("I am reading a book now.", "ഞാൻ ഇപ്പോൾ പുസ്തകം വായിക്കുന്നു.", "njān ippōḷ pustakaṁ vāyikkunnu."),
            R("Did you sleep well?", "നിനക്ക് നല്ല ഉറക്കം കിട്ടിയോ?", "ninakku nalla uṟakkaṁ kiṭṭiyō?"),
            R("I will go to Kochi tomorrow.", "നാളെ ഞാൻ കോച്ചിയിലേക്ക് പോകും.", "nāḷe njān kōcciyilēkk pōkuṁ."),
            R("It gets colder when the weather changes.", "കാലാവസ്ഥ മാറുമ്പോൾ തണുപ്പ് കൂടും.", "kālāvastha māṟumbōḷ taṇup kūṭuṁ."),
            R("Mother gave food to the child.", "അമ്മ കുട്ടിക്ക് ഭക്ഷണം കൊടുത്തു.", "amma kuṭṭikk bhakṣaṇaṁ koṭuttu."),
            R("I am not going today.", "ഇന്ന് ഞാൻ പോകുന്നില്ല.", "inn njān pōkunnilla."),
            R("Come here quickly and stand still.", "വേഗം വന്ന് ഇവിടെ നിൽക്കുക.", "vēgaṁ vannu ivide nilkkuka."),
            R("Will you come to see me tomorrow?", "നാളെ കാണാൻ വരുമോ?", "nāḷe kāṇān varumō?"),
            R("I enjoy reading good books.", "നല്ല പുസ്തകം വായിക്കുന്നത് ഇഷ്ടമാണ്.", "nalla pustakaṁ vāyikkunnat iṣṭamāṇ."),
            R("I paid the money and left.", "പണം കൊടുത്തു പോയി.", "paṇaṁ koṭuttu pōyi."),
            R("He was sitting there for a long time.", "അവൻ അവിടെ ഇരിക്കുകയായിരുന്നു.", "avan aviṭe irikkukayāyirunnu."),
            R("I need some rest today.", "ഇന്ന് വിശ്രമം വേണം.", "inn viśramaṁ vēṇaṁ."),
            R("We help each other when we can.", "നമ്മൾ പരസ്പരം സഹായിക്കാം.", "nammaḷ parasparaṁ sahāyikkāṁ."),
            R("They came home in the evening.", "അവർ വീട്ടിൽ വന്നു.", "avar vīṭṭil vannu."),
            R("He helped me carry the bags.", "അവൻ സഹായം ചെയ്തു.", "avan sahāyaṁ ceytu."),
            R("I read the newspaper in class today.", "ഇന്ന് ക്ലാസിൽ പത്രം വായിച്ചു.", "inn klāsil patraṁ vāyiccu."),
            R("I read the book from cover to cover.", "ഞാൻ പുസ്തകം മുഴുവൻ വായിച്ചു.", "njān pustakaṁ muḻuvan vāyiccu."),
            R("The child laughed loudly.", "കുട്ടി ഉച്ചത്തിൽ ചിരിച്ചു.", "kuṭṭi uccattil ciriccu."),
            R("We finish school at four in the afternoon.", "വൈകുന്നേരം നാലുമണിക്ക് സ്കൂൾ അവസാനിക്കും.", "vaikunnēraṁ nālumaṇik skūḷ avasānikkuṁ."),
        ],
        n=20,
    )


def g513():
    return _pad(
        [
            R("I drink tea every morning.", "ഞാൻ ഓരോ പ്രഭാതവും ചായ കുടിക്കുന്നു.", "njān ōrō prabhātavuṁ cāya kuṭikkunnu."),
            R("She teaches Malayalam at the college.", "അവർ കോളേജിൽ മലയാളം പഠിപ്പിക്കുന്നു.", "avar kōḷējil malayāḷaṁ paṭhippikkunnu."),
            R("We live in Thiruvananthapuram now.", "ഞങ്ങൾ ഇപ്പോൾ തിരുവനന്തപുരത്ത് താമസിക്കുന്നു.", "ñaṅṅaḷ ippōḷ tiruvanantapuratt tāmasikkunnu."),
            R("They work in a software company.", "അവർ ഒരു സോഫ്റ്റ്‌വെയർ കമ്പനിയിൽ ജോലി ചെയ്യുന്നു.", "avar oru sōphṭ‌veyar kampaniyil jōli ceyyunnu."),
            R("The bus stops here every ten minutes.", "പത്തു മിനിറ്റിൽ ഒരിക്കൽ ബസ് ഇവിടെ നിർത്തുന്നു.", "pathu miṇiṭṭil orikkal bas ivide nirtthunnu."),
            R("My brother plays cricket on Sundays.", "ഞങ്ങളുടെ സഹോദരൻ ഞായറാഴ്ച ക്രിക്കറ്റ് കളിക്കുന്നു.", "ñaṅṅaḷuṭe sahōdaraṁ ñāyaṟāḻcca krikkeṭṭ kaḷikkunnu."),
            R("The shop opens at nine o’clock.", "കട ഒമ്പത് മണിക്ക് തുറക്കുന്നു.", "kaṭa ompatu maṇik tuṟakkunnu."),
            R("Mother cooks rice and curry for lunch.", "അമ്മ ഉച്ചയ്ക്ക് ചോറും കറിയും ഉണ്ടാക്കുന്നു.", "amma uccaykku cōṟuṁ kaṛiyuṁ uṇṭākkunnu."),
            R("Birds sing in the mango tree.", "മാവിന് ചുവട്ടിൽ പക്ഷികൾ പാടുന്നു.", "māvin cuvaṭṭil pakṣikaḷ pāṭunnu."),
            R("The sea looks calm this evening.", "ഈ സായാഹ്നം കടൽ ശാന്തമായി കാണപ്പെടുന്നു.", "ī sāyāhnaṁ kaḍal śāntamāyi kāṇappeṭunnu."),
            R("Children draw pictures in the classroom.", "കുട്ടികൾ ക്ലാസ് മുറിയിൽ ചിത്രങ്ങൾ വരയ്ക്കുന്നു.", "kuṭṭikaḷ klās muṟiyil citraṅṅaḷ varaykkunnu."),
            R("Grandfather reads the newspaper after breakfast.", "അപ്പൂപ്പൻ പ്രാതൽ കഴിഞ്ഞ് പത്രം വായിക്കുന്നു.", "appūppan prātal kaḻiññ patraṁ vāyikkunnu."),
            R("We watch the news on television at night.", "ഞങ്ങൾ രാത്രി ടെലിവിഷനിൽ വാർത്ത കാണുന്നു.", "ñaṅṅaḷ rātri ṭeliviṣanil vārttha kāṇunnu."),
            R("The train leaves from platform number three.", "ട്രെയിൻ മൂന്നാം പ്ലാറ്റ്ഫോമിൽ നിന്ന് പുറപ്പെടുന്നു.", "ṭreyin mūnnāṁ plāṭṭphōmil ninn puṛappeṭunnu."),
            R("Farmers harvest paddy in December.", "കർഷകർ ഡിസംബറിൽ നെൽകൃഷി കൊയ്യുന്നു.", "karṣakar ḍisambaril nelkr̥ṣi koyyunnu."),
            R("The doctor examines patients in the morning.", "ഡോക്ടർ പ്രഭാതത്തിൽ രോഗികളെ പരിശോധിക്കുന്നു.", "ḍōkṭṭar prabhātattil rōgikaḷe pariśōdhikkunnu."),
            R("I write emails in English for my office.", "ഞാൻ ഓഫീസിന് ഇംഗ്ലീഷിൽ ഇമെയിൽ എഴുതുന്നു.", "njān ōphīsin iṅglīṣil imeyil eḻutunnu."),
            R("We celebrate Onam with flowers and feasts.", "ഞങ്ങൾ പൂക്കളത്തോടും വിരുന്നോടും ഓണം ആഘോഷിക്കുന്നു.", "ñaṅṅaḷ pūkkaḷattōṭuṁ virunnōṭuṁ ōṇaṁ āghōṣikkunnu."),
            R("I teach Malayalam at a small school.", "ഞാൻ മലയാളം പഠിപ്പിക്കുന്നു.", "njān malayāḷaṁ paṭhippikkunnu."),
            R("The sun rises in the east.", "സൂര്യൻ കിഴക്കു ഉദിക്കുന്നു.", "sūryan kiḻakku udikkunnu."),
        ],
        n=20,
    )


def g514():
    return _pad(
        [
            R("I am a teacher.", "ഞാൻ അധ്യാപകനാണ്.", "njān adhyāpakanāṇ."),
            R("She is a doctor.", "അവൾ ഡോക്ടറാണ്.", "avaḷ ḍōkṭarāṇ."),
            R("This is my house.", "ഇത് എന്റെ വീടാണ്.", "it enṟe vīṭāṇ."),
            R("Those are our books.", "അവ ഞങ്ങളുടെ പുസ്തകങ്ങളാണ്.", "ava ñaṅṅaḷuṭe pustakaṅṅaḷāṇ."),
            R("He was tired yesterday.", "അവൻ ഇന്നലെ ക്ഷീണിതനായിരുന്നു.", "avan innale kṣīṇitanāyirunnu."),
            R("We will be ready in ten minutes.", "ഞങ്ങൾ പത്തു മിനിറ്റിൽ തയ്യാറായിരിക്കും.", "ñaṅṅaḷ pathu miṇiṭṭil tayyāyāyirikuṁ."),
            R("It is raining heavily now.", "ഇപ്പോൾ കനത്ത മഴ പെയ്യുന്നു.", "ippōḷ kanatta maḻa peyyunnu."),
            R("There were many people at the temple.", "ക്ഷേത്രത്തിൽ ധാരാളം ആളുകൾ ഉണ്ടായിരുന്നു.", "kṣētrattil dhārāḷaṁ āḷukaḷ uṇṭāyirunnu."),
            R("I am not angry with you.", "ഞാൻ നിനോട് ദുഷിച്ചിട്ടില്ല.", "njān ninōṭ duṣicc iṭṭilla."),
            R("Are you ready for the journey?", "നിനക്ക് യാത്രയ്ക്ക് തയ്യാറാണോ?", "ninakk yātraykku tayyāṟāṇō?"),
            R("This place is famous for spices.", "ഈ സ്ഥലം മസാലകൾക്ക് പ്രസിദ്ധമാണ്.", "ī sthalaṁ masālakaḷkku prasiddhamāṇ."),
            R("The keys were on the table.", "ചാവികൾ മേശയ്ക്ക് മുകളിലായിരുന്നു.", "cāvikaḷ mēśaykku mukaḷilāyirunnu."),
            R("I have been a resident here for five years.", "ഞാൻ ഇവിടെ അഞ്ചു വർഷമായി താമസിക്കുന്നു.", "njān ivide añcu varṣamāyi tāmasikkunnu."),
            R("The child is afraid of loud sounds.", "കുട്ടിക്ക് ഉച്ച ശബ്ദങ്ങൾ പേടിയാണ്.", "kuṭṭikku ucca śabdagaḷ pēṭiyāṇ."),
            R("Those mountains are beautiful in the monsoon.", "മൺസൂണിൽ ആ മലകൾ മനോഹരമാണ്.", "maṇsūṇil ā malakaḷ manōharamāṇ."),
            R("We are grateful for your hospitality.", "നിങ്ങളുടെ സത്കാരത്തിന് ഞങ്ങൾ നന്ദിയുള്ളവരാണ്.", "niṅṅaḷuṭe satkārattin ñaṅṅaḷ nandiyuḷḷavarāṇ."),
            R("The hall was empty after the programme.", "പരിപാടിക്ക് ശേഷം ഹാൾ ശൂന്യമായിരുന്നു.", "paripāṭikk śeṣaṁ hāḷ śūnyamāyirunnu."),
            R("I am learning Malayalam step by step.", "ഞാൻ ഘട്ടം ഘട്ടമായി മലയാളം പഠിക്കുന്നു.", "njān ghaṭṭaṁ ghaṭṭamāyi malayāḷaṁ paṭhikkunnu."),
            R("There is rice on the plate.", "പ്ലേറ്റിൽ ചോറുണ്ട്.", "plēṭṭil cōṟuṇṭ."),
            R("The keys are on the table.", "ചാവികൾ മേശയിലാണ്.", "cāvikaḷ mēśayilāṇ."),
        ],
        n=20,
    )
