# niche-radar Phase 1 — Niche Explorer cho Google Play — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm test && npm run typecheck && npm run lint`
> xanh rồi mới commit. Steps dùng checkbox (`- [ ]`).

**Goal:** gõ một niche → mở ra cây keyword người ta gõ thật trên Play + Google, gom sub-niche theo luật, mỗi keyword có
số liệu nhẹ + **điểm cơ hội 0–100 có công thức hiện trên UI**, bản đồ ngách, Top cơ hội, research sâu ≤ 5 keyword,
xuất CSV, câu than 1–2★ của top app Play.

**Định vị:** tool nội bộ (master plan, 2026-10-24). Không làm gì cho việc bán/host.

**Nền:** git stash `phase2-wip-codex-2-20261024-1019` (viết lúc app còn Next.js). Lấy logic, viết lại phần route/page
cho Vite + Hono. Chi tiết dùng lại / viết lại / bỏ: master plan §7 Phase 1 "Nền code".

**Spec:** master plan §7 Phase 1 + nháp `../specs/2026-10-24-niche-radar-phase2-explorer.md` (các câu hỏi mở ở cuối
nháp đã chốt trong master plan: có điểm cơ hội, Play + Google trước, không AI, deep ≤ 5, có CSV).

## Mục tiêu · làm · không làm

- **Xong khi:** gõ `habit tracker` (US) → ≥ 80 keyword có nguồn trong ≤ 3 phút; bảng sắp xếp theo điểm cơ hội;
  bản đồ ngách tô màu theo sub-niche; tick 3 keyword → research sâu ra 3 run v1; tải được CSV; khối "Đối thủ bị chê gì"
  có ≥ 3 cụm từ cho top app Play. Có screenshot đã Read của từng màn.
- **Làm:** đúng 9 Task bên dưới + **Task 10–11 (UI thêm 2026-10-24: Loading rõ ràng + Flow niche)** — spec ở master plan
  §3 Phase 1 "Làm thêm".
- **Không làm (backlog):** App Store search hints / review iOS (Phase 2) · so sánh nhiều keyword Trends (Phase 3) ·
  MCP (Phase 4–5) · AI gom ngách · key Reddit (anh tự tạo khi cần, không chặn Phase 1) · đổi giao diện v1 lẫn trong stash.

## Global Constraints

- Repo `niche-radar`, nhánh `phase1-explorer` cắt từ `main`.
- Stack hiện tại: Vite + React Router (`src/client/`), Hono (`src/server/app.ts`, mọi route dưới `/api`, giữ `api-guard`).
- Không pop stash vào cây làm việc (xung đột Next.js). Lấy từng file: `git show 'stash@{0}^3:<path>'` (file mới) hoặc
  `git show 'stash@{0}:<path>'` (file đã sửa), rồi sửa import/đường dẫn.
- Nhịp gọi giữ như v1: Play ≤ 1 req/s, Google suggest ≤ 1 req/s, iTunes 1 req/3s. Mỗi lần "Mở rộng" ≤ 50 keyword mới,
  độ sâu ≤ 3, cache gợi ý 7 ngày, timeout 10 phút.
- **Điểm cơ hội** = `round(phổ_biến × (1 − độ_đông))`, `phổ_biến` 0–100 từ `popularity()` của stash (hạng autocomplete +
  số nguồn xác nhận), `độ_đông` 0–1 = `min(1, log10(1 + tổng rating top 5) / 6)` (1M rating ≈ 1.0). Màu: xanh < 0.4,
  vàng 0.4–0.7, đỏ > 0.7. UI ghi rõ: "ước lượng, không phải lượt tìm thật".
- Độ đông lấy từ tổng rating top 5 **App Store** (iTunes trả sẵn trong search, rẻ); Play chỉ lấy số app (search không
  `fullDetail`). Ghi chú điều này trên UI.

## Tiến độ (2026-10-24, nhánh `phase1-explorer`, chưa commit)

- Task 1–7: **code xong**, 114 test xanh, typecheck + lint sạch. UI viết lại bằng Tailwind theo mockup
  `design/mockups/phase2/` (stash dùng class CSS của bản Next cũ nên không lấy UI của stash).
- Task 8: làm dạng **bấm mới tải** (nút “Đọc review 1–2★” trên trang run) thay vì collector chạy mỗi lần tra — không tốn
  request khi không cần. Endpoint `GET /api/research/:id/complaints`, cache `review_cache` 7 ngày.
