// ===== LANGUAGE SYSTEM =====
const CAT_INITIALS = { greetings:'Hi', reading:'Rd', writing:'Wr', numbers:'#', animals:'An', dailyLife:'DL', environment:'En', food:'Fd', health:'He', schoolWork:'Sw', socialInteractions:'So', time:'Ti', tourism:'To', transportation:'Tr', travel:'Go', shopping:'Sh', emergency:'!' };
// Real images for categories (Unsplash, free to use)
const CAT_IMAGES = {
  greetings: 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=80&h=80&fit=crop',
  travel: 'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=80&h=80&fit=crop',
  food: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=80&h=80&fit=crop',
  shopping: 'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=80&h=80&fit=crop',
  emergency: 'https://images.pexels.com/photos/263402/pexels-photo-263402.jpeg?auto=compress&cs=tinysrgb&w=80&h=80&fit=crop',
  numbers: 'https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=80&h=80&fit=crop',
  reading: 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=80&h=80&fit=crop',
  writing: 'https://images.unsplash.com/photo-1586281380349-632531db7ed4?w=80&h=80&fit=crop',
  animals: 'https://images.pexels.com/photos/1335971/pexels-photo-1335971.jpeg?auto=compress&cs=tinysrgb&w=80&h=80&fit=crop',
  dailyLife: 'https://images.unsplash.com/photo-1484101403633-562f891dc89a?w=80&h=80&fit=crop',
  environment: 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=80&h=80&fit=crop',
  health: 'https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=80&h=80&fit=crop',
  schoolWork: 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=80&h=80&fit=crop',
  socialInteractions: 'https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=80&h=80&fit=crop',
  time: 'https://images.unsplash.com/photo-1501139083538-0139583c060f?w=80&h=80&fit=crop',
  tourism: 'https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=80&h=80&fit=crop',
  transportation: 'https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=80&h=80&fit=crop'
};
let selectedLanguage = localStorage.getItem('selectedLanguage') || '';

function getLang() {
  return LANGUAGES[selectedLanguage] || LANGUAGES.marathi;
}
function getPHRASES() { return getLang().PHRASES; }
function getDICTIONARY() { return getLang().DICTIONARY; }
function getScriptFont() { return getLang().scriptFont; }

function selectLanguage(lang) {
  selectedLanguage = lang;
  localStorage.setItem('selectedLanguage', lang);
  document.getElementById('screen-lang-select').classList.remove('active');
  document.getElementById('screen-lang-select').style.display = 'none';
  document.getElementById('app-content').style.display = 'block';
  document.body.classList.add('nav-visible');
  loadSavedPhrases();
  loadSavedLessons();
  initLanguageUI();
  expandedCategory = null;
  renderCategories();
  if (currentTab === 'dictionary') renderDict('');
  if (currentTab === 'saved') renderSaved();
  chaptersLoaded = false;
  chaptersLoadedForLang = '';
  expandedMajorLesson = null;
  expandedChapter = null;
}

function changeLanguage() {
  document.getElementById('app-content').style.display = 'none';
  document.body.classList.remove('nav-visible');
  document.getElementById('screen-lang-select').style.display = 'block';
  document.getElementById('screen-lang-select').classList.add('active');
  selectedLanguage = '';
  localStorage.removeItem('selectedLanguage');
}

function initLanguageUI() {
  const lang = getLang();
  const el = (id) => document.getElementById(id);
  if (el('home-title')) el('home-title').textContent = 'Learn ' + lang.name;
  if (el('home-subtitle')) el('home-subtitle').textContent = lang.subtitle + ' • Phrase categories';
  if (el('dict-subtitle')) el('dict-subtitle').textContent = 'English → ' + lang.name;
  if (el('current-lang-display')) el('current-lang-display').textContent = 'Learning ' + lang.name;
  if (el('data-source-display')) el('data-source-display').textContent = lang.dataSource;
  document.querySelectorAll('.nav-chapters').forEach(el => {
    el.style.display = lang.hasLessons ? '' : 'none';
  });
  const resDev = document.getElementById('result-devanagari');
  if (resDev) resDev.style.fontFamily = getScriptFont();
}

function toggleCategory(catId) {
  if (expandedCategory === catId) {
    expandedCategory = null;
  } else {
    expandedCategory = catId;
  }
  renderCategories();
}

function speakPhrase(cat, idx) {
  const p = getPHRASES()[cat].phrases[idx];
  if (!p || !p.mr || !('speechSynthesis' in window)) return;
  const utt = new SpeechSynthesisUtterance(p.mr);
  utt.lang = getLang().speechLang;
  utt.rate = 0.85;
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(utt);
  showToast('Playing...');
}

function savePhraseInline(cat, idx) {
  const p = getPHRASES()[cat].phrases[idx];
  const isSaved = savedPhrases.some(s => s.mr === p.mr);
  if (isSaved) {
    savedPhrases = savedPhrases.filter(s => s.mr !== p.mr);
    showToast('Removed from saved');
  } else {
    savedPhrases.push(p);
    showToast('Phrase saved!');
  }
  saveSavedPhrases();
  renderCategories();
}

function speakSearchPhrase(ri) {
  const r = lastSearchResults[ri];
  if (!r || !r.phrase || !r.phrase.mr || !('speechSynthesis' in window)) return;
  const utt = new SpeechSynthesisUtterance(r.phrase.mr);
  utt.lang = getLang().speechLang;
  utt.rate = 0.85;
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(utt);
  showToast('Playing...');
}

function saveSearchPhraseInline(ri) {
  const r = lastSearchResults[ri];
  if (!r || !r.phrase) return;
  const p = r.phrase;
  const isSaved = savedPhrases.some(s => s.mr === p.mr);
  if (isSaved) {
    savedPhrases = savedPhrases.filter(s => s.mr !== p.mr);
    showToast('Removed from saved');
  } else {
    savedPhrases.push(p);
    showToast('Phrase saved!');
  }
  saveSavedPhrases();
  handleHomeSearch(document.getElementById('home-search').value);
}

function renderCategories() {
  const phrases = getPHRASES();
  const list = document.getElementById('cat-grid');
  if (!list) return;
  list.innerHTML = Object.entries(phrases).map(([id, data]) => {
    const iconUrl = CAT_IMAGES[id] || '';
    const fallback = CAT_INITIALS[id] || id.slice(0, 2);
    const iconHtml = iconUrl
      ? `<img class="cat-icon-img" src="${iconUrl}" alt="" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" /><span class="cat-icon cat-icon-fallback" style="display:none" data-initial="${fallback}"></span>`
      : `<span class="cat-icon" data-initial="${fallback}"></span>`;
    const isExpanded = expandedCategory === id;
    const phrasesHtml = isExpanded ? data.phrases.map((p, i) => {
      const isSaved = savedPhrases.some(s => s.mr === p.mr);
      const speakerSvg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>';
      const bookmarkSvg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m19 21-7-4-7 4V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>';
      return `
      <div class="phrase-row phrase-row-flat">
        <div class="phrase-row-text">
          <span class="phrase-en">${p.en}</span>
          <span class="phrase-roman">${p.roman}</span>
          <span class="phrase-mr" style="font-family:${getScriptFont()}">${p.mr}</span>
        </div>
        <div class="phrase-row-actions">
          <button class="phrase-save-btn phrase-save-btn-icon ${isSaved ? 'saved' : ''}" onclick="event.stopPropagation(); savePhraseInline('${id}', ${i})" title="Bookmark">${bookmarkSvg}</button>
          <button class="phrase-speaker-btn" onclick="event.stopPropagation(); speakPhrase('${id}', ${i})" title="Pronounce">${speakerSvg}</button>
        </div>
      </div>
      `;
    }).join('') : '';
    return `
    <div class="cat-row">
      <div class="cat-row-header" onclick="toggleCategory('${id}')">
        <span class="cat-icon-wrap">${iconHtml}</span>
        <div class="cat-row-info">
          <span class="cat-name">${data.name}</span>
          <span class="cat-count">${data.phrases.length} phrases</span>
        </div>
        <span class="cat-expand">${isExpanded ? '−' : '+'}</span>
      </div>
      ${isExpanded ? `<div class="cat-row-phrases">${phrasesHtml}</div>` : ''}
    </div>
  `;
  }).join('');
}

