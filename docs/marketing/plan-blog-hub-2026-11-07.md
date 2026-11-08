# Plan dựng lại trang Blog: hub, chủ đề, link nội bộ (2026-11-07)

> Trang này lo cấu trúc blog: tìm bài, phân loại, link nội bộ, độ phủ index. Đề tài bài mới vẫn theo
> Plan blog SEO + GEO. Thứ tự việc bán tổng thể vẫn theo Audit (link ở cuối trang).

<span class="chip chip--doing">Đã duyệt 2026-11-07 · Đợt 1 đã deploy · Search Console vẫn chưa đọc được</span>

<div class="box box--goal" markdown>
**Kết luận**

- **Bố cục mới giải quyết được chuyện khó tìm bài và thiếu trang chủ đề**, nên đáng làm ngay.
- **Bố cục mới không tự làm bài được index.** Có 66 trong 85 bài dưới 600 từ, và 74 bài lên trong 3 ngày. Nếu Google xếp đây là vấn đề chất lượng, phải bồi hoặc gộp bài.
- **Thứ tự đề xuất:** chia lại chủ đề → hub `/blog` → trang chủ đề → link nội bộ → bồi bài theo số Search Console.
- **Đề xuất giữ lại 52 bài đã hẹn** vì 47 bài dưới 600 từ. Đẩy tiếp sẽ làm tỉ lệ bài mỏng tăng lên.

**Xong khi:** mọi bài cách `/blog` tối đa 2 click · không còn bài nào 0 link từ thân bài khác · mỗi chủ đề có bài trụ · có số index tuần 0 để so sau 28 ngày.
</div>

## 1. Hiện trạng đo được

Nguồn: `origin/main` của repo landing và site thật, đo 2026-11-07. Số link tính bằng script đọc Markdown và mô phỏng phần Related của template.

| Chỉ số | Số | Hệ quả |
|---|---:|---|
| Bài đang lên / đã hẹn | 85 / 52 | |
| Bài mỗi trang, số trang danh sách | 6 / 15 | Bài cũ nằm sâu, phải bấm số trang mà không biết trong đó có gì |
| Bài lên trong 3 ngày 31/10–02/11 | 74 | Cùng ngày thì xếp theo slug A–Z, nên thứ tự "mới nhất" gần như vô nghĩa |
| Bài thuộc chuyên mục `niche` | 52 / 85 | Một ngăn chứa cả `codex-vs-claude-code` lẫn `flutter-vs-react-native-vs-native-indie`. SEO và AEO mỗi mục chỉ có 1 bài |
| Trang chuyên mục được index | 0 | Cả 7 trang đều `noindex`, trong khi 14 trang `/blog/page/N` không có chủ đề lại được index |
| Bài có 0 link từ thân bài khác | 30 / 85 | Có 44 bài có tối đa 1 link. Nguồn link chính là khối Related tự động |
| Link từ trang chủ tới blog | chỉ `/blog` | Trang chủ không đẩy tới bài cụ thể nào |
| Thân bài: dưới 600 / 600–1.199 / từ 1.200 từ | 66 / 11 / 8 | Trung vị 447 từ |
| Bài đã hẹn dưới 600 từ | 47 / 52 | Chỉ 1 bài đạt 1.200 từ |
| Bài đã index | `chưa đo` | Thiếu file khoá Search Console |

**Những phần đang tốt, giữ nguyên:** canonical, BlogPosting, BreadcrumbList, RSS, `llms.txt`, bản `.md` có `noindex`, mục lục dính bên phải bài, khung câu trả lời ngắn, FAQ và nguồn hiển thị trong bài.

**Lưu ý về bài hẹn giờ:** site build tĩnh, nên bài đến ngày chỉ lên khi có build mới. Repo không có cron hay workflow build lại. Chưa kiểm tra phía Vercel có deploy hook hẹn giờ không.

## 2. Bố cục mới

