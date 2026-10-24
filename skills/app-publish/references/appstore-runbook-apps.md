# Runbook App Store — app Flutter có subscription

Mỗi bước ghi **AI LÀM**: `CLAUDE` (chuẩn bị, chỉ đường, ghi log) hoặc `NGƯỜI DÙNG` (đăng nhập, bấm, ký, trả tiền).
Đối chiếu App Store Connect Help ngày **2026-09-15** — giao diện đổi thường xuyên, tên nút có thể lệch; tìm theo ý.
Nguồn: developer.apple.com/help/app-store-connect · developer.apple.com/app-store/subscriptions ·
developer.apple.com/documentation/storekit/testing-in-app-purchases-with-sandbox

## Pha 0 — việc chậm, làm từ đầu

| # | Việc | Ai | Chặn |
|---|---|---|---|
| 0.1 | Apple Developer Program (Individual) → Team ID | NGƯỜI DÙNG | mọi thứ |
| 0.2 | Business ▸ **Paid Apps Agreement** → thuế W-8BEN → ngân hàng → trạng thái **Active** | NGƯỜI DÙNG | sản phẩm subscription tải được (thiếu = paywall trống khi review) |
| 0.3 | Đăng ký **App Store Small Business Program** (15%) | NGƯỜI DÙNG | phí 30% nếu quên |
| 0.4 | Site Privacy / Terms / Support đã đăng (`scripts/make_site.py`) | CLAUDE dựng · NGƯỜI DÙNG đăng | submission |
| 0.5 | Business ▸ **EU trader status** (địa chỉ, điện thoại, email sẽ hiện công khai ở EU) · ký **điều khoản EU** mới (hiệu lực 2026-10-01) | NGƯỜI DÙNG | app bị ẩn khỏi store EU |

## Pha 1 — app record + sản phẩm

| # | Màn | Điền | Ai |
|---|---|---|---|
| 1.1 | Certificates, IDs & Profiles ▸ Identifiers | bundle id = app.json, bật capability **In-App Purchase** | NGƯỜI DÙNG (Xcode automatic signing thường tự làm) |
| 1.2 | Apps ▸ **+** ▸ New App | Platform iOS · Name (listing `iOS · App Name`) · Primary language · Bundle ID · SKU (= slug) | NGƯỜI DÙNG |
| 1.3 | App ▸ Monetization ▸ **Subscriptions** ▸ tạo Subscription Group (vd "Pro") | tên nhóm hiển thị | NGƯỜI DÙNG |
| 1.4 | Trong group ▸ **+** mỗi sản phẩm | Reference name · **Product ID đúng money.md** · Duration · Price (từ USD, xem bảng giá các nước) · Localization: tên + mô tả · **Review Screenshot**: ảnh paywall (`run/out/screenshot-ios.png` khi đang ở paywall) · Review notes | NGƯỜI DÙNG, CLAUDE chuẩn bị chữ + ảnh |
| 1.5 | App ▸ App Information ▸ **App-Specific Shared Secret** / Users and Access ▸ Integrations ▸ **In-App Purchase key** (.p8) | tải lên RevenueCat | NGƯỜI DÙNG |
| 1.6 | RevenueCat ▸ Products ▸ import · Entitlements `pro` ▸ attach · Offerings `default` ▸ packages Monthly/Annual ▸ **Make current** | | NGƯỜI DÙNG, plugin revenuecat hướng dẫn |

## Pha 2 — build + thử mua thật

| # | Việc | Ai |
|---|---|---|
| 2.1 | `fvm flutter build ipa --release --dart-define-from-file=config/prod.json` | CLAUDE |
| 2.2 | Xcode ▸ Window ▸ Organizer ▸ archive mới nhất ▸ Distribute App ▸ App Store Connect ▸ Upload | NGƯỜI DÙNG |
| 2.3 | TestFlight: chờ Processing (5–60 phút) → Internal Testing → cài bằng app TestFlight | NGƯỜI DÙNG |
| 2.4 | Settings ▸ Developer ▸ **Sandbox Apple Account** (tạo ở Users and Access ▸ Sandbox) | NGƯỜI DÙNG |
| 2.5 | Mở app ▸ Upgrade ▸ mua gói tháng (sandbox không tốn tiền, chu kỳ rút ngắn) ▸ thấy Pro ▸ xoá app cài lại ▸ Restore ▸ thấy Pro | NGƯỜI DÙNG làm, CLAUDE ghi kết quả vào review.md |

Paywall trống trên TestFlight → dừng, xem `app-paywall` §Kiểm tra. Đừng nộp review khi chưa mua thử được.

## Pha 3 — phiên bản 1.0 → review

| # | Màn | Dán từ | Ai |
|---|---|---|---|
| 3.1 | App Information | Subtitle · Category · Content Rights · Age Rating (bảng hỏi) | NGƯỜI DÙNG |
| 3.2 | Pricing and Availability | Free · quốc gia | NGƯỜI DÙNG |
| 3.3 | **App Privacy** | listing `## Data safety` — RevenueCat: Purchases + Identifiers (App functionality, không liên kết danh tính nếu không có đăng nhập, không tracking) | NGƯỜI DÙNG |
| 3.4 | Version ▸ Screenshots 6.9" | `store/ios/*.png` theo thứ tự bảng | NGƯỜI DÙNG |
| 3.5 | Version ▸ Promotional Text · Description · Keywords · Support URL · Marketing URL | khối ``` trong listing.md | NGƯỜI DÙNG |
| 3.6 | Version ▸ Build | build đã thử ở Pha 2 | NGƯỜI DÙNG |
| 3.7 | Version ▸ **In-App Purchases and Subscriptions** | chọn các sản phẩm ở 1.4 — **bắt buộc cho lần gửi sản phẩm đầu tiên** | NGƯỜI DÙNG |
| 3.8 | App Review Information | liên hệ · `iOS · Review Notes` · không cần tài khoản demo nếu không có đăng nhập | NGƯỜI DÙNG |
| 3.9 | Version Release | thủ công (khuyên cho bản đầu) | NGƯỜI DÙNG |
| 3.10 | **Add for Review → Submit** | | NGƯỜI DÙNG |

## Pha 4 — sau khi nộp

| Trạng thái | Thời gian thường gặp | Việc |
|---|---|---|
| Waiting for Review → In Review | Apple: ~90% trong 24h · lần đầu của tài khoản mới *(cộng đồng)* 2–5 ngày | chờ |
| Rejected | | dán nguyên văn vào publish.md → bảng "Bị từ chối" trong SKILL → sửa → build mới → nộp lại |
| Pending Developer Release | | người dùng bấm Release khi sẵn sàng truyền thông (`/app-marketing`) |
| Ready for Sale | index từ khoá vài giờ tới ~48h *(cộng đồng)* | `iOS: live` · `/app-grow` |

## Mã lỗi upload hay gặp

| Thông báo | Nghĩa | Sửa |
|---|---|---|
| ITMS-90062 / "bundle version must be higher" | build number đã dùng | tăng số sau `+` trong pubspec |
| ITMS-90717 invalid App Store icon | icon có alpha | `remove_alpha_ios: true` + chạy lại flutter_launcher_icons |
| ITMS-90683 missing purpose string | thiếu `NS...UsageDescription` cho quyền một plugin dùng | thêm câu giải thích vào Info.plist |
| "Missing required privacy manifest" | SDK thiếu `PrivacyInfo.xcprivacy` | nâng phiên bản plugin (bản mới đã kèm manifest) |
| No signing certificate "iOS Distribution" | chưa có chứng chỉ phân phối | Xcode Organizer (Automatically manage signing) tạo giúp |
