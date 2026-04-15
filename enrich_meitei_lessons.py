#!/usr/bin/env python3
import json
import re
from pathlib import Path


BASE = Path(__file__).parent.resolve()


def para(heading, content):
    return {"type": "paragraph", "heading": heading, "content": content}


def table(heading, headers, rows, speak_col=None):
    out = {"type": "table", "heading": heading, "headers": headers, "rows": rows}
    if speak_col is not None:
        out["speakCol"] = speak_col
    return out


structure = json.loads((BASE / "lessons_structure_meitei.json").read_text(encoding="utf-8"))
data = json.loads((BASE / "data_meitei.json").read_text(encoding="utf-8"))
cache = json.loads((BASE / "meitei_translate_cache.json").read_text(encoding="utf-8"))

section_by_id = {}
for major in structure["majorLessons"]:
    for sub in major["sublessons"]:
        section_by_id[sub["chapterId"]] = major["name"]


def cache_mayek(english):
    entry = cache.get(english)
    return entry["mayek"] if entry else ""


def row_en_mei(english):
    return [english, cache_mayek(english)]


def short_title(title):
    title = re.sub(r" in Meitei \(Manipuri\)", "", title)
    return re.sub(r"\s+", " ", title).strip(" .")


def grammar_topic(title):
    t = title.lower()
    if "pronouns and articles" in t:
        return "pronouns"
    if "plurals to indicate respect" in t:
        return "honorific_plural"
    if "verbs in meitei" in t:
        return "verbs"
    if 'simple present tense of "to be"' in t:
        return "present_be"
    if "present continuous" in t:
        return "present_continuous"
    if "future continuous" in t:
        return "future_continuous"
    if "past continuous" in t:
        return "past_continuous"
    if "simple present tense" in t:
        return "simple_present"
    if "simple future tense" in t:
        return "simple_future"
    if "simple past tense" in t:
        return "simple_past"
    if "perfect continuous" in t:
        return "perfect_continuous"
    if "perfect tense" in t:
        return "perfect"
    if 'preposition "to"' in t:
        return "postposition_to"
    if "prepositions with similar" in t:
        return "postposition_pairs"
    if "learn prepositions" in t or "working with nouns – prepositions" in t:
        return "postpositions"
    if "sentences with person or living things as object" in t:
        return "animate_object"
    if "saying my/his/her" in t:
        return "possession"
    if "basic questions" in t:
        return "questions"
    if "negative sentences" in t or "negative sentence" in t:
        return "negative"
    if "gender & plurals" in t:
        return "gender_plural"
    if "cases in meitei" in t:
        return "cases"
    if "commands / imperative" in t:
        return "imperative"
    if "time related words" in t:
        return "time_words"
    if "causative" in t or "cause of action" in t:
        return "causative"
    return "grammar_general"


def pattern_topic(title):
    t = title.lower()
    mapping = [
        ("going to", "going_to"),
        ("used to", "used_to"),
        ("if-then", "if_then"),
        ("adjectives in", "adjectives"),
        ("can/to be able to", "can"),
        ("to want/to need", "want_need"),
        ("to become/to happen", "become_happen"),
        ('using "should"', "should"),
        ('using "must"', "must"),
        ("to keep doing", "keep_doing"),
        ("degrees of comparison", "comparison"),
        ('using verb "to know"', "know"),
        ('using "let" and "shall we"', "shall_we"),
        ("giving instructions formally", "formal_instruction"),
        ('using "to like"', "like"),
        ("would", "would"),
        ('"to understand" & "to come to know"', "understand"),
        ("question tag", "question_tag"),
        ('using verb "to remember"', "remember"),
        ("supposed to", "supposed_to"),
        ("short forms", "short_forms"),
        ("greeting, wishes, blessings", "greetings"),
        ("compound verbs / phrases", "compound_phrases"),
        ("calling or addressing", "addressing"),
        ("exclamations", "exclamations"),
        ("may i", "requests"),
        ("may, might", "may_might"),
        ("adjectives made from verb", "verbal_adjectives"),
        ("adjectives related to prepositions", "relational_adjectives"),
        ("using may to express wish", "wish_may"),
        ("to make someone do something", "causative_phrase"),
        ("generalizing words", "generalizers"),
        ('"to have" to indicate possession', "have_possession"),
        ('using "to mean"', "meaning"),
        ("conjunctions", "conjunctions"),
        ("combining sentences", "combining_sentences"),
        ("active passive voice", "voice"),
        ('using "to feel" & "to think"', "feel_think"),
        ("idioms and phrases", "idioms"),
    ]
    for key, value in mapping:
        if key in t:
            return value
    return "pattern_general"


