# Phase 46.2 · shotmatic.app — Từ khoá + blog theo cụm + Search Console

> Một phase gộp 3 việc cho **chính ShotMatic**: (1) tối ưu từ khoá cho site shotmatic.app, (2) viết blog kéo người
> tìm đúng các từ khoá đó, (3) dựng Search Console làm bảng đo của marketing. Đích: người gõ "app idea validation",
> "App Store keyword research", "app competitor analysis" trên Google / AI search gặp ShotMatic → Download (để lại
> email) → mua PRO.

<span class="chip chip--doing">Đang làm · Đợt 1 + 2 live 2026-10-31 (còn Cloudflare) · Đợt 3 bài 1–5 live (bài 6 chờ thử đối thủ) · Đợt 0 chờ khoá Search Console</span>

Bản review SEO + bản đồ từ khoá đầy đủ (đo 2026-10-31): `apps/ACTIVE/web-apps/niche-radar/marketing/2026-10-31-seo-keyword-plan.md`
ở repo App-AI-Skills. Phase này là bản làm việc của file đó.

## Mục tiêu

- **Site nói đúng từ khoá người mua gõ.** Trang chủ trụ `app idea validation`, phụ `app store keyword research`,
  `app competitor analysis` — thay chữ "niche" ít người gõ.
- **Blog lệch về người đang chọn app để làm**, không phải dân marketing. Mỗi bài 1 từ khoá đã đo, dẫn về 1 trang đích.
- **Có số đo có nguồn:** mốc Search Console (impressions, click, query, trang đã index) trước khi sửa, đo lại sau 4 tuần.

**Xong khi:** đợt 1–3 live trên shotmatic.app · sitemap gửi Search Console, mọi trang đích + bài mới đã index ·
bảng số mốc + bảng số tuần 4 đủ cột · GEO 5 câu hỏi đo 2 lần (trước / sau). Chưa đo được thì ghi `chưa đo`.

## Bản đồ từ khoá (Autocomplete US + Trends US, 2026-10-31)

Volume tuyệt đối **chưa đo** (không có tool volume); đa số cụm dưới ngưỡng Trends → từ khoá đuôi dài, ít người gõ nhưng đúng người mua.

1. **Kiểm ý tưởng app** — app idea validation · mobile app idea validation · validate your app idea → **trang chủ** + bài trụ
2. **Research keyword store** — app store keyword research tool (free) · play store keyword research · aso keyword research tools free → trang `/app-store-keyword-research`
3. **Đối thủ + review** — app competitor analysis tool · app store review analysis · play store app review analysis → trang `/app-competitor-analysis`
4. **Tìm ý tưởng** — how to find (profitable) app ideas · app ideas that make money · indie dev app ideas → blog
5. **AI builder** — vibe coding app ideas · saas idea validation prompt → `/ai` + blog
6. **So sánh** — astro aso · "alternative" các tool ASO → trang so sánh (chỉ khi đã thử đối thủ thật)

## Đợt 0 · Search Console + số mốc (trước khi sửa gì)

- [ ] **(Anh)** đặt lại khoá service account vào `~/.config/gcp/oneclicktool-sa.json` (MCP `search-console` đang báo thiếu file, 2026-10-31) và thêm email service account vào property shotmatic.app (quyền Đọc là đủ)
- [ ] Claude kiểm property: `sc-domain:shotmatic.app` hay `https://shotmatic.app/` — ghi lại tên đúng
- [ ] Ghi **bảng mốc 28 ngày**: impressions · click · CTR · vị trí TB · top 20 query · top trang · số trang đã index / bị loại và lý do
- [ ] Soát sitemap đã gửi chưa, lỗi gì; gửi `https://shotmatic.app/sitemap.xml` nếu chưa có
- [ ] Đo GEO mốc: hỏi ChatGPT / Perplexity / Gemini 5 câu thuộc cụm 1–3, ghi ShotMatic có được nhắc không (`/app-geo`)

Bảng số lưu ở `marketing/seo-gsc.md` (repo App-AI-Skills), mỗi lần đo 1 khối có ngày.

## Đợt 1 · Tối ưu từ khoá + sửa nền (repo `nvminhtu/shotmatic`)

Code live 2026-10-31 (commit `80419f0`), soát bằng curl trên shotmatic.app cùng ngày.


