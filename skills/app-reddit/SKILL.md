---
name: app-reddit
description: "Skill phụ của bước 12 (marketing) và app Promo Desk — viết bài đăng, comment, trả lời comment, DM trên Reddit sao cho đọc như người thật trong sub đó viết, KHÔNG AI slop: đọc thread thật trước (bài + comment, hoặc bài gần đây của sub), đọc luật sub, trả lời đúng cái người ta hỏi ở câu đầu, một chi tiết cụ thể thay cho ba câu chung chung, không gạch ngang dài (—), không emoji, không 'Great question / Hope this helps / delve / game-changer', không bịa trải nghiệm, số liệu, đường dẫn menu; nhắc sản phẩm của mình chỉ khi thật sự giải đúng nhu cầu và luật sub cho phép, kèm câu 'I made it'. Có bảng tự kiểm trước khi lưu. Use when 'viết bài reddit', 'comment reddit', 'trả lời comment', 'reply reddit', 'post bài lên r/…', 'dán link reddit', 'trả lời bài này', 'viết sao cho không giống AI', 'ai slop', 'bài reddit bị chê giống chatgpt', 'reddit DM', or when Promo Desk sends /reddit or /comment."
---

# app-reddit — viết Reddit như người thật

Dân Reddit bắt bài văn máy rất nhanh, và một comment bị gắn mác "ChatGPT" làm hỏng uy tín cả tài khoản. Skill này là
**giọng viết** — dùng cho mọi chữ đăng lên Reddit: bài mới, comment vào bài, trả lời một comment, DM.
Luật sub (tự quảng cáo, flair, tiêu đề, **giọng văn, hình kèm theo**) nằm ở trang Wiki subreddit — **đọc ở đó, đừng đi
lấy luật lại**:
- Promo Desk: `~/Library/Application Support/PromoDesk/subreddits/r-<Name>.md` (app tự chép từ Wiki mỗi lần Sync Knowledge).
- Ngoài Promo Desk: repo Product Growth Playbook, `docs/subreddits/r-<Name>.md` + mục lục `docs/subreddits/README.md`
  (danh sách sub cho app Mac xếp từ dễ tới khó).
Trang có `checked:` dưới 60 ngày thì dùng luôn. Chưa có trang hoặc cũ hơn → đọc luật thật rồi ghi trang mới cùng khuôn
(`/rules`). Skill này là giọng viết, không thay chỗ đó.
Frontmatter trang luật có thêm 3 dòng cho cổng luật của Promo Desk (luật không nói thì bỏ dòng, không đoán):
`promo: yes|no|<ngày>` (cho tự quảng cáo không — `no` thì chỉ viết bài giúp đỡ, không link), `min-karma: <n>`,
`cooldown-days: <n>` (số ngày giữa hai bài của cùng một người làm app).
Danh sách sub **của từng app** ở `marketing/reddit/subs.md` (`- r/name · fit 1–10 · angle … · why: …`, `hidden` = bỏ) —
viết bài cho app nào thì ưu tiên sub trong file đó.

## 0. Đầu vào — không có thì không viết

| Việc | Phải đọc trước |
|---|---|
| Bài mới trong r/X | hồ sơ luật sub + vài bài đang lên ở sub (Promo Desk lưu sẵn file "Recent posts") |
| Comment vào bài | toàn bộ bài + các comment đang có (file thread Promo Desk lưu, mục **TARGET** là bài) |
| Trả lời một comment | comment đó (mục **TARGET**) + bài gốc + các comment khác |
| DM | bài/comment công khai mà người đó hỏi |

Không đọc được thread → dừng, xin người dùng dán chữ vào. **Không bao giờ đoán nội dung từ cái link.**

## 1. Quyết định nói gì (trước khi viết chữ nào)

1. Họ hỏi/nói **đúng** điều gì? Viết lại thành một câu bằng chữ của họ. Trả lời câu đó, không phải phiên bản chung chung.
2. Người dùng (chủ app) muốn nói gì — lấy ý từ ghi chú của họ (thường tiếng Việt). Giữ đúng ý, đúng sự thật họ đưa.
3. Mình thêm được **một** điều gì mà các comment khác chưa nói? Không có gì mới → nói ngắn, hoặc khuyên người dùng đừng comment.
4. Có nên nhắc sản phẩm không? Chỉ khi: người dùng bảo nhắc, **hoặc** sản phẩm giải đúng câu họ hỏi **và** luật sub cho phép.
   Nhắc thì nói thẳng `I made it` / `I built this` (Reddit ghét giấu danh tính), không link nếu sub cấm link trong comment,
   và vẫn trả lời trọn câu hỏi trước — sản phẩm là câu phụ ở cuối, không phải lý do của comment.

## 2. Giọng viết

