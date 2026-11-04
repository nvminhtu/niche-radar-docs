# Marketing 2 · Google Search Suggestion → Blog

> Lấy cụm người ta **đang gõ thật** trong ô tìm Google (gợi ý Autocomplete), lọc cụm có chữ "đau", rồi viết bài blog
> trả lời đúng cụm đó. Kênh chính để kéo khách im lặng từ Google.

<span class="chip chip--doing">Đang chạy · 64 bài đã có (2026-11-02) · chưa đo số</span>

<div class="box box--goal" markdown>
**Đích**

- Mỗi bài mới bắt đầu từ **1 cụm có trong gợi ý Google** (có người gõ), không đoán từ khoá.
- Chăm 64 bài đã có trước, viết thêm **2–3 bài / tuần**.
- Tháng 3–6: vài bài lên top 10, tổng **30–100+ click / ngày** từ Google (giả định).

**Xong khi:** Search Console có ≥ 10 bài nằm top 10 (đo ở [Google Analytics + Search Console](google-analytics.md)).
</div>

## Lấy gợi ý thế nào

Skill `/shotmatic-blog` chạy `harvest.py`:

1. Gọi gợi ý Google (US, tiếng Anh) cho từng seed + bộ chữ "đau": *not working, why, no downloads, alternative, vs…*
2. Gọi thêm Ask HN (founder tự kể chỗ kẹt) theo cùng seed.
3. In 2 danh sách: **Autocomplete có chữ đau** và **Ask HN xếp theo điểm**, ghi vào hàng chờ `content/blog-queue.csv` (repo shotmatic).

Lọc tay:

- Giữ cụm của **người làm app** đang kẹt, bỏ cụm của người dùng app ("outfit ideas app free").
- Cụm phải có trong gợi ý Google **hoặc** có bài Ask HN ≥ 5 điểm. Không có cả hai thì bỏ.
- Đo thêm Google Trends 12 tháng (US). Cụm = 0 vẫn viết được nếu có trong gợi ý: đó là đuôi dài.
- Không viết 2 bài cùng một từ khoá (tự giành hạng của nhau). Trùng thì sửa bài cũ.

## Chăm 64 bài đã có (tuần 1–8)

Đã đăng 59 bài (2026-11-01 và 02), 5 bài hẹn 04–13/11 (xem [Phase 46.1 · Blog](../web/phase-46-1-landing-blog.md)).
Việc chính là **xem bài nào Google đang thử** rồi đẩy tiếp bài đó.

- [ ] Mỗi tuần ghi impressions và click từng bài (bảng ở [Google Analytics + Search Console](google-analytics.md))
- [ ] Bài có impressions mà **vị trí 8–30**: sửa lại cho sát câu hỏi, thêm số tự đo, thêm FAQ, thêm link nội bộ từ bài khác
- [ ] Bài **0 impressions sau 6 tuần**: xem lại từ khoá (có ai gõ không?), sửa tiêu đề hoặc gộp vào bài khác
- [ ] Viết thêm **2–3 bài / tuần**, chỉ từ cụm đã lấy ở bước trên

## Cách nhận biết blog đang chạy

| Thời điểm | Dấu hiệu đúng hướng |
|---|---|
| Tuần 2–6 | Bài đã index, impressions tăng dần dù click gần như bằng 0 |
| Tháng 2–3 | Vài bài lên top 20–30, có vài click mỗi ngày |
| Tháng 3–6 | Vài bài lên top 10, tổng 30–100+ click / ngày từ Google |

Nếu sau 6–8 tuần impressions vẫn gần như bằng 0, lỗi nằm ở **cách chọn từ khoá hoặc index**, đừng bỏ kênh blog.

## Liên quan

[Phase 46.2 · Từ khoá + blog + Search Console](../web/phase-46-2-seo-keyword-blog-gsc.md) ·
[Phase 46.4 · Guide Google Trends](../web/phase-46-4-google-trends-guide.md) · [AEO / GEO](aeo-geo.md) ·
Skill: `/shotmatic-blog`
