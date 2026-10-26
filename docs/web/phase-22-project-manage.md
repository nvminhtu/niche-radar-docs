# Phase 22 · Quản lý Project của Niche Collection

> Khi đã có chục project và hàng trăm item, cần **tìm, lọc, xếp ưu tiên, dọn** được — và mỗi project luôn trả lời
> "đang ở bước nào, bước tiếp là gì".

<span class="chip chip--done">Xong 2026-10-26 · 7 tab · tìm / lọc thẻ + trạng thái · lưu trữ / nhân bản / gộp · bước tiếp · nhật ký · so 2 project</span>

<div class="box box--goal" markdown>
**Hiện có (Phase 8 + 9).** Trang Projects (danh sách) + trang một Project: trạng thái **đang xem / ứng viên / loại**,
kết luận, ghi chú, mô tả, xuất / nhập, theo dõi định kỳ 7 / 30 / 90 ngày. Chưa tìm / lọc, chưa thẻ, item chỉ là danh
sách phẳng.
</div>

**Cần xong trước:** [Phase 21](phase-21-collect.md) (item có loại + schema chung 14 + 15)

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
| :material-compare-horizontal: **So 2 project nhanh** | chọn 2 project → bảng cạnh nhau: điểm v2, số đối thủ, lời chê nặng nhất, ai thu tiền, xu hướng. Bản rút gọn — so nhiều niche đầy đủ ở [Phase 44](phase-44-compare-niche.md) |
| :material-rocket-launch: **Ra pipeline** | nút "Làm evidence pack" và "Mở /app-demand" với project đã là ứng viên ([Phase 43](phase-43-evidence-presell.md)) |

<div class="box box--rules" markdown>
**Luật**

- Không xoá cứng từ danh sách: lưu trữ trước, xoá hẳn phải xác nhận + có backup tự động ngay trước đó
- Mọi trường mới (thẻ, lý do loại, bước tiếp, nhật ký) đi theo gói `.niche.json`. **Schema đã thêm sẵn ở migration chung
  của [Phase 21](phase-21-collect.md)** — phase này không nâng DB lần nữa
</div>

<div class="box box--star" markdown>
**Xong khi**

- Dùng đúng schema chung của Phase 21, không thêm migration; mọi trường mới round-trip qua `.niche.json`
- Tìm 1 keyword ra đúng project chứa nó; lọc thẻ + trạng thái cùng lúc chạy đúng
- Gộp 2 project có item trùng → không nhân đôi, nhật ký ghi lại
- Trang project đọc được ở 1340px và 375px, screenshot đã Read
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Chia sẻ project cho người khác / nhiều người sửa — sau [Version 9](version-9.md)
- Bảng kanban kéo thả giữa cột trạng thái (chỉ làm nếu dùng thật thấy cần — ghi Appendix)
</div>

## Kết quả (2026-10-26)

- Dùng đúng schema chung của Phase 21, **không thêm migration**; thẻ, lưu trữ, bước tiếp, trạng thái + lý do item, nhật ký đều đi theo `.niche.json` (test).
- **Danh sách**: ô tìm khớp tên project **và keyword bên trong** · lọc trạng thái + thẻ cùng lúc · sắp Mới sửa / Điểm cao nhất (lịch sử điểm Phase 20) /
  Nhiều item · nút "Đã lưu trữ" · project **đến hạn lên đầu** (⏰). Bộ lọc nằm trên URL (`?tag=mac&status=ứng viên`) nên bấm thẻ ở trang project mở đúng danh sách.
- **Lưu trữ / nhân bản / gộp**: nhân bản cấp `uid` mới cho item; gộp → item trùng (loại + khoá + nước) gộp 1, giữ số chụp cũ nhất, project nguồn
  lưu trữ, nhật ký ghi 2 bên. **Xoá hẳn** chỉ khi đã lưu trữ, tự backup DB ngay trước.
- **Trang project 7 tab**: Tổng quan (đánh giá, bước tiếp + ngày hẹn, thẻ, Ra pipeline, gộp / so, Bàn quyết định) · Keyword · Đối thủ · Lời chê ·
  Khoảng trống · Theo dõi · Ghi chú & nhật ký (+ xuất file). Mỗi bảng: trạng thái giữ / ứng viên / loại (**loại bắt ghi lý do**), ↑ ↓ hoặc
  "Sắp theo điểm cao → thấp" (lưu `rank`).
- **Ra pipeline** (project ứng viên): "Làm evidence pack" từ lượt Research điểm cao nhất + "Copy lệnh /app-demand".
- **So 2 project**: tick 2 dòng hoặc chọn ở tab Tổng quan → bảng cạnh nhau (375px thành 2 khối chồng): điểm + gợi ý, số đối thủ, lời chê nặng nhất,
  đối thủ thu tiền, xu hướng. Thử trên bản sao DB: habit tracker 5,7 TEST THÊM · 118 đối thủ · "subscription" 95 review vs ram issue 5,4 · 43 đối thủ.
- Kéo thả thật chưa làm — ↑ ↓ + sắp theo điểm đủ dùng; kanban vẫn để Appendix như plan.

Plan code chi tiết: [Phase 22](../superpowers/plans/2026-10-25-niche-radar-phase15-project-manage.md)
