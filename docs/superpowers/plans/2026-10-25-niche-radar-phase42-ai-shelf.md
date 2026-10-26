# Niche Radar Phase 60 — Kệ AI (GEO / AEO) — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** hỏi Gemini, ChatGPT, Claude đúng câu người dùng hay hỏi; đếm **app nào được nhắc**, **trang nào được trích**. LLM là nguồn dữ liệu.

**Spec:** [Phase 60 · Kệ AI](../../web/phase-60-ai-shelf.md) · **Cần trước:** Phase 59 (bộ câu hỏi), Phase 41 (tên đối thủ + regex),
Phase 27.6 (key Gemini, sổ chi phí). Đọc `scripts/geo.py` của repo App-AI-Skills để dùng **cùng câu lệnh mẫu + cách đếm**.

## Mục tiêu · làm · không làm

- **Xong khi:** 3 niche thật × 10 câu × ≥ 2 engine xong dưới trần chi phí · kiểm tay 10 câu trả lời: đếm nhắc tên đúng · kết quả
  1 niche khớp `geo.py analyze` trên cùng câu hỏi.
- **Làm:** chọn 10–20 câu, hỏi mỗi câu × engine 1 lần, đếm nhắc tên (regex), đếm trang được trích, cờ câu trả lời yếu, xem nguyên văn.
- **Không làm:** Perplexity / Copilot · hỏi lặp lấy trung bình · đo app của mình (`/app-geo`).

## Global Constraints

- Engine sau 1 interface: `gemini_grounded` (API, Google Search grounding), `chatgpt_cli` (`codex exec`), `claude_cli` (`claude -p`).
  CLI chạy bằng `child_process` trên máy, không key trong app; không có CLI → engine "không chạy được: <lý do>".
- Prompt mẫu chép từ `geo.py` vào `web/src/lib/geo/prompt.ts` (ghi nguồn + ngày chép); đổi thì đổi cả hai — test so chuỗi với file mẫu đã lưu.
- Đếm bằng regex trên chữ đã lưu (`web/src/lib/geo/count.ts`), không nhờ AI đếm. Regex tên lấy từ đối thủ (tên thương hiệu trước ":" / " - ").
- Mỗi câu trả lời lưu nguyên văn + engine + model + ngày. Số cũ không trộn với số mới (lọc theo lần đo).
- Chạy song song tối đa 2, trần chi phí / niche (Gemini qua sổ chi phí Phase 27.6; CLI tính 0 đ, ghi thời gian).
- "Câu trả lời yếu": không nhắc app nào, hoặc chỉ nhắc app có cờ `bị chê` (Phase 41).

## File đụng tới

- `web/src/lib/geo/engines.ts` (mới) — 3 engine
- `web/src/lib/geo/prompt.ts` (mới) — câu lệnh mẫu như `geo.py`
- `web/src/lib/geo/count.ts` (mới) — đếm nhắc tên, tách URL / domain nguồn
- `web/src/db/schema.ts` + migration mới — `geo_runs` (runId, createdAt), `geo_answers` (geoRunId, questionId, engine, model, text, sources json, ms, costUsd)
- `web/src/server/app.ts` — `POST /research/:id/geo` (chọn câu) · `GET /research/:id/geo`
- `web/src/components/AiShelfBlock.tsx` (mới) — ma trận câu × engine, app được nhắc, domain được trích, cờ yếu, mở nguyên văn
- `web/tests/geo-*.test.ts` — fixture câu trả lời thật đã lưu

## Tasks

### Task 1: Prompt + đếm
- [ ] Chép prompt + luật đếm từ `geo.py`; `count.ts` + test trên 10 câu trả lời fixture.

### Task 2: Engine
- [ ] 3 engine; test với `exec` / fetch giả; engine thiếu → báo lý do.

### Task 3: Chạy + lưu + UI
- [ ] Migration, route, chạy song song 2, trần; `AiShelfBlock`.

### Task 4: Chạy thật + đối chiếu
- [ ] 3 niche × 10 câu × ≥ 2 engine; kiểm tay 10 câu; chạy `geo.py run` + `analyze` cùng câu cho 1 niche, so số → ghi vào đây.
- [ ] Screenshot 1340 + 375, Read. `features.ts`, chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
