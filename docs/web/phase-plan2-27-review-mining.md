# 27 · Review Mining: đào review chê ra cơ hội làm app

> Plan 2 · mục 27. Một trang riêng: **dán link 1 app (hoặc vài app) → đọc review chê → xếp nỗi đau có điểm → bấm vào xem
> review gốc → xuất báo cáo**. Không phải đi qua Săn app. Câu định vị: *Săn app tìm chỗ có cơ hội, Review Mining chỉ ra
> cơ hội nằm ở đâu.*

<span class="chip chip--doing">Viết 2026-11-16 · code 27.0–27.4 + xuất 2026-11-17 · chờ anh soát · chưa commit</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Mục 24–26 cũng chưa commit. Nên commit 24–26 trước rồi mới code mục này.
</div>

## Vì sao làm

Ngày 2026-11-16 anh dán một bản đề xuất "Review Mining" gồm 8 module, viết theo kiểu sản phẩm lớn (embeddings, HDBSCAN,
monitoring theo lịch, gói Free/Pro). Đọc code ngày 2026-11-16 thì **khoảng 60% phần lõi đã có**, nhưng nằm rải ở Soi 1 app,
So sánh app và Săn app (mục 26). Mục này **gom phần đã có vào 1 trang** và chỉ thêm phần còn thiếu cho 6 bước MVP:

1. Nhập 1 app.
2. Lấy review 1–3★.
3. Phân loại + gom nhóm.
4. Xem bảng xếp hạng nỗi đau.
5. Bấm vào nỗi đau là ra review gốc.
6. Xuất báo cáo.

## Bản đề xuất đối chiếu với code (đọc 2026-11-16)

| Module đề xuất | Đã có | Mục này làm |
|---|---|---|
| 01 Thu review | Play 200 review mới nhất (`collectors/play-reviews.ts`), iOS tối đa 100 (`appstore-web.ts`, 5 trang × 20). Cache 7 ngày, chỉ giữ 1–3★ | 27.2: lấy được nhiều hơn + import CSV/JSON |
| Lưu review + chống trùng | Bảng `review_seen`: khoá app + nước + hash nội dung, có sao, chữ, ngày, version, link, lần thấy đầu / cuối | 27.2: thêm `helpful`, `reply`, `source` |
| 02 Phân loại | 9 loại chê theo luật (`complaint-rules.ts`), có mức nặng | Dùng lại nguyên |
| 03 Gom cụm | Cụm 1–3 chữ sau khi gộp đồng nghĩa (`complaints.ts`) | 27.4: ✦ AI gom lại theo nghĩa (tuỳ chọn) |
| 04 Điểm nỗi đau | Chỉ có đếm số người (`complaint-pains.ts`, mục 26) | 27.3: điểm /100 có công thức |
| 05 So đối thủ | Trang So sánh app, Feature Gap, Săn app điểm yếu | 27.5: bảng nỗi đau × app (2–10 app) |
| 06 Xin tính năng | Mẫu câu "I wish / please add / bring back" | 27.5: tách thành 1 tab riêng |
| 07 Cơ hội | Nút Bắt đầu build (mục 13), ✦ AI trang 1 trang (mục 26.7) | 27.6: thẻ cơ hội, gắn nhãn "AI suy luận" |
| 08 Theo dõi | `review_seen.first_seen_at` có sẵn | 27.7: hộp "Mới từ lần trước", **không** chạy theo lịch |
| Xuất | `lib/export` (CSV, JSON, Markdown, zip) | 27.6: thêm bộ xuất Review Mining |

## Không làm (và vì sao)

- **Embeddings + HDBSCAN chạy trên máy.** Phải nhúng model khoảng 100MB, mà JS không có thư viện HDBSCAN tốt. Một app
  thường có vài trăm review chê, nên luật chữ + ✦ AI gom lại (27.4) là đủ.
