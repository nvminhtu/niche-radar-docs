# Bản đồ nguồn gap

> Kết quả của [Phase 14](phase-14-gap-sources.md). Có **52 nguồn** tìm gap và keyword niche, **17 MCP**, **21 repo / tool**
> và **12 phương pháp**, tất cả chấm chung một thang. Kiểm ngày **2026-10-26**: mở thật vài trang của từng nguồn, đọc
> điều khoản. Không đăng ký, không trả phí, không quét hàng loạt. Số nào chưa đo được thì ghi `chưa đo`.

<span class="chip chip--done">Xong 2026-10-26 · top 3 đã duyệt → Phase 12 + 13</span>

<div class="box box--star" markdown>
**Tóm tắt**

- **Làm phase riêng (đã duyệt 2026-10-26 → Phase 12 + 13):**
  1. **Stack Exchange Q&A** (Ask Different + Super User): đã gọi thử API được, không cần key, có điểm và lượt xem.
  2. **GitHub Issues xếp theo 👍**: tính năng người dùng xin mà maintainer không làm. API miễn phí, điều khoản thoáng nhất trong các nguồn.
  3. **Hacker News Ask HN** (API Algolia): câu "is there an app / tool…" kèm điểm và số bình luận.
- **Dự bị:** X search. Tín hiệu mạnh, nhưng API tính tiền theo bài đọc ($0.005 / bài), nên anh quyết.
- **Đã có trong ShotMatic, không cần phase mới:** Google / store autocomplete (Phase 1–2), review App Store (Phase 2, sẽ đào sâu ở Phase 18), Google Trends (Phase 3), TrustMRR (Phase 38), Reddit (Phase 11).
- **Phần lớn chợ review lớn cấm quét** (G2, Trustpilot, Shopify, Upwork, VS Code, Gumroad…). Chỉ đọc tay khi đã chọn niche.
- **Amazon (Phase 53–54) yếu:** gợi ý Amazon chỉ cho thấy hàng vật lý, còn điều khoản cấm khai thác dữ liệu. Đề xuất hạ xuống ứng viên.
</div>

## Thang chấm

