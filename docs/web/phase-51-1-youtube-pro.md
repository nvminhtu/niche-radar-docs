# Phase 51.1 · YouTube Research Pro

> Nâng trang YouTube theo cách các tool YouTube hàng đầu đang làm (vidIQ, 1of10, OutlierKit, TubeLab, NexLev…):
> **video vượt kênh tính theo chính kênh đó** thay vì chia cho số sub, **video thắng trong 12 tháng**, **xu hướng tìm trên
> YouTube**, **kênh mới đang lên**, **tín hiệu cho app** (người xem tìm app / đang tự chế bằng Notion, Excel), một
> **điểm Cầu + Chỗ** có giải thích, và **tuyến MCP** để đem số lượt tìm của vidIQ / OutlierKit / TubeLab về tool.
> Lớp không AI, không key vẫn chạy đủ một mình.

<span class="chip chip--done">Xong 2026-11-06 · chưa thử với MCP thật</span>

## 1 · Các tool YouTube đang làm gì (đọc 2026-11-06)

Phần lớn trang so sánh là **trang marketing của chính đối thủ** (OutlierKit viết về vidIQ, 1of10 viết về OutlierKit…).
Giá và số tool dưới đây lấy từ trang của chính hãng khi có, còn lại ghi rõ là bên thứ 3 nói — kiểm lại trước khi mua.

**vidIQ** — bộ SEO cho kênh (keyword, điểm cạnh tranh, outlier, trending, ý tưởng hằng ngày).

- MCP `https://mcp.vidiq.com/mcp`: trang chính hãng ghi 52 tool (46 lõi + 6 tiện ích), "có ở mọi gói, kể cả Free",
  đa số tool 5 credit / lần. Đăng nhập OAuth hoặc **API key chỉ đọc**. Không tốn quota YouTube Data API.
- Có cả tool **sửa video / trả lời comment** (cần duyệt) và tool tạo nội dung → mình chỉ dùng tool đọc.
- Free 150 credit / tháng (trang giá 2026-11-02) ≈ 30 lần gọi.

**TubeBuddy** — extension SEO + A/B thumbnail + sửa hàng loạt. Keyword Explorer chấm điểm từ lượt tìm ước tính,
độ cạnh tranh và mức tối ưu của video top. **Không có MCP / API công khai.**

**1of10** — extension hiện huy hiệu **"× lần"** (view ÷ view trung bình của kênh) ngay trên trang YouTube; swipe file,
AI ý tưởng. Hãng khuyên lấy trung bình **10–20 video gần nhất**, không lấy cả đời kênh. **Không có MCP / API.**

**ViewStats (MrBeast)** — Pro 49,99 USD/tháng: công cụ Outliers, đối thủ, tìm thumbnail, A/B. Thiên về thumbnail +
phân tích kênh. **Không có MCP / API.**

**OutlierKit** — outlier tính theo nền của chính kênh, tìm theo nghĩa, **lượt tìm keyword theo tháng**, kênh giống kênh.

- MCP `https://outlierkit.com/mcp` (OAuth 2.1, cần gói trả phí hoặc dùng thử), 10 tool chỉ đọc:
  `outliers_search` 2 · `outliers_refresh` 10 · `channels_search` / `channels_similar` / `channels_get` / `channels_videos` 5 ·
  `videos_get` / `videos_transcript` / `videos_comments` 2 · `keywords_research` 2 credit (có lượt tìm / tháng).
- Có REST API (`/api-docs`).

**TubeLab** — outlier theo keyword, kênh tương tự, **mẫu tiêu đề đang thắng** (trending formats).

- MCP `https://public-api.tubelab.net/mcp`: OAuth **hoặc API key Bearer** (dùng được cho app / agent tự viết).
- 12 tool, 7 tool **miễn phí**: `get_channel`, `get_channel_videos`, `get_channel_shorts`, `get_video`,
  **`get_video_transcript`**, `get_video_comments`, `get_credits_balance`. Tốn credit: `search_outliers` 2,
  `search_related_outliers` 2, `search_trending_formats` 1, `search_channels` 5, `search_related_channels` 5.
- Có REST API + webhook + file skill có sẵn lệnh curl.
- **Đáng chú ý:** phụ đề miễn phí — đúng chỗ YouTube.js và yt-dlp đang hỏng (đo ở Backlog 27).