Không skill nào đang có viết về giao diện trang danh sách blog. `site-architecture` chỉ lo cấu trúc trang và URL. Phần bố cục dưới đây lấy từ cách 3 blog lớn làm: [Ahrefs](https://ahrefs.com/blog/), [Backlinko](https://backlinko.com/blog), [Zapier](https://zapier.com/blog/). Cả 3 đều dùng `/blog` như trang biên tập có bài chọn sẵn và khối theo chủ đề. Thứ tự khối dưới đây là đề xuất, không chép riêng blog nào.

### `/blog` · trang hub

Cột chính, từ trên xuống:

1. **Hero:** H1, một câu nói blog giúp gì, ô tìm bài, các chip chủ đề.
2. **Bài chủ đạo:** một bài do người chọn (`featured: true`), không tự lấy bài mới nhất. Đề xuất `validate-app-idea-before-you-build` (1.818 từ).
3. **Start here:** lộ trình 5 bài có đánh số, cho người mới vào.
4. **Khối theo chủ đề:** mỗi chủ đề có blurb một câu, 3 bài chọn sẵn, nút "All N articles".
5. **Mới cập nhật:** 5 bài xếp theo `updated`.
6. **Link `/blog/all`:** xem toàn bộ bài.

Cột phụ, dính khi cuộn, từ 1100px trở lên: danh sách chủ đề kèm số bài · bài đọc nhiều (khi có số GA4) · thẻ App Idea Checker · nút tải app. Dưới 1100px, cột phụ xuống cuối trang, còn chip chủ đề vẫn ở Hero.

Mọi bài trong cột chính xếp một hàng ngang hết bề rộng, không chia thành lưới thẻ hẹp, để tiêu đề dài không vỡ dòng.

Lộ trình Start here đề xuất:

1. `low-competition-app-niche` · tìm niche ít cạnh tranh
2. `validate-app-idea-before-you-build` · kiểm ý tưởng trước khi làm
3. `google-trends-find-a-niche` · đọc nhu cầu trên Google Trends
4. `app-store-keyword-research-free` · tìm keyword
5. `app-store-competitor-analysis-example` · soi đối thủ

### `/blog/category/<chủ đề>` · trang chủ đề

Breadcrumb hiển thị → H1 → đoạn giới thiệu 100–200 từ viết tay → bài trụ → toàn bộ bài của chủ đề, không chia trang → chủ đề liên quan.

Chỉ bỏ `noindex` khi chủ đề có từ 5 bài trở lên, đã có đoạn giới thiệu và bài trụ. Trang danh sách trần không có giá trị riêng để index.

### `/blog/all` · toàn bộ bài

Một trang gom mọi bài theo chủ đề, mỗi dòng chỉ có tiêu đề, số phút đọc, ngày. Trang này thay `/blog/page/N`.

**Đề xuất bỏ phân trang.** Với 85–137 bài, một trang liệt kê đủ đưa mọi bài về 2 click, gọn hơn 15 trang mỗi trang 6 bài. `/blog/page/N` chuyển 301 về `/blog/all`, trang phân trang của chuyên mục chuyển về trang chủ đề. Mục tiêu là index bài viết, không phải index trang danh sách. Khi một danh sách vượt khoảng 200 bài thì xem lại, và khi đó phân trang theo [hướng dẫn của Google](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading): mỗi trang có URL và canonical riêng.

### Ô tìm bài

Dùng Fuse.js, tìm trên tiêu đề, mô tả, keyword, chủ đề. File chỉ mục sinh lúc build và chỉ tải khi bấm vào ô tìm. Kết quả hiện ngay tại chỗ, không tạo URL `/search?q=`, nên không sinh thêm trang rác cho bot.

Chọn Fuse thay vì Pagefind vì không phải đụng tới bước build trên Vercel. Pagefind tìm được cả thân bài, nhưng chưa thử với cấu hình Next hiện tại. Nếu người dùng cần tìm trong thân bài thì đổi sau.

Gửi GA4 event `blog_search`. Các từ tìm không ra kết quả cũng là gợi ý đề tài.

### Trang bài viết

- **Breadcrumb hiển thị:** Home › Blog › Chủ đề › Bài, khớp schema đang có.
- **Cột phụ:** giữ mục lục và Read next, thêm link "Part of: <chủ đề>" trỏ về trang chủ đề.
- **Bỏ Older / Newer:** với 74 bài cùng 3 ngày, hai link này gần như ngẫu nhiên. Thay bằng bài trước / sau trong cùng chủ đề hoặc lộ trình.
- **Related:** ưu tiên danh sách chọn tay (`related:`), rồi mới tới chấm điểm cùng chủ đề. Hiện chỉ so từ trong tiêu đề nên dễ lệch: `google-play-niche-research` nhận 18 link còn `estimate-app-revenue-from-public-signals` nhận 0.
- **Hộp tác giả:** tên, việc đang làm, cách đo số trong bài. Đây là tín hiệu tin cậy cho người đọc và AI search.

## 3. Chia lại chủ đề

Thêm field `topic` thay `category`. Bảng đếm theo một lượt phân loại sơ bộ theo slug. Bạn duyệt xong mới gán thật. Số "hẹn" có thể lệch vài bài.

| Chủ đề | Slug đề xuất | Đang lên | Đã hẹn | Trang chủ đề |
|---|---|---:|---:|---|
| Niche research & validation | `niche-research` | 19 | 6 | Index |
| Building with AI | `build-with-ai` | 17 | 0 | Index |
| Tools & alternatives | `tools` | 12 | 1 | Index |
| Launch & growth | `launch` | 11 | 12 | Index |
| App ideas | `app-ideas` | 10 | 19 | Index |
| ASO & keywords | `aso` | 10 | 13 | Index |
| SEO, AEO, GEO | `seo-geo` | 4 | 0 | `noindex` tới khi đủ 5 bài |
| Google Trends | `google-trends` | 2 | 1 | `noindex` tới khi đủ 5 bài |

Chuyển 301 từ URL cũ: `niche` → `niche-research` · `founders` → `launch` · `trends` → `google-trends` · `product` → `tools` · `seo`, `aeo`, `geo` → `seo-geo`.

Không dùng slug `ideas` vì đã dành cho chuyên mục cũ đang chuyển sang oneclicktool.app. Không tạo trang tag, vì 85 bài chia tag chỉ sinh thêm trang mỏng.

## 4. Link nội bộ

Mô hình trục và nan hoa, theo `site-architecture`:

- **Bài trụ** link tới mọi bài trong chủ đề. Mỗi chủ đề có đúng 1 bài trụ (`pillar: true`).
- **Bài con** có ít nhất 1 link trong thân bài về bài trụ và 1 link sang bài cùng chủ đề, chữ neo mô tả rõ nội dung.
- **Trang chủ** thêm khối 3–5 bài trụ.
- **Trang tool và trang tính năng** link sang bài trụ gần nhất, ví dụ `/app-idea-checker` → bài validate.
- **Bài tool** dẫn về trang tính năng đúng việc, không chỉ nút tải chung.

Thêm vào `scripts/check-blog.mjs`: báo khi bài có 0 link vào từ thân bài khác, thiếu link về bài trụ, hoặc link tới bài chưa lên. Giai đoạn đầu chỉ cảnh báo, sửa xong 30 bài đang thiếu mới chặn build.

## 5. SEO, AEO, GEO

Làm:

- Đưa trang chủ đề đủ điều kiện vào `sitemap.xml` và `llms.txt`, chỉ giữ URL đang index được. `lastmod` chỉ đổi khi sửa nội dung thật.
- Gửi lại sitemap và chạy `npm run indexnow` sau đợt đổi URL.
- Giữ nội dung trong HTML ban đầu, đúng như hiện tại, vì bot AI cần đọc được không qua JS.
- Việc mở bot trên Cloudflare vẫn theo Bước 0 của [Plan blog SEO + GEO](plan-blog-seo-geo-2026-11-07.md). Không làm phần này thì AI search vẫn đọc khó, dù blog có đẹp hơn.

Không làm, vì đã lỗi thời hoặc chưa có bằng chứng:

- **`rel=next/prev`:** Google không còn dùng. Bỏ luôn cùng phân trang.
- **Noindex trang 2 trở đi, hoặc canonical chúng về trang 1:** Google khuyên mỗi trang có canonical riêng.
- **Làm thêm FAQ schema để lấy rich result:** Google ghi [đã ngừng từ 7/5/2026](https://developers.google.com/search/updates). Giữ FAQ hiển thị vì có ích cho người đọc.
- **HowTo schema, SearchAction:** không còn cho kết quả đặc biệt trên Google. Chưa mở trang gốc xác nhận riêng SearchAction.
- **Hy vọng `llms.txt` giúp lên Google AI:** không có bằng chứng. Giữ file vì đã có sẵn và không tốn công.
- **Noindex hàng loạt bài mỏng:** ưu tiên bồi hoặc gộp.

## 6. Bồi bài theo số đo

Google không đặt ngưỡng số từ, cũng [không cấm tốc độ đăng](https://developers.google.com/search/docs/essentials/spam-policies). Tiêu chí là giá trị và mục đích, nên số từ ở đây chỉ để chọn bài xem trước, không dùng để kết tội bài nào. Khi chưa có Search Console, chưa thể kết luận blog đang bị xử lý.

Khi có số, xếp 85 bài vào 4 nhóm:

| Tình huống | Việc làm |
|---|---|
| Có impressions, hoặc là bài trụ | Bồi sâu, thêm số tự đo, giữ URL |
| Trùng ý với bài mạnh hơn | Gộp, chuyển 301, bỏ khỏi sitemap |
| Crawled nhưng không index, chưa ai tìm | Bồi nếu có số riêng để thêm, không thì gộp |
| Không có gì riêng để nói | Bỏ, chuyển 301 về bài gần nhất |

Mỗi bài giữ lại phải có điều mà kết quả top chưa có, thường là bảng số tự đo. Bài trụ làm trước.

## 7. Thứ tự làm

Mỗi đợt deploy riêng, xem ở 1340px và 375px.

### Đợt 0 · Chốt và mở đo

- [x] **(Bạn)** Duyệt 3 quyết định ở mục cuối (2026-11-07)
- [ ] **(Bạn)** Đặt file khoá service account, cấp quyền cho email service account ([các bước](google-analytics.md))
- [ ] **(Claude)** Ghi số mốc tuần 0: bài đã index, impressions, click, các lý do không index

Có thể làm Đợt 1–3 trước khi có khoá, vì đây là việc cấu trúc. Riêng Đợt 4 phải đợi số. Tuy vậy, nên ghi mốc trước khi deploy Đợt 1, nếu không sẽ khó so trước và sau.

### Đợt 1 · Chủ đề và trang danh sách

Deploy 2026-11-07, commit `3ad5edf` trên `main` của repo landing. Đã soát trên site thật: chuyển hướng đúng, 87 URL blog trong sitemap đều trả 200, bài đang giữ trả 404.

- [x] Thêm `topic`, `featured`, `pillar` vào frontmatter, gán chủ đề cho cả 139 file (137 bài + 2 nháp). Script soát đã đọc `related`, chưa bài nào dùng
- [x] Đặt `draft: true` cho 52 bài đã hẹn, theo Quyết định 1
- [x] Thêm chuyển hướng cho chuyên mục cũ và `/blog/page/N`. Next.js trả 308, Google xử lý như 301
- [x] Làm `/blog/all`, bỏ phân trang, cập nhật sitemap và `llms.txt`. `/blog` tạm hiện 12 bài mới nhất cho tới Đợt 2
- [x] Cập nhật skill `shotmatic-blog` theo chủ đề mới
- [x] **(Bạn)** Cho phép đẩy lên `main` để deploy (2026-11-07)
- [x] Kiểm chuyển hướng trên site thật, chạy `npm run indexnow` (108 URL, HTTP 200)
- [ ] Gửi lại sitemap trong Search Console (cần file khoá)

### Đợt 2 · Hub và trang chủ đề

- [ ] Làm hub: Hero, bài chủ đạo, Start here, khối chủ đề, Mới cập nhật, cột phụ
- [ ] Viết đoạn giới thiệu cho 6 trang chủ đề, chọn bài trụ, bỏ `noindex` khi đủ điều kiện
- [ ] Làm ô tìm bài và event `blog_search`

### Đợt 3 · Trang bài và link nội bộ

- [ ] Breadcrumb hiển thị, Related mới, bỏ Older / Newer, hộp tác giả
- [ ] Thêm link trong thân bài cho 30 bài đang 0 link vào, thêm link về bài trụ
- [ ] Thêm khối bài trụ ở trang chủ, link từ trang tool và trang tính năng
- [ ] Thêm cảnh báo vào `check-blog.mjs`, gửi lại sitemap, chạy IndexNow

### Đợt 4 · Nội dung (cần số Search Console)

- [ ] Xếp 85 bài vào 4 nhóm ở mục 6
- [ ] Bồi 6–8 bài trụ trước, kèm 6 bài đã liệt kê trong [Plan blog SEO + GEO](plan-blog-seo-geo-2026-11-07.md)
- [ ] Xem lại 52 bài đã hẹn: bài nào đủ chuẩn mới cho lên

## 8. Đo sau 28 ngày

Không đặt mục tiêu organic bằng con số vì chưa có mốc. So với số tuần 0:

| Câu hỏi | Lấy từ đâu | Đọc thế nào |
|---|---|---|
| Thêm bao nhiêu bài được index? | Search Console | Tăng là cấu trúc có tác dụng. Đứng yên mà lý do là "Crawled" thì nghi chất lượng, chuyển sang Đợt 4 |
| Trang chủ đề có impressions không? | Search Console | Không có sau 2 chu kỳ thì xem lại đoạn giới thiệu và bài trụ |
| Có đọc thêm bài không? | GA4 `blog_next`, số trang mỗi phiên | So theo `place` trước và sau |
| Người ta tìm gì? | GA4 `blog_search` | Từ không ra kết quả thành gợi ý đề tài |
| Có ra lượt tải không? | GA4 `download` theo `place` | Đích cuối, không dừng ở traffic |

Rủi ro chính là đổi nhiều URL cùng lúc, nên chỉ đổi URL danh sách, không đổi URL bài. URL bài chỉ đổi khi gộp bài, luôn kèm 301.

## Quyết định cần chốt

1. **Có giữ lại 52 bài đã hẹn không?** Đề xuất: giữ lại tới khi có số Search Console, rồi cho lên từng bài đạt chuẩn. Bài đầu tiên hẹn ngày 2026-11-09.
2. **8 chủ đề trên có đúng cách bạn muốn chia không?** Đề xuất: dùng bảng ở mục 3, gộp SEO, AEO, GEO thành một.
3. **Có bỏ hẳn phân trang không?** Đề xuất: bỏ, dùng `/blog/all`.

**Đã chốt 2026-11-07:** làm theo cả 3 đề xuất.

Bài trụ đã gán ở Đợt 1: `validate-app-idea-before-you-build` · `app-ideas-that-make-money` · `app-store-keyword-research-free` · `what-is-vibe-coding` · `app-launch-checklist-indie` · `best-app-niche-research-tools-2026` · `google-trends-find-a-niche` · `seo-vs-aeo-vs-geo`. Độ sâu chưa đều: `what-is-vibe-coding`, `app-launch-checklist-indie`, `best-app-niche-research-tools-2026` và `seo-vs-aeo-vs-geo` đều dưới 600 từ, phải bồi ở Đợt 4.

## Nguồn tham khảo

- Google: [phân trang](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading) · [link crawl được](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) · [chính sách spam](https://developers.google.com/search/docs/essentials/spam-policies) · [sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) · [cập nhật Search](https://developers.google.com/search/updates) · [báo cáo index](https://support.google.com/webmasters/answer/7440203)
- Bố cục blog đã đọc: [Ahrefs](https://ahrefs.com/blog/) · [Ahrefs archive](https://ahrefs.com/blog/archive/) · [Backlinko](https://backlinko.com/blog) · [Backlinko hub](https://backlinko.com/hub) · [Zapier](https://zapier.com/blog/). Đọc bản chuyển sang văn bản, chưa xem giao diện thật.
- Skill đã rà: `site-architecture` · `seo-audit` · `schema` · `ai-seo` · `content-strategy` · `programmatic-seo` · `shotmatic-blog`

## Liên quan

[Plan blog SEO + GEO](plan-blog-seo-geo-2026-11-07.md) · [Audit 2026-11-07](audit-2026-11-07.md) · [AEO / GEO](aeo-geo.md) · [Google Analytics + Search Console](google-analytics.md) · [Programmatic SEO](programmatic-seo.md)
