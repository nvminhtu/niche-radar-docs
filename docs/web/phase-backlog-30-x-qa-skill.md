# Backlog 30 · Skill X Q&A: tìm câu hỏi trên X → nháp câu trả lời

> Anh em của [Backlog 29 · Skill Reddit Q&A](phase-backlog-29-reddit-qa-skill.md), đổi nguồn sang X.
> Một skill Claude Code dùng chung cho mọi sản phẩm: lái Chrome thật của người dùng để đọc trang tìm kiếm X, lấy các bài
> hỏi quanh chuyện chọn niche app ("is there an app…", "I'd pay for…", "which niche…"), gom thành hàng chờ `.md`, rồi
> viết nháp câu trả lời theo context của sản phẩm. Người dùng tự đăng lên X.

<span class="chip chip--todo">Plan mới 2026-11-02 · chưa làm · làm sau khi Backlog 29 chạy thật</span>

## 1. Vì sao làm, vì sao lái Chrome

- X có rất nhiều câu hỏi xin app và câu "I'd pay for…", kèm like / reply / view để đo mức quan tâm
  ([bản đồ nguồn gap, mục 15](gap-sources-map.md)). Niche Radar hiện **chưa có nguồn X**.
- API chính thức không còn gói free: đọc $0.005 / bài (đo 2026-10-26), nên đang để **Dự bị**.
- Claude Code mở bằng `claude --chrome` đọc được trang tìm kiếm X trên Chrome đã đăng nhập sẵn, không tốn tiền API.
  Điều kiện và giới hạn của tuyến lái Chrome: xem [Backlog 27 §1](phase-backlog-27-youtube-chrome-skill.md).
- **Rủi ro điều khoản:** điều khoản của X cấm truy cập tự động / cào khi chưa được phép. Skill này chỉ làm việc người dùng
  vẫn làm bằng tay (mở vài trang tìm, đọc), có người ngồi cạnh, trần thấp hơn Reddit (mục 3). Không chạy nền, không hẹn giờ,
  không cào hàng loạt. Cần dữ liệu đều đặn, số lớn → dùng API chính thức (mục 8), không nới trần của skill.

## 2. Chỗ để đồ

**Skill (chung, một bản cho cả máy)**: folder `x-qa` trong thư mục skill của Claude Code, cạnh `reddit-qa`.

| File | Có gì |
|---|---|
| `SKILL.md` | luồng chính, 3 lệnh, luật cứng |
| `references/queries.md` | bộ câu tìm mặc định theo nhóm (mục 3), dùng toán tử tìm kiếm của X |
| `references/answer-rules.md` | luật viết reply cho X (mục 5) |
| `templates/profile.md` | khung hồ sơ sản phẩm, cùng khung với `reddit-qa`, thêm mục tài khoản X của sản phẩm |
| `scripts/queue.mjs` | gộp kết quả thô → bỏ trùng → chấm điểm → ghi `queue.md`; đổi trạng thái 1 dòng |
| `scripts/queue.test.mjs` | test bỏ trùng, chấm điểm, đổi trạng thái (`node --test`) |

`queue.mjs` chép từ `reddit-qa` rồi đổi cột (mục 4). Không gộp 2 skill làm một ở bước này: luật trả lời và cách chấm điểm
khác nhau. Khi cả hai chạy ổn mới tính tách phần chung.

**Mỗi sản phẩm**: folder `marketing/x/` trong repo của sản phẩm đó (không nằm trong `docs/`).

| File | Có gì |
|---|---|
| `profile.md` | dùng lại nội dung `marketing/reddit/profile.md` nếu có, thêm câu tìm riêng cho X |
| `queue.md` | bảng hàng chờ (mục 4) |
| `raw/YYYY-MM-DD.json` | kết quả tìm thô của mỗi lượt |
| `drafts/YYYY-MM-DD-<slug>.md` | mỗi reply nháp một file (mục 5) |

Lúc làm: tạo `marketing/x/` thì sửa cùng lúc README gốc, `marketing/README.md`, `CLAUDE.md`, `docs/cach-dung.md` và
`CHANGELOG.md`.

## 3. Lệnh `/x-qa tìm [nhóm]`

