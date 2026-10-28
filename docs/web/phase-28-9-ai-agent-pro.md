# Phase 28.9 · AI Agent xịn: xuất Brief/Spec/Plan .md, gợi ý đóng mở, chat có format và nút hành động

> Ba việc làm AI Agent từ "chạy được" thành "hàng xịn": (1) phiên săn ra **file .md đem đi build** — Brief, Spec, **Plan**;
> (2) mọi đoạn **gợi ý / giải thích dài** gập lại còn 1 câu, có nút ⓘ và mở ra khi cần; (3) chat trả lời **có format đẹp**,
> và cuối mỗi câu trả lời có **nút bấm làm luôn** thay vì bắt người dùng gõ lại lệnh. Học khung của Wow Keywords:
> ô chat có chọn model, đáp án có tab bản, nút "Use this listing" một bấm.

<span class="chip chip--done">Xong 2026-10-28 · T1–T7</span>

<div class="box box--goal" markdown>
**Đã làm 2026-10-28 (nhánh `phase28-9-ai-agent-pro`, 478 test xanh, chạy thật trên bản sao DB thật).**

- **T4:** `components/Hint.tsx` (gập + nhớ theo id, `lib/hint-state.ts`) · `InfoTip` lật lên khi sát đáy và **sửa lỗi
  chạm/bấm không mở được** (mouseenter mở rồi click đóng ngay). Áp: hộp "Chi tiết gợi ý" ở Sức khoẻ niche (ảnh 1 — giờ 1 dòng
  "Show more"), "Tính điểm thế nào?" thành ⓘ, mô tả từng bước flow thành ⓘ, dải "AI đang chỉ đọc" gọn 1 hàng + ⓘ (nút bật
  quyền vẫn luôn thấy). Chưa áp: chip mức "estimate / measured" (nằm trong `<summary>`, lồng nút không hợp lệ) — để T5.
- **T1:** bước 7 **Plan làm** (`PLAN:`), prompt mốc M1/M2/M3 + checklist "xong khi"; note BRIEF / SPEC / PLAN tới 12 000 ký tự,
  note thường giữ 2000 — kiểm ở máy chủ (`/api/mcp/projects/:id/note`) và zod của MCP.
- **T2:** `lib/export/hunt-docs.ts` + route `GET /api/projects/:id/docs.md?doc=brief|spec|plan|all`, `GET /api/projects/:id/docs`,
  `POST /api/projects/:id/docs/save`. Nút **Tải .md · Copy Markdown** ở thẻ Brief/Spec/Plan, dải **Tài liệu mang đi build**
  (Tải cả bộ · Lưu vào thư mục AI), khối "Brief · Spec · Plan (.md)" trong hộp Xuất trang Project. Bảng nguồn bắt cả
  "Research #44 #45" (AI hay viết gộp — gặp khi chạy thật).
- **Khác plan:** "Tải cả bộ" **bật khi có ≥ 1 tài liệu** (plan ghi đợi đủ 3) — phần chưa viết ghi "Chưa viết" trong file,
  có Brief + Spec là mang đi được ngay. Tên file không kèm ngày (`<slug>-spec.md`) để lưu đè cùng chỗ.
- **Chưa kiểm:** tải trên app Mac (Tauri) — dùng chung đường `<a download>` của Phase 15, chưa build lại .app để thử.
</div>

<div class="box box--goal" markdown>
**Hiện có — đối chiếu code ngày 2026-10-27 (sau commit `29b2509`).**

- **Chat đã render Markdown:** `web/src/components/Markdown.tsx` (marked GFM + DOMPurify, "Research #12" thành link).
  Dùng ở `HuntChat.tsx`, `ChatPanel.tsx` (Hỏi AI) và note BRIEF/SPEC trong `HuntFlow.tsx`. Chưa có: nút copy khối code,
  thanh công cụ dưới mỗi câu trả lời, tool-call hiện gọn, nút hành động, chip câu hỏi tiếp.
- **Nút trong chat hiện có đúng 1 loại:** tool MCP `suggest_view` → nút "Mở" ở dòng "AI gợi ý xem" (`HuntChat.tsx:150`).
- **Brief / Spec là note**: AI gọi `add_project_note` với text mở đầu `BRIEF:` / `SPEC:` (`hunt-flow.ts`), **trần 2000 ký tự**
  (`mcp/write-tools.ts`) — Spec ở ảnh chụp 2026-10-27 đã bị dồn chữ vì trần này. **Chưa có bước Plan**, chưa có nút tải .md,
  chỉ xem được trong `<details>` của thẻ bước.
