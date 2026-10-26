# Niche Radar Phase 12 — Q&A Gap (Stack Exchange + Hacker News) — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự. Mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [x]`). Không tạo key StackApps thay anh, không đăng gì lên Stack Exchange / HN.

**Goal:** thêm hai nguồn hỏi đáp gọi bằng API miễn phí (Stack Exchange, Hacker News) vào bảng gap của Phase 11, để biết
chủ đề nào **hỏi nhiều, nhiều người xem, chưa ai giải**, kèm link câu gốc.

**Spec:** [Phase 12 · Q&A Gap](../../web/phase-12-qa-gap.md) · **Cần trước:** Phase 11 (luật phân loại, điểm gap,
đếm app Mac, trang `/reddit`), Phase 8 (backup trước migrate) · **Nguồn quyết định:** [Bản đồ nguồn gap](../../web/gap-sources-map.md).

## Mục tiêu · làm · không làm

- **Xong khi:** chạy thật 3 site Stack Exchange + HN (ghi số câu, số lệnh) · kiểm tay 30 câu: chuyên mục ≥ 80 %, chủ đề ≥ 70 %
  · top 10 gap tab Gộp mỗi dòng ≥ 3 link mở được · `.md` chọn được 1 bài `/fix` hoặc 1 ý tưởng app Mac · test fixture thật.
- **Làm:** bảng `qa_threads`, 2 collector (SE, HN), dùng lại phân loại Phase 11, điểm gap có lượt xem + cờ đã giải, tab
  nguồn + tab Gộp trên trang Gap hỏi đáp, xuất `.md` có ghi công CC BY-SA.
- **Không làm:** đăng bài · lưu tên / id người dùng · cây comment HN · site SE ngoài 3 site · gom chủ đề bằng AI / BERTopic ·
  tạo key thay anh.

## Đo trước (2026-10-26, từ máy làm việc)

- SE `search/advanced` không key: chạy, `quota_max` 300 / ngày. `filter=withbody` có thân bài.
- SE `tags/info`: `apple/software-recommendation` 1.735 câu · `superuser/software-rec` 1.118 câu · `softwarerecs/macos` 208 câu.
  (`superuser/software-recommendation` = 0, đừng dùng.)
- HN Algolia `search?tags=ask_hn&query="is there an app"`: 92 bài, có `points`, `num_comments`, `created_at`. Không key.

## Global Constraints

- **Không lưu người dùng:** bỏ `owner`, `author`, `user_id` ngay trong collector, trước khi ghi DB.
- **Lịch sự:** ≥ 1 giây giữa hai lệnh; SE trả `backoff` thì chờ đúng số giây đó; cache 7 ngày theo `(source, query)` trong
  `qa_fetches`; hiện `quota_remaining` SE trên trang.
- **Key tuỳ chọn:** `STACKEXCHANGE_KEY` đọc từ Cài đặt / `.env.local` (anh tự tạo). Không có thì chạy không key.
- **Dùng lại, không chép:** `categoryOf`, `topicsOf`, `saysNoNative`, `gapScore`, `countMacApps` từ `reddit-gap.ts`; luật trong
  `reddit-rules.ts`. Hàm nào đang nhận kiểu `RedditThread` thì đổi sang nhận `Pick<…, 'title' | 'body' | 'flair'>` (đã gần như vậy).
- Migration số kế tiếp (hiện tới `0014`) qua `npm run db:generate`; backup DB trước migrate như Phase 8.
- Công thức điểm hiện trên UI, không có điểm bí ẩn. Trang 1 cột, đọc rõ ở 1340px.
- Test không gọi mạng: collector nhận `fetch` tiêm vào (như `FetchMacApps`), test dùng fixture JSON thật đã bỏ tên người.

## File đụng tới

| File | Việc |
|---|---|
| `web/src/db/schema.ts` + migration mới | `qa_threads`, `qa_fetches` |
| `web/src/lib/qa-sources.ts` | danh sách site + tag + câu search (dùng `SEARCH_QUERIES` của Phase 11) |
| `web/src/lib/qa-stackexchange.ts` | gọi SE, chuẩn hoá, lấy câu trả lời top, xử lý `backoff` / quota |
| `web/src/lib/qa-hn.ts` | gọi Algolia, chuẩn hoá |
| `web/src/lib/qa-gap.ts` | nhập vào DB, gap board theo nguồn, board Gộp (Reddit + QA), `.md` |
| `web/src/lib/reddit-rules.ts` | thêm chủ đề Windows / đa nền tảng, dev tool |
| `web/src/server/app.ts` | `GET /api/qa`, `POST /api/qa/fetch`, `GET /api/qa/gap`, `GET /api/qa/threads`, `GET /api/qa/export.md` |
| `web/src/client/RedditGapPage.tsx` (+ component tab nhỏ nếu file quá dài) | tab Reddit · Stack Exchange · HN · Gộp; tên trang "Gap hỏi đáp" |
| `web/src/lib/features.ts`, `web/src/locales/*` | thêm mục Phase 12; chữ mới qua `useT()` |
| `web/tests/qa-*.test.ts` + `web/tests/fixtures/qa/` | fixture SE + Algolia thật (bỏ tên) |