- **Đọc review theo lịch, báo động.** Mục 25 đã bỏ phần chạy theo lịch. Chỉ so với lần đọc trước khi anh bấm đọc lại.
- **Nhiều ngôn ngữ.** Luật chê chỉ viết cho tiếng Anh, review cũng chỉ lấy `lang=en`. Tiếng Việt / Nhật cần bộ luật riêng, để sau.
- **Chia gói Free / Pro, giới hạn số review.** Để lúc bán, không chặn kết quả trong bản này.
- **Bộ 500–1.000 review gán nhãn tay.** Thay bằng file test nhỏ khoảng 60 review thật đã gán nhãn (27.8).

## 27.0 · Đủ nước để so (đã làm 2026-11-16)

Anh dặn 2026-11-16: các mục App phải có đủ nước để phân tích. Ô chọn nước của Tra keyword, Cây keyword, Săn app,
Soi 1 app và So sánh app đã tăng từ **5 lên 17 nước**, cùng bộ cờ đang có trong app:

- **Nói tiếng Anh:** US · GB · CA · AU · IN · PH
- **Châu Âu:** DE · FR · ES · IT
- **Mỹ Latinh:** BR · MX
- **Châu Á:** JP · KR · VN · TH · ID

App Store đã có mã storefront cho cả 17 nước, dùng cho gợi ý keyword. Giá ở KRW và IDR hiện không có số lẻ.

Review Mining dùng chung danh sách này, và cho chọn **nhiều nước cùng lúc**: review mỗi nước lưu riêng (khoá có `country`),
gộp lại khi xếp nỗi đau. Tab Review gốc lọc được theo nước. Bảng So app thêm chế độ **nỗi đau × nước** để thấy một vấn đề
nặng ở chợ nào.

**Giới hạn:** store vẫn đọc bằng `lang: 'en'`. Ở JP, KR, VN, TH, ID, BR, MX… review và gợi ý tiếng Anh ít hơn hẳn, và luật chê
chỉ hiểu tiếng Anh. Muốn đọc review tiếng địa phương thì cần thêm `lang` theo nước + bộ luật chê từng tiếng, để sau.

## 27.1 · Trang riêng trong menu App

- Thêm mục con **"Đào review"** vào menu App (`APP_SUB` ở `AppShell.tsx`), nằm sau "Soi 1 app", link `/?mode=reviews`.
- Ô nhập nhận: link Play / App Store, package / id, hoặc tên app (tìm như Soi 1 app). Thêm được **tối đa 10 app**.
  Chọn **1 hoặc nhiều nước** trong 17 nước (mặc định US), xem 27.0.
- Mở thẳng được bằng `/?mode=reviews&link=…&country=…`. Nút **Đào review** đặt ở Soi 1 app và ở thẻ app dẫn đầu của Săn app.
- Trang có 4 tab, xếp **1 cột** từ trên xuống:
  1. **Nỗi đau**: bảng xếp hạng, là tab mặc định.
  2. **Xin tính năng**
  3. **So app**: chỉ hiện khi có từ 2 app.
  4. **Review gốc**: Review Explorer.
- Đầu trang có 4 ô số: review đã đọc · review chê · nhóm nỗi đau · review mới từ lần trước.

## 27.2 · Thu review: lấy nhiều hơn + import

- **Play:** mặc định 200 review như cũ. Thêm nút **"Đọc sâu"** lấy 1.000 review mới nhất bằng `nextPaginationToken`,
  có nút Dừng. Phải đo thời gian thật rồi ghi vào trang này.
- **App Store:** giữ tối đa 100 review (Apple trả 429 nếu đọc nhiều). Lỗi thì ghi rõ lỗi và gợi ý import.
- **Import CSV / JSON:** cột bắt buộc `rating`, `text`. Cột tuỳ chọn: `date`, `version`, `country`, `helpful`, `reply`, `url`.
  Dòng hỏng thì bỏ và báo số dòng bỏ. Lưu với `source = 'import'`.
- **Thêm cột cho `review_seen`:** `helpful` (Play `thumbsUp`), `reply` (câu developer trả lời), `source` (`play` · `appstore` · `import`).
  Review cũ để trống, không bịa.
- **Chống trùng:** giữ khoá hash như cũ. Đọc lại hay import lại thì chỉ cập nhật `last_seen_at`.
- **Lọc** (ở tab Review gốc): sao 1–5, khoảng ngày, version, nguồn. Mặc định 1–3★. Bật 4–5★ để xem người dùng **thích** gì,
  tránh đề xuất bỏ đúng tính năng họ quý. Nếu bật thì phải lưu cả 4–5★, xem câu chốt 2.

