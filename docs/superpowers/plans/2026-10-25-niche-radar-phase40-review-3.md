# Niche Radar Phase 40 — Review Version 3 — Implementation Plan

> **For agentic workers:** phase **chỉ soát + sửa** Phase 37–39. Mỗi lỗi sửa xong `npm run check` xanh rồi commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** dùng Version 3 **chọn niche thật 3 lần** ở bản Web, sửa lỗi gặp phải.

**Spec:** [Phase 40 · Review Version 3](../../web/phase-40-review-3.md) · **Cần trước:** Phase 37, 38, 39.

## Mục tiêu · làm · không làm

- **Xong khi:** 3 lần chọn thật xong, ≥ 2 lần ≤ 30 phút, mỗi lần có evidence pack · so 3 niche + hỏi 1 câu + xuất 1 báo cáo chạy được, test xanh.
- **Làm:** 3 lần: so 3 niche → so 4 đối thủ → báo cáo → evidence pack, bấm giờ; sửa lỗi.
- **Không làm:** tính năng mới.

## Global Constraints

- Bấm giờ từ lúc mở `/compare` tới lúc tải evidence pack; ghi từng bước tốn bao lâu.
- Lỗi lớn → Master Plan §4 pending, không sửa lén.
- Không ghi tên app chưa ra mắt vào docs (dùng nhãn "lần 1 / 2 / 3").

## File đụng tới

| File | Việc |
|---|---|
| `docs/web/phase-40-review-3.md` | bảng 3 lần: thời gian từng bước, chỗ vướng, evidence pack có / không |
| code Phase 37–39 | sửa lỗi kèm test |
| `CHANGELOG.md` | bản Web mới |

## Tasks

### Task 1: Lần 1
- [ ] Chọn thật, bấm giờ, ghi vướng. Sửa lỗi chặn ngay.

### Task 2: Lần 2 + 3
- [ ] Như lần 1, sau khi sửa. Mục tiêu ≥ 2 lần ≤ 30 phút.

### Task 3: Khoá lại
- [ ] Test luồng so 3 niche + hỏi 1 câu + xuất báo cáo (test tích hợp với Ask giả). Bản Web mới, CHANGELOG, chip 37–40, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
