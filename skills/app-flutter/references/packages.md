# Gói Flutter đã cân nhắc cho pipeline

Chọn theo: nhà phát hành tin cậy · còn bảo trì · license dùng thương mại được · hỗ trợ iOS + Android · ít phụ thuộc.
Phiên bản **không ghi ở đây** — `fvm flutter pub add` tự chọn bản tương thích với Flutter đã ghim; bản thật đang dùng nằm
trong `pubspec.lock` của từng app. Kiểm lại trên pub.dev trước khi thêm (điểm, ngày cập nhật, nhà phát hành).

## Có sẵn khi scaffold

| Gói | Nhà phát hành | Để làm gì |
|---|---|---|
| `provider` | Flutter Favorite | truyền repository xuống cây widget (kiến trúc chính chủ dùng) |
| `go_router` | flutter.dev | điều hướng, deep link |
| `url_launcher` | flutter.dev | mở Terms / Privacy / quản lý subscription / email |
| `purchases_flutter` | RevenueCat | subscription iOS + Android |

## Hay cần thêm

| Nhu cầu | Gói | Nhà phát hành | Lưu ý |
|---|---|---|---|
| Lưu cài đặt | `shared_preferences` | flutter.dev | |
| Thư mục file | `path_provider` | flutter.dev | |
| CSDL cục bộ | `sqflite` | tekartik (Flutter Favorite) | migration khi đổi schema |
| CSDL type-safe | `drift` | simolus3 | có code generation — nặng hơn cho người mới |
| Lưu bí mật | `flutter_secure_storage` | | |
| Thông báo nhắc giờ | `flutter_local_notifications` + `timezone` | | Android 13+ xin quyền POST_NOTIFICATIONS lúc bật tính năng; exact alarm cần khai báo |
| Xin đánh giá | `in_app_review` | | gọi sau khoảnh khắc thành công |
| Chia sẻ | `share_plus` | fluttercommunity.dev | |
| Icon app | `flutter_launcher_icons` (dev) | fluttercommunity.dev | `remove_alpha_ios: true` |
| Splash | `flutter_native_splash` (dev) | | |
| Đa ngôn ngữ | `flutter_localizations` (SDK) + `intl` | flutter.dev / dart.dev | skill `flutter-setup-localization` |
| Gọi API | `http` | dart.dev | skill `flutter-use-http-package` |
| Paywall do RevenueCat dựng | `purchases_ui_flutter` | RevenueCat | Android cần `FlutterFragmentActivity` — xem app-paywall |
| Đăng nhập / đồng bộ | `firebase_core`, `firebase_auth`, `cloud_firestore` | firebase.google.com | cần `flutterfire configure`; privacy + xoá tài khoản |
| Crash report | `firebase_crashlytics` | firebase.google.com | khai Data safety "Crash logs" |

## Tránh cho người mới

| Tránh | Vì sao |
|---|---|
| Nhiều thư viện state cùng lúc (bloc + riverpod + getx) | một kiến trúc thôi — pipeline dùng ChangeNotifier + provider |
| `get` / GetX | trộn điều hướng + state + DI, khó theo kiến trúc chính chủ |
| Gói không cập nhật > 18 tháng | dễ vỡ khi Flutter/Xcode lên bản |
| Gói license GPL/AGPL | ràng buộc mở mã nguồn app |
| SDK quảng cáo/analytics chưa cần | thêm khai báo privacy, ATT, và làm chậm app |
