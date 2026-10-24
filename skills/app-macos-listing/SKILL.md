---
name: app-macos-listing
description: "Bước 10 nhánh macOS — viết trang bán app Mac vào macos_listing.md rồi kiểm bằng check_macos_listing.py. Hai kiểu khác hẳn nhau: Mac App Store (App Name 30 · Subtitle 30 · Keywords 100 BYTE · Description 4000 · Review Notes · App Privacy · ảnh 16:10 1280×800/1440×900/2560×1600/2880×1800 không alpha · icon 1024 · danh mục · Copyright) và bán ngoài store (trang tải, yêu cầu hệ thống, ghi chú Gatekeeper cho bản notarized, release notes, appcast Sparkle, Homebrew cask, Privacy/Terms URL, bảng gói khớp money.md). Chụp ảnh store bằng run_app.py shot --platform macos, dựng website bằng make_site.py. Cảnh báo chữ quyên góp trong mô tả (Apple 3.2.2(iv)). Use when 'listing app mac', 'trang bán app mac', 'aso mac app store', 'mô tả app macos', 'ảnh chụp màn hình mac app store', 'kích thước screenshot mac', 'trang tải dmg', 'homebrew cask', 'release notes mac app', 'app privacy mac', or when scripts/app.py status says step 10 is next on a macos app. Không bịa độ phổ biến từ khoá, không bịa lượt tải."
argument-hint: "[slug]"
user-invocable: true
---

# app-macos-listing — trang bán app Mac

Bước 10 của pipeline khi `app.json` có `"stack": "macos"`. File kết quả: `apps/ACTIVE/<slug>/context-ai/macos_listing.md`.
App điện thoại dùng `/app-listing` — **đừng lẫn**: cỡ ảnh, danh mục và cả việc "có store hay không" đều khác.

## Trước khi viết

```bash
python3 scripts/app.py status <slug>          # phải qua bước 9 (bản build đã ký) mới có ảnh thật để chụp
cat apps/ACTIVE/<slug>/app.json | grep distribution  # direct | mas — quyết định viết những mục nào
cat apps/ACTIVE/<slug>/context-ai/money.md                      # bảng Products phải khớp bảng Subscriptions trong listing
```

`distribution: mas` → viết mục ◆ (App Privacy).
`distribution: direct` → viết mục ◇ (Download URL, Gatekeeper note, Sparkle appcast, Homebrew cask).
**Luôn viết** `## Review Notes` + `## Release notes` dù phân phối kiểu nào: Review Notes bắt buộc khi `mas` (WARN khi
`direct` — chuyển sang store sau là có sẵn), Release notes bắt buộc khi `direct` (WARN khi `mas` — dán vào
"What's New in This Version" mỗi bản cập nhật). Mỗi lần tăng version, sửa Release notes cho đúng bản mới.
Mục còn lại (tên, mô tả, ảnh, icon, URL, gói) cả hai đều cần — vì cả hai đều phải thuyết phục người lạ trả tiền.

## Pha 0 — nhắc việc Apple Developer (mục đầu file)

`## Chuẩn bị Apple Developer` là checklist Certificate (Apple Distribution + Mac Installer ◆ / Developer ID ◇) →
Identifier `bundle_id` → Profile "Mac App Store Connect" tên `<Name> App Store` → app record trên App Store Connect.
Template điền sẵn bundle id + tên. Claude **không** làm thay — chỉ nhắc, và tick sẵn dòng không áp dụng kèm lý do
(vd app miễn phí → không cần Paid Apps Agreement). Checker WARN dòng chưa tick, không FAIL.

## Pha 1 — chữ

| Ô | Giới hạn | Luật viết |
|---|---|---|
| App Name | 30 ký tự | **cụm đã đo đứng đầu** + ` - Brand` (xem luật dưới bảng). Không "best", "#1", không tên đối thủ |
| Subtitle | 30 | một cụm đã đo khác tên + lợi ích, không lặp chữ của tên |
| Keywords | **100 byte** | `a,b,c` không khoảng trắng. Chữ có dấu tốn 2–3 byte. Không lặp từ đã có trong tên (Apple đã đánh chỉ mục tên) |
| Promotional Text | 170 | đổi được bất cứ lúc nào không cần bản mới — để dành cho tin mới |
| Description | 4000 | **150 chữ đầu** quyết định: app làm gì · cho ai · khác gì. Rồi mới tới danh sách tính năng |
| System requirements | — | "macOS 14 trở lên · Apple Silicon và Intel" — người mua app Mac hỏi câu này trước tiên |

