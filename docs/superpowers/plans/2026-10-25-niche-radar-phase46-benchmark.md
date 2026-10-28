# ShotMatic Backlog 05 — Đo mốc — Implementation Plan

> **For agentic workers:** phase **chỉ đo**, không sửa cho nhanh. Mỗi Task xong thì `npm run check` xanh rồi commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** biết tool đang chậm ở đâu: lệnh đo thời gian, RAM, dung lượng từng luồng chính → bảng mốc cho Backlog 06–B07 so lại.

**Spec:** [Backlog 05 · Đo mốc](../../web/phase-backlog-05-benchmark.md) · **Cần trước:** không (Version 5 bắt đầu ở đây).

## Mục tiêu · làm · không làm

- **Xong khi:** `npm run bench` chạy 3 lần liên tiếp, mỗi số chênh ≤ 15% · `bench/baseline.json` đủ 9 chỉ số cho 3 niche, bảng mốc trong
  trang phase · chỉ ra luồng / query chậm nhất.
- **Làm:** bộ 3 niche chuẩn, `npm run bench`, `bench/baseline.json`, script so kết quả (bảng keyword + điểm) giữa 2 lần chạy.
- **Không làm:** sửa cho nhanh · đặt mục tiêu trước khi đo · gọi nguồn nhanh hơn giới hạn.

## Global Constraints

- 9 chỉ số / niche: thời gian tới kết quả đầu tiên · tổng thời gian Research · tổng thời gian Explore · thời gian mở `/`, `/r/:id`, `/explore/:id`,
  `/projects/:id` · query SQLite chậm nhất (tên + ms) · RAM server đỉnh (`process.memoryUsage().rss`) · dung lượng bundle JS + CSS.
- Đo trên DB **bản sao** (`NICHE_DB` tạm) có dữ liệu thật — không ghi vào DB anh đang dùng.
- Đo thời gian mở trang bằng Playwright (`page.goto` → chờ khối chính có số) — cài Playwright ở đây, Backlog 09 dùng lại.
- Query chậm: bọc `better-sqlite3` bằng hàm đo (bật qua `NR_PROFILE=1`), ghi `{ sql, ms }` top 10.
- Mạng thật cho Research / Explore (đo là đo thật), giữ rate limit hiện có. Lệch > 15% → chạy lại lúc mạng ổn, ghi lý do.
- Script so (`bench/compare.ts`): 2 lần chạy cùng niche cùng ngày → cùng danh sách keyword (bỏ thứ tự), cùng điểm (±0,01).

## File đụng tới

- `bench/niches.json` (mới) — 3 niche chuẩn + country
- `bench/run.ts` (mới) — chạy luồng, đo 9 chỉ số, ghi `bench/out/<ngày>.json`
- `bench/compare.ts` (mới) — so 2 file kết quả + so bảng keyword / điểm
- `bench/baseline.json` (mới) — mốc đã chốt
- `web/src/db/client.ts` — hook đo query khi `NR_PROFILE=1`
- `package.json` gốc — `bench`, `bench:compare`
- `docs/web/phase-backlog-05-benchmark.md` — bảng mốc + luồng chậm nhất
- `README.md`, `CLAUDE.md`, `docs/cach-dung.md`, `CHANGELOG.md` — folder + lệnh mới (luật repo)

## Tasks

### Task 1: Khung đo
- [ ] `bench/` + 3 niche chuẩn; đo thời gian Research / Explore qua API (`POST /research`, chờ job xong). Test nhỏ cho `compare.ts`.

### Task 2: Trang + RAM + bundle + query
- [ ] Playwright đo mở trang; RSS đỉnh; `vite build` đọc kích thước `dist/assets`; hook query.

### Task 3: Ổn định + mốc
- [ ] Chạy 3 lần, chênh ≤ 15%; chốt `baseline.json`; bảng mốc + "chậm nhất" vào trang phase.

### Task 4: Ghi lại
- [ ] README / CLAUDE.md / Cách dùng / CHANGELOG cho folder `bench/`. Chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan. Explore hiện ~6 phút / 100 keyword (chưa đo bằng bench).
