# AI Blindspots Reference

Edge cases and scenarios that AI models commonly miss when generating GUI
checklists. Use this list during Step 2 (Human Critical Review) to verify
coverage and add missing items.

## Category: LOCALE — Vietnamese / Regional

| ID | Missed Scenario |
| :--- | :--- |
| L-01 | Currency display: prices must use `₫` or `VNĐ` with dot-separated thousands (e.g. `1.500.000₫`) |
| L-02 | Phone number validation: Vietnamese mobile numbers start with `03x`, `05x`, `07x`, `08x`, `09x` (10 digits) |
| L-03 | Diacritics rendering: Vietnamese characters (ắ, ề, ồ, ụ) must render correctly across all fonts |
| L-04 | Date format: must follow `DD/MM/YYYY` convention, not `MM/DD/YYYY` |
| L-05 | Province/City dropdown: must include all 63 Vietnamese provinces in correct Vietnamese alphabetical order |

## Category: EDGE_CASE — Boundary Conditions

| ID | Missed Scenario |
| :--- | :--- |
| E-01 | Empty cart state: cart page shows meaningful empty-state illustration + CTA "Tiếp tục mua sắm" |
| E-02 | Out-of-stock product: "Thêm vào giỏ" button is disabled; tooltip or message explains why |
| E-03 | Coupon expired: system shows specific error "Mã giảm giá đã hết hạn" (not a generic error) |
| E-04 | Coupon already used: distinct error from "expired" — "Mã giảm giá đã được sử dụng" |
| E-05 | Search with zero results: empty-state page shown, search term is echoed back, suggestions offered |
| E-06 | Maximum cart quantity: attempting to add more than stock limit shows inline warning |
| E-07 | Long product name: names > 60 chars must truncate with ellipsis and show full title on hover/tap |
| E-08 | Very long address input: checkout form must handle 200+ char address without layout break |
| E-09 | Order with zero items: checkout button must remain disabled until cart has ≥ 1 item |
| E-10 | Same-item duplicate add: quantity increments rather than duplicating the row in cart |

## Category: PLATFORM — Device / Browser Specific

| ID | Missed Scenario |
| :--- | :--- |
| P-01 | Mobile viewport (375 px): all CTAs have minimum tap target of 44×44 px |
| P-02 | iOS Safari: `position: fixed` elements (navbar, cart drawer) do not overlap keyboard |
| P-03 | Mobile landscape: checkout form reflows correctly without horizontal scroll |
| P-04 | High-DPI (Retina): product images served at 2× resolution, not blurry |
| P-05 | Dark mode (system): if the app does not support dark mode, text remains readable on darkened backgrounds |

## Category: CONTEXT — Implicit Business Rules

| ID | Missed Scenario |
| :--- | :--- |
| C-01 | Guest checkout: unauthenticated users can still place an order (or are redirected to register with reason) |
| C-02 | Coupon + sale price: discount applies to sale price, not original price; both prices visible |
| C-03 | Order history empty state: first-time buyers see empty-state with CTA to browse products |
| C-04 | Order status labels: statuses (Pending, Confirmed, Shipping, Delivered, Cancelled) match business terminology |
| C-05 | Re-order action: order history detail page has "Mua lại" button that re-adds items to cart |

## Category: PROMPT_GAP — Structural AI Gaps

| ID | Missed Scenario |
| :--- | :--- |
| G-01 | Focus trap: modal dialogs must trap keyboard focus; Tab key cannot escape the modal |
| G-02 | Skip navigation link: "Skip to main content" link present for keyboard/screen-reader users |
| G-03 | Form autocomplete: checkout name/address fields have correct `autocomplete` attributes |
| G-04 | Scroll restoration: navigating back from PDP to listing restores scroll position |
| G-05 | Print stylesheet: order confirmation/history page renders cleanly when printed |

