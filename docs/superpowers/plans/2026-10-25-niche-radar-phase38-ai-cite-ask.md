# Niche Radar Phase 26.4 — Hỏi dữ liệu (AI Cite) — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** gõ câu hỏi bằng lời → AI trả lời **chỉ từ dữ liệu đã cào**, câu nào cũng có trích dẫn bấm được; dựng **lớp kiểm trích dẫn** dùng chung.

**Spec:** [Phase 26.4 · Hỏi dữ liệu](../../web/phase-26-4-ai-cite-ask.md) · **Cần trước:** Phase 26.6 (tuyến AI theo việc), Phase 15 (`Dataset`),
Phase 43 / 55 (màn so sánh có ô hỏi).

## Mục tiêu · làm · không làm

- **Xong khi:** bài thử 20 câu trên 3 niche đạt cả 4 dòng (trích dẫn qua kiểm ≥ 95% · 0 câu không trích dẫn · "chưa có dữ liệu" khi
  đúng là thiếu · chi phí dưới trần) · sửa 1 câu trích trong DB → câu trả lời cũ bị cờ đỏ khi kiểm lại · lớp kiểm có test riêng.
- **Làm:** ô hỏi (màn niche + màn so sánh), lấy dòng liên quan kèm id, trích dẫn → link, lớp kiểm dùng chung, lịch sử hỏi.
- **Không làm:** chat nhiều lượt nhớ dài · AI lên web · AI ghi DB.

## Global Constraints

- **Id nguồn ổn định** dạng `<loại>:<khoá>` (`review:<hash>`, `app:<store>:<id>`, `kw:<id>`, `theme:<runId>:<n>`, `yt:<videoId>@<giây>`, `cell:<compareId>:<row>:<col>`).
  Hàm `resolveRef(db, id)` → `{ exists, text, numbers, url }`.
- Lấy dữ liệu: không gửi cả DB. Tìm dòng liên quan bằng từ khoá câu hỏi trên `Dataset` của phạm vi đang xem (BM25 đơn giản viết tay
  hoặc SQLite FTS5 nếu có sẵn trong better-sqlite3), tối đa theo trần token.
- AI trả `{ sentences: [{ text, refs: [{ id, quote?, numbers? }] }] }`.
- Lớp kiểm `web/src/lib/cite-check.ts`: id có thật · `quote` đúng chữ trong nguồn · mọi số trong câu bằng số trong nguồn
  (so sau khi chuẩn hoá "1.2k" / "1,200"). Không qua → cờ đỏ. Số trong câu không có ref nào chứa → cờ đỏ.
- Tắt AI → ô hỏi ẩn.

## File đụng tới

- `web/src/lib/cite-ref.ts` (mới) — sinh / giải id nguồn
- `web/src/lib/cite-check.ts` (mới) — lớp kiểm dùng chung (Phase 56 dùng lại)
- `web/src/lib/ask/retrieve.ts` (mới) — chọn dòng liên quan + id
- `web/src/lib/ask/ask.ts` (mới) — prompt, schema, gọi `aiAsk(db, 'ask')`, chạy `cite-check`
- `web/src/db/schema.ts` + migration mới — `ask_history` (scope, question, answer json, check json, createdAt)
- `web/src/server/app.ts` — `POST /ask` · `GET /ask/history` · `POST /ask/:id/recheck`
- `web/src/components/AskBox.tsx` (mới) — ô hỏi + ví dụ sẵn, câu trả lời có link, cờ đỏ, lịch sử
- `web/tests/cite-check.test.ts`, `ask*.test.ts`, `fixtures/ask-benchmark.json` (20 câu)

## Tasks

### Task 1: Id nguồn + lớp kiểm
- [ ] `cite-ref.ts`, `cite-check.ts` + test: khớp · sai chữ · sai số · id không tồn tại · số không có ref.

### Task 2: Lấy dữ liệu
- [ ] `retrieve.ts` + test: câu "app nào bị chê về giá" lấy đúng dòng chủ đề giá.

### Task 3: Hỏi + UI + lịch sử
- [ ] `ask.ts` (Ask giả trong test), `AskBox` trên `/r/:id`, `/compare`, `/compare/apps`; lịch sử; kiểm lại câu cũ.

### Task 4: Bài thử 20 câu
- [ ] Chạy trên 3 niche, chấm 4 dòng → bảng trên trang phase. Sửa 1 câu trích trong DB → recheck → cờ đỏ.
- [ ] Screenshot 1340 + 375, Read. `features.ts`, chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
