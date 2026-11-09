# ShotMatic Phase 56 — So sánh đối thủ — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** đặt **2–5 đối thủ** cạnh nhau — giá, sao, tính năng, bị chê gì, cập nhật — để biết app mình đánh vào ai, hơn ở đâu. Không AI.

**Spec:** [Phase 56 · So sánh đối thủ](../../web/phase-56-compare-competitor.md) · **Cần trước:** Phase 41 (hồ sơ đối thủ), Phase 18
(lời chê theo app), Phase 4 (Feature Gap), Phase 44 (khung bảng so sánh dùng lại).

## Mục tiêu · làm · không làm

- **Xong khi:** 2 niche thật × 4 đối thủ có bảng đủ hàng, ô thiếu "chưa có" · kiểm tay 10 câu than mở đúng review gốc · hàng
  "Chỗ trống" ra ≥ 1 dòng ở ≥ 1 niche.
- **Làm:** chọn đối thủ (gợi ý sẵn), nhóm Tiền · Chất lượng · Tính năng · Bị chê gì · Chỗ trống, xuất CSV + Markdown.
- **Không làm:** cào thêm đối thủ · theo dõi theo thời gian · AI kết luận (Phase 57).

## Global Constraints

- Dữ liệu từ `competitor-profile.ts` (Phase 41) — không query lại kiểu khác.
- Không ước doanh thu; chỉ giá công khai + verified (Phase 38).
- Câu than nguyên văn đã lưu, link review gốc.
- "Chỗ trống" = hàng Feature Gap / "ước gì" có ≥ 3 lần xin mà ≤ 1 đối thủ trong bảng là `yes`.
- Dùng lại component bảng của Phase 44 (`CompareTable`) — tách ra nếu Phase 44 viết liền trong trang.

## File đụng tới

- `web/src/lib/compare-competitor.ts` (mới) — hàng + luật thắng; `suggest(run)` = top 3 theo lượt tải + 1–2 app bị chê nhiều nhất
- `web/src/components/CompareTable.tsx` — dùng chung với Phase 44
- `web/src/server/app.ts` — `GET /api/compare/apps?ids=` + `.csv` + `.md`
- `web/src/client/CompareAppsPage.tsx` (mới) + route — trang so đối thủ; ô tick trong `CompetitorBlock`
- `web/src/lib/features.ts` — "So sánh đối thủ" → done
- `web/tests/compare-competitor.test.ts`
- `web/src/db/schema.ts` + migration — bảng `node_hits` (node · store · app · hạng) cho tab Keyword
- `web/src/collectors/explore-metrics.ts` — giữ id app top 30 Play / App Store thay vì chỉ đếm (không thêm request)
- `web/src/lib/compare-keywords.ts` (mới) — gộp `keyword_hits` + `node_hits` thành bảng keyword × app, lọc app mốc

## Tasks

### Task 0: Lưu app mỗi keyword lúc Explore
- [ ] Migration `node_hits`; `collectLightMetrics` trả thêm danh sách `{ store, storeAppId, rank }` (top 30 mỗi store), ghi vào
      `node_hits` + upsert `apps`. Test: số đếm cũ (`playCount`, `appstoreCount`) không đổi, số request không đổi.

### Task 1: Hàng + gợi ý
- [ ] `compare-competitor.ts`: Tiền (free / trả phí / IAP, giá từng gói, tháng / năm) · Chất lượng (sao, số rating, mức lượt cài Play,
      % 1–2★, ngày ra mắt, cập nhật cuối, 2 store) · Tính năng (từ matrix, link listing) · Bị chê gì (3 chủ đề, số lần, 1 câu + link)
      · Chỗ trống. Test.

### Task 1b: Bảng keyword × app
- [ ] `compare-keywords.ts`: hàng = keyword (ngày đo, điểm phổ biến, mức chen chúc, số app), cột = hạng từng app hoặc "—" kèm N
      đã lưu; đếm số keyword mỗi app có hạng; lọc mức hạng 1–10 / 11–25 / 26+, app mốc là "—" mà ≥ 1 app khác có hạng. Test.

### Task 2: API + xuất
- [ ] 2–5 id (khác → 400); CSV (BOM) + Markdown theo tab; tab Keyword thêm danh sách keyword dạng text.

### Task 3: Trang
- [ ] Tick trong bảng đối thủ → "So sánh (N)" + nút Compare trên dòng app (Research, Keyword search); thẻ app có màu + menu ⋮;
      4 tab Tổng quan · Keyword · Tính năng · Lời chê (`?tab=`); bảng dùng `CompareTable`; ô thiếu "chưa có".

### Task 4: Soát
- [ ] 2 niche × 4 đối thủ; kiểm tay 10 câu than + 10 ô hạng tab Keyword. Screenshot 960 + 1340, sáng + tối, Read. Chip, ROADMAP,
      CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
- 2026-11-06: thêm Task 0 + 1b (tab Keyword, học Competitor Keywords của Appfigures), thẻ app + nút Compare, 4 tab — xem
  [Học từ Appfigures](../../web/phase-56-compare-competitor.md#hoc-tu-appfigures).
