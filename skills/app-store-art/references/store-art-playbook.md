# Store art playbook — ảnh store kể chuyện

## Mạch 5 khung (mặc định)

| # | Nhịp | Cảnh | Ảnh app thật | Bố cục |
|---|---|---|---|---|
| 1 | **Nỗi đau → hành động chính** | người đang khổ đúng lúc khổ, tay đưa điện thoại lên làm việc chính | màn bắt đầu việc chính | green |
| 2 | **Phép màu** — kết quả tức thì | đồ vật/người thay đổi trạng thái (trang sách → thẻ bay ra; người thở phào) | màn kết quả | bottom |
| 3 | **Thói quen** — dùng lại mỗi ngày | người dùng app ở chỗ đời thường (xe buýt, giường, quán) | màn dùng hằng ngày | green hoặc bottom |
| 4 | **Ngăn nắp / kiểm soát** | bàn gọn, đồ vật xếp theo nhóm | màn danh sách/quản lý | bottom |
| 5 | **Xoá nỗi lo** — riêng tư, offline, không quảng cáo (chỉ khi đúng) | đêm khuya, máy bay, chỗ không mạng | màn tối / Settings | bottom |

2–3 khung đầu quyết định lượt cài — dồn cảnh mạnh nhất vào khung 1. Khung sau có thể là screenshot + chữ thường.

## Mạch kiểu CapWords (ADA 2025) — app vui, học, trẻ

Bộ 9 ảnh store của [CapWords](https://apps.apple.com/us/app/capwords-ai-photo-vocabulary/id6738896465) (soi 2026-10-01)
không có cảnh người. Thứ bán là **sticker đồ vật thật** bay quanh điện thoại. Hợp app có "vật phẩm" để khoe
(sticker, thẻ, ảnh kết quả, huy hiệu):

| Khung | CapWords làm | Mình áp |
|---|---|---|
| 1 | Hero: tên app + câu hứa to, chữ tròn mập, sticker xếp quanh. Huy hiệu giải (có thật) ở đáy | caption = lời hứa; huy hiệu chỉ khi có |
| 1→2 | **Ảnh toàn cảnh nối 2 khung**: điện thoại nghiêng vắt qua mép khung 1 sang khung 2 | Codex sinh 1 cảnh 2640×2868 → cắt đôi (`sips --cropOffset`) thành raw 01 + 02 |
| 2–8 | Mỗi khung 1 câu ≤ 5 chữ ("Turn your world into words", "Ditch boring word lists") + 1 điện thoại thẳng + vài sticker | bố cục `green` (máy thẳng) |
| | **Nền mỗi khung một màu pastel** (vàng, hồng, tím, olive), cùng độ sáng | màu lấy từ `design.md` |
| 9 | Review thật dạng thẻ trắng 5 sao | chỉ khi đã có review thật, chép nguyên văn + tên |

Style lock mẫu (**Sticker**): `flat solid pastel background <hex>, playful die-cut stickers of everyday objects with thick white
borders and soft drop shadows scattered around the phone, slightly rotated, photographic objects, cheerful and clean, lots of
breathing room`. Sticker phải là **vật app thật sự nhận diện/tạo ra** (2.3.1). Không vẽ sticker tính năng app không có.

## Luật Apple — vì sao màn hình luôn phải là ảnh thật

| Luật | Áp vào ảnh |
|---|---|
| 2.3.3 | Ảnh phải cho thấy app đang dùng, không chỉ title art/splash. Cảnh + chữ quanh ảnh thật: được. AI vẽ giao diện: không |
| 2.3.1 / 2.3.7 | Không hứa tính năng app không có ("AI tutor" khi app chỉ tạo thẻ), không "#1", "best" không kiểm được |
| 2.3.8 | Hình hợp 4+: không bạo lực, không gợi dục, kể cả khi app rating cao hơn |
| 2.3.9 | Người trong ảnh: AI sinh hoặc có quyền dùng; dữ liệu trên màn là dữ liệu mẫu |
| 5.2.1 | Không logo/thương hiệu người khác (bìa sách Pearson, logo trường, áo có brand) |
| 3.2.2(iv) | Không chữ quyên góp |

Google Play (khi app có Android): ảnh 1080×1920 cùng luật "không hình gây hiểu lầm" — chạy lại compose với cỡ Play sau.

## Mẫu prompt cảnh

**green (tay cầm máy, camera đẩy lên):**
```
Subject: a tired high-school student (17) at a cluttered desk at night, stack of open textbooks and highlighted notes,
holding a smartphone up with one hand toward the camera as if about to scan a page.
Style: <Style lock>
Composition: phone held upright in the lower-middle of the frame, facing the camera straight on (no tilt, no perspective),
screen fills most of the phone face; student's face visible behind/beside the phone, slightly frowning; textbooks at bottom.
Top 22% of the image is a calm plain wall/background with nothing important — headline goes there.
Palette: <hex từ design.md> for clothing, props and background accents.
Spec: 1320x2868 portrait PNG, opaque. The phone screen is a flat solid pure green #00FF00 rectangle with rounded corners,
no reflections, no glare, no UI, no notch drawn on it.
Negative: text, letters, captions, logos, brand names, app interface, fake UI, watermark, extra fingers, distorted hands,
green anywhere except the phone screen, children, real textbook covers
```

**bottom (cảnh nền, điện thoại phẳng đặt sau):**
```
Subject: <cảnh kết quả/thói quen>.
Style: <Style lock>
Composition: people and props in the upper-middle and along the left/right edges; keep the lower 65% center area simple,
soft and low-detail — a phone will be placed there. Top 22% calm for the headline.
Spec: 1320x2868 portrait PNG, opaque, no phone drawn.
Negative: <như trên> , phone, tablet, screen
```

## Style lock — chọn một kiểu, giữ cả bộ

- **Editorial photo** (thật, ấm): "warm natural light editorial photograph, shallow depth of field, soft film grain" — hợp app học tập, sức khoẻ.
- **3D soft clay**: "soft 3D clay render, rounded shapes, pastel lighting" — hợp app vui, trẻ.
- **Flat illustration**: "flat vector illustration, bold shapes, no outlines" — hợp app tiện ích.
- **Sticker** (kiểu CapWords): nền pastel phẳng + sticker đồ vật viền trắng quanh máy — hợp app học, sưu tầm, trẻ (mẫu ở mục trên).
Màu lấy hex trong `design.md` `## Colors` cho quần áo, đồ vật, nền — để cảnh và UI cùng một tông.

## Lỗi Codex hay gặp → cách sửa

| Lỗi | Sửa |
|---|---|
| Vẽ chữ/ giao diện lên màn hình | nhắc lại "screen is flat solid #00FF00, nothing on it" ở Spec và Negative |
| Màn hình nghiêng/ phối cảnh → ảnh dán bị méo | "facing the camera straight on, front view, no tilt" |
| Xanh lọt vào cảnh (cây, áo) → script dán nhầm | thêm "no green objects", đổi màu áo trong Palette |
| Tay 6 ngón, cổ tay gãy | "hand partially out of frame" hoặc đổi sang bố cục bottom |
| Chừa chỗ chữ không đủ → caption đè mặt | "top 25% plain wall" |
