---
name: app-macos
description: "Skill nhánh macOS của pipeline app — dùng khi app.json stack là macos: app Mac để bàn viết bằng Swift 6 + SwiftUI, project là gói SwiftPM text thuần (không .xcodeproj để Claude phá), logic nằm trong <Name>Core không import SwiftUI nên test được, luật CỨNG khi động vào file của người dùng (không try!/as!, không xoá thẳng mà đưa vào Thùng rác, chỉ đọc thư mục người dùng tự chọn qua security-scoped bookmark), sandbox + entitlement, FSEvents theo dõi thư mục, dedupe bằng SHA-256, nén ảnh bằng ImageIO/Core Image và video bằng AVFoundation (KHÔNG nhúng ffmpeg/HandBrake vì GPL), chạy + chụp màn hình app thật bằng run_macos.sh, ký Developer ID + notarize hoặc nộp Mac App Store, trial + license key (dùng thử N ngày lưu Keychain, kích hoạt key Lemon Squeezy, trial StoreKit). Khác app điện thoại từ cách bán tiền tới cách nộp store. Used by app-build, app-feature, app-fix on macOS apps. Use when 'làm app mac', 'app macos', 'app để bàn', 'swiftui macos', 'menu bar app', 'app dọn file trên mac', 'notarize', 'dmg', 'sparkle', 'sandbox macos', 'security-scoped bookmark', 'nén ảnh video trên mac', 'tìm file trùng', 'trial app mac', 'dùng thử 14 ngày', 'license key', 'kích hoạt bản quyền', 'lemon squeezy', 'hết hạn dùng thử'."
argument-hint: "[slug]"
user-invocable: true
---

# app-macos — Swift 6 + SwiftUI cho app Mac để bàn

Được gọi từ `/app-scaffold`, `/app-build`, `/app-feature`, `/app-fix` khi `apps/ACTIVE/<slug>/app.json` có `"stack": "macos"`.

## App Mac KHÁC app điện thoại ở đâu (đọc trước khi gõ dòng nào)

| | iOS/Android | macOS |
|---|---|---|
| Bán tiền | chỉ qua store, RevenueCat | **hai đường**: Mac App Store (StoreKit, Apple cắt 15–30%) hoặc bán thẳng (.dmg + Paddle/Lemon Squeezy/Stripe, tự thu 100%) |
| Nộp bài | bắt buộc qua store | ngoài store được — nhưng **bắt buộc ký Developer ID + notarize**, không thì Gatekeeper chặn |
| Cập nhật | store đẩy | ngoài store tự lo (Sparkle + appcast.xml) |
| File của người dùng | app chỉ thấy hộp cát của nó | app đụng thẳng vào `~/Downloads`, ổ ngoài… — **một dòng sai là mất file thật của người ta** |
| Cửa sổ | một màn hình đầy | nhiều cửa sổ, sidebar, menu bar, kéo thả, phím tắt, Settings riêng |
| Ảnh store | ảnh dọc điện thoại | 16:10 ngang: 1280×800 · 1440×900 · 2560×1600 · 2880×1800 |

Quyết định `direct` hay `mas` nằm ở **bước 2 (`/app-money`)** và ghi trong `app.json` → nó đổi entitlement, cách ký,
cách nén video (license) và cả trang listing. Đổi sau là làm lại nhiều thứ — chốt sớm.

## Tạo project (bước 5)

```bash
python3 scripts/native/new_macos_app.py <slug>          # đọc app.json: name, bundle id, distribution, min_macos, about, technical, legal_url
python3 scripts/design_tokens.py <slug>                 # theme từ design.md
cd apps/ACTIVE/<slug>/source/mac && make check                        # lint + test phải xanh trước khi sang bước 6
```

Sinh ra gói SwiftPM — **không có `.xcodeproj`**. Lý do: `.pbxproj` là một đống UUID, sửa bằng tay là hỏng project;
`Package.swift` thì đọc, sửa, diff được như code. Cần Xcode (chỉ khi nộp Mac App Store): `make xcodeproj` sinh lại từ `project.yml`.

```
mac/
  Package.swift              exe <Name>App · thư viện <Name>Core · test <Name>CoreTests
  Makefile                   make check | run | app | dmg | sign | notarize
  Resources/Info.plist       CFBundleVersion — tăng mỗi lần nộp
  Resources/<Name>.entitlements
  Sources/<Name>Core/        LOGIC THUẦN, không một dòng SwiftUI  ← mọi test ở đây
  Sources/<Name>App/         SwiftUI: App, View, ViewModel
  Tests/<Name>CoreTests/     Swift Testing
```

## Kiến trúc — một luật, không ngoại lệ

| Lớp | Là gì | Luật |
|---|---|---|
| `<Name>Core` | luật nghiệp vụ, đụng file, hash, nén | **không `import SwiftUI` / `import AppKit`**. Việc nặng là `actor`. Mọi kiểu đi qua biên là `Sendable` |
| ViewModel | `@MainActor @Observable final class XViewModel` | giữ trạng thái, gọi Core bằng `async`. Không `import SwiftUI` |
| View | `struct XView: View` | **chỉ vẽ + gọi ViewModel**. Không `if` nghiệp vụ, không đụng `FileManager` |
| Service | `protocol XService: Sendable` + bản thật + `FakeXService` | View/ViewModel chỉ biết protocol. Fake để chạy khi chưa có tài khoản bán hàng |

Mẫu code đầy đủ, luật đặt tên theo Swift API Design Guidelines, bảng lỗi hay gặp:
[references/swift-strict.md](references/swift-strict.md).

## Luật CỨNG của app động vào file người khác

