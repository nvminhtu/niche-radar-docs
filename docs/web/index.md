# WEB · Plan 2 — việc đang làm

> **Plan 2 mở 2026-11-07, đánh số lại từ 1.** Plan 1 (Phase 1–55) đã xong phần chính → tab
> [Plan 1](plan-1/index.md). Việc còn dở của Plan 1 chuyển sang đây thành mục 1, 3, 4, 5 (trang cũ giữ nguyên, chỉ đổi số);
> plan mới nối tiếp số sau. Phase chưa bắt đầu vẫn ở tab BACKLOG.
>
> Mọi tính năng vẫn làm và **test** ở **bản Web chạy local** (`web/`, `npm run dev` → `localhost:3200`); app Mac +
> Windows bọc đúng giao diện này: [App Mac + Windows](../app/index.md).

<span class="chip chip--doing">Plan 2 · 6 mục · mở 2026-11-07</span>

<div class="box box--goal" markdown>
**Thứ tự ưu tiên**

- **Từ 2026-11-07 không thêm tính năng mới, dồn sức cho bán hàng** ([Marketing](../marketing/index.md)). Mục 1, 2, 5 kéo
  người tới và khép cửa bán, làm trước.
- **Mục 3 và 4 chỉ làm cho xong phần đã code dở** (đo thật, sửa lỗi, commit). Không mở thêm bước mới.
- **Thêm plan mới:** đặt số tiếp theo (6, 7…) ở cuối trang, mục con đánh 6.1, 6.2… Mỗi mục đi theo
  [Quy trình build](../quy-trinh-build.md), máy mới thì xem [Setup máy](../setup.md).
- **Từ 2026-11-16 gom về launch app:** mọi mục về app được gom ở [Launch · Phân tích thị trường app](launch-app-market.md)
  (7 câu khách cần trả lời, trạng thái, chỗ chưa đủ sâu, bước 0 đào sâu trước brief → spec → plan).
</div>

## 1 · Extension Chrome — 3 extension miễn phí

Mỗi extension là một cửa vào shotmatic.app từ Chrome Web Store. Code bản 0.1.0 đã chạy; phần còn lại chủ yếu là đưa lên
store (anh tự bấm Submit, đồ nằm sẵn trong `STORE-LISTING.md`) và gắn link store lên landing.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">1.1</span>
<div class="step__body">
<h3>ShotMatic Lite — Play + App Store <span class="chip chip--doing">0.1.0 xong 2026-11-01 · chờ tải lên Chrome Web Store</span></h3>
<p>Kiểm nhanh keyword + niche ngay trên trang app của Google Play / App Store, rồi kéo người dùng về shotmatic.app. Trang cũ: Backlog 26.</p>
<a class="go" href="phase-backlog-26-chrome-extension-lite/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">1.2</span>
<div class="step__body">
<h3>YouTube + skill lái Chrome <span class="chip chip--doing">Bước 0 đo xong · còn vidIQ + Claude in Chrome thật</span></h3>
<p>Claude Code lái Chrome bằng skill cho YouTube và trang store, ghép MCP vidIQ, dùng repo có sẵn cho nhanh. Trang cũ: Backlog 27.</p>
<a class="go" href="phase-backlog-27-youtube-chrome-skill/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">1.3</span>
<div class="step__body">
<h3>ShotMatic Scout — Amazon <span class="chip chip--doing">0.1.0 xong 2026-11-02 · chờ ảnh store + tải lên</span></h3>
<p>Keyword dài từ ô tìm kiếm Amazon, chấm độ cạnh tranh trên trang kết quả, BSR trên trang sản phẩm. Miễn phí hết. Trang cũ: Backlog 28.</p>
<a class="go" href="phase-backlog-28-chrome-extension-amazon/">Xem chi tiết →</a>
</div>
</div>
</div>

## 2 · Landing page · Guide · Free tool

Người lạ vào shotmatic.app phải hiểu ngay ShotMatic làm gì, thấy kết quả thật, rồi bấm tải. Học cách AppKittie (đối thủ
đang được ChatGPT gợi ý) bày landing và trang free tool.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">2</span>
<div class="step__body">
<h3>Plan tối ưu Landing, Guide, Free tool <span class="chip chip--todo">Plan 2026-11-07 · chờ anh duyệt</span></h3>
<p>Landing: hook theo kết quả + thẻ niche có số thật ở màn đầu. Guide: ảnh app thật + nút tải cuối bài. Free tool: trang /tools gom tool, App Idea Checker là tool đầu.</p>
<a class="go" href="phase-plan2-02-landing-guide-free-tool/">Xem chi tiết →</a>
</div>
</div>
</div>