- **Xuất file** hiện đi qua `/api/export` + `<a download>` (`ExportDialog.tsx`, Phase 15) — đường này đã chạy cả bản Web
  lẫn app Mac (Tauri). Phạm vi chưa có Brief/Spec/Plan.
- **Ô chat** (`HuntChat.tsx`): textarea + ô tick "So sánh tự động" + nút ✦ Gửi. Không chọn model tại chỗ; model nằm ở
  Settings (`lib/ai/settings.ts` có `MODELS` từng tuyến) và `runChat()` **chưa nhận model** (ghi ở Phase 28.7 T1).
- **Gợi ý dài**: `HealthBlock.tsx` đã có `<details>` "Tính điểm thế nào? ⓘ" và câu kết luận tách từ `summary`; nhưng các chỗ
  khác vẫn bày đủ chữ: hộp vàng hướng dẫn/cảnh báo trong `HuntChat.tsx`, đoạn "what" của thẻ bước `HuntFlow.tsx`,
  dòng ngưỡng ở Settings, chú thích AiTaskBlock. Mỗi chỗ tự viết `<details>` theo kiểu riêng, không nhớ đóng/mở.
</div>

**Cần xong trước:** nền phiên săn [Phase 28.6](phase-28-6-ai-agent.md) (đã có code). Nên làm cùng hoặc sau
[Phase 28.7](phase-28-7-ai-agent-ux.md) T1 (model thật) + T3 (menu lệnh) — 28.9 **dùng lại**, không làm lại hai phần đó.
Phần "chốt bản, khoá mục, Gói Build .zip, đồng bộ MCP" vẫn là của [Phase 28.5](phase-28-5-brief-plan.md); 28.9 chỉ làm
**file .md tải được ngay** từ note đang có — bậc thang lên 28.5, không đè.

**Gộp:** mục **B · Giải thích thu gọn** của [Phase 28.8](phase-28-8-niche-ui-polish.md) làm bằng component chung ở T4
của phase này — làm một lần, 28.8 B chỉ còn việc áp vào `HealthBlock`.

## Mục tiêu · cần làm · KHÔNG làm

- **Mục tiêu:** xong một phiên săn là bấm 1 nút có bộ file `.md` (Brief · Spec · Plan) đưa thẳng cho Claude Code / Codex /
  dev; trang không còn tường chữ; chat đọc như tài liệu và đi tiếp bằng nút bấm.
- **Cần làm:**
    - T1 · Bước 7 **Plan** + nới trần note
    - T2 · **Xuất .md**: từng file + cả bộ, copy, lưu vào thư mục AI
    - T3 · **Tab bản** cho Brief/Spec/Plan (kiểu Wow Keywords "Current · 1 · 2 · 3")
    - T4 · **Gợi ý gập + ⓘ** dùng chung (`<Hint>`, `<InfoTip>`), áp lên mọi chỗ đang bày chữ dài
    - T5 · **Câu trả lời có format xịn**: khung tin nhắn, copy code, bảng cuộn, tool-call gọn, thanh công cụ
    - T6 · **Nút hành động trong chat**: nút do code sinh (chắc chắn) + nút AI đề xuất qua tool `suggest_actions` (danh sách trắng)
    - T7 · **Ô chat kiểu Wow Keywords**: chọn model tại chỗ, nút `/`, nút gửi tròn / dừng, chip câu tiếp theo
- **KHÔNG làm:**
    - Chốt bản, khoá mục, Gói Build `.zip`, pull/sync qua MCP, PDF, link chia sẻ (→ Phase 28.5 / Version 12)
    - Nhập bằng giọng nói (nút mic trong ảnh Wow Keywords) — chưa ai xin, tốn công quyền micro trên Tauri
    - Cho AI trả HTML/JS tự do hay nút gọi URL tuỳ ý — nút chỉ từ danh sách trắng, mỗi nút đi đúng API nút tay đang dùng
    - Thêm nhà cung cấp chat mới (Gemini/API chat), đổi công thức điểm, sửa collector
    - Lưu toàn bộ lịch sử hội thoại vào DB (vẫn chỉ resume ID như 28.6)
- Tài liệu và menu xếp **một cột dọc**; tên dài xuống dòng, không lưới thẻ hẹp.

## Khung tham chiếu — Wow Keywords (xem 2026-10-27)

Đọc trang chủ wowkeywords.com và ảnh chụp màn Optimize người dùng gửi. Những gì **lấy**, gắn vào task:

