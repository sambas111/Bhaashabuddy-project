/**
 * BhaashaBuddy Feedback - Google Apps Script (Sheet1 only, menu-based)
 *
 * SETUP (do in this order):
 * 1. Paste this entire script into Extensions → Apps Script
 * 2. Run → setupSheet1        (creates the header area on Sheet1)
 * 3. Deploy → New deployment → Web app
 *    Execute as: Me | Who has access: Anyone
 * 4. Authorize Drive (first run of doPost with files creates a folder in your Drive)
 * 5. Paste the Web App URL into app.js as FEEDBACK_SHEET_URL
 *
 * TO ENABLE/DISABLE FEEDBACK:
 * Use the "🛠 BhaashaBuddy" menu that appears in the Google Sheets menu bar.
 *
 * Sheet1 layout:
 *   Row 1 : Title banner (A1:H1)
 *   Row 2 : "Feedback Status:" | TRUE/FALSE (B2) | …
 *   Row 3 : "Last Changed:"    | timestamp (B3)
 *   Row 4 : blank spacer
 *   Row 5 : Timestamp | Type | Rating | Message | Email | Language | Version | Attachments
 *   Row 6+: Feedback data rows (Attachments = Drive URLs, one per line if multiple files)
 *
 * App sends (POST): type, rating, message, email, language, version, attachments
 *   attachments = JSON array: [{ name, type, size, data }] where data is base64 (from the web app)
 */

const SHEET_ID = '1a8vppsvQ21QGuoTG3vSSlRA27xqLNsOUMatlHqMUHHI';
const STATUS_CELL = 'B2';
const DATA_START_ROW = 5;

var FEEDBACK_FOLDER_PROP = 'FEEDBACK_UPLOAD_FOLDER_ID';

// ─── Helpers ──────────────────────────────────────────────────────────────────

function getSpreadsheet() {
  return SpreadsheetApp.openById(SHEET_ID);
}

function getSheet1() {
  const ss = getSpreadsheet();
  return ss.getSheetByName('Sheet1') || ss.getSheets()[0];
}

/** Prefer e.parameter so URL-encoded bodies are parsed correctly (messages with & etc.). */
function getPostFields_(e) {
  const p = e && e.parameter;
  if (p && typeof p === 'object' && (p.type != null || p.message != null || p.attachments != null)) {
    return {
      type: String(p.type || ''),
      rating: String(p.rating || ''),
      message: String(p.message || ''),
      email: String(p.email || ''),
      language: String(p.language || ''),
      version: String(p.version || ''),
      attachments: String(p.attachments || '')
    };
  }
  if (e && e.postData && e.postData.contents) {
    const ct = (e.postData.type || '').toLowerCase();
    const raw = e.postData.contents || '';
    if (ct.indexOf('json') >= 0) {
      try {
        const j = JSON.parse(raw);
        return {
          type: String(j.type || ''),
          rating: String(j.rating || ''),
          message: String(j.message || ''),
          email: String(j.email || ''),
          language: String(j.language || ''),
          version: String(j.version || ''),
          attachments: typeof j.attachments === 'string' ? j.attachments : JSON.stringify(j.attachments || '')
        };
      } catch (err) {
        return { type: '', rating: '', message: '', email: '', language: '', version: '', attachments: '' };
      }
    }
    return parseFormData_(raw);
  }
  return { type: '', rating: '', message: '', email: '', language: '', version: '', attachments: '' };
}

function parseFormData_(str) {
  const out = { type: '', rating: '', message: '', email: '', language: '', version: '', attachments: '' };
  if (!str) return out;
  str.split('&').forEach(function(pair) {
    const i = pair.indexOf('=');
    if (i > 0) {
      const k = decodeURIComponent(pair.substring(0, i).replace(/\+/g, ' '));
      const v = decodeURIComponent((pair.substring(i + 1) || '').replace(/\+/g, ' '));
      if (k in out) out[k] = v;
    }
  });
  return out;
}

