# Hướng Dẫn Sử Dụng Agent Skills — HW03

## Tổng quan

Hai agent skills trong repo này được thiết kế để **tái sử dụng** trên bất kỳ
màn hình hoặc luồng người dùng mới nào trong tương lai, không chỉ cho HW03.

---

## Skill 1: `gui-checklist-runner`

### Khi nào dùng?

Mỗi khi bạn cần kiểm tra giao diện của một màn hình / luồng người dùng mới.

### Cách invoke (gõ vào chat với AI agent):

```
Hãy dùng skill gui-checklist-runner để kiểm tra luồng [tên luồng].

Inputs:
- FLOW_NAME: "Quản lý sản phẩm Admin"
- SCREENS: "FR-01 Admin Login, FR-02 Product Create, FR-03 Product Edit"
- SUT_URL: "http://localhost:3000"
- STUDENT_ID: "25127001"
- TARGET_COUNT: 40
```

### Workflow gồm 5 bước:

```
Bước 1: AI sinh checklist ban đầu (~35-40 items)
         ↓
Bước 2: Bạn review + thêm edge case từ ai-blindspots.md
         ↓
Bước 3: Thực thi trên SUT → đánh dấu Passed/Failed
         ↓
Bước 4: Chụp ảnh lỗi theo screenshot-protocol.md
         ↓
Bước 5: Tạo GitHub Issues + cập nhật Test Summary
```

### Files được tạo ra tự động:

- `checklists/HW03_GUI_Checklist.xlsx` (> 40 items)
- `evidence/bug_screenshots/` (ảnh các item Failed có watermark)
- `reports/Bug_Report.md`
- `reports/AI_Audit_Report.md` (cập nhật thêm log)

### Tái sử dụng cho flow mới:

Chỉ cần thay đổi `FLOW_NAME` và `SCREENS`. Tất cả schema, template và
quy trình đều giữ nguyên.

---

## Skill 2: `usability-evaluator`

### Khi nào dùng?

Mỗi khi bạn cần đánh giá usability với người dùng thực.

### Cách invoke:

```
Hãy dùng skill usability-evaluator để đánh giá usability.

Inputs:
- FLOW_NAME: "Luồng mua hàng từ tìm kiếm đến lịch sử đơn hàng"
- TASK_GOAL: "Tìm sản phẩm, áp mã giảm giá, và hoàn thành đơn hàng"
- SUT_URL: "http://localhost:3000"
- PARTICIPANT_COUNT: 7
- SCALE: "SUS"
- STUDENT_ID: "25127001"
```

### Workflow gồm 6 bước:

```
Bước 1: Thiết kế kịch bản task (goal-based, không có step-by-step)
         ↓
Bước 2: Lập danh sách 7 người tham gia (đủ độ đa dạng)
         ↓
Bước 3: Chuẩn bị bảng SUS 10 câu + câu hỏi probe
         ↓
Bước 4: Tiến hành 7 phiên (think-aloud + ghi âm/quay màn hình)
         ↓
Bước 5: Tính điểm SUS (công thức trong scoring-guide.md)
         ↓
Bước 6: Viết báo cáo tổng hợp vào reports/Main_Report.md
```

### Files được tạo ra:

- `usability/task_scenario.md` (kịch bản chuẩn hóa)
- `usability/participants.md` (bảng có mask SĐT)
- `usability/session_notes/session_01.md` đến `session_07.md`
- `usability/survey_responses/analysis_summary.md` (điểm SUS + phân tích)

---

## Quy trình Git Commit bắt buộc (Regulation 12)

Mỗi bước trong skill cần 1 commit riêng biệt:

|          Bước          | Commit message mẫu                                                            |
| :--------------------: | :---------------------------------------------------------------------------- |
| Sinh checklist bằng AI | `feat(checklist): generate initial GUI checklist with AI`                     |
|  Review + thêm items   | `feat(checklist): review and extend with human-curated edge cases`            |
|     Thực thi FR-05     | `test(gui): execute checklist for FR-05 Product Listing – X passed, Y failed` |
| Thực thi FR-06..FR-11  | _(tương tự)_                                                                  |
|    Log bug reports     | `docs(bugs): log GUI bug reports to GitHub Issues`                            |
|   Thiết kế kịch bản    | `docs(usability): define task scenario for <FLOW_NAME>`                       |
|     Ghi chú phiên      | `test(usability): record session notes for participants 01-07`                |
|   Báo cáo usability    | `docs(usability): complete evaluation report`                                 |

Sau mỗi nhóm commit, chạy:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\export_git_log.ps1
```

---

## Tái sử dụng trong tương lai

Khi có flow mới (ví dụ: Task 2 của HW04), bạn chỉ cần:

1. Copy `checklists/HW03_GUI_Checklist.xlsx` → `checklists/HW04_GUI_Checklist.xlsx`
2. Invoke skill với `SCREENS` mới.
3. Toàn bộ schema, template, và quy trình giữ nguyên.
