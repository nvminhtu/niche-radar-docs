# 6 · Bộ tool KDP: sách trend, chuyên mục đang lên, thu nhập, từ khoá

> Plan 2 · mục 6. Gom phần sách của ShotMatic thành **4 tool KDP nhỏ**, dùng chung một nền số liệu:
> sách nào đang bán, BSR ra sao, thuộc niche nào, dùng keyword gì, ước thu nhập tháng bao nhiêu, chuyên mục nào đang lên.
> Trang này thay cho 2 plan riêng trước đó: [6.3 Book Discover](phase-plan2-06-book-discover.md) (mục 6 cũ) và
> [6.1 Từ khoá + cạnh tranh](phase-plan2-07-kdp-nang-cap.md) (mục 7 cũ). 2 trang đó giữ làm phần chi tiết kỹ thuật.

<span class="chip chip--todo">Plan 2026-11-11 · để sau Marketing · chưa làm</span>

<div class="box" markdown>
**Đổi 2026-11-14 ([mục 12](phase-plan2-12-san-sach.md)):** máy chủ app **được tự đọc** trang Amazon (bảng xếp hạng, trang sách,
trang tìm) có giới hạn: nghỉ 5–8 giây / trang, ≤ ~35 trang / lượt săn, gặp captcha thì dừng. Các chỗ dưới đây ghi "Scout tải trang",
"dán gói Scout" nay do app làm; Scout không còn cần cho app.
</div>

<div class="box box--danger" markdown>
**Nhắc quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho bán hàng + SEO + GEO
([Marketing](../marketing/index.md)). Plan này viết sẵn, **code sau Marketing**.
</div>

<div class="box box--goal" markdown>
**Đích**

- **4 tool**, mỗi tool trả lời 1 câu hỏi:
    1. **Sách đang trend** — sách nào đang lên, thuộc niche nào, keyword gì?
    2. **Chuyên mục đang lên** — chuyên mục nào đang nóng, top sách ở đó là thể loại gì?
    3. **Thu nhập sách** — mỗi cuốn bán được khoảng bao nhiêu / tháng, keyword và niche của nó là gì?
    4. **Từ khoá + cạnh tranh** — Amazon gợi ý keyword nào, chen vào có dễ không?
- Mọi con số ghi **đo ngày nào, từ trang nào**. Số ước (thu nhập) luôn là **khoảng thấp–cao + tên nguồn**.
- **AI đọc lại** các số đã có để kết luận. Số thiếu hoặc lệch thì AI nói là thiếu / lệch, không đoán ra số thay.

**Xong khi:** đã chạy thật trên Chrome của anh, chợ US: tool 1 đọc được 2 trang Movers & Shakers (Books + Kindle),
tool 2 đọc 10 chuyên mục × 50 cuốn, tool 3 ra khoảng thu nhập cho mọi cuốn có BSR tổng, tool 4 chạy 3 chủ đề rộng.
Mỗi tool đứng được ở 960px và 1340px, cả English lẫn tiếng Việt.
</div>

## Anh chốt 2026-11-11: 2 luật mới

<div class="box" markdown>
**1 · Scout được tự tải trang sách để lấy BSR** (trước đây chưa cho, gọi là "Cách B" ở trang 6.3)

- Học DS Amazon Quick View: trên trang danh sách sách (Best Sellers, Movers & Shakers, New Releases, trang tìm, trang
  Amazon Books store), dưới mỗi cuốn hiện **BSR tổng + 3 hạng chuyên mục + ASIN**. DS Quick View làm việc này bằng cách tự
  tải trang từng cuốn ("Loading rank…"), lịch sử BSR thì bắt trả tiền.
- Giới hạn của Scout:
    - chỉ chạy khi anh **bấm nút** *Lấy BSR* trên trang đang mở, không chạy theo lịch, không chạy nền khi anh không xem;
    - tải trang sách bằng phiên Chrome của anh (`fetch` trang `/dp/<ASIN>`), **không mở tab mới**;
    - **tối đa 20 cuốn / lần bấm**, nghỉ ngẫu nhiên 4–8 giây giữa 2 cuốn;
    - gặp trang captcha, "Robot check" hay lỗi 503 thì **dừng ngay**, giữ phần đã lấy, báo cuốn nào chưa có;
    - giới hạn mỗi ngày: `chưa đo`, chốt sau M1.
