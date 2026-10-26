# Niche Radar Phase 15 — Export (CSV, JSON, gói cho LLM + brief tính năng) — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [x]`).

**Goal:** **một nút Xuất chung**: phạm vi × định dạng. Excel / Sheets mở được, code đọc được, có **gói cho LLM** không vượt
trần token, và gói đó kèm khung để AI viết **brief tính năng** (khách · vấn đề · giải pháp khác · MVP · giá thử · 10 người đầu).

**Spec:** [Phase 15 · Export](../../web/phase-15-export.md) · **Đổi 2026-10-26:** kéo lên ngay sau Phase 11, gộp Product Brief
Export (Version 12). Không chờ Phase 18–21 — dùng dữ liệu đang có (chủ đề than AI · điểm v2 · Feature Gap đã lưu · item keyword).

## Mục tiêu · làm · không làm

- **Xong khi:** CSV mở trong Numbers + Google Sheets không vỡ dấu, không lệch cột (3 niche thật) · JSON 3 niche đủ 6 bảng,
  `schema_version` 1 · gói LLM 1 niche ≤ 8k token, dán vào Claude hỏi 5 câu kiểm → 5/5 đúng số · Claude viết brief tính năng
  đủ 7 mục, mã nguồn có thật · `/app-demand` đọc được gói Markdown không sửa tay.
- **Làm:** hộp thoại Xuất chung (trang Research, trang Project) · CSV · JSON · Markdown (evidence pack) · gói LLM
  (`brief.md` + `schema.md` + `prompt.md`) · trần token · `.zip` / Copy cho AI.
- **Không làm:** phạm vi Explore / cả DB · JSONL · file JSON Schema · nhập từ CSV · PDF / slide · API (MCP ở Phase 27.3) ·
  tự gửi file lên AI · tool tự viết brief.

## Global Constraints

- **Một nguồn dữ liệu**: `web/src/lib/export/dataset.ts` dựng `Dataset` (keywords · competitors · complaints · gaps · trends ·
  scores) cho phạm vi run / project. Mọi định dạng render từ `Dataset` → cùng số (test so chéo).
- **Không gọi mạng khi xuất**: Feature Gap dựng bằng fetcher chỉ đọc cache (`gapMatrix` với listing / iap ném lỗi) — ô chưa
  đọc là `unknown`.
- CSV: UTF-8 có BOM, cột tiếng Anh `snake_case` cố định, ngày ISO, số thô, dùng lại `csvCell`.
- JSON có `format: "niche-radar/export"` + `schema_version: 1`; mô tả cột ở `docs/export-schema.md` và `schema.md` của gói LLM
  (cùng một bảng `COLUMNS` trong code). Đổi tên cột = tăng `schema_version` + CHANGELOG.
- Mã nguồn trong brief: `C<n>` đối thủ · `P<n>` lời chê · `G<n>` khoảng trống · `S<n>` điểm · `T` Trends · `K<n>` keyword.
- Ước token = ký tự / 3 (ghi rõ là ước; tiếng Việt có dấu tốn token hơn nên chia 3 thay vì 4); cắt theo thứ tự cố định: đuôi bảng keyword → đối thủ ngoài top 5 → câu trích thứ 3+ →
  Trends chi tiết; ghi "đã cắt X dòng".
- `.zip` tự viết (store, CRC32) — không thêm dependency.
- Lựa chọn lần trước nhớ bằng localStorage (try/catch).

## File đụng tới

- `web/src/lib/export/dataset.ts` (mới) — dựng `Dataset` theo phạm vi, dùng lại `run-view`, `projects`, `score-v2`, `gap`, `ai/tasks`
- `web/src/lib/export/columns.ts` (mới) — cột từng bảng + mô tả (dùng cho CSV, JSON, `schema.md`, docs)
- `web/src/lib/export/formats.ts` (mới) — CSV · JSON · Markdown
- `web/src/lib/export/llm.ts` (mới) — `brief.md` · `schema.md` · `prompt.md` (khung brief tính năng) + cắt theo trần
- `web/src/lib/export/zip.ts` (mới) — đóng `.zip` không nén
- `web/src/server/app.ts` — `GET /api/export?scope=run:12 | project:3&format=csv | json | md | llm&cap=8000[&preview=1]`
- `web/src/components/ExportDialog.tsx` (mới) — hộp chọn định dạng × trần, hiện ước token, Tải / Copy cho AI
- `RunHeader`, `ProjectPage` — gắn nút Xuất
- `web/src/lib/features.ts` — thêm dòng "Xuất cho AI + brief tính năng"
- `docs/export-schema.md` (mới) + `mkdocs.yml` — tài liệu cột
- `web/tests/export.test.ts`

## Tasks

### Task 1: Dataset chung
- [x] `dataset.ts` cho run + project; mỗi bảng có `source` + `fetched_at`.
- [x] Test: dataset của 1 run fixture có đủ 6 bảng, số khớp `run-view` + `scoreV2`.

### Task 2: CSV + JSON + Markdown
- [x] `columns.ts`, `formats.ts` (BOM, cột cố định, `format` + `schema_version`); Markdown = evidence pack (run) / báo cáo project.
- [x] Test: CSV có BOM + đúng số cột mỗi dòng; JSON parse lại ra cùng số.

### Task 3: Gói LLM + brief tính năng + trần token
- [x] `llm.ts`: `brief.md` (front matter; số chính; top đối thủ `C`; lời chê + câu trích `P`; khoảng trống `G`; giá; điểm + cờ `S`),
  `schema.md`, `prompt.md` (5 câu kiểm + khung brief 7 mục, luật dẫn mã nguồn, `chưa đo`).
