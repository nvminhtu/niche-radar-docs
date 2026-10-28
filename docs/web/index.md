# Web — làm + test tính năng (chạy local)

> Mọi tính năng làm và **test** ở **bản Web chạy local** (`web/`, `npm run dev` → `localhost:3200`). Khách nhận
> **app Mac + Windows** bọc đúng giao diện này: [App Mac + Windows](../app/index.md).
>
> **Số phase = thứ tự làm (đánh số lại 2026-10-26):** đã xong 1–16 → Hoàn thiện Web trước bản bán 18–26 → AI 27–28 →
> bán 29–37 (Version 9 + 10 + app) → Hoàn thiện Web sau bản bán 38–45 → Version 11 (46–49) → Version 2, 3, 4 (50–63).
> Phase không làm bỏ số, thành **Backlog 01–21** dưới vạch ⛔ KO LÀM. Link số cũ vẫn mở được (tự chuyển trang).

<span class="chip chip--doing">Hoàn thiện Web 18–26 xong 2026-10-26 (bản 0.10.0) · AI 27 + 28 xong 2026-10-27 (phần còn → Backlog 22–25) → bán 29–37</span>

Mỗi phase đi theo [Quy trình build](../quy-trinh-build.md). Việc ngoài plan → [Appendix](../appendix.md).

## Đã xong (Phase 1–17)

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
<span class="step__n">10</span>
<div class="step__body">
<h3>Đa ngôn ngữ (i18n) <span class="chip chip--done">Khung xong 2026-10-25</span></h3>
<p>Chữ giao diện tách ra file theo ngôn ngữ (Tiếng Việt · English · Español), ô chọn ngôn ngữ ở header + Cài đặt. Thiếu bản dịch thì hiện tiếng Anh rồi tiếng Việt. Dịch dần từng trang khi cần.</p>
<a class="go" href="phase-10-i18n/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">11</span>
<div class="step__body">
<h3>Reddit Gap <span class="chip chip--todo">Tạm dừng · Reddit tắt RSS 11/2026, đóng API 3/2027 → thay bằng Phase 12 + 13</span></h3>
<p>Lưu trang Reddit bằng Chrome (JSON hoặc HTML), nhập vào trang Reddit Gap → xếp chuyên mục + chủ đề, đếm chủ đề hỏi nhiều, quan tâm nhiều, chưa ai giải, kèm link bài gốc và xuất .md.</p>
<a class="go" href="phase-11-reddit-gap/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">12</span>
<div class="step__body">
<h3>Q&amp;A Gap (Stack Exchange + Hacker News) <span class="chip chip--done">Xong 2026-10-26</span></h3>
<p>Câu xin phần mềm / hỏi cách làm từ Ask Different, Super User, Software Recs và Ask HN qua API miễn phí, không key. Xếp chung chủ đề với Reddit Gap, thêm lượt xem và cờ "đã có câu trả lời được chấp nhận"; tab Gộp cộng các nguồn.</p>
<a class="go" href="phase-12-qa-gap/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">13</span>
<div class="step__body">
<h3>GitHub Feature Request Gap <span class="chip chip--done">Xong 2026-10-26</span></h3>
<p>Issue nhiều 👍 của nhóm repo app Mac menu bar, app Mac, Chrome extension, plugin Obsidian → tính năng người dùng xin mà maintainer từ chối hoặc để treo, gom theo chủ đề và repo.</p>
<a class="go" href="phase-13-github-gap/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">14</span>
<div class="step__body">
<h3>Research nguồn tìm gap <span class="chip chip--done">Xong 2026-10-26 · chờ duyệt top 3</span></h3>
<p>Chỉ research, chưa code: liệt kê mọi nơi dev / indie tìm gap + keyword niche (Pinterest Trends, Product Hunt, Hacker News…), chấm mức độ và nên làm hay không; gom MCP free / trả phí, tool scrape, repo GitHub dùng kèm, và phương pháp tìm gap / niche anh chưa biết.</p>
<a class="go" href="phase-14-gap-sources/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">15</span>
<div class="step__body">
<h3>Export (CSV, JSON, gói cho LLM) <span class="chip chip--done">Xong 2026-10-27 · kiểm Google Sheets → Backlog 22</span></h3>
<p>Một hộp Xuất chung: CSV mở đúng trên Excel / Sheets, JSON có schema, Markdown, gói LLM (brief + schema + prompt) cắt theo trần token.</p>
<a class="go" href="phase-15-export/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">16</span>
<div class="step__body">
<h3>Bàn quyết định long-tail + đo nhu cầu Pro <span class="chip chip--done">Xong 2026-10-26 · fake-door live trên demo</span></h3>
<p>Chấm các keyword trong Project theo rubric 5 trục có dẫn chứng, Copy prompt cho AI rồi dán JSON ngược, ra BUILD / TEST THÊM / BỎ. Kèm 2 nút Pro giả (fake-door) đo có ai muốn trả tiền.</p>
<a class="go" href="phase-16-decision-board/">Xem chi tiết →</a>
</div>
</div>
</div>

