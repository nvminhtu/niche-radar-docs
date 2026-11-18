# 29 · Săn việc làm tay: chỗ người ta còn chắp vá

> Plan 2 · mục 29. Một cách săn mới trong **Săn app**: gõ 1 việc (ví dụ "budget", "meal plan") →
> tool đo xem người ta có đang **làm tay** việc đó không (bảng tính, template, giấy in, hỏi "có app nào không"),
> app nào đang bán đúng cách làm tay đó, và người dùng app đối thủ có **bỏ về làm tay** không.

<span class="chip chip--todo">Viết plan 2026-11-17 · chờ anh duyệt</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Mục này chỉ code khi anh duyệt.
</div>

## Vì sao làm

Trong thread r/SideProject anh đăng (đọc 2026-11-16, chi tiết ở [mục 26](phase-plan2-26-san-app-diem-yeu.md)),
nhiều người cùng nói: tín hiệu khó giả nhất là **người ta đã bỏ công hoặc tiền** để tự vá vấn đề.

| Ai nói | Ý chính |
|---|---|
| ausecko | Tìm người đang tự chắp vá cách làm, ý tưởng app thật hay nằm ở đó |
| xiaoyao8888 | Tín hiệu khó giả: có bảng tính họ tự giữ, app trả phí bị chê, hoặc thuê người làm hộ |
| Kitchen_Cable6192 | Không có nỗi đau hay cách vá nào đang tồn tại thì bỏ ý tưởng |
| ram-popular | Mỗi kết luận nên chỉ ra được nguồn (review, keyword) để người dùng tự kiểm |

Hiện tool chỉ có **1 mẩu nhỏ** của ý này: mẫu chữ `WORKAROUND_RE` trong `web/src/lib/weak-spots.ts`
bắt review có "spreadsheet", "notes app", "went back to"… (mục 26). Chưa có chỗ nào đo **ngoài store**.

## Anh chốt (2026-11-17)

1. **Chỗ đặt:** thêm 1 chế độ mới trong **Săn app** (cạnh "cầu > cung"). Soi 1 app có link sang.
2. **People Also Ask:** không lấy thẳng (xem phần dưới). Dùng Google gợi ý kèm chữ hỏi + Stack Exchange + Ask HN. Chưa trả tiền API nào.
3. **Cách làm:** viết plan này trước, anh duyệt rồi mới code.

## Đo thử trước khi viết (2026-11-17, Google gợi ý, US, tiếng Anh)

Gọi cùng endpoint Google gợi ý mà `web/src/collectors/suggest.ts` đang dùng, mỗi câu 1 lần.

| Gõ vào Google | Số gợi ý | Gợi ý đầu |
|---|---|---|
| budget spreadsheet | 10 | budget spreadsheet template, … google sheets |
| budget notion template | 10 | budget notion template free, … reddit |
| is there an app to budget | 10 | is there an app to help budget money |
| meal plan spreadsheet | 10 | meal plan spreadsheet template google sheets |
| is there an app to meal plan | 10 | … plan meals for families · … based on macros |
| dog vaccination record spreadsheet | 10 | nhưng Google đổi sang "printable pdf free", không còn chữ spreadsheet |
| is there an app to track dog vaccinations | 2 | is there an app to keep track of dog vaccinations |
| shift swap spreadsheet | 3 | shift swap sheets · rules · policy |
| is there an app to swap shifts | 0 | — |

Rút ra 2 điều cho thiết kế:

- **Việc lớn** (budget, meal plan) luôn đủ 10 gợi ý, nên **đếm số gợi ý không phân biệt được gì**. Độ mạnh phải lấy từ Google Trends (29.2).
- Google hay **đổi chữ** (spreadsheet → printable). Chỉ tính gợi ý **còn chứa đúng chữ làm tay**; phần đuôi gợi ý ("for families", "based on macros") mới là thứ đáng đọc: nó nói ai cần và cần kiểu gì.

## Về People Also Ask (PAA)

PAA là khối câu hỏi trên **trang kết quả Google**. Google chặn bot đọc trang này và bắt giải CAPTCHA, tool không vượt CAPTCHA.
Cách thay (miễn phí, đã có sẵn trong code):

- **Google gợi ý kèm chữ hỏi**: "how to X", "can I X in excel", "is there an app to X", "X without an app". Phần lớn câu PAA cũng xuất hiện ở đây.
- **Stack Exchange** (Ask Different, Super User, Software Recs) + **Ask HN**: API miễn phí, đã có ở `web/src/lib/qa-sources.ts`.

Nếu sau này có key dịch vụ SERP trả phí (SerpAPI, DataForSEO…) thì cắm thêm 1 nguồn, không đổi phần còn lại.

## 29.1 · Người ta có tìm cách làm tay không

Gõ 1 việc `X` → hỏi Google gợi ý (có cache 7 ngày như hiện nay) với 6 đuôi làm tay:

