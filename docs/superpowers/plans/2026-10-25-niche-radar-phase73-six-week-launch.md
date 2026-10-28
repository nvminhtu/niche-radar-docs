# ShotMatic Phase 49 — Lịch 6 tuần + ra mắt — Implementation Plan

> **For agentic workers:** Steps dùng checkbox (`- [ ]`). Claude soạn nháp + bảng số, **anh đăng**. Luật dừng viết trước tuần 1.
> Không quảng cáo trả tiền trước 10 đơn tự nhiên, không mua review / follow, không gửi email hàng loạt thay anh.

**Goal:** 6 tuần đăng bài thật trên 2 kênh đã chọn, có ngày ra mắt, mỗi tuần nhìn số, luật dừng viết trước.

**Spec:** [Phase 49 · Lịch 6 tuần + ra mắt](../../web/phase-49-six-week-launch.md) · **Cần trước:** Phase 46, 47, 72.

## Mục tiêu · làm · không làm

- **Xong khi:** 6 tuần xong, bảng số đủ 6 dòng · mỗi kênh có quyết định giữ / dừng theo luật dừng · đo lại GEO so mốc Phase 48 ·
  thước đo Version 11: landing có số lượt bấm tải / mua · ≥ 100 email (số thật + ngày; chưa đạt ghi đúng số).
- **Làm:** lịch 4 chặng (warmup · share + ra mắt · discuss + dài hạn · results), file bài từng kênh, ngày ra mắt tuần 3, bảng số tuần, luật dừng, đo lại GEO.
- **Không làm:** quảng cáo trước 10 đơn · mua review / follow · thêm kênh thứ 3 giữa chừng · đổi giá giữa chừng (trừ khi số rõ sai, ghi lý do).

## Global Constraints

- Lịch + file bài qua `/app-gtm`: `marketing/gtm.md` mục lịch, mỗi bài `marketing/<kênh>/NN-*.md` theo khuôn Campaign Promo Desk; `check_gtm.py` 0 FAIL.
- Bảng số tuần (trong `gtm.md`): lượt vào landing (GA4) · email (Mailchimp) · tải (GitHub Releases download count) · dùng thử · đơn (Lemon Squeezy) —
  mỗi ô nguồn + ngày, không có → `chưa đo`. Dùng MCP GA / Search Console đã nối để đọc số.
- Luật dừng viết **trước tuần 1**: ngưỡng mỗi kênh (vd. lượt vào landing / tuần từ kênh đó qua UTM); 3 tuần liền dưới ngưỡng → dừng kênh, dồn sức kênh kia.
- Bài X đã đăng ghi vào `marketing/x-marketing.md` (nháp ở `marketing/x/`) theo luật repo.
- Đo lại GEO cuối tuần 6: `geo.py compare` với mốc Phase 72.

## File đụng tới

- `marketing/gtm.md` — lịch, luật dừng, bảng số tuần, quyết định cuối
- `marketing/<kênh>/NN-*.md` — bài từng tuần
- `marketing/x-marketing.md` — bài X đã đăng
- `marketing/geo-test/<ngày>/` — đo lại GEO
- `docs/web/phase-49-six-week-launch.md` — tóm tắt kết quả (không số nhạy cảm nếu sync public)

## Tasks

### Task 1: Trước tuần 1
- [ ] Luật dừng + ngưỡng; lịch 6 tuần; nháp bài tuần 1–2 (warmup, chưa link). `check_gtm.py` 0 FAIL. Anh duyệt.

### Task 2: Tuần 1–2 warmup
- [ ] Có mặt 2 kênh, giúp người; bảng số tuần.

### Task 3: Tuần 3 ra mắt
- [ ] Chốt ngày; bài "tôi làm cái này vì…" mỗi kênh, cách ≥ 1 ngày, link UTM; Product Hunt / Indie Hackers nếu được chọn (`/app-marketing` nếu cần).

### Task 4: Tuần 4–6
- [ ] Discuss + bài SEO từ khoảng trống GEO; tuần 6 bài kết quả; áp luật dừng; `geo.py compare`.
- [ ] Bảng số đủ 6 dòng, quyết định từng kênh. Chip Version 11, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
