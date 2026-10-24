# App Review Guidelines — cổng kiểm trước khi bấm Submit

Nguồn: https://developer.apple.com/app-store/review/guidelines/ — bản **Last Updated: June 8, 2026**,
đối chiếu ngày **2026-09-24**. Apple đổi guideline vài lần mỗi năm: trước mỗi lần nộp bản 1.0, mở trang
xem ngày "Last Updated"; khác ngày trên thì đọc lại mục đổi và sửa file này.

Cách dùng: đi từng dòng (app Mac lên Mac App Store thêm mục I), ghi `PASS` / `FAIL` / `N/A` vào `review.md` mục **Guideline gate**. Còn một dòng
`FAIL` thì **không nộp**. Cột "Sửa ở" chỉ skill phụ trách. Số mục (vd `3.1.2`) giữ nguyên để dán vào
Resolution Center khi trả lời Apple.

## A. Trước khi nộp — "Before You Submit" (lý do reject 2.1 phổ biến nhất)

| # | Kiểm | Mục | Sửa ở |
|---|---|---|---|
| A1 | Đã chạy trên **máy thật** (TestFlight), không crash ở luồng chính, onboarding, paywall, restore | 2.1(a) | `/app-fix`, `/app-review` |
| A2 | Không còn chữ placeholder, lorem ipsum, "TODO", màn trống, nút chưa làm, link chết | 2.1(a) | `/app-review` |
| A3 | Backend / API / RevenueCat **đang bật** và gọi được từ mạng ngoài (reviewer ở Mỹ) | 2.1(a) | — |
| A4 | Có đăng nhập → **tài khoản demo** còn hạn trong App Review Information (hoặc demo mode đã được Apple duyệt) | 2.1(a) | Review Notes |
| A5 | Review Notes giải thích **tính năng không hiển nhiên** + từng IAP nằm ở đâu, cách tới paywall | 2.1(b), 2.3.1(a) | Review Notes |
| A6 | Thông tin liên hệ trong App Review Information là số/email thật, trực được | Before You Submit | — |
| A7 | Chạy được trên **mạng IPv6-only** (không hardcode IPv4) | 2.5.5 | `/app-fix` |
| A8 | Chỉ dùng **public API**, build bằng Xcode/SDK hiện hành, không tải/thực thi code làm đổi tính năng | 2.5.1, 2.5.2 | `/app-build` |
| A9 | Không tốn pin / nóng máy / chạy nền vô cớ; background mode chỉ dùng đúng mục đích | 2.4.2, 2.5.4 | `/app-fix` |
| A10 | Không bảo người dùng tắt Wi-Fi, tắt bảo mật, khởi động lại máy | 2.4.4 | copy |
| A11 | App iPhone chạy được trên iPad (không vỡ layout, không crash) nếu không tắt iPad | 2.4.1 | `/app-design` |

## B. Metadata — chữ, ảnh, tên (lý do reject 2.3.x)

| # | Kiểm | Mục | Sửa ở |
|---|---|---|---|
| B1 | Tên app ≤ **30 ký tự**, không nhồi từ khoá, tên app khác, thương hiệu người khác, giá | 2.3.7, 4.1(c) | `/app-listing` |
| B2 | Subtitle không nhắc app khác, không tuyên bố không kiểm chứng được ("#1", "tốt nhất") | 2.3.7 | `/app-listing` |
| B3 | Keywords không chứa tên thương hiệu/app khác, không chứa từ không liên quan | 2.3.7 | `/app-listing` |
| B4 | Ảnh chụp là **app đang dùng thật**, không chỉ splash/login/title art; chữ overlay được | 2.3.3 | `run_app.py shot` |
| B5 | Video preview chỉ quay màn hình của chính app | 2.3.4 | `/app-listing` |
| B6 | Mô tả/ảnh nói rõ cái gì **cần trả tiền** (Pro, subscription) | 2.3.2 | `/app-listing` |
| B7 | Icon, ảnh, preview phù hợp **4+** kể cả khi app rating cao hơn | 2.3.8 | `/app-design` |
| B8 | Không dùng chữ "For Kids"/"For Children" nếu không ở Kids Category | 2.3.8, 5.1.4 | `/app-listing` |
| B9 | Không có tên/logo Android, Google Play, chợ app khác trong app hoặc metadata | 2.3.10 | `/app-listing`, copy |
| B10 | Ảnh dùng dữ liệu giả (tên, email, số dư…), không phải dữ liệu người thật; có quyền dùng mọi hình | 2.3.9 | `/app-listing` |
| B11 | Category đúng bản chất app | 2.3.5 | `/app-listing` |
| B12 | Bảng hỏi **Age Rating mới** (4+/9+/13+/16+/18+; có câu AI, wellness, UGC, IAP) trả lời thật — chưa trả lời thì không nộp được | 2.3.6 | App Information |
| B13 | Không ám chỉ Apple tài trợ/đề xuất; không giả giao diện Apple (Finder, App Store, Messages) | 5.2.4, 5.2.5 | copy, `/app-design` |
| B14 | "What's New" liệt kê tính năng/thay đổi thật (bản cập nhật lớn không được ghi "bug fixes") | 2.3.12 | `/app-release` |
| B15 | Không có tính năng ẩn / khoá bằng cờ server mà reviewer không thấy | 2.3.1(a) | `/app-review` |

