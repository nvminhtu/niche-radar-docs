# niche-radar — Master Plan

> Cập nhật 2026-10-24 (11 phase + Appendix: 1 Google Play · 2 App Store · 3 Google Trends · 4 Feature Gap Matrix · 5 Verified Sites · 6 AI bản Web · 7 Review + Validate · 8 Project + dữ liệu · 9 Feature Plan · 10 UI/UX · 11 Account + Flow = MVP; sau MVP: 12 YouTube Search · 13 YouTube AI · 14 Amazon Search · 15 Amazon AI · 16 Google Maps AI … tới 55; cuối cùng Version 13 App Mac 56–63) · Plan gốc của sản phẩm. Plan code chi tiết từng phase ở `docs/superpowers/plans/`.
> Bản đọc nhanh có sơ đồ: trang chủ của site tài liệu (`npm run docs`).

## 0. Một câu

Gõ một niche → tool tự tra **Google Play, App Store, Google Trends** (+ Reddit) → biết keyword nào còn trống,
đối thủ yếu ở đâu, **ai đang thu tiền thật**, nhu cầu lên hay xuống — trong vài phút. Phase 1–5 chạy không cần AI;
AI vào ở Phase 4 (Feature Gap Matrix, tuỳ chọn) và Phase 6 (tích hợp AI bản Web).

**Định vị:** tool **nội bộ** để chọn niche cho app của mình. Không bán, không host. Thử bán một tool tìm niche là
việc của Idea Lab (repo App-AI-Skills) — chỉ khi Idea Lab qua test mới viết plan mới.

## 1. Sản phẩm có 2 dạng: Web và App

| | **Web** (làm trước) | **App Mac** (làm sau) |
|---|---|---|
| Là gì | Web chạy trên máy: `npm run dev` → `http://localhost:3200` | App mở bằng double-click, không cần gõ lệnh |
| Giao diện | React (Vite) | **Dùng lại đúng giao diện Web**, bọc bằng Tauri (không Electron) |
| Lấy dữ liệu | Server Node (Hono) trong máy | Cùng server Node chạy kèm app (sidecar) |
| Dữ liệu | `data/niche.db` (SQLite) | Cùng định dạng SQLite, nằm trong thư mục app |
| Khi nào | Mọi phase tính năng (Version 1–12, Phase 1–55) | **Version 13, phase cuối cùng**: 56 → 57 → 58 → 59 → 60 → 61 → 62 → 63 (Phase 56 đã code sớm — [spec Local App](2026-10-24-niche-radar-phase8-local-app.md)) — macOS, ký Developer ID + notarize |

Vì App bọc lại Web, mọi tính năng làm ở Web đều có trong App — không viết 2 lần.

## 2. Hệ thống chạy thế nào

```
 Bạn gõ niche ─► Giao diện (React) ─► API (Hono, 127.0.0.1) ─► Collectors ─┬─► Google Play  (scraper)
                       ▲                        │                          ├─► App Store    (iTunes API)
                       │                        ▼                          ├─► Google gợi ý (autocomplete)
                  dashboard,             SQLite data/niche.db  ◄───────────┼─► Google Trends (không chính thức)
                  bản đồ, CSV            (cache 24h / 7 ngày)              ├─► Reddit       (OAuth, tuỳ chọn)
                                                                           ├─► TrustMRR     (Phase 5, doanh thu verified)
                                                                           └─► AI           (Phase 4 · 6, tắt mặc định)
```

Hai luồng:
- **Explore niche:** niche → gợi ý tìm kiếm (Play + Google) → cây ≤ 100 keyword → đếm đối thủ từng keyword →
  điểm cơ hội → bản đồ ngách + Top 10.
- **Research 1 keyword:** keyword → 4 nguồn song song → đối thủ, Trends, Reddit, câu than 1–2★.

## 3. Lộ trình

```
v1 nền ─► 1 Google Play ─► 2 App Store ─► 3 Google Trends ─► 4 Feature Gap Matrix ─► 5 Verified Sites
 XONG       🟡 code xong     🟡 đang làm    🟡 có cơ bản        ⚪                      🟡 đang làm (TrustMRR)

      ─► 6 AI bản Web ─► 7 Review + Validate ─► 9 Small Features Update ─► 18 So sánh niche ─► 10 UI/UX ─► 11 Account + Flow
          ✅ tuyến B       🟡 code xong            ⚪                          ⚪                  ⚪          ⚪

      ─► … Version 2–12 (Phase 13–55, chỉ bản Web) …

Version 13 · App Mac — phase cuối cùng, sau khi hết mọi phase Web:
      56 Local App 1.0 ─► 57 ─► 58 ─► 59 ─► 60 App nhẹ ─► 61 Phần riêng app ─► 62 CI ─► 63 Release
      🟡 code sớm
```

| Phase | Trả lời câu gì | Trạng thái |
|---|---|---|
| v1 — Nền | tra 1 keyword × 4 nguồn ra dashboard | ✅ Xong 2026-10-24 |
| **1 — Google Play** | trên Play, keyword nào còn trống? đối thủ bị chê gì? | 🟡 Code xong, đã ở `main` · làm thêm UI Loading + Flow niche (Task 10–11 plan Phase 1) |
| **2 — App Store** | trên iOS thì sao? giá + gói mua trong app? | 🟡 Code xong, đạt "Xong khi" 3/3 niche (2026-10-24, kết quả trong plan Phase 2) · chờ merge nhánh `phase2-appstore-money` |
| **3 — Google Trends** | nhu cầu lên hay xuống, nước nào, mùa vụ? | 🟡 Có cơ bản từ v1 (12 tháng + related queries cho 1 keyword) |
| **4 — Feature Gap Matrix** | đối thủ thiếu tính năng gì? | ⚪ |
| **5 — Verified Sites** | ai đang thu tiền thật (TrustMRR + trang tương tự)? | 🟡 TrustMRR bản đầu (trang công khai, chưa API key) · nguồn tương tự chưa kiểm |
| **6 — Tích hợp AI (bản Web)** | AI đọc review / Reddit / listing — đường nào rẻ / miễn phí chạy được? | ⚪ Có Bước 0 thử 4 tuyến, chưa chắc làm được hết |
| **7 — Review + Validate** | Phase 1–6 có đạt thật trên niche thật không? niche nào đáng làm, có người trả tiền không? | ⚪ |
| **8 — Project + dữ liệu** (Web; vỏ app tách sang Phase 56) | project có đánh giá, xuất/nhập giữa các máy, backup? | ✅ Xong 2026-10-25 — `docs/web/phase-8-project-data.md` |
| **9 — Small Features Update** | tính năng nhỏ nào đáng làm tiếp? | ✅ 4 mục ưu tiên xong 2026-10-25 — `docs/web/phase-9-small-features.md` · ứng viên khác chưa chốt |
| **18 — So sánh niche** (dời lên 2026-10-25) | 2–4 niche cạnh nhau, niche nào đáng chọn? (không AI) | ⚪ Làm ngay sau Phase 9 |
| **10 — UI / UX Improvement** | chỗ nào dùng còn vướng? | ⚪ |
| **11 — Account + Flow** | người khác dùng được không cần hỏi? góp ý vào đâu? | ⚪ Xét lại trước khi code (cần người dùng ngoài) |
| ─── | **Vạch MVP** — Phase 1–12.2 xong mới sang dưới. Từ đây thêm nguồn mới + AI, chỉ bản Web; app Mac làm sau khi hết mọi phase Web | |
| **12 — YouTube Search** | người ta tìm gì trên YouTube, video nào hút view, kênh nhỏ nào thắng? (không AI) | ⚪ |
| **13 — YouTube Research (AI)** | người xem than gì, xin gì, dùng tool nào? | ⚪ |
| **14 — Amazon Search** | tìm gì trên Amazon, top bán chạy, giá, độ đông? (không AI) | ⚪ |
| **15 — Amazon Research (AI)** | người mua chê gì, ước gì, chỗ app làm tốt hơn? | ⚪ |
| **16 — Google Maps Research (AI)** | cửa hàng địa phương than gì, việc nào app làm thay được? | ⚪ |
| Appendix | việc không làm | — |