## 3 · AI Agent + giao diện — phần còn dở

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">3.1</span>
<div class="step__body">
<h3>AI Agent — Đã có app / web <span class="chip chip--doing">M1 code xong 2026-10-31 · chưa chạy AI thật · M2–M4 chưa làm</span></h3>
<p>Người đã có app hoặc web đưa context vào, xác nhận Hồ sơ app, rồi chọn Đánh giá app hiện tại hoặc Mở rộng tìm niche. Trang cũ: Phase 28.18.</p>
<a class="go" href="phase-28-18-ai-agent-da-co-app/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">3.2</span>
<div class="step__body">
<h3>Giao diện mới: sidebar · màu · bớt chữ <span class="chip chip--doing">M1 + M2 xong · M3 còn 3 trang chưa đạt</span></h3>
<p>Sidebar trái 4 nhóm, bảng màu đã chọn, chữ sàn 14px, mỗi trang bớt chữ. Còn 3 trang chưa đạt mục tiêu số chữ. Trang cũ: Phase 28.21.</p>
<a class="go" href="phase-28-21-sidebar-mau-bot-chu/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">3.3</span>
<div class="step__body">
<h3>Phiên AI Agent: kết quả lên đầu <span class="chip chip--todo">M1–M4 code xong 2026-11-05 · chưa chạy thật nút Fill</span></h3>
<p>AI đề xuất gì nằm trên cùng với 1 nút duyệt, 5 nút lấy số lẻ gom thành "Fill missing factors". Trang cũ: Phase 28.22.</p>
<a class="go" href="phase-28-22-hunt-ket-qua-truoc/">Xem chi tiết →</a>
</div>
</div>
</div>

## 4 · Demo + YouTube · Amazon · Maps — phần còn dở

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">4.1</span>
<div class="step__body">
<h3>Demo Site — show hàng <span class="chip chip--doing">Code đã có · soát lại 2026-11-02</span></h3>
<p>UI thật trên dữ liệu chụp sẵn, trang tĩnh, không server. Muốn xài thật → để email + tải app. Trang cũ: Phase 50.</p>
<a class="go" href="phase-50-demo-site/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">4.2</span>
<div class="step__body">
<h3>YouTube · Amazon · Maps: tách trang + có hình <span class="chip chip--doing">M1–M3 code xong 2026-11-05 · M4, M5 chưa làm</span></h3>
<p>3 trang riêng trên sidebar, thumbnail video YouTube + ảnh sản phẩm Amazon, giá Amazon US đúng đơn vị. Trang cũ: Phase 55.1.</p>
<a class="go" href="phase-55-1-nguon-ngoai-store/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">4.3</span>
<div class="step__body">
<h3>Amazon Books: Kindle · Paperback · Hardcover <span class="chip chip--doing">M1–M7 có code 2026-11-07 · còn đo trên Amazon thật</span></h3>
<p>Chế độ Sách trên trang Amazon: điểm riêng từng định dạng, BSR theo ngày, keyword KDP, brief sách. Còn đo bằng Chrome của anh. Trang cũ: Phase 55.2.</p>
<a class="go" href="phase-55-2-amazon-books/">Xem chi tiết →</a>
</div>
</div>
</div>

## 5 · Bán — phần còn dở

Bản 1.1.0 đã public và mua thử đã chạy, nên ⭐ Build App + Money, Phase 33.1 và Version 10 đã về lại
[Plan 1](plan-1/index.md) (anh chốt 2026-11-07). Số đơn thật trên Lemon Squeezy theo dõi ở [Marketing](../marketing/index.md).

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">5.1</span>
<div class="step__body">
<h3>Review + Validate — test bán trước <span class="chip chip--doing">Code xong · chờ anh chạy test + nhập số thật</span></h3>
<p>Vòng test bán trước trên niche thật, nhập số thật vào evidence pack. Trang cũ: Phase 7.</p>
<a class="go" href="phase-7-review-validate/">Xem chi tiết →</a>
</div>
</div>
</div>

## 6 · Bộ tool KDP

4 tool sách dùng chung 1 nền số: Scout đọc trang danh sách sách anh mở trên Amazon và tự lấy BSR (tối đa 20 cuốn / lần
bấm). AI đọc lại số để kết luận. Gộp 2 plan Book Discover (mục 6 cũ) và Tool KDP nâng cấp (mục 7 cũ) ngày 2026-11-11.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">6</span>
<div class="step__body">
<h3>Bộ tool KDP — plan chung <span class="chip chip--todo">Plan 2026-11-11 · để sau Marketing · chưa làm</span></h3>
<p>Nền chung, 2 luật mới (Scout tự lấy BSR, ước thu nhập dạng khoảng), thứ tự làm, AI đọc lại số, màn hình KDP 4 tab.</p>
<a class="go" href="phase-plan2-06-bo-tool-kdp/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">6.1</span>
<div class="step__body">
<h3>Từ khoá + cạnh tranh (tool 4) <span class="chip chip--todo">Plan 2026-11-10 · chưa làm</span></h3>
<p>Scout chấm điểm sách ngay trên trang tìm Amazon và gửi sang app; gõ 1 chủ đề rộng ra 30–50 niche sách con.</p>
<a class="go" href="phase-plan2-07-kdp-nang-cap/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">6.2</span>
<div class="step__body">
<h3>Sách đang trend (tool 1) <span class="chip chip--todo">Plan 2026-11-11 · chưa làm</span></h3>
<p>Movers & Shakers, New Releases → sách đang lên, niche (chuyên mục nhỏ nhất), keyword suy ra từ tên sách.</p>
<a class="go" href="phase-plan2-06-bo-tool-kdp/#62-tool-1-sach-ang-trend/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">6.3</span>
<div class="step__body">
<h3>Chuyên mục đang lên + thu nhập sách (tool 2, 3) <span class="chip chip--todo">Plan 2026-11-09 · bản gọn Soi 1 cuốn sách làm 2026-11-13</span></h3>
<p>Top 50 sách của tối đa 10 chuyên mục, chuyên mục nào đang lên, thu nhập / tháng dạng khoảng có nguồn.</p>
<a class="go" href="phase-plan2-06-book-discover/">Xem chi tiết →</a>
</div>
</div>
</div>

