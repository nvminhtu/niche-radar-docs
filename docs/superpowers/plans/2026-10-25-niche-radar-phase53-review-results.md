# Niche Radar Backlog 11 — Review kết quả — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` xanh rồi commit.
> Steps dùng checkbox (`- [ ]`). Đáp án do anh kiểm tay — Claude không tự viết đáp án rồi tự chấm.

**Goal:** chấm **tool có trả lời đúng không**: bộ 5 niche có đáp án tay, mỗi bản mới ra phiếu review.

**Spec:** [Backlog 11 · Review kết quả](../../web/phase-backlog-11-review-results.md) · **Cần trước:** Backlog 05 (bộ niche chuẩn), Phase 26.4 (`cite-check`), Phase 28.

## Mục tiêu · làm · không làm

- **Xong khi:** phiếu review ra tự động, điểm từng niche + điểm chung · chạy 2 lần cùng dữ liệu ra cùng điểm · phiếu có cột so lần trước.
- **Làm:** 5 niche + đáp án tay, `npm run review`, phiếu `.md`, lịch sử phiếu.
- **Không làm:** AI viết / sửa đáp án · sửa đáp án cho điểm đẹp · CI.

## Global Constraints

- Đáp án `review/answers/<niche>.json`: 10 keyword đáng làm · 5 đối thủ chính · 3 chủ đề than — anh điền (Claude chỉ tạo khung rỗng).
  Sửa đáp án phải có dòng `changes: [{ date, why }]`.
- Chấm trên **dữ liệu đã chụp** (bản sao DB cố định `review/db/<ngày>.db`) để "2 lần cùng dữ liệu ra cùng điểm"; lệnh `--fresh` mới tra lại thật.
- Cách chấm: keyword = số trùng / 10 (so sau chuẩn hoá `mergeKey` của Phase 39) · đối thủ = số trùng / 5 (theo app id) · chủ đề than = trùng
  theo từ khoá nhãn (luật ghi trong code, tay kiểm khi lệch) · trích dẫn = % qua `cite-check` · so sánh niche = % ô khớp màn chi tiết.
- Phiếu `review/reports/<ngày>-v<version>.md`, có cột Δ so phiếu trước.

## File đụng tới

- `review/answers/*.json` (mới, khung rỗng) — anh điền
- `review/run.ts` (mới) — chạy tool trên 5 niche (DB chụp hoặc `--fresh`), chấm, viết phiếu
- `review/score.ts` (mới) — 5 cách chấm
- `package.json` gốc — `review`
- `web/tests/review-score.test.ts`
- `README.md`, `CLAUDE.md`, `docs/cach-dung.md`, `CHANGELOG.md` — folder mới

## Tasks

### Task 1: Khung đáp án
- [ ] 5 file khung + hướng dẫn điền; anh điền đáp án (chặn: chưa có đáp án thì chưa chấm được).

### Task 2: Chấm
- [ ] `score.ts` + test từng cách chấm.

### Task 3: Phiếu + lịch sử
- [ ] `run.ts` viết phiếu + Δ; chạy 2 lần trên DB chụp → cùng điểm.

### Task 4: Ghi lại
- [ ] Phiếu đầu tiên tóm tắt vào trang phase. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
