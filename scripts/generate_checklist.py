"""
HW03 — GUI Checklist Generator & Execution Results (gui-checklist-runner skill)
Updated per user request:
  - Removed columns: Check_Description, Source
  - Removed cases: FR06-IA02-002, FR06-IA04-002, FR07-IA02-002, FR07-IA04-001, FR08-IA02-002, FR07-IA04-002
  - Updated screenshot paths to user-provided screenshots in evidence/bug_screenshots/
  - Multi-step consecutive action screenshots (-1 and -2) grouped together
Outputs:
  - checklists/HW03_GUI_Checklist.xlsx (Checklist: 42 items, Test_Summary, Bug_Log: 22 items)
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

STUDENT_ID = "23120320"

# Schema: (ID, Screen, FR_Code, Aspect, Category, Steps_to_Test, Expected_Result, Status, Notes, Issue_URL, Why_AI_Missed, Screenshot)
ITEMS = [
    # =========================================================================
    # 1. FR-05: Product Listing and Search (8 items: 5 Passed, 3 Failed)
    # =========================================================================
    (
        "FR05-IA01-001", "Product Listing & Search", "FR-05", "IA-01", "Typography",
        "1. Truy cập http://localhost:5173/\n2. Kiểm tra cỡ chữ tiêu đề 'Danh sách sản phẩm' (h1), tên sản phẩm (h2), và giá bán.",
        "Tiêu đề trang h1 >= 24px, tên sản phẩm h2 >= 18px font-semibold, giá bán rõ ràng nổi bật; phân cấp thị giác chuẩn.",
        "Passed", "Cỡ chữ hiển thị rõ ràng, tiêu đề h1 text-3xl, thẻ sản phẩm có cấu trúc phân cấp trực quan tốt.",
        "", "", ""
    ),
    (
        "FR05-IA01-002", "Product Listing & Search", "FR-05", "IA-01", "Color & Contrast",
        "1. Dùng DevTools kiểm tra độ tương phản giữa màu chữ tên sản phẩm/giá bán với nền thẻ card trắng.",
        "Tỷ lệ tương phản chữ đen trên nền trắng >= 12:1, chữ giá đỏ trên nền trắng >= 4.6:1, đạt chuẩn WCAG AA.",
        "Passed", "Độ tương phản đạt chuẩn WCAG AA, chữ dễ đọc trên nền card trắng.",
        "", "", ""
    ),
    (
        "FR05-IA02-001", "Product Listing & Search", "FR-05", "IA-02", "Search Form",
        "1. Kiểm tra ô tìm kiếm trên góc phải trang chủ.\n2. Kiểm tra placeholder và nút 'Tìm'.",
        "Ô input có placeholder 'Tìm kiếm...', nút 'Tìm' màu xanh rõ ràng và kích hoạt tìm kiếm khi click.",
        "Passed", "Ô tìm kiếm hoạt động bình thường, placeholder hiển thị đầy đủ.",
        "", "", ""
    ),
    (
        "FR05-IA02-002", "Product Listing & Search", "FR-05", "IA-02", "Empty Search State",
        "1. Nhập chuỗi không tồn tại 'SanphamKhongTonTai999' vào ô tìm kiếm.\n2. Bấm nút 'Tìm'.",
        "Hệ thống hiển thị thông báo thân thiện 'Không tìm thấy sản phẩm' kèm nút reset hoặc gợi ý tìm kiếm.",
        "Failed", "Màn hình trống trơn hoàn toàn, không có thông báo không tìm thấy kết quả hay nút quay lại.",
        "https://github.com/hoangphi117/HW03/issues/1", "EDGE_CASE", "evidence/bug_screenshots/FR05-IA02-002.png"
    ),
    (
        "FR05-IA03-001", "Product Listing & Search", "FR-05", "IA-03", "Pagination",
        "1. Kiểm tra phần chân trang danh sách sản phẩm.\n2. Tìm các nút phân trang (Next, Prev, Trang 1, 2...).",
        "Có thanh điều hướng phân trang khi số lượng sản phẩm lớn hơn kích thước 1 trang.",
        "Failed", "Thiếu hoàn toàn phân trang (Pagination), toàn bộ sản phẩm bị dồn trên một trang duy nhất.",
        "https://github.com/hoangphi117/HW03/issues/2", "", "evidence/bug_screenshots/FR05-IA03-001.png"
    ),
    (
        "FR05-IA03-002", "Product Listing & Search", "FR-05", "IA-03", "Filter & Sorting",
        "1. Tìm bộ lọc danh mục (Điện thoại, Laptop, Phụ kiện).\n2. Tìm menu sắp xếp theo giá (Tăng/Giảm dần).",
        "Có thanh bộ lọc danh mục và dropdown sắp xếp giá hoạt động tức thì.",
        "Failed", "Thiếu hoàn toàn bộ lọc danh mục và dropdown sắp xếp sản phẩm trên giao diện người dùng.",
        "https://github.com/hoangphi117/HW03/issues/3", "", "evidence/bug_screenshots/FR05-IA03-002.png"
    ),
    (
        "FR05-IA04-001", "Product Listing & Search", "FR-05", "IA-04", "Loading State",
        "1. Điều chỉnh Network sang 'Slow 3G' trong DevTools.\n2. Tải lại trang chủ http://localhost:5173/.",
        "Xuất hiện skeleton placeholder hoặc spinner loading mượt mà trong lúc fetch dữ liệu API.",
        "Failed", "Không có loading spinner hay skeleton; giao diện nhấp nháy chuyển từ trắng sang nội dung.",
        "https://github.com/hoangphi117/HW03/issues/4", "", "evidence/bug_screenshots/FR05-IA04-001.png"
    ),
    (
        "FR05-IA04-002", "Product Listing & Search", "FR-05", "IA-04", "Scroll Restoration",
        "1. Cuộn chuột xuống cuối danh sách sản phẩm.\n2. Bấm 'Xem chi tiết' một sản phẩm.\n3. Bấm nút Back của trình duyệt.",
        "Trình duyệt quay lại đúng vị trí sản phẩm đã xem trước đó mà không bị giật cuộn.",
        "Failed", "Vị trí cuộn bị reset hoàn toàn về đầu trang (top 0), người dùng phải cuộn lại từ đầu.",
        "https://github.com/hoangphi117/HW03/issues/5", "PROMPT_GAP", "evidence/bug_screenshots/FR05-IA04-002-1.png\nevidence/bug_screenshots/FR05-IA04-002-2.png"
    ),

    # =========================================================================
    # 2. FR-06: Product Detail View (6 items: 2 Passed, 4 Failed)
    # [Deleted FR06-IA02-002, FR06-IA04-002]
    # =========================================================================
    (
        "FR06-IA01-001", "Product Detail", "FR-06", "IA-01", "Retina Image Display",
        "1. Mở trang chi tiết sản phẩm /product/1.\n2. Phóng to trình duyệt 150-200% để kiểm tra độ sắc nét ảnh.",
        "Hình ảnh giữ được độ phân giải nét, tỷ lệ khung hình không bị méo lệch.",
        "Passed", "Ảnh hiển thị đúng tỷ lệ khung hình, không vỡ nét khi zoom.",
        "", "", ""
    ),
    (
        "FR06-IA01-002", "Product Detail", "FR-06", "IA-01", "Layout Consistency",
        "1. Kiểm tra bố cục 2 cột (ảnh bên trái, thông tin bên phải trên desktop).\n2. Kiểm tra khoảng cách margin/padding.",
        "Khoảng cách padding p-6, gap-8 đồng nhất, thông tin trình bày gọn gàng, trực quan.",
        "Passed", "Bố cục chia 2 cột rõ ràng, khoảng cách margin padding đạt chuẩn thiết kế.",
        "", "", ""
    ),
    (
        "FR06-IA02-001", "Product Detail", "FR-06", "IA-02", "Variant Selector",
        "1. Mở chi tiết sản phẩm có nhiều cấu hình (ví dụ iPhone 15 Pro Max).\n2. Tìm bộ chọn màu sắc / dung lượng.",
        "Có các nút chọn biến thể với trạng thái active/inactive rõ ràng.",
        "Failed", "Thiếu hoàn toàn bộ chọn biến thể (màu sắc, kích cỡ, dung lượng) trên trang chi tiết.",
        "https://github.com/hoangphi117/HW03/issues/6", "", "evidence/bug_screenshots/FR06-IA02-001.png"
    ),
    (
        "FR06-IA03-001", "Product Detail", "FR-06", "IA-03", "Breadcrumbs Navigation",
        "1. Quan sát phần đầu nội dung trang chi tiết sản phẩm.\n2. Kiểm tra liên kết phân cấp danh mục.",
        "Thanh breadcrumb hiển thị đầy đủ và cho phép bấm quay về danh mục cha.",
        "Failed", "Thiếu hoàn toàn thanh điều hướng Breadcrumb, người dùng mất dấu vị trí hiện tại.",
        "https://github.com/hoangphi117/HW03/issues/7", "", "evidence/bug_screenshots/FR06-IA03-001.png"
    ),
    (
        "FR06-IA03-002", "Product Detail", "FR-06", "IA-03", "Back Navigation",
        "1. Tìm nút quay lại trên trang chi tiết sản phẩm.",
        "Có nút 'Quay lại' hoặc mũi tên điều hướng đưa người dùng về trang danh sách sản phẩm.",
        "Failed", "Không có nút quay lại danh sách sản phẩm; chỉ có thể bấm nút Back trình duyệt hoặc logo Header.",
        "https://github.com/hoangphi117/HW03/issues/8", "", "evidence/bug_screenshots/FR06-IA03-002.png"
    ),
    (
        "FR06-IA04-001", "Product Detail", "FR-06", "IA-04", "Add to Cart Feedback",
        "1. Mở trang chi tiết sản phẩm /product/1.\n2. Click nút 'Thêm vào giỏ hàng' 1 lần duy nhất.\n3. Quan sát giỏ hàng và phản hồi.",
        "Sản phẩm được thêm ngay vào giỏ hàng từ lần click đầu tiên, nút chuyển trạng thái 'Đã thêm'.",
        "Failed", "LỖI CODE NẶNG: Click lần 1 bị nuốt sự kiện (clickCount===0), người dùng phải click lần 2 mới thêm được.",
        "https://github.com/hoangphi117/HW03/issues/9", "", "evidence/bug_screenshots/FR06-IA04-001-1.png\nevidence/bug_screenshots/FR06-IA04-001-2.png"
    ),

    # =========================================================================
    # 3. FR-07: Shopping Cart (5 items: 4 Passed, 1 Failed)
    # [Deleted FR07-IA02-002, FR07-IA04-001, FR07-IA04-002]
    # =========================================================================
    (
        "FR07-IA01-001", "Shopping Cart", "FR-07", "IA-01", "Cart Layout Structure",
        "1. Thêm sản phẩm vào giỏ và điều hướng đến /cart.\n2. Kiểm tra cấu trúc các cột trong bảng giỏ hàng.",
        "Bảng giỏ hàng hiển thị đầy đủ, căn lề chuẩn, giá thành tiền hiển thị ngay hàng thẳng lối.",
        "Passed", "Bảng hiển thị đầy đủ các cột thông tin, giao diện gọn gàng và dễ nhìn.",
        "", "", ""
    ),
    (
        "FR07-IA01-002", "Shopping Cart", "FR-07", "IA-01", "Currency Formatting",
        "1. Quan sát cột Giá, Thành tiền và dòng Tổng tạm tính tại giỏ hàng.",
        "Số tiền có dấu chấm phân cách hàng nghìn (ví dụ 30.000.000 ₫), ký hiệu tiền tệ chuẩn tiếng Việt.",
        "Passed", "Định dạng số tiền hiển thị đúng chuẩn phân cách hàng nghìn (locale string) và ký hiệu ₫.",
        "", "LOCALE", ""
    ),
    (
        "FR07-IA02-001", "Shopping Cart", "FR-07", "IA-02", "Quantity Stepper Input",
        "1. Tại trang giỏ hàng, tìm ô nhập số lượng hoặc nút tăng/giảm (+ / -).\n2. Thử đổi số lượng từ 1 thành 2.",
        "Có ô input hoặc cặp nút +/- để thay đổi số lượng, tổng tiền tự động tính lại ngay lập tức.",
        "Failed", "Số lượng chỉ là text tĩnh không cho chỉnh sửa; người dùng buộc phải xóa đi và thêm lại từ đầu.",
        "https://github.com/hoangphi117/HW03/issues/10", "", "evidence/bug_screenshots/FR07-IA02-001.png"
    ),
    (
        "FR07-IA03-001", "Shopping Cart", "FR-07", "IA-03", "Continue Shopping Navigation",
        "1. Tại trang giỏ hàng, bấm nút '← Mua tiếp'.",
        "Hệ thống chuyển hướng mượt mà về trang chủ danh sách sản phẩm /.",
        "Passed", "Nút 'Mua tiếp' hoạt động chính xác, đưa người dùng quay lại trang chủ.",
        "", "", ""
    ),
    (
        "FR07-IA03-002", "Shopping Cart", "FR-07", "IA-03", "Proceed to Checkout CTA",
        "1. Khi đã đăng nhập và có sản phẩm trong giỏ, bấm 'Tiến hành thanh toán'.",
        "Hệ thống chuyển sang trang xác nhận đơn hàng /checkout.",
        "Passed", "Nút bấm hoạt động đúng, điều hướng mượt mà đến trang checkout.",
        "", "", ""
    ),

    # =========================================================================
    # 4. FR-09: Discount Coupons (8 items: 6 Passed, 2 Failed)
    # =========================================================================
    (
        "FR09-IA01-001", "Discount Coupons", "FR-09", "IA-01", "Coupon Section Layout",
        "1. Quan sát khu vực 'Mã Giảm Giá' tại trang /checkout.\n2. Kiểm tra cách nhóm ô input, nút bấm và vùng kết quả.",
        "Khu vực mã giảm giá đóng khung nền xám bg-gray-50, ô input viền rõ, nút cam nổi bật.",
        "Passed", "Khu vực mã giảm giá được bố cục gọn gàng, thành phần trực quan và đồng bộ.",
        "", "", ""
    ),
    (
        "FR09-IA02-001", "Discount Coupons", "FR-09", "IA-02", "Percentage Coupon Calculation",
        "1. Nhập mã coupon 'SAVE10' (giảm 10% cho đơn từ 300k).\n2. Bấm nút 'Áp dụng'.\n3. Kiểm tra số tiền giảm và tổng thanh toán.",
        "Tiết kiệm: 3.000.000 ₫ (10%), tổng thanh toán giảm từ 30.000.000 ₫ còn 27.000.000 ₫.",
        "Failed", "LỖI LOGIC NGHIÊM TRỌNG: Backend tính Math.floor(total * (1 - discount_value)) làm giảm giá thành số âm (-270tr), tổng tiền tăng vọt lên 300 triệu VND.",
        "https://github.com/hoangphi117/HW03/issues/11", "", "evidence/bug_screenshots/FR09-IA02-001.png"
    ),
    (
        "FR09-IA02-002", "Discount Coupons", "FR-09", "IA-02", "Expired Coupon Error",
        "1. Nhập mã coupon 'EXPIRED' vào ô giảm giá.\n2. Bấm 'Áp dụng'.",
        "Hiển thị thông báo lỗi màu đỏ rõ ràng: 'Mã giảm giá đã hết hạn'.",
        "Passed", "Hệ thống hiển thị đúng câu thông báo: 'Mã giảm giá đã hết hạn'.",
        "", "EDGE_CASE", ""
    ),
    (
        "FR09-IA02-003", "Discount Coupons", "FR-09", "IA-02", "Usage Limit Error",
        "1. Dùng tài khoản đã sử dụng coupon quá số lần quy định.\n2. Nhập lại mã và bấm 'Áp dụng'.",
        "Hiển thị thông báo cụ thể về việc đã đạt giới hạn sử dụng mã của tài khoản.",
        "Passed", "Thông báo giới hạn số lần sử dụng hiển thị chính xác.",
        "", "EDGE_CASE", ""
    ),
    (
        "FR09-IA03-001", "Discount Coupons", "FR-09", "IA-03", "Remove Applied Coupon",
        "1. Áp dụng mã coupon thành công.\n2. Tìm nút 'Hủy mã' hoặc dấu 'X' để gỡ coupon.",
        "Có nút gỡ mã giảm giá, sau khi bấm tổng tiền hoàn về ban đầu và ô input được xóa sạch.",
        "Failed", "Không có nút hủy/gỡ mã giảm giá đã áp dụng; người dùng không thể hủy mã nếu đổi ý.",
        "https://github.com/hoangphi117/HW03/issues/12", "", "evidence/bug_screenshots/FR09-IA03-001.png"
    ),
    (
        "FR09-IA03-002", "Discount Coupons", "FR-09", "IA-03", "Min Order Amount Warning",
        "1. Nhập mã có điều kiện giá trị đơn hàng tối thiểu cao hơn giỏ hàng hiện tại.\n2. Bấm 'Áp dụng'.",
        "Thông báo cảnh báo hiển thị rõ ràng số tiền tối thiểu cần đạt để áp dụng mã.",
        "Passed", "Thông báo yêu cầu giá trị đơn hàng tối thiểu hiển thị đầy đủ.",
        "", "", ""
    ),
    (
        "FR09-IA04-001", "Discount Coupons", "FR-09", "IA-04", "Apply Loading State",
        "1. Nhập mã coupon và click 'Áp dụng'.\n2. Quan sát nút bấm trong thời gian gọi API.",
        "Nút hiển thị trạng thái loading '...' và disabled để ngăn người dùng bấm liên tục.",
        "Passed", "Nút đổi sang '...' và disabled trong lúc đang gọi API xử lý.",
        "", "", ""
    ),
    (
        "FR09-IA04-002", "Discount Coupons", "FR-09", "IA-04", "Invalid Code Inline Feedback",
        "1. Nhập mã bừa không có trong hệ thống (ví dụ: 'KHONGTONTAI').\n2. Bấm 'Áp dụng'.",
        "Thông báo chữ đỏ xuất hiện bên dưới ô nhập: 'Mã giảm giá không tồn tại hoặc đã bị vô hiệu hóa'.",
        "Passed", "Thông báo lỗi hiển thị rõ ràng, màu đỏ đúng chuẩn trạng thái thất bại.",
        "", "", ""
    ),

    # =========================================================================
    # 5. FR-08: Checkout (9 items: 2 Passed, 7 Failed)
    # [Deleted FR08-IA02-002]
    # =========================================================================
    (
        "FR08-IA01-001", "Checkout", "FR-08", "IA-01", "Order Summary Structure",
        "1. Quan sát phần 'Xác Nhận Đơn Hàng' tại trang /checkout.\n2. Kiểm tra danh sách món hàng và tiền.",
        "Danh sách sản phẩm được định dạng rõ ràng, tên món kèm số lượng và thành tiền từng món.",
        "Passed", "Thông tin tóm tắt giỏ hàng hiển thị rõ ràng, dễ đối chiếu.",
        "", "", ""
    ),
    (
        "FR08-IA01-002", "Checkout", "FR-08", "IA-01", "Mobile Responsive Reflow",
        "1. Mở DevTools chế độ Mobile (iPhone SE 375px width).\n2. Kiểm tra thanh cuộn ngang.",
        "Trang hiển thị vừa vặn chiều ngang 100%, không bị tràn layout hay xuất hiện thanh cuộn ngang.",
        "Passed", "Giao diện reflow tốt trên màn hình hẹp, không bị bể khung hay thanh cuộn ngang.",
        "", "PLATFORM", ""
    ),
    (
        "FR08-IA02-001", "Checkout", "FR-08", "IA-02", "Shipping Address Form",
        "1. Kiểm tra các trường thông tin giao hàng tại trang Checkout.",
        "Có form đầy đủ gồm: Tên người nhận, Số điện thoại nhận hàng, Địa chỉ chi tiết, Tỉnh/Thành phố.",
        "Failed", "THIẾU FORM GIAO HÀNG: Trang thanh toán hoàn toàn không có form nhập họ tên, SĐT, địa chỉ nhận hàng.",
        "https://github.com/hoangphi117/HW03/issues/13", "", "evidence/bug_screenshots/FR08-IA02-001.png"
    ),
    (
        "FR08-IA02-003", "Checkout", "FR-08", "IA-02", "Total Price Input Security & Integrity",
        "1. Quan sát trường 'Tổng tiền thanh toán (VND)' tại /checkout.\n2. Thử gõ số tiền khác (ví dụ 1.000 VND).",
        "Tổng tiền phải là nhãn text hiển thị cố định (read-only); không được phép là ô input cho sửa giá.",
        "Failed", "LỖI BẢO MẬT CỰC NẶNG: Tổng tiền là một thẻ input cho phép người dùng tự sửa thành bất kỳ số tiền nào (ví dụ 1.000₫) rồi thanh toán.",
        "https://github.com/hoangphi117/HW03/issues/14", "", "evidence/bug_screenshots/FR08-IA02-003.png"
    ),
    (
        "FR08-IA02-004", "Checkout", "FR-08", "IA-02", "Payment Method Selection",
        "1. Tìm khu vực chọn phương thức thanh toán tại trang Checkout.",
        "Có tùy chọn radio button giữa: 'Thanh toán khi nhận hàng (COD)' và 'Chuyển khoản ngân hàng'.",
        "Failed", "Thiếu hoàn toàn tùy chọn phương thức thanh toán; người dùng không biết sẽ thanh toán bằng hình thức nào.",
        "https://github.com/hoangphi117/HW03/issues/15", "", "evidence/bug_screenshots/FR08-IA02-004.png"
    ),
    (
        "FR08-IA03-001", "Checkout", "FR-08", "IA-03", "Checkout Progress Indicator",
        "1. Kiểm tra đầu trang thanh toán xem có thanh tiến trình các bước mua hàng hay không.",
        "Có thanh step indicator hiển thị bước hiện tại, các bước trước có dấu tick hoàn thành.",
        "Failed", "Thiếu hoàn toàn thanh tiến trình các bước thanh toán (Checkout Step Progress Bar).",
        "https://github.com/hoangphi117/HW03/issues/16", "", "evidence/bug_screenshots/FR08-IA03-001.png"
    ),
    (
        "FR08-IA03-002", "Checkout", "FR-08", "IA-03", "Back to Cart Link",
        "1. Tìm liên kết quay lại giỏ hàng từ trang Checkout.",
        "Có liên kết 'Quay lại giỏ hàng' đưa người dùng về /cart mà không làm mất sản phẩm hay voucher.",
        "Failed", "Không có liên kết 'Quay lại giỏ hàng' trên trang checkout; người dùng bị khóa trong luồng thanh toán.",
        "https://github.com/hoangphi117/HW03/issues/17", "", "evidence/bug_screenshots/FR08-IA03-002.png"
    ),
    (
        "FR08-IA04-001", "Checkout", "FR-08", "IA-04", "Submit Button Loading State",
        "1. Bấm nút 'Xác Nhận Thanh Toán'.\n2. Quan sát nút bấm.",
        "Nút chuyển sang trạng thái disabled và hiển thị 'Đang xử lý...' để chống double-submit.",
        "Passed", "Nút bấm hiển thị 'Đang xử lý...' và bị khóa click đúng chuẩn.",
        "", "", ""
    ),
    (
        "FR08-IA04-002", "Checkout", "FR-08", "IA-04", "Post-checkout Cart State Reset",
        "1. Đặt hàng thành công (hiện thông báo 'Thanh toán thành công!').\n2. Quay lại trang /cart.",
        "Giỏ hàng phải được làm rỗng hoàn toàn, hiển thị 'Giỏ hàng của bạn đang trống'.",
        "Failed", "LỖI STATE: Sau khi thanh toán thành công, hàm clearCart() không được gọi; sản phẩm vẫn nằm nguyên trong giỏ hàng.",
        "https://github.com/hoangphi117/HW03/issues/18", "", "evidence/bug_screenshots/FR08-IA04-002-1.png\nevidence/bug_screenshots/FR08-IA04-002-2.png"
    ),

    # =========================================================================
    # 6. FR-11: Order History View (6 items: 2 Passed, 4 Failed)
    # =========================================================================
    (
        "FR11-IA01-001", "Order History", "FR-11", "IA-01", "Order Status Badge Semantics",
        "1. Truy cập /profile xem danh sách đơn hàng.\n2. Kiểm tra nhãn và màu sắc: Chờ xác nhận, Đã xác nhận, Đang giao, Đã giao, Đã hủy.",
        "Mỗi trạng thái có màu nền riêng biệt (xanh lá, xanh dương, đỏ, vàng) kèm nhãn tiếng Việt chuẩn.",
        "Passed", "Nhãn trạng thái dịch chuẩn tiếng Việt và có màu sắc phân biệt rất trực quan.",
        "", "CONTEXT", ""
    ),
    (
        "FR11-IA01-002", "Order History", "FR-11", "IA-01", "Date Display Format",
        "1. Kiểm tra cột 'Ngày đặt' trong bảng lịch sử đơn hàng.",
        "Ngày hiển thị theo chuẩn định dạng Việt Nam ngày/tháng/năm (ví dụ 07/11/2026).",
        "Passed", "Định dạng ngày tháng chuẩn DD/MM/YYYY thông qua hàm toLocaleDateString().",
        "", "LOCALE", ""
    ),
    (
        "FR11-IA02-001", "Order History", "FR-11", "IA-02", "Order Details Breakdown",
        "1. Click vào mã đơn hàng hoặc dòng đơn hàng trong bảng.\n2. Kiểm tra xem có mở popup/trang chi tiết đơn không.",
        "Hiển thị danh sách các sản phẩm trong đơn, đơn giá, số lượng, địa chỉ giao hàng và mã giảm giá đã dùng.",
        "Failed", "Không có tính năng xem chi tiết đơn hàng; người dùng hoàn toàn không biết đơn đó gồm những sản phẩm nào.",
        "https://github.com/hoangphi117/HW03/issues/19", "", "evidence/bug_screenshots/FR11-IA02-001.png"
    ),
    (
        "FR11-IA03-001", "Order History", "FR-11", "IA-03", "Re-order Quick CTA",
        "1. Tìm nút 'Mua lại' trên từng đơn hàng đã giao thành công.",
        "Có nút 'Mua lại' giúp thêm nhanh toàn bộ sản phẩm của đơn cũ vào giỏ và dẫn đến /cart.",
        "Failed", "Thiếu hoàn toàn tính năng 'Mua lại' (Re-order) cho các đơn hàng cũ.",
        "https://github.com/hoangphi117/HW03/issues/20", "CONTEXT", "evidence/bug_screenshots/FR11-IA03-001.png"
    ),
    (
        "FR11-IA03-002", "Order History", "FR-11", "IA-03", "Checkout Success Navigation Link",
        "1. Hoàn tất thanh toán đơn hàng.\n2. Quan sát các nút bấm tại màn hình 'Thanh toán thành công!'.",
        "Có nút 'Xem đơn hàng trong Lịch sử' đưa người dùng đến /profile để theo dõi đơn vừa tạo.",
        "Failed", "Trang thành công chỉ có duy nhất nút 'Quay lại trang chủ', không có liên kết xem đơn hàng vừa tạo.",
        "https://github.com/hoangphi117/HW03/issues/22", "", "evidence/bug_screenshots/FR11-IA03-002.png"
    ),
    (
        "FR11-IA04-001", "Order History", "FR-11", "IA-04", "Cancel Order Action Validation",
        "1. Kiểm tra đơn hàng có trạng thái 'Đang giao' (shipping).\n2. Quan sát cột Thao tác.",
        "Đơn hàng đang giao không được phép hủy; nút 'Hủy đơn' phải bị ẩn hoặc vô hiệu hóa.",
        "Failed", "Nút 'Hủy đơn' vẫn hiển thị và cho phép hủy ngay cả khi đơn hàng đã chuyển sang trạng thái 'Đang giao'.",
        "https://github.com/hoangphi117/HW03/issues/23", "", "evidence/bug_screenshots/FR11-IA04-001.png"
    )
]

# ─────────────────────────────────────────────
# STYLING CONSTANTS
# ─────────────────────────────────────────────
HEADER_FILL = PatternFill("solid", fgColor="1F4E79")
HEADER_FONT = Font(name="Calibri", bold=True, color="FFFFFF", size=11)
PASSED_FILL = PatternFill("solid", fgColor="D5F5E3")
FAILED_FILL = PatternFill("solid", fgColor="FADBD8")

THIN = Side(style="thin", color="CCCCCC")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)

# 12 Columns (Removed Check_Description, Source)
COLUMNS = [
    ("ID",               18),
    ("Screen",           26),
    ("FR_Code",           9),
    ("Aspect",            9),
    ("Category",         24),
    ("Steps_to_Test",    55),
    ("Expected_Result",  55),
    ("Status",           11),
    ("Notes",            55),
    ("Issue_URL",        38),
    ("Why_AI_Missed",    15),
    ("Screenshot",       48),
]

def apply_header(ws, cols):
    for idx, (name, width) in enumerate(cols, 1):
        cell = ws.cell(row=1, column=idx, value=name)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = CENTER
        cell.border = BORDER
        ws.column_dimensions[get_column_letter(idx)].width = width
    ws.row_dimensions[1].height = 28
    ws.freeze_panes = "A2"

def build_checklist_sheet(wb):
    ws = wb.create_sheet("Checklist")
    apply_header(ws, COLUMNS)

    for r_idx, item in enumerate(ITEMS, 2):
        status = item[7]

        for c_idx, val in enumerate(item, 1):
            cell = ws.cell(row=r_idx, column=c_idx, value=val)
            cell.border = BORDER
            cell.alignment = WRAP

            # Column 8: Status styling
            if c_idx == 8:
                cell.alignment = CENTER
                if status == "Passed":
                    cell.fill = PASSED_FILL
                    cell.font = Font(bold=True, color="196F3D")
                elif status == "Failed":
                    cell.fill = FAILED_FILL
                    cell.font = Font(bold=True, color="922B21")

            elif c_idx in (1, 3, 4):
                cell.alignment = CENTER

        ws.row_dimensions[r_idx].height = 55

def build_summary_sheet(wb):
    ws = wb.create_sheet("Test_Summary")
    ws.column_dimensions["A"].width = 35
    ws.column_dimensions["B"].width = 25

    total = len(ITEMS)
    passed = sum(1 for i in ITEMS if i[7] == "Passed")
    failed = sum(1 for i in ITEMS if i[7] == "Failed")

    rows = [
        ("Metric", "Value"),
        ("Student ID", STUDENT_ID),
        ("Target User Flow", "FR-05 → FR-06 → FR-07 → FR-09 → FR-08 → FR-11"),
        ("Total Screens Tested", 6),
        ("Total Checklist Items", total),
        ("--------------------------------", "--------------------------------"),
        ("Checklist Items Executed", total),
        ("Passed Items", f"{passed} ({passed/total*100:.1f}%)"),
        ("Failed Items", f"{failed} ({failed/total*100:.1f}%)"),
        ("Discovered GUI Bugs", failed),
        ("Bug Screenshots Captured", "25 images (across 22 bug cases)"),
        ("GitHub Issues Logged", failed),
    ]

    for r_idx, (m, v) in enumerate(rows, 1):
        ca = ws.cell(row=r_idx, column=1, value=m)
        cb = ws.cell(row=r_idx, column=2, value=v)
        ca.border = BORDER
        cb.border = BORDER
        if r_idx == 1:
            ca.font = HEADER_FONT
            cb.font = HEADER_FONT
            ca.fill = HEADER_FILL
            cb.fill = HEADER_FILL
            ca.alignment = CENTER
            cb.alignment = CENTER
        else:
            ca.font = Font(bold=True, size=11)
            cb.alignment = Alignment(horizontal="left", vertical="center")

def build_buglog_sheet(wb):
    ws = wb.create_sheet("Bug_Log")
    bug_cols = [
        ("ID", 18), ("Screen", 26), ("FR_Code", 9), ("Aspect", 9),
        ("Category", 24), ("Notes / Defect Details", 60),
        ("Issue_URL", 38), ("Screenshot Path", 48)
    ]
    apply_header(ws, bug_cols)

    failed_items = [i for i in ITEMS if i[7] == "Failed"]
    for r_idx, item in enumerate(failed_items, 2):
        vals = [item[0], item[1], item[2], item[3], item[4], item[8], item[9], item[11]]
        for c_idx, v in enumerate(vals, 1):
            cell = ws.cell(row=r_idx, column=c_idx, value=v)
            cell.border = BORDER
            cell.alignment = WRAP
            cell.fill = FAILED_FILL
            if c_idx in (1, 3, 4):
                cell.alignment = CENTER
        ws.row_dimensions[r_idx].height = 45

def main():
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    build_checklist_sheet(wb)
    build_summary_sheet(wb)
    build_buglog_sheet(wb)

    out = "checklists/HW03_GUI_Checklist.xlsx"
    wb.save(out)

    total = len(ITEMS)
    passed = sum(1 for i in ITEMS if i[7] == "Passed")
    failed = sum(1 for i in ITEMS if i[7] == "Failed")

    print(f"SUCCESS: Generated {out}")
    print(f"Total Items : {total}")
    print(f"Passed      : {passed}")
    print(f"Failed      : {failed}")

if __name__ == "__main__":
    main()
