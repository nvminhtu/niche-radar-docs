# Plan · Analytics — 2.000 active user / tháng cho shotmatic.app

> Kéo shotmatic.app lên **2.000 active user / tháng** trên GA4 bằng các kênh "im lặng": SEO blog, free tool,
> programmatic SEO, AEO / GEO. **Không launch Product Hunt / Show HN** khi app chưa được chứng minh. Số mục tiêu là
> **giả định** để đặt đích; số hiện tại **chưa đo** (khoá GA / Search Console đang thiếu, 2026-11-02).

<span class="chip chip--todo">Plan · chưa làm · 2026-11-02 · Đợt 0 chờ khoá service account</span>

<div class="box box--goal" markdown>
**Đích**

- **2.000 active user / tháng** trên GA4 (tháng = 28 ngày cuộn), tức khoảng **500 / 7 ngày ≈ 70 / ngày**.
- Phần lớn đến từ **Google + AI search** (kênh Organic Search và Referral từ ChatGPT / Perplexity / Gemini), không phải từ một cú launch.
- Đạt trong khoảng **3–6 tháng** kể từ Đợt 0 (giả định, SEO cần thời gian).

**Xong khi:** GA4 báo ≥ 2.000 active user / 28 ngày **2 tháng liền** · Search Console có ≥ 10 bài nằm top 10 ·
bảng số tuần ở cuối trang đủ cột từ tuần 1. Chưa đo được thì ghi `chưa đo`.
</div>

## Vì sao không launch Product Hunt / Show HN lúc này

Anh chốt 2026-11-02:

- Người vào Product Hunt phần lớn là **maker khác và người gửi mail chào hàng**, không phải người mua.
- App **chưa được chứng minh** (chưa có số chuyển đổi), launch sớm dễ thành **thêm đối thủ** chép idea mà không ra đơn.
- Traffic launch là **một cú vọt rồi tụt**, không giúp đạt mốc tháng nào cũng 2.000.

SEO kéo traffic im lặng, đối thủ khó thấy, và người vào là người đang gõ đúng nỗi đau. Product Hunt để dành tới khi
có số chuyển đổi thật (xem [Phase 47 · Chọn 2 kênh](phase-47-two-channels.md)).

## Đọc số cho đúng

- **"Active user / tháng" của GA4 = 28 ngày cuộn**, không cộng số từng ngày lại (người quay lại bị đếm nhiều lần).
- **Tách 2 loại khách**: khách đọc landing / blog và khách đã tải app. Mục tiêu 2.000 là khách **web** (landing + blog).
- **Tín hiệu sớm nhất của blog là impressions** trên Search Console, không phải số trên GA. Click và active user đến sau.
- Chi tiết cách đọc số GA4 + phễu tính ngược: [Research · SaaS làm marketing](research-marketing-saas.md).

## Đợt 0 · Mở lại bảng đo + ghi số mốc (tuần 0)

Chưa có số mốc thì không biết blog có đang chạy hay không. Làm đợt này trước mọi việc khác.

- [ ] **(Anh)** đặt khoá service account vào đúng `~/.config/gcp/oneclicktool-sa.json` (MCP `google-analytics` và `search-console` cùng dùng file này; 2026-11-02 cả hai báo thiếu file)
- [ ] **(Anh)** thêm email service account vào property GA4 của shotmatic.app (quyền Viewer) và vào Search Console (quyền Đọc)
- [ ] Claude ghi **số mốc GA4 28 ngày**: active user · new user · sessions · kênh (Organic Search, Direct, Referral, Social) · top 20 trang vào đầu tiên
- [ ] Claude ghi **số mốc Search Console 28 ngày**: impressions · click · CTR · vị trí TB · số bài đã index / bị loại
- [ ] Soát 64 bài blog: bài nào **đã index**, bài nào chưa (gửi lại sitemap nếu cần)
- [ ] Soát CTA `/download?ref=blog-<slug>` có vào GA4 không, để đếm được blog nào ra lượt tải

## Đợt 1 · Blog: chăm 64 bài đã có trước, viết thêm sau (tuần 1–8)

Đã đăng 59 bài (2026-11-01 và 02), 5 bài hẹn 04–13/11 (xem [Phase 46.1 · Blog](phase-46-1-landing-blog.md)). Không cần viết ồ ạt
thêm. Việc chính là **xem bài nào Google đang thử** rồi đẩy tiếp bài đó.

- [ ] Mỗi tuần mở Search Console, ghi số impressions và click (bảng ở cuối trang)
- [ ] Bài có impressions mà **vị trí 8–30**: sửa lại cho sát câu hỏi, thêm số tự đo, thêm FAQ, thêm link nội bộ từ bài khác
- [ ] Bài **0 impressions sau 6 tuần**: xem lại từ khoá (có ai gõ không?), sửa tiêu đề hoặc gộp vào bài khác
- [ ] Viết thêm **2–3 bài / tuần**, chỉ từ từ khoá đã đo thật bằng `/shotmatic-blog` (Autocomplete + Trends + xem SERP)
- [ ] Không viết 2 bài cùng một từ khoá (tự giành hạng của nhau)

Cách nhận biết blog đang chạy:

