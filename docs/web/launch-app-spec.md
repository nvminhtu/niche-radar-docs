# Launch · Spec: 1 điểm cơ hội, Độ khó, Tiền

> Spec cho [Launch · Brief](launch-app-brief.md) (anh chốt 2026-11-17). Số căn cứ ở [Bước 0 hiểu sâu](launch-app-hieu-sau.md).
> Đọc code 2026-11-17. Anh duyệt spec → mới chia task (plan).

<span class="chip chip--doing">Viết 2026-11-17 · anh duyệt theo mặc định 2026-11-17 · plan viết 2026-11-17</span>

<div class="box box--goal" markdown>
**Tóm tắt**

- **Không viết điểm thứ 5.** Nâng **sức khoẻ v2** thành điểm chính, vì nó đã có sẵn trọng số, phần "chưa đo", ngưỡng,
  nguồn từng yếu tố, và đang được Bàn quyết định, Project, MCP, export dùng.
- Đổi 3 chỗ trong v2: **thêm yếu tố Cửa vào** (app mới leo được, nặng nhất) · **tách Cạnh tranh ra thành thẻ Độ khó** ·
  **làm lại Tiền** (gói IAP iOS + giá + TrustMRR).
- Hiện **/100** thay /10. v1 (Explorer), điểm Săn app, điểm keyword (mục 10) **thôi hiện như điểm quyết định**.
- Mọi lần đổi công thức phải qua **bộ kiểm điểm**: 14 niche kiếm tiền + ~15 niche chết.
</div>

## Thứ tự làm

| # | Khối | Vì sao trước |
|---|---|---|
| S1 | Bộ kiểm điểm | không có nó thì không biết đổi điểm là tốt lên hay xấu đi |
| S2 | Yếu tố Cửa vào + trọng số mới + thang /100 | sửa lỗi lớn nhất của B0.1 |
| S3 | Thẻ Độ khó | đi cùng S2 (Cạnh tranh rời khỏi điểm) |
| S4 | Tiền: IAP iOS trong Research + giá + TrustMRR | câu khách hỏi nhiều, đang yếu nhất |
| S5 | 1 điểm ở mọi trang | sau khi điểm đã đúng |
| S6 | Gom phần app đang dở | soát + commit, không viết thêm |

## S1 · Bộ kiểm điểm

**Mục tiêu:** sau mỗi lần đổi công thức, chạy 1 lệnh để biết niche kiếm tiền có còn bị chê không, và niche chết có bị khen không.

- **File:** `web/src/lib/score-bench.ts` (hàm thuần, có test) + lệnh `npm run score:bench` ở `web/`.
  Lệnh này đọc DB **chỉ đọc**, chấm lại bằng code hiện tại và in bảng.
- **Nhóm kiếm tiền (14):** keyword ở B0.1, kèm slug TrustMRR + doanh thu 30 ngày + ngày đọc.
  Chạy lại "workout tracker" vì lượt #332 bị dừng; chạy lại Play cho vignette, keyboard themes, make friends.
- **Nhóm chết (~15), chọn bằng luật ghi trong file**, không chọn bằng cảm giác:
    - lấy từ các lượt Research US đã có;
    - **≥ 70% app top 10 bỏ bê > 1 năm**, **0 app top 10 thu tiền** (không giá, không IAP, không gói IAP iOS), **không có app nào dưới 1 năm** trong top 10;
    - không trùng nhóm kiếm tiền; mỗi keyword ghi số lượt Research.
    - Không đủ 15 thì ghi rõ thiếu, không nới luật.
- **In ra:** từng keyword: điểm, kết luận, điểm từng yếu tố · trung vị mỗi nhóm · cách biệt.
- **Đạt khi:** nhóm kiếm tiền **0 cái BỎ** · trung vị kiếm tiền cao hơn trung vị chết **≥ 15 điểm** · nhóm chết **0 cái BUILD**.
- **Test:** `web/tests/score-bench.test.ts` với dữ liệu giả (không đọc DB thật): tính trung vị, cách biệt, luật chọn nhóm chết.

