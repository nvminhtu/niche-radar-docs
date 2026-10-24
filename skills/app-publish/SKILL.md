---
name: app-publish
description: "Bước 11 của pipeline app — đưa bản build đã ký và listing đã kiểm lên App Store + Google Play tới trạng thái live, dưới dạng checklist NGƯỜI DÙNG bấm còn Claude chuẩn bị file, chỉ đúng ô và ghi log vào publish.md: tạo app record, tạo subscription group + sản phẩm đúng Product ID, gửi sản phẩm subscription CÙNG bản app đầu tiên, ảnh paywall cho review IAP, TestFlight + Sandbox, App Privacy, nộp review; Google Play: internal testing, tạo subscription + base plan, license tester, closed test ≥12 người × 14 ngày cho tài khoản cá nhân, xin production, phát hành theo tỉ lệ. Cổng App Review Guidelines (bản Apple June 8, 2026) PASS từng dòng trước khi Submit. Xử lý khi bị từ chối (3.1.2 thiếu Terms, 2.1 paywall trống vì chưa ký Paid Apps Agreement, 5.1.1 privacy, 4.2 tính năng tối thiểu, 3.2.2 chữ quyên góp). Use when someone wants to put the app on the stores, 'đưa app lên app store', 'submit app', 'upload lên testflight', 'tạo subscription trên app store connect', 'closed testing 12 tester', 'app bị reject', 'in-app purchase bị từ chối', 'bao lâu thì duyệt', 'app review guidelines', 'guideline apple', 'kiểm guideline trước khi nộp', or when scripts/app.py status says step 11 is next. Claude không đăng nhập, không bấm Submit."
argument-hint: "[slug] [ios|android]"
user-invocable: true
model: claude-sonnet-5-5
---

# Bước 11 — publish

**Một việc:** publish.md ghi đúng trạng thái; bước ok khi `iOS: live` và/hoặc `Android: production` theo nền tảng của app.

**Claude không đăng nhập, không điền form, không bấm Submit/Publish/Upload.** Mỗi bước: Claude nói rõ trang nào, ô nào,
dán gì (từ listing.md / money.md) → người dùng bấm → Claude ghi một dòng log.

Runbook chi tiết từng màn: [references/appstore-runbook-apps.md](references/appstore-runbook-apps.md) ·
[references/play-runbook.md](references/play-runbook.md) · tài khoản/thời gian chờ: [references/appstore-account.md](references/appstore-account.md) ·
**cổng guideline Apple:** [references/app-review-guidelines.md](references/app-review-guidelines.md).

## Điều kiện trước khi bắt đầu

- [ ] `check_release.py` 0 FAIL · `check_listing.py` 0 FAIL · review PASS
- [ ] Apple: Paid Apps Agreement **Active** (không thì sản phẩm không tải được → paywall trống → bị từ chối 2.1)
- [ ] Google: Payments profile đã liên kết
- [ ] Site Privacy/Terms/Support đang mở được từ trình duyệt
- [ ] **Guideline gate** trong review.md: đi hết [app-review-guidelines.md](references/app-review-guidelines.md) (mục A–H, app Mac thêm mục I),
      mỗi dòng `PASS`/`FAIL`/`N/A` kèm bằng chứng — còn 1 `FAIL` là **không nộp**. Mở trang guideline xem ngày
      "Last Updated": khác `June 8, 2026` thì đọc phần đổi và cập nhật file reference trước.

## Luôn sinh thư mục `publish/` trước

Sản xuất (spec, design, code, listing.md nguồn…) và **thứ đem lên store** tách riêng: mọi thứ người dùng copy/kéo thả nằm
trong `apps/<nhóm>/<slug>/publish/`, sinh bằng `python3 scripts/publish_kit.py <slug>` (release.py tự gọi sau mỗi bản build):

- `STORE-SETUP.md` — tạo app lần đầu: Bundle ID, Name, SKU, subscription group + Product ID (money.md), Team ID
- `LISTING.md` — mỗi ô store một khối copy kèm đếm ký tự/giới hạn, ảnh nào kéo vào đâu, đường dẫn file build
- `appstore/` `googleplay/` `macappstore/` `website/` — mỗi ô một `<field>.txt`, icon, `screenshots/<máy>/`
- `manifest.json` + `products.json` — bản máy đọc cho ShotMatic (schema: `reference/README-APP-PUBLISH-02-PUBLISH-KIT.md`)

