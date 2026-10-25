# Niche Radar Phase 77 — Local App 4.0 — Implementation Plan

> **For agentic workers:** chỉ làm khi bản Web **xong Version 9**. Chỉ gói Phase 41–44 đã xong ở Web. Build chỉ bằng `npm run mac`.
> Steps dùng checkbox (`- [ ]`).

**Goal:** gói kệ Google, kệ AI, cột kệ yếu, gói GEO (Phase 41–44) vào app Mac.

**Spec:** [Phase 77 · Local App 4.0](../../app/phase-77-local-app-4.md) · **Cần trước:** Phase 76, Phase 45 (đã soát ở Web).

## Mục tiêu · làm · không làm

- **Xong khi:** app 3.x có dữ liệu thật → cài 4.0 → đếm từng bảng trước / sau, không mất dòng · trên app tra kệ Google + kệ AI cho 1 niche chạy được,
  test xanh, bản Web vẫn chạy.
- **Làm:** gói collector top 10, kệ AI, điểm kệ, xuất gói GEO; engine trên máy (`codex exec` / `claude -p`) có thì dùng, không thì ẩn; migration; `.dmg` 4.0.
- **Không làm:** tính năng mới · auto-update · Windows.

## Global Constraints

- App mở từ Finder **không** có `PATH` của shell → tìm `codex` / `claude` ở các chỗ cài phổ biến (`/opt/homebrew/bin`, `/usr/local/bin`, `~/.local/bin`,
  `~/.npm-global/bin`) + cho anh chọn đường dẫn ở Cài đặt. Không thấy → engine ẩn, Gemini vẫn chạy.
- Sandbox: app Developer ID (không Mac App Store) → chạy được tiến trình con; ghi rõ trong entitlements nếu cần.
- Migration có backup + đếm bảng; version khớp.

## File đụng tới

| File | Việc |
|---|---|
| `web/src/lib/geo/engines.ts` | tìm binary theo danh sách chỗ + cài đặt đường dẫn |
| `app/src-tauri/entitlements.plist` | kiểm quyền chạy tiến trình con |
| `docs/app/phase-77-local-app-4.md`, `CHANGELOG.md` | |

## Tasks

### Task 1: Tìm engine trong app
- [ ] Danh sách chỗ + cài đặt; test: không thấy → engine "không có trên máy".

### Task 2: Gói + migration
- [ ] Build; bản sao DB 3.x → 4.0, đếm bảng.

### Task 3: Phát hành
- [ ] `npm run mac`; tra kệ Google + kệ AI 1 niche trên app (mở từ Finder, không từ Terminal). What's New, CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