## C. Tiền — subscription, IAP, paywall (lý do reject 3.1.x, 2.1(b))

| # | Kiểm | Mục | Sửa ở |
|---|---|---|---|
| C1 | Mở khoá tính năng số **chỉ bằng IAP** — không license key, QR, link web mua (trừ storefront Mỹ / entitlement) | 3.1.1, 3.1.1(a) | `/app-money` |
| C2 | Có nút **Restore Purchases** thấy được (paywall hoặc Settings) | 3.1.1 | `/app-paywall` |
| C3 | Sản phẩm IAP đầu tiên được **gửi CÙNG phiên bản app**, trạng thái Ready to Submit, có Review Screenshot | 2.1(b) | runbook 1.4, 3.7 |
| C4 | Paywall **hiện giá thật** trên TestFlight (Paid Apps Agreement Active, offering current) | 2.1(b) | `/app-paywall` §Kiểm tra |
| C5 | Paywall ghi rõ **được gì**, giá, chu kỳ gia hạn, trial bao lâu, tự gia hạn đến khi huỷ, cách huỷ | 3.1.2(c) | `/app-paywall`, `/app-money` |
| C6 | Paywall (hoặc gần nút mua) có link **Terms of Use (EULA)** + **Privacy Policy** hoạt động; mô tả App Store cũng có Terms URL | 3.1.2, 5.1.1(i) | `/app-paywall`, `/app-listing` |
| C7 | Subscription tối thiểu **7 ngày**, có giá trị liên tục, dùng được trên mọi thiết bị của người dùng | 3.1.2(a) | `/app-money` |
| C8 | Không bắt làm thêm việc (share MXH, mời bạn, check-in N lần) mới nhận thứ đã trả tiền | 3.1.2(a) | `/app-money` |
| C9 | Nút đóng paywall thấy rõ, không lừa (giá gạch ngang giả, "miễn phí" rồi tính tiền, bait-and-switch) | 3.1.2(a), 5.6 | `/app-paywall` |
| C10 | Các gói trong một Subscription Group, nâng/hạ cấp mượt, không mua trùng hai gói cùng loại | 3.1.2(b) | runbook 1.3 |
| C11 | Chuyển app cũ sang subscription: người đã mua trước **không mất** tính năng đã trả | 3.1.2(a) | `/app-money` |
| C12 | Tiền ảo/credit mua bằng IAP **không hết hạn** | 3.1.1 | `/app-money` |
| C13 | Không quyên góp/gây quỹ trong app (trừ nonprofit đã duyệt) | 3.2.2(iv) | `app-money/references/donation-rule.md` |
| C14 | **Không ép** rate/review/tải app khác để dùng tính năng; xin rating chỉ bằng API `requestReview` của Apple | 3.2.2(x), 5.6.1 | `/app-grow`, code |
| C15 | App không tạo ra chủ yếu để hiện quảng cáo; không tăng lượt xem/click quảng cáo giả | 3.2.2(iii) | `/app-money` |
| C16 | Giá hợp lý — không "rip-off" giá cao vô lý | 3. Business | `/app-money` |

## D. Quảng cáo (nếu có ad SDK)

| # | Kiểm | Mục | Sửa ở |
|---|---|---|---|
| D1 | Quảng cáo chỉ trong app chính — không ở widget, extension, notification, App Clip | 2.5.18 | code |
| D2 | Interstitial ghi rõ là quảng cáo, **nút đóng/skip to rõ**, không lừa bấm | 2.5.18 | code |
| D3 | Người dùng **báo cáo được** quảng cáo không phù hợp | 2.5.18 | code |
| D4 | Nội dung quảng cáo hợp age rating; không nhắm mục tiêu theo dữ liệu nhạy cảm (sức khoẻ, trẻ em) | 2.5.18 | cấu hình ad network |
| D5 | Tracking (IDFA) → bật **ATT prompt** trước; không chặn tính năng khi người dùng từ chối | 5.1.2(i) | code, `NSUserTrackingUsageDescription` |

## E. Privacy & dữ liệu (lý do reject 5.1.x)

