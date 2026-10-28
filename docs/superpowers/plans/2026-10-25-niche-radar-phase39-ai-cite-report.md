# ShotMatic Phase 57 — Báo cáo so sánh (AI Cite) — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Tool không ghi `Verdict` thay người dùng.

**Goal:** từ bảng so sánh niche (Phase 44) hoặc đối thủ (Phase 56), AI viết **một trang kết luận** có trích dẫn đã kiểm → evidence pack.

**Spec:** [Phase 57 · Báo cáo so sánh](../../web/phase-57-ai-cite-report.md) · **Cần trước:** Phase 27.4 (`cite-check.ts`, `cite-ref.ts`), Phase 44, 56, 24.

## Mục tiêu · làm · không làm

- **Xong khi:** 2 báo cáo niche + 1 báo cáo đối thủ thật, xuất được, 0 cờ đỏ · kiểm tay 15 trích dẫn đúng hết · evidence pack mở bằng
  `/app-research` đọc được không sửa.
- **Làm:** khung 4 mục, trích dẫn về ô bảng / dòng nguồn, kiểm (còn cờ đỏ → không xuất), sửa tay trên trang (ghi "người viết"), evidence pack.
- **Không làm:** sinh concept / giá / spec · PDF / slide · gửi báo cáo.

## Global Constraints

- Khung cố định: 1 Kết luận 3 dòng · 2 Mỗi niche / đối thủ mạnh ở đâu, yếu ở đâu · 3 Rủi ro (dữ liệu thiếu, nguồn chưa tra) · 4 Câu hỏi còn mở.
- AI **không** đổi ô thắng của Phase 44; khác ý → mục Rủi ro kèm trích dẫn. Kiểm bằng code: câu nói "X thắng hàng Y" trái `winners()` → cờ đỏ.
- Câu sửa tay lưu `by: 'human'`, không qua kiểm AI nhưng vẫn kiểm số nếu có ref.
- Xuất bị chặn khi còn cờ đỏ (API trả 409).

## File đụng tới

- `web/src/lib/report/compare-report.ts` (mới) — prompt + schema 4 mục, gọi `aiAsk(db, 'report')`, chạy `cite-check` + kiểm ô thắng
- `web/src/db/schema.ts` + migration mới — `reports` (kind `niche | app`, inputIds, json, status, createdAt, updatedAt)
- `web/src/server/app.ts` — `POST /reports` · `GET /reports/:id` · `POST /reports/:id/edit` · `GET /reports/:id/evidence.md`
- `web/src/client/ReportPage.tsx` (mới) + nút trên `/compare`, `/compare/apps` — đọc, sửa câu, cờ đỏ, xuất
- `web/src/lib/evidence.ts` — gộp bảng so sánh + báo cáo theo khung Phase 7
- `web/tests/compare-report.test.ts` — Ask giả

## Tasks

### Task 1: Sinh + kiểm
- [ ] `compare-report.ts` + migration; test: câu trái ô thắng → cờ đỏ; ref sai → cờ đỏ.

### Task 2: Trang + sửa tay
- [ ] `ReportPage`: 4 mục, cờ đỏ, sửa / xoá câu (lưu `human`), kiểm lại.

### Task 3: Xuất evidence pack
- [ ] Chặn khi còn cờ đỏ; `.md` theo khung Phase 7 + bảng + báo cáo; thử `/app-research` đọc.

### Task 4: Chạy thật + soát
- [ ] 2 báo cáo niche + 1 đối thủ; kiểm tay 15 trích dẫn. Screenshot 1340 + 375, Read. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
