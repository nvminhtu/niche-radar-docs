# 3 · AEO (Answer Engine Optimization)

> Làm cho site được nêu trong **câu trả lời có sẵn trên Google**: AI Overview, AI Mode, featured snippet. Người tìm đọc
> được đáp án ngay, nên đích là tên và link của mình nằm trong đáp án đó.

<span class="chip chip--todo">Chưa làm · chưa đo mốc 10 câu</span>

<div class="box box--goal" markdown>
**Target với bộ 10 câu (đích tự đặt, đo trên Google US)**

- **Tháng 1:** có số mốc · biết câu nào có AI Overview, câu nào không · báo cáo Generative AI có số
- **Tháng 3:** được trích ở 1 câu
- **Tháng 6:** được trích ở 3 câu
- **Tháng 12:** được trích ở 5 câu, trong đó 2 câu là nguồn đầu tiên

"Được trích" nghĩa là shotmatic.app nằm trong phần nguồn của câu trả lời, ở ít nhất 3 trong 5 lần kiểm tra.
</div>

## Có top 1 hết cả 10 câu được không

**Không nên đặt đích đó.** Lý do:

- Google ghi rõ [không đảm bảo trang được hiển thị](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), kể cả khi làm đúng mọi thứ.
- Câu trả lời AI thay đổi giữa các lần hỏi, nên "top 1" chỉ đo được theo tỉ lệ, không đo được một lần là xong.
- Một số câu không có AI Overview. Câu đó thì không có gì để lên top.
- Site mới cạnh tranh với AppTweak, Appfigures, Sensor Tower, những site có nhiều năm tuổi.

Đích thực tế là đứng đầu ở **câu rất hẹp, nơi ShotMatic có số riêng mà người khác không có**.

## Nó là gì

Các tên gọi này chưa có định nghĩa thống nhất. [Nhiều nguồn dùng AEO và GEO lẫn lộn](https://en.wikipedia.org/wiki/Generative_engine_optimization). Trong docs này, để dễ giao việc, quy ước:

- **AEO:** bề mặt của Google, gồm AI Overview, AI Mode, featured snippet, People Also Ask.
- **[GEO](geo.md):** công cụ chat AI khác, gồm ChatGPT, Perplexity, Gemini, Copilot.

Google tự xem việc này [vẫn là SEO](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), vì AI Overview và AI Mode dựa trên hệ thống xếp hạng của Search. Do đó AEO không có mẹo riêng: mục [SEO](seo.md) yếu thì AEO cũng yếu.

Đứng top 10 giúp ích nhưng không đủ. Tỉ lệ nguồn của AI Overview cũng nằm trong top 10 lệch nhiều giữa các nghiên cứu: [Ahrefs 38%](https://news.designrush.com/ai-overview-citations-drop-ahrefs), [Surfer 52%](https://surfer.ai/blog/ai-overviews-study/), một phân tích của BrightEdge khoảng 17%. Không có một con số chốt.

## Vì sao nên làm

- Khi có AI Overview, [CTR của kết quả đứng đầu thấp hơn khoảng 58%](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/) so với dự báo (Ahrefs, 12/2025, số tương quan), nên đứng top thôi chưa chắc có khách.
- Được nêu trong câu trả lời thì vẫn có người biết tên, kể cả khi họ không bấm.
- Làm tốt AEO cũng giúp GEO, vì cùng cần nội dung rõ và có số riêng.

## Làm gì để được trích

Theo hướng dẫn của Google, cộng với phần đo được trên site:

**Điều kiện bắt buộc**

- [ ] Trang đã index và được phép hiện snippet. Kiểm tra ở [Search Console](google-search-console.md)
- [ ] Nội dung chính đọc được không cần chạy JavaScript phức tạp, không bị trùng lặp nhiều
- [ ] Site có mặt trong báo cáo Generative AI của Search Console. Google nêu đây là điều kiện

**Nội dung Google ưu tiên**

- [ ] **Có góc nhìn thực tế và thông tin riêng.** Đây là lợi thế lớn nhất: số đo thật từ ShotMatic, ví dụ top 10 App Store của `pet medication tracker` có 8 app dưới 1.000 rating, 7 app ra trong 24 tháng (đo 2026-11-07)
- [ ] **Trả lời ngay đầu bài**, rồi mới giải thích. Khung câu trả lời ngắn trên blog đã có sẵn, giữ lại
- [ ] **Một bài trụ trả lời trọn một chủ đề.** Google tách câu hỏi thành nhiều câu nhỏ để tìm, nên một bài phủ cả các ý phụ dễ được chọn hơn
- [ ] **Thêm hình và video thật**, ví dụ ảnh chụp kết quả trong app

**Những điều Google bảo đừng làm**

- [ ] **Đừng cắt bài thành mẩu nhỏ** chỉ để AI đọc
- [ ] **Đừng viết nhiều trang cho từng biến thể câu hỏi.** Google xếp việc này vào lỗi nội dung hàng loạt. Điều này liên quan trực tiếp tới 137 bài đã đăng và đã hẹn lịch
- [ ] **Đừng trông vào `llms.txt` cho Google.** Google nói Search không dùng file này. Vẫn giữ vì có thể có ích với công cụ khác
- [ ] **Đừng tạo lượt nhắc giả** trên web

Schema không bắt buộc cho AI search theo Google, nhưng vẫn giữ vì có ích cho kết quả tìm kiếm thường.

## Cách đo

- **Báo cáo Generative AI trong Search Console:** cho biết trang nào được hiển thị, bao nhiêu lần. Bài giới thiệu không liệt kê từ khoá, nên không biết chính xác ở câu nào.
- **Kiểm tra tay bộ 10 câu, mỗi 4 tuần:** mỗi câu 5 lần, ở cửa sổ ẩn danh, ghi rõ nước đo. Ghi: có AI Overview không, mình có trong nguồn không, ai đang được trích.
- **Ai được trích thì đọc người đó.** Trang của họ có gì mà bài mình không có? Đó chính là việc cần sửa.

<div class="box box--example" markdown>
**Ví dụ · bộ 10 câu cho chiến dịch "AI kiểm ý tưởng app"**

Đổi chiến dịch thì đổi bộ câu. Giữ nguyên 10 câu trong suốt một đợt đo để số so được với nhau. Có 2 câu được gợi ý Google xác nhận: `validate your app idea` và `app idea checker` (đo 2026-11-07). Các câu còn lại do tôi đề xuất theo cách người dùng hỏi, chưa đo.

1. how to validate an app idea before building
2. free app idea checker
3. how do I know if my app idea is good
4. how to find a low competition app niche
5. how to do app store keyword research for free
6. how to analyze app competitors on the App Store
7. how to use Google Trends for an app idea
8. how many ratings means an app niche is too crowded
9. free alternative to Sensor Tower for indie developers
10. how to read bad app reviews to find a feature gap

**Câu có cơ hội đứng đầu nhất:** câu 8 và câu 10, vì có thể trả lời bằng số tự đo.

**Câu khó nhất:** câu 5 và câu 9, vì vendor lớn đang chiếm.
</div>

## Số đo mỗi 4 tuần

**2026-11-07 (mốc):** số câu có AI Overview `chưa đo` · số câu được trích `chưa đo` · hiển thị trong báo cáo Generative AI `chưa đo`.

## Liên quan

[4 · SEO](seo.md) · [5 · GEO](geo.md) · [1 · Google Search Console](google-search-console.md)
