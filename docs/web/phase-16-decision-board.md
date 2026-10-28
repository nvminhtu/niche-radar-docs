# Phase 16 · Bàn quyết định long-tail + đo nhu cầu Pro

> Trả lời câu **"chọn được 5 long-tail rồi, xong sao nữa?"**. Trong một Project, đặt các keyword cạnh nhau, chấm theo
> **rubric cố định 5 trục**, mỗi điểm phải có dẫn chứng lấy từ dữ liệu. Ra **BUILD / TEST THÊM / BỎ** cho từng keyword.
> AI chấm qua **Copy prompt → dán kết quả JSON ngược vào app**. Cùng lúc, gắn **nút Pro giả (fake-door)** để đo xem có
> ai muốn trả tiền không, trước khi đi tới Version 10.

<span class="chip chip--done">Xong 2026-10-26 · fake-door live trên demo · GA4 chờ VITE_GA_ID</span>

<div class="box box--goal" markdown>
**Vì sao làm.** Review sản phẩm ngày 2026-10-26 chỉ ra đoạn trống giữa "đẩy keyword vào Project" và "quyết định làm app":

- Project hiện chỉ có 3 chip (đang xem / ứng viên / loại), 1 dòng kết luận và ghi chú tự do. Không rubric, không so
  các keyword với nhau. Anh phải tự nhớ tiêu chí.
- [Phase 15](phase-15-export.md) đã có gói cho LLM, nhưng **chỉ một chiều**: anh dán ra AI, kết quả AI không quay lại
  app được.
- [Phase 43](phase-43-evidence-presell.md) có vòng BUILD / TEST THÊM / BỎ, nhưng cho **1 niche đã chọn**. Bước chọn
  1 trong N long-tail chưa có công cụ.
- [Phase 44](phase-44-compare-niche.md) so 2–4 **niche** (cả Research), không có verdict. Phase này so các **keyword
  trong 1 Project**, có verdict + dẫn chứng.
- Bán Pro nằm ở [Version 10](version-10.md) (Phase 31–27.7), sau App Mac. Đi tới đó mới biết có ai trả tiền là rủi ro
  lớn. Fake-door rẻ, đo được ngay trên demo site đang live.
</div>

**Cần xong trước:** [Phase 15](phase-15-export.md) (đã merge main: dataset chung, gói LLM có mã nguồn `[C1]`, `[P2]`…).
Phase 18 · 13 · 14 không chặn — xong thì rubric có thêm dữ liệu.

## Chạy thế nào

```mermaid
flowchart LR
  P[Project<br/>2–8 keyword] --> B[Bàn quyết định<br/>bảng rubric 5 trục]
  B --> M[Tự chấm<br/>tay, ghi dẫn chứng]
  B --> C[Copy prompt<br/>gói LLM Phase 15 + rubric]
  C --> AI[Claude / ChatGPT<br/>anh tự dán]
  AI --> J[Dán JSON ngược lại]
  J --> K{Kiểm JSON<br/>schema + mã nguồn có thật}
  K -->|đạt| B
  K -->|sai| E[Báo dòng lỗi<br/>không lưu]
  M & B --> V[Verdict từng keyword<br/>BUILD · TEST THÊM · BỎ]
  V --> S[Lưu vào Project<br/>kết luận + lý do]
  V -->|BUILD| X[Phase 43<br/>evidence pack]
```

## Làm gì

### Phần A · Bàn quyết định (miễn phí, chạy ngay)

