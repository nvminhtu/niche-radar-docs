# 24 · Săn app cầu > cung + gom nhóm tính năng App

> Plan 2 · mục 24. Bên App có 5 tính năng ngang hàng (Keyword · Explorer · Projects · So sánh app · AI Agent), nhưng chưa có
> chỗ nào **tự gom nhiều keyword rồi lọc ra chỗ cầu > cung** như Săn kênh nhỏ (YouTube) hay Săn sách (KDP). Mục này thêm
> **Săn app** (phễu 100 → 10 → 3) và gom menu App thành nhóm theo việc, giống khuôn mục 23 của YouTube.

<span class="chip chip--doing">Viết 2026-11-15 · code 2026-11-16 theo 3 mặc định bên dưới · chờ anh soát</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Mục này ghi lại yêu cầu anh đưa ra ngày 2026-11-15. Chỉ code khi anh chốt.
</div>

## Vì sao làm

Anh hỏi (2026-11-15): phần keyword, explorer bên App đã gom thành 1 nhóm như YouTube chưa, và muốn có thêm mục săn app
có **Demand > Supply**.

Trả lời: **chưa gom**. Nhãn Cầu > cung cho app đã code ở mục 22.3, nhưng chỉ hiện trong So sánh app, trên 1 keyword anh
tự gõ. Chưa có phễu nào tự tìm keyword cầu > cung từ 1 chủ đề.

## Đang có gì (đọc code 2026-11-15)

- **Menu** (`web/src/components/AppShell.tsx`): nhóm "Tính năng chính" có 5 mục ngang hàng: Keyword · Explorer · Projects ·
  So sánh app · AI Agent. YouTube · Amazon · KDP nằm ở nhóm "Tính năng khác".
- **Explorer** (`web/src/lib/explore.ts`): gõ 1 chủ đề → cây keyword con lấy từ gợi ý store + Google. Mỗi keyword đã có
  số nhẹ: `popularity_score` (0–100, tính từ hạng trong ô gợi ý), số app Play / App Store, rating top 5 App Store và mức
  `crowding` (low · medium · high).
- **Research** 1 keyword: đọc top app Play + App Store + Trends, có ngày ra mắt và số rating từng app.
- **Nhãn Cầu > cung** (`web/src/lib/app-demand-supply.ts`, mục 22.3, có test): keyword được 🔥 khi top 10 có app ra mắt
  dưới 1 năm, ≥ 50 rating, và keyword có người gõ (có trong gợi ý store hoặc Trends có số). Hàm thuần, dùng lại được.

## Đã đo (2026-11-15 · DB máy dev `web/data/niche.db`, chỉ đọc)

| Số | Giá trị | Nghĩa là |
|---|---|---|
| Thời gian 1 lượt Explorer | trung bình **317 giây** (153–422 giây, 5 lượt) | Bước 1 mất khoảng 5 phút |
| Số keyword / lượt Explorer | trung bình **88** (nhiều nhất 201) | Đủ cho bước 1 "100 keyword" |
| Keyword có `crowding = high` | **1.163 / 1.734** (67%) | Lọc theo crowding bỏ được 2/3 ngay ở bước 1 |
| Thời gian 1 lượt Research | trung bình **93 giây** (275 lượt) | Bước 2 tra 10 keyword chạy lần lượt mất khoảng 15 phút |
| Nguồn chậm nhất trong Research | Play Store **95 giây**; App Store 12 giây; Trends 13 giây | Play là nút thắt khi chạy nhiều luồng |
| Lượt Research có app dưới 1 năm vào top 10, ≥ 50 rating | **144 / 294** (đo ở mục 22) | Tín hiệu 🔥 có thật, nhưng phải lọc ở bước 1 để khỏi ra quá nhiều |

**Chưa đo:** chạy 3 lượt Research cùng lúc có làm Play Store chặn hay chậm hơn không.

## 24.1 · Gom nhóm tính năng App

Menu bên trái đổi nhóm "Tính năng chính" thành các mục theo việc (giống 3 nhóm YouTube ở mục 23):

| Nhóm | Mục con | Ghi chú |
|---|---|---|
| 🔍 **Tìm ngách** | Keyword · Explorer | 2 trang cũ, giữ nguyên route `/` và `/?mode=explore` |
| 🎯 **Săn app** | Săn app cầu > cung | Trang mới `/hunt-apps` (xem 24.2) |
| 🔬 **Soi app** | So sánh app | Route cũ `/compare/competitors`. Sau này thêm "Soi 1 app" nếu cần |
| 📁 Projects | (mục đơn) | Giữ riêng vì project gom cả app, YouTube lẫn sách |
| ✦ AI Agent | (mục đơn) | Giữ riêng vì AI Agent chạy hết các bước, không thuộc 1 nhóm |