/** Create / reuse a Drive folder for uploaded files (script runs as you). */
function getOrCreateFeedbackFolder_() {
  const props = PropertiesService.getScriptProperties();
  let id = props.getProperty(FEEDBACK_FOLDER_PROP);
  if (id) {
    try {
      return DriveApp.getFolderById(id);
    } catch (e) {
      props.deleteProperty(FEEDBACK_FOLDER_PROP);
    }
  }
  const folder = DriveApp.createFolder('BhaashaBuddy Feedback Uploads');
  props.setProperty(FEEDBACK_FOLDER_PROP, folder.getId());
  return folder;
}

/**
 * Parse attachments JSON, upload to Drive, return RichText (clickable file names) or plain fallback.
 * @returns {{ rich: GoogleAppsScript.Spreadsheet.RichTextValue|null, plain: string }}
 */
function saveAttachmentsToDrive_(attachmentsRaw) {
  if (!attachmentsRaw || String(attachmentsRaw).trim() === '') {
    return { rich: null, plain: '' };
  }
  var list;
  try {
    list = JSON.parse(String(attachmentsRaw));
  } catch (e) {
    return { rich: null, plain: 'Parse error (attachments)' };
  }
  if (!list || !list.length) {
    return { rich: null, plain: '' };
  }

  const folder = getOrCreateFeedbackFolder_();
  /** @type {{type:string,name?:string,url?:string,text?:string}[]} */
  var parts = [];
  for (var i = 0; i < list.length; i++) {
    var item = list[i];
    if (!item || !item.data) continue;
    var name = sanitizeFilename_(item.name || ('upload-' + (i + 1)));
    var mime = item.type || 'application/octet-stream';
    try {
      var bytes = Utilities.base64Decode(String(item.data));
      var blob = Utilities.newBlob(bytes, mime, name);
      var file = folder.createFile(blob);
      file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
      parts.push({ type: 'link', name: file.getName(), url: file.getUrl() });
    } catch (err) {
      parts.push({ type: 'text', text: name + ' (upload failed — ' + err.message + ')' });
    }
  }
  if (!parts.length) {
    return { rich: null, plain: '' };
  }

  var rich = buildAttachmentsRichText_(parts);
  if (rich) {
    return { rich: rich, plain: '' };
  }
  return {
    rich: null,
    plain: parts
      .map(function(p) {
        return p.type === 'link' ? p.name + '\n' + p.url : p.text;
      })
      .join('\n')
  };
}

/**
 * One line per file: "📎 filename" is a single clickable hyperlink. Plain lines for errors.
 */
function buildAttachmentsRichText_(parts) {
  var fullText = '';
  var linkRanges = [];
  for (var i = 0; i < parts.length; i++) {
    var p = parts[i];
    if (p.type === 'link') {
      if (fullText.length > 0) fullText += '\n';
      var start = fullText.length;
      fullText += '📎 ' + p.name;
      var end = fullText.length;
      linkRanges.push({ start: start, end: end, url: p.url });
    } else {
      if (fullText.length > 0) fullText += '\n';
      fullText += p.text;
    }
  }
  if (!fullText) return null;
  if (!linkRanges.length) return null;

  var builder = SpreadsheetApp.newRichTextValue().setText(fullText);
  for (var j = 0; j < linkRanges.length; j++) {
    var L = linkRanges[j];
    builder.setLinkUrl(L.start, L.end, L.url);
  }
  return builder.build();
}

function sanitizeFilename_(name) {
  var s = String(name).replace(/[/\\?*:[\]]/g, '_');
  if (s.length > 200) s = s.substring(0, 200);
  return s || 'file';
}

// ─── Toggle logic ─────────────────────────────────────────────────────────────

function isFeedbackEnabled() {
  const v = getSheet1().getRange(STATUS_CELL).getValue();
  return v === true || String(v).toUpperCase() === 'TRUE';
}

function enableFeedback() {
  getSheet1().getRange(STATUS_CELL).setValue(true);
  refreshStatusUI_();
  SpreadsheetApp.getUi().alert('✅  Feedback collection is now ENABLED.');
}

function disableFeedback() {
  getSheet1().getRange(STATUS_CELL).setValue(false);
  refreshStatusUI_();
  SpreadsheetApp.getUi().alert('🚫  Feedback collection is now DISABLED.');
}

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('🛠 BhaashaBuddy')
    .addItem('✅  Enable Feedback', 'enableFeedback')
    .addItem('🚫  Disable Feedback', 'disableFeedback')
    .addSeparator()
    .addItem('🔄  Refresh Status Display', 'refreshStatusUI_')
    .addToUi();
}