| | |
|---|---|
| :material-table-check: **Bảng rubric** | tab mới trong trang Project: mỗi keyword 1 hàng, 5 cột trục + cột verdict. 5 trục, chấm 1–5: **Nhu cầu** · **Đối thủ yếu** · **Khả năng thu tiền** · **Công sức build** (5 = ít công) · **Khả năng ASO ngách**. Bảng xếp dọc theo keyword, đọc được ở 1340px và 375px |
| :material-database-search: **Dữ liệu gợi ý mỗi ô** | ô hiện sẵn số có trong DB làm dẫn chứng: Trends 12 tháng + số gợi ý autocomplete (Nhu cầu) · sao TB top 10, số review, lần cập nhật cuối (Đối thủ yếu) · nhãn mô hình tiền, gói IAP, TrustMRR (Thu tiền) · điểm cơ hội keyword, số app khớp tên (ASO). **Công sức build** không có dữ liệu → người / AI tự chấm, bắt buộc ghi lý do (dùng lại trục "Hợp sức mình" của điểm v2) |
| :material-pencil: **Tự chấm tay** | bấm ô → chọn 1–5 + chọn dẫn chứng từ danh sách mã nguồn của gói Phase 15, hoặc gõ lý do. Không có dẫn chứng → ô ghi **chưa đo**, không tính vào tổng |
| :material-content-copy: **Copy prompt** | nút ở đầu bảng: ghép gói LLM Phase 15 (phạm vi Project, trần 8k / 32k) + rubric + luật dẫn chứng + định dạng JSON phải trả. Prompt ép: mỗi điểm 1 dẫn chứng có mã nguồn, không có thì `"chưa đo"`; chọn **1 BUILD, tối đa 1 TEST THÊM**, còn lại BỎ; 2 rủi ro lớn nhất của keyword BUILD + cách kiểm rẻ nhất (< $50, < 1 tuần); chỗ nào dữ liệu chưa đủ để kết luận |
| :material-clipboard-arrow-down: **Dán JSON ngược** | ô dán kết quả AI → kiểm theo schema `niche-radar/decision` v1: đúng keyword trong Project, điểm 1–5, mỗi dẫn chứng trỏ mã nguồn **có thật** trong gói đã copy. Dẫn chứng không có thật → ô đó gạch đỏ "dẫn chứng không có trong dữ liệu", điểm không tính. JSON sai cú pháp → báo dòng lỗi, không lưu gì |
| :material-compare: **AI vs tay** | khi có cả 2 bản chấm, ô lệch ≥ 2 điểm tô vàng để anh xem lại. Bản lưu cuối là bản anh chốt |
| :material-scale-balance: **Verdict + lưu** | mỗi keyword: BUILD / TEST THÊM / BỎ + 1 dòng lý do (bắt buộc với BỎ). Lưu vào kết luận Project + trạng thái item (BỎ = loại có lý do, khớp [Phase 22](phase-22-project-manage.md)). Mỗi lần chấm lưu thành 1 bản, xem lại được bản cũ |
| :material-rocket-launch: **Sang Phase 43** | keyword BUILD → nút "Làm evidence pack" mở đúng luồng [Phase 43](phase-43-evidence-presell.md) |
| :material-file-export: **Xuất** | bảng rubric + verdict + dẫn chứng đi theo hộp Xuất chung của Phase 15 (Markdown + CSV `decisions`) và gói `.niche.json` |

### Phần B · Fake-door đo nhu cầu Pro (chưa thu tiền)

**Fake-door** = nút cho tính năng chưa có. Người bấm thấy "đang làm, để email nhận khi mở" — đo được có ai muốn
trước khi làm thật.

| | |
|---|---|
| :material-lock-open-variant: **2 nút Pro** | (1) **"Chấm bằng AI 1 bấm"** cạnh nút Copy prompt · (2) **"Báo tôi qua email khi niche đổi"** ở khối Theo dõi của Project. Nhãn `Pro · sắp có` |
| :material-form-select: **Hộp khi bấm** | nói thật: tính năng chưa có, đang đo nhu cầu. Hỏi 1 câu giá **"Bạn sẵn sàng trả bao nhiêu?"** (Không trả · ~$5/tháng · ~$10/tháng · ~$29 một lần · Khác) + ô email. Không có nút mua, không lấy thẻ |
| :material-email-plus: **Email** | Mailchimp như demo site (`PRODUCT=niche-radar`) + tag `pro-<tính năng>` và tag mức giá đã chọn |
| :material-chart-bar: **Đếm** | GA4 sự kiện `pro_interest_click` (tính năng) và `pro_interest_email` (tính năng, mức giá). Gắn `VITE_GA_ID` cho demo site (việc còn treo từ Phase 50). Bản chạy trên máy không gửi GA — chỉ ghi đếm vào DB của anh |
| :material-ruler-square: **Ngưỡng ghi trước** | trước khi bật, anh ghi ngưỡng vào trang này (đề xuất để anh sửa: sau 4 tuần ≥ 20 email Pro **và** ≥ 30 % trong số đó chọn mức có trả tiền) — đạt thì mở [Phase 31](phase-31-money-model.md) sớm, không chờ App Mac |
| :material-table-eye: **Kết quả** | bảng ở cuối trang này: ngày bật, số click, số email, phân bố mức giá, nguồn (GA4 + Mailchimp) + ngày đo. Chưa có số → ghi **chưa đo** |

