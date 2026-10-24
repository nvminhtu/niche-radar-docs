---
name: app-fix
description: "Sửa lỗi trong app một cách có hệ thống cho người không biết code: tạo file việc trong apps/ACTIVE/<slug>/plan/ (fix, qua scripts/app.py change), TÁI HIỆN lỗi trước (các bước, thiết bị, log crash qua run_app.py logs, Crashlytics/App Store Connect crash), viết test đỏ chứng minh lỗi, tìm nguyên nhân gốc (không đoán, không vá triệu chứng), sửa, test xanh + chạy lại toàn bộ test + chạy app thật và xem screenshot, tăng build number, rồi release. Có bảng lỗi hay gặp riêng cho Flutter và subscription (paywall trống, mua xong không thành Pro, Restore không thấy gì, crash lúc mở, màn trắng, chữ bị cắt). Use when something is broken, 'app bị lỗi', 'sửa bug', 'app crash', 'bấm nút không được', 'màn hình trắng', 'paywall không hiện giá', 'mua rồi mà không mở khoá', 'restore không được', 'người dùng báo lỗi', 'review 1 sao vì lỗi', 'build lỗi', 'test fail'."
argument-hint: "[slug] \"mô tả lỗi\""
user-invocable: true
---

# app-fix — sửa lỗi

**Một việc:** lỗi tái hiện được → có test chứng minh → nguyên nhân gốc ghi rõ → test xanh → app chạy thật đúng → `status: done` rồi `python3 scripts/app.py plan-close <slug> --tag xong` (file sang `plan/done/`).

Quy trình tư duy: `superpowers:systematic-debugging` (dùng nó, đừng đoán). Skill này thêm phần tái hiện trên app thật
và các lỗi đặc thù subscription.

## 1. Tạo file thay đổi

```bash
python3 scripts/app.py change <slug> --type fix --title "Paywall không hiện giá trên Android"
```

## 2. Tái hiện — chưa tái hiện được thì chưa sửa

Điền bảng mục 3 của file: các bước · mong đợi · thực tế · thiết bị/phiên bản.

```bash
python3 scripts/run_app.py run <slug> --platform android     # đưa app lên
python3 scripts/native/android_ui.py tap "Upgrade to Pro"    # đi theo các bước
python3 scripts/run_app.py logs <slug> --platform android    # crash log
```

iOS: công cụ iOS Simulator của phiên (inspect/tap) · crash report `~/Library/Logs/DiagnosticReports/Runner*.ips`.
Lỗi người dùng thật báo: App Store Connect ▸ TestFlight/Crashes, Play Console ▸ Android vitals, Crashlytics nếu có.
Không tái hiện được trên simulator → hỏi người dùng thiết bị, phiên bản OS, thao tác, ảnh chụp.

## 3. Test đỏ trước khi sửa

Viết test ViewModel (hoặc widget test) **fail đúng vì lỗi đó** — dùng bản Fake để dựng lại tình huống
(vd `FakeSubscriptionRepository(nextStatus: PurchaseStatus.failed)`). Chạy `python3 scripts/test_app.py <slug>` thấy đỏ.
Lỗi thuần giao diện không test được → screenshot "trước" làm bằng chứng.

## 4. Nguyên nhân gốc

Đọc log từ dòng lỗi **đầu tiên** (Flutter: dòng `══╡ EXCEPTION CAUGHT` và frame đầu trong `lib/`). Hỏi "vì sao" tới khi ra
nguyên nhân, không dừng ở triệu chứng. Ghi một câu vào file thay đổi. **Không** sửa assertion cho khớp output sai;
**không** bọc `try/catch` nuốt lỗi cho hết đỏ.

## 5. Sửa → chứng minh

Sửa nhỏ nhất đúng nguyên nhân → test đỏ thành xanh → **toàn bộ** test xanh → `run_app.py run` cả hai nền tảng → Read screenshot →
làm lại các bước tái hiện, lỗi không còn. Dán lệnh + kết quả vào mục 7 của file thay đổi.

3 lần sửa không được → dừng, báo người dùng đã thử gì, giả thuyết còn lại là gì.

## 6. Phát hành

`python3 scripts/release.py <slug> --patch` — tự tăng version patch + build (`1.1.0+6` → `1.1.1+7`), build, ký, đóng gói vào
`publish/release/v<version>/` + `App-Ready-Publish/<Tên-store>/release/v<version>/` (luật: `reference/README-APP-PUBLISH-03-RELEASE-FOLDERS.md`). Lỗi nghiêm trọng (crash lúc mở, không mua được) → phát hành ngay: `release.py` → `/app-publish`. `status: done` trong frontmatter. Ghi LEARNED.md (mục "Lỗi: <tên>" — nguyên nhân gốc bằng lời thường).

## Lỗi hay gặp

| Triệu chứng | Nguyên nhân thường gặp | Kiểm |
|---|---|---|
| Paywall trống / "Could not load plans" (bản thật) | Apple: Paid Apps Agreement chưa Active, sản phẩm chưa "Ready to Submit", bundle id lệch · Google: chưa upload bản nào lên Play, base plan chưa Activate, cài APK debug thay vì từ link Play · RevenueCat: offering chưa **current**, package chưa gắn sản phẩm | `app-paywall` §Kiểm tra; skill `revenuecat-troubleshoot` |
| Mua xong không thành Pro | sản phẩm chưa gắn vào entitlement `pro` · code kiểm entitlement tên khác | RevenueCat ▸ Entitlements; `AppConfig.entitlementId` |
| Restore "No previous purchase" | đang đăng nhập store bằng tài khoản khác lúc mua · sandbox vs production lẫn | hỏi tài khoản đã mua |
| Crash lúc mở, chỉ bản release | thiếu key trong `config/prod.json` · R8 xoá lớp (Android) | `run_app.py logs`; build release chạy thử |
| Màn trắng/đỏ "RenderFlex overflowed" | layout cố định chiều cao, chữ lớn | skill `flutter-fix-layout-issues`; bọc `ListView`/`SingleChildScrollView` |
| `setState() called after dispose()` / dùng `context` sau `await` | widget đã đóng khi tác vụ async xong | kiểm `context.mounted` trước khi dùng |
| Chữ bị cắt ở tiếng Việt | line-height thấp, `maxLines` | tăng `height`, bỏ giới hạn dòng |
| Build iOS lỗi Pods sau khi thêm gói | cache CocoaPods cũ | `cd app/ios && pod repo update && pod install` |
| Build Android lỗi `minSdk` | gói mới đòi minSdk cao hơn | nâng `minSdk` trong `android/app/build.gradle.kts`, ghi vào spec |
