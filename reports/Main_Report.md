# Báo cáo Tổng thể Đồ án HW03 — GUI và Usability Testing

## Thông tin Chung

- Tên bài tập: Bài tập lớn HW03 — GUI và Usability Testing
- Mã bài tập: HW03-AI
- Sinh viên thực hiện: Phi
- Mã số sinh viên: 23120320
- Email sinh viên: 23120320@student.hcmus.edu.vn
- Môn học: Kiểm thử Phần mềm
- Hệ thống kiểm thử: Ứng dụng thương mại điện tử EShop
- Luồng nghiệp vụ lựa chọn: Tìm kiếm sản phẩm qua FR-05, Xem chi tiết sản phẩm qua FR-06, Quản lý giỏ hàng qua FR-07, Áp dụng mã giảm giá qua FR-09, Thanh toán đơn hàng qua FR-08, Kiểm tra lịch sử đơn hàng qua FR-11

---

## 1. Phần một — Thiết kế và Thực thi GUI Checklist

### 1.1. Mục tiêu và Phương pháp luận
Nhiệm vụ thứ nhất tập trung xây dựng bộ danh mục kiểm thử giao diện bao phủ toàn diện bốn khía cạnh giao diện chuẩn mực bao gồm: tiêu chuẩn giao diện chung IA-01, biểu mẫu nhập liệu IA-02, điều hướng luồng người dùng IA-03, và phản hồi trạng thái hệ thống IA-04.

Quy trình kết hợp giữa việc sử dụng trí tuệ nhân tạo để sinh tập kiểm thử ban đầu và sự rà soát kỹ lưỡng của con người nhằm bổ sung các trường hợp biên, các yếu tố bản địa hóa và các khiếm khuyết ngữ cảnh thực tế.

### 1.2. Thống kê Kết quả Thực thi
- Tổng số lượng ca kiểm thử được thiết kế: 42 ca kiểm thử, vượt yêu cầu tối thiểu 40 ca của môn học
- Tỷ lệ phân bổ theo bốn khía cạnh giao diện:
  - Khía cạnh Tiêu chuẩn giao diện chung IA-01: 11 ca kiểm thử
  - Khía cạnh Biểu mẫu nhập liệu IA-02: 11 ca kiểm thử
  - Khía cạnh Điều hướng luồng IA-03: 11 ca kiểm thử
  - Khía cạnh Phản hồi trạng thái IA-04: 9 ca kiểm thử
- Kết quả kiểm thử thực tế trên hệ thống SUT:
  - Số lượng ca kiểm thử đạt: 20 ca kiểm thử, chiếm tỷ lệ 47.6 phần trăm
  - Số lượng ca kiểm thử không đạt: 22 ca kiểm thử, chiếm tỷ lệ 52.4 phần trăm
  - Tổng số lỗi phát hiện: 22 lỗi thực tế

### 1.3. Tổng hợp các Lỗi Giao diện Trọng yếu
Toàn bộ 22 lỗi phát hiện đã được lập thành các GitHub Issues độc lập trên kho lưu trữ mã nguồn và liên kết đầy đủ vào file bảng tính Excel:
- Lỗi trường tổng tiền thanh toán cho phép người dùng tự do nhập sửa số tiền tùy ý
- Lỗi thuật toán tính mã giảm giá phần trăm làm giá trị thanh toán tăng vọt thay vì giảm giá
- Lỗi nút Thêm vào giỏ hàng nuốt lượt click đầu tiên của người dùng
- Lỗi giỏ hàng không tự làm trống sau khi đặt hàng thành công
- Lỗi biểu thức chính quy từ chối số điện thoại di động Việt Nam bắt đầu bằng số không
- Lỗi thiếu hoàn toàn biểu mẫu nhập địa chỉ nhận hàng chi tiết khi thanh toán

---

## 2. Phần hai — Đánh giá Trải nghiệm Người dùng

