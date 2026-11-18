# 25 · Học từ AppTweak + Appfigures, giữ chất riêng

> Plan 2 · mục 25. Xem 2 tool ASO lớn đang có gì, chọn **3 thứ nhỏ** đáng học, và chốt **câu định vị** để ShotMatic
> không bị so như "AppTweak bản rẻ".

<span class="chip chip--todo">Viết 2026-11-16 · chờ anh chốt · chưa code</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Phần **25.4 (định vị + trang so sánh)** là việc marketing, làm được ngay. 25.1–25.3 là tính năng, chỉ code khi anh chốt.
</div>

## Vì sao làm

Anh hỏi (2026-11-16): AppTweak, Appfigures đang có tính năng gì, mình có nên học không, và làm sao định vị được chất riêng.

## 2 tool kia đang có gì (tra 2026-11-16)

Tra qua trang giá và trang review bên ngoài. Trang chính của Appfigures chặn bot nên chưa đọc trực tiếp được.
Giá ở các nguồn lệch nhau, chỉ dùng để hình dung.

**AppTweak** dành cho team ASO / marketing có ngân sách:

- Keyword ở hơn 100 nước, có lượt tìm, độ cạnh tranh, **điểm độ khó**.
- Soi đối thủ: metadata, ảnh store, mức hiển thị.
- Ước số tải và doanh thu.
- AI riêng (Atlas) và các agent ASO, Reviews, Reporting, Ads. Có tự chạy Apple Ads.
- **Mới:** theo dõi thương hiệu có được AI (ChatGPT…) nhắc tới không, và AI gợi ý ai thay mình.
- Giá từ khoảng $69–79/tháng. Review hay chê đắt với dev nhỏ.

**Appfigures** dành cho indie đến công ty vừa:

- Ước số tải và doanh thu app khác để so đối thủ, xem thị trường.
- Hạng danh mục và hạng keyword, cập nhật mỗi giờ.
- Báo cáo app của chính mình, **cảnh báo qua Slack**, có API.
- Gói rẻ khoảng $10/tháng. Xem đủ dữ liệu app khác từ khoảng $150/tháng, gói cao hơn $1.000/tháng.

**Điểm chung:** cả 2 phục vụ người **đã có app**, muốn app lên hạng và bán nhiều hơn.

## Học gì, không học gì

| Thứ của họ | Mình làm gì | Vì sao |
|---|---|---|
| Điểm độ khó keyword | **Học** · 25.1 | Mình đã có đủ số, chỉ chưa gom thành 1 con số dễ hiểu |
| Cảnh báo khi đối thủ đổi | **Học bản gọn** · 25.2 | Đã có chụp số 7 / 30 / 90 ngày, chỉ thiếu phần báo |
| AI có nhắc tên app không | **Học bản gọn** · 25.3 | Chính AppTweak vừa thêm. Mình đã làm GEO cho blog nên hiểu việc này |
| Ước số tải / doanh thu chính xác | **Không học** | Cần kho dữ liệu lớn. Giữ quy ước doanh thu dạng khoảng |
| Hạng cập nhật mỗi giờ | **Không học** | Cùng lý do. Người chọn niche không cần số từng giờ |
| Tự chạy Apple Ads, báo cáo app của mình | **Không học** | Việc của người đã có app, không phải khách của mình |

## Đang có gì (đọc code 2026-11-16)

- **Độ đông app store** (`web/src/keyword-engine/types.ts` → `appCompetition`; trang Keyword Intelligence `IntelPage.tsx`):
  tổng rating 5 app đầu App Store, thang log, 5 bậc. Trang đã ghi rõ đây **không phải** độ khó SEO.
