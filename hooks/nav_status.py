"""Tô link sidebar theo trạng thái phase: xong → xanh, đang làm → vàng nhạt.

Trạng thái lấy từ chip đầu tiên của chính trang (<span class="chip chip--done">…) — không ghi tay ở chỗ khác.
MkDocs đọc markdown của mọi trang trước rồi mới render, nên lúc on_post_page đã có đủ bảng trạng thái.
"""
import posixpath
import re

CHIP = re.compile(r'class="chip chip--(done|doing|todo)"')
LINK = re.compile(r'<a href="([^"#:]*)" class="md-nav__link')
status_by_url: dict[str, str] = {}


def on_page_markdown(markdown, page, **_):
    m = CHIP.search(markdown)
    if m and page.file.src_uri.startswith("phase-"):  # chỉ trang phase; Master Plan có chip trong bảng lộ trình
        status_by_url[page.url] = m.group(1)
    return markdown


def on_post_page(output, page, **_):
    def repl(m):
        url = posixpath.normpath(posixpath.join(page.url or ".", m.group(1)))
        url = "" if url == "." else url.rstrip("/") + "/"
        status = status_by_url.get(url)
        return m.group(0) + (f" nr-nav--{status}" if status in ("done", "doing") else "")

    return LINK.sub(repl, output)
