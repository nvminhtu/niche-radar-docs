# Plan · Gắn event GA4 cho các cửa vào shotmatic.app

> Mục đích: nhìn GA4 là trả lời được **khách vào site để làm gì**: tải app, xài free tool, đọc blog hay đọc guide, và
> từ cửa đó họ có đi tới lượt tải không. Trang này là plan, chưa sửa code.

<span class="chip chip--todo">Plan · chờ duyệt · 2026-11-07 · GA4 chưa đọc được qua MCP (thiếu khoá service account)</span>

<div class="box box--goal" markdown>
**Kết luận**

- **Không cần gắn event vào từng nút.** Site đã có GA4 (`G-58F6TSQ8M9`) và đã có event cho nút tải, Idea Checker, mua PRO.
  Thứ còn thiếu là **gom mỗi trang vào 1 trong 5 cửa** và **đếm lượt bấm đi từ cửa này sang cửa khác**. Hai việc này làm ở 1 chỗ (`pages/_app.jsx`).
- **Có 1 lỗ đang làm sai số ngay bây giờ:** 117 bài blog có link `/download?ref=blog-<slug>`, nhưng khi mở hộp tải thì `ref` bị bỏ, lượt tải ghi `place=direct`.
  Nghĩa là hiện tại **không biết bài nào ra lượt tải**. Sửa cái này trước.
- **Target:** sau 28 ngày, trả lời được bằng số: mỗi cửa có bao nhiêu phiên, mỗi cửa ra bao nhiêu `download`.

**Xong khi:** mở GA4 → Reports → Engagement → Pages and screens, chọn chiều *Content group*, thấy đủ 5 cửa; và báo cáo
`download` theo `place` không còn dồn hết vào `direct`.
</div>

## Hiện đang đo được gì

Đọc từ `nvminhtu/shotmatic` bản `origin/main` (commit `7c3499c`). Bản checkout ở máy đang chậm 12 commit, khi làm phải tạo nhánh từ `origin/main`.

**Đã có, giữ nguyên:**

- `page_view` tự động cho mọi trang. Site dùng thẻ `<a>` thường nên mỗi lần chuyển trang là tải lại trang, GA4 đếm đúng.
- `download_click` khi bấm bất kỳ nút Download nào, kèm `place` (`nav`, `hero`, `final`, `sticky`, `blog_nav`, `blog_sticky`, `blog:<slug>`, `tool:idea-checker:*`).
- `download` khi khách nhập email xong và file `.dmg` bắt đầu tải. Đây là con số quan trọng nhất.
- `generate_lead` khi form email gửi thành công.
- `tool_run`, `tool_export`, `tool_locked_tab` cho App Idea Checker.
- `blog_next` khi bấm bài tiếp theo trong bài (`toc`, `inline`, `end_next`, `older`, `newer`, `end_more`).
- `checkout_click`, `buy_reserve` cho nút mua PRO.
- `tour_*`, `brief_*`, `shot_zoom` cho phần demo trên trang chủ.

**Chưa có:**

- Không biết một trang thuộc cửa nào. Muốn xem "bao nhiêu người vào để đọc blog" phải tự lọc theo đường dẫn mỗi lần.
- Không đếm lượt bấm menu **Guide**, **Blog**, link sang free tool, link "Every feature, step by step", link ở footer.
- Không đếm lượt mở bài từ trang danh sách blog (`/blog`, `/blog/all`, trang chủ đề).
- Không đếm lượt mở guide từ `/features`.
- `/scorecard` không có event nào khi khách dùng checklist.
- Link CTA trong bài (`/download?ref=blog-<slug>`) bị mất `ref` như nói ở trên.

## 5 cửa vào

Mỗi trang thuộc đúng 1 cửa. Cửa của **trang đầu tiên** khách vào là câu trả lời cho "họ vào để làm gì".

1. **`download` · Tải app.** Trang chủ `/` khi mở bằng `/#download` hoặc `/download`. Hành động cần đếm: `download_click` → `download`.
2. **`tool` · Xài free tool.** `/app-idea-checker`, `/scorecard`. Hành động cần đếm: `tool_run`.
3. **`blog` · Đọc blog.** `/blog`, `/blog/all`, `/blog/category/*`, `/blog/<slug>`. Hành động cần đếm: đọc hết bài, bấm sang bài khác, bấm tải.
4. **`guide` · Đọc hướng dẫn.** `/features`, `/features/<slug>`, `/ai`. Hành động cần đếm: mở 1 guide, bấm tải.
5. **`product` · Xem sản phẩm.** Trang chủ `/` mở bình thường, `/app-store-keyword-research`, `/app-competitor-analysis`. Hành động cần đếm: xem giá, bấm tải.

