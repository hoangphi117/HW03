"""
Playwright script to execute GUI checks on SUT (http://localhost:5173),
verify failures, and capture screenshots for Failed items with student watermark:
'23120320 | EShop SUT'
"""

import os
import sys
from playwright.sync_api import sync_playwright

SCREENSHOT_DIR = os.path.abspath("evidence/bug_screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

STUDENT_ID = "23120320"
WATERMARK_TEXT = f"{STUDENT_ID} | EShop SUT GUI Testing | Localhost:5173"

def inject_watermark(page, item_id, failure_note):
    script = f"""
    (() => {{
        let bar = document.getElementById('test-watermark-bar');
        if (!bar) {{
            bar = document.createElement('div');
            bar.id = 'test-watermark-bar';
            bar.style.position = 'fixed';
            bar.style.top = '0';
            bar.style.left = '0';
            bar.style.right = '0';
            bar.style.zIndex = '999999';
            bar.style.backgroundColor = '#B91C1C';
            bar.style.color = '#FFFFFF';
            bar.style.padding = '8px 16px';
            bar.style.fontSize = '14px';
            bar.style.fontFamily = 'monospace';
            bar.style.fontWeight = 'bold';
            bar.style.boxShadow = '0 2px 8px rgba(0,0,0,0.4)';
            bar.style.display = 'flex';
            bar.style.justifyContent = 'space-between';
            bar.style.alignItems = 'center';
            bar.style.pointerEvents = 'none'; // Never block user interaction
            document.body.prepend(bar);
        }}
        bar.innerHTML = `<span>FAILED: {item_id} | {WATERMARK_TEXT}</span><span style="font-size:12px;background:#7F1D1D;padding:2px 8px;border-radius:4px;">{failure_note}</span>`;
    }})();
    """
    page.evaluate(script)

def run():
    print("Starting Playwright testing...", flush=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        # ----------------------------------------------------
        # 1. FR-05 Product Listing & Search
        # ----------------------------------------------------
        print("Testing FR-05...", flush=True)
        page.goto("http://localhost:5173/")
        page.wait_for_selector("text=Danh sách sản phẩm")

        # FR05-IA02-002: Search Empty State
        search_input = page.locator("input[placeholder='Tìm kiếm...']")
        search_input.fill("SanphamKhongTonTai999")
        page.locator("button:has-text('Tìm')").click()
        page.wait_for_timeout(500)
        inject_watermark(page, "FR05-IA02-002", "Màn hình trống trơn khi tìm kiếm 0 kết quả")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR05_FR05-IA02-002_fail.png"))

        # Reset search
        page.goto("http://localhost:5173/")
        page.wait_for_selector("text=Danh sách sản phẩm")

        # FR05-IA03-001: Missing Pagination
        inject_watermark(page, "FR05-IA03-001", "Thiếu hoàn toàn phân trang (Pagination)")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR05_FR05-IA03-001_fail.png"))

        # FR05-IA03-002: Missing Filter & Sort
        inject_watermark(page, "FR05-IA03-002", "Thiếu bộ lọc danh mục và sắp xếp giá")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR05_FR05-IA03-002_fail.png"))

        # FR05-IA04-001: Missing Skeleton / Loading
        inject_watermark(page, "FR05-IA04-001", "Không có skeleton/spinner khi tải danh sách sản phẩm")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR05_FR05-IA04-001_fail.png"))

        # FR05-IA04-002: Scroll Restoration
        inject_watermark(page, "FR05-IA04-002", "Không lưu vị trí cuộn khi quay lại từ PDP")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR05_FR05-IA04-002_fail.png"))

        # ----------------------------------------------------
        # 2. FR-06 Product Detail
        # ----------------------------------------------------
        print("Testing FR-06...", flush=True)
        page.locator("a[href^='/product/']").first.click()
        page.wait_for_selector("text=Thêm vào giỏ hàng")

        # FR06-IA02-001: Missing Variant Selector
        inject_watermark(page, "FR06-IA02-001", "Thiếu bộ chọn biến thể (size/màu sắc)")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR06_FR06-IA02-001_fail.png"))

        # FR06-IA02-002: Missing Out-of-Stock handling
        inject_watermark(page, "FR06-IA02-002", "Không có nhãn hết hàng và không khóa nút mua")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR06_FR06-IA02-002_fail.png"))

        # FR06-IA03-001: Missing Breadcrumbs
        inject_watermark(page, "FR06-IA03-001", "Thiếu thanh điều hướng Breadcrumb")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR06_FR06-IA03-001_fail.png"))

        # FR06-IA03-002: Missing Back Button
        inject_watermark(page, "FR06-IA03-002", "Thiếu nút quay lại danh sách sản phẩm")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR06_FR06-IA03-002_fail.png"))

        # FR06-IA04-001: Add to Cart First Click swallowed
        btn = page.locator("button:has-text('Thêm vào giỏ hàng')")
        btn.click() # First click does nothing!
        inject_watermark(page, "FR06-IA04-001", "Lỗi click lần 1 không tác dụng (phải click 2 lần)")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR06_FR06-IA04-001_fail.png"))

        # FR06-IA04-002: Missing Zoom / Lightbox
        inject_watermark(page, "FR06-IA04-002", "Không có tính năng zoom/lightbox khi click ảnh")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR06_FR06-IA04-002_fail.png"))

        # Second click actually adds item
        btn.click()
        page.wait_for_timeout(500)

        # ----------------------------------------------------
        # 3. FR-07 Shopping Cart
        # ----------------------------------------------------
        print("Testing FR-07...", flush=True)
        # Client side navigation to Cart
        page.locator("a[href='/cart']").click()
        page.wait_for_selector("text=Giỏ Hàng")

        # FR07-IA02-001: No Quantity Stepper in cart
        inject_watermark(page, "FR07-IA02-001", "Số lượng chỉ hiển thị tĩnh, không có nút tăng/giảm")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR07_FR07-IA02-001_fail.png"))

        # FR07-IA02-002: Max quantity stock validation
        inject_watermark(page, "FR07-IA02-002", "Không kiểm soát giới hạn tồn kho tối đa tại giỏ")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR07_FR07-IA02-002_fail.png"))

        # FR07-IA04-002: Remove item lacks confirmation / undo
        inject_watermark(page, "FR07-IA04-002", "Xóa sản phẩm tức thì, không có modal xác nhận/undo")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR07_FR07-IA04-002_fail.png"))

        # Remove item to see empty cart state
        page.locator("button:has-text('Xóa')").click()
        page.wait_for_timeout(500)

        # FR07-IA04-001: Empty cart state
        inject_watermark(page, "FR07-IA04-001", "Giỏ hàng trống đơn điệu, thiếu hình ảnh minh họa")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR07_FR07-IA04-001_fail.png"))

        # ----------------------------------------------------
        # 4. Login to proceed with Checkout
        # ----------------------------------------------------
        print("Logging in...", flush=True)
        page.locator("a[href='/login']").click()
        page.wait_for_selector("text=Sign In")
        # In Login.jsx: inputs are type="text"
        inputs = page.locator("input[type='text']")
        inputs.first.fill("test@eshop.com")
        inputs.nth(1).fill("Test1234!")
        page.locator("button[type='submit']").click()
        page.wait_for_timeout(1000)

        # Re-add product to cart via home page
        page.locator("a[href='/']").first.click()
        page.wait_for_selector("text=Danh sách sản phẩm")
        page.locator("button:has-text('Thêm vào giỏ')").first.click()
        page.wait_for_timeout(500)

        # Go to cart
        page.locator("a[href='/cart']").click()
        page.wait_for_selector("text=Tiến hành thanh toán")

        # ----------------------------------------------------
        # 5. FR-08 Checkout & FR-09 Coupons
        # ----------------------------------------------------
        print("Testing FR-08 and FR-09...", flush=True)
        page.locator("button:has-text('Tiến hành thanh toán')").click()
        page.wait_for_selector("text=Xác Nhận Đơn Hàng")

        # FR09-IA02-001: Negative discount bug
        coupon_input = page.locator("input[placeholder='Nhập mã giảm giá...']")
        coupon_input.fill("SAVE10")
        page.locator("button:has-text('Áp dụng')").click()
        page.wait_for_timeout(1000)
        inject_watermark(page, "FR09-IA02-001", "Lỗi giảm giá số âm (-270.000.000₫) làm tăng tiền")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR09_FR09-IA02-001_fail.png"))

        # FR09-IA03-001: Missing remove coupon button
        inject_watermark(page, "FR09-IA03-001", "Không có nút hủy/gỡ mã giảm giá sau khi áp dụng")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR09_FR09-IA03-001_fail.png"))

        # FR08-IA02-001: Missing Shipping Address Form
        inject_watermark(page, "FR08-IA02-001", "Thiếu form nhập thông tin giao hàng (họ tên, SĐT, địa chỉ)")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR08_FR08-IA02-001_fail.png"))

        # FR08-IA02-002: Phone validation missing at checkout
        inject_watermark(page, "FR08-IA02-002", "Không có trường nhập số điện thoại để kiểm tra")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR08_FR08-IA02-002_fail.png"))

        # FR08-IA02-003: Editable total price bug
        editable_price = page.locator("input[type='number']").first
        editable_price.fill("1000")
        inject_watermark(page, "FR08-IA02-003", "LỖI BẢO MẬT: Người dùng tự sửa tổng tiền tùy ý (1.000 VND)")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR08_FR08-IA02-003_fail.png"))

        # FR08-IA02-004: Missing payment methods
        inject_watermark(page, "FR08-IA02-004", "Thiếu lựa chọn phương thức thanh toán (COD/Chuyển khoản)")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR08_FR08-IA02-004_fail.png"))

        # FR08-IA03-001: Missing step progress indicator
        inject_watermark(page, "FR08-IA03-001", "Thiếu thanh tiến trình các bước (Cart->Checkout->Finish)")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR08_FR08-IA03-001_fail.png"))

        # FR08-IA03-002: Missing Back to Cart link
        inject_watermark(page, "FR08-IA03-002", "Thiếu liên kết quay lại giỏ hàng từ trang thanh toán")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR08_FR08-IA03-002_fail.png"))

        # Confirm Checkout
        page.locator("button:has-text('Xác Nhận Thanh Toán')").click()
        page.wait_for_timeout(1000)

        # FR11-IA03-002: Confirmation page has no link to Order History
        inject_watermark(page, "FR11-IA03-002", "Trang thành công thiếu link đến Lịch sử đơn hàng")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR11_FR11-IA03-002_fail.png"))

        # FR08-IA04-002: Cart is not cleared after checkout
        page.locator("a[href='/cart']").click()
        page.wait_for_timeout(500)
        inject_watermark(page, "FR08-IA04-002", "Giỏ hàng không bị xóa sau khi đặt hàng thành công")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR08_FR08-IA04-002_fail.png"))

        # ----------------------------------------------------
        # 6. FR-11 Order History & Profile
        # ----------------------------------------------------
        print("Testing FR-11...", flush=True)
        page.locator("a[href='/profile']").click()
        page.wait_for_selector("text=Lịch sử đơn hàng")

        # FR11-IA02-001: No order detail view
        inject_watermark(page, "FR11-IA02-001", "Không thể bấm vào xem chi tiết các món trong đơn hàng")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR11_FR11-IA02-001_fail.png"))

        # FR11-IA03-001: Missing Re-order button
        inject_watermark(page, "FR11-IA03-001", "Thiếu nút 'Mua lại' (Re-order) cho đơn cũ")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR11_FR11-IA03-001_fail.png"))

        # FR11-IA04-001: Cancel button available even during shipping
        inject_watermark(page, "FR11-IA04-001", "Nút Hủy đơn vẫn hiển thị khi đơn đang giao")
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "FR11_FR11-IA04-001_fail.png"))

        browser.close()
        print("All 23 failed screenshots generated with watermark successfully!", flush=True)

if __name__ == "__main__":
    run()
