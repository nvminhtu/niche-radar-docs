# Đánh giá nhận định về AppKittie + Appfigures (2026-11-07)

> Anh nhận một bài phân tích của ChatGPT về AppKittie, Appfigures và thị trường tool tìm app, kèm lời khuyên xây một
> "App Opportunity Radar" 9 module. Trang này kiểm bài đó với trang giá thật và với ShotMatic hiện có, rồi chia việc
> nên làm thành 2 đợt.

<span class="chip chip--todo">Đánh giá 2026-11-07 · đợt A làm ngay · đợt B chờ 10 đơn PRO</span>

<div class="box box--goal" markdown>
**Kết luận**

- **Phần mô tả thị trường phần lớn đúng. Phần khuyên build gì không hợp ShotMatic**, vì ShotMatic đã có gần hết, phần
  còn thiếu là phần tốn tiền nhất, và bài bỏ qua chỗ nghẽn thật là chưa ai biết tới sản phẩm.
- **ShotMatic có đủ 5 / 9 module** bài đề xuất, 2 module có một phần, 2 module chưa có.
- **Không thêm tính năng lúc này** (đã chốt ở [Audit](audit-2026-11-07.md)). Đợt A không cần code, làm ngay. Đợt B
  chỉ mở khi có 10 đơn PRO.

**Xong khi:** đợt A xong cả 5 việc · có 10 đơn PRO thì quay lại chọn 1 việc của đợt B.
</div>

## Bài gốc nói gì

- Appfigures dùng để đo app của chính mình (doanh thu, ASO), AppKittie dùng để soi app đối thủ đang thắng (doanh thu
  ước tính, quảng cáo, video viral, onboarding, paywall).
- Thị trường có nhiều tầng: Sensor Tower cho doanh nghiệp, AppMagic, AppTweak, MobileAction cho ASO.
- Khách sẵn trả $49–79 / tháng vì tìm được 1 app kiếm $5K–50K / tháng đáng hơn nhiều.
- Lời khuyên: đừng làm Appfigures thứ hai. Làm "App Opportunity Radar" 9 module, đi từ tìm cơ hội tới viết PRD, nối
  thêm Reddit, TikTok, Product Hunt.

## Chỗ đúng

