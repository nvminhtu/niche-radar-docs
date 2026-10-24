# Niche Radar Docs — tài liệu Niche Radar + bộ skill App AI Skills

Đọc online: **https://nvminhtu.github.io/niche-radar-docs/**

Niche Radar: gõ một niche → biết keyword nào còn trống, đối thủ yếu ở đâu, nhu cầu lên hay xuống
(Google Play, App Store, Google Trends, Reddit). Code của tool nằm ở repo riêng (private); repo này chỉ chứa:

- `docs/` + `mkdocs.yml` — master plan, lộ trình Version 1–4, cách hệ thống chạy, cách dùng.
- `skills/` — 36 skill Claude Code của pipeline App AI Skills (research → spec → design → build → store → marketing).
  Danh sách + mô tả: trang [Skills](https://nvminhtu.github.io/niche-radar-docs/skills/).

## Dùng skill

Chép thư mục skill cần dùng vào `~/.claude/skills/`, ví dụ:

```bash
cp -r skills/app-demand ~/.claude/skills/
```

Nhiều skill gọi script `scripts/*.py` của repo pipeline (chưa public); phương pháp trong `SKILL.md` + `references/`
vẫn áp dụng được.

## Cập nhật (người giữ repo)

Không sửa tay `docs/` hay `skills/` ở đây — nguồn thật nằm ở repo code Niche Radar và repo App AI Skills.

```bash
python3 scripts/sync.py
```

Script chép lại cả hai, xoá đường dẫn máy riêng, sinh `docs/skills.md`. Commit + push lên `main` là GitHub Actions
tự build trang. Xem thử ở máy: `pip install -r requirements-docs.txt && mkdocs serve`.
