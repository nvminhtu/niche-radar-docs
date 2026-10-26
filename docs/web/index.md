# Web — làm + test tính năng (chạy local)

> Mọi tính năng làm và **test** ở **bản Web chạy local** (`web/`, `npm run dev` → `localhost:3200`). Khách nhận
> **app Mac + Windows** bọc đúng giao diện này: [App Mac + Windows](../app/index.md).
>
> **Thứ tự (chốt 2026-10-26):** Version 1 → **Version 9** (analytics) → **Version 10** (dùng thử + license) → App Mac +
> Windows → Version 11 (marketing) → Version 2, 3, 4, 12. Dưới vạch **⛔ KO LÀM** là các phase không ra tiền, không thêm người dùng.

<span class="chip chip--doing">Đang làm · Phase 7 · tiếp theo 10 Reddit Gap → 11 Research nguồn gap → 12–27</span>

Mỗi phase đi theo [Quy trình build](../quy-trinh-build.md). Việc ngoài plan → [Appendix](../appendix.md).

## Version 1 · MVP (Phase 1–11)

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
<h3>Verified Sites <span class="chip chip--todo">Tạm dừng · dời sang Claude in Chrome (Phase 6)</span></h3>
<p>Doanh thu thật từ TrustMRR và các trang tương tự — ai đang thu tiền trong ngách.</p>
<a class="go" href="phase-5-verified/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">6</span>
<div class="step__body">
<h3>Tích hợp AI (bản Web) <span class="chip chip--done">Xong · tuyến A chờ key</span></h3>
<p>API key, extension miễn phí, AI chạy trong trình duyệt / trên máy — thử từng đường rồi chọn.</p>
<a class="go" href="phase-6-ai-web/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">7</span>
<div class="step__body">
<h3>Review + Validate <span class="chip chip--doing">Code xong · chờ anh chạy test bán trước</span></h3>
<p>Soát lại Phase 1–6 trên 5 niche thật, chấm điểm v2, evidence pack, test bán trước.</p>
<a class="go" href="phase-7-review-validate/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">8</span>
<div class="step__body">
<h3>Project + dữ liệu chuyển máy <span class="chip chip--done">Xong</span></h3>
<p>Project có đánh giá, xuất / nhập .niche.json · .md · CSV, backup / restore.</p>
<a class="go" href="phase-8-project-data/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">9</span>
<div class="step__body">
<h3>Small Features Update <span class="chip chip--done">4 mục ưu tiên xong 2026-10-25</span></h3>
<p>Các tính năng nhỏ lượm được khi dùng thật, mỗi cái một plan ngắn. Ưu tiên: điểm v2 thêm trục Tiếp cận + Hợp sức mình, mức nặng chủ đề than, nhãn mô hình tiền, theo dõi định kỳ.</p>
<a class="go" href="phase-9-small-features/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">9c</span>
<div class="step__body">
<h3>Đa ngôn ngữ (i18n) <span class="chip chip--done">Khung xong 2026-10-25</span></h3>
<p>Chữ giao diện tách ra file theo ngôn ngữ (Tiếng Việt · English · Español), ô chọn ngôn ngữ ở header + Cài đặt. Thiếu bản dịch thì hiện tiếng Anh rồi tiếng Việt. Dịch dần từng trang khi cần.</p>
<a class="go" href="phase-9c-i18n/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">10</span>
<div class="step__body">
<h3>Reddit Gap <span class="chip chip--doing">Code xong 2026-10-25 (tuyến C: nhập file) · chờ anh nhập ≥ 500 bài r/MacOS thật</span></h3>
<p>Lưu trang Reddit bằng Chrome (JSON hoặc HTML), nhập vào trang Reddit Gap → xếp chuyên mục + chủ đề, đếm chủ đề hỏi nhiều, quan tâm nhiều, chưa ai giải, kèm link bài gốc và xuất .md.</p>
<a class="go" href="phase-10-reddit-gap/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">10b</span>
<div class="step__body">
<h3>Q&amp;A Gap (Stack Exchange + Hacker News) <span class="chip chip--done">Xong 2026-10-26</span></h3>
<p>Câu xin phần mềm / hỏi cách làm từ Ask Different, Super User, Software Recs và Ask HN qua API miễn phí, không key. Xếp chung chủ đề với Reddit Gap, thêm lượt xem và cờ "đã có câu trả lời được chấp nhận"; tab Gộp cộng các nguồn.</p>
<a class="go" href="phase-10b-qa-gap/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">10c</span>
<div class="step__body">
<h3>GitHub Feature Request Gap <span class="chip chip--todo">Chưa làm · plan 2026-10-26</span></h3>
<p>Issue nhiều 👍 của nhóm repo app Mac menu bar, app Mac, Chrome extension, plugin Obsidian → tính năng người dùng xin mà maintainer từ chối hoặc để treo, gom theo chủ đề và repo.</p>
<a class="go" href="phase-10c-github-gap/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">11</span>
<div class="step__body">
<h3>Research nguồn tìm gap <span class="chip chip--done">Xong 2026-10-26 · chờ duyệt top 3</span></h3>
<p>Chỉ research, chưa code: liệt kê mọi nơi dev / indie tìm gap + keyword niche (Pinterest Trends, Product Hunt, Hacker News…), chấm mức độ và nên làm hay không; gom MCP free / trả phí, tool scrape, repo GitHub dùng kèm, và phương pháp tìm gap / niche anh chưa biết.</p>
<a class="go" href="phase-11-gap-sources/">Xem chi tiết →</a>
</div>
</div>
</div>

