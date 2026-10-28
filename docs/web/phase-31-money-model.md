# Phase 31 · Mô hình tiền

> Chốt **Free gồm gì, Pro gồm gì**, bán **mua đứt (lifetime)** hay **gói tháng / năm** hay cả hai, và giá bao nhiêu.
> Mọi con số dựa trên đo thật, không đoán. Kết quả là file `money.md` để anh duyệt.
>
> **Đổi 2026-10-26:** bán **app tải về + dùng thử + license key**, không tài khoản ([Version 10](version-10.md)).
> Phase này chốt thêm: dùng thử bao nhiêu ngày, có làm giá bậc thang như Wow Keywords không.

<span class="chip chip--done">Xong 2026-10-28 · plan chốt, chưa đo số bán</span>

## Chạy thế nào

```mermaid
flowchart LR
  G[Giá đối thủ<br/>tool niche · keyword · app<br/>có nguồn + ngày] --> M[money.md<br/>qua /app-money]
  C[Chi phí AI mỗi niche<br/>log Phase 27.4 · 39 · 42] --> M
  F[Phễu GA4<br/>Phase 29] --> M
  M --> D[Anh duyệt]
```

**Lifetime** = trả một lần, dùng mãi. **Subscription** = trả theo tháng / năm, tự gia hạn tới khi huỷ.

## Ứng viên chia gói

Chốt ở phase này, chưa phải quyết định:

| Gói | Ứng viên |
|---|---|
| **Dùng thử** | đủ tính năng N ngày (ứng viên 7 hoặc 14), không cần thẻ |
| **Pro (mua đứt)** | license key, 2 máy, cập nhật mãi. Ứng viên giá bậc thang: tăng sau mỗi 20 license, số còn lại đọc từ đơn thật |
| **Hết dùng thử, chưa mua** | ứng viên: chỉ xem + xuất dữ liệu cũ, không tra mới — hoặc giữ Play + App Store + Trends miễn phí. Chốt bằng số fake-door |

Giá: **chưa đo**. Chỉ ghi số sau khi đo giá đối thủ và chi phí AI.

## Làm gì

| | |
|---|---|
| :material-tag-search: **Giá đối thủ** | đo giá tool nghiên cứu niche / keyword / app, mỗi dòng ghi nguồn + ngày. Mốc đầu: [Wow Keywords](../doi-thu-tham-khao.md#wow-keywords) $79 mua đứt (2026-10-26) |
| :material-robot: **Chi phí AI** | AI chạy trên thứ người dùng đã trả ([Phase 27.7](phase-27-7-ai-cost-plans.md)) nên mình không tốn; chỉ đo để ghi trên landing "1 niche tốn khoảng bao nhiêu" |
| :material-lock-open-variant: **Số fake-door** | đọc bảng kết quả [Phase 16](phase-16-decision-board.md#ket-qua-fake-door): tính năng nào được bấm, bao nhiêu email, mức giá người chọn — tín hiệu giá đầu tiên có nguồn |
| :material-filter-variant: **Phễu GA4** | đọc phễu [Version 9](version-9.md): người dùng dừng ở tính năng nào |
| :material-scale-balance: **Chọn mô hình** | mua đứt (mặc định, như Wow Keywords) hay thêm gói năm cho cập nhật · số ngày dùng thử · hết hạn còn dùng được gì · giá bậc thang có / không |
| :material-file-document-edit: **money.md** | viết theo `/app-money` của App-AI-Skills: bảng gói, giá, lý do từng con số kèm nguồn |

<div class="box box--star" markdown>
**Xong khi**

- `money.md` có bảng gói, giá, lý do từng con số kèm nguồn
- Mỗi giá đối thủ có link + ngày đo
- Có số chi phí AI trung bình mỗi niche, lấy từ log thật
- Có số ngày dùng thử + hết hạn còn dùng được gì
- Anh duyệt
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Tạo sản phẩm trên Lemon Squeezy, viết code license (Phase 32)
- Hứa doanh thu, bịa số người mua
- Khoá lại thành Pro tính năng đã Free với người đang dùng
- Gói team / nhiều chỗ ngồi, mã giảm giá, affiliate
</div>

## Kết quả (2026-10-28)

Chốt để làm bản bán đầu. Mọi số đối thủ có nguồn; số bán, chi phí AI thật, phễu GA4: **chưa đo** (chưa có bản bán nào).

**Bản bán 1.0 = app Mac, chỉ tính năng Niche Research.** Tra 1 keyword (Research) + mở cây keyword (Explore) + trang kết
quả. Các tính năng khác (Project, AI Agent, Q&A Gap, chat AI…) **xám + ghi "Bản đầy đủ"**, không xoá code — bật lại bằng 1
biến lúc build. Lý do: bán 1 việc rõ ràng trước, đỡ lỗi, landing nói gọn được.

| Quyết định | Chốt | Vì sao |
|---|---|---|
| Mô hình | **Mua đứt** (lifetime), không subscription | App chạy trên máy, AI dùng tài khoản của người dùng → mình không tốn chi phí hằng tháng. Wow Keywords bán mua đứt (sổ đối thủ, 2026-10-26) |
| Giá | **$39.99 trả một lần**, cố định (anh chốt 2026-10-28) | Bằng khoảng nửa Wow Keywords **$79** (đủ tính năng, đo 2026-10-26) vì bản 1.0 chỉ có 1 tính năng. Không giảm giá, không bậc thang ở bản này |
| Dùng thử | **14 ngày đủ tính năng**, không thẻ, không đăng ký | Tool chọn niche phải chạy trên niche của chính họ mới thấy giá trị. Cùng số với RAM Rescue (đã bán bằng Lemon Squeezy) |
| Số máy | **1 license = 2 máy**, gỡ máy trong Cài đặt | Như Wow Keywords |
| Hết dùng thử, chưa mua | **Không tra mới**; vẫn mở mọi kết quả cũ + tải CSV / xuất | Không khoá dữ liệu của người dùng (luật Version 10) |
| Cập nhật | Miễn phí mọi bản **1.x** | Ghi rõ trên màn mua + landing |
| Giá bậc thang | **Chưa làm** — xét lại sau đơn thứ 20, khi có số đơn thật để đếm | Đếm ngược "còn N license" chỉ được làm khi số đọc từ đơn thật |
| Bản đầy đủ (Project, AI Agent…) | Giá mới khi bật lại, người đã mua $39.99 được nâng cấp — chốt sau | Không hứa trước |

**Doanh thu — phép tính, không phải dự báo:** người mua × $39.99 × (1 − 5 %) − $0,50 / đơn (phí Lemon Squeezy) − thuế.
Chưa có người mua.

**Còn để đo sau khi bán:** chi phí AI trung bình mỗi niche (log Phase 27.4) · phễu GA4 tải → mở → tra → mua.

[Tổng quan Version 10](version-10.md)

Plan code chi tiết: [Phase 31](../superpowers/plans/2026-10-25-niche-radar-phase66-money-model.md)
