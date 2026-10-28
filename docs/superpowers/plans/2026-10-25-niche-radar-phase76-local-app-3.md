# ShotMatic Backlog 18 — Local App 3.0 — Implementation Plan

> **For agentic workers:** chỉ làm khi bản Web **xong Version 9**. Chỉ gói Phase 56–57 đã xong ở Web. Build chỉ bằng `npm run mac`.
> Steps dùng checkbox (`- [ ]`).

**Goal:** gói So sánh đối thủ, Hỏi dữ liệu, Báo cáo so sánh (Phase 56–57) vào app Mac.

**Spec:** [Backlog 18 · Local App 3.0](../../app/phase-backlog-18-local-app-3.md) · **Cần trước:** Phase 34, Phase 58 (đã soát ở Web).

## Mục tiêu · làm · không làm

- **Xong khi:** app 2.x có dữ liệu thật → cài 3.0 → đếm từng bảng trước / sau, không mất dòng · trên app so 3 niche + hỏi 1 câu + xuất 1 báo cáo chạy được,
  test xanh, bản Web vẫn chạy.
- **Làm:** gói màn so sánh, ô hỏi, báo cáo; migration bảng mới (bộ so sánh, `ask_history`, `reports`); `.dmg` 3.0 + What's New.
- **Không làm:** tính năng mới · auto-update (Phase 37) · Windows.

## Global Constraints

- Như Phase 34: sidecar chạy code `web/`; migration có backup + đếm bảng; version khớp.
- Xuất báo cáo / evidence pack trong app: lưu bằng hộp thoại Lưu của macOS (Tauri `dialog.save`) thay vì tải trình duyệt.
- AI trong app dùng key theo Phase 34 / 79.

## File đụng tới

- `app/src-tauri/*` — `dialog.save` cho file xuất (nếu chưa có)
- `web/src/lib/download.ts` (mới nếu chưa có) — 1 hàm tải file: trình duyệt → `<a download>`, app → lệnh Tauri
- `docs/app/phase-backlog-18-local-app-3.md`, `CHANGELOG.md`

## Tasks

### Task 1: Gói + migration
- [ ] Build; bản sao DB 2.x → 3.0, đếm bảng.

### Task 2: Xuất file trong app
- [ ] `download.ts` dùng chung; báo cáo / evidence pack lưu được qua hộp thoại.

### Task 3: Phát hành
- [ ] `npm run mac`; so 3 niche + hỏi + xuất trên app. What's New, CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
