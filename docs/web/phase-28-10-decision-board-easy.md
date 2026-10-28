# Phase 28.10 · Bàn quyết định nhìn là hiểu: Nên làm không? Keyword phủ dày hay thưa?

> Người dùng mở Bàn quyết định chỉ để biết **2 điều**: (1) keyword này **có nên làm không**, (2) **độ phủ / cạnh tranh**
> của keyword **mạnh hay yếu**. Màn hiện tại bắt đọc 5 trục × 3–4 dòng chữ dẫn chứng + mã `[C1]` + `+ use` mới tự suy ra.
> Làm lại: mỗi keyword mở đầu bằng **2 dòng trả lời** (icon + chữ ngắn), mỗi trục **1 hàng**: icon · mức màu · 1 con số.
> Dẫn chứng, mã nguồn, chấm tay 1–5 vẫn còn nhưng **gập vào "Chi tiết"**.

<span class="chip chip--done">Xong 2026-10-28 · phương án B (2 đèn)</span>

<div class="box box--goal" markdown>
**Hiện có — đối chiếu code ngày 2026-10-28.**

- `web/src/components/DecisionBoard.tsx` (trang Project, gọi từ `ProjectPage.tsx`): mỗi keyword 1 `article`, 5 trục
  (`AXES` trong `web/src/lib/decision-config.ts`: Nhu cầu · Đối thủ yếu · Khả năng thu tiền · Công sức build · ASO ngách).
  Mỗi trục hiện: nhãn + 5 nút 1–5 + "chưa đo" → câu `AXIS_HINT` ("5 = …") → danh sách gợi ý `hintsFor()` dạng
  `[T] Google Trends … + dùng`. Không có dòng nào nói thẳng "nên làm / không", không có mức mạnh–yếu.
- Lúc chưa chấm tay, cả 5 trục ghi "chưa đo" dù dữ liệu **đã có** (Trends 21/100, ★4.5 · 9.1M rating, 7/10 app thu tiền…):
  người dùng tưởng tool chưa đo gì. "Tổng" = cộng điểm tay, chưa chấm thì là 0.
- Điểm v2 (`web/src/lib/score-v2.ts`) **đã có sẵn** cho từng run: yếu tố 0–10 `money · pain · competition · demand · trend
  · reach · fit`, `decision` BUILD / TEST THÊM / BỎ đã áp ngưỡng + độ phủ + cờ, `capped` (lý do bị hạ), `next`.
  `healthSummary()` đã có dải chữ ≥ 7 / ≥ 4 / thấp ("cạnh tranh thưa / vừa / đông", "đang lên / đi ngang / đang xuống").
  Bàn quyết định **không dùng** các số này — `decisionBoard()` trong `web/src/lib/decision.ts` không gọi `scoreV2`.
- Icon nét kiểu Lucide đã có: `web/src/components/SectionIcon.tsx` (`demand`, `competitors`, `money`, `trend`, `verdict`, …).
  Trang Niche đã làm lại theo mockup Codex (vòng điểm, thanh điểm, ô số có icon — `design/ui-27-niche-page/`).
</div>

**Liên quan:** [Phase 28.8](phase-28-8-niche-ui-polish.md) mục C (điểm dễ hiểu ở trang Niche) và
[Phase 28.9](phase-28-9-ai-agent-pro.md) T4 (component gập `Hint` / ⓘ). Làm 28.9 T4 trước thì dùng lại; chưa có thì
dùng `<details>` có sẵn.

## Mục tiêu · cần làm · KHÔNG làm

- **Mục tiêu:** mở bàn, trong **5 giây** đọc được: nên làm không, keyword phủ dày hay thưa, vì sao (1 dòng).
  Đếm được: chữ hiện sẵn trên 1 keyword (chưa mở Chi tiết) giảm từ ~15 dòng xuống **≤ 7 dòng**.
- **Cần làm:** A khối trả lời 2 dòng → B mỗi trục 1 hàng icon + mức + số → C gập dẫn chứng + chấm tay → D chữ EN/VI ngắn.
- **KHÔNG làm:** đổi công thức, trọng số, ngưỡng điểm v2; thêm ngưỡng mới tự bịa; tự quyết BUILD thay người dùng
  (vẫn là **gợi ý**, verdict cuối người dùng bấm); đổi định dạng JSON `niche-radar/decision`, prompt AI, lịch sử bản;
  xoá chấm tay 1–5 hay mã nguồn. Không đụng trang Niche (đã ở 28.8).
