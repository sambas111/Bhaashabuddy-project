#!/usr/bin/env python3
"""
Scrape Gujarati lessons from learnmarathiwithkaushik.com/gujarati-from-english/
Outputs data_gujarati.json with id, title, url, content for each lesson.
Requires: pip install requests beautifulsoup4
"""

import json
import re
import time
from pathlib import Path
from urllib.parse import urljoin

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Install: pip install requests beautifulsoup4")
    exit(1)

BASE_URL = "https://learnmarathiwithkaushik.com"
GUJARATI_INDEX = f"{BASE_URL}/gujarati-from-english/"
COURSES_PREFIX = f"{BASE_URL}/courses/"

# Skip non-lesson links (e.g. contact, about)
SKIP_URLS = {"contact-us"}


def fetch_page(url):
    """Fetch page with retries."""
    for _ in range(3):
        try:
            r = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
            r.raise_for_status()
            return r.text
        except Exception as e:
            print(f"  Retry: {e}")
            time.sleep(2)
    return None


# Lesson URLs in order (from gujarati-from-english index page)
LESSON_URLS = [
    "https://learnmarathiwithkaushik.com/courses/welcome-to-world-of-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/tips-to-learn-gujarati-rather-any-new-language/",
    "https://learnmarathiwithkaushik.com/courses/alphabets-in-gujarati-script/",
    "https://learnmarathiwithkaushik.com/courses/gujarati-barakhadi-barakshari/",
    "https://learnmarathiwithkaushik.com/courses/pronunciation-of-anusvar-%e0%aa%85%e0%aa%a8%e0%ab%81%e0%aa%b8%e0%ab%8d%e0%aa%b5%e0%aa%be%e0%aa%b0-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/combining-consonants-in-gujarati-%e0%aa%97%e0%ab%81%e0%aa%9c%e0%aa%b0%e0%aa%be%e0%aa%a4%e0%ab%80-%e0%aa%9c%e0%ab%8b%e0%aa%a1%e0%aa%be%e0%aa%95%e0%ab%8d%e0%aa%b7%e0%aa%b0/",
    "https://learnmarathiwithkaushik.com/courses/combining-consonants-with-%e0%aa%b0r-%e0%aa%97%e0%ab%81%e0%aa%9c%e0%aa%b0%e0%aa%be%e0%aa%a4%e0%ab%80-%e0%aa%9c%e0%ab%8b%e0%aa%a1%e0%aa%be%e0%aa%95%e0%ab%8d%e0%aa%b7%e0%aa%b0-part-2/",
    "https://learnmarathiwithkaushik.com/courses/combining-consonants-with-%e0%aa%b9h-%e0%aa%97%e0%ab%81%e0%aa%9c%e0%aa%b0%e0%aa%be%e0%aa%a4%e0%ab%80-%e0%aa%9c%e0%ab%8b%e0%aa%a1%e0%aa%be%e0%aa%95%e0%ab%8d%e0%aa%b7%e0%aa%b0-part-3/",
    "https://learnmarathiwithkaushik.com/courses/special-or-separate-symbols-for-combined-consonants-%e0%aa%97%e0%ab%81%e0%aa%9c%e0%aa%b0%e0%aa%be%e0%aa%a4%e0%ab%80-%e0%aa%9c%e0%ab%8b%e0%aa%a1%e0%aa%be%e0%aa%95%e0%ab%8d%e0%aa%b7%e0%aa%b0-part-4/",
    "https://learnmarathiwithkaushik.com/courses/pronouns-and-articles-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/working-with-nounsgenders-and-plurals-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/%e0%aa%93-%e0%aa%88-%e0%aa%89%e0%aa%82-%e0%aa%86-%e0%aa%88-%e0%aa%86%e0%aa%82-o-i-um-a-i-am-%e0%aa%af%e0%ab%8b-%e0%aa%88-%e0%aa%af%e0%ab%81%e0%aa%82-%e0%aa%af%e0%aa%be-%e0%aa%88-%e0%aa%af%e0%aa%be/",
    "https://learnmarathiwithkaushik.com/courses/using-plurals-to-indicate-respect-%e0%aa%86%e0%aa%a6%e0%aa%b0%e0%aa%be%e0%aa%b0%e0%ab%8d%e0%aa%a5%e0%ab%80-%e0%aa%ac%e0%aa%b9%e0%ab%81%e0%aa%b5%e0%aa%9a%e0%aa%a8-adararthi-bahuvachan/",
    "https://learnmarathiwithkaushik.com/courses/verbs-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/simple-present-tense-of-to-be-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/simple-present-tense-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/simple-future-tense-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/simple-past-tense-of-to-be-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/simple-past-tense-in-gujarati-part-1/",
    "https://learnmarathiwithkaushik.com/courses/simple-past-tense-in-gujarati-part-2/",
    "https://learnmarathiwithkaushik.com/courses/present-continuous-tense-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/past-continuous-tense-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/future-continuous-tense-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/negative-sentence-in-simple-present-tense-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/negative-sentence-in-present-continuous-tense-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/negative-sentence-in-simple-past-tense-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/negative-sentence-in-past-continuous-tense-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/negative-sentences-in-simple-future-tense-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/negative-sentence-in-future-continuous-tense-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/present-past-future-perfect-tense-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/past-present-future-perfect-continuous-tense-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/commands-imperative-statements-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/saying-my-his-her-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/preposition-to-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/sentences-with-living-person-or-human-being/",
    "https://learnmarathiwithkaushik.com/courses/asking-questions-in-gujarati-part-1/",
    "https://learnmarathiwithkaushik.com/courses/asking-wh-questions-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/learn-prepositions-in-gujarati-language/",
    "https://learnmarathiwithkaushik.com/courses/prepositions-with-nouns-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/cases-in-gujarati-%e0%aa%b5%e0%aa%bf%e0%aa%ad%e0%aa%95%e0%ab%8d%e0%aa%a4%e0%aa%bf-vibhakti-and-%e0%aa%b5%e0%aa%bf%e0%aa%ad%e0%aa%95%e0%ab%8d%e0%aa%a4%e0%aa%bf-%e0%aa%aa%e0%ab%8d%e0%aa%b0%e0%aa%a4/",
    "https://learnmarathiwithkaushik.com/courses/asking-wh-questions-with-prepositions-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/adjectives-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/using-phrase-to-keep-doing-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/using-verb-to-want-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/using-verb-to-know-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/saying-to-come-to-know-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/using-to-understand-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/using-to-like-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/using-going-to-phrase-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/using-verb-can-to-be-able-to-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/using-verb-to-remember-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/using-to-want-to-need-with-other-verbs-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/using-should-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/sentences-using-would-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/saying-phrase-must-have-to-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/prepositions-with-verbs-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/using-let-and-shall-we-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/saying-to-become-to-happen-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/asking-permission-and-requesting-someone-may-i-can-you-etc/",
    "https://learnmarathiwithkaushik.com/courses/comparison-and-degrees-of-comparison-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/sentence-using-if-then-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/simple-future-tense-in-conditional-statements/",
    "https://learnmarathiwithkaushik.com/courses/sentence-using-used-to-phrase-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/which-that-what-that-sentences-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/using-to-feel-to-think-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/add-a-question-tag-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/to-emphasize-word-using-%e0%aa%9cj-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/showing-uncertainty-using-may-might-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/using-to-mean-how-to-ask-meaning-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/to-have-to-indicate-possession-and-relation-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/adjectives-made-from-verbs-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/generalizing-words-somewhere-somehow-anything-anybody-etc-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/adverbs-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/using-like-to-indicate-similarity-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/active-voice-and-passive-voice-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/phrase-to-make-someone-do-something-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/using-may-to-express-wish-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/time-related-words-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/numbers-in-gujarati-part-1/",
    "https://learnmarathiwithkaushik.com/courses/numbers-in-gujarati-part-2/",
    "https://learnmarathiwithkaushik.com/courses/fractional-numbers-sequence-percentage-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/conjunctions-in-gujarati-part-1-andbutbecausesothatalthoughthoughstillyet/",
    "https://learnmarathiwithkaushik.com/courses/conjunctions-in-gujarati-part-2-asas-well-asor-neither-nor-ifin-case-provided/",
    "https://learnmarathiwithkaushik.com/courses/conjunctions-in-gujarati-part-3-after-thenas-far-as-as-long-asas-if-as-though/",
    "https://learnmarathiwithkaushik.com/courses/conjunctions-in-gujarati-part-4-as-soon-as-oncerather-than-instead-ofso-thatwhereaswhether-or-notalso/",
    "https://learnmarathiwithkaushik.com/courses/list-of-conjunctions-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/list-of-body-parts-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/relations-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/simple-sentences-in-gujarati-introduction-salutation/",
    "https://learnmarathiwithkaushik.com/courses/simple-gujarati-sentences-where-place-related/",
    "https://learnmarathiwithkaushik.com/courses/asking-address-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/greetingwishesblessingsslogans-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/simple-gujarati-sentences-in-hotel/",
    "https://learnmarathiwithkaushik.com/courses/simple-gujarati-conversation-grocery-shop/",
    "https://learnmarathiwithkaushik.com/courses/simple-gujarati-conversation-at-bus-stop-and-in-bus/",
    "https://learnmarathiwithkaushik.com/courses/simple-gujarati-conversation-rickshaw-taxi-driver/",
    "https://learnmarathiwithkaushik.com/courses/simple-gujarati-conversation-software-engineers/",
    "https://learnmarathiwithkaushik.com/courses/simple-gujarati-conversation-doctor-patient/",
    "https://learnmarathiwithkaushik.com/courses/simple-gujarati-conversation-teacher-students/",
    "https://learnmarathiwithkaushik.com/courses/simple-gujarati-conversation-informal-phone-conversation/",
    "https://learnmarathiwithkaushik.com/courses/simple-gujarati-conversation-at-vegetable-market/",
    "https://learnmarathiwithkaushik.com/courses/simple-gujarati-conversation-with-traffic-police/",
    "https://learnmarathiwithkaushik.com/courses/simple-gujarati-sentences-weather-related/",
    "https://learnmarathiwithkaushik.com/courses/simple-gujarati-conversation-interview-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/simple-gujarati-conversation-with-housemaid/",
    "https://learnmarathiwithkaushik.com/courses/i-love-you-in-gujarati-proposing-someone-in-gujarati/",
    "https://learnmarathiwithkaushik.com/courses/simple-gujarati-conversation-linking-aadhar-card-to-mobile-number/",
    "https://learnmarathiwithkaushik.com/courses/type-gujarati-in-roman-gujarati-transliteration/",
]


