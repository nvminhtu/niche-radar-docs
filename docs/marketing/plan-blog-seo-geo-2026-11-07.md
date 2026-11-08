# Plan blog SEO + GEO từ Google Trends (2026-11-07)

> Luồng: Google Trends → chọn cụm → đo bằng ShotMatic → lập danh sách bài. Trang này ghi số đo ngày 2026-11-07 và thứ tự
> việc. Thứ tự tổng của việc bán vẫn theo Audit 2026-11-07 (link ở cuối trang).

<span class="chip chip--doing">Đo 2026-11-07 · Search Console chưa đọc được · Google Play chưa đo xong</span>

<div class="box box--goal" markdown>
**Kết luận**

- **Top 1 làm được ở cụm đuôi dài, chưa thực tế ở cụm lớn.** `aso keyword research` và `best aso tools` đang do blog của vendor ASO chiếm.
- **Chưa biết site đang đứng hạng mấy.** Không đọc được Search Console vì thiếu file khoá. Việc đầu tiên là mở lại phần đo.
- **Bước 3 cần đổi một chút:** ShotMatic đo được niche app, không đo được từ khoá blog. Từ khoá blog dùng để chọn đề tài, niche app mới là thứ đưa vào ShotMatic để lấy số.
- **Lợi thế GEO là bộ số tự đo.** Bài ASO chung chung đã có quá nhiều, AI search khó có lý do để trích thêm một bài nữa.

**Xong khi:** có số Search Console tuần 0 · 5 bài đợt 1 và 6 bài viết lại đã lên, mỗi bài có số tự đo · đã đo mốc 5 câu hỏi trên AI search.
</div>

## 1. Google Trends cho thấy gì?

Nguồn: Google Trends, US, 12 tháng, đo 2026-11-07. Mỗi nhóm so riêng với mốc `pomodoro timer`. Số chỉ so được trong cùng nhóm, không cộng hay so giữa các nhóm.

| Cụm | Đỉnh 12 tháng | Tuần 2026-11-01 | Mốc pomodoro cùng tuần | Đọc thế nào |
|---|---|---:|---:|---|
| `app ideas` | 100 | 22 | 13 | Cụm lớn nhất trong nhóm ý tưởng |
| `niche research` | 15 | 2 | 13 | Nhỏ |
| `app idea validation` | 0 | 0 | 13 | Dưới ngưỡng Trends |
| `aso keywords` | 1 | 0 | 13 | Dưới ngưỡng Trends |
| `keyword research` | 100 | 22 | 37 | Có nhu cầu, nhưng là SEO chung |
| `startup ideas` | 62 | 8 | 37 | Rộng hơn app |
| `app store optimization` | 28 | 2 | 37 | Có thật, nhỏ |
| `business idea validation` | 3 | 0 | 37 | Gần như không có |
| `google trends api` | 79 | 1 | 67 | Đỉnh tháng 6, đã tụt |
| `google trends alternative` | 10 | 0 | 67 | Nhỏ |
| `idea validation` | 15 | 4 | 67 | Nhỏ |
| `validate idea` | 12 | 3 | 67 | Nhỏ |

Query đang tăng đáng dùng: `trending and relevant app ideas`, `mobile app ideas`, `how to stop app tracking on iphone`. Phần lớn còn lại là rác, ví dụ `lidl near me` và `sports scores today`. Riêng `aso` trên Trends toàn kết quả về nẹp cổ chân và núi Aso, nên phải đo bằng `app store optimization`.

### Cú tụt từ giữa tháng 7/2026 là gì?

Từ tuần 2026-07-12, hầu hết các cụm trên tụt mạnh cùng lúc, còn `pomodoro timer` không tụt. Cụm đối chứng `seo` cũng giảm (58 tuần 07-05, 20 tuần 11-01, dải 5 năm).

Chưa rõ nguyên nhân: có thể người tìm giảm thật, chuyển sang hỏi AI, hoặc Google đổi cách tính. **Chưa đo được, nên chưa dùng làm kết luận.** Đừng viết bài kiểu "nhu cầu đang chết". Search Console sẽ kiểm tra được phần này.

## 2. ShotMatic đo được gì?

Nguồn: ShotMatic Research #242–#249 và `store_check` (top 10 App Store US), đo 2026-11-07.

**Từ khoá blog không dùng được làm input.** `app idea` trả về Pinterest, FaceApp, Airbnb. `business idea` trả về Pinterest, Wayfair. Hai lượt này không nói gì về thị trường tool kiểm ý tưởng.

