# Research · Pinterest Trends cho flow skill

> Đánh giá lại nguồn số 6 của [Bản đồ nguồn gap](gap-sources-map.md) theo yêu cầu anh 2026-11-02:
> lấy keyword Pinterest Trends gắn vào flow skill của AI Agent, rồi thử tìm keyword cho nhóm **phụ nữ Mỹ làm side
> project / work from home**. Kiểm ngày **2026-11-02**. Chưa đăng ký tài khoản dev Pinterest, chưa gọi được API thật,
> nên mọi số Pinterest ở trang này đều ghi nguồn, còn lại ghi `chưa đo`.

<span class="chip chip--skip">KO LÀM · anh chốt 2026-11-02 · ưu tiên đi bán, giữ trang để tham khảo</span>

<div class="box box--danger" markdown>
**Đã chốt 2026-11-02: không làm.** Không code collector, tool MCP hay skill `pinterest-seeds` cho Niche Radar — anh ưu
tiên đi bán bản hiện có. Trang này chỉ giữ lại kết quả research; muốn làm lại → kéo vào plan, sửa Master Plan trước.
</div>

<div class="box box--star" markdown>
**Tóm tắt**

- **Có API chính thức:** Pinterest API v5 `GET /v5/trends/keywords/{region}/top/{trend_type}` trả tối đa 50 keyword
  đang lên, lọc được theo **giới tính** (`genders`), **tuổi** (`ages`), **nhóm sở thích** (`interests`) và
  **chữ phải có** (`include_keywords`). Đây đúng là bộ lọc "phụ nữ Mỹ hay search gì" anh cần.
- **Vướng:** cần token OAuth (scope `ads:read`) của tài khoản Pinterest Business, và nhiều nguồn nói endpoint này
  **chưa mở cho mọi app** — phải xin quyền. Chưa đo được mất bao lâu.
- **Không dùng:** quét trang `trends.pinterest.com` (điều khoản cấm), actor Apify (trả phí, vẫn là quét), MCP Pinterest
  cộng đồng (chỉ làm pin / board, không có Trends).
- **Đề xuất:** collector đọc API chính thức bằng token của người dùng + skill mới `pinterest-seeds` trong AI Agent.
  Không có token thì người dùng dán keyword đọc tay từ trang Trends. Pinterest chỉ là **nguồn hạt giống**; nhu cầu app
  vẫn đo bằng Play / App Store như cũ.
- **Kết luận cũ "Bỏ" đổi thành "Ứng viên":** lý do bỏ cũ là lệch app Mac / SaaS, nhưng với app mobile lifestyle cho
  phụ nữ (tiền, kế hoạch, sức khoẻ, việc nhà) thì Pinterest là nơi họ tìm ý tưởng trước khi tìm app.
</div>

## 1 · Các đường lấy dữ liệu

### A · Pinterest API v5 · Trends (chính thức) — nên dùng

- **Endpoint:** `GET https://api.pinterest.com/v5/trends/keywords/{region}/top/{trend_type}`
- **`region`:** `US`, `CA`, `GB+IE`, `AU+NZ`, `DE`, `FR`, `BR`, `MX`… (danh sách trong spec).
- **`trend_type`:** `growing` (tăng mạnh quý vừa rồi) · `monthly` (nhiều lượt tháng vừa rồi) · `yearly` (nhiều lượt
  năm vừa rồi) · `seasonal` (tăng trong tháng và lặp theo mùa).
- **`genders`:** `female`, `male`, `unknown` · **`ages`:** dải tuổi, ví dụ trong spec có `35-44`, `50-54`
  (danh sách đủ: `chưa đo`).
- **`interests`:** 25 nhóm, trong đó hợp app cho phụ nữ: `finance`, `education`, `health`, `beauty`, `parenting`,
  `food_and_drinks`, `home_decor`, `diy_and_crafts`, `event_planning`, `wedding`.
- **`include_keywords`:** chỉ trả keyword có chứa ít nhất một chữ trong danh sách (ví dụ `side hustle`, `budget`).
- **`normalize_against_group=true`:** so độ lớn tương đối giữa các keyword trong cùng lượt gọi (0–100).
- **Trả về mỗi keyword:** `pct_growth_wow` · `pct_growth_mom` · `pct_growth_yoy` (% tăng tuần / tháng / năm) và
  `time_series` theo tuần trong 1 năm (0–100). **Không có số lượt search tuyệt đối.** Chỉ có số của hôm nay, không
  hỏi lại ngày cũ được → muốn có lịch sử phải tự lưu mỗi lần gọi.
