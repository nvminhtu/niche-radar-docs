---
name: app-listing
description: "Bước 10 của pipeline app — viết trang store (ASO) cho App Store và Google Play vào listing.md và kiểm bằng check_listing.py: App Name + Subtitle 30 ký tự, ô Keywords 100 byte không lặp từ trong tên, mô tả 150 ký tự đầu trả lời app gì/cho ai/khác gì, Play title 30 · short 80 · full 4000 không vi phạm metadata policy, danh mục, Copyright, Support/Privacy/Terms URL (dựng bằng make_site.py), bảng subscription khớp money.md, Data safety / App Privacy khớp SDK, ảnh chụp màn hình thật đúng cỡ (iOS 6.9\" 1320×2868, Play 1080×1920, không alpha) chụp bằng run_app.py shot, icon Play 512 + feature graphic 1024×500 bằng prompt cho image generator. Cảnh báo chữ quyên góp trong mô tả. Use when someone wants the store page, 'ASO', 'viết mô tả app', 'từ khoá app store', 'tên app bao nhiêu ký tự', 'subtitle', 'ảnh chụp màn hình store', 'kích thước screenshot app store', 'feature graphic', 'data safety', 'app privacy', 'privacy policy url', or when scripts/app.py status says step 10 is next. Không bịa độ phổ biến từ khoá."
argument-hint: "[slug]"
user-invocable: true
---

# Bước 10 — listing (ASO)
> **Tuyến chạy do skill cha `core:asset-prompt` quyết định — đọc nó trước.**
> Codex/ChatGPT → sinh ảnh luôn. Claude → chỉ viết prompt (tuyến B), hoặc xuất thêm
> `jobs.json` (tuyến C) để user tự đem đi sinh ảnh rồi paste về `assets.raw_dir` trong
> `.claude/repo-profile.yaml`; `asset-prompt/scripts/collect_raw.py --apply` khớp và đổ
> ảnh vào đúng chỗ, rồi skill này chạy tiếp phần chuyên môn của nó.
> Không bao giờ tự vẽ thay ảnh thật, không coi prompt đã xuất là asset đã xong.


**Một việc:** `python3 scripts/check_listing.py apps/ACTIVE/<slug>` in `0 FAIL`.

> **App Mac (`stack: macos`) dùng `/app-macos-listing`** — file `macos_listing.md`, checker `check_macos_listing.py`,
> ảnh 16:10 ngang, và (nếu bán ngoài store) trang tải + release notes + appcast thay cho trang App Store.
Mọi lỗi ở bước này là lỗi **hình dạng/giới hạn**; nội dung hay hay không là nghiên cứu + mắt người.

Đọc: [references/aso-apps.md](references/aso-apps.md) (giới hạn + cách viết cho app) ·
[references/aso-advanced.md](references/aso-advanced.md) (thuật toán xếp hạng 2026, PPO, Custom Product Pages, In-App Events — viết gốc cho game, áp cho app) ·
[references/store-assets.md](references/store-assets.md) (quy trình ảnh + công cụ).

## Nguồn chữ — không bịa

1. `context-ai/research-<slug>.md` (app cũ: `research.md`) — khoảng trống, từ người dùng tự nói trong review, dòng autocomplete.
2. `spec.md` + app đang chạy — **chỉ viết điều app đang làm**.
3. `money.md` — sản phẩm, giá; `design.md` — màu cho ảnh.
4. Từ khoá: `python3 scripts/store_research.py hints "<gốc>"` cho từng gốc, và tên/subtitle của 10 app đầu.

## Thứ tự làm

1. **Website pháp lý:** điền `developer_name`, `contact_email`, `site_url` trong app.json →
   `python3 scripts/make_site.py <slug>` → người dùng đăng `site/` (GitHub Pages: repo public → Settings → Pages).
   Dán 3 URL vào listing.md.
2. **Tên trước tiên.** **Tên store = cụm nhu cầu đã đo + brand** (`store_name.py`): chạy `python3 scripts/store_research.py rank "<cụm>" … --app <id>` → dán bảng vào `## Từ khoá đã đo`. Tên phải chứa nguyên một cụm có Gợi ý `có`; brand chưa nổi (`Brand known: no`) thì cụm đứng **đầu**, brand ra sau: `Duplicate File Finder - Sweepy`, không phải `Sweepy: …`. Người ta tìm bằng việc cần làm — tên riêng chưa ai nhớ. Subtitle giữ một cụm đã đo khác. **Không nhãn hiệu Apple trong tên** (Mac, iPhone, iPad, iOS, Apple…) — Guideline 5.2.5, cả tên store lẫn tên hiện trên máy; "Declutter - Mac Fix Kit" bị từ chối 2026-10-22; đổi tên giữ nguyên bundle id. Checker FAIL (`store_name.apple_marks`).
   **Nhưng không lấy tên loại app bão hoà** (`flashcard maker`, `pdf scanner`, `ai chat`…) dù cụm đó nhiều lượt gõ nhất — chọn cụm của ngách mình; checker WARN `SATURATED`. Capture Words bị 4.3(a) Spam vì `Flashcard Maker: …` (`reference/README-APP-PUBLISH-01-GUIDELINE-4-3-SPAM.md`). Review Notes luôn có đoạn "What makes this app different". Checker FAIL nếu tên không theo luật. Play Title theo cùng luật.
   **iOS:** App Name (`<cụm đã đo> - <Brand>`) · Subtitle (cụm đã đo khác, không lặp chữ của tên) · Keywords (100 byte, `a,b,c` không dấu cách,
   không lặp từ trong tên/subtitle, không `free/app/best`) · Description (150 ký tự đầu: app gì, cho ai, khác gì) ·
   Review Notes (cách test subscription + không cần đăng nhập) · What's New (bản đầu: "First release."; sửa mỗi lần tăng version).
