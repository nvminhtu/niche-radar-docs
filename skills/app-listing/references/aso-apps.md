# ASO cho app (không phải game) — giới hạn + cách viết

Giới hạn đối chiếu tài liệu chính thức **2026-09-06 → 2026-09-15**:
App Store Connect — developer.apple.com/help/app-store-connect/reference/app-information ·
screenshot-specifications · Google Play — support.google.com/googleplay/android-developer/answer/9859152 (chữ),
answer/9866151 (ảnh), answer/9898842 (metadata policy).

## 1. Giới hạn cứng

| Ô | App Store | Google Play |
|---|---|---|
| Tên | App Name **30** | Title **30** |
| Dòng phụ | Subtitle **30** | Short description **80** |
| Từ khoá | Keywords **100 byte**, một ô, phẩy ngăn cách, mỗi từ > 2 ký tự | không có ô — Play đọc tên + mô tả |
| Mô tả | Description **4000**, chữ thường, không HTML | Full description **4000** |
| Sửa không cần review | Promotional Text **170** | — |
| Ảnh điện thoại | 6.9" **1320×2868** (hoặc 6.5" 1284×2778 khi không có 6.9"), 1–10 ảnh, **không alpha** | 2–8 ảnh, cạnh 320–3840, cạnh dài ≤ 2× cạnh ngắn, khuyên ≥ 1080×1920, không alpha |
| Icon | 1024×1024 nằm **trong bản build**, không alpha | 512×512 PNG ≤ 1 MB tải lên Console |
| Ảnh ngang quảng bá | — | Feature graphic **1024×500**, không alpha |
| Bắt buộc khác | Copyright · Support URL · Privacy Policy URL · (subscription) Terms of Use | Privacy Policy URL · email liên hệ · Data safety · IARC |

**Byte, không phải ký tự** cho Keywords: từ tiếng Việt có dấu tốn 2–3 byte mỗi ký tự có dấu.

## 2. Trọng số xếp hạng

App Store: **Tên > Subtitle > Keywords**; mô tả không được index cho tìm kiếm (nhưng người + công cụ AI đọc).
Google Play: **Title > Short description > Full description** — mô tả CÓ được index → viết cụm từ khoá tự nhiên, lặp vừa phải.
Cả hai: sau cú chạm, **hành vi** (tỉ lệ cài từ trang, giữ chân, đánh giá) quyết định hạng — xem aso-advanced.md §1.

## 3. Tên app

Công thức: `[Tên riêng]: [việc người ta gõ để tìm]` → `Sprout: Habit Tracker`. Tên riêng một mình không ai tìm ra.
Kiểm trùng: `python3 scripts/store_research.py search "<tên>"` + tìm trên Play. Không dùng tên/thương hiệu đối thủ.

## 4. Keywords (iOS)

- Nguồn từ thật: autocomplete (`store_research.py hints`), tên + subtitle 10 app đầu, lời review.
- Bỏ từ đã có trong Tên/Subtitle (Apple đã ghép sẵn), bỏ số ít/số nhiều trùng, bỏ `app`, `free`, `best`.
- Viết `habit,routine,daily goals,streak` — không dấu cách sau dấu phẩy.
- Chọn cụm mà 10 app đầu có số đánh giá hàng trăm/nghìn, không phải hàng triệu.

## 5. Mô tả — 150 ký tự đầu làm hết việc

Trả lời theo thứ tự, câu bình thường: **app gì · cho ai · khác gì**. Sau đó: 3–5 gạch đầu dòng tính năng **có thật** →
Free vs Pro → một câu về subscription (giá theo chu kỳ, tự gia hạn, huỷ ở đâu) → link Terms + Privacy (iOS).
Không kêu gọi quyên góp.

Mẫu câu subscription (sửa theo money.md):

```
Pro is available as a monthly or yearly auto-renewing subscription. Payment is charged to your Apple ID account at
confirmation of purchase. The subscription renews automatically unless cancelled at least 24 hours before the end of the
current period. Manage or cancel in your account settings.
Terms of Use: <TERMS_URL>
Privacy Policy: <PRIVACY_URL>
```

## 6. Metadata policy Google Play — cấm trong title/icon/tên dev

Xếp hạng/giải thưởng ("#1", "Best of Play", "Editor's Choice"), giá/khuyến mãi ("free", "% off", "sale"), emoji,
ký tự lặp ("!!!"), VIẾT HOA TOÀN BỘ (trừ tên thương hiệu). `check_listing.py` FAIL với cụm policy nêu nguyên văn, WARN
với `best/top/new/free` vì có thể là tên riêng.

## 7. Danh mục

Chọn danh mục **nơi người dùng tìm**, không phải nơi ít đối thủ nhất. App thói quen: Health & Fitness hoặc Productivity;
app học: Education (tránh Kids Category nếu có subscription + analytics — xem app-money playbook §5).

## 8. Bản địa hoá

Mỗi ngôn ngữ trên store có Tên/Subtitle/Keywords/ảnh riêng, được index riêng. Bản đầu: tiếng Anh (Mỹ). Thêm tiếng Việt khi
app có giao diện tiếng Việt thật — dịch cả caption ảnh, không để ảnh tiếng Anh trên trang tiếng Việt.

## 9. Skill cộng đồng tham khảo (đọc lấy ý, luật ở trên thắng)

`Eronred/aso-skills` (keyword-research, metadata-optimization, screenshot-optimization, android-aso, review-management) ·
`alirezarezvani/claude-skills` marketing-skill/app-store-optimization · `TimBroddin/app-store-aso-skill` (validator giới hạn Apple) ·
`adamlyttleapps/claude-skill-aso-appstore-screenshots` (ảnh store). Bảng cài: reference/README-REFERENCES.md.
