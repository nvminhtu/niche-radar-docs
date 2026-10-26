# Phase 42 · Theo dõi niche định kỳ

> Bản đầu (Phase 9) chụp số khi anh bấm. Phase này làm nó **tự chạy theo lịch** và **chỉ báo cái đáng chú ý**: đối thủ
> mới vào top, đối thủ bỏ bê cập nhật lại, giá đổi, nhu cầu đổi mạnh.

<span class="chip chip--todo">Chưa làm · plan 2026-10-25</span>

<div class="box box--goal" markdown>
**Hiện có (Phase 9).** Trang Project: **Chụp số ngay** / **Tra lại tất cả + chụp số**, so với lần trước (đối thủ vào /
rời top 10, rating ≥ 0,1★, nhãn tiền, số keyword, Trends, điểm v2), mốc 7 / 30 / 90 ngày hiện "đến hạn". Bảng
`project_snapshots`.
</div>

**Cần xong trước:** [Phase 18](phase-18-competitor-complaints.md) (lời chê mới nổi) · [Phase 20](phase-20-niche-health.md) (lịch sử điểm) · [Phase 40](phase-40-explore-tree.md) (hàng đợi lần lượt) · [Phase 41](phase-41-competitor-profile.md) (cờ bỏ bê)

## Làm gì

| | |
|---|---|
| :material-calendar-sync: **Tự chạy theo lịch** | project bật theo dõi → khi server đang chạy và đến hạn, tự tra lại lần lượt (ban đêm / lúc máy rảnh), giới hạn số lượt mỗi ngày |
| :material-bell-ring: **Chỉ báo cái đáng chú ý** | luật: đối thủ mới vào top 5 · đối thủ `bỏ bê` vừa cập nhật · giá / gói đổi · Trends trung bình đổi ≥ 20% · điểm v2 đổi ≥ 1 · lời chê mới nổi. Còn lại gom thành "không có gì mới" |
| :material-inbox: **Hộp tin thay đổi** | trang chủ có hộp "Thay đổi tuần này" theo project; bấm vào mở so sánh 2 lần chụp |
| :material-chart-timeline-variant: **Dòng thời gian** | trang project: biểu đồ điểm v2 (lịch sử điểm của [Phase 20](phase-20-niche-health.md)), số đối thủ, Trends qua các lần chụp; chấm trên biểu đồ = 1 lần chụp. Đây là **chỗ duy nhất** vẽ điểm theo thời gian |
| :material-account-eye: **Theo dõi đối thủ** | đối thủ đã collect: theo dõi riêng giá, rating, lần cập nhật |
| :material-cog: **Chọn nhịp** | 7 / 30 / 90 ngày hoặc tắt, từng project |

<div class="box box--rules" markdown>
**Luật**

- Không chạy song song nhiều keyword (đỡ bị store / Google chặn); bị chặn thì hoãn, không thử dồn
- Không gửi thông báo ra ngoài máy (email, điện thoại) ở phase này
</div>

<div class="box box--star" markdown>
**Xong khi**

- 1 project thật bật theo dõi chạy tự động đủ 2 lần (giả lập ngày), không cần bấm
- Luật báo: test với dữ liệu giả cho từng loại thay đổi, đúng loại nào báo loại đó
- Hộp "Thay đổi tuần này" + dòng thời gian, screenshot đã Read
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Thông báo đẩy / email — sau [Version 9](version-9.md)
- Chạy khi app tắt (cần dịch vụ nền / máy chủ)
</div>

Plan code chi tiết: [Phase 42](../superpowers/plans/2026-10-25-niche-radar-phase23-tracking.md)