## 27.3 · Điểm nỗi đau /100

Mỗi nhóm nỗi đau (loại chê + cụm chữ, đếm **số review khác nhau** như mục 26):

| Phần | Trọng số | Cách đo |
|---|---|---|
| Tần suất | 30 | Số review của nhóm ÷ tổng review chê đã đọc. Đạt 25% thì đủ điểm |
| Mức nặng | 30 | Lấy từ `severity` của loại chê sẵn có. Sao trung bình của nhóm ≤ 1,5 thì cộng thêm |
| Xu hướng | 20 | Tỉ lệ nhóm trong 30 ngày gần nhất so với phần còn lại (theo `date`). Dưới 20 review có ngày thì **chưa đo** |
| Chưa ai giải | 20 | Chỉ khi có ≥ 2 app: số app cùng bị chê nhóm này ÷ số app. 1 app thì **chưa đo** |

- Phần chưa đo thì bỏ khỏi mẫu số, không cho 0 điểm. Luật này giống mục 24.4.
- Nhóm dưới 3 người khác nhau thì vẫn hiện, nhưng gắn nhãn "ít bằng chứng" và không xếp vào top.
- Trọng số là **quy ước ShotMatic** (lấy từ bản đề xuất), chưa kiểm bằng app thật. ⓘ ghi rõ công thức và nguồn.
- Mỗi con số gắn 1 trong 3 nhãn: **Đo được** (đếm từ review), **Tính ra** (điểm, tỉ lệ), **AI suy luận** (tên cụm do AI đặt, thẻ cơ hội).

## 27.4 · Bằng chứng + sửa nhóm

- Bấm 1 nỗi đau là ra: số người, % trên review chê, sao trung bình, các version bị chê, 3 câu trích nguyên văn, rồi toàn bộ
  review của nhóm (nhảy sang tab Review gốc, đã lọc sẵn). Mỗi review có link về store nếu có.
- Nút **✦ Gom lại theo nghĩa** (tuỳ chọn, cần AI trên máy): gửi tên cụm + 3 câu trích của mỗi cụm cho AI, nhận lại lệnh
  "gộp cụm A vào B" và tên mới. **AI không được tạo review hay số.** Chỉ gộp các cụm đang có, số đếm lại bằng code.
- Sửa tay: gộp 2 nhóm, đổi tên nhóm. Lưu theo app + nước. Bấm "Về như cũ" để bỏ sửa.
- Một review được nằm trong nhiều nhóm. Ví dụ "slow and too expensive" vào cả Lỗi và Giá. Kiểm lại trong test.

## 27.5 · Xin tính năng + So app

**Xin tính năng:** gom câu "ước gì" thành danh sách: tính năng · số người xin · sao trung bình · app nào bị xin · câu trích.
Nếu đã có ma trận Feature Gap của các app này thì thêm cột "app nào đã có". Không đoán độ khó build, không đoán tiền.

**So app** (2–10 app): bảng nỗi đau × app, mỗi ô là % review chê của app đó. Dưới bảng có 3 dòng chữ, đều do code tính:

- **Chung:** nỗi đau có ở ≥ 60% số app. Đây là khoảng trống của cả chợ, nhưng vẫn phải kiểm có người trả tiền.
- **Riêng:** nỗi đau chỉ 1 app bị chê.
- **App yếu nhất / mạnh nhất** ở từng nỗi đau.

Đèn 🔴 "Chỉ chen được bằng giá" của mục 26.2 dùng lại ở đây.

## 27.6 · Tổng kết: nên nhắm vào đâu (viết + code 2026-11-17)

Anh hỏi 2026-11-17: trang đã ra nỗi đau của nhiều app một lúc, nhưng cuối trang chưa có phần đúc kết. Khối này trả lời
**"làm gì tiếp"** trong 10 giây, thay cho việc tự đọc 10–20 nhóm. Phần kết luận là **luật** (không AI), mỗi câu trỏ về nhóm và số đo có thật.
Khối nằm **ngay dưới 4 ô số**, trên các tab, xếp 1 cột.

