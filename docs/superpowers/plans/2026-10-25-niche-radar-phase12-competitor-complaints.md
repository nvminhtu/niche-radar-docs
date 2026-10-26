# Niche Radar Phase 18 — Đối thủ bị chê gì — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** từ "vài cụm lặp lại" thành **bản đồ lời chê**: app nào bị chê gì, loại gì, mới nổi hay cũ, người dùng ước gì —
mọi dòng có câu nguyên văn. Không AI.

**Spec:** [Phase 18 · Đối thủ bị chê gì](../../web/phase-18-competitor-complaints.md) · **Cần trước:** Phase 1–2 (review),
Phase 9 (bảng mức nặng `severityOf` trong `lib/ai/themes.ts`).

## Mục tiêu · làm · không làm

- **Xong khi:** 3 niche thật, top 10 cụm mỗi niche ≥ 8/10 có nghĩa · số cụm trùng ý giảm rõ (đếm trước / sau, ghi số) ·
  bảng app × loại đọc được ở 1340px, ô bấm ra câu trích đúng app · "ước gì" ≥ 5 dòng ở ≥ 2/3 niche · test xanh · screenshot đã Read.
- **Làm:** lấy đủ review (có 3★), gộp cùng ý, loại lời chê, bảng app × loại, mới nổi, ước gì, lọc, đưa vào evidence pack.
- **Không làm:** AI gom chủ đề (Phase 28.1) · so 2–5 đối thủ (Phase 56) · review ngoài 2 store.

## Đo trước khi code

| Đo gì | Cách | Ghi vào |
|---|---|---|
| Số review lấy được / app, có `version` không, **150 / 60 review mới nhất phủ bao nhiêu ngày** | gọi `fetchPlayReviews` + `fetchIosReviews` (proxy apps.apple.com — RSS đã chết) cho 1 app lớn + 1 app nhỏ mỗi store | bảng này |
| Số cụm trùng ý hiện tại | chạy `topComplaints` trên 3 niche (budget tracker, habit tracker, pomodoro timer), đếm tay cụm trùng | "Kết quả chạy thật" — cột *trước* |

## Global Constraints

- Mỗi cụm ≥ 3 review **khác nhau**; câu trích phải **khớp nguyên văn** review gốc (kiểm bằng `includes` như Phase 6), không dịch, không viết lại.
- Luật gộp (gốc từ + đồng nghĩa) và luật loại nằm trong **1 file** `web/src/lib/complaint-rules.ts`; thêm từ không sửa code.
- 8 loại: Lỗi / crash · Mất dữ liệu · Ép trả phí / giá · Quảng cáo · Thiếu tính năng · Khó dùng · Đồng bộ / tài khoản · Khác.
  Mức nặng dùng chung `severityOf` của Phase 9 (không tạo bảng thứ hai).
- Top 5 app mỗi store: Play `SCAN` 150 → 200, App Store `REVIEW_PAGES` 3 → 5 (100 review, giữ `appleWebLimit`). Lọc giữ
  **1–3★** (hiện `score <= 2` ở `play-reviews.ts`). Cache 7 ngày (`review_cache`, `REVIEW_CACHE_MS`). Tên app + thương hiệu bị bỏ khỏi cụm.
- **Mới nổi không dựa vào "90 ngày" của một lần lấy** — 150 review mới nhất của app lớn chỉ phủ vài ngày. Bảng mới
  `review_seen` (storeAppId, country, hash = sha256 text, score, date, version, firstSeenAt) giữ mọi review 1–3★ đã thấy;
  `review_cache` vẫn bị ghi đè như cũ. Mới nổi = review có `firstSeenAt` ở lần lấy này so với phần còn lại; chỉ khi 200
  review đã phủ ≥ 180 ngày mới so thẳng theo `date`. Chưa có lần trước → `emerging: null` + lý do, không đoán.
- `review_seen` dùng chung cho cache "chỉ gửi review mới" của Phase 28.1 (không tạo bảng hash thứ hai).
- API cũ `GET /api/research/:id/complaints` giữ trường `complaints` để khối cũ không vỡ; thêm trường mới bên cạnh.

## File đụng tới

