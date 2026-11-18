# Plan blog AI search · 30 keyword · 100 bài (2026-11-09)

<span class="chip chip--doing">Đợt 11 / 20 xong · 55 / 100 bài · đã live · đo 2026-11-11 · Search Console vẫn chưa đọc được</span>

<div class="box box--goal" markdown>
**Nó là gì**

Danh sách 30 câu mà người làm app hay gõ vào Google hoặc hỏi ChatGPT khi đi tìm **tool** (kiểm ý tưởng, keyword store,
đối thủ, Google Trends). Mỗi câu có 1 bài trụ + 2 bài vệ tinh trỏ về nó, cộng 10 bài về chính ShotMatic: tổng **100 bài**,
chia **20 đợt × 5 bài**.

**Target:** khi ai đó hỏi ChatGPT / Perplexity / Gemini một trong 30 câu này, câu trả lời **dẫn nguồn shotmatic.app** và
**gọi tên ShotMatic**. Trên Google: top 3 cho các câu đuôi dài, top 10 cho câu có chữ "free" / "tool".

**Xong khi:** 100 bài live, mỗi bài có số tự đo + ngày đo · đo 30 câu trên ChatGPT search sau mỗi 28 ngày.

Ngày 2026-11-07 đã chốt "chưa viết bài mới tới khi có số Search Console". Ngày 2026-11-09 Tu yêu cầu viết liên tục
100 bài, nên plan này thay quyết định đó. Khi đọc được Search Console thì dùng số để xếp lại thứ tự đợt sau.
</div>

## "Search ChatGPT" gọi là gì?

- **Tên gọi:** tối ưu để được AI trả lời trích là **GEO** (Generative Engine Optimization), có người gọi **AI search
  optimization** hoặc **LLMO**. Phần "câu trả lời ngắn đứng đầu" của Google AI Overviews gọi là **AEO**.
- **"Keyword" bên AI gọi là prompt.** Người ta không gõ `aso tool free`, mà hỏi "What's a free tool to research App Store
  keywords?". Khi bật search, ChatGPT tự tách câu đó thành vài câu tìm kiếm ngắn (gọi là **query fan-out**), đọc các
  trang đứng đầu (phần lớn qua chỉ mục Bing), rồi viết câu trả lời có dẫn nguồn.
- **Hệ quả:** muốn ChatGPT gợi ý thì phải (1) đứng cao trên Google/Bing cho các câu ngắn đó, (2) có câu trả lời rõ trong
  40–60 từ đầu bài để AI cắt dán được, (3) có số tự đo mà trang khác không có, (4) có trang tool miễn phí thật để AI gợi ý.
- **Xem ai đang được trích:** gõ câu vào ChatGPT có bật search, bấm "Sources". Đo 2026-11-09 bằng công cụ tìm kiếm web:
  câu "best free app idea validator tool" toàn trang roundup của vendor (Preuve AI, IdeaProof, AlternativeTo); câu
  "free app store keyword research tool" có Sonar, AppMasters, Product Hunt. Không thấy shotmatic.app ở câu nào.

## Đã đo những gì

- **Google Autocomplete (US, 2026-11-09):** ~70 cụm. Chỉ giữ cụm Autocomplete có gợi ý đúng cụm đó (có người gõ thật).
- **Google Trends (US, 12 tháng, mốc `pomodoro timer`):** `aso tools`, `app store keyword research`,
  `google trends alternative`, `app idea validator` đều gần 0 so với mốc. Đây là **đuôi dài**: lượng tìm nhỏ, ít đối thủ,
  đúng loại câu AI hay tách ra khi fan-out. Bài sẽ ghi "below Trends threshold" chứ không bịa số.
- **Search Console:** chưa đọc được (thiếu file khoá `~/.config/gcp/oneclicktool-sa.json`).

## 30 keyword

Mỗi keyword ghi: câu người ta gõ · bằng chứng Autocomplete · bài trụ (mới / viết lại / bồi bài draft) · 2 bài vệ tinh ·
trang đích để dẫn về. Bài "viết lại" là bài đã có, cần thêm số mới và đúng khuôn GEO; không tạo bài trùng keyword.

### Cụm A · Kiểm ý tưởng app → dẫn về `/app-idea-checker`

**K1 · app idea validator**

