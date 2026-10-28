# Phase 41 · Hồ sơ đối thủ + cờ đối thủ yếu

> Mỗi đối thủ có **một trang riêng** gom mọi thứ tool biết về nó, và bảng đối thủ có **cờ** để nhìn là thấy ai yếu:
> bỏ bê, bị chê, chỉ một store, thu tiền mà làm dở.

<span class="chip chip--todo">Backlog · làm sau · 2026-10-28 · làm một phần · soát code 2026-10-27: có bảng đối thủ + gom vào project · chưa có trang từng đối thủ, cờ đối thủ yếu, nối Play ↔ iOS</span>

<div class="box box--goal" markdown>
**Hiện có.** Bảng đối thủ trong Research (tên, store, rating, số rating, giá, nhãn mô hình tiền — Phase 2, 9); lời chê
và Feature Gap nằm ở khối khác. "Cờ đối thủ yếu" là ứng viên chưa chốt ở [Phase 9](phase-9-small-features.md).
</div>

**Cần xong trước:** [Phase 18](phase-18-competitor-complaints.md) (lời chê theo app) · [Phase 21](phase-21-collect.md) (collect đối thủ) · [Phase 38](phase-38-revenue.md) (doanh thu verified)

## Làm gì

| | |
|---|---|
| :material-card-account-details: **Trang 1 đối thủ** | 2 store (nếu có cả hai), dev, ngày ra mắt, lần cập nhật cuối + nhịp cập nhật, rating + số rating, giá / gói IAP, mô hình tiền, bị chê gì ([Phase 18](phase-18-competitor-complaints.md)), có tính năng gì (Feature Gap), doanh thu verified nếu có ([Phase 38](phase-38-revenue.md)) |
| :material-flag-variant: **Cờ trên bảng đối thủ** | `bỏ bê` (cập nhật > 12 tháng) · `bị chê` (★ < 4 mà ≥ 1k rating) · `một store` · `thu tiền` (subscription / mua đứt) · `mới vào` (ra mắt < 12 tháng mà đã lên top) |
| :material-link-variant: **Khớp cùng 1 app 2 store** | luật tên + dev + web để nối bản Play với bản iOS; không chắc thì để riêng |
| :material-shape-outline: **Đối thủ ở niche nào** | trang đối thủ liệt kê mọi niche / keyword nó xuất hiện trong DB |
| :material-plus-box: **Collect đối thủ** | gom đối thủ vào project ([Phase 21](phase-21-collect.md)) để theo dõi |

<div class="box box--rules" markdown>
**Luật**

- Mỗi cờ là luật cố định ghi trên UI (di chuột vào cờ), ngưỡng sửa được ở Cài đặt
- Không tự gắn "yếu" bằng AI
</div>

<div class="box box--star" markdown>
**Xong khi**

- 3 niche thật: kiểm tay 15 cờ, ≥ 14 đúng với trang store
- Nối Play ↔ iOS: kiểm tay 10 cặp, 0 cặp nối sai
- Trang đối thủ đọc được ở 1340px + 375px, screenshot đã Read
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- So 2–5 đối thủ cạnh nhau — [Phase 56](phase-56-compare-competitor.md)
- Theo dõi thay đổi của đối thủ theo thời gian — [Phase 42](phase-42-tracking.md)
</div>

Plan code chi tiết: [Phase 41](../superpowers/plans/2026-10-25-niche-radar-phase22-competitor-profile.md)
