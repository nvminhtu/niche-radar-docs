# 17 · Soi kênh: Google Trends, keyword dễ hiểu, so 3 kênh

> Plan 2 · mục 17. Thêm 3 thứ cho trang **Soi 1 kênh** (mục 7):
> khối **Google Trends** cho biết kênh có đu trend hay lọt trend không, bảng **keyword dễ hiểu** có tag thật của video,
> và chế độ **So kênh** để soi tối đa 3 kênh một lượt. Phần lớn không cần key. Riêng lượt tìm Google lấy từ Keywords Everywhere thì phải có key và không bắt buộc.

<span class="chip chip--doing">17.1 + 17.2 + 17.4 đã code 2026-11-15, chưa ra bản · 17.3 + 17.5 chờ anh duyệt</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Mục này ghi lại 3 câu anh hỏi ngày 2026-11-15. Chỉ code khi anh chốt.
</div>

## Vì sao làm

Anh hỏi 3 câu (2026-11-15):

1. Soi 1 kênh nên có thêm Google Trends để biết kênh có **lọt vào trend** hay đang **đu trend**, có video nào dính trend,
   và kênh có keyword nào trùng với Google Trends.
2. Thêm kiểu số của **Keywords Everywhere** để biết kênh đang dùng keyword gì, số dễ hiểu, rồi đem keyword đó đi soi tiếp.
3. Có nên **soi nhiều kênh một lượt** (so kênh) không, tối đa bao nhiêu kênh, và sau khi soi thì so những gì.

## Tool khác đang làm gì (đọc 2026-11-15)

- **TubeBuddy:** có Keyword Explorer (điểm keyword, lượt tìm ước tính, độ cạnh tranh) và tab Competitors (kênh nào đang lên hạng cho keyword nào).
  Theo các bài review, audit kênh nằm ở gói đắt nhất. Giá mỗi nguồn nói một khác, `chưa đo` trên trang chính chủ.
- **vidIQ:** có Channel Audit với mục đối thủ, xếp video của đối thủ theo view / giờ, có chọn kỳ 30 / 60 / 90 ngày (gói Boost).
  Theo dõi được 10 kênh ở gói Pro, 30 kênh ở gói Boost (theo review). Có Trend Alerts báo khi một chủ đề đang lên.
- **1of10:** chỉ làm video vượt trội: theo dõi kênh, Niche Explorer, tìm thumbnail / tiêu đề giống nhau, có dùng được trong Claude.
  **Không có keyword, không có trang so kênh.** Gói free theo dõi được 3 kênh.
- **Keywords Everywhere:** trả theo credit, 1 keyword tốn 1 credit. Bản free có widget và danh sách tag.
  Muốn có lượt tìm, CPC, độ cạnh tranh, xu hướng thì phải trả tiền. Có API key.

**Chỗ trống:** chưa tool nào trong số này đặt Google Trends ngay trong trang soi kênh, và chỉ 1of10 có thứ giống so kênh,
mà cũng chỉ là theo dõi chứ không đặt các kênh cạnh nhau. Mục này lấp đúng 2 chỗ đó.

## Đã đo (2026-11-15)

- **Google Trends lọc "YouTube Search" chạy được, không cần key.** `google-trends-api` truyền `property: 'youtube'`.
  Thử `relatedQueries` với "morning routine", nước US, 90 ngày: danh sách Rising khác hẳn bản web.
  Bản YouTube có "early morning routine" +170%, "fall morning routine" +140%. Bản web toàn chữ Breakout, kể cả câu hỏi ChatGPT dài.
- **RSS "Trending now" theo nước chạy được:** `trends.google.com/trending/rss?geo=US` trả 10 chủ đề hôm nay (tên người, trận đấu…).
  Lệnh `dailyTrends` cũ của thư viện và tool `get_trending_searches` trong MCP google-trends đều trả 404.
- **Đọc được tag thật của video:** `youtubei.js` gọi `getBasicInfo` mất khoảng 0,15 giây / video, có `keywords` (tag chủ kênh tự đặt) và chuyên mục.
  Đo trên 1 video. Đọc 30 video liền thì `chưa đo`.
