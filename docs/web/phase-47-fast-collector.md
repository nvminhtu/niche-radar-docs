# Phase 47 · Collector nhanh hơn

> Hiện tool tra **lần lượt từng nguồn**, nên phải chờ cộng dồn. Phase này cho các nguồn **chạy cùng lúc**, kết quả
> hiện dần lên màn hình, và không tra lại thứ vừa tra xong.

<span class="chip chip--todo">Chưa làm · sau Phase 46</span>

## Chạy thế nào

```mermaid
flowchart LR
  K[Keyword cần tra] --> C{Cache 24 giờ<br/>đã có?}
  C -- có --> S[Dùng lại]
  C -- chưa --> Q[Hàng đợi theo nguồn<br/>Play · App Store · Trends…]
  Q --> L[Mỗi nguồn giữ<br/>giới hạn gọi riêng]
  L & S --> U[Đổ dần lên UI<br/>stream]
  L --> P[(Lưu tiến độ<br/>lỗi thì chạy tiếp)]
```

## Làm gì

| | |
|---|---|
| :material-call-split: **Song song theo nguồn** | mỗi nguồn một hàng đợi riêng, chạy cùng lúc. Giới hạn gọi giữ như cũ (vd App Store 1 request / 3 giây ở `web/src/lib/rate-limit.ts` + `web/src/collectors/appstore.ts`) |
| :material-play-speed: **Đổ kết quả dần** | có dòng nào đẩy lên UI ngay (stream — gửi từng phần, không chờ xong hết) |
| :material-cached: **Cache dùng chung** | cache theo keyword, dùng chung giữa các niche: niche B dùng lại keyword niche A đã tra trong 24 giờ |
| :material-restart: **Chạy tiếp khi lỗi** | lỗi / mất mạng giữa chừng → chạy tiếp từ chỗ dừng, không tra lại từ đầu |
| :material-scale-balance: **Giữ kết quả** | chạy script so của Phase 46: cùng niche, cùng ngày → cùng bảng keyword, cùng điểm |

<div class="box box--star" markdown>
**Xong khi**

- Kết quả đầu tiên ≤ 30 giây
- Tổng thời gian ≈ nguồn chậm nhất + ≤ 10%
- Không nguồn nào bị chặn nhiều hơn mốc
- Ngắt mạng giữa chừng rồi bật lại → chạy tiếp được
- `npm run bench` đo lại: không chỉ số nào tệ đi quá 10% so với `bench/baseline.json`
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Gọi nguồn nhanh hơn giới hạn, proxy xoay, nhiều IP
- Hàng đợi trên server cloud
- Thêm nguồn mới
</div>

[Tổng quan Version 5](version-5.md)