## Version 1 · Làm kỹ tính năng chính (Phase 12–27)

Các tính năng chính đã có bản đầu ở Phase 1–9 — mỗi cái được **một phase riêng** để làm kỹ: đủ dữ liệu, giải thích
được, có "Xong khi" đo được. Làm theo thứ tự 12 → 26; Phase 27 soát lại cả cụm.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">12</span>
<div class="step__body">
<h3>Đối thủ bị chê gì <span class="chip chip--todo">Chưa làm · plan 2026-10-25</span></h3>
<p>Gộp lời chê cùng ý, chia loại (lỗi · mất dữ liệu · ép trả phí · quảng cáo · thiếu tính năng…), bảng app × lời chê, lời chê mới nổi, danh sách "người dùng ước gì" — không AI.</p>
<a class="go" href="phase-12-competitor-complaints/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">13</span>
<div class="step__body">
<h3>Chấm sức khoẻ niche <span class="chip chip--todo">Chưa làm · plan 2026-10-25</span></h3>
<p>Mở từng yếu tố ra công thức + nguồn, độ tin hiện to, cờ chặn ép xuống TEST THÊM / BỎ, ngưỡng do anh đặt, back-test với niche đã biết kết quả.</p>
<a class="go" href="phase-13-niche-health/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">14</span>
<div class="step__body">
<h3>Collect niche vào Project <span class="chip chip--todo">Chưa làm · plan 2026-10-25</span></h3>
<p>Gom từ mọi chỗ (keyword, đối thủ, lời chê, ô trống tính năng), gom hàng loạt, tạo project ngay trong popover, chụp số lúc gom, không trùng, hoàn tác.</p>
<a class="go" href="phase-14-collect/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">15</span>
<div class="step__body">
<h3>Quản lý Project <span class="chip chip--todo">Chưa làm · plan 2026-10-25</span></h3>
<p>Tìm / lọc / thẻ / lưu trữ / nhân bản / gộp project, trang project chia tab, lý do loại bắt buộc, bước tiếp + ngày hẹn, nhật ký.</p>
<a class="go" href="phase-15-project-manage/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">16</span>
<div class="step__body">
<h3>Export (CSV, JSON, gói cho LLM) <span class="chip chip--doing">Code xong · merge main 2026-10-26 · còn mở CSV bằng Google Sheets</span></h3>
<p>Một hộp Xuất chung: CSV mở đúng trên Excel / Sheets, JSON có schema, Markdown, gói LLM (brief + schema + prompt) cắt theo trần token.</p>
<a class="go" href="phase-16-export/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">16b</span>
<div class="step__body">
<h3>Bàn quyết định long-tail + đo nhu cầu Pro <span class="chip chip--done">Xong 2026-10-26 · fake-door live trên demo</span></h3>
<p>Chấm các keyword trong Project theo rubric 5 trục có dẫn chứng, Copy prompt cho AI rồi dán JSON ngược, ra BUILD / TEST THÊM / BỎ. Kèm 2 nút Pro giả (fake-door) đo có ai muốn trả tiền.</p>
<a class="go" href="phase-16b-decision-board/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">17</span>
<div class="step__body">
<h3>Tóm tắt niche + chủ đề than (AI) <span class="chip chip--todo">Chưa làm · plan 2026-10-25</span></h3>
<p>Chạy tuyến A thật khi có key, tóm tắt khung 6 mục, trích dẫn đã kiểm, kiểm chéo với lời chê không AI, chỉ gửi review mới.</p>
<a class="go" href="phase-17-ai-summary/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">18</span>
<div class="step__body">
<h3>Doanh thu thật: TrustMRR + nguồn khác + AI <span class="chip chip--todo">Chưa làm · plan 2026-10-25</span></h3>
<p>Bước 0 chọn nguồn doanh thu công khai, AI khớp tên đối thủ, dòng verified đủ trường, ước theo bậc tách riêng, bảng "Ai đang thu tiền".</p>
<a class="go" href="phase-18-revenue/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">19</span>
<div class="step__body">
<h3>Backup / restore dữ liệu <span class="chip chip--todo">Chưa làm · plan 2026-10-25</span></h3>
<p>Backup tự động mỗi ngày, giữ 7 ngày · 4 tuần · 6 tháng, kiểm toàn vẹn, thư mục ngoài máy, restore xem trước, restore 1 project.</p>
<a class="go" href="phase-19-backup-restore/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">20</span>
<div class="step__body">
<h3>Research 1 keyword — trang kết quả <span class="chip chip--todo">Chưa làm · plan 2026-10-25</span></h3>
<p>Đầu trang là câu trả lời (5 con số), khối xếp theo câu hỏi chọn niche, trạng thái + chạy lại từng nguồn, so với lần tra trước.</p>
<a class="go" href="phase-20-research-page/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">21</span>
<div class="step__body">
<h3>Explore — cây keyword + bản đồ ngách <span class="chip chip--todo">Chưa làm · plan 2026-10-25</span></h3>
<p>Lọc rác + thương hiệu, gộp keyword cùng nghĩa, thêm gợi ý App Store, điểm cơ hội giải thích được, chọn lá → Research hàng loạt.</p>
<a class="go" href="phase-21-explore-tree/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">22</span>
<div class="step__body">
<h3>Hồ sơ đối thủ + cờ đối thủ yếu <span class="chip chip--todo">Chưa làm · plan 2026-10-25</span></h3>
<p>Trang riêng mỗi đối thủ (2 store, nhịp cập nhật, giá, bị chê gì, doanh thu), cờ bỏ bê · bị chê · một store · thu tiền · mới vào.</p>
<a class="go" href="phase-22-competitor-profile/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">23</span>
<div class="step__body">
<h3>Theo dõi niche định kỳ <span class="chip chip--todo">Chưa làm · plan 2026-10-25</span></h3>
<p>Tự tra lại theo lịch khi server chạy, chỉ báo thay đổi đáng chú ý, hộp "Thay đổi tuần này", dòng thời gian project.</p>
<a class="go" href="phase-23-tracking/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">24</span>
<div class="step__body">
<h3>Evidence pack + test bán trước <span class="chip chip--todo">Chưa làm · plan 2026-10-25</span></h3>
<p>Chạy hết 1 vòng thật: evidence pack đủ khung → /app-demand → ngưỡng ghi trước → số thật → BUILD / TEST THÊM / BỎ.</p>
<a class="go" href="phase-24-evidence-presell/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">25</span>
<div class="step__body">
<h3>Cài đặt AI + tuyến miễn phí <span class="chip chip--todo">Chưa làm · plan 2026-10-25</span></h3>
<p>Nhiều nhà cung cấp tự mang key, thử lại Gemini Nano trong Chrome + model trên máy, sổ chi phí, bài thử chuẩn 1 bấm.</p>
<a class="go" href="phase-25-ai-settings/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">26</span>
<div class="step__body">
<h3>MCP của app <span class="chip chip--todo">Chưa làm · plan 2026-10-25</span></h3>
<p>MCP server chỉ đọc để Claude tự đọc DB: tìm niche, so niche, đối thủ, lời chê, project — trả kèm nguồn.</p>
<a class="go" href="phase-26-mcp/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">27</span>
<div class="step__body">
<h3>Review cụm tính năng chính <span class="chip chip--todo">Chưa làm · plan 2026-10-25</span></h3>
<p>Soát Phase 12–26 trên 5 niche thật, phiếu soát từng phase, sửa lỗi, cập nhật Hướng dẫn / About, ra bản Web mới.</p>
<a class="go" href="phase-27-review-core/">Xem chi tiết →</a>
</div>
</div>
</div>