1. **Câu kết luận** (thẻ lớn có màu):
   - 🟢 *Nên nhắm vào: {nỗi đau}* — {n} người · ở {a}/{N} app · điểm {s}/100.
   - 🟠 cùng câu đó nhưng kèm cảnh báo khi nhóm tiền lớn nhất (xem đèn đỏ dưới).
   - ⚪ *Chưa thấy chỗ đáng nhắm* — không nhóm nào (trừ tiền / khác) đạt ≥ 3 người.
2. **Đèn** (luật giống mục 26, ngưỡng là quy ước ShotMatic):

   | Đèn | Luật |
   |---|---|
   | 🔴 Chỉ chen được bằng giá | Loại Ép trả phí / giá lớn nhất (trừ Khác) **và** ≥ 35% review chê |
   | 🔴 Chưa thấy điểm làm khác | Không nhóm nào ngoài tiền / khác có ≥ 3 người |
   | 🟡 Ít review chê | Dưới 30 review chê → kết luận yếu, nên Đọc sâu hoặc thêm app |
   | 🟢 Việc hỏng lặp ở nhiều app | 1 nhóm ngoài tiền có ≥ 3 người, ở ≥ 2 app |
   | 🟢 Người dùng đang tự vá | ≥ 3 review chê nhắc *spreadsheet, excel, google sheets, notes app, pen and paper, switched to, went back to* |
   | 🟢 App bị phình | ≥ 3 review chê nhắc *too many features, cluttered, bloated, redesign, used to be simple, old version was better* |

3. **3 nỗi đau đáng nhắm:** 3 nhóm điểm cao nhất, ≥ 3 người, không phải tiền / khác. Mỗi dòng: tên · số người · số app · điểm ·
   1 câu trích. Khi có ≥ 2 app: **app bị chê nặng nhất** ở nhóm đó (tỉ lệ review chê của app thuộc nhóm).
4. **Người dùng khen (4–5★):** tối đa 5 cụm chữ lặp ≥ 3 lần, chỉ lấy từ **câu có chữ khen** (love, great, easy, best, helps, fun…) trong review 4–5★,
   kèm 1 câu trích. Bỏ cụm về tiền (pay, premium, gems…) và cụm trùng nhóm lời chê. App mới nên giữ những thứ này.
   Chưa có review 4–5★ thì ghi rõ.
5. **Cần kiểm thêm** (luôn có): review không đo được **bao nhiêu người đang tìm** và **có chịu trả tiền không**. Nút sang
   Tra keyword / Săn app. Xu hướng chưa đo thì nhắc Đọc sâu hoặc đọc lại sau.
6. **Làm tiếp:**
   - **Tạo Project**: tạo project loại App, thêm các app làm đối thủ + 3 nỗi đau làm item "lời chê" (có số người, điểm).
   - **✦ AI viết thẻ cơ hội**: gửi đúng các số + câu trích ở trên, nhận tối đa 3 thẻ (tên app · cho ai · vấn đề · MVP 3–5 tính năng ·
     cách thu tiền · cần kiểm gì). Nhãn **AI suy luận**, AI không được thêm số.
   - **Copy tổng kết** (Markdown).
7. **Xuất .md** có phần Tổng kết ngay đầu file. JSON có thêm `summary`.

**Xuất:** Markdown (báo cáo đọc được, có câu trích + link), CSV (review + nhóm), JSON (tất cả, kèm phiên bản luật).

## 27.7 · Mới từ lần trước (không chạy theo lịch)

Khi anh bấm đọc lại 1 app đã đọc, review có `first_seen_at` sau lần đọc trước được tính là **mới**. Hộp "Mới từ lần trước" ghi:
số review chê mới, nhóm nào tăng nhiều nhất, nhóm mới xuất hiện. Không chạy nền, không báo động.

## 27.8 · Kiểm độ đúng

- File `web/tests/fixtures/reviews-labeled.json` chứa khoảng 60 review thật (lấy từ `review_seen` trên máy), gán nhãn loại chê
  bằng tay. Test kiểm luật đúng ≥ 80% và kiểm review nhiều nhãn.