## 7 · Audit kênh YouTube

Dán 1 link kênh hoặc @handle → sức khoẻ kênh, video vượt kênh / tụt, kiểu tiêu đề và độ dài đang ăn, người xem hỏi gì,
so với 3–5 đối thủ cùng niche. Không key; AI đọc lại số để kết luận.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">7</span>
<div class="step__body">
<h3>Audit kênh YouTube <span class="chip chip--todo">Plan 2026-11-11 · để sau Marketing · chưa làm</span></h3>
<p>Tab Audit kênh trên trang YouTube: 8 khối từ thẻ kênh tới AI đọc lại, dùng lại phần lõi của YouTube Research Pro, 7 bước M1–M7.</p>
<a class="go" href="phase-plan2-07-audit-kenh-youtube/">Xem chi tiết →</a>
</div>
</div>
</div>

## 8 · YouTube theo quốc gia + Kênh trend

Tra niche YouTube theo nước, và xem tuần này kênh nào đang ăn view ở 1 nước. Không key, không AI.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">8</span>
<div class="step__body">
<h3>YouTube theo quốc gia + Kênh trend <span class="chip chip--done">Làm 2026-11-11 · đã code</span></h3>
<p>Ô chọn nước 16 nước cho tra niche; tab Kênh trend: gợi ý địa phương → video tuần này → gom theo kênh. Ước lượng, không phải bảng xếp hạng chính thức.</p>
<a class="go" href="phase-plan2-08-youtube-theo-nuoc/">Xem chi tiết →</a>
</div>
</div>
</div>

## 9 · Học từ tool YouTube: tìm ý tưởng, soi đối thủ, gom số

Đọc các tool chuyên về YouTube (bắt trend, video vượt kênh, tìm niche, xếp hạng kênh), rút 7 bài học dẫn người mới và 8 việc
áp dụng cho trang YouTube.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">9</span>
<div class="step__body">
<h3>Học từ tool YouTube <span class="chip chip--doing">9.1–9.5 làm 2026-11-12 · 9.6–9.8 chưa làm</span></h3>
<p>YouTube Studio Trends / Research, vidIQ Outliers, 1of10, ViewStats, TubeLab, NexLev, Playboard, Social Blade → 3 lối vào, chip lọc, view / giờ, nhãn Đuổi / Thử / Bỏ, trend theo chuyên mục, lưu kênh theo dõi, xuất bảng.</p>
<a class="go" href="phase-plan2-09-youtube-hoc-tu-tool/">Xem chi tiết →</a>
</div>
</div>
</div>

## 10 · Keyword Intelligence

Biến cây keyword của Explorer thành trang Soi cơ hội: ma trận cơ hội, điểm có giải thích, độ đông, ý định, so xu hướng — chỉ số miễn phí đã có.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">10</span>
<div class="step__body">
<h3>Keyword Intelligence <span class="chip chip--doing">Phase 1–3 làm 2026-11-13 → 14 · Phase 4–8 chưa làm</span></h3>
<p>Mỗi số có nhãn nguồn, 3 kiểu cạnh tranh tách riêng, điểm cơ hội sửa được trọng số. Lượt tìm / CPC / độ khó SEO để xám “sắp có”.</p>
<a class="go" href="phase-plan2-10-keyword-engine/">Xem chi tiết →</a>
</div>
</div>
</div>

## 11 · Săn kênh nhỏ view nổ

Gõ 1 chủ đề → gom tới 100 kênh → lọc kênh nhỏ, mới, ít video mà view nổ → chốt 3 kênh. Cung – cầu: kênh nhỏ nổ to là cầu > cung. Không key.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">11</span>
<div class="step__body">
<h3>Săn kênh nhỏ view nổ <span class="chip chip--done">Làm 2026-11-14 · đã code</span></h3>
<p>Phễu 3 nút: lưới rộng → đọc kênh + 4 chip lọc → soi sâu 10 kênh, điểm 0–100. Mỗi kênh chốt có keyword gắn nhãn trend, nội dung kênh, video nổ to.</p>
<a class="go" href="phase-plan2-11-san-kenh-nho/">Xem chi tiết →</a>
</div>
</div>
</div>