- `web/src/collectors/play-reviews.ts` + `appstore-web.ts` — giữ 1–3★, `version` (Play), ngày; Play 200 · iOS 5 trang; vẫn cache 7 ngày
- `web/src/db/schema.ts` + migration mới — bảng `review_seen` (backup trước, như Phase 8)
- `web/src/lib/complaint-rules.ts` (mới) — gốc từ, đồng nghĩa, từ khoá 8 loại, mẫu câu "ước gì"
- `web/src/lib/complaints.ts` — gộp cùng ý, gán loại, đếm theo app, mới nổi (90 ngày vs trước), `wishes()`
- `web/src/server/app.ts` — `/research/:id/complaints` trả `{ complaints, byApp, emerging, wishes }`, nhận lọc `store/app/type/from/to`
- `web/src/components/ComplaintsBlock.tsx` — bảng app × loại, chip mới nổi, danh sách ước gì, bộ lọc, câu trích có link
- `web/src/lib/evidence.ts` — thêm mục lời chê + ước gì
- `web/tests/complaints*.test.ts` + fixture — review thật đã ẩn tên

## Tasks

### Task 1: Lấy đủ review
- [ ] Mở rộng fetch: giữ review 1–3★ (3★ chỉ dùng cho "ước gì"), lưu `score`, `date`, `version`; Play 200, iOS 5 trang.
- [ ] Đổi khoá cache nếu cần (không làm mất cache cũ — đọc được cả bản cũ thiếu `version`). Khối lời chê cũ vẫn chỉ đọc 1–2★.
- [ ] Migration `review_seen`; mỗi lần lấy mạng thật → upsert theo hash, giữ `firstSeenAt` cũ.
- [ ] Test: parse review có / không `version`; cache còn hạn không gọi mạng; lấy 2 lần cùng review → 0 dòng mới.

### Task 2: Gộp cùng ý + loại
- [ ] `complaint-rules.ts`: gốc từ (crash / crashes / crashing), đồng nghĩa (`ads` = `advertisement` = `commercials`…),
      từ khoá từng loại, danh sách bỏ (tên app trong run, tên thương hiệu).
- [ ] `complaints.ts`: chuẩn hoá cụm → khoá gộp; gán loại; câu trích kiểm nguyên văn.
- [ ] Test: "crash" + "keeps crashing" thành 1 cụm; cụm < 3 review bị bỏ; câu trích không khớp bị bỏ.

### Task 3: App × loại + mới nổi + ước gì
- [ ] `byApp`: ô = số review + ≤ 3 câu trích (app, store, link review/app).
- [ ] `emerging`: review mới thấy lần này (`firstSeenAt`) vs lịch sử `review_seen`; cụm ≥ 3 review mới và tỉ lệ ≥ 2× → "mới nổi"
      (kèm phiên bản hay gặp, Play). App có 200 review phủ ≥ 180 ngày → so 90 ngày gần nhất vs 90 ngày trước theo `date`.
      Chưa có lần trước → `null` + "chưa có lần trước để so".
- [ ] `wishes()`: câu "wish / would be nice / please add / missing / need a way to" ở 1–3★ → gộp như cụm, đếm lần.
- [ ] Test từng hàm trên fixture.

### Task 4: UI + lọc + evidence
- [ ] `ComplaintsBlock`: bảng app × loại (ô bấm mở câu trích), chip "mới nổi", danh sách "ước gì", lọc store / app / loại / khoảng ngày.
- [ ] Bảng đọc được ở 1340px; ở 375px chuyển thành danh sách theo app (1 cột).
- [ ] `evidence.ts` thêm top cụm + ước gì; gói xuất Phase 15 đọc từ đây.

### Task 5: Chạy thật + soát
- [ ] 3 niche thật: đếm cụm trùng ý trước / sau, kiểm tay top 10 cụm, đếm dòng "ước gì" → ghi bảng dưới.
- [ ] Screenshot 1340 + 375, Read. `features.ts`, chip phase, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
- 2026-10-26: review plan — "mới nổi 90 ngày" không làm được từ 150 / 60 review mới nhất → đổi sang so lần lấy trước qua
  bảng `review_seen`; tăng Play 200, iOS 100; giữ 1–3★; sửa "RSS review iOS" thành proxy apps.apple.com.

## Kết quả chạy thật

| Niche | Cụm trùng trước | Cụm trùng sau | Top 10 có nghĩa | Ước gì |
|---|---|---|---|---|
| — | chưa đo | chưa đo | chưa đo | chưa đo |
