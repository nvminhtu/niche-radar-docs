# Launch playbook — app đầu tay, ngân sách gần 0

Kinh nghiệm thực hành phổ biến, **không phải số đo**. Mọi mục tiêu thay bằng số của chính app sau tuần đầu.

## 1. Lịch D-21 → D+7

| Ngày | Việc | Kết quả |
|---|---|---|
| D-21 | Lead magnet làm xong + form email + email chào mừng tự gửi (tự đăng ký thử) | `Email form:` chạy được |
| D-14 | Landing có nút đăng ký → rủ người quen, nhóm cộng đồng vào danh sách | URL chạy được |
| D-14 | Viết 3 dòng định vị, người dùng duyệt | marketing.md |
| D-12 | Mời 15–20 tester (TestFlight + closed test Google) — dùng lại cho closed test 14 ngày | danh sách |
| D-10 | Quay 5 video màn hình thật (vấn đề → app → kết quả) | thư mục store/video |
| D-7 | Góp ý từ tester → `/app-fix` những lỗi chặn | bản build cuối |
| D-5 | Soạn bài ra mắt (dài + ngắn), tin nhắn cá nhân; duyệt lại email 2 + 3 | marketing.md Nội dung |
| D-3 | Nhờ tester sẵn sàng để lại đánh giá thật **sau khi** app live (không viết hộ, không đổi quà lấy 5★) | |
| D0 | App live → gửi email 3 cho danh sách → đăng bài kênh chính → tin nhắn → trả lời mọi bình luận trong ngày | |
| D+1…3 | Mỗi ngày một video / bài nhỏ; trả lời review | |
| D+7 | Báo cáo tuần đầu vào grow.md; quyết định kênh nào giữ | |

## 2. Danh sách email + lead magnet

**Mồi theo loại app**

| Loại app | Mồi hợp | Thu email ở đâu |
|---|---|---|
| iOS / Android (chưa live) | danh sách chờ + "người đăng ký sớm nhận Offer Code / Promo code dùng Pro 1 tháng" | landing |
| iOS / Android (đã live) | tài liệu miễn phí cùng chủ đề (checklist, template, hướng dẫn PDF) | landing, blog, ô tự nguyện trong Settings |
| Mac bán ngoài store (`direct`) | bản dùng thử: nhập email → nhận link tải / license dùng thử | trang tải |
| Mac App Store (`mas`) | như iOS — store đã lo trial, chỉ thu email trên web | landing |

Mồi tốt: dùng được ngay trong 5 phút, đúng nỗi đau ở research, dẫn tự nhiên tới app. Không hứa thứ app không làm.

**Công cụ** (đều có gói free, form nhúng hoặc trang form riêng, link huỷ đăng ký tự động — kiểm giới hạn gói free ở trang giá
của họ lúc chọn, không ghi số từ trí nhớ): MailerLite · Buttondown · Kit (ConvertKit). Google Form / Tally chỉ để tạm —
không gửi email hàng loạt được, không có link huỷ.

**3 email tối thiểu**

```
1 — Chào mừng (gửi ngay): Đây là [mồi] bạn đăng ký: [link]. Mình đang làm [Tên app] để [kết quả].
    Trả lời email này cho mình biết: [câu hỏi về nỗi đau] — mình đọc hết.
2 — D-3: [Tên app] ra mắt [ngày]. [1 ảnh màn hình thật]. Bản miễn phí làm được [...].
3 — D0: Đã có trên store: [link App Store] · [link Google Play]. [Ưu đãi người đăng ký sớm nếu có, kèm hạn].
```

Câu trả lời cho email 1 là research miễn phí — chép lời than mới vào grow.md.

**Luật**
- Apple 5.1.1 — mục Account Sign-In: app không cần tài khoản thì không được bắt nhập email/đăng ký mới cho dùng tính năng. Ô email trong app = tự nguyện.
- Chỉ email cho người tự đăng ký; mọi email có link huỷ + tên + email liên hệ thật (CAN-SPAM / GDPR). Không mua danh sách.
- Có thu email trên web → Privacy Policy phải nói (`make_site.py` tự thêm khi `email_form_url` có trong app.json).

## 3. Bài ra mắt — khung

```
[Vấn đề trong một câu, bằng lời người dùng thật]
Mình làm [Tên app] để [kết quả]. Khác các app khác ở [điểm khác từ research].
Bản miễn phí làm được [...]. Bản Pro thêm [...].
Tải: [link App Store] · [link Google Play]
Mình đang cần góp ý thật — [câu hỏi cụ thể để mọi người trả lời].
```

## 4. Video ngắn — 3 kịch bản

| # | 0–3s (móc) | 3–20s | 20–30s |
|---|---|---|---|
| 1 | "Mình từng [lời than phổ biến]" | quay màn hình làm việc chính trong app | kết quả + tên app |
| 2 | "Một app nhỏ, một phần doanh thu cho các em vùng cao" | 3 cảnh app thật | "báo cáo công khai mỗi tháng" |
| 3 | "3 cách [kết quả] không cần [thứ phiền]" | mẹo 1, 2 (không app), 3 (app) | CTA mềm |

Quay bằng simulator: `xcrun simctl io booted recordVideo out.mov` · Android `adb shell screenrecord /sdcard/out.mp4`.

## 5. Apple Search Ads — dùng như công cụ nghiên cứu

- Tạo campaign nhỏ, bật Search Match, ngân sách 5–10 USD/ngày, 7 ngày.
- Đọc **Search terms report**: cụm người ta gõ thật dẫn tới app → đưa vào Keywords / Subtitle ở bản sau.
- Tắt khi đã có dữ liệu. Không cần lãi ở giai đoạn này.

## 6. Mã Pro miễn phí cho người sáng tạo / báo chí

- iOS: **Offer Codes** cho subscription (App Store Connect ▸ Subscriptions ▸ Offer Codes).
- Android: **Promo codes** trong Play Console.
- Ghi ai nhận mã nào, để đo kênh nào hiệu quả.

## 7. Không làm

Mua lượt cài / mua review / đổi quà lấy 5★ (vi phạm policy cả hai store, có thể bị gỡ app) · spam link vào nhóm · mua danh sách email / thêm email người chưa tự đăng ký.
