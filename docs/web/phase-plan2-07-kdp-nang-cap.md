# 6.1 · Từ khoá + cạnh tranh: điểm sách ngay trên Amazon + tìm niche sách con (mục 7 cũ)

> Plan 2 · mục 7. Hai việc làm cho phần sách của ShotMatic khác hẳn Publisher Rocket, KDSPY, BookBeam:
> **7.1** Scout chấm điểm sách ngay trên trang Amazon anh đang mở và gửi số sang app, không phải copy / dán;
> **7.2** gõ 1 chủ đề rộng (ví dụ *cookbook*), ShotMatic trả về danh sách niche sách con đã xếp hạng.
> Nối tiếp [4.3 Amazon Books](phase-55-2-amazon-books.md) (tra từng keyword) và [6 Book Discover](phase-plan2-06-book-discover.md)
> (xem top sách theo chuyên mục).

<span class="chip chip--todo">Plan 2026-11-10 · để sau Marketing · chưa làm</span>

<div class="box" markdown>
**Từ 2026-11-11 trang này là phần chi tiết của [6 · Bộ tool KDP](phase-plan2-06-bo-tool-kdp.md)** (tool 4 Từ khoá + cạnh tranh).
Anh chốt 2 luật mới ở trang đó: **Scout được tự tải trang sách để lấy BSR** (tối đa 20 cuốn / lần bấm, nghỉ 4–8 giây,
gặp chặn thì dừng) và **hiện ước thu nhập dạng khoảng thấp–cao có ghi nguồn**. Chỗ nào bên dưới ghi khác thì theo trang 6.
</div>

<div class="box box--danger" markdown>
**Nhắc quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho bán hàng + SEO + GEO
([Marketing](../marketing/index.md)). Anh chốt 2026-11-10: **viết plan trước, code sau Marketing**.
</div>

<div class="box box--goal" markdown>
**Đích**

- **7.1:** đang ở trang tìm Books hoặc Kindle trên Amazon, panel Scout hiện ngay **điểm sách 0–100** (đúng con số app sẽ
  ra), sách mới / 10, rating giữa, cờ thương hiệu. Bấm **Gửi sang ShotMatic** là lượt tra trong app có trang đó, khỏi
  chép nguồn trang.
- **7.2:** gõ 1 chủ đề rộng, nhận về **30–50 niche sách con** xếp theo độ mạnh gợi ý Amazon + Trends 12 tháng, mỗi
  niche có nút chấm trên Amazon (đi tiếp qua 7.1).
- Mọi số vẫn theo luật cũ: đo được, ghi ngày, không ước doanh số từ BSR, không tự mở trang Amazon.

**Xong khi:** 7.1 chấm thật 5 keyword trên Chrome của anh, điểm trên panel Scout trùng điểm trong app. 7.2 chạy thật
3 chủ đề rộng, mỗi chủ đề ra ≥ 30 niche con không trùng, không bị Amazon chặn. Màn đứng được ở 960px và 1340px, cả
English lẫn tiếng Việt.
</div>

## Vì sao làm 2 việc này

- **Chỗ nghẽn là bước dán tay.** Ngày 2026-11-09, bảng niche sách trong máy anh có 10 lượt tra, **cả 10 đều "Chưa chấm
  điểm"**. Muốn có điểm phải mở trang → Xem nguồn → chọn hết → chép → dán, làm cho 2 trang + 5 trang sách. Không ai làm.
