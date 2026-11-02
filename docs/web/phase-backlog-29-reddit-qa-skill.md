# Backlog 29 · Skill Reddit Q&A: tìm câu hỏi → nháp câu trả lời

> Một skill Claude Code dùng chung cho mọi sản phẩm: lái Chrome thật của người dùng để tìm câu hỏi trên Reddit
> quanh chuyện chọn niche app, gom thành hàng chờ `.md`, rồi viết nháp câu trả lời theo context của sản phẩm.
> Người dùng tự copy lên Reddit. Mục tiêu: có traffic từ những câu trả lời giúp được người hỏi thật.

<span class="chip chip--todo">Plan mới 2026-11-02 · chưa làm · dựa trên Backlog 27 (Claude Code lái Chrome)</span>

## 1. Vì sao lái Chrome mà không gọi API

- Claude Code mở bằng `claude --chrome` có bộ tool `claude-in-chrome` chạy trên **Chrome thật** của người dùng,
  sẵn đăng nhập Reddit. Trang được đọc như người lướt, không đụng giới hạn API Reddit, không cần key.
  Điều kiện và giới hạn của tuyến này: xem [Backlog 27 §1](phase-backlog-27-youtube-chrome-skill.md).
- Tab Gap hỏi đáp → Reddit trong app ([Phase 11](phase-11-reddit-gap.md)) vẫn bắt người dùng tự Cmd + S từng trang.
  Skill này làm thay bước mở + đọc, và làm thêm phần trả lời mà app không có.
- Chậm và cần người ngồi cạnh → hợp **≤ 15 trang tìm / lượt**, không hợp cào hàng loạt.

## 2. Chỗ để đồ

**Skill (chung, một bản cho cả máy)** — folder `reddit-qa` trong thư mục skill của Claude Code:

| File | Có gì |
|---|---|
| `SKILL.md` | luồng chính, 3 lệnh, luật cứng |
| `references/queries.md` | bộ câu tìm mặc định theo 5 nhóm (mục 3) + subreddit mặc định |
| `references/answer-rules.md` | luật viết câu trả lời cho Reddit (mục 5) |
| `templates/profile.md` | khung hồ sơ sản phẩm |
| `scripts/queue.mjs` | gộp kết quả thô → bỏ trùng → chấm điểm → ghi `queue.md`; đổi trạng thái 1 dòng |
| `scripts/queue.test.mjs` | test bỏ trùng, chấm điểm, đổi trạng thái (`node --test`) |

**Mỗi sản phẩm** — folder `marketing/reddit/` trong repo của sản phẩm đó (không nằm trong `docs/`):

| File | Có gì |
|---|---|
| `profile.md` | app làm gì · kinh nghiệm thật · số đã đo (nguồn + ngày) · link · subreddit nên tìm · câu tìm thêm |
| `queue.md` | bảng hàng chờ (mục 4) |
| `raw/YYYY-MM-DD.json` | kết quả tìm thô của mỗi lượt, để chạy lại `queue.mjs` không phải mở Chrome |
| `drafts/YYYY-MM-DD-<slug>.md` | mỗi bài nháp một file (mục 5) |

Chưa có `profile.md` → skill tạo từ khung, điền thử từ README / docs của repo, **dừng lại** cho người dùng sửa và xác nhận
rồi mới tìm.

## 3. Lệnh `/reddit-qa tìm [nhóm]`

5 nhóm câu tìm mặc định (tiếng Anh, sửa / thêm trong `profile.md`):

| Nhóm | Ví dụ câu tìm |
|---|---|
| `build` | "what app should I build", "app idea validation", "how to find a niche for an app" |
| `competitors` | "how to see competitors google play", "app store competitor research", "spy on competitor apps" |
| `trends` | "google trends app idea", "how to use google trends for app" |
| `ai` | "use claude for market research", "AI niche research", "chatgpt find app idea" |
| `keywords` | "ASO keyword competition", "how many competitors keyword app store", "keyword difficulty app" |

Subreddit mặc định: r/SideProject, r/indiehackers, r/androiddev, r/iOSProgramming, r/SaaS, r/Entrepreneur, r/startups,
r/AppBusiness. Có thể tìm cả Reddit (không giới hạn subreddit).

Luồng:

1. Kiểm tra phiên có tool `claude-in-chrome`. Không có → báo "mở lại bằng `claude --chrome`", dừng.
2. Mỗi câu tìm: mở trang Reddit search (bài, 12 tháng, sắp theo liên quan). Lấy dữ liệu bằng cách:
   **(a)** trong tab Reddit đang mở, đọc bản JSON của chính trang tìm (cùng domain, cùng cookie);
   **(b)** không được thì đọc chữ trên trang. Cách nào chạy ổn: ghi vào bảng thử (mục 7), lúc viết chưa đo.
3. Nghỉ 2–3 giây giữa 2 trang. Trần **15 trang / lượt**. Gặp đăng nhập / captcha / trang chặn → dừng, báo, không vượt.
4. Ghi kết quả thô vào `raw/YYYY-MM-DD.json` (id, tiêu đề, subreddit, upvote, số comment, ngày, link, bị khoá / lưu trữ không, câu tìm nào ra).
5. Chạy `node scripts/queue.mjs merge <folder>` → cập nhật `queue.md`.

## 4. Hàng chờ `queue.md`

Cột: `id` · `tiêu đề` · `subreddit` · `upvote` · `comment` · `ngày đăng` · `nhóm` · `điểm` · `trạng thái` · `link`.

