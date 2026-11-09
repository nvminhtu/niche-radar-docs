# 1.3 · Extension Chrome "ShotMatic Scout" cho Amazon (Backlog 28)

> Extension miễn phí hoàn toàn cho người bán Amazon / KDP: keyword dài từ ô tìm kiếm Amazon, chấm độ cạnh tranh ngay
> trên trang kết quả, BSR trên trang sản phẩm. Mục tiêu: thêm một cửa vào shotmatic.app từ nhóm người tìm "amazon keyword tool".

<span class="chip chip--doing">Bản 0.1.0 xong 2026-11-02 · chạy thử với trang Amazon thật · chờ ảnh store + tải lên Chrome Web Store</span>

## Vì sao

- Người bán Amazon / KDP cũng đi tìm niche, và họ tìm tool trên Chrome Web Store bằng chữ "amazon keyword", "product research".
  ShotMatic Lite chỉ bắt được nhóm chữ ASO → listing thứ hai bắt thêm nhóm chữ khác.
- **Miễn phí hết, không giới hạn lượt:** extension không có server, mọi lượt gọi đi từ máy người dùng → không tốn tiền chạy.
- Cầu sang ShotMatic: mỗi keyword Amazon có ô "Could this be an app instead?" (đếm app trên App Store) + nút
  "Full app niche report in ShotMatic →" kèm UTM `utm_campaign=shotmatic_scout`.

## Làm được không (soát 2026-11-02) → Được

| Dữ liệu | Lấy ở đâu | Đã thử |
|---|---|---|
| Gợi ý keyword | API autocomplete công khai của Amazon (`completion.amazon.*`), không cần key | 10 chợ trả gợi ý đúng tiếng: US, CA, MX, UK, DE, FR, IT, ES, AU, JP. India: không trả JSON |
| Mở rộng a–z | 27 lượt gọi ("kw", "kw a"… "kw z") | 27 lượt liền nhau vẫn trả đủ 10 gợi ý mỗi lượt; extension gọi 3 lượt một lúc. "yoga mat" ra 250 keyword |
| Tổng kết quả | dòng "1-48 of over 7,000 results" trên trang tìm kiếm | đọc được |
| Rating, số rating | `.a-icon-alt` + `aria-label="46,855 ratings"` của từng ô kết quả | đọc được |
| Nhu cầu | badge Amazon tự hiện "10K+ bought in past month" | đọc được (mức sàn, không phải doanh số thật) |
| Sponsored | nhãn `.puis-sponsored-label-text` | đọc được. Một ASIN hay hiện 2 lần (1 ô Sponsored + 1 ô thường) → đếm 1 lần |
| BSR | bảng "Best Sellers Rank" trên trang sản phẩm | đọc được, kể cả khi innerText dồn 1 dòng |
| App Store | iTunes Search API (công khai) | gọi được |

**Không làm:** ước doanh số từ BSR (không có nguồn đo — luật "không bịa số"), lượng tìm kiếm (Amazon không công bố),
tải trang sản phẩm chạy ngầm (dễ dính captcha, store duyệt khó hơn). Chỉ đọc trang người dùng đang mở + autocomplete.

## Đối thủ trên Chrome Web Store (tìm 2026-11-02)

- **Bản miễn phí của bộ trả phí:** Helium 10 (gói free giới hạn), SellerSprite (giới hạn lượt/ngày), AMZScout Unicorn Smasher,
  SellerApp. Phần lớn bắt đăng ký tài khoản.
- **Tool lẻ miễn phí:** AMZ Suggestion Expander, Helium 10 Search Expander, Ultra Amazon Suggestion Expander (gợi ý a–z),
  Amz Keyword Extractor, DS Amazon Quick View.
- **Chỗ trống:** chưa thấy cái nào gộp *keyword a–z + chấm cạnh tranh trên trang + không bắt đăng ký*, và không cái nào hỏi
  "keyword này làm thành app được không".
- Lượt cài, rating từng extension: `chưa đo`.

