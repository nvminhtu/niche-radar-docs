# 33 · So đối thủ theo lời chê: ai làm tốt, ai đang hỏng, chỗ nào cả chợ bỏ trống

> Plan 2 · mục 33. Làm thật tab **So app** của [Đào review](phase-plan2-27-review-mining.md) (đang "Sắp có", ý ở 27.5):
> chọn **2–10 app**, ra bảng **nỗi đau × app**, rồi code tự rút 6 kết luận: chung · riêng · app tốt nhất · app yếu nhất ·
> khoảng trống cả chợ · chỗ làm khác được. Mỗi cơ hội có **cửa kiểm chứng** (có người tìm không, có người trả tiền không)
> trước khi được gọi là cơ hội.

<span class="chip chip--todo">Viết + anh duyệt 2026-11-18 · chưa code · commit 24–27 trước</span>

## Feature này có phải "Compare Apps" không?

**Gần đúng, nhưng không nằm ở trang Compare Apps.** Mình đang có 2 chỗ "so app":

| Chỗ | So gì | Có lời chê? |
|---|---|---|
| **So sánh app** (`/compare/competitors`, mục 20 + 22) | 2–4 app: số store, hạng keyword, tính năng có / không, bảng "app mới nên có gì" | **Không.** Anh chốt 2026-11-15 bản đầu không có khối lời chê |
| **Đào review → tab So app** (mục 27.5) | 2–10 app: nỗi đau × app | Đúng việc này, nhưng tab đang xám "Sắp có" |

Bản đề xuất anh dán (Module 05) chính là **tab So app của Đào review**. Mục này làm tab đó, rồi đặt **1 khối gọn** ở trang
So sánh app trỏ sang (33.6), để 2 trang không làm 2 lần cùng một việc.

## Đã đo (2026-11-18 · DB máy dev, chỉ đọc)

- **`review_seen`:** 15.956 review của **266 app**. 13.850 review 1–3★, chỉ **2.106** review 4–5★ (bản cũ chỉ giữ review chê).
- **App có ≥ 30 review chê:** 188 / 266. **≥ 50 review chê:** 116. Trung bình 52 review chê mỗi app. Đủ để so phần lớn app.
- **Nguồn:** 2.858 Play, 100 App Store, 12.998 review cũ chưa có cột `source`. App Store chỉ lấy được tối đa 100 review / app / nước.
- **Đã có sẵn trong code:** 9 loại chê (`complaint-rules.ts`), nhóm + điểm /100 (`review-mining.ts`), luật "chung ≥ 60%",
  đèn "chỉ chen bằng giá" + "người dùng tự vá" (`weak-spots.ts`, mục 26), cụm khen 4–5★ (27.6). Mục này dùng lại, không viết lại.

## Học từ tool lớn + nghiên cứu (tìm 2026-11-18)

| Nguồn | Họ làm gì | Mình lấy gì |
|---|---|---|
| **Appbot** · trang Compare | Theo dõi app đối thủ như app mình; so số review, sao trung bình, sentiment, đường xu hướng theo thời gian | Mỗi ô có **xu hướng** (đang tăng / đang giảm), không chỉ 1 con số |
| **AppFollow** · Compare feedback | So điểm sentiment + **tag phổ biến nhất theo từng chợ** (nước) | Chế độ **nỗi đau × nước** (đã hứa ở 27.0) dùng chung bảng này |
| **FeatCompare** (bài báo, khảo sát 107 dev, > 70% thấy hữu ích) | So app theo **từng tính năng** rút từ review, không chỉ sao tổng | Hàng của bảng là **nỗi đau cụ thể**, mở rộng từ 9 loại ra cụm chữ |
| **RE-SWOT** (bài báo) | Gom review nhiều app thành ma trận mạnh / yếu / cơ hội / đe doạ theo tính năng | Khối **Chỗ làm khác được** xếp theo 4 ô kiểu SWOT |
| Bài báo LLM 2025 (aspect – sentiment – đề xuất) | AI rút bộ ba "khía cạnh · khen/chê · người dùng muốn gì" | Chỉ là nút ✦ tuỳ chọn để **đặt tên cụm**, số đếm vẫn do code |

**Repo / skill có sẵn:** không tìm thấy repo GitHub nào làm sẵn đúng việc "so lời chê nhiều app ra cơ hội"; phần lớn là bài
báo. Skill `marketing-skills:competitor-profiling` và `marketing-skills:customer-research` chỉ dùng làm khung câu hỏi cho
✦ AI. Phần lõi tự viết bằng luật, như mục 22 + 27.

