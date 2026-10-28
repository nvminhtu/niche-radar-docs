# ShotMatic Phase 28.1 — Tóm tắt niche + chủ đề than (AI) — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Không nhập key thay anh. **Task 1–4 + 6 làm bằng tuyến B, không cần key**; chỉ Task 5
> chờ anh thêm `ANTHROPIC_API_KEY` — xong 1–4 + 6 là phase lên chip "Code xong · tuyến A chờ key".

**Goal:** đưa tóm tắt AI lên mức **dùng hằng ngày**: 1 bấm khi có key, khung 6 mục cố định, kiểm chéo với lời chê không AI,
mọi câu có trích dẫn đã kiểm.

**Spec:** [Phase 28.1 · Tóm tắt niche + chủ đề than (AI)](../../web/phase-28-1-ai-summary.md) · **Cần trước:** Phase 6
(`lib/ai/tasks.ts`, `themes.ts`, `providers.ts`), Phase 18 (cụm lời chê để kiểm chéo + bảng `review_seen` để chỉ gửi review mới).

## Mục tiêu · làm · không làm

- **Xong khi (phần 1, tuyến B — không cần key):** 3 niche tóm tắt đủ 6 mục, ≥ 95% câu trích khớp nguyên văn · tra lại sau
  7 ngày (giả lập) chỉ đưa review mới vào job · kiểm chéo gắn đúng nhãn trên ≥ 1 niche thật · test xanh · screenshot đã Read.
- **Xong khi (phần 2, khi có key):** bảng tuyến A vs B trên 3 niche (chất lượng · thời gian · tiền, có số đo + ngày);
  báo giá trước khi bấm lệch ≤ 30% so với `ai_calls`.
- **Làm:** khung 6 mục, tỉ lệ khớp trích dẫn (câu trượt bị gạch), kiểm chéo, review nhiều thứ tiếng, chỉ gửi review mới,
  lịch sử bản tóm tắt, báo giá trước khi bấm (tuyến A), đo tuyến A khi có key.
- **Không làm:** hỏi dữ liệu bằng lời (Phase 27.4) · tuyến AI mới (Phase 27.6).

## Global Constraints

- AI **không đưa số** — số chỉ từ collector; schema JSON không có trường số do AI điền (trừ `count` tính lại bằng code).
- Trần chi phí mỗi lần tra (`AiSettings.capUsd`); ước trước khi gửi, vượt trần → dừng + báo.
- Khung 6 mục cố định: `who` ai dùng · `pain` đau gì nhất · `weak` đối thủ yếu chỗ nào · `money` ai đang thu tiền ·
  `gap` khoảng trống nên làm · `risk` rủi ro. Thiếu dữ kiện → "chưa đủ dữ liệu".
- Câu trượt kiểm nguyên văn **không ẩn** — hiện gạch ngang + lý do.
- Chỉ gửi review mới: dùng `review_seen` của Phase 18 (hash = `sha256(text)`, `firstSeenAt`) + mốc lần chạy AI trước
  (`ai_history.createdAt`); không tạo bảng hash riêng. Ghép chủ đề cũ, cộng `count` bằng code.
- Báo giá trước khi gửi (tuyến A): ước token từ độ dài prompt + bảng giá model trong `providers.ts`, hiện cho anh bấm.
- Tắt AI → mọi tính năng khác vẫn chạy (đã có `AI_OFF`).

## File đụng tới

- `web/src/lib/ai/tasks.ts` — task `summary` đổi sang khung 6 mục (`cleanSummary` kiểm từng mục); giữ đọc được bản cũ 5 câu
- `web/src/lib/ai/themes.ts` — gửi phần mới + ghép chủ đề cũ; tên chủ đề tiếng Việt, câu trích giữ nguyên văn gốc
- `web/src/lib/ai/crosscheck.ts` (mới) — khớp chủ đề AI ↔ cụm Phase 18 (từ chung trong nhãn + câu trích trùng) → "chỉ AI thấy, nên kiểm"
- `web/src/db/schema.ts` + migration mới — `ai_history` (runId, task, json, createdAt) — `ai_results` vẫn là bản hiện tại (review mới lấy từ `review_seen` của Phase 18)
- `web/src/lib/ai/estimate.ts` (mới) — ước token + tiền trước khi gửi
- `web/src/components/AiResults.tsx`, `AiTaskBlock.tsx` — 6 mục, tỉ lệ khớp "22/22", câu gạch, nhãn kiểm chéo, xem lịch sử
- `web/tests/ai-summary*.test.ts` — client giả (`Ask` giả)

## Tasks

### Task 1: Báo giá trước khi bấm
- [ ] `estimate.ts` + nút tuyến A hiện "~N token · ~$X" trước khi gửi. Test với `Ask` giả: ước đúng bậc, vượt trần → không gửi.

### Task 2: Khung 6 mục + kiểm trích dẫn
- [ ] Schema structured output 6 mục, mỗi câu `refs[]`; `cleanSummary` kiểm nguyên văn từng ref, trả `matched/total`.
- [ ] UI hiện tỉ lệ + câu trượt gạch. Test: ref sai bị gạch, mục rỗng → "chưa đủ dữ liệu".

### Task 3: Kiểm chéo + nhiều thứ tiếng
- [ ] `crosscheck.ts` + nhãn trên UI. Test: chủ đề có cụm đỡ / không có cụm đỡ.
- [ ] Prompt yêu cầu gom review mọi ngôn ngữ, nhãn tiếng Việt; test bằng fixture review tiếng Đức / Nhật.

### Task 4: Cache phần mới + lịch sử
- [ ] Đọc review mới từ `review_seen` (sau lần chạy AI trước); tra lại chỉ gửi phần đó, ghép chủ đề (cộng `count` bằng code).
- [ ] `ai_history` mỗi lần chạy; UI chọn ngày, đánh dấu chủ đề mới xuất hiện.
- [ ] Test: lần 2 với 0 review mới → không gọi `Ask`.

### Task 5: Chạy tuyến A thật (phần 2 — chờ key)
- [ ] Anh thêm key ở Cài đặt (hoặc `.env.local`). Chạy `themes` + `summary` trên 3 niche, đọc `ai_calls` → bảng token · tiền · thời gian; so với báo giá.
- [ ] So với tuyến B cùng dữ liệu (số chủ đề, % khớp, chủ đề trùng) → bảng A vs B ở dưới.

### Task 6: Soát (phần 1)
- [ ] Tuyến B trên 3 niche; tra lại 1 niche sau 7 ngày (giả lập) → đếm review trong job, ghi vào đây. Screenshot 1340 + 375, Read.
      Chip "Code xong · tuyến A chờ key", ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan. Tuyến B đã chạy 5 niche (47 chủ đề, mọi câu khớp). Tuyến A chưa có key.
- 2026-10-26: review plan — tách Xong khi phần 1 (tuyến B) / phần 2 (key) để không bị chặn; dùng `review_seen` của Phase 18
  thay bảng `review_hashes`; thêm báo giá trước khi bấm.

## Kết quả chạy thật

| Niche | Tuyến | Chủ đề | % khớp | Token vào / ra | Tiền | Thời gian |
|---|---|---|---|---|---|---|
| — | A | chưa đo | chưa đo | chưa đo | chưa đo | chưa đo |
