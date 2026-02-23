# Connect BhaashaBuddy Feedback to Google Sheet

Feedback from the app is sent to your Google Sheet. Follow these steps:

## 1. Open your sheet
https://docs.google.com/spreadsheets/d/1a8vppsvQ21QGuoTG3vSSlRA27xqLNsOUMatlHqMUHHI/edit

**Important:** The script must be added from this same sheet (Extensions → Apps Script).

## 2. Add the script
- **Extensions** → **Apps Script**
- Delete any existing code
- Copy the contents of `Code.gs` and paste it
- Click **Save** (Ctrl+S)

## 3. Deploy as Web App
- Click **Deploy** → **New deployment**
- Click the gear icon → **Web app**
- **Description:** BhaashaBuddy Feedback
- **Execute as:** Me
- **Who has access:** Anyone
- Click **Deploy**
- **Authorize** when prompted (choose your Google account)
- Copy the **Web app URL** (looks like `https://script.google.com/macros/s/.../exec`)

## 4. Add URL to the app
- Open `app.js`
- Find `const FEEDBACK_SHEET_URL = '';`
- Paste your Web app URL between the quotes

## Where does data go?
- If you have a sheet tab named **Feedback**, data goes there.
- Otherwise, data goes to the **first tab** (Sheet1).

## Sheet columns
The script adds a header row and then appends:
| Timestamp | Type | Rating | Message | Email | Language | Version |
