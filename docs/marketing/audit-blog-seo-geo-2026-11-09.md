# Audit bài blog shotmatic.app · SEO + GEO

> Chấm 85 bài đang đăng trên shotmatic.app/blog (bỏ 54 bài `draft`) bằng bộ tiêu chí gộp từ 3 repo skill SEO miễn phí
> nhiều sao nhất trên GitHub. Mục tiêu: biết bài nào yếu chỗ nào, sửa gì trước để lên top Google và được AI trích.

<span class="chip chip--todo">Audit · 2026-11-09 · chưa có số Search Console (thiếu file khoá)</span>

<div class="box box--goal" markdown>
**Kết luận**

- **Khung GEO của blog đã tốt, thân bài quá mỏng.** Bài nào cũng có short answer, FAQ, nguồn, schema BlogPosting + FAQPage, bản `.md`, `llms.txt`. Nhưng thân bài trung vị chỉ **418 từ**, 83/85 bài dưới 1.500 từ. Bài "alternative" chỉ 270–320 từ.
- **Title quá dài.** Trung vị 74 ký tự, 76/85 bài vượt 60, cộng thêm đuôi " — ShotMatic" nên Google cắt gần hết.
- **Keyword đặt lệch.** 56 bài không có keyword trong H2 nào, 46 bài không có trong description, 34 bài không có trong 100 từ đầu.
- **Thiếu dấu hiệu tự làm.** 62 bài không có câu kiểu "we measured… on Oct 31, 2026"; 45 bài không có một ảnh/screenshot nào.
- **30 bài không được bài nào khác link tới trong thân bài.** Chỉ có trang chủ đề trỏ vào.
- **PerplexityBot vẫn bị chặn 403.** Đây là lỗ GEO lớn nhất ở phía kỹ thuật.

**Xong khi:** 20 bài ưu tiên đạt ≥ 1.200 từ thân bài, title ≤ 60 ký tự, keyword đúng 4 chỗ, có ≥ 1 số tự đo + 1 ảnh, và mỗi bài có ≥ 3 bài khác link tới.
</div>

## Đã sửa gì (2026-11-09)?

**Đợt 1 · title + description + H2, 86 bài** (90 bài đang đăng, gồm 5 bài mới của đợt 1 plan AI search). Commit `c2468fa` ở repo shotmatic, đã push lên `main` ngày 2026-11-09 (rebase lên sau đợt 2 plan AI search). 5 bài đợt 2 chưa qua soát title/H2 này.

- Title: còn 0 bài vượt 60 ký tự (trước 79). Trang bài chỉ thêm đuôi " — ShotMatic" khi tổng vẫn ≤ 60 ký tự.
- Keyword trong description: còn 0 bài thiếu (trước 47). Trong H2: còn 0 (trước 57). Trong title: còn 0 (trước 10).
- Không đổi slug (đổi URL mất link cũ), không đổi `updated` (chỉ sửa chữ, không phải cập nhật nội dung).
- Còn lại: 34 bài chưa có keyword trong 100 từ đầu / short answer, 12 slug không chứa keyword (giữ nguyên), và mọi việc ở bước 3–6 bên dưới.

## Lấy skill audit từ đâu?

Tìm trên GitHub ngày 2026-11-09, lấy 3 repo miễn phí nhiều sao nhất, đang cập nhật:

- **coreyhaines31/marketingskills · 59.240★.** Đã cài sẵn trong máy (`marketing-skills:seo-audit`, `marketing-skills:ai-seo`). Lấy phần on-page và AI citation.
- **AgriciDaniel/claude-seo · 27.474★.** Lấy skill `seo-content` (E-E-A-T, độ dài tối thiểu, link nội bộ 3–5/1.000 từ, keyword ở title/H1/100 từ đầu) và `seo-page`.
- **zubair-trabzada/geo-seo-claude · 11.581★.** Lấy skill `geo-citability`: mỗi section mở bằng câu trả lời tự đứng được, không mở bằng "it/this", có số, có bảng, đoạn 134–167 từ.

Hai repo sau chỉ clone về đọc rubric, không cài, không chạy script của họ. Script chấm tự viết lại: [audit-blog-seo-geo.py](audit-blog-seo-geo.py). Kết quả từng bài: [audit-blog-seo-geo-2026-11-09.csv](audit-blog-seo-geo-2026-11-09.csv) (xếp từ bài nhiều lỗi nhất).

