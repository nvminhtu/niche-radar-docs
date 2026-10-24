---
name: app-video
description: "Skill phụ của bước 10–13 — làm VIDEO cho app từ bản quay app thật bằng Remotion (React dựng video bằng code, Claude tự render được): demo ngang 1920×1080 cho landing + YouTube (dùng luôn làm App Preview nếu 15–30 s), shorts dọc 1080×1920 cho landing / YouTube Shorts / TikTok / Reels, mỗi short có poster jpg (khung đầu = hook + hình app, không màn chữ trơn). Tạo dự án bằng scripts/new_video.py từ templates/video-remotion, chỉ sửa src/brand.ts + src/scenes.ts, render bằng render.sh, kiểm bằng scripts/check_video.py (kích thước khớp tên, h264, faststart, short 5–60 s có poster, App Preview 15–30 s có tiếng), Read poster trước khi báo xong; ghi videos.md (file nào đăng ở đâu) + file metadata YouTube để người dùng tự đăng; phân loại đưa vào repo video hub để nhúng landing / README GitHub. Use when 'làm video', 'video short', 'video demo app', 'remotion', 'shorts cho landing', 'youtube shorts', 'tiktok video app', 'reels', 'app preview video', 'video giới thiệu', 'poster video', 'video landing bị trắng', 'thumbnail video', 'kho video', 'host video github', 'chèn video vào readme', 'các loại video marketing'. Không bịa số/testimonial, không cảnh giao diện giả, không nhét nhạc có bản quyền vào file, không đăng/đăng nhập YouTube thay người dùng."
argument-hint: "[slug] [loại video]"
user-invocable: true
---

# App video — quay thật, dựng bằng code, đăng nhiều chỗ

**Một việc:** `python3 scripts/check_video.py <slug>` in `0 FAIL`, mọi poster đã Read, `marketing/video/videos.md` ghi
file nào đăng ở đâu. Video là thứ bán hàng — không phải đồ trang trí: mỗi video phải **cho thấy app thật làm xong một việc**.

Đọc: [references/video-playbook.md](references/video-playbook.md) (§1 các loại video · §2 luồng YouTube · §3 cách làm khác
ngoài Remotion · §4 host video / repo hub / README GitHub · §5 thông số) · `spec.md` `## MVP` (chỉ quay tính năng đã có) ·
`design.md` `## Colors` · research/review (câu nỗi đau thật cho hook) · Promo Desk `VideoFormats.swift` (17 kiểu short, id `format:`).

## 1. Chọn loại — bộ tối thiểu cho một app

| # | File | Dùng ở |
|---|---|---|
| 1 | `<slug>-demo-1920x1080.mp4` + poster | landing (khối video), YouTube dài, App Preview nếu 15–30 s & không giá/không stock |
| 2 | 3 × `<slug>-<việc>-1080x1920.mp4` + poster | landing (khối shorts), YouTube Shorts, TikTok, Reels — **cùng file** |

Muốn thêm (hero loop, before/after, race, tutorial dài…): chọn từ playbook §1, ghi vào `videos.md` trước khi làm.
Khuôn `templates/video-remotion` = bậc 1 (demo + chữ). Bậc 2–4 (giọng AI + phụ đề từng chữ, cắt dán stock nỗi đau,
bắt trend/Stitch) theo spec JSON: chép cách làm của `apps/ACTIVE/desk-apps/sweepy/marketing/video/make_short.py` + `specs/README.md`.

**Short theo spec (4 loại):** 1 demo + nhạc · 2 giọng đọc + phụ đề từng chữ · 3 cắt dán stock/split/meme · 4 bắt trend
(dựng lại hoặc bản trả lời để Stitch). Mỗi video = 1 file `specs/<id>.json`, render bằng `make_short.py` (composition `Spec`,
tự chuẩn −14 LUFS). Mẫu đang chạy: `apps/ACTIVE/desk-apps/sweepy/marketing/video/` — đọc `specs/README.md`; app khác thì chép
`src/Spec.tsx` + `make_short.py` + `specs/` sang rồi đổi tên app/màu. Không tải video người khác về cắt ghép (dùng Stitch/Duet).

