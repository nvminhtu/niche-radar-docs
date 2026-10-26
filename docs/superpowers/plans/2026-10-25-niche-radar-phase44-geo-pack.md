# Niche Radar Phase 61 — Gói GEO + trang cần viết — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Chỉ xuất gói — không viết bài, không đăng, không tạo file trong repo App-AI-Skills thay người dùng.

**Goal:** niche đã chọn → **gói GEO** đúng định dạng `scripts/geo.py` + **danh sách trang cần viết** để được Google và AI nhắc.

**Spec:** [Phase 61 · Gói GEO](../../web/phase-61-geo-pack.md) · **Cần trước:** Phase 58 (câu hỏi), 42 (trang AI trích), 43 (câu chưa ai trả lời tốt),
38 (lớp AI Cite cho lý do).

## Mục tiêu · làm · không làm

- **Xong khi:** 1 niche thật xuất gói → `python3 scripts/geo.py run <dir>` + `analyze` chạy được, không sửa tay · danh sách trang cần viết
  ≥ 5 dòng, mỗi lý do có trích dẫn qua kiểm Phase 26.4 · gói mở bằng `/app-geo` (Pha 1 — Bộ câu hỏi) dùng được luôn.
- **Làm:** `questions.tsv`, `brands.tsv`, `pages.md` (trang cần viết), `README.md` lệnh chạy, đóng `geo-pack/` (zip).
- **Không làm:** viết nháp bài (`/oneclicktool-blog`) · đo lại sau ra mắt (`/app-geo` + `geo.py compare`).

## Global Constraints

- Định dạng theo `geo.py` **hiện tại**: đọc `geo.py` lúc làm, ghi phiên bản / commit đã đối chiếu vào code (`GEO_PY_FORMAT`). `geo.py` đổi →
  sửa phase này, không sửa `geo.py`.
- `questions.tsv`: `id · nhóm · câu hỏi`, 10–40 câu. `brands.tsv`: `nhóm · regex`, mỗi đối thủ 1 dòng + dòng `*` để trống cho domain mình.
- Trang cần viết: loại (so sánh "X vs Y" · "best app for…" · "how to…" · alternative) theo luật từ dạng câu hỏi; trang AI đang trích (Phase 59);
  lý do 1 dòng sinh qua `ask` (Phase 26.4) với ref, qua `cite-check`.
- Test chạy `geo.py` thật chỉ khi có Python + file (skip nếu không có, ghi lý do) — kiểm định dạng bằng parser TS bám theo `geo.py`.

## File đụng tới

- `web/src/lib/geo/pack.ts` (mới) — dựng 4 file + zip (dùng `zip.ts` của Phase 15)
- `web/src/lib/geo/pages.ts` (mới) — luật loại trang + lý do có trích dẫn
- `web/src/server/app.ts` — `GET /research/:id/geo-pack.zip`
- nút "Xuất gói GEO" trên `/r/:id` + project ứng viên
- `web/tests/geo-pack.test.ts` + fixture `questions.tsv` mẫu từ `geo.py`

## Tasks

### Task 1: Đối chiếu định dạng
- [ ] Đọc `geo.py` (lệnh `run`, `analyze`), ghi định dạng 2 file vào test fixture.

### Task 2: Xuất file
- [ ] `pack.ts` + test định dạng (cột, tab, encoding, số câu).

### Task 3: Trang cần viết
- [ ] `pages.ts` + lý do qua AI Cite; cờ đỏ → không đưa vào gói. Test với Ask giả.

### Task 4: Chạy thật + soát
- [ ] 1 niche: xuất → `geo.py run` + `analyze` → mở bằng `/app-geo` Pha 1. Ghi kết quả. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