- [x] Trang chủ: title `App Idea Validation & App Store Keyword Research | ShotMatic` (≤ 60 ký tự), description có 2 từ khoá phụ, H1 có cụm "validate your app idea", 1 H2 có "competitor analysis"
- [x] `llms.txt` + `llms-full.txt`: đúng 1.0 live, Free 15 lượt tra, PRO $39.99, link /download (đang ghi "waitlist", "14-day trial")
- [x] `/privacy` bỏ chữ demo / waitlist, ghi đúng hộp email khi tải
- [x] `pages/_document.jsx` với `<Html lang="en">`
- [x] JSON-LD `SoftwareApplication`: 2 offer (Free 0 · PRO 39.99), `softwareVersion`, `downloadUrl`, `featureList`; `/scorecard` thêm schema
- [x] Sitemap: thêm /privacy, trang chuyên mục `noindex` + bỏ khỏi sitemap, `lastmod` trang chủ · giữ /blog/page/2 (trang phân trang có bài thật, canonical riêng)
- [x] `og:image` cho /terms /privacy · logo AI giữ `alt=""` vì tên AI đã in chữ ngay cạnh (đọc màn hình khỏi đọc 2 lần)
- [ ] **(Anh)** Cloudflare: tắt "Managed robots.txt", cho PerplexityBot (đang 403), `www` → 308 — 2026-10-31 vẫn còn cả 3

## Đợt 2 · 2 trang đích theo từ khoá

Mỗi trang 800–1.200 từ, ảnh app thật (host ở `app-demo`), FAQ 3 câu, CTA Download, link qua lại trang chủ + /scorecard + bài blog.

- [x] `/app-store-keyword-research` — "App Store & Google Play keyword research on your Mac" (cụm 2)
- [x] `/app-competitor-analysis` — đối thủ 2 store + đọc review 1–2★ (cụm 3)

## Đợt 3 · Blog theo cụm từ khoá

Mỗi bài: 1 từ khoá đã đo (Autocomplete + Trends + xem SERP), mở bằng "The short answer" 40–60 từ, H2 là câu hỏi người ta
gõ, số tự đo có ngày, `sources` ≥ 2, dẫn về đúng 1 trang đích. Tiếng Anh, khuôn `content/blog/<slug>.md` của [Phase 46.1](phase-46-1-landing-blog.md).
Thứ tự = thứ tự viết.

1. [x] How to validate an app idea before you build → trang chủ (cụm 1, bài trụ) — live, commit `3c31881` (2026-10-31)
2. [x] Free App Store keyword research: what you can measure without paid tools → `/app-store-keyword-research` (cụm 2) — live `/blog/app-store-keyword-research-free`, commit `85011bf` (ví dụ pomodoro timer, 2026-10-31)
3. [x] How to analyze competitor app reviews (App Store + Google Play) → `/app-competitor-analysis` (cụm 3) — live `/blog/analyze-app-store-google-play-reviews`, commit `f646d4e` (1.500 review 3 app meal planner)
4. [x] How to find app ideas that make money: read the 1–2★ reviews → trang chủ (cụm 4) — live `/blog/app-ideas-that-make-money`, commit `f646d4e` (8 ngách đo App Store)
5. [x] Vibe coding app ideas: check the niche before Claude Code writes it → `/ai` (cụm 5) — live `/blog/vibe-coding-app-ideas`, commit `f646d4e` (8 ý tưởng vs 8 bản hẹp)
6. [ ] ShotMatic vs Astro / AppFigures for an indie maker → trang chủ (cụm 6 — chỉ viết khi đã thử thật đối thủ)

Xong mỗi bài: build xanh, xem 1340 + 375, push main, **gửi URL lên Search Console** (Request indexing qua tay anh, hoặc sitemap tự lấy).

## Đợt 4 · Đo lại (4 tuần sau đợt 1)

- [ ] Search Console 28 ngày: so với mốc đợt 0 (impressions, click, query mới thuộc 6 cụm, trang đã index)
- [ ] Query có impressions nhưng CTR thấp → sửa title / description trang đó; query mới xuất hiện → ghi vào bản đồ từ khoá
- [ ] GEO 5 câu hỏi đo lại, so với mốc
- [ ] Ghi kết luận: cụm nào lên, cụm nào không — viết tiếp hay dừng cụm đó

<div class="box box--rules" markdown>
**Luật**

- Không bịa volume / số click: chỉ số đo có nguồn + ngày, không có thì `chưa đo`
- Site 100 % tiếng Anh; ảnh là màn hình app thật, không ảnh giả giao diện
- Bài nói đúng tính năng đang có — không nói ShotMatic đo được GEO (Phase 59–62 chưa làm)
- Claude không đăng nhập Cloudflare / Google; việc ghi **(Anh)** là của anh
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Đổi giá / terms / `BUY_URL` (chờ chính sách bán mới)
- Làm lại thiết kế landing, mua tool SEO trả phí, chạy quảng cáo
- Viết thêm bài SEO / AEO / GEO chung (đúng chỗ hơn ở Promo Desk); viết hàng loạt bài mỏng
- Đổi slug `/blog/niche-radar-feature-tour` khi chưa có redirect
</div>

[Tổng quan Version 11](version-11.md) · Code ở repo `nvminhtu/shotmatic` · Skill: `/oneclicktool-blog` (khuôn bài), `/app-geo` (đo AI search), `marketing-skills:seo-audit`
