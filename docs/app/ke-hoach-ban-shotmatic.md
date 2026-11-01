# Kế hoạch bán ShotMatic: làm tay → chào mời → tự động → traffic thụ động (2026-11-01)

> Làm theo thứ tự tầng 0 → 4. Không nhảy tầng: tầng sau chỉ khuếch đại câu chào đã bán được ở tầng trước.
> Số nào cũng có nguồn + ngày. Tỉ lệ chuyển đổi ghi **giả định** là đoán để đặt mục tiêu, không phải số đo.
> Bản gốc nằm ở repo App-AI-Skills: `apps/ACTIVE/web-apps/niche-radar/marketing/2026-11-01-ke-hoach-ban-shotmatic.md`.

<span class="chip chip--doing">Plan 2026-11-01 · đang làm Tầng 0</span>

<div class="box box--goal" markdown>
**Mục tiêu:** 10 đơn PRO đầu tiên trong 14 ngày bằng tay, rồi biến cách đã bán được thành kênh tự chạy, để có đơn mà
không phải ngồi chào từng người.

**Không làm:** tính năng mới, bản Windows, quảng cáo trả tiền, đổi giá khi chưa có ≥ 10 đơn.
</div>

## Số thật lúc lập plan (2026-11-01)

| Chỉ số | Số | Nguồn |
|---|---|---|
| Lượt tải .dmg | **9** (chỉ v1.0.0, từ 29/10) | GitHub API, release của niche-radar-docs |
| Checkout trong app | có trong code bản 1.1.0, chưa phát hành | `web/src/lib/license/config.ts` |
| Checkout trên landing | chưa — trang ghi "Checkout opens soon" | shotmatic.app |
| Đơn PRO | **0** | chưa có cách mua |
| Bài Reddit / X đã đăng | **0** | thư mục marketing |
| Email danh sách chờ, lượt vào landing | `chưa đo` | EmailOctopus, GA4 |

Chưa có cửa thu tiền và chưa ai biết tới sản phẩm. 9 người đã tải là tài sản quý nhất hiện có.

## Tầng 0 — Mở cửa thu tiền (ngày 0–1)

Chưa xong tầng này thì không làm tầng sau: người đọc bài, muốn mua mà không mua được là mất luôn người đó.

- [x] **0.1** Chốt chính sách bán: $39.99 trả một lần, 2 Mac, hoàn tiền 14 ngày, Free 15 lượt tra — Tu chốt 2026-11-01
- [ ] **0.2** Phát hành 1.1.0 có checkout: .dmg ký + notarize, release GitHub, `/download` trỏ bản mới — Claude build, **Tu bấm Publish release**
- [ ] **0.3** Landing: thay "Checkout opens soon" bằng nút mua thật, link có `?ref=landing` — Claude
- [ ] **0.4** Mua thử bằng test mode Lemon Squeezy → nhận key → dán vào app → thành PRO — **Tu mua**, Claude kiểm app
- [ ] **0.5** Bật Affiliates trong Lemon Squeezy (30 %) để dùng ở tầng 2 — **Tu**

## Tầng 1 — Làm tay, bán từng người (ngày 1–14) · mục tiêu 10 đơn

**Đừng bán phần mềm, bán kết quả.** Người ta không mua "tool tìm niche" (đã có tool $29), họ mua "biết ý tưởng của mình
có đáng làm không + bản brief đưa thẳng cho Claude Code". Ở tầng này mình **tự chạy ShotMatic cho họ** rồi gửi file kết quả.
Đó vừa là demo, vừa là cách học câu chào nào trúng.

### 1.1 Chăm 9 người đã tải (ngày 1–2)

- [ ] Lấy email người đã tải từ EmailOctopus (DownloadGate)
- [ ] Gửi từng thư **tay**, không phải bản tin, hỏi đúng 1 câu: họ đang kiểm ý tưởng app gì → hứa gửi lại brief thật
- [ ] Ai trả lời → Claude chạy niche đó, xuất brief.md + spec.md, Tu gửi lại kèm link mua
- [ ] Ai chưa mở app lần nào → hỏi vì sao (cài lỗi, Gatekeeper, không biết bắt đầu ở đâu) → sửa ngay nếu là lỗi
- [ ] Đếm: số trả lời · số mở app · số đơn

### 1.2 "Gửi ý tưởng, nhận báo cáo miễn phí" — 20 bản (ngày 2–14)

