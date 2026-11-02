# Research · SaaS làm marketing thế nào (traffic · event · blog · kênh · tool)

> Trả lời 5 câu: SaaS trung bình có bao nhiêu active user trên GA, log event gì, có blog không, đăng bài ở đâu thì
> người ta chịu trả tiền, và các trang SaaS xài tool gì. Mọi số có nguồn + ngày tra (2026-11-02). Số **tính** = suy ra từ số có nguồn, không phải đo.
> Số **giả định** = đoán để đặt mục tiêu.

<span class="chip chip--done">Research 2026-11-02</span>

<div class="box box--goal" markdown>
**Kết luận nhanh cho ShotMatic**

- Không có "số trung bình" đáng tin cho SaaS nhỏ. Thay vào đó tính ngược từ mục tiêu đơn: muốn **10 đơn / tháng** cần
  khoảng **2.700 visitor / tháng ≈ 90 / ngày** (tính, xem bảng phễu bên dưới).
- Event cần log: đủ phễu `page_view → store_click / download → sign_up / generate_lead → begin_checkout → purchase`,
  không cần nhiều hơn ~10 event.
- Có blog: ~85% SaaS lớn có blog. Blog là kênh chậm (đơn đến sau 3–6 tháng), không phải kênh đơn đầu tiên.
- Kênh ra đơn đầu: **cộng đồng (Reddit) + chợ / thư mục + Product Hunt**, sau đó mới SEO. Chỉ chạy 2–3 kênh cùng lúc.
</div>

## 1. Một SaaS có bao nhiêu active user trên GA?

### Đọc số GA4 cho đúng trước đã

| Điều cần biết | Vì sao quan trọng |
|---|---|
| "Monthly" trong GA4 = **28 ngày cuộn**, không phải tháng lịch | so với số tháng của Stripe sẽ lệch |
| **Không cộng** số active user từng ngày ra số tháng | người quay lại bị đếm nhiều lần → luôn phóng to |
| "Active user" của GA4 khắt khe hơn Universal Analytics cũ (phiên > 10 giây, hoặc ≥ 2 trang, hoặc có key event) | số GA4 thấp hơn số "visitor" của Plausible / Vercel Analytics — bình thường |
| Người chặn cookie / adblock không vào GA4 | GA4 thường thiếu so với log server |

### Số tham khảo có nguồn

| Chỉ số | Số | Nguồn · độ tin |
|---|---|---|
| MAU trung vị website SaaS | ~2.500–3.200 / tháng | bài tổng hợp trích Databox, chính bài đó ghi 2 số khác nhau → **tin thấp** |
| Engagement rate SaaS / B2B software | 38–45% | WebFX (vendor, không rõ cách đo) → tin trung bình |
| Thời gian phiên SaaS | 45 giây – 1 phút 15 | WebFX |
| Số trang / phiên | 1,2–1,7 | WebFX |
| 50% indie hacker đang build | $0–1K MRR | khảo sát cộng đồng, ghi là ước lượng |

!!! warning "Không có số trung bình chuẩn"
    Không tìm thấy khảo sát nào đo traffic GA4 của SaaS nhỏ / indie. Số trên gom cả SaaS lớn. Dùng phễu bên dưới để
    đặt mục tiêu, đừng so mình với "trung bình".

### Tính ngược: cần bao nhiêu traffic để có đơn

| Bước phễu | Tỉ lệ | Nguồn |
|---|---|---|
| Visitor → bắt đầu dùng thử (không đòi thẻ) | 2–7% tuỳ ngành, dev tool 3,5–7,1% | tổng hợp 2025 (PoweredBySearch, UXCam) |
| Visitor → dùng thử khi **đòi thẻ** | ~2% (không đòi thẻ ~10%) | First Page Sage / Flint |
| Visitor → lead cả site B2B SaaS | ~1–2% | First Page Sage 2025 |
| Visitor từ **bài blog** → dùng thử | 0,3–1% | tổng hợp benchmark |
| Dùng thử → trả tiền | trung vị ~18,5% (15–28%) | phân tích 10.000+ SaaS |