- Máy chủ ShotMatic và trình duyệt AI vẫn **không** tự tải trang Amazon. Luật này chỉ mở cho Scout trong Chrome của anh.
- **Rủi ro:** Amazon có thể bắt captcha hoặc chặn chính tài khoản anh. Ngày 2026-11-05, server tự tải bị chặn sau 61 trang.
  Tải từ Chrome người dùng: `chưa đo`, M1 đo trước khi code.

**2 · Hiện ước thu nhập dạng khoảng thấp–cao có ghi nguồn** (thay luật "không ước doanh thu từ BSR" của
[4.3 mục 8](phase-55-2-amazon-books.md#8-khong-lam))

- Cách tính viết sẵn ở [6.3 mục Ước doanh thu](phase-plan2-06-book-discover.md#uoc-doanh-thu): BSR tổng đúng định dạng →
  bán / ngày theo 2 đường cong đã công bố → × 30 × giá → khoảng. Royalty là dòng phụ.
- Không có BSR tổng (chỉ có hạng chuyên mục) thì ô thu nhập để "—".
</div>

## Nền chung: Scout đọc trang danh sách sách

Cả 4 tool lấy số từ cùng một chỗ, nên làm nền trước.

- **Trang Scout đọc được** (anh tự mở): Best Sellers từng chuyên mục, Movers & Shakers, New Releases, trang tìm mục
  Books / Kindle, trang Amazon Books store (như link anh gửi ngày 2026-11-11), trang 1 cuốn sách.
- **Mỗi cuốn đọc được trên trang danh sách:** ASIN, tên, tác giả, ảnh bìa, định dạng, giá, rating, số rating, hạng trong
  danh sách. Trang Movers & Shakers còn có hạng bán hôm nay so với hôm qua. Định dạng chính xác của từng loại trang:
  `chưa đo`, M1 lưu trang thật làm fixture.
- **Bấm *Lấy BSR*** (luật mới 1): Scout tải trang từng cuốn, lấy BSR tổng, 3 hạng chuyên mục, NXB, số trang, ngày ra.
  Dùng lại bộ đọc `parseBookDetails` đã có ở 4.3.
- **Gửi sang ShotMatic** qua localhost (cách viết ở [6.1 phần gửi sang app](phase-plan2-07-kdp-nang-cap.md#gui-sang-app-the-nao)).
  Không có app thì panel Scout vẫn hiện đủ số.
- **Lưu:** mỗi lần chụp 1 dòng `ASIN · chợ · trang nguồn · hạng trong danh sách · BSR tổng · hạng chuyên mục · ngày`.
  Mở rộng bảng `book_bsr_log` đã có. Chụp càng đều thì cột theo ngày / tháng càng nhiều điểm.
- **Niche của 1 cuốn** = chuyên mục nhỏ nhất nó đứng (ví dụ *#4 in 90-Minute Romance Short Reads*). Không đoán thêm.

## 6.1 · Tool 4 — Từ khoá + cạnh tranh

Câu hỏi: *Amazon gợi ý keyword nào, chen vào có dễ không?* Phần này đã có nhiều nhất, làm đầu tiên.

- **Đã có ở 4.3:** gợi ý a–z, số lần gợi ý, hạng gợi ý, làm sạch keyword, cờ thương hiệu, điểm sách 0–100 khi có trang 1,
  7 ô keyword KDP.
- **Thêm (chi tiết ở [6.1](phase-plan2-07-kdp-nang-cap.md)):**
    - panel Scout chấm điểm sách ngay trên trang tìm Books / Kindle, cùng con số với app;
    - gõ 1 chủ đề rộng (*cookbook*) → 30–50 niche sách con xếp theo lần gợi ý + Trends.
- **Thêm nhờ nền chung:** ở trang tìm, bấm *Lấy BSR* cho 10 cuốn đầu → điểm có thêm BSR giữa top 10 (hiện giờ phải mở
  tay từng cuốn).

## 6.2 · Tool 1 — Sách đang trend

<div class="box" markdown>
**Bản gọn đã làm 2026-11-12** (anh mở trước Marketing để điều tra): trang Amazon → chế độ **Sách đang trend**.

- Scout 0.3.0 đọc trang Best Sellers · Movers & Shakers · New Releases (Books + Kindle), nút *Get BSR* đúng luật mới 1,
  gom nhiều trang vào giỏ rồi *Copy for ShotMatic* → dán 1 lần vào app.
- App: 1 bảng mỗi cuốn 1 hàng (hạng danh sách · % tăng hạng · BSR · niche · keyword suy ra · ngày ra · rating · giá ·
  tự xuất bản), lọc + sắp xếp, bảng niche, cụm chữ lặp trong tên sách.
- **Chưa đo:** bộ đọc ô sách viết theo khuôn chữ amazon.com, chưa chạy trên trang thật; số cuốn Amazon chịu cho *Get BSR*
  mỗi ngày.
- **Chưa làm:** kiểm keyword suy ra với ô gợi ý Amazon, gửi thẳng qua localhost (đang qua clipboard), nút ✦ AI, mục KDP riêng
  trên sidebar.
</div>

Câu hỏi: *sách nào đang lên, thuộc niche nào, keyword gì?*

- **Nguồn:** trang Movers & Shakers mục Books và Kindle Store (sách tăng hạng bán mạnh nhất), New Releases, Best Sellers.
  Anh mở trang, Scout đọc. Số cuốn mỗi trang: `chưa đo`.
- **Bảng sách trend**, mỗi cuốn 1 hàng: bìa + tên · % tăng hạng (Movers & Shakers) · BSR tổng · **niche** (chuyên mục
  nhỏ nhất) · **keyword suy ra** · ngày ra · rating · KU · tự xuất bản hay không.
- **Gom theo niche:** niche nào có nhiều sách đang lên nhất, mỗi niche bao nhiêu cuốn tự xuất bản (cửa cho người mới).
- **Keyword suy ra:** lấy cụm 2–4 chữ trong tên + phụ đề sách, bỏ chữ nối, rồi hỏi ô gợi ý Amazon xem cụm đó có người gõ
  không. Giữ cụm được gợi ý, ghi rõ nhãn **"suy ra từ tên sách"**.
- **Không lấy được:** keyword thật mà cuốn đó đang lên hạng (Reverse ASIN, cần dữ liệu Amazon Ads). Không giả vờ có.
- **Bấm 1 niche** → mở tool 4 với niche đó; **bấm 1 cuốn** → tool 3 với cuốn đó.

## 6.3 · Tool 2 — Chuyên mục đang lên

Câu hỏi: *chuyên mục nào đang nóng, top sách ở đó là thể loại gì?* Chi tiết màn hình + nguồn ở
[6.3 Book Discover](phase-plan2-06-book-discover.md).

- **Nguồn:** Best Sellers từng chuyên mục (top 50 / trang), tối đa 10 chuyên mục đang theo dõi; Keepa nếu anh có key.
- **"Đang lên" đo bằng 2 số**, cần ít nhất 2 lần chụp:
    - số sách Movers & Shakers (tool 1) rơi vào chuyên mục đó, tuần này so tuần trước;
    - BSR giữa của top 50 chuyên mục, lần chụp này so lần trước (nhỏ đi = bán chạy hơn).
- Ngày đầu chỉ có 1 lần chụp: màn hình ghi "Bắt đầu theo dõi ngày …", chưa xếp "đang lên". Có Keepa thì có lịch sử ngay.
- **Top sách là thể loại gì:** với mỗi chuyên mục, đếm các chuyên mục con mà top 50 cùng đứng, định dạng (Kindle /
  paperback / hardcover), % tự xuất bản, giá giữa, % trong KU, chữ hay gặp trong tên sách (có sẵn từ 4.3).

## 6.4 · Tool 3 — Thu nhập sách

<div class="box" markdown>
**Bản gọn đã làm 2026-11-13: Soi 1 cuốn sách** (anh mở trước Marketing). Trang Amazon → chế độ thứ tư **Soi 1 cuốn sách**.

- Anh mở trang 1 cuốn sách trong Chrome, bấm Scout *Copy for Niche Radar*, rồi bấm *Dán trang sách* trong app (không có
  extension thì dán HTML nguồn trang). Máy chủ chỉ hỏi ô gợi ý Amazon, không mở trang Amazon.
- **Thẻ sách:** tên, tác giả, định dạng, NXB / tự xuất bản, BSR tổng + chuyên mục (chuyên mục hẹp nhất = niche), giá,
  rating, số lượt chấm, ngày ra, số trang. Dán lại ngày khác thì thấy BSR lên / xuống bao nhiêu bậc.
- **Keyword và thứ hạng:** cụm 2–4 chữ trong tên sách, hỏi ô gợi ý Amazon, giữ tối đa 8 cụm có người gõ. Hạng: anh bấm
  *Mở trang tìm* của từng keyword, chép trang bằng Scout, bấm *Dán trang tìm* → vị trí của cuốn sách trên trang 1, bỏ ô tài
  trợ, riêng Books và Kindle. Dán trang tìm của keyword khác cũng được, máy thêm dòng.
- **Ra tiền ra sao:** anh chốt 2026-11-13 chỉ dùng dòng *“bought in past month”* Amazon tự hiện: số cuốn × giá = doanh thu
  / tháng **mức sàn**. Trang không có dòng đó thì ghi `chưa đo`. **Không đổi BSR ra số bán**: Kindlepreneur, Vappingo,
  TCK Publishing không công bố bảng BSR → số bán (đọc 2026-11-13). Royalty tác giả: `chưa đo`.
- **Nút ✦ AI** gửi mọi số trên cho AI: niche thật, keyword, có tiền không, sách mới nên làm khác gì, đo gì tiếp.
- Scout **0.3.1** chép thêm tác giả, định dạng, giá, rating, số lượt chấm, dòng bought, ảnh bìa. **Chưa đo:** các ô này
  viết theo khuôn trang amazon.com, chưa chạy trên trang thật (Claude không được mở Amazon).
- **Chưa làm:** bảng thu nhập nhiều cuốn, ước theo BSR khi không có dòng bought, royalty, review.
</div>

Câu hỏi: *mỗi cuốn bán được khoảng bao nhiêu / tháng, keyword và niche của nó là gì?*

- **Bảng sách** từ mọi lần chụp (tool 1, 2, 4), lọc theo niche, định dạng, chuyên mục, tự xuất bản. Cột: bìa + tên ·
  định dạng · giá · BSR tổng · **bán / ngày (khoảng)** · **thu nhập / tháng (khoảng)** · royalty ước · niche · keyword suy ra
  · BSR theo tháng (sparkline).
- **Cách tính:** luật mới 2. Rê vào ô thu nhập thấy BSR dùng, ngày chụp, 2 nguồn đường cong, cách nhân.
- **Tổng theo niche:** thu nhập giữa của top 10 trong niche, số cuốn > 1.000 USD / tháng (ước). Đây là số để chọn niche,
  không phải để hứa với người dùng.
- Công thức phí in của sách in và royalty: đọc lại trang trợ giúp KDP trước khi code (`chưa đo`).

## AI đọc lại

Mỗi tool có nút ✦ (dùng `AiMagic` có sẵn). AI chỉ đọc số đã đo trên màn hình:

- **Kết luận:** niche nào đáng làm, góc khác biệt, định dạng nên chọn, vì sao, kèm số làm bằng chứng.
- **Số không ổn thì nói:** thiếu BSR, mới chụp 1 lần, 2 nguồn lệch nhau (BSR tự chụp so với Keepa), chuyên mục quá ít sách
  → AI ghi rõ chỗ thiếu và đề xuất trang nào nên mở thêm. **AI không tự điền số thay.**
- Niche sức khoẻ không hứa chữa bệnh; nhắc KDP bắt khai nội dung do AI tạo (luật có sẵn ở 4.3).

## Màn hình

- Sidebar có mục **KDP** riêng (anh chốt 2026-11-11; thay chế độ *Sách* trên trang Amazon), 4 tab theo thứ tự làm: **Từ khoá** · **Sách trend** ·
  **Chuyên mục** · **Thu nhập**. Trang Amazon trở về chỉ tra hàng hoá.
- Mỗi tab đọc từ trên xuống: ô tra / chọn nguồn → dải số ngắn → bảng → nút ✦ AI. Bước lấy số dùng thẻ *Bước tiếp theo*
  đã làm ở gói A (2026-11-09).
- Bảng: cột đầu dính trái, bấm tên cột để sắp, chữ dài 1 dòng + rê xem đủ.

## Đối thủ đang làm gì

- **DS Amazon Quick View** (extension): BSR + hạng chuyên mục + ASIN dưới mỗi sản phẩm trên mọi trang danh sách; lịch sử BSR
  phải trả tiền (bản Extended). Không nói niche, không gom, không ước thu nhập.
- **Publisher Rocket, KDSPY, BookBeam, Book Bolt:** keyword + ước doanh thu + theo dõi hạng, trả phí. Bảng so ở
  [4.3 mục 4](phase-55-2-amazon-books.md#4-oi-thu).
- **Khác của ShotMatic:** miễn phí trong Scout, gom thẳng ra niche + keyword, AI đọc lại số, nối sang tra app / Trends.

## Các bước

Thứ tự: nền → tool 4 → tool 1 → tool 2 → tool 3. Tool 3 cần BSR từ 3 tool trước nên làm cuối.

### M1 · Đo trên Chrome của anh

- Lưu làm fixture: Movers & Shakers (Books, Kindle), Best Sellers 3 chuyên mục, New Releases, trang Amazon Books store,
  trang tìm Books + Kindle.
- Thử *Lấy BSR* bằng tay cho 20 cuốn, 4–8 giây / cuốn: mất bao lâu, có gặp captcha không. Từ đó chốt giới hạn mỗi ngày.
- Đếm số cuốn mỗi loại trang, cách Amazon ghi % tăng hạng trên Movers & Shakers.

### M2 · Nền: bộ đọc trang danh sách + Lấy BSR + gửi sang app

- `extension-amazon/lib/`: bộ đọc từng loại trang danh sách (test bằng fixture M1), hàm *Lấy BSR* có giới hạn + dừng khi
  gặp chặn (test bằng trang captcha giả).
- Endpoint nhận trang từ Scout ở `web/src/server/social-api.ts`, mở rộng `book_bsr_log`.
- Scout 0.3.0: panel BSR dưới mỗi cuốn + nút gửi.

### M3 · Tool 4 (6.1)

- Làm 7.1 + 7.2 của trang [6.1](phase-plan2-07-kdp-nang-cap.md), thêm *Lấy BSR* cho 10 cuốn đầu trang tìm.

### M4 · Tool 1 (6.2)

- Bảng sách trend, gom niche, keyword suy ra (hàm thuần + test: cụm lấy từ tên, giữ cụm được gợi ý, bỏ cụm là tên tác giả).

### M5 · Tool 2 (6.3)

- Theo dõi 10 chuyên mục, 2 số "đang lên", thể loại top sách. M1–M3 của trang 6.3.

### M6 · Tool 3 (6.4)

- Khoảng thu nhập + royalty, test 3 mốc BSR (1.000 / 10.000 / 100.000) ra đúng khoảng của 2 nguồn. M4 của trang 6.3.

### M7 · Keepa (tuỳ chọn)

- Nút nâng cấp cho người có key Keepa: lịch sử BSR 12 tháng, best seller theo chuyên mục. M5 của trang 6.3.

### M8 · Mục KDP trên sidebar + bài blog

- Dời chế độ Sách sang mục KDP 4 tab. Soát 960px + 1340px, sáng + tối, English + tiếng Việt.
- Khi Marketing mở lại việc viết bài: 1 bài shotmatic.app/blog từ số thật của tool 1 hoặc 2 (skill `shotmatic-blog`).

## Rủi ro

- **Amazon chặn tài khoản anh vì Lấy BSR.** Giới hạn 20 cuốn / lần, nghỉ 4–8 giây, dừng khi gặp chặn, M1 đo trước.
  Điều khoản Amazon cấm tool tự động truy cập; đây là quyết định anh chốt ngày 2026-11-11, chạy trên tài khoản của anh.
- **Chrome Web Store** có thể hỏi vì sao Scout tải trang Amazon và gọi localhost. Ghi rõ lý do trong store listing.
- **Ước thu nhập lệch xa**, nhất là chuyên mục nhỏ. Luôn là khoảng + nguồn, có chữ "ước".
- **Amazon đổi HTML** → bộ đọc hỏng. Fixture test; đọc được 0 cuốn thì báo, không im lặng.
- **"Đang lên" cần thời gian.** Tool 2 vô nghĩa nếu chỉ chụp 1 lần; màn hình nói rõ điều này.

## Không làm

- Máy chủ ShotMatic hoặc trình duyệt AI tự tải trang Amazon.
- Scout chạy theo lịch hoặc mở tab mới khi anh không bấm.
- Số "lượt tìm / tháng" tự tính; Reverse ASIN (keyword thật của 1 cuốn).
- Vượt captcha.
- Chợ ngoài US ở bản đầu.

## Cần anh chốt

1. ~~Scout tự tải trang sách lấy BSR~~ — đã chốt 2026-11-11: cho, có giới hạn.
2. ~~Ước thu nhập dạng khoảng~~ — đã chốt 2026-11-11: cho, có nguồn.
3. ~~Mục KDP riêng trên sidebar hay giữ chế độ Sách~~ — đã chốt 2026-11-11: **mục KDP riêng trên sidebar**, 4 tab.
4. **10 chuyên mục mẫu cho tool 2:** anh có sẵn, hay để M1 đề xuất cho anh duyệt?