<div class="box box--rules" markdown>
**Luật**

- Tool **không gọi AI** ở phase này: Copy prompt + dán JSON là đường duy nhất. AI chạy trong app = tính năng Pro, chỉ
  làm khi fake-door đạt ngưỡng
- Không bịa dẫn chứng: điểm không có mã nguồn có thật trong gói → không tính, ghi `chưa đo`
- Không có "điểm tổng bí ẩn": tổng = cộng 5 trục, ô `chưa đo` không cộng, ghi rõ "3/5 trục có dữ liệu"
- Fake-door nói thật là chưa có, không thu tiền, không hứa ngày ra
- Ngưỡng ghi trước khi bật; đổi sau khi thấy số → ghi đỏ "đổi sau khi thấy số" (như Phase 43)
- Giá đối thủ trong review (credit $9, $19, $5.99…) **chưa vào `money.md`** — Phase 31 mở từng trang pricing đo lại có
  link + ngày
- Schema mới: `decision` đi theo `.niche.json` + tăng `schema_version` của Export + ghi CHANGELOG
</div>

<div class="box box--star" markdown>
**Xong khi**

- 1 Project thật 5 keyword: chấm tay đủ 5 trục, ra verdict, lưu, mở lại thấy đúng
- Copy prompt → dán vào Claude → dán JSON ngược: lưu được, 5/5 keyword đúng tên, mọi dẫn chứng trỏ mã nguồn có thật.
  Test thêm: JSON có 1 mã nguồn bịa → ô đó bị gạch, không tính điểm
- JSON sai cú pháp / thiếu keyword / điểm ngoài 1–5 → báo lỗi đúng dòng, không ghi DB (test tự động)
- `.niche.json` xuất → nhập lại giữ đủ bản chấm + verdict
- 2 nút fake-door chạy trên demo site live: bấm → hộp → email vào Mailchimp có đúng tag; GA4 Realtime thấy 2 sự kiện
- Bảng rubric + hộp fake-door đọc được ở 1340px và 375px, screenshot đã Read
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Gọi AI trong app (Decision Engine Pro) — chỉ khi fake-door đạt ngưỡng; ghi ứng viên ở [Version 12](version-12.md)
- Gửi email báo thay đổi thật — [Phase 42](phase-42-tracking.md) làm phần báo trong app, email sau [Version 9](version-9.md)
- Niche → Spec / ASO (PRD tóm tắt, title / subtitle / keyword field), báo cáo chia sẻ PDF / link — ứng viên Version 12
- Thanh toán, license, paywall thật — [Version 10](version-10.md)
- So nhiều niche (cả Research) — [Phase 44](phase-44-compare-niche.md)
- Đổi rubric theo từng người (trọng số tuỳ chỉnh) — dùng bản cố định trước, đổi khi có người xin
</div>

## Đã làm (2026-10-26)

**Phần A · Bàn quyết định** — khối mới trong trang Project, dưới bảng long-tail.

- Mỗi keyword 1 khối xếp dọc, 5 trục chấm 1–5. Mỗi ô có **gợi ý dẫn chứng** lấy từ DB (Trends + mã `[T]`, đối thủ top 3
  `[C…]`, mô hình tiền + điểm `[S…]`, keyword gốc `[K…]`, số đối thủ có đủ chữ của keyword trong tên). Bấm **+ dùng** là gắn
  mã + lý do vào ô. Công sức build không có số → ghi lý do; nếu đã tự chấm Hợp sức mình ở điểm v2 thì hiện làm gợi ý.
- **Copy prompt cho AI**: prompt rubric + `brief.md` phạm vi Project của Phase 15 + `schema.md`, mặc định trần 32k
  (project 5 keyword không vừa 8k: ~8.900 token sau khi cắt hết mức — hộp báo "vẫn vượt trần").
- **Dán JSON AI**: bóc JSON khỏi chữ thừa và khung code của AI, kiểm schema `niche-radar/decision` v1. Sai cú pháp → báo đúng dòng
  (kể cả dấu phẩy thừa trước `]` mà V8 không báo vị trí). Thiếu keyword, keyword lạ, điểm ngoài 1–5, 2 BUILD, > 1 TEST THÊM,
  BỎ không lý do, trục có số mà không dẫn mã → lỗi, **không ghi gì**. Mã nguồn không có trong dữ liệu → ô bị gạch, không cộng.
