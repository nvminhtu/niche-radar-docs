# ShotMatic Backlog 20 — App Mac nhẹ — Implementation Plan

> **For agentic workers:** đo trước, sửa đúng chỗ đo ra nặng. Build chỉ bằng `npm run mac`. Steps dùng checkbox (`- [ ]`).

**Goal:** app Mac mở nhanh, ít RAM khi rảnh, file cài nhỏ hơn; đo lại cả Version 5 so với mốc.

**Spec:** [Backlog 20 · App Mac nhẹ](../../app/phase-backlog-20-light-mac-app.md) · **Cần trước:** Backlog 19, Backlog 05 (`bench/baseline.json`).

## Mục tiêu · làm · không làm

- **Xong khi:** app mở ≤ 3 giây · RAM rảnh và dung lượng `.dmg` nhỏ hơn mốc · test xanh, bản Web vẫn chạy · cả bảng mốc: mọi chỉ số bằng hoặc tốt hơn,
  không chỉ số nào tệ đi quá 10%.
- **Làm:** đo trên app đã cài, sidecar bỏ dependency dev, server tự ngủ khi rảnh, build lại + đo dung lượng, `npm run bench` lại.
- **Không làm:** viết lại collector bằng Rust (chỉ ghi pending nếu Node là nút cổ chai) · auto-update · Windows · tính năng mới.

## Global Constraints

- Mốc app ghi trước khi sửa: thời gian mở (từ `open -a` tới khi API trả `/api/research` lần đầu), RSS nghỉ của app + sidecar (sau 2 phút không thao tác),
  dung lượng `.app` + `.dmg`. Lệnh đo `app/scripts/measure.sh` (mới).
- Sidecar gọn: bundle server bằng `esbuild` (1 file + `better-sqlite3` native) thay vì chép `node_modules` đầy đủ; danh sách external ghi trong script.
- Server tự ngủ: không có request trong N phút (mặc định 10) và không job đang chạy → thoát tiến trình; Tauri khởi động lại sidecar khi UI gọi API
  (lệnh Rust `ensure_server`), UI hiện "đang mở lại…" ≤ 1 giây. Job theo lịch (Phase 42) giữ server thức.
- Đo lại Version 5: `npm run bench` + `bench:compare` 3 niche chuẩn, ghi cột "Backlog 20" cạnh mốc.

## File đụng tới

- `app/scripts/measure.sh` (mới) — đo mở / RAM / dung lượng
- `app/scripts/build-mac.sh` — bundle sidecar bằng esbuild
- `app/src-tauri/src/*.rs` — `ensure_server`, khởi động lại sidecar
- `web/src/server/index.ts` — hẹn giờ ngủ khi rảnh (chỉ bật khi `NR_APP=1`)
- `web/src/client/page-cache.ts` / fetch chung — chờ server dậy khi gọi lỗi kết nối
- `docs/app/phase-backlog-20-light-mac-app.md`, `bench/` — số trước / sau

## Tasks

### Task 1: Mốc app
- [ ] `measure.sh` trên app đã cài (build hiện tại) → bảng mốc vào trang phase.

### Task 2: Sidecar gọn
- [ ] esbuild bundle; app vẫn tra được 1 niche; đo dung lượng.

### Task 3: Server tự ngủ
- [ ] Hẹn giờ ngủ + `ensure_server`; test: rảnh 10 phút → thoát; bấm tra → dậy, chạy đúng. Job theo lịch không bị ngủ.

### Task 4: Đo lại
- [ ] `measure.sh` + `npm run bench`; so mốc, không chỉ số nào tệ > 10%. `npm run mac`, What's New, CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan. Mốc cũ Phase 17: mở ~0,14 giây tới server sẵn sàng · RAM nghỉ ≈ 200 MB · `.dmg` 45 MB (app 119 MB).