Việc người dùng tự bấm trên store → **không** liệt kê ô cần điền trong chat; trả lời chỉ cần link `publish/STORE-SETUP.md`
hoặc `publish/LISTING.md` + 1–2 câu bước nào làm trước. Thiếu giá trị → sửa listing.md / money.md / app.json `store_name`
rồi chạy lại, **không** gõ tay vào `publish/`. Làm cả khi người dùng chỉ xin "tạo app sẵn để test TestFlight" (trước bước 11).

## iOS — thứ tự (tóm tắt)

1. App Store Connect ▸ Apps ▸ **+** New App (Name, Bundle ID, SKU).
2. **Subscriptions**: tạo *Subscription Group* → thêm sản phẩm **đúng Product ID** trong money.md → giá, tên hiển thị, mô tả,
   **ảnh chụp paywall** (Review Screenshot) → trạng thái "Ready to Submit".
3. Nối sản phẩm vào RevenueCat (entitlement `pro`, offering `default`) + tải In-App Purchase Key lên RevenueCat.
4. Upload build (Xcode Organizer) → TestFlight → cài trên máy thật → **mua thử bằng Sandbox Apple Account**, Restore thử.
5. App Information + Pricing (Free) + **App Privacy** (từ listing.md Data safety) + Age Rating.
6. Version 1.0: dán chữ + ảnh từ listing.md, chọn build, **chọn sản phẩm subscription ở mục In-App Purchases and Subscriptions**
   (sản phẩm đầu tiên phải được gửi CÙNG một phiên bản app), Review Notes (tính năng không hiển nhiên, đường tới
   paywall, tài khoản demo nếu có đăng nhập — guideline 2.1, 2.3.1).
7. Soát lại Guideline gate với **đúng build + metadata vừa chọn** (tên ≤ 30 ký tự, ảnh là app thật, Privacy khớp SDK,
   paywall có Terms/Privacy/Restore, xoá tài khoản nếu có đăng nhập). Rồi **Add for Review → Submit.** Ghi `iOS: review`.
8. Duyệt → phát hành (thủ công hoặc tự động) → `iOS: live`, `Last iOS build: <N>`.

## Android — thứ tự (tóm tắt)

1. Play Console ▸ Create app → **Internal testing** → upload AAB → `Android: internal`.
2. **Monetize ▸ Subscriptions**: tạo subscription **đúng Product ID** + base plan (tháng/năm, tự gia hạn), kích hoạt.
3. Nối vào RevenueCat (service account JSON). **License testing**: thêm Gmail tester → cài từ link internal test → mua thử.
4. **App content**: Privacy policy, Ads (không), Data safety, Content rating (IARC), Target audience, Financial features (không).
5. Store listing: dán từ listing.md + ảnh `store/android/`.
6. **Closed testing** (tài khoản cá nhân tạo sau 2023-11-13): ≥ 12 tester opt-in **liên tục 14 ngày** → `Android: closed`.
7. **Apply for production** → Google duyệt → Production, phát hành theo tỉ lệ (vd 20%) → theo dõi crash/ANR → 100%
   → `Android: production`, `Last Android versionCode: <N>`.

## Ghi log

```markdown
iOS: review
Android: closed
Last iOS build: 3
Last Android versionCode: 3

| 2026-10-02 | iOS | review | 3 | nộp 1.0 + 2 sản phẩm subscription | người dùng |
```

Đổi trạng thái thì ghi luôn phần đầu `state.md` (ShotMatic đọc chỗ này):

```bash
python3 scripts/state_header.py <slug> Cycle=upgrade "Live=1.0.1 — https://apps.apple.com/…" "Step=done · 1.0.1 live"   # store duyệt
python3 scripts/state_header.py <slug> "Step=submit · 1.0.2 (4) đã nộp, chờ duyệt"                                    # vừa nộp
```

`Live:` **luôn kèm link** — trang store; chưa có trên store (bán .dmg, APK GitHub, web game) thì link landing/trang tải.
Live trên nhiều store, version khác nhau → mỗi store một đoạn: `Live: iOS 1.2 — <link App Store> · Android 1.1 — <link Play>`
(`release.py` chọn chỗ theo từng store; kiểm khớp store thật: `python3 ready.py check` trong App-Ready-Publish).
`release.py` đóng gói xong đã tự ghi `Version` + `Step: submit …`. App chưa từng có bản build thì không ghi phần đầu.

## Bị từ chối — bình thường, không phải thảm hoạ

