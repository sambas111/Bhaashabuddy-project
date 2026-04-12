#!/usr/bin/env python3
"""Generate data_assamese.json for BhaashaBuddy — mirrors Maithili lesson IDs 501–662
with Bengali (Bangla) content. References: Bangla barnamala, যুক্তাক্ষর, standard grammar."""
import json

from assamese_lesson_helpers import H, S, r, ch, block_table, blk_para


def main():
    out = []

    # ----- 501 Bengali alphabets -----
    out.append(
        ch(
            501,
            "Bengali Alphabets – Bangla Barnamala (Eastern Nagari)",
            "Bengali is written in the Eastern Nagari script. Learn vowels (স্বরবর্ণ) and consonants (ব্যঞ্জনবর্ণ).",
            "Bangla uses 11 vowel letters and about 39 consonants. Each consonant has an inherent vowel /ɔ/; vowel signs (কার) attach to consonants.",
            tables=[
                {
                    "heading": "Vowels in Bengali (স্বরবর্ণ)",
                    "headers": ["Letter", "Transliteration"],
                    "speakCol": 1,
                    "rows": [
                        ["অ", "ô / o"],
                        ["আ", "a"],
                        ["ই", "i"],
                        ["ঈ", "i"],
                        ["উ", "u"],
                        ["ঊ", "u"],
                        ["ঋ", "ri"],
                        ["এ", "e"],
                        ["ঐ", "oi"],
                        ["ও", "o"],
                        ["ঔ", "ou"],
                    ],
                },
                {
                    "heading": "Vowel usage examples",
                    "headers": H,
                    "speakCol": S,
                    "rows": [
                        r("name", "নাম", "nām"),
                        r("water", "জল", "jôl"),
                        r("rice", "ভাত", "bhāt"),
                        r("day", "দিন", "din"),
                        r("house", "বাড়ি", "bāṛi"),
                        r("good", "ভালো", "bhālō"),
                        r("today", "আজ", "āj"),
                        r("come", "আসা", "āsā"),
                        r("tea", "চা", "chā"),
                        r("one", "এক", "ek"),
                        r("two", "দুই", "dui"),
                        r("body", "শরীর", "shorīr"),
                        r("yes", "হ্যাঁ", "hyẫ"),
                        r("no", "না", "nā"),
                    ],
                },
                {
                    "heading": "Consonants in Bengali (ব্যঞ্জনবর্ণ) — sample",
                    "headers": ["Letter", "Transliteration"],
                    "speakCol": 1,
                    "rows": [
                        ["ক", "k"],
                        ["খ", "kh"],
                        ["গ", "g"],
                        ["ঘ", "gh"],
                        ["ঙ", "ng"],
                        ["চ", "ch"],
                        ["ছ", "chh"],
                        ["জ", "j"],
                        ["ঝ", "jh"],
                        ["ট", "ṭ"],
                        ["ঠ", "ṭh"],
                        ["ড", "ḍ"],
                        ["ঢ", "ḍh"],
                        ["ণ", "ṇ"],
                        ["ত", "t"],
                        ["থ", "th"],
                        ["দ", "d"],
                        ["ধ", "dh"],
                        ["ন", "n"],
                        ["প", "p"],
                        ["ফ", "ph"],
                        ["ব", "b"],
                        ["ভ", "bh"],
                        ["ম", "m"],
                        ["য", "j"],
                        ["র", "r"],
                        ["ল", "l"],
                        ["শ", "sh"],
                        ["ষ", "sh"],
                        ["স", "s"],
                        ["হ", "h"],
                    ],
                },
                {
                    "heading": "Example sentences using the alphabet",
                    "headers": H,
                    "speakCol": S,
                    "rows": [
                        r("Welcome", "স্বাগতম", "Swāgotom"),
                        r("Thank you", "ধন্যবাদ", "Dhonyobād"),
                        r("Hello (formal)", "নমস্কার", "Nômôskār"),
                        r("How are you?", "আপনি কেমন আছেন?", "Āpni kēmon āchen?"),
                        r("I am fine", "আমি ভালো আছি", "Āmi bhālō āchi"),
                        r("What is your name?", "আপনার নাম কী?", "Āpār nām ki?"),
                        r("My name is...", "আমার নাম...", "Āmār nām..."),
                        r("Yes", "হ্যাঁ", "Hyẫ"),
                        r("No", "না", "Nā"),
                        r("Please", "দয়া করে", "Dôya kōre"),
                        r("I love you", "আমি তোমাকে ভালোবাসি", "Āmi tōmākē bhālōbāsi"),
                        r("Goodbye", "বিদায়", "Bidāy"),
                        r("Good morning", "সুপ্রভাত", "Suprobhāt"),
                        r("Good night", "শুভ রাত্রি", "Shubh rātri"),
                        r("Help!", "সাহায্য করুন!", "Sāhājjo kôrun!"),
                    ],
                },
            ],
        )
    )

    # ----- 502 -----
    out.append(
        ch(
            502,
            "Vowels, Consonants in Bengali and their pronunciation",
            "Pronunciation of Bengali vowels and consonants. Modern Bengali often does not distinguish short vs long ই/ঈ and উ/ঊ in speech.",
            "Each letter maps to fairly consistent sounds. Nasalization (ঁ, ং) is common. Practice with the speaker.",
            blocks=[
                blk_para(
                    "Vowel pronunciation",
                    "Front vowels: ই, ঈ. Central: অ, আ. Back: উ, ঊ, ও, ও. Diphthongs: ঐ, ঔ. In Sanskrit loans, spelling may differ from colloquial pronunciation.",
                ),
                block_table(
                    "Sentence examples – vowels in use",
                    [
                        r("I am fine", "আমি ভালো আছি", "Āmi bhālō āchi"),
                        r("How are you?", "তুমি কেমন আছো?", "Tumi kēmon āchho?"),
                        r("My name is...", "আমার নাম...", "Āmār nām..."),
                        r("Thank you", "ধন্যবাদ", "Dhonyobād"),
                        r("I am a student", "আমি ছাত্র", "Āmi chātrô"),
                        r("You are a teacher", "তুমি শিক্ষক", "Tumi shikkhôk"),
                        r("This is my book", "এটা আমার বই", "Ēṭā āmār bôi"),
                        r("This is my friend", "এই আমার বন্ধু", "Ei āmār bondhu"),
                        r("We are happy", "আমরা খুশি", "Āmrā khushi"),
                        r("She is beautiful", "সে সুন্দর", "Sē sundor"),
                        r("He was brave", "সে সাহসী ছিল", "Sē sāhsī chhil"),
                        r("I'm so happy", "আমি খুব খুশি", "Āmi khub khushi"),
                        r("Good idea", "ভালো ধারণা", "Bhālō dhārôṇā"),
                        r("Very good", "খুব ভালো", "Khub bhālō"),
                        r("Well done", "খুব ভালো হয়েছে", "Khub bhālō hōyēchhe"),
                    ],
                ),
                block_table(
                    "Consonant pronunciation notes",
                    [
                        r("Come in", "ভিতরে আসুন", "Bhitōre āsun"),
                        r("Please come in", "দয়া করে ভিতরে আসুন", "Dôya kōre bhitōre āsun"),
                        r("Can you help me?", "আপনি কি আমাকে সাহায্য করতে পারবেন?", "Āpni ki āmākē sāhājjo kôrte pārben?"),
                        r("Have you eaten?", "খেয়েছেন?", "Khēyēchen?"),
                        r("I'm hungry", "আমার খিদে পেয়েছে", "Āmār khidē pēyēchhe"),
                        r("Take care", "যত্ন নিন", "Jôtno nin"),
                        r("I miss you", "আমি তোমাকে মিস করি", "Āmi tōmākē mis kori"),
                        r("No problem", "কোনো সমস্যা নেই", "Kōnō shomosshā nēi"),
                        r("Get well soon", "আশা করি তাড়াতাড়ি সুস্থ হবেন", "Āshā kori ṭāṛāṭāṛi sustho hōben"),
                        r("No worries", "চিন্তা নেই", "Chinta nēi"),
                        r("Congratulations", "অভিনন্দন", "Ôbhinondon"),
                        r("Good luck", "শুভকামনা", "Shubhokāmnā"),
                        r("See you", "আবার দেখা হবে", "Ābār dēkhā hōbe"),
                        r("I'm sorry", "আমি দুঃখিত", "Āmi duhkhito"),
                        r("That is a good idea", "সেটা ভালো ধারণা", "Sēṭā bhālō dhārôṇā"),
                    ],
                ),
            ],
        )
    )

    # ----- 503 Barakhadi / kars -----
    out.append(
        ch(
            503,
            "Bengali Barakhadi: vowel signs (কার) with consonants",
            "How vowels combine with consonants in Bangla. The inherent vowel is ô; other vowels use kār (া, ি, ী, etc.).",
            "ক + া = কা (kā); ক + ই = কি (ki); ক + ই = কি; ক + ু = কু (ku); ক + ূ = কু; ক + ে = কে (ke); ক + ৈ = কৈ (koi); ক + ো = কো (ko); ক + ৌ = কৌ (kou).",
            blocks=[
                blk_para(
                    "Matra examples",
                    "Same pattern applies to other consonants. হসন্ত (্) removes the inherent vowel for consonant clusters (যুক্তাক্ষর).",
                ),
                block_table(
                    "Words and sentences using vowel signs",
                    [
                        r("What is your name?", "আপনার নাম কী?", "Āpār nām ki?"),
                        r("My name is...", "আমার নাম...", "Āmār nām..."),
                        r("I don't understand", "আমি বুঝতে পারছি না", "Āmi bujhte pārchhi nā"),
                        r("Please speak slowly", "আস্তে আস্তে বলুন", "Āste āste bôlun"),
                        r("Please say that again", "আবার বলবেন?", "Ābār bôlben?"),
                        r("Please write it down", "এটা লিখে দিন", "Ēṭā likhe din"),
                        r("Do you speak Bengali?", "আপনি কি বাংলা বলতে পারেন?", "Āpni ki bāṅlā bolte pāren?"),
                        r("Yes, a little", "হ্যাঁ, একটু", "Hyẫ, ekṭu"),
                        r("Speak to me in Bengali", "আমার সঙ্গে বাংলায় কথা বলুন", "Āmār songe bāṅlāy kōthā bôlun"),
                        r("How do you say ... in Bengali?", "... বাংলায় কী বলে?", "... bāṅlāy ki bōle?"),
                        r("Excuse me", "মাফ করবেন", "Māph kôrben"),
                        r("How much is this?", "এটার দাম কত?", "Ēṭār dām kôt?"),
                        r("Sorry", "দুঃখিত", "Duhkhito"),
                        r("Thank you", "ধন্যবাদ", "Dhonyobād"),
                        r("You're welcome", "স্বাগতম", "Swāgotom"),
                    ],
                ),
            ],
        )
    )

    # ----- 504–509 script -----
    out.append(
        ch(
            504,
            "Frequently faced pronunciation problems in Bengali (Bangla script)",
            "Common pitfalls: অ vs আ, ই/ঈ merge, স/শ/ষ, ন/ণ, ড/দ.",
            "Learners familiar with Hindi may notice differences in vowel quality and conjuncts.",
            blocks=[
                blk_para(
                    "Tips",
                    "Aspiration matters: ক vs খ, গ vs ঘ. Retroflex ট ঠ ড ঢ differs from dental ত থ দ ধ.",
                ),
                block_table(
                    "Practice sentences",
                    [
                        r("I'm sorry", "আমি দুঃখিত", "Āmi duhkhito"),
                        r("I'm so sorry", "আমি খুব দুঃখিত", "Āmi khub duhkhito"),
                        r("I don't understand", "আমি বুঝতে পারছি না", "Āmi bujhte pārchhi nā"),
                        r("Please speak more slowly", "আরও আস্তে বলুন", "Ārō āste bôlun"),
                        r("Please say that again", "আবার বলবেন", "Ābār bôlben"),
                        r("Do you speak English?", "আপনি কি ইংরেজি বলেন?", "Āpni ki iṅrejī bôlen?"),
                        r("Is there someone who speaks English?", "কেউ কি ইংরেজি বলে?", "Keu ki iṅrejī bōle?"),
                        r("Help!", "সাহায্য করুন!", "Sāhājjo kôrun!"),
                        r("Look out!", "সাবধান!", "Sābdhān!"),
                        r("Good morning", "সুপ্রভাত", "Suprobhāt"),
                        r("Good evening", "শুভ সন্ধ্যা", "Shubh sondhyā"),
                        r("Good night", "শুভ রাত্রি", "Shubh rātri"),
                        r("Where is the toilet?", "টয়লেট কোথায়?", "Ōyaleṭ kōthāy?"),
                        r("I'm lost", "আমি পথ হারিয়েছি", "Āmi poth hāriēchhi"),
                        r("Leave me alone", "আমাকে একা থাকতে দিন", "Āmākē ekā thākte din"),
                    ],
                ),
            ],
        )
    )

    out.append(
        ch(
            505,
            "Pronunciation of Anusvara (ং) and related symbols in Bengali",
            "ং (anusvara) nasalizes or represents a nasal consonant. ঃ (visarga) is rare in Bengali. ঁ (chandrabindu) nasalizes vowels.",
            "অনুস্বার (ং) often sounds like ঙ or ন depending on the following consonant.",
            blocks=[
                block_table(
                    "Words and sentences with ং / ঁ",
                    [
                        r("Bengal", "বাংলা", "Bāṅlā"),
                        r("language", "ভাষা", "bhāṣā"),
                        r("today", "আজ", "āj"),
                        r("morning", "সকাল", "sākāl"),
                        r("evening", "সন্ধ্যা", "sondhyā"),
                        r("night", "রাত", "rāt"),
                        r("Good morning", "সুপ্রভাত", "Suprobhāt"),
                        r("Good night", "শুভ রাত্রি", "Shubh rātri"),
                        r("I will stay one night", "আমি এক রাত থাকব", "Āmi ek rāt thākbo"),
                        r("What time is breakfast?", "নাস্তা কখন?", "Nāstā kôkhon?"),
                        r("minute", "মিনিট", "miniṭ"),
                        r("hour", "ঘণ্টা", "ghôṇṭā"),
                        r("month", "মাস", "mās"),
                        r("year", "বছর", "bôchhor"),
                        r("Long time no see", "দেখা হয়নি অনেক দিন", "Dēkhā hōyni ônek din"),
                    ],
                ),
            ],
        )
    )

    out.append(
        ch(
            506,
            "Combining consonants in Bengali (যুক্তাক্ষর)",
            "Consonant clusters use হসন্ত (্) to join letters: ক্ + ত = ক্ত (kto).",
            "যুক্তাক্ষর is common in Sanskrit and English loanwords.",
            blocks=[
                block_table(
                    "Sentences using consonant combinations",
                    [
                        r("Stop!", "থামুন!", "Thāmun!"),
                        r("Call the police!", "পুলিশ ডাকুন!", "Pulish ḍākun!"),
                        r("Police!", "পুলিশ!", "Pulish!"),
                        r("Stop! Thief!", "থামুন! চোর!", "Thāmun! chōr!"),
                        r("I need your help", "আমার আপনার সাহায্য দরকার", "Āmār āpār sāhājjo dôrkār"),
                        r("It's an emergency", "এটা জরুরি", "Ēṭā joruri"),
                        r("I lost my bag", "আমার ব্যাগ হারিয়ে গেছে", "Āmār bēg hāriē gēchhe"),
                        r("I'm sick", "আমি অসুস্থ", "Āmi ôsustho"),
                        r("I've been injured", "আমি আঘাত পেয়েছি", "Āmi āghāt pēyēchhi"),
                        r("I need a doctor", "আমার ডাক্তার দরকার", "Āmār ḍāktār dôrkār"),
                        r("Can I use your phone?", "আমি কি আপনার ফোন ব্যবহার করতে পারি?", "Āmi ki āpār phōn bôbohār kôrte pāri?"),
                        r("I haven't done anything wrong", "আমি কিছু ভুল করিনি", "Āmi kichhu bhul korini"),
                        r("It was a misunderstanding", "ভুল বোঝাবুঝি ছিল", "Bhul bōjhābūjhī chhil"),
                        r("I want to talk to a lawyer", "আমি একজন আইনজীবীর সঙ্গে কথা বলতে চাই", "Āmi ekjon āinjībīr songe kōthā bolte chāi"),
                        r("Fire!", "আগুন!", "Āgun!"),
                    ],
                ),
            ],
        )
    )

    out.append(
        ch(
            507,
            "Combining consonants with র (r) – Bengali যুক্তাক্ষর Part 2",
            "র can appear as রেফ (reph) before a consonant or in clusters like প্র, ক্র, স্ত.",
            "Practice reading words with র in the middle or end.",
            blocks=[
                block_table(
                    "Sentences with র clusters",
                    [
                        r("problem", "সমস্যা", "shomosshā"),
                        r("country", "দেশ", "dēsh"),
                        r("first", "প্রথম", "prôthom"),
                        r("question", "প্রশ্ন", "prôshno"),
                        r("I will try", "আমি চেষ্টা করব", "Āmi chēṣṭā korbo"),
                        r("Please read", "পড়ুন", "Pōṛun"),
                        r("Write clearly", "পরিষ্কার লিখুন", "Pôriskār likhun"),
                        r("Practice daily", "প্রতিদিন অনুশীলন করুন", "Prôtidin ônushīlon kôrun"),
                        r("Respect everyone", "সবাইকে সম্মান করুন", "Sobāikē shommān kôrun"),
                        r("Learn Bengali", "বাংলা শিখুন", "Bāṅlā shikhun"),
                        r("Good progress", "ভালো অগ্রগতি", "Bhālō ôgrogoti"),
                        r("Keep going", "চালিয়ে যান", "Chāliē jān"),
                        r("Don't give up", "হার মানবেন না", "Hār mānben nā"),
                        r("Well done", "খুব ভালো", "Khub bhālō"),
                        r("Thank you", "ধন্যবাদ", "Dhonyobād"),
                    ],
                ),
            ],
        )
    )

    out.append(
        ch(
            508,
            "Combining consonants with হ (h) – Bengali যুক্তাক্ষর Part 3",
            "হ combines as in ক্ষ (kh), ম্হ (mha), or in ঠ + হ.",
            "হ is common in Bengali grammar words.",
            blocks=[
                block_table(
                    "Words with হ",
                    [
                        r("today", "আজ", "āj"),
                        r("happiness", "খুশি", "khushi"),
                        r("laughter", "হাসি", "hāsi"),
                        r("hand", "হাত", "hāt"),
                        r("day after tomorrow", "পরশু", "pôrshu"),
                        r("I am fine", "আমি ভালো আছি", "Āmi bhālō āchi"),
                        r("How are you?", "কেমন আছেন?", "Kēmon āchen?"),
                        r("I am learning", "আমি শিখছি", "Āmi shikhchhi"),
                        r("Speak slowly", "আস্তে বলুন", "Āste bôlun"),
                        r("This is hard", "এটা কঠিন", "Ēṭā kôṭhin"),
                        r("Help me", "সাহায্য করুন", "Sāhājjo kôrun"),
                        r("Have patience", "ধৈর্য ধরুন", "Dhôirjyo dhôrun"),
                        r("Good habit", "ভালো অভ্যাস", "Bhālō ôbhyās"),
                        r("Practice", "অনুশীলন", "Ônushīlon"),
                        r("Success", "সাফল্য", "Sāpholyo"),
                    ],
                ),
            ],
        )
    )

    out.append(
        ch(
            509,
            "Special or separate symbols for combined consonants in Bengali",
            "Some ligatures have special shapes: ক্ষ, জ্ঞ, দ্র, etc.",
            "These appear in many Sanskrit and formal words.",
            blocks=[
                block_table(
                    "Words with special conjuncts",
                    [
                        r("student", "ছাত্র", "chātrô"),
                        r("knowledge", "জ্ঞান", "gyān"),
                        r("country", "দেশ", "dēsh"),
                        r("difficult", "কঠিন", "kôṭhin"),
                        r("question", "প্রশ্ন", "prôshno"),
                        r("answer", "উত্তর", "uttor"),
                        r("read a book", "বই পড়া", "Bôi pōṛā"),
                        r("write clearly", "পরিষ্কার লেখা", "Pôriskār lēkhā"),
                        r("I study Bengali", "আমি বাংলা পড়ি", "Āmi bāṅlā pōṛi"),
                        r("Good teacher", "ভালো শিক্ষক", "Bhālō shikkhôk"),
                        r("School", "স্কুল", "sḳul"),
                        r("University", "বিশ্ববিদ্যালয়", "bishbôbidyālôy"),
                        r("Library", "গ্রন্থাগার", "grônthāgār"),
                        r("Homework", "বাড়ির কাজ", "bāṛir kāj"),
                        r("Exam", "পরীক্ষা", "porīkkhā"),
                    ],
                ),
            ],
        )
    )

    # Placeholder: append remaining chapters from supplemental module
    from build_assamese_data_part2 import add_grammar_phrases_vocab_conv

    add_grammar_phrases_vocab_conv(out)

    out.sort(key=lambda x: x["id"])

    with open("data_assamese.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print("Wrote data_assamese.json with", len(out), "chapters")


if __name__ == "__main__":
    main()
