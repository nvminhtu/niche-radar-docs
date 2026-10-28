# ShotMatic Backlog 03 — Firebase Auth — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` xanh rồi commit.
> Steps dùng checkbox (`- [ ]`). Anh tạo project Firebase / Apple Developer cấu hình; Claude nối code, không nhập thanh toán.

**Goal:** đăng nhập thật (Google · Apple · email link) để Backlog 04 mang project sang máy khác. Không đăng nhập → app vẫn đủ như cũ.

**Spec:** [Backlog 03 · Firebase Auth](../../web/phase-backlog-03-firebase-auth.md) · **Cần trước:** Backlog 02 (bảng `users`), Backlog 15 (token API).

## Mục tiêu · làm · không làm

- **Xong khi:** đăng nhập / đăng xuất được cả 3 cách trên bản Web · tắt mạng vẫn mở project trên máy · lần đầu đăng nhập: đếm project trước / sau
  gắn hồ sơ, không mất dòng · không đăng nhập: mọi tính năng như 8.0 · `npm run check` xanh.
- **Làm:** client Firebase Auth, route kiểm ID token, gắn hồ sơ ↔ tài khoản, đăng xuất giữ dữ liệu máy.
- **Không làm:** sync (Backlog 04) · analytics (64) · xoá tài khoản cloud (65) · tự làm mật khẩu / server riêng.

## Global Constraints

- Tên file chốt: client `web/src/lib/auth-client.ts` (Firebase JS SDK modular, chỉ import `firebase/auth`), server `web/src/server/auth.ts`
  (kiểm ID token bằng `firebase-admin` **hoặc** kiểm JWT bằng khoá công khai Google `securetoken` — chọn lúc làm, ưu tiên không cần service account trên máy người dùng).
- Config Firebase (apiKey web, authDomain…) là public, để `web/.env` (`VITE_FIREBASE_*`); không có → nút đăng nhập ẩn, app chạy local thuần.
- `users` thêm `firebaseUid` (unique, null được). Gắn: hồ sơ đang chọn chưa có `firebaseUid` → gắn; đã có hồ sơ khác gắn uid này → hỏi chọn.
- Đăng xuất chỉ xoá phiên Firebase trên client; DB máy giữ nguyên.
- Email link: domain chuyển về là `localhost` (bản Web) — thêm vào Authorized domains (anh làm).
- Apple Sign-In trên web cần Service ID + domain xác minh — anh làm ở Apple Developer; chưa xong thì nút Apple xám "chưa cấu hình".

## File đụng tới

- `web/src/lib/auth-client.ts` (mới) — 3 cách đăng nhập, theo dõi phiên, lấy ID token
- `web/src/server/auth.ts` (mới) — kiểm token, `POST /auth/link` gắn hồ sơ, `POST /auth/logout`
- `web/src/db/schema.ts` + migration mới — `users.firebaseUid`
- `web/src/client/SettingsPage.tsx` / `ProfilesPage.tsx`, `AppShell.tsx` — nút đăng nhập, trạng thái tài khoản
- `docs/cach-dung.md` — bước anh tạo Firebase project + bật 3 provider
- `web/tests/auth-*.test.ts` — token giả, gắn hồ sơ

## Tasks

### Task 1: Cấu hình (anh)
- [ ] Anh tạo project Firebase, bật Google + Email link (+ Apple khi có Service ID), dán config vào `web/.env`.

### Task 2: Client
- [ ] `auth-client.ts`; nút đăng nhập 3 cách; không config → ẩn. Test render khi có / không config.

### Task 3: Server + gắn hồ sơ
- [ ] Kiểm token, migration `firebaseUid`, gắn hồ sơ. Test: token sai 401; gắn lần đầu không mất project (đếm).

### Task 4: Offline + đăng xuất
- [ ] Tắt mạng mở project bình thường; đăng xuất giữ dữ liệu. E2E (Backlog 09) chạy không config → như 8.0.

### Task 5: Soát
- [ ] Đăng nhập thật 3 cách; screenshot 1340 + 375, Read. Cách dùng, CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
