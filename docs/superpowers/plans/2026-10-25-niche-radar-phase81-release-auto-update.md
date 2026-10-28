# ShotMatic Phase 37 — Release + auto-update (Mac + Windows) — Implementation Plan

> **For agentic workers:** Claude không tự gắn tag hay bấm phát hành khi anh chưa đồng ý. Khoá ký file cập nhật do anh tạo, lưu trên máy anh
> (không vào repo). Steps dùng checkbox (`- [ ]`).

**Goal:** một lệnh trên máy ra bản cho **cả Mac và Windows**: `.dmg` + `.exe` + What's New lên **GitHub Releases public**; app trên cả hai hệ điều
hành tự thấy bản mới và hỏi trước khi cập nhật.

**Spec:** [Phase 37 · Release + auto-update](../../app/phase-37-release-auto-update.md) · **Cần trước:** Phase 34 + 35 (app Mac bán được), Phase 36
(`npm run win` ra `.exe`). **Đổi 2026-10-26:** không CI — Backlog 21 không làm, build + ký trên máy (học Wow Keywords: ra bản dày, ghi chú lời thường).

## Mục tiêu · làm · không làm

- **Xong khi:** cài `x.y.0` trên Mac **và** trên Windows → ra `x.y.1` → cả hai app báo có bản mới, cập nhật được, dữ liệu còn đủ · từ lúc chạy
  `npm run release` tới lúc `.dmg` + `.exe` có trên Releases không thao tác tay nào khác · What's New chỉ gồm commit `feat` / `fix`, lời thường ·
  bấm "Để sau" → app chạy bản cũ bình thường.
- **Làm:** `npm run release` (build Mac → build Windows → What's New → ký file cập nhật → `latest.json` → GitHub Release), Tauri updater trên 2 nền tảng,
  hộp thoại hỏi cập nhật.
- **Không làm:** Claude tự tag / phát hành · cập nhật ngầm · Linux, Mac App Store, Microsoft Store · deploy bản Web · CI.

## Global Constraints

- **Repo phát hành public riêng** (kiểu `Kronop/wowkeywords-releases` của Wow Keywords): code vẫn ở repo private, repo public chỉ chứa Release —
  host 0 đồng, có số tải công khai. Tên repo anh chốt (vd. `nvminhtu/niche-radar-releases`); anh tạo repo, Claude dùng `gh release create`.
- **Tauri updater v2:** `plugins.updater.pubkey` trong `tauri.conf.json` (commit được); private key ở `~/.tauri/niche-radar.key` trên máy anh
  (anh tạo bằng `npx tauri signer generate`), mật khẩu đọc từ biến môi trường lúc build — không vào repo, không in ra log.
- **Endpoint:** `https://github.com/<repo-public>/releases/latest/download/latest.json`; `latest.json` có `platforms.darwin-aarch64` (file `.app.tar.gz`)
  và `platforms.windows-x86_64` (file `-setup.exe` hoặc `.nsis.zip` theo bản Tauri lúc làm) kèm chữ ký từng file.
- **Mac:** bản cập nhật vẫn ký Developer ID + notarize (dùng lại `build-mac.sh`). **Windows:** chưa ký Authenticode (Beta) — chữ ký updater vẫn bắt buộc.
- **What's New:** commit `feat` / `fix` kể từ tag trước, nhóm theo loại, tiếng Việt như CHANGELOG; anh sửa được trước khi đăng (script dừng hỏi).
- **Cập nhật xong** → migrate DB có backup (Phase 39) như mọi lần nâng. Tag khớp version (`version.test.ts`).

## File đụng tới

- `scripts/release.sh` (mới) + `package.json` gốc `release` — gọi `npm run mac`, `npm run win`, sinh What's New, ký, `latest.json`, `gh release create`
- `scripts/whats-new.ts` (mới) — sinh What's New từ commit
- `scripts/latest-json.ts` (mới) — dựng `latest.json` 2 nền tảng
- `app/src-tauri/tauri.conf.json`, `Cargo.toml` (`tauri-plugin-updater`), `src/main.rs` — plugin updater, pubkey, endpoint, `createUpdaterArtifacts`
- `web/src/lib/app-bridge.ts`, `web/src/components/UpdatePrompt.tsx` (mới) — hộp thoại cập nhật (chỉ trong app)
- `docs/quy-trinh-build.md`, `app/README.md`, `CLAUDE.md`, `CHANGELOG.md` — lệnh `npm run release`, khoá ký nằm đâu

## Tasks

### Task 1: What's New + latest.json
- [ ] `whats-new.ts` + test lịch sử giả (chỉ `feat` / `fix`); `latest-json.ts` + test (2 nền tảng, thiếu file → lỗi rõ).

### Task 2: Updater trong app
- [ ] Plugin updater + pubkey + endpoint; `UpdatePrompt` (Cập nhật / Để sau). Test: file sai chữ ký → bị từ chối.

### Task 3: Lệnh release
- [ ] `release.sh`: build 2 nền tảng → ký file cập nhật → `latest.json` → dừng cho anh duyệt What's New → anh đồng ý → `gh release create` đính `.dmg`, `.exe`,
      file cập nhật, `latest.json`.

### Task 4: Vòng thật trên 2 máy
- [ ] Cài `x.y.0` trên Mac + Windows → anh đồng ý ra `x.y.1` → cả hai báo + cập nhật; đếm bảng DB trước / sau mỗi máy. "Để sau" không chặn.
- [ ] Trang tải trỏ link `releases/latest`. Quy trình build, CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan (bản CI, chỉ Mac).
- 2026-10-26: viết lại — không CI, phát hành từ máy, cả Mac + Windows, repo Releases public riêng.
