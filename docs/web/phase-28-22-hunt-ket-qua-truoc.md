# 3.3 · Phiên AI Agent: kết quả lên đầu, người dùng chỉ duyệt (Phase 28.22)

> Trang phiên AI Agent (`/hunt/:id`) đang hiện tiến độ 3 lần, có 2 nút chính cùng lúc, và lặp lại cùng một con số ở nhiều
> chỗ. Kết quả người dùng cần (niche nào nên làm) lại bị đẩy xuống dưới. Phase này xếp lại trang: **AI đề xuất gì** nằm
> trên cùng, kèm **1 nút duyệt**. Năm nút lấy số lẻ gom thành 1 nút. Panel AI chỉ còn nhật ký và ô nhập. Logic chạy bước,
> Autopilot, API giữ nguyên.

<span class="chip chip--todo">M1–M4 code xong 2026-11-05 · chưa commit · chưa chạy thật nút Fill</span>

!!! note "Tiến độ (2026-11-05)"
    - **Đã có:** `FlowProgress.tsx` (7 chấm, khung < 38rem ẩn tên dưới chấm) · `HuntPickCard.tsx` (vòng điểm, nút Fill N missing
      factors chạy `fillPlan` lần lượt) · `HuntCandidateList.tsx` (5 nhóm, Keep / Drop có lý do) · `AutopilotBar.tsx` gọn
      (thẻ đang tra + Pause; dừng / xong = 1 dòng, lý do cũ ẩn khi dữ liệu đã qua Health check) · `HuntChat.tsx` đầu 1 dòng + ⋯ ·
      chip lệnh nằm trên ô nhập. Chặng lên kế hoạch thì thẻ bước lên ngay dưới AI's pick, nút AI ở đó là nút chính.
    - Bảng sức khoẻ chỉ còn ở chế độ Tuỳ chỉnh (giữ cột "Điểm của bạn"). Khối `AnswerRow` không hiện ở trang phiên (trùng điểm).
    - **Đã soát:** `npm run check` xanh (692 test, 7 test mới `tests/hunt-pick.test.ts`) · phiên #42 ở 1340px sáng + tối và 960px,
      không cuộn ngang, ⋯ và Chi tiết từng yếu tố mở được, console không lỗi.
    - **Chưa làm:** bấm thật nút Fill (gọi review + Trends + 1 lượt AI) · soát tiếng Việt · soát lúc Autopilot đang chạy (bản B) bằng phiên mới.

## 1 · Vì sao làm — soát trang ngày 2026-11-05

Soát phiên `mac extra dock` (8 ứng viên, 2 giữ, 3 đang tra, 3 chưa tra, 4 loại), bản sáng + tối, lúc Autopilot dừng và lúc đang chạy.

| # | Lỗi | Ở đâu trong code |
|---|---|---|
| 1 | Tiến độ hiện 3 lần: chip ở banner vàng · khối 2 chặng "Research niche / Plan the app" · thẻ "STEP 4/7 YOU ARE HERE". Số còn lệch: banner ghi 3/4, thẻ ghi 4/7 | `AutopilotBar.tsx`, `HuntFlow.tsx` |
| 2 | Banner vàng "Autopilot stopped" vẫn hiện trong khi 3 niche đang tra, trông như báo lỗi | `AutopilotBar.tsx` |
| 3 | 8 niche hiện 2 lần (Health table + dãy chip). Điểm 5.3 hiện 3 lần. "40% of the weight measured" hiện 3 lần. "Research the rest (3)" có 2 nút | `HuntFlow.tsx` HealthTable, `HuntPage.tsx` Chip, `AnswerRow`, `HealthBlock` |
| 4 | Yếu tố chưa đo rải thành 5 nút lẻ (Read 1–3★ reviews · Retry Google Trends ×2 · Let AI score it ×2), người dùng phải bấm 5 lần | `HealthBlock.tsx` FactorAction |
| 5 | Hai nút chính cùng lúc: "Continue" và "AI adds long-tail keywords" | `AutopilotBar.tsx` + `HuntFlow.tsx` |
| 6 | Nửa trên panel AI toàn là cấu hình (Runs on · email · Team · Chat 1 · New chat 1/2 · Default/Custom · AI rules), ô nhập cao mà trống | `HuntChat.tsx` |
| 7 | Dòng niche đang tra ở đầu trang bị cắt chữ còn "Rese…" ở cột 800px | `HuntPage.tsx` RunningList |

