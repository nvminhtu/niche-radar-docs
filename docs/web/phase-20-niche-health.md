# Phase 20 · Chấm sức khoẻ niche

> Điểm v2 đã có đủ 7 yếu tố — phase này làm cho điểm **đọc được và tin được**: mỗi số giải thích được trong 1 phút,
> có cờ chặn khi niche có rủi ro mà điểm không thấy, và kiểm lại bằng niche đã biết kết quả.

<span class="chip chip--done">Xong 2026-10-26 · công thức + nguồn từng yếu tố · 5 cờ chặn · ngưỡng có lý do · lịch sử điểm · back-test 10 niche (kết quả thật còn thiếu)</span>

<div class="box box--goal" markdown>
**Hiện có (Phase 7 + 9).** Khối Sức khoẻ niche: 7 yếu tố (Tiền · Đau · Cạnh tranh · Nhu cầu · Xu hướng · Tiếp cận ·
Hợp sức), trọng số sửa được + 4 mẫu (App Mac · iOS · Android · SaaS), 2 trục tự chấm có lý do, % đã đo, gợi ý BUILD /
TEST THÊM / BỎ. Back-test 5 niche ra 4,5–5,4 điểm, chưa niche nào ≥ 6.
</div>

**Cần xong trước:** [Phase 9](phase-9-small-features.md) (điểm v2) · [Phase 18](phase-18-competitor-complaints.md) (lời chê theo loại cho yếu tố Đau) · back-test **chạy lại sau [Phase 38](phase-38-revenue.md)** (Tiền đổi từ ước sang đo)

## Làm gì

| | |
|---|---|
| :material-calculator-variant: **Mở từng yếu tố** | bấm vào 1 yếu tố → công thức, số đầu vào, nguồn + ngày lấy, ví dụ "Cạnh tranh 3/10 vì top 5 có 2 app > 100k rating". Không có số nào "từ trên trời" |
| :material-shield-check: **Độ tin hiện to** | mỗi yếu tố gắn nhãn **đo** · **ước (proxy)** · **tự chấm** · **chưa đo**; điểm tổng ghi "đo 70%" ngay cạnh, dưới 60% thì gợi ý chỉ được là TEST THÊM |
| :material-flag: **Cờ chặn** | luật cố định ép gợi ý xuống TEST THÊM / BỎ dù điểm cao: thương hiệu lớn chiếm ≥ 3 / 5 top · cần backend / tài khoản bắt buộc · tên loại app bão hoà (rủi ro 4.3) · nội dung có bản quyền · xu hướng giảm 2 năm liền. Mỗi cờ ghi lý do + nguồn |
| :material-ruler: **Ngưỡng do anh đặt** | ngưỡng BUILD / TEST THÊM / BỎ sửa ở Cài đặt, mỗi lần sửa ghi lý do + ngày (giống Quyết định đã chốt) |
| :material-history: **Back-test** | chấm lại các niche đã biết kết quả (app đã ra mắt của mình, niche đã bỏ) → bảng điểm vs kết quả thật, chỉnh trọng số mẫu theo đó |
| :material-chart-line: **Lưu điểm mỗi lần chấm** | mỗi lần tra lại lưu 1 dòng điểm + % đo + cờ. Biểu đồ điểm theo thời gian **chỉ làm ở [Phase 42](phase-42-tracking.md)** (dòng thời gian chung), không vẽ 2 chỗ |
| :material-arrow-up-bold-circle: **Cần đo thêm gì để chắc hơn** | dưới điểm: yếu tố nào đang "ước" / "chưa đo" và bước nào nâng nó lên, VD "Tiền đang ước → nhập trang TrustMRR ([Phase 38](phase-38-revenue.md)) → độ tin 55% → ~70%". Tool chỉ ra bước tiếp, không chỉ cho điểm |
| :material-text-box-outline: **1 đoạn kết luận không AI** | ghép câu từ mẫu: "Tiền rõ (3 app thu subscription), đau vừa, cạnh tranh đông; cờ: thương hiệu lớn" — vào evidence pack |

<div class="box box--rules" markdown>
**Luật**

- Không có "điểm tổng hợp bí ẩn": điểm = tổng có trọng số của số đang hiện, ai cũng tính lại tay được
- Yếu tố chưa đo không được coi là 0 hay 5 — bỏ ra khỏi tổng và báo
- Quyết định cuối là của anh (CỔNG 1); tool chỉ gợi ý
</div>

<div class="box box--star" markdown>
**Xong khi**

- Mở 1 niche bất kỳ, giải thích được từng yếu tố từ màn hình, không phải đọc code (anh thử 3 niche)
- Back-test ≥ 5 niche đã biết kết quả, bảng điểm vs kết quả nằm trong trang này; chạy lại sau Phase 38, thêm cột "sau Phase 38"
- Cờ chặn bật đúng trên ≥ 2 niche thử có rủi ro thật (kiểm tay lý do)
- Test xanh cho công thức + cờ, screenshot đã Read
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- AI tự chấm hay tự quyết BUILD
- So nhiều niche cạnh nhau — [Phase 44](phase-44-compare-niche.md)
- Đo trục Tiếp cận / Hợp sức tự động (cần nguồn mới — YouTube, Reddit ở Version 2)
</div>

