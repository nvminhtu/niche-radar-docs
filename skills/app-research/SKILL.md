---
name: app-research
description: "Bước 1 của pipeline app — tìm ý tưởng app ĐÁNG làm trước khi viết một dòng code: đo kệ App Store bằng endpoint công khai của Apple (bảng xếp hạng theo thể loại, tuổi app, số đánh giá, autocomplete tìm kiếm, review 1–3★, danh sách In-App Purchase để biết đối thủ thu phí kiểu gì), đo Google Play qua trang tìm kiếm, Google Trends, Reddit; lọc theo ràng buộc của người không biết code (không backend, MVP ≤ 4 tuần, bán subscription được); soi nhu cầu thật (lúc dùng, việc được làm xong, chỗ đau, vì sao đổi — đo từ review bằng lệnh `mine`, autocomplete, Reddit); chấm điểm 3–5 ý tưởng, TỰ ĐỀ XUẤT một ý và ghi 2 file để người dùng duyệt lúc rảnh: research/<niche>.md (phân tích đủ, đối thủ kèm link) và apps/ACTIVE/<slug>/context-ai/brief.md (app làm gì trong vài dòng + prompt sinh màn hình chính). Có nhánh app Mac nhỏ (`search --mac`, `macchart`, app Mac gốc vs app iPhone chạy trên Mac, mua đứt vs subscription). Chạy được không cần người trông trong giờ làm; thêm `--ask` để dừng hỏi ở CỔNG 1 như cũ. Người dùng duyệt xong mới tạo app bằng scripts/app.py init. Use when someone has no app idea yet or wants to validate one, 'nên làm app gì', 'tìm ý tưởng app', 'research thị trường app', 'app nào đang kiếm tiền', 'đối thủ app', 'review app đối thủ chê gì', 'ý tưởng này có ai làm chưa', 'app subscription nào hợp người mới', 'research app mac', 'app mac nhỏ bán được', 'ý tưởng app macos', 'tìm idea app', 'người dùng thật sự cần gì', 'find an app niche', or when scripts/app.py status says step 1 is next. Đề xuất của Claude luôn ghi 'chờ anh duyệt' — không tự ghi Verdict: GO, không bịa lượt tải hay doanh thu."
argument-hint: "[niche / chủ đề, vd 'thói quen', 'app mac dọn file'] [--mac] [quốc gia, mặc định us] [--ask]"
user-invocable: true
---

# Bước 1 — research (CỔNG 1)

Câu hỏi của bước này: **app nào đáng làm, cho người không biết code, bán subscription được?**
Đo → soi nhu cầu → chấm điểm → **đề xuất một ý + ghi file** → dừng. Mặc định chạy không cần người trông (người dùng
đang làm việc khác, đọc file sau); `--ask` → dừng hỏi ở CỔNG 1 như cũ. Dù chế độ nào, **CỔNG 1 vẫn là của người dùng**:
Claude chỉ đề xuất, không `app.py init`, không ghi `Verdict: GO` trước khi người dùng nói chọn.

Script: `S=scripts/store_research.py` (Python chuẩn + curl, không cần key).
Lăng kính: **[references/user-need.md](references/user-need.md)** — đọc trước Pha 3; §4 là phần riêng app Mac.

## Chế độ research chung (`--out <dir>`) — routine cloud, không người trông

Khi được gọi kèm `--out <dir>` (routine cloud `niche-research` truyền `dir = ai-skills-shared/research/<kind>/YYYY-MM-DD-<niche-slug>/`;
quy trình đủ ở `ai-skills-shared/reference/README-CORE-RESEARCH-01-CLOUD-NICHE-RESEARCH.md`):

- Làm đủ mọi bước đo · soi · chấm điểm của skill này — **chạy kỹ, không rút gọn**. Không hỏi người dùng (bỏ `--ask`, không AskUserQuestion); ngữ cảnh lấy từ dòng hàng chờ.
- **Chỉ ghi vào `<dir>`**, 3 file theo khuôn `ai-skills-shared/templates/research/`: `report.md`, `evidence.md`, `review.md` (chép khuôn, để trống). Không tạo / sửa / commit gì trong repo này: không file research local, không thư mục sản phẩm, brief, plan hay `state.md`.
- Nội dung bình thường ghi vào file research của skill → mục "Phân tích chi tiết" của `report.md` (giữ các mục `##` của skill), cộng các mục bắt buộc của khuôn: Bảng claim, 3 giả định rủi ro, ngách/ý đã loại, nguồn bị SKIP. Brief / prompt màn hình → mục "Brief (nếu duyệt)".
- Mọi con số → một dòng trong `evidence.md` (id · giá trị · nguồn/lệnh · link · ngày lấy). Nguồn lỗi hoặc bị chặn → `SKIP · <lý do>`, không đoán, không thay bằng số nhớ.
- Đề xuất luôn `chờ duyệt` — không bao giờ ghi `Verdict: GO` hay tạo sản phẩm.
- Cloud: endpoint công khai của Apple thường chạy được; Google Play / Reddit / Google Trends bị chặn → WebSearch thay thế, không được thì `SKIP`. Bỏ Pha 6 (không `app.py init`).

