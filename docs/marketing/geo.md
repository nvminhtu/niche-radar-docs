# 5 · GEO (Generative Engine Optimization)

> Làm cho **ChatGPT, Perplexity, Gemini, Copilot** nhắc tới ShotMatic khi có người hỏi: "Tool nào để kiểm ý tưởng app?".
> SEO nhắm tới danh sách link. GEO nhắm tới việc được AI gọi tên trong câu trả lời.

<span class="chip chip--todo">Chưa làm · còn bot bị chặn · chưa đo mốc 10 câu</span>

<div class="box box--goal" markdown>
**Target với bộ 10 câu (đích tự đặt)**

Đo trên ChatGPT search, Perplexity, Gemini. Mỗi câu chạy 5 lần trên mỗi công cụ. "Được nhắc" là có tên ShotMatic ở ít nhất 3 trong 5 lần.

- **Tháng 1:** hết bot bị chặn · có số mốc · hỏi "ShotMatic là gì" thì AI trả lời đúng, không nói là tool screenshot
- **Tháng 3:** được nhắc ở 2 câu, trên ít nhất 1 công cụ
- **Tháng 6:** được nhắc ở 4 câu · đứng đầu ở 1 câu trên ChatGPT search · 50 khách / 28 ngày từ kênh AI
- **Tháng 12:** được nhắc ở 6 câu · đứng đầu ở 3 câu · có đơn PRO đầu tiên từ kênh AI

"Đứng đầu" là tên đầu tiên AI gợi ý, ở ít nhất 3 trong 5 lần.
</div>

## Nó là gì

Khi bạn hỏi ChatGPT có bật tìm kiếm, nó thường làm 3 bước:

1. Tự tách câu hỏi thành vài câu tìm kiếm.
2. Đọc một số trang tìm được.
3. Viết câu trả lời và có thể dẫn nguồn.