## 12 · Săn sách cầu > cung

App tự đọc bảng xếp hạng sách Amazon → 100 cuốn → lọc sách mới, ít review, bán mạnh, có người gõ → chốt 5 cuốn. Bỏ Scout khỏi app.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">12</span>
<div class="step__body">
<h3>Săn sách cầu > cung <span class="chip chip--done">Làm 2026-11-14 · đã code</span></h3>
<p>Phễu 3 nút: đọc bảng xếp hạng → 4 chip lọc + ô gợi ý Amazon → soi sâu 20 cuốn, điểm 0–100, chốt 5. Soi 1 cuốn chỉ cần dán link / ASIN.</p>
<a class="go" href="phase-plan2-12-san-sach/">Xem chi tiết →</a>
</div>
</div>
</div>

## 13 · Nút Bắt đầu build

Bấm 1 nút trên trang Research → project đã gom sẵn keyword, đối thủ, lời chê, khoảng trống → tab Build 5 bước tới bộ build cho Claude Code.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">13</span>
<div class="step__body">
<h3>Nút Bắt đầu build <span class="chip chip--done">Làm 2026-11-14 · đã code</span></h3>
<p>Nối 3 chỗ rời (Collect tay, Projects, phiên AI Agent) thành 1 đường. Brief / Spec / Plan viết ngay trong project, xuất thư mục có START.md.</p>
<a class="go" href="phase-plan2-13-bat-dau-build/">Xem chi tiết →</a>
</div>
</div>
</div>

## 15 · Theo dõi ngách YouTube

Kênh nhỏ nổ view → gom kênh cùng ngách vào danh sách theo dõi → máy đọc lại mỗi ngày, chấm video Sắp nổ / Đang nổ / Đã nổ theo số nhiều ngày, rút cụm keyword đang nóng của ngách. Agent đọc qua MCP và tự tra YouTube (video vượt trội, soi kênh, phụ đề), giống TubeLab MCP nhưng chạy trên máy.
(Mục 14 · chấm đối thủ nên bắt chước đã giữ số trong mục 13, chưa viết.)

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">15</span>
<div class="step__body">
<h3>Theo dõi ngách + giai đoạn video <span class="chip chip--doing">15.7 Agent tự tra YouTube đã code 2026-11-15 · phần còn lại chờ duyệt</span></h3>
<p>Từ góp ý: tool lớn chỉ chụp 1 lần, không theo dõi cả ngách mỗi ngày. Dùng lại phễu Săn kênh nhỏ và nhãn nổ có sẵn, thêm số theo ngày.</p>
<a class="go" href="phase-plan2-15-theo-doi-ngach/">Xem chi tiết →</a>
</div>
</div>
</div>

## 16 · Trang Project dễ xài

Project là điểm cuối của app → mỗi project 1 loại (App / YouTube / Sách) có icon, 4 chặng Gom → Chấm → Làm → Theo dõi thay 8 tab, bàn chấm gọn thành đèn + thanh, AI Agents gộp vào Projects.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">16</span>
<div class="step__body">
<h3>Loại project + 4 chặng + bàn chấm gọn <span class="chip chip--doing">16.1 + 16.2 đã code 2026-11-15 · phần còn lại chưa làm</span></h3>
<p>Từ góp ý 2026-11-15: không biết project loại gì, tab không nói để làm gì, bàn quyết định nhiều chữ, Brief / Spec / Plan nằm riêng ở AI Agents.</p>
<a class="go" href="phase-plan2-16-trang-project/">Xem chi tiết →</a>
</div>
</div>
</div>

## 17 · Soi kênh: Google Trends, keyword, so kênh

Soi 1 kênh thêm khối Google Trends (đu trend, lọt trend, trend kênh chưa làm), bảng keyword có tag thật của video và nút đem đi soi tiếp, cùng chế độ so tối đa 3 kênh một lượt.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">17</span>
<div class="step__body">
<h3>Google Trends, keyword dễ hiểu, so 3 kênh <span class="chip chip--doing">17.1 + 17.2 + 17.4 đã code 2026-11-15 · 17.3 + 17.5 chờ duyệt</span></h3>
<p>Học từ TubeBuddy, vidIQ, 1of10, Keywords Everywhere. Đã đo: Trends lọc YouTube Search và RSS Trending now chạy không cần key, đọc được tag thật của video.</p>
<a class="go" href="phase-plan2-17-trend-keyword-so-kenh/">Xem chi tiết →</a>
</div>
</div>
</div>

## 18 · Soi kênh: kênh đối thủ liên quan

Soi 1 kênh thêm khối Kênh đối thủ lấy từ cột Video đề xuất của YouTube (tệp cùng khán giả, không cần chung keyword), kèm sub, số video, năm lập kênh, × sub và nút soi tiếp. Đầu trang có thêm chip sub · số video · năm lập kênh.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">18</span>
<div class="step__body">
<h3>Kênh đối thủ liên quan <span class="chip chip--done">Xong 2026-11-15</span></h3>
<p>Đo trên Happiko: 5 video gốc, 8 kênh cùng ngách, cả lượt soi 17,5 giây. Không key, không AI.</p>
<a class="go" href="phase-plan2-18-kenh-doi-thu/">Xem chi tiết →</a>
</div>
</div>
</div>