- Thêm ngoài plan (bug thật gặp khi chạy): server khởi động lại để exploration kẹt `running` mãi → `markInterrupted`
  giờ mở khoá cả exploration + research sâu.
- Migration: `0003` (bảng Explorer), `0004` (`review_cache`).
- Task 9: đang chạy thật — số đo ghi ở mục “Kết quả chạy thật” cuối file.
- Task 10–11 (UI Loading + Flow niche): **code xong 2026-10-24** trên nhánh `phase1-ui-flow` (worktree
  `../niche-radar-ui-flow`, cắt từ `main`, rebase lên `phase3-trends` 2026-10-24), migration `0007_ui_flow`. Số đo thật ở “Kết quả chạy thật — Task 10–11”.

## Tasks

### Task 1: Nhánh + lấy logic từ stash
- [ ] `git switch -c phase1-explorer`
- [ ] Lấy nguyên: `src/collectors/suggest.ts`, `src/collectors/explore-metrics.ts`, `src/lib/explore.ts`,
      `src/lib/explore-view.ts`, `src/lib/explore-deps.ts`, `tests/explore*.test.ts`. Sửa import cho khớp main.
- [ ] Ghép phần bảng mới (`explorations`, `explore_nodes`, `node_sources`, `node_metrics`, `node_runs`, `suggest_cache`)
      từ `db/schema.ts` của stash vào schema main. **Không** lấy `drizzle/0002_harsh_blockbuster.sql`;
      chạy `npm run db:generate` → `0003_*`.
- [ ] Sửa `collectors/appstore.ts` / `playstore.ts` nếu stash cần export thêm (`fetchItunes`, `itunesLimit`, `playLimit`).
- Kiểm: test explore cũ xanh trên main mới.

### Task 2: Điểm cơ hội
- [ ] Trong `explore-view.ts`: thêm `crowdRatio(top5)` và `opportunity(popularity, top5)` theo công thức ở trên;
      `crowdLevel` đổi sang ngưỡng 0.4 / 0.7 của `crowdRatio`.
- [ ] `opportunities` (Top cơ hội) sắp theo điểm cơ hội giảm dần, lấy 10.
- [ ] Test: 0 rating → độ đông 0, điểm = phổ biến; 1M rating → điểm 0; biên 0.4 / 0.7.

### Task 3: Route Hono
- [ ] Trong `src/server/app.ts`: `POST /api/explore` · `GET /api/explore` (danh sách) · `GET /api/explore/:id` ·
      `POST /api/explore/:id/expand` (body `{nodeId}`) · `POST /api/explore/:id/deep` (body `{nodeIds}`, **1–5**) ·
      `GET /api/explore/:id/csv`. Logic lấy từ 5 file `src/app/api/explore/**/route.ts` của stash.
- [ ] Validate body như route research hiện có; lỗi `ExploreError` → đúng status.
- [ ] `startDeep`: đổi giới hạn 10 → 5, message "Chọn 1–5 keyword khác nhau".
- [ ] Test API (port `tests/explore-api.test.ts` sang `app.request()` của Hono).

### Task 4: Trang `/explore` và `/explore/:id`
- [ ] `src/client/ExplorePage.tsx` + route trong `main.tsx`. Trang chủ thêm lựa chọn "Research 1 keyword" | "Explore niche".
- [ ] Lấy `ExploreDashboard`, `ExploreShared`, `NicheMap`, `ExploreButton` từ stash, bỏ phần Next (`next/link`,
      `'use client'`) → React Router `Link`. Polling 2 giây như `RunPage`.
- [ ] Cây gập/mở theo nhóm (đối tượng / dạng / nền tảng / tính năng), nút "Mở tiếp" mỗi node (ẩn khi depth = 3).
- [ ] Bảng keyword: cột nguồn, phổ biến, số app Play, số app iOS, độ đông (chấm màu), **điểm cơ hội**; sắp xếp được;
      dòng công thức ngay trên bảng.
- [ ] Ô "Explore từ đây" trong bảng Keyword × Store của dashboard v1 (`DrillLink`).

