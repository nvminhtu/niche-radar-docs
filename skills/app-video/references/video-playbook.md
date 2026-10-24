# Video playbook — loại video, luồng YouTube, cách làm, nơi host

## §1. Các loại video (landing · YouTube · store · GitHub)

Một bản quay app thật → dựng ra nhiều loại. Cột **Ai làm**: *Claude* = render bằng Remotion không cần ai; *Một nửa* =
máy dựng, người dùng thêm 1 thứ lúc đăng (nhạc trend, Stitch); *Tay* = phải có mặt/giọng người thật.

| # | Loại | Khung · dài | Đặt ở | Ai làm | Ưu tiên |
|---|---|---|---|---|---|
| 1 | **Hero loop** — 1 thao tác chính lặp vòng, không chữ | 16:10 / 16:9 · 4–8 s · ≤ 3 MB | đầu landing, cạnh nút tải | Claude | ★★★ |
| 2 | **Demo** — icon → 5–7 cảnh có tiêu đề | 16:9 1920×1080 · 25–60 s | khối "See it work" của landing · YouTube dài · App Preview (15–30 s) | Claude | ★★★ |
| 3 | **How-to short** — hook + 2–3 bước | 9:16 1080×1920 · 10–25 s | khối shorts của landing · YouTube Shorts · TikTok · Reels | Claude | ★★★ |
| 4 | **Feature clip** — 1 tính năng, lặp vòng | 16:10 · 3–6 s | cạnh từng khối tính năng trên landing (thay ảnh tĩnh) | Claude | ★★ |
| 5 | **Before → after** — bừa → 1 chạm → gọn | 9:16 · 6–12 s | Shorts / TikTok / khối nỗi đau | Claude | ★★ |
| 6 | **Pain hook** — 2 s stock người bực + app gỡ | 9:16 · 12–20 s | Shorts / TikTok / quảng cáo | Claude (stock ghi nguồn) | ★★ |
| 7 | **Voice how-to** — giọng AI + phụ đề từng chữ | 9:16 · 20–40 s | Shorts / TikTok | Claude (edge-tts) | ★★ |
| 8 | **Race / so sánh** — làm tay vs app, giây đo thật | 9:16 · 10–20 s | Shorts / TikTok | Claude (cần quay cả phần làm tay) | ★ |
| 9 | **Trend / Stitch** — format đang hot dựng lại bằng cảnh mình | 9:16 · 7–20 s | TikTok / Reels | Một nửa | ★ |
| 10 | **Tutorial dài** — "How to X on Mac" trả lời đúng câu người ta search | 16:9 · 2–8 min | YouTube (SEO) · nhúng vào bài blog | Một nửa (giọng AI hoặc người) | ★★ (kênh tìm kiếm) |
| 11 | **Launch trailer** — 30–60 s, có nhạc, cho ngày ra mắt | 16:9 · 30–60 s | Product Hunt · X · đầu kênh YouTube | Claude | ★ khi launch |
| 12 | **App Preview** — chỉ hình quay app, không giá, không stock | Mac 1920×1080 · iPhone 886×1920 · 15–30 s | App Store | Claude | ★★★ nếu bán trên store |
| 13 | **README demo** — 1 luồng chính | 16:10 · ≤ 10 MB | README GitHub của app/tool | Claude | ★★ (app có repo public) |
| 14 | **Dev story / face** — "Tôi làm app này vì…" | 9:16 · 20–45 s | TikTok / Shorts / X | Tay | ★ (tin cậy cao nhất) |

Bộ tối thiểu mỗi app: **1 + 2 + 3×3 (+12 nếu có store)**. 17 kiểu short chi tiết (`format:` id) ở Promo Desk
`VideoFormats.swift`; bộ nâng cao 4 bậc theo spec JSON (giọng AI, cắt dán stock, bắt trend): mẫu Sweepy
`apps/ACTIVE/desk-apps/sweepy/marketing/video/specs/README.md` + `make_short.py`.