## Hoàn thiện Web · trước bản bán (Phase 18–26)

Người mua mở app ra là thấy những chỗ này — phải xong trước bản bán đầu. Mỗi tính năng chính có bản đầu ở Phase 1–16,
phase ở đây làm kỹ: đủ dữ liệu, giải thích được, có "Xong khi" đo được. Phase 26 soát lại cả cụm.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">HW</span>
<div class="step__body">
<h3>Tổng quan Hoàn thiện Web <span class="chip chip--doing">Đang làm</span></h3>
<p>Gom mọi việc Web dang dở: việc chờ chạy thật · 9 phase trước bản bán (18–26) · 8 phase sau bản bán (38–45).</p>
<a class="go" href="../app/hoan-thien-web/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">18</span>
<div class="step__body">
<h3>Đối thủ bị chê gì <span class="chip chip--done">Xong 2026-10-26</span></h3>
<p>Gộp lời chê cùng ý, chia loại (lỗi · mất dữ liệu · ép trả phí · quảng cáo · thiếu tính năng…), bảng app × lời chê, lời chê mới nổi, danh sách "người dùng ước gì" — không AI.</p>
<a class="go" href="phase-18-competitor-complaints/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">19</span>
<div class="step__body">
<h3>Ai là khách hàng <span class="chip chip--done">Xong 2026-10-26</span></h3>
<p>Loại khách theo vai (trẻ em, phụ huynh, giáo viên, người ADHD…) từ keyword · review · đối thủ · Reddit / Q&amp;A, bảng loại khách có dẫn chứng, điền mục Đối tượng của evidence pack. Không đoán giới tính / độ tuổi.</p>
<a class="go" href="phase-19-ai-la-khach/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">20</span>
<div class="step__body">
<h3>Chấm sức khoẻ niche <span class="chip chip--done">Xong 2026-10-26 · back-test chờ kết quả thật</span></h3>
<p>Mở từng yếu tố ra công thức + nguồn, độ tin hiện to, cờ chặn ép xuống TEST THÊM / BỎ, ngưỡng do anh đặt, back-test với niche đã biết kết quả.</p>
<a class="go" href="phase-20-niche-health/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">21</span>
<div class="step__body">
<h3>Collect niche vào Project <span class="chip chip--done">Xong 2026-10-26</span></h3>
<p>Gom từ mọi chỗ (keyword, đối thủ, lời chê, ô trống tính năng), gom hàng loạt, tạo project ngay trong popover, chụp số lúc gom, không trùng, hoàn tác.</p>
<a class="go" href="phase-21-collect/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">22</span>
<div class="step__body">
<h3>Quản lý Project <span class="chip chip--done">Xong 2026-10-26</span></h3>
<p>Tìm / lọc / thẻ / lưu trữ / nhân bản / gộp project, trang project chia tab, lý do loại bắt buộc, bước tiếp + ngày hẹn, nhật ký.</p>
<a class="go" href="phase-22-project-manage/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">23</span>
<div class="step__body">
<h3>Research 1 keyword — trang kết quả <span class="chip chip--done">Xong 2026-10-26</span></h3>
<p>Đầu trang là câu trả lời (5 con số), khối xếp theo câu hỏi chọn niche, trạng thái + chạy lại từng nguồn, so với lần tra trước.</p>
<a class="go" href="phase-23-research-page/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">24</span>
<div class="step__body">
<h3>Setup ngay trong Web <span class="chip chip--done">Xong 2026-10-26</span></h3>
<p>Hướng dẫn cài đúng máy, nút Kiểm tra máy báo thiếu gì + gói cài, nút Hỏi AI (ChatGPT · Gemini · Claude).</p>
<a class="go" href="phase-24-setup/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">25</span>
<div class="step__body">
<h3>UI / UX Improvement <span class="chip chip--done">Xong 2026-10-26</span></h3>
<p>Sửa chỗ vướng thật: luồng chính, trạng thái tải / lỗi, bảng dày, sáng / tối.</p>
<a class="go" href="phase-25-ui-ux/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">26</span>
<div class="step__body">
<h3>Review cụm tính năng chính <span class="chip chip--done">Xong 2026-10-26 · bản 0.10.0</span></h3>
<p>Soát Phase 18–25 + 27–28 đợt 1 trên 5 niche thật, phiếu soát từng phase, sửa lỗi, cập nhật Hướng dẫn / About, ra bản Web mới.</p>
<a class="go" href="phase-26-review-core/">Xem chi tiết →</a>
</div>
</div>
</div>

