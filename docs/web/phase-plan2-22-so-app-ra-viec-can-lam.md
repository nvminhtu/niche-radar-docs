# 22 · So sánh app → bảng "app mới nên có gì" + Cầu > cung cho app

> Plan 2 · mục 22. Nối tiếp [mục 20](phase-plan2-20-so-sanh-doi-thu.md). Chọn 2–4 app đối thủ, cuối trang ra **1 bảng
> tổng kết**: tính năng nào phải có, tính năng nào làm mình khác, chỗ nào còn trống. Thêm nhãn **Cầu > cung** cho keyword
> app, cùng ý với Săn kênh nhỏ YouTube.

<span class="chip chip--todo">Viết 2026-11-15 · chờ anh duyệt</span>

## Anh hỏi gì (2026-11-15)

- Tiêu đề trong app to + đậm hơn cho dễ theo dõi. **Đã làm ngay** (xem 22.0).
- Áp tiêu chí **Cầu > cung** của YouTube cho app được không? **Được**, xem 22.3.
- So sánh nhiều app đưa vào **Main features**. **Đã làm ngay** (xem 22.0). So 4 app xong phải ra **bảng tổng kết các tính năng
  app nên có**, khỏi tự gom tay.

## Đã có gì, còn thiếu gì

- Trang **So sánh app** (mục 20) đã so được 2–4 app: số store, hạng keyword, tính năng.
- Hàng tính năng chỉ có **5 hàng mặc định** của Feature Gap + hàng anh tự thêm. Không đủ để nói "app mới nên có gì".
- Trang chỉ đọc cache. App chưa có mô tả trong cache thì cột tính năng ghi "chưa đo".
- Chưa có khối tổng kết cuối trang.

## Đã đo (2026-11-15 · DB máy dev, chỉ đọc)

- **Mô tả store đã cache:** 195 app, trung bình **2.350 ký tự** mỗi mô tả. Đủ dài để rút tính năng.
- **Review đã cache:** 207 app. Dùng được cho hàng "người dùng chê / xin thêm".
- **Cầu > cung:** 144 / 294 lượt Research có ít nhất 1 app **ra mắt dưới 1 năm** mà vẫn nằm **top 10** một keyword
  với **≥ 50 rating**. Tín hiệu có thật, ngưỡng cần chỉnh cho bớt nhiễu (xem 22.3).

## Phương pháp (tìm trên GitHub + skill Claude)

| Nguồn | Lấy gì | Ghi chú |
|---|---|---|
| Bài báo **SAFE** (Johann, Stanik, Maalej · RE 2017) | Rút tính năng từ mô tả + review bằng **luật mẫu câu** (gạch đầu dòng, động từ + danh từ), không cần AI | Miễn phí, chạy offline. Đây là cách chính của mục này |
| `app-store-scraper` · `google-play-scraper` (npm, MIT) | Mô tả + review | Repo đã dùng để lấy số store |
| Skill `marketing-skills:competitor-profiling` · `aso` | Khung so đối thủ: điểm mạnh / yếu, định vị | Chỉ dùng làm khung cho câu hỏi ✦ AI tuỳ chọn |
| Mô hình **Kano** | Chia tính năng: phải có · làm khác · gây thích | Dùng để xếp nhóm bảng tổng kết |

Không có tool miễn phí nào làm sẵn đúng việc "so 4 app → bảng nên có". Mình tự viết bằng luật, AI chỉ là nút tuỳ chọn.

## Làm gì

### 22.0 · Đã làm ngay (2026-11-15)

- Thanh dính trên trang Keyword: chữ **RESEARCHING KEYWORD** 13px đậm màu xanh, keyword to hơn (`text-xl` đậm). H1 trang
  Keyword lên `text-3xl` đậm.
- Sidebar: **So sánh app** vào nhóm Main features (dưới Projects), mô tả "2–4 đối thủ → nên làm gì". Mục con trùng ở
  Compare bỏ đi. Tab trên trang Compare giữ nguyên.

