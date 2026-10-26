# Niche Radar Phase 28 — Analytics + báo lỗi — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` xanh rồi commit.
> Steps dùng checkbox (`- [ ]`). Không gửi chữ người dùng gõ.

**Goal:** đo người dùng đi tới bước nào trong phễu, biết khi app lỗi trên máy người khác — có hỏi đồng ý.

**Spec:** [Phase 28 · Analytics + báo lỗi](../../web/phase-28-analytics-errors.md) · **Cần trước:** Backlog 03 (Firebase project — nếu chọn ghi lỗi lên Firestore).

## Mục tiêu · làm · không làm

- **Xong khi:** bảng phễu GA4 hiện đủ bước · từ chối đồng ý → 0 request tới GA4 (network log) · payload 7 sự kiện không có keyword / niche / email ·
  gây lỗi thử → lỗi hiện ở chỗ báo lỗi đã chọn.
- **Làm:** 7 sự kiện GA4 + phễu, hỏi đồng ý lần đầu (tắt / bật ở Cài đặt), báo lỗi tự động, một chỗ gửi duy nhất.
- **Không làm:** gửi nội dung gõ / email / tên · quảng cáo / bán dữ liệu · session replay / heatmap · server analytics riêng.

## Global Constraints

- Tên file chốt: `web/src/lib/telemetry.ts` — hàm duy nhất `track(event, counts?)`; kiểu `event` là union 7 tên
  (`app_open · niche_search · explore_done · compare_open · ask_ai · export · geo_pack`); `counts` chỉ nhận **số** (kiểu `Record<string, number>`) —
  TypeScript chặn chuỗi.
- GA4 qua Measurement Protocol từ **server local** hoặc `gtag` ở client — chọn `gtag` (nhẹ, GA4 chuẩn), tải script **chỉ sau** khi đồng ý.
- Đồng ý lưu `settings.telemetry = 'yes'|'no'|null`; `null` → hỏi 1 lần; `no` → không tải script.
- Báo lỗi: chọn lúc làm giữa (a) Sentry gói free (ghi giá + giới hạn, link + ngày) và (b) ghi Firestore `errors/{id}` (đã có Firebase).
  Ghi lựa chọn + lý do vào trang phase. Lỗi gửi qua `redact()` (Backlog 15) + bỏ đường dẫn máy (`scrub()` Phase 23). Cùng cổng đồng ý.
- Demo site (Phase 49) giữ GA riêng của nó, không dùng `telemetry.ts`.

## File đụng tới

- `web/src/lib/telemetry.ts` (mới) — track + đồng ý + tải gtag
- `web/src/lib/errors.ts` — `reportError()` qua cùng cổng
- `web/src/components/ConsentBanner.tsx` (mới), `SettingsPage.tsx` — hỏi đồng ý, tắt / bật
- chỗ gọi 7 sự kiện (HomePage, ExplorePage, ComparePage, AskBox, ExportDialog, geo pack) — `track()`
- `web/tests/telemetry.test.ts` — payload không chuỗi, không gửi khi `no`

## Tasks

### Task 1: Cổng gửi + đồng ý
- [ ] `telemetry.ts` + banner + Cài đặt. Test: `no` → không tạo thẻ script, không gọi mạng.

### Task 2: 7 sự kiện
- [ ] Gắn 7 chỗ; test payload chỉ số.

### Task 3: Báo lỗi
- [ ] Chọn (a) / (b), ghi lý do; `reportError` qua `redact` + `scrub`. Gây lỗi thử → thấy lỗi.

### Task 4: Phễu + soát
- [ ] Anh tạo GA4 property, dán ID; tạo phễu 5 bước trong GA4 (Explore → Funnel). Network log khi từ chối. Privacy (Phase 29) lấy danh sách từ đây.
- [ ] CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