### 2.1. Thiết lập Kịch bản Nhiệm vụ
Kịch bản được xây dựng theo định hướng mục tiêu thực tế: Người dùng đóng vai trò khách hàng cần tìm mua một chiếc điện thoại thông minh với ngân sách dưới hai mươi triệu đồng, tìm kiếm mã giảm giá có sẵn để tiết kiệm chi phí, tiến hành đặt hàng và kiểm tra lại lịch sử giao dịch. Điều phối viên tuân thủ nguyên tắc quan sát trung lập và hướng dẫn người dùng nói to suy nghĩ trong suốt phiên kiểm thử.

### 2.2. Danh sách Bảy Người tham gia Thực tế
Bảy người tham gia đều là người thật ngoài ngành công nghệ thông tin và cung cấp thông tin liên hệ xác thực phục vụ việc kiểm tra ngẫu nhiên:
- Người thứ nhất: Nguyễn Yến Nhi, email yennhifab@gmail.com, 21 tuổi, Nữ, Sinh viên, thiết bị Laptop Windows 11 Chrome 124, thời gian 13 phút, kết quả thất bại do đơn hàng bị nhân đôi
- Người thứ hai: Trần Trọng Quân, email trantrongquan052@gmail.com, 21 tuổi, Nam, Sinh viên, thiết bị Desktop PC Windows 10 Chrome 124, thời gian 10 phút, kết quả hoàn thành
- Người thứ ba: Phạm Gia Bảo, email phambao0364@gmail.com, 21 tuổi, Nam, Sinh viên, thiết bị Laptop ASUS Windows 11 Chrome 124, thời gian 3 phút, kết quả hoàn thành
- Người thứ tư: Hoàng Minh Vũ, email vu97694@gmail.com, 21 tuổi, Nam, Nhân viên kinh doanh, thiết bị Laptop Lenovo Windows 11 Edge 124, thời gian 6 phút, kết quả thất bại do sai lệch thông tin và giá tiền
- Người thứ năm: Nguyễn Mạnh Hiền, email manhhien12a1@gmail.com, 21 tuổi, Nam, Sinh viên, thiết bị Laptop Dell Windows 10 Chrome 124, thời gian 6.9 phút, kết quả hoàn thành
- Người thứ sáu: Trần Thượng Tuyên, email jacktr1104@gmail.com, 22 tuổi, Nam, Nhân viên thiết kế, thiết bị MacBook macOS 14 Chrome 124, thời gian 9.9 phút, kết quả hoàn thành
- Người thứ bảy: Nguyễn Thanh Phương, email nguyenthanhphuong221105@gmail.com, 21 tuổi, Nam, Sinh viên, thiết bị Laptop HP Windows 11 Chrome 124, thời gian 5.2 phút, kết quả hoàn thành

### 2.3. Phân tích Định lượng Thang đo SUS
- Điểm số SUS trung bình: 62.14 trên thang điểm 100
- Độ lệch chuẩn: 18.78
- Điểm thấp nhất đạt 32.5 điểm và điểm cao nhất đạt 90.0 điểm
- Xếp hạng theo thang Sauro-Lewis: Hạng F
- Đánh giá theo thang tính từ Bangor: Mức Poor
- Tỷ lệ hoàn thành nhiệm vụ: 5 trên 7 người hoàn thành, đạt 71.4 phần trăm

### 2.4. Phân nhóm Điểm đau và Tách biệt Bản chất Lỗi
- Nhóm lỗi kỹ thuật cá biệt:
  - Lỗi thuật toán nhân chiết khấu ngược làm tăng tiền đơn hàng từ hai mươi tám triệu lên bảy trăm triệu đồng
  - Lỗi biến đếm chặn click đầu tiên trong mã nguồn giao diện giỏ hàng
  - Lỗi nhân đôi đơn hàng trong lịch sử giao dịch khi máy chủ nhận request trùng lặp
  - Lỗi biểu thức chính quy chặn đầu số không của điện thoại Việt Nam
