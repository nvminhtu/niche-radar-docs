# niche-radar Phase 3 — Google Trends — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm test && npm run typecheck && npm run lint`
> xanh rồi mới commit. Steps dùng checkbox (`- [ ]`).

**Goal:** biết nhu cầu đang lên hay xuống (cột xu hướng cho Top 10 cơ hội), so tối đa 5 keyword trên một biểu đồ,
nước nào quan tâm nhất, có mùa vụ không (5 năm).

**Spec:** `docs/phase-3-google-trends.md` + master plan §3 Phase 3. **Mockup:** `design/mockups/phase3-trends/`.

## Mục tiêu · làm · không làm

- **Xong khi:** Top 10 của 3 niche thật có cột xu hướng, một lần chạy không bị Trends chặn · so 5 keyword + theo nước +
  mùa vụ chạy được trên 1 niche thật · screenshot đã Read.
- **Làm:** 5 Task bên dưới, tất cả trên trang Explore `/explore/:id`, **bấm mới tải**.
- **Không làm:** hỏi Trends cho cả 100 keyword · số lượt tìm thật (Trends chỉ cho 0–100) · related topics (xem lệch) ·
  thay đổi khối Trends của trang run.

## Đo trước khi code (2026-10-24, `google-trends-api` 4.9.2)

| Gọi | Kết quả |
|---|---|
| `interestOverTime` 5 keyword, US, 12 tháng | ✅ 53 điểm tuần, mỗi điểm 5 giá trị (cùng thang trong 1 request) |
| `interestOverTime` 1 keyword, 5 năm | ✅ 261 điểm tuần |
| `interestByRegion` resolution COUNTRY, toàn cầu | ✅ (water reminder: US 100, Singapore 90, UAE 80…) |
| `relatedTopics` | ❌ `rankedList: []` cho mọi keyword thử (`water reminder`, `habit tracker`, `budget app`, `budget`) → **bỏ** khỏi Phase 3, related queries v1 vẫn có |

## Global Constraints

- Nhánh `phase3-trends` cắt từ `main` (`fd7671b`, đã có Phase 2).
- Mọi lệnh Trends đi qua một limiter chung 1 request / 4 giây + retry 2s/5s/10s khi bị chặn (dùng lại `withRetry`).
- Cache `trends_cache(key, body, fetched_at)`: 12 tháng 1 ngày, 5 năm + theo nước 7 ngày.
- Xu hướng một keyword = so trung bình 13 tuần cuối với 13 tuần đầu của 12 tháng: > +20% **lên**, < −20% **xuống**,
  còn lại **phẳng**; cả hai trung bình < 1 → **ít dữ liệu**. Ghi công thức trên UI.
- Gom request: Top 10 hỏi theo lô 5 keyword (2 request). Keyword bị keyword to trong lô đè thành ~0 (max < 5 trong khi
  lô có keyword ≥ 50) → hỏi lại riêng (tối đa 4 request thêm).

## Tasks

### Task 1: Lớp gọi Trends dùng chung + cache
- [x] `collectors/trends.ts`: export `trendsLimit` (4s) và `callTrends` dùng chung; collector v1 đi qua cùng limiter.
- [x] Bảng `trends_cache` (migration `0006`), `cachedTrends(db, method, opts, ttl)`.
- [x] Test: cache theo key, hết hạn thì gọi lại, trang HTML → RATE_LIMITED.

### Task 2: Xu hướng cho Top 10 cơ hội
- [x] `lib/trend-direction.ts`: `trendDirection(points)` → `{ direction: 'up'|'down'|'flat'|'low', changePct }`.
- [x] `normalizeMulti(json, terms)` tách series từng keyword từ 1 request nhiều keyword.
- [x] Bảng `node_trends(node_id, direction, change_pct, points json, fetched_at)` (migration `0006`).
- [x] `POST /api/explore/:id/trends` → Top 10 theo điểm cơ hội (cùng thứ tự với khối Top cơ hội), lô 5 + hỏi lại riêng; trả kết quả.
- [x] `getExploreView` kèm `trend` cho mỗi node.
- [x] Test: hướng từng ca, tách series, chọn Top 10, hỏi lại riêng khi bị đè.

### Task 3: Xu hướng niche — so 5 keyword · theo nước · mùa vụ 5 năm
- [x] `GET /api/explore/:id/trends-deep?terms=a|b|…` (≤ 5, mặc định Top 5 cơ hội có xu hướng) → `{ compare, regions, season }`.
- [x] `season`: 5 năm của seed → trung bình theo tháng dương lịch, tháng đỉnh/đáy, độ mùa vụ `(max − min) / trung bình`
      (≥ 0.5 = "có mùa vụ rõ").
- [x] `regions`: top 10 nước theo `interestByRegion` (toàn cầu, 12 tháng).
- [x] Test: tính mùa vụ trên series giả có đỉnh tháng 1, parse region, giới hạn 5 terms.

### Task 4: UI theo mockup
- [x] `NicheMap` → khối Top cơ hội: nút "Đọc xu hướng Top 10", cột **Xu hướng** (mũi tên + % + sparkline nhỏ).
- [x] Bảng keyword Explore: cột Xu hướng (chỉ node đã đọc).
- [x] Khối mới `TrendsDeepBlock`: chọn ≤ 5 keyword (checkbox đã có) → biểu đồ so sánh; mùa vụ 12 cột; top nước.
- [x] Test render.

### Task 5: Build + chạy thật + tài liệu
- [x] `npm run build && npm start`, `npm run docs:build`.
- [x] Chạy thật Top 10 cho 3 exploration (water reminder, budget tracker, meal planner) + khối niche cho 1 → bảng kết quả.

## Tiến độ

- 2026-10-24: probe Trends (bảng trên), viết plan, giao Codex mockup.
- 2026-10-24: Task 1–3 (`206ff34`), Task 4–5 (`8622164`) — 158 test xanh lúc xong Phase 3; sau khi gộp Task 10–11 Phase 1: 176.
  Sửa sau chạy thật: (1) keyword < nửa số tuần có số → "ít dữ liệu"; (2) so sánh mặc định = seed + keyword có hướng thật;
  (3) bỏ lãnh thổ < ~100k dân ở bảng nước; (4) `google-trends-api` ném SyntaxError khi Google trả trang chặn → RATE_LIMITED + thử lại.

## Kết quả chạy thật

Đo 2026-10-24, US, Top 10 cơ hội (lô 5 + hỏi lại keyword bị đè):

| Exploration | Có hướng | Ít dữ liệu | Keyword có hướng |
|---|---|---|---|
| water reminder (#11) | 0 | 10 | — |
| budget tracker (#6) | 1 | 9 | `budget tracker free` ▼ −38% |
| meal planner (#4) | 1 | 9 | `meal planner app` ▲ +26% |

Đọc: long-tail trong Top 10 cơ hội phần lớn quá nhỏ với Google Trends (toàn 0, vài đỉnh lẻ) — cột Xu hướng chỉ có ích
với keyword đầu niche; muốn đo long-tail phải dùng nguồn khác (autocomplete/Play) chứ không phải Trends.

Khối niche `meal planner` (#4): mùa vụ 5 năm đỉnh T1, đáy T11, độ lệch 45% → "không rõ mùa vụ" (ngưỡng 50%);
top nước Australia 41 · New Zealand 40 · UK 39 · US 24 · Ireland 24 (trước khi lọc, St. Helena đứng đầu 100).
Phần so sánh lần đo thứ hai bị Google chặn tạm (RATE_LIMITED) — giờ báo chữ dễ hiểu, phần mùa vụ + nước vẫn hiện.
