# Niche Radar Phase 25 — Cài đặt AI + tuyến miễn phí, sổ chi phí — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Không nhập key thay anh, không tự tải model lớn.

**Goal:** chọn **nhiều nhà cung cấp** (tự mang key), thử lại **tuyến miễn phí**, thấy rõ mỗi lần tra tốn bao nhiêu.

**Spec:** [Phase 25 · Cài đặt AI](../../web/phase-25-ai-settings.md) · **Cần trước:** Phase 6 (`lib/ai/providers.ts`, `settings.ts`, `ai_calls`).

## Mục tiêu · làm · không làm

- **Xong khi:** bảng bài thử chuẩn điền đủ các tuyến đã thử (số đo + ngày) · ≥ 2 nhà cung cấp chạy với key thật · sổ chi phí
  khớp trang tính tiền nhà cung cấp (sai ≤ 10%) · tắt hết AI → tính năng không AI vẫn chạy.
- **Làm:** Claude · Gemini Flash · OpenAI (key riêng, nút thử key), chọn tuyến theo việc, thử lại tuyến C (Gemini Nano trong
  Chrome) + D (Ollama / LM Studio), sổ chi phí ngày / tháng + trần tháng, bài thử chuẩn 1 bấm.
- **Không làm:** gói lượt AI kèm Pro (Phase 69) · key trong Keychain (Phase 79).

## Global Constraints

- Mọi provider cài cùng kiểu `Ask` (`providers.ts`); thêm `geminiAsk`, `openaiAsk` dùng structured output của từng hãng.
  Model id lấy từ tài liệu chính chủ lúc làm (ghi link + ngày), không đoán.
- Key lưu `settings` trong thư mục dữ liệu / `.env.local`; **không** vào log, `ai_calls`, gói xuất (`portable.ts` lọc `ai.*Key`).
- Bảng giá ở `costOf` có nguồn + ngày từng dòng; giá đổi → sửa 1 chỗ.
- Bài thử chuẩn = bài Phase 6 (110 review → chủ đề + câu nguyên văn), fixture cố định trong `web/tests/fixtures/ai-benchmark.json`.
- Tuyến trượt bài thử không bật, ghi lý do. Tuyến C chạy ở **trình duyệt** (Prompt API) → kết quả gửi về server qua route nhập như job.

## File đụng tới

- `web/src/lib/ai/providers.ts` — `geminiAsk`, `openaiAsk`, `lmstudioAsk`; `testKey(provider)` gọi 1 lần rẻ nhất
- `web/src/lib/ai/settings.ts` — `route` thành map theo việc (`themes`, `summary`, `gap`, `revenue`, `presale`), key theo provider, `capMonthUsd`
- `web/src/lib/ai/ledger.ts` (mới) — tổng theo ngày / tháng từ `ai_calls`, chặn khi vượt trần tháng
- `web/src/lib/ai/benchmark.ts` (mới) — chạy fixture qua mọi tuyến bật → `{ route, themes, matchedPct, ms, costUsd }`
- `web/src/client/browser-ai.ts` (mới) — tuyến C: phát hiện Prompt API, chạy bài thử, POST kết quả
- `web/src/server/app.ts` — `POST /settings/ai/test-key` · `POST /ai/benchmark` · `GET /ai/ledger`
- `web/src/client/SettingsPage.tsx` — 3 provider, chọn tuyến theo việc, sổ chi phí, nút bài thử + bảng so
- `web/tests/ai-providers.test.ts`, `ai-ledger.test.ts` — fetch giả

## Tasks

### Task 1: Provider mới + thử key
- [ ] `geminiAsk`, `openaiAsk` + test với fetch giả (parse JSON, usage → `AiUsage`).
- [ ] Nút "thử key"; key không lộ trong response (chỉ `****abcd`).

### Task 2: Tuyến theo việc
- [ ] `aiAsk(db, task)` đọc tuyến của việc đó; migrate cài đặt cũ (`route: 'claude'`) sang map. Test.

### Task 3: Sổ chi phí + trần tháng
- [ ] `ledger.ts` + UI ngày / tháng; vượt trần tháng → `AI_OFF`-kiểu báo, không gọi. Test.

### Task 4: Bài thử chuẩn + tuyến C, D
- [ ] `benchmark.ts` + bảng so.
- [ ] Tuyến D: Ollama / LM Studio model mới (anh chọn, ghi dung lượng trước khi tải).
- [ ] Tuyến C: hỏi anh trước khi Chrome tải Gemini Nano; chạy bài thử ở trình duyệt.

### Task 5: Chạy thật + soát
- [ ] ≥ 2 provider với key thật của anh; so sổ chi phí với trang billing (anh đọc số) → sai ≤ 10%.
- [ ] Tắt hết AI → chạy Research + Explore + Project bình thường. Bảng bài thử vào trang phase. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan. Phase 6: tuyến D (llama3.1 8B) bỏ vì kém; tuyến C chưa thử.
