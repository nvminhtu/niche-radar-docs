#!/usr/bin/env python3
"""Chép tài liệu Niche Radar + skills của App-AI-Skills vào repo public này.

Nguồn (máy anh Tu, mặc định đứng cạnh repo này):
  ../niche-radar                          → docs/, hooks/, mkdocs.yml, requirements-docs.txt
  ../../App-AI-Skills/app-AI-skills/.claude/skills → skills/

Chạy: python3 scripts/sync.py [--docs <dir>] [--skills <dir>]
Rồi: git add -A && git commit && git push — GitHub Actions tự build trang docs.
"""
import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/nvminhtu/niche-radar-docs"
SITE_URL = "https://nvminhtu.github.io/niche-radar-docs/"

# Đường dẫn máy riêng không được lên public
SCRUB = [
    (re.compile(r"/Users/[^/\s]+/DATA/PROJECTS/OTHERS/CLAUDE_SKILL/Niche-Research/niche-radar"), "niche-radar"),
    (re.compile(r"/Users/[^/\s]+/DATA/PROJECTS/OTHERS/CLAUDE_SKILL/Niche-Research"), "Niche-Research"),
    (re.compile(r"/Users/[^/\s]+/"), "~/"),
    (re.compile(r"research/\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.md"), "research/<ngày>-<chủ-đề>.md"),
]
# Tên app chưa ra mắt: mỗi dòng một slug trong scripts/private-words.txt (gitignore, chỉ có ở máy)
_private = Path(__file__).with_name("private-words.txt")
if _private.exists():
    for w in _private.read_text(encoding="utf-8").split():
        SCRUB.append((re.compile(rf"\b{re.escape(w)}\b"), "<slug>"))
TEXT_EXT = {".md", ".yml", ".yaml", ".txt", ".py", ".sh", ".json", ".css", ".html", ".ts", ".dart", ".swift", ".kt"}


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".DS_Store", "__pycache__"))
    for f in dst.rglob("*"):
        if f.is_file() and f.suffix in TEXT_EXT:
            scrub(f)


def scrub(f: Path) -> None:
    text = f.read_text(encoding="utf-8")
    new = text
    for pat, rep in SCRUB:
        new = pat.sub(rep, new)
    if new != text:
        f.write_text(new, encoding="utf-8")


def skill_desc(skill_md: Path) -> str:
    m = re.search(r"^description:\s*(.+)$", skill_md.read_text(encoding="utf-8"), re.M)
    if not m:
        return ""
    d = m.group(1).strip().strip("\"'")
    first = re.split(r"(?<=[.!?])\s|\s—\s", d, maxsplit=1)[0]
    return first if len(first) <= 220 else first[:217].rstrip() + "…"


def write_skills_page(skills_dir: Path) -> int:
    names = sorted(p.name for p in skills_dir.iterdir() if (p / "SKILL.md").exists())
    lines = [
        "# Skills (App AI Skills)",
        "",
        "Bộ skill Claude Code của pipeline **App AI Skills** — làm app bán subscription từ ý tưởng tới store.",
        "Niche Radar là tool research đứng đầu pipeline (`app-research`, `app-demand`, `best-app`).",
        "",
        "Cài: chép thư mục skill cần dùng vào `~/.claude/skills/` (hoặc `.claude/skills/` của repo).",
        "Nhiều skill gọi script `scripts/*.py` của repo pipeline (chưa public) — phần phương pháp trong `SKILL.md`",
        "và `references/` vẫn đọc và áp dụng được.",
        "",
    ]
    for n in names:
        lines.append(f"- **[{n}]({REPO_URL}/tree/main/skills/{n})** — {skill_desc(skills_dir / n / 'SKILL.md')}")
    (ROOT / "docs" / "skills.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(names)


def patch_mkdocs() -> None:
    f = ROOT / "mkdocs.yml"
    text = f.read_text(encoding="utf-8")
    text = text.replace("site_name: niche-radar", "site_name: Niche Radar", 1)
    if "site_url:" not in text:
        text = text.replace("docs_dir: docs", f"site_url: {SITE_URL}\nrepo_url: {REPO_URL}\ndocs_dir: docs", 1)
    if "Skills: skills.md" not in text:
        text = text.replace("  - Cách dùng: cach-dung.md\n", "  - Cách dùng: cach-dung.md\n  - Skills: skills.md\n", 1)
    f.write_text(text, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", default=str(ROOT.parent / "niche-radar"))
    ap.add_argument("--skills", default=str(ROOT.parent.parent / "App-AI-Skills/app-AI-skills/.claude/skills"))
    a = ap.parse_args()
    docs_src, skills_src = Path(a.docs), Path(a.skills)

    copy_tree(docs_src / "docs", ROOT / "docs")
    copy_tree(docs_src / "hooks", ROOT / "hooks")
    for name in ("mkdocs.yml", "requirements-docs.txt"):
        shutil.copy2(docs_src / name, ROOT / name)
    patch_mkdocs()
    copy_tree(skills_src, ROOT / "skills")
    n = write_skills_page(ROOT / "skills")
    print(f"docs ← {docs_src}\nskills ← {skills_src} ({n} skill)")


if __name__ == "__main__":
    main()
