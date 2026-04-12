# -*- coding: utf-8 -*-
from pathlib import Path

path = Path(__file__).resolve().parent / "malayalam_remainder_data.py"
lines = path.read_text(encoding="utf-8").splitlines(keepends=True)

subs = {
    "contrast outside and inside": '    ("The children play outside and eat inside.", "കുട്ടികൾ പുറത്ത് കളിക്കുകയും അകത്ത് ഭക്ഷണം കഴിക്കുകയും ചെയ്യുന്നു.", "kuṭṭikaḷ puṛatt kaḷikkukayuṁ akatt bhakṣaṇaṁ kaḻikkukayuṁ ceyyunnu."),',
    "Do not confuse “മേൽ” (above) with “കീഴ്” (below)": '    ("The book is on the shelf; the shoes are below.", "പുസ്തകം അലമാരിയിൽ; ചെരുപ്പുകൾ താഴെയാണ്.", "pustakaṁ alamāriyil; ceruppuḷ tāḻeyāṇ."),',
    '"നിന്ന്" shows source: from the shop': '    ("I bought rice from the shop.", "ഞാൻ കടയിൽ നിന്ന് ചോറ് വാങ്ങി.", "njān kaṭayil ninn cōṟ vāṅṅi."),',
    '"വരെ" expresses extent: from here to there': '    ("We walked from here to the bus stop.", "ഞങ്ങൾ ഇവിടെ മുതൽ ബസ് സ്റ്റോപ്പ് വരെ നടന്നു.", "ñaṅṅaḷ ivide mutal bas sṟṟōpp vare naṭannu."),',
    '"കൊണ്ട്" often marks reason or instrument': '    ("He stayed home because of the rain.", "മഴ കൊണ്ട് അവൻ വീട്ടിൽ താമസിച്ചു.", "maḻa koṇṭ avan vīṭṭil tāmasiccu."),',
    '"ആയി" links nouns: teacher became writer': '    ("My uncle became a writer after retirement.", "റിട്ടയർമെന്റിന് ശേഷം അമ്മാവൻ എഴുത്തുകാരനായി.", "riṭṭayarmentin śeṣaṁ ammāvan eḻuttukāranāyi."),',
    '"വേണ്ടി" shows purpose: for the children': '    ("Mother cooked lunch for the children.", "അമ്മ കുട്ടികൾക്ക് ഉച്ചഭക്ഷണം ഉണ്ടാക്കി.", "amma kuṭṭikaḷkku uccabhakṣaṇaṁ uṇṭākki."),',
    '"കൂടെ" means together: came with me': '    ("My friend came with me to the station.", "സുഹൃത്ത് എന്റെ കൂടെ സ്റ്റേഷനിലേക്ക് വന്നു.", "suhr̥utt enṟe kūṭe sṟṟēṣanilēkk vannu."),',
    '"പോലെ" compares: like gold': '    ("Her necklace shines like gold.", "അവളുടെ നെക്ലസ് സ്വർണ്ണം പോലെ മിന്നുന്നു.", "avaḷuṭe neklas svarṇṇaṁ pōle minnunnu."),',
    '"മാത്രം" restricts: only today': '    ("I can stay only today.", "എനിക്ക് ഇന്ന് മാത്രം താമസിക്കാം.", "enikk inn mātraṁ tāmasikkāᮂ."),',
    '"വരെ" with time: until evening': '    ("We worked until evening.", "ഞങ്ങൾ സായാഹ്നം വരെ ജോലി ചെയ്തു.", "ñaṅṅaḷ sāyāhnaᮂ vare jōli ceytu."),',
    '"ഇടയിൽ" means between two things': '    ("The shop is between the bank and the post office.", "ബാങ്കിനും പോസ്റ്റ് ഓഫീസിനും ഇടയിലാണ് കട.", "bāṅkinuᮂ pōsṭ ṭōphisinuᮂ iṭayilāṇ kaṭa."),',
    '"മുകളിൽ" is on top of a surface': '    ("The book is on the table.", "മേശയ്ക്ക് മുകളിൽ പുസ്തകം.", "mēśaykku mukaḷil pustakaᮂ."),',
    '"പിന്നിൽ" is behind spatially': '    ("Walk behind the vehicle.", "വാഹനത്തിന് പിന്നിൽ നടക്കുക.", "vāhanattin piṉnil naṭakkuka."),',
    '"മുന്നിൽ" is in front': '    ("Please wait in front of the gate.", "ഗേറ്റിന് മുന്നിൽ നിൽക്കുക.", "gēṭṭin munnil nilkkuka."),',
    "Practice prepositions in full sentences, not word lists alone": '    ("I pack my bag before every trip.", "ഓരോ യാത്രയ്ക്കും മുമ്പ് ഞാൻ ബാഗ് പാക്ക് ചെയ്യുന്നു.", "ōrō yātraykkuᮂ mumpe njān bāk pāk ceyyunnu."),',
}

# Fix ṁ characters - use proper ṁ in transliteration
for k in list(subs.keys()):
    pass

out = []
for line in lines:
    replaced = False
    for key, new_line in subs.items():
        if key in line:
            out.append(new_line + ("\n" if not new_line.endswith("\n") else ""))
            if not new_line.endswith("\n"):
                out[-1] = new_line + "\n"
            replaced = True
            break
    if not replaced:
        out.append(line)

path.write_text("".join(out), encoding="utf-8")
print("done")