| Wow Keywords có | Niche Radar làm | Task |
|---|---|---|
| Tab bản `Current · 1 Scanner subtitle ★ +237 · 2 · 3 · +`, mỗi tab một bản listing | Tab bản cho Brief / Spec / Plan, mỗi bản là 1 note, có ngày + model đã viết | T3 |
| Nút xanh **"✓ Use this listing"** một bấm | Nút **"Dùng bản này"** (ghim bản chính để xuất) + **"Tải .md"** | T2, T3 |
| `› Explanation` gập dưới bản | Lý do / nguồn của bản gập trong `<Hint>` | T3, T4 |
| Ô chat: placeholder gợi ý câu lệnh + "or type /", chip **model ⌄** ở góc trái, nút gửi tròn ở góc phải | Ô chat cùng bố cục: model ⌄ · `/` lệnh · ✦ gửi tròn / ■ dừng | T7 |
| Agent chạy trên AI người dùng đã trả (Claude Code, Codex, OpenCode, Ollama) | Giữ nguyên định vị "chạy bằng Claude Code / Codex của bạn"; không thêm tuyến | — |
| Agent đọc DB qua MCP (`board_get(...)` hiện ra trong khung) | Tool-call hiện thành dòng gọn mở ra xem được | T5 |

Không lấy: số "reach / difficulty" của listing (Niche Radar đã có điểm sức khoẻ), bảng quốc gia.

## T1 · Bước 7 "Plan" + nới trần note — S

**Mục tiêu:** flow 6 bước hiện dừng ở Spec; người dùng xin "spec / plan" → thêm bước cuối viết **plan làm**.

**Cần làm**

- `FLOW_STEPS` thêm `plan` sau `spec` (`hunt-flow.ts`): tiêu đề "Plan làm", mô tả "Từ Spec, AI chia việc theo thứ tự:
  mốc 1 bản chạy được → mốc bán được, mỗi việc có tiêu chí xong kiểm được". Prompt EN/VI mới trong `en-text-flow.ts`.
- Khuôn Plan (AI viết Markdown, mỗi mục `##`): **Mục tiêu · cần làm · KHÔNG làm** → **Mốc** (M1 bản chạy, M2 paywall,
  M3 lên store) → **Việc** từng mốc dạng checklist `- [ ]` kèm tiêu chí xong → **Rủi ro** → **Đo gì sau ra mắt**.
  Mỗi tính năng trong Plan phải trỏ về mục trong Spec; số có nguồn Research #id.
- Ghi bằng `add_project_note`, tiền tố `PLAN:`. `noteOf()` / `noteMarkdown()` (`HuntFlow.tsx`) nhận thêm `PLAN`.
- Nới trần: note có tiền tố `BRIEF:` / `SPEC:` / `PLAN:` cho tới **12 000 ký tự**; note khác giữ 2000. Kiểm ở **server**
  (route `/projects/:id/note`) chứ không chỉ zod của MCP. Prompt Brief/Spec bỏ câu "tối đa 2000 ký tự".
- Thẻ "Bạn đang ở bước nào" + thanh bước hiện 7 bước; điều kiện mở bước Plan = đã có note SPEC (theo luật T4 của 28.7 nếu
  đã làm, chưa thì cảnh báo như bước khác hiện nay).

**Không làm:** để AI tự chạy liền Brief → Spec → Plan không hỏi (vẫn mỗi bước một bấm).

**Tiêu chí kiểm được:** chạy thật 1 phiên tới bước 7, có note PLAN ≥ 3 mốc, mỗi việc có tiêu chí xong; Spec dài > 2000 ký tự
lưu đủ, không bị cắt; note thường > 2000 vẫn bị từ chối.

**File đụng:** `web/src/lib/hunt-flow.ts`, `HuntFlow.tsx`, `locales/en-text-flow.ts`, `mcp/write-tools.ts`,
route note ở `web/src/server/` (hunt-api / project API), `lib/ai/ai-dir.ts` (playbook nhắc bước Plan).

**Test:** `hunt-flow.test.ts` (bước 7 xong khi có PLAN, hoàn tác thì lùi), test route note (trần theo tiền tố).

## T2 · Xuất .md — từng file và cả bộ — M

**Mục tiêu:** một bấm ra file Markdown đọc được ở mọi nơi (GitHub, Obsidian, Claude Code, Codex), có nguồn.

**Cần làm**

- Endpoint dùng lại `/api/export`: phạm vi mới `scope=hunt-docs&project=<id>&doc=brief|spec|plan|all`, `format=md`.
  Dùng đúng đường tải `<a download>` của `ExportDialog` để chạy được trên app Mac.
