# niche-radar Phase 2 — App Store + Tiền thật — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm test && npm run typecheck && npm run lint`
> xanh rồi mới commit. Steps dùng checkbox (`- [ ]`).

**Goal:** cùng câu hỏi Phase 1 cho iOS, cộng thêm "ai đang thu tiền, thu bao nhiêu": gợi ý App Store làm nguồn keyword
thứ 3, câu than 1–2★ cả Play + iOS, cột Tiền + nhãn "chỉ 1 store" ở bảng đối thủ, khối "Tiền thật — TrustMRR".

> **Lộ trình 11 phase (2026-10-24):** Task 6 (TrustMRR) và phần TrustMRR của Task 7 giờ thuộc **Phase 5 · Verified Sites** (`docs/phase-5-verified.md`).
> Plan này giữ nguyên để làm tiếp cho liền; tick xong thì tính vào Phase 5.

**Spec:** master plan §3 Phase 2 (`../specs/2026-10-24-niche-radar-master-plan.md`) + `docs/phase-2-app-store.md`.
**Mockup:** `design/mockups/phase2-money/` (Codex sinh từ `image-prompts.md`).

## Mục tiêu · làm · không làm

- **Xong khi** (y master plan): 3 niche thật có câu than cả Play + iOS · cột Tiền có số cho ≥ 4/5 top app iOS · khối
  TrustMRR có ≥ 1 dòng cho 2/3 niche (hoặc ghi rõ "không có sản phẩm cùng ngách" + ngày tra) · test xanh, chạy thật
  không bị chặn · screenshot đã Read.
- **Làm:** đúng 8 Task bên dưới.
- **Không làm:** ước doanh thu từ rating/lượt cài · coi TrustMRR là khớp chính xác · giá nhiều nước · nguồn verified
  khác ngoài TrustMRR (tuỳ chọn trong master plan → để §4 pending, chưa có ứng viên đã kiểm) · AI.

## Đo endpoint trước khi code (2026-10-24, US, curl)

| Nguồn | Kết quả | Dùng thế nào |
|---|---|---|
| App Store search hints `search.itunes.apple.com/WebObjects/MZSearchHints.woa/wa/hints?clientApplication=Software&term=…` + header `X-Apple-Store-Front: <sf>-1,29` | ✅ trả plist, có `<key>term</key>` | nguồn `appstore_hint` cho Explorer |
| iOS review RSS `itunes.apple.com/<cc>/rss/customerreviews/…/json` | ❌ **chết** — feed không còn `entry` cho mọi app thử (HabitKit, Finch, Habit Tracker) | bỏ |
| iOS review qua proxy web `apps.apple.com/api/apps/v1/catalog/<cc>/apps/<id>/reviews?l=en-US&offset=0&limit=20&platform=web&additionalPlatforms=appletv,ipad,iphone,mac&sort=recent` | ✅ 200, không cần token, có `next` để phân trang, mỗi dòng `rating/title/review/date` | **thay RSS** — 3 trang × 20 = 60 review mới nhất |
| Gói IAP iOS trên `apps.apple.com/<cc>/app/id<id>` | ✅ nhưng **định dạng đổi**: `"In-App Purchases","summary":"Yes","items":[{"$kind":"textPair","leadingText":"…","trailingText":"$4.99"}…]` (regex `textPairs` cũ của `store_research.py` không khớp) | parse `leadingText/trailingText` |
| TrustMRR `trustmrr.com/category/<slug>` | ✅ HTML có JSON nhúng (escape `\"`): `name, description, currentMrr, currentLast30DaysRevenue, currentTotalRevenue, slug, onSale` — top 30 mỗi category, 30 category | quét category → khớp từ khoá |
| TrustMRR `trustmrr.com/startup/<slug>.md` | ✅ có provider, `Revenue last synced`, `Mobile app`, `Current MRR` | chi tiết top 5 dòng khớp |
| TrustMRR `trustmrr.com/search?q=` | ⚠️ render phía trình duyệt, HTML không có kết quả | không dùng |
| TrustMRR API `api/v1/startups?q=` (Bearer `TRUSTMRR_API_KEY`) | chưa kiểm (chưa có key) | tuỳ chọn, có key mới gọi |

Ghi nhận: HabitKit trên TrustMRR có "Last 30 days $0" nhưng "Current MRR $33,339", sync 2026-09-09 → đúng ca
"số 30 ngày = 0 giả" → UI cảnh báo khi sync > 30 ngày.

## Global Constraints

- Nhánh `phase2-appstore-money` cắt từ `main` (Phase 1 đã merge fast-forward 2026-10-24).
- Nhịp gọi: iTunes search 1 req/3s (giữ `itunesLimit`); hints + `apps.apple.com` dùng chung limiter mới `appleWebLimit`
  1 req/2s; TrustMRR 1 req/2s. Timeout 20s mỗi request.
- Cache: hints 7 ngày (`suggest_cache`, thêm source `appstore_hint`); review iOS 7 ngày (`review_cache`, id iOS toàn
  số nên không trùng id Play); IAP 7 ngày (bảng `iap_cache`); TrustMRR category 7 ngày (`trustmrr_cache`, key = URL).