| # | Kiểm | Mục | Sửa ở |
|---|---|---|---|
| E1 | Link Privacy Policy ở **ô metadata App Store Connect** VÀ **trong app** (Settings/About), mở được | 5.1.1(i) | `make_site.py` |
| E2 | Privacy Policy nêu: thu dữ liệu gì, cách thu, dùng làm gì; bên thứ ba (SDK, analytics, AI) bảo vệ tương đương; thời gian lưu, cách xoá, cách rút đồng ý | 5.1.1(i) | `make_site.py` |
| E3 | **App Privacy** (nutrition label) khớp **mọi SDK** thật trong build (RevenueCat, Firebase, Sentry, ads…) | 2.3, 5.1.1 | listing Data safety |
| E4 | Mỗi quyền có **purpose string** (`NS…UsageDescription`) nói rõ, cụ thể để làm gì | 5.1.1(ii) | Info.plist |
| E5 | Chỉ xin quyền cần cho tính năng lõi, xin **đúng lúc dùng**; ưu tiên picker (PHPicker, share sheet) thay vì full access | 5.1.1(iii) | code |
| E6 | Từ chối quyền vẫn dùng được phần còn lại (vd nhập tay địa chỉ thay GPS); tính năng trả phí không phụ thuộc cấp quyền | 5.1.1(ii)(iv) | code |
| E7 | Không bắt đăng nhập nếu app không có tính năng dựa trên tài khoản | 5.1.1(v) | `/app-feature` |
| E8 | Có tạo tài khoản → có **Xoá tài khoản ngay trong app** (không chỉ "email cho chúng tôi") | 5.1.1(v) | `/app-feature` |
| E9 | Có login Google/Facebook/… cho tài khoản chính → phải có thêm lựa chọn tương đương (vd **Sign in with Apple**) | 4.8 | `/app-feature` |
| E10 | Gửi dữ liệu cá nhân cho **AI bên thứ ba** (OpenAI, Claude, Gemini…) → nói rõ và xin phép rõ ràng trước khi gửi | 5.1.2(i) | code + Privacy Policy |
| E11 | Không bắt bật push / location / tracking để dùng app hoặc nhận thưởng | 5.1.2(i) | code |
| E12 | Ghi hình/ghi âm/ghi màn hình → xin đồng ý rõ + có chỉ báo đang ghi | 2.5.14 | code |
| E13 | Có **`PrivacyInfo.xcprivacy`** cho app + mọi SDK dùng required-reason API | privacy manifest | nâng plugin |
| E14 | Push marketing chỉ khi người dùng opt-in bằng chữ trong app + có chỗ tắt | 4.5.4 | code |
| E15 | Dữ liệu người dùng lưu/truyền an toàn (HTTPS, Keychain cho token) | 1.6 | code |

## F. Thiết kế & chức năng tối thiểu (lý do reject 4.x)

| # | Kiểm | Mục | Sửa ở |
|---|---|---|---|
| F1 | App có giá trị "như app" — không chỉ là web view bọc website, không chỉ là list link | 4.2, 4.2.2 | `/app-feature` |
| F2 | Không phải bản sao app khác (tên, UI, icon); không mạo danh | 4.1 | `/app-design` |
| F3 | Không nộp app thuộc loại **bão hoà** (flashlight, wallpaper, timer đơn giản, soundboard, bói toán, dating) nếu không khác biệt thật | 4.3(b) | `/app-research` |
| F4 | Không nộp nhiều Bundle ID cho cùng một app (vd mỗi thành phố một app) | 4.3(a) | `/app-spec` |
| F5 | Không làm từ template/app generator thương mại rồi nộp hộ | 4.2.6 | — |
| F6 | App chạy độc lập, không đòi cài app khác; tải thêm tài nguyên lần đầu → báo dung lượng và hỏi trước | 4.2.3 | code |
| F7 | Widget/extension/notification liên quan tới app, extension không có quảng cáo/IAP | 2.5.16, 4.4 | code |
| F8 | Không thu tiền cho tính năng có sẵn của máy/OS (camera, push, iCloud, con quay) | 4.10 | `/app-money` |
| F9 | Dùng Apple Pay cho thanh toán định kỳ → ghi kỳ hạn, được gì, số tiền, cách huỷ | 4.9 | `/app-paywall` |
| F10 | Nhúng mini app/HTML5 game/chatbot → lọc nội dung, báo cáo, chặn người dùng, có index + giới hạn tuổi | 4.7 | code |

## G. Nội dung & an toàn (1.x) — chỉ app có các dạng này