// ─── Sheet1 setup ─────────────────────────────────────────────────────────────

function setupSheet1() {
  const sheet = getSheet1();

  sheet.getRange('A1:H1')
    .merge()
    .setValue('BhaashaBuddy — Feedback Admin Controls')
    .setFontSize(14).setFontWeight('bold')
    .setBackground('#1a73e8').setFontColor('#ffffff')
    .setHorizontalAlignment('center').setVerticalAlignment('middle');
  sheet.setRowHeight(1, 44);

  sheet.getRange('A2').setValue('Feedback Status:')
    .setFontWeight('bold').setFontSize(11).setVerticalAlignment('middle');

  const statusCell = sheet.getRange(STATUS_CELL);
  if (statusCell.getValue() === '') statusCell.setValue(true);

  sheet.getRange('D2').setValue(
    '👆 Use the  "🛠 BhaashaBuddy"  menu above to Enable / Disable feedback.'
  ).setFontStyle('italic').setFontColor('#555555');

  sheet.getRange('A3').setValue('Last Changed:').setFontWeight('bold');
  sheet.getRange('B3').setValue(new Date())
    .setNumberFormat('yyyy-mm-dd hh:mm:ss');

  sheet.getRange('A4:H4').clearContent().clearFormat();
  sheet.setRowHeight(4, 10);

  const headers = [
    'Timestamp', 'Type', 'Rating', 'Message', 'Email', 'Language', 'Version', 'Attachments'
  ];
  const headerRange = sheet.getRange(DATA_START_ROW, 1, 1, headers.length);
  headerRange.setValues([headers])
    .setBackground('#f3f3f3').setFontWeight('bold')
    .setBorder(true, true, true, true, true, true);

  [180, 120, 70, 300, 200, 100, 80, 320].forEach(function(w, i) {
    sheet.setColumnWidth(i + 1, w);
  });

  refreshStatusUI_();

  SpreadsheetApp.getUi().alert(
    '✅  Sheet1 is set up!\n\n' +
    'Column H = Attachments (clickable Drive links on each file name).\n' +
    'Re-deploy the web app if you changed this script.\n' +
    'Use the menu to Enable or Disable feedback collection.'
  );
}

function refreshStatusUI_() {
  const sheet = getSheet1();
  const enabled = isFeedbackEnabled();

  sheet.getRange(STATUS_CELL)
    .setBackground(enabled ? '#34a853' : '#ea4335')
    .setFontColor('#ffffff')
    .setFontWeight('bold')
    .setHorizontalAlignment('center')
    .setVerticalAlignment('middle')
    .setValue(enabled);

  sheet.getRange('B3').setValue(new Date());
}

// ─── Web app endpoints ────────────────────────────────────────────────────────

function doPost(e) {
  try {
    if (!isFeedbackEnabled()) {
      return ContentService
        .createTextOutput(JSON.stringify({
          success: false,
          disabled: true,
          message: 'Feedback collection is currently disabled by the administrator.'
        }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    const sheet = getSheet1();
    const data = getPostFields_(e);

    var attResult = { rich: null, plain: '' };
    if (data.attachments && String(data.attachments).trim() !== '') {
      attResult = saveAttachmentsToDrive_(data.attachments);
    }

    sheet.appendRow([
      new Date(),
      data.type || '',
      data.rating || '',
      data.message || '',
      data.email || '',
      data.language || '',
      data.version || '',
      ''
    ]);

    var row = sheet.getLastRow();
    var attCell = sheet.getRange(row, 8);
    if (attResult.rich) {
      attCell.setRichTextValue(attResult.rich);
      attCell.setWrap(true);
    } else if (attResult.plain) {
      attCell.setValue(attResult.plain);
      attCell.setWrap(true);
    }

    return ContentService
      .createTextOutput(JSON.stringify({ success: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ success: false, error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet() {
  return ContentService
    .createTextOutput(JSON.stringify({
      status: 'ok',
      feedbackEnabled: isFeedbackEnabled()
    }))
    .setMimeType(ContentService.MimeType.JSON);
}
