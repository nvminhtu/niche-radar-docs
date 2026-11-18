# 31 · Trending Apps: bảng xếp hạng theo nước, thiết bị, nhóm app

> Plan 2 · mục 31. Thẻ thứ 8 ở App Market Research: **chọn store → nước (1 hoặc nhiều) → thiết bị → loại bảng → nhóm app**
> → xem bảng Top kèm chip **mới vào bảng** / **↑ hạng** → bấm 1 app sang Soi app, Săn app hoặc So sánh app.
> Làm giống tab trend YouTube (chọn nhiều nước, chạy 1 lượt, lọc theo nước).

<span class="chip chip--todo">Spec 2026-11-17 · chờ anh chốt 3 câu · chưa code</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Mục 26–30 cũng chưa commit hết. Nên gom và commit chúng trước rồi mới code mục này.
</div>

## Vì sao làm

- Tool hiện **chỉ đi từ keyword** (Săn app, Tìm app, Soi app). Người chưa có ý tưởng không có chỗ bắt đầu.
- YouTube đã có tab trend theo nước, App thì chưa. Anh hỏi 2026-11-17: *"có Trending Apps theo quốc gia, filter theo device… giống YouTube không?"*
- Bảng Top theo **nhóm app nhỏ** (ví dụ Health & Fitness ở Đức) cho thấy ngách nào đang có app mới leo lên. Đó là chỗ đáng soi.

## Đo thử nguồn (2026-11-17)

Gọi thật, mỗi nguồn 1 lần, không cần key.

| Nguồn | Gọi gì | Kết quả |
|---|---|---|
| Google Play | `gplay.list` (đã có trong `google-play-scraper` 10.1.4) · Top Free US, 200 app | 200 app, 1,9 giây |
| Google Play | Top Paid VN · Grossing US | 198 · 200 app, khoảng 0,5 giây |
| Google Play | Top Free + nhóm Productivity US | 200 app; chỉ 5/50 app trùng bảng chung, nên **lọc nhóm có tác dụng** |
| Google Play | Top Free + nhóm Game Puzzle JP | 200 app |
| App Store | RSS cũ `itunes.apple.com/{nước}/rss/topfreeapplications/limit=100/genre=6007/json` | 100 app, đúng nhóm Productivity |
| App Store | RSS cũ, bảng iPad (`topfreeipadapplications`) · Mac (`topfreemacapps`) · Grossing | đều trả bảng |
| App Store | RSS mới `rss.marketingtools.apple.com/api/v2/{nước}/apps/top-free/…` | chạy, nhưng **không lọc nhóm, không có Grossing** |

Rút ra:

- App Store dùng **RSS cũ**: có đủ iPhone / iPad / Mac, có Grossing, có lọc nhóm. Tối đa **100 app** mỗi bảng (xin 200 vẫn trả 100).
- Google Play **không tách điện thoại / máy tính bảng**: chỉ có 1 bảng chung.
- Cả 2 nguồn **không có số tải, số lượt đánh giá** trong bảng. Play có sao; App Store không có sao. Muốn có thêm số thì phải đọc từng app (chậm), xem 31.4.

## Anh chốt (chờ, 3 câu)

1. **Chỗ đặt:** thẻ thứ 8 trong App Market Research (đề xuất), hay 1 tab riêng trong Săn app?
2. **Lưu bảng mỗi ngày để tính ↑ hạng:** chỉ lưu khi anh bấm chạy (đề xuất, giống YouTube trend), hay tự chạy 1 lần / ngày khi app đang mở?
3. **Đọc thêm số từng app** (số đánh giá, ngày ra mắt) cho **top 20** của bảng: có làm không? Thêm khoảng 20 lượt gọi / bảng.

## 31.1 · Ô chọn

1 hàng chọn, giống form trend YouTube:

- **Store:** Google Play · App Store
- **Nước:** 1 nước, hoặc tick nhiều nước (bộ 17 nước ở `web/src/lib/countries.ts`, có "Chọn hết")
- **Thiết bị:** App Store: iPhone · iPad · Mac. Google Play: ẩn ô này, ghi nhỏ "Play chỉ có 1 bảng chung"
- **Loại bảng:** Miễn phí · Trả phí · Doanh thu cao
- **Nhóm app:** Tất cả, hoặc 1 nhóm. Danh sách nhóm của 2 store khác nhau; mỗi store giữ danh sách riêng
- **Số app:** Top 50 / 100 (Play cho tới 200, App Store tối đa 100)

Mở thẳng được bằng `/?mode=trending&store=play&country=US&chart=free&cat=PRODUCTIVITY`.

## 31.2 · Bảng Top

Mỗi hàng: hạng · icon · tên · studio · nhóm · giá · sao (chỉ Play) · chip thay đổi · 3 nút.

- **Chip thay đổi** (chỉ có khi đã lưu ít nhất 1 lần trước, xem 31.3):
  - **Mới**: app không có ở lần lưu trước
  - **↑ 12** / **↓ 5**: lên / xuống bao nhiêu hạng so với lần trước
  - Chưa có lần trước: ghi "chưa có lần trước để so", **không bịa ↑**
