# Định dạng file xuất

> Cột cố định của [Phase 16 · Export](web/phase-16-export.md). CSV, JSON và `schema.md` trong gói cho AI dùng chung một
> bảng cột ở `web/src/lib/export/columns.ts`. Đổi tên / bỏ cột = tăng `schema_version` + ghi CHANGELOG.

## Chung

- **CSV**: UTF-8 có BOM, dấu phẩy, mọi ô trong ngoặc kép, xuống dòng CRLF, ngày ISO, số thô. Mỗi bảng 1 file, gói trong `.zip`.
- **JSON**: `{ "format": "niche-radar/export", "schema_version": 1, "scope", "name", "created_at", "project", "runs", "tables" }` —
  `tables` có đủ 6 bảng dưới đây, mỗi dòng đủ mọi cột (thiếu số = `null`).
- **Gói cho AI**: `prompt.md` (việc AI phải làm + khung brief tính năng 7 mục) · `brief.md` (dữ liệu gọn có mã nguồn) ·
  `schema.md` (nội dung như trang này). Ước token = ký tự / 3.

## Bảng

Mã nguồn trong brief: `C` đối thủ · `P` chủ đề than (mỗi mã một chủ đề, nhiều câu trích) · `G` khoảng trống tính năng · `S` yếu tố điểm · `K` keyword · `T` Google Trends.
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