- **Độ phổ biến** `popularity_score` 0–100 từ hạng trong ô gợi ý store (Explorer).
- **Nhãn Cầu > cung** `web/src/lib/app-demand-supply.ts` (mục 22.3): có app dưới 1 năm, ≥ 50 rating đang leo top 10.
- **Chụp số project** `web/src/lib/tracking.ts` (Phase 9): mốc 7 / 30 / 90 ngày, so đối thủ vào / rời top 10, rating, giá,
  Trends, điểm v2. Phase 42 đã bỏ tự chạy theo lịch (chốt 2026-10-28).
- **Kệ AI** (Phase 60): mới là plan, chưa code.

## 25.1 · Điểm "Độ khó leo" 0–100

Một con số cho mỗi keyword app: **app mới vào top 10 khó tới đâu**. Gom từ số đã có, **không gọi thêm mạng**.

| Phần | Trọng số | Lấy từ |
|---|---|---|
| Độ đông app store | 50% | `appCompetition` (thang log đã có) |
| Không có app mới leo được | 30% | Nhãn Cầu > cung: có app mới leo thì phần này = 0 |
| Rating trung vị top 10 | 20% | Lượt Research gần nhất |

- Hiện 3 mức: 🟢 dễ (< 35) · 🟡 vừa (35–65) · 🔴 khó (> 65), kèm số. Bấm ⓘ thì thấy 3 phần cộng lại thế nào.
- Hiện ở: trang Keyword, hàng Explorer, thẻ Săn app (mục 24).
- Mục 24 đang có điểm Săn app /100 riêng. Phần "Cung còn chỗ" của mục 24 nên dùng chung hàm của 25.1, để 2 điểm không lệch nhau.
- Keyword chưa Research thì chỉ tính phần độ đông và ghi "ước sơ bộ".
- **Ghi rõ ở ⓘ:** đây là quy ước của ShotMatic, không phải điểm độ khó của AppTweak hay của store.

## 25.2 · Hộp "Đổi gì từ lần trước"

Không chạy theo lịch, vì Phase 42 đã chốt không làm. Chỉ **so khi anh mở project** hoặc bấm Tra lại.

- Đầu trang Project có 1 hộp, tối đa 5 dòng, chỉ hiện thay đổi **đáng chú ý**:
    - app mới vào top 10 (nhất là app dưới 1 năm),
    - đối thủ tụt hoặc tăng ≥ 0,3★,
    - Trends lên hoặc xuống ≥ 30% so với lần chụp trước,
    - Độ khó leo (25.1) đổi mức (🟢 → 🟡…).
- Mỗi dòng có icon và mũi tên, bấm vào thì mở đúng keyword đó.
- Không có gì đáng chú ý thì ghi 1 dòng: "Chưa đổi gì đáng kể từ <ngày>".
- Dùng lại diff trong `tracking.ts`, chỉ thêm luật lọc. Phía YouTube nối vào watchlist mục 15 sau.
- **Không** làm Slack hay email ở bản này.

## 25.3 · AI có nhắc app nào trong niche này (bản gọn của Phase 60)

- Trên trang Research 1 keyword, thêm nút **Hỏi AI**. Nút này gửi 3 câu cố định (vd "best <keyword> app for iPhone")
  tới 1 model mà anh đã cài trong Cài đặt AI.
- Đếm **tên app nào được nhắc** và so với top 10 store:
    - app có trong store mà AI không nhắc → chỗ trống,
    - AI nhắc app đã chết hoặc không còn trên store → chỗ trống lớn hơn.
- Lưu câu hỏi, câu trả lời gốc, model, ngày. Mọi số đều có nguồn.
- Tốn token, nên hiện số token ước trước khi bấm (theo luật Phase 28.15).
- Chỉ 1 model. Hỏi nhiều model một lúc thì để Phase 60.

## 25.4 · Định vị + trang so sánh (marketing, làm được ngay)

**Câu định vị:**

> AppTweak giúp app của bạn lên hạng. ShotMatic giúp bạn **chọn đúng app để làm**, có bằng chứng, trước khi viết
> dòng code đầu tiên.

