# Niche Radar Phase 33 — Amazon Search — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Task 0 làm trước. Gặp captcha → dừng, không vượt.

**Goal:** gõ niche → biết người ta tìm gì trên Amazon, sản phẩm nào bán chạy, đông tới đâu, giá bao nhiêu. Không AI.

**Spec:** [Phase 33 · Amazon Search](../../web/phase-33-amazon-search.md) · **Cần trước:** Phase 11 (kết luận nguồn Amazon —
nếu Bỏ thì dừng, hỏi anh), Phase 31 (mẫu thêm nguồn mới).

## Mục tiêu · làm · không làm

- **Xong khi:** 3 niche thật có cây keyword Amazon + bảng top sản phẩm + khoảng giá · chạy 3 niche liền không chạm captcha (hoặc
  chạm thì UI báo đúng, nguồn khác vẫn chạy) · test xanh · screenshot đã Read.
- **Làm:** gợi ý Amazon (nhãn `AMZ`), top 20 sản phẩm (giá, sao, số review, "bought in past month"), độ đông (log tổng review), BSR top 5,
  khoảng giá, lính mới thắng.
- **Không làm:** AI đọc review (Phase 34) · ước doanh số từ BSR · dịch vụ trả phí (Jungle Scout, Helium 10, Keepa).

## Đo trước khi code (Task 0)

| Đo gì | Cách | Ghi vào |
|---|---|---|
| Endpoint gợi ý Amazon (`completion.amazon.com/api/2017/suggestions`) | 1 keyword, marketplace US | bảng này + ngày |
| Trang tìm `amazon.com/s?k=` với `fetch` + `cheerio` | 1 keyword: có giá / sao / review / badge không, hay captcha ngay | bảng này |
| Trang sản phẩm: BSR, ngày lên kệ ("Date First Available") | 3 sản phẩm | bảng này |
| Điều khoản Conditions of Use về robot | đọc, trích link | bảng này — cấm rõ ràng thì chỉ giữ gợi ý + hỏi anh |

## Global Constraints

- ≥ 5 giây / request, cache 7 ngày, chỉ Top 5 keyword × Top 20 sản phẩm; BSR chỉ top 5 sản phẩm / keyword.
- Gặp captcha / trang chặn (dấu hiệu: form captcha, status 503) → `RATE_LIMITED` cho nguồn Amazon cả lượt; không thử lại trong lượt đó.
- Không đăng nhập, không trang cần đăng nhập, không proxy.
- Parse HTML tách riêng 1 file có fixture HTML thật đã lưu → Amazon đổi giao diện thì sửa 1 chỗ, test báo ngay.
- BSR ghi nguyên số + danh mục, **không** quy ra tiền.

## File đụng tới

- `web/src/db/schema.ts` + migration mới — `SOURCES` thêm `amazon`; `amz_products` (asin, keywordId, rank, title, price, currency, rating, reviews, boughtBadge, bsr, bsrCategory, firstAvailable, fetchedAt)
- `web/src/collectors/amazon.ts` (mới) — gợi ý + tìm + trang sản phẩm, limiter 5 giây
- `web/src/collectors/amazon-parse.ts` (mới) — parse HTML (cheerio)
- `web/src/lib/amazon-metrics.ts` (mới) — độ đông log, khoảng giá (thấp / trung vị / cao), lính mới (< 12 tháng trong top)
- `run-research.ts`, `run-view.ts`, `explore.ts` — nguồn mới, nhãn `AMZ`
- `web/src/components/AmazonBlock.tsx` (mới) — bảng top sản phẩm, khoảng giá, BSR, lính mới
- `web/tests/amazon-*.test.ts` + `fixtures/amazon/*.html`

## Tasks

### Task 0: Đo + điều khoản
- [ ] Bảng đo. Trang tìm captcha ngay từ lần đầu → chỉ làm gợi ý (Task 1), ghi lý do, hỏi anh trước khi đi tiếp.

### Task 1: Gợi ý Amazon
- [ ] Nguồn `amz` trong suggest + nhãn trong cây. Test.

### Task 2: Tìm + sản phẩm
- [ ] `amazon-parse.ts` + fixture; `amazon.ts` + migration; dừng khi captcha. Test: fixture captcha → `RATE_LIMITED`.

### Task 3: Chỉ số + UI
- [ ] `amazon-metrics.ts` + test; `AmazonBlock`; `features.ts` Amazon → done.

### Task 4: Chạy thật + soát
- [ ] 3 niche liền (số request + có chạm captcha không → ghi). Screenshot 1340 + 375, Read. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