// ===== DATA =====
const PHRASES = {
  greetings: {
    name: "Greetings",
    color: "#2B6CB0",
    icon: "👋",
    phrases: [
      { en: "Hello / Hi", mr: "नमस्कार", roman: "Namaskār", hint: "Formal greeting" },
      { en: "Good morning", mr: "शुभ सकाळ", roman: "Shubh sakāḷ", hint: "" },
      { en: "Good evening", mr: "शुभ संध्याकाळ", roman: "Shubh sandhyākāḷ", hint: "" },
      { en: "Good night", mr: "शुभ रात्री", roman: "Shubh rātri", hint: "" },
      { en: "How are you?", mr: "तुम्ही कसे आहात?", roman: "Tumhī kase āhāt?", hint: "" },
      { en: "I am fine", mr: "मी ठीक आहे", roman: "Mī ṭhīk āhe", hint: "" },
      { en: "What is your name?", mr: "तुमचे नाव काय आहे?", roman: "Tumche nāv kāy āhe?", hint: "" },
      { en: "My name is...", mr: "माझे नाव ... आहे", roman: "Mājhe nāv ... āhe", hint: "" },
      { en: "Nice to meet you", mr: "तुम्हाला भेटून आनंद झाला", roman: "Tumhālā bheṭun ānand jhālā", hint: "" },
      { en: "Thank you", mr: "धन्यवाद", roman: "Dhanyavād", hint: "Very common" },
      { en: "Please", mr: "कृपया", roman: "Kṛpayā", hint: "" },
      { en: "Sorry / Excuse me", mr: "माफ करा", roman: "Māf karā", hint: "" },
    ]
  },
  travel: {
    name: "Travel",
    color: "#D69E2E",
    icon: "🚗",
    phrases: [
      { en: "How much to go here?", mr: "भाऊ, इथे जाण्याचे किती पैसे घेणार?", roman: "Bhāu, ithe jāṇyāce kitī paise gheṇār?", hint: "Auto/Taxi fare" },
      { en: "Take me to the station", mr: "मला स्टेशनला न्या", roman: "Malā steśanalā nyā", hint: "" },
      { en: "Where is the bus stop?", mr: "बस स्टॉप कुठे आहे?", roman: "Bas sṭop kuṭhe āhe?", hint: "" },
      { en: "Stop here", mr: "इथेच थांबा", roman: "Ithe thāmbā", hint: "Tell driver to stop" },
      { en: "How far is it?", mr: "किती दूर आहे?", roman: "Kitī dūr āhe?", hint: "" },
      { en: "Turn left", mr: "डावीकडे वळा", roman: "Ḍāvīkaḍe vaḷā", hint: "" },
      { en: "Turn right", mr: "उजवीकडे वळा", roman: "Ujavīkaḍe vaḷā", hint: "" },
      { en: "Go straight", mr: "सरळ जा", roman: "Saraḷ jā", hint: "" },
      { en: "I am lost", mr: "मी हरवलो आहे", roman: "Mī harvalō āhe", hint: "" },
      { en: "Where is the hospital?", mr: "दवाखाना कुठे आहे?", roman: "Davākhānā kuṭhe āhe?", hint: "" },
      { en: "Is this the right road?", mr: "हा बरोबर रस्ता आहे का?", roman: "Hā barōbar rastā āhe kā?", hint: "" },
      { en: "Please drive slowly", mr: "हळू चालवा", roman: "Haḷū cālavā", hint: "" },
      { en: "Where is the market?", mr: "बाजार कुठे आहे?", roman: "Bājār kuṭhe āhe?", hint: "" },
      { en: "How much is the ticket?", mr: "तिकिटाचे किती पैसे?", roman: "Tikaṭāce kitī paise?", hint: "" },
      { en: "I want to go to...", mr: "मला ... ला जायचे आहे", roman: "Malā ... lā jāyace āhe", hint: "" },
      { en: "Wait here", mr: "इथे थांबा", roman: "Ithe thāmbā", hint: "" },
      { en: "Can you come back later?", mr: "नंतर याल का?", roman: "Nantara yāl kā?", hint: "" },
      { en: "Take the highway", mr: "हायवे घ्या", roman: "Hāyave ghyā", hint: "" },
    ]
  },
  food: {
    name: "Food & Dining",
    color: "#C05621",
    icon: "🍽️",
    phrases: [
      { en: "What do you have to eat?", mr: "जेवायला काय आहे?", roman: "Jevāyalā kāy āhe?", hint: "" },
      { en: "I am hungry", mr: "मला भूक लागली आहे", roman: "Malā bhūk lāgalī āhe", hint: "" },
      { en: "The food is very tasty", mr: "जेवण खूप चविष्ट आहे", roman: "Jevaṇ khūp caviṣṭ āhe", hint: "" },
      { en: "Give me water please", mr: "मला पाणी द्या", roman: "Malā pāṇī dyā", hint: "" },
      { en: "I don't eat meat", mr: "मी मांस खात नाही", roman: "Mī māns khāt nāhī", hint: "" },
      { en: "The bill please", mr: "बिल आणा", roman: "Bil āṇā", hint: "" },
      { en: "Is it spicy?", mr: "हे तिखट आहे का?", roman: "He tikhaṭ āhe kā?", hint: "" },
      { en: "Less spicy please", mr: "कमी तिखट करा", roman: "Kamī tikhaṭ karā", hint: "" },
      { en: "One more serving", mr: "आणखी एक वाढा", roman: "Āṇakhī ek vāḍhā", hint: "" },
      { en: "Do you have veg options?", mr: "शाकाहारी काही आहे का?", roman: "Śākāhārī kāhī āhe kā?", hint: "" },
      { en: "Very delicious!", mr: "खूप छान!", roman: "Khūp chān!", hint: "" },
      { en: "I am full", mr: "माझे पोट भरले", roman: "Mājhe poṭ bharale", hint: "" },
      { en: "Can I get tea?", mr: "चहा मिळेल का?", roman: "Cahā miḷel kā?", hint: "" },
      { en: "No sugar please", mr: "साखर नको", roman: "Sākhar nakō", hint: "" },
      { en: "Pack it please", mr: "पार्सल करा", roman: "Pārsal karā", hint: "Takeaway" },
    ]
  },
  shopping: {
    name: "Shopping",
    color: "#805AD5",
    icon: "🛍️",
    phrases: [
      { en: "How much does this cost?", mr: "हे किती रुपयांना आहे?", roman: "He kitī rupayānnā āhe?", hint: "" },
      { en: "Give me a discount", mr: "थोडे कमी करा", roman: "Thoḍe kamī karā", hint: "Ask for discount" },
      { en: "Do you have a smaller size?", mr: "लहान साइज आहे का?", roman: "Lahān sāij āhe kā?", hint: "" },
      { en: "I'll take this", mr: "मला हे हवे आहे", roman: "Malā he have āhe", hint: "" },
      { en: "This is too expensive", mr: "हे खूप महाग आहे", roman: "He khūp mahāg āhe", hint: "" },
      { en: "Final price?", mr: "शेवटची किंमत किती?", roman: "Śevaṭacī kimmat kitī?", hint: "" },
      { en: "I'll come back later", mr: "मी नंतर येतो", roman: "Mī nantar yetō", hint: "" },
      { en: "Do you accept card?", mr: "कार्ड चालते का?", roman: "Kārḍ cālate kā?", hint: "" },
      { en: "Give me a bag", mr: "पिशवी द्या", roman: "Piśavī dyā", hint: "" },
      { en: "Do you have this in another color?", mr: "दुसऱ्या रंगात आहे का?", roman: "Dusaṛyā rangāt āhe kā?", hint: "" },
    ]
  },
  emergency: {
    name: "Emergency",
    color: "#E53E3E",
    icon: "🚨",
    phrases: [
      { en: "Help!", mr: "मदत करा!", roman: "Madat karā!", hint: "Urgent" },
      { en: "Call the police", mr: "पोलिसांना बोलवा", roman: "Polisānnā bolavā", hint: "" },
      { en: "I need a doctor", mr: "मला डॉक्टर हवे आहेत", roman: "Malā ḍŏkṭar have āhet", hint: "" },
      { en: "There is a fire!", mr: "आग लागली!", roman: "Āg lāgalī!", hint: "" },
      { en: "I have been robbed", mr: "माझी चोरी झाली", roman: "Mājhī corī jhālī", hint: "" },
      { en: "I am not feeling well", mr: "मला बरे वाटत नाही", roman: "Malā bare vāṭat nāhī", hint: "" },
      { en: "Take me to hospital", mr: "मला रुग्णालयात न्या", roman: "Malā rugṇālayāt nyā", hint: "" },
      { en: "I lost my phone", mr: "माझा फोन हरवला", roman: "Mājhā phon haravalā", hint: "" },
    ]
  },
  numbers: {
    name: "Numbers",
    color: "#38A169",
    icon: "🔢",
    phrases: [
      { en: "One (1)", mr: "एक", roman: "Ek", hint: "" },
      { en: "Two (2)", mr: "दोन", roman: "Don", hint: "" },
      { en: "Three (3)", mr: "तीन", roman: "Tīn", hint: "" },
      { en: "Four (4)", mr: "चार", roman: "Cār", hint: "" },
      { en: "Five (5)", mr: "पाच", roman: "Pāc", hint: "" },
      { en: "Six (6)", mr: "सहा", roman: "Sahā", hint: "" },
      { en: "Seven (7)", mr: "सात", roman: "Sāt", hint: "" },
      { en: "Eight (8)", mr: "आठ", roman: "Āṭh", hint: "" },
      { en: "Nine (9)", mr: "नऊ", roman: "Na'ū", hint: "" },
      { en: "Ten (10)", mr: "दहा", roman: "Dahā", hint: "" },
      { en: "Twenty (20)", mr: "वीस", roman: "Vīs", hint: "" },
      { en: "Fifty (50)", mr: "पन्नास", roman: "Pannās", hint: "" },
      { en: "Hundred (100)", mr: "शंभर", roman: "Śambhar", hint: "" },
      { en: "Thousand (1000)", mr: "हजार", roman: "Hajār", hint: "" },
      { en: "How many?", mr: "किती?", roman: "Kitī?", hint: "" },
      { en: "How much money?", mr: "किती पैसे?", roman: "Kitī paise?", hint: "" },
      { en: "Zero (0)", mr: "शून्य", roman: "Śūnya", hint: "" },
      { en: "First", mr: "पहिला", roman: "Pahilā", hint: "" },
      { en: "Second", mr: "दुसरा", roman: "Dusarā", hint: "" },
      { en: "Last", mr: "शेवटचा", roman: "Śevaṭacā", hint: "" },
    ]
  },
  reading: {
    name: "Reading",
    color: "#4A5568",
    icon: "📖",
    phrases: [
      { en: "Book", mr: "पुस्तक", roman: "Pustak", hint: "" },
      { en: "Library", mr: "ग्रंथालय", roman: "Graṃthālay", hint: "" },
      { en: "I am reading", mr: "मी वाचत आहे", roman: "Mī vācat āhe", hint: "" },
      { en: "Where is the library?", mr: "ग्रंथालय कुठे आहे?", roman: "Graṃthālay kuṭhe āhe?", hint: "" },
      { en: "Do you have this book?", mr: "तुमच्याकडे हे पुस्तक आहे का?", roman: "Tumacyākaḍe he pustak āhe kā?", hint: "" },
      { en: "I like to read", mr: "मला वाचायला आवडते", roman: "Malā vācāyalā āvaḍate", hint: "" },
      { en: "Newspaper", mr: "वृत्तपत्र", roman: "Vṛttapatra", hint: "" },
      { en: "Story", mr: "कथा", roman: "Kathā", hint: "" },
      { en: "Page", mr: "पृष्ठ", roman: "Pṛṣṭh", hint: "" },
      { en: "Can you read this?", mr: "तुम्ही हे वाचू शकता का?", roman: "Tumhī he vācū śakatā kā?", hint: "" },
    ]
  },
  writing: {
    name: "Writing",
    color: "#2C5282",
    icon: "✏️",
    phrases: [
      { en: "Pen", mr: "पेन", roman: "Pen", hint: "" },
      { en: "Paper", mr: "कागद", roman: "Kāgad", hint: "" },
      { en: "I am writing", mr: "मी लिहित आहे", roman: "Mī lihit āhe", hint: "" },
      { en: "Write your name", mr: "तुमचे नाव लिहा", roman: "Tumace nāv lihā", hint: "" },
      { en: "Letter", mr: "पत्र", roman: "Patra", hint: "" },
      { en: "Please write this down", mr: "कृपया हे लिहून द्या", roman: "Kṛpayā he lihūn dyā", hint: "" },
      { en: "I cannot write Marathi", mr: "मी मराठी लिहू शकत नाही", roman: "Mī marāṭhī lihū śakat nāhī", hint: "" },
      { en: "Notebook", mr: "नोटबुक", roman: "Noṭabuk", hint: "" },
      { en: "Pencil", mr: "पेन्सिल", roman: "Pensil", hint: "" },
      { en: "Signature", mr: "सही", roman: "Sahī", hint: "" },
    ]
  },
  animals: {
    name: "Animals",
    color: "#744210",
    icon: "🐾",
    phrases: [
      { en: "Dog", mr: "कुत्रा", roman: "Kutrā", hint: "" },
      { en: "Cat", mr: "मांजर", roman: "Māṃjar", hint: "" },
      { en: "Cow", mr: "गाय", roman: "Gāy", hint: "" },
      { en: "Bird", mr: "पक्षी", roman: "Pakṣī", hint: "" },
      { en: "Elephant", mr: "हत्ती", roman: "Hattī", hint: "" },
      { en: "Horse", mr: "घोडा", roman: "Ghoḍā", hint: "" },
      { en: "Tiger", mr: "वाघ", roman: "Vāgh", hint: "" },
      { en: "Monkey", mr: "माकड", roman: "Mākaḍ", hint: "" },
      { en: "Fish", mr: "मासा", roman: "Māsā", hint: "" },
      { en: "Animal", mr: "प्राणी", roman: "Prāṇī", hint: "" },
      { en: "Peacock", mr: "मोर", roman: "Mor", hint: "" },
      { en: "Snake", mr: "साप", roman: "Sāp", hint: "" },
    ]
  },
  dailyLife: {
    name: "Daily Life",
    color: "#553C9A",
    icon: "🏠",
    phrases: [
      { en: "I wake up early", mr: "मी लवकर उठतो", roman: "Mī lavakar uṭhatō", hint: "" },
      { en: "I am going to work", mr: "मी कामाला जात आहे", roman: "Mī kāmālā jāt āhe", hint: "" },
      { en: "What are you doing?", mr: "तू काय करत आहेस?", roman: "Tū kāy karat āhes?", hint: "" },
      { en: "I don't understand", mr: "मला कळत नाही", roman: "Malā kaḷat nāhī", hint: "" },
      { en: "Please speak slowly", mr: "कृपया हळू बोला", roman: "Kṛpayā haḷū bolā", hint: "" },
      { en: "How was your day?", mr: "तुमचा दिवस कसा गेला?", roman: "Tumacā divas kasā gelā?", hint: "" },
      { en: "I need water", mr: "मला पाणी पाहिजे", roman: "Malā pāṇī pāhije", hint: "" },
      { en: "Where do you live?", mr: "तुम्ही कुठे राहता?", roman: "Tumhī kuṭhe rāhatā?", hint: "" },
      { en: "I am tired", mr: "मला थकवा आला", roman: "Malā thakavā ālā", hint: "" },
      { en: "Good luck!", mr: "शुभेच्छा!", roman: "Śubhecchā!", hint: "" },
    ]
  },
  environment: {
    name: "Environment",
    color: "#276749",
    icon: "🌿",
    phrases: [
      { en: "Weather", mr: "हवामान", roman: "Havāmān", hint: "" },
      { en: "It's hot", mr: "गरम आहे", roman: "Garam āhe", hint: "" },
      { en: "It's cold", mr: "थंड आहे", roman: "Thaṇḍ āhe", hint: "" },
      { en: "It's raining", mr: "पाऊस पडत आहे", roman: "Pāūs paḍat āhe", hint: "" },
      { en: "Sun", mr: "सूर्य", roman: "Sūrya", hint: "" },
      { en: "Tree", mr: "झाड", roman: "Jhāḍ", hint: "" },
      { en: "Flower", mr: "फूल", roman: "Phūl", hint: "" },
      { en: "Nature", mr: "निसर्ग", roman: "Nisarga", hint: "" },
      { en: "River", mr: "नदी", roman: "Nadī", hint: "" },
      { en: "Summer", mr: "उन्हाळा", roman: "Unhāḷā", hint: "" },
      { en: "Winter", mr: "हिवाळा", roman: "Hivāḷā", hint: "" },
      { en: "Rain", mr: "पाऊस", roman: "Pāūs", hint: "" },
    ]
  },
  health: {
    name: "Health",
    color: "#C53030",
    icon: "🏥",
    phrases: [
      { en: "Doctor", mr: "डॉक्टर", roman: "Ḍŏkṭar", hint: "" },
      { en: "Hospital", mr: "रुग्णालय", roman: "Rugṇālay", hint: "" },
      { en: "Medicine", mr: "औषध", roman: "Auṣadh", hint: "" },
      { en: "I have fever", mr: "मला ताप आहे", roman: "Malā tāp āhe", hint: "" },
      { en: "I have pain", mr: "मला वेदना आहे", roman: "Malā vedanā āhe", hint: "" },
      { en: "Where is the pharmacy?", mr: "औषधाची दुकान कुठे आहे?", roman: "Auṣadhācī dukān kuṭhe āhe?", hint: "" },
      { en: "Take this medicine", mr: "हे औषध घ्या", roman: "He auṣadh ghyā", hint: "" },
      { en: "I need a doctor", mr: "मला डॉक्टर हवे आहेत", roman: "Malā ḍŏkṭar have āhet", hint: "" },
      { en: "Headache", mr: "डोकेदुखी", roman: "Ḍōkedukhī", hint: "" },
      { en: "Stomach ache", mr: "पोटदुखी", roman: "Poṭadukhī", hint: "" },
    ]
  },
  schoolWork: {
    name: "School & Work",
    color: "#2B6CB0",
    icon: "💼",
    phrases: [
      { en: "School", mr: "शाळा", roman: "Śāḷā", hint: "" },
      { en: "Teacher", mr: "शिक्षक", roman: "Śikṣak", hint: "" },
      { en: "Student", mr: "विद्यार्थी", roman: "Vidyārthī", hint: "" },
      { en: "Office", mr: "कार्यालय", roman: "Kāryālay", hint: "" },
      { en: "Meeting", mr: "बैठक", roman: "Baiṭhak", hint: "" },
      { en: "What is the homework?", mr: "गृहपाठ काय आहे?", roman: "Gruhapāṭh kāy āhe?", hint: "" },
      { en: "I have a meeting", mr: "मला बैठक आहे", roman: "Malā baiṭhak āhe", hint: "" },
      { en: "Where is the manager?", mr: "व्यवस्थापक कुठे आहे?", roman: "Vyavasthāpak kuṭhe āhe?", hint: "" },
      { en: "Exam", mr: "परीक्षा", roman: "Parīkṣā", hint: "" },
      { en: "I don't understand", mr: "मला समजत नाही", roman: "Malā samajat nāhī", hint: "" },
    ]
  },
  socialInteractions: {
    name: "Social Interactions",
    color: "#9F7AEA",
    icon: "👥",
    phrases: [
      { en: "How are you?", mr: "तुम्ही कसे आहात?", roman: "Tumhī kase āhāt?", hint: "" },
      { en: "What's going on?", mr: "काय चालते?", roman: "Kāy cālate?", hint: "" },
      { en: "I am fine", mr: "मी ठीक आहे", roman: "Mī ṭhīk āhe", hint: "" },
      { en: "Nice to meet you", mr: "तुम्हाला भेटून आनंद झाला", roman: "Tumhālā bheṭun ānand jhālā", hint: "" },
      { en: "See you later", mr: "नंतर भेटू", roman: "Nantar bheṭū", hint: "" },
      { en: "Take care", mr: "काळजी घ्या", roman: "Kāḷajī ghyā", hint: "" },
      { en: "Congratulations!", mr: "अभिनंदन!", roman: "Abhinandan!", hint: "" },
      { en: "Welcome", mr: "स्वागत आहे", roman: "Svāgat āhe", hint: "" },
      { en: "Excuse me", mr: "माफ करा", roman: "Māf karā", hint: "" },
      { en: "Can you help me?", mr: "तुम्ही मला मदत करू शकता का?", roman: "Tumhī malā madat karū śakatā kā?", hint: "" },
    ]
  },
  time: {
    name: "Time",
    color: "#3182CE",
    icon: "🕐",
    phrases: [
      { en: "What time is it?", mr: "किती वाजले?", roman: "Kitī vājale?", hint: "" },
      { en: "Today", mr: "आज", roman: "Āj", hint: "" },
      { en: "Tomorrow", mr: "उद्या", roman: "Udyā", hint: "" },
      { en: "Yesterday", mr: "काल", roman: "Kāl", hint: "" },
      { en: "Morning", mr: "सकाळ", roman: "Sakāḷ", hint: "" },
      { en: "Evening", mr: "संध्याकाळ", roman: "Sandhyākāḷ", hint: "" },
      { en: "Night", mr: "रात्र", roman: "Rātra", hint: "" },
      { en: "Monday", mr: "सोमवार", roman: "Sōmavār", hint: "" },
      { en: "Week", mr: "आठवडा", roman: "Āṭhavaḍā", hint: "" },
      { en: "When?", mr: "केव्हा?", roman: "Kēvhā?", hint: "" },
    ]
  },
  tourism: {
    name: "Tourism",
    color: "#D69E2E",
    icon: "🗺️",
    phrases: [
      { en: "Where is this place?", mr: "हे स्थान कुठे आहे?", roman: "He sthān kuṭhe āhe?", hint: "" },
      { en: "Where is the bathroom?", mr: "बाथरूम कुठे आहे?", roman: "Bāthrūm kuṭhe āhe?", hint: "" },
      { en: "I am a tourist", mr: "मी पर्यटक आहे", roman: "Mī paryaṭak āhe", hint: "" },
      { en: "Take a photo please", mr: "कृपया फोटो काढा", roman: "Kṛpayā phōṭō kāḍhā", hint: "" },
      { en: "The food was delicious", mr: "जेवण छान होते", roman: "Jevaṇ chān hōte", hint: "" },
      { en: "Where can I stay?", mr: "मला कुठे राहता येईल?", roman: "Malā kuṭhe rāhatā yēīl?", hint: "" },
      { en: "Hotel", mr: "हॉटेल", roman: "Hŏṭel", hint: "" },
      { en: "Beautiful place", mr: "सुंदर ठिकाण", roman: "Suṃdar ṭhikāṇ", hint: "" },
      { en: "I need help", mr: "मला मदतीची आवश्यकता आहे", roman: "Malā madatīcī āvaśyakatā āhe", hint: "" },
      { en: "Goodbye", mr: "निरोप घ्या", roman: "Nirōp ghyā", hint: "" },
    ]
  },
  transportation: {
    name: "Transportation",
    color: "#2D3748",
    icon: "🚌",
    phrases: [
      { en: "Bus", mr: "बस", roman: "Bas", hint: "" },
      { en: "Train", mr: "रेल्वे", roman: "Relve", hint: "" },
      { en: "Ticket", mr: "तिकीट", roman: "Tikīṭ", hint: "" },
      { en: "When is the next bus?", mr: "पुढची बस कधी आहे?", roman: "Puḍhacī bas kadhī āhe?", hint: "" },
      { en: "How much is the fare?", mr: "भाडे किती आहे?", roman: "Bhāḍe kitī āhe?", hint: "" },
      { en: "Where is the railway station?", mr: "रेल्वे स्टेशन कुठे आहे?", roman: "Relve sṭeśan kuṭhe āhe?", hint: "" },
      { en: "I want a ticket to...", mr: "मला ... साठी तिकीट पाहिजे", roman: "Malā ... sāṭhī tikīṭ pāhije", hint: "" },
      { en: "Does this bus go to...?", mr: "ही बस ... ला जाते का?", roman: "Hī bas ... lā jāte kā?", hint: "" },
      { en: "Platform", mr: "प्लॅटफॉर्म", roman: "Plaṭphŏrm", hint: "" },
      { en: "Ticket counter", mr: "तिकीट काऊंटर", roman: "Tikīṭ kāūnṭar", hint: "" },
    ]
  }
};