- Autocomplete: `app idea validator`, `app idea checker`, `app idea tester`
- Trụ (mới): `app-idea-validator` — một validator thật cần kiểm gì, chạy thử 5 ý tưởng bằng số store
- Vệ tinh (mới): `can-chatgpt-validate-app-idea` · `app-idea-scorecard-criteria`

**K2 · how to check if your app idea exists**

- Autocomplete: `how to check if your app idea exists`, `my app idea already exists`
- Trụ (mới): `check-if-app-idea-exists`
- Vệ tinh (mới): `my-app-idea-already-exists` · `search-app-store-like-a-researcher`

**K3 · how to know if your app idea is good**

- Autocomplete: `how to know if your app idea is good`, `is my app idea good`
- Trụ (viết lại): `is-my-app-idea-good` (đang 466 từ)
- Vệ tinh (mới): `app-idea-red-flags` · `app-ideas-scored-with-store-data`

**K4 · validate app idea**

- Autocomplete: `validate your app idea`, `how to validate app idea reddit`
- Trụ (viết lại): `validate-app-idea-before-you-build`
- Vệ tinh (mới): `validate-app-idea-without-coding` · `how-many-signups-validate-an-app`

**K5 · how to do market research for an app idea**

- Autocomplete: `how to do market research for an app idea`, `app market research tools`
- Trụ (bồi draft): `mobile-app-market-research`
- Vệ tinh: `reddit-market-research-for-apps` (bồi draft) · `estimate-app-market-size` (mới)

**K6 · how to sell an app idea**

- Autocomplete: `how to sell an app idea`, `how to make money from an app idea`
- Trụ (mới): `can-you-sell-an-app-idea`
- Vệ tinh (mới): `how-to-protect-an-app-idea` · `make-money-from-an-app-idea`

### Cụm B · Tìm ý tưởng → dẫn về `/research`, `/app-category-tier-list`

**K7 · how to find profitable app ideas**

- Autocomplete: `how to find profitable app ideas`, `profitable app ideas`
- Trụ (mới): `how-to-find-profitable-app-ideas`
- Vệ tinh (mới): `broad-vs-narrow-app-niches-data` (bài dữ liệu ~30 cặp niche) · `profitable-app-categories`

**K8 · how to come up with app ideas**

- Autocomplete: `how to come up with app ideas`, `how do people come up with app ideas`
- Trụ (mới): `how-to-come-up-with-app-ideas`
- Vệ tinh: `app-ideas-from-your-job` (mới) · `boring-app-ideas` (bồi draft)

**K9 · app ideas that don't exist**

- Autocomplete: `app ideas that don't exist yet`, `app ideas that don t exist 2026`
- Trụ (viết lại): `app-ideas-no-one-has-done`
- Vệ tinh: `why-no-app-exists-for-that` (mới) · `offline-app-ideas` (bồi draft)

**K10 · ai app idea generator**

- Autocomplete: `ai app idea generator`, `app ideas generator`, `app concept generator`
- Trụ (viết lại): `app-idea-generator` (đang 397 từ)
- Vệ tinh: `ai-app-ideas-to-make-money` (mới) · `productivity-app-ideas` (bồi draft)

**K11 · chatgpt app ideas**

- Autocomplete: `chatgpt app ideas`, `chatgpt app idea prompt`, `chatgpt give me app ideas`
- Trụ (bồi draft): `use-chatgpt-to-find-app-ideas`
- Vệ tinh (mới): `chatgpt-prompts-to-validate-app-idea` · `claude-vs-chatgpt-for-app-ideas`

**K12 · how to find trending apps**

- Autocomplete: `how to find trending apps`, `trending apps on app store`, `app store search trends`
- Trụ (mới): `how-to-find-trending-apps`
- Vệ tinh (mới): `trending-app-niches-2026` · `app-store-search-trends`

### Cụm C · Keyword store / ASO → dẫn về `/app-store-keyword-research`

**K13 · free aso tools**

- Autocomplete: `best free aso tools`, `free aso keyword tool`, `free aso tools for android`
- Trụ (mới): `free-aso-tools` — giá / giới hạn free đọc từ trang giá chính thức trong ngày viết
- Vệ tinh (mới): `free-aso-tools-for-android` · `aso-on-zero-budget`