- **Tên file:** `<slug-project>-brief.md`, `-spec.md`, `-plan.md`; cả bộ `<slug-project>-brief-spec-plan.md` (1 file, 3 phần
  theo thứ tự). Slug từ tên project, bỏ dấu.
- **Đầu file (frontmatter YAML):** `project`, `project_id`, `doc`, `version` (bản mấy, T3), `written_at`, `model` (nếu biết
  từ 28.7 T1, không thì bỏ trống — không bịa), `source: Niche Radar`, `schema_version: 1`.
- **Cuối file — bảng nguồn:** mọi `Research #id` xuất hiện trong bài → keyword, nước, ngày tra, link store top app,
  điểm sức khoẻ lúc xuất. Mã không có trong DB → liệt kê riêng "mã không tìm thấy" (không xoá chữ AI).
- Bỏ tiền tố `BRIEF:` / `SPEC:` / `PLAN:`, áp `noteMarkdown()` để file sạch như trên màn.
- **Chỗ bấm:**
    - thẻ bước Brief / Spec / Plan trong `HuntFlow`: **Tải .md** · **Copy Markdown**
    - đầu trang phiên săn (hoặc cuối flow khi đủ 3 note): **Tải cả bộ .md** (xám + lý do khi thiếu note)
    - hộp Xuất của trang Project (Phase 15): thêm phạm vi "Brief · Spec · Plan"
    - nút trong chat sau khi AI ghi note (T6)
- **Lưu vào thư mục AI** (tuỳ chọn, khi đã cài thư mục AI ở Phase 27): ghi `briefs/<slug-project>/brief.md|spec.md|plan.md`
  để Claude Code / Codex đọc thẳng; ghi đè thì giữ bản cũ `*.prev.md` (một bản), báo đường dẫn đã ghi.
- Định dạng thêm vào [Định dạng file xuất](../export-schema.md).

**Không làm:** `.docx` / PDF, gói `.zip` cho AI code (28.5), đẩy file lên GitHub.

**Tiêu chí kiểm được:** tải 3 file + 1 file gộp từ phiên thật trên bản Web và app Mac; mở bằng GitHub preview và
Claude Code đọc được, frontmatter parse được; bảng nguồn khớp DB; thiếu note → nút xám có lý do.

**File đụng:** `web/src/lib/export/` (module mới `hunt-docs.ts`), `web/src/server/app.ts` (scope export),
`HuntFlow.tsx`, `HuntPage.tsx`, `ExportDialog.tsx`, `lib/ai/ai-dir.ts` (ghi thư mục AI), `docs/export-schema.md`.

**Test:** mới `web/tests/export-hunt-docs.test.ts`: tên file/slug có dấu, frontmatter, gộp 3 phần đúng thứ tự,
bảng nguồn + mã bịa, thiếu note, ghi thư mục AI giữ `.prev.md`.

## T3 · Tab bản cho Brief / Spec / Plan — M

**Mục tiêu:** hỏi AI viết lại không làm mất bản cũ; chọn bản tốt nhất như Wow Keywords chọn listing.

**Cần làm**

- Đọc **mọi** note cùng tiền tố (chưa hoàn tác) → tab `Bản 1 · Bản 2 · Bản 3 …` theo thời gian, nhãn ngắn = dòng `##`
  đầu hoặc 4–5 từ đầu (AI có thể đặt nhãn bằng dòng `Label: …` trong note). Bản đang dùng có ★.
- Nút **"✓ Dùng bản này"** ghi dòng nhật ký `projectLog` loại `doc_pick` (doc + log id); xuất .md (T2) mặc định lấy bản ★,
  chưa ghim → bản mới nhất. Không cần migration nếu `projectLog` nhận kiểu mới; nếu có enum thì thêm migration nhỏ.
- Nút **"+ Viết lại"** cạnh tab: đưa vào ô chat prompt "Viết lại SPEC, giữ … đổi …" để người dùng sửa rồi gửi (không tự gửi).
- `› Vì sao bản này` gập (T4): danh sách mã nguồn bản đó dùng + model + ngày.
- Tab cuộn ngang khi nhiều bản (chỉ dải tab cuộn, trang không cuộn ngang).

**Không làm:** so khác biệt từng dòng giữa hai bản, khoá mục, Chốt (28.5).

**Tiêu chí kiểm được:** viết Spec 3 lần → 3 tab; ghim bản 2 → tải .md ra bản 2; hoàn tác note bản 3 → tab biến mất,
★ không trỏ vào bản đã hoàn tác.