def build_grammar(title):
    label = short_title(title)
    topic = grammar_topic(title)
    content = f"Meitei (Manipuri) grammar lesson on {label}."

    if topic == "pronouns":
        intro = (
            'Meitei uses a verb-final sentence order, and pronouns often change according '
            'to politeness or honorific level. Unlike English, it does not rely on true articles like "a" and "the".'
        )
        blocks = [
            para(
                "Key idea",
                "Start by learning the core pronouns and noticing where they appear before the verb. "
                "In Meitei, sentence structure is easiest to follow when you first identify the subject and then look at the final verb.",
            ),
            table(
                "Starter pronouns",
                ["English", "Meitei Mayek"],
                [
                    row_en_mei("I"),
                    row_en_mei("You (respectful)"),
                    row_en_mei("He / She"),
                    row_en_mei("We"),
                    row_en_mei("They"),
                    row_en_mei("This"),
                    row_en_mei("That"),
                ],
                1,
            ),
            para(
                "Study focus",
                "Because articles are not a central grammatical category in Meitei, learners should spend more time on pronoun choice, "
                "honorific usage, and natural word order than on translating English article patterns directly.",
            ),
        ]
        return content, intro, blocks

    if topic == "honorific_plural":
        intro = "Respect in Meitei is shown through pronoun choice, polite verb forms, and plural-style respectful reference, especially for human referents."
        blocks = [
            para(
                "Key idea",
                "Do not treat plural marking as only a number feature. In Meitei, respectful reference can overlap with plural-style expression, so social meaning matters as much as grammar.",
            ),
            table(
                "Human plural and respect markers",
                ["Marker", "Typical use"],
                [
                    ["-sing", "Plural marking with human nouns"],
                    ["honorific pronouns", "Respectful address or reference"],
                    ["polite verb choice", "Softens commands and requests"],
                ],
            ),
            para(
                "Practice focus",
                'Take one sentence such as "you come" or "they are here" and recast it in neutral, friendly, and respectful ways. '
                "This helps you hear how grammar and social tone work together.",
            ),
        ]
        return content, intro, blocks

    if topic == "verbs":
        intro = "Meitei is largely agglutinative, so verb meaning is built through suffixes and small grammatical elements added near the end of the clause."
        blocks = [
            para(
                "How verbs behave",
                "The verb usually comes at the end of the sentence. As you learn new forms, watch how tense, aspect, negation, and politeness are layered onto the verb stem rather than expressed as separate helper words.",
            ),
            para(
                "What to notice",
                "Meitei often gives more weight to aspect and completion than a simple one-to-one English tense match. Learn each verb form as part of a sentence pattern instead of memorising isolated labels only.",
            ),
            para(
                "Practice focus",
                "Pick one verb and build a small ladder: plain statement, negative, question, polite version, and past or future version. "
                "This is the fastest way to understand how suffixing works.",
            ),
        ]
        return content, intro, blocks

    if topic in {
        "simple_present",
        "simple_future",
        "simple_past",
        "present_continuous",
        "future_continuous",
        "past_continuous",
        "perfect",
        "perfect_continuous",
        "present_be",
    }:
        aspect_note = {
            "simple_present": "Use this lesson to separate habitual meaning from immediate ongoing action. Many learner mistakes come from mapping English present forms too directly.",
            "simple_future": "Future meaning in Meitei often interacts with intention, prediction, and context, so practise it in full sentences rather than as a single ending list.",
            "simple_past": "Past reference is easiest to learn when you compare completed events, background narration, and object-marked vs non-object-marked clauses.",
            "present_continuous": "Continuous forms are especially useful in daily conversation because they let you describe what is happening right now or around the current time.",
            "future_continuous": "Future continuous patterns are helpful for planned ongoing events, expectations, and polite discussion of what someone will be doing later.",
            "past_continuous": "Past continuous forms help describe background action, interrupted events, and scenes in stories.",
            "perfect": "Perfect-style meaning often overlaps with completion, result, and relevance to the present moment, so compare it carefully with plain past sentences.",
            "perfect_continuous": "This pattern is most useful when you want to highlight both duration and continuity, especially across time expressions.",
            "present_be": 'Treat the "to be" lesson as a lesson about existence, identity, and location rather than a direct copy of English copula rules.',
        }[topic]
        intro = "Meitei is verb-final, so tense and aspect cues gather near the end of the sentence. Learn the whole sentence frame, not only the ending."
        blocks = [
            para("Key idea", aspect_note),
            para(
                "What to compare",
                "Build a contrast set with the same subject and verb: statement, negative, yes-no question, and respectful form. "
                "Seeing the same core meaning in several frames makes the tense or aspect pattern easier to retain.",
            ),
            para(
                "Practice focus",
                "Add a time word such as today, yesterday, now, or tomorrow while practising. Meitei tense and aspect become clearer when a time reference is present.",
            ),
        ]
        return content, intro, blocks

    if topic in {"postpositions", "postposition_to", "postposition_pairs"}:
        intro = "Meitei uses postpositions and case suffixes, so relational meaning usually follows the noun instead of coming before it as in English prepositions."
        blocks = [
            para(
                "Key idea",
                "When you see an English preposition, first ask whether Meitei would express that meaning by a case suffix, a postposition, or the wider clause context. "
                "A direct word-for-word replacement is often misleading.",
            ),
            table(
                "Common relational markers",
                ["Marker", "Typical function"],
                [
                    ["-gi", "Genitive / belonging"],
                    ["-da", "Dative or locative / to, at, in"],
                    ["-bu", "Object / accusative"],
                    ["-dagi", "From / ablative"],
                    ["-na", "Agentive or instrumental in many contexts"],
                ],
            ),
            para(
                "Practice focus",
                "Take one noun and attach different markers to see how the meaning changes: at the house, from the house, to the person, with the person, and so on.",
            ),
        ]
        return content, intro, blocks

    if topic == "animate_object":
        intro = "Human and animate objects are often marked more clearly than inanimate ones, so object marking deserves separate attention in Meitei sentence building."
        blocks = [
            para(
                "Key idea",
                "When the object is a person or another living being, clarity and naturalness often depend on using the expected marker rather than copying a bare English order.",
            ),
            para(
                "What to notice",
                "Listen for how the object phrase sits between the subject and the final verb. This lesson becomes easier if you practise with family words, names, and everyday actions.",
            ),
            para(
                "Practice focus",
                'Make short pairs such as "I saw the child" and "I saw the house" so you can compare animate and inanimate object behaviour.',
            ),
        ]
        return content, intro, blocks

    if topic == "possession":
        intro = "Possession in Meitei is usually built through relational marking rather than by copying English standalone possessive adjectives."
        blocks = [
            para(
                "Key idea",
                "Learn possession as a noun-linking pattern: the possessor, the marker, and the possessed noun. This is more useful than memorising isolated equivalents of my, his, and her.",
            ),
            para(
                "What to compare",
                "Practise with family relations, objects, and body parts. Possession can also interact with social meaning and emphasis, especially in everyday speech.",
            ),
            para(
                "Practice focus",
                "Make a small grid: my book, your house, his name, our food, their country. Then say each one inside a complete sentence.",
            ),
        ]
        return content, intro, blocks

    if topic == "questions":
        intro = "Question building in Meitei depends on word order, particles, and the position of interrogative words inside a verb-final sentence frame."
        blocks = [
            para(
                "Key idea",
                "Separate yes-no questions from WH-questions. In a verb-final language, the learner should follow the whole clause all the way to the end before deciding the sentence type.",
            ),
            para(
                "What to notice",
                "Pay attention to where question words sit, how polite questioning sounds, and how the final part of the sentence signals that the speaker is asking rather than stating.",
            ),
            para(
                "Practice focus",
                "Turn five basic statements into questions. Then answer them in short and full forms so the question pattern becomes active, not just recognisable.",
            ),
        ]
        return content, intro, blocks

    if topic == "negative":
        intro = "Negation in Meitei is best learned as part of the verb system, because the negative shape of a sentence is often built near the end of the clause."
        blocks = [
            para(
                "Key idea",
                "Do not learn negative sentences as one universal word added anywhere in the clause. In Meitei, tense, aspect, and negation interact, so each frame needs practice.",
            ),
            para(
                "What to compare",
                "Place the affirmative and negative versions side by side: present, past, and future. This shows which part changes and which part stays stable.",
            ),
            para(
                "Practice focus",
                "Use high-frequency meanings first: know, want, come, go, understand, like, and have. Negation becomes natural faster with everyday verbs.",
            ),
        ]
        return content, intro, blocks

    if topic == "gender_plural":
        intro = "Meitei does not treat grammatical gender the same way many Indo-Aryan languages do, and plural marking is especially clear with human nouns."
        blocks = [
            para(
                "Key idea",
                "Start from the fact that general noun classification is lighter in Meitei. Human plurality is commonly marked with -sing, while gender is often optional or expressed lexically when needed.",
            ),
            table(
                "Useful noun facts",
                ["Feature", "Observation"],
                [
                    ["gender", "No broad grammatical gender system like Hindi or Marathi"],
                    ["human plural", "Often marked with -sing"],
                    ["non-human plurality", "Often shown by quantity words or context"],
                    ["honorific reference", "Social meaning can override simple number logic"],
                ],
            ),
            para(
                "Practice focus",
                "Compare one person, many people, one animal, many animals, and one object, many objects. This prevents overusing one plural strategy everywhere.",
            ),
        ]
        return content, intro, blocks

    if topic == "cases":
        intro = "Case suffixes are one of the clearest gateways into Meitei sentence structure because they show how nouns relate to the verb and to each other."
        blocks = [
            table(
                "Core case markers",
                ["Marker", "Common meaning"],
                [
                    ["-na", "Agentive or nominative-like in many clauses"],
                    ["-gi", "Genitive / of"],
                    ["-da", "Locative or dative / at, in, to"],
                    ["-bu", "Object marker"],
                    ["-dagi", "From / ablative"],
                ],
            ),
            para(
                "How to study them",
                "Learn each marker with a short noun phrase first, then place that phrase inside a full sentence. This keeps the case meaning tied to real usage rather than abstract charts only.",
            ),
            para(
                "Practice focus",
                "Build mini-sets such as child, child-of, to the child, from the child, child-object. The visual pattern of the suffixes is easier to remember when grouped this way.",
            ),
        ]
        return content, intro, blocks

    if topic == "imperative":
        intro = "Imperatives in Meitei range from direct orders to polite requests, so tone and social distance matter as much as the verb itself."
        blocks = [
            para(
                "Key idea",
                "Learn commands in pairs: direct and polite. A form that is grammatically correct may still sound too sharp in the wrong social setting.",
            ),
            para(
                "What to notice",
                "Requests often overlap with imperative meaning, especially in service situations, family speech, and classroom language. Practise softening strategies early.",
            ),
            para(
                "Practice focus",
                "Use common verbs such as come, sit, listen, speak, wait, and write. Say each as an instruction to a friend and again as a respectful request.",
            ),
        ]
        return content, intro, blocks

    if topic == "time_words":
        intro = "Time expressions help anchor tense and aspect, so this lesson is useful across the whole grammar course."
        blocks = [
            table(
                "Basic time words from the starter pack",
                ["English", "Meitei Mayek"],
                [
                    row_en_mei("Today"),
                    row_en_mei("Morning"),
                    row_en_mei("Evening"),
                    row_en_mei("Night"),
                    row_en_mei("Minute"),
                    row_en_mei("Hour"),
                    row_en_mei("Month"),
                    row_en_mei("Year"),
                ],
                1,
            ),
            para(
                "How to use them",
                "Place time words early in the sentence while keeping the verb at the end. This is one of the easiest ways to make tense practice feel concrete.",
            ),
            para(
                "Practice focus",
                "Make present, past, and future examples with the same verb and only change the time phrase. This shows how meaning shifts without changing the whole sentence.",
            ),
        ]
        return content, intro, blocks

    if topic == "causative":
        intro = "Causative meaning in Meitei lets you show that one person causes, allows, or gets another person to do something."
        blocks = [
            para(
                "Key idea",
                "Keep track of the participants carefully: who performs the action, who causes it, and who is affected. This lesson is really about argument structure, not only a single suffix.",
            ),
            para(
                "What to compare",
                "Start with a simple verb such as eat, sit, or read, and compare the plain form with a caused version. The semantic difference becomes clearer than memorising a definition.",
            ),
            para(
                "Practice focus",
                "Use family or classroom situations first, because causative meaning appears naturally in sentences like make someone sit, ask someone to read, or have someone bring something.",
            ),
        ]
        return content, intro, blocks

    intro = "This lesson belongs to the Meitei grammar track. Use it to connect a specific form with wider verb-final sentence structure, case marking, and natural spoken usage."
    blocks = [
        para(
            "Overview",
            "Approach this topic through complete examples rather than isolated labels. In Meitei, grammar patterns become easier when you watch how the final verb and noun markers interact.",
        ),
        para(
            "What to notice",
            "Check whether the lesson mainly changes the verb ending, the noun marking, the information order, or the politeness level. That tells you where to focus your attention.",
        ),
        para(
            "Practice focus",
            "Build three short examples from daily life and say them aloud. Then change one piece at a time so you can hear what the target pattern actually controls.",
        ),
    ]
    return content, intro, blocks


