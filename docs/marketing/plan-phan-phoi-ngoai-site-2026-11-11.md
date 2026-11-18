# 6 · Phân phối ngoài site: từ Reddit tới thư mục tool (2026-11-11)

> Đưa shotmatic.app và oneclicktool.app ra các site khác, đi từ chỗ nhỏ dễ vào (Reddit, thư mục tool, Indie Hackers)
> lên chỗ lớn (Show HN, Product Hunt). Mục đích: Google và Bing index nhanh hơn, có site thật link về, và có khách thật
> bấm vào.

<span class="chip chip--todo">Plan · chờ duyệt · 2026-11-11 · chưa đăng gì</span>

<div class="box box--goal" markdown>
**Kết luận**

- **Đăng link lên Reddit không làm trang được index.** Index đến từ sitemap, link nội bộ và nội dung đủ dày. Site ngoài cho 3 thứ khác: bot tìm ra trang sớm hơn, khách thật bấm vào, và tên sản phẩm xuất hiện ở nơi AI hay đọc.
- **Sửa nền trước khi đi đăng.** Cloudflare đang chặn `PerplexityBot` và ghi `Disallow` cho bot của ChatGPT, Perplexity, Claude ở shotmatic.app (đo 2026-11-11). Đăng ở đâu thì một phần AI cũng chưa đọc được trang đích.
- **Đi 4 tầng theo thứ tự:** nền index → hồ sơ + thư mục tool → cộng đồng → launch lớn. Tầng sau chỉ mở khi tầng trước có số.
- **Bạn tự đăng, Claude soạn.** Giữ nguyên luật của [Reddit Q&A](reddit.md): không tài khoản phụ, không nhờ vote, luôn nói rõ mình là người làm.

**Xong khi:** sau 8 tuần có 10 site thật link về trong báo cáo Links của Search Console và 100 lượt vào từ site ngoài trong 28 ngày.
</div>

## Số hiện tại

- **Search Console shotmatic.app:** 253 lượt hiển thị, 1 click, vị trí trung bình 31,3 trong 3 tháng. Đọc tay ngày 2026-11-08.
- **Sitemap:** shotmatic.app có 158 URL, oneclicktool.app có 416 URL. Đo 2026-11-11.
- **Bot:** shotmatic.app trả 200 cho Googlebot và bingbot, trả 403 cho PerplexityBot và GPTBot. oneclicktool.app trả 200 cho cả bốn. Đo 2026-11-11 bằng `curl` giả user agent, nên chỉ cho biết luật chặn theo tên bot.
- **Số trang đã index, số site link về, lượt vào từ site ngoài:** `chưa đo`. File khoá service account vẫn chưa có trên máy (kiểm 2026-11-11), nên Search Console và GA4 chưa đọc tự động được.
- **Bài Reddit, hồ sơ thư mục đã có:** `chưa đo`. Lần ghi gần nhất là 0 bài Reddit ngày 2026-11-01.

## Nó là gì

Phân phối ngoài site là mọi chỗ **không phải site của mình** mà có tên, mô tả và link về sản phẩm. Có 3 loại:

1. **Hồ sơ và thư mục:** một trang cố định mô tả sản phẩm, ví dụ AlternativeTo. Làm một lần, nằm đó lâu.
2. **Cộng đồng:** bài và comment ở Reddit, Indie Hackers, Hacker News, dev.to. Phải có ích cho người đọc thì mới sống.
3. **Launch:** một ngày tập trung ở Product Hunt hoặc Show HN. Nhiều khách trong 1–2 ngày rồi tắt.

## Nó giúp gì, không giúp gì

**Giúp:**

- **Bot tìm ra trang sớm hơn.** Googlebot và bingbot đi theo link, kể cả link `nofollow`, để phát hiện URL mới.
- **Khách thật.** Một comment đúng chỗ đưa về người đang có đúng vấn đề đó. Đây là nguồn khách sớm nhất khi Google chưa xếp hạng.
- **Tên sản phẩm ở nơi AI đọc.** ChatGPT, Perplexity và AI Overview hay trích Reddit và các trang so sánh tool. Đây là phần nối với [GEO](geo.md).
- **Vài backlink thật.** Một số thư mục và blog cho link thường. Chưa kiểm nơi nào cho, nên không tính trước.

**Không giúp:**

