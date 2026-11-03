# Phase 53 · Amazon Search

> Gõ một niche → biết **người ta tìm gì trên Amazon**, sản phẩm nào bán chạy, đông tới đâu, giá bao nhiêu —
> **không dùng AI**, chỉ cào số. Hợp niche sản phẩm số / vật lý đi kèm app (planner, template, journal…).

<span class="chip chip--done">Xong bản đầu 2026-11-02 · trang Social Search → tab Amazon</span>

<div class="box box--star" markdown>
**Đã làm (2026-11-02)** — tab Amazon

- Gợi ý Amazon keyword gốc + a–z (10 chợ: US, CA, MX, UK, DE, FR, IT, ES, AU, JP), nhãn `AMZ`
- Trang kết quả của 3 keyword, cách nhau ≥ 5 giây: sản phẩm không tài trợ · giá · sao · số review · huy hiệu "bought in past month" · nhận xét từng keyword
- Ô số: số sản phẩm · tổng review · review trung vị · giá thấp / giữa / cao · lính mới (< 100 review) · đã bán tháng trước
- Đọc số dùng chung lib của extension ShotMatic Scout (`extension-amazon/lib/`) — một chỗ cho khuôn chữ Amazon
- **Bị chặn** (503, captcha, trang thử thách `bm-verify`) → dừng phần trang tìm, báo trên UI, không vượt, không proxy; lần tra bị chặn không giữ cache
- Đo 2026-11-02 từ máy dev: lúc ra đủ (80 sản phẩm, 3 trang), lúc ra trang thử thách → chặn đúng. Giá hiện theo tiền tệ Amazon đổi theo IP (VND ở Việt Nam)

**Chưa làm:** BSR top 5 + ngày lên kệ (cần mở trang sản phẩm) — "lính mới" tạm tính theo số review, không theo ngày lên kệ
</div>


## Chạy thế nào

```mermaid
flowchart LR
  N([niche]) --> AC[Gợi ý Amazon<br/>autocomplete]
  AC --> K[Cây keyword Amazon]
  K --> S[Trang kết quả tìm<br/>Top 20 sản phẩm]
  S --> P[Giá · sao · số review<br/>· huy hiệu đã bán]
  P --> D[Trang sản phẩm Top 5<br/>BSR · ngày lên kệ]
  D --> T[Bảng Amazon<br/>độ đông · giá · cơ hội]
```

## Chọn cách lấy (kiểm lại lúc làm)

| Cách | Là gì | Ưu | Nhược |
|---|---|---|---|
| **Gợi ý Amazon** (autocomplete) | endpoint gợi ý tìm kiếm công khai | nhẹ, ít bị chặn | chỉ có keyword |
| **Cào trang tìm + trang sản phẩm** (đề xuất) | `fetch` + `cheerio` đọc HTML | 0 đ, đủ giá / sao / review / BSR | Amazon chặn rất nhanh, hay hiện captcha |
| Amazon Product Advertising API | API chính thức | ổn định | cần tài khoản Associates có doanh số — không hợp tool nội bộ |

<div class="box box--rules" markdown>
**Luật cào** (chặt hơn các nguồn khác)

- Gọi rất thưa (≥ 5 giây / request), cache 7 ngày, chỉ Top 5 keyword × Top 20 sản phẩm
- Gặp captcha / trang chặn → **dừng nguồn Amazon**, báo trên UI; **không vượt captcha**, không proxy xoay
- Không đăng nhập Amazon, không đọc trang cần đăng nhập
</div>

## Làm gì

| | |
|---|---|
| :material-magnify: **Gợi ý Amazon** | nguồn keyword riêng, nhãn `AMZ` trong cây |
| :material-cart: **Top 20 sản phẩm** | giá · sao · số review · huy hiệu "bought in past month" (khi có) |
| :material-account-group: **Độ đông Amazon** | tổng review top 20 (thang log) |
| :material-trophy: **BSR top 5** | hạng bán chạy theo danh mục — số Amazon tự công khai |
| :material-cash: **Khoảng giá** | thấp · trung vị · cao |
| :material-clock-fast: **Lính mới thắng** | sản phẩm lên kệ < 12 tháng mà vào top → còn chỗ chen |

<div class="box box--star" markdown>
**Xong khi**

- 3 niche thật có cây keyword Amazon + bảng top sản phẩm + khoảng giá
- Chạy 3 niche liền không chạm captcha (hoặc chạm thì UI báo đúng, nguồn khác vẫn chạy)
- Test xanh; screenshot đã Read
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Đọc review bằng AI — [Phase 54](phase-54-amazon-ai.md)
- Ước doanh số từ BSR (chỉ ghi BSR, không quy ra tiền)
- Dịch vụ trả phí (Jungle Scout, Helium 10, Keepa)
</div>

Plan code chi tiết: [Phase 53](../superpowers/plans/2026-10-25-niche-radar-phase33-amazon-search.md)
