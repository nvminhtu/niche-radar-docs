# Đối thủ — tool phân tích thị trường

> 15 sản phẩm người dùng có thể dùng thay **một phần** việc ShotMatic làm, chia 4 nhóm. Codex tìm bằng web search
> và mở trang chính thức từng cái; Claude mở lại 10 link để kiểm. Mô tả lấy từ trang của nhà cung cấp, **chưa dùng thử**.
> Giá chỉ ghi khi đọc thấy trên trang giá chính thức, không thấy thì ghi `chưa rõ`.

<span class="chip chip--todo">Đọc 2026-11-05 · thêm AppKittie 2026-11-07 · chưa dùng thử sản phẩm nào</span>

<div class="box box--goal" markdown>
**Dùng trang này để**

- Viết câu định vị ShotMatic: chỗ nào giống họ, chỗ nào khác thật.
- Chọn keyword so sánh cho blog (vd "AppTweak alternative for indie devs") — đo trước ở [Google Search Suggestion → Blog](google-search-suggestion.md), không viết theo cảm tính.
- Học cách họ trình bày số, giá, landing.

Sổ đầy đủ (gồm Wow Keywords, đối tác, tham khảo): [Đối thủ · Đối tác · Tham khảo](../doi-thu-tham-khao.md).
</div>

## Mở 6 cái này trước

