# Phase 5 · Verified Sites

> Biết **ai đang thu tiền thật** trong ngách — doanh thu lấy từ cổng thanh toán, không phải ước tính.

<span class="chip chip--todo">Tạm dừng 2026-10-24 · dời sang tuyến Claude in Chrome (Phase 6)</span>

!!! warning "Tạm bỏ khỏi app (anh chốt 2026-10-24)"
    `llms.txt` của TrustMRR ghi **"Do not scrape the website for full marketplace access"** — tìm theo từ khoá,
    lọc, phân trang phải qua API có key (10 lượt/phút, phải đồng ý Acceptable Use Policy). Bản đầu chỉ đọc top 30
    mỗi category nên 4/5 niche thật ra rỗng. → Khối "Tiền thật" bị gỡ khỏi trang Research; việc tra "ai đang thu
    tiền thật" chuyển thành **job cho Claude in Chrome** ở [Phase 6](phase-6-ai-web.md): Claude mở TrustMRR, tìm
    theo tên đối thủ / niche như người dùng thường, trả file kết quả có link + ngày sync. Code collector cũ giữ lại
    (`web/src/lib/trustmrr.ts`) để dùng khi có API key.

## Chạy thế nào

```mermaid
flowchart LR
  N([niche]) --> TM[TrustMRR<br/>category + trang startup]
  N --> O[Nguồn kiểu TrustMRR<br/>cắm thêm, kiểm từng cái]
  TM --> V[Dòng verified<br/>30 ngày · MRR · provider · ngày sync]
  O --> V2[Dòng verified<br/>hoặc tự khai]
  V --> B[Khối Tiền thật<br/>trên trang run]
  V2 --> B
```

## Làm gì

| | |
|---|---|
| :material-shield-check: **TrustMRR** | doanh thu lấy từ cổng thanh toán (Stripe, RevenueCat, Lemon Squeezy…) của sản phẩm cùng ngách: 30 ngày · MRR · provider · **ngày sync** · nhãn `verified`. Không key: đọc trang công khai; có key (tuỳ chọn): tìm theo từ khoá |
| :material-alert: **Cảnh báo sync cũ** | sync > 30 ngày → "số 30 ngày có thể là 0 giả, xem MRR" |
| :material-puzzle-plus: **Nguồn tương tự TrustMRR** | mỗi nguồn 1 collector, cùng khuôn dòng. Trước khi code mỗi nguồn: còn sống không · số lấy từ cổng thanh toán hay tự khai · có trang/API công khai không |
| :material-tag: **Nhãn độ tin** | `verified` chỉ khi số từ cổng thanh toán; nguồn tự khai → `tự khai`, không bao giờ `verified` |
| :material-link-variant: **Ghép với niche** | từ khoá + category, luôn ghi "**khớp gần đúng**" |

## Nguồn sẽ kiểm (chưa kiểm — điền khi làm)

| Nguồn | Kiểu | Trạng thái |
|---|---|---|
| TrustMRR | cổng thanh toán | ✅ bản đầu 2026-10-24 — 1/3 niche có dòng, 2/3 "không có" + ngày |
| Trang "Open Startup" công khai của founder (dashboard Stripe / Baremetrics / ProfitWell public) | cổng thanh toán | chưa kiểm |
| Sàn bán startup có số đã xác minh | tuỳ sàn | chưa kiểm |

<div class="box box--star" markdown>
**Xong khi**

- Khối Tiền thật có ≥ 1 dòng cho 2/3 niche thật (hoặc ghi rõ "không có sản phẩm cùng ngách" + ngày tra)
- Mỗi nguồn thêm vào có ghi kết quả kiểm (sống / verified hay tự khai) trước khi code
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Coi số TrustMRR là khớp chính xác ngách
- Dịch vụ ước tính trả phí (Sensor Tower, AppTweak…)
- Nguồn chỉ có số tự khai mà dán nhãn `verified`
</div>
