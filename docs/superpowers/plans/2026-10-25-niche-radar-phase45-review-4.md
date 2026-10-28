# ShotMatic Phase 63 — Review Version 4 — Implementation Plan

> **For agentic workers:** phase **chỉ soát + sửa** Phase 59–44. Mỗi lỗi sửa xong `npm run check` xanh rồi commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** dùng Version 4 **chọn niche thật 3 lần** có kệ Google + kệ AI ở bản Web, sửa lỗi.

**Spec:** [Phase 63 · Review Version 4](../../web/phase-63-review-4.md) · **Cần trước:** Phase 59–44.

## Mục tiêu · làm · không làm

- **Xong khi:** 3 lần chọn thật xong, mỗi lần có gói GEO đã chạy `geo.py` làm mốc, chi phí dưới trần · tra kệ Google + kệ AI cho 1 niche
  chạy được trên bản Web, test xanh.
- **Làm:** 3 lần: so 3 niche có 2 cột kệ → chọn 1 → xuất gói GEO → `geo.py` làm mốc; ghi chi phí AI mỗi lần; sửa lỗi.
- **Không làm:** tính năng mới.

## Global Constraints

- Chi phí lấy từ sổ chi phí Phase 27.6 (không ước tay). Quota SERP từ `serp_calls`.
- Mốc `geo.py` lưu ở thư mục `research/` của repo pipeline do anh chọn — tool không tự ghi vào repo đó.
- Lỗi lớn → Master Plan §4 pending.

## File đụng tới

- `docs/web/phase-63-review-4.md` — bảng 3 lần: thời gian, chi phí AI, quota SERP, gói GEO, vướng
- code Phase 59–62 — sửa lỗi kèm test
- `CHANGELOG.md` — bản Web mới

## Tasks

### Task 1: Lần 1
- [ ] Chạy hết luồng, ghi thời gian + chi phí, sửa lỗi chặn.

### Task 2: Lần 2 + 3
- [ ] Như lần 1, sau khi sửa.

### Task 3: Khoá lại
- [ ] Test tích hợp: kệ Google + kệ AI cho 1 niche fixture (provider / engine giả). Bản Web mới, CHANGELOG, chip 41–45, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
