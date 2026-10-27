# Version 9 · Analytics + báo lỗi (bỏ Account)

> Trước khi bán, phải **đo được** người tải app đi tới đâu: mở app → dùng thử → tra niche đầu tiên → nhập license.
> Và **biết khi app lỗi** trên máy người khác mà không cần họ báo. Version 9 làm đúng 2 việc đó.
>
> **Đổi 2026-10-26:** bỏ hẳn tài khoản (Firebase Auth, sync project, xoá tài khoản). Học Wow Keywords: app chạy trên
> máy, không tài khoản, license key là đủ để bán. Backlog 03, B04 chuyển xuống [Không làm](../appendix.md#khong-lam-chot-2026-10-26).

<span class="chip chip--todo">Chưa làm · làm ngay sau Version 1 (Phase 1–45)</span>

## Mục tiêu

- **Đo được phễu bán app:** tải → mở app → dùng thử → tra niche đầu tiên → explore → xuất → nhập license. Biết người
  dùng rơi ở bước nào.
- **Biết khi app lỗi** trên máy người khác.
- **Trang Riêng tư** ghi đúng thứ app gửi đi — điều kiện để mở bán ở [Version 10](version-10.md).

**Thước đo Version 9 xong:** bảng phễu có số thật từ ≥ 3 người dùng ngoài · có báo lỗi tự động từ app · Privacy Policy
khớp từng sự kiện gửi đi.

## Chạy thế nào

```mermaid
flowchart LR
  APP[App / bản Web<br/>chạy trên máy] --> C{Đồng ý<br/>gửi số đo?}
  C -- có --> AN[Phase 29<br/>sự kiện phễu<br/>chỉ loại + số đếm]
  C -- không --> N[Không gửi gì]
  APP --> ER[Phase 29<br/>báo lỗi tự động]
  AN & ER --> PV[Phase 30<br/>trang Riêng tư]
  LOCAL[(SQLite trên máy<br/>mọi dữ liệu)] -.ở lại máy.- APP
```

## Các phase

- [Phase 29 · Analytics + báo lỗi](phase-29-analytics-errors.md) — ✅ 2026-10-27: 6 sự kiện phễu + báo lỗi qua GA4, có hỏi
  đồng ý (`trial_start`, `license_activate` để Version 10)
- [Phase 30 · Trang Riêng tư](phase-30-privacy-delete.md) — ✅ 2026-10-27: Privacy ghi đúng thứ gửi đi; phần xoá tài khoản bỏ

<div class="box box--rules" markdown>
**Luật**

- Không tài khoản, không đăng nhập. Mọi dữ liệu người dùng ở SQLite trên máy
- Analytics không gửi nội dung người dùng gõ, không gửi email / tên
- Không chọn dịch vụ bắt phải có server riêng; Claude không tạo tài khoản dịch vụ, anh tạo, Claude nối code
</div>

## Không làm ở Version 9

<div class="box box--danger" markdown>
- **Tài khoản, đăng nhập, sync project lên cloud** (Backlog 03, B04 cũ) — bỏ 2026-10-26
- **Xoá tài khoản** (phần đầu Phase 30 cũ) — không có tài khoản thì không cần
- **Đưa dữ liệu cào lên cloud**, chạy collector trên server
- **Thanh toán, license**: [Version 10](version-10.md)
- **Quảng cáo, bán dữ liệu người dùng**
</div>