## S2 · Điểm cơ hội /100

Sửa trong `web/src/lib/score-v2.ts` + `score-config.ts`. Giữ cấu trúc `Factor` (giá trị 0–10, nguồn, công thức, độ tin).

### Yếu tố mới: Cửa vào (`entry`)

Dùng lại `demandSupply()` của mục 22.3 (`app-demand-supply.ts`): app top 10 có ngày ra mắt, app dưới 1 năm, app đủ 50 rating.

| Tình huống trong top 10 (2 store, gộp app trùng tên) | Điểm /10 |
|---|---|
| ≥ 2 app dưới 1 năm, mỗi app ≥ 50 rating | 10 |
| 1 app dưới 1 năm, ≥ 50 rating | 7 |
| có app dưới 1 năm nhưng < 50 rating | 4 |
| không app nào dưới 1 năm | 1 |
| không app nào có ngày ra mắt | chưa đo |
| cộng thêm: ≥ 30% app bỏ bê > 1 năm | +1 (tối đa 10) |

Nguồn hiện ra: tên từng app mới, tuổi (ngày), số rating, store, link.

### Trọng số mặc định mới

| Yếu tố | Cũ | Mới | Ghi chú |
|---|---|---|---|
| Cửa vào (mới) | — | **25** | tín hiệu tách được nhất ở B0.1 |
| Tiền | 25 | **25** | công thức mới ở S4 |
| Đau | 15 | 15 | giữ |
| Nhu cầu (Trends TB) | 10 | 10 | giữ |
| Xu hướng (Trends lên/xuống) | 10 | 10 | giữ |
| Tiếp cận khách (tự chấm) | 15 | 10 | |
| Hợp sức mình (tự chấm) | 10 | 5 | |
| Cạnh tranh | 15 | **0 → thẻ Độ khó** | ngược hướng ở B0.1 |

- 4 bộ mẫu (Mac, iOS, Android, SaaS) đổi theo cùng hướng: thêm Cửa vào, bỏ Cạnh tranh.
- **Trọng số anh đã lưu** ở Cài đặt: giữ nguyên số anh đặt, chỉ thêm Cửa vào = 25, Cạnh tranh về 0. Hiện 1 dòng báo đã đổi.
- Con số trên là **điểm xuất phát**. Chốt sau khi chạy S1. Nếu S1 chưa đạt, chỉnh trọng số, không chỉnh ngưỡng trước.

### Thang /100 và kết luận

- Điểm = trung bình có trọng số các yếu tố **đã đo** × 10, làm tròn. Ví dụ: 6,4/10 → **64/100**.
- Ngưỡng: BUILD ≥ 60 · TEST THÊM ≥ 40 · dưới 40 là BỎ (giữ 6 / 4 cũ × 10). Anh vẫn sửa được ở Cài đặt.
- Đo dưới 60% trọng số → tối đa TEST THÊM, ghi "mới đo X%" (giữ luật cũ).
- 5 cờ chặn giữ nguyên.
- **Lịch sử điểm cũ** (bảng `score_history`, thang /10): hiện × 10 kèm chú thích "công thức cũ trước 2026-11-xx", không tính lại.

## S3 · Thẻ Độ khó

Không cộng, không trừ vào điểm cơ hội. Hiện ngay cạnh điểm: **"64 / 100 · Độ khó: Khó"**.

| Mức | Khi nào |
|---|---|
| Khó | tổng rating top 10 ≥ 1 triệu **hoặc** rating trung vị ≥ 10.000 |
| Dễ | tổng rating top 10 < 50.000 **và** rating trung vị < 1.000 |
| Vừa | còn lại |
| chưa đo | không có rating |

Bấm mở ra 3 dòng **"khó vì sao"**:

- 3 app nhiều rating nhất (số rating, link).
- Tên app đã chiếm keyword: x/10 app có đủ chữ của keyword trong tên (dùng `titleShare()` mục 24.4).
- App bỏ bê > 1 năm: x% ("chỗ hở").

