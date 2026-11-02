# Phase 46.3 · Blog shotmatic.app — mục Indie founders (market + tìm niche)

> Thêm **1 chuyên mục mới** trên [shotmatic.app/blog](https://shotmatic.app/blog) cho indie dev, solo founder, người làm
> micro SaaS: chọn market, đọc tín hiệu thị trường, tìm niche trước khi build. Khác mục `niche` đang có (cách kiểm 1 ý tưởng
> app bằng số store): mục này nói **ở tầm founder** — chọn chợ nào, đánh ai, bao nhiêu là đủ sống.

<span class="chip chip--todo">Plan · 2026-10-31 · chưa làm</span>

## Mục tiêu

- **Một chỗ cho người đang chọn làm gì**, chưa chọn app nào: đọc xong biết cách lọc market và có lý do tải ShotMatic.
- **Mỗi bài 1 từ khoá đã đo**, dẫn về đúng 1 trang đích (trang chủ, `/app-store-keyword-research`, `/app-competitor-analysis`, `/ai`).
- **Không chồng bài cũ:** chủ đề nào mục `niche` đã viết thì link sang, không viết lại.

**Xong khi:** chuyên mục `founders` có trang `/blog/category/founders`, ≥ 4 bài live đúng khuôn [46.1](phase-46-1-landing-blog.md),
mỗi bài có trong sitemap + `llms.txt` và đã gửi Search Console; số đo có nguồn + ngày, không có thì `chưa đo`.

## Tên chuyên mục

- Slug `founders`, tên hiện **Indie founders**, blurb: *Picking a market as a solo or small team: demand, money, competition — before you build.*
- **Không** dùng `ideas` hay `indie-marketing`: 2 tên này là chuyên mục blog ShotMatic cũ, đang 308 sang oneclicktool.app (`oldCategories` trong `next.config.js`).
- Thêm 1 dòng vào `categories` ở `lib/blog-meta.mjs` (repo `nvminhtu/shotmatic`) — thứ tự: sau `niche`, trước `product`.

## Số đo (Google Trends US 12 tháng + Autocomplete US, 2026-10-31)

Trends là số **tương đối 0–100 trong từng nhóm so sánh**, không phải lượt tìm. Volume tuyệt đối `chưa đo`.

| Nhóm so sánh | Từ khoá | Đỉnh 12 tháng | Ghi chú |
|---|---|---|---|
| Founder | side project | 100 (2026-06-07) | rộng, nhiều người không làm app |
| Founder | solo founder | 22 | Autocomplete lệch về *programs, grants, YC* |
| Founder | micro saas | 18 | related: *what is micro saas*, *micro saas examples* |
| Founder | bootstrapped | 15 | phần lớn là *bootstrapped meaning* — ý định đọc định nghĩa |
| Founder | indie hackers | 9 | đa số tìm tên cộng đồng, không phải câu hỏi |
| Thị trường | market research | 100 (2026-06-07) | rất rộng, cạnh tranh lớn |
| Thị trường | app ideas | 15 | related đang lên: *mobile app ideas* |
| Thị trường | niche research | 2 | đuôi dài, đúng người |

Autocomplete đáng viết: *micro saas ideas 2026* · *micro saas ideas for solopreneurs* · *how to find a niche market* ·
*how to find a niche for business* · *mobile app ideas* · *what is micro saas*.

<div class="box box--danger" markdown>
**Trends có đứt gãy chung tuần 2026-07-12:** mọi từ khoá đo hôm nay (cả *google trends*, *market research*) tụt 50–70 % cùng một tuần
rồi đi ngang. Coi là thay đổi cách Google lấy mẫu, **không** phải nhu cầu giảm — so xu hướng chỉ trong cùng một phía của mốc đó.
</div>

## Bài (thứ tự = thứ tự viết)

Mỗi bài: SERP top 10 xem trước khi viết, "The short answer" 40–60 từ, H2 là câu người ta gõ, số tự đo có ngày, `sources` ≥ 2.

1. [ ] **Micro SaaS ideas for 2026: how to check demand before you build** — `micro saas ideas 2026` → trang chủ.
   Lấy 8–10 ý tưởng trên các list phổ biến, đo từng cái (Trends, store, đối thủ), chấm qua / trượt.
2. [ ] **What is micro SaaS? Examples measured, and what they really earn** — `what is micro saas` · `micro saas examples` → `/blog/validate-app-idea-before-you-build`.
   Chỉ ghi doanh thu có nguồn công khai (TrustMRR, bài tự công bố); không có thì `not measured`.
3. [ ] **How to find a niche market for an app (as a solo founder)** — `how to find a niche market` → trang chủ.
   Khác bài `find-your-niche-before-you-build`: bài này đi từ market rộng xuống niche; bài cũ đi từ 1 ý tưởng. Link qua lại.
4. [ ] **Mobile app ideas: read the market, not the list** — `mobile app ideas` → `/app-competitor-analysis`.
   Chỉ viết nếu SERP còn chỗ cho blog nhỏ (Phase 59 chưa có → xem tay top 10).
5. [ ] **Side project to paid app: the 3 numbers to check first** — `side project ideas` (`chưa đo` — đo trước khi viết) → trang chủ.

<div class="box box--rules" markdown>
**Luật**

- Không bịa doanh thu / MRR của người khác — chỉ số có link nguồn và ngày đọc
- Bài nói ở tầm founder, nhưng ví dụ luôn là app thật đo bằng ShotMatic (màn hình thật ở `app-demo`)
- Tiếng Anh, khuôn `content/blog/<slug>.md` của 46.1; CTA là Download (để lại email)
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Bài định nghĩa trần (*bootstrapped meaning*, *indie hacker meaning*) — người đọc không đi tìm tool
- Bài phỏng vấn / tin tức founder — không có số tự đo, AI search không trích
- Bài về Google Trends — để riêng ở [Phase 46.4](phase-46-4-google-trends-guide.md)
</div>

[Tổng quan Version 11](version-11.md) · Code ở repo `nvminhtu/shotmatic` · Skill: `/oneclicktool-blog` (khuôn bài), `marketing-skills:content-strategy`
