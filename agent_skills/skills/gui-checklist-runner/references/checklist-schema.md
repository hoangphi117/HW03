# Checklist Row Schema

Every checklist row **must** contain exactly these columns in the Excel sheet
and in Markdown tables. Do not add or remove columns without updating this file.

## Column Definitions

| Column Name | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| `ID` | String | ✅ | Unique item ID: `<FR_CODE>-<IA_CODE>-<SEQ>` e.g. `FR05-IA01-001` |
| `Screen` | String | ✅ | Human-readable screen name matching the FR code |
| `FR_Code` | String | ✅ | Functional Requirement code e.g. `FR-05` |
| `Aspect` | Enum | ✅ | One of: `IA-01`, `IA-02`, `IA-03`, `IA-04` |
| `Category` | String | ✅ | Sub-category label e.g. "Typography", "Form Validation", "Breadcrumbs", "Loading State" |
| `Check_Description` | String | ✅ | Imperative sentence: what to verify. ≤ 120 characters. |
| `Steps_to_Test` | String | ✅ | Numbered steps to reproduce the check scenario |
| `Expected_Result` | String | ✅ | Observable, unambiguous expected outcome |
| `Status` | Enum | ✅ | `Passed` / `Failed` / `N/A` — filled during execution |
| `Notes` | String | ❌ | Mandatory when Status = `Failed`. Actual observed behavior. |
| `Issue_URL` | URL | ❌ | GitHub Issue URL — mandatory when Status = `Failed` |
| `Source` | Enum | ✅ | `AI` = AI-generated \| `HUMAN` = human-curated |
| `Why_AI_Missed` | Enum | ❌ | Mandatory when Source = `HUMAN`. One of: `LOCALE`, `EDGE_CASE`, `PLATFORM`, `CONTEXT`, `PROMPT_GAP` |
| `Screenshot` | String | ❌ | Relative path to screenshot — mandatory when Status = `Failed` |

## ID Format Rules

- `FR_CODE`: Two-digit zero-padded FR number → `FR05`, `FR06`, `FR07`, `FR08`, `FR09`, `FR11`
- `IA_CODE`: `IA01`, `IA02`, `IA03`, `IA04`
- `SEQ`: Three-digit zero-padded sequence within that FR + IA group → `001`, `002`

**Example:** `FR05-IA02-001` = First form check on the Product Listing screen.

## Excel Sheet Structure

| Sheet Name | Contents |
| :--- | :--- |
| `Checklist` | All checklist items using the schema above |
| `Test_Summary` | Aggregated counts: Total, Passed, Failed, N/A, Bugs Filed, AI count, Human count |
| `Bug_Log` | Flattened list of Failed items with Issue URL and screenshot path |

