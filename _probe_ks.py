import requests
from bs4 import BeautifulSoup

def try_tl(tl):
    r = requests.get(
        "https://translate.google.com/m",
        params={"sl": "en", "tl": tl, "q": "Hello"},
        timeout=25,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    s = BeautifulSoup(r.text, "html.parser")
    el = s.find("div", class_="t0") or s.find("div", class_="result-container")
    return el.get_text(strip=True) if el else ""

with open("_ks_codes.txt", "w", encoding="utf-8") as out:
    for tl in ["ks", "kas", "ur", "hi", "gom", "doi", "sd", "ps"]:
        t = try_tl(tl)
        out.write(f"{tl}\t{t}\n")