**Làm:**
- Câu đầu là câu trả lời. Không chào, không khen câu hỏi, không nhắc lại đề bài.
- Một chi tiết cụ thể kiểm được (đường dẫn menu, phím tắt, tên lệnh, phiên bản macOS) hơn ba câu chung chung.
- Chữ thường ngày, viết tắt kiểu nói (`it's`, `don't`, `you'll`), câu dài ngắn xen nhau, đoạn 1–3 câu.
- Độ dài theo comment hay nhất trong thread — thường 2–6 câu. Bài mới: theo bài đang lên ở sub.
- Được phép có chính kiến, được nói "not sure, but…", được nói cách này có nhược điểm gì.
- Danh sách chỉ khi thật sự là các bước làm theo thứ tự; dùng `1.` hoặc `-` trần, không in đậm đầu dòng.
- Tiếng của thread (thường là tiếng Anh). Ghi chú cho người dùng thì tiếng Việt có dấu.

**Không (máy hay viết — bị bắt ngay):**
- Gạch ngang dài `—` / `–`. Dùng dấu phẩy, dấu chấm, ngoặc đơn, hoặc ` - `.
- Emoji, tiêu đề `##`, dòng in đậm làm đề mục trong comment, "TL;DR:" ở đầu.
- Mở bài: "Great question", "Absolutely!", "As someone who…", "Ah, the classic…".
- Kết bài: "Hope this helps!", "Let me know if you have any questions", "Feel free to…", "Happy to help", đoạn tóm tắt.
- Từ: delve, tapestry, game-changer, seamless, leverage, robust, elevate, unlock, unleash, dive into, navigate the,
  crucial, furthermore, moreover, it's worth noting, testament to, plethora, myriad, landscape, realm, supercharge,
  empower, streamline, cutting-edge, hidden gem, must-have, level up, here's the thing, buckle up.
- Cấu trúc: "It's not just X, it's Y", liệt kê ba thứ mọi câu, câu hỏi tu từ rồi tự trả lời, mỗi đoạn kết bằng một câu "chốt".
- Bịa chuyện bản thân cho "giống người": "I've been using Macs for years", "Took me years to learn this", "people around me
  had no idea", "I had the same issue", "my wife…". Người dùng không kể thì không có — mẹo cứ trình bày là mẹo.
  (Promo Desk cảnh báo "Personal claim" khi thấy các câu này.)
- Bịa số, bịa đường dẫn menu / phím tắt không chắc. Thiếu → hỏi người dùng hoặc để ra ngoài và ghi vào dòng ghi chú "cần kiểm".
- Giọng bán hàng: "Check out…", "You'll love…", "the best app for…".

## 3. Ví dụ

Thread: *"Mac says 'System Data' is 120 GB, how do I shrink it?"* — ghi chú người dùng: "chỉ cách xoá Time Machine local snapshots".

Máy viết (bỏ):
```text
Great question! "System Data" can be a real headache — but don't worry, there are several ways to tackle it. 🚀
**1. Local Snapshots:** Time Machine stores local snapshots...
Hope this helps!
```

Người viết (giữ):
```text
A big chunk of that is usually Time Machine local snapshots. Run `tmutil listlocalsnapshots /` in Terminal to see them,
and `tmutil thinlocalsnapshots / 999999999999 4` to drop them. macOS also clears them on its own when space runs low,
so the number in Storage can look scarier than it is.
```

## 4. Tự kiểm trước khi lưu (sửa hết mới lưu)

- [ ] Câu đầu trả lời đúng điều họ hỏi (đọc lại TARGET).
- [ ] Không có `—` `–`, emoji, tiêu đề, dòng in đậm, mở/kết bài sáo rỗng, từ trong danh sách cấm.
- [ ] Mọi chi tiết kỹ thuật là thứ chắc chắn đúng hoặc người dùng đưa; chỗ chưa chắc đã ghi vào ghi chú "cần kiểm".
- [ ] Không câu kể chuyện bản thân nào mà người dùng không đưa. Không bịa số liệu. Không có chữ quyên góp.
- [ ] Sản phẩm: không nhắc, hoặc nhắc đúng luật + có "I made it".
- [ ] Độ dài ngang comment tốt nhất trong thread; đọc to lên nghe như người gõ trên điện thoại.
- [ ] Bài mới: tiêu đề ≤ 300 ký tự, đúng kiểu tiêu đề + flair trong hồ sơ sub, không giống bài nào khác mình đã đăng.

Promo Desk cũng tự soi các dấu hiệu trên (cảnh báo vàng trên thẻ bài) — còn cảnh báo thì sửa câu, đừng lách chữ cho qua.

## 5. File kết quả (Promo Desk)

- Bài mới: `marketing/reddit/NN-<sub>.md` — `## Title` + `## Body` (khuôn ở lệnh `/reddit` của app).
- Comment / trả lời: `marketing/reddit/NN-<sub>-<comment|reply>.md` — frontmatter `kind: comment|reply`, `source: <link>`,
  `reply-to: u/<tên>`, `asked`, `ask`, `stage: discuss`, `link`, `status: planned`; chỉ có `## Body`.
- Người dùng tự dán và bấm đăng. Claude không đăng, không đăng nhập Reddit.
- Bài có ảnh quảng cáo làm riêng → cũng đưa lên landing: `scripts/promo_gallery.py add` (xem `/app-marketing` ▸ Ảnh quảng cáo → landing).
