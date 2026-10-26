# Niche Radar Phase 11 — Reddit Gap — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Task 0 trượt → dừng cả phase, ghi lý do vào `docs/appendix.md`.

**Goal:** biết người dùng Mac **cần mà chưa có** gì — chủ đề hỏi nhiều, được quan tâm, chưa ai giải — kèm link bài gốc.

**Spec:** [Phase 11 · Reddit Gap](../../web/phase-11-reddit-gap.md) · **Cần trước:** Phase 6 (job Claude in Chrome), Phase 2
(collector App Store), Phase 8 (Project + backup).

## Mục tiêu · làm · không làm

- **Xong khi:** ≥ 500 bài r/MacOS qua ít nhất 1 tuyến (ghi ngày) · bảng gap 12 tháng · kiểm tay 30 bài: chuyên mục đúng
  ≥ 80 %, chủ đề đúng ≥ 70 % · top 10 gap mỗi dòng ≥ 3 link mở được · file `.md` chọn được 1 bài `/fix` hoặc 1 ý tưởng app
  Mac · test phân loại + test định dạng file nhập.
- **Làm:** bảng `reddit_threads`, 3 tuyến nhập cùng một định dạng, bộ phân loại không AI, điểm gap, trang `/reddit`, xuất `.md`.
- **Không làm:** đăng bài / comment · lưu tên người đăng · subreddit ngoài danh sách anh chọn · vượt chặn DNS / IP / proxy ·
  đọc cả cây comment · subreddit ngoài Mac · đếm bài theo keyword như bản cũ.

## Global Constraints

- **Một định dạng file** cho cả 3 tuyến (`niche-radar/reddit-threads@1`): `{ format, subreddit, fetchedAt, route, threads: [...] }`.
  Mỗi thread: `id`, `subreddit`, `title`, `body` (≤ 500 ký tự), `flair`, `score`, `comments`, `createdAt` (ISO), `url`,
  `topComments` (≤ 3, mỗi cái ≤ 300 ký tự), `solved` (bool). **Không** có trường tác giả — file có `author` thì bỏ trường đó khi nhập.
- Tuyến B (Claude in Chrome) là mặc định; tuyến A (API) chỉ dựng khung, tắt tới khi có key; tuyến C = nhập file tay.
- Lịch sự: job ghi rõ "≥ 2 giây / trang", cache 7 ngày theo subreddit (`reddit_fetches`).
- Luật phân loại nằm trong **một file** `web/src/lib/reddit/rules.ts` (mẫu câu + flair + từ điển chủ đề) để sửa không đụng code khác.
- Điểm gap hiện công thức trên UI (`title` ở tiêu đề cột) — không có điểm bí ẩn.
- Migration mới số kế tiếp (hiện tới `0013`) qua `npm run db:generate`; backup DB trước khi migrate như Phase 8 (`backupDb`).

## File đụng tới

- `web/src/db/schema.ts` + migration mới — bảng `reddit_threads` (khoá `id` Reddit), `reddit_fetches` (subreddit, route, fetchedAt, count)
- `web/src/lib/reddit/format.ts` — kiểm + chuẩn hoá file nhập (bỏ `author`, cắt độ dài, loại trùng)
- `web/src/lib/reddit/rules.ts` — mẫu câu chuyên mục, flair, từ điển ~40 chủ đề Mac, cụm "chưa giải"
- `web/src/lib/reddit/classify.ts` — `categoryOf(thread)`, `topicsOf(thread)` (1–2 chủ đề)
- `web/src/lib/reddit/gap.ts` — gom chủ đề × chuyên mục, số liệu, điểm gap, đếm app Mac App Store
- `web/src/lib/reddit/job.ts` — sinh file job cho Claude in Chrome (link top năm / tháng / search 6–8 mẫu)
- `web/src/server/app.ts` — `GET /api/reddit`, `GET /api/reddit/job`, `POST /api/reddit/import`, `GET /api/reddit/gap`, `GET /api/reddit/export.md`
- `web/src/client/RedditGapPage.tsx` + `main.tsx` + `NavMenu.tsx` — trang `/reddit`, 1 cột
- `web/src/lib/features.ts` — thêm "Reddit Gap" (Phase 11)
- `web/tests/reddit-*.test.ts` + `web/tests/fixtures/reddit/` — fixture bài thật đã bỏ tên người đăng

## Tasks