- **Không biết được video nào đang nằm trong tab Trending của YouTube:** YouTube đã bỏ trang này, `FEtrending` trả 400 (đo 2026-11-11, mục 8).
- **Trang API của Keywords Everywhere không đọc tự động được** (trang chạy bằng JS). Vì vậy endpoint, giá, số keyword tối đa mỗi lần gọi,
  và có số riêng cho YouTube hay không đều đang `chưa đo`.

## Đã code 17.1 + 17.2 (2026-11-15)

Anh chốt *Code 17.1 + 17.2* ngày 2026-11-15. Chạy thật trên 4 lượt soi kênh (US), không bị Google chặn lần nào.

- **Thời gian:** soi 1 kênh (đã có đọc tag 30 video) mất 44–46 giây. Đọc Google Trends lần đầu mất 48–88 giây, lâu hơn mức 25–30 giây đã ước,
  vì mỗi lượt Trends cách nhau 4 giây. Đọc lại trong ngày thì gần như tức thì (cache 1 ngày).
- **Khối Trends chạy riêng:** trang kênh hiện ngay, khối Google Trends tự đọc 1 lần cho lượt soi chưa có, rồi lưu vào chính lượt soi đó.
  Hôm sau có nút *Đọc lại Trends hôm nay*. API: `POST /api/social/youtube/channel-trends`.
- **Nút Đem đi soi:** bấm keyword hoặc câu ở *Chỗ trống* sẽ tra ở *Tìm ý tưởng* trên trang YouTube, giống bảng keyword hiện có.
  Chưa làm phần tick nhiều keyword để đem sang trang Soi cơ hội.

Luật thêm sau khi chạy số thật:

- **Tag là tên kênh viết sai cũng bỏ** (lệch tối đa 2 chữ cái). Một kênh thật đặt cả "Ali Abdaal" lẫn "Ali abdal".
- **Tag mặc định chỉ giữ 3.** Tag có ở ≥ 90% video có tag là tag mặc định của cả kênh. Một kênh thật đặt cùng 7 tag cho cả 30 video,
  chiếm hết 10 suất đem đi tìm hạng. Giữ 3 cụm nhiều chữ nhất.
- **Chấm đu trend theo tiêu đề trước, tag sau,** và không chấm theo tag mặc định (tag có ở mọi video không nói lên chủ đề của 1 video).
- **Không chấm keyword quá ít người tìm:** trung vị 12 tháng dưới 5/100. Ở mức trung bình 2/100, nhích từ 2 lên 3 đã vượt ngưỡng,
  khiến 13/14 video bị chấm "đi trước trend".
- **Chỗ trống phải chứa đủ chữ của keyword gốc.** Bỏ câu lạc đề kiểu "babydoll" quanh "notion", "iran news" quanh "ai news".
- **Khối Trends trong câu hỏi ✦ AI chỉ thêm khi còn chỗ** dưới 3.900 ký tự (khung Hỏi AI nhận tối đa 4.000).

Code: `web/src/lib/channel-keywords.ts` (tag), `web/src/lib/channel-trends.ts` (chấm, hàm thuần), `web/src/collectors/channel-trends.ts` (đọc Trends + RSS),
`web/src/client/ChannelTrends.tsx` (giao diện). Test: `web/tests/channel-trends.test.ts`.

## Đã code 17.4 So kênh (2026-11-15)

Anh chốt *Làm 17.4 So kênh* ngày 2026-11-15. Chạy thật trên 3 kênh US: Ali Abdaal, Thomas Frank Explains, Jeff Su (đánh dấu Kênh của tôi).

- **Luồng:** tab thứ 5 *So kênh* trên trang YouTube. Dán 2–3 link, chọn nước, có thể đánh dấu 1 kênh là *Kênh của tôi*.
  Trình duyệt soi lần lượt từng kênh (1 request / kênh, kênh đã soi trong 7 ngày thì dùng lại), rồi gửi id về `POST /api/social/youtube/channel-compare` để gộp thành 1 lượt mở lại được.
