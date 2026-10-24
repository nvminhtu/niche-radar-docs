---
name: app-paywall
description: "Skill phụ subscription của pipeline app — nối RevenueCat thật vào app (Flutter mặc định, native khi cần): việc người dùng làm trên dashboard (project, app iOS/Android, public SDK key, entitlement pro, offering default với package tháng/năm, In-App Purchase key .p8, service account Google), đưa key public vào config/dev.json + prod.json, hiểu khung SubscriptionRepository đã scaffold (RevenueCat thật + Fake), chọn paywall tự vẽ hay RevenueCat Paywalls (purchases_ui_flutter), thử mua sandbox iOS và license tester Android, giữ paywall đủ thành phần store bắt buộc, và bảng kiểm tra khi paywall trống / mua xong không mở khoá / restore không thấy gì. Dựa trên SDK purchases_flutter 10.x (API đã đọc từ mã nguồn) và plugin chính chủ RevenueCat AI Toolkit. Used by app-build (lát cắt Paywall), app-fix, app-publish. Use when 'gắn revenuecat', 'nối subscription thật', 'paywall không hiện giá', 'test mua in-app', 'sandbox apple', 'license tester', 'entitlement', 'offering', 'restore purchases', 'revenuecat paywalls', 'purchases_flutter'."
user-invocable: false
---

# app-paywall — RevenueCat + paywall

App Flutter đã scaffold **có sẵn** khung: `SubscriptionRepository` (hợp đồng) · `RevenueCatSubscriptionRepository` (thật) ·
`FakeSubscriptionRepository` (chưa có key / test) · `PaywallScreen` + `PaywallViewModel` · test canh thành phần bắt buộc.
Việc của skill này: **nối bản thật** và **chứng minh mua được**.

money.md `Model: shop` (app free + gói mua một lần): vẫn dùng khung trên, đổi chỗ — offering `shop` gồm các package
Non-Consumable, mỗi gói một entitlement `pack_<tên>` (gói all gắn mọi entitlement); repository trả về **tập gói đã sở hữu**
thay vì một cờ `isPro`; màn Shop là `PaywallScreen` dạng lưới, mua bằng `Purchases.purchase(PurchaseParams.package(pkg))`,
Restore trả lại mọi gói non-consumable. Bản Fake giữ danh sách gói giả để chạy khi chưa có key.

Đọc: [references/revenuecat.md](references/revenuecat.md) (API đã kiểm, native, RevenueCat Paywalls).
Plugin chính chủ (nếu đã cài ở `/app-setup`): `create-revenuecat-project`, `integrate-revenuecat`, `revenuecat-paywall`,
`revenuecat-testing-setup`, `revenuecat-troubleshoot`, `revenuecat-entitlements-gate`.

## 1. Dashboard — người dùng làm, Claude chỉ từng nút

1. RevenueCat ▸ New project (tên app).
2. Add app ▸ **App Store** (bundle id) → tải **In-App Purchase Key** `.p8` từ App Store Connect ▸ Users and Access ▸ Integrations.
3. Add app ▸ **Play Store** (applicationId) → service account JSON (quyền tài chính Play Console).
4. **Products**: import từ store (sản phẩm phải tạo trước ở `/app-publish` Pha 1–2, đúng Product ID money.md).
5. **Entitlements** ▸ `pro` ▸ attach mọi sản phẩm Pro.
6. **Offerings** ▸ `default` ▸ package Monthly (`$rc_monthly`) + Annual (`$rc_annual`) → **Make current**.
7. API keys ▸ copy **public** key mỗi app (`appl_...`, `goog_...`).

## 2. Đưa key vào app

`apps/ACTIVE/<slug>/source/app/config/dev.json` và `prod.json`:

```json
{ "RC_IOS_KEY": "appl_xxx", "RC_ANDROID_KEY": "goog_xxx",
  "TERMS_URL": "https://.../terms.html", "PRIVACY_URL": "https://.../privacy.html",
  "SUPPORT_EMAIL": "support@..." }
```

Chỉ key public. `sk_...` (secret) **không bao giờ** vào app — `check_release.py` FAIL nếu thấy.
`run_app.py` tự truyền dev.json; bản release truyền prod.json (`/app-release`). Có key → `main.dart` tự dùng RevenueCat thật.

## 3. Paywall tự vẽ (mặc định) hay RevenueCat Paywalls?

| | Tự vẽ (scaffold) | RevenueCat Paywalls (`purchases_ui_flutter`) |
|---|---|---|
| Đổi giao diện/giá hiển thị | cần build mới | đổi trên dashboard, không cần review |
| Test không cần mạng | có (Fake) | không |
| Thành phần bắt buộc | test canh sẵn | RevenueCat template lo, vẫn phải kiểm |
| Android | không yêu cầu thêm | `MainActivity` phải kế thừa `FlutterFragmentActivity` |
| A/B test | code | RevenueCat Experiments trên dashboard |

Mặc định giữ tự vẽ cho MVP (test được, theo design.md). Chuyển khi bắt đầu thử nghiệm paywall ở `/app-grow`.

## 4. Chứng minh mua được — chưa chứng minh thì chưa tick lát Paywall bản thật

| Nền tảng | Cách thử | Điều kiện |
|---|---|---|
| iOS | TestFlight trên máy thật + **Sandbox Apple Account** (Settings ▸ Developer) → mua → Pro → xoá cài lại → Restore → Pro | Paid Apps Agreement Active · sản phẩm Ready to Submit · IAP key đã tải lên RevenueCat |
| iOS nhanh (simulator) | StoreKit Configuration file trong Xcode (skill `revenuecat-testing-setup`) | chỉ kiểm luồng UI, không kiểm server |
| Android | cài từ link **internal testing** bằng Gmail trong **License testing** → mua → Pro → Restore | đã upload ≥1 AAB · base plan Active · service account hợp lệ |
| Mọi nơi | RevenueCat ▸ Customers: thấy giao dịch sandbox + entitlement `pro` active | |

Ghi kết quả (ngày, thiết bị, gói, Pro có/không) vào review.md và file thay đổi.

## 5. Kiểm tra khi hỏng — đi từ trên xuống

1. Log SDK: tạm thêm `await Purchases.setLogLevel(LogLevel.debug);` trước `configure` → đọc log (`run_app.py logs`, Xcode console).
   **Gỡ ra trước release.**
2. `Offerings empty` / `There is no current offering` → offering chưa **Make current** hoặc package chưa gắn sản phẩm.
3. `None of the products registered in the RevenueCat dashboard could be fetched` → iOS: Paid Apps Agreement, bundle id,
   trạng thái sản phẩm; Android: chưa upload AAB, base plan chưa Activate, cài không từ Play.
4. Mua xong không Pro → sản phẩm chưa attach entitlement `pro` / `AppConfig.entitlementId` khác tên.
5. `Invalid API key` → dùng nhầm key iOS cho Android (hoặc ngược lại) / dán nhầm secret key.
6. Restore trống → tài khoản store lúc restore khác lúc mua; sandbox ≠ production.

Vẫn kẹt: skill `revenuecat-troubleshoot` (plugin) · docs.revenuecat.com ▸ Troubleshooting · community.revenuecat.com.
