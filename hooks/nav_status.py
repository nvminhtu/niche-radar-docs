"""Tô link sidebar theo trạng thái phase: xong → xanh, đang làm → vàng nhạt, không làm → xám gạch ngang,
tạm dừng (chip "Tạm dừng …") → gạch ngang đỏ; trang không phải phase (research, hướng dẫn, plan) → đậm + nghiêng;
phase chỉ research (câu mở đầu "Phase **chỉ research") làm xong → xanh + đậm + nghiêng.
Phase Review (trang có khối class="nr-review-stop") → nhãn REVIEW ở sidebar + vạch REVIEW trên thẻ phase.

Trạng thái lấy từ chip đầu tiên của chính trang (<span class="chip chip--done">…) — không ghi tay ở chỗ khác.
MkDocs đọc markdown của mọi trang trước rồi mới render, nên lúc on_post_page đã có đủ bảng trạng thái.
"""
import posixpath
import re

CHIP = re.compile(r'class="chip chip--(done|doing|todo|skip)">(Tạm dừng)?')
LINK = re.compile(r'<a href="([^"#:]*)" class="md-nav__link')
RESEARCH = re.compile(r'Phase \*\*chỉ research')
REVIEW = re.compile(r'class="nr-review-stop"')
STEP = re.compile(r'<div class="step">((?:(?!<div class="step">).)*?<a class="go" href="([^"#:]+)")', re.S)
# mục nav có chữ "KO LÀM" = vạch chặn: mọi mục dưới nó không làm (chốt 2026-10-26)
SKIPLINE = re.compile(r'(<(?:label|span|a)[^>]*class="md-nav__link)("[^>]*>\s*(?:<span class="md-ellipsis">\s*)?[^<]*KO LÀM)')
status_by_url: dict[str, str] = {}
review_urls: set[str] = set()
doc_urls: set[str] = set()  # trang tài liệu/research (không phải phase-*) → đậm + nghiêng ở sidebar


def _abs(page, href):
    url = posixpath.normpath(posixpath.join(page.url or ".", href))
    return "" if url == "." else url.rstrip("/") + "/"


def on_page_markdown(markdown, page, **_):
    m = CHIP.search(markdown)
    is_phase = posixpath.basename(page.file.src_uri).startswith("phase-")
    if m and is_phase:  # chỉ trang phase (web/, app/); trang mục lục có chip trong bảng
        status_by_url[page.url] = "pause" if m.group(2) else m.group(1)  # chip "Tạm dừng …" → gạch ngang
        if m.group(1) == "done" and RESEARCH.search(markdown):
            doc_urls.add(page.url)  # phase research đã xong → đậm + nghiêng
    if not is_phase and posixpath.basename(page.file.src_uri) != "index.md":
        doc_urls.add(page.url)
    if REVIEW.search(markdown) and posixpath.basename(page.file.src_uri).startswith("phase-"):
        review_urls.add(page.url)
    return markdown


def on_post_page(output, page, **_):
    def repl(m):
        url = _abs(page, m.group(1))
        status = status_by_url.get(url)
        return (m.group(0) + (f" nr-nav--{status}" if status in ("done", "doing", "skip", "pause") else "")
                + (" nr-nav--doc" if url in doc_urls else "")
                + (" nr-nav--review" if url in review_urls else ""))

    def step(m):
        review = _abs(page, m.group(2)) in review_urls
        return ('<div class="step step--review">' if review else '<div class="step">') + m.group(1)

    output = SKIPLINE.sub(lambda m: m.group(1) + " nr-nav--skipline" + m.group(2), output)
    return STEP.sub(step, LINK.sub(repl, output))
