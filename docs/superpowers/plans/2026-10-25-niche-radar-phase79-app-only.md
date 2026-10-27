# Niche Radar Phase 35 — Phần riêng của app (license, dùng thử, bảo mật) — Implementation Plan

> **For agentic workers:** chỉ làm sau Phase 34 (bản bán đầu) và khi bản Web xong Version 10 (dùng thử + license chạy ở Web).
> Build Mac chỉ bằng `npm run mac`. Steps dùng checkbox (`- [ ]`). Không nhập key / mật khẩu thay anh, không bấm bán thật.

**Goal:** gắn phần chỉ app mới có: lưu license + ngày dùng thử an toàn, checkout mở bằng trình duyệt ngoài, CSP chặt, tìm AI có sẵn trên máy.
Viết **một lần cho cả Mac và Windows** — Phase 36 chỉ build + thử trên Windows.

**Spec:** [Phase 35 · Phần riêng của app](../../app/phase-35-app-only.md) · **Cần trước:** Phase 34, Version 10 Web (Phase 31–27.7), Backlog 15 (phiếu bảo mật),
Phase 24 (trang Setup). **Đổi 2026-10-26:** bỏ tài khoản → bỏ đăng nhập trong app + deep link.

## Mục tiêu · làm · không làm

- **Xong khi:** `.dmg` mới: CSP + quyền Tauri qua phiếu Backlog 15, key / license không còn trong file thường · mua test → license key kích hoạt trên app
  không cần tài khoản · khôi phục mua (tìm lại key bằng email) chạy · dùng thử N ngày đếm đúng, xoá app cài lại không reset được · lượt AI / tuyến AI
  hiện đúng · test xanh, screenshot app đã Read.
- **Làm:** Setup trong app, CSP + capability tối thiểu, lưu bí mật qua `keyring`, license key (activate / validate / deactivate, 2 máy), dùng thử,
  checkout + khôi phục mua mở trình duyệt ngoài, BYOK + tìm Claude Code / Codex.
- **Không làm:** tài khoản / đăng nhập / deep link (bỏ 2026-10-26) · tính năng không có ở Web · Mac App Store / IAP Apple · làm trước khi Web xong Version 10.

## Global Constraints

- **Lưu bí mật:** crate Rust `keyring` qua lệnh Tauri `secret_get/set/delete` — Mac: Keychain, Windows: Credential Manager (Phase 36 dùng lại, không
  viết lớp thứ hai). Sidecar Node nhận key qua biến môi trường lúc Tauri khởi động nó, không ghi ra đĩa. Migrate: key cũ trong `settings` → kho bí mật → xoá khỏi `settings`.
- **License:** theo luật đã chốt ở Version 10 (Lemon Squeezy License API như RAM Rescue, hoặc nhà bán đã chốt ở Phase 32): `instance_id` = id máy;
  2 máy / license; offline dùng kết quả validate gần nhất ≤ 7 ngày; chuyển máy = deactivate trong Cài đặt.
- **Dùng thử:** ngày bắt đầu lưu ở kho bí mật **và** trong DB; lấy ngày sớm hơn → xoá DB không reset được dùng thử. Hết hạn → Free, dữ liệu giữ nguyên.
- **CSP** trong `tauri.conf.json`: `default-src 'self'`, `connect-src` chỉ `self` + sidecar `127.0.0.1:<port>` + domain license / checkout; không `unsafe-eval`.
  Đo domain gọi thật bằng log network trước khi khoá.
- **Capability Tauri v2:** chỉ bật lệnh dùng thật (mở URL ngoài, hộp thoại lưu file, kho bí mật); 1 file capability, phiếu Backlog 15 ghi từng quyền.
- **Tìm AI:** danh sách chỗ cài theo hệ điều hành (Mac: `/opt/homebrew/bin`, `/usr/local/bin`, `~/.local/bin`, `~/.npm-global/bin`; Windows: Phase 36) +
  ô chọn đường dẫn ở Cài đặt. App mở từ Finder không có `PATH` của shell.

## File đụng tới

- `app/src-tauri/tauri.conf.json`, `app/src-tauri/capabilities/*.json` — CSP, quyền
- `app/src-tauri/src/secrets.rs` (mới), `license.rs` (mới), `main.rs` — kho bí mật, license, truyền key xuống sidecar
- `app/src-tauri/Cargo.toml` — `keyring`, `tauri-plugin-shell` (mở URL) / `opener`
- `web/src/lib/app-bridge.ts` (mới) — gọi lệnh Tauri khi chạy trong app, no-op ở Web
- `web/src/lib/entitlement.ts`, `web/src/lib/ai/settings.ts` — nhánh app (đọc license / key qua bridge)
- `web/src/client/SetupPage.tsx` — chế độ app: bỏ mục Node / npm, chỉ kiểm phần tuỳ chọn
- `web/src/client/SettingsPage.tsx` — mục Gói: trạng thái license, máy đang dùng, Khôi phục mua, ô đường dẫn AI
- `security/checklist.md` — mục CSP + quyền Tauri
- `docs/app/phase-35-app-only.md`, `CHANGELOG.md` (App)

## Tasks

### Task 1: Setup trong app
- [ ] `/setup` khi chạy trong app: Node + SQLite đã gói → chỉ kiểm key AI, Claude in Chrome.

### Task 2: Kho bí mật
- [ ] `secrets.rs` + bridge + migrate key cũ; grep thư mục dữ liệu không còn chuỗi key.

### Task 3: License + dùng thử
- [ ] `license.rs` (activate / validate / deactivate) ở test mode; nhập key → Pro không cần tài khoản; 2 máy; offline ≤ 7 ngày.
- [ ] Dùng thử: ngày bắt đầu ở 2 chỗ, lấy sớm hơn; test xoá DB không reset.

### Task 4: Checkout + khôi phục mua + AI
- [ ] Nút mua mở trình duyệt ngoài; Khôi phục mua = nhập email → nhà bán gửi lại key.
- [ ] BYOK trong kho bí mật; tìm Claude Code / Codex; lượt AI / tuyến hiện đúng.

### Task 5: CSP + quyền + phát hành
- [ ] Đo domain → CSP; capability tối thiểu; thử tiêm script → bị CSP chặn. Phiếu Backlog 15 phần app.
- [ ] `npm run mac`; screenshot app, Read. What's New, CHANGELOG, chip, ROADMAP. Phase 36 dùng lại toàn bộ phần này trên Windows.

## Tiến độ

- 2026-10-25: viết plan (có đăng nhập + deep link).
- 2026-10-26: viết lại — bỏ tài khoản, license + dùng thử làm ở đây, một lớp kho bí mật cho cả Mac + Windows.