## 19 · Soi kênh: làm theo kênh bằng mẫu kịch bản

Soi 1 kênh hiện tiêu đề video đúng ngôn ngữ nước đã chọn, và có khối Làm theo kênh: tick các video đã chứng minh, AI đọc phụ đề thật, viết 1 mẫu kênh (giọng, kiểu story, người xem…) và 1 mẫu cốt truyện cho mỗi video. Dừng ở mẫu.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">19</span>
<div class="step__body">
<h3>Làm theo kênh bằng mẫu kịch bản <span class="chip chip--todo">Viết 2026-11-15 · chờ anh duyệt</span></h3>
<p>Dùng lại phụ đề (mục 7) và luồng ✦ Dùng · Bỏ · Hỏi lại. Tiêu đề sai ngôn ngữ do phiên YouTube luôn là tiếng Anh.</p>
<a class="go" href="phase-plan2-19-mau-kich-ban/">Xem chi tiết →</a>
</div>
</div>
</div>

## 20 · So sánh đối thủ app

Bật tab Compare competitors: chọn 2–4 app Play / App Store từ 1 lượt Research hoặc 1 project App, so số store bằng bảng mỗi app 1 cột, hạng keyword, tính năng có / không. Nút ✦ AI viết điểm mạnh / yếu kèm nguồn, không bắt buộc.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">20</span>
<div class="step__body">
<h3>So sánh đối thủ app <span class="chip chip--done">Xong 2026-11-15</span></h3>
<p>Chỉ đọc DB, không tải thêm. Có 293 lượt Research, trung bình 94,6 app mỗi lượt, nên luôn có app để chọn.</p>
<a class="go" href="phase-plan2-20-so-sanh-doi-thu/">Xem chi tiết →</a>
</div>
</div>
</div>

## 21 · YouTube trend: keyword đang được tìm

Tab Xem đang trend gì thêm phần keyword: thẻ kết luận "nên làm", đường Google Trends (YouTube Search) cho 5 keyword, cột đang lên, bong bóng cầu – cung, vòng tròn chia nhóm, Google đang tìm gì hôm nay.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">21</span>
<div class="step__body">
<h3>Keyword đang được tìm + Google Trends <span class="chip chip--done">Chốt + code 2026-11-16 · 21.2–21.7</span></h3>
<p>Không key, không AI. Đo 2026-11-15: 5 keyword trong 1 lần gọi Trends mất 0,9 giây, rising 1 keyword mất 3,8 giây.</p>
<a class="go" href="phase-plan2-21-keyword-dang-tim/">Xem chi tiết →</a>
</div>
</div>
</div>

## 22 · So sánh app → app mới nên có gì

So 2–4 app đối thủ, cuối trang ra bảng tổng kết: phải có · làm khác · còn trống · đang thu tiền. Thêm nhãn Cầu > cung cho keyword app.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">22</span>
<div class="step__body">
<h3>Bảng "app mới nên có gì" + Cầu > cung <span class="chip chip--todo">Viết 2026-11-15 · chờ anh duyệt</span></h3>
<p>Rút tính năng bằng luật SAFE, không AI. Đo 2026-11-15: 144 / 294 lượt Research có app dưới 1 năm vào top 10 với ≥ 50 rating.</p>
<a class="go" href="phase-plan2-22-so-app-ra-viec-can-lam/">Xem chi tiết →</a>
</div>
</div>
</div>

## 23 · Trang YouTube: gom nhóm + chạy nhiều lượt

5 thẻ gom thành 3 nhóm (Tìm ngách · Săn kênh · Soi kênh) có chip chế độ. Gõ nhiều keyword / link một lần, hàng chờ máy chủ chạy nhiều luồng.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">23</span>
<div class="step__body">
<h3>3 nhóm + chip · ô nhiều dòng · hàng chờ 3 luồng <span class="chip chip--todo">Viết 2026-11-15 · chờ anh duyệt</span></h3>
<p>Bỏ lỗi "Tab này đang chạy", lượt dư xếp hàng. Số luồng chưa đo, sẽ đo 1 · 3 · 5 luồng trước khi chốt.</p>
<a class="go" href="phase-plan2-23-youtube-gom-nhom-chay-nhieu/">Xem chi tiết →</a>
</div>
</div>
</div>

## 24 · Săn app cầu > cung + gom nhóm App

Menu App gom theo việc (Tìm ngách · Săn app · Soi app). Trang mới Săn app: 1 chủ đề → Explorer 100 keyword → Research 10 → chốt 3 keyword cầu > cung.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">24</span>
<div class="step__body">
<h3>Săn app 100 → 10 → 3 · gom menu App <span class="chip chip--doing">Code 2026-11-16 theo mặc định · chờ anh soát</span></h3>
<p>Không key, không AI. Đo 2026-11-15: Explorer trung bình 317 giây / 88 keyword, Research 93 giây / keyword. Code theo 3 mặc định: menu bên trái, tick sẵn 10, 3 luồng.</p>
<a class="go" href="phase-plan2-24-san-app-cau-cung/">Xem chi tiết →</a>
</div>
</div>
</div>

