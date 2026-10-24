# Trial + license key cho app Mac

Quyết định ở bước 2 (`/app-money`, dòng `Trial:` và `License check:` trong money.md), code sinh sẵn ở bước 5
(`new_macos_app.py`), nối bản thật ở lát Paywall (`/app-build`), soi ở bước 9 (`check_macos.py`).

Trial trên Mac **không có một cách chung** — nó đi theo đường bán (`distribution`) và mô hình (`Model`):

| | `mas` — Mac App Store | `direct` — .dmg trên web |
|---|---|---|
| **subscription** | Introductory offer "Free" của StoreKit, gắn vào gói năm. Apple đếm ngày, tự trừ tiền khi hết. App không giữ đồng hồ nào | Cổng thanh toán lo trial của subscription (Lemon Squeezy / Paddle đều có). App chỉ đọc trạng thái qua license key |
| **one-time (mua đứt)** | IAP **Non-Consumable giá 0** tên "14-day Trial" (Apple 3.1.1). Ngày bắt đầu = ngày "mua" IAP đó. App tự đếm bằng `TrialPolicy` | App tự đếm: `TrialTracker` + `KeychainTrialStore`, bắt đầu từ lần mở đầu tiên. Hết hạn → nhập license key |

## Luật chung — áp cho cả 4 ô

1. **Hết trial = quay về Free, không khoá app.** File, dữ liệu, lịch sử của người dùng vẫn mở được. Khoá dữ liệu
   người dùng tạo ra là cách nhanh nhất để ăn review 1 sao (và trái luật `app-money` bước 2).
2. **Một trial cho một người, một lần.** Gọi `begin()` bao nhiêu lần cũng không kéo dài thêm ngày; xoá app cài lại
   không reset (Keychain còn nguyên). Không chống được người cố tình (đổi user macOS, xoá Keychain) — không cần:
   người đó không phải khách hàng. Đừng tốn công DRM.
3. **Paywall nói rõ khi nào trừ tiền** (subscription) hoặc **khi nào hết dùng thử** (mua đứt). `check_money.py` FAIL
   nếu `## Paywall` của subscription có trial mà không nói lúc trừ tiền.
4. **Độ dài**: 7 hoặc 14 ngày cho tiện ích Mac. Dưới 3 ngày không kịp thấy giá trị; trên 30 ngày người ta quên app.
   `check_money.py` WARN ngoài 3–30.
5. **Không trial trên gói tuần** (bị coi là bẫy thu phí) — `check_money.py` WARN.

## money.md — ghi thế nào

```
Trial: 14 days            # hoặc: none · 7 days · 2 weeks
License check: lemonsqueezy   # chỉ direct: lemonsqueezy | keygen | own-server. mas: none
```

Bảng `## Products`, cột `Trial`:

| Ô | Dòng phải có |
|---|---|
| mas + subscription | gói năm ghi `14 days` ở cột Trial (introductory offer); gói tháng `none` |
| mas + one-time | thêm dòng `<slug>_trial_14d \| non-consumable \| 14 days \| 0 \| —` — đây LÀ trial |
| direct | cột Trial `none` cho mọi dòng — trial do app đếm, không phải một sản phẩm |

## Code đã sinh sẵn (`new_macos_app.py`)

| File | Là gì | Test |
|---|---|---|
| `Core/Trial.swift` | `TrialPolicy` (luật thuần: ngày bắt đầu + giờ hiện tại → `TrialState`), `TrialTracker` (bắt đầu đúng một lần), `TrialStore` + `InMemoryTrialStore` + `KeychainTrialStore`, `Access` (gộp mua + trial thành quyền dùng) | `TrialTests.swift` |
| `Core/Keychain.swift` | `KeychainItem` — đọc/ghi một ô chuỗi trong Keychain đăng nhập | không test tự động (không ghi vào Keychain thật trong test) |
| `Core/License.swift` (chỉ `direct`) | `LicenseService` + `FakeLicenseService` (nhận key `TEST-xxxx`) + `LemonSqueezyLicenseService` | `LicenseTests.swift` (bản Fake) |
| `App/*` | `RootViewModel.access`, dòng "Pro trial — N days left", ô nhập license key trong Paywall, nút "Deactivate this Mac" trong Settings | chạy app, chụp màn hình |

Số ngày lấy từ dòng `Trial:` của money.md lúc scaffold (hoặc `--trial-days N`). Đổi sau: sửa
`TrialPolicy(days: N)` trong `<Name>App.swift` — `check_macos.py` FAIL nếu lệch money.md.

### Đồng hồ bị vặn lùi

`TrialPolicy.state` coi đồng hồ lùi **quá 1 ngày** so với ngày bắt đầu là hết hạn. Một ngày dung sai cho đổi múi giờ /
đồng bộ giờ; lùi xa hơn là cố tình.

### Keychain khi đang dev (chữ ký tạm)

Chữ ký ad-hoc đổi sau mỗi `make app`, nên macOS có thể hỏi "Sweepy wants to use your confidential information stored
in … keychain" sau mỗi lần build. Bấm **Always Allow**. Muốn thử lại từ đầu trial:

```bash
security delete-generic-password -s "<bundle_id>.trial" -a start      # xoá ngày bắt đầu
security delete-generic-password -s "<bundle_id>.license" -a key      # xoá key đã kích hoạt
```

Bản đã ký Developer ID thì chữ ký ổn định, người dùng thật không bị hỏi.

## `direct` — license key

### Chọn cổng kiểm key (`License check:`)

