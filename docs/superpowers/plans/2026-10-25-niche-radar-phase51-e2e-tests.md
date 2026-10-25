# Niche Radar Phase 51 — Test giao diện (E2E) — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` + `npm run e2e` xanh rồi commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** máy tự bấm 5 luồng chính như người dùng thật, chụp từng màn so ảnh chuẩn — nút hỏng / màn vỡ thì đỏ trước khi tới tay mình.

**Spec:** [Phase 51 · Test giao diện (E2E)](../../web/phase-51-e2e-tests.md) · **Cần trước:** Phase 50 (fixture, chặn mạng), Phase 46 (Playwright đã cài).

## Mục tiêu · làm · không làm

- **Xong khi:** 5 luồng chạy xanh không mạng · cố tình hỏng 1 nút → đỏ đúng chỗ · bộ ảnh chuẩn 1340 + 375 cho từng màn.
- **Làm:** Playwright 5 luồng (tra niche · Explore · xem đối thủ · so sánh niche · hỏi dữ liệu → xuất), AI giả, chụp + so ảnh, lệnh `npm run e2e`.
- **Không làm:** search thật trên nguồn thật (Phase 53b) · CI (Version 7) · test tải nặng.

## Global Constraints

- Server E2E chạy với `NR_E2E=1`: collector đọc fixture (qua cơ chế `fetcher` của Phase 50), AI = `Ask` giả trả câu ghi sẵn, DB tạm mới mỗi lần.
- Selector theo `role` + tên (`getByRole('button', { name: 'Research' })`) — không selector CSS dễ gãy; thiếu tên thì thêm `aria-label` vào component.
- So ảnh: `expect(page).toHaveScreenshot()` với ngưỡng nhỏ (`maxDiffPixelRatio` 0.01); ẩn phần đổi theo giờ (ngày, ETA) bằng `mask`.
  Ảnh chuẩn lưu `web/tests/e2e/__screenshots__/`; cập nhật chỉ bằng `npm run e2e:update` khi đổi UI có chủ ý.
- `npm run e2e` không nằm trong `check` mặc định (cần trình duyệt); Phase 54 đưa vào CI.

## File đụng tới

| File | Việc |
|---|---|
| `web/playwright.config.ts` (mới / mở rộng từ Phase 46) | 2 viewport 1340 + 375, webServer `NR_E2E=1` |
| `web/src/server/index.ts`, `lib/deps.ts` | chế độ E2E: deps fixture + AI giả |
| `web/tests/e2e/{research,explore,competitor,compare,ask-export}.spec.ts` | 5 luồng |
| `web/package.json` | `e2e`, `e2e:update` |
| component thiếu tên truy cập | thêm `aria-label` |

## Tasks

### Task 1: Chế độ E2E
- [ ] `NR_E2E=1` → deps fixture + AI giả + DB tạm. Test nhỏ: server E2E không gọi mạng.

### Task 2: 5 luồng
- [ ] Mỗi luồng 1 spec, kiểm kết quả hiện đúng (số từ fixture).

### Task 3: Ảnh chuẩn
- [ ] Chụp từng màn 1340 + 375, mask phần đổi theo giờ; Read ảnh chuẩn trước khi chốt.

### Task 4: Chứng minh bắt lỗi
- [ ] Đổi tạm tên 1 nút → spec đỏ đúng chỗ (ghi output vào trang phase) → trả lại.
- [ ] README / Cách dùng (lệnh mới), CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