const DICTIONARY = [
  { en: "Water", mr: "पाणी", roman: "Pāṇī" },
  { en: "Food", mr: "जेवण", roman: "Jevaṇ" },
  { en: "House", mr: "घर", roman: "Ghar" },
  { en: "Road", mr: "रस्ता", roman: "Rastā" },
  { en: "Money", mr: "पैसे", roman: "Paise" },
  { en: "Time", mr: "वेळ", roman: "Veḷ" },
  { en: "Day", mr: "दिवस", roman: "Divas" },
  { en: "Night", mr: "रात्र", roman: "Rātra" },
  { en: "Mother", mr: "आई", roman: "Āī" },
  { en: "Father", mr: "बाबा", roman: "Bābā" },
  { en: "Brother", mr: "भाऊ", roman: "Bhāū" },
  { en: "Sister", mr: "ताई", roman: "Tāī" },
  { en: "Friend", mr: "मित्र", roman: "Mitra" },
  { en: "School", mr: "शाळा", roman: "Śāḷā" },
  { en: "Work", mr: "काम", roman: "Kām" },
  { en: "City", mr: "शहर", roman: "Śahar" },
  { en: "Village", mr: "गाव", roman: "Gāv" },
  { en: "Morning", mr: "सकाळ", roman: "Sakāḷ" },
  { en: "Evening", mr: "संध्याकाळ", roman: "Sandhyākāḷ" },
  { en: "Today", mr: "आज", roman: "Āj" },
  { en: "Tomorrow", mr: "उद्या", roman: "Udyā" },
  { en: "Yesterday", mr: "काल", roman: "Kāl" },
  { en: "Yes", mr: "हो", roman: "Ho" },
  { en: "No", mr: "नाही", roman: "Nāhī" },
  { en: "Good", mr: "चांगले", roman: "Cāṅgale" },
  { en: "Bad", mr: "वाईट", roman: "Vāīṭ" },
  { en: "Big", mr: "मोठे", roman: "Moṭhe" },
  { en: "Small", mr: "लहान", roman: "Lahān" },
  { en: "Hot", mr: "गरम", roman: "Garam" },
  { en: "Cold", mr: "थंड", roman: "Thaṇḍ" },
];

