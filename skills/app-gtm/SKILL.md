---
name: app-gtm
description: "Marketing từ số 0 cho indie (go-to-market, GTM) — dựng cả hệ thống tìm khách cho một sản phẩm khi chưa có người theo dõi, chưa có danh sách email, chưa có tiền quảng cáo: kiểm điểm xuất phát (landing, email, X, karma Reddit, GitHub, blog, doanh thu — số thật), định vị một câu có bằng chứng (học 3 indie cùng ngách qua /app-indie), dựng nền tảng sở hữu trước (landing + form email + link đo nguồn), chấm điểm kênh bằng ICE rồi chọn đúng 2 kênh chính + 1 kênh dài hạn (SEO), lịch 6 tuần theo chặng warmup → share → discuss → update → results, viết từng bài thành file marketing/<kênh>/NN-*.md đúng frontmatter Promo Desk (tab Campaign hiện ngay), bảng số mỗi tuần có nguồn, luật dừng/dồn sức. Ghi marketing/gtm.md, kiểm bằng scripts/check_gtm.py. Dùng cho app store lẫn app bán thẳng, tool dev, kit, web. Use when 'marketing từ số 0', 'chưa có ai biết app', 'không có follower', 'go to market', 'GTM', 'kế hoạch marketing bài bản', 'tìm khách đầu tiên', 'first 100 users', 'build in public', 'lên lịch đăng bài', 'campaign cho app', 'marketing cho indie', 'tự đi sale', 'bán tool cho dev', or when Promo Desk sends /app-gtm. Không đăng bài, không mua quảng cáo, không mua follower/upvote, không bịa số."
argument-hint: "<slug> [--refresh tuần N]"
user-invocable: true
---

# app-gtm — marketing từ số 0, làm như việc thật

Người làm indie thường làm ngược: code xong → đăng một bài → im lặng → kết luận "không ai cần". Skill này đi đúng chiều:
**có chỗ đứng (owned) → có người nghe (warm-up) → mới ra mắt (share) → giữ nhịp (discuss/SEO) → đọc số → dồn sức hoặc dừng.**

- Kết quả: `apps/<nhóm>/<slug>/marketing/gtm.md` (khuôn `templates/gtm.md`) + các file bài `marketing/<kênh>/NN-*.md`.
- Kiểm: `python3 scripts/check_gtm.py <slug>` tới 0 FAIL — kiểm cả gtm.md lẫn frontmatter từng file bài.
- Đọc: **[references/channels.md](references/channels.md)** (kênh nào hợp khi nào, công thức bài, nhịp tuần, luật dừng) ·
  mindset + giá + SEO + TrustMRR: [../app-indie/references/playbook.md](../app-indie/references/playbook.md).
- Promo Desk: skill này hiện trong menu `/` của khung Claude; file bài ghi ra hiện ngay ở tab **Campaign** (theo chặng, theo ngày),
  file trong `marketing/email/` hiện ở tab **Outreach**. Giọng Reddit: `/app-reddit`. Luật từng sub: lệnh `/rules`.

Quan hệ với `/app-marketing` (bước 12): bước 12 là **tuần ra mắt** của app store (landing, email, D-21 → D+7, `Launched: yes`).
`/app-gtm` là **cả hệ thống 6 tuần lặp lại**, chạy được trước khi có app trên store và sau ra mắt; nó dùng lại landing/email của bước 12 nếu đã có.

## Pha 0 — Điểm xuất phát (đo, không đoán)

Điền bảng `## Điểm xuất phát`: Landing · Form email (số người) · X (follower) · Reddit (karma) · GitHub (star) · Blog (số bài) ·
Doanh thu (verified/`chưa đo`) · Sản phẩm (live ở đâu, giá). Mỗi dòng có link hoặc số + ngày. Người dùng đọc số tài khoản của họ
cho Claude; Claude không đăng nhập. Số = 0 là bình thường — viết 0, đừng viết "chưa có gì" chung chung.

## Pha 1 — Định vị một câu (có bằng chứng)

1. Chạy `/app-indie <ngách>` nếu chưa có file `research/*-indie-*.md` cùng ngách — học 3 indie: khách ở đâu, giá, câu hero.
2. Viết 5 dòng: `Cho ai:` (một nhóm hẹp, gọi được tên chỗ họ tụ tập) · `Việc họ cần xong:` · `Họ đang dùng:` (cả "không làm gì") ·
   `Khác một câu:` (cái chỉ mình có) · `Bằng chứng:` (link review/thread/research — không có thì định vị là đoán).
3. Hỏi người dùng duyệt 5 dòng này **trước** khi viết bài nào. Sai định vị thì mọi bài sau đều phí.

## Pha 2 — Nền tảng sở hữu (xong trước bài share đầu tiên)

Kênh mượn (Reddit, X, HN) cho người xem một lần; nền tảng sở hữu giữ họ lại. Cần đủ 4 dòng:
- `Landing:` URL thật (oneclicktool.app / shotmatic.app / `make_site.py`; app Mac → `/app-mac-landing`).
- `Email form:` URL form (MailerLite / Buttondown / Kit, người dùng tự mở tài khoản) + mồi (lead magnet) một dòng.
- `Tracking:` mỗi bài một link đo nguồn — App Store: `?ct=<kênh>-<nơi>&pt=<mã>`; web: `?utm_source=<kênh>&utm_campaign=<slug>`.
- `Analytics:` nơi đọc số (GA4 qua MCP `google-analytics`, App Store Connect, Lemon Squeezy/Polar, TrustMRR).
Thiếu landing → bài share/discuss có link bị checker chặn (FAIL). Warm-up không cần link nên chạy song song được.