## Số liệu nói được gì (đọc trước)

Apple và Google **không công bố lượt tải hay doanh thu**. Mọi con số là tín hiệu gián tiếp:

| Tín hiệu | Gián tiếp cho | Bẫy |
|---|---|---|
| hạng top-free theo thể loại | tốc độ cài hiện tại | đổi mỗi ngày — ảnh chụp, không phải xu hướng |
| hạng top-grossing | **app đó kiếm được tiền** | gồm cả ông lớn |
| số đánh giá (`userRatingCount`) | lượt cài tích luỹ | app hay xin đánh giá làm số phồng |
| ngày phát hành của app trên bảng | bảng có bị ông lớn khoá không | |
| autocomplete (`hints`) | người ta thật sự gõ gì | cho biết có nhu cầu, không cho biết lớn cỡ nào |
| review 1–3★ | **khoảng trống để làm** | |
| tên gói IAP | đối thủ bán subscription không, giá bao nhiêu | |

Mọi bảng ghi **ngày + quốc gia**. Không bao giờ viết "lượt tải" cho một con số là số đánh giá.

## Pha 1 — Khung lọc (một đoạn, không hỏi nếu người dùng đã cho chủ đề)

Mọi ý tưởng phải qua được:

1. **Người không biết code + Claude làm MVP ≤ 4 tuần.** Không backend riêng; đăng nhập/đồng bộ chỉ khi thật cần (Firebase).
2. **Giá trị lặp lại** — người dùng mở app hằng ngày/tuần → subscription có lý do tồn tại (Apple 3.1.2(a) đòi "ongoing value").
   **App Mac nhỏ** (`--mac`): mua đứt cũng được — tiện ích Mac hay bán một lần; chốt mô hình ở `/app-money`.
3. **Không vùng pháp lý nặng:** dữ liệu y tế chẩn đoán, tài chính/đầu tư, app dành cho trẻ em (Kids Category cấm analytics bên thứ ba, paywall phải có parental gate), cờ bạc.

**Đã có ý tưởng/niche, cần biết bán được không** (ai đang thu tiền, đối thủ, đối tượng, test bán trước trên X) → chạy
`/app-demand <ý tưởng>` trước; đề xuất BUILD của nó thay cho Pha 2–4 ở đây, rồi quay lại Pha 5–6.

**Nguồn ý tưởng ngoài store:** sản phẩm indie đang có doanh thu xác minh (TrustMRR) → chạy `/app-indie <chủ đề>` trước,
dùng file `research/YYYY-MM-DD-indie-*.md` làm bậc bằng chứng "người ta đang trả tiền" (học cách làm, không chép sản phẩm).

## Pha 2 — Đo bảng xếp hạng

```bash
python3 $S genres --parent 36          # id thể loại app (6000–6027). Game là 6014 — không thuộc pipeline này
python3 $S scan --genres 6013,6017,6007,6012 --country us --out /tmp/scan.md
```

Id hay dùng: 6013 Health & Fitness · 6017 Education · 6007 Productivity · 6012 Lifestyle · 6018 Books ·
6002 Utilities · 6006 Reference · 6023 Food & Drink · 6008 Photo & Video. Kiểm lại bằng `genres`.

Đọc `scan`:
- **Tỉ lệ app < 18 tháng ≥ 40%** + tuổi trung vị < 2 năm → bảng đang thay máu, người mới vào được.
- **Tuổi trung vị ≥ 4 năm** → ông lớn khoá, bỏ qua.
- **App top-50 có < 2.000 đánh giá** → dev nhỏ đang leo được. Ghi tên — đó là bằng chứng và cũng là đối thủ gần nhất.
- **Vừa top-free vừa top-grossing** → thể loại đó trả tiền được.

**Nhánh Mac (`--mac`)** — Apple chỉ còn bảng top free Mac *tổng*, không theo thể loại (đo 2026-09-22):

```bash
python3 $S macchart --limit 50                          # top free Mac, mọi thể loại: ai đang được cài, tuổi bao nhiêu
python3 $S search "clipboard manager" --mac --limit 15  # mac-native vs iphone-on-mac, giá, link
```

