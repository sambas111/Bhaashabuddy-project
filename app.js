// ===== LANGUAGE SYSTEM =====
const CAT_INITIALS = {
  greetings: 'Hi',
  reading: 'Rd',
  writing: 'Wr',
  numbers: '#',
  animals: 'An',
  dailyLife: 'DL',
  environment: 'En',
  food: 'Fd',
  health: 'He',
  schoolWork: 'Sw',
  socialInteractions: 'So',
  time: 'Ti',
  tourism: 'To',
  transportation: 'Tr',
  travel: 'Go',
  shopping: 'Sh',
  emergency: '!',
  common: 'CP',
  body: 'Bd',
  family: 'Fm',
  home: 'Hm',
  nature: 'Na',
  colours: 'Cl',
  questions: 'Q?'
};
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
  transportation: 'https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=80&h=80&fit=crop',
  common: 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=80&h=80&fit=crop',
  body: 'https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=80&h=80&fit=crop',
  family: 'https://images.unsplash.com/photo-1511895426328-dc8714191300?w=80&h=80&fit=crop',
  home: 'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=80&h=80&fit=crop',
  nature: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=80&h=80&fit=crop',
  colours: 'https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=80&h=80&fit=crop',
  questions: 'https://images.unsplash.com/photo-1496200186974-4293800e2c20?w=80&h=80&fit=crop'
};
let selectedLanguage = localStorage.getItem('selectedLanguage') || '';

function getLang() {
  return LANGUAGES[selectedLanguage] || LANGUAGES.marathi;
}
function getPHRASES() { return getLang().PHRASES; }
function getDICTIONARY() {
  const d = getLang().DICTIONARY;
  if (Array.isArray(d)) return d;
  if (d && typeof d === 'object') {
    const flat = [];
    for (const sec of Object.values(d)) {
      if (sec && sec.words) flat.push(...sec.words);
    }
    return flat;
  }
  return [];
}
function getDICTIONARY_BY_SECTION() {
  const d = getLang().DICTIONARY;
  if (d && typeof d === 'object' && !Array.isArray(d)) return d;
  return null;
}
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
  expandedDictSection = null;
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
  const chSub = document.getElementById('chapters-subtitle');
  if (chSub) chSub.textContent = lang.dataSource;
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
    const baseId = id.split('_')[0]; // support Set 1/2/3 ids like greetings_1
    const iconUrl = CAT_IMAGES[id] || CAT_IMAGES[baseId] || '';
    const fallback = CAT_INITIALS[id] || CAT_INITIALS[baseId] || id.slice(0, 2);
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
    ,
      { en: "Greetings", mr: "शुभेच्छा", roman: "shubhechChA", hint: "" },
      { en: "Many Greetings", mr: "अनेकानेक शुभेच्छा", roman: "anekAnek shubhechChA", hint: "" },
      { en: "Happy Birthday", mr: "वाढदिवसाच्या हार्दिक शुभेच्छा", roman: "vADhadivasAchyA hArdik shubhechChA", hint: "" },
      { en: "Happy Diwali", mr: "दिवाळीच्या हार्दिक शुभेच्छा", roman: "divaLIchyA hArdik shubhechChA", hint: "" },
      { en: "Merry X'mas", mr: "नाताळ्च्या/ख्रिसमसच्या हार्दिक शुभेच्छा", roman: "nAtALchyA/khrisamasachyA hArdik shubhechChA", hint: "" },
      { en: "Congratulations", mr: "अभिनंदन", roman: "abhinaMdan", hint: "" },
      { en: "Heartiest Congratulations", mr: "हार्दिक/मनःपूर्वक अभिनंदन", roman: "hArdik/manHpUrvak abhinaMdan", hint: "" },
      { en: "I love you", mr: "माझे तुझ्यावर प्रेम आहे", roman: "mAjhe tujhyAvar prem Ahe", hint: "" },
      { en: "Live long life", mr: "आयुष्मान भव", roman: "AyuShmAn bhava", hint: "" },
      { en: "May you live 100 years", mr: "जीवेत शरदः शतम", roman: "jIvet sharadH shatam", hint: "" },
      { en: "Be successful", mr: "यशस्वी भव", roman: "yashasvI bhava", hint: "" },
      { en: "Live long life", mr: "चिरंजीव भव", roman: "chiraMjIv bhava", hint: "" },
      { en: "May your pair lives forever", mr: "अखंडसौभाग्यवती भव", roman: "akhaMDasaubhAgyavatI bhava", hint: "" },
      { en: "Blessing/Blessings", mr: "आशिर्वाद", roman: "AshirvAd", hint: "" },
      { en: "Bless me", mr: "मला आशिर्वाद द्या", roman: "malA AshirvAd dyA", hint: "" },
      { en: "My blessings are always with you", mr: "माझे आशिर्वाद सदैव तुझ्या पठीशी आहेत", roman: "mAjhe AshirvAd sadaiva tujhyA paThIshI Ahet", hint: "" },
      { en: "May god grace you", mr: "देव तुझं भलं करो", roman: "dev tujhaM bhalaM karo", hint: "" },
      { en: "Long live!", mr: "जिंदाबाद", roman: "jiMdAbAd", hint: "" },
      { en: "Long live India", mr: "भारत जिन्दाबाद", roman: "bhArat jindAbAd", hint: "" },
      { en: "Down with inflation", mr: "महागाई मुर्दाबाद", roman: "mahAgAI murdAbAd", hint: "" },
      { en: "Victory be of India", mr: "भारताचा विजय असो", roman: "bhAratAchA vijay aso", hint: "" },
      { en: "Gift with love", mr: "सप्रेम भेट", roman: "saprem bheT", hint: "" },
      { en: "Dear", mr: "प्रिय", roman: "priya", hint: "" },
      { en: "May God bless you", mr: "देव तुम्हाला आशिर्वाद देवो", roman: "dev tumhAlA AshirvAd devo", hint: "" },
      { en: "May God bless you (custom)", mr: "देव तुमचं भलं करो", roman: "dev tumachaM bhalaM karo", hint: "" },
      { en: "May he help you", mr: "तो तुम्हाला मदत करो", roman: "to tumhAlA madat karo", hint: "" },
      { en: "May they help you", mr: "ते तुम्हाला मदत करोत", roman: "te tumhAlA madat karot", hint: "" },
      { en: "May new year be happy", mr: "नवीन वर्ष सुखदायक असो", roman: "navIn varSh sukhadAyak aso", hint: "" },
      { en: "May shop open soon", mr: "दुकान लवकर उघडो", roman: "dukAn lavakar ughaDo", hint: "" },
      { en: "I wish he goes to school", mr: "माझी अशी इच्छा आहे की तो शाळेत गेला पाहिजे", roman: "mAjhI ashI ichChA Ahe kI to shALet gelA pAhije", hint: "" },
      { en: "He wishes Kaushik wins", mr: "त्याची अशी इच्छा आहे की कौशिक जिंको", roman: "tyAchI ashI ichChA Ahe kI kaushik jiMko", hint: "" },
      { en: "I wish that he should win", mr: "माझी अशी इच्छा आहे की तो जिंकावा", roman: "mAjhI ashI ichChA Ahe kI to jiMkAvA", hint: "" },
      { en: "I wish that she should win", mr: "माझी अशी इच्छा आहे की ती जिंकावी", roman: "mAjhI ashI ichChA Ahe kI tI jiMkAvI", hint: "" },
      { en: "He wishes that we win", mr: "त्याची अशी इच्छा आहे की आम्ही जिंकावे", roman: "tyAchI ashI ichChA Ahe kI AmhI jiMkAve", hint: "" },
      { en: "I wish that you(boy) should smile", mr: "माझी अशी इच्छा आहे की तू हसावास", roman: "mAjhI ashI ichChA Ahe kI tU hasAvAs", hint: "" },
      { en: "I wish that you(girl) should smile", mr: "माझी अशी इच्छा आहे की तू हसावीस", roman: "mAjhI ashI ichChA Ahe kI tU hasAvIs", hint: "" },
      { en: "May God not bless you", mr: "देव तुम्हाला आशिर्वाद न देवो", roman: "dev tumhAlA AshirvAd na devo", hint: "" },
      { en: "May he not help you", mr: "तो तुम्हाला मदत न करो", roman: "to tumhAlA madat na karo", hint: "" },
      { en: "I wish that he should not win", mr: "माझी अशी इच्छा आहे की तो जिंकू नये", roman: "mAjhI ashI ichChA Ahe kI to jiMkU naye", hint: "" },
      { en: "I wish that he should not eat mango", mr: "माझी अशी इच्छा आहे की त्याने आंबा खाऊ नये", roman: "mAjhI ashI ichChA Ahe kI tyAne AMbA khAU naye", hint: "" },
      { en: "Festival", mr: "उत्सव", roman: "utsav", hint: "" },
      { en: "Religious festival", mr: "सण", roman: "saN", hint: "" },
      { en: "Diwali", mr: "दिवाळी / दीपावली", roman: "diwALI / dIpAvalI", hint: "" },
      { en: "Greeting", mr: "दीपावलीच्या हार्दिक शुभेच्छा!", roman: "dIpAvalIchyA hardik shubhechChA!", hint: "" },
      { en: "Lamp", mr: "दिवा", roman: "divA", hint: "" },
      { en: "To light a lamp", mr: "दिवा लावणे", roman: "divA lAvaNe", hint: "" },
      { en: "Earthen lamp", mr: "पणती", roman: "paNatI", hint: "" },
      { en: "Oil", mr: "तेल", roman: "tel", hint: "" },
      { en: "Cotton wick", mr: "वात", roman: "vAt", hint: "" },
      { en: "Lantern", mr: "कंदील", roman: "kaMdIl", hint: "" },
      { en: "Door garland", mr: "तोरण", roman: "toraN", hint: "" },
      { en: "Flower", mr: "फूल", roman: "phUl", hint: "" },
      { en: "Mango leaves", mr: "आंब्याची पाने", roman: "AMbyAchI pAne", hint: "" },
      { en: "Front yard", mr: "अंगण", roman: "aMgaN", hint: "" },
      { en: "Rangoli", mr: "रांगोळी", roman: "rAMgoLI", hint: "" },
      { en: "To draw rangoli", mr: "रांगोळी काढणे", roman: "rAMgoLI kADhaNe", hint: "" },
      { en: "Worship", mr: "पूजा", roman: "pUjA", hint: "" },
      { en: "To worship", mr: "पूजा करणे", roman: "pUjA karaNe", hint: "" },
      { en: "To offer food to god", mr: "नैवेद्य दाखवणे", roman: "naivedya dAkhavaNe", hint: "" },
      { en: "Prasad", mr: "प्रसाद", roman: "prasAd", hint: "" },
      { en: "Crackers", mr: "फटाके", roman: "phaTAke", hint: "" },
      { en: "To burst crackers", mr: "फटाके फोडणे/वाजवणे/उडवणे", roman: "phaTAke phoDaNe/vAjavaNe/uDavaNe", hint: "" },
      { en: "Sweets", mr: "मिठाई", roman: "miThAI", hint: "" },
      { en: "Snacks & sweets", mr: "फराळ", roman: "pharAL", hint: "" },
      { en: "To have snacks", mr: "फराळ करणे", roman: "pharAL karaNe", hint: "" },
      { en: "Diwali edition", mr: "दिवाळी अंक", roman: "divALI aMk", hint: "" },
      { en: "Magazine", mr: "मासिक", roman: "mAsik", hint: "" },
      { en: "King", mr: "राजा / महाराज", roman: "rAjA / mahArAj", hint: "" },
      { en: "Soldiers", mr: "शिपाई", roman: "shipAI", hint: "" },
      { en: "Fort", mr: "किल्ला", roman: "killA", hint: "" },
      { en: "To build fort", mr: "किल्ला बांधणे", roman: "killA bAMdhaNe", hint: "" },
      { en: "Good morning/evening/night", mr: "नमस्कार / नमस्ते (or English)", roman: "namaskAr / namaste", hint: "" },
      { en: "Welcome (formal)", mr: "सुस्वागतम", roman: "susvAgatam", hint: "" },
      { en: "Welcome (daily)", mr: "या या", roman: "yA yA", hint: "" },
      { en: "How are you (to boy)", mr: "तू कसा आहेस", roman: "tU kasA Ahes", hint: "" },
      { en: "How are you (to girl)", mr: "तू कशी आहेस", roman: "tU kashI Ahes", hint: "" },
      { en: "How are you (to man/lady)", mr: "तुम्ही कसे आहात", roman: "tumhI kase AhAt", hint: "" },
      { en: "How do you do (to boy)", mr: "तू काय म्हणतोस", roman: "tU kAy mhaNatos", hint: "" },
      { en: "How do you do (to girl)", mr: "तू काय म्हणतेस", roman: "tU kAy mhaNates", hint: "" },
      { en: "How do you do (to man/lady)", mr: "तुम्ही काय म्हणता", roman: "tumhI kAy mhaNatA", hint: "" },
      { en: "I am fine", mr: "मी मजेत आहे", roman: "mI majet Ahe", hint: "" },
      { en: "Long-time no see (to boy)", mr: "खूप दिवसात भेटला नाहीस", roman: "khUp divasAt bheTalA nAhIs", hint: "" },
      { en: "Long-time no see (to girl)", mr: "खूप दिवसात भेटली नाहीस", roman: "khUp divasAt bheTalI nAhIs", hint: "" },
      { en: "Please have a seat (to boy/girl)", mr: "बस", roman: "bas", hint: "" },
      { en: "Please have a seat (to man/lady)", mr: "बसा", roman: "basA", hint: "" },
      { en: "Can you give me water? (to boy)", mr: "मला थोडे पाणी देतोस का?", roman: "malA thoDe pANI detos kA?", hint: "" },
      { en: "Can you give me water? (to man/lady)", mr: "मला थोडे पाणी देता का?", roman: "malA thoDe pANI detA kA?", hint: "" },
      { en: "What would you like? Tea or Coffee?", mr: "तुम्ही काय घेणार? चहा की कॉफी?", roman: "tumhI kAy gheNAr? chahA kI k~ophI?", hint: "" },
      { en: "I will take tea", mr: "मी चहा घेईन", roman: "mI chahA gheIn", hint: "" },
      { en: "Tea is fine for me", mr: "मला चहा चालेल", roman: "malA chahA chAlel", hint: "" },
      { en: "No thanks", mr: "नको", roman: "nako", hint: "" },
      { en: "No I don't want anything", mr: "नको. मला काही नको", roman: "nako malA kAhI nako", hint: "" },
      { en: "What do you do? (to boy)", mr: "सध्या काय करतो आहेस", roman: "sadhyA kAy karato Ahes", hint: "" },
      { en: "What do you do? (to man/lady)", mr: "सध्या काय करत आहात", roman: "sadhyA kAy karat AhAt", hint: "" },
      { en: "Where do you stay? (to boy)", mr: "तू कुठे राहतोस", roman: "tU kuThe rAhatos", hint: "" },
      { en: "Where do you stay? (to man/lady)", mr: "तुम्ही कुठे राहता", roman: "tumhI kuThe rAhatA", hint: "" },
      { en: "What is your name? (to boy/girl)", mr: "तुझे नाव काय", roman: "tujhe nAv kAy", hint: "" },
      { en: "What is your name? (to man/lady)", mr: "तुमचे नाव काय", roman: "tumache nAv kAy", hint: "" },
      { en: "My name is Kaushik", mr: "माझे नाव कौशिक", roman: "mAjhe nAv kaushik", hint: "" },
      { en: "Where do you work? (to boy)", mr: "तू कुठे काम करतोस", roman: "tU kuThe kAm karatos", hint: "" },
      { en: "How is everybody at home?", mr: "घरी सगळे कसे आहेत?", roman: "gharI sagaLe kase Ahet?", hint: "" },
      { en: "Give my regards to uncle", mr: "काकांना माझा नमस्कार सांग", roman: "kAkAMnA mAjhA namaskAr sAMg", hint: "" },
      { en: "Bye bye", mr: "टा टा", roman: "TA TA", hint: "" },
      { en: "See you again", mr: "परत भेटू / भेटुया", roman: "parat bheTU / bheTuyA", hint: "" },
      { en: "When will we see again?", mr: "परत कधी भेटणार?", roman: "parat kadhI bheTaNAr?", hint: "" },
      { en: "Ok", mr: "ठीक / ठीक आहे", roman: "ThIk / ThIk Ahe", hint: "" },
      { en: "It was nice to meet you (familiar)", mr: "तुम्हाला भेटून बरं वाटलं", roman: "tumhAlA bheTUn baraM vATalaM", hint: "" },
      { en: "It was nice to hear that", mr: "हे ऐकून बरं वाटलं की", roman: "he aikUn baraM vATalM kI", hint: "" },
      { en: "It was nice to see that", mr: "हे बघून बरं वाटलं की", roman: "he baghUn baraM vATalM kI", hint: "" }
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
    ,
      { en: "Hey friend", mr: "अरे मित्रा", roman: "are mitrA", hint: "" },
      { en: "Hey brother", mr: "अरे दादा", roman: "are dAdA", hint: "" },
      { en: "Hey lad/boy", mr: "अरे मुला / बाळा", roman: "are mulA / bALA", hint: "" },
      { en: "Hey Sister (formal)", mr: "अहो ताई", roman: "aho tAI", hint: "" },
      { en: "Hey Sister (known elder)", mr: "अगं ताई", roman: "agaM tAI", hint: "" },
      { en: "Uncle!", mr: "अहो काका", roman: "aho kAkA", hint: "" },
      { en: "Aunty!", mr: "अहो काकू / अहो मावशी", roman: "aho kAkU / aho mAvashI", hint: "" },
      { en: "Hello Madam", mr: "अहो Madam", roman: "aho Madam", hint: "" },
      { en: "Hello Sir", mr: "अहो Sir", roman: "aho Sir", hint: "" },
      { en: "Hey! How are you? (to boy)", mr: "कायरे? कसा आहेस?", roman: "kAyare? kasA Ahes?", hint: "" },
      { en: "Hey! How are you? (to girl)", mr: "कायगं? कशी आहेस?", roman: "kAyagaM? kashI Ahes?", hint: "" },
      { en: "Hello! How are you? (to elder)", mr: "कायहो? कसे आहात?", roman: "kAyaho? kase AhAt?", hint: "" },
      { en: "Hey, Boss has come", mr: "साहेब आलेरे", roman: "sAheb Alere", hint: "" },
      { en: "Come (to boy)", mr: "येरे", roman: "yere", hint: "" },
      { en: "Come (to girl)", mr: "येगं", roman: "yegaM", hint: "" },
      { en: "Come (to elder)", mr: "याहो", roman: "yAho", hint: "" },
      { en: "Please sing", mr: "गाना/गानं", roman: "gAnA/gAnaM", hint: "" },
      { en: "Do come to my marriage", mr: "माझ्या लग्नाला ये. येहं", roman: "mAjhyA lagnAlA ye. yehaM", hint: "" },
      { en: "Do talk to him", mr: "त्याच्याशी बोला. बोलाहं", roman: "tyAchyAshI bolA. bolAhaM", hint: "" },
      { en: "Can you take me to Tilak road?", mr: "टिळक रोड ला येणार का?", roman: "TiLak roD lA yeNAr kA?", hint: "" },
      { en: "No", mr: "नाही", roman: "nAhI", hint: "" },
      { en: "Why?", mr: "का?", roman: "kA?", hint: "" },
      { en: "I want passenger to Kothrud, Baner", mr: "मला कोथरूड, बाणेरचे भाडे हवे आहे", roman: "malA kotharUD, bANerache bhADe have aahe", hint: "" },
      { en: "Yes. Have a seat", mr: "हो, बसा", roman: "ho, basA", hint: "" },
      { en: "Will you charge by meter?", mr: "मीटरने येणार ना?", roman: "mITarane yeNAr nA?", hint: "" },
      { en: "Where exactly on Tilak road?", mr: "टिळक रोड ला नक्की कुठे जायचेय?", roman: "TiLak roD lA nakkI kuThe jAyachey?", hint: "" },
      { en: "Drop me near S.P. College", mr: "एस. पी. कॉलेजला सोडा", roman: "es. pI. k~olejalA soda", hint: "" },
      { en: "Here is S.P. College", mr: "आले एस. पी. कॉलेज", roman: "aale es. pI. k~olej", hint: "" },
      { en: "How much is fare?", mr: "किती झाले?", roman: "kitI jhAle", hint: "" },
      { en: "Forty rupees", mr: "चाळीस रुपये", roman: "chALIs rupaye", hint: "" },
      { en: "We came so near, how so much?", mr: "इतक्या जवळ आलो, तरी इतके कसे?", roman: "itakyA javaL aalo, tarI itake kase?", hint: "" },
      { en: "I am telling as per meter only", mr: "मीटर प्रमाणेच सांगतो आहे", roman: "mITar pramANech sAMgato aahe", hint: "" },
      { en: "Show me the meter card", mr: "मला मीटर कार्ड दाखवा", roman: "malA mITar kArD dAkhavA", hint: "" },
      { en: "I don't have change for 100", mr: "माझ्याकडे शंभरचे सुट्टे नाहीत", roman: "mAjhyAkaDe shaMbharache suTTe nAhIt", hint: "" },
      { en: "Take these remaining 10 rupees", mr: "हे घ्या बाकीचे दहा रुपये", roman: "he ghyA bAkIche dahA rupaye", hint: "" },
      { en: "Where will I get share auto to Swargate?", mr: "स्वारगेटला शेअर रिक्शा कुठून मिळतील?", roman: "svArageTalA shear rikshA kuThUn miLatIl", hint: "" },
      { en: "From next square", mr: "पुढच्या चौकातून", roman: "puDhachyA chaukAtUn", hint: "" },
      { en: "Can you take me to Swargate? By share?", mr: "स्वारगेटला जाणार का? शेअर ने?", roman: "svArageTalA jANAr kA? shear ne?", hint: "" },
      { en: "Ten rupees per person", mr: "दहा रुपये", roman: "dahA rupaye", hint: "" },
      { en: "Straight", mr: "सरळ", roman: "saraL", hint: "" },
      { en: "Left", mr: "डावे", roman: "DAve", hint: "" },
      { en: "To left", mr: "डावीकडे", roman: "DAvIkaDe", hint: "" },
      { en: "Right", mr: "उजवे", roman: "ujave", hint: "" },
      { en: "To right", mr: "उजवीकडे", roman: "ujavIkaDe", hint: "" },
      { en: "Behind", mr: "मागे", roman: "mAge", hint: "" },
      { en: "In-front", mr: "समोर", roman: "samor", hint: "" },
      { en: "Next", mr: "पुढे", roman: "puDhe", hint: "" },
      { en: "Till", mr: "पर्यंत", roman: "paryaMt", hint: "" },
      { en: "After", mr: "नंतर", roman: "naMtar", hint: "" },
      { en: "Near", mr: "जवळ", roman: "javaL", hint: "" },
      { en: "Far", mr: "लांब", roman: "lAMb", hint: "" },
      { en: "Road", mr: "रस्ता", roman: "rastA", hint: "" },
      { en: "Square", mr: "चौक", roman: "chauk", hint: "" },
      { en: "Corner", mr: "कोपरा", roman: "koparA", hint: "" },
      { en: "Lane", mr: "गल्ली / बोळ", roman: "gallI / boL", hint: "" },
      { en: "Bridge", mr: "पूल", roman: "pUl", hint: "" },
      { en: "Hello, My Dear Kesari group", mr: "नमस्कार, केसरी group.", roman: "namaskAr, kesarI grUp.", hint: "" },
      { en: "Welcome to Singapore", mr: "सिंगापूरमध्ये तुमचं स्वागत आहे.", roman: "siMgApUramadhye tumachM svAgat Ahe.", hint: "" },
      { en: "I am Fiona, your local tour guide", mr: "मी फिओना, तुमची स्थानिक टूर गाईड.", roman: "mI phionA, tumachI sthAnik TUr gAID.", hint: "" },
      { en: "For next 4 days I will accompany you", mr: "पुढचे चार दिवस मी तुमच्या बरोबर असेन आणि सिंगापूर बघण्यासाठी तुम्हाला मार्गदर्शन करेन.", roman: "puDhache chAr divas mI tumachyA barobar asen ANi siMgApUr baghaNyAsAThI tumhAlA mArgadarshan karen.", hint: "" },
      { en: "Today we visit Universal Studios", mr: "आज आपण Universal Studios ला भेट देणार आहोत.", roman: "Aj ApaN Universal Studios lA bheT deNAr Ahot.", hint: "" },
      { en: "We will reach there in 40 minutes", mr: "इथून चाळीस मिनिटांत आपण तिथे पोचू.", roman: "ithUn chALIs miniTAMt ApaN tithe pochU.", hint: "" },
      { en: "Follow the Kesari flag after getting down", mr: "बसमधून उतरल्यावर केसरीच्या झेंड्याच्या मागोमाग जा.", roman: "basamadhUn utaralyAvar kesarIchyA jheMDyAchyA mAgomAg jA.", hint: "" },
      { en: "Ticket will have two parts", mr: "तिकिटाचे दोन भाग आहेत.", roman: "tikiTAche don bhAg Ahet.", hint: "" },
      { en: "Do not loose it", mr: "ते हरवू नका.", roman: "te haravU nakA.", hint: "" },
      { en: "We will meet at 4.30 PM", mr: "याच ठिकाणी साडे चार वाजता आपण भेटू.", roman: "yAch ThikANI sADe chAr vAjatA ApaN bheTU.", hint: "" },
      { en: "See you tomorrow", mr: "उद्या भेटूया.", roman: "udyA bheTUyA.", hint: "" },
      { en: "Good night", mr: "शुभरात्री.", roman: "shubharAtrI.", hint: "" }
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
    ,
      { en: "Ashgourd", mr: "कोहळा", roman: "kohaLA", hint: "" },
      { en: "Aubergine/Eggplant/Brinjal", mr: "वांगे", roman: "vAMge", hint: "" },
      { en: "Banana (raw)", mr: "कच्चे केळे", roman: "kachche keLe", hint: "" },
      { en: "French Beans", mr: "फरसबी", roman: "pharasabI", hint: "" },
      { en: "Beetroot", mr: "बीट", roman: "beeT", hint: "" },
      { en: "Bell Pepper/Capsicum", mr: "ढोबळी मिर्ची / सिमला मिर्ची", roman: "DhobaLI mirchI", hint: "" },
      { en: "Bitter Gourd", mr: "कारले", roman: "kArale", hint: "" },
      { en: "Bottle Gourd", mr: "दूधी भोपळा", roman: "dUdhI bhopaLA", hint: "" },
      { en: "Broad Beans", mr: "वाल पापडी / घेवडा", roman: "vAl pApaDI / ghevaDA", hint: "" },
      { en: "Cabbage", mr: "कोबी", roman: "kobI", hint: "" },
      { en: "Carrot", mr: "गाजर", roman: "gAjar", hint: "" },
      { en: "Cauliflower", mr: "फुलकोबी", roman: "phulakobI", hint: "" },
      { en: "Cilantro", mr: "कोथिंबिर", roman: "kothiMbir", hint: "" },
      { en: "Cluster Beans", mr: "गवार", roman: "gavAr", hint: "" },
      { en: "Cucumber", mr: "काकडी", roman: "kAkaDI", hint: "" },
      { en: "Drumstick", mr: "शेवग्याची शेंग", roman: "shevagyAchI sheMg", hint: "" },
      { en: "Garlic", mr: "लसूण", roman: "lasUN", hint: "" },
      { en: "Green Chili", mr: "हिरवी मिरची", roman: "hiravI mirachI", hint: "" },
      { en: "Green Peas", mr: "वाटाणा", roman: "vATANA", hint: "" },
      { en: "Lady Finger", mr: "भेंडी", roman: "bheMDI", hint: "" },
      { en: "Onion", mr: "कांदा", roman: "kAMdA", hint: "" },
      { en: "Potato", mr: "बटाटा", roman: "baTATA", hint: "" },
      { en: "Pumpkin", mr: "भोपळा", roman: "bhopaLA", hint: "" },
      { en: "Radish", mr: "मुळा", roman: "muLA", hint: "" },
      { en: "Ridgegourd", mr: "दोडका", roman: "doDakA", hint: "" },
      { en: "Sweet Potato", mr: "रताळे", roman: "ratALe", hint: "" },
      { en: "Tomato", mr: "टोमॅटो", roman: "TomaTo", hint: "" },
      { en: "Ginger", mr: "आले", roman: "Ale", hint: "" },
      { en: "Mint leaves", mr: "पुदिना", roman: "pudinA", hint: "" },
      { en: "Fenugreek Leaves", mr: "मेथी", roman: "methI", hint: "" },
      { en: "Coconut", mr: "नारळ", roman: "nAraL", hint: "" },
      { en: "Lemon", mr: "लिंबु", roman: "liMbu", hint: "" },
      { en: "Apple", mr: "सफरचंद", roman: "sapharachaMd", hint: "" },
      { en: "Apricot", mr: "जर्दाळू", roman: "jardALU", hint: "" },
      { en: "Banana", mr: "केळे", roman: "keLe", hint: "" },
      { en: "Indian Black Berry / Jamun", mr: "जांभुळ", roman: "jAMbhuL", hint: "" },
      { en: "Chickoo sapota", mr: "चिक्कु", roman: "chikku", hint: "" },
      { en: "Custard apple", mr: "सिताफळ", roman: "sitAphaL", hint: "" },
      { en: "Dates", mr: "खजूर", roman: "khajoor", hint: "" },
      { en: "Figs", mr: "अंजीर", roman: "aMjIr", hint: "" },
      { en: "Grapes", mr: "द्राक्ष", roman: "drAkSha", hint: "" },
      { en: "Guavas", mr: "पेरू", roman: "perU", hint: "" },
      { en: "Jackfruit", mr: "फणस", roman: "phaNas", hint: "" },
      { en: "Mango Ripe", mr: "आंबा", roman: "AMbA", hint: "" },
      { en: "Mango Raw", mr: "कैरी", roman: "kairI", hint: "" },
      { en: "Muskmelon / Cantalope", mr: "खरबूज", roman: "kharabUj", hint: "" },
      { en: "Olive", mr: "ऑलिव्ह", roman: "~olivh", hint: "" },
      { en: "Orange", mr: "संत्रे", roman: "saMtre", hint: "" },
      { en: "Papaya", mr: "पपई", roman: "papaI", hint: "" },
      { en: "Pear", mr: "नासपती", roman: "nAsapatI", hint: "" },
      { en: "Pineapple", mr: "अननस", roman: "ananas", hint: "" },
      { en: "Pomegranate", mr: "डाळिंब", roman: "DALiMb", hint: "" },
      { en: "Watermelon", mr: "टरबूज / कलिंगड", roman: "TarabUj / kaliMgaD", hint: "" },
      { en: "Sweet lime", mr: "मोसंबे", roman: "mosaMbe", hint: "" },
      { en: "Strawberry", mr: "स्ट्रॉबेरी", roman: "sTr~oberI", hint: "" },
      { en: "Jujube", mr: "बोर", roman: "bor", hint: "" },
      { en: "Peach", mr: "पीच", roman: "pIch", hint: "" },
      { en: "Friend, can you give me menucard?", mr: "मित्रा, जरा मेनूकार्ड देतोस का?", roman: "mitrA, jarA menUkArD detos kA?", hint: "" },
      { en: "Please give menucard", mr: "मेनूकार्ड द्या", roman: "menUkArD dyA", hint: "" },
      { en: "Which dish is served hot?", mr: "गरम काय आहे?", roman: "garam kAy Ahe?", hint: "" },
      { en: "Which dish is served cold?", mr: "थंड काय आहे?", roman: "thaMD kAy Ahe?", hint: "" },
      { en: "Is Idli available?", mr: "इडली आहे का?", roman: "iDalI Ahe kA?", hint: "" },
      { en: "Can I get pizza?", mr: "पिझ्झा मिळेल का?", roman: "pijhjhA miLel kA?", hint: "" },
      { en: "How much time for order?", mr: "ऑर्डर यायला किती वेळ लागेल?", roman: "~orDar yAyalA kitI veL lAgel?", hint: "" },
      { en: "Friend, is it not ready yet?", mr: "मित्रा, अजून झाले नाही का?", roman: "mitrA, ajUn jhaale nAhI kA?", hint: "" },
      { en: "Give one more Roti", mr: "एक रोटी आणखी द्या", roman: "ek roTI ANakhI dyA", hint: "" },
      { en: "I want still more butter", mr: "मला अजून लोणी हवे आहे", roman: "malA ajUn loNI have Ahe", hint: "" },
      { en: "Give the bill", mr: "बिल द्या", roman: "bil dyA", hint: "" },
      { en: "How much is bill?", mr: "बिल किती झाले?", roman: "bil kitI jhAle?", hint: "" },
      { en: "How much is 1 VadaPaav?", mr: "एक वडापाव कितीला?", roman: "ek vaDApAv kitIlA?", hint: "" },
      { en: "How much is 1 Dosa?", mr: "एक डोसा कितीला?", roman: "ek DosA kitIlA?", hint: "" },
      { en: "Give me 10 Vadas in parcel", mr: "मला दहा वडे पार्सल द्या", roman: "malA dahA vaDe pArsal dyA", hint: "" },
      { en: "Do you have change?", mr: "सुट्टे पैसे आहेत का?", roman: "suTTe paise Ahet kA?", hint: "" },
      { en: "I do not have change", mr: "सुट्टे नाहीत", roman: "suTTe nAhIt", hint: "" },
      { en: "10 minutes passed, food not served", mr: "दहा मिनिटे झाली. जेवण अजून आले नाही", roman: "dahA miniTe jhAlI. jevaN ajUn Ale nAhI", hint: "" },
      { en: "You will get idli", mr: "इडली मिळेल", roman: "iDalI miLel", hint: "" },
      { en: "Pizza is not available", mr: "पिझ्झा मिळणार नाही", roman: "pijhjhA miLaNAr nAhI", hint: "" },
      { en: "It will take 10 minutes", mr: "१० मिनिटे लागतील", roman: "10 miniTe lAgatIl", hint: "" },
      { en: "This vegetable will be sweet", mr: "ही भाजी गोड असेल", roman: "hI bhAjI goD asel", hint: "" },
      { en: "This dish will be hot in taste", mr: "ही डिश तिखट असेल", roman: "hI Dish tikhaT asel", hint: "" },
      { en: "It is very hot today", mr: "आज खूप गरम होते आहे", roman: "Aj khUp garam hote Ahe", hint: "" },
      { en: "It is very hot and humid today", mr: "आज खूप उकडते आहे", roman: "Aj khUp ukaDate Ahe", hint: "" },
      { en: "Yesterday was cool", mr: "काल थंडी होती", roman: "kAl thaMDI hotI", hint: "" },
      { en: "I thought coolness will continue", mr: "मला वाटले आजही गारवा राहील", roman: "malA vATale AjahI gAravA rAhIl", hint: "" },
      { en: "It is raining", mr: "पाऊस पडतो आहे", roman: "pAUs paDato Ahe", hint: "" },
      { en: "It rained yesterday also", mr: "काल पण पाऊस पडला", roman: "kAl paN pAUs paDalA", hint: "" },
      { en: "It was torrential rain", mr: "मुसळधार पाऊस पडला", roman: "musaLadhAr pAUs paDalA", hint: "" },
      { en: "It is rainy weather today", mr: "आज पावसाळी वातावरण आहे", roman: "Aj pAvasALI vAtAvaraN Ahe", hint: "" },
      { en: "Many clouds are seen", mr: "बरेच ढग दिसत आहेत", roman: "barech Dhag disat Ahet", hint: "" },
      { en: "It is cloudy now", mr: "आत्ता मळभ आहे", roman: "AttA maLabh aahe", hint: "" },
      { en: "The sky is cloud-free", mr: "आकाश निरभ्र आहे", roman: "Akash nirabhra Ahe", hint: "" },
      { en: "Good sunlight outside", mr: "बाहेर चांगले ऊन पडले आहे", roman: "bAher chAMgale Un paDale Ahe", hint: "" },
      { en: "What is the temperature now?", mr: "आत्ता तापमान किती आहे", roman: "AttA tApamAn kitI Ahe", hint: "" },
      { en: "25 degree Celsius", mr: "पंचवीस अंश सेल्सिअस", roman: "paMchavIs aMsh selsias", hint: "" },
      { en: "The wind is blowing fast", mr: "वारा जोरात वाहतो आहे", roman: "vArA jorAt vAhato Ahe", hint: "" },
      { en: "Air is fresh and pure there", mr: "तिथे हवा ताजी आणि शुद्ध आहे", roman: "tithe havA tAjI ANi shuddha Ahe", hint: "" },
      { en: "Hello my dear", mr: "हॅलो बेटा.", roman: "h~alo beTA.", hint: "" },
      { en: "Hello aunty", mr: "नमस्कार काकू.", roman: "namaskAr kAkU.", hint: "" },
      { en: "How are you?", mr: "तुम्ही कशा आहात?", roman: "tumhI kashA AhAt?", hint: "" },
      { en: "I am fine", mr: "मी ठीक आहे.", roman: "mI ThIk Ahe.", hint: "" },
      { en: "You came after so many days", mr: "तू खूप दिवसानंतर आला आहेस.", roman: "tU khUp divasAnMtar AlA Ahes.", hint: "" },
      { en: "Aunty my exams were going on", mr: "हो काकू. माझी परीक्षा चालू होती म्हणून मी नाही आलो.", roman: "ho kAkU. mAjhI parIkShA chAlU hotI mhaNUn mI nAhI Alo.", hint: "" },
      { en: "We are going to eat lunch. You too come", mr: "आता आम्ही जेवायला बसतो आहोत. तू सुद्धा ये.", roman: "AtA AmhI jevAyalA basato Ahot. tU suddhA ye.", hint: "" },
      { en: "No aunty. I am not much hungry", mr: "नको काकू मला जास्त भूक नाहीये.", roman: "nako kAkU malA jAst bhUk nAhIye.", hint: "" },
      { en: "Aunty, this dal is too tasty", mr: "काकू, ही डाळ खूप चविष्ट आहे.", roman: "kAkU, hI DAL khUp chaviShT Ahe.", hint: "" },
      { en: "Please give me a bit more", mr: "मला थोडी अजून द्या.", roman: "malA thoDI ajUn dyA.", hint: "" },
      { en: "What do you love to eat?", mr: "तुला खायला काय काय आवडते?", roman: "tulA khAyalA kAy kAy AvaDate?", hint: "" },
      { en: "Aunty, I like all vegetables but ladyfinger is my favourite", mr: "काकू मला सगळ्या भाज्या आवडतात पण मला भेंडी सगळ्यात जास्त आवडते.", roman: "kAkU malA sagaLyA bhAjyA AvaDatAt paN malA bheMDI sagaLyAt jAst AvaDate.", hint: "" },
      { en: "What's the time of dinner at your home?", mr: "तुझ्या घरी रात्री कधी जेवता?", roman: "tujhyA gharI rAtrI kadhI jevatA?", hint: "" },
      { en: "Dinner time is not fixed. Mostly 9 or 10 pm", mr: "जेवायची वेळ नक्की नाही. बहुतेक वेळा आठ किंवा नऊ वाजता जेवतो.", roman: "jevAyachI veL nakkI nAhI. bahutek veLA ATh kiMvA naU vAjatA jevato.", hint: "" },
      { en: "No, I am full now", mr: "नको, माझे पोट भरले आहे. आता मी जास्त नाही खाऊ शकत.", roman: "nakko, mAjhe poT bharale Ahe. AtA mI jAst nAhI khAU shakat.", hint: "" },
      { en: "I went to my friend's house today", mr: "मी आज माझ्या मित्राच्या घरी गेले.", roman: "mI mAjhyA mitrAchyA gharI gele", hint: "" },
      { en: "She cooked Indian dishes", mr: "तिने भारतीय स्वयंपाक केला", roman: "tine bhAratIy svayaMpAk kelA", hint: "" },
      { en: "What did you eat?", mr: "तू काय खाल्लेस?", roman: "tU kAy khAlles?", hint: "" },
      { en: "I ate coconut chutney", mr: "मी नारळाची चटणी खाल्ली", roman: "mI nAraLAchI chaTaNI khAllI", hint: "" },
      { en: "How important is food in your family?", mr: "तुझ्या कुटुंबाच्या जीवनात जेवण तयार करणे किती महत्वाचे आहे?", roman: "tujhyA kuTuMbAchyAjIvanAt jevaN tayAr karaNe kitI mahatvAche Ahe?", hint: "" },
      { en: "My family is multicultural", mr: "माझं कुटुंब बहुसांस्कृतिक कुटुंब आहे.", roman: "mAjhM kuTuMb bahusAMskRutik kuTuMb Ahe.", hint: "" },
      { en: "On Monday we ate North Indian food", mr: "सोमवारी आम्ही उत्तर भारतीय भोजन खाल्ले.", roman: "somavArI AmhI uttar bhAratIy bhojan khAlle.", hint: "" },
      { en: "What did you cook this morning?", mr: "कृपया मला सांगा आज सकाळी तुम्ही काय बनवले?", roman: "kRupayA malA sAMgA Aj sakALI tumhI kAy banavale?", hint: "" },
      { en: "I prepared capsicum with gram flour", mr: "मी खूप चविष्ट ढब्बू मिरचीचे बेसन केले.", roman: "mI khUp chaviShT DhabbU mirachIche besan kele.", hint: "" }
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
    ,
      { en: "Give me 1kg Sugar", mr: "एक किलो साखर द्या", roman: "ek kilo sAkhar dyA", hint: "" },
      { en: "Take this", mr: "ही घ्या", roman: "hI ghyA", hint: "" },
      { en: "Do you have Good day biscuit?", mr: "\"गुड डे\" बिस्किट आहे का?", roman: "guD De biskiT Ahe kA?", hint: "" },
      { en: "Yes. I have", mr: "आहे", roman: "Ahe", hint: "" },
      { en: "Give 2 packs", mr: "दोन पुडे द्या", roman: "don puDe dyA", hint: "" },
      { en: "Which cream biscuit is there?", mr: "कुठले क्रीम बिस्किट आहे?", roman: "kuThale krIm biskiT Ahe?", hint: "" },
      { en: "Parle's", mr: "पारले चे आहे", roman: "pArale che Ahe", hint: "" },
      { en: "I do not want this. Is there any other?", mr: "हे नको. अजून दुसरे. कुठले आहे का?", roman: "he nako. ajUn dusare kuThale Ahe kA?", hint: "" },
      { en: "Bournville is there", mr: "बोरबोन आहे", roman: "borabon Ahe", hint: "" },
      { en: "It will do. Give 1 pack. How much is total bill?", mr: "चालेल. १ पुडा द्या. किती झाले?", roman: "chAlel. 1 puDA dyA. kitI jhAle?", hint: "" },
      { en: "Seventy rupees", mr: "सत्तर झाले", roman: "sattar jhAle", hint: "" },
      { en: "I do not have bag. Can you give me plastic bag?", mr: "माझ्याकडे पिशवी नाहिये. प्लॅस्टिकची पिशवी देता का?", roman: "mAjhyAkaDe pishavI nAhiye. pl~asTikachI pishavI detA kA?", hint: "" },
      { en: "Plastic bags are banned. Take this paper bag", mr: "प्लॅस्टिकच्या पिशव्यांवर सध्या बंदी आहे. हि कागदी पिशवी घ्या.", roman: "pl~asTikachyA pishavyAMvar sadhyA baMdI Ahe. hi kAgadI pishavI ghyA.", hint: "" },
      { en: "Do you have Good day biscuit?", mr: "\"गुड डे\" बिस्किट आहे का?", roman: "guD De biskiT Ahe kA?", hint: "" }
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
    ,
      { en: "Police: Hey, take vehicle to side", mr: "अरे ए, गाडी बाजूला घे", roman: "are e, gADI bAjUlA ghe", hint: "" },
      { en: "Police: Hey, can't you hear?", mr: "ऐकू नाही आलं का रे?", roman: "aikU nAhI AlaM kA re?", hint: "" },
      { en: "Police: Bring vehicle to side", mr: "गाडी बाजूला आण", roman: "gADI bAjUlA AN", hint: "" },
      { en: "Driver: What happened Sir?", mr: "काय झालं साहेब?", roman: "kAy jhAlM sAheb?", hint: "" },
      { en: "Police: You jumped signal", mr: "सिग्नल तोडलास तू", roman: "signal toDalAs tU", hint: "" },
      { en: "Driver: No Sir", mr: "नाही साहेब", roman: "nAhI sAheb", hint: "" },
      { en: "Police: How come no?", mr: "नाही कसं?", roman: "nAhI kasaM?", hint: "" },
      { en: "Driver: It is true Sir", mr: "खरंच सांगतो साहेब", roman: "kharaMch sAMgato sAheb", hint: "" },
      { en: "Driver: I was just following that car", mr: "ती गाडी चालली होती तिच्या मागोमागच मी चाललो होतो", roman: "tI gADI chAlalI hotI tichyA mAgomAgach mI chAlalo hoto", hint: "" },
      { en: "Police: Don't tell about that car. Tell about you", mr: "त्या गाडीचं मला नको सांगू. तुझं सांग", roman: "tyA gADIchM malA nako sAMgU. tujhaM sAMg", hint: "" },
      { en: "Police: You broke rule. Pay fine", mr: "रुल मोडला. फाईन भरावी लागेल", roman: "rul moDalA. phAIn bharAvI lAgel", hint: "" },
      { en: "Police: Pay 500 rupees", mr: "पाचशे रुपये भरा", roman: "pAchashe rupaye bharA", hint: "" },
      { en: "Driver: Thanks you sir", mr: "थॅंक यू साहेब", roman: "th~aMk yU sAheb", hint: "" },
      { en: "Please come. Have seat", mr: "या, बसा.", roman: "yA, basA.", hint: "" },
      { en: "What is the problem?", mr: "काय होतंय?", roman: "kAy hotaMy?", hint: "" },
      { en: "I am suffering from cold", mr: "सर्दी झालिये", roman: "sardI jhAliye", hint: "" },
      { en: "There is temperature", mr: "ताप आलाय", roman: "tAp AlAy", hint: "" },
      { en: "From when?", mr: "कधीपासून?", roman: "kadhIpAsUn?", hint: "" },
      { en: "From yesterday morning", mr: "काल सकाळ पासून", roman: "kAl sakAL pAsUn", hint: "" },
      { en: "Ok. Lay down there", mr: "बरं. तिकडे झोपा.", roman: "barM. tikaDe jhopA.", hint: "" },
      { en: "Show eyes", mr: "डोळे दाखवा", roman: "DoLe dAkhavA", hint: "" },
      { en: "Show tongue", mr: "जीभ दाखवा", roman: "jIbh dAkhavA", hint: "" },
      { en: "Open mouth wide", mr: "मोठा आ करा.", roman: "moThA A karA.", hint: "" },
      { en: "Let me see throat", mr: "घसा बघू", roman: "ghasA baghU", hint: "" },
      { en: "Take deep breath", mr: "मोठा श्वास घ्या.", roman: "moThA shwAs ghyA.", hint: "" },
      { en: "Leave it", mr: "सोडा", roman: "soDA", hint: "" },
      { en: "Take again", mr: "पुन्हा घ्या.", roman: "punhA ghyA.", hint: "" },
      { en: "OK. Sit there", mr: "ठीक आहे. बसा तिकडे.", roman: "ThIk Ahe. basA tikaDe.", hint: "" },
      { en: "Let me check pulse", mr: "नाडी बघू.", roman: "nADI baghU.", hint: "" },
      { en: "I check B.P.", mr: "बीपी चेक करतो.", roman: "bIpI chek karato.", hint: "" },
      { en: "Why is there temperature?", mr: "कशामुळे ताप आला असेल?", roman: "kashAmuLe tAp AlA asel?", hint: "" },
      { en: "Nothing serious", mr: "काही विशेष नाही", roman: "kAhI visheSh nAhI", hint: "" },
      { en: "May be because of changing weather", mr: "हवा बदलत्ये त्यामुळे असावा.", roman: "havA badalatye tyAmuLe asAvA.", hint: "" },
      { en: "I give you pills for 2 days. Take them", mr: "मी दोन दिवसांच्या गोळ्या देतो त्या घ्या.", roman: "mI don divasAMchyA goLyA deto tyA ghyA.", hint: "" },
      { en: "These two in morning and these 2 in evening", mr: "या दोन सकाळी या दोन संध्याकाळी.", roman: "yA don sakALI yA don saMdhyAkALI.", hint: "" },
      { en: "Before lunch or after?", mr: "जेवणाआधी का नंतर?", roman: "jevaNAAdhI kA naMtar?", hint: "" },
      { en: "Yes, take after eating something", mr: "हो, काहितरी खाऊनच घ्या.", roman: "ho, kAhitarI khAUnach ghyA.", hint: "" },
      { en: "Do not take when empty stomach", mr: "रिकाम्या पोटी नका घेऊ", roman: "rikAmyA poTI nakA gheU", hint: "" },
      { en: "Anything about diet?", mr: "बाकी पथ्य?", roman: "bAkI pathya?", hint: "" },
      { en: "Do not take cold water, curd, buttermilk", mr: "गार पाणी, गार दही, ताक पिऊ नका.", roman: "gAr pANI, gAr dahI, tAk piU nakA.", hint: "" },
      { en: "Drink boiled water", mr: "पाणी उकळून प्या.", roman: "pANI ukaLUn pyA.", hint: "" },
      { en: "And wear woolen cloths", mr: "आणि गरम कपडे घाला.", roman: "ANi garam kapaDe ghAlA.", hint: "" },
      { en: "OK. How much is fee?", mr: "ओके. किती फी झाली?", roman: "oke. kitI phI jhAlI?", hint: "" },
      { en: "Hundred rupees", mr: "शंभर रुपये.", roman: "shaMbhar rupaye.", hint: "" },
      { en: "Should I visit again?", mr: "पुन्हा दाखवायला येऊ का?", roman: "punhA dAkhavAyalA yeU kA?", hint: "" },
      { en: "If temperature is normal then no need", mr: "ताप उतरला तर गरज नाही.", roman: "tAp utaralA tar garaj nAhI.", hint: "" },
      { en: "If you do not feel well then please come", mr: "बरं नाही वाटलं तर या.", roman: "barM nAhI vATalaM tar yA.", hint: "" },
      { en: "It will do", mr: "चालेल.", roman: "chAlel.", hint: "" }
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
    ,
      { en: "Third", mr: "तिसरा", roman: "tisarA", hint: "" },
      { en: "Fourth", mr: "चौथा", roman: "chauthA", hint: "" },
      { en: "Fifth", mr: "पाचवा", roman: "pAchavA", hint: "" },
      { en: "Sixth", mr: "सहावा", roman: "sahAvA", hint: "" },
      { en: "Seventh", mr: "सातवा", roman: "sAtavA", hint: "" },
      { en: "Eighth", mr: "आठवा", roman: "AThavA", hint: "" },
      { en: "Quarter", mr: "पाव", roman: "pAv", hint: "" },
      { en: "Half", mr: "अर्धा", roman: "ardhA", hint: "" },
      { en: "Three fourth", mr: "पाऊण", roman: "pAUN", hint: "" },
      { en: "Full", mr: "पूर्ण", roman: "pUrN", hint: "" },
      { en: "One & quarter", mr: "सव्वा", roman: "savvA", hint: "" },
      { en: "One & half", mr: "दीड", roman: "dID", hint: "" },
      { en: "Quarter to two", mr: "पावणे दोन", roman: "pAvaNe don", hint: "" },
      { en: "Two & quarter", mr: "सव्वा दोन", roman: "savvA don", hint: "" },
      { en: "Two & half", mr: "अडीच", roman: "aDIch", hint: "" },
      { en: "Three & half", mr: "साडे तीन", roman: "sADe tIn", hint: "" },
      { en: "Hello", mr: "नमस्कार", roman: "namaskar", hint: "" },
      { en: "Hello sir, how may I help you?", mr: "नमस्कार सर, मी तुम्हाला कशी मदत करु शकतो?", roman: "namaskar sar mi tumhala kashi madat karu shakato?", hint: "" },
      { en: "I received a message to link my Aadhaar with postpaid. Please tell me the procedure.", mr: "मला माझ्या पोस्टपेड कनेक्शनला आधार नंबर लिंक करण्याबद्दल मेसेज आला आहे. कृपया मला प्रक्रिया सांगा.", roman: "mala majhya postaped kanekshanala Adhar nambar link karanyabaddal mesej ala ahe. krupaya mala prakriya sanga.", hint: "" },
      { en: "Aadhar card alone is sufficient. Biometric test will validate.", mr: "तुमच्या मोबाईल नंबरच्या शिवाय फक्त आधार कार्ड पुरेसे आहे. पण दिलेला आधार क्रमांक प्रमाणित करण्यासाठी बायोमेट्रिक चाचणी घेतली जाईल", roman: "tumachya mobail nmbarachya shivay phakt Adhar kard purese ahe. pan dilela Adhar kramank pramanit karanyasathi bayometrik chachani ghetali jail.", hint: "" },
      { en: "Is the process chargeable? How many days?", mr: "काही चार्ज लागतो का? आणि सगळ्या गोष्टी सत्यापित करण्यासाठी किती दिवस लागतील?", roman: "kahi charj lagato ka? ani sagalya goshti satyapit karanyasathi kiti divas lagatil?", hint: "" },
      { en: "No it's free. Connection verified within a day.", mr: "हे विनामूल्य आहे आणि कनेक्शन एका दिवसात सत्यापित होऊन जाईल.", roman: "he vinamuly ahe ani kanekshan eka divasat satyapit houn jail.", hint: "" },
      { en: "What if I hold 2 connections?", mr: "माझ्याकडे 2 कनेक्शन असतील तर?", roman: "majhyakade 2 kanekshan asatil tar?", hint: "" },
      { en: "You'll have to complete process for both numbers separately", mr: "तर तुम्हाला दोन्ही नंबरसाठी प्रक्रिया वेगवेगळी पूर्ण करावी लागेल.", roman: "tar tumhala donhi nmbarasathi prakriya vegavegali purn karavi lagel.", hint: "" },
      { en: "I have registered your both numbers. Check if you've received the OTP.", mr: "मी तुमच्या दोन्ही नंबरची नोंदणी करून दिली आहे. बघा OTP आला आहे का?", roman: "mi tumachya donhi nmbarachi nondani karun dili ahe. bagha OTP ala ahe ka?", hint: "" },
      { en: "Yes, type in 1234 and 5678", mr: "हो 1234 आणि 5678 टाइप करा.", roman: "ho 1234 ani 5678 taip kara.", hint: "" },
      { en: "You can go for finger print on that side now", mr: "हो झाले. आता तुम्ही तिकडे जाऊन फिंगर प्रिंट देऊ शकता.", roman: "ho jhale. ata tumhi tikade jaun phingar print deu shakata.", hint: "" },
      { en: "After Biometric verification, reply with 'Y' to confirmation message", mr: "बायोमेट्रिक सत्यापनानंतर तुम्हाला 24 तासांत पुष्टीकरण संदेश मिळेल. त्यावर 'Y' लिहून पाठवून द्या.", roman: "bayometrik satyapananantar tumhala 24 tasaat pushtikaran sandesh milel. tyavar 'Y' lihun pathavun dya.", hint: "" },
      { en: "Fine. Thanks", mr: "ठीक आहे. धन्यवाद.", roman: "Thik ahe dhanyavad.", hint: "" },
      { en: "Bala - citizen who wants to link mobile number", mr: "बाला : आपला मोबाईल क्रमांक जोडण्यास इच्छुक असलेला नागरीक.", roman: "ApalA mobAIl kramAMk joDaNyAs ichChuk asalelA nAgarIk.", hint: "" },
      { en: "Sakshi - Help desk lady at Aadhaar center", mr: "साक्षी : आधार सेंटर येथे हेल्पडेस्क वर बसलेली महिला", roman: "sAkShI : AdhAr seMTar yethe helpaDesk var basalelI mahilA", hint: "" },
      { en: "Hi", mr: "नमस्कार.", roman: "namaskAr.", hint: "" },
      { en: "Hello, how can I help you?", mr: "नमस्कार. मी काय मदत करू शकते तुमची.", roman: "namaskAr. mI kAy madat karU shakate tumachI.", hint: "" },
      { en: "I had received a message to link phone with Aadhaar", mr: "माझ्या मोबाईल नंबरवर, आधार क्रमांकाला फोन नंबर जोडण्याविषयी मला एक संदेश मिळाला होता.", roman: "mAjhyA mobAIl naMbaravar, AdhAr kramAMkAlA phon naMbar joDaNyAviShayI malA ek saMdesh miLAlA hotA.", hint: "" },
      { en: "Do I need to submit any request form?", mr: "बरं, त्यासाठी काही अर्ज द्यावा लागतो का?", roman: "barM, tyAsAThI kAhI arj dyAvA lAgato kA?", hint: "" },
      { en: "Same Aadhaar update form. Get from next photostat shop", mr: "होय, अ‍ॅक्च्युअली हा आधारपत्र वालाच फॉर्म भरायचा असतो. सध्या तुम्हाला पुढच्या फोटोस्टॅट शॉपमधून मिळून जाईल", roman: "hoy, ~akchyualI hA AdhArapatr vAlAch ph~orm bharAyachA asato. sadhyA tumhAlA puDhachyA phoTosT~aT sh~opamadhUn miLUn jAIl.", hint: "" },
      { en: "Will I need to resubmit ID proofs?", mr: "बरं. आणि सगळी कागदपत्रं परत सादर करायची गरज पडेल का?", roman: "barM. ANi sagaLI kAgadapatrM parat sAdar karAyachI garaj paDel kA?", hint: "" },
      { en: "One name, dob and address proof. Biometric tests redone.", mr: "हो. एक नाव, जन्मतारीख आणि पत्त्याचा पुरावा सादर करणे आवश्यक आहे.", roman: "ho. ek nAv, janmatArIkh ANi pattyAchA purAvA sAdar karaNe Avashyak Ahe.", hint: "" },
      { en: "How long will it take?", mr: "नंबर लिंक होण्यासाठी किती दिवस लागतील?", roman: "naMbar liMk hoNyAsAThI kitI divasa lAgatIl?", hint: "" },
      { en: "Nearly 7-10 days. You'll get message.", mr: "सुमारे सात ते दहा दिवसांत होऊन जाईल. तुम्हाला तुमच्या नंबरवर मेसेज येईल.", roman: "sumAre sAt te dahA divasAMt hoUn jAIl. tumhAlA tumachyA naMbaravar mesej yeIl.", hint: "" },
      { en: "Thank you so much", mr: "बरं. खूप खूप धन्यवाद.", roman: "barM. khUp khUp dhanyvAd", hint: "" },
      { en: "No problem", mr: "काही हरकत नाही", roman: "kAhI harakat nAhI", hint: "" }
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
    ,
      { en: "From the new year, I have decided not to spend time on Facebook", mr: "नवीन वर्षापासून मी ठरवलंय ... फेसबुक वर अजिबात वेळ घालवायचा नाही", roman: "navIn varShApAsUn mI TharavalMy ... Facebook var ajibAt veL ghAlavAyachA nAhI", hint: "" },
      { en: "If your eyes are good, you will fall in love of this world. But if your tongue is sweet, this whole world will fall in your love", mr: "जर तुमचे डोळे चांगले असतील तर तुम्ही या जगाच्या प्रेमात पडाल. पण तुमची जीभ गोड असेल तर हे संपूर्ण जग तुमच्या प्रेमात पडेल", roman: "jar tumache DoLe chAMgale asatIl tar tumhI yA jagAchyA premAt paDAl. paN tumachI jIbh goD asel tar he sMpUrN jag tumachyA premAt paDel", hint: "" },
      { en: "A relationship created by pure mind will never break", mr: "निर्मळ मानाने बनलेलं नातं कधीच तुटणार नाही", roman: "nirmaL mAnAne banalelM nAtM kadhIch tuTaNAr nAhI", hint: "" },
      { en: "Look at every problem as an opportunity", mr: "आयुष्यात येणाऱ्या प्रत्येक समस्येला सामोरे जाताना त्या समस्येकडे एक संधी म्हणून बघा", roman: "AyuShyAt yeNAryA pratyek samasyelA sAmore jAtAnA tyA samasyekaDe ek sMdhI mhaNUn baghA", hint: "" },
      { en: "I am not trying to be better than others but better than what I was yesterday", mr: "माझा प्रयत्न इतरांपेक्षा श्रेष्ठ होणे नसून मी जो काल होतो त्यापेक्षा आज चांगला होण्याचा आहे", roman: "mAjhA prayatn itarAMpekShA shreShTh hoNe nasUn mI jo kAl hoto tyApekShA Aj chAMgalA hoNyAchA Ahe", hint: "" }
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
    ,
      { en: "Digit", mr: "अंक", roman: "aMk", hint: "" },
      { en: "Fan", mr: "पंखा", roman: "paMkhA", hint: "" },
      { en: "Comb", mr: "कंगवा", roman: "kaMgava", hint: "" },
      { en: "Bath", mr: "आंघोळ", roman: "AMghoL", hint: "" },
      { en: "Set", mr: "संच", roman: "saMch", hint: "" },
      { en: "कंछ", mr: "कंछ", roman: "kaMCh", hint: "" },
      { en: "Thread for kite", mr: "मांजा", roman: "mAMjA", hint: "" },
      { en: "सांझ", mr: "सांझ", roman: "sAMjh", hint: "" },
      { en: "Bore", mr: "कंटाळा", roman: "kaMTALA", hint: "" },
      { en: "Dry ginger", mr: "सुंठ", roman: "suMTh", hint: "" },
      { en: "Pot", mr: "भांडे", roman: "bhAMDe", hint: "" },
      { en: "Eunuch", mr: "षंढ", roman: "ShaMDh", hint: "" },
      { en: "Saint", mr: "संत", roman: "saMt", hint: "" },
      { en: "Gradual", mr: "संथ", roman: "saMth", hint: "" },
      { en: "Close", mr: "बंद", roman: "baMd", hint: "" },
      { en: "Joint", mr: "सांधा", roman: "sAMdhA", hint: "" },
      { en: "To them", mr: "त्यांना", roman: "tyAMnA", hint: "" },
      { en: "Pump", mr: "पंप", roman: "paMp", hint: "" },
      { en: "अंफ", mr: "अंफ", roman: "aMph", hint: "" },
      { en: "Mango", mr: "आंबा", roman: "AMbA", hint: "" },
      { en: "Start", mr: "आरंभ", roman: "AraMbh", hint: "" },
      { en: "Approval", mr: "संमती", roman: "saMmatI", hint: "" },
      { en: "Part", mr: "अंश", roman: "aMsh", hint: "" },
      { en: "Bracket", mr: "कंस", roman: "kaMs", hint: "" },
      { en: "Term", mr: "संज्ञा", roman: "saMdnyA", hint: "" },
      { en: "Patience", mr: "संयम", roman: "saMyam", hint: "" },
      { en: "Dialogue", mr: "संवाद", roman: "saMvAd", hint: "" },
      { en: "Part", mr: "पार्ट", roman: "pArT", hint: "" },
      { en: "Harp", mr: "हार्प", roman: "hArp", hint: "" },
      { en: "Mark", mr: "मार्क", roman: "mArk", hint: "" },
      { en: "Support", mr: "साह्य", roman: "sAhy", hint: "" },
      { en: "External", mr: "बाह्य", roman: "bAhy", hint: "" },
      { en: "Brahman", mr: "ब्राह्मण", roman: "brAhmaN", hint: "" },
      { en: "A ritual", mr: "आह्निक", roman: "Ahnik", hint: "" }
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
    ,
      { en: "Body", mr: "शरीर", roman: "sharIr", hint: "" },
      { en: "Head", mr: "डोके", roman: "Doke", hint: "" },
      { en: "Brain", mr: "मेंदू", roman: "meMdU", hint: "" },
      { en: "Hairs", mr: "केस", roman: "kes", hint: "" },
      { en: "Face", mr: "चेहरा", roman: "cheharA", hint: "" },
      { en: "Forehead", mr: "कपाळ", roman: "kapAL", hint: "" },
      { en: "Eyebrow", mr: "भुवई", roman: "bhuvaI", hint: "" },
      { en: "Eyelid", mr: "पापणी", roman: "pApaNI", hint: "" },
      { en: "Eye", mr: "डोळा", roman: "DoLA", hint: "" },
      { en: "Eyeball", mr: "बुब्बुळ", roman: "bubbuL", hint: "" },
      { en: "Pupil", mr: "डोळ्याची बाहुली", roman: "DoLyAchI bAhulI", hint: "" },
      { en: "Nose", mr: "नाक", roman: "nAk", hint: "" },
      { en: "Nostril", mr: "नाकपुडी", roman: "nAkapuDI", hint: "" },
      { en: "Cheek", mr: "गाल", roman: "gAl", hint: "" },
      { en: "Ear", mr: "कान", roman: "kAn", hint: "" },
      { en: "Earlobe", mr: "कानाची पाळी", roman: "kAnAchI pALI", hint: "" },
      { en: "Moustache", mr: "मिशी", roman: "mishI", hint: "" },
      { en: "Lip", mr: "ओठ", roman: "oTh", hint: "" },
      { en: "Mouth", mr: "तोंड", roman: "toMD", hint: "" },
      { en: "Jaw", mr: "जबडा", roman: "jabaDA", hint: "" },
      { en: "Tooth", mr: "दात", roman: "dAt", hint: "" },
      { en: "Gum", mr: "हिरडी", roman: "hiraDI", hint: "" },
      { en: "Tongue", mr: "जीभ", roman: "jIbh", hint: "" },
      { en: "Beard", mr: "दाढी", roman: "dADhI", hint: "" },
      { en: "Whiskers", mr: "कल्ले", roman: "kalle", hint: "" },
      { en: "Chin", mr: "हनुवटी", roman: "hanuvaTI", hint: "" },
      { en: "Outerside of Throat", mr: "गळा", roman: "gaLA", hint: "" },
      { en: "Innerside of throat / Pharynx", mr: "घसा", roman: "ghasA", hint: "" },
      { en: "Neck", mr: "मान", roman: "mAn", hint: "" },
      { en: "Shoulder", mr: "खांदा", roman: "khAMdA", hint: "" },
      { en: "Breast", mr: "स्तन", roman: "stan", hint: "" },
      { en: "Chest", mr: "छाती", roman: "ChAtI", hint: "" },
      { en: "Heart", mr: "ह्रुदय", roman: "hruday", hint: "" },
      { en: "Lung", mr: "फुफ्फुस", roman: "phuphphus", hint: "" },
      { en: "Back", mr: "पाठ", roman: "pATh", hint: "" },
      { en: "Backbone", mr: "कणा", roman: "kaNA", hint: "" },
      { en: "Arm", mr: "दंड", roman: "daMD", hint: "" },
      { en: "Elbow", mr: "कोपर", roman: "kopar", hint: "" },
      { en: "Hand", mr: "हात", roman: "hAt", hint: "" },
      { en: "Wrist", mr: "मनगट", roman: "managaT", hint: "" },
      { en: "Palm", mr: "पंजा", roman: "paMjA", hint: "" },
      { en: "Sole of palm", mr: "तळहात", roman: "taLahAt", hint: "" },
      { en: "Fist", mr: "मूठ", roman: "mUTh", hint: "" },
      { en: "Finger", mr: "बोट", roman: "boT", hint: "" },
      { en: "Thumb", mr: "अंगठा", roman: "aMgaThA", hint: "" },
      { en: "Index finger", mr: "तर्जनी", roman: "tarjanI", hint: "" },
      { en: "Middle finger", mr: "मधले बोट", roman: "madhale boT", hint: "" },
      { en: "Ring finger", mr: "अनामिका", roman: "anAmikA", hint: "" },
      { en: "Small finger", mr: "करंगळी", roman: "karaMgaLI", hint: "" },
      { en: "Nail", mr: "नख", roman: "nakh", hint: "" },
      { en: "Stomach", mr: "पोट", roman: "poT", hint: "" },
      { en: "Belly button", mr: "बेंबी", roman: "beMbI", hint: "" },
      { en: "Waist", mr: "कंबर", roman: "kaMbar", hint: "" },
      { en: "Leg", mr: "पाय", roman: "pAy", hint: "" },
      { en: "Thigh", mr: "मांडी", roman: "mAMDI", hint: "" },
      { en: "Groin", mr: "जांघ", roman: "jAMgh", hint: "" },
      { en: "Penis", mr: "शिस्न", roman: "shisn", hint: "" },
      { en: "Vulva / Vagina", mr: "योनी", roman: "yonI", hint: "" },
      { en: "Buttocks / Hip", mr: "ढुंगण", roman: "DhuMgaN", hint: "" },
      { en: "Knee", mr: "गुडघा", roman: "guDaghA", hint: "" },
      { en: "Calf", mr: "पोटरी", roman: "poTarI", hint: "" },
      { en: "Ankle", mr: "घोटा", roman: "ghoTA", hint: "" },
      { en: "Foot", mr: "पाऊल", roman: "pAUl", hint: "" },
      { en: "Sole of foot", mr: "तळवा", roman: "taLavA", hint: "" },
      { en: "Heel", mr: "टाच", roman: "TAch", hint: "" },
      { en: "Toe", mr: "चवडा", roman: "chavaDA", hint: "" },
      { en: "Blood", mr: "रक्त", roman: "rakt", hint: "" },
      { en: "Bone", mr: "हाड", roman: "hAD", hint: "" },
      { en: "Joint", mr: "सांधा", roman: "sAMdhA", hint: "" },
      { en: "Ostrich", mr: "शहामृग", roman: "shahAmRug", hint: "" },
      { en: "Cock", mr: "कोंबडा", roman: "koMbaDA", hint: "" },
      { en: "Hen", mr: "कोंबडी", roman: "koMbaDI", hint: "" },
      { en: "Goose / Swan", mr: "हंस", roman: "haMs", hint: "" },
      { en: "Sparrow", mr: "चिमणी", roman: "chimaNI", hint: "" },
      { en: "Crane", mr: "बगळा", roman: "bagaLA", hint: "" },
      { en: "Stork", mr: "करकोचा", roman: "karakochA", hint: "" },
      { en: "Eagle", mr: "गरूड", roman: "garUD", hint: "" },
      { en: "Parrot", mr: "पोपट", roman: "popaT", hint: "" },
      { en: "Duck", mr: "बदक / बतख", roman: "badak / batakh", hint: "" },
      { en: "Owl", mr: "घुबड", roman: "ghubaD", hint: "" },
      { en: "Pigeon", mr: "कबूतर", roman: "kabUtar", hint: "" },
      { en: "Cuckoo", mr: "कोकिळा", roman: "kokiLA", hint: "" },
      { en: "Kite", mr: "घार", roman: "ghAr", hint: "" },
      { en: "Vulture", mr: "गिधाड", roman: "gidhAD", hint: "" },
      { en: "Woodpecker", mr: "सुतार", roman: "sutAr", hint: "" },
      { en: "Crow", mr: "कावळा", roman: "kAvaLA", hint: "" },
      { en: "Ant", mr: "मुंगी", roman: "muMgI", hint: "" },
      { en: "Bed bug", mr: "ढेकुण", roman: "DhekuN", hint: "" },
      { en: "Butterfly", mr: "फुलपाखरू", roman: "phulapAkharU", hint: "" },
      { en: "Spider", mr: "कोळी", roman: "koLI", hint: "" },
      { en: "Cockroach", mr: "झुरळ", roman: "jhuraL", hint: "" },
      { en: "Beetle", mr: "भुंगा", roman: "bhuMgA", hint: "" },
      { en: "Fly", mr: "माशी", roman: "mAshI", hint: "" },
      { en: "Mosquito", mr: "डास", roman: "DAs", hint: "" },
      { en: "Lizard", mr: "सरडा", roman: "saraDA", hint: "" },
      { en: "House Lizard", mr: "पाल", roman: "pAl", hint: "" },
      { en: "Grasshopper", mr: "नाकतोडा", roman: "nAkatoDA", hint: "" },
      { en: "Flea", mr: "पिसू", roman: "pisU", hint: "" },
      { en: "Centipede", mr: "गोम / घोण", roman: "gom / ghoN", hint: "" },
      { en: "Bear", mr: "अस्वल", roman: "asval", hint: "" },
      { en: "Buffalo", mr: "म्हैस", roman: "mhais", hint: "" },
      { en: "Camel", mr: "उंट", roman: "uMT", hint: "" },
      { en: "Cheetah", mr: "चित्ता", roman: "chittA", hint: "" },
      { en: "Deer", mr: "हरीण", roman: "harIN", hint: "" },
      { en: "Donkey", mr: "गाढव", roman: "gADhav", hint: "" },
      { en: "Fox", mr: "कोल्हा", roman: "kolhA", hint: "" },
      { en: "Frog", mr: "बेडूक", roman: "beDUk", hint: "" },
      { en: "Giraffe", mr: "जिराफ", roman: "jirAph", hint: "" },
      { en: "Goat", mr: "शेळी", roman: "sheLI", hint: "" },
      { en: "Male goat", mr: "बोकड", roman: "bokaD", hint: "" },
      { en: "Hippopotamus", mr: "पणघोडा", roman: "paNaghoDA", hint: "" },
      { en: "Lion", mr: "सिंह", roman: "siMh", hint: "" },
      { en: "Mongoose", mr: "मुंगूस", roman: "muMgUs", hint: "" },
      { en: "Ox", mr: "बैल", roman: "bail", hint: "" },
      { en: "Pig", mr: "डुक्कर", roman: "Dukkar", hint: "" },
      { en: "Rabbit", mr: "ससा", roman: "sasA", hint: "" },
      { en: "Mouse", mr: "उंदीर", roman: "uMdIr", hint: "" },
      { en: "Rhino", mr: "गेंडा", roman: "geMDA", hint: "" },
      { en: "Sheep", mr: "मेंढी", roman: "meMDhI", hint: "" },
      { en: "Squirrel", mr: "खार", roman: "khAr", hint: "" },
      { en: "Wolf", mr: "लांडगा", roman: "lAMDagA", hint: "" },
      { en: "Zebra", mr: "झेब्रा", roman: "jhebrA", hint: "" }
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
    ,
      { en: "We", mr: "आम्ही", roman: "AmhI", hint: "" },
      { en: "We (listener including)", mr: "आपण", roman: "ApaN", hint: "" },
      { en: "You (singular)", mr: "तू", roman: "tU", hint: "" },
      { en: "You (plural)", mr: "तुम्ही", roman: "tumhI", hint: "" },
      { en: "He / That (m.)", mr: "तो", roman: "to", hint: "" },
      { en: "She / That (f.)", mr: "ती", roman: "tI", hint: "" },
      { en: "It / That (n.)", mr: "ते", roman: "te", hint: "" },
      { en: "They (Plural of She) / Those (f.)", mr: "त्या", roman: "tyA", hint: "" },
      { en: "This (m.)", mr: "हा", roman: "hA", hint: "" },
      { en: "This (f.)", mr: "ही", roman: "hI", hint: "" },
      { en: "This (n.)", mr: "हे", roman: "he", hint: "" },
      { en: "These (f.)", mr: "ह्या", roman: "hyA", hint: "" },
      { en: "We went to the party (listener not included)", mr: "आम्ही पार्टीला गेलो", roman: "AmhI pArTIlA gelo", hint: "" },
      { en: "We went to the party (listener included)", mr: "आपण पार्टीला गेलो", roman: "ApaN pArTIlA gelo", hint: "" },
      { en: "Self", mr: "स्वतः", roman: "svataH", hint: "" },
      { en: "This is a horse", mr: "हा घोडा आहे", roman: "hA ghoDA Ahe", hint: "" },
      { en: "This is an ant", mr: "ही मुंगी आहे", roman: "hI muMgI Ahe", hint: "" },
      { en: "Sun", mr: "सूर्य", roman: "sUrya", hint: "" },
      { en: "Moon", mr: "चंद्र", roman: "chaMdra", hint: "" },
      { en: "Come", mr: "ये", roman: "ye", hint: "" },
      { en: "Go", mr: "जा", roman: "jA", hint: "" },
      { en: "Sit", mr: "बस", roman: "basa", hint: "" },
      { en: "Eat", mr: "खा", roman: "khA", hint: "" },
      { en: "Sing", mr: "गा", roman: "gA", hint: "" },
      { en: "Speak", mr: "बोल", roman: "bola", hint: "" },
      { en: "Listen", mr: "ऐक", roman: "aik", hint: "" },
      { en: "Beat", mr: "मार", roman: "mAr", hint: "" },
      { en: "Drink", mr: "पी", roman: "pI", hint: "" },
      { en: "Smile", mr: "हस", roman: "has", hint: "" },
      { en: "Write", mr: "लिही", roman: "lihI", hint: "" },
      { en: "Do", mr: "कर", roman: "kar", hint: "" },
      { en: "Get up", mr: "उठ", roman: "uTh", hint: "" },
      { en: "Sleep", mr: "झोप", roman: "jhop", hint: "" },
      { en: "Run", mr: "धाव", roman: "dhAv", hint: "" },
      { en: "Stop", mr: "थांब", roman: "thAMb", hint: "" },
      { en: "Open", mr: "उघड", roman: "ughaD", hint: "" },
      { en: "Close", mr: "बंद कर", roman: "baMd kar", hint: "" },
      { en: "See", mr: "बघ", roman: "bagh", hint: "" },
      { en: "I (male)", mr: "मी", roman: "to", hint: "" },
      { en: "He / That (male) / This (male)", mr: "तो / हा", roman: "to", hint: "" },
      { en: "She / That (female) / This (female)", mr: "ती / ही", roman: "te", hint: "" },
      { en: "It / That (neuter) / This (neuter)", mr: "ते / हे", roman: "te", hint: "" },
      { en: "They (f.) / Those (f.) / These (f.)", mr: "त्या / ह्या", roman: "tAt", hint: "" },
      { en: "I (male) do", mr: "मी करतो", roman: "mI karato", hint: "" },
      { en: "I (female) do", mr: "मी करते", roman: "mI karate", hint: "" },
      { en: "We dance", mr: "आम्ही/आपण नाचतो", roman: "AmhI/ApaN nAchato", hint: "" },
      { en: "You (male) cry", mr: "तू रडतोस", roman: "tU raDatos", hint: "" },
      { en: "You (female) cry", mr: "तू रडतेस", roman: "tU raDates", hint: "" },
      { en: "You (plural) walk", mr: "तुम्ही चालता", roman: "tumhI chAlatA", hint: "" },
      { en: "He walks", mr: "तो चालतो", roman: "to chAlato", hint: "" },
      { en: "She speaks", mr: "ती बोलते", roman: "tI bolate", hint: "" },
      { en: "It moves", mr: "ते हलते", roman: "te halate", hint: "" },
      { en: "They dance", mr: "ते/त्या/ती नाचतात", roman: "te/tyA/tI nAchatAt", hint: "" },
      { en: "I shall be doing.", mr: "मी करत असेन", roman: "mI karat asen", hint: "" },
      { en: "We will be dancing.", mr: "आम्ही/आपण नाचत असू", roman: "AmhI/ApaN nAchat asU", hint: "" },
      { en: "You will be crying.", mr: "तू रडत असशील", roman: "tU raDat asashIl", hint: "" },
      { en: "You (pl.) will be walking.", mr: "तुम्ही चालत असाल", roman: "tumhI chAlat asAl", hint: "" },
      { en: "He will be walking.", mr: "तो चालत असेल", roman: "to chAlat asel", hint: "" },
      { en: "She will be speaking.", mr: "ती बोलत असेल", roman: "tI bolat asel", hint: "" },
      { en: "It will be moving.", mr: "ते हलत असेल", roman: "te halat asel", hint: "" },
      { en: "They will be dancing.", mr: "ते/त्या/ती नाचत असतील", roman: "te/tyA/tI nAchat asatIl", hint: "" },
      { en: "He / That (m.) / This (m.)", mr: "तो / तो / हा", roman: "lA", hint: "" },
      { en: "She / That (f.) / This (f.)", mr: "ती / ती / ही", roman: "lI", hint: "" },
      { en: "It / That (n.) / This (n.)", mr: "ते / ते / हे", roman: "le", hint: "" },
      { en: "They (f.) / Those (f.) / These (f.)", mr: "त्या / त्या / ह्या", roman: "lyA", hint: "" },
      { en: "You (singular/plural)", mr: "तू / तुम्ही", roman: "tU / tumhI", hint: "" },
      { en: "They (all)", mr: "ते / त्या / ती", roman: "tyAMnI / hyAMnI", hint: "" },
      { en: "I (male) was doing.", mr: "मी करत होतो", roman: "mI karat hoto", hint: "" },
      { en: "I (female) was doing.", mr: "मी करत होते", roman: "mI karat hote", hint: "" },
      { en: "We were dancing.", mr: "आम्ही/आपण नाचत होतो", roman: "AmhI/ApaN nAchat hoto", hint: "" },
      { en: "You (male) were crying.", mr: "तू रडत होतास", roman: "tU raDat hotAs", hint: "" },
      { en: "You (female) were crying.", mr: "तू रडत होतीस", roman: "tU raDat hotIs", hint: "" },
      { en: "You (Plural) were walking", mr: "तुम्ही चालत होता", roman: "tumhI chAlat hotA", hint: "" },
      { en: "He was walking.", mr: "तो चालत होता", roman: "to chAlat hotA", hint: "" },
      { en: "She was speaking.", mr: "ती बोलत होती", roman: "tI bolat hotI", hint: "" },
      { en: "It was moving.", mr: "ते हलत होते", roman: "te halat hote", hint: "" },
      { en: "They(m.) were dancing.", mr: "ते नाचत होते", roman: "te nAchat hote", hint: "" },
      { en: "They(f.) were dancing.", mr: "त्या नाचत होत्या", roman: "tyA nAchat hotyA", hint: "" },
      { en: "They(n.) were dancing.", mr: "ती नाचत होती", roman: "tI nAchat hotI", hint: "" },
      { en: "She has opened door", mr: "तीने दरवाजा उघडला आहे", roman: "tIne daravAjA ughaDalA Ahe", hint: "" },
      { en: "She had opened door", mr: "तीने दरवाजा उघडला होता", roman: "tIne daravAjA ughaDalA hotA", hint: "" },
      { en: "She will have opened door", mr: "तीने दरवाजा उघडला असेल", roman: "tIne daravAjA ughaDalA asel", hint: "" },
      { en: "You (female) have danced", mr: "तू नाचली आहेस", roman: "tU nAchalI Ahes", hint: "" },
      { en: "You (female) had danced", mr: "तू नाचली होतीस", roman: "tU nAchalI hotIs", hint: "" },
      { en: "You (female) will have danced", mr: "तू नाचली असशील", roman: "tU nAchalI asashIl", hint: "" },
      { en: "You (plural) have danced", mr: "तुम्ही नाचला आहात", roman: "tumhI nAchalA AhAt", hint: "" },
      { en: "You (plural) had danced", mr: "तुम्ही नाचला होतात", roman: "tumhI nAchalA hotAt", hint: "" },
      { en: "You (plural) will have danced", mr: "तुम्ही नाचला असाल", roman: "tumhI nAchalA asAl", hint: "" },
      { en: "These (male/female/neuter)", mr: "हे / ह्या / ही", roman: "hyAMchyA / hyAM", hint: "" },
      { en: "about", mr: "बद्दल", roman: "baddal", hint: "" },
      { en: "Above", mr: "वर", roman: "var", hint: "" },
      { en: "across", mr: "पलिकडे", roman: "palikaDe", hint: "" },
      { en: "after", mr: "नंतर", roman: "naMtar", hint: "" },
      { en: "against", mr: "विरुद्ध", roman: "viruddh", hint: "" },
      { en: "Among", mr: "मध्ये", roman: "madhye", hint: "" },
      { en: "Around", mr: "भोवती", roman: "bhovatI", hint: "" },
      { en: "As/like", mr: "सारखा", roman: "sArakhA", hint: "" },
      { en: "aside", mr: "बाजुला", roman: "bAjulA", hint: "" },
      { en: "Before", mr: "आधी", roman: "AdhI", hint: "" },
      { en: "below", mr: "खाली", roman: "khAlI", hint: "" },
      { en: "for", mr: "साठी", roman: "sAThI", hint: "" },
      { en: "From/since", mr: "पासून / कडून", roman: "pAsUn / kaDUn", hint: "" },
      { en: "in", mr: "आत", roman: "At", hint: "" },
      { en: "outside", mr: "बाहेर", roman: "bAher", hint: "" },
      { en: "till/until", mr: "पर्यंत", roman: "paryaMt", hint: "" },
      { en: "without", mr: "शिवाय", roman: "shivAy", hint: "" },
      { en: "behind", mr: "मागे", roman: "mAge", hint: "" },
      { en: "during", mr: "दरम्यान", roman: "daramyAn", hint: "" },
      { en: "Near/close to", mr: "जवळ", roman: "javaL", hint: "" },
      { en: "towards", mr: "दिशेने", roman: "dishene", hint: "" },
      { en: "with", mr: "सोबत / बरोबर", roman: "sobat / barobar", hint: "" },
      { en: "Instead of", mr: "ऐवजी", roman: "aivajI", hint: "" },
      { en: "On behalf of", mr: "वतीने", roman: "vatIne", hint: "" },
      { en: "In front of", mr: "समोर", roman: "samor", hint: "" },
      { en: "Prior to", mr: "पूर्वी", roman: "pUrvI", hint: "" },
      { en: "Because of", mr: "मुळे", roman: "muLe", hint: "" },
      { en: "According to", mr: "अनुसार / प्रमाणे", roman: "anusAr / pramANe", hint: "" },
      { en: "Through", mr: "मधून", roman: "madhUn", hint: "" },
      { en: "With", mr: "शी", roman: "shI", hint: "" },
      { en: "These (male/female/neuter)", mr: "हे/ह्या/ही", roman: "hyAMnA", hint: "" },
      { en: "I do not speak", mr: "मी बोलत नाही", roman: "mI bolat nAhI", hint: "" },
      { en: "He does not walk", mr: "तो चालत नाही", roman: "to chAlat nAhI", hint: "" },
      { en: "You do not eat", mr: "तू खात नाहीस", roman: "tU khAt nAhIs", hint: "" },
      { en: "They do not dance", mr: "ते नाचत नाहीत", roman: "te nAchat nAhIt", hint: "" },
      { en: "I am not speaking", mr: "मी बोलत नाही आहे", roman: "mI bolat nAhI Ahe", hint: "" },
      { en: "He is not walking", mr: "तो चालत नाही आहे", roman: "to chAlat nAhI Ahe", hint: "" },
      { en: "She is not speaking", mr: "ती बोलत नाही आहे", roman: "tI bolat nAhI Ahe", hint: "" },
      { en: "It is not moving", mr: "ते हलत नाही आहे", roman: "te halat nAhI Ahe", hint: "" },
      { en: "They are not dancing", mr: "ते/त्या/ती नाचत नाही आहेत", roman: "te/tyA/tI nAchat nAhI Ahet", hint: "" },
      { en: "You are not dancing", mr: "तू नाचत नाही आहेस", roman: "tU nAchat nAhI Ahes", hint: "" },
      { en: "I have not opened the box", mr: "मी खोका उघडला नाही आहे", roman: "mI khokA ughaDalA nAhI Ahe", hint: "" },
      { en: "I have not spoken", mr: "मी बोललो नाही आहे", roman: "mI bolalo nAhI Ahe", hint: "" },
      { en: "He has not eaten the mango", mr: "त्याने आंबा खाल्ला नाही आहे", roman: "tyAne AMbA khAllA nAhI Ahe", hint: "" },
      { en: "You speak", mr: "तू बोल", roman: "tU bol", hint: "" },
      { en: "Read it", mr: "हे वाच", roman: "he vAch", hint: "" },
      { en: "Do it", mr: "हे कर", roman: "he kar", hint: "" },
      { en: "You go", mr: "तू जा", roman: "tU jA", hint: "" },
      { en: "You give", mr: "तू दे", roman: "tU de", hint: "" },
      { en: "You drink", mr: "तू पी", roman: "tU pI", hint: "" },
      { en: "You do not speak", mr: "तू बोलू नकोस", roman: "tU bolU nakos", hint: "" },
      { en: "Do not read it", mr: "हे वाचू नकोस", roman: "he vAchU nakos", hint: "" },
      { en: "Do not do it", mr: "हे करू नकोस", roman: "he karU nakos", hint: "" },
      { en: "You do not go", mr: "तू जाऊ नकोस", roman: "tU jAU nakos", hint: "" },
      { en: "To become होणे (hoNe)", mr: "हो", roman: "ho", hint: "" },
      { en: "To wash धूणे (dhUNe)", mr: "धू", roman: "dhU", hint: "" },
      { en: "To give देणे (deNe)", mr: "दे", roman: "de", hint: "" },
      { en: "To take घेणे (gheNe)", mr: "घे", roman: "ghe", hint: "" },
      { en: "To live राहणे (rAhaNe)", mr: "रहा", roman: "rahA", hint: "" },
      { en: "To write लिहिणे (lihiNe)", mr: "लिहा", roman: "lihA", hint: "" },
      { en: "To see पाहणे (pAhaNe)", mr: "पहा", roman: "pahA", hint: "" },
      { en: "Toy moved", mr: "खेळणे हलले", roman: "kheLaNe halale", hint: "" },
      { en: "I moved toy", mr: "मी खेळणे हलवले", roman: "mI kheLaNe halavale", hint: "" },
      { en: "To cook", mr: "शिजणे", roman: "shijaNe", hint: "" },
      { en: "To cause to cook", mr: "शिजवणे", roman: "shijavaNe", hint: "" },
      { en: "Rice cooked", mr: "भात शिजला", roman: "bhAt shijalA", hint: "" },
      { en: "I cooked rice", mr: "मी भात शिजवला", roman: "mI bhAt shijavalA", hint: "" },
      { en: "To die", mr: "मरणे", roman: "maraNe", hint: "" },
      { en: "To cause to die / To kill", mr: "मारणे", roman: "mAraNe", hint: "" },
      { en: "To fall", mr: "पडणे", roman: "paDaNe", hint: "" },
      { en: "To cause to fall", mr: "पाडणे", roman: "pADaNe", hint: "" },
      { en: "To break (intransitive)", mr: "फुटणे", roman: "phuTaNe", hint: "" },
      { en: "To cause to break", mr: "फोडणे", roman: "phoDaNe", hint: "" },
      { en: "Glass broke", mr: "ग्लास फुटला", roman: "glAs phuTalA", hint: "" },
      { en: "I broke glass", mr: "मी ग्लास फोडला", roman: "mI glAs phoDalA", hint: "" },
      { en: "To leave", mr: "सुटणे", roman: "suTaNe", hint: "" },
      { en: "To cause to leave", mr: "सोडणे", roman: "soDaNe", hint: "" },
      { en: "To drink", mr: "पीणे", roman: "pINe", hint: "" },
      { en: "To cause to drink / To feed liquid", mr: "पाजणे", roman: "pAjaNe", hint: "" },
      { en: "To eat", mr: "खाणे", roman: "khANe", hint: "" },
      { en: "To feed", mr: "भरवणे", roman: "bharavaNe", hint: "" },
      { en: "To speak", mr: "बोलणे", roman: "bolaNe", hint: "" },
      { en: "To call (not cause to speak)", mr: "बोलवणे", roman: "bolavaNe", hint: "" },
      { en: "To run", mr: "पळणे", roman: "paLaNe", hint: "" },
      { en: "To keep animal (not cause to run)", mr: "पाळणे", roman: "pALaNe", hint: "" },
      { en: "my", mr: "माझा", roman: "mAjhA", hint: "" },
      { en: "speaking", mr: "बोलणारा", roman: "bolaNArA", hint: "" },
      { en: "want", mr: "हवा", roman: "havA", hint: "" },
      { en: "grey", mr: "करडा", roman: "karaDA", hint: "" },
      { en: "how / what kind (कसा)", mr: "कसा-कशी-कसे-कसे-कश्या-कशी", roman: "kasA-kashI-kase-kase-kashyA-kashI", hint: "" },
      { en: "my", mr: "माझा-माझी-माझे-माझे-माझ्या-माझी", roman: "mAjhA-mAjhI-mAjhe-mAjhe-mAjhyA-mAjhI", hint: "" },
      { en: "your", mr: "तुझा-तुझी-तुझे-तुझे-तुझ्या-तुझी", roman: "tujhA-tujhI-tujhe-tujhe-tujhyA-tujhI", hint: "" },
      { en: "his", mr: "त्याचा-त्याची-त्याचे-त्याचे-त्याच्या-त्याची", roman: "tyAchA-tyAchI-tyAche-tyAche-tyAchyA-tyAchI", hint: "" },
      { en: "Ram's", mr: "रामचा-रामची-रामचे-रामचे-रामच्या-रामची", roman: "rAmachA-rAmachI-rAmache-rAmache-rAmachyA-rAmachI", hint: "" },
      { en: "which", mr: "जो-जी-जे-जे-ज्या-जी", roman: "jo-jI-je-je-jyA-jI", hint: "" },
      { en: "fresh", mr: "ताजा-ताजी-ताजे-ताजे-ताज्या-ताजी", roman: "tAjA-tAjI-tAje-tAje-tAjyA-tAjI", hint: "" },
      { en: "I had spoken", mr: "मी बोललेलो", roman: "mI bolalelo", hint: "" },
      { en: "You (male) had danced", mr: "तू नाचलेलास", roman: "tU nAchalelAs", hint: "" },
      { en: "He had laughed", mr: "तो हसलेला", roman: "to hasalelA", hint: "" },
      { en: "Those boys had laughed", mr: "ते मुलगे हसलेले", roman: "te mulage hasalele", hint: "" },
      { en: "I had opened door", mr: "मी दरवाजा उघडलेला", roman: "mI daravAjA ughaDalelA", hint: "" },
      { en: "I had opened window", mr: "मी खिडकी उघडलेली", roman: "mI khiDakI ughaDalelI", hint: "" },
      { en: "She had eaten mango", mr: "तीने आंबा खाल्लेला", roman: "tIne AMbA khAllelA", hint: "" },
      { en: "Those girls had picked keys", mr: "त्या मुलींनी किल्ल्या उचललेल्या", roman: "tyA mulIMnI killyA uchalalelyA", hint: "" },
      { en: "I have spoken", mr: "मी बोललेलो आहे", roman: "mI bolalelo Ahe", hint: "" },
      { en: "I will have spoken", mr: "मी बोललेलो असेन", roman: "mI bolalelo asen", hint: "" },
      { en: "He had been saying", mr: "तो बोलत होता", roman: "to bolat hotA", hint: "" },
      { en: "He has been saying", mr: "तो बोलत आहे", roman: "to bolat Ahe", hint: "" },
      { en: "He will have been saying", mr: "तो बोलत असेल", roman: "to bolat asel", hint: "" },
      { en: "I have been saying", mr: "मी बोलत आलो आहे", roman: "mI bolat Alo Ahe", hint: "" },
      { en: "She has been saying", mr: "ती बोलत आली आहे", roman: "tI bolat AlI Ahe", hint: "" },
      { en: "They have been dancing", mr: "ते नाचत आले आहेत", roman: "te nAchat Ale Ahet", hint: "" },
      { en: "You have been eating mango", mr: "तुम्ही आंबा खात आला आहात", roman: "tumhI AMbA khAt AlA AhAt", hint: "" },
      { en: "I have been working there for 3 years", mr: "मी तिकडे ३ वर्षे काम करत आलो आहे", roman: "mI tikaDe 3 varShe kAm karat Alo Ahe", hint: "" },
      { en: "I had been saying", mr: "मी बोलत आलो होतो", roman: "mI bolat Alo hoto", hint: "" },
      { en: "She had been saying", mr: "ती बोलत आली होती", roman: "tI bolat AlI hotI", hint: "" },
      { en: "They had been dancing", mr: "ते नाचत आले होते", roman: "te nAchat Ale hote", hint: "" },
      { en: "You had been eating mango", mr: "तुम्ही आंबा खात आला होतात", roman: "tumhI AMbA khAt AlA hotAt", hint: "" },
      { en: "She will have been saying", mr: "ती बोलत आली असेल", roman: "tI bolat AlI asel", hint: "" },
      { en: "They will have been dancing", mr: "ते नाचत आले असतील", roman: "te nAchat Ale asatIl", hint: "" },
      { en: "You will have been eating mango", mr: "तुम्ही आंबा खात आला असाल", roman: "tumhI AMbA khAt AlA asAl", hint: "" },
      { en: "I will have been working there for 3 years", mr: "मी तिकडे ३ वर्षे काम करत आलो असेन", roman: "mI tikaDe 3 varShe kAm karat Alo asen", hint: "" },
      { en: "They are going to come", mr: "ते येणार आहेत", roman: "te yeNAr Ahet", hint: "" },
      { en: "I am going to speak", mr: "मी बोलणार आहे", roman: "mI bolaNAr Ahe", hint: "" },
      { en: "She is going to open door", mr: "ती दार उघडणार आहे", roman: "tI dAr ughaDaNAr Ahe", hint: "" },
      { en: "You are going to dance", mr: "तू नाचणार आहेस", roman: "tU nAchaNAr Ahes", hint: "" },
      { en: "Are they going to come?", mr: "ते येणार आहेत का", roman: "te yeNAr Ahet kA", hint: "" },
      { en: "Am I going to speak?", mr: "मी बोलणार आहे का", roman: "mI bolaNAr Ahe kA", hint: "" },
      { en: "Is she going to open door?", mr: "ती दार उघडणार आहे का", roman: "tI dAr ughaDaNAr Ahe kA", hint: "" },
      { en: "Are you going to dance?", mr: "तू नाचणार आहेस का", roman: "tU nAchaNAr Ahes kA", hint: "" },
      { en: "I used to do", mr: "मी करायचो", roman: "mI karAyacho", hint: "" },
      { en: "She used to speak", mr: "ती बोलायची", roman: "tI bolAyachI", hint: "" },
      { en: "He used to dance", mr: "तो नाचायचा", roman: "to nAchAyachA", hint: "" },
      { en: "They (plural of he) used to eat mangos", mr: "ते आंबे खायचे", roman: "te AMbe khAyache", hint: "" },
      { en: "They (plural of she) used to play cricket", mr: "त्या क्रिकेट खेळायच्या", roman: "tyA krikeT kheLAyachyA", hint: "" },
      { en: "He used to be there", mr: "तो तिकडे असायचा", roman: "to tikaDe asAyachA", hint: "" },
      { en: "She used to be quiet", mr: "ती शांत असायची", roman: "tI shAMt asAyachI", hint: "" },
      { en: "I did not use to do", mr: "मी करायचो नाही", roman: "mI karAyacho nAhI", hint: "" },
      { en: "She did not use to speak", mr: "ती बोलायची नाही", roman: "tI bolAyachI nAhI", hint: "" },
      { en: "You did not use to dance", mr: "तू नाचायचा नाहीस", roman: "tU nAchAyachA nAhIs", hint: "" },
      { en: "They (plural of he) did not use to eat mangos", mr: "ते आंबे खायचे नाहीत", roman: "te AMbe khAyache nAhIT", hint: "" },
      { en: "She did not use to be quiet", mr: "ती शांत असायची नाही", roman: "tI shAMt asAyachI nAhI", hint: "" },
      { en: "He did not use to be there", mr: "तो तिकडे नसायचा", roman: "to tikaDe nasAyachA", hint: "" },
      { en: "She did not use to be quiet", mr: "ती शांत नसायची", roman: "tI shAMt nasAyachI", hint: "" },
      { en: "He is used to dance", mr: "तो नाचत असतो", roman: "to nAchat asato", hint: "" },
      { en: "She is used to speak", mr: "ती बोलत असते", roman: "tI bolat asate", hint: "" },
      { en: "Those girls are used to laugh", mr: "त्या मुली हसत असतात", roman: "tyA mulI hasat asatAt", hint: "" },
      { en: "I am used to be there", mr: "मी तिकडे असतो", roman: "mI tikaDe asato", hint: "" },
      { en: "She is used to be quiet", mr: "ती शांत असते", roman: "tI shAMt asate", hint: "" },
      { en: "He is not used to dance", mr: "तो नाचत नसतो", roman: "to nAchat nasato", hint: "" },
      { en: "She is not used to speak", mr: "ती बोलत नसते", roman: "tI bolat nasate", hint: "" },
      { en: "I used to eat mango", mr: "मी आंबा खात असे", roman: "mI AMbA khAt ase", hint: "" },
      { en: "Kaushik used to eat mango", mr: "कौशिक आंबा खात असे", roman: "kaushik AMbA khAt ase", hint: "" },
      { en: "Kaushik, Guru, sundar used to meet every day", mr: "कौशिक,गुरू,सुंदर रोज भेटत असत", roman: "kaushik,gurU,suMdar roj bheTat asat", hint: "" },
      { en: "My friends and I used to play cricket", mr: "माझे मित्र आणि मी क्रिकेट खेळत असू", roman: "mAjhe mitr ANi mI krikeT kheLat asU", hint: "" },
      { en: "I used to eat mango", mr: "मी आंबा खाई", roman: "mI AMbA khAI", hint: "" },
      { en: "Kaushik used to eat mango", mr: "कौशिक आंबा खाई", roman: "kaushik AMbA khAI", hint: "" },
      { en: "I used to see", mr: "मी बघे/बघी", roman: "mI baghe/baghI", hint: "" },
      { en: "Kaushik used to see", mr: "कौशिक बघे/बघी", roman: "kaushik baghe/baghI", hint: "" },
      { en: "I used to do", mr: "मी करे/करी", roman: "mI kare/karI", hint: "" },
      { en: "Kaushik used to do", mr: "कौशिक करे/करी", roman: "kaushik kare/karI", hint: "" },
      { en: "He opened the door", mr: "त्याने दार उघडले", roman: "tyAne dAr ughaDale", hint: "" },
      { en: "If he had opened the door then", mr: "त्याने दार उघडले असते तर", roman: "tyAne dAr ughaDale asate tar", hint: "" },
      { en: "He had spoken", mr: "तो बोलला होता", roman: "to bolalA hotA", hint: "" },
      { en: "If he had spoken", mr: "तो बोलला असता तर", roman: "to bolalA asatA tar", hint: "" },
      { en: "If you had spoken then she would have spoken", mr: "जर तू बोलला असतास तर ती बोलली असती", roman: "jar tU bolalA asatAs tar tI bolalI asatI", hint: "" },
      { en: "If he had cried then they would have ran", mr: "जर तो रडला असता तर ते धावले असते", roman: "jar to raDalA asatA tar te dhavale asate", hint: "" },
      { en: "If you go I will cry", mr: "जर तू गेलास तर मी रडेन", roman: "jar tU gelAs tar mI raDen", hint: "" },
      { en: "If he sings she will dance", mr: "तो गायला तर ती नाचेल", roman: "to gAyalA tar tI nAchel", hint: "" },
      { en: "do", mr: "कर (kar)", roman: "karaNyA", hint: "" },
      { en: "speak", mr: "बोल (bol)", roman: "bolaNyA", hint: "" },
      { en: "dance", mr: "नाच (nAch)", roman: "nAchaNyA", hint: "" },
      { en: "About speaking", mr: "बोलण्याबद्दल", roman: "bolaNyAbaddal", hint: "" },
      { en: "For eating", mr: "खाण्यासाठी", roman: "khANyAsAThI", hint: "" },
      { en: "reason of coming", mr: "येण्याचे कारण", roman: "yeNyAche kAraN", hint: "" },
      { en: "She spoke after my dancing", mr: "माझ्या नाचण्यानंतर ती गायली", roman: "mAjhyA nAchaNyAnaMtar tI gAyalI", hint: "" },
      { en: "after I danced", mr: "नाचल्यानंतर", roman: "nAchalyAnaMtar", hint: "" },
      { en: "She spoke after I danced", mr: "मी नाचल्यानंतर ती बोलली", roman: "mI nAchalyAnaMtar tI bolalI", hint: "" },
      { en: "He cried after she went", mr: "ती गेल्यानंतर तो रडला", roman: "tI gelyAnaMtar to raDalA", hint: "" },
      { en: "He told about his coming to school", mr: "तो शाळेत आल्याचे त्याने मला सांगितले", roman: "to shALet AlyAche tyAne malA sAMgitale", hint: "" },
      { en: "He told me that he is coming", mr: "तो शाळेत येत असल्याचे त्याने मला सांगितले", roman: "to shALet yet asalyAche tyAne malA sAMgitale", hint: "" },
      { en: "He told me that he is going to come", mr: "तो शाळेत येणार असल्याचे त्याने मला सांगितले", roman: "to shALet yeNAr asalyAche tyAne malA sAMgitale", hint: "" },
      { en: "I don't remember she having said something", mr: "ती असे काही बोलली असल्याचे मला आठवत नाही", roman: "tI ase kAhI bolalI asalyAche malA AThavat nAhI", hint: "" },
      { en: "I don't remember she having eaten mango", mr: "तीने आंबा खाल्ल्याचे मला आठवत नाही", roman: "tIne AMbA khAllyAche malA AThavat nAhI", hint: "" },
      { en: "while I speak", mr: "बोलताना", roman: "bolatAnA", hint: "" },
      { en: "while I do", mr: "करताना", roman: "karatAnA", hint: "" },
      { en: "while I dance", mr: "नाचताना", roman: "nAchatAnA", hint: "" },
      { en: "while speaking", mr: "बोलत असताना", roman: "bolat asatAnA", hint: "" },
      { en: "while doing", mr: "करत असताना", roman: "karat asatAnA", hint: "" },
      { en: "while dancing", mr: "नाचत असताना", roman: "nAchat asatAnA", hint: "" },
      { en: "to see", mr: "बघायला", roman: "baghAyalA", hint: "" },
      { en: "to do", mr: "करायला", roman: "karAyalA", hint: "" },
      { en: "to speak", mr: "बोलायला", roman: "bolAyalA", hint: "" },
      { en: "to dance", mr: "नाचायला", roman: "nAchAyalA", hint: "" },
      { en: "Come to see this photo", mr: "फोटो बघायला ये", roman: "phoTo baghAyalA ye", hint: "" },
      { en: "Come to eat with me", mr: "माझ्याबरोबर जेवायला ये", roman: "mAjhyAbarobar jevAyalA ye", hint: "" },
      { en: "to see", mr: "बघण्यास", roman: "baghaNyAs", hint: "" },
      { en: "to do", mr: "करण्यास", roman: "karaNyAs", hint: "" },
      { en: "to speak", mr: "बोलण्यास", roman: "bolaNyAs", hint: "" },
      { en: "to dance", mr: "नाचण्यास", roman: "nAchaNyAs", hint: "" },
      { en: "Come to see this photo", mr: "फोटो बघण्यास ये", roman: "phoTo baghaNyAs ye", hint: "" },
      { en: "Smoking is prohibited", mr: "धूम्रपान करण्यास मनाई आहे", roman: "dhUmrapAn karaNyAs manAI Ahe", hint: "" },
      { en: "Court asked to be present tomorrow", mr: "न्यायालयाने उद्या हजर राहण्यास सांगितले", roman: "nyAyAlayAne udyA hajar rAhaNyAs sAMgitale", hint: "" },
      { en: "Sit and watch", mr: "बसून बघ", roman: "basUn bagh", hint: "" },
      { en: "come and go", mr: "येऊन जा", roman: "yeUn jA", hint: "" },
      { en: "He came and saw it", mr: "त्याने येऊन बघितले", roman: "tyAne yeUn baghitale", hint: "" },
      { en: "They will go and check it", mr: "ते जाऊन तपासतील", roman: "te jAUn tapAsatIl", hint: "" },
      { en: "smile and say", mr: "हसून बोल", roman: "hasoon bol", hint: "" },
      { en: "till I speak", mr: "मी बोले पर्यंत", roman: "mI bole paryaMt", hint: "" },
      { en: "until she smiles", mr: "ती हसे पर्यंत", roman: "tI hase paryaMt", hint: "" },
      { en: "till he goes", mr: "तो जाई पर्यंत", roman: "to jAI paryaMt", hint: "" },
      { en: "until we come", mr: "आम्ही येई पर्यंत", roman: "AmhI yeI paryaMt", hint: "" },
      { en: "Black horse", mr: "काळा घोडा", roman: "kALA ghoDA", hint: "" },
      { en: "Black chair", mr: "काळी खुर्ची", roman: "kALI khurchI", hint: "" },
      { en: "Black page", mr: "काळे पान", roman: "kALe pAn", hint: "" },
      { en: "Black horses", mr: "काळे घोडे", roman: "kALe ghoDe", hint: "" },
      { en: "Black chairs", mr: "काळ्या खुर्च्या", roman: "kALyA khurchyA", hint: "" },
      { en: "Black pages", mr: "काळी पाने", roman: "kALI pAne", hint: "" },
      { en: "Good horse", mr: "चांगला घोडा", roman: "chAMgalA ghoDA", hint: "" },
      { en: "For good horse", mr: "चांगल्या घोड्या साठी", roman: "chAMgalyA ghoDyA sAThI", hint: "" },
      { en: "Good chair", mr: "चांगली खुर्ची", roman: "chAMgalI khurchI", hint: "" },
      { en: "For good chair", mr: "चांगल्या खुर्ची साठी", roman: "chAMgalyA khurchI sAThI", hint: "" },
      { en: "Easy exam", mr: "सोपी परीक्षा", roman: "sopI parIkShA", hint: "" },
      { en: "After easy exam", mr: "सोप्या परीक्षेनंतर", roman: "sopyA parIkShenaMtar", hint: "" },
      { en: "Red horse", mr: "लाल घोडा", roman: "lAl ghoDA", hint: "" },
      { en: "For red horse", mr: "लाल घोड्यासाठी", roman: "lAl ghoDyAsAThI", hint: "" },
      { en: "Beautiful drawing", mr: "सुंदर चित्र", roman: "suMdar chitr", hint: "" },
      { en: "About beautiful drawing", mr: "सुंदर चित्राबद्दल", roman: "suMdar chitrAbaddal", hint: "" },
      { en: "Talking boy", mr: "बोलणारा मुलगा", roman: "bolaNArA mulagA", hint: "" },
      { en: "Rotating fan", mr: "फिरणारा पंखा", roman: "phiraNArA paMkhA", hint: "" },
      { en: "Talking girl", mr: "बोलणारी मुलगी", roman: "bolaNArI mulagI", hint: "" },
      { en: "Moving chair", mr: "हलणारी खुर्ची", roman: "halaNArI khurchI", hint: "" },
      { en: "Flying saucer", mr: "उडणारी तबकडी", roman: "uDaNArI tabakaDI", hint: "" },
      { en: "Talking book", mr: "बोलणारे पुस्तक", roman: "bolaNAre pustak", hint: "" },
      { en: "Moving tree", mr: "हलणारे झाड", roman: "halaNAre jhAD", hint: "" },
      { en: "Talked boy", mr: "बोललेला मुलगा", roman: "bolalelA mulagA", hint: "" },
      { en: "Rotated fan", mr: "फिरलेला पंखा", roman: "phiralelA paMkhA", hint: "" },
      { en: "Talked girl", mr: "बोललेली मुलगी", roman: "bolalelI mulagI", hint: "" },
      { en: "Moved chair", mr: "हललेली खुर्ची", roman: "halalelI khurchI", hint: "" },
      { en: "Flown saucer", mr: "उडलेली तबकडी", roman: "uDalelI tabakaDI", hint: "" },
      { en: "Talked book", mr: "बोललेले पुस्तक", roman: "bolalele pustak", hint: "" },
      { en: "Moved tree", mr: "हललेले झाड", roman: "halalele jhAD", hint: "" },
      { en: "I can eat", mr: "मी खाऊ शकतो", roman: "mI khAU shakato", hint: "" },
      { en: "He can sing", mr: "तो गाऊ शकतो", roman: "to gAU shakato", hint: "" },
      { en: "You(plural) could eat mango", mr: "तुम्ही आंबा खाऊ शकलात", roman: "tumhI AMbA khAU shakalAt", hint: "" },
      { en: "You(plural) could eat chutney", mr: "तुम्ही चटणी खाऊ शकलात", roman: "tumhI chaTaNI khAU shakalAt", hint: "" },
      { en: "She could dance", mr: "ती नाचू शकली", roman: "tI nAchU shakalI", hint: "" },
      { en: "They (plural of she) will be able to move", mr: "त्या हलू शकतील", roman: "tyA halU shakatIl", hint: "" },
      { en: "I can not eat", mr: "मी खाऊ शकत नाही", roman: "mI khAU shakat nAhI", hint: "" },
      { en: "He can not sing", mr: "तो गाऊ शकत नाही", roman: "to gAU shakat nAhI", hint: "" },
      { en: "She could not dance", mr: "ती नाचू शकली नाही", roman: "tI nAchU shakalI nAhI", hint: "" },
      { en: "You(plural) could not eat mango", mr: "तुम्ही आंबा खाऊ शकला नाहीत", roman: "tumhI AMbA khAU shakalA nAhIt", hint: "" },
      { en: "You(plural) could not eat chutney", mr: "तुम्ही चटणी खाऊ शकला नाहीत", roman: "tumhI chaTaNI khAU shakalA nAhIt", hint: "" },
      { en: "They will not be able to move", mr: "त्या हलू शकणार नाहीत", roman: "tyA halU shakaNAr nAhIt", hint: "" },
      { en: "I can play cricket", mr: "मला क्रिकेट खेळायला जमते", roman: "malA krikeT kheLAyalA jamate", hint: "" },
      { en: "I could play cricket", mr: "मला क्रिकेट खेळायला जमले", roman: "malA krikeT kheLAyalA jamale", hint: "" },
      { en: "I will be able to play cricket", mr: "मला क्रिकेट खेळायला जमेल", roman: "malA krikeT kheLAyalA jamel", hint: "" },
      { en: "He can eat mangoes", mr: "त्याला आंबे खायला जमते", roman: "tyAlA AMbe khAyalA jamate", hint: "" },
      { en: "He could eat mangoes", mr: "त्याला आंबे खायला जमले", roman: "tyAlA AMbe khAyalA jamale", hint: "" },
      { en: "He will be able to eat mangoes", mr: "त्याला आंबे खायला जमेल", roman: "tyAlA AMbe khAyalA jamel", hint: "" },
      { en: "They could open box", mr: "त्यांना खोका उघडायला जमला", roman: "tyAMnA khokA ughaDAyalA jamalA", hint: "" },
      { en: "They could open bag", mr: "त्यांना पेटी उघडायला जमली", roman: "tyAMnA peTI ughaDAyalA jamalI", hint: "" },
      { en: "They could speak", mr: "त्यांना बोलायला जमले", roman: "tyAMnA bolAyalA jamale", hint: "" },
      { en: "They gathered to speak", mr: "ते बोलायला जमले", roman: "te bolAyalA jamale", hint: "" },
      { en: "I want mango", mr: "मला आंबा पाहिजे/हवा आहे", roman: "malA AMbA pAhije/havA Ahe", hint: "" },
      { en: "He wants mango", mr: "त्याला आंबा पाहिजे/हवा आहे", roman: "tyAlA AMbA pAhije/havA Ahe", hint: "" },
      { en: "She wants mango", mr: "तीला आंबा पाहिजे/हवा आहे", roman: "tIlA AMbA pAhije/havA Ahe", hint: "" },
      { en: "I/He/She want mangoes", mr: "मला/त्याला/तीला आंबे पाहिजे/हवे आहेत", roman: "malA/tyAlA/tIlA AMbe pAhije/have Ahet", hint: "" },
      { en: "He/She/They want chalk", mr: "त्याला/तीला/त्यांना खडू पाहिजे/हवा आहे", roman: "tyAlA/tIlA/tyAMnA khaDU pahije/havA Ahe", hint: "" },
      { en: "He/She/They want chalks", mr: "त्याला/तीला/त्यांना खडू पाहिजे/हवे आहेत", roman: "tyAlA/tIlA/tyAMnA khaDU pahije/have Ahet", hint: "" },
      { en: "He/She/They want bag", mr: "त्याला/तीला/त्यांना पेटी पाहिजे/हवी आहे", roman: "tyAlA/tIlA/tyAMnA peTI pahije/havI Ahe", hint: "" },
      { en: "He/She/They want bags", mr: "त्याला/तीला/त्यांना पेट्या पाहिजे/हव्या आहेत", roman: "tyAlA/tIlA/tyAMnA peTyA pahije/havyA Ahet", hint: "" },
      { en: "He/She/They want page", mr: "त्याला/तीला/त्यांना पान पाहिजे/हवे आहे", roman: "tyAlA/tIlA/tyAMnA pAn pahije/have Ahe", hint: "" },
      { en: "He/She/They want pages", mr: "त्याला/तीला/त्यांना पाने पाहिजे/हवी आहेत", roman: "tyAlA/tIlA/tyAMnA pAne pahije/havI Ahet", hint: "" },
      { en: "He/She/They wanted chalk", mr: "त्याला/तीला/त्यांना खडू पाहिजे/हवा होता", roman: "tyAlA/tIlA/tyAMnA khaDU pahije/havA hotA", hint: "" },
      { en: "He/She/They wanted chalks", mr: "त्याला/तीला/त्यांना खडू पाहिजे/हवे होते", roman: "tyAlA/tIlA/tyAMnA khaDU pahije/have hote", hint: "" },
      { en: "He/She/They wanted bag", mr: "त्याला/तीला/त्यांना पेटी पाहिजे/हवी होती", roman: "tyAlA/tIlA/tyAMnA peTI pahije/havI hotI", hint: "" },
      { en: "He/She/They wanted bags", mr: "त्याला/तीला/त्यांना पेट्या पाहिजे/हव्या होत्या", roman: "tyAlA/tIlA/tyAMnA peTyA pahije/havyA hotyA", hint: "" },
      { en: "He/She/They wanted page", mr: "त्याला/तीला/त्यांना पान पाहिजे/हवे होते", roman: "tyAlA/tIlA/tyAMnA pAn pahije/have hote", hint: "" },
      { en: "He/She/They wanted pages", mr: "त्याला/तीला/त्यांना पाने पाहिजे/हवी होती", roman: "tyAlA/tIlA/tyAMnA pAne pahije/havI hotI", hint: "" },
      { en: "He/She/They will need chalk", mr: "त्याला/तीला/त्यांना खडू पाहिजे/हवा असेल", roman: "tyAlA/tIlA/tyAMnA khaDU pahije/havA asel", hint: "" },
      { en: "He/She/They will need chalks", mr: "त्याला/तीला/त्यांना खडू पाहिजे/हवे असतील", roman: "tyAlA/tIlA/tyAMnA khaDU pahije/have asatIl", hint: "" },
      { en: "He/She/They will need bag", mr: "त्याला/तीला/त्यांना पेटी पाहिजे/हवी असेल", roman: "tyAlA/tIlA/tyAMnA peTI pahije/havI asel", hint: "" },
      { en: "He/She/They will need bags", mr: "त्याला/तीला/त्यांना पेट्या पाहिजे/हव्या असतील", roman: "tyAlA/tIlA/tyAMnA peTyA pahije/havyA asatIl", hint: "" },
      { en: "He/She/They will need page", mr: "त्याला/तीला/त्यांना पान पाहिजे/हवे असेल", roman: "tyAlA/tIlA/tyAMnA pAn pahije/have asel", hint: "" },
      { en: "He/She/They will need pages", mr: "त्याला/तीला/त्यांना पाने पाहिजे/हवी असतील", roman: "tyAlA/tIlA/tyAMnA pAne pahije/havI asatIl", hint: "" },
      { en: "I do not want mango", mr: "मला आंबा नको आहे", roman: "malA AMbA nako Ahe", hint: "" },
      { en: "She will not want bag", mr: "तीला पेटी नको असेल", roman: "tIlA peTI nako asel", hint: "" },
      { en: "He did not want chalk", mr: "त्याला खडू नको होता", roman: "tyAlA khaDU nako hotA", hint: "" },
      { en: "He did not want bag", mr: "त्याला पेटी नको होती", roman: "tyAlA peTI nako hotI", hint: "" },
      { en: "I do not want mango", mr: "मला आंबा नाही पाहिजे", roman: "malA AMbA nAhI pAhije", hint: "" },
      { en: "She does not want ice cream", mr: "तीला आईसक्रीम नाही पाहिजे", roman: "tIlA AIskrIm nAhI pAhije", hint: "" },
      { en: "He did not want chalk", mr: "त्याला खडू नाही पाहिजे होता", roman: "tyAlA khaDU nAhI pAhije hotA", hint: "" },
      { en: "What happened?", mr: "काय झाले?", roman: "kAy jhAle?", hint: "" },
      { en: "What will happen?", mr: "काय होईल?", roman: "kAy hoIl?", hint: "" },
      { en: "What is happening?", mr: "काय होत आहे?", roman: "kAy hot Ahe?", hint: "" },
      { en: "It did not happen", mr: "हे झाले नाही", roman: "he jhAle nAhI", hint: "" },
      { en: "I will become winner", mr: "मी विजेता होईन", roman: "mI vijetA hoIn", hint: "" },
      { en: "It was happening", mr: "ते होत होते", roman: "te hot hote", hint: "" },
      { en: "He will become mad", mr: "तो वेडा होईल", roman: "to veDA hoIl", hint: "" },
      { en: "He should have eaten mango", mr: "त्याने आंबा खायला पाहिजे/हवा होता", roman: "tyAne AMbA khAyalA pAhije/havA hotA", hint: "" },
      { en: "He should have eaten tamarind", mr: "त्याने चिंच खायला पाहिजे/हवी होती", roman: "tyAne chiMch khAyalA pAhije/havI hotI", hint: "" },
      { en: "He should eat mango", mr: "त्याने आंबा खायला पाहिजे/हवा", roman: "tyAne AMbA khAyalA pAhije/havA", hint: "" },
      { en: "He should go", mr: "त्याने जायला पाहिजे", roman: "tyAne jAyalA pAhije", hint: "" },
      { en: "He should have gone", mr: "त्याने जायला पाहिजे होते", roman: "tyAne jAyalA pAhije hote", hint: "" },
      { en: "I should speak", mr: "मी बोलायला पाहिजे", roman: "mI bolAyalA pAhije", hint: "" },
      { en: "I should have spoken", mr: "मी बोलायला पाहिजे होते", roman: "mI bolAyalA pAhije hote", hint: "" },
      { en: "They should dance", mr: "त्यांनी नाचायला पाहिजे", roman: "tyAMnI nAchAyalA pAhije", hint: "" },
      { en: "They should not dance", mr: "त्यांनी नाचायला नाही पाहिजे", roman: "tyAMnI nAchAyalA nAhI pAhije", hint: "" },
      { en: "They should have danced", mr: "त्यांनी नाचायला पाहिजे होते", roman: "tyAMnI nAchAyalA pAhije hote", hint: "" },
      { en: "They should not have danced", mr: "त्यांनी नाचायला नाही पाहिजे होते", roman: "tyAMnI nAchAyalA nAhI pAhije hote", hint: "" },
      { en: "You should play", mr: "तू खेळायला पाहिजे/पाहिजेस", roman: "tU kheLAyalA pAhije/pAhijes", hint: "" },
      { en: "You should not play", mr: "तू खेळायला नाही पाहिजे/पाहिजेस", roman: "tU kheLAyalA nAhI pAhije/pAhijes", hint: "" },
      { en: "You should have played", mr: "तू खेळायला पाहिजे होतेस", roman: "tU kheLAyalA pAhije hotes", hint: "" },
      { en: "You should not have smiled", mr: "तू हसायला नाही पाहिजे होतेस", roman: "tU hasAyalA nAhI pAhije hotes", hint: "" },
      { en: "They should not dance", mr: "त्यांनी नाचायला नको", roman: "tyAMnI nAchAyalA nako", hint: "" },
      { en: "They should not have danced", mr: "त्यांनी नाचायला नको होते", roman: "tyAMnI nAchAyalA nako hote", hint: "" },
      { en: "You should not have smiled", mr: "तू हसायला नको होतेस", roman: "tU hasAyalA nako hotes", hint: "" },
      { en: "He should eat mango", mr: "त्याने आंबा खाल्ला पाहिजे", roman: "tyAne AMbA khAllA pAhije", hint: "" },
      { en: "She should open box", mr: "तीने पेटी उघडली पाहिजे", roman: "tIne peTI ughaDalI pAhije", hint: "" },
      { en: "He should eat", mr: "त्याने खाल्ले पाहिजे", roman: "tyAne khAlle pAhije", hint: "" },
      { en: "He should go", mr: "तो गेला पाहिजे", roman: "to gelA pAhije", hint: "" },
      { en: "You(male) should go", mr: "तू गेला पाहिजेस", roman: "tU gelA pAhijes", hint: "" },
      { en: "You(male) should eat mango", mr: "तू आंबा खाल्ला पाहिजेस", roman: "tU AMbA khAllA pAhijes", hint: "" },
      { en: "He should have gone", mr: "तो गेला पाहिजे होता", roman: "to gelA pAhije hotA", hint: "" },
      { en: "He should not go", mr: "तो गेला नाही पाहिजे", roman: "to gelA nAhI pAhije", hint: "" },
      { en: "She should not open box", mr: "तीने पेटी उघडली नाही पाहिजे", roman: "tIne peTI ughaDalI nAhI pAhije", hint: "" },
      { en: "He should not eat", mr: "त्याने खाल्ले नाही पाहिजे", roman: "tyAne khAlle nAhI pAhije", hint: "" },
      { en: "He should eat mango", mr: "त्याने आंबा खावा", roman: "tyAne AMbA khAvA", hint: "" },
      { en: "He should eat tamarind", mr: "त्याने चिंच खावी", roman: "tyAne chiMch khAvI", hint: "" },
      { en: "She should write letter", mr: "तीने पत्र लिहावे", roman: "tIne patr lihAve", hint: "" },
      { en: "You should eat mango", mr: "तू आंबा खावास", roman: "tU AMbA khAvAs", hint: "" },
      { en: "He should go", mr: "त्याने जावे", roman: "tyAne jAve", hint: "" },
      { en: "He has to do it every day", mr: "त्याला हे रोज करायला/करावे लागते", roman: "tyAlA he roj karAyalA/karAve lAgate", hint: "" },
      { en: "He will have to do it every day", mr: "त्याला हे रोज करायला/करावे लागेल", roman: "tyAlA he roj karAyalA/karAve lAgel", hint: "" },
      { en: "He had to do it every day", mr: "त्याला हे रोज करायला/करावे लागले", roman: "tyAlA he roj karAyalA/karAve lAgale", hint: "" },
      { en: "She has to eat mango", mr: "तीला आंबा खायला/खावा लागतो", roman: "tIlA AMbA khAyalA/khAvA lAgato", hint: "" },
      { en: "She will have to eat mango", mr: "तीला आंबा खायला/खावा लागेल", roman: "tIlA AMbA khAyalA/khAvA lAgel", hint: "" },
      { en: "She had to eat mango", mr: "तीला आंबा खायला/खावा लागला", roman: "tIlA AMbA khAyalA/khAvA lAgalA", hint: "" },
      { en: "She has to eat mangoes", mr: "तीला आंबे खायला/खावे लागतात", roman: "tIlA AMbe khAyalA/khAve lAgatAt", hint: "" },
      { en: "She has to eat tamarind", mr: "तीला चिंच खायला/खावी लागते", roman: "tIlA chiMch khAyalA/khAvI lAgate", hint: "" },
      { en: "She has to eat tamarinds", mr: "तीला चिंचा खायला/खाव्या लागतात", roman: "tIlA chiMchA khAyalA/khAvyA lAgatAt", hint: "" },
      { en: "She has to eat medicine", mr: "तीला औषध खायला/खावे लागते", roman: "tIlA auShadh khAyalA/khAve lAgate", hint: "" },
      { en: "She has to eat medicines", mr: "तीला औषधे खायला/खावी लागतात", roman: "tIlA auShadhe khAyalA/khAvI lAgatAt", hint: "" },
      { en: "I have to go", mr: "मला जावे लागते", roman: "malA jAve lAgate", hint: "" },
      { en: "We have to speak", mr: "आम्हाला बोलावे लागते", roman: "AmhAlA bolAve lAgate", hint: "" },
      { en: "I keep speaking", mr: "मी बोलत राहतो", roman: "mI bolat rAhato", hint: "" },
      { en: "I kept speaking", mr: "मी बोलत राहिलो", roman: "mI bolat rAhilo", hint: "" },
      { en: "I will keep speaking", mr: "मी बोलत राहीन", roman: "mI bolat rAhIn", hint: "" },
      { en: "You keep speaking", mr: "तू बोलत राहतोस", roman: "tU bolat rAhatos", hint: "" },
      { en: "You kept speaking", mr: "तू बोलत राहिलास", roman: "tU bolat rAhilAs", hint: "" },
      { en: "You will keep speaking", mr: "तू बोलत राहशील", roman: "tU bolat rAhashIl", hint: "" },
      { en: "Keep speaking! (Imperative)", mr: "बोलत राहा", roman: "bolat rAhA", hint: "" },
      { en: "Bitter", mr: "कडू", roman: "kaDU", hint: "" },
      { en: "More bitter", mr: "जास्त/अधिक कडू", roman: "jAst/adhik kaDU", hint: "" },
      { en: "Most bitter", mr: "सर्वात/सर्वात जास्त/सर्वाधिक कडू", roman: "sarvAt/sarvAt jAst/sarvAdhik kaDU", hint: "" },
      { en: "Tall", mr: "उंच", roman: "uMch", hint: "" },
      { en: "Taller", mr: "जास्त/अधिक उंच", roman: "jAst/adhik uMch", hint: "" },
      { en: "Tallest", mr: "सर्वात जास्त/सर्वाधिक उंच", roman: "sarvAt jAst/sarvAdhik uMch", hint: "" },
      { en: "Good", mr: "चांगला", roman: "chAMgalA", hint: "" },
      { en: "Better", mr: "जास्त/अधिक चांगला", roman: "jAst/adhik chAMgalA", hint: "" },
      { en: "Best", mr: "सर्वात/सर्वात जास्त/सर्वाधिक चांगला", roman: "sarvAt/sarvAt jAst/sarvAdhik chAMgalA", hint: "" },
      { en: "He is taller than me", mr: "तो माझ्यापेक्षा जास्त/अधिक उंच आहे", roman: "to mAjhyApekShA jAst/adhik uMch Ahe", hint: "" },
      { en: "I am shorter than you", mr: "मी तुझ्यापेक्षा बुटका आहे", roman: "mI tujhyApekShA buTakA Ahe", hint: "" },
      { en: "They were happier than now", mr: "त्या आत्तापेक्षा जास्त/अधिक सुखी होत्या", roman: "tyA AttApekShA jAst/adhik sukhI hotyA", hint: "" },
      { en: "He is best", mr: "तो सर्वात चांगला आहे", roman: "to sarvAt chAMgalA Ahe", hint: "" },
      { en: "Everest is the tallest peak", mr: "एव्हरेस्ट सर्वाधिक उंच शिखर आहे", roman: "evharesT sarvAdhik uMch shikhar Ahe", hint: "" },
      { en: "She was the youngest player", mr: "ती सर्वात लहान खेळाडू होती", roman: "tI sarvAt lahAn kheLADU hotI", hint: "" },
      { en: "Your voice is loudest of all", mr: "तुझा आवाज सर्वात जास्त मोठा आहे", roman: "tujhA AvAj sarvAt jAst moThA Ahe", hint: "" },
      { en: "Your name is known to me", mr: "तुझे नाव मला माहीत आहे", roman: "tujhe nAv malA mAhIt Ahe", hint: "" },
      { en: "She knows his address", mr: "तीला त्याचा पत्ता माहीत आहे", roman: "tIlA tyAchA pattA mAhIt Ahe", hint: "" },
      { en: "She knew his address", mr: "तीला त्याचा पत्ता माहीत होता", roman: "tIlA tyAchA pattA mAhIt hotA", hint: "" },
      { en: "Do you know it?", mr: "तुला हे माहीत आहे का?", roman: "tulA he mAhIt Ahe kA?", hint: "" },
      { en: "Did she know that?", mr: "तीला हे माहीत होते का?", roman: "tIlA he mAhIt hote kA?", hint: "" },
      { en: "Your name is not known to me", mr: "तुझे नाव मला माहीत नाही", roman: "tujhe nAv malA mAhIt nAhI", hint: "" },
      { en: "She does not know his address", mr: "तीला त्याचा पत्ता माहीत नाही", roman: "tIlA tyAchA pattA mAhIt nAhI", hint: "" },
      { en: "She did not know his address", mr: "तीला त्याचा पत्ता माहीत नव्हता", roman: "tIlA tyAchA pattA mAhIt navhatA", hint: "" },
      { en: "Don't you know it?", mr: "तुला हे माहीत नाही का?", roman: "tulA he mAhIt nAhI kA?", hint: "" },
      { en: "Didn't she know that?", mr: "तीला हे माहीत नव्हते का?", roman: "tIlA he mAhIt navhate kA?", hint: "" },
      { en: "I know eating cake", mr: "मला केक खाता येतो", roman: "malA kek khAtA yeto", hint: "" },
      { en: "I know swimming", mr: "मला पोहता येते", roman: "malA pohatA yete", hint: "" },
      { en: "I know Japanese", mr: "मला जपानी येते", roman: "malA japAnI yete", hint: "" },
      { en: "I know cooking", mr: "मला जेवण बनवता येते", roman: "malA jevaN banavatA yete", hint: "" },
      { en: "Do you know playing cricket?", mr: "तुला क्रिकेट खेळता येते का?", roman: "tulA krikeT kheLatA yete kA?", hint: "" },
      { en: "I know killing mosquitoes", mr: "मला डास मारता येतात", roman: "malA DAs mAratA yetAt", hint: "" },
      { en: "She used to know dancing before", mr: "तीला पूर्वी नाचता यायचे", roman: "tIlA poorvI nAchatA yAyache", hint: "" },
      { en: "They knew to talk", mr: "त्यांना बोलता यायचे", roman: "tyAMnA bolatA yAyache", hint: "" },
      { en: "He learned. So he could speak Japanese", mr: "तो शिकला. म्हणून त्याला जपानी बोलता आले", roman: "to shikalA. mhaNUn tyAlA japAnI bolatA Ale", hint: "" },
      { en: "I do not know eating cake", mr: "मला केक खाता येत नाही", roman: "malA kek khAtA yet nAhI", hint: "" },
      { en: "I do not know swimming", mr: "मला पोहता येत नाही", roman: "malA pohatA yet nAhI", hint: "" },
      { en: "I do not know Japanese", mr: "मला जपानी येत नाही", roman: "malA japAnI yet nAhI", hint: "" },
      { en: "She did not know dancing before", mr: "तीला पूर्वी नाचता यायचे नाही", roman: "tIlA poorvI nAchatA yAyache nAhI", hint: "" },
      { en: "They did not know to talk", mr: "त्यांना बोलता यायचे नाही", roman: "tyAMnA bolatA yAyache nAhI", hint: "" },
      { en: "He did not learn. So he could not speak Japanese", mr: "तो शिकला नाही. म्हणून त्याला जपानी बोलता आले नाही", roman: "to shikalA nAhI. mhaNUn tyAlA japAnI bolatA Ale nAhI", hint: "" },
      { en: "I(boy) know you", mr: "मी तुला ओळखतो", roman: "mI tulA oLakhato", hint: "" },
      { en: "I(girl) know you", mr: "मी तुला ओळखते", roman: "mI tulA oLakhate", hint: "" },
      { en: "You know me", mr: "तू मला ओळखतोस", roman: "tU malA oLakhatos", hint: "" },
      { en: "He knows Mr. Ram", mr: "तो श्री. राम ना ओळखतो", roman: "to shrI. rAma nA oLakhato", hint: "" },
      { en: "Let's play", mr: "चला, आपण खेळूया", roman: "chalA, ApaN kheLUyA", hint: "" },
      { en: "Let's go", mr: "चला, आपण जाऊया", roman: "chalA, ApaN jAUyA", hint: "" },
      { en: "Let's speak", mr: "चला, बोलूया", roman: "chalA, bolUyA", hint: "" },
      { en: "Let's not play", mr: "आपण नको खेळूया", roman: "ApaN nako kheLUyA", hint: "" },
      { en: "Let's not go", mr: "आपण नको जाऊया", roman: "ApaN nako jAUyA", hint: "" },
      { en: "Let's not speak", mr: "नको बोलूया", roman: "nako bolUyA", hint: "" },
      { en: "Shall we play cricket? (style 1)", mr: "क्रिकेट खेळूया का?", roman: "krikeT kheLUyA kA?", hint: "" },
      { en: "Shall we play cricket? (style 2)", mr: "क्रिकेट खेळायचे का?", roman: "krikeT kheLAyAche kA?", hint: "" },
      { en: "Shall we watch movie? (style 1)", mr: "सिनेमा बघूया का?", roman: "sinemA baghUyA kA?", hint: "" },
      { en: "Shall we watch movie? (style 2)", mr: "सिनेमा बघायचा का?", roman: "sinemA baghAyachA kA?", hint: "" },
      { en: "Shall we go home? (style 1)", mr: "घरी जाऊया का?", roman: "gharI jAUyA kA?", hint: "" },
      { en: "Shall we go home? (style 2)", mr: "घरी जायचे का?", roman: "gharI jAyache kA?", hint: "" },
      { en: "Shall we eat mango? (style 1)", mr: "आंबा खाऊया का?", roman: "AMbA khAUyA kA?", hint: "" },
      { en: "Shall we eat mango? (style 2)", mr: "आंबा खायचा का?", roman: "AMbA khAyachA kA?", hint: "" },
      { en: "Shall we eat tamarind? (style 1)", mr: "चिंच खाऊया का?", roman: "chiMch khAUyA kA?", hint: "" },
      { en: "Shall we eat tamarind? (style 2)", mr: "चिंच खायची का?", roman: "chiMch khAyachI kA?", hint: "" },
      { en: "Let him play", mr: "त्याला खेळू दे", roman: "tyAlA kheLU de", hint: "" },
      { en: "Let me eat", mr: "मला खाऊ दे", roman: "malA khAU de", hint: "" },
      { en: "Let her speak", mr: "तीला बोलू दे", roman: "tIlA bolU de", hint: "" },
      { en: "You all, Let him play", mr: "त्याला खेळू द्या", roman: "tyAlA kheLU dyA", hint: "" },
      { en: "You all, Let me eat", mr: "मला खाऊ द्या", roman: "malA khAU dyA", hint: "" },
      { en: "You all, Let her speak", mr: "तीला बोलू द्या", roman: "tIlA bolU dyA", hint: "" },
      { en: "Don't let him play", mr: "त्याला खेळू देऊ नकोस", roman: "tyAlA kheLU deU nakos", hint: "" },
      { en: "Don't let me eat", mr: "मला खाऊ देऊ नकोस", roman: "malA khAU deU nakos", hint: "" },
      { en: "You all, don't let her speak", mr: "तीला बोलू देऊ नका", roman: "tIlA bolU deU nakA", hint: "" },
      { en: "You all, don't let me eat", mr: "मला खाऊ देऊ नका", roman: "malA khAU deU nakA", hint: "" },
      { en: "I could not understand what you just said", mr: "तू आत्ता काय म्हणालास ते मला कळले नाही", roman: "tU AttA kAy mhaNAlAs te malA kaLale nAhI", hint: "" },
      { en: "Which fruit you want, show me that", mr: "तुला कोणते फळ हवे आहे ते मला दाखव", roman: "tulA koNate phaL have Ahe te malA dAkhav", hint: "" },
      { en: "I could not understand what you just said", mr: "तू आत्ता जे म्हणालास ते मला कळले नाही", roman: "tU AttA je mhaNAlAs te malA kaLale nAhI", hint: "" },
      { en: "When you come I feel happy", mr: "तू जेव्हा येतोस तेव्हा मला आनंद वाटतो", roman: "tU jevhA yetos tevhA malA AnaMda vATato", hint: "" },
      { en: "What is in your mind, tell me that", mr: "तुझ्या मनात जे आहे, ते मला सांग", roman: "tujhyA manAt je Ahe, te malA sAMg", hint: "" },
      { en: "Which fruit you want, show me that", mr: "तुला जे फळ हवे आहे ते मला दाखव", roman: "tulA je phaL have Ahe te malA dAkhav", hint: "" },
      { en: "When you(girl) come I feel happy", mr: "तू जेव्हा येतेस तेव्हा मला आनंद वाटतो", roman: "tU jevhA yetes tevhA malA AnaMda vATato", hint: "" },
      { en: "Go back, the way you have come", mr: "तू जसा आलास तसा परत जा", roman: "tU jasA AlAs tasA parat jA", hint: "" },
      { en: "Give it to him, who wants it", mr: "ज्याला हवे आहे त्याला दे", roman: "jyAlA have Ahe tyAlA de", hint: "" },
      { en: "Tell me about them whom you read about", mr: "ज्यांच्याबद्दल तू वाचलेस त्यांच्याबद्दल मला सांग", roman: "jyAMchyAbaddal tU vAchales tyAMchyAbaddal malA sAMg", hint: "" },
      { en: "Wherever you will go I will come", mr: "तू जिथे जिथे जाशील तिथे तिथे मी येईन", roman: "tU jithe jithe jAshIl tithe tithe mI yeIn", hint: "" },
      { en: "Whichever vegetables you want, you buy it", mr: "तुला जी जी भाजी हवी आहे ती ती तू विकत घे", roman: "tulA jI jI bhAjI havI Ahe tI tI tU vikat ghe", hint: "" },
      { en: "Whenever you call he will answer", mr: "तू जेव्हा जेव्हा फोन करशील तेव्हा तेव्हा तो उत्तर देईल", roman: "tU jevhA jevhA phon karashIl tevhA tevhA to uttar deIl", hint: "" },
      { en: "Do not smoke here", mr: "धूम्रपान करू नका", roman: "dhoomrapAn karU nakA", hint: "" },
      { en: "Do not use mobile phones", mr: "मोबाईल फोन वापरु नका", roman: "mobAIl phon vAparu nakA", hint: "" },
      { en: "Enter your preferences", mr: "तुमची पसंती भरा", roman: "tumachI pasMtI bharA", hint: "" },
      { en: "Write your address", mr: "तुमचा पत्ता लिहावा", roman: "tumachA pattA lihAvA", hint: "" },
      { en: "Write your addresses", mr: "तुमचे पत्ते लिहावे", roman: "tumache patte lihAve", hint: "" },
      { en: "Enter your preference", mr: "तुमची पसंती भरावी", roman: "tumachI pasMtI bharAvI", hint: "" },
      { en: "Enter your preferences", mr: "तुमच्या पसंती भराव्यात", roman: "tumachyA pasMtI bharAvyAt", hint: "" },
      { en: "Speak your name", mr: "आपले नाव सांगावे", roman: "Apale nAv sAMgAve", hint: "" },
      { en: "Speak your names", mr: "आपली नावे सांगावी/सांगावीत", roman: "ApalI nAve sAMgAvI/sAMgAvIt", hint: "" },
      { en: "Do not speak", mr: "बोलू नये", roman: "bolU naye", hint: "" },
      { en: "Do not smoke", mr: "धूम्रपान करू नये", roman: "dhoomrapAn karU naye", hint: "" },
      { en: "Do not cross road here", mr: "येथे रस्ता ओलाण्डू नये", roman: "yethe rastA olANDU naye", hint: "" },
      { en: "Do not pluck flowers", mr: "फुले तोडू नयेत", roman: "phule toDU nayet", hint: "" },
      { en: "I like to eat mango", mr: "मला आंबा खायला आवडतो", roman: "malA AMbA khAyalA AvaDato", hint: "" },
      { en: "I like to eat mangoes", mr: "मला आंबे खायला आवडतात", roman: "malA AMbe khAyalA AvaDatAt", hint: "" },
      { en: "He liked to open bag", mr: "त्याला पेटी उघडायला आवडली", roman: "tyAlA peTI ughaDAyalA AvaDalI", hint: "" },
      { en: "He liked to open bags", mr: "त्याला पेट्या उघडायला आवडल्या", roman: "tyAlA peTyA ughaDAyalA AvaDalyA", hint: "" },
      { en: "She will like to sing song", mr: "तीला गाणे गायला आवडेल", roman: "tIlA gANe gAyalA AvaDel", hint: "" },
      { en: "She will like to sing songs", mr: "तीला गाणी गायला आवडतील", roman: "tIlA gANI gAyalA AvaDatIl", hint: "" },
      { en: "I do not like to eat mango", mr: "मला आंबा खायला आवडत नाही", roman: "malA AMbA khAyalA AvaDat nAhI", hint: "" },
      { en: "I do not like to eat mangoes", mr: "मला आंबे खायला आवडत नाहीत", roman: "malA AMbe khAyalA AvaDat nAhIt", hint: "" },
      { en: "He did not like to open bag", mr: "त्याला पेटी उघडायला आवडली नाही", roman: "tyAlA peTI ughaDAyalA AvaDalI nAhI", hint: "" },
      { en: "She will not like to sing song", mr: "तीला गाणे गायला आवडणार नाही", roman: "tIlA gANe gAyalA AvaDaNAr nAhI", hint: "" },
      { en: "I like to see Kaushik", mr: "मला कौशिकला बघायला आवडते", roman: "malA kaushikalA baghAyalA AvaDate", hint: "" },
      { en: "He likes to push me", mr: "त्याला मला ढकलायला आवडते", roman: "tyAlA malA DhakalAyalA AvaDate", hint: "" },
      { en: "He likes to push her", mr: "त्याला तीला ढकलायला आवडते", roman: "tyAlA tIlA DhakalAyalA AvaDate", hint: "" },
      { en: "They will like to hold us", mr: "त्यांना आम्हाला धरायला आवडेल", roman: "tyAMnA AmhAlA dharAyalA AvaDel", hint: "" },
      { en: "Kaushik said that he would eat", mr: "कौशिक म्हणाला की तो खाईल", roman: "kaushik mhaNAlA kI to khAIl", hint: "" },
      { en: "I thought I would be late so I would have to run", mr: "मला वाटले मला उशीर होईल म्हणून मला धावावे लागेल", roman: "malA vATale malA ushIr hoIl mhaNUn malA dhAvAve lAgel", hint: "" },
      { en: "I would love to visit New York", mr: "मला न्यूयॉर्कला भेट द्यायला आवडली असती", roman: "malA nyUy~orkalA bheT dyAyalA AvaDalI asatI", hint: "" },
      { en: "We would go, but we are too busy", mr: "आपण गेलो असतो, पण आपण खूप व्यग्र आहोत", roman: "ApaN gelo asato, paN ApaN khUp vyagr Ahot", hint: "" },
      { en: "I would not disclose it in any condition", mr: "मी कुठल्याही परिस्थितीत उघड केले नसते", roman: "mI kuThalyAhI paristhitIt ughaD kele nasate", hint: "" },
      { en: "Would you like to drink tea?", mr: "तुम्हाला चहा प्यायला आवडेल का?", roman: "tumhAlA chahA pyAyalA AvaDel kA?", hint: "" },
      { en: "Would you please help me?", mr: "कृपया मला मदत कराल का?", roman: "kRupayA malA madat karAl kA?", hint: "" },
      { en: "I would suggest you to take this medicine", mr: "मी हे औषध घेण्याचा सल्ला तुम्हाला देईन", roman: "mI he auShadh gheNyAchA sallA tumhAlA deIn", hint: "" },
      { en: "I understand its importance", mr: "मला याचे महत्व समजते", roman: "malA yAche mahatva samajate", hint: "" },
      { en: "He understood the logic", mr: "त्याला तत्व समजले", roman: "tyAlA tatva samajale", hint: "" },
      { en: "She came to know the news", mr: "तीला बातमी समजली/कळली", roman: "tIlA bAtamI samajalI/kaLalI", hint: "" },
      { en: "They will understand your mistakes", mr: "त्यांना तुझ्या चुका समजतील/कळतील", roman: "tyAMnA tujhyA chukA samajatIl/kaLatIl", hint: "" },
      { en: "Did you understand?", mr: "तुला कळले/समजले का?", roman: "tulA kaLale/samajale kA?", hint: "" },
      { en: "She does not understand", mr: "तीला कळत/समजत नाही", roman: "tIlA kaLat/samajat nAhI", hint: "" },
      { en: "He will not come to know this", mr: "त्याला हे समजणार/कळणार नाही", roman: "tyAlA he samajaNAr/kaLaNAr nAhI", hint: "" },
      { en: "You are coming", mr: "तू येतो आहेस", roman: "tU yeto Ahes", hint: "" },
      { en: "You are coming, aren't you?", mr: "तू येतो आहेस ना?", roman: "tU yeto Ahes nA?", hint: "" },
      { en: "She did not speak", mr: "ती बोलली नाही", roman: "tI bolalI nAhI", hint: "" },
      { en: "She did not speak, did she?", mr: "ती बोलली नाही ना?", roman: "tI bolalI nAhI nA?", hint: "" },
      { en: "He will do", mr: "तो करेल", roman: "to karel", hint: "" },
      { en: "He will do, won't he?", mr: "तो करेल ना?", roman: "to karel nA?", hint: "" },
      { en: "I remember you", mr: "मला तू आठवतोस", roman: "malA tU AThavatos", hint: "" },
      { en: "You remember me", mr: "तुला मी आठवतो", roman: "tulA mI AThavato", hint: "" },
      { en: "We remember Mary", mr: "आम्हाला मेरी आठवते", roman: "AmhAlA merI AThavate", hint: "" },
      { en: "Mary remembers us", mr: "मेरीला आम्ही आठवतो", roman: "merIlA AmhI AThavato", hint: "" },
      { en: "I remember you (लक्षात)", mr: "तू माझ्या लक्षात आहेस", roman: "tU mAjhyA lakShAt Ahes", hint: "" },
      { en: "You remember me (लक्षात)", mr: "मी तुझ्या लक्षात आहे", roman: "mI tujhyA lakShAt Ahe", hint: "" },
      { en: "I remember you (miss)", mr: "मला तुझी आठवण येते", roman: "malA tujhI AThavaN yete", hint: "" },
      { en: "You remember me", mr: "तुला माझी आठवण येते", roman: "tulA mAjhI AThavaN yete", hint: "" },
      { en: "Mary remembered us", mr: "मेरीला आमची आठवण आली", roman: "merIlA AmachI AThavaN AlI", hint: "" },
      { en: "Peter misses his friend", mr: "पीटरला त्याच्या मित्रांची आठवण येते", roman: "pITaralA tyAchyA mitrAMchI AThavaN yete", hint: "" },
      { en: "She missed her mother a lot", mr: "तीला तीच्या आईची खूप आठवण आली", roman: "tIlA tIchyA AIchI khUp AThavaN AlI", hint: "" },
      { en: "I will remember your favor", mr: "मी तुझे उपकार लक्षात ठेवीन", roman: "mI tujhe upakAr lakShAt ThevIn", hint: "" },
      { en: "He always remembered my advice", mr: "त्याने माझा सल्ला नेहमी लक्षात ठेवला", roman: "tyAne mAjhA sallA nehamI lakShAt ThevalA", hint: "" },
      { en: "I want to eat mango", mr: "मला आंबा खायचा आहे", roman: "malA AMbA khAyachA Ahe", hint: "" },
      { en: "I want to eat mangoes", mr: "मला आंबे खायचे आहेत", roman: "malA AMbe khAyache Ahet", hint: "" },
      { en: "He wanted to open bag", mr: "त्याला पेटी उघडायची होती", roman: "tyAlA peTI ughaDAyachI hotI", hint: "" },
      { en: "He wanted to open bags", mr: "त्याला पेट्या उघडायच्या होत्या", roman: "tyAlA peTyA ughaDAyachyA hotyA", hint: "" },
      { en: "She will want to sing song", mr: "तीला गाणे गायचे असेल", roman: "tIlA gANe gAyache asel", hint: "" },
      { en: "She will want to sing songs", mr: "तीला गाणी गायची असतील", roman: "tIlA gANI gAyachI asatIl", hint: "" },
      { en: "I wanted to go", mr: "मला जायचे होते", roman: "malA jAyache hote", hint: "" },
      { en: "I will want to run", mr: "मला धावायचे असेल", roman: "malA dhAvAyache asel", hint: "" },
      { en: "I do not want to eat mango", mr: "मला आंबा खायचा नाही आहे", roman: "malA AMbA khAyachA nAhI Ahe", hint: "" },
      { en: "He did not want to open bag", mr: "त्याला पेटी उघडायची नव्हती", roman: "tyAlA peTI ughaDAyachI navhtI", hint: "" },
      { en: "She will not want to sing song", mr: "तीला गाणे गायचे नसेल", roman: "tIlA gANe gAyache nasel", hint: "" },
      { en: "Kaushik wants to see Peter", mr: "कौशिकला पीटरला बघायचे आहे", roman: "kaushikalA pITar baghAyache Ahe", hint: "" },
      { en: "Kaushik wants to see him", mr: "कौशिकला त्याला बघायचे आहे", roman: "kaushikalA tyAlA baghAyache Ahe", hint: "" },
      { en: "Kaushik wants to see you", mr: "कौशिकला तुला बघायचे आहे", roman: "kaushikalA tulA baghAyache Ahe", hint: "" },
      { en: "I want you to finish work", mr: "मला, तू काम संपवायला पाहिजेस", roman: "malA, tU kAm saMpavAyalA pAhijes", hint: "" },
      { en: "She wants me to avoid junk food", mr: "तिला, मी जंकफूड टाळायला पाहिजे", roman: "tilA, mI jaMkaphUD TALAyalA pAhije", hint: "" },
      { en: "Kaushik wants students to practice more", mr: "कौशिकला विद्यार्थ्यांनी जास्त सराव करायला पाहिजे", roman: "kaushikalA vidyArthyAMnI jAst sarAv karAyalA pAhije", hint: "" },
      { en: "Kaushik wanted students to practice more", mr: "कौशिकला विद्यार्थ्यांनी जास्त सराव करायला पाहिजे होता", roman: "kaushikalA vidyArthyAMnI jAst sarAv karAyalA pAhije hotA", hint: "" },
      { en: "Students want Kaushik to talk slowly", mr: "विद्यार्थ्यांना कौशिकने हळू बोलायला पाहिजे", roman: "vidyArthyAMnA kaushikane haLU bolAyalA pAhije", hint: "" },
      { en: "I am supposed to meet him tomorrow", mr: "मला त्याला उद्या भेटायचे आहे", roman: "malA tyAlA udyA bheTAyache Ahe", hint: "" },
      { en: "I am supposed to finish that bottle", mr: "मी ती बाटली संपवायची आहे", roman: "mI tI bATalI saMpavAyachI Ahe", hint: "" },
      { en: "He is supposed to finish that bottle", mr: "त्याने ती बाटली संपवायची आहे", roman: "tyAne tI bATalI saMpavAyachI Ahe", hint: "" },
      { en: "She is supposed to finish that bottle", mr: "तीने ती बाटली संपवायची आहे", roman: "tIne tI bATalI saMpavAyachI Ahe", hint: "" },
      { en: "I/He/She was supposed to finish that bottle", mr: "मी/त्याने/तीने ती बाटली संपवायची होती", roman: "mI/tyAne/tIne tI bATalI saMpavAyachI hotI", hint: "" },
      { en: "I/He/She was supposed to finish those bottles", mr: "मी/त्याने/तीने त्या बाटल्या संपवायच्या होत्या", roman: "mI/tyAne/tIne tyA bATalyA saMpavAyachyA hotyA", hint: "" },
      { en: "I am supposed to go there tomorrow", mr: "मी उद्या तिकडे जायचे आहे", roman: "mI udyA tikaDe jAyache Ahe", hint: "" },
      { en: "He is supposed to come tomorrow", mr: "त्याने उद्या यायचे आहे / यायचं", roman: "tyAne udyA yAyache Ahe / yAyachM", hint: "" },
      { en: "We could not meet but next time we must meet", mr: "यावेळी भेटू शकलो नाही पण पुढच्या वेळी नक्की भेटायचं", roman: "yAveLI bheTU shakalo nAhI paN puDhachyA veLI nakkI bheTAyachM", hint: "" },
      { en: "Do attend my uncle's wedding – chintu, motu, gotu", mr: "माझ्या काकाच्या लग्नाला यायचं हं – चिंटू, मोटू, गोटू", roman: "mAjhyA kAkAchyA lagnAlA yAyachM haM – chiMTU, moTU, goTU", hint: "" },
      { en: "You must pay me ransom tomorrow itself", mr: "तू मला उद्याच्या उद्या खंडणी द्यायची", roman: "tU malA udyAchyA udyA khMDaNI dyAyachI", hint: "" },
      { en: "I get a prize", mr: "मला बक्षिस मिळते", roman: "malA bakShis miLate", hint: "" },
      { en: "I get 10 prizes", mr: "मला १० बक्षिसे मिळतात", roman: "malA 10 bakShise miLatAt", hint: "" },
      { en: "He gets a prize", mr: "त्याला बक्षिस मिळते", roman: "tyAlA bakShis miLate", hint: "" },
      { en: "He gets 10 prizes", mr: "त्याला १० बक्षिसे मिळतात", roman: "tyAlA 10 bakShise miLatAt", hint: "" },
      { en: "He got a prize", mr: "त्याला बक्षिस मिळाले", roman: "tyAlA bakShis miLAle", hint: "" },
      { en: "He got 10 prizes", mr: "त्याला १० बक्षिसे मिळाली", roman: "tyAlA 10 bakShise miLAlI", hint: "" },
      { en: "I found my wallet under the bed", mr: "मला माझे पाकीट दिवाणाखाली सापडले", roman: "malA mAjhe pAkIT divANAkhAlI sApaDale", hint: "" },
      { en: "She became angry", mr: "तिला राग आला", roman: "tIlA rAg AlA", hint: "" },
      { en: "He became angry", mr: "त्याला राग आला", roman: "tyAlA rAg AlA", hint: "" },
      { en: "He agrees to this condition", mr: "त्याला ही अट मान्य आहे", roman: "tyAlA hI aT mAny Ahe", hint: "" },
      { en: "He agrees to these conditions", mr: "त्याला ह्या अटी मान्य आहेत", roman: "tyAlA hyA aTI mAny Ahet", hint: "" },
      { en: "Finish it off in 10 minutes", mr: "दहा मिनिटात संपवून टाक आणि जा झोपायला", roman: "dahA miniTAt saMpavUn TAk ANi jA jhopAyalA", hint: "" },
      { en: "Do not hesitate. Speak it out", mr: "संकोच करू नकोस. बोलून टाक", roman: "saMkoch karU nakos. bolUn TAk", hint: "" },
      { en: "Nobody is looking. Just do it", mr: "कोणी आपल्याकडे बघत नाहिये. करून टाक लवकर", roman: "koNI ApalyAkaDe baghat nAhiye. karUn TAk lavakar", hint: "" },
      { en: "I somehow managed to gulp it", mr: "मी कसाबसा गिळून टाकला", roman: "mI kasAbasA giLUn TAkalA", hint: "" },
      { en: "He quickly came and read the letter", mr: "तेवढ्यात त्याने येऊन पत्र वाचून घेतले", roman: "tevaDhyAt tyAne yeUn patr vAchUn ghetale", hint: "" },
      { en: "Ask whatever you want; right now", mr: "तुला काय विचारायचे आहे ते आत्ताच विचारून घे", roman: "tulA kAy vichArAyache Ahe te AttAch vichArUn ghe", hint: "" },
      { en: "You may call me whatever you want", mr: "तुला हवं ते तू बोलून घे", roman: "tulA havM te tU bolUn ghe", hint: "" },
      { en: "Get that work done by him", mr: "त्याच्याकडून काम करून घे", roman: "tyAchyAkaDUn kAm karUn ghe", hint: "" },
      { en: "I made her take exercise every day", mr: "मी तीच्याकडून रोज व्यायाम करून घेतला", roman: "mI tIchyAkaDUn roj vyAyAm karUn ghetalA", hint: "" },
      { en: "I washed clothes very hard", mr: "मी कपडे धुवून काढले", roman: "mI kapaDe dhuvUn kADhale", hint: "" },
      { en: "Batsman hit every ball very hard", mr: "फलंदाजाने प्रत्येक बॉल फोडून काढला", roman: "phalaMdAjAne pratyek b~ol phoDUn kADhalA", hint: "" },
      { en: "I just told him we drank liquor", mr: "मी त्यांना सांगून बसलो की आपण काल दारू प्यायली", roman: "mI tyAMnA sAMgUn basalo kI ApaN kAl dArU pyAyalI", hint: "" },
      { en: "Oh my God! What have I done!", mr: "अरे देवा मी हे काय करून बसलो", roman: "are devA mI he kAy karUn basalo", hint: "" },
      { en: "Now keep crying", mr: "आता रडत बस", roman: "AtA raDat bas", hint: "" },
      { en: "She will search it forever", mr: "ती कायम ते शोधत बसेल", roman: "tI kAyam te shodhat basel", hint: "" },
      { en: "I forgot to tell you", mr: "तुला सांगायचे राहिले", roman: "tulA sAMgAyache rAhile", hint: "" },
      { en: "She could not see the sign", mr: "पाटी बघायची राहिली", roman: "pATI baghAyachI rAhilI", hint: "" },
      { en: "Start following my advice", mr: "माझे ऐकत जा", roman: "mAjhe aikat jA", hint: "" },
      { en: "If you had taken exercise every day then", mr: "जर तू रोज व्यायाम करत गेला असतास तर", roman: "jar tU roj vyAyAm karat gelA asatAs tar", hint: "" },
      { en: "I was about to open the door when I saw", mr: "मी दरवाजा उघडायला गेलो तेवढ्यात मला पोलिस दिसले", roman: "mI daravAjA ughaDAyalA gelo tevaDhyAt malA polis disale", hint: "" },
      { en: "If we think of eating mango then", mr: "आंबा खायचा म्हटला तर", roman: "AMbA khAyachA mhaTalA tar", hint: "" },
      { en: "If he decides to take revenge", mr: "जर त्याने सूड घ्यायचा म्हटला तर कोणीही त्याला थांबवू शकत नाही", roman: "jar tyAne sUD ghyAyachA mhaTalA tar koNIhI tyAlA thAMbavU shakat nAhI", hint: "" },
      { en: "Give him your information", mr: "त्याला तुझी महिती देऊन ठेव", roman: "tyAlA tujhI mahitI deUn Thev", hint: "" },
      { en: "Keep tea ready", mr: "चहा करून ठेव", roman: "chahA karUn Thev", hint: "" },
      { en: "We have booked tickets", mr: "आम्ही तिकिटे काढून ठेवली आहेत", roman: "AmhI tikiTe kADhUn ThevalI Ahet", hint: "" },
      { en: "I had already given my password", mr: "मी आधीच पासवर्ड सांगून चुकलो होतो", roman: "mI AdhIch pAsavarD sAMgUn chukalo hoto", hint: "" },
      { en: "I have decided plan for tonight", mr: "मी आजचा प्लॅन करून चुकलो आहे", roman: "mI AjachA pl~an karUn chukalo Ahe", hint: "" },
      { en: "He happened to say he was from India", mr: "त्याच्या बोलण्यात आले की तोही भारतामधील आहे", roman: "tyAchyA bolaNyAt Ale kI tohI bhAratAmadhIl Ahe", hint: "" },
      { en: "I happened to hear about strike", mr: "माझ्या ऐकण्यात आले", roman: "mAjhyA aikaNyAt Ale", hint: "" },
      { en: "Really!", mr: "खरंच!", roman: "kharaMch", hint: "" },
      { en: "Hey! When did you come?", mr: "अरे! तुम्ही कधी आलात?", roman: "are! tumhI kadhI AlAt?", hint: "" },
      { en: "How big!", mr: "अबब! किती मोठा", roman: "ababa! kitI moThA", hint: "" },
      { en: "Nice smell / Very tasty", mr: "अहाहा!", roman: "ahAhA!", hint: "" },
      { en: "Very bad", mr: "ओहो! वाईट झालं", roman: "oho! vAIT jhAlaM", hint: "" },
      { en: "Oh my God! Who did this?", mr: "अरे देवा! हे कोणी केलं", roman: "are devaa! he koNI kelM", hint: "" },
      { en: "Oh! He failed!", mr: "अरे बापरे! तो नापास झाला", roman: "are baapare! to nApAs jhAlA", hint: "" },
      { en: "No! He will never do it", mr: "छे! तो कधीही असं करणार नाही", roman: "Che! to kadhIhI asaM karaNAr nAhI", hint: "" },
      { en: "No! I do not believe", mr: "छट! मझा नाही विश्वास", roman: "ChaT! majhA nAhI vishvAs", hint: "" },
      { en: "Yes! I will surely come", mr: "होय! मी नक्की येणार", roman: "hoy! mI nakkI yeNAr", hint: "" },
      { en: "Hmm! I got it", mr: "हं! समजलं मला ते", roman: "haM! samajalM malA te", hint: "" },
      { en: "Well done! You won", mr: "शाब्बास! तू सामना जिंकलास", roman: "shAbbAs! tU sAmanA jiMkalAs", hint: "" },
      { en: "Good handwriting", mr: "अरे वा! / छान! हस्ताक्षर", roman: "are vA! / ChAn! hastAkShar", hint: "" },
      { en: "Very Good", mr: "खूप छान", roman: "khUp ChAn", hint: "" },
      { en: "Excellent!", mr: "मस्त! / जबरदस्त", roman: "mast! / jabaradast", hint: "" },
      { en: "Mummy! It is paining", mr: "अगं आई! खूप दुखतंय", roman: "agaM AI! khUp dukhataMy", hint: "" },
      { en: "Yuck! It looks ugly", mr: "शी! घाणेरडं दिसतंय ते", roman: "shI! ghANeraDM disataMy te", hint: "" },
      { en: "I spit on your cowardice", mr: "थू! तुमच्या भित्रेपणावर", roman: "thU! tumachyA bhitrepaNAvar", hint: "" },
      { en: "Shhh! Keep quiet", mr: "शू / श्श! शांत बसा!", roman: "shU / shsh! shAMt basA!", hint: "" },
      { en: "How well you danced!", mr: "किती छान नाचलास तू!", roman: "kitI ChAn nAchalAs tU!", hint: "" },
      { en: "What a fool he is!", mr: "काय मूर्ख आहे तो!", roman: "kAy mUrkha Ahe to!", hint: "" },
      { en: "Oh! What happened then?", mr: "अय्या! मग काय झालं?", roman: "ayyA! mag kAy jhAlaM?", hint: "" },
      { en: "Oh! When did you come?", mr: "अगं बाई! तुम्ही कधी आलात?", roman: "agaM bAI! tumhI kadhI AlAt?", hint: "" },
      { en: "Someone may see it! (blush)", mr: "इश्श्य कोणीतरी बघेल ना", roman: "ishshya koNItarI baghel nA", hint: "" },
      { en: "May I come", mr: "मी येऊ का?", roman: "mI yeU kA", hint: "" },
      { en: "May I go", mr: "मी जाऊ का?", roman: "mI jAU kA", hint: "" },
      { en: "May we come", mr: "आम्ही येऊ का?", roman: "AmhI yeU kA", hint: "" },
      { en: "May we go", mr: "आम्ही जाऊ का?", roman: "AmhI jAU kA", hint: "" },
      { en: "May we speak", mr: "आम्ही बोलू का", roman: "AmhI bolU kA", hint: "" },
      { en: "May you come", mr: "तुम्ही येऊ शकता का?", roman: "tumhI yeU shakatA kA?", hint: "" },
      { en: "May you speak", mr: "तुम्ही बोलू शकता का?", roman: "tumhI bolU shakatA kA?", hint: "" },
      { en: "May he tell", mr: "तो सांगू शकतो का?", roman: "to sAMgU shakato kA?", hint: "" },
      { en: "Can I tell", mr: "मी सांगू शकतो का?", roman: "mI sAMgU shakato kA?", hint: "" },
      { en: "Can I write", mr: "मी लिहू शकतो का?", roman: "mI lihU shakato kA?", hint: "" },
      { en: "May you come", mr: "येता का", roman: "yetA kA", hint: "" },
      { en: "May you speak", mr: "बोलता का?", roman: "bolatA kA?", hint: "" },
      { en: "May you give pen", mr: "पेन देता का", roman: "pen detA kA", hint: "" },
      { en: "Please give pen", mr: "जरा पेन देता का?", roman: "jarA pen detA kA?", hint: "" },
      { en: "Please tell address", mr: "जरा पत्ता सांगता का?", roman: "jarA pattA sAMgatA kA?", hint: "" },
      { en: "He may go", mr: "कदाचित तो जाईल", roman: "kadAchit to jAIl", hint: "" },
      { en: "I may sing", mr: "एखादवेळेस मी गाईन", roman: "ekhAdaveLes mI gAIn", hint: "" },
      { en: "He might come", mr: "बहुतेक तो येईल", roman: "bahutek to yeIl", hint: "" },
      { en: "He might have gone yesterday", mr: "कदाचित तो काल गेला असेल", roman: "kadAchit to kAl gelA asel", hint: "" },
      { en: "She might have completed it", mr: "कदाचित तीने पूर्ण केला असेल", roman: "kadAchit tIne pUrN kelA asel", hint: "" },
      { en: "They might have returned yesterday", mr: "बहुतेक ते काल परत गेले असतील", roman: "bahutek te kAla parat gele asatIl", hint: "" },
      { en: "He had gone", mr: "तो गेला होता", roman: "to gelA hotA", hint: "" },
      { en: "He might have gone", mr: "तो गेला असावा", roman: "to gelA asAvA", hint: "" },
      { en: "She had said", mr: "ती बोलली आहे", roman: "tI bolalI Ahe", hint: "" },
      { en: "She might have said", mr: "ती बोलली असावी", roman: "tI bolalI asAvI", hint: "" },
      { en: "You have eaten mango", mr: "तू आंबा खाल्ला आहेस", roman: "tU AMbA khAllA Ahes", hint: "" },
      { en: "You might have eaten mango", mr: "तू आंबा खाल्ला असावास", roman: "tU AMbA khAllA asAvAs", hint: "" },
      { en: "Moving chair", mr: "हलती खुर्ची", roman: "halatI khurchI", hint: "" },
      { en: "Speaking phone", mr: "बोलता फोन", roman: "bolatA phon", hint: "" },
      { en: "The day I like", mr: "माझा आवडता दिवस", roman: "mAjhA AvaDatA divas", hint: "" },
      { en: "Boy who is giving", mr: "देत असलेला मुलगा", roman: "det asalelA mulagA", hint: "" },
      { en: "Person who is dancing", mr: "नाचत असलेली व्यक्ती", roman: "nAchat asalelI vyaktI", hint: "" },
      { en: "Pot on table", mr: "टेबलावरचा माठ", roman: "TebalAvarachA mATh", hint: "" },
      { en: "Jar on table", mr: "टेबलावरची बरणी", roman: "TebalAvarachI baraNI", hint: "" },
      { en: "Leaf on table", mr: "टेबलावरचे पान", roman: "TebalAvarache pAn", hint: "" },
      { en: "Gift inside box", mr: "खोक्यातली भेटवस्तू", roman: "khokyAtalI bheTavastU", hint: "" },
      { en: "Area outside my home", mr: "माझ्या घराबाहेरचा परिसर", roman: "mAjhyA gharAbAherachA parisar", hint: "" },
      { en: "Pot on table", mr: "टेबलावरील माठ", roman: "TebalAvarIl mATh", hint: "" },
      { en: "I make him say", mr: "मी त्याला बोलायला लावतो", roman: "mI tyAlA bolAyalA lAvato", hint: "" },
      { en: "I will make him say", mr: "मी त्याला बोलायला लावीन", roman: "mI tyAlA bolAyalA lAvIn", hint: "" },
      { en: "I made him say", mr: "मी त्याला बोलायला लावले", roman: "mI tyAlA bolAyalA lAvale", hint: "" },
      { en: "He made me work", mr: "त्याने मला काम करायला लावले", roman: "tyAne malA kAm karAyalA lAvale", hint: "" },
      { en: "He makes me work", mr: "तो मला काम करायला लावतो", roman: "to malA kAm karAyalA lAvato", hint: "" },
      { en: "He will make me work", mr: "तो मला काम करायला लावेल", roman: "to malA kAm karAyalA lAvel", hint: "" },
      { en: "That joke made me laugh", mr: "त्या विनोदाने मला हसायला लावले", roman: "tyA vinodAne malA hasAyalA lAvale", hint: "" },
      { en: "Peter made Mary eat mango", mr: "पीटरने मेरीला आंबा खायला लावला", roman: "pITarane merIlA AMbA khAyalA lAvalA", hint: "" },
      { en: "Peter made Mary eat mangoes", mr: "पीटरने मेरीला आंबे खायला लावले", roman: "pITarane merIlA AMbe khAyalA lAvale", hint: "" },
      { en: "I myself did it", mr: "मीच हे केले", roman: "mIch he kele", hint: "" },
      { en: "I did this itself", mr: "मी हेच केले", roman: "mI hech kele", hint: "" },
      { en: "I will come tomorrow itself", mr: "मी उद्याच येईन", roman: "mI udyAch yeIn", hint: "" },
      { en: "I will surely come", mr: "मी येईनच", roman: "mI yeInach", hint: "" },
      { en: "I have seen India only", mr: "मी भारतच बघितला आहे", roman: "mI bhAratach baghitalA Ahe", hint: "" },
      { en: "He kept on talking", mr: "तो बोलतच राहिला", roman: "to bolatach rAhilA", hint: "" },
      { en: "He kept on staring that car", mr: "तो ती गाडी बघतच राहिला", roman: "to tI gADI baghatach rAhilA", hint: "" },
      { en: "I want only sedan car", mr: "मला सिडान कारच पाहिजे", roman: "malA siDAn kArach pAhije", hint: "" },
      { en: "I must go there", mr: "मला तिथे जायलाच पाहिजे", roman: "malA tithe jAyalAch pAhije", hint: "" },
      { en: "Why just me?", mr: "मीच का", roman: "mIch kA", hint: "" },
      { en: "I have a car", mr: "माझ्या जवळ/कडे गाडी आहे", roman: "mAjhyA javaL/kaDe gADI Ahe", hint: "" },
      { en: "I have 10 cars", mr: "माझ्या जवळ/कडे १० गाड्या आहेत", roman: "mAjhyA javaL/kaDe 10 gADyA Ahet", hint: "" },
      { en: "I had a car", mr: "माझ्या जवळ/कडे गाडी होती", roman: "mAjhyA javaL/kaDe gADI hotI", hint: "" },
      { en: "Anup will have watch", mr: "अनुप जवळ/कडे घड्याळ असेल", roman: "anup javaL/kaDe ghaDyAL asel", hint: "" },
      { en: "I do not have car", mr: "माझ्या जवळ/कडे गाडी नाही", roman: "mAjhyA javaL/kaDe gADI nAhI", hint: "" },
      { en: "I did not have car", mr: "माझ्या जवळ/कडे गाडी नव्हती", roman: "mAjhyA javaL/kaDe gADI navhatI", hint: "" },
      { en: "I have 2 brothers", mr: "मला दोन भाऊ आहेत", roman: "malA don bhAU Ahet", hint: "" },
      { en: "He has three paternal uncles", mr: "त्याला तीन काका आहेत", roman: "tyAlA tIn kAkA Ahet", hint: "" },
      { en: "Ravi had 2 kids", mr: "रवीला दोन मुले होती", roman: "ravIlA don mule hotI", hint: "" },
      { en: "He does not have a brother", mr: "त्याला भाऊ नाही", roman: "tyAlA bhAU nAhI", hint: "" },
      { en: "She did not have any relatives", mr: "तिला कोणीही नातेवाईक नव्हते", roman: "tIlA koNIhI nAtevAIk navhate", hint: "" },
      { en: "What does it mean?", mr: "त्याचा अर्थ काय", roman: "tyAchA arth kAy", hint: "" },
      { en: "What does that signboard mean?", mr: "त्या पाटीचा अर्थ काय", roman: "tyA pATIchA arth kAy", hint: "" },
      { en: "What did his speech mean?", mr: "त्याच्या भाषणाचा अर्थ काय होता", roman: "tyAchyA bhAShaNAchA arth kAy hotA", hint: "" },
      { en: "What does encyclopedia mean?", mr: "encyclopedia म्हणजे काय", roman: "encyclopedia mhaNaje kAy", hint: "" },
      { en: "What does Sundar mean in Marathi?", mr: "मराठीमधे सुंदर म्हणजे काय", roman: "marAThImadhe suMdar mhaNaje kAy", hint: "" },
      { en: "I did mean it", mr: "माझ्या बोलण्याचा अर्थ हा होता", roman: "mAjhyA bolaNyAchA arth hA hotA", hint: "" },
      { en: "I did not mean it", mr: "माझ्या बोलण्याचा अर्थ हा नव्हता", roman: "mAjhyA bolaNyAchA arth hA navhatA", hint: "" },
      { en: "He did not mean hurting you", mr: "त्याचा उद्देश तुम्हाला दुखवण्याचा नव्हता", roman: "tyAchA uddesh tumhAlA dukhavaNyAchA navhatA", hint: "" },
      { en: "I meant to insult him", mr: "माझा उद्देश त्याचा अपमान करण्याचा होता", roman: "mAjhA uddesh tyAchA apamAn karaNyAchA hotA", hint: "" },
      { en: "He and me", mr: "तो आणि/व मी", roman: "to ANi/v mI", hint: "" },
      { en: "Milk and sugar", mr: "दूध आणि/व साखर", roman: "dUdh ANi/v sAkhar", hint: "" },
      { en: "I want to buy but shop is closed", mr: "मला खरेदी करायची आहे पण दुकान बंद आहे", roman: "malA kharedI karAyachI Ahe paN dukAn baMd Ahe", hint: "" },
      { en: "He was clever but did not work hard", mr: "तो हुशार होता पण त्याने परिश्रम केले नाहीत", roman: "to hushAr hotA paN tyAne parishram kele nAhIt", hint: "" },
      { en: "I had warned him, still he opened the box", mr: "मी त्याला इशारा दिला होता तरीही त्याने खोका उघडला", roman: "mI tyAlA ishArA dilA hotA tarIhI tyAne khokA ughaDalA", hint: "" },
      { en: "He helped her still she insulted him", mr: "त्याने तिला मदत केली तरीही तीने त्याचा अपमान केला", roman: "tyAne tilA madat kelI tarIhI tIne tyAchA apamAn kelA", hint: "" },
      { en: "I did not come yesterday, because I was sick", mr: "मी काल आलो नाही, कारण मी आजारी होतो", roman: "mI kAl Alo nAhI, kAraN mI AjArI hoto", hint: "" },
      { en: "Car will not start because no petrol", mr: "गाडी चालू होणार नाही, कारण टाकीत पेट्रोल नाही", roman: "gADI chAlU hoNAr nAhI, kAraN TAkIt peTrol nAhI", hint: "" },
      { en: "I was sick so I did not come", mr: "मी आजारी होतो म्हणून मी काल आलो नाही", roman: "mI AjArI hoto mhaNUn mI kAl Alo nAhI", hint: "" },
      { en: "No petrol so car will not start", mr: "टाकीत पेट्रोल नाही म्हणून गाडी चालू होणार नाही", roman: "TAkIt peTrol nAhI mhaNUn gADI chAlU hoNAr nAhI", hint: "" },
      { en: "He told her that he is happy", mr: "त्याने तीला सांगितले की तो खूप खूष आहे", roman: "tyAne tIlA sAMgitale kI to khUp khUSh Ahe", hint: "" },
      { en: "I am sure that we will succeed", mr: "मला खात्री आहे की आपण यशस्वी होऊ", roman: "malA khAtrI Ahe kI ApaN yashasvI hoU", hint: "" },
      { en: "As you wish, my lord", mr: "जशी आपली इच्छा, साहेब", roman: "jashI ApalI ichChA, sAheb", hint: "" },
      { en: "Do it the same way as he is doing", mr: "तो जसे करतो आहे तसेच कर", roman: "to jase karato Ahe tasech kar", hint: "" },
      { en: "He as well as me", mr: "तो तसेच मी / तो आणि मी सुद्धा", roman: "to tasech mI / to ANi mI suddhA", hint: "" },
      { en: "She sang as well as danced", mr: "ती नाचली तसेच गायली", roman: "tI nAchalI tasech gAyalI", hint: "" },
      { en: "He or me", mr: "तो किंवा मी", roman: "to kiMvA mI", hint: "" },
      { en: "Do or die", mr: "करा किंवा मरा", roman: "karA kiMvA marA", hint: "" },
      { en: "Neither he nor I were interested", mr: "तो आणि मी दोघेही इच्छुक नव्हतो", roman: "to ANi mI doghehI ichChuk navhato", hint: "" },
      { en: "I finished study then I went to play", mr: "मी अभ्यास संपवला त्यानंतर खेळायला गेलो", roman: "mI abhyAs saMpavalA tyAnaMtar kheLAyalA gelo", hint: "" },
      { en: "I will call you then you enter on stage", mr: "मी तुला बोलवीन त्यानंतर/मग तू स्टेज वर ये", roman: "mI tulA bolavIn tyAnaMtar/mag tU sTej var ye", hint: "" },
      { en: "As long as you want me, I will stay", mr: "जोपर्यंत तुला हवे आहे, तोपर्यंत मी तुझ्याबरोबर राहीन", roman: "joparyMt tulA have Ahe, toparyaMt mI tujhyAbarobar rAhIn", hint: "" },
      { en: "As long as you follow rules", mr: "जोपर्यंत तुम्ही नियम पाळता तोपर्यंत तुम्हाला काही अडचण येणार नाही", roman: "joparyMt tumhI niyam pALatA toparyaMt tumhAlA kAhI aDachaN yeNAr nAhI", hint: "" },
      { en: "As far as I know, he is studious", mr: "जेवढे मला माहिती आहे त्याप्रमाणे तो अभ्यासू व्यक्ती आहे", roman: "jevaDhe malA mAhitI Ahe tyApramANe to abhyAsU vyaktI Ahe", hint: "" },
      { en: "As far as India is concerned", mr: "जोपर्यंत भारताचा प्रश्न आहे, कंपनी चांगले काम करत आहे", roman: "joparyMt bhAratAchA prashn Ahe toparyaMt kaMpanI chAMgale kAm karat Ahe", hint: "" },
      { en: "As far as literacy is concerned", mr: "जोपर्यंत साक्षरतेचा प्रश्न आहे, आपल्याला खूप मेहनत करावी लागेल", roman: "joparyMt sAkSharatechA prashn Ahe ApalyAlA khUp mehanat karAvI lAgel", hint: "" },
      { en: "He is blaming me as if I have not tried", mr: "तो माझ्यावर असे आरोप करत आहे, जणू मी प्रयत्नच केले नाहीत", roman: "to mAjhyAvar ase Arop karat Ahe, jaNU mI prayatnach kele nAhIt", hint: "" },
      { en: "He passed by as if she was not there", mr: "तो तिला स्मितहास्य न देता गेला, जणू ती तिथे नव्हतीच", roman: "to tilA smitahAsy na detA gelA, jaNU tI tithe navhatIch", hint: "" },
      { en: "As soon as he came", mr: "तो आल्या आल्या / तो येताच", roman: "to AlyA AlyA / to yetAch", hint: "" },
      { en: "As soon as she saw", mr: "तीने बघितल्या बघितल्या / तीने बघताच", roman: "tIne baghitalyA baghitalyA / tIne baghatAch", hint: "" },
      { en: "As soon as they become", mr: "ते झाल्या झाल्या / ते होताच", roman: "te jhAlyA jhAlyA / te hotAch", hint: "" },
      { en: "Let me know once he comes", mr: "तो आला की मला सांग", roman: "to AlA kI malA sAMg", hint: "" },
      { en: "Once I see your story I will give review", mr: "मी तुझी गोष्ट बघितली की अभिप्राय देईन", roman: "mI tujhI goShT baghitalI kI abhiprAy deIn", hint: "" },
      { en: "Rather than surrendering soldier will accept death", mr: "शरण जाण्याऐवजी सैनिक मरण स्वीकारेल", roman: "sharaN jANyAaivajI sainik maraN svIkArel", hint: "" },
      { en: "I will take tea rather than coffee", mr: "मी चहाच्या ऐवजी कॉफी घेईन", roman: "mI chahAchyA aivajI coffee gheIn", hint: "" },
      { en: "I will work hard so that I will win", mr: "मी परिश्रम करीन जेणेकरून मी यशस्वी होईन", roman: "mI parishram karIn jeNekarUn mI yashasvI hoIn", hint: "" },
      { en: "We should avoid plastic so that less pollution", mr: "आपण प्लास्टिक टाळले पाहिजे जेणेकरून प्रदूषण कमी होईल", roman: "ApaN plAsTik TALale pAhije jeNekarUn pradUShaN kamI hoIl", hint: "" },
      { en: "He cheated me whereas I was helping him", mr: "त्याने मला फसवले उलट मी त्याला मदत करत होतो", roman: "tyAne malA phasavale ulaT mI tyAlA madat karat hoto", hint: "" },
      { en: "Govt said prices declined whereas inflation rose", mr: "सरकारने सांगितले की भाव कमी झाले उलट महागाई वाढली", roman: "sarakArane sAMgitale kI bhAv kamI jhAle ulaT mahAgAI vADhalI", hint: "" },
      { en: "I did not know whether he is going", mr: "तो जाणार आहे का मला माहित नाही", roman: "to jANAr Ahe kA malA mAhit nAhI", hint: "" },
      { en: "She could not realize whether to speak or not", mr: "तीने बोलावे का नाही तीला कळले नाही", roman: "tIne bolAve kA nAhI tIlA kaLale nAhI", hint: "" },
      { en: "Do this otherwise you will not win", mr: "हे कर नाहीतर तू जिंकणार नाहीस", roman: "he kar nAhItar tU jiMkaNAr nAhIs", hint: "" },
      { en: "He should inform me otherwise I will not know", mr: "त्याने मला लगेच कळवले पाहिजे नाहीतर मला कळणार नाही", roman: "tyAne malA lagech kaLavale nAhItar malA kaLaNAr nAhI", hint: "" },
      { en: "I also ran", mr: "मी सुद्धा धावलो / मीही धावलो", roman: "mI suddhA dhAvalo / mIhI dhAvalo", hint: "" },
      { en: "He will come tomorrow as well", mr: "तो उद्यासुद्धा / उद्याही येईल", roman: "to udyAsuddhA / udyAhI yeIl", hint: "" },
      { en: "This is old video. I saw it. I am sharing today", mr: "हा जुना व्हिडिओ आहे. मी आत्ता बघितला. मी आज शेअर करत आहे", roman: "hA junA vhiDio Ahe. mI AttA baghitalA. mI Aj shear karat Ahe", hint: "" },
      { en: "This is old video, yet I saw it so I am sharing today", mr: "हा जुना व्हिडिओ असला तरी मी आत्ता बघितल्यामुळे आज शेअर करत आहे", roman: "hA junA vhiDio asalA tarI mI AttA baghitalyAmuLe Aj shear karat Ahe", hint: "" },
      { en: "This is old song. I heard it today", mr: "हे जुने गाणे आहे. मी आज ऐकले", roman: "he june gANe Ahe. mI Aj aikale", hint: "" },
      { en: "Though it is old song, I heard it today", mr: "हे जुने गाणे असले तरी मी आज ऐकले", roman: "he june gANe asale tarI mI Aj aikale", hint: "" },
      { en: "My wife was standing there. He asked about girlfriend", mr: "माझी बायको तिथे उभी होती. त्याने माझ्या मैत्रिणीबद्दल विचारले", roman: "mAjhI bAyako tithe ubhI hotI. tyAne mAjhyA maitriNIbaddal vichArale", hint: "" },
      { en: "My wife was standing there yet he asked", mr: "माझी बायको तिथे उभी असली तरी त्याने माझ्या मैत्रिणीबद्दल विचारले", roman: "mAjhI bAyako tithe ubhI asalI tarI tyAne mAjhyA maitriNIbaddal vichArale", hint: "" },
      { en: "Policeman was watching. He did not dare to run", mr: "पोलिस त्याला बारकाईने बघत होता. त्याने पळून जायचे धाडस केले नाही", roman: "polis tyAlA bArakAIne baghat hotA. tyAne paLUn jAyache dhADas kele nAhI", hint: "" },
      { en: "As policeman was watching he did not dare", mr: "पोलिस त्याला बारकाईने बघत असल्यामुळे त्याने पळून जायचे धाडस केले नाही", roman: "polis tyAlA bArakAIne baghat asalyAmuLe tyAne paLUn jAyache dhADas kele nAhI", hint: "" },
      { en: "I had illusion of monsters coming", mr: "मोठे राक्षस येत आहेत असा मला भास झाला", roman: "moThe rAkShas yet Ahet asA malA bhAs jhAlA", hint: "" },
      { en: "Monsters coming – असल्या सारखा", mr: "मोठे राक्षस येत असल्या सारखा मला भास झाला", roman: "moThe rAkShas yet asalyA sArakhA malA bhAs jhAlA", hint: "" },
      { en: "I just told him we drank liquor", mr: "मी त्यांना सांगून बसलो/गेलो की आपण काल दारू प्यायली", roman: "mI tyAMnA sAMgUn basalo/gelo kI ApaN kAl dArU pyAyalI", hint: "" },
      { en: "Oh my God! What have I done!", mr: "अरे देवा मी हे काय करून बसलो/गेलो", roman: "are devA mI he kAy karUn basalo/gelo", hint: "" },
      { en: "Now she will search it forever", mr: "आता ती कायम ते शोधत बसेल", roman: "AtA tI kAyam te shodhat basel", hint: "" },
      { en: "If we think of eating mango then..", mr: "आंबा खायचा म्हटला तर ..", roman: "AMbA khAyachA mhaTalA tar ..", hint: "" },
      { en: "I happened to hear about strike", mr: "रिक्षांच्या संपाबद्दल माझ्या ऐकण्यात आले", roman: "rikShAMchyA saMpAbaddal mAjhyA aikaNyAt Ale", hint: "" },
      { en: "I feel this way", mr: "मला असे वाटते", roman: "malA ase vATate", hint: "" },
      { en: "I feel this", mr: "मला हे वाटते", roman: "malA he vATate", hint: "" },
      { en: "He felt that I will not come", mr: "त्याला असे वाटले की मी येणार नाही", roman: "tyAlA ase vATale kI mI yeNAr nAhI", hint: "" },
      { en: "What do you feel?", mr: "तुला काय वाटते?", roman: "tulA kAy vATate?", hint: "" },
      { en: "He felt happiness", mr: "त्याला आनंद वाटला", roman: "tyAlA AnaMd vATalA", hint: "" },
      { en: "Don't you feel ashamed?", mr: "तुला लाज वाटत नाही का?", roman: "tulA lAj vATat nAhI kA?", hint: "" },
      { en: "Kaushik thinks he should go", mr: "कौशिकला असे वाटते की त्याने गेले पाहिजे", roman: "kaushikalA ase vATate kI tyAne gele pAhije", hint: "" },
      { en: "He will feel bad", mr: "त्याला वाईट वाटेल", roman: "tyAlA vAIT vATel", hint: "" },
      { en: "To show different aspects", mr: "कंगोरे उलगडणे", roman: "kaMgore ulagaDaNe", hint: "" },
      { en: "To follow up & pressurize", mr: "मानगुटीवर बसणे", roman: "mAnaguTIvar basaNe", hint: "" },
      { en: "Every home same story", mr: "घरोघरी मातीच्या चुली", roman: "gharogharI mAtIchyA chulI", hint: "" },
      { en: "Something fishy", mr: "पाणी मुरणे", roman: "pANI muraNe", hint: "" },
      { en: "Dampen spirit", mr: "आधीच हौस अन् त्यात पडला पाऊस", roman: "AdhIch haus an tyAt paDalA pAUs", hint: "" },
      { en: "To approve formally", mr: "शिक्कामोर्तब करणे", roman: "shikkAmortab karaNe", hint: "" },
      { en: "To threaten", mr: "दम भरणे", roman: "dam bharaNe", hint: "" },
      { en: "To cause destruction", mr: "मोडकळीस आणणे", roman: "moDakaLIs ANaNe", hint: "" },
      { en: "After-effects", mr: "पडसाद उमटणे", roman: "paDasAd umaTaNe", hint: "" },
      { en: "To override/violate", mr: "पायमल्ली करणे/होणे", roman: "pAyamallI karaNe/hoNe", hint: "" },
      { en: "Repeat like tape", mr: "टेप लावणे", roman: "Tepa lAvaNe", hint: "" },
      { en: "To renounce", mr: "तिलांजली देणे", roman: "tilAMjalI deNe", hint: "" },
      { en: "To force to do", mr: "भाग पाडणे", roman: "bhAg pADaNe", hint: "" },
      { en: "No control on tongue", mr: "जिभेला हाड नसणे", roman: "jibhelA hAD nasaNe", hint: "" },
      { en: "To pretend", mr: "कांगावा करणे", roman: "kAMgAvA karaNe", hint: "" },
      { en: "To trap", mr: "कोंडी करणे", roman: "koMDI karaNe", hint: "" },
      { en: "Not utter a word", mr: "अवाक्षर न काढणे", roman: "avAkShar n kADhaNe", hint: "" },
      { en: "To take control", mr: "ठाव घेणे", roman: "ThAv gheNe", hint: "" },
      { en: "To feel embarrassed", mr: "ओशाळणे", roman: "oshALaNe", hint: "" },
      { en: "To spew venom", mr: "गरळ ओकणे", roman: "garaL okaNe", hint: "" },
      { en: "To support", mr: "तळी उचलणे", roman: "taLI uchalaNe", hint: "" },
      { en: "To uncover mystery", mr: "गूढ उकलणे", roman: "gUDh ukalaNe", hint: "" },
      { en: "To strike", mr: "टोला हाणणे", roman: "TolA hANaNe", hint: "" },
      { en: "To be puzzled", mr: "पेचात पडणे", roman: "pechAt paDaNe", hint: "" },
      { en: "To defeat completely", mr: "धुव्वा उडवणे", roman: "dhuvvA uDavaNe", hint: "" },
      { en: "To pardon", mr: "गय करणे", roman: "gay karaNe", hint: "" },
      { en: "If employee works 1 year, gratuity right", mr: "१ वर्ष काम केल्यास कर्मचाऱ्याला Gratuityचा अधिकार मिळेल", roman: "1 varSh kAm kelyAs karmachAryAlA GratuitychA adhikAr miLel", hint: "" },
      { en: "If wrong info given, disciplinary action", mr: "चुकीची माहिती दिल्यास शिस्तभंगाची कारवाई होईल", roman: "chukIchI mAhitI dilyAs shistabhMgAchI kAravAI hoIl", hint: "" },
      { en: "If possible, come to meet me", mr: "जमल्यास मला भेटायला ये", roman: "jamalyAs malA bheTAyalA ye", hint: "" },
      { en: "What does this mean?", mr: "याचा अर्थ काय", roman: "yAchA arth kAy", hint: "" },
      { en: "Cryptography means?", mr: "\"Cryptography\" म्हणजे काय", roman: "\"Cryptography\" mhaNaje kAy", hint: "" },
      { en: "I came because you called", mr: "तू बोलावलेस म्हणून मी आलो", roman: "tU bolAvales mhaNUn mI Alo", hint: "" },
      { en: "Someone called Kaushik has come", mr: "कौशिक म्हणून कोणीतरी आले", roman: "kaushik mhaNUn koNItarI aale", hint: "" },
      { en: "Someone named Kaushik has come", mr: "कौशिक नावाचे कोणीतरी आले", roman: "kaushik nAvAche koNItarI aale", hint: "" },
      { en: "Why do you want it for?", mr: "तुला हे कशासाठी हवे आहे", roman: "tulA he kashAsAThI have Ahe", hint: "" },
      { en: "What is its reason?", mr: "त्याचे कारण काय", roman: "tyAche kAraN kAy", hint: "" },
      { en: "You only complete this", mr: "तूच हे पूर्ण कर", roman: "tUch he pUrNa kar", hint: "" },
      { en: "It is you who told", mr: "तूच मला हे सांगितलेस", roman: "tUch malA he sAMgitales", hint: "" },
      { en: "I want it tomorrow itself", mr: "मला हे उद्याच हवे आहे", roman: "malA he udyAch have Ahe", hint: "" },
      { en: "I am bored", mr: "मला कंटाळा आला आहे", roman: "malA kaMTALA AlA Ahe", hint: "" },
      { en: "He was bored", mr: "त्याला कंटाळा आला होता", roman: "tyAlA kaMTALA AlA hotA", hint: "" },
      { en: "Relation", mr: "नाते", roman: "nAte", hint: "" },
      { en: "Relative / Relatives", mr: "नातेवाईक", roman: "nAtevAIk", hint: "" },
      { en: "Mother", mr: "आई", roman: "AI", hint: "" },
      { en: "Father", mr: "वडील / बाबा", roman: "vaDIl / bAbA", hint: "" },
      { en: "Brother", mr: "भाऊ", roman: "bhAU", hint: "" },
      { en: "Elder brother", mr: "मोठा भाऊ / दादा", roman: "moThA bhAU / dAdA", hint: "" },
      { en: "Sister", mr: "बहीण", roman: "bahIN", hint: "" },
      { en: "Elder sister", mr: "मोठी बहीण / ताई", roman: "moThI bahIN / tAI", hint: "" },
      { en: "Direct brother", mr: "सख्खा भाऊ", roman: "sakhkhA bhAU", hint: "" },
      { en: "Direct sister", mr: "सख्खी बहीण", roman: "sakhkhI bahIN", hint: "" },
      { en: "Grand father", mr: "आजोबा", roman: "AjobA", hint: "" },
      { en: "Grand mother", mr: "आजी", roman: "AjI", hint: "" },
      { en: "Father's brother", mr: "काका", roman: "kAkA", hint: "" },
      { en: "Father's brother's wife", mr: "काकू", roman: "kAkU", hint: "" },
      { en: "Father's brother's son", mr: "चुलत भाऊ", roman: "chulat bhAU", hint: "" },
      { en: "Father's brother's daughter", mr: "चुलत बहीण", roman: "chulat bahIN", hint: "" },
      { en: "Mother's brother", mr: "मामा", roman: "mAmA", hint: "" },
      { en: "Mother's brother's wife", mr: "मामी", roman: "mAmI", hint: "" },
      { en: "Mother's brother's son", mr: "मामे भाऊ", roman: "mAme bhAU", hint: "" },
      { en: "Mother's brother's daughter", mr: "मामे बहीण", roman: "mAme bahIN", hint: "" },
      { en: "Father's sister", mr: "आत्या", roman: "AtyA", hint: "" },
      { en: "Father's sister's son", mr: "आत्ते भाऊ", roman: "Atte bhAU", hint: "" },
      { en: "Father's sister's daughter", mr: "आत्ते बहीण", roman: "Atte bahIN", hint: "" },
      { en: "Mother's sister", mr: "मावशी", roman: "mAvashI", hint: "" },
      { en: "Mother's sister's son", mr: "मावस भाऊ", roman: "mAvas bhAU", hint: "" },
      { en: "Mother's sister's daughter", mr: "मावस बहीण", roman: "mAvas bahIN", hint: "" },
      { en: "Mother's sister's husband", mr: "काका / मावसा", roman: "kAkA / mAvasA", hint: "" },
      { en: "Great grand father", mr: "पणजोबा", roman: "paNajobA", hint: "" },
      { en: "Great grand mother", mr: "पणजी", roman: "paNajI", hint: "" },
      { en: "Wife", mr: "पत्नी / बायको", roman: "patnI / bAyako", hint: "" },
      { en: "Husband", mr: "पती / नवरा", roman: "patI / navarA", hint: "" },
      { en: "Son", mr: "मुलगा", roman: "mulagA", hint: "" },
      { en: "Daughter", mr: "मुलगी", roman: "mulagI", hint: "" },
      { en: "Son's wife / Daughter in law", mr: "सून", roman: "sUn", hint: "" },
      { en: "Daughter's husband / Son in law", mr: "जावई", roman: "jAvaI", hint: "" },
      { en: "Father in law", mr: "सासरे", roman: "sAsare", hint: "" },
      { en: "Mother in law", mr: "सासू / सासुबाई", roman: "sAsU / sAsubAI", hint: "" },
      { en: "Father in law's father", mr: "आजेसासरे", roman: "AjesAsare", hint: "" },
      { en: "Father in law's mother", mr: "आजेसासू / आजेसासुबाई", roman: "AjesAsU / AjesAsubAI", hint: "" },
      { en: "Grandson", mr: "नातू", roman: "nAtU", hint: "" },
      { en: "Granddaughter", mr: "नात", roman: "nAt", hint: "" },
      { en: "Grandson's wife", mr: "नातसून", roman: "nAtasUn", hint: "" },
      { en: "Grand daughter's husband", mr: "नातजावई", roman: "nAtajAvaI", hint: "" },
      { en: "Great grandson", mr: "पणतू", roman: "paNatU", hint: "" },
      { en: "Great granddaughter", mr: "पणती", roman: "paNatI", hint: "" },
      { en: "Husband's brother", mr: "दीर", roman: "dIr", hint: "" },
      { en: "Husband's brother's wife", mr: "जाऊ", roman: "jAU", hint: "" },
      { en: "Husband's sister", mr: "नणंद", roman: "naNMd", hint: "" },
      { en: "Wife's brother", mr: "मेहुणा", roman: "mehuNA", hint: "" },
      { en: "Wife's sister", mr: "मेहुणी", roman: "mehuNI", hint: "" },
      { en: "Wife's sisters' husband", mr: "साडू", roman: "sADU", hint: "" },
      { en: "Sister's son", mr: "भाचा", roman: "bhAchA", hint: "" },
      { en: "Sister's daughter", mr: "भाची", roman: "bhAchI", hint: "" },
      { en: "Elder Brother's wife", mr: "वहिनी", roman: "vahinI", hint: "" },
      { en: "Younger brother's wife", mr: "भावजय", roman: "bhAvajay", hint: "" },
      { en: "A man's brother's son", mr: "पुतण्या", roman: "putaNyA", hint: "" },
      { en: "A man's brother's daughter", mr: "पुतणी", roman: "putaNI", hint: "" },
      { en: "Friend (boy)", mr: "मित्र", roman: "mitra", hint: "" },
      { en: "Friend (girl)", mr: "मैत्रीण", roman: "maitrIN", hint: "" },
      { en: "Neighbour", mr: "शेजारी", roman: "shejArI", hint: "" },
      { en: "Bride", mr: "वधू / नवरी मुलगी", roman: "vadhU / navarI mulagI", hint: "" },
      { en: "Bridegroom", mr: "वर / नवरा मुलगा", roman: "var / navarA mulagA", hint: "" },
      { en: "Adopted", mr: "दत्तक", roman: "dattak", hint: "" },
      { en: "Adopted son", mr: "दत्तक मुलगा", roman: "dattak mulagA", hint: "" },
      { en: "Adopted daughter", mr: "दत्तक मुलगी", roman: "dattak mulagI", hint: "" },
      { en: "Heir", mr: "वारस", roman: "vAras", hint: "" },
      { en: "Assumed son", mr: "मानलेला मुलगा", roman: "mAnalelA mulagA", hint: "" },
      { en: "Assumed daughter", mr: "मानलेली मुलगी", roman: "mAnalelI mulagI", hint: "" },
      { en: "To wake up", mr: "जागे होणे jAge hoNe", roman: "mI jAgA jhAlo", hint: "" },
      { en: "To get up", mr: "उठणे uThaNe", roman: "mI uThalo", hint: "" },
      { en: "To wash", mr: "धूणे dhUNe", roman: "toND dhutale", hint: "" },
      { en: "To brush", mr: "घासणे ghAsaNe", roman: "dAt ghAsale", hint: "" },
      { en: "To gargle", mr: "चूळ भरणे chUL bharaNe", roman: "chUL bharalI", hint: "" },
      { en: "To fold", mr: "घडी करणे ghaDI karaNe", roman: "chAdarIMchyA ghaDyA kelyA", hint: "" },
      { en: "To drink", mr: "पीणे pINe", roman: "chahA pyAyalA", hint: "" },
      { en: "To go to toilet", mr: "संडासला जाणे saMDAsalA jANe", roman: "saMDAsalA gelo", hint: "" },
      { en: "To urinate", mr: "लघवीला जाणे laghavIlA jANe", roman: "laghavIlA gelo", hint: "" },
      { en: "To exercise", mr: "व्यायाम करणे vyAyAm karaNe", roman: "vyAyAm kelA", hint: "" },
      { en: "To bath", mr: "आंघोळ करणे AMghoL karaNe", roman: "AMghoL kelI", hint: "" },
      { en: "To have breakfast", mr: "नाश्ता करणे nAshtA karaNe", roman: "nAshtA kelA", hint: "" },
      { en: "To eat", mr: "खाणे khANe", roman: "poLI bhAjI khAllI", hint: "" },
      { en: "To change", mr: "बदलणे badalaNe", roman: "kapaDe badalale", hint: "" },
      { en: "To wear", mr: "घालणे ghAlaNe", roman: "sharT ghAtalA", hint: "" },
      { en: "To wear (accessory)", mr: "लावणे lAvaNe", roman: "chaShmA lAvalA", hint: "" },
      { en: "To comb", mr: "भांग पाडणे bhAMg pADaNe", roman: "bhAMg pADalA", hint: "" },
      { en: "To close", mr: "बंद करणे baMd karaNe", roman: "dAr baMd kele", hint: "" },
      { en: "To climb down", mr: "उतरणे utaraNe", roman: "jInA utaralo", hint: "" },
      { en: "To sit", mr: "बसणे basaNe", roman: "gADIt basalo", hint: "" },
      { en: "To start", mr: "सुरू करणे surU karaNe", roman: "gADI surU kelI", hint: "" },
      { en: "To reach", mr: "पोचणे pochaNe", roman: "~ophisalA pochalo", hint: "" },
      { en: "To climb up", mr: "चढणे chaDhaNe", roman: "jInA chaDhalo", hint: "" },
      { en: "To work", mr: "काम करणे kAm karaNe", roman: "kAm kele", hint: "" },
      { en: "To speak/say/talk", mr: "बोलणे bolaNe", roman: "mitrAbarobar bolalo", hint: "" },
      { en: "To answer", mr: "उत्तर देणे uttar deNe", roman: "uttar dile", hint: "" },
      { en: "To send", mr: "पाठवणे pAThavaNe", roman: "Imel pAThavalA", hint: "" },
      { en: "To have lunch/dinner", mr: "जेवणे jevaNe", roman: "mI jevalo", hint: "" },
      { en: "To chitchat", mr: "गप्पा मारणे gappA mAraNe", roman: "gappA mAralyA", hint: "" },
      { en: "To buy", mr: "विकत घेणे vikat gheNe", roman: "sharT vikat ghetalA", hint: "" },
      { en: "To buy ticket", mr: "तिकिट काढणे tikiT kADhaNe", roman: "tikiT kADhale", hint: "" },
      { en: "To sell", mr: "विकणे vikaNe", roman: "sharT vikalA", hint: "" },
      { en: "To put/keep", mr: "ठेवणे ThevaNe", roman: "sharT pishavIt ThevalA", hint: "" },
      { en: "To put", mr: "टाकणे TAkaNe", roman: "sharT pishavIt TAkalA", hint: "" },
      { en: "To count", mr: "मोजणे mojaNe", roman: "paise mojale", hint: "" },
      { en: "To stand", mr: "उभे राहणे ubhe rAhaNe", roman: "ubhA rAhilo", hint: "" },
      { en: "To listen", mr: "ऐकणे aikaNe", roman: "gANI aikalI", hint: "" },
      { en: "To return", mr: "परत येणे parat yeNe", roman: "gharI parat Alo", hint: "" },
      { en: "To open", mr: "उघडणे ughaDaNe", roman: "daravAjA ughaDalA", hint: "" },
      { en: "To lift", mr: "उचलणे uchalaNe", roman: "pishavI uchalalI", hint: "" },
      { en: "To play", mr: "खेळणे kheLaNe", roman: "mulAMbarobar kheLalo", hint: "" },
      { en: "To jump", mr: "उडी मारणे uDI mAraNe", roman: "uDI mAralI", hint: "" },
      { en: "To hide", mr: "लपणे lapaNe", roman: "lapalo", hint: "" },
      { en: "To search", mr: "शोधणे shodhaNe", roman: "shodhale", hint: "" },
      { en: "To recite", mr: "म्हणणे mhaNaNe", roman: "kavitA mhaTalI", hint: "" },
      { en: "To sing", mr: "गाणे gANe", roman: "gANe gAyale", hint: "" },
      { en: "To shout", mr: "ओरडणे oraDaNe", roman: "oraDalo", hint: "" },
      { en: "To throw", mr: "फेकणे phekaNe", roman: "cheMDU phekalA", hint: "" },
      { en: "To hit", mr: "मारणे mAraNe", roman: "cheMDU mAralA", hint: "" },
      { en: "To ask", mr: "विचारणे vichAraNe", roman: "tyAche nAv vichArale", hint: "" },
      { en: "To ask for", mr: "मागणे mAgaNe", roman: "tyAche pen mAgitale", hint: "" },
      { en: "To clean", mr: "स्वच्छ करणे svachCha karaNe", roman: "Tebal svachCha kele", hint: "" },
      { en: "To cut", mr: "कापणे kApaNe", roman: "kek kApalA", hint: "" },
      { en: "To break", mr: "तोडणे toDaNe / मोडणे moDaNe", roman: "kheLaNe toDale", hint: "" },
      { en: "To burst", mr: "फोडणे phoDaNe", roman: "glAs phoDalA", hint: "" },
      { en: "To write", mr: "लिहिणे lihiNe", roman: "patr lihile", hint: "" },
      { en: "Accept", mr: "स्वीकारणे svIkAraNe", roman: "mI kalpanA svIkAralI", hint: "" },
      { en: "Give", mr: "देणे deNe", roman: "pen dile", hint: "" },
      { en: "Take", mr: "घेणे gheNe", roman: "pen ghetale", hint: "" },
      { en: "Bring", mr: "आणणे ANaNe", roman: "sAkhar ANalI", hint: "" },
      { en: "Help", mr: "मदत करणे madat karaNe", roman: "tyAlA madat kelI", hint: "" },
      { en: "Complain", mr: "तक्रार करणे takrAr karaNe", roman: "tyAchyAviruddh takrAr kelI", hint: "" },
      { en: "Dance", mr: "नाचणे nAchaNe", roman: "nAchalo", hint: "" },
      { en: "Cough", mr: "खोकणे khokaNe", roman: "khokalo", hint: "" },
      { en: "Draw", mr: "चित्र काढणे chitra kADhaNe", roman: "chitra kADhale", hint: "" },
      { en: "Fall", mr: "पडणे paDaNe", roman: "paDalo", hint: "" },
      { en: "Fill", mr: "भरणे bharaNe", roman: "bATalI bharalI", hint: "" },
      { en: "Finish", mr: "संपवणे saMpavaNe", roman: "dUdh saMpavale", hint: "" },
      { en: "Live", mr: "राहणे rAhaNe", roman: "mI shaharAt rAhilo", hint: "" },
      { en: "See/watch/look", mr: "बघणे baghaNe / पाहणे pAhaNe", roman: "sUchanA baghitalI", hint: "" },
      { en: "Wait", mr: "वाट बघणे vAT baghaNe", roman: "basachI vAT baghitalI", hint: "" },
      { en: "Use", mr: "वापरणे vAparaNe", roman: "pen vAparale", hint: "" },
      { en: "Run", mr: "पळणे paLaNe / धावणे dhAvaNe", roman: "paLAlo", hint: "" },
      { en: "Go", mr: "जाणे jANe", roman: "bAjArAt gelo", hint: "" },
      { en: "Come", mr: "येणे yeNe", roman: "bAjArAtUn Alo", hint: "" },
      { en: "Learn", mr: "शिकणे shikaNe", roman: "phreMch shikalo", hint: "" },
      { en: "Teach", mr: "शिकवणे shikavaNe", roman: "phreMch shikavalI", hint: "" },
      { en: "Study", mr: "अभ्यास करणे abhyAs karaNe", roman: "gaNitAchA abhyAs kelA", hint: "" },
      { en: "Read", mr: "वाचणे vAchaNe", roman: "patr vAchale", hint: "" },
      { en: "Make/prepare", mr: "तयार करणे tayAr karaNe / बनवणे banavaNe", roman: "mUrtI tayAr kelI", hint: "" },
      { en: "Tell", mr: "सांगणे sAMgaNe", roman: "pattA sAMgitalA", hint: "" },
      { en: "Fly", mr: "उडणे uDaNe", roman: "mI uDalo", hint: "" },
      { en: "Forget", mr: "विसरणे visaraNe", roman: "tyAche nAv visaralo", hint: "" },
      { en: "Remember", mr: "आठवणे AThavaNe", roman: "tyAche nAv AThavale", hint: "" },
      { en: "Get bored", mr: "कंटाळणे kaMTALaNe", roman: "kaMTALalo", hint: "" },
      { en: "Know", mr: "महिती असणे mahitI asaNe", roman: "tyAche nAv malA mAhitI hote", hint: "" },
      { en: "Leave", mr: "सोडणे soDaNe", roman: "kaMpanI soDalI", hint: "" },
      { en: "Want/need", mr: "हवे असणे have asaNe", roman: "malA pANI have hote", hint: "" },
      { en: "Sign", mr: "सही करणे sahI karaNe", roman: "chekavar sahI kelI", hint: "" },
      { en: "Sleep", mr: "झोपणे jhopaNe", roman: "dahA vAjatA jhopalo", hint: "" },
      { en: "Swim", mr: "पोहणे pohaNe", roman: "chAr tAs pohalo", hint: "" },
      { en: "Travel", mr: "प्रवास करणे pravAs karaNe", roman: "rAtrabhar pravAs kelA", hint: "" },
      { en: "Try", mr: "प्रयत्न करणे prayatn karaNe", roman: "phreMch shikAyachA prayatn kelA", hint: "" },
      { en: "Understand", mr: "समजणे samajaNe", roman: "malA muddA kaLalA", hint: "" },
      { en: "Worry", mr: "चिंता करणे chiMtA karaNe / काळजी करणे kALajI karaNe", roman: "tyAchyA abhyAsachI chiMtA kelI", hint: "" },
      { en: "Achieve", mr: "मिळवणे miLavaNe", roman: "yash miLavale", hint: "" },
      { en: "Admit (mistake)", mr: "मान्य करणे mAny karaNe", roman: "chUk mAny kelI", hint: "" },
      { en: "Admit (school)", mr: "भरती करणे bharatI karaNe", roman: "mulAlA shALet bharatI kele", hint: "" },
      { en: "Afford", mr: "परवडणे paravaDaNe", roman: "malA mahAg kAr gheNe paravaDale", hint: "" },
      { en: "Win", mr: "जिंकणे jiMkaNe", roman: "spardhA jiMkalo", hint: "" },
      { en: "Lose", mr: "हरणे haraNe", roman: "spardhA haralo", hint: "" },
      { en: "Think", mr: "विचार करणे vichAr karaNe", roman: "tikaDe jANyAchA vichAr kelA", hint: "" },
      { en: "Shake", mr: "हलवणे halavaNe", roman: "mishraN halavale", hint: "" },
      { en: "Decide", mr: "ठरवणे TharavaNe", roman: "mI jAyache Tharavale", hint: "" },
      { en: "Hold", mr: "धरणे dharaNe", roman: "b~aT hAtAt dharalI", hint: "" },
      { en: "Choose", mr: "निवडणे nivaDaNe", roman: "pivaLA sharT nivaDalA", hint: "" },
      { en: "Turn", mr: "वळणे vaLaNe", roman: "ujavIkaDe vaLalo", hint: "" },
      { en: "Rise", mr: "उगवणे ugavaNe", roman: "sUry ugavalA", hint: "" },
      { en: "Set (sun,moon)", mr: "मावळणे mAvaLaNe", roman: "sUry mAvaLalA", hint: "" },
      { en: "Deny", mr: "नाकारणे nAkAraNe", roman: "mI kalpanA nAkAralI", hint: "" },
      { en: "To turn on the lamp", mr: "दिवा लावणे", roman: "divA lAvaNe", hint: "" },
      { en: "To turn on the TV", mr: "टी.व्ही. लावणे", roman: "TI vhI lAvaNe", hint: "" },
      { en: "To bolt the door", mr: "कडी लावणे", roman: "kaDI lAvaNe", hint: "" },
      { en: "To touch by hand", mr: "हात लावणे", roman: "hAt lAvaNe", hint: "" },
      { en: "To touch by foot", mr: "पाय लावणे", roman: "pAy lAvaNe", hint: "" },
      { en: "To park car", mr: "गाडी लावणे", roman: "gADI lAvaNe", hint: "" },
      { en: "To reproach/blame", mr: "बोल लावणे", roman: "bol lAvaNe", hint: "" },
      { en: "To call on phone", mr: "फोन लावणे", roman: "phon lAvaNe", hint: "" },
      { en: "To take time", mr: "वेळ लावणे", roman: "veL lAvaNe", hint: "" },
      { en: "To fix price", mr: "भाव लावणे", roman: "bhAv lAvaNe", hint: "" },
      { en: "To wear sunglass", mr: "चष्मा लावणे", roman: "chaShmA lAvaNe", hint: "" },
      { en: "To cook rice", mr: "भात लावणे", roman: "bhAt lAvaNe", hint: "" },
      { en: "To sow wheat", mr: "गहू लावणे", roman: "gahU lAvaNe", hint: "" },
      { en: "To fix tune of song", mr: "चाल लावणे", roman: "chAl lAvaNe", hint: "" },
      { en: "To color", mr: "रंग लावणे", roman: "raMg lAvaNe", hint: "" },
      { en: "To destroy", mr: "वाट लावणे", roman: "vAT lAvaNe", hint: "" },
      { en: "To plant a tree", mr: "झाड लावणे", roman: "jhAD lAvaNe", hint: "" },
      { en: "To apply face powder", mr: "पावडर लावणे", roman: "pAvaDar lAvaNe", hint: "" },
      { en: "To apply oil", mr: "तेल लावणे", roman: "tel lAvaNe", hint: "" },
      { en: "To make one speak", mr: "बोलायला लावणे", roman: "bolAyalA lAvaNe", hint: "" },
      { en: "To make one laugh", mr: "हसायला लावणे", roman: "hasAyalA lAvaNe", hint: "" },
      { en: "To make one drink", mr: "प्यायला लावणे", roman: "pyAyalA lAvaNe", hint: "" },
      { en: "I need bucket", mr: "मला बादली लागते", roman: "malA bAdalI lAgate", hint: "" },
      { en: "I will need bucket", mr: "मला बादली लागेल", roman: "malA bAdalI lAgel", hint: "" },
      { en: "My car needs a lot of petrol", mr: "माझ्या गाडीला खूप पेट्रोल लागते", roman: "mAjhyA gADIlA khUp peTrol lAgate", hint: "" },
      { en: "I got hurt by knife", mr: "मला सुरी लागली", roman: "malA surI lAgalI", hint: "" },
      { en: "I got hurt by car", mr: "मला गाडी लागली", roman: "malA gADI lAgalI", hint: "" },
      { en: "I was hungry", mr: "मला भूक लागली", roman: "malA bhUk lAgalI", hint: "" },
      { en: "I am hungry", mr: "मला भूक लागली आहे", roman: "malA bhUk lAgalI Ahe", hint: "" },
      { en: "I was thirsty", mr: "मला तहान लागली", roman: "malA tahAn lAgalI", hint: "" },
      { en: "I am thirsty", mr: "मला तहान लागली आहे", roman: "malA tahAn lAgalI Ahe", hint: "" },
      { en: "Big Boss serial starts at 9", mr: "बिग बॉस मालिका नऊ वाजता लागते", roman: "big b~os mAlikA naU vAjatA lAgate", hint: "" },
      { en: "Lata's song was going on", mr: "लताचे गाणे लागले होते", roman: "latAche gANe lAgale hote", hint: "" },
      { en: "The bulb was on", mr: "विजेचा बल्ब लागला", roman: "vijechA bulb lAgalA", hint: "" },
      { en: "TV started after repair", mr: "त्याने दुरुस्त केल्यावर टीव्ही लागला", roman: "tyAne durust kelyAvar TIvhI lAgalA", hint: "" },
      { en: "To feel nausea in bus", mr: "गाडी लागणे", roman: "gADI lAgaNe", hint: "" },
      { en: "She feels nausea in bus", mr: "तीला गाडी लागते", roman: "tIlA gADI lAgate", hint: "" },
      { en: "Big", mr: "मोठा", roman: "moThA", hint: "" },
      { en: "Small", mr: "लहान / छोटा", roman: "lahAn / ChoTA", hint: "" },
      { en: "Bad", mr: "वाईट", roman: "vAIT", hint: "" },
      { en: "Far / Away", mr: "दूर / लांब", roman: "dUr / lAMb", hint: "" },
      { en: "Deep", mr: "खोल", roman: "khol", hint: "" },
      { en: "Shallow", mr: "उथळ", roman: "uthaL", hint: "" },
      { en: "Simple", mr: "साधा", roman: "sAdhA", hint: "" },
      { en: "Special", mr: "विशेष", roman: "visheSh", hint: "" },
      { en: "Dark", mr: "गडद", roman: "gaDad", hint: "" },
      { en: "Faint", mr: "फिका", roman: "phikA", hint: "" },
      { en: "Short", mr: "बुटका", roman: "buTakA", hint: "" },
      { en: "Fat / Thick", mr: "जाडा", roman: "jADA", hint: "" },
      { en: "Thin", mr: "बारीक", roman: "bArIk", hint: "" },
      { en: "Wide", mr: "रुंद", roman: "ruMda", hint: "" },
      { en: "Narrow", mr: "अरुंद", roman: "aruMda", hint: "" },
      { en: "Straight", mr: "सरळ", roman: "saraL", hint: "" },
      { en: "Curved", mr: "वाकडा", roman: "vAkaDA", hint: "" },
      { en: "Tasty", mr: "चवदार / चविष्ट", roman: "chavadAr / chaviShT", hint: "" },
      { en: "Tasteless", mr: "बेचव", roman: "bechav", hint: "" },
      { en: "Sweet", mr: "गोड", roman: "goD", hint: "" },
      { en: "Sour", mr: "आंबट", roman: "AMbaT", hint: "" },
      { en: "Salty", mr: "खारट", roman: "khAraT", hint: "" },
      { en: "Fresh", mr: "ताजा", roman: "tAjA", hint: "" },
      { en: "Stale", mr: "शिळा", roman: "shiLA", hint: "" },
      { en: "Spicy", mr: "मसालेदार", roman: "masAledAr", hint: "" },
      { en: "Colourful", mr: "रंगीत", roman: "raMgIt", hint: "" },
      { en: "Easy", mr: "सोपा", roman: "sopA", hint: "" },
      { en: "Hard / Difficult", mr: "कठीण", roman: "kaThIN", hint: "" },
      { en: "Clean", mr: "स्वच्छ", roman: "svachCha", hint: "" },
      { en: "Dirty / Soiled", mr: "मळका", roman: "maLakA", hint: "" },
      { en: "Dry", mr: "कोरडा / सुका", roman: "koraDA / sukA", hint: "" },
      { en: "Wet", mr: "ओला", roman: "olA", hint: "" },
      { en: "Empty", mr: "रिकामा", roman: "rikAmA", hint: "" },
      { en: "Filled", mr: "भरलेला", roman: "bharalelA", hint: "" },
      { en: "Expensive", mr: "महाग", roman: "mahAg", hint: "" },
      { en: "Cheap", mr: "स्वस्त", roman: "svasta", hint: "" },
      { en: "Full / Complete", mr: "पूर्ण", roman: "pUrNa", hint: "" },
      { en: "Incomplete", mr: "अपूर्ण", roman: "apUrNa", hint: "" },
      { en: "Half", mr: "अर्धा", roman: "ardhA", hint: "" },
      { en: "Hard (surface)", mr: "कडक", roman: "kaDak", hint: "" },
      { en: "Soft", mr: "मऊ", roman: "maU", hint: "" },
      { en: "Heavy", mr: "जड", roman: "jaD", hint: "" },
      { en: "Light (weight)", mr: "हलका", roman: "halakA", hint: "" },
      { en: "New", mr: "नवीन / नवा", roman: "navIn / navA", hint: "" },
      { en: "Old", mr: "जुना", roman: "junA", hint: "" },
      { en: "Quiet / Peaceful", mr: "शांत", roman: "shAMt", hint: "" },
      { en: "Slow", mr: "हळू", roman: "haLU", hint: "" },
      { en: "Fast", mr: "वेगवान", roman: "vegavAn", hint: "" },
      { en: "Young", mr: "तरूण", roman: "tarUN", hint: "" },
      { en: "Old", mr: "म्हातारा", roman: "mhAtArA", hint: "" },
      { en: "Little / Few / Some", mr: "थोडा", roman: "thoDA", hint: "" },
      { en: "Many / Much", mr: "खूप", roman: "khUp", hint: "" },
      { en: "Happy", mr: "आनंदी / खुश", roman: "AnaMdI / khush", hint: "" },
      { en: "Unhappy", mr: "नाखुश", roman: "nAkhush", hint: "" },
      { en: "Sad", mr: "दुःखी", roman: "duHkhI", hint: "" },
      { en: "Gloomy", mr: "उदास", roman: "udAs", hint: "" },
      { en: "Agile / Swift", mr: "चपळ", roman: "chapaL", hint: "" },
      { en: "Dull", mr: "मंद", roman: "maMd", hint: "" },
      { en: "Lazy", mr: "आळशी", roman: "ALashI", hint: "" },
      { en: "Eager / Enthusiastic", mr: "उत्साही", roman: "utsAhI", hint: "" },
      { en: "Hot in taste", mr: "तिखट", roman: "tikhaT", hint: "" },
      { en: "Carefully", mr: "काळजीपूर्वक", roman: "kALajIpUrvak", hint: "" },
      { en: "Slowly", mr: "हळूहळू", roman: "haLUhaLU", hint: "" },
      { en: "Fast", mr: "जोरात", roman: "jorAt", hint: "" },
      { en: "Quickly", mr: "पटकन", roman: "paTakan", hint: "" },
      { en: "I told him clearly", mr: "मी त्याला स्पष्टपणे सांगितले", roman: "mI tyAlA spaShTapaNe sAMgitale", hint: "" },
      { en: "He watched eagerly", mr: "त्याने अधिरतेने बघितली", roman: "tyAne adhiratene baghitalI", hint: "" },
      { en: "She can finish easily", mr: "ती हे काम सहजपणे संपवू शकते", roman: "tI he kAm sahajapaNe saMpavU shakate", hint: "" },
      { en: "A bit", mr: "थोडासा", roman: "thoDAsA", hint: "" },
      { en: "Absolutely", mr: "पूर्णपणे", roman: "pUrNapaNe", hint: "" },
      { en: "Accordingly", mr: "प्रमाणे", roman: "pramANe", hint: "" },
      { en: "Accurately", mr: "अचूकपणे", roman: "achUkapaNe", hint: "" },
      { en: "Actively", mr: "सक्रियपणे", roman: "sakriyapaNe", hint: "" },
      { en: "Afresh", mr: "नव्याने", roman: "navyAne", hint: "" },
      { en: "Again", mr: "पुन्हा", roman: "punhA", hint: "" },
      { en: "Agreeably", mr: "संमतीपूर्वक", roman: "saMmatIpUrvak", hint: "" },
      { en: "All", mr: "सर्व", roman: "sarva", hint: "" },
      { en: "Almost", mr: "बहुतेक / जवळजवळ पूर्ण", roman: "bahutek / javaLajavaL pUrN", hint: "" },
      { en: "Already", mr: "पूर्वीच / आधीच", roman: "pUrvIch / AdhIch", hint: "" },
      { en: "Altogether", mr: "एकत्र / सगळे मिळून", roman: "ekatra / sagaLe miLUn", hint: "" },
      { en: "Always", mr: "नेहमी", roman: "nehamI", hint: "" },
      { en: "Any", mr: "कुठलाही", roman: "kuThalAhI", hint: "" },
      { en: "Away", mr: "दूर", roman: "dUr", hint: "" },
      { en: "Badly", mr: "वाईटपणे", roman: "vAITapaNe", hint: "" },
      { en: "Barely", mr: "जेमतेम", roman: "jematem", hint: "" },
      { en: "Beautifully", mr: "सुंदरपणे", roman: "suMdarapaNe", hint: "" },
      { en: "Best", mr: "सर्वात छान", roman: "sarvAt ChAn", hint: "" },
      { en: "Better", mr: "चांगले", roman: "chAMgale", hint: "" },
      { en: "Certainly", mr: "नक्कीच / निश्चितपणे", roman: "nakkIch / nishchitapaNe", hint: "" },
      { en: "Clearly", mr: "स्पष्टपणे", roman: "spaShTapaNe", hint: "" },
      { en: "Easily", mr: "सहजपणे", roman: "sahajapaNe", hint: "" },
      { en: "Enough", mr: "पुरेसे", roman: "purese", hint: "" },
      { en: "Fortunately", mr: "नशिबाने / सुदैवाने", roman: "nashibAne / sudaivAne", hint: "" },
      { en: "Frequently", mr: "वरचेवर", roman: "varachevar", hint: "" },
      { en: "Happily", mr: "आनंदाने", roman: "AnaMdAne", hint: "" },
      { en: "Once", mr: "एकदा", roman: "ekadA", hint: "" },
      { en: "Quickly", mr: "लगेच / पटकन", roman: "lagech / paTakan", hint: "" },
      { en: "Rarely", mr: "क्वचित", roman: "kvachit", hint: "" },
      { en: "Really", mr: "खरेच", roman: "kharech", hint: "" },
      { en: "Secretly", mr: "लपूनछपून / गुप्तपणे", roman: "lapUnaChapUn / guptapaNe", hint: "" },
      { en: "Truly", mr: "खरोखर", roman: "kharokhar", hint: "" },
      { en: "Usually", mr: "नेहमी / सामान्यतः", roman: "nehamI / sAmAnyatH", hint: "" },
      { en: "Well", mr: "ठीक", roman: "ThIk", hint: "" },
      { en: "Yearly", mr: "दरवर्षी", roman: "daravarShI", hint: "" },
      { en: "Red", mr: "लाल / तांबडा", roman: "lAl / tAMbaDA", hint: "" },
      { en: "Yellow", mr: "पिवळा", roman: "pivaLA", hint: "" },
      { en: "Green", mr: "हिरवा", roman: "hiravA", hint: "" },
      { en: "Blue", mr: "निळा", roman: "niLA", hint: "" },
      { en: "Purple", mr: "जांभळा", roman: "jAMbhaLA", hint: "" },
      { en: "Brown", mr: "भुरा / तपकिरी", roman: "bhurA / tapakirI", hint: "" },
      { en: "Black", mr: "काळा", roman: "kALA", hint: "" },
      { en: "White", mr: "पांढरा", roman: "pAMDharA", hint: "" },
      { en: "Pink", mr: "गुलाबी", roman: "gulAbI", hint: "" },
      { en: "Orange", mr: "नारींगी", roman: "nArIMgI", hint: "" },
      { en: "Saffron", mr: "भगवा केशरी", roman: "bhagavA kesharI", hint: "" },
      { en: "Sky Blue", mr: "आकाशी", roman: "AkAshI", hint: "" },
      { en: "Ivory", mr: "हस्तिदंती", roman: "hastidaMtI", hint: "" },
      { en: "Gold", mr: "सोनेरी", roman: "sonerI", hint: "" },
      { en: "Silver", mr: "चंदेरी", roman: "chaMderI", hint: "" },
      { en: "Night cestrum", mr: "रातराणी", roman: "rAtarANI", hint: "" },
      { en: "Annona Hexapetala", mr: "चाफा", roman: "chAphA", hint: "" },
      { en: "Chrysanthemums", mr: "शेवंती", roman: "shevaMtI", hint: "" },
      { en: "Giant milkweed", mr: "रूई", roman: "rUI", hint: "" },
      { en: "Crape Jasmine / Pinwheel", mr: "तगर", roman: "tagar", hint: "" },
      { en: "Common Jasmine", mr: "जुई", roman: "juI", hint: "" },
      { en: "Jasminum grandiflorum", mr: "जाई", roman: "jAI", hint: "" },
      { en: "Lotus", mr: "कमळ", roman: "kamaL", hint: "" },
      { en: "Tuberose", mr: "निशिगंध", roman: "nishigaMdh", hint: "" },
      { en: "Lantana Camera", mr: "कुंदा", roman: "kuMdA", hint: "" },
      { en: "Rose", mr: "गुलाब", roman: "gulAb", hint: "" },
      { en: "Hibiscus", mr: "जास्वंद", roman: "jAsvaMd", hint: "" },
      { en: "Magnolia", mr: "चंपा", roman: "chaMpA", hint: "" },
      { en: "Jasminum sambac", mr: "मोगरा", roman: "mogarA", hint: "" },
      { en: "Royal poinciana / Peacock Flower", mr: "गुलमोहर", roman: "gulamohar", hint: "" },
      { en: "Sweet Granadilla", mr: "कृष्णकमळ", roman: "kRuShNakamaL", hint: "" },
      { en: "Coral Jasmine", mr: "पारिजातक", roman: "pArijAtak", hint: "" },
      { en: "Bullet wood", mr: "बकुळ", roman: "bakuL", hint: "" },
      { en: "Spanish Jasmine", mr: "चमेली", roman: "chamelI", hint: "" },
      { en: "Marigold", mr: "झेंडू", roman: "jheMDU", hint: "" },
      { en: "Periwinkle", mr: "सदाफुली", roman: "sadAphulI", hint: "" },
      { en: "Peacock Flower", mr: "शंकासुर", roman: "shaMkAsur", hint: "" },
      { en: "Umbrella Tree / Screw pine", mr: "केवडा", roman: "kevaDA", hint: "" },
      { en: "Frangipani", mr: "सोनचाफा", roman: "sonachAphA", hint: "" },
      { en: "Indian Shot / Canna Indica", mr: "कर्दळ", roman: "kardaL", hint: "" },
      { en: "Rangoon creeper", mr: "मधुमालती", roman: "madhumAlatI", hint: "" },
      { en: "Yellow ginger", mr: "सोनटक्का", roman: "sonaTakkA", hint: "" },
      { en: "Lantana Camera", mr: "घाणेरी", roman: "ghANerI", hint: "" },
      { en: "Cypress vine", mr: "गणेशवेल", roman: "gaNeshavel", hint: "" },
      { en: "Sunflower", mr: "सूर्यफूल", roman: "sUryaphUl", hint: "" },
      { en: "Oleander", mr: "कण्हेर", roman: "kaNher", hint: "" },
      { en: "Datura", mr: "धोतरा", roman: "dhotarA", hint: "" },
      { en: "Crossandra", mr: "अबोली", roman: "abolI", hint: "" },
      { en: "Where are you (to boy/girl)", mr: "तू कुठे आहेस", roman: "tU kuThe Ahes", hint: "" },
      { en: "Where are you (to man/lady)", mr: "तुम्ही कुठे आहात", roman: "tumhI kuThe AhAt", hint: "" },
      { en: "I am here", mr: "मी इकडे आहे", roman: "mI ikaDe Ahe", hint: "" },
      { en: "I am there", mr: "मी तिकडे आहे", roman: "mI tikaDe Ahe", hint: "" },
      { en: "I am in office", mr: "मी ऑफिसमधे आहे", roman: "mI ~ophisamadhe Ahe", hint: "" },
      { en: "I am on terrace", mr: "मी गच्चीवर आहे", roman: "mI gachchIvar Ahe", hint: "" },
      { en: "I am on road", mr: "मी रस्त्यात आहे", roman: "mI rastyAt Ahe", hint: "" },
      { en: "I am on the way", mr: "मी वाटेत आहे", roman: "mI vATet Ahe", hint: "" },
      { en: "Where had you gone? (to boy)", mr: "तू कुठे गेला होतास", roman: "tU kuThe gelA hotAs", hint: "" },
      { en: "I had gone to movie (boy)", mr: "मी पिक्चरला गेलो होतो", roman: "mI pikcharalA gelo hoto", hint: "" },
      { en: "Where is post office", mr: "पोस्ट ऑफीस कुठे आहे", roman: "posT ~ophIs kuThe Ahe", hint: "" },
      { en: "Post office is nearby", mr: "पोस्ट ऑफीस जवळच आहे", roman: "posT ~ophIs javaLach Ahe", hint: "" },
      { en: "Post office is far", mr: "पोस्ट ऑफीस लांब/दूर आहे", roman: "posT ~ophIs lAMb/dUr Ahe", hint: "" },
      { en: "How to go to Central Park", mr: "सेन्ट्रल पार्कला कसे जायचे", roman: "senTral pArkalA kase jAyache", hint: "" },
      { en: "Go straight", mr: "सरळ जा", roman: "saraL jA", hint: "" },
      { en: "Turn left", mr: "डावीकडे वळा", roman: "DAvIkaDe vaLA", hint: "" },
      { en: "Turn right", mr: "उजवीकडे वळा", roman: "ujavIkaDe vaLA", hint: "" },
      { en: "Go back", mr: "मागे जा", roman: "mAge jA", hint: "" },
      { en: "Go uphill", mr: "त्या टेकडीवर चढा", roman: "tyA TekaDIvar chaDhA", hint: "" },
      { en: "Come here (to boy/girl)", mr: "इकडे ये", roman: "ikaDe ye", hint: "" },
      { en: "Go there (to boy/girl)", mr: "तिकडे जा", roman: "tikaDe jA", hint: "" },
      { en: "What will you bring from there?", mr: "तिकडून मला काय आणशील?", roman: "tikaDUn malA kAy ANashIl?", hint: "" },
      { en: "Write your name here", mr: "इथे तुमचे नाव लिहा", roman: "ithe tumache nAv lihA", hint: "" },
      { en: "Maintain silence there", mr: "तिथे शांतता पाळा", roman: "tithe shAMtatA pALA", hint: "" },
      { en: "Do not roam here-and-there", mr: "इकडेतिकडे भटकू नकोस", roman: "ikaDetikaDe bhaTakU nakos", hint: "" },
      { en: "Hey, how come you are here? You were in ABC company, right?", mr: "अरे तू इकडे कसा काय? तू ABC कंपनीत होतास ना?", roman: "are tU ikaDe kasA kAy? tU ABC kaMpanIt hotAs nA?", hint: "" },
      { en: "Yes. I left it 2 months back", mr: "हो. दोन महिन्यांपूर्वी मी ती कंपनी सोडली", roman: "ho. don mahinyAMpUrvI mI tI kaMpanI soDalI", hint: "" },
      { en: "Wow!! But why did you leave?", mr: "अरे वा !! पण का सोडलीस?", roman: "are wA. paN kA sodalist", hint: "" },
      { en: "I was not getting good work there", mr: "तिकडे मला काम चांगलं मिळालं नव्हतं.", roman: "tikaDe malA kAm chAMgalM miLAlM navhatM.", hint: "" },
      { en: "Which technology did you work on?", mr: "कुठल्या technology वर काम होतं?", roman: "kuThalyA technology var kAm hotM?", hint: "" },
      { en: "Core Java", mr: "कोअर जावा", roman: "koar jAvA", hint: "" },
      { en: "Which technologies are here?", mr: "इथे कुठली technology आहे?", roman: "ithe kuThalI technology Ahe?", hint: "" },
      { en: "Core java and spring, hibernate", mr: "Core Java आणि Spring, Hibernate", roman: "Core Java ANi Spring, Hibernate", hint: "" },
      { en: "Great!! How much hike did you get?", mr: "मस्त! Hike किती मिळाली?", roman: "mast! Hike kitI miLAlI?", hint: "" },
      { en: "Is completely fix?", mr: "पूर्ण fix आहे का?", roman: "poorN fix Ahe kA?", hint: "" },
      { en: "No. 0.6 of that is variable", mr: "नाही त्यातलं ०.६ variable आहे.", roman: "nAhI tyAtalM 0.6 variable Ahe.", hint: "" },
      { en: "And how much is your total experience?", mr: "आणि एकूण experience किती झाला?", roman: "ANi ekUN experience kitI jhAlA?", hint: "" },
      { en: "Eight years", mr: "आठ वर्षं", roman: "ATh varShM", hint: "" },
      { en: "How many years were you there?", mr: "तिकडे किती वर्षं होतास?", roman: "tikaDe kitI varShM hotAs?", hint: "" },
      { en: "4 Years", mr: "चार वर्षं", roman: "chAr varShM", hint: "" },
      { en: "Had you stayed one more year, you would have got gratuity", mr: "तिकडे अजून एक वर्ष थांबला असतास तर gratuity मिळाली असती", roman: "tikaDe ajUn ek varSh thAMbalA asatAs tar gratuity miLAlI asatI", hint: "" },
      { en: "Yes. But I was bored. I could not see growth there", mr: "हो. पण कंटाळा आला होता. तिथे काही growth दिसत नव्हती.", roman: "ho. paN kaMTALA aalA hotA. tithe kAhI growth disat navhatI.", hint: "" },
      { en: "How is this company?", mr: "ही company कशी वाटत्ये?", roman: "hI company kashi vATatye?", hint: "" },
      { en: "It is good", mr: "चांगलीये", roman: "chAMgalIye.", hint: "" },
      { en: "How much work-pressure?", mr: "Work-pressure कसं आहे", roman: "work-pressure kasaM Ahe", hint: "" },
      { en: "It is OK. Not much. Work will be Nine-to-six", mr: "ठीक आहे. इतकं जास्त नाही. Nine-to-six काम होतं", roman: "ThIk Ahe. itakaM jAst nAhI. Nine-to-six kAm hotM", hint: "" },
      { en: "How do you travel to office?", mr: "Office ला कसा येतोस?", roman: "office lA kasA yetos?", hint: "" },
      { en: "By company bus", mr: "companyच्या बस ने", roman: "company chyA bas ne", hint: "" },
      { en: "How much time it takes?", mr: "किती वेळ लागतो?", roman: "kitI veL lAgato?", hint: "" },
      { en: "1 hour", mr: "एक तास", roman: "ek tAs", hint: "" },
      { en: "Where do you live?", mr: "राहतोस कुठे?", roman: "rAhatos kuThe?", hint: "" },
      { en: "It is near. At Rahul Garden City. Highway touch place", mr: "जवळच. राहूल Garden City मध्ये. High-way ला लागूनच आहे.", roman: "javaLach. rAhUl garden city madhye. High way lA lAgUnach Ahe.", hint: "" },
      { en: "Did you buy flat?", mr: "तू घेतला आहेस का flat?", roman: "tU ghetalA Ahes kA flat?", hint: "" },
      { en: "No. It is rented", mr: "नाही भाड्याचा आहे", roman: "nAhI bhADyAchA Ahe", hint: "" },
      { en: "Are you looking for a house?", mr: "तू बघतोयस का घर?", roman: "tU baghatoyas kA ghar?", hint: "" },
      { en: "Yes, the search is going on", mr: "हो, शोध चालू आहे.", roman: "ho shodh chAlU Ahe.", hint: "" },
      { en: "My friend booked in Nature Park. 2BHK", mr: "माझ्या मित्राने nature park मधे बूक केला. 2BHK", roman: "mAjhyA mitrAne nature park madhe book kelA. 2bhk", hint: "" },
      { en: "How much did it cost?", mr: "कितीला पडला?", roman: "kitIlA paDalA?", hint: "" },
      { en: "30 Lakhs", mr: "तीस लाखाला", roman: "tIs lAkhAlA", hint: "" },
      { en: "It is cheap then. How much is rate there?", mr: "स्वस्त आहे की. किती Rate आहे तिकडे.", roman: "swast Ahe kI. kitI rate aahe tikaDe.", hint: "" },
      { en: "2000", mr: "दोन हजार", roman: "don hajAr", hint: "" },
      { en: "I will also go and see it", mr: "मी पण जाउन बघून येईन.", roman: "mI paN jAun baghUn yeIn", hint: "" },
      { en: "Go for sure", mr: "नक्की जा.", roman: "nakkI jA.", hint: "" },
      { en: "I leave now. I have one meeting now.", mr: "चल मी निघतो. आता एक meeting आहे.", roman: "chal mI nighato. AtA ek meeting aahe", hint: "" },
      { en: "OK. What is your number?", mr: "OK. तुझा number काय?", roman: "OK. tujhA number kAy?", hint: "" },
      { en: "I have your number. I give you miss-call", mr: "माझ्या कडे तुझा number आहे. miss-call देतो.", roman: "mAjhyA kaDe tujhA number Ahe. miss-call deto.", hint: "" },
      { en: "Fine", mr: "चालेल.", roman: "chalel.", hint: "" },
      { en: "Good morning Teacher/Madam", mr: "गुड मॉर्निंग बाई/मॅडम", roman: "guD morniMg bAI/maDam", hint: "" },
      { en: "Good morning pupils", mr: "गुड मॉर्निंग मुलांनो", roman: "guD morniMg mulAMno", hint: "" },
      { en: "Sit down", mr: "बसा", roman: "basA", hint: "" },
      { en: "Its period of geography, right?", mr: "भुगोलाचा तास आहे ना?", roman: "bhugolAchA tAs Ahe nA?", hint: "" },
      { en: "Take out book", mr: "पुस्तक काढा", roman: "pustak kADhA", hint: "" },
      { en: "Open tenth chapter", mr: "दहावा धडा उघडा", roman: "dahAvA dhaDA ughaDA", hint: "" },
      { en: "Yesterday we learnt half of lesson", mr: "काल आपण अर्धा धडा शिकलो होतो.", roman: "kAl ApaN ardhA dhaDA shikalo hoto.", hint: "" },
      { en: "Let's go ahead today", mr: "आज पुढे जाऊया", roman: "Aj puDhe jAUyA", hint: "" },
      { en: "Did you understand everything taught yesterday?", mr: "काल शिकवलेले सगळे कळले का?", roman: "kAl shikavalele sagaLe kaLale kA?", hint: "" },
      { en: "Yes. Understood", mr: "हो. कळले.", roman: "ho. kaLale.", hint: "" },
      { en: "Sure?", mr: "नक्की?", roman: "nakkI?", hint: "" },
      { en: "Yes. Sure", mr: "हो नक्की.", roman: "ho nakkI.", hint: "" },
      { en: "Did you do homework given yesterday?", mr: "काल दिलेला गृहपाठ केला का?", roman: "kAl dilelA gRuhapATh kelA kA?", hint: "" },
      { en: "Teacher, I did not do", mr: "बाई मी नाही केला", roman: "bAI mI nAhI kelA", hint: "" },
      { en: "Why?", mr: "का", roman: "kA", hint: "" },
      { en: "I was not feeling well", mr: "मला काल बरं वाटत नव्हतं", roman: "malA kAl baraM vATat navhataM", hint: "" },
      { en: "Ok", mr: "ठिक आहे", roman: "Thik Ahe", hint: "" },
      { en: "Teacher, when is unit test?", mr: "बाई चाचणी परिक्षा कधी आहे?", roman: "bAI chAchaNI parikShA kadhI Ahe?", hint: "" },
      { en: "Next month", mr: "पुढच्या महिन्यात.", roman: "puDhachyA mahinyAt.", hint: "" },
      { en: "Is date decided?", mr: "तारीख ठरली का?", roman: "tArIkh TharalI kA?", hint: "" },
      { en: "Not yet", mr: "अजून नाही.", roman: "ajUn nAhI.", hint: "" },
      { en: "But mostly it will be from 15th", mr: "पण बहुतेक पंधरा (१५) तारखेपासून असेल", roman: "paN bahutek paMdharA (15) tArakhepAsUn asel", hint: "" },
      { en: "But start preparing from now onwards only", mr: "पण आत्तापासूनच तयारी सुरू करा", roman: "paN AttApAsUnach tayArI surU karA", hint: "" },
      { en: "Lets move towards the lesson", mr: "चला, आता धड्याकडे वळूया", roman: "chalA, AtA dhaDyAkaDe vaLUyA", hint: "" },
      { en: "Keep quiet", mr: "शांत बसा.", roman: "shAMt basA.", hint: "" },
      { en: "What is the noise in that corner?", mr: "त्या कोपऱ्यात काय गडबड चालू आहे?", roman: "tya koparyAt kAy gaDabaD chAlU Ahe?", hint: "" },
      { en: "Kaushik standup", mr: "कौशिक उभा रहा.", roman: "kaushik ubhA rahA.", hint: "" },
      { en: "Teacher, I am not doing anything", mr: "बाई मी काही नाही करते?", roman: "bAI mI kAhI nAhIkarate?", hint: "" },
      { en: "Then why is noise coming from there?", mr: "मग तिकडून आवाज का येतोय.", roman: "mag tikaDUn AvAj kA yetoy.", hint: "" },
      { en: "This Raju is telling joke to Sanju", mr: "हा राजू, संजू ला जोक संगतोय?", roman: "hA rAjU saMjU lA jok saMgatoy?", hint: "" },
      { en: "Raju, Is it time to tell joke?", mr: "राजू, ही जोक संगायची वेळ आहे?", roman: "rAjU, hI jok saMgAyachI veL Ahe?", hint: "" },
      { en: "No madam. Sorry", mr: "नाही बाई. सॉरी.", roman: "nAhI bAI. sorry.", hint: "" },
      { en: "Ok. All sit down", mr: "ठिक आहे. बसा सगळे खाली.", roman: "Thik Ahe. basA sagaLe khAlI.", hint: "" },
      { en: "If I hear noise again, I will make you stand for whole period", mr: "परत आवाज आला तर पूर्ण तासभर उभे करीन.", roman: "parat AvAj AlA tar pUrN tAsabhar ubhe karIn.", hint: "" },
      { en: "Lets start chapter", mr: "चला धडा सुरू करू.", roman: "chalA dhaDA surU karU.", hint: "" },
      { en: "Hello", mr: "हॅलो", roman: "Hello", hint: "" },
      { en: "I am Kaushik speaking", mr: "मी कौशिक बोलतोय", roman: "mI kaushik bolatoy", hint: "" },
      { en: "Yes; please go ahead", mr: "हं बोला", roman: "haM bolA", hint: "" },
      { en: "Is this number of Joshi?", mr: "हा जोश्यांचा नंबर आहे ना?", roman: "hA joshyAMchA naMbar Ahe nA", hint: "" },
      { en: "Is this house of Joshi?", mr: "जोश्यांचं घर ना?", roman: "joshyAMchM ghar nA", hint: "" },
      { en: "I wanted to speak with Vaibhav Joshi", mr: "मला वैभव जोशी यांच्याशी बोलायचं होतं", roman: "malA vaibhav joshI yAMchyAshI bolAyachaM hotaM", hint: "" },
      { en: "He is not at home", mr: "ते आत्ता घरात नाहियेत.", roman: "te AttA gharAt nAhiyet", hint: "" },
      { en: "When will he be back?", mr: "कधी येतील परत?", roman: "kadhI yetIl parat?", hint: "" },
      { en: "He will come in evening", mr: "संध्याकाळी येतील", roman: "saMdhyAkALI yetIl", hint: "" },
      { en: "Did you have any work with him?", mr: "काही काम होतं का?", roman: "kAhI kAm hotM kA?", hint: "" },
      { en: "Yes, wanted to give him a message", mr: "हो त्यांना एक निरोप द्यायचा होता", roman: "ho tyAMnA ek nirop dyAyachA hotA", hint: "" },
      { en: "Tell me. I will tell him once he is back", mr: "मला सांगा. मी त्यांना सांगतो आल्यावर.", roman: "malA sAMgA. mI tyAMnA sAMgato AlyAvar.", hint: "" },
      { en: "Ok. Tell him club meeting tomorrow at five", mr: "ठीक आहे. त्यांना सांगा उद्या क्लबची मीटिंग आहे. संध्याकाळी पाच वाजता.", roman: "ThIk Ahe. tyAMnA sAMgA udyA klabachI mITiMg Ahe. saMdhyAkALI pAch vAjatA.", hint: "" },
      { en: "Where?", mr: "कुठे आहे?", roman: "kuThe Ahe?", hint: "" },
      { en: "In park", mr: "पार्कमध्ये", roman: "pArkamadhye", hint: "" },
      { en: "Just wait. Door bell is ringing. I will open door", mr: "एक मिनिट थांबा दाराची बेल वाजत्ये. मी दार उघडतो.", roman: "ek miniT thAMbA dArAchI bel vAjatye. mI dAr ughaDato.", hint: "" },
      { en: "Probably its Vaibhav", mr: "बहुतेक वैभवच आला असेल.", roman: "bahutek vaibhavach AlA asel.", hint: "" },
      { en: "Hey Mr. Kulakarni, how are you?", mr: "बोला कुलकर्णी साहेब. कसे आहात.", roman: "bolA kulakarNI sAheb. kase AhAt.", hint: "" },
      { en: "I am fine. How are you?", mr: "मी मजेत. तुम्ही कसे आहात?", roman: "mI majet. tumhI kase AhAt?", hint: "" },
      { en: "I am fine too. Tell me. What were you up to?", mr: "मी पण मजेत. बोला काय काम होतं.", roman: "mI paN majet. bolA kAy kAm hotM.", hint: "" },
      { en: "Nothing special. Wanted to tell about meeting", mr: "विशेष काही नाही. मीटिंग बद्दल सांगायचं होतं.", roman: "visheSh kAhI nAhI. mITiMg baddal sAMgAyachaM hotaM.", hint: "" },
      { en: "I came to know. Mr. Rajwade met me. He told", mr: "मला कळलं त्याबद्दल. राजवाडे भेटले होते मला. ते बोलले.", roman: "malA kaLalM tyAbaddal. rAjavADe bheTale hote malA. te bolale.", hint: "" },
      { en: "Good", mr: "बरं झालं.", roman: "baraM jhAlM.", hint: "" },
      { en: "Ok then. See you tomorrow", mr: "ठीक आहे भेटू उद्या", roman: "ThIk Ahe bheTU udyA", hint: "" },
      { en: "Yes, see you", mr: "हो भेटुया.", roman: "ho bheTuyA.", hint: "" },
      { en: "I am Kaushik. Can I speak to Vaibhav?", mr: "मी कौशिक बोलतोय. वैभव आहेत का?", roman: "mI kaushik bolatoy. vaibhav Ahet kA?", hint: "" },
      { en: "Who Vaibhav?", mr: "कोण वैभव?", roman: "koN vaibhav?", hint: "" },
      { en: "Vaibhav joshi", mr: "वैभव जोशी.", roman: "vaibhav joshI.", hint: "" },
      { en: "No. This not number of Joshis", mr: "नाही हा जोश्यांचा नंबर नाही.", roman: "nAhI hA joshyAMchA naMbar nAhI.", hint: "" },
      { en: "It is 12345678, isn't it?", mr: "१२३४५६७८ च आहे ना?", roman: "12345678 ch Ahe nA?", hint: "" },
      { en: "No. It is 12345679. Wrong number.", mr: "नाही. १२३४५६७९ आहे. रॉंग नंबर", roman: "nAhI. 12345679 Ahe. wrong number", hint: "" },
      { en: "Ohh. Sorry", mr: "अरे. सॉरी", roman: "are. sorry.", hint: "" },
      { en: "I want to go to Hinjewadi. Where can I get bus?", mr: "मला हिंजवडीला जायचं आहे. बस कुठून मिळेल?", roman: "malA hiMjavaDIlA jAyachM Ahe. bas kuThUn miLel?", hint: "" },
      { en: "Not here. Go ahead", mr: "इथे नाही. पुढे जा.", roman: "ithe nAhI. puDhe jA.", hint: "" },
      { en: "Where ahead?", mr: "पुढे कुठे?", roman: "puDhe kuThe?", hint: "" },
      { en: "There under that bridge", mr: "त्या पुला खाली", roman: "tyA pulA khAlI", hint: "" },
      { en: "Ok. Thanks", mr: "बरं. थॅंक्स", roman: "baraM. th~aMks", hint: "" },
      { en: "Does Hinjewadi bus start from here?", mr: "हिंजवडीची बस इथुनच सुटते का?", roman: "hiMjavaDIchI bas ithunach suTate kA?", hint: "" },
      { en: "Yes", mr: "हो.", roman: "ho.", hint: "" },
      { en: "When is the next bus?", mr: "पुढची बस कधी आहे?", roman: "puDhachI bas kadhI Ahe?", hint: "" },
      { en: "Don't know", mr: "माहित नाही.", roman: "mAhit nAhI.", hint: "" },
      { en: "Uncle, do you know when is the next bus?", mr: "काका, तुम्हाला माहिती आहे का; पुढची बस कधी आहे ते?", roman: "kAkA, tumhAlA mAhitI Ahe kA? puDhachI bas kadhI Ahe te?", hint: "" },
      { en: "Yes it is at 10 past 10", mr: "हो दहा दहा ची आहे.", roman: "ho dahA dahA chI Ahe.", hint: "" },
      { en: "Oh god. It is half an hour more. Does any other bus go to Hinjewadi?", mr: "अरे बापरे. अजून अर्धा तास आहे. दुसरी कुठली बस जाते का हिंजवडीला.", roman: "are bApare. ajUn ardhA tAs Ahe. dusarI kuThalI bas jAte kA hiMjavaDIlA.", hint: "" },
      { en: "No. That is the only one. Catch bus for Chinchwad. Get down at Dange Chowk. Take another bus from there.", mr: "नाही ती एकच आहे. तुम्ही चिंचवडची बस पकडा. डांगे चौकात उतरा. आणि तिकडून दुसरी बस पकडा.", roman: "nAhI tI ekach Ahe. tumhI chiMchavaDachI bas pakaDA. DAMge chaukAt utarA ANi tikaDUn dusarI bas pakaDA.", hint: "" },
      { en: "Will I get bus for phase-3 directly?", mr: "डायरेक्ट फेज-३ पर्यंत मिळेल का?", roman: "DAyarekT phej-3 paryaMt miLel kA?", hint: "" },
      { en: "Mostly you will get. Otherwise catch bus for phase-2", mr: "बहुतेक मिळेल. नाहितर फेज-२ पर्यंत जाणारी बस पकडा.", roman: "bahutek miLel. nAhitar phej-2 paryaMt jANArI bas pakaDA.", hint: "" },
      { en: "And then?", mr: "आणि पुढे?", roman: "ANi puDhe?", hint: "" },
      { en: "From phase-2 you will get share-auto for phase-3", mr: "फेज-२ पासून पुढे शेअर रिक्शा मिळते फेज-३ ला जायला.", roman: "phej-2 pAsUn puDhe shear rikshA miLate phej-3 lA jAyalA.", hint: "" },
      { en: "From where does bus for Chinchwad start?", mr: "चिंचवडची बस कुठून सुटते?", roman: "chiMchavaDachI bas kuThUn suTate?", hint: "" },
      { en: "From that next stop. Get in and stand in queue.", mr: "या पुढच्या स्टॉप पासून. आत रांगेत उभे रहा.", roman: "yA puDhachyA sT~op pAsUn. At rAMget ubhe rahA.", hint: "" },
      { en: "Which ticket you want?", mr: "तिकिट बोला. / तुम्हाला कुठलं तिकिट पाहिजे", roman: "tikiT bolA. / tumhAlA kuThalaM tikiT pAhije", hint: "" },
      { en: "1 Dange chowk", mr: "एक डांगे चौक द्या.", roman: "ek DAMge chauk dyA.", hint: "" },
      { en: "Twelve rupees", mr: "बारा रुपये.", roman: "bArA rupaye.", hint: "" },
      { en: "Here it is", mr: "हे घ्या.", roman: "he ghyA.", hint: "" },
      { en: "Give two rupees change", mr: "दोन रुपये सुट्टे द्या.", roman: "don rupaye suTTe dyA.", hint: "" },
      { en: "I do not have change", mr: "माझ्याकडे सुट्टे नाहित.", roman: "mAjhyAkaDe suTTe nAhit.", hint: "" },
      { en: "Please check carefully. There may be some in your bag.", mr: "बघा जरा नीट. बॅगेत असतील.", roman: "baghA jarA nIT. b~aget asatIl.", hint: "" },
      { en: "Let me check", mr: "बघतो.", roman: "baghato.", hint: "" },
      { en: "I have 5", mr: "५ आहेत.", roman: "5 Ahet.", hint: "" },
      { en: "I will give you 3 rupees afterwards. Take it while getting down", mr: "३ रुपये नंतर देतो. उतरताना घ्या.", roman: "3 rupaye naMtar deto. utaratAnA ghyA.", hint: "" },
      { en: "I do not know the stop. Can you tell me once we reach there?", mr: "मला स्टॉप माहित नाहिये. स्टॉप आला की सांगा.", roman: "malA sT~op mAhit nAhiye. sT~op AlA kI sAMgA.", hint: "" },
      { en: "Hello, it is Dange chowk", mr: "चला. डांगे चौक.", roman: "chalA. DAMge chauk.", hint: "" },
      { en: "Should I get down here?", mr: "मी उतरू का इकडे.", roman: "mI utarU kA ikaDe.", hint: "" },
      { en: "My 3 rupees are pending", mr: "माझे तीन रुपये राहिलेत.", roman: "mAjhe tIn rupaye rAhilet.", hint: "" },
      { en: "I love you", mr: "माझं तुझ्यावर प्रेम आहे", roman: "mAjhaM tujhyAvar prem Ahe", hint: "" },
      { en: "I love you (Boy to Girl)", mr: "मी तुझ्यावर प्रेम करतो", roman: "mI tujhyAvar prem karato", hint: "" },
      { en: "I love you (Girl to Boy)", mr: "मी तुझ्यावर प्रेम करते", roman: "mI tujhyAvar prem karate", hint: "" },
      { en: "I like you (Girl to Boy)", mr: "मला तू आवडतोस", roman: "malA tU AvaDatos", hint: "" },
      { en: "I like you (Boy to Girl)", mr: "मला तू आवडतेस", roman: "malA tU AvaDates", hint: "" },
      { en: "You are very beautiful", mr: "तू खूप सुंदर आहेस", roman: "tU khUp suMdar Ahes", hint: "" },
      { en: "Shall we marry?", mr: "आपण लग्न करूया का.", roman: "ApaN lagn karUyA kA.", hint: "" },
      { en: "Will you marry me?", mr: "तू माझ्याशी लग्न करशील का?", roman: "tU mAjhyAshI lagn karashIl kA?", hint: "" },
      { en: "Yes, Lets marry!!", mr: "हो. आपण लग्न करूया.", roman: "ho. ApaN lagn karUyA.", hint: "" },
      { en: "But my family members do not like it", mr: "पण माझ्या घरच्यांना हे पसंत नाही.", roman: "paN mAjhyA gharachyAMnA he pasaMt nAhI.", hint: "" },
      { en: "We shall elope and get married", mr: "आपण पळून जाऊन लग्न करू.", roman: "ApaN paLUn jAUn lagn karU.", hint: "" },
      { en: "No. I do not want to get married secretly", mr: "नाही. मला लपूनछपून लग्न करायचे नाही.", roman: "nAhI. malA lapUnaChapUn lagn karAyache nAhI.", hint: "" },
      { en: "I will marry only if my parents allow", mr: "माझ्या आई वडीलांनी परवानगी दिली तरच मी लग्न करीन", roman: "mAjhyA AI vaDIlAMnI paravAnagI dilI tarach mI lagn karIn", hint: "" },
      { en: "I will convince your parents", mr: "मी तुझ्या आई वडिलांना समजावेन.", roman: "mI tujhyA AI vaDilAMnA samajAven.", hint: "" },
      { en: "I am ready to leave my home, my parents for you", mr: "तुझ्यासाठी मी माझं घर, माझ्या आईवडिलांना सोडायला तयार आहे", roman: "tujhyAsAThI mI mAjhM ghar, mAjhyA AIvaDilAMnA soDAyalA tayAr Ahe", hint: "" },
      { en: "I am ready to come with you anywhere you say", mr: "तू म्हणशील तिथे मी तुझ्या बरोबर यायला तयार आहे", roman: "tU mhaNashIl tithe mI tujhyA barobar yAyalA tayAr Ahe", hint: "" },
      { en: "I trust you completely", mr: "माझा तुझ्यावर पूर्ण विश्वास आहे", roman: "mAjhA tujhyAvar pUrN vishvAs Ahe", hint: "" },
      { en: "Why do you sulk (Boy to Girl)", mr: "तू का रुसली आहेस", roman: "tU kA rusalI Ahes", hint: "" },
      { en: "Why do you sulk (Girl to Boy)", mr: "तू का रुसला आहेस", roman: "tU kA rusalA Ahes", hint: "" },
      { en: "Why are you angry (Boy to Girl)", mr: "तू का रागावली आहेस", roman: "tU kA rAgAvalI Ahes", hint: "" },
      { en: "Why are you angry (Girl to Boy)", mr: "तू का रागावला आहेस", roman: "tU kA rAgAvalA Ahes", hint: "" },
      { en: "Why don't you talk with me?", mr: "तू माझ्याशी का बोलत नाहीस", roman: "tU mAjhyAshI kA bolat nAhIs", hint: "" },
      { en: "I will not talk with you", mr: "मी तुझ्याशी बोलणार नाही", roman: "mI tujhyAshI bolaNAr nAhI", hint: "" },
      { en: "I miss you a lot", mr: "मला तुझी खूप आठवण येते", roman: "malA tujhI khUp AThavaN yete", hint: "" },
      { en: "I can not live without you", mr: "मी तुझ्याशिवाय जगू शकत नाही", roman: "mI tujhyAshivAy jagU shakat nAhI", hint: "" },
      { en: "I want to marry your daughter", mr: "मला तुमच्या मुलीशी लग्न करायचे आहे", roman: "malA tumachyA mulIshI lagn karAyache Ahe", hint: "" },
      { en: "I want to marry your son", mr: "मला तुमच्या मुलाशी लग्न करायचे आहे", roman: "malA tumachyA mulAshI lagn karAyache Ahe", hint: "" },
      { en: "I will keep your son/daughter happy", mr: "मी तुमच्या मुलाला/मुलीला नेहमी सुखात/ आनंदात ठेवीन", roman: "mI tumachyA mulAlA/mulIlA nehamI sukhAt/ AnaMdAt ThevIn", hint: "" },
      { en: "We will always live very happily", mr: "आपण नेहमी सुखात/आनंदात राहू.", roman: "ApaN nehamI sukhAt/ AnaMdAt rAhU", hint: "" },
      { en: "We two! King-and-Queen", mr: "आपण दोघं राजाराणी", roman: "ApaN doghaM rAjArANI", hint: "" },
      { en: "Hello", mr: "हॅलो / नमस्कार", roman: "h~alo / namaskAr", hint: "" },
      { en: "Let me see your resume", mr: "तुमचा रेझ्युमे बघू", roman: "tumachA rejhyume baghU", hint: "" },
      { en: "Tell me a bit about yourself", mr: "मला जरा तुमच्या बद्दल सांगा", roman: "malA jarA tumachyA baddal sAMgA", hint: "" },
      { en: "My name is Kaushik Lele", mr: "माझं नाव कौशिक लेले", roman: "mAjhM nAv kaushik lele", hint: "" },
      { en: "I am from Mumbai", mr: "मी मुंबईचा आहे", roman: "mI muMbaIchA Ahe", hint: "" },
      { en: "I was born in Mumbai", mr: "माझा जन्म मुंबईत झाला.", roman: "mAjhA janm muMbaIt jhAlA.", hint: "" },
      { en: "Primary education took place in Delhi", mr: "प्राथमिक शिक्षण दिल्लीत झालं.", roman: "prAthamik shikShaN dillIt jhAlM.", hint: "" },
      { en: "My college was also in Delhi", mr: "माझं कॉलेज सुद्धा दिल्लीला होतं", roman: "mAjhaM k~olej suddhA dillIlA hotaM", hint: "" },
      { en: "Which college?", mr: "कुठलं कॉलेज?", roman: "kuThalaM k~olej?", hint: "" },
      { en: "Delhi Engineering College", mr: "दिल्ली इंजिनिअरिंग कॉलेज", roman: "dillI iMjiniariMg k~olej", hint: "" },
      { en: "From where did you do M.B.A.?", mr: "तुम्ही एम.बी.ए कुठून केलंत?", roman: "tumhI em.bI.e kuThUn kelMt?", hint: "" },
      { en: "I did MBA from IIM Ahmedabad", mr: "मी एम.बी.ए आय.आय.एम. अहमदाबाद मधून केलं.", roman: "mI em.bI.e Ay.Ay.em. ahamadAbAd madhUn kelM.", hint: "" },
      { en: "How much total experience do you have?", mr: "तुमचा एकूण अनुभव किती आहे?", roman: "tumachA ekUN anubhav kitI Ahe?", hint: "" },
      { en: "I have 10 years of experience in IT", mr: "माझा आय.टी. मधला अनुभव १० वर्षांचा आहे.", roman: "mAjhA Ay.TI. madhalA anubhav 10 varShAMchA Ahe.", hint: "" },
      { en: "Which companies have you worked in?", mr: "कुठल्या कंपन्यांमध्ये तुम्ही काम केलं आहे?", roman: "kuThalyA kaMpanyAMmadhye tumhI kAm kelM Ahe.", hint: "" },
      { en: "ABC, PQR and XYZ. Currently in XYZ company", mr: "ABC, PQR आणि XYZ. सध्या XYZ कंपनीत आहे.", roman: "ABC, PQR ANi XYZ. sadhyA kaMpanIt Ahe.", hint: "" },
      { en: "What kind of work do you do currently?", mr: "सध्या कामाचं स्वरूप काय आहे?", roman: "sadhyA kAmAchaM svarUp kAy Ahe?", hint: "" },
      { en: "I am senior software developer", mr: "मी सिनिअर सोफ्टवेअर डेव्हलपर आहे.", roman: "mI siniar sophTavear Devhalapar Ahe.", hint: "" },
      { en: "Which technologies do you work on?", mr: "कुठल्या टेक्नोलोजी वर काम करता?", roman: "kuThalyA TeknolojI var kAm karatA?", hint: "" },
      { en: "Java, Web-Service, Spring", mr: "जावा, वेब-सर्विस, स्प्रिंग.", roman: "jAvA, veba-sarvis, spriMg.", hint: "" },
      { en: "Who all do you have at home?", mr: "तुमच्या घरी कोण असतं?", roman: "tumachyA gharI koN asatM?", hint: "" },
      { en: "Mother, Father, two brothers and one sister", mr: "आई, वडील, दोन भाऊ आणि एक बहीण.", roman: "AI, vaDIl, don bhAU ANi ek bahIN.", hint: "" },
      { en: "Do you live together?", mr: "सगळे एकत्र रहता का?", roman: "sagaLe ekatr rahatA kA?", hint: "" },
      { en: "Yes. We all live in Pune", mr: "हो सगळे सध्या पुण्यात राहतो.", roman: "ho sagaLe sadhyA puNyAt rAhato.", hint: "" },
      { en: "What do your siblings do?", mr: "तुमची भावंडे काय करतात?", roman: "tumachI bhAvaMDe kAy karatAt?", hint: "" },
      { en: "Elder brother is in bank. Other siblings are studying", mr: "मोठा भाऊ बॅंकेत आहे. बाकीची भावंडे शिकत आहेत.", roman: "moThA bhAU b~aMket Ahe. bAkIchI bhAvaMDe shikat Ahet.", hint: "" },
      { en: "What are your hobbies?", mr: "तुमचे छंद काय आहेत?", roman: "tumache ChaMd kAy Ahet?", hint: "" },
      { en: "I like reading", mr: "मला वाचन करायला आवडते.", roman: "malA vAchan karAyalA AvaDate.", hint: "" },
      { en: "What are your strengths and weaknesses?", mr: "तुमच्या स्ट्रेंथ्स आणि वीकनेस काय अहेत?", roman: "tumachyA sTreMths ANi vIkanes kAy ahet?", hint: "" },
      { en: "Positive attitude and dedication", mr: "सकारात्मक विचार आणि डेडीकेशन.", roman: "sakArAtmak vichAr ANi DeDIkeshan.", hint: "" },
      { en: "What do you expect from this job?", mr: "तुम्हाला या जॉब कडून काय अपेक्षा आहेत?", roman: "tumhAlA yA j~ob kaDUn kAy apekShA Ahet?", hint: "" },
      { en: "It was nice talking with you", mr: "तुमच्याशी बोलून बरं वाटलं.", roman: "tumachyAshI bolUn baraM vATalM.", hint: "" },
      { en: "Our H.R. will let you know", mr: "आमचे एच.आर तुम्हाला कळवतील.", roman: "Amache ech.Ar tumhAlA kaLavatIl.", hint: "" },
      { en: "Thanks", mr: "धन्यवाद.", roman: "dhanyavAd", hint: "" },
      { en: "Come aunty", mr: "या मावशी", roman: "yA mAvashI", hint: "" },
      { en: "Will you do work at our place?", mr: "आमच्याकडचं काम कराल का?", roman: "AmachyAkaDachM kAm karAl kA?", hint: "" },
      { en: "What all is work?", mr: "काय काय काम आहे?", roman: "kAy kAy kAm Ahe?", hint: "" },
      { en: "Washing clothes and dishes and floor-cleaning", mr: "धुणं, भांडी आणि केरफरशी", roman: "dhuNaM, bhAMDI ANi kerapharashI", hint: "" },
      { en: "For how many people?", mr: "किती जणांचं धुणं-भांडी", roman: "kitI jaNAMchaM dhuNM-bhAMDI", hint: "" },
      { en: "We are 4 elders and 2 children", mr: "आम्ही ४ मोठी माणसं आहोत आणि २ लहान मुलं आहेत.", roman: "AmhI 4 moThI mANasaM Ahot ANi 2 lahAn mulaM Ahet.", hint: "" },
      { en: "Ok. 700 for Clothes, 700 for dishes", mr: "बरं. धुण्याचे सातशे आणि भांड्यांचे सातशे होतील.", roman: "baraM. dhuNyAche sAtashe ANi bhAMDyAMche sAtashe hotIl.", hint: "" },
      { en: "200 for floor cleaning", mr: "लाद्या पुसायचे दोनशे.", roman: "lAdyA pusAyache donashe.", hint: "" },
      { en: "700 for clothes and dishes seems a lot", mr: "पण धुण्याचे आणि भांड्यांचे सातशे म्हणजे खूपच वाटतात.", roman: "paN dhuNyAche ANi bhAMDyAMche sAtashe mhaNaje khUpach vATatAt.", hint: "" },
      { en: "Please take 500 aunty", mr: "पाचशे घ्या ना मावशी.", roman: "pAchashe ghyA nA mAvashI.", hint: "" },
      { en: "We charge 150 per person", mr: "माणशी दीडशेच घेतो.", roman: "mANashI dIDashech gheto.", hint: "" },
      { en: "600 for clothes, 600 for dishes and 200 for cleaning", mr: "सहाशे धुण्याचे; सहाशे भांड्यांचे आणि दोनशे लादी पुसायचे.", roman: "sahAshe dhuNyAche; sahAshe bhAMDyAMche ANi donashe lAdI pusAyache.", hint: "" },
      { en: "I will take 4 holidays every month", mr: "महिन्यातून ४ सुट्ट्या घेत जाईन.", roman: "mahinyAtUn 4 suTTyA ghet jAIn.", hint: "" },
      { en: "Do not take unplanned leaves without informing", mr: "पण न सांगता दांड्या मारू नका.", roman: "hM. paN na sAMgatA dAMDyA mArU nakA.", hint: "" },
      { en: "Start the work from today itself", mr: "आजपासूनच सुरुवात करा कामाला.", roman: "AjapAsUnach suruvAt karA kAmAlA.", hint: "" },
      { en: "Pots-n-Dishes are in basin. Take them to bathroom", mr: "भांडी बेसिन मध्ये ठेवली आहेत ती मोरीत घेऊन जा.", roman: "bhAMDI besin madhye ThevalI Ahet tI morIt gheUn jA.", hint: "" },
      { en: "Soap and scrubber is there in that corner", mr: "साबण, घासणी तिकडे कोपऱ्यात आहे.", roman: "sAbaN, ghAsaNI tikaDe koparxyAt Ahe.", hint: "" },
      { en: "Take this your salary", mr: "हा घ्या तुमचा पगार.", roman: "hA ghyA tumachA pagAr.", hint: "" },
      { en: "Aunty, you did not give me bonus for Diwali", mr: "काकू दिवाळीचा बोनस नाही दिलात.", roman: "kAkU divALIchA bonas nAhI dilAt.", hint: "" },
      { en: "Take these 400 extra", mr: "हे घ्या चारशे जास्ती देते.", roman: "he ghyA chaarashe jAstI dete.", hint: "" },
      { en: "See you / Will come again", mr: "येते मी.", roman: "yete mI.", hint: "" },
      { en: "Hi Sara, I heard 26 Jan is holiday - Republic Day", mr: "हाना: हाय सारा. मला आत्ताच कळलं २६ जानेवारीला भारतात सुट्टी आहे कारण 26 जानेवारी हा इंडियाचा रिपब्लिक डे असतो!", roman: "hAnA hAy sArA. malA AttAch kaLalM jAnevArIlA bhAratAt suTTI Ahe kAraN jAnevArI hA iMDiyAchA ripablik De asato!", hint: "" },
      { en: "What is that actually?", mr: "हे नक्की काय असतं?", roman: "he nakkI kAy asatM?", hint: "" },
      { en: "Yes, right. Prajasattak Din in Marathi", mr: "हो बरोबर. हो मराठीत प्रजासत्ताकदिन असं म्हणतात.", roman: "ho barobar. ho marAThIt prajAsattAkadin asM mhaNatAt.", hint: "" },
      { en: "Constitution got approval on Nov 26, 1949", mr: "संविधानाला २६ नोव्हेंबर १९४९ मध्ये मंजुरी मिळाली.", roman: "sMvidhAnAlA novheMbar madhye mMjurI miLAlI.", hint: "" },
      { en: "Implemented on 26 January 1950", mr: "आणि अखेरीस २६ जानेवारी १९५० रोजी संविधान अंमलात आले.", roman: "ANi akherIs jAnevArI rojI sMvidhAn aMmalAt Ale.", hint: "" },
      { en: "How is the day celebrated?", mr: "हा दिवस कसा साजरा केला जातो?", roman: "hA divas kasA sAjarA kelA jAto?", hint: "" },
      { en: "Flag hoisting and salute in morning", mr: "सकाळच्या वेळी ध्वज फडकवून, झेंडावंदन करून समारंभ सुरू केला जातो.", roman: "sakALachyA veLI dhvaj phaDakavUn, jheMDAvMdan karUn samArMbh surU kelA jAto.", hint: "" },
      { en: "Parade at Rajpath New Delhi, 3 days", mr: "राजपथ नवी दिल्ली येथे संरक्षण मंत्रायल एक कार्यक्रम आयोजित करते, जो तीन दिवस चालतो.", roman: "rAjapath navI dillI yethe sMrakShaN mMtrAyal ek kAryakram Ayojit karate, jo tIn divas chAlato.", hint: "" },
      { en: "Happy Republic day", mr: "हो, प्रजासत्ताक दिनाच्या शुभेच्छा", roman: "ho, prajAsattAk dinAchyA shubhechChA.", hint: "" },
      { en: "Thank you", mr: "धन्यवाद!", roman: "dhanyavAd!", hint: "" },
      { en: "Hi, I want to open a saving account", mr: "नमस्कार, मला आपल्या बॅंकेत बचत खाते उघडायचे आहे.", roman: "namaskAr, malA ApalyA b~aMket bachat khAte ughaDAyache Ahe.", hint: "" },
      { en: "From where will I get form to open account?", mr: "खाते उघडण्यासाठी मला फॉर्म कुठून मिळेल?", roman: "khAte ughaDaNyAsAThI malA ph~orm kuThUn miLel?", hint: "" },
      { en: "I want to meet Branch manager", mr: "मला शाखा व्यवस्थापकांना भेटायचे आहे. ते कुठे बसतात?", roman: "malA shAkhA vyavasthApakAMnA bheTAyache Ahe. te kuThe basatAt?", hint: "" },
      { en: "I had applied for ATM card 1 month back. Not received yet", mr: "मी एक महिन्यापूर्वी एटीएम कार्डासाठी अर्ज केला होता पण अजून मिळाले नाही.", roman: "mI eka mahinyApUrvI eTIem kArDAsAThI arj kelA hotA paN ajUn miLAle nAhI.", hint: "" },
      { en: "How can I apply for cheque book?", mr: "मी चेकबुकसाठी अर्ज कसा करू?", roman: "mI chekabukasAThI arj kasA karU?", hint: "" },
      { en: "I want to make a DD. Where is the form?", mr: "मला डिमांड ड्राफ्ट तयार करायचा आहे. डीडी बनवायसाठी मला फॉर्म कुठे मिळेल?", roman: "malA DimAMD DrAphT tayAr karAyachA Ahe. DIDI banavAyasAThI malA ph~orm kuThe miLel?", hint: "" },
      { en: "Where is feedback box?", mr: "अभिप्राय पेटी कुठे आहे?", roman: "abhiprAy peTI kuThe Ahe?", hint: "" },
      { en: "Please fill up this application form", mr: "कृपया खाते उघडण्यासाठी हा अर्ज भरा", roman: "kRupayA khAte ughaDaNyAsAThI hA arj bharA", hint: "" },
      { en: "How much do you want to deposit?", mr: "तुम्हाला तुमच्या खात्यात किती रक्कम जमा करायची आहे?", roman: "tumhAlA tumachyA khAtyAt kitI rakkam jamA karAyachI Ahe?", hint: "" },
      { en: "What is minimum deposit?", mr: "मी कमीतकमी कीती रक्कम जमा करू शकतो?", roman: "mI kamitakamI kItI rakkam jamA karU shakato?", hint: "" },
      { en: "How long for cheque to arrive?", mr: "मला चेक मिळायला किती वेळ लागेल?", roman: "mala chek milayala kiti vel lagel?", hint: "" },
      { en: "Cheque takes approximately 2 weeks", mr: "चेक येण्यासाठी अंदाजे दोन आठवडे लागतात.", roman: "chek yeNyAsAThI aMdAje don AThavaDe lAgatAt.", hint: "" },
      { en: "I need locker facility", mr: "मला तिजोरीची सुविधा हवी आहे.", roman: "malA tijorIchI suvIdhA havI Ahe.", hint: "" },
      { en: "I want last year's account statements", mr: "मला मागच्या वर्षाचे अकाउंट स्टेटमेंट हवे आहे.", roman: "malA mAgachyA varShAche akAuMT sTeTameMT have Ahe.", hint: "" },
      { en: "I need net banking facility", mr: "मला माझ्या खात्यासाठी नेट बॅंकिगची सुविधा हवी आहे.", roman: "malA mAjhyA khAtyAsAThI neT b~aMkigachI suvidhA havI Ahe.", hint: "" },
      { en: "Go to counter number 4", mr: "काउंटर नंबर चारवर जा.", roman: "kAuMTar nMbar chAravar jA.", hint: "" },
      { en: "Attach two photos. Also AADHAR copy", mr: "याच्यावर दोन फोटो लावा. आणि आधार कार्डची कॉपी सुद्धा जोडावी लागेल.", roman: "yAchyAvar don phoTo lAvA. ANi AdhAr kArDachI k~opI suddhA joDAvI lAgel.", hint: "" },
      { en: "Can voter-id work?", mr: "वोटर कार्ड चालेल का?", roman: "voTar kArD chAlel kA?", hint: "" },
      { en: "Why did you not write wife's name?", mr: "इथे पत्नीचे नाव का नाही लिहिले?", roman: "ithe patnIche nAv kA nAhI lihile?", hint: "" },
      { en: "Sir, I am not married", mr: "साहेब माझे लग्न झाले नाही आहे.", roman: "sAheb mAjhe lagn jhAle nAhI Ahe.", hint: "" },
      { en: "This photo is not allowed", mr: "हा फोटो चालणार नाही.", roman: "hA phoTo chAlaNAr nAhI.", hint: "" },
      { en: "Please take a photo and bring it", mr: "फोटो काढून आणा", roman: "phoTo kADhUn ANA", hint: "" },
      { en: "I want some information about this temple", mr: "मला या मंदिराबद्दल थोडी माहिती हवी आहे.", roman: "malA yA maMdirAbaddal thoDI mAhitI havI Ahe.", hint: "" },
      { en: "Who can help me?", mr: "मला कोण मदत करू शकेल?", roman: "malA koN madat karU shakel?", hint: "" },
      { en: "Go straight. There is enquiry counter", mr: "तुम्ही सरळ जा. तिकडे चौकशीचे काउंटर आहे.", roman: "tumhI saraL jA tikaDe. tikaDe chaukashIche kAuMTar Ahe.", hint: "" },
      { en: "What are the Darshan timings?", mr: "मंदिराची दर्शनाची वेळ काय आहे", roman: "maMdirAchI darshanAchI veL kAy Ahe", hint: "" },
      { en: "Morning 7 to 11 and Evening 4 to 8", mr: "सकाळी सात ते अकरा आणि संध्याकाळी चार ते आठ", roman: "sakALI sAt te akarA ANi saMdhyAkALI chAr te ATh", hint: "" },
      { en: "When is it crowded more?", mr: "गर्दी कधी जास्त असते?", roman: "gardI kadhI jAst asate?", hint: "" },
      { en: "Come for Mangalarati. At 4.30 early morning", mr: "मंगलारती ला या. पहाटे साडे चार वाजता या.", roman: "maMgalAratI lA yA. pahATe sADe chAr vAjatA yA.", hint: "" },
      { en: "What is timing for Prasad?", mr: "प्रसादची वेळ काय आहे?", roman: "prasAdachI veL kAy Ahe?", hint: "" },
      { en: "Afternoon 12 to 2", mr: "दुपारी बारा ते दोन.", roman: "dupArI bArA te don.", hint: "" },
      { en: "There are 4 halls for Prasad", mr: "तिथे चार प्रसाद भवन आहेत.", roman: "tithe chAr prasAd bhavan Ahet.", hint: "" },
      { en: "Hey Buddy, whats up?", mr: "मित्रा! काय म्हणतोस?", roman: "mitrA! kAy mhaNatos?", hint: "" },
      { en: "There was your football match yesterday, wasn't it?", mr: "तुझी आज फुटबॉलची मॅच होती ना", roman: "tujhI Aj football m~ach hotI nA?", hint: "" },
      { en: "How was it?", mr: "कशी झाली?", roman: "kashI jhAlI?", hint: "" },
      { en: "Quite exciting", mr: "जबरदस्त.", roman: "jabaradast.", hint: "" },
      { en: "With whom?", mr: "कोणाबारोबर होती?", roman: "koNAbArobar hotI?", hint: "" },
      { en: "Who did win then?", mr: "मग कोण जिंकलं?", roman: "mag koN jiMkalM?", hint: "" },
      { en: "Is it a question? It's we!", mr: "हे काय विचारणं झालं? आम्हीच.", roman: "he kAy vichAraNM jhAlM? AmhIch.", hint: "" },
      { en: "Only 1 goal. We won 1-0", mr: "एकच गोल झाला. आम्ही एक-शून्य असे जिंकलो.", roman: "ekach gol jhAlA. AmhI ekshUny ase jiMkalo.", hint: "" },
      { en: "Nice! Congratulations", mr: "वा. अभिनंदन.", roman: "vA. abhinMdan.", hint: "" },
      { en: "I am a defender", mr: "नाही रे. मी तर डिफेंडर आहे.", roman: "nAhI re. mI tar DipheMDar Ahe.", hint: "" },
      { en: "Did it rain during your match?", mr: "तुमच्या मॅचच्या वेळी पाऊस पडला का?", roman: "tumachyA m~achachyA veLI pAUs paDalA kA?", hint: "" },
      { en: "Yes it rained heavily", mr: "हो. भयंकर पाऊस झाला.", roman: "ho. bhayMkar pAUs jhAlA.", hint: "" },
      { en: "Do inform me for next match", mr: "पुढच्या वेळी तुझी मॅच असेल तेव्हा मला आधी सांग.", roman: "puDhachyA veLI tujhI m~ach asel tevhA malA AdhI sAMg.", hint: "" },
      { en: "Hey buddy, let's go to watch movie today", mr: "मित्रा, चल आज आपण सिनेमा बघायला जाऊया.", roman: "mitrA, chal Aj ApaN sinemA baghAyalA jAUyA.", hint: "" },
      { en: "But which movie?", mr: "पण कोणता सिनेमा?", roman: "paN koNatA sinemA?", hint: "" },
      { en: "Let's go to watch Raazi", mr: "आपण राझी बघायला जाऊया.", roman: "ApaN rAjhI baghAyalA jAUyA.", hint: "" },
      { en: "No friend; I have already seen that movie", mr: "नको मित्रा, तो सिनेमा मी आघीच बघितला आहे.", roman: "nako mitrA, to sinemA mI AghIch baghitalA Ahe.", hint: "" },
      { en: "Let's go to watch Surma", mr: "मग सूरमा बघायला जाऊया.", roman: "mag sUramA baghAyalA jAUyA.", hint: "" },
      { en: "But that movie hasn't been released yet", mr: "पण तो सिनेमा अजून रिलीज झाला नाही.", roman: "paN to sinemA ajUn rilIj jhAlA nAhI.", hint: "" },
      { en: "Let's go and watch Kaala", mr: "काला बघायला जाऊया.", roman: "kAlA baghAyalA jAUyA.", hint: "" },
      { en: "Rajnikant is in that movie", mr: "त्यामध्ये रजनीकांत आहे.", roman: "tyAmadhye rajanIkAMt Ahe.", hint: "" },
      { en: "It's running in Alankar theatre", mr: "अलंकार थेटरला लागला आहे.", roman: "alaMkAr theTaralA lAgalA Ahe.", hint: "" },
      { en: "Half past six", mr: "साडे सहा वाजता.", roman: "sADe sahA vAjatA.", hint: "" },
      { en: "I will come to your place at six", mr: "मी तुझ्या घरी सहा वाजता येतो.", roman: "mI tujhyA gharI sahA vAjatA yeto.", hint: "" },
      { en: "Friend, are you watching world cup these days?", mr: "मित्रा, तू सध्या वर्ल्ड कप बघतो आहेस का?", roman: "mitrA, tU sadhyA varlD kap baghato Ahes kA?", hint: "" },
      { en: "Which team are you supporting?", mr: "तू कोणत्या टीमला सपोर्ट करतो आहेस?", roman: "tU koNatyA TImalA saporT karato Ahes?", hint: "" },
      { en: "I am fan of Messi. Supporting Argentina", mr: "मी मेस्सीचा फॅन आहे त्यामुळे मी अर्जेंटिनाला सपोर्ट करतो आहे.", roman: "mI messIchA ph~an Ahe tyAmuLe mI arjeMTinAlA saporT karato Ahe.", hint: "" },
      { en: "I am Ronaldo fan but supporting Brazil", mr: "मी रोनाल्डोचा फॅन आहे पण मी ब्राझीलला सपोर्ट करतो आहे.", roman: "mI ronAlDochA ph~an Ahe paN mI brAjhIlalA saporT karato Ahe.", hint: "" },
      { en: "Have you seen yesterday's match? Germany vs Korea", mr: "तू कालची मॅच बघितलीस का? जर्मनी आणि कोरियाची.", roman: "tU kAlachI m~ach baghitalIs kA? jarmanI ANi koriyAchI.", hint: "" },
      { en: "Yes friend, that was a very good match", mr: "हो मित्रा, खूप चांगली होती.", roman: "ho mitrA, khUp chAMgalI hotI.", hint: "" },
      { en: "Korea defended very good", mr: "कोरियाने खूप चांगला डिफेन्स केला", roman: "koriyAne khUp chAMgalA Diphens kelA", hint: "" },
      { en: "He dives very well", mr: "तो खूप छान झेप घेतो.", roman: "to khUp ChAn jhep ghetto.", hint: "" },
      { en: "Hey Kaushik, where are you going in so hurry?", mr: "अरे कौशिक, इतक्या घाईत कुठे जातोयस?", roman: "are kaushik, itakyA ghAIt kuThe jAtoyas?", hint: "" },
      { en: "I am going to my hobby class", mr: "मी माझ्या छंदवर्गाला जातोय.", roman: "mI maajhyA ChaMdavargAlA jaatoy.", hint: "" },
      { en: "Wow. What are you learning?", mr: "वा! तू काय शिकतोयस?", roman: "vA! tU kAy shikatoyas?", hint: "" },
      { en: "I am learning to play guitar", mr: "मी गिटार वाजवायला शिकतोय.", roman: "mI giTAr vAjavAyalA shikatoy.", hint: "" },
      { en: "I am also interested in learning guitar", mr: "मला पण गिटार शिकण्यात रस आहे.", roman: "malA paN giTAr shikaNyAt ras Ahe.", hint: "" },
      { en: "Who is your teacher?", mr: "तुझे शिक्षक कोण आहेत?", roman: "tujhe shikShak koN Ahet?", hint: "" },
      { en: "Shashi teaches me", mr: "शशी मला शिकवतात.", roman: "shashI malA shikavatAt.", hint: "" },
      { en: "Where is your class?", mr: "तुझा क्लास कुठे आहे?", roman: "tujha klas kuthe aahe?", hint: "" },
      { en: "My class is 5 minutes from railway station", mr: "माझा क्लास रेल्वे स्टेशन पासून पाच मिनिटांवर आहे.", roman: "maajhA klAs relve sTeshan pAsUn pAch miniTAMvar aahe.", hint: "" },
      { en: "Is it every day?", mr: "तो रोज असतो का?", roman: "to roj asato kA?", hint: "" },
      { en: "No. On alternate days. 5 to 6 in evening", mr: "नाही. एकाडएक दिवस असतो. संध्याकाळी पाच ते सहा.", roman: "nAhI. ekADaek divas asato. saMdhyAkALI pAch te sahA.", hint: "" },
      { en: "How much is fee?", mr: "फी किती आहे?", roman: "phI kitI aahe?", hint: "" },
      { en: "500 Rs. Per month", mr: "प्रत्येक महिन्याचे पाचशे रुपये.", roman: "pratyek mahinyAche pAchashe rupaye.", hint: "" },
      { en: "Only 10 in one batch", mr: "फक्त दहा.", roman: "phakta dahA.", hint: "" },
      { en: "Can I join too?", mr: "मी पण क्लास लावू शकतो का?", roman: "mI paN klAs lAvU shakato kA?", hint: "" },
      { en: "New batch will start soon", mr: "पण नवीन बॅच लवकरच सुरू होते आहे.", roman: "paN navIn b~ach lavakarach surU hote aahe.", hint: "" },
      { en: "Great. Let's go!", mr: "छान. चल निघूया!", roman: "ChAn. chal nighUyA!", hint: "" },
      { en: "He/She is hungry", mr: "त्याला/तीला भूक लागली आहे", roman: "tyAlA/tIlA bhUk laagalI Ahe", hint: "" },
      { en: "They are hungry", mr: "त्यांना भूक लागली आहे", roman: "tyAMnA bhUk laagalI Ahe", hint: "" },
      { en: "I am not hungry", mr: "मला भूक नाही लागली आहे", roman: "malA bhUk nAhI laagalI Ahe", hint: "" },
      { en: "I am not thirsty", mr: "मला तहान नाही लागली आहे", roman: "malA tahAn nAhI lAgalI Ahe", hint: "" },
      { en: "Favorite sport", mr: "सर्वांत आवडता खेळ", roman: "sarvAMt AvaDatA kheL", hint: "" },
      { en: "Favorite song", mr: "सर्वांत आवडते गाणे", roman: "sarvAMt AvaDate gANe", hint: "" },
      { en: "What is your favorite car?", mr: "तुझी आवडती गाडी कुठली", roman: "tujhI AvaDatI gADI kuThalI", hint: "" },
      { en: "I am waiting for Kaushik", mr: "मी कौशिकची वाट बघतोय", roman: "mI kaushikachI vAT baghatoy", hint: "" },
      { en: "He is waiting for me", mr: "तो माझी वाट बघतोय", roman: "to mAjhI vAT baghatoy", hint: "" },
      { en: "I waited for Kaushik", mr: "मी कौशिकची वाट बघितली", roman: "mI kaushikachI vAT baghitalI", hint: "" },
      { en: "She will wait for you", mr: "ती तुझी वाट बघेल", roman: "tI tujhI vAT baghel", hint: "" },
      { en: "Is it ok if I sit here?", mr: "मी इथे बसलो तर चालेल का?", roman: "mI ithe basalo tar chAlel kA?", hint: "" },
      { en: "Is it ok if he sits here?", mr: "तो इथे बसला तर चालेल का?", roman: "to ithe basala tar chAlel kA?", hint: "" },
      { en: "Is it ok if they play on terrace?", mr: "ते गच्चीवर खेळले तर चालेल का?", roman: "te gachchIvar kheLale tar chAlel kA?", hint: "" },
      { en: "Is mobile working?", mr: "मोबाईल चालू आहे का?", roman: "mobAIl chAlU Ahe kA?", hint: "" },
      { en: "Yes, mobile is working", mr: "हो, मोबाईल चालू/सुरू आहे", roman: "ho, mobAIl chAlU/surU Ahe", hint: "" },
      { en: "Was watch working?", mr: "घड्याळ चालू/सुरू होते का?", roman: "ghaDyAL chAlU/surU hote kA?", hint: "" },
      { en: "Is mobile not working?", mr: "मोबाईल बंद आहे का?", roman: "mobAIl baMd Ahe kA?", hint: "" },
      { en: "Yes, mobile is not working", mr: "मोबाईल बंद आहे", roman: "mobAIl baMd Ahe", hint: "" },
      { en: "I am wearing T-shirt", mr: "मी टीशर्ट घातला आहे", roman: "mI TIsharT ghAtalA Ahe", hint: "" },
      { en: "He had worn suit when he met me", mr: "तो मला भेटलो तेव्हा त्याने सूट घातला होता", roman: "to malA bheTalo tevhA tyAne sUT ghAtalA hotA", hint: "" },
      { en: "Wait, I am wearing tie (in act)", mr: "एक मिनिट थांब. मी टाय घालतो आहे", roman: "ek miniT thAMb. mI TAy ghAlato Ahe", hint: "" },
      { en: "I wish he goes to school", mr: "माझी अशी इच्छा आहे की तो शाळेत गेला पाहिजे", roman: "mAjhI ashI ichChA Ahe kI to shALet gelA pAhije", hint: "" },
      { en: "He wishes Kaushik wins", mr: "त्याची अशी इच्छा आहे की कौशिक जिंको", roman: "tyAchI ashI ichChA Ahe kI kaushik jiMko", hint: "" },
      { en: "I believe you", mr: "माझा तुझ्यावर विश्वास आहे", roman: "mAjhA tujhyAvar vishvAs Ahe", hint: "" },
      { en: "He believes Kaushik", mr: "त्याचा कौशिकवर विश्वास आहे", roman: "tyAchA kaushikavar vishvAs Ahe", hint: "" },
      { en: "She believed me", mr: "तीचा माझ्यावर विश्वास होता", roman: "tIchA mAjhyAvar vishvAs hotA", hint: "" },
      { en: "Will you please believe me?", mr: "तू कृपया माझ्यावर विश्वास ठेवशील का?", roman: "tU kRupayA mAjhyAvar vishvAs ThevashIl kA?", hint: "" },
      { en: "I go by bus", mr: "मी बसने जातो", roman: "mI basane jAto", hint: "" },
      { en: "He goes by plane", mr: "तो विमानाने जातो", roman: "to vimAnAne jAto", hint: "" },
      { en: "He walks to office / He goes by foot", mr: "तो चालत जातो", roman: "to chAlat jAto", hint: "" },
      { en: "I have a car", mr: "माझ्याकडे गाडी आहे", roman: "mAjhyAkaDe gADI Ahe", hint: "" },
      { en: "He has two brothers", mr: "त्याला दोन भाऊ आहेत", roman: "tyAlA don bhAU Ahet", hint: "" },
      { en: "I did not have time", mr: "माझ्याकडे/मला वेळ नव्हता", roman: "mAjhyAkaDe/malA veL navhatA", hint: "" },
      { en: "I do not have time", mr: "माझ्याकडे/मला वेळ नाही", roman: "mAjhyAkaDe/malA veL nAhI", hint: "" },
      { en: "What have you prepared for lunch today?", mr: "आज जेवायला काय केले आहे", roman: "Aj jevAyalA kAy kele Ahe", hint: "" },
      { en: "What have you prepared for lunch today?", mr: "आज काय स्वयंपाक केला आहे", roman: "Aj kAy svayaMpAk kelA Ahe", hint: "" },
      { en: "What have you prepared for breakfast today?", mr: "आज नाष्त्याला काय केले आहे", roman: "Aj nAShtyAlA kAy kele Ahe", hint: "" },
      { en: "I cleaned house", mr: "मी घराची साफसफाई केली", roman: "mI gharAchI sAphasaphAI kelI", hint: "" },
      { en: "We burst crackers", mr: "आम्ही फटाके फोडले / वाजवले", roman: "AmhI phaTAke phoDale / vAjavale", hint: "" },
      { en: "I can't draw Rangoli", mr: "मला रांगोळी काढता येत नाही", roman: "malA rAMgoLI kADhatA yet nAhI", hint: "" },
      { en: "So I draw Rangoli of flowers", mr: "म्हणून मी फुलांची रांगोळी काढते", roman: "mhaNUn mI phulAMchI rAMgoLI kADhate", hint: "" },
      { en: "I went everywhere and ate mithai", mr: "मी सगळीकडे गेलो आणि मिठाई खाल्ली", roman: "mI sagaLIkaDe gelo ANi miThAI khAllI", hint: "" },
      { en: "Family members worship Ganpati and Lakshmi in the evening", mr: "घरचे लोक संध्याकाळी गणपती आणि लक्ष्मीची पूजा करतात", roman: "gharache lok sMdhyAkALI gaNapatI ANi lakShmIchI pUjA karatAt", hint: "" },
      { en: "I light the lantern and decorate house", mr: "मी कंदील लावतो आणि घर सजवतो", roman: "mI kMdIl lAvato ANi ghar sajavato", hint: "" },
      { en: "Crackers cause air and sound pollution", mr: "फटाक्यांमुळे वायू आणि ध्वनी प्रदूषण होते", roman: "phaTAkyAMmuLe vAyU ANi dhvanI pradUShaN hote", hint: "" },
      { en: "How many days have you taken leave?", mr: "तू किती दिवस सुट्टी घेतली आहेस?", roman: "tU kitI divas suTTI ghetalI Ahes?", hint: "" },
      { en: "I have taken leave for 7 days", mr: "मी सात दिवस सुट्टी घेतली आहे", roman: "mI sAt divas suTTI ghetalI Ahe", hint: "" },
      { en: "I am going to my hometown", mr: "मी गावाला जाणार आहे", roman: "mI gAvAlA jANAr Ahe", hint: "" },
      { en: "I am going by train", mr: "मी ट्रेनने जाणार आहे", roman: "mI Trenane jANAr Ahe", hint: "" },
      { en: "How much time does it take to reach hometown?", mr: "गावाला पोचायला किती वेळ लागतो?", roman: "gAvAlA pochAyalA kitI veL lAgato?", hint: "" },
      { en: "When will you be back?", mr: "तू कधी परत येणार आहेस?", roman: "tU kadhI parat yeNAr Ahes?", hint: "" },
      { en: "Let's have a lot of fun there", mr: "आपण तिकडे खूप मजा करूया", roman: "ApaN tikaDe khUp majA karUyA", hint: "" },
      { en: "We went to Khadki railway station for wall painting activity", mr: "आम्ही काल खडकी रेल्वे स्टेशनला गेलो", roman: "AmhI kAl khaDakI relve sTeshanalA gelo", hint: "" },
      { en: "We painted 2 drawings", mr: "आम्ही दोन चित्रं रंगवली", roman: "AmhI don chitrM raMgavalI", hint: "" },
      { en: "Will you like to join?", mr: "तुला join करायला आवडेल का?", roman: "tulA join karAyalA AvaDel kA?", hint: "" },
      { en: "I like to join", mr: "मला join करायला आवडतं", roman: "malA join karAyalA AvaDatM", hint: "" },
      { en: "There was a party in our office today", mr: "आज आमच्या ऑफिस मध्ये पार्टी झाली", roman: "Aj AmachyA office madhye pArTI jhAlI", hint: "" },
      { en: "We ate cake in party", mr: "आम्ही पार्टी मध्ये केक खाल्ला", roman: "AmhI pArTI madhye kek khAllA", hint: "" },
      { en: "Who brought the cake?", mr: "केक कोणी आणला", roman: "kek koNI ANalA", hint: "" },
      { en: "Do not disturb me", mr: "मला disturb करू नकोस", roman: "malA disturb karU nakos", hint: "" },
      { en: "When is the class in next week?", mr: "पुढच्या आठवड्यात क्लास कधी आहे?", roman: "puDhachyA AThavaDyAt klAs kadhI Ahe?", hint: "" },
      { en: "Roll the chapatis", mr: "पोली लाट", roman: "polI lAT", hint: "" },
      { en: "Grate the coconut", mr: "नारळ किसून घ्या", roman: "nAraL kisUn ghyA", hint: "" },
      { en: "Strain the tea", mr: "चहा गाळ", roman: "chahA gAL", hint: "" },
      { en: "Put the clothes to dry", mr: "कपडे वाळत घाला", roman: "kapaDe vALat ghAlA", hint: "" },
      { en: "Soak the clothes", mr: "कपडे भिजवा", roman: "kapaDe bhijavA", hint: "" },
      { en: "My earphone is tangled", mr: "माझा इयरफोन गुंतला आहे", roman: "mAjhA iyaraphon guMtalA Ahe", hint: "" },
      { en: "Untangle it", mr: "तो सोडवा", roman: "to soDavA", hint: "" },
      { en: "Put my phone to charge", mr: "माझा फोन चार्जीगला ठेवा", roman: "mAjhA phon chArjIgalA ThevA", hint: "" },
      { en: "My phone's battery is dead", mr: "माझा फोन चार्ज नाहिये", roman: "mAjhA phon chArj nAhiye", hint: "" },
      { en: "He ripped my bag", mr: "त्याने माझी बॅग फाडली", roman: "tyAne mAjhI b~ag phADalI", hint: "" },
      { en: "Throw it away", mr: "ते फेका", roman: "te phekA", hint: "" },
      { en: "Exams are nearing", mr: "परीक्षा जवळ आली आहे", roman: "parIkShA javaL AlI Ahe", hint: "" },
      { en: "I was stuck in the traffic", mr: "मी ट्रॅफिकमध्ये अडकलो होतो", roman: "mI Tr~aphikamadhye aDakalo hoto", hint: "" },
      { en: "I am in debt", mr: "मी कर्जात आहे", roman: "mI karjAt Ahe", hint: "" },
      { en: "Give me a hand", mr: "मला थोडी मदत करा", roman: "malA thoDI madat karA", hint: "" },
      { en: "Get on the bus", mr: "बसमध्ये चढ", roman: "basamadhye chaDh", hint: "" },
      { en: "Get off the bus", mr: "बसमधून उतर", roman: "basamadhUn utar", hint: "" },
      { en: "Come closer", mr: "जवळ ये", roman: "javaL ye", hint: "" },
      { en: "Keep going", mr: "पुढे जात रहा", roman: "puDhe jAt rahA", hint: "" },
      { en: "Cut down on sugar", mr: "कमी साखर खा", roman: "kamI sAkhar khA", hint: "" },
      { en: "I have a runny nose", mr: "मला सर्दी झाली आहे", roman: "malA sardI jhAlI Ahe", hint: "" },
      { en: "How did it go?", mr: "कसं झालं", roman: "kasaM jhAlM", hint: "" },
      { en: "It went well", mr: "चांगलं झालं", roman: "chAMgalM jhAlM", hint: "" },
      { en: "Close the lid", mr: "झाकण बंद करा", roman: "jhAkaN bMd karA", hint: "" },
      { en: "Everyone talks about corona virus these days", mr: "आजकाल प्रत्येकजण कोरोना विषाणू बद्दल बोलतो", roman: "AjakAl pratyekajaN koronA viShANU baddal bolato", hint: "" },
      { en: "Because of the virus, I can't go out", mr: "विषाणूमुळे, मी माझ्या मित्रांबरोबर बाहेर जाऊ शकत नाही", roman: "viShANUmuLe, mI mAjhyA mitrAMbarobar bAher jAU shakat nAhI", hint: "" },
      { en: "Instead of meeting friends, stay home and relax", mr: "तुमच्या मित्रांना भेटण्याऐवजी तुम्ही घरी राहून आराम करू शकता", roman: "tumachyA mitrAMnA bheTaNyAaivajI tumhI gharI rAhUn ArAm karU shakatA", hint: "" },
      { en: "Learn Marathi or read your favorite books", mr: "मराठी शिका किंवा आपली आवडती पुस्तके वाचा", roman: "marAThI shikA kiMvA ApalI AvaDatI pustake vAchA", hint: "" },
      { en: "These are Marathi online lessons. They're free", mr: "हे मराठी ऑनलाइन धडे आहेत. ते विनामूल्य आहेत", roman: "he marAThI ~onalAin dhaDe Ahet. te vinAmUly Ahet", hint: "" },
      { en: "The guavas are near the book", mr: "पेरू पुस्तकाजवळ आहेत", roman: "perU pustakAjavaL Ahet", hint: "" },
      { en: "The cabbage and onion are in the pot", mr: "कोबी आणि कांदा भांड्यात आहे", roman: "kobI ANi kAMdA bhAMDyAt Ahe", hint: "" },
      { en: "The tea is on the stove", mr: "चहा गॅसवर आहे", roman: "chahA g~asavar Ahe", hint: "" },
      { en: "After getting up I shower", mr: "उठल्यानंतर मी अंघोळ करते", roman: "uThalyAnMtar mI aMghoL karate", hint: "" },
      { en: "Long time since we met. Do you live near here?", mr: "आपल्याला भेटून बरेच दिवस झाले. तू जवळपास राहतोस का?", roman: "ApalyAlA bheTUn barech divas jhAle. tU javaLapAs rAhatos kA?", hint: "" },
      { en: "I live across the street", mr: "मी रस्त्याच्या पलिकडे राहतो", roman: "kharaMch. mI rastyAchyA palikaDe rAhato", hint: "" },
      { en: "I live in this area 200 meters from here", mr: "मी पण या भागातच राहते. इथून २०० मीटर अंतरावर", roman: "mI paN yA bhAgAtach rAhate. ithUn 200 mITar aMtarAvar", hint: "" },
      { en: "I just moved here", mr: "मी तर नुकताच इकडे राहायला आलो", roman: "mI tar nukatAch ikaDe rAhAyalA Alo", hint: "" },
      { en: "I don't go to work these days", mr: "आजकाल मी कामाला जात नाही", roman: "AjakAl mI kAmAlA jAt nAhI", hint: "" },
      { en: "Instead I work at home on the computer", mr: "त्याऐवजी मी घरी computerवर काम करते", roman: "tyAaivajI mI gharI computer var kAm karate", hint: "" },
      { en: "Sometimes I make breakfast for Rohan", mr: "कधीकधी मी रोहनसाठी नाश्ता बनवते", roman: "kadhIkadhI mI rohanasAThI nAshtA banavate", hint: "" },
      { en: "I need to go to the grocery store", mr: "मला किराणा दुकानात जायचं आहे", roman: "malA kirANA dukAnAt jAyachaM Ahe", hint: "" },
      { en: "Apply hand sanitizer when you leave", mr: "निघताना हॅन्ड सॅनिटायझर लाव", roman: "nighatAnA h~anD s~aniTAyajhar lAv", hint: "" },
      { en: "My native language is English", mr: "माझी मातृभाषा इंग्रजी आहे", roman: "mAjhI mAtRubhAShA iMgrajI Ahe", hint: "" },
      { en: "I speak American English", mr: "मी अमेरिकन इंग्रजी बोलते", roman: "mI amerikan iMgrajI bolate", hint: "" },
      { en: "I really like studying languages", mr: "मला भाषा शिकायला खूप आवडते", roman: "malA bhAShA shikAyalA khUp AvaDate", hint: "" },
      { en: "In high school, I learned French", mr: "हायस्कुलमध्ये मी फ्रेंच शिकले", roman: "hAyaskulamadhye mI phreMch shikale", hint: "" },
      { en: "I would like to teach English", mr: "मला इंग्रजी शिकवायला आवडेल", roman: "malA iMgrajI shikavAyalA AvaDel", hint: "" },
      { en: "I will tell you about my country Wales", mr: "तुम्हाला माझा देश – वेल्सबद्दल सांगीन", roman: "tumhAlA mAjhA desh – vels deshabaddal sAMgIn", hint: "" },
      { en: "Behind my house there is a large mountain", mr: "माझ्या घरामागे एक मोठा पर्वत आहे", roman: "mAjhyA gharAmAge ek moThA parvat Ahe", hint: "" },
      { en: "I live close to the sea", mr: "मी समुद्राजवळ राहते", roman: "mI samudrAjavaL rAhate", hint: "" },
      { en: "In front of my house you can see a castle", mr: "माझ्या घरासमोर आपण किल्ला पाहू शकता", roman: "mAjhyA gharAsamor ApaN killA pAhU shakatA", hint: "" },
      { en: "Once a boy goes to see a girl for marriage", mr: "एकदा एक मुलगा लग्नासाठी मुलगी बघायला जातो", roman: "ekadA ek mulagA lagnAsAThI mulagI baghAyalA jAto", hint: "" },
      { en: "Can you sing?", mr: "तुला गाता येते का?", roman: "tulA gAtA yete kA?", hint: "" },
      { en: "The gown has been put outside to dry", mr: "गाऊन बाहेर वाळत टाकला आहे", roman: "gAUn bAher vALat TAkalA Ahe", hint: "" },
      { en: "Ok let it dry", mr: "बर, वाळूदे", roman: "bar, vALUde", hint: "" },
      { en: "Then the girl gives him one hand full of sand", mr: "मुलगी त्याला एक मूठ वाळू आणून देते", roman: "mulagI tyAlA ek mUTh vALU ANUn dete", hint: "" },
      { en: "Social media has good and bad points", mr: "सोशल मीडियाचे चांगले व वाईट मुद्दे आहेत", roman: "soshal mIDiyAche chAMgale v vAIT mudde Ahet", hint: "" },
      { en: "You can make friends by using social media", mr: "आपण सोशल मीडिया वापरून मित्र बनवू शकतो", roman: "ApaN soshal mIDiyA vAparUn mitr banavU shakato", hint: "" },
      { en: "Actually I made friends online recently", mr: "खरं तर माझे नुकतेच काही नवीन मित्र बनले आहेत", roman: "kharM tar mAjhe nukatech kAhI navIn mitr banale Ahet", hint: "" },
      { en: "The amount of information is too much", mr: "माहितीचे प्रमाण खूप जास्त होते", roman: "mAhitIche pramAN khUp jAst hote", hint: "" },
      { en: "I have mixed feelings towards social media", mr: "सोशल मीडियाबद्दल माझ्या संमिश्र भावना आहेत", roman: "soshal mIDiyAbaddal mAjhyA sMmishr bhAvanA Ahet", hint: "" },
      { en: "For many years I was on Facebook", mr: "बऱ्याच वर्षांपासून मी फेसबुकवर होतो", roman: "bryAch varShAMpAsUn mI phesabukavar hoto", hint: "" },
      { en: "Therefore I also left", mr: "म्हणून मीसुद्धा फेसबुक सोडले", roman: "mhaNUn mIsuddhA phesabuk soDale", hint: "" },
      { en: "Now I only use linkedin", mr: "आता मी फक्त लिंक्डइन वापरतो", roman: "AtA mI phakt liMkDin vAparato", hint: "" },
      { en: "This I find sad", mr: "ह्याचे मला वाईट वाटते", roman: "hyAche malA vAIT vATate", hint: "" },
      { en: "I use social media everyday", mr: "मी सोशल मीडिया दररोज वापरते", roman: "mI soshal mIDiyA dararoj vAparate", hint: "" },
      { en: "Now I use Whatsapp, Facebook, YouTube daily", mr: "आजकाल मी Whatsapp, Facebook, YouTube दररोज वापरते", roman: "AjakAl mI Whatsapp Facebook YouTube dararoj vAparate", hint: "" },
      { en: "I am enjoying learning Marathi through social media", mr: "मी सोशल मीडियातून मराठी शिकायला मला खूप मजा येतेय", roman: "mI soshal mIDiyAtUn marAThI shikAyalA malA khUp majA yetey", hint: "" },
      { en: "Social media can be so addictive", mr: "सोशल मीडिया व्यसन लागू शकते", roman: "soshal mIDiyA vyasan lAgU shakate", hint: "" },
      { en: "Social Media is a bad habit for many people", mr: "बर्‍याच लोकांसाठी सोशल मीडिया वाइट सवय आहे", roman: "baryAch lokAMsAThI soshal mIDiyA vAiT savay Ahe", hint: "" },
      { en: "Kaushik, why are you going to terrace?", mr: "कौशिक, तू गच्चीवर का जातोयस?", roman: "kaushik tU gachchIvar kA jAtoyas", hint: "" },
      { en: "I am going to watch the solar eclipse", mr: "मी सूर्यग्रहण बघायला जातो आहे", roman: "mI sUryagrahaN baghAyalA jAto Ahe", hint: "" },
      { en: "Solar eclipse should not be seen by naked eyes", mr: "सूर्यग्रहण नुसत्या डोळ्यांनी बघायचं नसतं असं ऐकलं आहे", roman: "sUryagrahaN nusatyA DoLyAMnI baghAyachM nasatM asM aikalM Ahe", hint: "" },
      { en: "Do you have special goggle to watch the eclipse?", mr: "तुझ्याकडे ग्रहण बघायचा खास चष्मा आहे का?", roman: "tujhyAkaDe grahaN baghAyachA khAs chaShmA Ahe kA", hint: "" },
      { en: "Yes, I have", mr: "हो माझ्याकडे आहे", roman: "ho mAjhyAkaDe Ahe", hint: "" },
      { en: "Because of moon coming between sun and earth, sun gets hidden", mr: "सूर्य आणि पृथ्वीच्या मध्ये चंद्र आल्यामुळे सूर्य झाकला जातो", roman: "sUry ANi pRuthvIchyA madhye chMdr AlyAmuLe sUry jhAkalA jAto", hint: "" },
      { en: "That is called eclipse", mr: "त्याला ग्रहण म्हणतात", roman: "tyAlA grahaN mhaNatAt", hint: "" },
      { en: "Lunar eclipse can be seen by naked eyes", mr: "चंद्रग्रहण सध्या डोळ्यांनी पाहता येतं", roman: "chMdragrahaN sadhyA DoLyAMnI pAhatA yetM", hint: "" },
      { en: "In Chinese culture, heavenly dog eats the sun", mr: "चिनी संस्कृतीमध्ये, आकाशातला कुत्रा सूर्याला खातो अशी कल्पना आहे", roman: "chinI sMskRutImadhye AkAshAtalA kutrA sUryAlA khAto ashI kalpanA Ahe", hint: "" },
      { en: "In India, Rahu and Ketu gulp the sun and moon", mr: "भारतात राहू आणि राक्षस सूर्य आणि चंद्राला गिळतात अशी कल्पना आहे", roman: "bhAratAt rAhU ANi rAkShas sUry ANi chMdrAlA giLatAt ashI kalpanA Ahe", hint: "" },
      { en: "Eclipse will start in five minutes", mr: "पाच मिनिटांनी सुरु होईल ग्रहण", roman: "pAch miniTAMnI suru hoIl grahaN", hint: "" },
      { en: "How are you feeling? New car!", mr: "कसं वाटलं तुम्हाला? नवीन गाडी!", roman: "kasM vATalM tumhAlA? navIn gADI", hint: "" },
      { en: "Very nice!", mr: "खूप खूप छान", roman: "khUp khUp ChAn", hint: "" },
      { en: "I wanted it on GudhiPadva itself", mr: "मला गुढीपाडव्याच्या दिवशीच हवं होतं", roman: "malA guDhIpADavyAchyA divashIch havM hotM", hint: "" },
      { en: "But I was shooting that time", mr: "पण त्यावेळी मी शूट करत होते", roman: "paN tyAveLI mI shUT karat hote", hint: "" },
      { en: "Then, is there a party after going home?", mr: "मग आज घरी गेल्यावर पार्टी?", roman: "mag Aj gharI gelyAvar pArTI", hint: "" },
      { en: "See you again", mr: "परत भेटू", roman: "parat bheTU", hint: "" },
      { en: "Their work is to not let our roadmap become bridge", mr: "त्यांचं काम काय आहे? आपला हा roadmap bridge बनू द्यायचा नाही", roman: "tyAMchM kAm kAy Ahe? ApalA hA roadmap brij banU dyAyachA nAhI", hint: "" },
      { en: "Our work is to make this roadmap", mr: "आपलं काम काय आहे? हा roadmap बनवायचा", roman: "ApalM kAm kAy Ahe? hA roadmap banavAyachA", hint: "" },
      { en: "We can build a friendship with him", mr: "त्याच्यासोबत मैत्री होऊ शकते", roman: "tyAchyAsobat maitrI hoU shakate", hint: "" },
      { en: "I hope I have managed to surprise you this time", mr: "मला असं वाटतं की मी तुला ह्यावेळी surprise द्यायला जमलं एकदाचं!", roman: "malA asM vATatM kI mI tulA hyAveLI surprise dyAyalA jamalM ekadAchM", hint: "" },
      { en: "I am so lucky to have you in my life", mr: "माझ्या आयुष्यात तू असण्यामुळे मी खूप नशीबवान आहे", roman: "mAjhyA AyuShyAt tU asaNyAmuLe mI khUp nashIbavAn Ahe", hint: "" },
      { en: "You are somebody who changed my life", mr: "तू अशी व्यक्ती आहेस जिने माझं आयुष्य बदलून टाकलं", roman: "tU ashI vyaktI Ahes jine mAjhM AyuShy badalUn TAkalM", hint: "" },
      { en: "I had learned horse riding first time 10 years ago", mr: "हॉर्स रायडींग मी पहिल्यांदा दहा वर्षांपूर्वी शिकलो होतो", roman: "Horse riding mI pahilyAMdA dahA varShAMpUrvI shikalo hoto", hint: "" },
      { en: "I had learned in a jungle which is after Thane", mr: "मी ठाण्याच्या पुढे एका जंगलात शिकलो होतो", roman: "mI ThANyAchyA puDhe ekA jMgalAt shikalo hoto", hint: "" },
      { en: "And that horse was very young", mr: "आणि तो अगदी तरुण घोडा होता", roman: "ANi to agadI taruN ghoDA hotA", hint: "" },
      { en: "On that day he did not want to let anybody sit on him", mr: "त्याला त्या दिवशी कोणालाही स्वतःवर बसवायचं नव्हतं", roman: "tyAlA tyA divashI koNAlAhI svatHvar basavAyachM navhatM", hint: "" },
      { en: "For nearly 15 minutes he took me deep within the jungle", mr: "तो मला साधारणतः पंधरा मिनिटांकरता जंगलाच्या आत कुठेतरी घेऊन गेला", roman: "to malA sAdhAraNatH pandhara miniTAMkaratA jMgalAchyA At kuThetarI gheUn gelA", hint: "" },
      { en: "That day I felt, I am gone (dead)", mr: "त्यादिवशी मला वाटलं मी गेलो", roman: "tyAdivashI malA vATalM mI gelo", hint: "" },
      { en: "I like those poor lenient horses", mr: "ते बिचारे खूपच आवडतात मला", roman: "te bichAre khUpach AvaDatAt malA", hint: "" },
      { en: "Now after 2-3 months I will get call for what I was calling for", mr: "आता अजून काहीतरी दोन तीन महिन्यांनंतर ज्या आज गोष्टीसाठी मी कॉल करत होतो ते कॉल येतील मला", roman: "AtA ajUn kAhItarI don tIn mahinyAMnMtar jyA Aj goShTIsAThI mI k~ol karat hoto te k~ol yetIl malA", hint: "" },
      { en: "I got a hint", mr: "मला थोडं hint आलीये", roman: "malA thoDM hint AlIye", hint: "" },
      { en: "These are steps in my life", mr: "तर माझ्या ह्याच्यात lifeमध्ये ते पायऱ्या आहेत", roman: "tar mAjhyA hyAchyAt lifemadhye te pAyryA Ahet", hint: "" },
      { en: "I will not get a jump. And I don't want it either", mr: "मला कधी jump नाही मिळणार. आणि मला ती हवी पण नाहीये की", roman: "malA kadhI jump nAhI miLaNAr. ANi malA tI havI paN nAhIye kI", hint: "" },
      { en: "So I am enjoying", mr: "म्हणून मी मस्त मजे घेत घेत", roman: "mhaNUn mI mast maje ghet ghet", hint: "" },
      { en: "Comes from Amaravati and grabs the trophy", mr: "कुठे ते अमरावतीवरून येऊन एक trophy घेऊन जातो", roman: "kuThe te amarAvatIvarUn yeUn ek trofy gheUn jAto", hint: "" },
      { en: "You should appreciate it", mr: "त्याला तुम्ही appreciate करायला पाहिजे जाताना", roman: "tyAlA tumhI appreciate karAyalA pAhije jAtAnA", hint: "" },
      { en: "I had a bond with Abdul. I had a fight with MC once", mr: "अब्दुल सोबत माझा bond होता. MC सोबत तर माझी fight ही झाली होती एकदा", roman: "abdul sobat mAjhA bond hotA. MC sobat tar mAjhI fight hI jhAlI hotI ekadA", hint: "" },
      { en: "So we started friendship", mr: "तर आम्ही मैत्री केली", roman: "tar AmhI maitrI kelI", hint: "" },
      { en: "I am talking with you. Can you hear?", mr: "मी तुझ्याशी बोलतो आहे. तुला ऐकू येतंय का?", roman: "mI tujhyAshI bolato Ahe. tulA aikU yetMy kA", hint: "" },
      { en: "Why do you think I can't hear? I have not plugged my ears", mr: "ऐकू न यायला काय झालं? कानात बोळे नाही घातले मी", roman: "aikU n yAyalA kAy jhAlM? kAnAt boLe nAhI ghAtale mI", hint: "" },
      { en: "I am busy", mr: "मी कामात आहे. बिझी आहे", roman: "mI kAmAt Ahe. bijhI Ahe", hint: "" },
      { en: "You are busy. Am I sitting idle?", mr: "तू बिझी आणि मी फुकट बसलो आहे का?", roman: "tU bijhI ANi mI phukaT basalo Ahe kA", hint: "" },
      { en: "I do all the work. But you do not value me", mr: "सगळी कामं मी करतो पण तुला माझी किंमतच नाहीये", roman: "sagaLI kAmM mI karato paN tulA mAjhI kiMmatach nAhIye", hint: "" },
      { en: "You are a fool. You don't have an iota of intelligence", mr: "तू मूर्ख/बावळट आहेस. तुला काडीची अक्कल नाही", roman: "tU mUrkh/bAvaLaT Ahes. tulA kADIchI akkal nAhI", hint: "" },
      { en: "Don't talk too much. Keep quiet", mr: "जास्त बोलू नकोस. गप्प बस", roman: "jAst bolU nakos. gapp bas", hint: "" },
      { en: "Keep your mouth shut", mr: "थोबाड बंद ठेव तुझं", roman: "thobAD bMd Thev tujhM", hint: "" },
      { en: "Did you do the task I told you yesterday?", mr: "काल सांगितलेलं काम केलंस का?", roman: "kAl sAMgitalelM kAm kelMs kA", hint: "" },
      { en: "I will do whenever its possible for me", mr: "जमेल तेव्हा करीन काम", roman: "jamel tevhA karIn kAm", hint: "" },
      { en: "Do it fast. It will be a great favour on me", mr: "लवकर कर. माझ्यावर उपकार कर", roman: "lavakar kar. mAjhyAvar upakAr kar", hint: "" },
      { en: "Cryptography means?", mr: "\"Cryptography\" म्हणजे काय", roman: "\"Cryptography\" mhaNaje kAy", hint: "" }
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
    ,
      { en: "Call someone", mr: "कोणाला तरी बोलव", roman: "koNAlA tarI bolav", hint: "" },
      { en: "Call anyone", mr: "कोणालाही बोलव", roman: "koNAlAhI bolav", hint: "" },
      { en: "I reached there somehow", mr: "मी तिकडे कसातरी पोचलो", roman: "mI tikaDe kasAtarI pochalo", hint: "" },
      { en: "I will reach there anyhow", mr: "मी तिकडे कसाही पोचेन", roman: "mI tikaDe kasAhI pochen", hint: "" },
      { en: "He has gone somewhere", mr: "तो सकाळपासून कुठेतरी गेला आहे", roman: "to sakALapAsUn kuThetarI gelA Ahe", hint: "" },
      { en: "He is not ready to go anywhere", mr: "तो कुठेही जायला तयार नाही", roman: "to kuThehI jAyalA tayAr nAhI", hint: "" },
      { en: "I told him, still he ate it", mr: "मी त्याला सांगितले तरी त्याने हे खाल्ले", roman: "mI tyAlA sAMgitale tarI tyAne he khAlle", hint: "" },
      { en: "At least he came", mr: "तो तरी आला", roman: "to tarI AlA", hint: "" },
      { en: "Finish work at least by tomorrow", mr: "उद्यापर्यंत तरी काम संपव", roman: "udyAparyMt tarI kAm saMpav", hint: "" },
      { en: "You should have told me at least", mr: "तू मला तरी सांगायला हवे होतेस", roman: "tU malA tarI saMgAyalA have hotes", hint: "" },
      { en: "I will also come", mr: "मीही येईन", roman: "mIhI yeIn", hint: "" },
      { en: "This program is tomorrow also", mr: "हा कार्यक्रम उद्याही आहे", roman: "hA kAryakram udyAhI Ahe", hint: "" },
      { en: "He did not even tell it to me", mr: "त्याने मला हे सांगितलेही नाही", roman: "tyAne malA he sAMgitalehI nAhI", hint: "" },
      { en: "Everybody / Everyone", mr: "प्रत्येक जण", roman: "pratyek jaN", hint: "" },
      { en: "Every time", mr: "प्रत्येक वेळी", roman: "pratyek veLI", hint: "" },
      { en: "Everywhere", mr: "प्रत्येक ठिकाणी / सगळीकडे / सर्वत्र", roman: "pratyek ThikANI / sagaLIkaDe / sarvatr", hint: "" },
      { en: "Everything", mr: "प्रत्येक गोष्ट", roman: "pratyek goShT", hint: "" }
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
    ,
      { en: "Day after tomorrow", mr: "परवा", roman: "paravA", hint: "" },
      { en: "Afternoon", mr: "दुपार", roman: "dupAr", hint: "" },
      { en: "at Morning", mr: "सकाळी", roman: "sakALI", hint: "" },
      { en: "at afternoon", mr: "दुपारी", roman: "dupArI", hint: "" },
      { en: "at evening", mr: "संध्याकाळी", roman: "saMdhyAkALI", hint: "" },
      { en: "when", mr: "कधी / केव्हा", roman: "kadhI / kevhA", hint: "" },
      { en: "Now", mr: "आत्ता", roman: "AttA", hint: "" },
      { en: "Nowadays", mr: "हल्ली / सध्या", roman: "hallI / sadhyA", hint: "" },
      { en: "Everyday", mr: "रोज / दररोज", roman: "roj / dararoj", hint: "" },
      { en: "Day", mr: "दिवस", roman: "divas", hint: "" },
      { en: "at Day", mr: "दिवसा", roman: "divasA", hint: "" },
      { en: "at night", mr: "रात्री", roman: "rAtrI", hint: "" },
      { en: "Month", mr: "महिना", roman: "mahinA", hint: "" },
      { en: "Year", mr: "वर्ष", roman: "varSha", hint: "" },
      { en: "I am in office now", mr: "मी आत्ता ऑफिसमध्ये आहे", roman: "mI AttA ophisamadhye Ahe", hint: "" },
      { en: "We play cricket every day", mr: "आम्ही रोज क्रिकेट खेळतो", roman: "AmhI roj krikeT kheLato", hint: "" },
      { en: "He comes back from school in the evening", mr: "तो संध्याकाळी शाळेतून परत येतो", roman: "to saMdhyAkALI shALetUn parat yeto", hint: "" },
      { en: "When will she dance?", mr: "ती कधी/केव्हा नाचेल?", roman: "tI kadhI/kevhA nAchel?", hint: "" },
      { en: "Meet me at 2 pm", mr: "मला दुपारी दोन वाजता भेट", roman: "malA dupArI don vajatA bheT", hint: "" },
      { en: "Meet me at 2 am", mr: "मला रात्री दोन वाजता भेट", roman: "malA rAtrI don vajatA bheT", hint: "" },
      { en: "We work from 10 am to 10 pm", mr: "आम्ही सकाळी 10 ते रात्री 10 काम करतो", roman: "AmhI sakALI 10 te rAtrI 10 kAm karato", hint: "" },
      { en: "January", mr: "जानेवारी", roman: "jAnevArI", hint: "" },
      { en: "February", mr: "फेब्रुवारी", roman: "phebruvArI", hint: "" },
      { en: "March", mr: "मार्च", roman: "mArch", hint: "" },
      { en: "April", mr: "एप्रिल", roman: "epril", hint: "" },
      { en: "May", mr: "मे", roman: "me", hint: "" },
      { en: "June", mr: "जून", roman: "jUn", hint: "" },
      { en: "July", mr: "जुलै", roman: "julai", hint: "" },
      { en: "August", mr: "ऑगस्ट", roman: "ogasT", hint: "" },
      { en: "September", mr: "सप्टेंबर", roman: "sapTeMbar", hint: "" },
      { en: "October", mr: "ऑक्टोबर", roman: "okTobar", hint: "" },
      { en: "November", mr: "नोव्हेंबर", roman: "novheMbar", hint: "" },
      { en: "December", mr: "डिसेंबर", roman: "DiseMbar", hint: "" },
      { en: "Sunday", mr: "रविवार", roman: "ravivAr", hint: "" },
      { en: "Tuesday", mr: "मंगळवार", roman: "maMgaLavAr", hint: "" },
      { en: "Wednesday", mr: "बुधवार", roman: "budhavAr", hint: "" },
      { en: "Thursday", mr: "गुरुवार", roman: "guruvAr", hint: "" },
      { en: "Friday", mr: "शुक्रवार", roman: "shukravAr", hint: "" },
      { en: "Saturday", mr: "शनिवार", roman: "shanivAr", hint: "" },
      { en: "What date is it today?", mr: "आज काय तारीख आहे?", roman: "Aj kAy tArIkh Ahe?", hint: "" },
      { en: "It was 1st July yesterday", mr: "काल १ जुलै होती", roman: "kAl 1 julai hotI", hint: "" },
      { en: "It is 2nd July today", mr: "आज दोन जुलै आहे", roman: "Aj don julai Ahe", hint: "" },
      { en: "Celebrating women's day started on 28th Feb 1909", mr: "महिला दिन साजरा करण्याची सुरुवात 28 फेब्रुवारी 1909 साली झाली होती", roman: "mahilA din sAjarA karaNyAchI suruvAt 28 phebruvArI 1909 sAlI jhAlI hotI", hint: "" },
      { en: "8th March was declared as International Women's day", mr: "आणि त्या सुचनेनुसार 8 मार्च हा दिवस जागतिक महिला दिन म्हणून घोषित करण्यात आला", roman: "ANi tyA suchanenusAr 8 mArch hA divas jAgatik mahilA din mhaNUn ghoShit karaNyAt AlA", hint: "" },
      { en: "Its main purpose is to give equal rights and honour women", mr: "समाजातील महिलांना समान अधिकार देणे आणि सन्मान करणे हा त्याचा मुख्य उद्देश आहे", roman: "samAjAtIl mahilAMnA samAn adhikAr deNe ANi sanmAn karaNe hA tyAchA mukhy uddesh Ahe", hint: "" },
      { en: "Women have great contribution from home to country development", mr: "आपल्या घरापासून ते देशाच्या विकासामध्येही महिलांचे मोठे योगदान आहे", roman: "ApalyA gharApAsUn te deshAchyA vikAsAmadhyehI mahilAMche moThe yogadAn Ahe", hint: "" },
      { en: "Every woman's place in our life is special", mr: "प्रत्येक 'ती'चं आपल्या आयुष्यातील स्थान अतिशय महत्त्वाचे-खास आहे", roman: "pratyek tI chM ApalyA AyuShyAtIl sthAn atishay mahattvAche-khAs Ahe", hint: "" },
      { en: "If you cannot meet in person, send a nice message", mr: "त्यांना मेसेजद्वारे छानसा संदेश पाठवा", roman: "tyAMnA mesejadvAre ChAnasA sMdesh pAThavA", hint: "" }
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
    ,
      { en: "Swear word (singular)", mr: "शिवी", roman: "shivI", hint: "" },
      { en: "Swear words (plural)", mr: "शिव्या", roman: "shivyA", hint: "" },
      { en: "To curse / To abuse", mr: "शिवी/शिव्या देणे", roman: "shivI/shivyA deNe", hint: "" },
      { en: "To curse / To abuse", mr: "शिविगाळ करणे", roman: "shivigAL karaNe", hint: "" }
    ]
  }
};

const DICTIONARY = {
  greetings: {
    name: "Greetings & Basics",
    words: [
    { en: "This (m.)", mr: "हा", roman: "hA" },
    { en: "This (f.)", mr: "ही", roman: "hI" },
    { en: "This (n.)", mr: "हे", roman: "he" },
    { en: "This is a horse", mr: "हा घोडा आहे", roman: "hA ghoDA Ahe" },
    { en: "This is an ant", mr: "ही मुंगी आहे", roman: "hI muMgI Ahe" },
    { en: "He / That (male) / This (male)", mr: "तो / हा", roman: "to" },
    { en: "She / That (female) / This (female)", mr: "ती / ही", roman: "te" },
    { en: "It / That (neuter) / This (neuter)", mr: "ते / हे", roman: "te" },
    { en: "He / That (m.) / This (m.)", mr: "तो / तो / हा", roman: "lA" },
    { en: "She / That (f.) / This (f.)", mr: "ती / ती / ही", roman: "lI" },
    { en: "It / That (n.) / This (n.)", mr: "ते / ते / हे", roman: "le" },
    { en: "behind", mr: "मागे", roman: "mAge" },
    { en: "To write लिहिणे (lihiNe)", mr: "लिहा", roman: "lihA" },
    { en: "his", mr: "त्याचा-त्याची-त्याचे-त्याचे-त्याच्या-त्याची", roman: "tyAchA-tyAchI-tyAche-tyAche-tyAchyA-tyAchI" },
    { en: "which", mr: "जो-जी-जे-जे-ज्या-जी", roman: "jo-jI-je-je-jyA-jI" },
    { en: "Kaushik used to eat mango", mr: "कौशिक आंबा खात असे", roman: "kaushik AMbA khAt ase" },
    { en: "Kaushik, Guru, sundar used to meet every day", mr: "कौशिक,गुरू,सुंदर रोज भेटत असत", roman: "kaushik,gurU,suMdar roj bheTat asat" },
    { en: "Kaushik used to eat mango", mr: "कौशिक आंबा खाई", roman: "kaushik AMbA khAI" },
    { en: "Kaushik used to see", mr: "कौशिक बघे/बघी", roman: "kaushik baghe/baghI" },
    { en: "Kaushik used to do", mr: "कौशिक करे/करी", roman: "kaushik kare/karI" },
    { en: "He told about his coming to school", mr: "तो शाळेत आल्याचे त्याने मला सांगितले", roman: "to shALet AlyAche tyAne malA sAMgitale" },
    { en: "I don't remember she having said something", mr: "ती असे काही बोलली असल्याचे मला आठवत नाही", roman: "tI ase kAhI bolalI asalyAche malA AThavat nAhI" },
    { en: "while I speak", mr: "बोलताना", roman: "bolatAnA" },
    { en: "while I do", mr: "करताना", roman: "karatAnA" },
    { en: "while I dance", mr: "नाचताना", roman: "nAchatAnA" },
    { en: "while speaking", mr: "बोलत असताना", roman: "bolat asatAnA" },
    { en: "while doing", mr: "करत असताना", roman: "karat asatAnA" },
    { en: "while dancing", mr: "नाचत असताना", roman: "nAchat asatAnA" },
    { en: "Come to see this photo", mr: "फोटो बघायला ये", roman: "phoTo baghAyalA ye" },
    { en: "Come to see this photo", mr: "फोटो बघण्यास ये", roman: "phoTo baghaNyAs ye" },
    { en: "Smoking is prohibited", mr: "धूम्रपान करण्यास मनाई आहे", roman: "dhUmrapAn karaNyAs manAI Ahe" },
    { en: "Your name is known to me", mr: "तुझे नाव मला माहीत आहे", roman: "tujhe nAv malA mAhIt Ahe" },
    { en: "She knows his address", mr: "तीला त्याचा पत्ता माहीत आहे", roman: "tIlA tyAchA pattA mAhIt Ahe" },
    { en: "She knew his address", mr: "तीला त्याचा पत्ता माहीत होता", roman: "tIlA tyAchA pattA mAhIt hotA" },
    { en: "Your name is not known to me", mr: "तुझे नाव मला माहीत नाही", roman: "tujhe nAv malA mAhIt nAhI" },
    { en: "She does not know his address", mr: "तीला त्याचा पत्ता माहीत नाही", roman: "tIlA tyAchA pattA mAhIt nAhI" },
    { en: "She did not know his address", mr: "तीला त्याचा पत्ता माहीत नव्हता", roman: "tIlA tyAchA pattA mAhIt navhatA" },
    { en: "Let him play", mr: "त्याला खेळू दे", roman: "tyAlA kheLU de" },
    { en: "You all, Let him play", mr: "त्याला खेळू द्या", roman: "tyAlA kheLU dyA" },
    { en: "Don't let him play", mr: "त्याला खेळू देऊ नकोस", roman: "tyAlA kheLU deU nakos" },
    { en: "Which fruit you want, show me that", mr: "तुला कोणते फळ हवे आहे ते मला दाखव", roman: "tulA koNate phaL have Ahe te malA dAkhav" },
    { en: "Which fruit you want, show me that", mr: "तुला जे फळ हवे आहे ते मला दाखव", roman: "tulA je phaL have Ahe te malA dAkhav" },
    { en: "Give it to him, who wants it", mr: "ज्याला हवे आहे त्याला दे", roman: "jyAlA have Ahe tyAlA de" },
    { en: "Whichever vegetables you want, you buy it", mr: "तुला जी जी भाजी हवी आहे ती ती तू विकत घे", roman: "tulA jI jI bhAjI havI Ahe tI tI tU vikat ghe" },
    { en: "Speak your name", mr: "आपले नाव सांगावे", roman: "Apale nAv sAMgAve" },
    { en: "Speak your names", mr: "आपली नावे सांगावी/सांगावीत", roman: "ApalI nAve sAMgAvI/sAMgAvIt" },
    { en: "I like to see Kaushik", mr: "मला कौशिकला बघायला आवडते", roman: "malA kaushikalA baghAyalA AvaDate" },
    { en: "Kaushik said that he would eat", mr: "कौशिक म्हणाला की तो खाईल", roman: "kaushik mhaNAlA kI to khAIl" },
    { en: "Would you please help me?", mr: "कृपया मला मदत कराल का?", roman: "kRupayA malA madat karAl kA?" },
    { en: "I would suggest you to take this medicine", mr: "मी हे औषध घेण्याचा सल्ला तुम्हाला देईन", roman: "mI he auShadh gheNyAchA sallA tumhAlA deIn" },
    { en: "He will not come to know this", mr: "त्याला हे समजणार/कळणार नाही", roman: "tyAlA he samajaNAr/kaLaNAr nAhI" },
    { en: "Peter misses his friend", mr: "पीटरला त्याच्या मित्रांची आठवण येते", roman: "pITaralA tyAchyA mitrAMchI AThavaN yete" },
    { en: "Kaushik wants to see Peter", mr: "कौशिकला पीटरला बघायचे आहे", roman: "kaushikalA pITar baghAyache Ahe" },
    { en: "Kaushik wants to see him", mr: "कौशिकला त्याला बघायचे आहे", roman: "kaushikalA tyAlA baghAyache Ahe" },
    { en: "Kaushik wants to see you", mr: "कौशिकला तुला बघायचे आहे", roman: "kaushikalA tulA baghAyache Ahe" },
    { en: "Kaushik wants students to practice more", mr: "कौशिकला विद्यार्थ्यांनी जास्त सराव करायला पाहिजे", roman: "kaushikalA vidyArthyAMnI jAst sarAv karAyalA pAhije" },
    { en: "Kaushik wanted students to practice more", mr: "कौशिकला विद्यार्थ्यांनी जास्त सराव करायला पाहिजे होता", roman: "kaushikalA vidyArthyAMnI jAst sarAv karAyalA pAhije hotA" },
    { en: "Students want Kaushik to talk slowly", mr: "विद्यार्थ्यांना कौशिकने हळू बोलायला पाहिजे", roman: "vidyArthyAMnA kaushikane haLU bolAyalA pAhije" },
    { en: "I am supposed to meet him tomorrow", mr: "मला त्याला उद्या भेटायचे आहे", roman: "malA tyAlA udyA bheTAyache Ahe" },
    { en: "We could not meet but next time we must meet", mr: "यावेळी भेटू शकलो नाही पण पुढच्या वेळी नक्की भेटायचं", roman: "yAveLI bheTU shakalo nAhI paN puDhachyA veLI nakkI bheTAyachM" },
    { en: "Do attend my uncle's wedding – chintu, motu, gotu", mr: "माझ्या काकाच्या लग्नाला यायचं हं – चिंटू, मोटू, गोटू", roman: "mAjhyA kAkAchyA lagnAlA yAyachM haM – chiMTU, moTU, goTU" },
    { en: "He agrees to this condition", mr: "त्याला ही अट मान्य आहे", roman: "tyAlA hI aT mAny Ahe" },
    { en: "Get that work done by him", mr: "त्याच्याकडून काम करून घे", roman: "tyAchyAkaDUn kAm karUn ghe" },
    { en: "Batsman hit every ball very hard", mr: "फलंदाजाने प्रत्येक बॉल फोडून काढला", roman: "phalaMdAjAne pratyek b~ol phoDUn kADhalA" },
    { en: "I just told him we drank liquor", mr: "मी त्यांना सांगून बसलो की आपण काल दारू प्यायली", roman: "mI tyAMnA sAMgUn basalo kI ApaN kAl dArU pyAyalI" },
    { en: "If we think of eating mango then", mr: "आंबा खायचा म्हटला तर", roman: "AMbA khAyachA mhaTalA tar" },
    { en: "Give him your information", mr: "त्याला तुझी महिती देऊन ठेव", roman: "tyAlA tujhI mahitI deUn Thev" },
    { en: "Oh my God! Who did this?", mr: "अरे देवा! हे कोणी केलं", roman: "are devaa! he koNI kelM" },
    { en: "Please give pen", mr: "जरा पेन देता का?", roman: "jarA pen detA kA?" },
    { en: "Please tell address", mr: "जरा पत्ता सांगता का?", roman: "jarA pattA sAMgatA kA?" },
    { en: "I make him say", mr: "मी त्याला बोलायला लावतो", roman: "mI tyAlA bolAyalA lAvato" },
    { en: "I will make him say", mr: "मी त्याला बोलायला लावीन", roman: "mI tyAlA bolAyalA lAvIn" },
    { en: "I made him say", mr: "मी त्याला बोलायला लावले", roman: "mI tyAlA bolAyalA lAvale" },
    { en: "I did this itself", mr: "मी हेच केले", roman: "mI hech kele" },
    { en: "What did his speech mean?", mr: "त्याच्या भाषणाचा अर्थ काय होता", roman: "tyAchyA bhAShaNAchA arth kAy hotA" },
    { en: "What does Sundar mean in Marathi?", mr: "मराठीमधे सुंदर म्हणजे काय", roman: "marAThImadhe suMdar mhaNaje kAy" },
    { en: "I meant to insult him", mr: "माझा उद्देश त्याचा अपमान करण्याचा होता", roman: "mAjhA uddesh tyAchA apamAn karaNyAchA hotA" },
    { en: "I had warned him, still he opened the box", mr: "मी त्याला इशारा दिला होता तरीही त्याने खोका उघडला", roman: "mI tyAlA ishArA dilA hotA tarIhI tyAne khokA ughaDalA" },
    { en: "He helped her still she insulted him", mr: "त्याने तिला मदत केली तरीही तीने त्याचा अपमान केला", roman: "tyAne tilA madat kelI tarIhI tIne tyAchA apamAn kelA" },
    { en: "As you wish, my lord", mr: "जशी आपली इच्छा, साहेब", roman: "jashI ApalI ichChA, sAheb" },
    { en: "He cheated me whereas I was helping him", mr: "त्याने मला फसवले उलट मी त्याला मदत करत होतो", roman: "tyAne malA phasavale ulaT mI tyAlA madat karat hoto" },
    { en: "Do this otherwise you will not win", mr: "हे कर नाहीतर तू जिंकणार नाहीस", roman: "he kar nAhItar tU jiMkaNAr nAhIs" },
    { en: "This is old video. I saw it. I am sharing today", mr: "हा जुना व्हिडिओ आहे. मी आत्ता बघितला. मी आज शेअर करत आहे", roman: "hA junA vhiDio Ahe. mI AttA baghitalA. mI Aj shear karat Ahe" },
    { en: "This is old video, yet I saw it so I am sharing today", mr: "हा जुना व्हिडिओ असला तरी मी आत्ता बघितल्यामुळे आज शेअर करत आहे", roman: "hA junA vhiDio asalA tarI mI AttA baghitalyAmuLe Aj shear karat Ahe" },
    { en: "This is old song. I heard it today", mr: "हे जुने गाणे आहे. मी आज ऐकले", roman: "he june gANe Ahe. mI Aj aikale" },
    { en: "Policeman was watching. He did not dare to run", mr: "पोलिस त्याला बारकाईने बघत होता. त्याने पळून जायचे धाडस केले नाही", roman: "polis tyAlA bArakAIne baghat hotA. tyAne paLUn jAyache dhADas kele nAhI" },
    { en: "As policeman was watching he did not dare", mr: "पोलिस त्याला बारकाईने बघत असल्यामुळे त्याने पळून जायचे धाडस केले नाही", roman: "polis tyAlA bArakAIne baghat asalyAmuLe tyAne paLUn jAyache dhADas kele nAhI" },
    { en: "I just told him we drank liquor", mr: "मी त्यांना सांगून बसलो/गेलो की आपण काल दारू प्यायली", roman: "mI tyAMnA sAMgUn basalo/gelo kI ApaN kAl dArU pyAyalI" },
    { en: "If we think of eating mango then..", mr: "आंबा खायचा म्हटला तर ..", roman: "AMbA khAyachA mhaTalA tar .." },
    { en: "I feel this way", mr: "मला असे वाटते", roman: "malA ase vATate" },
    { en: "I feel this", mr: "मला हे वाटते", roman: "malA he vATate" },
    { en: "Kaushik thinks he should go", mr: "कौशिकला असे वाटते की त्याने गेले पाहिजे", roman: "kaushikalA ase vATate kI tyAne gele pAhije" },
    { en: "Something fishy", mr: "पाणी मुरणे", roman: "pANI muraNe" },
    { en: "If possible, come to meet me", mr: "जमल्यास मला भेटायला ये", roman: "jamalyAs malA bheTAyalA ye" },
    { en: "What does this mean?", mr: "याचा अर्थ काय", roman: "yAchA arth kAy" },
    { en: "Someone called Kaushik has come", mr: "कौशिक म्हणून कोणीतरी आले", roman: "kaushik mhaNUn koNItarI aale" },
    { en: "Someone named Kaushik has come", mr: "कौशिक नावाचे कोणीतरी आले", roman: "kaushik nAvAche koNItarI aale" },
    { en: "You only complete this", mr: "तूच हे पूर्ण कर", roman: "tUch he pUrNa kar" },
    { en: "To chitchat", mr: "गप्पा मारणे gappA mAraNe", roman: "gappA mAralyA" },
    { en: "To hide", mr: "लपणे lapaNe", roman: "lapalo" },
    { en: "To hit", mr: "मारणे mAraNe", roman: "cheMDU mAralA" },
    { en: "Achieve", mr: "मिळवणे miLavaNe", roman: "yash miLavale" },
    { en: "Think", mr: "विचार करणे vichAr karaNe", roman: "tikaDe jANyAchA vichAr kelA" },
    { en: "I was thirsty", mr: "मला तहान लागली", roman: "malA tahAn lAgalI" },
    { en: "I am thirsty", mr: "मला तहान लागली आहे", roman: "malA tahAn lAgalI Ahe" },
    { en: "Fat / Thick", mr: "जाडा", roman: "jADA" },
    { en: "Thin", mr: "बारीक", roman: "bArIk" },
    { en: "I told him clearly", mr: "मी त्याला स्पष्टपणे सांगितले", roman: "mI tyAlA spaShTapaNe sAMgitale" },
    { en: "White", mr: "पांढरा", roman: "pAMDharA" },
    { en: "Hibiscus", mr: "जास्वंद", roman: "jAsvaMd" },
    { en: "Go uphill", mr: "त्या टेकडीवर चढा", roman: "tyA TekaDIvar chaDhA" },
    { en: "Write your name here", mr: "इथे तुमचे नाव लिहा", roman: "ithe tumache nAv lihA" },
    { en: "Which technology did you work on?", mr: "कुठल्या technology वर काम होतं?", roman: "kuThalyA technology var kAm hotM?" },
    { en: "Which technologies are here?", mr: "इथे कुठली technology आहे?", roman: "ithe kuThalI technology Ahe?" },
    { en: "Core java and spring, hibernate", mr: "Core Java आणि Spring, Hibernate", roman: "Core Java ANi Spring, Hibernate" },
    { en: "Great!! How much hike did you get?", mr: "मस्त! Hike किती मिळाली?", roman: "mast! Hike kitI miLAlI?" },
    { en: "How is this company?", mr: "ही company कशी वाटत्ये?", roman: "hI company kashi vATatye?" },
    { en: "It is near. At Rahul Garden City. Highway touch place", mr: "जवळच. राहूल Garden City मध्ये. High-way ला लागूनच आहे.", roman: "javaLach. rAhUl garden city madhye. High way lA lAgUnach Ahe." },
    { en: "I leave now. I have one meeting now.", mr: "चल मी निघतो. आता एक meeting आहे.", roman: "chal mI nighato. AtA ek meeting aahe" },
    { en: "Did you understand everything taught yesterday?", mr: "काल शिकवलेले सगळे कळले का?", roman: "kAl shikavalele sagaLe kaLale kA?" },
    { en: "Kaushik standup", mr: "कौशिक उभा रहा.", roman: "kaushik ubhA rahA." },
    { en: "Teacher, I am not doing anything", mr: "बाई मी काही नाही करते?", roman: "bAI mI kAhI nAhIkarate?" },
    { en: "This Raju is telling joke to Sanju", mr: "हा राजू, संजू ला जोक संगतोय?", roman: "hA rAjU saMjU lA jok saMgatoy?" },
    { en: "No madam. Sorry", mr: "नाही बाई. सॉरी.", roman: "nAhI bAI. sorry." },
    { en: "Hello", mr: "हॅलो", roman: "Hello" },
    { en: "I am Kaushik speaking", mr: "मी कौशिक बोलतोय", roman: "mI kaushik bolatoy" },
    { en: "Yes; please go ahead", mr: "हं बोला", roman: "haM bolA" },
    { en: "Is this number of Joshi?", mr: "हा जोश्यांचा नंबर आहे ना?", roman: "hA joshyAMchA naMbar Ahe nA" },
    { en: "Is this house of Joshi?", mr: "जोश्यांचं घर ना?", roman: "joshyAMchM ghar nA" },
    { en: "I wanted to speak with Vaibhav Joshi", mr: "मला वैभव जोशी यांच्याशी बोलायचं होतं", roman: "malA vaibhav joshI yAMchyAshI bolAyachaM hotaM" },
    { en: "Did you have any work with him?", mr: "काही काम होतं का?", roman: "kAhI kAm hotM kA?" },
    { en: "Yes, wanted to give him a message", mr: "हो त्यांना एक निरोप द्यायचा होता", roman: "ho tyAMnA ek nirop dyAyachA hotA" },
    { en: "Tell me. I will tell him once he is back", mr: "मला सांगा. मी त्यांना सांगतो आल्यावर.", roman: "malA sAMgA. mI tyAMnA sAMgato AlyAvar." },
    { en: "Ok. Tell him club meeting tomorrow at five", mr: "ठीक आहे. त्यांना सांगा उद्या क्लबची मीटिंग आहे. संध्याकाळी पाच वाजता.", roman: "ThIk Ahe. tyAMnA sAMgA udyA klabachI mITiMg Ahe. saMdhyAkALI pAch vAjatA." },
    { en: "Nothing special. Wanted to tell about meeting", mr: "विशेष काही नाही. मीटिंग बद्दल सांगायचं होतं.", roman: "visheSh kAhI nAhI. mITiMg baddal sAMgAyachaM hotaM." },
    { en: "I am Kaushik. Can I speak to Vaibhav?", mr: "मी कौशिक बोलतोय. वैभव आहेत का?", roman: "mI kaushik bolatoy. vaibhav Ahet kA?" },
    { en: "Vaibhav joshi", mr: "वैभव जोशी.", roman: "vaibhav joshI." },
    { en: "No. This not number of Joshis", mr: "नाही हा जोश्यांचा नंबर नाही.", roman: "nAhI hA joshyAMchA naMbar nAhI." },
    { en: "Ohh. Sorry", mr: "अरे. सॉरी", roman: "are. sorry." },
    { en: "I want to go to Hinjewadi. Where can I get bus?", mr: "मला हिंजवडीला जायचं आहे. बस कुठून मिळेल?", roman: "malA hiMjavaDIlA jAyachM Ahe. bas kuThUn miLel?" },
    { en: "Ok. Thanks", mr: "बरं. थॅंक्स", roman: "baraM. th~aMks" },
    { en: "Does Hinjewadi bus start from here?", mr: "हिंजवडीची बस इथुनच सुटते का?", roman: "hiMjavaDIchI bas ithunach suTate kA?" },
    { en: "Oh god. It is half an hour more. Does any other bus go to Hinjewadi?", mr: "अरे बापरे. अजून अर्धा तास आहे. दुसरी कुठली बस जाते का हिंजवडीला.", roman: "are bApare. ajUn ardhA tAs Ahe. dusarI kuThalI bas jAte kA hiMjavaDIlA." },
    { en: "No. That is the only one. Catch bus for Chinchwad. Get down at Dange Chowk. Take another bus from there.", mr: "नाही ती एकच आहे. तुम्ही चिंचवडची बस पकडा. डांगे चौकात उतरा. आणि तिकडून दुसरी बस पकडा.", roman: "nAhI tI ekach Ahe. tumhI chiMchavaDachI bas pakaDA. DAMge chaukAt utarA ANi tikaDUn dusarI bas pakaDA." },
    { en: "From where does bus for Chinchwad start?", mr: "चिंचवडची बस कुठून सुटते?", roman: "chiMchavaDachI bas kuThUn suTate?" },
    { en: "Which ticket you want?", mr: "तिकिट बोला. / तुम्हाला कुठलं तिकिट पाहिजे", roman: "tikiT bolA. / tumhAlA kuThalaM tikiT pAhije" },
    { en: "Please check carefully. There may be some in your bag.", mr: "बघा जरा नीट. बॅगेत असतील.", roman: "baghA jarA nIT. b~aget asatIl." },
    { en: "I will give you 3 rupees afterwards. Take it while getting down", mr: "३ रुपये नंतर देतो. उतरताना घ्या.", roman: "3 rupaye naMtar deto. utaratAnA ghyA." },
    { en: "Hello, it is Dange chowk", mr: "चला. डांगे चौक.", roman: "chalA. DAMge chauk." },
    { en: "Hello", mr: "हॅलो / नमस्कार", roman: "h~alo / namaskAr" },
    { en: "My name is Kaushik Lele", mr: "माझं नाव कौशिक लेले", roman: "mAjhM nAv kaushik lele" },
    { en: "Primary education took place in Delhi", mr: "प्राथमिक शिक्षण दिल्लीत झालं.", roman: "prAthamik shikShaN dillIt jhAlM." },
    { en: "My college was also in Delhi", mr: "माझं कॉलेज सुद्धा दिल्लीला होतं", roman: "mAjhaM k~olej suddhA dillIlA hotaM" },
    { en: "Which college?", mr: "कुठलं कॉलेज?", roman: "kuThalaM k~olej?" },
    { en: "Delhi Engineering College", mr: "दिल्ली इंजिनिअरिंग कॉलेज", roman: "dillI iMjiniariMg k~olej" },
    { en: "Which companies have you worked in?", mr: "कुठल्या कंपन्यांमध्ये तुम्ही काम केलं आहे?", roman: "kuThalyA kaMpanyAMmadhye tumhI kAm kelM Ahe." },
    { en: "Which technologies do you work on?", mr: "कुठल्या टेक्नोलोजी वर काम करता?", roman: "kuThalyA TeknolojI var kAm karatA?" },
    { en: "What do you expect from this job?", mr: "तुम्हाला या जॉब कडून काय अपेक्षा आहेत?", roman: "tumhAlA yA j~ob kaDUn kAy apekShA Ahet?" },
    { en: "Thanks", mr: "धन्यवाद.", roman: "dhanyavAd" },
    { en: "Washing clothes and dishes and floor-cleaning", mr: "धुणं, भांडी आणि केरफरशी", roman: "dhuNaM, bhAMDI ANi kerapharashI" },
    { en: "We are 4 elders and 2 children", mr: "आम्ही ४ मोठी माणसं आहोत आणि २ लहान मुलं आहेत.", roman: "AmhI 4 moThI mANasaM Ahot ANi 2 lahAn mulaM Ahet." },
    { en: "Please take 500 aunty", mr: "पाचशे घ्या ना मावशी.", roman: "pAchashe ghyA nA mAvashI." },
    { en: "Take this your salary", mr: "हा घ्या तुमचा पगार.", roman: "hA ghyA tumachA pagAr." },
    { en: "Hi Sara, I heard 26 Jan is holiday - Republic Day", mr: "हाना: हाय सारा. मला आत्ताच कळलं २६ जानेवारीला भारतात सुट्टी आहे कारण 26 जानेवारी हा इंडियाचा रिपब्लिक डे असतो!", roman: "hAnA hAy sArA. malA AttAch kaLalM jAnevArIlA bhAratAt suTTI Ahe kAraN jAnevArI hA iMDiyAchA ripablik De asato!" },
    { en: "Yes, right. Prajasattak Din in Marathi", mr: "हो बरोबर. हो मराठीत प्रजासत्ताकदिन असं म्हणतात.", roman: "ho barobar. ho marAThIt prajAsattAkadin asM mhaNatAt." },
    { en: "Parade at Rajpath New Delhi, 3 days", mr: "राजपथ नवी दिल्ली येथे संरक्षण मंत्रायल एक कार्यक्रम आयोजित करते, जो तीन दिवस चालतो.", roman: "rAjapath navI dillI yethe sMrakShaN mMtrAyal ek kAryakram Ayojit karate, jo tIn divas chAlato." },
    { en: "Thank you", mr: "धन्यवाद!", roman: "dhanyavAd!" },
    { en: "Hi, I want to open a saving account", mr: "नमस्कार, मला आपल्या बॅंकेत बचत खाते उघडायचे आहे.", roman: "namaskAr, malA ApalyA b~aMket bachat khAte ughaDAyache Ahe." },
    { en: "I want to meet Branch manager", mr: "मला शाखा व्यवस्थापकांना भेटायचे आहे. ते कुठे बसतात?", roman: "malA shAkhA vyavasthApakAMnA bheTAyache Ahe. te kuThe basatAt?" },
    { en: "Please fill up this application form", mr: "कृपया खाते उघडण्यासाठी हा अर्ज भरा", roman: "kRupayA khAte ughaDaNyAsAThI hA arj bharA" },
    { en: "Why did you not write wife's name?", mr: "इथे पत्नीचे नाव का नाही लिहिले?", roman: "ithe patnIche nAv kA nAhI lihile?" },
    { en: "This photo is not allowed", mr: "हा फोटो चालणार नाही.", roman: "hA phoTo chAlaNAr nAhI." },
    { en: "Please take a photo and bring it", mr: "फोटो काढून आणा", roman: "phoTo kADhUn ANA" },
    { en: "I want some information about this temple", mr: "मला या मंदिराबद्दल थोडी माहिती हवी आहे.", roman: "malA yA maMdirAbaddal thoDI mAhitI havI Ahe." },
    { en: "But which movie?", mr: "पण कोणता सिनेमा?", roman: "paN koNatA sinemA?" },
    { en: "Friend, are you watching world cup these days?", mr: "मित्रा, तू सध्या वर्ल्ड कप बघतो आहेस का?", roman: "mitrA, tU sadhyA varlD kap baghato Ahes kA?" },
    { en: "Which team are you supporting?", mr: "तू कोणत्या टीमला सपोर्ट करतो आहेस?", roman: "tU koNatyA TImalA saporT karato Ahes?" },
    { en: "Hey Kaushik, where are you going in so hurry?", mr: "अरे कौशिक, इतक्या घाईत कुठे जातोयस?", roman: "are kaushik, itakyA ghAIt kuThe jAtoyas?" },
    { en: "Shashi teaches me", mr: "शशी मला शिकवतात.", roman: "shashI malA shikavatAt." },
    { en: "I am not thirsty", mr: "मला तहान नाही लागली आहे", roman: "malA tahAn nAhI lAgalI Ahe" },
    { en: "I am waiting for Kaushik", mr: "मी कौशिकची वाट बघतोय", roman: "mI kaushikachI vAT baghatoy" },
    { en: "I waited for Kaushik", mr: "मी कौशिकची वाट बघितली", roman: "mI kaushikachI vAT baghitalI" },
    { en: "I am wearing T-shirt", mr: "मी टीशर्ट घातला आहे", roman: "mI TIsharT ghAtalA Ahe" },
    { en: "I wish he goes to school", mr: "माझी अशी इच्छा आहे की तो शाळेत गेला पाहिजे", roman: "mAjhI ashI ichChA Ahe kI to shALet gelA pAhije" },
    { en: "He wishes Kaushik wins", mr: "त्याची अशी इच्छा आहे की कौशिक जिंको", roman: "tyAchI ashI ichChA Ahe kI kaushik jiMko" },
    { en: "He believes Kaushik", mr: "त्याचा कौशिकवर विश्वास आहे", roman: "tyAchA kaushikavar vishvAs Ahe" },
    { en: "Will you please believe me?", mr: "तू कृपया माझ्यावर विश्वास ठेवशील का?", roman: "tU kRupayA mAjhyAvar vishvAs ThevashIl kA?" },
    { en: "Family members worship Ganpati and Lakshmi in the evening", mr: "घरचे लोक संध्याकाळी गणपती आणि लक्ष्मीची पूजा करतात", roman: "gharache lok sMdhyAkALI gaNapatI ANi lakShmIchI pUjA karatAt" },
    { en: "Instead of meeting friends, stay home and relax", mr: "तुमच्या मित्रांना भेटण्याऐवजी तुम्ही घरी राहून आराम करू शकता", roman: "tumachyA mitrAMnA bheTaNyAaivajI tumhI gharI rAhUn ArAm karU shakatA" },
    { en: "Learn Marathi or read your favorite books", mr: "मराठी शिका किंवा आपली आवडती पुस्तके वाचा", roman: "marAThI shikA kiMvA ApalI AvaDatI pustake vAchA" },
    { en: "These are Marathi online lessons. They're free", mr: "हे मराठी ऑनलाइन धडे आहेत. ते विनामूल्य आहेत", roman: "he marAThI ~onalAin dhaDe Ahet. te vinAmUly Ahet" },
    { en: "I live in this area 200 meters from here", mr: "मी पण या भागातच राहते. इथून २०० मीटर अंतरावर", roman: "mI paN yA bhAgAtach rAhate. ithUn 200 mITar aMtarAvar" },
    { en: "In high school, I learned French", mr: "हायस्कुलमध्ये मी फ्रेंच शिकले", roman: "hAyaskulamadhye mI phreMch shikale" },
    { en: "Behind my house there is a large mountain", mr: "माझ्या घरामागे एक मोठा पर्वत आहे", roman: "mAjhyA gharAmAge ek moThA parvat Ahe" },
    { en: "Then the girl gives him one hand full of sand", mr: "मुलगी त्याला एक मूठ वाळू आणून देते", roman: "mulagI tyAlA ek mUTh vALU ANUn dete" },
    { en: "This I find sad", mr: "ह्याचे मला वाईट वाटते", roman: "hyAche malA vAIT vATate" },
    { en: "I am enjoying learning Marathi through social media", mr: "मी सोशल मीडियातून मराठी शिकायला मला खूप मजा येतेय", roman: "mI soshal mIDiyAtUn marAThI shikAyalA malA khUp majA yetey" },
    { en: "Kaushik, why are you going to terrace?", mr: "कौशिक, तू गच्चीवर का जातोयस?", roman: "kaushik tU gachchIvar kA jAtoyas" },
    { en: "Because of moon coming between sun and earth, sun gets hidden", mr: "सूर्य आणि पृथ्वीच्या मध्ये चंद्र आल्यामुळे सूर्य झाकला जातो", roman: "sUry ANi pRuthvIchyA madhye chMdr AlyAmuLe sUry jhAkalA jAto" },
    { en: "In Chinese culture, heavenly dog eats the sun", mr: "चिनी संस्कृतीमध्ये, आकाशातला कुत्रा सूर्याला खातो अशी कल्पना आहे", roman: "chinI sMskRutImadhye AkAshAtalA kutrA sUryAlA khAto ashI kalpanA Ahe" },
    { en: "I wanted it on GudhiPadva itself", mr: "मला गुढीपाडव्याच्या दिवशीच हवं होतं", roman: "malA guDhIpADavyAchyA divashIch havM hotM" },
    { en: "Our work is to make this roadmap", mr: "आपलं काम काय आहे? हा roadmap बनवायचा", roman: "ApalM kAm kAy Ahe? hA roadmap banavAyachA" },
    { en: "We can build a friendship with him", mr: "त्याच्यासोबत मैत्री होऊ शकते", roman: "tyAchyAsobat maitrI hoU shakate" },
    { en: "I hope I have managed to surprise you this time", mr: "मला असं वाटतं की मी तुला ह्यावेळी surprise द्यायला जमलं एकदाचं!", roman: "malA asM vATatM kI mI tulA hyAveLI surprise dyAyalA jamalM ekadAchM" },
    { en: "I had learned in a jungle which is after Thane", mr: "मी ठाण्याच्या पुढे एका जंगलात शिकलो होतो", roman: "mI ThANyAchyA puDhe ekA jMgalAt shikalo hoto" },
    { en: "On that day he did not want to let anybody sit on him", mr: "त्याला त्या दिवशी कोणालाही स्वतःवर बसवायचं नव्हतं", roman: "tyAlA tyA divashI koNAlAhI svatHvar basavAyachM navhatM" },
    { en: "For nearly 15 minutes he took me deep within the jungle", mr: "तो मला साधारणतः पंधरा मिनिटांकरता जंगलाच्या आत कुठेतरी घेऊन गेला", roman: "to malA sAdhAraNatH pandhara miniTAMkaratA jMgalAchyA At kuThetarI gheUn gelA" },
    { en: "I got a hint", mr: "मला थोडं hint आलीये", roman: "malA thoDM hint AlIye" },
    { en: "So we started friendship", mr: "तर आम्ही मैत्री केली", roman: "tar AmhI maitrI kelI" },
    { en: "Why do you think I can't hear? I have not plugged my ears", mr: "ऐकू न यायला काय झालं? कानात बोळे नाही घातले मी", roman: "aikU n yAyalA kAy jhAlM? kAnAt boLe nAhI ghAtale mI" },
    { en: "Meet me at 2 pm", mr: "मला दुपारी दोन वाजता भेट", roman: "malA dupArI don vajatA bheT" },
    { en: "Meet me at 2 am", mr: "मला रात्री दोन वाजता भेट", roman: "malA rAtrI don vajatA bheT" },
    { en: "If you cannot meet in person, send a nice message", mr: "त्यांना मेसेजद्वारे छानसा संदेश पाठवा", roman: "tyAMnA mesejadvAre ChAnasA sMdesh pAThavA" },
    { en: "Blessing/Blessings", mr: "आशिर्वाद", roman: "AshirvAd" },
    { en: "My blessings are always with you", mr: "माझे आशिर्वाद सदैव तुझ्या पठीशी आहेत", roman: "mAjhe AshirvAd sadaiva tujhyA paThIshI Ahet" },
    { en: "Thank you", mr: "धन्यवाद", roman: "dhanyavAd" },
    { en: "I wish that he should win", mr: "माझी अशी इच्छा आहे की तो जिंकावा", roman: "mAjhI ashI ichChA Ahe kI to jiMkAvA" },
    { en: "I wish that she should win", mr: "माझी अशी इच्छा आहे की ती जिंकावी", roman: "mAjhI ashI ichChA Ahe kI tI jiMkAvI" },
    { en: "He wishes that we win", mr: "त्याची अशी इच्छा आहे की आम्ही जिंकावे", roman: "tyAchI ashI ichChA Ahe kI AmhI jiMkAve" },
    { en: "I wish that you(boy) should smile", mr: "माझी अशी इच्छा आहे की तू हसावास", roman: "mAjhI ashI ichChA Ahe kI tU hasAvAs" },
    { en: "I wish that you(girl) should smile", mr: "माझी अशी इच्छा आहे की तू हसावीस", roman: "mAjhI ashI ichChA Ahe kI tU hasAvIs" },
    { en: "I wish that he should not win", mr: "माझी अशी इच्छा आहे की तो जिंकू नये", roman: "mAjhI ashI ichChA Ahe kI to jiMkU naye" },
    { en: "I wish that he should not eat mango", mr: "माझी अशी इच्छा आहे की त्याने आंबा खाऊ नये", roman: "mAjhI ashI ichChA Ahe kI tyAne AMbA khAU naye" },
    { en: "Worship", mr: "पूजा", roman: "pUjA" },
    { en: "To worship", mr: "पूजा करणे", roman: "pUjA karaNe" },
    { en: "Welcome (formal)", mr: "सुस्वागतम", roman: "susvAgatam" },
    { en: "Welcome (daily)", mr: "या या", roman: "yA yA" },
    { en: "No thanks", mr: "नको", roman: "nako" },
    { en: "No I don't want anything", mr: "नको. मला काही नको", roman: "nako malA kAhI nako" },
    { en: "What is your name? (to boy/girl)", mr: "तुझे नाव काय", roman: "tujhe nAv kAy" },
    { en: "What is your name? (to man/lady)", mr: "तुमचे नाव काय", roman: "tumache nAv kAy" },
    { en: "My name is Kaushik", mr: "माझे नाव कौशिक", roman: "mAjhe nAv kaushik" },
    { en: "It was nice to meet you (formal)", mr: "तुम्हाला भेटून आनंद झाला", roman: "tumhAlA bheTUn AnaMd jhAlA" },
    { en: "It was nice to meet you (familiar)", mr: "तुम्हाला भेटून बरं वाटलं", roman: "tumhAlA bheTUn baraM vATalaM" },
    { en: "Hello Madam", mr: "अहो Madam", roman: "aho Madam" },
    { en: "Hello Sir", mr: "अहो Sir", roman: "aho Sir" },
    { en: "Hello! How are you? (to elder)", mr: "कायहो? कसे आहात?", roman: "kAyaho? kase AhAt?" },
    { en: "Please sing", mr: "गाना/गानं", roman: "gAnA/gAnaM" },
    { en: "Do talk to him", mr: "त्याच्याशी बोला. बोलाहं", roman: "tyAchyAshI bolA. bolAhaM" },
    { en: "Hello, My Dear Kesari group", mr: "नमस्कार, केसरी group.", roman: "namaskAr, kesarI grUp." },
    { en: "Welcome to Singapore", mr: "सिंगापूरमध्ये तुमचं स्वागत आहे.", roman: "siMgApUramadhye tumachM svAgat Ahe." },
    { en: "We will meet at 4.30 PM", mr: "याच ठिकाणी साडे चार वाजता आपण भेटू.", roman: "yAch ThikANI sADe chAr vAjatA ApaN bheTU." },
    { en: "I told him, still he ate it", mr: "मी त्याला सांगितले तरी त्याने हे खाल्ले", roman: "mI tyAlA sAMgitale tarI tyAne he khAlle" },
    { en: "This program is tomorrow also", mr: "हा कार्यक्रम उद्याही आहे", roman: "hA kAryakram udyAhI Ahe" },
    { en: "Everything", mr: "प्रत्येक गोष्ट", roman: "pratyek goShT" },
    { en: "Whiskers", mr: "कल्ले", roman: "kalle" },
    { en: "Chin", mr: "हनुवटी", roman: "hanuvaTI" },
    { en: "Thigh", mr: "मांडी", roman: "mAMDI" },
    { en: "Buttocks / Hip", mr: "ढुंगण", roman: "DhuMgaN" },
    { en: "Hippopotamus", mr: "पणघोडा", roman: "paNaghoDA" },
    { en: "Rhino", mr: "गेंडा", roman: "geMDA" },
    { en: "Third", mr: "तिसरा", roman: "tisarA" },
    { en: "Hello", mr: "नमस्कार", roman: "namaskar" },
    { en: "Hello sir, how may I help you?", mr: "नमस्कार सर, मी तुम्हाला कशी मदत करु शकतो?", roman: "namaskar sar mi tumhala kashi madat karu shakato?" },
    { en: "I received a message to link my Aadhaar with postpaid. Please tell me the procedure.", mr: "मला माझ्या पोस्टपेड कनेक्शनला आधार नंबर लिंक करण्याबद्दल मेसेज आला आहे. कृपया मला प्रक्रिया सांगा.", roman: "mala majhya postaped kanekshanala Adhar nambar link karanyabaddal mesej ala ahe. krupaya mala prakriya sanga." },
    { en: "No it's free. Connection verified within a day.", mr: "हे विनामूल्य आहे आणि कनेक्शन एका दिवसात सत्यापित होऊन जाईल.", roman: "he vinamuly ahe ani kanekshan eka divasat satyapit houn jail." },
    { en: "Fine. Thanks", mr: "ठीक आहे. धन्यवाद.", roman: "Thik ahe dhanyavad." },
    { en: "Sakshi - Help desk lady at Aadhaar center", mr: "साक्षी : आधार सेंटर येथे हेल्पडेस्क वर बसलेली महिला", roman: "sAkShI : AdhAr seMTar yethe helpaDesk var basalelI mahilA" },
    { en: "Hi", mr: "नमस्कार.", roman: "namaskAr." },
    { en: "Hello, how can I help you?", mr: "नमस्कार. मी काय मदत करू शकते तुमची.", roman: "namaskAr. mI kAy madat karU shakate tumachI." },
    { en: "One name, dob and address proof. Biometric tests redone.", mr: "हो. एक नाव, जन्मतारीख आणि पत्त्याचा पुरावा सादर करणे आवश्यक आहे.", roman: "ho. ek nAv, janmatArIkh ANi pattyAchA purAvA sAdar karaNe Avashyak Ahe." },
    { en: "Thank you so much", mr: "बरं. खूप खूप धन्यवाद.", roman: "barM. khUp khUp dhanyvAd" },
    { en: "Green Chili", mr: "हिरवी मिरची", roman: "hiravI mirachI" },
    { en: "Chickoo sapota", mr: "चिक्कु", roman: "chikku" },
    { en: "Please give menucard", mr: "मेनूकार्ड द्या", roman: "menUkArD dyA" },
    { en: "Which dish is served hot?", mr: "गरम काय आहे?", roman: "garam kAy Ahe?" },
    { en: "Which dish is served cold?", mr: "थंड काय आहे?", roman: "thaMD kAy Ahe?" },
    { en: "This vegetable will be sweet", mr: "ही भाजी गोड असेल", roman: "hI bhAjI goD asel" },
    { en: "This dish will be hot in taste", mr: "ही डिश तिखट असेल", roman: "hI Dish tikhaT asel" },
    { en: "Hello my dear", mr: "हॅलो बेटा.", roman: "h~alo beTA." },
    { en: "Hello aunty", mr: "नमस्कार काकू.", roman: "namaskAr kAkU." },
    { en: "Aunty, this dal is too tasty", mr: "काकू, ही डाळ खूप चविष्ट आहे.", roman: "kAkU, hI DAL khUp chaviShT Ahe." },
    { en: "Please give me a bit more", mr: "मला थोडी अजून द्या.", roman: "malA thoDI ajUn dyA." },
    { en: "What did you cook this morning?", mr: "कृपया मला सांगा आज सकाळी तुम्ही काय बनवले?", roman: "kRupayA malA sAMgA Aj sakALI tumhI kAy banavale?" },
    { en: "Police: Hey, take vehicle to side", mr: "अरे ए, गाडी बाजूला घे", roman: "are e, gADI bAjUlA ghe" },
    { en: "Police: Bring vehicle to side", mr: "गाडी बाजूला आण", roman: "gADI bAjUlA AN" },
    { en: "Driver: Thanks you sir", mr: "थॅंक यू साहेब", roman: "th~aMk yU sAheb" },
    { en: "Please come. Have seat", mr: "या, बसा.", roman: "yA, basA." },
    { en: "Nothing serious", mr: "काही विशेष नाही", roman: "kAhI visheSh nAhI" },
    { en: "Yes, take after eating something", mr: "हो, काहितरी खाऊनच घ्या.", roman: "ho, kAhitarI khAUnach ghyA." },
    { en: "Anything about diet?", mr: "बाकी पथ्य?", roman: "bAkI pathya?" },
    { en: "If you do not feel well then please come", mr: "बरं नाही वाटलं तर या.", roman: "barM nAhI vATalaM tar yA." },
    { en: "Take this", mr: "ही घ्या", roman: "hI ghyA" },
    { en: "Which cream biscuit is there?", mr: "कुठले क्रीम बिस्किट आहे?", roman: "kuThale krIm biskiT Ahe?" },
    { en: "I do not want this. Is there any other?", mr: "हे नको. अजून दुसरे. कुठले आहे का?", roman: "he nako. ajUn dusare kuThale Ahe kA?" },
    { en: "Plastic bags are banned. Take this paper bag", mr: "प्लॅस्टिकच्या पिशव्यांवर सध्या बंदी आहे. हि कागदी पिशवी घ्या.", roman: "pl~asTikachyA pishavyAMvar sadhyA baMdI Ahe. hi kAgadI pishavI ghyA." },
    { en: "If your eyes are good, you will fall in love of this world. But if your tongue is sweet, this whole world will fall in your love", mr: "जर तुमचे डोळे चांगले असतील तर तुम्ही या जगाच्या प्रेमात पडाल. पण तुमची जीभ गोड असेल तर हे संपूर्ण जग तुमच्या प्रेमात पडेल", roman: "jar tumache DoLe chAMgale asatIl tar tumhI yA jagAchyA premAt paDAl. paN tumachI jIbh goD asel tar he sMpUrN jag tumachyA premAt paDel" },
    { en: "A relationship created by pure mind will never break", mr: "निर्मळ मानाने बनलेलं नातं कधीच तुटणार नाही", roman: "nirmaL mAnAne banalelM nAtM kadhIch tuTaNAr nAhI" }
  ]
  },
  reading: {
    name: "Reading",
    words: [
    { en: "Thread for kite", mr: "मांजा", roman: "mAMjA" },
    { en: "Read it", mr: "हे वाच", roman: "he vAch" },
    { en: "Do not read it", mr: "हे वाचू नकोस", roman: "he vAchU nakos" },
    { en: "Black page", mr: "काळे पान", roman: "kALe pAn" },
    { en: "Black pages", mr: "काळी पाने", roman: "kALI pAne" },
    { en: "Talking book", mr: "बोलणारे पुस्तक", roman: "bolaNAre pustak" },
    { en: "Talked book", mr: "बोललेले पुस्तक", roman: "bolalele pustak" },
    { en: "He/She/They want page", mr: "त्याला/तीला/त्यांना पान पाहिजे/हवे आहे", roman: "tyAlA/tIlA/tyAMnA pAn pahije/have Ahe" },
    { en: "He/She/They want pages", mr: "त्याला/तीला/त्यांना पाने पाहिजे/हवी आहेत", roman: "tyAlA/tIlA/tyAMnA pAne pahije/havI Ahet" },
    { en: "He/She/They wanted page", mr: "त्याला/तीला/त्यांना पान पाहिजे/हवे होते", roman: "tyAlA/tIlA/tyAMnA pAn pahije/have hote" },
    { en: "He/She/They wanted pages", mr: "त्याला/तीला/त्यांना पाने पाहिजे/हवी होती", roman: "tyAlA/tIlA/tyAMnA pAne pahije/havI hotI" },
    { en: "He/She/They will need page", mr: "त्याला/तीला/त्यांना पान पाहिजे/हवे असेल", roman: "tyAlA/tIlA/tyAMnA pAn pahije/have asel" },
    { en: "He/She/They will need pages", mr: "त्याला/तीला/त्यांना पाने पाहिजे/हवी असतील", roman: "tyAlA/tIlA/tyAMnA pAne pahije/havI asatIl" },
    { en: "She should write letter", mr: "तीने पत्र लिहावे", roman: "tIne patr lihAve" },
    { en: "Tell me about them whom you read about", mr: "ज्यांच्याबद्दल तू वाचलेस त्यांच्याबद्दल मला सांग", roman: "jyAMchyAbaddal tU vAchales tyAMchyAbaddal malA sAMg" },
    { en: "He quickly came and read the letter", mr: "तेवढ्यात त्याने येऊन पत्र वाचून घेतले", roman: "tevaDhyAt tyAne yeUn patr vAchUn ghetale" },
    { en: "Keep tea ready", mr: "चहा करून ठेव", roman: "chahA karUn Thev" },
    { en: "We have booked tickets", mr: "आम्ही तिकिटे काढून ठेवली आहेत", roman: "AmhI tikiTe kADhUn ThevalI Ahet" },
    { en: "I had already given my password", mr: "मी आधीच पासवर्ड सांगून चुकलो होतो", roman: "mI AdhIch pAsavarD sAMgUn chukalo hoto" },
    { en: "Not utter a word", mr: "अवाक्षर न काढणे", roman: "avAkShar n kADhaNe" },
    { en: "Read", mr: "वाचणे vAchaNe", roman: "patr vAchale" },
    { en: "Already", mr: "पूर्वीच / आधीच", roman: "pUrvIch / AdhIch" },
    { en: "My friend booked in Nature Park. 2BHK", mr: "माझ्या मित्राने nature park मधे बूक केला. 2BHK", roman: "mAjhyA mitrAne nature park madhe book kelA. 2bhk" },
    { en: "Take out book", mr: "पुस्तक काढा", roman: "pustak kADhA" },
    { en: "I am ready to leave my home, my parents for you", mr: "तुझ्यासाठी मी माझं घर, माझ्या आईवडिलांना सोडायला तयार आहे", roman: "tujhyAsAThI mI mAjhM ghar, mAjhyA AIvaDilAMnA soDAyalA tayAr Ahe" },
    { en: "I am ready to come with you anywhere you say", mr: "तू म्हणशील तिथे मी तुझ्या बरोबर यायला तयार आहे", roman: "tU mhaNashIl tithe mI tujhyA barobar yAyalA tayAr Ahe" },
    { en: "I like reading", mr: "मला वाचन करायला आवडते.", roman: "malA vAchan karAyalA AvaDate." },
    { en: "How can I apply for cheque book?", mr: "मी चेकबुकसाठी अर्ज कसा करू?", roman: "mI chekabukasAThI arj kasA karU?" },
    { en: "No friend; I have already seen that movie", mr: "नको मित्रा, तो सिनेमा मी आघीच बघितला आहे.", roman: "nako mitrA, to sinemA mI AghIch baghitalA Ahe." },
    { en: "The guavas are near the book", mr: "पेरू पुस्तकाजवळ आहेत", roman: "perU pustakAjavaL Ahet" },
    { en: "For many years I was on Facebook", mr: "बऱ्याच वर्षांपासून मी फेसबुकवर होतो", roman: "bryAch varShAMpAsUn mI phesabukavar hoto" },
    { en: "Now I use Whatsapp, Facebook, YouTube daily", mr: "आजकाल मी Whatsapp, Facebook, YouTube दररोज वापरते", roman: "AjakAl mI Whatsapp Facebook YouTube dararoj vAparate" },
    { en: "Swear word (singular)", mr: "शिवी", roman: "shivI" },
    { en: "Swear words (plural)", mr: "शिव्या", roman: "shivyA" },
    { en: "He is not ready to go anywhere", mr: "तो कुठेही जायला तयार नाही", roman: "to kuThehI jAyalA tayAr nAhI" },
    { en: "Friend, is it not ready yet?", mr: "मित्रा, अजून झाले नाही का?", roman: "mitrA, ajUn jhaale nAhI kA?" },
    { en: "From the new year, I have decided not to spend time on Facebook", mr: "नवीन वर्षापासून मी ठरवलंय ... फेसबुक वर अजिबात वेळ घालवायचा नाही", roman: "navIn varShApAsUn mI TharavalMy ... Facebook var ajibAt veL ghAlavAyachA nAhI" }
  ]
  },
  writing: {
    name: "Writing & Script",
    words: [
    { en: "Digit", mr: "अंक", roman: "aMk" },
    { en: "Bracket", mr: "कंस", roman: "kaMs" },
    { en: "Mark", mr: "मार्क", roman: "mArk" },
    { en: "Write", mr: "लिही", roman: "lihI" },
    { en: "Write your address", mr: "तुमचा पत्ता लिहावा", roman: "tumachA pattA lihAvA" },
    { en: "Write your addresses", mr: "तुमचे पत्ते लिहावे", roman: "tumache patte lihAve" },
    { en: "Good handwriting", mr: "अरे वा! / छान! हस्ताक्षर", roman: "are vA! / ChAn! hastAkShar" },
    { en: "Can I write", mr: "मी लिहू शकतो का?", roman: "mI lihU shakato kA?" },
    { en: "To write", mr: "लिहिणे lihiNe", roman: "patr lihile" }
  ]
  },
  numbers: {
    name: "Numbers",
    words: [
    { en: "Money", mr: "पैसे", roman: "Paise" },
    { en: "We (listener including)", mr: "आपण", roman: "ApaN" },
    { en: "We went to the party (listener not included)", mr: "आम्ही पार्टीला गेलो", roman: "AmhI pArTIlA gelo" },
    { en: "We went to the party (listener included)", mr: "आपण पार्टीला गेलो", roman: "ApaN pArTIlA gelo" },
    { en: "Listen", mr: "ऐक", roman: "aik" },
    { en: "He has not eaten the mango", mr: "त्याने आंबा खाल्ला नाही आहे", roman: "tyAne AMbA khAllA nAhI Ahe" },
    { en: "She had eaten mango", mr: "तीने आंबा खाल्लेला", roman: "tIne AMbA khAllelA" },
    { en: "I don't remember she having eaten mango", mr: "तीने आंबा खाल्ल्याचे मला आठवत नाही", roman: "tIne AMbA khAllyAche malA AThavat nAhI" },
    { en: "He should have eaten mango", mr: "त्याने आंबा खायला पाहिजे/हवा होता", roman: "tyAne AMbA khAyalA pAhije/havA hotA" },
    { en: "He should have eaten tamarind", mr: "त्याने चिंच खायला पाहिजे/हवी होती", roman: "tyAne chiMch khAyalA pAhije/havI hotI" },
    { en: "He should have gone", mr: "त्याने जायला पाहिजे होते", roman: "tyAne jAyalA pAhije hote" },
    { en: "He should have gone", mr: "तो गेला पाहिजे होता", roman: "to gelA pAhije hotA" },
    { en: "Do not use mobile phones", mr: "मोबाईल फोन वापरु नका", roman: "mobAIl phon vAparu nakA" },
    { en: "Oh my God! What have I done!", mr: "अरे देवा मी हे काय करून बसलो", roman: "are devA mI he kAy karUn basalo" },
    { en: "Well done! You won", mr: "शाब्बास! तू सामना जिंकलास", roman: "shAbbAs! tU sAmanA jiMkalAs" },
    { en: "Someone may see it! (blush)", mr: "इश्श्य कोणीतरी बघेल ना", roman: "ishshya koNItarI baghel nA" },
    { en: "He might have gone yesterday", mr: "कदाचित तो काल गेला असेल", roman: "kadAchit to kAl gelA asel" },
    { en: "He had gone", mr: "तो गेला होता", roman: "to gelA hotA" },
    { en: "He might have gone", mr: "तो गेला असावा", roman: "to gelA asAvA" },
    { en: "You have eaten mango", mr: "तू आंबा खाल्ला आहेस", roman: "tU AMbA khAllA Ahes" },
    { en: "You might have eaten mango", mr: "तू आंबा खाल्ला असावास", roman: "tU AMbA khAllA asAvAs" },
    { en: "Speaking phone", mr: "बोलता फोन", roman: "bolatA phon" },
    { en: "He has three paternal uncles", mr: "त्याला तीन काका आहेत", roman: "tyAlA tIn kAkA Ahet" },
    { en: "Oh my God! What have I done!", mr: "अरे देवा मी हे काय करून बसलो/गेलो", roman: "are devA mI he kAy karUn basalo/gelo" },
    { en: "To threaten", mr: "दम भरणे", roman: "dam bharaNe" },
    { en: "To pretend", mr: "कांगावा करणे", roman: "kAMgAvA karaNe" },
    { en: "To count", mr: "मोजणे mojaNe", roman: "paise mojale" },
    { en: "To listen", mr: "ऐकणे aikaNe", roman: "gANI aikalI" },
    { en: "To call on phone", mr: "फोन लावणे", roman: "phon lAvaNe" },
    { en: "To make one speak", mr: "बोलायला लावणे", roman: "bolAyalA lAvaNe" },
    { en: "To make one laugh", mr: "हसायला लावणे", roman: "hasAyalA lAvaNe" },
    { en: "To make one drink", mr: "प्यायला लावणे", roman: "pyAyalA lAvaNe" },
    { en: "Light (weight)", mr: "हलका", roman: "halakA" },
    { en: "Where had you gone? (to boy)", mr: "तू कुठे गेला होतास", roman: "tU kuThe gelA hotAs" },
    { en: "I had gone to movie (boy)", mr: "मी पिक्चरला गेलो होतो", roman: "mI pikcharalA gelo hoto" },
    { en: "Eight years", mr: "आठ वर्षं", roman: "ATh varShM" },
    { en: "Had you stayed one more year, you would have got gratuity", mr: "तिकडे अजून एक वर्ष थांबला असतास तर gratuity मिळाली असती", roman: "tikaDe ajUn ek varSh thAMbalA asatAs tar gratuity miLAlI asatI" },
    { en: "It is OK. Not much. Work will be Nine-to-six", mr: "ठीक आहे. इतकं जास्त नाही. Nine-to-six काम होतं", roman: "ThIk Ahe. itakaM jAst nAhI. Nine-to-six kAm hotM" },
    { en: "OK. What is your number?", mr: "OK. तुझा number काय?", roman: "OK. tujhA number kAy?" },
    { en: "I have your number. I give you miss-call", mr: "माझ्या कडे तुझा number आहे. miss-call देतो.", roman: "mAjhyA kaDe tujhA number Ahe. miss-call deto." },
    { en: "Open tenth chapter", mr: "दहावा धडा उघडा", roman: "dahAvA dhaDA ughaDA" },
    { en: "No. It is 12345679. Wrong number.", mr: "नाही. १२३४५६७९ आहे. रॉंग नंबर", roman: "nAhI. 12345679 Ahe. wrong number" },
    { en: "Give two rupees change", mr: "दोन रुपये सुट्टे द्या.", roman: "don rupaye suTTe dyA." },
    { en: "We two! King-and-Queen", mr: "आपण दोघं राजाराणी", roman: "ApaN doghaM rAjArANI" },
    { en: "Mother, Father, two brothers and one sister", mr: "आई, वडील, दोन भाऊ आणि एक बहीण.", roman: "AI, vaDIl, don bhAU ANi ek bahIN." },
    { en: "From where will I get form to open account?", mr: "खाते उघडण्यासाठी मला फॉर्म कुठून मिळेल?", roman: "khAte ughaDaNyAsAThI malA ph~orm kuThUn miLel?" },
    { en: "I want last year's account statements", mr: "मला मागच्या वर्षाचे अकाउंट स्टेटमेंट हवे आहे.", roman: "malA mAgachyA varShAche akAuMT sTeTameMT have Ahe." },
    { en: "Go to counter number 4", mr: "काउंटर नंबर चारवर जा.", roman: "kAuMTar nMbar chAravar jA." },
    { en: "Attach two photos. Also AADHAR copy", mr: "याच्यावर दोन फोटो लावा. आणि आधार कार्डची कॉपी सुद्धा जोडावी लागेल.", roman: "yAchyAvar don phoTo lAvA. ANi AdhAr kArDachI k~opI suddhA joDAvI lAgel." },
    { en: "Go straight. There is enquiry counter", mr: "तुम्ही सरळ जा. तिकडे चौकशीचे काउंटर आहे.", roman: "tumhI saraL jA tikaDe. tikaDe chaukashIche kAuMTar Ahe." },
    { en: "Half past six", mr: "साडे सहा वाजता.", roman: "sADe sahA vAjatA." },
    { en: "I will come to your place at six", mr: "मी तुझ्या घरी सहा वाजता येतो.", roman: "mI tujhyA gharI sahA vAjatA yeto." },
    { en: "Only 10 in one batch", mr: "फक्त दहा.", roman: "phakta dahA." },
    { en: "He has two brothers", mr: "त्याला दोन भाऊ आहेत", roman: "tyAlA don bhAU Ahet" },
    { en: "My earphone is tangled", mr: "माझा इयरफोन गुंतला आहे", roman: "mAjhA iyaraphon guMtalA Ahe" },
    { en: "Put my phone to charge", mr: "माझा फोन चार्जीगला ठेवा", roman: "mAjhA phon chArjIgalA ThevA" },
    { en: "My phone's battery is dead", mr: "माझा फोन चार्ज नाहिये", roman: "mAjhA phon chArj nAhiye" },
    { en: "Everyone talks about corona virus these days", mr: "आजकाल प्रत्येकजण कोरोना विषाणू बद्दल बोलतो", roman: "AjakAl pratyekajaN koronA viShANU baddal bolato" },
    { en: "I will tell you about my country Wales", mr: "तुम्हाला माझा देश – वेल्सबद्दल सांगीन", roman: "tumhAlA mAjhA desh – vels deshabaddal sAMgIn" },
    { en: "Eclipse will start in five minutes", mr: "पाच मिनिटांनी सुरु होईल ग्रहण", roman: "pAch miniTAMnI suru hoIl grahaN" },
    { en: "I had learned horse riding first time 10 years ago", mr: "हॉर्स रायडींग मी पहिल्यांदा दहा वर्षांपूर्वी शिकलो होतो", roman: "Horse riding mI pahilyAMdA dahA varShAMpUrvI shikalo hoto" },
    { en: "That day I felt, I am gone (dead)", mr: "त्यादिवशी मला वाटलं मी गेलो", roman: "tyAdivashI malA vATalM mI gelo" },
    { en: "Women have great contribution from home to country development", mr: "आपल्या घरापासून ते देशाच्या विकासामध्येही महिलांचे मोठे योगदान आहे", roman: "ApalyA gharApAsUn te deshAchyA vikAsAmadhyehI mahilAMche moThe yogadAn Ahe" },
    { en: "Ten rupees per person", mr: "दहा रुपये", roman: "dahA rupaye" },
    { en: "Ticket will have two parts", mr: "तिकिटाचे दोन भाग आहेत.", roman: "tikiTAche don bhAg Ahet." },
    { en: "Call someone", mr: "कोणाला तरी बोलव", roman: "koNAlA tarI bolav" },
    { en: "Call anyone", mr: "कोणालाही बोलव", roman: "koNAlAhI bolav" },
    { en: "He has gone somewhere", mr: "तो सकाळपासून कुठेतरी गेला आहे", roman: "to sakALapAsUn kuThetarI gelA Ahe" },
    { en: "Everybody / Everyone", mr: "प्रत्येक जण", roman: "pratyek jaN" },
    { en: "Backbone", mr: "कणा", roman: "kaNA" },
    { en: "Bone", mr: "हाड", roman: "hAD" },
    { en: "First", mr: "पहिला", roman: "pahilA" },
    { en: "Second", mr: "दुसरा", roman: "dusarA" },
    { en: "Fourth", mr: "चौथा", roman: "chauthA" },
    { en: "Sixth", mr: "सहावा", roman: "sahAvA" },
    { en: "Seventh", mr: "सातवा", roman: "sAtavA" },
    { en: "Eighth", mr: "आठवा", roman: "AThavA" },
    { en: "Three fourth", mr: "पाऊण", roman: "pAUN" },
    { en: "One & quarter", mr: "सव्वा", roman: "savvA" },
    { en: "One & half", mr: "दीड", roman: "dID" },
    { en: "Quarter to two", mr: "पावणे दोन", roman: "pAvaNe don" },
    { en: "Two & quarter", mr: "सव्वा दोन", roman: "savvA don" },
    { en: "Two & half", mr: "अडीच", roman: "aDIch" },
    { en: "Three & half", mr: "साडे तीन", roman: "sADe tIn" },
    { en: "Aadhar card alone is sufficient. Biometric test will validate.", mr: "तुमच्या मोबाईल नंबरच्या शिवाय फक्त आधार कार्ड पुरेसे आहे. पण दिलेला आधार क्रमांक प्रमाणित करण्यासाठी बायोमेट्रिक चाचणी घेतली जाईल", roman: "tumachya mobail nmbarachya shivay phakt Adhar kard purese ahe. pan dilela Adhar kramank pramanit karanyasathi bayometrik chachani ghetali jail." },
    { en: "You'll have to complete process for both numbers separately", mr: "तर तुम्हाला दोन्ही नंबरसाठी प्रक्रिया वेगवेगळी पूर्ण करावी लागेल.", roman: "tar tumhala donhi nmbarasathi prakriya vegavegali purn karavi lagel." },
    { en: "I have registered your both numbers. Check if you've received the OTP.", mr: "मी तुमच्या दोन्ही नंबरची नोंदणी करून दिली आहे. बघा OTP आला आहे का?", roman: "mi tumachya donhi nmbarachi nondani karun dili ahe. bagha OTP ala ahe ka?" },
    { en: "Bala - citizen who wants to link mobile number", mr: "बाला : आपला मोबाईल क्रमांक जोडण्यास इच्छुक असलेला नागरीक.", roman: "ApalA mobAIl kramAMk joDaNyAs ichChuk asalelA nAgarIk." },
    { en: "I had received a message to link phone with Aadhaar", mr: "माझ्या मोबाईल नंबरवर, आधार क्रमांकाला फोन नंबर जोडण्याविषयी मला एक संदेश मिळाला होता.", roman: "mAjhyA mobAIl naMbaravar, AdhAr kramAMkAlA phon naMbar joDaNyAviShayI malA ek saMdesh miLAlA hotA." },
    { en: "Give one more Roti", mr: "एक रोटी आणखी द्या", roman: "ek roTI ANakhI dyA" },
    { en: "These two in morning and these 2 in evening", mr: "या दोन सकाळी या दोन संध्याकाळी.", roman: "yA don sakALI yA don saMdhyAkALI." },
    { en: "Hundred rupees", mr: "शंभर रुपये.", roman: "shaMbhar rupaye." },
    { en: "Seventy rupees", mr: "सत्तर झाले", roman: "sattar jhAle" }
  ]
  },
  animals: {
    name: "Animals & Nature",
    words: [
    { en: "Near/close to", mr: "जवळ", roman: "javaL" },
    { en: "To keep animal (not cause to run)", mr: "पाळणे", roman: "pALaNe" },
    { en: "I have been working there for 3 years", mr: "मी तिकडे ३ वर्षे काम करत आलो आहे", roman: "mI tikaDe 3 varShe kAm karat Alo Ahe" },
    { en: "I will have been working there for 3 years", mr: "मी तिकडे ३ वर्षे काम करत आलो असेन", roman: "mI tikaDe 3 varShe kAm karat Alo asen" },
    { en: "Black chair", mr: "काळी खुर्ची", roman: "kALI khurchI" },
    { en: "Black chairs", mr: "काळ्या खुर्च्या", roman: "kALyA khurchyA" },
    { en: "Good chair", mr: "चांगली खुर्ची", roman: "chAMgalI khurchI" },
    { en: "For good chair", mr: "चांगल्या खुर्ची साठी", roman: "chAMgalyA khurchI sAThI" },
    { en: "Moving chair", mr: "हलणारी खुर्ची", roman: "halaNArI khurchI" },
    { en: "Moved chair", mr: "हललेली खुर्ची", roman: "halalelI khurchI" },
    { en: "He learned. So he could speak Japanese", mr: "तो शिकला. म्हणून त्याला जपानी बोलता आले", roman: "to shikalA. mhaNUn tyAlA japAnI bolatA Ale" },
    { en: "He did not learn. So he could not speak Japanese", mr: "तो शिकला नाही. म्हणून त्याला जपानी बोलता आले नाही", roman: "to shikalA nAhI. mhaNUn tyAlA japAnI bolatA Ale nAhI" },
    { en: "She will search it forever", mr: "ती कायम ते शोधत बसेल", roman: "tI kAyam te shodhat basel" },
    { en: "I happened to hear about strike", mr: "माझ्या ऐकण्यात आले", roman: "mAjhyA aikaNyAt Ale" },
    { en: "Moving chair", mr: "हलती खुर्ची", roman: "halatI khurchI" },
    { en: "Though it is old song, I heard it today", mr: "हे जुने गाणे असले तरी मी आज ऐकले", roman: "he june gANe asale tarI mI Aj aikale" },
    { en: "Now she will search it forever", mr: "आता ती कायम ते शोधत बसेल", roman: "AtA tI kAyam te shodhat basel" },
    { en: "I happened to hear about strike", mr: "रिक्षांच्या संपाबद्दल माझ्या ऐकण्यात आले", roman: "rikShAMchyA saMpAbaddal mAjhyA aikaNyAt Ale" },
    { en: "No control on tongue", mr: "जिभेला हाड नसणे", roman: "jibhelA hAD nasaNe" },
    { en: "If employee works 1 year, gratuity right", mr: "१ वर्ष काम केल्यास कर्मचाऱ्याला Gratuityचा अधिकार मिळेल", roman: "1 varSh kAm kelyAs karmachAryAlA GratuitychA adhikAr miLel" },
    { en: "To wear", mr: "घालणे ghAlaNe", roman: "sharT ghAtalA" },
    { en: "To wear (accessory)", mr: "लावणे lAvaNe", roman: "chaShmA lAvalA" },
    { en: "To search", mr: "शोधणे shodhaNe", roman: "shodhale" },
    { en: "Learn", mr: "शिकणे shikaNe", roman: "phreMch shikalo" },
    { en: "To touch by hand", mr: "हात लावणे", roman: "hAt lAvaNe" },
    { en: "To wear sunglass", mr: "चष्मा लावणे", roman: "chaShmA lAvaNe" },
    { en: "To apply face powder", mr: "पावडर लावणे", roman: "pAvaDar lAvaNe" },
    { en: "Hard (surface)", mr: "कडक", roman: "kaDak" },
    { en: "Clearly", mr: "स्पष्टपणे", roman: "spaShTapaNe" },
    { en: "Yearly", mr: "दरवर्षी", roman: "daravarShI" },
    { en: "Post office is nearby", mr: "पोस्ट ऑफीस जवळच आहे", roman: "posT ~ophIs javaLach Ahe" },
    { en: "How many years were you there?", mr: "तिकडे किती वर्षं होतास?", roman: "tikaDe kitI varShM hotAs?" },
    { en: "4 Years", mr: "चार वर्षं", roman: "chAr varShM" },
    { en: "Yes, the search is going on", mr: "हो, शोध चालू आहे.", roman: "ho shodh chAlU Ahe." },
    { en: "Yesterday we learnt half of lesson", mr: "काल आपण अर्धा धडा शिकलो होतो.", roman: "kAl ApaN ardhA dhaDA shikalo hoto." },
    { en: "Let's go ahead today", mr: "आज पुढे जाऊया", roman: "Aj puDhe jAUyA" },
    { en: "If I hear noise again, I will make you stand for whole period", mr: "परत आवाज आला तर पूर्ण तासभर उभे करीन.", roman: "parat AvAj AlA tar pUrN tAsabhar ubhe karIn." },
    { en: "Not here. Go ahead", mr: "इथे नाही. पुढे जा.", roman: "ithe nAhI. puDhe jA." },
    { en: "Where ahead?", mr: "पुढे कुठे?", roman: "puDhe kuThe?" },
    { en: "Mostly you will get. Otherwise catch bus for phase-2", mr: "बहुतेक मिळेल. नाहितर फेज-२ पर्यंत जाणारी बस पकडा.", roman: "bahutek miLel. nAhitar phej-2 paryaMt jANArI bas pakaDA." },
    { en: "I have 10 years of experience in IT", mr: "माझा आय.टी. मधला अनुभव १० वर्षांचा आहे.", roman: "mAjhA Ay.TI. madhalA anubhav 10 varShAMchA Ahe." },
    { en: "Positive attitude and dedication", mr: "सकारात्मक विचार आणि डेडीकेशन.", roman: "sakArAtmak vichAr ANi DeDIkeshan." },
    { en: "Come for Mangalarati. At 4.30 early morning", mr: "मंगलारती ला या. पहाटे साडे चार वाजता या.", roman: "maMgalAratI lA yA. pahATe sADe chAr vAjatA yA." },
    { en: "Wow. What are you learning?", mr: "वा! तू काय शिकतोयस?", roman: "vA! tU kAy shikatoyas?" },
    { en: "I am learning to play guitar", mr: "मी गिटार वाजवायला शिकतोय.", roman: "mI giTAr vAjavAyalA shikatoy." },
    { en: "I am also interested in learning guitar", mr: "मला पण गिटार शिकण्यात रस आहे.", roman: "malA paN giTAr shikaNyAt ras Ahe." },
    { en: "Wait, I am wearing tie (in act)", mr: "एक मिनिट थांब. मी टाय घालतो आहे", roman: "ek miniT thAMb. mI TAy ghAlato Ahe" },
    { en: "Exams are nearing", mr: "परीक्षा जवळ आली आहे", roman: "parIkShA javaL AlI Ahe" },
    { en: "Give me a hand", mr: "मला थोडी मदत करा", roman: "malA thoDI madat karA" },
    { en: "I have a runny nose", mr: "मला सर्दी झाली आहे", roman: "malA sardI jhAlI Ahe" },
    { en: "Long time since we met. Do you live near here?", mr: "आपल्याला भेटून बरेच दिवस झाले. तू जवळपास राहतोस का?", roman: "ApalyAlA bheTUn barech divas jhAle. tU javaLapAs rAhatos kA?" },
    { en: "Apply hand sanitizer when you leave", mr: "निघताना हॅन्ड सॅनिटायझर लाव", roman: "nighatAnA h~anD s~aniTAyajhar lAv" },
    { en: "Solar eclipse should not be seen by naked eyes", mr: "सूर्यग्रहण नुसत्या डोळ्यांनी बघायचं नसतं असं ऐकलं आहे", roman: "sUryagrahaN nusatyA DoLyAMnI baghAyachM nasatM asM aikalM Ahe" },
    { en: "Lunar eclipse can be seen by naked eyes", mr: "चंद्रग्रहण सध्या डोळ्यांनी पाहता येतं", roman: "chMdragrahaN sadhyA DoLyAMnI pAhatA yetM" },
    { en: "I am talking with you. Can you hear?", mr: "मी तुझ्याशी बोलतो आहे. तुला ऐकू येतंय का?", roman: "mI tujhyAshI bolato Ahe. tulA aikU yetMy kA" },
    { en: "Keep your mouth shut", mr: "थोबाड बंद ठेव तुझं", roman: "thobAD bMd Thev tujhM" },
    { en: "Year", mr: "वर्ष", roman: "varSha" },
    { en: "Heartiest Congratulations", mr: "हार्दिक/मनःपूर्वक अभिनंदन", roman: "hArdik/manHpUrvak abhinaMdan" },
    { en: "May you live 100 years", mr: "जीवेत शरदः शतम", roman: "jIvet sharadH shatam" },
    { en: "Dear", mr: "प्रिय", roman: "priya" },
    { en: "May new year be happy", mr: "नवीन वर्ष सुखदायक असो", roman: "navIn varSh sukhadAyak aso" },
    { en: "It was nice to hear that", mr: "हे ऐकून बरं वाटलं की", roman: "he aikUn baraM vATalM kI" },
    { en: "Drop me near S.P. College", mr: "एस. पी. कॉलेजला सोडा", roman: "es. pI. k~olejalA soda" },
    { en: "Here is S.P. College", mr: "आले एस. पी. कॉलेज", roman: "aale es. pI. k~olej" },
    { en: "We came so near, how so much?", mr: "इतक्या जवळ आलो, तरी इतके कसे?", roman: "itakyA javaL aalo, tarI itake kase?" },
    { en: "Head", mr: "डोके", roman: "Doke" },
    { en: "Brain", mr: "मेंदू", roman: "meMdU" },
    { en: "Hairs", mr: "केस", roman: "kes" },
    { en: "Face", mr: "चेहरा", roman: "cheharA" },
    { en: "Forehead", mr: "कपाळ", roman: "kapAL" },
    { en: "Eyebrow", mr: "भुवई", roman: "bhuvaI" },
    { en: "Eyelid", mr: "पापणी", roman: "pApaNI" },
    { en: "Eye", mr: "डोळा", roman: "DoLA" },
    { en: "Eyeball", mr: "बुब्बुळ", roman: "bubbuL" },
    { en: "Nose", mr: "नाक", roman: "nAk" },
    { en: "Ear", mr: "कान", roman: "kAn" },
    { en: "Earlobe", mr: "कानाची पाळी", roman: "kAnAchI pALI" },
    { en: "Mouth", mr: "तोंड", roman: "toMD" },
    { en: "Tooth", mr: "दात", roman: "dAt" },
    { en: "Tongue", mr: "जीभ", roman: "jIbh" },
    { en: "Beard", mr: "दाढी", roman: "dADhI" },
    { en: "Heart", mr: "ह्रुदय", roman: "hruday" },
    { en: "Hand", mr: "हात", roman: "hAt" },
    { en: "Finger", mr: "बोट", roman: "boT" },
    { en: "Index finger", mr: "तर्जनी", roman: "tarjanI" },
    { en: "Middle finger", mr: "मधले बोट", roman: "madhale boT" },
    { en: "Ring finger", mr: "अनामिका", roman: "anAmikA" },
    { en: "Small finger", mr: "करंगळी", roman: "karaMgaLI" },
    { en: "Leg", mr: "पाय", roman: "pAy" },
    { en: "Bear", mr: "अस्वल", roman: "asval" },
    { en: "Cat", mr: "मांजर", roman: "mAMjar" },
    { en: "Dog", mr: "कुत्रा", roman: "kutrA" },
    { en: "Fish", mr: "मासा", roman: "mAsA" },
    { en: "You can go for finger print on that side now", mr: "हो झाले. आता तुम्ही तिकडे जाऊन फिंगर प्रिंट देऊ शकता.", roman: "ho jhale. ata tumhi tikade jaun phingar print deu shakata." },
    { en: "After Biometric verification, reply with 'Y' to confirmation message", mr: "बायोमेट्रिक सत्यापनानंतर तुम्हाला 24 तासांत पुष्टीकरण संदेश मिळेल. त्यावर 'Y' लिहून पाठवून द्या.", roman: "bayometrik satyapananantar tumhala 24 tasaat pushtikaran sandesh milel. tyavar 'Y' lihun pathavun dya." },
    { en: "Nearly 7-10 days. You'll get message.", mr: "सुमारे सात ते दहा दिवसांत होऊन जाईल. तुम्हाला तुमच्या नंबरवर मेसेज येईल.", roman: "sumAre sAt te dahA divasAMt hoUn jAIl. tumhAlA tumachyA naMbaravar mesej yeIl." },
    { en: "Lady Finger", mr: "भेंडी", roman: "bheMDI" },
    { en: "Pear", mr: "नासपती", roman: "nAsapatI" },
    { en: "Aunty, I like all vegetables but ladyfinger is my favourite", mr: "काकू मला सगळ्या भाज्या आवडतात पण मला भेंडी सगळ्यात जास्त आवडते.", roman: "kAkU malA sagaLyA bhAjyA AvaDatAt paN malA bheMDI sagaLyAt jAst AvaDate." },
    { en: "Police: Hey, can't you hear?", mr: "ऐकू नाही आलं का रे?", roman: "aikU nAhI AlaM kA re?" },
    { en: "Show eyes", mr: "डोळे दाखवा", roman: "DoLe dAkhavA" },
    { en: "Show tongue", mr: "जीभ दाखवा", roman: "jIbh dAkhavA" },
    { en: "Open mouth wide", mr: "मोठा आ करा.", roman: "moThA A karA." },
    { en: "And wear woolen cloths", mr: "आणि गरम कपडे घाला.", roman: "ANi garam kapaDe ghAlA." }
  ]
  },
  dailyLife: {
    name: "Daily Life",
    words: [
    { en: "House", mr: "घर", roman: "Ghar" },
    { en: "City", mr: "शहर", roman: "Śahar" },
    { en: "Village", mr: "गाव", roman: "Gāv" },
    { en: "Yes", mr: "हो", roman: "Ho" },
    { en: "No", mr: "नाही", roman: "Nāhī" },
    { en: "Bad", mr: "वाईट", roman: "Vāīṭ" },
    { en: "Big", mr: "मोठे", roman: "Moṭhe" },
    { en: "Small", mr: "लहान", roman: "Lahān" },
    { en: "Fan", mr: "पंखा", roman: "paMkhA" },
    { en: "Comb", mr: "कंगवा", roman: "kaMgava" },
    { en: "Bath", mr: "आंघोळ", roman: "AMghoL" },
    { en: "Set", mr: "संच", roman: "saMch" },
    { en: "कंछ", mr: "कंछ", roman: "kaMCh" },
    { en: "सांझ", mr: "सांझ", roman: "sAMjh" },
    { en: "Bore", mr: "कंटाळा", roman: "kaMTALA" },
    { en: "Dry ginger", mr: "सुंठ", roman: "suMTh" },
    { en: "Pot", mr: "भांडे", roman: "bhAMDe" },
    { en: "Eunuch", mr: "षंढ", roman: "ShaMDh" },
    { en: "Saint", mr: "संत", roman: "saMt" },
    { en: "Gradual", mr: "संथ", roman: "saMth" },
    { en: "Close", mr: "बंद", roman: "baMd" },
    { en: "Joint", mr: "सांधा", roman: "sAMdhA" },
    { en: "To them", mr: "त्यांना", roman: "tyAMnA" },
    { en: "Pump", mr: "पंप", roman: "paMp" },
    { en: "अंफ", mr: "अंफ", roman: "aMph" },
    { en: "Start", mr: "आरंभ", roman: "AraMbh" },
    { en: "Approval", mr: "संमती", roman: "saMmatI" },
    { en: "Part", mr: "अंश", roman: "aMsh" },
    { en: "Term", mr: "संज्ञा", roman: "saMdnyA" },
    { en: "Patience", mr: "संयम", roman: "saMyam" },
    { en: "Dialogue", mr: "संवाद", roman: "saMvAd" },
    { en: "Part", mr: "पार्ट", roman: "pArT" },
    { en: "Harp", mr: "हार्प", roman: "hArp" },
    { en: "Support", mr: "साह्य", roman: "sAhy" },
    { en: "External", mr: "बाह्य", roman: "bAhy" },
    { en: "Brahman", mr: "ब्राह्मण", roman: "brAhmaN" },
    { en: "A ritual", mr: "आह्निक", roman: "Ahnik" },
    { en: "We", mr: "आम्ही", roman: "AmhI" },
    { en: "You (singular)", mr: "तू", roman: "tU" },
    { en: "You (plural)", mr: "तुम्ही", roman: "tumhI" },
    { en: "He / That (m.)", mr: "तो", roman: "to" },
    { en: "She / That (f.)", mr: "ती", roman: "tI" },
    { en: "It / That (n.)", mr: "ते", roman: "te" },
    { en: "They (Plural of She) / Those (f.)", mr: "त्या", roman: "tyA" },
    { en: "These (f.)", mr: "ह्या", roman: "hyA" },
    { en: "Self", mr: "स्वतः", roman: "svataH" },
    { en: "Moon", mr: "चंद्र", roman: "chaMdra" },
    { en: "Sit", mr: "बस", roman: "basa" },
    { en: "Sing", mr: "गा", roman: "gA" },
    { en: "Speak", mr: "बोल", roman: "bola" },
    { en: "Smile", mr: "हस", roman: "has" },
    { en: "Do", mr: "कर", roman: "kar" },
    { en: "Get up", mr: "उठ", roman: "uTh" },
    { en: "Sleep", mr: "झोप", roman: "jhop" },
    { en: "Run", mr: "धाव", roman: "dhAv" },
    { en: "Stop", mr: "थांब", roman: "thAMb" },
    { en: "Open", mr: "उघड", roman: "ughaD" },
    { en: "Close", mr: "बंद कर", roman: "baMd kar" },
    { en: "See", mr: "बघ", roman: "bagh" },
    { en: "I (male)", mr: "मी", roman: "to" },
    { en: "They (f.) / Those (f.) / These (f.)", mr: "त्या / ह्या", roman: "tAt" },
    { en: "I (male) do", mr: "मी करतो", roman: "mI karato" },
    { en: "I (female) do", mr: "मी करते", roman: "mI karate" },
    { en: "We dance", mr: "आम्ही/आपण नाचतो", roman: "AmhI/ApaN nAchato" },
    { en: "You (male) cry", mr: "तू रडतोस", roman: "tU raDatos" },
    { en: "You (female) cry", mr: "तू रडतेस", roman: "tU raDates" },
    { en: "You (plural) walk", mr: "तुम्ही चालता", roman: "tumhI chAlatA" },
    { en: "He walks", mr: "तो चालतो", roman: "to chAlato" },
    { en: "She speaks", mr: "ती बोलते", roman: "tI bolate" },
    { en: "It moves", mr: "ते हलते", roman: "te halate" },
    { en: "They dance", mr: "ते/त्या/ती नाचतात", roman: "te/tyA/tI nAchatAt" },
    { en: "I shall be doing.", mr: "मी करत असेन", roman: "mI karat asen" },
    { en: "We will be dancing.", mr: "आम्ही/आपण नाचत असू", roman: "AmhI/ApaN nAchat asU" },
    { en: "You will be crying.", mr: "तू रडत असशील", roman: "tU raDat asashIl" },
    { en: "You (pl.) will be walking.", mr: "तुम्ही चालत असाल", roman: "tumhI chAlat asAl" },
    { en: "He will be walking.", mr: "तो चालत असेल", roman: "to chAlat asel" },
    { en: "She will be speaking.", mr: "ती बोलत असेल", roman: "tI bolat asel" },
    { en: "It will be moving.", mr: "ते हलत असेल", roman: "te halat asel" },
    { en: "They will be dancing.", mr: "ते/त्या/ती नाचत असतील", roman: "te/tyA/tI nAchat asatIl" },
    { en: "They (f.) / Those (f.) / These (f.)", mr: "त्या / त्या / ह्या", roman: "lyA" },
    { en: "You (singular/plural)", mr: "तू / तुम्ही", roman: "tU / tumhI" },
    { en: "They (all)", mr: "ते / त्या / ती", roman: "tyAMnI / hyAMnI" },
    { en: "I (male) was doing.", mr: "मी करत होतो", roman: "mI karat hoto" },
    { en: "I (female) was doing.", mr: "मी करत होते", roman: "mI karat hote" },
    { en: "We were dancing.", mr: "आम्ही/आपण नाचत होतो", roman: "AmhI/ApaN nAchat hoto" },
    { en: "You (male) were crying.", mr: "तू रडत होतास", roman: "tU raDat hotAs" },
    { en: "You (female) were crying.", mr: "तू रडत होतीस", roman: "tU raDat hotIs" },
    { en: "You (Plural) were walking", mr: "तुम्ही चालत होता", roman: "tumhI chAlat hotA" },
    { en: "He was walking.", mr: "तो चालत होता", roman: "to chAlat hotA" },
    { en: "She was speaking.", mr: "ती बोलत होती", roman: "tI bolat hotI" },
    { en: "It was moving.", mr: "ते हलत होते", roman: "te halat hote" },
    { en: "They(m.) were dancing.", mr: "ते नाचत होते", roman: "te nAchat hote" },
    { en: "They(f.) were dancing.", mr: "त्या नाचत होत्या", roman: "tyA nAchat hotyA" },
    { en: "They(n.) were dancing.", mr: "ती नाचत होती", roman: "tI nAchat hotI" },
    { en: "She has opened door", mr: "तीने दरवाजा उघडला आहे", roman: "tIne daravAjA ughaDalA Ahe" },
    { en: "She had opened door", mr: "तीने दरवाजा उघडला होता", roman: "tIne daravAjA ughaDalA hotA" },
    { en: "She will have opened door", mr: "तीने दरवाजा उघडला असेल", roman: "tIne daravAjA ughaDalA asel" },
    { en: "You (female) have danced", mr: "तू नाचली आहेस", roman: "tU nAchalI Ahes" },
    { en: "You (female) had danced", mr: "तू नाचली होतीस", roman: "tU nAchalI hotIs" },
    { en: "You (female) will have danced", mr: "तू नाचली असशील", roman: "tU nAchalI asashIl" },
    { en: "You (plural) have danced", mr: "तुम्ही नाचला आहात", roman: "tumhI nAchalA AhAt" },
    { en: "You (plural) had danced", mr: "तुम्ही नाचला होतात", roman: "tumhI nAchalA hotAt" },
    { en: "You (plural) will have danced", mr: "तुम्ही नाचला असाल", roman: "tumhI nAchalA asAl" },
    { en: "These (male/female/neuter)", mr: "हे / ह्या / ही", roman: "hyAMchyA / hyAM" },
    { en: "about", mr: "बद्दल", roman: "baddal" },
    { en: "Above", mr: "वर", roman: "var" },
    { en: "across", mr: "पलिकडे", roman: "palikaDe" },
    { en: "after", mr: "नंतर", roman: "naMtar" },
    { en: "against", mr: "विरुद्ध", roman: "viruddh" },
    { en: "Among", mr: "मध्ये", roman: "madhye" },
    { en: "Around", mr: "भोवती", roman: "bhovatI" },
    { en: "As/like", mr: "सारखा", roman: "sArakhA" },
    { en: "aside", mr: "बाजुला", roman: "bAjulA" },
    { en: "Before", mr: "आधी", roman: "AdhI" },
    { en: "below", mr: "खाली", roman: "khAlI" },
    { en: "for", mr: "साठी", roman: "sAThI" },
    { en: "From/since", mr: "पासून / कडून", roman: "pAsUn / kaDUn" },
    { en: "in", mr: "आत", roman: "At" },
    { en: "outside", mr: "बाहेर", roman: "bAher" },
    { en: "till/until", mr: "पर्यंत", roman: "paryaMt" },
    { en: "without", mr: "शिवाय", roman: "shivAy" },
    { en: "during", mr: "दरम्यान", roman: "daramyAn" },
    { en: "towards", mr: "दिशेने", roman: "dishene" },
    { en: "with", mr: "सोबत / बरोबर", roman: "sobat / barobar" },
    { en: "On behalf of", mr: "वतीने", roman: "vatIne" },
    { en: "In front of", mr: "समोर", roman: "samor" },
    { en: "Prior to", mr: "पूर्वी", roman: "pUrvI" },
    { en: "Because of", mr: "मुळे", roman: "muLe" },
    { en: "According to", mr: "अनुसार / प्रमाणे", roman: "anusAr / pramANe" },
    { en: "Through", mr: "मधून", roman: "madhUn" },
    { en: "With", mr: "शी", roman: "shI" },
    { en: "These (male/female/neuter)", mr: "हे/ह्या/ही", roman: "hyAMnA" },
    { en: "I do not speak", mr: "मी बोलत नाही", roman: "mI bolat nAhI" },
    { en: "He does not walk", mr: "तो चालत नाही", roman: "to chAlat nAhI" },
    { en: "They do not dance", mr: "ते नाचत नाहीत", roman: "te nAchat nAhIt" },
    { en: "I am not speaking", mr: "मी बोलत नाही आहे", roman: "mI bolat nAhI Ahe" },
    { en: "He is not walking", mr: "तो चालत नाही आहे", roman: "to chAlat nAhI Ahe" },
    { en: "She is not speaking", mr: "ती बोलत नाही आहे", roman: "tI bolat nAhI Ahe" },
    { en: "It is not moving", mr: "ते हलत नाही आहे", roman: "te halat nAhI Ahe" },
    { en: "They are not dancing", mr: "ते/त्या/ती नाचत नाही आहेत", roman: "te/tyA/tI nAchat nAhI Ahet" },
    { en: "You are not dancing", mr: "तू नाचत नाही आहेस", roman: "tU nAchat nAhI Ahes" },
    { en: "I have not opened the box", mr: "मी खोका उघडला नाही आहे", roman: "mI khokA ughaDalA nAhI Ahe" },
    { en: "I have not spoken", mr: "मी बोललो नाही आहे", roman: "mI bolalo nAhI Ahe" },
    { en: "You speak", mr: "तू बोल", roman: "tU bol" },
    { en: "Do it", mr: "हे कर", roman: "he kar" },
    { en: "You give", mr: "तू दे", roman: "tU de" },
    { en: "You do not speak", mr: "तू बोलू नकोस", roman: "tU bolU nakos" },
    { en: "Do not do it", mr: "हे करू नकोस", roman: "he karU nakos" },
    { en: "To wash धूणे (dhUNe)", mr: "धू", roman: "dhU" },
    { en: "To give देणे (deNe)", mr: "दे", roman: "de" },
    { en: "To take घेणे (gheNe)", mr: "घे", roman: "ghe" },
    { en: "To live राहणे (rAhaNe)", mr: "रहा", roman: "rahA" },
    { en: "To see पाहणे (pAhaNe)", mr: "पहा", roman: "pahA" },
    { en: "Toy moved", mr: "खेळणे हलले", roman: "kheLaNe halale" },
    { en: "I moved toy", mr: "मी खेळणे हलवले", roman: "mI kheLaNe halavale" },
    { en: "To cook", mr: "शिजणे", roman: "shijaNe" },
    { en: "To cause to cook", mr: "शिजवणे", roman: "shijavaNe" },
    { en: "To die", mr: "मरणे", roman: "maraNe" },
    { en: "To cause to die / To kill", mr: "मारणे", roman: "mAraNe" },
    { en: "To fall", mr: "पडणे", roman: "paDaNe" },
    { en: "To cause to fall", mr: "पाडणे", roman: "pADaNe" },
    { en: "To break (intransitive)", mr: "फुटणे", roman: "phuTaNe" },
    { en: "To cause to break", mr: "फोडणे", roman: "phoDaNe" },
    { en: "Glass broke", mr: "ग्लास फुटला", roman: "glAs phuTalA" },
    { en: "I broke glass", mr: "मी ग्लास फोडला", roman: "mI glAs phoDalA" },
    { en: "To leave", mr: "सुटणे", roman: "suTaNe" },
    { en: "To cause to leave", mr: "सोडणे", roman: "soDaNe" },
    { en: "To feed", mr: "भरवणे", roman: "bharavaNe" },
    { en: "To speak", mr: "बोलणे", roman: "bolaNe" },
    { en: "To call (not cause to speak)", mr: "बोलवणे", roman: "bolavaNe" },
    { en: "To run", mr: "पळणे", roman: "paLaNe" },
    { en: "my", mr: "माझा", roman: "mAjhA" },
    { en: "speaking", mr: "बोलणारा", roman: "bolaNArA" },
    { en: "want", mr: "हवा", roman: "havA" },
    { en: "grey", mr: "करडा", roman: "karaDA" },
    { en: "how / what kind (कसा)", mr: "कसा-कशी-कसे-कसे-कश्या-कशी", roman: "kasA-kashI-kase-kase-kashyA-kashI" },
    { en: "my", mr: "माझा-माझी-माझे-माझे-माझ्या-माझी", roman: "mAjhA-mAjhI-mAjhe-mAjhe-mAjhyA-mAjhI" },
    { en: "your", mr: "तुझा-तुझी-तुझे-तुझे-तुझ्या-तुझी", roman: "tujhA-tujhI-tujhe-tujhe-tujhyA-tujhI" },
    { en: "Ram's", mr: "रामचा-रामची-रामचे-रामचे-रामच्या-रामची", roman: "rAmachA-rAmachI-rAmache-rAmache-rAmachyA-rAmachI" },
    { en: "fresh", mr: "ताजा-ताजी-ताजे-ताजे-ताज्या-ताजी", roman: "tAjA-tAjI-tAje-tAje-tAjyA-tAjI" },
    { en: "I had spoken", mr: "मी बोललेलो", roman: "mI bolalelo" },
    { en: "You (male) had danced", mr: "तू नाचलेलास", roman: "tU nAchalelAs" },
    { en: "He had laughed", mr: "तो हसलेला", roman: "to hasalelA" },
    { en: "Those boys had laughed", mr: "ते मुलगे हसलेले", roman: "te mulage hasalele" },
    { en: "I had opened door", mr: "मी दरवाजा उघडलेला", roman: "mI daravAjA ughaDalelA" },
    { en: "Those girls had picked keys", mr: "त्या मुलींनी किल्ल्या उचललेल्या", roman: "tyA mulIMnI killyA uchalalelyA" },
    { en: "I have spoken", mr: "मी बोललेलो आहे", roman: "mI bolalelo Ahe" },
    { en: "I will have spoken", mr: "मी बोललेलो असेन", roman: "mI bolalelo asen" },
    { en: "He had been saying", mr: "तो बोलत होता", roman: "to bolat hotA" },
    { en: "He has been saying", mr: "तो बोलत आहे", roman: "to bolat Ahe" },
    { en: "He will have been saying", mr: "तो बोलत असेल", roman: "to bolat asel" },
    { en: "I have been saying", mr: "मी बोलत आलो आहे", roman: "mI bolat Alo Ahe" },
    { en: "She has been saying", mr: "ती बोलत आली आहे", roman: "tI bolat AlI Ahe" },
    { en: "They have been dancing", mr: "ते नाचत आले आहेत", roman: "te nAchat Ale Ahet" },
    { en: "I had been saying", mr: "मी बोलत आलो होतो", roman: "mI bolat Alo hoto" },
    { en: "She had been saying", mr: "ती बोलत आली होती", roman: "tI bolat AlI hotI" },
    { en: "They had been dancing", mr: "ते नाचत आले होते", roman: "te nAchat Ale hote" },
    { en: "She will have been saying", mr: "ती बोलत आली असेल", roman: "tI bolat AlI asel" },
    { en: "They will have been dancing", mr: "ते नाचत आले असतील", roman: "te nAchat Ale asatIl" },
    { en: "I used to do", mr: "मी करायचो", roman: "mI karAyacho" },
    { en: "She used to speak", mr: "ती बोलायची", roman: "tI bolAyachI" },
    { en: "He used to dance", mr: "तो नाचायचा", roman: "to nAchAyachA" },
    { en: "They (plural of she) used to play cricket", mr: "त्या क्रिकेट खेळायच्या", roman: "tyA krikeT kheLAyachyA" },
    { en: "He used to be there", mr: "तो तिकडे असायचा", roman: "to tikaDe asAyachA" },
    { en: "She used to be quiet", mr: "ती शांत असायची", roman: "tI shAMt asAyachI" },
    { en: "I did not use to do", mr: "मी करायचो नाही", roman: "mI karAyacho nAhI" },
    { en: "She did not use to speak", mr: "ती बोलायची नाही", roman: "tI bolAyachI nAhI" },
    { en: "You did not use to dance", mr: "तू नाचायचा नाहीस", roman: "tU nAchAyachA nAhIs" },
    { en: "She did not use to be quiet", mr: "ती शांत असायची नाही", roman: "tI shAMt asAyachI nAhI" },
    { en: "He did not use to be there", mr: "तो तिकडे नसायचा", roman: "to tikaDe nasAyachA" },
    { en: "She did not use to be quiet", mr: "ती शांत नसायची", roman: "tI shAMt nasAyachI" },
    { en: "He is used to dance", mr: "तो नाचत असतो", roman: "to nAchat asato" },
    { en: "She is used to speak", mr: "ती बोलत असते", roman: "tI bolat asate" },
    { en: "Those girls are used to laugh", mr: "त्या मुली हसत असतात", roman: "tyA mulI hasat asatAt" },
    { en: "I am used to be there", mr: "मी तिकडे असतो", roman: "mI tikaDe asato" },
    { en: "She is used to be quiet", mr: "ती शांत असते", roman: "tI shAMt asate" },
    { en: "He is not used to dance", mr: "तो नाचत नसतो", roman: "to nAchat nasato" },
    { en: "She is not used to speak", mr: "ती बोलत नसते", roman: "tI bolat nasate" },
    { en: "I used to see", mr: "मी बघे/बघी", roman: "mI baghe/baghI" },
    { en: "I used to do", mr: "मी करे/करी", roman: "mI kare/karI" },
    { en: "He opened the door", mr: "त्याने दार उघडले", roman: "tyAne dAr ughaDale" },
    { en: "If he had opened the door then", mr: "त्याने दार उघडले असते तर", roman: "tyAne dAr ughaDale asate tar" },
    { en: "He had spoken", mr: "तो बोलला होता", roman: "to bolalA hotA" },
    { en: "If he had spoken", mr: "तो बोलला असता तर", roman: "to bolalA asatA tar" },
    { en: "If you had spoken then she would have spoken", mr: "जर तू बोलला असतास तर ती बोलली असती", roman: "jar tU bolalA asatAs tar tI bolalI asatI" },
    { en: "If he had cried then they would have ran", mr: "जर तो रडला असता तर ते धावले असते", roman: "jar to raDalA asatA tar te dhavale asate" },
    { en: "If he sings she will dance", mr: "तो गायला तर ती नाचेल", roman: "to gAyalA tar tI nAchel" },
    { en: "do", mr: "कर (kar)", roman: "karaNyA" },
    { en: "speak", mr: "बोल (bol)", roman: "bolaNyA" },
    { en: "dance", mr: "नाच (nAch)", roman: "nAchaNyA" },
    { en: "About speaking", mr: "बोलण्याबद्दल", roman: "bolaNyAbaddal" },
    { en: "reason of coming", mr: "येण्याचे कारण", roman: "yeNyAche kAraN" },
    { en: "She spoke after my dancing", mr: "माझ्या नाचण्यानंतर ती गायली", roman: "mAjhyA nAchaNyAnaMtar tI gAyalI" },
    { en: "after I danced", mr: "नाचल्यानंतर", roman: "nAchalyAnaMtar" },
    { en: "She spoke after I danced", mr: "मी नाचल्यानंतर ती बोलली", roman: "mI nAchalyAnaMtar tI bolalI" },
    { en: "He cried after she went", mr: "ती गेल्यानंतर तो रडला", roman: "tI gelyAnaMtar to raDalA" },
    { en: "He told me that he is coming", mr: "तो शाळेत येत असल्याचे त्याने मला सांगितले", roman: "to shALet yet asalyAche tyAne malA sAMgitale" },
    { en: "to see", mr: "बघायला", roman: "baghAyalA" },
    { en: "to do", mr: "करायला", roman: "karAyalA" },
    { en: "to speak", mr: "बोलायला", roman: "bolAyalA" },
    { en: "to dance", mr: "नाचायला", roman: "nAchAyalA" },
    { en: "to see", mr: "बघण्यास", roman: "baghaNyAs" },
    { en: "to do", mr: "करण्यास", roman: "karaNyAs" },
    { en: "to speak", mr: "बोलण्यास", roman: "bolaNyAs" },
    { en: "to dance", mr: "नाचण्यास", roman: "nAchaNyAs" },
    { en: "Sit and watch", mr: "बसून बघ", roman: "basUn bagh" },
    { en: "He came and saw it", mr: "त्याने येऊन बघितले", roman: "tyAne yeUn baghitale" },
    { en: "smile and say", mr: "हसून बोल", roman: "hasoon bol" },
    { en: "till I speak", mr: "मी बोले पर्यंत", roman: "mI bole paryaMt" },
    { en: "until she smiles", mr: "ती हसे पर्यंत", roman: "tI hase paryaMt" },
    { en: "Black horse", mr: "काळा घोडा", roman: "kALA ghoDA" },
    { en: "Black horses", mr: "काळे घोडे", roman: "kALe ghoDe" },
    { en: "Easy exam", mr: "सोपी परीक्षा", roman: "sopI parIkShA" },
    { en: "After easy exam", mr: "सोप्या परीक्षेनंतर", roman: "sopyA parIkShenaMtar" },
    { en: "Red horse", mr: "लाल घोडा", roman: "lAl ghoDA" },
    { en: "For red horse", mr: "लाल घोड्यासाठी", roman: "lAl ghoDyAsAThI" },
    { en: "Beautiful drawing", mr: "सुंदर चित्र", roman: "suMdar chitr" },
    { en: "About beautiful drawing", mr: "सुंदर चित्राबद्दल", roman: "suMdar chitrAbaddal" },
    { en: "Talking boy", mr: "बोलणारा मुलगा", roman: "bolaNArA mulagA" },
    { en: "Rotating fan", mr: "फिरणारा पंखा", roman: "phiraNArA paMkhA" },
    { en: "Talking girl", mr: "बोलणारी मुलगी", roman: "bolaNArI mulagI" },
    { en: "Flying saucer", mr: "उडणारी तबकडी", roman: "uDaNArI tabakaDI" },
    { en: "Talked boy", mr: "बोललेला मुलगा", roman: "bolalelA mulagA" },
    { en: "Rotated fan", mr: "फिरलेला पंखा", roman: "phiralelA paMkhA" },
    { en: "Talked girl", mr: "बोललेली मुलगी", roman: "bolalelI mulagI" },
    { en: "Flown saucer", mr: "उडलेली तबकडी", roman: "uDalelI tabakaDI" },
    { en: "He can sing", mr: "तो गाऊ शकतो", roman: "to gAU shakato" },
    { en: "She could dance", mr: "ती नाचू शकली", roman: "tI nAchU shakalI" },
    { en: "They (plural of she) will be able to move", mr: "त्या हलू शकतील", roman: "tyA halU shakatIl" },
    { en: "He can not sing", mr: "तो गाऊ शकत नाही", roman: "to gAU shakat nAhI" },
    { en: "She could not dance", mr: "ती नाचू शकली नाही", roman: "tI nAchU shakalI nAhI" },
    { en: "They will not be able to move", mr: "त्या हलू शकणार नाहीत", roman: "tyA halU shakaNAr nAhIt" },
    { en: "I can play cricket", mr: "मला क्रिकेट खेळायला जमते", roman: "malA krikeT kheLAyalA jamate" },
    { en: "I could play cricket", mr: "मला क्रिकेट खेळायला जमले", roman: "malA krikeT kheLAyalA jamale" },
    { en: "I will be able to play cricket", mr: "मला क्रिकेट खेळायला जमेल", roman: "malA krikeT kheLAyalA jamel" },
    { en: "They could open box", mr: "त्यांना खोका उघडायला जमला", roman: "tyAMnA khokA ughaDAyalA jamalA" },
    { en: "They could open bag", mr: "त्यांना पेटी उघडायला जमली", roman: "tyAMnA peTI ughaDAyalA jamalI" },
    { en: "They could speak", mr: "त्यांना बोलायला जमले", roman: "tyAMnA bolAyalA jamale" },
    { en: "They gathered to speak", mr: "ते बोलायला जमले", roman: "te bolAyalA jamale" },
    { en: "He/She/They want chalk", mr: "त्याला/तीला/त्यांना खडू पाहिजे/हवा आहे", roman: "tyAlA/tIlA/tyAMnA khaDU pahije/havA Ahe" },
    { en: "He/She/They want chalks", mr: "त्याला/तीला/त्यांना खडू पाहिजे/हवे आहेत", roman: "tyAlA/tIlA/tyAMnA khaDU pahije/have Ahet" },
    { en: "He/She/They want bag", mr: "त्याला/तीला/त्यांना पेटी पाहिजे/हवी आहे", roman: "tyAlA/tIlA/tyAMnA peTI pahije/havI Ahe" },
    { en: "He/She/They want bags", mr: "त्याला/तीला/त्यांना पेट्या पाहिजे/हव्या आहेत", roman: "tyAlA/tIlA/tyAMnA peTyA pahije/havyA Ahet" },
    { en: "He/She/They wanted chalk", mr: "त्याला/तीला/त्यांना खडू पाहिजे/हवा होता", roman: "tyAlA/tIlA/tyAMnA khaDU pahije/havA hotA" },
    { en: "He/She/They wanted chalks", mr: "त्याला/तीला/त्यांना खडू पाहिजे/हवे होते", roman: "tyAlA/tIlA/tyAMnA khaDU pahije/have hote" },
    { en: "He/She/They wanted bag", mr: "त्याला/तीला/त्यांना पेटी पाहिजे/हवी होती", roman: "tyAlA/tIlA/tyAMnA peTI pahije/havI hotI" },
    { en: "He/She/They wanted bags", mr: "त्याला/तीला/त्यांना पेट्या पाहिजे/हव्या होत्या", roman: "tyAlA/tIlA/tyAMnA peTyA pahije/havyA hotyA" },
    { en: "He/She/They will need chalk", mr: "त्याला/तीला/त्यांना खडू पाहिजे/हवा असेल", roman: "tyAlA/tIlA/tyAMnA khaDU pahije/havA asel" },
    { en: "He/She/They will need chalks", mr: "त्याला/तीला/त्यांना खडू पाहिजे/हवे असतील", roman: "tyAlA/tIlA/tyAMnA khaDU pahije/have asatIl" },
    { en: "He/She/They will need bag", mr: "त्याला/तीला/त्यांना पेटी पाहिजे/हवी असेल", roman: "tyAlA/tIlA/tyAMnA peTI pahije/havI asel" },
    { en: "He/She/They will need bags", mr: "त्याला/तीला/त्यांना पेट्या पाहिजे/हव्या असतील", roman: "tyAlA/tIlA/tyAMnA peTyA pahije/havyA asatIl" },
    { en: "She will not want bag", mr: "तीला पेटी नको असेल", roman: "tIlA peTI nako asel" },
    { en: "He did not want chalk", mr: "त्याला खडू नको होता", roman: "tyAlA khaDU nako hotA" },
    { en: "He did not want bag", mr: "त्याला पेटी नको होती", roman: "tyAlA peTI nako hotI" },
    { en: "She does not want ice cream", mr: "तीला आईसक्रीम नाही पाहिजे", roman: "tIlA AIskrIm nAhI pAhije" },
    { en: "He did not want chalk", mr: "त्याला खडू नाही पाहिजे होता", roman: "tyAlA khaDU nAhI pAhije hotA" },
    { en: "What happened?", mr: "काय झाले?", roman: "kAy jhAle?" },
    { en: "What will happen?", mr: "काय होईल?", roman: "kAy hoIl?" },
    { en: "What is happening?", mr: "काय होत आहे?", roman: "kAy hot Ahe?" },
    { en: "It did not happen", mr: "हे झाले नाही", roman: "he jhAle nAhI" },
    { en: "It was happening", mr: "ते होत होते", roman: "te hot hote" },
    { en: "I should speak", mr: "मी बोलायला पाहिजे", roman: "mI bolAyalA pAhije" },
    { en: "I should have spoken", mr: "मी बोलायला पाहिजे होते", roman: "mI bolAyalA pAhije hote" },
    { en: "They should dance", mr: "त्यांनी नाचायला पाहिजे", roman: "tyAMnI nAchAyalA pAhije" },
    { en: "They should not dance", mr: "त्यांनी नाचायला नाही पाहिजे", roman: "tyAMnI nAchAyalA nAhI pAhije" },
    { en: "They should have danced", mr: "त्यांनी नाचायला पाहिजे होते", roman: "tyAMnI nAchAyalA pAhije hote" },
    { en: "They should not have danced", mr: "त्यांनी नाचायला नाही पाहिजे होते", roman: "tyAMnI nAchAyalA nAhI pAhije hote" },
    { en: "You should play", mr: "तू खेळायला पाहिजे/पाहिजेस", roman: "tU kheLAyalA pAhije/pAhijes" },
    { en: "You should not play", mr: "तू खेळायला नाही पाहिजे/पाहिजेस", roman: "tU kheLAyalA nAhI pAhije/pAhijes" },
    { en: "You should have played", mr: "तू खेळायला पाहिजे होतेस", roman: "tU kheLAyalA pAhije hotes" },
    { en: "You should not have smiled", mr: "तू हसायला नाही पाहिजे होतेस", roman: "tU hasAyalA nAhI pAhije hotes" },
    { en: "They should not dance", mr: "त्यांनी नाचायला नको", roman: "tyAMnI nAchAyalA nako" },
    { en: "They should not have danced", mr: "त्यांनी नाचायला नको होते", roman: "tyAMnI nAchAyalA nako hote" },
    { en: "You should not have smiled", mr: "तू हसायला नको होतेस", roman: "tU hasAyalA nako hotes" },
    { en: "She should open box", mr: "तीने पेटी उघडली पाहिजे", roman: "tIne peTI ughaDalI pAhije" },
    { en: "She should not open box", mr: "तीने पेटी उघडली नाही पाहिजे", roman: "tIne peTI ughaDalI nAhI pAhije" },
    { en: "We have to speak", mr: "आम्हाला बोलावे लागते", roman: "AmhAlA bolAve lAgate" },
    { en: "I keep speaking", mr: "मी बोलत राहतो", roman: "mI bolat rAhato" },
    { en: "I kept speaking", mr: "मी बोलत राहिलो", roman: "mI bolat rAhilo" },
    { en: "I will keep speaking", mr: "मी बोलत राहीन", roman: "mI bolat rAhIn" },
    { en: "You keep speaking", mr: "तू बोलत राहतोस", roman: "tU bolat rAhatos" },
    { en: "You kept speaking", mr: "तू बोलत राहिलास", roman: "tU bolat rAhilAs" },
    { en: "You will keep speaking", mr: "तू बोलत राहशील", roman: "tU bolat rAhashIl" },
    { en: "Keep speaking! (Imperative)", mr: "बोलत राहा", roman: "bolat rAhA" },
    { en: "Bitter", mr: "कडू", roman: "kaDU" },
    { en: "More bitter", mr: "जास्त/अधिक कडू", roman: "jAst/adhik kaDU" },
    { en: "Most bitter", mr: "सर्वात/सर्वात जास्त/सर्वाधिक कडू", roman: "sarvAt/sarvAt jAst/sarvAdhik kaDU" },
    { en: "Tall", mr: "उंच", roman: "uMch" },
    { en: "Taller", mr: "जास्त/अधिक उंच", roman: "jAst/adhik uMch" },
    { en: "Tallest", mr: "सर्वात जास्त/सर्वाधिक उंच", roman: "sarvAt jAst/sarvAdhik uMch" },
    { en: "Better", mr: "जास्त/अधिक चांगला", roman: "jAst/adhik chAMgalA" },
    { en: "Best", mr: "सर्वात/सर्वात जास्त/सर्वाधिक चांगला", roman: "sarvAt/sarvAt jAst/sarvAdhik chAMgalA" },
    { en: "He is taller than me", mr: "तो माझ्यापेक्षा जास्त/अधिक उंच आहे", roman: "to mAjhyApekShA jAst/adhik uMch Ahe" },
    { en: "I am shorter than you", mr: "मी तुझ्यापेक्षा बुटका आहे", roman: "mI tujhyApekShA buTakA Ahe" },
    { en: "They were happier than now", mr: "त्या आत्तापेक्षा जास्त/अधिक सुखी होत्या", roman: "tyA AttApekShA jAst/adhik sukhI hotyA" },
    { en: "He is best", mr: "तो सर्वात चांगला आहे", roman: "to sarvAt chAMgalA Ahe" },
    { en: "Everest is the tallest peak", mr: "एव्हरेस्ट सर्वाधिक उंच शिखर आहे", roman: "evharesT sarvAdhik uMch shikhar Ahe" },
    { en: "She was the youngest player", mr: "ती सर्वात लहान खेळाडू होती", roman: "tI sarvAt lahAn kheLADU hotI" },
    { en: "Your voice is loudest of all", mr: "तुझा आवाज सर्वात जास्त मोठा आहे", roman: "tujhA AvAj sarvAt jAst moThA Ahe" },
    { en: "Do you know it?", mr: "तुला हे माहीत आहे का?", roman: "tulA he mAhIt Ahe kA?" },
    { en: "Did she know that?", mr: "तीला हे माहीत होते का?", roman: "tIlA he mAhIt hote kA?" },
    { en: "Don't you know it?", mr: "तुला हे माहीत नाही का?", roman: "tulA he mAhIt nAhI kA?" },
    { en: "Didn't she know that?", mr: "तीला हे माहीत नव्हते का?", roman: "tIlA he mAhIt navhate kA?" },
    { en: "I know swimming", mr: "मला पोहता येते", roman: "malA pohatA yete" },
    { en: "I know Japanese", mr: "मला जपानी येते", roman: "malA japAnI yete" },
    { en: "I know cooking", mr: "मला जेवण बनवता येते", roman: "malA jevaN banavatA yete" },
    { en: "Do you know playing cricket?", mr: "तुला क्रिकेट खेळता येते का?", roman: "tulA krikeT kheLatA yete kA?" },
    { en: "I know killing mosquitoes", mr: "मला डास मारता येतात", roman: "malA DAs mAratA yetAt" },
    { en: "She used to know dancing before", mr: "तीला पूर्वी नाचता यायचे", roman: "tIlA poorvI nAchatA yAyache" },
    { en: "They knew to talk", mr: "त्यांना बोलता यायचे", roman: "tyAMnA bolatA yAyache" },
    { en: "I do not know swimming", mr: "मला पोहता येत नाही", roman: "malA pohatA yet nAhI" },
    { en: "I do not know Japanese", mr: "मला जपानी येत नाही", roman: "malA japAnI yet nAhI" },
    { en: "She did not know dancing before", mr: "तीला पूर्वी नाचता यायचे नाही", roman: "tIlA poorvI nAchatA yAyache nAhI" },
    { en: "They did not know to talk", mr: "त्यांना बोलता यायचे नाही", roman: "tyAMnA bolatA yAyache nAhI" },
    { en: "I(boy) know you", mr: "मी तुला ओळखतो", roman: "mI tulA oLakhato" },
    { en: "I(girl) know you", mr: "मी तुला ओळखते", roman: "mI tulA oLakhate" },
    { en: "You know me", mr: "तू मला ओळखतोस", roman: "tU malA oLakhatos" },
    { en: "He knows Mr. Ram", mr: "तो श्री. राम ना ओळखतो", roman: "to shrI. rAma nA oLakhato" },
    { en: "Let's play", mr: "चला, आपण खेळूया", roman: "chalA, ApaN kheLUyA" },
    { en: "Let's speak", mr: "चला, बोलूया", roman: "chalA, bolUyA" },
    { en: "Let's not play", mr: "आपण नको खेळूया", roman: "ApaN nako kheLUyA" },
    { en: "Let's not speak", mr: "नको बोलूया", roman: "nako bolUyA" },
    { en: "Shall we play cricket? (style 1)", mr: "क्रिकेट खेळूया का?", roman: "krikeT kheLUyA kA?" },
    { en: "Shall we play cricket? (style 2)", mr: "क्रिकेट खेळायचे का?", roman: "krikeT kheLAyAche kA?" },
    { en: "Shall we watch movie? (style 1)", mr: "सिनेमा बघूया का?", roman: "sinemA baghUyA kA?" },
    { en: "Shall we watch movie? (style 2)", mr: "सिनेमा बघायचा का?", roman: "sinemA baghAyachA kA?" },
    { en: "Let her speak", mr: "तीला बोलू दे", roman: "tIlA bolU de" },
    { en: "You all, Let her speak", mr: "तीला बोलू द्या", roman: "tIlA bolU dyA" },
    { en: "You all, don't let her speak", mr: "तीला बोलू देऊ नका", roman: "tIlA bolU deU nakA" },
    { en: "I could not understand what you just said", mr: "तू आत्ता काय म्हणालास ते मला कळले नाही", roman: "tU AttA kAy mhaNAlAs te malA kaLale nAhI" },
    { en: "I could not understand what you just said", mr: "तू आत्ता जे म्हणालास ते मला कळले नाही", roman: "tU AttA je mhaNAlAs te malA kaLale nAhI" },
    { en: "What is in your mind, tell me that", mr: "तुझ्या मनात जे आहे, ते मला सांग", roman: "tujhyA manAt je Ahe, te malA sAMg" },
    { en: "Whenever you call he will answer", mr: "तू जेव्हा जेव्हा फोन करशील तेव्हा तेव्हा तो उत्तर देईल", roman: "tU jevhA jevhA phon karashIl tevhA tevhA to uttar deIl" },
    { en: "Do not smoke here", mr: "धूम्रपान करू नका", roman: "dhoomrapAn karU nakA" },
    { en: "Enter your preferences", mr: "तुमची पसंती भरा", roman: "tumachI pasMtI bharA" },
    { en: "Enter your preference", mr: "तुमची पसंती भरावी", roman: "tumachI pasMtI bharAvI" },
    { en: "Enter your preferences", mr: "तुमच्या पसंती भराव्यात", roman: "tumachyA pasMtI bharAvyAt" },
    { en: "Do not speak", mr: "बोलू नये", roman: "bolU naye" },
    { en: "Do not smoke", mr: "धूम्रपान करू नये", roman: "dhoomrapAn karU naye" },
    { en: "He liked to open bag", mr: "त्याला पेटी उघडायला आवडली", roman: "tyAlA peTI ughaDAyalA AvaDalI" },
    { en: "He liked to open bags", mr: "त्याला पेट्या उघडायला आवडल्या", roman: "tyAlA peTyA ughaDAyalA AvaDalyA" },
    { en: "She will like to sing song", mr: "तीला गाणे गायला आवडेल", roman: "tIlA gANe gAyalA AvaDel" },
    { en: "She will like to sing songs", mr: "तीला गाणी गायला आवडतील", roman: "tIlA gANI gAyalA AvaDatIl" },
    { en: "He did not like to open bag", mr: "त्याला पेटी उघडायला आवडली नाही", roman: "tyAlA peTI ughaDAyalA AvaDalI nAhI" },
    { en: "She will not like to sing song", mr: "तीला गाणे गायला आवडणार नाही", roman: "tIlA gANe gAyalA AvaDaNAr nAhI" },
    { en: "He likes to push me", mr: "त्याला मला ढकलायला आवडते", roman: "tyAlA malA DhakalAyalA AvaDate" },
    { en: "He likes to push her", mr: "त्याला तीला ढकलायला आवडते", roman: "tyAlA tIlA DhakalAyalA AvaDate" },
    { en: "They will like to hold us", mr: "त्यांना आम्हाला धरायला आवडेल", roman: "tyAMnA AmhAlA dharAyalA AvaDel" },
    { en: "I thought I would be late so I would have to run", mr: "मला वाटले मला उशीर होईल म्हणून मला धावावे लागेल", roman: "malA vATale malA ushIr hoIl mhaNUn malA dhAvAve lAgel" },
    { en: "I would not disclose it in any condition", mr: "मी कुठल्याही परिस्थितीत उघड केले नसते", roman: "mI kuThalyAhI paristhitIt ughaD kele nasate" },
    { en: "I understand its importance", mr: "मला याचे महत्व समजते", roman: "malA yAche mahatva samajate" },
    { en: "He understood the logic", mr: "त्याला तत्व समजले", roman: "tyAlA tatva samajale" },
    { en: "She came to know the news", mr: "तीला बातमी समजली/कळली", roman: "tIlA bAtamI samajalI/kaLalI" },
    { en: "They will understand your mistakes", mr: "त्यांना तुझ्या चुका समजतील/कळतील", roman: "tyAMnA tujhyA chukA samajatIl/kaLatIl" },
    { en: "Did you understand?", mr: "तुला कळले/समजले का?", roman: "tulA kaLale/samajale kA?" },
    { en: "She does not understand", mr: "तीला कळत/समजत नाही", roman: "tIlA kaLat/samajat nAhI" },
    { en: "You are coming", mr: "तू येतो आहेस", roman: "tU yeto Ahes" },
    { en: "You are coming, aren't you?", mr: "तू येतो आहेस ना?", roman: "tU yeto Ahes nA?" },
    { en: "She did not speak", mr: "ती बोलली नाही", roman: "tI bolalI nAhI" },
    { en: "She did not speak, did she?", mr: "ती बोलली नाही ना?", roman: "tI bolalI nAhI nA?" },
    { en: "He will do", mr: "तो करेल", roman: "to karel" },
    { en: "He will do, won't he?", mr: "तो करेल ना?", roman: "to karel nA?" },
    { en: "I remember you", mr: "मला तू आठवतोस", roman: "malA tU AThavatos" },
    { en: "You remember me", mr: "तुला मी आठवतो", roman: "tulA mI AThavato" },
    { en: "We remember Mary", mr: "आम्हाला मेरी आठवते", roman: "AmhAlA merI AThavate" },
    { en: "Mary remembers us", mr: "मेरीला आम्ही आठवतो", roman: "merIlA AmhI AThavato" },
    { en: "I remember you (लक्षात)", mr: "तू माझ्या लक्षात आहेस", roman: "tU mAjhyA lakShAt Ahes" },
    { en: "You remember me (लक्षात)", mr: "मी तुझ्या लक्षात आहे", roman: "mI tujhyA lakShAt Ahe" },
    { en: "I remember you (miss)", mr: "मला तुझी आठवण येते", roman: "malA tujhI AThavaN yete" },
    { en: "You remember me", mr: "तुला माझी आठवण येते", roman: "tulA mAjhI AThavaN yete" },
    { en: "Mary remembered us", mr: "मेरीला आमची आठवण आली", roman: "merIlA AmachI AThavaN AlI" },
    { en: "I will remember your favor", mr: "मी तुझे उपकार लक्षात ठेवीन", roman: "mI tujhe upakAr lakShAt ThevIn" },
    { en: "He always remembered my advice", mr: "त्याने माझा सल्ला नेहमी लक्षात ठेवला", roman: "tyAne mAjhA sallA nehamI lakShAt ThevalA" },
    { en: "He wanted to open bag", mr: "त्याला पेटी उघडायची होती", roman: "tyAlA peTI ughaDAyachI hotI" },
    { en: "He wanted to open bags", mr: "त्याला पेट्या उघडायच्या होत्या", roman: "tyAlA peTyA ughaDAyachyA hotyA" },
    { en: "She will want to sing song", mr: "तीला गाणे गायचे असेल", roman: "tIlA gANe gAyache asel" },
    { en: "She will want to sing songs", mr: "तीला गाणी गायची असतील", roman: "tIlA gANI gAyachI asatIl" },
    { en: "I will want to run", mr: "मला धावायचे असेल", roman: "malA dhAvAyache asel" },
    { en: "He did not want to open bag", mr: "त्याला पेटी उघडायची नव्हती", roman: "tyAlA peTI ughaDAyachI navhtI" },
    { en: "She will not want to sing song", mr: "तीला गाणे गायचे नसेल", roman: "tIlA gANe gAyache nasel" },
    { en: "I am supposed to finish that bottle", mr: "मी ती बाटली संपवायची आहे", roman: "mI tI bATalI saMpavAyachI Ahe" },
    { en: "He is supposed to finish that bottle", mr: "त्याने ती बाटली संपवायची आहे", roman: "tyAne tI bATalI saMpavAyachI Ahe" },
    { en: "She is supposed to finish that bottle", mr: "तीने ती बाटली संपवायची आहे", roman: "tIne tI bATalI saMpavAyachI Ahe" },
    { en: "I/He/She was supposed to finish that bottle", mr: "मी/त्याने/तीने ती बाटली संपवायची होती", roman: "mI/tyAne/tIne tI bATalI saMpavAyachI hotI" },
    { en: "I/He/She was supposed to finish those bottles", mr: "मी/त्याने/तीने त्या बाटल्या संपवायच्या होत्या", roman: "mI/tyAne/tIne tyA bATalyA saMpavAyachyA hotyA" },
    { en: "I get a prize", mr: "मला बक्षिस मिळते", roman: "malA bakShis miLate" },
    { en: "I get 10 prizes", mr: "मला १० बक्षिसे मिळतात", roman: "malA 10 bakShise miLatAt" },
    { en: "He gets a prize", mr: "त्याला बक्षिस मिळते", roman: "tyAlA bakShis miLate" },
    { en: "He gets 10 prizes", mr: "त्याला १० बक्षिसे मिळतात", roman: "tyAlA 10 bakShise miLatAt" },
    { en: "I found my wallet under the bed", mr: "मला माझे पाकीट दिवाणाखाली सापडले", roman: "malA mAjhe pAkIT divANAkhAlI sApaDale" },
    { en: "She became angry", mr: "तिला राग आला", roman: "tIlA rAg AlA" },
    { en: "He became angry", mr: "त्याला राग आला", roman: "tyAlA rAg AlA" },
    { en: "He agrees to these conditions", mr: "त्याला ह्या अटी मान्य आहेत", roman: "tyAlA hyA aTI mAny Ahet" },
    { en: "Do not hesitate. Speak it out", mr: "संकोच करू नकोस. बोलून टाक", roman: "saMkoch karU nakos. bolUn TAk" },
    { en: "I somehow managed to gulp it", mr: "मी कसाबसा गिळून टाकला", roman: "mI kasAbasA giLUn TAkalA" },
    { en: "Ask whatever you want; right now", mr: "तुला काय विचारायचे आहे ते आत्ताच विचारून घे", roman: "tulA kAy vichArAyache Ahe te AttAch vichArUn ghe" },
    { en: "You may call me whatever you want", mr: "तुला हवं ते तू बोलून घे", roman: "tulA havM te tU bolUn ghe" },
    { en: "I washed clothes very hard", mr: "मी कपडे धुवून काढले", roman: "mI kapaDe dhuvUn kADhale" },
    { en: "Now keep crying", mr: "आता रडत बस", roman: "AtA raDat bas" },
    { en: "She could not see the sign", mr: "पाटी बघायची राहिली", roman: "pATI baghAyachI rAhilI" },
    { en: "Start following my advice", mr: "माझे ऐकत जा", roman: "mAjhe aikat jA" },
    { en: "I was about to open the door when I saw", mr: "मी दरवाजा उघडायला गेलो तेवढ्यात मला पोलिस दिसले", roman: "mI daravAjA ughaDAyalA gelo tevaDhyAt malA polis disale" },
    { en: "If he decides to take revenge", mr: "जर त्याने सूड घ्यायचा म्हटला तर कोणीही त्याला थांबवू शकत नाही", roman: "jar tyAne sUD ghyAyachA mhaTalA tar koNIhI tyAlA thAMbavU shakat nAhI" },
    { en: "He happened to say he was from India", mr: "त्याच्या बोलण्यात आले की तोही भारतामधील आहे", roman: "tyAchyA bolaNyAt Ale kI tohI bhAratAmadhIl Ahe" },
    { en: "Really!", mr: "खरंच!", roman: "kharaMch" },
    { en: "How big!", mr: "अबब! किती मोठा", roman: "ababa! kitI moThA" },
    { en: "Nice smell / Very tasty", mr: "अहाहा!", roman: "ahAhA!" },
    { en: "Very bad", mr: "ओहो! वाईट झालं", roman: "oho! vAIT jhAlaM" },
    { en: "Oh! He failed!", mr: "अरे बापरे! तो नापास झाला", roman: "are baapare! to nApAs jhAlA" },
    { en: "No! He will never do it", mr: "छे! तो कधीही असं करणार नाही", roman: "Che! to kadhIhI asaM karaNAr nAhI" },
    { en: "No! I do not believe", mr: "छट! मझा नाही विश्वास", roman: "ChaT! majhA nAhI vishvAs" },
    { en: "Excellent!", mr: "मस्त! / जबरदस्त", roman: "mast! / jabaradast" },
    { en: "Yuck! It looks ugly", mr: "शी! घाणेरडं दिसतंय ते", roman: "shI! ghANeraDM disataMy te" },
    { en: "I spit on your cowardice", mr: "थू! तुमच्या भित्रेपणावर", roman: "thU! tumachyA bhitrepaNAvar" },
    { en: "Shhh! Keep quiet", mr: "शू / श्श! शांत बसा!", roman: "shU / shsh! shAMt basA!" },
    { en: "How well you danced!", mr: "किती छान नाचलास तू!", roman: "kitI ChAn nAchalAs tU!" },
    { en: "What a fool he is!", mr: "काय मूर्ख आहे तो!", roman: "kAy mUrkha Ahe to!" },
    { en: "Oh! What happened then?", mr: "अय्या! मग काय झालं?", roman: "ayyA! mag kAy jhAlaM?" },
    { en: "May we speak", mr: "आम्ही बोलू का", roman: "AmhI bolU kA" },
    { en: "May you speak", mr: "तुम्ही बोलू शकता का?", roman: "tumhI bolU shakatA kA?" },
    { en: "May he tell", mr: "तो सांगू शकतो का?", roman: "to sAMgU shakato kA?" },
    { en: "Can I tell", mr: "मी सांगू शकतो का?", roman: "mI sAMgU shakato kA?" },
    { en: "May you speak", mr: "बोलता का?", roman: "bolatA kA?" },
    { en: "May you give pen", mr: "पेन देता का", roman: "pen detA kA" },
    { en: "I may sing", mr: "एखादवेळेस मी गाईन", roman: "ekhAdaveLes mI gAIn" },
    { en: "She might have completed it", mr: "कदाचित तीने पूर्ण केला असेल", roman: "kadAchit tIne pUrN kelA asel" },
    { en: "She had said", mr: "ती बोलली आहे", roman: "tI bolalI Ahe" },
    { en: "She might have said", mr: "ती बोलली असावी", roman: "tI bolalI asAvI" },
    { en: "Boy who is giving", mr: "देत असलेला मुलगा", roman: "det asalelA mulagA" },
    { en: "Person who is dancing", mr: "नाचत असलेली व्यक्ती", roman: "nAchat asalelI vyaktI" },
    { en: "Pot on table", mr: "टेबलावरचा माठ", roman: "TebalAvarachA mATh" },
    { en: "Jar on table", mr: "टेबलावरची बरणी", roman: "TebalAvarachI baraNI" },
    { en: "Leaf on table", mr: "टेबलावरचे पान", roman: "TebalAvarache pAn" },
    { en: "Gift inside box", mr: "खोक्यातली भेटवस्तू", roman: "khokyAtalI bheTavastU" },
    { en: "Area outside my home", mr: "माझ्या घराबाहेरचा परिसर", roman: "mAjhyA gharAbAherachA parisar" },
    { en: "Pot on table", mr: "टेबलावरील माठ", roman: "TebalAvarIl mATh" },
    { en: "That joke made me laugh", mr: "त्या विनोदाने मला हसायला लावले", roman: "tyA vinodAne malA hasAyalA lAvale" },
    { en: "I myself did it", mr: "मीच हे केले", roman: "mIch he kele" },
    { en: "I have seen India only", mr: "मी भारतच बघितला आहे", roman: "mI bhAratach baghitalA Ahe" },
    { en: "He kept on talking", mr: "तो बोलतच राहिला", roman: "to bolatach rAhilA" },
    { en: "Why just me?", mr: "मीच का", roman: "mIch kA" },
    { en: "Anup will have watch", mr: "अनुप जवळ/कडे घड्याळ असेल", roman: "anup javaL/kaDe ghaDyAL asel" },
    { en: "Ravi had 2 kids", mr: "रवीला दोन मुले होती", roman: "ravIlA don mule hotI" },
    { en: "She did not have any relatives", mr: "तिला कोणीही नातेवाईक नव्हते", roman: "tIlA koNIhI nAtevAIk navhate" },
    { en: "What does it mean?", mr: "त्याचा अर्थ काय", roman: "tyAchA arth kAy" },
    { en: "What does that signboard mean?", mr: "त्या पाटीचा अर्थ काय", roman: "tyA pATIchA arth kAy" },
    { en: "What does encyclopedia mean?", mr: "encyclopedia म्हणजे काय", roman: "encyclopedia mhaNaje kAy" },
    { en: "I did mean it", mr: "माझ्या बोलण्याचा अर्थ हा होता", roman: "mAjhyA bolaNyAchA arth hA hotA" },
    { en: "I did not mean it", mr: "माझ्या बोलण्याचा अर्थ हा नव्हता", roman: "mAjhyA bolaNyAchA arth hA navhatA" },
    { en: "He did not mean hurting you", mr: "त्याचा उद्देश तुम्हाला दुखवण्याचा नव्हता", roman: "tyAchA uddesh tumhAlA dukhavaNyAchA navhatA" },
    { en: "He and me", mr: "तो आणि/व मी", roman: "to ANi/v mI" },
    { en: "He told her that he is happy", mr: "त्याने तीला सांगितले की तो खूप खूष आहे", roman: "tyAne tIlA sAMgitale kI to khUp khUSh Ahe" },
    { en: "I am sure that we will succeed", mr: "मला खात्री आहे की आपण यशस्वी होऊ", roman: "malA khAtrI Ahe kI ApaN yashasvI hoU" },
    { en: "Do it the same way as he is doing", mr: "तो जसे करतो आहे तसेच कर", roman: "to jase karato Ahe tasech kar" },
    { en: "He as well as me", mr: "तो तसेच मी / तो आणि मी सुद्धा", roman: "to tasech mI / to ANi mI suddhA" },
    { en: "She sang as well as danced", mr: "ती नाचली तसेच गायली", roman: "tI nAchalI tasech gAyalI" },
    { en: "He or me", mr: "तो किंवा मी", roman: "to kiMvA mI" },
    { en: "Do or die", mr: "करा किंवा मरा", roman: "karA kiMvA marA" },
    { en: "Neither he nor I were interested", mr: "तो आणि मी दोघेही इच्छुक नव्हतो", roman: "to ANi mI doghehI ichChuk navhato" },
    { en: "I will call you then you enter on stage", mr: "मी तुला बोलवीन त्यानंतर/मग तू स्टेज वर ये", roman: "mI tulA bolavIn tyAnaMtar/mag tU sTej var ye" },
    { en: "As long as you want me, I will stay", mr: "जोपर्यंत तुला हवे आहे, तोपर्यंत मी तुझ्याबरोबर राहीन", roman: "joparyMt tulA have Ahe, toparyaMt mI tujhyAbarobar rAhIn" },
    { en: "As long as you follow rules", mr: "जोपर्यंत तुम्ही नियम पाळता तोपर्यंत तुम्हाला काही अडचण येणार नाही", roman: "joparyMt tumhI niyam pALatA toparyaMt tumhAlA kAhI aDachaN yeNAr nAhI" },
    { en: "As far as I know, he is studious", mr: "जेवढे मला माहिती आहे त्याप्रमाणे तो अभ्यासू व्यक्ती आहे", roman: "jevaDhe malA mAhitI Ahe tyApramANe to abhyAsU vyaktI Ahe" },
    { en: "As far as India is concerned", mr: "जोपर्यंत भारताचा प्रश्न आहे, कंपनी चांगले काम करत आहे", roman: "joparyMt bhAratAchA prashn Ahe toparyaMt kaMpanI chAMgale kAm karat Ahe" },
    { en: "As far as literacy is concerned", mr: "जोपर्यंत साक्षरतेचा प्रश्न आहे, आपल्याला खूप मेहनत करावी लागेल", roman: "joparyMt sAkSharatechA prashn Ahe ApalyAlA khUp mehanat karAvI lAgel" },
    { en: "He is blaming me as if I have not tried", mr: "तो माझ्यावर असे आरोप करत आहे, जणू मी प्रयत्नच केले नाहीत", roman: "to mAjhyAvar ase Arop karat Ahe, jaNU mI prayatnach kele nAhIt" },
    { en: "He passed by as if she was not there", mr: "तो तिला स्मितहास्य न देता गेला, जणू ती तिथे नव्हतीच", roman: "to tilA smitahAsy na detA gelA, jaNU tI tithe navhatIch" },
    { en: "As soon as he came", mr: "तो आल्या आल्या / तो येताच", roman: "to AlyA AlyA / to yetAch" },
    { en: "As soon as she saw", mr: "तीने बघितल्या बघितल्या / तीने बघताच", roman: "tIne baghitalyA baghitalyA / tIne baghatAch" },
    { en: "Once I see your story I will give review", mr: "मी तुझी गोष्ट बघितली की अभिप्राय देईन", roman: "mI tujhI goShT baghitalI kI abhiprAy deIn" },
    { en: "We should avoid plastic so that less pollution", mr: "आपण प्लास्टिक टाळले पाहिजे जेणेकरून प्रदूषण कमी होईल", roman: "ApaN plAsTik TALale pAhije jeNekarUn pradUShaN kamI hoIl" },
    { en: "She could not realize whether to speak or not", mr: "तीने बोलावे का नाही तीला कळले नाही", roman: "tIne bolAve kA nAhI tIlA kaLale nAhI" },
    { en: "He should inform me otherwise I will not know", mr: "त्याने मला लगेच कळवले पाहिजे नाहीतर मला कळणार नाही", roman: "tyAne malA lagech kaLavale nAhItar malA kaLaNAr nAhI" },
    { en: "I also ran", mr: "मी सुद्धा धावलो / मीही धावलो", roman: "mI suddhA dhAvalo / mIhI dhAvalo" },
    { en: "My wife was standing there yet he asked", mr: "माझी बायको तिथे उभी असली तरी त्याने माझ्या मैत्रिणीबद्दल विचारले", roman: "mAjhI bAyako tithe ubhI asalI tarI tyAne mAjhyA maitriNIbaddal vichArale" },
    { en: "I had illusion of monsters coming", mr: "मोठे राक्षस येत आहेत असा मला भास झाला", roman: "moThe rAkShas yet Ahet asA malA bhAs jhAlA" },
    { en: "Monsters coming – असल्या सारखा", mr: "मोठे राक्षस येत असल्या सारखा मला भास झाला", roman: "moThe rAkShas yet asalyA sArakhA malA bhAs jhAlA" },
    { en: "What do you feel?", mr: "तुला काय वाटते?", roman: "tulA kAy vATate?" },
    { en: "He felt happiness", mr: "त्याला आनंद वाटला", roman: "tyAlA AnaMd vATalA" },
    { en: "Don't you feel ashamed?", mr: "तुला लाज वाटत नाही का?", roman: "tulA lAj vATat nAhI kA?" },
    { en: "He will feel bad", mr: "त्याला वाईट वाटेल", roman: "tyAlA vAIT vATel" },
    { en: "To show different aspects", mr: "कंगोरे उलगडणे", roman: "kaMgore ulagaDaNe" },
    { en: "To follow up & pressurize", mr: "मानगुटीवर बसणे", roman: "mAnaguTIvar basaNe" },
    { en: "Every home same story", mr: "घरोघरी मातीच्या चुली", roman: "gharogharI mAtIchyA chulI" },
    { en: "Dampen spirit", mr: "आधीच हौस अन् त्यात पडला पाऊस", roman: "AdhIch haus an tyAt paDalA pAUs" },
    { en: "To approve formally", mr: "शिक्कामोर्तब करणे", roman: "shikkAmortab karaNe" },
    { en: "To cause destruction", mr: "मोडकळीस आणणे", roman: "moDakaLIs ANaNe" },
    { en: "After-effects", mr: "पडसाद उमटणे", roman: "paDasAd umaTaNe" },
    { en: "To override/violate", mr: "पायमल्ली करणे/होणे", roman: "pAyamallI karaNe/hoNe" },
    { en: "To renounce", mr: "तिलांजली देणे", roman: "tilAMjalI deNe" },
    { en: "To force to do", mr: "भाग पाडणे", roman: "bhAg pADaNe" },
    { en: "To trap", mr: "कोंडी करणे", roman: "koMDI karaNe" },
    { en: "To take control", mr: "ठाव घेणे", roman: "ThAv gheNe" },
    { en: "To feel embarrassed", mr: "ओशाळणे", roman: "oshALaNe" },
    { en: "To spew venom", mr: "गरळ ओकणे", roman: "garaL okaNe" },
    { en: "To support", mr: "तळी उचलणे", roman: "taLI uchalaNe" },
    { en: "To uncover mystery", mr: "गूढ उकलणे", roman: "gUDh ukalaNe" },
    { en: "To strike", mr: "टोला हाणणे", roman: "TolA hANaNe" },
    { en: "To be puzzled", mr: "पेचात पडणे", roman: "pechAt paDaNe" },
    { en: "To pardon", mr: "गय करणे", roman: "gay karaNe" },
    { en: "If wrong info given, disciplinary action", mr: "चुकीची माहिती दिल्यास शिस्तभंगाची कारवाई होईल", roman: "chukIchI mAhitI dilyAs shistabhMgAchI kAravAI hoIl" },
    { en: "Cryptography means?", mr: "\"Cryptography\" म्हणजे काय", roman: "\"Cryptography\" mhaNaje kAy" },
    { en: "I came because you called", mr: "तू बोलावलेस म्हणून मी आलो", roman: "tU bolAvales mhaNUn mI Alo" },
    { en: "Why do you want it for?", mr: "तुला हे कशासाठी हवे आहे", roman: "tulA he kashAsAThI have Ahe" },
    { en: "What is its reason?", mr: "त्याचे कारण काय", roman: "tyAche kAraN kAy" },
    { en: "It is you who told", mr: "तूच मला हे सांगितलेस", roman: "tUch malA he sAMgitales" },
    { en: "I am bored", mr: "मला कंटाळा आला आहे", roman: "malA kaMTALA AlA Ahe" },
    { en: "He was bored", mr: "त्याला कंटाळा आला होता", roman: "tyAlA kaMTALA AlA hotA" },
    { en: "Relation", mr: "नाते", roman: "nAte" },
    { en: "Relative / Relatives", mr: "नातेवाईक", roman: "nAtevAIk" },
    { en: "Wife", mr: "पत्नी / बायको", roman: "patnI / bAyako" },
    { en: "Husband", mr: "पती / नवरा", roman: "patI / navarA" },
    { en: "Son", mr: "मुलगा", roman: "mulagA" },
    { en: "Daughter", mr: "मुलगी", roman: "mulagI" },
    { en: "Son's wife / Daughter in law", mr: "सून", roman: "sUn" },
    { en: "Daughter's husband / Son in law", mr: "जावई", roman: "jAvaI" },
    { en: "Grandson", mr: "नातू", roman: "nAtU" },
    { en: "Granddaughter", mr: "नात", roman: "nAt" },
    { en: "Grandson's wife", mr: "नातसून", roman: "nAtasUn" },
    { en: "Grand daughter's husband", mr: "नातजावई", roman: "nAtajAvaI" },
    { en: "Neighbour", mr: "शेजारी", roman: "shejArI" },
    { en: "Bride", mr: "वधू / नवरी मुलगी", roman: "vadhU / navarI mulagI" },
    { en: "Bridegroom", mr: "वर / नवरा मुलगा", roman: "var / navarA mulagA" },
    { en: "Adopted", mr: "दत्तक", roman: "dattak" },
    { en: "Adopted son", mr: "दत्तक मुलगा", roman: "dattak mulagA" },
    { en: "Adopted daughter", mr: "दत्तक मुलगी", roman: "dattak mulagI" },
    { en: "Heir", mr: "वारस", roman: "vAras" },
    { en: "Assumed son", mr: "मानलेला मुलगा", roman: "mAnalelA mulagA" },
    { en: "Assumed daughter", mr: "मानलेली मुलगी", roman: "mAnalelI mulagI" },
    { en: "To wake up", mr: "जागे होणे jAge hoNe", roman: "mI jAgA jhAlo" },
    { en: "To get up", mr: "उठणे uThaNe", roman: "mI uThalo" },
    { en: "To wash", mr: "धूणे dhUNe", roman: "toND dhutale" },
    { en: "To brush", mr: "घासणे ghAsaNe", roman: "dAt ghAsale" },
    { en: "To gargle", mr: "चूळ भरणे chUL bharaNe", roman: "chUL bharalI" },
    { en: "To fold", mr: "घडी करणे ghaDI karaNe", roman: "chAdarIMchyA ghaDyA kelyA" },
    { en: "To urinate", mr: "लघवीला जाणे laghavIlA jANe", roman: "laghavIlA gelo" },
    { en: "To exercise", mr: "व्यायाम करणे vyAyAm karaNe", roman: "vyAyAm kelA" },
    { en: "To bath", mr: "आंघोळ करणे AMghoL karaNe", roman: "AMghoL kelI" },
    { en: "To change", mr: "बदलणे badalaNe", roman: "kapaDe badalale" },
    { en: "To comb", mr: "भांग पाडणे bhAMg pADaNe", roman: "bhAMg pADalA" },
    { en: "To close", mr: "बंद करणे baMd karaNe", roman: "dAr baMd kele" },
    { en: "To climb down", mr: "उतरणे utaraNe", roman: "jInA utaralo" },
    { en: "To sit", mr: "बसणे basaNe", roman: "gADIt basalo" },
    { en: "To start", mr: "सुरू करणे surU karaNe", roman: "gADI surU kelI" },
    { en: "To reach", mr: "पोचणे pochaNe", roman: "~ophisalA pochalo" },
    { en: "To climb up", mr: "चढणे chaDhaNe", roman: "jInA chaDhalo" },
    { en: "To speak/say/talk", mr: "बोलणे bolaNe", roman: "mitrAbarobar bolalo" },
    { en: "To answer", mr: "उत्तर देणे uttar deNe", roman: "uttar dile" },
    { en: "To send", mr: "पाठवणे pAThavaNe", roman: "Imel pAThavalA" },
    { en: "To put/keep", mr: "ठेवणे ThevaNe", roman: "sharT pishavIt ThevalA" },
    { en: "To put", mr: "टाकणे TAkaNe", roman: "sharT pishavIt TAkalA" },
    { en: "To stand", mr: "उभे राहणे ubhe rAhaNe", roman: "ubhA rAhilo" },
    { en: "To return", mr: "परत येणे parat yeNe", roman: "gharI parat Alo" },
    { en: "To open", mr: "उघडणे ughaDaNe", roman: "daravAjA ughaDalA" },
    { en: "To lift", mr: "उचलणे uchalaNe", roman: "pishavI uchalalI" },
    { en: "To play", mr: "खेळणे kheLaNe", roman: "mulAMbarobar kheLalo" },
    { en: "To jump", mr: "उडी मारणे uDI mAraNe", roman: "uDI mAralI" },
    { en: "To recite", mr: "म्हणणे mhaNaNe", roman: "kavitA mhaTalI" },
    { en: "To sing", mr: "गाणे gANe", roman: "gANe gAyale" },
    { en: "To shout", mr: "ओरडणे oraDaNe", roman: "oraDalo" },
    { en: "To throw", mr: "फेकणे phekaNe", roman: "cheMDU phekalA" },
    { en: "To ask", mr: "विचारणे vichAraNe", roman: "tyAche nAv vichArale" },
    { en: "To ask for", mr: "मागणे mAgaNe", roman: "tyAche pen mAgitale" },
    { en: "To clean", mr: "स्वच्छ करणे svachCha karaNe", roman: "Tebal svachCha kele" },
    { en: "To cut", mr: "कापणे kApaNe", roman: "kek kApalA" },
    { en: "To break", mr: "तोडणे toDaNe / मोडणे moDaNe", roman: "kheLaNe toDale" },
    { en: "To burst", mr: "फोडणे phoDaNe", roman: "glAs phoDalA" },
    { en: "Accept", mr: "स्वीकारणे svIkAraNe", roman: "mI kalpanA svIkAralI" },
    { en: "Give", mr: "देणे deNe", roman: "pen dile" },
    { en: "Take", mr: "घेणे gheNe", roman: "pen ghetale" },
    { en: "Bring", mr: "आणणे ANaNe", roman: "sAkhar ANalI" },
    { en: "Complain", mr: "तक्रार करणे takrAr karaNe", roman: "tyAchyAviruddh takrAr kelI" },
    { en: "Dance", mr: "नाचणे nAchaNe", roman: "nAchalo" },
    { en: "Draw", mr: "चित्र काढणे chitra kADhaNe", roman: "chitra kADhale" },
    { en: "Fall", mr: "पडणे paDaNe", roman: "paDalo" },
    { en: "Fill", mr: "भरणे bharaNe", roman: "bATalI bharalI" },
    { en: "Finish", mr: "संपवणे saMpavaNe", roman: "dUdh saMpavale" },
    { en: "Live", mr: "राहणे rAhaNe", roman: "mI shaharAt rAhilo" },
    { en: "See/watch/look", mr: "बघणे baghaNe / पाहणे pAhaNe", roman: "sUchanA baghitalI" },
    { en: "Wait", mr: "वाट बघणे vAT baghaNe", roman: "basachI vAT baghitalI" },
    { en: "Use", mr: "वापरणे vAparaNe", roman: "pen vAparale" },
    { en: "Run", mr: "पळणे paLaNe / धावणे dhAvaNe", roman: "paLAlo" },
    { en: "Make/prepare", mr: "तयार करणे tayAr karaNe / बनवणे banavaNe", roman: "mUrtI tayAr kelI" },
    { en: "Tell", mr: "सांगणे sAMgaNe", roman: "pattA sAMgitalA" },
    { en: "Fly", mr: "उडणे uDaNe", roman: "mI uDalo" },
    { en: "Forget", mr: "विसरणे visaraNe", roman: "tyAche nAv visaralo" },
    { en: "Remember", mr: "आठवणे AThavaNe", roman: "tyAche nAv AThavale" },
    { en: "Get bored", mr: "कंटाळणे kaMTALaNe", roman: "kaMTALalo" },
    { en: "Know", mr: "महिती असणे mahitI asaNe", roman: "tyAche nAv malA mAhitI hote" },
    { en: "Leave", mr: "सोडणे soDaNe", roman: "kaMpanI soDalI" },
    { en: "Want/need", mr: "हवे असणे have asaNe", roman: "malA pANI have hote" },
    { en: "Sign", mr: "सही करणे sahI karaNe", roman: "chekavar sahI kelI" },
    { en: "Sleep", mr: "झोपणे jhopaNe", roman: "dahA vAjatA jhopalo" },
    { en: "Swim", mr: "पोहणे pohaNe", roman: "chAr tAs pohalo" },
    { en: "Try", mr: "प्रयत्न करणे prayatn karaNe", roman: "phreMch shikAyachA prayatn kelA" },
    { en: "Understand", mr: "समजणे samajaNe", roman: "malA muddA kaLalA" },
    { en: "Worry", mr: "चिंता करणे chiMtA karaNe / काळजी करणे kALajI karaNe", roman: "tyAchyA abhyAsachI chiMtA kelI" },
    { en: "Admit (mistake)", mr: "मान्य करणे mAny karaNe", roman: "chUk mAny kelI" },
    { en: "Afford", mr: "परवडणे paravaDaNe", roman: "malA mahAg kAr gheNe paravaDale" },
    { en: "Win", mr: "जिंकणे jiMkaNe", roman: "spardhA jiMkalo" },
    { en: "Lose", mr: "हरणे haraNe", roman: "spardhA haralo" },
    { en: "Shake", mr: "हलवणे halavaNe", roman: "mishraN halavale" },
    { en: "Decide", mr: "ठरवणे TharavaNe", roman: "mI jAyache Tharavale" },
    { en: "Hold", mr: "धरणे dharaNe", roman: "b~aT hAtAt dharalI" },
    { en: "Choose", mr: "निवडणे nivaDaNe", roman: "pivaLA sharT nivaDalA" },
    { en: "Turn", mr: "वळणे vaLaNe", roman: "ujavIkaDe vaLalo" },
    { en: "Rise", mr: "उगवणे ugavaNe", roman: "sUry ugavalA" },
    { en: "Deny", mr: "नाकारणे nAkAraNe", roman: "mI kalpanA nAkAralI" },
    { en: "To turn on the lamp", mr: "दिवा लावणे", roman: "divA lAvaNe" },
    { en: "To turn on the TV", mr: "टी.व्ही. लावणे", roman: "TI vhI lAvaNe" },
    { en: "To bolt the door", mr: "कडी लावणे", roman: "kaDI lAvaNe" },
    { en: "To touch by foot", mr: "पाय लावणे", roman: "pAy lAvaNe" },
    { en: "To reproach/blame", mr: "बोल लावणे", roman: "bol lAvaNe" },
    { en: "To fix tune of song", mr: "चाल लावणे", roman: "chAl lAvaNe" },
    { en: "To color", mr: "रंग लावणे", roman: "raMg lAvaNe" },
    { en: "To destroy", mr: "वाट लावणे", roman: "vAT lAvaNe" },
    { en: "To apply oil", mr: "तेल लावणे", roman: "tel lAvaNe" },
    { en: "I need bucket", mr: "मला बादली लागते", roman: "malA bAdalI lAgate" },
    { en: "I will need bucket", mr: "मला बादली लागेल", roman: "malA bAdalI lAgel" },
    { en: "I was hungry", mr: "मला भूक लागली", roman: "malA bhUk lAgalI" },
    { en: "I am hungry", mr: "मला भूक लागली आहे", roman: "malA bhUk lAgalI Ahe" },
    { en: "Big Boss serial starts at 9", mr: "बिग बॉस मालिका नऊ वाजता लागते", roman: "big b~os mAlikA naU vAjatA lAgate" },
    { en: "The bulb was on", mr: "विजेचा बल्ब लागला", roman: "vijechA bulb lAgalA" },
    { en: "TV started after repair", mr: "त्याने दुरुस्त केल्यावर टीव्ही लागला", roman: "tyAne durust kelyAvar TIvhI lAgalA" },
    { en: "Big", mr: "मोठा", roman: "moThA" },
    { en: "Small", mr: "लहान / छोटा", roman: "lahAn / ChoTA" },
    { en: "Far / Away", mr: "दूर / लांब", roman: "dUr / lAMb" },
    { en: "Deep", mr: "खोल", roman: "khol" },
    { en: "Shallow", mr: "उथळ", roman: "uthaL" },
    { en: "Simple", mr: "साधा", roman: "sAdhA" },
    { en: "Special", mr: "विशेष", roman: "visheSh" },
    { en: "Dark", mr: "गडद", roman: "gaDad" },
    { en: "Faint", mr: "फिका", roman: "phikA" },
    { en: "Short", mr: "बुटका", roman: "buTakA" },
    { en: "Wide", mr: "रुंद", roman: "ruMda" },
    { en: "Narrow", mr: "अरुंद", roman: "aruMda" },
    { en: "Straight", mr: "सरळ", roman: "saraL" },
    { en: "Curved", mr: "वाकडा", roman: "vAkaDA" },
    { en: "Tasty", mr: "चवदार / चविष्ट", roman: "chavadAr / chaviShT" },
    { en: "Tasteless", mr: "बेचव", roman: "bechav" },
    { en: "Sweet", mr: "गोड", roman: "goD" },
    { en: "Sour", mr: "आंबट", roman: "AMbaT" },
    { en: "Fresh", mr: "ताजा", roman: "tAjA" },
    { en: "Stale", mr: "शिळा", roman: "shiLA" },
    { en: "Spicy", mr: "मसालेदार", roman: "masAledAr" },
    { en: "Colourful", mr: "रंगीत", roman: "raMgIt" },
    { en: "Easy", mr: "सोपा", roman: "sopA" },
    { en: "Hard / Difficult", mr: "कठीण", roman: "kaThIN" },
    { en: "Clean", mr: "स्वच्छ", roman: "svachCha" },
    { en: "Dirty / Soiled", mr: "मळका", roman: "maLakA" },
    { en: "Dry", mr: "कोरडा / सुका", roman: "koraDA / sukA" },
    { en: "Wet", mr: "ओला", roman: "olA" },
    { en: "Empty", mr: "रिकामा", roman: "rikAmA" },
    { en: "Filled", mr: "भरलेला", roman: "bharalelA" },
    { en: "Expensive", mr: "महाग", roman: "mahAg" },
    { en: "Cheap", mr: "स्वस्त", roman: "svasta" },
    { en: "Full / Complete", mr: "पूर्ण", roman: "pUrNa" },
    { en: "Incomplete", mr: "अपूर्ण", roman: "apUrNa" },
    { en: "Half", mr: "अर्धा", roman: "ardhA" },
    { en: "Soft", mr: "मऊ", roman: "maU" },
    { en: "Heavy", mr: "जड", roman: "jaD" },
    { en: "New", mr: "नवीन / नवा", roman: "navIn / navA" },
    { en: "Old", mr: "जुना", roman: "junA" },
    { en: "Quiet / Peaceful", mr: "शांत", roman: "shAMt" },
    { en: "Slow", mr: "हळू", roman: "haLU" },
    { en: "Fast", mr: "वेगवान", roman: "vegavAn" },
    { en: "Young", mr: "तरूण", roman: "tarUN" },
    { en: "Old", mr: "म्हातारा", roman: "mhAtArA" },
    { en: "Little / Few / Some", mr: "थोडा", roman: "thoDA" },
    { en: "Many / Much", mr: "खूप", roman: "khUp" },
    { en: "Happy", mr: "आनंदी / खुश", roman: "AnaMdI / khush" },
    { en: "Unhappy", mr: "नाखुश", roman: "nAkhush" },
    { en: "Sad", mr: "दुःखी", roman: "duHkhI" },
    { en: "Gloomy", mr: "उदास", roman: "udAs" },
    { en: "Agile / Swift", mr: "चपळ", roman: "chapaL" },
    { en: "Dull", mr: "मंद", roman: "maMd" },
    { en: "Lazy", mr: "आळशी", roman: "ALashI" },
    { en: "Eager / Enthusiastic", mr: "उत्साही", roman: "utsAhI" },
    { en: "Slowly", mr: "हळूहळू", roman: "haLUhaLU" },
    { en: "Fast", mr: "जोरात", roman: "jorAt" },
    { en: "Quickly", mr: "पटकन", roman: "paTakan" },
    { en: "He watched eagerly", mr: "त्याने अधिरतेने बघितली", roman: "tyAne adhiratene baghitalI" },
    { en: "She can finish easily", mr: "ती हे काम सहजपणे संपवू शकते", roman: "tI he kAm sahajapaNe saMpavU shakate" },
    { en: "A bit", mr: "थोडासा", roman: "thoDAsA" },
    { en: "Absolutely", mr: "पूर्णपणे", roman: "pUrNapaNe" },
    { en: "Accordingly", mr: "प्रमाणे", roman: "pramANe" },
    { en: "Accurately", mr: "अचूकपणे", roman: "achUkapaNe" },
    { en: "Actively", mr: "सक्रियपणे", roman: "sakriyapaNe" },
    { en: "Afresh", mr: "नव्याने", roman: "navyAne" },
    { en: "Again", mr: "पुन्हा", roman: "punhA" },
    { en: "Agreeably", mr: "संमतीपूर्वक", roman: "saMmatIpUrvak" },
    { en: "All", mr: "सर्व", roman: "sarva" },
    { en: "Almost", mr: "बहुतेक / जवळजवळ पूर्ण", roman: "bahutek / javaLajavaL pUrN" },
    { en: "Altogether", mr: "एकत्र / सगळे मिळून", roman: "ekatra / sagaLe miLUn" },
    { en: "Always", mr: "नेहमी", roman: "nehamI" },
    { en: "Any", mr: "कुठलाही", roman: "kuThalAhI" },
    { en: "Away", mr: "दूर", roman: "dUr" },
    { en: "Badly", mr: "वाईटपणे", roman: "vAITapaNe" },
    { en: "Barely", mr: "जेमतेम", roman: "jematem" },
    { en: "Beautifully", mr: "सुंदरपणे", roman: "suMdarapaNe" },
    { en: "Best", mr: "सर्वात छान", roman: "sarvAt ChAn" },
    { en: "Certainly", mr: "नक्कीच / निश्चितपणे", roman: "nakkIch / nishchitapaNe" },
    { en: "Easily", mr: "सहजपणे", roman: "sahajapaNe" },
    { en: "Enough", mr: "पुरेसे", roman: "purese" },
    { en: "Fortunately", mr: "नशिबाने / सुदैवाने", roman: "nashibAne / sudaivAne" },
    { en: "Frequently", mr: "वरचेवर", roman: "varachevar" },
    { en: "Happily", mr: "आनंदाने", roman: "AnaMdAne" },
    { en: "Once", mr: "एकदा", roman: "ekadA" },
    { en: "Quickly", mr: "लगेच / पटकन", roman: "lagech / paTakan" },
    { en: "Rarely", mr: "क्वचित", roman: "kvachit" },
    { en: "Really", mr: "खरेच", roman: "kharech" },
    { en: "Secretly", mr: "लपूनछपून / गुप्तपणे", roman: "lapUnaChapUn / guptapaNe" },
    { en: "Truly", mr: "खरोखर", roman: "kharokhar" },
    { en: "Usually", mr: "नेहमी / सामान्यतः", roman: "nehamI / sAmAnyatH" },
    { en: "Well", mr: "ठीक", roman: "ThIk" },
    { en: "Red", mr: "लाल / तांबडा", roman: "lAl / tAMbaDA" },
    { en: "Yellow", mr: "पिवळा", roman: "pivaLA" },
    { en: "Green", mr: "हिरवा", roman: "hiravA" },
    { en: "Blue", mr: "निळा", roman: "niLA" },
    { en: "Purple", mr: "जांभळा", roman: "jAMbhaLA" },
    { en: "Brown", mr: "भुरा / तपकिरी", roman: "bhurA / tapakirI" },
    { en: "Black", mr: "काळा", roman: "kALA" },
    { en: "Pink", mr: "गुलाबी", roman: "gulAbI" },
    { en: "Orange", mr: "नारींगी", roman: "nArIMgI" },
    { en: "Saffron", mr: "भगवा केशरी", roman: "bhagavA kesharI" },
    { en: "Ivory", mr: "हस्तिदंती", roman: "hastidaMtI" },
    { en: "Silver", mr: "चंदेरी", roman: "chaMderI" },
    { en: "Annona Hexapetala", mr: "चाफा", roman: "chAphA" },
    { en: "Chrysanthemums", mr: "शेवंती", roman: "shevaMtI" },
    { en: "Crape Jasmine / Pinwheel", mr: "तगर", roman: "tagar" },
    { en: "Common Jasmine", mr: "जुई", roman: "juI" },
    { en: "Jasminum grandiflorum", mr: "जाई", roman: "jAI" },
    { en: "Lotus", mr: "कमळ", roman: "kamaL" },
    { en: "Tuberose", mr: "निशिगंध", roman: "nishigaMdh" },
    { en: "Lantana Camera", mr: "कुंदा", roman: "kuMdA" },
    { en: "Rose", mr: "गुलाब", roman: "gulAb" },
    { en: "Magnolia", mr: "चंपा", roman: "chaMpA" },
    { en: "Jasminum sambac", mr: "मोगरा", roman: "mogarA" },
    { en: "Sweet Granadilla", mr: "कृष्णकमळ", roman: "kRuShNakamaL" },
    { en: "Coral Jasmine", mr: "पारिजातक", roman: "pArijAtak" },
    { en: "Bullet wood", mr: "बकुळ", roman: "bakuL" },
    { en: "Spanish Jasmine", mr: "चमेली", roman: "chamelI" },
    { en: "Periwinkle", mr: "सदाफुली", roman: "sadAphulI" },
    { en: "Frangipani", mr: "सोनचाफा", roman: "sonachAphA" },
    { en: "Yellow ginger", mr: "सोनटक्का", roman: "sonaTakkA" },
    { en: "Lantana Camera", mr: "घाणेरी", roman: "ghANerI" },
    { en: "Cypress vine", mr: "गणेशवेल", roman: "gaNeshavel" },
    { en: "Oleander", mr: "कण्हेर", roman: "kaNher" },
    { en: "Datura", mr: "धोतरा", roman: "dhotarA" },
    { en: "Crossandra", mr: "अबोली", roman: "abolI" },
    { en: "Where are you (to boy/girl)", mr: "तू कुठे आहेस", roman: "tU kuThe Ahes" },
    { en: "Where are you (to man/lady)", mr: "तुम्ही कुठे आहात", roman: "tumhI kuThe AhAt" },
    { en: "I am here", mr: "मी इकडे आहे", roman: "mI ikaDe Ahe" },
    { en: "I am there", mr: "मी तिकडे आहे", roman: "mI tikaDe Ahe" },
    { en: "I am in office", mr: "मी ऑफिसमधे आहे", roman: "mI ~ophisamadhe Ahe" },
    { en: "I am on terrace", mr: "मी गच्चीवर आहे", roman: "mI gachchIvar Ahe" },
    { en: "I am on the way", mr: "मी वाटेत आहे", roman: "mI vATet Ahe" },
    { en: "Where is post office", mr: "पोस्ट ऑफीस कुठे आहे", roman: "posT ~ophIs kuThe Ahe" },
    { en: "Post office is far", mr: "पोस्ट ऑफीस लांब/दूर आहे", roman: "posT ~ophIs lAMb/dUr Ahe" },
    { en: "Turn left", mr: "डावीकडे वळा", roman: "DAvIkaDe vaLA" },
    { en: "Turn right", mr: "उजवीकडे वळा", roman: "ujavIkaDe vaLA" },
    { en: "What will you bring from there?", mr: "तिकडून मला काय आणशील?", roman: "tikaDUn malA kAy ANashIl?" },
    { en: "Maintain silence there", mr: "तिथे शांतता पाळा", roman: "tithe shAMtatA pALA" },
    { en: "Do not roam here-and-there", mr: "इकडेतिकडे भटकू नकोस", roman: "ikaDetikaDe bhaTakU nakos" },
    { en: "Wow!! But why did you leave?", mr: "अरे वा !! पण का सोडलीस?", roman: "are wA. paN kA sodalist" },
    { en: "Core Java", mr: "कोअर जावा", roman: "koar jAvA" },
    { en: "Is completely fix?", mr: "पूर्ण fix आहे का?", roman: "poorN fix Ahe kA?" },
    { en: "No. 0.6 of that is variable", mr: "नाही त्यातलं ०.६ variable आहे.", roman: "nAhI tyAtalM 0.6 variable Ahe." },
    { en: "And how much is your total experience?", mr: "आणि एकूण experience किती झाला?", roman: "ANi ekUN experience kitI jhAlA?" },
    { en: "Yes. But I was bored. I could not see growth there", mr: "हो. पण कंटाळा आला होता. तिथे काही growth दिसत नव्हती.", roman: "ho. paN kaMTALA aalA hotA. tithe kAhI growth disat navhatI." },
    { en: "Where do you live?", mr: "राहतोस कुठे?", roman: "rAhatos kuThe?" },
    { en: "No. It is rented", mr: "नाही भाड्याचा आहे", roman: "nAhI bhADyAchA Ahe" },
    { en: "Are you looking for a house?", mr: "तू बघतोयस का घर?", roman: "tU baghatoyas kA ghar?" },
    { en: "How much did it cost?", mr: "कितीला पडला?", roman: "kitIlA paDalA?" },
    { en: "30 Lakhs", mr: "तीस लाखाला", roman: "tIs lAkhAlA" },
    { en: "It is cheap then. How much is rate there?", mr: "स्वस्त आहे की. किती Rate आहे तिकडे.", roman: "swast Ahe kI. kitI rate aahe tikaDe." },
    { en: "2000", mr: "दोन हजार", roman: "don hajAr" },
    { en: "Fine", mr: "चालेल.", roman: "chalel." },
    { en: "Sit down", mr: "बसा", roman: "basA" },
    { en: "Its period of geography, right?", mr: "भुगोलाचा तास आहे ना?", roman: "bhugolAchA tAs Ahe nA?" },
    { en: "Yes. Understood", mr: "हो. कळले.", roman: "ho. kaLale." },
    { en: "Sure?", mr: "नक्की?", roman: "nakkI?" },
    { en: "Yes. Sure", mr: "हो नक्की.", roman: "ho nakkI." },
    { en: "Why?", mr: "का", roman: "kA" },
    { en: "I was not feeling well", mr: "मला काल बरं वाटत नव्हतं", roman: "malA kAl baraM vATat navhataM" },
    { en: "Ok", mr: "ठिक आहे", roman: "Thik Ahe" },
    { en: "Is date decided?", mr: "तारीख ठरली का?", roman: "tArIkh TharalI kA?" },
    { en: "Not yet", mr: "अजून नाही.", roman: "ajUn nAhI." },
    { en: "But mostly it will be from 15th", mr: "पण बहुतेक पंधरा (१५) तारखेपासून असेल", roman: "paN bahutek paMdharA (15) tArakhepAsUn asel" },
    { en: "But start preparing from now onwards only", mr: "पण आत्तापासूनच तयारी सुरू करा", roman: "paN AttApAsUnach tayArI surU karA" },
    { en: "Lets move towards the lesson", mr: "चला, आता धड्याकडे वळूया", roman: "chalA, AtA dhaDyAkaDe vaLUyA" },
    { en: "Keep quiet", mr: "शांत बसा.", roman: "shAMt basA." },
    { en: "What is the noise in that corner?", mr: "त्या कोपऱ्यात काय गडबड चालू आहे?", roman: "tya koparyAt kAy gaDabaD chAlU Ahe?" },
    { en: "Then why is noise coming from there?", mr: "मग तिकडून आवाज का येतोय.", roman: "mag tikaDUn AvAj kA yetoy." },
    { en: "Ok. All sit down", mr: "ठिक आहे. बसा सगळे खाली.", roman: "Thik Ahe. basA sagaLe khAlI." },
    { en: "Lets start chapter", mr: "चला धडा सुरू करू.", roman: "chalA dhaDA surU karU." },
    { en: "He is not at home", mr: "ते आत्ता घरात नाहियेत.", roman: "te AttA gharAt nAhiyet" },
    { en: "When will he be back?", mr: "कधी येतील परत?", roman: "kadhI yetIl parat?" },
    { en: "Where?", mr: "कुठे आहे?", roman: "kuThe Ahe?" },
    { en: "In park", mr: "पार्कमध्ये", roman: "pArkamadhye" },
    { en: "Just wait. Door bell is ringing. I will open door", mr: "एक मिनिट थांबा दाराची बेल वाजत्ये. मी दार उघडतो.", roman: "ek miniT thAMbA dArAchI bel vAjatye. mI dAr ughaDato." },
    { en: "Probably its Vaibhav", mr: "बहुतेक वैभवच आला असेल.", roman: "bahutek vaibhavach AlA asel." },
    { en: "Hey Mr. Kulakarni, how are you?", mr: "बोला कुलकर्णी साहेब. कसे आहात.", roman: "bolA kulakarNI sAheb. kase AhAt." },
    { en: "I am fine. How are you?", mr: "मी मजेत. तुम्ही कसे आहात?", roman: "mI majet. tumhI kase AhAt?" },
    { en: "I am fine too. Tell me. What were you up to?", mr: "मी पण मजेत. बोला काय काम होतं.", roman: "mI paN majet. bolA kAy kAm hotM." },
    { en: "I came to know. Mr. Rajwade met me. He told", mr: "मला कळलं त्याबद्दल. राजवाडे भेटले होते मला. ते बोलले.", roman: "malA kaLalM tyAbaddal. rAjavADe bheTale hote malA. te bolale." },
    { en: "Yes, see you", mr: "हो भेटुया.", roman: "ho bheTuyA." },
    { en: "Who Vaibhav?", mr: "कोण वैभव?", roman: "koN vaibhav?" },
    { en: "It is 12345678, isn't it?", mr: "१२३४५६७८ च आहे ना?", roman: "12345678 ch Ahe nA?" },
    { en: "There under that bridge", mr: "त्या पुला खाली", roman: "tyA pulA khAlI" },
    { en: "Yes", mr: "हो.", roman: "ho." },
    { en: "Don't know", mr: "माहित नाही.", roman: "mAhit nAhI." },
    { en: "Yes it is at 10 past 10", mr: "हो दहा दहा ची आहे.", roman: "ho dahA dahA chI Ahe." },
    { en: "And then?", mr: "आणि पुढे?", roman: "ANi puDhe?" },
    { en: "From phase-2 you will get share-auto for phase-3", mr: "फेज-२ पासून पुढे शेअर रिक्शा मिळते फेज-३ ला जायला.", roman: "phej-2 pAsUn puDhe shear rikshA miLate phej-3 lA jAyalA." },
    { en: "From that next stop. Get in and stand in queue.", mr: "या पुढच्या स्टॉप पासून. आत रांगेत उभे रहा.", roman: "yA puDhachyA sT~op pAsUn. At rAMget ubhe rahA." },
    { en: "1 Dange chowk", mr: "एक डांगे चौक द्या.", roman: "ek DAMge chauk dyA." },
    { en: "Twelve rupees", mr: "बारा रुपये.", roman: "bArA rupaye." },
    { en: "Here it is", mr: "हे घ्या.", roman: "he ghyA." },
    { en: "I do not have change", mr: "माझ्याकडे सुट्टे नाहित.", roman: "mAjhyAkaDe suTTe nAhit." },
    { en: "Let me check", mr: "बघतो.", roman: "baghato." },
    { en: "I have 5", mr: "५ आहेत.", roman: "5 Ahet." },
    { en: "I do not know the stop. Can you tell me once we reach there?", mr: "मला स्टॉप माहित नाहिये. स्टॉप आला की सांगा.", roman: "malA sT~op mAhit nAhiye. sT~op AlA kI sAMgA." },
    { en: "Should I get down here?", mr: "मी उतरू का इकडे.", roman: "mI utarU kA ikaDe." },
    { en: "My 3 rupees are pending", mr: "माझे तीन रुपये राहिलेत.", roman: "mAjhe tIn rupaye rAhilet." },
    { en: "I love you", mr: "माझं तुझ्यावर प्रेम आहे", roman: "mAjhaM tujhyAvar prem Ahe" },
    { en: "I love you (Boy to Girl)", mr: "मी तुझ्यावर प्रेम करतो", roman: "mI tujhyAvar prem karato" },
    { en: "I love you (Girl to Boy)", mr: "मी तुझ्यावर प्रेम करते", roman: "mI tujhyAvar prem karate" },
    { en: "I like you (Girl to Boy)", mr: "मला तू आवडतोस", roman: "malA tU AvaDatos" },
    { en: "I like you (Boy to Girl)", mr: "मला तू आवडतेस", roman: "malA tU AvaDates" },
    { en: "You are very beautiful", mr: "तू खूप सुंदर आहेस", roman: "tU khUp suMdar Ahes" },
    { en: "Shall we marry?", mr: "आपण लग्न करूया का.", roman: "ApaN lagn karUyA kA." },
    { en: "Will you marry me?", mr: "तू माझ्याशी लग्न करशील का?", roman: "tU mAjhyAshI lagn karashIl kA?" },
    { en: "Yes, Lets marry!!", mr: "हो. आपण लग्न करूया.", roman: "ho. ApaN lagn karUyA." },
    { en: "We shall elope and get married", mr: "आपण पळून जाऊन लग्न करू.", roman: "ApaN paLUn jAUn lagn karU." },
    { en: "No. I do not want to get married secretly", mr: "नाही. मला लपूनछपून लग्न करायचे नाही.", roman: "nAhI. malA lapUnaChapUn lagn karAyache nAhI." },
    { en: "I trust you completely", mr: "माझा तुझ्यावर पूर्ण विश्वास आहे", roman: "mAjhA tujhyAvar pUrN vishvAs Ahe" },
    { en: "Why do you sulk (Boy to Girl)", mr: "तू का रुसली आहेस", roman: "tU kA rusalI Ahes" },
    { en: "Why do you sulk (Girl to Boy)", mr: "तू का रुसला आहेस", roman: "tU kA rusalA Ahes" },
    { en: "Why are you angry (Boy to Girl)", mr: "तू का रागावली आहेस", roman: "tU kA rAgAvalI Ahes" },
    { en: "Why are you angry (Girl to Boy)", mr: "तू का रागावला आहेस", roman: "tU kA rAgAvalA Ahes" },
    { en: "Why don't you talk with me?", mr: "तू माझ्याशी का बोलत नाहीस", roman: "tU mAjhyAshI kA bolat nAhIs" },
    { en: "I will not talk with you", mr: "मी तुझ्याशी बोलणार नाही", roman: "mI tujhyAshI bolaNAr nAhI" },
    { en: "I miss you a lot", mr: "मला तुझी खूप आठवण येते", roman: "malA tujhI khUp AThavaN yete" },
    { en: "I can not live without you", mr: "मी तुझ्याशिवाय जगू शकत नाही", roman: "mI tujhyAshivAy jagU shakat nAhI" },
    { en: "I want to marry your daughter", mr: "मला तुमच्या मुलीशी लग्न करायचे आहे", roman: "malA tumachyA mulIshI lagn karAyache Ahe" },
    { en: "I want to marry your son", mr: "मला तुमच्या मुलाशी लग्न करायचे आहे", roman: "malA tumachyA mulAshI lagn karAyache Ahe" },
    { en: "I will keep your son/daughter happy", mr: "मी तुमच्या मुलाला/मुलीला नेहमी सुखात/ आनंदात ठेवीन", roman: "mI tumachyA mulAlA/mulIlA nehamI sukhAt/ AnaMdAt ThevIn" },
    { en: "We will always live very happily", mr: "आपण नेहमी सुखात/आनंदात राहू.", roman: "ApaN nehamI sukhAt/ AnaMdAt rAhU" },
    { en: "Let me see your resume", mr: "तुमचा रेझ्युमे बघू", roman: "tumachA rejhyume baghU" },
    { en: "Tell me a bit about yourself", mr: "मला जरा तुमच्या बद्दल सांगा", roman: "malA jarA tumachyA baddal sAMgA" },
    { en: "I am from Mumbai", mr: "मी मुंबईचा आहे", roman: "mI muMbaIchA Ahe" },
    { en: "I was born in Mumbai", mr: "माझा जन्म मुंबईत झाला.", roman: "mAjhA janm muMbaIt jhAlA." },
    { en: "From where did you do M.B.A.?", mr: "तुम्ही एम.बी.ए कुठून केलंत?", roman: "tumhI em.bI.e kuThUn kelMt?" },
    { en: "I did MBA from IIM Ahmedabad", mr: "मी एम.बी.ए आय.आय.एम. अहमदाबाद मधून केलं.", roman: "mI em.bI.e Ay.Ay.em. ahamadAbAd madhUn kelM." },
    { en: "How much total experience do you have?", mr: "तुमचा एकूण अनुभव किती आहे?", roman: "tumachA ekUN anubhav kitI Ahe?" },
    { en: "ABC, PQR and XYZ. Currently in XYZ company", mr: "ABC, PQR आणि XYZ. सध्या XYZ कंपनीत आहे.", roman: "ABC, PQR ANi XYZ. sadhyA kaMpanIt Ahe." },
    { en: "Java, Web-Service, Spring", mr: "जावा, वेब-सर्विस, स्प्रिंग.", roman: "jAvA, veba-sarvis, spriMg." },
    { en: "Who all do you have at home?", mr: "तुमच्या घरी कोण असतं?", roman: "tumachyA gharI koN asatM?" },
    { en: "Do you live together?", mr: "सगळे एकत्र रहता का?", roman: "sagaLe ekatr rahatA kA?" },
    { en: "Yes. We all live in Pune", mr: "हो सगळे सध्या पुण्यात राहतो.", roman: "ho sagaLe sadhyA puNyAt rAhato." },
    { en: "What do your siblings do?", mr: "तुमची भावंडे काय करतात?", roman: "tumachI bhAvaMDe kAy karatAt?" },
    { en: "What are your hobbies?", mr: "तुमचे छंद काय आहेत?", roman: "tumache ChaMd kAy Ahet?" },
    { en: "What are your strengths and weaknesses?", mr: "तुमच्या स्ट्रेंथ्स आणि वीकनेस काय अहेत?", roman: "tumachyA sTreMths ANi vIkanes kAy ahet?" },
    { en: "It was nice talking with you", mr: "तुमच्याशी बोलून बरं वाटलं.", roman: "tumachyAshI bolUn baraM vATalM." },
    { en: "Our H.R. will let you know", mr: "आमचे एच.आर तुम्हाला कळवतील.", roman: "Amache ech.Ar tumhAlA kaLavatIl." },
    { en: "For how many people?", mr: "किती जणांचं धुणं-भांडी", roman: "kitI jaNAMchaM dhuNM-bhAMDI" },
    { en: "Ok. 700 for Clothes, 700 for dishes", mr: "बरं. धुण्याचे सातशे आणि भांड्यांचे सातशे होतील.", roman: "baraM. dhuNyAche sAtashe ANi bhAMDyAMche sAtashe hotIl." },
    { en: "200 for floor cleaning", mr: "लाद्या पुसायचे दोनशे.", roman: "lAdyA pusAyache donashe." },
    { en: "700 for clothes and dishes seems a lot", mr: "पण धुण्याचे आणि भांड्यांचे सातशे म्हणजे खूपच वाटतात.", roman: "paN dhuNyAche ANi bhAMDyAMche sAtashe mhaNaje khUpach vATatAt." },
    { en: "We charge 150 per person", mr: "माणशी दीडशेच घेतो.", roman: "mANashI dIDashech gheto." },
    { en: "600 for clothes, 600 for dishes and 200 for cleaning", mr: "सहाशे धुण्याचे; सहाशे भांड्यांचे आणि दोनशे लादी पुसायचे.", roman: "sahAshe dhuNyAche; sahAshe bhAMDyAMche ANi donashe lAdI pusAyache." },
    { en: "Do not take unplanned leaves without informing", mr: "पण न सांगता दांड्या मारू नका.", roman: "hM. paN na sAMgatA dAMDyA mArU nakA." },
    { en: "Pots-n-Dishes are in basin. Take them to bathroom", mr: "भांडी बेसिन मध्ये ठेवली आहेत ती मोरीत घेऊन जा.", roman: "bhAMDI besin madhye ThevalI Ahet tI morIt gheUn jA." },
    { en: "Soap and scrubber is there in that corner", mr: "साबण, घासणी तिकडे कोपऱ्यात आहे.", roman: "sAbaN, ghAsaNI tikaDe koparxyAt Ahe." },
    { en: "Aunty, you did not give me bonus for Diwali", mr: "काकू दिवाळीचा बोनस नाही दिलात.", roman: "kAkU divALIchA bonas nAhI dilAt." },
    { en: "Take these 400 extra", mr: "हे घ्या चारशे जास्ती देते.", roman: "he ghyA chaarashe jAstI dete." },
    { en: "What is that actually?", mr: "हे नक्की काय असतं?", roman: "he nakkI kAy asatM?" },
    { en: "Implemented on 26 January 1950", mr: "आणि अखेरीस २६ जानेवारी १९५० रोजी संविधान अंमलात आले.", roman: "ANi akherIs jAnevArI rojI sMvidhAn aMmalAt Ale." },
    { en: "I want to make a DD. Where is the form?", mr: "मला डिमांड ड्राफ्ट तयार करायचा आहे. डीडी बनवायसाठी मला फॉर्म कुठे मिळेल?", roman: "malA DimAMD DrAphT tayAr karAyachA Ahe. DIDI banavAyasAThI malA ph~orm kuThe miLel?" },
    { en: "Where is feedback box?", mr: "अभिप्राय पेटी कुठे आहे?", roman: "abhiprAy peTI kuThe Ahe?" },
    { en: "How much do you want to deposit?", mr: "तुम्हाला तुमच्या खात्यात किती रक्कम जमा करायची आहे?", roman: "tumhAlA tumachyA khAtyAt kitI rakkam jamA karAyachI Ahe?" },
    { en: "What is minimum deposit?", mr: "मी कमीतकमी कीती रक्कम जमा करू शकतो?", roman: "mI kamitakamI kItI rakkam jamA karU shakato?" },
    { en: "How long for cheque to arrive?", mr: "मला चेक मिळायला किती वेळ लागेल?", roman: "mala chek milayala kiti vel lagel?" },
    { en: "I need locker facility", mr: "मला तिजोरीची सुविधा हवी आहे.", roman: "malA tijorIchI suvIdhA havI Ahe." },
    { en: "Sir, I am not married", mr: "साहेब माझे लग्न झाले नाही आहे.", roman: "sAheb mAjhe lagn jhAle nAhI Ahe." },
    { en: "What are the Darshan timings?", mr: "मंदिराची दर्शनाची वेळ काय आहे", roman: "maMdirAchI darshanAchI veL kAy Ahe" },
    { en: "When is it crowded more?", mr: "गर्दी कधी जास्त असते?", roman: "gardI kadhI jAst asate?" },
    { en: "What is timing for Prasad?", mr: "प्रसादची वेळ काय आहे?", roman: "prasAdachI veL kAy Ahe?" },
    { en: "Afternoon 12 to 2", mr: "दुपारी बारा ते दोन.", roman: "dupArI bArA te don." },
    { en: "There are 4 halls for Prasad", mr: "तिथे चार प्रसाद भवन आहेत.", roman: "tithe chAr prasAd bhavan Ahet." },
    { en: "Hey Buddy, whats up?", mr: "मित्रा! काय म्हणतोस?", roman: "mitrA! kAy mhaNatos?" },
    { en: "How was it?", mr: "कशी झाली?", roman: "kashI jhAlI?" },
    { en: "Quite exciting", mr: "जबरदस्त.", roman: "jabaradast." },
    { en: "With whom?", mr: "कोणाबारोबर होती?", roman: "koNAbArobar hotI?" },
    { en: "Who did win then?", mr: "मग कोण जिंकलं?", roman: "mag koN jiMkalM?" },
    { en: "Is it a question? It's we!", mr: "हे काय विचारणं झालं? आम्हीच.", roman: "he kAy vichAraNM jhAlM? AmhIch." },
    { en: "Nice! Congratulations", mr: "वा. अभिनंदन.", roman: "vA. abhinMdan." },
    { en: "I am a defender", mr: "नाही रे. मी तर डिफेंडर आहे.", roman: "nAhI re. mI tar DipheMDar Ahe." },
    { en: "Do inform me for next match", mr: "पुढच्या वेळी तुझी मॅच असेल तेव्हा मला आधी सांग.", roman: "puDhachyA veLI tujhI m~ach asel tevhA malA AdhI sAMg." },
    { en: "But that movie hasn't been released yet", mr: "पण तो सिनेमा अजून रिलीज झाला नाही.", roman: "paN to sinemA ajUn rilIj jhAlA nAhI." },
    { en: "Rajnikant is in that movie", mr: "त्यामध्ये रजनीकांत आहे.", roman: "tyAmadhye rajanIkAMt Ahe." },
    { en: "I am fan of Messi. Supporting Argentina", mr: "मी मेस्सीचा फॅन आहे त्यामुळे मी अर्जेंटिनाला सपोर्ट करतो आहे.", roman: "mI messIchA ph~an Ahe tyAmuLe mI arjeMTinAlA saporT karato Ahe." },
    { en: "I am Ronaldo fan but supporting Brazil", mr: "मी रोनाल्डोचा फॅन आहे पण मी ब्राझीलला सपोर्ट करतो आहे.", roman: "mI ronAlDochA ph~an Ahe paN mI brAjhIlalA saporT karato Ahe." },
    { en: "He dives very well", mr: "तो खूप छान झेप घेतो.", roman: "to khUp ChAn jhep ghetto." },
    { en: "Where is your class?", mr: "तुझा क्लास कुठे आहे?", roman: "tujha klas kuthe aahe?" },
    { en: "How much is fee?", mr: "फी किती आहे?", roman: "phI kitI aahe?" },
    { en: "Can I join too?", mr: "मी पण क्लास लावू शकतो का?", roman: "mI paN klAs lAvU shakato kA?" },
    { en: "New batch will start soon", mr: "पण नवीन बॅच लवकरच सुरू होते आहे.", roman: "paN navIn b~ach lavakarach surU hote aahe." },
    { en: "He/She is hungry", mr: "त्याला/तीला भूक लागली आहे", roman: "tyAlA/tIlA bhUk laagalI Ahe" },
    { en: "They are hungry", mr: "त्यांना भूक लागली आहे", roman: "tyAMnA bhUk laagalI Ahe" },
    { en: "I am not hungry", mr: "मला भूक नाही लागली आहे", roman: "malA bhUk nAhI laagalI Ahe" },
    { en: "Favorite sport", mr: "सर्वांत आवडता खेळ", roman: "sarvAMt AvaDatA kheL" },
    { en: "Favorite song", mr: "सर्वांत आवडते गाणे", roman: "sarvAMt AvaDate gANe" },
    { en: "He is waiting for me", mr: "तो माझी वाट बघतोय", roman: "to mAjhI vAT baghatoy" },
    { en: "She will wait for you", mr: "ती तुझी वाट बघेल", roman: "tI tujhI vAT baghel" },
    { en: "Is it ok if I sit here?", mr: "मी इथे बसलो तर चालेल का?", roman: "mI ithe basalo tar chAlel kA?" },
    { en: "Is it ok if he sits here?", mr: "तो इथे बसला तर चालेल का?", roman: "to ithe basala tar chAlel kA?" },
    { en: "Is it ok if they play on terrace?", mr: "ते गच्चीवर खेळले तर चालेल का?", roman: "te gachchIvar kheLale tar chAlel kA?" },
    { en: "He had worn suit when he met me", mr: "तो मला भेटलो तेव्हा त्याने सूट घातला होता", roman: "to malA bheTalo tevhA tyAne sUT ghAtalA hotA" },
    { en: "I believe you", mr: "माझा तुझ्यावर विश्वास आहे", roman: "mAjhA tujhyAvar vishvAs Ahe" },
    { en: "She believed me", mr: "तीचा माझ्यावर विश्वास होता", roman: "tIchA mAjhyAvar vishvAs hotA" },
    { en: "I cleaned house", mr: "मी घराची साफसफाई केली", roman: "mI gharAchI sAphasaphAI kelI" },
    { en: "We burst crackers", mr: "आम्ही फटाके फोडले / वाजवले", roman: "AmhI phaTAke phoDale / vAjavale" },
    { en: "I went everywhere and ate mithai", mr: "मी सगळीकडे गेलो आणि मिठाई खाल्ली", roman: "mI sagaLIkaDe gelo ANi miThAI khAllI" },
    { en: "I light the lantern and decorate house", mr: "मी कंदील लावतो आणि घर सजवतो", roman: "mI kMdIl lAvato ANi ghar sajavato" },
    { en: "Crackers cause air and sound pollution", mr: "फटाक्यांमुळे वायू आणि ध्वनी प्रदूषण होते", roman: "phaTAkyAMmuLe vAyU ANi dhvanI pradUShaN hote" },
    { en: "When will you be back?", mr: "तू कधी परत येणार आहेस?", roman: "tU kadhI parat yeNAr Ahes?" },
    { en: "Let's have a lot of fun there", mr: "आपण तिकडे खूप मजा करूया", roman: "ApaN tikaDe khUp majA karUyA" },
    { en: "Will you like to join?", mr: "तुला join करायला आवडेल का?", roman: "tulA join karAyalA AvaDel kA?" },
    { en: "I like to join", mr: "मला join करायला आवडतं", roman: "malA join karAyalA AvaDatM" },
    { en: "We ate cake in party", mr: "आम्ही पार्टी मध्ये केक खाल्ला", roman: "AmhI pArTI madhye kek khAllA" },
    { en: "Who brought the cake?", mr: "केक कोणी आणला", roman: "kek koNI ANalA" },
    { en: "Do not disturb me", mr: "मला disturb करू नकोस", roman: "malA disturb karU nakos" },
    { en: "Roll the chapatis", mr: "पोली लाट", roman: "polI lAT" },
    { en: "Grate the coconut", mr: "नारळ किसून घ्या", roman: "nAraL kisUn ghyA" },
    { en: "Put the clothes to dry", mr: "कपडे वाळत घाला", roman: "kapaDe vALat ghAlA" },
    { en: "Soak the clothes", mr: "कपडे भिजवा", roman: "kapaDe bhijavA" },
    { en: "Untangle it", mr: "तो सोडवा", roman: "to soDavA" },
    { en: "He ripped my bag", mr: "त्याने माझी बॅग फाडली", roman: "tyAne mAjhI b~ag phADalI" },
    { en: "Throw it away", mr: "ते फेका", roman: "te phekA" },
    { en: "I am in debt", mr: "मी कर्जात आहे", roman: "mI karjAt Ahe" },
    { en: "It went well", mr: "चांगलं झालं", roman: "chAMgalM jhAlM" },
    { en: "Close the lid", mr: "झाकण बंद करा", roman: "jhAkaN bMd karA" },
    { en: "The cabbage and onion are in the pot", mr: "कोबी आणि कांदा भांड्यात आहे", roman: "kobI ANi kAMdA bhAMDyAt Ahe" },
    { en: "After getting up I shower", mr: "उठल्यानंतर मी अंघोळ करते", roman: "uThalyAnMtar mI aMghoL karate" },
    { en: "I just moved here", mr: "मी तर नुकताच इकडे राहायला आलो", roman: "mI tar nukatAch ikaDe rAhAyalA Alo" },
    { en: "My native language is English", mr: "माझी मातृभाषा इंग्रजी आहे", roman: "mAjhI mAtRubhAShA iMgrajI Ahe" },
    { en: "I speak American English", mr: "मी अमेरिकन इंग्रजी बोलते", roman: "mI amerikan iMgrajI bolate" },
    { en: "I live close to the sea", mr: "मी समुद्राजवळ राहते", roman: "mI samudrAjavaL rAhate" },
    { en: "In front of my house you can see a castle", mr: "माझ्या घरासमोर आपण किल्ला पाहू शकता", roman: "mAjhyA gharAsamor ApaN killA pAhU shakatA" },
    { en: "Can you sing?", mr: "तुला गाता येते का?", roman: "tulA gAtA yete kA?" },
    { en: "Ok let it dry", mr: "बर, वाळूदे", roman: "bar, vALUde" },
    { en: "The amount of information is too much", mr: "माहितीचे प्रमाण खूप जास्त होते", roman: "mAhitIche pramAN khUp jAst hote" },
    { en: "I have mixed feelings towards social media", mr: "सोशल मीडियाबद्दल माझ्या संमिश्र भावना आहेत", roman: "soshal mIDiyAbaddal mAjhyA sMmishr bhAvanA Ahet" },
    { en: "Therefore I also left", mr: "म्हणून मीसुद्धा फेसबुक सोडले", roman: "mhaNUn mIsuddhA phesabuk soDale" },
    { en: "Now I only use linkedin", mr: "आता मी फक्त लिंक्डइन वापरतो", roman: "AtA mI phakt liMkDin vAparato" },
    { en: "Social media can be so addictive", mr: "सोशल मीडिया व्यसन लागू शकते", roman: "soshal mIDiyA vyasan lAgU shakate" },
    { en: "Social Media is a bad habit for many people", mr: "बर्‍याच लोकांसाठी सोशल मीडिया वाइट सवय आहे", roman: "baryAch lokAMsAThI soshal mIDiyA vAiT savay Ahe" },
    { en: "Yes, I have", mr: "हो माझ्याकडे आहे", roman: "ho mAjhyAkaDe Ahe" },
    { en: "Very nice!", mr: "खूप खूप छान", roman: "khUp khUp ChAn" },
    { en: "See you again", mr: "परत भेटू", roman: "parat bheTU" },
    { en: "I am so lucky to have you in my life", mr: "माझ्या आयुष्यात तू असण्यामुळे मी खूप नशीबवान आहे", roman: "mAjhyA AyuShyAt tU asaNyAmuLe mI khUp nashIbavAn Ahe" },
    { en: "And that horse was very young", mr: "आणि तो अगदी तरुण घोडा होता", roman: "ANi to agadI taruN ghoDA hotA" },
    { en: "I like those poor lenient horses", mr: "ते बिचारे खूपच आवडतात मला", roman: "te bichAre khUpach AvaDatAt malA" },
    { en: "These are steps in my life", mr: "तर माझ्या ह्याच्यात lifeमध्ये ते पायऱ्या आहेत", roman: "tar mAjhyA hyAchyAt lifemadhye te pAyryA Ahet" },
    { en: "I will not get a jump. And I don't want it either", mr: "मला कधी jump नाही मिळणार. आणि मला ती हवी पण नाहीये की", roman: "malA kadhI jump nAhI miLaNAr. ANi malA tI havI paN nAhIye kI" },
    { en: "So I am enjoying", mr: "म्हणून मी मस्त मजे घेत घेत", roman: "mhaNUn mI mast maje ghet ghet" },
    { en: "You should appreciate it", mr: "त्याला तुम्ही appreciate करायला पाहिजे जाताना", roman: "tyAlA tumhI appreciate karAyalA pAhije jAtAnA" },
    { en: "I had a bond with Abdul. I had a fight with MC once", mr: "अब्दुल सोबत माझा bond होता. MC सोबत तर माझी fight ही झाली होती एकदा", roman: "abdul sobat mAjhA bond hotA. MC sobat tar mAjhI fight hI jhAlI hotI ekadA" },
    { en: "You are a fool. You don't have an iota of intelligence", mr: "तू मूर्ख/बावळट आहेस. तुला काडीची अक्कल नाही", roman: "tU mUrkh/bAvaLaT Ahes. tulA kADIchI akkal nAhI" },
    { en: "Don't talk too much. Keep quiet", mr: "जास्त बोलू नकोस. गप्प बस", roman: "jAst bolU nakos. gapp bas" },
    { en: "I will do whenever its possible for me", mr: "जमेल तेव्हा करीन काम", roman: "jamel tevhA karIn kAm" },
    { en: "Afternoon", mr: "दुपार", roman: "dupAr" },
    { en: "at afternoon", mr: "दुपारी", roman: "dupArI" },
    { en: "when", mr: "कधी / केव्हा", roman: "kadhI / kevhA" },
    { en: "Now", mr: "आत्ता", roman: "AttA" },
    { en: "I am in office now", mr: "मी आत्ता ऑफिसमध्ये आहे", roman: "mI AttA ophisamadhye Ahe" },
    { en: "When will she dance?", mr: "ती कधी/केव्हा नाचेल?", roman: "tI kadhI/kevhA nAchel?" },
    { en: "January", mr: "जानेवारी", roman: "jAnevArI" },
    { en: "February", mr: "फेब्रुवारी", roman: "phebruvArI" },
    { en: "March", mr: "मार्च", roman: "mArch" },
    { en: "April", mr: "एप्रिल", roman: "epril" },
    { en: "May", mr: "मे", roman: "me" },
    { en: "June", mr: "जून", roman: "jUn" },
    { en: "July", mr: "जुलै", roman: "julai" },
    { en: "August", mr: "ऑगस्ट", roman: "ogasT" },
    { en: "September", mr: "सप्टेंबर", roman: "sapTeMbar" },
    { en: "October", mr: "ऑक्टोबर", roman: "okTobar" },
    { en: "November", mr: "नोव्हेंबर", roman: "novheMbar" },
    { en: "December", mr: "डिसेंबर", roman: "DiseMbar" },
    { en: "Its main purpose is to give equal rights and honour women", mr: "समाजातील महिलांना समान अधिकार देणे आणि सन्मान करणे हा त्याचा मुख्य उद्देश आहे", roman: "samAjAtIl mahilAMnA samAn adhikAr deNe ANi sanmAn karaNe hA tyAchA mukhy uddesh Ahe" },
    { en: "Every woman's place in our life is special", mr: "प्रत्येक 'ती'चं आपल्या आयुष्यातील स्थान अतिशय महत्त्वाचे-खास आहे", roman: "pratyek tI chM ApalyA AyuShyAtIl sthAn atishay mahattvAche-khAs Ahe" },
    { en: "Greetings", mr: "शुभेच्छा", roman: "shubhechChA" },
    { en: "Many Greetings", mr: "अनेकानेक शुभेच्छा", roman: "anekAnek shubhechChA" },
    { en: "Happy Diwali", mr: "दिवाळीच्या हार्दिक शुभेच्छा", roman: "divaLIchyA hArdik shubhechChA" },
    { en: "Merry X'mas", mr: "नाताळ्च्या/ख्रिसमसच्या हार्दिक शुभेच्छा", roman: "nAtALchyA/khrisamasachyA hArdik shubhechChA" },
    { en: "Congratulations", mr: "अभिनंदन", roman: "abhinaMdan" },
    { en: "I love you", mr: "माझे तुझ्यावर प्रेम आहे", roman: "mAjhe tujhyAvar prem Ahe" },
    { en: "Live long life", mr: "आयुष्मान भव", roman: "AyuShmAn bhava" },
    { en: "Be successful", mr: "यशस्वी भव", roman: "yashasvI bhava" },
    { en: "Live long life", mr: "चिरंजीव भव", roman: "chiraMjIv bhava" },
    { en: "May your pair lives forever", mr: "अखंडसौभाग्यवती भव", roman: "akhaMDasaubhAgyavatI bhava" },
    { en: "Bless me", mr: "मला आशिर्वाद द्या", roman: "malA AshirvAd dyA" },
    { en: "Long live!", mr: "जिंदाबाद", roman: "jiMdAbAd" },
    { en: "Long live India", mr: "भारत जिन्दाबाद", roman: "bhArat jindAbAd" },
    { en: "Down with inflation", mr: "महागाई मुर्दाबाद", roman: "mahAgAI murdAbAd" },
    { en: "Victory be of India", mr: "भारताचा विजय असो", roman: "bhAratAchA vijay aso" },
    { en: "Gift with love", mr: "सप्रेम भेट", roman: "saprem bheT" },
    { en: "Festival", mr: "उत्सव", roman: "utsav" },
    { en: "Religious festival", mr: "सण", roman: "saN" },
    { en: "Diwali", mr: "दिवाळी / दीपावली", roman: "diwALI / dIpAvalI" },
    { en: "Greeting", mr: "दीपावलीच्या हार्दिक शुभेच्छा!", roman: "dIpAvalIchyA hardik shubhechChA!" },
    { en: "Lamp", mr: "दिवा", roman: "divA" },
    { en: "Oil", mr: "तेल", roman: "tel" },
    { en: "Cotton wick", mr: "वात", roman: "vAt" },
    { en: "Lantern", mr: "कंदील", roman: "kaMdIl" },
    { en: "Door garland", mr: "तोरण", roman: "toraN" },
    { en: "Front yard", mr: "अंगण", roman: "aMgaN" },
    { en: "Prasad", mr: "प्रसाद", roman: "prasAd" },
    { en: "Crackers", mr: "फटाके", roman: "phaTAke" },
    { en: "To burst crackers", mr: "फटाके फोडणे/वाजवणे/उडवणे", roman: "phaTAke phoDaNe/vAjavaNe/uDavaNe" },
    { en: "Sweets", mr: "मिठाई", roman: "miThAI" },
    { en: "Snacks & sweets", mr: "फराळ", roman: "pharAL" },
    { en: "To have snacks", mr: "फराळ करणे", roman: "pharAL karaNe" },
    { en: "Diwali edition", mr: "दिवाळी अंक", roman: "divALI aMk" },
    { en: "Magazine", mr: "मासिक", roman: "mAsik" },
    { en: "King", mr: "राजा / महाराज", roman: "rAjA / mahArAj" },
    { en: "Soldiers", mr: "शिपाई", roman: "shipAI" },
    { en: "Fort", mr: "किल्ला", roman: "killA" },
    { en: "To build fort", mr: "किल्ला बांधणे", roman: "killA bAMdhaNe" },
    { en: "How are you (to boy)", mr: "तू कसा आहेस", roman: "tU kasA Ahes" },
    { en: "How are you (to girl)", mr: "तू कशी आहेस", roman: "tU kashI Ahes" },
    { en: "How are you (to man/lady)", mr: "तुम्ही कसे आहात", roman: "tumhI kase AhAt" },
    { en: "How do you do (to boy)", mr: "तू काय म्हणतोस", roman: "tU kAy mhaNatos" },
    { en: "How do you do (to girl)", mr: "तू काय म्हणतेस", roman: "tU kAy mhaNates" },
    { en: "How do you do (to man/lady)", mr: "तुम्ही काय म्हणता", roman: "tumhI kAy mhaNatA" },
    { en: "I am fine", mr: "मी मजेत आहे", roman: "mI majet Ahe" },
    { en: "I am ok", mr: "मी ठीक आहे", roman: "mI ThIk Ahe" },
    { en: "What do you do? (to boy)", mr: "सध्या काय करतो आहेस", roman: "sadhyA kAy karato Ahes" },
    { en: "What do you do? (to man/lady)", mr: "सध्या काय करत आहात", roman: "sadhyA kAy karat AhAt" },
    { en: "Where do you stay? (to boy)", mr: "तू कुठे राहतोस", roman: "tU kuThe rAhatos" },
    { en: "Where do you stay? (to man/lady)", mr: "तुम्ही कुठे राहता", roman: "tumhI kuThe rAhatA" },
    { en: "Give my regards to uncle", mr: "काकांना माझा नमस्कार सांग", roman: "kAkAMnA mAjhA namaskAr sAMg" },
    { en: "Bye bye", mr: "टा टा", roman: "TA TA" },
    { en: "See you again", mr: "परत भेटू / भेटुया", roman: "parat bheTU / bheTuyA" },
    { en: "When will we see again?", mr: "परत कधी भेटणार?", roman: "parat kadhI bheTaNAr?" },
    { en: "Ok", mr: "ठीक / ठीक आहे", roman: "ThIk / ThIk Ahe" },
    { en: "It was nice to see that", mr: "हे बघून बरं वाटलं की", roman: "he baghUn baraM vATalM kI" },
    { en: "Hey lad/boy", mr: "अरे मुला / बाळा", roman: "are mulA / bALA" },
    { en: "Uncle!", mr: "अहो काका", roman: "aho kAkA" },
    { en: "Aunty!", mr: "अहो काकू / अहो मावशी", roman: "aho kAkU / aho mAvashI" },
    { en: "Hey! How are you? (to boy)", mr: "कायरे? कसा आहेस?", roman: "kAyare? kasA Ahes?" },
    { en: "Hey! How are you? (to girl)", mr: "कायगं? कशी आहेस?", roman: "kAyagaM? kashI Ahes?" },
    { en: "Why?", mr: "का?", roman: "kA?" },
    { en: "I want passenger to Kothrud, Baner", mr: "मला कोथरूड, बाणेरचे भाडे हवे आहे", roman: "malA kotharUD, bANerache bhADe have aahe" },
    { en: "Will you charge by meter?", mr: "मीटरने येणार ना?", roman: "mITarane yeNAr nA?" },
    { en: "How much is fare?", mr: "किती झाले?", roman: "kitI jhAle" },
    { en: "Forty rupees", mr: "चाळीस रुपये", roman: "chALIs rupaye" },
    { en: "I am telling as per meter only", mr: "मीटर प्रमाणेच सांगतो आहे", roman: "mITar pramANech sAMgato aahe" },
    { en: "I don't have change for 100", mr: "माझ्याकडे शंभरचे सुट्टे नाहीत", roman: "mAjhyAkaDe shaMbharache suTTe nAhIt" },
    { en: "Take these remaining 10 rupees", mr: "हे घ्या बाकीचे दहा रुपये", roman: "he ghyA bAkIche dahA rupaye" },
    { en: "Where will I get share auto to Swargate?", mr: "स्वारगेटला शेअर रिक्शा कुठून मिळतील?", roman: "svArageTalA shear rikshA kuThUn miLatIl" },
    { en: "From next square", mr: "पुढच्या चौकातून", roman: "puDhachyA chaukAtUn" },
    { en: "Can you take me to Swargate? By share?", mr: "स्वारगेटला जाणार का? शेअर ने?", roman: "svArageTalA jANAr kA? shear ne?" },
    { en: "Left", mr: "डावे", roman: "DAve" },
    { en: "To left", mr: "डावीकडे", roman: "DAvIkaDe" },
    { en: "Right", mr: "उजवे", roman: "ujave" },
    { en: "To right", mr: "उजवीकडे", roman: "ujavIkaDe" },
    { en: "Next", mr: "पुढे", roman: "puDhe" },
    { en: "Far", mr: "लांब", roman: "lAMb" },
    { en: "Square", mr: "चौक", roman: "chauk" },
    { en: "Corner", mr: "कोपरा", roman: "koparA" },
    { en: "Lane", mr: "गल्ली / बोळ", roman: "gallI / boL" },
    { en: "Bridge", mr: "पूल", roman: "pUl" },
    { en: "Follow the Kesari flag after getting down", mr: "बसमधून उतरल्यावर केसरीच्या झेंड्याच्या मागोमाग जा.", roman: "basamadhUn utaralyAvar kesarIchyA jheMDyAchyA mAgomAg jA." },
    { en: "Do not loose it", mr: "ते हरवू नका.", roman: "te haravU nakA." },
    { en: "I reached there somehow", mr: "मी तिकडे कसातरी पोचलो", roman: "mI tikaDe kasAtarI pochalo" },
    { en: "I will reach there anyhow", mr: "मी तिकडे कसाही पोचेन", roman: "mI tikaDe kasAhI pochen" },
    { en: "At least he came", mr: "तो तरी आला", roman: "to tarI AlA" },
    { en: "You should have told me at least", mr: "तू मला तरी सांगायला हवे होतेस", roman: "tU malA tarI saMgAyalA have hotes" },
    { en: "He did not even tell it to me", mr: "त्याने मला हे सांगितलेही नाही", roman: "tyAne malA he sAMgitalehI nAhI" },
    { en: "Everywhere", mr: "प्रत्येक ठिकाणी / सगळीकडे / सर्वत्र", roman: "pratyek ThikANI / sagaLIkaDe / sarvatr" },
    { en: "Pupil", mr: "डोळ्याची बाहुली", roman: "DoLyAchI bAhulI" },
    { en: "Nostril", mr: "नाकपुडी", roman: "nAkapuDI" },
    { en: "Cheek", mr: "गाल", roman: "gAl" },
    { en: "Moustache", mr: "मिशी", roman: "mishI" },
    { en: "Lip", mr: "ओठ", roman: "oTh" },
    { en: "Jaw", mr: "जबडा", roman: "jabaDA" },
    { en: "Gum", mr: "हिरडी", roman: "hiraDI" },
    { en: "Outerside of Throat", mr: "गळा", roman: "gaLA" },
    { en: "Innerside of throat / Pharynx", mr: "घसा", roman: "ghasA" },
    { en: "Neck", mr: "मान", roman: "mAn" },
    { en: "Shoulder", mr: "खांदा", roman: "khAMdA" },
    { en: "Breast", mr: "स्तन", roman: "stan" },
    { en: "Chest", mr: "छाती", roman: "ChAtI" },
    { en: "Lung", mr: "फुफ्फुस", roman: "phuphphus" },
    { en: "Back", mr: "पाठ", roman: "pATh" },
    { en: "Arm", mr: "दंड", roman: "daMD" },
    { en: "Elbow", mr: "कोपर", roman: "kopar" },
    { en: "Wrist", mr: "मनगट", roman: "managaT" },
    { en: "Palm", mr: "पंजा", roman: "paMjA" },
    { en: "Sole of palm", mr: "तळहात", roman: "taLahAt" },
    { en: "Fist", mr: "मूठ", roman: "mUTh" },
    { en: "Thumb", mr: "अंगठा", roman: "aMgaThA" },
    { en: "Nail", mr: "नख", roman: "nakh" },
    { en: "Stomach", mr: "पोट", roman: "poT" },
    { en: "Belly button", mr: "बेंबी", roman: "beMbI" },
    { en: "Waist", mr: "कंबर", roman: "kaMbar" },
    { en: "Groin", mr: "जांघ", roman: "jAMgh" },
    { en: "Penis", mr: "शिस्न", roman: "shisn" },
    { en: "Vulva / Vagina", mr: "योनी", roman: "yonI" },
    { en: "Knee", mr: "गुडघा", roman: "guDaghA" },
    { en: "Calf", mr: "पोटरी", roman: "poTarI" },
    { en: "Ankle", mr: "घोटा", roman: "ghoTA" },
    { en: "Foot", mr: "पाऊल", roman: "pAUl" },
    { en: "Sole of foot", mr: "तळवा", roman: "taLavA" },
    { en: "Heel", mr: "टाच", roman: "TAch" },
    { en: "Toe", mr: "चवडा", roman: "chavaDA" },
    { en: "Blood", mr: "रक्त", roman: "rakt" },
    { en: "Ostrich", mr: "शहामृग", roman: "shahAmRug" },
    { en: "Cock", mr: "कोंबडा", roman: "koMbaDA" },
    { en: "Hen", mr: "कोंबडी", roman: "koMbaDI" },
    { en: "Sparrow", mr: "चिमणी", roman: "chimaNI" },
    { en: "Peacock", mr: "मोर", roman: "mor" },
    { en: "Crane", mr: "बगळा", roman: "bagaLA" },
    { en: "Stork", mr: "करकोचा", roman: "karakochA" },
    { en: "Eagle", mr: "गरूड", roman: "garUD" },
    { en: "Parrot", mr: "पोपट", roman: "popaT" },
    { en: "Duck", mr: "बदक / बतख", roman: "badak / batakh" },
    { en: "Owl", mr: "घुबड", roman: "ghubaD" },
    { en: "Pigeon", mr: "कबूतर", roman: "kabUtar" },
    { en: "Cuckoo", mr: "कोकिळा", roman: "kokiLA" },
    { en: "Kite", mr: "घार", roman: "ghAr" },
    { en: "Vulture", mr: "गिधाड", roman: "gidhAD" },
    { en: "Woodpecker", mr: "सुतार", roman: "sutAr" },
    { en: "Crow", mr: "कावळा", roman: "kAvaLA" },
    { en: "Ant", mr: "मुंगी", roman: "muMgI" },
    { en: "Bed bug", mr: "ढेकुण", roman: "DhekuN" },
    { en: "Butterfly", mr: "फुलपाखरू", roman: "phulapAkharU" },
    { en: "Spider", mr: "कोळी", roman: "koLI" },
    { en: "Cockroach", mr: "झुरळ", roman: "jhuraL" },
    { en: "Beetle", mr: "भुंगा", roman: "bhuMgA" },
    { en: "Fly", mr: "माशी", roman: "mAshI" },
    { en: "Mosquito", mr: "डास", roman: "DAs" },
    { en: "Lizard", mr: "सरडा", roman: "saraDA" },
    { en: "House Lizard", mr: "पाल", roman: "pAl" },
    { en: "Flea", mr: "पिसू", roman: "pisU" },
    { en: "Centipede", mr: "गोम / घोण", roman: "gom / ghoN" },
    { en: "Buffalo", mr: "म्हैस", roman: "mhais" },
    { en: "Camel", mr: "उंट", roman: "uMT" },
    { en: "Cheetah", mr: "चित्ता", roman: "chittA" },
    { en: "Cow", mr: "गाय", roman: "gAy" },
    { en: "Deer", mr: "हरीण", roman: "harIN" },
    { en: "Donkey", mr: "गाढव", roman: "gADhav" },
    { en: "Elephant", mr: "हत्ती", roman: "hattI" },
    { en: "Fox", mr: "कोल्हा", roman: "kolhA" },
    { en: "Frog", mr: "बेडूक", roman: "beDUk" },
    { en: "Giraffe", mr: "जिराफ", roman: "jirAph" },
    { en: "Horse", mr: "घोडा", roman: "ghoDA" },
    { en: "Lion", mr: "सिंह", roman: "siMh" },
    { en: "Monkey", mr: "माकड", roman: "mAkaD" },
    { en: "Ox", mr: "बैल", roman: "bail" },
    { en: "Pig", mr: "डुक्कर", roman: "Dukkar" },
    { en: "Rabbit", mr: "ससा", roman: "sasA" },
    { en: "Mouse", mr: "उंदीर", roman: "uMdIr" },
    { en: "Sheep", mr: "मेंढी", roman: "meMDhI" },
    { en: "Squirrel", mr: "खार", roman: "khAr" },
    { en: "Tiger", mr: "वाघ", roman: "vAgh" },
    { en: "Wolf", mr: "लांडगा", roman: "lAMDagA" },
    { en: "Zebra", mr: "झेब्रा", roman: "jhebrA" },
    { en: "Fifth", mr: "पाचवा", roman: "pAchavA" },
    { en: "Quarter", mr: "पाव", roman: "pAv" },
    { en: "What if I hold 2 connections?", mr: "माझ्याकडे 2 कनेक्शन असतील तर?", roman: "majhyakade 2 kanekshan asatil tar?" },
    { en: "Yes, type in 1234 and 5678", mr: "हो 1234 आणि 5678 टाइप करा.", roman: "ho 1234 ani 5678 taip kara." },
    { en: "Do I need to submit any request form?", mr: "बरं, त्यासाठी काही अर्ज द्यावा लागतो का?", roman: "barM, tyAsAThI kAhI arj dyAvA lAgato kA?" },
    { en: "Will I need to resubmit ID proofs?", mr: "बरं. आणि सगळी कागदपत्रं परत सादर करायची गरज पडेल का?", roman: "barM. ANi sagaLI kAgadapatrM parat sAdar karAyachI garaj paDel kA?" },
    { en: "How long will it take?", mr: "नंबर लिंक होण्यासाठी किती दिवस लागतील?", roman: "naMbar liMk hoNyAsAThI kitI divasa lAgatIl?" },
    { en: "No problem", mr: "काही हरकत नाही", roman: "kAhI harakat nAhI" },
    { en: "Banana (raw)", mr: "कच्चे केळे", roman: "kachche keLe" },
    { en: "French Beans", mr: "फरसबी", roman: "pharasabI" },
    { en: "Beetroot", mr: "बीट", roman: "beeT" },
    { en: "Bell Pepper/Capsicum", mr: "ढोबळी मिर्ची / सिमला मिर्ची", roman: "DhobaLI mirchI" },
    { en: "Cabbage", mr: "कोबी", roman: "kobI" },
    { en: "Cilantro", mr: "कोथिंबिर", roman: "kothiMbir" },
    { en: "Cluster Beans", mr: "गवार", roman: "gavAr" },
    { en: "Cucumber", mr: "काकडी", roman: "kAkaDI" },
    { en: "Drumstick", mr: "शेवग्याची शेंग", roman: "shevagyAchI sheMg" },
    { en: "Garlic", mr: "लसूण", roman: "lasUN" },
    { en: "Green Peas", mr: "वाटाणा", roman: "vATANA" },
    { en: "Onion", mr: "कांदा", roman: "kAMdA" },
    { en: "Potato", mr: "बटाटा", roman: "baTATA" },
    { en: "Pumpkin", mr: "भोपळा", roman: "bhopaLA" },
    { en: "Radish", mr: "मुळा", roman: "muLA" },
    { en: "Sweet Potato", mr: "रताळे", roman: "ratALe" },
    { en: "Tomato", mr: "टोमॅटो", roman: "TomaTo" },
    { en: "Ginger", mr: "आले", roman: "Ale" },
    { en: "Mint leaves", mr: "पुदिना", roman: "pudinA" },
    { en: "Fenugreek Leaves", mr: "मेथी", roman: "methI" },
    { en: "Coconut", mr: "नारळ", roman: "nAraL" },
    { en: "Lemon", mr: "लिंबु", roman: "liMbu" },
    { en: "Apple", mr: "सफरचंद", roman: "sapharachaMd" },
    { en: "Apricot", mr: "जर्दाळू", roman: "jardALU" },
    { en: "Banana", mr: "केळे", roman: "keLe" },
    { en: "Indian Black Berry / Jamun", mr: "जांभुळ", roman: "jAMbhuL" },
    { en: "Custard apple", mr: "सिताफळ", roman: "sitAphaL" },
    { en: "Dates", mr: "खजूर", roman: "khajoor" },
    { en: "Figs", mr: "अंजीर", roman: "aMjIr" },
    { en: "Grapes", mr: "द्राक्ष", roman: "drAkSha" },
    { en: "Guavas", mr: "पेरू", roman: "perU" },
    { en: "Muskmelon / Cantalope", mr: "खरबूज", roman: "kharabUj" },
    { en: "Olive", mr: "ऑलिव्ह", roman: "~olivh" },
    { en: "Orange", mr: "संत्रे", roman: "saMtre" },
    { en: "Papaya", mr: "पपई", roman: "papaI" },
    { en: "Pineapple", mr: "अननस", roman: "ananas" },
    { en: "Pomegranate", mr: "डाळिंब", roman: "DALiMb" },
    { en: "Sweet lime", mr: "मोसंबे", roman: "mosaMbe" },
    { en: "Strawberry", mr: "स्ट्रॉबेरी", roman: "sTr~oberI" },
    { en: "Jujube", mr: "बोर", roman: "bor" },
    { en: "Peach", mr: "पीच", roman: "pIch" },
    { en: "Is Idli available?", mr: "इडली आहे का?", roman: "iDalI Ahe kA?" },
    { en: "Can I get pizza?", mr: "पिझ्झा मिळेल का?", roman: "pijhjhA miLel kA?" },
    { en: "I want still more butter", mr: "मला अजून लोणी हवे आहे", roman: "malA ajUn loNI have Ahe" },
    { en: "Give the bill", mr: "बिल द्या", roman: "bil dyA" },
    { en: "How much is bill?", mr: "बिल किती झाले?", roman: "bil kitI jhAle?" },
    { en: "How much is 1 VadaPaav?", mr: "एक वडापाव कितीला?", roman: "ek vaDApAv kitIlA?" },
    { en: "How much is 1 Dosa?", mr: "एक डोसा कितीला?", roman: "ek DosA kitIlA?" },
    { en: "Give me 10 Vadas in parcel", mr: "मला दहा वडे पार्सल द्या", roman: "malA dahA vaDe pArsal dyA" },
    { en: "Do you have change?", mr: "सुट्टे पैसे आहेत का?", roman: "suTTe paise Ahet kA?" },
    { en: "I do not have change", mr: "सुट्टे नाहीत", roman: "suTTe nAhIt" },
    { en: "You will get idli", mr: "इडली मिळेल", roman: "iDalI miLel" },
    { en: "Pizza is not available", mr: "पिझ्झा मिळणार नाही", roman: "pijhjhA miLaNAr nAhI" },
    { en: "I thought coolness will continue", mr: "मला वाटले आजही गारवा राहील", roman: "malA vATale AjahI gAravA rAhIl" },
    { en: "What is the temperature now?", mr: "आत्ता तापमान किती आहे", roman: "AttA tApamAn kitI Ahe" },
    { en: "25 degree Celsius", mr: "पंचवीस अंश सेल्सिअस", roman: "paMchavIs aMsh selsias" },
    { en: "Air is fresh and pure there", mr: "तिथे हवा ताजी आणि शुद्ध आहे", roman: "tithe havA tAjI ANi shuddha Ahe" },
    { en: "How are you?", mr: "तुम्ही कशा आहात?", roman: "tumhI kashA AhAt?" },
    { en: "I am fine", mr: "मी ठीक आहे.", roman: "mI ThIk Ahe." },
    { en: "No aunty. I am not much hungry", mr: "नको काकू मला जास्त भूक नाहीये.", roman: "nako kAkU malA jAst bhUk nAhIye." },
    { en: "No, I am full now", mr: "नको, माझे पोट भरले आहे. आता मी जास्त नाही खाऊ शकत.", roman: "nakko, mAjhe poT bharale Ahe. AtA mI jAst nAhI khAU shakat." },
    { en: "She cooked Indian dishes", mr: "तिने भारतीय स्वयंपाक केला", roman: "tine bhAratIy svayaMpAk kelA" },
    { en: "I ate coconut chutney", mr: "मी नारळाची चटणी खाल्ली", roman: "mI nAraLAchI chaTaNI khAllI" },
    { en: "I prepared capsicum with gram flour", mr: "मी खूप चविष्ट ढब्बू मिरचीचे बेसन केले.", roman: "mI khUp chaviShT DhabbU mirachIche besan kele." },
    { en: "What is the problem?", mr: "काय होतंय?", roman: "kAy hotaMy?" },
    { en: "There is temperature", mr: "ताप आलाय", roman: "tAp AlAy" },
    { en: "From when?", mr: "कधीपासून?", roman: "kadhIpAsUn?" },
    { en: "Ok. Lay down there", mr: "बरं. तिकडे झोपा.", roman: "barM. tikaDe jhopA." },
    { en: "Let me see throat", mr: "घसा बघू", roman: "ghasA baghU" },
    { en: "Leave it", mr: "सोडा", roman: "soDA" },
    { en: "Take again", mr: "पुन्हा घ्या.", roman: "punhA ghyA." },
    { en: "OK. Sit there", mr: "ठीक आहे. बसा तिकडे.", roman: "ThIk Ahe. basA tikaDe." },
    { en: "Let me check pulse", mr: "नाडी बघू.", roman: "nADI baghU." },
    { en: "I check B.P.", mr: "बीपी चेक करतो.", roman: "bIpI chek karato." },
    { en: "Why is there temperature?", mr: "कशामुळे ताप आला असेल?", roman: "kashAmuLe tAp AlA asel?" },
    { en: "Do not take when empty stomach", mr: "रिकाम्या पोटी नका घेऊ", roman: "rikAmyA poTI nakA gheU" },
    { en: "OK. How much is fee?", mr: "ओके. किती फी झाली?", roman: "oke. kitI phI jhAlI?" },
    { en: "If temperature is normal then no need", mr: "ताप उतरला तर गरज नाही.", roman: "tAp utaralA tar garaj nAhI." },
    { en: "Yes. I have", mr: "आहे", roman: "Ahe" },
    { en: "Give 2 packs", mr: "दोन पुडे द्या", roman: "don puDe dyA" },
    { en: "Parle's", mr: "पारले चे आहे", roman: "pArale che Ahe" },
    { en: "Bournville is there", mr: "बोरबोन आहे", roman: "borabon Ahe" },
    { en: "It will do. Give 1 pack. How much is total bill?", mr: "चालेल. १ पुडा द्या. किती झाले?", roman: "chAlel. 1 puDA dyA. kitI jhAle?" },
    { en: "I do not have bag. Can you give me plastic bag?", mr: "माझ्याकडे पिशवी नाहिये. प्लॅस्टिकची पिशवी देता का?", roman: "mAjhyAkaDe pishavI nAhiye. pl~asTikachI pishavI detA kA?" },
    { en: "Look at every problem as an opportunity", mr: "आयुष्यात येणाऱ्या प्रत्येक समस्येला सामोरे जाताना त्या समस्येकडे एक संधी म्हणून बघा", roman: "AyuShyAt yeNAryA pratyek samasyelA sAmore jAtAnA tyA samasyekaDe ek sMdhI mhaNUn baghA" }
  ]
  },
  environment: {
    name: "Environment & Weather",
    words: [
    { en: "Hot", mr: "गरम", roman: "Garam" },
    { en: "Cold", mr: "थंड", roman: "Thaṇḍ" },
    { en: "Sun", mr: "सूर्य", roman: "sUrya" },
    { en: "I had opened window", mr: "मी खिडकी उघडलेली", roman: "mI khiDakI ughaDalelI" },
    { en: "Moving tree", mr: "हलणारे झाड", roman: "halaNAre jhAD" },
    { en: "Moved tree", mr: "हललेले झाड", roman: "halalele jhAD" },
    { en: "Do not pluck flowers", mr: "फुले तोडू नयेत", roman: "phule toDU nayet" },
    { en: "Set (sun,moon)", mr: "मावळणे mAvaLaNe", roman: "sUry mAvaLalA" },
    { en: "To plant a tree", mr: "झाड लावणे", roman: "jhAD lAvaNe" },
    { en: "Hot in taste", mr: "तिखट", roman: "tikhaT" },
    { en: "Sky Blue", mr: "आकाशी", roman: "AkAshI" },
    { en: "Royal poinciana / Peacock Flower", mr: "गुलमोहर", roman: "gulamohar" },
    { en: "Peacock Flower", mr: "शंकासुर", roman: "shaMkAsur" },
    { en: "Umbrella Tree / Screw pine", mr: "केवडा", roman: "kevaDA" },
    { en: "Indian Shot / Canna Indica", mr: "कर्दळ", roman: "kardaL" },
    { en: "Sunflower", mr: "सूर्यफूल", roman: "sUryaphUl" },
    { en: "Did it rain during your match?", mr: "तुमच्या मॅचच्या वेळी पाऊस पडला का?", roman: "tumachyA m~achachyA veLI pAUs paDalA kA?" },
    { en: "Yes it rained heavily", mr: "हो. भयंकर पाऊस झाला.", roman: "ho. bhayMkar pAUs jhAlA." },
    { en: "So I draw Rangoli of flowers", mr: "म्हणून मी फुलांची रांगोळी काढते", roman: "mhaNUn mI phulAMchI rAMgoLI kADhate" },
    { en: "I am going by train", mr: "मी ट्रेनने जाणार आहे", roman: "mI Trenane jANAr Ahe" },
    { en: "I live across the street", mr: "मी रस्त्याच्या पलिकडे राहतो", roman: "kharaMch. mI rastyAchyA palikaDe rAhato" },
    { en: "In India, Rahu and Ketu gulp the sun and moon", mr: "भारतात राहू आणि राक्षस सूर्य आणि चंद्राला गिळतात अशी कल्पना आहे", roman: "bhAratAt rAhU ANi rAkShas sUry ANi chMdrAlA giLatAt ashI kalpanA Ahe" },
    { en: "Sunday", mr: "रविवार", roman: "ravivAr" },
    { en: "Flower", mr: "फूल", roman: "phUl" },
    { en: "Same Aadhaar update form. Get from next photostat shop", mr: "होय, अ‍ॅक्च्युअली हा आधारपत्र वालाच फॉर्म भरायचा असतो. सध्या तुम्हाला पुढच्या फोटोस्टॅट शॉपमधून मिळून जाईल", roman: "hoy, ~akchyualI hA AdhArapatr vAlAch ph~orm bharAyachA asato. sadhyA tumhAlA puDhachyA phoTosT~aT sh~opamadhUn miLUn jAIl." },
    { en: "Aubergine/Eggplant/Brinjal", mr: "वांगे", roman: "vAMge" },
    { en: "Cauliflower", mr: "फुलकोबी", roman: "phulakobI" },
    { en: "It is very hot today", mr: "आज खूप गरम होते आहे", roman: "Aj khUp garam hote Ahe" },
    { en: "It is very hot and humid today", mr: "आज खूप उकडते आहे", roman: "Aj khUp ukaDate Ahe" },
    { en: "It is raining", mr: "पाऊस पडतो आहे", roman: "pAUs paDato Ahe" },
    { en: "It rained yesterday also", mr: "काल पण पाऊस पडला", roman: "kAl paN pAUs paDalA" },
    { en: "It was torrential rain", mr: "मुसळधार पाऊस पडला", roman: "musaLadhAr pAUs paDalA" },
    { en: "Many clouds are seen", mr: "बरेच ढग दिसत आहेत", roman: "barech Dhag disat Ahet" },
    { en: "It is cloudy now", mr: "आत्ता मळभ आहे", roman: "AttA maLabh aahe" },
    { en: "The sky is cloud-free", mr: "आकाश निरभ्र आहे", roman: "Akash nirabhra Ahe" },
    { en: "Good sunlight outside", mr: "बाहेर चांगले ऊन पडले आहे", roman: "bAher chAMgale Un paDale Ahe" },
    { en: "The wind is blowing fast", mr: "वारा जोरात वाहतो आहे", roman: "vArA jorAt vAhato Ahe" },
    { en: "I am suffering from cold", mr: "सर्दी झालिये", roman: "sardI jhAliye" }
  ]
  },
  food: {
    name: "Food & Drink",
    words: [
    { en: "Water", mr: "पाणी", roman: "Pāṇī" },
    { en: "Food", mr: "जेवण", roman: "Jevaṇ" },
    { en: "Mango", mr: "आंबा", roman: "AMbA" },
    { en: "Eat", mr: "खा", roman: "khA" },
    { en: "Beat", mr: "मार", roman: "mAr" },
    { en: "Drink", mr: "पी", roman: "pI" },
    { en: "Instead of", mr: "ऐवजी", roman: "aivajI" },
    { en: "You do not eat", mr: "तू खात नाहीस", roman: "tU khAt nAhIs" },
    { en: "You drink", mr: "तू पी", roman: "tU pI" },
    { en: "Rice cooked", mr: "भात शिजला", roman: "bhAt shijalA" },
    { en: "I cooked rice", mr: "मी भात शिजवला", roman: "mI bhAt shijavalA" },
    { en: "To drink", mr: "पीणे", roman: "pINe" },
    { en: "To cause to drink / To feed liquid", mr: "पाजणे", roman: "pAjaNe" },
    { en: "To eat", mr: "खाणे", roman: "khANe" },
    { en: "You have been eating mango", mr: "तुम्ही आंबा खात आला आहात", roman: "tumhI AMbA khAt AlA AhAt" },
    { en: "You had been eating mango", mr: "तुम्ही आंबा खात आला होतात", roman: "tumhI AMbA khAt AlA hotAt" },
    { en: "You will have been eating mango", mr: "तुम्ही आंबा खात आला असाल", roman: "tumhI AMbA khAt AlA asAl" },
    { en: "They (plural of he) used to eat mangos", mr: "ते आंबे खायचे", roman: "te AMbe khAyache" },
    { en: "They (plural of he) did not use to eat mangos", mr: "ते आंबे खायचे नाहीत", roman: "te AMbe khAyache nAhIT" },
    { en: "I used to eat mango", mr: "मी आंबा खात असे", roman: "mI AMbA khAt ase" },
    { en: "I used to eat mango", mr: "मी आंबा खाई", roman: "mI AMbA khAI" },
    { en: "For eating", mr: "खाण्यासाठी", roman: "khANyAsAThI" },
    { en: "Come to eat with me", mr: "माझ्याबरोबर जेवायला ये", roman: "mAjhyAbarobar jevAyalA ye" },
    { en: "I can eat", mr: "मी खाऊ शकतो", roman: "mI khAU shakato" },
    { en: "You(plural) could eat mango", mr: "तुम्ही आंबा खाऊ शकलात", roman: "tumhI AMbA khAU shakalAt" },
    { en: "You(plural) could eat chutney", mr: "तुम्ही चटणी खाऊ शकलात", roman: "tumhI chaTaNI khAU shakalAt" },
    { en: "I can not eat", mr: "मी खाऊ शकत नाही", roman: "mI khAU shakat nAhI" },
    { en: "You(plural) could not eat mango", mr: "तुम्ही आंबा खाऊ शकला नाहीत", roman: "tumhI AMbA khAU shakalA nAhIt" },
    { en: "You(plural) could not eat chutney", mr: "तुम्ही चटणी खाऊ शकला नाहीत", roman: "tumhI chaTaNI khAU shakalA nAhIt" },
    { en: "He can eat mangoes", mr: "त्याला आंबे खायला जमते", roman: "tyAlA AMbe khAyalA jamate" },
    { en: "He could eat mangoes", mr: "त्याला आंबे खायला जमले", roman: "tyAlA AMbe khAyalA jamale" },
    { en: "He will be able to eat mangoes", mr: "त्याला आंबे खायला जमेल", roman: "tyAlA AMbe khAyalA jamel" },
    { en: "I want mango", mr: "मला आंबा पाहिजे/हवा आहे", roman: "malA AMbA pAhije/havA Ahe" },
    { en: "He wants mango", mr: "त्याला आंबा पाहिजे/हवा आहे", roman: "tyAlA AMbA pAhije/havA Ahe" },
    { en: "She wants mango", mr: "तीला आंबा पाहिजे/हवा आहे", roman: "tIlA AMbA pAhije/havA Ahe" },
    { en: "I/He/She want mangoes", mr: "मला/त्याला/तीला आंबे पाहिजे/हवे आहेत", roman: "malA/tyAlA/tIlA AMbe pAhije/have Ahet" },
    { en: "I do not want mango", mr: "मला आंबा नको आहे", roman: "malA AMbA nako Ahe" },
    { en: "I do not want mango", mr: "मला आंबा नाही पाहिजे", roman: "malA AMbA nAhI pAhije" },
    { en: "He should eat mango", mr: "त्याने आंबा खायला पाहिजे/हवा", roman: "tyAne AMbA khAyalA pAhije/havA" },
    { en: "He should eat mango", mr: "त्याने आंबा खाल्ला पाहिजे", roman: "tyAne AMbA khAllA pAhije" },
    { en: "He should eat", mr: "त्याने खाल्ले पाहिजे", roman: "tyAne khAlle pAhije" },
    { en: "You(male) should eat mango", mr: "तू आंबा खाल्ला पाहिजेस", roman: "tU AMbA khAllA pAhijes" },
    { en: "He should not eat", mr: "त्याने खाल्ले नाही पाहिजे", roman: "tyAne khAlle nAhI pAhije" },
    { en: "He should eat mango", mr: "त्याने आंबा खावा", roman: "tyAne AMbA khAvA" },
    { en: "He should eat tamarind", mr: "त्याने चिंच खावी", roman: "tyAne chiMch khAvI" },
    { en: "You should eat mango", mr: "तू आंबा खावास", roman: "tU AMbA khAvAs" },
    { en: "She has to eat mango", mr: "तीला आंबा खायला/खावा लागतो", roman: "tIlA AMbA khAyalA/khAvA lAgato" },
    { en: "She will have to eat mango", mr: "तीला आंबा खायला/खावा लागेल", roman: "tIlA AMbA khAyalA/khAvA lAgel" },
    { en: "She had to eat mango", mr: "तीला आंबा खायला/खावा लागला", roman: "tIlA AMbA khAyalA/khAvA lAgalA" },
    { en: "She has to eat mangoes", mr: "तीला आंबे खायला/खावे लागतात", roman: "tIlA AMbe khAyalA/khAve lAgatAt" },
    { en: "She has to eat tamarind", mr: "तीला चिंच खायला/खावी लागते", roman: "tIlA chiMch khAyalA/khAvI lAgate" },
    { en: "She has to eat tamarinds", mr: "तीला चिंचा खायला/खाव्या लागतात", roman: "tIlA chiMchA khAyalA/khAvyA lAgatAt" },
    { en: "She has to eat medicine", mr: "तीला औषध खायला/खावे लागते", roman: "tIlA auShadh khAyalA/khAve lAgate" },
    { en: "She has to eat medicines", mr: "तीला औषधे खायला/खावी लागतात", roman: "tIlA auShadhe khAyalA/khAvI lAgatAt" },
    { en: "I know eating cake", mr: "मला केक खाता येतो", roman: "malA kek khAtA yeto" },
    { en: "I do not know eating cake", mr: "मला केक खाता येत नाही", roman: "malA kek khAtA yet nAhI" },
    { en: "Shall we eat mango? (style 1)", mr: "आंबा खाऊया का?", roman: "AMbA khAUyA kA?" },
    { en: "Shall we eat mango? (style 2)", mr: "आंबा खायचा का?", roman: "AMbA khAyachA kA?" },
    { en: "Shall we eat tamarind? (style 1)", mr: "चिंच खाऊया का?", roman: "chiMch khAUyA kA?" },
    { en: "Shall we eat tamarind? (style 2)", mr: "चिंच खायची का?", roman: "chiMch khAyachI kA?" },
    { en: "Let me eat", mr: "मला खाऊ दे", roman: "malA khAU de" },
    { en: "You all, Let me eat", mr: "मला खाऊ द्या", roman: "malA khAU dyA" },
    { en: "Don't let me eat", mr: "मला खाऊ देऊ नकोस", roman: "malA khAU deU nakos" },
    { en: "You all, don't let me eat", mr: "मला खाऊ देऊ नका", roman: "malA khAU deU nakA" },
    { en: "I like to eat mango", mr: "मला आंबा खायला आवडतो", roman: "malA AMbA khAyalA AvaDato" },
    { en: "I like to eat mangoes", mr: "मला आंबे खायला आवडतात", roman: "malA AMbe khAyalA AvaDatAt" },
    { en: "I do not like to eat mango", mr: "मला आंबा खायला आवडत नाही", roman: "malA AMbA khAyalA AvaDat nAhI" },
    { en: "I do not like to eat mangoes", mr: "मला आंबे खायला आवडत नाहीत", roman: "malA AMbe khAyalA AvaDat nAhIt" },
    { en: "Would you like to drink tea?", mr: "तुम्हाला चहा प्यायला आवडेल का?", roman: "tumhAlA chahA pyAyalA AvaDel kA?" },
    { en: "I want to eat mango", mr: "मला आंबा खायचा आहे", roman: "malA AMbA khAyachA Ahe" },
    { en: "I want to eat mangoes", mr: "मला आंबे खायचे आहेत", roman: "malA AMbe khAyache Ahet" },
    { en: "I do not want to eat mango", mr: "मला आंबा खायचा नाही आहे", roman: "malA AMbA khAyachA nAhI Ahe" },
    { en: "She wants me to avoid junk food", mr: "तिला, मी जंकफूड टाळायला पाहिजे", roman: "tilA, mI jaMkaphUD TALAyalA pAhije" },
    { en: "Peter made Mary eat mango", mr: "पीटरने मेरीला आंबा खायला लावला", roman: "pITarane merIlA AMbA khAyalA lAvalA" },
    { en: "Peter made Mary eat mangoes", mr: "पीटरने मेरीला आंबे खायला लावले", roman: "pITarane merIlA AMbe khAyalA lAvale" },
    { en: "Milk and sugar", mr: "दूध आणि/व साखर", roman: "dUdh ANi/v sAkhar" },
    { en: "Rather than surrendering soldier will accept death", mr: "शरण जाण्याऐवजी सैनिक मरण स्वीकारेल", roman: "sharaN jANyAaivajI sainik maraN svIkArel" },
    { en: "I will take tea rather than coffee", mr: "मी चहाच्या ऐवजी कॉफी घेईन", roman: "mI chahAchyA aivajI coffee gheIn" },
    { en: "Govt said prices declined whereas inflation rose", mr: "सरकारने सांगितले की भाव कमी झाले उलट महागाई वाढली", roman: "sarakArane sAMgitale kI bhAv kamI jhAle ulaT mahAgAI vADhalI" },
    { en: "Repeat like tape", mr: "टेप लावणे", roman: "Tepa lAvaNe" },
    { en: "To defeat completely", mr: "धुव्वा उडवणे", roman: "dhuvvA uDavaNe" },
    { en: "Great grand father", mr: "पणजोबा", roman: "paNajobA" },
    { en: "Great grand mother", mr: "पणजी", roman: "paNajI" },
    { en: "Great grandson", mr: "पणतू", roman: "paNatU" },
    { en: "Great granddaughter", mr: "पणती", roman: "paNatI" },
    { en: "To drink", mr: "पीणे pINe", roman: "chahA pyAyalA" },
    { en: "To have breakfast", mr: "नाश्ता करणे nAshtA karaNe", roman: "nAshtA kelA" },
    { en: "To eat", mr: "खाणे khANe", roman: "poLI bhAjI khAllI" },
    { en: "To have lunch/dinner", mr: "जेवणे jevaNe", roman: "mI jevalo" },
    { en: "Teach", mr: "शिकवणे shikavaNe", roman: "phreMch shikavalI" },
    { en: "To fix price", mr: "भाव लावणे", roman: "bhAv lAvaNe" },
    { en: "To cook rice", mr: "भात लावणे", roman: "bhAt lAvaNe" },
    { en: "To sow wheat", mr: "गहू लावणे", roman: "gahU lAvaNe" },
    { en: "Salty", mr: "खारट", roman: "khAraT" },
    { en: "Giant milkweed", mr: "रूई", roman: "rUI" },
    { en: "Good morning Teacher/Madam", mr: "गुड मॉर्निंग बाई/मॅडम", roman: "guD morniMg bAI/maDam" },
    { en: "Teacher, I did not do", mr: "बाई मी नाही केला", roman: "bAI mI nAhI kelA" },
    { en: "Teacher, when is unit test?", mr: "बाई चाचणी परिक्षा कधी आहे?", roman: "bAI chAchaNI parikShA kadhI Ahe?" },
    { en: "It's running in Alankar theatre", mr: "अलंकार थेटरला लागला आहे.", roman: "alaMkAr theTaralA lAgalA Ahe." },
    { en: "Who is your teacher?", mr: "तुझे शिक्षक कोण आहेत?", roman: "tujhe shikShak koN Ahet?" },
    { en: "Great. Let's go!", mr: "छान. चल निघूया!", roman: "ChAn. chal nighUyA!" },
    { en: "What have you prepared for lunch today?", mr: "आज जेवायला काय केले आहे", roman: "Aj jevAyalA kAy kele Ahe" },
    { en: "What have you prepared for lunch today?", mr: "आज काय स्वयंपाक केला आहे", roman: "Aj kAy svayaMpAk kelA Ahe" },
    { en: "What have you prepared for breakfast today?", mr: "आज नाष्त्याला काय केले आहे", roman: "Aj nAShtyAlA kAy kele Ahe" },
    { en: "Strain the tea", mr: "चहा गाळ", roman: "chahA gAL" },
    { en: "Cut down on sugar", mr: "कमी साखर खा", roman: "kamI sAkhar khA" },
    { en: "The tea is on the stove", mr: "चहा गॅसवर आहे", roman: "chahA g~asavar Ahe" },
    { en: "Instead I work at home on the computer", mr: "त्याऐवजी मी घरी computerवर काम करते", roman: "tyAaivajI mI gharI computer var kAm karate" },
    { en: "Sometimes I make breakfast for Rohan", mr: "कधीकधी मी रोहनसाठी नाश्ता बनवते", roman: "kadhIkadhI mI rohanasAThI nAshtA banavate" },
    { en: "I would like to teach English", mr: "मला इंग्रजी शिकवायला आवडेल", roman: "malA iMgrajI shikavAyalA AvaDel" },
    { en: "Do it fast. It will be a great favour on me", mr: "लवकर कर. माझ्यावर उपकार कर", roman: "lavakar kar. mAjhyAvar upakAr kar" },
    { en: "Mango leaves", mr: "आंब्याची पाने", roman: "AMbyAchI pAne" },
    { en: "To offer food to god", mr: "नैवेद्य दाखवणे", roman: "naivedya dAkhavaNe" },
    { en: "Can you give me water? (to boy)", mr: "मला थोडे पाणी देतोस का?", roman: "malA thoDe pANI detos kA?" },
    { en: "Can you give me water? (to man/lady)", mr: "मला थोडे पाणी देता का?", roman: "malA thoDe pANI detA kA?" },
    { en: "What would you like? Tea or Coffee?", mr: "तुम्ही काय घेणार? चहा की कॉफी?", roman: "tumhI kAy gheNAr? chahA kI k~ophI?" },
    { en: "I will take tea", mr: "मी चहा घेईन", roman: "mI chahA gheIn" },
    { en: "Tea is fine for me", mr: "मला चहा चालेल", roman: "malA chahA chAlel" },
    { en: "Yes. Have a seat", mr: "हो, बसा", roman: "ho, basA" },
    { en: "Jackfruit", mr: "फणस", roman: "phaNas" },
    { en: "Mango Raw", mr: "कैरी", roman: "kairI" },
    { en: "Watermelon", mr: "टरबूज / कलिंगड", roman: "TarabUj / kaliMgaD" },
    { en: "10 minutes passed, food not served", mr: "दहा मिनिटे झाली. जेवण अजून आले नाही", roman: "dahA miniTe jhAlI. jevaN ajUn Ale nAhI" },
    { en: "It is rainy weather today", mr: "आज पावसाळी वातावरण आहे", roman: "Aj pAvasALI vAtAvaraN Ahe" },
    { en: "We are going to eat lunch. You too come", mr: "आता आम्ही जेवायला बसतो आहोत. तू सुद्धा ये.", roman: "AtA AmhI jevAyalA basato Ahot. tU suddhA ye." },
    { en: "What do you love to eat?", mr: "तुला खायला काय काय आवडते?", roman: "tulA khAyalA kAy kAy AvaDate?" },
    { en: "What's the time of dinner at your home?", mr: "तुझ्या घरी रात्री कधी जेवता?", roman: "tujhyA gharI rAtrI kadhI jevatA?" },
    { en: "Dinner time is not fixed. Mostly 9 or 10 pm", mr: "जेवायची वेळ नक्की नाही. बहुतेक वेळा आठ किंवा नऊ वाजता जेवतो.", roman: "jevAyachI veL nakkI nAhI. bahutek veLA ATh kiMvA naU vAjatA jevato." },
    { en: "What did you eat?", mr: "तू काय खाल्लेस?", roman: "tU kAy khAlles?" },
    { en: "How important is food in your family?", mr: "तुझ्या कुटुंबाच्या जीवनात जेवण तयार करणे किती महत्वाचे आहे?", roman: "tujhyA kuTuMbAchyAjIvanAt jevaN tayAr karaNe kitI mahatvAche Ahe?" },
    { en: "On Monday we ate North Indian food", mr: "सोमवारी आम्ही उत्तर भारतीय भोजन खाल्ले.", roman: "somavArI AmhI uttar bhAratIy bhojan khAlle." },
    { en: "Take deep breath", mr: "मोठा श्वास घ्या.", roman: "moThA shwAs ghyA." },
    { en: "May be because of changing weather", mr: "हवा बदलत्ये त्यामुळे असावा.", roman: "havA badalatye tyAmuLe asAvA." },
    { en: "Before lunch or after?", mr: "जेवणाआधी का नंतर?", roman: "jevaNAAdhI kA naMtar?" },
    { en: "Do not take cold water, curd, buttermilk", mr: "गार पाणी, गार दही, ताक पिऊ नका.", roman: "gAr pANI, gAr dahI, tAk piU nakA." },
    { en: "Drink boiled water", mr: "पाणी उकळून प्या.", roman: "pANI ukaLUn pyA." },
    { en: "Give me 1kg Sugar", mr: "एक किलो साखर द्या", roman: "ek kilo sAkhar dyA" }
  ]
  },
  health: {
    name: "Health & Body",
    words: [
    { en: "Nobody is looking. Just do it", mr: "कोणी आपल्याकडे बघत नाहिये. करून टाक लवकर", roman: "koNI ApalyAkaDe baghat nAhiye. karUn TAk lavakar" },
    { en: "Mummy! It is paining", mr: "अगं आई! खूप दुखतंय", roman: "agaM AI! khUp dukhataMy" },
    { en: "I did not come yesterday, because I was sick", mr: "मी काल आलो नाही, कारण मी आजारी होतो", roman: "mI kAl Alo nAhI, kAraN mI AjArI hoto" },
    { en: "I was sick so I did not come", mr: "मी आजारी होतो म्हणून मी काल आलो नाही", roman: "mI AjArI hoto mhaNUn mI kAl Alo nAhI" },
    { en: "Cough", mr: "खोकणे khokaNe", roman: "khokalo" },
    { en: "We went to Khadki railway station for wall painting activity", mr: "आम्ही काल खडकी रेल्वे स्टेशनला गेलो", roman: "AmhI kAl khaDakI relve sTeshanalA gelo" },
    { en: "We painted 2 drawings", mr: "आम्ही दोन चित्रं रंगवली", roman: "AmhI don chitrM raMgavalI" },
    { en: "You are somebody who changed my life", mr: "तू अशी व्यक्ती आहेस जिने माझं आयुष्य बदलून टाकलं", roman: "tU ashI vyaktI Ahes jine mAjhM AyuShy badalUn TAkalM" },
    { en: "How is everybody at home?", mr: "घरी सगळे कसे आहेत?", roman: "gharI sagaLe kase Ahet?" },
    { en: "Body", mr: "शरीर", roman: "sharIr" }
  ]
  },
  schoolWork: {
    name: "School & Work",
    words: [
    { en: "School", mr: "शाळा", roman: "Śāḷā" },
    { en: "Work", mr: "काम", roman: "Kām" },
    { en: "I want you to finish work", mr: "मला, तू काम संपवायला पाहिजेस", roman: "malA, tU kAm saMpavAyalA pAhijes" },
    { en: "He made me work", mr: "त्याने मला काम करायला लावले", roman: "tyAne malA kAm karAyalA lAvale" },
    { en: "He makes me work", mr: "तो मला काम करायला लावतो", roman: "to malA kAm karAyalA lAvato" },
    { en: "He will make me work", mr: "तो मला काम करायला लावेल", roman: "to malA kAm karAyalA lAvel" },
    { en: "He was clever but did not work hard", mr: "तो हुशार होता पण त्याने परिश्रम केले नाहीत", roman: "to hushAr hotA paN tyAne parishram kele nAhIt" },
    { en: "I finished study then I went to play", mr: "मी अभ्यास संपवला त्यानंतर खेळायला गेलो", roman: "mI abhyAs saMpavalA tyAnaMtar kheLAyalA gelo" },
    { en: "I will work hard so that I will win", mr: "मी परिश्रम करीन जेणेकरून मी यशस्वी होईन", roman: "mI parishram karIn jeNekarUn mI yashasvI hoIn" },
    { en: "To work", mr: "काम करणे kAm karaNe", roman: "kAm kele" },
    { en: "Study", mr: "अभ्यास करणे abhyAs karaNe", roman: "gaNitAchA abhyAs kelA" },
    { en: "Admit (school)", mr: "भरती करणे bharatI karaNe", roman: "mulAlA shALet bharatI kele" },
    { en: "How much work-pressure?", mr: "Work-pressure कसं आहे", roman: "work-pressure kasaM Ahe" },
    { en: "What kind of work do you do currently?", mr: "सध्या कामाचं स्वरूप काय आहे?", roman: "sadhyA kAmAchaM svarUp kAy Ahe?" },
    { en: "I am senior software developer", mr: "मी सिनिअर सोफ्टवेअर डेव्हलपर आहे.", roman: "mI siniar sophTavear Devhalapar Ahe." },
    { en: "Elder brother is in bank. Other siblings are studying", mr: "मोठा भाऊ बॅंकेत आहे. बाकीची भावंडे शिकत आहेत.", roman: "moThA bhAU b~aMket Ahe. bAkIchI bhAvaMDe shikat Ahet." },
    { en: "Will you do work at our place?", mr: "आमच्याकडचं काम कराल का?", roman: "AmachyAkaDachM kAm karAl kA?" },
    { en: "What all is work?", mr: "काय काय काम आहे?", roman: "kAy kAy kAm Ahe?" },
    { en: "I need net banking facility", mr: "मला माझ्या खात्यासाठी नेट बॅंकिगची सुविधा हवी आहे.", roman: "malA mAjhyA khAtyAsAThI neT b~aMkigachI suvidhA havI Ahe." },
    { en: "Can voter-id work?", mr: "वोटर कार्ड चालेल का?", roman: "voTar kArD chAlel kA?" },
    { en: "Is mobile working?", mr: "मोबाईल चालू आहे का?", roman: "mobAIl chAlU Ahe kA?" },
    { en: "Yes, mobile is working", mr: "हो, मोबाईल चालू/सुरू आहे", roman: "ho, mobAIl chAlU/surU Ahe" },
    { en: "Was watch working?", mr: "घड्याळ चालू/सुरू होते का?", roman: "ghaDyAL chAlU/surU hote kA?" },
    { en: "Is mobile not working?", mr: "मोबाईल बंद आहे का?", roman: "mobAIl baMd Ahe kA?" },
    { en: "Yes, mobile is not working", mr: "मोबाईल बंद आहे", roman: "mobAIl baMd Ahe" },
    { en: "I really like studying languages", mr: "मला भाषा शिकायला खूप आवडते", roman: "malA bhAShA shikAyalA khUp AvaDate" },
    { en: "I do all the work. But you do not value me", mr: "सगळी कामं मी करतो पण तुला माझी किंमतच नाहीये", roman: "sagaLI kAmM mI karato paN tulA mAjhI kiMmatach nAhIye" },
    { en: "We work from 10 am to 10 pm", mr: "आम्ही सकाळी 10 ते रात्री 10 काम करतो", roman: "AmhI sakALI 10 te rAtrI 10 kAm karato" },
    { en: "Where do you work? (to boy)", mr: "तू कुठे काम करतोस", roman: "tU kuThe kAm karatos" }
  ]
  },
  socialInteractions: {
    name: "Social & People",
    words: [
    { en: "Mother", mr: "आई", roman: "Āī" },
    { en: "Father", mr: "बाबा", roman: "Bābā" },
    { en: "Brother", mr: "भाऊ", roman: "Bhāū" },
    { en: "Sister", mr: "ताई", roman: "Tāī" },
    { en: "Friend", mr: "मित्र", roman: "Mitra" },
    { en: "My friends and I used to play cricket", mr: "माझे मित्र आणि मी क्रिकेट खेळत असू", roman: "mAjhe mitr ANi mI krikeT kheLat asU" },
    { en: "She missed her mother a lot", mr: "तीला तीच्या आईची खूप आठवण आली", roman: "tIlA tIchyA AIchI khUp AThavaN AlI" },
    { en: "I have 2 brothers", mr: "मला दोन भाऊ आहेत", roman: "malA don bhAU Ahet" },
    { en: "He does not have a brother", mr: "त्याला भाऊ नाही", roman: "tyAlA bhAU nAhI" },
    { en: "My wife was standing there. He asked about girlfriend", mr: "माझी बायको तिथे उभी होती. त्याने माझ्या मैत्रिणीबद्दल विचारले", roman: "mAjhI bAyako tithe ubhI hotI. tyAne mAjhyA maitriNIbaddal vichArale" },
    { en: "Father", mr: "वडील / बाबा", roman: "vaDIl / bAbA" },
    { en: "Elder brother", mr: "मोठा भाऊ / दादा", roman: "moThA bhAU / dAdA" },
    { en: "Sister", mr: "बहीण", roman: "bahIN" },
    { en: "Elder sister", mr: "मोठी बहीण / ताई", roman: "moThI bahIN / tAI" },
    { en: "Direct brother", mr: "सख्खा भाऊ", roman: "sakhkhA bhAU" },
    { en: "Direct sister", mr: "सख्खी बहीण", roman: "sakhkhI bahIN" },
    { en: "Grand father", mr: "आजोबा", roman: "AjobA" },
    { en: "Grand mother", mr: "आजी", roman: "AjI" },
    { en: "Father's brother", mr: "काका", roman: "kAkA" },
    { en: "Father's brother's wife", mr: "काकू", roman: "kAkU" },
    { en: "Father's brother's son", mr: "चुलत भाऊ", roman: "chulat bhAU" },
    { en: "Father's brother's daughter", mr: "चुलत बहीण", roman: "chulat bahIN" },
    { en: "Mother's brother", mr: "मामा", roman: "mAmA" },
    { en: "Mother's brother's wife", mr: "मामी", roman: "mAmI" },
    { en: "Mother's brother's son", mr: "मामे भाऊ", roman: "mAme bhAU" },
    { en: "Mother's brother's daughter", mr: "मामे बहीण", roman: "mAme bahIN" },
    { en: "Father's sister", mr: "आत्या", roman: "AtyA" },
    { en: "Father's sister's son", mr: "आत्ते भाऊ", roman: "Atte bhAU" },
    { en: "Father's sister's daughter", mr: "आत्ते बहीण", roman: "Atte bahIN" },
    { en: "Mother's sister", mr: "मावशी", roman: "mAvashI" },
    { en: "Mother's sister's son", mr: "मावस भाऊ", roman: "mAvas bhAU" },
    { en: "Mother's sister's daughter", mr: "मावस बहीण", roman: "mAvas bahIN" },
    { en: "Mother's sister's husband", mr: "काका / मावसा", roman: "kAkA / mAvasA" },
    { en: "Father in law", mr: "सासरे", roman: "sAsare" },
    { en: "Mother in law", mr: "सासू / सासुबाई", roman: "sAsU / sAsubAI" },
    { en: "Father in law's father", mr: "आजेसासरे", roman: "AjesAsare" },
    { en: "Father in law's mother", mr: "आजेसासू / आजेसासुबाई", roman: "AjesAsU / AjesAsubAI" },
    { en: "Husband's brother", mr: "दीर", roman: "dIr" },
    { en: "Husband's brother's wife", mr: "जाऊ", roman: "jAU" },
    { en: "Husband's sister", mr: "नणंद", roman: "naNMd" },
    { en: "Wife's brother", mr: "मेहुणा", roman: "mehuNA" },
    { en: "Wife's sister", mr: "मेहुणी", roman: "mehuNI" },
    { en: "Wife's sisters' husband", mr: "साडू", roman: "sADU" },
    { en: "Sister's son", mr: "भाचा", roman: "bhAchA" },
    { en: "Sister's daughter", mr: "भाची", roman: "bhAchI" },
    { en: "Elder Brother's wife", mr: "वहिनी", roman: "vahinI" },
    { en: "Younger brother's wife", mr: "भावजय", roman: "bhAvajay" },
    { en: "A man's brother's son", mr: "पुतण्या", roman: "putaNyA" },
    { en: "A man's brother's daughter", mr: "पुतणी", roman: "putaNI" },
    { en: "Friend (girl)", mr: "मैत्रीण", roman: "maitrIN" },
    { en: "But my family members do not like it", mr: "पण माझ्या घरच्यांना हे पसंत नाही.", roman: "paN mAjhyA gharachyAMnA he pasaMt nAhI." },
    { en: "I will marry only if my parents allow", mr: "माझ्या आई वडीलांनी परवानगी दिली तरच मी लग्न करीन", roman: "mAjhyA AI vaDIlAMnI paravAnagI dilI tarach mI lagn karIn" },
    { en: "I will convince your parents", mr: "मी तुझ्या आई वडिलांना समजावेन.", roman: "mI tujhyA AI vaDilAMnA samajAven." },
    { en: "You can make friends by using social media", mr: "आपण सोशल मीडिया वापरून मित्र बनवू शकतो", roman: "ApaN soshal mIDiyA vAparUn mitr banavU shakato" },
    { en: "Actually I made friends online recently", mr: "खरं तर माझे नुकतेच काही नवीन मित्र बनले आहेत", roman: "kharM tar mAjhe nukatech kAhI navIn mitr banale Ahet" },
    { en: "Hey friend", mr: "अरे मित्रा", roman: "are mitrA" },
    { en: "Hey brother", mr: "अरे दादा", roman: "are dAdA" },
    { en: "Hey Sister (formal)", mr: "अहो ताई", roman: "aho tAI" },
    { en: "Hey Sister (known elder)", mr: "अगं ताई", roman: "agaM tAI" },
    { en: "My family is multicultural", mr: "माझं कुटुंब बहुसांस्कृतिक कुटुंब आहे.", roman: "mAjhM kuTuMb bahusAMskRutik kuTuMb Ahe." }
  ]
  },
  time: {
    name: "Time & Dates",
    words: [
    { en: "Time", mr: "वेळ", roman: "Veḷ" },
    { en: "Day", mr: "दिवस", roman: "Divas" },
    { en: "Night", mr: "रात्र", roman: "Rātra" },
    { en: "Morning", mr: "सकाळ", roman: "Sakāḷ" },
    { en: "Evening", mr: "संध्याकाळ", roman: "Sandhyākāḷ" },
    { en: "Today", mr: "आज", roman: "Āj" },
    { en: "Tomorrow", mr: "उद्या", roman: "Udyā" },
    { en: "Yesterday", mr: "काल", roman: "Kāl" },
    { en: "Court asked to be present tomorrow", mr: "न्यायालयाने उद्या हजर राहण्यास सांगितले", roman: "nyAyAlayAne udyA hajar rAhaNyAs sAMgitale" },
    { en: "He has to do it every day", mr: "त्याला हे रोज करायला/करावे लागते", roman: "tyAlA he roj karAyalA/karAve lAgate" },
    { en: "He will have to do it every day", mr: "त्याला हे रोज करायला/करावे लागेल", roman: "tyAlA he roj karAyalA/karAve lAgel" },
    { en: "He had to do it every day", mr: "त्याला हे रोज करायला/करावे लागले", roman: "tyAlA he roj karAyalA/karAve lAgale" },
    { en: "I am supposed to go there tomorrow", mr: "मी उद्या तिकडे जायचे आहे", roman: "mI udyA tikaDe jAyache Ahe" },
    { en: "He is supposed to come tomorrow", mr: "त्याने उद्या यायचे आहे / यायचं", roman: "tyAne udyA yAyache Ahe / yAyachM" },
    { en: "You must pay me ransom tomorrow itself", mr: "तू मला उद्याच्या उद्या खंडणी द्यायची", roman: "tU malA udyAchyA udyA khMDaNI dyAyachI" },
    { en: "Finish it off in 10 minutes", mr: "दहा मिनिटात संपवून टाक आणि जा झोपायला", roman: "dahA miniTAt saMpavUn TAk ANi jA jhopAyalA" },
    { en: "I made her take exercise every day", mr: "मी तीच्याकडून रोज व्यायाम करून घेतला", roman: "mI tIchyAkaDUn roj vyAyAm karUn ghetalA" },
    { en: "If you had taken exercise every day then", mr: "जर तू रोज व्यायाम करत गेला असतास तर", roman: "jar tU roj vyAyAm karat gelA asatAs tar" },
    { en: "I have decided plan for tonight", mr: "मी आजचा प्लॅन करून चुकलो आहे", roman: "mI AjachA pl~an karUn chukalo Ahe" },
    { en: "They might have returned yesterday", mr: "बहुतेक ते काल परत गेले असतील", roman: "bahutek te kAla parat gele asatIl" },
    { en: "The day I like", mr: "माझा आवडता दिवस", roman: "mAjhA AvaDatA divas" },
    { en: "I will come tomorrow itself", mr: "मी उद्याच येईन", roman: "mI udyAch yeIn" },
    { en: "He will come tomorrow as well", mr: "तो उद्यासुद्धा / उद्याही येईल", roman: "to udyAsuddhA / udyAhI yeIl" },
    { en: "I want it tomorrow itself", mr: "मला हे उद्याच हवे आहे", roman: "malA he udyAch have Ahe" },
    { en: "To take time", mr: "वेळ लावणे", roman: "veL lAvaNe" },
    { en: "Night cestrum", mr: "रातराणी", roman: "rAtarANI" },
    { en: "Yes. I left it 2 months back", mr: "हो. दोन महिन्यांपूर्वी मी ती कंपनी सोडली", roman: "ho. don mahinyAMpUrvI mI tI kaMpanI soDalI" },
    { en: "How much time it takes?", mr: "किती वेळ लागतो?", roman: "kitI veL lAgato?" },
    { en: "1 hour", mr: "एक तास", roman: "ek tAs" },
    { en: "Good morning pupils", mr: "गुड मॉर्निंग मुलांनो", roman: "guD morniMg mulAMno" },
    { en: "Did you do homework given yesterday?", mr: "काल दिलेला गृहपाठ केला का?", roman: "kAl dilelA gRuhapATh kelA kA?" },
    { en: "Next month", mr: "पुढच्या महिन्यात.", roman: "puDhachyA mahinyAt." },
    { en: "Raju, Is it time to tell joke?", mr: "राजू, ही जोक संगायची वेळ आहे?", roman: "rAjU, hI jok saMgAyachI veL Ahe?" },
    { en: "He will come in evening", mr: "संध्याकाळी येतील", roman: "saMdhyAkALI yetIl" },
    { en: "Ok then. See you tomorrow", mr: "ठीक आहे भेटू उद्या", roman: "ThIk Ahe bheTU udyA" },
    { en: "I will take 4 holidays every month", mr: "महिन्यातून ४ सुट्ट्या घेत जाईन.", roman: "mahinyAtUn 4 suTTyA ghet jAIn." },
    { en: "Start the work from today itself", mr: "आजपासूनच सुरुवात करा कामाला.", roman: "AjapAsUnach suruvAt karA kAmAlA." },
    { en: "How is the day celebrated?", mr: "हा दिवस कसा साजरा केला जातो?", roman: "hA divas kasA sAjarA kelA jAto?" },
    { en: "Flag hoisting and salute in morning", mr: "सकाळच्या वेळी ध्वज फडकवून, झेंडावंदन करून समारंभ सुरू केला जातो.", roman: "sakALachyA veLI dhvaj phaDakavUn, jheMDAvMdan karUn samArMbh surU kelA jAto." },
    { en: "Happy Republic day", mr: "हो, प्रजासत्ताक दिनाच्या शुभेच्छा", roman: "ho, prajAsattAk dinAchyA shubhechChA." },
    { en: "I had applied for ATM card 1 month back. Not received yet", mr: "मी एक महिन्यापूर्वी एटीएम कार्डासाठी अर्ज केला होता पण अजून मिळाले नाही.", roman: "mI eka mahinyApUrvI eTIem kArDAsAThI arj kelA hotA paN ajUn miLAle nAhI." },
    { en: "Cheque takes approximately 2 weeks", mr: "चेक येण्यासाठी अंदाजे दोन आठवडे लागतात.", roman: "chek yeNyAsAThI aMdAje don AThavaDe lAgatAt." },
    { en: "Morning 7 to 11 and Evening 4 to 8", mr: "सकाळी सात ते अकरा आणि संध्याकाळी चार ते आठ", roman: "sakALI sAt te akarA ANi saMdhyAkALI chAr te ATh" },
    { en: "There was your football match yesterday, wasn't it?", mr: "तुझी आज फुटबॉलची मॅच होती ना", roman: "tujhI Aj football m~ach hotI nA?" },
    { en: "Hey buddy, let's go to watch movie today", mr: "मित्रा, चल आज आपण सिनेमा बघायला जाऊया.", roman: "mitrA, chal Aj ApaN sinemA baghAyalA jAUyA." },
    { en: "Have you seen yesterday's match? Germany vs Korea", mr: "तू कालची मॅच बघितलीस का? जर्मनी आणि कोरियाची.", roman: "tU kAlachI m~ach baghitalIs kA? jarmanI ANi koriyAchI." },
    { en: "My class is 5 minutes from railway station", mr: "माझा क्लास रेल्वे स्टेशन पासून पाच मिनिटांवर आहे.", roman: "maajhA klAs relve sTeshan pAsUn pAch miniTAMvar aahe." },
    { en: "Is it every day?", mr: "तो रोज असतो का?", roman: "to roj asato kA?" },
    { en: "No. On alternate days. 5 to 6 in evening", mr: "नाही. एकाडएक दिवस असतो. संध्याकाळी पाच ते सहा.", roman: "nAhI. ekADaek divas asato. saMdhyAkALI pAch te sahA." },
    { en: "500 Rs. Per month", mr: "प्रत्येक महिन्याचे पाचशे रुपये.", roman: "pratyek mahinyAche pAchashe rupaye." },
    { en: "I did not have time", mr: "माझ्याकडे/मला वेळ नव्हता", roman: "mAjhyAkaDe/malA veL navhatA" },
    { en: "I do not have time", mr: "माझ्याकडे/मला वेळ नाही", roman: "mAjhyAkaDe/malA veL nAhI" },
    { en: "How many days have you taken leave?", mr: "तू किती दिवस सुट्टी घेतली आहेस?", roman: "tU kitI divas suTTI ghetalI Ahes?" },
    { en: "I have taken leave for 7 days", mr: "मी सात दिवस सुट्टी घेतली आहे", roman: "mI sAt divas suTTI ghetalI Ahe" },
    { en: "How much time does it take to reach hometown?", mr: "गावाला पोचायला किती वेळ लागतो?", roman: "gAvAlA pochAyalA kitI veL lAgato?" },
    { en: "There was a party in our office today", mr: "आज आमच्या ऑफिस मध्ये पार्टी झाली", roman: "Aj AmachyA office madhye pArTI jhAlI" },
    { en: "When is the class in next week?", mr: "पुढच्या आठवड्यात क्लास कधी आहे?", roman: "puDhachyA AThavaDyAt klAs kadhI Ahe?" },
    { en: "I don't go to work these days", mr: "आजकाल मी कामाला जात नाही", roman: "AjakAl mI kAmAlA jAt nAhI" },
    { en: "I use social media everyday", mr: "मी सोशल मीडिया दररोज वापरते", roman: "mI soshal mIDiyA dararoj vAparate" },
    { en: "I am going to watch the solar eclipse", mr: "मी सूर्यग्रहण बघायला जातो आहे", roman: "mI sUryagrahaN baghAyalA jAto Ahe" },
    { en: "Do you have special goggle to watch the eclipse?", mr: "तुझ्याकडे ग्रहण बघायचा खास चष्मा आहे का?", roman: "tujhyAkaDe grahaN baghAyachA khAs chaShmA Ahe kA" },
    { en: "That is called eclipse", mr: "त्याला ग्रहण म्हणतात", roman: "tyAlA grahaN mhaNatAt" },
    { en: "But I was shooting that time", mr: "पण त्यावेळी मी शूट करत होते", roman: "paN tyAveLI mI shUT karat hote" },
    { en: "Now after 2-3 months I will get call for what I was calling for", mr: "आता अजून काहीतरी दोन तीन महिन्यांनंतर ज्या आज गोष्टीसाठी मी कॉल करत होतो ते कॉल येतील मला", roman: "AtA ajUn kAhItarI don tIn mahinyAMnMtar jyA Aj goShTIsAThI mI k~ol karat hoto te k~ol yetIl malA" },
    { en: "Did you do the task I told you yesterday?", mr: "काल सांगितलेलं काम केलंस का?", roman: "kAl sAMgitalelM kAm kelMs kA" },
    { en: "Day after tomorrow", mr: "परवा", roman: "paravA" },
    { en: "at Morning", mr: "सकाळी", roman: "sakALI" },
    { en: "at evening", mr: "संध्याकाळी", roman: "saMdhyAkALI" },
    { en: "Nowadays", mr: "हल्ली / सध्या", roman: "hallI / sadhyA" },
    { en: "Everyday", mr: "रोज / दररोज", roman: "roj / dararoj" },
    { en: "at Day", mr: "दिवसा", roman: "divasA" },
    { en: "at night", mr: "रात्री", roman: "rAtrI" },
    { en: "Week", mr: "आठवडा", roman: "AThavaDA" },
    { en: "Month", mr: "महिना", roman: "mahinA" },
    { en: "We play cricket every day", mr: "आम्ही रोज क्रिकेट खेळतो", roman: "AmhI roj krikeT kheLato" },
    { en: "He comes back from school in the evening", mr: "तो संध्याकाळी शाळेतून परत येतो", roman: "to saMdhyAkALI shALetUn parat yeto" },
    { en: "Monday", mr: "सोमवार", roman: "somavAr" },
    { en: "Tuesday", mr: "मंगळवार", roman: "maMgaLavAr" },
    { en: "Wednesday", mr: "बुधवार", roman: "budhavAr" },
    { en: "Thursday", mr: "गुरुवार", roman: "guruvAr" },
    { en: "Friday", mr: "शुक्रवार", roman: "shukravAr" },
    { en: "Saturday", mr: "शनिवार", roman: "shanivAr" },
    { en: "What date is it today?", mr: "आज काय तारीख आहे?", roman: "Aj kAy tArIkh Ahe?" },
    { en: "It was 1st July yesterday", mr: "काल १ जुलै होती", roman: "kAl 1 julai hotI" },
    { en: "It is 2nd July today", mr: "आज दोन जुलै आहे", roman: "Aj don julai Ahe" },
    { en: "Celebrating women's day started on 28th Feb 1909", mr: "महिला दिन साजरा करण्याची सुरुवात 28 फेब्रुवारी 1909 साली झाली होती", roman: "mahilA din sAjarA karaNyAchI suruvAt 28 phebruvArI 1909 sAlI jhAlI hotI" },
    { en: "8th March was declared as International Women's day", mr: "आणि त्या सुचनेनुसार 8 मार्च हा दिवस जागतिक महिला दिन म्हणून घोषित करण्यात आला", roman: "ANi tyA suchanenusAr 8 mArch hA divas jAgatik mahilA din mhaNUn ghoShit karaNyAt AlA" },
    { en: "Happy Birthday", mr: "वाढदिवसाच्या हार्दिक शुभेच्छा", roman: "vADhadivasAchyA hArdik shubhechChA" },
    { en: "Good morning/evening/night", mr: "नमस्कार / नमस्ते (or English)", roman: "namaskAr / namaste" },
    { en: "Long-time no see (to boy)", mr: "खूप दिवसात भेटला नाहीस", roman: "khUp divasAt bheTalA nAhIs" },
    { en: "Long-time no see (to girl)", mr: "खूप दिवसात भेटली नाहीस", roman: "khUp divasAt bheTalI nAhIs" },
    { en: "For next 4 days I will accompany you", mr: "पुढचे चार दिवस मी तुमच्या बरोबर असेन आणि सिंगापूर बघण्यासाठी तुम्हाला मार्गदर्शन करेन.", roman: "puDhache chAr divas mI tumachyA barobar asen ANi siMgApUr baghaNyAsAThI tumhAlA mArgadarshan karen." },
    { en: "Today we visit Universal Studios", mr: "आज आपण Universal Studios ला भेट देणार आहोत.", roman: "Aj ApaN Universal Studios lA bheT deNAr Ahot." },
    { en: "We will reach there in 40 minutes", mr: "इथून चाळीस मिनिटांत आपण तिथे पोचू.", roman: "ithUn chALIs miniTAMt ApaN tithe pochU." },
    { en: "See you tomorrow", mr: "उद्या भेटूया.", roman: "udyA bheTUyA." },
    { en: "Good night", mr: "शुभरात्री.", roman: "shubharAtrI." },
    { en: "Finish work at least by tomorrow", mr: "उद्यापर्यंत तरी काम संपव", roman: "udyAparyMt tarI kAm saMpav" },
    { en: "Every time", mr: "प्रत्येक वेळी", roman: "pratyek veLI" },
    { en: "Is the process chargeable? How many days?", mr: "काही चार्ज लागतो का? आणि सगळ्या गोष्टी सत्यापित करण्यासाठी किती दिवस लागतील?", roman: "kahi charj lagato ka? ani sagalya goshti satyapit karanyasathi kiti divas lagatil?" },
    { en: "How much time for order?", mr: "ऑर्डर यायला किती वेळ लागेल?", roman: "~orDar yAyalA kitI veL lAgel?" },
    { en: "It will take 10 minutes", mr: "१० मिनिटे लागतील", roman: "10 miniTe lAgatIl" },
    { en: "Yesterday was cool", mr: "काल थंडी होती", roman: "kAl thaMDI hotI" },
    { en: "You came after so many days", mr: "तू खूप दिवसानंतर आला आहेस.", roman: "tU khUp divasAnMtar AlA Ahes." },
    { en: "I went to my friend's house today", mr: "मी आज माझ्या मित्राच्या घरी गेले.", roman: "mI mAjhyA mitrAchyA gharI gele" },
    { en: "From yesterday morning", mr: "काल सकाळ पासून", roman: "kAl sakAL pAsUn" },
    { en: "I give you pills for 2 days. Take them", mr: "मी दोन दिवसांच्या गोळ्या देतो त्या घ्या.", roman: "mI don divasAMchyA goLyA deto tyA ghyA." },
    { en: "Do you have Good day biscuit?", mr: "\"गुड डे\" बिस्किट आहे का?", roman: "guD De biskiT Ahe kA?" },
    { en: "I am not trying to be better than others but better than what I was yesterday", mr: "माझा प्रयत्न इतरांपेक्षा श्रेष्ठ होणे नसून मी जो काल होतो त्यापेक्षा आज चांगला होण्याचा आहे", roman: "mAjhA prayatn itarAMpekShA shreShTh hoNe nasUn mI jo kAl hoto tyApekShA Aj chAMgalA hoNyAchA Ahe" }
  ]
  },
  transportation: {
    name: "Transportation",
    words: [
    { en: "Road", mr: "रस्ता", roman: "Rastā" },
    { en: "Do not cross road here", mr: "येथे रस्ता ओलाण्डू नये", roman: "yethe rastA olANDU naye" },
    { en: "We would go, but we are too busy", mr: "आपण गेलो असतो, पण आपण खूप व्यग्र आहोत", roman: "ApaN gelo asato, paN ApaN khUp vyagr Ahot" },
    { en: "He kept on staring that car", mr: "तो ती गाडी बघतच राहिला", roman: "to tI gADI baghatach rAhilA" },
    { en: "I want only sedan car", mr: "मला सिडान कारच पाहिजे", roman: "malA siDAn kArach pAhije" },
    { en: "I have a car", mr: "माझ्या जवळ/कडे गाडी आहे", roman: "mAjhyA javaL/kaDe gADI Ahe" },
    { en: "I have 10 cars", mr: "माझ्या जवळ/कडे १० गाड्या आहेत", roman: "mAjhyA javaL/kaDe 10 gADyA Ahet" },
    { en: "I had a car", mr: "माझ्या जवळ/कडे गाडी होती", roman: "mAjhyA javaL/kaDe gADI hotI" },
    { en: "I do not have car", mr: "माझ्या जवळ/कडे गाडी नाही", roman: "mAjhyA javaL/kaDe gADI nAhI" },
    { en: "I did not have car", mr: "माझ्या जवळ/कडे गाडी नव्हती", roman: "mAjhyA javaL/kaDe gADI navhatI" },
    { en: "Car will not start because no petrol", mr: "गाडी चालू होणार नाही, कारण टाकीत पेट्रोल नाही", roman: "gADI chAlU hoNAr nAhI, kAraN TAkIt peTrol nAhI" },
    { en: "No petrol so car will not start", mr: "टाकीत पेट्रोल नाही म्हणून गाडी चालू होणार नाही", roman: "TAkIt peTrol nAhI mhaNUn gADI chAlU hoNAr nAhI" },
    { en: "To park car", mr: "गाडी लावणे", roman: "gADI lAvaNe" },
    { en: "My car needs a lot of petrol", mr: "माझ्या गाडीला खूप पेट्रोल लागते", roman: "mAjhyA gADIlA khUp peTrol lAgate" },
    { en: "I got hurt by car", mr: "मला गाडी लागली", roman: "malA gADI lAgalI" },
    { en: "To feel nausea in bus", mr: "गाडी लागणे", roman: "gADI lAgaNe" },
    { en: "She feels nausea in bus", mr: "तीला गाडी लागते", roman: "tIlA gADI lAgate" },
    { en: "Carefully", mr: "काळजीपूर्वक", roman: "kALajIpUrvak" },
    { en: "I am on road", mr: "मी रस्त्यात आहे", roman: "mI rastyAt Ahe" },
    { en: "By company bus", mr: "companyच्या बस ने", roman: "company chyA bas ne" },
    { en: "When is the next bus?", mr: "पुढची बस कधी आहे?", roman: "puDhachI bas kadhI Ahe?" },
    { en: "Uncle, do you know when is the next bus?", mr: "काका, तुम्हाला माहिती आहे का; पुढची बस कधी आहे ते?", roman: "kAkA, tumhAlA mAhitI Ahe kA? puDhachI bas kadhI Ahe te?" },
    { en: "Will I get bus for phase-3 directly?", mr: "डायरेक्ट फेज-३ पर्यंत मिळेल का?", roman: "DAyarekT phej-3 paryaMt miLel kA?" },
    { en: "What is your favorite car?", mr: "तुझी आवडती गाडी कुठली", roman: "tujhI AvaDatI gADI kuThalI" },
    { en: "I go by bus", mr: "मी बसने जातो", roman: "mI basane jAto" },
    { en: "I have a car", mr: "माझ्याकडे गाडी आहे", roman: "mAjhyAkaDe gADI Ahe" },
    { en: "I was stuck in the traffic", mr: "मी ट्रॅफिकमध्ये अडकलो होतो", roman: "mI Tr~aphikamadhye aDakalo hoto" },
    { en: "Get on the bus", mr: "बसमध्ये चढ", roman: "basamadhye chaDh" },
    { en: "Get off the bus", mr: "बसमधून उतर", roman: "basamadhUn utar" },
    { en: "How are you feeling? New car!", mr: "कसं वाटलं तुम्हाला? नवीन गाडी!", roman: "kasM vATalM tumhAlA? navIn gADI" },
    { en: "Their work is to not let our roadmap become bridge", mr: "त्यांचं काम काय आहे? आपला हा roadmap bridge बनू द्यायचा नाही", roman: "tyAMchM kAm kAy Ahe? ApalA hA roadmap brij banU dyAyachA nAhI" },
    { en: "I am busy", mr: "मी कामात आहे. बिझी आहे", roman: "mI kAmAt Ahe. bijhI Ahe" },
    { en: "You are busy. Am I sitting idle?", mr: "तू बिझी आणि मी फुकट बसलो आहे का?", roman: "tU bijhI ANi mI phukaT basalo Ahe kA" },
    { en: "To curse / To abuse", mr: "शिवी/शिव्या देणे", roman: "shivI/shivyA deNe" },
    { en: "To curse / To abuse", mr: "शिविगाळ करणे", roman: "shivigAL karaNe" },
    { en: "Can you take me to Tilak road?", mr: "टिळक रोड ला येणार का?", roman: "TiLak roD lA yeNAr kA?" },
    { en: "Where exactly on Tilak road?", mr: "टिळक रोड ला नक्की कुठे जायचेय?", roman: "TiLak roD lA nakkI kuThe jAyachey?" },
    { en: "Show me the meter card", mr: "मला मीटर कार्ड दाखवा", roman: "malA mITar kArD dAkhavA" },
    { en: "Broad Beans", mr: "वाल पापडी / घेवडा", roman: "vAl pApaDI / ghevaDA" },
    { en: "Carrot", mr: "गाजर", roman: "gAjar" },
    { en: "Friend, can you give me menucard?", mr: "मित्रा, जरा मेनूकार्ड देतोस का?", roman: "mitrA, jarA menUkArD detos kA?" },
    { en: "Driver: What happened Sir?", mr: "काय झालं साहेब?", roman: "kAy jhAlM sAheb?" },
    { en: "Police: You jumped signal", mr: "सिग्नल तोडलास तू", roman: "signal toDalAs tU" },
    { en: "Driver: No Sir", mr: "नाही साहेब", roman: "nAhI sAheb" },
    { en: "Police: How come no?", mr: "नाही कसं?", roman: "nAhI kasaM?" },
    { en: "Driver: It is true Sir", mr: "खरंच सांगतो साहेब", roman: "kharaMch sAMgato sAheb" },
    { en: "Driver: I was just following that car", mr: "ती गाडी चालली होती तिच्या मागोमागच मी चाललो होतो", roman: "tI gADI chAlalI hotI tichyA mAgomAgach mI chAlalo hoto" },
    { en: "Police: Don't tell about that car. Tell about you", mr: "त्या गाडीचं मला नको सांगू. तुझं सांग", roman: "tyA gADIchM malA nako sAMgU. tujhaM sAMg" },
    { en: "Police: You broke rule. Pay fine", mr: "रुल मोडला. फाईन भरावी लागेल", roman: "rul moDalA. phAIn bharAvI lAgel" },
    { en: "Police: Pay 500 rupees", mr: "पाचशे रुपये भरा", roman: "pAchashe rupaye bharA" }
  ]
  },
  travel: {
    name: "Travel",
    words: [
    { en: "Good", mr: "चांगले", roman: "Cāṅgale" },
    { en: "Come", mr: "ये", roman: "ye" },
    { en: "Go", mr: "जा", roman: "jA" },
    { en: "You go", mr: "तू जा", roman: "tU jA" },
    { en: "You do not go", mr: "तू जाऊ नकोस", roman: "tU jAU nakos" },
    { en: "They are going to come", mr: "ते येणार आहेत", roman: "te yeNAr Ahet" },
    { en: "I am going to speak", mr: "मी बोलणार आहे", roman: "mI bolaNAr Ahe" },
    { en: "She is going to open door", mr: "ती दार उघडणार आहे", roman: "tI dAr ughaDaNAr Ahe" },
    { en: "You are going to dance", mr: "तू नाचणार आहेस", roman: "tU nAchaNAr Ahes" },
    { en: "Are they going to come?", mr: "ते येणार आहेत का", roman: "te yeNAr Ahet kA" },
    { en: "Am I going to speak?", mr: "मी बोलणार आहे का", roman: "mI bolaNAr Ahe kA" },
    { en: "Is she going to open door?", mr: "ती दार उघडणार आहे का", roman: "tI dAr ughaDaNAr Ahe kA" },
    { en: "Are you going to dance?", mr: "तू नाचणार आहेस का", roman: "tU nAchaNAr Ahes kA" },
    { en: "If you go I will cry", mr: "जर तू गेलास तर मी रडेन", roman: "jar tU gelAs tar mI raDen" },
    { en: "He told me that he is going to come", mr: "तो शाळेत येणार असल्याचे त्याने मला सांगितले", roman: "to shALet yeNAr asalyAche tyAne malA sAMgitale" },
    { en: "come and go", mr: "येऊन जा", roman: "yeUn jA" },
    { en: "They will go and check it", mr: "ते जाऊन तपासतील", roman: "te jAUn tapAsatIl" },
    { en: "till he goes", mr: "तो जाई पर्यंत", roman: "to jAI paryaMt" },
    { en: "until we come", mr: "आम्ही येई पर्यंत", roman: "AmhI yeI paryaMt" },
    { en: "Good horse", mr: "चांगला घोडा", roman: "chAMgalA ghoDA" },
    { en: "For good horse", mr: "चांगल्या घोड्या साठी", roman: "chAMgalyA ghoDyA sAThI" },
    { en: "I will become winner", mr: "मी विजेता होईन", roman: "mI vijetA hoIn" },
    { en: "He will become mad", mr: "तो वेडा होईल", roman: "to veDA hoIl" },
    { en: "He should go", mr: "त्याने जायला पाहिजे", roman: "tyAne jAyalA pAhije" },
    { en: "He should go", mr: "तो गेला पाहिजे", roman: "to gelA pAhije" },
    { en: "You(male) should go", mr: "तू गेला पाहिजेस", roman: "tU gelA pAhijes" },
    { en: "He should not go", mr: "तो गेला नाही पाहिजे", roman: "to gelA nAhI pAhije" },
    { en: "He should go", mr: "त्याने जावे", roman: "tyAne jAve" },
    { en: "I have to go", mr: "मला जावे लागते", roman: "malA jAve lAgate" },
    { en: "Good", mr: "चांगला", roman: "chAMgalA" },
    { en: "Let's go", mr: "चला, आपण जाऊया", roman: "chalA, ApaN jAUyA" },
    { en: "Let's not go", mr: "आपण नको जाऊया", roman: "ApaN nako jAUyA" },
    { en: "Shall we go home? (style 1)", mr: "घरी जाऊया का?", roman: "gharI jAUyA kA?" },
    { en: "Shall we go home? (style 2)", mr: "घरी जायचे का?", roman: "gharI jAyache kA?" },
    { en: "When you come I feel happy", mr: "तू जेव्हा येतोस तेव्हा मला आनंद वाटतो", roman: "tU jevhA yetos tevhA malA AnaMda vATato" },
    { en: "When you(girl) come I feel happy", mr: "तू जेव्हा येतेस तेव्हा मला आनंद वाटतो", roman: "tU jevhA yetes tevhA malA AnaMda vATato" },
    { en: "Go back, the way you have come", mr: "तू जसा आलास तसा परत जा", roman: "tU jasA AlAs tasA parat jA" },
    { en: "Wherever you will go I will come", mr: "तू जिथे जिथे जाशील तिथे तिथे मी येईन", roman: "tU jithe jithe jAshIl tithe tithe mI yeIn" },
    { en: "I would love to visit New York", mr: "मला न्यूयॉर्कला भेट द्यायला आवडली असती", roman: "malA nyUy~orkalA bheT dyAyalA AvaDalI asatI" },
    { en: "I wanted to go", mr: "मला जायचे होते", roman: "malA jAyache hote" },
    { en: "He got a prize", mr: "त्याला बक्षिस मिळाले", roman: "tyAlA bakShis miLAle" },
    { en: "He got 10 prizes", mr: "त्याला १० बक्षिसे मिळाली", roman: "tyAlA 10 bakShise miLAlI" },
    { en: "I forgot to tell you", mr: "तुला सांगायचे राहिले", roman: "tulA sAMgAyache rAhile" },
    { en: "Hey! When did you come?", mr: "अरे! तुम्ही कधी आलात?", roman: "are! tumhI kadhI AlAt?" },
    { en: "Yes! I will surely come", mr: "होय! मी नक्की येणार", roman: "hoy! mI nakkI yeNAr" },
    { en: "Hmm! I got it", mr: "हं! समजलं मला ते", roman: "haM! samajalM malA te" },
    { en: "Very Good", mr: "खूप छान", roman: "khUp ChAn" },
    { en: "Oh! When did you come?", mr: "अगं बाई! तुम्ही कधी आलात?", roman: "agaM bAI! tumhI kadhI AlAt?" },
    { en: "May I come", mr: "मी येऊ का?", roman: "mI yeU kA" },
    { en: "May I go", mr: "मी जाऊ का?", roman: "mI jAU kA" },
    { en: "May we come", mr: "आम्ही येऊ का?", roman: "AmhI yeU kA" },
    { en: "May we go", mr: "आम्ही जाऊ का?", roman: "AmhI jAU kA" },
    { en: "May you come", mr: "तुम्ही येऊ शकता का?", roman: "tumhI yeU shakatA kA?" },
    { en: "May you come", mr: "येता का", roman: "yetA kA" },
    { en: "He may go", mr: "कदाचित तो जाईल", roman: "kadAchit to jAIl" },
    { en: "He might come", mr: "बहुतेक तो येईल", roman: "bahutek to yeIl" },
    { en: "I will surely come", mr: "मी येईनच", roman: "mI yeInach" },
    { en: "I must go there", mr: "मला तिथे जायलाच पाहिजे", roman: "malA tithe jAyalAch pAhije" },
    { en: "As soon as they become", mr: "ते झाल्या झाल्या / ते होताच", roman: "te jhAlyA jhAlyA / te hotAch" },
    { en: "Let me know once he comes", mr: "तो आला की मला सांग", roman: "to AlA kI malA sAMg" },
    { en: "I did not know whether he is going", mr: "तो जाणार आहे का मला माहित नाही", roman: "to jANAr Ahe kA malA mAhit nAhI" },
    { en: "He felt that I will not come", mr: "त्याला असे वाटले की मी येणार नाही", roman: "tyAlA ase vATale kI mI yeNAr nAhI" },
    { en: "To go to toilet", mr: "संडासला जाणे saMDAsalA jANe", roman: "saMDAsalA gelo" },
    { en: "Go", mr: "जाणे jANe", roman: "bAjArAt gelo" },
    { en: "Come", mr: "येणे yeNe", roman: "bAjArAtUn Alo" },
    { en: "Travel", mr: "प्रवास करणे pravAs karaNe", roman: "rAtrabhar pravAs kelA" },
    { en: "I got hurt by knife", mr: "मला सुरी लागली", roman: "malA surI lAgalI" },
    { en: "Lata's song was going on", mr: "लताचे गाणे लागले होते", roman: "latAche gANe lAgale hote" },
    { en: "Gold", mr: "सोनेरी", roman: "sonerI" },
    { en: "Marigold", mr: "झेंडू", roman: "jheMDU" },
    { en: "Rangoon creeper", mr: "मधुमालती", roman: "madhumAlatI" },
    { en: "How to go to Central Park", mr: "सेन्ट्रल पार्कला कसे जायचे", roman: "senTral pArkalA kase jAyache" },
    { en: "Go straight", mr: "सरळ जा", roman: "saraL jA" },
    { en: "Go back", mr: "मागे जा", roman: "mAge jA" },
    { en: "Come here (to boy/girl)", mr: "इकडे ये", roman: "ikaDe ye" },
    { en: "Go there (to boy/girl)", mr: "तिकडे जा", roman: "tikaDe jA" },
    { en: "Hey, how come you are here? You were in ABC company, right?", mr: "अरे तू इकडे कसा काय? तू ABC कंपनीत होतास ना?", roman: "are tU ikaDe kasA kAy? tU ABC kaMpanIt hotAs nA?" },
    { en: "I was not getting good work there", mr: "तिकडे मला काम चांगलं मिळालं नव्हतं.", roman: "tikaDe malA kAm chAMgalM miLAlM navhatM." },
    { en: "It is good", mr: "चांगलीये", roman: "chAMgalIye." },
    { en: "How do you travel to office?", mr: "Office ला कसा येतोस?", roman: "office lA kasA yetos?" },
    { en: "I will also go and see it", mr: "मी पण जाउन बघून येईन.", roman: "mI paN jAun baghUn yeIn" },
    { en: "Go for sure", mr: "नक्की जा.", roman: "nakkI jA." },
    { en: "Good", mr: "बरं झालं.", roman: "baraM jhAlM." },
    { en: "Come aunty", mr: "या मावशी", roman: "yA mAvashI" },
    { en: "See you / Will come again", mr: "येते मी.", roman: "yete mI." },
    { en: "Constitution got approval on Nov 26, 1949", mr: "संविधानाला २६ नोव्हेंबर १९४९ मध्ये मंजुरी मिळाली.", roman: "sMvidhAnAlA novheMbar madhye mMjurI miLAlI." },
    { en: "Only 1 goal. We won 1-0", mr: "एकच गोल झाला. आम्ही एक-शून्य असे जिंकलो.", roman: "ekach gol jhAlA. AmhI ekshUny ase jiMkalo." },
    { en: "Let's go to watch Raazi", mr: "आपण राझी बघायला जाऊया.", roman: "ApaN rAjhI baghAyalA jAUyA." },
    { en: "Let's go to watch Surma", mr: "मग सूरमा बघायला जाऊया.", roman: "mag sUramA baghAyalA jAUyA." },
    { en: "Let's go and watch Kaala", mr: "काला बघायला जाऊया.", roman: "kAlA baghAyalA jAUyA." },
    { en: "Yes friend, that was a very good match", mr: "हो मित्रा, खूप चांगली होती.", roman: "ho mitrA, khUp chAMgalI hotI." },
    { en: "Korea defended very good", mr: "कोरियाने खूप चांगला डिफेन्स केला", roman: "koriyAne khUp chAMgalA Diphens kelA" },
    { en: "I am going to my hobby class", mr: "मी माझ्या छंदवर्गाला जातोय.", roman: "mI maajhyA ChaMdavargAlA jaatoy." },
    { en: "He goes by plane", mr: "तो विमानाने जातो", roman: "to vimAnAne jAto" },
    { en: "He walks to office / He goes by foot", mr: "तो चालत जातो", roman: "to chAlat jAto" },
    { en: "I can't draw Rangoli", mr: "मला रांगोळी काढता येत नाही", roman: "malA rAMgoLI kADhatA yet nAhI" },
    { en: "I am going to my hometown", mr: "मी गावाला जाणार आहे", roman: "mI gAvAlA jANAr Ahe" },
    { en: "Come closer", mr: "जवळ ये", roman: "javaL ye" },
    { en: "Keep going", mr: "पुढे जात रहा", roman: "puDhe jAt rahA" },
    { en: "How did it go?", mr: "कसं झालं", roman: "kasaM jhAlM" },
    { en: "Because of the virus, I can't go out", mr: "विषाणूमुळे, मी माझ्या मित्रांबरोबर बाहेर जाऊ शकत नाही", roman: "viShANUmuLe, mI mAjhyA mitrAMbarobar bAher jAU shakat nAhI" },
    { en: "I need to go to the grocery store", mr: "मला किराणा दुकानात जायचं आहे", roman: "malA kirANA dukAnAt jAyachaM Ahe" },
    { en: "Once a boy goes to see a girl for marriage", mr: "एकदा एक मुलगा लग्नासाठी मुलगी बघायला जातो", roman: "ekadA ek mulagA lagnAsAThI mulagI baghAyalA jAto" },
    { en: "The gown has been put outside to dry", mr: "गाऊन बाहेर वाळत टाकला आहे", roman: "gAUn bAher vALat TAkalA Ahe" },
    { en: "Social media has good and bad points", mr: "सोशल मीडियाचे चांगले व वाईट मुद्दे आहेत", roman: "soshal mIDiyAche chAMgale v vAIT mudde Ahet" },
    { en: "Then, is there a party after going home?", mr: "मग आज घरी गेल्यावर पार्टी?", roman: "mag Aj gharI gelyAvar pArTI" },
    { en: "Comes from Amaravati and grabs the trophy", mr: "कुठे ते अमरावतीवरून येऊन एक trophy घेऊन जातो", roman: "kuThe te amarAvatIvarUn yeUn ek trofy gheUn jAto" },
    { en: "May god grace you", mr: "देव तुझं भलं करो", roman: "dev tujhaM bhalaM karo" },
    { en: "May God bless you", mr: "देव तुम्हाला आशिर्वाद देवो", roman: "dev tumhAlA AshirvAd devo" },
    { en: "May God bless you (custom)", mr: "देव तुमचं भलं करो", roman: "dev tumachaM bhalaM karo" },
    { en: "May God not bless you", mr: "देव तुम्हाला आशिर्वाद न देवो", roman: "dev tumhAlA AshirvAd na devo" },
    { en: "Rangoli", mr: "रांगोळी", roman: "rAMgoLI" },
    { en: "To draw rangoli", mr: "रांगोळी काढणे", roman: "rAMgoLI kADhaNe" },
    { en: "Hey, Boss has come", mr: "साहेब आलेरे", roman: "sAheb Alere" },
    { en: "Come (to boy)", mr: "येरे", roman: "yere" },
    { en: "Come (to girl)", mr: "येगं", roman: "yegaM" },
    { en: "Come (to elder)", mr: "याहो", roman: "yAho" },
    { en: "Do come to my marriage", mr: "माझ्या लग्नाला ये. येहं", roman: "mAjhyA lagnAlA ye. yehaM" },
    { en: "I am Fiona, your local tour guide", mr: "मी फिओना, तुमची स्थानिक टूर गाईड.", roman: "mI phionA, tumachI sthAnik TUr gAID." },
    { en: "I will also come", mr: "मीही येईन", roman: "mIhI yeIn" },
    { en: "Goose / Swan", mr: "हंस", roman: "haMs" },
    { en: "Goat", mr: "शेळी", roman: "sheLI" },
    { en: "Male goat", mr: "बोकड", roman: "bokaD" },
    { en: "Mongoose", mr: "मुंगूस", roman: "muMgUs" },
    { en: "Ashgourd", mr: "कोहळा", roman: "kohaLA" },
    { en: "Bitter Gourd", mr: "कारले", roman: "kArale" },
    { en: "Bottle Gourd", mr: "दूधी भोपळा", roman: "dUdhI bhopaLA" },
    { en: "Ridgegourd", mr: "दोडका", roman: "doDakA" },
    { en: "Aunty my exams were going on", mr: "हो काकू. माझी परीक्षा चालू होती म्हणून मी नाही आलो.", roman: "ho kAkU. mAjhI parIkShA chAlU hotI mhaNUn mI nAhI Alo." },
    { en: "Should I visit again?", mr: "पुन्हा दाखवायला येऊ का?", roman: "punhA dAkhavAyalA yeU kA?" }
  ]
  },
  shopping: {
    name: "Shopping",
    words: [
    { en: "I want to buy but shop is closed", mr: "मला खरेदी करायची आहे पण दुकान बंद आहे", roman: "malA kharedI karAyachI Ahe paN dukAn baMd Ahe" },
    { en: "To buy", mr: "विकत घेणे vikat gheNe", roman: "sharT vikat ghetalA" },
    { en: "To buy ticket", mr: "तिकिट काढणे tikiT kADhaNe", roman: "tikiT kADhale" },
    { en: "To sell", mr: "विकणे vikaNe", roman: "sharT vikalA" },
    { en: "Did you buy flat?", mr: "तू घेतला आहेस का flat?", roman: "tU ghetalA Ahes kA flat?" },
    { en: "May shop open soon", mr: "दुकान लवकर उघडो", roman: "dukAn lavakar ughaDo" },
    { en: "Grasshopper", mr: "नाकतोडा", roman: "nAkatoDA" }
  ]
  },
  emergency: {
    name: "Emergency",
    words: [
    { en: "Help", mr: "मदत करणे madat karaNe", roman: "tyAlA madat kelI" },
    { en: "Who can help me?", mr: "मला कोण मदत करू शकेल?", roman: "malA koN madat karU shakel?" },
    { en: "May he help you", mr: "तो तुम्हाला मदत करो", roman: "to tumhAlA madat karo" },
    { en: "May they help you", mr: "ते तुम्हाला मदत करोत", roman: "te tumhAlA madat karot" },
    { en: "May he not help you", mr: "तो तुम्हाला मदत न करो", roman: "to tumhAlA madat na karo" }
  ]
  }
};


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
  },
  punjabi: {
    name: "Punjabi",
    code: "pa",
    subtitle: "ਪੰਜਾਬੀ ਸਿੱਖੋ",
    scriptFont: "'Noto Sans Gurmukhi', sans-serif",
    speechLang: "pa-IN",
    dataSource: "BhaashaBuddy (web)",
    hasLessons: true,
    dataFile: "data_punjabi.json",
    structureFile: "lessons_structure_punjabi.json",
    PHRASES: typeof PUNJABI_PHRASES !== "undefined" ? PUNJABI_PHRASES : {},
    DICTIONARY: typeof PUNJABI_DICTIONARY !== "undefined" ? PUNJABI_DICTIONARY : []
  },
  kannada: {
    name: "Kannada",
    code: "kn",
    subtitle: "ಕನ್ನಡ ಕಲಿಯಿರಿ",
    scriptFont: "'Noto Sans Kannada', sans-serif",
    speechLang: "kn-IN",
    dataSource: "BhaashaBuddy (Marathi → Kannada)",
    hasLessons: true,
    dataFile: "data_kannada.json",
    structureFile: "lessons_structure_kannada.json",
    PHRASES: typeof KANNADA_PHRASES !== "undefined" ? KANNADA_PHRASES : {},
    DICTIONARY: typeof KANNADA_DICTIONARY !== "undefined" ? KANNADA_DICTIONARY : []
  },
  tamil: {
    name: "Tamil",
    code: "ta",
    subtitle: "தமிழ் கற்க",
    scriptFont: "'Noto Sans Tamil', sans-serif",
    speechLang: "ta-IN",
    dataSource: "BhaashaBuddy (web)",
    hasLessons: true,
    dataFile: "data_tamil.json",
    structureFile: "lessons_structure_tamil.json",
    PHRASES: typeof TAMIL_PHRASES !== "undefined" ? TAMIL_PHRASES : {},
    DICTIONARY: typeof TAMIL_DICTIONARY !== "undefined" ? TAMIL_DICTIONARY : []
  },
  maithili: {
    name: "Maithili",
    code: "mai",
    subtitle: "मैथिली सीखू",
    scriptFont: "'Noto Sans Devanagari', sans-serif",
    speechLang: "hi-IN",
    dataSource: "BhaashaBuddy (web)",
    hasLessons: true,
    dataFile: "data_maithili.json",
    structureFile: "lessons_structure_maithili.json",
    PHRASES: typeof MAITHILI_PHRASES !== "undefined" ? MAITHILI_PHRASES : {},
    DICTIONARY: typeof MAITHILI_DICTIONARY !== "undefined" ? MAITHILI_DICTIONARY : []
  },
  telugu: {
    name: "Telugu",
    code: "te",
    subtitle: "తెలుగు నేర్చుకోండి",
    scriptFont: "'Noto Sans Telugu', sans-serif",
    speechLang: "te-IN",
    dataSource: "BhaashaBuddy (web)",
    hasLessons: true,
    dataFile: "data_telugu.json",
    structureFile: "lessons_structure_telugu.json",
    PHRASES: typeof TELUGU_PHRASES !== "undefined" ? TELUGU_PHRASES : {},
    DICTIONARY: typeof TELUGU_DICTIONARY !== "undefined" ? TELUGU_DICTIONARY : []
  },
  bengali: {
    name: "Bengali",
    code: "bn",
    subtitle: "বাংলা শিখুন",
    scriptFont: "'Noto Sans Bengali', sans-serif",
    speechLang: "bn-IN",
    dataSource: "BhaashaBuddy (web)",
    hasLessons: true,
    dataFile: "data_bengali.json",
    structureFile: "lessons_structure_bengali.json",
    PHRASES: typeof BENGALI_PHRASES !== "undefined" ? BENGALI_PHRASES : {},
    DICTIONARY: typeof BENGALI_DICTIONARY !== "undefined" ? BENGALI_DICTIONARY : []
  },
  assamese: {
    name: "Assamese",
    code: "as",
    subtitle: "অসমীয়া শিকক",
    scriptFont: "'Noto Sans Bengali', sans-serif",
    speechLang: "as-IN",
    dataSource: "BhaashaBuddy (web)",
    hasLessons: true,
    dataFile: "data_assamese.json",
    structureFile: "lessons_structure_assamese.json",
    PHRASES: typeof ASSAMESE_PHRASES !== "undefined" ? ASSAMESE_PHRASES : {},
    DICTIONARY: typeof ASSAMESE_DICTIONARY !== "undefined" ? ASSAMESE_DICTIONARY : []
  },
  malayalam: {
    name: "Malayalam",
    code: "ml",
    subtitle: "മലയാളം പഠിക്കാം",
    scriptFont: "'Noto Sans Malayalam', sans-serif",
    speechLang: "ml-IN",
    dataSource: "BhaashaBuddy (web)",
    hasLessons: true,
    dataFile: "data_malayalam.json",
    structureFile: "lessons_structure_malayalam.json",
    PHRASES: typeof MALAYALAM_PHRASES !== "undefined" ? MALAYALAM_PHRASES : {},
    DICTIONARY: typeof MALAYALAM_DICTIONARY !== "undefined" ? MALAYALAM_DICTIONARY : []
  },
  nepali: {
    name: "Nepali",
    code: "ne",
    subtitle: "नेपाली सिकौं",
    scriptFont: "'Noto Sans Devanagari', sans-serif",
    speechLang: "ne-NP",
    dataSource: "BhaashaBuddy (web)",
    hasLessons: true,
    dataFile: "data_nepali.json",
    structureFile: "lessons_structure_nepali.json",
    PHRASES: {},
    DICTIONARY: []
  }
};

// ===== STATE =====
let currentTab = 'home';
let currentCategory = null;
let previousScreen = 'home';
let expandedCategory = null;
let expandedDictSection = null;
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

function toggleDictSection(secId) {
  if (expandedDictSection === secId) expandedDictSection = null;
  else expandedDictSection = secId;
  renderDict(document.getElementById('dict-search').value);
}

function renderDict(query) {
  const list = document.getElementById('dict-list');
  const q = (query || '').toLowerCase();
  const bySection = getDICTIONARY_BY_SECTION();
  const speakerSvg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>';
  const bookmarkSvg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m19 21-7-4-7 4V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>';

  const renderWordRow = (d, i) => {
    const isSaved = savedPhrases.some(s => s.mr === d.mr);
    return `<div class="phrase-row phrase-row-flat dict-row">
      <div class="phrase-row-text">
        <span class="phrase-en">${d.en}</span>
        <span class="phrase-roman">${d.roman}</span>
        <span class="phrase-mr" style="font-family:${getScriptFont()}">${d.mr}</span>
      </div>
      <div class="phrase-row-actions">
        <button class="phrase-save-btn phrase-save-btn-icon ${isSaved ? 'saved' : ''}" onclick="event.stopPropagation(); saveDictItem(${i})" title="Bookmark">${bookmarkSvg}</button>
        <button class="phrase-speaker-btn" onclick="event.stopPropagation(); speakDictItem(${i})" title="Pronounce">${speakerSvg}</button>
      </div>
    </div>`;
  };

  if (q) {
    lastDictItems = getDICTIONARY().filter(d => d.en.toLowerCase().includes(q) || d.roman.toLowerCase().includes(q));
    list.innerHTML = lastDictItems.map((d, i) => renderWordRow(d, i)).join('');
    return;
  }

  if (bySection) {
    lastDictItems = [];
    let globalIdx = 0;
    list.innerHTML = Object.entries(bySection).map(([secId, secData]) => {
      if (!secData || !secData.words || !secData.words.length) return '';
      const words = secData.words;
      const isExpanded = expandedDictSection === secId;
      const baseId = secId.split('_')[0]; // support Set 1/2/3 ids like greetings_1
      const iconUrl = CAT_IMAGES[secId] || CAT_IMAGES[baseId] || '';
      const fallback = CAT_INITIALS[secId] || CAT_INITIALS[baseId] || secId.slice(0, 2);
      const iconHtml = iconUrl
        ? `<img class="cat-icon-img" src="${iconUrl}" alt="" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" /><span class="cat-icon cat-icon-fallback" style="display:none" data-initial="${fallback}"></span>`
        : `<span class="cat-icon" data-initial="${fallback}"></span>`;
      const rowsHtml = isExpanded ? words.map((d, wi) => {
        lastDictItems.push(d);
        const idx = lastDictItems.length - 1;
        return renderWordRow(d, idx);
      }).join('') : '';
      return `<div class="cat-row">
        <div class="cat-row-header" onclick="toggleDictSection('${secId}')">
          <span class="cat-icon-wrap">${iconHtml}</span>
          <div class="cat-row-info">
            <span class="cat-name">${secData.name || secId}</span>
            <span class="cat-count">${words.length} words</span>
          </div>
          <span class="cat-expand">${isExpanded ? '−' : '+'}</span>
        </div>
        ${isExpanded ? `<div class="cat-row-phrases">${rowsHtml}</div>` : ''}
      </div>`;
    }).join('');
    return;
  }

  lastDictItems = getDICTIONARY();
  list.innerHTML = lastDictItems.map((d, i) => renderWordRow(d, i)).join('');
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

// ===== SETTINGS (OFFLINE MODE) =====
const OFFLINE_STORAGE_KEY = 'offlineModeEnabled';
const OFFLINE_CACHE_PREFIX = 'offline_lessons_';

let offlineEnabled = localStorage.getItem(OFFLINE_STORAGE_KEY) !== 'false';

function initOfflineToggle() {
  const t = document.getElementById('offline-toggle');
  if (t) t.className = 'toggle' + (offlineEnabled ? '' : ' off');
}

function toggleOffline() {
  offlineEnabled = !offlineEnabled;
  localStorage.setItem(OFFLINE_STORAGE_KEY, offlineEnabled ? 'true' : 'false');
  const t = document.getElementById('offline-toggle');
  if (t) t.className = 'toggle' + (offlineEnabled ? '' : ' off');
  showToast(offlineEnabled ? 'Offline mode enabled' : 'Offline mode disabled');
}

function getOfflineCacheKey() {
  return OFFLINE_CACHE_PREFIX + (selectedLanguage || 'marathi');
}

function saveLessonsToCache(data, structure) {
  if (!offlineEnabled || !selectedLanguage) return;
  try {
    localStorage.setItem(getOfflineCacheKey(), JSON.stringify({ data, structure }));
  } catch (e) {
    console.warn('Offline cache save failed', e);
  }
}

function loadLessonsFromCache() {
  try {
    const raw = localStorage.getItem(getOfflineCacheKey());
    if (!raw) return null;
    return JSON.parse(raw);
  } catch (e) {
    return null;
  }
}

// ===== DATA ADDITION & RATE THE APP =====
// Google Apps Script Web App URL – receives data addition (and feedback) submissions
const FEEDBACK_SHEET_URL = 'https://script.google.com/macros/s/AKfycbwuQVHBxBaDLohbvFg1Ux_eqWEiRmJORTgOZUEZ0N_SqKEMLCqE8YQDcGgkbl1bj60/exec';

function onDataAdditionTypeChange(value) {
  const form = document.getElementById('data-addition-form');
  if (!form) return;
  if (!value) {
    form.style.display = 'none';
    const msg = document.getElementById('data-addition-message');
    if (msg) msg.value = '';
    return;
  }
  form.style.display = 'block';
}

function sendDataSuggestion() {
  const typeEl = document.getElementById('data-addition-type');
  const messageEl = document.getElementById('data-addition-message');
  const type = (typeEl && typeEl.value) || '';
  const labels = { phrase: 'Phrase', words: 'Words', lessons: 'Lessons' };
  const typeLabel = labels[type] || type;

  if (!type) {
    showToast('Please select Phrase, Words or Lessons first');
    return;
  }

  const message = (messageEl && messageEl.value.trim()) || '';
  if (!FEEDBACK_SHEET_URL) {
    showToast('Feedback sheet not configured');
    return;
  }

  const btn = document.querySelector('.data-addition-btn');
  if (btn) {
    btn.disabled = true;
    btn.textContent = 'Sending...';
  }

  const iframe = document.createElement('iframe');
  iframe.name = 'data-suggestion-frame-' + Date.now();
  iframe.style.cssText = 'position:absolute;width:0;height:0;border:0;visibility:hidden';
  document.body.appendChild(iframe);

  const form = document.createElement('form');
  form.method = 'POST';
  form.action = FEEDBACK_SHEET_URL;
  form.target = iframe.name;
  form.style.display = 'none';

  const fields = {
    type: 'Data addition: ' + typeLabel,
    message: message || '(No message)',
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

  function done() {
    form.remove();
    if (iframe.parentNode) iframe.remove();
    if (btn) {
      btn.disabled = false;
      btn.textContent = 'Send suggestion';
    }
    if (messageEl) messageEl.value = '';
    showToast('Thank you! Suggestion sent.');
  }

  iframe.onload = function() {
    iframe.onload = null;
    setTimeout(done, 300);
  };
  setTimeout(done, 6000);
  form.submit();
}

// Replace with your app’s store URLs when published
const PLAY_STORE_URL = 'https://play.google.com/store/apps/details?id=YOUR_PACKAGE_ID';
const APP_STORE_URL = 'https://apps.apple.com/app/idYOUR_APP_ID';

function openStoreRating(store) {
  const url = store === 'play' ? PLAY_STORE_URL : APP_STORE_URL;
  if (url && !url.includes('YOUR_')) window.open(url, '_blank');
  else showToast('Rate us on ' + (store === 'play' ? 'Google Play Store' : 'App Store'));
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
    const option = e.target.closest('.theme-option');
    const btn = option?.querySelector('.theme-swatch') || e.target.closest('.theme-swatch');
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
    if (!/letter|transliteration|sound|character|kannada|marathi|devanagari|tamil|telugu|bengali|bangla|assamese|malayalam|nepali|script/.test(hStr)) return false;
    // Any Indian-script letter (Devanagari, Gurmukhi, Gujarati, Bengali, Telugu, Kannada, Tamil, etc.)
    return rows.every(r => Array.isArray(r) && r.length >= 2 && /[\u0900-\u0D7F]/.test(String(r[0])));
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
      h += '<span class="alphabet-script" style="font-family:' + getScriptFont() + '">' + escape(letter) + '</span>';
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
        const isScript = /[\u0900-\u0D7F]/.test(cell);
        const cls = isScript ? ' class="busuu-script-cell"' : '';
        const style = isScript ? ' style="font-family:' + getScriptFont() + '"' : '';
        h += '<td' + cls + style + '>' + escape(cell) + '</td>';
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
          const isScript = /[\u0900-\u097F\u0A00-\u0A7F\u0B80-\u0BFF\u0C80-\u0CFF]/.test(cell);
          const cls = isScript ? ' class="busuu-script-cell"' : '';
          const style = isScript ? ' style="font-family:' + getScriptFont() + '"' : '';
          html += '<td' + cls + style + '>' + escape(cell) + '</td>';
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

  function applyChaptersData(data, structure) {
    allChapters = data;
    lessonsStructure = structure;
    chaptersById = {};
    if (allChapters) allChapters.forEach(ch => { chaptersById[ch.id] = ch; });
    chaptersLoaded = true;
    chaptersLoadedForLang = selectedLanguage;
    loading.style.display = 'none';
    error.style.display = 'none';
    renderLessonsList();
  }

  function showLoadError(msg) {
    loading.style.display = 'none';
    error.style.display = 'block';
    document.getElementById('chapters-error').innerHTML = `
      <div class="error-icon" style="margin:0 auto 12px;"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg></div>
      <div style="font-weight:800;color:var(--text);margin-bottom:6px;">${msg}</div>
      <div style="font-size:12px;color:var(--text-muted);font-weight:600;">Enable offline mode and load lessons once while online to use them offline.</div>`;
  }

  const cached = loadLessonsFromCache();
  const isOffline = typeof navigator !== 'undefined' && !navigator.onLine;

  if (isOffline && cached && cached.data && cached.structure) {
    applyChaptersData(cached.data, cached.structure);
    showToast('Showing cached lessons (offline)');
    return;
  }
  if (isOffline) {
    showLoadError('You\'re offline');
    return;
  }

  try {
    const [chaptersRes, structureRes] = await Promise.all([
      fetch(dataFile),
      fetch(structureFile)
    ]);
    if (!chaptersRes.ok) throw new Error(dataFile + ' not found');
    if (!structureRes.ok) throw new Error(structureFile + ' not found');
    const data = await chaptersRes.json();
    const structure = await structureRes.json();
    applyChaptersData(data, structure);
    saveLessonsToCache(data, structure);
  } catch (e) {
    if (cached && cached.data && cached.structure) {
      applyChaptersData(cached.data, cached.structure);
      showToast('Using cached lessons (network failed)');
      return;
    }
    showLoadError(e.message || 'Failed to load');
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
  let majorIdx = 0;
  for (const major of lessonsStructure.majorLessons) {
    majorIdx++;
    let subIdx = 0;
    for (const s of major.sublessons || []) {
      subIdx++;
      if (s.chapterId === chapterId) return majorIdx + '.' + subIdx;
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

    const majorNum = lessonsStructure.majorLessons.indexOf(major) + 1;
    const sublessonsHtml = isMajorExpanded ? sublessons.map((s) => {
      const ch = s.chapterId != null ? chaptersById[s.chapterId] : null;
      const hasContent = !!ch;
      const headerOnclick = hasContent ? `onclick="openChapter(${s.chapterId})"` : '';
      const subNum = majorNum + '.' + ((major.sublessons || []).indexOf(s) + 1);
      return `
      <div class="chapter-sub-row">
        <div class="chapter-row-header" ${headerOnclick}>
          <div class="chapter-row-title"><span class="lesson-sub-num">${subNum}</span> ${s.title}</div>
          ${hasContent ? '<span class="chapter-expand">→</span>' : ''}
        </div>
      </div>
      `;
    }).join('') : '';

    return `
    <div class="major-lesson-row">
      <div class="major-lesson-header" onclick="toggleMajorLesson('${major.name.replace(/'/g, "\\'")}')">
        <div class="major-lesson-name">Lesson ${majorNum}: ${major.name}</div>
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

// ===== SCROLL TO TOP =====
function scrollToTop() {
  // Scroll the active screen (Phrases, Words, Lessons, lesson content – this is the main scroll container)
  const active = document.querySelector('#app-content .screen.active');
  if (active) active.scrollTop = 0;
  // Scroll main and window in case the page scrolls instead
  const main = document.getElementById('app-content');
  if (main) main.scrollTop = 0;
  window.scrollTo({ top: 0, behavior: 'smooth' });
  document.documentElement.scrollTop = 0;
  document.body.scrollTop = 0;
}

function initScrollToTop() {
  /* Button is always visible when language selected (CSS body.nav-visible); no scroll-based show/hide */
}

// ===== INIT ON LOAD =====
function initApp() {
  initTheme();
  initOfflineToggle();
  initScrollToTop();
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
