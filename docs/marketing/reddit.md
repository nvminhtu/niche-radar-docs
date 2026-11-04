# Marketing 4 · Reddit Q&A

> Tìm câu hỏi thật trên Reddit về chọn niche app, soi đối thủ Google Play / App Store, Google Trends, keyword cạnh
> tranh. Claude viết nháp câu trả lời, **anh tự đăng**. Chỉ nhắc ShotMatic khi hợp với câu hỏi.

<span class="chip chip--todo">Chưa chạy · skill + hồ sơ nháp có từ 2026-11-02 · chờ anh duyệt hồ sơ</span>

<div class="box box--goal" markdown>
**Đích**

- Mỗi tuần **3 câu trả lời** giúp được thật, đăng ở đúng subreddit.
- Khách từ Reddit hiện trong GA4 (kênh Social / Referral `reddit.com`) và lượt tải có `ref=reddit`.

**Xong khi:** đăng đủ 10 câu trả lời · có số khách từ Reddit trong [bảng số tuần](google-analytics.md#bang-so-tuan).
</div>

## Chạy thế nào

Mở Claude Code bằng `claude --chrome` ở gốc repo niche-radar, rồi:

1. `/reddit-qa tìm`: Claude dùng Chrome thật của anh **chỉ để đọc** Reddit, gom câu hỏi vào hàng chờ có điểm.
2. `/reddit-qa viết 3`: viết nháp 3 câu trả lời tiếng Anh theo hồ sơ sản phẩm.
3. Anh tự copy lên Reddit, rồi `/reddit-qa đã đăng <id>` để đánh dấu.

Dữ liệu ở `marketing/reddit/` (không sync ra trang này): `profile.md` hồ sơ · `queue.md` hàng chờ · `raw/` · `drafts/`.

## Việc trước khi chạy

- [ ] **(Anh)** đọc `marketing/reddit/profile.md`, sửa các dòng có dấu ❓ (giá, kinh nghiệm thật của người viết), gõ "ok profile"
- [ ] Chạy lượt tìm đầu, chọn 3 câu hỏi
- [ ] Gắn `ref=reddit` vào link tải trong câu trả lời để đếm được

## Luật

- Claude không đăng, không comment, không vote, không đăng nhập thay anh.
- Không bịa số: chỉ dùng số có nguồn trong `profile.md`.
- Không nhắc sản phẩm ở subreddit cấm tự quảng cáo, hoặc khi người hỏi chưa có niche.

## Liên quan

[Backlog 29 · Skill Reddit Q&A](../web/phase-backlog-29-reddit-qa-skill.md) ·
[Phase 11 · Reddit Gap](../web/phase-11-reddit-gap.md) · Skill: `/reddit-qa`