### Task 5: Bản đồ ngách + Top cơ hội
- [ ] Scatter phổ biến (trục dọc) × độ đông (trục ngang), màu theo sub-niche, tooltip tên keyword + điểm.
- [ ] Bảng Top 10 cơ hội cạnh bản đồ, mỗi dòng có checkbox để chọn research sâu.

### Task 6: Research sâu hàng loạt ≤ 5
- [ ] Tick 1–5 keyword → `POST deep` → hàng đợi chạy lần lượt, mỗi keyword thành một run v1 (`node_runs`), dòng hiện
      link sang `/r/:id` khi xong.

### Task 7: Xuất CSV
- [ ] Nút "Tải CSV" → `GET /api/explore/:id/csv`; thêm cột `opportunity`. Test: escape dấu phẩy/ngoặc kép.

### Task 8: Đối thủ bị chê gì (review 1–2★ Play)
- [ ] Collector mới `src/collectors/play-reviews.ts`: `gplay.reviews` cho top 3 app Play của run, sort mới nhất,
      100 review/app, lọc score ≤ 2, qua `playLimit`. Cache theo run.
- [ ] `lib/complaints.ts` (thuần, có test): tách từ, bỏ stopword, đếm cụm 1–3 từ lặp ≥ 3 lần → top 10 cụm kèm 2 câu trích.
- [ ] Khối "Đối thủ bị chê gì" trên dashboard run v1. Không AI.

### Task 9: Nợ UX v1 + kiểm thật
- [ ] Nguồn trả `RATE_LIMITED` → dòng "Nguồn đang chặn tạm — thử lại sau 10–30 phút" cạnh nút Thử lại.
- [ ] `npm run smoke -- "habit tracker" US` + chạy UI thật: `habit tracker` US → đo số keyword, thời gian; chụp màn
      `/explore/:id` (1280 + 375), bản đồ, CSV mở được, khối chê. Read từng screenshot.
- [ ] Cập nhật README (lệnh + màn mới) và master plan (Phase 1 → XONG, ngày, số đo thật).
- [ ] Merge `phase1-explorer` vào `main`. Xoá stash **chỉ khi anh đồng ý**.

### Task 10: UI Loading — tiến độ, ước lượng, checklist, quay lại được (thêm 2026-10-24)

> Vấn đề: một lượt tra mất 1–6 phút, chỉ thấy skeleton xám cao 446–1086px → không biết đang làm gì, còn bao lâu, cái
> nào xong. Đóng tab thì không biết xem lại ở đâu.

- [x] Migration mới (số kế tiếp lúc làm): `source_jobs.progress_done/progress_total`,
      `explorations.progress_done/progress_total`. Collector Play/App Store/Trends/Reddit + vòng đo keyword của Explore
      gọi `onProgress(n, total)` sau mỗi keyword. Test: số tăng đúng, lỗi giữa chừng vẫn giữ số đã tới.
- [x] `lib/eta.ts` (thuần, có test): trung vị `finishedAt − startedAt` 20 job `done` gần nhất cùng nguồn, chia theo số
      keyword → còn lại × mỗi keyword. Explore: keyword còn lại × 3 giây. Không có lịch sử → số đo thật (50 keyword ≈
      4 phút, 100 ≈ 6,3 phút) + cờ `estimate: 'mặc định'`. Lấy từ cache → `instant`.
- [x] `components/ProgressPanel.tsx`: thanh tổng + mỗi nguồn 1 dòng (icon · chữ đang làm gì · `3/6` · ✓/✗/⏳ · thời gian
      chạy), dòng "Còn khoảng ~X phút · đã chạy 1:20", dòng "Có thể đóng tab — tool vẫn chạy, xem lại ở Lịch sử".
      Dùng ở `RunDashboard` + `ExploreDashboard`, thay `DashboardSkeleton` cả trang. `SourceBlock` chỉ giữ skeleton
      ≤ 160px có chữ "Chờ <nguồn>…". Tắt hiệu ứng khi `prefers-reduced-motion`.
- [x] Xong → panel thành "Tóm tắt lượt tra" (gập được): ✓ nguồn · số ra được · thời gian; ✗ nguồn · lý do · nút Thử lại.
      Tiêu đề tab "✓ Xong — <niche>". Nút "Báo tôi khi xong" → `Notification.requestPermission()` chỉ khi bấm.