**Tính cho ShotMatic** (giả định visitor → tải 2%, tải → mua 18,5%):

| Mục tiêu đơn / tháng | Lượt tải cần | Visitor / tháng | Visitor / ngày |
|---|---|---|---|
| 10 | ~54 | ~2.700 | ~90 |
| 30 | ~162 | ~8.100 | ~270 |
| 100 | ~540 | ~27.000 | ~900 |

Số GA4 thật của shotmatic.app: `chưa đo` trong trang này — lấy bằng GA4 MCP (`run_report`, metric `activeUsers`,
khoảng 28 ngày) rồi điền vào [Kế hoạch bán ShotMatic](../app/ke-hoach-ban-shotmatic.md).

## 2. SaaS thường log event gì để làm marketing?

GA4 có sẵn tên **recommended event** (`sign_up`, `login`, `generate_lead`, `begin_checkout`, `purchase`, `search`…).
Dùng đúng tên này thì GA4 tự dựng báo cáo; event tự đặt (`trial_started`) chỉ xem được trong Explorations.

- **Đến** — `page_view`, `session_start`
    - Tên chuẩn GA4: tự có
    - Tham số nên gửi: `utm_source`, `utm_campaign`
    - Trả lời: kênh nào mang người tới

- **Quan tâm** — `scroll` 90%, `video_start`, `view_pricing`
    - Tên chuẩn GA4: 2 cái đầu tự có (Enhanced measurement), `view_pricing` tự đặt
    - Tham số nên gửi: `page`, `section`
    - Trả lời: landing có giữ được người không

- **Hành động** — `store_click`, `file_download` (.dmg)
    - Tên chuẩn GA4: `file_download` tự có
    - Tham số nên gửi: `product`, `store`, `platform`
    - Trả lời: bao nhiêu người muốn thử

- **Để lại liên lạc** — `generate_lead` (email)
    - Tên chuẩn GA4: chuẩn
    - Tham số nên gửi: `form`, `product`
    - Trả lời: danh sách chờ lớn tới đâu

- **Đăng ký / dùng thử** — `sign_up`, `trial_started`
    - Tên chuẩn GA4: `sign_up` chuẩn, `trial_started` tự đặt
    - Tham số nên gửi: `method`, `plan`
    - Trả lời: phễu rơi ở bước nào

- **Kích hoạt** — `first_research_done` (lần đầu ra giá trị)
    - Tên chuẩn GA4: tự đặt
    - Tham số nên gửi: `niche_count`
    - Trả lời: người dùng có tới "aha" không

- **Tiền** — `begin_checkout`, `purchase`, `refund`
    - Tên chuẩn GA4: chuẩn
    - Tham số nên gửi: `value` (số), `currency`, `plan_name`, `transaction_id`
    - Trả lời: doanh thu theo kênh

- **Giữ chân** — `login`, `feature_used`, `subscription_cancel`
    - Tên chuẩn GA4: `login` chuẩn
    - Tham số nên gửi: `feature`
    - Trả lời: ai bỏ, bỏ sau tính năng nào

Luật đặt tên: chữ thường + gạch dưới, giữ tên chuẩn của Google, event tự đặt viết cùng một kiểu. Mỗi property tối đa
**30 key event**, mỗi event tối đa **25 tham số** — chỉ đánh dấu key event cho `generate_lead`, `file_download` /
`store_click`, `begin_checkout`, `purchase`.

!!! tip "App Mac chạy local"
    Event trong app (kích hoạt, dùng tính năng) không đi qua GA4 web. Nếu cần, gửi qua Measurement Protocol hoặc chỉ
    đếm phía license server — quyết khi làm, không thêm theo dõi ngầm mà người dùng không biết.

## 3. SaaS thường có blog không?