Các app có AI làm tốt (Perplexity, Cursor Agent, Linear, Superhuman) đều theo chung 4 luật: kết quả trước · AI làm, người
duyệt · mỗi trạng thái hiện 1 lần · chọn model là việc phụ.

## 2 · Mockup đã chốt

Brief + ảnh: `design/ui-hunt-result-first/` (Codex sinh 2026-11-05). Anh chốt **A + B**, tức cùng 1 trang ở 2 trạng thái.

- **A, AI dừng chờ duyệt** (`option-a.png`): tên phiên → thanh 7 chấm → thẻ **AI's pick** (niche · vòng điểm · gợi ý · lý do ·
  "2 of 7 factors measured" · nút chính **Fill 5 missing factors** · link "Pick this and plan the app →" · "Factor details ▾")
  → danh sách ứng viên 1 cột chia nhóm → panel AI = nhật ký + ô nhập.
- **B, AI đang chạy** (`option-b.png`): thay banner vàng bằng thẻ "AI is researching N candidates" (đủ tên, % nguồn, nút Pause),
  thẻ AI's pick vẫn hiện bên dưới, ghi "so far".

Khi code, sửa 3 chỗ Codex vẽ sai: tên bước dùng đúng 7 tên thật · lúc AI chạy thì nút "Fill missing" bị khoá (để chỉ còn
1 nút chính) · màu nút theo bảng màu A của Phase 28.21 (nút xanh `--accent-solid`, cam chỉ ở thanh điểm / gợi ý TEST MORE).

## 3 · Làm gì

### M1 · Đầu trang: 1 thanh tiến độ + thẻ trạng thái

- `FlowProgress` mới: 7 chấm trên 1 hàng, nhãn 2 chặng ở trên, tên bước dưới chấm, chữ "Step n of 7" ở phải. Bấm chấm
  nào thì mở thẻ bước đó (như chip cũ). Bỏ khối 2 chặng của `HuntFlow` và hàng chip trong `AutopilotBar`.
- `AutopilotBar` lúc **đang chạy**: thẻ xanh dịu gộp luôn `RunningList`. Mỗi niche đang tra 1 hàng, tên đủ chữ (`truncate` + `title`),
  có "2/3 sources" + thanh %. Nút phụ Pause (= Dừng cũ).
- `AutopilotBar` lúc **đã dừng**: không còn banner vàng 2 viền. Còn 1 dòng xám "Autopilot paused · lý do" + link "Continue".
  Nút chính của trang lúc này là nút trên thẻ AI's pick.
- Thẻ bước của `HuntFlow` (hình + "STEP n/7" + nút) gập vào "Manual steps ▾". Mặc định đóng khi đã có AI's pick, mở khi chưa có.

### M2 · Thẻ AI's pick + gom việc lẻ

- `PickCard` mới cho niche giữ có điểm cao nhất (hoặc niche đang chọn `?c=`). Gồm tên to · vòng điểm x/10 · chip gợi ý bằng
  lời (`DECISION_PLAIN`) · lý do (`note`) · "n of 7 factors measured".
- Nút chính **Fill N missing factors**: lib thuần `fillPlan(factors, aiSaves)` → danh sách việc không trùng. Đau → đọc review
  1–3★. Nhu cầu + Xu hướng → chạy lại Trends 1 lần. Tiền / Cạnh tranh → chạy lại 2 store. Tiếp cận khách + Hợp sức mình
  → 1 câu gửi AI chấm cả hai. Chạy lần lượt, có chữ "Filling 2/4…", xong thì tải lại điểm. Khoá khi AI đang chạy hoặc khi
  Autopilot đang chạy.
- Link "Pick this and plan the app →" = nhảy tới bước Feature brief (như nút "Bước tiếp" cũ).
- "Factor details ▾" mở `AnswerRow` + `HealthBlock` như cũ. Khối chi tiết không còn nằm mở sẵn dưới danh sách.

### M3 · Danh sách ứng viên 1 cột

- `CandidateList` mới thay dãy `Chip` + `HealthTable` (bảng sức khoẻ không còn hiện lần 2 trong thẻ Health check).
  Nhóm Kept · Researching · Not researched · Dropped (n, gập). Mỗi hàng: ★ · tên (`truncate`) · điểm hoặc thanh % hoặc "not researched"
  · chip gợi ý · Keep / Drop. Bấm tên = chọn niche cho thẻ AI's pick.
