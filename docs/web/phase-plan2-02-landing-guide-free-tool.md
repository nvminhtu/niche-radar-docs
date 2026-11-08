# 2 · Plan tối ưu Landing page, Guide, Free tool

> Plan 2 · mục 2. Người lạ vào shotmatic.app phải hiểu ngay ShotMatic làm gì, thấy một kết quả thật, rồi bấm tải. Ba chỗ
> người lạ chạm vào đầu tiên là landing, guide và free tool, nên làm cả ba theo cùng một khuôn. Mẫu để học: AppKittie,
> đối thủ đang được ChatGPT gợi ý cho người làm app.

<span class="chip chip--todo">Plan 2026-11-07 · chờ anh duyệt · chưa làm</span>

<div class="box box--goal" markdown>
**Đích**

- **Landing:** màn đầu nói ShotMatic cho người làm app được gì, kèm 1 thẻ niche có số thật và 1 nút tải.
- **Guide:** mỗi guide có ảnh chụp app thật, cuối bài có nút tải và link sang free tool cùng chủ đề.
- **Free tool:** có trang `/tools` gom các tool; App Idea Checker (live 2026-11-07) là tool đầu.

**Xong khi:** 3 phần trên đã live, và GA4 đếm được lượt bấm tải theo chỗ bấm (`place=landing`, `place=guide:<slug>`,
`place=tool:<slug>`). GA4 chưa đọc được (thiếu khoá service account), nên target số lượt tải để `chưa đo`, đặt sau 4 tuần có số.
</div>

## Học gì từ AppKittie (đọc trang 2026-11-07)

Số dưới đây là **họ tự ghi** trên trang, chưa kiểm. Mục đích là học cách bày, không phải so số.

- **Hook nói kết quả, không nói tính năng.** Câu đầu "Find what's winning in mobile apps", dòng dưới liệt kê thứ có:
  doanh thu, lượt tải, quảng cáo, video viral, keyword, màn onboarding.
- **Màn đầu có sản phẩm thật kèm số.** Thẻ app (Cal AI, Nomadtable…) ghi doanh thu ước tính, lượt tải, tăng trưởng 12 tháng.
  Người xem hiểu tool làm gì mà không cần đọc.
- **Lời khen ghi rõ người nói là ai.** Mỗi lời khen kèm tên app và doanh thu của người nói. Có thêm logo khách và con số
  "3,000+" người dùng.
- **"Ask your AI".** Họ cho nối ChatGPT, Claude vào dữ liệu, giống MCP của ShotMatic, nên điểm này không còn làm ShotMatic khác biệt.
- **Giá 1 gói, mở hết.** 79 USD / tháng, hoặc 49 USD / tháng nếu trả theo năm. Có chương trình affiliate 30% định kỳ.
- **Trang `/tools`.** Mới có 1 tool (App Pricing Calculator, giá theo sức mua 190+ nước), không cần đăng ký. Trang tool
  có tiêu đề đúng cụm người ta gõ, 3 bước dùng, FAQ, rồi nút "Try appkittie Free".
- **Không có blog, không có `sitemap.xml`, không có `llms.txt`.** File `robots.txt` chặn GPTBot, ClaudeBot, Google-Extended.
  Dù vậy, link anh mở có `utm_source=chatgpt.com`, và một lời khen trên trang kể ChatGPT đã giới thiệu họ. Có vẻ họ được
  AI nhắc tới vì nhiều người nói về họ, không phải nhờ bài viết.

**ShotMatic khác ở đâu (dùng khi viết landing):** trả 1 lần 39,99 USD so với gói tháng · chạy trên máy, dữ liệu ở máy
người dùng · chấm sức khoẻ niche từ Google Play + App Store + Google Trends. AppKittie có doanh thu ước tính, quảng cáo,
video viral, còn ShotMatic không có, nên đừng so ở mấy chỗ đó.

## Việc

### A · Landing shotmatic.app

- [ ] Viết 3 bản hook theo kết quả (1 câu + 1 dòng liệt kê thứ có), anh chọn 1.
- [ ] Màn đầu: 1 thẻ niche thật đã tra bằng ShotMatic (điểm sức khoẻ, keyword còn trống, đối thủ yếu), ghi ngày tra.
- [ ] Khối giá: 39,99 USD trả 1 lần đặt cạnh gói tháng của 2–3 tool cùng loại. Chỉ ghi giá đọc được trên trang giá chính thức, kèm ngày đọc.
- [ ] Bằng chứng: chưa có số người dùng lớn thì dùng thứ có thật (ảnh màn hình thật, số tự đo). Khi 13 người đã tải trả lời thư, xin 1–2 câu kèm tên app của họ.
- [ ] FAQ ngắn ở cuối trang và lặp lại nút tải.

### B · Guide

- [ ] 12 guide đang có: thêm ảnh chụp app thật nếu thiếu, cuối bài có nút tải (`place=guide:<slug>`) và link sang free tool cùng chủ đề.
- [ ] Trang Hướng dẫn xếp theo việc người dùng muốn làm (tìm niche → kiểm keyword → soi đối thủ → quyết định), không xếp theo tên tính năng.

### C · Free tool

- [ ] Dựng trang `/tools` (tiêu đề dạng "Free App Store & ASO tools"), App Idea Checker là thẻ đầu.
- [ ] Mỗi trang tool theo một khuôn: H1 đúng cụm người ta gõ · chạy không cần đăng ký · 3 bước · FAQ · nút tải ShotMatic.
- [ ] Chỉ làm tool thứ 2 khi App Idea Checker đạt từ 20 lượt chạy trong 4 tuần (luật ở [Audit](../marketing/audit-2026-11-07.md)).
  Ứng viên: App Store keyword difficulty checker, Amazon keyword → app idea (logic có sẵn trong 2 extension ở mục 1).
  Đo từ khoá cho tên tool trước khi làm.

## Không làm trong mục này

- Bài blog mới: chờ số Search Console ([Plan blog](../marketing/plan-blog-seo-geo-2026-11-07.md)).
- Affiliate: để sau khi có đơn thật đầu tiên.
- Tool giá theo nước: AppKittie đã có, làm theo thì không thêm gì.

## Liên quan

[Marketing · 5 hạng mục](../marketing/index.md) · [Audit bán hàng + SEO / GEO](../marketing/audit-2026-11-07.md) ·
[Free tool trên shotmatic.app](../marketing/free-tool.md) · [Đối thủ · AppKittie](../marketing/doi-thu.md#appkittie) ·
Mục 1 · [Extension Chrome](index.md#1-extension-chrome-3-extension-mien-phi) ·
Skill khi làm: `marketing-skills:copywriting`, `marketing-skills:cro`, `marketing-skills:free-tools`
