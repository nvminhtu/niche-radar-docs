# Niche Radar Phase 12 — Đối thủ bị chê gì — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** từ "vài cụm lặp lại" thành **bản đồ lời chê**: app nào bị chê gì, loại gì, mới nổi hay cũ, người dùng ước gì —
mọi dòng có câu nguyên văn. Không AI.

**Spec:** [Phase 12 · Đối thủ bị chê gì](../../web/phase-12-competitor-complaints.md) · **Cần trước:** Phase 1–2 (review),
Phase 9 (bảng mức nặng `severityOf` trong `lib/ai/themes.ts`).

## Mục tiêu · làm · không làm

- **Xong khi:** 3 niche thật, top 10 cụm mỗi niche ≥ 8/10 có nghĩa · số cụm trùng ý giảm rõ (đếm trước / sau, ghi số) ·
  bảng app × loại đọc được ở 1340px, ô bấm ra câu trích đúng app · "ước gì" ≥ 5 dòng ở ≥ 2/3 niche · test xanh · screenshot đã Read.
- **Làm:** lấy đủ review (có 3★), gộp cùng ý, loại lời chê, bảng app × loại, mới nổi, ước gì, lọc, đưa vào evidence pack.
- **Không làm:** AI gom chủ đề (Phase 17) · so 2–5 đối thủ (Phase 37) · review ngoài 2 store.

## Đo trước khi code

| Đo gì | Cách | Ghi vào |
|---|---|---|
| Số review lấy được / app, có `version` không | gọi `fetchPlayReviews` + RSS review iOS cho 1 app mỗi store | bảng này |
| Số cụm trùng ý hiện tại | chạy `topComplaints` trên 3 niche (budget tracker, habit tracker, pomodoro timer), đếm tay cụm trùng | "Kết quả chạy thật" — cột *trước* |

## Global Constraints

- Mỗi cụm ≥ 3 review **khác nhau**; câu trích phải **khớp nguyên văn** review gốc (kiểm bằng `includes` như Phase 6), không dịch, không viết lại.
- Luật gộp (gốc từ + đồng nghĩa) và luật loại nằm trong **1 file** `web/src/lib/complaint-rules.ts`; thêm từ không sửa code.
- 8 loại: Lỗi / crash · Mất dữ liệu · Ép trả phí / giá · Quảng cáo · Thiếu tính năng · Khó dùng · Đồng bộ / tài khoản · Khác.
  Mức nặng dùng chung `severityOf` của Phase 9 (không tạo bảng thứ hai).
- Top 5 app mỗi store, ≤ 200 review / app, cache 7 ngày (`review_cache`, `REVIEW_CACHE_MS`). Tên app + thương hiệu bị bỏ khỏi cụm.
- API cũ `GET /api/research/:id/complaints` giữ trường `complaints` để khối cũ không vỡ; thêm trường mới bên cạnh.

## File đụng tới

| File | Việc |
|---|---|
| `web/src/collectors/play-reviews.ts` + review iOS | thêm 3★, `version`, ngày; vẫn cache 7 ngày |
| `web/src/lib/complaint-rules.ts` (mới) | gốc từ, đồng nghĩa, từ khoá 8 loại, mẫu câu "ước gì" |
| `web/src/lib/complaints.ts` | gộp cùng ý, gán loại, đếm theo app, mới nổi (90 ngày vs trước), `wishes()` |
| `web/src/server/app.ts` | `/research/:id/complaints` trả `{ complaints, byApp, emerging, wishes }`, nhận lọc `store/app/type/from/to` |
| `web/src/components/ComplaintsBlock.tsx` | bảng app × loại, chip mới nổi, danh sách ước gì, bộ lọc, câu trích có link |
| `web/src/lib/evidence.ts` | thêm mục lời chê + ước gì |
| `web/tests/complaints*.test.ts` + fixture | review thật đã ẩn tên |

## Tasks

### Task 1: Lấy đủ review
- [ ] Mở rộng fetch: giữ review 1–3★ (3★ chỉ dùng cho "ước gì"), lưu `score`, `date`, `version`.
- [ ] Đổi khoá cache nếu cần (không làm mất cache cũ — đọc được cả bản cũ thiếu `version`).
- [ ] Test: parse review có / không `version`; cache còn hạn không gọi mạng.

### Task 2: Gộp cùng ý + loại
- [ ] `complaint-rules.ts`: gốc từ (crash / crashes / crashing), đồng nghĩa (`ads` = `advertisement` = `commercials`…),
      từ khoá từng loại, danh sách bỏ (tên app trong run, tên thương hiệu).
- [ ] `complaints.ts`: chuẩn hoá cụm → khoá gộp; gán loại; câu trích kiểm nguyên văn.
- [ ] Test: "crash" + "keeps crashing" thành 1 cụm; cụm < 3 review bị bỏ; câu trích không khớp bị bỏ.

### Task 3: App × loại + mới nổi + ước gì
- [ ] `byApp`: ô = số review + ≤ 3 câu trích (app, store, link review/app).
- [ ] `emerging`: so 90 ngày gần nhất với trước đó, cụm tăng ≥ 2× và ≥ 3 review mới → "mới nổi" (kèm phiên bản hay gặp).
- [ ] `wishes()`: câu "wish / would be nice / please add / missing / need a way to" ở 1–3★ → gộp như cụm, đếm lần.
- [ ] Test từng hàm trên fixture.

### Task 4: UI + lọc + evidence
- [ ] `ComplaintsBlock`: bảng app × loại (ô bấm mở câu trích), chip "mới nổi", danh sách "ước gì", lọc store / app / loại / khoảng ngày.
- [ ] Bảng đọc được ở 1340px; ở 375px chuyển thành danh sách theo app (1 cột).
- [ ] `evidence.ts` thêm top cụm + ước gì; gói xuất Phase 16 đọc từ đây.

### Task 5: Chạy thật + soát
- [ ] 3 niche thật: đếm cụm trùng ý trước / sau, kiểm tay top 10 cụm, đếm dòng "ước gì" → ghi bảng dưới.
- [ ] Screenshot 1340 + 375, Read. `features.ts`, chip phase, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.

## Kết quả chạy thật

| Niche | Cụm trùng trước | Cụm trùng sau | Top 10 có nghĩa | Ước gì |
|---|---|---|---|---|
| — | chưa đo | chưa đo | chưa đo | chưa đo |
