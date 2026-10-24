---
hide:
  - navigation
  - toc
---

# niche-radar — Master Plan

> Gõ một niche → biết **keyword nào còn trống**, **đối thủ yếu ở đâu**, **nhu cầu lên hay xuống**.

Tool nội bộ để chọn niche cho app của mình. Tra Google Play, App Store, Google Trends, TrustMRR — Phase 1–5 không cần AI, không tốn phí; AI vào ở Phase 4 (tuỳ chọn) và Phase 6.

<div class="nr-stats" markdown>
<div><b>100</b><span>keyword mỗi lần explore</span></div>
<div><b>~6 phút</b><span>cho 100 keyword đủ số liệu</span></div>
<div><b>3</b><span>nguồn: Play · App Store · Trends</span></div>
<div><b>0 đ</b><span>Phase 1–5: không AI, không API trả phí</span></div>
</div>

## Có 2 dạng: Web và App

<div class="nr-forms" markdown>
<div class="nr-web" markdown>
### :material-web: Web — làm trước

- Chạy trên máy: `npm run dev` → mở `localhost:3200`
- Làm Phase 1 → 7 ở đây
- <span class="chip chip--doing">Đang làm</span>
</div>
<div class="nr-app" markdown>
### :material-apple: App Mac — Phase 8

- Double-click là mở, không cần gõ lệnh
- **Bọc lại đúng giao diện Web** bằng Tauri → không viết 2 lần
- <span class="chip chip--todo">Phase 8 · macOS trước</span>
</div>
</div>

## Chạy thế nào

```mermaid
flowchart LR
  U([Bạn gõ niche]) --> UI[Web / App Mac<br/>giao diện]
  UI --> API[Máy chủ nhỏ<br/>chạy trong máy]
  API --> P[Google Play]
  API --> S[App Store]
  API --> G[Google gợi ý]
  API --> T[Google Trends]
  P & S & G & T --> DB[(Lưu lại<br/>SQLite)]
  DB --> R[Cây keyword · Bản đồ ngách<br/>Top cơ hội · CSV]
```

Mọi thứ chạy trong máy bạn. Tra lại cùng niche trong 24 giờ lấy từ bộ nhớ, không gọi lại.
Chi tiết: [Hệ thống chạy thế nào](he-thong.md).

## Lộ trình MVP · Phase 1–11

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">1</span>
<div class="step__body">
<h3>Google Play <span class="chip chip--done">Xong · có UI Loading + Flow niche</span></h3>
<p>Mở niche thành cây keyword, chấm điểm cơ hội, bản đồ ngách, đối thủ bị chê gì.</p>
<a class="go" href="phase-1-google-play/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">2</span>
<div class="step__body">
<h3>App Store <span class="chip chip--done">Xong</span></h3>
<p>Keyword + đối thủ iOS, review 1–2★ iOS, giá / gói mua trong app, khoảng trống Play ↔ iOS.</p>
<a class="go" href="phase-2-app-store/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">3</span>
<div class="step__body">
<h3>Google Trends <span class="chip chip--done">Xong</span></h3>
<p>Nhu cầu lên hay xuống, so 5 keyword, theo nước, mùa vụ 5 năm.</p>
<a class="go" href="phase-3-google-trends/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">4</span>
<div class="step__body">
<h3>Feature Gap Matrix <span class="chip chip--done">Xong · tuyến A chờ key</span></h3>
<p>Bảng tính năng × top 5 app, mỗi ô có câu nguồn — tìm chỗ đối thủ còn thiếu.</p>
<a class="go" href="phase-4-feature-gap/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">5</span>
<div class="step__body">
<h3>Verified Sites <span class="chip chip--doing">Đang làm · TrustMRR bản đầu</span></h3>
<p>Doanh thu thật từ TrustMRR và các trang tương tự — ai đang thu tiền trong ngách.</p>
<a class="go" href="phase-5-verified/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">6</span>
<div class="step__body">
<h3>Tích hợp AI (bản Web) <span class="chip chip--todo">Chưa làm · có phần thử</span></h3>
<p>API key, extension miễn phí, AI chạy trong trình duyệt / trên máy — thử từng đường rồi chọn.</p>
<a class="go" href="phase-6-ai-web/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">7</span>
<div class="step__body">
<h3>Review + Validate <span class="chip chip--todo">Chưa làm</span></h3>
<p>Soát lại Phase 1–6 trên 5 niche thật, chấm điểm v2, evidence pack, test bán trước.</p>
<a class="go" href="phase-7-review-validate/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">8</span>
<div class="step__body">
<h3>Local App <span class="chip chip--todo">Spec đã duyệt</span></h3>
<p>Đóng gói Phase 1–6 thành app Mac (Tauri + Rust), project, xuất / nhập giữa các máy.</p>
<a class="go" href="phase-8-local-app/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">9</span>
<div class="step__body">
<h3>Small Features Update <span class="chip chip--todo">Chưa làm</span></h3>
<p>Các tính năng nhỏ lượm được khi dùng thật, mỗi cái một plan ngắn.</p>
<a class="go" href="phase-9-small-features/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">10</span>
<div class="step__body">
<h3>UI / UX Improvement <span class="chip chip--todo">Chưa làm</span></h3>
<p>Sửa chỗ vướng thật: luồng chính, trạng thái tải / lỗi, bảng dày, sáng / tối.</p>
<a class="go" href="phase-10-ui-ux/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">11</span>
<div class="step__body">
<h3>Account + Flow người dùng <span class="chip chip--todo">Chưa làm</span></h3>
<p>Tài khoản, luồng người dùng mới, nút góp ý → nhận tính năng mới.</p>
<a class="go" href="phase-11-account/">Xem chi tiết →</a>
</div>
</div>
</div>