## Tasks

### Task 1: Bảng + nguồn
- [x] Schema `qa_threads`: `source` (`se:apple` · `se:superuser` · `se:softwarerecs` · `hn`), `id`, `title`, `body` (≤ 500),
      `tags` json, `score`, `views` (null cho HN), `answers` (SE: số trả lời · HN: số comment), `accepted` (bool, null cho HN),
      `topAnswers` json (≤ 3 × 300 ký tự, [] cho HN), `createdAt`, `url`, `fetchedAt`. Khoá chính `(source, id)`.
- [x] `qa_fetches`: `source`, `query`, `fetchedAt`, `count`, `quotaRemaining`.
- [x] `qa-sources.ts`: 3 site SE + tag đã đo ở trên + `SEARCH_QUERIES`; HN dùng `SEARCH_QUERIES`, cửa sổ 3 năm.
- [x] Test: migrate trên DB rỗng và DB đang có dữ liệu Phase 11 (backup được tạo).

### Task 2: Collector Stack Exchange
- [x] `fetchSe(site, { tag? , q? }, fetcher)` → `search/advanced?order=desc&sort=votes&pagesize=100&filter=withbody`.
- [x] Chuẩn hoá: bỏ HTML trong `body` (dùng `decodeEntities` của Phase 11 + bỏ thẻ), cắt 500 ký tự, bỏ `owner`.
- [x] `fetchTopAnswers(site, ids, fetcher)` → `/questions/{ids}/answers?sort=votes&filter=withbody`, 100 id / lệnh,
      giữ ≤ 3 câu điểm cao nhất mỗi câu hỏi.
- [x] Tôn trọng `backoff`, ≥ 1 giây / lệnh, trả `quotaRemaining`; hết quota → dừng, báo rõ, giữ phần đã lấy.
- [x] Test với fixture thật: có body HTML, có `backoff`, hết quota, câu trùng giữa tag và search.

### Task 3: Collector Hacker News
- [x] `fetchHn(query, sinceUnix, fetcher)` → Algolia `search?tags=ask_hn&hitsPerPage=100&numericFilters=created_at_i>…`.
- [x] Chuẩn hoá: `title`, `story_text` (bỏ HTML, ≤ 500), `points` → score, `num_comments` → answers, `url` = trang item HN.
      Bỏ `author`.
- [x] Test với fixture thật: bài không có `story_text`, trùng id giữa các câu search.

### Task 4: Phân loại + gap
- [x] `reddit-rules.ts`: thêm chủ đề Windows / đa nền tảng, dev tool (CLI, git, editor, API), giữ ~40 chủ đề cũ.
- [x] Tag `software-recommendation` / `software-rec` → chuyên mục `app-request`, trừ khi tiêu đề khớp mẫu chuyên mục khác.
- [x] `qa-gap.ts`: `qaBoard(db, { source?, sinceYears? })` cùng kiểu `GapRow` + cột `medianViews`, `unansweredShare`.
      "Đã giải" của SE = `accepted`; HN = "—" (không tính, hệ số = 1).
