# Định dạng file xuất

> Cột cố định của [Phase 16 · Export](web/phase-16-export.md). CSV, JSON và `schema.md` trong gói cho AI dùng chung một
> bảng cột ở `web/src/lib/export/columns.ts`. Đổi tên / bỏ cột = tăng `schema_version` + ghi CHANGELOG.

## Chung

- **CSV**: UTF-8 có BOM, dấu phẩy, mọi ô trong ngoặc kép, xuống dòng CRLF, ngày ISO, số thô. Mỗi bảng 1 file, gói trong `.zip` (Reddit Gap chỉ 1 bảng → tải thẳng `.csv`).
- **JSON**: `{ "format": "niche-radar/export", "schema_version": 2, "scope", "name", "created_at", "project", "runs", "tables" }` —
  `tables` có các bảng của phạm vi (Research: 6 bảng store · Project: 6 bảng store + `decisions` · Reddit Gap: `reddit_gaps`). `schema_version` 2 (2026-10-26): thêm `decisions`, mỗi dòng đủ mọi cột (thiếu số = `null`).
- **Gói cho AI**: `prompt.md` (việc AI phải làm + khung brief tính năng 7 mục) · `brief.md` (dữ liệu gọn có mã nguồn) ·
  `schema.md` (nội dung như trang này). Ước token = ký tự / 3.

## Bảng

Mã nguồn trong brief: `C` đối thủ · `P` chủ đề than (mỗi mã một chủ đề, nhiều câu trích) · `G` khoảng trống tính năng · `S` yếu tố điểm · `K` keyword · `T` Google Trends · `R` chủ đề Reddit Gap.
Bảng đủ cột có trong CSV / JSON cùng lần xuất.

### keywords

Keyword đã tra trong lượt Research (keyword gốc + gợi ý của Google Play) và số app hiện ra ở mỗi store.

- `run_id`: Mã lượt Research trong Niche Radar
- `niche`: Keyword gốc (seed) của lượt Research
- `country`: Mã nước 2 chữ (store + Trends)
- `code`: Mã dẫn nguồn trong brief (K1, K2…)
- `term`: Keyword
- `origin`: seed = keyword gốc · play_suggest = Google Play gợi ý
- `play_count`: Số app Google Play hiện ra (top 30)
- `appstore_count`: Số app App Store hiện ra (top 30)
- `top_play_app`: App đứng đầu Google Play cho keyword này
- `top_appstore_app`: App đứng đầu App Store cho keyword này
- `source`: Nguồn của dòng này
- `fetched_at`: Ngày lấy số (ISO)

### competitors

Đối thủ: mọi app hiện ra cho các keyword, xếp theo số rating giảm dần. Không có doanh thu — chỉ số công khai của store.

- `run_id`: Mã lượt Research trong Niche Radar
- `niche`: Keyword gốc (seed) của lượt Research
- `country`: Mã nước 2 chữ (store + Trends)
- `code`: Mã dẫn nguồn trong brief (C1, C2…)
- `store`: play = Google Play · appstore = App Store
- `title`: Tên app
- `developer`: Nhà phát triển
- `rating`: Điểm sao trung bình (0–5)
- `ratings_count`: Số lượt chấm sao
- `installs_min`: Lượt cài tối thiểu (chỉ Google Play, mốc 1K/10K/…)
- `price`: Giá tải (0 = miễn phí)
- `currency`: Đơn vị tiền của giá
- `money_model`: Mô hình tiền: sub · lifetime · iap · ads · free · unknown
- `money_label`: Nhãn tiền đọc được (vd "Sub ~$4.99/tháng", "IAP $1.99–$9.99")
- `updated_at`: Lần cập nhật cuối trên store
- `released_at`: Ngày phát hành
- `best_rank`: Hạng tốt nhất trong các keyword (1 = đầu)
- `keyword_count`: Số keyword app này hiện ra
- `url`: Link trang store
- `source`: Nguồn của dòng này
- `fetched_at`: Ngày lấy số (ISO)

### complaints

Lời chê: chủ đề than gom từ review 1–2★ của top đối thủ, kèm câu nguyên văn đã kiểm khớp review gốc.

- `run_id`: Mã lượt Research trong Niche Radar
- `niche`: Keyword gốc (seed) của lượt Research
- `country`: Mã nước 2 chữ (store + Trends)
- `code`: Mã dẫn nguồn trong brief (P1, P2…) — một mã mỗi chủ đề
- `theme`: Chủ đề than
- `review_count`: Số review 1–2★ nói về chủ đề này
- `severity`: Mức nặng: Mất dữ liệu · Trả tiền mà không dùng được (×3) · Ép trả phí · Hỏng (×2) · Quảng cáo · Giao diện (×1)
- `quote`: Câu nguyên văn trong review
- `quote_app`: App bị chê trong câu đó
- `reviews_total`: Tổng số review 1–2★ đã đọc
- `source`: Nguồn của dòng này
- `fetched_at`: Ngày lấy số (ISO)

### gaps

Feature Gap: tính năng × top 5 app mỗi store, đếm bao nhiêu app có. Chỉ phần đã đọc trang store (không gọi mạng khi xuất).