def build_pattern(title):
    label = short_title(title)
    topic = pattern_topic(title)
    content = f"Meitei (Manipuri) sentence-pattern lesson on {label}."
    intros = {
        "going_to": "This lesson focuses on intention and near-future planning in Meitei.",
        "used_to": "This lesson focuses on habitual past meaning and contrast between old habits and present reality.",
        "if_then": "Conditional patterns in Meitei become clearer when you practise whole clause pairs rather than isolated words.",
        "adjectives": "Adjectives in Meitei are best learned in natural noun phrases and short descriptive sentences.",
        "can": "Ability and possibility patterns are common in daily conversation, so this lesson should stay practical and sentence-based.",
        "want_need": "Want and need patterns often interact with person, politeness, and whether another verb follows.",
        "become_happen": "This lesson covers change-of-state and event meaning, which are essential for natural narration.",
        "should": "Advice language works best when you compare neutral suggestion, stronger recommendation, and polite guidance.",
        "must": "Obligation in Meitei can sound very strong, so context and politeness are important.",
        "comparison": "Comparison structures help you move from basic meaning to more expressive daily speech.",
        "conjunctions": "Conjunctions show how Meitei connects ideas while keeping a verb-final structure.",
        "voice": "Voice-related patterns are easier if you start from active clauses and then observe how focus shifts.",
        "idioms": "Idioms are valuable because they show what sounds natural beyond dictionary-level meaning.",
    }
    intro = intros.get(
        topic,
        "This lesson builds a useful Meitei sentence pattern that becomes more natural through repeated whole-sentence practice.",
    )
    guides = {
        "going_to": "Use this pattern to talk about plans, intentions, and what someone is about to do. Practise with daily routines, travel plans, and decisions made in the moment.",
        "used_to": "Contrast old repeated behaviour with the present. Habitual past meaning becomes clearer when the same subject is shown in both time frames.",
        "if_then": "Separate the condition from the result and pay attention to how the listener waits for the final verb before fully processing the sentence.",
        "adjectives": "Move beyond one-word meanings and place adjectives inside noun phrases, statements, and comparisons.",
        "can": "Test the pattern across permission, ability, and practical possibility. These meanings overlap in English but do not always feel identical in real usage.",
        "want_need": "Notice whether the sentence ends with a bare desire, a necessity, or a desire to do another action. This changes the clause shape.",
        "become_happen": "These verbs are central in storytelling and reaction language. Use them to describe changes, accidents, and new situations.",
        "should": "Advice language should sound appropriate, not merely literal. Practise family, health, school, and travel situations.",
        "must": "Obligation language is often easiest to learn through rules, duties, and urgent practical needs.",
        "keep_doing": "This pattern is useful for repeated or continuing action, especially when talking about habits, effort, and ongoing behaviour.",
        "comparison": "Compare two people, two objects, and one thing against the whole group. That helps separate plain comparison from superlative meaning.",
        "know": "Knowledge verbs often split into knowing facts, knowing people, and coming to know something. Practise these meanings separately.",
        "shall_we": "Invitation and joint-action patterns become smoother when they sound collaborative instead of commanding.",
        "formal_instruction": "Formal instructions need clarity, politeness, and consistent sequencing, especially in classroom or public-service contexts.",
        "like": "Start with liking nouns, then move to liking activities and preferences between alternatives.",
        "would": "Would-patterns often overlap with habit, softness, preference, and hypothetical meaning. Learn them through example clusters.",
        "understand": "This lesson is useful for both learning conversations and real-life clarification. Practise it with positive, negative, and question forms.",
        "question_tag": "Question tags are not only grammar; they shape tone, expectation, and friendliness.",
        "remember": "Memory verbs are especially useful with people, places, promises, and things learned earlier.",
        "supposed_to": "This pattern often combines duty, expectation, and what is normally intended. Context determines which sense is strongest.",
        "short_forms": "Short forms matter because conversational Meitei often feels faster and more compact than textbook-style examples.",
        "greetings": "Greetings, wishes, and blessings are formulaic, so memorisation plus role-play works better than grammar-first study.",
        "compound_phrases": "Compound expressions help speech sound idiomatic. Learn them as fixed or semi-fixed chunks.",
        "addressing": "Forms of address depend on age, closeness, and respect. A correct word in the wrong relationship can still sound unnatural.",
        "exclamations": "Exclamations reveal emotion, surprise, irritation, or delight. Learn their tone, not only their literal meaning.",
        "requests": "May-I and can-you requests should be practised with politeness levels, because social fit matters greatly.",
        "may_might": "Uncertainty language is useful when you do not want to sound too direct or too certain.",
        "verbal_adjectives": "This pattern shows how action and description interact. It is a good bridge between verbs and modifiers.",
        "relational_adjectives": "These adjectives often describe position, relation, or context rather than a simple inherent quality.",
        "wish_may": "Wish expressions often sound formal or ceremonial, so practise them in blessings and polite greetings.",
        "causative_phrase": "Making someone do something requires tracking both the cause and the main action clearly.",
        "generalizers": "Generalizing words are useful because they let you speak naturally even when you do not know every specific noun.",
        "have_possession": "Possession and relation can be expressed in several ways, so compare literal ownership with family or part-whole relations.",
        "meaning": "Meaning questions are core survival language. Practise them with unknown words, signs, and expressions people say to you.",
        "conjunctions": "Group conjunctions by function: adding, contrasting, giving reason, showing condition, and sequencing events.",
        "combining_sentences": "Sentence-combining is a strong test of fluency because it forces you to manage clause order and the final verb carefully.",
        "voice": "Compare who performs the action, who receives it, and what the speaker wants to highlight.",
        "feel_think": "Thought and feeling verbs are essential in natural conversation because they soften statements and express personal stance.",
        "idioms": "Idioms should be learned with situation, tone, and rough meaning, not as literal word-by-word translation.",
    }
    blocks = [
        para("Key idea", guides.get(topic, "Study the pattern inside full everyday examples so that grammar and meaning stay connected.")),
        para(
            "What to notice",
            "Ask what the pattern contributes beyond the plain statement: time, condition, politeness, uncertainty, obligation, emphasis, or relationship between clauses.",
        ),
        para(
            "Practice focus",
            "Make three examples about your own life and three about an imagined situation. The contrast helps the pattern become flexible instead of memorised in one form only.",
        ),
    ]
    return content, intro, blocks


