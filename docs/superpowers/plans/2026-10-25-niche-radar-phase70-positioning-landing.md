# Niche Radar Phase 70 — Định vị + landing + email — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự. Steps dùng checkbox (`- [ ]`). Landing ở repo oneclicktool.app (tiếng Anh 100%),
> media host ở repo `app-demo` (không để trong `public/`). Anh mở tài khoản email; Claude không đăng bài.

**Goal:** một câu định vị có bằng chứng, rồi dựng **chỗ của mình**: landing riêng + form email + đo lượt bấm.

**Spec:** [Phase 70 · Định vị + landing + email](../../web/phase-70-positioning-landing.md) · **Cần trước:** Version 10 (giá), Phase 31a (demo site để link "Try the demo"),
Phase 10 / 12 (dữ liệu nỗi đau).

## Mục tiêu · làm · không làm

- **Xong khi:** 5 dòng định vị có bằng chứng, anh duyệt · landing live, `check_landing.py` qua, đã xem 1280 + 375 · 1 email test vào đúng danh sách ·
  bấm tải / mua / gửi email → GA4 thấy `download`, `checkout_click`, `generate_lead`.
- **Làm:** định vị qua `/app-gtm` (Pha 0 + Pha 1), 3 nỗi đau có link, landing `/oneclicktool-landing`, form email, sự kiện GA4 + UTM.
- **Không làm:** đăng bài · bịa số / lời khen · đổi giá · quảng cáo trả tiền.

## Global Constraints

- File GTM: `marketing/gtm.md` của Niche Radar (tạo bằng `/app-gtm`, khung + checker `check_gtm.py` của App-AI-Skills).
- 3 nỗi đau lấy bằng chính tool: Reddit Gap (Phase 10) / lời chê (Phase 12) về "app idea", "niche research" — mỗi nỗi đau 1 link nguồn.
- Landing: skill `/oneclicktool-landing` (layout riêng, đủ khối bán hàng), đường dẫn `oneclicktool.app/niche-radar`; video demo quay từ app thật
  (`/app-video`), host ở `app-demo`. Giá lấy đúng `money.md`.
- Form email: Mailchimp `PRODUCT=niche-radar` (như demo site) — anh tạo audience / tag.
- UTM chuẩn `?utm_source=<kênh>&utm_campaign=niche-radar`; sự kiện GA4 theo khuôn landing có sẵn (`store_click` → đổi tên theo spec: `download`, `checkout_click`, `generate_lead`).

## File đụng tới

| File | Việc |
|---|---|
| `marketing/gtm.md` (mới, qua `/app-gtm`) | Pha 0 + Pha 1: định vị 5 dòng + bằng chứng |
| repo oneclicktool.app: trang `niche-radar` + dữ liệu sản phẩm | landing |
| repo `app-demo`: `niche-radar/` | video demo + ảnh |
| `docs/web/phase-70-positioning-landing.md` | link landing, kết quả kiểm |

## Tasks

### Task 1: Định vị
- [ ] `/app-gtm` Pha 0 + Pha 1 → 5 dòng, mỗi dòng có link bằng chứng. Anh duyệt (chặn: chưa duyệt không dựng landing).

### Task 2: 3 nỗi đau
- [ ] Chạy tool với niche "app idea / niche research" → 3 nỗi đau + link.

### Task 3: Video + landing
- [ ] Quay app thật → video demo + shorts (`/app-video`), đẩy `app-demo`. `/oneclicktool-landing` dựng trang, `check_landing.py` 0 lỗi.

### Task 4: Email + GA4
- [ ] Anh tạo audience; nối form; gửi email test. Bấm 3 nút → GA4 Realtime thấy 3 sự kiện.

### Task 5: Soát
- [ ] Xem 1280 + 375, Read screenshot. Deploy (theo quy trình repo oneclicktool.app). Chip, ROADMAP, CHANGELOG (Docs).

## Tiến độ

- 2026-10-25: viết plan.
