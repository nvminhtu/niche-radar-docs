> Nguồn: skill cá nhân `swift-ios-code, swift-ios-test` (repo mobile-app-learning, 2026-09-15), chép vào đây làm tài liệu tham khảo cho nhánh Native.
> Chỗ nhắc `native-feature-task` / `TASK.md` / `GO-THEO.md` / `demo/...` là quy ước của repo học — trong pipeline app
> thay bằng `/app-build` (MVP) hoặc file việc trong `apps/ACTIVE/<slug>/plan/` (`/app-feature`, `/app-fix`).

# swift-ios-code — logic Swift tách khỏi SwiftUI

Có requirement cụ thể mà chưa có `TASK.md` → dùng `native-feature-task` trước.
Layout chi tiết → `native-ui-layout`. Test → `swift-ios-test`.
Port màn từ app Ionic CarMD → `swift-ios-port-ionic`. Demo đánh số + SPEC → `swift-ios-feature`.

## Cấu trúc 1 feature

```
MobileAppLearning/
├── MobileAppLearningApp.swift   tạo dependency TAY, không DI
├── AuthService.swift            protocol (Sendable) + FakeAuthService
├── RememberMeStore.swift        protocol + UserDefaultsRememberMeStore
├── LoginViewModel.swift         @MainActor @Observable — KHÔNG import SwiftUI
└── LoginView.swift              View + component nhỏ + #Preview
```

Nhiều feature → mỗi feature 1 group/thư mục (`Login/`, `Settings/`). Xcode project cũ (không
synchronized group) → thêm file mới vào target bằng `swift-ios-feature/assets/patch_pbxproj.py`.

## 3 lớp — mỗi lớp 1 việc

| Lớp | Viết thế nào | Luật |
|---|---|---|
| ViewModel | `@MainActor @Observable final class` · input `var` · output `private(set) var` · luật suy ra là computed property | `import Foundation, Observation` — **không `SwiftUI`** |
| Service/Store | `protocol` + bản thật + `Fake…` · việc chậm là `async` | Protocol gọi qua `await` → `: Sendable`. Mật khẩu → Keychain, không UserDefaults |
| View | `@State private var viewModel` · bind `$viewModel.email` · gọi `Task { await viewModel.login() }` | Không `if` nghiệp vụ trong `body` |

## Mẫu cốt lõi

```swift
@MainActor
@Observable
final class LoginViewModel {
    var email = ""
    var password = ""
    var rememberMe = false
    private(set) var isLoading = false
    private(set) var errorMessage: String?
    private(set) var isLoggedIn = false

    var canSubmit: Bool { !email.isEmpty && !password.isEmpty && !isLoading }

    private let authService: AuthService
    private let rememberMeStore: RememberMeStore

    init(authService: AuthService, rememberMeStore: RememberMeStore) {
        self.authService = authService
        self.rememberMeStore = rememberMeStore
        if let saved = rememberMeStore.savedEmail() { email = saved; rememberMe = true }
    }

    func login() async {
        guard canSubmit else { return }
        let email = email, password = password, rememberMe = rememberMe   // chụp lại trước await
        isLoading = true; errorMessage = nil
        let success = await authService.login(email: email, password: password)
        isLoading = false
        if success {
            if rememberMe { rememberMeStore.save(email: email) } else { rememberMeStore.clear() }
            isLoggedIn = true
        } else {
            errorMessage = "Sai email hoặc mật khẩu"
        }
    }
}

// View giữ ViewModel được truyền từ ngoài vào
init(viewModel: LoginViewModel, onLoggedIn: @escaping () -> Void = {}) {
    _viewModel = State(initialValue: viewModel)
    self.onLoggedIn = onLoggedIn
}
```

Điều hướng khi state đổi: `.onChange(of: viewModel.isLoggedIn) { _, v in if v { onLoggedIn() } }`.

## Thêm 1 yêu cầu vào màn có sẵn (vd "thêm checkbox")

1. Thêm `var rememberMe` vào ViewModel → 2. dùng trong `login()` → 3. test (`swift-ios-test`) →
4. `Toggle(isOn: $viewModel.rememberMe)` trong View → 5. `#Preview`.
Logic đúng trước, UI chỉ là nối dây.

## Lỗi hay gặp

