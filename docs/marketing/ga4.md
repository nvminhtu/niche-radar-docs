# 2 · Google Analytics

> Search Console cho biết chuyện xảy ra **trước** khi khách bấm vào site. Google Analytics (GA4) cho biết chuyện xảy ra
> **sau** đó: khách từ đâu tới, đọc gì, có tải app không.

<span class="chip chip--todo">Chưa làm · chờ khoá service account · số hiện tại: chưa đo</span>

<div class="box box--goal" markdown>
**Target**

- **Tháng 1:** đo đủ đường đi từ lượt vào tới đơn PRO · tách riêng được khách từ AI · biết tỉ lệ chuyển đổi thật của từng bước
- **Tháng 3:** biết 5 bài hoặc trang nào ra nhiều lượt tải nhất · trả lời được kênh nào đáng làm tiếp
- **Tháng 6:** 500 active user / 28 ngày · 20 lượt tải có nguồn rõ · 50 khách từ AI (đích tự đặt)
- **Tháng 12:** 2.000 active user / 28 ngày, cộng tất cả các kênh (đích đã đặt từ 02/11, vẫn là giả định và khá khó)

SEO một mình chưa đủ 2.000. Target ở [mục 1](google-search-console.md) mới chỉ khoảng 600 click ở tháng 12.
</div>

## Nó là gì

GA4 đếm người và hành động trên site. Với ShotMatic chỉ cần đọc 4 thứ:

- **Active user:** số người có tương tác. Xem theo 28 ngày cuộn, không cộng số từng ngày, vì người quay lại sẽ bị đếm nhiều lần.
- **Kênh (Channel):** Organic Search, Direct, Referral, Social.
- **Trang đích (Landing page):** trang đầu tiên khách vào. Đây là cách biết bài nào kéo được người.
- **Key event:** hành động có giá trị, ví dụ `download` và `tool_run`.

## Dùng nó có lợi gì

- **Biết bài nào ra tiền, không chỉ ra lượt xem.** Một bài 100 lượt xem ra 5 lượt tải tốt hơn bài 1.000 lượt xem ra 0.
- **Biết cửa nào rò.** Nhiều lượt vào mà ít tải thì lỗi ở trang. Nhiều tải mà không mua thì lỗi ở app hoặc giá.
- **Thấy khách từ AI.** Đây là cách chính để đo hiệu quả mục [GEO](geo.md).
- **Tránh làm tiếp kênh không ra gì.** Làm một mình thì không đủ sức làm mọi kênh.

## Làm gì để đo đúng

Plan chi tiết gắn event cho từng cửa vào (tải app, free tool, blog, guide): [2.1 · Plan gắn event GA4](plan-ga4-events-2026-11-07.md).

Đây là việc cài đặt, làm một lần.

- [ ] **(Bạn)** Đặt file khoá và thêm email service account vào property GA4, quyền Viewer
- [ ] **(Bạn)** Liên kết GA4 với Search Console, để xem từ khoá và hành vi trong cùng một nơi
- [ ] **(Bạn)** Đặt thời gian giữ dữ liệu lên mức cao nhất, vì mặc định chỉ 2 tháng, không đủ để so theo mùa
- [ ] **(Bạn)** Đánh dấu `download` và `tool_run` là key event
- [ ] **(Claude)** Kiểm tra `/download?ref=blog-<slug>` có vào GA4 không. Không có thì không biết bài nào ra lượt tải
- [ ] **(Claude)** Kiểm tra đơn PRO từ Lemon Squeezy có nối được về GA4 không. Không nối được thì ghi số đơn tay mỗi tuần

**Tạo kênh riêng cho AI.** GA4 không có sẵn kênh này, nên [khách từ ChatGPT rơi vào Referral](https://www.orbitmedia.com/blog/track-ai-traffic-ga4/).

- [ ] Vào Admin → Data display → Channel groups, tạo nhóm mới
- [ ] Thêm kênh `AI` khớp nguồn: `chatgpt.com`, `chat.openai.com`, `perplexity.ai`, `claude.ai`, `gemini.google.com`, `copilot.microsoft.com`
- [ ] Kéo kênh `AI` lên **trên** Referral, nếu không nó sẽ không khớp được lượt nào

Số này luôn thấp hơn thực tế: khách từ app điện thoại hoặc khách tự chép link sang trình duyệt thường bị tính là Direct. Vì vậy nên xem xu hướng, không xem số tuyệt đối.

## Đường đi cần đo

Mỗi bước là một con số, và mỗi bước chỉ đo được khi có event riêng:

1. Lượt vào site (`session`)
2. Vào trang tải hoặc chạy free tool (`page_view /download`, `tool_run`)
3. Bấm tải (`download`)
4. Mở app và làm research đầu tiên, nếu app có đo được
5. Mua PRO (số đơn trên Lemon Squeezy)

Tôi không tìm được chuẩn chuyển đổi đáng tin cho app Mac bán một lần, nên **không đặt target tỉ lệ khi chưa có số**. Sau 28 ngày, lấy số thật làm mốc rồi đặt đích cao hơn 20–30%.

## Việc mỗi tuần

- [ ] Ghi active user, kênh, top 10 trang đích, số `download`, số `tool_run`, số đơn
- [ ] Ghi riêng khách từ kênh `AI` và trang họ vào
- [ ] Nếu một trang có nhiều khách mà không ai tải, ghi lại để sửa lời mời tải

<div class="box box--example" markdown>
**Ví dụ · chiến dịch "AI kiểm ý tưởng app"**

Cần trả lời 3 câu sau 8 tuần:

- Bao nhiêu người vào `/app-idea-checker`, và bao nhiêu người chạy `tool_run`?
- Bao nhiêu lượt tải có `place=tool:idea-checker`?
- Khách từ kênh `AI` có vào trang này không?

Theo [Audit](audit-2026-11-07.md): dưới 20 lượt chạy sau 4 tuần thì xem lại tên và cách kéo khách trước khi làm tool thứ hai.
</div>

## Số đo mỗi 4 tuần

**2026-11-07 (mốc):** active user `chưa đo` · Organic `chưa đo` · kênh AI `chưa đo`. Số đo được từ nguồn khác: **9** lượt tải `.dmg` (GitHub API, 2026-11-07, lấy từ Audit).

## Liên quan

[1 · Google Search Console](google-search-console.md) · [5 · GEO](geo.md)