- [x] Cắt theo trần 8k / 32k / 128k, trả `{ files, estTokens, cut }`. Test: trần 8k không vượt; ghi đúng số dòng cắt.

### Task 4: API + zip + hộp thoại
- [x] `zip.ts` + route `/api/export`; `preview=1` trả JSON `{ files: [{name, size}], estTokens, cut }`.
- [x] `ExportDialog` ở trang Research + Project; nhiều file → `.zip`; gói LLM có **Copy cho AI**.
- [x] Test so chéo: cùng run → CSV, JSON, gói LLM cùng số (top đối thủ, số rating, điểm).

### Task 4b: Còn lại — từ review Phase 18–42 (2026-10-26, nhánh khác)
- [x] Phạm vi subreddit (đọc `lib/reddit-gap.ts`), bảng `reddit_gaps`; nút Tải .md của trang Reddit Gap gọi qua lớp mới (giữ top 20 gap + 3 link mẫu).
- [x] Test: gói Markdown có đủ các mục `/app-demand` đọc (đối chiếu SKILL.md của app-demand, ghi danh sách mục vào test).

### Task 5: Chạy thật + soát
- [x] Build + 3 niche thật: CSV mở trong Numbers (screenshot), JSON đủ bảng, gói LLM ≤ 8k, dán vào Claude hỏi 5 câu + viết brief → ghi kết quả.
- [x] Screenshot 1280 + 375 hộp Xuất. Chip phase, ROADMAP, CHANGELOG, features.ts.

## Tiến độ

- 2026-10-25: viết plan.
- 2026-10-26: kéo lên ngay sau Phase 11, gộp brief tính năng; cắt phạm vi Explore / cả DB, JSONL, file JSON Schema (→ Appendix).
  Mockup: hộp thoại nhỏ dùng lại kiểu popover `CollectButton` — không sinh mockup riêng (ghi lệch quy trình).
- 2026-10-26: Task 1–4 xong (`040d0d8`, `a6c7d3a`), 261 test xanh. Lệch plan: ước token chia 3 thay vì 4; thêm mức cắt mịn
  (keyword 40/20/10/5, đối thủ 40/30/20/15/10/5) vì bản đầu cắt 118 đối thủ còn 15 dù còn dư 2.5k token; Copy có đường
  dự phòng `execCommand` vì Clipboard API bị chặn trong pane / app Mac.

- 2026-10-26: merge `main` — gộp review Phase 18–42 (`4b70c8c`): 2 việc mới thành Task 4b, chưa làm.
- 2026-10-26: Task 4b xong (`be1dffe` + sửa nhãn chuyên mục), 264 test xanh. Lệch: nút Tải .md của Reddit Gap thay bằng hộp
  Xuất (route `/api/reddit/gap.md` giữ nguyên cho link cũ, cùng hàm `gapMarkdown`); Reddit Gap 1 bảng nên CSV tải thẳng, không zip.

## Kết quả chạy thật (2026-10-26, bản sao DB thật, nhánh `phase16-export`)

| Phạm vi | Gói LLM 8k | 32k / 128k | CSV | JSON |
|---|---|---|---|---|
| Research #13 habit tracker (US) | ~6,241 token, cắt 100 dòng | ~8,760 token, không cắt | zip 6 file, `unzip -t` sạch, BOM, đủ cột (118 đối thủ, 19 câu chê, 10 gap, 95 Trends) | `schema_version` 1, đủ 6 bảng |
| Research #14 budget tracker (US) | ~6,706 token, cắt 124 dòng | — | zip sạch | — |
| Research #17 bubble shooter (US) | ~5,603 token, cắt 87 dòng | — | zip sạch | — |
| Project #2 Ram Rescue (3 keyword) | ~7,738 token, cắt 123 dòng | — | — | — |

- **Numbers**: mở `complaints.csv` của #13 → đúng dấu tiếng Việt, đúng 12 cột, không lệch (xuất PDF từ Numbers để soát).
  Google Sheets: chưa mở thử.
- **Dán vào AI** (agent mới, chỉ đọc gói 8k của #13): 5/5 câu kiểm đúng số với brief (top 3 rating 1,493,862 / 813,969 /
  767,011; chủ đề 25 review; Trends −59%, 29/100; IAP lẻ 50%; điểm 5.7/10, 75% trọng số). Brief tính năng đủ 7 mục, mọi ý
  có mã nguồn có thật; ý không có số ghi "suy luận" / "giả định, cần kiểm". Kết luận AI: test thêm.
- **Giao diện**: hộp Xuất ở trang Research + Project, 1280 và 375 không tràn; Copy cho AI → clipboard có đủ gói.
- `/app-demand`: Markdown = evidence pack Phase 7 (đã đọc được từ trước), chưa chạy lại.
- **Reddit Gap** (70 bài r/macos — DB thử của session Phase 11, link bài là dữ liệu dựng, không phải bài thật): gói 8k ~3,231
  token, không cắt; 15 dòng R1–R15 cùng số với `/api/reddit/gap` (Menu bar · Tìm thay thế 14 bài, gap 38.2…); llm / csv /
  md / json đều 200. Hộp Xuất xem ở 1340: gọn, không tràn.
- **`check_demand.py` thật** trên gói Markdown #13: không lỗi mục / ô / cột; còn 9 FAIL đều là phần nhận định để TODO
  (27 TODO, 3 tiêu chí điểm, Tổng, Đề xuất) — đúng phần `/app-demand` điền.
- Thấy ngoài phạm vi: ở bề rộng ~1009px nút "Tra niche mới" trên header tràn 40px (sau đổi logo `dbfbea2`) — chưa sửa.