- Màn vẫn **1 cột dọc**; chỉ chip / con số ngắn được nằm ngang. Đứng được 960–1920px, không cuộn ngang cả trang.

## Mẫu đích (mô tả chữ — ảnh mockup do Codex vẽ ở bước 0)

```text
pomodoro timer · US                                   ✦ AI   ▾ Chi tiết
┌──────────────────────────────────────────────────────────────────┐
│ 🧭 Nên làm?        🟡 Thử bán trước đã   · bị hạ: mới đo 55%      │
│ 🔎 Độ phủ keyword  🔴 Dày — top 10 có 9.1M rating, 8/10 tên trùng │
└──────────────────────────────────────────────────────────────────┘
📈 Nhu cầu          🔴 Thấp     21/100 · ↓23%
👥 Đối thủ          🔴 Mạnh     ★4.5 · 9.1M rating · cập nhật 10/2026
💰 Thu tiền         🟢 Có       7/10 app thu tiền · $1.39–$39.99
🛠️ Công sức         ⚪ Bạn chấm  [ 1 2 3 4 5 ]
🔤 ASO ngách        🟡 Vừa      Play 250 app · App Store 180 app

Verdict của bạn:  [✅ Làm]  [🟡 Test thêm]  [⛔ Bỏ]   lý do 1 dòng…
```

Emoji trên chỉ để minh hoạ trong tài liệu; giao diện dùng `SectionIcon` + chấm màu, không emoji.

## 0 · Mockup Codex — S

- Viết `design/ui-28-decision-board/codex-brief.md` (style lock lấy từ `design/ui-27-niche-page/codex-brief-mockup.md`,
  màu accent cam hiện tại, chữ EN). 3 phương án: **a** 2 dòng trả lời trong ô nền nhạt + hàng trục dạng list;
  **b** 2 "đèn" lớn trái + list phải (chỉ khi khung ≥ 1200px, hẹp hơn xếp dọc); **c** list trục dạng thanh ngang 0–10.
- Chạy `codex exec` (skill `asset-prompt` tuyến D), nhặt ảnh, người dùng chọn 1. Không tự vẽ SVG/HTML làm mockup.

**Kết quả 2026-10-28 — người dùng chốt phương án B** (nhiều icon, dễ nhìn, dễ biết cần gì). Brief: `design/ui-28-decision-board/codex-brief.md`.

- `option-a.png` — **Answer strip**, 8/10: 2 câu trả lời trong dải nền nhạt, chip lớn; gọn nhất, gần code hiện tại nhất.
- `option-b.png` — **Two lights**, 9/10 (**đề xuất**): 2 đèn tròn lớn có icon + chữ đậm màu, đọc nhanh nhất;
  keyword gập còn 1 hàng (tên · 2 đèn nhỏ · Research →). Ở khung < 1200px 2 đèn xếp dọc.
- `option-c.png` — **Meter rows**, 7.5/10: tiêu đề "Pre-sell test first · Crowded keyword" rất to, trục có thanh 0–10.
  Lỗi: Codex tự thêm câu "Rank these competitors (1 = biggest threat)" — sai nghĩa nút 1–5, không dùng câu này.
- Chung cả 3: header vẽ "Niche Radar" (tên cũ) — chỉ là mockup, code giữ header ShotMatic hiện tại.
  Số trong ảnh lấy từ ảnh màn cũ người dùng gửi; tên keyword và gợi ý "Pre-sell test first" là **ví dụ**.

## A · Khối trả lời 2 dòng ở đầu mỗi keyword — M

**Mục tiêu:** câu hỏi 1 và 2 có đáp án ngay dưới tên keyword, kể cả khi chưa chấm tay.

**Cần làm**

- `decisionBoard()` trả thêm cho mỗi item có `runId`: `scoreV2(db, view)` rút gọn → `{ decision, total, coverage, capped,
  factors: {key, value, trust}[] }` (dựng `view` bằng `getRunView` như `healthOf` ở `web/src/server/app.ts`).
  Không ghi `recordScore` ở đây (chỉ đọc).
- Dòng **Nên làm?** — ưu tiên: verdict tay đã lưu → verdict AI → `decision` điểm v2 (ghi nhỏ "gợi ý từ số đo").
  Chữ: BUILD = "Nên làm", TEST THÊM = "Thử bán trước đã", BỎ = "Bỏ qua", `null` = "Chưa đủ số — thiếu {yếu tố}".
  Có `capped` → thêm 1 cụm ngắn "bị hạ: …" (lấy nguyên chữ `capped[0]`, chi tiết vào ⓘ).
