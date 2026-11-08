# Báo cáo Đánh giá Trải nghiệm Người dùng

> **Môn học:** Kiểm thử Phần mềm (Software Testing) — FIT, HCMUS  
> **Bài tập lớn:** HW03 — Task 2: Usability Evaluation  
> **Mã số sinh viên:** 23120320  
> **Họ và tên:** Phi  
> **Luồng đánh giá:** Mua hàng E-commerce (Tìm kiếm → Chi tiết → Giỏ hàng → Mã giảm giá → Thanh toán → Lịch sử đơn hàng)  
> **SUT:** EShop Web Application (`http://localhost:3000`)  
> **Thời gian thực hiện:** Tháng 11/2026

---

## 1. Tóm tắt

Đợt đánh giá Usability này được thực hiện nhằm kiểm tra mức độ tiện dụng, tính rõ ràng, khả năng phục hồi lỗi và độ tin cậy của luồng mua hàng trên hệ thống EShop.
Quá trình đánh giá được thực hiện với **7 người tham gia thật (N=7)**, đại diện cho nhóm người dùng mua sắm trực tuyến phổ thông ngoài ngành IT, cung cấp email xác thực chính xác phục vụ kiểm tra đối soát (Mục 11).

### Kết quả then chốt:

- **Tỷ lệ hoàn thành nhiệm vụ (Completion Rate):** **71.4%** (5/7 người hoàn tất luồng, 2 người thất bại: P-01 do lỗi đơn hàng bị nhân đôi và P-04 do sai lệch thông tin & giá tiền).
- **Thời gian trung bình (Mean Time on Task):** **7.7 phút**.
- **Điểm Thang đo SUS (System Usability Scale):** **62.14 / 100** (Độ lệch chuẩn: 18.78).
- **Xếp hạng:** Hạng **F** — Đánh giá tính từ: **Poor** — Mức độ chấp nhận: **Marginal / Not Acceptable**.
- Điểm SUS đạt 62.14, **thấp hơn mức trung bình chuẩn công nghiệp (68.0)**, phản ánh rằng mặc dù hệ thống đáp ứng các bước cơ bản, người dùng phải đối mặt với **nhiều trở ngại nghiêm trọng về mặt trải nghiệm và tâm lý an toàn tài chính**.

---

## 2. Phương pháp luận & Thiết lập Đánh giá

### 2.1. Kịch bản Nhiệm vụ (Task Scenario)

Kịch bản được thiết kế theo phương pháp **Goal-Oriented**, không chỉ dẫn từng thao tác click chuột:

> _"Bạn đang cần mua một chiếc điện thoại thông minh dưới 20 triệu đồng trên EShop, tìm mã giảm giá có sẵn để tiết kiệm chi phí, tiến hành đặt hàng thanh toán và kiểm tra lại lịch sử đơn hàng để chắc chắn đơn đã được lưu."_

### 2.2. Phương thức Quan sát

- Điều phối viên đóng vai trò quan sát trung lập, không can thiệp hay giải thích giao diện trừ khi người dùng gặp bế tắc kỹ thuật hoàn toàn quá 3 phút.

### 2.3. Đối tượng Tham gia (Participants - Tuân thủ Mục 11)

Toàn bộ 7 người tham gia đều là người thật, có email xác thực trực tiếp:

|  ID  | Người tham gia      | Email liên hệ xác thực              | Tuổi | Giới tính | Trạng thái Task | Điểm SUS |
| :--: | :------------------ | :---------------------------------- | :--: | :-------: | :-------------: | :------: |
| P-01 | Nguyễn Yến Nhi      | `yennhifab@gmail.com`               |  21  |    Nữ     |   **Failed**    | **32.5** |
| P-02 | Trần Trọng Quân     | `trantrongquan052@gmail.com`        |  21  |    Nam    |   Hoàn thành    | **90.0** |
| P-03 | Phạm Gia Bảo        | `phambao0364@gmail.com`             |  21  |    Nam    |   Hoàn thành    | **72.5** |
| P-04 | Hoàng Minh Vũ       | `vu97694@gmail.com`                 |  21  |    Nam    |   **Failed**    | **50.0** |
| P-05 | Nguyễn Mạnh Hiền    | `manhhien12a1@gmail.com`            |  21  |    Nam    |   Hoàn thành    | **55.0** |
| P-06 | Trần Thượng Tuyên   | `jacktr1104@gmail.com`              |  22  |    Nam    |   Hoàn thành    | **82.5** |
| P-07 | Nguyễn Thanh Phương | `nguyenthanhphuong221105@gmail.com` |  21  |    Nam    |   Hoàn thành    | **52.5** |

