# Screenshot Protocol

Follow this protocol for every checklist item with `Status = Failed`.

## Naming Convention

```
evidence/bug_screenshots/<FR_CODE>_<ITEM_ID>_fail.<ext>
```

**Examples:**
- `evidence/bug_screenshots/FR07_FR07-IA04-002_fail.png`
- `evidence/bug_screenshots/FR09_FR09-IA02-001_fail.png`

## Required Elements in Every Screenshot

Each screenshot **must visibly contain**:

1. **Browser URL bar** showing `localhost` (or the SUT domain) — proves the
   test ran on the actual SUT, not a mockup.
2. **Student ID watermark** — white or yellow text overlay in one corner
   containing: `<StudentID> | <Full Name>`.
3. **The defect itself** — the UI element/state that failed the check,
   clearly visible (use a red rectangle annotation if needed).
4. **Date/Time stamp** — system clock or screenshot metadata.

## Watermark Tool Options

**Option A — Python (scripts/watermark_helper.py):**
```bash
python scripts/watermark_helper.py --input "raw_screenshot.png" \
  --student-id "25127001" --name "Nguyen Van A" \
  --output "evidence/bug_screenshots/FR07_FR07-IA04-002_fail.png"
```

**Option B — Windows Snipping Tool + Paint:**
1. Take screenshot with Snipping Tool (Win + Shift + S).
2. Open in Paint → Insert a text box in the corner with your StudentID.
3. Save as PNG into the correct path.

**Option C — Browser DevTools:**
1. Open DevTools → Console tab → type: `document.title = "25127001 - Nguyen Van A"`
   to embed ID in page title, then take screenshot.

## Compression Rules

- Format: `.png` preferred; `.jpg` acceptable for photos.
- Maximum file size: **2 MB** per screenshot.
- Minimum resolution: **1280 × 720 px**.
- Do not crop out the browser chrome / URL bar.