**NexLev** — tìm niche cho kênh "faceless": lọc kênh theo sub / view / đã bật kiếm tiền, **ước RPM**, extension.
Bên thứ 3 ghi có MCP 60+ tool, "miễn phí tạm thời", quota theo ngày — **chưa kiểm trên trang chính hãng**.

**Spotter Studio** — Outlier Index + Brainstorm (tiêu đề, thumbnail, hook), nhắm kênh lớn. **Subscribr** — từ ý tưởng
ra kịch bản. Cả hai không có MCP công khai.

**Social Blade** — số sub / view theo ngày, có REST Business API trả trước, không MCP.

### Cách họ tính (gom lại)

- **Video vượt kênh (outlier)** = view của video ÷ **nền của chính kênh** (trung bình hoặc trung vị 10–30 video gần nhất).
  Không chia cho số sub — kênh nhiều sub cũ mà nay ít view sẽ làm sai. Niche Radar hiện chia cho sub → **phải đổi**.
- **Lượt tìm keyword YouTube:** YouTube không công bố. Mọi tool đều **ước** (lượt tìm Google + clickstream + xu hướng
  YouTube), mỗi tool một số khác nhau. Không có nguồn miễn phí cho số tuyệt đối.
- **Độ cạnh tranh:** số kết quả, độ to của video / kênh top, và mức "tối ưu" (tiêu đề có đúng keyword không).
- **Còn sống không:** video top **đăng gần đây** còn hút view không, kênh **mới mở** có thắng không (NexLev, OutlierKit).
- **Mẫu tiêu đề / packaging:** gom tiêu đề của video vượt kênh thành mẫu ("best N apps", "I tried…", "how to…").

## 2 · MCP dùng được

- **vidIQ** — nối: Claude connector (OAuth) hoặc API key chỉ đọc · tiền: gói Free có, ~5 credit / lần ·
  cho mình: `keyword_research` (lượt tìm + cạnh tranh), `outliers`, `trending_videos`
- **OutlierKit** — nối: Claude connector (OAuth 2.1) · tiền: gói trả phí hoặc dùng thử, 2–10 credit ·
  cho mình: `keywords_research` (lượt tìm / tháng), `outliers_search`, `channels_similar`
- **TubeLab** — nối: OAuth hoặc API key Bearer · tiền: 7 tool miễn phí, outlier 2 credit ·
  cho mình: **phụ đề + comment miễn phí**, `search_outliers`, `search_trending_formats`
- **NexLev** — nối: Claude connector (bên thứ 3 nói) · tiền: chưa kiểm · cho mình: lọc kênh đã kiếm tiền, RPM — chưa kiểm
- **MCP cộng đồng** (`kirbah/mcp-youtube`, Bangermap…) — nối: chạy trên máy + key YouTube Data API ·
  tiền: 0 đ nhưng quota 10.000 đơn vị / ngày, 1 lần tìm = 100 · cho mình: tìm video, số kênh, outlier theo sub; không có lượt tìm
- **Apify** (các actor YouTube) — nối: `APIFY_TOKEN` · tiền: ~0,1–2 USD / 1.000 kết quả (trang actor 2026-11-06) ·
  cho mình: cào hàng loạt khi YouTube.js gãy

**Chọn:** giữ đúng luật Phase 51 — app **không giữ key** của bên thứ 3 ở bản này. Số MCP đi theo **tuyến job**:
app xuất job → phiên Claude của anh đã nối vidIQ / OutlierKit / TubeLab chạy skill `youtube-demand` → trả 1 khối JSON →
dán vào trang YouTube → hiện **cột riêng, ghi nguồn + ngày**, không trộn vào điểm. Phiên này của Claude Code đã có
connector vidIQ nhưng **chưa đăng nhập** (cần `/mcp` → vidIQ) nên số credit thật vẫn `chưa đo`.

## 3 · Đo thật trên máy (2026-11-06, `youtubei.js` 18.3.0, niche `habit tracker`, `lang=en` `location=US`)

- **Tìm + lọc:** `upload_date=year` + `prioritize=popularity` chạy — trả 20 video đăng trong 12 tháng, xếp theo view
  (video đầu 2.248.639 view, đăng 2 tháng trước; video thứ 10: 104.501 view). Tham số `sort_by` không có trong
  `youtubei.js` 18.3.0 — truyền vào thì bị bỏ qua, ra thứ tự "liên quan". Mỗi lần tìm 0,4–1 giây.
