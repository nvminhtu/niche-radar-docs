# Đánh giá plan "Mac super app / MacKit Studio" (2026-10-18)

## Giữ lại (đúng)

- Micro app trước, suite sau; module chỉ thêm khi cùng workflow / cùng tệp khách.
- Tìm sản phẩm đã có người trả tiền trước khi code; doanh thu "verified" ≠ lợi nhuận.
- Luật dừng theo mốc 14/30/60/90 ngày; chẩn đoán "tải mà không quay lại / quay lại mà không mua / không ai tải".
- Database nghiên cứu dùng lại; 50–100 app đúng nhóm > 5.000 startup nông.
- Không khoá thao tác cơ bản sau subscription; mua đứt + sub chỉ cho phần có chi phí duy trì.

## Sửa (không hợp với repo / người dùng)

| Plan nói | Vấn đề | Thay bằng |
|---|---|---|
| Tauri 2 + React + TS | Người dùng không code; repo đã có pipeline Swift + 3 app Mac bán thật | Swift 6 + SwiftUI, SwiftPM |
| Bắt đầu Capture Studio | Đã có `<slug>` + `research/<ngày>-<chủ-đề>.md`; screenshot là loại bão hoà (CleanShot, Shottr free, Xnapper, Cap open source) | Nếu chọn capture → đào tiếp StepSnap (Step Guide là wedge), không mở app mới |
| Screen Studio $30k/tháng, CleanShot ~$15k | Số 2023 / ước tính bên thứ 3 → `tự khai` | Ưu tiên số `verified` TrustMRR đo lại 2026-10-18 (30 ngày / tổng): Sandimax-Wallper $12,758 / $155,395 · MacMD Viewer $1,903 / $12,561 · SlapMac $1,300 / $57,542 · How to Convert $1,105 / $60,360 · Screen Charm $395 / $54,428 (sync cũ). Bản 07/10: `research/<ngày>-<chủ-đề>.md` |
| Mô phỏng 2% visitor → mua | Giả định, chưa đo; không có benchmark công khai cho app Mac bán direct | Lấy tỷ lệ thật từ app đang bán; QuickCheck + RAM Rescue chưa có đơn (2026-10-18) → `chưa đo`, không mô phỏng |
| 50 đối thủ trong 14 ngày + 10–15 phỏng vấn | Quá rộng cho 1–2h/ngày | 15–25 app trong 1–2 cụm, câu nói người dùng từ review/Reddit/X |
| Super app có launcher, modules | Đấu Raycast/Alfred; phình phạm vi | Bundle license các app đã có đơn |
| AI Desktop Assistant | Chi phí API, Apple Intelligence + ChatGPT app có sẵn | Loại khỏi 1.0 |
| Mac App Store song song | Tài khoản đang dính đợt 4.3 | Direct trước |

## Thiếu trong plan

- **Phân phối là nút thắt thật**: repo đã có nhiều app chưa tới đơn đầu tiên. Mỗi wedge phải có kênh đo được trước khi code
  (keyword SEO kiểu How to Convert, video kiểu SlapMac, landing oneclicktool.app).
- Cross-promo giữa các app của mình (mô hình studio của Wallper: nhiều app nhỏ, một thương hiệu).

## Nguồn (kiểm tải được 2026-10-18 bằng curl, đo lại cùng ngày)

| Nguồn | Tải | Dùng để | Nhãn số |
|---|---|---|---|
| trustmrr.com (`/startup/<slug>.md`) | 200 | doanh thu từ cổng thanh toán | verified |
| showmrr.com · microns.io | 200 | đối chiếu MRR, sản phẩm nhỏ đang bán | tự khai / verified tuỳ listing |
| indiemakerlist.com/leaderboard/mac-apps | 200 | founder app Mac + doanh thu công bố | tự khai |
| macapps.report · thisiswhyibuilt.com · boringcashcow.com | 200 | bản đồ thị trường, câu chuyện | tự khai |
| acquire.com · flippa.com · sideprojectors.com · acquisiteur.com | 200 | định giá, app rao bán | tự khai (đòi bằng chứng) |
| setapp.com/apps · macupdate.com | 200 | danh mục app Mac có người trả | proxy |
| alternativeto.net | 403 | đối thủ + khe hở — dùng WebSearch | proxy |
| Product Hunt · r/macapps (`.json`) | 403 | tín hiệu nhu cầu — dùng WebSearch | proxy |
| HN (hn.algolia.com qua `demand_research.py hn`) | 200 | dân kỹ thuật than gì | proxy |
