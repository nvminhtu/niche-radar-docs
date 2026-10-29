# Phase 28.14 · Mọi trang cùng một bề rộng (full width)

> Làm trước khi build bản app. Đi giữa các trang thấy nội dung lúc rộng lúc hẹp: Niche, Explorer, Projects chạy hết
> khung 1152px (thẳng mép logo và nút "New niche search"), còn AI Agent, Setup, Settings, Guide, License tự bó lại
> 768px hoặc nhỏ hơn rồi canh giữa hoặc canh trái — trông như hai app khác nhau.

<span class="chip chip--done">Xong 2026-10-29</span>

## Mục tiêu · cần làm · KHÔNG làm

- **Mục tiêu:** mọi trang dùng đúng một bề rộng nội dung — bề rộng của khung chung `shell-container` (cùng mép với
  thanh menu), không trang nào tự co lại.
- **Cần làm:** bỏ khung `max-w-*` / `mx-auto` ở cấp trang của 6 chỗ:
  `HuntIndexPage` (AI Agent), `SetupPage`, `SettingsPage`, `GuidePage`, `LicensePage` (2 trạng thái), `FullEditionOnly`.
- **KHÔNG làm:** không đổi bề rộng khung chung 1152px (đổi là đổi cả header + mọi trang, để phase khác nếu cần);
  không đụng hộp thoại, tooltip, đoạn chữ mô tả `max-w-3xl` trong thân trang (giới hạn dòng chữ cho dễ đọc, không phải
  bề rộng trang); không đổi bố cục bên trong từng trang.

## Hiện có — đối chiếu code 2026-10-29

- `web/src/client/globals.css`: `.shell-container { max-width: 1152px; padding-inline: 24px }` — header, `<main>`,
  footer, thanh dùng thử đều dùng.
- 6 chỗ trên bọc nội dung trong `max-w-3xl` (768px), `max-w-2xl` hoặc `max-w-xl`, có chỗ `mx-auto` (canh giữa), có chỗ
  không (canh trái) → 3 kiểu bề rộng khác nhau.

## Xong khi

- [x] 6 chỗ trên không còn `max-w-*` ở thẻ ngoài cùng của trang.
- [x] Mở từng trang ở 1340px: mép trái nội dung thẳng mép logo, mép phải thẳng mép nút "New niche search".
- [x] 960px: cả trang không cuộn ngang.
- [x] `npm run check` xanh.