- **Đối thủ tra từng keyword.** Publisher Rocket, KDSPY, BookBeam đều bắt anh nghĩ ra keyword trước rồi mới tra. Chưa tool
  nào nhận 1 chủ đề rộng và trả về danh sách niche con đã xếp hạng (bảng đối thủ ở
  [4.3 mục 4](phase-55-2-amazon-books.md#4-oi-thu)).
- **Dùng lại đồ đã có.** Bộ chấm sách (`summarizeBooks`, `formatScore`, `bookLevel`) nằm trong
  `extension-amazon/lib/books.js`, dùng chung cho app và Scout. Gợi ý a–z + làm sạch keyword sách đã chạy ở 4.3.
- **Có số để làm marketing.** 7.2 ra được bài kiểu "12 niche cookbook đang lên tháng này" bằng số thật, đúng hướng
  [Marketing](../marketing/index.md) đang đi.

## 7.1 · Scout chấm sách ngay trên Amazon

### Hôm nay đang có gì

- Trên trang tìm Amazon, Scout hiện panel chấm kiểu **hàng hoá chung**: số kết quả, ★ trung bình, số ô tài trợ,
  "bought / mo", top 5 kết quả. Trang tìm mục Books / Kindle có thêm nút **Copy for Niche Radar**.
- Điểm sách (Kindle, Paperback, Hardcover) chỉ có **trong app**, sau khi anh dán trang.

### Anh sẽ thấy gì

Đọc từ trên xuống, trong panel Scout ở trang tìm Books hoặc Kindle:

1. **Keyword + chợ** như hiện giờ.
2. **Điểm sách 0–100** của định dạng đang xem (Books → Paperback, Kindle Store → Kindle) + nhãn *Nên làm / Cân nhắc /
   Đông / Có cờ chặn*, dùng đúng hàm của app nên ra cùng con số.
3. **3 dòng lý do** bằng chữ: *4/10 sách mới (< 100 rating)*, *rating giữa 230*, *3/10 trong Kindle Unlimited* (chỉ Kindle).
4. **Cờ thương hiệu** nếu keyword có tên thuốc / đồ bếp / nhân vật, kèm link *Tra trademark ↗* (USPTO).
5. Nút **Gửi sang ShotMatic** (chính) và **Copy** (dự phòng, như hiện giờ).

Trên trang 1 cuốn sách: BSR + hạng chuyên mục + NXB + chip *tự xuất bản*, và cũng có nút **Gửi sang ShotMatic** để
đưa vào BSR watchlist.

### Gửi sang app thế nào

- Scout gửi trang đang mở tới app ShotMatic chạy trên máy anh (`http://127.0.0.1:<cổng>`), giống nút dán hiện giờ nhưng
  không qua clipboard. App tìm lượt tra sách cùng keyword + chợ, chưa có thì tạo mới, rồi gắn trang vào.
- **Cổng:** bản web dev chạy `3200`. App Mac tự chọn cổng lúc mở (`app/src-tauri/src/main.rs` đặt biến `PORT`), số cổng
  thật: `chưa đo`. Cách tìm cổng (Scout thử danh sách cổng, hay anh dán cổng vào popup Scout 1 lần) chốt sau M1.
- **Quyền Chrome:** cần thêm `http://127.0.0.1/*`. Để khỏi làm người cài Scout từ store thấy cảnh báo, xin quyền này
  **lúc bấm nút lần đầu** (`optional_host_permissions`), không xin lúc cài.
- **App chỉ nhận từ Scout:** endpoint mới chỉ nhận yêu cầu có origin là đúng id extension Scout, giữ chặn như
  `guardJsonPost` đang làm cho web.
- App không mở → báo *"Chưa mở ShotMatic — mở app rồi bấm lại, hoặc bấm Copy"*, không im lặng.

### Luật

- Scout chỉ đọc **trang anh đang mở**, không tự mở trang, không tự chuyển trang 2. Đúng luật của 4.3 mục 7.
- Người dùng Scout không có app vẫn thấy đủ điểm trên panel. Nút gửi chỉ là thêm, và là cửa kéo người dùng tải app.

## 7.2 · Tìm niche sách con từ 1 chủ đề rộng

### Anh sẽ thấy gì

Trên trang Amazon chế độ Sách, cạnh ô tra có lựa chọn **Một keyword** (như hiện giờ) / **Chủ đề rộng**. Gõ
*cookbook* ở chế độ Chủ đề rộng:

1. **Dải số ngắn** (nằm ngang): số niche con, số lần gọi gợi ý, thời gian chạy, ngày đo.
2. **Bảng niche con**, mỗi niche 1 hàng, cột:
    - niche (ví dụ *cookbook for seniors*, *air fryer cookbook*)
    - **Lần gợi ý**: tổng số lần Amazon gợi ý niche này qua cả 2 tầng a–z
    - **Hạng gợi ý**: dòng cao nhất niche đứng trong ô gợi ý
    - **Keyword con**: số keyword sách nằm dưới niche này
    - **Trends**: 13 tuần cuối so 13 tuần đầu, chỉ đo cho 15 niche đứng đầu
    - **Cờ**: thương hiệu / sốt 1 lần
    - **Điểm**: nếu niche đã tra ở 4.3 thì hiện điểm, chưa thì trống
    - nút **Chấm trên Amazon ↗**: mở trang tìm Books của niche đó, Scout (7.1) chấm và gửi về
3. Bấm tên niche → tra niche đó ở chế độ Một keyword (như bấm keyword trong bảng hiện giờ).
4. Nút **Chép danh sách** và **Lưu vào Project**.

### Cách chạy

1. **Tầng 1:** gợi ý a–z của chủ đề (27 lần gọi, code có sẵn) → làm sạch bằng `cleanBookSuggestions` (bỏ rác, tách tên
   tác giả, gộp biến thể).
2. **Tầng 2:** lấy **10 keyword tầng 1 có nhiều lần gợi ý nhất**, chạy a–z tiếp cho từng cái (10 × 27 = 270 lần gọi).
3. **Gom niche:** bỏ chữ của chủ đề, gom keyword theo phần còn lại (*for seniors*, *air fryer*, *for diabetics*…).
   Niche = nhóm có ≥ 2 keyword, hoặc 1 keyword có ≥ 3 lần gợi ý.
4. **Xếp hạng:** lần gợi ý giảm dần, hoà thì hạng gợi ý cao hơn đứng trước. Không đổi ra "lượt tìm / tháng".
5. **Trends:** chỉ gọi cho 15 niche đầu, dùng `cachedTrends` có sẵn, niche còn lại ghi "—".
6. **Lưu 7 ngày** như lượt tra hiện giờ. Tick *Tra mới, bỏ kết quả đã lưu* thì chạy lại.

Số lần gọi tổng (khoảng 300 lần gợi ý + 15 lần Trends), thời gian chạy, và Amazon có chặn ô gợi ý ở mức này không:
`chưa đo`. Ngày 2026-11-05 lấy được 4.845 keyword sách từ ô gợi ý mà không bị chặn, nhưng chưa ghi số lần gọi.

## Các bước

### 7.1 · M1 · Đo trên Chrome của anh

- 5 keyword (ví dụ *cookbook for seniors*, *adhd workbook for adults*, *dog training*, *gratitude journal*,
  *coloring book for adults*), mỗi keyword trang Books + Kindle.
- Ghi: điểm hàm Scout tính trên trang vs điểm app tính từ trang dán. Phải trùng.
- Ghi cổng app Mac thật trên 2 lần mở app.

### 7.1 · M2 · Panel điểm sách trong Scout

- `content.js`: ở trang Books / Kindle thì vẽ khối điểm sách thay khối hàng hoá chung, dùng hàm trong `lib/books.js`.
- Test trong `web/tests/extension-amazon.test.ts` với trang chụp sẵn (fixture), không gọi Amazon thật.

### 7.1 · M3 · Gửi sang ShotMatic

- Endpoint mới trong `web/src/server/social-api.ts`: nhận trang + keyword + chợ, tìm hoặc tạo lượt tra sách, gắn trang.
- Scout: nút gửi, xin quyền lúc bấm, báo lỗi rõ khi app không mở. Giữ nút Copy.
- Test endpoint: origin lạ bị chặn, tạo mới khi chưa có lượt tra, gắn vào lượt có sẵn.

### 7.1 · M4 · Phát hành Scout 0.3.0

- Cập nhật `STORE-LISTING.md` (dòng tính năng mới + lý do xin quyền localhost), `npm run ext:amazon:zip`.
- Anh tự bấm Submit trên Chrome Web Store.

### 7.2 · M1 · Đo 3 chủ đề rộng

- *cookbook*, *journal*, *coloring book*, chợ US: đếm lần gọi, thời gian, số niche con, có lỗi / bị chặn không.
- Từ số đo chốt lại: tầng 2 lấy 10 hay ít hơn, khoảng nghỉ giữa các lần gọi.

### 7.2 · M2 · Bộ chạy 2 tầng + gom niche

- Hàm thuần trong `web/src/collectors/amazon-books.ts` (tầng 2) và `web/src/lib/book-research.ts` (gom + xếp hạng).
- Test với gợi ý giả: gom đúng nhóm, bỏ keyword là tên tác giả, xếp đúng thứ tự, Trends chỉ gọi 15 lần.

### 7.2 · M3 · Giao diện Chủ đề rộng

- Lựa chọn Một keyword / Chủ đề rộng trên trang Amazon chế độ Sách, bảng niche con, nút chấm trên Amazon, chép, lưu Project.
- Soát ở 960px + 1340px, English + tiếng Việt, sáng + tối.

### 7.2 · M4 · Bài blog từ số thật

- Chạy 1 chủ đề, viết 1 bài shotmatic.app/blog bằng skill `shotmatic-blog` từ bảng niche con (số + ngày đo).
- Chỉ làm khi Marketing đang mở lại việc viết bài.

## Rủi ro + luật

- **Amazon đổi HTML trang tìm** → panel Scout chấm sai hoặc 0 cuốn. Có fixture test, đọc được 0 cuốn thì báo, không hiện điểm.
- **Ô gợi ý bị chặn khi gọi ~300 lần.** M1 đo trước; gặp chặn thì dừng, giữ phần đã có, ghi rõ niche nào thiếu tầng 2.
- **Google Trends giới hạn.** Chỉ 15 lần / chủ đề, dùng cache. Lỗi thì cột Trends ghi "—", không chặn cả bảng.
- **Chrome Web Store hỏi quyền localhost.** Xin lúc bấm, ghi lý do trong store listing.
- **Điểm Scout và app lệch** nếu 2 bên dùng 2 bản hàm khác nhau. Cùng import `lib/books.js`, test so 2 bên.

## Không làm

- Ước doanh số / royalty từ BSR (luật [4.3 mục 8](phase-55-2-amazon-books.md#8-khong-lam)).
- Số "lượt tìm / tháng" tự tính.
- Scout tự mở trang tìm hay trang sách, kể cả cho 7.2. Nút *Chấm trên Amazon* chỉ mở 1 tab khi anh bấm.
- Hướng 3 (AI đọc review 1–3★ của top 5) và hướng 4 (câu hỏi Reddit / YouTube → mục lục): để plan sau.

## Cần anh chốt

1. **7.1 gửi qua localhost** hay chỉ giữ Copy nhưng tự dán khi app đang mở tab đó? Gửi qua localhost tiện nhất nhưng
   phải xin thêm quyền Chrome.
2. **7.2 tầng 2 lấy mấy keyword** (đề xuất 10, chốt lại sau khi đo ở M1).
3. **7.2 nằm ở đâu:** lựa chọn trong trang Amazon chế độ Sách (đề xuất), hay mục riêng trên sidebar.
