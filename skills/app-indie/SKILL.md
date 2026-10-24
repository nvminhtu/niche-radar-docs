---
name: app-indie
description: "Skill phụ của pipeline app — học (clone cách làm, KHÔNG chép sản phẩm) từ indie hacker đang kiếm tiền thật: tìm 3–8 sản phẩm có doanh thu xác minh trên TrustMRR (danh bạ doanh thu nối thẳng Stripe/Lemon Squeezy/Polar/RevenueCat), Reddit (r/SideProject, r/indiehackers, r/macapps, r/ClaudeAI), X build-in-public, Product Hunt; mổ từng cái theo 7 trục (ý tưởng · cách làm/stack · giá & cổng thu tiền · kênh phân phối · SEO · quảng cáo · mindset của founder), rút pattern lặp lại, rồi áp vào sản phẩm của mình thành bảng việc có output ra đô (trang bán, bài SEO, post, đơn hàng) — ghi research/YYYY-MM-DD-indie-<chủ đề>.md, kiểm bằng scripts/check_indie.py; đẩy kết quả sang /app-research (ý tưởng), /app-money (giá, Lemon Squeezy/Polar, bán ngoài store), /app-marketing (kênh, SEO, TrustMRR), /app-grow (số verified). Use when 'học từ indie', 'clone ý tưởng', 'trustmrr', 'indie hacker kiếm tiền thế nào', 'họ bán bằng gì', 'họ seo thế nào', 'họ quảng cáo ở đâu', 'mindset indie', 'build in public', 'bán tool cho dân dev', 'bán cho dân vibe code', 'kiếm tiền từ code', 'tự bán không qua store', 'marc lou', 'pieter levels', 'tony dinh', 'teardown sản phẩm', 'đối thủ ngoài store bán sao'. Không chép tên/chữ/ảnh/code của sản phẩm mẫu, không bịa doanh thu, không đăng bài hay trả phí thay người dùng."
argument-hint: "[chủ đề / danh mục, vd 'dev tools', 'claude code', 'mac utility'] [--for <slug>]"
user-invocable: true
---

# app-indie — học cách các indie đang kiếm tiền, rồi làm y cách đó cho sản phẩm của mình

**Clone = chép CÁCH LÀM** (cách chọn ý, định giá, kênh, SEO, nhịp đăng bài, tư duy), **không chép SẢN PHẨM**
(tên, chữ, ảnh, code, UI). Chép sản phẩm vừa là vi phạm bản quyền, vừa là đường thẳng tới 4.3(a) Spam
(`reference/README-APP-PUBLISH-01-GUIDELINE-4-3-SPAM.md`) và bị khách dev bóc là hàng nhái.

Đọc trước: **[references/playbook.md](references/playbook.md)** — mindset, chiêu SEO, chiêu quảng cáo, cách dùng TrustMRR,
khuôn giá đã đo. Mỗi lần chạy skill này mà học được pattern mới có nguồn → thêm vào playbook.

Kết quả: `research/YYYY-MM-DD-indie-<chủ-đề>.md` (khuôn `templates/indie.md`) · kiểm:
`python3 scripts/check_indie.py research/<file>.md` tới 0 FAIL.

## Pha 1 — Chọn mẫu (3–8 sản phẩm)

Lọc theo **cái mình làm được và bán được**, không theo cái giàu nhất:

1. **TrustMRR** — số đã xác minh từ cổng thanh toán, nên ưu tiên số 1.
   - Danh mục: `https://trustmrr.com/category/<danh-mục>` (vd `developer-tools`, `artificial-intelligence`, `saas`, `productivity`).
   - Trang từng sản phẩm: `https://trustmrr.com/startup/<slug>` → đọc doanh thu 30 ngày, tổng, MRR, số khách, provider, founder, quốc gia, ngày lập, giá.
   - WebSearch `site:trustmrr.com <từ khoá>` khi chưa biết slug.
   - Ưu tiên mẫu **gần mình**: một người làm, không vốn, sản phẩm cài trên máy / tool dev / AI tool, 30 ngày $500–$20k
     (mẫu $1M MRR có team và vốn — học được ít).
2. **Reddit** — r/SideProject, r/indiehackers, r/macapps, r/ClaudeAI, r/ClaudeCode, r/vibecoding, r/SaaS: tìm bài
   "$X MRR", "first 100 customers", "how I got", "postmortem". Số trên Reddit là **tự khai** → ghi `tự khai` cạnh số.
3. **X / blog / Product Hunt** — founder đăng số, changelog, bài "what worked". Cũng là `tự khai` trừ khi có ảnh dashboard.
4. **Bắt buộc có ít nhất 1 mẫu thất bại hoặc chững** (doanh thu 30 ngày ~$0, đang rao bán, founder than) — học cái gì *không* chạy.

Ghi bảng `## Mẫu`. Không mở được trang → `SKIP · <lý do>`, không điền số từ trí nhớ.

