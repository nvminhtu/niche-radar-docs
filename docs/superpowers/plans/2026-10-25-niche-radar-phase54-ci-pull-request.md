# Niche Radar Phase 54 — CI cho pull request — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự trên nhánh riêng, mở PR thử. Steps dùng checkbox (`- [ ]`).
> Bật luật bảo vệ nhánh trên GitHub là việc của anh (quyền admin repo) — Claude ghi bước, không tự đổi cài đặt repo khi chưa được đồng ý.

**Goal:** mỗi PR, GitHub tự chạy hết các bước kiểm; đỏ là không gộp được.

**Spec:** [Phase 54 · CI cho pull request](../../web/phase-54-ci-pull-request.md) · **Cần trước:** Phase 50 (test không mạng), Phase 51 (E2E fixture).

## Mục tiêu · làm · không làm

- **Xong khi:** PR cố tình đỏ 1 test → CI đỏ, nút merge khoá · PR đỏ 1 test giao diện → CI có ảnh lỗi mở được · PR xanh ≤ 10 phút ·
  CI không gọi nguồn thật nào.
- **Làm:** `.github/workflows/ci.yml` (lint · typecheck · test · Playwright fixture · `docs:build --strict`), cache, ảnh lỗi, luật chặn merge.
- **Không làm:** canary trên CI · tự merge · Windows / Linux build.

## Global Constraints

- Chỉ dùng lệnh có sẵn: `npm run lint`, `typecheck`, `npm test` (qua `npm --prefix web`), `npm run e2e`, `npm run docs:build`.
- Runner `ubuntu-latest` cho web + docs (better-sqlite3 build được trên Linux); Node theo `.nvmrc` / `engines`.
- Cache `actions/setup-node` (npm) + `actions/cache` cho trình duyệt Playwright; Python + `pip install -r requirements-docs.txt` có cache.
- Chặn mạng ngoài trong test đã có từ Phase 50; thêm bước kiểm `NR_E2E=1` cho E2E.
- E2E đỏ → `actions/upload-artifact` thư mục `test-results/` + `playwright-report/`.
- Luật nhánh: `main` cần check `ci` xanh — anh bật ở Settings → Branches (hoặc `gh api` khi anh đồng ý).

## File đụng tới

| File | Việc |
|---|---|
| `.github/workflows/ci.yml` (mới) | 2 job: `web` (lint, typecheck, test, e2e) · `docs` (build strict) |
| `.nvmrc` (mới nếu chưa có) | phiên bản Node |
| `docs/quy-trinh-build.md` | mục CI |
| `CHANGELOG.md` (Repo) | |

## Tasks

### Task 1: Workflow
- [ ] `ci.yml` trên nhánh `phase54-ci`; mở PR → xanh, đo thời gian.

### Task 2: Ảnh lỗi
- [ ] PR thử làm đỏ 1 spec E2E → artifact có ảnh; đóng PR thử.

### Task 3: Chặn merge
- [ ] Anh bật luật; PR thử làm đỏ 1 unit test → merge bị khoá. Ghi bằng chứng (link PR) vào trang phase.

### Task 4: Ghi lại
- [ ] Quy trình build mục CI, CHANGELOG, chip, ROADMAP. Thời gian PR xanh ≤ 10 phút (ghi số).

## Tiến độ

- 2026-10-25: viết plan.