- **Không ép được Google index.** Trang mỏng thì có 100 link vẫn nằm ở "Crawled, currently not indexed". Việc đó sửa ở [SEO](seo.md).
- **Link Reddit, Quora, Medium đa số là `nofollow`.** Đừng đăng để lấy "sức mạnh link". Đăng để có người đọc.
- **Đăng hàng loạt cùng một nội dung** bị cả Reddit lẫn Google coi là spam, và có thể bị khoá cả domain trên Reddit.

## Tầng 0 · Nền index (tuần 1)

Làm trước khi đăng ở bất cứ đâu. Thiếu tầng này thì khách và bot tới nơi cũng không dùng được.

<span class="chip chip--todo">Đang làm · 2026-11-11 · phần trong code đã xong, còn 3 việc của bạn</span>

**Đã xong (2026-11-11):**

- [x] **Tìm ra chỗ chặn bot AI.** Không nằm trong code. Cloudflare đang làm 2 việc trước khi request tới site, xem [mục dưới](#cloudflare-ang-chan-gi).
- [x] **IndexNow cho shotmatic.app.** Script `npm run indexnow` và file khoá đã có sẵn trong repo `shotmatic`. Đã gửi 158 URL của sitemap, IndexNow trả HTTP 200.
- [x] **`?ref=<nguồn>` đã chạy.** Site đọc `ref` trên URL và ghi vào event `download_click` của GA4 (commit `1cc55de`). Link đặt ở ngoài dùng dạng `https://shotmatic.app/?ref=reddit`.
- [x] **Soát 8 trang đích chính:** đều trả 200, có canonical trỏ về chính nó, không có thẻ `noindex`.
- [x] **Chọn 10 trang đích cho shotmatic.app**, xem [danh sách dưới](#10-trang-ich-cua-shotmaticapp).

**Còn lại:**

- [ ] **(Bạn)** Sửa 2 chỗ trong Cloudflare, theo mục dưới. Xong thì báo để đo lại bằng `curl`.
- [ ] **(Bạn)** Đặt file khoá service account để đọc được Search Console và GA4. Việc này đang chặn mọi số đo.
- [ ] **(Bạn)** Bing Webmaster Tools: thêm cả hai site, nộp sitemap. Có thể nhập thẳng từ Search Console. Bing là nguồn cho Copilot và một phần ChatGPT search.
- [ ] **Ghi số mốc** sau khi có khoá: số trang đã index, số trang "Discovered" và "Crawled, not indexed", số site đang link về.
- [ ] **oneclicktool.app:** chưa thấy IndexNow, chưa chọn 10 trang đích. Làm khi tới lượt site này (sau 2 tuần).

### Cloudflare đang chặn gì

Đo 2026-11-11 bằng `curl` giả user agent, ở trang chủ và `/blog`.

**Việc 1 · Cloudflare chèn robots.txt của nó lên đầu file.** Khối "Cloudflare Managed content" ghi `Disallow: /` cho
`ChatGPT-User`, `Perplexity-User`, `Claude-User`, `Google-Agent`. Đây đúng là nhóm bot đọc trang khi người dùng hỏi AI, và
phần robots.txt của site bên dưới lại ghi cho phép cả nhóm này. Hai khối trái nhau, bot gặp khối của Cloudflare trước.

**Việc 2 · Cloudflare trả 403 theo tên bot.** Trang lỗi ghi "Your request was blocked", header `server: cloudflare`.

- **Bị 403:** `PerplexityBot`, `GPTBot`, `ClaudeBot`, `CCBot`, `Bytespider`, `Amazonbot`
- **Vẫn 200:** `OAI-SearchBot`, `ChatGPT-User`, `Perplexity-User`, `Claude-SearchBot`, Googlebot, bingbot

Chỉ `PerplexityBot` là bị chặn nhầm. Nó là bot dựng chỉ mục tìm kiếm của Perplexity và robots.txt của site đã cho phép nó.
Năm bot còn lại là bot gom dữ liệu để train, site cố ý chặn, nên giữ nguyên.

**Cách sửa (bạn làm trong Cloudflare dashboard, zone `shotmatic.app`):**

1. Tắt phần robots.txt do Cloudflare quản lý, để chỉ còn file của site. Tên mục có thể là "Manage robots.txt" hoặc nằm trong AI Crawl Control.
2. Ở phần chặn bot AI ("Block AI bots" hoặc AI Crawl Control), cho phép riêng `PerplexityBot`. Nếu chỉ có nút bật / tắt cả nhóm thì tắt, vì robots.txt của site đã chặn bot train.

Tên mục trong dashboard tôi `chưa kiểm`, Cloudflare hay đổi chỗ. Claude không tự sửa phần này vì đây là cài đặt bảo mật của tài khoản.

### 10 trang đích của shotmatic.app

Mọi link đặt ở ngoài chỉ trỏ vào các trang này:

1. `/` (trang chủ)
2. `/app-idea-checker`
3. `/app-store-keyword-research`
4. `/app-competitor-analysis`
5. `/app-category-tier-list`
6. `/scorecard`
7. `/pricing`
8. `/features`
9. `/blog/free-aso-tools` (đề xuất)
10. `/blog/check-if-app-idea-exists` (đề xuất)

Hai bài blog là đề xuất của tôi theo tên bài, chưa có số Search Console để chọn. Đổi sang bài có nhiều lượt hiển thị nhất khi đọc được số.

## Tầng 1 · Hồ sơ và thư mục tool (tuần 1–3)

Việc dễ nhất, làm một lần. Mỗi hồ sơ dùng chung một bộ chữ: tên, một câu mô tả, mô tả 100 từ, 5 ảnh, link.

**Nhịp:** 3 hồ sơ mỗi tuần, không nộp 20 nơi trong một ngày.

**Nơi đề xuất, theo thứ tự làm:**

1. **AlternativeTo:** ghi ShotMatic là lựa chọn thay cho Sensor Tower, Appfigures, AppKittie. Người tìm ở đây đang so tool.
2. **Indie Hackers (trang Products):** hồ sơ sản phẩm kèm số thật.
3. **SaaSHub:** trang so sánh tool, có mục alternatives.
4. **Uneed, Peerlist, Microlaunch, Fazier, TinyLaunch:** các bảng launch nhỏ cho indie.
5. **GitHub:** README của repo public `shotmatic-releases` ghi rõ sản phẩm là gì và link về site.
6. **Chrome Web Store:** trang extension ShotMatic Lite và Scout có link về site.
7. **Crunchbase, LinkedIn Company Page:** hồ sơ công ty, giúp Google và AI nhận ra đây là một thực thể thật.
8. **Với oneclicktool.app:** thêm thư mục app Mac (MacUpdate) và trang riêng cho từng app trên AlternativeTo.

Luật nộp, giá và kiểu link của từng nơi `chưa kiểm`. Kiểm trang submit trước khi nộp, bỏ nơi nào bắt trả tiền mới cho link.

## Tầng 2 · Cộng đồng (tuần 2–8)

Đây là phần mang khách về. Tỉ lệ giữ nguyên như plan cũ: **ít nhất 9 comment giúp người, mới 1 lần nhắc sản phẩm**.

**Reddit, làm đầu tiên.**

- **Tuần 2:** nuôi tài khoản. Mỗi ngày 3–5 comment có ích, chưa nhắc sản phẩm.
- **Từ tuần 3:** 3 câu trả lời mỗi tuần qua `/reddit-qa`, và 1 bài hành trình mỗi tuần theo [Plan Reddit 8 bài](../app/ke-hoach-reddit.md).
- **Sub cho ShotMatic:** r/SideProject, r/indiehackers, r/microsaas, r/ClaudeCode, r/iOSProgramming, r/androiddev.
- **Sub cho OneClickTool:** r/macapps, r/chrome_extensions, r/SideProject.
- **Link chỉ nằm trong comment** khi có người hỏi, không nằm trong bài.

**Indie Hackers.** Mỗi 2 tuần một bài có số thật: lượt tải, đơn, thứ đã thử và hỏng.

**Hacker News.** Chỉ comment khi có điều đáng nói. Show HN để ở tầng 3.

**dev.to và Hashnode.** Đăng lại 1 bài blog kỹ thuật mỗi tuần, đặt `canonical_url` về bài gốc để Google không coi là trùng.

**X và LinkedIn.** Mỗi bài blog mới thành 1 bài ngắn kèm ảnh kết quả thật. Không phải kênh chính.

**YouTube.** Đã có [plan video 14 ngày](https://claude.ai/artifact/UdC118LHNbAkF2WHZyi1WK). Mỗi video ghi link trang đích trong mô tả.

**Không làm lúc này:** Quora, Medium, Pinterest, forum profile hàng loạt, dịch vụ "nộp 500 thư mục". Tốn giờ, khách ít, hoặc dễ thành spam.

## Tầng 3 · Launch lớn (sau tuần 8)

Chỉ mở khi đạt cả 3 điều kiện:

- Tầng 1 và 2 đã có số, biết trang đích nào giữ được khách.
- Có ít nhất 1 đơn PRO thật, để biết cửa bán chạy.
- Có 10 người sẵn sàng nhận xét thật trong ngày launch.

**Show HN** trước, vì free tool `/app-idea-checker` là thứ người ta thử được ngay không cần tải.
**Product Hunt** sau, vẫn theo quyết định ngày 02/11 là để sau khi có số chuyển đổi.

## Lịch 8 tuần

- **Tuần 1:** tầng 0 xong. Viết bộ chữ hồ sơ dùng chung. Nộp AlternativeTo, Indie Hackers Products, SaaSHub.
- **Tuần 2:** nuôi tài khoản Reddit. Thêm 3 hồ sơ. Bật Bing Webmaster và IndexNow.
- **Tuần 3:** bài Reddit số 1, 3 câu trả lời. Thêm 3 hồ sơ. Bài dev.to đầu tiên.
- **Tuần 4:** bài Reddit số 2 và 3. Bài Indie Hackers đầu tiên. **Đo lần 1.**
- **Tuần 5–6:** giữ nhịp 3 câu trả lời + 1 bài mỗi tuần. Bỏ nơi nào sau 4 tuần không có lượt vào.
- **Tuần 7:** dồn giờ vào 2 nơi cho nhiều khách nhất.
- **Tuần 8:** **đo lần 2**, quyết có mở tầng 3 không.

## Target (đích tự đặt)

Chưa có số mốc, nên các số này để so, không phải chuẩn ngành. Chỉnh lại sau lần đo ở tuần 4.

**Tuần 4:**

- 9 hồ sơ thư mục đã lên
- 40 comment giúp người, 9 câu trả lời có nhắc sản phẩm, 3 bài Reddit
- 3 site thật link về trong Search Console
- 30 lượt vào từ site ngoài trong 28 ngày

**Tuần 8:**

- 15 hồ sơ thư mục
- 10 site thật link về
- 100 lượt vào từ site ngoài trong 28 ngày
- Mọi trang trong 10 trang đích đã index
- Ít nhất 5 lượt tải có `ref` từ site ngoài

## Đo thế nào

- **Search Console → Links:** số site link về và trang nào được link.
- **Search Console → Page indexing:** số trang đã index, đọc trước và sau.
- **GA4 → Traffic acquisition:** lượt vào theo nguồn Referral và Organic Social, lọc theo `ref`.
- **Bing Webmaster → Backlinks:** nguồn thứ hai để đối chiếu.
- **Sổ tay:** một dòng cho mỗi lần đăng, gồm ngày, nơi, link bài, trang đích, lượt vào sau 7 ngày.

## Áp cho site khác

Quy trình giữ nguyên, mỗi site đổi 3 thứ:

1. **Bộ chữ hồ sơ:** tên, một câu mô tả, sản phẩm đang thay thế.
2. **10 trang đích.**
3. **Danh sách sub và thư mục** đúng ngành của site đó.

oneclicktool.app đi sau shotmatic.app 2 tuần, để dùng lại những gì đã học và không chia đôi giờ ngay từ đầu.

## Luật

- Claude không đăng, không comment, không vote, không tạo tài khoản thay bạn.
- Không bịa số. Số trong bài lấy từ số đã đo có ngày.
- Một nội dung chỉ đăng một nơi. Nơi khác thì viết lại góc khác.
- Không mua link, không trả tiền cho thư mục để lấy link.

## Việc cần bạn quyết

1. **Duyệt plan này**, và chốt làm shotmatic.app trước, oneclicktool.app sau 2 tuần.
2. **Đặt khoá service account**, hoặc chấp nhận đọc tay Search Console mỗi 4 tuần.
3. **Duyệt hồ sơ Reddit** ở `marketing/reddit/profile.md`, việc này đang chờ từ 2026-11-02.
4. **Cho sửa luật chặn bot AI** ở shotmatic.app.

## Liên quan

[1 · Google Search Console](google-search-console.md) · [4 · SEO](seo.md) · [5 · GEO](geo.md) · [Reddit Q&A](reddit.md) ·
[Plan Reddit 8 bài](../app/ke-hoach-reddit.md)