**Niche thật thì có số dùng được.** `Yếu` là số app dưới 1.000 rating trong top 10. `Mới` là số app ra trong 24 tháng.

| Keyword | Tổng rating top 10 | App ≥ 1k rating | Yếu | Mới |
|---|---:|---:|---:|---:|
| `home workout` | 1.064.397 | 9 | 0 | 0 |
| `meal planner` | 430.697 | 8 | 0 | 2 |
| `meal prep for one` | 33.945 | 5 | 3 | 1 |
| `vegetable garden planner` | 144.895 | 5 | 4 | 1 |
| `raised bed planner` | 78.202 | 6 | 4 | 2 |
| `dog medication reminder` | 104.369 | 5 | 5 | 3 |
| `pet medication tracker` | 11.139 | 1 | 8 | 7 |

Điều đọc được: **thu hẹp cụm thì top 10 yếu đi rõ rệt.** `pet medication tracker` là ví dụ mạnh nhất. Đây chỉ là tín hiệu cạnh tranh, chưa chứng minh có nhu cầu hay có tiền.

Giới hạn của lượt đo này:

- **Google Play chưa đo xong.** Cả 8 lượt đều lỗi `interrupted` vì dev server tự khởi động lại khi có code đang được sửa. `Play 0` trên thẻ nghĩa là không đo được, không phải không có đối thủ.
- **Điểm BỎ của `meal prep planner`, `garden planner`, `pet care` chưa phải kết luận.** Mỗi lượt chỉ đo được 40% trọng số.
- **`home workout` và `tracker blocker` chưa có số trong ShotMatic.** Hai lượt #248, #249 bị ngắt giữa chừng; số trong bảng lấy từ `store_check`.
- **Trends trong ShotMatic bị chặn** ở các lượt #245–#247 (Google tạm chặn, HTTP 429).

## 3. Top 1 thực tế ở đâu?

Nguồn: một lượt xem kết quả tìm kiếm bằng công cụ web, 2026-11-07. Đây không phải đo hạng trên Google, chỉ để đánh giá mặt bằng đối thủ.

| Cụm | Đang chiếm kết quả | Cơ hội |
|---|---|---|
| `how to do keyword research for aso` | AppTweak, Appfigures, MobileAction | Thấp. Viết lại bài cũ, không nhắm top 1 |
| `best aso tools` | AppFollow, Sonar, ASOMobile | Thấp. Skill blog cũng cấm so sánh tool chưa tự thử |
| `how much does app store optimization cost` | Agency và vendor bán dịch vụ | Trung bình. Thiếu góc nhìn của người làm một mình |
| `how to come up with app ideas` | Agency, bài Medium cũ | Trung bình. Chưa ai có số thật |
| `how to sell app ideas` | Agency, bài chép lại nhau | Khá. Câu trả lời thật là "gần như không bán được", agency ít nói thẳng |
| `why does google trends data change` | Forum cũ, trang hỗ trợ của vendor | Khá. Có ca thật để phân tích |
| `how to validate micro saas idea` | Newsletter, blog nhỏ, trang bán playbook | Khá |
| `app idea validator` | Toàn trang tool | Dùng free tool, không dùng bài viết ([mục 5 của Audit](audit-2026-11-07.md)) |

Công cụ tìm kiếm trong lượt này chỉ thấy **đúng một trang** của shotmatic.app, và vẫn mô tả là tool screenshot cũ. Khớp với điều Audit ghi về Bing. Cần xác nhận lại bằng Search Console.

## 4. Thứ tự việc

### Bước 0 · Mở đo số và mở đường cho bot (làm trước khi viết)

- [ ] **(Bạn)** Đặt lại file khoá service account, thêm email service account vào Search Console + GA4 ([các bước](google-analytics.md))
- [ ] **(Claude)** Gửi `sitemap.xml`, soát số bài đã index, ghi số mốc tuần 0: impressions, click, hạng trung bình theo query
- [ ] **(Bạn)** Cloudflare: tắt managed robots.txt, cho `PerplexityBot` đi qua
- [ ] **(Bạn)** Bing Webmaster Tools: nhập từ Search Console, gửi sitemap. Công cụ AI search có thể lấy dữ liệu từ Bing, nên mô tả cũ ở đây đáng sửa
- [ ] **(Claude)** Thêm IndexNow khi deploy, thêm `sameAs` vào schema khi có link hồ sơ