- **Quyền:** OAuth 2.0, scope `ads:read`. Nguồn bên thứ ba nói cần tài khoản Business / Ads đã duyệt; diễn đàn dev
  Pinterest có câu hỏi xin quyền endpoint này → coi như **phải xin**, thời gian duyệt `chưa đo`.
- **Repo chính thức:** `pinterest/pinterest-python-generated-api-client` (client Python sinh từ OpenAPI, commit mới
  nhất 2026-08-27). App ta chạy Node nên **không cần nhúng Python** — gọi REST bằng `fetch` như collector Trends / suggest.

### B · Đọc tay trang trends.pinterest.com — đường dự phòng

- Trang dựng bằng JS, không API công khai, điều khoản cấm quét tự động.
- Người dùng tự mở trang, lọc (Mỹ · nữ · nhóm sở thích), rồi **dán danh sách keyword** vào app — giống cách
  Reddit Gap nhập trang đã lưu từ Chrome. Trang có nút tải file hay không: `chưa đo`.

### C · Không dùng

| Đường | Lý do |
|---|---|
| Actor Apify (`pinterest-trends-scraper` của vài tác giả) | trả phí theo kết quả, bản chất vẫn quét trang Trends → rủi ro điều khoản như quét trực tiếp |
| MCP Pinterest cộng đồng (`collactivelabs/pinterest-mcp-server`, CData…) | chỉ đọc / tạo pin, board, analytics tài khoản; không thấy tool Trends |
| Repo Python quét Pinterest (`pinscrape`, `Pinterest_Scrapper`) | chỉ tải ảnh / video theo keyword, không có xu hướng |
| Typeahead nội bộ `pinterest.com/resource/…` | endpoint nội bộ, điều khoản cấm |

## 2 · Gắn vào flow skill

Theo [Phase 28.3 · bộ skill](phase-28-3-skills.md) (1 skill = 1 việc, khuôn JSON trong code, skill không tự ghi) và
[AI Agent](phase-28-6-ai-agent.md) (skill `/find-niches`, `/long-tail`, `/kill-weak`).

1. **Collector `web/src/collectors/pinterest-trends.ts`** — gọi endpoint A bằng token người dùng nhập ở Cài đặt
   (không token → tắt, nút xám "sắp có"). Cache 7 ngày theo bộ lọc, giãn nhịp như Google Trends, lưu mỗi lượt gọi
   (vì API không trả ngày cũ). Thêm nguồn `pinterest_trend` cạnh `play_suggest` · `google_suggest` · `appstore_hint`
   để Explore dùng được.
2. **Tool MCP chỉ đọc `get_pinterest_trends`** — nhận `region`, `trend_type`, `genders`, `ages`, `interests`,
   `include_keywords`; trả keyword + 3 mức % tăng + ngày gọi. Mọi số trích kèm `[Pinterest Trends · US · 2026-11-02]`.
3. **Skill mới `pinterest-seeds`** (AI Agent, chặng Research niche):
    1. Đổi câu của người dùng ("phụ nữ Mỹ làm side project") thành bộ lọc: `US` · `female` · tuổi · 1–3 `interests`
       · 3–6 `include_keywords`.
    2. Gọi `get_pinterest_trends` với `growing` và `yearly` → gom, bỏ trùng.
    3. **Dịch ý Pinterest sang câu tìm app:** Pinterest có nhiều "ý tưởng / ảnh đẹp / printable"; skill chỉ giữ keyword
       có việc lặp lại mà app làm được (theo dõi, lên lịch, tính, nhắc) và viết lại thành 2–4 chữ người ta gõ trên store.
    4. `propose_candidates` (≤ 8, lý do kèm keyword Pinterest gốc + % tăng) → `start_research` → các bước cũ
       (`/kill-weak`, `/long-tail`) chạy như bình thường.
4. **Không có token:** skill hỏi người dùng dán danh sách đọc tay từ đường B, rồi làm từ bước 3.

<div class="box box--rules" markdown>
**Luật riêng cho nguồn này**

- Pinterest chỉ cho **% tăng tương đối**, không có lượt search → không đưa vào điểm "Nhu cầu"; điểm vẫn tính từ
  Play / App Store / Google Trends. Pinterest chỉ hiện ở lý do đề xuất và một dòng "Xu hướng Pinterest" trong evidence.
- Lọc `female` là lọc của Pinterest theo hồ sơ người dùng, không phải app tự đoán giới tính — giữ đúng luật Phase 19.
- Token của người dùng, lưu như key AI; app không tự đăng ký hay xin quyền thay.
</div>

## 3 · Làm thử · phụ nữ Mỹ, side project / work from home