| Triệu chứng | Nguyên nhân / sửa |
|---|---|
| `ObservableObject` + `@Published` + `@StateObject` | Code cũ (iOS 13–16). Deployment ≥ 17 → `@Observable` + `@State` |
| "Sending … risks causing data races" (Swift 6) | Service protocol thiếu `Sendable`, hoặc ViewModel thiếu `@MainActor` |
| Test ViewModel phải bật simulator UI | ViewModel đang `import SwiftUI` → bỏ, dùng `Observation` |
| Giá trị sai sau `await` | Đọc lại `self.email` sau await — chụp vào `let` trước |
| iOS không có `.toggleStyle(.checkbox)` | Chỉ macOS — tự viết `ToggleStyle` (xem `native-ui-layout`) |

Ví dụ đầy đủ đã chạy: `demo/swift/login-remember-me/` (repo native-mobile-learning).


---

# swift-ios-test — test logic ViewModel, không cần simulator

ViewModel không `import SwiftUI` (xem `swift-ios-code`) → test chạy trên macOS bằng `swift test`
trong vài giây. UI kiểm bằng `#Preview` + chạy simulator có screenshot (`swift-ios-build-run`).

## Chọn cách chạy

| Project có… | Làm |
|---|---|
| Test target trong Xcode (`XxxTests`) | `xcodebuild test -scheme X -destination 'platform=iOS Simulator,name=iPhone 17 Pro'` |
| Không có test target (project tạo bằng script) | Thêm `Package.swift` cạnh `.xcodeproj`, trỏ vào file logic — **không copy code** |

```swift
// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "LoginFeature",
    platforms: [.macOS(.v14), .iOS(.v17)],
    targets: [
        .target(
            name: "LoginFeature",
            path: "MobileAppLearning",                                   // thư mục app
            sources: ["LoginViewModel.swift", "AuthService.swift", "RememberMeStore.swift"] // chỉ file không import SwiftUI/UIKit
        ),
        .testTarget(name: "LoginFeatureTests", dependencies: ["LoginFeature"], path: "Tests/LoginFeatureTests"),
    ]
)
```

Chạy: `swift test`. Thêm `.build/` vào `.gitignore`. File logic mới → thêm tên vào `sources`.

## Test ViewModel — Swift Testing + fake viết tay

```swift
import Testing
@testable import LoginFeature

private struct TestAuthService: AuthService {
    let result: Bool
    func login(email: String, password: String) async -> Bool { result }
}

private final class TestRememberMeStore: RememberMeStore {
    var email: String?
    init(email: String? = nil) { self.email = email }
    func savedEmail() -> String? { email }
    func save(email: String) { self.email = email }
    func clear() { email = nil }
}

@MainActor                       // ViewModel là @MainActor → cả suite chạy trên MainActor
struct LoginViewModelTests {
    @Test func loginSuccessWithRememberMeSavesEmail() async {
        let store = TestRememberMeStore()
        let viewModel = LoginViewModel(authService: TestAuthService(result: true), rememberMeStore: store)
        viewModel.email = "a@b.com"
        viewModel.password = "123456"
        viewModel.rememberMe = true

        await viewModel.login()

        #expect(viewModel.isLoggedIn)
        #expect(store.email == "a@b.com")
    }
}
```

Chọn case từ **tiêu chí nghiệm thu** trong `TASK.md`: mỗi AC ≥ 1 test. Bộ tối thiểu cho màn form:
trạng thái ban đầu · không submit được khi thiếu input · thành công · thất bại (có lỗi, không lưu).
Làm cả Kotlin → giữ **cùng tên case** với `kotlin-android-test` để so cặp.

## Swift Testing ↔ XCTest

| Swift Testing (mặc định, Xcode 16+) | XCTest (code cũ) |
|---|---|
| `@Test func x()` trong `struct` | `func testX()` trong `class …: XCTestCase` |
| `#expect(a == b)` · `#expect(flag)` | `XCTAssertEqual(a, b)` · `XCTAssertTrue(flag)` |
| `try #require(optional)` | `try XCTUnwrap(optional)` |
| `@Test(arguments: [...])` | lặp tay |

## Lỗi hay gặp

| Lỗi | Sửa |
|---|---|
| `main actor-isolated … nonisolated context` | Thêm `@MainActor` cho suite hoặc hàm test |
| `No such module 'LoginFeature'` | Tên `@testable import` phải = tên target trong `Package.swift` |
| `swift test` lỗi `No such module 'SwiftUI'`/`UIKit` | Lỡ đưa file View vào `sources` — chỉ file logic |
| UserDefaults thật bị ghi trong test | Test phải dùng `TestRememberMeStore`, không dùng bản thật |
| Test chậm vì `Task.sleep` | Fake trong test trả ngay; `FakeAuthService` có sleep chỉ cho app demo |

Kết quả (lệnh + số test pass) ghi vào mục 6 của `TASK.md`.