Dán **nguyên văn** thông báo vào publish.md. Tìm dòng trong bảng, sửa ở đúng bước, tăng build number, nộp lại.

| Lý do | Mục | Sửa ở |
|---|---|---|
| Không có link Terms of Use / Privacy trong app hoặc metadata | 3.1.2 | `/app-listing` (Terms URL, mô tả) + paywall |
| Paywall không hiện giá / không mua được khi review | 2.1 | Paid Apps Agreement chưa Active, sản phẩm chưa gửi kèm version, offering RevenueCat chưa đặt current → `app-paywall` §Kiểm tra |
| Subscription không nói rõ giá trị | 3.1.2(c) | copy paywall (`/app-money`, `/app-design`) |
| Privacy URL hỏng / khai báo privacy không khớp SDK | 5.1.1 | `make_site.py` + listing Data safety |
| App quá đơn giản / giống web | 4.2 | thêm giá trị thật (`/app-feature`) |
| Thu tiền cho từ thiện trong app | 3.2.2(iv) | bỏ chữ quyên góp/nút donate — `app-money/references/donation-rule.md` |
| Ảnh không phải app thật | 2.3.3 | chụp lại bằng `run_app.py shot` |
| Bản nộp crash / màn trống / link chết / backend tắt | 2.1(a) | `/app-fix` → chạy TestFlight máy thật; bật backend |
| Có đăng nhập mà không có tài khoản demo | 2.1(a) | App Review Information ▸ Sign-in required |
| Tính năng ẩn / Review Notes chung chung | 2.3.1(a) | viết Review Notes cụ thể từng tính năng mới |
| Tên/subtitle/keywords nhồi thương hiệu khác, quá 30 ký tự | 2.3.7 | `/app-listing` |
| Metadata nhắc Android/Google Play | 2.3.10 | `/app-listing` |
| Không có Restore / mở khoá ngoài IAP | 3.1.1 | `/app-paywall` |
| Ép đánh giá, tự vẽ popup xin 5 sao | 3.2.2(x), 5.6.1 | dùng `requestReview` của Apple (`/app-grow`) |
| Có tạo tài khoản mà không xoá được trong app | 5.1.1(v) | `/app-feature` |
| Bắt đăng nhập khi app không cần tài khoản | 5.1.1(v) | `/app-feature` |
| Login Google/Facebook mà không có lựa chọn tương đương (Sign in with Apple) | 4.8 | `/app-feature` |
| Purpose string mơ hồ / xin quyền không cần | 5.1.1(ii)(iii) | Info.plist + code |
| Gửi dữ liệu người dùng cho AI bên thứ ba không hỏi | 5.1.2(i) | xin phép rõ + Privacy Policy |
| App loại bão hoà (timer, wallpaper, flashlight…) / bản sao | 4.3(b), 4.1 | thêm khác biệt thật hoặc bỏ ý tưởng (`/app-research`) |
| "Similar binary, metadata, and/or concept" — Spam | 4.3(a) | sửa **binary** (tắt tính năng giống template), tên/mô tả/ảnh đầu nói luồng chỉ mình có, Review Notes thêm "What makes this app different", trả lời Resolution Center — `reference/README-APP-PUBLISH-01-GUIDELINE-4-3-SPAM.md` |
| Quảng cáo không có nút đóng rõ / không báo cáo được | 2.5.18 | code quảng cáo |
| Google: Data safety không khớp | Play policy | listing Data safety |

Bảng đủ theo từng mục guideline: [references/app-review-guidelines.md](references/app-review-guidelines.md).
Không đồng ý kết luận → trả lời trong Resolution Center dẫn đúng số mục, hoặc **Appeal**. Đừng nộp lại y nguyên
(reject lặp cùng mục làm lần sau duyệt chậm hơn).

## Bản cập nhật về sau

`/app-feature` hoặc `/app-fix` → test → review nhanh → `python3 scripts/release.py <slug> --minor|--patch` (tự tăng version + build, build, ký, đóng gói) → upload từ `App-Ready-Publish/<Tên-store>/release/v<version>/` (chạy `upload.sh`) lên track đang dùng.
Không phải chạy lại closed test 14 ngày. Chữ "What's New" viết điều người dùng thấy, không viết "bug fixes".

LEARNED.md mục **Bước 11** · `scripts/app.py log` · tiếp theo `/app-marketing` (có thể chạy song song từ lúc nộp review).
