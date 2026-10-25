# Niche Radar Phase 75 — Local App 2.0 — Implementation Plan

> **For agentic workers:** chỉ làm khi bản Web **xong Version 9**. Chỉ gói thứ đã xong ở Web, không thêm tính năng. Build chỉ bằng `npm run mac`.
> Steps dùng checkbox (`- [ ]`).

**Goal:** gói phần còn lại của Version 1 (Phase 7, 9–30.2) và Version 2 (Phase 31a, 31–35) vào app Mac một lần.

**Spec:** [Phase 75 · Local App 2.0](../../app/phase-75-local-app-2.md) · **Cần trước:** Web Version 1–9 xong; Phase 74; Phase 79 nếu cần Keychain (xem dưới).

## Mục tiêu · làm · không làm

- **Xong khi:** app 1.x có dữ liệu thật → cài 2.0 → dữ liệu còn đủ (đếm từng bảng trước / sau) · trên app tra 1 niche ra đủ khối YouTube + Amazon + Maps
  (khối bị chặn báo đúng) · mở ≤ 5 giây, test xanh, bản web vẫn chạy.
- **Làm:** review 3 niche ở Web trước khi gói, collector mới vào sidecar, migration DB, key trong Keychain, nút mở thư mục job, `.dmg` mới + What's New.
- **Không làm:** tính năng mới · auto-update · Windows.

## Global Constraints

- Sidecar Node chạy đúng code `web/` (cùng build) → collector mới tự có; chỉ cần kiểm dependency native / binary đi kèm.
- `yt-dlp` (nếu Phase 31 dùng): gói binary kèm (ký trong bundle, license Unlicense) **hoặc** bỏ — mặc định bỏ vì Phase 31 chọn `youtubei.js`.
- Migration: app mở DB cũ → migrate có backup (Phase 19) → đếm bảng; test bằng bản sao DB app 1.x thật.
- Keychain cho key (YouTube, Places, AI): dùng plugin Tauri stronghold / keyring qua lệnh Rust; nếu Phase 79 chưa làm, dời phần Keychain sang Phase 79
  và giữ key trong `settings` như Web (ghi rõ trong What's New).
- "Mở thư mục job": lệnh Tauri mở `NR_DATA_DIR/jobs/` bằng Finder.
- Version app = version Web lúc gói (`version.test.ts` bắt lệch với `tauri.conf.json`).

## File đụng tới

| File | Việc |
|---|---|
| `app/src-tauri/src/*.rs` | lệnh mở thư mục job, (Keychain nếu làm ở đây) |
| `app/src-tauri/tauri.conf.json`, `app/package.json` | version, resource mới |
| `app/scripts/build-mac.sh` | gói thêm resource nếu có |
| `web/src/lib/ai/settings.ts` (nếu Keychain) | đọc key qua bridge khi chạy trong app |
| `docs/app/phase-75-local-app-2.md`, `CHANGELOG.md` | What's New, kết quả |

## Tasks

### Task 1: Review ở Web
- [ ] 3 niche thật qua Phase 31–35 ở bản Web; lỗi còn lại → sửa ở Web trước.

### Task 2: Gói + migration
- [ ] Build sidecar mới; mở bản sao DB 1.x → đếm bảng trước / sau. Test migrate.

### Task 3: Key + thư mục job
- [ ] Keychain (hoặc dời sang 79, ghi rõ); nút mở thư mục job.

### Task 4: Phát hành
- [ ] `npm run mac` (ký + notarize); mở ≤ 5 giây; tra 1 niche đủ khối. What's New, CHANGELOG (App), chip, ROADMAP. Anh đưa lên Releases.

## Tiến độ

- 2026-10-25: viết plan. Trang phase còn ghi "Phase 7, 9–28.2" (số cũ) — đúng là 7, 9–30.2 sau lần đổi số 2026-10-25.