<hr class="nr-mvp-line">

## Version 2 · sau MVP: nguồn mới + AI (Phase 12–17)

Phase 1–11 là **MVP**. Từ đây thêm nguồn YouTube, Amazon, Google Maps — mỗi nguồn một phase **cào số (không AI)**
rồi một phase **AI đọc chữ**. Vẫn **làm bản Web trước**, xong vài phase mới gói một lần vào app Mac (Phase 17).

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">12</span>
<div class="step__body">
<h3>YouTube Search <span class="chip chip--todo">Chưa làm</span></h3>
<p>Cào gợi ý YouTube + top video mỗi keyword: view, độ mới, kênh nhỏ thắng kênh to — không AI. Tuỳ chọn: MCP bên thứ 3 (vidIQ…) cho lượt tìm + độ cạnh tranh.</p>
<a class="go" href="phase-12-youtube-search/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">13</span>
<div class="step__body">
<h3>YouTube Research (AI) <span class="chip chip--todo">Chưa làm</span></h3>
<p>AI đọc phụ đề + comment: người xem than gì, xin gì, dùng tool nào — trích dẫn kèm mốc giây.</p>
<a class="go" href="phase-13-youtube-ai/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">14</span>
<div class="step__body">
<h3>Amazon Search <span class="chip chip--todo">Chưa làm</span></h3>
<p>Cào gợi ý Amazon + top sản phẩm: giá, sao, số review, BSR — không AI, gọi rất thưa.</p>
<a class="go" href="phase-14-amazon-search/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">15</span>
<div class="step__body">
<h3>Amazon Research (AI) <span class="chip chip--todo">Chưa làm</span></h3>
<p>Claude in Chrome đọc review 1–3★: người mua chê gì, ước gì, chỗ một app làm tốt hơn.</p>
<a class="go" href="phase-15-amazon-ai/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">16</span>
<div class="step__body">
<h3>Google Maps Research (AI) <span class="chip chip--todo">Chưa làm</span></h3>
<p>Đếm cửa hàng theo loại × thành phố, AI đọc review → việc chủ quán đang làm tay, app làm thay được.</p>
<a class="go" href="phase-16-google-maps/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">17</span>
<div class="step__body">
<h3>Local App 2.0 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gói Phase 12–16 vào app Mac một lần, migration DB không mất dữ liệu, .dmg mới.</p>
<a class="go" href="phase-17-local-app-2/">Xem chi tiết →</a>
</div>
</div>
</div>

