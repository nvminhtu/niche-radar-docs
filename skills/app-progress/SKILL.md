---
name: app-progress
description: "Sinh lại và kiểm progress.json của repo App (bảng Relay đọc để biết app nào đang ở bước nào trong 15 bước). Dùng khi nói 'cập nhật tiến độ app', 'sinh lại progress.json', 'Relay không thấy app mới', 'bước app hiện sai', 'bảng listing app cũ rồi', 'check progress', hoặc sau khi chạy app.py status. Không sửa tay progress.json — sửa state.md rồi chạy lại script."
user-invocable: true
model: claude-sonnet-5-5
---

# app-progress — tiến độ repo App

**Một việc:** `progress.json` ở gốc repo luôn khớp với bảng STATUS trong `apps/ACTIVE/<slug>/context-ai/state.md`.

## Luật (chung cho mọi repo — skill `core:progress-file`)

1. **Không sửa tay `progress.json`.** Lần sinh sau ghi đè sạch. Số sai → sửa `apps/ACTIVE/<slug>/context-ai/state.md` (chạy `python3 scripts/app.py status <slug>` để nó tự cập nhật), hoặc sửa script sinh.
2. **`slug` là khoá ổn định.** Đổi slug = mất những gì đã bấm ✓ trong Relay (lưu ở `progress.overrides.json`).
3. **Không bịa.** Thiếu dữ liệu thì `phase: null` + nói lý do trong `step`.
4. `progress.overrides.json` là của Relay — đừng sửa, đừng xoá khi sinh lại `progress.json`.

## Làm

```bash
python3 scripts/app.py status <slug>   # cập nhật state.md của 1 app
python3 scripts/app_table.py           # ghi README-APP-LISTING.md + progress.json
python3 scripts/check_progress.py     # phải 0 lỗi
```

Rồi commit cả script lẫn `progress.json` (và `README-APP-LISTING.md`).

`README-APP-LISTING.md` theo RULE-04 (skill `core:repo-rules`): 1 bảng dưới `<!-- LISTING:TABLE -->`, cột
`STT | Tên | Slug | Nhóm | Vòng | Bước | Cập nhật | Stack | Nền tảng | Tiến độ | Tạo`. `Bước` = emoji + bước kế
(🟡 đang làm · 🔴 chờ CỔNG / Blocker · 🔵 chờ store · ⚪ live · ⏸️ BACKLOG) — không còn cột `Trạng thái`;
`Tiến độ` = số bước ok / 14. Kiểm: `python3 <core>/skills/repo-rules/scripts/check_listing.py .` → 0 lỗi.

## Field repo này ghi

| Field | Lấy từ đâu |
|---|---|
| `pipeline` | 15 bước cố định: setup → research → money → spec → design → mockup → scaffold → build → run → review → release → listing → publish → marketing → grow |
| `status` | `marketing.md` có `Launched: yes` → DONE · `publish.md` có store `review` → REVIEW · bước kế là app-publish → NEED_UPLOAD · còn lại ACTIVE/PENDING |
| `phase` / `phases` | số bước `ok` trong bảng STATUS / tổng số bước (15) |
| `blocker` | dòng `Blocker:` trong state.md, hoặc bước kế đang chờ CỔNG |
| `track` | luôn `pipeline` |

Chi tiết khuôn chung + ý nghĩa từng field: skill `core:progress-file`
(`ai-skills-shared/plugins/core/skills/progress-file/SKILL.md`).
