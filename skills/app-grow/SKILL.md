---
name: app-grow
description: "Bước 13 của pipeline app — vòng lặp tăng trưởng hằng tuần sau khi ra mắt: lấy số thật từ App Store Connect Analytics, Play Console, RevenueCat Charts (qua plugin revenuecat nếu có) vào grow.md, đọc phễu để biết đòn bẩy nào hỏng (hiển thị → xem trang → cài → mở paywall → dùng thử → trả phí → gia hạn), gom review thành nhóm và soạn trả lời, xin đánh giá đúng lúc, chạy MỘT thí nghiệm mỗi lần (giá/paywall bằng RevenueCat Experiments, icon/ảnh bằng Product Page Optimization, In-App Events), biến kết quả thành /app-feature hoặc /app-fix. Use when the app is live and someone asks 'app được bao nhiêu người tải', 'doanh thu tháng này', 'sao ít người mua', 'tăng chuyển đổi paywall', 'trả lời review', 'xin đánh giá 5 sao', 'thử giá mới', 'MRR', 'churn', or when scripts/app.py status says the pipeline is in the growth loop. Không bịa số, không mua review."
argument-hint: "[slug] [week|month|report YYYY-MM]"
user-invocable: true
---

# Bước 13 — grow (vòng lặp)

Không có "xong". Mỗi tuần một dòng số liệu, mỗi lần một thí nghiệm.

## Hằng tuần (30 phút)

1. **Lấy số** — người dùng mở và đọc cho Claude, hoặc Claude đọc qua MCP nếu đã cài:
   - App Store Connect ▸ Analytics: impressions, product page views, downloads (7 ngày).
   - Play Console ▸ Statistics + Store listing conversion.
   - RevenueCat Charts: trials mới, active subscriptions, MRR, churn — plugin `revenuecat` có skill `revenuecat-charts`.
   Ghi một dòng vào `grow.md` `## Số liệu` **kèm nguồn**. Không có → `chưa đo`.
2. **Đọc phễu** — tìm đoạn gãy nhất, sửa đúng đòn bẩy:

| Triệu chứng | Đòn bẩy hỏng | Việc |
|---|---|---|
| ít hiển thị | từ khoá, tên, subtitle, danh mục | `/app-listing` + từ khoá thật từ Search Ads |
| hiển thị nhiều, ít xem trang | **icon** + tên trong kết quả tìm kiếm | PPO thử icon |
| xem trang nhiều, ít cài | ảnh 1–2, 150 ký tự đầu, số sao | PPO thử ảnh; xin đánh giá đúng lúc |
| cài nhiều, ít mở paywall | người dùng chưa thấy giá trị / paywall khó tìm | onboarding, vị trí paywall (`/app-feature`) |
| mở paywall nhiều, ít mua | copy, giá, gói mặc định | RevenueCat Experiments (một biến) |
| mua nhiều, huỷ nhiều | giá trị không lặp lại | tính năng giữ chân (`/app-feature`), khảo sát lý do huỷ |
| review 1–3★ lặp một nhóm | lỗi/thiếu thật | `/app-fix` hoặc `/app-feature` |

3. **Review** — gom nhóm vào `## Review người dùng`; soạn câu trả lời ngắn, cảm ơn, nói đã/sẽ sửa gì (người dùng tự đăng).
4. **Một hành động** cho tuần tới, ghi vào log.
5. **Công khai số thật** (bán ngoài store / có RevenueCat): đơn đầu → người dùng nối provider vào TrustMRR; mỗi mốc
   soạn sẵn 1 post X kèm ảnh verified. Tháng một lần chạy `/app-indie` lại để so mình với 3 indie cùng ngách.

## Xin đánh giá đúng lúc

Gói `in_app_review` (Flutter) sau một **khoảnh khắc thành công** (vd hoàn thành 7 ngày liên tiếp) — không lúc mở app,
không sau lỗi, không hỏi "bạn có thích app không" rồi mới chuyển ai thích sang store (vi phạm policy). Hệ điều hành tự giới hạn
số lần hiện. Thêm bằng `/app-feature`.

## Thí nghiệm — một biến mỗi lần

| Thử | Công cụ | Đọc kết quả khi |
|---|---|---|
| Giá, gói mặc định, paywall | RevenueCat Experiments (skill `revenuecat-experiments`) | đủ mẫu theo RevenueCat báo; không dừng sớm |
| Icon, ảnh store | App Store Product Page Optimization · Play Store listing experiments | độ tin cậy ≥ ~90% |
| Chữ được index không cần build | In-App Events (iOS) · Promotional Text | |

Ghi vào `## Thí nghiệm`: bắt đầu, thay đổi gì, đo gì, kết thúc, kết quả. Không đổi giá + icon + từ khoá cùng lúc.

## Không làm

Bịa/ước số · mua lượt cài hay review · đổi quà lấy đánh giá · đọc kết quả thí nghiệm khi chưa đủ độ tin cậy.

Mỗi tuần: `scripts/app.py log <slug> --skill app-grow "..."`; bài học mới vào LEARNED.md.
