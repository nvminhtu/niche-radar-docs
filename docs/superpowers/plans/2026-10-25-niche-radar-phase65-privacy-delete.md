# ShotMatic Phase 30 — Riêng tư + xoá tài khoản — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` xanh rồi commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** người dùng xoá được tài khoản (cả cloud), tải được dữ liệu cloud, đọc trang Privacy ghi đúng thứ app gửi đi — điều kiện để bán ở Version 10.

**Spec:** [Phase 30 · Riêng tư + xoá tài khoản](../../web/phase-30-privacy-delete.md) · **Cần trước:** Backlog 03, B04, 64.

## Mục tiêu · làm · không làm

- **Xong khi:** xoá tài khoản → Firestore còn 0 tài liệu của người đó · đăng nhập lại tài khoản vừa xoá → không dữ liệu cũ · Privacy khớp danh sách
  sự kiện Phase 29 (đối chiếu từng dòng) · chọn "giữ dữ liệu máy" → project máy vẫn mở · test quy tắc xanh.
- **Làm:** xoá tài khoản (Auth + Firestore, hỏi xoá dữ liệu máy), xuất dữ liệu cloud, trang Privacy, rà lại quy tắc.
- **Không làm:** thanh toán / Pro · giữ bản sao dữ liệu đã xoá.

## Global Constraints

- Xoá cloud phía client (người dùng đã đăng nhập): xoá đệ quy `users/{uid}/**` (batch ≤ 500) rồi `deleteUser()`; cần đăng nhập gần đây →
  yêu cầu đăng nhập lại trước khi xoá. Không cần server admin.
- Thứ tự: xuất (tuỳ chọn) → xác nhận (gõ email) → xoá Firestore → xoá Auth → hỏi "xoá dữ liệu trên máy?" → có thì dùng xoá hồ sơ Phase 59.
- Privacy: trang tĩnh `docs/privacy.md` (public, dùng cho store / landing) + link trong app. Danh sách sự kiện **sinh từ** union trong `telemetry.ts`
  (script `scripts/privacy-events.ts` in bảng; test so bảng trong `privacy.md` với union — lệch là đỏ).
- Quy tắc Firestore rà lại + thêm test "đã xoá → không còn đọc được".

## File đụng tới

- `web/src/lib/sync/account-delete.ts` (mới) — xoá đệ quy + `deleteUser`
- `web/src/lib/sync/cloud-export.ts` (mới) — tải mọi tài liệu `users/{uid}` ra `.json`
- `web/src/client/SettingsPage.tsx` — mục Tài khoản: Xuất · Xoá (có bước xác nhận)
- `docs/privacy.md` (mới) + `mkdocs.yml` + link trong app — trang Privacy
- `scripts/privacy-events.ts`, `web/tests/privacy.test.ts` — bảng sự kiện khớp code
- `tests/rules/*.test.ts` — rà quy tắc

## Tasks

### Task 1: Xuất cloud
- [ ] `cloud-export.ts` + nút; test trên emulator.

### Task 2: Xoá tài khoản
- [ ] `account-delete.ts`, luồng xác nhận, đăng nhập lại; test emulator: sau xoá 0 tài liệu; đăng nhập lại → rỗng.

### Task 3: Privacy
- [ ] `docs/privacy.md` (tài khoản, Firestore, 7 sự kiện, báo lỗi, không bán dữ liệu); test khớp sự kiện; link trong app. `docs:build` xanh.

### Task 4: Soát
- [ ] Chạy thật 1 tài khoản thử; "giữ dữ liệu máy" mở project được. Screenshot 1340 + 375, Read. CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