## Audit cái gì?

Chia làm 3 nhóm. Nhóm 1 và 2 là để lên top Google, nhóm 3 là để AI (AI Overview, ChatGPT, Perplexity, Claude) trích.

**1 · Kỹ thuật (cả site).** Bot có vào được không, có index không, schema, canonical, `llms.txt`, sitemap.

**2 · SEO on-page (từng bài).** Title ≤ 60 ký tự. Keyword nằm ở title, description, slug, 100 từ đầu và ít nhất 1 H2. Độ dài đủ phủ chủ đề. Link nội bộ 3–5/1.000 từ và có bài khác link tới. Ảnh có alt. Ngày cập nhật. Không có hai bài tranh cùng keyword.

**3 · GEO / E-E-A-T (từng bài).** Section mở bằng đoạn trả lời 15–80 từ, không mở bằng đại từ. Có bảng. Có số. Có dấu hiệu tự đo, tự thử (Experience). Có trích nguồn ngay trong thân bài. Không có văn kiểu AI.

## Kỹ thuật: đang ổn chỗ nào?

- Canonical, `og:*`, `twitter:card` đủ. Schema mỗi bài: BlogPosting, BreadcrumbList, FAQPage, Organization, Person, có `datePublished` / `dateModified`.
- `llms.txt` trả 200, liệt kê trang + bài theo chủ đề, có `llms-full.txt` và bản `.md` cho từng bài.
- Sitemap có 109 URL. Không có hai bài trùng `keyword`.
- Googlebot, Bingbot, Applebot, OAI-SearchBot (ChatGPT search), ChatGPT-User, Claude-SearchBot, Claude-User, Perplexity-User đều vào được (200).

## Kỹ thuật: phải sửa gì?

- **PerplexityBot → 403.** Bot này dựng index cho Perplexity; chặn nó thì Perplexity khó trích bài. Robots.txt không chặn, chặn nằm ở tường lửa Cloudflare (bật "Block AI bots"). Sửa: Cloudflare → Security → Bots, cho phép PerplexityBot. Test bằng UA giả nên cần xác nhận lại trong Cloudflare log.
- **GPTBot, ClaudeBot, CCBot → 403, Google-Extended bị Disallow.** Đây là bot huấn luyện, chặn không ảnh hưởng AI Overview hay ChatGPT search. Giữ nguyên là được, chỉ cần biết là chủ ý.
- **Ảnh OG giống nhau cho mọi bài** (`/og/shotmatic-2.jpg`). Không phải lỗi xếp hạng, nhưng chia sẻ lên mạng xã hội trông như nhau. Làm sau.
- **Tác giả "Leo Nguyen" trỏ sang oneclicktool.app/about.** Nên có trang tác giả ngay trên shotmatic.app (ai viết, đã làm app gì) để tăng điểm Who của Google.

## SEO on-page: 85 bài đang thế nào?

Đếm số bài dính từng lỗi (một bài dính nhiều lỗi):

- **83 bài · thân bài dưới 1.500 từ.** Trung vị 418, ít nhất 271, nhiều nhất 1.909. Google không chấm theo số từ, nhưng 300 từ không đủ phủ một câu hỏi so với các bài đang top. `check_post.mjs` đòi ≥ 1.200 từ cho bài mới; bài cũ chưa đạt.
- **76 bài · title > 60 ký tự.** Trung vị 74, dài nhất 92. 54 bài vượt 70.
- **56 bài · keyword không có trong H2 nào.**
- **46 bài · keyword không có trong description.**
- **34 bài · keyword không ở 100 từ đầu (kể cả short answer).**
- **30 bài · không bài nào link tới trong thân bài** (chỉ có trang chủ đề / `/blog/all`). Danh sách ở cuối trang.
- **11 bài · slug không chứa keyword. 10 bài · title không chứa keyword.**

## GEO: 85 bài đang thế nào?

- **80 bài · không có link nguồn trong thân bài.** Nguồn chỉ nằm ở khối `sources` cuối bài. AI trích dễ hơn khi câu có số đi kèm link ngay tại chỗ.
- **62 bài · không thấy dấu hiệu tự đo / tự thử.** Không có câu kiểu "We pulled 500 reviews on Oct 31, 2026".
- **61 bài · dưới 70% section mở bằng đoạn trả lời.** Nhiều section mở bằng list hoặc câu dẫn.
- **45 bài · không có ảnh hay screenshot nào.**
- **8 bài · không có bảng.** Mật độ số thì tốt (trung vị 44 số / 1.000 từ), chỉ 2 bài thấp.

