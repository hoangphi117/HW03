# Báo cáo Kiểm thử Tương thích Đa nền tảng — Task 3

## 1. Tổng quan Thực thi

Kiểm thử đa nền tảng được tiến hành nhằm xác định tính nhất quán về giao diện, bố cục và hành vi chức năng của hệ thống EShop trên các môi trường duyệt web khác nhau. Quá trình kiểm thử bao phủ toàn bộ luồng mua hàng từ tìm kiếm sản phẩm, xem chi tiết, quản lý giỏ hàng, thanh toán đến kiểm tra lịch sử đơn hàng.

Danh sách ba nền tảng được lựa chọn kiểm thử:
- Nền tảng thứ nhất: Google Chrome phiên bản 124 trên hệ điều hành Windows 11 Desktop
- Nền tảng thứ hai: Mozilla Firefox phiên bản 125 trên hệ điều hành Windows 11 Desktop
- Nền tảng thứ ba: Trình duyệt di động Mobile Browser trên thiết bị di động

Tất cả các ảnh chụp màn hình đều ghi nhận thanh thông tin sinh viên chứa mã số sinh viên 23120320 và email sinh viên 23120320@student.hcmus.edu.vn để đảm bảo tính xác thực.

---

## 2. Bằng chứng Thực nghiệm

Các bằng chứng ảnh chụp màn hình được tổ chức theo cấu trúc thư mục quy định:

### Nhóm 1. Desktop Google Chrome
- Bước 1. Danh sách sản phẩm và Tìm kiếm: `cross_platform/desktop_chrome/chrome_1.png`
- Bước 2. Chi tiết sản phẩm: `cross_platform/desktop_chrome/chrome_2.png`
- Bước 3. Giỏ hàng mua sắm: `cross_platform/desktop_chrome/chrome_3.png`
- Bước 4. Thanh toán đơn hàng: `cross_platform/desktop_chrome/chrome_4.png`
- Bước 5. Lịch sử đơn hàng: `cross_platform/desktop_chrome/chrome_5.png`

### Nhóm 2. Desktop Mozilla Firefox
- Bước 1. Danh sách sản phẩm và Tìm kiếm: `cross_platform/desktop_firefox/ff_1.png`
- Bước 2. Chi tiết sản phẩm: `cross_platform/desktop_firefox/ff_2.png`
- Bước 3. Giỏ hàng mua sắm: `cross_platform/desktop_firefox/ff_3.png`
- Bước 4. Thanh toán đơn hàng: `cross_platform/desktop_firefox/ff_4.png`
- Bước 5. Lịch sử đơn hàng: `cross_platform/desktop_firefox/ff_5.png`

### Nhóm 3. Mobile Browser
- Bước 1. Danh sách sản phẩm và Tìm kiếm: `cross_platform/mobile_or_safari/phone_1.png`
- Bước 2. Chi tiết sản phẩm: `cross_platform/mobile_or_safari/phone_2.png`
- Bước 3. Giỏ hàng mua sắm: `cross_platform/mobile_or_safari/phone_3.png`
- Bước 4. Thanh toán đơn hàng: `cross_platform/mobile_or_safari/phone_4.png`
- Bước 5. Lịch sử đơn hàng: `cross_platform/mobile_or_safari/phone_5.png`

---

## 3. Ma trận Tương thích Đa nền tảng

Bảng so sánh khả năng hiển thị và vận hành qua 5 bước chính:

