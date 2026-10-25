# Niche Radar Phase 53b — Test chức năng thật + chụp màn kết quả — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` xanh rồi commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** gõ keyword **thật**, đợi tool chạy xong, chụp lại màn kết quả để anh mở xem ngay.

**Spec:** [Phase 53b · Test chức năng thật](../../web/phase-53b-functest-screenshots.md) · **Cần trước:** Phase 51 (Playwright config, selector theo role),
Phase 53 (bộ niche chuẩn).

## Mục tiêu · làm · không làm

- **Xong khi:** 1 lệnh ra đủ thư mục ảnh + `report.md` · tắt 1 nguồn → `report.md` ghi rõ nguồn đó rỗng, ảnh vẫn chụp phần còn lại.
- **Làm:** `npm run functest -- "<keyword>"`, search thật, chụp cả trang 1340 + 375, `report.md`, kiểm tối thiểu.
- **Không làm:** chạy hằng ngày (canary) · đưa vào `npm test` · CI.

## Global Constraints

- Chạy trên bản Web thật (`npm run dev` hoặc build), mạng thật, DB **tạm** (không ghi DB anh đang dùng).
- Giới hạn thời gian mỗi bước (Research 10 phút, Explore 15 phút); quá → ghi "quá giờ", chụp trạng thái hiện tại, đi tiếp.
- Kiểm tối thiểu: bảng keyword ≥ 1 dòng · không ô "lỗi" / trang trắng · console không lỗi đỏ. Không so ảnh chuẩn.
- Lưu `run/functest/<ngày>-<keyword>/` (gitignore), `report.md` có thời gian từng bước + nguồn rỗng + link ảnh.
- Tắt nguồn để thử: biến `NR_DISABLE_SOURCES=trends` (đọc ở `run-research.ts`).

## File đụng tới

| File | Việc |
|---|---|
| `web/tests/functest/run.spec.ts` (mới) + `web/scripts/functest.ts` | nhận keyword, chạy Playwright, viết `report.md` |
| `web/src/lib/run-research.ts` | `NR_DISABLE_SOURCES` |
| `web/package.json` | `functest` |
| `.gitignore` | `run/functest/` |
| `docs/cach-dung.md`, `CHANGELOG.md` | lệnh mới |

## Tasks

### Task 1: Lệnh + search thật
- [ ] Playwright mở Web, gõ keyword, đợi run xong (theo `ProgressPanel`), giới hạn giờ.

### Task 2: Chụp + report
- [ ] Chụp tóm tắt run, bảng keyword, đối thủ, chủ đề than, so sánh niche ở 1340 + 375; `report.md`.

### Task 3: Thử nguồn rỗng
- [ ] `NR_DISABLE_SOURCES=trends` → report ghi Trends rỗng, ảnh vẫn đủ phần khác. Mở ảnh xem (Read).
- [ ] Cách dùng, CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
