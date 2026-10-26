# Niche Radar Phase 61 — Chỗ trống AI + SEO — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** gộp kệ Google + kệ AI thành điểm **"kệ yếu"** công thức cố định, đưa vào bảng so sánh niche. Không AI.

**Spec:** [Phase 61 · Chỗ trống AI + SEO](../../web/phase-61-ai-seo-gap.md) · **Cần trước:** Phase 59, 60, 28.

## Mục tiêu · làm · không làm

- **Xong khi:** 3 niche thật có điểm kệ Google + kệ AI, bảng so sánh có 2 cột mới · mỗi điểm bấm ra số gốc (câu nào, URL nào) ·
  thử 1 niche đông ("habit tracker") → "khó chen".
- **Làm:** điểm kệ Google, điểm kệ AI, công thức trên UI, 2 hàng mới trong so sánh niche, danh sách câu "chưa ai trả lời tốt".
- **Không làm:** đổi điểm cơ hội Phase 1 · AI chấm / giải thích.

## Global Constraints

- Công thức 1 chỗ `web/src/lib/shelf-score.ts`, trả `{ value, parts: [{ label, value, refs }] , formula }`:
  - Kệ Google = % top 10 là `forum` + `blog nhỏ`, trừ điểm khi có `app chính chủ` đứng top 3.
  - Kệ AI = % câu trả lời yếu − phạt độ tập trung (1 app > 50% lượt nhắc) + điểm khi trang được trích là loại mình viết được (blog / so sánh).
- Trọng số khởi đầu đều; chốt sau 3 niche thật, ghi vào trang phase + lý do. Đổi trọng số → test cập nhật.
- "Câu chưa ai trả lời tốt" = câu có kệ Google dễ **và** kệ AI yếu → lưu để Phase 62 đọc.

## File đụng tới

- `web/src/lib/shelf-score.ts` (mới) — 2 điểm + phần + refs
- `web/src/lib/compare-niche.ts` — 2 hàng mới nhóm "Kệ" (cao = thắng), ô thiếu "chưa tra"
- `web/src/components/ShelfScore.tsx` (mới) — hiện điểm + tooltip công thức + bấm ra số gốc; dùng trên `/r/:id` và `/compare`
- `web/src/lib/open-questions.ts` (mới) — danh sách câu chưa ai trả lời tốt
- `web/tests/shelf-score.test.ts`

## Tasks

### Task 1: Công thức
- [ ] `shelf-score.ts` + test: niche đông giả → khó chen; niche toàn forum → dễ chen.

### Task 2: Vào so sánh + trang Research
- [ ] 2 hàng trong `compare-niche.ts`; `ShelfScore` bấm ra câu / URL.

### Task 3: Câu chưa ai trả lời tốt
- [ ] `open-questions.ts` + hiện trên trang Research.

### Task 4: Chạy thật + chốt trọng số
- [ ] 3 niche thật + "habit tracker"; chốt trọng số, ghi lý do. Screenshot 1340 + 375, Read. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
