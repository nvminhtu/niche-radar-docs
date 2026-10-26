# Niche Radar Phase 31a — Demo Site (show hàng) — Implementation Plan

> **For agentic workers:** code đã xong ở bản 0.9.0 (tên cũ Phase 13a). Phần còn lại là **đưa lên + đo**. Claude không đăng
> nhập Cloudflare / Mailchimp / GA, không trả phí — anh làm bước tài khoản, Claude chạy lệnh và kiểm. Steps dùng checkbox (`- [ ]`).

**Goal:** trang **tĩnh** cho khách bấm thử UI thật trên dữ liệu chụp sẵn; muốn xài thật → để email + tải app.

**Spec:** [Phase 31a · Demo Site](../../web/phase-31a-demo-site.md) · **Cần trước:** `.dmg` đã ký + notarize (0.9.0, GitHub Releases).

## Mục tiêu · làm · không làm

- **Xong khi:** `dist-demo/` chạy bằng server tĩnh bất kỳ · 3–5 niche bấm qua Research · Explore · Trends · Feature Gap, không trang
  trắng, console sạch, đã xem 1340 + 375 · nút chỉ có trong app → "Bản demo", không request ra ngoài · trang live trên Cloudflare
  Pages, tải `.dmg` mở được trên Mac khác · 1 email test vào đúng danh sách; GA thấy `demo_view`, `download`, `generate_lead`.
- **Làm:** phần còn lại — deploy, nối email + GA thật, kiểm live.
- **Không làm:** host server thật · tài khoản / thanh toán / trial · dịch UI · landing bán hàng (Phase 70) · đăng bài.

## Global Constraints

- Dữ liệu demo chỉ từ DB thật, ghi ngày chụp; script soát key / đường dẫn máy / ghi chú riêng trước mỗi deploy.
- Một lớp chặn `fetch` (`web/src/demo/demo-fetch.ts`) — không `if (demo)` rải trong component.
- Không route nào gọi ra Play / App Store / Trends từ trang demo.

## File đụng tới

- `web/scripts/export-demo.ts`, `web/public-demo/api/*` — đã có — chụp lại nếu đổi niche mẫu
- `web/src/demo/*` — đã có
- `web/scripts/check-demo.ts` (mới, nếu chưa có) — soát JSON: không `/Users/`, không chuỗi giống key, không `notes`
- `web/.env.demo` (gitignore) — `VITE_GA_ID`, mã form Mailchimp — anh điền
- `docs/web/phase-31a-demo-site.md` — chip, link live, kết quả đo

## Tasks

### Task 1: Code (đã xong 2026-10-25, bản 0.9.0)
- [x] `export-demo.ts` (6 lượt Research + 2 Explore), lớp chặn fetch, thanh demo, hộp "Tải app" + email, GA4 tuỳ chọn, `demo:build`, `demo:deploy`.
- [x] Link `.dmg` 0.9.0.

### Task 2: Soát trước deploy
- [ ] `check-demo.ts` chạy trong `demo:build`; trượt → không build.
- [ ] `demo:preview`: bấm hết trang ở 1340 + 375, console sạch; bấm nút chỉ có trong app → hộp demo, tab Network không có request ra ngoài.

### Task 3: Tài khoản (anh làm)
- [ ] Anh tạo project Cloudflare Pages `niche-radar-demo`, đăng nhập `wrangler` trên máy.
- [ ] Anh mở form Mailchimp (`PRODUCT=niche-radar`) + GA4 property, dán mã vào `.env.demo`.

### Task 4: Deploy + kiểm live
- [ ] `npm run demo:deploy`; mở link live 1340 + 375, Read screenshot.
- [ ] Tải `.dmg` từ link trên trang, mở trên Mac khác (Gatekeeper không chặn).
- [ ] Gửi 1 email test → có trong danh sách; GA Realtime thấy 3 sự kiện.

### Task 5: Ghi lại
- [ ] Chip phase → Xong, link live vào trang phase + ROADMAP, CHANGELOG (Docs). Số đo tuần đầu (view, tải, email) ghi có ngày — chưa có ghi `chưa đo`.

## Tiến độ

- 2026-10-25: code xong ở 0.9.0 (tên cũ Phase 13a). Viết plan phần còn lại.
