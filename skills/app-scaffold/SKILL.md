---
name: app-scaffold
description: "Bước 5 của pipeline app — tạo project chạy được trước khi viết tính năng: nhánh Flutter (mặc định) sinh apps/ACTIVE/<slug>/source/app bằng scripts/new_flutter_app.py với Flutter ghim qua fvm, bundle id đúng cho iOS + Android, kiến trúc chính chủ UI → ViewModel → Repository, khung subscription RevenueCat có bản Fake để chạy khi chưa có key, paywall đủ thành phần store bắt buộc, theme sinh từ design.md, test xanh sẵn; nhánh Native sinh android/ (Kotlin + Compose, stack đã pin) và ios/ (SwiftUI, không cần mở Xcode); nhánh macOS sinh mac/ (gói SwiftPM Swift 6 + SwiftUI, Makefile build/ký/notarize, SwiftLint strict, test Swift Testing — không .xcodeproj). Chứng minh bằng analyze + test trước khi sang bước build. Use when someone wants to create the app project, 'tạo project flutter', 'khởi tạo app', 'scaffold app', 'tạo project android ios', 'tạo project app mac', 'swiftpm', 'bundle id đặt ở đâu', 'flutter create', or when scripts/app.py status says step 5 is next. Không viết tính năng."
argument-hint: "[slug]"
user-invocable: true
---

# Bước 5 — scaffold

**Một việc:** project tồn tại, `analyze` sạch, `test` xanh. **Không viết tính năng.**

Điều kiện: CỔNG 3 đã qua (design.md `Approved: yes`) — theme sinh từ nó — và bước 4b `mockup.md` 0 FAIL
(ảnh từng màn ở `design/mockup/`, bước build code bám theo). Stack đọc từ `apps/ACTIVE/<slug>/app.json`.

## Flutter (mặc định)

```bash
python3 scripts/new_flutter_app.py <slug>     # ~1–3 phút: create → ghi khung → pub add → analyze → test
python3 scripts/test_app.py <slug>            # ghi run/out/tests.json
python3 scripts/app.py status <slug>          # bước 5 phải ok
```

Script làm gì (giải thích cho người dùng bằng lời thường — đây là bản đồ app họ sẽ sống cùng):

```
apps/ACTIVE/<slug>/source/app/
├── lib/main.dart                         cửa vào: có key RevenueCat → dùng thật, chưa có → bản giả (Fake)
├── lib/config/app_config.dart            mọi cấu hình một chỗ (key public, link Terms/Privacy)
├── lib/data/repositories/                "kho": nói chuyện với RevenueCat / lưu dữ liệu. Có bản Fake để test
├── lib/routing/router.dart               danh sách màn: / · /paywall · /settings
├── lib/ui/core/theme/tokens.dart         SINH TỪ design.md — không sửa tay
├── lib/ui/core/app_strings.dart          mọi chữ người dùng thấy (dịch app = dịch file này)
├── lib/ui/<màn>/<màn>_screen.dart        chỉ VẼ
├── lib/ui/<màn>/<màn>_view_model.dart    mọi LUẬT của màn (test được không cần điện thoại)
├── test/ui/                              test ViewModel + test paywall đủ thành phần store bắt buộc
├── config/dev.json                       giá trị truyền lúc build (--dart-define-from-file)
└── .fvmrc                                ghim Flutter 3.47.4 cho riêng app này
```

Việc script tự lo mà người dùng nên biết:
- Bundle id iOS = applicationId Android = `app.json` `bundle_id`.
- Xoá `DEVELOPMENT_TEAM` mà `flutter create` tự gắn từ chứng chỉ có sẵn trên máy — app phải ký bằng Team **của người dùng** ở bước 9.
- Info.plist có `ITSAppUsesNonExemptEncryption = false` (khỏi bị hỏi mã hoá mỗi lần upload).
- Lưu dấu vân tay icon mặc định → `check_release.py` báo nếu quên thay icon.
- Không ghi đè project đã có.

Xong thì chạy thử luôn để người dùng **thấy** app: `/app-run` (bản Fake: bấm Upgrade → Continue → thành Pro).

## Native

```bash
S=scripts/native
python3 $S/new_android_app.py --name <Name> --package <bundle_id> --label "<Label>" --dir apps/ACTIVE/<slug>/source/android
(cd apps/ACTIVE/<slug>/source/android && ./gradlew assembleDebug testDebugUnitTest --console=plain -q)
python3 $S/new_ios_app.py --name <Name> --dir apps/ACTIVE/<slug>/source/ios --bundle-id <bundle_id> --deployment 17.0
(cd apps/ACTIVE/<slug>/source/ios && xcodebuild -list)
python3 scripts/design_tokens.py <slug>       # Tokens.kt + Tokens.swift
```

Android: AGP 8.13.2 · Kotlin 2.4.20 · Compose BOM 2026.06.01 · compileSdk/targetSdk 36 — đã build thật; lint báo
"có bản mới hơn" là **cố ý** (BOM 2026.09 đòi AGP 9.1 + compileSdk 37). iOS: project SwiftUI sinh không cần Xcode GUI.
Chi tiết kiến trúc + layout: `app-native`.

## macOS (`stack: macos`)

```bash
python3 scripts/native/new_macos_app.py <slug>     # đọc app.json: name, bundle id, distribution, min_macos, about, technical, legal_url
python3 scripts/design_tokens.py <slug>            # Tokens.swift
(cd apps/ACTIVE/<slug>/source/mac && make check)                 # swiftlint --strict + swift test — phải xanh
```

Sinh gói SwiftPM, **không** `.xcodeproj` (file .pbxproj toàn UUID, sửa tay là hỏng). Cần Xcode để nộp Mac App Store:
`make xcodeproj` sinh lại từ `project.yml`. Logic nằm ở `Sources/<Name>Core` (không import SwiftUI → test được),
giao diện ở `Sources/<Name>App`. Luật viết code + luật đụng vào file người dùng: `app-macos`.

Có sẵn **Settings → About** (`AboutView.swift`): giới thiệu ngắn (`about` trong app.json), mục **Technical** — công nghệ
đang dùng, tuỳ chọn (`technical` trong app.json; bỏ trống → tự điền theo stack; `[]` → ẩn), và link About · Technical ·
Support · Privacy · Terms trong `enum AppLinks` (Paywall dùng chung). Gốc link: `legal_url` (VD
`https://oneclicktool.app/legal/apps/<slug>/`), không có thì `site_url` + `/privacy.html`. Điền `about` trước khi scaffold —
không thì app hiện chữ `TODO`.

## Lỗi hay gặp

| Triệu chứng | Sửa |
|---|---|
| `chưa có Flutter 3.47.4` | `bash scripts/setup_flutter.sh` |
| `pub add` lỗi mạng / version solving failed | chạy lại; vẫn lỗi → đọc dòng `because ...`, báo người dùng thư viện nào xung đột |
| analyze có `info` | sửa theo gợi ý; `warning`/`error` thì bắt buộc sửa trước khi đi tiếp |
| `CocoaPods not installed` (lần build iOS đầu) | `brew install cocoapods` |
| `SDK location not found` (native) | `local.properties` → `sdk.dir=$HOME/Library/Android/sdk` |
| `swift test` không thấy `Testing` (macOS) | cần Swift 6 — kiểm `swift --version`, cập nhật Xcode |
| app Mac mở rồi tắt ngay | chạy file nhị phân trần thay vì `.app` — dùng `make run` |

LEARNED.md mục **Bước 5** (vẽ lại cây thư mục trên bằng lời của người dùng) · `scripts/app.py log` · tiếp theo `/app-build`.