## Pha 2 — Mổ từng mẫu theo 7 trục

Với mỗi mẫu, đi đủ các nguồn: trang TrustMRR → website (trang chủ, pricing, blog, changelog, docs) → X/GitHub của founder
→ Product Hunt / HN / Reddit nhắc tới nó. Mỗi trục một dòng, có bằng chứng (link hoặc thứ đã thấy):

| Trục | Hỏi gì | Đo bằng gì |
|---|---|---|
| **Ý tưởng** | giải việc gì, cho ai, khác đồ miễn phí ở đâu | câu hero của site, review, bài ra mắt |
| **Làm** | stack, nền tảng (web / Mac / Windows / extension / API), làm bao lâu, 1 người hay team | founder kể, `whatruns`/source trang, GitHub |
| **Giá** | mua đứt / subscription / lifetime / theo lượng, giá, free tier ra sao, cổng thu (Lemon Squeezy / Polar / Paddle / Stripe / store) | trang pricing + provider trên TrustMRR |
| **Kênh** | khách đầu tiên đến từ đâu, kênh nào đang chạy | X (tần suất đăng), PH, HN, Reddit, GitHub stars, newsletter, affiliate, directory |
| **SEO** | blog bao nhiêu bài, kiểu trang (so sánh "X vs Y", "X alternative", tool free, trang theo từng từ khoá) | `<site>/sitemap.xml` đếm URL, đọc 3 tiêu đề bài, backlink từ TrustMRR/directory |
| **Quảng cáo** | có trả tiền không, ở đâu (X ads, Google, sponsor newsletter, TrustMRR sponsor, creator) | founder kể; không thấy dấu → `không thấy` |
| **Mindset** | founder nghĩ gì về làm / bán / bỏ — 1 câu trích ≤ 15 từ có link, hoặc diễn đạt lại | X, phỏng vấn, mục "founder note" trên TrustMRR |

Thấy được thì ghi, không thấy thì `không thấy` / `chưa đo` — **không đoán** kênh hay doanh thu.

## Pha 3 — Rút pattern

Viết `## Pattern`: thứ **lặp ở ≥ 2 mẫu** (vd "tool dev bán mua đứt $19–99 qua Lemon Squeezy/Polar", "khách đầu tiên từ X
của chính founder", "blog so sánh 'alternative' kéo traffic"). Mỗi pattern ghi mẫu nào. Thêm `## Phản mẫu` — thứ mẫu
thất bại làm (vd "làm xong rồi mới đi tìm khách", "không có kênh riêng").

## Pha 4 — Áp vào sản phẩm của mình (`--for <slug>` hoặc hỏi)

Bảng `## Áp vào` — mỗi dòng là **một việc ra đô** (trang bán, bài blog, post, đơn đầu, email, listing TrustMRR),
có hạn, học từ mẫu nào. Tối thiểu 1 dòng mỗi trục Giá · Kênh · SEO; trục Ý tưởng thì viết **điểm khác** của mình
(cái mẫu không có), không viết "làm giống X".

Rồi `## Không chép` — checklist tick hết: tên khác hẳn · chữ trên site tự viết · ảnh/icon tự sinh (tuyến `core:asset-prompt`) ·
không lấy code · luồng chính có thứ chỉ mình có.

## Pha 5 — Đổ vào pipeline

| Kết quả | Đi đâu |
|---|---|
| ý tưởng mới đáng làm | `/app-research` (dùng file này làm nguồn bằng chứng), rồi CỔNG 1 như thường |
| giá, mua đứt vs subscription, bán ngoài store | `/app-money` (`distribution: direct`, `Provider: Lemon Squeezy` / Polar) |
| kênh, SEO, TrustMRR, build in public | `/app-gtm` (lịch 6 tuần + file bài) · `/app-marketing` Pha 3 + `marketing.md` |
| đo số verified hằng tuần | `/app-grow` — nối provider vào TrustMRR khi có đơn đầu |
| pattern mới có nguồn | thêm vào `references/playbook.md` |

Câu trả lời cuối: link file research, 3 pattern mạnh nhất, 3 việc ra đô tuần này. Ghi `LEARNED.md` của app nếu có `--for`.

## Không làm

- Không chép tên, câu chữ, ảnh, icon, code, UI của mẫu. Trích lời founder ≤ 15 từ, có link.
- Không bịa / ước doanh thu. Số TrustMRR ghi `verified`, số Reddit/X ghi `tự khai`, không có → `chưa đo`. Luôn kèm ngày.
- Không đăng ký TrustMRR, không dán API key, không mua backlink/sponsor, không đăng bài thay người dùng — Claude soạn sẵn, người dùng bấm.
- Không biến research thành lý do làm app mới khi plan hiện tại chưa ra đô (Mindset #6 của CLAUDE.md) — ghi vào backlog.
