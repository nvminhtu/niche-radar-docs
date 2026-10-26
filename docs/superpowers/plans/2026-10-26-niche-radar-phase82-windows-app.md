# Niche Radar Phase 35 — App Windows (Beta) — Implementation Plan

> **For agentic workers:** chỉ làm sau Phase 34 (license + dùng thử đã chạy trên Mac). Cùng một app Tauri + cùng `web/` — **không** viết UI
> riêng cho Windows. Steps dùng checkbox (`- [ ]`). Không mua chứng chỉ ký, không nộp Microsoft Store, không nhập key / mật khẩu thay anh.

**Goal:** thêm khách ngoài người dùng Mac: cùng app build cho **Windows 11 x64**, ra **Beta chưa ký** trước, dùng thử + license chạy như Mac.

**Spec:** [Phase 35 · App Windows (Beta)](../../app/phase-35-windows-app.md) · **Cần trước:** Phase 33 (bản bán đầu Mac), Phase 34 (license, dùng thử,
lưu key theo hệ điều hành). **Sau:** Phase 36 phát hành cả `.dmg` + `.exe` và tự cập nhật trên cả hai.

## Mục tiêu · làm · không làm

- **Xong khi:** cài `.exe` trên máy Windows 11 sạch → mở được, dùng thử chạy, tra 1 niche ra số · nhập key test → Pro, máy Windows tính là
  1 trong 2 máy của license · gỡ cài đặt → không còn server chạy nền · screenshot app trên Windows đã Read.
- **Làm:** lệnh `npm run win` ra `Niche-Radar-<version>-win-x64-setup.exe` (NSIS), sidecar Node Windows, đường dẫn dữ liệu `%APPDATA%`,
  lưu key + ngày dùng thử bằng Windows Credential Manager, tìm Claude Code / Codex / Ollama trên Windows, nút tải trên trang tải.
- **Không làm:** mua chứng chỉ ký Windows trước khi có đơn · Microsoft Store · Windows 10 / ARM / 32-bit · tính năng chỉ có trên Windows.

## Đo trước khi code (Task 0)

| Đo gì | Cách | Ghi vào |
|---|---|---|
| Build Windows được từ máy Mac không | Tauri v2 hỗ trợ build NSIS chéo từ macOS bằng `cargo-xwin` (tài liệu Tauri "Windows Installer → Build on Linux and macOS", ghi trạng thái lúc đọc); thử `npx tauri build --runner cargo-xwin --target x86_64-pc-windows-msvc` | bảng này + ngày |
| `better-sqlite3` có prebuild `win32-x64` không | xem `node_modules/better-sqlite3/prebuilds/` hoặc tải prebuild đúng phiên bản Node ABI | bảng này |
| Node Windows chính chủ | `node-v<ver>-win-x64.zip` từ nodejs.org, cùng phiên bản Node đang gói cho Mac | bảng này |
| Máy Windows để thử | máy thật / máy ảo (UTM, Parallels) của anh; không có → hỏi anh trước khi dùng runner GitHub `windows-latest` | bảng này |

Build chéo từ Mac trượt → đường dự phòng: build trên máy Windows / máy ảo bằng cùng script (PowerShell bản tương đương), hoặc 1 job
`windows-latest` chạy tay (`workflow_dispatch`) — không dựng CI đầy đủ (Backlog 21 không làm).

## Global Constraints

- **Một code:** khác biệt hệ điều hành chỉ ở `app/` (script build, cấu hình bundle, lệnh Rust lưu key) và vài chỗ `web/src/lib/paths.ts` /
  tìm binary — mỗi chỗ rẽ nhánh bằng `process.platform`, có test cho cả hai nhánh.
- **Dữ liệu:** `%APPDATA%\niche-radar\` (Tauri `app_data_dir`), truyền xuống sidecar qua `NR_DATA_DIR` như Mac. Backup / restore (Phase 38) dùng
  `path.join`, không nối chuỗi `/`.
- **Lưu key + ngày dùng thử:** crate `keyring` (Rust) — trên Mac là Keychain, trên Windows là Credential Manager — cùng lệnh
  `secret_get/set/delete` của Phase 34, không viết lớp thứ hai.
- **Sidecar không chạy nền khi tắt app:** Tauri giết tiến trình Node lúc cửa sổ đóng (`RunEvent::Exit`); NSIS uninstall chạy `taskkill` tiến trình
  `node.exe` trong thư mục cài trước khi xoá file.
- **Tìm AI:** Claude Code / Codex / Ollama trên Windows — `where.exe`, `%LOCALAPPDATA%\Programs\`, `%APPDATA%\npm\`; Ollama gọi `http://127.0.0.1:11434`
  như Mac. Không thấy → ẩn tuyến đó, như Backlog 19 đã ghi cho Mac.