Các trang còn lại (`/privacy`, `/terms`, `/desktop/privacy`) vào nhóm `other`.

`/app-store-keyword-research` và `/app-competitor-analysis` là trang giới thiệu tính năng để bắt từ khoá, không có ô tìm kiếm thật, nên xếp vào `product`, không xếp vào `tool`.

## Việc cần làm

### Bước 1 · Sửa lỗ `ref` của link tải trong bài (Claude)

<span class="chip chip--done">Xong · deploy 2026-11-08 · commit `1cc55de` trên `main`</span>

Đã thử trên bản build production ở máy: `/download?ref=blog-habit-tracker-ideas` gửi đúng 1 `download_click` với `place=blog-habit-tracker-ideas` và mở hộp tải; `ref` có ký tự lạ bị lọc (`blog-habittrackerscript`); `/download` không có `ref` vẫn ghi `direct`; nút Download trên menu vẫn ghi `nav`.
Trên shotmatic.app sau deploy: `/download?ref=blog-claude-test-check` gửi `download_click` với `place=blog-claude-test-check` (lượt thử này nằm trong số GA4, bỏ qua khi đọc).

- **Vấn đề:** `/download` chuyển sang `/?ref=blog-<slug>#download`. `DownloadGate` mở hộp với `place='direct'` và không đọc `ref`.
- **Sửa:** trong `components/niche-radar/DownloadGate.jsx`, khi mở hộp do `#download` thì lấy `ref` trên URL làm `place`
  (ví dụ `place=blog-habit-tracker-ideas`), không có `ref` mới dùng `direct`. Bắn thêm `download_click` lúc đó để số bấm và số tải khớp nhau.
- **Kiểm tra:** mở `/download?ref=blog-test` trên máy, xem request `collect` gửi lên GA4 có `ep.place=blog-test`.

### Bước 2 · Gắn cửa cho mọi trang bằng `content_group` (Claude)

<span class="chip chip--done">Xong · deploy 2026-11-08 · commit `321a43e` trên `main`</span>

Đã thử trên bản build production ở máy: 11 trang đại diện ra đúng cửa, request `page_view` gửi lên GA4 có `ep.content_group`. Thêm `/app-category-tier-list` (trang mới) vào cửa `tool`. Code: `lib/ga.js` + `pages/_app.jsx`.
Trên shotmatic.app sau deploy: `/blog/is-my-app-idea-good` gửi `page_view` với `content_group=blog`; bấm link Idea Checker trong bài gửi `nav_click` `blog → tool`, `place=article` (lượt thử này nằm trong số GA4).

- **Là gì:** `content_group` là chiều có sẵn của GA4. Gửi kèm `page_view` thì mọi báo cáo trang đều chia được theo cửa, không cần đăng ký thêm gì.
- **Sửa:** trong `pages/_app.jsx`, thêm 1 hàm đổi đường dẫn thành tên cửa theo danh sách ở trên, rồi đưa vào
  `gtag('config', GA_ID, { content_group: ... })`. Riêng `/` có `#download` thì là `download`.
- **Kiểm tra:** mở 5 trang đại diện, mỗi trang xem request `collect` có `ep.content_group` đúng cửa.

### Bước 3 · Đếm lượt đi từ cửa này sang cửa khác bằng 1 event `nav_click` (Claude)

<span class="chip chip--done">Xong · deploy 2026-11-08 · commit `321a43e` trên `main`</span>

Đã thử bằng cú bấm thật: menu trang chủ → Blog (`from=product`, `to=blog`, `place=nav`), dòng routes → Idea Checker (`place=routes`), footer → Guide (`place=footer`), link trong bài → Idea Checker (`from=blog`, `to=tool`, `place=article`), menu scorecard → Blog (`from=tool`). Không gửi khi bấm `#faq`, bấm bài khác trong blog, hay bấm Download (nút này vẫn chỉ gửi `download_click`).

