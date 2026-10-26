# Niche Radar Phase 52 — Canary nguồn thật — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` xanh rồi commit.
> Steps dùng checkbox (`- [ ]`). Canary chỉ báo, không tự sửa collector.

**Goal:** mỗi ngày tự gọi thật một lượt nhỏ tới từng nguồn; nguồn đổi dạng / bị chặn → biết trong 1 ngày.

**Spec:** [Phase 52 · Canary nguồn thật](../../web/phase-52-source-canary.md) · **Cần trước:** Phase 50 (fixture + `_meta`, collector nhận `fetcher`).

## Mục tiêu · làm · không làm

- **Xong khi:** chạy 7 ngày liền có log trong `canary/log.md` · cố tình đổi fixture → báo "nguồn đổi dạng" · nguồn bị chặn / rỗng → thông báo macOS ghi rõ nguồn.
- **Làm:** lệnh `npm run canary`, so dạng dữ liệu với fixture, thông báo macOS + log, LaunchAgent chạy mỗi ngày.
- **Không làm:** gọi dày / nhiều keyword · chạy trên server / CI · tự sửa collector.

## Global Constraints

- 1 keyword nhỏ cố định / nguồn (`canary/keywords.json`), giữ limiter từng nguồn.
- So **dạng** chứ không so giá trị: sinh "hình dạng" (tên trường + kiểu + có rỗng không) từ fixture và từ phản hồi thật → khác → `shape_changed`.
  Rỗng → `empty`; HTTP 429 / captcha → `blocked`.
- Thông báo macOS qua `osascript -e 'display notification …'` (không cài thêm gì). Không phải macOS → chỉ ghi log.
- LaunchAgent `~/Library/LaunchAgents/com.oneclicktool.niche-radar-canary.plist` — script `canary/install.sh` cài / gỡ, **anh chạy** (không tự cài vào máy).
- `canary/log.md` gitignore phần chi tiết; chỉ commit tóm tắt 7 ngày vào trang phase.

## File đụng tới

- `canary/run.ts` (mới) — gọi mọi collector qua `fetcher` thật, so dạng, ghi log, thông báo
- `canary/shape.ts` (mới) — sinh + so hình dạng
- `canary/install.sh`, `canary/uninstall.sh`, plist mẫu (mới) — LaunchAgent 1 lần / ngày
- `canary/keywords.json` (mới) — keyword từng nguồn
- `package.json` gốc — `canary`
- `web/tests/canary-shape.test.ts`
- `README.md`, `CLAUDE.md`, `docs/cach-dung.md`, `CHANGELOG.md` — folder mới

## Tasks

### Task 1: So dạng
- [ ] `shape.ts` + test: thêm / bớt / đổi kiểu trường → `shape_changed`.

### Task 2: Lệnh canary
- [ ] `run.ts`: gọi nguồn, phân loại `ok | empty | blocked | shape_changed | error`, log + thông báo. Test với fetcher giả.

### Task 3: Lịch chạy
- [ ] `install.sh` / `uninstall.sh` + plist; anh cài. Ghi lệnh vào Cách dùng.

### Task 4: Chạy 7 ngày + thử lỗi
- [ ] Sửa tạm fixture → canary báo; tắt mạng 1 nguồn → thông báo đúng tên. 7 ngày log → tóm tắt vào trang phase. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
