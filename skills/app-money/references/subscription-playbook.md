# Subscription playbook — luật store + cách định giá cho app đầu tay

Luật trích từ nguồn gốc, đọc ngày **2026-09-15**; phí + luật Mỹ/EU cập nhật **2026-09-30** (§3, §5, §7). Phần kinh nghiệm ghi *(thực hành phổ biến)* — không phải số đo,
đừng trích như sự thật.

## 1. Luật Apple bắt buộc

Nguồn: developer.apple.com/app-store/review/guidelines

| Mục | Nội dung (trích) | Hệ quả cho app |
|---|---|---|
| 3.1.1 | "If you want to unlock features or functionality within your app, (by way of example: subscriptions ...), you must use in-app purchase." | Mở Pro bằng IAP (RevenueCat bọc StoreKit) — không mã kích hoạt. Link ra web mua: **chỉ storefront Mỹ** (và EU theo điều khoản EU, có phí) — xem §3 + `growth:direct-sales` |
| 3.1.2(a) | "you must provide ongoing value to the customer, and the subscription period must last at least seven days and be available across all of the user's devices." | chu kỳ ≥ 7 ngày · Pro phải là giá trị lặp lại · mua trên iPhone dùng được trên iPad cùng Apple ID |
| 3.1.2(c) | "Before asking a customer to subscribe, you should clearly describe what the user will get for the price." | paywall nói rõ Pro gồm gì, giá theo chu kỳ |
| Schedule 2 (hợp đồng Paid Apps) | tên gói, chu kỳ, giá, link Privacy Policy + Terms of Use (EULA) trong app và trong metadata | paywall có 2 link; listing có Terms URL (hoặc EULA chuẩn của Apple) |
| Restore | app IAP phải cho khôi phục giao dịch | nút Restore trên paywall + Settings |
| 5.1.1(v) | "If your app supports account creation, you must also offer account deletion within the app." | có đăng nhập → có nút xoá tài khoản |
| 2.3.1(a) | không tính năng ẩn; thay đổi phải ghi cụ thể trong Review Notes | Review Notes ghi cách test subscription |

## 2. Luật Google Play bắt buộc

Nguồn: support.google.com/googleplay/android-developer/answer/9858738 (Payments) · answer/140504 (Subscriptions)

- Tính năng số trong app → **Google Play Billing** (RevenueCat bọc Play Billing Library).
- Paywall phải nói rõ giá, chu kỳ, việc tự gia hạn, cách huỷ; trial phải nói khi nào bắt đầu trừ tiền.
- Link quản lý subscription: `https://play.google.com/store/account/subscriptions`.

## 3. Phí

| Store | Phí subscription | Nguồn |
|---|---|---|
| Apple — Small Business Program (doanh thu < 1 triệu USD/năm, **phải đăng ký**) | 15% | developer.apple.com/app-store/small-business-program |
| Apple — chương trình chuẩn | 30% năm đầu mỗi người đăng ký, 15% từ năm thứ 2 | App Store Connect Help |
| Apple — **EU**, từ **2026-10-01** (một bộ điều khoản duy nhất, phải ký trong App Store Connect) | IAP: **26%** chuẩn · **15%** Small Business & subscription từ năm 2 · thanh toán thay thế 20% (10% SBP) · link ra web 15% (10% SBP) | apple.com/newsroom 2026-08 · developer.apple.com/support/apps-in-the-eu |
| Apple — **Mỹ**, mua qua link ra web | hiện **0%** (toà chưa duyệt mức phí; Apple đề xuất 15% / 5% SBP) | Epic v. Apple, Ninth Circuit 2025-12-11 |
| Google Play — **Mỹ, EEA, UK** từ **2026-06-30** | phí dịch vụ **10%** trên 1 triệu USD đầu/năm và mọi subscription tự gia hạn · **+5% billing** nếu dùng Play Billing (→ ~15%) · dùng billing riêng / link web: chỉ 10% + phí cổng của mình | android-developers.googleblog.com 2026-06 · answer/16954621 |
| Google Play — nước khác | 15% subscription (lịch mới tới Úc/Nhật 2026-09-30, Hàn 2026-12-31, còn lại 2027-09-30) | answer/112622 |
| RevenueCat | 0 tới 2.500 USD doanh thu theo dõi/tháng | revenuecat.com/pricing |

App đầu tay (< 1 triệu USD): Play Billing ~15%, Apple SBP 15% — **nhớ đăng ký SBP**, quên là mất 11–15%.

## 4. Định giá — cách làm có căn cứ

1. **Đo giá đối thủ**: `python3 scripts/store_research.py iap <id>` cho 5 app đầu cùng loại. Ghi bảng vào money.md.
2. **Đặt trong khoảng đó.** App mới không có đánh giá → không đặt cao nhất.
3. **Gói năm** rẻ hơn rõ so với 12 × gói tháng, để người dùng có lý do chọn năm *(thực hành phổ biến)*.
4. **Giá theo quốc gia**: App Store Connect và Play Console tự quy đổi từ giá USD; kiểm lại giá VND trước khi ra mắt
   nếu nhắm người dùng Việt Nam.
