# 26 · Săn app tìm ra điểm yếu đối thủ

> Plan 2 · mục 26. Săn app (mục 24) hiện chỉ trả lời **"keyword nào có cầu > cung"**. Mục này thêm câu trả lời
> **"đánh vào điểm yếu nào, của app nào, có bao nhiêu người than"** cho từng keyword được chốt.

<span class="chip chip--doing">Viết + code 26.1–26.7 2026-11-16 · chờ anh soát</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Anh chốt "làm hết" ngày 2026-11-16, nên mục này đã code.
</div>

## Vì sao làm

Anh đăng thread hỏi "làm sao biết ý tưởng app đáng làm trước khi code" trên r/SideProject (2026-11-16) và dán nội dung
thread vào chat. Nhiều góp ý trùng một ý: **review xấu của app đang có mới nói rõ chỗ hổng**, số lượt tìm thì không.
Săn app hiện chấm keyword bằng số store (gợi ý, Trends, app mới leo, rating, tên app, tiền), còn lời chê thì **không tính điểm**
và chỉ có khi bấm "Đọc review" (mục 24.4).

## Góp ý đáng dùng trong thread (đọc 2026-11-16)

Chỉ giữ góp ý đổi được thành luật trong tool. Bỏ các comment quảng cáo và comment đùa.

| Ai nói | Ý chính | Đưa vào |
|---|---|---|
| N_Moon_3019 (làm ReviewFold) | Đếm **độ lặp**, không đếm tổng review. Lấy 3 app dẫn đầu × 50 review mới nhất, giữ 1–2★, chia theo **việc bị hỏng**, rồi xem tỉ lệ từng nhóm. Ví dụ của họ: 5 app đếm calo, 69 review chê, nhóm tiền / paywall 41% | 26.1 |
| N_Moon_3019 | 🔴 Nhóm lớn nhất là **tiền / paywall** thì dừng: không build hơn được một quyết định về giá, chỉ bán rẻ hơn được, mà đó là kiểu kinh doanh khác | 26.2 |
| N_Moon_3019 | 🟢 **≥ 3 người khác nhau** tả cùng 1 việc hỏng bằng chữ khác nhau. Ít hơn thì chỉ là 1 người to tiếng. Nhóm nhỏ mà solo dev sửa được (ví dụ đơn vị đo theo vùng) là chỗ app lớn bỏ quên nhiều năm | 26.2 |
| brandhacker | Đặt review **cao hơn** số lượt tìm. Phần khó là đo cung: **đếm số app hay đo app đó tốt cỡ nào?** Nên có nhiều chế độ săn: theo keyword, theo đối thủ, theo review chê | 26.3, 26.5 |
| ram-popular | 🔴 **Không có đối thủ nào**, hoặc chợ đông mà **không nêu được 1 điểm làm khác**. Chợ đông chứng minh có người trả tiền, nên câu hỏi là app lớn hụt ở đâu | 26.2 |
| xiaoyao8888, ausecko, Kitchen_Cable6192 | Tín hiệu khó giả: người dùng đang **tự vá** (bảng tính, app ghi chú, giấy) hoặc **trả tiền cho app bị chê** | 26.2 |
| Pale_Individual4850 | App lớn **phình**: quá nhiều tính năng, rối. Bản làm **gọn hơn** là một góc chen | 26.2 |
| patryk_builds, LumynaAI | 🔴 Không nêu được **10 chỗ** người mua đang hỏi về vấn đề, vì không tìm được họ thì sau khi ra app cũng không tìm được | 26.6 |
| Individual_Big873, xiaoyao8888 | Tín hiệu mạnh nhất là **trả tiền trước khi có code**: trang 1 trang có giá thật, gửi cho người đang chê | 26.7 |

## Đang có gì (đọc code 2026-11-16)

- **Săn app** `web/src/lib/app-hunt.ts` + `app-hunt-run.ts` (mục 24): điểm /100 gồm 6 phần, lời chê chỉ hiện thành 1 chip khi đã đọc review.
- **Lời chê** `web/src/lib/complaints.ts` + `complaint-rules.ts`: gom cụm 1–3 chữ, 8 loại (Lỗi · Mất dữ liệu · Ép trả phí · Quảng cáo ·
  Đồng bộ · Thiếu tính năng · Khó dùng · Khác). Mỗi cụm đếm số review **khác nhau** (`ids`).
- **Nỗi đau** `web/src/lib/complaint-pains.ts` (Soi 1 app, 2026-11-16): gom cụm theo loại, kèm câu "cơ hội cho app mới".
  Số đang là **tổng lần nhắc của các cụm**, nên 1 review nhắc 2 cụm bị đếm 2 lần.
