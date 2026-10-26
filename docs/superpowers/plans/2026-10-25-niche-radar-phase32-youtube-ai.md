# Niche Radar Phase 32 — YouTube Research (AI) — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Task 0 (bài thử tuyến) làm trước.

**Goal:** AI đọc phụ đề + comment của niche: người xem than gì, xin gì, dùng app nào — trích dẫn kèm mốc giây.

**Spec:** [Phase 32 · YouTube Research (AI)](../../web/phase-32-youtube-ai.md) · **Cần trước:** Phase 31 (`yt_videos`),
Phase 6 / 17 / 25 (lớp AI, kiểm trích dẫn, tuyến theo việc).

## Mục tiêu · làm · không làm

- **Xong khi:** bảng thử tuyến đủ (phụ đề + comment và ≥ 1 tuyến khác) · 3 niche thật có chủ đề than + xin tính năng, mọi câu có
  trích dẫn bấm được · mỗi lần tra dưới trần chi phí.
- **Làm:** lấy phụ đề + comment, chủ đề than, xin tính năng, tool / app được nhắc (nối đối thủ), tóm tắt video 5 dòng có mốc giây,
  gợi ý hàng mới cho Feature Gap.
- **Không làm:** tải video / ffmpeg · đăng comment.

## Global Constraints

- AI không bịa số — view / sub / số comment từ Phase 31.
- Mọi câu kèm link video + `&t=<giây>` (phụ đề) hoặc link comment; câu trích **khớp nguyên văn** văn bản đã gửi (dùng chung hàm kiểm của Phase 6 / 17).
- Tuyến chính: chữ từ `youtubei.js` → `aiAsk(db, 'youtube')`. Tuyến phụ: Gemini đọc link (nếu Phase 25 có Gemini) · job Claude in Chrome.
- Chỉ video top 10 của Top 5 keyword; ≤ 100 comment / video; phụ đề cắt theo trần token của tuyến.
- Tắt AI → Phase 31 vẫn chạy.

## File đụng tới

- `web/src/collectors/youtube-text.ts` (mới) — phụ đề (có mốc giây) + comment top, cache 7 ngày
- `web/src/db/schema.ts` + migration mới — `yt_texts` (videoId, kind `caption | comment`, json, fetchedAt)
- `web/src/lib/ai/tasks.ts` — task `yt_themes`, `yt_wishes`, `yt_tools`, `yt_summary` (hoặc 1 task gộp có 4 mục) + `clean*` kiểm trích dẫn
- `web/src/lib/youtube-link.ts` (mới) — nối tên tool được nhắc với đối thủ trong run (luật tên như Phase 22)
- `web/src/lib/gap.ts` — nhận gợi ý hàng mới (nhãn "từ YouTube"), anh bấm thêm
- `web/src/components/YoutubeAiBlock.tsx` (mới) — 4 mục, mốc giây bấm được
- `web/tests/youtube-ai*.test.ts` — `Ask` giả

## Tasks

### Task 0: Bài thử tuyến
- [ ] 10 video của 1 niche × 3 tuyến (phụ đề + comment / Gemini link / job Chrome): chất lượng · thời gian · tiền → bảng trên trang phase.

### Task 1: Lấy chữ
- [ ] `youtube-text.ts` + migration + test fixture (phụ đề có mốc giây, comment có id).

### Task 2: Task AI + kiểm
- [ ] 4 mục, mỗi câu `ref` (videoId + giây hoặc commentId); câu trượt kiểm bị gạch. Test.

### Task 3: Nối đối thủ + Feature Gap
- [ ] Tool được nhắc → đối thủ (nếu khớp chắc). Tính năng được xin ≥ 3 lần → gợi ý hàng Feature Gap.

### Task 4: UI + soát
- [ ] `YoutubeAiBlock`; 3 niche thật dưới trần chi phí. Screenshot 1340 + 375, Read. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
