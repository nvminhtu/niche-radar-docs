# 6.3 · Book Discover: chuyên mục đang lên + thu nhập sách (mục 6 cũ)

> Plan 2 · mục 6. Một màn hình trong ShotMatic để xem top sách của nhiều chuyên mục Amazon cùng lúc: hạng, BSR, ước doanh
> thu, BSR theo tháng. Mục tiêu là anh khỏi phải mở trang Amazon rồi mở hàng chục tab. Màn này nối tiếp
> [4.3 Amazon Books](phase-55-2-amazon-books.md): 4.3 bắt đầu từ **keyword**, còn Book Discover bắt đầu từ **chuyên mục**.

<span class="chip chip--todo">Plan 2026-11-09 · để sau Marketing · chưa làm</span>

<div class="box" markdown>
**Từ 2026-11-11 trang này là phần chi tiết của [6 · Bộ tool KDP](phase-plan2-06-bo-tool-kdp.md)** (tool 2 Chuyên mục đang lên + tool 3 Thu nhập sách).
Anh chốt 2 luật mới ở trang đó: **Scout được tự tải trang sách để lấy BSR** (tối đa 20 cuốn / lần bấm, nghỉ 4–8 giây,
gặp chặn thì dừng) và **hiện ước thu nhập dạng khoảng thấp–cao có ghi nguồn**. Chỗ nào bên dưới ghi khác thì theo trang 6.
</div>

<div class="box box--danger" markdown>
**Nhắc quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho bán hàng + SEO + GEO
([Marketing](../marketing/index.md)). Anh chốt 2026-11-09: **để sau Marketing**. Plan này viết sẵn, chưa code.
</div>

<div class="box box--goal" markdown>
**Đích**

- Một trang **Book Discover** trên sidebar, nằm dưới Amazon.
- Xem cùng lúc **top 50 sách của tối đa 10 chuyên mục** (ví dụ 10 × 50 = 500 sách) trong một bảng. Lọc được theo
  chuyên mục và định dạng (Kindle / Paperback / Hardcover), sắp được theo hạng, BSR, ước doanh thu, số review, ngày ra.
- Mỗi sách có: hạng trong chuyên mục, BSR tổng (khi có), **ước doanh thu / tháng dạng khoảng thấp–cao**, BSR theo tháng.
- Mỗi con số ghi **đo ngày nào, từ trang nào**, kèm nút mở lại trang gốc trên Amazon.

**Xong khi:** đã chụp thật 10 chuyên mục sách US, mỗi chuyên mục 50 cuốn, hiện đúng trong 1 bảng lọc được. Sau ≥ 30 ngày
chụp lại thì cột BSR theo tháng có ít nhất 2 điểm. Màn đứng được ở 960px và 1340px, cả English lẫn tiếng Việt.
</div>

## Anh sẽ thấy gì trên màn hình

Đọc từ trên xuống:

