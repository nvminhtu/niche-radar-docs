# Niche Radar Phase 37 — So sánh đối thủ — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** đặt **2–5 đối thủ** cạnh nhau — giá, sao, tính năng, bị chê gì, cập nhật — để biết app mình đánh vào ai, hơn ở đâu. Không AI.

**Spec:** [Phase 37 · So sánh đối thủ](../../web/phase-37-compare-competitor.md) · **Cần trước:** Phase 22 (hồ sơ đối thủ), Phase 12
(lời chê theo app), Phase 4 (Feature Gap), Phase 28 (khung bảng so sánh dùng lại).

## Mục tiêu · làm · không làm

- **Xong khi:** 2 niche thật × 4 đối thủ có bảng đủ hàng, ô thiếu "chưa có" · kiểm tay 10 câu than mở đúng review gốc · hàng
  "Chỗ trống" ra ≥ 1 dòng ở ≥ 1 niche.
- **Làm:** chọn đối thủ (gợi ý sẵn), nhóm Tiền · Chất lượng · Tính năng · Bị chê gì · Chỗ trống, xuất CSV + Markdown.
- **Không làm:** cào thêm đối thủ · theo dõi theo thời gian · AI kết luận (Phase 39).

## Global Constraints

- Dữ liệu từ `competitor-profile.ts` (Phase 22) — không query lại kiểu khác.
- Không ước doanh thu; chỉ giá công khai + verified (Phase 18).
- Câu than nguyên văn đã lưu, link review gốc.
- "Chỗ trống" = hàng Feature Gap / "ước gì" có ≥ 3 lần xin mà ≤ 1 đối thủ trong bảng là `yes`.
- Dùng lại component bảng của Phase 28 (`CompareTable`) — tách ra nếu Phase 28 viết liền trong trang.

## File đụng tới

- `web/src/lib/compare-competitor.ts` (mới) — hàng + luật thắng; `suggest(run)` = top 3 theo lượt tải + 1–2 app bị chê nhiều nhất
- `web/src/components/CompareTable.tsx` — dùng chung với Phase 28
- `web/src/server/app.ts` — `GET /api/compare/apps?ids=` + `.csv` + `.md`
- `web/src/client/CompareAppsPage.tsx` (mới) + route — trang so đối thủ; ô tick trong `CompetitorBlock`
- `web/src/lib/features.ts` — "So sánh đối thủ" → done
- `web/tests/compare-competitor.test.ts`

## Tasks

### Task 1: Hàng + gợi ý
- [ ] `compare-competitor.ts`: Tiền (free / trả phí / IAP, giá từng gói, tháng / năm) · Chất lượng (sao, số rating, % 1–2★, cập nhật cuối,
      2 store) · Tính năng (từ matrix, link listing) · Bị chê gì (3 chủ đề, số lần, 1 câu + link) · Chỗ trống. Test.

### Task 2: API + xuất
- [ ] 2–5 id (khác → 400); CSV (BOM) + Markdown.

### Task 3: Trang
- [ ] Tick trong bảng đối thủ → "So sánh (N)"; bảng dùng `CompareTable`; ô thiếu "chưa có".

### Task 4: Soát
- [ ] 2 niche × 4 đối thủ; kiểm tay 10 câu than. Screenshot 1340 + 375, Read. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
