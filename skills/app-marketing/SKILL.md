---
name: app-marketing
description: "Bước 12 của pipeline app — kế hoạch ra mắt cho người không có ngân sách lớn: định vị một câu, chân dung người dùng, trang landing 5 variant (sticker/CapWords · bento/Flighty · cinematic/Opal · classic/Things · cards/Gentler Streak) từ landing.md → make_site.py + check_landing.py (skill dùng chung growth:landing-page), kèm trang Our Story + Press, danh sách email + lead magnet dựng trước D-21, lịch tuần ra mắt D-21 → D+7, kênh phù hợp (cộng đồng Facebook/TikTok/Zalo ở Việt Nam, Reddit/Product Hunt quốc tế, người sáng tạo nội dung, Apple Search Ads ngân sách nhỏ để lấy từ khoá thật), bộ nội dung mẫu, mục tiêu đo được. Ghi marketing.md, bước xong khi Launched: yes. Use when someone wants users, 'marketing app', 'ra mắt app thế nào', 'quảng bá app', 'đăng bài ở đâu', 'tiktok cho app', 'product hunt', 'trustmrr', 'công khai doanh thu', 'listing cộng đồng', 'directory ra mắt', 'apple search ads', 'landing page app', 'landing kiểu capwords', 'landing kiểu flighty', 'landing kiểu opal', 'variant landing', 'trang giới thiệu app', 'trang press', 'our story', 'lead magnet', 'danh sách email', 'waitlist', 'thu email khách', 'chưa ai tải app', or when scripts/app.py status says step 12 is next. Không đăng bài thay người dùng, không mua quảng cáo."
argument-hint: "[slug]"
user-invocable: true
---

# Bước 12 — marketing

**Một việc:** `marketing.md` có kế hoạch cụ thể, đã chạy tuần ra mắt, dòng `Launched: yes`.
Bắt đầu **song song** với `/app-publish` — landing page và danh sách email cần có trước ngày live (Pha 2 xong trước D-21).

Đọc: [references/launch-playbook.md](references/launch-playbook.md) · landing: skill dùng chung `growth:landing-page`
→ [design-variants.md](../../../.agents/skills/landing-page/references/design-variants.md) (5 variant học từ trang thật: chọn variant nào, vì sao người xem muốn xài, mục nào lấy chữ từ file nào).
Bản chép trong repo: `.agents/skills/landing-page/` — sửa ở repo ai-skills-shared rồi `PLUGINS="growth" scripts/sync-to-codex.sh <repo>`.

## Pha 1 — Định vị (điền đầu marketing.md)

Từ context-ai/research-<slug>.md + spec.md, viết:
- **Cho ai** — một nhóm người cụ thể, không phải "mọi người".
- **Họ đang dùng gì thay thế** — app đối thủ, giấy bút, không làm gì.
- **Khác biệt một câu** — lấy từ nhóm lời than ở research §4.

Hỏi người dùng duyệt 3 dòng này trước khi viết nội dung nào.

## Pha 2 — Danh sách email + lead magnet (xong trước D-21)

Ngày ra mắt phải có sẵn người để báo. Chi tiết + luật store: playbook §2.

1. **Chọn mồi (lead magnet)** — thứ miễn phí khách nhận ngay khi để email, gắn với "Khác biệt một câu":
   danh sách chờ + ưu đãi người đăng ký sớm (mặc định) · checklist/template/bộ prompt PDF · bản dùng thử app Mac bán ngoài store.
   Ghi `Lead magnet:`. Mồi là file → làm xong file thật trước khi mở form.
2. **Chọn công cụ có gói free + form + link huỷ đăng ký** (MailerLite / Buttondown / Kit) → ghi `Email tool:`.
   Người dùng tự mở tài khoản; Claude soạn chữ form + email, không đăng nhập thay.
3. **Gắn form lên landing** — URL form vào `app.json` (`email_form_url`, `lead_magnet`) → chạy lại `make_site.py`:
   trang chủ có nút đăng ký, Privacy tự thêm mục danh sách email. Ghi `Email form:`.
4. **Soạn 3 email** vào bảng (chào mừng + trao mồi · D-3 · D0). Người dùng tự đăng ký thử bằng email riêng để thấy email 1 tới.
5. **Đếm** — `Subscribers: N (YYYY-MM-DD)` đọc từ công cụ email, không ước.

