# ShotMatic Backlog 06 — Collector nhanh hơn — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` xanh + `npm run bench:compare` không tệ đi rồi commit.
> Steps dùng checkbox (`- [ ]`). Không gọi nhanh hơn giới hạn, không proxy.

**Goal:** nguồn **chạy cùng lúc**, kết quả hiện dần, không tra lại thứ vừa tra.

**Spec:** [Backlog 06 · Collector nhanh hơn](../../web/phase-backlog-06-fast-collector.md) · **Cần trước:** Backlog 05 (`bench/baseline.json`, `compare.ts`).

## Mục tiêu · làm · không làm

- **Xong khi:** kết quả đầu tiên ≤ 30 giây · tổng thời gian ≈ nguồn chậm nhất + ≤ 10% · không nguồn nào bị chặn nhiều hơn mốc · ngắt mạng
  giữa chừng rồi bật lại → chạy tiếp · `npm run bench`: không chỉ số nào tệ đi quá 10% so với mốc.
- **Làm:** song song theo nguồn (giữ limiter từng nguồn), đổ kết quả dần (stream), cache theo keyword dùng chung giữa niche (24 giờ), chạy tiếp khi lỗi.
- **Không làm:** gọi nhanh hơn giới hạn / nhiều IP · hàng đợi cloud · nguồn mới.

## Global Constraints

- Mỗi nguồn 1 hàng đợi (`createLimiter` hiện có trong `lib/rate-limit.ts`); song song **giữa** nguồn, không song song **trong** một nguồn vượt limiter.
- Stream bằng Server-Sent Events (`GET /api/research/:id/events`) — UI vẫn đọc được bằng poll cũ nếu SSE đứt.
- Cache keyword dùng chung: bảng `keyword_cache` khoá `(source, term, country)`, hạn 24 giờ (`CACHE_MS`); run mới đọc cache trước khi gọi.
- Chạy tiếp: mỗi job ghi `progressDone` + danh sách keyword đã xong (`source_jobs.checkpoint` json); restart / retry đọc checkpoint.
- Kết quả không đổi: `bench:compare` cùng niche cùng ngày phải trùng (bảng keyword + điểm).

## File đụng tới

- `web/src/lib/run-research.ts` — chạy nguồn song song (`Promise.allSettled`), checkpoint, đọc cache
- `web/src/collectors/*.ts` — ghi từng phần ngay khi có, nhận checkpoint
- `web/src/db/schema.ts` + migration mới — `keyword_cache`, `source_jobs.checkpoint`
- `web/src/server/app.ts` — SSE `/research/:id/events`
- `web/src/components/progress-hooks.ts`, `ProgressPanel.tsx`, `RunDashboard.tsx` — nhận SSE, vẽ khối khi có dữ liệu
- `web/tests/run-research*.test.ts` — deps giả có độ trễ, lỗi giữa chừng

## Tasks

### Task 1: Song song theo nguồn
- [ ] `startResearch` chạy các nguồn cùng lúc; test: tổng thời gian ≈ nguồn chậm nhất (deps giả có sleep).

### Task 2: Ghi dần + SSE
- [ ] Collector ghi từng phần; SSE đẩy sự kiện; UI vẽ dần, fallback poll. Test SSE nhận đủ sự kiện.

### Task 3: Cache dùng chung
- [ ] `keyword_cache` + đọc trước khi gọi. Test: niche B dùng lại keyword niche A → 0 lần gọi.

### Task 4: Chạy tiếp khi lỗi
- [ ] Checkpoint; test: lỗi mạng ở keyword 5/10 → retry bắt đầu từ 6.

### Task 5: Đo lại
- [ ] `npm run bench` + `bench:compare`; ghi bảng trước / sau vào trang phase. Thử ngắt mạng thật giữa chừng. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
