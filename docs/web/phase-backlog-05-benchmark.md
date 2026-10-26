# Backlog 05 · Đo mốc

> Trước khi làm tool nhanh hơn, phải **đo nó đang chậm ở đâu**. Phase này viết một lệnh đo thời gian, RAM và dung lượng
> của từng luồng chính, rồi lưu thành **bảng mốc** để các phase sau so lại.

<span class="chip chip--skip">Không làm · 2026-10-26</span>

<div class="box box--danger" markdown>
**Không làm (chốt 2026-10-26):** performance — không ra tiền, không thêm người dùng. Trang giữ lại để tra, không code.
</div>

## Chạy thế nào

```mermaid
flowchart LR
  N[3 niche chuẩn] --> B[npm run bench<br/>mới]
  B --> W[Bản Web<br/>explore · mở trang · query]
  W --> J[(bench/baseline.json)]
  J --> T[Bảng mốc<br/>trong trang này]
```

## Đo những gì

| Chỉ số | Ở đâu |
|---|---|
| Thời gian tới kết quả đầu tiên | bản Web, tra 1 niche |
| Tổng thời gian explore | bản Web (100 keyword hiện mất ~6 phút) |
| Thời gian mở từng trang | bản Web |
| Thời gian query chậm nhất | SQLite (cơ sở dữ liệu trên máy) |
| RAM server | process Node |
| Dung lượng bundle web | file JS/CSS sau `npm run build` |

Mục tiêu cụ thể cho từng số: ghi sau khi đo, không đặt trước.

## Làm gì

| | |
|---|---|
| :material-flask-outline: **Bộ niche chuẩn** | chốt 3 niche cố định, dùng lại cho mọi lần đo của Version 5 |
| :material-timer-outline: **Lệnh đo** | `npm run bench` (mới) chạy 3 niche, ghi đủ các chỉ số ở bảng trên |
| :material-file-chart: **Lưu mốc** | `bench/baseline.json` (mới) trong repo + bảng số trong trang này |
| :material-compare: **So kết quả** | script so bảng keyword và điểm giữa 2 lần chạy cùng niche, cùng ngày — dùng ở Backlog 06–49 để chắc nhanh hơn mà kết quả không đổi |

<div class="box box--star" markdown>
**Xong khi**

- `npm run bench` chạy 3 lần liên tiếp, chênh lệch mỗi số ≤ 15% (đo ổn định mới tin được)
- `bench/baseline.json` có đủ 9 chỉ số cho 3 niche, bảng mốc điền vào trang này
- Chỉ ra được luồng nào / query nào chậm nhất, làm đầu vào cho Backlog 06–49
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Sửa gì cho nhanh (chỉ đo)
- Đặt mục tiêu trước khi có số đo
- Gọi nguồn nhanh hơn giới hạn để đo cho đẹp
</div>

[Tổng quan Version 5](version-5.md)

Plan code chi tiết: [Backlog 05](../superpowers/plans/2026-10-25-niche-radar-phase46-benchmark.md)
