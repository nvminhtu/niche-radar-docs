# 35 · Xin tính năng: người dùng muốn có gì, app nào còn thiếu

> Plan 2 · mục 35. Làm thật tab **Xin tính năng** của [Đào review](phase-plan2-27-review-mining.md) (đang "Sắp có", ý ở 27.5),
> từ "Module 06 · Feature Request Mining" anh dán 2026-11-18. Lời chê cho biết người dùng **ghét gì**, tab này cho biết họ
> **muốn có gì**: gom câu "I wish… / please add… / bring back…" thành danh sách tính năng, đếm người xin, xem app nào đã có,
> và chấm xem có đáng làm không.

<span class="chip chip--todo">Viết 2026-11-18 · chờ anh chốt 4 câu · chưa code</span>

## Có gì sẵn rồi

Không làm từ đầu. Code đã có gần nửa:

| Đã có | Ở đâu | Còn thiếu gì |
|---|---|---|
| Mẫu câu "ước gì" (14 mẫu: *wish, please add, would be nice, bring back, need a way to…*) | `complaint-rules.ts` → `WISH_PATTERNS` | Chỉ đọc review **1–3★**. Gộp theo 2 chữ đầu nên "dark mode" và "night theme" là 2 dòng |
| Hàm `wishes()` gộp điều ước + câu trích | `complaints.ts` | Mỗi review chỉ lấy **điều ước đầu tiên**. Không có sao trung bình, không biết app nào bị xin |
| Khối "Người dùng ước gì" ở Lời chê + MCP `top wish` | `ComplaintsBlock.tsx`, `mcp/tools.ts` | Chỉ là danh sách, chưa có trang riêng |
| Ma trận tính năng có / không theo mô tả store (Feature Gap) | `compare-extract.ts` (`FEATURE_LEXICON`, `wishCount`) | Đã nối điều ước vào hàng tính năng, nhưng chiều ngược lại (điều ước → app nào thiếu) chưa có |
| App có IAP / gói tháng | `iap_cache`, `offers_iap` | Chưa dùng cho điều ước |

## Đã đo (2026-11-18 · DB máy dev, chỉ đọc)

- **`review_seen`:** 15.956 review của 266 app (14.903 câu khác nhau).
- **Review có mẫu câu xin** (đếm thô bằng 10 mẫu chính): **394** review (2,5%), 366 câu khác nhau, ở **140 app**.
- **Theo sao:** 1★ 111 · 2★ 56 · 3★ 110 · **4★ 56 · 5★ 61**. Tức **30% lời xin nằm ở review 4–5★** mà `wishes()` hiện bỏ qua.
  Đúng như mẫu anh dán: người khen app vẫn xin thêm (*"Best application ever. Wish that widgets… are coming soon"*).
- **Chỉ 6 app có ≥ 10 lời xin.** Một app đơn lẻ thường quá ít để xếp hạng → tab này phải gom **nhiều app cùng niche**
  mới có số đáng tin.
- **Không có cột người viết** trong `review_seen` (chỉ có `hash` của chữ). "Số người xin khác nhau" chỉ đếm được bằng
  **số review khác nhau** (bỏ trùng chữ + bỏ trùng giữa các nước, như gotcha của 27). Không gọi là "unique reviewers".
- Một review hay xin **nhiều thứ cùng lúc** (*"please add penalty… or add non-repeat option…"*). Phải tách từng câu / từng vế.

## Học từ tool lớn + nghiên cứu (tìm 2026-11-18)

| Nguồn | Họ làm gì | Mình lấy gì |
|---|---|---|
| **Pendo Feedback** (ảnh anh dán) | Bảng Requests: tên · trạng thái · số vote · "Smartlist value" (vote cân theo giá trị khách) | Bảng 1 dòng / tính năng, cột **số người xin** + **thanh điểm**. Không lấy cột trạng thái (mình không phải chủ app) |
| **Canny / ProductLift / UserVoice** | Vote → chấm RICE, cân theo doanh thu của khách (MRR / ARR) | Ý "**vote chưa đủ, phải có tín hiệu tiền**". Mình không có MRR của ai, nên thay bằng tín hiệu trả tiền đọc được từ review + IAP |
| **AppFollow** | Tự gắn tag *feature request / bug / opportunity*, xem được cả review đối thủ | Tách lời xin thành **loại** (mới · mang lại · tích hợp · nền tảng · cách trả tiền) |
| **Appbot** | Lọc review theo topic + sao + ngôn ngữ để tìm lời xin | Lọc tab theo sao / nước / app |
| **Maalej et al. 2015–16** (bộ dữ liệu chuẩn: bug · feature request · trải nghiệm · rating) | Phân loại review bằng chữ + luật + học máy | Lời xin là 1 lớp riêng, **có thể trùng** với lỗi ("crashes, please add backup") |
| **SAFE / MARA / RE-Miner** (bài báo, có tool mẫu) | Rút tên tính năng bằng mẫu câu (SAFE), rút lời xin + lỗi (MARA) | Đúng hướng mình đang làm (luật mẫu câu). Bản sao SAFE cho thấy luật đơn giản bỏ sót nhiều, nên cần ✦ AI gộp tên |
| **LLM zero-shot 2025** (ICAART: GPT-3.5 F1 ≈ 0,85 cho 4 lớp; bài khác F1 0,32–0,74) | AI phân loại lời xin khá tốt, nhưng dao động | ✦ AI chỉ **đặt tên + gộp nhóm**, không đếm, không tạo lời xin mới |

