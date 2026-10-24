> Nguồn: skill cá nhân `kotlin-android-code, kotlin-android-test` (repo mobile-app-learning, 2026-09-15), chép vào đây làm tài liệu tham khảo cho nhánh Native.
> Chỗ nhắc `native-feature-task` / `TASK.md` / `GO-THEO.md` / `demo/...` là quy ước của repo học — trong pipeline app
> thay bằng `/app-build` (MVP) hoặc file việc trong `apps/ACTIVE/<slug>/plan/` (`/app-feature`, `/app-fix`).

# kotlin-android-code — logic Kotlin tách khỏi Compose UI

Có requirement cụ thể mà chưa có `TASK.md` → dùng `native-feature-task` trước.
Layout chi tiết → `native-ui-layout`. Test → `kotlin-android-test`.

## Cấu trúc 1 feature (package theo feature, không theo loại)

```
app/src/main/java/<pkg>/
├── MainActivity.kt            setContent { … } — tạo dependency TAY, không DI
├── data/
│   ├── AuthRepository.kt      interface + FakeAuthRepository
│   └── RememberMeStore.kt     interface + PrefsRememberMeStore
└── feature/login/
    ├── LoginUiState.kt        data class bất biến + luật suy ra (canSubmit)
    ├── LoginViewModel.kt      StateFlow<UiState> + hàm onXxx()
    └── LoginScreen.kt         LoginScreen (stateful) + LoginContent (stateless) + @Preview
```

## 4 lớp — mỗi lớp 1 việc

| Lớp | Viết thế nào | Luật |
|---|---|---|
| `UiState` | `data class` mặc định rỗng, `val` hết | Không `Context`, không Compose. Luật suy ra để `get()` |
| `ViewModel` | `MutableStateFlow` private + `StateFlow` public · `_uiState.update { it.copy(...) }` · async trong `viewModelScope.launch` | **Không import `androidx.compose.*`**. Nhận repository qua constructor |
| Repository/Store | `interface` + 1 bản thật + 1 bản `Fake…` | `suspend fun` cho việc chậm. Không lưu mật khẩu vào prefs |
| UI | `XxxScreen(viewModel, onNavigate)` đọc `collectAsStateWithLifecycle()` → gọi `XxxContent(state, onA, onB)` | `Content` không biết ViewModel → Preview + UI test dễ |

## Mẫu cốt lõi

```kotlin
data class LoginUiState(
    val email: String = "", val password: String = "", val rememberMe: Boolean = false,
    val isLoading: Boolean = false, val errorMessage: String? = null, val isLoggedIn: Boolean = false,
) {
    val canSubmit get() = email.isNotBlank() && password.isNotBlank() && !isLoading
}

class LoginViewModel(
    private val authRepository: AuthRepository,
    private val rememberMeStore: RememberMeStore,
) : ViewModel() {
    private val _uiState = MutableStateFlow(LoginUiState())
    val uiState: StateFlow<LoginUiState> = _uiState.asStateFlow()

    init { rememberMeStore.savedEmail()?.let { saved -> _uiState.update { it.copy(email = saved, rememberMe = true) } } }

    fun onRememberMeChange(checked: Boolean) = _uiState.update { it.copy(rememberMe = checked) }

    fun onLoginClick() {
        val current = _uiState.value
        if (!current.canSubmit) return
        _uiState.update { it.copy(isLoading = true, errorMessage = null) }
        viewModelScope.launch {
            val success = authRepository.login(current.email, current.password)
            if (success) { if (current.rememberMe) rememberMeStore.save(current.email) else rememberMeStore.clear() }
            _uiState.update { it.copy(isLoading = false, isLoggedIn = success, errorMessage = if (success) null else "Sai email hoặc mật khẩu") }
        }
    }
}

// MainActivity: tạo ViewModel có tham số mà không cần Factory class
val vm = viewModel { LoginViewModel(FakeAuthRepository(), PrefsRememberMeStore(appContext)) }
```

Điều hướng 1 lần khi state đổi: `LaunchedEffect(state.isLoggedIn) { if (state.isLoggedIn) onLoggedIn() }` —
không gọi `onLoggedIn()` thẳng trong thân Composable.

## Dependency cần (Compose BOM giữ 2026.06.x khi còn AGP 8.13)

`lifecycle-viewmodel-compose` (hàm `viewModel {}`) · `lifecycle-runtime-compose` (`collectAsStateWithLifecycle`).
Kiểm tra `gradle/libs.versions.toml` của project trước khi thêm — không đoán version.

## Thêm 1 yêu cầu vào màn có sẵn (vd "thêm checkbox")

1. Thêm field vào `UiState` (`rememberMe`) → 2. thêm `onXxxChange` ở ViewModel →
3. dùng field trong logic (`onLoginClick`) → 4. test (`kotlin-android-test`) →
5. thêm tham số `state.x` + lambda vào `Content`, truyền từ `Screen` → 6. Preview.
Đi theo thứ tự này: logic đúng trước, UI chỉ là nối dây.

## Lỗi hay gặp