- Dòng **Độ phủ keyword** — mức lấy từ yếu tố `competition` của điểm v2 theo **đúng dải đang có** trong `healthSummary`
  (≥ 7 thưa = xanh · ≥ 4 vừa = vàng · < 4 dày = đỏ); số kèm: tổng rating top 10 (đã có `topRatingsSum`) + "{n}/{total}
  tên app trùng keyword" (đã tính trong `hintsFor` mục ASO). `competition` chưa đo → xám "Chưa đo — chạy lại nguồn store".
- Tách hàm thuần `web/src/lib/decision-summary.ts` (nhận item + scoreV2 rút gọn + bản tay/AI → 2 dòng chữ + mức màu)
  để test được không cần DB.

**Tiêu chí kiểm được:** keyword có run nhưng chưa chấm tay vẫn hiện 2 dòng có mức; keyword chưa tra Research hiện
"Chưa tra Research" + nút "Tra →" (dùng lại hành động bảng long-tail), không hiện "chưa đo" × 5.

## B · Mỗi trục 1 hàng: icon · mức · 1 con số — M

**Mục tiêu:** quét dọc 5 hàng là thấy trục nào kéo xuống.

**Cần làm**

- Hàng = `SectionIcon` + nhãn ngắn + chấm màu + chữ mức 1 từ + **1 con số chính** (`truncate` + `title` đủ câu).
  Icon: Nhu cầu `trend` · Đối thủ `competitors` · Thu tiền `money` · Công sức icon mới (Codex vẽ cùng bộ, thêm vào
  `design/icons/sections/`) · ASO `demand`.
- Nguồn mức (không ngưỡng mới): Nhu cầu ← yếu tố `demand` (+ chữ `trend` "đang lên/xuống"); Đối thủ ← `competition`;
  Thu tiền ← `money`; Công sức ← `fit` nếu đã tự chấm, chưa thì "Bạn chấm"; ASO ← dùng điểm tay nếu có, chưa có thì
  chỉ hiện số app khớp, **không tô màu** (chưa có yếu tố v2 tương ứng — xem câu hỏi mở).
- Đã chấm tay → hàng hiện điểm tay `4/5` thay mức gợi ý; lệch AI ≥ 2 giữ nền vàng + chữ "lệch AI".
- Nhãn trục đổi ngắn, thuận chiều đọc: "Đối thủ yếu" → **"Đối thủ"** (mức: Yếu = xanh / Mạnh = đỏ),
  "Khả năng thu tiền" → **"Thu tiền"**, "Công sức build" → **"Công sức"**. Khoá `AXES` giữ nguyên.
- Tổng trên đầu: bỏ "Tổng 0 · 0/5 trục có dữ liệu" khi chưa chấm; đã chấm hiện "Bạn chấm 14/25".

## C · Gập dẫn chứng và chấm tay vào "Chi tiết" — S

- Mỗi hàng trục có nút ▾ mở: 5 nút 1–5, câu `AXIS_HINT`, gợi ý `[mã] … + dùng`, chọn mã nguồn, ô lý do, dòng AI —
  **y như hiện tại**, chỉ chuyển vào vùng gập. Nút "▾ Chi tiết" ở đầu keyword mở cả 5 trục cùng lúc.
- Mặc định gập. Mở tự động khi: trục có mã bị gạch (`bad`), lệch AI ≥ 2, hoặc người dùng vừa bấm "Dùng điểm AI làm nháp".
  Không gập lỗi / cảnh báo.
- Câu giới thiệu dài đầu bàn ("Chấm từng keyword theo 5 trục …") rút còn 1 dòng + ⓘ.
- Thanh "Copy prompt cho AI · token · Dán JSON AI · Pro" giữ, nhưng gom phụ (token, Dán JSON) vào menu ⋯ như khối AI 28.

## D · Chữ EN/VI ngắn — S

- Thêm khoá mới vào `web/src/locales/en-text.ts` (VI là khoá). Mỗi nhãn ≤ 3 từ, mỗi số ≤ 1 dòng ở 960px.
  EN đề xuất: "Worth building?" · "Keyword crowding" · "Build it" · "Pre-sell test first" · "Skip" · "Not enough data" ·
  "Thin / Medium / Crowded" · "Demand / Competitors / Revenue / Effort / Niche ASO" · "Low / Mid / High" · "You score".
