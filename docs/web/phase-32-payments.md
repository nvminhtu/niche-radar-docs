# Phase 32 · Thanh toán + license key

> Bấm Mua → trả tiền → **email gửi license key** → dán vào app → Pro mở. Dùng **Lemon Squeezy** (nền tảng bán phần
> mềm, lo thuế VAT các nước thay mình) và **API license key** có sẵn của nó: app tự kích hoạt / kiểm / gỡ máy, không
> cần server riêng, không tài khoản. Anh tạo cửa hàng, Claude nối code.
>
> **Đổi 2026-10-26:** bỏ webhook + Cloud Functions + quyền Pro trên tài khoản Firebase. Học Wow Keywords: license key là đủ.

<span class="chip chip--todo">Chưa làm · sau Phase 31</span>

## Chạy thế nào

```mermaid
flowchart LR
  A[App<br/>bấm Mua] --> CO[Checkout<br/>Lemon Squeezy<br/>trình duyệt ngoài]
  CO --> EM[Email<br/>license key]
  EM --> K[Dán key vào app]
  K --> ACT[API license<br/>activate · tối đa 2 máy]
  ACT --> PRO[Pro mở<br/>lưu trạng thái trên máy]
  PRO --> V[Kiểm lại định kỳ<br/>validate · offline vẫn chạy]
```

**License key** = chuỗi mã gửi qua email sau khi mua, dán vào app để mở bản đầy đủ. **Activate** = gắn key với một máy;
Lemon Squeezy tự đếm số máy và từ chối khi vượt giới hạn.

## Làm gì

- **Sản phẩm:** theo `money.md` Phase 31, bật "Generate license keys", giới hạn 2 máy. Anh tạo cửa hàng, nhập ngân hàng, thuế
- **Checkout:** nút Mua mở trang checkout trong trình duyệt ngoài, có sẵn mẫu RAM Rescue
- **Kích hoạt:** dán key → gọi API activate, lưu mã máy trên máy · key sai / hết lượt máy → báo rõ bằng lời thường
- **Kiểm lại:** validate lúc mở app tối đa 1 lần / ngày; mất mạng vẫn dùng được tới 14 ngày; hoàn tiền / huỷ key → về
  trạng thái hết dùng thử ở lần kiểm sau
- **Gỡ máy:** nút "Chuyển license sang máy khác" gọi deactivate
- **File:** mới: lớp license trong `web/src/server/` (gọi API Lemon Squeezy) + màn nhập key ở `web/src/client/` (tên chốt ở plan)

<div class="box box--star" markdown>
**Xong khi**

- Mua bằng chế độ test → nhận key → kích hoạt → Pro ≤ 30 giây, không khởi động lại
- Kích hoạt máy thứ 3 → báo "đã dùng trên 2 máy" kèm nút gỡ máy cũ
- Hoàn tiền / tắt key trên dashboard → lần kiểm sau app về hết dùng thử, dữ liệu còn đủ
- Tắt mạng → Pro vẫn chạy trong 14 ngày
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Tài khoản, webhook, Cloud Functions, server riêng
- Mac App Store / Microsoft Store / thanh toán trong app của Apple
- Tự xử lý thẻ, crypto, chuyển khoản tay
- Claude tạo tài khoản Lemon Squeezy, nhập ngân hàng / thuế, bấm bán thật
- Dùng thử, paywall (Phase 33)
</div>

[Tổng quan Version 10](version-10.md)

Plan code chi tiết: [Phase 32](../superpowers/plans/2026-10-25-niche-radar-phase67-payments.md) (bản cũ dùng webhook + Firebase — viết lại theo trang này khi code)
