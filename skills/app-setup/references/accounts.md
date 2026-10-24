# Tài khoản để bán app subscription — thứ tự, chi phí, thời gian chờ

Đối chiếu trang chính thức ngày **2026-09-15**. Mục ghi *(cộng đồng)* là kinh nghiệm thực tế, hay thay đổi — kiểm lại.
Chi tiết Apple (Team ID, chứng chỉ ký, thuế): `.claude/skills/app-publish/references/appstore-account.md` và
`.claude/skills/app-release/references/apple-signing.md`.

## Tổng quan

| Tài khoản | Phí | Chờ | Chặn bước | Ai làm |
|---|---|---|---|---|
| Apple ID riêng cho dev + 2FA | 0 | ngay | mọi thứ phía Apple | người dùng |
| Apple Developer Program (Individual) | 99 USD/năm | ~24h | 9 release iOS, 11 publish | người dùng |
| Apple Paid Apps Agreement → thuế → ngân hàng | 0 | thuế tới **90 ngày** (trường hợp xấu) | bán subscription trên iOS | người dùng |
| Google Play Console (cá nhân) | 25 USD một lần | xác minh danh tính vài ngày | 9 release Android | người dùng |
| Google Payments profile (merchant) | 0 | vài ngày | bán subscription trên Android | người dùng |
| Google closed test | 0 | **≥ 14 ngày**, ≥ 12 tester tham gia liên tục | lên production (tài khoản cá nhân tạo sau 2023-11-13) | người dùng + bạn bè |
| RevenueCat | 0 tới 2.500 USD doanh thu theo dõi/tháng | ngay | bước 6 nối subscription thật | người dùng |
| Email hỗ trợ + trang Privacy/Terms/Support | 0 (GitHub Pages) | 1 buổi | listing, review | Claude dựng, người dùng đăng |

**Lịch khuyên dùng:** ngày 1 mở cả Apple + Google + RevenueCat, điền thuế Apple ngay; tuần 2 rủ tester cho
closed test Google; app xong ở tuần 4–6 thì mọi đồng hồ chờ đã chạy xong.

## Apple

- Nguồn: developer.apple.com/programs · developer.apple.com/help/account/membership/program-enrollment
- **Individual** thay vì Organization: cùng 99 USD, duyệt ~24h thay vì 1–2 tuần, không cần pháp nhân / D-U-N-S.
  Đổi lại tên thật hiện là người bán trên store.
- Đăng ký nhanh nhất qua app **Apple Developer** trên iPhone (xác minh CCCD/hộ chiếu ngay trên máy).
- **Small Business Program**: phí Apple 15% thay vì 30% khi doanh thu < 1 triệu USD/năm — **phải tự đăng ký**
  (developer.apple.com/app-store/small-business-program). Không đăng ký = mất 30%.
- Thuế: người ngoài Mỹ nộp **W-8BEN** trong App Store Connect ▸ Business. Hiệp định thuế Mỹ–Việt Nam đã ký nhưng
  chưa có hiệu lực → giả định có khấu trừ thuế phần doanh thu Mỹ, hỏi kế toán trước khi tính tiền ròng.
  Pipeline không tư vấn thuế.
- Gia hạn 99 USD hằng năm — hết hạn là app bị gỡ khỏi store. Đặt lịch nhắc trước 30 ngày.

## Google Play

- Nguồn: support.google.com/googleplay/android-developer/answer/6112435 (đăng ký) ·
  answer/14151465 (closed test 12 tester × 14 ngày)
- Tài khoản cá nhân tạo sau 2023-11-13: phải chạy closed test với **≥ 12 tester opt-in liên tục 14 ngày**, sau
  đó nộp đơn xin production. Ai rút ra rồi vào lại thì đếm lại *(cộng đồng)*.
- Phí dịch vụ Google Play cho subscription: **15%** (support.google.com/googleplay/android-developer/answer/112622).
- Bán subscription cần **Payments profile** (merchant account) liên kết với Play Console.

## RevenueCat

- Nguồn: revenuecat.com/pricing · revenuecat.com/docs
- Tạo project → thêm app iOS (bundle id) + app Android (applicationId) → lấy **public SDK key** cho mỗi app
  (`appl_...`, `goog_...`). Secret key (`sk_...`) **không bao giờ** nằm trong app.
- iOS: tải **In-App Purchase Key** (.p8) từ App Store Connect lên RevenueCat. Android: service account JSON có quyền
  xem tài chính trên Play Console. Plugin `revenuecat` hướng dẫn từng bước.

## Việt Nam — lưu ý thực tế *(cộng đồng)*

- Thẻ Visa/Mastercard ghi nợ quốc tế trả được phí Apple/Google nếu ngân hàng bật thanh toán quốc tế.
- Tài khoản ngân hàng nhận tiền: tên chủ tài khoản phải khớp tên pháp lý trên hợp đồng Apple.
- Tiền về có thể qua ngân hàng trung gian — hỏi ngân hàng của bạn về SWIFT và phí nhận ngoại tệ.

## Không bao giờ

Mua/thuê tài khoản developer của người khác · dùng Apple ID gia đình chung · commit file `.p8`, `.p12`, `.jks`,
`key.properties` vào git · để Claude gõ mật khẩu hay số thẻ.