Đọc: top kết quả toàn `iphone-on-mac` → chưa có bản Mac gốc tử tế · app Mac gốc đầu bảng già > 5 năm → có thể đang
bị bỏ rơi · cột ratings `n/a` = app Mac gốc (API trả 0) → dùng nhịp review của `mine`. Đối thủ ngoài store
(bán thẳng, Setapp): WebSearch trang hãng, ghi giá + nguồn + ngày.

Google Play (không có endpoint công khai ổn định): WebFetch
`https://play.google.com/store/search?q=<cụm từ>&c=apps&hl=en_US&gl=US` → tên, dev, ★. Lượt tải dạng "100K+" nằm ở
trang từng app (`/store/apps/details?id=`). Xu hướng: MCP `google-trends` (`compare_keywords`); lỗi 429 → đợi 60s thử một lần, vẫn lỗi → `chưa đo`.

## Pha 3 — Soi 4–6 hướng ứng viên

```bash
python3 $S hints "habit tracker"                      # autocomplete: người ta gõ gì, kèm từ gì ("no ads", "for adhd")
python3 $S search "habit tracker" --limit 15          # ai đứng đầu, bao nhiêu đánh giá, bao nhiêu tuổi
python3 $S reviews <id> --pages 2 --max-stars 3       # 2–3 app đầu
python3 $S iap <id>                                   # đối thủ bán gì, giá bao nhiêu (dòng "<- subscription-like")
python3 $S mine <id1>,<id2>,<id3> --pages 3           # review → chỗ đau, việc được làm xong, câu nói nhu cầu, nhịp review
```

Rồi áp lăng kính `references/user-need.md`: **bốn câu hỏi** (§1) có bằng chứng cho từng ý · **thang bằng chứng**
(§2, cần 2+ bậc) · **đau → hứa → chứng minh** (§3) · **câu hook một dòng** (§7) — không qua thì bỏ ý đó.
Reddit hỏi thẳng: §5.

- Từ đi kèm trong autocomplete (`no subscription`, `offline`, `for kids`, `simple`) là **câu nói nhu cầu** — chép nguyên văn.
- Review: gom lời than thành nhóm (ép subscription quá sớm, quảng cáo, mất dữ liệu, rối, thiếu tính năng X).
  Nhóm lặp ở nhiều app đầu = định vị của mình, **chỉ có giá trị nếu app thật sự làm được**.
- `iap`: đối thủ bán tháng/năm giá bao nhiêu → mốc giá cho `/app-money`.

## Pha 4 — Chấm điểm và đề xuất

Chấm 1–5, có trọng số:

| Tiêu chí | Trọng số | 5 nghĩa là |
|---|---|---|
| Bằng chứng nhu cầu | ×3 | 3+ bậc thang, câu nói nhu cầu ở 2+ app |
| Chỗ trống trên kệ | ×2 | bảng thay máu / toàn iphone-on-mac / ông lớn bỏ rơi |
| Chỗ đau mình giải được | ×2 | đau lặp lại, sửa bằng quyết định thiết kế chứ không bằng tiền |
| Làm được | ×2 | không backend, MVP ≤ 4 tuần, một màn chính |
| Hook rõ | ×1 | câu hook đọc một hơi |
| Thu tiền được | ×1 | đối thủ đang thu (nguồn `iap` / trang hãng), mô hình không phá lời hứa |

**Luật loại:** Bằng chứng < 3 hoặc Làm được < 3 → loại, tổng cao mấy cũng vậy. Có rủi ro Sherlock (Apple đã làm sẵn)
→ ghi rõ, thường là loại. **Rủi ro 4.3(a) Spam:** viết concept một dòng — đúng cho 50+ app trên store ("AI flashcard maker",
"PDF scanner", "AI chat") mà không có luồng chính chỉ mình có → loại (`reference/README-APP-PUBLISH-01-GUIDELINE-4-3-SPAM.md`). Chọn tổng cao nhất; hoà → cái làm rẻ hơn. Ghi một dòng *vì sao ý về nhì thua*.

## Pha 5 — Ghi file (rồi dừng) · CỔNG 1

`--ask` → `AskUserQuestion` như cũ (ý khuyên chọn đứng đầu + "(Recommended)", mô tả có bằng chứng + rủi ro) rồi mới
ghi brief. Không có `--ask` → ghi luôn, đề xuất đánh dấu "chờ anh duyệt".

**1. `research/<niche-slug>.md`** — đặt theo tên niche, không ngày. Trùng tên → thêm `-2`, `-3`… (không ghi đè):

