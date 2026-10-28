# ShotMatic Backlog 17 — Review bảo mật + bản 8.0 — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự. Steps dùng checkbox (`- [ ]`). Claude không tự gắn tag 8.0 khi anh chưa đồng ý.

**Goal:** tự **tấn công thử** theo phiếu Backlog 15 trên bản build, sửa chỗ lọt, rồi ra bản Web 8.0 qua CI.

**Spec:** [Backlog 17 · Review bảo mật + 8.0](../../web/phase-backlog-17-security-review-8.md) · **Cần trước:** Backlog 15, B02, B16, B13, 57.

## Mục tiêu · làm · không làm

- **Xong khi:** mọi lần thử bị chặn, có ảnh / log bằng chứng · bản 8.0 cài đè 7.x không mất dữ liệu (đếm từng bảng trước / sau).
  Dòng "7.x tự nhận 8.0 qua auto-update" chỉ áp dụng khi App Mac đã có auto-update (Phase 37 — làm sau Version 9); trước đó ghi "chưa áp dụng".
- **Làm:** 3 nhóm thử (trang lạ gọi API · review có `<script>` · key lọt log) + mọi mục phiếu Backlog 15, bằng chứng, sửa, ra bản 8.0.
- **Không làm:** pentest thuê ngoài · tính năng mới.

## Global Constraints

- Thử trên **bản build** (`npm run build` + `npm start`), không bản dev.
- Trang lạ: file HTML ở origin khác (`python3 -m http.server` cổng khác) gọi `fetch('http://127.0.0.1:<port>/api/...')` có / không token; thêm thử
  DNS rebinding bằng `Host` giả qua `curl -H 'Host: evil.test'`.
- Review `<script>`: chèn vào fixture review → mở trang → không chạy (Playwright kiểm `window.__pwned` không có).
- Key lọt log: đặt key giả `sk-test-…`, gây lỗi provider → grep log + `ai_calls` + gói xuất → không thấy chuỗi.
- Bằng chứng lưu `security/evidence/<ngày>/` + dòng trong `security/checklist.md`.
- Ra bản: tăng version Web 8.0.0, CHANGELOG, CI xanh, anh đồng ý mới tag `v8.0.0`.

## File đụng tới

- `security/attacks/*.html`, `security/attacks/run.sh` (mới) — kịch bản thử lặp lại được
- `web/tests/e2e/security.spec.ts` (mới) — XSS + token chạy được trong E2E
- `security/checklist.md`, `security/evidence/` — bằng chứng
- code lọt — sửa + test
- `web/package.json`, `version.ts`, `CHANGELOG.md` — 8.0.0

## Tasks

### Task 1: Kịch bản thử
- [ ] `security/attacks/` + spec E2E; chạy trên bản build.

### Task 2: Sửa chỗ lọt
- [ ] Mỗi chỗ lọt: sửa + test → thử lại tới khi chặn.

### Task 3: Nâng cấp không mất dữ liệu
- [ ] Bản sao DB 7.x → chạy 8.0 → đếm từng bảng trước / sau (dùng `countRows`).

### Task 4: Ra bản
- [ ] Version 8.0.0, CHANGELOG, CI xanh → anh đồng ý → tag. Chip 58–61, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
