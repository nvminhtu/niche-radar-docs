# Phase 30 · Trang Riêng tư

> Người tải app đọc được **trang Privacy** ghi đúng thứ app gửi đi. Điều kiện để mở bán ở Version 10.
>
> **Đổi 2026-10-26:** bỏ tài khoản nên bỏ luôn phần **xoá tài khoản** và **xuất dữ liệu cloud** — không còn gì trên
> cloud để xoá. Dữ liệu trên máy đã xuất / xoá được từ [Phase 8](phase-8-project-data.md).

<span class="chip chip--done">Xong 2026-10-27</span>

Trang đã có sẵn ở [shotmatic.app/privacy](https://shotmatic.app/privacy) (app chạy local, AI, GitHub token, email,
GA4 trên web, thanh toán sau). Phase này chỉ sửa mục **2. The Niche Radar app**: thay "No tracking in the app" bằng
**số đo tuỳ chọn** — hỏi đồng ý, đúng 6 sự kiện của [Phase 29](phase-29-analytics-errors.md), không gửi chữ gõ, tắt ở
Settings → Data & backup; mục 6 ghi Google Analytics nhận cả số đo app nếu đồng ý.

## Đã làm

- **Landing** (repo `nvminhtu/shotmatic`, `pages/privacy.jsx`): commit `125c4ad` lên `main`, live 2026-10-27
- **Trong app:** link Privacy ở thanh hỏi đồng ý + mục Cài đặt → Data & backup (`PRIVACY_URL` trong `analytics.ts`)

<div class="box box--star" markdown>
**Xong khi**

- Privacy khớp danh sách sự kiện Phase 29 — đối chiếu từng dòng: 6 tên sự kiện, `platform`, version, mã ngẫu nhiên,
  tên loại lỗi ✓
- Thanh hỏi đồng ý có link Privacy, mở đúng trang ✓
- Network 1 phiên: không request nào ngoài danh sách (kiểm ở Phase 29) ✓
- shotmatic.app/privacy hiện mục mới sau deploy ✓
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Tài khoản, xoá tài khoản, xuất dữ liệu cloud — bỏ 2026-10-26
- Tên nhà thanh toán, license: [Version 10](version-10.md)
</div>

[← Phase 29](phase-29-analytics-errors.md) · [Tổng quan Version 9](version-9.md)