## Version 3 · So sánh + AI Cite (Phase 18–22)

Chọn giữa nhiều niche / đối thủ trên một màn, hỏi dữ liệu bằng lời — AI chỉ trả lời từ DB, **mọi câu có trích dẫn và
máy tự kiểm**. Chi tiết: [Tổng quan Version 3](version-3.md).

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">18</span>
<div class="step__body">
<h3>So sánh niche <span class="chip chip--todo">Chưa làm</span></h3>
<p>2–4 niche cạnh nhau: cơ hội, đối thủ, xu hướng, đau, tiền — tô ô thắng từng hàng, không AI.</p>
<a class="go" href="phase-18-compare-niche/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">19</span>
<div class="step__body">
<h3>So sánh đối thủ <span class="chip chip--todo">Chưa làm</span></h3>
<p>2–5 đối thủ cạnh nhau: giá, sao, tính năng, bị chê gì, chỗ trống chưa ai làm tốt — không AI.</p>
<a class="go" href="phase-19-compare-competitor/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">20</span>
<div class="step__body">
<h3>Hỏi dữ liệu (AI Cite) <span class="chip chip--todo">Chưa làm</span></h3>
<p>Hỏi bằng lời, AI trả lời chỉ từ DB, mọi câu có trích dẫn — máy tự kiểm từng trích dẫn.</p>
<a class="go" href="phase-20-ai-cite-ask/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">21</span>
<div class="step__body">
<h3>Báo cáo so sánh (AI Cite) <span class="chip chip--todo">Chưa làm</span></h3>
<p>AI viết kết luận cho bảng so sánh, còn cờ đỏ thì không xuất; ra evidence pack cho /app-research.</p>
<a class="go" href="phase-21-ai-cite-report/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">22</span>
<div class="step__body">
<h3>Review + Local App 3.0 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Chọn niche thật 3 lần (≤ 30 phút/lần), sửa lỗi, gói vào app Mac 3.0.</p>
<a class="go" href="phase-22-local-app-3/">Xem chi tiết →</a>
</div>
</div>
</div>

## Version 4 · LLM + AEO, GEO, SEO (Phase 23–27)

Người dùng ngày càng hỏi Google và AI thay vì lên store. Thêm **kệ Google** (ai đứng top 10) và **kệ AI** (ChatGPT /
Gemini / Claude gợi ý app nào, trích trang nào) vào lúc chọn niche. Chi tiết: [Tổng quan Version 4](version-4.md).

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">23</span>
<div class="step__body">
<h3>Kệ Google (SEO) <span class="chip chip--todo">Chưa làm</span></h3>
<p>Top 10 Google của keyword chính, loại trang đứng top (forum, blog nhỏ = dễ chen), bộ câu hỏi người dùng — không AI.</p>
<a class="go" href="phase-23-seo-shelf/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">24</span>
<div class="step__body">
<h3>Kệ AI (GEO / AEO) <span class="chip chip--todo">Chưa làm</span></h3>
<p>Hỏi Gemini · ChatGPT · Claude như người dùng, đếm app được nhắc và trang được trích bằng regex.</p>
<a class="go" href="phase-24-ai-shelf/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">25</span>
<div class="step__body">
<h3>Chỗ trống AI + SEO <span class="chip chip--todo">Chưa làm</span></h3>
<p>Điểm kệ yếu theo công thức cố định, thêm cột Kệ Google + Kệ AI vào so sánh niche.</p>
<a class="go" href="phase-25-ai-seo-gap/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">26</span>
<div class="step__body">
<h3>Gói GEO + trang cần viết <span class="chip chip--todo">Chưa làm</span></h3>
<p>Xuất questions.tsv + brands.tsv cho geo.py và danh sách trang cần viết — cầu nối sang ra mắt.</p>
<a class="go" href="phase-26-geo-pack/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">27</span>
<div class="step__body">
<h3>Review + Local App 4.0 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Chọn niche thật 3 lần có kệ Google + kệ AI, gói vào app Mac 4.0.</p>
<a class="go" href="phase-27-local-app-4/">Xem chi tiết →</a>
</div>
</div>
</div>