- **Số kết quả** (`estimated_results`): 4.023.462 kết quả mọi lúc · **757.519 trong 12 tháng**. YouTube làm tròn / ước,
  chỉ dùng để so giữa các niche.
- **Lọc độ dài:** giá trị đúng là `under_three_mins` / `three_to_twenty_mins` / `over_twenty_mins`; có cả `type: 'shorts'`. Chưa dùng ở bản này.
- **Video gần nhất của kênh** (`getChannel` → `getVideos`): 30 video / trang, ~0,2 giây; mỗi video có view dạng
  "22K" + "2d ago" → đủ tính **nền của kênh**. `getShorts` cũng chạy (48 Shorts). Cả 3 request (kênh + About + video)
  mất 0,6–0,8 giây / kênh (3 kênh đo).
- **Trang About** (`getAbout`): có `joined_date`, `subscriber_count`, `view_count`, `country` → biết **kênh mới**.
- **Tag video** (`getBasicInfo`): chạy (10 tag đầu của 1 video review app). Chưa dùng ở bản này.
- **Google Trends · YouTube Search** (`property: 'youtube'`): chạy, 53 điểm tuần cho 12 tháng; `habit tracker` trung bình 23
  (YouTube) so với 29 (Web) cùng khung. Gọi `relatedQueries` ngay sau đó bị chặn (trả HTML) → chỉ gọi 1 lần / lượt, qua nhịp 4 giây.

## 4 · Lấy gì về Niche Radar

Một cột, từ trên xuống, theo thứ tự hiện trên trang YouTube:

1. **Điểm Cầu + Chỗ (0–100 mỗi điểm)** cạnh tên keyword, bấm xem vì sao — giống điểm keyword của vidIQ / TubeBuddy
   nhưng **mỗi phần ghi rõ số gốc**. Ngưỡng là quy ước của Niche Radar, không phải số đo.
2. **Ô số:** kết quả YouTube (mọi lúc · 12 tháng) · view trung vị video 12 tháng · kênh nhỏ thắng · kênh mới thắng ·
   YouTube Trends 12 tháng (lên / ngang / xuống).
3. **Tín hiệu cho app** (thứ các tool YouTube không làm vì họ phục vụ người làm video):
   - **Người xem tìm app:** % video top có tiêu đề kiểu "best … apps", "… app review", "… vs …".
   - **Đang tự chế:** gợi ý + tiêu đề có Notion / Excel / Google Sheets / template / printable / journal → người ta đang
     tự ráp công cụ = chỗ cho một app gọn hơn.
   - **Mẫu tiêu đề thắng:** gom tiêu đề vào 6 mẫu (danh sách "best / top", hướng dẫn, review / so sánh, trải nghiệm
   "I tried", setup / template, có năm) → mỗi mẫu bao nhiêu video, bao nhiêu video vượt kênh.
4. **Keyword YouTube:** thêm cột YouTube Trends (trung bình + hướng) và cột MCP (lượt tìm, cạnh tranh — khi đã dán).
5. **Video thắng trong 12 tháng:** top 20 video đăng trong năm của keyword gốc, xếp theo view.
6. **Top video:** cột chính đổi thành **× kênh** (view ÷ trung vị video gần nhất của kênh); view ÷ sub để cột phụ.
7. **Kênh trong niche:** sub · view trung vị video gần nhất · số video vượt kênh · ngày mở kênh (nhãn **Kênh mới** khi < 12 tháng).
8. **Người xem nói gì** (giữ như Phase 52).
9. **Số từ MCP:** nút chép job + ô dán kết quả JSON.

Nối ra ngoài trang YouTube:

- Tool MCP `get_youtube` trả thêm điểm, video 12 tháng, kênh, tín hiệu app, YouTube Trends, số MCP đã dán.
- Skill `youtube-demand`: lớp 2 nhận vidIQ **hoặc** OutlierKit **hoặc** TubeLab (tool nào phiên có), lấy phụ đề qua
  TubeLab khi có, trả đúng khuôn JSON mà trang YouTube nhận.
- **So sánh niche:** hàng YouTube (đang "sắp có") lấy Cầu / Chỗ của lần tra YouTube mới nhất cùng keyword gốc.

## 5 · Cách chấm (quy ước, sửa được ở `web/src/lib/youtube-score.ts`)

**Cầu (0–100)** — người xem còn tìm và còn xem chủ đề này không:

