# ShotMatic Backlog 07 — UI + DB nhanh — Implementation Plan

> **For agentic workers:** chỉ sửa chỗ Backlog 05 **đo ra chậm**. Mỗi Task xong thì `npm run check` xanh + `bench:compare` không tệ đi rồi commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** bảng nghìn dòng không giật, trang mở nhanh, query nhanh.

**Spec:** [Backlog 07 · UI + DB nhanh](../../web/phase-backlog-07-fast-ui-db.md) · **Cần trước:** Backlog 05 (danh sách chậm nhất), Phase 47.

## Mục tiêu · làm · không làm

- **Xong khi:** bảng 1.000 keyword cuộn mượt · mở trang niche ≤ 1 giây với DB 50 niche · bundle trang chủ nhỏ hơn mốc · `bench:compare` cùng
  kết quả · test xanh, không chỉ số nào tệ đi quá 10%.
- **Làm:** virtualize bảng > 200 dòng, lazy load từng trang, index cho query chậm đã đo, WAL, API trả từng trang.
- **Không làm:** đổi framework / DB · sửa chỗ chưa đo là chậm · đổi giao diện.

## Global Constraints

- Virtualize bằng `@tanstack/react-virtual` (nhỏ, không đổi kiểu bảng) — bắt đầu `KeywordTable.tsx`, rồi bảng nào > 200 dòng thật.
- Lazy load: `React.lazy` + route `lazy` của react-router cho mọi trang trừ `HomePage`.
- Index chỉ cho query trong top 10 chậm của Backlog 05; mỗi index ghi query nó phục vụ (comment trong schema) + ms trước / sau.
- WAL: `PRAGMA journal_mode = WAL` khi mở DB; backup (Phase 39) phải xử lý file `-wal` (dùng API backup nên ổn — test lại).
- Phân trang API: `?page=&size=` (mặc định 100) cho danh sách lớn (explore nodes, keywords, lịch sử); client cũ không truyền → trang 1 + `total`.
- DB 50 niche để đo: script tạo từ fixture (`bench/seed-50.ts`), không dùng DB thật.

## File đụng tới

- `web/src/components/KeywordTable.tsx` (+ bảng lớn khác theo đo) — virtualize
- `web/src/client/main.tsx` — lazy route
- `web/src/db/schema.ts` + migration mới — index
- `web/src/db/client.ts` — WAL
- `web/src/server/app.ts`, `lib/explore-view.ts`, `lib/run-view.ts` — phân trang
- `bench/seed-50.ts` (mới) — DB 50 niche
- `web/tests/*` — phân trang, WAL + backup

## Tasks

### Task 1: DB 50 niche + đo lại mốc trang niche
- [ ] `seed-50.ts`; đo mở `/r/:id` → mốc riêng của phase.

### Task 2: Index + WAL
- [ ] Index cho từng query chậm (ms trước / sau); WAL + test backup với WAL.

### Task 3: Phân trang API
- [ ] Danh sách lớn trả trang; test `total`, trang cuối.

### Task 4: Virtualize + lazy load
- [ ] Bảng 1.000 dòng (đo FPS khi cuộn bằng Playwright `requestAnimationFrame` đếm khung, ghi số); lazy route, đo bundle trang chủ.

### Task 5: Đo lại
- [ ] `npm run bench` + `bench:compare`; bảng trước / sau vào trang phase. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