Nguồn: [SellerSprite blog](https://www.sellersprite.com/en/blog/Best-Chrome-Extensions-for-Amazon-Sellers) ·
[amazonseo.ai](https://www.amazonseo.ai/blog/best-free-chrome-extensions-for-amazon-sellers) ·
[Salesduo](https://salesduo.com/blog/amazon-search-suggestion-expander-keyword-research/) ·
[Ultra Amazon Suggestion Expander](https://chromewebstore.google.com/detail/johgeokkpfohidfdpfdlojhpaplodjbk) ·
[Amz Keyword Extractor](https://chromewebstore.google.com/detail/camhpbickjmpmjbcegmdhlckfdkhkbfb)

## Vì sao extension riêng, không gộp vào ShotMatic Lite

- Thêm quyền `amazon.*` vào Lite → Chrome tắt Lite ở máy người dùng cũ tới khi họ bấm đồng ý quyền mới.
- Listing riêng có tên + mô tả riêng → được tìm thấy bằng nhóm chữ Amazon, không làm loãng chữ ASO của Lite.
- Hai extension chung icon, chung màu, chung trang đích; UTM khác nhau để đo riêng.

## Bản 0.1.0 đã làm (2026-11-02)

Code ở folder `extension-amazon/` (README trong đó có cách chạy thử + đóng gói). Test logic: `web/tests/extension-amazon.test.ts`.

- **Card trên trang tìm kiếm Amazon:** keyword + chợ, kết luận Room to enter / Competitive / Crowded kèm lý do (median rating
  top 10 ô thường, bao nhiêu ô dưới 100 rating, bao nhiêu ô 1K+ rating, tổng badge "bought", số ô Sponsored, keyword đúng
  trong tên). Chip số: tổng kết quả, ★ trung bình, số Sponsored, bought/tháng. Danh sách 5 ô thường đầu.
- **Card trên trang sản phẩm:** rating, số rating, bought tháng trước, BSR (tối đa 3 dòng), keyword đoán từ tên sản phẩm
  (bỏ thương hiệu) điền sẵn vào ô gợi ý.
- **Long-tail keyword ideas (A–Z):** bấm Find → gộp gợi ý của 27 tiền tố, bỏ trùng; bấm chip mở trang tìm kiếm keyword đó;
  Copy · tải CSV.
- **Could this be an app instead?** bấm Check → số app App Store cho keyword đó + median rating + 3 app đầu.
- **Popup:** gõ keyword + chọn chợ → keyword a–z, Copy · CSV · mở trên Amazon, Check App Store. Đang mở trang Amazon thì
  điền sẵn chợ + keyword.
- **Quyền:** `storage`, `activeTab`, content script trên 10 trang chợ Amazon, gọi mạng tới 4 máy chủ autocomplete + iTunes.
- **Ngưỡng là quy ước** trong `lib/serp.js` (100 rating = người mới, 1.000 = đứng vững, median 5.000 = đông), không phải số đo.

Chạy thử 2026-11-02 trên amazon.com thật (keyword "yoga mat"): Crowded — top 10 ô thường đều 1K+ rating, median 10.8K,
12 Sponsored; A–Z ra 250 keyword; App Store 9 app, median 4.6K rating. Cách thử: gói `sw.js` + `content.js` thành 1 file
rồi chạy trong trang (browser pane không cài được extension unpacked) → **cần thử lại bằng Load unpacked trên Chrome thật**.

## Còn lại trước khi tải lên store

1. Load unpacked trên Chrome thật, thử trang tìm kiếm + sản phẩm + popup ở US và 1 chợ khác tiếng (DE hoặc JP).
2. Ảnh store 1280×800 + promo 440×280: Claude viết prompt, Codex sinh (như ShotMatic Lite).
3. Người dùng tự tải lên Developer Dashboard + bấm Submit (dùng chung tài khoản developer với Lite).
4. Trang shotmatic.app cho người đến từ Amazon: hiện trang đích là trang app niche, nên đo xem họ có ở lại không trước khi làm trang riêng.

## Đo gì

- Lượt cài, lượt bấm về shotmatic.app (`utm_campaign=shotmatic_scout`, `utm_content` = chỗ bấm: `card_app_report`,
  `card_footer`, `popup_app_report`, `popup_footer`), lượt tải bản đầy đủ đến từ UTM này.
- Chưa có số mốc: `chưa đo`.

## Rủi ro

- Amazon đổi giao diện trang → sửa chỗ đọc trong `content.js`; phần đọc số nằm ở `lib/parse.js` có test.
- Amazon đóng API autocomplete hoặc đòi cookie → phần A–Z hỏng; card trên trang vẫn chạy.
- Chữ "bought in past month" ở chợ khác tiếng: đã bắt `gekauft`, `achet`, `acquistat`, `comprad`, `購入` nhưng chưa thử trang thật.
- Tên có chữ "Amazon": dùng dạng "for Amazon" như các extension khác; store có thể đòi sửa khi duyệt.