**File đụng:** `HuntFlow.tsx` (hoặc component mới `HuntDocTabs.tsx`), `hunt-flow.ts`, `hunt.ts` (đọc log `doc_pick`),
`lib/export/hunt-docs.ts`.

**Test:** `hunt-flow.test.ts` / mới `hunt-docs.test.ts`: chọn bản, mặc định mới nhất, hoàn tác.

## T4 · Gợi ý gập + nút ⓘ dùng chung — S/M

**Mục tiêu:** chỗ nào bày đoạn giải thích dài (như hộp "Some money (9/10 competitors charge)… Thresholds: BUILD ≥ 6…"
trong ảnh 1) thì mặc định chỉ còn **một câu kết luận** + nút mở; thuật ngữ ngắn có ⓘ.

**Cần làm**

- Component `web/src/components/Hint.tsx`:
    - `<Hint id title summary>` — dòng tóm tắt luôn thấy + nút `› Xem thêm` / `ⓘ`; mở ra nội dung đầy đủ (Markdown được).
      Dựng trên `<details>/<summary>` để Enter/Space chạy sẵn. Nhớ đóng/mở theo `id` trong `localStorage`
      (bọc try/catch; hỏng thì về mặc định đóng).
    - `<InfoTip text>` — nút ⓘ 24×24, mở bằng hover **và** focus **và** chạm; Esc đóng; nội dung ≤ 2 câu, dài hơn thì dùng `<Hint>`.
      Không bị cắt trong khung chat hẹp (tự lật lên/trái).
- Áp vào (kiểm kê theo code 2026-10-27):
    - `HealthBlock.tsx`: câu tóm tắt + "Thresholds … edit in Settings" vào `<Hint>` (đây là 28.8 B — làm ở đây)
    - `HuntFlow.tsx`: đoạn "what" của thẻ bước → 1 dòng + ⓘ; cảnh báo thiếu điều kiện giữ ngoài
    - `HuntChat.tsx`: hộp vàng hướng dẫn / "Cho AI thêm dữ liệu" → `<Hint>` (lỗi + quyền **không** gập)
    - `AiTaskBlock` / Settings AI: dòng chú thích cách chạy, ngưỡng
    - nhãn mức "estimate (proxy)", "measured", "not measured" ở bảng yếu tố → `<InfoTip>` giải nghĩa
- Luật: **không gập** lỗi, cờ chặn, cảnh báo dữ liệu thiếu, quyền ghi — những thứ người dùng phải thấy.

**Không làm:** tour hướng dẫn (Phase 45), đổi chữ `summary` server viết (evidence pack dùng lại).

**Tiêu chí kiểm được:** ở 1340px trang niche và trang phiên săn không còn đoạn giải thích > 2 dòng mở sẵn; mở/đóng nhớ sau
tải lại; bàn phím Tab → Enter mở, Esc đóng ⓘ và focus quay lại nút; trên màn chạm ⓘ mở được; EN/VI không tràn.

**File đụng:** mới `Hint.tsx`; `HealthBlock.tsx`, `HuntFlow.tsx`, `HuntChat.tsx`, `AiTaskBlock.tsx`, trang Settings AI; locale.

**Test:** mới `web/tests/hint.test.ts` (nhớ trạng thái, localStorage hỏng), kiểm tay bàn phím + chạm trong trình duyệt.

## T5 · Câu trả lời có format xịn — M

**Mục tiêu:** đọc câu trả lời như một tài liệu gọn, không phải cục chữ.

**Cần làm**

- **Khung tin nhắn:** tin người dùng là bong bóng bên phải (như hiện tại); trả lời của AI **không bong bóng**, rộng hết khung,
  dòng đầu nhỏ: dấu ✦ + tên AI/model (lấy từ 28.7 T1 nếu có) + giờ. Dòng cuối nhỏ xám: thời gian chạy · token (đã có `ms`,
  `inputTokens`, `outputTokens` trong event `done`).
- **Kiểu chữ trong `.md`** (`globals.css`): `##` / `###` rõ cỡ, danh sách thụt đều, `- [ ]` thành ô tick chỉ đọc,
  bảng có viền + cuộn ngang riêng trong khung hẹp, trích dẫn `>` thành hộp nhạt, `code` nền xám.
- **Khối code:** nút **Copy** góc phải; ngôn ngữ ghi nhỏ. Làm bằng renderer `code` của `marked` + một handler click trong
  `Markdown.tsx` (vẫn qua DOMPurify; nút là phần tử app thêm, không phải HTML của AI).