| Thời điểm | Dấu hiệu đúng hướng |
|---|---|
| Tuần 2–6 | Bài đã index, impressions tăng dần dù click gần như bằng 0 |
| Tháng 2–3 | Vài bài lên top 20–30, có vài click mỗi ngày |
| Tháng 3–6 | Vài bài lên top 10, tổng 30–100+ click / ngày từ Google |

Nếu sau 6–8 tuần impressions vẫn gần như bằng 0, lỗi nằm ở **cách chọn từ khoá hoặc index**, đừng bỏ kênh blog.

## Đợt 2 · Free tool trên shotmatic.app (tuần 3–8)

Free tool thường kéo traffic nhanh hơn blog, vì người ta tìm "X checker / X generator" rất nhiều, và trang tool tự có
backlink. Đã có sẵn logic chạy được trong 2 extension, chỉ cần đưa lên web:

- [ ] Chọn **1 tool** để làm trước (anh chốt). Ứng viên:
    - **Niche check** bản web (giống extension ShotMatic Lite: tra iTunes Search + app đầu Google Play → Worth a look / Think twice / Crowded)
    - **App Store keyword difficulty checker** (đã có bài `app-store-keyword-difficulty-without-search-volume`)
    - **Amazon keyword → app idea** (giống extension ShotMatic Scout)
- [ ] Đo từ khoá cho tên tool trước khi làm (Autocomplete + Trends), chọn tên người ta gõ thật
- [ ] Giới hạn lượt tra / ngày để không lộ hết sức mạnh bản đầy đủ, cuối kết quả có nút tải ShotMatic
- [ ] Gắn event GA4 `tool_run` và `store_click` / `download` để biết tool ra bao nhiêu lượt tải

## Đợt 3 · Programmatic SEO (tháng 2–3, chỉ khi Đợt 1 có tín hiệu)

Tạo nhiều trang từ một khuôn chung, mỗi trang có **số thật riêng** chứ không chỉ đổi chữ.

- [ ] Khuôn **"[tool] alternative"**: đã có 7 bài tay (App Annie, Sensor Tower, Appfigures…), xem bài nào có impressions rồi mới nhân lên
- [ ] Khuôn **"[niche] app ideas"**: mỗi trang chạy ShotMatic thật cho niche đó, ghi số + ngày đo
- [ ] Không đăng trang mỏng (chỉ đổi tên niche): Google phạt cả site

## Đợt 4 · AEO / GEO: được AI search trích (song song mọi đợt)

- [ ] Đo mốc: hỏi ChatGPT / Perplexity / Gemini 5 câu thuộc cụm chính, ghi ShotMatic có được nhắc không
- [ ] Mỗi bài giữ khuôn đã có: `answer` 40–60 từ đầu bài, H2 dạng câu hỏi, FAQ ngắn, `evidence` có số tự đo
- [ ] Đo lại mỗi 4 tuần, ghi vào bảng số tuần

## Kênh phụ, cũng "im lặng" (không lộ idea)

- **Reddit Q&A** bằng `/reddit-qa`: trả lời đúng câu hỏi người ta đang hỏi, chỉ nhắc ShotMatic khi hợp (hàng chờ ở `marketing/reddit/`).
- **Video ngắn demo**: quay cảnh ShotMatic giải một nỗi đau, 15–30 giây. Không cần lộ toàn bộ cách làm.

## Mốc kỳ vọng (giả định, không phải số đo)

| Thời gian | Việc chính | Active user / 28 ngày |
|---|---|---|
| Tuần 0 | Đợt 0: mở bảng đo, ghi số mốc | `chưa đo` |
| Tuần 1–4 | Chăm 64 bài, viết thêm 2–3 bài / tuần | ~200–500 |
| Tuần 5–8 | Free tool lên, sửa bài có impressions | ~500–1.000 |
| Tuần 9–12 | Programmatic SEO nếu có tín hiệu, GEO | ~1.000–2.000 |
| Tháng 4–6 | Giữ nhịp, refresh bài top 20 | ≥ 2.000 |

**Lưu ý:** chỉ chạy đều 1–2 kênh chính (blog + free tool). Làm cả 10 kênh mỗi kênh một chút thì không kênh nào lên.

## Bảng số tuần

Claude điền mỗi tuần từ GA4 + Search Console. Chưa có khoá thì ghi `chưa đo`.

| Tuần · ngày đo | GA4 (28 ngày) | Search Console (28 ngày) | Lượt tải từ blog |
|---|---|---|---|
| 0 · 2026-11-02 | active user `chưa đo` · Organic `chưa đo` | impressions `chưa đo` · click `chưa đo` · bài top 10 `chưa đo` | `chưa đo` |

## Liên quan

[Research · SaaS làm marketing](research-marketing-saas.md) · [Phase 46.2 · Từ khoá + blog + Search Console](phase-46-2-seo-keyword-blog-gsc.md) ·
[Phase 46.1 · Blog](phase-46-1-landing-blog.md) · [Phase 47 · Chọn 2 kênh](phase-47-two-channels.md) · [Kế hoạch bán ShotMatic](../app/ke-hoach-ban-shotmatic.md) ·
Skill: `/shotmatic-blog`, `/reddit-qa`, `marketing-skills:free-tools`, `marketing-skills:programmatic-seo`, `marketing-skills:ai-seo`
