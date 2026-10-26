# Niche Radar Phase 21 — Collect niche vào Project — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** thấy gì đáng giữ ở **bất cứ chỗ nào** — bấm 1 lần là vào project, kèm số liệu lúc đó và nguồn.

**Spec:** [Phase 21 · Collect niche vào Project](../../web/phase-21-collect.md) · **Cần trước:** Phase 8 (`projects.ts`,
`portable.ts`, `CollectButton.tsx`), Phase 18 (lời chê để gom).

## Mục tiêu · làm · không làm

- **Xong khi:** gom được từ đủ 6 chỗ, mỗi loại đúng cột trong project · gom 20 keyword 1 lần < 2 giây, gom lại → 0 dòng
  trùng · xuất / nhập project đủ item + số chụp (test round-trip) · test xanh · screenshot popover + project đã Read.
- **Làm:** 5 loại item, Collect ở 6 chỗ, gom hàng loạt, popover nhớ project gần nhất + tìm + tạo mới, chụp số lúc gom,
  ghi chú 1 dòng, chống trùng, hoàn tác.
- **Không làm:** sắp / lọc / gộp project (Phase 22) · đồng bộ lên mạng (Backlog 04).

## Global Constraints

- `project_items` hiện chỉ có `term/country/runId/explorationId`. Thêm cột: `uid` (ULID), `kind`
  (`keyword | niche | competitor | complaint | gap`), `ref` (khoá trong loại: appId+store, khoá cụm, rowKey…), `snapshot`
  (json số lúc gom), `note`, `sourceUrl`. Item cũ → `kind = 'keyword'`, `uid` sinh lúc migrate.
- Khoá chống trùng đổi từ `(projectId, term, country)` sang `(projectId, kind, ref, country)`; với keyword `ref = term`.
- Số chụp lúc gom **không** bị ghi đè khi gom lại; gom lại chỉ cập nhật `lastSeen` + `latest` (json) riêng.
- Gói `.niche.json` (`BUNDLE_FORMAT`) tăng phiên bản, nhập được cả gói cũ; nhập máy khác không nhân đôi nhờ `uid`.
- **Một migration chung Phase 21 + 22** (số kế tiếp, `backupDb` trước; đếm dòng trước / sau `countRows`). Ngoài cột Phase 21
  ở trên, thêm luôn phần Phase 22: `projects.tags` (json), `archivedAt`, `nextStep`, `nextDue` · `project_items.status`
  (`giữ | ứng viên | loại`, mặc định `giữ`), `reason`, `rank` · bảng `project_log` (projectId, at, kind, detail json).
  Phase 21 chỉ ghi / đọc phần của mình; phần Phase 22 để mặc định, chưa có UI. `BUNDLE_FORMAT` tăng **một lần** cho cả hai.

## File đụng tới

- `web/src/db/schema.ts` + migration mới (chung 14 + 15) — cột mới `project_items` + `projects`, index mới, bảng `project_log`
- `web/src/lib/projects.ts` — `addItems(db, projectId, items[])` hàng loạt trong 1 transaction, trả `{ added, updated }`; `undoAdd(ids)`
- `web/src/lib/collect-snapshot.ts` (mới) — dựng `snapshot` theo loại từ `RunView` / explore view
- `web/src/lib/projects-client.ts` — `CollectTarget` có `kind/ref/snapshot/note`; nhớ project gần nhất (localStorage, try/catch)
- `web/src/components/CollectButton.tsx` — ô tìm project, tạo mới, ghi chú, chế độ hàng loạt
- `KeywordTable`, `ExploreDashboard`, `NicheMap`, `CompetitorBlock`, `ComplaintsBlock`, `GapMatrixBlock` — gắn nút + ô tick
- `web/src/client/ProjectPage.tsx` — cột theo loại
- `web/src/lib/portable.ts` — xuất / nhập trường mới, đọc gói cũ
- `web/tests/projects*.test.ts`, `portable*.test.ts`

## Tasks

### Task 1: Schema chung 14 + 15 + migrate dữ liệu thật
- [ ] Cột mới + index mới (Phase 21) **và** cột / bảng Phase 22 (xem Global Constraints) trong cùng 1 file migration;
      chuyển item cũ (`kind = 'keyword'`, `ref = term`, sinh `uid`, `status = 'giữ'`).
- [ ] `portable.ts`: xuất / nhập mọi cột mới (cả phần Phase 22, để trống cũng round-trip), đọc được gói cũ.
- [ ] Test migrate trên bản sao DB có item cũ: 0 dòng mất; round-trip `.niche.json` giữ đủ trường 14 + 15.

### Task 2: API hàng loạt + chống trùng + hoàn tác
- [ ] `POST /api/projects/:id/items` nhận 1 hoặc mảng item; trùng → cập nhật `latest`, trả "đã có".
- [ ] `POST /api/projects/:id/items/undo` nhận danh sách id vừa thêm.
- [ ] Test: 20 item < 2 giây (đo trong test), gom lại 0 dòng mới, undo xoá đúng.

### Task 3: Chụp số
- [ ] `collect-snapshot.ts`: keyword / niche (điểm cơ hội, số đối thủ, trends) · đối thủ (rating, số rating, giá, mô hình tiền) ·
      lời chê (cụm, số review, 3 câu trích) · khoảng trống (hàng, số app có, ô `?`) — kèm `runId`/`explorationId` + ngày.
- [ ] Test mỗi loại.

### Task 4: Popover + Collect ở 6 chỗ (+ phím `C`)
- [ ] Popover: project gần nhất lên đầu, gõ tìm, tạo mới, ghi chú 1 dòng.
- [ ] Gắn vào cây keyword, Top cơ hội, bản đồ ngách, bảng đối thủ, khối Đối thủ bị chê gì, ô Feature Gap "không ai có".
- [ ] Ô tick nhiều dòng + nút "Collect N"; thanh báo "Đã thêm N vào Project X · Hoàn tác".
- [ ] Phím `C` khi đang chọn dòng mở popover (bỏ qua khi đang gõ trong ô nhập).

### Task 5: Trang project + xuất / nhập
- [ ] `ProjectPage`: nhóm item theo loại, cột riêng (icon, số chụp, ngày, ghi chú, link nguồn).
- [ ] `portable.ts`: trường mới; nhập gói cũ; test round-trip đủ item + snapshot.

### Task 6: Soát
- [ ] Gom thật từ đủ 6 chỗ; screenshot popover + project 1340 + 375, Read. `features.ts`, chip phase, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
- 2026-10-26: review plan — gộp migration với Phase 22 (DB thật chỉ nâng 1 lần, `BUNDLE_FORMAT` tăng 1 lần); thêm phím `C`.
