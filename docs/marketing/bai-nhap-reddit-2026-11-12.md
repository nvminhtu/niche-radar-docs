# 6.1 · Bài nháp Reddit + Show HN (2026-11-12)

> Các bài tiếng Anh đã soạn sẵn để kéo người làm startup / indie dev ở US về shotmatic.app. **Bạn tự đăng, Claude soạn.**
> Thuộc Tầng 2 và Tầng 3 của [Plan phân phối ngoài site](plan-phan-phoi-ngoai-site-2026-11-11.md). Luật đăng giữ nguyên
> như [Plan Reddit 8 bài](../app/ke-hoach-reddit.md).

<span class="chip chip--todo">Nháp · 2026-11-12 · chưa đăng bài nào</span>

<div class="box box--goal" markdown>
**Nó là gì:** 2 bài nháp + 1 câu trả lời mẫu, để copy lên Reddit và Hacker News.

**Làm gì:** điền các chỗ `{...}` bằng số thật, soát lại, rồi tự đăng đúng giờ và đúng sub.

**Target:** bài Reddit số 1 lên r/SideProject sau tuần nuôi tài khoản. Bài Show HN chỉ đăng khi mở Tầng 3 (sau lần đo
tuần 8).

**Không làm:** dán link vào bài Reddit, nhờ upvote, dùng tài khoản phụ, đăng cùng một bài ở nhiều sub, bịa số.
</div>

## Số dùng trong bài

- **Lượt tải .dmg: 22.** Đo 2026-11-12 bằng GitHub API: 11 lượt bản 1.0.0, 7 lượt bản 1.1.0, 4 lượt bản 1.1.1.
- **Bản đầu ra ngày 2026-10-29**, sau đó có 2 bản cập nhật (1.1.0 ngày 2026-11-01, 1.1.1 ngày 2026-11-10).
- **Số đơn PRO:** `chưa đo`. Bạn xem ở Lemon Squeezy rồi điền vào `{N}`. Mở bán từ 2026-11-01.
- **Free tier 15 lượt tra:** lấy từ plan ngày 2026-11-01, `chưa kiểm lại`.

Đo lại số tải ngay trước ngày đăng, vì số này đổi mỗi ngày.

## Vì sao không viết bài theo thành phố

Ghi lại để khỏi bàn lại: bài kiểu "keyword research tool for indie dev in Denver" hay "top startups in New York" **không
đáng làm**. Đây là đánh giá theo kinh nghiệm SEO, chưa đo số cho từng keyword.

- **Không ai gõ tên thành phố khi tìm phần mềm.** Tên thành phố chỉ đi với dịch vụ tại chỗ.
- **Nhiều trang chỉ khác tên thành phố** bị Google coi là doorway pages, có thể kéo cả domain xuống.
- **Bài "top startups in [city]" kéo sai người:** người tìm việc, nhà đầu tư, sales. Họ không cần tool research app.
- **Một bài tiếng Anh xếp hạng ở Google US thì mọi thành phố ở Mỹ đều thấy.** Không cần chia nhỏ hơn cấp quốc gia.

Thay vào đó: viết theo nỗi đau, có mặt ở cộng đồng (Reddit, Indie Hackers, Hacker News), và dẫn về trang tool miễn phí.

## Bài Reddit số 1 · r/SideProject · Vì sao làm

Bản cập nhật của Bài 1 trong [Plan Reddit 8 bài](../app/ke-hoach-reddit.md), thay số ngày 2026-11-01 bằng số ngày
2026-11-12.

**Flair:** Build in public (hoặc flair gần nhất sub có)

**Title:** I kept building apps nobody searched for, so I built a tool to check the niche before I write code

```text
Hi r/SideProject, solo dev here.

My pattern for years: get an idea, spend weeks building it, ship it, then find out
nobody types those words into the App Store, or there are already 40 apps doing it.

So this time I flipped the order. Before writing any app code, I wanted answers to:
- What do people actually type when they search for this? (the keyword tree, not my guess)
- How many apps already compete on each keyword?
- What do users complain about in 1-2 star reviews of those apps?
- Is interest going up or down (Google Trends)?

I ended up building a small Mac app that does this locally: it pulls Google Play,
App Store, Google Trends and a few other public sources, saves everything to a SQLite
file on my machine, and scores where the gaps are.

Where I am two weeks in:
- First public build went out on Oct 29, two updates since
- 22 downloads so far, {N} paying users (sales opened Nov 1)
- Biggest lesson so far: the review complaints were more useful than the keyword volumes

I'll keep posting what I learn, including the numbers that look bad.

Question for you: how do you check an idea before building? Gut feeling, keyword
tools, posting a landing page first?
```