GEO là làm cho mình lọt qua cả 3 bước. Tên gọi này đến từ [một nghiên cứu của Princeton và cộng sự](https://arxiv.org/abs/2311.09735), đăng ở hội nghị KDD 2024.

Nên hiểu 4 nấc, từ dễ tới khó:

1. **Được đọc:** bot AI vào được trang.
2. **Được dẫn nguồn:** AI dùng trang làm tài liệu tham khảo.
3. **Được nhắc tên:** ShotMatic xuất hiện trong câu trả lời.
4. **Được gợi ý:** AI khuyên dùng ShotMatic. Đây mới là thứ ra đơn.

Được dẫn nguồn chưa chắc được gợi ý. AI có thể đọc bài của mình rồi vẫn khuyên dùng đối thủ.

## GEO khác SEO chỗ nào

- **Kết quả:** SEO cho một vị trí. GEO cho một lần được nhắc, và mỗi lần hỏi một khác.
- **Chỗ cần xuất hiện:** SEO chủ yếu xét site của mình. GEO xét cả việc **người khác nói gì về mình**.
- **Cách đo:** SEO có Search Console. GEO chủ yếu đo tay. Riêng Copilot có [báo cáo AI Performance trong Bing Webmaster Tools](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/), cho biết số lần được trích và câu hỏi mẫu.

## Mỗi công cụ cần gì

- **ChatGPT search:** phải cho [`OAI-SearchBot`](https://developers.openai.com/api/docs/bots) vào. Bot này đang trả 200, tốt. `GPTBot` chỉ dùng để huấn luyện và độc lập với search, nên chặn nó không làm site mất khỏi ChatGPT search.
- **Perplexity:** dùng bot riêng. `PerplexityBot` đang **bị 403**, nên đây là chỗ chặn cần sửa đầu tiên.
- **Copilot:** dựa nhiều vào Bing. Bing vẫn mô tả site là tool screenshot cũ (đo 2026-11-07), nên phải sửa qua Bing Webmaster Tools.
- **Gemini:** dựa trên hệ sinh thái của Google. `Google-Extended` đang bị chặn. Google nói token này không ảnh hưởng tới Google Search, nhưng nó có ảnh hưởng tới một số cách Gemini dùng nội dung, nên cần bạn quyết định.
- **Claude:** `Claude-SearchBot` đang trả 200.

## Bước 1 · Mở đường cho bot

Đo 2026-11-07 trên site thật. curl chỉ giả User-Agent nên bot thật có thể bị xử lý khác.

- **403:** `PerplexityBot`, `GPTBot`, `ClaudeBot`
- **200:** `OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot`, `Googlebot`, `bingbot`
- **robots.txt đang tự mâu thuẫn:** khối Cloudflare tự chèn ở đầu file cấm `ChatGPT-User`, `Claude-User`, `Perplexity-User`, trong khi phần của mình ở dưới lại cho phép. Bot nào đọc theo khối đầu thì sẽ không vào.

Việc cần làm:

- [ ] **(Bạn)** Cloudflare: tắt managed robots.txt của domain này
- [ ] **(Bạn)** Cloudflare: cho `PerplexityBot` đi qua luật chặn bot AI
- [ ] **(Bạn)** Quyết `GPTBot`, `ClaudeBot`, `Google-Extended`. Đề xuất cho phép trên site marketing, vì mục tiêu là được biết tới và các trang này không có gì cần giữ
- [ ] **(Bạn)** Bing Webmaster Tools: nhập từ Search Console, gửi sitemap, bật báo cáo AI Performance
- [ ] **(Claude)** Đo lại mọi bot sau khi sửa, ghi vào cuối trang này

## Bước 2 · Làm cho AI hiểu đúng ShotMatic là ai

Tên "ShotMatic" đang trùng với **Shotmatic** (video AI), **Shotomatic** (chụp màn hình Mac) và chính bản screenshot cũ của domain này.

- [ ] Dùng một câu giống nhau ở mọi nơi: "ShotMatic, a Mac app for app niche research"
- [ ] Dùng câu đó ở trang chủ, `llms.txt`, Chrome Web Store, GitHub, mọi hồ sơ
- [ ] Thêm `sameAs` vào schema khi có link hồ sơ
- [ ] Kiểm tra: `llms.txt` đang ghi "version 1.0". Cập nhật khi có bản 1.1.0

## Bước 3 · Làm cho nội dung đáng trích

Nghiên cứu GEO thử 9 cách trên 10.000 câu hỏi trong môi trường thử nghiệm:

- **Hiệu quả nhất:** dẫn nguồn, thêm trích dẫn, thêm số liệu, tăng khoảng 30–40% độ hiển thị.
- **Không hiệu quả:** nhồi từ khoá, không hơn mức gốc.
- **Site xếp thấp được lợi nhiều hơn**, theo bảng kết quả của bài báo.

Đây là thử nghiệm năm 2023–2024, nên chỉ xem như hướng đi, không xem như con số sẽ đạt được.

- [ ] Mỗi trang quan trọng có số tự đo, ngày đo, nguồn dẫn
- [ ] Trang chủ, `/features`, `/terms` nói rõ làm gì, giá bao nhiêu, cho ai. AI so sánh sản phẩm dựa vào các trang chính thức này
- [ ] Có trang so sánh trung thực: ShotMatic so với Appfigures, Sensor Tower, chỉ viết khi đã tự thử
- [ ] Làm một bộ dữ liệu riêng mà người khác muốn trích, ví dụ độ cạnh tranh của 30 niche nhỏ

## Bước 4 · Được người khác nhắc tới

Đây có lẽ là phần quan trọng nhất. Ahrefs đo [75.000 thương hiệu](https://ahrefs.com/blog/ai-overview-brand-correlation/): số lần thương hiệu được nhắc trên web tương quan với việc được nhắc trong AI Overview ở mức **0,664**, còn số backlink chỉ **0,218**. Đây là tương quan, không phải nguyên nhân, và mẫu là các thương hiệu đã khá lớn.

Cách làm:

- [ ] **Bắt đầu từ đo mốc:** với mỗi câu, ghi AI đang dẫn nguồn từ đâu. Các trang đó chính là danh sách cần có mặt
- [ ] **Reddit, Indie Hackers:** bạn tự trả lời thật, dùng `/reddit-qa` để tìm câu hỏi và viết nháp
- [ ] **AlternativeTo, thư mục tool:** thêm hồ sơ đúng mô tả
- [ ] **Viết thư cho người làm bài "best tools":** xin được thử và được thêm vào. Chỉ làm với bài có thật
- [ ] **YouTube:** video demo thật, có phụ đề và mô tả rõ, vì AI đọc phần chữ của video
- [ ] **Khách đã tải:** xin nhận xét thật, không viết hộ

Không được tạo tài khoản giả, không tự viết review, không spam. Google cũng cấm lượt nhắc giả, và làm vậy còn hại về lâu dài.

## Cách đo

- **Bộ 10 câu, mỗi 4 tuần:** 10 câu × 3 công cụ × 5 lần = 150 lượt. Ghi: có được nhắc không, đứng thứ mấy, ai đứng trước, AI mô tả đúng không, nguồn nào được dẫn.
- **Ghi theo tỉ lệ:** ví dụ "được nhắc 3/5". Một lần hỏi không chứng minh được gì.
- **GA4:** khách từ [kênh AI](ga4.md) và trang họ vào.
- **Bing Webmaster Tools:** số lần được trích trên Copilot.
- **Công cụ trả phí như Otterly, Peec AI:** chưa cần. Khi nào đo tay tốn quá nhiều thời gian mới xem xét.

<div class="box box--example" markdown>
**Ví dụ · bộ 10 câu cho chiến dịch "AI kiểm ý tưởng app"**

Câu hỏi viết theo cách người ta nói với AI, không theo kiểu gõ từ khoá. Đổi chiến dịch thì đổi bộ câu.

1. What's the best AI tool to validate a mobile app idea?
2. I'm a solo developer. How do I check if an app niche is worth building?
3. What are the best free tools to validate an app idea?
4. Which tools show App Store and Google Play competitors for a niche?
5. What are good Sensor Tower alternatives for indie developers?
6. What's a cheap Appfigures alternative for keyword research?
7. Is there a Mac app for app niche research?
8. How do I find low competition app ideas using real data?
9. What is ShotMatic?
10. Is ShotMatic worth buying?

**Đích đứng đầu trên ChatGPT search:** câu 7 ở tháng 6, vì câu rất hẹp và ít đối thủ đúng loại.

**Câu 1, 3, 5 khó nhất:** cần nhiều site khác nhắc tới, nên đừng đặt đích đứng đầu trong năm đầu.

**Câu 9, 10 để kiểm tra độ chính xác:** AI có nói đúng sản phẩm, đúng giá $39.99 không.
</div>

## Số đo mỗi 4 tuần

**2026-11-07 (mốc):** bot như Bước 1 · số câu được nhắc `chưa đo` · khách từ kênh AI `chưa đo` · số lần được trích trên Copilot `chưa đo`.

## Liên quan

[3 · AEO](aeo.md) · [4 · SEO](seo.md) · [2 · Google Analytics](ga4.md) · [Đối thủ](doi-thu.md)
