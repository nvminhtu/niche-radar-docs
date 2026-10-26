# Niche Radar Phase 54 — Amazon Research (AI) — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Claude không đăng nhập Amazon thay anh; chỉ đọc, không giỏ hàng, không mua.

**Goal:** AI đọc review Amazon: người mua chê gì, ước gì, so với ai — điểm yếu đối thủ có trích dẫn, và chỗ một app làm tốt hơn.

**Spec:** [Phase 54 · Amazon Research (AI)](../../web/phase-54-amazon-ai.md) · **Cần trước:** Phase 53 (`amz_products`), Phase 6 / 28.1 (lớp AI + kiểm trích dẫn).

## Mục tiêu · làm · không làm

- **Xong khi:** bảng thử tuyến đủ · 3 niche thật có chủ đề chê + ước gì, mọi câu có link review · ≥ 1 "gợi ý cho app" anh đánh giá đáng soi.
- **Làm:** job Claude in Chrome đọc review 1–3★ (tuyến chính), tuyến Phase 6 trên phần công khai, chủ đề chê, ước gì, so với ai,
  gợi ý cho app, cột nguồn Amazon cho Feature Gap.
- **Không làm:** cào review sau đăng nhập bằng script · tự mua.

## Global Constraints

- Job `.json` theo mẫu Phase 6: danh sách ASIN (top 5 / niche), link trang review 1–3★, định dạng trả về
  `{ asin, themes[], wishes[], comparisons[], appIdeas[] }`, mỗi câu có `quote` + `url`. Nhập lại: câu trích không có trong
  phần chữ job trả kèm (`sourceText`) → bỏ.
- Không lưu tên người viết review.
- AI không bịa số — giá, sao, BSR từ Phase 33.
- "Gợi ý cho app" phải kèm ≥ 1 review gốc; anh đánh dấu đáng soi / bỏ.

## File đụng tới

- `web/src/lib/ai/tasks.ts` — task `amazon` (JOB_ONLY như `trustmrr` + tuyến A trên mô tả / bullet / review công khai), `cleanAmazon`
- `web/src/db/schema.ts` + migration mới — `amz_insights` (runId, asin, kind, text, quote, url, by `job | ai`, verdict)
- `web/src/lib/gap.ts` — cột nguồn Amazon (ô từ "có / không" trong review)
- `web/src/components/AmazonAiBlock.tsx` (mới) — 4 mục + nút "đáng soi"
- `web/src/lib/evidence.ts` — thêm gợi ý cho app đã đánh dấu
- `web/tests/amazon-ai*.test.ts`

## Tasks

### Task 0: Bài thử tuyến
- [ ] 5 sản phẩm × review 1–3★ của 1 niche: job Chrome vs tuyến Phase 6 (vs AI duyệt web nếu 2 tuyến yếu) → bảng trên trang phase.

### Task 1: Job + nhập
- [ ] Sinh job, nhập kết quả, kiểm trích dẫn, migration. Test: câu không có trong `sourceText` bị bỏ; trường tên người viết bị bỏ.

### Task 2: Tuyến A phần công khai
- [ ] Mô tả + bullet + review công khai qua `aiAsk(db, 'amazon')`. Test `Ask` giả.

### Task 3: UI + Feature Gap + evidence
- [ ] `AmazonAiBlock`, đánh dấu đáng soi, cột Amazon trong matrix, evidence pack.

### Task 4: Chạy thật + soát
- [ ] 3 niche thật (anh tự đăng nhập Amazon trong Chrome nếu muốn nhiều review). Screenshot 1340 + 375, Read. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
