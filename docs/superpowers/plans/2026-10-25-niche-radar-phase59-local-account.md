# Niche Radar Phase 59 — Lớp tài khoản trên máy — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` xanh rồi commit.
> Steps dùng checkbox (`- [ ]`). Migration luôn backup trước, đếm dòng trước / sau.

**Goal:** mọi dữ liệu gắn một **hồ sơ** (`user_id`); nhiều hồ sơ trên một máy không thấy nhau; mỗi người xuất / xoá được toàn bộ dữ liệu của mình.

**Spec:** [Phase 59 · Lớp tài khoản trên máy](../../web/phase-59-local-account.md) · **Cần trước:** Phase 30 (hồ sơ đơn `profile.*` — nâng thành bảng), Phase 19 (backup), Phase 58.

## Mục tiêu · làm · không làm

- **Xong khi:** 2 hồ sơ trên một máy không thấy dữ liệu nhau · xoá hồ sơ → mọi bảng còn 0 dòng của hồ sơ đó · DB bản 7.x lên 8.0 → đếm từng bảng
  trước / sau, không mất dòng · `.zip` xuất mở được, đủ project + lần tra của hồ sơ đó.
- **Làm:** bảng `users`, `user_id` trên dữ liệu của người (project, run, exploration, hỏi, AI, validation…), màn hồ sơ, lọc theo hồ sơ, xuất `.zip`,
  xoá toàn bộ, migration gán hồ sơ mặc định.
- **Không làm:** đăng nhập mạng · mật khẩu hồ sơ · Pro · team / chia sẻ.

## Global Constraints

- **Cache nguồn dùng chung** (review_cache, listing_cache, iap_cache, trends_cache, keyword_cache, apps, app_snapshots…) **không** gắn `user_id` —
  là dữ liệu công khai; chỉ bảng "của người" gắn. Danh sách bảng ghi trong `web/src/db/ownership.ts`.
- Lọc ở 1 lớp: mọi hàm `lib/*` nhận `ctx.userId`; route lấy `userId` từ header `X-NR-User` (gắn sau token Phase 58); test bắt route quên lọc
  (duyệt mọi bảng "của người" sau khi gọi API bằng hồ sơ B → không có dòng của A).
- Hồ sơ đang chọn lưu `settings` + localStorage; đổi hồ sơ reload dữ liệu.
- Xoá toàn bộ: hỏi lại (gõ tên hồ sơ), backup trước, xoá thật mọi bảng "của người", đếm 0.
- Xuất `.zip`: dùng `exportProject` cho từng project + JSON các bảng còn lại của hồ sơ (`zip.ts` Phase 16).

## File đụng tới

| File | Việc |
|---|---|
| `web/src/db/schema.ts` + migration mới | `users` (id, uid, name, createdAt); `user_id` + index trên bảng "của người"; gán hồ sơ mặc định |
| `web/src/db/ownership.ts` (mới) | danh sách bảng của người / dùng chung |
| `web/src/lib/*` (projects, run-research, explore, ai, validate, ask, reports, tracking…) | nhận `userId` |
| `web/src/server/app.ts` | middleware `userId`; `GET/POST /users`, `POST /users/:id/select`, `GET /users/:id/export.zip`, `POST /users/:id/delete` |
| `web/src/client/SettingsPage.tsx` / `ProfilesPage.tsx` (mới), `AppShell.tsx` | màn hồ sơ, chọn hồ sơ ở góc |
| `web/tests/users-*.test.ts` | cách ly, xoá, migrate |

## Tasks

### Task 1: Schema + migrate
- [ ] `users` + `user_id`; migration gán mặc định; test trên bản sao DB thật: đếm từng bảng trước / sau.

### Task 2: Lọc mọi chỗ
- [ ] `lib/*` nhận `userId`; middleware; test cách ly A / B duyệt mọi bảng của người.

### Task 3: Màn hồ sơ
- [ ] Thêm / đổi tên / chọn hồ sơ, thư mục dữ liệu (dùng lại Phase 30).

### Task 4: Xuất + xoá
- [ ] `.zip` của 1 hồ sơ; xoá toàn bộ có xác nhận + backup. Test: sau xoá 0 dòng.

### Task 5: Soát
- [ ] Migrate DB thật (backup) — ghi số trước / sau. Screenshot màn hồ sơ 1340 + 375, Read. CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
