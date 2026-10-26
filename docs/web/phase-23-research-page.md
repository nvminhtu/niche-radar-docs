# Phase 23 · Research 1 keyword — trang kết quả

> Trang dùng nhiều nhất của tool. Mở ra là trả lời được **"niche này có đáng xem tiếp không"** trong 30 giây; nguồn nào
> lỗi thì biết ngay, chạy lại đúng nguồn đó, không phải tra lại cả lượt.

<span class="chip chip--done">Xong 2026-10-26 · đầu trang là câu trả lời + 3 lý do · 6 câu hỏi · trạng thái + chạy lại từng nguồn · so lần trước · 4 nút đi tiếp</span>

<div class="box box--goal" markdown>
**Hiện có (Phase 1–9).** Research tra Google Play + App Store + Google Trends cùng lúc, bảng tiến độ từng nguồn, rồi
xếp các khối: đối thủ, Trends, Feature Gap, chủ đề than, TrustMRR, sức khoẻ niche… Khối được thêm dần theo phase nên
thứ tự chưa theo câu hỏi chọn niche, trang dài, nguồn lỗi phải tra lại cả lượt.
</div>

**Cần xong trước:** [Phase 18](phase-18-competitor-complaints.md) (lời chê) · [Phase 20](phase-20-niche-health.md) (điểm + cờ) · [Phase 28.1](phase-28-1-ai-summary.md) (tóm tắt) · [Phase 38](phase-38-revenue.md) (ai thu tiền) · [Phase 41](phase-41-competitor-profile.md) (cờ trên bảng đối thủ) · **làm sau Phase 41** dù số nhỏ hơn: trang này sắp lại các khối mà 12–22 thêm vào

## Làm gì

| | |
|---|---|
| :material-view-dashboard: **Đầu trang = câu trả lời** | 1 hàng số ngắn: điểm v2 + gợi ý · số đối thủ đáng gờm · xu hướng 12 tháng · lời chê nặng nhất · có ai thu tiền thật. Bấm số nào nhảy tới khối đó |
| :material-sort-variant: **Thứ tự theo câu hỏi** | Có nhu cầu không → Ai đang làm → Họ bị chê gì → Ai thu tiền → Còn chỗ trống nào → Kết luận. Khối phụ (dữ liệu thô) gập lại |
| :material-alert-circle: **Trạng thái từng nguồn** | mỗi khối ghi nguồn + giờ lấy + trạng thái (đủ · thiếu · lỗi · bị chặn tạm); lỗi có lý do thường ("Google chặn tạm, thử lại sau ~15 phút") |
| :material-refresh: **Chạy lại 1 nguồn** | nút làm lại riêng Trends / App Store / review…, giữ phần đã có |
| :material-compare: **So với lần tra trước** | cùng keyword đã tra → mũi tên lên / xuống cạnh số chính (đối thủ mới, rating, xu hướng) |
| :material-link-variant: **Đi tiếp** | cuối trang: Collect · Explore sâu · Xuất · Làm evidence pack — đúng 4 nút |

<div class="box box--rules" markdown>
**Luật**

- Không thêm nguồn mới, không đổi cách tính — chỉ sắp lại, gom gọn, sửa trạng thái
- Trang dài 1 cột, đọc từ trên xuống; khối có bảng rộng cuộn trong khối, không vỡ trang ở 375px
</div>

<div class="box box--star" markdown>
**Xong khi**

- Anh mở 3 niche thật, trả lời "đáng xem tiếp không" chỉ từ hàng số đầu trang (đồng ý với đọc cả trang)
- Giả lập lỗi từng nguồn (fixture) → khối đó báo đúng lý do, chạy lại riêng được
- Đo thời gian tới khi hàng số đầu trang hiện (ghi số, so với trước)
- Screenshot 1340px + 375px đã Read
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Làm nhanh collector — [Version 5](version-5.md)
- Đổi màu, font, hệ thống giao diện chung — [Phase 25](phase-25-ui-ux.md)
</div>

## Kết quả (2026-10-26)

- **Đầu trang** (`AnswerRow`, API `/research/:id/answer`, chỉ đọc DB): gợi ý BUILD / TEST THÊM / BỎ + điểm + % đo, **3 lý do** (cờ bật trước, rồi yếu
  tố lệch xa điểm giữa nhất), 5 ô: điểm v2 · đối thủ đáng gờm (≥ 100K rating) · xu hướng 12 tháng · lời chê nặng nhất · có ai thu tiền thật
  (TrustMRR nếu có, không thì nhãn giá — ghi rõ "ước"). Bấm ô nhảy tới khối. Thiếu số → "chưa đo".
- **So lần tra trước** cùng keyword + nước: mũi tên + màu (xanh tốt / đỏ xấu) cho điểm, đối thủ đáng gờm, Trends TB, rating trung vị; số app mới.
- **Thứ tự theo câu hỏi**: 1 Có nhu cầu không (Trends) → 2 Ai đang làm (Đối thủ) → 3 Họ bị chê gì · ai là khách → 4 Ai thu tiền → 5 Còn chỗ trống nào
  (Feature Gap) → 6 Kết luận (Sức khoẻ niche). Bảng Keyword × Store (dữ liệu thô) gập cuối trang.
- **Trạng thái từng nguồn** trên mỗi khối: đủ · thiếu (xong nhưng không có số) · lỗi · bị chặn tạm · đang chạy + giờ lấy + nút **chạy lại** riêng
  nguồn đó (giữ nguồn khác). Lỗi có lý do thường ("Nguồn chặn tạm vì gọi dồn dập — thử lại sau ~15 phút"), mã lỗi để nhỏ bên dưới. Test fixture
  RATE_LIMITED / NETWORK / PARSE / xong-không-số.
- **Đi tiếp** cuối trang đúng 4 nút: Collect · Explore sâu · Xuất cho AI · Làm evidence pack.
- **Đo thời gian** (dev server, bản sao DB, 1340px, 3 niche habit / pomodoro / bubble shooter): số đầu tiên (thẻ số, cũ) có sau 66–131 ms; hàng
  câu trả lời hiện sau **602–649 ms** kể từ mở trang (API `/answer` 142–154 ms). Bản build app sẽ nhanh hơn dev.
- Xem 1340 + 375 (375: lý do xuống dưới gợi ý, 5 ô xếp dọc, không cuộn ngang).

Plan code chi tiết: [Phase 23](../superpowers/plans/2026-10-25-niche-radar-phase20-research-page.md)