| Triệu chứng | Nguyên nhân / sửa |
|---|---|
| Luật `if` nghiệp vụ nằm trong Composable | Chuyển thành field suy ra trong `UiState` hoặc hàm ViewModel |
| `mutableStateOf` trong ViewModel + `StateFlow` lẫn lộn | Chọn 1: `StateFlow<UiState>` |
| Truyền `ViewModel` xuống component con | Chỉ truyền `state` + lambda |
| `Context` trong ViewModel để đọc prefs | Bọc prefs vào `Store` interface, truyền vào constructor |
| Ghi đè state khi async xong bằng `value = current.copy` | Dùng `update { it.copy }` — giữ thay đổi người dùng gõ trong lúc chờ |

Ví dụ đầy đủ đã chạy: `demo/kotlin/login-remember-me/` (repo native-mobile-learning).


---

# kotlin-android-test — test logic trước, UI sau

| Loại | Thư mục | Chạy | Cần máy? |
|---|---|---|---|
| Unit test ViewModel/State | `app/src/test/java/...` | `./gradlew :app:testDebugUnitTest` | Không (JVM) |
| Compose UI test | `app/src/androidTest/java/...` | `./gradlew :app:connectedDebugAndroidTest` | Emulator/máy thật |

Ưu tiên **unit test ViewModel** — nhanh, phủ hết luật nghiệp vụ. UI test chỉ 1–3 case cho
tương tác dễ sai (bấm cả dòng checkbox, nút disabled).

## Dependency

```kotlin
testImplementation(libs.junit)                              // junit:junit 4.13.2
testImplementation(libs.kotlinx.coroutines.test)            // org.jetbrains.kotlinx:kotlinx-coroutines-test
androidTestImplementation(platform(libs.androidx.compose.bom))
androidTestImplementation(libs.androidx.test.ext.junit)
androidTestImplementation(libs.androidx.test.espresso.core) // ≥ 3.7.0 — thiếu/cũ → NoSuchMethodException InputManager.getInstance trên Android mới
androidTestImplementation(libs.androidx.compose.ui.test.junit4)
debugImplementation(libs.androidx.compose.ui.test.manifest)
```

## 1. MainDispatcherRule (bắt buộc khi ViewModel dùng `viewModelScope`)

```kotlin
@OptIn(ExperimentalCoroutinesApi::class)
class MainDispatcherRule(
    private val dispatcher: TestDispatcher = UnconfinedTestDispatcher(),
) : TestWatcher() {
    override fun starting(description: Description) = Dispatchers.setMain(dispatcher)
    override fun finished(description: Description) = Dispatchers.resetMain()
}
```

## 2. Unit test ViewModel — fake viết tay, không thư viện mock

```kotlin
class LoginViewModelTest {
    @get:Rule val mainDispatcherRule = MainDispatcherRule()

    private class TestAuthRepository(private val result: Boolean) : AuthRepository {
        override suspend fun login(email: String, password: String) = result
    }
    private class TestRememberMeStore(var email: String? = null) : RememberMeStore {
        override fun savedEmail() = email
        override fun save(email: String) { this.email = email }
        override fun clear() { email = null }
    }

    @Test
    fun login_success_withRememberMe_savesEmail() = runTest {
        val store = TestRememberMeStore()
        val viewModel = LoginViewModel(TestAuthRepository(true), store)

        viewModel.onEmailChange("a@b.com")
        viewModel.onPasswordChange("123456")
        viewModel.onRememberMeChange(true)
        viewModel.onLoginClick()

        assertTrue(viewModel.uiState.value.isLoggedIn)
        assertEquals("a@b.com", store.email)
    }
}
```

Chọn case từ **tiêu chí nghiệm thu** trong `TASK.md`: mỗi AC ≥ 1 test. Bộ tối thiểu cho 1 màn form:
trạng thái ban đầu · nút disabled khi thiếu input · thành công · thất bại (có lỗi, không lưu).
Tên: `hanhDong_dieuKien_ketQua`. Thân: arrange / act / assert cách 1 dòng trống.

## 3. Compose UI test — test `XxxContent` stateless

```kotlin
class LoginContentTest {
    // Compose BOM 2026.06: import androidx.compose.ui.test.junit4.v2.createComposeRule
    // (bản junit4.createComposeRule cũ báo deprecated)
    @get:Rule val composeRule = createComposeRule()

    @Test
    fun clickRememberMeRow_sendsCheckedTrue() {
        var checked: Boolean? = null
        composeRule.setContent {
            LoginContent(LoginUiState(), {}, {}, onRememberMeChange = { checked = it }, onLoginClick = {})
        }
        composeRule.onNodeWithText("Ghi nhớ đăng nhập").performClick()
        assertEquals(true, checked)
    }
}
```

## Lỗi hay gặp

| Lỗi | Sửa |
|---|---|
| `Module with the Main dispatcher is missing` | Thiếu `MainDispatcherRule` |
| Assert chạy trước khi coroutine xong | Dùng `UnconfinedTestDispatcher` trong rule, hoặc `advanceUntilIdle()` với `StandardTestDispatcher` |
| `delay(1000)` trong Fake làm test chậm | Test dùng Test fake trả ngay; `FakeXxx` có delay chỉ cho app demo |
| `onNodeWithText` báo nhiều node | `onNode(hasText("…") and hasClickAction())` |
| UI test fail ngay lần đầu / timeout install | Emulator chưa boot xong — `adb wait-for-device`, chạy lại (xem `kotlin-android-build-run`) |
| Muốn thêm MockK/Mockito | Không cần — interface + class fake 5 dòng là đủ |

Kết quả (lệnh + số test pass) ghi vào mục 6 của `TASK.md`.