- Mọi số tiền đến từ nguồn (store / TrustMRR). Không đoán. Không có thì `chưa đo`.
- Câu than + TrustMRR **bấm mới tải** (như Phase 1) — không làm chậm lần tra chính.

## Tasks

### Task 1: Gợi ý App Store làm nguồn keyword thứ 3 (Explorer)
- [x] `suggest.ts`: `SuggestSource` thêm `'appstore_hint'`; `fetchSuggest` nhánh hints (plist → list term, unescape HTML);
      `discoverKeywords` chạy cả 3 nguồn song song. Storefront theo nước (bảng US/GB/CA/AU/DE/FR/JP/KR/VN/BR…, nước khác → US).
- [x] Schema `suggest_cache.source` enum thêm `appstore_hint` (SQLite text, không cần migration dữ liệu).
- [x] UI chip nguồn trong bảng keyword hiện icon App Store khi có `appstore_hint`.
- [x] Test: parse plist mẫu; `discoverKeywords` gom 3 nguồn; nguồn hint lỗi không làm hỏng 2 nguồn kia.

### Task 2: Play — giữ free/IAP từ trang app
- [x] `StoreApp` thêm `offersIap: boolean | null`, `iapRange: string | null`; `normalizePlayApp` lấy `offersIAP`, `IAPRange`.
- [x] `app_snapshots` thêm cột `offers_iap`, `iap_range` → migration `0005`.
- [x] `CompetitorRow` mang 2 trường này. Test normalize + run-view.

### Task 3: iOS — gói IAP top 5 app (bấm mới tải cùng khối Tiền, tự gọi khi mở run)
- [x] `collectors/appstore-web.ts`: `appleWebLimit`, `fetchIapItems(id, country)` parse `leadingText/trailingText`.
- [x] Bảng `iap_cache(store_app_id, country, items json, fetched_at)` (migration `0005`).
- [x] `lib/money.ts`: `moneyLabel(app, iapItems?)` → `Free` · `Trả tiền $X` · `IAP $a–$b` · `Sub ~$X/tháng` · `chưa đo`.
      Sub: tên gói khớp week/month/year/annual/premium/pro/plus/subscri → quy về tháng (tuần ×4.33, năm ÷12), lấy gói rẻ nhất/tháng.
- [x] `GET /api/research/:id/money` → nhãn tiền cho top 5 iOS (theo số rating) + mọi app Play (từ snapshot).
- [x] Test: parse HTML mẫu (định dạng mới), moneyLabel từng ca, endpoint với fetcher giả.

### Task 4: Khoảng trống Play ↔ iOS
- [x] `lib/store-gap.ts`: ghép app 2 store theo tên chuẩn hoá (bỏ dấu câu, phần sau `:`/`-`, chữ thường) hoặc cùng developer + tên
      giống ≥ 0.8 → nhãn `2 store` / `chỉ Play` / `chỉ iOS`. Thêm vào `CompetitorRow.storeGap`.
- [x] Test: ghép đúng "Habit Tracker - HabitKit" ↔ "HabitKit: Habit Tracker", không ghép 2 app khác tên.

### Task 5: Review 1–2★ iOS vào "Đối thủ bị chê gì"
- [x] `collectors/appstore-reviews.ts`: `fetchIosReviews` qua proxy `apps.apple.com/api/apps/…/reviews` 3 trang, `lowIosReviews`
      dùng `review_cache`.
- [x] Endpoint complaints: top 3 Play + top 3 iOS; mỗi app ghi `store`; mỗi cụm từ có đếm theo store (`byStore`).
- [x] Test: parse JSON mẫu, phân trang dừng khi hết `next`, endpoint gộp 2 store.

### Task 6: Tiền thật — TrustMRR
- [x] `collectors/trustmrr.ts`: `fetchCategory(slug)` parse JSON nhúng; `fetchStartupMd(slug)` lấy provider, sync, mobile, MRR,
      30 ngày; cache 7 ngày (`trustmrr_cache`, migration `0005`). Có `TRUSTMRR_API_KEY` → gọi `api/v1/startups?q=` trước.
- [x] `lib/trustmrr-match.ts`: token niche (bỏ stopword + từ chung "app/tracker"? — không, giữ "tracker"), điểm = số token trùng trong
      name+description; giữ dòng ≥ 1 token chính (token dài nhất của niche), xếp theo điểm rồi MRR, top 8. Nhãn luôn "khớp gần đúng".
- [x] `GET /api/research/:id/trustmrr` → `{ checkedAt, rows[], categoriesScanned, note }`; rỗng → note "TrustMRR không có sản phẩm
      cùng ngách" + ngày.
- [x] Test: parse category HTML mẫu, parse .md mẫu (HabitKit), match, cảnh báo sync > 30 ngày.