**Repo / skill có sẵn:** không có skill nào trong máy hay trên claude.ai làm việc này. Repo GitHub chỉ có code bài báo
(SAFE, RE-Miner) chạy Python + model, không ghép vào được app Node. Phần lõi tự viết bằng luật như 27 + 33.
Skill `marketing-skills:customer-research` chỉ dùng làm khung câu hỏi cho ✦ AI.

**Tool lớn không làm (và mình làm được):** Pendo / Canny gom lời xin **của khách app mình**. AppFollow gom lời xin **của
app đối thủ** nhưng không trả lời "**cả chợ đang xin cái gì mà chưa ai làm, có đáng làm app mới không**". Đây là chỗ ShotMatic khác.

## Bản đề xuất được chỉnh lại ở đâu

| Bản đề xuất (8 cột) | Vấn đề | Plan này làm |
|---|---|---|
| Feature name | AI đặt tên dễ bịa | Tên = cụm chữ người dùng gõ nhiều nhất trong nhóm. ✦ AI chỉ đề xuất tên gọn hơn, nhãn **AI suy luận** |
| Number of requests | Đếm câu hay đếm review? | Đếm **review** (1 review xin 2 lần vẫn là 1). Ghi rõ "từ N review đã đọc" |
| Number of unique reviewers | DB không có người viết | Đổi thành **số review khác nhau** (bỏ trùng chữ + nước). Ghi rõ trong ⓘ |
| Competitors missing the feature | Không nói lấy từ đâu | Đọc **mô tả store** bằng Feature Gap (mục 22) → chấm **có / không thấy / chưa đọc**. "Không thấy trong mô tả" ≠ "không có" |
| User rating | Sao của gì? | **Sao trung bình của review xin** + tách: bao nhiêu ở review chê, bao nhiêu ở review khen |
| Potential revenue impact | Không có số tiền thật, đoán là bịa | **Không ra số tiền.** Thay bằng 3 chấm **tín hiệu trả tiền** (35.3). Đúng luật 27.5 "không đoán tiền" |
| Implementation complexity | Code không biết độ khó | Chip **Cỡ việc** S / M / L từ bảng tra tay (35.4), nhãn **Ước tính**, anh sửa được. Không biết thì để "?" |
| Supporting review quotes | Ổn | 3 câu trích nguyên văn + link review gốc, như 27.4 |

## Làm gì

### 35.0 · Đọc lời xin đủ hơn

- Đọc lời xin trong **cả 1–5★** (lời chê vẫn 1–3★ như cũ). Khi ở Đào review chỉ đã đọc 1–3★ → ⓘ "chưa đọc review khen,
  có thể thiếu ~30% lời xin" + nút **Đọc thêm 4–5★**.
- Tách review thành câu, rồi tách vế bằng *or / and also / also*. Mỗi vế khớp mẫu là 1 lời xin. Bỏ giới hạn
  "mỗi review 1 điều ước".
- Thêm mẫu câu (đo lại số trúng trước khi giữ): *can you add, could you add, it needs, really need, add support for,
  allow us to, let me, would pay for, any plans to, hope (you|they) add, should be able to*. Mẫu phủ định
  (*"no need to add"*, *"don't add ads"*) bị loại.
- Bỏ câu xin **chính app đang có lỗi** ("wish it didn't crash" → về Lỗi, không phải tính năng).

### 35.1 · Gom lời xin thành tính năng (hàm thuần)

- Khoá gộp như `wishes()` hiện nay, thêm **bảng đồng nghĩa tính năng** (dark mode = night mode = dark theme;
  export = backup to file; sync = cloud; widget = home screen) dùng chung với `FEATURE_LEXICON` của Feature Gap.
- Gắn **loại lời xin** bằng luật:

| Loại | Dấu hiệu |
|---|---|
| ✨ Tính năng mới | mặc định |
| ↩️ Mang lại | *bring back, used to have, removed, old version had* |
| 🔗 Tích hợp | tên dịch vụ: *Google Drive, Dropbox, Calendar, Notion, Apple Health, Zapier…* |
| 📱 Nền tảng | *widget, watch, iPad, tablet, desktop, web version, offline, dark mode* |
| 💳 Cách trả tiền | *lifetime, one-time purchase, family plan, cheaper plan, free tier* |

