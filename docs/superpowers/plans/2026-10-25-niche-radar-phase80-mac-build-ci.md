# ShotMatic Backlog 21 — Build app Mac trên CI — Implementation Plan

> **For agentic workers:** Claude viết workflow đọc secret **theo tên**, không bao giờ đọc, in hay đổi giá trị. Anh tạo chứng chỉ và nhập GitHub Secrets.
> Steps dùng checkbox (`- [ ]`).

**Goal:** `.dmg` build trên runner macOS của GitHub, tự ký Developer ID + notarize + staple.

**Spec:** [Backlog 21 · Build app Mac trên CI](../../app/phase-backlog-21-mac-build-ci.md) · **Cần trước:** Backlog 13 (CI), Phase 17–B20 (build tay chạy ổn bằng `npm run mac`).

## Mục tiêu · làm · không làm

- **Xong khi:** `.dmg` tải từ CI mở trên máy sạch không bị Gatekeeper chặn · log CI không có giá trị secret (chỉ `***`) · không chứng chỉ / mật khẩu / key nào trong repo.
- **Làm:** `.github/workflows/build-mac.yml` (runner macOS), build Tauri + sidecar như `build-mac.sh`, keychain tạm, ký → notarize → staple, artifact `.dmg`.
- **Không làm:** GitHub Release / What's New / auto-update (Phase 37) · Mac App Store · Windows / Linux · Claude tạo chứng chỉ / nhập secret.

## Global Constraints

- Tên secret cố định (anh nhập): `MAC_CERT_P12_BASE64`, `MAC_CERT_PASSWORD`, `KEYCHAIN_PASSWORD`, `APPLE_ID`, `APPLE_TEAM_ID`, `APPLE_APP_PASSWORD`
  (hoặc `APPLE_API_KEY_P8_BASE64` + `APPLE_API_KEY_ID` + `APPLE_API_ISSUER` nếu dùng App Store Connect API key).
- Workflow gọi **đúng** `app/scripts/build-mac.sh` (thêm cờ đọc identity + notary từ env) — một đường build cho cả máy và CI; không nhân bản logic.
- Keychain tạm: `security create-keychain` → import p12 → `set-key-partition-list` → xoá ở bước `if: always()`.
- Không `set -x` trong bước có secret; không `echo` biến secret.
- Chạy khi: `workflow_dispatch` + PR chạm `app/**` (chỉ build không ký khi PR từ fork — secret không có).
- Runner: `macos-14` (Apple Silicon); build universal nếu `build-mac.sh` đang làm universal, giữ nguyên.

## File đụng tới

- `.github/workflows/build-mac.yml` (mới) — build + ký + notarize + artifact
- `app/scripts/build-mac.sh` — đọc identity / notary từ env khi có, giữ chạy tay như cũ
- `docs/quy-trinh-build.md` — mục build trên CI + danh sách secret anh cần nhập
- `CHANGELOG.md` (Repo)

## Tasks

### Task 1: Script dùng chung
- [ ] `build-mac.sh` nhận env (`MAC_SIGN_IDENTITY`, notary profile / API key); chạy tay vẫn như cũ (thử `npm run mac` trên máy).

### Task 2: Workflow không ký
- [ ] Build trên `macos-14` không ký → artifact `.app`. Đo thời gian.

### Task 3: Ký + notarize (sau khi anh nhập secret)
- [ ] Keychain tạm, ký, notarize, staple, xoá keychain; artifact `.dmg`. Kiểm log không có giá trị secret.

### Task 4: Thử máy sạch
- [ ] Tải `.dmg` từ artifact → máy / user sạch → mở không cảnh báo (`spctl -a -vv` ghi output). Quy trình build, CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
