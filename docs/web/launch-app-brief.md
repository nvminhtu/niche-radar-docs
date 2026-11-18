# Launch · Brief: ShotMatic chọn đúng app để làm

> Brief 1 trang cho bản launch. Dựa vào [Bước 0 hiểu sâu](launch-app-hieu-sau.md) (số đo 2026-11-17)
> và [trang Launch](launch-app-market.md). Anh duyệt brief → mới viết spec.

<span class="chip chip--doing">Viết 2026-11-17 · anh chốt 3 câu theo mặc định 2026-11-17 · spec viết 2026-11-17</span>

<div class="box box--goal" markdown>
**Một câu**

ShotMatic giúp người **chưa có app** biết keyword nào **đang có app mới kiếm được tiền**, chợ đó **khó cỡ nào**,
và **có nên làm không**. Trả lời đủ 7 câu ở một chỗ, mỗi số có nguồn, chỗ chưa đo ghi "chưa đo".
</div>

## Khách

**Indie dev / founder làm một mình, chưa có app, đang chọn app để làm.**

- Họ hỏi nhiều nhất về **Cầu, Cung, Nỗi đau, Tiền** (B0.4: 6 · 5 · 5 · 5 trên 30 câu).
- Họ sợ nhất là **mất 6 tháng cho app không ai cần**.
- AppTweak và Appfigures phục vụ team **đã có app**. Tool niche trên TrustMRR thì còn rất nhỏ:
  Niches Hunter $70 MRR, AppSigma $90 (đọc 2026-11-17). Chỗ này chưa ai chiếm.

## Vấn đề phải sửa trước khi hứa

Lấy từ B0, đo 2026-11-17:

- **Điểm đang dẫn sai.** Với 13 niche đang kiếm tiền thật trên TrustMRR, v2 bảo BỎ 8, không niche nào được BUILD.
  Điểm Săn app chấm chúng ngang keyword bình thường (trung vị 64 so với 60).
- **4 điểm cho 1 keyword.** Người dùng không biết tin điểm nào.
- **Câu Tiền gần như mù trên App Store.** Research biết IAP 0/19.710 lần chụp App Store.
- **"Chợ trống" bị coi là tốt**, trong khi tiền nằm ở chợ đông. Tín hiệu đúng là **app mới vẫn leo được top 10**
  (18,8 so với 10,2 /25).

## Lời hứa launch

- **Tiếng Việt:** "Đừng tìm chợ trống. Tìm chợ có app mới đang leo lên và có người trả tiền."
- **Tiếng Anh (landing):** *"Find the app niches where new apps are still breaking into the top 10, and people pay."*
- **Nói thẳng điều không có:** ShotMatic không có số lượt tìm, lượt tải hay lịch sử hạng. Thay bằng độ hot gợi ý,
  Trends, app mới leo được và doanh thu có nguồn.

## Bản launch trả lời 7 câu thế nào

| Câu | Trả lời bằng | Khác hiện tại |
|---|---|---|
| 1 · Cầu | độ hot gợi ý · Trends trung bình + đang lên | giữ, gộp vào điểm chính |
| 2 · Cung | tổng rating top 10 · rating trung vị · tên app chiếm keyword | **thành thẻ Độ khó**, không trừ điểm cơ hội |
| 3 · Cửa vào | số app dưới 1 năm leo được top 10 · % đối thủ bỏ bê | **phần nặng nhất của điểm** |
| 4 · Nỗi đau | 3 lời chê nặng nhất, có câu nguyên văn | giữ (Review Mining, Điểm yếu đối thủ) |
| 5 · Tiền | gói IAP iOS + giá Play · khoảng doanh thu TrustMRR có nguồn | **mới: đọc IAP iOS ngay trong Research** |
| 6 · Khác biệt | bảng tính năng + "làm cái này vì người ta than cái kia" | không chấm, chỉ để đọc |
| 7 · Quyết định | **1 điểm cơ hội /100** + Độ khó + BUILD / TEST / BỎ | **thay 4 điểm bằng 1** |

## Phạm vi

**Làm cho launch** (theo thứ tự):

1. **Một điểm cơ hội /100** thay v1, v2, sức khoẻ và Săn app. "App mới leo được" nặng nhất, Trends kế tiếp.
   Phần chưa đo bỏ khỏi mẫu số. Đo dưới 60% trọng số thì không nói "nên làm".