| # | Kiểm | Mục |
|---|---|---|
| G1 | **UGC / MXH / chat**: có lọc nội dung, nút **báo cáo**, **chặn người dùng**, thông tin liên hệ công khai | 1.2 |
| G2 | Kids Category: không link ra ngoài/mua hàng nếu không có parental gate; không analytics/ads bên thứ ba gửi dữ liệu nhận dạng | 1.3, 5.1.4 |
| G3 | App y tế/sức khoẻ: công bố phương pháp đo, nhắc hỏi bác sĩ; không tuyên bố đo huyết áp/SpO2 chỉ bằng cảm biến máy | 1.4.1 |
| G4 | Không nội dung phản cảm, kỳ thị, bạo lực thật, tình dục, khai thác sự kiện thảm hoạ | 1.1 |
| G5 | Không tính năng giả/đùa đánh lừa (định vị giả, "đo" giả), ghi "for entertainment" không cứu được | 1.1.6 |
| G6 | Support URL có cách liên hệ thật | 1.5 |
| G7 | Ngành bị quản lý (tài chính, y tế, crypto exchange, gambling, VPN, vay tiền) → phải nộp bằng **tài khoản tổ chức** có giấy phép | 5.1.1(ix), 3.1.5, 5.3, 5.4, 3.2.2(ix) |
| G8 | Nội dung/nhạc/API bên thứ ba: có quyền dùng; không tải video/nhạc từ YouTube, Spotify… | 5.2.1–5.2.3 |

## R. Luật theo vùng — Mỹ + EU (kiểm 2026-09-30)

| # | Kiểm | Nguồn | Sửa ở |
|---|---|---|---|
| R1 | **EU trader status** đã khai (App Store Connect ▸ Business) nếu app kiếm tiền và bán ở EU — thiếu = app bị ẩn ở EU | DSA | NGƯỜI DÙNG |
| R2 | Bán ở EU → đã ký **điều khoản EU mới** (hiệu lực 2026-10-01, IAP 26%/15%) và hiểu phí link-out/billing thay thế | DMA | `/app-money` playbook §3 |
| R3 | Link/nút mua trên web chỉ bật ở storefront được phép (Mỹ; EU theo điều khoản EU) — ẩn theo storefront, không theo IP | 3.1.1(a) | `growth:direct-sales` |
| R4 | App 18+/nội dung nhạy cảm hoặc có trẻ em dùng: đọc **Declared Age Range** (Texas SB 2420 đang có hiệu lực, Utah từ 2026-05-06) | luật bang | `/app-feature` |
| R5 | Trẻ em < 13 dùng được: COPPA sửa đổi (từ 2026-04-22) — chính sách lưu dữ liệu, xin phép riêng trước khi chia cho bên thứ ba | COPPA | `/app-money` playbook §5 |
| R6 | Có AI chatbot / sinh nội dung giống thật cho người dùng EU: báo rõ đang nói chuyện với AI; nội dung sinh ra gắn nhãn | EU AI Act Art. 50 (từ 2026-08-02) | code + Privacy Policy |

## H. Sau khi nộp — "After You Submit"

- Bị reject: trả lời trong **App Store Connect** (Resolution Center), lịch sự, dẫn đúng số mục; không đồng ý thì **Appeal**.
- Reject lặp lại cùng một mục → lần review sau chậm hơn. Sửa tận gốc, đừng nộp thử.
- **Expedited review** chỉ khi thật sự gấp (lỗi nghiêm trọng đang live) — lạm dụng sẽ bị từ chối về sau.
- App đã live: bản **bug fix** không bị giữ vì lỗi guideline (trừ pháp lý/an toàn) — ghi trong Resolution Center là muốn dùng quy trình này.
- Đã duyệt có thể mất tới **24h** mới hiện ở mọi storefront.
- Không thao túng review/xếp hạng (review mua, review ảo, thưởng để đánh 5 sao) → bị đuổi khỏi Developer Program (5.6.3).
- Trả lời review người dùng lịch sự, không marketing, không thông tin cá nhân (5.6.1).

## I. Mac App Store (chỉ app stack `macos` nộp lên store) — 2.4.5

| # | Kiểm | Mục | Sửa ở |
|---|---|---|---|
| I1 | Bật **App Sandbox**; chỉ sửa dữ liệu app khác qua API chính thức | 2.4.5(i) | `/app-macos` |
| I2 | Đóng gói bằng Xcode/`productbuild`, một bundle tự chứa — không installer bên thứ ba, không cài vào chỗ dùng chung | 2.4.5(ii) | `/app-macos` |
| I3 | Không tự chạy lúc login / không để process chạy sau khi thoát nếu chưa được đồng ý; không tự thêm icon vào Dock/desktop | 2.4.5(iii) | code |
| I4 | Không tải thêm app/kext/code làm đổi tính năng | 2.4.5(iv) | code |
| I5 | Không xin quyền root / setuid | 2.4.5(v) | code |
| I6 | Không màn license key, không copy protection tự làm; **không Sparkle** — cập nhật chỉ qua Mac App Store | 2.4.5(vi)(vii) | `/app-macos` |
| I7 | Mọi ngôn ngữ nằm trong một bundle; chạy trên macOS hiện hành | 2.4.5(viii)(ix) | `/app-build` |