// Gujarati phrases & dictionary - same structure as Marathi
const GUJARATI_PHRASES = {
  greetings: {
    name: "Greetings",
    color: "#2B6CB0",
    icon: "👋",
    phrases: [
      { en: "Hello / Hi", mr: "નમસ્તે", roman: "Namastē", hint: "Formal greeting" },
      { en: "Good morning", mr: "સુપ્રભાત", roman: "Suprabhāt", hint: "" },
      { en: "Good evening", mr: "શુભ સાંજ", roman: "Śubh sāñj", hint: "" },
      { en: "Good night", mr: "શુભ રાત્રી", roman: "Śubh rātrī", hint: "" },
      { en: "How are you?", mr: "તમે કેમ છો?", roman: "Tame kēm chhō?", hint: "" },
      { en: "I am fine", mr: "હું ઠીક છું", roman: "Huṃ ṭhīk chhuṃ", hint: "" },
      { en: "What is your name?", mr: "તમારું નામ શું છે?", roman: "Tamāruṃ nām śuṃ chhe?", hint: "" },
      { en: "My name is...", mr: "મારું નામ ... છે", roman: "Māruṃ nām ... chhe", hint: "" },
      { en: "Nice to meet you", mr: "તમને મળીને આનંદ થયો", roman: "Tamne maḷīnē ānand thayō", hint: "" },
      { en: "Thank you", mr: "આભાર", roman: "Ābhār", hint: "Very common" },
      { en: "Please", mr: "કૃપા કરીને", roman: "Kṛpā karīnē", hint: "" },
      { en: "Sorry / Excuse me", mr: "માફ કરજો", roman: "Māf karajō", hint: "" },
    ]
  },
  travel: {
    name: "Travel",
    color: "#D69E2E",
    icon: "🚗",
    phrases: [
      { en: "How much to go here?", mr: "ભાઈ, અહીં જવાના કેટલા પૈસા લેશો?", roman: "Bhāī, ahīṃ javānā keṭalā paisā lēśō?", hint: "Auto/Taxi fare" },
      { en: "Take me to the station", mr: "મને સ્ટેશન લઈ જાઓ", roman: "Mane sṭēśan laī jāō", hint: "" },
      { en: "Where is the bus stop?", mr: "બસ સ્ટોપ ક્યાં છે?", roman: "Bas sṭōp kyaṃ chhe?", hint: "" },
      { en: "Stop here", mr: "અહીં થોભો", roman: "Ahīṃ thōbhō", hint: "Tell driver to stop" },
      { en: "How far is it?", mr: "કેટલું દૂર છે?", roman: "Keṭaluṃ dūr chhe?", hint: "" },
      { en: "Turn left", mr: "ડાબી બાજુ વળો", roman: "Ḍābī bāju vaḷō", hint: "" },
      { en: "Turn right", mr: "જમણી બાજુ વળો", roman: "Jamaṇī bāju vaḷō", hint: "" },
      { en: "Go straight", mr: "સીધા જાઓ", roman: "Sīdhā jāō", hint: "" },
      { en: "I am lost", mr: "હું ખોવાઈ ગયો છું", roman: "Huṃ khōvāī gayō chhuṃ", hint: "" },
      { en: "Where is the hospital?", mr: "હોસ્પિટલ ક્યાં છે?", roman: "Hōspiṭal kyaṃ chhe?", hint: "" },
      { en: "Is this the right road?", mr: "આ સાચો રસ્તો છે?", roman: "Ā sācō rastō chhe?", hint: "" },
      { en: "Please drive slowly", mr: "ધીમે ચલાવો", roman: "Dhīmē calāvō", hint: "" },
      { en: "Where is the market?", mr: "બજાર ક્યાં છે?", roman: "Bajār kyaṃ chhe?", hint: "" },
      { en: "How much is the ticket?", mr: "ટિકિટના કેટલા પૈસા?", roman: "Ṭikiṭanā keṭalā paisā?", hint: "" },
      { en: "I want to go to...", mr: "મારે ... જવું છે", roman: "Mārē ... javuṃ chhe", hint: "" },
      { en: "Wait here", mr: "અહીં થોભો", roman: "Ahīṃ thōbhō", hint: "" },
      { en: "Can you come back later?", mr: "પછી આવશો?", roman: "Pachī āvaśō?", hint: "" },
      { en: "Take the highway", mr: "હાઇવે લો", roman: "Hāivē lō", hint: "" },
    ]
  },
  food: {
    name: "Food & Dining",
    color: "#C05621",
    icon: "🍽️",
    phrases: [
      { en: "What do you have to eat?", mr: "જમવાને શું છે?", roman: "Jamavānē śuṃ chhe?", hint: "" },
      { en: "I am hungry", mr: "મને ભૂખ લાગી છે", roman: "Mane bhūkh lāgī chhe", hint: "" },
      { en: "The food is very tasty", mr: "જમવું ખૂબ સ્વાદિષ્ટ છે", roman: "Jamavuṃ khūba svādiṣṭ chhe", hint: "" },
      { en: "Give me water please", mr: "મને પાણી આપો", roman: "Mane pāṇī āpō", hint: "" },
      { en: "I don't eat meat", mr: "હું માંસ ખાતો નથી", roman: "Huṃ māṃs khātō nathī", hint: "" },
      { en: "The bill please", mr: "બિલ લાવો", roman: "Bil lāvō", hint: "" },
      { en: "Is it spicy?", mr: "આ તીખું છે?", roman: "Ā tīkhuṃ chhe?", hint: "" },
      { en: "Less spicy please", mr: "ઓછું તીખું કરો", roman: "Ōchuṃ tīkhuṃ karō", hint: "" },
      { en: "One more serving", mr: "એક વધુ વાઢો", roman: "Ēk vadhu vāḍhō", hint: "" },
      { en: "Do you have veg options?", mr: "શાકાહારી કંઈ છે?", roman: "Śākāhārī kaṃī chhe?", hint: "" },
      { en: "Very delicious!", mr: "ખૂબ સ્વાદિષ્ટ!", roman: "Khūba svādiṣṭ!", hint: "" },
      { en: "I am full", mr: "મારું પેટ ભરી ગયું", roman: "Māruṃ pēṭ bharī gayuṃ", hint: "" },
      { en: "Can I get tea?", mr: "ચા મળશે?", roman: "Cā maḷaśē?", hint: "" },
      { en: "No sugar please", mr: "ખાંડ નહીં", roman: "Khāṃḍ nahīṃ", hint: "" },
      { en: "Pack it please", mr: "પાર્સલ કરો", roman: "Pārsal karō", hint: "Takeaway" },
    ]
  },
  shopping: {
    name: "Shopping",
    color: "#805AD5",
    icon: "🛍️",
    phrases: [
      { en: "How much does this cost?", mr: "આ કેટલા રૂપિયા?", roman: "Ā keṭalā rūpiyā?", hint: "" },
      { en: "Give me a discount", mr: "થોડું ઓછું કરો", roman: "Thōḍuṃ ōchuṃ karō", hint: "Ask for discount" },
      { en: "Do you have a smaller size?", mr: "છોટી સાઇઝ છે?", roman: "Chhōṭī sāij chhe?", hint: "" },
      { en: "I'll take this", mr: "મારે આ જોઈએ છે", roman: "Mārē ā jōīē chhe", hint: "" },
      { en: "This is too expensive", mr: "આ ખૂબ ખર્ચાળ છે", roman: "Ā khūba kharcāḷ chhe", hint: "" },
      { en: "Final price?", mr: "છેલ્લી કિંમત કેટલી?", roman: "Chhēllī kiṃmat keṭalī?", hint: "" },
      { en: "I'll come back later", mr: "હું પછી આવીશ", roman: "Huṃ pachī āvīś", hint: "" },
      { en: "Do you accept card?", mr: "કાર્ડ ચાલે?", roman: "Kārḍ cālē?", hint: "" },
      { en: "Give me a bag", mr: "બેગ આપો", roman: "Bēg āpō", hint: "" },
      { en: "Do you have this in another color?", mr: "બીજા રંગમાં છે?", roman: "Bījā raṃgamāṃ chhe?", hint: "" },
    ]
  },
  emergency: {
    name: "Emergency",
    color: "#E53E3E",
    icon: "🚨",
    phrases: [
      { en: "Help!", mr: "મદદ કરો!", roman: "Madad karō!", hint: "Urgent" },
      { en: "Call the police", mr: "પોલીસને બોલાવો", roman: "Pōlīsne bōlāvō", hint: "" },
      { en: "I need a doctor", mr: "મારે ડૉક્ટર જોઈએ છે", roman: "Mārē ḍŏkṭar jōīē chhe", hint: "" },
      { en: "There is a fire!", mr: "આગ લાગી!", roman: "Āg lāgī!", hint: "" },
      { en: "I have been robbed", mr: "મારી ચોરી થઈ ગઈ", roman: "Mārī cōrī thaī gaī", hint: "" },
      { en: "I am not feeling well", mr: "મને સારું લાગતું નથી", roman: "Mane sāruṃ lāgatuṃ nathī", hint: "" },
      { en: "Take me to hospital", mr: "મને હોસ્પિટલ લઈ જાઓ", roman: "Mane hōspiṭal laī jāō", hint: "" },
      { en: "I lost my phone", mr: "મારો ફોન ખોવાઈ ગયો", roman: "Mārō phōn khōvāī gayō", hint: "" },
    ]
  },
  numbers: {
    name: "Numbers",
    color: "#38A169",
    icon: "🔢",
    phrases: [
      { en: "One (1)", mr: "એક", roman: "Ēk", hint: "" },
      { en: "Two (2)", mr: "બે", roman: "Bē", hint: "" },
      { en: "Three (3)", mr: "ત્રણ", roman: "Traṇ", hint: "" },
      { en: "Four (4)", mr: "ચાર", roman: "Cār", hint: "" },
      { en: "Five (5)", mr: "પાંચ", roman: "Pāṃc", hint: "" },
      { en: "Six (6)", mr: "છ", roman: "Chha", hint: "" },
      { en: "Seven (7)", mr: "સાત", roman: "Sāt", hint: "" },
      { en: "Eight (8)", mr: "આઠ", roman: "Āṭh", hint: "" },
      { en: "Nine (9)", mr: "નવ", roman: "Nav", hint: "" },
      { en: "Ten (10)", mr: "દસ", roman: "Das", hint: "" },
      { en: "Twenty (20)", mr: "વીસ", roman: "Vīs", hint: "" },
      { en: "Fifty (50)", mr: "પચાસ", roman: "Pacās", hint: "" },
      { en: "Hundred (100)", mr: "સો", roman: "Sō", hint: "" },
      { en: "Thousand (1000)", mr: "હજાર", roman: "Hajār", hint: "" },
      { en: "How many?", mr: "કેટલા?", roman: "Keṭalā?", hint: "" },
      { en: "How much money?", mr: "કેટલા પૈસા?", roman: "Keṭalā paisā?", hint: "" },
      { en: "Zero (0)", mr: "શૂન્ય", roman: "Śūnya", hint: "" },
      { en: "First", mr: "પહેલું", roman: "Pahēluṃ", hint: "" },
      { en: "Second", mr: "બીજું", roman: "Bījuṃ", hint: "" },
      { en: "Last", mr: "છેલ્લું", roman: "Chhēlluṃ", hint: "" },
    ]
  },
  reading: {
    name: "Reading",
    color: "#4A5568",
    icon: "📖",
    phrases: [
      { en: "Book", mr: "પુસ્તક", roman: "Pustak", hint: "" },
      { en: "Library", mr: "ગ્રંથાલય", roman: "Graṃthālay", hint: "" },
      { en: "I am reading", mr: "હું વાંચું છું", roman: "Huṃ vāṃcuṃ chhuṃ", hint: "" },
      { en: "Where is the library?", mr: "ગ્રંથાલય ક્યાં છે?", roman: "Graṃthālay kyaṃ chhe?", hint: "" },
      { en: "Do you have this book?", mr: "તમારી પાસે આ પુસ્તક છે?", roman: "Tamārī pāsē ā pustak chhe?", hint: "" },
      { en: "I like to read", mr: "મને વાંચવું ગમે છે", roman: "Mane vāṃcavuṃ gamē chhe", hint: "" },
      { en: "Newspaper", mr: "વર્તમાનપત્ર", roman: "Vartamānapatra", hint: "" },
      { en: "Story", mr: "કથા", roman: "Kathā", hint: "" },
      { en: "Page", mr: "પાનું", roman: "Pānuṃ", hint: "" },
      { en: "Can you read this?", mr: "તમે આ વાંચી શકો છો?", roman: "Tame ā vāṃcī śakō chhō?", hint: "" },
    ]
  },
  writing: {
    name: "Writing",
    color: "#2C5282",
    icon: "✏️",
    phrases: [
      { en: "Pen", mr: "પેન", roman: "Pēn", hint: "" },
      { en: "Paper", mr: "કાગળ", roman: "Kāgaḷ", hint: "" },
      { en: "I am writing", mr: "હું લખું છું", roman: "Huṃ lakhūṃ chhuṃ", hint: "" },
      { en: "Write your name", mr: "તમારું નામ લખો", roman: "Tamāruṃ nām lakhō", hint: "" },
      { en: "Letter", mr: "પત્ર", roman: "Patra", hint: "" },
      { en: "Please write this down", mr: "કૃપા કરીને આ લખી આપો", roman: "Kṛpā karīnē ā lakhī āpō", hint: "" },
      { en: "I cannot write Gujarati", mr: "હું ગુજરાતી લખી શકતો નથી", roman: "Huṃ gujarātī lakhī śakatō nathī", hint: "" },
      { en: "Notebook", mr: "નોટબુક", roman: "Nōṭabuk", hint: "" },
      { en: "Pencil", mr: "પેન્સિલ", roman: "Pēnsil", hint: "" },
      { en: "Signature", mr: "સહી", roman: "Sahī", hint: "" },
    ]
  },
  animals: {
    name: "Animals",
    color: "#744210",
    icon: "🐾",
    phrases: [
      { en: "Dog", mr: "કુતરો", roman: "Kutrō", hint: "" },
      { en: "Cat", mr: "બિલાડી", roman: "Bilāḍī", hint: "" },
      { en: "Cow", mr: "ગાય", roman: "Gāy", hint: "" },
      { en: "Bird", mr: "પક્ષી", roman: "Pakṣī", hint: "" },
      { en: "Elephant", mr: "હાથી", roman: "Hāthī", hint: "" },
      { en: "Horse", mr: "ઘોડો", roman: "Ghōḍō", hint: "" },
      { en: "Tiger", mr: "વાઘ", roman: "Vāgh", hint: "" },
      { en: "Monkey", mr: "માકડો", roman: "Mākaḍō", hint: "" },
      { en: "Fish", mr: "માછલી", roman: "Māchalī", hint: "" },
      { en: "Animal", mr: "પ્રાણી", roman: "Prāṇī", hint: "" },
      { en: "Peacock", mr: "મોર", roman: "Mōr", hint: "" },
      { en: "Snake", mr: "સાપ", roman: "Sāp", hint: "" },
    ]
  },
  dailyLife: {
    name: "Daily Life",
    color: "#553C9A",
    icon: "🏠",
    phrases: [
      { en: "I wake up early", mr: "હું લવકર ઊઠું છું", roman: "Huṃ lavakar ūṭhuṃ chhuṃ", hint: "" },
      { en: "I am going to work", mr: "હું કામે જાઉં છું", roman: "Huṃ kāmē jāuṃ chhuṃ", hint: "" },
      { en: "What are you doing?", mr: "તમે શું કરો છો?", roman: "Tame śuṃ karō chhō?", hint: "" },
      { en: "I don't understand", mr: "મને સમજાતું નથી", roman: "Mane samajātuṃ nathī", hint: "" },
      { en: "Please speak slowly", mr: "કૃપા કરીને ધીમે બોલો", roman: "Kṛpā karīnē dhīmē bōlō", hint: "" },
      { en: "How was your day?", mr: "તમારો દિવસ કેવો ગયો?", roman: "Tamārō divas kēvō gayō?", hint: "" },
      { en: "I need water", mr: "મને પાણી જોઈએ છે", roman: "Mane pāṇī jōīē chhe", hint: "" },
      { en: "Where do you live?", mr: "તમે ક્યાં રહો છો?", roman: "Tame kyaṃ rahō chhō?", hint: "" },
      { en: "I am tired", mr: "મને થાક લાગ્યો છે", roman: "Mane thāk lāgyō chhe", hint: "" },
      { en: "Good luck!", mr: "શુભેચ્છા!", roman: "Śubhēcchā!", hint: "" },
    ]
  },
  environment: {
    name: "Environment",
    color: "#276749",
    icon: "🌿",
    phrases: [
      { en: "Weather", mr: "હવામાન", roman: "Havāmān", hint: "" },
      { en: "It's hot", mr: "ગરમ છે", roman: "Garam chhe", hint: "" },
      { en: "It's cold", mr: "ઠંડું છે", roman: "Ṭhaṃḍuṃ chhe", hint: "" },
      { en: "It's raining", mr: "વરસાદ પડે છે", roman: "Varasād paḍē chhe", hint: "" },
      { en: "Sun", mr: "સૂર્ય", roman: "Sūrya", hint: "" },
      { en: "Tree", mr: "ઝાડ", roman: "Jhāḍ", hint: "" },
      { en: "Flower", mr: "ફૂલ", roman: "Phūl", hint: "" },
      { en: "Nature", mr: "પ્રકૃતિ", roman: "Prakṛti", hint: "" },
      { en: "River", mr: "નદી", roman: "Nadī", hint: "" },
      { en: "Summer", mr: "ઉનાળો", roman: "Unāḷō", hint: "" },
      { en: "Winter", mr: "શિયાળો", roman: "Śiyāḷō", hint: "" },
      { en: "Rain", mr: "વરસાદ", roman: "Varasād", hint: "" },
    ]
  },
  health: {
    name: "Health",
    color: "#C53030",
    icon: "🏥",
    phrases: [
      { en: "Doctor", mr: "ડૉક્ટર", roman: "Ḍŏkṭar", hint: "" },
      { en: "Hospital", mr: "હોસ્પિટલ", roman: "Hōspiṭal", hint: "" },
      { en: "Medicine", mr: "દવા", roman: "Davā", hint: "" },
      { en: "I have fever", mr: "મને તાવ છે", roman: "Mane tāv chhe", hint: "" },
      { en: "I have pain", mr: "મને દરદ છે", roman: "Mane darad chhe", hint: "" },
      { en: "Where is the pharmacy?", mr: "દવાખાનું ક્યાં છે?", roman: "Davākhānuṃ kyaṃ chhe?", hint: "" },
      { en: "Take this medicine", mr: "આ દવા લો", roman: "Ā davā lō", hint: "" },
      { en: "I need a doctor", mr: "મારે ડૉક્ટર જોઈએ છે", roman: "Mārē ḍŏkṭar jōīē chhe", hint: "" },
      { en: "Headache", mr: "ડોકમાં દરદ", roman: "Ḍōkamāṃ darad", hint: "" },
      { en: "Stomach ache", mr: "પેટમાં દરદ", roman: "Pēṭamāṃ darad", hint: "" },
    ]
  },
  schoolWork: {
    name: "School & Work",
    color: "#2B6CB0",
    icon: "💼",
    phrases: [
      { en: "School", mr: "શાળા", roman: "Śāḷā", hint: "" },
      { en: "Teacher", mr: "શિક્ષક", roman: "Śikṣak", hint: "" },
      { en: "Student", mr: "વિદ્યાર્થી", roman: "Vidyārthī", hint: "" },
      { en: "Office", mr: "ઓફિસ", roman: "Ōphis", hint: "" },
      { en: "Meeting", mr: "બેઠક", roman: "Bēṭhak", hint: "" },
      { en: "What is the homework?", mr: "હોમવર્ક શું છે?", roman: "Hōmavark śuṃ chhe?", hint: "" },
      { en: "I have a meeting", mr: "મારી બેઠક છે", roman: "Mārī bēṭhak chhe", hint: "" },
      { en: "Where is the manager?", mr: "મેનેજર ક્યાં છે?", roman: "Mēnējar kyaṃ chhe?", hint: "" },
      { en: "Exam", mr: "પરીક્ષા", roman: "Parīkṣā", hint: "" },
      { en: "I don't understand", mr: "મને સમજાતું નથી", roman: "Mane samajātuṃ nathī", hint: "" },
    ]
  },
  socialInteractions: {
    name: "Social Interactions",
    color: "#9F7AEA",
    icon: "👥",
    phrases: [
      { en: "How are you?", mr: "તમે કેમ છો?", roman: "Tame kēm chhō?", hint: "" },
      { en: "What's going on?", mr: "શું ચાલે છે?", roman: "Śuṃ cālē chhe?", hint: "" },
      { en: "I am fine", mr: "હું ઠીક છું", roman: "Huṃ ṭhīk chhuṃ", hint: "" },
      { en: "Nice to meet you", mr: "તમને મળીને આનંદ થયો", roman: "Tamne maḷīnē ānand thayō", hint: "" },
      { en: "See you later", mr: "પછી મળીશું", roman: "Pachī maḷīśuṃ", hint: "" },
      { en: "Take care", mr: "કાળજી રાખો", roman: "Kāḷajī rākhō", hint: "" },
      { en: "Congratulations!", mr: "અભિનંદન!", roman: "Abhinandan!", hint: "" },
      { en: "Welcome", mr: "સ્વાગત છે", roman: "Svāgat chhe", hint: "" },
      { en: "Excuse me", mr: "માફ કરજો", roman: "Māf karajō", hint: "" },
      { en: "Can you help me?", mr: "તમે મને મદદ કરી શકો છો?", roman: "Tame mane madad karī śakō chhō?", hint: "" },
    ]
  },
  time: {
    name: "Time",
    color: "#3182CE",
    icon: "🕐",
    phrases: [
      { en: "What time is it?", mr: "કેટલા વાગ્યા?", roman: "Keṭalā vāgyā?", hint: "" },
      { en: "Today", mr: "આજે", roman: "Ājē", hint: "" },
      { en: "Tomorrow", mr: "આવતીકાલે", roman: "Āvatīkālē", hint: "" },
      { en: "Yesterday", mr: "ગઈકાલે", roman: "Gaīkālē", hint: "" },
      { en: "Morning", mr: "સવાર", roman: "Savār", hint: "" },
      { en: "Evening", mr: "સાંજ", roman: "Sāñj", hint: "" },
      { en: "Night", mr: "રાત્રી", roman: "Rātrī", hint: "" },
      { en: "Monday", mr: "સોમવાર", roman: "Sōmavār", hint: "" },
      { en: "Week", mr: "અઠવાડિયું", roman: "Aṭhavaḍiyuṃ", hint: "" },
      { en: "When?", mr: "ક્યારે?", roman: "Kyārē?", hint: "" },
    ]
  },
  tourism: {
    name: "Tourism",
    color: "#D69E2E",
    icon: "🗺️",
    phrases: [
      { en: "Where is this place?", mr: "આ જગ્યા ક્યાં છે?", roman: "Ā jagyā kyaṃ chhe?", hint: "" },
      { en: "Where is the bathroom?", mr: "બાથરૂમ ક્યાં છે?", roman: "Bātharūm kyaṃ chhe?", hint: "" },
      { en: "I am a tourist", mr: "હું પ્રવાસી છું", roman: "Huṃ pravāsī chhuṃ", hint: "" },
      { en: "Take a photo please", mr: "કૃપા કરીને ફોટો લો", roman: "Kṛpā karīnē phōṭō lō", hint: "" },
      { en: "The food was delicious", mr: "જમવું સ્વાદિષ્ટ હતું", roman: "Jamavuṃ svādiṣṭ hatuṃ", hint: "" },
      { en: "Where can I stay?", mr: "મને ક્યાં રહી શકાય?", roman: "Mane kyaṃ rahī śakāy?", hint: "" },
      { en: "Hotel", mr: "હોટેલ", roman: "Hōṭēl", hint: "" },
      { en: "Beautiful place", mr: "સુંદર જગ્યા", roman: "Suṃdar jagyā", hint: "" },
      { en: "I need help", mr: "મારે મદદ જોઈએ છે", roman: "Mārē madad jōīē chhe", hint: "" },
      { en: "Goodbye", mr: "આવજો", roman: "Āvajō", hint: "" },
    ]
  },
  transportation: {
    name: "Transportation",
    color: "#2D3748",
    icon: "🚌",
    phrases: [
      { en: "Bus", mr: "બસ", roman: "Bas", hint: "" },
      { en: "Train", mr: "ટ્રેન", roman: "Ṭrēn", hint: "" },
      { en: "Ticket", mr: "ટિકિટ", roman: "Ṭikiṭ", hint: "" },
      { en: "When is the next bus?", mr: "આગળની બસ ક્યારે છે?", roman: "Āgaḷanī bas kyārē chhe?", hint: "" },
      { en: "How much is the fare?", mr: "ભાડું કેટલું છે?", roman: "Bhāḍuṃ keṭaluṃ chhe?", hint: "" },
      { en: "Where is the railway station?", mr: "રેલવે સ્ટેશન ક્યાં છે?", roman: "Rēlavē sṭēśan kyaṃ chhe?", hint: "" },
      { en: "I want a ticket to...", mr: "મારે ... માટે ટિકિટ જોઈએ છે", roman: "Mārē ... māṭē ṭikiṭ jōīē chhe", hint: "" },
      { en: "Does this bus go to...?", mr: "આ બસ ... જાય છે?", roman: "Ā bas ... jāy chhe?", hint: "" },
      { en: "Platform", mr: "પ્લેટફોર્મ", roman: "Plēṭphōrm", hint: "" },
      { en: "Ticket counter", mr: "ટિકિટ કાઉન્ટર", roman: "Ṭikiṭ kāunṭar", hint: "" },
    ]
  }
};

