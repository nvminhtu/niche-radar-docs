# Runbook Google Play — app Flutter có subscription

`CLAUDE` chuẩn bị · `NGƯỜI DÙNG` bấm. Đối chiếu Play Console Help ngày **2026-09-15**.
Nguồn: support.google.com/googleplay/android-developer — answer/9859152 (listing), answer/14151465 (closed test),
answer/140504 (subscriptions), answer/9842756 (Play App Signing), developer.android.com/google/play/billing/test.

## Pha 0

| # | Việc | Ai |
|---|---|---|
| 0.1 | Tài khoản Play Console (25 USD, xác minh danh tính) | NGƯỜI DÙNG |
| 0.2 | Payments profile (merchant) liên kết | NGƯỜI DÙNG |
| 0.3 | Danh sách ≥ 15 người có Gmail đồng ý test 14 ngày (dư ra phòng người rút) | NGƯỜI DÙNG, CLAUDE soạn tin nhắn mời |
| 0.4 | **targetSdk 36** (Android 16) — bắt buộc cho app mới/bản cập nhật từ 2026-08-31 (xin gia hạn tới 2026-11-01) · kiểm `android/app/build.gradle` | CLAUDE |
| 0.5 | **Android developer verification** đã xong (Play Console) — từ 2026-09-30 app của dev chưa xác minh bị chặn cài ở BR/ID/SG/TH, toàn cầu 2027 | NGƯỜI DÙNG |

## Pha 1 — internal testing (không cần duyệt lâu)

| # | Màn | Việc | Ai |
|---|---|---|---|
| 1.1 | Create app | tên (`Play · Title`), ngôn ngữ, App, Free, cam kết chính sách | NGƯỜI DÙNG |
| 1.2 | Test and release ▸ Testing ▸ **Internal testing** ▸ Create release | bật Play App Signing · upload `app-release.aab` · release notes | NGƯỜI DÙNG |
| 1.3 | Internal testing ▸ Testers | thêm email chính mình → mở link opt-in → cài từ Play | NGƯỜI DÙNG |

Sau lần upload đầu, Play mới cho tạo sản phẩm subscription (app phải có bản build có quyền BILLING — `purchases_flutter` đã kèm).

## Pha 2 — subscription

| # | Màn | Việc | Ai |
|---|---|---|---|
| 2.1 | Monetize with Play ▸ Products ▸ **Subscriptions** ▸ Create | Product ID **đúng money.md** · tên · lợi ích | NGƯỜI DÙNG |
| 2.2 | Trong subscription ▸ **Add base plan** | Auto-renewing · chu kỳ (1 tháng / 1 năm) · giá · **Activate** | NGƯỜI DÙNG |
| 2.3 | Setup ▸ **License testing** | thêm Gmail tester (mua thử không mất tiền) | NGƯỜI DÙNG |
| 2.4 | RevenueCat ▸ app Android ▸ service account JSON (Google Cloud, quyền xem tài chính trong Play Console) | | NGƯỜI DÙNG, plugin revenuecat hướng dẫn |
| 2.5 | Cài từ link internal test ▸ mua thử ▸ Pro ▸ xoá cài lại ▸ Restore | | NGƯỜI DÙNG, CLAUDE ghi kết quả |

Service account mới có thể mất tới ~36 giờ mới có quyền *(cộng đồng)* — RevenueCat báo "credentials invalid" trong lúc chờ.

## Pha 3 — App content + listing

| Mục | Dán từ |
|---|---|
| Privacy policy | listing `## Privacy Policy URL` |
| Ads | Không có quảng cáo (nếu đúng) |
| App access | Toàn bộ tính năng truy cập được không cần đăng nhập (nếu đúng) |
| Content rating | bảng hỏi IARC — NGƯỜI DÙNG trả lời |
| Target audience | 18+ hoặc 13+ — **không** chọn nhóm dưới 13 nếu không làm app trẻ em (kéo theo Families policy). Mỹ: luật bang (Texas, Utah) → cân nhắc **Play Age Signals API** |
| Data safety | listing `## Data safety` — RevenueCat: Purchase history (App functionality), không chia sẻ, mã hoá khi truyền |
| Main store listing | `Play · Title` · `Play · Short description` · `Play · Full description` · icon 512 · feature graphic · ảnh `store/android/` |

## Pha 4 — closed test → production (tài khoản cá nhân tạo sau 2023-11-13)

| # | Việc | Điều kiện | Ai |
|---|---|---|---|
| 4.1 | Closed testing ▸ tạo track ▸ upload cùng AAB (hoặc bản mới) ▸ gửi duyệt | Google duyệt bản test (vài giờ–vài ngày) | NGƯỜI DÙNG |
| 4.2 | Mời tester (email list hoặc Google Group) ▸ họ opt-in + cài | **≥ 12 người opt-in liên tục 14 ngày** | NGƯỜI DÙNG + bạn bè |
| 4.3 | Trong 14 ngày: thu góp ý (form), sửa lỗi bằng `/app-fix`, cập nhật bản test | | CLAUDE + NGƯỜI DÙNG |
| 4.4 | Dashboard ▸ **Apply for production** — trả lời bảng hỏi về test (đã test gì, sửa gì) | CLAUDE soạn câu trả lời từ publish.md + plan/ (việc đã làm) | NGƯỜI DÙNG gửi |
| 4.5 | Production ▸ Create release ▸ **staged rollout 20%** | Google duyệt | NGƯỜI DÙNG |
| 4.6 | Theo dõi Android vitals (crash, ANR) 2–3 ngày → tăng 100% | | NGƯỜI DÙNG, CLAUDE đọc số |

## Lỗi hay gặp

| Triệu chứng | Nguyên nhân → sửa |
|---|---|
| Không tạo được subscription | chưa upload bản build nào / Payments profile chưa xong |
| Paywall trống trên máy test | cài bằng APK debug chứ không từ link Play; base plan chưa Activate; tài khoản test chưa thêm vào License testing; RevenueCat chưa có service account |
| "Version code has already been used" | tăng số sau `+` trong pubspec |
| Bị treo ở "Apply for production" | chưa đủ 12 người × 14 ngày liên tục — kiểm tab Testers |
| Từ chối vì Data safety | khai thiếu SDK — đối chiếu pubspec.yaml |
