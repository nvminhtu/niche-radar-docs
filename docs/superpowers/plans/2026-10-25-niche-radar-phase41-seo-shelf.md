# Niche Radar Phase 59 — Kệ Google (SEO) — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Không cào trang kết quả Google bằng script. Key API anh tự tạo.

**Goal:** với keyword chính của niche: top 10 Google là ai, loại trang gì, còn chỗ chen không; kèm câu hỏi người dùng hay gõ. Không AI.

**Spec:** [Phase 59 · Kệ Google](../../web/phase-59-seo-shelf.md) · **Cần trước:** Phase 1 (Top 10 cơ hội, `collectors/suggest.ts`).

## Mục tiêu · làm · không làm

- **Xong khi:** bảng thử nguồn đủ, chọn 1 nguồn chính · 3 niche thật có top 10 cho 10 keyword + loại trang + bộ ≥ 20 câu hỏi ·
  kiểm tay 10 URL với Google mở tay: ≥ 6/10 có trong top 10 · hết quota → UI báo đúng, phần khác vẫn chạy.
- **Làm:** top 10 / keyword (URL, tiêu đề, domain, hạng), loại trang theo luật domain, độ dễ chen, bộ câu hỏi từ autocomplete, CSV.
- **Không làm:** lượt tìm thật / độ khó keyword · phân tích nội dung trang · theo dõi thứ hạng.

## Đo trước khi code (Task 0)

| Nguồn | Đo gì | Ghi vào |
|---|---|---|
| Brave Search API | quota free / tháng (trang giá chính chủ + ngày), 1 truy vấn thử | bảng thử trên trang phase |
| Google Programmable Search JSON API | còn mở cho tài khoản mới không, quota / ngày | bảng thử |
| Độ gần Google | 5 keyword: so top 10 nguồn với Google mở tay | bảng thử |

## Global Constraints

- Nguồn top 10 sau 1 interface `SerpProvider` (`brave`, `google_cse`) — đổi nguồn không đụng chỗ khác. Key ở `.env.local` / Cài đặt.
- Đếm quota trong DB (`serp_calls`), trần / tháng do anh đặt; hết → `QUOTA` (UI báo), nguồn khác vẫn chạy.
- Cache 7 ngày theo `(keyword, country, provider)`.
- Luật loại trang trong `web/src/lib/serp-rules.ts`: `store` · `forum` · `blog nhỏ` · `site lớn` (danh sách domain) · `app chính chủ`
  (domain trùng web của đối thủ trong run) · `video`.
- Độ dễ chen = số `forum` + `blog nhỏ` trong top 10 (0–10), không trộn vào điểm cơ hội Phase 1.
- Câu hỏi: Google autocomplete (đã dùng ở Phase 1) với tiền tố `how / why / can / best / vs / alternative`; gộp câu trùng bằng chuẩn hoá.

## File đụng tới

- `web/src/collectors/serp.ts` (mới) — `SerpProvider` + `brave`, `google_cse`
- `web/src/lib/serp-rules.ts` (mới) — loại trang + độ dễ chen
- `web/src/lib/questions.ts` (mới) — bộ câu hỏi từ autocomplete
- `web/src/db/schema.ts` + migration mới — `SOURCES` thêm `serp`; `serp_results` (keywordId, rank, url, title, domain, kind, provider, fetchedAt), `serp_calls`, `niche_questions` (runId, prefix, text)
- `run-research.ts`, `run-view.ts` — nguồn mới chạy cho Top 10 cơ hội
- `web/src/components/SerpBlock.tsx` (mới) — bảng top 10 theo keyword, chip loại trang, độ dễ chen, bộ câu hỏi
- export (Phase 15) — bảng `serp`, `questions`
- `web/tests/serp-*.test.ts` — fixture JSON Brave / CSE

## Tasks

### Task 0: Bảng thử nguồn
- [ ] Đo 2 nguồn, chọn 1 chính (anh duyệt). Anh tạo key.

### Task 1: Provider + quota
- [ ] `serp.ts` + migration + trần quota; test fixture + hết quota.

### Task 2: Loại trang + độ dễ chen
- [ ] `serp-rules.ts` + test mỗi loại.

### Task 3: Bộ câu hỏi
- [ ] `questions.ts`; ≥ 20 câu / niche sau gộp. Test gộp trùng.

### Task 4: UI + CSV + soát
- [ ] `SerpBlock`, CSV. 3 niche thật; kiểm tay 10 URL → ghi tỷ lệ. Screenshot 1340 + 375, Read. `features.ts`, chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
