# 30 · Audit 1 app: chấm ASO app đã có, sửa gì trước, ai đang vượt mình

> Plan 2 · mục 30. Thẻ thứ 7 ở App Market Research: **dán link app của mình → chọn keyword → điểm /100 + bảng hạng
> keyword + 3–5 việc nên sửa → lấy đối thủ → đẩy sang So sánh app**. Dành cho người **đã build xong app**, khác 6 thẻ
> kia (dành cho người đang chọn app để làm).

<span class="chip chip--doing">Spec 2026-11-17 · anh đã chốt 3 câu · plan code xong · chưa code · chưa commit</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Mục 26, 27, 28 và Soi app liên quan cũng chưa commit. Nên gom và commit chúng trước rồi mới code mục này.
</div>

## Vì sao làm

Ngày 2026-11-17 anh gửi [wowkeywords.com](https://wowkeywords.com/) để học, và muốn có tính năng cho người đã có app:
phát hiện chỗ yếu về ASO, sửa, rồi so với đối thủ. Có thêm một nút lấy đối thủ liên quan để đẩy vào danh sách so cho nhanh.

Cũng là chỗ trống mà [mục 25](phase-plan2-25-hoc-apptweak-appfigures.md) đã ghi: AppTweak / Appfigures phục vụ người
đã có app muốn lên hạng. ShotMatic có sẵn gần hết nguyên liệu, chỉ thiếu phần chấm điểm và gợi ý việc nên sửa.

## Học gì từ WowKeywords (đọc 2026-11-17)

- **Audit** cho điểm 0–100, tính từ hạng keyword + trang store + độ cạnh tranh, rồi chỉ ra **vài việc nên sửa nhất**.
- Ghi rõ 3 thứ: keyword trang mình chưa phủ · app đang đứng trên mình · nước chưa có tên bằng tiếng địa phương.
- Sau Audit thì có AI viết lại tên / phụ đề / mô tả, theo dõi hạng theo lịch, MCP cho agent.

Mục này chỉ lấy **lõi Audit**. Phần còn lại để ở mục "Đợt 2" cuối trang.

## 3 câu anh đã chốt (2026-11-17)

1. **Phạm vi:** chấm **trang store + hạng keyword**, 1 nước mỗi lần chạy.
2. **Keyword:** **tự gợi ý khoảng 15 chip, user bỏ / thêm được** rồi mới bấm chạy.
3. **Lấy đối thủ:** gộp **app đứng trên mình ở các keyword + app tương tự của store**, xếp theo số keyword trùng.

Plan code: [2026-11-17-plan2-30-audit-app.md](../superpowers/plans/2026-11-17-plan2-30-audit-app.md) (8 task). Lúc viết plan sửa 2 chỗ: tick tối đa 3 đối thủ, hạng lưu ở `app_audits`.

## Đã có trong code (đọc 2026-11-17)

| Cần | Đã có | Mục này làm |
|---|---|---|
| Đọc link app | `parseAppLink` (`lib/app-inspect-core.ts`) | Dùng lại nguyên |
| Đọc trang store | `fetchStoreApp` (`lib/app-inspect.ts`), `collectors/listing.ts` | Dùng lại, thêm đếm ảnh / video nếu chưa có |
| Gợi ý keyword | `collectors/suggest.ts` (autocomplete Play + App Store) | Dùng cho 30.2 |
| Tìm trên store theo keyword | `liveSearch` (`lib/app-search.ts`) | Dùng để đo hạng ở 30.3 |
| App tương tự | `playRelated` / `iosRelated` / `pastedSimilar` (`lib/app-related.ts`) | Dùng cho 30.5 |
| So sánh app | `/?mode=compare&apps=a,b,…` (trang So sánh app) | Đẩy app đã tick sang |
| 17 nước | Danh sách nước của mục 27.0 | Dùng lại |

## 30.1 · Thẻ thứ 7 + ô nhập

- Thêm thẻ **"Audit my app"** vào lưới việc của App Market Research. Dòng mô tả dưới thẻ:
  *"Paste your live app: score its store page and keyword ranks /100, see what to fix first, pull rivals into Compare."*
- Dòng "The 6 tasks below run without AI" đổi thành **7 tasks**.
- Mở thẳng được bằng `/?mode=audit&link=…&country=…`. Thêm nút **Audit app này** ở Soi 1 app.
- Ô nhập: **1 link** Play / App Store (hoặc package / id) + chọn **1 nước** (mặc định US, đủ 17 nước).
- Bấm **Đọc app** → thấy ngay thẻ app (icon, tên, phụ đề, sao, ngày cập nhật) và các chip keyword ở 30.2.

## 30.2 · Chip keyword gợi ý

Khoảng **15 chip**, mỗi chip ghi nguồn bằng chấm màu nhỏ:

- **Từ tên + phụ đề** (Play: tên + mô tả ngắn): cụm 1–3 chữ, bỏ stop word và tên thương hiệu.
- **Gợi ý store:** autocomplete của 2–3 cụm đầu (dùng `suggest.ts`).
- **Từ đối thủ** (chỉ có sau khi bấm Lấy đối thủ): cụm xuất hiện trong tên của ≥ 2 đối thủ mà app mình không có.

User bỏ chip bằng ×, thêm bằng ô gõ (Enter). Tối đa **20 keyword** mỗi lần chạy. Bấm **Chạy audit** (~30–60 giây,
có thanh tiến độ + nút Dừng).

## 30.3 · Đo hạng keyword

- Với mỗi keyword: tìm trên store đúng nước đó, lấy **top 50**, ghi hạng của app mình (hoặc "ngoài top 50") và **3 app đứng đầu**.
- Chạy tối đa **3 luồng** cùng lúc. Gặp 429 thì chờ rồi thử lại 1 lần. Vẫn lỗi thì keyword đó ghi **"chưa đo"**, không tính là ngoài top.
- Mỗi lần chạy lưu 1 dòng vào bảng mới `app_audits` (hạng nằm trong đó) để mở lại. **Không** ghi vào bảng hạng của Research, để không tạo lượt Research giả.

## 30.4 · Điểm /100 + việc nên sửa

Trên cùng là **1 số lớn /100** + 1 câu kết luận (vd *"Trang ổn, nhưng chỉ 2/15 keyword vào top 10"*).
Dưới đó là **4 thanh điểm thành phần**, mỗi thanh có ⓘ giải thích cách tính. Đây là **quy ước ShotMatic**, không phải số store công bố.

| Phần | Điểm | Đo gì |
|---|---|---|
| Tên & phụ đề | 30 | Dùng bao nhiêu % giới hạn ký tự của store · có keyword đang hạng tốt nhất không · có lặp từ giữa tên và phụ đề không |
| Mô tả | 15 | Đủ dài chưa · keyword chính có nằm trong 3 dòng đầu không |
| Hình ảnh & rating | 20 | Số ảnh chụp màn hình · có video không · số sao · số ngày từ lần cập nhật cuối |
| Hạng keyword | 35 | Tỉ lệ keyword vào top 10 và top 50 (top 10 nặng hơn) |

**Luật "chưa đo":** phần nào store không trả dữ liệu (vd App Store không cho biết video) thì phần đó ghi "chưa đo"
và **bỏ khỏi mẫu số**, không cho 0 điểm. Giống luật của mục 24.4.

Giới hạn ký tự lấy theo store (ghi rõ trong code, có test):

- App Store: tên 30, phụ đề 30.
- Play: tên 30, mô tả ngắn 80.

**3–5 việc nên sửa trước**, xếp theo số điểm lấy lại được. Mỗi việc là 1 câu có số. Ví dụ:

- *"Keyword **habit tracker** bạn hạng 38, nhưng tên chưa có chữ này."*
- *"Phụ đề mới dùng 14/30 ký tự."*
- *"Cập nhật lần cuối 212 ngày trước. App đứng top 3 ở 4/5 keyword của bạn đều cập nhật trong 30 ngày."*

Bảng **hạng keyword** nằm dưới, 1 dòng mỗi keyword: keyword · hạng mình (chấm màu: xanh top 10, vàng 11–50, xám ngoài
top / chưa đo) · icon 3 app đứng đầu.

## 30.5 · Nút "Lấy đối thủ" → So sánh app

- Đặt ngay cạnh khối kết quả. Bấm thì gộp 2 nguồn:
  - **App đứng trên mình:** các app xuất hiện ở top 10 những keyword mình thua.
  - **App tương tự:** Play tự đọc (`playRelated`). App Store không có danh sách tương tự, nên hiện ô dán tay như Soi app liên quan.
- Bỏ trùng, bỏ chính app mình. Xếp theo **số keyword trùng** (mình và app đó cùng có hạng). Mỗi dòng ghi: icon · tên · số
  keyword trùng · sao · số rating · nguồn (đứng trên / tương tự).
- User tick **tối đa 3 app** (So sánh app nhận tối đa 4 app: mình + 3) → nút **Đẩy sang So sánh app** mở `/?mode=compare&apps=<id app mình>,<id các app đã tick>` (id trong máy, app chưa có thì thêm vào trước).
- Các app này cũng sinh chip "Từ đối thủ" ở 30.2, để chạy lại audit với keyword của đối thủ.

## Phần code

- `lib/app-audit-core.ts` (thuần, có test): rút keyword từ tên / phụ đề, chấm 4 phần, luật "chưa đo", tạo danh sách việc
  nên sửa, gộp + xếp đối thủ.
- `lib/app-audit.ts`: đọc app, đo hạng (3 luồng, thử lại khi 429), lưu bản ghi.
- `client/AppAudit.tsx`: trang 1 cột, khối kết luận theo skill tool-chart (số lớn + thanh + chấm), chữ dài gập vào ⓘ.
- Chữ giao diện: `locales/en-text-app-audit.ts` + bản tiếng Việt, giống Review Mining.
- Test: file thuần chấm điểm với 3 app mẫu (trang tốt / trang thiếu / thiếu dữ liệu), kiểm "chưa đo" không kéo điểm về 0.

## Xong là khi

1. Dán link 1 app Play thật và 1 app App Store thật ở US: ra điểm, bảng hạng, việc nên sửa, không có ô nào trống mà không ghi "chưa đo".
2. Bấm Lấy đối thủ → tick 3 app → So sánh app mở đúng 4 app (mình + 3).
3. Test thuần chạy qua. Xem trang ở 960px và 1340px: 1 cột, không có cột hẹp.

## Không làm ở bản này

- **Chấm từng nước** (17 nước cùng lúc). Mỗi nước tốn 15–20 lượt tìm, App Store sẽ trả 429.
- **AI viết lại tên / phụ đề / mô tả.** Đợt 2, dùng ✦ AI như mục 26.7.
- **Theo dõi hạng theo lịch.** Mục 25 đã bỏ phần chạy theo lịch.
- **Volume / difficulty của keyword.** Store không công bố. Chỉ dùng hạng thật và số gợi ý.
- **Upload lên App Store Connect / Play Console.**

## Đợt 2 (chưa xếp lịch)

- Chấm nhiều nước, chỉ ra nước chưa có tên bằng tiếng địa phương (giống WowKeywords).
- ✦ AI đề xuất 3 phương án tên + phụ đề, chấm lại bằng chính bảng hạng.
- MCP tool `audit_app` cho agent.
