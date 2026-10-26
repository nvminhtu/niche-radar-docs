# Niche Radar Phase 33 — Paywall + dùng thử — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` xanh rồi commit.
> Steps dùng checkbox (`- [ ]`). Không đếm ngược giả, không giấu nút đóng, không gọi gói trả phí là quyên góp.

**Goal:** bấm tính năng Pro → màn nâng cấp nói rõ được gì, có dùng thử, có Khôi phục mua; mua xong dùng ngay.

**Spec:** [Phase 33 · Paywall + dùng thử](../../web/phase-33-paywall-trial.md) · **Cần trước:** Phase 31 (gói, N ngày, số máy), Phase 32 (`entitlement`).

## Mục tiêu · làm · không làm

- **Xong khi:** Free → bấm Pro → mua → dùng ngay, không khởi động lại · hết dùng thử → về Free, dữ liệu còn đủ (đếm project trước / sau) ·
  "Khôi phục mua" trên máy mới mở lại Pro · vượt số máy → báo rõ, không khoá máy đang dùng · tính năng đã Free ở bản trước vẫn Free với người đang dùng.
- **Làm:** khoá Pro đúng chỗ, màn nâng cấp (giá, chu kỳ, tự gia hạn, cách huỷ), dùng thử N ngày, Khôi phục mua, giới hạn số máy, khớp landing.
- **Không làm:** mã giảm giá / affiliate · gói team · chi phí AI theo gói (Phase 27.7).

## Global Constraints

- Danh sách tính năng Pro ở **1 chỗ**: `features.ts` thêm `tier: 'free' | 'pro'` + `freeSince` (bản đã Free) — tính năng có `freeSince` ≤ bản người
  dùng cài đầu (`users.firstVersion`) thì vẫn Free với người đó (grandfather).
- Cổng: `requirePro(feature)` ở server (route Pro trả 402 kèm lý do) + `<ProGate>` ở client mở `PaywallModal`.
- Dùng thử: `entitlement.trialEndsAt` do Function ghi lúc bấm "Dùng thử" lần đầu (1 lần / tài khoản); hết hạn → Free, không xoá gì.
- Số máy: mỗi máy có `deviceId` (Backlog 04); `users/{uid}/devices/{deviceId}` lưu `lastSeen`; vượt giới hạn → màn báo + danh sách máy để tự gỡ máy cũ
  — **không** khoá máy đang dùng giữa chừng.
- Khôi phục mua: đọc lại `entitlement` từ Firestore sau đăng nhập + gọi Function `restore` tra Lemon Squeezy theo email nếu thiếu.
- Mua xong: nghe `entitlement` thay đổi → mở khoá ngay (không reload).

## File đụng tới

- `web/src/lib/features.ts` — `tier`, `freeSince`
- `web/src/lib/pro-gate.ts` (mới) + `web/src/server/app.ts` — `requirePro`
- `web/src/components/PaywallModal.tsx`, `ProGate.tsx` (mới) — màn nâng cấp + cổng
- `functions/src/trial.ts`, `restore.ts`, `devices.ts` (mới) — dùng thử, khôi phục, số máy
- `web/src/client/SettingsPage.tsx` — mục Gói: trạng thái, Khôi phục mua, danh sách máy
- `web/tests/pro-gate.test.ts`, `functions/test/*`

## Tasks

### Task 1: Danh sách Pro + cổng
- [ ] `tier`, `freeSince`, `requirePro`, `ProGate`. Test grandfather: người cài bản cũ vẫn dùng tính năng đã Free.

### Task 2: Màn nâng cấp
- [ ] Được gì, giá + chu kỳ, "tự gia hạn, huỷ bất cứ lúc nào ở …", nút đóng rõ, Khôi phục mua. Đối chiếu luật store trong `money.md`.

### Task 3: Dùng thử + hết hạn
- [ ] Function trial; hết hạn → Free; test đếm project trước / sau không đổi.

### Task 4: Số máy + khôi phục
- [ ] Devices + màn vượt giới hạn; restore trên máy mới. Test emulator.

### Task 5: Soát
- [ ] Luồng thật test mode: Free → Pro → dùng ngay. Giá khớp landing (Phase 46). Screenshot paywall 1340 + 375, sáng + tối, Read. CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