Máy cloud chạy research này bị chặn mạng tới Pinterest, Google suggest, Play, App Store → **chưa gọi được số thật**.
Dưới đây là bộ lọc sẽ gọi và danh sách keyword hạt giống để chạy Research trong app; cột số để `chưa đo` tới khi
chạy trên máy anh.

### Bộ lọc sẽ gọi

| # | region | trend_type | genders | interests | include_keywords |
|---|---|---|---|---|---|
| 1 | US | growing | female | finance | side hustle, business ideas, work from home, extra income |
| 2 | US | yearly | female | finance | budget, savings, debt, money |
| 3 | US | growing | female | education, parenting | mom, teacher, schedule, routine |
| 4 | US | seasonal | female | diy_and_crafts, food_and_drinks | sell, business, pricing, bakery |
| 5 | US | growing | female | health, beauty | self care, cycle, routine, tracker |

Số có nguồn tìm được (cũ, chỉ để biết hướng): báo cáo Ngày Phụ nữ của Pinterest ghi tìm kiếm "business ideas start up"
**+941%** (tháng 1/2019 → tháng 1/2020). Pinterest Predicts 2026 xếp xu hướng **Pen Pals** với "cute stamps" +105%,
"penpal ideas" +90% (các trang trích lệch nhau ở "snail mail gifts": +110% hay +35%).

### Keyword hạt giống (Pinterest → câu tìm app)

| Ý người dùng gõ trên Pinterest | Câu tìm app để chạy Research | Loại app | Pinterest % tăng |
|---|---|---|---|
| side hustle ideas for women | side hustle tracker · income tracker | tiền | chưa đo |
| business ideas for women from home | small business planner | kế hoạch | chưa đo |
| work from home mom schedule | wfh schedule planner · mom planner | kế hoạch | chưa đo |
| budget planner printable | budget planner · paycheck budget | tiền | chưa đo |
| cash envelope / savings challenge | cash envelope budget · savings challenge | tiền | chưa đo |
| sinking funds | sinking funds tracker | tiền | chưa đo |
| how to price crafts | craft pricing calculator | công cụ bán hàng | chưa đo |
| home bakery business | bakery order tracker | công cụ bán hàng | chưa đo |
| nail tech / lash business | salon booking for solo | đặt lịch | chưa đo |
| content ideas for small business | content planner small business | marketing | chưa đo |
| virtual assistant for beginners | freelance time tracker · client invoice | công cụ làm thuê | chưa đo |
| teacher side hustle | lesson plan to sell · tutor schedule | giáo dục | chưa đo |
| daily routine aesthetic | routine planner · habit tracker aesthetic | thói quen | chưa đo |
| meal prep for busy moms | family meal planner | việc nhà | chưa đo |
| cycle syncing | cycle syncing planner | sức khoẻ | chưa đo |

**Bước tiếp khi có máy chạy mạng:** dán cột "Câu tìm app" vào AI Agent → `/find-niches` (hoặc `pinterest-seeds` khi
đã code) → `/kill-weak`. Ghi kết quả vào cột cuối cùng ngày đo.

## 4 · Đã chốt

- 2026-11-02: **không làm** tính năng / skill Pinterest. Không xin quyền API, không mở mạng cloud cho Pinterest.

## Nguồn

- [Spec endpoint `trending_keywords_list` · repo client chính thức của Pinterest](https://github.com/pinterest/pinterest-python-generated-api-client/blob/main/docs/KeywordsApi.md)
- [Pinterest Developers · Trends](https://developers.pinterest.com/docs/analytics-and-reports/trends/) · [List trending keywords](https://developers.pinterest.com/docs/api/v5/trending_keywords-list/)
- [Diễn đàn dev Pinterest · xin quyền List Trending Keywords](https://community.pinterest.biz/t/list-trending-keywords-access/2617)
- [Điều khoản Pinterest](https://policy.pinterest.com/en/terms-of-service)
- [Apify · Pinterest Trends Scraper](https://apify.com/automation-lab/pinterest-trends-scraper) · [MCP Pinterest cộng đồng (glama)](https://glama.ai/mcp/servers/collactivelabs/pinterest-mcp-server/tree)
- [Pinterest · báo cáo hỗ trợ phụ nữ (+941% "business ideas start up")](https://newsroom-archive.pinterest.com/en-gb/living-single-buying-a-home-and-negotiating-salaries-how-pinterest-is-supporting-empowering)
- [Pinterest Create · Pinterest Predicts 2026](https://create.pinterest.com/blog/2026-pinterest-predicts-trends-and-content-ideas/) · [pgbuzz · Pen Pals](https://www.pgbuzz.net/lets-get-writing/)

[← Bản đồ nguồn gap](gap-sources-map.md)
