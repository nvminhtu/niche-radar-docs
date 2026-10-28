# ShotMatic Phase 38 — Doanh thu thật: TrustMRR + nguồn khác + AI — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Task 0 làm trước hết.

**Goal:** trả lời "**có ai đang thu tiền thật không, bao nhiêu**" — số verified tách bạch với số ước.

**Spec:** [Phase 38 · Doanh thu thật](../../web/phase-38-revenue.md) · **Cần trước:** Phase 6 (job TrustMRR, `cleanTrust`),
Phase 9 (nhãn mô hình tiền `lib/money.ts`), Phase 20 (yếu tố Tiền + độ tin + back-test để chạy lại),
Phase 11 (mẫu nhập file tuyến C: `lib/reddit-import.ts`).

## Mục tiêu · làm · không làm

- **Xong khi:** bảng Bước 0 đủ nguồn ứng viên, quyết dùng / bỏ + lý do · 10 niche thật: đếm đối thủ có verified, kiểm tay
  10 dòng khớp tên (≥ 9 đúng) · bảng "Ai đang thu tiền" tách verified / ước, có trong evidence pack.
- **Xong khi (thêm):** chạy được không cần Claude in Chrome — tuyến C nhập ≥ 10 trang đã lưu thật, đọc đúng số · back-test
  Phase 20 chạy lại, bảng trước / sau.
- **Làm:** tuyến C nhập trang đã lưu, khớp tên chắc hơn (luật + AI xác nhận), dòng verified đủ trường, ước theo bậc, bảng "Ai đang thu tiền", nối điểm v2, làm mới, chạy lại back-test.
- **Không làm:** mua dữ liệu trả phí · mô hình ước doanh thu phức tạp · dự báo doanh thu app mình.

## Global Constraints

- Không quét trang cấm quét (TrustMRR): tool **không tự gọi** trustmrr.com. Đường chính là **tuyến C** — anh tự mở link
  tool đưa, Cmd + S, nhập file (như Reddit Gap Phase 11). Job Claude in Chrome là tuyến phụ: Chrome không nối được 5 lần
  tới 2026-10-25, nên không Task nào được chỉ chạy qua job. Không đăng nhập thay anh.
- **Verified** = có số nguyên văn trên trang + link + ngày sync + ngày mình lấy. Thiếu một → không phải verified.
- **Ước** chỉ theo bậc `$0 · <$1k · $1–10k · >$10k / tháng` từ giá × tín hiệu (Top Grossing, số rating); luôn nhãn "ước", không trộn cột.
- Lượt tải không thay cho doanh thu.
- Collector cũ `lib/trustmrr.ts` giữ, chỉ bật khi có API key chính thức — không viết lại.
- Số verified > 30 ngày → nhãn "cũ" + nút tạo job tra lại.

## File đụng tới

- `docs/web/phase-38-revenue.md` — điền bảng Bước 0
- `web/src/lib/revenue/import.ts` (mới) — đọc file `.html` / `.json` đã lưu (TrustMRR, trang /open) → dòng verified nguyên văn + link + ngày sync; chống nhân đôi theo (nguồn, link); mẫu theo `reddit-import.ts`
- `web/src/lib/revenue/links.ts` (mới) — danh sách link cần mở cho 1 niche (TrustMRR theo tên đối thủ, /open từ `developerWebsite`, câu tìm bài công khai)
- `web/src/db/schema.ts` + migration mới — `revenue_rows` (appId?, source, url, mrr, revenue30d, provider, syncedAt, fetchedAt, match, matchReason)
- `web/src/lib/revenue/match.ts` (mới) — điểm khớp luật (tên, dev, domain web) → `chắc · gần đúng · không khớp`; AI xác nhận (tuỳ chọn) kèm lý do
- `web/src/lib/revenue/estimate.ts` (mới) — bậc ước từ giá + Top Grossing + số rating, kèm lý do
- `web/src/lib/revenue/table.ts` (mới) — gộp verified (TrustMRR job, trang /open, bài công khai) + ước → bảng "Ai đang thu tiền"
- `web/src/lib/ai/tasks.ts` — task `revenue` (job + tuyến A) đọc trang /open, bài chia sẻ: trả số nguyên văn + link, `cleanRevenue` kiểm số có trong câu trích
- `web/src/collectors/top-grossing.ts` (mới) — RSS Top Grossing App Store theo thể loại (công khai) — chỉ thứ hạng, cache 1 ngày
- `web/src/lib/score-v2.ts` — yếu tố Tiền: verified → "đo", ước → "proxy"
- `web/src/components/RevenueBlock.tsx` (mới) — bảng + dòng tóm tắt "3 app verified > $1k MRR", nhãn cũ, nút tra lại
- `web/src/lib/evidence.ts` — thêm bảng
- `web/tests/revenue-*.test.ts`