- **Trends bản gọn:** kênh chưa đọc Trends hôm nay thì máy đọc 1 lượt hướng keyword (bỏ tên kênh, Rising, Trending now), không ghi vào lượt Soi 1 kênh.
  Kênh đã đọc Trends hôm nay thì dùng lại.
- **Nút ＋ So với kênh khác** ở đầu trang Soi 1 kênh: sang tab So kênh, điền sẵn kênh đang xem làm kênh đầu.
- **Thời gian đo:** 2 kênh đã soi sẵn mất 0–1 giây, kênh mới (Jeff Su) 46 giây, bước gộp 1 giây.
- **Trang kết quả, 1 cột:** thẻ kết luận (nên học theo + dễ chen nhất) → Quy mô → Sức bật → Thu nhập ước → Keyword (chung / chỉ 1 kênh / đối thủ có mà mình chưa có) → Trend → Video mạnh nhất.
  Mỗi kênh 1 màu cố định, mỗi chỉ số 1 hàng thanh. Nút ✦ AI nhận đủ số của các kênh.

Luật thêm sau khi chạy số thật:

- **Bỏ cụm số vô nghĩa:** cụm có số mà chỉ còn tối đa 1 chữ có nghĩa ("10 minutes", "top 5", "learn 80") không đem so. Đo trên Jeff Su: các cụm này lặp trong tiêu đề nhưng không phải chủ đề.
- **Gộp cụm chỉ khác gạch nối:** "claude co-work" và "claude cowork" là 1 keyword.
- **Chỗ trống nhiều đối thủ cùng có lên trước:** "ultimate guide" (2 đối thủ có) đứng trên các cụm chỉ 1 kênh có.
- **3 kênh khác ngách thì không có keyword chung:** trang ghi rõ "không keyword nào chung, so sức bật thôi" thay vì để trống.

Kết quả lượt chạy thật (đọc 2026-11-15, số do tool đo): nên học theo Thomas Frank Explains (view nền ÷ sub 0,215×),
dễ chen nhất cũng là Thomas Frank Explains (302K sub, 18 video vượt kênh). Không keyword nào cả 3 kênh cùng dùng.

Code: `web/src/lib/channel-compare.ts` (hàm thuần), `web/src/lib/social.ts` (`saveChannelCompare`), `web/src/client/YoutubeCompare.tsx` (giao diện).
Test: `web/tests/channel-compare.test.ts`.

## Đã có sẵn, dùng lại

| Có sẵn | Ở đâu | Dùng cho |
|---|---|---|
| Soi 1 kênh: đọc kênh + 90 video, keyword từ tiêu đề, hạng top 20 | `collectors/youtube-channel.ts`, `lib/channel-audit.ts` | nền của cả 3 việc |
| Rút cụm keyword từ tiêu đề | `lib/channel-keywords.ts` | gộp với tag thật |
| Google Trends + nhịp giãn 4 giây | `collectors/trends.ts` (`callTrends`) | thêm `property: 'youtube'` |
| Nhãn Sắp nổ / Đang nổ / Đã nổ | `lib/video-heat.ts`, `client/heat-ui.tsx` | thay cho "video đang trending" |
| Trang Soi cơ hội | `/intel/:id` (mục 10) | đích của nút **Đem đi soi** |
| Tool agent `youtube_channel` + hàng đợi job | `lib/youtube-agent.ts` (mục 15.7) | thêm `youtube_compare` |

## 17.1 · Bảng keyword dễ hiểu (tag thật + tiêu đề)

Hiện bảng keyword chỉ rút cụm chữ từ tiêu đề. Bước này thêm **tag thật** của 30 video gần nhất rồi gộp với cụm từ tiêu đề.

Mỗi keyword là 1 dòng, cột ngắn và có icon:

- **Keyword**
- **Lấy từ:** 🏷 tag · 📝 tiêu đề · cả hai
- **Số video** của kênh dùng keyword này
- **Gợi ý YouTube:** ✓ / ✗ (đã có)
- **Hạng của kênh** trong top 20 tìm kiếm (đã có)
- **Xu hướng trên YouTube:** đường nhỏ 12 tháng + mũi tên ↑ / → / ↓ (lấy ở 17.2)
- **Rising liên quan:** số câu đang lên quanh keyword này (lấy ở 17.2)
- **Lượt tìm Google / tháng** và **CPC:** xám chữ *cần key*, chỉ có số khi làm 17.3
- **Đem đi soi →** mở trang Soi cơ hội với keyword đó, hoặc tick nhiều keyword rồi đem đi một lượt

Phần giải thích dài (tag là gì, vì sao hạng có thể khác khi anh đăng nhập) gập vào ⓘ.

Luật:
- Tag là thứ chủ kênh **muốn được tìm thấy**, không phải keyword thật đem view về (số đó chỉ chủ kênh thấy trong YouTube Studio). Ghi rõ trong ⓘ.
- Tag trùng tên kênh hoặc tên chủ kênh thì gom vào 1 dòng *Tên kênh*, không đem đi tìm hạng.
- Đọc tag đi chung hàng đợi YouTube có sẵn, không gọi dồn.

## 17.2 · Khối Google Trends trong Soi 1 kênh

Một khối mới, nằm dưới bảng keyword. Trả lời 4 câu, mỗi câu là 1 hàng: kết luận ngắn + số + hình.

### Kênh có đu trend không?

- Lấy 5 keyword mạnh nhất của kênh (nhiều video nhất, có gợi ý YouTube), hỏi Trends bản YouTube, 12 tháng, đúng nước của kênh.
- Mỗi video có keyword đó được chấm theo tuần đăng:
  - **🌊 Đu trend:** video đăng trong tuần keyword đang cao hơn 1,5 lần mức trung vị 12 tháng của chính keyword đó.
  - **⏩ Đi trước trend:** video đăng trước, rồi keyword mới vọt lên trong 8 tuần sau.
  - **Không nhãn:** các trường hợp còn lại.
- Kết luận của kênh: *X / 30 video gần nhất đăng lúc keyword đang lên*. Kèm 1 hình: đường Trends có chấm các video của kênh nằm trên đó.
- Ngưỡng 1,5 lần và 8 tuần là quy ước của ShotMatic, sửa được, ghi trong ⓘ.

### Kênh có lọt trend không?

- **Kênh đứng đầu 1 keyword đang lên:** kênh nằm top 3 tìm kiếm YouTube (số đã có) *và* keyword đó có mũi tên ↑. Đây là tín hiệu mạnh nhất, đặt lên đầu.
- **Tên kênh có người tìm:** hỏi Trends bản YouTube với tên kênh. Kênh nhỏ gần như luôn ra 0, khi đó ghi *quá ít người tìm tên kênh* chứ không ghi 0.

### Có video nào đang dính trend?

- Không có tab Trending để đối chiếu (YouTube đã bỏ). Thay bằng: video có nhãn **🔥 Đang nổ** (đã có) *và* keyword của video đang ↑ trên Trends.
- Đối chiếu thêm với **Trending now** hôm nay của nước đó (RSS, 10 chủ đề). Tiêu đề hoặc tag khớp một chủ đề thì gắn **📈 Đang có trên Trending now**.
  Kênh theo ngách hiếm khi khớp. Không khớp thì khối này ẩn đi, không hiện dòng trống.

### Chỗ trống: trend kênh chưa làm

- Lấy Rising (bản YouTube) của 3 keyword mạnh nhất.
- Câu Rising nào **không có video nào** của kênh dùng thì đưa vào danh sách *Chỗ trống*, mỗi câu có nút **Đem đi soi →**.
- Đây là phần dễ cầm đi làm nhất. Nó cũng đi thẳng vào câu ✦ AI gửi đi.

### Chi phí gọi Trends

- 1 lần `interestOverTime` cho 5 keyword (chung 1 thang nên so được với nhau), 3 lần `relatedQueries`, 1 lần tên kênh, 1 lần RSS.
  Ước lúc viết plan là 25–30 giây; **đo thật 2026-11-15 là 48–88 giây** lần đầu. Trang kênh hiện trước, khối Trends hiện sau.
