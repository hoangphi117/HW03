"""
Script to create 22 GitHub issues directly on hoangphi117/HW03 in Vietnamese,
embed the corresponding screenshot(s) with raw GitHub URLs,
and update HW03_GUI_Checklist.xlsx, gui_checklist.md, and Bug_Report.md with real issue URLs.
"""

import os
import json
import base64
import time
import urllib.request
import urllib.error
import openpyxl

TOKEN = os.environ.get('GITHUB_TOKEN', '')
REPO = 'hoangphi117/HW03'
BRANCH = 'main'
HEADERS = {
    'Authorization': f'token {TOKEN}' if TOKEN else '',
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': 'HW03-Issue-Creator',
    'Content-Type': 'application/json'
}

# -------------------------------------------------------------
# 1. Upload screenshots to GitHub repository if missing
# -------------------------------------------------------------
def upload_file_if_needed(rel_path):
    filename = os.path.basename(rel_path)
    github_path = f"evidence/bug_screenshots/{filename}"
    url = f"https://api.github.com/repos/{REPO}/contents/{github_path}"

    # Check if file exists on GitHub
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            return data['download_url']
    except urllib.error.HTTPError as e:
        if e.code != 404:
            print(f"Check error {filename}:", e)

    # If 404, upload it
    local_path = os.path.join("evidence/bug_screenshots", filename)
    if not os.path.exists(local_path):
        print(f"Local file missing: {local_path}")
        return f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{github_path}"

    with open(local_path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf-8")

    payload = json.dumps({
        "message": f"docs(evidence): upload bug screenshot {filename}",
        "content": content,
        "branch": BRANCH
    }).encode("utf-8")

    put_req = urllib.request.Request(url, data=payload, headers=HEADERS, method="PUT")
    try:
        with urllib.request.urlopen(put_req) as resp:
            res = json.loads(resp.read().decode())
            print(f"Uploaded {filename} -> {res['content']['download_url']}")
            return res['content']['download_url']
    except Exception as ex:
        print(f"Upload error {filename}:", ex)
        return f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{github_path}"

# -------------------------------------------------------------
# 2. Bug definitions (22 bugs)
# -------------------------------------------------------------
BUGS = [
    {
        "id": "FR05-IA02-002",
        "screen": "Product Listing & Search",
        "fr": "FR-05",
        "aspect": "IA-02",
        "category": "Empty Search State",
        "severity": "Medium",
        "title": "[GUI Bug][FR-05][IA-02] Không có giao diện Empty State khi tìm kiếm không ra kết quả",
        "steps": [
            "Truy cập trang chủ EShop tại `http://localhost:5173/`.",
            "Tại ô tìm kiếm, nhập chuỗi ký tự không tồn tại trong hệ thống: `SanphamKhongTonTai999`.",
            "Bấm nút 'Tìm' (hoặc nhấn Enter)."
        ],
        "expected": "Hệ thống hiển thị giao diện trạng thái trống (Empty State) thân thiện, có thông báo 'Không tìm thấy sản phẩm phù hợp', gợi ý từ khóa tìm kiếm và nút 'Xem tất cả sản phẩm'.",
        "actual": "Màn hình danh sách sản phẩm bị trống trơn hoàn toàn dưới ô tìm kiếm, không có thông báo hay hướng dẫn nào cho người dùng.",
        "images": ["evidence/bug_screenshots/FR05-IA02-002.png"]
    },
    {
        "id": "FR05-IA03-001",
        "screen": "Product Listing & Search",
        "fr": "FR-05",
        "aspect": "IA-03",
        "category": "Pagination",
        "severity": "Medium",
        "title": "[GUI Bug][FR-05][IA-03] Thiếu hoàn toàn phân trang (Pagination) trên danh mục sản phẩm",
        "steps": [
            "Truy cập trang chủ EShop tại `http://localhost:5173/`.",
            "Cuộn xuống dưới cùng của danh sách sản phẩm."
        ],
        "expected": "Có thanh điều hướng phân trang (nút Trước, Sau, số trang 1, 2, ...) hoặc thanh tải thêm sản phẩm khi danh mục có nhiều mặt hàng.",
        "actual": "Trang web hoàn toàn không có bất kỳ bộ điều khiển phân trang nào; toàn bộ sản phẩm hiển thị chung trên một trang.",
        "images": ["evidence/bug_screenshots/FR05-IA03-001.png"]
    },
    {
        "id": "FR05-IA03-002",
        "screen": "Product Listing & Search",
        "fr": "FR-05",
        "aspect": "IA-03",
        "category": "Filter & Sorting",
        "severity": "Medium",
        "title": "[GUI Bug][FR-05][IA-03] Thiếu bộ lọc theo danh mục và sắp xếp sản phẩm theo giá",
        "steps": [
            "Truy cập trang chủ EShop tại `http://localhost:5173/`.",
            "Tìm kiếm thanh bộ lọc danh mục (Điện thoại, Laptop, Phụ kiện) hoặc dropdown sắp xếp giá."
        ],
        "expected": "Có thanh bộ lọc danh mục trực quan và menu chọn sắp xếp theo giá (Tăng dần / Giảm dần) hoạt động mượt mà.",
        "actual": "Giao diện không cung cấp bất kỳ bộ lọc danh mục hay dropdown sắp xếp nào cho người dùng.",
        "images": ["evidence/bug_screenshots/FR05-IA03-002.png"]
    },
    {
        "id": "FR05-IA04-001",
        "screen": "Product Listing & Search",
        "fr": "FR-05",
        "aspect": "IA-04",
        "category": "Loading State",
        "severity": "Low",
        "title": "[GUI Bug][FR-05][IA-04] Thiếu hiệu ứng Skeleton loading / Spinner khi tải danh sách sản phẩm",
        "steps": [
            "Mở DevTools trình duyệt, chọn tab Network và cấu hình throttling sang 'Slow 3G'.",
            "Tải lại trang chủ `http://localhost:5173/`."
        ],
        "expected": "Hiển thị khung hình chờ (Skeleton loader) hoặc vòng xoay spinner cho biết dữ liệu đang được tải về.",
        "actual": "Màn hình bị trắng một khoảng thời gian mà không có bất kỳ chỉ báo loading nào, gây cảm giác trang bị treo.",
        "images": ["evidence/bug_screenshots/FR05-IA04-001.png"]
    },
    {
        "id": "FR05-IA04-002",
        "screen": "Product Listing & Search",
        "fr": "FR-05",
        "aspect": "IA-04",
        "category": "Scroll Restoration",
        "severity": "Low",
        "title": "[GUI Bug][FR-05][IA-04] Vị trí cuộn trang bị reset về đầu trang khi quay lại từ trang chi tiết sản phẩm",
        "steps": [
            "Tại trang danh sách sản phẩm, cuộn chuột xuống dưới cùng của danh sách.",
            "Bấm 'Xem chi tiết' một sản phẩm ở cuối trang.",
            "Tại trang chi tiết, bấm nút Back của trình duyệt để quay về danh sách."
        ],
        "expected": "Vị trí cuộn của trang danh sách sản phẩm được giữ nguyên tại vị trí sản phẩm vừa xem (Scroll restoration).",
        "actual": "Vị trí cuộn bị đẩy ngược về đỉnh trang (top 0), người dùng phải cuộn lại từ đầu để tiếp tục duyệt hàng.",
        "images": ["evidence/bug_screenshots/FR05-IA04-002-1.png", "evidence/bug_screenshots/FR05-IA04-002-2.png"]
    },
    {
        "id": "FR06-IA02-001",
        "screen": "Product Detail",
        "fr": "FR-06",
        "aspect": "IA-02",
        "category": "Variant Selector",
        "severity": "Medium",
        "title": "[GUI Bug][FR-06][IA-02] Thiếu bộ chọn biến thể (màu sắc, kích cỡ, dung lượng) trên trang chi tiết sản phẩm",
        "steps": [
            "Bấm vào xem chi tiết một sản phẩm công nghệ (ví dụ iPhone 15 Pro Max tại `/product/1`).",
            "Tìm khu vực chọn màu sắc, dung lượng bộ nhớ hoặc phiên bản."
        ],
        "expected": "Có các nút chọn biến thể (ví dụ 128GB, 256GB; Màu Titan tự nhiên, Titan xanh) có trạng thái chọn rõ ràng.",
        "actual": "Trang chi tiết chỉ có duy nhất ô nhập số lượng, hoàn toàn không có lựa chọn biến thể sản phẩm.",
        "images": ["evidence/bug_screenshots/FR06-IA02-001.png"]
    },
    {
        "id": "FR06-IA03-001",
        "screen": "Product Detail",
        "fr": "FR-06",
        "aspect": "IA-03",
        "category": "Breadcrumbs Navigation",
        "severity": "Medium",
        "title": "[GUI Bug][FR-06][IA-03] Thiếu thanh điều hướng phân cấp Breadcrumb trên trang chi tiết sản phẩm",
        "steps": [
            "Truy cập vào trang chi tiết sản phẩm bất kỳ.",
            "Quan sát đầu trang phía trên tên sản phẩm."
        ],
        "expected": "Hiển thị thanh Breadcrumb phân cấp: 'Trang chủ > Danh mục > Tên sản phẩm' giúp người dùng định vị và điều hướng nhanh.",
        "actual": "Hoàn toàn không có thanh điều hướng Breadcrumb.",
        "images": ["evidence/bug_screenshots/FR06-IA03-001.png"]
    },
    {
        "id": "FR06-IA03-002",
        "screen": "Product Detail",
        "fr": "FR-06",
        "aspect": "IA-03",
        "category": "Back Navigation",
        "severity": "Low",
        "title": "[GUI Bug][FR-06][IA-03] Thiếu nút quay lại danh mục sản phẩm trên trang chi tiết",
        "steps": [
            "Truy cập trang chi tiết sản phẩm `/product/1`.",
            "Tìm nút bấm quay lại danh sách sản phẩm trên giao diện."
        ],
        "expected": "Có nút '← Quay lại' hoặc liên kết rõ ràng giúp người dùng trở về danh sách sản phẩm.",
        "actual": "Không có nút quay lại; người dùng buộc phải bấm nút Back của trình duyệt hoặc click vào logo Header.",
        "images": ["evidence/bug_screenshots/FR06-IA03-002.png"]
    },
    {
        "id": "FR06-IA04-001",
        "screen": "Product Detail",
        "fr": "FR-06",
        "aspect": "IA-04",
        "category": "Add to Cart Feedback",
        "severity": "Critical",
        "title": "[GUI Bug][FR-06][IA-04] Click lần đầu vào nút 'Thêm vào giỏ hàng' bị nuốt sự kiện, phải click 2 lần",
        "steps": [
            "Truy cập trang chi tiết sản phẩm `/product/1`.",
            "Click chuột một lần vào nút 'Thêm vào giỏ hàng'.",
            "Quan sát giao diện và kiểm tra số lượng món trong giỏ hàng."
        ],
        "expected": "Sản phẩm phải được thêm ngay lập tức vào giỏ hàng từ lần click đầu tiên, hiển thị phản hồi 'Đã thêm'.",
        "actual": "Lần click đầu tiên bị nuốt hoàn toàn do logic `if (clickCount === 0) return;`. Người dùng không thấy phản hồi gì và bắt buộc phải click lần thứ 2 mới thêm được hàng.",
        "images": ["evidence/bug_screenshots/FR06-IA04-001-1.png", "evidence/bug_screenshots/FR06-IA04-001-2.png"]
    },
    {
        "id": "FR07-IA02-001",
        "screen": "Shopping Cart",
        "fr": "FR-07",
        "aspect": "IA-02",
        "category": "Quantity Stepper Input",
        "severity": "High",
        "title": "[GUI Bug][FR-07][IA-02] Số lượng trong giỏ hàng là text tĩnh, không thể tăng giảm hoặc chỉnh sửa",
        "steps": [
            "Thêm sản phẩm vào giỏ hàng và truy cập `/cart`.",
            "Quan sát cột 'Số lượng' trong bảng giỏ hàng.",
            "Thử tìm ô nhập số lượng hoặc nút tăng/giảm (+ / -)."
        ],
        "expected": "Có ô input hoặc cặp nút +/- cho phép thay đổi số lượng trực tiếp trong giỏ, tổng tiền cập nhật tức thì.",
        "actual": "Số lượng chỉ là một đoạn text tĩnh `<td>{item.quantity}</td>`, không cho chỉnh sửa. Người dùng muốn đổi số lượng phải xóa đi và thêm lại từ đầu.",
        "images": ["evidence/bug_screenshots/FR07-IA02-001.png"]
    },
    {
        "id": "FR09-IA02-001",
        "screen": "Discount Coupons",
        "fr": "FR-09",
        "aspect": "IA-02",
        "category": "Percentage Coupon Calculation",
        "severity": "Critical",
        "title": "[GUI Bug][FR-09][IA-02] Lỗi tính mã giảm giá %: số tiền giảm bị âm làm tổng tiền thanh toán tăng gấp 10 lần",
        "steps": [
            "Thêm sản phẩm có giá trị lớn (ví dụ iPhone 15 trị giá 30.000.000₫) vào giỏ hàng.",
            "Chuyển sang trang thanh toán `/checkout`.",
            "Tại ô 'Mã Giảm Giá', nhập mã hợp lệ: `SAVE10` (giảm giá 10%).",
            "Bấm nút 'Áp dụng'."
        ],
        "expected": "Tiết kiệm 3.000.000 ₫ (10%), tổng thanh toán giảm từ 30.000.000 ₫ xuống còn 27.000.000 ₫.",
        "actual": "Backend tính `total * (1 - coupon.discount_value)` dẫn đến số tiền giảm giá bị âm: `Tiết kiệm: -270.000.000 ₫` và tổng tiền thanh toán tăng vọt thành `300.000.000 ₫` (gấp 10 lần).",
        "images": ["evidence/bug_screenshots/FR09-IA02-001.png"]
    },
    {
        "id": "FR09-IA03-001",
        "screen": "Discount Coupons",
        "fr": "FR-09",
        "aspect": "IA-03",
        "category": "Remove Applied Coupon",
        "severity": "Medium",
        "title": "[GUI Bug][FR-09][IA-03] Không có nút hủy hoặc gỡ mã giảm giá sau khi đã áp dụng",
        "steps": [
            "Tại màn hình checkout, áp dụng thành công một mã giảm giá.",
            "Tìm nút hủy mã (nút 'Hủy', 'Gỡ bỏ' hoặc icon X)."
        ],
        "expected": "Có nút cho phép người dùng gỡ mã giảm giá, sau khi gỡ tổng tiền hoàn về giá trị ban đầu.",
        "actual": "Không có nút hủy/gỡ mã giảm giá đã áp dụng. Người dùng không thể xóa mã nếu muốn đổi ý.",
        "images": ["evidence/bug_screenshots/FR09-IA03-001.png"]
    },
    {
        "id": "FR08-IA02-001",
        "screen": "Checkout",
        "fr": "FR-08",
        "aspect": "IA-02",
        "category": "Shipping Address Form",
        "severity": "Critical",
        "title": "[GUI Bug][FR-08][IA-02] Màn hình thanh toán thiếu hoàn toàn form nhập thông tin giao hàng",
        "steps": [
            "Truy cập vào màn hình thanh toán `/checkout`.",
            "Tìm các ô nhập thông tin người nhận hàng: Họ tên, Số điện thoại nhận hàng, Địa chỉ giao hàng."
        ],
        "expected": "Có form thông tin giao hàng với đầy đủ các trường bắt buộc và validation thời gian thực.",
        "actual": "Trang thanh toán hoàn toàn không có form nhập địa chỉ giao hàng; chỉ có danh sách hàng và nút thanh toán.",
        "images": ["evidence/bug_screenshots/FR08-IA02-001.png"]
    },
    {
        "id": "FR08-IA02-003",
        "screen": "Checkout",
        "fr": "FR-08",
        "aspect": "IA-02",
        "category": "Total Price Input Security",
        "severity": "Critical",
        "title": "[GUI Bug][FR-08][IA-02] LỖI BẢO MẬT: Tổng tiền thanh toán là ô input cho phép người dùng tự sửa giá tùy ý",
        "steps": [
            "Tại trang `/checkout`, quan sát ô 'Tổng tiền thanh toán (VND)'.",
            "Xóa số tiền hiện tại và nhập vào giá trị bất kỳ: `1000`.",
            "Bấm 'Xác Nhận Thanh Toán'."
        ],
        "expected": "Tổng tiền phải là nhãn văn bản tĩnh (read-only), không cho phép chỉnh sửa từ phía client dưới bất kỳ hình thức nào.",
        "actual": "Tổng tiền lại là một thẻ `<input type='number'>` cho phép người dùng tự gõ số tiền tùy ý và đặt hàng thành công với giá 1.000₫.",
        "images": ["evidence/bug_screenshots/FR08-IA02-003.png"]
    },
    {
        "id": "FR08-IA02-004",
        "screen": "Checkout",
        "fr": "FR-08",
        "aspect": "IA-02",
        "category": "Payment Method Selection",
        "severity": "High",
        "title": "[GUI Bug][FR-08][IA-02] Thiếu tùy chọn phương thức thanh toán (COD / Chuyển khoản ngân hàng)",
        "steps": [
            "Tại màn hình checkout, tìm khu vực lựa chọn phương thức thanh toán."
        ],
        "expected": "Có các tùy chọn phương thức thanh toán (Thanh toán khi nhận hàng - COD, Chuyển khoản ngân hàng, Ví điện tử) để người mua lựa chọn.",
        "actual": "Không có bất kỳ tùy chọn phương thức thanh toán nào trên giao diện checkout.",
        "images": ["evidence/bug_screenshots/FR08-IA02-004.png"]
    },
    {
        "id": "FR08-IA03-001",
        "screen": "Checkout",
        "fr": "FR-08",
        "aspect": "IA-03",
        "category": "Checkout Progress Indicator",
        "severity": "Medium",
        "title": "[GUI Bug][FR-08][IA-03] Thiếu thanh tiến trình các bước mua hàng (Checkout Step Indicator)",
        "steps": [
            "Quan sát đầu trang xác nhận đơn hàng tại `/checkout`."
        ],
        "expected": "Có thanh tiến trình trực quan hiển thị các giai đoạn (Giỏ hàng -> Thông tin giao hàng -> Thanh toán -> Hoàn tất).",
        "actual": "Không có thanh chỉ báo tiến trình các bước, người dùng không nắm được mình đang ở bước nào trong quy trình thanh toán.",
        "images": ["evidence/bug_screenshots/FR08-IA03-001.png"]
    },
    {
        "id": "FR08-IA03-002",
        "screen": "Checkout",
        "fr": "FR-08",
        "aspect": "IA-03",
        "category": "Back to Cart Link",
        "severity": "Low",
        "title": "[GUI Bug][FR-08][IA-03] Thiếu liên kết quay lại giỏ hàng từ màn hình thanh toán",
        "steps": [
            "Tại trang `/checkout`, tìm liên kết hoặc nút bấm quay lại giỏ hàng."
        ],
        "expected": "Có liên kết '← Quay lại giỏ hàng' giúp người dùng dễ dàng kiểm tra hoặc điều chỉnh sản phẩm.",
        "actual": "Không có nút hoặc link quay lại giỏ hàng; người dùng bị kẹt trong màn hình thanh toán.",
        "images": ["evidence/bug_screenshots/FR08-IA03-002.png"]
    },
    {
        "id": "FR08-IA04-002",
        "screen": "Checkout",
        "fr": "FR-08",
        "aspect": "IA-04",
        "category": "Post-checkout Cart State Reset",
        "severity": "High",
        "title": "[GUI Bug][FR-08][IA-04] Giỏ hàng không được làm rỗng sau khi đặt hàng thành công",
        "steps": [
            "Hoàn tất đặt hàng thành công trên màn hình `/checkout` (hiện thông báo 'Thanh toán thành công!').",
            "Bấm vào mục 'Giỏ hàng' trên thanh Menu Header."
        ],
        "expected": "Giỏ hàng phải được làm rỗng hoàn toàn (`cart = []`), hiển thị trạng thái 'Giỏ hàng của bạn đang trống'.",
        "actual": "Hàm `clearCart()` không được gọi; các sản phẩm vừa mua vẫn nằm nguyên trong giỏ hàng, dễ gây đặt trùng đơn.",
        "images": ["evidence/bug_screenshots/FR08-IA04-002-1.png", "evidence/bug_screenshots/FR08-IA04-002-2.png"]
    },
    {
        "id": "FR11-IA02-001",
        "screen": "Order History",
        "fr": "FR-11",
        "aspect": "IA-02",
        "category": "Order Details Breakdown",
        "severity": "High",
        "title": "[GUI Bug][FR-11][IA-02] Không thể bấm vào xem chi tiết danh sách sản phẩm trong đơn hàng đã đặt",
        "steps": [
            "Truy cập vào trang Hồ sơ / Lịch sử đơn hàng tại `/profile`.",
            "Click vào mã đơn hàng hoặc dòng đơn hàng trong bảng."
        ],
        "expected": "Mở popup hoặc trang chi tiết đơn hàng hiển thị danh sách các món hàng đã mua, số lượng, đơn giá và địa chỉ nhận hàng.",
        "actual": "Bảng đơn hàng chỉ hiển thị text tĩnh; không có chức năng xem chi tiết đơn hàng khiến người dùng không biết trong đơn gồm những sản phẩm nào.",
        "images": ["evidence/bug_screenshots/FR11-IA02-001.png"]
    },
    {
        "id": "FR11-IA03-001",
        "screen": "Order History",
        "fr": "FR-11",
        "aspect": "IA-03",
        "category": "Re-order Quick CTA",
        "severity": "Medium",
        "title": "[GUI Bug][FR-11][IA-03] Thiếu tính năng 'Mua lại' (Re-order) các sản phẩm từ đơn hàng cũ",
        "steps": [
            "Tại trang Lịch sử đơn hàng `/profile`, kiểm tra các đơn đã giao thành công."
        ],
        "expected": "Có nút 'Mua lại' (Re-order) cho phép thêm nhanh toàn bộ các món trong đơn cũ vào giỏ hàng hiện tại.",
        "actual": "Không có nút 'Mua lại'; người mua muốn đặt lại phải tự tìm kiếm từng món từ đầu.",
        "images": ["evidence/bug_screenshots/FR11-IA03-001.png"]
    },
    {
        "id": "FR11-IA03-002",
        "screen": "Order History",
        "fr": "FR-11",
        "aspect": "IA-03",
        "category": "Checkout Success Navigation Link",
        "severity": "Low",
        "title": "[GUI Bug][FR-11][IA-03] Màn hình đặt hàng thành công thiếu nút liên kết xem đơn trong Lịch sử đơn hàng",
        "steps": [
            "Đặt hàng thành công và dừng tại màn hình 'Thanh toán thành công!'.",
            "Quan sát các liên kết điều hướng trên màn hình."
        ],
        "expected": "Có nút 'Xem đơn hàng của bạn' dẫn trực tiếp đến `/profile` để theo dõi tình trạng đơn vừa tạo.",
        "actual": "Chỉ có duy nhất một nút 'Quay lại trang chủ', không có liên kết nào dẫn tới trang Lịch sử đơn hàng.",
        "images": ["evidence/bug_screenshots/FR11-IA03-002.png"]
    },
    {
        "id": "FR11-IA04-001",
        "screen": "Order History",
        "fr": "FR-11",
        "aspect": "IA-04",
        "category": "Cancel Order Action Validation",
        "severity": "High",
        "title": "[GUI Bug][FR-11][IA-04] Nút 'Hủy đơn' vẫn cho phép hủy khi đơn hàng đã chuyển sang trạng thái đang giao",
        "steps": [
            "Tại trang `/profile`, tìm đơn hàng đang có trạng thái 'Đang giao' (`shipping`).",
            "Quan sát cột Thao tác và bấm nút 'Hủy đơn'."
        ],
        "expected": "Đơn hàng đang giao không được phép hủy từ phía khách hàng; nút 'Hủy đơn' phải bị ẩn hoặc vô hiệu hóa.",
        "actual": "Nút 'Hủy đơn' vẫn hiển thị và cho phép hủy thành công đơn hàng đang giao (`o.status !== 'delivered' && o.status !== 'canceled'`).",
        "images": ["evidence/bug_screenshots/FR11-IA04-001.png"]
    }
]

# -------------------------------------------------------------
# 3. Create issues via GitHub REST API
# -------------------------------------------------------------
def create_issue(bug, img_urls):
    images_markdown = ""
    for idx, u in enumerate(img_urls, 1):
        if len(img_urls) > 1:
            images_markdown += f"**Ảnh minh chứng {idx}:**\n![Ảnh minh chứng {idx}]({u})\n\n"
        else:
            images_markdown += f"![Ảnh minh chứng]({u})\n\n"

    steps_text = "\n".join([f"{idx}. {step}" for idx, step in enumerate(bug['steps'], 1)])

    body = f"""## 📌 Thông Tin Lỗi GUI (GUI Bug Report)

* **Mã Checklist Item:** `{bug['id']}`
* **Màn hình / Tính năng:** `{bug['screen']}` ({bug['fr']})
* **Khía cạnh kiểm thử:** `{bug['aspect']}`
* **Phân loại:** {bug['category']}
* **Mức độ nghiêm trọng:** `{bug['severity']}`
* **Người báo cáo:** MSSV `23120320`

---

## 🔁 Các bước tái hiện (Steps to Reproduce)

{steps_text}

---

## 🎯 Kết quả kỳ vọng (Expected Result)

{bug['expected']}

---

## ❌ Kết quả thực tế (Actual Result)

{bug['actual']}

---

## 📸 Ảnh chụp minh chứng (Screenshot Evidence)

{images_markdown}

---
*Ghi chú: Lỗi được phát hiện trong quá trình kiểm thử GUI & Usability (HW03) trên ứng dụng EShop SUT.*
"""

    payload = json.dumps({
        "title": bug['title'],
        "body": body,
        "labels": ["bug", f"severity:{bug['severity'].lower()}", bug['fr'], bug['aspect']]
    }).encode("utf-8")

    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/issues",
        data=payload,
        headers=HEADERS,
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            return data['html_url'], data['number']
    except Exception as e:
        print(f"Error creating issue for {bug['id']}:", e)
        return None, None

def main():
    print(f"Bắt đầu tải ảnh lên repo {REPO} và tạo 22 GitHub Issues...")

    # Upload all screenshots first
    uploaded_urls = {}
    all_image_paths = set()
    for b in BUGS:
        for img in b['images']:
            all_image_paths.add(img)

    for p in sorted(all_image_paths):
        u = upload_file_if_needed(p)
        uploaded_urls[p] = u
        time.sleep(0.5)

    print("Đã hoàn tất kiểm tra và tải ảnh lên GitHub.")

    # Create issues
    issue_map = {}
    for idx, b in enumerate(BUGS, 1):
        img_urls = [uploaded_urls[img] for img in b['images']]
        url, num = create_issue(b, img_urls)
        if url:
            print(f"[{idx}/22] Đã tạo Issue #{num}: {b['id']} -> {url}")
            issue_map[b['id']] = url
        else:
            print(f"[{idx}/22] Lỗi tạo issue: {b['id']}")
        time.sleep(1) # avoid rate limits

    # Save mapping to file
    with open("scripts/created_issues.json", "w", encoding="utf-8") as f:
        json.dump(issue_map, f, indent=2, ensure_ascii=False)

    print("Hoàn tất tạo 22 issues!")

if __name__ == "__main__":
    main()