- **Bỏ trùng** theo id bài Reddit. Bài đã có thì cập nhật upvote / comment, **giữ nguyên trạng thái**.
- **Bỏ luôn**: bài bị khoá hoặc lưu trữ (không trả lời được), bài quá 12 tháng.
- **Điểm 0–100** (công thức nằm trong `queue.mjs`, có test):
  độ mới (bài ≤ 30 ngày cao nhất) · số comment (đông nhưng chưa quá đông, > 200 comment thì câu trả lời mới dễ chìm) ·
  upvote · số câu tìm cùng ra bài đó (khớp nhiều nhóm = đúng chủ đề hơn).
- **Trạng thái:** `mới` → `đã nháp` → `đã đăng`, hoặc `bỏ qua`. Bảng xếp `mới` lên đầu, trong đó điểm cao lên trước.

## 5. Lệnh `/reddit-qa viết [1|3]` và luật trả lời

1. Lấy 1 hoặc 3 bài `mới` điểm cao nhất (mặc định 1). Mỗi subreddit tối đa 1 bài trong cùng 1 lần viết.
2. Mở thread bằng Chrome: đọc bài gốc + comment đứng đầu, để không trả lời lặp lại ý đã có; đọc luật subreddit
   (sidebar / wiki) về tự quảng cáo.
3. Viết bằng tiếng Anh dựa trên `profile.md`, lưu `drafts/YYYY-MM-DD-<slug>.md`, đổi trạng thái thành `đã nháp`.

Mỗi file nháp gồm:

- Link thread + tóm tắt câu hỏi 1 câu + ngày đọc
- **Câu trả lời** (Markdown của Reddit, dán thẳng được)
- Có nhắc sản phẩm không, vì sao; luật tự quảng cáo của subreddit đó
- Checklist trước khi đăng: còn đúng khi bỏ hết link? · số nào cũng có nguồn? · có ghi "I built this" nếu nhắc app? ·
  subreddit này tuần này đã đăng mấy bài?

<div class="box box--rules" markdown>
**Luật trả lời**

- Giúp người hỏi trước: câu trả lời vẫn dùng được khi bỏ hết link — có bước làm cụ thể, không chung chung
- Nhắc sản phẩm **chỉ khi** nó giải đúng câu hỏi, tối đa 1 lần, ghi rõ "I built this" — subreddit cấm thì không nhắc
- Không bịa số: chỉ số đã có trong `profile.md` (kèm nguồn), còn lại không nêu
- Không giả làm người dùng khác, không viết nhiều câu trả lời cho cùng 1 thread
- Mỗi subreddit ≤ 2 bài đã đăng / tuần (đếm từ `queue.md`); vượt thì skill nhắc và gợi ý subreddit khác
- Giọng tự nhiên, ngắn (thường 80–250 từ), không tiêu đề kiểu bài blog, không emoji tràn lan
</div>

## 6. Lệnh `/reddit-qa đã đăng <id>` · `bỏ qua <id>`

Gọi `node scripts/queue.mjs set <folder> <id> <trạng thái>`, ghi kèm ngày. Người dùng tự đăng lên Reddit, skill không biết
bài đã lên hay chưa nếu không được báo.

<div class="box box--rules" markdown>
**Luật cứng của skill**

- Chrome chỉ **đọc**: không đăng bài, không comment, không vote, không nhắn tin, không join subreddit
- Không đăng nhập, không nhập mật khẩu thay người dùng; gặp captcha / chặn → dừng, báo
- ≤ 15 trang tìm / lượt, nghỉ 2–3 giây giữa 2 trang
- Hàng chờ và nháp nằm trong repo sản phẩm, không nằm trong `docs/` (bị sync ra ngoài)
</div>

<div class="box box--star" markdown>
**Xong khi**

- Bảng thử (mục 7) điền đủ
- `queue.test.mjs` xanh: bỏ trùng giữ trạng thái, bỏ bài khoá / quá cũ, điểm đúng thứ tự trên dữ liệu mẫu, đổi trạng thái
- Chạy thật với Niche Radar: `/reddit-qa tìm` 1 nhóm ra `queue.md` đúng khung; `/reddit-qa viết 1` ra 1 nháp qua đủ checklist
- Chạy thử với 1 sản phẩm thứ hai chỉ bằng cách viết `profile.md` mới, không sửa skill
</div>

<div class="box box--danger" markdown>
**Không làm ở đây**

- Tự đăng / tự comment lên Reddit, hẹn giờ đăng
- Theo dõi upvote / traffic sau khi đăng (để sau, cần đo trước)
- Đưa tính năng này vào giao diện `web/` hay extension
- Nguồn khác ngoài Reddit (Stack Exchange, HN… đã có ở Gap hỏi đáp)
</div>

## 7. Bảng thử (điền lúc làm)

| Thử gì | Kết quả | Ngày |
|---|---|---|
| Đọc JSON trang tìm trong tab Reddit đã đăng nhập: chạy không, có bị chặn không | chưa đo | — |
| Đọc chữ trang tìm (dự phòng): đủ upvote / comment / ngày không | chưa đo | — |
| 15 trang / lượt: mất bao lâu, có bị Reddit hỏi captcha không | chưa đo | — |

Plan code: [2026-11-02 · Skill Reddit Q&A](../superpowers/plans/2026-11-02-reddit-qa-skill.md)

[← Backlog 27 · YouTube + skill lái Chrome](phase-backlog-27-youtube-chrome-skill.md) · [Phase 11 · Reddit Gap](phase-11-reddit-gap.md)