- Drop vẫn hỏi lý do (bắt buộc), như form cũ trong `Detail`.
- "Research the rest (n)" chỉ còn 1 nút, ở đầu nhóm Not researched. Ô "+ add keyword" ở cuối danh sách.

### M4 · Panel AI gọn

- Đầu panel còn 1 dòng: "AI Agent · {AI đang chạy} · trạng thái" + nút ⋯. Bấm ⋯ thì mở account, tab Chat 1/2, Default/Custom,
  AI rules.
- Thân panel là nhật ký việc AI đã làm, mở sẵn. Ô nhập thấp lại, cao lên khi gõ. Chip `/find-niches` `/long-tail` `/kill-weak`
  nằm ngay trên ô nhập.

## 4 · Không làm

- Không đổi API, DB, bộ chạy Autopilot, các lệnh gửi AI (`STEP_PROMPT`), PRO lock, bộ luật Tuỳ chỉnh. Chỉ đổi cách hiện.
- Không đổi trang `/r/:id` (kết quả đầy đủ) và trang Project.
- Không làm bản C (1 cột, AI thành thanh dưới đáy).

## 5 · Xong khi

- Lúc nào trên trang cũng chỉ có **1 nút chính**. Mỗi con số (điểm, % đo, số ứng viên) chỉ hiện 1 lần trên màn đầu.
- Phiên có niche giữ: AI's pick nằm trong màn đầu ở 1340×800 mà không phải cuộn.
- Từ "Fill N missing factors": 1 lần bấm chạy hết việc lấy số, không cần bấm từng nút.
- Test mới trong `web/tests/`: `fillPlan` (gộp Trends, gộp reach + fit, không có gì thiếu = rỗng), `pickOf` (chọn niche),
  nhóm `CandidateList`. `npm run check` xanh.
- Soát 960px + 1340px, sáng + tối, English + tiếng Việt: không cuộn ngang, tên niche dài không đẩy nút ra khỏi hàng.

## Một đường tới Brief + Spec + Plan (2026-11-06)

Người mới không thấy đích của AI Agent: flow chia 2 chặng, Autopilot dừng ở Health check, và trang Niche không có lối sang Brief.
Bản này gộp thành một đường, đích là bộ tài liệu.

- **Thanh tiến độ:** 1 flow 7 bước. 3 bước cuối có icon tài liệu, cuối đường có cờ "Kết quả: Brief + Spec + Plan".
- **Thẻ Bộ tài liệu app:** luôn hiện dưới thẻ AI's pick, 3 dòng Brief / Spec / Plan, mỗi dòng có trạng thái và nút Xem. Nút
  "AI viết cả bộ" chạy Autopilot từ bước Brief, tài liệu đã có thì không viết lại. Có tài liệu thì hiện Tải .md và Lưu thư mục AI.
- **Autopilot:** thêm tham số `until` (`health` hoặc `plan`) và `from` (`find` hoặc `brief`). Mặc định của API vẫn dừng ở Health
  check. Bước tài liệu xét theo kết quả: AI chưa ghi thì gửi lại, quá 2 lần thì dừng và báo thiếu tài liệu nào. Mỗi lần bấm chạy
  được thử lại từ đầu.
- **Trang Niche:** nút "Lên Brief + Spec + Plan cho niche này" gọi `POST /api/hunt/from-run`: tạo phiên với niche đã giữ, không tra
  lại, không trừ lượt tra, rồi viết 3 tài liệu. Bấm lần nữa mở lại phiên cũ của niche đó.
- **Highlight:** mục AI Agent ở sidebar tô màu AI và có ✦, trang chủ có banner, Autopilot đứng đầu trang AI Agent và được chọn sẵn.
- **Bản Free:** vẫn chạy 2 bước đầu. Chế độ tới Plan và 2 nút viết tài liệu dẫn sang trang PRO, API trả 402.

### Chạy thật 2026-11-06

1 phiên thật với Claude Code, ý tưởng "a medication reminder app that adult children manage for their elderly parents", 16 ứng viên.