### Bước 1 · Đo lại cho sạch

- [ ] **(Bạn)** Chọn lúc không có ai sửa `web/src`, hoặc chạy trên app đã build, để dev server không tự khởi động lại
- [ ] **(Claude)** Chạy lại khoảng 30 niche theo từng cặp cụm rộng / cụm hẹp, đủ Play + App Store + Trends, 3 lượt một lần
- [ ] **(Claude)** Đọc review 1–3★ của các niche có triển vọng, vì hiện phần nỗi đau chưa đo

ShotMatic trả lại lượt cũ nếu tra lại cùng keyword trong 24 giờ, nên các keyword đã tra hôm nay chỉ chạy lại được từ 2026-11-08.

### Bước 2 · Viết lại 6 bài mỏng (làm trước bài mới)

Audit ghi trung vị thân bài là 409 từ, trong khi skill blog đặt sàn 1.200 từ. Thêm bài mỏng không giúp được gì.

| Bài | Số từ | Việc cần làm |
|---|---:|---|
| `what-is-app-store-optimization` (hẹn 2027-01-11) | 368 | Viết lại trước ngày lên |
| `app-idea-generator` | 397 | Thêm bảng số thật |
| `is-my-app-idea-good` | 466 | Dùng bộ số đo ở Bước 1 |
| `best-app-niche-research-tools-2026` | 513 | Tự thử từng tool, chưa thử thì bỏ khỏi bảng |
| `niche-radar-feature-tour` | 601 | Đổi tên sang ShotMatic, đúng tính năng hiện có |
| `find-your-niche-before-you-build` | 787 | Bài trụ của cụm niche, cần sâu hơn |

Các bài đã trên 1.400 từ (`validate-app-idea-before-you-build`, `google-trends-find-a-niche`, `app-store-keyword-research-free`) chỉ cần cập nhật số khi có dữ liệu Search Console.

Sửa thêm cột `covered_by` của hàng chờ vì đang khớp sai. Ví dụ `how to find app ideas` trỏ vào `android-app-ideas`, còn `how to choose a niche` trỏ vào bài subscription. Nhờ vậy mới thấy `how to find app ideas` thật ra chưa có bài riêng.

### Bước 3 · Viết 5 bài đợt 1

Bài nào cũng đi đủ 5 bước của skill blog, gồm đo Trends 5 năm có mốc và số tự đo. Các cụm dưới đây có trong Autocomplete nhưng chưa đo riêng trên Trends, sẽ đo khi viết; nếu = 0 thì ghi `below Trends threshold`.

**Bài 1 · Bài dữ liệu trụ: cụm rộng và cụm hẹp khác nhau bao nhiêu trên store**

- **Mục tiêu:** GEO và backlink, không nhắm một keyword cụ thể
- **Số:** khoảng 30 cặp niche, đủ 2 store, đăng kèm bảng và cách đo
- **Vì sao đứng đầu:** các bài sau đều lấy số từ đây. AI search cần con số có nguồn để trích

**Bài 2 · How to come up with app ideas**

- **Keyword:** `how to come up with app ideas` · phụ: `how to get app ideas`, `where can i find app ideas`
- **Góc:** đi từ cụm rộng tới cụm hẹp bằng số thật, thay cho danh sách ý tưởng chung chung
- **Dẫn về:** bài dữ liệu, `validate-app-idea-before-you-build`

**Bài 3 · Can you sell an app idea?**

- **Keyword:** `how to sell app ideas` · phụ: `can i sell app ideas`, `where can i sell my app ideas`, `can you protect an app idea`
- **Góc:** trả lời thẳng rằng người mua trả tiền cho bằng chứng và sản phẩm, rồi chỉ cách tạo bằng chứng
- **Lưu ý:** phần pháp lý chỉ dẫn nguồn chính thức, khuyên hỏi luật sư. Chính sách của Apple phải đọc từ trang của Apple

**Bài 4 · Why Google Trends data changes (and what to do when it shows nothing)**

- **Keyword:** `why does google trends data change` · phụ: `google trends not showing data`, `google trends not working`
- **Góc:** dùng ca cú tụt tháng 7/2026, ghi rõ phần chưa giải thích được. Giải thích về 429 và ngưỡng dữ liệu
- **Dẫn về:** `is-google-trends-accurate`, phải khác ý với bài này để không tranh hạng nhau

**Bài 5 · How much does ASO cost for an indie app?**