def extract_lesson_links(html):
    """Fallback: extract from HTML if LESSON_URLS not used."""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a.get("href", "")
        if COURSES_PREFIX in href and not any(s in href.lower() for s in SKIP_URLS):
            full = href.split("?")[0].rstrip("/")
            if full not in links:
                links.append(full)
    return links


def extract_lesson_content(html, url):
    """Extract title and main content from a lesson page."""
    soup = BeautifulSoup(html, "html.parser")
    title = ""
    content_parts = []

    # Main content first (LearnDash uses .lesson_content)
    main = soup.select_one(".lesson_content, .entry-content, .ld-item-content, .learndash-content")
    if not main:
        main = soup.find("article") or soup.find("main")

    # Title: prefer h1 inside lesson area, else any h1 with actual lesson title
    if main:
        h1_in_main = main.select_one("h1")
        if h1_in_main:
            title = h1_in_main.get_text(strip=True)
    if not title:
        for h1 in soup.find_all("h1"):
            raw = h1.get_text(strip=True)
            if raw and len(raw) > 5 and "Kaushik" not in raw and "Learn Marathi" not in raw:
                title = raw
                break
    if not title:
        slug = url.rstrip("/").split("/")[-1]
        title = slug.replace("-", " ").replace("%20", " ").title()

    if main:
        for el in main.find_all(["p", "h2", "h3", "h4", "li", "td", "th"]):
            text = el.get_text(separator=" ", strip=True)
            if text and len(text) > 2 and "Copyright" not in text:
                tag = el.name
                if tag == "h2":
                    content_parts.append(f"\n## {text}\n")
                elif tag == "h3":
                    content_parts.append(f"\n### {text}\n")
                elif tag == "h4":
                    content_parts.append(f"\n#### {text}\n")
                else:
                    content_parts.append(text)

    content = "\n".join(content_parts).strip()
    for marker in ["Copyright ©", "Developed By", "Next Lesson", "Previous Lesson"]:
        idx = content.find(marker)
        if idx > 0:
            content = content[:idx].strip()
    return title, content


def main():
    out_path = Path(__file__).parent / "data_gujarati.json"
    links = [u.rstrip("/") for u in LESSON_URLS]
    print(f"Scraping {len(links)} lesson URLs")
    chapters = []
    for i, url in enumerate(links):
        print(f"[{i+1}/{len(links)}] {url.split('/')[-2][:50]}...")
        h = fetch_page(url)
        if h:
            title, content = extract_lesson_content(h, url)
            if not title:
                title = url.split("/")[-2].replace("-", " ").title()
            chapters.append({"id": i + 1, "title": title, "url": url, "content": content})
        time.sleep(0.5)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(chapters, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(chapters)} chapters to {out_path}")


if __name__ == "__main__":
    main()
