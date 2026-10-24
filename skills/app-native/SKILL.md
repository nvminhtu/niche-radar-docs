---
name: app-native
description: "Skill phụ nhánh Native của pipeline app — dùng khi app.json stack là native: Android bằng Kotlin + Jetpack Compose + Material 3 (UiState bất biến, ViewModel StateFlow, Repository interface + Fake, test JUnit + runTest) và iOS bằng Swift + SwiftUI (@Observable @MainActor ViewModel, service protocol Sendable + Fake, Swift Testing); cách scaffold không cần mở Android Studio/Xcode, bảng quy đổi layout Compose ↔ SwiftUI, chạy/bấm/chụp bằng scripts/native, gắn RevenueCat SDK native, và khi nào nên chọn native thay Flutter. Tài liệu chép từ bộ skill học mobile-app-learning. Used by app-build, app-feature, app-fix on native apps. Use when 'làm app native', 'kotlin compose', 'swiftui', 'viết viewmodel kotlin', 'viết viewmodel swift', 'layout compose', 'layout swiftui', 'app chỉ android', 'app chỉ ios', 'nên dùng native hay flutter'."
user-invocable: false
---

# app-native — Kotlin/Compose + Swift/SwiftUI

Được gọi từ `/app-build`, `/app-feature`, `/app-fix` khi `apps/ACTIVE/<slug>/app.json` có `"stack": "native"`.

## Khi nào native (quyết ở `/app-spec`)

| Chọn native khi | Ở lại Flutter khi |
|---|---|
| Chỉ một nền tảng | cần cả iOS + Android (mặc định) |
| Tính năng hệ điều hành sâu: widget màn khoá / Live Activities, HealthKit, Wear OS, BLE nặng, App Intents | màn hình + dữ liệu + subscription |
| Đã có code native sẵn | người không biết code muốn một codebase |

Cả hai nền tảng native = **mọi tính năng làm hai lần**. Nói rõ cái giá này với người dùng.

## Tạo project

```bash
S=scripts/native
python3 $S/new_android_app.py --name <Name> --package <bundle_id> --label "<Label>" --dir apps/ACTIVE/<slug>/source/android
python3 $S/new_ios_app.py --name <Name> --dir apps/ACTIVE/<slug>/source/ios --bundle-id <bundle_id> --deployment 17.0
python3 scripts/design_tokens.py <slug>
```

Android stack đã build thật: AGP 8.13.2 · Kotlin 2.4.20 · Compose BOM 2026.06.01 · compileSdk/targetSdk 36 · minSdk 26.
Không "sửa" cảnh báo lint "newer version available" — BOM 2026.09 đòi AGP 9.1 + compileSdk 37.

## Kiến trúc — cùng tên lớp hai bên để so cặp

| Lớp | Kotlin / Compose | Swift / SwiftUI |
|---|---|---|
| State | `data class XUiState` + thuộc tính suy ra `val canX get()` | property trong ViewModel + computed `var canX: Bool` |
| ViewModel | `class XViewModel(repo) : ViewModel()` · `StateFlow` · `viewModelScope` · **không import Compose** | `@MainActor @Observable final class XViewModel` · `async func` · **không import SwiftUI** |
| Repository | `interface XRepository` + bản thật + `FakeXRepository` | `protocol XService: Sendable` + bản thật + `FakeXService` |
| UI stateful | `XScreen(viewModel)` + `collectAsStateWithLifecycle()` | `XView` + `@State private var viewModel` |
| UI stateless | `XContent(state, onA, onB)` + `@Preview` | view nhận `Binding`/closure + `#Preview` |
| Lưu nhẹ | DataStore Preferences | `UserDefaults` (bí mật → Keychain) |
| Test | JUnit4 + `kotlinx-coroutines-test` `runTest` + `MainDispatcherRule` | Swift Testing `@Test` `#expect` |

Mẫu code đầy đủ + lỗi hay gặp:
[references/kotlin-compose.md](references/kotlin-compose.md) ·
[references/swift-swiftui.md](references/swift-swiftui.md) ·
[references/ui-layout.md](references/ui-layout.md) (bảng quy đổi Column/Row ↔ VStack/HStack, checkbox, form, loading).

## Build · chạy · bấm · test

```bash
python3 scripts/run_app.py run <slug> --platform android      # → scripts/native/run_android.sh
python3 scripts/run_app.py run <slug> --platform ios          # → scripts/native/run_ios.sh
python3 scripts/native/android_ui.py dump | tap "<chữ>" | text "<chữ>" | shot store/android/01.png
python3 scripts/test_app.py <slug>                            # gradlew testDebugUnitTest + xcodebuild test
```

## Subscription native (chi tiết ở `app-paywall`)

- Android: `com.revenuecat.purchases:purchases` (+ `purchases-ui` nếu dùng RevenueCat Paywalls) — thêm vào `libs.versions.toml`, build ngay.
- iOS: Swift Package `https://github.com/RevenueCat/purchases-ios-spm` — thêm bằng Xcode (File ▸ Add Package Dependencies), người dùng bấm hoặc sửa pbxproj có kiểm.
- Cùng hợp đồng như bản Flutter: `SubscriptionRepository` (Kotlin interface / Swift protocol) + bản RevenueCat + bản Fake.

## Skill chính chủ nên đọc khi đi sâu

`android/skills` (Google — edge-to-edge, navigation-3, camerax, r8-analyzer, play-policy-insights, testing-setup) ·
`Kotlin/kotlin-agent-skills` (JetBrains) · `chrisbanes/skills` (compose performance, state & effects) ·
iOS: `tucarmd/claude-code-skills` (fork bộ skill iOS 26 / Swift 6.3 / SwiftUI). Bảng cài: reference/README-REFERENCES.md.