- **Keyword:** `how much does app store optimization cost` · phụ: `app store optimization free tools`
- **Góc:** ngân sách cho người làm một mình, từ 0 đồng tới khi nào đáng trả tiền
- **Lưu ý:** mọi mức giá phải đọc từ trang giá chính thức trong ngày viết. Bài này gần chuyện mua nhất, dẫn về trang giá

**Để dành đợt 2** (quyết định sau khi có số Search Console): `how to validate micro saas idea` · `best google trends alternatives` (chỉ khi đã tự thử từng tool) · `how to do niche research` · `how to find a niche market`.

**Chưa viết:** các cụm `niche research` cho YouTube, Etsy, KDP. Có người tìm, nhưng phải xác nhận ShotMatic giải được đúng việc đó, kể cả KDP với Scout, trước khi nhận viết.

### Bước 4 · Khuôn GEO cho mọi bài

- `answer` 40–60 từ ở đầu bài, trả lời được khi tách riêng
- H2 dạng câu hỏi, FAQ ngắn, `evidence` có nguồn và ngày đo
- Ít nhất một bảng số tự đo, ghi rõ giới hạn của số đó
- Luôn gọi là "ShotMatic, app niche research" vì tên đang trùng với nhiều sản phẩm khác
- Không đăng lại bài chỉ bằng cách đổi `date`

### Bước 5 · Đo và quyết định sau mỗi 28 ngày

| Tình huống trong Search Console | Việc làm |
|---|---|
| Chưa được index | Kiểm tra kỹ thuật, gộp bài trùng ý, chưa viết thêm |
| Có impressions, hạng 11–30 | Viết sâu hơn, thêm link nội bộ |
| Hạng 4–10 | Sửa tiêu đề và mô tả, thêm số mới |
| Hạng 1–3 | Giữ số luôn mới, dẫn link sang trang tải |
| Không có impressions sau 2 chu kỳ | Xét gộp hoặc bỏ |

GEO: mỗi tháng hỏi 5 câu cố định trên ChatGPT, Perplexity, Gemini và ghi lại có được nhắc tên hay không ([AEO / GEO](aeo-geo.md)). Traffic chỉ là chặng giữa, nên theo dõi đến lượt tải và đơn PRO.

## Quyết định cần chốt

**Đã chốt 2026-11-07: giữ quy tắc "ngừng bài mới cho tới khi có số Search Console".** Làm Bước 0 trước, chưa viết đợt 1.

Trạng thái Bước 0 đo cùng ngày: file khoá vẫn thiếu. `PerplexityBot` và `ClaudeBot` trả 403. `GPTBot`, `OAI-SearchBot`, `Bingbot`, `Googlebot` trả 200 (curl đổi User-Agent, bot thật có thể bị xử lý khác). `sitemap.xml`, `robots.txt`, `llms.txt` đều trả 200.

**Có cho 74 bài đã hẹn tiếp tục lên không?** Nhiều bài trong đó có thể mỏng, ví dụ `what-is-app-store-optimization` chỉ 368 từ. Đề xuất: khi có số index, xem lại những bài dưới 1.200 từ trước khi cho lên tiếp.

## Nguồn tham khảo

- Trang đối thủ về cách làm keyword: [Appfigures](https://appfigures.com/resources/guides/keyword-research), [AppTweak](https://www.apptweak.com/en/aso-blog/10-tips-to-find-the-perfect-keywords), [MobileAction](https://www.mobileaction.co/blog/aso-keyword-research/)
- Trang đối thủ về công cụ và chi phí: [AppFollow](https://appfollow.io/blog/keywords-tools-for-aso), [Sonar](https://trysonar.app/blog/best-free-aso-tools), [AppFollow · chi phí ASO](https://appfollow.io/blog/app-store-optimization-cost)
- Trang đối thủ về ý tưởng: [Cleveroad](https://www.cleveroad.com/amp/blog/how-to-come-up-with-an-app-idea-and-make-sure-it-is-valid/), [MobileAction · bán ý tưởng](https://www.mobileaction.co/blog/how-to-sell-an-app-idea/), [Indie Hackers · kiểm micro SaaS](https://www.indiehackers.com/post/how-i-validated-my-micro-saas-idea-quickly-and-you-can-too-53decf45b9)

## Liên quan

[Audit 2026-11-07](audit-2026-11-07.md) · [AEO / GEO](aeo-geo.md) · [Google Analytics + Search Console](google-analytics.md) · [Free tool](free-tool.md)