### 22.1 · Đọc trang store của 2–4 app (1 nút)

- Khi có app chưa có mô tả trong cache: hiện nút **Đọc trang store (N app)**. Bấm thì tải mô tả + review của đúng N app
  đó (tối đa 4 app × 2 request), lưu vào `listing_cache` + `review_cache`. Không tự tải khi mở trang.

### 22.2 · Rút tính năng (luật SAFE, không AI)

- Từ mô tả: lấy dòng gạch đầu dòng + câu có mẫu "động từ + danh từ" (track habits, export PDF, sync iCloud…). Chuẩn hoá
  (viết thường, bỏ từ thừa, gộp từ đồng nghĩa theo bảng nhỏ có test).
- Gộp cùng tính năng giữa các app → 1 hàng. Mỗi ô **có · trả phí · không nói**, rê chuột thấy câu trích.
- Từ review: câu "wish / please add / missing / doesn't have" → hàng **người dùng xin thêm**, kèm số review.

### 22.3 · Nhãn Cầu > cung cho app

Cùng ý YouTube: app **mới, ít rating** mà vẫn leo **top 10** một keyword **có người gõ** = người tìm nhiều hơn app đang có.

| Nhãn | Luật (ngưỡng là quy ước ShotMatic, anh chỉnh được) |
|---|---|
| 🔥 Cầu > cung | Top 10 có app ra mắt < 12 tháng, rating ≥ 50, và keyword có trong gợi ý store / Trends có số |
| Có cầu, chưa nổ | Có app mới top 10 nhưng < 50 rating, hoặc keyword không có tín hiệu gõ |
| Cung đầy | Top 10 toàn app > 3 năm, rating trung vị ≥ 10K |
| Chưa đủ số | Thiếu ngày ra mắt / hạng |

- Hiện ở đầu trang Keyword (chip cạnh điểm 6/10) và ở trang So sánh app.
- Mỗi nhãn có ⓘ ghi đúng app + số + Research #id làm căn cứ.

### 22.4 · Bảng tổng kết cuối trang So sánh app

Xếp **1 cột dọc**, mỗi nhóm 1 khối:

| Nhóm | Luật |
|---|---|
| ✅ Phải có | ≥ 3 / 4 app có (hoặc tất cả khi so 2–3 app). Thiếu là bị chê |
| ⭐ Làm khác | Chỉ 1 app có, và app đó sao / rating cao nhất bảng |
| 🕳 Còn trống | Không app nào có, nhưng review xin thêm ≥ 3 lần, hoặc lời chê top 1 của app nhiều rating nhất |
| 💰 Đang thu tiền | Tính năng app khác bắt trả phí: cơ hội cho miễn phí hoặc rẻ hơn |
| — Bỏ qua | 1 app có, app đó yếu, không ai xin |

- Mỗi dòng: tên tính năng · chấm có / không của từng app · số review xin · link câu trích.
- Nút **Gom vào project** (đưa cả bảng vào tab Ý tưởng của project) và **Copy Markdown**.
- Nút ✦ AI tuỳ chọn: viết 1 đoạn "MVP nên gồm", chỉ được dùng hàng đang hiện.

### 22.6 · Đổi tên "Tính năng nên có" + chọn dòng → file .md cho AI

Anh hỏi 2026-11-15: ghi rõ tên khối là **Tính năng nên có** (EN: *Features to have*), và cần file .md liệt kê sẵn để chọn
rồi đưa AI cập nhật plan. Đã code 2026-11-15:

- Mỗi dòng có **ô tick**. Mặc định tick sẵn Phải có + Còn trống + Làm khác (đúng 3 nhóm của nút Gom vào project).
  Dòng đã tick lưu trên máy theo bộ app đang so; mất thì về mặc định.