1. **Thanh chọn chuyên mục.** Chip chuyên mục đã lưu (ví dụ *Self-Help*, *Cookbooks*, *Children's Activity Books*…),
   có cờ nước bên cạnh. Bấm `+ Thêm chuyên mục` để thêm, tối đa 10 chip đang bật. Bên cạnh là ô lọc định dạng và nút
   **Cập nhật** (cách cập nhật xem mục [Lấy số từ đâu](#lay-so-tu-au)).
2. **Dải số tóm tắt** (chỉ số ngắn, nằm ngang): tổng số sách, số chuyên mục, % sách tự xuất bản trong top, BSR trung vị,
   ước doanh thu trung vị / tháng, lần chụp gần nhất.
3. **Bảng top sách.** Cột: ảnh bìa · tên sách + tác giả · chuyên mục + hạng (ví dụ `#3 trong Self-Help`) · định dạng ·
   giá · rating + số review · BSR tổng · ước doanh thu / tháng · sparkline BSR theo tháng · ngày ra · NXB (*tự xuất bản* hay không).
   Cột đầu dính trái, bảng có phân trang, rê vào tên sách xem tên đầy đủ.
4. **Bấm 1 cuốn → khung chi tiết** bên phải: biểu đồ BSR theo tháng (mỗi điểm ghi ngày chụp), cách tính doanh thu
   (BSR → bán / ngày → × giá → khoảng), các chuyên mục cuốn đó đang đứng, nút **Theo dõi** (đưa vào BSR watchlist có sẵn)
   và nút **Tra keyword này** (mở chế độ Books ở 4.3 với tên chủ đề của sách).
5. **Tab phụ:** *Sách mới lọt top* (lần chụp này có, lần trước không) và *Lên / xuống mạnh nhất* (so 2 lần chụp).

## Lấy số từ đâu

Amazon chặn tool tự mở trang. Đo ngày 2026-11-05: trình duyệt AI bị chặn ngay lần tìm đầu, server tự tải trang bị chặn
sau 61 trang. Vì vậy ShotMatic không tự mở trang Amazon. Có 3 cách:

### Cách A · Extension Scout đọc trang Best Sellers anh đang mở (anh chốt: làm trước)

- Anh mở trang Best Sellers của một chuyên mục sách trên Amazon, bấm *Copy for ShotMatic* trong Scout (hoặc dán
  HTML như 4.3 đang làm). ShotMatic đọc 50 cuốn trên trang đó.
- 10 chuyên mục = anh mở 10 trang (thêm trang 2 nếu muốn top 100). Một lần mở được 50 cuốn, so với hiện giờ phải mở
  50 tab sách.
- Lấy được: hạng trong chuyên mục, tên, tác giả, ASIN, ảnh bìa, giá, định dạng, rating, số review.
- **Không lấy được BSR tổng.** Trang Best Sellers chỉ ghi hạng trong chuyên mục. BSR tổng chỉ có trên trang của từng
  cuốn (`/dp/<ASIN>`). Vì thế ước doanh thu chỉ có cho sách anh đã dán trang chi tiết (4.3 đang làm được, tối đa 10 cuốn / lần).
- Miễn phí, an toàn vì là phiên Chrome của chính anh, và Scout đã có sẵn bộ đọc trang Amazon.
- Số 50 cuốn / trang và đường dẫn trang 2: `chưa đo`, cần đo trên Chrome của anh trước khi code.

### Cách B · Scout tự mở lần lượt các trang trong Chrome của anh

- Anh bấm *Cập nhật 10 chuyên mục* một lần, Scout mở lần lượt 10–20 trang trong Chrome của anh, cách nhau 6–8 giây.
- Đỡ bấm hơn A, nhưng vẫn là tool tự mở trang. Amazon có thể chặn hoặc bắt captcha trên chính tài khoản anh.
  Gặp chặn thì dừng và báo, không vượt captcha.
- Đề xuất chỉ làm khi A đã chạy ổn, và là nút anh tự bấm, không chạy theo lịch.

### Cách C · Keepa API bằng key của anh (anh chốt: làm sau A, tuỳ chọn, trả phí)

- Keepa có sẵn danh sách best seller theo chuyên mục, BSR tổng và **lịch sử BSR nhiều năm**. Nhờ đó cột BSR theo tháng
  có số ngay từ ngày đầu, và ước doanh thu có cho cả 500 cuốn.
- Giá: gói API thấp nhất €49 / tháng cho 20 token / phút, mỗi sản phẩm tốn 1 token. Số này lấy từ
  [trang tổng hợp giá Keepa](https://revenuegeeks.com/keepa-pricing/) và [tài liệu token của Keepa](https://keepa.com/api-docs/plans-tokens.html),
  đọc ngày 2026-11-09. Giá chính thức đọc lại trên trang Keepa trước khi làm. Số token của lệnh best seller: `chưa đo`.
- 20 token / phút → 500 cuốn mất khoảng 25 phút cho mỗi lượt làm mới. Chạy nền, có thanh tiến độ.
- Key nằm ở máy anh như các key khác (Cài đặt). ShotMatic không bán lại dữ liệu Keepa.

**Anh chốt 2026-11-09:** làm A trước (M1–M4), xong A mới làm C, là nút nâng cấp cho người đã có key Keepa (M5). B chưa làm.

## BSR theo tháng

- **Không có Keepa:** mỗi lần chụp (trang Best Sellers hoặc trang sách) lưu 1 dòng `ASIN · chuyên mục · hạng · BSR · ngày`.
  Bảng `book_bsr_log` đã có từ 4.3 M7, thêm cột hạng chuyên mục. Cột tháng lấy điểm cuối của mỗi tháng. Ngày đầu cột
  này **trống**, chụp càng đều thì càng nhiều điểm. Màn hình ghi rõ "Bắt đầu theo dõi ngày …".
- **Có Keepa:** lấy lịch sử BSR 12 tháng gần nhất, gộp theo tháng (trung vị trong tháng), ghi nguồn "Keepa".
- Hai nguồn không trộn lẫn trên một đường: điểm tự chụp vẽ chấm đặc, điểm Keepa vẽ đường nhạt, chú thích ghi rõ.

## Ước doanh thu

Đây là **đổi luật** so với 4.3 (mục 8 của trang đó ghi "Không ước doanh thu từ BSR khi chưa có nguồn đo"). Cách làm
để không bịa số:

1. Chỉ ước khi có **BSR tổng** của đúng định dạng: Kindle tính theo BSR Kindle Store, sách in tính theo BSR Books.
2. BSR → số bán / ngày bằng **2 đường cong đã công bố**, cho ra khoảng thấp–cao, không phải 1 con số. Ví dụ ở BSR Kindle
   5.000, các nguồn cho khoảng 25–40 cuốn / ngày ([Kindlepreneur](https://kindlepreneur.com/amazon-kdp-sales-rank-calculator/),
   [Vappingo](https://www.vappingo.com/word-blog/kdp-bsr-sales-estimator/), đọc 2026-11-09). Các nguồn này lệch nhau,
   nên màn hình hiện cả khoảng và ghi tên nguồn.
3. Doanh thu / tháng = bán / ngày × 30 × giá. Royalty (tiền tác giả nhận) là dòng phụ: Kindle 70% giá trong khoảng
   2,99–9,99 USD; sách in 60% giá trừ phí in. Công thức phí in đọc lại trên trang trợ giúp KDP trước khi code (`chưa đo`).
4. Mỗi ô doanh thu có chữ "ước", rê vào thấy: BSR dùng, ngày chụp, 2 nguồn đường cong, cách nhân.
5. Thêm test: 3 mốc BSR (1.000 / 10.000 / 100.000) cho ra đúng khoảng của 2 nguồn đã ghi trong code.

## Các bước

### M1 · Đo trên Amazon thật (Chrome của anh)

- Mở trang Best Sellers của 3 chuyên mục sách US, lưu HTML làm fixture test. Ghi lại: bao nhiêu cuốn / trang, trang 2
  lấy bằng cách nào, mỗi ô sách có những chữ gì, Kindle và sách in có chung danh sách không.
- Chọn sẵn 10 chuyên mục mẫu cho chợ US (danh sách để anh duyệt).

### M2 · Bộ đọc trang Best Sellers trong Scout

- `extension-amazon/lib/bestsellers.js`: HTML trang Best Sellers → danh sách `{ rank, asin, title, author, price,
  format, rating, reviews, image }` + tên chuyên mục + id chuyên mục (node) + chợ.
- Nút *Copy for ShotMatic* trên trang Best Sellers, và ô dán HTML trong app (giống 4.3).
- Test bằng fixture M1 trong `web/tests/extension-amazon.test.ts`.

### M3 · Lưu + trang Book Discover

- Bảng `book_categories` (chuyên mục đã lưu, bật / tắt, chợ) và `book_category_snapshot` (mỗi lần chụp: ngày, chuyên
  mục, ASIN, hạng). Ghi thêm vào `book_bsr_log` khi có BSR.
- Trang `/amazon/discover`: thanh chip chuyên mục, dải số tóm tắt, bảng top sách có lọc + sắp + phân trang, khung chi tiết.
  Cờ nước dùng `Flag` có sẵn.
- Soát layout ở 960px và 1340px, sáng + tối, English + tiếng Việt, với 500 dòng và tên sách dài nhất.

### M4 · BSR theo tháng + ước doanh thu

- Gộp `book_bsr_log` theo tháng, vẽ sparkline trong bảng và biểu đồ trong khung chi tiết.
- Hàm ước doanh thu theo [mục trên](#uoc-doanh-thu) + test 3 mốc.
- Tab *Sách mới lọt top* và *Lên / xuống mạnh nhất* (so 2 lần chụp gần nhất).

### M5 · Keepa (tuỳ chọn)

- Ô key Keepa trong Cài đặt, nút *Cập nhật bằng Keepa* chạy nền có tiến độ + đếm token còn lại.
- Lấy best seller theo chuyên mục, BSR tổng, lịch sử BSR 12 tháng. Ghi nguồn "Keepa" vào từng điểm.

### M6 · Nối với phần có sẵn

- Nút **Theo dõi** → BSR watchlist của 4.3. Nút **Tra keyword này** → chế độ Books ở 4.3.
- Hỏi AI: gửi top sách đang lọc (đã rút gọn) cho AI hỏi "chuyên mục nào đang có sách tự xuất bản lọt top nhiều nhất".
- Bản demo site: chụp sẵn 2–3 chuyên mục để người chưa tải app xem được.

## Rủi ro + luật

- **Amazon đổi HTML** → bộ đọc hỏng. Có fixture test, trang đọc lỗi thì báo "đọc được 0 cuốn" chứ không im lặng.
- **Ước doanh thu sai lệch lớn**, nhất là chuyên mục nhỏ. Luôn hiện khoảng + nguồn, không hiện 1 con số "chắc chắn".
- **Hạng trong chuyên mục ≠ BSR tổng.** Bảng ghi rõ 2 cột riêng, không gộp.
- **Cách B có thể làm Amazon chặn tài khoản anh.** Chỉ chạy khi anh bấm, có khoảng nghỉ, gặp chặn thì dừng.
- Không vượt captcha, không bấm "Continue" trên trang chặn, không chạy theo lịch tự động.

## Không làm

- Không để server hay trình duyệt AI tự tải trang Amazon.
- Không tự ước "lượt tìm / tháng".
- Không ước doanh thu khi chưa có BSR tổng (chỉ có hạng chuyên mục thì để "—").
- Không làm chợ ngoài US ở bản đầu. Thêm chợ sau khi US chạy ổn.

## Xong khi

- [ ] M1: 3 trang Best Sellers đã lưu làm fixture, đã ghi số cuốn / trang
- [ ] M2: đọc đúng 50 cuốn từ mỗi fixture, test xanh
- [ ] M3: 10 chuyên mục × 50 cuốn trong 1 bảng, lọc theo chuyên mục + định dạng chạy đúng
- [ ] M3: soát 960px + 1340px, sáng + tối, English + tiếng Việt, không cuộn ngang cả trang
- [ ] M4: ước doanh thu có khoảng + nguồn, test 3 mốc BSR xanh
- [ ] M4: sau ≥ 30 ngày, cột BSR theo tháng có ≥ 2 điểm cho sách đã chụp lại
- [ ] `npm run check` xanh, `npm run docs:build` xanh

## Cần anh chốt

1. ~~**Làm ngay hay để sau Marketing?**~~ — đã chốt 2026-11-09: để sau Marketing.
2. ~~**Nguồn số**~~ — đã chốt 2026-11-09: A trước, Keepa (C) sau. Ngày 2026-11-11 anh cho thêm B (Scout tự tải trang sách lấy BSR, có giới hạn).
3. ~~**Đổi luật ước doanh thu**~~ — đã chốt 2026-11-11: cho. Câu hỏi cũ: đồng ý hiện khoảng thấp–cao từ 2 nguồn đã công bố, có ghi nguồn, thay cho luật "không ước" của 4.3?
4. **10 chuyên mục mẫu:** anh có danh sách sẵn, hay để M1 đề xuất cho anh duyệt?
