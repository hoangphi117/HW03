# Task Scenario & Usability Testing Instruments — EShop

> **Môn học:** Kiểm thử Phần mềm (FIT - HCMUS)  
> **Bài tập lớn:** HW03 — GUI & Usability Evaluation  
> **Mã số sinh viên:** 23120320  
> **Luồng kiểm thử (Flow):** Tìm kiếm sản phẩm → Xem chi tiết → Giỏ hàng → Áp dụng mã giảm giá → Thanh toán → Kiểm tra Lịch sử đơn hàng  
> **URL SUT:** `http://localhost:3000` (hoặc link ngrok/public khi test từ xa)

---

## 1. Kịch bản nhiệm vụ (Task Scenario — Goal-Oriented)

> [!IMPORTANT]
> **Nguyên tắc vàng:** Cung cấp cho người tham gia **mục tiêu thực tế (Goal)**, tuyệt đối **không hướng dẫn từng bước click chuột**. Để người tham gia tự do khám phá và thao tác trên giao diện.

### Lời dẫn đọc cho người tham gia (Backstory):
*"Chào bạn, bạn đang muốn mua một chiếc điện thoại thông minh để phục vụ công việc và giải trí trên trang web thương mại điện tử EShop. Ngân sách dự kiến của bạn khoảng dưới 20.000.000 ₫.*

*Nhiệm vụ của bạn là:*
1. *Tìm một sản phẩm điện thoại phù hợp trong danh mục và xem chi tiết thông tin.*
2. *Thêm sản phẩm đó vào giỏ hàng.*
3. *Tìm kiếm mã giảm giá khả dụng của cửa hàng để áp dụng giảm chi phí.*
4. *Tiến hành đặt hàng và hoàn tất thanh toán.*
5. *Kiểm tra lại xem đơn hàng vừa đặt đã được ghi nhận trong lịch sử mua hàng của tài khoản hay chưa.*

*Trong toàn bộ quá trình, bạn hãy thoải mái thao tác và chia sẻ suy nghĩ thành tiếng (Think Aloud). Không có thao tác nào là sai, chúng tôi đang đánh giá mức độ dễ dùng của hệ thống chứ không đánh giá bạn."*

---

## 2. Hướng dẫn Điều phối viên (Moderator Guide)

### Bước 1: Giới thiệu & Khởi động (2 phút)
- Chào đón người tham gia, cảm ơn họ đã dành thời gian.
- Nhấn mạnh: *"Chúng tôi kiểm thử sản phẩm, không kiểm tra bạn. Người dùng luôn luôn đúng; nếu có gì khó hiểu hay gây lỗi thì đó là lỗi của hệ thống."*
- Giới thiệu phương pháp **Think Aloud**: *"Hãy nói to bất cứ suy nghĩ, thắc mắc, băn khoăn hay sự bối rối nào xuất hiện trong đầu bạn khi nhìn vào màn hình."*
- Xin phép ghi âm/quay màn hình phục vụ phân tích học tập.

### Bước 2: Quan sát trung lập trong lúc làm bài (Neutral Observation) (5 - 8 phút)
- **Giữ im lặng**: Không chỉ trỏ vào màn hình, không giải thích các nút hay biểu tượng.
- **Nếu người dùng hỏi**: *"Tôi có nên bấm vào đây không?"* → Trả lời: *"Bạn nghĩ nếu bấm vào đó thì chuyện gì sẽ xảy ra? Hãy cứ làm theo trực giác của bạn."*
- **Can thiệp tối thiểu**: Chỉ can thiệp gợi ý khi người dùng bị kẹt hoàn toàn (hard blocker) quá 3 phút không biết đi tiếp thế nào. Ghi chú lại thời điểm can thiệp vào Session Notes.
- **Ghi chép (Live Notes)**:
  - Sự ngập ngừng, do dự (hesitation).
  - Thao tác nhấp chuột nhầm lẫn (misclicks).
  - Vẻ mặt hoặc lời nói bực bội, bất ngờ.

