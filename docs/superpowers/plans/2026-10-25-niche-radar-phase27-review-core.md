# Niche Radar Phase 26 — Review cụm tính năng chính (12–26) — Implementation Plan

> **For agentic workers:** phase **chỉ soát + sửa**, không thêm tính năng. Mỗi lỗi sửa xong thì `npm run check` xanh rồi commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** soát Phase 18–27.3 như Phase 7 đã làm cho 1–6: 5 niche thật qua mọi tính năng, đối chiếu từng "Xong khi", sửa lỗi, ra bản Web mới.

**Spec:** [Phase 26 · Review cụm tính năng chính](../../web/phase-26-review-core.md) · **Cần trước:** Phase 18–27.3 code xong.

## Mục tiêu · làm · không làm

- **Xong khi:** phiếu soát đủ 15 phase, phase trượt có lý do + việc còn lại · 5 niche thật chạy hết luồng không lỗi chặn ·
  test xanh, screenshot luồng chính đã Read, bản Web mới có CHANGELOG.
- **Làm:** phiếu soát, 5 niche đi hết luồng, sửa lỗi, cập nhật `features.ts` + Hướng dẫn + Cách dùng, ra bản.
- **Không làm:** tính năng mới.

## Global Constraints

- Phiếu soát nằm ở `docs/web/phase-26-review-core.md` mục "Phiếu soát": mỗi phase 1 mục (1 cột), mỗi dòng "Xong khi" →
  **đạt / trượt** + bằng chứng (số đo + ngày, đường dẫn screenshot trong `design/review-27/`).
- Lỗi nhỏ (< 1 giờ) sửa ngay; lớn → Master Plan §4 "Đang pending", không sửa lén trong phase này.
- 5 niche chọn khác loại: 1 app Mac, 1 iOS tiêu dùng, 1 Android, 1 SaaS, 1 niche đã biết là xấu (để thấy cờ / BỎ).
- Ra bản chỉ qua quy trình release hiện có (tăng version Web, CHANGELOG, `version.ts`, test `version.test.ts`).

## File đụng tới

- `docs/web/phase-26-review-core.md` — phiếu soát + bảng 5 niche
- `design/review-27/*.png` — screenshot bằng chứng
- `web/src/lib/features.ts`, `GuidePage.tsx`, `AboutPage.tsx`, `docs/cach-dung.md` — tính năng chính / phụ, hướng dẫn
- `docs/superpowers/specs/2026-10-24-niche-radar-master-plan.md` §4 — lỗi lớn pending
- `CHANGELOG.md`, `web/package.json`, `web/src/lib/version.ts` — ra bản

## Tasks

### Task 1: Phiếu soát rỗng
- [ ] Chép mọi "Xong khi" của Phase 18–27.3 vào phiếu (15 mục). `npm run docs:build` xanh.

### Task 2: 5 niche đi hết luồng
- [ ] Mỗi niche: Research → Explore → collect → chấm điểm → theo dõi → xuất / gói LLM → evidence pack. Ghi chỗ vướng + thời gian.

### Task 3: Điền phiếu + sửa
- [ ] Mỗi dòng đạt / trượt + bằng chứng. Lỗi nhỏ sửa (test kèm), lỗi lớn ghi pending.

### Task 4: Hướng dẫn + ra bản
- [ ] `features.ts` (status `done` đúng thực tế), Hướng dẫn, Cách dùng, About.
- [ ] Tăng version Web, CHANGELOG, chip 12–27. Screenshot luồng chính 1340 + 375, Read.

## Tiến độ

- 2026-10-25: viết plan.