- [x] `GET /api/activity`: run + explore đang chạy và xong trong 24h. Nav có huy hiệu "1 đang chạy"; Lịch sử ghim lượt
      đang chạy lên đầu kèm thanh tiến độ; trang chủ có banner "Lượt tra '<niche>' xong lúc HH:MM — Xem". `localStorage`
      chỉ nhớ id đã xem (bọc try/catch). Server tắt giữa chừng → `markInterrupted` (đã có) → checklist "Bị dừng vì
      server tắt — Thử lại".
- [x] Mockup trước khi code: `design/mockups/phase1-ui-flow/` ảnh 01–02 (đang chạy, tóm tắt xong); 03 chưa sinh (Codex hết lượt)
      — Codex sinh 2026-10-24, Claude soát.
- Không làm: WebSocket/SSE (giữ poll 2 giây), push từ server.
- Kiểm: 1 research + 1 explore thật, ghi ước lượng lúc đầu vs thời gian thật (lệch ≤ 50%); đóng tab giữa chừng, mở lại
  `/r/:id` + `/explore/:id` thấy đúng tiến độ; screenshot đang chạy + đã xong ở 1280 + 375, Read từng ảnh.

### Task 11: UI Flow niche — thanh bước đầu trang + sơ đồ nhánh + FLOW 1, 2… (thêm 2026-10-24)

> Mục tiêu UX: luôn biết **đang đi hướng nào, tới bước nào**. Research `bubble game` → Explore → Mở rộng
> `bubble shooter` → Mở rộng `bubble shooter offline` → Research sâu. Lá cuối một nhánh = long-tail niche; một đường
> gốc → lá được chốt = **FLOW niche N**.

- [x] Migration: `explorations.source_run_id` (Explore mở từ trang Research nào — `ExploreButton`/`DrillLink` gửi kèm),
      `explorations.current_node_id` (node vừa mở rộng / đang xem), bảng `flows` (id, exploration_id, leaf_node_id, n,
      note, created_at; unique exploration + leaf). Đường đi tính lại từ chuỗi `parentId`, không lưu trùng.
- [x] `lib/flow-path.ts` (thuần, có test): dựng chuỗi bước từ `runs.parentRunId` → `source_run_id` → `explore_nodes`
      (`parentId`, `depth` ≤ 3) → `node_runs`; mỗi bước có loại (Research / Explore / Mở rộng / Research sâu), term,
      trạng thái, link. Test: run → explore → 2 tầng mở rộng → research sâu ra đúng 5 bước.
- [x] API: `GET /api/explore/:id/flow` (bước + cây rút gọn + danh sách FLOW), `POST /api/explore/:id/flows`
      `{nodeId}` → FLOW N, `POST /api/explore/:id/flows/:flowId/delete`, `POST /api/explore/:id/current` `{nodeId}` (POST thay DELETE/PATCH để dùng
      chung chốt chặn CSRF `guardJsonPost`), `GET /api/research/:id/flow`.
- [x] `components/FlowSteps.tsx`: thanh bước ngay dưới nav, trên tiêu đề (cả `/r/:id` + `/explore/:id`):
      `① Research bubble game ✓ → ② Explore ✓ 100 keyword → ③ Mở rộng bubble shooter ⏳ 12/50`. Bước hiện tại tô đậm,
      bước đã qua bấm được; bước đang chạy lấy tiến độ từ Task 10 (một thanh duy nhất). 375px: bước trước · hiện tại ·
      "3/5", vuốt ngang xem hết.
- [x] `components/FlowMap.tsx`: khối gập/mở, cây ngang gốc trái → phải, chỉ vẽ node đã mở rộng hoặc research sâu; nhánh
      đang đi tô màu, nhánh khác mờ, nhãn `FLOW 1`/`FLOW 2`; bấm node → cuộn tới keyword trong bảng. Mỗi node có nút
      "Chốt làm long-tail niche". Danh sách cuối khối: `FLOW niche 1 · bubble game → bubble shooter → bubble shooter
      offline · điểm cơ hội 64 · research sâu ✓` + Bỏ chốt.
- [ ] Mockup 04–06: chỉ 06 (điện thoại 375) đạt; 04 chưa sinh, 05 bản đầu bị loại — Codex hết lượt 2026-10-24.
      Code đã làm thẳng, duyệt bằng screenshot app thật.
