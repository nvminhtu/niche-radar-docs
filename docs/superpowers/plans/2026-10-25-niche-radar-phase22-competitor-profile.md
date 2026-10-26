# Niche Radar Phase 40 — Hồ sơ đối thủ + cờ đối thủ yếu — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** mỗi đối thủ có **một trang riêng**; bảng đối thủ có **cờ** để thấy ngay ai yếu.

**Spec:** [Phase 40 · Hồ sơ đối thủ](../../web/phase-40-competitor-profile.md) · **Cần trước:** Phase 18 (lời chê theo app),
Phase 37 (doanh thu verified), Phase 20 (collect đối thủ).

## Mục tiêu · làm · không làm

- **Xong khi:** 3 niche thật: kiểm tay 15 cờ, ≥ 14 đúng với trang store · nối Play ↔ iOS: kiểm tay 10 cặp, **0 cặp nối sai** ·
  trang đối thủ đọc được 1340 + 375, screenshot đã Read.
- **Làm:** trang `/app/:store/:id`, 5 cờ trên bảng đối thủ, nối cùng app 2 store, đối thủ xuất hiện ở niche nào, Collect đối thủ.
- **Không làm:** so 2–5 đối thủ (Phase 55) · theo dõi thay đổi theo thời gian (Phase 41) · AI gắn "yếu".

## Global Constraints

- 5 cờ là luật cố định, ngưỡng ở `settings` (`flags.*`), tooltip ghi luật: `bỏ bê` (cập nhật > 12 tháng) · `bị chê`
  (★ < 4 và ≥ 1k rating) · `một store` · `thu tiền` (subscription / mua đứt từ `lib/money.ts`) · `mới vào` (ra mắt < 12 tháng mà ở top).
- **Nối 2 store thiên về không nối**: chỉ nối khi cùng web domain (listing) **hoặc** cùng dev + cùng tên thương hiệu. Không chắc → để riêng.
  (Bài học Phase 2: ghép chỉ bằng tên trong kết quả quét sai gần hết — đã gỡ tab "Chỉ 1 store" 2026-10-25.)
- Cờ `một store` chỉ bật khi **đã tra store bên kia** theo tên + dev (gọi search store kia, cache) và không thấy — không suy từ kết quả quét.
- Gọi thêm store kia chỉ cho top 10 mỗi run, theo rate limit hiện có.

## File đụng tới

- `web/src/db/schema.ts` + migration mới — `app_links` (playAppId, iosAppId, by `domain | dev-brand | manual`, checkedAt), `cross_store_checks` (appId, found, checkedAt)
- `web/src/lib/competitor-flags.ts` (mới) — 5 cờ + lý do
- `web/src/lib/app-link.ts` (mới) — nối 2 store theo luật chặt + tra store kia
- `web/src/lib/competitor-profile.ts` (mới) — gom: 2 store, dev, ra mắt, cập nhật cuối + nhịp (từ `app_snapshots`), rating, giá / IAP, mô hình tiền, lời chê, tính năng (gap), doanh thu, niche xuất hiện
- `web/src/server/app.ts` — `GET /api/apps/:id` · `POST /api/apps/:id/link` (nối / tách tay)
- `web/src/client/AppPage.tsx` (mới) + `main.tsx` — trang `/app/:id`, 1 cột
- `web/src/components/CompetitorBlock.tsx` — cột cờ (chip + tooltip), tên app link sang trang đối thủ
- `web/tests/competitor-flags.test.ts`, `app-link.test.ts`

## Tasks

### Task 1: Cờ
- [ ] `competitor-flags.ts` + ngưỡng ở Cài đặt; cột cờ trong bảng. Test từng cờ.

### Task 2: Nối 2 store
- [ ] `app-link.ts` (domain / dev + thương hiệu), tra store kia cho top 10; nối / tách tay. Test: 2 app tên giống, dev khác → không nối.

### Task 3: Trang đối thủ
- [ ] `competitor-profile.ts` + `AppPage`: đủ mục spec, mục thiếu ghi "chưa đo"; "xuất hiện ở niche nào" (query `keyword_hits`).
- [ ] Nút Collect đối thủ (Phase 20).

### Task 4: Soát
- [ ] 3 niche: kiểm tay 15 cờ + 10 cặp nối → bảng dưới. Screenshot 1340 + 375, Read. `features.ts`, chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.

## Kết quả chạy thật

| Niche | Cờ đúng / kiểm | Cặp nối đúng / kiểm |
|---|---|---|
| — | chưa đo | chưa đo |
