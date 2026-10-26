# Niche Radar Phase 79 — Phần riêng của app Mac (bảo mật, đăng nhập, Pro) — Implementation Plan

> **For agentic workers:** chỉ làm khi bản Web **xong Version 9** và app đã gói đủ (Phase 74–77). 3 dòng Pro (license, khôi phục mua, BYOK + lượt AI)
> làm khi tới Version 10, sau khi Web xong phần Pro. Build chỉ bằng `npm run mac`. Steps dùng checkbox (`- [ ]`).

**Goal:** làm mọi việc **chỉ app Mac mới có** mà các phase Web đã tách ra.

**Spec:** [Phase 79 · Phần riêng của app Mac](../../app/phase-79-app-only.md) · **Cần trước:** Phase 30.1, 58, 62 (cho phần A); Phase 67, 68, 69 (cho phần B).

## Mục tiêu · làm · không làm

- **Xong khi:** `.dmg` mới: CSP + quyền Tauri qua phiếu Phase 58, key không còn trong file thường · đăng nhập 3 cách trên app, deep link quay lại đúng app ·
  mua test → license key kích hoạt trên app không đăng nhập · khôi phục mua chạy · lượt AI hiện đúng · test xanh, screenshot app đã Read.
- **Làm:** phần A (sau Version 9): Setup trong app, CSP + capability Tauri tối thiểu, key trong Keychain, đăng nhập qua trình duyệt + deep link.
  Phần B (khi tới Version 10): license key kiểu RAM Rescue + checkout mở từ app, Khôi phục mua, BYOK trong Keychain + lượt AI còn lại.
- **Không làm:** tính năng không có ở Web · Mac App Store / IAP Apple · làm trước khi Web xong Version 9.

## Global Constraints

- **CSP** trong `tauri.conf.json`: `default-src 'self'; connect-src 'self' http://127.0.0.1:<port> https://*.googleapis.com https://*.firebaseio.com …`
  (liệt kê đúng domain đang gọi, đo bằng log network trước); không `unsafe-eval`.
- **Capability Tauri v2**: chỉ bật lệnh dùng thật (shell open URL, dialog save, deep link, keychain); file capability 1 chỗ, phiếu Phase 58 ghi từng quyền.
- **Keychain**: plugin keyring (Rust crate `keyring`) qua lệnh `secret_get/set/delete`; server sidecar đọc key qua biến môi trường do Tauri nạp lúc
  khởi động sidecar (không ghi ra đĩa). Migrate: key cũ trong `settings` → Keychain → xoá khỏi `settings`.
- **Deep link**: scheme `nicheradar://auth?…`; luồng đăng nhập mở trình duyệt mặc định tới trang đăng nhập (host trên Firebase Hosting / landing),
  trang đó chuyển `nicheradar://` kèm token một lần → app đổi lấy phiên Firebase (`signInWithCustomToken` hoặc credential). Kiểm `state` chống giả mạo.
- **License key**: dùng lại mẫu Lemon Squeezy License API của RAM Rescue (activate / validate / deactivate theo `instance_id` = id máy);
  key lưu Keychain; offline → dùng kết quả validate gần nhất ≤ 7 ngày.
- Không tự nhập key / mật khẩu thay anh; không bấm phát hành.

## File đụng tới

- `app/src-tauri/tauri.conf.json`, `capabilities/*.json` — CSP, quyền, deep link scheme
- `app/src-tauri/src/secrets.rs`, `deeplink.rs`, `license.rs` (mới) — Keychain, deep link, license
- `web/src/lib/app-bridge.ts` (mới) — gọi lệnh Tauri khi chạy trong app, no-op ở Web
- `web/src/client/SetupPage.tsx` — chế độ app: bỏ mục Node / npm, chỉ kiểm tuỳ chọn
- `web/src/lib/auth-client.ts`, `entitlement.ts`, `ai/settings.ts` — nhánh app
- `security/checklist.md` — mục CSP + quyền Tauri
- `docs/app/phase-79-app-only.md`, `CHANGELOG.md`

## Tasks

### Phần A — sau Version 9

#### Task 1: Setup trong app
- [ ] `/setup` khi `NR_APP=1`: Node + SQLite đã gói → chỉ kiểm key AI, Ollama, Claude in Chrome.

#### Task 2: CSP + quyền
- [ ] Đo domain gọi thật → CSP; capability tối thiểu; phiếu Phase 58 điền phần app. Thử tiêm script → bị CSP chặn.

#### Task 3: Keychain
- [ ] `secrets.rs` + migrate key cũ; grep thư mục dữ liệu không còn chuỗi key.

#### Task 4: Đăng nhập + deep link
- [ ] Trang đăng nhập web + `nicheradar://`; 3 cách đăng nhập trên app; test `state` sai bị từ chối.

### Phần B — khi tới Version 10

#### Task 5: License + checkout
- [ ] `license.rs` theo mẫu RAM Rescue; checkout mở trình duyệt; kích hoạt không cần đăng nhập. Test mode.

#### Task 6: Khôi phục mua + BYOK + lượt AI
- [ ] Nút Khôi phục mua; BYOK trong Keychain; `AiQuota` trong app.

### Task 7: Phát hành
- [ ] `npm run mac`; screenshot app, Read. What's New, CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
