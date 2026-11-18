# 12 · Săn sách cầu > cung (bỏ Scout)

> Plan 2 · mục 12. Trang Amazon Books có lối vào **Săn sách**: app tự đọc các bảng xếp hạng sách Amazon → gom tới 100 cuốn →
> lọc ra cuốn **mới, ít review mà bán mạnh, và chủ đề có người gõ tìm** → soi sâu 20 cuốn → chốt 5 cuốn.
> Cùng lúc **bỏ extension Scout khỏi app**: Soi 1 cuốn sách chỉ cần dán link / ASIN.

<span class="chip chip--done">Anh duyệt 2026-11-14 · đã code</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Anh mở mục này ngày 2026-11-14.
</div>

## Ý tưởng: cùng luật cung – cầu bên YouTube

Bên YouTube: kênh **nhỏ** mà view **gấp nhiều lần sub** → người xem tìm tới nhiều hơn số kênh đang làm.
Bên sách, bản tương đương:

| YouTube (mục 11) | Sách (mục này) |
|---|---|
| kênh nhỏ (ít sub) | sách **ít review** (người mới) |
| kênh mới mở | sách **phát hành gần đây** |
| view nổ | **BSR tốt** (bán mạnh) |
| có người gõ trên YouTube | cụm chủ đề trong tên sách **được ô gợi ý Amazon trả về** |
| nhiều kênh nhỏ cùng nổ | trong **niche** của sách, nhiều sách mới / ít review cũng lọt top |

Phân biệt rõ 2 loại sách cùng BSR tốt:

- **Cầu > cung** — sách mới, ít review, chủ đề có người gõ tìm, niche còn chỗ cho người mới → làm được.
- **Trend nhưng không ai tìm** — BSR tốt nhưng 0 cụm nào trong tên được Amazon gợi ý: bán nhờ tên tác giả, quảng cáo,
  TikTok, series cũ… → người mới khó chen, gắn nhãn riêng, không xếp vào top.

## Đã đo trước khi làm (2026-11-14, máy dev ở VN, gọi thẳng từ máy chủ app, không Scout)

- Best Sellers **Kindle Store**: HTTP 200, có danh sách 50 cuốn (hạng + ASIN), 30 cuốn đầu có sẵn tên, tác giả, sao, số review, giá.
- Best Sellers **Books**: HTTP 200, có danh sách 50 cuốn.
- Movers & Shakers **Books**: HTTP 200 nhưng **0 cuốn** trong bảng (lần đo này) → bảng nào trả 0 cuốn thì báo trên màn hình, không im lặng.
- Trang 1 cuốn `/dp/<ASIN>`: HTTP 200, đọc được BSR tổng + 3 hạng niche, ngày phát hành, số trang, số review, **mô tả sách**.
- Không gặp captcha trong 5 lần gọi cách nhau ≥ 6 giây. Đo cũ 2026-11-05: trang tìm bị chặn sau **61 trang** → mỗi lần săn giữ dưới ~35 trang.

## Phễu 3 bước, mỗi bước 1 nút

### Bước 1 · Lưới rộng (~40 giây, ≤ 8 trang)