- **Chưa ký:** SmartScreen hiện "Windows protected your PC" → trang tải ghi rõ "More info → Run anyway" (học Wow Keywords:
  "unsigned, so Windows may show a security warning"). Tên file + version giữ ổn định để Phase 36 dùng làm link tải.
- **Version** khớp `web/package.json` + `tauri.conf.json` (`version.test.ts` đã bắt lệch).

## File đụng tới

- `app/scripts/build-win.sh` (mới) — build UI + server bundle (dùng lại bước 1–2 của `build-mac.sh`, tách thành hàm chung), chép `node.exe` +
  prebuild `better-sqlite3` win32-x64, `tauri build --bundles nsis --target x86_64-pc-windows-msvc`, ra `app/dist/Niche-Radar-<v>-win-x64-setup.exe`
- `app/scripts/common.sh` (mới) — phần chung Mac / Windows tách từ `build-mac.sh`
- `package.json` gốc — lệnh `win`
- `app/src-tauri/tauri.conf.json` — `bundle.windows` (NSIS, `installMode: currentUser`, icon `.ico` đã có), resources theo hệ điều hành
- `app/src-tauri/src/main.rs` (+ `secrets.rs` của Phase 34) — tắt sidecar khi thoát, `keyring` chạy cả 2 nền tảng
- `app/src-tauri/windows/hooks.nsh` (mới) — `taskkill` lúc gỡ cài
- `web/src/lib/paths.ts`, `web/src/lib/geo/engines.ts` / chỗ tìm Claude Code · Codex · Ollama — nhánh Windows
- `web/tests/paths-win.test.ts` (mới) — giả `process.platform = 'win32'`
- trang tải (demo site Phase 49 / landing) — nút "Windows 11 · x64 · Beta" + cảnh báo SmartScreen
- `app/README.md`, `README.md`, `CLAUDE.md`, `docs/cach-dung.md`, `CHANGELOG.md` (App) — lệnh `npm run win` (luật repo khi thêm lệnh)

## Tasks

### Task 0: Đo đường build
- [ ] Bảng đo ở trên. Chọn: build chéo từ Mac / máy ảo Windows / job tay — ghi lý do vào trang phase.

### Task 1: Tách phần chung + build Windows
- [ ] `common.sh` (UI + server bundle + smoke test server); `build-mac.sh` gọi lại, `npm run mac` vẫn ra `.dmg` như cũ (thử).
- [ ] `build-win.sh` + `npm run win` → `.exe` NSIS. Kiểm file có `node.exe`, `server.cjs`, prebuild win32.

### Task 2: Đường dẫn + tắt sidecar
- [ ] `paths.ts` + test nhánh Windows; Tauri giết sidecar khi thoát; hook gỡ cài.
- [ ] Trên Windows: mở app → tra 1 niche → đóng app → Task Manager không còn `node.exe` của app.

### Task 3: License + dùng thử trên Windows
- [ ] `keyring` cho Credential Manager (dùng chung lệnh Phase 34). Nhập key test → Pro; máy Windows hiện trong danh sách 2 máy của license.
- [ ] Hết dùng thử (giả lập ngày) → về Free, dữ liệu còn đủ.

### Task 4: Tìm AI trên Windows
- [ ] Đường tìm Claude Code / Codex / Ollama; không có → ẩn tuyến, phần không AI vẫn chạy.

### Task 5: Trang tải + soát
- [ ] Nút "Windows 11 · x64 · Beta" cạnh nút Mac, ghi cách vượt SmartScreen.
- [ ] Máy Windows 11 sạch: cài → dùng thử → tra niche → nhập key → gỡ cài. Screenshot từng bước, Read. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-26: viết plan (anh chốt bán cả app Mac + Windows).
