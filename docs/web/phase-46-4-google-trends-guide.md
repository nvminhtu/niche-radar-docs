# Phase 46.4 · Blog shotmatic.app — Guide Google Trends (trend marketing cho app nhỏ)

> Một chuyên mục **guide** trên shotmatic.app/blog dạy dùng Google Trends để tìm niche, chọn từ khoá và quyết định
> trend nào đáng làm trang. Hai lợi: (1) người tìm "how to use google trends to find a niche" đúng là người ShotMatic bán cho
> (ShotMatic kéo Trends tự động); (2) chính bộ luật trong guide là cách ta bắt trend để **đưa người từ web vào app**.

<span class="chip chip--todo">Plan · 2026-10-31 · chưa làm</span>

## Trả lời câu hỏi: theo từ khoá trend có kéo được người từ web vào app không?

**Có, nhưng chỉ với 3 loại trend — loại "bùng 1 tuần" thì gần như không.**

- **Bài SEO cần 2–8 tuần** mới được index và lên trang 1 (`chưa đo` cho shotmatic.app — đo ở đợt 4 của [46.2](phase-46-2-seo-keyword-blog-gsc.md)).
  Trend bùng rồi tắt trong 1–2 tuần thì bài lên hạng lúc không ai còn tìm.
- **Người vào app khi trang giải đúng việc họ gõ.** Trend tin tức (người nổi tiếng, sự kiện) cho lượt xem, không cho lượt tải.
  Trend dạng *việc cần làm* ("how to…", "… app", "… tool") mới đi được tới nút tải.
- **Danh sách Rising của Trends có rác:** đo hôm nay, *app ideas* có rising "8 tech ideas that made the web move quicker",
  "sam's club mobile app embraces the future in 2025"; *micro saas* có rising "walmart near me". Phải soát chéo bằng Autocomplete + SERP.

**4 loại trend:**

1. **Mùa vụ lặp lại → đưa vào app: tốt nhất.** Nhận biết: đỉnh cùng tuần mỗi năm (xem 5 năm).
   Làm: đăng trước đỉnh 6–8 tuần, sửa lại mỗi năm — biết trước nên kịp index.
2. **Đang lên đều → tốt.** Nhận biết: 12 tháng tăng, không gãy.
   Làm: bài trụ + trang đích, viết ngay — lượng tìm còn tăng khi bài lên hạng.
3. **Bùng đột ngột (breakout) → có thể.** Nhận biết: rising "Breakout" trong 7 ngày.
   Làm: chỉ khi đã có app / tính năng giải đúng việc đó; đăng social + sửa trang có sẵn, không chờ SEO.
4. **Tin tức / người nổi tiếng → không.** Nhận biết: đỉnh nhọn 1–3 ngày. Làm: bỏ qua.

Luật đi từ web vào app: **1 trang = 1 việc người ta gõ = 1 app/tính năng giải việc đó = 1 nút tải**, đo bằng GA4
(`store_click` / `download` / `generate_lead`). Không có app khớp việc → không làm trang, dù trend to.

## Mục tiêu

- **Chuyên mục `trends` (tên hiện "Google Trends")** với 1 bài trụ + 4 bài cụm, mỗi bài dẫn về đúng 1 trang đích.
- **Kịp mùa:** *how to use google trends* có đỉnh tuần 2025-11-30 và 2026-02-01 → bài trụ live **trước 2026-11-20**.
- **Có bằng chứng tự đo:** mỗi bài kèm 1 lần tra thật bằng ShotMatic (Trends + store) có ngày, không ảnh giả.

**Xong khi:** `/blog/category/trends` mở được, ≥ 4 bài live đúng khuôn [46.1](phase-46-1-landing-blog.md), đã gửi Search Console;
4 loại trend ở trên có mặt trong bài trụ; số click / impressions đo lại sau 4 tuần (chưa có thì `chưa đo`).

## Số đo (Google Trends US 12 tháng + Autocomplete US, 2026-10-31)

Số tương đối 0–100 trong 1 nhóm so sánh. Có đứt gãy chung tuần 2026-07-12 ở mọi từ (xem [46.3](phase-46-3-blog-founders.md)) — chỉ so trong cùng một phía mốc đó.

| Từ khoá | Đỉnh 12 tháng | Ghi chú |
|---|---|---|
| trending products | 100 (2026-01-18) | dân bán hàng (Etsy, Shopify) — chỉ dùng làm ví dụ |
| trend marketing | 74 | Autocomplete toàn tên công ty (*Trend Marketing wholesale*) → **không viết** |
| google trends api | 48 | người muốn tự động hoá — đúng chỗ ShotMatic kéo Trends sẵn |
| how to use google trends | 26 | đỉnh cuối tháng 11 và đầu tháng 2 |
| google trends for seo | 8 | nhỏ, nhưng đúng ý định |

Autocomplete *how to use google trends …*: *to find products to sell* · *for market research* · *to find a niche* ·
*for keyword research* · *for product research*. *google trends for …*: *business ideas* · *digital products* · *products*.
Related của *google trends*: *google trends data*, *google trends api*, *google trends analysis* (rising +90 → +250).

## Bài (thứ tự = thứ tự viết)

