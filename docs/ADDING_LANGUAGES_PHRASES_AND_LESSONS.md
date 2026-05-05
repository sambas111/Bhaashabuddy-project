# Simple prompts for adding language / lessons / phrases

Use **Agent mode** for edits and running scripts. Use **Composer 2** or **Opus** when you care about grammar and spelling. If one model messes up, try the other.

**“Don’t translate”** here means: don’t only convert English → target language in your head. **Search the web** for real examples, grammar notes, or a standard book (e.g. for Kashmiri), then build sentences that match that language — not word-for-word English.

---

## Copy-paste prompts (plain English)

You can change `[language]` or `Kashmiri` to whatever you need.

**1. Fill / refresh a whole section (web + on-topic sentences)**  
```
ok now add for [language] — search the web — use good long or medium size sentences relevant to each sublesson. search web. dont translate only — keep examples real for that lesson topic.
```

**2. Same idea, with row count**  
```
check all sublessons for [language] — remove weak or off-topic lines — write relevant to-the-point sentences: correct English, native script, and transliteration. at least 15 to 20 per sublesson. not repeating the same lines everywhere. each sublesson should match its title (e.g. past tense only past examples).
```

**3. Fix one grammar lesson that has junk**  
```
lesson [id or title] for [language] — remove lines that are wrong tense or random phrasebook stuff. replace with medium/long sentences that only fit this grammar topic. search web if needed. then run the patch script for this project.
```

**4. After content is in the Python data file**  
```
run py -3 patch_[language]_section2_lessons.py from Bhaashabuddy-project folder and make sure data_[language].json updated
```
(Adjust the script name if your section uses a different patch file.)

**5. Short version (fastest)**  
```
search web for [language] grammar examples for section 2 sublessons — medium/long sentences — on topic — update kashmiri_s2_data.py (or the right *_data.py) — dont translate — run patch script
```

---

## What you’re asking the AI to do (in simple terms)

| You say | What it should do |
|--------|---------------------|
| **search web** | Look up real usage, grammar sketches, or trusted pages — not guess from English only. |
| **long / medium sentences** | Enough words to show grammar clearly; not one-word answers. |
| **relevant to sublessons** | “Past tense” lesson → past examples only. Not “thank you” unless the lesson is greetings. |
| **dont translate** | Build natural target-language lines; avoid English-think word order and random glosses. |
| **15–20 per table** | Match what the app expects (here we used 20 rows per table). |
| **not repeating** | Don’t paste the same 20 lines into every sublesson. |

---

## Where files usually are (for Bhaashabuddy)

- **Lesson list / IDs:** `lessons_structure_<language>.json`
- **What the app shows:** `data_<language>.json`
- **Big tables in code:** e.g. `kashmiri_s2_data.py` with a `PATCH` dict, then  
  `py -3 patch_kashmiri_section2_lessons.py`  
  to push rows into `data_kashmiri.json`

If the patch says it updated 0 lessons, the **table heading** in the Python file must match the **heading** in JSON **exactly**.

---

## Models — keep it simple

| Job | Model |
|-----|--------|
| Grammar, script, long tables | **Opus** (or best “smart” model you have) |
| Edit many files, run commands, patch | **Composer 2** |
| Something went wrong | Switch model and paste the same simple prompt again |

---

## Optional: more detail (tables, headings, quality)

Only if you need it — same ideas as above, with file names and checklists.

<details>
<summary>Expand</summary>

### Files (same as before, short)

| Piece | Files |
|--------|--------|
| Structure / order | `lessons_structure_<lang>.json` |
| App text + tables | `data_<lang>.json` |
| Many table rows | `*_s2_data.py` + `patch_*_section*_lessons.py` |

### Before ship (quick)

- [ ] Each lesson has the right number of rows (e.g. 20).
- [ ] Examples match the lesson title (tense, topic).
- [ ] No duplicate “thank you / welcome / police” in a grammar-only lesson.
- [ ] Patch script ran; JSON is valid.

</details>

---

*These prompts match the style of requests we used in the Kashmiri section-2 work: web search, on-topic long/medium lines, and “don’t translate” as in don’t fake the language with English calques.*