## Version 5–12 · Từ tool riêng thành sản phẩm bán được

Mỗi version một trang tổng quan, các phase nằm trong trang đó. Thứ tự: nhanh → test → CI/CD → bảo mật → tài khoản
mạng → bán → marketing → tính năng mới.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">V5</span>
<div class="step__body">
<h3>Performance <span class="chip chip--todo">Phase 28–31</span></h3>
<p>Nhanh và nhẹ: đo mốc trước, kết quả đầu ≤ 30 giây, collector song song giữ giới hạn từng nguồn, bảng lớn mượt, app Mac mở ≤ 3 giây.</p>
<a class="go" href="version-5/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">V6</span>
<div class="step__body">
<h3>Automation Test + Review Results <span class="chip chip--todo">Phase 32–35</span></h3>
<p>Test chạy không cần mạng (fixture), E2E Playwright, canary nguồn thật hằng ngày, bộ niche chuẩn + phiếu review kết quả.</p>
<a class="go" href="version-6/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">V7</span>
<div class="step__body">
<h3>CI/CD <span class="chip chip--todo">Phase 36–39</span></h3>
<p>GitHub Actions chặn PR đỏ, build + ký + notarize app Mac trên CI, tag là ra bản, app tự cập nhật.</p>
<a class="go" href="version-7/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">V8</span>
<div class="step__body">
<h3>Security & Account & Refactor Code <span class="chip chip--todo">Phase 40–43</span></h3>
<p>Vá bảo mật API cục bộ / key / XSS, lớp tài khoản trên máy (xuất / xoá dữ liệu), khuôn collector chung — hành vi không đổi.</p>
<a class="go" href="version-8/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">V9</span>
<div class="step__body">
<h3>Firebase, Analytics, Account <span class="chip chip--todo">Phase 44–47</span></h3>
<p>Đăng nhập Firebase, sync project (dữ liệu cào thô ở lại máy), phễu GA4 có hỏi đồng ý, xoá tài khoản.</p>
<a class="go" href="version-9/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">V10</span>
<div class="step__body">
<h3>Sell Pro — Lifetime / Subscriptions <span class="chip chip--todo">Phase 48–51</span></h3>
<p>money.md bằng số đo, Lemon Squeezy + webhook → quyền Pro, paywall + dùng thử, chi phí AI theo gói (BYOK / lượt).</p>
<a class="go" href="version-10/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">V11</span>
<div class="step__body">
<h3>Marketing Plan <span class="chip chip--todo">Phase 52–55</span></h3>
<p>Định vị + landing + email, 2 kênh chọn bằng ICE, dogfood báo cáo niche công khai, lịch 6 tuần + luật dừng.</p>
<a class="go" href="version-11/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">V12</span>
<div class="step__body">
<h3>New Features — Just Planned <span class="chip chip--todo">chưa đánh số</span></h3>
<p>Danh sách ứng viên + cách chấm điểm; chọn ≤ 3 mỗi đợt, anh duyệt mới tách thành phase.</p>
<a class="go" href="version-12/">Xem chi tiết →</a>
</div>
</div>
</div>

Việc chưa xếp phase hoặc không làm: [Appendix](appendix.md). Mỗi phase đi theo [Quy trình build](quy-trinh-build.md).

## Trông như thế này

<figure class="frame" markdown>
![Bảng keyword của niche budget tracker](images/explore-table.jpg)
</figure>

<div class="box box--danger" markdown>
**Không làm (cố ý)**

- AI tự đưa ra con số — AI (Phase 4, 6) chỉ đọc chữ và trích dẫn
- Lượt tìm "thật" — store không công khai, "phổ biến" là ước lượng
- Bán / host cho nhiều người — tool nội bộ
</div>

[Bản Master Plan đầy đủ (chữ)](superpowers/specs/2026-10-24-niche-radar-master-plan.md)
