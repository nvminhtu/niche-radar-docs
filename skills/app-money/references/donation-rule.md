# Không gây quỹ trong app — luật store

Đọc ngày **2026-09-15**. Pipeline này **không tư vấn pháp lý hay thuế** — đây là luật store trích nguyên văn và
cách làm an toàn.

## 1. Luật Apple (trích nguyên văn)

**3.2.1(vi) — được phép:**
> "Approved nonprofits may fundraise directly within their own apps or third-party apps, provided those fundraising
> campaigns adhere to all App Review Guidelines and offer Apple Pay support. These apps must disclose how the funds
> will be used, abide by all required local and federal laws, and ensure appropriate tax receipts are available to donors."

**3.2.2(iv) — không được phép:**
> "Unless you are an approved nonprofit or otherwise permitted under Section 3.2.1 (vi) above, collecting funds within
> the app for charities and fundraisers. Apps that seek to raise money for such causes must be free on the App Store
> and may only collect funds outside of the app, such as via Safari or SMS."

**2.3 — metadata chính xác:** mô tả, ảnh, thông tin phải phản ánh đúng trải nghiệm cốt lõi của app.

## 2. Luật Google Play

Payments policy (answer/9858738): quyên góp từ thiện được miễn thuế là trường hợp **không** dùng Google Play
Billing. Nghĩa là: một khoản *quyên góp* khác hẳn một khoản *mua subscription* — đừng trộn hai thứ.

## 3. Mặc định của pipeline

| Làm | Không làm |
|---|---|
| Subscription / mua đứt bán **tính năng thật** của app | gọi việc mua là "quyên góp", "ủng hộ", "donate" |
| `In-app donation: no` trong money.md | nút "Quyên góp" / "Donate" / link thanh toán gây quỹ trong app |

Checker bắt chữ quyên góp/donate: `check_money.py` (copy paywall), `check_design.py` (paywall),
`check_listing.py` + `check_macos_listing.py` (mô tả store).

## 4. Nếu thật sự muốn nhận quyên góp trong app

Chỉ đi đường này khi người dùng **là** (hoặc hợp tác với) tổ chức phi lợi nhuận đủ điều kiện Apple duyệt:
đăng ký nonprofit với Apple, dùng Apple Pay, công bố cách dùng tiền, cấp biên nhận thuế. Đây là dự án pháp lý riêng,
không nằm trong MVP. Ghi `Nonprofit approved: yes` chỉ khi đã được Apple duyệt thật.
