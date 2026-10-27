# Niche Radar Phase 44 — So sánh niche — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** đặt **2–4 niche đã tra** cạnh nhau trên một màn, luật thắng / thua rõ ràng. Không AI, không cào thêm.

**Spec:** [Phase 44 · So sánh niche](../../web/phase-44-compare-niche.md) · **Cần trước:** dữ liệu Phase 1–9 (chạy được ngay);
Phase 18, 38 làm số Đau / Tiền tốt hơn nếu đã xong.

## Mục tiêu · làm · không làm

- **Xong khi:** so 3 niche thật ra bảng đủ nhóm, ô thiếu ghi "chưa tra" · kiểm tay 10 ô ngẫu nhiên khớp màn chi tiết ·
  bảng 4 niche đọc được ở 1340px · xuất Markdown dán vào `research/*.md`.
- **Làm:** chọn 2–4 niche, bảng 6 nhóm hàng, ô thắng theo luật, ô thiếu, bấm ô mở chi tiết, xuất CSV + Markdown.
- **Không làm:** > 4 niche · AI kết luận (Phase 57) · so cùng niche 2 thời điểm.

## Global Constraints

- Mọi số từ DB đã có, qua `getRunView` / explore view / `score-v2` / `money` / `trustmrr`. **Không** gọi collector.
- Hàng và luật thắng định nghĩa 1 chỗ: `web/src/lib/compare-niche.ts` → `ROWS = [{ group, key, label, value(view), better: 'high'|'low'|'up', rule }]`.
  Tooltip tên hàng hiện `rule`. Không điểm tổng hợp — chỉ đếm số hàng thắng.
- Ô thiếu → "chưa tra", không tính thắng thua.
- Niche > 7 ngày → nút "tra lại trước khi so" (gọi Research thường, không tự chạy).
- Bảng 4 cột niche + 1 cột nhãn; ở 375px xoay thành từng niche 1 khối (1 cột).

## File đụng tới

- `web/src/lib/compare-niche.ts` (mới) — hàng 6 nhóm: Cơ hội · Đối thủ · Xu hướng · Đau · Tiền · Nguồn mới; `winners()`
- `web/src/server/app.ts` — `GET /api/compare?runs=12,15,18` · `GET /api/compare.csv` · `GET /api/compare.md`
- `web/src/client/ComparePage.tsx` (mới) + `main.tsx` + `NavMenu.tsx` — trang `/compare`, chọn niche (tick trong lịch sử), bảng, ô bấm mở `/r/:id#khối`
- `RunHistory.tsx` — ô tick + nút "So sánh (N)"
- `web/src/lib/features.ts` — "So sánh niche" → done
- `web/tests/compare-niche.test.ts`

## Tasks

### Task 1: Hàng + luật
- [x] `compare-niche.ts`: Cơ hội (số keyword Top cơ hội, điểm cao nhất) · Đối thủ (số app, sao TB top 10, app bỏ bê) · Xu hướng
      (Trends 12 tháng, mùa vụ) · Đau (số chủ đề than, review 1–2★) · Tiền (% app thu phí, khoảng giá, verified) · Nguồn mới (chưa tra).
- [x] Test: luật thắng từng hàng; ô `null` không tính.

### Task 2: API + xuất
- [x] `GET /compare` 2–4 run (khác → 400). CSV (BOM, `csvCell`) + Markdown (bảng + link `/r/:id`).

### Task 3: Trang
- [x] Chọn niche từ lịch sử; bảng tô ô thắng, đếm hàng thắng; ô bấm mở chi tiết; "tra lại trước khi so" cho niche cũ.

### Task 4: Soát
- [x] So 3 niche thật; kiểm tay 10 ô → ghi vào đây. Screenshot 1340 (4 niche) + 375, Read. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
- 2026-10-27: làm xong theo giao diện khối So sánh trên landing (thẻ niche + tab). Khác plan: không API riêng, xuất ở trình duyệt — ghi ở mục Đã làm của [trang phase](../../web/phase-44-compare-niche.md).