1. [x] **Bài trụ · How to use Google Trends to find a niche (for apps and digital products)** — `how to use google trends to find a niche` → trang chủ.
   Đọc 0–100, top vs rising, 5 năm để thấy mùa vụ, so 5 từ cùng lúc, bảng 4 loại trend + rác ở Rising. Live trước 2026-11-20.
   **Live 2026-10-31** (commit `7c80a10`, `/blog/google-trends-find-a-niche`): `content/blog/google-trends-find-a-niche.md` (~2.300 từ) + chuyên mục `trends` ở `lib/blog-meta.mjs`;
   số đo: 5 niche app (habit tracker, budget app, plant identifier, pomodoro timer, meal planner) 5 năm US, related queries
   của *budget app*, đứt gãy tuần 2026-07-12. SERP top đều nói dropshipping / affiliate — chưa bài nào cho app.
2. [ ] **How to use Google Trends for keyword research (and what it cannot tell you)** — `how to use google trends for keyword research` → `/app-store-keyword-research`.
   Trends không cho volume; ghép với Autocomplete + top 10 store. Ví dụ pomodoro timer có sẵn ở bài cũ.
3. [ ] **Google Trends for business ideas: seasonal, rising or a spike?** — `google trends for business ideas` → trang chủ.
   Lấy 10 ý tưởng, xếp vào 4 loại, cái nào đáng build app. Đây là bài trả lời "trend → app" ở trên.
4. [ ] **How to use Google Trends for market research** — `how to use google trends for market research` → `/app-competitor-analysis`.
   Theo vùng (US vs khác), related topics, ghép với review 1–2★ của đối thủ.
5. [ ] **Google Trends API in 2026: options, limits, and a no-code way** — `google trends api` → `/blog/niche-radar-feature-tour`.
   Chỉ ghi giới hạn có nguồn chính thức; giới hạn chưa công bố thì `not measured`. Nói đúng: ShotMatic kéo Trends trong 1 lần tra, không nói hơn.

**Bài nỗi đau thêm (ngoài danh sách, từ skill `/shotmatic-blog`):**

- [x] **Is Google Trends accurate? 6 ways it misleads app makers** — `is google trends accurate` (Autocomplete: *google trends not accurate*, *not enough data*) —
  live 2026-10-31 `/blog/is-google-trends-accurate`, commit `62f7263`. Số đo: cùng 1 từ ra 18 và 39 ở 2 biểu đồ, cụm Autocomplete có mà Trends = 0, *gift tracker* bùng 9 → 100 tháng 4/2026.
- [x] **App ideas no one has done? We checked 8 in the App Store** (mục `niche`) — live cùng commit. 8 ý tưởng, top 10 App Store US + Trends 5 năm.
- [x] Đợt 2 (mục `niche`, commit `1adda08`, live 2026-10-31): **Is the app market saturated?** (12 nhóm app: 4/120 app yếu trong top 10) ·
  **Is ASO worth it?** (`/blog/does-aso-work`: #1 có đúng cụm trong tên 9/12, #1 không phải app nhiều rating nhất 9/12) ·
  **How to find a low competition app niche** (8 cặp rộng → hẹp, 6 cặp mở ra).
- [x] Đợt 3 (commit `2d2a0c5`, live 2026-10-31): **App Store keyword search volume** (mục `niche`: Trends so với tổng rating top 10 trên 10 từ, tương quan hạng 0,50) ·
  **Building something nobody wants?** (mục `founders` mới: Show HN 12 tháng, ~13.900 bài "app", 62,5% ≤ 2 điểm, 1,7% ≥ 100 điểm) ·
  **App Store ranking by country** (mục `niche`: 4 từ × 7 nước, Mỹ 0–1 app yếu, nước khác tới 7).

## Đợt thử · trend → web → app (sau khi bài 1–3 live)

- [ ] Mỗi thứ Hai quét Trends cho 5 từ gốc của ShotMatic, xếp vào 4 loại, ghi vào `marketing/trend-log.md` (repo App-AI-Skills)
- [ ] Chọn **1** trend mùa vụ hoặc đang lên có trang đích khớp → sửa / thêm 1 đoạn + FAQ vào bài sẵn có, không viết bài mỏng mới
- [ ] Đo 4 tuần: impressions + click (Search Console), `generate_lead` / `download` từ trang đó (GA4) — kết luận giữ hay bỏ cách này

<div class="box box--rules" markdown>
**Luật**

- Không bịa volume — Trends chỉ là số tương đối; ghi rõ nhóm so sánh và ngày đo
- Mỗi từ "rising" phải qua Autocomplete + SERP mới được viết
- Tiếng Anh, khuôn `content/blog/<slug>.md` của 46.1; CTA Download (để lại email)
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Bài chạy theo tin nóng / người nổi tiếng; bài *trend marketing* chung chung (từ khoá là tên công ty)
- Trang tự sinh hàng loạt theo trend (programmatic) — để sau khi có số Search Console
- Tính năng mới trong app để bắt trend (vd. cảnh báo "breakout") — nếu cần thì mở phase riêng ở `docs/web/`
</div>

[Tổng quan Version 11](version-11.md) · Code ở repo `nvminhtu/shotmatic` · Skill: `/oneclicktool-blog` (khuôn bài), `marketing-skills:content-strategy`, `marketing-skills:seo-audit`