- Nút **Tải .md** (`features-to-have-<ngày>.md`) và **Copy Markdown** ra cùng 1 nội dung: checklist `- [x]` / `- [ ]` theo nhóm,
  ✓ / $ / – / ? từng app, 3 dòng đầu ghi app đang so, nguồn (Research #id + ngày đo) và câu nhờ AI cập nhật plan build theo dòng `[x]`.
- Hàm thuần `checklistMarkdown` · `defaultPicks` · `pickId` ở `web/src/lib/compare-extract-core.ts`, test ở `web/tests/compare-extract.test.ts`.
- Bảng này **chưa** chấm cầu > cung theo từng tính năng: nhãn Cầu > cung (22.3) chấm cả keyword. Nhóm gần "cầu" nhất là 🕳 Còn trống (review xin ≥ 3 lần).

### 22.5 · Lọc niche · keyword · đối tượng từ 2–4 app đã chọn

Anh hỏi 2026-11-15: so xong thì lọc ra luôn **niche, keyword, đối tượng** của nhóm app đó. Thêm 3 khối dưới bảng tổng kết,
xếp 1 cột dọc:

| Khối | Lấy từ đâu | Luật |
|---|---|---|
| 🔑 Keyword | `keyword_hits` của lượt Research + chữ trong tên / phụ đề app | Keyword app nào cũng có hạng = keyword chung của niche. Keyword chỉ 1 app có hạng = ngách riêng của app đó |
| 🧭 Niche con | Cụm 2–3 chữ lặp lại trong tên + mô tả các app (vd "drawing for toddlers", "step by step") | Cụm có ở ≥ 2 app = niche con đang có người làm. Kèm nút **Research cụm này** (mở trang Keyword) |
| 👥 Đối tượng | Dùng lại luật **Ai là khách hàng** đã có (`customer-rules.ts`): vai người dùng từ mô tả + review | Mỗi vai ghi app nào nhắm tới, kèm câu trích. Không đoán tuổi / giới tính |

- Mỗi dòng có nút **Gom vào project**.
- Tất cả đọc từ cache (mô tả + review của 22.1). Không AI.

## Code ở đâu

| File | Việc |
|---|---|
| `web/src/lib/feature-extract.ts` | luật SAFE + gộp hàng (hàm thuần) |
| `web/src/lib/app-demand-supply.ts` | nhãn Cầu > cung (hàm thuần) |
| `web/src/lib/compare-extract.ts` | keyword chung / riêng, cụm niche con, đối tượng (dùng lại `customer-rules.ts`) |
| `web/src/lib/competitor-compare.ts` | thêm `summary` vào `CcView` |
| `web/src/client/CompareCompetitorsPage.tsx` | nút đọc store, khối tổng kết |
| `web/tests/feature-extract.test.ts` · `app-demand-supply.test.ts` | test luật + ngưỡng |

<div class="box box--rules" markdown>
**Luật**

- Không bịa số. Ô thiếu ghi "chưa đo". Mỗi dòng tổng kết có câu trích hoặc số review làm căn cứ
- Ngưỡng Cầu > cung ghi rõ là quy ước, không phải sự thật của store
- Không ước lượt tải / doanh thu
- Không hiện số mục trên UI
</div>

<div class="box box--star" markdown>
**Xong khi**

- So 4 app thật (vd "drawing for kids") → bảng tổng kết có đủ 4 nhóm, mỗi dòng bấm ra câu trích
- Nhãn Cầu > cung hiện trên 3 lượt Research thật, kiểm tay đúng luật
- Đọc được ở 960px + 1340px, sáng + tối, English + tiếng Việt
- `npm run check` + `npm run docs:build` xanh
</div>

## Cần anh chốt

1. Ngưỡng Cầu > cung: **< 12 tháng + ≥ 50 rating** có ổn không?
2. Đọc store: bấm nút mới tải (đề xuất) hay tự tải khi mở trang?
3. Bảng tổng kết có cần nút ✦ AI "MVP nên gồm" ở bản đầu không?
4. Khối lọc niche · keyword · đối tượng (22.5) làm cùng đợt với bảng tổng kết, hay làm trước?