Luật chung: khung đầu đã có nỗi đau hoặc kết quả (không logo, không "hey guys") · chữ đọc được khi tắt tiếng ·
chỉ tính năng có thật · không số bịa · nhạc trend gắn trong app lúc đăng.

## §2. Luồng YouTube

```
1 bản quay app thật
  ├─ Demo 16:9 ──────────► YouTube dài (video "gốc" của app) ◄── nhúng landing + blog
  ├─ 3–N Shorts 9:16 ────► YouTube Shorts ─ "Related video" trỏ về video gốc
  │                         (cùng file → TikTok, Reels)
  └─ Tutorial dài ───────► YouTube search ("how to find duplicate files on mac")
```

- **Shorts trước, dài sau:** Shorts kéo người thấy; video dài + blog giữ người tìm kiếm. Mỗi Short gắn *Related video*
  (YouTube Studio → Shorts → Related video) về video gốc — đường duy nhất Short có link bấm được.
- **Nhịp:** 3 Shorts/tuần trong 6 tuần đầu, 1 video dài/tháng; đo views · % xem hết · lượt bấm link (`ct=youtube`) trong
  `grow.md` — không đoán.
- **File metadata** mỗi video: `marketing/youtube/NN-<loại>.md` (Title ≤ 60 ký tự, câu search được · Description: 2 dòng đầu
  = lợi ích + link store có `ct=youtube` · Tags · Thumbnail prompt cho Codex · ô Đã đăng). Shorts: title có `#shorts` không bắt
  buộc; hook trong title giống hook khung đầu.
- **Gói upload chi tiết + hồ sơ kênh:** skill `app-youtube-upload` · `app-youtube-channel` (`check_youtube.py`).
- **Đăng:** người dùng tự upload trong YouTube Studio (Claude không đăng nhập). Upload qua API cần OAuth + project đã
  được Google xác minh — không đáng làm khi chưa > 5 video/tuần.
- Kênh: một kênh studio (oneclicktool) với playlist mỗi app, không mỗi app một kênh — dồn subscriber.

## §3. Cách làm khác ngoài Remotion

| Cách | Hợp khi | Ghi chú |
|---|---|---|
| **Remotion** (mặc định) | lặp lại nhiều app, Claude tự render, đổi chữ là ra bản mới | React; miễn phí cá nhân/công ty ≤ 3 người |
| **Screen Studio** (Mac) | quay bản thô đẹp: tự zoom theo con trỏ, nền gradient | người dùng tự quay; xuất mp4 rồi đưa vào Remotion |
| **ffmpeg thuần** | cắt nhanh, hero loop, nén, ghép tiếng im lặng, GIF cho README | Claude chạy được, không cần dự án |
| **Motion Canvas / Revideo** | thích animation vector kiểu giải thích | thay Remotion, cùng ý tưởng "video bằng code" |
| **CapCut / trình sửa TikTok** | trend sound, auto caption, hiệu ứng trend | tay; dùng cho loại 9, 14 |
| **Giọng AI** (edge-tts free · ElevenLabs trả phí) | loại 7, 10 | phụ đề từng chữ lấy mốc từ TTS (Sweepy `make_short.py`) |
| **Phụ đề tự động** (whisper.cpp → `@remotion/captions`) | video có giọng người thật | chạy local, không gửi file ra ngoài |
| **AI sinh video** (Sora / Veo / Kling) | chỉ b-roll cảnh *nỗi đau* (người bực, bàn bừa) | KHÔNG dùng vẽ giao diện app; ghi nguồn |
| **Avatar AI** (HeyGen…) | hầu như không | mặt thật ăn hơn; người xem nhận ra avatar |

## §4. Host video — repo hub, landing, README GitHub

**GitHub làm kho được, nhưng không phải chỗ phát video lớn.** Giới hạn: file > 100 MB bị chặn (cảnh báo từ 50 MB), repo
nên < 1 GB; Git LFS có quota băng thông nhỏ và jsDelivr không phát file LFS → **không dùng LFS**.