- [ ] **X** (Tu đăng): mời người đang build app bằng Claude Code reply ý tưởng → nhận số thật (đối thủ Play + App Store, lời chê 1★, xu hướng) + brief. Chỉ 20 người đầu
- [ ] **Reddit:** không đăng lời mời riêng (dễ bị coi là spam). Trả lời thẳng các thread "what app should I build" / "is my app idea good" trên r/SideProject, r/indiehackers, r/ClaudeCode, r/iOSProgramming bằng **số thật đã chạy** cho ý tưởng của người đó (luật `/app-reddit`)
- [ ] **Indie Hackers / Discord indie:** cùng lời mời như X
- [ ] Mỗi báo cáo gửi đi kèm 1 ảnh chụp kết quả (xin phép dùng lại) + 1 dòng mời mua PRO, link `?ref=report`

### 1.3 Danh sách 50 người chào trực tiếp (ngày 3–14)

| Nguồn | Tìm ai |
|---|---|
| Reddit | người vừa đăng "what app should I build" / "idea validation" trong 30 ngày |
| X | người tweet "building with Claude Code / vibe coding my first app" |
| Indie Hackers | bài "looking for app ideas", "how did you validate your idea" |
| Người dùng GummySearch | GummySearch đóng 01/12 — người hỏi "GummySearch alternative" |

- [ ] Lập file 50 người: tên · link · ý tưởng của họ · ngày chào · trả lời · đơn
- [ ] Mỗi tin chào **cá nhân**: nhắc đúng ý tưởng của họ + 1 con số đã chạy sẵn, không dán mẫu y nguyên
- [ ] Chào đủ 50 người

**Giả định để đặt mục tiêu:** 50 người chào → ~15 trả lời → ~5 đơn · 20 báo cáo → ~3 đơn · 9 người đã tải → ~2 đơn. Cộng ≈ 10 đơn.

### 1.4 Ghi lại câu khách nói

- [ ] Mọi câu khách nói (khen, chê, hỏi, lý do không mua) ghi **nguyên văn** vào file voice-of-customer
- [ ] Câu được nhắc ≥ 3 lần → sửa landing / app

### Luật dừng ngày 14

- **≥ 10 đơn:** câu chào đúng → sang tầng 2 với đúng câu đó.
- **3–9 đơn:** giữ tầng 1 thêm 7 ngày, đổi góc câu chào theo câu khách nói.
- **Nhiều người nhận báo cáo, 0 đơn:** giá trị nằm ở báo cáo, không phải app → cân nhắc bán báo cáo làm sẵn theo từng niche (Tu quyết giá), hoặc cho Free 1 brief đầy đủ.
- **Ít người trả lời:** người ta chưa cần "kiểm ý tưởng" lúc này → đổi người nhắm sang dân Claude Code đang build (góc "spec cho AI").

## Tầng 2 — Chào mời có hệ thống (tuần 3–6)

Chỉ khi tầng 1 có đơn. Đem câu chào đã chứng minh tới nhiều người cùng lúc. Mọi link có `?ref=<kênh>`.

- [ ] **Reddit launch:** bài r/SideProject rồi r/ClaudeCode (sửa theo câu khách nói), cách nhau ≥ 2 ngày, ở lại trả lời 2 giờ đầu — Tu đăng, Claude soạn
- [ ] **Reddit số thật:** r/microsaas / r/indiehackers "X lượt tải, Y đơn sau 3 tuần — cái gì hiệu quả" (chỉ khi có số)
- [ ] **X hằng ngày:** 1 bài "mổ xẻ niche" lấy từ báo cáo tầng 1 + 10 reply vào người làm app — Claude soạn, Tu đăng
- [ ] **Danh bạ:** 5 trang danh bạ + 5 thư trong gói "GummySearch alternatives"; thêm Product Hunt / Uneed / Fazier khi có ≥ 5 câu khen thật — Tu tự đăng
- [ ] **Affiliate:** mời 10 người làm nội dung indie / Claude Code (YouTube, newsletter) dùng PRO miễn phí + link affiliate 30 % — Claude soạn danh sách + thư, Tu gửi
- [ ] **Newsletter trả tiền:** chỉ khi affiliate không ai nhận — Tu quyết tiền

**Luật dừng tuần 6:** kênh nào 0 đơn sau 2 lần thử → bỏ. Kênh nào ra đơn → giữ, chuyển sang tự động ở tầng 3.

## Tầng 3 — Tự động hoá (tuần 5–10)

Biến các bước làm tay thành thứ tự chạy, để mỗi lượt tải tự đi tới đơn mà không cần Tu nhắn tin.

