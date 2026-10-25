# Niche Radar Phase 67 — Thanh toán — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` xanh rồi commit. Steps dùng checkbox (`- [ ]`).
> Anh tạo cửa hàng Lemon Squeezy, nhập ngân hàng / thuế, bấm bán thật. Claude chỉ nối code và test ở **test mode**.

**Goal:** bấm nâng cấp → trả tiền → quyền Pro gắn vào tài khoản trong vài giây.

**Spec:** [Phase 67 · Thanh toán](../../web/phase-67-payments.md) · **Cần trước:** Phase 66 (`money.md` đã duyệt), Phase 62 (tài khoản Firebase).
Tham khảo mẫu Lemon Squeezy đã chạy ở app RAM Rescue (license key + webhook).

## Mục tiêu · làm · không làm

- **Xong khi:** mua test → Pro ≤ 30 giây · huỷ / hoàn tiền → tắt quyền · webhook giả bị từ chối (chữ ký) · mua test → Pro mở trên 2 trình duyệt.
- **Làm:** sản phẩm theo `money.md` (anh tạo), checkout gắn tài khoản, Cloud Function webhook, lớp kiểm quyền Pro.
- **Không làm:** thanh toán của Apple · tự xử lý thẻ · crypto / chuyển khoản · paywall + dùng thử (Phase 68).

## Global Constraints

- Tên file chốt: `functions/src/lemon-webhook.ts` (Cloud Function HTTPS, kiểm `X-Signature` HMAC-SHA256 bằng signing secret trong Secret Manager),
  `web/src/lib/entitlement.ts` (đọc `users/{uid}/entitlement` từ Firestore, cache local có hạn).
- Checkout: link Lemon Squeezy có `checkout[custom][uid]=<firebaseUid>` → webhook đọc `meta.custom_data.uid`.
- Sự kiện xử lý: `order_created`, `subscription_created/updated/cancelled/expired/resumed`, `order_refunded`, `subscription_payment_refunded`.
  Idempotent theo `event id` (`webhook_events/{id}`).
- `entitlement`: `{ plan, status, renewsAt, endsAt, source: 'lemon', orderId, updatedAt }` — chỉ Function ghi (quy tắc Firestore cấm client ghi).
- Không đăng nhập → không mua được (nút yêu cầu đăng nhập).
- Secret không vào repo; `functions/.env` gitignore; `firebase functions:secrets:set` anh chạy.

## File đụng tới

| File | Việc |
|---|---|
| `functions/` (mới: `package.json`, `src/lemon-webhook.ts`, test) | webhook |
| `firestore.rules` | `entitlement` chỉ đọc với chủ, không ghi từ client |
| `web/src/lib/entitlement.ts` (mới) | `isPro(uid)`, nghe thay đổi |
| `web/src/components/UpgradeButton.tsx` (mới) | mở checkout có `uid` |
| `README.md`, `CLAUDE.md`, `docs/cach-dung.md`, `CHANGELOG.md` | folder `functions/` mới |
| `functions/test/*.test.ts`, `tests/rules/*` | chữ ký, idempotent, quy tắc |

## Tasks

### Task 1: Cửa hàng (anh)
- [ ] Anh tạo store + sản phẩm theo `money.md` ở test mode, lấy signing secret + variant id.

### Task 2: Webhook
- [ ] Function + kiểm chữ ký + idempotent + ghi `entitlement`. Test: chữ ký sai 401; sự kiện lặp không ghi 2 lần; refund → `status: 'refunded'`.

### Task 3: Client
- [ ] `entitlement.ts`, `UpgradeButton`; quy tắc cấm client ghi `entitlement` (test emulator).

### Task 4: Thử test mode
- [ ] Mua test → đo thời gian tới Pro; huỷ, hoàn tiền; webhook giả bằng `curl`; 2 trình duyệt. Ghi bằng chứng.
- [ ] Cách dùng (bước anh làm), CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
