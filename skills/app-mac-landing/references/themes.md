# Theme — 7 kiểu màu + chữ của landing app Mac

Theme = **bảng màu + cặp phông**. Đặt bằng dòng `Theme:` trong landing.md (để trống = theme mặc định của variant).
Màu nhấn `Accent:` lấy từ `design.md` của app (màu chính đã qua kiểm tương phản ở bước 4) — **không** lấy màu thương hiệu
của app mẫu. Mọi bảng dưới đây đã đo tương phản WCAG (ngày 2026-10-03, công thức WCAG 2.x):

| Theme | `Theme:` | bg | fg | mut (chữ phụ) | card | Tương phản fg / mut trên bg | Phông |
|---|---|---|---|---|---|---|---|
| Native light | `light` hoặc `mist` | #ffffff / #f2f5f7 | #111114 / #1d1d1f | #5c5c66 / #55595f | #f3f3f6 / #fff | đã có từ trước | chữ hệ thống (SF Pro qua `-apple-system`) |
| Wallpaper | `light` + variant `window` | #ffffff | #111114 | #5c5c66 | — | như trên | hệ thống; nền "desktop" gradient từ `Accent` |
| Midnight | `midnight` | #08080b | #f2f2f5 | #9a9aa6 | #111117 | 17.9 / 7.2 | Inter |
| Graphite (pro, ảnh/video) | `graphite` | #1c1c1e | #f5f5f7 | #a1a1a8 | #2a2a2d | 15.6 / 6.6 | hệ thống hoặc Inter |
| Paper | `paper` | #fbfaf6 | #1b1b1a | #62605a | #ffffff | 16.5 / 6.0 | Newsreader (serif) + Inter + IBM Plex Mono |
| Candy (indie vui) | `candy` | #fff8f1 | #2a1c12 | #6f5c4f | #ffffff | 15.7 / 6.0 | theo variant (`sticker`: Merriweather + Inter) |
| Utility (docs) | — | trắng | đen | xám | — | — | không dựng — xem layout `docs` |

Theme cũ của 5 variant gốc vẫn dùng được: `dark` (#2e2e2e ấm, CapWords) · `black` (#040404, Opal).

## Ghép layout × theme (khuyên dùng)

| Layout ↓ / Theme → | light/mist | midnight | graphite | paper | candy |
|---|---|---|---|---|---|
| `window` | **mặc định** — utility, dev tool | công cụ dev "pro" | **ảnh, video, âm thanh** | — | app có mascot |
| `spotlight` | — | **mặc định** | được | — | — |
| `editorial` | được | — | — | **mặc định** | — |
| `classic` (icon) | **mặc định** (`mist`) | — | — | được | được |
| `bento` | **mặc định** | được | — | — | — |
| `sticker` / `cards` | `cards` | — | — | — | **`sticker` + `candy`** |

Ô `—` = ghép này thường lệch nhau (vd editorial nền đen làm chữ serif khó đọc; spotlight nền sáng mất vầng sáng).

## Luật theme cho app Mac

1. **Một màu nhấn.** Cả trang chỉ một `Accent`, dùng cho cụm nhấn trong headline + eyebrow + nền "desktop".
   Màu thứ hai đến từ chính ảnh chụp app.
2. **Chữ hệ thống khi nghi ngờ.** App Mac native bán cảm giác "thuộc về macOS" → `-apple-system` hợp nhất với
   `window`/`classic`. Chỉ đổi phông khi layout cần giọng riêng (`editorial` serif, `spotlight` Inter).
3. **Trang tối cần ảnh app tối.** Ảnh app chế độ sáng trên nền đen chói mắt; app có dark mode → chụp bản tối
   (`run_app.py shot --platform macos` sau khi đổi giao diện hệ thống sang Dark).
4. **Không giả kính, không giả cửa sổ.** Bóng đổ + viền mảnh là đủ; không vẽ khung MacBook, không blur kính lên ảnh.
5. **Đo lại tương phản** khi đổi `Accent` trên nền tối: cụm nhấn phải đọc được (≥ 3:1 cho chữ ≥ 24px).