| Bước Luồng Mua Hàng | Desktop Chrome | Desktop Firefox | Mobile Browser | Đánh giá Tương thích |
| :--- | :--- | :--- | :--- | :--- |
| Bước 1. Danh sách & Tìm kiếm | Hiển thị đầy đủ lưới sản phẩm, font chữ đồng đều | Bố cục lưới sản phẩm ổn định, thanh tìm kiếm hoạt động bình thường | Lưới sản phẩm co về một cột, nút tìm kiếm sát cạnh viền | Tương thích tốt trên máy tính, giao diện di động chấp nhận được |
| Bước 2. Chi tiết sản phẩm | Hình ảnh hiển thị rõ, nút thêm giỏ hàng đúng vị trí | Tương đồng hoàn toàn với Chrome về bố cục | Hình ảnh thu nhỏ vừa chiều rộng màn hình, văn bản tự ngắt dòng | Đạt tính nhất quán hiển thị trên cả ba nền tảng |
| Bước 3. Giỏ hàng mua sắm | Bảng giỏ hàng căn lề chuẩn, hiển thị đủ cột | Hiển thị bảng dữ liệu tương đồng Chrome | Bảng giỏ hàng xuất hiện thanh cuộn ngang do chiều rộng vượt khung | Khác biệt lớn trên di động do thiếu thiết kế responsive cho bảng |
| Bước 4. Thanh toán đặt hàng | Form điền thông tin hiển thị đúng thứ tự | Các trường nhập liệu và nút bấm đặt hàng hiển thị tốt | Bàn phím ảo trên di động đẩy khung nhìn lên che một phần form | Cần cải tiến vùng nhìn khi bàn phím ảo xuất hiện |
| Bước 5. Lịch sử đơn hàng | Bảng lịch sử đơn hiển thị đầy đủ thông tin | Màu sắc và định dạng số tiền hiển thị chuẩn | Chiều rộng bảng đơn hàng bị cắt mép phải nếu không cuộn ngang | Di động cần chuyển đổi bảng dữ liệu thành dạng thẻ |

---

## 4. Phân tích Kỹ thuật Chuyên sâu

### 4.1. Hiển thị Bố cục và CSS
- Cơ chế dàn trang Flexbox và Grid trên Chrome và Firefox cho kết quả tương đồng nhau hoàn toàn. Các khối nội dung không bị xô lệch vị trí.
- Trên môi trường di động, do màn hình hẹp, hệ thống sử dụng quy tắc CSS Tailwind responsive cơ bản. Tuy nhiên, các bảng dữ liệu giỏ hàng và lịch sử đơn hàng sử dụng thẻ HTML table thuần mà không có thuộc tính bọc cuộn mềm, dẫn đến hiện tượng tràn chiều rộng màn hình.

### 4.2. Hiển thị Phông chữ và Màu sắc
- Phông chữ hệ thống hiển thị đồng bộ giữa Blink Engine trên Chrome và Gecko Engine trên Firefox.
- Độ tương phản của các khối màu cảnh báo đỏ trên trang thanh toán và lịch sử đơn hàng giữ nguyên sắc thái trên cả ba nền tảng.

### 4.3. Trường Nhập liệu Form
- Ô nhập tổng tiền thanh toán hiển thị dưới dạng trường số trên cả ba nền tảng và đều có chung lỗi cho phép người dùng tự gõ chỉnh sửa số tiền.
- Bàn phím ảo trên thiết bị di động tự động kích hoạt bàn phím số khi chạm vào ô tổng tiền và bàn phím chữ khi chạm vào ô họ tên.

---

## 5. Phân loại Lỗi Đa nền tảng

### 5.1. Lỗi Hệ thống Chung
Các lỗi này xuất hiện trên toàn bộ các nền tảng do logic lập trình ở mã nguồn dùng chung:
- Lỗi nuốt click đầu tiên khi nhấn Thêm vào giỏ hàng
- Lỗi ô tổng tiền thanh toán cho phép người dùng tự chỉnh sửa số tiền
- Lỗi công thức tính toán mã giảm giá phần trăm làm tăng tổng tiền
- Lỗi giỏ hàng không tự động làm trống sau khi hoàn tất đặt hàng
- Lỗi biểu thức chính quy từ chối số điện thoại có số không ở đầu

### 5.2. Lỗi Đặc thù Nền tảng
- Trên nền tảng di động: Bảng danh sách giỏ hàng và lịch sử đơn hàng không có tính năng co giãn tự động, buộc người dùng phải vuốt ngang để xem hết thông tin cột.

---

## 6. Kết luận Kiểm thử Đa nền tảng

Trang web EShop duy trì được tính tương thích cốt lõi giữa hai trình duyệt máy tính phổ biến nhất hiện nay là Chrome và Firefox. Trải nghiệm trên thiết bị di động đáp ứng được các thao tác đặt hàng cơ bản nhưng cần tối ưu hóa thêm về thiết kế bảng biểu để người dùng không phải thao tác cuộn ngang.