- **Mã nguồn:** link "Research #12" hiện thành chip nhỏ (keyword khi biết, hover/ⓘ ra điểm + ngày) thay vì chữ gạch chân.
- **Tool-call gọn:** sự kiện `tool` hiện thành một dòng "⚙ start_research · 3 keyword" trong tin nhắn, gập; mở ra thấy input
  đã lọc (không dump config). Trạng thái chạy/xong của tool là việc của 28.7 T6 — ở đây chỉ hiển thị.
- **Thanh công cụ dưới mỗi câu trả lời** (hiện khi hover/focus, luôn hiện trên màn chạm): Copy · Tải .md · Hỏi lại
  (đưa câu hỏi cũ vào ô chat, không tự gửi).
- Câu trả lời đang chạy: con trỏ nhấp nháy cuối chữ + nút ■ Dừng (T7); Markdown dở dang (bảng, code chưa đóng) không làm vỡ khung.

**Không làm:** render biểu đồ / mermaid trong chat, LaTeX, ảnh do AI gửi.

**Tiêu chí kiểm được:** một câu trả lời mẫu có `##`, danh sách, bảng 6 cột, khối code, checklist, 5 mã Research hiện đúng ở
khung chat 380px và 600px; copy khối code ra đúng chữ; HTML/script AI chèn vào vẫn bị DOMPurify lọc.

**File đụng:** `Markdown.tsx`, `globals.css`, `HuntChat.tsx`, `ChatPanel.tsx` (Hỏi AI dùng chung phần hiển thị) — tách
component `ChatMessage.tsx` để hai khung dùng chung.

**Test:** `markdown.test.ts` (mới hoặc bổ sung): code block có nút copy, script bị lọc, Markdown dở dang, chip mã nguồn.

## T6 · Nút hành động trong chat — L

**Mục tiêu:** cuối câu trả lời có nút bấm làm luôn việc tiếp theo, như "Use this listing" của Wow Keywords.
Hai nguồn nút, **không** để AI tự viết nút bằng chữ.

**Nguồn 1 — code sinh (chắc chắn đúng):** đọc trạng thái phiên sau mỗi lượt (`flowState()` + nhật ký) và gắn nút:

| Sau khi | Nút |
|---|---|
| AI đề xuất keyword + gửi tra | `Xem ứng viên` · `So sánh khi xong` |
| Ứng viên tra xong | `So sánh 3 niche` · `Giữ BEST` |
| AI giữ / loại ứng viên | `Mở niche đã giữ` · `Hoàn tác` |
| Ghi BRIEF / SPEC / PLAN | `Xem` · `Tải .md` · `Viết bước tiếp →` |
| Đủ Brief + Spec + Plan | `Tải cả bộ .md` · `Lưu vào thư mục AI` |
| Lỗi quota / thiếu quyền ghi | `Bật quyền ghi` · `Mở Settings AI` |

**Nguồn 2 — AI đề xuất qua tool mới `suggest_actions`** (mở rộng `suggest_view`): input là mảng ≤ 3 phần tử
`{ kind, keyword?, itemId?, step?, label ≤ 40 ký tự, why? }`, `kind` thuộc danh sách trắng:
`open_candidate · research_keyword · keep · drop · run_step · export_md · insert_prompt`.

- Server kiểm từng nút: ID thuộc phiên, bước đủ điều kiện, quyền ghi đang bật; sai thì bỏ nút đó + ghi lý do vào log, không lỗi cả lượt.
- Bấm nút **gọi đúng API nút tay đang dùng** (cùng số, cùng hoàn tác). Nút ghi dữ liệu (`research_keyword`, `keep`, `drop`)
  có xác nhận một dòng nếu quyền ghi tắt; `insert_prompt` chỉ đưa chữ vào ô, không tự gửi.
- Nút đã bấm đổi thành "✓ Đã làm · Hoàn tác"; nút hết hạn (ứng viên đã loại, bước đã qua) xám + lý do.

**Chip câu hỏi tiếp** (dưới câu trả lời cuối, ≤ 3 chip): lấy từ sổ lệnh 28.7 T3 theo bước hiện tại
(ví dụ "So sánh 3 ứng viên, bỏ cái yếu"), bấm = đưa vào ô chat.

**Không làm:** nút mở URL ngoài do AI đưa, nút chạy shell, nhiều nút xếp hàng tự chạy nối nhau.

**Tiêu chí kiểm được:** phiên thật 7 bước đi hết **chỉ bằng nút** (không gõ lệnh) trừ câu ý tưởng đầu; AI gửi `kind` lạ
hoặc ID phiên khác → không hiện nút; bấm Giữ từ chat cho cùng kết quả + hoàn tác như bấm tay; hai tab cùng phiên không chạy trùng.