## Kết quả chạy thật (2026-10-26)

Bản sao DB thật, trọng số mặc định, ngưỡng mặc định BUILD ≥ 6 · TEST THÊM ≥ 4.

**Đã làm**

- Bấm từng yếu tố → **công thức** (vd `8/10 × 7 + 3 (có doanh thu TrustMRR) = 8.6`) + số đầu vào + nguồn + ngày + app / câu làm dẫn chứng.
  Test kiểm: công thức kết thúc bằng đúng điểm, tổng tính lại tay khớp.
- **Đau đo được không cần AI**: chưa gom chủ đề AI thì lấy cụm lời chê theo luật của [Phase 18](phase-18-competitor-complaints.md).
- 4 nhãn **đo · ước (proxy) · tự chấm · chưa đo**; điểm ghi "đo N % · số thật M %" (số thật = đo + tự chấm, không gồm ước).
- **Cờ chặn** (`web/src/lib/health-flags.ts`): thương hiệu lớn ≥ 3/5 top · cần backend / tài khoản (≥ 3 và ≥ 50 % mô tả store) ·
  loại app bão hoà 4.3 · bản quyền (seed → BỎ, ≥ 3 keyword gợi ý → TEST THÊM) · Trends giảm 2 năm liền (mỗi năm ≥ 15 %, đọc cache
  Mùa vụ 5 năm). Thiếu dữ liệu → "chưa kiểm", không đoán.
- **Ngưỡng** sửa ở Cài đặt → Ngưỡng gợi ý điểm niche, bắt ghi lý do, lưu lịch sử. **Lịch sử điểm**: bảng `score_history`, 1 dòng mỗi lần
  điểm / gợi ý / cờ đổi (xem lại trang không nhân dòng) — biểu đồ để [Phase 42](phase-42-tracking.md).
- **Cần đo thêm gì**: chỉ hiện bước làm được (đọc review, chạy lại Trends, tự chấm, TrustMRR) + % đo sau khi làm.
- **Kết luận không AI** ở đầu khối + dòng "Kết luận không AI" và "Cờ chặn" trong evidence pack.

**Back-test** (tool chấm lại, trọng số mặc định)

| Niche | Điểm | Đo | Gợi ý | Cờ bật | Kết quả thật |
|---|---|---|---|---|---|
| not enough ram | 5,7 | 75 % | TEST THÊM | — | đã làm app Mac cho niche RAM, đang bán (doanh thu chưa đo) |
| ram issue | 5,4 | 75 % | TEST THÊM | — | như trên |
| habit tracker | 5,7 | 75 % | TEST THÊM | loại bão hoà 4.3 | chưa ghi |
| color by number | 5,5 | 75 % | TEST THÊM | — | chưa ghi |
| pomodoro timer | 5,3 | 75 % | TEST THÊM | — | chưa ghi |
| budget tracker | 4,7 | 75 % | TEST THÊM | — | chưa ghi |
| bubble shooter | 4,6 | 55 % | TEST THÊM (hạ vì đo < 60 %) | — | chưa ghi |
| dual monitor wallpaper | 3,1 | 60 % | BỎ | loại bão hoà 4.3 | chưa ghi |
| external display manager | 3,0 | 60 % | BỎ | — | chưa ghi |
| bubble game for toddlers | 2,2 | 65 % | BỎ | — | chưa ghi |

**Ghi chú**

- **Chưa đạt "back-test ≥ 5 niche đã biết kết quả"**: DB chỉ có 2 niche (cùng nhóm RAM) có kết quả thật ghi được; các niche khác chưa
  làm app / chưa bán nên chưa có kết quả. **Chưa đổi trọng số / ngưỡng** — không có số để căn. Cần anh: ghi kết quả thật (bán được /
  không / bị từ chối) cho ≥ 3 niche nữa, rồi chạy lại bảng này.
- Cờ **thương hiệu lớn** không bật ở 31 niche: top 5 theo thứ hạng của các niche này toàn nhà phát triển nhỏ (bubble shooter: Ilyon,
  MadOverGames…; app King chỉ đứng đầu khi xếp theo số rating). Đúng với dữ liệu. Cờ **bão hoà 4.3** bật đúng 3 niche (habit tracker ×2,
  dual monitor wallpaper). Cờ **cần backend** đọc 9–10 mô tả / niche, cao nhất 1/9 — chưa niche nào bật.
- Không niche nào ≥ 6: cả 31 niche đều đông hoặc thiếu số thật (số thật 0–40 %).

Plan code chi tiết: [Phase 20](../superpowers/plans/2026-10-25-niche-radar-phase13-niche-health.md)