- Không viết hoa toàn câu, không ghép câu dài bằng "·" quá 3 cụm.

**File đụng:** `web/src/components/DecisionBoard.tsx`, `web/src/lib/decision.ts`, `web/src/lib/decision-config.ts`
(nhãn), mới `web/src/lib/decision-summary.ts`, `web/src/components/SectionIcon.tsx` (icon Công sức),
`web/src/locales/en-text.ts`, `design/ui-28-decision-board/`.

**Test `web/tests/`:** `decision-summary.test.ts` — ưu tiên tay > AI > v2; `decision null` → "Chưa đủ số";
`competition` 7 / 4 / 3 / null → thưa / vừa / dày / chưa đo; keyword không run. Giữ xanh test decision hiện có.
`npm run check` xanh; mở trang Project ở **960px và 1340px**, EN + VI, project có keyword dài + keyword chưa tra,
screenshot đã Read: không cuộn ngang, mỗi keyword chưa mở Chi tiết ≤ 7 dòng.

## Thứ tự làm · độ lớn

1. **0 — S:** mockup Codex, người dùng chọn phương án.
2. **A — M:** API + `decision-summary.ts` + khối 2 dòng — ra giá trị ngay (trả lời được 2 câu hỏi).
3. **B — M:** hàng trục gọn.
4. **C — S:** gập dẫn chứng.
5. **D — S:** soát chữ EN/VI + screenshot 960/1340.

S/M/L là độ lớn tương đối, **chưa đo thời gian**.

## Kết quả 2026-10-28

- A: `decisionBoard()` trả `signals` mỗi keyword (điểm v2 chỉ đọc, không ghi lịch sử) → 2 đèn **Worth building?** (tay > AI > gợi ý số đo, kèm "bị hạ: …") và **Keyword crowding** (dải ≥ 7 / ≥ 4 / thấp của yếu tố cạnh tranh, kèm tổng rating top 10 + số tên trùng keyword). Keyword chưa tra → "chưa tra Research" + nút **Tra →** (cùng hành động bảng long-tail).
- B: 5 hàng trục icon · chấm màu · chữ mức · 1 số; đã chấm tay hiện chip "Bạn n/5"; lệch AI giữ nền vàng. Icon Công sức = cờ lê Lucide.
- C: dẫn chứng + chấm 1–5 + mã nguồn gập trong từng trục; tự mở khi lệch AI / mã bị gạch / vừa bấm "Dùng điểm AI làm nháp". Trần token cất vào menu ⋯.
- Kiểm: `decision-summary.test.ts` + test bàn cũ, 472 test xanh, tsc + eslint sạch; xem project #4 (5 keyword) ở 1340px và 960px, không cuộn ngang, thẻ gập còn 3 dòng.
- Còn mở (theo câu hỏi bên dưới, mặc định giữ): ASO ngách không tô màu, "độ phủ" = nhiều app chiếm keyword.

## Rủi ro

- **Gợi ý v2 bị hiểu là quyết định:** luôn ghi "gợi ý từ số đo", verdict cuối vẫn là 3 nút của người dùng.
- **Hai nguồn điểm lệch nhau** (v2 0–10 vs chấm tay 1–5): đã chấm tay thì hàng hiện điểm tay, gợi ý v2 lùi vào Chi tiết.
- **`scoreV2` gọi cho mọi keyword làm bàn chậm** khi project nhiều keyword: đo thời gian tải bàn trước/sau;
  chậm thì chỉ tính cho keyword đang hiện.
- **Gập mất thông tin cần sửa:** luật mở tự động ở mục C.

## Câu hỏi còn mở cho người dùng

- Trục **ASO ngách** chưa có yếu tố v2 → tạm chỉ hiện số, không màu. Có muốn thêm ngưỡng riêng (vd số app khớp tên)
  không? Thêm ngưỡng = đổi cách chấm, cần anh duyệt. Mặc định: không thêm.
- Dòng "Độ phủ keyword" dùng yếu tố **cạnh tranh** (tổng rating top 10). Anh muốn "độ phủ" nghĩa là **nhiều app chiếm
  keyword** (đúng cái này) hay **nhiều người tìm keyword** (Nhu cầu)? Mặc định: nhiều app chiếm.

[← Phase 28.9 · AI Agent xịn](phase-28-9-ai-agent-pro.md) · [Mục lục Web](index.md)