Ghi chú phụ: nút Download trên menu của trang Guide đang ghi `place=blog_nav` vì Guide dùng chung khung với Blog. Không sai số cửa (đã có `content_group`), để Bước 4 sửa nếu cần.

- **Là gì:** 1 event duy nhất thay cho việc gắn `onClick` vào từng link. Một bộ nghe click chung trong `_app.jsx` bắt mọi thẻ `<a>`
  trỏ về trang trong site; nếu cửa đích khác cửa hiện tại thì gửi `nav_click`.
- **Tham số:**
  `from` (cửa hiện tại) · `to` (cửa đích) · `place` (vị trí link: `nav`, `menu_mobile`, `footer`, `hero`, `routes`, `article`, `list`, `guide_index`, `related`, lấy từ `data-place` gần nhất hoặc thẻ `nav`/`footer` bao quanh) · `link` (đường dẫn đích, bỏ query).
- **Bỏ qua:** link neo trong cùng trang (`#how`, `#faq`) và link ra ngoài site. Nút Download đã có `download_click` nên không bắn trùng.
- **Gắn `data-place`:** chỉ thêm ở các chỗ cần phân biệt mà thẻ bao quanh không nói rõ, ví dụ dòng "Every feature, step by step · App Idea Checker" ở trang chủ (`routes`) và thẻ bài trong danh sách blog (`list`).
- **Ví dụ đọc số:** `nav_click` với `from=blog`, `to=tool` = khách đọc bài rồi bấm sang thử free tool.

### Bước 4 · Đếm hành động trong từng cửa (Claude)

<span class="chip chip--done">Xong · deploy 2026-11-08 · commit `979fe16` trên `main`</span>

Đã thử trên bản build production ở máy, bấm và cuộn thật:

- `blog_open`: từ `/blog` ra `place=latest`, từ `/blog/all` ra `all`, từ trang chủ đề ASO ra `topic:aso`.
- `guide_open`: từ `/features` ra `place=guide_index`, từ "Related guides" ra `related`, từ nút Trước/Sau ra `pager`.
- `blog_read`: chưa bắn ở 72% phần chữ, bắn ở 75% (cuộn tới y≈1700 trên bài `is-my-app-idea-good`), cuộn tiếp không bắn lại. Phần FAQ và nguồn không tính vào độ dài bài.
- `tool_read` (scorecard): bắn 1 lần khi khối "Decide" hiện trên màn hình, cuộn lên xuống không lặp.
- `pricing_view`: phiên mở ở `/blog`, sang trang chủ bấm Pricing ra `from=blog`, `page=product`.
- Nút Download trên menu trang Guide giờ ghi `place=guide_nav` (trước là `blog_nav`), trang Idea Checker ghi `tool_nav`.
- Trên shotmatic.app sau deploy: `/features` gửi `page_view` với `content_group=guide`, bấm guide đầu tiên ra `guide_open` `place=guide_index`, nút Download ra `place=guide_nav` (lượt thử này nằm trong số GA4).

**Khác plan:** `/scorecard` chỉ là checklist để đọc, không có ô nào để tick, nên không có "lần tick đầu". Thay bằng event riêng `tool_read`, không gộp vào `tool_run`, để `tool_run` (key event) chỉ đếm lượt chạy tool thật.

Chỉ thêm những event trả lời được câu hỏi "khách có làm việc họ vào để làm không":

- **`blog_read`** khi khách cuộn tới 75% bài (`/blog/<slug>`), tham số `slug`, `topic`. Mỗi bài mỗi phiên chỉ gửi 1 lần.
  Cuộn 90% có sẵn của GA4 tính cả trang danh sách và hay bị trượt vì phần FAQ, nguồn dài ở cuối bài, nên dùng mốc riêng.
- **`blog_open`** khi bấm 1 bài từ `/blog`, `/blog/all`, trang chủ đề, tham số `place` (`latest`, `all`, `topic:<tên>`), `to` (slug).
- **`guide_open`** khi bấm 1 guide từ `/features` hoặc "Related guides", tham số `to` (slug), `place`.
- ~~**`tool_run`** cho `/scorecard` khi khách tick mục đầu tiên~~ → đã làm thành **`tool_read`** `{tool: 'scorecard'}` khi khối "Decide" hiện trên màn hình (xem ghi chú ở trên).
- **`pricing_view`** khi khối giá `#buy` trên trang chủ hiện trên màn hình, tham số `from` (cửa vào của phiên). Cho biết bao nhiêu người đi tới tận giá.

