# Niche Radar Phase 22 — Quản lý Project — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** chục project, hàng trăm item vẫn **tìm, lọc, xếp ưu tiên, dọn** được; mỗi project trả lời "đang ở bước nào, bước tiếp là gì".

**Spec:** [Phase 22 · Quản lý Project](../../web/phase-22-project-manage.md) · **Cần trước:** Phase 21 (item có `kind` +
**schema chung 14 + 15 đã migrate** — phase này không có migration).

## Mục tiêu · làm · không làm

- **Xong khi:** không thêm migration (dùng schema chung Phase 21) · tìm 1 keyword ra đúng project · lọc thẻ + trạng thái
  cùng lúc đúng · gộp 2 project có item trùng không nhân đôi, nhật ký ghi lại · trang project đọc được 1340 + 375, screenshot đã Read.
- **Làm:** tìm / lọc / sắp danh sách, thẻ, lưu trữ / nhân bản / gộp, tab trong project, ưu tiên + trạng thái item (loại phải
  có lý do), bước tiếp + ngày hẹn, nhật ký tự động, so 2 project nhanh, nút ra pipeline.
- **Không làm:** chia sẻ / nhiều người sửa · kanban kéo giữa cột (ghi Appendix nếu thấy cần).

## Global Constraints

- Không xoá cứng từ danh sách: **lưu trữ** trước; xoá hẳn phải xác nhận + `backupDb` ngay trước đó.
- **Không migration**: mọi cột / bảng (`tags`, `archivedAt`, `nextStep`, `nextDue`, `status`, `reason`, `rank`,
  `project_log`) đã có từ migration chung Phase 21, `portable.ts` đã round-trip. Thấy thiếu cột → sửa migration chung nếu
  Phase 21 chưa vào `main`, đã vào rồi thì mới thêm migration nhỏ (ghi lý do ở Tiến độ).
- Item "loại" bắt buộc `reason` (API trả 400 nếu thiếu).
- Nhật ký ghi **tự động** ở tầng `lib/projects.ts` (không để UI tự ghi), loại sự kiện cố định.

## File đụng tới

- `web/src/lib/projects.ts` — `searchProjects`, `archive/unarchive`, `duplicate`, `merge(a, b)`, `setItemStatus`, `reorder`, `log()`
- `web/src/server/app.ts` — `GET /projects?q=&tag=&status=&sort=&archived=` · `POST /projects/:id/archive` · `/duplicate` · `/merge` · `/items/:itemId/status` · `/items/reorder` · `GET /projects/:id/log`
- `web/src/client/ProjectsPage.tsx` — ô tìm, lọc thẻ + trạng thái, sắp, "đến hạn trước", đã lưu trữ
- `web/src/client/ProjectPage.tsx` — 7 tab (Tổng quan · Keyword · Đối thủ · Lời chê · Khoảng trống · Theo dõi · Ghi chú), bước tiếp, nhật ký, nút pipeline
- `web/src/lib/project-compare.ts` (mới) — so 2 project: điểm v2, số đối thủ, lời chê nặng nhất, ai thu tiền, xu hướng
- `web/tests/projects-manage.test.ts`

## Tasks

### Task 1: Kiểm schema có sẵn
- [ ] Xác nhận cột / bảng Phase 22 đã có từ migration chung Phase 21; test round-trip `.niche.json` có thẻ, lý do, bước tiếp, nhật ký.

### Task 2: Tìm, lọc, sắp, thẻ
- [ ] `searchProjects`: tên + term item bên trong, lọc `tag` + `status`, sắp `updatedAt | bestScore | itemCount`, ẩn lưu trữ mặc định.
- [ ] UI danh sách + chip thẻ bấm để lọc. Test tìm keyword ra đúng project; lọc 2 điều kiện.

### Task 3: Lưu trữ / nhân bản / gộp
- [ ] `archive`, `duplicate` (uid mới cho item), `merge` (item trùng theo khoá `(kind, ref, country)` gộp 1, giữ snapshot cũ nhất, ghi nhật ký).
- [ ] Xoá hẳn: xác nhận + backup tự động. Test merge không nhân đôi.

### Task 4: Tab + ưu tiên item + bước tiếp
- [ ] `ProjectPage` chia 7 tab, mỗi tab bảng sắp được; trạng thái item giữ / ứng viên / loại (loại → ô lý do bắt buộc).
- [ ] Sắp theo điểm hoặc kéo thả (`rank`); bước tiếp + ngày hẹn; danh sách hiện project đến hạn lên đầu.

### Task 5: Nhật ký + pipeline + xuất / nhập
- [ ] `log()` gọi ở thêm / loại item, đổi trạng thái, đổi kết luận, chụp số; tab nhật ký.
- [ ] Nút "Làm evidence pack" (Phase 43) và "Mở /app-demand" (copy lệnh + đường dẫn file) cho project ứng viên.
- [ ] So 2 project nhanh (`project-compare.ts` + bảng 1 cột ở 375px). Test số khớp trang từng project.

### Task 6: Soát
- [ ] Chạy trên DB thật (đã ở schema chung từ Phase 21). Screenshot 1340 + 375, Read. Chip phase, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
- 2026-10-26: review plan — migration dời sang Phase 21 (chung 1 lần); thêm so 2 project nhanh.