```markdown
# <Niche> — research <YYYY-MM-DD>, <quốc gia>, <iPhone | Mac>
> Đề xuất: **<Ý tưởng>** → [brief](../<slug>/brief.md) (Claude chọn, chờ anh duyệt)

## Tóm tắt (5 dòng) — niche, người dùng, nhu cầu thật, khoảng trống, vì sao chọn
## Khung lọc
## Kệ — bảng xếp hạng / search, app mới, app dev nhỏ (kèm link)
## Người dùng — 4 câu hỏi (lúc nào · việc gì · đau ở đâu · vì sao đổi) + bậc bằng chứng
## Đối thủ — | App | link | loại (native / iphone-on-mac) | đánh giá hoặc nhịp review | tuổi | giá / mô hình | khen | chê |
## Nhu cầu nguyên văn — autocomplete, câu nói nhu cầu, Reddit (trích ngắn, có link)
## Ý tưởng — bảng điểm + mỗi ý một đoạn + câu hook + đau→hứa→chứng minh
## Đề xuất — ý chọn, vì sao, vì sao ý nhì thua, rủi ro lớn nhất, điều gì sẽ đổi quyết định
## Nguồn — mọi URL + ngày; output thô của scan
```

**2. `apps/ACTIVE/<slug>/context-ai/brief.md`** — đọc trong một phút (thư mục tạo bằng tay; `app.py init` sau này vẫn chạy được vì nó chỉ
từ chối khi đã có `app.json`):

```markdown
# <Tên app> — <câu hook>
- Làm gì: <3 dòng: người dùng làm gì, app làm gì, điểm khác>
- Cho ai / lúc nào: <người dùng + khoảnh khắc>
- Khác đối thủ: <lời hứa + cách chứng minh>
- Thu tiền: <subscription / mua đứt / free + Pro> · đối thủ thu <giá, nguồn>
- Nền tảng: <iOS+Android Flutter | macOS, direct hay mas để app-money chốt>
- MVP: <màn chính, có cần backend không, ước tuần>
- Tên store dự kiến: <cụm người ta gõ> - <Brand> (cụm lấy từ `store_research.py rank`, có Gợi ý `có`)
- Research: [research/<niche>.md](../../research/<niche>.md)

## Prompt — màn hình chính
<prompt ảnh dán được ngay>
```

Prompt màn chính theo tuyến ảnh của repo (`core:asset-prompt`): **Claude chỉ viết prompt, Codex/ChatGPT sinh ảnh.**
Tả đúng một khoảnh khắc đang dùng thật: bố cục, nội dung mẫu thật (không lorem ipsum), trạng thái của hành động
chính. Điện thoại: dọc 1290×2796. Mac: cửa sổ 16:10 2880×1800 (hoặc popover menu bar nếu là app menu bar), theo
giao diện macOS (sidebar, toolbar, vật liệu hệ thống). Không chữ ngoài UI, không tên/logo/giao diện nhái đối thủ. Đây là
đích thiết kế cho `/app-design`, không phải ảnh store — ảnh store chụp từ app thật.

**3. Mục lục** — thêm một dòng đầu bảng trong `research/` index nếu repo có, hoặc ở cuối câu trả lời:
ngày · niche · đề xuất · link.

Câu trả lời cuối: 2 đường dẫn file, đề xuất một dòng, và câu "duyệt thì nói *chọn <ý>* → tôi chạy Pha 6".
**Chưa `app.py init`, chưa spec, chưa code** trước khi người dùng chọn.

## Pha 6 — Tạo app và bàn giao

Sau khi người dùng chọn (trong phiên này hoặc lúc duyệt file sau), hỏi (hoặc đề xuất rồi xác nhận) tên hiển thị và **bundle id** — dạng `com.<tên-bạn>.<tênapp>`,
chữ thường, **không đổi được sau khi lên store**. Kiểm tên chưa bị dùng: `python3 $S search "<tên>"` + tìm trên Play.

```bash
python3 scripts/app.py init --slug <slug> --name <PascalCase> --bundle-id com.<ban>.<tenapp> \
    --label "<Tên hiển thị>" --research research/<niche>.md
# app Mac: thêm --stack macos --distribution direct|mas (distribution chốt ở app-money — hỏi nếu chưa rõ)
```

Điền `apps/ACTIVE/<slug>/context-ai/research-<slug>.md` (`init` đã tạo, app cũ: `research.md`) từ hàng đã chọn, dòng cuối `Verdict: GO` (người dùng đã chọn ở CỔNG 1 — ghi vào
"Quyết định đã chốt" trong state.md). Mục **Bước 1** trong LEARNED.md. Tiếp theo: `/app-money`.

## Không làm

- Không gọi số đánh giá là lượt tải; không ước doanh thu đối thủ.
- Không chép tên, icon, ảnh, nội dung của đối thủ — research tìm **nhu cầu**, không tìm thứ để sao chép.
- Script lỗi (Apple 403/503) → thử lại một lần sau; không lấp chỗ trống bằng trí nhớ.
