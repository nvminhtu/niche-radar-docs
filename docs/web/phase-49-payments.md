# Phase 49 · Thanh toán

> Bấm nâng cấp → trả tiền → **quyền Pro gắn vào tài khoản** trong vài giây. Dùng **Lemon Squeezy** (nền tảng bán phần
> mềm, lo luôn thuế VAT các nước thay mình). Anh tạo cửa hàng, Claude nối code.

<span class="chip chip--todo">Chưa làm · sau Phase 48</span>

## Chạy thế nào

```mermaid
flowchart LR
  A[App · Web<br/>bấm Nâng cấp] --> CO[Checkout<br/>Lemon Squeezy]
  CO --> WH[Webhook<br/>Cloud Functions<br/>kiểm chữ ký]
  WH --> P[(Quyền Pro<br/>trên tài khoản Firebase)]
  CO --> LK[License key<br/>app Mac, mẫu RAM Rescue]
  P & LK --> ON[Pro mở<br/>trên app Mac + Web]
```

**Webhook** = Lemon Squeezy tự gọi về server của mình mỗi khi có đơn, gia hạn, huỷ, hoàn tiền. **Cloud Functions** =
đoạn code chạy trên Firebase, không cần server riêng. **License key** = mã kích hoạt, dùng được khi không đăng nhập.

## Làm gì

| | |
|---|---|
| :material-store: **Sản phẩm** | gói theo `money.md` Phase 48. Anh tạo cửa hàng, nhập ngân hàng, thuế trên Lemon Squeezy |
| :material-cart-arrow-right: **Checkout** | mở từ bản Web, gắn tài khoản người mua |
| :material-webhook: **Webhook** | nhận đơn / gia hạn / huỷ / hoàn tiền → cập nhật quyền Pro. Kiểm chữ ký, webhook giả bị từ chối |
| :material-key: **License key** | Lemon Squeezy sinh key khi mua; kích hoạt trong app Mac làm ở [Phase 55b](../app/phase-55b-app-only.md) |
| :material-file-code: **File** | mới: Cloud Function webhook, lớp kiểm quyền Pro trong `web/src/lib/` (tên chốt ở plan) |

<div class="box box--star" markdown>
**Xong khi**

- Mua bằng chế độ test → quyền Pro ≤ 30 giây
- Huỷ / hoàn tiền → quyền tắt
- Webhook giả mạo bị từ chối (kiểm chữ ký)
- Mua test → Pro mở trên bản Web ở 2 trình duyệt
- Đơn test có license key trong email / webhook (kích hoạt trên app ở Phase 55b)
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Mac App Store / thanh toán trong app của Apple
- Tự xử lý thẻ, Stripe tự làm phần thuế
- Crypto, chuyển khoản tay
- Claude tạo tài khoản Lemon Squeezy, nhập ngân hàng / thuế, bấm bán thật
- Paywall, dùng thử (Phase 50)
</div>

[Tổng quan Version 10](version-10.md)
