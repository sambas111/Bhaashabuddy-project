import glob, json, re, sys
sys.stdout.reconfigure(encoding="utf-8")

en_pat = re.compile(r"\{ en:")
files = sorted(glob.glob("*_data.js"))
print(f"{'file':28} {'total':>6} {'dl_phr':>7} {'dl_wrd':>7}  notes")
bad = []
for f in files:
    t = open(f, encoding="utf-8").read()
    total = len(en_pat.findall(t))
    dl_p = "dailylife_1" in t and "phrases:" in t
    has_dl = t.count("dailylife_")
    # count english==mr untranslated (rough): rows where mr equals en string
    untrans = len(re.findall(r'\{ en: (\"(?:\\.|[^\"\\])*\"), mr: \1', t))
    note = ""
    if total != 2510:
        note += f"COUNT!={2510} "
        bad.append(f)
    if has_dl == 0:
        note += "NO_DAILYLIFE "
        bad.append(f)
    print(f"{f:28} {total:6} {has_dl:7} {untrans:7}  {note}")

print("\nbad files:", sorted(set(bad)) if bad else "none")
