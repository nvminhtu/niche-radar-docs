# Launch · ShotMatic phân tích thị trường app

> Gom mọi thứ về **app** của Plan 1 và Plan 2 vào một chỗ, để chốt một bản launch **chuyên về phân tích thị trường app**.
> Trang này là **bước 0: hiểu sâu**. Chỉ khi bước 0 xong mới viết brief → spec → plan.

<span class="chip chip--doing">Gom 2026-11-16 · anh chốt 4 câu theo mặc định 2026-11-17 · bước 0 xong · brief + spec + plan viết 2026-11-17, chờ anh duyệt plan</span>

<div class="box box--goal" markdown>
**Tóm tắt**

- Plan 2 có 28 mục, trải 4 mảng: App, YouTube, Amazon/KDP, Maps. Chỉ 9 mục là về app. Vì vậy hiện khó nói "bản launch có gì".
- Bản launch nên trả lời **7 câu** mà người sắp chọn app để làm cần biết. ShotMatic đã có tính năng cho cả 7 câu,
  nhưng **độ sâu chưa đều**, và có chỗ **số chưa đáng tin** (xem phần "Chỗ chưa đủ sâu").
- Đề xuất: làm **bước 0 · đào sâu** (5 việc, có số) → rồi mới viết brief → spec → plan.
</div>

## Khách của bản launch

**Indie dev / founder làm một mình, chưa có app, đang chọn app để làm.**

- Đây là chỗ AppTweak và Appfigures bỏ trống: hai tool đó phục vụ người **đã có app** muốn lên hạng (xem [mục 25](phase-plan2-25-hoc-apptweak-appfigures.md)).
- Người đã có app vẫn dùng được (Soi 1 app, So sánh app), nhưng không phải khách chính.

## 7 câu khách cần trả lời

Xếp theo thứ tự ra quyết định. Mỗi câu ghi: tính năng đang có · độ sâu hiện tại · lỗ hổng.

### 1 · Có ai tìm không? (Cầu)

- **Đang có:** Tra 1 keyword có Google Trends ([Phase 3](phase-3-google-trends.md)) · độ hot trong Explorer
  ([Phase 40](phase-40-explore-tree.md)) · Keyword Intelligence: ma trận cơ hội ([mục 10](phase-plan2-10-keyword-engine.md)).
- **Độ sâu:** vừa. Có xu hướng, có thứ hạng gợi ý.
- **Lỗ hổng:** không có **số lượt tìm thật**. Độ hot là hạng trong ô gợi ý; Trends chỉ là chỉ số tương đối.
  Popularity 5–100 của Apple chỉ lấy được qua Apple Search Ads.

### 2 · Ai đang chiếm chỗ, mạnh cỡ nào? (Cung)

- **Đang có:** Research top app Google Play + App Store ([Phase 1](phase-1-google-play.md), [Phase 2](phase-2-app-store.md))
  · độ đông app store · hồ sơ đối thủ + cờ yếu ([Phase 41](phase-41-competitor-profile.md))
  · So sánh app 2–4 app ([mục 20](phase-plan2-20-so-sanh-doi-thu.md), [mục 22](phase-plan2-22-so-app-ra-viec-can-lam.md)) · Soi 1 app.
- **Độ sâu:** tốt nhất trong 7 câu.
- **Lỗ hổng:** chỉ có ảnh chụp 1 lần, **không có lịch sử hạng**. Play chậm (trung bình 95 giây / lượt, đo 2026-11-15).
  App Store hay trả lỗi 429 khi chạy nhiều (ghi chú mục 26).

### 3 · App mới còn chen được không? (Cửa vào)

- **Đang có:** nhãn Cầu > cung (mục 22.3) · Săn app 100 → 10 → 3 ([mục 24](phase-plan2-24-san-app-cau-cung.md), chấm lại ở 24.4)
  · đèn đỏ / xanh điểm yếu đối thủ ([mục 26](phase-plan2-26-san-app-diem-yeu.md)).
- **Độ sâu:** vừa. Đây là **chất riêng** của ShotMatic (app dưới 1 năm vẫn leo được top 10).
- **Lỗ hổng:** dựa trên ngày ra mắt + số rating ở 1 thời điểm. Không biết app đó leo nhanh hay chậm.

### 4 · Người dùng đang khổ chỗ nào? (Nỗi đau)

- **Đang có:** Đối thủ bị chê gì ([Phase 18](phase-18-competitor-complaints.md)) · điểm yếu đối thủ (mục 26)
  · Review Mining ([mục 27](phase-plan2-27-review-mining.md), mới là spec, 27.0 đã code)
  · Reddit / Q&A / GitHub ([Phase 11](phase-11-reddit-gap.md), [12](phase-12-qa-gap.md), [13](phase-13-github-gap.md)).