Chia vai:

| Nơi | Giữ gì |
|---|---|
| **YouTube** | bản to (1440p demo, tutorial dài) — host chính, miễn phí, có SEO |
| **Repo hub** (GitHub public, vd `oneclicktool-videos`) | bản web ≤ 8 MB (shorts, hero loop, demo nén 1080p) + poster + `index.json` — phân loại theo app |
| **jsDelivr** (`cdn.jsdelivr.net/gh/<user>/<repo>@<tag>/…`) | CDN miễn phí phát thẳng file từ repo hub, file ≤ 20 MB, content-type đúng → `<video src>` trên landing |
| **Cloudflare R2** | khi hub vượt ~1 GB hoặc cần file > 20 MB — không tính phí băng thông |
| `public/` của site (Vercel) | chỉ hero loop ≤ 3 MB nếu muốn khỏi phụ thuộc CDN |

Khung repo hub:
```
oneclicktool-videos/
├── README.md            bảng mọi video (sinh từ index.json)
├── index.json           [{app, file, type, w, h, sec, youtube, posted}]
└── <slug>/
    ├── landing/         <slug>-hero-1600x1000.mp4 · <slug>-demo-1920x1080.mp4 (+ poster)
    ├── shorts/          <slug>-<việc>-1080x1920.mp4 + -poster.jpg
    └── store/           <slug>-app-preview-1920x1080.mp4
```
Nguồn dựng (Remotion, bản quay thô) vẫn ở repo này (`apps/…/marketing/video/`); hub chỉ nhận file đã qua `check_video.py`.
Link jsDelivr ghim theo tag (`@v2026.10.08`) để cache không giữ bản cũ; đổi video = commit + tag mới.

Landing:
```html
<video src="https://cdn.jsdelivr.net/gh/<user>/oneclicktool-videos@<tag>/sweepy/shorts/sweepy-undo-1080x1920.mp4"
       poster="…/sweepy-undo-poster.jpg" muted playsinline loop preload="none"></video>
```
Hero loop: `autoplay muted loop playsinline`. Demo dài: nhúng YouTube kiểu facade (ảnh poster + nút play, bấm mới tạo
iframe `youtube-nocookie.com/embed/<id>`) để trang không nặng.

README GitHub (không nhận thẻ `<video>` tự viết):
- Video ≤ 10 MB: kéo thả mp4 vào ô sửa README trên github.com → GitHub tạo link `github.com/user-attachments/assets/…`, đặt
  link đó một mình một dòng → hiện trình phát.
- Video dài: `[![Watch the demo](poster.jpg)](https://youtu.be/<id>)` — ảnh poster bấm ra YouTube.
- GIF chỉ khi cần tự chạy trong README: `ffmpeg -i in.mp4 -vf "fps=12,scale=800:-1" out.gif`, giữ ≤ 5 MB.

## §5. Thông số

| Đích | Khung | Dài | Ghi chú |
|---|---|---|---|
| YouTube Shorts | 1080×1920 | ≤ 3 min (tốt nhất 15–45 s) | vùng an toàn: chừa 250 px dưới + 120 px phải cho nút |
| TikTok / Reels | 1080×1920 | 7–60 s | cùng file Shorts |
| YouTube dài | 1920×1080 hoặc 2560×1440 | tuỳ | ≥ 1440p được YouTube nén tốt hơn |
| App Preview Mac | 1920×1080 (16:9) | 15–30 s | ≤ 30 fps, có track tiếng, không giá, không stock |
| App Preview iPhone 6.9" | 886×1920 | 15–30 s | như trên |
| Landing short | 1080×1920 | ≤ 25 s | ≤ 8 MB, faststart, poster bắt buộc |
| Hero loop | 1600×1000 | 4–8 s | ≤ 3 MB, không tiếng |