- **Lọc nhanh** (chip trên đầu bảng): Chỉ app mới · Chỉ app leo ≥ 10 hạng · Ẩn app của Google / Meta / Microsoft… (studio lớn)
- **3 nút mỗi hàng:** Soi app · Săn app với tên nhóm / keyword trong tên · Thêm vào So sánh app (tick nhiều rồi đẩy sang)
- Mỗi app có link mở trang store gốc.

## 31.3 · Lưu bảng + tính ↑ hạng

- Mỗi lần chạy lưu 1 bản: `store · nước · thiết bị · loại bảng · nhóm · ngày · [appId, hạng]`. Có cache 6 giờ: chạy lại trong 6 giờ thì đọc bản đã lưu, nút **Tra lại** để bỏ cache (như StaleTrendBar của YouTube).
- So với bản **gần nhất cũ hơn 20 giờ** của cùng bộ chọn. Ghi rõ "so với 2026-11-15" trên đầu bảng.
- Có từ 3 bản trở lên: mỗi app có 1 đường nhỏ hạng theo ngày (sparkline), lấy hình từ skill `tool-chart`.
- Bảng cũ hơn 90 ngày tự gom: giữ 1 bản / tuần.

## 31.4 · Thêm số cho top 20 (nếu anh chốt câu 3)

Đọc chi tiết 20 app đầu (dùng lại `gplay.app` và đọc App Store như Soi app), cache 7 ngày:

- **số lượt đánh giá**, **ngày ra mắt**, **ngày cập nhật**
- Chip **App mới < 90 ngày** khi ngày ra mắt gần: app mới mà đã vào Top là tín hiệu mạnh nhất của bảng này.

Gọi giãn 1 giây / app; App Store gặp 429 thì dừng, giữ phần đã đọc, ghi "đọc được 12/20".

## 31.5 · Chạy nhiều nước

Giống "chạy nhiều" của YouTube trend (mục 23): hàng chờ máy chủ, chạy **2 nước một lúc**, có thanh tiến độ.
Xong thì hiện 1 bảng gộp:

- Chip lọc theo nước (như "Lọc theo nước" ở YouTube trend)
- Cột **"có ở mấy nước"**: app có mặt ở nhiều nước cùng lúc
- Chip **Chỉ ở 1 nước**: app mạnh ở 1 nước mà chưa có ở nước khác, gợi ý làm bản cho thị trường còn lại

## 31.6 · Thẻ kết luận đầu trang

1 câu + 3 ô số, không chấm điểm:

- "Top Free Productivity · US · iPhone: **7 app mới**, **4 app leo ≥ 10 hạng** so với 2026-11-15"
- Ô số: app mới · app leo mạnh · app của studio nhỏ (không thuộc danh sách studio lớn)
- Chưa có lần trước: chỉ hiện ô "app của studio nhỏ", ghi "chạy lại ngày mai để thấy ↑ hạng".

## Đã có sẵn, dùng lại

| Cần | Có sẵn ở |
|---|---|
| Đọc Play | `google-play-scraper` (thêm `gplay.list`, chưa dùng chỗ nào) |
| Đọc App Store | `web/src/collectors/appstore.ts` (thêm hàm đọc RSS cũ) |
| 17 nước + cờ | `web/src/lib/countries.ts`, `components/Flag.tsx` |
| Form chọn nhiều nước, chạy nhiều, thanh cũ | `web/src/client/YoutubeTrend.tsx` (`TrendForm`, `StaleTrendBar`) |
| Hàng chờ chạy nhiều | mục 23 |
| Soi app · So sánh app · Săn app | `/?mode=inspect`, `/?mode=compare&apps=…`, Săn app |

## Không làm

- Không có **số tải / doanh thu ước tính** (store không cho; không đoán bừa). Nếu sau này có nguồn trả phí thì cắm thêm.
- Không tách Play theo điện thoại / máy tính bảng (nguồn không có).
- Không chạy theo lịch khi app tắt. Không chấm bằng AI.
- Không lấy bảng "Trending / Editor's choice" của store (không có nguồn đọc được).

## Rủi ro

- `gplay.list` từng có lúc hỏng theo đợt Google đổi trang. Hỏng thì hiện "Play đang không trả bảng, thử lại sau", không hiện bảng rỗng như kết quả thật.
- App Store hay trả **429** khi gọi nhiều nước liên tiếp: giãn 2 giây / bảng, chạy nhiều nước thì 2 luồng.
- RSS cũ của Apple là nguồn cũ, Apple có thể tắt. Khi đó lùi về RSS mới (mất lọc nhóm + Grossing), ghi rõ trên trang.

## Thứ tự code (khi anh duyệt)

1. 31.1 + 31.2: đọc bảng 2 store, 1 nước, bảng Top (chưa có chip thay đổi)
2. 31.3: lưu bản + chip Mới / ↑ / ↓
3. 31.6: thẻ kết luận
4. 31.5: chạy nhiều nước
5. 31.4 nếu anh chốt
6. Chạy thật 3 bộ (Productivity US iPhone, Health & Fitness DE Play, Game Puzzle JP Play) 2 ngày liên tiếp, ghi số đo vào trang này