**Tên store = cụm nhu cầu đã đo + brand** (`store_name.py`): chạy `python3 scripts/store_research.py rank "<cụm>" … --app <id> --mac` → dán bảng vào `## Từ khoá đã đo`. Tên phải chứa nguyên một cụm có Gợi ý `có`; brand chưa nổi (`Brand known: no`) thì cụm đứng **đầu**, brand ra sau: `Duplicate File Finder - Sweepy`, không phải `Sweepy: …`. Người ta tìm bằng việc cần làm — tên riêng chưa ai nhớ. Subtitle giữ một cụm đã đo khác. Checker FAIL nếu tên không theo luật. Chỉ áp cho Mac App Store (`distribution: mas`) — bán ngoài store không có ô tìm kiếm App Store. **Không nhãn hiệu Apple trong tên** (Mac, iPhone, iPad, iOS, Apple…) — Guideline 5.2.5, cả tên store lẫn tên hiện trên máy; "Declutter - Mac Fix Kit" bị từ chối 2026-10-22; đổi tên giữ nguyên bundle id. Checker FAIL (`store_name.apple_marks`).

Với app đụng vào file người dùng, mô tả **phải** nói rõ: app đọc thư mục nào, có gửi gì lên mạng không, xoá kiểu gì
(Thùng rác, hoàn tác được). Người mua app dọn file sợ nhất là mất dữ liệu — nói trước, bán dễ hơn.

Cấm: hứa điều app không làm · số liệu bịa ("tiết kiệm 80% dung lượng" khi chưa đo) · gọi tiền subscription là quyên góp
(Apple 3.2.2(iv)).

## Pha 2 — ảnh

```bash
python3 scripts/run_app.py shot <slug> --platform macos --name 01-inbox
```

- Cỡ hợp lệ: **1280×800 · 1440×900 · 2560×1600 · 2880×1800** (16:10 ngang), 1–10 ảnh, **không alpha**.
- Chỉnh cỡ cửa sổ app trước khi chụp cho khớp một trong bốn cỡ trên — checker đo thật và FAIL nếu lệch.
- Ảnh 1 là ảnh bán hàng: màn hình đầy dữ liệu thật (không rỗng), không lẫn thông tin cá nhân thật (tên file, email).
- Icon 1024×1024 — macOS **cho phép alpha** (khác iOS) và cần đúng hình vuông bo góc có lề của Apple; `.icns` sinh bằng
  `iconutil -c icns AppIcon.iconset` đặt ở `mac/Resources/AppIcon.icns` — hoặc một lệnh làm hết:
  `python3 scripts/native/make_macos_icon.py <slug> <ảnh-nguồn>` (xoá nền trắng quanh icon, đặt đúng lưới, sinh cả hai file).

## Pha 3 — trang web (bắt buộc cả hai kiểu)

```bash
python3 scripts/make_site.py <slug>     # About (trang chủ), Privacy, Terms, Support + Technical nếu app.json có `technical`
```

- Trang **About** (index.html) lấy `about` trong app.json; trang **Technical** (tuỳ chọn) liệt kê công nghệ đang dùng — cùng
  nội dung với Settings → About trong app. Web viết tay (VD oneclicktool.app) thì đặt bản cuối ở `site/*.html` rồi đồng bộ.

- `mas`: Apple bắt buộc **Privacy Policy URL**; bán subscription thì bắt buộc thêm **Terms (EULA)**.
- `direct`: trang chủ chính là cửa hàng của bạn — cần: nút tải, yêu cầu hệ thống, giá + gói, "mua rồi cài được mấy máy",
  chính sách hoàn tiền, `appcast.xml` cho Sparkle, và dòng trấn an Gatekeeper cho bản đã notarize.

## Pha 4 — kiểm

```bash
python3 scripts/check_macos_listing.py apps/ACTIVE/<slug>
```

Checker bắt: quá giới hạn ký tự · Keywords quá 100 byte / lặp / từ vô ích · URL không phải https hoặc còn `example.com` ·
bảng gói không khớp money.md · ảnh sai cỡ hoặc còn alpha · icon không phải 1024 · thiếu Review Notes / App Privacy (mas) · thiếu Release notes (direct) ·
thiếu Download URL / release notes / appcast (direct) · chữ quyên góp trong mô tả.

**Checker kêu → sửa quyết định, không sửa chữ cho qua regex.**

## Sau đó

- `mas` → `/app-publish`: tạo app record trên App Store Connect, upload bản Archive, khai App Privacy, nộp review.
- `direct` → `/app-publish`: đăng .dmg đã notarize + appcast lên web, ghi `macOS: released` và `Last macOS build:` vào `publish.md`.

Claude soạn chữ, chụp ảnh, dựng site, ghi log. **Người dùng** đăng nhập, upload, bấm phát hành.

## Dạy lại (bắt buộc, vào LEARNED.md)

4 dòng lời thường: vừa viết gì · vì sao giới hạn đó tồn tại · file nào · lần sau tự sửa ở đâu.