- **Độ sâu:** tốt về cách gom, yếu về lượng.
- **Lỗ hổng:** review chỉ đọc khi bấm tay, top 5 app mỗi store, mỗi lần tới 4 phút. Reddit bị chặn với AI (ghi chú 2026-11-12).

### 5 · Có ai trả tiền không, bao nhiêu? (Tiền)

- **Đang có:** nhãn tiền (giá, IAP) · doanh thu thật TrustMRR ([Phase 38](phase-38-revenue.md)) · trục Tiền của điểm v2.
- **Độ sâu:** **yếu nhất**.
- **Lỗ hổng:** Research **không ghi IAP của App Store**: 445/445 app App Store để trống ở các lượt #298–#301
  (DB máy dev, 2026-11-16). Không ước được doanh thu hay lượt tải. TrustMRR chỉ có vài app.

### 6 · Mình làm gì khác? (Tính năng · định vị)

- **Đang có:** Feature Gap Matrix ([Phase 4](phase-4-feature-gap.md)) · bảng "app mới nên có gì" (mục 22)
  · brief tính năng xuất .md ([Phase 15](phase-15-export.md)) · Ai là khách ([Phase 19](phase-19-ai-la-khach.md)).
- **Độ sâu:** vừa. Tính năng rút từ mô tả store bằng luật.
- **Lỗ hổng:** chưa nối nỗi đau (câu 4) với tính năng (câu 6) thành 1 bảng "làm cái này vì người ta than cái kia".

### 7 · Có nên làm không? (Quyết định)

- **Đang có:** Sức khoẻ niche ([Phase 20](phase-20-niche-health.md)) · Bàn quyết định ([Phase 16](phase-16-decision-board.md),
  [28.10](phase-28-10-decision-board-easy.md)) · Evidence pack ([Phase 43](phase-43-evidence-presell.md))
  · Project 4 chặng ([mục 16](phase-plan2-16-trang-project.md)) · nút Bắt đầu build ([mục 13](phase-plan2-13-bat-dau-build.md))
  · AI Agent ([Phase 28.6](phase-28-6-ai-agent.md)).
- **Độ sâu:** nhiều lớp, nhưng **rối**.
- **Lỗ hổng:** cùng 1 keyword đang có **4 điểm khác nhau**: điểm v1 (Explorer), điểm v2 (Research), sức khoẻ niche, điểm Săn app.
  Người dùng không biết tin điểm nào.

## Trạng thái các mục app của Plan 2

| Mục | Trạng thái | Cần gì để vào launch |
|---|---|---|
| [10 · Keyword Intelligence](phase-plan2-10-keyword-engine.md) | Phase 1–3 có code | Chốt có giữ không, hay gộp vào Tra keyword |
| [13 · Nút Bắt đầu build](phase-plan2-13-bat-dau-build.md) | Xong, đã push | — |
| [16 · Trang Project](phase-plan2-16-trang-project.md) | 16.1–16.2 trên nhánh riêng, chưa merge | Merge hoặc bỏ |
| [20 · So sánh đối thủ app](phase-plan2-20-so-sanh-doi-thu.md) | Xong | — |
| [22 · App mới nên có gì](phase-plan2-22-so-app-ra-viec-can-lam.md) | 22.0, 22.3 có code · phần còn lại chờ duyệt | Chốt phần còn lại |
| [24 · Săn app](phase-plan2-24-san-app-cau-cung.md) | Xong, 24.4 đã push | Kiểm điểm bằng app thật (B0.1) |
| [25 · Học AppTweak + Appfigures](phase-plan2-25-hoc-apptweak-appfigures.md) | Mới là spec | Phần định vị dùng cho brief |
| [26 · Điểm yếu đối thủ](phase-plan2-26-san-app-diem-yeu.md) | Có code, chưa commit | Soát + commit |
| [27 · Review Mining](phase-plan2-27-review-mining.md) | Spec · 27.0 có code chưa commit | Chốt 3 câu |
| 28 · Cài đặt quản lý dữ liệu | Có code, chưa commit | Soát + commit |
| Soi 1 app: cùng studio + tương tự | Có code, chưa commit | Soát + commit |

## Ngoài bản launch (đề xuất đóng băng)

Giữ code, không làm thêm, ẩn khỏi bản launch (sidebar đã ẩn Amazon / KDP / Maps từ 2026-11-15):

- **YouTube:** mục 7, 8, 9, 11, 15, 17, 18, 19, 21, 23.
- **Amazon / KDP:** mục 4.3, 6, 12, extension Scout (1.3).
- **Google Maps.**

Giữ cho launch vì kéo người tới: extension ShotMatic Lite (1.1) · landing / guide / free tool (mục 2) · Demo site (4.1).

## Chỗ chưa đủ sâu

Những điểm này cần đo hoặc sửa trước khi hứa với khách:

- **Mọi điểm đều là quy ước tự đặt** (điểm v2, sức khoẻ, Săn app), chưa kiểm bằng app thật thành công hay thất bại.
- **4 điểm cho 1 keyword**, không có câu trả lời "điểm nào là điểm chính".
- **Tiền gần như mù trên App Store** (không có IAP trong Research).
- **Nguồn chậm và dễ bị chặn:** Play 95 giây / lượt, App Store 429. Một lượt Săn app mất 5 phút (bước 1) + 5–15 phút (bước 2).
- **Không có số lượt tìm, lượt tải, lịch sử hạng.** Đây là thế mạnh của AppTweak / Appfigures; mình không đua (mục 25), nhưng phải
  nói rõ với khách ShotMatic đo cái gì và không đo cái gì.
- **Nhiều phần chưa commit** (mục 26, 27.0, 28, Soi app liên quan): chưa thể tính là đã có.

## Bước 0 · Đào sâu (làm trước brief)

!!! note "Kết quả bước 0"
    Đã làm xong 2026-11-17, số + nguồn ở [Launch · Bước 0 hiểu sâu](launch-app-hieu-sau.md).
    Ý chính: điểm hiện tại chưa nhận ra niche kiếm tiền (13 app thật: v2 bảo BỎ 8); tín hiệu đúng nhất là "app mới leo được top 10".

Năm việc, mỗi việc ra **số có nguồn và ngày**. Kết quả ghi vào một trang "Hiểu sâu" để brief dựa vào.

### B0.1 · Kiểm điểm bằng app thật

- Lấy khoảng 20 app indie **đang kiếm tiền** (doanh thu công khai trên TrustMRR hoặc tự công bố) và khoảng 20 app **đã bỏ**
  (hơn 1 năm không cập nhật, ít rating).
- Chạy ShotMatic trên keyword chính của từng app. Xem điểm có **tách được 2 nhóm** không.
- Nếu không tách được: chỉnh trọng số, hoặc bỏ phần điểm đó.

### B0.2 · Một khung điểm duy nhất

- Gom 4 điểm hiện có về **1 điểm chính** cho 1 keyword, các điểm còn lại thành "phần" của điểm đó (đúng 7 câu ở trên).
- Phần nào chưa đo thì ghi "chưa đo", không chấm 0 (đã làm ở 24.4).

### B0.3 · Đo nguồn số

- Đo lại Play, App Store, Trends: thời gian mỗi lượt, tỉ lệ lỗi, chạy 1 · 3 luồng.
- Thử đọc IAP App Store ngay trong Research. Đo có làm chậm thêm bao nhiêu.

### B0.4 · Khách hỏi thật những gì

- Gom khoảng 30 câu hỏi thật của indie dev về chọn niche app (Indie Hackers, HN, Reddit do anh dán vào).
- Khớp từng câu với 7 câu ở trên. Câu nào khách hỏi nhiều mà ShotMatic trả lời yếu → ưu tiên.

### B0.5 · Bảng so đối thủ theo 7 câu

- AppTweak · Appfigures · AppKittie · Sensor Tower · ShotMatic: mỗi tool trả lời được câu nào, bằng số gì, giá bao nhiêu.
- Dùng lại [doi-thu.md](../marketing/doi-thu.md), [đánh giá AppKittie + Appfigures](../marketing/danh-gia-appkittie-appfigures-2026-11-07.md) và mục 25.

## Rồi mới tới brief → spec → plan

1. **Brief** (1 trang): khách · 7 câu · lời hứa launch · phạm vi · Free / PRO · đo thành công thế nào. → [Launch · Brief](launch-app-brief.md) (2026-11-17).
2. **Spec:** mỗi câu là 1 khối kết quả: nguồn số, công thức, chỗ "chưa đo", màn hình. → [Launch · Spec](launch-app-spec.md) (2026-11-17).
3. **Plan:** chia task theo [Quy trình build](../quy-trinh-build.md), làm từng task, đo thật, xem tận mắt. → [plan launch](../superpowers/plans/2026-11-17-launch-1-diem-co-hoi.md) (2026-11-17).

## Anh đã chốt (2026-11-17)

Cả 4 câu theo mặc định: khách chính là người chưa có app · ẩn YouTube / Amazon / Maps khỏi bản launch, giữ code ·
B0.1 lấy nhóm "thành công" từ TrustMRR + app tự công bố doanh thu · gộp về 1 điểm chính.

| # | Câu hỏi | Đã chốt |
|---|---|---|
| 1 | Khách launch chỉ là người **chưa có app, đang chọn app**? | Có. Người đã có app là khách phụ |
| 2 | YouTube / Amazon / Maps ẩn khỏi bản launch, giữ code? | Có |
| 3 | B0.1 lấy nhóm "app thành công" từ TrustMRR + app tự công bố doanh thu? | Có |
| 4 | Gộp 4 điểm về 1 điểm chính (B0.2)? | Có |
