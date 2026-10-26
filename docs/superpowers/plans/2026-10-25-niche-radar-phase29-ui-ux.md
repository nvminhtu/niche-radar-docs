# Niche Radar Phase 24 — UI / UX Improvement — Implementation Plan

> **For agentic workers:** chỉ sửa chỗ **vướng thật**, không thêm tính năng. Mỗi màn sửa xong thì `npm run check` xanh,
> có screenshot trước / sau đã Read, rồi commit. Steps dùng checkbox (`- [ ]`).

**Goal:** tool dễ dùng hơn — ít bấm hơn, đọc nhanh hơn, không lạc.

**Spec:** [Phase 24 · UI / UX Improvement](../../web/phase-24-ui-ux.md) · **Cần trước:** Phase 25 (chỗ vướng ghi được khi đi 5 niche).

## Mục tiêu · làm · không làm

- **Xong khi:** danh sách chỗ vướng có trạng thái từng mục (sửa / bỏ + lý do) · mỗi màn sửa có screenshot trước / sau đã Read.
- **Làm:** soát 6 mặt (luồng chính · trạng thái · bảng dày · sáng / tối · bàn phím + đọc màn hình · cỡ màn), sửa theo danh sách.
- **Không làm:** tính năng mới (ghi Phase 9) · đổi hết giao diện vì thích.

## Global Constraints

- Danh sách chỗ vướng = bảng trong trang phase: `# · màn · mặt · vướng gì · bằng chứng · sửa / bỏ · lý do`.
- Đo luồng chính bằng số: số lần bấm từ gõ niche tới thấy gợi ý BUILD / TEST THÊM / BỎ (trước / sau).
- Tương phản WCAG AA 4.5:1 cho chữ, cả sáng và tối (đo bằng script, vd `axe-core` trong Playwright hoặc tính từ token màu).
- Cỡ màn kiểm: 1280 · 1340 · 375. Tài liệu / màn đọc: 1 cột (luật repo).
- Screenshot trước / sau lưu `design/ui-29/<màn>-before|after-<cỡ>.png`.

## File đụng tới

- `docs/web/phase-24-ui-ux.md` — danh sách chỗ vướng + trạng thái
- `web/tests/e2e/a11y.spec.ts` (mới, nếu Backlog 09 chưa có Playwright thì dùng script tạm) — tương phản + phím Tab tới mọi nút chính
- `web/src/components/*`, `web/src/client/*` — sửa theo danh sách
- `web/src/client/globals.css`, `components/charts/theme.tsx` — token màu nếu tương phản trượt
- `design/ui-29/` — screenshot

## Tasks

### Task 1: Soát + lập danh sách
- [ ] Đi luồng chính trên 3 niche, đếm số bấm. Mở mọi màn ở 3 cỡ, sáng + tối.
- [ ] Kiểm trạng thái đang tải · rỗng · lỗi · bị chặn từng màn (dùng fixture lỗi của Phase 22).
- [ ] Phím Tab + VoiceOver trên Research, Explore, Project. Ghi mọi chỗ vướng có screenshot "trước".

### Task 2: Sửa theo thứ tự đau nhất
- [ ] Mỗi mục: sửa nhỏ nhất đủ hết vướng, test nếu đụng logic, screenshot "sau", đổi trạng thái. Mục không sửa → "bỏ" + lý do.

### Task 3: Kiểm tự động
- [ ] Test tương phản + phím Tab cho 3 màn chính chạy trong `npm run check` (hoặc ghi rõ chạy tay nếu cần trình duyệt).

### Task 4: Soát
- [ ] Đếm lại số bấm luồng chính. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