const GUJARATI_DICTIONARY = [
  { en: "Water", mr: "પાણી", roman: "Pāṇī" },
  { en: "Food", mr: "ખોરાક", roman: "Khōrāk" },
  { en: "House", mr: "ઘર", roman: "Ghar" },
  { en: "Road", mr: "રસ્તો", roman: "Rastō" },
  { en: "Money", mr: "પૈસા", roman: "Paisā" },
  { en: "Time", mr: "સમય", roman: "Samay" },
  { en: "Day", mr: "દિવસ", roman: "Divas" },
  { en: "Night", mr: "રાત્રી", roman: "Rātrī" },
  { en: "Mother", mr: "મા", roman: "Mā" },
  { en: "Father", mr: "બાપુ", roman: "Bāpu" },
  { en: "Brother", mr: "ભાઈ", roman: "Bhāī" },
  { en: "Sister", mr: "બહેન", roman: "Bahēn" },
  { en: "Friend", mr: "મિત્ર", roman: "Mitra" },
  { en: "School", mr: "શાળા", roman: "Śāḷā" },
  { en: "Work", mr: "કામ", roman: "Kām" },
  { en: "City", mr: "શહેર", roman: "Śahēr" },
  { en: "Village", mr: "ગામ", roman: "Gām" },
  { en: "Morning", mr: "સવાર", roman: "Savār" },
  { en: "Evening", mr: "સાંજ", roman: "Sāñj" },
  { en: "Today", mr: "આજે", roman: "Ājē" },
  { en: "Tomorrow", mr: "આવતીકાલે", roman: "Āvatīkālē" },
  { en: "Yesterday", mr: "ગઈકાલે", roman: "Gaīkālē" },
  { en: "Yes", mr: "હા", roman: "Hā" },
  { en: "No", mr: "ના", roman: "Nā" },
  { en: "Good", mr: "સારું", roman: "Sāruṃ" },
  { en: "Bad", mr: "ખરાબ", roman: "Kharāb" },
  { en: "Big", mr: "મોટું", roman: "Mōṭuṃ" },
  { en: "Small", mr: "છોટું", roman: "Chhōṭuṃ" },
  { en: "Hot", mr: "ગરમ", roman: "Garam" },
  { en: "Cold", mr: "ઠંડું", roman: "Ṭhaṃḍuṃ" },
];

const LANGUAGES = {
  marathi: {
    name: "Marathi",
    code: "mr",
    subtitle: "मराठी शिका",
    scriptFont: "'Noto Sans Devanagari', sans-serif",
    speechLang: "mr-IN",
    dataSource: "learnmarathiwithkaushik.com",
    hasLessons: true,
    dataFile: "data.json",
    structureFile: "lessons_structure.json",
    PHRASES: PHRASES,
    DICTIONARY: DICTIONARY
  },
  gujarati: {
    name: "Gujarati",
    code: "gu",
    subtitle: "ગુજરાતી શીખો",
    scriptFont: "'Noto Sans Gujarati', sans-serif",
    speechLang: "gu-IN",
    dataSource: "learnmarathiwithkaushik.com",
    hasLessons: true,
    dataFile: "data_gujarati.json",
    structureFile: "lessons_structure_gujarati.json",
    PHRASES: GUJARATI_PHRASES,
    DICTIONARY: GUJARATI_DICTIONARY
  }
};

// ===== STATE =====
let currentTab = 'home';
let currentCategory = null;
let previousScreen = 'home';
let expandedCategory = null;
let lastSearchResults = [];
let savedPhrases = [];
let currentPhrase = null;
let savedLessons = [];
let currentChapterId = null;

function loadSavedPhrases() {
  const key = 'savedPhrases_' + (selectedLanguage || 'marathi');
  savedPhrases = JSON.parse(localStorage.getItem(key) || '[]');
}
function saveSavedPhrases() {
  const key = 'savedPhrases_' + (selectedLanguage || 'marathi');
  localStorage.setItem(key, JSON.stringify(savedPhrases));
}

function loadSavedLessons() {
  const key = 'savedLessons_' + (selectedLanguage || 'marathi');
  savedLessons = JSON.parse(localStorage.getItem(key) || '[]');
}
function saveSavedLessons() {
  const key = 'savedLessons_' + (selectedLanguage || 'marathi');
  localStorage.setItem(key, JSON.stringify(savedLessons));
}

