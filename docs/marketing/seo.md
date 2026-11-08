# 4 · SEO (Search Engine Optimization)

> Làm cho Google hiểu site nói về chủ đề gì và tin nó đủ để xếp cao. Đây là phần nền: AEO và GEO đều đứng trên phần này.

<span class="chip chip--todo">Chưa làm theo plan mới · dừng viết bài mới cho tới khi có số Search Console</span>

<div class="box box--goal" markdown>
**Target (đích tự đặt)**

- **Tháng 1:** 0 bài mới · có số index · bồi 10 bài · không còn bài nào 0 link từ thân bài khác
- **Tháng 3:** 1 cụm chủ đề hoàn chỉnh · 8 bài mới · bồi thêm 8 bài · 2 site thật link về
- **Tháng 6:** 2 cụm chủ đề hoàn chỉnh · tổng 20 bài mới · 5 site thật link về
- **Tháng 12:** 4 cụm chủ đề hoàn chỉnh · 15 site thật link về

Kết quả trên Search Console là target ở [mục 1](google-search-console.md): tháng 6 có 15 từ khoá top 10, tháng 12 có 50 từ khoá top 10.
</div>

## Mỗi tháng bao nhiêu bài

**Đề xuất: 4 bài mới + 4 bài bồi mỗi tháng, bắt đầu từ tháng 2.** Không có con số chuẩn, nên đây là mức một người làm được mà vẫn đủ sâu và có số tự đo.

Đề xuất này thấp hơn nhịp cũ vì 3 lý do:

- Site đã có 85 bài, nhưng **trung vị thân bài chỉ 447 từ**, 66 bài dưới 600 từ, 74 bài lên trong 3 ngày.
- **52 bài đã hẹn lịch có 47 bài dưới 600 từ.** Đẩy tiếp sẽ làm tỉ lệ bài mỏng tăng. [Plan dựng lại Blog](plan-blog-hub-2026-11-07.md) đề xuất giữ lại, đang chờ bạn quyết.
- Google xếp việc [viết hàng loạt trang để nhắm nhiều biến thể câu hỏi](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) vào lỗi spam.

Theo quyết định ngày 2026-11-07, **chưa viết bài mới cho tới khi có số Search Console**. Tháng 1 vì vậy chỉ bồi bài.

## Nó là gì

SEO có 4 phần, Google cần cả 4:

1. **Kỹ thuật:** Google đọc được và index được. Phần lớn đã ổn: canonical, sitemap, schema, RSS.
2. **Nội dung:** bài đúng thứ người ta tìm và có thông tin riêng.
3. **Link nội bộ:** các bài nối với nhau để Google hiểu cấu trúc chủ đề. Đây là chỗ yếu: 30/85 bài có 0 link từ thân bài khác.
4. **Link từ site khác (backlink):** site khác chứng nhận mình đáng tin. Hiện `chưa đo`.

## Một cụm chủ đề trông thế nào

Một cụm gồm **1 bài trụ + 6 đến 10 bài con**:

- **Bài trụ:** bài dài, trả lời trọn chủ đề. Nhắm từ khoá chính.
- **Bài con:** mỗi bài một câu hỏi hẹp. Nhắm từ khoá đuôi dài.
- **Một bài con** link lên bài trụ, link sang ít nhất 2 bài con khác, và link tới trang sản phẩm phù hợp.
- **Bài trụ** link xuống mọi bài con, và được trang chủ đề hoặc trang chủ link tới.

**Một cụm 8 bài kéo được bao nhiêu từ khoá?** Không có số chắc, vì một bài tốt có thể hiện cho nhiều từ khoá. Target để so: sau 3 tháng, một cụm 8 bài có ít nhất **40 từ khoá có hiển thị** và **3 từ khoá trong top 20**. Sau tháng đầu tiên có số thật thì chỉnh lại.

## Mỗi bài cần đạt

