---
name: app-flutter
description: "Skill phụ nhánh Flutter (mặc định) của pipeline app — luật viết code Flutter/Dart cho app đã scaffold bằng scripts/new_flutter_app.py: kiến trúc chính chủ UI (Screen chỉ vẽ) → ViewModel (ChangeNotifier, test được) → Repository (interface + bản thật + Fake), Provider cho dependency, go_router cho điều hướng, theme từ tokens sinh từ design.md, chữ gom một file, cách thêm lưu dữ liệu (shared_preferences / file / sqflite), gọi API (http), thông báo, đa ngôn ngữ, cách thêm gói an toàn qua fvm, test ViewModel/widget/integration, và bảng lỗi Flutter hay gặp. Chỉ tới skill chính chủ của Flutter team (plugin dart-flutter) cho layout, widget test, integration test, routing, localization. Used by app-build, app-feature, app-fix. Use when writing Flutter code in this pipeline, 'code flutter', 'thêm màn flutter', 'lưu dữ liệu flutter', 'provider', 'go_router', 'ChangeNotifier', 'widget test', 'RenderFlex overflowed', 'thêm package flutter', 'flutter pub add', 'đa ngôn ngữ flutter'."
user-invocable: false
---

# app-flutter — luật code Flutter trong pipeline

Được gọi từ `/app-build`, `/app-feature`, `/app-fix`. **Theo mẫu đã có trong project trước** (home/paywall/settings);
bảng dưới là mặc định khi chưa có mẫu. Luôn gọi Flutter bằng `fvm flutter` trong `apps/ACTIVE/<slug>/source/app`.

Kiến trúc gốc: docs.flutter.dev/app-architecture (Flutter team) — skill chính chủ `flutter-apply-architecture-best-practices`.

## Cấu trúc

```
lib/
├── main.dart                     tạo repository (thật/Fake) → MultiProvider → App
├── config/app_config.dart        String.fromEnvironment — không hard-code key/URL
├── data/
│   ├── repositories/<x>_repository.dart          abstract class (hợp đồng)
│   ├── repositories/<x>_repository_local.dart    bản thật
│   ├── repositories/<x>_repository_fake.dart     bản giả cho test/dev
│   └── models/<x>.dart                           dữ liệu bất biến (final + copyWith + toJson/fromJson)
├── routing/router.dart           Routes.<tên> hằng số + GoRoute
└── ui/
    ├── core/theme/               tokens.dart (SINH) + app_theme.dart
    ├── core/app_strings.dart     mọi chữ người dùng thấy
    └── <feature>/<feature>_screen.dart + <feature>_view_model.dart (+ widgets/ nếu màn lớn)
test/
├── ui/<feature>_view_model_test.dart
└── ui/<feature>_screen_test.dart
```

## Mẫu một lát cắt

```dart
// data/repositories/habit_repository.dart
abstract class HabitRepository {
  Stream<List<Habit>> watchToday();
  Future<void> toggle(String id);
}

// ui/today/today_view_model.dart
class TodayViewModel extends ChangeNotifier {
  TodayViewModel({required this._habits}) {
    _sub = _habits.watchToday().listen((list) { _items = list; notifyListeners(); });
  }
  final HabitRepository _habits;
  late final StreamSubscription<List<Habit>> _sub;
  List<Habit> _items = const [];
  List<Habit> get items => _items;
  bool get isEmpty => _items.isEmpty;             // luật nằm ở đây, không ở Screen
  Future<void> toggle(String id) => _habits.toggle(id);
  @override
  void dispose() { _sub.cancel(); super.dispose(); }
}

// ui/today/today_screen.dart
class TodayScreen extends StatelessWidget {
  const TodayScreen({super.key, required this.viewModel});
  final TodayViewModel viewModel;
  @override
  Widget build(BuildContext context) => ListenableBuilder(
        listenable: viewModel,
        builder: (context, _) => viewModel.isEmpty ? const _Empty() : ListView(/* ... */),
      );
}

// routing/router.dart
GoRoute(path: Routes.today, builder: (context, _) => TodayScreen(viewModel: TodayViewModel(habits: context.read())));

// main.dart — thêm repository vào providers
Provider<HabitRepository>.value(value: LocalHabitRepository(prefs)),
```

## Luật