- 60 điểm · view trung vị của 20 video thắng trong 12 tháng (keyword gốc), thang log: 100 view → 0 · 1.000 → 20 · 10.000 → 40 · ≥ 100.000 → 60
- 25 điểm · YouTube Trends 12 tháng của keyword gốc: lên 25 · ngang 15 · xuống 5 · ít dữ liệu 8 (không có số → chia lại trọng số)
- 15 điểm · số gợi ý YouTube (≥ 10 gợi ý = đủ 15)
- Nhãn: ≥ 60 **Cầu mạnh** · 35–59 **Có cầu** · < 35 **Cầu yếu**

**Chỗ (0–100)** — người mới còn chen vào được không:

- 40 điểm · số video vượt kênh (≥ 3× nền kênh) của kênh < 100K sub (≥ 5 video = đủ)
- 25 điểm · phần video top keyword gốc **không** thuộc kênh ≥ 1M sub
- 15 điểm · số kênh mở < 12 tháng có video vượt kênh (≥ 2 kênh = đủ)
- 20 điểm · phần tiêu đề top **không** chứa đủ chữ của keyword (ít người tối ưu = dễ chen)
- Nhãn: ≥ 60 **Còn chỗ** · 35–59 **Lẫn lộn** · < 35 **Đông** · keyword gốc < 5 video → **Chưa đủ dữ liệu**

Lượt tra cũ (trước Phase 51.1) không có số mới → giữ nhãn cũ, nhắc "Tra lại để có điểm mới".

## 6 · Các mốc

**M1 · Collector** — tìm 12 tháng theo view, số kết quả, video gần nhất + About của kênh (1 nhịp / kênh), YouTube Trends.

- File: `web/src/collectors/youtube.ts`, `web/src/lib/trends-deep.ts`
- Test: `web/tests/social.test.ts` (client giả, không gọi mạng)

**M2 · Chấm điểm** — Cầu + Chỗ, tín hiệu app, mẫu tiêu đề (hàm thuần).

- File: `web/src/lib/youtube-score.ts` (mới), `web/src/lib/social.ts`
- Test: `web/tests/youtube-score.test.ts` (mới)

**M3 · Giao diện** — tách `YoutubeResult` ra file riêng, thêm các khối theo mục 4.

- File: `web/src/client/YoutubeResult.tsx` (mới), `web/src/client/social-ui.tsx` (mới, phần dùng chung), `web/src/client/SocialPage.tsx`
- Soát: typecheck, trang 960px + 1340px, Sáng + Tối

**M4 · Tuyến MCP** — job cho Claude + dán JSON → cột riêng có nguồn + ngày.

- File: `web/src/lib/youtube-mcp.ts` (mới), `web/src/server/social-api.ts`
- Test: `web/tests/youtube-mcp.test.ts` (mới)

**M5 · AI đọc số mới** — `get_youtube` + skill `youtube-demand` nhận vidIQ / OutlierKit / TubeLab.

- File: `web/src/lib/social.ts`, `web/src/lib/ai/ai-dir.ts`
- Test: `web/tests/youtube-skill.test.ts`

**M6 · So sánh niche** — hàng YouTube có số Cầu / Chỗ.

- File: `web/src/lib/compare-niche.ts`, `web/src/client/ComparePage.tsx`, `web/src/server/social-api.ts`
- Test: `web/tests/compare-niche.test.ts`

**M7 · Tài liệu** — trang này, Phase 51, CHANGELOG, `web/src/lib/features.ts`. Kiểm: `npm run docs:build`.

Thời gian một lượt tra tăng từ ~30 giây lên khoảng 45–60 giây (thêm 1 lần tìm, 15 kênh × 3 request trong 1 nhịp, 1 lần
Trends) — đo lại khi xong, ghi vào mục "Đã làm".

<div class="box box--rules" markdown>
**Luật**

- Không key, không AI vẫn chạy đủ M1–M3. MCP + Chrome chỉ ở phiên Claude của người dùng
- Số MCP là **ước tính bên thứ 3**: cột riêng, ghi tên nguồn + ngày, không cộng vào điểm Cầu / Chỗ
- Không dùng tool sửa video / trả lời comment / tạo nội dung của MCP. Không tạo tài khoản, không trả phí thay người dùng
- Gọi thưa như Phase 51 (nhịp chung 800 ms, Trends 4 giây), bị chặn → ghi lỗi bước đó, các bước khác vẫn chạy
- Mỗi ngưỡng ghi trong code là quy ước; giao diện ghi "quy ước của Niche Radar" ở chỗ giải thích điểm
</div>

