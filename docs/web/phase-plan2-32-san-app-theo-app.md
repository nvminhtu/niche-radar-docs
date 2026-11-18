# 32 · Săn app theo app: ra 1 app đáng bắt chước

> Plan 2 · mục 32. Săn app có 2 tab: **Theo keyword** (đang có) và **Theo app** (mới).
> Tab Theo app dùng chung lượt săn: gom mọi app trong top 10 các keyword đã Research → bỏ trùng → lọc → chấm
> **"Đáng bắt chước" /100** → ra **1 app** để soi kỹ, kèm 2 app xếp sau.

<span class="chip chip--todo">Spec 2026-11-17 · anh đã duyệt thiết kế · chưa code</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Mục 26–30 cũng chưa commit hết. Nên gom và commit chúng trước rồi mới code mục này.
</div>

## Vì sao làm

Anh hỏi 2026-11-17: *"Tôi tưởng cái này hunting theo apps có chứa các từ khóa đó rồi gom nhóm, kết quả cuối cùng là 1 app để phân tích kĩ… phân theo keyword cũng được nếu user muốn, nên làm 2 tab."*

Hiện Săn app chỉ đi theo keyword ([mục 24](phase-plan2-24-san-app-cau-cung.md)): gom 100 keyword → Research 8–10 → ghim 3 keyword.
Ý "chấm đối thủ đáng bắt chước" đã ghi từ 2026-11-14 (mục 14 cũ, chưa spec). Mục này làm ý đó, gắn vào Săn app.

## Anh chốt (2026-11-17)

1. **App cuối là app đáng bắt chước:** còn mới, studio nhỏ, rating tăng nhanh, có thu tiền, đứng nhiều keyword mà ít app mạnh.
   Không phải app "đáng đánh bại" (cái đó đã có ở đèn điểm yếu, [mục 26](phase-plan2-26-san-app-diem-yeu.md)).
2. **Dùng chung lượt săn:** không thêm lượt gọi store. Tab Theo app đọc từ các Research đã chạy trong lượt săn.
3. Thiết kế 5 bước bên dưới anh đã duyệt.

## Đo trước khi viết (2026-11-17, DB máy dev, chỉ đọc)

Đếm app trong top 10 các keyword đã Research của 3 lượt săn, mỗi app tính 1 lần (theo store + id).

| Lượt săn | App trong top 10 | Có ở ≥ 2 keyword | Ra mắt < 2 năm và ≥ 1.000 rating | Trong đó có thu tiền |
|---|---|---|---|---|
| selfie camera · US · 8 keyword | 151 | 46 | 9 | 6 |
| habit tracker · US · 7 keyword | 165 | 27 | 6 | 4 |
| calorie counter · US · 5 keyword | 49 | 14 | 11 | 3 |

Phễu **~150 → ~10 → 1** đứng được với ngưỡng mặc định. Ví dụ selfie camera, 3 app đầu theo số rating / ngày:

| App | Store | Ra mắt | Rating | Rating / ngày | Số keyword | Thu tiền |
|---|---|---|---|---|---|---|
| Selfie Camera - Beauty Camera (iMediaStar) | Play | 2025-09-09 | 20.576 | 47 | 4 | có |
| Glow Cam: Selfie Light Camera | Play | 2025-01-21 | 15.410 | 23 | 2 | có |
| Zoomera: Super Camera HD (Revoto) | Play | 2026-07-28 | 1.145 | 10 | 1 | có |

Lưu ý từ số đo: app App Store hay ra "không thu tiền" vì **Research không đọc IAP App Store**. Phải lấy IAP đã cache (như mục 24.4), không có thì ghi **chưa đo**, không tính 0.

## 32.1 · Hai tab

- Trên phần kết quả Săn app thêm 2 tab: **Theo keyword** · **Theo app**. Mặc định Theo keyword (giữ như cũ).
- Tab Theo app hiện khi có ít nhất 1 keyword Research xong. Research còn chạy thì ghi "đang gom từ 5/8 keyword", số tự cập nhật.
- Chuyển tab không chạy lại gì. Tab đang mở lưu vào link (`&view=apps`) để mở lại đúng chỗ.

## 32.2 · Gom app

Đọc từ `getAppHunt` (đã có `rv.competitors` của mỗi keyword), không gọi mạng:

- Lấy app có `bestRank ≤ 10` ở từng keyword đã Research xong.
- **Bỏ trùng trong 1 store** theo store + id. Ghi lại: các keyword app có mặt, hạng tốt nhất, hạng ở từng keyword.
- **Gộp 2 store** khi tên rút gọn trùng nhau (phần trước `-` `:` `|`, bỏ dấu, chữ thường — `appKey` ở `web/src/lib/app-hunt.ts`).
  Dòng gộp có 2 chip Play + App Store, số rating cộng lại, ngày ra mắt lấy ngày sớm hơn. Ghi chú nhỏ "gộp theo tên".
- Số rating, ngày ra mắt, cập nhật, giá, IAP lấy từ bản chụp mới nhất của app.

## 32.3 · Lọc (chỉnh ở Tuỳ chọn)

