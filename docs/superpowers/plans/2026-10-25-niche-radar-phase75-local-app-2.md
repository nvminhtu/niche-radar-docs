# Niche Radar Phase 75 — Local App 2.0 (bản bán đầu tiên) — Implementation Plan

> **For agentic workers:** chỉ làm khi bản Web **xong Version 10** (dùng thử + license chạy ở Web). Chỉ gói thứ đã xong ở Web, không thêm tính năng.
> Build chỉ bằng `npm run mac`. Steps dùng checkbox (`- [ ]`).

**Goal:** gói Version 1 (Phase 7, 9–30.2) + Version 9 (analytics) + Version 10 (dùng thử, license) vào app Mac một lần — **bản bán đầu tiên**.
Windows đi sau ở Phase 82 trên cùng code này.

**Spec:** [Phase 75 · Local App 2.0](../../app/phase-75-local-app-2.md) · **Cần trước:** Web Version 1, 9, 10 xong; Phase 74 (`.dmg` 1.x).
**Sau:** Phase 79 (license + kho bí mật cho cả Mac / Windows) → 82 (Windows) → 81 (phát hành + tự cập nhật). Version 2 (YouTube, Amazon, Maps)
vào app qua bản cập nhật Phase 81, không gói ở đây.

## Mục tiêu · làm · không làm

- **Xong khi:** app 1.x có dữ liệu thật → cài 2.0 → dữ liệu còn đủ (đếm từng bảng trước / sau) · trên app tra 1 niche ra đủ khối của Version 1
  (khối bị chặn báo đúng) · dùng thử chạy, nhập key test → Pro · mở ≤ 5 giây, test xanh, bản web vẫn chạy.
- **Làm:** review ở Web trước khi gói, collector mới vào sidecar, migration DB, nút mở thư mục job, `.dmg` mới + What's New.
- **Không làm:** tính năng mới · Version 2 · kho bí mật Keychain (Phase 79) · Windows (Phase 82) · tự cập nhật (Phase 81).

## Global Constraints

- Sidecar Node chạy đúng code `web/` (cùng build) → collector mới tự có; chỉ cần kiểm dependency native / binary đi kèm (hiện chỉ `better-sqlite3`).
- Migration: app mở DB cũ → migrate có backup (Phase 19) → đếm bảng; test bằng bản sao DB app 1.x thật.
- Key AI ở phase này vẫn lưu `settings` như Web; chuyển sang kho bí mật ở Phase 79 (ghi rõ trong What's New).
- "Mở thư mục job": lệnh Tauri mở `NR_DATA_DIR/jobs/` bằng Finder (Windows: Explorer — cùng lệnh `opener`, thử ở Phase 82).
- Đường dẫn trong code dùng `path.join` (để Phase 82 không phải sửa lại).
- Version app = version Web lúc gói (`version.test.ts` bắt lệch với `tauri.conf.json`).

## File đụng tới

- `app/src-tauri/src/main.rs` — lệnh mở thư mục job
- `app/src-tauri/tauri.conf.json`, `app/package.json` — version, resource mới
- `app/scripts/build-mac.sh` — gói thêm resource nếu có
- `docs/app/phase-75-local-app-2.md`, `CHANGELOG.md` — What's New, kết quả

## Tasks

### Task 1: Review ở Web
- [ ] 3 niche thật chạy hết luồng Version 1 + dùng thử / license (Version 10) ở bản Web; lỗi còn lại → sửa ở Web trước.

### Task 2: Gói + migration
- [ ] Build sidecar mới; mở bản sao DB 1.x → đếm bảng trước / sau. Test migrate.

### Task 3: Thư mục job
- [ ] Nút mở thư mục job trong app.

### Task 4: Phát hành
- [ ] `npm run mac` (ký + notarize); mở ≤ 5 giây; tra 1 niche đủ khối; dùng thử + key test. What's New, CHANGELOG (App), chip, ROADMAP. Anh đưa lên Releases.

## Tiến độ

- 2026-10-25: viết plan (gói Version 1 + 2).
- 2026-10-26: viết lại — gói Version 1 + 9 + 10, bản bán đầu; Version 2 đi qua bản cập nhật; Windows ở Phase 82.