1. **[AppKittie](https://www.appkittie.com/)** — landing và cách bán làm tốt: cùng khách người làm app, ChatGPT đang gợi ý họ (thêm 2026-11-07).
1. **[Preuve AI](https://preuve.ai/)** — gần ShotMatic nhất: nhập ý tưởng → AI agent tra nguồn → chấm điểm → báo cáo, và chuyển báo cáo sang Claude Code / Codex để xây MVP.
2. **[Astro](https://tryastro.app/)** — app Mac nghiên cứu keyword App Store, cùng kiểu "tool desktop cho developer" như ShotMatic.
3. **[PainOnSocial](https://painonsocial.com/)** — biến thảo luận Reddit thành pain point có trích dẫn link gốc.
4. **[Appbot](https://appbot.co/)** — gom lời chê trong review app theo chủ đề, so với đối thủ, có MCP.
5. **[AppTweak](https://www.apptweak.com/en)** — ASO chuyên sâu; xem cách họ giải thích độ khó / cơ hội keyword.

!!! warning "Điểm khác biệt phải viết lại"
    Preuve AI đã nêu trên trang giá: có MCP và chuyển ngữ cảnh báo cáo sang Claude Code / Codex. Vậy câu "research nối
    sang coding agent" **không còn đủ** để nói ShotMatic khác. Chỗ khác cần nói rõ hơn: chạy local trên máy, dữ liệu
    thật từ cả Google Play + App Store + Trends, và chấm sức khoẻ niche app (không phải ý tưởng kinh doanh chung).

## 1. ASO / keyword cho app store

### AppTweak

- **Link:** [apptweak.com](https://www.apptweak.com/en) · **Giá:** Essential 79 USD/tháng, 949 USD/năm ([trang giá](https://www.apptweak.com/en/pricing))
- **Làm gì:** keyword, thứ hạng, đối thủ trên app store; thêm Market Intelligence, quản lý review, Apple Ads.
- **Giống:** dùng keyword + dữ liệu đối thủ để đánh giá cơ hội app. **Khác:** chuyên vận hành ASO sau khi đã có app, rộng hơn bước chọn niche.
- **Nên học:** tách độ phổ biến, độ khó, cơ hội thành từng chỉ số có giải thích, không chỉ 1 điểm tổng.

### Appfigures

- **Link:** [appfigures.com](https://appfigures.com/) · **Giá:** Starter miễn phí · Connect 9,99 USD/tháng · Optimize 149,99 USD/tháng ([trang giá](https://appfigures.com/platform/pricing))
- **Làm gì:** analytics app + ASO + theo dõi đối thủ + dữ liệu thị trường app.
- **Giống:** tìm cơ hội từ keyword, xu hướng, app cạnh tranh. **Khác:** nối số liệu app của chính người dùng (doanh thu, subscription); quyền nghiên cứu đối thủ chia theo gói.
- **Nên học:** tách rõ số của app mình với số ước của đối thủ, để người đọc không coi chúng chắc như nhau.
- **Đã ghi vào plan:** Competitors report + Competitor Keywords (so 1–8 app, bảng keyword × hạng từng app) → [Phase 56 · So sánh đối thủ](../web/phase-56-compare-competitor.md#hoc-tu-appfigures) (đọc 2026-11-06).

### Astro

- **Link:** [tryastro.app](https://tryastro.app/) · **Giá:** 108 USD/năm cho 1 Mac (trang ghi tương đương 9 USD/tháng, có thể cộng thuế)
- **Làm gì:** app macOS nghiên cứu keyword App Store, theo dõi hạng, xem keyword + rating đối thủ. Trang nêu số popularity lấy từ Apple Search Ads.
- **Giống:** tool desktop cho developer, gom keyword + cạnh tranh vào 1 màn. **Khác:** chỉ ASO App Store, trả theo năm (không mua 1 lần).
- **Nên học:** 1 màn gọn, đặt popularity, difficulty, diễn biến hạng ngay cạnh keyword.

### ASOMobile

- **Link:** [asomobile.net](https://asomobile.net/en/) · **Giá:** ASO Indie 59 USD/tháng · Maximum 299 USD/tháng ([trang giá](https://asomobile.net/en/pricing/))
- **Làm gì:** bộ ASO cho Google Play + App Store: keyword, review, đối thủ, phân tích thị trường.
- **Giống:** cùng soi 2 store, keyword, app cạnh tranh. **Khác:** theo dõi keyword IAP, cập nhật đối thủ; số tải / doanh thu đối thủ chỉ ở gói Maximum.
- **Nên học:** so cùng 1 cơ hội giữa 2 store để thấy store nào dễ chen hơn.

## 2. Tìm niche / ý tưởng

### Exploding Topics

- **Link:** [explodingtopics.com](https://explodingtopics.com/) · **Giá:** `chưa rõ` — [trang giá](https://explodingtopics.com/pricing) không đọc được số
- **Làm gì:** kho xu hướng, sản phẩm, startup đang lên; theo dõi chủ đề theo thời gian.
- **Giống:** tín hiệu nhu cầu + thời điểm để chọn niche. **Khác:** khám phá rộng (SaaS, hàng tiêu dùng), không soi cạnh tranh trong app store.
- **Nên học:** vẽ đường tăng theo thời gian để phân biệt nhu cầu bền với đợt tăng ngắn.

### PainOnSocial

- **Link:** [painonsocial.com](https://painonsocial.com/) · **Giá:** Starter 19 USD/tháng sau dùng thử · Professional 49 USD/tháng (mục giá trên trang chủ)
- **Làm gì:** đọc thảo luận Reddit theo subreddit + khoảng thời gian, nhóm pain point, chấm tần suất / cường độ, gợi ý giải pháp, kèm link bài gốc.
- **Giống:** biến lời phàn nàn thành ý tưởng sản phẩm. **Khác:** đi sâu riêng Reddit; chưa trả lời câu "người ta có trả tiền không".
- **Nên học:** mỗi feature gap mở được câu gốc + ngày + cộng đồng, để người dùng tự kiểm kết luận AI.

### Trends.vc

- **Link:** [join.trends.vc](https://join.trends.vc/) (trends.vc chuyển sang đây) · **Giá:** Trends Pro 299 USD/năm ([trang gói Pro](https://access.trends.vc/))
- **Làm gì:** thư viện báo cáo thị trường + ý tưởng cho founder, ra bài mới hằng tuần, có cộng đồng.
- **Giống:** giúp chọn thị trường trước khi xây. **Khác:** báo cáo biên tập sẵn, không quét dữ liệu theo ý tưởng của người dùng.
- **Nên học:** gói mỗi niche thành 1 brief ngắn: cơ hội + câu hỏi cần kiểm tiếp.

## 3. Soi review / market intelligence

### AppKittie

> Đánh giá nhận định của ChatGPT về AppKittie + Appfigures và plan cho ShotMatic: [trang riêng](danh-gia-appkittie-appfigures-2026-11-07.md).

- **Link:** [appkittie.com](https://www.appkittie.com/) · **Giá:** 1 gói mở hết, 79 USD/tháng, hoặc 49 USD/tháng khi trả năm (bảng giá trên trang chủ, đọc 2026-11-07)
- **Làm gì:** kho app iOS + Android lọc theo doanh thu ước tính, lượt tải, ngày ra mắt; xem quảng cáo đang chạy + chi tiêu quảng cáo theo nước, video viral trên TikTok / Instagram / Shorts, keyword ASO, màn onboarding + paywall; nối ChatGPT / Claude để hỏi. Có trang [free tools](https://www.appkittie.com/tools) (1 tool tính giá theo nước) và affiliate 30% định kỳ.
- **Giống:** cùng nhóm khách (người làm app tìm cái đang thắng để làm theo), cùng cho hỏi bằng AI của mình. **Khác:** SaaS trả tháng, số doanh thu / quảng cáo là ước tính trên server của họ; ShotMatic chạy trên máy, trả 1 lần, chấm sức khoẻ niche từ keyword + review + Trends.
- **Nên học:** màn đầu landing là thẻ app có số; lời khen ghi rõ tên app + doanh thu của người nói; trang tool không cần đăng ký, có FAQ, cuối trang dẫn về sản phẩm. Link anh gặp có `utm_source=chatgpt.com`, tức ChatGPT đang gợi ý họ. Áp dụng ở [Plan 2 · mục 2](../web/phase-plan2-02-landing-guide-free-tool.md).

### Appbot

- **Link:** [appbot.co](https://appbot.co/) · **Giá:** Small 59 USD/tháng, hoặc 49 USD/tháng khi trả năm ([trang giá](https://appbot.co/plans-help-choose/))
- **Làm gì:** sentiment, cụm từ, chủ đề trong review app; so sao + sentiment với đối thủ. Có API, Ask Appbot, MCP.
- **Giống:** khai thác lời chê để tìm chỗ khác biệt. **Khác:** phân tích review liên tục cho app đang chạy, có dashboard; đã đưa review vào AI qua MCP.
- **Nên học:** gom review theo vấn đề, lọc theo sao + thời gian để biết lỗi còn tồn tại hay đã sửa.

### AppFollow

- **Link:** [appfollow.io](https://appfollow.io/) · **Giá:** `chưa rõ` — [trang giá](https://appfollow.io/pricing) không hiện số tiền
- **Làm gì:** theo dõi review, rating, ASO, đối thủ; tự phân loại / trả lời review, nối tool hỗ trợ khách.
- **Giống:** tìm điểm cần sửa từ feedback + đối thủ. **Khác:** cho đội vận hành app sau khi ra mắt; có MCP & AI Toolkit.
- **Nên học:** cho AI hỏi dữ liệu có cấu trúc, dùng lại cách phân tích — không chỉ xuất 1 báo cáo chữ.

### Sensor Tower

- **Link:** [sensortower.com](https://sensortower.com/) · **Giá:** `chưa rõ` — báo giá riêng từng khách ([trang liên hệ](https://sensortower.com/demo))
- **Làm gì:** dữ liệu app, web, quảng cáo, audience: lượt tải, doanh thu, sử dụng, retention, review.
- **Giống:** đánh giá quy mô cơ hội + vị thế đối thủ. **Khác:** dữ liệu hành vi + quảng cáo rộng hơn listing; số là mô hình hoá; có MCP.
- **Nên học:** ghi nhãn rõ số quan sát với số ước, kèm thị trường + thời kỳ.

### Similarweb

- **Link:** [similarweb.com](https://www.similarweb.com/) · **Giá:** `chưa rõ` cho dữ liệu app ([trang gói Web](https://www.similarweb.com/packages/web/) không đủ căn cứ)
- **Làm gì:** nghiên cứu thị trường số + đối thủ: traffic web, nhu cầu tìm kiếm, xu hướng app, review app.
- **Giống:** dùng tín hiệu nhu cầu + đối thủ để cân cơ hội. **Khác:** đối chiếu web với app, hợp niche có cả SaaS web lẫn app.
- **Nên học:** mở rộng danh sách đối thủ theo việc người dùng cần làm, tính cả website / SaaS thay thế app.

## 4. AI agent làm market research / validate ý tưởng

### Preuve AI

- **Link:** [preuve.ai](https://preuve.ai/) · **Giá:** Reality Check miễn phí · Founder Report 59 USD một lần ([trang giá](https://preuve.ai/pricing))
- **Làm gì:** trang mô tả AI agent tra nguồn trực tiếp, chấm khả thi, vẽ bản đồ đối thủ, tìm tín hiệu cộng đồng, viết báo cáo có nguồn.
- **Giống:** rất gần luồng ý tưởng → bằng chứng → điểm → khuyến nghị trước khi xây. **Khác:** thêm founder fit, business plan, kế hoạch tìm khách; có MCP + chuyển sang Claude Code / Codex.
- **Nên học:** mỗi phán quyết kèm rủi ro chính, nguồn chứng minh, và hướng đổi cụ thể.

### DimeADozen

- **Link:** [dimeadozen.ai](https://www.dimeadozen.ai/) · **Giá:** chấm ý tưởng miễn phí · Starter 9 USD · Entrepreneur 129 USD, trả 1 lần ([trang giá](https://www.dimeadozen.ai/pricing))
- **Làm gì:** báo cáo validation: nhu cầu, đối thủ, thị trường, kiếm tiền, rủi ro; trang nhấn mạnh dẫn nguồn kiểm được.
- **Giống:** giúp quyết định có xây hay không từ 1 mô tả ý tưởng. **Khác:** bán từng báo cáo, không phải tool local.
- **Nên học:** cho xem kết quả sơ bộ miễn phí trước, ý tưởng đáng làm mới mở nghiên cứu sâu.

### VenturusAI

- **Link:** [venturusai.com](https://venturusai.com/) · **Giá:** `chưa rõ` — không tìm thấy trang giá riêng
- **Làm gì:** phân tích ý tưởng kinh doanh bằng AI: SWOT, PESTEL, Five Forces, khách hàng, gợi ý marketing.
- **Giống:** biến mô tả ý tưởng thành phân tích có khung. **Khác:** khung chiến lược chung; trang không cho thấy có quét review app store.
- **Nên học:** chia báo cáo thành khách hàng · vấn đề · cạnh tranh · bước thử tiếp.

## Chưa xác minh được

- **Wow Keywords** — lần đọc này mở trang lỗi qua công cụ web; thông tin đọc 2026-10-26 vẫn ở [Đối thủ · Đối tác · Tham khảo](../doi-thu-tham-khao.md#wow-keywords).
- **IdeaBrowser** — trang chính thức trả HTTP 403, không đưa vào. Lỗi truy cập không có nghĩa sản phẩm đã đóng.
- Chưa sản phẩm nào thay được **toàn bộ** ShotMatic; mỗi cái thay 1 phần việc.

## Liên quan

[Tổng quan · 2.000 active user / tháng](../web/PLAN-ANALYTICS-2000-active-users-per-month.md) ·
[Google Search Suggestion → Blog](google-search-suggestion.md) · [AEO / GEO](aeo-geo.md) ·
[Đối thủ · Đối tác · Tham khảo](../doi-thu-tham-khao.md)