## Tasks

### Task 0: Chọn nguồn (làm trước)
- [ ] TrustMRR qua tuyến C: anh lưu 3–5 trang (trang startup, tìm kiếm, top category) → xem đọc được trường nào; job Chrome chỉ thử nếu nối được.
- [ ] Trang /open /stats của đối thủ: tìm link từ web đối thủ (listing cache có `developerWebsite`), đọc được không.
- [ ] Bài công khai (Indie Hackers, X founder): tìm theo tên app — chỉ số có ngày + link.
- [ ] Top Grossing RSS: có cho thể loại cần không.
- [ ] Điền bảng Bước 0 (có số công khai · điều khoản · cần đăng nhập · độ phủ mobile · dùng / bỏ + lý do).

### Task 0b: Tuyến C — nhập trang đã lưu
- [ ] `links.ts` + khối "Link cần mở" (mỗi dòng: Mở · tên file gợi ý), `import.ts` + kéo thả nhiều file, báo từng file đọc được gì.
- [ ] Fixture: trang TrustMRR + trang /open đã lưu (ẩn tên) → đúng MRR, ngày sync, link; nhập lại → 0 dòng mới; file lạ → báo "không đọc được", không đoán.

### Task 1: Khớp tên
- [ ] `match.ts` luật + test (cùng dev, domain trùng, tên thương hiệu trước ":"). AI xác nhận khi có key, lưu lý do.

### Task 2: Verified đủ trường + ước theo bậc
- [ ] Mở rộng `TrustRow` / dòng verified: MRR · 30 ngày · provider · ngày sync · link · ngày lấy · nguồn.
- [ ] `top-grossing.ts` + `estimate.ts`; test bậc ước với dữ liệu giả.

### Task 3: Bảng + điểm v2 + làm mới
- [ ] `table.ts` + `RevenueBlock`; verified và ước ở 2 cột riêng.
- [ ] Yếu tố Tiền dùng verified trước. Test độ tin đổi theo nguồn.
- [ ] Nhãn "cũ" > 30 ngày + nút mở lại link để lưu bản mới (hoặc tạo job).
- [ ] Chạy lại back-test Phase 20 (Tiền giờ là "đo" ở niche có verified) → bảng trước / sau ở trang Phase 13.

### Task 4: Chạy thật + soát
- [ ] 10 niche thật: đếm đối thủ có verified, kiểm tay 10 dòng khớp → bảng dưới.
- [ ] Evidence pack có bảng. Screenshot 1340 + 375, Read. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan. Đã có 1 khớp gần đúng (habit tracker) qua job TrustMRR ở Phase 6.
- 2026-10-26: review plan — Claude in Chrome không nối được nên thêm tuyến C (nhập trang đã lưu) làm đường chính, job thành
  tuyến phụ; thêm bảng `revenue_rows`; thêm bước chạy lại back-test Phase 13.

## Kết quả chạy thật

| Niche | Đối thủ | Có verified | Khớp đúng / kiểm |
|---|---|---|---|
| — | chưa đo | chưa đo | chưa đo |