### Task 7: UI theo mockup
- [x] `CompetitorBlock`: cột Tiền + Store, tab "Chỉ 1 store", ghi chú nguồn tiền.
- [x] `ComplaintsBlock`: 2 store, chip app theo màu store, đếm theo store.
- [x] `TrustMrrBlock` mới trên trang run: nút "Tra TrustMRR", bảng, nhãn verified, cảnh báo sync cũ.
- [x] Test render (renderToStaticMarkup) cho 3 khối.

### Task 8: Build + chạy thật 3 niche + tài liệu
- [x] `npm run build && npm start` — mở được, không lỗi console. `npm run docs:build`.
- [x] Chạy thật: `habit tracker`, `budget tracker`, `pomodoro timer` (US) → điền bảng "Kết quả chạy thật". Screenshot đã Read.
- [ ] Master plan §3 trạng thái Phase 2, `docs/phase-2-app-store.md` chip → xong, §4 pending cập nhật.

## Tiến độ

- 2026-10-24: đo endpoint (bảng trên), viết plan, giao Codex mockup (`design/mockups/phase2-money/01-*.png`, `02-*.png`).
- Task 1–8 code xong trên nhánh `phase2-appstore-money`, 146 test xanh, typecheck + lint + build + docs:build sạch, `npm start` mở được.
- **Lệch so với plan (ghi lại vì sao):**
  - Task 1: gợi ý App Store chỉ chạy truy vấn bắt đầu bằng niche (`habit tracker a…z` + mẫu), bỏ dạng `a habit tracker` — endpoint khớp theo tiền tố, đỡ ~26 request × 2 giây.
  - Task 3: lowPlayReviews đổi tên `lowReviews` (nhận fetcher) để dùng chung Play + iOS, không viết bản trùng.
  - Task 4: thêm 2 luật sau khi chạy thật — ghép theo tên thương hiệu trước `:`/` - ` ("Forest: …"), và từ có trong ≥ 4 tên app của run coi là từ chung (pomodoro: "Pomodoro - Focus Timer" bị ghép nhầm trước đó).
  - Task 6: API có key của TrustMRR không tìm theo từ khoá (chỉ lọc category) và chưa có key để kiểm → **không làm**, dùng trang công khai. Top 30 mỗi category chỉ phủ ~625 startup → thêm đường thứ 2: thử trang `startup/<tên app đối thủ>.md`, chỉ nhận khi ghi `Mobile app: Yes`. Khớp từ khoá phải chứa **đủ** mọi từ của niche (bản "từ dài nhất" cho ra app du lịch với `meal planner`).
  - Complaints: thêm từ dừng (`cant`, `doesnt`, `back`, `new`, `time`…). Cụm từ vẫn còn thô — đọc sâu bằng AI là việc Phase sau.
- Lộ trình 11 phase (phiên khác cập nhật cùng ngày): TrustMRR (Task 6 + khối UI) tính vào **Phase 5 · Verified Sites**. Trang `docs/phase-*.md` và master plan do phiên đó giữ — chưa sửa trạng thái ở đây.

## Kết quả chạy thật

Đo 2026-10-24, US, run mới (`force`), dev server máy nhà, không bị chặn lần nào.

| Niche | Run | Tiền iOS top 5 | Câu than (app ≤2★/review đọc) | TrustMRR | Ghép 2 store |
|---|---|---|---|---|---|
| habit tracker | #13 | 5/5 có nhãn (Finch IAP $5.99–$69.99, Me+ Sub ~$12.99/tháng…) | Play 3 app (54/150, 56/150, 16/150) · iOS 3 app (3/40, 4/40, 7/40) | 1 dòng: nutrIA — MRR $18,073, 30 ngày $38,865, RevenueCat, sync 2026-10-24 | 20 cả 2 · 40 chỉ Play · 58 chỉ iOS |
| budget tracker | #14 | 5/5 (Rocket Money IAP $2.99–$9.99, Monarch Sub ~$14.99/tháng, EveryDollar Sub ~$17.99/tháng…) | Play 6/150, 1/150, 26/150 · iOS 29/40, 21/40, 27/40 — iOS than "subscription/cancel/scam" | "không có sản phẩm cùng ngách" (625 startup + 8 tên app, 2026-10-24) | 30 · 35 · 79 |
| pomodoro timer | #15 | 5/5 (Forest Sub ~$5.99/tháng, Timer+ IAP $0.99–$44.99…) | Play 24/150, 10/150, 25/150 · iOS 21/40, 0/40, 10/40 | "không có sản phẩm cùng ngách" (2026-10-24) | 2 · 38 · 84 |

Ghi chú: lúc chạy, iOS chỉ đọc 40 review/app vì `next` của Apple bỏ mất `limit` (trang 2–3 chỉ 10 review). Đã sửa: thêm lại `limit=20` → 60 review/app; cache cũ 7 ngày vẫn giữ số 40 tới khi hết hạn.
Screenshot đã xem: bảng đối thủ cột Tiền + Store (run #14), khối TrustMRR + câu than 2 store (run #13), 1280px.

→ Đạt "Xong khi": câu than cả Play + iOS ở 3/3 niche · cột Tiền 5/5 top iOS · TrustMRR 1/3 có dòng, 2/3 ghi rõ "không có" + ngày.