**Tool lớn không làm (và mình làm được):** Appbot / AppFollow bán cho **app đã có** muốn theo dõi đối thủ. Không tool nào trả
lời câu "**cả chợ đang hỏng ở đâu, có đáng làm app mới không**". Đây là chỗ ShotMatic khác: mọi kết luận dẫn tới cửa kiểm
chứng cầu + tiền.

## Bản đề xuất được chỉnh lại ở đâu

| Bản đề xuất | Vấn đề | Plan này sửa |
|---|---|---|
| Ô = 1 con số % | App 40 review và app 400 review bị so như nhau | Mỗi ô có **khoảng tin** (Wilson 95%). Chỉ gọi "tốt nhất / tệ nhất" khi chênh rõ, sát nhau thì ghi **ngang nhau** |
| % trên gì? (không nói) | Cache cũ gần như chỉ có review chê, nên % trên mọi review bị sai | Ô = **% trong review chê** (chê về gì). Hàng riêng **Tỉ lệ review chê** chỉ hiện khi đã đọc đủ cả 1–5★ |
| Best = ít bị chê nhất | Không bị chê có thể chỉ vì app không có tính năng đó | Best cần **thêm bằng chứng khen** (cụm 4–5★ cùng nhóm). Không có thì ghi "ít bị chê", không gọi "làm tốt" |
| Không nói thời gian | Lời chê đã sửa ở bản mới vẫn bị tính | Ô có chip **▲ / ▼** (30 ngày gần nhất so với trước). Giảm mạnh thì ghi "có thể đã sửa" |
| Market-wide gap = mọi app bị chê | Chung nhưng nhẹ, hoặc toàn app nhỏ | Cần ≥ 60% app **và** mỗi app ≥ 5% review chê **và** không app nào có bằng chứng khen. Kèm "đè lên bao nhiêu rating" |
| "Phải kiểm chứng thêm" chỉ là câu nhắc | Dễ bị bỏ qua | **Cửa kiểm chứng** là 3 chấm bắt buộc trên mỗi cơ hội (33.4). Chưa qua thì nhãn "chưa kiểm", không lên đầu |

## Làm gì

### 33.0 · Đọc review đủ để so công bằng

- Khi chọn ≥ 2 app ở Đào review, mặc định đọc **cả 1–5★** (cần cho tỉ lệ chê + bằng chứng khen). Lưu cả review 4–5★.
- Mỗi app ghi rõ **cỡ mẫu**: số review đã đọc · số review chê · khoảng ngày của mẫu · nguồn. App có < 30 review chê → cột xám
  "ít review, chưa so", vẫn hiện nhưng không được chọn làm tốt nhất / tệ nhất.
- Mẫu khác khung thời gian (app lớn: 200 review = 3 ngày, app nhỏ: 200 review = 1 năm) → ⓘ cảnh báo trên đầu cột.
  Có nút **Chỉ so 90 ngày gần nhất** để cắt cùng một khung.

### 33.1 · Bảng nỗi đau × app (hàm thuần)

- Hàng mặc định = **9 loại chê** sẵn có (ổn định, so được giữa mọi app). Nút **Chi tiết hơn** đổi hàng sang nhóm nỗi đau
  (cụm chữ của 27.3, đã gộp tay / ✦ ở 27.4), chỉ lấy nhóm có ≥ 3 người.
- Ô = số review chê của app thuộc nhóm ÷ tổng review chê của app. Một review được vào nhiều nhóm (giống 27.4).
- Mỗi ô giữ: n, %, khoảng tin, chip xu hướng, 1 câu trích, link mở Review gốc đã lọc sẵn app + nhóm.
- Hàng cuối **Tỉ lệ review chê** của app (review 1–3★ ÷ mọi review đã đọc), chỉ khi 33.0 đọc đủ 1–5★.
- Chế độ phụ **nỗi đau × nước** cho 1 app (từ 27.0): cùng hàm, cột là nước.

### 33.2 · 6 kết luận (luật, không AI)