- [ ] Trả lời đúng một câu người ta đang tìm, đã kiểm bằng gợi ý Google
- [ ] Có số tự đo hoặc ví dụ thật mà bài khác không có
- [ ] Từ 1.200 từ trở lên nếu chủ đề cần, nhưng không thêm chữ cho đủ số
- [ ] Có ít nhất 3 link nội bộ trỏ tới, và ít nhất 3 link nội bộ đi ra
- [ ] Có ngày cập nhật, tên tác giả, nguồn dẫn
- [ ] Có lời mời hợp với bài: thử App Idea Checker hoặc tải app

## Liên quan thế nào tới Search Console

SEO là phần làm, [Search Console](google-search-console.md) là phần chấm điểm. Mỗi bài đi qua 5 mốc:

1. **Đăng bài** → xem URL Inspection, đảm bảo trang đã được index.
2. **Có impressions** → Google đã xem bài liên quan tới từ khoá nào. Thường là tín hiệu đầu tiên.
3. **Đọc vị trí** → đứng 8–20 thì bồi thêm nội dung, thêm link nội bộ.
4. **Đọc CTR** → hiển thị nhiều mà ít bấm thì sửa tiêu đề và mô tả.
5. **Đọc [GA4](ga4.md)** → có bấm mà không tải thì sửa lời mời trong bài.

Báo cáo **Links** trong Search Console cho biết site nào đang link về và trang nào được link nội bộ nhiều nhất, nên dùng nó để đo cả link nội bộ lẫn backlink.

Thời gian cần đợi: [theo Ahrefs](https://ahrefs.com/blog/how-long-does-it-take-to-rank/), trong các trang lọt top 10 trong vòng 1 năm, 40,82% lọt trong tháng đầu. Trang đứng top 10 đa phần đã nhiều tuổi: 72,9% trên 3 năm. Vì vậy site mới nên nhắm cụm đuôi dài trước.

## Lấy backlink thế nào

Không mua link. Cách phù hợp với site này:

- [ ] **Free tool:** App Idea Checker là thứ người khác có lý do để link tới
- [ ] **Dữ liệu tự đo:** ví dụ "top 10 App Store của 30 niche nhỏ", một bộ số người khác trích được
- [ ] **Thư mục sản phẩm đúng ngành:** AlternativeTo và các thư mục tool indie
- [ ] **Trả lời thật trên Reddit và Indie Hackers:** bạn tự đăng, theo hồ sơ ở `/reddit-qa`
- [ ] **Đăng bài khách trên blog indie:** chỉ khi có số riêng để chia sẻ

Product Hunt vẫn để sau, theo quyết định ngày 02/11, vì chưa có số chuyển đổi.

<div class="box box--example" markdown>
**Ví dụ · cụm "AI kiểm ý tưởng app"**

**Bài trụ:** How to validate an app idea before you build. Có sẵn `validate-app-idea-before-you-build` (1.818 từ), chỉ cần bồi thêm số.

**Trang sản phẩm đi cùng:** `/app-idea-checker`.

**Bài con đề xuất:**

1. How to validate an app idea on Reddit (có trong gợi ý Google)
2. How many ratings means an app niche is too crowded
3. How to read 1–2★ reviews to find a feature gap
4. How to use Google Trends for an app idea
5. Can AI validate an app idea? What it gets wrong (thử thật rồi mới viết)
6. Free alternatives to Sensor Tower for indie developers (có trong gợi ý Google)

Bài nào đã có trên blog thì bồi và gộp, không viết bài mới. Nhu cầu của cụm này nhỏ: `app idea validation` gần 0 trên Google Trends US, đo 2026-11-07. Bù lại, người tìm đang gần việc cần một tool.
</div>

## Số đo mỗi 4 tuần

**2026-11-07 (mốc):** 85 bài đã đăng · 52 bài đã hẹn · trung vị 447 từ · 30 bài có 0 link từ thân bài khác · backlink `chưa đo`.

## Liên quan

[1 · Google Search Console](google-search-console.md) · [3 · AEO](aeo.md) · [Plan dựng lại trang Blog](plan-blog-hub-2026-11-07.md)