Ngưỡng là **quy ước của ShotMatic**, ghi ở ⓘ. Chạy S1 xem 2 nhóm phân bố ra sao rồi mới chốt.

## S4 · Tiền

### Đọc gói IAP iOS ngay trong Research

- Sau khi nguồn **App Store** tìm app xong, đọc tiếp trang `apps.apple.com` của **app App Store top 10** bằng `iosIapItems()`
  có sẵn (cache 7 ngày, giới hạn 1 lần / 2 giây). Tiến độ hiện "đọc gói IAP 3/10".
- Lỗi 429 khi đọc IAP **chỉ dừng phần đọc IAP**, lượt App Store vẫn xong. Lỗi 1 app thì bỏ app đó.
  (Plan đổi từ "nguồn `iap` riêng" sang cách này vì thêm 1 nguồn mới đụng hơn 12 file, 2026-11-17.)
- Thời gian: tối đa 10 trang × 2 giây ≈ **20 giây** thêm vào lượt App Store (trung bình 12 giây), vẫn ngắn hơn Play (95 giây).
  **Chưa đo thật.** Đo trên 5 lượt khi code xong.
- Đạt khi: ≥ 80% app top 10 App Store biết có IAP hay không (hiện 0%).

### Công thức Tiền mới (/10)

| Phần | Cách tính | Tối đa |
|---|---|---|
| Có người trả tiền | tỷ lệ app top 10 thu tiền (giá > 0 / IAP / gói IAP iOS) × 4 | 4 |
| Mức giá | gói IAP iOS đắt nhất, lấy trung vị giữa các app: ≥ $9,99 → 3 · ≥ $4,99 → 2 · > 0 → 1 | 3 |
| Doanh thu thật | app TrustMRR cùng niche: doanh thu 30 ngày ≥ $10k → 3 · ≥ $1k → 2 · > 0 → 1 | 3 |

- Phần nào chưa đo thì **bỏ khỏi mẫu số** của yếu tố, như cách cả điểm đang làm.
  Ví dụ: chưa có TrustMRR → Tiền = (phần 1 + phần 2) / 7 × 10.
- Không đo được cả 3 → Tiền "chưa đo".
- Play không cho giá gói IAP, nên phần Mức giá chỉ dựa vào iOS. Ghi rõ điều này ở ⓘ.

### Khớp TrustMRR

- Dùng cache category TrustMRR có sẵn (`trustmrr_cache`, quét 31 category, 7 ngày).
- Thẻ TrustMRR khớp khi tên hoặc mô tả có **đủ các chữ chính** của keyword (cùng cách tách chữ với `titleShare`),
  **hoặc** tên trùng 1 app top 10.
- Hiện **"app cùng niche đang thu $X–$Y / 30 ngày"**: n app, link từng app, ngày đọc.
  ShotMatic **không tự ước** doanh thu.
- Khớp sai là chuyện có thể xảy ra: mỗi dòng có link tới trang TrustMRR để tự kiểm. Nút "không phải niche này" làm sau, nếu bộ kiểm cho thấy khớp sai nhiều.

## S5 · 1 điểm ở mọi trang

| Trang | Hiện giờ | Sau |
|---|---|---|
| Research (đầu trang + khối Sức khoẻ) | v2 /10 + v1 | **điểm /100 + Độ khó + BUILD / TEST / BỎ**, 7 hàng theo 7 câu (chấm + thanh, chữ dài gập vào ⓘ) |
| Bàn quyết định, Project, So sánh | v2 /10 | điểm /100, cùng hàm |
| Săn app | điểm Săn app /100 | điểm Săn app thành **"lọc nhanh"** (chỉ để xếp hàng, không hiện số /100). Thẻ đã chạy Research thì hiện điểm chính |
| Explorer | điểm v1 | chữ **"ước sơ bộ"** (chỉ Cầu + Cung), không ghi /100. Nút "Research để có điểm" |
| Keyword Intelligence (mục 10) | điểm cơ hội 6 chiều | đổi tên **"điểm keyword (ASO)"**. Keyword đã Research thì hiện thêm điểm chính |
| MCP (`get_niche_card`, `get_decision`), export | v2 /10 | /100, kèm `formulaVersion: 2026-11` |

