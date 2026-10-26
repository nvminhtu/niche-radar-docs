# Niche Radar Phase 55 — Google Maps Research (AI) — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Không cào Google Maps bằng script / headless.

**Goal:** niche phục vụ cửa hàng / dịch vụ địa phương: một thành phố có bao nhiêu chỗ, khách và chủ than gì → ý tưởng app nhỏ có bằng chứng.

**Spec:** [Phase 55 · Google Maps Research (AI)](../../web/phase-55-google-maps.md) · **Cần trước:** Phase 6 (job Chrome), Phase 43 (evidence pack),
Phase 14 (kết luận nguồn Maps).

## Mục tiêu · làm · không làm

- **Xong khi:** 3 loại cửa hàng × 2 thành phố có số đếm + chủ đề than có trích dẫn · ≥ 1 ý tưởng app có ≥ 3 review làm bằng chứng ·
  chạy được không key (Overpass + Claude in Chrome); có key thì Places API dưới trần.
- **Làm:** đếm chỗ (loại × thành phố, % có web, sao TB), so ≤ 5 thành phố, khách than gì, chủ trả lời gì, ý tưởng app → evidence pack.
- **Không làm:** cào Maps · thu thập liên hệ chủ cửa hàng (lead list).

## Đo trước khi code

| Đo gì | Cách | Ghi vào |
|---|---|---|
| Overpass: đếm `shop=hairdresser` / `leisure=fitness_centre` ở 1 thành phố | 1 query, đo thời gian | bảng này + ngày |
| Places API (New) bảng giá + hạn mức miễn phí | đọc trang giá chính chủ | bảng này (link + ngày) |
| Ánh xạ loại cửa hàng → tag OSM / type Places | 10 loại thường gặp | `web/src/lib/maps-types.ts` |

## Global Constraints

- Không lưu tên / ảnh người viết review — chỉ câu trích + link.
- Places API: key `.env.local`, tắt mặc định, trần số lần gọi / lượt tra (mặc định 20); vượt → dừng, báo.
- Overpass: 1 query / lượt, ≥ 5 giây giữa các query, cache 30 ngày; dùng endpoint công khai, ghi User-Agent có tên tool.
- AI không bịa số — số chỗ / sao / review từ Overpass / Places.
- Đây là chế độ tra **riêng** (loại cửa hàng × thành phố), không gắn vào Research keyword app.

## File đụng tới

- `web/src/db/schema.ts` + migration mới — `maps_runs` (type, city, createdAt), `maps_places` (runId, osmId/placeId, name, rating, reviews, hasWebsite, source), `maps_insights` (runId, kind `complaint | owner_reply | idea`, text, quote, url)
- `web/src/collectors/overpass.ts` (mới) — đếm chỗ + có web / điện thoại
- `web/src/collectors/places.ts` (mới) — Places Text Search (khi có key, có trần)
- `web/src/lib/maps-types.ts` (mới) — loại → tag OSM / type Places
- `web/src/lib/ai/tasks.ts` — task `maps` (job Chrome đọc review top 20 chỗ + trả lời của chủ)
- `web/src/server/app.ts` — `POST /maps` · `GET /maps/:id` · job + import
- `web/src/client/MapsPage.tsx` (mới) + route — chọn loại + ≤ 5 thành phố, bảng so, chủ đề, ý tưởng
- `web/tests/maps-*.test.ts` — fixture Overpass JSON

## Tasks

### Task 1: Đếm chỗ (Overpass)
- [ ] `overpass.ts` + `maps-types.ts` + migration. Test parse fixture.

### Task 2: Places (tuỳ chọn)
- [ ] `places.ts` với trần; không key → bỏ qua, ghi "chưa tra". Test trần.

### Task 3: Job đọc review
- [ ] Job: top 20 chỗ (link Maps), review 1–3★ + trả lời của chủ; nhập: kiểm câu trích, bỏ tên người viết. Test.

### Task 4: Trang + evidence
- [ ] `/maps`: so ≤ 5 thành phố, chủ đề than, chủ trả lời gì, ý tưởng app (≥ 3 review) → nút vào evidence pack.

### Task 5: Chạy thật + soát
- [ ] 3 loại × 2 thành phố. Screenshot 1340 + 375, Read. `features.ts` Google Maps → done, chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
