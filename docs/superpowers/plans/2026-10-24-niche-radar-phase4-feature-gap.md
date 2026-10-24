# niche-radar Phase 4 — Feature Gap Matrix — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm test && npm run typecheck && npm run lint`
> xanh rồi mới commit. Steps dùng checkbox (`- [ ]`).

**Goal:** biết đối thủ đang **thiếu** tính năng gì → chỗ để app mình khác biệt (wedge).

**Spec:** `docs/phase-4-feature-gap.md` + master plan §3 Phase 4.

## Mục tiêu · làm · không làm

- **Xong khi:** 3 niche thật có matrix ≥ 5 app × 10 hàng, ≤ 20% ô còn `?`, mọi ô `Có/Không/Trả phí` có câu nguồn + link ·
  tuyến A và tuyến B mỗi tuyến chạy được ít nhất 1 lần · screenshot đã Read.
- **Làm:** khối mới "Feature Gap Matrix" trên trang Research `/r/:id`, **bấm mới tải**, 5 Task bên dưới.
- **Không làm:** lớp AI đầy đủ (chọn provider, trần chi phí, trang cài đặt — Phase 6) · AI điền ô mà không có câu nguồn ·
  đọc ảnh chụp màn hình store · matrix trên trang Explore.

## Đo trước khi code (2026-10-24)

| Gọi | Có gì |
|---|---|
| `gplay.app({appId})` | `description` (~2.100 ký tự), `adSupported` (nhãn "Contains ads"), `offersIAP`, `IAPRange` |
| `itunes.apple.com/lookup?id=` | `description` (~3.900 ký tự); `features` rỗng → không dùng |
| `iap_cache` (Phase 2) | tên + giá từng gói IAP iOS (gói tuần/tháng/năm, lifetime) |

## Global Constraints

- Hàng mặc định (10): offline · không quảng cáo · widget · đồng bộ · mua một lần · subscription · dùng thử · AI ·
  xuất dữ liệu · không cần tài khoản. Thêm/xoá hàng riêng của run (nhãn + từ khoá).
- App: top 5 mỗi store theo số rating (đúng thứ tự bảng đối thủ).
- Ô: `yes` (Có) · `no` (Không) · `paid` (Trả phí — có nhưng sau Pro) · `unknown` (?). Ô ≠ `?` **bắt buộc** câu nguồn
  + link; `by` = `rule` | `ai` | `chrome`. Ô của AI/Chrome không bị luật ghi đè.
- Không nhắc ≠ không có → luật chỉ ghi `no` khi có bằng chứng (vd Play gắn nhãn có quảng cáo, không có IAP).
- Khoảng trống: số app Có/Trả phí ≤ 1/5 số app **và** ô `?` ≤ 1/5 → "Khoảng trống"; ít app có nhưng nhiều `?` → "chưa chắc".
- Tuyến A: `@anthropic-ai/sdk`, model `claude-opus-5-5`, **tắt mặc định** — cần `NICHE_AI=1` + `ANTHROPIC_API_KEY` trong
  `.env.local`. Chỉ hỏi ô `?`; câu nguồn AI trả phải **khớp nguyên văn** mô tả đã gửi, không khớp → bỏ.
- Tuyến B: tải file job `.json` → Claude (Chrome / Claude Code) đọc trang listing → nhập file kết quả. Ô không có câu
  nguồn → bỏ.
- Listing cache 7 ngày (`listing_cache`), gọi thưa (Play 1 req/giây, Apple 2 giây).

## Tasks

### Task 1: Listing + luật từ khoá
- [x] Bảng `listing_cache`, `gap_cells`, `gap_rows` (migration `0008`).
- [x] `collectors/listing.ts`: Play `gplay.app`, iOS iTunes lookup → `{ description, adSupported }`, cache 7 ngày.
- [x] `lib/feature-gap.ts`: 10 hàng + luật (câu chứa từ khoá → câu nguồn; câu có premium/pro/upgrade → `paid`),
      IAP iOS → subscription / mua một lần, Play `adSupported` / `offersIAP` → quảng cáo / subscription.
- [x] Test luật trên mô tả giả + bản đo thật.

### Task 2: API matrix + cột Khoảng trống
- [x] `GET /api/research/:id/gap` dựng matrix (đọc listing còn thiếu), trộn ô AI/Chrome đã lưu, tính Khoảng trống.
- [x] `POST /api/research/:id/gap/rows` thêm hàng · `POST …/gap/rows/:key/delete` xoá hàng.

