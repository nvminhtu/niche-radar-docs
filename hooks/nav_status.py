"""Tô xanh link sidebar của phase đã xong.

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
    if m:
        status_by_url[page.url] = m.group(1)
    return markdown


def on_post_page(output, page, **_):
    def repl(m):
        url = posixpath.normpath(posixpath.join(page.url or ".", m.group(1)))
        url = "" if url == "." else url.rstrip("/") + "/"
        return m.group(0) + (" nr-nav--done" if status_by_url.get(url) == "done" else "")

    return LINK.sub(repl, output)