def build_vocab(title):
    label = short_title(title)
    t = title.lower()
    content = f"Meitei (Manipuri) vocabulary lesson on {label}."
    topic_line = "Organize the words by meaning, use, and likely conversation context rather than memorising one long list in isolation."
    if "numbers" in t or "fractional" in t or "percentage" in t:
        topic_line = "Number vocabulary becomes easier when practised in dates, prices, time, counting objects, and sequence words rather than as bare recitation."
    elif "verbs" in t:
        topic_line = "Verb vocabulary should be memorised together with a simple subject and object pattern so the word becomes usable immediately."
    elif "adjectives" in t or "adverbs" in t:
        topic_line = "Modifier words are best learned in pairs and opposites: fast or slow, big or small, early or late, near or far, and so on."
    elif any(k in t for k in ["body", "relations", "vegetable", "fruits", "birds", "insects", "colours", "flowers", "animals"]):
        topic_line = "Use this lesson to build semantic groups and quick recall. Topic-based vocabulary sticks better when you can picture the items together."
    intro = f"This vocabulary chapter covers {label.lower()}. {topic_line}"
    blocks = [
        para(
            "How to study the list",
            "Group new words into small batches, say them aloud, and then use each batch in one or two short sentences. Active recall matters more than rereading.",
        ),
        para(
            "What to notice",
            "Listen for repeated endings, sound patterns, and which words appear often in everyday talk. Those high-frequency items should be mastered first.",
        ),
        para(
            "Practice focus",
            "Turn the list into mini quizzes, picture naming, or category games. Vocabulary grows fastest when retrieval is timed and repeated over several short sessions.",
        ),
    ]
    return content, intro, blocks


