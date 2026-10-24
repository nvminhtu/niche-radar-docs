---
name: app-mockup
description: "Bước 4b của pipeline app — sau CỔNG 3 (design duyệt), TRƯỚC khi dựng project: làm ảnh mockup cho từng màn trong spec.md để dev (người hoặc Claude) code bám theo và người dùng nhìn tận mắt app trông thế nào. Claude chọn 3–5 app tham khảo có doanh thu thật (TrustMRR / bảng top grossing / Mobbin) để học bố cục, viết Style lock + prompt từng màn từ design.md (màu hex, chữ, bo góc) và spec.md (màn, nút, chữ đúng từng từ); Codex/ChatGPT sinh ảnh (tuyến của core:asset-prompt); Claude nhặt ảnh về design/mockup/, Read từng ảnh, đối chiếu spec, chấm điểm đẹp theo thang 10 (dưới 8 sinh lại), ghi mockup.md và kiểm bằng check_mockup.py; màn hero dùng lại cho bài X / slideshow TikTok trước ra mắt. Không tự vẽ bằng SVG/HTML/Pillow. Use when 'mockup', 'vẽ màn hình trước khi code', 'app trông thế nào', 'cho dev xem giao diện', 'prompt mockup cho codex', 'tôi paste ảnh mockup vào raw rồi', 'mockup đẹp hơn', 'prototype chuẩn đẹp', 'học giao diện app doanh thu cao', or when scripts/app.py status says step 4b is next."
argument-hint: "[slug]"
user-invocable: true
---

# Bước 4b — mockup

> **Tuyến chạy do skill cha `core:asset-prompt` quyết định — đọc nó trước.**
> Codex/ChatGPT → sinh ảnh luôn (tuyến A). Claude → viết prompt + `jobs.json` (tuyến C) rồi DỪNG, chờ ảnh về
> `assets/raw/`; `asset-prompt/scripts/collect_raw.py --apply` đổ ảnh vào `design/mockup/`.
> Không bao giờ tự vẽ mockup bằng SVG / HTML / Pillow / screenshot. Prompt đã xuất chưa phải mockup đã xong.

**Một việc:** `mockup.md` 0 FAIL — mỗi màn trong bảng `## Màn hình` của spec.md có ảnh mockup thật trong `design/mockup/`.
Vì sao có bước này: code thẳng từ bảng màu thì tới bước chạy app mới thấy giao diện, lúc đó sửa tốn gấp nhiều lần
(PageCards 2026-10-01: nút bị bẻ chữ, chữ không phóng to — lộ ra ở bước review). Ảnh mockup rẻ, sửa bằng một prompt.

Đọc trước: `spec.md` (`## Màn hình`, `## MVP`), `design.md` (Colors, Typography, Spacing, Screens, Paywall),
`money.md` (có paywall không), `.claude/repo-profile.yaml` preset `app-mockup`.

## 0. Tham khảo — học từ app đang có tiền thật