**File đụng:** `mcp/write-tools.ts` (tool `suggest_actions`), `lib/hunt.ts` (log + kiểm), `lib/ai/ai-dir.ts` (playbook dạy
khi nào gọi), mới `lib/hunt-actions.ts` (nút code sinh), `HuntChat.tsx` / `ChatMessage.tsx`, `HuntPage.tsx` (thực thi), locale.

**Test:** mới `web/tests/hunt-actions.test.ts`: bảng nút theo trạng thái, danh sách trắng, ID lạ, hết hạn, hoàn tác;
bổ sung `hunt.test.ts` cho `suggest_actions`.

## T7 · Ô chat kiểu Wow Keywords — M

**Mục tiêu:** khung nhập gọn, đủ thứ hay dùng trong tầm tay, giống ảnh 3.

**Cần làm**

- Bố cục một khối bo góc: textarea (tự cao 2–8 dòng) ở trên; hàng dưới: **chip model ⌄** bên trái · nút **/** lệnh ·
  khoảng trống · **nút gửi tròn ✦** bên phải; đang chạy thì nút gửi thành **■ Dừng** (gọi `run.stop`).
- **Chip model:** liệt kê `MODELS` của tuyến đang bật (Settings), đổi ở đây = lưu Settings luôn (một nguồn sự thật).
  Cần `runChat()` nhận `model` và truyền `--model` cho Claude Code / Codex — nếu 28.7 T1 chưa làm thì làm phần truyền model
  ở đây, phần đọc model thật vẫn để 28.7. Đổi model giữa phiên → lượt sau dùng model mới, ghi một dòng hệ thống trong chat.
- **Placeholder** gợi ý theo bước hiện tại (ví dụ bước Spec: "Viết lại Spec, bỏ màn Settings… hoặc gõ /").
- Phím: Enter gửi, Shift+Enter xuống dòng, ↑ trong ô trống lấy lại câu trước, Esc đóng menu `/`. Gõ tiếng Việt (IME) không
  gửi nhầm khi đang ghép chữ (`isComposing`).
- Ô tick "So sánh tự động khi xong" chuyển vào menu ⋯ cạnh chip model (bớt rối).
- Bản nháp đang gõ giữ khi chuyển ứng viên / tải lại trang (localStorage theo phiên, bọc try/catch).

**Không làm:** nút mic, đính kèm file/ảnh, chọn nhiều model so song song.

**Tiêu chí kiểm được:** đổi model ở chip → lượt sau CLI chạy đúng `--model` (log server); Dừng giữa chừng không để CLI mồ côi;
IME tiếng Việt không gửi nhầm; khung 380px không tràn, chip model dài xuống dòng chứ không đè nút gửi.

**File đụng:** `HuntChat.tsx` (tách `ChatComposer.tsx` dùng chung với `ChatPanel.tsx`), `lib/ai/chat.ts` (`model` vào
`chatArgs`), `lib/ai/settings.ts`, `server/app.ts` (`/api/ai/chat` nhận model), locale.

**Test:** `ai-chat.test.ts`: argv có `--model` đúng tuyến, model rỗng = mặc định CLI; test composer phím/IME.

## Cách soát và bằng chứng hoàn tất khi triển khai

- Mỗi task có test hành vi trong `web/tests/`; `npm run check` ở gốc và `npm run docs:build` xanh.
- Chạy thật **một phiên săn từ ý tưởng tới bước 7** trên DB thật, đi bằng nút (T6), tải cả bộ .md (T2), mở 3 file đọc lại.
  Chụp và **mở đọc từng ảnh**: chat có bảng + code + nút, tab bản Spec, hộp gợi ý đóng/mở, chip model mở —
  ở **380px khung chat, 960px và 1340px**, cả **EN và VI**.
- App Mac: tải .md từ app Tauri, kiểm file ra đúng thư mục Downloads.
- Chưa đo thì ghi "chưa đo", không ghi thời gian hay tỷ lệ giả.

## Thứ tự làm đề xuất · độ lớn

1. **T4 — S/M:** component `Hint` / `InfoTip` trước, gỡ tường chữ ngay (kèm 28.8 B).
2. **T1 — S:** bước Plan + nới trần note — mở khoá cho T2/T3.
3. **T2 — M:** xuất .md — ra **output đếm được** sớm nhất (file đem đi build).
4. **T5 — M:** tách `ChatMessage`, format xịn.
5. **T7 — M:** `ChatComposer` + chip model.
6. **T3 — M:** tab bản.
7. **T6 — L:** nút hành động — cần T1/T2/T5 xong để có chỗ gắn nút.

S/M/L là độ lớn tương đối, **chưa đo thời gian**.

## Kết quả 2026-10-28

- **T4 + T1 + T2** (nhánh `phase28-9-ai-agent-pro`, merge main): `Hint` / ⓘ, bước 7 Plan, xuất Brief / Spec / Plan .md.
- **T5:** `ChatMessage.tsx` dùng chung Hỏi AI + AI Agent — dòng ✦ tên AI · giờ, tool gập 1 dòng, khối code có nhãn + Copy,
  mã nguồn thành chip (cả `[Research #n]`), dòng giây · token, thanh Copy · Tải .md · Hỏi lại. Chạy thật Claude Code: bảng 3 cột,
  checklist, khối bash, chip Project #4 hiện đúng ở khung 420px.
- **T7:** `ChatComposer.tsx` — chip model (đổi = lưu Cài đặt; Claude Code `--model`, Codex `-c model=`), nút gửi tròn ✦ ↔ ■ Dừng,
  ↑ lấy câu trước, IME không gửi nhầm, nháp localStorage, "Tự so" vào ⋯. Chạy thật: chọn haiku → sổ dùng AI ghi "Claude Code · haiku", trả lời 4 giây.
  Dòng báo đổi model hiện trên ô nhập (không chèn vào lịch sử chat).
- **T3:** tab bản cũ → mới, ★ Dùng bản này (dòng nhật ký `chọn bản`, không migration), xuất .md lấy bản ★, bản ★ bị hoàn tác → về bản mới nhất; + Viết lại điền lệnh vào chat.
- **T6:** `lib/hunt-actions.ts` — nút code sinh (Xem ứng viên · So sánh + giữ BEST · Mở niche đã giữ · Tải .md / cả bộ · Viết bước tiếp →)
  + tool `suggest_actions` (danh sách trắng 7 kind, ứng viên phải thuộc phiên, ≤ 3 nút, nút sai bị bỏ kèm lý do). Kiểm lại lúc bấm
  (đã loại / đã giữ / chưa có tài liệu). Chạy thật: AI gắn 2 nút, bấm "Open best niche" mở đúng ứng viên.
- **Chưa làm (để sau, ghi rõ):** chip câu hỏi tiếp (cần sổ lệnh 28.7 T3); "Hoàn tác" ngay trên nút đã bấm (giữ / loại bằng nút ghi là
  việc của người dùng, đổi lại ở chip ứng viên); đi hết 7 bước chỉ bằng nút trên phiên thật; tải .md trong app Mac Tauri — **chưa đo**.
- Kiểm: 493 test xanh, tsc + eslint sạch.

## Rủi ro

- **Trần 12 000 ký tự** làm gói ngữ cảnh lần sau phình: chỉ đưa bản ★ vào ngữ cảnh AI, bản cũ chỉ để xem/xuất.
- **AI lạm dụng `suggest_actions`** (nút mỗi câu): playbook giới hạn ≤ 3 nút, chỉ khi có việc tiếp rõ ràng; server cắt thừa.
- **Model đổi giữa phiên Claude Code resume** có thể bị CLI từ chối hoặc lờ đi: kiểm bằng fixture thật; không được thì
  đổi model = mở cuộc mới, báo rõ.
- **Nút trong chat lệch dữ liệu** khi người dùng đã thao tác tay: kiểm điều kiện lại lúc bấm, không lúc vẽ.
- **Gập nhầm thông tin quan trọng**: luật "không gập lỗi / cờ chặn / quyền" ghi trong `Hint.tsx` + kiểm khi review.

## Câu hỏi còn mở cho người dùng

- Plan nên chia theo **mốc** (bản chạy → paywall → store) như đề xuất, hay theo **tuần**? Mặc định theo mốc.
- Khi lưu vào thư mục AI, đường `briefs/<project>/` có hợp không, hay anh muốn ghi thẳng vào repo app
  (`apps/ACTIVE/<loại>/<slug>/context-ai/`)? Mặc định `briefs/` trong thư mục AI của Niche Radar.
- Chip model: chỉ model của tuyến đang bật, hay cho đổi luôn tuyến (Claude Code ↔ Codex) ngay ở chip? Mặc định chỉ model,
  đổi tuyến vẫn ở Settings.

[← Phase 28.8 · Trang niche + Explorer](phase-28-8-niche-ui-polish.md) · [Phase 28.10 · Bàn quyết định →](phase-28-10-decision-board-easy.md) · [Mục lục Web](index.md)