### Task 3: Tuyến A — AI API key
- [x] `lib/gap-ai.ts`: gửi mô tả + danh sách ô `?`, structured output JSON, lọc câu nguồn không khớp nguyên văn.
- [x] `POST /api/research/:id/gap/ai` (tắt → 400 kèm hướng dẫn bật). Test bằng client giả.
- [ ] **Chạy thật tuyến A** — máy chưa có `ANTHROPIC_API_KEY` (anh thêm vào `.env.local` + `NICHE_AI=1`).

### Task 4: Tuyến B — job Claude in Chrome
- [x] `GET /api/research/:id/gap/job` → file `.json` (link listing, ô `?`, định dạng trả về, luật câu nguồn).
- [x] `POST /api/research/:id/gap/import` nhận kết quả, bỏ ô thiếu câu nguồn, lưu `by: chrome`.

### Task 5: UI + chạy thật
- [x] `GapMatrixBlock`: nút dựng, bảng hàng × app (chip Có/Không/Trả phí/?, rê chuột xem câu nguồn, link), cột Khoảng
      trống, nút AI / tải job / nhập kết quả, thêm hàng.
- [x] Chạy thật 3 niche + tuyến B (30 trang store) — 0% `?` sau khi thêm “Không nói” → bảng kết quả cuối file. Screenshot 1280 + 375.

## Tiến độ

- 2026-10-24: đo listing, viết plan.
- 2026-10-24: Task 1–5 code xong, 191 test. Sửa luật sau khi đọc trang thật: "subscriptions" trong app tài chính là hoá đơn
  của người dùng (cần ngữ cảnh giá/gói) · app bán gói qua web không có mục IAP (Cleo, Albert) → đọc mô tả trước khi kết
  luận "Không" · dòng dưới tiêu đề "Upgraded…:" / "* Paid version *" = Trả phí · "free to try" = dùng thử · "synchronization".

## Kết quả chạy thật

Đo 2026-10-24, US, top 5 app mỗi store × 10 hàng (100 ô):

| Run | Luật | Claude in Chrome | Còn `?` | Khoảng trống |
|---|---|---|---|---|
| budget tracker (#14) | 18 | 18 (nhập 18/18, bỏ 0) | **64%** | chưa thấy · "ít app có, còn ?": Offline, Widget, Không cần tài khoản |
| habit tracker (#13) | 27 | — | 73% | chưa thấy |
| pomodoro timer (#15) | 20 | — | 80% | chưa thấy |

**Đọc:** tuyến B đọc *cả trang store* (mô tả + What's new + review) của 10 app `budget tracker` mà chỉ chứng minh thêm
được 18 ô — trang store không nhắc phần lớn tính năng (offline, widget, tài khoản…). Với luật "không nhắc ≠ không có",
mục tiêu ≤ 20% `?` **không đạt được chỉ từ trang store**. Cần anh chốt: (a) thêm trạng thái "Không nói" (trang store đã
đọc hết mà không quảng cáo) — chính nó là khoảng trống *định vị*; hoặc (b) cho tuyến B đọc thêm web/help center của app;
hoặc (c) hạ mục tiêu. Tuyến A chưa chạy thật (chưa có key).

**Anh chốt 2026-10-24: thêm “Không nói”.** Sau khi tuyến B đọc hết trang store của cả 3 niche:

| Run | Có | Trả phí | Không | Không nói | `?` | Khoảng trống định vị |
|---|---|---|---|---|---|---|
| budget tracker (#14) | 27 | 7 | 2 | 64 | 0% | Offline · Widget · Không cần tài khoản |
| habit tracker (#13) | 24 | 2 | 5 | 69 | 0% | Offline · Dùng thử · AI · Xuất dữ liệu · Không cần tài khoản |
| pomodoro timer (#15) | 19 | 2 | 4 | 75 | 0% | Offline · Mua một lần · Dùng thử · AI · Xuất dữ liệu · Không cần tài khoản |

**Đọc:** cả 3 niche, không app top nào quảng cáo **offline** và **không cần tài khoản** — wedge định vị lặp lại. Chưa có khoảng trống *tính năng* (đối thủ nói rõ không có) ở niche nào.

Sửa luật thêm khi đọc 20 trang sau: "without creating an account" · tiêu đề VIẾT HOA ("STRUCTURED PRO") · "removes ads".
