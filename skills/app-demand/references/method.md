# app-demand — phương pháp

Gom từ: slavingia/skills (`validate-idea`, `first-customers` — sách *The Minimalist Entrepreneur*),
coreyhaines31/marketingskills (`customer-research`, `competitors`), BMAD-METHOD (market research), cộng luật đã trả giá
của repo này (4.3 Spam, không bịa số). Diễn đạt lại, không chép nguyên văn.

## §1 Thang bằng chứng (yếu → mạnh)

| Bậc | Bằng chứng | Tính cho |
|---|---|---|
| 0 | bạn bè khen, "ý hay đấy" | **không tính** |
| 1 | autocomplete / Google Trends có cụm này | có người tìm |
| 2 | câu than nguyên văn trên review/Reddit/HN/X | có người đau |
| 3 | đối thủ có review 1–3★ chê đúng chỗ đó | đau mà chưa ai chữa tốt |
| 4 | đối thủ đang thu tiền (TrustMRR verified, top-grossing, IAP) | **có người trả tiền** |
| 5 | người lạ để lại email / bấm nút giá trên landing của mình | **muốn mua của mình** |
| 6 | người lạ trả tiền đặt trước | đã bán được |

BUILD cần bậc 4 **và** bậc 5 trở lên. Chỉ có bậc 1–3 → TEST THÊM.

Cờ đỏ (Sahil): không ai đang cố giải việc này (không có cách làm tay nào) · không kể ra được 10 người cụ thể ·
phải "giáo dục" người ta rằng họ có vấn đề · làm cho cộng đồng mình không thuộc về.
Cờ xanh: người ta đang trả tiền cho đồ kém hơn · cộng đồng than liên tục · tả được khách + nỗi đau trong một câu · tự mình cũng cần.

Độ tin của một nhận định (customer-research): **cao** = ≥ 3 nguồn độc lập, tự nói ra (không bị hỏi) · **vừa** = 2 nguồn ·
**thấp** = 1 nguồn. Lệch mẫu: review là người cực khen/cực chê; Reddit/HN nghiêng dân kỹ thuật, khó tính; X nghiêng
người thích công cụ mới. Ưu tiên nguồn 12 tháng gần nhất.

## §2 Câu tìm (dán thẳng)

**Reddit** (search.json bị chặn → WebSearch):
- `site:reddit.com "<cụm>" "is there an app"` · `"alternative to <đối thủ>"` · `"<đối thủ>" "too expensive"` ·
  `"<cụm>" "I wish"` · `"<cụm>" "switched from"` · `"<cụm>" "worth paying"`
- Sub hay dùng: r/apps, r/iphone, r/androidapps, r/macapps, r/productivity, r/selfhosted (đồ free), sub của nghề/sở thích.

**X** (người dùng tự tìm trên X, Claude đưa câu):
- `"<cụm>" ("anyone know" OR "looking for" OR "recommend") min_faves:5 -filter:replies`
- `"<đối thủ>" (hate OR "switched" OR "cancel" OR "too expensive")`
- `"<cụm>" filter:links` → ai đang ra mắt cái gì; xem reply để thấy ai quan tâm.

**Hacker News:** `python3 scripts/demand_research.py hn "<cụm>"` (bài: Show HN = đối thủ mới) và `--comments`
(câu than, "is there anything that sets it apart"). Ask HN "what do you use for <việc>".

**App Store / Play:** `store_research.py hints` (từ đi kèm "no subscription", "offline", "for adhd" = nhu cầu) ·
`store_research.py mine <ids>` · `demand_research.py play "<cụm>"` (lượt cài dải + IAP + lần cập nhật).

**TrustMRR:** `site:trustmrr.com "<cụm>"` → slug → `demand_research.py trustmrr <slug>`. Trang
`trustmrr.com/category/<slug>` và `trustmrr.com/channels/<slug>` (sản phẩm theo kênh marketing).

## §3 Thẻ đối tượng (điền đủ, mỗi ô 1 bằng chứng)

```
Ai: <nghề/hoàn cảnh cụ thể>            Kích hoạt: <chuyện vừa xảy ra>
Việc cần xong: chức năng <> · cảm xúc <> · xã hội <>
Đang xài gì thay: <cách làm tay / app>  Vì sao chưa đủ: <câu chê>
Ở đâu: <sub · hashtag · tài khoản X · nhóm>
Trả được: <giá họ đang trả cho thứ gần nhất>
```

## §4 Câu hook

Công thức: **<kết quả họ muốn> + <không phải chịu nỗi đau cũ>** — đọc một hơi, không thuật ngữ.
Kiểm: đưa câu hook cho người trong nhóm đối tượng — họ phải nói được "à, cái này để làm X cho tôi".
Viết 3 bản, đem bản tốt nhất đi test Pha 5 (mỗi bài X một bản = A/B tự nhiên).

## §5 Mẫu bài X test nhu cầu (tiếng Anh, người dùng tự đăng)

1. **Vấn đề trước, app sau** — "<Nỗi đau cụ thể bằng lời của họ>. Every app I tried <chỗ chê>. So I'm building <hook>.
   Want early access? <link>" + ảnh mockup.
2. **Hỏi thẳng** — "If an app did <việc> without <nỗi đau>, would you pay $<giá>/<kỳ>? Building it this month." (đếm reply có
   "yes"/giá; reply có tên tài khoản = dòng "người nói sẽ trả").
3. **Build in public** — ảnh mockup + "Day 1 of building <hook>. Waitlist: <link>" — giữ nhịp, mỗi lần có tiến độ thì đăng.

Không hứa tính năng chưa chắc làm được; không dùng tên/ảnh đối thủ trong ảnh.

## §6 Mẫu DM/reply (cá nhân hoá từng người, không dán hàng loạt)

> "Saw your post about <nỗi đau cụ thể của họ>. I'm building a small app for exactly that — <hook>. Would you try an early
> build and tell me what's missing? No pitch, just want it to be useful."

Mỗi lời từ chối là dữ liệu: sai người hay sai sản phẩm → ghi 1 dòng.

## §7 Fake door / đặt trước

- Nút "Get early access — $X/yr" trên landing → mở form email + câu "we'll email you at launch, price locked". Đếm click
  bằng GA4 event (`store_click`/`generate_lead` của oneclicktool-landing).
- Đặt trước thật: Lemon Squeezy/Polar sản phẩm "Founding member" giá thấp, hoàn tiền nếu không ra mắt — **người dùng tự tạo
  sản phẩm và bấm**, Claude chỉ soạn chữ. App store: dùng tính năng Pre-order của App Store khi đã có build.
- Chưa có cổng thu tiền → đếm email + click giá là đủ cho quyết định đầu.

## §8 Sau khi BUILD — biến research thành ngày ra mắt có người mua

- Waitlist = danh sách email báo ra mắt (ngày 1 có người tải trial).
- Câu nói nguyên văn → mô tả store, landing, bài X ra mắt.
- Nơi đối tượng ở → 2 kênh chính của `/app-gtm`.
- Mẫu verified gần nhất trên TrustMRR → mốc giá cho `/app-money`, và mục tiêu so sánh ở `/app-grow`.
