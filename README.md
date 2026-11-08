# HW03 — GUI và Usability Testing

- Mã số sinh viên: 23120320  
- Họ và tên: Phi  
- Email: 23120320@student.hcmus.edu.vn  
- Môn học: Kiểm thử phần mềm — FIT HCMUS  
- Hệ thống SUT: EShop — https://github.com/ttbhanh/eshop-sut  
- Luồng kiểm thử: FR-05 Search và Listing đến FR-06 Product Detail đến FR-07 Cart đến FR-09 Coupons đến FR-08 Checkout đến FR-11 Order History

---

## 1. Báo cáo Tổng kết Kiểm thử — Test Summary Report

| Chỉ số | Giá trị |
| :--- | :--- |
| Số màn hình và luồng kiểm thử | 6 màn hình xuyên suốt 1 luồng người dùng hoàn chỉnh |
| Số lượng ca kiểm thử checklist thiết kế | 42 ca kiểm thử, vượt quy định tối thiểu 40 ca |
| Số lượng ca kiểm thử checklist thực thi | 42 trên 42 ca kiểm thử, đạt 100 phần trăm |
| Số lượng ca kiểm thử đạt | 20 ca kiểm thử, chiếm 47.6 phần trăm |
| Số lượng ca kiểm thử không đạt | 22 ca kiểm thử, chiếm 52.4 phần trăm |
| Số lượng lỗi phát hiện | 22 lỗi thực tế, đã tạo GitHub Issues từ số 1 đến số 23 |
| Số ảnh chụp màn hình bằng chứng lỗi | 25 ảnh trên 22 ca lỗi bao gồm cả chuỗi hành động liên tiếp |
| Số người tham gia đánh giá Usability | 7 người tham gia thật ngoài ngành với email xác thực |
| Điểm số SUS trung bình | 62.14 trên 100 điểm, Hạng F, mức Poor |
| Tỷ lệ hoàn thành nhiệm vụ Usability | 71.4 phần trăm, 5 người hoàn thành và 2 người thất bại |
| Số nền tảng kiểm thử tương thích | 3 nền tảng gồm Desktop Chrome, Desktop Firefox, Mobile Browser |
| Số ảnh bằng chứng đa nền tảng | 15 ảnh chụp màn hình có watermark thông tin sinh viên |
| Liên kết video minh họa | Đính kèm trong hồ sơ nộp bài |

---

## 2. Bảng Tự Đánh giá Kết quả — Self-Assessment Table

| STT | Tiêu chí Đánh giá | Điểm Tối đa | Điểm Tự đánh giá | Giải trình Minh chứng |
| :---: | :--- | :---: | :---: | :--- |
| 1 | Nhiệm vụ một — GUI Checklist | 30 | 30 | Thiết kế 42 ca kiểm thử bao phủ đủ bốn khía cạnh, thực thi 100 phần trăm trên SUT thật, chụp 25 ảnh bằng chứng và lập 22 GitHub Issues liên kết |
| 2 | Nhiệm vụ hai — Usability Evaluation | 40 | 40 | Kịch bản mục tiêu thực tế, đánh giá bảy người thật ngoài ngành với email xác thực, phân tích điểm SUS 62.14 và lập báo cáo chuyên sâu |
| 3 | Nhiệm vụ ba — Cross-Browser và Cross-Platform | 20 | 20 | Thực thi trên ba nền tảng Chrome, Firefox, Mobile Browser, thu thập 15 ảnh bằng chứng có watermark sinh viên và lập ma trận tương thích |
| 4 | Kỹ năng Agent Skills | 10 | 10 | Xây dựng hai kỹ năng hoàn chỉnh tái sử dụng được gồm gui-checklist-runner và usability-evaluator kèm hướng dẫn sử dụng và lược đồ tham chiếu |
| Tổng | Toàn bộ Đồ án | 100 | 100 | Hoàn thành trọn vẹn toàn bộ các yêu cầu của bài tập lớn |

---

## 3. Cấu trúc Thư mục Dự án

- agent_skills: Mã nguồn hai kỹ năng tái sử dụng cho agent kiểm thử
- checklists:
  - HW03_GUI_Checklist.xlsx: File Excel checklist chuẩn gồm 3 sheets Checklist 42 items, Test_Summary, Bug_Log 22 lỗi có link GitHub
  - gui_checklist.md: Bảng Markdown checklist đầy đủ phục vụ tra cứu
- cross_platform:
  - desktop_chrome: Chứa 5 ảnh chụp màn hình kiểm thử trên Google Chrome
  - desktop_firefox: Chứa 5 ảnh chụp màn hình kiểm thử trên Mozilla Firefox
  - mobile_or_safari: Chứa 5 ảnh chụp màn hình kiểm thử trên Mobile Browser
- evidence/bug_screenshots: 25 ảnh chụp màn hình chứng minh 22 ca lỗi phát hiện được
- usability:
  - participants.md: Danh sách bảy người tham gia thật với email xác thực
  - raw_responses.csv: Dữ liệu phản hồi khảo sát gốc của bảy người tham gia
  - session_notes: 7 file nhật ký quan sát cá nhân từ session_P-01 đến session_P-07
  - survey_instruments: Kịch bản nhiệm vụ và bộ câu hỏi SUS chuẩn hóa
  - survey_responses: File Excel kết quả sus_results.xlsx và sus_results.md
- reports:
  - Main_Report.md: Báo cáo tổng thể tích hợp toàn bộ đồ án nộp bài
  - Bug_Report.md: Báo cáo chi tiết 22 lỗi phát hiện trên SUT
  - Usability_Report.md: Báo cáo đánh giá trải nghiệm người dùng chuyên sâu
  - Cross_Platform_Report.md: Báo cáo ma trận kiểm thử tương thích đa nền tảng
  - AI_Critique.md: Đoạn văn phản biện trí tuệ nhân tạo bắt buộc
  - AI_Audit_Report.md: Nhật ký sử dụng trí tuệ nhân tạo bắt buộc
- scripts: Các mã nguồn kịch bản tự động hóa kiểm thử và xử lý số liệu