| Lọc | Mặc định | Vì sao |
|---|---|---|
| Ra mắt trong | 2 năm | App cũ đã chiếm chỗ từ lâu, khó học cách lên |
| Rating tối thiểu | 1.000 | Dưới mức này chưa chứng minh có người dùng |
| Bỏ studio lớn | bật | Google, Meta, Microsoft, Apple, Adobe, Snap, ByteDance, Amazon… thắng nhờ thương hiệu, không bắt chước được |

- Danh sách studio lớn là 1 mảng cố định trong code, có test. Chip **"Hiện cả studio lớn"** bật lại ngay trên bảng.
- App không có ngày ra mắt: không lọc ra, xếp cuối, ghi "chưa rõ ngày ra mắt".
- Không app nào qua lọc: ghi rõ, gợi ý hạ ngưỡng ở Tuỳ chọn (như tab Theo keyword đang làm).

## 32.4 · Điểm "Đáng bắt chước" /100

Hàm thuần `copyScore` trong file mới `web/src/lib/app-hunt-apps.ts`, có test. 5 phần:

| Phần | Tối đa | Đo bằng | Chưa đo khi |
|---|---|---|---|
| Cầu đã chứng minh | 30 | rating / ngày kể từ ra mắt, thang log (≥ 50/ngày = đủ 30) | thiếu ngày ra mắt hoặc số rating |
| Phủ keyword | 20 | số keyword có mặt trong top 10 (≥ 4 = 14 điểm) + hạng tốt nhất (#1–3 = 6 điểm) | — |
| Chỗ chen | 20 | trung vị rating top 10 của các keyword app đứng (thấp = nhiều chỗ), dùng lại `medianRatings` của mục 24 | keyword chưa có trung vị |
| Còn mới | 15 | < 6 tháng = 15, < 1 năm = 10, < 2 năm = 5 | thiếu ngày ra mắt |
| Thu tiền | 15 | trả phí hoặc có IAP = 15; free không IAP = 0 | App Store chưa có IAP cache |

- Phần chưa đo **không tính 0**: điểm = tổng phần đã đo × 100 / tổng tối đa của phần đã đo, như mục 24.4.
  Ghi rõ "chấm trên 4/5 phần" khi thiếu.
- Ngưỡng là điểm xuất phát; chỉnh sau khi chạy thật 3 lượt săn ở bảng đo trên, ghi lại số mới vào trang này.

## 32.5 · Kết quả

1 cột từ trên xuống:

1. **Thẻ lớn: app đáng bắt chước nhất.** Icon, tên, studio, chip store, điểm /100 dạng thanh 5 phần (mỗi phần 1 màu, rê chuột ra số).
   1 câu vì sao, dựng từ số thật, ví dụ: "47 rating/ngày từ 2025-09 · top 10 ở 4 keyword · có IAP".
   Nút **Soi app này** (mở Soi 1 app, tự chạy — `?mode=app&link=…&country=…`) · nút ⇄ **Thêm để so** · link trang store.
2. **2 app xếp sau:** thẻ nhỏ cùng dạng, cùng nút.
3. **Bảng đủ app đã lọc:** hạng · app · điểm · rating / ngày · số keyword · hạng tốt nhất · ra mắt · thu tiền · 2 nút tròn ⇄ 👁 (dùng lại `web/src/client/app-row-actions.tsx`).
   Bấm số keyword mở danh sách keyword + hạng ở từng keyword, mỗi keyword link về Research của nó.
4. Dưới cùng: "Đã gom 151 app → 9 qua lọc" + link "Xem cả app bị lọc" (hiện bảng đủ, cột lý do bị lọc).

## Đã có sẵn, dùng lại

| Cần | Có sẵn ở |
|---|---|
| Danh sách app top 10 mỗi keyword | `getAppHunt` → `getRunView(...).competitors` (`web/src/lib/app-hunt-run.ts`) |
| IAP App Store đã đọc | `cachedIap` (mục 24.4) |
| Trung vị rating top 10 | `demandSupply(...).medianRatings` (`web/src/lib/app-demand-supply.ts`) |
| Gộp tên app 2 store | `appKey` (`web/src/lib/app-hunt.ts`) |
| Nút ⇄ Thêm để so · 👁 Soi app | `web/src/client/app-row-actions.tsx` (2026-11-17) |
| Tuỳ chọn lưu máy | `niche-radar.appHuntOptions` ở `web/src/client/AppHunt.tsx` |

## Không làm

- Không gọi thêm store hay đọc review cho tab này (đọc review đã có ở mục 26, bấm Soi app là có).
- Không chấm bằng AI. Mọi số kèm keyword nguồn.
- Không đoán lượt tải, doanh thu, tuổi / giới tính người dùng.
- Không đổi điểm của tab Theo keyword.

## Thứ tự code (khi bắt đầu)

1. `app-hunt-apps.ts`: gom + bỏ trùng + gộp 2 store + lọc + `copyScore`, test với dữ liệu giả có app trùng, thiếu ngày, iOS chưa có IAP
2. Nối vào `getAppHunt` (thêm `apps` vào view) + MCP đọc được
3. Tab + thẻ app đầu + 2 app sau + bảng, dùng lại nút ⇄ 👁
4. Tuỳ chọn: 3 ngưỡng lọc + chip studio lớn
5. Chạy 3 lượt săn ở bảng đo (selfie camera, habit tracker, calorie counter), chỉnh ngưỡng, ghi số; soát 960px + 1340px, sáng + tối
