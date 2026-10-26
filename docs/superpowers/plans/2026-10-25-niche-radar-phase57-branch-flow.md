# Niche Radar Phase 57 — Quy trình nhánh — Implementation Plan

> **For agentic workers:** phase về quy trình, ít code. Steps dùng checkbox (`- [ ]`). Claude không tự merge / gắn tag khi anh chưa đồng ý,
> không tự đổi cài đặt bảo vệ nhánh.

**Goal:** khoá `main` (chỉ vào qua PR có CI xanh), mỗi phase một nhánh, xong mới gộp + tag; ghi vào Quy trình build.

**Spec:** [Phase 57 · Quy trình nhánh](../../web/phase-57-branch-flow.md) · **Cần trước:** Phase 54 (CI).

## Mục tiêu · làm · không làm

- **Xong khi:** 1 phase thật đi đủ vòng nhánh → PR → CI → merge → tag → bản mới · đẩy thẳng lên `main` → GitHub từ chối · trang Quy trình build
  có mục nhánh, PR, tag, release và qua `docs:build --strict`.
- **Làm:** bảo vệ `main`, tên nhánh `phaseN-<tên>`, mục quy trình, chạy thử 1 vòng.
- **Không làm:** auto-merge · Claude tự merge / tag · tính năng mới.

## Global Constraints

- Bảo vệ `main`: cần PR, cần check `ci`, cấm force-push; anh bật (Settings → Branches / Rulesets).
- Tag theo `v<version>` khớp `web/package.json` (test `version.test.ts` đã bắt lệch). Release Mac vẫn chỉ bằng `npm run mac`.
- Các session Claude khác đang push thẳng `main` → sau phase này phải đổi sang nhánh + PR: ghi luật vào `CLAUDE.md` (luật cứng) và `AGENTS.md`.
- Ngoại lệ docs-only: vẫn qua PR (CI có `docs:build`), không có đường tắt.

## File đụng tới

- `docs/quy-trinh-build.md` — mục Nhánh → PR → CI → merge → tag → release
- `CLAUDE.md`, `AGENTS.md` — luật: không push thẳng `main`, mỗi phase một nhánh
- `CHANGELOG.md` (Repo)

## Tasks

### Task 1: Viết quy trình
- [ ] Mục mới trong Quy trình build (1 cột, có lệnh `git switch -c phaseN-…`, `gh pr create`, `git tag v…`). `docs:build --strict` xanh.

### Task 2: Bật bảo vệ
- [ ] Anh bật ruleset; thử `git push origin main` từ nhánh thử → bị từ chối (ghi output).

### Task 3: Chạy 1 vòng
- [ ] Lấy phase kế tiếp làm thật trên nhánh → PR → CI → anh merge → anh đồng ý tag → bản mới. Ghi link PR + tag vào trang phase.
- [ ] `CLAUDE.md` / `AGENTS.md` luật mới. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