| Phát hiện | Số | Nguồn |
|---|---|---|
| 250 SaaS lớn nhất **không** có blog | 38 / 250 ≈ 15% → **~85% có blog** | Emily Byford, 2019 (có mẫu rõ, nhưng cũ) |
| 250 SaaS tăng nhanh nhất không có blog | 35 / 250 = 14% | Emily Byford, 2019 |
| "98% / 90% SaaS có blog" | hay được trích | trang tổng hợp chép nhau, không rõ mẫu → tin thấp |
| Kênh được founder nhắc nhiều nhất (479 phỏng vấn Indie Hackers) | SEO 83 lượt — nhưng **thêm sau khi đã có đà** từ kênh khác | Zero to Users, 2020 |

**Nghĩa là:** có blog là chuẩn, nhưng blog là kênh tích luỹ. Bài blog dẫn tới dùng thử chỉ 0,3–1% (bảng phễu trên).
Với ShotMatic, blog (Phase 46.1–46.3) là kênh `dài hạn`, không phải nơi ra 10 đơn đầu.

## 4. Đăng bài và seeding ở 10 nền tảng nào?

Số về "kênh ra đơn đầu tiên" (không có khảo sát nào chuẩn, các mẫu nhỏ và lệch nhau):

| Mẫu | Kênh dẫn đầu | Nguồn |
|---|---|---|
| 70 solo founder, 2023–2026 | cộng đồng người khác dựng 34%, riêng **Reddit 25%**; không ai có đơn đầu từ quảng cáo | lead-scorer.com (blog vendor) |
| 326 dự án trên Hacker News, 2025 | truyền miệng (40), **app store / chợ** (33), Google search (27) | IndieLaunches |
| 479 phỏng vấn Indie Hackers, 2020 | SEO (83), chợ + Product Hunt (77 mỗi kênh), cold email (42) | Zero to Users |
| ~50 launch top 10 Product Hunt, 2024 | chỉ ~50% thấy tăng đăng ký, **42% thấy tăng doanh số** | MySignature |

10 nền tảng, xếp theo mức hợp với khách **chịu trả tiền cho tool indie / founder** (đánh giá định tính từ nguồn trên,
không phải số đo):

1. **Reddit** (r/SideProject, r/indiehackers, r/SaaS, r/iOSProgramming, r/androiddev, r/EntrepreneurRideAlong) — hợp trả tiền: **cao**
    - Dạng bài: trả lời câu hỏi, case study có số
    - Lưu ý: đóng góp nhiều tuần trước khi nhắc sản phẩm; đọc luật từng sub

2. **Chợ / thư mục** (Mac App Store, Setapp, Chrome Web Store, AlternativeTo, SaaSHub, G2/Capterra) — hợp trả tiền: **cao**
    - Dạng bài: trang listing
    - Lưu ý: người vào đã có ý định mua — "app store / marketplace" đứng top ở 2/3 mẫu

3. **Google (SEO blog)** — hợp trả tiền: **cao nhưng chậm**
    - Dạng bài: bài trả lời 1 nỗi đau
    - Lưu ý: tích luỹ 3–6 tháng; blog → thử chỉ 0,3–1%

4. **X (build in public)** — hợp trả tiền: **trung bình–cao**
    - Dạng bài: thread số thật, ảnh chụp app
    - Lưu ý: hợp khi khách là indie dev — đúng chân dung ShotMatic

5. **Product Hunt** — hợp trả tiền: **trung bình (1 lần)**
    - Dạng bài: ngày launch
    - Lưu ý: đỉnh 1 ngày; 42% launch top 10 có tăng doanh số

6. **Hacker News** (Show HN) — hợp trả tiền: **trung bình, rủi ro cao**
    - Dạng bài: Show HN + trả lời bình luận
    - Lưu ý: được thì rất lớn, hỏng thì im; không xin upvote

7. **Indie Hackers** — hợp trả tiền: **trung bình**
    - Dạng bài: bài milestone, câu chuyện doanh thu
    - Lưu ý: cộng đồng đúng khách, traffic nhỏ

8. **YouTube** (dài + Shorts) — hợp trả tiền: **trung bình**
    - Dạng bài: demo, tutorial "tìm niche app"
    - Lưu ý: tìm được lâu dài như SEO; tốn công dựng