- Chạy thật 2 app: 1 app Play nhiều review ("habit tracker" dẫn đầu), 1 app iOS. So với kết quả Soi 1 app. Ghi số + thời gian
  vào trang này.

## Chia việc

1. DB: migration thêm `helpful`, `reply`, `source` cho `review_seen`, thêm bảng `review_group_edit` (gộp / đổi tên).
   `parsePlayReview` đọc `thumbsUp`, `replyText`.
2. `web/src/lib/review-mining.ts` (hàm thuần): nhóm, điểm /100 (27.3), xin tính năng, So app, "mới từ lần trước". Test kèm.
3. `web/src/lib/review-import.ts`: đọc CSV / JSON, báo dòng hỏng. Test kèm.
4. Máy chủ: `POST /api/reviews/read` (1–10 app, đọc sâu, có Dừng), `POST /api/reviews/import`, `GET /api/reviews/:app`.
5. Giao diện `web/src/client/ReviewMining.tsx` + 4 tab, chữ 3 ngôn ngữ, nút từ Soi 1 app / Săn app.
6. ✦ AI: gom lại theo nghĩa (27.4), thẻ cơ hội (27.6). Code kiểm từng dòng AI trả về.
7. Bộ xuất Review Mining trong `lib/export`.
8. Tool MCP `get_review_mining` (chỉ đọc) cho Claude Code.
9. Chạy 27.8, `npm run check` xanh, xem 960px + 1340px, sáng + tối.

## Anh chốt (2026-11-17)

Anh trả lời "theo mặc định, code":

1. Trang là mục con **"Đào review"** trong menu App (thẻ thứ 6 của trang App).
2. **Lưu cả 4–5★** để tab Review gốc xem được người dùng thích gì.
3. Bản đầu làm **27.1–27.4 + xuất báo cáo**. Tab Xin tính năng và So app hiện xám "Sắp có" (27.5). 27.7 hộp riêng để sau, riêng số "mới từ lần trước" đã có ở ô đầu trang. 27.6 làm ngày 2026-11-17 theo lời anh.

## Đã làm (2026-11-17)

- **DB** (migration `0029_review_mining`): `review_seen` thêm `helpful`, `reply`, `source`. Thêm bảng `review_mine_apps` (app đã đào theo nước, lần đọc cuối + lần trước) và `review_group_edits` (gộp / đổi tên nhóm theo bộ app).
- **Thu review** `web/src/collectors/review-mine.ts`: Play lật trang tới 1.000 review (Đọc sâu), có số người thấy hữu ích + câu developer trả lời. App Store dùng đường đọc sẵn có (tối đa 100). Ghi cả 1–5★, không ghi đè lần thấy đầu. Các chỗ cũ đọc lịch sử (`seenBefore`) tự lọc ≤ 3★.
- **Lõi** `web/src/lib/review-mining.ts` (hàm thuần): bỏ trùng cùng review ở nhiều nước, nhóm theo cụm chữ (1 review vào nhiều nhóm), điểm /100 với phần chưa đo bỏ khỏi mẫu số, áp sửa tay, nhóm dưới 3 người gắn "ít bằng chứng", xuất .md / .csv / .json, câu hỏi ✦ AI gợi ý gộp.
- **Import** `web/src/lib/review-import.ts`: CSV (ngoặc kép, xuống dòng trong ô) + JSON (mảng hoặc `{ reviews }`), nhận nhiều tên cột, bỏ dòng hỏng và đếm.
- **Máy chủ** `web/src/lib/review-mining-run.ts` + `web/src/server/reviews-api.ts`: `GET /api/reviews/apps`, `POST /api/reviews/read` (1–10 app × nhiều nước, lỗi từng ô ghi lại, nút Dừng hủy request), `/view`, `/import`, `/edit`.
- **Giao diện** `web/src/client/ReviewMining.tsx`: ô dán nhiều link, chọn nhiều nước, tick app đã đào để so cùng, Đọc sâu, import file; 4 ô số; tab Nỗi đau (thanh loại lời chê, xếp hạng có điểm, mở ra thấy Tính ra / Đo được / câu trích có link / sửa nhóm / ✦ AI) và tab Review gốc (lọc sao, chữ, app, nước, version, ngày, theo nhóm; 👍; câu developer trả lời). Mở thẳng bằng `/?mode=reviews&link=…&country=…`.
- **Test** `web/tests/review-mining.test.ts` (17 test). `npm run check` xanh 2026-11-17.