- `X spreadsheet`
- `X excel template` · `X google sheets`
- `X notion template`
- `printable X`
- `X template`

Giữ gợi ý **còn chứa chữ làm tay** (spreadsheet / excel / sheets / notion / printable / template / pdf).
Hiện: mỗi đuôi 1 hàng, số gợi ý giữ lại + 3 gợi ý đầu (bấm mở Google). Số request: 6 / việc.

## 29.2 · Làm tay hay dùng app (Google Trends)

So 2 nhánh trên cùng 1 biểu đồ 12 tháng, cùng nước:

- nhánh làm tay: `X spreadsheet` (hoặc đuôi có nhiều gợi ý nhất ở 29.1)
- nhánh app: `X app`

Hiện tỉ lệ trung bình (ví dụ "làm tay = 0,6 × app") + mũi tên đang lên / xuống. Trends không có số (quá ít người tìm) thì ghi **chưa đo**.
Dùng lại `web/src/collectors/trends.ts` (đã có giãn cách 4 giây). Số request: 1 lượt so / việc.

## 29.3 · Người ta đang hỏi gì (thay PAA)

- Google gợi ý với 4 đầu câu hỏi: `how to X` · `can I X` · `is there an app to X` · `X without`.
- Stack Exchange + Ask HN: tìm `X` trong tiêu đề, giữ câu có chữ hỏi app / công cụ / cách làm.

Hiện: danh sách câu hỏi, mỗi câu có nguồn (Google gợi ý / tên site) + link. Câu "is there an app to X" trả 0 gợi ý cũng là 1 kết quả đáng ghi.

## 29.4 · App đang bán chính cách làm tay

Tìm trên Google Play + App Store (dùng lại `web/src/lib/app-search.ts`) với `X spreadsheet`, `X template`, `X tracker sheet`.
Giữ app có tên / mô tả nhắc chữ làm tay. Hiện rating, số lượt đánh giá, ngày cập nhật.
Ý nghĩa: app kiểu "template" mà vẫn có nhiều người dùng = người ta chịu trả công cho cách làm tay, một app làm đúng việc có thể thay được.

## 29.5 · Người dùng app đối thủ bỏ về làm tay

Lấy 3 app dẫn đầu khi tìm `X` trên store, đọc review 1–3★ (cache 7 ngày, như mục 26),
đếm **số người** có câu bỏ về làm tay ("went back to a spreadsheet", "just use excel", "pen and paper", "notes app").
Mở rộng `WORKAROUND_RE` thêm vài mẫu, có test. Mỗi câu trích có link review gốc.

## 29.6 · Thẻ kết luận

1 thẻ trên cùng: **"Người ta đang làm tay: rõ / ít / không thấy / chưa đo"**, rồi 5 hàng chấm (29.1–29.5), mỗi hàng 1 dòng + link nguồn.

| Hàng | Rõ khi | Chưa đo khi |
|---|---|---|
| Tìm cách làm tay | ≥ 2 đuôi còn ≥ 3 gợi ý đúng chữ | Google gợi ý lỗi |
| Làm tay vs app | nhánh làm tay ≥ 0,3 × nhánh app | Trends không có số |
| Đang hỏi | ≥ 3 câu hỏi từ ≥ 2 nguồn | mọi nguồn lỗi |
| App bán cách làm tay | ≥ 1 app có ≥ 1.000 lượt đánh giá | store lỗi |
| Bỏ về làm tay | ≥ 3 người trong review | chưa đọc được review |

Ngưỡng là **điểm xuất phát**, chỉnh sau khi chạy thật 5 việc. "Rõ" cần ≥ 3 hàng đạt. Phần chưa đo **không tính là 0**, như mục 24.4.
Nút cuối thẻ: **Research "X app"** (cầu > cung) · **Soi app** cho từng app ở 29.4.

## Không làm

- Không đọc trang kết quả Google, không vượt CAPTCHA, không vào Reddit (Reddit chặn tool; anh dán link thì đọc như cũ).
- Không chấm bằng AI. Mọi số đi kèm nguồn + ngày.
- Không chạy theo lịch.

## Ước lượng mỗi lần săn

Khoảng 6 + 4 gợi ý Google, 1 lượt Trends, 2 nguồn hỏi đáp, 3 lượt tìm store, 3 lượt đọc review.
Thời gian chưa đo; đo khi code xong, ghi lại ở đây.

## Thứ tự code (khi anh duyệt)

1. 29.1 + 29.3: Google gợi ý (đã có hạ tầng, nhanh nhất)
2. 29.2: Trends so 2 nhánh
3. 29.4 + 29.5: store + review
4. 29.6: thẻ kết luận, chế độ mới trong Săn app, link từ Soi 1 app
5. Chạy thật 5 việc (budget, meal plan, dog vaccination record, shift swap, habit tracker), chỉnh ngưỡng, ghi số đo vào trang này