## Pha 3 — Chọn kênh bằng điểm (ICE), không bằng cảm giác

Bảng `## Chọn kênh`: mỗi kênh ứng viên từ references/channels.md chấm 1–5 cho **Impact** (khách đúng nhóm, đủ đông) ·
**Confidence** (có bằng chứng indie cùng ngách thắng ở đó — link) · **Ease** (mình làm đều được 6 tuần với sức hiện tại).
`Điểm = I × C × E`. Chọn **đúng 2 kênh `chính`** + **1 kênh `dài hạn`** (SEO/blog/GitHub — thứ tích luỹ) + tối đa 2 `phụ`.
Còn lại `bỏ` — viết lý do một dòng. Làm 2 kênh đều tay ăn hơn 6 kênh mỗi kênh một bài.

## Pha 4 — Lịch 6 tuần theo chặng

| Tuần | Chặng | Mục tiêu tuần |
|---|---|---|
| 1–2 | **warmup** | có mặt: 3–5 comment giúp người/ngày ở kênh chính, 1 post build-in-public/ngày, chưa link; dựng xong Pha 2 |
| 3 | **share** | ra mắt: 1 bài "tôi làm cái này vì…" mỗi kênh chính, cách nhau ≥ 1 ngày; directory theo `marketing/listings.md` |
| 4–5 | **discuss** + dài hạn | góc khác (cách làm, quyết định, số liệu, hỏi ý kiến) · 2 bài SEO (trang "X alternative", bài how-to đúng câu người ta gõ) |
| 6 | **results** | số thật sau 30 ngày, bài kể lại; quyết định tháng sau theo `## Luật dừng` |
| ≥ 30 ngày sau | **update** · **deal** | bản mới / giảm giá thật — không trước |

Mỗi dòng bảng `## Lịch 6 tuần` có một **file bài** (hoặc `—` cho việc không phải bài, vd dựng landing). Sinh file:

~~~markdown
---
stage: warmup | share | discuss | update | results | deal
where: r/macapps | X | Show HN | Product Hunt | blog
date: 2026-10-15 19:30      # giờ VN, hoặc D+3 so với Launch date
tone: <một dòng>
link: direct | first-comment | bio | none
media: media/<file>
gate: <điều kiện trước khi đăng, vd ≥10 karma, landing live>
status: planned
---
# NN — <nơi> · <ngày>
<2–3 dòng ghi chú tiếng Việt: vì sao bài này, kiểm gì trước khi đăng>
## Title
```text
...
```
## Body
```markdown
...
```
~~~

Đặt ở `marketing/<kênh>/NN-<nơi>.md` (kênh: `reddit`, `x`, `hn`, `producthunt`, `blog`, `youtube`…; số kế tiếp, **không ghi đè** file có sẵn).
Reddit: viết theo `/app-reddit` + hồ sơ luật sub (chưa có → ghi `gate: chạy /rules r/<sub>`). X: 1 file = 1 post hoặc 1 thread.
Email 1-1 (blogger, YouTuber) → `marketing/email/NN-<người>.md` (tab Outreach), không vào lịch Campaign.

## Pha 5 — Bảng số + nhịp tuần (30 phút, cùng một ngày mỗi tuần)

Mỗi tuần một dòng `## Bảng số`: lượt xem landing · email mới · lượt cài/đơn · doanh thu · bài đã đăng · nguồn (link dashboard + ngày).
Không có số → `chưa đo`. Đọc theo thứ tự: bài nào đem người tới (link đo nguồn) → trang có giữ được không (xem → email/đơn) → làm 1 việc.
Đánh dấu bài đã đăng bằng Promo Desk (**Mark as posted** ghi `status: posted <ngày> <link>`) hoặc sửa dòng `status:`.

## Pha 6 — Luật dừng / dồn sức (viết trước, đọc ở tuần 6)

Viết trước khi bắt đầu, để tuần 6 không tự lừa mình. Mẫu:
- Kênh chính có ≥ 3 bài mà 0 người về landing → `bỏ`, lấy kênh `phụ` điểm cao nhất lên.
- Có người về mà 0 email/đơn → lỗi ở trang/định vị, không ở kênh → sửa landing/câu hero trước khi đăng thêm.
- Có đơn → giữ kênh đó, tăng nhịp ×2, nối TrustMRR, viết bài results.
- 6 tuần, tổng < 3 đơn và < 30 email → định vị sai: quay lại Pha 1 với nhóm khách khác (hoặc bán dịch vụ trước).

## Không làm

- Không đăng bài, không comment, không gửi email thay người dùng; không đăng nhập mạng xã hội.
- Không mua follower, upvote, review; không nhờ nhóm upvote; không dùng nhiều tài khoản; không dán một bài vào nhiều sub.
- Không bịa số, trải nghiệm, lời khen của khách. Số không có nguồn → `chưa đo`.
- Không làm thêm kênh ngoài 2 chính + 1 dài hạn + ≤ 2 phụ trong 6 tuần — kênh mới ghi vào `## Backlog`.

Xong mỗi lần chạy: `python3 scripts/check_gtm.py <slug>` · `python3 scripts/app.py log <slug> --skill app-gtm "..."` ·
4 dòng lời thường vào LEARNED.md (vừa làm gì · vì sao · file nào · lần sau gõ gì).