// ===== NAVIGATION =====

function openPhrase(cat, idx) {
  const p = getPHRASES()[cat].phrases[idx];
  currentPhrase = p;
  previousScreen = currentTab === 'home' ? 'home' : currentTab;

  document.getElementById('result-input-display').textContent = p.en;
  document.getElementById('result-devanagari').textContent = p.mr;
  document.getElementById('result-roman').textContent = p.roman;

  const saveBtn = document.getElementById('save-btn');
  const isSaved = savedPhrases.some(s => s.mr === p.mr);
  saveBtn.className = 'save-btn phrase-save-btn phrase-save-btn-icon' + (isSaved ? ' saved' : '');

  // Similar phrases from same category
  const phrases = getPHRASES()[cat].phrases;
  const similar = phrases.filter((_, i) => i !== idx).slice(0, 3);
  document.getElementById('similar-phrases').innerHTML = similar.map((sp) => `
    <div class="phrase-item" onclick="openPhrase('${cat}', ${phrases.indexOf(sp)})">
      <div class="phrase-item-left">
        <div class="phrase-en">${sp.en}</div>
        <div class="phrase-roman">${sp.roman}</div>
      </div>
      <span class="phrase-arrow">›</span>
    </div>
  `).join('');

  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById('screen-result').classList.add('active');
}

function goBack() {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById('screen-home').classList.add('active');
}

function goBackFromResult() {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById('screen-' + (previousScreen || 'home')).classList.add('active');
}

// ===== SEARCH =====
function handleHomeSearch(val) {
  const resultsArea = document.getElementById('search-results-area');
  const categoriesArea = document.getElementById('categories-area');
  const resultsList = document.getElementById('search-results-list');

  if (!val.trim()) {
    resultsArea.style.display = 'none';
    categoriesArea.style.display = 'block';
    return;
  }

  resultsArea.style.display = 'block';
  categoriesArea.style.display = 'none';

  const query = val.toLowerCase();
  let results = [];

  Object.entries(getPHRASES()).forEach(([cat, data]) => {
    data.phrases.forEach((p, i) => {
      if (p.en.toLowerCase().includes(query) || p.roman.toLowerCase().includes(query) || p.mr.includes(val)) {
        results.push({ cat, idx: i, phrase: p });
      }
    });
  });

  getDICTIONARY().forEach(d => {
    if (d.en.toLowerCase().includes(query) || d.roman.toLowerCase().includes(query)) {
      results.push({ dict: true, phrase: d });
    }
  });

  if (!results.length) {
    resultsList.innerHTML = '<div class="no-results">No results found for "' + val + '"</div>';
    return;
  }

  lastSearchResults = results.slice(0, 15);
  const speakerSvg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>';
  const bookmarkSvg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m19 21-7-4-7 4V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>';
  resultsList.innerHTML = lastSearchResults.map((r, ri) => {
    const isSaved = savedPhrases.some(s => s.mr === r.phrase.mr);
    return `
    <div class="phrase-row phrase-row-flat">
      <div class="phrase-row-text">
        <span class="phrase-en">${r.phrase.en}</span>
        <span class="phrase-roman">${r.phrase.roman}</span>
        <span class="phrase-mr" style="font-family:${getScriptFont()}">${r.phrase.mr}</span>
      </div>
      <div class="phrase-row-actions">
        <button class="phrase-save-btn phrase-save-btn-icon ${isSaved ? 'saved' : ''}" onclick="event.stopPropagation(); ${r.dict ? `saveSearchPhraseInline(${ri})` : `savePhraseInline('${r.cat}', ${r.idx})`}" title="Bookmark">${bookmarkSvg}</button>
        <button class="phrase-speaker-btn" onclick="event.stopPropagation(); ${r.dict ? `speakSearchPhrase(${ri})` : `speakPhrase('${r.cat}', ${r.idx})`}" title="Pronounce">${speakerSvg}</button>
      </div>
    </div>
    `;
  }).join('');
}

// ===== DICTIONARY =====
let lastDictItems = [];

function speakDictItem(i) {
  const d = lastDictItems[i];
  if (!d || !d.mr || !('speechSynthesis' in window)) return;
  const utt = new SpeechSynthesisUtterance(d.mr);
  utt.lang = getLang().speechLang;
  utt.rate = 0.85;
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(utt);
  showToast('Playing...');
}

function saveDictItem(i) {
  const d = lastDictItems[i];
  if (!d) return;
  const isSaved = savedPhrases.some(s => s.mr === d.mr);
  if (isSaved) {
    savedPhrases = savedPhrases.filter(s => s.mr !== d.mr);
    showToast('Removed from saved');
  } else {
    savedPhrases.push(d);
    showToast('Phrase saved!');
  }
  saveSavedPhrases();
  renderDict(document.getElementById('dict-search').value);
}

function renderDict(query) {
  const list = document.getElementById('dict-list');
  const q = (query || '').toLowerCase();
  lastDictItems = q
    ? getDICTIONARY().filter(d => d.en.toLowerCase().includes(q) || d.roman.toLowerCase().includes(q))
    : getDICTIONARY();

  const speakerSvg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>';
  const bookmarkSvg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m19 21-7-4-7 4V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>';
  list.innerHTML = lastDictItems.map((d, i) => {
    const isSaved = savedPhrases.some(s => s.mr === d.mr);
    return `
    <div class="phrase-row phrase-row-flat dict-row">
      <div class="phrase-row-text">
        <span class="phrase-en">${d.en}</span>
        <span class="phrase-roman">${d.roman}</span>
        <span class="phrase-mr" style="font-family:${getScriptFont()}">${d.mr}</span>
      </div>
      <div class="phrase-row-actions">
        <button class="phrase-save-btn phrase-save-btn-icon ${isSaved ? 'saved' : ''}" onclick="event.stopPropagation(); saveDictItem(${i})" title="Bookmark">${bookmarkSvg}</button>
        <button class="phrase-speaker-btn" onclick="event.stopPropagation(); speakDictItem(${i})" title="Pronounce">${speakerSvg}</button>
      </div>
    </div>
    `;
  }).join('');
}

function handleDictSearch(val) { renderDict(val); }

// ===== SAVED =====
function savePhrase() {
  if (!currentPhrase) return;
  const isSaved = savedPhrases.some(s => s.mr === currentPhrase.mr);
  if (isSaved) {
    savedPhrases = savedPhrases.filter(s => s.mr !== currentPhrase.mr);
    showToast('Removed from saved');
    document.getElementById('save-btn').className = 'save-btn phrase-save-btn phrase-save-btn-icon';
  } else {
    savedPhrases.push(currentPhrase);
    showToast('Phrase saved!');
    document.getElementById('save-btn').className = 'save-btn phrase-save-btn phrase-save-btn-icon saved';
  }
  saveSavedPhrases();
}

function speakSavedPhrase(i) {
  const p = savedPhrases[i];
  if (!p || !p.mr || !('speechSynthesis' in window)) return;
  const utt = new SpeechSynthesisUtterance(p.mr);
  utt.lang = getLang().speechLang;
  utt.rate = 0.85;
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(utt);
  showToast('Playing...');
}

function removeSavedPhrase(i) {
  savedPhrases.splice(i, 1);
  saveSavedPhrases();
  renderSaved();
  showToast('Removed from saved');
}

function removeSavedLesson(i) {
  savedLessons.splice(i, 1);
  saveSavedLessons();
  renderSaved();
  showToast('Removed from saved');
}

async function openSavedLesson(chapterId) {
  if (!chaptersLoaded || chaptersLoadedForLang !== selectedLanguage) {
    await loadChapters();
  }
  if (chaptersById[chapterId]) openChapter(chapterId);
}

function renderSaved() {
  const wrap = document.getElementById('saved-list-wrap');
  const hasPhrases = savedPhrases.length > 0;
  const hasLessons = savedLessons.length > 0;
  if (!hasPhrases && !hasLessons) {
    wrap.innerHTML = `
      <div class="empty-state">
        <div class="empty-icon"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="m19 21-7-4-7 4V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg></div>
        <div class="empty-title">No saved items yet</div>
        <div class="empty-sub">Tap the bookmark icon on any phrase or lesson to save it here</div>
      </div>`;
    return;
  }
  const speakerSvg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>';
  let html = '<div style="padding: 0 20px; display: flex; flex-direction: column; gap: 16px;">';
  if (hasLessons) {
    html += '<div class="section-label">Saved Lessons</div>';
    html += '<div class="phrase-list saved-list" style="display: flex; flex-direction: column; gap: 10px;">';
    html += savedLessons.map((l, i) => `
      <div class="phrase-row phrase-row-flat chapter-saved-row" onclick="openSavedLesson(${l.id})">
        <div class="phrase-row-text">
          <span class="phrase-en">${l.title}</span>
          <span class="phrase-roman" style="font-size:11px;color:var(--text-muted);">Lesson</span>
        </div>
        <div class="phrase-row-actions">
          <button class="phrase-save-btn saved" onclick="event.stopPropagation(); removeSavedLesson(${i})">Remove</button>
        </div>
      </div>`).join('');
    html += '</div>';
  }
  if (hasPhrases) {
    html += '<div class="section-label">Saved Phrases</div>';
    html += '<div class="phrase-list saved-list" style="display: flex; flex-direction: column; gap: 10px;">';
    html += savedPhrases.map((p, i) => `
      <div class="phrase-row phrase-row-flat">
        <div class="phrase-row-text">
          <span class="phrase-en">${p.en}</span>
          <span class="phrase-roman">${p.roman}</span>
          <span class="phrase-mr" style="font-family:${getScriptFont()}">${p.mr}</span>
        </div>
        <div class="phrase-row-actions">
          <button class="phrase-save-btn saved" onclick="event.stopPropagation(); removeSavedPhrase(${i})">Remove</button>
          <button class="phrase-speaker-btn" onclick="event.stopPropagation(); speakSavedPhrase(${i})" title="Pronounce">${speakerSvg}</button>
        </div>
      </div>`).join('');
    html += '</div>';
  }
  html += '</div>';
  wrap.innerHTML = html;
}

// ===== SPEAK =====
function speakMarathi() {
  if (!currentPhrase) return;
  if ('speechSynthesis' in window) {
    const utt = new SpeechSynthesisUtterance(currentPhrase.mr);
    utt.lang = getLang().speechLang;
    utt.rate = 0.85;
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(utt);
    showToast('Playing...');
  } else {
    showToast('Speech not supported on this device');
  }
}

// ===== SETTINGS =====
let offlineEnabled = true;
function toggleOffline() {
  offlineEnabled = !offlineEnabled;
  const t = document.getElementById('offline-toggle');
  t.className = 'toggle' + (offlineEnabled ? '' : ' off');
  showToast(offlineEnabled ? 'Offline mode enabled' : 'Offline mode disabled');
}

// ===== FEEDBACK =====
// Paste your Google Apps Script Web App URL here after deploying (see google-apps-script/Code.gs)
const FEEDBACK_SHEET_URL = 'https://script.google.com/macros/s/AKfycbwuQVHBxBaDLohbvFg1Ux_eqWEiRmJORTgOZUEZ0N_SqKEMLCqE8YQDcGgkbl1bj60/exec'; // e.g. 'https://script.google.com/macros/s/XXXXX/exec'

function openFeedback() {
  const overlay = document.getElementById('feedback-overlay');
  const form = document.getElementById('feedback-form');
  if (overlay) {
    overlay.classList.add('show');
    form?.reset();
    document.querySelectorAll('input[name="rating"]').forEach(r => r.checked = false);
    document.addEventListener('keydown', feedbackEscapeHandler);
  }
}

function feedbackEscapeHandler(e) {
  if (e.key === 'Escape') {
    closeFeedbackModal();
    document.removeEventListener('keydown', feedbackEscapeHandler);
  }
}

function closeFeedbackModal(e) {
  if (e && e.target !== e.currentTarget) return;
  document.getElementById('feedback-overlay')?.classList.remove('show');
  document.removeEventListener('keydown', feedbackEscapeHandler);
}

