---
name: app-store-art
description: "Skill phụ của bước 10 (listing) và 12 (marketing) — làm bộ ảnh store KIỂU QUẢNG CÁO thay vì chỉ screenshot + chữ: mỗi khung kể một nhịp nỗi đau → tính năng → kết quả bằng cảnh có người thật (học sinh nhức đầu trước đống sách, tay cầm điện thoại đưa camera lên trang vở, người ôn bài trên xe buýt…) do Codex/ChatGPT sinh, còn màn hình điện thoại trong cảnh luôn là ẢNH CHỤP THẬT của app (Apple 2.3.3) được script dán vào vùng màn hình xanh #00FF00 hoặc đặt phẳng ở nửa dưới, chữ do script viết cho sắc nét. Claude viết Story + Style lock + prompt cảnh từng khung + jobs.json (tuyến C của core:asset-prompt), Codex sinh cảnh, Claude ghép bằng compose_store_art.py ra bộ 6.9\" 1320×2868 + 6.5\" 1284×2778, Read từng ảnh, kiểm bằng check_store_art.py. Use when 'ảnh store kiểu marketing', 'hình quảng cáo app', 'screenshot có người', 'ảnh store có học sinh', 'lifestyle screenshot', 'hình camera đẩy lên', 'ảnh store đẹp hơn chỉ screenshot', 'hero image app store', 'ảnh store kiểu capwords', 'sticker quanh điện thoại', 'ảnh store nối 2 khung', 'ảnh marketing tính năng chính', 'store art'. Không tự vẽ cảnh bằng SVG/Pillow, không để AI vẽ giao diện app giả, không hứa tính năng app không có."
argument-hint: "[slug]"
user-invocable: true
---

# Store art — ảnh store kể chuyện, màn hình thật

> **Tuyến chạy do skill cha `core:asset-prompt` quyết định — đọc nó trước.** Codex/ChatGPT → sinh cảnh luôn (tuyến A).
> Claude → viết prompt + `store/art/jobs.json` (tuyến C) rồi DỪNG, chờ cảnh về `store/art/raw/`.
> Không bao giờ tự vẽ cảnh bằng SVG / HTML / Pillow. Prompt đã xuất chưa phải ảnh đã xong.

**Một việc:** `python3 scripts/check_store_art.py apps/ACTIVE/<slug>` in `0 FAIL` — bộ ảnh ghép ở `store/art/out/`.

Vì sao có skill này: `/app-listing` chỉ ra screenshot thật + chữ — đúng luật nhưng giống mọi app khác. Người lướt store
quyết định trong ~3 giây ở 2–3 khung đầu; khung có **người đang gặp đúng nỗi đau** + **khoảnh khắc app gỡ nó** bán tốt hơn
màn hình trơn. Skill này thêm phần "cảnh" mà không phá luật 2.3.3 (ảnh phải cho thấy app đang dùng).

Đọc: [references/store-art-playbook.md](references/store-art-playbook.md) (mạch 5 khung, mạch sticker kiểu CapWords, mẫu prompt cảnh, luật Apple,
lỗi Codex hay gặp) · `context-ai/research-<slug>.md` (nỗi đau thật, chữ người dùng tự nói) · `spec.md` `## MVP`
(chỉ bán tính năng đã có) · `design.md` `## Colors` · `listing.md` `## Screenshots` · preset `store-art` trong `.claude/repo-profile.yaml`.

## 1. Story — trước khi viết prompt nào

Điền `## Story` trong `store_art.md` (khuôn: `templates/store_art.md`): **ai** đang khổ (cụ thể: "học sinh lớp 11 ôn thi sinh"),
**lúc nào** (tối trước hôm kiểm tra), **tính năng nào** gỡ (đúng tên trong spec), **kết quả** họ nhận. Không có nỗi đau
trong research thì lấy từ autocomplete/review đối thủ — không bịa số, không bịa lời người dùng.

## 2. Frames — mỗi khung bán MỘT tính năng có thật