Luật: app iOS/Android **không được bắt nhập email** mới cho dùng (Apple 5.1.1 — mục Account Sign-In, app không cần tài khoản) — ô email trong app
chỉ tự nguyện, hoặc để thu trên web. Không mua danh sách, không thêm email người khác khi họ chưa tự đăng ký.
`app.py status` báo `invalid` nếu `Launched: yes` mà 3 dòng trên còn `TODO`.

## Pha 2b — Landing page (song song Pha 2, xong trước D-21)

Mạch + lý do: [design-variants.md](../../../.agents/skills/landing-page/references/design-variants.md) (growth:landing-page). Trang phải làm người xem **thấy app chạy trong 3 giây**
(video quay app thật ngay dưới headline), **thấy mình trong đó** (ảnh người dùng đời thường), **hết lo** (Privacy nói thật).

1. **Chọn variant** theo bảng trong design-variants.md (sticker · bento · cinematic · classic · cards). Ghi lý do 1 dòng vào LEARNED.md.
   App Mac (`stack: macos`) → theo `/app-mac-landing` (layout × theme học từ app Mac native, variant `window` · `spotlight` · `editorial`).
   `cp .agents/skills/landing-page/templates/landing.md apps/ACTIVE/<slug>/context-ai/landing.md`, đặt `Variant:`, điền chữ từ marketing.md (Định vị), spec.md, money.md.
   Chữ trên trang viết bằng ngôn ngữ người mua (thường tiếng Anh).
2. Ảnh/video vào `site/media/`: Claude quay simulator + chụp `run_app.py shot`. Cảnh người: Codex sinh
   (tuyến `core:asset-prompt`, dùng lại cảnh `/app-store-art` nếu có). Sticker/thẻ: xuất thật từ app.
3. `python3 scripts/make_site.py <slug>` → `site/index.html` (landing) + `story.html` + `press.html` + 3 trang pháp lý.
4. `python3 .agents/skills/landing-page/scripts/check_landing.py apps/ACTIVE/<slug>` tới 0 FAIL. Rồi mở qua server tĩnh, **Read screenshot desktop +
   mobile 375px** trước khi báo xong.
5. Story: hỏi người dùng chuyện thật vì sao làm app (2–4 câu). Claude biên tập, không bịa.
6. **Trang bán riêng trên oneclicktool.app** (app đã có trang ở oneclicktool.app và sắp chạy quảng cáo / đăng social) →
   `/oneclicktool-landing` (skill máy `~/.claude/skills/oneclicktool-landing`): trang Next.js style riêng, đủ 12 khối bán hàng
   (hook · video demo · nỗi đau · cách dùng · features · shorts · trust · offer · email · follow · FAQ · CTA cuối).
   Video demo + shorts làm trước bằng `/app-video`. Mẫu: Sweepy `/macos/sweepy`, Markdown Viewer `/desktop/markdown-viewer`.

## Pha 3 — Kênh (chọn 2–3, làm tốt hơn làm nhiều)

| Kênh | Hợp khi | Việc cụ thể |
|---|---|---|
| Landing (`landing.md` → `make_site.py`) | luôn | landing kiểu CapWords (Pha 2b) + nút đăng ký email (Pha 2) + nút tải khi live |
| Cộng đồng người dùng mục tiêu (nhóm Facebook, subreddit, Discord) | có nhóm đúng chủ đề | đọc luật nhóm, đóng góp trước, chia sẻ như người làm chứ không spam link |
| TikTok / Reels / Shorts | app có khoảnh khắc nhìn thấy được | 5–10 video 15–30s quay màn hình thật: vấn đề → app giải → kết quả |
| Product Hunt / Hacker News Show | app tiếng Anh, người dùng công nghệ | ra mắt thứ Ba–Thứ Năm, chuẩn bị ảnh + câu trả lời |
| Apple Search Ads (Basic/Advanced) | đã live iOS | 5–10 USD/ngày × 1 tuần — mục tiêu là **báo cáo từ khoá thật**, không phải lãi |
| Người sáng tạo nội dung | có ngân sách nhỏ hoặc trao đổi Pro miễn phí | gửi mã Pro (Offer Codes / Promo codes) |
| Slideshow ảnh TikTok (không lộ mặt) | app có kết quả nhìn thấy được | 5–7 slide: slide 1 câu móc < 8 chữ, câu khẳng định; slide cuối = màn hero (mockup trước ra mắt, ảnh chụp thật sau ra mắt) |
| X build-in-public | người làm chịu đăng đều 3–5 bài/tuần | tiến độ + ảnh màn hero; sau ra mắt đăng số thật (ảnh RevenueCat) và nối RevenueCat lên TrustMRR để được thấy trên bảng doanh thu xác minh |

