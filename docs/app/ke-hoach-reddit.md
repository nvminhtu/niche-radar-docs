# Plan Reddit: chia sẻ hành trình làm ShotMatic, từ A tới Z (2026-11-01)

> Tu đăng, Claude soạn. Bài là **nhật ký hành trình** (build in public), không phải quảng cáo: kể đã làm gì, học được gì,
> số thật bao nhiêu. Không có link trong bài; ai hỏi thì trả lời bằng comment (mẫu ở [Kho câu trả lời](#kho-cau-tra-loi)).
> Nội dung bài để nguyên **tiếng Anh** vì đăng ở sub tiếng Anh; phần hướng dẫn bằng tiếng Việt.
> Đi cùng [Kế hoạch bán ShotMatic](ke-hoach-ban-shotmatic.md): bài 1–3 thuộc tầng 1, bài 4–8 thuộc tầng 2.

<span class="chip chip--todo">Plan 2026-11-01 · chưa đăng bài nào</span>

<div class="box box--goal" markdown>
**Mục tiêu:** 8 bài trong ~6 tuần, mỗi bài có ích cho người đọc dù họ không bao giờ mua. Người tò mò tự hỏi
"tool gì vậy" → lúc đó mới đưa link trong comment.

**Không làm:** đăng bài mời mua, dán link vào bài, nhờ người upvote, dùng tài khoản phụ, đăng cùng 1 bài ở nhiều sub
trong cùng ngày, bịa số.
</div>

## Số thật lúc lập plan (2026-11-01)

| Chỉ số | Số | Nguồn |
|---|---|---|
| Lượt tải .dmg | **9** (v1.0.0, từ 29/10) | GitHub API, release của niche-radar-docs |
| Đơn PRO | **0** | Lemon Squeezy (mới mở bán 2026-11-01) |
| Bài Reddit đã đăng | **0** | — |
| Karma, tuổi tài khoản Reddit của Tu | `chưa đo` | Tu xem ở trang profile |
| Luật từng sub | `chưa kiểm` — trang rules của Reddit không tải được từ máy Claude (403) ngày 2026-11-01 | Tu đọc sidebar trước khi đăng |

Chỗ nào trong bài ghi `{...}` là số phải điền bằng số đo được trước khi đăng. Không có số thì bỏ câu đó, không đoán.

## Luật Reddit phải giữ

Luật chung của Reddit (áp dụng mọi sub):

1. **Một người, một tài khoản.** Không dùng tài khoản phụ để comment / upvote bài mình, không nhờ bạn bè vào upvote
   (Reddit coi là gian lận vote, có thể bị khoá cả tài khoản lẫn domain).
2. **Nói rõ mình là người làm.** Mỗi bài, mỗi comment nhắc tới ShotMatic đều có câu kiểu "I'm the solo dev of it".
3. **Tỉ lệ cho / lấy.** Đa số hoạt động của tài khoản phải là comment giúp người khác, không phải nói về sản phẩm mình.
   Giữ khoảng **≥ 9 comment giúp người / 1 lần nhắc ShotMatic**.
4. **Không đăng chéo hàng loạt.** Một bài chỉ đăng 1 sub; bài tiếp theo ở sub khác phải viết lại góc khác, cách ≥ 2 ngày.
5. **Domain sạch.** Không link rút gọn, không UTM dài trong bài; link chỉ nằm trong comment trả lời người hỏi,
   dùng `shotmatic.app/?ref=reddit`.
6. **Không xoá rồi đăng lại** bài bị ít vote. Bài bị mod gỡ → nhắn mod hỏi lý do, không đăng lại y nguyên.

Luật riêng từng sub thường gặp (Tu **đọc sidebar + bài ghim** của sub đó trước mỗi lần đăng, ghi ngày đã kiểm vào bảng dưới):

- Ngày / thread riêng cho tự quảng cáo (vd. "Self-promotion Saturday", "Show-off thread").
- Yêu cầu flair (Build in public · Feedback · Showcase…).
- Ngưỡng karma / tuổi tài khoản tối thiểu để đăng bài.
- Có cho link trong bài không; có bắt buộc ghi "I made this" không.

## Chọn sub

| Sub | Hợp bài kiểu gì | Luật đã kiểm |
|---|---|---|
| r/SideProject | hành trình, ra mắt, ảnh chụp app | `chưa kiểm` |
| r/indiehackers | số thật, bài học, thất bại | `chưa kiểm` |
| r/ClaudeCode | làm app bằng Claude Code, quy trình, MCP | `chưa kiểm` |
| r/microsaas | số tải / đơn, giá | `chưa kiểm` |
| r/iOSProgramming · r/androiddev | chỉ bài kỹ thuật / dữ liệu store, không nhắc mua | `chưa kiểm` |
| r/macapps | chỉ khi app ổn định + có bản cập nhật, thường có luật riêng cho dev tự giới thiệu | `chưa kiểm` |

## Tuần 0 — Nuôi tài khoản (7 ngày trước bài 1)

- [ ] Mỗi ngày 3–5 comment **có ích** ở các sub trên: trả lời thread "what app should I build", "how do I validate",
  "ASO keyword help" bằng kinh nghiệm thật — **không nhắc ShotMatic**
- [ ] Join và đọc 1 tuần bài top của mỗi sub để biết giọng, độ dài, kiểu tiêu đề được upvote
- [ ] Ghi karma + tuổi tài khoản vào bảng số ở trên

## Lịch đăng

| # | Tuần | Sub | Góc | Điều kiện đăng |
|---|---|---|---|---|
| 1 | 1 | r/SideProject | Vì sao làm: chọn sai niche trước đây | xong tuần 0 |
| 2 | 1–2 | r/ClaudeCode | Làm cả app Mac bằng Claude Code | cách bài 1 ≥ 2 ngày |
| 3 | 2 | r/indiehackers | Mở bán: 9 lượt tải, 0 đơn, đang làm gì | có số tải mới |
| 4 | 3 | r/SideProject | Dữ liệu: đọc review 1★ học được gì | đã chạy ≥ 3 niche thật |
| 5 | 3–4 | r/ClaudeCode | Brief / spec cho AI: từ dữ liệu → prompt | có ví dụ thật xuất từ app |
| 6 | 4 | r/indiehackers | Bán tay 14 ngày: chào N người, ra M đơn | hết ngày 14 tầng 1 |
| 7 | 5 | r/microsaas | Sai lầm: cái không hiệu quả | có ≥ 2 kênh đã thử |
| 8 | 6 | r/SideProject | Tháng 1 nhìn lại: số tải, đơn, sửa gì | có số tháng đầu |

Giờ đăng: sáng thứ 3–5 giờ Mỹ (khoảng 20–22h giờ Việt Nam). Giờ "tốt nhất" là `chưa đo` — ghi lại giờ đăng + điểm
sau 24h của từng bài để tự rút ra.

## Bài viết

### Bài 1 · r/SideProject · Vì sao làm

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

Where I am today:
- First public build went out on Oct 29
- {9} downloads so far, 0 paying users (I only opened sales today)
- Biggest lesson so far: the review complaints were more useful than the keyword volumes

I'll keep posting what I learn, including the numbers that look bad.

Question for you: how do you check an idea before building? Gut feeling, keyword
tools, posting a landing page first?
```

**Lưu ý:** không có tên app, không link trong bài. Ai hỏi tên / link → reply mẫu R1.

### Bài 2 · r/ClaudeCode · Làm app bằng Claude Code

**Title:** What I learned building a full Mac app with Claude Code as a solo dev (web UI + Tauri shell + MCP)

```text
I've been building a niche-research app mostly with Claude Code. Sharing what worked
and what didn't, since a lot of posts here are about small scripts.

Setup:
- All UI + API in one web/ folder (Vite + React + Hono + SQLite)
- The Mac app is just a Tauri shell around the same web code, so I never write UI twice
- A CLAUDE.md with hard rules: every page must work from 960px wide, no made-up numbers,
  tests next to new code, one check command must pass before "done"

What worked:
1. Hard rules in CLAUDE.md beat long prompts. "Never invent numbers, write 'not measured'"
   saved me from a lot of confident nonsense.
2. One `npm run check` that runs lint + types + tests. Claude runs it before saying done.
3. A read-only MCP server so Claude Code can query my own research data
   instead of me pasting tables.

What didn't:
- {Tu điền 1-2 chuyện thật: lỗi layout, bug khó, chỗ Claude làm sai}

Happy to share the CLAUDE.md structure if useful.
```

**Lưu ý:** sub này về Claude Code, nên trọng tâm là quy trình. Chỉ nhắc ShotMatic khi có người hỏi app gì (R1).
Nếu có người xin CLAUDE.md → đưa **bản rút gọn bỏ đường dẫn máy và tên nội bộ**, Claude soạn.

### Bài 3 · r/indiehackers · Mở bán, số thật

**Điều kiện:** checkout chạy được (tầng 0 xong) và có số tải mới đo bằng GitHub API.

**Title:** Opened sales for my first paid app: {N} downloads, 0 sales. Here's my plan for the next 14 days

```text
Honest numbers, since I learn more from these posts than from the success ones.

- Mac app for checking an app niche before building (Play Store, App Store, Trends data)
- Public since Oct 29, sales opened Nov 1
- {N} downloads, 0 sales as of {ngày}
- Price: $39.99 one-time, free tier with 15 lookups

My guess at why 0: nobody knows it exists, and "a niche research tool" is not something
people wake up wanting. What they want is "is my idea worth building?"

So for the next 14 days I'm not adding features. I'm going to:
1. Email each person who downloaded and ask what idea they were checking
2. Run the research for people by hand and send them the report
3. Write down every objection word for word

I'll post the results either way. If you've sold a dev tool before:
what got you from 0 to your first 10 customers?
```

### Bài 4 · r/SideProject · Đọc review 1★

**Điều kiện:** đã chạy ≥ 3 niche thật trong app; mọi số lấy từ dữ liệu đã lưu, ghi ngày tra.

**Title:** I read {N} one-star reviews across {M} niches. The same 3 complaints show up everywhere

```text
While testing my niche tool I ended up reading a lot of 1-2 star reviews.
Sharing the patterns because they're useful whether or not you use any tool.

Data: {N} reviews from {M} competing apps in {niche list}, pulled {ngày}.

1. {lời chê 1} — {x}% of complaints. Example (paraphrased): "..."
2. {lời chê 2} — {y}%
3. {lời chê 3} — {z}%

What this means if you're building in these niches: {1-2 câu rút ra}

Method: grouped complaints by topic, counted per app, ignored reviews under 5 words.
```

**Lưu ý:** trích review thì viết lại ý (paraphrase), không dán tên người review.

### Bài 5 · r/ClaudeCode · Từ dữ liệu → brief cho AI

**Điều kiện:** có 1 brief.md / spec.md thật xuất từ app (niche của chính Tu, không phải của khách).

**Title:** Instead of "build me an app like X", I give Claude Code a spec built from real store data. Here's the template

```text
Most "vibe coded" apps I see fail on the idea, not the code. So before I let Claude Code
write anything, I generate a spec from research data:

- Target keywords + how many competitors each has
- Top complaints from 1-2 star reviews of those competitors (= features to get right)
- What competitors already do well (= table stakes)
- Trend direction for the niche

Template (trimmed):
{dán khung brief, bỏ số nhạy cảm}

The difference I noticed: {Tu điền chuyện thật}
```

### Bài 6 · r/indiehackers · 14 ngày bán tay

**Điều kiện:** hết luật dừng ngày 14 của [tầng 1](ke-hoach-ban-shotmatic.md#tang-1-lam-tay-ban-tung-nguoi-ngay-114-muc-tieu-10-on). Đăng **dù số xấu**.

**Title:** 14 days of selling by hand: messaged {N} people, sent {R} free reports, got {M} sales

```text
Two weeks ago I posted 0 sales. Here's what happened.

What I did:
- Emailed {9} people who downloaded: {x} replied
- Sent {R} free niche reports to people who asked
- Messaged {N} people who posted "what app should I build": {y} replied

Results: {M} sales, {€} revenue.

What people actually said (word for word):
- "{câu khách 1}"
- "{câu khách 2}"
- "{câu khách 3}"

What I'm changing because of it: {1-3 điều}
```

### Bài 7 · r/microsaas · Cái không hiệu quả

**Title:** Things that didn't work in my first month selling a $39.99 Mac app

```text
{3-5 việc đã thử mà ra 0 đơn, mỗi việc 1-2 câu: đã làm gì, số bao nhiêu, vì sao nghĩ là không ăn}

What did work: {1 việc, kèm số}
```

### Bài 8 · r/SideProject · Tháng 1 nhìn lại

**Title:** One month after launching my side project: {N} downloads, {M} customers, and what I'd do differently

```text
Monthly recap, same format as before:
- Downloads: {N} (was 9 at launch)
- Paying customers: {M}
- Revenue: ${X}
- Biggest change I made because of feedback: {...}
- What I'd tell myself a month ago: {...}

Next month: {1-2 việc}
```

## Comment đầu tiên của chủ bài

Một số sub cho dev tự comment link ngay dưới bài, một số không. **Chỉ làm nếu sidebar cho phép**; không thì đợi có người hỏi.

```text
Since a few people usually ask: the app is ShotMatic (shotmatic.app/?ref=reddit).
I'm the solo dev. Free tier is 15 lookups, Mac only for now. Happy to answer anything.
```

## Kho câu trả lời

Trả lời trong 2 giờ đầu sau khi đăng. Viết lại theo câu người ta hỏi, không dán y nguyên mẫu (dán giống nhau ở nhiều chỗ dễ bị coi là spam).

**R1 · "What's the app / link?"**
```text
It's called ShotMatic, I'm the solo dev: shotmatic.app/?ref=reddit
Mac only for now, free tier is 15 lookups so you can try it on your own idea first.
```

**R2 · "How much?"**
```text
$39.99 one-time, works on 2 Macs, 14-day refund. Free tier has 15 lookups.
No subscription because the data is fetched from your own machine, so I have no server cost per user.
```

**R3 · "Windows / Linux?"**
```text
Mac only right now. Windows is planned but I don't have a date I can promise yet.
```

**R4 · "How is this different from AppFigures / Sensor Tower / AppTweak?"**
```text
Those are great for tracking downloads and revenue estimates, and much deeper than mine.
Mine is narrower: before you build, it opens a niche into the keywords people type, counts
competitors per keyword, and groups 1-2 star complaints. It runs locally, one-time price.
If you already pay for one of those, you probably don't need this.
```

**R5 · "Where does the data come from? Is that allowed?"**
```text
Public store listings and reviews, Google Trends, and a few other public sources, fetched
from your own machine at normal rates. Nothing goes through my server. Numbers it can't
measure are shown as "not measured" instead of an estimate.
```

**R6 · "Does it use AI? Does my data go anywhere?"**
```text
The research itself is plain data, no AI needed. If you want, it can hand the results to
your own Claude Code / Codex (your account, your machine). Your data stays in a SQLite file
on your Mac.
```

**R7 · "Can you check my idea?"**
```text
Sure, tell me the idea in a sentence and the country/store you care about.
I'll run it and reply with the competitor count, top complaints and trend.
```
→ Chạy thật trong app, trả lời **bằng số đã chạy** + ngày tra, không đoán. Đây là đường vào [tầng 1.2](ke-hoach-ban-shotmatic.md#12-gui-y-tuong-nhan-bao-cao-mien-phi-20-ban-ngay-214).

**R8 · Chê / nói "just another tool"**
```text
Fair point. What would make a tool like this actually useful for you?
```
→ Không cãi. Ghi câu đó vào file voice-of-customer.

## Sau mỗi bài

- [ ] Ở lại trả lời 2 giờ đầu, trả lời mọi comment trong 24 giờ
- [ ] Sau 24h ghi: upvote, số comment, số người hỏi link, lượt vào `ref=reddit` (GA4), lượt tải, đơn `ref=reddit`
- [ ] Câu hỏi lặp lại ≥ 3 lần → thêm vào Kho câu trả lời hoặc sửa landing

| # | Ngày đăng | Sub | Upvote 24h | Comment | Hỏi link | Tải | Đơn |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |
| 6 | | | | | | | |
| 7 | | | | | | | |
| 8 | | | | | | | |

## Luật dừng

- **Bài bị mod gỡ:** đọc lý do, sửa theo luật sub đó, không đăng lại ở sub đó trong 2 tuần.
- **2 bài liền ở một sub dưới 5 upvote:** bỏ sub đó, dồn sang sub khác.
- **Nhiều người hỏi "check my idea" hơn hỏi link:** giá trị nằm ở báo cáo → đẩy mạnh R7, báo cho [tầng 1](ke-hoach-ban-shotmatic.md).
- **Bài số thật (3, 6, 8) chạy tốt hơn bài quy trình:** đổi lịch sang nhiều bài số thật hơn.

## Việc chỉ Tu làm được

Claude không đăng nhập Reddit, không đăng bài / comment thay.

1. Đọc sidebar từng sub và điền cột "Luật đã kiểm".
2. Đăng bài, trả lời comment, nhắn mod khi cần.
3. Điền số vào `{...}` trước khi đăng và bảng đo sau mỗi bài — hoặc gửi số cho Claude điền.