Gom tất cả về 1 hàm `track()` sẵn có trong `components/landing-kit/kit.jsx`. Không thêm thư viện.

### Bước 5 · Cài đặt trong GA4 Admin (Bạn)

Làm một lần, khoảng 10 phút. Không làm bước này thì tham số vẫn được gửi nhưng không hiện trong báo cáo.

- [ ] **Admin → Custom definitions → Create custom dimension**, phạm vi *Event*, tạo 8 chiều: `place`, `from`, `to`, `link`, `page`, `tool`, `slug`, `topic`
- [ ] **Admin → Events → Mark as key event:** `download`, `tool_run`, `generate_lead`, `checkout_click`
- [ ] **Admin → Data retention:** đặt *14 months*
- [ ] Tạo kênh `AI` như trong [mục 2 · Google Analytics](ga4.md)
- [ ] Thêm email service account vào property, quyền Viewer, để Claude đọc số qua MCP

### Bước 6 · Dựng 3 báo cáo để đọc mỗi tuần (Claude dựng, Bạn xem)

- **Khách vào để làm gì:** Explore → Free form, hàng = *Landing page content group*, cột số = Sessions, Key events (`download`), Session key event rate.
  Đọc: cửa nào nhiều phiên nhất, cửa nào ra `download` nhiều nhất trên 100 phiên.
- **Từ cửa vào tới lượt tải:** Explore → Funnel, 4 bước mở (open funnel): `session_start` → `nav_click` hoặc `page_view` bất kỳ → `download_click` → `download`, chia theo *Landing page content group*.
  Đọc: cửa nào rơi nhiều nhất ở bước hộp email (`download_click` → `download`).
- **Bài và tool nào ra lượt tải:** Explore → Free form, lọc event `download_click` và `download`, hàng = `place`.
  Đọc: top 10 bài theo `place=blog-*` và `place=blog:*`, đủ để quyết bài nào nên viết tiếp cùng chủ đề.

## Kiểm tra trước khi đẩy

- [ ] Chạy site ở máy (`shotmatic-site`, cổng 3220), mở từng cửa, xem request `https://www.google-analytics.com/g/collect` có đúng `en=` (tên event) và tham số
- [ ] Bật GA4 **DebugView** bằng `?debug_mode=1` hoặc extension Google Analytics Debugger, đi 1 vòng: blog → bấm sang tool → chạy tool → bấm Download → nhập email
- [ ] Không event nào gửi 2 lần cho 1 cú bấm
- [ ] Không gửi email hay chữ khách gõ vào ô tìm kiếm lên GA4 (chỉ gửi `country`, `verdict` như hiện nay)
- [ ] 24 giờ sau deploy, xem GA4 → Realtime và Events có đủ tên event mới

## Thứ tự và công

1. **Bước 1** (lỗ `ref`): nhỏ, làm ngay, vì mỗi ngày chậm là mất số bài nào ra lượt tải.
2. **Bước 2 + 3** (cửa + `nav_click`): 1 lần sửa `_app.jsx`, cộng vài thẻ `data-place`.
3. **Bước 4** (hành động trong cửa): 5 event, mỗi event vài dòng.
4. **Bước 5** (Admin): Bạn làm song song, không cần chờ code.
5. **Bước 6** (báo cáo): dựng khi đã có ít nhất 7 ngày số.

Làm trên 1 nhánh mới từ `origin/main` của `nvminhtu/shotmatic`, 1 PR, tách commit theo bước.

## Những gì plan này không đo được

- **Khách tải xong có mở app không.** Đó là số trong app Mac, không phải trên web.
- **Đơn PRO.** Mua qua Lemon Squeezy, chưa nối về GA4. Tạm ghi số đơn tay mỗi tuần như [mục 2](ga4.md) đã ghi.
- **Khách chặn quảng cáo.** Trình chặn quảng cáo chặn luôn GA4, nên số luôn thấp hơn thực tế. So xu hướng, không so số tuyệt đối với số tải trên GitHub.

## Liên quan

[2 · Google Analytics](ga4.md) · [Audit bán hàng 2026-11-07](audit-2026-11-07.md) · [Plan dựng lại trang Blog](plan-blog-hub-2026-11-07.md)