function submitFeedback(e) {
  e.preventDefault();
  const typeEl = document.getElementById('feedback-type');
  const ratingEl = document.querySelector('input[name="rating"]:checked');
  const messageEl = document.getElementById('feedback-message');
  const emailEl = document.getElementById('feedback-email');
  const submitBtn = document.getElementById('feedback-submit');

  const type = typeEl?.value || '';
  const rating = ratingEl?.value || '';
  const message = messageEl?.value?.trim() || '';
  const email = emailEl?.value?.trim() || '';

  if (!type || !rating) {
    showToast('Please select type and rating');
    return;
  }

  if (!FEEDBACK_SHEET_URL) {
    showToast('Google Sheet not connected. See setup in google-apps-script folder.');
    return;
  }

  submitBtn.disabled = true;
  submitBtn.textContent = 'Sending...';

  // Use form POST to iframe - avoids CORS (form submissions are not restricted by CORS)
  const iframe = document.createElement('iframe');
  iframe.name = 'feedback-frame-' + Date.now();
  iframe.style.cssText = 'position:absolute;width:0;height:0;border:0;visibility:hidden';
  document.body.appendChild(iframe);

  const form = document.createElement('form');
  form.method = 'POST';
  form.action = FEEDBACK_SHEET_URL;
  form.target = iframe.name;
  form.style.display = 'none';

  const fields = {
    type, rating, message, email,
    language: getLang().name || 'Marathi',
    version: '1.0.0'
  };
  for (const [k, v] of Object.entries(fields)) {
    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = k;
    input.value = String(v);
    form.appendChild(input);
  }
  document.body.appendChild(form);

  iframe.onload = function() {
    iframe.onload = null;
    setTimeout(function() {
      form.remove();
      iframe.remove();
      closeFeedbackModal();
      showToast('Thank you! Feedback sent.');
      submitBtn.disabled = false;
      submitBtn.textContent = 'Submit';
    }, 300);
  };
  // Fallback if onload never fires (e.g. network error)
  setTimeout(function() {
    if (iframe.parentNode) {
      form.remove();
      iframe.remove();
      submitBtn.disabled = false;
      submitBtn.textContent = 'Submit';
      showToast('Thank you! Feedback sent.');
    }
  }, 8000);

  form.submit();
}

// ===== THEME =====
function setTheme(themeId, silent) {
  themeId = themeId || 'teal';
  document.body.setAttribute('data-theme', themeId);
  localStorage.setItem('appTheme', themeId);
  document.querySelectorAll('.theme-swatch').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-theme') === themeId);
  });
  if (!silent) showToast('Theme updated');
}
function initTheme() {
  const saved = localStorage.getItem('appTheme') || 'teal';
  setTheme(saved, true);
  document.getElementById('theme-options')?.addEventListener('click', (e) => {
    const btn = e.target.closest('.theme-swatch');
    if (btn) setTheme(btn.getAttribute('data-theme'));
  });
}

// ===== TOAST =====
function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2200);
}


// ===== CHAPTERS (hierarchical: lessons_structure.json + data.json) =====
let allChapters = [];
let chaptersById = {};
let lessonsStructure = null;
let chaptersLoaded = false;
let chaptersLoadedForLang = ''; // which language's chapters are loaded
let expandedMajorLesson = null; // major lesson name when expanded
let expandedChapter = null; // chapter id when sublesson content expanded

// Busuu-style formatted lessons (chapterId -> structured content)
const BUSUU_FORMATTED_LESSONS = {
  22: {
    intro: 'Consider sentences: Do you go? Did he go? Will she speak? These are all basic questions in English. In Marathi, basic questions can be formed by adding **का (kA)**. By appending का (kA) to a statement, it will be converted to a question.',
    sections: [
      {
        heading: 'Forming questions with का (kA)',
        intro: 'Adding का (kA) at the end of a sentence turns it into a question.',
        examples: [
          { roman: 'to jAto', script: 'तो जातो', en: 'He goes' },
          { roman: 'to jAto kA ?', script: 'तो जातो का?', en: 'Does he go?' },
          { roman: 'tI gelI', script: 'ती गेली', en: 'She went' },
          { roman: 'tI gelI kA ?', script: 'ती गेली का?', en: 'Did she go?' },
          { roman: 'te jAtIl', script: 'ते जातील', en: 'They will go' },
          { roman: 'te jAtIl kA ?', script: 'ते जातील का?', en: 'Will they go?' }
        ]
      },
      {
        heading: 'Questions by tone',
        intro: 'Such questions can also be asked by using the same sentence but just changing the tone. In English we do this sometimes too.',
        examples: [
          { roman: 'tU yeto Ahes', script: 'तू येतो आहेस', en: 'You are coming' },
          { roman: 'tU tyAlA rahasy sAMgitales', script: 'तू त्याला रहस्य सांगितलेस', en: 'You told him the secret' }
        ]
      }
    ]
  },
  228: {
    intro: 'Let\'s learn basic Marathi sentence formation. In English the verb "To Be" has special significance. Its different forms are used along with other verbs to indicate tense. The same is the case in Marathi. "To Be" in English is **असणे (asaNe)** in Marathi.',
    sections: [
      {
        heading: 'Affirmative sentences',
        intro: 'In English "am", "are", "is" are different forms of "To be" for different pronouns. Similarly, in Marathi there are different forms of असणे (asaNe). A sentence in Marathi can be formed as:',
        examples: [
          { roman: 'mI Ahe', script: 'मी आहे', en: 'I am' },
          { roman: 'tumhI AhAt', script: 'तुम्ही आहात', en: 'You are' },
          { roman: 'te Ahet', script: 'ते आहेत', en: 'They are' },
          { roman: 'AmhI / ApaN Ahot', script: 'आम्ही/आपण आहोत', en: 'We are' }
        ]
      },
      {
        heading: 'More examples',
        intro: 'The form of असणे (asaNe) changes based on the pronoun. Here are more examples:',
        examples: [
          { roman: 'to Ahe', script: 'तो आहे', en: 'He is' },
          { roman: 'tI Ahe', script: 'ती आहे', en: 'She is' },
          { roman: 'te Ahe', script: 'ते आहे', en: 'It is' },
          { roman: 'tU Ahes', script: 'तू आहेस', en: 'You are (singular)' }
        ]
      }
    ]
  }
};

function speakLessonPhrase(text) {
  if (!text || !('speechSynthesis' in window)) return;
  const utt = new SpeechSynthesisUtterance(text);
  utt.lang = getLang().speechLang || 'hi-IN';
  utt.rate = 0.85;
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(utt);
  showToast('Playing...');
}

function formatChapterFromData(ch) {
  if (!ch) return null;
  const hasBlocks = ch.blocks && ch.blocks.length;
  const hasTables = ch.tables && ch.tables.length;
  if (!hasBlocks && !hasTables) return null;

  const escape = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  const bold = (t) => escape(t).replace(/\*\*(.+?)\*\*/g, (_, x) => '<strong>' + escape(x) + '</strong>');

  const isAlphabetTable = (tbl) => {
    const headers = tbl.headers || [];
    const rows = tbl.rows || [];
    if (headers.length !== 2 || rows.length === 0) return false;
    const hStr = (headers[0] + ' ' + headers[1]).toLowerCase();
    if (!/letter|transliteration|sound|character/.test(hStr)) return false;
    return rows.every(r => Array.isArray(r) && r.length >= 2 && /[\u0900-\u097F]/.test(String(r[0])));
  };

  const renderAlphabetGrid = (tbl) => {
    const rows = tbl.rows || [];
    const heading = (tbl.heading || '').toLowerCase();
    const isBarakhadi = /barakhadi|barakahadi/.test(heading);
    let cols = heading.includes('vowel') ? 4 : 5;
    if (isBarakhadi) cols = 15;
    const compactClass = isBarakhadi ? ' alphabet-grid--barakhadi' : '';
    let h = '<h3 class="busuu-section-heading">' + escape(tbl.heading) + '</h3>';
    h += '<div class="alphabet-grid' + compactClass + '" style="--grid-cols:' + cols + '">';
    rows.forEach(row => {
      const letter = row[0] || '';
      const roman = row[1] || '';
      const textToSpeak = (roman || letter).trim();
      const dataSpeak = textToSpeak ? ' data-speak="' + escape(textToSpeak) + '"' : '';
      h += '<div class="alphabet-card">';
      h += '<span class="alphabet-script">' + escape(letter) + '</span>';
      h += '<span class="alphabet-roman">' + escape(roman) + '</span>';
      h += '<span class="alphabet-line"></span>';
      h += '<button type="button" class="alphabet-audio-btn"' + dataSpeak + ' onclick="var t=this.getAttribute(\'data-speak\');if(t)speakLessonPhrase(t)" title="Listen" aria-label="Play audio"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg></button>';
      h += '</div>';
    });
    h += '</div>';
    return h;
  };

  const renderTable = (tbl) => {
    if (isAlphabetTable(tbl)) return renderAlphabetGrid(tbl);
    let h = '<h3 class="busuu-section-heading">' + escape(tbl.heading) + '</h3>';
    h += '<div class="busuu-table-wrap"><table class="busuu-table">';
    h += '<thead><tr>';
    (tbl.headers || []).forEach(hd => { h += '<th>' + escape(hd) + '</th>'; });
    if (tbl.speakCol != null) h += '<th></th>';
    h += '</tr></thead><tbody>';
    const speakCol = tbl.speakCol != null ? tbl.speakCol : -1;
    (tbl.rows || []).forEach(row => {
      h += '<tr>';
      row.forEach((cell, i) => {
        const cls = i === 0 && /[\u0900-\u097F]/.test(cell) ? ' class="busuu-script-cell"' : '';
        h += '<td' + cls + '>' + escape(cell) + '</td>';
      });
      if (speakCol >= 0 && row[speakCol]) {
        const textToSpeak = escape(String(row[speakCol]));
        h += '<td class="busuu-table-audio"><button type="button" class="busuu-audio-btn" data-speak="' + textToSpeak + '" onclick="speakLessonPhrase(this.getAttribute(\'data-speak\'))" title="Listen" aria-label="Play audio"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg></button></td>';
      }
      h += '</tr>';
    });
    h += '</tbody></table></div>';
    return h;
  };

  let html = '<div class="busuu-lesson">';
  if (ch.intro) html += '<p class="busuu-intro">' + bold(ch.intro) + '</p>';

  if (hasBlocks) {
    ch.blocks.forEach(blk => {
      if (blk.type === 'table') html += renderTable(blk);
      else if (blk.type === 'paragraph') {
        html += '<h3 class="busuu-section-heading">' + escape(blk.heading || '') + '</h3>';
        html += '<p class="busuu-para">' + bold(blk.content || '').replace(/\n/g, '<br>') + '</p>';
      }
    });
  } else {
    ch.tables.forEach(tbl => { html += renderTable(tbl); });
  }
  html += '</div>';
  return html;
}

function formatChapterContentBusuu(chapterId) {
  const data = BUSUU_FORMATTED_LESSONS[chapterId];
  if (!data) return null;
  const escape = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  const bold = (t) => escape(t).replace(/\*\*(.+?)\*\*/g, (_, x) => '<strong>' + escape(x) + '</strong>');
  let html = '<div class="busuu-lesson">';
  if (data.intro) html += '<p class="busuu-intro">' + bold(data.intro) + '</p>';

  if (data.tables) {
    data.tables.forEach(tbl => {
      html += '<h3 class="busuu-section-heading">' + escape(tbl.heading) + '</h3>';
      html += '<div class="busuu-table-wrap"><table class="busuu-table">';
      html += '<thead><tr>';
      (tbl.headers || []).forEach(h => { html += '<th>' + escape(h) + '</th>'; });
      html += '</tr></thead><tbody>';
      (tbl.rows || []).forEach(row => {
        html += '<tr>';
        row.forEach((cell, i) => {
          const cls = i === 0 && /[\u0900-\u097F]/.test(cell) ? ' class="busuu-script-cell"' : '';
          html += '<td' + cls + '>' + escape(cell) + '</td>';
        });
        html += '</tr>';
      });
      html += '</tbody></table></div>';
    });
  } else {
    (data.sections || []).forEach(sec => {
      html += '<h3 class="busuu-section-heading">' + escape(sec.heading) + '</h3>';
      if (sec.intro) html += '<p class="busuu-section-intro">' + bold(sec.intro) + '</p>';
      html += '<div class="busuu-examples">';
      (sec.examples || []).forEach(ex => {
        const textToSpeak = (ex.roman || ex.script || '').trim();
        const speakAttr = textToSpeak ? `onclick="speakLessonPhrase('${textToSpeak.replace(/'/g, "\\'")}')"` : '';
        html += '<div class="busuu-card">';
        html += '<div class="busuu-card-text">';
        if (ex.roman) html += '<span class="busuu-roman">' + escape(ex.roman) + '</span>';
        if (ex.script) html += ' <span class="busuu-script">/ ' + escape(ex.script) + '</span>';
        if (ex.en) html += ' <span class="busuu-en">(' + escape(ex.en) + ')</span>';
        html += '</div>';
        html += '<button type="button" class="busuu-audio-btn" ' + speakAttr + ' title="Listen" aria-label="Play audio"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg></button>';
        html += '</div>';
      });
      html += '</div>';
    });
  }
  html += '</div>';
  return html;
}