Chọn chợ (US mặc định), loại (Kindle / Books / cả hai), và chuyên mục lớn (tất cả / Self-help / Romance / Children's…).
App đọc **Movers & Shakers + New Releases + Best Sellers** của lựa chọn đó, bỏ trùng, giữ tối đa 100 cuốn.
Mỗi cuốn có: hạng trong bảng, % tăng hạng (Movers), tên, tác giả, sao, số review, giá. Nghỉ 5–8 giây giữa 2 trang.

### Bước 2 · Lọc nhanh, chưa mở trang sách (~50 giây)

Hỏi ô gợi ý Amazon cho cụm chủ đề chính trong tên mỗi cuốn (đường an toàn, đã chạy ~810 lần không bị chặn).
4 chip lọc, đổi chip là phễu đổi ngay:

- Ít review: dưới 500 (100 / 500 / 2.000 / tắt)
- Có người gõ: ≥ 1 cụm được Amazon gợi ý (bật / tắt)
- Bỏ tác giả lớn: tác giả có ≥ 2 cuốn trong 100 cuốn (bật / tắt)
- Hạng bảng: top 50 (20 / 50 / 100)

Xếp theo **sức bán ÷ số review** (giống view ÷ sub). 20 cuốn đầu được tick sẵn, anh bỏ / thêm được.

### Bước 3 · Soi sâu 20 cuốn → chốt 5 (~3 phút, ≤ 25 trang)

Mở trang từng cuốn đã tick (nghỉ 5–8 giây), rồi đọc bảng Best Sellers của **niche** (chuyên mục nhỏ nhất) của 5 cuốn đứng đầu
để đo phía cung. Mỗi cuốn có điểm 0–100:

| Phần | Điểm | Đủ điểm khi |
|---|---|---|
| Bán mạnh | 30 | BSR tổng ≤ 2.000 (giảm dần tới 100.000) |
| Mới mà lên được | 25 | phát hành ≤ 90 ngày **và** < 200 review (giảm dần tới 1 năm / 2.000 review) |
| Có người gõ | 25 | ≥ 3 cụm trong tên / niche được Amazon gợi ý |
| Niche còn chỗ | 20 | trong top 50 của niche, ≥ 30% là sách < 100 review |

Nhãn kèm điểm: **Cầu > cung** · **Trend không ai tìm** · **Niche đông** (top niche toàn sách > 2.000 review).
Mọi ngưỡng là quy ước của ShotMatic, không phải số đo. Sửa ở `web/src/lib/book-hunt.ts`.

## Trang chi tiết 1 cuốn (Soi 1 cuốn sách, nâng cấp)

- **Số lớn:** điểm / 100 + nhãn, BSR tổng + hạng 3 niche, ngày phát hành (bao nhiêu ngày), số review, giá, "bought in past month".
- **SEO trên Amazon:** tên + phụ đề (độ dài, cụm nào trong đó được Amazon gợi ý), chuyên mục sách đang đứng, có A+ content không,
  series, số trang, nhà xuất bản (tự xuất bản hay NXB).
- **Keyword:** cụm rút từ tên + phụ đề + mô tả, gắn nhãn *Amazon gợi ý* (có người gõ). Bấm để tra ở chế độ Books · Kindle.
- **Nội dung:** mô tả sách (gập, 4 dòng), cụm lặp nhiều trong mô tả. Nút ✦ AI: tóm tắt sách nói về gì, cho ai, góc nào khác.
- **Thu nhập:** "bought in past month" × giá (mức sàn) như hiện tại. Không đổi BSR ra số bán.
- **Niche:** 5 sách mới nhất trong top niche + số review của chúng (thấy được người mới có chen được không).

## Bỏ Scout khỏi app

| Chỗ | Bây giờ | Sau |
|---|---|---|
| Soi 1 cuốn sách | mở trang trong Chrome → Scout copy → dán | **dán link / ASIN → app tự đọc** (~5 giây) |
| Sách đang trend | mở 6 trang danh sách → Scout → dán | thay bằng **Săn sách** (app tự đọc bảng) |
| Books · Kindle · Hardcover | dán trang tìm qua Scout / HTML | app tự đọc trang tìm như chế độ Tất cả sản phẩm |
| Lúc Amazon chặn | — | báo rõ "Amazon tạm chặn, thử lại sau 1 giờ", giữ ô dán HTML (gập) làm đường dự phòng |

- Xoá mọi chữ, nút, link nhắc Scout trên giao diện app.
- Folder `extension-amazon/` **giữ lại** vì bộ đọc số Amazon (`lib/`) đang dùng chung với app; không ra bản Scout mới, đánh dấu ngừng trong README.

## Giới hạn

- Amazon có thể chặn máy chủ (đo cũ: sau 61 trang). Mỗi lần săn ≤ ~35 trang, nghỉ 5–8 giây, gặp captcha / 503 thì dừng và giữ phần đã đọc.
  Không vượt captcha, không proxy, không đăng nhập.
- "Có người gõ" = ô gợi ý Amazon có trả cụm đó, **không** phải số lượt tìm (Amazon không công bố).
- Bảng xếp hạng đổi theo giờ; điểm là ảnh chụp lúc săn. Sách ≠ niche: chắc hơn khi 2–3 cuốn mới cùng niche cùng lên.

## Chạy thật lần đầu (2026-11-14, US · Kindle · mọi chuyên mục)

- **Bước 1:** đọc 3 bảng → 44 cuốn (New Releases 30 · Best Sellers 30, trùng bỏ). Bảng Movers & Shakers Kindle trống —
  chính Amazon ghi "there are no movers and shakers available in this category" (cả Kindle eBooks lẫn Kindle Store gốc);
  app ghi rõ *Amazon đang để trống bảng này*.
- **Bước 2:** hỏi ô gợi ý Amazon → còn 4 cuốn dưới 500 review (top Kindle mọi chuyên mục gần như toàn tác giả lớn —
  chọn 1 chuyên mục / dán link niche sâu sẽ ra nhiều sách mới hơn).
- **Bước 3:** đọc 4 trang sách + 4 bảng niche → điểm 80 / 77 / 72 / … Cuốn đầu bị nhãn *Niche đông* (Cozy Mystery: 2/30 cuốn
  top dưới 100 review, trung vị 1.475 review); cuốn *Small Town Romance* được *Cầu > cung* (4/30, trung vị 822).
- Cả lượt ~14 trang Amazon, không bị chặn. Sửa sau khi chạy: tên NXB nuốt đoạn "Editorial Reviews" (cần dấu `:`),
  mô tả dính đuôi "Report an issue…", số review xuống dòng.

## Code

- Thu số: `web/src/collectors/amazon-lists.ts` (đọc bảng xếp hạng + phần thêm của trang sách, hàng đợi 5–8 giây riêng).
- Lọc, chấm điểm: `web/src/lib/book-hunt.ts` (thuần) + `web/src/lib/book-hunt-run.ts` (3 bước, gọi mạng).
  Soi 1 cuốn: `web/src/lib/book-audit.ts` nhận link / ASIN (`runBookAuditUrl`).
- API: `POST /api/social/books/hunt`, `POST /api/social/books/audit` nhận `{url}`, `POST /api/social/:id/fetch` (đo hạng keyword,
  đọc trang tìm Books / Kindle) — thay các chỗ phải dán gói Scout. Bỏ `/books/trend` và chế độ *Sách đang trend*.
- Giao diện: `web/src/client/BookHunt.tsx` (thay `BookTrend.tsx`), sửa `BookAudit.tsx`, `BooksResearch.tsx`. Test: `web/tests/book-hunt.test.ts`.
