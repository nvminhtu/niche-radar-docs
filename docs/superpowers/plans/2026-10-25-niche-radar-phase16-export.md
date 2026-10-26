# Niche Radar Phase 16 — Export (CSV, JSON, gói cho LLM) — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** **một nút Xuất chung**: phạm vi × định dạng. Excel / Sheets mở được, code đọc được, có **gói cho LLM** không vượt trần token.

**Spec:** [Phase 16 · Export](../../web/phase-16-export.md) · **Cần trước:** Phase 10 (bảng Reddit Gap, `lib/reddit-gap.ts`),
Phase 12 (lời chê), Phase 13 (điểm + cờ), Phase 14 (item theo loại).

## Mục tiêu · làm · không làm

- **Xong khi:** CSV mở trong Numbers + Google Sheets không vỡ dấu, không lệch cột (3 niche thật) · JSON 3 niche qua JSON
  Schema, nhập lại `.niche.json` vẫn chạy · gói LLM 1 niche ≤ 8k token, dán vào Claude hỏi 5 câu kiểm → 5/5 đúng số ·
  `/app-demand` đọc được gói Markdown không sửa tay.
- **Làm:** hộp thoại Xuất chung (Research, Explore, Project, Cài đặt → Dữ liệu), CSV · JSON / JSONL · Markdown · gói LLM, trần token, `.zip` / Copy.
- **Không làm:** nhập từ CSV · PDF / slide · API cho tool khác (MCP ở Phase 26) · tự gửi file lên AI.

## Global Constraints

- **Một nguồn dữ liệu**: `web/src/lib/export/dataset.ts` dựng `Dataset` (keywords · competitors · complaints · gaps · trends ·
  scores · reddit_gaps) cho một phạm vi (run / exploration / project / subreddit / toàn bộ). Mọi định dạng render từ `Dataset` → cùng số (test so chéo).
- CSV: UTF-8 có BOM, cột tiếng Anh `snake_case` cố định, ngày ISO, số thô (không định dạng địa phương), dùng lại `csvCell`.
- JSON có `format: "niche-radar/export"` + `schema_version`; JSON Schema ở `docs/export-schema.md` (+ file `.json` trong `docs/`).
  Đổi tên cột = tăng `schema_version` + CHANGELOG.
- Ước token = ký tự / 4 (ghi rõ là ước); cắt theo thứ tự cố định: đuôi bảng → câu trích thứ 4+ → trends chi tiết; ghi "đã cắt X dòng".
- Lựa chọn lần trước nhớ bằng localStorage (try/catch); không gửi file đi đâu.

## File đụng tới

| File | Việc |
|---|---|
| `web/src/lib/export/dataset.ts` (mới) | dựng `Dataset` theo phạm vi, dùng lại `run-view`, `explore-view`, `projects`, `complaints`, `score-v2` |
| `web/src/lib/export/csv.ts` · `json.ts` · `markdown.ts` · `llm.ts` (mới) | render từng định dạng; `llm.ts` sinh `brief.md` · `schema.md` · `prompt.md` + cắt theo trần |
| `web/src/lib/export/zip.ts` (mới) | đóng `.zip` (thư viện nhỏ thuần JS, vd `fflate`) |
| `web/src/server/app.ts` | `GET /api/export?scope=run:12&format=csv|json|jsonl|md|llm&cap=8000` → file / zip; giữ route cũ (`/explore/:id/csv`, `/projects/:id/*.csv`, `report.md`) gọi qua lớp mới |
| `web/src/components/ExportDialog.tsx` (mới) | hộp chọn phạm vi × định dạng × trần, hiện ước token, Tải / Copy |
| `RunHeader`, `ExploreDashboard`, `ProjectPage`, `SettingsPage` | gắn nút Xuất |
| `docs/export-schema.md` (mới) + `mkdocs.yml` | tài liệu cột + JSON Schema |
| `web/tests/export-*.test.ts` | |

## Tasks

### Task 1: Dataset chung
- [ ] `dataset.ts` cho 5 phạm vi (thêm subreddit — đọc `lib/reddit-gap.ts`); mỗi dòng có `source` + `fetched_at`.
- [ ] Nút Tải .md của trang Reddit Gap gọi qua lớp mới (giữ nội dung top 20 gap + 3 link mẫu).
- [ ] Test: dataset của 1 run fixture có đủ 6 bảng, số khớp `run-view`.

### Task 2: CSV + JSON / JSONL
- [ ] `csv.ts` (BOM, cột cố định từng bảng), `json.ts` (`format`, `schema_version`), JSONL cho bảng lớn.
- [ ] JSON Schema + test validate (dùng `ajv` hoặc kiểm tay bằng code nhỏ nếu không muốn thêm dependency).
- [ ] Đổi route CSV cũ sang lớp mới, giữ tên file cũ để không gãy link.

### Task 3: Markdown + gói LLM + trần token
- [ ] `markdown.ts`: tóm tắt, bảng chính, nguồn + ngày (dùng lại phần `evidence.ts`).
- [ ] `llm.ts`: `brief.md` (front matter niche / ngày / nguồn; số chính; top N; lời chê + câu trích; điểm + cờ), `schema.md`, `prompt.md`.
- [ ] Cắt theo trần 8k / 32k / 128k, trả `{ files, estTokens, cut }`. Test: trần 8k không vượt; ghi đúng số dòng cắt.

### Task 4: Hộp thoại + zip / Copy
- [ ] `ExportDialog` ở 4 chỗ; nhiều file → `niche-radar-<phạm vi>-<ngày>.zip`; 1 file → tải hoặc Copy.
- [ ] Test so chéo: cùng phạm vi → CSV, JSON, Markdown, gói LLM cùng số (top đối thủ, số rating, điểm).

### Task 5: Chạy thật + soát
- [ ] 3 niche: mở CSV trong Numbers + Google Sheets (screenshot), validate JSON, gói LLM ≤ 8k, dán vào Claude hỏi 5 câu → ghi kết quả.
- [ ] Test: gói Markdown có đủ các mục `/app-demand` đọc (đối chiếu SKILL.md của app-demand, ghi danh sách mục vào test).
- [ ] Đưa gói Markdown cho `/app-demand` đọc thử. Chip phase, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
- 2026-10-26: review plan — thêm phạm vi Reddit Gap (Phase 10) và test gói Markdown khớp `/app-demand`.