**5 điểm khác, dùng cho landing và blog:**

1. **Cầu > cung có bằng chứng.** Lấy lời chê trong review, Reddit, HN, GitHub cộng với Trends. Kết quả là 1 kết luận, không phải bảng số.
2. **Đi đến lúc build.** Phễu 100 → 10 → 3, bàn chấm điểm, nút Bắt đầu build. Hai tool kia không có bước này.
3. **Chạy trong Claude.** Bộ công cụ niche-radar để Claude tự đi research ngay trong chỗ anh code.
4. **Nhiều nguồn.** App, YouTube, (sau này) sách. Dành cho người làm sản phẩm số, không chỉ team ASO.
5. **Giá cho người làm một mình.** Nhắm đúng chỗ review chê 2 tool kia đắt.

**Việc làm:**

- 2 bài blog so sánh: "ShotMatic vs AppTweak for app idea research", "Appfigures alternative for indie devs".
  Viết theo skill `/shotmatic-blog`. Mỗi bài có bảng tự làm, chạy cùng 1 niche thật trên ShotMatic, và
  **không chê sai** đối thủ: chỉ ghi điều trang của họ công bố, có link nguồn và ngày tra.
- Landing: thêm 1 dòng "Not another ASO tool" gần hook, link tới 2 bài trên.
- Không dùng logo hay tên thương hiệu của họ làm hình ảnh. Chỉ nhắc tên trong chữ.

## Câu chờ anh chốt

| # | Câu hỏi | Mặc định nếu anh không chọn |
|---|---|---|
| 1 | Làm 25.4 (marketing) ngay, 25.1–25.3 để sau khi bán? | Có: 25.4 trước |
| 2 | Code thì theo thứ tự 25.1 → 25.2 → 25.3? | Có. 25.1 nhỏ nhất và mục 24 dùng lại được |
| 3 | 25.3 dùng model nào để hỏi? | Model anh đang cài trong Cài đặt AI |

## Chia việc

1. **25.4** 2 bài blog qua `/shotmatic-blog` + 1 dòng trên landing. Soát `check_post.mjs`, xem tận mắt 1340px.
2. **25.1** Hàm thuần `web/src/lib/climb-difficulty.ts` + test `tests/climb-difficulty.test.ts`, test bằng số 3–4 lượt Research thật trong DB máy dev.
   Gắn vào Keyword, Explorer, Săn app. Chữ 3 ngôn ngữ.
3. **25.2** Luật lọc trong `tracking.ts` (hàm thuần + test) + hộp trên trang Project.
4. **25.3** Nút Hỏi AI + bảng lưu câu trả lời + migration. Chạy thật 2 keyword, ghi số token thật vào mục **Đã đo**.
5. Xem tận mắt 960px và 1340px, sáng và tối.

## Đã đo

Chưa đo gì. 25.1 cần soát lại ngưỡng 35 / 65 bằng số thật trước khi chốt.

## Giới hạn

- Độ khó leo là quy ước tự đặt, chưa kiểm bằng app thật thành công.
- 25.2 chỉ báo khi anh mở app, không báo lúc máy tắt.
- 25.3: câu trả lời của AI đổi theo ngày và theo model. Chỉ coi là tín hiệu, không phải số đếm chắc.
- Tính năng và giá của AppTweak, Appfigures có thể đã đổi. Tra lại trước khi đăng bài so sánh.

Nguồn tra 2026-11-16:

- [Appfigures pricing](https://appfigures.com/platform/pricing)
- [Appfigures App Intelligence](https://appfigures.com/products/app-intelligence)
- [toolradar – Appfigures](https://toolradar.com/tools/appfigures)
- [AppTweak pricing](https://www.apptweak.com/en/pricing?currency=usd)
- [Capterra – AppTweak](https://www.capterra.co.uk/software/196668/apptweak)
- [G2 – AppTweak](https://www.g2.com/products/apptweak/reviews)
