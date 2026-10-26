# Niche Radar Phase 81 — Release + auto-update — Implementation Plan

> **For agentic workers:** Claude không tự gắn tag hay bấm phát hành khi anh chưa đồng ý. Khoá ký file cập nhật do anh tạo, lưu GitHub Secrets.
> Steps dùng checkbox (`- [ ]`).

**Goal:** gắn tag là CI tự ra bản (`.dmg` + What's New lên GitHub Releases); app trên máy người dùng tự thấy bản mới, hỏi trước khi cập nhật.

**Spec:** [Phase 81 · Release + auto-update](../../app/phase-81-release-auto-update.md) · **Cần trước:** Phase 80 (build ký trên CI), Phase 57 (tag theo quy trình).

## Mục tiêu · làm · không làm

- **Xong khi:** cài `x.y.0` → ra tag `x.y.1` → app báo có bản mới và cập nhật được, dữ liệu còn đủ · từ lúc gắn tag tới lúc `.dmg` đã ký trên Releases
  không thao tác tay · What's New chỉ gồm commit `feat` / `fix` · bấm "Để sau" → app chạy bản cũ bình thường.
- **Làm:** workflow `release.yml` khi có tag `v*` (dùng lại build Phase 80), What's New từ commit, GitHub Release + `.dmg` + file cập nhật, Tauri updater, chữ ký file cập nhật.
- **Không làm:** Claude tự tag / phát hành · cập nhật ngầm không hỏi · Windows / Linux, Mac App Store · deploy bản Web.

## Global Constraints

- Release ở repo nào: `.dmg` hiện để ở GitHub Releases (bản 0.9.0) — giữ đúng repo đó; repo code private thì endpoint updater phải là
  repo / nơi **public** (Releases của repo public riêng hoặc file `latest.json` trên GitHub Pages) — chốt lúc làm, ghi lý do.
- Tauri updater v2: `plugins.updater.pubkey` trong `tauri.conf.json` (public key, commit được), private key + password ở secret
  `TAURI_SIGNING_PRIVATE_KEY`, `TAURI_SIGNING_PRIVATE_KEY_PASSWORD` (anh tạo bằng `tauri signer generate`).
- `latest.json` sinh trong workflow: version, notes (What's New), `platforms.darwin-*` url + signature.
- What's New: commit `feat` / `fix` kể từ tag trước (`git log <prev>..<tag> --grep`), nhóm theo loại, tiếng Việt như CHANGELOG.
- App kiểm lúc mở, hỏi bằng hộp thoại có "Cập nhật" / "Để sau"; cập nhật xong → migrate DB có backup (Phase 19) như mọi lần nâng.
- Tag khớp version (`version.test.ts` đã bắt lệch `package.json` / `tauri.conf.json`); CI fail nếu lệch.

## File đụng tới

- `.github/workflows/release.yml` (mới) — tag `v*` → build (gọi lại job Phase 80) → What's New → Release + `latest.json`
- `scripts/whats-new.ts` (mới) — sinh What's New từ commit
- `app/src-tauri/tauri.conf.json`, `Cargo.toml`, `src/*.rs` — plugin updater, pubkey, endpoint
- `web/src/lib/app-bridge.ts`, `components/UpdatePrompt.tsx` (mới) — hộp thoại cập nhật (chỉ trong app)
- `docs/quy-trinh-build.md`, `CHANGELOG.md` — mục release + secret cần nhập

## Tasks

### Task 1: What's New
- [ ] `whats-new.ts` + test trên lịch sử giả (chỉ `feat` / `fix`).

### Task 2: Release workflow
- [ ] `release.yml` dùng job build Phase 80; tạo Release + `.dmg` + `latest.json`. Thử với tag nháp trên nhánh thử (anh đồng ý), xoá sau.

### Task 3: Updater trong app
- [ ] Plugin updater, pubkey, endpoint; hộp thoại hỏi; "Để sau" không chặn. Test file cập nhật sai chữ ký → bị từ chối.

### Task 4: Vòng thật
- [ ] Cài `x.y.0` → anh tag `x.y.1` → app báo + cập nhật; đếm bảng DB trước / sau. Ghi bằng chứng, quy trình build, CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
