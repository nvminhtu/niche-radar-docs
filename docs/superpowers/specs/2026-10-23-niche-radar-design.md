# niche-radar — Thiết kế v1

> Ngày: 2026-10-23 · Trạng thái: đã duyệt thiết kế, chờ review spec

## Mục tiêu

Web tool cá nhân, chạy local. Gõ **một niche** → tool tự tra Google Play, App Store,
Google Trends và Reddit → trả lời "**theo từng từ khoá, đã có ai làm chưa, làm tới đâu**"
→ lưu vào database → hiện dữ liệu thô dạng trực quan kèm số liệu thống kê.

v1 **không chấm điểm** niche. Người dùng tự kết luận từ dữ liệu.

## Phạm vi

**Trong v1**

- Nguồn: Google Play, App Store, Google Trends, Reddit.
- Mở rộng keyword: seed + tối đa 5 gợi ý từ Play Store autocomplete.
- Lưu mọi kết quả vào SQLite, xem lại được lịch sử các lần tra.
- Dashboard: số liệu tổng, bảng Keyword × Store, bảng đối thủ, biểu đồ Trends và Reddit.

**Ngoài v1**

Chấm điểm cơ hội · Chrome Web Store · so sánh nhiều niche cạnh nhau · đọc comment Reddit ·
tự động tra định kỳ · biểu đồ lịch sử snapshot · login · deploy.

## Stack

| Phần | Chọn |
|---|---|
| App | Next.js 15 App Router, TypeScript |
| DB | SQLite file `data/niche.db` (gitignore), `better-sqlite3` + Drizzle ORM |
| Biểu đồ | Recharts |
| Style | Tailwind CSS |
| Test | Vitest |
| Cổng dev | `localhost:3200` (`npm run dev`) |

Chạy local trên Mac: IP nhà ít bị Google Trends chặn hơn IP datacenter, không tốn tiền.

## Luồng một lần tra

```
Trang chủ: gõ seed "habit tracker" + chọn nước (mặc định US)
  → POST /api/research {seed, country}
      → tạo run, trả {runId} ngay (không chờ collector)
      → chạy nền trong process:
          1. mở rộng keyword: seed + ≤ 5 gợi ý Play autocomplete → bảng keywords
          2. Promise.allSettled([playstore, appstore, trends, reddit])
             mỗi collector cập nhật source_jobs của mình: pending → running → done | error
  → chuyển sang /r/[runId]
      → GET /api/research/[runId] mỗi 2 giây, dừng khi mọi source_jobs là done hoặc error
      → khối nào có dữ liệu thì hiện ngay
```

Bước 1 lỗi (autocomplete không trả về) thì vẫn chạy tiếp, chỉ với keyword seed.

**Cache:** khi tạo run, nếu đã có run cùng `seed` + `country` trong 24 giờ mà nguồn đó
`done` thì nguồn đó **chép dữ liệu** từ run cũ thay vì gọi mạng. Run mới vẫn là một run
riêng. Body có `force: true` (nút "Tra lại") thì bỏ qua cache.

**Thử lại một nguồn:** `POST /api/research/[runId]/retry {source}` xoá dữ liệu của nguồn
đó trong run, đặt lại `pending`, chạy lại collector đó.

## Collector

Mỗi nguồn là một module `src/collectors/<source>.ts`, cùng interface:

```ts
type CollectContext = { runId: number; keywords: { id: number; term: string }[]; country: string };
type Collector = (ctx: CollectContext) => Promise<void>; // tự ghi DB; ném lỗi khi thất bại
```

Phần gọi mạng và phần chuẩn hoá dữ liệu tách hàm: `fetchX()` trả JSON thô,
`normalizeX(raw)` là hàm thuần trả về các dòng để ghi DB. Test nhắm vào `normalizeX`.

| Nguồn | Thư viện / endpoint | Mỗi keyword lấy | Nhịp gọi |
|---|---|---|---|
| `playstore` | `google-play-scraper` (`search`, `suggest`) | top 30 app: id, tên, dev, icon, url, genre, giá, số cài tối thiểu (`minInstalls`), rating, số rating, ngày update, ngày ra mắt | ≤ 1 req/s |
| `appstore` | iTunes Search API `https://itunes.apple.com/search?term=&country=&entity=software&limit=30` | top 30 app: id, tên, dev, icon, url, genre, giá, rating, số rating, ngày update, ngày ra mắt. **Không có số cài.** | ≤ 20 req/phút |
| `trends` | `google-trends-api` (`interestOverTime`, `relatedQueries`) | chỉ cho **seed**: độ quan tâm 12 tháng theo tuần + related queries top/rising | retry 3 lần với 429/lỗi mạng, chờ 2s → 5s → 10s |
| `reddit` | Reddit OAuth (app loại script, `client_credentials`), `GET /search?q=&t=year&sort=relevance&limit=100` | bài 12 tháng: id, subreddit, tiêu đề, url, điểm, số comment, ngày đăng, `is_app_request` | ≤ 1 req/s |

`is_app_request` = tiêu đề hoặc nội dung khớp (không phân biệt hoa thường) một trong:
`is there an app`, `looking for an app`, `app that`, `alternative to`, `recommend an app`.

**Key Reddit** đặt trong `.env.local`: `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`,
`REDDIT_USER_AGENT`. Thiếu key thì collector `reddit` ném lỗi mã `MISSING_KEYS`.

## Database