- **Tổng** = cộng các trục có dữ liệu, ghi "4/5 trục có dữ liệu". Ô lệch ≥ 2 điểm giữa bản tay và bản AI tô vàng.
- **Lưu bản chốt** (tuỳ chọn ghi verdict vào Kết luận) · **Dùng điểm AI làm nháp** (bỏ ô bị gạch) · **Lịch sử chấm**: mọi
  bản tay / AI, xem lại bản cũ ở chế độ chỉ xem. Keyword BUILD có nút **Làm evidence pack** xám · Phase 24.
- Xuất: bảng `decisions` trong CSV / JSON phạm vi Project (`schema_version` 2) · mục Bàn quyết định trong báo cáo `.md` ·
  `.niche.json` mang bản chấm, nhập lại 2 lần không nhân đôi. Bản chấm **không** vào gói cho AI (AI chấm độc lập).
- Bảng `decisions` + `pro_interest` (migration 0016).

**Phần B · Fake-door** — 2 nút `Pro · sắp có`: **Chấm bằng AI 1 bấm** (cạnh Copy prompt) và **Báo tôi qua email khi niche đổi**
(khối Theo dõi định kỳ). Hộp nói thật "chưa có, không thu tiền, không hứa ngày ra", hỏi mức giá, không nút mua.

- Bản demo: GA4 `pro_interest_click` / `pro_interest_email` (chỉ chạy khi build có `VITE_GA_ID` — **chưa gắn**) + email vào
  Mailchimp. JSONP của Mailchimp không gắn được tag → tính năng + mức giá ghi vào trường PRODUCT dạng
  `niche-radar|pro-ai-score|~$10/tháng`; lọc người ShotMatic bằng "PRODUCT contains niche-radar".
- Bản trên máy: chỉ đếm vào DB (`GET /api/pro-interest`), không gửi đi đâu.
- Demo có project mẫu "Mẫu: app tiện ích cá nhân" (habit tracker · budget tracker · pomodoro timer), chưa chấm sẵn:
  [niche-radar-demo.pages.dev/projects/4](https://niche-radar-demo.pages.dev/projects/4).

**Chạy thật** (bản sao DB thật, project RAM 5 keyword: ram issue · over ram · ram ios · not enough ram · ai bubble shooter game):
gợi ý đủ 5 trục cho cả 5 keyword, 375 mã nguồn chọn được · Copy prompt 32k = ~17.000 token, không cắt · dán JSON có dấu phẩy thừa
→ "Dòng 7: ký tự ] không đúng chỗ (dấu phẩy thừa?)", không lưu · dán JSON 5 keyword có 1 mã bịa `C999` → lưu, ô "ram ios · Đối thủ
yếu" bị gạch · dùng điểm AI làm nháp, sửa Nhu cầu "ram issue" 2 → 4 → lưu, mở lại thấy đúng, ô đó tô vàng, Kết luận ghi đủ 5
verdict · `.niche.json` có 2 bản chấm · CSV có `decisions.csv` · fake-door bản máy đếm 1 bấm + 1 chọn giá. Xem ở 1340px và 375px,
không tràn ngang. 288 test xanh (thêm `tests/decision.test.ts`, 11 test).

**Còn lại (của anh):** gắn `VITE_GA_ID` rồi `npm run demo:deploy` để GA4 đếm · thử 1 email thật trên demo, xem Mailchimp có dòng
PRODUCT đúng · sửa ngưỡng dưới đây nếu muốn, trước khi có số.

## Kết quả fake-door

| Ngày bật | Tính năng | Click | Email | Chọn có trả tiền | Nguồn + ngày đo |
|---|---|---|---|---|---|
| 2026-10-26 | Chấm bằng AI 1 bấm | chưa đo | chưa đo | chưa đo | GA4 chưa gắn · Mailchimp chưa đọc |
| 2026-10-26 | Báo email khi niche đổi | chưa đo | chưa đo | chưa đo | GA4 chưa gắn · Mailchimp chưa đọc |

**Ngưỡng (ghi trước khi bật, 2026-10-26):** sau 4 tuần (tới 2026-11-23) ≥ 20 email Pro **và** ≥ 30 % trong số đó chọn mức có trả tiền → mở Phase 31 sớm. Đây là mức đề xuất trong plan — anh sửa được trước khi có số; sửa sau khi thấy số thì ghi đỏ "đổi sau khi thấy số".