## Version 1 · So sánh + UI + Setup (Phase 28–30.2)

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">28</span>
<div class="step__body">
<h3>So sánh niche <span class="chip chip--todo">Chưa làm · sau Phase 27</span></h3>
<p>2–4 niche cạnh nhau: cơ hội, đối thủ, xu hướng, đau, tiền — tô ô thắng từng hàng, không AI.</p>
<a class="go" href="phase-28-compare-niche/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">29</span>
<div class="step__body">
<h3>UI / UX Improvement <span class="chip chip--todo">Chưa làm</span></h3>
<p>Sửa chỗ vướng thật: luồng chính, trạng thái tải / lỗi, bảng dày, sáng / tối.</p>
<a class="go" href="phase-29-ui-ux/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">30.1</span>
<div class="step__body">
<h3>Setup ngay trong Web <span class="chip chip--todo">Chưa làm</span></h3>
<p>Hướng dẫn cài đúng máy, nút Kiểm tra máy báo thiếu gì + gói cài, nút Hỏi AI (ChatGPT · Gemini · Claude).</p>
<a class="go" href="phase-30-1-setup/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">30.2</span>
<div class="step__body">
<h3>Tutorial — nút ? mỗi tính năng <span class="chip chip--todo">Chưa làm</span></h3>
<p>Bấm ? cạnh tính năng: 1 câu làm gì + 2–4 hình bước đơn giản, ít chữ.</p>
<a class="go" href="phase-30-2-tutorial/">Xem chi tiết →</a>
</div>
</div>
</div>

