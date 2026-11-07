# Bug Report Template

Use this template to create each GitHub Issue for a failed checklist item.

---

## Issue Title Format

```
[GUI Bug][<FR_CODE>][<ASPECT>] <Short description of defect>
```

**Example:**

```
[GUI Bug][FR-09][IA-02] Coupon expired error message is too generic
```

---

## Issue Body Template

```markdown
## Bug Summary

**Checklist Item ID:** FR09-IA02-001  
**Screen / Flow:** FR-09 — Discount Coupon Input  
**Interface Aspect:** IA-02 (Forms)  
**Severity:** Medium <!-- Critical / High / Medium / Low -->
**Found by:** [StudentID] [Full Name]  
**Date Found:** YYYY-MM-DD

---

## Steps to Reproduce

1. Navigate to `http://localhost:3000/cart`
2. Enter an expired coupon code (e.g., `SAVE10EXPIRED`) in the coupon field
3. Click "Áp dụng" button

---

## Expected Result

System shows specific error message: **"Mã giảm giá đã hết hạn"**

---

## Actual Result

System shows generic error message: **"Mã giảm giá không hợp lệ"** — no
distinction between expired, invalid, or already-used coupons.

---

## Evidence

![Screenshot](<relative path to screenshot>)

**Browser:** Chrome 120 | **OS:** Windows 11 | **Resolution:** 1920×1080

---

## Additional Notes

- Checklist Source: `AI` / `HUMAN`
- Why AI Missed (if human-added): `EDGE_CASE` — AI did not differentiate error subtypes
```

---

## Severity Definitions

| Severity     | Definition                                                        |
| :----------- | :---------------------------------------------------------------- |
| **Critical** | Feature completely broken; no workaround; blocks user flow        |
| **High**     | Significant usability issue; workaround exists but is non-obvious |
| **Medium**   | Noticeable issue; workaround available; impacts UX quality        |
| **Low**      | Minor cosmetic issue; no impact on functionality                  |

## GitHub Labels to Apply

Apply these labels when creating the issue:

- `gui-bug` — always
- `task1` — always (for HW03 Task 1 traceability)
- `severity:critical` / `severity:high` / `severity:medium` / `severity:low`
- `IA-01` / `IA-02` / `IA-03` / `IA-04` — matching the aspect
- `FR-05` through `FR-11` — matching the screen