### 2.4. Bằng chứng Thu thập & Xác nhận Quyền riêng tư

- **Ghi chép có cấu trúc (Structured Notes):** Toàn bộ 7 phiên quan sát đều được lập thành 7 file nhật ký độc lập tại `usability/session_notes/session_P-01.md` đến `session_P-07.md`.
- **Ghi hình & Quan sát (Screen Recordings):** Tiến hành quan sát trực tiếp màn hình thao tác của người tham gia (in-person và chia sẻ màn hình); các đoạn ghi hình minh chứng và log quan sát được lưu trữ quản lý tại thư mục `usability/recordings/`.
- **Đồng thuận (Consent):** 100% (7/7) người tham gia đã được phổ biến mục đích học thuật và xác nhận đồng thuận (Consent) cung cấp thông tin phản hồi và dữ liệu thực nghiệm.

---

## 3. Phân tích Dữ liệu Định lượng

### 3.1. Thang đo SUS (System Usability Scale)

- **Điểm trung bình (Mean SUS):** 62.14 / 100
- **Điểm trung vị (Median SUS):** 55.0 / 100
- **Phạm vi điểm (Range):** 32.5 - 90.0 (Độ lệch chuẩn: 18.78).
- **So sánh chuẩn (Benchmark Comparison):** Thấp hơn benchmark 68.0 là 5.86 điểm. Hệ thống nằm trong phân vị thứ 34 (Percentile Rank ~34%), xếp hạng **F (Poor)**, nằm ở mức **Marginal / Not Acceptable**.

### 3.2. Phân tích Chi tiết 10 Câu hỏi SUS

```
[Q1] Muốn dùng thường xuyên   : 2.6 / 5.0  (Thấp)
[Q2] Quá phức tạp             : 3.9 / 5.0  (Cao - Tiêu cực)
[Q3] Dễ sử dụng               : 2.6 / 5.0  (Thấp)
[Q4] Cần chuyên gia hỗ trợ    : 2.6 / 5.0  (Trung bình)
[Q5] Chức năng tích hợp tốt   : 2.7 / 5.0  (Thấp - Thiếu gắn kết)
[Q6] Quá nhiều mâu thuẫn      : 3.9 / 5.0  (Cao - Tiêu cực nặng)
[Q7] Dễ học sử dụng           : 3.6 / 5.0  (Tương đối tốt)
[Q8] Cồng kềnh khó dùng       : 3.4 / 5.0  (Trên trung bình)
[Q9] Tự tin khi sử dụng       : 2.6 / 5.0  (Rất thấp)
[Q10] Cần học nhiều trước dùng: 2.4 / 5.0  (Thấp - Dễ nắm bắt cơ bản)
```

---

## 4. Tổng hợp & Phân tích Định tính

Dựa trên ghi chép quan sát và phản hồi trực tiếp từ 7 người tham gia thực tế (N=7):

### 4.1. Độ rõ ràng & Nhận thức Giao diện (Clarity)

- **Sản phẩm bị thêm hàng loạt do lỗi nuốt phản hồi:** Người tham gia **P-03 (Phạm Gia Bảo)** phản ánh trực tiếp: _"Lúc bỏ giỏ hàng thì nó không hiện ra đã bỏ vào giỏ hàng, làm tôi ấn liên tục tưởng máy bị lag sau đó lúc kiểm tra giỏ hàng thì nó xuất hiện cả đống, tôi không hài lòng về cái này"_. Đây là minh chứng rõ rệt về hậu quả nghiêm trọng của khuyết tật không có thông báo Toast khi click `Add to Cart`.
- **Cấu trúc danh sách sản phẩm dễ tiếp cận ban đầu:** Người tham gia **P-01 (Nguyễn Yến Nhi)** và **P-02 (Trần Trọng Quân)** nhận xét giao diện tìm kiếm và hiển thị sản phẩm cơ bản khá tương đồng với các nền tảng thương mại điện tử quen thuộc, giúp họ không mất nhiều thời gian định hướng bước đầu.

