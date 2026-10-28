# ShotMatic Backlog 04 — Sync project — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` xanh rồi commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** đăng nhập máy khác là thấy project, ghi chú, kết luận của mình; chỉ thứ người dùng tự viết lên cloud, dữ liệu cào ở lại máy.

**Spec:** [Backlog 04 · Sync project](../../web/phase-backlog-04-project-sync.md) · **Cần trước:** Backlog 03 (đăng nhập), Backlog 02 (`user_id`), Phase 21–22 (item có `uid`).

## Mục tiêu · làm · không làm

- **Xong khi:** sửa ghi chú máy A → máy B thấy ≤ 10 giây · người B không đọc được dữ liệu người A (test quy tắc) · 2 máy sửa cùng ghi chú → giữ bản
  sau, bản cũ còn trong lịch sử · tắt mạng sửa → bật lại đồng bộ, không mất chữ · không đăng nhập: không gọi Firestore.
- **Làm:** đồng bộ project (tên, trạng thái, thẻ, kết luận, ghi chú, bước tiếp, item kèm snapshot), bộ so sánh, lịch sử hỏi; quy tắc Firestore + test.
- **Không làm:** dữ liệu cào thô lên cloud · team / chia sẻ · gộp sửa từng chữ.

## Global Constraints

- Tên file chốt: `web/src/lib/sync/firestore-sync.ts` (client — Firestore chạy ở trình duyệt, có cache offline sẵn), `web/src/lib/sync/mapping.ts`
  (SQLite row ↔ tài liệu), `firestore.rules` + `firestore.indexes.json` ở gốc repo.
- Cấu trúc: `users/{uid}/projects/{projectUid}`, `…/items/{itemUid}`, `users/{uid}/compares/{id}`, `users/{uid}/asks/{id}`,
  `users/{uid}/projects/{projectUid}/history/{ts}` (bản cũ khi bị ghi đè).
- Xung đột: mỗi tài liệu có `updatedAt` (server timestamp) + `deviceId`; bản sau thắng, bản thua chép vào `history`.
- Hướng dữ liệu: SQLite là nguồn cho máy; client nghe Firestore (`onSnapshot`) → gọi API local để ghi SQLite; sửa local → ghi Firestore.
  Vòng lặp chặn bằng `deviceId` + so `updatedAt`.
- Quy tắc: `request.auth.uid == uid` cho mọi đường dẫn dưới `users/{uid}`; test bằng Firebase Emulator (`@firebase/rules-unit-testing`).
- Không đăng nhập → module sync không tải (dynamic import).

## File đụng tới

- `web/src/lib/sync/*.ts` (mới) — mapping, sync 2 chiều, xung đột
- `web/src/server/app.ts` — `POST /sync/apply` (ghi bản từ cloud vào SQLite có kiểm `updatedAt`), `GET /sync/changes?since=`
- `web/src/db/schema.ts` + migration mới — `updatedAt` ms + `deviceId` trên bảng đồng bộ; `sync_state`
- `firestore.rules`, `firestore.indexes.json`, `firebase.json` (mới) — quy tắc + emulator
- `web/tests/sync-*.test.ts`, `tests/rules/*.test.ts` — mapping, xung đột, quy tắc
- `README.md`, `CLAUDE.md`, `CHANGELOG.md` — file mới ở gốc

## Tasks

### Task 1: Mapping + quy tắc
- [ ] `mapping.ts` (chỉ trường người viết); `firestore.rules`; test quy tắc trên emulator (A không đọc B).

### Task 2: Đẩy lên
- [ ] Sửa local → Firestore; offline → hàng đợi của SDK. Test với Firestore emulator.

### Task 3: Kéo về + xung đột
- [ ] `onSnapshot` → `/sync/apply`; bản sau thắng, bản cũ vào `history`. Test 2 "máy" (2 deviceId) sửa cùng lúc.

### Task 4: Thử 2 máy thật
- [ ] Máy A sửa → máy B ≤ 10 giây (đo); tắt mạng sửa rồi bật. Không đăng nhập → network log không có Firestore.
- [ ] CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