### Bước 3: Thu thập đánh giá (Post-task Survey & Debriefing) (3 - 5 phút)
- Mời người tham gia hoàn thành bảng khảo sát **SUS 10 câu**.
- Đặt 4 câu hỏi đào sâu (Probe Questions) dựa trên những điểm họ vừa ngập ngừng.
- Cảm ơn và kết thúc phiên.

---

## 3. Bảng câu hỏi SUS chuẩn hóa (System Usability Scale — 10 Items)

Thang đo Likert 5 mức độ:  
- **1 = Rất không đồng ý (Strongly Disagree)**  
- **2 = Không đồng ý (Disagree)**  
- **3 = Trung lập (Neutral)**  
- **4 = Đồng ý (Agree)**  
- **5 = Rất đồng ý (Strongly Agree)**

| STT | Câu hỏi (Tiếng Việt) | Original English Statement | Chiều đánh giá |
|:---:|:---|:---|:---:|
| **Q1** | Tôi nghĩ rằng tôi sẽ muốn sử dụng hệ thống này thường xuyên. | I think that I would like to use this system frequently. | Tích cực (+) |
| **Q2** | Tôi thấy hệ thống này phức tạp một cách không cần thiết. | I found the system unnecessarily complex. | Tiêu cực (-) |
| **Q3** | Tôi thấy hệ thống này dễ sử dụng. | I thought the system was easy to use. | Tích cực (+) |
| **Q4** | Tôi nghĩ rằng tôi sẽ cần sự hỗ trợ của một chuyên gia kỹ thuật để có thể sử dụng hệ thống này. | I think that I would need the support of a technical person to be able to use this system. | Tiêu cực (-) |
| **Q5** | Tôi nhận thấy các chức năng khác nhau trong hệ thống này được tích hợp rất tốt. | I found the various functions in this system were well integrated. | Tích cực (+) |
| **Q6** | Tôi nghĩ rằng hệ thống này có quá nhiều điểm thiếu nhất quán (mâu thuẫn). | I thought there was too much inconsistency in this system. | Tiêu cực (-) |
| **Q7** | Tôi tin rằng hầu hết mọi người sẽ học được cách sử dụng hệ thống này rất nhanh. | I would imagine that most people would learn to use this system very quickly. | Tích cực (+) |
| **Q8** | Tôi thấy hệ thống này rất cồng kềnh và khó sử dụng. | I found the system very cumbersome to use. | Tiêu cực (-) |
| **Q9** | Tôi cảm thấy rất tự tin khi sử dụng hệ thống này. | I felt very confident using the system. | Tích cực (+) |
| **Q10**| Tôi cần phải học rất nhiều điều trước khi có thể bắt đầu sử dụng thành thạo hệ thống này. | I needed to learn a lot of things before I could get going with this system. | Tiêu cực (-) |

---

## 4. Bộ câu hỏi Phỏng vấn mở đào sâu (Probe Questions)

Bao phủ 4 khía cạnh bắt buộc theo yêu cầu đề bài:

1. **Độ rõ ràng (Clarity):**
   - *"Trong suốt quá trình từ tìm sản phẩm đến thanh toán, có thông tin, nút bấm hay bước nào khiến bạn cảm thấy khó hiểu hoặc không chắc chắn về ý nghĩa của nó không?"*
2. **Khả năng phục hồi khi gặp lỗi (Error Recovery):**
   - *"Khi gặp lỗi (ví dụ nhập sai số điện thoại, chọn sai số lượng, hoặc nhập mã giảm giá), hệ thống thông báo cho bạn như thế nào? Bạn có dễ dàng nhận biết cách khắc phục để tiếp tục hay không?"*
3. **Tốc độ & Trải nghiệm thao tác (Speed):**
   - *"Bạn đánh giá thế nào về tốc độ phản hồi của trang web? Có thao tác nào bạn phải nhấp nhiều lần hoặc chờ đợi lâu không?"*
4. **Độ tin cậy & An tâm (Trust):**
   - *"Ở bước thanh toán và xem lại lịch sử đơn hàng, bạn có cảm thấy an tâm rằng đơn hàng và tiền của mình đã được xử lý chính xác không? Điều gì làm bạn cảm thấy an tâm (hoặc nghi ngờ)?"*