2. **Thẻ Độ khó** (Cung): hiện cạnh điểm, nói "khó vì sao", không trừ vào cơ hội.
3. **Câu Tiền:** đọc gói IAP iOS cho top 10 ngay trong Research (đã có đường đọc + cache 407 app)
   + ghép TrustMRR → "khoảng doanh thu" có nguồn, hoặc "chưa đo".
4. **Bộ kiểm điểm cố định:** 13 niche kiếm tiền (B0.1) + 1 bộ niche "chết" (app bỏ bê, không ai trả tiền).
   Chạy lại mỗi lần đổi công thức.
5. **Gom app đang dở vào launch:** soát + commit mục 26, 27.0, 28, Soi app liên quan; chốt mục 16 merge hay bỏ.

**Để sau launch:** tự chạy lại lượt bị dừng. Lỗi `interrupted` chủ yếu do server dev tự khởi động lại khi sửa code,
bản app ít gặp hơn. Cần đo lại trên bản app trước khi làm.

**Không làm:**

- số lượt tìm / lượt tải / lịch sử hạng (sân của AppTweak, Appfigures, cần dữ liệu trả tiền hằng tháng).
- YouTube, Amazon/KDP, Maps (giữ code, ẩn menu, anh đã chốt 2026-11-17).
- tính năng mới ngoài 7 câu.

## Free / PRO

Giữ giá **PRO 39,99 USD mua đứt** tới khi có 10 đơn (đã chốt ở [Audit](../marketing/audit-2026-11-07.md)).

| | Free | PRO |
|---|---|---|
| Điểm cơ hội /100 + thẻ Độ khó | có | có |
| Từng phần của điểm, công thức | tóm tắt | đủ |
| Tiền: gói IAP + khoảng doanh thu | **1 dòng** ("có người trả tiền: có / chưa đo") | đủ gói, giá, nguồn |
| Nỗi đau có câu nguyên văn | 1 lời chê | đủ |
| BUILD / TEST / BỎ | không | có (như hiện tại) |

Ý: Free cho thấy **có cơ hội hay không**; PRO cho **đủ bằng chứng để quyết**.

## Đo thành công thế nào

| Đo gì | Bây giờ (2026-11-17) | Mục tiêu launch |
|---|---|---|
| Niche kiếm tiền bị bảo BỎ | 8 / 13 | **0 / 13** |
| Cách biệt điểm: nhóm kiếm tiền so với nhóm chết | chưa có nhóm chết | **≥ 15 điểm** |
| App top 10 App Store biết có IAP | 0% trong Research | **≥ 80%** |
| Số điểm khác nhau cho 1 keyword | 4 | **1** |
| Lỗi nguồn thật (không tính bị dừng) | Play ~2% · App Store 1,9% · Trends 4,4% | giữ dưới 5% |
| Đơn PRO thật | chưa đo | 10 đơn (mốc xét lại giá) |

## Rủi ro

- **13 niche là mẫu nhỏ.** Có thể chỉnh điểm cho vừa 13 cái này mà sai với phần còn lại.
  Vì vậy cần nhóm "chết" để chặn kiểu "nâng điểm tất cả".
- **Đọc IAP iOS làm Research chậm hơn**, chưa đo. App Store hay trả 429 khi đọc nhiều.
- **Đổi điểm làm lệch dữ liệu cũ:** Project, Bàn quyết định, bản export đang dùng điểm v2.

## Anh đã chốt 3 câu (2026-11-17, theo mặc định)

| # | Câu hỏi | Đã chốt |
|---|---|---|
| 1 | Lời hứa "tìm chợ có app mới đang leo lên và có người trả tiền" được không? | Được |
| 2 | Free thấy điểm + Độ khó, nhưng không thấy BUILD / TEST / BỎ? | Có |
| 3 | Nhóm niche "chết": mình tự chọn ~15 keyword (app top 10 bỏ bê > 1 năm, không thu tiền), ghi rõ cách chọn? | Có |

Tiếp → [Launch · Spec](launch-app-spec.md): mỗi câu thành 1 khối kết quả (nguồn, công thức, chỗ "chưa đo", màn hình).