<div class="box box--star" markdown>
**Xong khi**

- 1 niche thật tra lại có đủ: điểm Cầu + Chỗ, video 12 tháng, × kênh, kênh mới, tín hiệu app, YouTube Trends
- Dán được 1 khối JSON MCP (mẫu) → cột lượt tìm hiện có nguồn + ngày
- `get_youtube` trả số mới; So sánh niche có hàng YouTube
- `npm run check` xanh, `npm run docs:build` xanh, screenshot 960px + 1340px đã xem
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Ước RPM / doanh thu kênh (NexLev làm) — không có số đo
- Gọi thẳng API vidIQ / OutlierKit / TubeLab từ app bằng key
- Tag video (`getBasicInfo`), Shorts riêng, kênh tương tự — để sau khi bản này chạy ổn
- Tải video, đọc phụ đề trong app (vẫn hỏng — đi qua TubeLab trong phiên Claude)
</div>

## 7 · Đã làm (2026-11-06)

- **Đo 1 lượt tra thật** (`habit tracker`, `force`, không cache): **25,2 giây**, nhanh hơn ước tính 45–60 giây; không lỗi bước nào.
  Kết quả: 71 video, 20 video trong 12 tháng, 15 kênh, 300 comment, YouTube Trends cho 5 keyword, Cầu **80** · Chỗ **69**.
- **YouTube Trends:** 1 / 5 keyword có xu hướng (`habit tracker` −41 %, trung bình 26/100). 4 keyword dài còn lại trung bình 0–1/100
  nên hiện `n/a`, không tính xu hướng từ số quá thưa.
- **Soát giao diện:** 1340px nền sáng, 960px nền tối: cả trang không cuộn ngang; bảng 6–7 cột cuộn trong khung, cột đầu dính.
- **Dán JSON MCP:** dán 1 khối mẫu tự viết → nhận 1 keyword, điểm Cầu không đổi; dán chữ không phải JSON → báo lỗi; nút xoá xoá được.
- **Đo lại 2026-11-07** (`habit tracker`, `force`): **24,2 giây**, không lỗi. 69 video, 20 video trong 12 tháng, 15 kênh, 300 comment,
  4,03 triệu kết quả YouTube; Trends `habit tracker` −42 %. Cầu **80** (60 + 5 + 15) · Chỗ **78** (40 + 21 + 8 + 9) — Chỗ khác lần đo
  trước vì danh sách video đổi theo ngày.
- **Soát giao diện 2026-11-07:** đủ 4 cỡ (960 / 1340px × sáng / tối): cả trang không cuộn ngang. Sửa thanh nhảy mục (dùng chung với
  Amazon · Google Maps): bấm 1 mục thì sáng đúng mục đó — trước sáng nhầm mục ở trên vì ngưỡng cứng 140px trong khi phần dừng ở
  208px (scroll-padding 80 + scroll-margin 128). Logic ở `web/src/lib/active-section.ts`, test `web/tests/active-section.test.ts`.
- **Bản tiếng Việt:** không soát được trong trình duyệt — giao diện hiện luôn chạy tiếng Anh, không có ô chọn ngôn ngữ.
- **Chưa làm:** chạy job với MCP thật (vidIQ cần đăng nhập, số credit chưa đo).

Liên quan: [Phase 51](phase-51-youtube-search.md) · [Phase 52](phase-52-youtube-ai.md) ·
[Backlog 27](phase-backlog-27-youtube-chrome-skill.md)

Nguồn đã đọc (2026-11-06): [vidIQ MCP](https://vidiq.com/mcp/) · [OutlierKit MCP docs](https://outlierkit.com/mcp/docs) ·
[TubeLab MCP](https://tubelab.net/docs/api/mcp-server) · [So sánh MCP YouTube (OutlierKit viết)](https://outlierkit.com/resources/youtube-mcp-servers/) ·
[Cách tính outlier của 1of10](https://1of10.com/blog/viral-youtube-video-ideas-outlier-method/) ·
[ViewStats Pro](https://viewstats.zendesk.com/hc/en-us/sections/22950925723035-Viewstats-Pro) ·
[YouTube bỏ trang Trending (9to5Google)](https://9to5google.com/2025/07/10/youtube-trending-page-removal/) ·
[Ahrefs: công cụ keyword YouTube](https://ahrefs.com/blog/youtube-keyword-tools/)