Đẹp = giống app top cùng thể loại đã chứng minh người ta trả tiền, không phải đẹp theo ý Claude.
Chọn **3–5 app** cùng thể loại, ghi vào `## Tham khảo` (App · Nguồn · Doanh thu · Học gì):
- Nguồn tìm: đối thủ trong `research/<niche>.md` · [TrustMRR Mobile Apps](https://trustmrr.com/category/mobile-apps)
  (doanh thu xác minh qua RevenueCat) · bảng top grossing (`store_research.py`) · [Mobbin](https://mobbin.com) (màn thật đã ship).
- Doanh thu: số **kèm link nguồn + ngày**, hoặc ghi `chưa đo` (luật không bịa số — checker bắt số không có link).
- Học gì: **bố cục / nhịp màn** (vd "số calo to giữa màn, ảnh món ở trên", "onboarding 5 câu → màn kế hoạch → paywall"),
  không chép logo, tên, màu thương hiệu, chữ của họ.
- Không mở được trang (mạng chặn) → dùng trích đoạn tìm kiếm, ghi rõ; hoặc nhờ người dùng dán link/ảnh chụp.
Mẫu đã đo: `research/<ngày>-<chủ-đề>.md`.

## 1. Style lock — chuẩn đẹp

Một khối tiếng Anh dùng chung cho **mọi** prompt — chép nguyên, không diễn đạt lại:
thiết bị (iPhone / Android / cửa sổ Mac), nền + màu chính/phụ bằng hex lấy từ bảng Colors, font hệ thống,
bo góc, lưới khoảng cách, kiểu icon (SF Symbols / Material Symbols), sáng hay tối, "flat UI screenshot".
Thêm các câu chất lượng này (bản tiếng Anh chép vào khối):
- **Một hero mỗi màn** — một con số / ảnh / nút chính to nhất, chiếm ~1/3 màn; mọi thứ khác nhỏ và dịu hơn
  (`one clear focal point, strong visual hierarchy`).
- **Một màu nhấn duy nhất** cho hành động chính; còn lại trung tính (`single accent color used only for the primary action`).
- **Khoảng thở**: lưới 8pt, lề 16–20pt, tối đa 3 cỡ chữ mỗi màn (`generous whitespace, max 3 font sizes`).
- **Chiều sâu nhẹ**: thẻ có bóng mềm hoặc viền mảnh, không gradient loè loẹt (`subtle soft shadows, no heavy gradients`).
- **Như app thật đã ship trên App Store 2026**, không phải concept Dribbble (`looks like a shipped top-grossing App Store app,
  pixel-perfect, crisp text`).

## 2. Danh sách màn

Mỗi màn trong bảng `## Màn hình` của spec = ít nhất một dòng ở `## Screens` (tên gõ **đúng** như spec — checker so tên).
Thêm dòng cho trạng thái quan trọng ghi ở `design.md` `## Screens`: rỗng (lần đầu mở), hết lượt/giới hạn, lỗi.
Money `Model: free` → màn Paywall vẫn có trong spec thì làm một dòng ghi rõ "ẩn ở v1" hoặc xoá màn khỏi spec trước.
Bản tối: nên có cho Home + một màn chính; còn lại ghi `—`.

**Chuỗi màn ra tiền** — app doanh thu cao đổ công nhất vào đây (Cal AI: 61 thí nghiệm chỉ riêng paywall sau onboarding):
onboarding vài câu cá nhân hoá → màn "kết quả / kế hoạch của bạn" → paywall. Spec có chuỗi này thì vẽ **đủ từng màn
theo đúng thứ tự** để thấy liền mạch. Spec chưa có mà money.md có paywall → **không vẽ lén**: ghi đề xuất ở
`## Ghi chú cho dev` và hỏi người dùng có thêm vào spec không.

## 3. Prompt từng màn

6 phần như `core:asset-prompt`: **Subject · Style (dán Style lock) · Composition · Palette · Spec · Negative.**
- Composition đi từ trên xuống: thanh trên (tiêu đề, nút) → nội dung (dữ liệu mẫu **thật**, như người dùng sẽ thấy) →
  nút chính. Chỉ vẽ nút/tính năng có trong spec — không thêm.
- Chữ trên màn chép đúng từng chữ trong ngoặc kép, đúng ngôn ngữ app (preset `text: verbatim`).
- Spec: kích thước theo preset (`1024x1536` điện thoại, `1536x1024` Mac), **không** khung điện thoại, không bàn tay,
  không nền marketing — chỉ màn hình phẳng.
- Negative: watermark, logo lạ, khung thiết bị, chữ lorem ipsum, nút không có trong spec, "Item 1/Title/Button",
  chữ méo/lỗi chính tả, quá nhiều màu, mọi thứ cùng cỡ.
- Dữ liệu mẫu **có chất người**: tên thật, số cụ thể, ngày gần đây, ảnh thật (món ăn, sách…) — màn đẹp nhờ nội dung
  đáng tin, không nhờ trang trí.

Ghi prompt vào `mockup.md` `## Prompts`. Claude (tuyến C): xuất thêm `design/mockup/jobs.json` đúng schema của
`core:asset-prompt` (`raw_dir` = `apps/ACTIVE/<slug>/source/assets/raw`, `dest` = `apps/ACTIVE/<slug>/design/mockup/<nn>-<màn>-<light|dark>.png` — tính từ gốc repo, chạy script ở gốc repo),
tạo sẵn thư mục raw, rồi báo người dùng: đem `jobs.json` (hoặc từng prompt) sang Codex, ảnh về paste vào raw.

## 4. Nhặt ảnh + soát bằng mắt

```bash
python3 .agents/skills/asset-prompt/scripts/collect_raw.py apps/ACTIVE/<slug>/design/mockup/jobs.json --apply
python3 scripts/check_mockup.py apps/ACTIVE/<slug>/context-ai/mockup.md
```

**Read từng ảnh** rồi soát: đúng màn, đủ nút trong spec, không thừa tính năng, chữ đọc được và đúng chính tả,
màu gần token. Sai nặng (thiếu nút chính, sai màn, chữ loạn) → sửa prompt, sinh lại — không lấy ảnh khác đắp vào.
Sai nhỏ (Codex vẽ lệch một icon) → ghi ở `## Ghi chú cho dev`: spec + design.md luôn thắng ảnh.

**Chấm điểm đẹp** — mỗi ảnh sáng một dòng ở `## Chấm điểm`, 5 tiêu chí × 2 điểm = 10:

| Tiêu chí | 2 điểm khi |
|---|---|
| Hero | nhìn 1 giây biết màn này để làm gì, một tiêu điểm rõ |
| Token | màu/bo góc/chữ khớp Style lock, chỉ một màu nhấn |
| Chữ | đúng từng chữ spec, sắc nét, không méo, ≤ 3 cỡ |
| Nội dung | dữ liệu mẫu thật, không placeholder |
| Ngang app top | đặt cạnh app trong `## Tham khảo` không thấy kém |

**Dưới 8 → sửa prompt, sinh lại** (checker FAIL). Chấm thật bằng mắt sau khi Read — không chấm cho qua.

## 5. Bàn giao

Gửi người dùng ảnh ghép các màn (SendUserFile) và nói bằng lời thường: có mấy màn, màn nào còn thiếu, chỗ nào ảnh
khác spec. Không có cổng mới — CỔNG 3 đã duyệt design; người dùng muốn đổi gì thì sửa design.md/spec rồi sinh lại ảnh.

## 6. Dùng lại cho quảng bá trước ra mắt

Mockup đẹp là nguyên liệu marketing sớm nhất (chi tiết ở `/app-marketing`):
- **X build-in-public**: ảnh màn hero + 1 câu "đang làm app X cho Y" — ghi rõ là bản thiết kế, chưa phải app thật.
- **Slideshow TikTok**: slide 1 câu móc < 8 chữ, slide cuối là màn hero.
- **Không** dùng mockup làm ảnh store — ảnh store phải chụp app thật (`/app-listing`, `run_app.py shot`).

App dựng project trước 2026-10-01 được `status` ghi "bỏ qua"; muốn làm mockup cho màn mới của app cũ thì chạy skill
này bình thường — có `mockup.md` là checker kiểm.

LEARNED.md mục **Bước 4b** · `scripts/app.py log` · tiếp theo `/app-scaffold` (dev code bám `design/mockup/`).