| Khối | Luật (ngưỡng là quy ước ShotMatic, anh chỉnh được) |
|---|---|
| 🌐 **Chung** | Nhóm có ở ≥ 60% số app, mỗi app ≥ 5% review chê |
| 🎯 **Riêng** | Chỉ 1 app ≥ 10% và cao hơn hẳn các app khác (khoảng tin không chồng) |
| 🏆 **Tốt nhất từng nhóm** | % thấp nhất, chênh rõ, app có ≥ 30 review chê. Có cụm khen cùng nhóm → "làm tốt", không có → "ít bị chê" |
| ⚠️ **Yếu nhất** | Theo nhóm: % cao nhất, chênh rõ. Tổng: tỉ lệ review chê cao nhất (khi có), hoặc nhiều nhóm "yếu nhất" nhất |
| 🕳 **Khoảng trống cả chợ** | Thuộc Chung **và** không app nào "làm tốt" **và** không phải nhóm tiền / khác. Ghi tổng số rating của các app bị chê = "đè lên bao nhiêu người dùng" |
| ✨ **Chỗ làm khác được** | Xếp theo 4 ô kiểu SWOT bên dưới |

**Chỗ làm khác được** (mỗi dòng có lý do + số):

- **Làm tốt cái cả chợ hỏng:** Khoảng trống cả chợ, nhóm không phải tiền. Đây là cơ hội mạnh nhất.
- **Hút khách của app lớn đang hỏng:** Riêng, rơi vào app nhiều rating nhất, đang ▲. Người dùng app đó là khách để kéo sang.
- **Phải ngang bằng (không phải lợi thế):** nhóm mà có app "làm tốt". Thiếu là bị chê, làm có cũng không khác ai.
- **Chỉ chen được bằng giá:** nhóm Ép trả phí / giá đứng đầu ≥ 35% (đèn 🔴 của mục 26). Ghi rõ đây là cạnh tranh giá, không phải tính năng.

Câu kết luận đầu tab (1 dòng, có màu): *"Cả 5 app bị chê {nhóm} ({min}–{max}%), chưa app nào làm tốt → nên kiểm thêm"*,
hoặc *"Chưa thấy khoảng trống chung, chỗ đáng nhắm là {app} đang hỏng {nhóm}"*.

### 33.3 · Nhãn bằng chứng trên mọi số

Giữ 3 nhãn của 27.3: **Đo được** (đếm review) · **Tính ra** (%, khoảng tin, kết luận luật) · **AI suy luận** (tên cụm, thẻ ✦).
ⓘ của mỗi kết luận ghi đúng luật + số đã dùng.

### 33.4 · Cửa kiểm chứng (cầu + trả tiền)

Mỗi dòng ở Khoảng trống cả chợ và Chỗ làm khác được có **3 chấm**, đọc từ dữ liệu đã có, không gọi store thêm:

| Chấm | Xanh khi | Chưa đo thì |
|---|---|---|
| 🔎 Có người tìm | Keyword của niche có trong Research với tín hiệu gõ (gợi ý store / Trends có số, mục 22.3 + 32) | Nút **Tra keyword** |
| 💰 Có người trả tiền | ≥ 1 app trong bảng có IAP / gói tháng (`iap_cache`, `offers_iap`), hoặc lời chê giá có câu "I paid / subscribed / refund" (người đã trả) | Ghi "chưa đo" |
| 🩹 Người dùng tự vá | ≥ 3 review nhắc spreadsheet / notes / switched to (luật `WORKAROUND_RE` mục 26) | Ghi "chưa thấy" |

- 2 / 3 chấm xanh → nhãn **Đáng làm tiếp**. Dưới 2 → **Chưa kiểm**, không lên đầu khối.
- Review không đo được số người tìm hay số tiền, nên chấm chỉ nói "có tín hiệu", không ra con số doanh thu.

### 33.5 · Giao diện tab So app

Theo skill `tool-chart`, xếp 1 cột từ trên xuống:

1. Câu kết luận + 4 ô số (số app · review chê đã so · nhóm chung · khoảng trống).
2. **Bảng nhiệt** nỗi đau × app: cột đầu `sticky`, bảng `overflow-x-auto` (10 app vẫn đứng được ở 960px), màu ô 1 thang
   tuần tự chạy cả sáng / tối, 🏆 / ⚠️ trong ô, chấm màu app trùng màu ở So sánh app. Rê ô thấy n, khoảng tin, câu trích.
3. 6 khối kết luận (33.2), mỗi khối 1 thẻ dọc, dòng có chip cửa kiểm chứng (33.4).
4. Nút: **Gom vào project** (app = đối thủ, dòng = item lời chê / cơ hội) · **Copy Markdown** · **✦ AI viết thẻ cơ hội**
   (dùng lại 27.6, chỉ được dùng dòng đang hiện).