9. **LinkedIn** — hợp trả tiền: **thấp với ShotMatic**
    - Dạng bài: post chuyên môn, nhắn trực tiếp
    - Lưu ý: mạnh cho B2B bán công ty; indie dev ít mua ở đây

10. **Discord / Facebook Group / Threads** — hợp trả tiền: **thấp–trung bình**
    - Dạng bài: trả lời trong nhóm
    - Lưu ý: khó đo, dễ bị coi là spam; dùng để nghe nỗi đau

<div class="box box--star" markdown>
**Gợi ý chọn cho ShotMatic** (để Phase 47 chấm ICE)

- `chính`: **Reddit** + **chợ / thư mục** (người đã có ý định mua, dễ đo bằng `store_click`)
- `dài hạn`: **SEO blog** (đang làm ở Phase 46.x)
- `phụ`: X build in public, Product Hunt đúng 1 ngày ở Phase 49
- Theo một playbook 2026: indie thành công thường chỉ chạy 2–3 kênh, chi $0–100 / tháng cho tool marketing.
</div>

<div class="box box--danger" markdown>
**Không làm**

- Mua upvote, nhờ người upvote, đăng cùng 1 bài lên nhiều sub một lúc
- Lấy "số trung bình SaaS" làm mục tiêu — dùng phễu tính ngược
- Thêm event theo dõi ngầm trong app Mac mà người dùng không biết
</div>

## 5. Các trang SaaS thường xài tool gì?

### Số đo trên toàn web (W3Techs, 10/2026)

| Tool theo dõi traffic | % mọi website | % trong các web có dùng tool đo |
|---|---|---|
| Google Analytics | 46,9% | 81,9% |
| Microsoft Clarity | 4,2% | 7,3% |
| Hotjar | 1,7% | 2,9% |
| Không dùng tool nào W3Techs theo dõi | 42,8% | — |

Plausible, Umami, PostHog không có trong bảng của W3Techs (dưới ngưỡng báo cáo) — dù được giới indie nhắc nhiều.
Số này là **mọi website**, không riêng SaaS: không tìm thấy khảo sát nào đo riêng stack của SaaS có số %.

### Stack hay gặp theo từng việc

Các tên dưới đây lấy từ bài "stack của tôi" / danh sách tool 2025–2026 (ý kiến, không phải số đo thị phần).

1. **Đo traffic web** — GA4 (miễn phí, mặc định) · **Plausible** (gọn, không cookie, "mặc định của indie") · Umami (tự host)
2. **Xem người dùng bấm gì trên trang** — **Microsoft Clarity** (miễn phí: heatmap + quay phiên) · Hotjar (trả phí)
3. **Phân tích trong sản phẩm (event, phễu, giữ chân)** — **PostHog** (free 1 triệu event / tháng, hay được khuyên cho team nhỏ) · Mixpanel · Amplitude
4. **Tag / gom dữ liệu** — Google Tag Manager · Segment (công ty lớn, indie ít dùng)
5. **Thu tiền** — **Stripe** (mặc định nếu bán ở Mỹ / ít nước) · **Lemon Squeezy**, **Paddle** (merchant of record — lo thuế VAT hộ, phí ~5% + $0,5 với Lemon Squeezy)
6. **Email** — gửi email trong app: Resend, Postmark · email marketing / danh sách chờ: Loops (free tới 1.000 contact), Mailchimp, EmailOctopus, ConvertKit (Kit)
7. **CRM** — HubSpot bản free (B2B bán công ty); indie bán lẻ thường không cần
8. **SEO** — Google Search Console (bắt buộc, miễn phí) · Ahrefs / Semrush (trả phí, khi làm SEO nghiêm túc)
9. **Lên lịch đăng mạng xã hội** — Buffer, Typefully (X / LinkedIn)

<div class="box box--star" markdown>
**Stack đủ dùng cho ShotMatic (gợi ý, $0 / tháng)**