- Không làm: gộp FLOW giữa nhiều lượt Explore · AI chọn lá (Phase 4–5) · kéo-thả sơ đồ · vượt độ sâu 3.
- Kiểm: đi thật `bubble game` (US) Research → Explore → mở rộng 2 tầng → chốt 2 FLOW → thanh bước đúng vị trí, sơ đồ có
  2 nhánh nhãn FLOW 1 / FLOW 2, đóng tab mở lại vẫn đúng bước; screenshot 1280 + 375, Read từng ảnh.

### Ghi chú làm Task 10–11

- Phase 1 đã ở `main`; nhánh `phase2-appstore-money` đang chạy song song và cũng sửa `schema.ts` → cắt nhánh
  `phase1-ui-flow` từ `main` sau khi Phase 2 merge, hoặc rebase trước khi tạo migration để số migration không đụng nhau.
- Đụng `RunDashboard`, `ExploreDashboard`, `SourceBlock`, `AppShell` (nav) — Phase 2 thêm cột/khối vào cùng trang,
  nên làm Task 10–11 sau khi khối "Tiền thật" của Phase 2 đã vào để không viết lại bố cục hai lần.

### Kết quả chạy thật — Task 10–11 (2026-10-24, sau khi gộp lên Phase 3)

- Research `bubble shooter` (US, #17): xong 1:04, panel tiến độ từng nguồn → tự gập thành "Tóm tắt lượt tra";
  Trends lỗi (Google chặn tạm), Reddit bỏ qua (chưa có key) — hiện rõ ✗ + lý do.
- Explore từ trang Research (#12, `source_run_id` = 17): 101 keyword, chạy thật **6:26**, ước lượng lúc đầu "~6 phút" (lệch ~7%).
- Thanh bước `① Research bubble shooter ✓ → ② Explore ✓ 100 keyword` đúng; chốt 2 keyword → sơ đồ có 2 nhánh FLOW 1 / FLOW 2,
  danh sách FLOW niche + Bỏ chốt; tải lại trang vẫn giữ. 375px: không cuộn ngang trang, sơ đồ vuốt ngang bên trong.
- Chưa đi thật: mở rộng 2 tầng (mỗi tầng ~4 phút gọi Google dồn, lúc đo Google đang chặn tạm) — có test `flow-path` 5 bước.
- Gộp với Phase 2–3: ProgressPanel thay thanh báo cũ; thanh báo dính đầu trang chỉ hiện khi cuộn khuất panel.

## Rủi ro

- Google suggest / Play chặn IP khi mở rộng dồn dập → đã có limiter + cache 7 ngày; gặp `RATE_LIMITED` thì dừng
  mở rộng, giữ phần đã lấy, báo trên UI.
- Độ đông chỉ từ App Store → keyword chỉ mạnh trên Play có thể bị chấm "ít đông" sai. Chấp nhận ở Phase 1, ghi trên UI;
  Phase 2 thêm số liệu iOS/Play đầy đủ hơn.
- `gplay.reviews` có thể gãy khi Google đổi trang → khối chê báo "nguồn lỗi", không chặn phần còn lại.

## Kết quả chạy thật

2026-10-24, chạy UI thật, nước US:

| Niche | Keyword | Đủ số liệu | Thời gian | Kết quả |
|---|---|---|---|---|
| pomodoro timer | 51 | 50 | ~3,5 phút | lỗi `play_suggest: Cannot read properties of null (reading 'map')` |
| water reminder | 51 | 50 | ~3,7 phút | cùng lỗi |
| meal planner | 51 | 50 | ~4 phút | `done`, không lỗi |

- Lỗi: `google-play-scraper` `suggest` đọc `data[0][0].map` → `TypeError` khi Play không có gợi ý cho chữ đó
  (`water reminder q/x/z`). Sửa ở `collectors/suggest.ts`: `TypeError` từ `gplay.suggest` = `[]`; thêm test null → `[]`.
- Lệch tiêu chí: mỗi lần chỉ 50 keyword (trần 50/lần) và ~4 phút (iTunes 1 req/3s × 50) → chưa đạt "≥ 80 trong ≤ 3 phút".
- Điểm phổ biến hầu như chỉ 80 hoặc 100 → điểm cơ hội gần như chỉ theo độ đông. Nhãn bản đồ chồng nhau.
- Tài liệu MkDocs: `mkdocs.yml` + `docs/index.md`, `cach-dung.md`, `cong-nghe.md`, `tien-do.md` (`npm run docs`).