- [x] Điểm = số câu × log2(2 + trung vị views / 1.000 + trung vị điểm) × (1 − tỷ lệ đã giải) × (1 + tỷ lệ "không có cách
      gốc" trong câu trả lời top) × 1 / (1 + số app Mac / 10). Xuất chuỗi công thức như `GAP_FORMULA`.
- [x] `mergedBoard(db)`: cộng Reddit + QA theo chủ đề × chuyên mục, thêm `sources: string[]`.
- [x] Test: chủ đề nhiều xem, ít accepted, ít app đứng đầu; HN không làm sai hệ số "đã giải".

### Task 5: API + trang
- [x] API: `GET /api/qa` (nguồn, số câu, lần lấy cuối, quota) · `POST /api/qa/fetch` (`{ source }`, chạy tuần tự,
      trả tiến độ) · `GET /api/qa/gap?source=` · `GET /api/qa/threads?source=&topic=&category=` · `GET /api/qa/export.md`.
- [x] Trang: tên "Gap hỏi đáp", giữ `/reddit`, tab Reddit · Stack Exchange · Hacker News · Gộp. Tab SE / HN: nút
      **Lấy dữ liệu** + chọn site, tiến độ, quota còn lại, rồi bảng gap. Bấm dòng ra câu gốc (link + nguồn).
- [x] `.md`: top 20 gap, 3 link mỗi dòng, dòng ghi công "Nội dung Stack Exchange theo CC BY-SA 4.0, link về câu gốc".
- [x] `features.ts`: thêm "Gap hỏi đáp · Stack Exchange + HN" (Phase 12). Chữ mới qua `useT()` (vi gốc, en, es).

### Task 6: Chạy thật + soát
- [x] Lấy cả 3 site SE + HN. Ghi số câu từng nguồn + số lệnh SE đã dùng vào "Kết quả chạy thật".
- [x] Kiểm tay 30 câu ngẫu nhiên, ghi tỷ lệ đúng. Mở ≥ 3 link của top 10 gap tab Gộp.
- [x] Xuất `.md`, chọn 1 bài `/fix` hoặc 1 ý tưởng app Mac, ghi vào đây.
- [x] Screenshot trang ở 1340 và 375, Read ảnh. Cập nhật chip phase, ROADMAP, CHANGELOG (nhãn Web), `docs/cach-dung.md`.

## Tiến độ

- 2026-10-26: anh duyệt (gộp A + C từ Phase 14), viết plan. Đo trước: SE + HN gọi được không key.

## Kết quả chạy thật

Chạy 2026-10-26 trên bản sao DB (`NICHE_DB`), qua giao diện (nút **Lấy dữ liệu**), không key:

- **Số câu:** Ask Different 850 · Super User 770 · Software Recs 105 · Ask HN 539 (2023-10 → 2026-10) = **2.264**.
  358 câu (16 %) chưa xếp được chủ đề.
- **Số lệnh:** Stack Exchange 60 (apple 25 · superuser 24 · softwarerecs 11) — nhiều hơn ước 40 vì lấy câu trả lời top
  100 id / lệnh × tối đa 2 trang. Quota còn 231 / 300 (đã tốn 9 lệnh đo trước). ⇒ một ngày chạy đủ 3 site được ~4 lần.
  HN 8 lệnh.
- **Kiểm tay 30 câu ngẫu nhiên.** Lần 1: chuyên mục 22/30 (73 %, trượt), chủ đề 21/30. Sửa 3 luật: cả site Software
  Recs = Xin app · "how to fix" = Lỗi · "charge for" không phải Pin. Lần 2 (mẫu mới): **chuyên mục 28/30 (93 %)**,
  **chủ đề 22/30 (73 %)** — đạt. Chủ đề sai chủ yếu là thứ từ điển Mac chưa có: mạng / IP / hosts, tmux, sudo, ổ cứng.
- **"Không có cách":** câu trả lời top lưu được cho 653 / 787 câu Ask Different có trả lời; thêm mẫu câu kiểu Stack Exchange
  ("the answer is no", "there is no app", "no such feature") nhưng tỷ lệ vẫn ≤ 4 % — Stack Exchange hầu như luôn có người
  chỉ cách. Cột này yếu ở nguồn này, giữ để đúng công thức.
- **Câu cũ:** sắp theo votes nên Stack Exchange chủ yếu 2010–2016, cột "12 tháng" gần như 0. Dùng để biết **nhu cầu bền**,
  không phải nhu cầu mới; nhu cầu mới xem tab HN / Reddit.
- **Link:** top 10 dòng tab Gộp, mở 3 link bằng trình duyệt — đều ra đúng câu. `curl` bị Cloudflare trả 403 (chặn bot web,
  API không bị).
- **Ý tưởng chọn từ `.md` (output ra đô):** dòng *Finder / file · Tìm thay thế* — "file copy utility for OS X similar to
  TeraCopy" (copy có hàng đợi, tạm dừng / chạy tiếp, kiểm checksum). Đo Mac App Store 2026-10-26: TeraCopy (Free, 0 đánh
  giá), CopyQueue $19.99 (0 đánh giá), RapidCopy $19.99 (0 đánh giá) — có người làm nhưng chưa ai có đánh giá ⇒ ứng viên
  cho `/best-app` / `/app-demand`, chưa kiểm nhu cầu tiền.
- **Chưa làm (ghi Appendix):** đưa Q&A vào hộp Xuất của Phase 15 (CSV / JSON / gói AI) — giờ chỉ có **Tải .md**; ô nhập
  key StackApps ở Cài đặt (giờ đọc `STACKEXCHANGE_KEY` từ môi trường); thêm chủ đề mạng / IP, terminal multiplexer.
