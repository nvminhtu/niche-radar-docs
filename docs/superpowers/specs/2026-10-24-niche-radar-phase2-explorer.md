# niche-radar — Phase 2: Niche Explorer (niche → sub-niche → keyword)

> Ngày: 2026-10-24 · Trạng thái: **nháp định hướng**. Cần một vòng brainstorm (chốt các câu hỏi
> mở ở cuối) trước khi viết spec chi tiết và plan code. Bắt đầu sau khi v1 (Task 1–15) xong.

## Mục tiêu

v1 trả lời câu "**một keyword** đã có ai làm chưa". Phase 2 trả lời câu rộng hơn:
"**niche này có những ngách con nào, mỗi ngách người ta gõ những từ khoá gì, ngách nào
còn trống**".

Gõ một niche (ví dụ `habit tracker`), tool sẽ:

1. Mở rộng ra **hàng chục tới hàng trăm keyword** người dùng thật đang gõ trên store và Google.
2. Gom chúng thành **sub-niche**: theo đối tượng (`for adhd`, `for students`), theo dạng
   (`widget`, `printable`, `notion`), theo nền tảng (`ios`, `android`), theo tính năng
   (`streak`, `reminder`).
3. Mỗi keyword có **số liệu nhẹ**: độ phổ biến ước lượng và độ đông đối thủ trên từng store.
4. Bấm một nút thì một keyword hay một sub-niche được **"Research sâu"**: tạo một run v1 bình
   thường với keyword đó làm seed, dùng lại toàn bộ dashboard v1.
5. Node nào cũng **mở tiếp** được: sub-niche → keyword → keyword con, như một cây.

```
habit tracker                         (niche gốc)
├── theo đối tượng
│   ├── habit tracker for adhd        Play 8 app · iOS 10 app · gợi ý #2
│   ├── habit tracker for students
│   └── habit tracker for couples      ← ít đối thủ, đáng soi
├── theo dạng
│   ├── habit tracker widget
│   ├── habit tracker printable
│   └── habit tracker notion
└── theo tính năng
    ├── habit tracker with reminders
    └── streak tracker
```

## Nguồn mở rộng keyword (đều miễn phí, không cần key)

| Nguồn | Cách lấy | Ghi chú |
|---|---|---|
| Play autocomplete | `gplay.suggest` với seed + **alphabet soup** (`seed a` … `seed z`, `a seed` …) | v1 đã dùng `suggest`, chỉ thêm vòng lặp |
| App Store search hints | endpoint gợi ý tìm kiếm của App Store (dân ASO hay dùng) | **phải kiểm còn chạy không** trước khi chốt |
| Google autocomplete | `suggestqueries.google.com/complete/search?client=firefox&q=…` | gợi ý theo hành vi tìm kiếm Google |
| Google Trends | related queries top + rising | v1 đã lấy cho seed, phase 2 lấy thêm cho sub-niche |
| Mẫu bổ nghĩa | danh sách cố định: `for …`, `free`, `widget`, `offline`, `ai`, `app`, `tracker`… ghép với seed | chỉ giữ cái mà autocomplete xác nhận có người gõ |

**Ước lượng độ phổ biến (không có số search volume thật):**
- Keyword xuất hiện ở **vị trí đầu** của autocomplete khi mới gõ vài ký tự → phổ biến hơn.
- Xuất hiện ở **nhiều nguồn** (Play + App Store + Google) → chắc chắn hơn.
- Có điểm Trends → dùng làm số tương đối.

Đây là chỉ số tương đối để xếp hạng, không phải lượt tìm thật. UI phải ghi rõ điều đó.

## Gom sub-niche

- **2.3a — theo luật (không tốn tiền):** tách keyword thành `seed` + phần bổ nghĩa, gom theo
  phần bổ nghĩa đứng đầu (`for X` → đối tượng; `widget/printable/notion/excel` → dạng;
  `ios/android/mac` → nền tảng; còn lại → tính năng). Có bảng từ điển, sửa được.
- **2.3b — tuỳ chọn, dùng LLM:** gửi danh sách keyword cho Claude API để đặt tên và gom ngách
  cho tự nhiên hơn. Chỉ làm nếu 2.3a gom chưa đủ tốt; cần key Anthropic trong `.env.local`.

## Số liệu nhẹ cho mỗi keyword

Không chạy đủ 4 nguồn cho hàng trăm keyword (quá chậm, dễ bị chặn). Mỗi keyword chỉ lấy:

- số app trên Play và App Store (search top 30, **không** gọi chi tiết từng app);
- tổng số rating của top 5 app App Store (iTunes trả sẵn trong kết quả search) → "độ đông";
- vị trí trong autocomplete và số nguồn xác nhận → "độ phổ biến".

Keyword nào đáng soi kỹ → nút **Research sâu** → run v1 đầy đủ.

## Màn hình

- **`/explore`** — ô nhập niche (trang chủ v1 có thêm tab "Explore").
- **`/explore/[id]`**:
  - **Cây ngách:** danh sách thụt lề, gập/mở được, mỗi node có nút "Mở tiếp".
  - **Bảng keyword:** lọc theo sub-niche; cột nguồn, độ phổ biến, số app Play/iOS, độ đông;
    sắp xếp được; tick nhiều dòng → "Research sâu" hàng loạt (xếp hàng, chạy lần lượt).
  - **Biểu đồ "bản đồ ngách":** scatter độ phổ biến × độ đông, mỗi chấm là một keyword, màu
    theo sub-niche. Góc **phổ biến cao + ít đối thủ** là chỗ đáng soi.
- Trên dashboard v1, mỗi keyword trong bảng Keyword × Store có link "Explore từ đây".

## Dữ liệu (bảng mới, không đổi bảng v1)

```
explorations    id, seed, country, created_at
explore_nodes   id, exploration_id, parent_id, term, kind ('niche'|'subniche'|'keyword'),
                group_label, depth, created_at
node_sources    node_id, source ('play_suggest'|'appstore_hint'|'google_suggest'|'trends'|'pattern'),
                rank
node_metrics    node_id, play_count, appstore_count, appstore_top5_ratings, popularity_score,
                updated_at
node_runs       node_id, run_id        ← nối sang run v1 khi bấm "Research sâu"
```

Cache autocomplete **7 ngày** theo (term, country, source), vì gợi ý ít đổi.

## Giới hạn để không bị chặn

- Mỗi lần "Mở tiếp" tối đa **50 keyword mới**; độ sâu tối đa **3**.
- Dùng lại `createLimiter`: Play 1 req/s, iTunes 1 req/3s, Google suggest 1 req/s.
- Alphabet soup cho 1 seed ≈ 26–52 request → khoảng 1 phút. Chạy nền + polling như v1.

## Chia nhỏ phase

| Phase | Làm gì | Xong khi |
|---|---|---|
| **2.1** | Mở rộng keyword: alphabet soup Play + Google suggest + mẫu bổ nghĩa; lưu cây; trang `/explore/[id]` dạng danh sách | gõ `habit tracker` → ra ≥ 80 keyword có nguồn |
| **2.2** | Số liệu nhẹ cho từng keyword + nút Research sâu (một hoặc nhiều keyword) | bảng sắp xếp được theo độ đông; bấm → mở run v1 |
| **2.3** | Gom sub-niche theo luật + cây gập/mở + "Mở tiếp" từng node | cây 3 tầng; mở tiếp một node ra keyword con |
| **2.4** | Bản đồ ngách (scatter) + App Store hints nếu endpoint còn chạy | scatter tô màu theo sub-niche |
| 2.5 *(tuỳ chọn)* | Gom ngách bằng LLM; so sánh 2–3 niche cạnh nhau | — |

## Câu hỏi mở (chốt ở vòng brainstorm)

1. Có muốn **chấm điểm cơ hội** cho từng sub-niche không, hay giữ đúng tinh thần v1 là chỉ hiện
   dữ liệu thô (bản đồ ngách đã gần như là chấm điểm bằng mắt)?
2. Thứ tự ưu tiên nguồn: Play + Google trước, App Store hints sau, có ổn không?
3. Có muốn dùng Claude API để gom ngách (2.3b / 2.5) không? Tốn tiền theo lượt gọi.
4. "Research sâu" hàng loạt: giới hạn bao nhiêu keyword một lần (đề xuất 10)?
5. Có cần xuất bảng keyword ra CSV không?

## Giới hạn nguồn & chia sẻ (2026-10-24)

Phase 2 gọi thêm Play suggest + Google autocomplete (~27–35 request mỗi lần "Mở rộng") và App Store search cho số
liệu (~2,5 phút cho 50 keyword). Giữ mô hình chạy local, mỗi người một IP, không proxy. Bảng giới hạn từng nguồn,
proxy và cách đưa tool cho người khác: `2026-10-24-niche-radar-limits-and-sharing.md`.