## 25 · Học AppTweak + Appfigures, giữ chất riêng

Học 3 thứ nhỏ (điểm độ khó leo, hộp "đổi gì từ lần trước", AI có nhắc app nào), không đua về số tải và doanh thu. Chốt câu định vị và 2 bài blog so sánh.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">25</span>
<div class="step__body">
<h3>3 thứ học + định vị "chọn đúng app để làm" <span class="chip chip--todo">Viết 2026-11-16 · chờ anh chốt</span></h3>
<p>Phần marketing (định vị + 2 bài so sánh) làm được ngay. Ba tính năng nhỏ code sau, dùng lại số đã có, không gọi thêm mạng (trừ nút Hỏi AI).</p>
<a class="go" href="phase-plan2-25-hoc-apptweak-appfigures/">Xem chi tiết →</a>
</div>
</div>
</div>

## 26 · Săn app tìm ra điểm yếu đối thủ

Săn app trả lời thêm "đánh vào điểm yếu nào, của app nào, bao nhiêu người than". Lấy từ góp ý thread r/SideProject 2026-11-16.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">26</span>
<div class="step__body">
<h3>Đọc review 3 app dẫn đầu · đèn đỏ / xanh · "đánh vào đâu" <span class="chip chip--doing">Viết + code 26.1–26.7 2026-11-16 · chờ anh soát</span></h3>
<p>Đếm độ lặp theo việc bị hỏng (≥ 3 người khác nhau), đèn đỏ khi nhóm tiền lớn nhất, cung đo bằng độ yếu của app dẫn đầu. Luật, không AI.</p>
<a class="go" href="phase-plan2-26-san-app-diem-yeu/">Xem chi tiết →</a>
</div>
</div>
</div>

## 27 · Review Mining: đào review chê ra cơ hội

Một trang riêng: dán link app → đọc review chê → xếp nỗi đau có điểm → xem review gốc → xuất báo cáo. Gom phần đã có ở Soi 1 app, So sánh app, Săn app.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">27</span>
<div class="step__body">
<h3>Đào review · điểm nỗi đau /100 · bằng chứng · 17 nước <span class="chip chip--doing">Code 27.0–27.4 + xuất + Tổng kết 27.6 · 2026-11-17 · chờ anh soát</span></h3>
<p>Mục App tăng từ 5 lên 17 nước (27.0, đã làm). Còn lại: import CSV/JSON, đọc sâu 1.000 review Play, điểm nỗi đau có công thức, sửa nhóm, xin tính năng, so app × nước, thẻ cơ hội gắn nhãn AI suy luận. Không dùng embeddings, không chạy theo lịch.</p>
<a class="go" href="phase-plan2-27-review-mining/">Xem chi tiết →</a>
</div>
</div>
</div>

## 28 · Cài đặt: quản lý dữ liệu (nhập · xuất · xoá)

Một chỗ trong Cài đặt → Dữ liệu & sao lưu để chuyển dữ liệu sang máy khác hoặc dọn bớt, thay vì đi từng trang.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">28</span>
<div class="step__body">
<h3>6 nhóm · tick chọn · Tải / Xoá · Nhập file <span class="chip chip--doing">Code 2026-11-16 · chờ anh soát</span></h3>
<p>Nhóm: Project · Phiên AI Agent · Keyword đã tra · Niche research · YouTube (kênh, săn kênh, so kênh, trend) · Amazon · Maps. Lọc theo tên (bỏ dấu), tick nhiều → <b>Tải</b> file <code>.niche-data.json</code> hoặc <b>Xoá</b> (hỏi lại, backup DB ngay trước). <b>Nhập file</b> nhận cả gói <code>.niche.json</code> cũ; nhập 2 lần không nhân đôi. Tải khoá PRO như Xuất Project; xem danh sách, nhập, xoá thì Free cũng được.</p>
</div>
</div>
</div>

## 29 · Săn việc làm tay: chỗ người ta còn chắp vá

Một cách săn mới trong Săn app: gõ 1 việc → đo xem người ta có đang làm tay việc đó không (bảng tính, template, giấy in, hỏi "có app nào không").

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">29</span>
<div class="step__body">
<h3>Google gợi ý · Trends làm tay vs app · câu hỏi · app bán template · review bỏ về làm tay <span class="chip chip--todo">Viết plan 2026-11-17 · chờ anh duyệt</span></h3>
<p>5 tín hiệu, mỗi tín hiệu có link nguồn, gom thành 1 thẻ "Người ta đang làm tay: rõ / ít / không thấy / chưa đo". Không đọc trang kết quả Google (CAPTCHA); câu hỏi kiểu People Also Ask lấy từ Google gợi ý + Stack Exchange + Ask HN.</p>
<a class="go" href="phase-plan2-29-san-viec-lam-tay/">Xem chi tiết →</a>
</div>
</div>
</div>

