---
name: app-geo
description: "Skill phụ GEO + AEO cho Google (và AI search) — đo xem AI có nhắc / trích app mình không, rồi sửa đúng chỗ thiếu. Vòng: (1) viết 15–20 câu người mua hay hỏi cho từng app (questions.tsv) + regex tên app (brands.tsv); (2) đo bằng scripts/geo.py run — Gemini API + Google Search grounding (gần Google AI Overview nhất đo tự động được, cần GEMINI_API_KEY user tự tạo free), Codex (ChatGPT có web), Claude; (3) chấm bằng geo.py analyze: bao nhiêu câu nhắc tên app / trích domain mình, domain + trang nào AI đang trích cho từng câu 0 điểm; (4) audit kỹ thuật trang mình cho Google bằng geo.py audit (HTTP 200, redirect, noindex/nosnippet, canonical, JSON-LD SoftwareApplication/BlogPosting, ngày cập nhật, khối trả lời đầu trang, robots.txt cho Googlebot/Bingbot/OAI-SearchBot/ClaudeBot); (5) biến khoảng trống thành việc: trang 'best X', 'X alternative', 'do you need X', trang tính năng nói thẳng việc app làm — giao /oneclicktool-blog, /oneclicktool-landing, /app-reddit; (6) đo lại sau 2–4 tuần bằng geo.py compare so với mốc. Use when 'GEO', 'AEO', 'AI Overview', 'AI Overviews', 'AI Mode', 'Google AI có nhắc app không', 'ChatGPT có giới thiệu app mình không', 'AI search', 'được AI trích dẫn', 'LLM SEO', 'generative engine optimization', 'answer engine optimization', 'đo lại geo-test', 'audit trang cho Google', 'vì sao AI không nhắc app mình'. Không vượt CAPTCHA, không tạo tài khoản/key thay user, không bịa số."
argument-hint: "[slug | 'all'] [--remeasure <ngày mốc>] [--audit <url>…]"
user-invocable: true
---

# app-geo — để Google AI (và ChatGPT, Claude) nhắc tới app mình

Câu hỏi duy nhất: **khi người mua hỏi AI đúng việc app mình làm, AI có nhắc tên app / trích trang mình không — và nếu
không thì trang nào đang được trích thay?** Kết thúc bằng một con số `x / N` có ngày + danh sách trang phải có, không
dừng ở "đã phân tích".

Viết bài chuẩn AEO (short answer 40–60 từ, H2 dạng câu hỏi, FAQ, `evidence:`) **không** nằm ở đây — đó là `/oneclicktool-blog`.
Skill này lo phần còn lại: đo → audit → chọn trang cần viết → đo lại.

Mốc đầu tiên (2026-10-18, Sweepy + Markdown Everywhere + RAM Rescue): **0 / 40** —
[README-RESULT.md](../../../apps/ACTIVE/desk-apps/promo-desk/marketing/geo-test/2026-10-18/README-RESULT.md).

## Google nói gì (đọc trước, đừng làm theo tin đồn)

Nguồn: Google Search Central — *AI features and your website* + *Creating helpful, reliable, people-first content*
(developers.google.com/search). Nhắc lại ý chính; kiểm lại trang gốc nếu đã quá 6 tháng.

- **Không có markup / file riêng cho AI Overviews hay AI Mode.** Điều kiện = trang được index và được phép hiện snippet. Hết.
  → kiểm `noindex`, `nosnippet`, `max-snippet`, `data-nosnippet`, robots.txt, HTTP 200, canonical (geo.py audit làm).
- **`Google-Extended` không ảnh hưởng AI Overviews** — nó chỉ điều khiển việc dùng cho Gemini app / training. Chặn nó
  không làm mất khỏi Search; chặn `Googlebot` thì mất tất cả.
- `llms.txt` — Google không dùng. Có thì không hại, nhưng đừng coi là việc GEO cho Google.
- Structured data phải **khớp chữ hiển thị** trên trang. FAQ rich result chỉ còn cho site chính phủ/y tế, HowTo rich
  result đã bỏ — vẫn để FAQPage/HowTo JSON-LD được (AI đọc), nhưng không trông rich result.
