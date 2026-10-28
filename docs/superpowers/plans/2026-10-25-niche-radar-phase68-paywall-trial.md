# ShotMatic Phase 33 — Bản Mac Niche Research + dùng thử + paywall — Implementation Plan

> Viết lại 2026-10-28 (bản cũ gắn tài khoản Firebase — bỏ). Làm từng Task theo thứ tự, mỗi Task xong `npm run check` xanh.
> Không đếm ngược giả, không giấu nút đóng, không khoá dữ liệu cũ, không gọi gói trả phí là quyên góp.

**Spec:** [Phase 33](../../web/phase-33-paywall-trial.md) · **Cần trước:** [Phase 31](../../web/phase-31-money-model.md) (giá $39.99, 14 ngày, 2 máy) ·
[Phase 32](../../web/phase-32-payments.md) (hợp đồng Lemon Squeezy).

## Mục tiêu · làm · không làm

- **Mục tiêu:** `npm run mac` ra `.dmg` chỉ có Niche Research, cài mới dùng thử 14 ngày, hết hạn mua $39.99 → dán key → Pro ngay.
- **Làm:** biến bản (edition) · trạng thái license trên máy · gọi API license Lemon Squeezy · chặn tra mới khi hết hạn ·
  thanh dùng thử · màn `/license` · menu xám "Bản đầy đủ" · test.
- **Không làm:** Keychain (Phase 35) · Windows (Phase 36) · tự cập nhật (Phase 37) · tài khoản · webhook · mã giảm giá ·
  giá bậc thang · tạo sản phẩm Lemon Squeezy (việc của anh).

## Tasks

- [x] **T1 · Biến bản** — `web/src/lib/edition.ts`: `EDITION` (client, `VITE_NR_EDITION`), `serverEdition()` (`NR_EDITION`),
  `RESEARCH_ONLY`, `LICENSED`. `build-mac.sh`: `NR_EDITION` mặc định `research`, truyền vào vite + esbuild `--define`.
- [x] **T2 · Trạng thái license** — `web/src/lib/license/state.ts`: đọc / ghi `license.json` + bản sao ngày bắt đầu thử;
  hàm thuần `licenseStatus(file, now)` → `trial` (còn N ngày) · `expired` · `pro` · `pro-offline-expired`. Test bằng đồng hồ giả.
- [x] **T3 · Lemon Squeezy** — `web/src/lib/license/lemon.ts`: activate / validate / deactivate, fetch truyền vào được (test giả),
  kiểm `meta.product_id`, lỗi đổi sang câu thường (sai key, hết lượt máy, mất mạng).
- [x] **T4 · API** — `GET /api/license`, `POST /api/license/activate`, `POST /api/license/deactivate`; chặn `POST /api/research`
  và `POST /api/explore` bằng `402` khi `LICENSED` và hết hạn. Validate lại khi mở app ≤ 1 lần / ngày.
- [x] **T5 · Giao diện** — `TrialBar` dưới header · trang `/license` (màn mua) · menu: mục ngoài Niche Research xám + "Bản đầy đủ" ·
  route ngoài Niche Research → trang `FullEditionOnly` · form Tra / Explore gặp `402` → mở `/license?reason=expired`.
- [x] **T6 · Kiểm** — `npm run check` xanh · `npm run mac:quick` · mở app: thanh "Còn 14 ngày" · sửa `license.json` lùi 15 ngày →
  màn mua, kết quả cũ vẫn mở + CSV tải được · dán key test → Pro · screenshot đã Read ở 1340px.

## Sau khi anh gửi link checkout + Product ID

Điền vào `web/src/lib/license/config.ts` → build lại → mua test → kích hoạt máy 3 phải bị báo → hoàn tiền → app về hết hạn.
