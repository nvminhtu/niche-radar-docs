# Layout — 8 kiểu bố cục landing app Mac

Layout = **thứ tự và hình khối** của trang (cái gì ở hero, tính năng xếp ra sao). Không phải màu — màu ở `themes.md`.
Một trang = 1 layout + 1 theme. `make_site.py` dựng được 6/8 kiểu (cột Variant). Kiểu `menubar` dựng bằng `window`;
kiểu `docs` không dùng để bán app trả phí.

Ví dụ app ở mỗi kiểu là **gợi ý chưa soi** (xem trạng thái trong `atlas.md`) — trừ Things/CapWords/Flighty/Opal/
Gentler Streak đã soi 2026-10-01 trong `app-marketing/references/landing-page.md`. Soi rồi thì sửa ví dụ cho đúng.

## Bảng chọn nhanh

| Layout | `Variant:` | Hero là gì | Hợp app Mac kiểu | Gợi ý trang để soi |
|---|---|---|---|---|
| `icon` | `classic` | icon app to + tên + 1 đoạn + link video | công cụ năng suất trả một lần, app có icon đẹp | Things (ADA 2017), One Thing, Lungo |
| `window` | `window` | **cửa sổ app thật** đặt trên nền "desktop" màu nhấn | utility, dọn file, ảnh, công cụ dev, database, mail | CleanShot X, DaisyDisk, Proxyman, TablePlus |
| `menubar` | `window` (Hero media = ảnh thanh menu + menu thả) | dải menu bar macOS + popover của app | app sống trên thanh menu | iStat Menus, Bartender, Itsycal |
| `spotlight` | `spotlight` | **phím tắt** dạng keycap + cửa sổ phát sáng trên nền gần đen | launcher, bàn phím, terminal, công cụ dân dev | Raycast, Warp, Alfred |
| `editorial` | `editorial` | **chữ** là hero: serif to căn trái, ảnh như trang sách | viết, ghi chú, đọc, Markdown | iA Writer (ADA 2025 finalist), Ulysses, Bear (ADA 2017) |
| `bento` | `bento` | lưới thẻ nhiều cỡ, mỗi thẻ 1 lý do | app nhiều tính năng nhỏ, tài chính, dữ liệu | Craft (ADA 2021 finalist), Copilot Money (ADA 2024 finalist) |
| `playful` | `sticker` / `cards` | mascot / màu kẹo / thứ app tạo ra | app vui, GIF, màu, camera — app có "nhân vật" (vd mascot của Sweepy) | Gifox, Pika, Hand Mirror, Tot |
| `docs` | — | README dạng web: tiêu đề, lệnh cài, link docs | mã nguồn mở, miễn phí | Alacritty, Kitty, MacVim, Skim |

Chọn theo **người mua làm gì trong 3 giây đầu**: muốn thấy app trông thế nào → `window`; muốn biết bấm phím gì →
`spotlight`; muốn cảm được chữ/sự yên tĩnh → `editorial`; muốn biết app có nhiều thứ → `bento`; muốn thấy
"nó dễ thương" → `playful`; app quá đơn giản để cần ảnh (1 nút, 1 việc) → `icon`.

## Mạch từng kiểu (thứ tự mục từ trên xuống)

### `window` — kiểu phổ biến nhất của app Mac bán trực tiếp

1. Nav viên thuốc: tên · Our Story · Press · Support · nút tải.
2. Headline lời hứa (≤ 60) + subhead (≤ 140) · (tuỳ) phím tắt · nút **Mac App Store** hoặc "Download free trial".
3. Dòng nhỏ dưới nút: `Requires macOS 14 or later · Free 14-day trial` — người mua Mac hỏi 2 câu này trước tiên.
4. **Cửa sổ app thật** 16:10 (screenshot `run_app.py shot --platform macos`) nằm trên nền gradient màu nhấn —
   trông như đang đặt trên desktop. Không khung MacBook giả, không giao diện vẽ tay.
5. 2–4 tính năng so le: chữ 5 phần · ảnh cửa sổ 7 phần (ảnh ngang, bo 10px, viền mảnh).
6. Privacy (app Mac đụng file → bắt buộc nói rõ dữ liệu ở đâu) · Platforms/giá · FAQ · CTA cuối lặp headline.

### `spotlight` — dân bàn phím

1. Keycap phím tắt **trước** headline (`Shortcut: ⌥ Space`) — phím chính là sản phẩm.
2. Headline trắng, cụm nhấn chuyển màu trắng → màu nhấn. Nút trắng trên nền đen.
3. Cửa sổ app có vầng sáng màu nhấn phía sau, viền trắng mờ.
4. Tính năng = lưới 2 cột thẻ viền mảnh (số lẻ → thẻ đầu rộng 2 ô).
5. Nền tối dễ "nhìn đắt" nhưng chữ xám phải còn đủ tương phản (giữ `mut` ≥ #9a9aa6 trên #08080b).

### `editorial` — chữ là sản phẩm

1. Tên app nhỏ dạng mono → headline serif rất to căn trái → 1 đoạn → nút.
2. Một đường kẻ đen ngang → ảnh cửa sổ phẳng, không bóng (như hình trong sách).
3. Tính năng: hàng 1/3 chữ · 2/3 ảnh, mỗi hàng cách bằng đường kẻ mảnh, không thẻ, không bo góc lớn.
4. Review = trích dẫn nghiêng có gạch dọc bên trái (chỉ review thật).

### `icon` (variant `classic`) · `bento` · `playful` (`sticker`/`cards`)

Đã mô tả trong `app-marketing/references/landing-page.md`. Khác biệt khi là app Mac: ảnh tính năng là cửa sổ ngang,
nên với `bento` dùng ảnh **cắt vùng** (một panel, một popover) thay vì cả cửa sổ cho vừa thẻ.

### `menubar`

Dựng bằng variant `window`, nhưng `Hero media:` là ảnh chụp **dải thanh menu + menu thả của app** (chụp màn hình thật,
cắt phần trên màn), không phải cả cửa sổ. Tính năng: mỗi khối là một trạng thái của menu.

### `docs`

Không dựng. Ghi nhận để biết: trang dạng README hợp với app miễn phí mã nguồn mở; app bán tiền dùng trang như vậy
sẽ trông như "dự án phụ" — người mua không yên tâm trả tiền.

## Những thứ app Mac luôn cần, mọi layout

- Ảnh là **cửa sổ thật, 16:10**, chụp ở cả chế độ sáng; trang tối thì dùng ảnh app ở chế độ tối nếu app có.
- `Requires:` (macOS tối thiểu = `min_macos` trong app.json) và, nếu bán ngoài store, cách tải: `.dmg` notarized,
  `brew install --cask <tên>` khi đã có cask (xem `app-macos-listing`).
- Dùng thử: chỉ ghi `Trial:` khi `money.md` có dùng thử thật.
- Nút **Mac App Store** chỉ khi `distribution: mas` và app đã live; còn lại là nút tải trực tiếp / form email.
