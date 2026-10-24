---
name: app-youtube-channel
description: "Skill phụ marketing — dựng hoặc sửa KÊNH YouTube (không phải từng video): định vị 1 câu, tên kênh, handle 3–30 ký tự (3 phương án), mô tả kênh, ≤ 14 link có UTM, banner 2048×1152 (vùng an toàn 1235×338, ≤ 6 MB), avatar vuông (hiện 98×98), watermark ≥ 150 vuông < 1 MB, playlist theo series, trailer + Home tab, Upload defaults — ghi vào channel-listing.md để Promo Desk hiện từng ô Copy, prompt ảnh cho Codex sinh (Claude không tự vẽ), kiểm bằng scripts/check_youtube.py. Đo đối thủ cùng ngách (sub, view 10 video gần nhất, nhịp đăng) từ trang công khai kèm ngày. Use when 'sửa kênh youtube', 'edit youtube channel', 'làm kênh youtube', 'tạo kênh youtube mới', 'banner youtube', 'avatar kênh', 'mô tả kênh', 'đổi tên kênh', 'handle youtube', 'playlist kênh', 'trailer kênh', 'kênh youtube về AI', 'tối ưu kênh youtube'. Không đăng nhập Studio, không tự đổi tên/handle thay người dùng, không mua sub/view, không bịa số kênh. Từng video → /app-youtube-upload."
argument-hint: "[kênh hoặc slug] [việc: setup | audit | banner | playlists]"
user-invocable: true
---

# Kênh YouTube — một trang hồ sơ, dán là xong

**Một việc:** `channel-listing.md` đầy đủ, `python3 scripts/check_youtube.py <thư mục>` in `0 FAIL`, ảnh banner/avatar đã
về từ Codex và đã Read. Người dùng mở Promo Desk (hoặc file) → Copy → dán vào **YouTube Studio → Customization**.

Khuôn: [templates/youtube_channel.md](../../../templates/youtube_channel.md). Luật số: docstring của `scripts/check_youtube.py`
(nguồn trang trợ giúp YouTube, đọc 2026-10-09).

## 0. File nằm đâu

| Kênh của | File |
|---|---|
| Một app (kênh riêng app — hiếm, thường dùng playlist trong kênh studio) | `apps/ACTIVE/<slug>/marketing/youtube/channel-listing.md` |
| Studio / kênh nội dung độc lập (vd kênh về AI) | `videos/ACTIVE/<kênh>/channel-listing.md` — Promo Desk thấy ở nhóm **Videos** |

Video của kênh (gói upload) ở `<cùng thư mục sản phẩm>/marketing/youtube/NN-*.md` → skill `app-youtube-upload`.

## 1. Đọc trước — không có thì hỏi

1. Plan kênh (vd `research/*-youtube-*-plan.md`): định vị, series, ngôn ngữ, lộ mặt hay không. Chưa có → hỏi 4 câu: ngôn ngữ ·
   dùng kênh cũ hay mới · lộ mặt · mấy giờ quay/tuần.
2. Kênh hiện tại (nếu sửa): người dùng dán link kênh hoặc screenshot Studio. Đọc trang công khai (`/about`, `/videos`,
   `/playlists`) bằng trình duyệt; số liệu Studio (watch time, CTR) chỉ người dùng xem được — xin screenshot, không đoán.
3. `.claude/repo-profile.yaml` `design` (đường dẫn ảnh) + màu/logo studio nếu có.

## 2. Đo đối thủ (10–15 kênh cùng ngách)

YouTube autocomplete (`suggestqueries.google.com/complete/search?client=firefox&ds=yt&q=…`) → từ khoá → mở 10–15 kênh hiện
lên. Mỗi kênh ghi: link · sub · view 10 video gần nhất (trung vị) · nhịp đăng · tiêu đề/thumbnail ăn nhất · có lộ mặt không
· **ngày đọc**. Ghi vào file plan kênh, mục `## Đối thủ`. Rút ra: chỗ trống (chủ đề/ngôn ngữ ít người làm) → câu định vị.

## 3. Viết hồ sơ (theo thứ tự trong khuôn)

- **Tên kênh:** người ta nhớ và gõ lại được; có thể kèm từ khoá ngách ("Tu builds with AI"), không nhồi từ khoá.
- **Handle:** 3 phương án, 3–30 ký tự, chữ/số/`_` `-` `.`, giống tên kênh. Ghi "chưa kiểm còn trống".
- **Mô tả:** câu đầu = cho ai + xem được gì (câu này hiện trong kết quả tìm) · lịch đăng · 1 lời mời bấm link. Giọng như
  người thật, theo `app-reddit` §2 (không "game-changer", không gạch ngang dài dày đặc, không emoji rải).
- **Links:** website/landing đầu tiên, mọi link có `utm_source=youtube&utm_medium=channel`.
- **Banner / avatar / watermark:** viết prompt (màu, chữ đúng từng từ, vùng an toàn) theo `core:asset-prompt` → Codex
  sinh → nhặt ảnh về cạnh file, ghi `File:` → Read ảnh, chữ có nằm trong 1235×338 không. Prompt chưa phải asset.
- **Playlists:** mỗi series một playlist (tên = thứ người ta tìm), mô tả 1 câu.
- **Home tab:** trailer ≤ 60 s cho người chưa sub; featured video cho người đã sub; sections = playlist.
- **Upload defaults:** chân mô tả chung + tags + category + Made for kids: no — để mỗi video khỏi điền lại.

Đổi tên/handle kênh **đang có sub**: YouTube cho 2 lần trong 14 ngày, đổi tên mất tích xanh → nói rõ trước, người dùng chốt.

## 4. Kiểm và giao

```bash
python3 scripts/check_youtube.py videos/ACTIVE/<kênh>
```

FAIL → sửa quyết định/ảnh, không sửa chữ cho qua. Báo người dùng bằng lời thường: kênh nói gì với ai · file nào · dán ô nào
trước · ảnh nào còn chờ Codex. Ghi `LEARNED.md` của sản phẩm (hoặc file plan kênh) 3–5 dòng.

## Không làm

Đăng nhập Studio · tự bấm Save/Publish · mua sub/view/comment · đổi tên kênh khi người dùng chưa chốt · bịa số kênh hay
doanh thu · reup video người khác · nút quyên góp/"ủng hộ kênh" gắn với app (Apple 3.2.2(iv)).