### Task 0: Bước 0 — thử đường lấy dữ liệu (½ ngày, làm trước hết)
- [ ] Nối lại Claude in Chrome (tắt hẳn Chrome, mở khung Claude, session mới); mở `r/MacOS/top/?t=year`, đọc 100 bài.
- [ ] Kiểm đủ trường: điểm, số comment, flair, ngày, 3 comment top.
- [ ] Nếu B vẫn kẹt: tuyến C — anh mở `top.json?t=year&limit=100` trong Chrome, lưu file → thử nhập.
- [ ] Ghi kết quả từng tuyến + ngày vào bảng bước 0 trên trang phase. Không tuyến nào ≥ 500 bài → **dừng phase**.

### Task 1: Bảng + định dạng file nhập
- [ ] Schema `reddit_threads` (id, subreddit, title, body, flair, score, comments, createdAt, url, topComments json, solved,
      category, topics json, topicBy `rule|ai`, importedAt) + `reddit_fetches`; migration mới.
- [ ] `format.ts`: `parseThreadsFile(body)` → `{ threads, dropped, errors }`; bỏ `author`, cắt `body`/comment, loại trùng id.
- [ ] Test: file đúng · thiếu trường · có `author` (bị bỏ) · trùng id · sai `format`.

### Task 2: Phân loại không AI
- [ ] `rules.ts`: chuyên mục `how-to` · `bug` · `app-request` · `alternative` · `complaint` · `other` (mẫu câu + flair);
      bỏ flair News / Discussion; từ điển ~40 chủ đề (Bluetooth, Wi-Fi, pin, RAM, dung lượng, Finder, cửa sổ, menu bar,
      Spotlight, chụp màn hình, màn hình ngoài, phím tắt, Time Machine, iCloud, AirDrop, cập nhật macOS…).
- [ ] `classify.ts` + gọi lúc nhập; bài không khớp → `other`.
- [ ] Test trên ≥ 40 bài fixture thật (đã ẩn tên).

### Task 3: Job + nhập (tuyến B, C; khung A)
- [ ] `job.ts`: file job liệt kê URL top năm, top tháng, search 6–8 mẫu ("is there an app", "how do I", "alternative to",
      "not working", "after updating"…) trong subreddit đã chọn; định dạng trả về; luật ≥ 2 giây / trang, không tác giả.
- [ ] `GET /api/reddit/job?sub=MacOS` · `POST /api/reddit/import` (ghi `reddit_fetches`, trả số thêm / bỏ).
- [ ] Tuyến A: hàm `fetchRedditApi` chỉ chạy khi có `REDDIT_CLIENT_ID` — chưa có thì trả hướng dẫn, không gọi mạng.
- [ ] Tuyến A gán chủ đề cho bài `other` qua `aiAsk` (Phase 6) nếu có key, ghi `topicBy: 'ai'`.

### Task 4: Thống kê gap
- [ ] `gap.ts`: mỗi chủ đề × chuyên mục: số bài, số bài 90 ngày, theo tháng, tổng / trung vị điểm, tổng comment,
      % Solved, % comment top có "no native way / not possible / use an app", số app Mac App Store khớp từ khoá
      (dùng lại collector App Store, cache).
- [ ] Điểm gap = hỏi (log) × quan tâm (log) × (1 − % giải) × 1/(1 + số app); công thức xuất kèm để UI hiện.
- [ ] Test với dữ liệu giả: chủ đề nhiều hỏi, ít giải, ít app đứng đầu.

### Task 5: Trang + xuất + Project
- [ ] `/reddit`: chọn subreddit (r/MacOS, r/mac, r/MacApps, r/applehelp + thêm tay) → nút tải job / nhập file → bảng
      chủ đề theo điểm gap, lọc chuyên mục, bấm dòng ra danh sách bài gốc (link). 1 cột.
- [ ] `GET /api/reddit/export.md`: top 20 gap + 3 link mẫu mỗi gap.
- [ ] "+ Collect" một gap vào Project (term = tên chủ đề, ghi nguồn reddit).
- [ ] `features.ts` đổi sang `done`; Hướng dẫn thêm mục Reddit Gap.

### Task 6: Chạy thật + soát
- [ ] Nhập ≥ 500 bài r/MacOS 12 tháng; kiểm tay 30 bài ngẫu nhiên, ghi tỷ lệ đúng vào "Kết quả chạy thật".
- [ ] Mở ≥ 3 link của top 10 gap. Xuất `.md`, chọn 1 bài `/fix` hoặc 1 ý tưởng app Mac, ghi vào đây.
- [ ] Screenshot `/reddit` ở 1340 và 375, Read ảnh. Cập nhật chip phase, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan. Bước 0 qua một nửa (Chrome vào được Reddit, Claude in Chrome chưa nối).

## Kết quả chạy thật

Chưa chạy.
