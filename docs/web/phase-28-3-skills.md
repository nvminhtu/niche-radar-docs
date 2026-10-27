# Phase 28.3 · Bộ skill Shotmatic (plan riêng)

> **Trang giữ số.** Mỗi nút đũa phép ([Phase 28.4](phase-28-4-ai-magic.md)) và mỗi nhóm việc MCP
> ([Phase 28.2](phase-28-2-mcp-write.md)) chạy **một skill** — skill là *cách làm* của việc đó (các bước, giọng, cách
> trích nguồn). **Nội dung từng skill plan ở một lượt riêng.** Trang này chỉ ghi phase khác cần skill nào, nhận gì,
> trả gì — để 28.2, 28.4, 28.5 làm được trước mà không phải đoán.

<span class="chip chip--todo">Chưa plan · giữ số 2026-10-27</span>

<div class="box box--goal" markdown>
**Hiện có (Phase 27 · 26.2).** Thư mục AI có 2 skill tiếng Anh: `/app-demand` (niche này có đáng làm không → BUILD /
TEST MORE / DROP) và `/compare-niches` (niche nào làm trước). Chữ skill nằm trong code (`web/src/lib/ai/ai-dir.ts`),
mỗi lần mở ghi bản mới nếu file còn dòng `niche-radar:auto`.
</div>

## Một nguồn chữ, 3 lối ra

| AI | Skill vào bằng đường nào |
|---|---|
| **Claude Code** (mặc định khi máy có) | `.claude/skills/<tên>/SKILL.md` trong thư mục AI → `/<tên>` chạy ở nút 1 bấm, khung chat, terminal nhúng, Claude Code người dùng tự mở trong thư mục AI |
| **Claude Desktop · Cursor · Windsurf** (không đọc thư mục AI) | **MCP prompts** của niche-radar MCP — cùng chữ với SKILL.md |
| **Tuyến không có skill** (Gemini CLI, Claude API; Codex nếu Bước 0 đo ra không đọc) | app gửi kèm chữ skill trong prompt |

## Skill các phase khác cần (tên tạm)

| Skill | Ai gọi | Nhận | Trả | Đợt |
|---|---|---|---|---|
| `health-niche-check` | 28.4 khối Sức khoẻ niche · MCP | gói `health_niche_check` | giải thích + phản biện + nên đo thêm gì | 1 |
| `health-project-check` | 28.4 Tổng quan project · MCP | gói `health_project_check` | thiếu gì, mâu thuẫn, làm gì trước | 1 |
| `expand-niche` | 28.4 trang Explore | `expand_niche_pack` | cụm + tên cụm + 10 long-tail | 1 |
| `niche-summary` | 28.4 đầu trang Research | review + mô tả + What's New | khung 6 mục (thay việc `summary`) | 1 |
| `complaint-themes` | 28.4 Chủ đề than | review 1–3★ | chủ đề + câu nguyên văn (thay `themes`) | 1 |
| `feature-gap` | 28.4 Feature Gap | trang store top 5 | ô Có / Không / Không nói + câu nguồn | 1 |
| `presale-draft` | 28.4 Test bán trước · 28.5 Plan | evidence pack | nháp landing + bài đăng (thay `presale`) | 1 |
| `gap-ideas` | 28.4 trang Gap · tab Khoảng trống | cụm gap | 3–5 ý tưởng app | 1 |
| `decision-score` | 28.4 Bàn quyết định | keyword project + dẫn chứng | 5 trục + lý do | 1 |
| `project-brief` | 28.5 | `brief_pack` (+ bản cũ + câu yêu cầu sửa) | Brief + Spec + Plan theo mục | 1 |
| `suggest-seeds` · `collect-suggest` · `complaint-merge` · `customer-roles` · `money-model` · `revenue-match` · `gap-label` · `project-verdict` · `tracking-diff` | 28.4 đợt 2 | xem bản đồ 28.4 | xem bản đồ 28.4 | 2 |
| `app-demand` · `compare-niches` | đã có | — | đọc lại khi plan | — |

<div class="box box--rules" markdown>
**Luật cho mọi skill** (plan riêng giữ đúng thì 28.2 / 28.4 / 28.5 không vỡ)

- Tiếng Anh, tên kebab-case, **1 skill = 1 việc**
- **Khuôn JSON nằm trong code**, không trong SKILL.md → chạy bằng `--json-schema` / `--output-schema`; skill chỉ nói cách làm
- Skill **không tự ghi**: trả kết quả (nút 1 bấm) hoặc gọi `save_ai_result` / `propose_*` (AI bên ngoài)
- Mỗi skill có bài thử: 1 niche fixture + hàm kiểm của việc đó → test bằng `Ask` giả
- Có số version trong frontmatter; kết quả lưu kèm version skill để biết bản nào viết ra
</div>

<div class="box box--danger" markdown>
**Để plan riêng (chưa làm ở trang này)**

- Viết nội dung từng skill, ví dụ mẫu, giọng
- Skill có gửi kèm email dùng thử / bán riêng không
- Cho người dùng tự thêm skill của họ
</div>

[← Phase 28.2 · MCP đợt 2](phase-28-2-mcp-write.md) · [Phase 28.4 · Nút đũa phép →](phase-28-4-ai-magic.md)
