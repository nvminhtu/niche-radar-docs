# 7 · Audit kênh YouTube

> Plan 2 · mục 7. Thêm tab **Audit kênh** vào trang YouTube. Anh dán 1 link kênh, 1 @handle hoặc 1 channel ID, tool trả về:
> kênh đăng đều không, view nền bao nhiêu, video nào vượt kênh và video nào tụt, kiểu tiêu đề / độ dài / Shorts nào đang ăn,
> người xem đang hỏi gì, kênh đứng ở đâu so với 3–5 đối thủ cùng niche. Cuối cùng AI đọc lại các số đó, kết luận nên làm gì.
> Lớp không AI, không key vẫn chạy đủ một mình, giống trang YouTube Research Pro (Phase 51.1, tab PLAN 1 · XONG).

<span class="chip chip--todo">Plan 2026-11-11 · bản gọn đã làm 2026-11-13 · phần còn lại để sau Marketing</span>

<div class="box" markdown>
**Bản gọn đã làm 2026-11-13** (anh mở trước Marketing): trang YouTube → thẻ **Soi 1 kênh**.

- **Ô nhập:** link kênh, link 1 video của kênh, `@handle` hoặc channel ID, kèm nước dùng để tìm keyword.
- **Thu số** (máy chủ, không key, ~30 giây): trang kênh + About (sub, số video, tổng view, ngày mở, quốc gia, mô tả, link ngoài) →
  90 video dài gần nhất (tiêu đề, view, tuổi, độ dài) → cụm 2–3 chữ lặp trong tiêu đề → hỏi ô gợi ý YouTube → tìm 10 keyword,
  ghi hạng video đầu tiên của kênh trong top 20 và kênh đang đứng #1.
- **5 khối:** thẻ kênh · sức khoẻ (nhịp đăng, view nền, xu hướng nền, nền ÷ sub, nhãn *đang ngưng*) · keyword + thứ hạng ·
  video vượt kênh / tụt + kiểu tiêu đề · thu nhập quảng cáo ước / tháng.