- Nhóm có mục con thì mở / gập như nhóm "Cài đặt" và "Hướng dẫn" đang có (`SideNav` đã hỗ trợ `children`).
- Nhóm đang chứa trang anh đang xem thì tự mở.
- **Không đổi route.** Link cũ, lịch sử, MCP vẫn chạy như cũ.
- Thanh dính trên trang thêm 1 nấc nhóm: `Tìm ngách / Explorer / <chủ đề>`.

## 24.2 · Trang Săn app: phễu 100 → 10 → 3

Gõ **1 chủ đề** (vd "habit tracker", "pdf scanner") + chọn nước. Trang chạy 3 bước, giống Săn kênh nhỏ và Săn sách:

### Bước 1 · Gom 100 keyword (Explorer, khoảng 5 phút)

- Chạy Explorer cho chủ đề đó. Nếu chủ đề + nước đã có lượt Explorer dưới 7 ngày thì dùng lại, không chạy lại.
- Lọc bằng số nhẹ đã có, **không gọi thêm**:
    - giữ keyword có `popularity_score` ≥ 40 (có người gõ),
    - bỏ keyword `crowding = high` (top 5 App Store quá nhiều rating),
    - bỏ keyword trùng nghĩa (chỉ khác số nhiều / thứ tự từ).
- Xếp theo `popularity_score` cao trước, crowding thấp trước. **Tick sẵn 10 keyword đầu** cho bước 2, anh bỏ tick / tick thêm được (tối đa 20).
- Mỗi hàng: keyword · thanh popularity · chấm crowding · số app Play / App Store.

### Bước 2 · Research 10 keyword (khoảng 5–15 phút)

- Chạy Research cho từng keyword đã tick. Keyword đã có Research dưới 7 ngày thì dùng lại.
- Chạy **3 lượt cùng lúc** (dùng chung hàng chờ máy chủ của mục 23 nếu mục 23 code trước; nếu chưa thì chạy lần lượt).
  10 keyword × 93 giây ÷ 3 luồng ≈ 5 phút. Chạy lần lượt ≈ 15 phút.
- Mỗi keyword xong thì hàng đó hiện nhãn Cầu > cung ngay, không đợi hết.
- Rời trang vẫn chạy tiếp. Quay lại thì thấy đúng tiến độ.

### Bước 3 · Chốt 3 keyword (không gọi thêm)

Chấm **điểm Săn app /100** cho mỗi keyword đã Research. Ngưỡng là **quy ước ShotMatic**, không phải số store công bố:

| Phần | Điểm | Cách tính |
|---|---|---|
| Có người gõ | 30 | `popularity_score` × 0,3 |
| Trends | 20 | Có số Trends > 0 trong 12 tháng = 10, đang lên (3 tháng gần > 3 tháng trước) = thêm 10 |
| App mới leo được | 30 | Số app dưới 1 năm, ≥ 50 rating trong top 10: 1 app = 20, ≥ 2 app = 30 |
| Cung còn chỗ | 20 | Rating trung vị top 10: dưới 1K = 20 · 1K–10K = 10 · ≥ 10K = 0 |

- Chốt **3 keyword điểm cao nhất**, mỗi keyword 1 thẻ: nhãn 🔥 / có cầu chưa nổ / cung đầy · điểm · tên app mới đang leo
  (link store, ngày ra mắt, số rating) · Research #id làm căn cứ.
- Các keyword còn lại xếp bên dưới, 1 cột, có điểm.
- Mỗi thẻ có 3 nút:
    - **Mở Research**: mở trang Keyword đã có.
    - **So sánh app**: mở So sánh app với 2–4 app top của keyword đó (mục 20 / 22).
    - **Gom vào project**: tạo hoặc thêm vào project, ghi điểm + căn cứ.
- **Tuỳ chọn** (như Săn kênh nhỏ): chỉnh ngưỡng popularity (40 · 20 · 60), bỏ / giữ crowding high, số keyword tick sẵn (10 · 5 · 20).
  Đổi ngưỡng thì xếp lại ngay trên máy, không gọi lại máy chủ.

### Giao diện

- Theo luật trang kết quả: thẻ kết luận "1 câu + số lớn + hình", ít chữ, giải thích gập vào ⓘ (mẫu: YouTube Soi kênh, Săn sách).
- Thanh 3 chấm tiến độ (Gom · Research · Chốt) ở đầu trang, như Săn kênh nhỏ.
- Xếp **1 cột từ trên xuống**. Chỉ chip số ngắn mới được nằm ngang.