def build_conversation(title):
    label = short_title(title)
    t = title.lower()
    content = f"Meitei (Manipuri) conversation practice for {label}."
    scenario = "Use this lesson as a role-play. Practise opening the interaction, asking for what you need, giving a short response, and closing politely."
    if "hotel" in t:
        scenario = "Focus on booking, room needs, timing, food, and simple problem-solving language used with staff."
    elif "doctor" in t:
        scenario = "Focus on symptoms, timing, instructions, medicine, and polite clarification when you do not understand."
    elif "bank" in t or "aadhar" in t or "interview" in t:
        scenario = "Focus on formal speech, personal details, requests, document-related questions, and confirmation checks."
    elif "traffic police" in t or "taxi" in t or "bus" in t or "address" in t or "tour guide" in t:
        scenario = "Focus on directions, destination, fares, clarification, and quick polite interaction with strangers."
    elif "teacher" in t or "students" in t or "language proficiency test" in t or "hobby class" in t:
        scenario = "Focus on question-answer turns, classroom language, explanation, and polite participation."
    elif "friends" in t or "football" in t or "movie" in t or "phone conversation" in t or "quarrel at home" in t:
        scenario = "Focus on natural back-and-forth speech, opinion, agreement, disagreement, and emotional tone."
    elif "grocery shop" in t or "vegetable market" in t or "food" in t or "lunch" in t:
        scenario = "Focus on buying, quantity, price, preference, and everyday transactional phrases."
    intro = f'This chapter uses the scenario "{label}" for practical Meitei conversation practice. {scenario}'
    blocks = [
        para(
            "Role-play structure",
            "Break the conversation into four parts: greeting, purpose, follow-up questions, and closing. Repeat each part until you can say it without pausing too much.",
        ),
        para(
            "What to notice",
            'Real conversation depends on repair language such as "please say that again", polite repetition, and short confirming responses. Keep those ready in every scenario.',
        ),
        para(
            "Practice focus",
            "Do the scene once as a textbook exchange, then repeat it with your own names, times, prices, places, or problems so the conversation becomes flexible and realistic.",
        ),
    ]
    return content, intro, blocks


new_data = []
for chapter in data:
    cid = chapter["id"]
    if cid <= 509:
        new_data.append(chapter)
        continue

    title = chapter["title"]
    section = section_by_id.get(cid, "")
    if "Sentence formation rules" in section:
        content, intro, blocks = build_grammar(title)
    elif "Phrases & other sentence structures" in section:
        content, intro, blocks = build_pattern(title)
    elif "Vocabulary" in section:
        content, intro, blocks = build_vocab(title)
    elif "Conversation practice" in section:
        content, intro, blocks = build_conversation(title)
    else:
        content = chapter.get("content", "")
        intro = chapter.get("intro", "")
        blocks = chapter.get("blocks", [])

    new_data.append(
        {
            "id": cid,
            "title": title,
            "url": "#",
            "content": content,
            "intro": intro,
            "blocks": blocks,
        }
    )

(BASE / "data_meitei.json").write_text(json.dumps(new_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Enriched Meitei lesson bodies for", len(new_data), "chapters")