### 4.2. Khả năng phục hồi khi gặp lỗi & Logic xử lý Coupon

- **Lỗi tính ngược mã giảm giá làm đội giá phi lý (Trở ngại chí mạng):**
  - **P-03 (Phạm Gia Bảo)** phát hiện và phản ánh: _"Cái mã giảm giá thì sử dụng được nhưng tổng tiền tăng từ 28 triệu lên 700 triệu, nó còn hiện đã giảm 672 triệu"_.
  - **P-05 (Nguyễn Mạnh Hiền)** và **P-04 (Hoàng Minh Vũ)** cùng xác nhận: _"Áp dụng mã giảm giá làm giá tiền tăng vọt lên thay vì giảm, sai giá mà không có thông báo hướng dẫn sửa lỗi"_.
  - Nguyên nhân bắt nguồn từ lỗi logic tính toán phần trăm coupon tại backend (`total * (1 - discount_value)` khi `discount_value = 25` thay vì `0.25`).
- **Thiếu thông báo hướng dẫn:** **P-01 (Nguyễn Yến Nhi)** nhận xét: _"Không thấy thông báo lỗi hiện lên để biết cách sửa"_ khi gặp các tình huống nhập liệu chưa khớp định dạng.

### 4.3. Tốc độ & Trải nghiệm thao tác (Speed)

- Thời gian thực hiện trung bình của 7 người tham gia đạt **7.7 phút** (dao động từ 3.0 phút đến 13.0 phút).
- Người tham gia **P-06 (Trần Thượng Tuyên)** đánh giá: _"Fast enough to keep someone with ADHD in check"_ — tốc độ tải trang và phản hồi HTTP của hệ thống rất nhanh nhẹn, không có hiện tượng giật lag hay treo trang.

### 4.4. Độ tin cậy & Tâm lý người dùng — _Điểm yếu lớn nhất_

- **Đơn hàng bị nhân đôi (Double Orders):** **P-01 (Nguyễn Yến Nhi)** gặp phải lỗi đơn hàng bị nhân đôi sau khi hoàn tất đặt hàng: _"Không chính xác lắm, tôi thấy đơn hàng bị double lên một cách khó hiểu"_. Lỗi này khiến người dùng xếp mức đánh giá Task Failed và cho điểm SUS rất thấp (32.5/100).
- **Mất niềm tin vì số tiền bị nhảy vọt:** **P-03** chia sẻ: _"Tôi không yên tâm chút nào tại số tiền cần thanh toán bị nhảy lên đến 700 triệu đồng"_.
- **Tác động tâm lý thị giác của màu sắc:** **P-06 (Trần Thượng Tuyên)** chỉ ra một chi tiết thiết kế tinh tế: _"Good at the fact that the orders instantly hit me in the eyes with the coloring. I wouldn't use red though, it truly emphasizes on how much money I'm spending"_ (Việc dùng màu đỏ rực cho tổng số tiền chi tiêu tạo cảm giác cảnh báo nguy hiểm và áp lực tài chính không đáng có cho người mua).

### 4.5. Phân nhóm Điểm đau & Tách biệt Lỗi cá biệt (Isolated Bugs) vs Vấn đề Thiết kế Hệ thống (Systemic Design Issues)

Theo đúng yêu cầu của Phase 3, các phát hiện từ 7 phiên kiểm thử được bóc tách rành mạch thành hai nhóm bản chất:

#### A. Lỗi Kỹ thuật Cá biệt

Đây là các khiếm khuyết lập trình cục bộ tại một hàm hoặc component cụ thể, có thể sửa nhanh bằng cách vá mã nguồn:

1. **Lỗi tính phần trăm coupon ngược (Issue #17):** Thuật toán nhân chiết khấu `total * (1 - discount)` với `discount = 25` khiến đơn hàng bị đội giá lên 700 triệu đồng.
2. **Lỗi nuốt click nút Thêm giỏ hàng (Issue #9):** Biến đếm `clickCount === 0` trong React Component chặn lần click đầu tiên của người dùng.
3. **Lỗi nhân đôi đơn hàng (Double Orders):** Gặp ở phiên P-01 do frontend gửi request đặt hàng hai lần liên tiếp khi người dùng bấm đúp nút thanh toán.
4. **Lỗi regex định dạng số điện thoại (Issue #13):** Biểu thức chính quy không hỗ trợ đầu số `0` của các nhà mạng Việt Nam.

#### B. Vấn đề Thiết kế Hệ thống

Đây là các khiếm khuyết mang tính hệ thống trong tư duy thiết kế trải nghiệm, ảnh hưởng xuyên suốt toàn bộ luồng mua hàng:

1. **Thiếu vòng lặp phản hồi trạng thái (Missing Feedback Loop):** Toàn bộ ứng dụng thiếu vắng hệ thống thông báo trạng thái Toast/Alert chuẩn. Người dùng không nhận được bất kỳ tín hiệu thị giác nào khi thêm hàng, áp mã, hay phát sinh lỗi nhập liệu.
2. **Lỗ hổng kiến trúc form nhập liệu (Form Architecture Flaw):** Trường "Tổng tiền" (Total Amount) được đặt trong thẻ `<input type="number">` có thể chỉnh sửa tự do thay vì là trường dữ liệu bất biến được tính toán bảo mật từ máy chủ (Issue #11).
3. **Lỗi đồng bộ trạng thái giỏ hàng sau thanh toán (State Desynchronization):** Sau khi hoàn tất đặt hàng, ứng dụng không có cơ chế tự động dọn sạch giỏ hàng (State management), dẫn đến xung đột tâm lý nghiêm trọng cho khách hàng (Issue #16).
4. **Thiếu bước tóm tắt & xác nhận giao dịch (Missing Order Review Step):** Chuyển từ giỏ hàng sang đặt hàng đột ngột, không có bước xác nhận địa chỉ giao hàng và phương thức thanh toán.

---

## 5. Phân cấp Mức độ Nghiêm trọng & Báo cáo Lỗi lên GitHub Issues

Toàn bộ các lỗi nghiêm trọng phát hiện qua thực nghiệm Usability đều đã được ghi nhận vào báo cáo Markdown và lập thành **GitHub Issues tương ứng có đính kèm ảnh bằng chứng chụp thực tế**:

|   Cấp độ    | Vấn đề Trải nghiệm                                            | Bằng chứng từ 7 Users     |    Màn hình    |  Khía cạnh IA  |                        GitHub Issue liên kết                        |
| :---------: | :------------------------------------------------------------ | :------------------------ | :------------: | :------------: | :-----------------------------------------------------------------: |
| **BLOCKER** | Lỗi tính toán coupon khiến đơn hàng tăng từ 28tr lên 700tr    | P-03, P-04, P-05 phản ánh | FR-09 Coupons  |  IA-02 Forms   |        [#17](https://github.com/hoangphi117/HW03/issues/17)         |
| **BLOCKER** | Đơn hàng bị nhân đôi (Double order) trong lịch sử sau khi đặt | P-01 thất bại task        | FR-11 History  | IA-04 Feedback | [#19](https://github.com/hoangphi117/HW03/issues/19) & Session P-01 |
|  **MAJOR**  | Nút "Thêm vào giỏ" nuốt click đầu tiên, không có thông báo    | P-03 click liên tục       |  FR-06 Detail  | IA-04 Feedback |         [#9](https://github.com/hoangphi117/HW03/issues/9)          |
|  **MAJOR**  | Ô tổng tiền thanh toán cho phép người dùng tự sửa số tiền     | 100% users băn khoăn      | FR-08 Checkout |  IA-02 Forms   |        [#11](https://github.com/hoangphi117/HW03/issues/11)         |
|  **MAJOR**  | Hệ thống từ chối số điện thoại Việt Nam hợp lệ (đầu số 09/08) | Ghi nhận trong form       | FR-08 Checkout |  IA-02 Forms   |        [#13](https://github.com/hoangphi117/HW03/issues/13)         |
|  **MAJOR**  | Giỏ hàng không tự làm trống sau khi đặt hàng thành công       | P-02, P-07 bối rối        | FR-07 & FR-08  | IA-04 Feedback |        [#16](https://github.com/hoangphi117/HW03/issues/16)         |
|  **MINOR**  | Dùng màu đỏ cảnh báo cho tổng số tiền chi tiêu trong lịch sử  | P-06 phản ánh áp lực      | FR-11 History  |    IA-01 UI    |        [#23](https://github.com/hoangphi117/HW03/issues/23)         |

---