| Giá trị | Khi nào | Ghi chú |
|---|---|---|
| `lemonsqueezy` | bán qua Lemon Squeezy (mặc định cho người mới) | License API công khai, **không cần API key trong app**: `activate` · `validate` · `deactivate`. Bật "Generate license keys" cho sản phẩm |
| `keygen` | bán qua Paddle / Stripe | Paddle Billing và Stripe không tự phát license key → dùng Keygen (keygen.sh) nhận webhook tạo key. Kiểm lại docs của cổng lúc làm — tính năng cổng thanh toán đổi nhanh |
| `own-server` | đã có backend | tự viết; vẫn theo hợp đồng `LicenseService` |

`check_money.py` FAIL khi `direct` bán mà thiếu `License check:`, và khi `Provider` là Paddle/Stripe mà
`License check: lemonsqueezy` (API Lemon Squeezy chỉ kiểm key do Lemon Squeezy phát).

### Luồng người dùng

1. Mở app lần đầu → trial bắt đầu, thanh trên cùng "Pro trial — 14 days left".
2. Bấm Upgrade → Paywall → "Buy" mở trang checkout trên trình duyệt (link Lemon Squeezy).
3. Email về có license key → dán vào ô "License key" trong Paywall → **Activate** → Pro.
4. Mỗi lần mở app: `validate()` kiểm lại. **Mất mạng** → tin lần kiểm gần nhất trong 7 ngày
   (`LemonSqueezyLicenseService.offlineGraceDays`). Key bị hoàn tiền / vô hiệu → server trả `valid: false` → về Free.
5. Đổi máy: Settings ▸ **Deactivate this Mac** → trả chỗ kích hoạt → dán key trên máy mới.
   Giới hạn số máy đặt ở Lemon Squeezy ("Activation limit", gợi ý 2–3).

### Nối bản thật (lát Paywall ở `/app-build`)

Người dùng làm trên Lemon Squeezy: tạo store, tạo product, bật license key, ghi lại **product ID** (số).
Claude làm, trong `<Name>App.swift`:

```swift
private let licenses: (any LicenseService)? = LemonSqueezyLicenseService(
    productID: 123456,                       // Lemon Squeezy ▸ Products ▸ ID — số, không phải bí mật
    bundleID: "com.you.app"
)
```

`LemonSqueezyLicenseService` **bắt buộc so `meta.product_id`**: License API của Lemon Squeezy nhận key của bất kỳ shop
nào trên nền tảng — không so product ID là ai có key của app khác cũng mở được Pro của bạn. Key sai sản phẩm bị trả
lại chỗ kích hoạt rồi từ chối.

`check_macos.py` FAIL (bản đầy đủ) / WARN (`--pre`) khi `<Name>App.swift` còn `FakeLicenseService()` — bản giả nhận
mọi key `TEST-…`, phát hành nó là phát Pro miễn phí.

Không bao giờ bỏ vào app: API key Lemon Squeezy (`eyJ…` dài), secret của Keygen, webhook secret. License API không
cần chúng; `check_macos.py` đã FAIL với `sk_…`.

### Thử không tốn tiền

Lemon Squeezy ▸ bật **Test mode** → mua bằng thẻ test → key test về email → Activate trong app. Trong test mode key
chỉ chạy với sản phẩm test — `productID` lúc đó là ID của bản test.

## `mas` — StoreKit

Code StoreKit 2 thật viết ở lát Paywall (scaffold chỉ có `FakeSubscriptionService`). Phần trial:

**Subscription + introductory offer**

- App Store Connect ▸ gói năm ▸ Subscription Prices ▸ **Introductory Offers** ▸ Free, 1 hoặc 2 tuần. Người dùng làm.
- Chỉ hiện chữ "14 days free" khi `await product.subscription?.isEligibleForIntroOffer == true` — người đã dùng
  trial rồi mà vẫn thấy chữ đó là Apple từ chối (3.1.2, lời hứa sai). `check_macos.py` WARN nếu code không gọi.
- Trong thời gian trial, `Transaction.currentEntitlements` đã trả gói đó → `Entitlement.pro`. Không cần `TrialTracker`.
- Paywall: "14 days free, then $19.99/year. Cancel anytime in App Store settings." — nói giá sau trial.

**Mua đứt + IAP giá 0**

- App Store Connect ▸ In-App Purchases ▸ **Non-Consumable**, giá 0, tên "14-day Trial" (Apple 3.1.1 bắt đúng kiểu
  tên "XX-day Trial"). Product ID `<slug>_trial_14d`.
- Paywall có nút "Start 14-day free trial" → mua IAP đó → ngày bắt đầu = `transaction.originalPurchaseDate`.
- Viết một `TrialStore` đọc ngày đó từ `Transaction.currentEntitlements(for: "<slug>_trial_14d")` rồi đưa vào
  `TrialTracker` — luật đếm ngày (`TrialPolicy`) dùng lại nguyên, test đã có.
- Trước khi dùng trial, app phải cho dùng được **một phần** (Free) — Apple không nhận app mở ra chỉ có nút trial.
- Hết trial → nút "Unlock Pro — $9.99" (IAP non-consumable thật) + vẫn dùng Free.

## Việc của người dùng, Claude không làm thay

Tạo store/product/bật license key trên Lemon Squeezy · tạo Introductory Offer / IAP giá 0 trên App Store Connect ·
nhập thuế, ngân hàng · mua thử bằng thẻ test hoặc Sandbox Apple Account.