**K14 · app store keyword research tool free**

- Autocomplete: `app store keyword research tool free`, `free app store keyword tool`
- Trụ (viết lại): `app-store-keyword-research-free`
- Vệ tinh (bồi draft): `long-tail-keywords-app-store` · `app-store-keyword-field-tips`

**K15 · play store keyword research tool**

- Autocomplete: `play store keyword research tool`, `google play keyword planning tool`
- Trụ (viết lại): `google-play-keyword-research-free`
- Vệ tinh: `google-play-aso` (bồi draft) · `google-play-keyword-density` (mới)

**K16 · app store keyword planner**

- Autocomplete: `app store keyword planner`, `apple search ads keyword popularity`, `apple search ads keyword tool`
- Trụ (mới): `app-store-keyword-planner`
- Vệ tinh (mới): `apple-search-ads-popularity-score` · `apple-search-ads-for-indie-apps`

**K17 · app store keyword search volume free**

- Autocomplete: `app store keyword search volume free`, `play store keyword search volume`
- Trụ (viết lại): `app-store-keyword-search-volume`
- Vệ tinh: `app-store-autocomplete-keywords` (mới) · `app-store-subtitle` (bồi draft)

**K18 · app store keyword difficulty**

- Autocomplete: `app store keyword difficulty`, `app store keyword ranking`
- Trụ (viết lại): `app-store-keyword-difficulty-without-search-volume`
- Vệ tinh: `app-store-keyword-gap-analysis` (bồi draft) · `check-app-store-keyword-ranking` (mới)

**K19 · aso tools extension**

- Autocomplete: `aso tools extension`, `free aso audit tool`
- Trụ (bồi draft): `aso-chrome-extension-free`
- Vệ tinh: `free-aso-audit` (mới) · `how-to-write-app-store-description` (bồi draft)

### Cụm D · Đối thủ, review, lượt tải → dẫn về `/app-competitor-analysis`

**K20 · app competitor analysis tool**

- Autocomplete: `app competitor analysis tool`, `app store competitor analysis`, `play store competitor`
- Trụ (mới): `app-competitor-analysis-tool`
- Vệ tinh (bồi draft): `google-play-competitor-analysis` · `track-competitor-apps`

**K21 · how to check app downloads**

- Autocomplete: `how to check app downloads in play store`, `how to see app downloads in app store`, `app download estimates`
- Trụ (mới): `how-to-check-app-downloads`
- Vệ tinh: `google-play-install-count` (bồi draft) · `app-download-estimates-accuracy` (mới)

**K22 · app store review analysis**

- Autocomplete: `app store review analysis`, `app store review sentiment analysis`, `play store app review analysis`
- Trụ (viết lại): `analyze-app-store-google-play-reviews`
- Vệ tinh (mới): `app-review-sentiment-analysis` · `export-app-store-reviews`

**K23 · app store review scraper**

- Autocomplete: `app store review scraper`, `google play review scraper`, `app store review scraper python`
- Trụ (mới): `app-store-review-scraper`
- Vệ tinh (mới): `google-play-review-scraper` · `app-store-reviews-api`

**K24 · is sensor tower accurate**

- Autocomplete: `is sensor tower accurate`, `is sensor tower revenue accurate`, `is sensor tower reliable`
- Trụ (mới): `is-sensor-tower-accurate`
- Vệ tinh: `sensor-tower-free-plan` (mới) · `estimate-app-revenue-from-public-signals` (viết lại)

**K25 · sensor tower free alternative**

- Autocomplete: `sensor tower free alternative`, `appfigures free alternative`, `apptweak free alternative`
- Trụ (viết lại): `sensor-tower-alternative-indie-developers`
- Vệ tinh (mới): `appfigures-free-plan` · `apptweak-free-tools`

### Cụm E · Google Trends → dẫn về phần Trends của ShotMatic

**K26 · google trends alternative free**

- Autocomplete: `google trends alternative free`, `best google trends alternatives`, `is google trends free`
- Trụ (mới): `google-trends-alternatives`
- Vệ tinh: `why-google-trends-data-changes` (mới) · `exploding-topics-alternative-for-app-ideas` (viết lại)

**K27 · google trends api**