- [ ] **3.1 Chuỗi email sau khi tải** (EmailOctopus): ngày 0 cách chạy niche đầu tiên · ngày 2 báo cáo mẫu thật · ngày 5 "brief cho Claude Code" · ngày 9 câu khách nói + nút mua · ngày 14 hỏi vì sao chưa mua — Claude viết, Tu dán
- [ ] **3.2 Nhắc trong app:** còn 3 lượt Free → thẻ "PRO = không giới hạn"; hết lượt → trang mua có ảnh brief mẫu — Claude code
- [ ] **3.3 Chia sẻ báo cáo:** nút "Gửi báo cáo này cho bạn bè" (xuất .md có dòng "Made with ShotMatic" + link `?ref=share`) — Claude code
- [ ] **3.4 Affiliate tự chạy:** trang `/affiliates` công khai trên landing — Claude làm trang, Tu bật trong Lemon Squeezy
- [ ] **3.5 Bảng số tuần:** script đọc lượt tải (GitHub), đơn (Lemon Squeezy), email (EmailOctopus) → 1 bảng — Claude viết script
- [ ] **3.6 Hàng chờ bài X** 2 tuần một lần từ dữ liệu niche thật, Tu chỉ duyệt + đăng / hẹn giờ — Claude

**Xong khi:** một người lạ tải app → nhận đủ chuỗi email → mua, mà Tu không chạm tay. Đo: % lượt tải thành đơn trong 30 ngày.

## Tầng 4 — Traffic thụ động (tháng 2–6, chạy nền từ tuần 3)

Người tìm trên Google / ChatGPT / Perplexity tự tìm thấy ShotMatic. Chậm (3–6 tháng mới thấy), nên bắt đầu sớm nhưng
không trông vào nó để có 10 đơn đầu.

- [ ] **4.1 Sửa lỗi kỹ thuật SEO:** robots.txt Cloudflare chặn bot AI (**Tu** tắt Managed robots.txt), llms.txt còn ghi "private testing", `lang="en"`, JSON-LD có offer $39.99, sitemap
- [ ] **4.2 Trang chủ đúng từ khoá** người ta gõ: "app idea validation", "App Store keyword research"
- [ ] **4.3 Blog 3 bài/tuần:** mỗi bài 1 nỗi đau + số tự đo + dẫn về Download (skill `/shotmatic-blog`)
- [ ] **4.4 Công cụ miễn phí trên web:** nhập 1 keyword → 3 số (số đối thủ, sao trung vị, xu hướng) + "báo cáo đủ trong app" → email
- [ ] **4.5 Trang báo cáo niche thật** từ báo cáo tầng 1 (đã xin phép), mỗi trang số thật + ngày đo, không sinh hàng loạt trang mỏng — 2/tuần
- [ ] **4.6 GEO:** đo hằng tháng 20 câu hỏi xem AI có nhắc ShotMatic không (skill `/app-geo`)
- [ ] **4.7 Video:** 1 demo + 4 shorts từ bản quay app thật, đăng YouTube + gắn landing
- [ ] **4.8 Backlink** từ danh bạ tầng 2 + bài khách mời trên blog indie

**Đo:** impressions + click Search Console (Tu cần đặt lại khoá Google), lượt Download từ /blog, email từ công cụ miễn phí,
đơn có `ref=blog` / `ref=tool`.

## Lịch gộp

| Khi | Tầng | Kết quả đếm được |
|---|---|---|
| Ngày 0–1 | 0 | 1.1.0 live, nút mua trên app + landing, 1 đơn test |
| Ngày 1–14 | 1 | 9 thư tay, 20 báo cáo miễn phí, 50 người chào, **mục tiêu 10 đơn** |
| Tuần 3 | 4.1 + 4.2 chạy nền | SEO kỹ thuật sạch |
| Tuần 3–6 | 2 | 2 bài launch Reddit, X hằng ngày, 10 danh bạ, 10 affiliate được mời |
| Tuần 5–10 | 3 | chuỗi email + nhắc trong app + bảng số tuần tự chạy |
| Tháng 2–6 | 4 | 3 bài/tuần, 1 công cụ miễn phí, trang báo cáo niche, đo GEO hằng tháng |

## Việc chỉ Tu làm được

Claude không đăng nhập store, không trả tiền, không gửi thư / đăng bài thay.

1. Bấm Publish release, mua test, bật Affiliates trong Lemon Squeezy.
2. Gửi thư, đăng bài Reddit / X / danh bạ, trả lời comment.
3. Tắt Managed robots.txt trên Cloudflare; đặt lại khoá Google cho Search Console.
4. Mọi quyết định giá: giảm giá founding, bán báo cáo lẻ, tài trợ newsletter.