- Lượt hiện / click từ AI Overviews **gộp chung** vào Search Console mục Web — không tách riêng được. Đo "AI có nhắc
  không" phải đo trực tiếp câu trả lời (Pha 2), không suy từ GSC.
- Nội dung sản xuất hàng loạt chỉ để xếp hạng = *scaled content abuse*. Mỗi trang phải có thứ AI không tự có (số đo thật,
  bảng tự làm, ảnh chụp app thật). Claude ở lần đo đầu **tự hạ điểm** bài "best X" tự khen không có bằng chứng.

## Luật cứng

- **Không vượt CAPTCHA, không tạo tài khoản, không đồng ý điều khoản thay user.** Google Search trong trình duyệt in-app
  bật CAPTCHA → dừng, dùng Gemini API. Perplexity / ChatGPT web đòi đăng nhập / điều khoản → bỏ, ghi `chưa đo`.
- `GEMINI_API_KEY`: **user tự tạo** ở https://aistudio.google.com/apikey (free tier) rồi `export` trong `~/.zshrc`. Claude
  không đọc, không in key. Thiếu key → `run` tự bỏ engine gemini và in `SKIP gemini · chưa đo`.
- Gemini Search grounding ≠ đúng y AI Overview (khác model, khác cách chọn nguồn) — ghi là **proxy** trong báo cáo.
- Không bịa số: mọi con số là `x / N` từ `geo.py analyze` + ngày đo + engine. Không có thì `chưa đo`.
- Câu hỏi viết **giọng người mua**, không chứa tên app mình (trừ nhóm `b*` hỏi đích danh — để riêng, không tính điểm).
- Đo lại phải dùng **đúng bộ câu cũ** (copy `questions.tsv` + `brands.tsv` của mốc) — đổi câu là mất so sánh.
- Site oneclicktool.app 100% tiếng Anh — câu hỏi + trang viết mới bằng tiếng Anh.

## Pha 1 — Bộ câu hỏi

Thư mục mỗi lần đo: `apps/ACTIVE/<slug>/marketing/geo-test/YYYY-MM-DD/` (nhiều app cùng lúc → để ở app đang chủ trì,
như lần đầu ở `promo-desk`). Trong đó:

```
questions.tsv   q01<TAB>sweepy<TAB>best duplicate file finder for Mac
brands.tsv      sweepy<TAB>\bsweepy\b          ← regex tên app theo nhóm
                *<TAB>oneclicktool|nvminhtu      ← domain/tài khoản của mình, tính cho mọi nhóm
```

Mỗi app 6–8 câu, phủ 4 kiểu (đúng các kiểu AI đang trích ở lần đầu):

| Kiểu | Ví dụ | Lấy từ đâu |
|---|---|---|
| best X | `best markdown viewer for Mac` | autocomplete (`~/.claude/skills/oneclicktool-blog/scripts/keywords.py`), Trends |
| X alternative / rẻ hơn / mua đứt | `Gemini 2 alternative one-time purchase` | đối thủ trong `research/`, `money.md` |
| việc cụ thể app làm | `app to find and kill forgotten localhost dev servers` | `spec.md`, landing |
| nỗi đau dạng hỏi | `how do I free up storage … is there an app` | review 1–3★, Reddit (`/app-reddit`) |

## Pha 2 — Đo

```bash
python3 scripts/geo.py run <dir>                       # mặc định gemini,codex,claude · 5 song song · chạy lại = hỏi tiếp câu thiếu
python3 scripts/geo.py run <dir> --engines codex,claude
```

20 câu × 2 engine ≈ 15 phút → chạy nền (`run_in_background`), không ngồi chờ. Câu trả lời gốc ở `<dir>/out/qNN.<engine>.md`.

## Pha 3 — Chấm

```bash
python3 scripts/geo.py analyze <dir>     # bảng nhóm × engine, top domain, mỗi câu 0 điểm → 4 URL AI đang trích · ghi result.json
```

Đọc tay thêm 3–5 câu trả lời: app nào được nhắc, AI nói **vì sao** chọn nó (thường là "trang chính chủ ghi rõ tính năng",
"có bảng so sánh", "giá mua đứt ghi rõ"), AI có nghi ngờ nguồn nào không.

## Pha 4 — Audit trang mình cho Google