<hr class="nr-mvp-line">

## Version 9 · Analytics + báo lỗi — bỏ Account (Phase 64–65)

Đo người tải app đi tới đâu (mở → dùng thử → tra niche → nhập license) và biết khi app lỗi. **Không tài khoản**: app
bán bằng license key, dữ liệu ở máy — học [Wow Keywords](../doi-thu-tham-khao.md#wow-keywords). Chi tiết: [Tổng quan Version 9](version-9.md).

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">64</span>
<div class="step__body">
<h3>Analytics + báo lỗi <span class="chip chip--todo">Chưa làm</span></h3>
<p>9 sự kiện phễu (thêm dùng thử, nhập license), chỉ loại + số đếm, có hỏi đồng ý; báo lỗi tự động không cần server riêng.</p>
<a class="go" href="phase-64-analytics-errors/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">65</span>
<div class="step__body">
<h3>Trang Riêng tư <span class="chip chip--todo">Chưa làm</span></h3>
<p>Privacy Policy ghi đúng từng thứ app gửi đi, link trong app. Phần xoá tài khoản bỏ.</p>
<a class="go" href="phase-65-privacy-delete/">Xem chi tiết →</a>
</div>
</div>
</div>

## Version 10 · Sell Pro — tải về + dùng thử + license (Phase 66–69)

Tải miễn phí từ GitHub Releases → dùng thử đủ tính năng N ngày → mua đứt → dán license key, 2 máy. AI chạy trên thứ
người dùng đã có. Chi tiết + bảng "họ làm gì → mình làm gì": [Tổng quan Version 10](version-10.md).

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">66</span>
<div class="step__body">
<h3>Mô hình tiền <span class="chip chip--todo">Chưa làm</span></h3>
<p>Mua đứt, giá bậc thang có / không, dùng thử bao nhiêu ngày, hết hạn còn dùng được gì — giá đo từ đối thủ + số fake-door.</p>
<a class="go" href="phase-66-money-model/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">67</span>
<div class="step__body">
<h3>Thanh toán + license key <span class="chip chip--todo">Chưa làm</span></h3>
<p>Lemon Squeezy checkout + API license key: kích hoạt, kiểm lại, gỡ máy. Không webhook, không server riêng.</p>
<a class="go" href="phase-67-payments/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">68</span>
<div class="step__body">
<h3>Dùng thử + paywall <span class="chip chip--todo">Chưa làm</span></h3>
<p>Đếm ngày dùng thử trên máy, thanh "còn X ngày", màn mua + nhập key, tìm lại key bằng email, dữ liệu cũ vẫn xuất được.</p>
<a class="go" href="phase-68-paywall-trial/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">69</span>
<div class="step__body">
<h3>AI của người dùng <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gọi Claude Code / Codex / Ollama / key riêng; nút Kiểm tra hỏi thử 1 câu; mình không bán lượt AI.</p>
<a class="go" href="phase-69-ai-cost-plans/">Xem chi tiết →</a>
</div>
</div>
</div>

Xong Version 10 → gói thành app Mac + Windows: [App Mac + Windows](../app/index.md) (Phase 75 → 79 → 82 → 81).

## Version 11 · Marketing (Phase 70–73)

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">V11</span>
<div class="step__body">
<h3>Marketing Plan <span class="chip chip--todo">Phase 70–73</span></h3>
<p>Định vị + landing + email, 2 kênh chọn bằng ICE, dogfood báo cáo niche công khai, lịch 6 tuần + luật dừng. Landing có nút tải Mac + Windows, MCP là điểm bán.</p>
<a class="go" href="version-11/">Xem chi tiết →</a>
</div>
</div>
</div>

## Version 2 · demo + nguồn mới + AI (Phase 31a, 31–35)

Làm sau khi app đã bán (Version 10 + App + Version 11), vào app qua bản cập nhật. Version 2 mở đầu bằng **trang demo tĩnh** để đi show hàng (29a), rồi thêm nguồn
YouTube, Amazon, Google Maps — mỗi nguồn một phase **cào số (không AI)** rồi một phase **AI đọc chữ**.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">31a</span>
<div class="step__body">
<h3>Demo Site — show hàng <span class="chip chip--todo">Chưa làm</span></h3>
<p>UI thật trên dữ liệu chụp sẵn, trang tĩnh Cloudflare Pages, không server. Muốn xài thật → để email + tải app. Host server để phase sau.</p>
<a class="go" href="phase-31a-demo-site/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">31</span>
<div class="step__body">
<h3>YouTube Search <span class="chip chip--todo">Chưa làm</span></h3>
<p>Cào gợi ý YouTube + top video mỗi keyword: view, độ mới, kênh nhỏ thắng kênh to — không AI. Tuỳ chọn: MCP bên thứ 3 (vidIQ…) cho lượt tìm + độ cạnh tranh.</p>
<a class="go" href="phase-31-youtube-search/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">32</span>
<div class="step__body">
<h3>YouTube Research (AI) <span class="chip chip--todo">Chưa làm</span></h3>
<p>AI đọc phụ đề + comment: người xem than gì, xin gì, dùng tool nào — trích dẫn kèm mốc giây.</p>
<a class="go" href="phase-32-youtube-ai/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">33</span>
<div class="step__body">
<h3>Amazon Search <span class="chip chip--todo">Chưa làm</span></h3>
<p>Cào gợi ý Amazon + top sản phẩm: giá, sao, số review, BSR — không AI, gọi rất thưa.</p>
<a class="go" href="phase-33-amazon-search/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">34</span>
<div class="step__body">
<h3>Amazon Research (AI) <span class="chip chip--todo">Chưa làm</span></h3>
<p>Claude in Chrome đọc review 1–3★: người mua chê gì, ước gì, chỗ một app làm tốt hơn.</p>
<a class="go" href="phase-34-amazon-ai/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">35</span>
<div class="step__body">
<h3>Google Maps Research (AI) <span class="chip chip--todo">Chưa làm</span></h3>
<p>Đếm cửa hàng theo loại × thành phố, AI đọc review → việc chủ quán đang làm tay, app làm thay được.</p>
<a class="go" href="phase-35-google-maps/">Xem chi tiết →</a>
</div>
</div>
</div>

## Version 3 · So sánh + AI Cite (Phase 37–40)

Chọn giữa nhiều niche / đối thủ trên một màn, hỏi dữ liệu bằng lời — AI chỉ trả lời từ DB, **mọi câu có trích dẫn và
máy tự kiểm**. So sánh niche (Phase 28) đã dời lên Version 1. Chi tiết: [Tổng quan Version 3](version-3.md).

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">37</span>
<div class="step__body">
<h3>So sánh đối thủ <span class="chip chip--todo">Chưa làm</span></h3>
<p>2–5 đối thủ cạnh nhau: giá, sao, tính năng, bị chê gì, chỗ trống chưa ai làm tốt — không AI.</p>
<a class="go" href="phase-37-compare-competitor/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">38</span>
<div class="step__body">
<h3>Hỏi dữ liệu (AI Cite) <span class="chip chip--todo">Chưa làm</span></h3>
<p>Hỏi bằng lời, AI trả lời chỉ từ DB, mọi câu có trích dẫn — máy tự kiểm từng trích dẫn.</p>
<a class="go" href="phase-38-ai-cite-ask/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">39</span>
<div class="step__body">
<h3>Báo cáo so sánh (AI Cite) <span class="chip chip--todo">Chưa làm</span></h3>
<p>AI viết kết luận cho bảng so sánh, còn cờ đỏ thì không xuất; ra evidence pack cho /app-research.</p>
<a class="go" href="phase-39-ai-cite-report/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">40</span>
<div class="step__body">
<h3>Review Version 3 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Chọn niche thật 3 lần (≤ 30 phút/lần), sửa lỗi.</p>
<a class="go" href="phase-40-review-3/">Xem chi tiết →</a>
</div>
</div>
</div>

## Version 4 · LLM + AEO, GEO, SEO (Phase 41–45)

Người dùng ngày càng hỏi Google và AI thay vì lên store. Thêm **kệ Google** (ai đứng top 10) và **kệ AI** (ChatGPT /
Gemini / Claude gợi ý app nào, trích trang nào) vào lúc chọn niche. Chi tiết: [Tổng quan Version 4](version-4.md).

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">41</span>
<div class="step__body">
<h3>Kệ Google (SEO) <span class="chip chip--todo">Chưa làm</span></h3>
<p>Top 10 Google của keyword chính, loại trang đứng top (forum, blog nhỏ = dễ chen), bộ câu hỏi người dùng — không AI.</p>
<a class="go" href="phase-41-seo-shelf/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">42</span>
<div class="step__body">
<h3>Kệ AI (GEO / AEO) <span class="chip chip--todo">Chưa làm</span></h3>
<p>Hỏi Gemini · ChatGPT · Claude như người dùng, đếm app được nhắc và trang được trích bằng regex.</p>
<a class="go" href="phase-42-ai-shelf/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">43</span>
<div class="step__body">
<h3>Chỗ trống AI + SEO <span class="chip chip--todo">Chưa làm</span></h3>
<p>Điểm kệ yếu theo công thức cố định, thêm cột Kệ Google + Kệ AI vào so sánh niche.</p>
<a class="go" href="phase-43-ai-seo-gap/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">44</span>
<div class="step__body">
<h3>Gói GEO + trang cần viết <span class="chip chip--todo">Chưa làm</span></h3>
<p>Xuất questions.tsv + brands.tsv cho geo.py và danh sách trang cần viết — cầu nối sang ra mắt.</p>
<a class="go" href="phase-44-geo-pack/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">45</span>
<div class="step__body">
<h3>Review Version 4 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Chọn niche thật 3 lần có kệ Google + kệ AI, sửa lỗi.</p>
<a class="go" href="phase-45-review-4/">Xem chi tiết →</a>
</div>
</div>
</div>

## Version 12 · Tính năng mới

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">V12</span>
<div class="step__body">
<h3>New Features — Just Planned <span class="chip chip--todo">chưa đánh số</span></h3>
<p>Danh sách ứng viên + cách chấm điểm; chọn ≤ 3 mỗi đợt, anh duyệt mới tách thành phase.</p>
<a class="go" href="version-12/">Xem chi tiết →</a>
</div>
</div>
</div>

<hr class="nr-skip-line">

## ⛔ KO LÀM — mọi phase dưới đây (chốt 2026-10-26)

Không ra tiền, không thêm người dùng: tài khoản, performance, test tự động, CI, security / refactor. Trang giữ lại để
tra, không code. Muốn làm lại → kéo lên trên vạch, sửa Master Plan trước. Danh sách + lý do: [Appendix](../appendix.md#khong-lam-chot-2026-10-26).

<div class="steps nr-phases nr-skip" markdown>
<div class="step" markdown>
<span class="step__n">30</span>
<div class="step__body">
<h3>Account + Flow người dùng <span class="chip chip--skip">Không làm</span></h3>
<p>Tài khoản, luồng người dùng mới — bỏ, app bán bằng license key.</p>
<a class="go" href="phase-30-account/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">59</span>
<div class="step__body">
<h3>Lớp tài khoản trên máy <span class="chip chip--skip">Không làm</span></h3>
<p>Hồ sơ người dùng trên máy — bỏ cùng Account.</p>
<a class="go" href="phase-59-local-account/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">62</span>
<div class="step__body">
<h3>Firebase Auth <span class="chip chip--skip">Không làm</span></h3>
<p>Đăng nhập Google / Apple / email link — bỏ.</p>
<a class="go" href="phase-62-firebase-auth/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">63</span>
<div class="step__body">
<h3>Sync project <span class="chip chip--skip">Không làm</span></h3>
<p>Project lên Firestore — bỏ, xuất / nhập file (Phase 8) là đủ.</p>
<a class="go" href="phase-63-project-sync/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">V5</span>
<div class="step__body">
<h3>Performance <span class="chip chip--skip">Không làm</span></h3>
<p>Đo mốc, collector nhanh hơn, UI + DB nhanh (Phase 46–48).</p>
<a class="go" href="version-5/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">V6</span>
<div class="step__body">
<h3>Automation Test + Review Results <span class="chip chip--skip">Không làm</span></h3>
<p>Fixture, E2E, canary nguồn thật, review kết quả (Phase 50–53b). Test đang có vẫn chạy trước khi merge.</p>
<a class="go" href="version-6/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">V7</span>
<div class="step__body">
<h3>CI cho PR <span class="chip chip--skip">Không làm</span></h3>
<p>GitHub Actions chặn PR đỏ, quy trình nhánh (Phase 54, 57).</p>
<a class="go" href="version-7/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">V8</span>
<div class="step__body">
<h3>Security & Refactor <span class="chip chip--skip">Không làm</span></h3>
<p>Kiểm + vá bảo mật, refactor, review 8.0 (Phase 58, 60, 61). Bảo mật tối thiểu cho app bán nằm ở Phase 79.</p>
<a class="go" href="version-8/">Xem chi tiết →</a>
</div>
</div>
</div>

