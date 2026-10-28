# ShotMatic Phase 51 — YouTube Search — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Task 0 làm trước.

**Goal:** gõ niche → biết người ta tìm gì trên YouTube, video nào hút view, kênh nhỏ nào thắng kênh to. Không AI. MCP bên thứ 3 tuỳ chọn.

**Spec:** [Phase 51 · YouTube Search](../../web/phase-51-youtube-search.md) · **Cần trước:** Phase 1 (cây keyword, `suggest.ts`),
Phase 3 (mẫu "chỉ Top 10 keyword"), Phase 14 (kết luận nguồn YouTube — nếu Phase 14 nói Bỏ thì dừng, hỏi anh).

## Mục tiêu · làm · không làm

- **Xong khi:** 3 niche thật có cây keyword YouTube + bảng top video + cột "video vượt kênh" · 1 lần chạy không bị chặn ·
  test xanh · screenshot đã Read · bảng thử MCP đủ (vidIQ + ≥ 1 MCP khác hoặc lý do bỏ); nếu dùng: 1 niche có cột vidIQ qua
  tuyến job, dưới trần credit.
- **Làm:** gợi ý YouTube (nhãn `YT`), top video mỗi keyword (Top 10 keyword), độ đông, độ mới, video vượt kênh, cột MCP tuỳ chọn, CSV.
- **Không làm:** AI đọc video (Phase 52) · tải video · ước doanh thu kênh · mua gói trả phí · tool tạo nội dung của MCP.

## Đo trước khi code (Task 0)

| Đo gì | Cách | Ghi vào |
|---|---|---|
| `youtubei.js` còn chạy: search, video info, channel | script nhỏ 1 keyword | bảng này, có ngày + phiên bản thư viện |
| Gợi ý YouTube (`suggestqueries.google.com/complete/search?ds=yt`) | 1 keyword | bảng này |
| Data API v3 (nếu có key) | 1 search = 100 đơn vị | bảng này |
| vidIQ MCP qua Claude Code (tuyến job) | 1 niche × Top 10 keyword, ghi credit + thời gian | bảng thử MCP trên trang phase |

## Global Constraints

- Nguồn mới đăng ký như các nguồn cũ trong `SOURCES` (`db/schema.ts`) + `SOURCE_TIMEOUT_MS`; job chạy độc lập, lỗi không kéo nguồn khác.
- Gọi ≥ 2 giây / request (limiter như `itunesLimit`), cache 24 giờ, chỉ Top 10 keyword. Bị chặn → `RATE_LIMITED`, dừng nguồn,
  không captcha, không proxy.
- Số view / sub kèm ngày lấy.
- Thang độ đông YouTube 0–1 = log tổng view top 20 + tỷ lệ kênh > 100k sub; công thức ghi 1 chỗ, hiện trên UI.
- Số MCP để cột riêng tiền tố `vidiq_`, ghi nguồn; **không** vào điểm cơ hội Phase 1. Trần credit / niche, mặc định tắt.
- Key vidIQ / Apify anh tự tạo, lưu `.env.local`, chỉ quyền đọc.

## File đụng tới

- `web/src/db/schema.ts` + migration mới — `SOURCES` thêm `youtube`; bảng `yt_videos` (videoId, keywordId, rank, title, channelId, views, publishedAt, durationSec, fetchedAt), `yt_channels` (channelId, subs, fetchedAt), `yt_mcp` (keywordId, provider, json, fetchedAt)
- `web/src/collectors/youtube.ts` (mới) — search + video + channel qua `youtubei.js`; Data API dự phòng khi có key
- `web/src/collectors/suggest.ts` — nguồn gợi ý `yt`
- `web/src/lib/youtube-metrics.ts` (mới) — độ đông, độ mới (% top đăng trong 12 tháng), vượt kênh (view ÷ sub)
- `web/src/lib/youtube-mcp-job.ts` (mới) — file job Top 10 keyword cho Claude đã nối vidIQ + nhập kết quả
- `web/src/lib/run-research.ts`, `run-view.ts` — chạy nguồn mới, view có khối YouTube
- `web/src/components/YoutubeBlock.tsx` (mới), `KeywordTable.tsx`, `ExploreShared.tsx` — bảng top video, cột vượt kênh, nhãn `YT`, cột `vidiq_*`
- `web/src/lib/explore.ts`, `exploreCsv` — gợi ý YT trong cây + CSV
- `web/tests/youtube-*.test.ts` + fixture JSON

## Tasks

### Task 0: Đo endpoint
- [ ] Bảng đo ở trên. `youtubei.js` gãy và không có key → hỏi anh (yt-dlp cần Python) trước khi code.

### Task 1: Gợi ý YouTube trong cây
- [ ] Nguồn `yt` trong suggest + nhãn `YT`. Test parse.

### Task 2: Collector top video + kênh
- [ ] `youtube.ts` + migration; Top 10 keyword × top 20 video; cache 24 giờ; limiter. Test với fixture (không gọi mạng).

### Task 3: Chỉ số
- [ ] `youtube-metrics.ts` + test (kênh nhỏ video to đứng đầu "vượt kênh").

### Task 4: UI + CSV
- [ ] `YoutubeBlock` trên trang Research + Explore; CSV thêm cột. `features.ts` YouTube → done.

### Task 5: MCP tuỳ chọn (tuyến job)
- [ ] Job `.json` + nhập; cột `vidiq_*`; trần credit. Bảng thử MCP điền đủ.

### Task 6: Chạy thật + soát
- [ ] 3 niche thật, 1 lượt không bị chặn. Screenshot 1340 + 375, Read. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
