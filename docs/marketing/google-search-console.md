# 1 · Google Search Console

> Công cụ miễn phí của Google cho biết site đã được index chưa, hiện với từ khoá nào, đứng vị trí mấy và có ai bấm không.
> Đây là nơi duy nhất có số thật từ chính Google.

<span class="chip chip--todo">Đang làm · có số mốc đọc tay ngày 2026-11-08 · chưa nối khoá service account</span>

<div class="box box--goal" markdown>
**Số hiện tại (đọc tay từ Search Console, 3 tháng tới 2026-11-08)**

- **253** lượt hiển thị (khoảng 85 mỗi tháng)
- **1** click
- CTR **0,4%**
- Vị trí trung bình **31,3** (trang 3–4)

So với mốc cần để có 1 đơn mỗi tháng chỉ từ Google (xem mục [Bao nhiêu hiển thị thì ra đơn](#bao-nhieu-hien-thi-thi-ra-on)), lượt hiển thị còn thiếu khoảng 40 lần.
</div>

<div class="box box--goal" markdown>
**Target (đích tự đặt, chỉnh lại sau 28 ngày có số)**

- **Tháng 1:** có số mốc · mọi trang quan trọng đã index · từ khoá `shotmatic` đứng số 1
- **Tháng 3:** 2.000 lượt hiển thị · 40 click · 100 từ khoá có hiển thị · 3 từ khoá trong top 10
- **Tháng 6:** 10.000 lượt hiển thị · 200 click · 300 từ khoá có hiển thị · 15 từ khoá trong top 10 · 3 từ khoá trong top 3
- **Tháng 12:** 30.000 lượt hiển thị · 600 click · 50 từ khoá trong top 10 · 10 từ khoá trong top 3

Mọi số tính theo 28 ngày và không tính từ khoá có chữ `shotmatic`, trừ dòng tháng 1.
</div>

## Nó là gì

Search Console trả lời 4 câu, theo đúng thứ tự Google xử lý một trang:

1. **Google có biết trang này không?** Xem ở báo cáo Sitemaps.
2. **Trang có được đưa vào chỉ mục không?** Xem ở báo cáo Page indexing. Đây là chữ "index".
3. **Trang có hiện ra khi người ta tìm không?** Xem Impressions và Average position.
4. **Có ai bấm không?** Xem Clicks và CTR.

Google định nghĩa [4 con số chính](https://support.google.com/webmasters/answer/7576553) như sau:

- **Impressions:** số lần site xuất hiện trong kết quả tìm kiếm.
- **Clicks:** số lần người ta bấm từ kết quả tìm kiếm vào site.
- **CTR:** clicks chia impressions.
- **Average position:** vị trí trung bình của kết quả cao nhất từ site. Xem theo cả site và theo từng trang sẽ ra số khác nhau, nên đừng so hai kiểu với nhau.

Từ tháng 6/2026 có thêm [báo cáo Generative AI](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports)
cho AI Overview và AI Mode. Google ghi đã mở cho mọi site từ 31/08/2026. Bài giới thiệu chỉ liệt kê lượt hiển thị theo trang,
nước, thiết bị và ngày, không liệt kê từ khoá và click. Vì vậy mục [AEO](aeo.md) vẫn phải kiểm tra tay từng câu.

## Dùng nó có lợi gì

- **Biết sớm nhất bài có chạy không.** Impressions lên trước, click và khách trên GA4 đến sau.
- **Biết bài nào hụt ở đâu.** Chưa index, có hiển thị mà đứng thấp, hay đứng cao mà ít bấm, mỗi loại cần cách sửa khác nhau.
- **Tìm từ khoá sắp lên.** Từ khoá đứng vị trí 8–20 là chỗ sửa ít mà được nhiều nhất.
- **Biết bài nào cần bỏ.** Sau 3 tháng không có hiển thị thì gộp bài đó vào bài khác hoặc viết lại.
- **Biết Google đã đọc lại site chưa.** Site này từng là tool screenshot, nên điều này quan trọng.

## Index bao nhiêu là ổn

**Không đuổi theo 100%.** Google xếp ["100% coverage" vào mục không nên nhắm tới](https://support.google.com/webmasters/answer/7440203),
vì chỉ trang chuẩn (canonical) mới cần được index. Trang trùng không được index là bình thường.

Nên tách làm 2 nhóm:

- **Trang quan trọng phải index 100%:** trang chủ, `/app-idea-checker`, `/app-store-keyword-research`, `/app-competitor-analysis`, `/download`, `/scorecard`, `/features` và các bài trụ.
- **Bài blog còn lại:** lần đầu chỉ cần đo tỉ lệ. Hiện có 85 bài đã đăng, 66 bài dưới 600 từ, 74 bài lên trong 3 ngày (đo 2026-11-07). Nếu nhiều bài rơi vào `Crawled - currently not indexed` thì đó là tín hiệu nên bồi hoặc gộp bài, không phải cứ gửi lại URL.

Hai trạng thái dễ nhầm:

- **`Discovered - currently not indexed`:** Google biết trang nhưng chưa ghé. Thường do trang nằm sâu, thiếu link nội bộ.
- **`Crawled - currently not indexed`:** Google đã đọc nhưng chưa đưa vào chỉ mục. Google ghi rằng việc này phổ biến và không phải lúc nào cũng là lỗi, nên chỉ kiểm tra các trang quan trọng.

## Vị trí nào thì ra click

Các nghiên cứu CTR lệch nhau rất nhiều. [Một số blog SEO](https://seocrawl.ai/blog/click-through-rate) ghi vị trí 1 khoảng 22–40%, còn
[Ahrefs đo trên dữ liệu Search Console tháng 12/2025](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/) chỉ còn **3,9%** với từ khoá thông tin và **1,6%** khi có AI Overview.

Blog ShotMatic chủ yếu là từ khoá thông tin, nên target ở đầu trang giả định CTR toàn site khoảng **2%**: 10.000 lượt hiển thị ra 200 click. Mức này vẫn có thể cao, nên sẽ chỉnh sau khi có số thật.

Vì vậy top 1 không có giá trị như nhau ở mọi từ khoá. Top 1 một từ khoá vài chục lượt tìm mỗi tháng kém hơn top 5 một từ khoá vài nghìn lượt tìm, trừ khi người tìm đang sẵn sàng mua.

## Bao nhiêu hiển thị thì ra đơn

Lượt hiển thị không tự ra tiền. Tiền đi qua một phễu:

**Lượt hiển thị × CTR = Click → Click × tỉ lệ mua = Đơn**

Đây là các tỉ lệ thường gặp ở tool SaaS giá thấp (khoảng $5–30/tháng). Chúng chỉ là mốc ước lượng, sẽ thay bằng số thật của GA4 khi có:

- **Hiển thị → Click (CTR toàn site):** 2–4%. Trang này giả định 2% vì blog chủ yếu là từ khoá thông tin.
- **Click → Đăng ký hoặc tải thử:** 3–8%.
- **Dùng thử → Trả tiền:** 10–25%.
- **Gộp lại, Click → Đơn:** khoảng 0,5–2%.

Tính ngược lại:

- **1 đơn** cần khoảng **50–200 click**, tức khoảng **2.500–10.000 lượt hiển thị**.
- **1 đơn mỗi tháng:** khoảng 100 click, tức khoảng 3.000–5.000 lượt hiển thị mỗi tháng.
- **10 đơn mỗi tháng:** khoảng 1.000 click, tức khoảng 30.000–50.000 lượt hiển thị mỗi tháng.
- **100 đơn mỗi tháng:** khoảng 10.000 click, tức hơn 300.000 lượt hiển thị mỗi tháng.

Nếu đạt các target ở đầu trang thì Google đem về khoảng:

- **Tháng 3** (40 click / 28 ngày): **0–1 đơn**. Chưa trông được vào Google.
- **Tháng 6** (200 click / 28 ngày): **1–4 đơn** mỗi tháng.
- **Tháng 12** (600 click / 28 ngày): **3–12 đơn** mỗi tháng.

Vì vậy vài đơn đầu nên đến từ kênh khác như Reddit, Product Hunt, cộng đồng indie dev hay email. Google là kênh tích luỹ dần, thường bắt đầu có hiệu quả sau 3–6 tháng.

**Đọc số 2026-11-08 theo phễu này:**

- Vị trí 31 nghĩa là đang ở trang 3–4, gần như không ai bấm. CTR 0,4% thấp chủ yếu vì vị trí, chưa hẳn do tiêu đề.
- Muốn tăng lượt hiển thị thì cần thêm nhiều trang, mỗi trang nhắm một từ khoá dài và ít cạnh tranh. Muốn tăng click thì đẩy các trang đang ở vị trí 8–20 lên top 5.
- Ngày 2–4/11 lượt hiển thị vọt lên rõ. Đây có vẻ là lúc các bài và trang mới bắt đầu được Google đem đi thử.

## Target này thực tế tới đâu

Ahrefs đo [2 triệu URL mới tạo năm 2023](https://ahrefs.com/blog/how-long-does-it-take-to-rank/): **6,11%** lọt top 10 trong vòng 1 năm, và với trang đã lọt thì 40,82% lọt ngay trong tháng đầu.

Nếu áp vào 85 bài thì chỉ khoảng **5 trang** lọt top 10 trong năm đầu. Một trang có thể đứng top 10 ở nhiều từ khoá, nên 50 từ khoá ở tháng 12 chỉ đạt được khi nhắm vào cụm ít cạnh tranh. Đây là target khó, không phải mức mặc định.

## Làm gì

Đây là ví dụ thứ tự, có thể đổi theo chiến dịch.

**Mở đo**

- [ ] **(Bạn)** Đặt lại file khoá service account và thêm email service account vào property Search Console, quyền đọc ([các bước ở bản cũ](google-analytics.md))
- [ ] **(Bạn)** Bật thêm Bing Webmaster Tools, nhập từ Search Console, vì mục [GEO](geo.md) cần
- [ ] **(Claude)** Kiểm tra sitemap đã gửi chưa. Sitemap thật hiện có 121 URL (đo 2026-11-07)
- [ ] **(Claude)** Ghi số mốc: impressions, click, CTR, vị trí, số trang đã index và lý do trang bị loại

**Mỗi tuần, 15 phút**

- [ ] Xem có trang quan trọng nào rơi khỏi chỉ mục không
- [ ] Lấy danh sách từ khoá vị trí 8–20, chọn tối đa 3 bài để sửa
- [ ] Tìm từ khoá nhiều hiển thị mà CTR thấp hơn mặt bằng cùng vị trí, rồi viết lại tiêu đề và mô tả

**Mỗi 4 tuần**

- [ ] So với 4 tuần trước, ghi 1 dòng vào cuối trang này
- [ ] Đọc thêm báo cáo Generative AI, đưa số sang mục [AEO](aeo.md)

<div class="box box--example" markdown>
**Ví dụ · chiến dịch "AI kiểm ý tưởng app"**

Lọc Search Console theo các từ khoá chứa `validate`, `validator`, `app idea`, `idea checker`.

- **Trong 28 ngày đầu:** trang `/app-idea-checker` được index và có hiển thị cho `app idea checker`.
- **Tháng 3:** `app idea checker` hoặc `app idea validator` vào top 20.
- **Tháng 6:** một trong hai từ khoá vào top 5, và `validate your app idea` vào top 20.

Cả 3 cụm trên đều có trong gợi ý Google (đo 2026-11-07). Gợi ý chỉ cho biết có người gõ, không cho biết bao nhiêu người.
</div>

## Số đo mỗi 4 tuần

**2026-11-07 (mốc):** impressions `chưa đo` · click `chưa đo` · số trang đã index `chưa đo` · từ khoá top 10 `chưa đo`. Lý do: thiếu file khoá service account.

**2026-11-08 (mốc đọc tay, khung 3 tháng chứ không phải 28 ngày):** 253 lượt hiển thị · 1 click · CTR 0,4% · vị trí trung bình 31,3 · số trang đã index `chưa đo` · từ khoá top 10 `chưa đo`.

Các từ khoá có nhiều lượt hiển thị nhất trong 3 tháng:

- `shotmatic`: 25
- `free google play store keyword tool`: 9
- `play store keyword tool free`: 7
- `google adwords niche finder`: 6
- `google trends niches scraper`: 6
- `free app keyword tool`: 6
- `app store keyword tool free`: 6

Nhiều từ khoá có chữ **free**, tức người tìm muốn một công cụ miễn phí. Các trang tool demo miễn phí (`/app-store-keyword-research`, `/app-idea-checker`) hợp với nhu cầu này nhất.

## Liên quan

[2 · Google Analytics](ga4.md) · [4 · SEO](seo.md) · [3 · AEO](aeo.md)
