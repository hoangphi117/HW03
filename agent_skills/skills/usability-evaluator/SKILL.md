---
name: usability-evaluator
description: >
  Prepare, facilitate, and analyze a usability evaluation session for a web
  application using SUS (System Usability Scale) and/or UEQ-S (User Experience
  Questionnaire Short). Use when you need to design task scenarios, recruit and
  brief participants, record think-aloud observations, calculate usability
  scores, and produce an evaluation report with actionable recommendations.
  Reusable for any number of screens, flows, and participant cohorts.
risk: low
source: custom
version: 1.0.0
---

# Usability Evaluator

**Purpose:** Orchestrate a complete usability evaluation lifecycle — from
scenario design through participant sessions to scored report — for any web
application screen or user flow.

**Trigger phrases (examples):**
- "run usability evaluation for [feature/flow]"
- "set up SUS study for [screen]"
- "evaluate usability with [n] participants"
- "đánh giá usability cho màn hình [tên màn hình]"
- "phân tích kết quả SUS/UEQ-S"

---

## Inputs Required

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `FLOW_NAME` | Flow being evaluated | "Search to Order History" |
| `TASK_GOAL` | One-sentence user goal | "Find a product and complete checkout" |
| `SUT_URL` | Base URL of SUT | `http://localhost:3000` |
| `PARTICIPANT_COUNT` | Number of real participants | `7` (minimum per HW03) |
| `SCALE` | Evaluation instrument | `SUS` / `UEQ-S` / `BOTH` |
| `STUDENT_ID` | For report headers and masking | `25127001` |

---

## Step 1 — Design Task Scenario

Write a goal-oriented task scenario using `references/scenario-template.md`.

Rules:
- One scenario per flow; must be **goal-based**, not **step-based**.
- Do NOT include navigation instructions (e.g., "click the Search button") —
  let participants discover the path.
- Include a realistic backstory/context to prime the participant.
- Define clear success criteria (observable completion state).

Output: `usability/task_scenario.md`

Git commit: `"docs(usability): define task scenario for <FLOW_NAME>"`

---

## Step 2 — Recruit and Log Participants

Fill the participant log at `usability/participants.md` using the schema in
`references/participant-schema.md`.

Privacy rules (mandatory):
- Display name: first name + masked last name initial only (e.g., "Nguyen T.").
- Phone/Zalo: mask the **middle 4 digits** → `090****789`.
- Do NOT store full CCCD/national ID numbers.
- Obtain verbal or written consent before each session.

Minimum participant profile diversity per HW03:
- At least 2 participants with limited e-commerce experience.
- At least 1 participant on a mobile device (phone or tablet).
- Age range ≥ 18 years; prefer mix of 18-25 and 26-40.

Output: `usability/participants.md`

---

## Step 3 — Prepare Evaluation Instruments

Based on `SCALE` input, generate the questionnaire(s):

### SUS (System Usability Scale) — 10 questions
Use the standard 10-item SUS questionnaire from
`references/sus-questionnaire.md`. Print or share digitally before each session.
Scoring: odd items → subtract 1; even items → subtract from 5; sum × 2.5.

### UEQ-S (User Experience Questionnaire Short) — 8 items
Use the 8 bi-polar adjective pairs from `references/ueq-s-questionnaire.md`.
Scoring: transform raw 1-7 scale to -3 to +3; average per dimension.

### Probe Questions (Post-task)
Generate 3-5 open-ended probe questions customized to `FLOW_NAME`.
Save in `usability/survey_instruments/probe_questions.md`.

---

## Step 4 — Conduct Sessions

For each participant session (Session 01 → `PARTICIPANT_COUNT`):

1. Brief participant: explain think-aloud protocol; confirm consent.
2. Start screen/audio recording — save link/file to `usability/recordings/`.
3. Assign the task scenario (read aloud or hand printed copy).
4. Observe silently; take timestamped notes using the template in
   `references/session-notes-template.md`. Save to
   `usability/session_notes/session_<NN>.md`.
5. After task completion (or failure), administer SUS/UEQ-S questionnaire.
6. Run probe questions; record answers verbatim.
7. Debrief participant; thank them.

Key observation metrics to record:
- Task completion: `Success` / `Partial` / `Failure`
- Time-on-task (seconds from task start to success/give-up)
- Number of navigation errors / wrong clicks
- Verbatim think-aloud quotes (top 3 per session)
- Emotional signals: confusion, frustration, delight

Git commit per session batch:
`"test(usability): record session notes for participants <range>"`

---

## Step 5 — Score and Analyze

After all sessions, compute scores using `references/scoring-guide.md`.

**SUS Analysis:**
- Calculate individual SUS score per participant.
- Compute mean, standard deviation, min, max.
- Map mean to adjective scale (Excellent ≥ 85.5 / Good 72.5-85.4 /
  OK 52.5-72.4 / Poor 38-52.4 / Awful < 38).
- Identify ≥ 3 usability problems with frequency count.

**UEQ-S Analysis (if applicable):**
- Compute mean per dimension: Pragmatic Quality (PQ) and Hedonic Quality (HQ).
- Benchmark against UEQ dataset (mean > 0.8 = good; > 1.5 = excellent).

**Qualitative synthesis:**
- Group think-aloud quotes by theme.
- Rank top 5 usability problems by severity (frequency × impact).
- Link each problem to the relevant checklist item ID from Task 1.

Output: `usability/survey_responses/analysis_summary.md`

---

## Step 6 — Write Evaluation Report

Populate `reports/Main_Report.md` usability section with:

1. **Executive Summary**: One paragraph with mean SUS score, adjective rating,
   and top 2 recommendations.
2. **Methodology**: Participants (count + masked table), scenario, instruments,
   session format, platform diversity.
3. **Results**: SUS table (one row per participant + summary row), UEQ-S chart
   (if applicable), task completion rate.
4. **Usability Problems**: Ranked table linking each problem to a checklist item
   and a recommended fix.
5. **Participant Quotes**: Select 3-5 impactful verbatim quotes.
6. **Recommendations**: Prioritized list of design improvements.

Git commit: `"docs(usability): complete evaluation report for <FLOW_NAME>"`

---

## Output Checklist (Definition of Done)

- [ ] Task scenario saved and goal-based (no step-by-step instructions)
- [ ] `participants.md` has ≥ `PARTICIPANT_COUNT` entries with privacy masking
- [ ] SUS/UEQ-S questionnaires saved in `usability/survey_instruments/`
- [ ] Session notes exist for every participant session
- [ ] Recording links logged in `usability/recordings/`
- [ ] SUS mean, SD, and adjective rating computed and documented
- [ ] ≥ 3 usability problems identified with frequency count
- [ ] Each usability problem linked to a GUI checklist item ID
- [ ] Evaluation report section complete in `reports/Main_Report.md`
- [ ] `git_commit_log.txt` updated

---

## When NOT to Use This Skill

- Do not use for automated performance or functional testing.
- Do not use if you cannot recruit real human participants
  (do not simulate fake participants or fabricate SUS scores).
- Do not use for accessibility audits (use WCAG audit tools instead).

