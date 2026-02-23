/**
 * BhaashaBuddy Feedback - Google Apps Script
 * 
 * SETUP:
 * 1. Open your Google Sheet: https://docs.google.com/spreadsheets/d/1a8vppsvQ21QGuoTG3vSSlRA27xqLNsOUMatlHqMUHHI/
 * 2. Extensions → Apps Script
 * 3. Replace any code with this script
 * 4. Click Deploy → New deployment → Type: Web app
 * 5. Execute as: Me | Who has access: Anyone
 * 6. Deploy and copy the Web app URL
 * 7. Paste the URL into app.js as FEEDBACK_SHEET_URL
 * 
 * The sheet will receive columns: Timestamp, Type, Rating, Message, Email, Language, Version
 */

const SHEET_ID = '1a8vppsvQ21QGuoTG3vSSlRA27xqLNsOUMatlHqMUHHI';

function getFeedbackSheet() {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  const feedbackTab = ss.getSheetByName('Feedback');
  return feedbackTab || ss.getSheets()[0];
}

function parseFormData(str) {
  const out = {};
  if (!str) return out;
  str.split('&').forEach(function(pair) {
    const i = pair.indexOf('=');
    if (i > 0) {
      const k = decodeURIComponent(pair.substring(0, i).replace(/\+/g, ' '));
      const v = decodeURIComponent((pair.substring(i + 1) || '').replace(/\+/g, ' '));
      out[k] = v;
    }
  });
  return out;
}

function doPost(e) {
  try {
    const sheet = getFeedbackSheet();
    let data = {};
    if (e.postData) {
      const ct = (e.postData.type || '').toLowerCase();
      const raw = e.postData.contents || '';
      if (ct.indexOf('json') >= 0) {
        data = JSON.parse(raw);
      } else {
        data = parseFormData(raw);
      }
    }

    const timestamp = new Date();
    const type = data.type || '';
    const rating = data.rating || '';
    const message = data.message || '';
    const email = data.email || '';
    const language = data.language || '';
    const version = data.version || '';
    
    // Add headers if sheet is empty
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(['Timestamp', 'Type', 'Rating', 'Message', 'Email', 'Language', 'Version']);
    }
    
    sheet.appendRow([timestamp, type, rating, message, email, language, version]);
    
    return ContentService
      .createTextOutput(JSON.stringify({ success: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ success: false, error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
