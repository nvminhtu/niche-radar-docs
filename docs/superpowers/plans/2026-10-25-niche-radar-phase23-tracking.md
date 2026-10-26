# Niche Radar Phase 42 — Theo dõi niche định kỳ — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** theo dõi **tự chạy theo lịch** và **chỉ báo cái đáng chú ý**.

**Spec:** [Phase 42 · Theo dõi niche định kỳ](../../web/phase-42-tracking.md) · **Cần trước:** Phase 9 (`lib/tracking.ts`,
`project_snapshots`), Phase 18 (`emerging` — luật "lời chê mới nổi"), Phase 20 (`score_history`), Phase 40 (hàng đợi
`research_queue`), Phase 41 (cờ `bỏ bê`).

## Mục tiêu · làm · không làm

- **Xong khi:** 1 project thật bật theo dõi chạy tự động đủ 2 lần (giả lập ngày), không bấm · luật báo: test dữ liệu giả cho
  từng loại thay đổi, đúng loại nào báo loại đó · hộp "Thay đổi tuần này" + dòng thời gian, screenshot đã Read.
- **Làm:** lịch tự chạy, luật báo, hộp thay đổi trang chủ, dòng thời gian, theo dõi đối thủ đã collect, chọn nhịp từng project.
- **Không làm:** thông báo đẩy / email · chạy khi app tắt.

## Global Constraints

- Chỉ chạy khi server đang chạy: bộ hẹn giờ trong `server/index.ts` (mỗi 15 phút kiểm "đến hạn"), giới hạn N lượt / ngày (settings, mặc định 10).
- **Không chạy song song** — dùng chung hàng đợi lần lượt của Phase 40 (`batch-research.ts`); bị chặn → hoãn tới lần kiểm sau, không dồn.
- Luật báo cố định trong `web/src/lib/tracking-alerts.ts`: đối thủ mới vào top 5 · `bỏ bê` vừa cập nhật · giá / gói đổi ·
  Trends trung bình đổi ≥ 20% · điểm v2 đổi ≥ 1 · lời chê mới nổi. Còn lại → "không có gì mới".
- Giờ qua tham số `now` để test.

## File đụng tới

- `web/src/db/schema.ts` + migration mới — `projects`: `trackEvery` (7/30/90/null), `lastAutoRun` · `tracking_alerts` (projectId, snapshotId, kind, detail json, seenAt) · `tracked_apps` (projectId, appId)
- `web/src/lib/tracking-scheduler.ts` (mới) — `dueProjects(now)`, `tick(deps, now)` → tra lại + `takeSnapshot`
- `web/src/lib/tracking-alerts.ts` (mới) — so 2 snapshot (`diffItem` có sẵn) → alert theo luật
- `web/src/lib/tracking.ts` — snapshot thêm số đối thủ đã collect (giá, rating, lần cập nhật)
- `web/src/server/index.ts`, `app.ts` — hẹn giờ; `GET /alerts/week` · `POST /alerts/:id/seen` · `POST /projects/:id/track`
- `HomePage.tsx` — hộp "Thay đổi tuần này" theo project
- `ProjectPage.tsx`, `TrackingBlock.tsx` — chọn nhịp, dòng thời gian (điểm v2, số đối thủ, Trends — `TrendLine`), so 2 lần chụp
- `web/tests/tracking-*.test.ts`

## Tasks

### Task 1: Nhịp + lịch
- [ ] Cột `trackEvery`, UI chọn 7 / 30 / 90 / tắt. `dueProjects` + `tick` với deps giả. Test: giả lập 2 kỳ → 2 snapshot, không bấm.

### Task 2: Luật báo
- [ ] `tracking-alerts.ts` — mỗi loại 1 test dữ liệu giả; thay đổi nhỏ → "không có gì mới".

### Task 3: Hộp thay đổi + dòng thời gian
- [ ] Trang chủ: alert 7 ngày theo project, bấm mở so 2 lần chụp; đánh dấu đã xem.
- [ ] Trang project: biểu đồ, chấm = 1 lần chụp — chỗ duy nhất vẽ điểm theo thời gian (Phase 20 chỉ lưu `score_history`).

### Task 4: Theo dõi đối thủ
- [ ] Đối thủ đã collect: lưu giá, rating, lần cập nhật mỗi snapshot; alert giá đổi / vừa cập nhật.

### Task 5: Soát
- [ ] Bật theo dõi 1 project thật, giả lập 2 kỳ. Screenshot hộp + dòng thời gian 1340 + 375, Read. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
- 2026-10-26: review plan — thêm Phase 18, 40 vào Cần trước; biểu đồ điểm chỉ làm ở đây.