- Nhóm vấn đề thiết kế hệ thống:
  - Thiếu hệ thống thông báo trạng thái trực quan xuyên suốt các màn hình
  - Lỗ hổng kiến trúc biểu mẫu cho phép sửa trường dữ liệu nhạy cảm
  - Mất đồng bộ trạng thái giữa giỏ hàng và đơn hàng sau thanh toán
  - Thiếu bước xác nhận tóm tắt giao dịch trước khi trừ tiền

---

## 3. Phần ba — Kiểm thử Tương thích Đa nền tảng

### 3.1. Phạm vi Môi trường Kiểm thử
Kiểm thử đa nền tảng được thực hiện trên ba môi trường độc lập:
- Môi trường máy tính Google Chrome 124
- Môi trường máy tính Mozilla Firefox 125
- Môi trường điện thoại di động Mobile Browser

Mỗi môi trường đều được thu thập đầy đủ năm ảnh chụp màn hình ghi nhận từng bước luồng mua hàng và hiển thị thanh định danh sinh viên 23120320@student.hcmus.edu.vn.

### 3.2. Đánh giá Khả năng Tương thích
- Giữa Chrome và Firefox: Khả năng dàn trang, hiển thị lưới sản phẩm và phông chữ đạt sự đồng nhất cao, không phát sinh lỗi lệch giao diện đặc thù.
- Giữa Máy tính và Di động: Giao diện di động đáp ứng tốt việc thu nhỏ hình ảnh và ngắt dòng văn bản. Tuy nhiên, các bảng biểu giỏ hàng và lịch sử đơn hàng phát sinh thanh cuộn ngang do không được thiết kế responsive dạng thẻ cho màn hình hẹp.

---

## 4. Phần bốn — Xây dựng Kỹ năng Tự động hóa Agent Skills

Đồ án đã xây dựng hai kỹ năng tự động hóa chuyên biệt:
- Kỹ năng thứ nhất gui-checklist-runner: Hỗ trợ tự động hóa toàn bộ quy trình năm bước từ phân tích mã nguồn SUT, sinh danh mục kiểm thử, đối chiếu điểm mù, xuất file Excel ba sheet và lập báo cáo lỗi.
- Kỹ năng thứ hai usability-evaluator: Hỗ trợ tự động hóa sáu bước quy trình đánh giá trải nghiệm người dùng từ thiết kế kịch bản, quản lý hồ sơ người tham gia, tính toán điểm số SUS chuẩn xác và xuất báo cáo phân tích chuyên sâu.

---

## 5. Bảng Tự Đánh giá Kết quả

| STT | Tiêu chí Đánh giá | Điểm Tối đa | Điểm Tự đánh giá | Giải trình Minh chứng |
| :---: | :--- | :---: | :---: | :--- |
| 1 | Nhiệm vụ một — GUI Checklist | 30 | 30 | Thiết kế 42 items đủ bốn khía cạnh, thực thi đầy đủ trên SUT thật, chụp 25 ảnh bằng chứng và lập 22 GitHub Issues liên kết |
| 2 | Nhiệm vụ hai — Usability Evaluation | 40 | 40 | Kịch bản mục tiêu thực tế, khảo sát bảy người dùng thật ngoài ngành với email xác thực, phân tích điểm SUS và lập báo cáo chuyên sâu |
| 3 | Nhiệm vụ ba — Cross-Browser và Cross-Platform | 20 | 20 | Kiểm thử trên ba nền tảng Chrome, Firefox và Mobile, chụp 15 ảnh bằng chứng có watermark sinh viên và lập ma trận tương thích |
| 4 | Kỹ năng Agent Skills | 10 | 10 | Xây dựng hai kỹ năng hoàn chỉnh tái sử dụng được kèm tài liệu hướng dẫn và các lược đồ tham chiếu chuẩn |
| Tổng | Toàn bộ Đồ án | 100 | 100 | Hoàn thành trọn vẹn toàn bộ các yêu cầu quy định trong đề bài |
