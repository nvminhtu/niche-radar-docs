# RevenueCat — API đã kiểm và cách dùng trong pipeline

## Flutter — `purchases_flutter` 10.12.0

Đọc trực tiếp mã nguồn tag `10.12.0` (github.com/RevenueCat/purchases-flutter, `lib/purchases_flutter.dart`,
`lib/models/purchase_params.dart`, `lib/errors.dart`) ngày **2026-09-16**. App ghim bản thật trong `pubspec.lock`.

| Việc | API | Ghi chú |
|---|---|---|
| Khởi tạo | `await Purchases.configure(PurchasesConfiguration(apiKey))` | gọi một lần ở `main` |
| Nghe thay đổi | `Purchases.addCustomerInfoUpdateListener((CustomerInfo info) { ... })` | gia hạn/hết hạn tự đẩy về |
| Trạng thái hiện tại | `await Purchases.getCustomerInfo()` | |
| Có Pro | `info.entitlements.active.containsKey('pro')` | |
| Gói đang bán | `(await Purchases.getOfferings()).current?.availablePackages` | `Package.identifier`, `.packageType` (`PackageType.monthly/annual/weekly/lifetime/...`), `.storeProduct.priceString`, `.storeProduct.price`, `.storeProduct.title` |
| Mua | `await Purchases.purchase(PurchaseParams.package(package))` → `PurchaseResult.customerInfo` | `purchasePackage(...)` đã **deprecated** ("Use purchase(PurchaseParams)") |
| Người dùng huỷ | `on PlatformException catch (e)` → `PurchasesErrorHelper.getErrorCode(e) == PurchasesErrorCode.purchaseCancelledError` | không coi là lỗi |
| Khôi phục | `await Purchases.restorePurchases()` → `CustomerInfo` | |
| Log | `await Purchases.setLogLevel(LogLevel.debug)` | chỉ khi debug |

Toàn bộ đã được `flutter analyze` + test trên app scaffold (Flutter 3.47.4) ngày 2026-09-16.

## RevenueCat Paywalls (tuỳ chọn) — `purchases_ui_flutter` 10.12.0

- Thêm: `fvm flutter pub add purchases_ui_flutter`.
- Hiện paywall khi chưa có entitlement: `RevenueCatUI.presentPaywallIfNeeded('pro')` — kiểm tên hàm với bản đang dùng
  (docs.revenuecat.com ▸ Paywalls ▸ Flutter) trước khi viết.
- Android: `MainActivity` phải kế thừa `FlutterFragmentActivity` thay vì `FlutterActivity`.
- Thiết kế paywall trên dashboard; vẫn phải có Restore, Terms, Privacy — template RevenueCat có sẵn ô cho link.

## Native (kiểm tên hàm với bản SDK hiện hành trước khi viết)

**Android — `com.revenuecat.purchases:purchases`**

```kotlin
Purchases.configure(PurchasesConfiguration.Builder(context, BuildConfig.RC_ANDROID_KEY).build())
val offerings = Purchases.sharedInstance.awaitOfferings()
val result = Purchases.sharedInstance.awaitPurchase(PurchaseParams.Builder(activity, pkg).build())
val info = Purchases.sharedInstance.awaitRestore()
val isPro = info.entitlements.active.containsKey("pro")
```

Key qua `buildConfigField` đọc từ `local.properties`/biến môi trường — không commit.

**iOS — Swift Package `purchases-ios-spm`**

```swift
Purchases.configure(withAPIKey: rcIOSKey)
let offerings = try await Purchases.shared.offerings()
let result = try await Purchases.shared.purchase(package: pkg)      // result.userCancelled, result.customerInfo
let info = try await Purchases.shared.restorePurchases()
let isPro = info.entitlements.active["pro"] != nil
```

Bọc sau `protocol SubscriptionService: Sendable` + `FakeSubscriptionService` giống bản Flutter (xem app-native).

## Khái niệm — nói với người không biết code

| Từ | Nghĩa đời thường |
|---|---|
| Product | một món trong cửa hàng (gói tháng, gói năm) — tạo trên App Store Connect / Play Console |
| Entitlement | "vé vào cửa" Pro — mua món nào trong nhóm Pro cũng được vé này |
| Offering | "kệ trưng bày" — những món đang bày cho người dùng chọn; đổi kệ không cần cập nhật app |
| Package | một ô trên kệ, trỏ tới một Product |
| Customer info | hồ sơ người mua: đang có vé nào, hết hạn khi nào |
| Sandbox | cửa hàng thử — mua không mất tiền, chu kỳ rút ngắn |

## Bảng giá RevenueCat

Miễn phí tới 2.500 USD doanh thu theo dõi/tháng; vượt thì tính % (revenuecat.com/pricing — kiểm lại khi gần ngưỡng).

## Nguồn

docs.revenuecat.com (Getting started ▸ Flutter, Entitlements, Offerings, Sandbox testing, Paywalls) ·
github.com/RevenueCat/purchases-flutter · github.com/RevenueCat/ai-toolkit (plugin cho Claude Code).