async function loadChapters() {
  const lang = getLang();
  if (!lang.hasLessons) {
    const list = document.getElementById('chapters-list');
    const loading = document.getElementById('chapters-loading');
    const error = document.getElementById('chapters-error');
    if (loading) loading.style.display = 'none';
    if (error) error.style.display = 'none';
    if (list) list.innerHTML = '<div class="empty-state"><div class="empty-title">Lessons coming soon</div><div class="empty-sub">Structured lessons for this language will be added later</div></div>';
    return;
  }
  const dataFile = lang.dataFile || 'data.json';
  const structureFile = lang.structureFile || 'lessons_structure.json';
  if (chaptersLoaded && chaptersLoadedForLang === selectedLanguage) return;

  const loading = document.getElementById('chapters-loading');
  const error   = document.getElementById('chapters-error');
  const list    = document.getElementById('chapters-list');

  loading.style.display = 'block';
  error.style.display   = 'none';
  list.innerHTML        = '';

  try {
    const [chaptersRes, structureRes] = await Promise.all([
      fetch(dataFile),
      fetch(structureFile)
    ]);
    if (!chaptersRes.ok) throw new Error(dataFile + ' not found');
    if (!structureRes.ok) throw new Error(structureFile + ' not found');
    allChapters = await chaptersRes.json();
    lessonsStructure = await structureRes.json();
    chaptersById = {};
    allChapters.forEach(ch => { chaptersById[ch.id] = ch; });
    chaptersLoaded = true;
    chaptersLoadedForLang = selectedLanguage;
    renderLessonsList();
  } catch(e) {
    loading.style.display = 'none';
    error.style.display   = 'block';
    document.getElementById('chapters-error').innerHTML = `
      <div class="error-icon" style="margin:0 auto 12px;"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg></div>
      <div style="font-weight:800;color:var(--text);margin-bottom:6px;">${e.message || 'Failed to load'}</div>
      <div style="font-size:12px;color:var(--text-muted);font-weight:600;">
        Ensure <code style="background:var(--border);padding:2px 6px;border-radius:4px;">data.json</code> and
        <code style="background:var(--border);padding:2px 6px;border-radius:4px;">lessons_structure.json</code> are in project root
      </div>`;
  }
}

function toggleMajorLesson(name) {
  if (expandedMajorLesson === name) {
    expandedMajorLesson = null;
    expandedChapter = null;
  } else {
    expandedMajorLesson = name;
    expandedChapter = null;
  }
  renderLessonsList();
}

function getChapterDisplayNumber(chapterId) {
  if (!lessonsStructure || !lessonsStructure.majorLessons) return chapterId;
  let n = 0;
  for (const major of lessonsStructure.majorLessons) {
    for (const s of major.sublessons || []) {
      n++;
      if (s.chapterId === chapterId) return n;
    }
  }
  return chapterId;
}

function openChapter(chapterId) {
  const ch = chaptersById[chapterId];
  if (!ch) return;
  currentChapterId = chapterId;
  const dataTablesHtml = (ch.tables || ch.blocks) ? formatChapterFromData(ch) : null;
  const busuuHtml = !dataTablesHtml && BUSUU_FORMATTED_LESSONS[chapterId] ? formatChapterContentBusuu(chapterId) : null;
  const formattedContent = dataTablesHtml || busuuHtml || formatChapterContent(ch.content || '');

  document.getElementById('chapter-detail-id').textContent = getChapterDisplayNumber(chapterId);
  document.getElementById('chapter-detail-title').textContent = ch.title;
  document.getElementById('chapter-detail-body').innerHTML = formattedContent;
  const linkEl = document.getElementById('chapter-detail-link');
  linkEl.href = ch.url || '#';
  linkEl.style.display = ch.url ? 'block' : 'none';

  const saveBtn = document.getElementById('chapter-save-btn');
  const saveBtnBottom = document.getElementById('chapter-save-btn-bottom');
  const isSaved = savedLessons.some(s => s.id === chapterId);
  [saveBtn, saveBtnBottom].forEach(btn => {
    if (btn) btn.classList.toggle('saved', isSaved);
  });

  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById('chapter-detail-loading').style.display = 'none';
  document.getElementById('chapter-detail-content').style.display = 'block';
  document.getElementById('screen-chapter-detail').classList.add('active');
}

function saveLesson() {
  if (currentChapterId == null) return;
  saveLessonInline(currentChapterId);
}

function saveLessonInline(chapterId) {
  const ch = chaptersById[chapterId];
  if (!ch) return;
  const isSaved = savedLessons.some(s => s.id === chapterId);
  if (isSaved) {
    savedLessons = savedLessons.filter(s => s.id !== chapterId);
    showToast('Removed from saved');
  } else {
    savedLessons.push({ id: chapterId, title: ch.title, url: ch.url || '' });
    showToast('Lesson saved!');
  }
  saveSavedLessons();
  if (currentTab === 'saved') renderSaved();
  // Update chapter detail save btns if this lesson is open
  if (currentChapterId === chapterId) {
    const isSavedNow = savedLessons.some(s => s.id === chapterId);
    [document.getElementById('chapter-save-btn'), document.getElementById('chapter-save-btn-bottom')].forEach(btn => {
      if (btn) btn.classList.toggle('saved', isSavedNow);
    });
  }
  renderLessonsList();
}

function goBackFromChapter() {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById('screen-chapters').classList.add('active');
}

function renderLessonsList() {
  const loading = document.getElementById('chapters-loading');
  const list    = document.getElementById('chapters-list');
  if (loading) loading.style.display = 'none';

  const q = (document.getElementById('chapters-search') || {}).value || '';
  const searchLower = q.trim().toLowerCase();

  if (!lessonsStructure || !lessonsStructure.majorLessons) {
    if (list) list.innerHTML = '<div class="no-results">No lessons found</div>';
    return;
  }

  const majorsToShow = lessonsStructure.majorLessons.filter(major => {
    if (!searchLower) return true;
    const hasMatch = (major.sublessons || []).some(s => {
      const ch = chaptersById[s.chapterId];
      return s.title.toLowerCase().includes(searchLower) ||
        (ch && (ch.title.toLowerCase().includes(searchLower) || (ch.content || '').toLowerCase().includes(searchLower)));
    });
    return hasMatch;
  });

  list.innerHTML = majorsToShow.map(major => {
    const isMajorExpanded = expandedMajorLesson === major.name;
    const sublessons = (major.sublessons || []).filter(s => {
      if (!searchLower) return true;
      const ch = chaptersById[s.chapterId];
      if (!ch) return s.title.toLowerCase().includes(searchLower);
      return s.title.toLowerCase().includes(searchLower) ||
        ch.title.toLowerCase().includes(searchLower) ||
        (ch.content || '').toLowerCase().includes(searchLower);
    });

    const sublessonsHtml = isMajorExpanded ? sublessons.map(s => {
      const ch = s.chapterId != null ? chaptersById[s.chapterId] : null;
      const hasContent = !!ch;
      const headerOnclick = hasContent ? `onclick="openChapter(${s.chapterId})"` : '';
      return `
      <div class="chapter-sub-row">
        <div class="chapter-row-header" ${headerOnclick}>
          <div class="chapter-row-title">${s.title}</div>
          ${hasContent ? '<span class="chapter-expand">→</span>' : ''}
        </div>
      </div>
      `;
    }).join('') : '';

    return `
    <div class="major-lesson-row">
      <div class="major-lesson-header" onclick="toggleMajorLesson('${major.name.replace(/'/g, "\\'")}')">
        <div class="major-lesson-name">${major.name}</div>
        <span class="chapter-expand">${isMajorExpanded ? '−' : '+'}</span>
      </div>
      ${isMajorExpanded && sublessons.length ? `
      <div class="major-lesson-sublessons">${sublessonsHtml}</div>
      ` : ''}
    </div>
    `;
  }).join('');
}

function handleChaptersSearch(val) {
  if (!chaptersLoaded) return;
  const q = (val || '').trim().toLowerCase();
  const majorsToShow = q ? lessonsStructure.majorLessons.filter(m => {
    return (m.sublessons || []).some(s => {
      const ch = chaptersById[s.chapterId];
      return s.title.toLowerCase().includes(q) ||
        (ch && (ch.title.toLowerCase().includes(q) || (ch.content || '').toLowerCase().includes(q)));
    });
  }) : lessonsStructure.majorLessons;
  if (expandedMajorLesson && !majorsToShow.some(m => m.name === expandedMajorLesson)) {
    expandedMajorLesson = null;
  }
  renderLessonsList();
}

function curateParagraph(text) {
  const skipStarts = ['please refer', 'refer to', 'http://', 'https://', 'copyright', 'developed by', 'download the', 'list is uploaded', 'previous lesson', 'next lesson', 'for grammar details'];
  const lower = text.toLowerCase().trim();
  if (skipStarts.some(s => lower.startsWith(s))) return '';
  const hasDevanagari = /[\u0900-\u097F]/.test(text);
  if (!hasDevanagari && text.length > 220) {
    const sentences = text.match(/[^.!?]+[.!?]+/g) || [text];
    return (sentences.slice(0, 2).join(' ').trim() || text.slice(0, 200) + '…').trim();
  }
  return text;
}

function formatChapterContent(content) {
  if (!content) return '';
  const escape = (s) => String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
  const bold = (t) => escape(t).replace(/\*\*(.+?)\*\*/g, (_, x) => '<strong>' + escape(x) + '</strong>');

  const examplePattern = /^([^:]*:?\s*)?([\u0900-\u097F\s\u200C\u200D]+)\(([a-zA-Z~A-Za-z0-9\s]+)\)\s*([–\-].*)?$/;
  const hasDevanagari = (s) => /[\u0900-\u097F]/.test(s);
  const renderCard = (ex) => {
    const textToSpeak = (ex.roman || ex.script || '').trim();
    const speakAttr = textToSpeak ? `onclick="speakLessonPhrase('${String(textToSpeak).replace(/'/g, "\\'")}')"` : '';
    let cardText = '';
    if (ex.label) cardText += '<span class="busuu-label">' + escape(ex.label) + '</span> ';
    cardText += '<span class="busuu-script">' + escape(ex.script) + '</span>';
    cardText += ' <span class="busuu-roman">(' + escape(ex.roman) + ')</span>';
    if (ex.extra) cardText += ' <span class="busuu-en">' + escape(ex.extra) + '</span>';
    return '<div class="busuu-card"><div class="busuu-card-text">' + cardText + '</div><button type="button" class="busuu-audio-btn" ' + speakAttr + ' title="Listen" aria-label="Play audio"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg></button></div>';
  };

  const blocks = content.split(/\n\s*\n/).filter(b => b.trim());
  let html = '<div class="busuu-lesson">';

  blocks.forEach(block => {
    const trimmed = block.trim();
    if (trimmed.startsWith('#### ')) {
      html += '<h4 class="busuu-section-heading busuu-h4">' + escape(trimmed.slice(5)) + '</h4>';
      return;
    }
    if (trimmed.startsWith('### ')) {
      html += '<h3 class="busuu-section-heading busuu-h3">' + escape(trimmed.slice(4)) + '</h3>';
      return;
    }
    if (trimmed.startsWith('## ')) {
      html += '<h2 class="busuu-section-heading">' + escape(trimmed.slice(3)) + '</h2>';
      return;
    }

    const lines = trimmed.split(/\n/).map(l => l.trim()).filter(l => l);
    const exampleLines = [];
    const paraLines = [];
    let prevLine = '';
    for (const line of lines) {
      const m = line.match(examplePattern);
      if (m && hasDevanagari(line)) {
        let label = (m[1] || '').trim();
        if (!label && prevLine && !hasDevanagari(prevLine) && prevLine.length < 80) {
          label = prevLine + ':';
          paraLines.pop();
        }
        const script = (m[2] || '').trim();
        const roman = (m[3] || '').trim();
        const extra = (m[4] || '').trim();
        if (script && roman) exampleLines.push({ label, script, roman, extra });
        prevLine = '';
      } else {
        paraLines.push(line);
        prevLine = line;
      }
    }

    if (paraLines.length) {
      const paraText = paraLines.map(curateParagraph).filter(Boolean).join('\n');
      if (paraText) html += '<p class="busuu-intro busuu-para">' + bold(paraText).replace(/\n/g, '<br>') + '</p>';
    }
    if (exampleLines.length) {
      html += '<div class="busuu-examples">';
      exampleLines.forEach(ex => { html += renderCard(ex); });
      html += '</div>';
    }
  });

  html += '</div>';
  return html;
}


function switchTab(tab) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  document.getElementById('screen-' + tab).classList.add('active');
  document.querySelectorAll('[data-tab="' + tab + '"]').forEach(n => n.classList.add('active'));
  currentTab = tab;

  if (tab === 'dictionary') renderDict('');
  if (tab === 'saved') renderSaved();
  if (tab === 'chapters') loadChapters();
}

// ===== INIT ON LOAD =====
function initApp() {
  initTheme();
  if (selectedLanguage && LANGUAGES[selectedLanguage]) {
    document.getElementById('screen-lang-select').classList.remove('active');
    document.getElementById('screen-lang-select').style.display = 'none';
    document.getElementById('app-content').style.display = 'block';
    document.body.classList.add('nav-visible');
    loadSavedPhrases();
    initLanguageUI();
    renderCategories();
    if (currentTab === 'dictionary') renderDict('');
    if (currentTab === 'saved') renderSaved();
  } else {
    document.getElementById('screen-lang-select').style.display = 'flex';
    document.getElementById('screen-lang-select').classList.add('active');
    document.getElementById('app-content').style.display = 'none';
    document.body.classList.remove('nav-visible');
  }
}

document.addEventListener('DOMContentLoaded', initApp);