## 30 · Audit 1 app: chấm ASO app đã có, sửa gì trước

Thẻ thứ 7 ở App Market Research cho người **đã có app trên store**: dán link → chọn keyword → điểm /100 → việc nên sửa → lấy đối thủ sang So sánh app. Học lõi Audit của WowKeywords.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">30</span>
<div class="step__body">
<h3>Trang store + hạng keyword · điểm /100 · 3–5 việc nên sửa · Lấy đối thủ <span class="chip chip--todo">Spec + plan 2026-11-17 · chưa code</span></h3>
<p>Chip keyword tự gợi ý (tên, phụ đề, gợi ý store), user sửa được. Điểm 4 phần: Tên &amp; phụ đề 30 · Mô tả 15 · Hình ảnh &amp; rating 20 · Hạng keyword 35, phần chưa đo không chấm 0. Lấy đối thủ = app đứng trên mình + app tương tự, tick tối đa 3 app đẩy sang So sánh app. Chưa làm: nhiều nước, AI viết lại tên.</p>
<a class="go" href="phase-plan2-30-audit-app/">Xem chi tiết →</a>
</div>
</div>
</div>

## 31 · Trending Apps: bảng xếp hạng theo nước, thiết bị, nhóm app

Thẻ thứ 8 ở App Market Research: chọn store, nước (1 hoặc nhiều), thiết bị, loại bảng, nhóm app → bảng Top kèm chip **Mới** / **↑ hạng**, giống tab trend YouTube.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">31</span>
<div class="step__body">
<h3>Bảng Top 2 store · lưu bản để tính ↑ hạng · chạy nhiều nước · thẻ kết luận <span class="chip chip--todo">Spec 2026-11-17 · chờ anh chốt 3 câu · chưa code</span></h3>
<p>Đã đo nguồn: Google Play <code>gplay.list</code> trả 200 app/bảng, lọc nhóm có tác dụng, không tách điện thoại / máy tính bảng. App Store RSS cũ có iPhone · iPad · Mac, Grossing, lọc nhóm, tối đa 100 app. Không có số tải / doanh thu. ↑ hạng chỉ có sau khi đã lưu ít nhất 1 lần trước.</p>
<a class="go" href="phase-plan2-31-trending-apps/">Xem chi tiết →</a>
</div>
</div>
</div>

## 32 · Google Trends trong Săn app · Soi app · So app

Đưa Google Trends vào 3 thẻ App: thấy keyword đang lên hay xuống và cụm từ người ta tìm kèm để dùng làm keyword, tính năng, tên phụ.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">32.1</span>
<div class="step__body">
<h3>Săn app: đường Trends + cụm từ tìm kèm <span class="chip chip--done">Coded 2026-11-18 · chưa commit</span></h3>
<p>Thẻ top 3 có đường 12 tháng + chip ▲/▼ % (13 tuần cuối so đầu), cụm Rising / Top của keyword (lấy từ Research đã chạy, không gọi Google thêm). Đo 2026-11-18: keyword dài trong top 3 gần như không có cụm từ Trends, nên thêm khối "Cụm từ người ta tìm quanh chủ đề" cho keyword gốc (1 lần gọi, cache 1 ngày). Bấm 1 cụm = Research cụm đó. Dòng keyword còn lại có đường nhỏ + chip.</p>
</div>
</div>
<div class="step" markdown>
<span class="step__n">32.2</span>
<div class="step__body">
<h3>Soi 1 app: Trends của keyword chính + tên app <span class="chip chip--done">Coded 2026-11-18 · chưa commit</span></h3>
<p>Keyword chính = keyword app đứng hạng tốt nhất trong Research đã có, chưa có thì phần sau dấu “:” / “-” của tên; tên app = phần thương hiệu (luật chọn phần ngắn, “by X”). 2 ô sửa được + Đo lại. 2 lần gọi Trends (cache 1 ngày): 2 đường cùng thang + câu “tên app được tìm bằng N% keyword”, cụm Rising / Top quanh keyword, đánh dấu cụm hợp ASO (app / free / alternative / vs / best…). Đo 2026-11-18 MyFitnessPal US: “calorie tracker” đi ngang −17%, tên app 242% keyword nhưng ▼ −38%, 6 cụm hợp ASO.</p>
</div>
</div>
<div class="step" markdown>
<span class="step__n">32.3</span>
<div class="step__body">
<h3>So app: tên ≤ 4 app + keyword gốc trên 1 biểu đồ Trends <span class="chip chip--done">Coded 2026-11-18 · chưa commit</span></h3>
<p>1 lần gọi, thang 0–100 chung, màu đường trùng màu chấm app. Câu kết luận: app được tìm nhiều nhất + app đang lên; mỗi app 1 thanh trung bình + chip ▲/▼. Cùng 1 app ở 2 store gộp 1 đường. Tên app quá ít người tìm → “quá ít người tìm trên Google”, không chấm 0.</p>
</div>
</div>
</div>