Đây là phần khác mọi app khác trong repo này: sai không phải xấu UI, mà là **mất ảnh cưới của người ta**.

1. **Không bao giờ `try!`, `as!`, `!` mở optional** trong code đụng file. `check_macos.py` bắt `try!`/`as!` là FAIL.
2. **Không `removeItem`.** Xoá = `FileManager.trashItem` (Thùng rác, người dùng Put Back lại được). Core có sẵn `SafeTrash`.
3. **Không ghi đè.** Trùng tên thì đổi tên (`photo 2.png`), như `SafeTrash.move` đang làm.
4. **Không sửa bản gốc khi nén.** Ghi ra file mới, so kích thước, người dùng bấm đồng ý, bản gốc mới vào Thùng rác.
5. **Chỉ vào thư mục người dùng tự chọn** qua `NSOpenPanel`, rồi giữ quyền bằng **security-scoped bookmark**. Không đòi Full Disk Access khi chưa cần.
6. **Mỗi thao tác hàng loạt phải có "hoàn tác"**: ghi nhật ký `từ → đến` ra đĩa trước khi chạy.
7. **Thử trên thư mục giả trước.** Test tạo thư mục tạm, không bao giờ trỏ vào `~/Downloads` thật.

Chi tiết + code: [references/file-safety.md](references/file-safety.md) (bookmark, FSEvents, SHA-256 dedupe, hoàn tác).

## Nén ảnh / video — bẫy license

| Việc | Dùng | KHÔNG dùng |
|---|---|---|
| Nén ảnh | `ImageIO` (`CGImageDestination`, `kCGImageDestinationLossyCompressionQuality`), `Core Image` | nhúng `mozjpeg`/`pngquant` binary khi chưa đọc license từng cái |
| Nén video | `AVFoundation` (`AVAssetExportSession`, `AVAssetWriter`, HEVC hardware) | **ffmpeg / HandBrakeCLI / x264 — GPL**: Mac App Store không nhận, bán ngoài store thì phải mở source cả app |

`check_macos.py` quét và FAIL nếu thấy binary GPL trong `mac/`. Chi tiết tham số nén: [references/media.md](references/media.md).

## Trial + license key

Quyết định ở `money.md` (`Trial: none | <N> days`, `License check:` cho `direct`), code sinh sẵn ở bước 5:

| | `mas` | `direct` |
|---|---|---|
| subscription | Introductory offer của StoreKit (gói năm) — chỉ hiện chữ trial khi `isEligibleForIntroOffer` | cổng thanh toán lo trial; app đọc qua license key |
| mua đứt | IAP Non-Consumable **giá 0** "14-day Trial" (Apple 3.1.1) → `TrialPolicy` đếm từ ngày mua IAP đó | `TrialTracker` + `KeychainTrialStore` đếm từ lần mở đầu → hết hạn nhập license key |

Có sẵn trong `<Name>Core`: `TrialPolicy` · `TrialTracker` · `KeychainTrialStore` · `Access` (mua **hoặc** đang trial) ·
`LicenseService` + `FakeLicenseService` · `LemonSqueezyLicenseService` (chỉ `direct`, bắt buộc so `product_id`,
7 ngày offline). ViewModel: `isPro` (được dùng Pro) khác `hasPurchased` (đã trả tiền) — nút mua hỏi cái sau.

Luật: **hết trial = về Free, không khoá app, không đụng dữ liệu** · một người một trial, cài lại không reset ·
phát hành còn `FakeLicenseService()` là `check_macos.py` FAIL · số ngày trong code phải khớp money.md.
Chi tiết, luồng người dùng, cách thử bằng Test mode: [references/trial-license.md](references/trial-license.md).

## Chạy · nhìn · test

```bash
python3 scripts/run_app.py run <slug> --platform macos      # build .app → mở → chụp ĐÚNG cửa sổ app
python3 scripts/run_app.py shot <slug> --platform macos --name 01-inbox   # ảnh store 16:10
cd apps/ACTIVE/<slug>/source/mac && make check                            # swiftlint --strict + swift test
```

**Luật không đổi:** build xanh ≠ UI đúng. Chụp xong phải **Read ảnh ra nhìn** rồi mới nói app chạy.

## Ký · phát hành

**Chưa có tài khoản Apple Developer vẫn làm và test được hết**: `make check` + `make run` dùng chữ ký tạm (ad-hoc),
macOS cho chạy trên chính máy đã build. Tài khoản 99 USD/năm chỉ cần khi đưa app cho **người khác** tải, hoặc nộp
Mac App Store. Đừng bắt người dùng mua tài khoản sớm hơn lúc thật sự cần — chi tiết ở references/distribution.md.

```bash
cd apps/ACTIVE/<slug>/source/mac
make app                                    # build/<Label>.app
TEAM_ID=XXXXXXXXXX make sign                # Developer ID + hardened runtime
KEYCHAIN_PROFILE=notary make notarize       # gửi Apple, đợi, staple vào .dmg
python3 scripts/check_macos.py apps/ACTIVE/<slug>  # soi trước khi phát hành
```

Người dùng tự làm: mua tài khoản Apple Developer, tạo chứng chỉ, chạy `xcrun notarytool store-credentials`, bấm phát hành.
Claude không đăng nhập, không nhập mật khẩu. Chi tiết từng lệnh + Sparkle + Homebrew cask:
[references/distribution.md](references/distribution.md).

Trang bán / trang store: `/app-macos-listing` (khác `/app-listing` của app điện thoại).

## Repo nên đọc khi bí

[references/top-repos.md](references/top-repos.md) — app Mac mã nguồn mở đáng học, đo sao ngày 2026-09-17, kèm "học cái gì ở đâu".