- Đo web: **GA4** (đang có) + **Microsoft Clarity** để xem người vào landing bấm / cuộn tới đâu
- SEO: **Search Console** (đang có MCP)
- Email: **EmailOctopus** (đang dùng) — chưa cần đổi
- Thu tiền: giữ cổng đang chốt ở Kế hoạch bán; nếu bán toàn cầu thì ưu tiên loại merchant of record để khỏi lo VAT
- Chưa cần: PostHog / Mixpanel (app Mac chạy local), Segment, HubSpot, Hotjar trả phí
</div>

## Nguồn (tra 2026-11-02)

- GA4 active user: [MeasureSchool](https://measureschool.com/ga4-active-users/) ·
  [Dolphin Analytics](https://www.dolphinanalytics.co.uk/blog/ga4-active-users-metrics) ·
  [MetricFixer](https://metricfixer.com/publications/analytics-conversion-tracking/ga4-users-active-new-returning-sessions-daily-totals) ·
  [WebFX GA4 benchmarks](https://www.webfx.com/blog/marketing/ga4-event-benchmarks/)
- Phễu chuyển đổi: [PoweredBySearch trial benchmarks](https://www.poweredbysearch.com/learn/b2b-saas-trial-conversion-rate-benchmarks/) ·
  [UXCam funnel benchmarks](https://uxcam.com/blog/b2b-saas-funnel-conversion-benchmarks/) ·
  [Flint free trial stats](https://www.flint.com/blog/b2b-saas-free-trial-conversion-rate-statistics) ·
  [SaaS Hero 2026 benchmarks](https://saashero.net/strategy/2026-b2b-saas-conversion-benchmarks/)
- Event GA4: [Stackmatix GA4 events](https://www.stackmatix.com/blog/ga4-events) ·
  [Custom events GA4](https://accs-net.com/custom-events-ga4-beyond-default-tracking/)
- Blog: [Emily Byford — State of SaaS Content Marketing 2019](https://medium.com/@EmilyByford/the-state-of-saas-content-marketing-2019-5d0532652588) ·
  [Biggest vs fastest-growing](https://medium.com/@EmilyByford/saas-content-marketing-the-biggest-vs-the-fastest-growing-companies-d10b64bf4400) ·
  [Mailmodo SaaS content stats](https://mailmodo.com/guides/saas-content-marketing-statistics)
- Kênh: [70 solo founder dataset](https://lead-scorer.com/blog/how-founders-get-first-customers-2026) ·
  [First customer statistics](https://mypip.io/first-customer/statistics) ·
  [Indie Hackers — first 33 paying customers](https://www.indiehackers.com/post/how-i-got-my-first-33-paying-customers-for-my-saas-513361a1b2) ·
  [Indie Hacker Marketing Playbook 2026](https://prems.ai/blog/indie-hacker-marketing-playbook-2026) ·
  [Micro-SaaS revenue](https://saasranger.com/blog/micro-saas-revenue-reality-what-1000-founders-actually-earn/)

- Tool: [W3Techs — traffic analysis tools](https://w3techs.com/technologies/overview/traffic_analysis) ·
  [W3Techs — Google Analytics](https://w3techs.com/technologies/details/ta-googleanalytics) ·
  [Venture Harbour — SaaS martech stack](https://ventureharbour.com/saas-martech-stack/) ·
  [Smol Launch — tool cho founder bootstrap](https://smollaunch.com/best-of/startup-marketing-tools-for-bootstrapped-saas-founders) ·
  [Sleek — analytics cho indie hacker](https://getsleek.io/blog/best-analytics-for-indie-hackers) ·
  [freeCodeCamp — tool stack indie hacker](https://www.freecodecamp.org/news/ultimate-tool-stack-for-indie-hackers/)

Liên quan: [Kế hoạch bán ShotMatic](../app/ke-hoach-ban-shotmatic.md) · [Phase 47 · Chọn 2 kênh](phase-47-two-channels.md) ·
[Phase 46.2 · Từ khoá + blog + Search Console](phase-46-2-seo-keyword-blog-gsc.md)