**Lưu ý:** không có tên app, không link trong bài. Ai hỏi tên hoặc link thì trả lời bằng mẫu dưới.

## Câu trả lời khi có người hỏi tên hoặc link

```text
It's called ShotMatic, I'm the solo dev: shotmatic.app/?ref=reddit
Mac only for now, free tier is 15 lookups so you can try it on your own idea first.
```

## Bài Show HN · để sẵn cho Tầng 3

Chưa đăng. Hacker News chỉ hợp khi có thứ người ta thử được ngay, nên bài dẫn về tool miễn phí, không dẫn về trang
bán hàng.

**Title:** Show HN: Free app idea checker – test an idea against both app stores

**URL:** `https://shotmatic.app/app-idea-checker?ref=hn`

**Comment đầu tiên** (tự đăng ngay sau khi gửi bài):

```text
Hi HN, solo dev here.

I've shipped several apps that nobody searched for. Each time I only found out after
the build. This page is the check I wish I had run first.

You type an app idea. It looks up the App Store and Google Play for that phrase and
tells you whether the space looks open, risky or crowded, with the apps it found so
you can judge for yourself.

What it does not do: it has no search volume numbers. Apple and Google don't publish
them, and I didn't want to show estimates dressed up as data. The verdict is based on
what is already ranking, not on demand.

Limits: {số lượt tra miễn phí mỗi ngày}, {có cần đăng ký hay không}.

The fuller version is a Mac app that runs locally and stores everything in a SQLite
file on your machine (keyword tree, 1-2 star review complaints, Google Trends). It is
paid, one-time. The checker on this page is free.

I'd like to know where the verdict is wrong. If you try an idea you know well and the
result looks off, please tell me the phrase.
```

**Lưu ý:** đoạn mô tả App Idea Checker viết theo ghi chú ở [Free tool](free-tool.md), `chưa kiểm` với trang thật. Bạn
soát 3 mức kết quả (open / risky / crowded) và 2 chỗ `{...}` trước khi đăng.

## Việc trước khi đăng

- [ ] **(Bạn)** Điền `{N}` số đơn PRO từ Lemon Squeezy. Vẫn là 0 thì ghi 0.
- [ ] **(Bạn)** Kiểm lại "15 lookups" trong câu trả lời link.
- [ ] **(Bạn)** Soát đoạn mô tả App Idea Checker và điền 2 chỗ `{...}` trong bài Show HN.
- [ ] **(Bạn)** Đọc sidebar và bài ghim của r/SideProject: flair, ngưỡng karma, luật tự giới thiệu.
- [ ] **(Bạn)** Xong tuần nuôi tài khoản: mỗi ngày 3–5 comment có ích, chưa nhắc sản phẩm.
- [ ] Đo lại số tải bằng GitHub API ngay trước ngày đăng, sửa con số 22 nếu đã đổi.

## Giờ đăng và cách đo

- **Giờ đăng:** thứ 3–5, 20:00–22:00 giờ Việt Nam (buổi sáng giờ miền Đông US). Giờ tốt nhất là `chưa đo`.
- **Sau 24 giờ:** ghi điểm, số comment và giờ đăng của bài vào trang này.
- **Trong GA4:** lọc quốc gia United States, xem lượt vào và event `download_click` có `ref=reddit` hoặc `ref=hn`.
- **Bỏ kênh** nào sau 2–3 lần thử không ra lượt tải.

## Nhật ký đăng

Chưa có bài nào được đăng.

## Liên quan

[Plan phân phối ngoài site](plan-phan-phoi-ngoai-site-2026-11-11.md) · [Plan Reddit 8 bài](../app/ke-hoach-reddit.md) ·
[Reddit Q&A](reddit.md) · [Free tool](free-tool.md)