- Lưu theo ngày: soi lại cùng kênh trong ngày thì không gọi Trends lại.
- Trends chặn (429) thì khối ghi *Google Trends đang chặn tạm, thử lại sau* và kèm nút thử lại. Phần còn lại của trang vẫn chạy.

## 17.3 · Lượt tìm Google từ Keywords Everywhere (có key, không bắt buộc)

- Trong Cài đặt có ô **Key Keywords Everywhere**, anh tự dán key của mình vào. Key chỉ lưu trên máy, không gửi đi đâu ngoài Keywords Everywhere.
- Có key thì bảng keyword hiện nút **Lấy lượt tìm Google** cho các keyword đang tick (tối đa 20 cái / lần), và báo trước số credit sẽ tốn.
- Có thêm 3 cột: lượt tìm / tháng, CPC, độ cạnh tranh quảng cáo. Mỗi số có nhãn nguồn + ngày lấy.
- Ghi rõ ngay đầu cột: **đây là lượt tìm trên Google web, không phải trên YouTube**.
- Không có key thì 3 cột này để xám, không có số giả.
- Bước đầu của 17.3 là đo: anh đăng ký hoặc mở trang tài liệu API, mình đọc endpoint, giá, số keyword mỗi lần gọi,
  và xem có số riêng cho YouTube không. Có số riêng cho YouTube thì dùng số đó thay số Google web.
- Đi chung với Phase 7 của mục 10 (nguồn trả phí / có tài khoản): cùng 1 kiểu ô key, cùng nhãn nguồn.

## 17.4 · So kênh (tối đa 3 kênh)

### Vì sao tối đa 3

- **Thời gian:** mỗi kênh tốn khoảng 2,4 giây đọc kênh, cộng 10 lượt tìm để xem hạng, cộng khoảng 25 giây Trends.
  3 kênh mất khoảng **1–1,5 phút**. Lên 4 kênh thì Trends dễ chặn giữa chừng.
- **Đọc được:** phần trùng keyword giữa 3 kênh vẫn nhìn ra. Giữa 4 kênh thì có tới 15 nhóm, rối.
- **Màn hình:** mỗi chỉ số là 1 hàng, 3 thanh ngắn nằm ngang vẫn rõ ở 960px.
- 1of10 bản free cũng dừng ở 3 kênh.

### Luồng

- Thẻ lối vào **So kênh** trên trang YouTube, cạnh thẻ Soi 1 kênh. Dán 2–3 link hoặc @handle.
- Trên trang Soi 1 kênh có thêm nút **＋ So với kênh khác**, mang kênh đang xem sang làm kênh đầu.
- Có thể đánh dấu 1 kênh là **Kênh của tôi** (không bắt buộc). Có đánh dấu thì phần keyword sẽ tính chỗ trống so với kênh đó.
- Kênh nào đã soi trong ngày thì dùng lại số đã lưu, không đọc lại.

### So những gì

Mỗi mục là 1 hàng, chỉ số nằm ngang, chữ giải thích gập vào ⓘ.

1. **Quy mô:** sub, tổng view, số video, tuổi kênh.
2. **Sức bật:** view trung vị 30 video gần nhất, view / sub, tỉ lệ video vượt kênh, số video / tháng.
3. **Thu nhập ước:** dạng khoảng thấp–cao, cùng cách tính với Soi 1 kênh, có nguồn RPM.
4. **Keyword:** xếp từ trên xuống, không chia cột:
   - *Cả 3 kênh cùng dùng*: đây là keyword lõi của ngách.
   - *Chỉ 1 kênh có*, mỗi kênh 1 nhóm.
   - Nếu có Kênh của tôi: *Đối thủ có, mình chưa có*, mỗi keyword có nút **Đem đi soi →**.