- **Thời gian:** khoảng 13 phút cho đủ 7 bước. Bước 1–2 mất khoảng 3 phút, bước Collect thêm mất 7 phút (tra 9 long-tail), Health check và 3 tài liệu mất khoảng 2,5 phút. Mới đo 1 lần, không tính lúc dừng để sửa lỗi.
- **Lỗi 1, đã sửa:** câu lệnh bước Collect thêm bắt chọn keyword trong danh sách của Research và cấm mở Explore, trong khi danh sách đó chỉ có keyword gốc. AI dừng lại hỏi nên Autopilot dừng ở bước 3. Câu lệnh giờ cho lấy cụm hẹp hơn từ tên app đối thủ hoặc lời chê.
- **Lỗi 2, đã sửa:** bấm Chạy tiếp ở bước đã gửi đủ 2 lần thì dừng ngay với cùng lý do. Giờ mỗi lần bấm chạy, bước chưa ra kết quả được thử lại từ đầu.
- **Kết quả:** đủ Brief + Spec + Plan, đối chiếu mẫu vài số với dữ liệu Research thì khớp.

Điểm yếu của lần chạy này, đã sửa ở phần dưới: Autopilot không đọc review nên 6 tính năng MVP đều ghi "chưa đo" lời chê, Brief chọn "dementia medication reminder" nhưng Spec và Plan chuyển sang "Family Med Reminder". Còn lại chưa sửa: cả 9 long-tail lấy từ tên app đối thủ đều bị loại, nên 7 phút ở bước Collect thêm không thêm được niche nào ở phiên này.

### Đọc review trước Brief, cả bộ bám 1 niche

- **Đọc review:** ngay trước khi viết Brief, Autopilot đọc review 1–3★ của tối đa 3 niche đang giữ (chưa giữ cái nào thì lấy 3 niche đã tra điểm cao nhất), rồi ghi lại điểm. Đọc lỗi thì vẫn đi tiếp, AI ghi chưa đo. Bấm Dừng ngắt ngay. Bước Brief mở bằng nút tay không tự đọc review.
- **Bám 1 niche:** Autopilot chỉ đích danh niche điểm cao nhất sau khi có review trong câu Brief. Câu Spec và Plan yêu cầu đúng niche của BRIEF, số của niche khác chỉ để so và phải ghi rõ.
- **Lỗi thứ 3, đã sửa:** người dùng giữ tay rồi AI giữ long-tail thì bước Collect thêm bị coi là chưa xong, vì nhật ký chỉ tính lần giữ của AI.

Chạy thật phiên 2 (cùng ý tưởng, 12 ứng viên, 2026-11-06):

- **Thời gian:** khoảng 8 phút, cộng 3 đoạn chạy, chưa tính lúc dừng. Đọc review 3 niche và viết Brief mất khoảng 1 phút. Một số số liệu đã có từ phiên trước nên chưa so được công bằng với 13 phút của phiên 1.
- **Kết quả:** 280 review 1–2★ của 5 app. Yếu tố Đau có số 6.8, điểm niche chọn từ 4.2 lên 4.9. Brief có lời chê kèm số, Spec và Plan cùng mở đầu "senior medication tracker".

Còn yếu, chưa sửa:

- Điểm vẫn chỉ đo được khoảng 55% trọng số, Nhu cầu và Xu hướng còn chưa đo.
- AI nhớ niche của phiên cũ trong cùng máy nên có thể né keyword đã loại trước đó.

### Bước AI Suggest không giữ được niche nào

Phiên 2 dừng ở bước 2 vì AI chấm mọi ứng viên là BỎ, lúc đó chưa niche nào có review.

- **Đọc review rồi chấm lại:** AI không giữ cái nào thì Autopilot đọc review 1–3★ của tối đa 3 niche còn lại rồi gửi lại bước 2, nêu rõ niche đã đọc. Đọc lỗi thì vẫn gửi lại nhưng không nói đã đọc.
- **Không ép giữ:** vẫn không đáng làm thì AI không giữ. Autopilot dừng và báo "AI chưa thấy niche nào đáng giữ", kèm 2 việc người dùng làm được: giữ tay 1 niche rồi Chạy tiếp, hoặc thử ý tưởng khác.

Kiểm bằng test với AI giả. Đã chạy thật phiên 3 ("a flashlight app for android", dừng ở Health check, 13 ứng viên, 2026-11-06) nhưng AI giữ được niche ngay nên nhánh này chưa chạy thật. Phiên 3 mất khoảng 14 phút tới Health check, chủ yếu vì tra 13 ứng viên.