## AI (Phase 27–28)

AI là của người dùng (Claude Code, Codex, key riêng…), app không bán AI. Tắt AI vẫn chạy đủ phần không AI.
Các phase AI cũ gộp vào đây thành trang con: 27.3 MCP · 27.4 Hỏi dữ liệu · 27.6 Cài đặt AI · 27.7 AI của người dùng · 28.1 Tóm tắt niche.
Chốt 2026-10-27: 27, 28, 28.2, 28.6 xong; 27.4, 27.6, 28.1, 28.3, 28.5 và phần còn dời xuống [Backlog · làm sau](#backlog-lam-sau); 28.4 làm tiếp phần UI dễ.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">27</span>
<div class="step__body">
<h3>AI của bạn — Claude Code, Codex trong app <span class="chip chip--done">Xong 2026-10-27 · Terminal nhúng + sổ dùng AI → Backlog 23</span></h3>
<p>Cầu AI gọi AI người dùng đã có, thư mục AI có sẵn skill, MCP của app (27.3), khung chat (27.4), Cài đặt AI (27.6, 27.7), terminal nhúng.</p>
<a class="go" href="../app/phase-27-ai-cua-ban/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">27.3</span>
<div class="step__body">
<h3>MCP của app <span class="chip chip--done">Xong đợt 1 · 2026-10-26</span></h3>
<p>MCP server chỉ đọc để Claude tự đọc DB: tìm niche, so niche, đối thủ, lời chê, project — trả kèm nguồn.</p>
<a class="go" href="phase-27-3-mcp/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">27.7</span>
<div class="step__body">
<h3>AI của người dùng <span class="chip chip--done">Xong · 2026-10-27</span></h3>
<p>Gọi Claude Code / Codex / key riêng; nút Kiểm tra hỏi thử 1 câu; mình không bán lượt AI.</p>
<a class="go" href="phase-27-7-ai-cost-plans/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">28</span>
<div class="step__body">
<h3>AI cho từng tính năng <span class="chip chip--done">Xong 2026-10-27 · 2/4 nút đợt 1 + AI Agent · phần còn → Backlog 24</span></h3>
<p>Đợt 1: tóm tắt niche 1 bấm (28.1) · bàn quyết định 1 bấm · gap → ý tưởng app · Feature Gap tự điền; đợt 2 vào bằng bản cập nhật.</p>
<a class="go" href="../app/phase-28-ai-tinh-nang/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">28.2</span>
<div class="step__body">
<h3>MCP đợt 2 — AI cập nhật niche, project, gap <span class="chip chip--done">Xong 2026-10-27 · 6 tool mức Thêm · phần còn → Backlog 25</span></h3>
<p>AI bên ngoài tra niche mới, gom vào project, xếp gap (thêm có hoàn tác · đề xuất chờ Dùng) + nhóm việc health_niche_check, health_project_check, brief_pack.</p>
<a class="go" href="phase-28-2-mcp-write/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">28.4</span>
<div class="step__body">
<h3>Nút AI đũa phép ở từng bước <span class="chip chip--doing">Đang làm · 2026-10-27 · chỗ UI dễ làm trước</span></h3>
<p>Nút ✦ ở mỗi bước đi tay: AI mặc định nhận đúng ngữ cảnh đang xem + chạy đúng skill. Làm trước các chỗ chỉ cần gắn nút vào khung có sẵn.</p>
<a class="go" href="phase-28-4-ai-magic/">Xem chi tiết →</a>
</div>
</div>
</div>


## Phase 28.7 · AI Agent dễ nhìn

<span class="chip chip--done">Xong 2026-10-28 · T1–T7 bản gọn</span>

Tiếp nối [Phase 28.6 · AI Agent](phase-28-6-ai-agent.md): hiện AI và model thật, đóng/mở hướng dẫn,
menu lệnh theo dữ liệu, chuyển bước có điều kiện và dấu ✦ thống nhất.

[Xem plan Phase 28.7 →](phase-28-7-ai-agent-ux.md)

## Phase 28.8 · Trang niche + Explorer

<span class="chip chip--done">Xong 2026-10-28 · D · E · B · C · A</span>

Ưu tiên sửa cuộn bảng/cây và trạng thái rỗng có nút; thu gọn giải thích, làm rõ điểm và độ phủ,
biến TEST MORE / BUILD / SKIP thành bước tiếp có điều kiện. Không đổi công thức tính.

[Xem plan Phase 28.8 →](phase-28-8-niche-ui-polish.md)

## Phase 28.9 · AI Agent xịn — xuất .md, gợi ý gập, chat có nút

<span class="chip chip--done">Xong 2026-10-28 · T1–T7</span>

Thêm bước Plan và tải Brief / Spec / Plan thành file `.md` (từng file + cả bộ, có bảng nguồn); gợi ý dài gập còn 1 câu
có nút ⓘ; chat trả lời có format, nút hành động một bấm và ô nhập chọn model tại chỗ — học khung Wow Keywords.

[Xem plan Phase 28.9 →](phase-28-9-ai-agent-pro.md)

## Phase 28.10 · Bàn quyết định nhìn là hiểu

<span class="chip chip--done">Xong 2026-10-28 · phương án B (2 đèn)</span>

Mỗi keyword mở đầu bằng 2 dòng trả lời: **Nên làm không?** và **Độ phủ keyword dày hay thưa** (lấy từ điểm v2 sẵn có);
mỗi trục 1 hàng icon · mức màu · 1 con số; dẫn chứng và chấm tay 1–5 gập vào Chi tiết. Không đổi công thức.

[Xem plan Phase 28.10 →](phase-28-10-decision-board-easy.md)

## Bán · Version 9 + 10 + app (Phase 29–37)

Đo người tải app đi tới đâu (mở → dùng thử → tra niche → nhập license) và biết khi app lỗi. **Không tài khoản**: app
bán bằng license key, dữ liệu ở máy — học [Wow Keywords](../doi-thu-tham-khao.md#wow-keywords). Chi tiết: [Tổng quan Version 9](version-9.md).

Tải miễn phí từ GitHub Releases → dùng thử đủ tính năng N ngày → mua đứt → dán license key, 2 máy. AI chạy trên thứ
người dùng đã có. Chi tiết + bảng "họ làm gì → mình làm gì": [Tổng quan Version 10](version-10.md).

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">29</span>
<div class="step__body">
<h3>Analytics + báo lỗi <span class="chip chip--done">Xong</span></h3>
<p>6 sự kiện phễu + báo lỗi qua GA4, hỏi đồng ý lần đầu, không gửi chữ gõ. Dùng thử / license thêm ở Version 10.</p>
<a class="go" href="phase-29-analytics-errors/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">30</span>
<div class="step__body">
<h3>Trang Riêng tư <span class="chip chip--done">Xong</span></h3>
<p>shotmatic.app/privacy ghi đúng 6 sự kiện app gửi, link trong app. Phần xoá tài khoản bỏ.</p>
<a class="go" href="phase-30-privacy-delete/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">31</span>
<div class="step__body">
<h3>Mô hình tiền <span class="chip chip--todo">Chưa làm</span></h3>
<p>Mua đứt, giá bậc thang có / không, dùng thử bao nhiêu ngày, hết hạn còn dùng được gì — giá đo từ đối thủ + số fake-door.</p>
<a class="go" href="phase-31-money-model/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">32</span>
<div class="step__body">
<h3>Thanh toán + license key <span class="chip chip--todo">Chưa làm</span></h3>
<p>Lemon Squeezy checkout + API license key: kích hoạt, kiểm lại, gỡ máy. Không webhook, không server riêng.</p>
<a class="go" href="phase-32-payments/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">33</span>
<div class="step__body">
<h3>Dùng thử + paywall <span class="chip chip--todo">Chưa làm</span></h3>
<p>Đếm ngày dùng thử trên máy, thanh "còn X ngày", màn mua + nhập key, tìm lại key bằng email, dữ liệu cũ vẫn xuất được.</p>
<a class="go" href="phase-33-paywall-trial/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">34–37</span>
<div class="step__body">
<h3>App Mac + Windows: bản bán đầu → phần riêng app → Windows → auto-update <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gói bản Web + Version 9 + 10 vào app Mac (33), phần riêng của app (34), app Windows Beta (35), release + cập nhật tự động (36).</p>
<a class="go" href="../app/">Xem chi tiết →</a>
</div>
</div>
</div>

## Version 11 · Marketing (Phase 46–49)

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">V11</span>
<div class="step__body">
<h3>Marketing Plan <span class="chip chip--todo">Phase 46–49</span></h3>
<p><a href="phase-46-positioning-landing/">46 Landing shotmatic.app ✅</a> (định vị + email) · <a href="phase-46-1-landing-blog/">46.1 Blog shotmatic.app (SEO · AEO · GEO)</a> · 2 kênh chọn bằng ICE, dogfood báo cáo niche công khai, lịch 6 tuần + luật dừng. Landing có nút tải Mac + Windows, MCP là điểm bán.</p>
<a class="go" href="version-11/">Xem chi tiết →</a>
</div>
</div>
</div>

## Version 2 · Demo + nguồn mới + AI (Phase 50–55)

Làm sau khi app đã bán (Version 10 + App + Version 11), vào app qua bản cập nhật. Version 2 mở đầu bằng **trang demo tĩnh** để đi show hàng (Phase 50), rồi thêm nguồn
YouTube, Amazon, Google Maps — mỗi nguồn một phase **cào số (không AI)** rồi một phase **AI đọc chữ**.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">50</span>
<div class="step__body">
<h3>Demo Site — show hàng <span class="chip chip--todo">Chưa làm</span></h3>
<p>UI thật trên dữ liệu chụp sẵn, trang tĩnh Cloudflare Pages, không server. Muốn xài thật → để email + tải app. Host server để phase sau.</p>
<a class="go" href="phase-50-demo-site/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">51</span>
<div class="step__body">
<h3>YouTube Search <span class="chip chip--todo">Chưa làm</span></h3>
<p>Cào gợi ý YouTube + top video mỗi keyword: view, độ mới, kênh nhỏ thắng kênh to — không AI. Tuỳ chọn: MCP bên thứ 3 (vidIQ…) cho lượt tìm + độ cạnh tranh.</p>
<a class="go" href="phase-51-youtube-search/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">52</span>
<div class="step__body">
<h3>YouTube Research (AI) <span class="chip chip--todo">Chưa làm</span></h3>
<p>AI đọc phụ đề + comment: người xem than gì, xin gì, dùng tool nào — trích dẫn kèm mốc giây.</p>
<a class="go" href="phase-52-youtube-ai/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">53</span>
<div class="step__body">
<h3>Amazon Search <span class="chip chip--todo">Chưa làm</span></h3>
<p>Cào gợi ý Amazon + top sản phẩm: giá, sao, số review, BSR — không AI, gọi rất thưa.</p>
<a class="go" href="phase-53-amazon-search/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">54</span>
<div class="step__body">
<h3>Amazon Research (AI) <span class="chip chip--todo">Chưa làm</span></h3>
<p>Claude in Chrome đọc review 1–3★: người mua chê gì, ước gì, chỗ một app làm tốt hơn.</p>
<a class="go" href="phase-54-amazon-ai/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">55</span>
<div class="step__body">
<h3>Google Maps Research (AI) <span class="chip chip--todo">Chưa làm</span></h3>
<p>Đếm cửa hàng theo loại × thành phố, AI đọc review → việc chủ quán đang làm tay, app làm thay được.</p>
<a class="go" href="phase-55-google-maps/">Xem chi tiết →</a>
</div>
</div>
</div>

## Version 3 · So sánh + AI Cite (Phase 56–58)

Chọn giữa nhiều niche / đối thủ trên một màn, hỏi dữ liệu bằng lời — AI chỉ trả lời từ DB, **mọi câu có trích dẫn và
máy tự kiểm**. So sánh niche đã dời lên Phase 44, Hỏi dữ liệu gộp vào Phase 27.4. Chi tiết: [Tổng quan Version 3](version-3.md).

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">56</span>
<div class="step__body">
<h3>So sánh đối thủ <span class="chip chip--todo">Chưa làm</span></h3>
<p>2–5 đối thủ cạnh nhau: giá, sao, tính năng, bị chê gì, chỗ trống chưa ai làm tốt — không AI.</p>
<a class="go" href="phase-56-compare-competitor/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">57</span>
<div class="step__body">
<h3>Báo cáo so sánh (AI Cite) <span class="chip chip--todo">Chưa làm</span></h3>
<p>AI viết kết luận cho bảng so sánh, còn cờ đỏ thì không xuất; ra evidence pack cho /app-research.</p>
<a class="go" href="phase-57-ai-cite-report/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">58</span>
<div class="step__body">
<h3>Review Version 3 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Chọn niche thật 3 lần (≤ 30 phút/lần), sửa lỗi.</p>
<a class="go" href="phase-58-review-3/">Xem chi tiết →</a>
</div>
</div>
</div>

## Version 4 · LLM + AEO, GEO, SEO (Phase 59–63)

Người dùng ngày càng hỏi Google và AI thay vì lên store. Thêm **kệ Google** (ai đứng top 10) và **kệ AI** (ChatGPT /
Gemini / Claude gợi ý app nào, trích trang nào) vào lúc chọn niche. Chi tiết: [Tổng quan Version 4](version-4.md).

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">59</span>
<div class="step__body">
<h3>Kệ Google (SEO) <span class="chip chip--todo">Chưa làm</span></h3>
<p>Top 10 Google của keyword chính, loại trang đứng top (forum, blog nhỏ = dễ chen), bộ câu hỏi người dùng — không AI.</p>
<a class="go" href="phase-59-seo-shelf/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">60</span>
<div class="step__body">
<h3>Kệ AI (GEO / AEO) <span class="chip chip--todo">Chưa làm</span></h3>
<p>Hỏi Gemini · ChatGPT · Claude như người dùng, đếm app được nhắc và trang được trích bằng regex.</p>
<a class="go" href="phase-60-ai-shelf/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">61</span>
<div class="step__body">
<h3>Chỗ trống AI + SEO <span class="chip chip--todo">Chưa làm</span></h3>
<p>Điểm kệ yếu theo công thức cố định, thêm cột Kệ Google + Kệ AI vào so sánh niche.</p>
<a class="go" href="phase-61-ai-seo-gap/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">62</span>
<div class="step__body">
<h3>Gói GEO + trang cần viết <span class="chip chip--todo">Chưa làm</span></h3>
<p>Xuất questions.tsv + brands.tsv cho geo.py và danh sách trang cần viết — cầu nối sang ra mắt.</p>
<a class="go" href="phase-62-geo-pack/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">63</span>
<div class="step__body">
<h3>Review Version 4 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Chọn niche thật 3 lần có kệ Google + kệ AI, sửa lỗi.</p>
<a class="go" href="phase-63-review-4/">Xem chi tiết →</a>
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

## Backlog · làm sau { #backlog-lam-sau }

Việc còn dở của phase đã chốt xong, và phase dời ra sau để làm xong bản Web (2026-10-27). Chưa đánh số phase mới —
lúc làm thì tách thành phase.

- [Backlog 22 · Export: CSV trên Google Sheets](phase-backlog-22-export-sheets.md) — từ Phase 15
- [Backlog 23 · Terminal nhúng + sổ dùng AI](phase-backlog-23-ai-terminal-usage.md) — từ Phase 27
- [Backlog 24 · Nút AI còn lại](phase-backlog-24-ai-buttons-rest.md) — từ Phase 28
- [Backlog 25 · MCP đợt 2 phần còn](phase-backlog-25-mcp-write-rest.md) — từ Phase 28.2
- Phase dời nguyên trang: [27.4 Hỏi dữ liệu](phase-27-4-ai-cite-ask.md) · [27.6 Cài đặt AI](phase-27-6-ai-settings.md) ·
  [28.1 Tóm tắt niche](phase-28-1-ai-summary.md) · [28.3 Bộ skill](phase-28-3-skills.md) ·
  [28.5 Brief + Spec + Plan](phase-28-5-brief-plan.md)
- [Phase 17 · Local App 1.0](../app/phase-17-local-app-1.md) — tạm dừng, lên plan phase mới khi bản Web xong

### Hoàn thiện Web · sau bản bán (Phase 38–45) — dời xuống 2026-10-28

Anh chốt 2026-10-28: chưa làm, để Backlog. 40–43 đã có một phần trong app — giữ nguyên, không code tiếp.

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">38</span>
<div class="step__body">
<h3>Doanh thu thật: TrustMRR + nguồn khác + AI <span class="chip chip--todo">Backlog · chưa làm</span></h3>
<p>Bước 0 chọn nguồn doanh thu công khai, AI khớp tên đối thủ, dòng verified đủ trường, ước theo bậc tách riêng, bảng "Ai đang thu tiền".</p>
<a class="go" href="phase-38-revenue/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">39</span>
<div class="step__body">
<h3>Backup / restore dữ liệu <span class="chip chip--todo">Backlog · chưa làm</span></h3>
<p>Backup tự động mỗi ngày, giữ 7 ngày · 4 tuần · 6 tháng, kiểm toàn vẹn, thư mục ngoài máy, restore xem trước, restore 1 project.</p>
<a class="go" href="phase-39-backup-restore/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">40</span>
<div class="step__body">
<h3>Explore — cây keyword + bản đồ ngách <span class="chip chip--todo">Backlog · Một phần · có bản đồ ngách</span></h3>
<p>Lọc rác + thương hiệu, gộp keyword cùng nghĩa, thêm gợi ý App Store, điểm cơ hội giải thích được, chọn lá → Research hàng loạt.</p>
<a class="go" href="phase-40-explore-tree/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">41</span>
<div class="step__body">
<h3>Hồ sơ đối thủ + cờ đối thủ yếu <span class="chip chip--todo">Backlog · Chưa xong · có bảng đối thủ</span></h3>
<p>Trang riêng mỗi đối thủ (2 store, nhịp cập nhật, giá, bị chê gì, doanh thu), cờ bỏ bê · bị chê · một store · thu tiền · mới vào.</p>
<a class="go" href="phase-41-competitor-profile/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">42</span>
<div class="step__body">
<h3>Theo dõi niche định kỳ <span class="chip chip--todo">Backlog · Một phần · chụp lại bằng tay</span></h3>
<p>Tự tra lại theo lịch khi server chạy, chỉ báo thay đổi đáng chú ý, hộp "Thay đổi tuần này", dòng thời gian project.</p>
<a class="go" href="phase-42-tracking/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">43</span>
<div class="step__body">
<h3>Evidence pack + test bán trước <span class="chip chip--todo">Backlog · Một phần · có evidence pack</span></h3>
<p>Chạy hết 1 vòng thật: evidence pack đủ khung → /app-demand → ngưỡng ghi trước → số thật → BUILD / TEST THÊM / BỎ.</p>
<a class="go" href="phase-43-evidence-presell/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">44</span>
<div class="step__body">
<h3>So sánh niche <span class="chip chip--skip">Không làm · ẩn khỏi app (code giữ)</span></h3>
<p>2–4 niche cạnh nhau: cơ hội, đối thủ, xu hướng, đau, tiền — tô ô thắng từng hàng, không AI.</p>
<a class="go" href="phase-44-compare-niche/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">45</span>
<div class="step__body">
<h3>Tutorial — nút ? mỗi tính năng <span class="chip chip--skip">Không làm</span></h3>
<p>Bấm ? cạnh tính năng: 1 câu làm gì + 2–4 hình bước đơn giản, ít chữ.</p>
<a class="go" href="phase-45-tutorial/">Xem chi tiết →</a>
</div>
</div>
</div>

<hr class="nr-skip-line">

## ⛔ KO LÀM — Backlog 01–21 (chốt 2026-10-26)

Không ra tiền, không thêm người dùng: tài khoản, performance, test tự động, CI, security / refactor. Bỏ số phase, đánh thành **Backlog 01–21** (Web 01–17, App 18–21). Trang giữ lại để
tra, không code. Muốn làm lại → kéo lên trên vạch, sửa Master Plan trước. Danh sách + lý do: [Appendix](../appendix.md#khong-lam-chot-2026-10-26).

<div class="steps nr-phases nr-skip" markdown>
<div class="step" markdown>
<span class="step__n">B01</span>
<div class="step__body">
<h3>Account + Flow người dùng <span class="chip chip--skip">Không làm</span></h3>
<p>Tài khoản, luồng người dùng mới — bỏ, app bán bằng license key.</p>
<a class="go" href="phase-backlog-01-account/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">B02</span>
<div class="step__body">
<h3>Lớp tài khoản trên máy <span class="chip chip--skip">Không làm</span></h3>
<p>Hồ sơ người dùng trên máy — bỏ cùng Account.</p>
<a class="go" href="phase-backlog-02-local-account/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">B03</span>
<div class="step__body">
<h3>Firebase Auth <span class="chip chip--skip">Không làm</span></h3>
<p>Đăng nhập Google / Apple / email link — bỏ.</p>
<a class="go" href="phase-backlog-03-firebase-auth/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">B04</span>
<div class="step__body">
<h3>Sync project <span class="chip chip--skip">Không làm</span></h3>
<p>Project lên Firestore — bỏ, xuất / nhập file (Phase 8) là đủ.</p>
<a class="go" href="phase-backlog-04-project-sync/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">V5</span>
<div class="step__body">
<h3>Performance <span class="chip chip--skip">Không làm</span></h3>
<p>Đo mốc, collector nhanh hơn, UI + DB nhanh (Backlog 05–07).</p>
<a class="go" href="version-5/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">V6</span>
<div class="step__body">
<h3>Automation Test + Review Results <span class="chip chip--skip">Không làm</span></h3>
<p>Fixture, E2E, canary nguồn thật, review kết quả (Backlog 08–12). Test đang có vẫn chạy trước khi merge.</p>
<a class="go" href="version-6/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">V7</span>
<div class="step__body">
<h3>CI cho PR <span class="chip chip--skip">Không làm</span></h3>
<p>GitHub Actions chặn PR đỏ, quy trình nhánh (Backlog 13–14).</p>
<a class="go" href="version-7/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">V8</span>
<div class="step__body">
<h3>Security & Refactor <span class="chip chip--skip">Không làm</span></h3>
<p>Kiểm + vá bảo mật, refactor, review 8.0 (Backlog 15–17). Bảo mật tối thiểu cho app bán nằm ở Phase 35.</p>
<a class="go" href="version-8/">Xem chi tiết →</a>
</div>
</div>
</div>
