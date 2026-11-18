# 11 · Săn kênh nhỏ view nổ

> Plan 2 · mục 11. Trang YouTube có lối vào thứ tư **Săn kênh nhỏ view nổ**: gõ 1 chủ đề → máy gom tới 100 kênh →
> lọc ra kênh nhỏ, mới, ít video mà view nổ → soi sâu 10 kênh → chốt 3 kênh. Không key, không AI (AI chỉ đọc lại số nếu bấm ✦).

<span class="chip chip--done">Làm 2026-11-14 · đã code, chưa ra bản</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Anh duyệt mockup và chốt làm mục này ngày 2026-11-14.
</div>

## Ý tưởng: quy luật cung – cầu

Kênh **nhỏ** (ít sub, mới mở, ít video) mà video lại có view **gấp nhiều lần số sub** nghĩa là người xem tìm tới chủ đề
nhiều hơn số kênh đang làm: **cầu > cung**, chủ đề vẫn làm được. Kênh lớn có view cao thì không chứng minh gì,
vì người xem cũ kéo view.

Trang Soi 1 kênh (mục 7) chỉ soi kênh anh tự dán vào. Mục này đi **tìm** những kênh như vậy.

## Đã đo trước khi làm (2026-11-14, VN, chủ đề "kinh tế")

- Tìm chủ đề + 9 câu YouTube gợi ý, lọc video đăng trong tháng: **10 lần tìm → 68 kênh trong 8 giây**.
- Đọc 1 kênh (trang kênh + About + 30 video gần nhất): **~0,9 giây**.
- Trong 12 kênh đầu đã có 2 kênh đúng loại cần tìm: 1 kênh 14,3K sub mở 96 ngày có video 1,05 triệu view (73× sub),
  1 kênh 5,1K sub mở 42 ngày có video 231K view (46× sub).

## Phễu 3 bước, mỗi bước 1 nút

### Bước 1 · Lưới rộng

Gõ chủ đề, chọn nước và kỳ đăng video (tuần / tháng / năm). Máy tìm chủ đề + tới 11 câu YouTube gợi ý, gom tất cả kênh có video
trong kết quả, giữ tối đa 100 kênh có video nhiều view nhất. Lúc này chưa biết sub. Lưu thành 1 dòng lịch sử `hunt|vn|month|chủ đề`,
dùng lại trong 1 ngày.

### Bước 2 · Đọc kênh + lọc kênh nhỏ

Đọc sub, ngày mở kênh, số video và 30 video gần nhất của từng kênh (~1 phút cho 70 kênh). Rồi lọc bằng 4 chip, đổi chip là phễu đổi ngay
(không gọi lại YouTube):

- Sub dưới 100K (chọn 10K / 50K / 100K / 500K / tắt)
- Mở chưa tới 1 năm (3 tháng / 6 tháng / 1 năm / 2 năm / tắt)
- Tối đa 50 video (20 / 50 / 100 / 300 / tắt)
- Có video từ 10× sub (3× / 5× / 10× / 20× / tắt)

Kênh qua đủ điều kiện xếp theo **view cao nhất đã thấy ÷ sub**. Thiếu ngày mở / số video thì không loại; kênh ẩn sub thì loại.
10 kênh đầu được tick sẵn để soi sâu, anh bỏ / thêm được.

### Bước 3 · Soi sâu, chốt 3 kênh

Đọc 90 video có tiêu đề của từng kênh đã chọn, rút cụm keyword lặp trong tiêu đề, hỏi ô gợi ý YouTube cho các cụm đó (bỏ trùng, tối đa 30 lần).
Mỗi kênh có điểm 0–100:

| Phần | Điểm | Đủ điểm khi |
|---|---|---|
| Nổ mạnh | 40 | view giữa mỗi video ÷ sub từ 10× |
| Nổ đều | 30 | từ 5 video đạt 3× sub (không bắt nhầm 1 video ăn may) |
| Có người gõ | 15 | có keyword được ô gợi ý YouTube trả về |
| Nhiều kênh cùng làm | 15 | keyword cũng có trong tiêu đề kênh khác trong nhóm |

Mọi ngưỡng là quy ước của ShotMatic, không phải số đo. Sửa ở `web/src/lib/youtube-hunt.ts`.

## Trang chi tiết 1 kênh chốt

- Số lớn: điểm / 100, view giữa ÷ sub, số video nổ / số video đã đọc, 4 thanh điểm có icon.
- **Keyword gắn nhãn:** lửa khi kênh nhỏ khác trong nhóm cũng làm, mũi tên lên khi YouTube gợi ý. Bấm keyword để tra ở *Tìm ý tưởng*.
- **Nội dung kênh:** kiểu tiêu đề (danh sách, hướng dẫn, review, trải nghiệm…) kèm số video nổ của từng kiểu, nhịp đăng / tuần.
- **Video nổ to:** thumbnail, thanh × sub, view, ngày đăng.
- Nút *Soi kênh* mở trang Soi 1 kênh đầy đủ (hạng tìm kiếm, thu nhập ước).

## Giới hạn

- "Keyword đang trend" suy ra từ dữ liệu YouTube tự có (có người gõ, nhiều kênh nhỏ cùng dùng), **chưa** có hướng lên / xuống của Google Trends.
- Kết quả tìm của YouTube khi không đăng nhập gần như không có Shorts (đo 2026-11-12), nên phễu này là kênh video dài.
- Tuổi video là số ước ("3 weeks ago"). 1 kênh chỉ là 1 dấu hiệu — chắc hơn khi 2–3 kênh nhỏ cùng nổ.

## Code

- Thu số: `web/src/collectors/youtube-hunt.ts` (3 hàm cho 3 bước, dùng chung hàng đợi YouTube).
- Lọc, chấm điểm, câu hỏi AI: `web/src/lib/youtube-hunt.ts`.
- API: `POST /api/social/search` với `{ hunt, country, period }` (bước 1) hoặc `{ huntStep: 2 | 3, from, picks }`; bước 2 + 3 cập nhật đúng dòng của bước 1.
- Giao diện: `web/src/client/YoutubeHunt.tsx`. Test: `web/tests/youtube-hunt.test.ts`.