Chạy thật 2026-11-17 trên Habitica:

| Lượt | Thời gian | Review khác nhau | Review chê | Nhóm ≥ 3 người |
|---|---|---|---|---|
| Play, US + GB, 200 review mỗi nước | 4,5 giây | 199 (US và GB trả gần như cùng review) | 61 | 8 |
| Play, US, Đọc sâu | 7,4 giây | 979 | 216 | 24 |
| + App Store US (so cùng bản Play) | 10,2 giây | 100 bản iOS | 246 cả 2 app | — |

Nhóm đứng đầu khi so 2 bản: subscription 67, lost 66, bug 66. Phần "Chưa ai giải" đo được khi có 2 app.
Xem ở 960px và 1340px, không cuộn ngang cả trang. Chưa soát chế độ sáng.

**Vì sao đếm sau bỏ trùng:** lượt đầu đếm 398 review cho US + GB nên tỉ lệ chê ra 15%. Thật ra Play trả gần như cùng review ở 2 nước. Sau khi bỏ trùng còn 199 review, tỉ lệ đúng là 31%.

### 27.6 Tổng kết (code 2026-11-17)

- **Lõi** `web/src/lib/review-summary.ts` (hàm thuần): câu kết luận, 6 đèn, 3 nỗi đau đáng nhắm + app bị chê nặng nhất, lời khen 4–5★, phần Tổng kết cho file .md, câu hỏi ✦ AI thẻ cơ hội. `mineView` trả thêm `summary`.
- **Tạo Project** `POST /api/reviews/project`: project loại App, mỗi app thành item đối thủ, mỗi nỗi đau đáng nhắm thành item lời chê (ghi chú: số người · số app · điểm).
- **Giao diện** `web/src/client/ReviewSummary.tsx`: nằm dưới 4 ô số, xếp 1 cột: thẻ kết luận có màu, đèn, 3 nỗi đau (bấm "Xem review gốc" là sang tab Review gốc lọc đúng nhóm), khen, Cần kiểm thêm (link Tra keyword / Săn app), Làm tiếp (Tạo Project · Copy tổng kết · ✦ AI viết thẻ cơ hội). Chỉ đào 1 app thì không hiện số app / "bị chê nặng nhất".
- **Xuất:** .md có Tổng kết ngay đầu file, JSON có `summary`.
- **Test** `web/tests/review-summary.test.ts` (8 test). `npm run check` xanh 2026-11-17 (1.325 test).

Thử trên Habitica (Play US, Đọc sâu, 979 review): kết luận *Nên nhắm vào: lost* (Sync / tài khoản, 17 người, 8% review chê, điểm 58). Không đèn nào bật.
Lượt đầu, phần khen ra cả "subscription", "ads", "update" vì lấy cả câu trung tính. Sau khi chỉ lấy câu có chữ khen và bỏ cụm về tiền, phần khen còn
"no ads", "self improvement", "daily habits", "fun and motivating". Đã xem ở 960px và 1340px, không cuộn ngang. Chưa bấm Tạo Project trên dữ liệu thật (đã có test).

## Giới hạn

- Gom nhóm bằng luật chữ. ✦ AI chỉ gộp các cụm đã có, không tự tìm nhóm mới từ review.
- App Store chỉ lấy được 100 review mới nhất, nên xu hướng của app iOS thường "chưa đo".
- Chỉ đọc review tiếng Anh.
- Điểm /100 là quy ước, chưa đối chiếu với app thật thành công.
- ✦ AI gom lại chỉ gợi ý trong khung chat. Anh gộp bằng tay ở "Sửa nhóm", app chưa tự áp lệnh của AI.
- Chưa có file 60 review gán nhãn tay (27.8).
- Tên nhóm là cụm chữ thô (vd. "lost"), nên câu kết luận đọc chưa mượt. Đổi tên nhóm ở "Sửa nhóm" thì kết luận đổi theo.