- **Nút ✦ AI** cạnh tên kênh: gửi toàn bộ số đã thu, AI trả kênh sống nhờ keyword nào, keyword nào còn yếu, 3 góc trống kèm số.
- **Nút *Soi kênh*** cạnh tên kênh trong bảng kênh của *Tìm ý tưởng* và *Kênh trend*. Bấm 1 keyword trong kết quả → điền sẵn ở *Tìm ý tưởng*.
- **Lưu:** chung bảng `social_searches` (câu tra `channel|<nước>|<channel ID>|<tên>`), giữ 7 ngày, chưa có bảng `youtube_channel_audits`.
- **Số đo 2026-11-13** (1 kênh 6,7M sub): đổi link ra ID ~0,2 giây; kênh + About + 3 trang video ~2,4 giây; About có tổng view kênh.
  Video làm chung với kênh khác không mang channel ID của kênh trong kết quả tìm → nhận thêm theo tên kênh.
  Hạng của cùng 1 keyword đổi giữa 2 lượt đo cách nhau vài phút (1 keyword từ #14 ra ngoài top 20).
- **Thu nhập:** view của video đăng dưới 30 ngày × 0,25–4 USD / 1.000 view. Khoảng này là khoảng chung của công cụ ước thu nhập
  [Social Blade](https://socialblade.com/tools) (đọc 2026-11-13); khoảng theo niche: `chưa đo`. Kênh dưới 1.000 sub
  ([ngưỡng YouTube Partner Program](https://support.google.com/youtube/answer/72851), đọc 2026-11-13) thì không ước.
- **Chưa làm:** Shorts + Live, ngày đăng chính xác, comment + tín hiệu app, so đối thủ, phụ đề, MCP, so với lần soi trước,
  thu nhập từ chênh lệch tổng view 2 lần soi, xuất LLM, tool MCP đọc lượt soi, đo trên 5 kênh mẫu của M1.
- Code: `web/src/collectors/youtube-channel.ts`, `web/src/lib/channel-keywords.ts`, `web/src/lib/channel-audit.ts`,
  `web/src/client/YoutubeChannel.tsx`; test `web/tests/channel-audit.test.ts`.
</div>

<div class="box box--danger" markdown>
**Nhắc quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho bán hàng + SEO + GEO
([Marketing](../marketing/index.md)). Plan này viết sẵn, **code sau Marketing**.
</div>

<div class="box box--goal" markdown>
**Đích**

- **1 ô nhập, 1 trang kết quả.** Nhận link `youtube.com/@handle`, `youtube.com/channel/UC…`, link 1 video của kênh, hoặc gõ thẳng `@handle`.
- Trang kết quả trả lời 6 câu hỏi, đọc từ trên xuống:
    1. **Sức khoẻ:** kênh đăng đều không, view nền đang lên hay xuống?
    2. **Vượt kênh / tụt:** video nào làm gấp ≥ 3 lần nền, video nào dưới 0,3 lần?
    3. **Cái gì ăn:** kiểu tiêu đề, độ dài, Shorts hay video dài, chủ đề nào đem view về?
    4. **Người xem nói gì:** comment hỏi gì, xin thêm gì, có hỏi app / đang tự chế bằng Notion, Excel không?
    5. **So đối thủ:** đứng ở đâu so với 3–5 kênh cùng niche?
    6. **Có tiền không:** ước thu nhập quảng cáo / tháng dạng khoảng thấp–cao, có nguồn.
- Mọi con số ghi **đo ngày nào, lấy từ đâu**. Số ước (ví dụ ngày đăng từ chữ "3 weeks ago") ghi chữ **"ước"**.
- **AI đọc lại** số đã đo và kết luận 3 việc nên làm, mỗi việc kèm số làm bằng chứng. Số thiếu thì AI nói thiếu, không đoán.

**Xong khi:** audit chạy thật trên 5 kênh mẫu của M1 (nhỏ < 10K sub, vừa, lớn > 1M, kênh nhiều Shorts, kênh ngưng đăng),
mỗi lần audit ≤ 60 giây, không bị chặn. Trang đứng được ở 960px và 1340px, sáng + tối, English + tiếng Việt.
</div>

## Audit kênh dùng để làm gì trong ShotMatic

**Anh chốt 2026-11-11: việc chính là soi kênh đối thủ.** ShotMatic là tool tìm ý tưởng app, nên audit kênh dùng để:

- **Soi kênh đối thủ / kênh trong niche:** người xem niche đó thích gì, đang hỏi gì, kênh nào đang lên, chỗ nào còn trống
  cho 1 app hoặc 1 kênh mới. Mọi khối, chữ trên màn hình và câu trả lời của AI viết theo góc này.
- Dán link kênh của chính anh vào vẫn chạy (cùng số liệu), nhưng **không làm riêng** phần khuyên "kênh của bạn nên đăng gì".

Từ trang YouTube Research hiện có, mỗi kênh trong bảng kênh có nút **Audit kênh này**. Vậy là nối được 2 tab với nhau:
tìm niche → thấy kênh đáng soi → audit kênh đó.

## Đã có sẵn, dùng lại được

Phần YouTube Research Pro (Phase 51.1, xong 2026-11-06) đã có gần đủ phần lõi. Code ở nhánh `main`:

- `web/src/collectors/youtube.ts` — `youtubei.js` (InnerTube, không key). Hàm `channel(id)` đã lấy: tên, số sub, số video,
  ngày mở kênh, quốc gia, **30 video gần nhất** (view + tuổi video).
- `web/src/lib/youtube-score.ts` — `channelBaseline` (nền = trung vị view video gần nhất, bỏ video < 7 ngày),
  `multiplierOf` (view ÷ nền), `isOutlier` (≥ 3 lần), `titleFormats` (kiểu tiêu đề), `appSignals` (tìm app / tự chế DIY).
- `web/src/lib/youtube-view.ts` — bảng kênh, cờ kênh mới, đếm video vượt kênh của kênh nhỏ.
- Comment (Phase 52): lấy comment 5 video, không lưu tên người comment.
- Phụ đề: đo ngày 2026-11-06 lấy được qua client **IOS / ANDROID** của `youtubei.js` (`getBasicInfo(id, { client: 'IOS' })`
  → `caption_tracks[].base_url` + `fmt=json3`). Client WEB vẫn lỗi 400. InnerTube không chính thức, **đo lại trước khi dùng**.
- Tuyến job MCP (`web/src/lib/youtube-mcp.ts`): app không giữ key vidIQ / OutlierKit / TubeLab, xuất job cho phiên Claude chạy.

## Lấy số thế nào

Không key, không YouTube Data API. Mọi request đi qua `createLimiter` như phần YouTube hiện có.

- **Đổi link / @handle ra channel ID:** `youtubei.js` có hàm đọc URL (`resolveURL`). Link 1 video thì lấy kênh của video đó.
  Cách đọc @handle chính xác: `chưa đo`, M1 thử.
- **Trang kênh + About:** đã có (sub, số video, ngày mở, quốc gia). Thêm: mô tả kênh, link ngoài trong About
  (thường có link app / web của chủ kênh). Đọc được hay không: `chưa đo`.
- **Danh sách video dài:** hiện lấy 30 video. Audit cần **tới 100 video** (hoặc toàn bộ 12 tháng gần nhất), đọc thêm trang
  bằng `getContinuation()`. Thêm cho mỗi video: tiêu đề, độ dài. Bao nhiêu trang thì bị chặn: `chưa đo`.
- **Tab Shorts và Live:** đọc riêng (`getShorts()`, `getLiveStreams()`), để tách Shorts khỏi video dài.
  View Shorts và video dài **không so chung một nền**.
- **Ngày đăng chính xác:** danh sách chỉ ghi "3 weeks ago" → tuổi video chỉ là ước. Muốn đúng ngày (để tính nhịp đăng,
  ngày trong tuần) thì gọi `getBasicInfo` từng video. Chỉ gọi cho **20 video gần nhất**; còn lại dùng tuổi ước, ghi chữ "ước".
- **Comment:** dùng lại Phase 52, lấy comment của 5 video vượt kênh mạnh nhất + 2 video mới nhất.
- **Phụ đề (tuỳ chọn, M6):** lấy phụ đề 3 video vượt kênh mạnh nhất để AI đọc mở bài (hook) và chủ đề. Chỉ khi anh bấm.

## Màn hình

**Anh chốt 2026-11-11: tab trong trang YouTube**, không thêm mục mới trên sidebar.
Trang YouTube có 2 tab: **Tìm niche** (như hiện tại) · **Audit kênh** (mới). Mỗi khối đọc từ trên xuống, 1 cột.

### Khối 1 · Thẻ kênh

- Ảnh đại diện + tên + @handle + link mở kênh.
- Dải số ngắn: sub · số video · tuổi kênh · quốc gia · **thu nhập ước / tháng (khoảng)** · **ngày audit**.
- Nếu đã audit kênh này trước đó: "so với lần trước ngày …" (sub +/−, nền +/−).

### Khối 2 · Sức khoẻ kênh

- **Nhịp đăng:** số video dài / tuần và Shorts / tuần trong 90 ngày gần nhất; khoảng nghỉ dài nhất; ngày gần nhất có video.
  Không đăng > 60 ngày thì gắn nhãn **"đang ngưng"**.
- **Nền view:** trung vị view của video dài gần nhất (dùng lại `channelBaseline`), Shorts có nền riêng.
- **Xu hướng nền:** trung vị 10 video mới nhất so với 10 video trước đó → **đang lên / đi ngang / đang xuống**
  (lệch ±20% mới tính là lên hoặc xuống; ngưỡng chốt sau M1).
- **View / sub:** nền ÷ số sub. Thấp nghĩa là nhiều sub cũ không còn xem.
- Biểu đồ cột nhỏ: view từng video theo thời gian, đường ngang là nền, cột vượt 3 lần tô màu khác.

### Khối 3 · Video vượt kênh và video tụt

- **Bảng vượt kênh:** video ≥ 3 lần nền (dùng lại `isOutlier`), xếp theo số lần. Cột: thumbnail + tiêu đề · số lần ·
  view · tuổi · độ dài · kiểu tiêu đề.
- **Bảng tụt:** video ≤ 0,3 lần nền, để thấy chủ đề / kiểu nào không ăn.
- Video < 7 ngày tuổi chưa xếp loại, để riêng "đang chạy".

### Khối 4 · Cái gì ăn

- **Kiểu tiêu đề:** dùng lại `titleFormats` (số, câu hỏi, so sánh, "how to"…). Mỗi kiểu: số video, số video vượt kênh, view giữa.
- **Độ dài:** chia nhóm (< 1 phút · 1–8 · 8–20 · > 20 phút), view giữa từng nhóm.
- **Shorts hay video dài:** tỉ lệ đăng và nền của mỗi loại.
- **Chữ hay gặp:** cụm 1–3 chữ trong tiêu đề video vượt kênh so với video tụt (bỏ chữ nối, dùng lại cách làm sạch của 51.1).
- **Ngày trong tuần:** chỉ hiện khi có ngày chính xác của ≥ 15 video, vì ước từ "3 weeks ago" thì lệch.

### Khối 5 · Người xem nói gì

- Comment gom theo loại: **câu hỏi** · **xin thêm / xin video** · **khen** · **chê**. Lọc bằng luật chữ trước
  (dấu "?", "can you", "please make"…), AI gom lại sau nếu anh bấm ✦.
- **Tín hiệu app:** dùng lại `appSignals`: comment hỏi "app nào", "có app không", hoặc nói đang dùng Notion / Excel / template.
  Đây là chỗ nối thẳng về việc chính của ShotMatic: bấm 1 tín hiệu → mở *Research 1 keyword* với cụm đó.
- Không lưu tên người comment (luật có sẵn ở Phase 52).

### Khối 6 · So đối thủ

- **Chọn đối thủ:** lấy từ bảng kênh của lần *Tìm niche* gần nhất có kênh này, hoặc anh dán thêm 3–5 link.
  Tự tìm "kênh giống kênh" không có trong InnerTube; muốn có thì đi tuyến MCP TubeLab / OutlierKit (khối 8).
- **Bảng so**, mỗi kênh 1 hàng: sub · nền · xu hướng nền · nhịp đăng / tuần · % video vượt kênh · % Shorts · kiểu tiêu đề ăn nhất ·
  thu nhập ước / tháng (khoảng). Kênh đang audit tô đậm.
- Mỗi đối thủ cũng là 1 lần audit, lưu lại, bấm vào xem đủ.

### Khối 7 · AI đọc lại

- Nút ✦ (dùng `AiMagic` có sẵn). AI chỉ đọc các số trên trang.
- Trả về: **3 góc trống** cho 1 app hoặc 1 kênh mới (ví dụ "người xem hỏi app theo dõi X 14 lần, chưa video nào trả lời",
  "kiểu so sánh 8–20 phút vượt kênh 4 lần mà kênh này ít đăng"), mỗi góc kèm số. Bấm 1 góc → mở *Research 1 keyword*.
- Thiếu số (ít video, chưa có ngày chính xác, chưa lấy comment) thì AI nói rõ thiếu gì và nên bấm lấy thêm gì.
- Không hứa tăng view, không nói chắc về thuật toán YouTube.

### Khối 8 · Thêm số từ MCP (tuỳ chọn)

- Dùng tuyến job MCP của 51.1: xuất job cho phiên Claude có MCP TubeLab (`get_channel`, `get_channel_videos`,
  `search_related_channels`) hoặc OutlierKit (`channels_get`, `channels_similar`), dán JSON trả về.
- Số MCP để **cột riêng, ghi nguồn + ngày**, không cộng vào số tự đo. Công cụ và giá credit: đọc lại trang chính hãng trước khi làm.

## Ước thu nhập kênh (dạng khoảng)

**Anh chốt 2026-11-11: có hiện**, theo cùng luật với Bộ tool KDP: luôn là **khoảng thấp–cao**, có ghi nguồn, có chữ "ước".
Mục đích là xem niche có tiền không, không phải để hứa với người dùng.

- **View / tháng**, tính 2 cách:
    - **Từ lần audit thứ 2:** (tổng view kênh lần này − lần trước) ÷ số ngày giữa 2 lần × 30. Cần 2 lần audit cách nhau
      ít nhất 7 ngày. Cách này đúng hơn vì có cả view của video cũ. Tổng view kênh đọc từ trang About: `chưa đo`, M1 thử.
    - **Lần audit đầu:** cộng view của các video đăng trong 30 ngày gần nhất. Cách này thiếu view của video cũ nên chỉ là
      **mức sàn**, màn hình ghi "thấp hơn thật".
- **Video dài và Shorts tính riêng**, vì tiền / 1.000 view (RPM) của Shorts thấp hơn video dài nhiều.
- **RPM thấp–cao theo nhóm niche:** lấy từ nguồn đã công bố (trang trợ giúp YouTube, báo cáo của bên thứ 3), ghi tên nguồn
  + ngày đọc. Số cụ thể: `chưa đo`, M1 đọc nguồn rồi mới đặt. Không tự đặt số. Niche chưa có trong bảng thì dùng khoảng chung,
  ghi rõ "khoảng chung".
- **Thu nhập / tháng** = view / tháng × RPM thấp ÷ 1.000 … view / tháng × RPM cao ÷ 1.000. Rê vào ô thấy view dùng, cách
  nào, nguồn RPM, ngày.
- **Kênh có thể chưa bật kiếm tiền:** tool không biết chắc. Sub dưới ngưỡng của YouTube Partner Program (đọc lại trang chính
  thức trước khi code) thì ô để "—". Còn lại ghi "nếu đã bật kiếm tiền".
- **Chỉ tính tiền quảng cáo YouTube.** Tài trợ, affiliate, bán khoá học / app không tính. Link ngoài trong About (khối 1)
  là dấu hiệu kênh có nguồn thu khác. Với góc soi đối thủ, đây cũng là chỗ thấy kênh đang bán app gì.
- AI (khối 7) chỉ đọc lại khoảng, không rút ra 1 con số.

## Lưu

- Bảng mới `youtube_channel_audits`: `channel_id · handle · ngày · số tóm tắt (JSON) · số thô (JSON)`.
  Mỗi lần audit 1 dòng, để so lần sau với lần trước.
- Lịch sử audit hiện dưới ô nhập: tên kênh · ngày · nền · xu hướng · nút xoá. Giống *Search history* ở trang chủ.
- Xuất: dùng lại bộ xuất Markdown / LLM (`web/src/lib/export/llm.ts`), thêm phần audit kênh.
- MCP của ShotMatic: thêm tool đọc `get_youtube_channel_audit` để Claude đọc kết quả audit đã lưu (giống `get_youtube`).

## Không lấy được

Các số này chỉ chủ kênh thấy trong YouTube Studio, tool ngoài không có:

- watch time, thời gian xem trung bình, giữ chân người xem (retention);
- CTR thumbnail, lượt hiển thị (impressions), nguồn traffic;
- doanh thu, RPM thật (tool chỉ **ước dạng khoảng**, xem mục *Ước thu nhập kênh*);
- lịch sử sub theo ngày trước lần audit đầu tiên (chỉ có từ các lần ShotMatic tự chụp).

Trang ghi rõ phần này để người dùng không tưởng tool thiếu. Kết nối YouTube Analytics bằng OAuth của chủ kênh: **không làm ở bản đầu**.

## Đối thủ đang làm gì

Đọc lại trang chính hãng trước khi code. Giá và tên tính năng dưới đây theo trang Phase 51.1 mục 1 (đọc 2026-11-06),
phần nào chưa kiểm ghi `chưa đo`.

- **vidIQ:** audit kênh + điểm SEO từng video, outlier, ý tưởng hằng ngày; có MCP. Cần đăng nhập kênh để có số Studio.
- **TubeBuddy:** điểm sức khoẻ kênh, SEO từng video, A/B thumbnail; cần nối kênh. Không MCP / API công khai.
- **Social Blade:** sub / view theo ngày của mọi kênh công khai, ước thu nhập dạng khoảng. Không phân tích nội dung.
- **ViewStats, 1of10, OutlierKit, TubeLab:** video vượt kênh tính theo nền của chính kênh, kênh giống kênh, mẫu tiêu đề thắng.
- **Khác của ShotMatic:** miễn phí, không cần đăng nhập kênh, soi được **kênh của người khác**, nối thẳng từ comment
  sang tra ý tưởng app, AI đọc lại số. Không thay được vidIQ / TubeBuddy cho chủ kênh muốn số Studio.

## Các bước

Thứ tự: đo → lấy số → tính → màn hình → so đối thủ + comment → AI + MCP → so lần trước.

### M1 · Đo trên 5 kênh thật

- **M1 đề xuất 5 kênh, anh duyệt** (anh chốt 2026-11-11). Lấy từ niche app thật: chạy *Tìm niche* trên 1–2 keyword app
  ShotMatic đã tra, chọn trong bảng kênh 5 kênh đủ 5 kiểu: 1 nhỏ (< 10K sub), 1 vừa, 1 lớn (> 1M), 1 nhiều Shorts,
  1 đã ngưng đăng > 60 ngày. Mỗi kênh ghi: link, sub, vì sao chọn. Anh duyệt xong mới đo. Lưu trang thật làm fixture.
- Đo: đọc @handle / link video ra ID; đọc thêm trang tới 100 video mất bao lâu, có bị chặn không; tab Shorts / Live;
  `getBasicInfo` cho 20 video mất bao lâu; About có link ngoài không, có tổng view kênh không.
- Đọc nguồn RPM theo nhóm niche (video dài + Shorts) và ngưỡng YouTube Partner Program, ghi tên nguồn + ngày.
- Chốt từ số đo: trần số video, ngưỡng "đang lên / xuống", 1 lần audit mất bao lâu.

### M2 · Collector `collectChannelAudit`

- `web/src/collectors/youtube.ts`: hàm đọc link / @handle, hàm lấy video có tiêu đề + độ dài + trang tiếp, Shorts, Live,
  ngày chính xác 20 video. Test bằng client giả (kiểu `YtClient` đã có), không gọi mạng.

### M3 · Phần tính `web/src/lib/channel-audit.ts`

- Hàm thuần + test: nhịp đăng, khoảng nghỉ, nền dài / Shorts, xu hướng nền, vượt kênh / tụt, nhóm độ dài, kiểu tiêu đề,
  chữ hay gặp, nhãn "đang ngưng", ước thu nhập dạng khoảng. Dùng lại hàm của `youtube-score.ts`, không chép lại.
- Test các mốc: kênh < 5 video (thiếu số), kênh toàn Shorts, kênh ngưng 90 ngày, video < 7 ngày; thu nhập: lần đầu
  ra mức sàn, lần 2 ra khoảng từ tổng view, sub dưới ngưỡng ra "—".

### M4 · API + tab Audit kênh

- Endpoint audit + lịch sử ở `web/src/server/` (chạy nền như job YouTube hiện có, có tiến độ từng bước).
- Bảng `youtube_channel_audits` + migration.
- Tab *Audit kênh* trên trang YouTube: khối 1–4. Nút *Audit kênh này* trong bảng kênh của tab *Tìm niche*.

### M5 · So đối thủ + comment

- Khối 5 (comment gom loại, tín hiệu app → mở Research 1 keyword) và khối 6 (bảng so 3–5 kênh).

### M6 · AI đọc lại + MCP + xuất

- Khối 7 (✦, prompt chỉ đọc số trên trang), phụ đề 3 video khi bấm, khối 8 (job MCP), tool MCP `get_youtube_channel_audit`,
  phần audit trong bộ xuất LLM.

### M7 · So lần trước + soát + bài blog

- "So với lần trước" ở khối 1, lịch sử audit.
- Soát 960px + 1340px, sáng + tối, English + tiếng Việt; chạy lại trên 5 kênh của M1.
- Khi Marketing mở lại việc viết bài: 1 bài shotmatic.app/blog từ 1 lần audit thật (skill `shotmatic-blog`).

## Rủi ro

- **YouTube đổi InnerTube → bộ đọc hỏng.** Đã gặp nhiều lần (LockupView 2026-11). Fixture test; đọc được 0 video thì báo,
  không im lặng.
- **Bị chặn khi đọc nhiều trang / nhiều kênh.** Giới hạn tốc độ có sẵn, trần 100 video / kênh, đối thủ tối đa 5 kênh / lần.
  M1 đo trước.
- **Ngày đăng ước lệch** (từ "3 weeks ago"). Chỉ dùng ngày chính xác cho nhịp đăng và ngày trong tuần, còn lại ghi "ước".
- **Người dùng tưởng có số Studio.** Mục *Không lấy được* hiện ngay trên trang.
- **Ước thu nhập lệch xa**, nhất là kênh ngoài US hoặc niche hiếm. Luôn là khoảng + nguồn + chữ "ước"; lần đầu ghi rõ là mức sàn.

## Không làm

- Kết nối YouTube Studio / YouTube Analytics bằng OAuth ở bản đầu.
- Ước 1 con số thu nhập duy nhất, hoặc tính cả tiền tài trợ / affiliate.
- Theo dõi kênh tự động theo lịch.
- Sửa video, trả lời comment, đổi tiêu đề thay chủ kênh.
- Lưu tên người comment.

## Cần anh chốt

1. ~~Soi kênh đối thủ hay audit kênh của anh~~ — đã chốt 2026-11-11: **soi kênh đối thủ** là việc chính.
2. ~~Đặt ở đâu~~ — đã chốt 2026-11-11: **tab *Audit kênh* trong trang YouTube**.
3. ~~Ước doanh thu kênh~~ — đã chốt 2026-11-11: **có, dạng khoảng thấp–cao có nguồn** (mục *Ước thu nhập kênh*).
4. ~~5 kênh mẫu cho M1~~ — đã chốt 2026-11-11: **M1 đề xuất từ bảng kênh của *Tìm niche*, anh duyệt**.

Đã chốt đủ 4 câu. Plan chờ Marketing xong để code.