Câu tìm dùng toán tử của X, mặc định thêm `lang:en -filter:replies` và `since:` 30 ngày trước:

| Nhóm | Ví dụ câu tìm |
|---|---|
| `ask` | `"is there an app" min_faves:3` · `"is there a tool" app` · `"anyone know an app"` |
| `pay` | `"I'd pay for" (app OR tool)` · `"take my money" app` |
| `wish` | `"wish there was an app"` · `"why is there no app"` |
| `niche` | `("app idea" OR "which niche") (indie OR solo) min_replies:3` · `"validate" "app idea"` |
| `aso` | `"ASO" (keyword OR competitors) min_faves:2` · `"app store" "keyword research"` |

Câu tìm theo chủ đề cụ thể (vd `"is there an app" budget`) ghi trong `profile.md` của từng sản phẩm.

Luồng:

1. Kiểm tra phiên có tool `claude-in-chrome`. Không có → báo "mở lại bằng `claude --chrome`", dừng.
   Chrome chưa đăng nhập X → báo người dùng tự đăng nhập, dừng. Skill không đăng nhập thay.
2. Mỗi câu tìm: mở `x.com/search?q=…&f=live` (tab Latest). Lấy dữ liệu theo thứ tự thử:
   **(a)** đọc phản hồi mạng mà trang tự gọi khi tải kết quả (Chrome đã tải sẵn, skill không gọi thêm request nào);
   **(b)** không được thì đọc chữ trên trang. Cách nào chạy ổn: ghi vào bảng thử (mục 7), lúc viết chưa đo.
3. Cuộn tối đa 2 lần mỗi câu tìm. Nghỉ 3–5 giây giữa 2 trang. Trần **10 trang tìm / lượt**.
   Gặp captcha / "rate limit exceeded" / trang khoá → dừng, báo, không vượt.
4. Ghi kết quả thô vào `raw/YYYY-MM-DD.json`: id bài, chữ bài, @tài khoản, số người theo dõi (nếu đọc được), like, reply,
   repost, view, ngày đăng, link, câu tìm nào ra.
5. Chạy `node scripts/queue.mjs merge <folder>` → cập nhật `queue.md`.

## 4. Hàng chờ `queue.md`

Cột: `id` · `chữ bài` (cắt 120 ký tự) · `tài khoản` · `like` · `reply` · `view` · `ngày đăng` · `nhóm` · `khớp` · `điểm` ·
`trạng thái` · `ngày đổi` · `link`.

- **Bỏ trùng** theo id bài. Bài đã có thì cập nhật số, **giữ nguyên trạng thái**.
- **Bỏ luôn**: bài quá 30 ngày (trên X reply muộn gần như không ai thấy), bài của chính tài khoản sản phẩm, bài quảng cáo.
- **Điểm 0–100** (công thức nằm trong `queue.mjs`, có test): độ mới nặng hơn Reddit (≤ 3 ngày cao nhất) · số reply
  (có người đang bàn nhưng chưa quá đông, > 100 reply thì reply mới dễ chìm) · like / view · số câu tìm cùng ra bài đó.
- **Trạng thái:** `mới` → `đã nháp` → `đã đăng`, hoặc `bỏ qua`. Bảng xếp `mới` lên đầu, trong đó điểm cao lên trước.

## 5. Lệnh `/x-qa viết [1|3]` và luật trả lời

1. Lấy 1 hoặc 3 bài `mới` điểm cao nhất (mặc định 1). Mỗi tài khoản tối đa 1 bài trong cùng 1 lần viết.
2. Mở bài bằng Chrome: đọc bài gốc + các reply đứng đầu, để không lặp ý đã có.
3. Viết bằng tiếng Anh dựa trên `profile.md`, lưu `drafts/YYYY-MM-DD-<slug>.md`, đổi trạng thái thành `đã nháp`.

Mỗi file nháp gồm:

- Link bài + tóm tắt câu hỏi 1 câu + ngày đọc
- **Reply** (chữ thuần, dán thẳng được, đếm sẵn số ký tự, ≤ 280 nếu tài khoản không có Premium)
- Có nhắc sản phẩm không, vì sao
- Checklist trước khi đăng: còn đúng khi bỏ link? · số nào cũng có nguồn? · có ghi "I built this" nếu nhắc app? ·
  hôm nay tài khoản đã reply mấy bài có link?

