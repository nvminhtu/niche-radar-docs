# Phase 13 · Quản lý Project của Niche Collection

> Khi đã có chục project và hàng trăm item, cần **tìm, lọc, xếp ưu tiên, dọn** được — và mỗi project luôn trả lời
> "đang ở bước nào, bước tiếp là gì".

<span class="chip chip--todo">Chưa làm · plan 2026-10-25</span>

<div class="box box--goal" markdown>
**Hiện có (Phase 8 + 9).** Trang Projects (danh sách) + trang một Project: trạng thái **đang xem / ứng viên / loại**,
kết luận, ghi chú, mô tả, xuất / nhập, theo dõi định kỳ 7 / 30 / 90 ngày. Chưa tìm / lọc, chưa thẻ, item chỉ là danh
sách phẳng.
</div>

## Làm gì

| | |
|---|---|
| :material-magnify: **Danh sách project** | tìm theo tên / keyword bên trong, lọc theo trạng thái + thẻ, sắp xếp theo ngày sửa · điểm cao nhất · số item |
| :material-tag: **Thẻ** | gắn thẻ tự do (`mac`, `ios`, `kids`, `quý 4`), bấm thẻ để lọc |
| :material-archive: **Lưu trữ / nhân bản / gộp** | lưu trữ project cũ (ẩn, không xoá), nhân bản để thử hướng khác, gộp 2 project (item trùng gộp 1) |
| :material-tab: **Trang project chia tab** | Tổng quan · Keyword · Đối thủ · Lời chê · Khoảng trống · Theo dõi · Ghi chú — mỗi tab là bảng sắp xếp được |
| :material-sort: **Xếp ưu tiên item** | kéo thả hoặc sắp theo điểm; trạng thái từng item (giữ / ứng viên / loại) — **loại phải ghi lý do** |
| :material-flag-checkered: **Bước tiếp** | mỗi project có 1 dòng "bước tiếp" + ngày hẹn; trang danh sách hiện project đến hạn trước |
| :material-timeline-text: **Nhật ký** | ghi tự động: thêm / loại item, đổi trạng thái, đổi kết luận, lần chụp số — xem lại vì sao đã quyết |
| :material-rocket-launch: **Ra pipeline** | nút "Làm evidence pack" và "Mở /app-demand" với project đã là ứng viên ([Phase 22](phase-22-evidence-presell.md)) |

<div class="box box--rules" markdown>
**Luật**

- Không xoá cứng từ danh sách: lưu trữ trước, xoá hẳn phải xác nhận + có backup tự động ngay trước đó
- Mọi trường mới (thẻ, lý do loại, bước tiếp, nhật ký) đi theo gói `.niche.json` và migration có backup
</div>

<div class="box box--star" markdown>
**Xong khi**

- DB thật (mọi project hiện có) lên schema mới, 0 dòng mất (đếm trước / sau)
- Tìm 1 keyword ra đúng project chứa nó; lọc thẻ + trạng thái cùng lúc chạy đúng
- Gộp 2 project có item trùng → không nhân đôi, nhật ký ghi lại
- Trang project đọc được ở 1340px và 375px, screenshot đã Read
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Chia sẻ project cho người khác / nhiều người sửa — sau [Version 9](version-9.md)
- Bảng kanban kéo thả giữa cột trạng thái (chỉ làm nếu dùng thật thấy cần — ghi Appendix)
</div>
