---
name: gui-checklist-runner
description: >
  Generate, review, and execute a GUI usability checklist for any screen or
  user flow in a web application. Use when you need to produce a structured
  set of interface quality checks covering General UI standards, Forms,
  Navigation, and Feedback/State across one or more screens, then record
  Pass/Fail execution results and bug evidence. Reusable across testing tasks.
risk: low
source: custom
version: 1.0.0
---

# GUI Checklist Runner

**Purpose:** Generate a reusable, structured GUI checklist covering 4 interface
aspects (IA-01 → IA-04) for any given screen or user flow, then guide the
tester through execution and bug logging.

**Trigger phrases (examples):**
- "build a GUI checklist for [screen/flow]"
- "run GUI testing on [feature]"
- "generate interface quality checks for [flow]"
- "kiểm thử giao diện màn hình [tên màn hình]"

---

## Inputs Required

Before starting, collect:

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `FLOW_NAME` | Human-readable name of the flow | "Search to Checkout" |
| `SCREENS` | Ordered list of FR codes + screen names | `FR-05 Product Listing, FR-06 Product Detail` |
| `SUT_URL` | Base URL of the system under test | `http://localhost:3000` |
| `STUDENT_ID` | Watermark ID for failed screenshots | `25127001` |
| `TARGET_COUNT` | Minimum checklist items to generate | `40` (required minimum per HW03) |

---

## Step 1 — Generate Checklist (AI Phase)

For each screen in `SCREENS`, generate checklist items across all 4 interface
aspects. Output every item using **exactly** the row schema defined in
`references/checklist-schema.md`.

**Interface Aspect Coverage Rules:**
- `IA-01 General UI`: Typography hierarchy, brand color consistency, spacing
  grid (8 px), contrast ratio ≥ 4.5:1 (WCAG AA), responsive breakpoints.
- `IA-02 Forms`: Label presence, placeholder text, real-time validation, error
  helper text, focus/disabled/readonly states, format constraints (phone VN,
  email, currency VND).
- `IA-03 Navigation`: Breadcrumbs, back/cancel links, CTA button routing,
  cross-step progress indicators, pagination / infinite-scroll controls.
- `IA-04 Feedback / State`: Loading spinners / skeleton screens, toast/snackbar
  notifications, empty states (zero results, empty cart), modal confirmation
  dialogs, error boundary fallbacks.

**Distribution target (adjust proportionally to `TARGET_COUNT`):**

| Aspect | Min % | Characteristic screens |
| :--- | :---: | :--- |
| IA-01 General UI | 20% | All screens |
| IA-02 Forms | 25% | Search, Checkout, Coupon input |
| IA-03 Navigation | 25% | Listing, Cart, Order History |
| IA-04 Feedback | 30% | Cart, Coupon, Checkout, Order History |

**Output:** Draft checklist table in Markdown, then immediately export to
`checklists/HW03_GUI_Checklist.xlsx` using the schema in
`references/checklist-schema.md`.

Log this AI generation step in `reports/AI_Audit_Report.md`:
- Tool name, date/time, exact prompt used, raw AI output summary.

---

## Step 2 — Human Critical Review (Extension Phase)

After AI generation:

1. Read through every generated item and flag duplicates or vague descriptions.
2. Identify **edge cases AI typically misses** (use `references/ai-blindspots.md`
   as a reference checklist).
3. Add at minimum **5 human-curated items** per flow.
4. For each added item, fill the `why_ai_missed` column with one of:
   - `LOCALE` — locale-specific rule (VN phone format, VND display, diacritics)
   - `EDGE_CASE` — boundary condition (empty cart, expired coupon, 0 results)
   - `PLATFORM` — platform-specific behavior (mobile viewport, iOS Safari)
   - `CONTEXT` — implicit business rule not stated in FR specs
   - `PROMPT_GAP` — the prompt did not cover this area

5. Git commit: `"feat(checklist): review and extend AI checklist with human-curated items"`

---

## Step 3 — Execute Checklist on SUT

For each checklist item:

1. Navigate to the relevant screen on `SUT_URL`.
2. Perform the described check.
3. Record result in the `Status` column: `Passed` | `Failed` | `N/A`.
4. For `Failed` items:
   - Write a concise note in the `Notes` column (what was observed vs expected).
   - Capture a screenshot following the protocol in `references/screenshot-protocol.md`.
   - Save to `evidence/bug_screenshots/<FR_CODE>_<ITEM_ID>_fail.png`.

5. Git commit after completing each FR screen:
   `"test(gui): execute checklist for <SCREEN_NAME> – X passed, Y failed"`

---

## Step 4 — Bug Report & GitHub Issues

For every `Failed` item:

1. Create a GitHub Issue using the template in `references/bug-report-template.md`.
2. Include: Title, Steps to Reproduce, Expected Result, Actual Result, Screenshot
   link, Severity label.
3. Record the issue URL in the `Issue_URL` column of the checklist Excel.
4. Update `reports/Bug_Report.md` with the aggregated issue list.

Git commit: `"docs(bugs): log all GUI bug reports to GitHub Issues"`

---

## Step 5 — Generate Test Summary

Compute and write to `README.md` (Test Summary section):

```
Total Items     : <n>
Passed          : <n> (<pct>%)
Failed          : <n> (<pct>%)
N/A             : <n>
Bugs Filed      : <n>
AI Generated    : <n>
Human Added     : <n>
```

Export updated `git_commit_log.txt` by running:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\export_git_log.ps1
```

---

## Output Checklist (Definition of Done)

- [ ] Checklist has ≥ `TARGET_COUNT` unique, non-duplicate items
- [ ] All 4 IA aspects covered on every screen
- [ ] Every `Failed` item has screenshot in `evidence/bug_screenshots/`
- [ ] Every `Failed` item has a GitHub Issue URL in the Excel file
- [ ] `AI_Audit_Report.md` updated with this run's prompt + output
- [ ] Git log has ≥ 4 commits (generate → review → execute → bug-report)
- [ ] `git_commit_log.txt` is current
- [ ] `README.md` Test Summary is updated

---

## When NOT to Use This Skill

- Do not use for backend API or logic testing (use an API testing skill instead).
- Do not use if the target SUT is not running / accessible at `SUT_URL`.
- Do not use as a replacement for automated regression tests (Playwright/Selenium).

