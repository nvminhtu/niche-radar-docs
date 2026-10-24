---
name: app-youtube-upload
description: "Skill phụ marketing — chuẩn bị UPLOAD một video YouTube (dài 16:9 hoặc Shorts 9:16) để người dùng chỉ việc Copy-dán trong YouTube Studio: chọn từ khoá bằng YouTube autocomplete, title ≤ 100 (giữ ≤ 70 cho điện thoại) + phương án B, description ≤ 5000 với 2 dòng đầu = lợi ích + link UTM, chapters (00:00, ≥ 3 mốc, mỗi mốc ≥ 10 s) lấy từ kịch bản/bản quay thật, ≤ 3 hashtag (> 60 thì YouTube bỏ hết), tags, thumbnail 16:9 rộng ≥ 640 ≤ 50 MB (prompt cho Codex, Claude không tự vẽ), playlist, Made for kids, Altered content (AI trông như thật), Paid promotion, end screen/cards/Related video, pinned comment — ghi marketing/youtube/NN-*.md (Promo Desk hiện ở tab Campaign, Mark as posted), kiểm bằng scripts/check_youtube.py. Use when 'chuẩn bị upload youtube', 'prepare upload youtube', 'đăng video lên youtube', 'title youtube', 'mô tả video youtube', 'description youtube', 'chapters', 'timestamp video', 'thumbnail youtube', 'tags youtube', 'hashtag youtube', 'shorts title', 'metadata youtube', 'seo youtube'. Không upload/đăng nhập thay người dùng, không bịa số, không clickbait sai nội dung. Làm video → /app-video; kênh → /app-youtube-channel."
argument-hint: "[slug hoặc kênh] [file video]"
user-invocable: true
---

# Upload YouTube — gói dán sẵn cho từng video

**Một việc:** `marketing/youtube/NN-<tên>.md` đủ ô, `python3 scripts/check_youtube.py <file>` in `0 FAIL`, thumbnail đã về
từ Codex và đã Read. Người dùng mở Promo Desk → tab Campaign → Copy từng ô → dán vào **Studio → Create → Upload videos** →
bấm Publish → Mark as posted (dán link).

Khuôn: [templates/youtube_upload.md](../../../templates/youtube_upload.md) (frontmatter giống file bài Campaign của Promo Desk;
`type: long|short`). Mẫu đang có: `apps/ACTIVE/desk-apps/sweepy/marketing/youtube/01-app-preview.md`.
Luồng dài ↔ Shorts, nhịp đăng: `app-video` → `references/video-playbook.md` §2.

## 1. Đầu vào — không có thì dừng

| Cần | Lấy ở |
|---|---|
| File video đã render, biết độ dài | `marketing/video/out/` (`app-video`) hoặc người dùng đưa đường dẫn |
| Nội dung thật của video | kịch bản/spec (`marketing/video/specs/`), hoặc xem video: `ffprobe` độ dài + trích vài khung `ffmpeg -ss … -frames:v 1` rồi Read |
| Link đích | landing/store của sản phẩm (`app.json` `site_url`, `listing.md`) |
| Kênh + playlist | `channel-listing.md` (`app-youtube-channel`) |

Không biết video nói gì → không viết chapters/title. **Không đoán nội dung từ tên file.**

## 2. Từ khoá (5 phút, có đo)

Autocomplete YouTube: `curl -s "https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q=<từ>"` cho 3–5 cụm
gần nội dung video. Chọn **một** cụm người ta đang gõ mà video trả lời đúng → ghi `Từ khoá chính (… , ngày)`. Lượt tìm: `chưa đo`.

## 3. Viết từng ô

- **Title:** từ khoá chính nằm trong 40 ký tự đầu; hứa đúng thứ video cho thấy; ≤ 70 ký tự. Phương án B khác góc
  (kết quả vs cách làm) để Studio thử. Không viết hoa toàn bộ, không `<` `>`.
- **Description:** dòng 1–2 = lợi ích + link có `utm_source=youtube&utm_medium=video&utm_campaign=<tên>` (App Store dùng
  `ct=youtube`). Rồi 3–5 dòng nói video có gì · chapters · link phụ · ≤ 3 hashtag ở cuối. Giọng theo `app-reddit` §2.
- **Chapters (video dài):** mốc từ kịch bản/bản quay thật, `00:00` đầu, ≥ 3 mốc, cách nhau ≥ 10 s, tên mốc = câu tìm được.
- **Tags:** 5–10 cụm, cụm chính trước, lỗi chính tả hay gặp — tags ít tác dụng, đừng mất thời gian.
- **Thumbnail:** ≤ 3 chữ khác title, một thứ to (kết quả/khuôn mặt/con số thật), tương phản mạnh; prompt theo
  `core:asset-prompt` → Codex sinh → `File:` → Read ở cỡ nhỏ. Shorts: thumbnail chọn trong Studio trên máy tính.
- **Settings:** Made for kids `no` (trừ khi thật sự cho trẻ em) · **Altered content** `yes` khi có cảnh AI trông như thật
  (người thật nói điều không nói, cảnh thật bị sửa, cảnh giả như thật); dùng AI viết kịch bản, phụ đề, lồng tiếng sửa âm
  thì không cần · **Paid promotion** `yes` nếu được trả/tặng · playlist · lịch đăng.
- **Video elements:** end screen (video ≥ 25 s) → video kế + Subscribe · card ở mốc nhắc tới video khác · Shorts → Related
  video trỏ về video dài gốc (link bấm được duy nhất của Short).
- **Pinned comment:** 1 câu hỏi thật cho người xem + link — comment đầu kéo thảo luận.

## 4. Kiểm và giao

```bash
python3 scripts/check_youtube.py apps/ACTIVE/<slug>/marketing/youtube/NN-<tên>.md
```

FAIL → sửa nội dung, không sửa chữ cho qua. Báo bằng lời thường: video nào · title chọn vì sao (từ khoá đo được) · còn chờ
gì (thumbnail Codex). Sau khi người dùng đăng: `status: posted <ngày> <link>` (Promo Desk tự ghi khi bấm Mark as posted);
48 giờ sau xin screenshot Studio (CTR thumbnail, % xem, lượt bấm) → ghi `grow.md` — không đoán số.

## Không làm

Upload hay đăng nhập Studio thay người dùng (API upload cần OAuth + app Google đã xác minh — không làm) · title/thumbnail hứa
thứ video không có · nhồi hashtag/tag · bịa số view/doanh thu trong title · nhạc có bản quyền trong file · reup video người khác.