- **Hai sản phẩm phục vụ hai việc khác nhau.** Đúng như trang của họ mô tả.
- **Giá AppKittie** 79 USD / tháng, hoặc 49 USD / tháng khi trả năm. Khớp với trang [Đối thủ](doi-thu.md#appkittie)
  đọc cùng ngày.
- **Thang giá Appfigures** khớp với [trang giá](https://appfigures.com/platform/pricing) đọc 2026-11-07: Connect
  9,99 USD · Monitor 44,99 USD · Optimize 149,99 USD · Boost 599,99 USD · Amplify 1.399,99 USD. Trang có 2 dãy số, dãy
  thấp hơn nhiều khả năng là giá khi trả năm. Con số 999,99 USD bài ghi cho Amplify thuộc dãy thấp đó.
- **"Đừng làm Appfigures thứ hai"** là đúng. Họ dùng mô hình máy học để ước lượt tải và doanh thu, cần dữ liệu thu liên
  tục nhiều năm.

## Chỗ sai hoặc thiếu

- **Bài bỏ sót chi tiết quan trọng nhất.** Ở Appfigures, các gói từ Free tới Optimize theo dõi được **0 đối thủ**.
  Phải lên Boost 599,99 USD mới được tới 25 đối thủ, và các gói dữ liệu thị trường riêng (Scout, Pathfinder, Scale) bắt
  đầu từ 599,99 USD / tháng. Dữ liệu đối thủ rất đắt, đó chính là khe AppKittie chen vào với giá cho indie.
- **Doanh thu Appfigures 1,2–2 triệu USD / năm và 80.956 lượt vào AppKittie / tháng** là số do bên thứ ba ước tính,
  không kiểm được. Không dùng để quyết định.
- **Bảng "250 khách = 20K USD MRR" chỉ là phép nhân.** ShotMatic bán 39,99 USD mua đứt. Muốn có cùng doanh thu tháng
  với 250 khách trả tháng của AppKittie (19.750 USD) thì mỗi tháng phải bán khoảng 494 đơn mới.
- **"Đi từ cơ hội tới PRD" không còn là điểm khác biệt.** Preuve AI đã làm việc này (MCP, chuyển báo cáo sang Claude
  Code / Codex), ShotMatic cũng đã có Brief → Spec → Plan.
- **Quảng cáo đối thủ, video viral, thư viện paywall, ước tính doanh thu** đều cần server cào dữ liệu liên tục và mô
  hình ước tính. Đi ngược với "chạy trên máy, không tốn phí API, trả một lần". AppKittie bán theo tháng chính vì phải
  gánh chi phí đó.
- **Bài không nói ra bài học lớn nhất:** link anh gặp có `utm_source=chatgpt.com`, tức AppKittie thắng một phần nhờ
  **được ChatGPT gợi ý**. ShotMatic hiện trả 403 cho `PerplexityBot`, còn Bing vẫn mô tả shotmatic.app là tool chụp
  screenshot cũ ([GEO](geo.md)).

## ShotMatic đã làm tới đâu

### So với 9 module bài đề xuất

- **App Discovery · có.** Explore niche mở thành cây khoảng 100 keyword và bản đồ ngách. Tìm theo keyword, không theo
  bảng xếp hạng store.
- **Revenue Radar · một phần.** Có cột giá IAP, nhãn mô hình tiền của từng đối thủ, TrustMRR (doanh thu tự khai).
  Không có ước tính doanh thu.
- **Growth Radar · một phần.** Có theo dõi định kỳ 7 / 30 / 90 ngày cho project và Google Trends. Không quét cả store
  tìm app tăng bất thường.
- **Review Mining · có, mạnh.** "Đối thủ bị chê gì": gộp cùng ý, câu nguyên văn, lời chê mới nổi, người dùng ước gì.
- **Feature Gap · có, rộng hơn đề xuất.** Feature Gap Matrix, thêm gap từ Reddit, Stack Exchange, Ask HN, GitHub.
- **Ads Intelligence · chưa có.**
- **Paywall Library · chưa có.** Chỉ có giá IAP và mô hình tiền.
- **Opportunity Score · có.** Điểm sức khoẻ niche v2, gợi ý BUILD / TEST THÊM / BỎ, cờ chặn.
- **Build Brief · có.** Brief → Spec → Plan, Niche Autopilot, MCP cho Claude Code / Codex, xuất gói cho AI.

Ngoài 9 module đó ShotMatic còn có: Ai là khách hàng, trang YouTube / Amazon / Amazon Books / Google Maps, app Mac,
2 extension Chrome. Trong 3 nguồn bài gợi ý nối thêm: Reddit đã có (nhập tay), TikTok và Product Hunt chưa có.

### Phía bán hàng (đo 2026-11-07)

- App Mac 1.1.0 đã public, đã notarize. Mua thử qua Lemon Squeezy chạy được. Free 15 lượt tra, PRO 39,99 USD trọn đời.
- **15 lượt tải `.dmg`**: 9 bản 1.0.0 + 6 bản 1.1.0 (GitHub API, không tính file `.sha256`).
- Đơn PRO thật: `chưa đo`.
- 2 extension Chrome chưa lên Chrome Web Store.
- GA4 và Search Console: `chưa đo`, còn thiếu file khoá service account.

**Sản phẩm đã vượt xa mức MVP. Bán hàng mới ở vạch xuất phát.**

## Đợt A · làm ngay, không code tính năng

**1 · Mở đường cho AI search (Anh).** Cho `PerplexityBot` qua Cloudflare, tắt managed robots.txt, nhập site vào
Bing Webmaster Tools. Chi tiết ở [Audit mục 3](audit-2026-11-07.md#3-mo-uong-cho-ai-search-bing). Đây là kênh
AppKittie đang thắng.
Target: hỏi ChatGPT / Perplexity "ShotMatic là gì" thì trả lời đúng là app niche research.

**2 · Câu định vị dựa vào giá đối thủ (Claude viết, Anh duyệt).** Ví dụ:
*"Appfigures và AppKittie cho bạn biết app nào đang thắng. ShotMatic cho bạn biết chỗ nào còn trống, chạy trên máy
bạn, trả 39,99 USD một lần thay vì 49–79 USD mỗi tháng."* Đặt ở màn đầu landing theo
[Plan 2 · mục 2](../web/phase-plan2-02-landing-guide-free-tool.md).
Target: người lạ đọc màn đầu biết ShotMatic khác AppKittie ở đâu.

**3 · Bật affiliate (Anh).** AppKittie trả 30% định kỳ. Lemon Squeezy có chương trình affiliate dựng sẵn, anh kiểm trong
dashboard và tự chọn mức %. Không cần code.
Target: có link affiliate để đưa cho người viết review hoặc YouTuber.

**4 · Trang so sánh, đo trước viết sau (Claude).** Gợi ý Google US đo 2026-11-07:

- `sensor tower alternatives reddit`, `sensor tower free alternative reddit`, `sensor tower app revenue alternative`
- `appfigures free alternative`, `appfigures vs astro`, `appfigures vs apptweak`
- `apptweak free alternative`, `app market research tools`, `app store research tool`
- `appkittie alternative`: **không có gợi ý**. Tên AppKittie còn nhỏ trên Google, chưa đáng viết bài riêng.

Hai cụm có chữ `reddit` cho thấy người ta hỏi trên Reddit, nên đưa vào hàng chờ `/reddit-qa` trước. Bài blog so sánh chỉ
viết sau khi có số Search Console, đúng quyết định ở [Audit mục 7](audit-2026-11-07.md#7-blog-chat-hon-thay-vi-them-bai).
Target: 1 bài so sánh "free alternative" có impressions trong 28 ngày đầu.

**5 · Bán tay 10 đơn (Anh + Claude).** Làm theo [Audit mục 4](audit-2026-11-07.md#4-ban-tay-10-on).
Target: 10 đơn PRO.

## Đợt B · chỉ mở khi có 10 đơn PRO

Xếp theo mức hợp với một app chạy trên máy. Mỗi việc dùng dữ liệu ShotMatic đã lấy, không thêm server.

**B1 · Ước tính doanh thu thô.** Từ số rating (App Store) hoặc mốc số cài (Google Play) nhân giá IAP, ra một khoảng
thấp–cao, ghi rõ "ước tính · độ tin thấp" và cho xem công thức. Trước khi hiện trên UI, so với doanh thu tự khai trên
TrustMRR ở ít nhất 10 app; lệch quá xa thì không ra mắt. Đây là thứ khách sẵn trả tiền nhất. Gắn được vào
[Phase 56 · So sánh đối thủ](../web/phase-56-compare-competitor.md).

**B2 · Growth Radar nhẹ.** Dùng lại số đã chụp ở theo dõi định kỳ 7 / 30 / 90 ngày, báo đối thủ nào có số rating tăng
nhanh bất thường trong niche đã tra. Không thêm nguồn.

**B3 · Nút mở sang Meta Ad Library và TikTok Creative Center** theo tên từng đối thủ. Chỉ mở link, không cào, không tốn
phí. Thay cho Ads Intelligence ở mức rẻ nhất.

**B4 · Product Hunt làm một nguồn gap.** API cần token của người dùng. Kết quả vào cùng bảng gap với Reddit và Ask HN.

## Không làm

- **Thư viện paywall / onboarding, kho video viral, đo chi tiêu quảng cáo, kho hàng triệu app.** Cần server cào liên
  tục và chi phí dữ liệu hằng tháng. Nếu muốn làm thì đó là một sản phẩm SaaS khác, không phải ShotMatic.
- **Đổi giá.** Giữ 39,99 USD mua đứt tới khi có 10 đơn, như [Audit](audit-2026-11-07.md#khong-lam-luc-nay) đã ghi.
  Sau đó mới xét thêm gói trả năm.

## Liên quan

[Audit bán hàng + SEO / GEO](audit-2026-11-07.md) · [Đối thủ](doi-thu.md) · [GEO](geo.md) ·
[Plan 2 · mục 2 Landing](../web/phase-plan2-02-landing-guide-free-tool.md) · [Reddit Q&A](reddit.md)