**X:** nháp ở `marketing/x/NN-*.md`; sổ thật là `marketing/x-marketing.md` (khuôn `templates/x-marketing.md`): `## Facts` để viết bài
và `## Đã đăng` = bài đã đăng thật, mới nhất trên cùng. Promo Desk ▸ Mark as posted tự chép bài vào sổ; đăng ngoài Promo Desk mà
người dùng báo "đã đăng" thì Claude chép tay đúng khuôn (ngày · URL · file nháp · chữ đã đăng). Chỉ chữ, không bảng.

**Ảnh quảng cáo → landing:** ảnh làm riêng để đăng (ảnh launch, ảnh ra mắt Pro/payment… — không phải ảnh store đã có trên trang)
cũng lên mục *From the launch* của landing oneclicktool: `python3 scripts/promo_gallery.py add <slug> <ảnh> --title "..." --alt "..." --channel x|reddit --date YYYY-MM-DD`
(ảnh → repo public `app-demo` qua GitHub Pages, web chỉ giữ `content/promo/<slug>.json`; chữ tiếng Anh). Đăng xong chạy lại với `--url <link bài>`.
Push app-demo trước, web sau.

Chưa có người theo dõi / muốn cả hệ thống 6 tuần (định vị → 2 kênh ICE → lịch theo chặng → bảng số): `/app-gtm` — ghi file bài
đúng định dạng Campaign của Promo Desk. Bán thẳng cho dân dev / vibe code (app Mac `direct`, kit, tool web): chạy `/app-indie` để mổ 3–8 indie cùng ngách, lấy
kênh + chiêu SEO (trang "X alternative", tool free, README GitHub, changelog) + mindset từ
[app-indie/references/playbook.md](../app-indie/references/playbook.md) §3–5.

Học từ app doanh thu cao (Cal AI, TrackAI, GainFrame…): creator tầm trung 10k–100k follower trả theo hiệu quả ăn hơn
người nổi tiếng; video/slide cho thấy kết quả trong 3 giây đầu. Số + nguồn: `research/<ngày>-<chủ-đề>.md`.

## Pha 3b — Listing cộng đồng (directory + trang công khai doanh thu)

Đọc [reference/README-APP-MARKETING-01-COMMUNITY-LISTINGS.md](../../../reference/README-APP-MARKETING-01-COMMUNITY-LISTINGS.md).
- **Trước ngày live:** BetaList (app chưa ra). **Tuần ra mắt:** Product Hunt / Show HN / Uneed / Peerlist / AlternativeTo… — 
  chọn 5–10 trang đúng người, soạn mô tả riêng từng trang từ listing, không chép một đoạn cho mọi nơi.
- **Khi đã có doanh thu thật:** TrustMRR / StartupPage (xác thực bằng khoá read-only). App thu tiền bằng StoreKit trực tiếp
  phải gắn RevenueCat trước — đó là `/app-feature`, ghi backlog, không làm trong bước này.
- Ghi từng trang vào marketing.md mục **Listing cộng đồng** (trạng thái · ngày · link). Người dùng tạo tài khoản / nối thanh toán / bấm Submit.

## Pha 4 — Lịch tuần ra mắt + nội dung

Điền bảng lịch trong marketing.md (mẫu D-21 → D+7 trong playbook). Soạn sẵn nội dung vào marketing.md mục Nội dung:
bài ra mắt (dài/ngắn), 3 kịch bản video, tin nhắn mời tester/bạn bè, thông cáo báo chí.
**Người dùng tự đăng.** Claude không đăng nhập mạng xã hội, không nhắn tin thay.

## Pha 5 — Đo

Mục tiêu tuần đầu viết bằng hành động đo được: số người trong danh sách email, lượt xem trang store, lượt cài, số người mở paywall, số dùng thử/trả phí,
số đánh giá. Không hứa doanh thu. Số liệu đi vào `grow.md` từ tuần sau.

Khi app đã live và tuần ra mắt đã chạy: `Launched: yes`, `Launch date: YYYY-MM-DD`.

## Skill cộng đồng tham khảo

`coreyhaines31/marketingskills` (launch, social, copywriting, content-strategy, public-relations, marketing-psychology) ·
`Eronred/aso-skills` (app-launch, apple-search-ads, creator-ugc-marketing, press-and-pr, referral-program). Cài/đọc: reference/README-REFERENCES.md.

LEARNED.md mục **Bước 12** · `scripts/app.py log` · tiếp theo `/app-grow`.