## 2. Quay bản thô — luôn là app THẬT, dữ liệu mẫu

| Loại app | Lệnh quay |
|---|---|
| Mac | script bấm theo toạ độ như `apps/ACTIVE/desk-apps/sweepy/source/store/macos-demo-video.sh` — chạy trong **Terminal.app** (Terminal của Claude không có quyền Screen Recording) |
| Web / Tauri | Playwright `recordVideo` như `apps/ACTIVE/desk-apps/markdown-viewer/marketing/video/record-demo.cjs` (có con trỏ giả) |
| iOS | `xcrun simctl io booted recordVideo --codec=h264 raw.mp4` (Ctrl-C để dừng) |
| Android | `adb shell screenrecord /sdcard/raw.mp4` → `adb pull` |

Dữ liệu mẫu, không lộ file/tên/email thật. Ghi lại giây bắt đầu từng thao tác (script in mốc) để điền `scenes.ts`.

## 3. Dựng

```bash
python3 scripts/new_video.py <slug>                 # → apps/…/<slug>/marketing/video/ (đã có thì dừng)
cd apps/ACTIVE/<slug>/marketing/video && npm install
sh prep.sh <bản quay> ../../store/icon-1024.png      # → public/demo.mp4 30 fps + icon
```
Sửa **chỉ 2 file**: `src/brand.ts` (tên, tagline, màu từ design.md, CTA, `ASPECT` của bản quay) và `src/scenes.ts`
(`SCENES` = giây + chữ từng cảnh; `SHORTS` = hook + cảnh). `npm run studio` để dò giây và xem. Rồi `npm run render`.

Luật chữ: hook ≤ 8 từ, gọi đúng nỗi đau (lấy từ review/autocomplete, không bịa); tiêu đề cảnh = động từ + kết quả;
đọc được khi tắt tiếng; tiếng Anh nếu đăng oneclicktool / store US. Không giá trong bản dùng làm App Preview.

## 4. Kiểm — máy trước, mắt sau

```bash
python3 scripts/check_video.py <slug>
```
Rồi **Read mọi `*-poster.jpg`** + 2–3 khung giữa (`npx remotion still <Id> /tmp/f.jpg --frame=N`): chữ có bị cắt, cửa sổ
app có lệch, cảnh có đúng tính năng trong chữ không. Chưa Read thì chưa được nói "xong".

## 5. Phân phối (Claude soạn, người dùng bấm đăng)

- **Landing:** `<video src poster muted playsinline loop preload="none">` — **luôn có `poster`** (không thì trình duyệt hiện
  khung 0:00 trơn). Demo dài → nhúng YouTube kiểu facade (ảnh poster, bấm mới tải iframe). Chi tiết §4 playbook.
- **YouTube:** mỗi video một file `marketing/youtube/NN-<loại>.md` (title · description có link `ct=youtube` · tags ·
  thumbnail prompt cho Codex · ô `Đã đăng`) — mẫu `apps/ACTIVE/desk-apps/sweepy/marketing/youtube/01-app-preview.md`.
  Shorts gắn **Related video** về video demo dài (§2).
- **Hub / README GitHub:** chép bản web (≤ 8 MB) vào repo hub theo §4; README dùng poster bấm ra YouTube.
- Cập nhật `videos.md` + một mục trong `LEARNED.md` (làm gì · file nào · lần sau gõ gì).

## Không làm

Không cảnh giao diện do AI vẽ (chỉ b-roll stock/AI cho cảnh *nỗi đau*, ghi nguồn `public/stock/SOURCES.md`) · không nhạc
có bản quyền trong file (nhạc trend gắn trong app TikTok/YouTube lúc đăng) · không số liệu/testimonial bịa · không stock
trong App Preview · không đăng nhập YouTube/TikTok, không bấm Publish · không nút/chữ quyên góp.
Remotion miễn phí cho cá nhân và công ty ≤ 3 người — đông hơn phải mua license công ty (remotion.dev/license).