- Nhóm chỉ lên bảng khi có **≥ 3 review** (giống 27). Dưới 3 vào mục gập "Lời xin lẻ".
- Nút **✦ Gom lại theo nghĩa** dùng lại 27.4: AI chỉ được gộp nhóm đang có + đặt tên, số đếm lại bằng code.
  Khi mục 34 (gom theo nghĩa bằng embedding) xong, thay luật gộp bằng embedding, tab này không đổi giao diện.

### 35.2 · Mỗi tính năng có gì

| Cột | Cách tính | Nhãn |
|---|---|---|
| Tính năng + loại | 35.1 | Đo được (tên) / AI suy luận (nếu ✦ đặt tên) |
| Số người xin | số review khác nhau | Đo được |
| Bao nhiêu app bị xin | số app có ≥ 1 review xin | Đo được |
| Sao trung bình + tách chê / khen | trung bình sao review xin; % ở 1–3★ | Tính ra |
| Xu hướng ▲ / ▼ | 90 ngày gần nhất so với trước (khi có ngày) | Tính ra |
| **App nào đã có** | Feature Gap đọc mô tả: ✅ có · ⬜ không thấy · · chưa đọc | Đo được (mô tả) |
| Tín hiệu trả tiền | 3 chấm, 35.3 | Tính ra |
| Cỡ việc | S / M / L / ?, 35.4 | Ước tính |
| Câu trích | 3 câu + link | Đo được |

### 35.3 · Tín hiệu trả tiền (thay cho "revenue impact")

Không ước doanh thu. 3 chấm, đọc từ dữ liệu đã có, không gọi store thêm:

| Chấm | Xanh khi |
|---|---|
| 💬 Nói sẽ trả | ≥ 2 review trong nhóm có *would pay, I'd pay, take my money, worth paying, upgrade to premium if* |
| 💰 Chợ đang thu tiền | ≥ 1 app **đã có** tính năng này mà có IAP / gói tháng (`iap_cache`) → người ta đang trả cho đúng thứ này |
| 👥 Đè lên nhiều người | tổng số rating của các app bị xin ≥ 100.000 (quy ước ShotMatic, sửa được) |

### 35.4 · Cỡ việc (ước tính, có thể sửa)

- Bảng tra tay khoảng 40 tính năng hay gặp: **S** (dark mode, export CSV, thêm cài đặt, sắp xếp) · **M** (widget, nhắc
  lịch, offline cơ bản, nhập file) · **L** (sync nhiều máy, bản web / desktop, cộng tác, AI, tích hợp dịch vụ ngoài).
- Không có trong bảng → **?**. Anh bấm chip để sửa, lưu theo tên tính năng.
- Luôn nhãn **Ước tính**. Không dùng Cỡ việc trong điểm chính, chỉ để lọc "việc nhỏ, nhiều người xin".

### 35.5 · Điểm "Đáng làm" /100 + 4 nhóm kết luận

Điểm dùng để xếp, kiểu thanh "Smartlist value" của Pendo:

| Phần | Điểm | Đo bằng |
|---|---|---|
| Nhiều người xin | 35 | số review xin, so với nhóm nhiều nhất trong lần đọc (trừ hao cỡ mẫu bằng Wilson như mục 34) |
| Xin ở nhiều app | 25 | % app bị xin |
| Chưa ai làm | 25 | % app **không thấy** trong mô tả. App "chưa đọc" không tính |
| Có tín hiệu tiền | 15 | 5 điểm mỗi chấm xanh ở 35.3 |

Phần chưa đo được thì **bỏ ra và chia lại**, không cho 0 (luật mục 24.4). Dưới bảng, 4 khối do code rút:

- 🕳 **Cả chợ xin, chưa ai làm:** xin ở ≥ 50% app, ≥ 70% app không thấy. Cơ hội mạnh nhất.
- 🎯 **Việc nhỏ, nhiều người xin:** Cỡ việc S, ≥ 5 người xin. Dễ làm ngay cho app mới.
- ↩️ **App đang bỏ tính năng người ta thích:** loại Mang lại, rơi vào 1 app. Khách để kéo sang.
- 💳 **Muốn trả kiểu khác:** loại Cách trả tiền (lifetime, rẻ hơn). Chỗ chen bằng giá, ghi rõ không phải tính năng.

### 35.6 · Giao diện tab Xin tính năng

Theo skill `tool-chart`, 1 cột từ trên xuống:

1. Câu kết luận: *"Người dùng 5 app này xin nhiều nhất {tính năng} ({n} người), {k}/5 app chưa có"* + 4 ô số (lời xin ·
   tính năng · chưa ai làm · đọc từ N review).