- 7 hàng ở Research: Cầu (Nhu cầu + Xu hướng) · Cung (Độ khó) · Cửa vào · Nỗi đau · Tiền · Khác biệt (link Feature Gap, không chấm) · Hợp mình (Tiếp cận + Hợp sức, tự chấm).
- Thêm dòng **"ShotMatic đo gì / không đo gì"** ở ⓘ: không có lượt tìm, lượt tải, lịch sử hạng.
- Giao diện theo luật repo: đứng được từ 960px, sáng + tối, có English. Soát 960 + 1340px.

### Free / PRO (theo brief)

| | Free | PRO |
|---|---|---|
| Điểm /100 + Độ khó | có | có |
| 7 hàng | chấm mức | + công thức, nguồn, app dẫn chứng |
| Tiền | 1 dòng "có người trả tiền: có / chưa đo" | gói, giá, TrustMRR |
| BUILD / TEST / BỎ | khoá (chip PRO `verdict` có sẵn) | có |

## S6 · Gom phần app đang dở

Không viết thêm tính năng. Mỗi phần: chạy `npm run check` + mở xem tận mắt → commit riêng.

- Mục 26 Điểm yếu đối thủ · 27.0 Review Mining (đã commit e49df96, chưa push) · 28 Cài đặt dữ liệu · Soi app cùng studio + tương tự · Tìm app + Tóm tắt app.
- Mục 16 Trang Project (nhánh riêng): xem câu 1 bên dưới.
- Mục 29 Săn việc làm tay (spec mới 2026-11-17): **để sau launch**, trừ khi anh muốn khác.

## Không đổi

- Collector Play, App Store, Trends: không đổi cách đọc.
- 5 cờ chặn, Bàn quyết định 5 trục long-tail, AI Agent 7 bước: chỉ đọc điểm mới, không đổi luồng.
- Giá PRO 39,99 USD.

## Rủi ro

- **Khớp quá vừa 14 niche:** cách chặn là nhóm chết và luật chọn ghi sẵn. Ghi cả kết quả xấu.
- **App Store 429 khi đọc IAP:** nguồn `iap` lỗi thì Tiền chỉ còn phần 1 và 3, ghi "chưa đo" ở phần giá. Không chặn lượt.
- **Điểm cũ đổi nghĩa:** Project và tracking đang lưu /10. Hiện × 10 với chú thích, không tự tính lại lượt cũ.
  Có nút "chấm lại bằng công thức mới" cho từng lượt.

## Đo xong khi

| Đo gì | Bây giờ | Đạt |
|---|---|---|
| Niche kiếm tiền bị bảo BỎ (`score:bench`) | 8 / 13 | 0 / 14 |
| Cách biệt trung vị: kiếm tiền so với chết | chưa có nhóm chết | ≥ 15 điểm |
| Niche chết được BUILD | chưa có | 0 |
| App top 10 App Store biết IAP | 0% | ≥ 80% |
| Số trang hiện điểm quyết định khác nhau | 4 | 1 |
| `npm run check` + `npm run docs:build` | — | xanh |

## Anh đã chốt 3 câu (2026-11-17, theo mặc định)

| # | Câu hỏi | Đã chốt |
|---|---|---|
| 1 | Mục 16 Trang Project (nhánh riêng, chưa merge): đưa vào launch hay bỏ? | **Để sau launch**, giữ nhánh |
| 2 | Hiện điểm /100 (thay /10) ở mọi trang? | Có |
| 3 | Bộ kiểm điểm: được chạy thêm ~5 lượt Research (workout tracker + chạy lại Play 3 lượt + niche chết nếu thiếu)? | Có |

Plan: [Launch · 1 điểm cơ hội](../superpowers/plans/2026-11-17-launch-1-diem-co-hoi.md) (12 task, S1 trước).