```
runs           id PK, seed, country, created_at
keywords       id PK, run_id FK, term, origin ('seed' | 'play_suggest')
source_jobs    run_id FK, source, status ('pending'|'running'|'done'|'error'),
               error_code, error_message, started_at, finished_at
               PK (run_id, source)
apps           id PK, store ('play'|'appstore'), store_app_id, title, developer,
               icon_url, url, genre, price, released_at
               UNIQUE (store, store_app_id)
app_snapshots  app_id FK, run_id FK, rating, ratings_count, installs_min (null với appstore),
               updated_at
               PK (app_id, run_id)
keyword_hits   keyword_id FK, app_id FK, rank      PK (keyword_id, app_id)
trend_points   run_id FK, date, value               PK (run_id, date)
trend_related  run_id FK, query, value, kind ('top'|'rising')
reddit_posts   run_id FK, keyword_id FK, post_id, subreddit, title, url, score,
               num_comments, created_at, is_app_request
               PK (run_id, post_id)
```

- `apps` upsert theo `(store, store_app_id)`: thông tin ít đổi.
- `app_snapshots` ghi số liệu hay đổi theo từng run. Lịch sử này để dành cho bản sau.
- Một bài Reddit khớp nhiều keyword thì chỉ lưu một lần, gắn với keyword khớp đầu tiên.

## Màn hình

### `/` — Trang chủ

- Ô nhập niche + dropdown nước (US, GB, VN, DE, JP; mặc định US) + nút **Research**.
- Danh sách run gần nhất: seed, nước, ngày, trạng thái 4 nguồn. Bấm vào để mở `/r/[id]`.

### `/r/[id]` — Kết quả

1. **Header:** seed, nước, ngày, 4 chip trạng thái (xám/xanh dương/xanh lá/đỏ). Chip đỏ có
   thông báo lỗi + nút **Thử lại**. Nút **Tra lại** (force) ở góc.
2. **Hàng số liệu** (tính trên keyword seed):
   - số app Play · số app App Store
   - số cài cao nhất trên Play
   - median rating (gộp 2 store)
   - tổng số rating của top 10 mỗi store
   - ngày ra mắt của app mới nhất
   - % app có lần update cuối > 365 ngày
   - số bài Reddit 12 tháng (trong đó bài xin app)
   - điểm Trends trung bình 12 tháng
3. **Bảng Keyword × Store:** mỗi keyword một dòng, gồm nguồn gốc, số app Play, số app
   App Store, app top 1 Play (tên + số cài + số rating), app top 1 App Store (tên + số rating).
4. **Đối thủ:** bảng gộp các app, không trùng, của mọi keyword. Lọc theo store, sắp xếp
   mọi cột, link ra store. Cột: icon, tên, store, dev, rating, số rating, số cài, update
   cuối, ra mắt, giá, số keyword app xuất hiện.
   Biểu đồ:
   - scatter rating × số rating (trục X log), màu theo store;
   - cột phân bố số cài Play theo mốc (<1K, 1K–10K, 10K–100K, 100K–1M, 1M+);
   - cột tuổi lần update cuối (<3 tháng, 3–12 tháng, 1–2 năm, >2 năm).
5. **Trends:** đường 12 tháng; cạnh đó 2 danh sách related queries (top, rising).
6. **Reddit:** cột số bài theo tháng; top 10 subreddit theo số bài; danh sách bài (bài
   `is_app_request` lên đầu, sau đó theo điểm).

Khối của nguồn đang chạy hiện skeleton, nguồn lỗi hiện hộp lỗi. Khối Reddit với lỗi
`MISSING_KEYS` hiện hướng dẫn tạo app tại reddit.com/prefs/apps và điền `.env.local`.

## Xử lý lỗi

- Mỗi collector chạy trong `try/catch` riêng. Lỗi thì ghi `error_code` + `error_message`
  vào `source_jobs`, không ảnh hưởng nguồn khác.
- Mã lỗi: `RATE_LIMITED`, `NETWORK`, `MISSING_KEYS`, `PARSE`, `UNKNOWN`.
- Lúc server khởi động: mọi `source_jobs` còn `running` (process cũ chết giữa chừng)
  chuyển thành `error` với mã `UNKNOWN`, message "interrupted".
- Ghi DB của một collector chạy trong một transaction: lỗi giữa chừng thì không để lại
  dữ liệu dở.

## Test

- **Unit (Vitest):** các hàm `normalizeX` của 4 collector với fixture JSON ghi lại từ lần gọi
  thật (`tests/fixtures/<source>/*.json`); các hàm tính số liệu tổng (median, phân mốc
  số cài, phân mốc tuổi update, đếm theo tháng).
- **Smoke:** `npm run smoke -- "habit tracker"` gọi thật cả 4 nguồn với DB tạm, in số dòng
  mỗi nguồn + lỗi nếu có. Không chạy trong CI.
- **UI:** mở preview, tra một niche thật, kiểm đủ 6 khối và trạng thái lỗi (chạy không có
  key Reddit).

## Cấu trúc thư mục

```
niche-radar/
├── src/
│   ├── app/                    page.tsx, r/[id]/page.tsx, api/research/...
│   ├── collectors/             playstore.ts appstore.ts trends.ts reddit.ts keywords.ts
│   ├── db/                     schema.ts client.ts
│   ├── lib/                    stats.ts rate-limit.ts run-research.ts
│   └── components/             StatTiles, KeywordTable, CompetitorTable, charts/...
├── scripts/smoke.ts
├── tests/                      *.test.ts + fixtures/
├── data/                       niche.db (gitignore)
└── docs/superpowers/specs/
```

## Rủi ro đã biết

- **Google Trends** không có API chính thức. Thư viện có thể gãy khi Google đổi endpoint.
  Đã cô lập trong một collector và có retry. Gãy hẳn thì thay thư viện chỉ trong file đó.
- **google-play-scraper** cào HTML, cũng có thể gãy, xử lý giống trên.
- **App Store không có số cài**: so sánh giữa 2 store chỉ dựa vào số rating.
- Kết quả search phụ thuộc nước (`country`): đổi nước thì ra danh sách khác.
