# Báo Cáo Lỗi Giao Diện & Trải Nghiệm (GUI & Usability Bug Report)

**Mã Sinh Viên:** 23120320  
**Họ và Tên:** Sinh viên Kiểm thử Phần mềm  
**Hệ thống kiểm thử (SUT):** EShop ([https://github.com/ttbhanh/eshop-sut](https://github.com/ttbhanh/eshop-sut))  
**Repository Báo Lỗi:** [https://github.com/hoangphi117/HW03/issues](https://github.com/hoangphi117/HW03/issues)  
**Luồng kiểm thử:** `FR-05` (Search & Listing) $\rightarrow$ `FR-06` (Product Detail) $\rightarrow$ `FR-07` (Cart) $\rightarrow$ `FR-09` (Coupons) $\rightarrow$ `FR-08` (Checkout) $\rightarrow$ `FR-11` (Order History)  
**Tổng số lỗi phát hiện & đã log lên GitHub:** 22 lỗi (4 Critical, 5 High, 9 Medium, 4 Low)  

---

## Danh Sách 22 Lỗi Đã Tạo Trên GitHub Issues

| STT | Mã Bug | Màn hình | Khía cạnh | Mức độ | Tóm tắt lỗi | GitHub Issue (Link thật) | Ảnh minh chứng |
|:---:|:---|:---|:---:|:---:|:---|:---:|:---|
| 1 | BUG-01 | FR-05 | IA-02 | Medium | Màn hình trống trơn khi tìm kiếm 0 kết quả (Thiếu Empty State) | [#1](https://github.com/hoangphi117/HW03/issues/1) | `FR05-IA02-002.png` |
| 2 | BUG-02 | FR-05 | IA-03 | Medium | Thiếu hoàn toàn phân trang (Pagination) trên danh mục sản phẩm | [#2](https://github.com/hoangphi117/HW03/issues/2) | `FR05-IA03-001.png` |
| 3 | BUG-03 | FR-05 | IA-03 | Medium | Thiếu bộ lọc danh mục và menu sắp xếp theo giá | [#3](https://github.com/hoangphi117/HW03/issues/3) | `FR05-IA03-002.png` |
| 4 | BUG-04 | FR-05 | IA-04 | Low | Thiếu Skeleton placeholder / Spinner khi tải danh sách sản phẩm | [#4](https://github.com/hoangphi117/HW03/issues/4) | `FR05-IA04-001.png` |
| 5 | BUG-05 | FR-05 | IA-04 | Low | Vị trí cuộn trang bị reset về đầu khi quay lại từ trang chi tiết (PDP) | [#5](https://github.com/hoangphi117/HW03/issues/5) | `FR05-IA04-002-1.png`<br/>`FR05-IA04-002-2.png` |
| 6 | BUG-06 | FR-06 | IA-02 | Medium | Thiếu bộ chọn biến thể sản phẩm (màu sắc, kích cỡ, dung lượng) | [#6](https://github.com/hoangphi117/HW03/issues/6) | `FR06-IA02-001.png` |
| 7 | BUG-07 | FR-06 | IA-03 | Medium | Thiếu thanh điều hướng phân cấp Breadcrumb | [#7](https://github.com/hoangphi117/HW03/issues/7) | `FR06-IA03-001.png` |
| 8 | BUG-08 | FR-06 | IA-03 | Low | Thiếu nút quay lại danh mục sản phẩm trên trang chi tiết | [#8](https://github.com/hoangphi117/HW03/issues/8) | `FR06-IA03-002.png` |
| 9 | BUG-09 | FR-06 | IA-04 | Critical | Click lần 1 vào nút "Thêm vào giỏ" bị nuốt sự kiện, phải click 2 lần | [#9](https://github.com/hoangphi117/HW03/issues/9) | `FR06-IA04-001-1.png`<br/>`FR06-IA04-001-2.png` |
| 10 | BUG-10 | FR-07 | IA-02 | High | Số lượng trong giỏ hàng là text tĩnh, không có nút tăng/giảm số lượng | [#10](https://github.com/hoangphi117/HW03/issues/10) | `FR07-IA02-001.png` |
| 11 | BUG-11 | FR-09 | IA-02 | Critical | Lỗi tính mã giảm giá phần trăm: giảm giá âm, tổng tiền tăng gấp 10 lần | [#11](https://github.com/hoangphi117/HW03/issues/11) | `FR09-IA02-001.png` |
| 12 | BUG-12 | FR-09 | IA-03 | Medium | Không có nút hủy / gỡ mã giảm giá đã áp dụng | [#12](https://github.com/hoangphi117/HW03/issues/12) | `FR09-IA03-001.png` |
| 13 | BUG-13 | FR-08 | IA-02 | Critical | Trang thanh toán thiếu hoàn toàn form nhập thông tin giao hàng | [#13](https://github.com/hoangphi117/HW03/issues/13) | `FR08-IA02-001.png` |
| 14 | BUG-14 | FR-08 | IA-02 | Critical | Tổng tiền thanh toán là ô input cho phép người dùng tự sửa giá tùy ý | [#14](https://github.com/hoangphi117/HW03/issues/14) | `FR08-IA02-003.png` |
| 15 | BUG-15 | FR-08 | IA-02 | High | Thiếu tùy chọn phương thức thanh toán (COD / Chuyển khoản) | [#15](https://github.com/hoangphi117/HW03/issues/15) | `FR08-IA02-004.png` |
| 16 | BUG-16 | FR-08 | IA-03 | Medium | Thiếu thanh tiến trình các bước mua hàng (Checkout Step Indicator) | [#16](https://github.com/hoangphi117/HW03/issues/16) | `FR08-IA03-001.png` |
| 17 | BUG-17 | FR-08 | IA-03 | Low | Thiếu liên kết "Quay lại giỏ hàng" từ màn hình thanh toán | [#17](https://github.com/hoangphi117/HW03/issues/17) | `FR08-IA03-002.png` |
| 18 | BUG-18 | FR-08 | IA-04 | High | Giỏ hàng không được làm rỗng sau khi đặt hàng thành công | [#18](https://github.com/hoangphi117/HW03/issues/18) | `FR08-IA04-002-1.png`<br/>`FR08-IA04-002-2.png` |
| 19 | BUG-19 | FR-11 | IA-02 | High | Không thể xem chi tiết danh sách sản phẩm đã mua trong đơn hàng | [#19](https://github.com/hoangphi117/HW03/issues/19) | `FR11-IA02-001.png` |
| 20 | BUG-20 | FR-11 | IA-03 | Medium | Thiếu tính năng "Mua lại" (Re-order) các sản phẩm từ đơn hàng cũ | [#20](https://github.com/hoangphi117/HW03/issues/20) | `FR11-IA03-001.png` |
| 21 | BUG-21 | FR-11 | IA-03 | Low | Màn hình đặt hàng thành công thiếu liên kết dẫn tới Lịch sử đơn hàng | [#22](https://github.com/hoangphi117/HW03/issues/22) | `FR11-IA03-002.png` |
| 22 | BUG-22 | FR-11 | IA-04 | High | Cho phép hủy đơn hàng ngay cả khi đơn đã chuyển sang trạng thái đang giao | [#23](https://github.com/hoangphi117/HW03/issues/23) | `FR11-IA04-001.png` |

---

## Chi Tiết Các Lỗi Nghiêm Trọng (Top Critical / High Defects)

### 1. BUG-14: [Security/GUI] Tổng tiền thanh toán là ô input cho phép người dùng tự chỉnh sửa
* **Mã Checklist:** `FR08-IA02-003`
* **Màn hình:** FR-08 (Checkout)
* **Khía cạnh:** IA-02 (Forms)
* **Mức độ nghiêm trọng:** `Critical` (Lỗ hổng bảo mật & lỗi logic giao diện)
* **GitHub Issue:** [Issue #14](https://github.com/hoangphi117/HW03/issues/14)
* **Mô tả:** Trường "Tổng tiền thanh toán (VND)" trên trang xác nhận đơn hàng không phải là text hiển thị tĩnh mà lại là một thẻ `<input type="number">`. Người dùng có thể xóa số tiền thực tế (ví dụ 30.000.000₫) và gõ vào `1000` rồi bấm "Xác Nhận Thanh Toán", hệ thống gửi thẳng 1000₫ lên backend và ghi nhận thành công.
* **Các bước tái hiện:**
  1. Thêm sản phẩm trị giá 30.000.000₫ vào giỏ hàng.
  2. Bấm "Tiến hành thanh toán" để vào trang `/checkout`.
  3. Tại ô "Tổng tiền thanh toán (VND)", click chuột vào và gõ `1000`.
  4. Bấm "Xác Nhận Thanh Toán".
* **Kết quả thực tế:** Hệ thống tạo đơn hàng thành công với giá 1.000₫.
* **Kết quả mong đợi:** Tổng tiền phải là nhãn văn bản cố định (`read-only`), không được phép chỉnh sửa từ phía client.
* **Bằng chứng lỗi:** `evidence/bug_screenshots/FR08-IA02-003.png`

---

### 2. BUG-11: [Business Logic/GUI] Công thức tính mã giảm giá % bị âm làm tổng tiền tăng vọt
* **Mã Checklist:** `FR09-IA02-001`
* **Màn hình:** FR-09 (Discount Coupons)
* **Khía cạnh:** IA-02 (Forms)
* **Mức độ nghiêm trọng:** `Critical`
* **GitHub Issue:** [Issue #11](https://github.com/hoangphi117/HW03/issues/11)
* **Mô tả:** Trong backend, công thức tính giảm giá phần trăm bị viết sai thành `discount_amount = Math.floor(total_amount * (1 - coupon.discount_value))`. Với đơn hàng 30.000.000₫ và mã `SAVE10` (10%), công thức tính ra `30.000.000 * (1 - 10) = -270.000.000₫`. Dẫn đến tổng tiền thanh toán bị trừ số âm thành `300.000.000₫` (tăng gấp 10 lần).
* **Các bước tái hiện:**
  1. Thêm sản phẩm 30.000.000₫ vào giỏ hàng và chuyển sang Checkout.
  2. Nhập mã giảm giá `SAVE10`.
  3. Bấm nút "Áp dụng".
* **Kết quả thực tế:** Giao diện hiển thị: "Tiết kiệm: -270.000.000 ₫", "Thành tiền: 300.000.000 ₫".
* **Kết quả mong đợi:** Tiết kiệm 3.000.000 ₫, thành tiền còn lại là 27.000.000 ₫.
* **Bằng chứng lỗi:** `evidence/bug_screenshots/FR09-IA02-001.png`

---

### 3. BUG-09: [Event Handling] Click lần 1 vào nút "Thêm vào giỏ hàng" bị nuốt sự kiện
* **Mã Checklist:** `FR06-IA04-001`
* **Màn hình:** FR-06 (Product Detail)
* **Khía cạnh:** IA-04 (Feedback / State)
* **Mức độ nghiêm trọng:** `Critical`
* **GitHub Issue:** [Issue #9](https://github.com/hoangphi117/HW03/issues/9)
* **Mô tả:** Trong mã nguồn `ProductDetail.jsx`, hàm `handleAddToCart` có đoạn code: `if (clickCount === 0) { setClickCount(1); return; }`. Điều này khiến cho lần click chuột đầu tiên của người dùng vào nút "Thêm vào giỏ hàng" hoàn toàn bị phớt lờ, không có bất kỳ phản hồi nào, khiến người dùng tưởng nút bị liệt hoặc trang web bị đơ.
* **Các bước tái hiện:**
  1. Mở trang chi tiết bất kỳ: `/product/1`.
  2. Bấm nút "Thêm vào giỏ hàng" 1 lần.
* **Kết quả thực tế:** Không có gì xảy ra, giỏ hàng vẫn có 0 sản phẩm, nút không đổi trạng thái. Phải bấm lần thứ 2 mới được thêm.
* **Kết quả mong đợi:** Sản phẩm phải được thêm vào giỏ hàng ngay từ cú click đầu tiên, hiển thị toast/trạng thái xác nhận tức thì.
* **Bằng chứng lỗi (chuỗi hành động):**
  - Bước 1 (Click lần đầu không tác dụng): `evidence/bug_screenshots/FR06-IA04-001-1.png`
  - Bước 2 (Click lần hai mới thêm được): `evidence/bug_screenshots/FR06-IA04-001-2.png`

---

### 4. BUG-13: [Form/UI] Màn hình thanh toán thiếu hoàn toàn form thông tin giao hàng
* **Mã Checklist:** `FR08-IA02-001`
* **Màn hình:** FR-08 (Checkout)
* **Khía cạnh:** IA-02 (Forms)
* **Mức độ nghiêm trọng:** `Critical`
* **GitHub Issue:** [Issue #13](https://github.com/hoangphi117/HW03/issues/13)
* **Mô tả:** Trang `/checkout` chỉ hiển thị danh sách sản phẩm và ô mã giảm giá, hoàn toàn không có các trường để người mua nhập Tên người nhận hàng, Số điện thoại liên hệ, Địa chỉ giao hàng hay Tỉnh/Thành phố.
* **Kết quả thực tế:** Người dùng bấm "Xác Nhận Thanh Toán" mà không thể nhập địa chỉ nhận hàng.
* **Kết quả mong đợi:** Có form địa chỉ giao hàng với các trường bắt buộc và validation thời gian thực.
* **Bằng chứng lỗi:** `evidence/bug_screenshots/FR08-IA02-001.png`

---

### 5. BUG-18: [State Management] Giỏ hàng không được làm rỗng sau khi đặt hàng thành công
* **Mã Checklist:** `FR08-IA04-002`
* **Màn hình:** FR-08 (Checkout)
* **Khía cạnh:** IA-04 (Feedback / State)
* **Mức độ nghiêm trọng:** `High`
* **GitHub Issue:** [Issue #18](https://github.com/hoangphi117/HW03/issues/18)
* **Mô tả:** Trong `Checkout.jsx`, hàm `handleCheckout` gửi request tạo đơn hàng lên API thành công nhưng quên gọi hàm `clearCart()`. Khi người dùng quay lại giỏ hàng, các sản phẩm đã mua vẫn còn nguyên trong giỏ, dễ dẫn đến việc đặt hàng trùng lặp.
* **Kết quả thực tế:** Giỏ hàng giữ nguyên các món đã thanh toán.
* **Kết quả mong đợi:** Giỏ hàng tự động reset về trạng thái rỗng sau khi đơn hàng được ghi nhận.
* **Bằng chứng lỗi (chuỗi hành động):**
  - Bước 1 (Đặt hàng thành công): `evidence/bug_screenshots/FR08-IA04-002-1.png`
  - Bước 2 (Vào lại giỏ hàng sản phẩm vẫn còn nguyên): `evidence/bug_screenshots/FR08-IA04-002-2.png`
