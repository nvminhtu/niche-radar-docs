# ShotMatic Backlog 16 — Refactor — Implementation Plan

> **For agentic workers:** mỗi bước là **1 PR nhỏ** (1 nguồn / 1 file to), không đổi API, không đổi giao diện. Mỗi PR: `npm run check` + `npm run e2e`
> xanh và `npm run review` giữ nguyên điểm. Steps dùng checkbox (`- [ ]`).

**Goal:** dọn code mà không đổi cách tool chạy: mọi nguồn theo một khuôn, file to tách nhỏ, code chết gỡ đi.

**Spec:** [Backlog 16 · Refactor](../../web/phase-backlog-16-refactor.md) · **Cần trước:** Backlog 08 (test collector), 51 (E2E), 53 (phiếu review).

## Mục tiêu · làm · không làm

- **Xong khi:** test + E2E xanh · phiếu review (Backlog 11) giữ nguyên điểm trước / sau · thêm thử 1 nguồn giả chỉ cần 2 file (collector + test) ·
  không còn file nào > 400 dòng.
- **Làm:** khuôn `Collector`, tách file > 400 dòng, gỡ code chết, gom kiểu chung.
- **Không làm:** đổi framework · viết lại ngôn ngữ khác · tính năng mới · nhiều nguồn trong một PR.

## Global Constraints

- Khuôn `defineCollector({ name, source, limiter, cacheMs, fetch, parse, save })` trong `web/src/collectors/define.ts`; registry tự liệt kê nguồn
  (để "thêm nguồn = 2 file": collector + test, registry đọc qua `import.meta.glob`).
- Tách `server/app.ts` theo nhóm route: `server/routes/{research,explore,projects,settings,data,ai,…}.ts`; `app.ts` chỉ gắn route.
- Code chết: `knip` (hoặc `ts-prune`) liệt kê → xoá từng mục có kiểm tay; export dùng trong test vẫn giữ.
- Kiểu chung: `web/src/types/` (Store, Source, kiểu row view) — chỉ gom kiểu dùng ở ≥ 2 nơi.
- Kiểm "không đổi": `npm run review` trước refactor lưu phiếu mốc; mỗi PR so phiếu, điểm phải bằng.

## File đụng tới

- `web/src/collectors/define.ts` (mới), `registry.ts` (mới) — khuôn + registry
- `web/src/collectors/*.ts` — chuyển từng nguồn sang khuôn (1 PR / nguồn)
- `web/src/server/app.ts` → `server/routes/*.ts` — tách
- file > 400 dòng khác (đo bằng `wc -l` lúc làm) — tách
- `web/src/types/*` — kiểu chung
- `web/tests/collectors/fake-source.test.ts` — chứng minh 2 file

## Tasks

### Task 1: Mốc
- [ ] Phiếu review mốc; danh sách file > 400 dòng; danh sách code chết (`knip`).

### Task 2: Khuôn + nguồn giả
- [ ] `define.ts` + `registry.ts`; thêm nguồn giả bằng đúng 2 file → chạy được trong Research (test).

### Task 3: Chuyển từng nguồn
- [ ] Play · App Store · Trends · TrustMRR · suggest · listing · reviews · YouTube · Amazon · SERP… mỗi nguồn 1 PR, phiếu review bằng điểm.

### Task 4: Tách file to + gỡ code chết + kiểu chung
- [ ] `app.ts` → routes; file > 400 dòng còn lại; gỡ code chết; gom kiểu.

### Task 5: Soát
- [ ] Không file > 400 dòng (lệnh kiểm trong `check`); phiếu review bằng mốc. Xoá nguồn giả. CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