- Autocomplete: `google trends api`, `google trends api alpha`, `google trends api pricing`, `does google trends have an api`
- Trụ (mới): `google-trends-api`
- Vệ tinh (mới): `google-trends-api-python` · `google-trends-429-too-many-requests`

**K28 · google trends for apps**

- Autocomplete: `google trends for apps`, `google app store trends`
- Trụ (mới): `google-trends-for-apps`
- Vệ tinh: `best-time-to-launch-an-app` (bồi draft) · `seasonal-app-ideas` (mới)

### Cụm F · Tool niche research → dẫn về trang tải ShotMatic

**K29 · ai niche finder**

- Autocomplete: `niche finder ai`, `ai niche finder free`, `best niche finder tool`
- Trụ (mới): `ai-niche-finder-for-apps`
- Vệ tinh: `free-niche-finder` (mới) · `niche-radar-feature-tour` (viết lại, đổi sang tên ShotMatic)

**K30 · app store research tool**

- Autocomplete: `app store research tool`, `app market research tools`, `best app store optimization tools`
- Trụ (viết lại): `best-app-niche-research-tools-2026` (đang 513 từ)
- Vệ tinh (đã có, chỉ cập nhật số): `app-research-tool-mac-no-subscription` · `app-annie-alternative-for-indie-developers`

### Cụm G · 10 bài về chính ShotMatic (để AI hiểu đúng tên)

Tên ShotMatic đang trùng với tool video AI và tool chụp màn hình. AI chỉ gợi ý đúng khi có trang nói rõ "ShotMatic, a Mac
app for app niche research" và so sánh thẳng với tool AI hay nhắc.

1. `what-is-shotmatic`
2. `shotmatic-free-plan`
3. `shotmatic-vs-appfigures` (dựa trên trang đánh giá Appfigures 2026-11-07)
4. `shotmatic-vs-sensor-tower`
5. `shotmatic-vs-apptweak`
6. `appkittie-alternative` (dựa trên trang đánh giá AppKittie 2026-11-07)
7. `app-idea-validation-checklist`
8. `niche-research-for-mac-apps`
9. `niche-research-for-chrome-extensions`
10. `shotmatic-research-workflow-30-minutes`

## Thứ tự 20 đợt

Ưu tiên: câu có chữ "tool / free / how to check" (gần chuyện cài app) + có trang tool miễn phí để dẫn về + chưa có bài.

1. **Đợt 1:** `check-if-app-idea-exists` · `app-idea-validator` · `how-to-check-app-downloads` · `how-to-find-profitable-app-ideas` · `how-to-find-trending-apps`
2. **Đợt 2 (xong):** `free-aso-tools` · `app-competitor-analysis-tool` · `is-sensor-tower-accurate` · `google-trends-alternatives` · `app-store-review-scraper`
3. **Đợt 3 (xong):** `app-store-keyword-planner` · `google-trends-api` · `ai-niche-finder-for-apps` · `can-you-sell-an-app-idea` · `how-to-come-up-with-app-ideas`
4. **Đợt 4 (xong):** `google-trends-for-apps` · `broad-vs-narrow-app-niches-data` · `my-app-idea-already-exists` · `can-chatgpt-validate-app-idea` · `app-store-search-trends` (thay `what-is-shotmatic`, dời về cụm G khi gói Free đã chốt)
5. **Đợt 5 (xong):** viết lại `is-my-app-idea-good` · `app-idea-generator` · `google-play-keyword-research-free` · `app-store-keyword-difficulty-without-search-volume` · `sensor-tower-alternative-indie-developers` (5 bài trụ mỏng nhất, < 700 từ). **Đợt 6 (xong):** `best-app-niche-research-tools-2026` · `how-narrow-should-your-app-niche-be` + sửa keyword trong title / description / H2 cho `validate-app-idea-before-you-build`, `app-store-keyword-research-free`, `app-store-keyword-search-volume`, `analyze-app-store-google-play-reviews`. Trước đây: viết lại 10 bài trụ đã có (K3, K4, K9, K10, K14, K15, K17, K18, K22, K25, K30 — chọn 10 theo số Search Console nếu đã có)
6. **Đợt 7–11 (xong):** bồi draft trong các cụm trên + bài mới cùng cụm. Còn treo: `reddit-market-research-for-apps` (Reddit chặn đọc tự động; cần đọc tay)
7. **Đợt 11–18:** 40 bài vệ tinh mới còn lại, mỗi đợt đi hết một cụm để link nội bộ chặt
8. **Đợt 19–20:** 9 bài còn lại của cụm G