```bash
python3 scripts/geo.py audit https://oneclicktool.app/macos/<app> https://oneclicktool.app/blog/<bài> …
```

Chạy cho: landing từng app, mọi bài blog dẫn về app đó, mọi link đang nằm ở GitHub README / Reddit / store listing.
`FAIL` sửa trước khi viết gì mới. Hay gặp: link cũ redirect (sửa nguồn trỏ thẳng URL cuối), trang app thiếu
`SoftwareApplication` + `offers.price`, không có ngày cập nhật, `<title>` chỉ có tên app mà không nói app làm gì.
Có khoá Search Console (`~/.config/gcp/oneclicktool-sa.json`) thì thêm `mcp__search-console__inspect_url_enhanced`
xem trang đã được index chưa — chưa index thì không AI Overview nào lấy được.

## Pha 5 — Khoảng trống → việc

Với mỗi câu 0 điểm, nhìn URL AI đang trích (output Pha 3) và chọn **1** trong 4 loại trang trên domain mình:

| AI đang trích | Mình cần | Giao cho |
|---|---|---|
| `…/blog/best-x`, `getmd.ma/guides/best-…` | bài "best X for Mac (tested)" có bảng tự đo, app mình là 1 dòng trung thực | `/oneclicktool-blog` |
| `…/x-alternative`, `alternativeto.net/…` | bài "X alternative" / trang `compare/<đối thủ>` | `/oneclicktool-blog` |
| trang tính năng của app indie (Ports, Portfox) | landing nói thẳng việc trong câu hỏi ở H1/H2 + đoạn đầu | `/oneclicktool-landing` |
| reddit / github / apps.apple.com | có mặt ở đó: README đúng link, trả lời Reddit thật, listing store | `/app-reddit`, `/app-listing`, `marketing-skills:directory-submissions` |

ChatGPT search dựa nhiều vào chỉ mục Bing → trang mới gửi Bing Webmaster / IndexNow (user tự đăng nhập Bing Webmaster).
Ghi việc vào `<dir>/README-RESULT.md` mục `## Việc` — mỗi dòng: câu `qNN` · loại trang · URL đích · skill · trạng thái.
Ngoài phạm vi → backlog của app, không làm lén.

## Pha 6 — Đo lại (2–4 tuần sau khi trang mới lên + đã index)

```bash
mkdir -p <app>/marketing/geo-test/<ngày mới> && cp <mốc>/{questions,brands}.tsv <app>/marketing/geo-test/<ngày mới>/
python3 scripts/geo.py run <ngày mới> && python3 scripts/geo.py compare <mốc> <ngày mới>
```

Bảng `compare` dán vào `README-RESULT.md` của lần mới. Tăng từ 0 → đó là bằng chứng bán Promo Desk hướng G
(memory `promo-desk-firebase-sync`). Không tăng sau 2 lần đo → xem lại loại trang ở Pha 5, không viết thêm cùng kiểu.

## `README-RESULT.md` — khung

```
# GEO test <app> · YYYY-MM-DD
## Engine đo được      bảng engine · cách · ✅/❌ (lý do) — ghi Gemini = proxy AI Overview
## Kết quả: x / N      bảng từ geo.py analyze (+ compare nếu là lần đo lại)
## Ai được nhắc và vì sao   domain/trang AI trích nhiều nhất, AI nói gì về nguồn
## Audit               FAIL/WARN từ geo.py audit, đã sửa chưa
## Việc                qNN · loại trang · URL · skill · trạng thái
```

## Sổ học

- 2026-10-18: Google Search in-app → CAPTCHA; Perplexity đòi đăng ký; ChatGPT web đòi đồng ý điều khoản; Gemini CLI bản
  free đã ngừng; Bing trả kết quả rác. Đo được: Codex + Claude CLI. Gemini API grounding thêm sau, cần key user tạo.
- App indie nhỏ vẫn được nhắc (MacMD Viewer, Portfox, Janus, MDHero) — nhờ bài "best X"/"X alternative" trên domain riêng.
- Hỏi đích danh tên app: ChatGPT tìm ra qua r/IMadeThis + GitHub README + link cũ hỏng → sửa link nguồn là việc rẻ nhất.