Bảng `## Frames` 3–10 khung (thường 5). Cột:
- **Tính năng (spec)** — dòng `## MVP` khung đó bán. Không có trong spec thì không được vẽ, không được viết (2.3.1).
- **Caption** ≤ 40 ký tự, động từ hoặc lời hứa; **Dòng phụ** ≤ 1 câu. Viết đúng điều app làm: app tạo thẻ bằng AI thì
  "AI writes your flashcards", **không** "AI tutor" nếu app không dạy kèm. Checker chặn best / #1 / guarantee / donate.
- **Chú thích** (tuỳ chọn) — dòng nhỏ ở đáy ảnh cho điều kiện kèm theo, vd "AI cards need Apple Intelligence on iOS 26".
- **Ảnh app thật** — ảnh chụp từ `run_app.py shot` / simulator (thường `store/ios/raw/NN.png`). Thiếu màn nào → chụp thêm,
  không để Codex vẽ giao diện.
- **Bố cục** — `green`: cảnh có tay cầm điện thoại **nhìn thẳng**, màn hình tô xanh `#00FF00` phẳng → script dán ảnh thật vào,
  ngón tay đè lên màn vẫn giữ. `bottom`: cảnh làm nền (người, bàn học, đồ vật ở nửa trên/hai bên), script đặt điện thoại
  phẳng ở nửa dưới. Khung đầu nên là `green` (khoảnh khắc dùng app); khung chi tiết nên là `bottom` (màn to, đọc được).

## 3. Prompts cảnh

Một khối `### NN` mỗi khung trong `## Prompts`, 6 phần như `core:asset-prompt`: **Subject · Style (dán Style lock) ·
Composition · Palette · Spec · Negative**. Bắt buộc trong mọi prompt:
- `Spec`: `1320x2868 portrait PNG, opaque` · **top 22% calm and uncluttered** (chỗ đặt chữ) · `green`: "the phone faces the
  camera straight on, screen is a flat solid pure green #00FF00 rectangle with rounded corners, no reflections, no UI" ·
  `bottom`: "keep the lower 65% center area simple and low-detail — a phone will be placed there".
- `Negative`: text, letters, captions, logos, brand names, app UI, fake interface, watermark, extra fingers, distorted hands,
  green anywhere except the phone screen, real textbook brands, children under 13 (giữ app khỏi Kids Category).
- Người: tuổi đúng đối tượng (học sinh 16–22), đa dạng, biểu cảm rõ ở khung nỗi đau (mệt, nhăn trán) và khung kết quả (nhẹ nhõm).

Claude: xuất `store/art/jobs.json` (schema `core:asset-prompt`, `raw_dir` = `apps/ACTIVE/<slug>/source/store/art/raw`, `dest` cùng chỗ),
tạo sẵn thư mục raw, báo người dùng đem `jobs.json` sang Codex. Codex: sinh từng cảnh, lưu đúng `dest`.

## 4. Ghép + soát bằng mắt

```bash
python3 scripts/compose_store_art.py apps/ACTIVE/<slug>     # → store/art/out/ios/NN.png + ios-6.5/NN.png
python3 scripts/check_store_art.py apps/ACTIVE/<slug>
```

**Read từng ảnh ghép:** ảnh app nằm khít màn hình (không lệch, không lộ viền xanh), chữ không đè mặt người, tay/ngón bình
thường, không có chữ/logo lạ Codex lén vẽ, khung tối/sáng đọc được. Sai → sửa prompt, sinh lại cảnh; không lấy Pillow đắp.

## 5. Đưa vào listing

Người dùng chọn bộ nào lên store (bộ quảng cáo, bộ screenshot + chữ, hoặc trộn — vd khung 1–2 quảng cáo, 3–5 screenshot).
Sửa cột iOS trong `listing.md` `## Screenshots` trỏ tới `store/art/out/ios/NN.png`, chạy `check_listing.py`.
Cùng bộ cảnh dùng lại cho `/app-marketing`: mục `## Moments` của `landing.md` (cảnh ngang 16:10), `og.png`, bài đăng.

LEARNED.md (lời thường: cảnh do Codex vẽ, màn hình là ảnh thật, vì sao) · `scripts/app.py log` · tiếp theo `/app-listing` hoặc `/app-publish`.