## 24.3 · AI dùng qua MCP (tuỳ chọn, làm sau)

- Thêm tool `app_hunt` (chạy phễu, trả mã việc) và `get_app_hunt` (đọc kết quả), giống `youtube_hunt`.
- Chỉ làm khi 24.1 + 24.2 chạy ổn.

## 24.4 · Sửa cách chấm (2026-11-16)

<span class="chip chip--doing">Viết + code 2026-11-16 · chờ anh soát</span>

Anh soát kết quả chủ đề "habit tracker" và hỏi tiêu chí lấy ở đâu. Trả lời thẳng: điểm /100 ở 24.2 là **quy ước tự đặt**,
không lấy từ chuẩn nào. Các tool lớn cũng giấu công thức: AppFollow chỉ nói "hơn 15 tham số", Sonar không tiết lộ, Mobile Action cũng vậy.
Con số "chính thức" duy nhất là Popularity 5–100 của Apple, lấy qua Apple Search Ads. Mình không có nguồn này.

### Lỗi thấy được trên kết quả thật

| Lỗi | Ví dụ | Sửa |
|---|---|---|
| 2 keyword cùng 1 niche chiếm 2 suất top 3 | "habit tracker game" (#2) và "habit tracker rpg" (#3) cùng có Monke, Levla | Bỏ trùng theo **app chung**, không chỉ theo chữ |
| Thiếu tín hiệu "tên app có keyword" | — | Thêm phần mới (Sonar coi đây là tín hiệu chính của độ khó) |
| Không biết đối thủ có thu được tiền không | — | Thêm phần mới, lấy từ giá và IAP đã đọc |
| Cùng tên app nhưng 2 số khác nhau | Levla 82 ngày · 139★ và 145 ngày · 1.2K★ | Không sai: bản App Store ra mắt 2026-08-26, bản Play ra mắt 2026-06-23 (DB máy dev). Thêm **icon store** lên chip |
| "Có người gõ" bị hiểu là lượt tìm | — | Đổi nhãn thành **Store gợi ý**. ⓘ ghi rõ đây là hạng trong ô gợi ý |

### Điểm mới /100

| Phần | Điểm | Cách tính | Học từ |
|---|---|---|---|
| Store gợi ý | 20 | `popularity_score` × 0,2 | Thay cho Apple Popularity (mình không có) |
| Google Trends | 15 | Có số = 8, 3 tháng gần cao hơn 3 tháng trước = thêm 7 | — |
| App mới leo được | 25 | App dưới 1 năm, ≥ 50 rating trong top 10: 1 app = 15, ≥ 2 app = 25 | Quy ước ShotMatic (mục 22.3) |
| Cung còn chỗ | 15 | Rating trung vị top 10: dưới 1K = 15, dưới 10K = 8 | Sonar, AppFollow: số review của app top |
| Tên app chưa chiếm keyword | 15 | % app top 10 có đủ chữ của keyword trong tên: ≤ 20% = 15, ≤ 50% = 8, còn lại = 0 | Sonar: title match ratio |
| Có người trả tiền | 10 | App top 10 bán giá hoặc có IAP: ≥ 3 app = 10, 1–2 app = 5, 0 = 0 | Phần "Tiền" của điểm v2 |

- App có cả bản Play lẫn App Store thì tính là **1 app** (gộp theo tên).
- **Lời chê không tính điểm.** Review chỉ có khi anh đã bấm "Đọc review" (mỗi keyword tới 4 phút). Nếu tính điểm thì keyword
  chưa đọc review sẽ bị thiệt. Đã có review thì thẻ hiện thêm 1 chip: lời chê đứng đầu và số review đã đọc.
- **Bỏ trùng:** xếp theo điểm. Keyword có ≥ 2 app mới chung, hoặc ≥ 60% app top 10 trùng với 1 keyword điểm cao hơn, thì không
  vào top 3. Nó xuống danh sách dưới với nhãn "giống <keyword>".
- Ngưỡng vẫn là quy ước, chưa kiểm bằng app thật thành công. ⓘ ghi rõ phần nào học từ đâu.

### Thêm khi code: phần chưa đo không chấm 0

Lúc soát mới thấy: Research **không đọc IAP của App Store**. Ở các lượt #298–#301, 445/445 app App Store để trống IAP, và #298, #299 không có dữ liệu Play.
Chấm 0 cho "Có người trả tiền" lúc đó là sai. Sửa như sau:

- IAP iOS lấy thêm từ cache gói IAP đã đọc (giống trục Tiền của điểm v2).
- Phần nào **chưa đo** (tiền, tên app, cung còn chỗ) thì hiện "chưa đo" và bỏ khỏi mẫu số. Tổng = điểm đã đo × 100 ÷ điểm tối đa đã đo.

### Kết quả thật (chủ đề "habit tracker", US, DB máy dev, 2026-11-16)

| Keyword | Điểm cũ (24.2) | Điểm mới (24.4) | Ghi chú |
|---|---|---|---|
| habit tracker cute | — | **84** · #1 | Có chip lời chê "subscription" (đã đọc review) |
| habit tracker game | 83 · #2 | **83** · #2 | |
| habit tracker offline | — | **65** · #3 | |
| habit tracker rpg | 75 · #3 | 76 · không vào top 3 | Nhãn "giống habit tracker game" (chung Monke, Levla) |

### Chia việc 24.4

1. `web/src/lib/app-hunt.ts`: `huntScore` 6 phần, `titleShare`, `payingCount`, `sameNiche` + test trong `tests/app-hunt.test.ts`.
2. `web/src/lib/app-hunt-run.ts`: tính tên app, tiền, chip lời chê (nếu đã có review) cho từng keyword. Đánh dấu trùng.
3. `web/src/client/AppHunt.tsx`: 6 thanh, nhãn mới, icon store trên chip, chip lời chê, nhãn "giống …". Chữ 3 ngôn ngữ.
4. `npm run check` xanh. Xem tận mắt 1340px với chủ đề "habit tracker".

## Câu chờ anh chốt

| # | Câu hỏi | Mặc định nếu anh không chọn |
|---|---|---|
| 1 | Gom ở **menu bên trái** (route giữ nguyên), hay làm **1 trang App có 3 thẻ nhóm** như trang YouTube? | Menu bên trái: ít việc, không đổi link |
| 2 | Bước 2 tick sẵn **10 keyword** (khoảng 5 phút nếu 3 luồng), hay 20 keyword (khoảng 10 phút)? | 10 |
| 3 | Đợi mục 23 xong hàng chờ máy chủ rồi dùng chung, hay làm Săn app trước, chạy lần lượt? | Làm sau mục 23, dùng chung hàng chờ |

## Chia việc

1. **24.1** Gom menu: `AppShell.tsx` (nhóm + mục con), chữ 3 ngôn ngữ (`en` · `vi` · `es`), sửa `tests/ui-shell.test.ts`.
2. **Hàm chấm** `web/src/lib/app-hunt.ts` (thuần): lọc bước 1, điểm /100 bước 3, tuỳ chọn ngưỡng. Test ở `tests/app-hunt.test.ts`
   với số từ 3–4 lượt Explorer / Research thật trong DB máy dev.
3. **Máy chủ** `web/src/server/app-hunt-api.ts`: tạo lượt săn, chạy Explorer (hoặc dùng lại), chạy Research các keyword đã tick,
   lưu tiến độ để rời trang vẫn chạy. Bảng mới `app_hunts` (chủ đề, nước, keyword đã tick, trạng thái) + migration.
4. **Trang** `web/src/client/AppHuntPage.tsx`: 3 bước, thẻ chốt, Tuỳ chọn, 3 nút mỗi thẻ.
5. Chạy thật 2 chủ đề (vd "habit tracker" US, "pdf scanner" US). Đo thời gian 1 · 3 luồng Research, ghi vào mục **Đã đo**.
   Xem tận mắt 960px và 1340px, sáng + tối, English + tiếng Việt.

## Giới hạn

- Điểm /100 và các ngưỡng là quy ước tự đặt, chưa kiểm bằng app thật thành công. Ghi rõ ở ⓘ.
- `popularity_score` đo **thứ hạng trong ô gợi ý**, không phải số lượt tìm. Keyword hiếm vẫn có thể lên hạng 1 cho chính chữ đầu của nó.
- Play Store là nguồn chậm nhất (95 giây). Chạy nhiều luồng có thể bị chặn. Chưa đo.
- Chưa tách Free / PRO. Ghi chú cho sau: Free 1 lượt săn / ngày, PRO không giới hạn.
- 24.4 "Có người trả tiền" thường là **số tối thiểu**: app iOS chỉ được đếm khi đã đọc gói IAP. Muốn đủ thì Research phải đọc IAP App Store (chưa làm).
- 24.4 "Tên app chưa chiếm keyword" gần như luôn đạt tối đa với keyword 3 chữ trở lên ("habit tracker offline"), vì ít tên app chứa đủ cả 3 chữ.
  Phần này mạnh nhất ở keyword 1–2 chữ.