Mỗi nguồn chấm 6 tiêu chí (chi tiết ở [Phase 14 · Thang chấm](phase-14-gap-sources.md#thang-cham-moi-nguon)):

1. **Gap**: có cho thấy người ta *cần mà chưa có* không. Chấm **Mạnh / Vừa / Yếu**
2. **Quan tâm**: có upvote, lượt xem, số review để xếp hạng không. Chấm **Mạnh / Vừa / Yếu**
3. **Lấy được**: API miễn phí · API trả phí · đọc qua trình duyệt · chỉ làm tay · cấm
4. **Chi phí**: miễn phí · có gói free · trả phí (giá có nguồn + ngày)
5. **Điều khoản**: rủi ro **Thấp / Vừa / Cao**
6. **Hợp app**: Mac · iOS / Android · SaaS web · Chrome ext · vật lý

**Luật kết luận:**

- Gap Mạnh + lấy được bằng máy (không cấm, không phải chỉ làm tay) → **Làm phase riêng**.
- Gap Mạnh nhưng chỉ làm tay hoặc bị cấm quét → **Làm tay khi cần**.
- Gap Yếu → **Bỏ**.
- Gap Vừa → chọn tay hoặc bỏ, có ghi lý do.

Nguồn ShotMatic đã có thì ghi **Đã có**.

## Bảng tóm tắt

**Tìm kiếm và xu hướng**

- 1 · Google Autocomplete — **Đã có** · gap Vừa · API miễn phí* · điều khoản Vừa
- 2 · Google "People also ask" — **Làm tay** · gap Vừa · chỉ làm tay · điều khoản Cao
- 3 · Google Trends — **Đã có** · gap Yếu · API miễn phí* · điều khoản Vừa
- 4 · YouTube search suggest — **Bỏ** · gap Yếu · API miễn phí* · điều khoản Vừa
- 5 · Amazon autocomplete — **Bỏ** · gap Yếu · API miễn phí* · điều khoản Cao
- 6 · Pinterest Trends — **Bỏ** · gap Yếu · trình duyệt · điều khoản Cao
- 7 · TikTok Creative Center — **Bỏ** · gap Yếu · trình duyệt · điều khoản Cao
- 8 · Exploding Topics — **Bỏ** · gap Yếu · trình duyệt · điều khoản Cao
- 9 · Glimpse — **Bỏ** · gap Yếu · API trả phí · điều khoản Vừa
- 10 · AnswerThePublic — **Bỏ** · gap Vừa · trình duyệt · điều khoản Vừa

**Cộng đồng hỏi đáp**

- 11 · Reddit — **Đã có** · gap Mạnh · trình duyệt · điều khoản Vừa
- 12 · **Ask Different** — ****Phase riêng**** · gap Mạnh · API miễn phí · điều khoản Vừa
- 13 · **Super User** — ****Phase riêng**** · gap Mạnh · API miễn phí · điều khoản Vừa
- 14 · **Hacker News (Ask HN)** — ****Phase riêng**** · gap Mạnh · API miễn phí · điều khoản Vừa
- 15 · X search — **Dự bị** · gap Mạnh · API trả phí · điều khoản Thấp
- 16 · Apple Community — **Làm tay** · gap Mạnh · chỉ làm tay · điều khoản Cao
- 17 · Product Hunt — **Làm tay** · gap Vừa · API (cấm thương mại) · điều khoản Vừa
- 18 · Indie Hackers — **Bỏ** · gap Vừa · chỉ làm tay · điều khoản chưa đo
- 19 · Quora — **Bỏ** · gap Vừa · chỉ làm tay · điều khoản Cao
- 20 · Discord — **Bỏ** · gap Vừa · cấm · điều khoản Cao
- 21 · Nhóm Facebook — **Bỏ** · gap Vừa · cấm · điều khoản Cao
- 22 · MacRumors Forums — **Bỏ** · gap Vừa · chỉ làm tay · điều khoản chưa đo

**Chợ app và review**

- 23 · App Store / Mac App Store review — **Đã có** · gap Mạnh · API miễn phí · điều khoản Vừa
- 24 · AlternativeTo — **Làm tay** · gap Mạnh · trình duyệt · điều khoản chưa đo
- 25 · Shopify App Store — **Làm tay** · gap Mạnh · cấm · điều khoản Cao
- 26 · Chrome Web Store — **Làm tay** · gap Vừa · trình duyệt · điều khoản Vừa
- 27 · Firefox Add-ons (AMO) — **Làm tay** · gap Vừa · API miễn phí · điều khoản Thấp
- 28 · Setapp — **Bỏ** · gap Yếu · trình duyệt · điều khoản Cao
- 29 · Raycast Store — **Bỏ** · gap Yếu · trình duyệt · điều khoản Cao
- 30 · VS Code Marketplace — **Bỏ** · gap Vừa · cấm · điều khoản Cao
- 31 · WordPress plugins — **Bỏ** · gap Vừa · API miễn phí · điều khoản Thấp
- 32 · Figma Community — **Bỏ** · gap Yếu · trình duyệt · điều khoản Vừa
- 33 · G2 — **Bỏ** · gap Vừa · cấm · điều khoản Cao
- 34 · Capterra — **Bỏ** · gap Vừa · chỉ làm tay · điều khoản Cao
- 35 · Trustpilot — **Bỏ** · gap Vừa · cấm · điều khoản Cao
- 36 · SaaSHub — **Bỏ** · gap Vừa · chỉ làm tay · điều khoản chưa đo

**Bằng chứng tiền**

- 37 · TrustMRR — **Đã có** · gap Vừa · API (key free) · điều khoản Vừa
- 38 · Etsy (template số) — **Làm tay** · gap Vừa · cấm · điều khoản Cao
- 39 · Acquire.com — **Bỏ** · gap Yếu · chỉ làm tay · điều khoản Cao
- 40 · Flippa — **Bỏ** · gap Yếu · chỉ làm tay · điều khoản Cao
- 41 · Indie Hackers products — **Bỏ** · gap Yếu · chỉ làm tay · điều khoản chưa đo
- 42 · Starter Story — **Bỏ** · gap Yếu · trình duyệt · điều khoản Vừa
- 43 · Gumroad Discover — **Bỏ** · gap Yếu · cấm · điều khoản Cao
- 44 · Notion template marketplace — **Bỏ** · gap Yếu · trình duyệt · điều khoản Vừa
- 45 · Chợ template Excel / Sheets — **Bỏ** · gap Yếu · trình duyệt · điều khoản chưa đo
- 46 · CodeCanyon — **Bỏ** · gap Yếu · chỉ làm tay · điều khoản chưa đo

**Yêu cầu tính năng**

- 47 · **GitHub Issues (👍)** — ****Phase riêng**** · gap Mạnh · API miễn phí · điều khoản Thấp
- 48 · Canny (bảng công khai) — **Làm tay** · gap Mạnh · trình duyệt · điều khoản Vừa
- 49 · Featurebase (bảng công khai) — **Làm tay** · gap Mạnh · trình duyệt · điều khoản chưa đo
- 50 · Upwork — **Làm tay** · gap Mạnh · cấm · điều khoản Cao
- 51 · Fiverr — **Làm tay** · gap Vừa · chỉ làm tay · điều khoản chưa đo

**Dữ liệu của mình**

- 52 · Search Console của mình — **Làm tay** · gap Vừa · API miễn phí · điều khoản Thấp

\* Endpoint không chính thức, không key. Gọi ít, có cache thì chạy được, nhưng có thể gãy bất cứ lúc nào.

## Chi tiết từng nguồn

Mỗi nguồn có kết luận, 6 tiêu chí và link đã mở. Tất cả kiểm ngày 2026-10-26.

### Tìm kiếm và xu hướng

#### 1 · Google Autocomplete

- **Kết luận: Đã có.** ShotMatic đã dùng để sinh keyword. Chỉ dùng để tìm keyword ứng viên, rồi kiểm gap ở nguồn khác.
- **Gap:** Vừa. Cho thấy đúng việc người ta muốn làm ("mac app to hide menu bar icons", "…keep awake"), nhưng không cho biết họ đã hài lòng với app đang dùng chưa.
- **Quan tâm:** Yếu. Không có số, chỉ có thứ tự gợi ý.
- **Lấy được:** API miễn phí, không chính thức, không cần key. Rate limit không công bố.
- **Chi phí:** miễn phí.
- **Điều khoản:** Vừa. ToS Google cấm truy cập tự động trái robots.txt.
- **Hợp app:** Mac · iOS / Android · SaaS web · Chrome ext.
- [Endpoint đã gọi](https://suggestqueries.google.com/complete/search?client=firefox&q=mac+app+to) · [Điều khoản](https://policies.google.com/terms)

#### 2 · Google "People also ask"

- **Kết luận: Làm tay khi cần.** Gõ keyword lên Google rồi chép 4–8 câu trong khối PAA vào file research.
- **Gap:** Vừa. Là câu hỏi thật, nhưng phần lớn đã có câu trả lời.
- **Quan tâm:** Yếu. Không có số.
- **Lấy được:** chỉ làm tay. Gọi máy thì bị chặn. Muốn tự động phải mua SERP API (vd SerpApi, DataForSEO ở mục MCP).
- **Chi phí:** miễn phí nếu làm tay.
- **Điều khoản:** Cao. Cào SERP trái robots.txt.
- **Hợp app:** Mac · SaaS web · Chrome ext.
- [Điều khoản](https://policies.google.com/terms)

#### 3 · Google Trends

- **Kết luận: Đã có** ([Phase 3](phase-3-google-trends.md)). Dùng để đo độ quan tâm, không dùng để tìm gap.
- **Gap:** Yếu. Chỉ cho đường xu hướng.
- **Quan tâm:** Vừa. Số tương đối 0–100.
- **Lấy được:** API miễn phí, không chính thức. Gói npm `google-trends-api` mà ShotMatic đang dùng không commit từ 2022-11 (xem mục Repo), nên dễ gãy.
- **Chi phí:** miễn phí.
- **Điều khoản:** Vừa.
- **Hợp app:** mọi loại.
- [Google Trends](https://trends.google.com/)

#### 4 · YouTube search suggest

- **Kết luận: Bỏ.** Trùng Google Autocomplete. Chỉ dùng khi chọn đề tài video marketing.
- **Gap:** Yếu. Chủ yếu là câu "best X app".
- **Quan tâm:** Yếu. Không có số.
- **Lấy được:** API miễn phí, không chính thức (`ds=yt`).
- **Chi phí:** miễn phí.
- **Điều khoản:** Vừa. ToS YouTube cấm truy cập tự động khi chưa được phép.
- **Hợp app:** Mac · iOS / Android.
- [Endpoint đã gọi](https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q=mac+app+for) · [Điều khoản](https://www.youtube.com/t/terms)

#### 5 · Amazon autocomplete

- **Kết luận: Bỏ.** Chỉ cho thấy hàng vật lý.
- **Gap:** Yếu.
- **Quan tâm:** Yếu. Không có số.
- **Lấy được:** API miễn phí, không chính thức.
- **Chi phí:** miễn phí.
- **Điều khoản:** Cao. Conditions of Use cấm data mining và robot, chỉ cho dùng cá nhân.
- **Hợp app:** vật lý.
- [Endpoint đã gọi](https://completion.amazon.com/api/2017/suggestions?mid=ATVPDKIKX0DER&alias=aps&prefix=mac+desk) · [Điều khoản](https://www.amazon.com/gp/help/customer/display.html?nodeId=508088)

#### 6 · Pinterest Trends

- **Kết luận: Bỏ.** Lệch khỏi app Mac / SaaS.
- **Gap:** Yếu. Chỉ có chủ đề đang lên (trang trí, công thức nấu ăn).
- **Quan tâm:** Vừa. Có % tăng theo tuần.
- **Lấy được:** đọc qua trình duyệt. Trang dựng bằng JS, không có API công khai.
- **Chi phí:** miễn phí.
- **Điều khoản:** Cao. Cấm scrape khi chưa được cho phép.
- **Hợp app:** vật lý · app lifestyle.
- [Trang](https://trends.pinterest.com/) · [Điều khoản](https://policy.pinterest.com/en/terms-of-service)

#### 7 · TikTok Creative Center

- **Kết luận: Bỏ.** Chỉ dùng để chọn hook marketing.
- **Gap:** Yếu. Chỉ có hashtag và quảng cáo đang chạy.
- **Quan tâm:** Mạnh. Có lượt xem theo hashtag.
- **Lấy được:** đọc qua trình duyệt. Research API chỉ dành cho học thuật.
- **Chi phí:** miễn phí.
- **Điều khoản:** Cao. Cấm trích xuất tự động (đọc qua bản tóm tắt bên thứ ba vì trang gốc đòi đăng nhập).
- **Hợp app:** iOS / Android.
- [Trang](https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en)

#### 8 · Exploding Topics

- **Kết luận: Bỏ.** Đắt và không cho tín hiệu gap.
- **Gap:** Yếu. Chủ đề đang tăng, đa số là hàng tiêu dùng.
- **Quan tâm:** Mạnh. Có lượt tìm / tháng và % tăng.
- **Lấy được:** đọc qua trình duyệt. Trang giá không nhắc API.
- **Chi phí:** trả phí. Entrepreneur $39 / tháng, Investor $99, Business $249, không có gói free (đo 2026-10-26).
- **Điều khoản:** Cao. Cấm dùng nội dung cho mục đích thương mại.
- **Hợp app:** SaaS web · vật lý.
- [Trang](https://explodingtopics.com/) · [Giá](https://explodingtopics.com/pricing) · [Điều khoản](https://explodingtopics.com/terms)

#### 9 · Glimpse

- **Kết luận: Bỏ.** Chỉ là lớp phủ lên Google Trends.
- **Gap:** Yếu.
- **Quan tâm:** Mạnh. Có lượt tìm tuyệt đối.
- **Lấy được:** API trả phí.
- **Chi phí:** `chưa đo`. Trang giá không ghi số.
- **Điều khoản:** Vừa. Không mở được ToS (404).
- **Hợp app:** SaaS web · Chrome ext.
- [Giá](https://meetglimpse.com/pricing/)

#### 10 · AnswerThePublic

- **Kết luận: Bỏ.** Tự ghép autocomplete với tiền tố "how / can / is there" là ra cùng kết quả, miễn phí.
- **Gap:** Vừa. Gom câu hỏi quanh keyword.
- **Quan tâm:** Vừa. Gói trả phí mới có lượt tìm.
- **Lấy được:** đọc qua trình duyệt.
- **Chi phí:** trả phí. Starter $20 / tháng, Growth $99, Business $199 (đo 2026-10-26).
- **Điều khoản:** Vừa. Chưa đọc được phần về scraping.
- **Hợp app:** SaaS web · Chrome ext · Mac.
- [Trang](https://answerthepublic.com/) · [Giá](https://answerthepublic.com/pricing)

### Cộng đồng hỏi đáp

#### 11 · Reddit

- **Kết luận: Đã có** ([Phase 11](phase-11-reddit-gap.md), tuyến C: nhập trang lưu từ Chrome).
- **Gap:** Mạnh. Câu "is there an app", "is there a way" có upvote.
- **Quan tâm:** Mạnh. Có upvote và số bình luận.
- **Lấy được:** đọc qua trình duyệt. Gọi `top.json` bằng máy trả **HTTP 403** (đo 2026-10-26). Đây là lý do Phase 11 đi tuyến nhập file.
- **Chi phí:** miễn phí. Apify actor từ $3.40 / 1.000 kết quả (xem mục MCP).
- **Điều khoản:** Vừa.
- **Hợp app:** mọi loại.

#### 12 · Ask Different (apple.stackexchange.com)

- **Kết luận: Làm phase riêng** (đề xuất A, gộp chung với Super User).
- **Gap:** Mạnh. Tag `software-recommendation` toàn câu "app that does X on macOS", nhiều câu có trả lời "không có app nào".
- **Quan tâm:** Mạnh. Có score, view_count, số trả lời và cờ "đã có câu trả lời được chấp nhận". Gọi thử ngày 2026-10-26: câu đầu bảng có score 370, 888.907 lượt xem.
- **Lấy được:** API miễn phí. Không key được 300 lệnh / ngày (đo: `quota_max` 300). Key miễn phí của StackApps nâng lên 10.000 / ngày (số này theo nguồn phụ, chưa đo).
- **Chi phí:** miễn phí.
- **Điều khoản:** Vừa. Nội dung theo CC BY-SA (phải ghi nguồn). Từ 2024 Stack Exchange siết việc dùng dữ liệu cho AI thương mại. Dùng nội bộ, ít lệnh thì rủi ro thấp.
- **Hợp app:** Mac · iOS.
- [API đã gọi](https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=votes&tagged=software-recommendation&site=apple) · [Điều khoản](https://stackoverflow.com/legal/terms-of-service/public)

#### 13 · Super User

- **Kết luận: Làm phase riêng** (đề xuất A, dùng chung API với Ask Different, chỉ đổi `site=superuser`).
- **Gap:** Mạnh. Cùng kiểu câu hỏi xin phần mềm, phủ cả Windows.
- **Quan tâm:** Mạnh. Có score và view.
- **Lấy được:** API miễn phí, dùng chung quota.
- **Chi phí:** miễn phí.
- **Điều khoản:** Vừa. Như Ask Different.
- **Hợp app:** Mac · Windows · Chrome ext.
- [Trang](https://superuser.com/)

#### 14 · Hacker News · Ask HN (Algolia)

- **Kết luận: Làm phase riêng** (đề xuất C).
- **Gap:** Mạnh. Có các câu "Is there an app / tool…", "What do you wish existed". Gọi thử ra 92 kết quả cho "is there an app", có bài 11 điểm / 13 bình luận.
- **Quan tâm:** Mạnh. JSON có `points` và `num_comments`.
- **Lấy được:** API miễn phí, không key. Lọc được `tags=ask_hn` và theo ngày. Rate limit không công bố.
- **Chi phí:** miễn phí.
- **Điều khoản:** Vừa. Điều khoản của YC cấm scrape trang. API Algolia là kênh công khai HN đưa ra.
- **Hợp app:** SaaS web · Mac (dev tool) · Chrome ext.
- [API đã gọi](https://hn.algolia.com/api/v1/search?query=%22is%20there%20an%20app%22&tags=ask_hn) · [Điều khoản](https://www.ycombinator.com/legal/)

#### 15 · X search

- **Kết luận: Dự bị.** Theo luật thì đủ điều kiện làm phase riêng, nhưng tốn tiền theo lượt, nên anh quyết.
- **Gap:** Mạnh. Có rất nhiều câu "is there an app that…", "I'd pay for…".
- **Quan tâm:** Mạnh. Có like, repost, reply, view.
- **Lấy được:** API trả phí, tính theo lượt. Không còn gói free, chỉ có tín dụng khuyến mãi cho người mới.
- **Chi phí:** đọc $0.005 / bài, đếm $0.005–0.010 (đo 2026-10-26). Ví dụ 2.000 bài / tuần ≈ $10 / tuần.
- **Điều khoản:** Thấp nếu qua API chính thức, Cao nếu cào.
- **Hợp app:** mọi loại.
- [Giá API](https://docs.x.com/x-api/getting-started/pricing)

#### 16 · Apple Community (discussions.apple.com)

- **Kết luận: Làm tay khi cần.** Tìm `site:discussions.apple.com "is there an app" <chủ đề>`, đọc 5–10 thread, ghi câu hỏi, ngày và số "Me too".
- **Gap:** Mạnh. Câu trả lời hay gặp là "không có, gửi feedback cho Apple". Đó là gap thật cho app Mac.
- **Quan tâm:** Vừa. Có "Me too" và lượt xem, nhưng gọi máy không lấy được.
- **Lấy được:** chỉ làm tay. Không có API, trang tìm kiếm cần JS.
- **Chi phí:** miễn phí.
- **Điều khoản:** Cao. Điều khoản site Apple cấm robot, spider, page-scrape.
- **Hợp app:** Mac · iOS.
- [Thread đã mở](https://discussions.apple.com/thread/256024640) · [Điều khoản](https://www.apple.com/legal/internet-services/terms/site.html)

#### 17 · Product Hunt

- **Kết luận: Làm tay khi cần.** Mở trang đối thủ trên PH, đọc bình luận chê và xin tính năng.
- **Gap:** Vừa. Bình luận chê nằm rải rác dưới bài ra mắt.
- **Quan tâm:** Mạnh. Có upvote và bình luận.
- **Lấy được:** API GraphQL miễn phí, cần token. Docs ghi **cấm dùng thương mại**.
- **Chi phí:** miễn phí.
- **Điều khoản:** Vừa.
- **Hợp app:** SaaS web · Mac · Chrome ext.
- [Diễn đàn](https://www.producthunt.com/p/general) · [Docs API](https://api.producthunt.com/v2/docs)

#### 18 · Indie Hackers

- **Kết luận: Bỏ.** Đây là gap của founder, không phải của người mua.
- **Gap:** Vừa.
- **Quan tâm:** Vừa.
- **Lấy được:** chỉ làm tay. Gọi máy bị 403.
- **Chi phí:** miễn phí.
- **Điều khoản:** `chưa đo`.
- **Hợp app:** SaaS web.
- [Trang](https://www.indiehackers.com/)

#### 19 · Quora

- **Kết luận: Bỏ.** Nhiễu. Ask Different / HN cho cùng loại câu hỏi mà sạch hơn.
- **Gap:** Vừa. Nhiều câu trả lời quảng cáo, câu hỏi cũ.
- **Quan tâm:** Yếu. Lượt xem phải đăng nhập mới thấy.
- **Lấy được:** chỉ làm tay (403).
- **Chi phí:** miễn phí.
- **Điều khoản:** Cao. Theo nguồn phụ.
- **Hợp app:** iOS / Android · SaaS web.
- [Điều khoản](https://www.quora.com/about/tos)

#### 20 · Discord

- **Kết luận: Bỏ** làm nguồn tìm niche. Đã chọn niche rồi thì đọc tay kênh #feature-requests của server đối thủ.
- **Gap:** Vừa. Có thật nhưng nằm sau link mời.
- **Quan tâm:** Yếu.
- **Lấy được:** cấm.
- **Chi phí:** miễn phí.
- **Điều khoản:** Cao. Cấm scrape và cấm thương mại hoá dữ liệu.
- **Hợp app:** Mac · SaaS web.
- [Điều khoản](https://discord.com/terms)

#### 21 · Nhóm Facebook

- **Kết luận: Bỏ.** Chỉ đọc tay khi niche nhắm người không rành công nghệ.
- **Gap:** Vừa.
- **Quan tâm:** Yếu.
- **Lấy được:** cấm. Groups API bị Meta gỡ từ 04/2024 (theo nguồn phụ).
- **Chi phí:** miễn phí.
- **Điều khoản:** Cao. Có điều khoản riêng cấm thu thập tự động.
- **Hợp app:** iOS / Android · vật lý.
- [Điều khoản thu thập tự động](https://www.facebook.com/legal/automated_data_collection_terms)

#### 22 · MacRumors Forums

- **Kết luận: Bỏ.** Không kiểm được (403). Apple Community + Ask Different đã phủ cùng đối tượng.
- **Gap:** Vừa.
- **Quan tâm:** Vừa.
- **Lấy được:** chỉ làm tay.
- **Chi phí:** miễn phí.
- **Điều khoản:** `chưa đo`.
- **Hợp app:** Mac · iOS.
- [Mục Mac Apps](https://forums.macrumors.com/forums/mac-apps-and-mac-app-store.71/)

### Chợ app và review

#### 23 · App Store / Mac App Store review

- **Kết luận: Đã có** ([Phase 2](phase-2-app-store.md)). Sẽ đào sâu ở [Phase 18 · Đối thủ bị chê gì](phase-18-competitor-complaints.md).
- **Gap:** Mạnh. Review 1–3★ chê thẳng đối thủ.
- **Quan tâm:** Vừa. Mặt app Mac rất mỏng: feed "Top Paid Mac Apps" trả 0 mục, trang web của Magnet ghi "chưa đủ đánh giá". Đọc RSS review theo từng id app là cách chắc nhất.
- **Lấy được:** API miễn phí (RSS + iTunes Search).
- **Chi phí:** miễn phí.
- **Điều khoản:** Vừa. Điều khoản Media Services cấm scrape. Feed RSS lại do Apple tự phát công khai.
- **Hợp app:** Mac · iOS.
- [RSS review](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1475387142/sortby=mostrecent/json) · [Điều khoản](https://www.apple.com/legal/internet-services/itunes/us/terms.html)

#### 24 · AlternativeTo

- **Kết luận: Làm tay khi cần.** Mở trang "<đối thủ> alternatives", lọc nền tảng Mac, đọc bình luận chê và các app bị gắn "discontinued".
- **Gap:** Mạnh. Người ta vào đây vì chán app đang dùng. Ví dụ trang CleanMyMac có bình luận chê, và có người xin danh sách mới vì app cũ không chạy trên chip M2.
- **Quan tâm:** Vừa. Có like và số lựa chọn thay thế, nhưng mẫu nhỏ.
- **Lấy được:** đọc qua trình duyệt. Không có API công khai.
- **Chi phí:** miễn phí.
- **Điều khoản:** `chưa đo` (ToS 404). Tạm coi như cấm quét.
- **Hợp app:** mọi loại.
- [Trang đã mở](https://alternativeto.net/software/cleanmymac/about/)

#### 25 · Shopify App Store

- **Kết luận: Làm tay khi cần.** Lọc review 1–2★ của 2–3 app đối thủ, chép ý chê kèm giá.
- **Gap:** Mạnh. Review có ngày, chê cụ thể, có giá đang bán. Ví dụ app QuickBooks có 32% đánh giá 1★, giá $19.99–59.99 / tháng.
- **Quan tâm:** Mạnh.
- **Lấy được:** cấm (ToS 1.9).
- **Chi phí:** miễn phí.
- **Điều khoản:** Cao.
- **Hợp app:** SaaS web.
- [Trang đã mở](https://apps.shopify.com/quickbooks-online) · [Điều khoản](https://www.shopify.com/legal/terms)

#### 26 · Chrome Web Store

- **Kết luận: Làm tay khi cần.** Đọc review 1–2★ của extension đối thủ, ghi số người dùng.
- **Gap:** Vừa. Review tải bằng JS.
- **Quan tâm:** Mạnh. Có số người dùng, điểm và số đánh giá.
- **Lấy được:** đọc qua trình duyệt. Không có API dữ liệu store.
- **Chi phí:** miễn phí.
- **Điều khoản:** Vừa.
- **Hợp app:** Chrome ext.
- [Trang đã mở](https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh) · [Điều khoản](https://developer.chrome.com/docs/webstore/program-policies/terms)

#### 27 · Firefox Add-ons (AMO)

- **Kết luận: Làm tay khi cần.** Chrome không có API, nên khi xét một ngách extension thì gọi API này, xếp theo số người dùng để xem ngách có người dùng không.
- **Gap:** Vừa.
- **Quan tâm:** Mạnh. Có `average_daily_users` và số đánh giá.
- **Lấy được:** API miễn phí, không key.
- **Chi phí:** miễn phí.
- **Điều khoản:** Thấp.
- **Hợp app:** Chrome ext (gần đúng).
- [API đã gọi](https://addons.mozilla.org/api/v5/addons/search/?q=tab&sort=users&page_size=3)

#### 28 · Setapp

- **Kết luận: Bỏ.** Chỉ để xem app Mac nào "đáng trả phí".
- **Gap:** Yếu. Không có review chê.
- **Quan tâm:** Yếu. Chỉ có điểm %.
- **Lấy được:** đọc qua trình duyệt.
- **Chi phí:** xem miễn phí. Giá gói thành viên `chưa đo`.
- **Điều khoản:** Cao. Cấm bot.
- **Hợp app:** Mac · iOS.
- [Trang](https://setapp.com/apps) · [Điều khoản](https://setapp.com/terms-of-use)

#### 29 · Raycast Store

- **Kết luận: Bỏ** làm nguồn gap. Xin tính năng nằm ở GitHub `raycast/extensions`, tức nguồn 47.
- **Gap:** Yếu.
- **Quan tâm:** Mạnh. Có số cài từng extension.
- **Lấy được:** đọc qua trình duyệt.
- **Chi phí:** miễn phí.
- **Điều khoản:** Cao. Cấm scrape.
- **Hợp app:** Mac.
- [Store](https://www.raycast.com/store) · [Điều khoản](https://www.raycast.com/terms-of-service)

#### 30 · VS Code Marketplace

- **Kết luận: Bỏ.** Gap của dev tool xem qua GitHub Issues.
- **Gap:** Vừa.
- **Quan tâm:** Mạnh.
- **Lấy được:** cấm. Điều khoản cấm cả "harvesting, spidering, scraping".
- **Chi phí:** miễn phí.
- **Điều khoản:** Cao.
- **Hợp app:** dev tool.
- [Điều khoản](https://aka.ms/vsmarketplace-ToU)

#### 31 · WordPress plugin directory

- **Kết luận: Bỏ.** Dễ lấy nhất nhưng lệch hướng. Chỉ dùng khi định làm SaaS cho chủ site WordPress.
- **Gap:** Vừa. Có thread hỗ trợ chưa giải quyết.
- **Quan tâm:** Mạnh. API trả `active_installs`, `num_ratings`, `support_threads_resolved`.
- **Lấy được:** API miễn phí.
- **Chi phí:** miễn phí.
- **Điều khoản:** Thấp.
- **Hợp app:** SaaS web.
- [API đã gọi](https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[search]=backup)

#### 32 · Figma Community

- **Kết luận: Bỏ.**
- **Gap:** Yếu.
- **Quan tâm:** `chưa đo` (403).
- **Lấy được:** đọc qua trình duyệt.
- **Chi phí:** miễn phí.
- **Điều khoản:** Vừa.
- **Hợp app:** plugin SaaS.
- [Điều khoản](https://www.figma.com/legal/tos/)

#### 33 · G2

- **Kết luận: Bỏ.**
- **Gap:** Vừa. Review B2B có mục "dislike".
- **Quan tâm:** Mạnh.
- **Lấy được:** cấm. §9 cấm crawler, kể cả với nội dung công khai.
- **Chi phí:** `chưa đo`.
- **Điều khoản:** Cao.
- **Hợp app:** SaaS web.
- [Điều khoản](https://legal.g2.com/terms-of-use)

#### 34 · Capterra

- **Kết luận: Bỏ.** Trùng G2.
- **Gap:** Vừa.
- **Quan tâm:** `chưa đo`.
- **Lấy được:** chỉ làm tay (403).
- **Chi phí:** miễn phí.
- **Điều khoản:** Cao (giả định, không đọc được).
- **Hợp app:** SaaS web.
- [Trang](https://www.capterra.com/)

#### 35 · Trustpilot

- **Kết luận: Bỏ.** Chỉ liếc tay khi soi uy tín một đối thủ.
- **Gap:** Vừa. Chủ yếu chê dịch vụ, ít chê tính năng.
- **Quan tâm:** Mạnh.
- **Lấy được:** cấm. §4 cấm text / data mining cho mọi mục đích.
- **Chi phí:** miễn phí.
- **Điều khoản:** Cao.
- **Hợp app:** SaaS web · app bán trực tiếp.
- [Điều khoản](https://legal.trustpilot.com/for-everyone/terms-of-use-for-consumers)

#### 36 · SaaSHub

- **Kết luận: Bỏ.** Trùng AlternativeTo, không mở được (403).
- **Gap:** Vừa.
- **Quan tâm:** `chưa đo`.
- **Lấy được:** chỉ làm tay.
- **Chi phí:** miễn phí.
- **Điều khoản:** `chưa đo`.
- **Hợp app:** SaaS web · Mac.
- [Trang](https://www.saashub.com/)

### Bằng chứng tiền

#### 37 · TrustMRR

- **Kết luận: Đã có** ([Phase 38](phase-38-revenue.md)). Chỉ dùng nội bộ, không đăng lại dữ liệu.
- **Gap:** Vừa. Không cho thấy gap, nhưng cho thấy ngách nào có doanh thu đã xác minh.
- **Quan tâm:** Mạnh. Có MRR và doanh thu xác minh.
- **Lấy được:** API có key miễn phí. Gói standard 10 lệnh / phút, premium 60 lệnh / phút. Giá premium `chưa đo`.
- **Chi phí:** có gói free.
- **Điều khoản:** Vừa. Cho dùng nội bộ. Cấm hiển thị công khai, cấm dựng lại database, cấm đưa vào AI.
- **Hợp app:** mọi loại.
- [Docs API](https://trustmrr.com/docs/api) · [Điều khoản](https://trustmrr.com/terms)

#### 38 · Etsy (template số)

- **Kết luận: Làm tay khi cần.** Tìm "<việc> template", ghi 5 listing nhiều review nhất làm bằng chứng có người trả tiền.
- **Gap:** Vừa. Template bán chạy cho thấy có quy trình lặp lại mà người ta chịu trả tiền.
- **Quan tâm:** Mạnh. Có số review và nhãn bán chạy.
- **Lấy được:** cấm. Dùng API để nghiên cứu thị trường phải được Etsy cho phép.
- **Chi phí:** `chưa đo`.
- **Điều khoản:** Cao.
- **Hợp app:** SaaS web · Mac / iOS.
- [Docs API](https://developers.etsy.com/documentation/) · [Điều khoản API](https://www.etsy.com/legal/api)

#### 39 · Acquire.com

- **Kết luận: Bỏ.** TrustMRR cho cùng loại tín hiệu, lại có API.
- **Gap:** Yếu.
- **Quan tâm:** Vừa. Phần lớn số liệu phải đăng nhập.
- **Lấy được:** chỉ làm tay.
- **Chi phí:** người mua có gói free, gói trả phí từ $390 (đo 2026-10-26).
- **Điều khoản:** Cao. Cấm cả sao chép tay.
- **Hợp app:** SaaS web · iOS / Android.
- [Giá](https://acquire.com/pricing/) · [Điều khoản](https://acquire.com/terms/)

#### 40 · Flippa

- **Kết luận: Bỏ.** Chỉ lướt tay khi muốn xem một ngách bán được giá bao nhiêu.
- **Gap:** Yếu.
- **Quan tâm:** Mạnh. Doanh thu, lợi nhuận, giá chào hiện công khai.
- **Lấy được:** chỉ làm tay.
- **Chi phí:** miễn phí để xem.
- **Điều khoản:** Cao. §3 cấm data mining.
- **Hợp app:** SaaS web · iOS / Android · Chrome ext.
- [Trang đã mở](https://flippa.com/search?filter[property_type][]=saas) · [Điều khoản](https://flippa.com/terms-of-service)

#### 41 · Indie Hackers products

- **Kết luận: Bỏ.** TrustMRR đã thay vai trò này.
- **Gap:** Yếu.
- **Quan tâm:** Vừa.
- **Lấy được:** chỉ làm tay (403).
- **Chi phí:** miễn phí.
- **Điều khoản:** `chưa đo`.
- **Hợp app:** SaaS web.
- [Trang](https://www.indiehackers.com/products)

#### 42 · Starter Story

- **Kết luận: Bỏ.** Doanh thu tự khai, không có gap.
- **Gap:** Yếu.
- **Quan tâm:** Vừa.
- **Lấy được:** đọc qua trình duyệt, phải nhập email.
- **Chi phí:** có gói free. Gói Academy `chưa đo`.
- **Điều khoản:** Vừa.
- **Hợp app:** SaaS web · iOS / Android.
- [Trang](https://www.starterstory.com/) · [Điều khoản](https://www.starterstory.com/terms)

#### 43 · Gumroad Discover

- **Kết luận: Bỏ.**
- **Gap:** Yếu.
- **Quan tâm:** `chưa đo` (trang JS).
- **Lấy được:** cấm. §14(e) cấm scrape.
- **Chi phí:** miễn phí.
- **Điều khoản:** Cao.
- **Hợp app:** SaaS web · Mac.
- [Điều khoản](https://gumroad.com/terms)

#### 44 · Notion template marketplace

- **Kết luận: Bỏ.** Không có số để xếp hạng.
- **Gap:** Yếu.
- **Quan tâm:** Yếu. Số bán chỉ người bán xem được.
- **Lấy được:** đọc qua trình duyệt.
- **Chi phí:** xem miễn phí. Người bán chịu phí 8% + $0.40 mỗi giao dịch (đo 2026-10-26).
- **Điều khoản:** Vừa.
- **Hợp app:** SaaS web.
- [Trang](https://www.notion.com/templates)

#### 45 · Chợ template Excel / Sheets

- **Kết luận: Bỏ.** Etsy làm tay cho tín hiệu template tốt hơn.
- **Gap:** Yếu.
- **Quan tâm:** Yếu.
- **Lấy được:** đọc qua trình duyệt.
- **Chi phí:** miễn phí.
- **Điều khoản:** `chưa đo`.
- **Hợp app:** SaaS web · Mac.
- [Trang mẫu đã mở](https://www.someka.net/)

#### 46 · CodeCanyon

- **Kết luận: Bỏ.** Không mở được (403), lệch tệp.
- **Gap:** Yếu.
- **Quan tâm:** `chưa đo`.
- **Lấy được:** chỉ làm tay.
- **Chi phí:** miễn phí.
- **Điều khoản:** `chưa đo`.
- **Hợp app:** SaaS web · iOS / Android.
- [Trang](https://codecanyon.net/)

### Yêu cầu tính năng

#### 47 · GitHub Issues xếp theo 👍

- **Kết luận: Làm phase riêng** (đề xuất B).
- **Gap:** Mạnh. Issue mở lâu, nhiều 👍 trên repo app Mac / dev tool là tính năng người dùng xin mà maintainer không làm. Đó là cơ hội làm app riêng hoặc plugin. Gọi thử: 154.487 issue `label:"feature request"` còn mở. Đầu bảng có issue 1.463 👍.
- **Quan tâm:** Mạnh. API sort thẳng theo `reactions-+1`, có số comment và ngày mở.
- **Lấy được:** API miễn phí. Search API 10 lệnh / phút khi không token, 30 khi có token.
- **Chi phí:** miễn phí.
- **Điều khoản:** Thấp. AUP cho dùng dữ liệu công khai để research, chỉ cấm spam và bán thông tin cá nhân.
- **Hợp app:** Mac · SaaS web · Chrome ext.
- [API đã gọi](https://api.github.com/search/issues?q=label:%22feature+request%22+state:open+is:issue&sort=reactions-%2B1&order=desc) · [AUP](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies)

#### 48 · Canny (bảng góp ý công khai)

- **Kết luận: Làm tay khi cần.** Tìm "<đối thủ> feedback canny", xếp Top, chép 10 mục nhiều vote nhất mà chưa "Complete".
- **Gap:** Mạnh. Mỗi bảng là danh sách tính năng khách của đối thủ xin mà chưa được làm.
- **Quan tâm:** Mạnh. Có vote và trạng thái.
- **Lấy được:** đọc qua trình duyệt. API chỉ chủ bảng dùng được.
- **Chi phí:** đọc miễn phí.
- **Điều khoản:** Vừa. Cấm dùng lại nội dung cho mục đích thương mại.
- **Hợp app:** SaaS web · Mac · iOS / Android.
- [Bảng mẫu](https://feedback.canny.io/feature-requests) · [Điều khoản](https://canny.io/terms)

#### 49 · Featurebase (bảng góp ý công khai)

- **Kết luận: Làm tay khi cần.** Làm chung bước tay với Canny.
- **Gap:** Mạnh.
- **Quan tâm:** Mạnh.
- **Lấy được:** đọc qua trình duyệt.
- **Chi phí:** đọc miễn phí.
- **Điều khoản:** `chưa đo` (404).
- **Hợp app:** SaaS web · Mac · iOS / Android.
- [Bảng mẫu](https://feedback.featurebase.app/)

#### 50 · Upwork

- **Kết luận: Làm tay khi cần.** Tìm job theo từ khoá ngách, đếm số job lặp lại trong 30 ngày, ghi budget.
- **Gap:** Mạnh. Việc lặp lại người ta trả tiền thuê làm tay là gap có sẵn bằng chứng trả tiền.
- **Quan tâm:** Vừa. Có budget và số proposal.
- **Lấy được:** cấm. API chỉ cho tài khoản của mình.
- **Chi phí:** xem miễn phí, cần tài khoản.
- **Điều khoản:** Cao.
- **Hợp app:** SaaS web · Mac · Chrome ext.
- [Trang](https://www.upwork.com/)

#### 51 · Fiverr

- **Kết luận: Làm tay khi cần.** Gig dịch vụ lặp lại có hàng trăm review là ứng viên "đóng gói thành sản phẩm".
- **Gap:** Vừa. Đây là phía người bán, không phải người mua xin.
- **Quan tâm:** Vừa.
- **Lấy được:** chỉ làm tay (403).
- **Chi phí:** miễn phí.
- **Điều khoản:** `chưa đo`.
- **Hợp app:** SaaS web · Chrome ext · Mac.
- [Trang](https://www.fiverr.com/)

### Dữ liệu của mình

#### 52 · Google Search Console (oneclicktool.app)

- **Kết luận: Làm tay khi cần.** Câu tìm kiếm có nhiều lượt hiện mà trang mình chưa trả lời = vừa là bài cần viết, vừa là ứng viên app.
- **Gap:** Vừa. Chỉ thấy nhu cầu quanh site mình, không phải cả thị trường.
- **Quan tâm:** Mạnh. Có lượt hiện, click, vị trí.
- **Lấy được:** API miễn phí qua MCP đã cài. Số `/fix` lần này `chưa đo`: MCP báo thiếu file khoá trên máy đang chạy.
- **Chi phí:** miễn phí.
- **Điều khoản:** Thấp.
- **Hợp app:** Mac (trang `/fix`).
- **Lưu ý:** MCP này có tool xoá site / sitemap. Chỉ dùng tool đọc.

## MCP dùng kèm AI

Kiểm ngày 2026-10-26: sao và ngày commit đo bằng `gh api`, giá lấy từ trang giá chính thức. Với MCP cộng đồng, đã đọc
code server để xem nó đòi quyền gì. Không cài thêm cái nào.

- [Google Trends](https://github.com/cryptoken/GoogleTrendsMCP) — **Nên dùng** · cộng đồng · 2 sao · commit 2026-02-12 · free
- [Search Console](https://github.com/AminForou/mcp-gsc) — **Dùng khi cần** · cộng đồng · 2.028 sao · commit 2026-09-15 · free
- [Google Analytics](https://github.com/googleanalytics/google-analytics-mcp) — **Dùng khi cần** · chính chủ · 3.553 sao · commit 2026-10-22 · free
- [Apify](https://github.com/apify/apify-mcp-server) — **Dùng khi cần** · chính chủ · 13.162 sao · commit 2026-10-25 · $5 free / tháng
- [Firecrawl](https://github.com/firecrawl/firecrawl-mcp-server) — **Nên dùng** · chính chủ · 7.685 sao · commit 2026-10-23 · 1.000 credit free / tháng
- [Exa](https://github.com/exa-labs/exa-mcp-server) — **Nên dùng** · chính chủ · 5.168 sao · commit 2026-10-19 · $10 free / tháng
- [Tavily](https://github.com/tavily-ai/tavily-mcp) — **Dùng khi cần** · chính chủ · 2.460 sao · commit 2026-10-15 · 1.000 credit free / tháng
- [Perplexity](https://github.com/perplexityai/modelcontextprotocol) — **Dùng khi cần** · chính chủ · 2.589 sao · commit 2026-10-21 · $5 / 1.000 lệnh
- [Bright Data](https://github.com/brightdata/brightdata-mcp) — **Dùng khi cần** · chính chủ · 2.686 sao · commit 2026-10-20 · 5.000 lệnh free / tháng
- [DataForSEO](https://github.com/dataforseo/mcp-server-typescript) — **Dùng khi cần** · chính chủ · 255 sao · commit 2026-10-02 · nạp tối thiểu $50
- [SerpApi](https://github.com/serpapi/serpapi-mcp) — **Dùng khi cần** · chính chủ · 182 sao · commit 2026-10-12 · 250 lệnh free / tháng
- [reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy) — **Dùng khi cần** · cộng đồng · 865 sao · commit 2026-10-25 · free
- [mcp-server-reddit](https://github.com/Hawstein/mcp-server-reddit) — **Dùng khi cần** · cộng đồng · 184 sao · commit 2026-06-10 · free
- [mcp-hn](https://github.com/erithwik/mcp-hn) — **Nên dùng** · cộng đồng · 76 sao · commit 2025-07-14 · free
- [producthunt-mcp-server](https://github.com/jaipandya/producthunt-mcp-server) — **Không dùng** · cộng đồng · 55 sao · commit 2025-04-19 · free
- [mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript) — **Nên dùng** · cộng đồng · 492 sao · commit 2026-10-21 · free
- [mcp-appstore](https://github.com/appreply-co/mcp-appstore) — **Nên dùng** · cộng đồng · 78 sao · commit 2026-10-22 · free

Ghi chú từng cái (giá lấy từ trang giá của hãng, đo 2026-10-26):

- **Google Trends:** dựa trên `pytrends`, mà repo này đã archived từ 2024-08. Dễ gãy khi Google đổi hoặc chặn 429. SerpApi là đường dự phòng.
- **Search Console:** có tool `delete_site`, `delete_sitemap`. Chỉ gọi tool đọc.
- **Apify:** chạy được actor quét Reddit, TikTok, Pinterest, Amazon. Ví dụ actor Reddit từ $3.40 / 1.000 kết quả, nằm gọn trong $5 free mỗi tháng. Có tool ghi / xoá và telemetry bật sẵn. Chỉ bật nhóm `actors` + `docs`, đặt `TELEMETRY_ENABLED=false`.
- **Firecrawl · Exa:** bản hosted dùng không cần key (có giới hạn), chỉ đọc. Hợp để soi trang đối thủ, trang giá, bài "alternative to X".
- **Bright Data · Tavily:** cho phép đặt key thẳng trong URL, dễ lộ qua log. Dùng header hoặc biến môi trường.
- **DataForSEO:** đường rẻ nhất để có **số tìm kiếm thật** (SERP từ $0.0006, keyword từ $0.0012 / task). Phải nạp $50, anh quyết.
- **reddit-mcp-buddy:** code sạch. Tool đăng bài chỉ hiện khi bật `REDDIT_BUDDY_WRITE`, đừng bật. Không có key Reddit thì chỉ đọc được RSS.
- **producthunt-mcp-server:** không có license, bỏ từ 2025-04, mà API của Product Hunt lại cấm dùng thương mại.
- **mcp-appstore:** chỉ đọc, gọi thẳng iTunes và dùng `google-play-scraper` chuẩn. AppInsightMCP (25 sao) có nhiều tool hơn nhưng phụ thuộc fork riêng của tác giả, nên có rủi ro chuỗi cung ứng.

**Nên thử trước (free, không cần key):** mcp-appstore · Exa hosted · mcp-hn · mcp-youtube-transcript.

## Repo và tool

Đo bằng `gh api` ngày 2026-10-26. "Commit" là lần push gần nhất.

- [facundoolano/google-play-scraper](https://github.com/facundoolano/google-play-scraper) — 2.988 sao · commit 2026-10-17 · MIT · Google Play (ShotMatic đang dùng)
- [JoMingyu/google-play-scraper](https://github.com/JoMingyu/google-play-scraper) — 1.021 sao · commit 2024-08-05 · MIT · Google Play, bản Python, ít bảo trì
- [facundoolano/app-store-scraper](https://github.com/facundoolano/app-store-scraper) — 1.436 sao · commit 2025-07-27 · MIT · App Store
- [pat310/google-trends-api](https://github.com/pat310/google-trends-api) — 975 sao · commit 2022-11-25 · MIT · Trends (ShotMatic đang dùng, **đứng yên 4 năm**)
- [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) — 202.080 sao · commit 2026-10-23 · Unlicense · metadata YouTube
- [apify/crawlee](https://github.com/apify/crawlee) — 26.263 sao · commit 2026-10-25 · Apache-2.0 · đọc trang JS
- [microsoft/playwright](https://github.com/microsoft/playwright) — 98.502 sao · commit 2026-10-25 · Apache-2.0 · đọc trang JS
- [scrapy/scrapy](https://github.com/scrapy/scrapy) — 65.026 sao · commit 2026-10-22 · BSD-3 · crawl số lượng lớn
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) — 86.261 sao · commit 2026-10-22 · Apache-2.0 · trang → markdown cho LLM
- [adbar/trafilatura](https://github.com/adbar/trafilatura) — 7.022 sao · commit 2026-10-23 · Apache-2.0 · lấy chữ chính của trang
- [praw-dev/praw](https://github.com/praw-dev/praw) — 4.289 sao · commit 2026-10-25 · BSD-2 · Reddit API (cần app được duyệt)
- [ArthurHeitmann/arctic_shift](https://github.com/ArthurHeitmann/arctic_shift) — 1.734 sao · commit 2026-10-11 · không ghi · kho dump Reddit + API giới hạn
- [pushshift/api](https://github.com/pushshift/api) — 1.435 sao · commit 2023-04-06 · không ghi · **đã chết**, thay bằng Arctic Shift
- [HackerNews/API](https://github.com/HackerNews/API) — 13.375 sao · commit 2025-01-01 · MIT · HN chính thức (không tìm kiếm được)
- [algolia/hn-search](https://github.com/algolia/hn-search) — 607 sao · commit 2023-11-04 · — · repo archived, nhưng API vẫn chạy
- [MaartenGr/BERTopic](https://github.com/MaartenGr/BERTopic) — 7.912 sao · commit 2026-10-25 · MIT · gom câu hỏi thành chủ đề
- [MaartenGr/KeyBERT](https://github.com/MaartenGr/KeyBERT) — 4.224 sao · commit 2026-08-25 · MIT · rút keyword từ đoạn văn
- [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers) — 19.219 sao · commit 2026-10-23 · Apache-2.0 · vector câu để gộp cùng ý
- [INESCTEC/yake](https://github.com/INESCTEC/yake) — 1.892 sao · commit 2026-02-11 · không rõ · rút keyword không cần model
- [lorien/awesome-web-scraping](https://github.com/lorien/awesome-web-scraping) — 8.192 sao · commit 2026-09-19 · không rõ · danh sách tool scrape
- [mezod/awesome-indie](https://github.com/mezod/awesome-indie) — 11.906 sao · commit 2024-06-12 · không rõ · danh sách tài nguyên indie

Rút ra:

- **Rủi ro đang có:** `google-trends-api` mà ShotMatic dùng không cập nhật từ 2022. Ghi vào [Backlog 10 · Canary nguồn thật](phase-backlog-10-source-canary.md) để báo khi gãy.
- **Thay từ điển tay ở Phase 11:** BERTopic + sentence-transformers gom được hàng nghìn câu hỏi thành chủ đề. Đây là Python, nên nếu dùng thì chạy như bước tiền xử lý. Ghi vào Appendix làm ứng viên, chưa làm.
- **Arctic Shift** là đường lấy Reddit số lượng lớn mà không cần API Reddit. Repo không ghi license, nên chỉ dùng để research nội bộ.

## Phương pháp tìm gap

Mỗi phương pháp ghi cách làm, nguồn dùng và ShotMatic đã có chưa.

1. **SERP do diễn đàn chiếm.** Gõ câu hỏi lên Google. Nếu top 3 là Reddit, Quora hay Apple Community thì chưa có trang
   hay app tốt trả lời: vừa là gap nội dung, vừa là gap app. Nguồn: Google SERP (làm tay, hoặc SerpApi / DataForSEO).
   **Chưa có.** Nên thêm cờ "top 3 là diễn đàn" vào [Phase 59 · Kệ Google](phase-59-seo-shelf.md).
2. **"X alternative", "X vs Y", "X free".** Tìm người đang muốn bỏ app đang dùng. Nguồn: autocomplete, AlternativeTo.
   **Có một phần** (autocomplete ở Phase 1–2). Nên thêm các tiền tố này thành nút sẵn trong
   [Phase 40 · Explore](phase-40-explore-tree.md).
3. **"I'd pay for", "is there an app", "wish there was".** Nguồn: Reddit, HN, Stack Exchange, X.
   **Có ở Phase 11** (8 câu search mẫu). Đề xuất A và C dùng lại đúng các cụm này.
4. **Feature request bị bỏ ngỏ.** Issue nhiều 👍 mà maintainer đóng "won't fix" hoặc để mở hơn 1 năm. Nguồn: GitHub,
   Canny, Featurebase. **Chưa có.** Đây là đề xuất B.
5. **Câu xin phần mềm chưa có câu trả lời được chấp nhận.** Câu hỏi nhiều lượt xem mà `is_answered = false` hoặc câu
   trả lời top là "không có". Nguồn: Ask Different, Super User. **Chưa có.** Đây là đề xuất A.
6. **Đợt đổi nền tảng.** macOS / iOS mới (WWDC tháng 6, bản phát hành tháng 9) làm hỏng app cũ hoặc mở API mới. Cửa sổ
   niche ngắn, rất hợp app Mac. Nguồn: Trends "Rising", Apple Community, Ask Different sau ngày phát hành. **Chưa có.**
   Nên thêm lịch nhắc vào [Phase 42 · Theo dõi niche](phase-42-tracking.md).
7. **Tách tool lớn (unbundling).** Người dùng Excel / Notion / Photoshop chỉ để làm 1 việc nhỏ, lặp lại → làm app nhỏ đúng
   việc đó. Nguồn: Reddit, template bán chạy. **Chưa có**, làm tay.
8. **Template bán chạy.** Template Notion / Excel bán tốt nghĩa là có quy trình người ta muốn có app. Nguồn: Etsy (tay).
   **Chưa có**, làm tay.
9. **Extension nhiều người dùng mà điểm thấp.** Nguồn: Chrome Web Store (tay), Firefox AMO (API). **Chưa có**, làm tay.
10. **Jobs-to-be-Done từ review.** Đọc review theo "lúc nào dùng · để xong việc gì · vì sao đổi app". Nguồn: App Store,
    Google Play. **Có** ([Phase 18](phase-18-competitor-complaints.md) cùng lệnh `mine` của `/app-research`).
11. **Việc lặp lại trên Upwork / Fiverr.** Việc người ta trả tiền thuê làm tay mỗi tuần. **Chưa có**, làm tay.
12. **Search Console của mình.** Câu có nhiều lượt hiện mà trang mình chưa trả lời. Nguồn: GSC qua MCP. **Chưa có trong
    app.** Làm tay qua MCP khi có khoá.

## Đề xuất top 3 (đã duyệt 2026-10-26)

**Anh duyệt cả 3:** A + C gộp thành [Phase 12 · Q&A Gap](phase-12-qa-gap.md), B thành
[Phase 13 · GitHub Feature Request Gap](phase-13-github-gap.md). Làm trước Phase 12.

Cả 3 đều là API miễn phí, không cần trả tiền, và **dùng lại khung của Phase 11**: chuyên mục + chủ đề → bảng gap → bài
gốc → xuất `.md`. Mỗi cái chỉ cần thêm một collector và một nguồn trong bảng gap, không cần trang mới.

**A · Stack Exchange Q&A Gap** (Ask Different + Super User + Software Recommendations)

- **Vì sao:** cùng loại tín hiệu với Reddit, nhưng có API chính thức gọi được ngay (đã thử). Có view_count để xếp hạng,
  có cờ "đã giải" để tìm câu chưa ai giải.
- **Cỡ việc:** nhỏ. Không key thì 300 lệnh / ngày. Cache 7 ngày là đủ.

**B · GitHub Feature Request Gap**

- **Vì sao:** tín hiệu sạch nhất, có 👍 đếm sẵn, điều khoản thoáng nhất. Hợp app Mac, dev tool, extension.
- **Cỡ việc:** nhỏ. Search API 30 lệnh / phút khi có token cá nhân (anh tự tạo token, Claude không nhập thay).

**C · Hacker News Ask Gap**

- **Vì sao:** không key, có điểm và số bình luận, mạnh cho SaaS và dev tool.
- **Cỡ việc:** rất nhỏ. Có thể gộp chung với A thành một phase "Q&A Gap".

**Dự bị · X search:** tín hiệu mạnh nhưng tính tiền theo bài đọc. Anh quyết có chi không.

**So với phase cũ (Version 2):**

- **YouTube (31–32):** giữ. YouTube suggest yếu, nhưng transcript video review đọc được miễn phí qua MCP. Giá trị của
  phase này nằm ở phần AI đọc video, không ở gợi ý tìm kiếm.
- **Amazon (33–34):** đề xuất **hạ xuống ứng viên**. Gợi ý Amazon chỉ cho thấy hàng vật lý, còn điều khoản cấm data
  mining. ShotMatic chọn app phần mềm.
- **Google Maps (35):** chưa xét ở phase này, vì đây là nguồn cho business địa phương, không phải app. Giữ nguyên, xét
  khi tới.
- **Thứ tự gợi ý:** A + C (gộp) và B làm ngay sau Phase 11, trước Phase 12. Lý do: cả hai dùng chung bảng gap vừa làm
  xong, và cho thêm dữ liệu để Phase 18–20 chấm.