- **Đọc review** `lowReviews` (Play + App Store, cache 7 ngày): Soi 1 app đọc 200 review mới nhất của 1 app.
- **Nơi người dùng hỏi** (Find Gaps): Hacker News, StackExchange, GitHub, Reddit (dán / import) ở `web/src/lib/qa-*.ts`, `gh-collect.ts`, `reddit-*.ts`.

## 26.1 · Đọc điểm yếu cho từng keyword được chốt

Làm theo cách của N_Moon_3019, gắn vào bước 3 của Săn app:

1. Với **3 keyword được chốt**, lấy **3 app dẫn đầu** mỗi keyword (nhiều rating nhất trong top 10, gộp bản Play + App Store theo tên).
2. Mỗi app đọc **50 review mới nhất có chữ**, giữ 1–2★ (1–3★ nếu 1–2★ dưới 10 review).
3. Gom theo **việc bị hỏng** (loại nỗi đau + cụm chữ của niche), đếm **số review khác nhau** cho từng nhóm, không cộng lần nhắc.
4. Hiện **tỉ lệ** từng nhóm trên tổng review chê, kèm câu trích nguyên văn.

Số request: 3 keyword × 3 app = **tối đa 9 app**, mỗi app 1 lượt đọc review (dùng cache 7 ngày nếu đã đọc).
Đo 2026-11-16 trên "habit tracker" US (lượt săn có sẵn): 8 app, **13 giây**. 4 app App Store bị trả lỗi 429 (Apple chặn tạm), tool đã thử bản Google Play cùng tên nếu có. Đo tiếp 2026-11-16 trên "calorie counter" US (lượt săn mới #25): 9 app, **khoảng 22 giây**, không lỗi.

So với ví dụ trong thread (N_Moon_3019: 5 app đếm calo, 69 review chê, nhóm tiền 41%):

| Đo | Số app | Review chê | Nhóm tiền / paywall |
|---|---|---|---|
| Thread (số của người comment) | 5 | 69 | 41% |
| ShotMatic, gộp 3 keyword chốt | 8 | 335 | 167 người · 50% |
| ShotMatic, từng keyword | 3 mỗi keyword | 65–144 | 37% – 51% |

Cùng kết luận với thread: **tiền là nhóm lớn nhất**, nên cả 3 keyword chốt đều bật đèn 🔴 "Chỉ chen được bằng giá".
Ngoài tiền, việc lặp nhiều nhất là **quảng cáo** (17 người ở 3 app, keyword "a i calorie counter"). Đèn 🟢 "App lớn bị phình" bật ở
"ai calorie counter - vaha" (8 người). Mọi app dẫn đầu đều có nhãn "tránh" hoặc "bình thường", không app nào "chen được".

Bước 1 còn lọt keyword rác: "a&w calorie counter" (tên hãng đồ ăn), "cal m counter strike" (tên game); "a i calorie counter"
và "ai calorie counter" chưa được coi là trùng. Đây là lỗi của bộ lọc bước 1 (mục 24), không phải của mục 26.

**Đã sửa bộ lọc bước 1 (2026-11-16, `huntRows` trong `app-hunt.ts`):**

- **Chưa đo:** keyword đo lỗi giữa chừng (có điểm hot nhưng độ chật và số app 2 store đều trống) bị loại.
  Đây là nguyên nhân chính ở lượt #25: 40 keyword điểm 43 rỗng số đo lọt vào danh sách tick sẵn.
- **Lạc đề:** keyword thiếu chữ chính của chủ đề bị loại. Chủ đề có tối đa 2 chữ chính thì phải có đủ, dài hơn thì cần ≥ 2/3.
  Chữ đệm (under, years, số…) không tính là chữ chính.
- **Tên hãng:** keyword có chữ dạng "a&w", "h&m" bị loại.
- **Trùng nghĩa:** gộp chữ cái lẻ liền nhau ("a i" = "ai"), bỏ "a / an / the", bỏ dấu câu.
- **Hoà điểm:** keyword ít chữ thêm ngoài chủ đề xếp trước, không xếp theo abc nữa.

Chạy lại trên số của lượt #25: với lọc mặc định, **0 keyword qua lọc** (60 keyword top 5 quá đông, 40 chưa đo). Niche này đông thật, nên trang
hiện câu "hạ ngưỡng ở Tuỳ chọn". Tắt lọc "quá đông" thì 10 keyword tick sẵn đều đúng chủ đề (calorie counter free, … widget). Lạc đề 6, trùng 3, tên hãng 1.
Giới hạn: "calorie calculator" cũng bị coi là lạc đề vì thiếu chữ "counter".

Sửa luôn số ở Soi 1 app: đếm **số review khác nhau** cho mỗi nhóm nỗi đau, không cộng lần nhắc các cụm.

## 26.2 · Đèn đỏ / đèn xanh (luật, không AI)

Mỗi keyword được chốt có 1 dòng đèn. Đèn **không đổi điểm /100**, chỉ nói nên đánh vào đâu hoặc nên cẩn thận chỗ nào.

| Đèn | Luật | Từ góp ý |
|---|---|---|
| 🔴 Chỉ chen được bằng giá | Nhóm **Ép trả phí** lớn nhất **và** ≥ 35% review chê | N_Moon_3019 |
| 🔴 Chưa thấy đối thủ thật | Top 10 dưới 3 app có ≥ 100 rating | ram-popular |
| 🔴 Chưa thấy điểm làm khác | Đã đọc review mà không nhóm nào (trừ tiền) đạt ≥ 3 người khác nhau | ram-popular |
| 🟢 Việc hỏng lặp lại | 1 nhóm (không phải tiền) có **≥ 3 người khác nhau**, ở ≥ 2 app | N_Moon_3019 |
| 🟢 Người dùng đang tự vá | Review nhắc *spreadsheet, excel, google sheets, notes app, paper, pen and paper, went back to, switched to* | xiaoyao8888, ausecko |
| 🟢 Trả tiền mà vẫn chê | App có giá hoặc IAP, sao dưới 4,0 hoặc hơn 180 ngày không cập nhật | xiaoyao8888, ram-popular |
| 🟢 App lớn bị phình | Review nhắc *too many features, cluttered, bloated, redesign, ai features, used to be simple* | Pale_Individual4850, N_Moon_3019 |

- Thêm loại lời chê **"Phình / đổi giao diện"** vào `complaint-rules.ts` cho đèn cuối cùng (hiện các chữ này rơi vào "Khó dùng").
- Ngưỡng 35%, 3 người, 100 rating là **quy ước ShotMatic**, chưa kiểm bằng app thật thành công. ⓘ ghi rõ.

## 26.3 · Cung đo bằng "app top yếu cỡ nào", không chỉ đếm

Trả lời câu brandhacker hỏi. Thêm **độ yếu** cho từng app dẫn đầu, dùng số đã có:

- Sao dưới 4,0 · hơn 180 ngày không cập nhật · tỉ lệ 1–2★ trong 50 review mới nhất · nhóm tiền lớn nhất.
- Nhãn từ Soi 1 app (`inspectVerdict`): Tránh đối đầu · Chen được · Nên học.

Thẻ keyword ghi: **"3 app dẫn đầu: 1 tránh, 2 chen được"**. Phần **"Cung còn chỗ"** trong điểm /100 sửa thành: rating trung vị
(như cũ) **cộng** số app dẫn đầu có nhãn Chen được. Tổng điểm tối đa không đổi.

## 26.4 · Thẻ chốt ghi rõ "đánh vào đâu"

Mỗi keyword được chốt có thêm 1 khối, xếp 1 cột:

- **Đánh vào:** 1 câu, ví dụ *"Đồng bộ hỏng — 7 người khác nhau, ở 2/3 app (Habitify, Loop)"* + 1–2 câu trích.
- **Đèn:** các chip 🔴 / 🟢 của 26.2.
- **Cung:** dòng của 26.3.
- Nút **Soi app** cho từng app dẫn đầu (mở Soi 1 app) và **Thêm để so** (list Sẵn sàng để so).

## 26.5 · Chế độ săn thứ 2: Săn từ lời chê (làm sau)

Theo ý brandhacker (nhiều chế độ săn). Gõ 1 chủ đề → lấy 10 app dẫn đầu → đọc review trước → xếp nỗi đau → trả về keyword gắn
với nỗi đau lớn nhất. Ngược chiều với phễu keyword hiện tại. Chỉ làm khi 26.1–26.4 chạy ổn.

## 26.6 · "Người dùng hỏi ở đâu" (làm sau)

Theo patryk_builds, LumynaAI. Với keyword được chốt, đếm số thread đang hỏi về vấn đề ở các nguồn Find Gaps đã có
(Hacker News, StackExchange, GitHub; Reddit chỉ khi anh đã dán / import). Hiện **"N chỗ đang hỏi"** + link.
Dưới 10 chỗ thì ghi đèn 🔴 "khó tìm khách đầu tiên". Không gọi nguồn mới.

## 26.7 · Bước kiểm trước khi code (chỉ chữ, làm sau)

Theo Individual_Big873, xiaoyao8888. Cuối thẻ keyword có 1 danh sách việc gợi ý, không tính điểm:
viết trang 1 trang có giá thật, gửi tới các chỗ ở 26.6, đếm người hỏi "bao giờ có" hoặc đặt cọc.
Nút ✦ AI soạn nháp trang 1 trang từ nỗi đau ở 26.4.

## Anh chốt (2026-11-16)

Anh trả lời "làm hết", nên code theo 2 mặc định đầu và làm luôn 26.5–26.7:

1. Bước 3 **tự đọc review** 1 lần cho 3 keyword chốt, có nút **Dừng**. Bấm Dừng thì lượt săn đó không tự chạy lại.
2. Đèn 🔴 "Chỉ chen được bằng giá" **chỉ cảnh báo**, không trừ điểm, không đẩy keyword xuống.
3. 26.5–26.7 **làm ngay**, bản gọn như mô tả ở dưới.

## Đã làm (2026-11-16)

- **Lõi** `web/src/lib/weak-spots.ts` (hàm thuần): lấy mẫu 50 review, gom theo việc hỏng, đếm review khác nhau, câu trích,
  đèn đỏ / xanh, độ yếu app dẫn đầu, chỗ nên đánh vào, bảng nỗi đau, câu hỏi AI trang 1 trang. Test ở `web/tests/weak-spots.test.ts`.
- **Loại lời chê mới** "Phình / đổi giao diện" trong `complaint-rules.ts` (chữ *cluttered* dời từ "Khó dùng" sang).
- **Máy chủ** `app-hunt-run.ts`: 3 app dẫn đầu mỗi keyword, đọc cache review (không gọi mạng khi mở trang), đếm chỗ đang hỏi
  trong dữ liệu Find Gaps, việc đọc review chạy nền `POST /api/app-hunt/:id/weak` (`scope` top / all, `stop`).
  App Store lỗi thì thử bản Google Play cùng tên.
- **Điểm /100:** phần Cung còn chỗ cộng app dẫn đầu "chen được" (1 app +4, từ 2 app +7, tối đa vẫn 15).
- **Giao diện** `web/src/client/hunt-weak.tsx`: khối Đánh vào · đèn · app dẫn đầu (nút Soi app, So) · chỗ đang hỏi ·
  Kiểm trước khi code + ✦ AI soạn trang 1 trang. Thêm thẻ "Săn từ lời chê" dưới top 3.
- **Soi 1 app:** số nỗi đau đổi sang **số review khác nhau** (người), không cộng lần nhắc. Mở thẳng được bằng
  `/?mode=app&link=…&country=…` (nút Soi app ở Săn app dùng link này).

Soát 2026-11-16 trên lượt "habit tracker" US: keyword "habit tracker game" ra **Đánh vào: lỗi / treo, 10 người ở 2/2 app**,
đèn 🔴 tiền 35% + 🟢 việc lặp. Thẻ "Săn từ lời chê": lỗi 35 người ở 4 app, dính 5 keyword. Mở ở 960px và 1340px, không cuộn ngang.
Chỗ đang hỏi ra 0 ở mọi keyword này vì dữ liệu Find Gaps trên máy nghiêng về Mac / dev.

## Chia việc (26.1–26.4)

1. `web/src/lib/complaint-pains.ts`: đếm số review khác nhau cho mỗi nhóm; hàm `weakSpots` trả nhóm, tỉ lệ, số app, câu trích.
   Test ở `tests/complaint-pains.test.ts`.
2. `web/src/lib/complaint-rules.ts`: loại **Phình / đổi giao diện** + mẫu chữ **tự vá**. Sửa test lời chê cũ nếu đổi loại.
3. `web/src/lib/app-hunt.ts`: hàm thuần `huntLights` (26.2) và `supplyWeakness` (26.3), test ở `tests/app-hunt.test.ts`
   bằng số thật từ DB máy dev.
4. `web/src/lib/app-hunt-run.ts`: sau khi chấm, đọc review 3 app dẫn đầu × 3 keyword (cache 7 ngày), lưu kết quả vào lượt săn.
5. `web/src/client/AppHunt.tsx`: khối "Đánh vào", chip đèn, dòng cung, nút Soi app / Thêm để so. Chữ 3 ngôn ngữ.
6. Soi 1 app: đổi số nỗi đau sang số review khác nhau.
7. Chạy thật 2 chủ đề ("habit tracker" US, "calorie counter" US để so với ví dụ trong thread). Đo thời gian bước đọc review,
   ghi vào trang này. `npm run check` xanh. Xem 960px + 1340px, sáng + tối.

## Giới hạn

- Gom theo **việc bị hỏng** bằng luật chữ, không hiểu nghĩa. Hai câu khác chữ cùng một việc có thể rơi vào 2 nhóm.
  Nếu thấy thiếu nhiều, thêm nút ✦ AI "gom lại theo việc hỏng" sau.
- 50 review mới nhất / app là mẫu nhỏ. Nhóm dưới 3 người coi là chưa đủ, không bật đèn.
- Ví dụ số trong thread (5 app đếm calo, 41% tiền) là số của người comment, **ShotMatic chưa đo lại**.