3. **Play:** Title · Short description (80 — dòng người ta đọc đầu tiên) · Full description (có thể dùng lại mô tả iOS) ·
   Release notes (≤ 500 ký tự, thường dùng lại What's New).
   Play đọc cả full description để xếp hạng → dùng tự nhiên các cụm từ khoá, không nhồi.
4. **Category, Copyright, Contact, Subscriptions** (Product ID y hệt money.md).
5. **Data safety / App Privacy:** mỗi SDK trong pubspec một dòng. RevenueCat: *Purchase history* + mã người dùng ẩn danh,
   mục đích *App functionality*, **không** tracking. Không analytics → không khai analytics.
6. **Ảnh chụp** (bên dưới) → **Graphics**.
7. `python3 scripts/check_listing.py apps/ACTIVE/<slug>` tới khi 0 FAIL.
8. `python3 scripts/publish_kit.py <slug>` → `publish/` (mỗi ô một file + ảnh + manifest cho ShotMatic) — người dùng copy từ đây, không mở listing.md.

## Ảnh chụp màn hình — ảnh THẬT của app

Apple 2.3.3: ảnh phải cho thấy app đang dùng. Chữ quảng cáo đặt **quanh** ảnh thật được, vẽ giả giao diện thì không.

Kịch bản 5–6 khung (viết vào bảng `## Screenshots` trước khi chụp):

| # | Vai trò | Caption ≤ 5 chữ |
|---|---|---|
| 1 | Kết quả người dùng nhận (màn đẹp nhất, có dữ liệu thật) | lời hứa |
| 2 | Hành động chính (chạm để làm việc chính) | động từ |
| 3 | Tiến bộ / thống kê | phần thưởng |
| 4 | Tính năng Pro nổi bật | giá trị Pro |
| 5 | Tuỳ biến / chế độ tối | cá nhân hoá |
| 6 | Riêng tư, không quảng cáo (nếu đúng) | xoá nỗi lo |

Đưa app tới đúng trạng thái (dữ liệu mẫu đẹp), rồi:

```bash
python3 scripts/run_app.py shot <slug> --platform ios --name 01      # store/ios/01.png 1320×2868, 9:41, pin đầy, không alpha
python3 scripts/run_app.py shot <slug> --platform android --name 01  # store/android/01.png 1080×1920, không alpha
```

Thêm caption + nền: fastlane `frameit`, skill cộng đồng `store-screenshots` / `claude-skill-aso-appstore-screenshots`,
hoặc Figma/Canva — bảng công cụ trong `store-assets.md`. Kích thước sau khi ghép phải giữ nguyên.

**Muốn ảnh kiểu quảng cáo** (cảnh có người, nỗi đau, tay cầm máy — không chỉ screenshot + chữ): `/app-store-art`.
Màn hình trong cảnh vẫn là ảnh chụp thật ở bước này; bộ ghép ra `store/art/out/`, chọn khung nào thì trỏ cột iOS vào đó.
App vui/học/sưu tầm → mạch **sticker kiểu CapWords** (nền pastel, sticker đồ vật quanh máy, khung 1–2 nối liền) trong
playbook của `/app-store-art`. Website: 3 trang pháp lý ở bước này. Landing bán hàng (kiểu CapWords) làm ở `/app-marketing` Pha 2b
— cùng `make_site.py`, thêm `landing.md`.

**Icon Play 512** = icon-1024 thu nhỏ (`sips -z 512 512 store/icon-1024.png --out store/android/icon-512.png`).
**Feature graphic 1024×500**: viết prompt nền (không chữ, không giao diện giả) cho image generator, người dùng tạo, Claude chỉ crop/bỏ alpha.

## Việc của người dùng

Đăng site · email hỗ trợ thật · bảng hỏi xếp hạng tuổi (Apple Age Rating, Google IARC) · duyệt lần cuối chữ trên store.

LEARNED.md mục **Bước 10** · `scripts/app.py log` · tiếp theo `/app-publish`.

## Sau khi live — listing chưa xong

Vòng lặp trong `aso-advanced.md`: In-App Events (thêm chữ được index mà không cần build mới), thử nghiệm icon bằng
Product Page Optimization, sửa chữ theo từ khoá thật từ Search Ads / review. Việc này thuộc `/app-grow`.