## 32 · Săn app theo app: ra 1 app đáng bắt chước

Săn app có 2 tab: Theo keyword (đang có) và **Theo app**. Tab mới gom mọi app trong top 10 các keyword đã Research, bỏ trùng, lọc, chấm "Đáng bắt chước" /100 rồi chỉ ra 1 app để soi kỹ.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">32</span>
<div class="step__body">
<h3>2 tab · gom + bỏ trùng app · lọc mới / ≥ 1.000 rating / bỏ studio lớn · điểm 5 phần · app đầu + 2 app sau <span class="chip chip--todo">Spec 2026-11-17 · anh đã duyệt thiết kế · chưa code</span></h3>
<p>Dùng chung lượt săn, không gọi store thêm. Đo trên 3 lượt săn thật: 151 / 165 / 49 app → 9 / 6 / 11 app qua lọc. Điểm: cầu đã chứng minh 30 · phủ keyword 20 · chỗ chen 20 · còn mới 15 · thu tiền 15; phần chưa đo không tính 0. Nút Soi app này + Thêm để so.</p>
<a class="go" href="phase-plan2-32-san-app-theo-app/">Xem chi tiết →</a>
</div>
</div>
</div>

## 33 · So đối thủ theo lời chê: ai tốt, ai hỏng, chỗ trống

Làm thật tab So app của Đào review: 2–10 app → bảng nhiệt nỗi đau × app → 6 kết luận bằng luật (chung · riêng · tốt nhất · yếu nhất · khoảng trống cả chợ · chỗ làm khác được), mỗi cơ hội qua cửa kiểm chứng cầu + trả tiền.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">33</span>
<div class="step__body">
<h3>Bảng nỗi đau × app · khoảng tin · 6 kết luận · cửa kiểm chứng <span class="chip chip--todo">Anh duyệt 2026-11-18 · chưa code · commit 24–27 trước</span></h3>
<p>Đo 2026-11-18: 266 app có review trong DB, 188 app có ≥ 30 review chê, nhưng chỉ 2.106 / 15.956 review là 4–5★ nên khi so phải đọc lại đủ 1–5★. Học Appbot (xu hướng), AppFollow (theo nước), FeatCompare + RE-SWOT (theo tính năng, ô SWOT).</p>
<a class="go" href="phase-plan2-33-so-doi-thu-theo-loi-che/">Xem chi tiết →</a>
</div>
</div>
</div>

## 34 · Đào review: gom theo nghĩa + chấm nỗi đau đúng hơn

Nâng mục 27: gom review theo nghĩa bằng model chạy trên máy, nên câu khác chữ cùng ý vào chung nhóm. Mỗi nhóm có tên đọc được và đủ 9 thông tin.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">34</span>
<div class="step__body">
<h3>Spike model trong app Mac · tách câu + nhận ngôn ngữ · embedding trên máy · gom phân cấp · tên c-TF-IDF · gộp / tách · điểm Wilson <span class="chip chip--todo">Spec 2026-11-18 · đã chốt model nhiều tiếng · chờ 2 câu · chưa code</span></h3>
<p>Học Appbot, AppFollow, Thematic, Enterpret, BERTopic, FeClustRE. Giữ công thức 30·30·20·20 của mục 27, sửa cách đo Tần suất (trừ hao cỡ mẫu, cân app to / nhỏ). Không UMAP / HDBSCAN, không API trả phí.</p>
<a class="go" href="phase-plan2-34-gom-review-theo-nghia/">Xem chi tiết →</a>
</div>
</div>
</div>


## 35 · Xin tính năng: người dùng muốn có gì, app nào còn thiếu

Làm thật tab Xin tính năng của Đào review (Module 06 · Feature Request Mining): gom câu "I wish / please add / bring back" thành bảng tính năng kiểu Pendo, mỗi dòng có số người xin, app nào đã có, tín hiệu trả tiền, cỡ việc và câu trích.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">35</span>
<div class="step__body">
<h3>Bảng lời xin · app đã có / thiếu · tín hiệu tiền · điểm Đáng làm /100 <span class="chip chip--todo">Viết 2026-11-18 · chờ anh chốt 4 câu · chưa code</span></h3>
<p>Đo 2026-11-18: 394 / 15.956 review có mẫu câu xin, ở 140 app, nhưng 30% nằm ở review 4–5★ mà code hiện bỏ qua; chỉ 6 app có ≥ 10 lời xin nên phải gom cả niche. Không ra số tiền, không có "unique reviewers" (DB không lưu người viết). Học Pendo, Canny, AppFollow, Appbot, bộ dữ liệu Maalej, SAFE / MARA.</p>
<a class="go" href="phase-plan2-35-xin-tinh-nang/">Xem chi tiết →</a>
</div>
</div>
</div>

---

Đã xong → [Plan 1](plan-1/index.md) · Chưa xếp lịch → tab BACKLOG · Việc ngoài plan → [Appendix](../appendix.md).