<div class="box box--rules" markdown>
**Luật trả lời**

- Giúp người hỏi trước: reply vẫn dùng được khi bỏ link, có 1–2 bước làm cụ thể
- Nhắc sản phẩm **chỉ khi** nó giải đúng câu hỏi, tối đa 1 lần, ghi rõ "I built this"; link đặt cuối hoặc để ở reply thứ hai
- Không bịa số: chỉ số đã có trong `profile.md` (kèm nguồn), còn lại không nêu
- Không giả làm người dùng khác, không reply nhiều lần vào cùng 1 bài, không tag người lạ
- ≤ 3 reply có link / ngày (đếm từ `queue.md`); vượt thì skill nhắc dừng
- Giọng tự nhiên, ngắn, không hashtag, không emoji tràn lan
</div>

## 6. Lệnh `/x-qa đã đăng <id>` · `bỏ qua <id>`

Gọi `node scripts/queue.mjs set <folder> <id> <trạng thái>`, ghi kèm ngày. Người dùng tự đăng lên X; skill không biết reply
đã lên hay chưa nếu không được báo.

<div class="box box--rules" markdown>
**Luật cứng của skill**

- Chrome chỉ **đọc**: không đăng, không reply, không like, không repost, không follow, không nhắn tin
- Không đăng nhập, không nhập mật khẩu thay người dùng; gặp captcha / chặn → dừng, báo
- ≤ 10 trang tìm / lượt, nghỉ 3–5 giây giữa 2 trang; không chạy nền, không hẹn giờ
- Không gọi thẳng API nội bộ của X; chỉ đọc những gì trang đã tự tải
- Hàng chờ và nháp nằm trong repo sản phẩm, không nằm trong `docs/` (bị sync ra ngoài)
</div>

<div class="box box--star" markdown>
**Xong khi**

- Bảng thử (mục 7) điền đủ
- `queue.test.mjs` xanh: bỏ trùng giữ trạng thái, bỏ bài quá 30 ngày / bài của chính mình, điểm đúng thứ tự trên dữ liệu mẫu,
  đổi trạng thái, nháp > 280 ký tự bị báo
- Chạy thật với Niche Radar: `/x-qa tìm ask` ra `queue.md` đúng khung; `/x-qa viết 1` ra 1 nháp qua đủ checklist
- Chạy thử với 1 sản phẩm thứ hai chỉ bằng cách viết `profile.md` mới, không sửa skill
</div>

<div class="box box--danger" markdown>
**Không làm ở đây**

- Tự đăng / tự reply lên X, hẹn giờ đăng
- Theo dõi like / traffic sau khi đăng
- Đưa X vào giao diện `web/` hay extension (là tuyến API, mục 8)
</div>

## 7. Bảng thử (điền lúc làm)

| Thử gì | Kết quả | Ngày |
|---|---|---|
| Đọc phản hồi mạng của trang tìm (Latest): có đủ like / reply / view / ngày không | chưa đo | — |
| Đọc chữ trang tìm (dự phòng): đủ số không, ngày có ra dạng tuyệt đối không | chưa đo | — |
| Mỗi trang cuộn 2 lần ra bao nhiêu bài | chưa đo | — |
| 10 trang / lượt: mất bao lâu, có bị X hỏi captcha / báo giới hạn không | chưa đo | — |
| Tỉ lệ bài đúng chủ đề ở nhóm `ask` (đọc tay 20 bài đầu) | chưa đo | — |

## 8. Sau này: tuyến API (không làm ở đây)

Nếu skill cho thấy X ra gap tốt (đo từ bảng thử + số reply đã đăng có người tương tác) thì mới mở phase riêng: nguồn X trong
tab Gap hỏi đáp của `web/`, gọi API chính thức bằng key của người dùng, có trần chi tiêu / tuần hiện trên UI. Giá và điều
khoản xem [bản đồ nguồn gap, mục 15](gap-sources-map.md). Người dùng tự tạo key, app không nhập key thay.

[← Backlog 29 · Skill Reddit Q&A](phase-backlog-29-reddit-qa-skill.md) · [Bản đồ nguồn gap](gap-sources-map.md)