2. **Bảng Requests** kiểu ảnh Pendo: tên + chip loại · số người xin · thanh điểm /100 · chấm app đã có · 3 chấm tiền ·
   chip Cỡ việc. Sắp xếp theo cột. Bấm 1 dòng mở **thẻ bên** (như thẻ tím trong ảnh): câu trích, sao, xu hướng, app có / thiếu,
   link review gốc đã lọc.
3. 4 khối kết luận (35.5), thẻ dọc.
4. Nút: **Gom vào project** (tính năng = item "tính năng nên có", câu trích là bằng chứng) · **Copy Markdown** · **CSV**.

### 35.7 · Nối chỗ khác + MCP

- **So sánh app (mục 20/22):** cột "người dùng xin" (`wishCount`) đổi sang đọc từ hàm mới, bấm vào mở tab này.
- **Tổng kết 27.6:** thêm 1 dòng "Tính năng được xin nhiều nhất".
- **MCP:** tool chỉ đọc `get_feature_requests` (app ids, nước) → danh sách + điểm + câu trích, mọi số kèm nguồn.
  `top wish` ở niche card đọc từ hàm mới.

### 35.8 · Kiểm độ đúng

- Test hàm thuần: tách vế, mẫu phủ định bị loại, "wish it didn't crash" không thành tính năng, đồng nghĩa gộp đúng,
  1 review nhiều lời xin, phần chưa đo không thành 0.
- Kiểm tay **50 review** ngẫu nhiên có mẫu câu: đếm đúng / sai / sót, ghi precision + recall vào trang này. Mục tiêu
  đúng ≥ 85% (ngang mức AI zero-shot của bài báo, nhưng không tốn API).
- Chạy thật 1 niche (5 app habit tracker, Play US, đọc 1–5★). Ghi số + thời gian vào trang này.

## Code ở đâu

| File | Việc |
|---|---|
| `web/src/lib/complaint-rules.ts` | thêm mẫu câu, mẫu phủ định, bảng đồng nghĩa, loại lời xin, bảng Cỡ việc |
| `web/src/lib/feature-requests.ts` | hàm thuần: tách vế, gom, cột 35.2, tín hiệu tiền, điểm, 4 khối |
| `web/src/lib/complaints.ts` | `wishes()` gọi hàm mới (giữ chữ ký cũ cho ComplaintsBlock + MCP) |
| `web/src/lib/review-mining-run.ts` | đọc lời xin ở 1–5★, thêm `requests` vào kết quả |
| `web/src/client/ReviewRequests.tsx` | tab Xin tính năng (bỏ chip "Sắp có" ở `ReviewMining.tsx`) |
| `web/src/mcp/…` | `get_feature_requests` |
| `web/tests/feature-requests.test.ts` | test luật + ngưỡng |

<div class="box box--rules" markdown>
**Luật**

- Không bịa số, không ra số tiền. Thiếu thì ghi "chưa đo"
- "Không thấy trong mô tả" ≠ "app không có"
- Số người xin = số review khác nhau, ghi rõ trong ⓘ
- Cỡ việc luôn là Ước tính, không vào điểm chính
- AI chỉ đặt tên + gộp nhóm, không đếm
- Ngưỡng là quy ước ShotMatic, ghi trong ⓘ. Không hiện số mục trên UI
</div>

<div class="box box--star" markdown>
**Xong khi**

- 5 app thật → bảng Requests có ≥ 10 tính năng, mỗi dòng đủ cột + 3 câu trích, kiểm tay 50 review đạt ≥ 85% đúng
- Lời xin trong review 4–5★ có mặt
- Đọc được ở 960px + 1340px, sáng + tối, English + tiếng Việt
- `npm run check` + `npm run docs:build` xanh
</div>

<div class="box box--danger" markdown>
**Không làm ở mục này**

- Ước doanh thu, ước số người sẵn sàng trả tiền
- Trạng thái Planned / Building / Released như Pendo (mình không phải chủ app)
- Theo dõi lời xin theo lịch
- Đọc lời xin tiếng địa phương (mẫu câu chỉ hiểu tiếng Anh)
- Embedding (để mục 34)
</div>

## Anh chốt (4 câu)

1. **Tab Xin tính năng của Đào review** (không làm trang riêng)? Đề xuất: **có**.
2. Đọc lời xin ở **cả 1–5★** (thêm ~30% lời xin, tốn thêm 1 lần đọc review khen)? Đề xuất: **có**.
3. **Cỡ việc S / M / L** bằng bảng tra tay, nhãn Ước tính? Hay bỏ hẳn cột này? Đề xuất: **giữ, nhưng không vào điểm**.
4. Làm **sau mục 33 (So app)** vì dùng chung cách đọc 1–5★ + khoảng tin, hay trước? Đề xuất: **sau 33**, và như 33 thì
   commit 24–27 trước.