- `run_id`: Mã lượt Research trong Niche Radar
- `niche`: Keyword gốc (seed) của lượt Research
- `country`: Mã nước 2 chữ (store + Trends)
- `code`: Mã dẫn nguồn trong brief (G1, G2…)
- `feature`: Tính năng
- `apps_total`: Số app trong bảng
- `have`: Số app có (kể cả bản trả phí)
- `paid_only`: Số app chỉ có ở bản trả phí
- `unstated`: Số app đã đọc trang store mà không nhắc tới
- `unknown`: Số ô chưa đọc được
- `gap`: gap = khoảng trống tính năng · positioning = khoảng trống định vị · unsure = chưa chắc · trống = không phải khoảng trống
- `apps_with`: Tên các app có tính năng này
- `source`: Nguồn của dòng này
- `fetched_at`: Ngày lấy số (ISO)

### trends

Google Trends 12 tháng của keyword gốc (chỉ số tương đối 0–100, không phải lượt tìm) + truy vấn liên quan.

- `run_id`: Mã lượt Research trong Niche Radar
- `niche`: Keyword gốc (seed) của lượt Research
- `country`: Mã nước 2 chữ (store + Trends)
- `kind`: point = điểm theo tuần · top = truy vấn liên quan nhiều nhất · rising = truy vấn đang lên
- `date`: Tuần (chỉ kind = point)
- `query`: Truy vấn (chỉ top / rising)
- `value`: Chỉ số 0–100 (rising: % tăng hoặc mức)
- `source`: Nguồn của dòng này
- `fetched_at`: Ngày lấy số (ISO)

### scores

Điểm sức khoẻ niche v2: từng yếu tố 0–10, trọng số, độ tin, bằng chứng. Dòng factor = total là điểm tổng.

- `run_id`: Mã lượt Research trong Niche Radar
- `niche`: Keyword gốc (seed) của lượt Research
- `country`: Mã nước 2 chữ (store + Trends)
- `code`: Mã dẫn nguồn trong brief (S1, S2…)
- `factor`: money · pain · competition · demand · trend · reach · fit · total
- `label`: Tên yếu tố
- `value`: Điểm 0–10 (trống = chưa đo)
- `weight`: Trọng số
- `trust`: verified · proxy · trích dẫn · tự chấm · chưa đo
- `evidence`: Bằng chứng / cách tính
- `source`: Nguồn của dòng này
- `fetched_at`: Ngày lấy số (ISO)

### reddit_gaps

Reddit Gap (Phase 10): chủ đề × chuyên mục từ bài Reddit anh đã lưu, xếp theo điểm gap. Cùng số với bảng trên trang /reddit.

- `subreddit`: Subreddit (all = mọi subreddit đã nhập)
- `code`: Mã dẫn nguồn trong brief (R1, R2…)
- `topic`: Mã chủ đề
- `topic_label`: Chủ đề
- `category`: Mã chuyên mục
- `category_label`: Chuyên mục: hỏi app · lỗi sau cập nhật · cách làm…
- `threads`: Số bài
- `recent_90d`: Số bài trong 90 ngày gần nhất
- `median_engagement`: Trung vị điểm + comment mỗi bài
- `solved_share`: Tỷ lệ bài đã giải (flair Solved / "Edit: solved"), 0–1
- `no_native_share`: Tỷ lệ bài có comment nói "không có cách gốc", 0–1 (trống = file không có comment)
- `mac_apps`: Số app Mac App Store cho chủ đề (50 = 50+, trống = chưa đếm)
- `gap_score`: Điểm gap — công thức ở trang Reddit Gap
- `sample_titles`: Tiêu đề 3 bài mẫu điểm cao nhất (cách nhau bởi " ; ")
- `sample_urls`: Link 3 bài mẫu (cùng thứ tự)
- `source`: Nguồn của dòng này
- `fetched_at`: Ngày dựng bảng (ISO)

### decisions

Bàn quyết định (Phase 16b): mỗi keyword của project chấm 5 trục 1–5 có dẫn chứng + verdict. Bản chốt (manual) và bản AI dán ngược (ai) mới nhất.

- `decision_id`: Mã lần chấm
- `kind`: manual = bản anh chốt · ai = JSON AI dán ngược
- `term`: Keyword
- `country`: Mã nước 2 chữ
- `verdict`: BUILD · TEST THÊM · BỎ (trống = chưa chọn)
- `reason`: Lý do verdict
- `total`: Tổng điểm các trục có dữ liệu (không có điểm tổng bí ẩn)
- `axes_measured`: Số trục có dữ liệu / 5
- `demand_score`: Nhu cầu: điểm 1–5 (trống = chưa đo hoặc mã nguồn bịa)
- `demand_evidence`: Nhu cầu: mã nguồn [C1]… + lý do
- `weak_score`: Đối thủ yếu: điểm 1–5 (trống = chưa đo hoặc mã nguồn bịa)
- `weak_evidence`: Đối thủ yếu: mã nguồn [C1]… + lý do
- `money_score`: Khả năng thu tiền: điểm 1–5 (trống = chưa đo hoặc mã nguồn bịa)
- `money_evidence`: Khả năng thu tiền: mã nguồn [C1]… + lý do
- `effort_score`: Công sức build (5 = ít công): điểm 1–5 (trống = chưa đo hoặc mã nguồn bịa)
- `effort_evidence`: Công sức build (5 = ít công): mã nguồn [C1]… + lý do
- `aso_score`: ASO ngách: điểm 1–5 (trống = chưa đo hoặc mã nguồn bịa)
- `aso_evidence`: ASO ngách: mã nguồn [C1]… + lý do
- `source`: Nguồn của dòng này
- `fetched_at`: Ngày chấm (ISO)