5. **Trend:** tỉ lệ video đu trend của từng kênh, số keyword đang ↑, kênh nào đang đứng đầu 1 keyword đang lên.
6. **Video mạnh nhất** của mỗi kênh (× kênh cao nhất trong 90 ngày), mỗi kênh 1 dòng có thumbnail.
7. **Kết luận:**
   - *Nên học theo:* kênh có view trung vị / sub cao nhất.
   - *Dễ chen nhất:* kênh có ít sub nhất mà vẫn có video vượt kênh.
   - Hai luật này là quy ước của ShotMatic, ghi trong ⓘ. Nút ✦ AI nhận đủ số của 3 kênh và chỉ được nói dựa trên số đó.

## 17.5 · Cho agent

- Thêm tool `youtube_compare` (2–3 kênh), chạy nền theo kiểu job của 15.7, trả mã job khi chạy quá 20 giây.
- `youtube_channel` trả thêm khối Trends + tag khi đã có.
- Agent phải ghi nguồn + ngày cho mọi số, không có số thì ghi `chưa đo`.

## Chia việc

1. **17.1** Tag thật + bảng keyword mới + nút Đem đi soi. Có test cho phần gộp tag với tiêu đề.
2. **17.2** Khối Google Trends: `property: 'youtube'`, nhãn 🌊 / ⏩, lọt trend, Trending now, Chỗ trống. Lưu theo ngày. Có test cho phép chấm tuần.
3. **17.4** So kênh 3 kênh, dùng lại 17.1 + 17.2.
4. **17.3** Keywords Everywhere: đo API trước, rồi làm ô key + 3 cột.
5. **17.5** Tool `youtube_compare` cho agent.

Làm xong 17.1 + 17.2 là anh đã thử được trên Soi 1 kênh. 17.4 cần 2 bước đó trước. 17.3 làm được bất kỳ lúc nào sau khi anh có key.

## Cần anh chốt

- **Làm ngay hay sau Marketing?**
- **Số kênh tối đa khi so:** đề xuất 3.
- **Free hay PRO?** Đề xuất: Free có Trends + bảng keyword trong Soi 1 kênh. So kênh thì PRO, hoặc Free được 1 lượt so / ngày.
- **Keywords Everywhere:** anh có muốn mua credit để đo API không, hay bỏ hẳn 17.3 và chỉ dùng số free?
- **Ngưỡng đu trend:** đề xuất 1,5 lần trung vị 12 tháng, nhìn trước 8 tuần.

## Giới hạn

- Google Trends là chỉ số tương đối 0–100, không phải lượt tìm. Keyword nhỏ hay ra 0, khi đó ghi *quá ít người tìm*.
- Không có danh sách Trending chính thức của YouTube, nên "video dính trend" chỉ là ước lượng (Đang nổ + keyword ↑).
- Tag và tiêu đề là thứ kênh **chọn đặt**, không phải keyword thật đem view về.
- Hạng tìm kiếm đo khi không đăng nhập, người xem thật có thể thấy thứ tự khác.
- Kết quả không đăng nhập gần như không có Shorts (đo 2026-11-12), nên mục này hợp với kênh video dài.
- Lượt tìm của Keywords Everywhere (nếu dùng) là lượt tìm Google web, không phải YouTube, trừ khi 17.3 đo ra có số riêng cho YouTube.

## Nguồn

- [TubeBuddy vs vidIQ (2026)](https://www.learningrevolution.net/tubebuddy-vs-vidiq/), đọc 2026-11-15
- [vidIQ · Channel Audit (trang hỗ trợ)](https://support.vidiq.com/en/articles/10141815-channel-audit), đọc 2026-11-15
- [vidIQ vs 1of10](https://vidiq.com/compare/vidiq-vs-1of10/), đọc 2026-11-15
- [vidIQ vs Keywords Everywhere](https://vidiq.com/compare/vidiq-vs-keywords-everywhere/), đọc 2026-11-15
- [1of10 · Features](https://1of10.com/features), đọc 2026-11-15
- [1of10 review (OutlierKit, đối thủ của 1of10)](https://outlierkit.com/resources/1of10-review/), đọc 2026-11-15
- [Keywords Everywhere · giá (toolradar)](https://toolradar.com/tools/keywords-everywhere/pricing), đọc 2026-11-15
- [Google Trends · Trending now RSS (US)](https://trends.google.com/trending/rss?geo=US), đo 2026-11-15