Mỗi phase đi đúng 6 bước: 📄 Spec → 🗺️ Plan + 🎨 Mockup → 🔨 Implement → 🔁 Update plan & Implement → 📦 Build → ✅ Test.
Chi tiết: [Quy trình build](../../quy-trinh-build.md). Cuối mỗi phase: dùng thật vài ngày, gom việc vào §4 "Đang pending".
Bản đọc nhanh từng phase (có sơ đồ, "Xong khi", "Không làm"): trang `docs/phase-<n>-*.md`.

### Phase 1 — Google Play

- **Mục tiêu:** từ một niche, mở ra mọi keyword người ta gõ trên Play, chấm điểm từng ngách.
- **Làm:** cây keyword từ gợi ý Play + Google (vòng chữ cái a–z + mẫu `for …`, `widget`, `offline`…), gom 4 nhóm
  (đối tượng / dạng / nền tảng / tính năng), lần đầu ≤ 100 keyword, mở tiếp ≤ 50, sâu ≤ 3 · điểm cơ hội
  `phổ biến × (1 − độ đông)` · bản đồ ngách + Top 10 · research sâu ≤ 5 keyword · CSV · câu than review 1–2★ Play.
- **Làm thêm — UI Loading (trang Research `/r/:id` + Explore `/explore/:id`)** — thêm 2026-10-24: một lượt tra mất 1–6 phút
  mà hiện chỉ có khối skeleton xám to (446px, 1086px) → người dùng không biết đang làm gì, còn bao lâu, cái nào xong.
  - **Bảng tiến độ ở đầu trang** thay cho skeleton cả trang: thanh tiến độ tổng + mỗi nguồn 1 dòng (icon nguồn · trạng
    thái chữ · số đếm), vd "Google Play — đang đếm đối thủ, keyword 3/6". Khối dữ liệu bên dưới chỉ giữ skeleton thấp
    (≤ 160px) có chữ "Chờ Google Play…" ở giữa, không còn ô trống cao. Hiệu ứng nhẹ (thanh chạy, chấm nhấp nháy), tắt khi
    `prefers-reduced-motion`.
  - **Tiến độ thật, không đoán:** thêm cột `progress_done` / `progress_total` cho `source_jobs` và `explorations`
    (migration mới); collector báo `onProgress(n, total)` sau mỗi keyword. Nguồn chưa báo được → chỉ hiện bước, không số.
  - **Ước lượng thời gian:** "Còn khoảng ~X phút · đã chạy 1:20". X = trung vị thời gian nguồn đó ở 20 lần chạy xong
    gần nhất (`finishedAt − startedAt` trong SQLite), chỉnh theo số keyword; Explore = keyword còn lại × nhịp iTunes
    3 giây. Chưa có lịch sử → số đo thật đã ghi (Explore 50 keyword ≈ 4 phút, 100 ≈ 6,3 phút) + chữ "ước lượng".
    Lấy từ cache 24h → "Lấy từ cache, gần như tức thì". Luôn có dòng: "Có thể đóng tab — tool vẫn chạy, xem lại ở Lịch sử".
  - **Khi xong → checklist kết quả:** mỗi bước ✓ / ✗ / ⏳ kèm số ra được + thời gian chạy (vd "✓ App Store · 38 app ·
    0:52", "✗ Reddit · thiếu key — bỏ qua", "✗ Trends · bị chặn tạm — Thử lại"). Bảng tiến độ đổi thành "Tóm tắt lượt
    tra", gập lại được. Tiêu đề tab đổi "✓ Xong — <niche>"; nút "Báo tôi khi xong" xin quyền Notification của trình duyệt
    (chỉ xin khi bấm).
  - **Thoát ra giữa chừng:** việc chạy ở server Node, trạng thái từng bước lưu trong SQLite (`source_jobs`,
    `explorations`) — đóng tab không dừng, mở lại `/r/:id` là thấy đúng tiến độ. Thêm: `GET /api/activity` (lượt đang
    chạy + lượt xong trong 24h) → huy hiệu "1 đang chạy" trên nav, Lịch sử ghim lượt đang chạy lên đầu kèm thanh tiến
    độ, banner trang chủ "Lượt tra '<niche>' xong lúc HH:MM — Xem". `localStorage` chỉ nhớ id đã xem để tắt banner —
    mất thì banner hiện lại, không mất dữ liệu. Tắt server giữa chừng → `markInterrupted` (đã có) → checklist ghi "Bị
    dừng vì server tắt — Thử lại".
  - **Không làm:** WebSocket/SSE (giữ poll 2 giây), push notification qua server, đếm tiến độ cho từng request nhỏ.
- **Làm thêm — UI Flow niche (thanh bước + sơ đồ nhánh)** — thêm 2026-10-24. Mục tiêu UX: người dùng luôn biết **mình đang
  đi theo hướng nào, tới bước nào**. Đường đi mẫu: Research `bubble game` → Explore `bubble game` → Mở rộng
  `bubble shooter` → Mở rộng `bubble shooter offline` → Research sâu. Mỗi lần đi sâu là rẽ một nhánh; **lá cuối của
  một nhánh = long-tail niche** (keyword niche đầy đủ). Một đường gốc → lá được chốt gọi là **FLOW niche 1, FLOW niche
  2…** của lượt tra đó.
  - **Thanh bước ở đầu trang** (chỗ trống ngay dưới nav, trên tiêu đề, cả `/r/:id` lẫn `/explore/:id`): các bước nối
    bằng mũi tên, vd `① Research bubble game ✓ → ② Explore ✓ 100 keyword → ③ Mở rộng bubble shooter ⏳ 12/50 → ④ …`.
    Bước đang đứng tô đậm, bước đã qua bấm được để quay lại, bước đang chạy dùng chung tiến độ + ước lượng của mục
    UI Loading ở trên (một chỗ duy nhất, không hai thanh). Điện thoại 375: chỉ hiện bước trước · bước hiện tại · số
    bước, vuốt ngang xem hết.
  - **Sơ đồ nhánh (roadmap):** khối gập/mở dưới thanh bước, vẽ cây ngang gốc trái → nhánh phải từ dữ liệu sẵn có
    (`explore_nodes.parentId` + `depth` ≤ 3, `node_runs` cho research sâu, `runs.parentRunId` cho run → run). Chỉ vẽ
    các node **đã mở rộng hoặc đã research sâu** (không vẽ cả 100 keyword); nhánh đang đi tô màu, nhánh khác mờ; FLOW
    đã chốt có nhãn `FLOW 1`, `FLOW 2`. Bấm node → nhảy tới keyword đó trong bảng.
  - **Chốt FLOW:** ở node bất kỳ có nút "Chốt làm long-tail niche" → tạo FLOW N = đường gốc → node đó. Danh sách FLOW
    ở cuối sơ đồ: `FLOW niche 1 · bubble game → bubble shooter → bubble shooter offline · điểm cơ hội 64 · đã research
    sâu ✓` + nút Bỏ chốt. FLOW là đầu vào cho Phase 7 (xếp hạng + evidence pack).
  - **Dữ liệu:** bảng mới `flows` (id, exploration_id, leaf_node_id, số thứ tự N, ghi chú, created_at) — đường đi tính
    lại từ chuỗi `parentId`, không lưu trùng. Thêm `explorations.source_run_id` (Explore mở từ trang Research nào) để
    nối run → explore thành một cây. Thêm `explorations.current_node_id` = node vừa mở rộng / đang xem → thoát ra
    vào lại vẫn đứng đúng bước (cùng nguyên tắc "server giữ trạng thái" của mục UI Loading).
  - **Không làm:** gộp FLOW giữa nhiều lượt Explore khác nhau · AI tự chọn lá (để Phase 6–7) · kéo-thả sắp xếp sơ đồ ·
    vượt độ sâu 3 hiện có.
- **Ra:** trang `/explore/:id`, file CSV · bảng tiến độ + checklist kết quả + huy hiệu "đang chạy" (trang run + explore) ·
  thanh bước đầu trang + sơ đồ nhánh + danh sách FLOW niche.
- **Xong khi (phần UI thêm):** 1 research + 1 explore thật: thấy tiến độ từng nguồn + ước lượng, ước lượng lệch ≤ 50%
  so với thời gian thật (ghi số), đóng tab giữa chừng rồi mở lại thấy đúng tiến độ, xong có checklist ✓/✗ · đi thật
  `bubble game` Research → Explore → mở rộng 2 tầng → chốt 2 FLOW: thanh bước đúng vị trí, sơ đồ hiện 2 nhánh có nhãn
  FLOW, thoát ra vào lại vẫn đúng bước · screenshot 1280 + 375 đã Read.
- **Đo thật (US, 2026-10-24):** `budget tracker` → 100 keyword đủ số liệu, ~6,3 phút, không lỗi.
- Chi tiết: [`../plans/2026-10-24-niche-radar-phase1-explorer.md`](../plans/2026-10-24-niche-radar-phase1-explorer.md).

### Phase 2 — App Store

- **Mục tiêu:** cùng câu hỏi như Phase 1 nhưng cho iOS, cộng giá + gói mua trong app.
- **Làm:** gợi ý App Store (search hints) làm nguồn keyword thứ 3 · độ đông riêng iOS / Play · review 1–2★ iOS vào
  "Đối thủ bị chê gì" · cột tiền (`Free` · `Trả tiền $X` · `IAP $a–$b` · `Sub ~$X/tháng` · `chưa đo`) · khoảng trống Play ↔ iOS.
- **Không làm:** ước doanh thu app từ số rating / lượt cài (chỉ số verified ở Phase 5, hoặc `chưa đo`) · giá nhiều nước cùng lúc.
- **Xong khi:** 3 niche thật có câu than cả Play + iOS · cột tiền có số cho ≥ 4/5 top app iOS · test xanh, chạy thật không bị chặn.
- Chi tiết: `docs/phase-2-app-store.md` · plan code [`../plans/2026-10-24-niche-radar-phase2-appstore-money.md`](../plans/2026-10-24-niche-radar-phase2-appstore-money.md).

### Phase 3 — Google Trends

- **Mục tiêu:** nhu cầu lên hay xuống, ở nước nào, có mùa vụ không.
- **Làm:** cột xu hướng cho Top 10 · so 5 keyword · theo nước/vùng · mùa vụ 5 năm · related topics. Chống chặn: gom
  request, cache dài, backoff, chỉ gọi cho Top 10.
- **Không làm:** hỏi Trends cho cả 100 keyword · số lượt tìm thật (Trends chỉ cho chỉ số 0–100).
- **Xong khi:** Top 10 của 3 niche thật có xu hướng, một lần chạy không bị chặn.
- Chi tiết: `docs/phase-3-google-trends.md`.

### Phase 4 — Feature Gap Matrix

- **Mục tiêu:** đối thủ đang thiếu tính năng gì → wedge.
- **Làm:** bảng 10 hàng mặc định × top 5 app mỗi store; ô `Có / Không / Trả phí / ?` + câu nguồn + link · bản nháp
  luật từ khoá (không AI) · tuyến A AI API key tối thiểu · tuyến B Claude in Chrome qua file job `.json` · cột Khoảng trống (≤ 1/5 app có).
- **Không làm:** lớp AI đầy đủ (để Phase 6) · AI tự điền ô không có câu nguồn.
- **Xong khi:** 3 niche có matrix 5 app × 10 hàng, ≤ 20% ô `?`, mọi ô `Có/Không` có câu nguồn · chạy được cả tuyến A và B.
- Chi tiết: `docs/phase-4-feature-gap.md`.

### Phase 5 — Verified Sites

- **Mục tiêu:** ai đang thu tiền thật trong ngách — số từ cổng thanh toán.
- **Làm:** collector TrustMRR (không key: `trustmrr.com/category/<slug>` + `startup/<slug>.md`; có key tuỳ chọn:
  `api/v1/startups?q=`) — 30 ngày · MRR · provider · ngày sync · nhãn `verified`, cảnh báo sync > 30 ngày, cache 7 ngày,
  1 req / 2 giây, ghi "khớp gần đúng" · nguồn tương tự TrustMRR cắm thêm, mỗi nguồn kiểm trước (sống? cổng thanh toán hay
  tự khai?); tự khai → nhãn `tự khai`, không bao giờ `verified`.
- **Không làm:** coi số TrustMRR là khớp chính xác ngách · dịch vụ ước tính trả phí (Sensor Tower, AppTweak…) · dán nhãn
  `verified` cho nguồn tự khai.
- **Xong khi:** khối Tiền thật có ≥ 1 dòng cho 2/3 niche thật (hoặc ghi "không có sản phẩm cùng ngách" + ngày tra) ·
  mỗi nguồn thêm có kết quả kiểm.
- Chi tiết: `docs/phase-5-verified.md` · code đang làm theo Task 6 plan Phase 2.

### Phase 6 — Tích hợp AI (bản Web)

- **Mục tiêu:** AI đọc thay mình review / Reddit / listing — có nguồn, tắt được, ưu tiên đường miễn phí.
- **Bước 0 (thử, chưa chắc được):** một bài chuẩn (gom 200 review 1–2★ thành chủ đề có câu nguyên văn) chạy trên 4 tuyến:
  A API key (Claude, Gemini Flash) · B extension miễn phí (Claude in Chrome, Gemini in Chrome) qua file job · C AI trong
  trình duyệt (Chrome built-in AI / Gemini Nano, WebLLM, Transformers.js) · D model trên máy (Ollama, LM Studio). Ghi chất
  lượng · thời gian · tiền · máy cần gì → chọn ≤ 2 tuyến.
- **Làm:** lớp AI chung (chọn tuyến, key, trần chi phí, cache, log) · chủ đề than · phân loại Reddit · Feature Gap Matrix
  tự động đủ · tóm tắt niche 5 dòng có nguồn.
- **Luật:** AI không bịa số; không bật AI thì Phase 1–5 vẫn chạy.
- **Không làm:** xây cả 4 tuyến (chỉ tuyến qua Bước 0) · gửi key lên server nào ngoài provider.
- **Xong khi:** bảng Bước 0 đủ 4 tuyến · 3 niche chạy đủ với tuyến đã chọn, dưới trần chi phí, trích dẫn bấm được.
- Chi tiết: `docs/phase-6-ai-web.md`.

### Phase 7 — Review + Validate

- **Mục tiêu:** soát lại Phase 1–6 trên niche thật, rồi kiểm cả hệ thống bằng một vòng chọn niche thật.
- **Làm:** 5 niche thật chạy qua Phase 1–6, đối chiếu "Xong khi" từng phase, kiểm tay 10 ô matrix + 10 trích dẫn, sửa lỗi ·
  Opportunity Score v2 (Nhu cầu · Cạnh tranh · Đau · Xu hướng · **Tiền**, mỗi yếu tố 0–10 có nguồn + độ tin, Tiền nặng hơn,
  giữ điểm v1 để so, back-test) · evidence pack `.md` theo `templates/demand.md` cho `/app-demand` · nháp test bán trước
  (tool không tự đăng) · bảng kết quả test với ngưỡng ghi trước → gợi ý BUILD / TEST THÊM / BỎ (quyết định là của anh).
- **Không làm:** tính năng tra cứu mới.
- **Xong khi:** 5 niche qua checklist · ≥ 5 niche có điểm v2 · 1 niche đi hết evidence pack → test bán trước → số thật.
- Chi tiết: `docs/phase-7-review-validate.md`.

### Phase 9 — Small Features Update

- **Mục tiêu:** làm các tính năng nhỏ lượm được khi dùng thật, mỗi cái một plan ngắn.
- **Trạng thái:** 4 mục ưu tiên xong 2026-10-25 (anh chốt làm luôn, không đợi test bán trước) · ứng viên khác chưa chốt.
- **Ứng viên ưu tiên (review 2026-10-25):** điểm v2 thêm trục **Tiếp cận khách** +
  **Hợp sức mình**, trọng số mẫu Mac / iOS / Android / SaaS, 1 dòng lý do mỗi điểm · **mức nặng** chủ đề than ·
  **nhãn mô hình tiền** (subscription / lifetime / IAP / quảng cáo / chưa biết) · **theo dõi định kỳ** 7 / 30 / 90 ngày cho project.
  Không thêm lại Reddit.
- **Ứng viên khác (từ Appendix cũ):** cờ đối thủ yếu · MCP có sẵn · MCP của app · Chrome Web Store · giá IAP nhiều nước ·
  search volume trả phí (chỉ khi Phase 7 cho thấy cần).
- **Không làm:** tính năng ngoài danh sách đã chốt · đổi UI tổng thể (Phase 11). Tính năng to hơn ~1 tuần → tách phase riêng.
- **Xong khi:** danh sách ưu tiên anh duyệt · mỗi tính năng có ở bản Web, test xanh, screenshot (app Mac nhận ở mục App).
- Chi tiết: `docs/phase-9-small-features.md`.

### Phase 10 — So sánh niche (không AI) · dời lên sau Phase 9, trước là Phase 18 (2026-10-25)

- **Vì sao dời:** chỉ đọc DB, chạy được với dữ liệu Phase 1–9; chọn giữa vài niche là câu hỏi chính, không chờ nguồn mới. Nhóm Nguồn mới ghi "chưa tra" tới Phase 13–17. App Mac gói ở Phase 57 (mục App).

- **Làm:** chọn 2–4 niche đã tra → bảng mỗi niche 1 cột, nhóm Cơ hội · Đối thủ · Xu hướng · Đau · Tiền · Nguồn mới → tô ô thắng theo luật cố định ghi trên UI · ô thiếu ghi "chưa tra" · xuất CSV + Markdown.
- **Xong khi:** 3 niche thật đủ nhóm · kiểm tay 10 ô khớp màn chi tiết · đọc được ở 1340px.
- Chi tiết: `docs/phase-10-compare-niche.md`.

### Phase 11 — UI / UX Improvement

- **Mục tiêu:** sửa chỗ vướng thật — luồng chính, trạng thái tải/rỗng/lỗi, bảng dày, sáng/tối, bàn phím, cỡ cửa sổ.
- **Làm:** soát từng màn → mockup (Codex) → anh duyệt → sửa bản Web → screenshot trước/sau. Checklist: [Soát gì](https://nvminhtu.github.io/niche-radar-docs/web/phase-11-ui-ux/#soat-gi).
- **Không làm:** thêm tính năng mới (ghi sang Phase 9) · đổi hết giao diện khi không có vướng thật.
- **Xong khi:** danh sách chỗ vướng có trạng thái từng mục (sửa / bỏ + lý do) · mỗi màn sửa có screenshot trước/sau đã Read ở bản Web.
- Chi tiết: `docs/phase-11-ui-ux.md`.

### Phase 12 — Account + Flow người dùng

- **Mục tiêu:** người khác dùng được không cần hỏi; có đường nhận tính năng mới.
- **Làm:** hồ sơ trên máy → đăng nhập khi cần · license key (mẫu Lemon Squeezy của RAM Rescue) nếu bán · flow lần đầu mở →
  tra niche đầu tiên → lưu project · nút góp ý → phân loại → danh sách Phase 9.
- **Không làm:** server nhiều người, sync cloud — chỉ khi Idea Lab qua test và chọn host.
- **Xong khi:** 1 người ngoài cài, tra 1 niche, gửi 1 góp ý không cần hỏi anh.
- Chi tiết: `docs/phase-12-account.md`.

---

**Vạch MVP.** Phase 1–12.2 là MVP. Từ Phase 13: mỗi nguồn mới một phase **cào số (không AI)** rồi một phase **AI đọc chữ**
(dùng lại lớp AI Phase 6). Chỉ bản Web; gói vào app Mac là Phase 57 ở mục App, sau khi hết mọi phase Web.
Luật cào chung: gọi thưa, cache, bị chặn thì dừng nguồn đó và báo — **không vượt captcha, không proxy xoay, không cào
trang cần đăng nhập bằng script**.

### Phase 13 — YouTube Search (không AI)

- **Làm:** gợi ý YouTube (autocomplete `ds=yt`) làm nguồn keyword thứ 4 · top 20 video mỗi keyword Top 10 (view, ngày
  đăng, độ dài, kênh) · độ đông YouTube · độ mới (video top trong 12 tháng) · "video vượt kênh" (view ÷ sub cao) · CSV.
- **Thư viện:** `youtubei.js` (InnerTube, không key) làm chính; YouTube Data API v3 (quota 10.000/ngày, 1 lần tìm = 100) dự phòng có key; `yt-dlp` nếu cần bền hơn. Đo endpoint trước khi code.
- **MCP bên thứ 3 (tuỳ chọn, tắt mặc định):** vidIQ (`mcp.vidiq.com/mcp`: `keyword_research` lượt tìm + cạnh tranh, `outliers`, `trending_videos`; có gói Free, trừ credit mỗi lần gọi) thử trước · Apify YouTube MCP · MCP cộng đồng trên YouTube Data API. Tuyến job `.json` qua Claude đã nối MCP (chính) hoặc app gọi thẳng bằng API key chỉ đọc. Số MCP = ước tính bên thứ 3, cột riêng, không trộn vào điểm cơ hội, trần credit mỗi niche.
- **Xong khi:** 3 niche thật có cây keyword YouTube + bảng top video + cột video vượt kênh, một lần chạy không bị chặn.
- Chi tiết: `docs/phase-13-youtube-search.md`.

### Phase 14 — YouTube Research (AI)

- **Làm:** phụ đề + comment top video → chủ đề than · xin tính năng · tool được nhắc · tóm tắt video có mốc giây · gợi ý hàng mới cho Feature Gap Matrix.
- **Tuyến:** phụ đề + comment qua lớp AI Phase 6 (chính) · Gemini API đọc thẳng link YouTube (video không phụ đề) · Claude in Chrome qua file job. Bài thử chuẩn 10 video → chọn.
- **Xong khi:** 3 niche có chủ đề + xin tính năng, mọi câu có link + mốc giây, dưới trần chi phí.
- Chi tiết: `docs/phase-14-youtube-ai.md`.

### Phase 15 — Amazon Search (không AI)

- **Làm:** gợi ý Amazon · top 20 sản phẩm mỗi keyword Top 5 (giá, sao, số review, huy hiệu đã bán) · BSR top 5 · khoảng giá · "lính mới thắng".
- **Cách lấy:** autocomplete + cào HTML (`fetch` + `cheerio`), ≥ 5 giây / request, cache 7 ngày; gặp captcha → dừng nguồn. PA-API không hợp (cần tài khoản Associates có doanh số).
- **Không làm:** ước doanh số từ BSR · Jungle Scout / Helium 10 / Keepa.
- **Xong khi:** 3 niche có cây keyword Amazon + top sản phẩm + khoảng giá; captcha (nếu có) báo đúng trên UI.
- Chi tiết: `docs/phase-15-amazon-search.md`.

### Phase 16 — Amazon Research (AI)

- **Làm:** review 1–3★ + hỏi đáp top 5 sản phẩm → chủ đề chê · ước gì · so với ai · gợi ý chỗ app làm tốt hơn · cột Amazon cho Feature Gap Matrix.
- **Tuyến:** Claude in Chrome trong phiên Amazon anh tự đăng nhập (chỉ đọc, kết quả qua file `.json`) — chính · lớp AI Phase 6 cho mô tả + review công khai.
- **Không làm:** cào review sau đăng nhập bằng script · Claude tự đăng nhập / nhập mật khẩu.
- **Xong khi:** 3 niche có chủ đề chê + ước gì có link review · ≥ 1 gợi ý cho app anh thấy đáng soi.
- Chi tiết: `docs/phase-16-amazon-ai.md`.

### Phase 17 — Google Maps Research (AI)

- **Làm:** đếm cửa hàng theo loại × thành phố (≤ 5 thành phố) · review 1–3★ Top 20 chỗ → khách than gì · chủ trả lời gì · việc làm tay → ý tưởng app có ≥ 3 review làm bằng chứng → evidence pack Phase 7.
- **Cách lấy:** OpenStreetMap Overpass (0 đ, đếm) · Google Places API (New) có key, có trần số lần gọi · Claude in Chrome đọc review trên Maps. **Không** cào Maps bằng script.
- **Xong khi:** 3 loại × 2 thành phố có số đếm + chủ đề có trích dẫn · ≥ 1 ý tưởng có ≥ 3 review · chạy được không cần key.
- Chi tiết: `docs/phase-17-google-maps.md`.

---

**Version 3 · So sánh + AI Cite.** Không thêm nguồn. So sánh niche (Phase 10) đã dời lên MVP; ở đây đặt 2–5 đối thủ cạnh nhau (không AI), rồi cho hỏi dữ liệu
bằng lời — AI chỉ đọc DB, mọi câu có trích dẫn, **máy tự kiểm** (id có thật · câu trích đúng chữ · số bằng DB), sai thì cờ
đỏ. Thước đo: chọn 1 niche thật ≤ 30 phút tới evidence pack. **Không làm:** nguồn mới · AEO/GEO/SEO (Version 4) · AI lên
web khi trả lời · so theo thời gian (theo dõi định kỳ, Phase 9) · AI chấm "niche tốt nhất" · chat nhiều lượt. Chi tiết: `docs/version-3.md`.

### Phase 19 — So sánh đối thủ (không AI)

- **Làm:** 2–5 đối thủ trong 1 niche → giá / gói · sao, % review 1–2★, cập nhật cuối · tính năng từ Feature Gap Matrix · 3 chủ đề than có câu nguyên văn + link · hàng "Chỗ trống" · xuất.
- **Xong khi:** 2 niche × 4 đối thủ đủ hàng · 10 câu than mở đúng review gốc · ≥ 1 dòng Chỗ trống.
- Chi tiết: `docs/phase-19-compare-competitor.md`.

### Phase 20 — Hỏi dữ liệu (AI Cite)

- **Làm:** ô hỏi trên màn niche / so sánh → lấy dòng liên quan từ DB kèm id → lớp AI Phase 6 → câu trả lời gắn id nguồn → **lớp kiểm trích dẫn dùng chung** → lịch sử hỏi.
- **Xong khi:** bài thử 20 câu: ≥ 95% trích dẫn qua kiểm, 0 câu thiếu trích dẫn, đúng "chưa có dữ liệu", dưới trần chi phí · sửa 1 câu trích trong DB → cờ đỏ.
- Chi tiết: `docs/phase-20-ai-cite-ask.md`.

### Phase 21 — Báo cáo so sánh (AI Cite)

- **Làm:** từ bảng Phase 10 / 19 → báo cáo khung cố định (kết luận · mạnh/yếu · rủi ro · câu hỏi mở) → kiểm trích dẫn, còn cờ đỏ thì chặn xuất → sửa tay → evidence pack `.md` cho `/app-research`.
- **Không làm:** ghi Verdict thay người dùng · sinh concept / giá / spec · PDF, slide.
- **Xong khi:** 2 báo cáo niche + 1 báo cáo đối thủ, 0 cờ đỏ · kiểm tay 15 trích dẫn đúng.
- Chi tiết: `docs/phase-21-ai-cite-report.md`.

### Phase 22 — Review Version 3

- **Làm:** 3 lần chọn niche thật ở bản Web (bấm giờ) → sửa lỗi. Gói vào app Mac → Phase 58 (mục App).
- **Xong khi:** ≥ 2/3 lần ≤ 30 phút · test xanh.
- Chi tiết: `docs/phase-22-local-app-3.md`.

---

**Version 4 · LLM + AEO, GEO, SEO.** Thêm kệ Google (top 10, loại trang) và kệ AI (LLM dùng làm nguồn: hỏi như người
dùng, đếm nhắc tên + trang được trích bằng regex) vào lúc chọn niche; niche đã chọn xuất gói GEO cho `scripts/geo.py` của
App-AI-Skills. Thước đo: 3 niche có cột Kệ Google + Kệ AI · ≥ 1 gói GEO chạy `geo.py` không sửa tay. **Không làm:** tool
SEO trả phí / search volume trả phí (ứng viên Phase 9) · cào Google / AI Overviews bằng script · đo app mình sau ra mắt
(`/app-geo`) · viết / đăng bài · audit kỹ thuật (`geo.py audit`) · fine-tune model · mẹo lừa AI · hứa thứ hạng.
Chi tiết: `docs/version-4.md`.

### Phase 23 — Kệ Google (SEO, không AI)

- **Làm:** top 10 cho Top 10 keyword qua API tìm kiếm có tầng miễn phí (Brave Search API đề xuất; đo quota trước) → loại trang theo luật domain (store · forum · blog nhỏ · site lớn · app chính chủ · video) → độ dễ chen · bộ câu hỏi từ autocomplete `how/why/can/best/vs/alternative` · cache 7 ngày.
- **Xong khi:** 3 niche × 10 keyword · ≥ 20 câu hỏi/niche · ≥ 6/10 URL kiểm tay có trong top 10 Google · hết quota báo đúng.
- Chi tiết: `docs/phase-23-seo-shelf.md`.

### Phase 24 — Kệ AI (GEO / AEO)

- **Làm:** 10–20 câu × engine (Gemini + Google Search grounding chính · ChatGPT qua `codex exec` · Claude qua `claude -p`, cùng câu lệnh mẫu `geo.py`) → lưu nguyên văn + engine + model + ngày → đếm nhắc tên + domain được trích bằng regex → cờ câu trả lời yếu · trần chi phí.
- **Xong khi:** 3 niche × 10 câu × ≥ 2 engine dưới trần · kiểm tay 10 câu đếm đúng · khớp `geo.py analyze` trên cùng câu.
- Chi tiết: `docs/phase-24-ai-shelf.md`.

### Phase 25 — Chỗ trống AI + SEO (không AI)

- **Làm:** điểm kệ Google (% forum + blog nhỏ, có app chính chủ không) + điểm kệ AI (% câu yếu, độ tập trung nhắc tên, trang trích viết được không) theo công thức ghi trên UI → 2 cột mới trong so sánh niche Phase 10 → danh sách câu hỏi chưa ai trả lời tốt.
- **Xong khi:** 3 niche có 2 cột mới, mỗi điểm bấm ra số gốc · niche biết chắc đông ra "khó chen".
- Chi tiết: `docs/phase-25-ai-seo-gap.md`.

### Phase 26 — Gói GEO + trang cần viết

- **Làm:** niche đã chọn → `questions.tsv` + `brands.tsv` đúng định dạng `geo.py` · danh sách trang cần viết (loại trang · trang AI đang trích · lý do qua AI Cite Phase 20) · `geo-pack/` + lệnh chạy mốc.
- **Không làm:** viết bài (`/oneclicktool-blog`) · đo lại sau ra mắt (`/app-geo`).
- **Xong khi:** 1 niche → `geo.py run` + `analyze` chạy không sửa tay · ≥ 5 trang cần viết có trích dẫn qua kiểm.
- Chi tiết: `docs/phase-26-geo-pack.md`.

### Phase 27 — Review Version 4

- **Làm:** 3 lần chọn niche thật có kệ Google + kệ AI → sửa lỗi. Gói vào app Mac → Phase 59 (mục App).
- **Xong khi:** 3 lần chọn có gói GEO chạy mốc, dưới trần · test xanh.
- Chi tiết: `docs/phase-27-local-app-4.md`.

---

**Version 5–12 · thành sản phẩm bán được.** Mỗi version một trang `docs/version-N.md`, phase nằm trong trang.

### Version 5 — Performance (Phase 28–30)

- Đo mốc (`npm run bench`, 3 niche chuẩn) → collector song song theo nguồn + stream + cache dùng chung + chạy tiếp khi lỗi → virtualize bảng, lazy load, index SQLite, WAL. App Mac nhẹ → Phase 60 (mục App). **Không:** tính năng mới · vượt giới hạn nguồn · viết lại bằng Rust · server cloud.
- Chi tiết: `docs/version-5.md`.

### Version 6 — Automation Test + Review Results (Phase 32–35)

- Fixture ghi lại từ nguồn thật, `npm test` xanh khi tắt mạng → Playwright 5 luồng chính + so ảnh → canary launchd hằng ngày báo nguồn đổi dạng → bộ 5 niche chuẩn đáp án tay + `npm run review` ra phiếu review → (tùy chọn 35b) `npm run functest` search thật + chụp màn kết quả 1340/375 vào `run/functest/`. **Không:** CI (Version 7) · coverage 100% · test tải.
- Chi tiết: `docs/version-6.md`.

### Version 7 — CI/CD (Phase 36–39)

- GitHub Actions cho PR (lint, type, test, E2E fixture, docs strict) → bảo vệ `main`. Build app trên CI + release + auto-update → Phase 62–38 (mục App). **Không:** Windows · Mac App Store · deploy Web · canary trên CI · auto-merge.
- Chi tiết: `docs/version-7.md`.

### Version 8 — Security & Account & Refactor Code (Phase 40–43)

- Phiếu bảo mật (token API cục bộ, chặn Origin lạ, chữ cào không render HTML, npm audit, quét secret) → `user_id` mọi bảng, nhiều hồ sơ, xuất / xoá dữ liệu → khuôn `Collector` chung, tách file > 400 dòng, hành vi không đổi (phiếu review giữ điểm) → tự tấn công thử + 8.0. **Không:** đăng nhập mạng · thanh toán · đổi framework · pentest thuê.
- Chi tiết: `docs/version-8.md`.

### Version 9 — Firebase, Analytics, Account (Phase 44–47)

- Firebase Auth trên bản Web (Google, Apple, email link) → Firestore chỉ project / ghi chú / kết luận / so sánh, dữ liệu cào thô ở lại SQLite, quy tắc chỉ chủ → GA4 sự kiện phễu không gửi chữ người gõ, hỏi đồng ý + báo lỗi → xoá tài khoản xoá cả cloud + Privacy Policy. **Không:** dữ liệu thô lên cloud · team · server riêng.
- Chi tiết: `docs/version-9.md`.

### Version 10 — Sell Pro — Lifetime / Subscriptions (Phase 48–51)

- `money.md` qua `/app-money` (giá đối thủ có nguồn + chi phí AI đo thật + phễu GA4) → Lemon Squeezy + webhook Cloud Functions → quyền Pro (license key kích hoạt trong app → Phase 61) → paywall, dùng thử, khôi phục, giới hạn máy → BYOK hay gói lượt AI có trần. Thước đo: 1 đơn thật có nguồn. **Không:** Mac App Store IAP · tự xử lý thẻ · gói team · crypto.
- Chi tiết: `docs/version-10.md`.

### Version 11 — Marketing Plan (Phase 52–55)

- `/app-gtm`: định vị + landing riêng (`/oneclicktool-landing`) + email + GA4 → 2 kênh chọn bằng ICE → dogfood: báo cáo niche công khai hằng tuần + Version 4 cho chính niche-radar → lịch 6 tuần + ra mắt + bảng số + luật dừng. Claude soạn, anh đăng. **Không:** quảng cáo trả tiền trước 10 đơn · mua review · > 2 kênh.
- Chi tiết: `docs/version-11.md`.

### Version 12 — New Features — Just Planned

- Chỉ lên plan: danh sách ứng viên (Product Brief Export — chỉ khi bán cho người ngoài, search volume trả phí, Chrome Web Store, IAP nhiều nước, MCP của app, team, Perplexity, Windows, TikTok / X, báo cáo công khai tự động, góp ý người dùng) → chấm số người xin · tác động · công · rủi ro → chọn ≤ 3 mỗi đợt, anh duyệt mới tách phase từ 64 (56–63 là App Mac).
- Chi tiết: `docs/version-12.md`.

### Version 13 — App Mac (Phase 56–63) — phase cuối cùng

App bọc lại đúng giao diện Web (Tauri), nên chỉ gói **một lần** khi bản Web đã chín. Phase Web chỉ làm phần Web;
phần riêng của app gom ở Phase 61. Thứ tự: **56 → 57 → 58 → 59 → 60 → 61 → 62 → 63**. Chi tiết: `docs/app/index.md`.

#### Phase 56 — Local App 1.0 (trước là phần app của Phase 8; code xong sớm 2026-10-25, thử máy mới khi tới lượt App)

- **Mục tiêu:** đóng gói Phase 1–6 thành app Mac bấm là mở; project; xuất/nhập giữa các máy.
- **Làm:** Tauri (lõi Rust) + đúng UI React + server Node chạy kèm (sidecar) · ULID · `schema_version` · `NR_DATA_DIR` ·
  project + ghi chú · xuất `.json` / CSV / `.md` · backup/restore · `.dmg` ký + notarize. Viết lại collector bằng Rust chỉ
  khi gói Node làm app quá nặng.
- **Không làm:** tính năng tra cứu / chấm điểm mới · đăng nhập, sync cloud, license (Phase 12) · bản Windows, auto-update.
- **Xong khi:** mở `.dmg` trên tài khoản macOS mới chưa có Node → tra được 1 keyword, Gatekeeper không cảnh báo · mở ≤ 5 giây ·
  xuất → nhập project bằng nhau, nhập lại không nhân đôi · backup → restore đủ · DB thật lên ULID không mất dòng · test xanh,
  web `npm run dev` vẫn chạy (đủ 6 mục ở spec §2).
- Chi tiết: [spec Phase 8](2026-10-24-niche-radar-phase8-local-app.md) · `docs/app/phase-56-local-app-1.md`.

#### Phase 57 — Local App 2.0

- **Làm:** gói phần còn lại Version 1 (7, 9–12.2) + Phase 13–17 → gói collector mới vào sidecar → migration DB (bảng mới ULID) → key trong Keychain → nút job Claude in Chrome → `.dmg` ký + notarize.
- **Xong khi:** app 1.x có dữ liệu → cài 2.0 không mất dòng · tra 1 niche ra đủ khối YouTube + Amazon + Maps · mở ≤ 5 giây.
- Chi tiết: `docs/phase-57-local-app-2.md`.


#### Phase 58 — Local App 3.0

- **Làm:** gói Phase 19–21 vào app → migration DB (bộ so sánh, lịch sử hỏi, kết quả kiểm, ULID) → `.dmg` 3.0 ký + notarize.
- **Xong khi:** 2.x → 3.0 không mất dòng · test xanh, bản Web vẫn chạy. Chi tiết: `docs/app/phase-58-local-app-3.md`.

#### Phase 59 — Local App 4.0

- **Làm:** gói Phase 23–26 (key trong Keychain, engine `codex`/`claude` có thì dùng) → migration DB → `.dmg` 4.0.
- **Xong khi:** 3.x → 4.0 không mất dòng · test xanh. Chi tiết: `docs/app/phase-59-local-app-4.md`.

#### Phase 60 — App Mac nhẹ

- Mở ≤ 3 giây, ít RAM khi rảnh, sidecar + `.dmg` nhỏ hơn — đo so với mốc Phase 28. Chi tiết: `docs/app/phase-60-light-mac-app.md`.

#### Phase 61 — Phần riêng của app Mac

- **Làm:** setup trong app (11.1) · CSP + quyền Tauri + key trong Keychain (40) · đăng nhập qua deep link (44) · license key + checkout từ app (49) · khôi phục mua (50) · BYOK Keychain + lượt AI còn lại (51).
- **Xong khi:** license key test kích hoạt được không đăng nhập · deep link quay lại đúng app · phiếu bảo mật app qua. Chi tiết: `docs/app/phase-61-app-only.md`.

#### Phase 62 — Build app Mac trên CI · Phase 63 — Release + auto-update

- Runner macOS build + ký + notarize bằng secret anh nhập → tag → GitHub Releases + What's New + Tauri updater. Chi tiết: `docs/app/phase-62-mac-build-ci.md`, `docs/app/phase-63-release-auto-update.md`.

### Appendix — chưa xếp phase / không làm

Xem §7 (mục chưa xếp cũ đã chuyển vào Phase 8, 9, 11).

## 4. Đang pending (cập nhật mỗi phase)

| Việc | Ghi chú |
|---|---|
| Merge `phase1-explorer` vào `main`, xoá stash `phase2-wip-codex-2-20261024-1019` | chờ anh đồng ý |
| Key Reddit | anh tự tạo app "script" trên Reddit khi cần; thiếu key thì 3 nguồn kia vẫn chạy |
| Explore 100 keyword mất ~6 phút | giới hạn App Store 1 request / 3 giây; Phase 2 xem lại cách đếm đối thủ |
| Điểm phổ biến còn nhiều keyword cùng mức 43 (chỉ gặp 1 lần ở hạng 1) | thêm nguồn thứ 3 (App Store hints) ở Phase 2 sẽ tách tốt hơn |
| Key TrustMRR (tuỳ chọn) | anh tự tạo ở trang dashboard TrustMRR khi cần; không key vẫn đọc trang công khai |

## 5. Xài gì

| Phần | Dùng gì |
|---|---|
| Giao diện | Vite + React 19 + React Router, Tailwind, Recharts |
| API | Hono trên Node, chỉ nghe `127.0.0.1` |
| Dữ liệu | SQLite qua better-sqlite3 + Drizzle ORM |
| Nguồn | `google-play-scraper` · iTunes Search API · Google autocomplete · `google-trends-api` · Reddit OAuth · TrustMRR (Phase 5) |
| Test | Vitest (115 test) + `npm run smoke` gọi thật |
| Tài liệu | MkDocs Material |
| App Mac (Phase 56) | Tauri (lõi Rust) + server Node chạy kèm |
| AI | Phase 1–3, 5 không dùng · Phase 4 tuỳ chọn (Feature Gap Matrix) · Phase 6 lớp AI chung — thử API key, extension miễn phí, AI trong trình duyệt, model trên máy; tắt mặc định |

## 6. Hạn chế và giới hạn miễn phí

| Hạn chế | Chi tiết |
|---|---|
| Không có lượt tìm thật | store không công khai; "phổ biến" là ước lượng từ gợi ý tìm kiếm |
| App Store không có số cài | so 2 store bằng số rating |
| Play / Trends / gợi ý Google không chính thức | có thể gãy khi Google đổi trang; gọi dồn dập bị chặn 10–30 phút |
| Doanh thu đối thủ | store không công khai; Play chỉ có "có IAP" + khoảng giá, iOS có giá từng gói. Doanh thu verified chỉ có ở TrustMRR (Phase 5) — chủ yếu web/SaaS, ít app mobile, ghép ngách gần đúng |
| AI tốn tiền theo lượt | tuyến API key (Phase 4, 6) có trần chi phí mỗi lần tra, tắt mặc định; Phase 6 thử thêm đường miễn phí |
| Claude in Chrome | extension của Claude, không có API cho app gọi — tuyến B Phase 4 chạy qua Claude Desktop / Claude Code, nhập kết quả bằng file |
| Giới hạn gọi | App Store ~20 req/phút · Reddit 100 req/phút/key · Play, Trends không công bố |

Thực tế: một người, mạng nhà, vài chục lần tra/ngày là ổn, không cần proxy. Chi tiết:
[giới hạn nguồn & chia sẻ](2026-10-24-niche-radar-limits-and-sharing.md).

## 7. Appendix — chưa xếp phase / không làm

Muốn làm mục nào → xếp vào một phase, sửa plan này trước. Không làm lén.

### Chưa xếp phase

Trống (2026-10-24): App Mac → Phase 8 · cờ đối thủ yếu, MCP có sẵn, MCP của app, Chrome Web Store, search volume trả phí,
giá IAP nhiều nước, theo dõi định kỳ → ứng viên Phase 9 · host nhiều người → Phase 12 (chỉ khi có quyết định bán).

### Không làm

| Không làm | Vì sao | Thay bằng |
|---|---|---|
| Dịch vụ ước tính trả phí hằng tháng (Sensor Tower, AppTweak, Appfigures, MobileAction) | tốn tiền hằng tháng cho tool nội bộ, số là ước tính của bên thứ ba | proxy miễn phí + Phase 5 verified |
| Sinh concept, giá, spec, checklist ra mắt trong tool | pipeline App-AI-Skills đã làm | `/app-research` → `/app-money` → `/app-spec` … đọc evidence pack |
| Tự đăng bài / chạy quảng cáo / thu tiền thật | ngoài vai trò tool; việc của người dùng | Phase 7 chỉ soạn nháp + lưu số |
| AI tự đưa ra con số (lượt tải, doanh thu) | dễ bịa | số chỉ từ collector, AI chỉ đọc chữ + trích dẫn |
| Dữ liệu TikTok / X | không có cách lấy miễn phí ổn định | Reddit; X đọc tay qua `/app-demand` |
| Electron | nặng | Tauri cho App Mac |
