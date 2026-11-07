# Agent Skills — HW03

Thư mục này chứa 2 Agent Skills có thể tái sử dụng cho bất kỳ màn hình hay
luồng kiểm thử nào trong tương lai.

## Skills Available

| Skill | Thư mục | Mục đích |
|:---|:---|:---|
| **gui-checklist-runner** | `skills/gui-checklist-runner/` | Sinh checklist GUI, review, thực thi, và log bug |
| **usability-evaluator** | `skills/usability-evaluator/` | Thiết kế kịch bản, tổ chức 7 session SUS/UEQ-S, phân tích kết quả |

## Cách sử dụng

Xem chi tiết trong [`USAGE_GUIDE.md`](USAGE_GUIDE.md).

## Cấu trúc thư mục

```
agent_skills/
├── USAGE_GUIDE.md                           ← Hướng dẫn sử dụng (đọc trước)
├── skills/
│   ├── gui-checklist-runner/
│   │   ├── SKILL.md                         ← Entry point của skill
│   │   └── references/
│   │       ├── checklist-schema.md          ← Schema cột Excel bắt buộc
│   │       ├── ai-blindspots.md             ← 25 edge case AI thường bỏ sót
│   │       ├── screenshot-protocol.md       ← Quy trình chụp ảnh lỗi
│   │       └── bug-report-template.md       ← Template GitHub Issue
│   └── usability-evaluator/
│       ├── SKILL.md                         ← Entry point của skill
│       └── references/
│           ├── scenario-template.md         ← Template kịch bản task
│           ├── sus-questionnaire.md         ← Bảng SUS 10 câu (EN + VI)
│           ├── session-notes-template.md    ← Template ghi chú phiên
│           ├── scoring-guide.md             ← Công thức tính điểm SUS & UEQ-S
│           └── participant-schema.md        ← Schema bảng người tham gia
└── demo_links.md                            ← Link video demo skill
```