## Ví dụ bài yếu: Astro alternative

`astro-alternative-with-google-play`, 11 lỗi, nhiều nhất blog.

- Keyword `astro aso alternative` không có ở title, description, H2, slug. Title 74 ký tự.
- Thân bài 271 từ: 1 bảng so sánh, 2 list, 1 đoạn. Không có số tự đo, không có ảnh.
- Không bài nào link tới.

Sửa theo hướng: title "Astro ASO Alternative for Google Play + App Store" (49 ký tự). Thêm H2 "What is the best Astro ASO alternative?" mở bằng câu trả lời 40–60 từ. Thêm một phép đo thật (chạy cùng 1 keyword trên ShotMatic, chụp màn hình, ghi ngày). Thêm phần "How to switch from Astro" và "Pricing compared" có link nguồn. Link tới bài từ 3 bài cùng chủ đề `tools`.

## Ví dụ bài tốt: phân tích review

`analyze-app-store-google-play-reviews` là khuôn nên nhân ra các bài khác.

- Có số tự đo thật: 1.500 review của 3 app meal planner, ngày 2026-10-31, 603 review 1–3★, 141 câu "I wish".
- 8 H2 đều là câu hỏi, section mở bằng câu trả lời.
- Còn thiếu: keyword `app store review analysis` chưa có trong title và H2, thân bài 971 từ, title 74 ký tự.

## Sửa theo thứ tự nào?

1. **Mở chặn PerplexityBot** trong Cloudflare. 5 phút, ảnh hưởng mọi bài.
2. **Sửa title + description + 1 H2 cho cả 85 bài.** Việc nhỏ, làm hàng loạt: title ≤ 60 ký tự có keyword, description có keyword, một H2 chứa keyword.
3. **Nối link cho 30 bài không ai link tới.** Mỗi bài thêm 3 link từ bài cùng chủ đề.
4. **Viết dày 20 bài ưu tiên** lên ≥ 1.200 từ, mỗi bài thêm 1 phép đo thật + 1 screenshot ShotMatic + nguồn ngay trong câu. Chọn 20 bài theo số Search Console khi có khoá; trước đó ưu tiên bài "alternative" và bài dẫn về sản phẩm.
5. **Thêm trang tác giả** trên shotmatic.app.
6. Đưa các tiêu chí mới (keyword ở H2/description, title ≤ 60, ≥ 3 link tới) vào `check_post.mjs` để bài sau không lặp lỗi.

## 30 bài không bài nào link tới

ai-app-ideas-that-are-not-wrappers, app-annie-alternative-for-indie-developers, app-idea-generator, app-ideas-for-beginners,
app-research-tool-mac-no-subscription, app-store-product-page-optimization, appfigures-alternative-one-time-purchase,
apptweak-alternative-for-indie-developers, astro-alternative-with-google-play, best-mcp-servers-for-app-developers,
build-an-app-in-a-weekend-with-ai, build-in-public-indie-app, chrome-extension-ideas, claude-opus-5-5-for-app-builders,
codex-vs-claude-code, estimate-app-revenue-from-public-signals, exploding-topics-alternative-for-app-ideas,
flutter-vs-react-native-vs-native-indie, google-play-niche-research, how-narrow-should-your-app-niche-be, how-to-name-an-app,
indie-hacking-guide-2026, is-it-ok-to-clone-an-app, mac-app-ideas-menu-bar, product-hunt-launch-for-indie-apps,
publish-vibe-coded-web-app-to-app-store, validate-or-just-build, vibe-coding-security-checklist, when-to-give-up-on-your-app,
why-users-uninstall-apps.

## Giới hạn của audit này

- Chưa có Search Console nên không biết bài nào đang có hiển thị, đứng vị trí mấy. Thứ tự sửa ở trên là đoán theo lỗi, chưa theo traffic.
- Đếm từ, keyword, đại từ bằng regex: có thể lệch vài bài. Keyword so theo từng từ, không theo cụm.
- Test bot bằng User-Agent giả từ máy này; Cloudflare có thể xử lý bot thật (IP đã xác minh) khác.
- Không chấm tốc độ trang / Core Web Vitals.