### 33.6 · Nối với trang So sánh app + xuất + MCP

- **So sánh app (mục 20):** thêm khối gọn **Lời chê**. App đã có review → 3 dòng đầu của bảng (Chung · Yếu nhất · Khoảng
  trống) + link **Mở so lời chê**. Chưa có → nút **Đào review N app này** (mở Đào review đã điền sẵn app + nước). Anh chốt có làm (2026-11-18).
- **Xuất:** Markdown + CSV ma trận + JSON (có phiên bản luật) vào bộ xuất Review Mining.
- **MCP:** tool chỉ đọc `get_competitor_pains` (app ids, nước) → ma trận + 6 kết luận + chấm kiểm chứng, mọi số kèm nguồn.

### 33.7 · Kiểm độ đúng

- Test hàm thuần: khoảng tin, "ngang nhau" khi chồng, app < 30 review không được chọn, Chung / Riêng / Khoảng trống đúng luật,
  1 review nhiều nhóm, phần chưa đo không thành 0.
- Chạy thật 2 bộ: 5 app "habit tracker" (Play, US) và 3 app iOS cùng niche. Kiểm tay 10 ô với Review gốc, ghi thời gian + số vào trang này.

## Code ở đâu

| File | Việc |
|---|---|
| `web/src/lib/competitor-pains.ts` | hàm thuần: ma trận, Wilson, xu hướng, 6 kết luận, chấm kiểm chứng |
| `web/src/lib/review-mining-run.ts` | đọc đủ 1–5★ khi ≥ 2 app, thêm `matrix` vào kết quả |
| `web/src/client/ReviewCompare.tsx` | tab So app (bỏ chip "Sắp có" ở `ReviewMining.tsx`) |
| `web/src/client/CompareCompetitorsPage.tsx` | khối gọn Lời chê |
| `web/src/mcp/…` | `get_competitor_pains` |
| `web/tests/competitor-pains.test.ts` | test luật + ngưỡng |

<div class="box box--rules" markdown>
**Luật**

- Không bịa số. Ô thiếu ghi "chưa đo", app ít review ghi "ít review, chưa so"
- Mọi % ghi rõ "% trong review chê" hay "% mọi review"
- "Tốt nhất / tệ nhất" chỉ khi chênh rõ. Không bị chê ≠ làm tốt
- Khoảng trống cả chợ chưa phải cơ hội: phải qua cửa kiểm chứng
- Không ước lượt tải / doanh thu. Ngưỡng là quy ước ShotMatic, ghi trong ⓘ
- Không hiện số mục trên UI
</div>

<div class="box box--star" markdown>
**Xong khi**

- So 5 app thật → bảng nhiệt đủ ô, 6 khối kết luận có số + câu trích, kiểm tay 10 ô đúng
- App < 30 review chê hiện xám, không bị chọn tốt nhất / tệ nhất
- Mỗi dòng cơ hội có 3 chấm kiểm chứng, chấm chưa đo có nút đi đo
- Đọc được ở 960px + 1340px với 10 app, sáng + tối, English + tiếng Việt
- `npm run check` + `npm run docs:build` xanh
</div>

<div class="box box--danger" markdown>
**Không làm ở mục này**

- Theo dõi đối thủ theo lịch, báo động (giống quyết định 27)
- Embeddings / gom cụm bằng model trên máy
- Đọc review tiếng địa phương (luật chê chỉ hiểu tiếng Anh)
- So hơn 10 app
- Ước doanh thu hay số người sẵn sàng trả tiền
</div>

## Anh chốt 2026-11-18 (duyệt theo đề xuất)

1. Làm ở **tab So app của Đào review**. Trang So sánh app không làm lại phần này.
2. Trang So sánh app **có** khối gọn Lời chê trỏ sang (33.6). Bỏ quyết định 2026-11-15 không có khối lời chê.
3. Khi so ≥ 2 app, **mặc định đọc cả 1–5★** (33.0).
4. Giữ ngưỡng: Chung ≥ 60% app và ≥ 5% mỗi app · app cần ≥ 30 review chê mới so · Riêng ≥ 10%. Ghi là quy ước ShotMatic trong ⓘ.
5. **Commit mục 24–27 trước**, rồi mới code mục này.
