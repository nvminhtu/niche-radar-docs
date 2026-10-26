# Niche Radar Backlog 08 — Test collector bằng fixture — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` xanh rồi commit. Không sửa test cho xanh khi code sai.
> Steps dùng checkbox (`- [ ]`).

**Goal:** ghi **phản hồi thật** của từng nguồn một lần; test chạy trên bản ghi — nhanh, không mạng, sửa collector không hỏng âm thầm.

**Spec:** [Backlog 08 · Test collector bằng fixture](../../web/phase-backlog-08-fixture-tests.md) · **Cần trước:** các collector đã có (Version 1–4).

## Mục tiêu · làm · không làm

- **Xong khi:** `npm test` xanh khi tắt mạng · mỗi collector ≥ 1 test trên fixture thật · độ phủ `web/src/lib` + `web/src/collectors` có số,
  ghi vào trang phase · có danh sách file chưa có test.
- **Làm:** `npm run record`, test mỗi collector, đo coverage, test lớp kiểm trích dẫn (Phase 27.4), test công thức điểm (Phase 1, 61).
- **Không làm:** mục tiêu 100% · CI (Version 7) · sửa test cho xanh khi code sai.

## Global Constraints

- `record` gọi mạng thật **một lần**, lịch sự (limiter hiện có), lưu `web/tests/fixtures/<nguồn>/<tên>.json|html` kèm `_meta` (url, ngày, phiên bản thư viện).
  Bỏ dữ liệu cá nhân (tên người viết review) trước khi lưu.
- Test chặn mạng: `vitest` setup file thay `fetch` toàn cục bằng hàm ném lỗi "network disabled in tests" — test nào gọi mạng là đỏ.
- Collector nhận `fetcher` qua tham số (đa số đã có kiểu `FetchReviews`, `FetchText`) — cái nào chưa thì thêm tham số, không mock module.
- Coverage bằng `@vitest/coverage-v8`, lệnh `npm run coverage` (không chạy trong `check` để `check` nhanh).

## File đụng tới

- `web/scripts/record.ts` (mới) + `web/package.json` — `npm run record [nguồn]`
- `web/tests/setup/no-network.ts` (mới) + `vitest.config` — chặn mạng
- `web/tests/fixtures/{playstore,appstore,trends,trustmrr,youtube,amazon,serp,…}/` — fixture
- `web/tests/collectors/*.test.ts` — 1 file / collector
- `web/src/collectors/*.ts` — thêm tham số `fetcher` nơi thiếu
- `docs/web/phase-backlog-08-fixture-tests.md` — số coverage + danh sách file chưa test

## Tasks

### Task 1: Chặn mạng
- [ ] Setup no-network; chạy `npm test`, liệt kê test đang gọi mạng → sửa cho đọc fixture.

### Task 2: Record
- [ ] `record.ts` cho mọi nguồn đang có; lưu fixture + `_meta`; bỏ tên người viết.

### Task 3: Test collector
- [ ] Mỗi file trong `web/src/collectors/` ≥ 1 test fixture thật (parse đúng trường, xử lý trang chặn / rỗng).

### Task 4: Test lõi
- [ ] Lớp kiểm trích dẫn (nếu Phase 27.4 chưa đủ ca), công thức điểm Phase 1 (`popularity`, `crowding`) + Phase 43.

### Task 5: Coverage + ghi lại
- [ ] `npm run coverage`; số + danh sách file chưa test vào trang phase. Tắt Wi-Fi chạy `npm test` → xanh. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan. Đã có fixture `appstore`, `playstore`, `trends`, `trustmrr`.
