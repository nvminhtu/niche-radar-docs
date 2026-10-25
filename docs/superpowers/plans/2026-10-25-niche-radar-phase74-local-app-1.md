# Niche Radar Phase 74 — Local App 1.0 (app Mac) — Implementation Plan

> **For agentic workers:** phần lớn đã xong (2026-10-25, `.dmg` ký + notarize). Còn lại là **kiểm trên máy sạch**. Build chỉ bằng `npm run mac`.
> Steps dùng checkbox (`- [ ]`).

**Goal:** bản Web thành app Mac bấm là mở — không cần Node, không gõ lệnh.

**Spec:** [Phase 74 · Local App 1.0](../../app/phase-74-local-app-1.md) · spec gốc [Phase 8 · Local App](../specs/2026-10-24-niche-radar-phase8-local-app.md).

## Mục tiêu · làm · không làm

- **Xong khi:** tài khoản macOS mới chưa cài Node: mở `.dmg` → bấm icon → tra được 1 keyword, Gatekeeper không cảnh báo · mở tới khi bấm được ≤ 5 giây,
  RAM nghỉ ≤ 300 MB · xuất project → nhập máy khác bằng dòng, không nhân đôi · backup → xoá DB → restore đủ · DB thật lên ULID không mất dòng ·
  test xanh, `npm run dev` vẫn chạy.
- **Làm:** phần còn lại — thử máy sạch, ghi số.
- **Không làm:** tính năng tra cứu mới · đăng nhập / sync / license · Windows, auto-update.

## Global Constraints

- Tauri + sidecar Node (`app/`), UI là `web/` — không viết UI lần hai trong `app/`.
- Dữ liệu app: `~/Library/Application Support/niche-radar/` (`NR_DATA_DIR`); bản web vẫn `data/`.

## File đụng tới

| File | Việc |
|---|---|
| `app/scripts/build-mac.sh`, `app/src-tauri/*` | đã có |
| `docs/app/phase-74-local-app-1.md` | kết quả thử máy sạch |

## Tasks

### Task 1: Đóng gói (đã xong 2026-10-25)
- [x] Tauri + sidecar Node, `.dmg` 45 MB (app 119 MB) ký Developer ID + notarize.
- [x] Mở tới khi server sẵn sàng ~0,14 giây · RAM nghỉ ≈ 200 MB.
- [x] Project + xuất / nhập + backup / restore trong app; dữ liệu ở Application Support.

### Task 2: Thử máy sạch (còn lại)
- [ ] Anh tạo user macOS mới (chưa Node), tải `.dmg` từ GitHub Releases → mở → tra 1 keyword. Gatekeeper không cảnh báo (screenshot).
- [ ] Xuất project ở máy chính → nhập máy sạch → đếm dòng bằng nhau; nhập lại không nhân đôi.
- [ ] Ghi kết quả vào trang phase, chip → Xong, ROADMAP.

## Tiến độ

- 2026-10-25: code + `.dmg` xong (bản 0.9.0 build 5 notarize). Còn thử máy sạch.
