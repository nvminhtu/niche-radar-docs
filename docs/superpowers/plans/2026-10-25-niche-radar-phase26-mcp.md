# Niche Radar Phase 26.3 — MCP của app (Claude đọc DB, chỉ đọc) — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** MCP server nhỏ `niche-radar-mcp` để **Claude tự đọc DB** — tìm niche, so niche, viết `research/*.md` — không xuất file rồi dán tay.

**Spec:** [Phase 26.3 · MCP của app](../../web/phase-26-3-mcp.md) · **Cần trước:** Phase 15 (`lib/export/dataset.ts`), Phase 40
(hồ sơ đối thủ), Phase 43 nếu đã có (`compare_niches`; chưa có thì tool này trả bảng thô).

## Mục tiêu · làm · không làm

- **Xong khi:** Claude Code gọi được mọi tool trên DB thật; 3 câu lệnh mẫu ra đúng số (kiểm tay với UI) · test từng tool
  (fixture DB) · thử ghi qua MCP → bị chặn.
- **Làm:** folder `mcp/` (stdio), 8 tool chỉ đọc, trả kèm nguồn, giới hạn kích thước, cài 1 lệnh, 3 quy trình mẫu.
- **Không làm:** tool ghi (tạo project, collect) · hỏi bằng lời trong UI (Phase 26.4).

## Global Constraints

- Dùng `@modelcontextprotocol/sdk` (TypeScript, stdio). Code đọc dữ liệu **dùng lại** `web/src/lib/*` (import qua path alias), không viết query thứ hai.
- Mở SQLite `readonly: true` + `PRAGMA query_only = 1`; test chứng minh lệnh ghi bị chặn.
- Mọi kết quả: `runId` / `explorationId` / `projectId`, ngày, link nguồn.
- Giới hạn ~20k ký tự mỗi kết quả; cắt + "còn X dòng".
- Không trả key, đường dẫn máy, ghi chú riêng (`projects.notes`) trừ khi tool được gọi rõ với `includeNotes: true`.
- DB tìm qua `NICHE_DB` / `dbFile()` như web.

## File đụng tới

- `mcp/package.json`, `mcp/server.ts`, `mcp/README.md` (mới) — server stdio, build ra `mcp/dist/server.js`
- `mcp/tools/*.ts` (mới) — `search_niches` · `get_research` · `get_explore` · `list_projects` · `get_project` · `get_competitor` · `get_complaints` · `compare_niches`
- `mcp/lib/limit.ts` (mới) — cắt kích thước + lọc trường riêng tư
- `web/tests/mcp-*.test.ts` hoặc `mcp/tests/` — fixture DB, kiểm read-only
- `docs/cach-dung.md`, `README.md`, `CLAUDE.md`, `CHANGELOG.md` — lệnh cài + folder mới (luật repo khi thêm folder)
- `package.json` gốc — `npm run check` chạy cả test `mcp/`

## Tasks

### Task 1: Khung server + read-only
- [ ] `mcp/` + SDK, mở DB chỉ đọc; test: `INSERT` qua kết nối → lỗi.

### Task 2: 8 tool
- [ ] Mỗi tool: schema input (zod), gọi `lib/*`, trả JSON gọn + nguồn. Test từng tool trên fixture DB.

### Task 3: Giới hạn + riêng tư
- [ ] `limit.ts`; test kết quả lớn bị cắt kèm "còn X dòng"; không lộ `notes`, key.

### Task 4: Cài + quy trình mẫu
- [ ] `claude mcp add niche-radar -- node mcp/dist/server.js` vào Cách dùng (không đường dẫn máy).
- [ ] 3 câu mẫu: "so 3 niche đã tra tuần này" · "viết research/<niche>.md từ dữ liệu" · "đối thủ nào bỏ bê trong project X".

### Task 5: Chạy thật + soát
- [ ] Cài trong Claude Code, chạy 3 câu trên DB thật, kiểm tay số với UI → ghi vào đây. README, CLAUDE.md, CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