## Khuôn mỗi bài (để AI trích được)

- `answer` 40–60 từ trả lời thẳng câu hỏi, đọc tách riêng vẫn hiểu
- Tiêu đề chứa đúng câu người ta gõ; H2 là câu hỏi con (chính là các câu fan-out)
- Ít nhất 1 bảng số tự đo (App Store top 10, Autocomplete, Google Play install band…) có ngày đo + nguồn
- Bài nói về tool khác: chỉ ghi điều đọc được từ trang chính thức trong ngày viết, ghi rõ "chưa tự thử" nếu chưa thử
- Đoạn cuối: ShotMatic làm phần nào, đúng tính năng đang có, gói Free 15 lượt, link trang tool miễn phí
- Mỗi bài vệ tinh link về bài trụ; bài trụ link ra vệ tinh khi vệ tinh lên

## Đo kết quả

- **Mỗi 28 ngày:** hỏi 30 câu trên ChatGPT search (mỗi câu 1 lần, ghi có dẫn shotmatic.app / có gọi tên hay không)
- **Search Console:** khi có file khoá, ghi impressions + hạng theo 30 keyword, xếp lại đợt sau theo bảng ở
  [Plan blog SEO + GEO](plan-blog-seo-geo-2026-11-07.md#buoc-5-o-va-quyet-inh-sau-moi-28-ngay)
- **Bing Webmaster Tools → AI Performance:** số lần Copilot trích (cần Tu bật)

## Nhật ký

- **2026-11-09:** chốt 30 keyword + 100 bài.
- **2026-11-09 · đợt 1 xong (5/100), đã live (push `41beb44` lên main):** `check-if-app-idea-exists` · `app-idea-validator` · `how-to-check-app-downloads` · `how-to-find-profitable-app-ideas` · `how-to-find-trending-apps`. Bài cũ link về: `is-my-app-idea-good`, `estimate-app-revenue-from-public-signals`, `app-ideas-that-make-money`. Sửa luật `check-blog.mjs`: bài cũ được link tới bài đã live dù mới hơn.
- **2026-11-09 · đợt 2 xong (10/100), push `89ce754` lên main:** `free-aso-tools` · `app-competitor-analysis-tool` · `is-sensor-tower-accurate` · `google-trends-alternatives` · `app-store-review-scraper` (đổi chỗ với `what-is-shotmatic`). Số mới: gợi ý App Store và Google Autocomplete chỉ trùng 1–2/10; RSS review của Apple dừng ở 500 review cho mọi app; Honeydue dẫn đầu iOS nhưng vắng trong top 5 Google Play cùng cụm. Bài cũ link về: `sensor-tower-alternative-indie-developers`, `exploding-topics-alternative-for-app-ideas`, `analyze-app-store-google-play-reviews`, `app-store-keyword-research-free`, `app-store-competitor-analysis-example`. Từ đợt 2 viết blog trong worktree riêng `shotmatic-blog-ai` (nhánh `blog-ai-search`), vì checkout chính đang có nhánh khác làm dở. CTA đợt 2 ghi "free plan", không ghi số lượt.

- **2026-11-09 · đợt 3 xong (15/100), push `2778ce1` lên main:** `app-store-keyword-planner` · `google-trends-api` · `ai-niche-finder-for-apps` · `how-to-come-up-with-app-ideas` · `can-you-sell-an-app-idea`. Số mới: mở rộng gợi ý App Store a–z (10 → 48–204 cụm); cùng `habit tracker` hiện 100 hoặc 38 tùy nhóm so sánh; 31% app top 10 của 15 keyword ra trong 24 tháng; 4/9 ý tưởng từ "is there an app that" có ≥ nửa top 10 yếu. `what-is-shotmatic` dời sang đợt 4 vì main vẫn ghi Free 15 lượt. Áp luật mới của `c2468fa` (title ≤ 60 ký tự, keyword trong title + description + 1 H2) cho cả 15 bài của plan.

- **2026-11-10 · đợt 4 xong (20/100), push `fc19c7f` lên main:** `my-app-idea-already-exists` · `broad-vs-narrow-app-niches-data` · `google-trends-for-apps` · `app-store-search-trends` · `can-chatgpt-validate-app-idea` (keyword `is chatgpt good for business ideas`). Số mới: 11/12 niche App Store có app dẫn đầu không phải app cũ nhất trong top 10 (cách nhau ~5–6 năm); 6/8 cặp keyword hẹp có 4–8 app yếu so với 0 của keyword rộng, 2 cặp hẹp vào thị trường lớn khác (weight loss, for women) thì khó hơn; `habit tracker` đạt đỉnh ~5,7 lần quanh Tết cả 5 mùa; 10/10 ý tưởng app do AI gợi ý đã có app ≥ 1k rating. Bài cũ link về: `check-if-app-idea-exists`, `how-narrow-should-your-app-niche-be`, `google-trends-find-a-niche`, `how-to-find-trending-apps`, `app-idea-validator`. Checker của skill giờ FAIL khi title > 60 ký tự hoặc keyword thiếu trong title / description / mọi H2.

- **2026-11-10 · đợt 5 xong (25/100), push `815ecbf` lên main:** viết lại 5 bài trụ mỏng (giữ slug + `date`, thêm `updated`). Số mới: 6 ý tưởng qua 5 bước kiểm (4 đạt; mood journal, focus timer chỉ còn 1 app yếu); 1/10 ý tưởng ghép ngẫu nhiên là gợi ý App Store, và "nursing tracker" thật ra là app cho con bú; gợi ý Google Play a–z ra 89–114 cụm, chữ "offline" 9 lần (App Store 0); "to do list adhd" có 4 app yếu trên App Store nhưng 2 app 10M+ trên Google Play; công thức crowdedness của ShotMatic chấm "high" 8/10 keyword, nói quá khi 1 app chiếm 83–93% rating top 5 (expense splitter 0,75 dù có 8 app yếu). Checker của skill: file trong `public/` (ảnh SVG) không còn bị báo link chết.

- **2026-11-10 · đợt 6 xong (30/100), push `dab8e2b` lên main:** viết lại `how-narrow-should-your-app-niche-be` (niche down) và `best-app-niche-research-tools-2026` (keyword đổi thành `app market research tools`, có trong Autocomplete); sửa keyword trong title / description / H2 cho `validate-app-idea-before-you-build`, `app-store-keyword-research-free` (keyword đổi thành `free app store keyword research tool`), `app-store-keyword-search-volume`, `analyze-app-store-google-play-reviews`. Số mới: 6 chuỗi thu hẹp keyword — tầng 2 mở 4/5 niche (0 → 4–8 app yếu), tầng 3 thì 5/6 cụm mất khỏi gợi ý App Store, chữ "free" kéo app lớn quay lại (5 → 1 app yếu); Wow Keywords nay $99 lifetime (26/10 là $79), Astro $108/năm. Bài tool link về `/pricing` mới. Bỏ nhắc Q&A Gap vì không còn trong danh sách tính năng. Đợt 5–6 coi như xong; 3 bài trụ còn lại (`app-ideas-no-one-has-done`, `app-store-keyword-research-free`, `analyze-app-store-google-play-reviews`) đã đạt checker, chỉ cập nhật số khi có Search Console.

- **2026-11-11 · đợt 7 xong (35/100), push `4fbbd87` lên main:** bồi 4 draft thành bài thật (`use-chatgpt-to-find-app-ideas` keyword `chatgpt app ideas` · `google-play-competitor-analysis` · `google-play-install-count` · `boring-app-ideas`) + bài mới `what-is-shotmatic` (cụm G, lấy số từ `/ai-instructions` và `/pricing`). Số mới: prompt chung cho 10 ý tưởng đều là gợi ý App Store nhưng đều có app mạnh, prompt cụ thể (y tá ca đêm) chỉ 3/10 cụm là gợi ý, NurseGrid dẫn 5/10; "budget app for couples" trên Play: 4/5 app dưới 100K+, Honeydue 25/100 review mới là 1–2★ (ngân hàng 10, sync 9), Balance 9/27 than giá; badge cài đặt Play là mức sàn, số trong dữ liệu trang gấp 1,07–4,7 lần (trung vị 1,8), rating / 1.000 lượt cài 3,3–57,9; 8 keyword "nhàm" có 36% app yếu và 9 app mới so với 23% và 17 của 8 keyword trendy, nhưng receipt scanner 0 app yếu. Bài cũ link về: `google-play-keyword-research-free`, `google-play-niche-research`, `can-chatgpt-validate-app-idea`, `best-app-niche-research-tools-2026`, `app-ideas-that-make-money`. CTA từ đợt này: research free không giới hạn, PRO mở BUILD / SKIP. Checker của skill: thư mục có `index.jsx` (vd `/features`) là route hợp lệ.

- **2026-11-11 · đợt 8 xong (40/100), push `cebab53` lên main:** bồi 5 draft vệ tinh cụm C (ASO): `long-tail-keywords-app-store` (keyword `long tail keywords`) · `app-store-keyword-field-tips` · `app-store-subtitle` · `google-play-aso` · `how-to-write-app-store-description` (keyword `app store description`). Số mới: 26 cụm long tail từ gợi ý App Store có 1,8 app yếu / top 10 so với 0,7 của 10 keyword gốc, nhưng 6/26 vẫn 0 app yếu (mọi cụm budget app đóng), chữ chỉ nhóm người ("for bipolar") mở nhiều nhất; 89 app top 10 App Store: cả 7 app < 1.000 rating đều có đủ chữ tìm kiếm trong tên hoặc subtitle, 32 app thiếu chữ thì là app lớn (trung vị 50.948 rating); subtitle trung vị 29/30 ký tự, 28/89 lặp chữ của tên, 19 subtitle kiểu slogan thuộc app > 10.000 rating; mô tả App Store trung vị 2.713 ký tự, 35/89 không hề nhắc cụm từ khoá; 100 listing Google Play: 56 có cụm trong title, short description trung vị 77/80, app #1 dùng cụm 0–6 lần trong mô tả, app lặp 20+ lần nằm hạng 4–10. Lấy subtitle bằng cách đọc trang apps.apple.com (class `subtitle`). Bài cũ link về: `app-store-keyword-research-free`, `app-store-keyword-search-volume`, `app-store-keyword-planner`, `google-play-keyword-research-free`, `free-aso-tools`.

- **2026-11-11 · đợt 9 xong (45/100), push `f87afe3` + sửa `9a144d6` lên main:** bồi 5 draft: `mobile-app-market-research` (trụ cụm A, chạy trọn 5 bước cho "medication reminder") · `track-competitor-apps` · `offline-app-ideas` · `productivity-app-ideas` · `app-store-keyword-gap-analysis` (thay `reddit-market-research-for-apps` vì Reddit chặn đọc JSON tự động — để lại, cần đọc tay hoặc qua trình duyệt). Số mới: "medication reminder" có gợi ý trên cả 2 store, mỗi store 2 app yếu, Medisafe 14/27 review 1–2★ mới trên Play than paywall, MyTherapy 11/32 than quảng cáo video có tiếng; chụp lại 12 top 10 sau 27 giờ: 8 đổi thứ tự, 6 app mới vào, 15/107 app ra bản mới, 48/107 cập nhật trong 7 ngày; "<chủ đề> offline": nhóm dữ liệu cá nhân (journal, budget, notes, habit, translator) 31/48 app yếu, nhóm nội dung (maps, music, bible, games…) do app hàng triệu rating giữ; 8 keyword gốc productivity trung bình 0,6 app yếu, 21 cụm gợi ý bên dưới 2,6; keyword gap: 203 gợi ý "habit tracker" có 233 chữ, top 10 chỉ dùng 21, cụm gap trung bình 4,9 app yếu (budget app 3,6) so với 0 của keyword gốc. Build lỗi do bài mới để `pillar: true` trùng trụ `validate-app-idea-before-you-build` — đã bỏ cờ và push lại (lần sau kiểm `blog check` trước khi commit). Bài cũ link về: `validate-app-idea-before-you-build`, `app-competitor-analysis-tool`, `app-ideas-no-one-has-done`, `how-to-come-up-with-app-ideas`, `long-tail-keywords-app-store`.

- **2026-11-11 · đợt 10 xong (50/100), push `bf0c761` lên main:** bồi `best-time-to-launch-an-app` + 4 bài mới: `seasonal-app-ideas` · `app-store-autocomplete-keywords` (keyword `app store autocomplete`) · `check-app-store-keyword-ranking` (keyword `check app store ranking`) · `free-aso-audit`. Bỏ `why-google-trends-data-changes` vì trùng bài live `is-google-trends-accurate`. Số mới: Trends US 5 năm cho 22 loại app (đo trên 11/2021–5/2025 vì nhiều từ cùng nhảy 7/2025 và cùng rơi tuần 12/7/2026: budget app 73→37, diet app 34→18): 7 loại đỉnh quanh Tết dương (25/12–7/1, một lần 22/1), thuế cuối 1–giữa 2, vườn 2–3, packing list và golf 6–7, homework/fantasy/flashcards cuối 8–giữa 9, advent/christmas/gift list cuối 11–12; advent calendar đỉnh 5x và 6 app yếu, packing list 6, garden planner 4, còn tax/gift/golf/fantasy/fishing do app lớn giữ; gợi ý App Store giữ 8–10/10 cụm qua đêm nhưng luôn đổi thứ tự, Mỹ–Anh chỉ chung 0–5/10, Google chung 1–3/10; thứ hạng 5 app nhỏ ở 5 nước: Habit Rabbit hạng 7 (UK) đến 13 (CA), HabitKit hạng 2 "habit tracker" nhưng ngoài top 200 "habit tracker widget" ở 4/5 nước, PillCat không vào top 200 tiếng Anh ở Đức, Super Simple Pill Reminder chỉ bán ở Mỹ và Canada; audit 10 điểm: Habit Rabbit 1 năm không cập nhật. Lấy Trends bằng pytrends trong venv của MCP (lưu được CSV, nghỉ 20 giây giữa các lượt, không bị 429 trừ 1 lần). Đã xem kết quả `blog check` trước khi commit. Bài cũ link về: `google-trends-for-apps`, `app-store-search-trends`, `app-store-keyword-planner`, `app-store-keyword-gap-analysis`, `free-aso-tools`.

- **2026-11-11 · đợt 11 xong (55/100), push `d0fdff7` lên main:** 5 bài mới cụm review + Trends + Android ASO: `app-store-reviews-api` · `google-play-review-scraper` · `app-review-sentiment-analysis` · `google-trends-429-too-many-requests` (keyword `google trends 429`) · `free-aso-tools-for-android` (keyword `aso tools for android`). Số mới: RSS review Apple dừng ở 500 (Finch 500 review = 27 ngày, HabitKit 215 review về tới 11/2022, Medisafe dừng ở 300, nomi 1 review trả về dạng object chứ không phải list); App Store Connect API chỉ đọc app của mình (lọc rating, territory, đã trả lời; 1 phản hồi / review); google-play-scraper lấy 3.000 review / app trong 20 lượt (Finch 28 giây, 11 tuần; Loop gần 3 năm), không chạm trần, Medisafe trả lời 90/3.000; 10.067 review: 23% review 5★ và 51% review 4★ có chữ tiêu cực, 27% review 1★ có chữ tích cực, "ads" trong review 4–5★ phần lớn là khen "no ads" (Loop 300/2.820); Medisafe tháng 12/2025 có 397 review, 310 là 1–2★, 88% than paywall; log Trends: 20 giây / lượt thì 7 lượt 0 lỗi, 12 lượt có 1 lần 429 ở lượt 12, chờ 60 giây là được, gọi lại cùng ngày giống hệt 0/1.310 điểm (bài chỉ khuyên đi chậm + cache, không chỉ cách lách giới hạn); chỉ 13/30 gợi ý Play trùng App Store. Bài cũ link về: `app-store-review-scraper`, `analyze-app-store-google-play-reviews`, `turn-one-star-reviews-into-features`, `google-trends-api`, `is-google-trends-accurate`, `free-aso-tools`, `google-play-aso`, `google-play-keyword-research-free`. `blog check` 0 lỗi trước khi commit.

## Liên quan

[GEO](geo.md) · [AEO](aeo.md) · [Plan blog SEO + GEO 2026-11-07](plan-blog-seo-geo-2026-11-07.md) ·
[Plan Data research](plan-data-research-2026-11-08.md) · [Free tool](free-tool.md)