| Chủ đề | Làm | Tránh |
|---|---|---|
| State | ViewModel `ChangeNotifier` + `ListenableBuilder`; state thuần UI (ô đang mở) → `StatefulWidget` | logic trong `build()`, `setState` cho dữ liệu nghiệp vụ |
| Dependency | truyền qua constructor; lấy từ Provider ở router (`context.read()`) | ViewModel tự tạo repository thật, singleton toàn cục |
| Async + UI | `if (!context.mounted) return;` sau `await` trước khi dùng `context` | dùng `context` sau await không kiểm |
| Màu/chữ | `Theme.of(context).colorScheme` / `textTheme` / `AppTokens` | `Color(0xFF...)`, `Colors.red` trong màn hình |
| Chữ | `AppStrings.x` (sau này ARB/l10n) | chuỗi rải trong widget |
| Danh sách | `ListView.builder` + `key` ổn định | `Column` cho danh sách dài |
| Layout cao | nội dung dài trong `ListView`/`SingleChildScrollView`, tôn trọng `SafeArea` | chiều cao cố định → vỡ khi chữ lớn |
| Accessibility | nút icon có `tooltip`; hình mang nghĩa có `Semantics(label:)` | icon không nhãn |
| Dữ liệu | model bất biến `final` + `copyWith` | sửa list đang được UI giữ |
| Lint | `fvm flutter analyze` sạch trước khi tick | bỏ qua `warning` |

## Chọn cách lưu

| Dữ liệu | Gói | Ghi chú |
|---|---|---|
| Vài cài đặt, cờ | `shared_preferences` | không lưu dữ liệu nhạy cảm |
| Danh sách nhỏ (< vài nghìn mục) | file JSON qua `path_provider` | đơn giản, dễ sao lưu |
| Danh sách lớn, truy vấn, lọc | `sqflite` (hoặc `drift` nếu cần type-safe) | cần migration khi đổi schema |
| Bí mật (token) | `flutter_secure_storage` | |
| Đồng bộ nhiều máy / đăng nhập | Firebase (`firebase_core`, `cloud_firestore`, `firebase_auth`) | kéo theo privacy + xoá tài khoản; chỉ khi spec yêu cầu |

Danh sách gói đã cân nhắc + lý do: [references/packages.md](references/packages.md).

## Thêm gói

```bash
cd apps/ACTIVE/<slug>/source/app && fvm flutter pub add <gói>      # tự chọn bản tương thích
```

Trước khi thêm: pub.dev ▸ nhà phát hành đã xác minh hoặc Flutter/Google/tổ chức lớn, cập nhật trong 12 tháng, license
MIT/BSD/Apache (không GPL cho app thương mại), hỗ trợ iOS + Android. Thêm xong: `analyze` + `test` + chạy iOS (Pods) + Android.
Gói thu dữ liệu → cập nhật listing Data safety.

## Test

| Tầng | Khi | Công cụ |
|---|---|---|
| ViewModel | **mọi** lát cắt | `flutter_test` + bản Fake |
| Widget | màn có luật hiển thị quan trọng (paywall, trạng thái rỗng/lỗi) | `testWidgets`, `pumpAndSettle`, `find.text` — skill `flutter-add-widget-test` |
| Integration | luồng nhiều màn trước bản lớn | `integration_test` — skill `flutter-add-integration-test` |

## Skill chính chủ (plugin `dart-flutter` — cài ở `/app-setup`)

| Việc | Skill |
|---|---|
| Layout vỡ, overflow | `flutter-fix-layout-issues` |
| Màn phone/tablet | `flutter-build-responsive-layout` |
| Điều hướng / deep link | `flutter-setup-declarative-routing` |
| Đa ngôn ngữ | `flutter-setup-localization` |
| JSON model | `flutter-implement-json-serialization` |
| Gọi API | `flutter-use-http-package` |
| Widget preview | `flutter-add-widget-preview` |
| Lỗi runtime Dart, xung đột gói | `dart-fix-runtime-errors`, `dart-resolve-package-conflicts` (repo dart-lang/skills) |

## Lỗi hay gặp

| Lỗi | Sửa |
|---|---|
| `A RenderFlex overflowed by N pixels` | bọc cuộn / `Expanded` / `Flexible`; skill `flutter-fix-layout-issues` |
| `Vertical viewport was given unbounded height` | `ListView` trong `Column` → `Expanded(child: ListView(...))` hoặc `shrinkWrap` cho list ngắn |
| `ProviderNotFoundException` | chưa thêm repository vào `MultiProvider` trong main.dart |
| `setState() called after dispose()` | huỷ `StreamSubscription` trong `dispose`, kiểm `mounted` |
| `version solving failed` | đọc dòng `because`, hạ/nâng gói xung đột; skill `dart-resolve-package-conflicts` |
| iOS: `CocoaPods could not find compatible versions` | `cd ios && pod repo update && pod install`; nâng iOS deployment target nếu gói đòi |
| Hot reload không thấy đổi | pipeline build lại bằng `run_app.py run` — không dựa vào hot reload |