5. **Không đổi giá liên tục** — mỗi thay đổi đợi đủ dữ liệu (xem `/app-grow`). RevenueCat Experiments cho A/B giá.

## 5. Kids Category / người dùng trẻ em

- Apple 1.3: app trong Kids Category không được có analytics hay quảng cáo bên thứ ba; mua hàng phải sau
  **parental gate**.
- App dành cho trẻ em còn kéo theo COPPA (Mỹ) và chính sách Families của Google Play.
  **COPPA sửa đổi bắt buộc từ 2026-04-22**: chính sách lưu dữ liệu có thời hạn viết ra giấy, xin phép cha mẹ
  **riêng** trước khi chia dữ liệu cho bên thứ ba (kể cả quảng cáo nhắm mục tiêu), dữ liệu sinh trắc (giọng, mặt) là dữ liệu cá nhân.
- **Age rating Apple mới** (4+ · 9+ · **13+ · 16+ · 18+**): bảng hỏi mới (có câu về AI, wellness, UGC, IAP) — trả lời
  xong mới nộp được bản cập nhật. Rating có thể khác theo nước.
- **Luật app store theo bang (Mỹ)**: Texas SB 2420 **đang có hiệu lực** (Supreme Court không chặn, 2026-07);
  Utah hiệu lực 2026-05-06, phạt từ 2026-12-31; Louisiana hoãn tới 2027-07-01. Store gửi nhóm tuổi (<13 · 13–15 · 16–17 · 18+);
  app **đọc tín hiệu store** (Apple Declared Age Range API · Google Play Age Signals API) để bật/tắt tính năng hợp tuổi —
  dựa vào tín hiệu store là vùng an toàn ở Utah/Louisiana. App 18+ hoặc nội dung nhạy cảm → phải làm; app thường → ghi quyết định vào money.md.
- Pipeline mặc định: **không** đăng ký Kids Category. Đây là quyết định pháp lý của người dùng — trình bày, ghi lại.

## 6. Paywall chuyển đổi tốt mà vẫn đúng luật *(thực hành phổ biến)*

- Tiêu đề nói **kết quả** người dùng nhận, không nói "Premium".
- 3 lợi ích, mỗi dòng một ý.
- Chọn sẵn gói năm, hiện giá quy ra tháng nhỏ bên dưới giá chính (giá chính vẫn là giá thật của chu kỳ).
- Nút đóng thấy rõ. Ép mua bằng cách giấu nút đóng = review xấu + rủi ro bị từ chối.
- Hiện paywall **sau** khi người dùng thấy giá trị (cuối onboarding hoặc khi chạm tính năng Pro).
- Tham khảo thêm: skill `revenuecat-paywall` (plugin revenuecat), `paywall-optimization` (Eronred/aso-skills),
  `paywalls` (coreyhaines31/marketingskills) — đọc để lấy ý, luật ở trên vẫn thắng.

## 7. Luật tiêu dùng về subscription — Mỹ + EU (kiểm 2026-09-30)

Mua qua App Store / Play thì store lo nút huỷ + hoàn tiền. Mấy dòng dưới **bắt buộc khi bán qua web** (Stripe,
Paddle, Lemon Squeezy, RevenueCat Web) và nên theo cả trong app:

| Luật | Đòi gì |
|---|---|
| FTC "click-to-cancel" | **Đã bị huỷ** (Eighth Circuit, 2025-07-08) — nhưng FTC vẫn phạt theo ROSCA/FTC Act, và ~30 bang có luật riêng |
| California ARL (sửa đổi, hiệu lực 2025-07-01) | Đồng ý **rõ ràng** với điều khoản tự gia hạn (lưu bằng chứng ≥ 3 năm) · huỷ bằng **cùng kênh** đã đăng ký (đăng ký online → huỷ online) · nhắc hằng năm (giá, chu kỳ, cách huỷ) · áp cả trial chuyển sang trả phí |
| EU — quyền rút 14 ngày | Nội dung số giao ngay: chỉ mất quyền rút nếu khách **tích đồng ý** giao ngay + xác nhận mất quyền rút |
| EU — **nút rút hợp đồng** (Directive 2023/2673, từ **2026-06-19**) | Hợp đồng ký online còn quyền rút → phải có nút "Withdraw from contract here" thấy rõ suốt 14 ngày; rút không khó hơn mua |
| EU DSA — trader status | App kiếm tiền (bán, IAP, ads) phải khai **trader** (địa chỉ, điện thoại, email công khai) trong App Store Connect — thiếu thì bị ẩn khỏi store EU (Apple gỡ ~135.000 app ngày 2025-02-17) |

