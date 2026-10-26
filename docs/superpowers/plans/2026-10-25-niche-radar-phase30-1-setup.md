# Niche Radar Phase 23 — Setup ngay trong Web — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` + `npm run docs:build` xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Tool chỉ hướng dẫn + kiểm, không tự cài, không `sudo`.

**Goal:** máy thiếu đồ cài vẫn tự lên được: trang Setup đúng máy, nút **Kiểm tra máy**, gói cài chính chủ, nút **Hỏi AI**.

**Spec:** [Phase 23 · Setup ngay trong Web](../../web/phase-23-setup.md) · **Cần trước:** không.

## Mục tiêu · làm · không làm

- **Xong khi:** Mac sạch (chưa Node) mở trang Setup tĩnh → làm theo → chạy được tool, không đọc README · Kiểm tra máy báo đúng
  3 tình huống: thiếu Node · Node cũ · thiếu Command Line Tools · Hỏi AI mở đủ 4 AI, câu hỏi không chứa đường dẫn máy / key ·
  screenshot trang Setup + menu Hỏi AI đã Read.
- **Làm:** lớp 1 trang tĩnh (docs), lớp 2 `/setup` + `GET /api/setup/check`, component `AskAi`.
- **Không làm:** tự cài hộ · gọi API ChatGPT / Gemini · Linux.

## Global Constraints

- Lớp 1 là trang MkDocs `docs/setup.md` + 1 đoạn JS nhỏ (`docs/javascripts/setup-detect.js`) đoán OS + chip từ
  `navigator.userAgentData` / `platform`; đoán không chắc → hiện cả 2 bộ bước.
- Lớp 2: mỗi mục kiểm là 1 hàm trả `{ key, status: 'ok'|'missing'|'old', found, need, fix }`; Node tối thiểu **20.19** (Vite 8 đòi — đọc lại `engines` trong `web/package.json` lúc làm).
- Kiểm mạng tới Play / App Store / Trends: 1 lượt nhỏ, timeout 5 giây, không lặp.
- Link cài chỉ trang chính chủ (nodejs.org, developer.apple.com, ollama.com…), không gói lại đồ người khác.
- Câu hỏi AI chỉ có OS, phiên bản, dòng lỗi — hàm `scrub()` bỏ `/Users/...`, tên user, chuỗi giống key (`sk-`, `AIza`…). Test.
- Link 4 AI: ChatGPT (`chatgpt.com/?q=`), Claude (`claude.ai/new?q=`), Perplexity (`perplexity.ai/search?q=`) — kiểm lại tham số lúc làm;
  Gemini không nhận qua link → copy clipboard rồi mở trang.

## File đụng tới

- `docs/setup.md` (mới) + `docs/javascripts/setup-detect.js` + `mkdocs.yml` — lớp 1
- `web/src/lib/setup-check.ts` (mới) — Node, npm, better-sqlite3 (mở DB thử), cổng 3200 / 3201, mạng 3 nguồn, key Claude, Ollama
- `web/src/server/app.ts` — `GET /api/setup/check`
- `web/src/client/SetupPage.tsx` (mới) + `main.tsx` + `NavMenu.tsx` — `/setup`, nút Kiểm tra máy, bắt buộc / tuỳ chọn
- `web/src/components/AskAi.tsx` (mới) — menu dọc 4 dòng, đóng khi bấm ngoài / Esc
- `web/src/lib/scrub.ts` (mới) — che dữ liệu riêng (dùng chung với Backlog 01 góp ý)
- `README.md`, `docs/cach-dung.md` — trỏ tới trang Setup
- `web/tests/setup-check.test.ts`, `scrub.test.ts`

## Tasks

### Task 1: Kiểm tra máy (lớp 2)
- [ ] `setup-check.ts` với `exec` giả trong test: thiếu Node, Node 18, thiếu CLT, cổng bận, nguồn bị chặn.
- [ ] Route + `/setup`; mỗi mục 1 dòng cách sửa + link.

### Task 2: AskAi + scrub
- [ ] `scrub.ts` + test (đường dẫn, user, key). `AskAi` mở tab mới với câu soạn sẵn; Gemini → copy + mở.

### Task 3: Trang Setup tĩnh (lớp 1)
- [ ] `docs/setup.md` 1 cột: macOS (Apple / Intel) · Windows; JS đoán máy; link chính chủ. `npm run docs:build` xanh.

### Task 4: Thử máy sạch
- [ ] Máy Mac sạch (user macOS mới, chưa Node) làm theo trang tĩnh → chạy được. Thử 3 tình huống lỗi. Ghi kết quả.
- [ ] Screenshot `/setup` + menu Hỏi AI 1340 + 375, Read. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
