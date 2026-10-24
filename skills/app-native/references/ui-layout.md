> Nguồn: skill cá nhân `native-ui-layout` (repo mobile-app-learning, 2026-09-15), chép vào đây làm tài liệu tham khảo cho nhánh Native.
> Chỗ nhắc `native-feature-task` / `TASK.md` / `GO-THEO.md` / `demo/...` là quy ước của repo học — trong pipeline app
> thay bằng `/app-build` (MVP) hoặc file việc trong `apps/ACTIVE/<slug>/plan/` (`/app-feature`, `/app-fix`).

# native-ui-layout — dựng layout Compose / SwiftUI

UI **chỉ vẽ state và gửi event**. Luật nghiệp vụ nằm ở ViewModel (`kotlin-android-code` /
`swift-ios-code`). Không XML layout, không Storyboard.

## Quy trình dựng 1 màn

1. **Vẽ khung ASCII** từ requirement/ảnh: chia thành hàng dọc các khối → mỗi khối ngang.
2. **Map khối → container** (bảng dưới). Ngoài cùng thường là 1 cột dọc có padding.
3. **Tách stateless:** Compose `XxxContent(state, onA…)`; SwiftUI View nhận binding/closure.
   Khối lặp lại hoặc > ~30 dòng → component riêng (`RememberMeRow`, `CheckboxToggleStyle`).
4. **Preview** với state mẫu (rỗng, đang loading, có lỗi) trước khi chạy máy.
5. Chạy thật + screenshot (build-run skill) cả dọc lẫn ngang nếu màn có form.

## Bảng quy đổi

| Việc | Jetpack Compose | SwiftUI |
|---|---|---|
| Cột / hàng / chồng lớp | `Column` / `Row` / `Box` | `VStack` / `HStack` / `ZStack` |
| Khoảng cách đều | `verticalArrangement = Arrangement.spacedBy(12.dp)` | `VStack(spacing: 12)` |
| Căn trái các con | `horizontalAlignment = Alignment.Start` | `VStack(alignment: .leading)` |
| Đẩy xuống / giãn | `Spacer(Modifier.weight(1f))` | `Spacer()` |
| Full width | `Modifier.fillMaxWidth()` | `.frame(maxWidth: .infinity)` |
| Padding | `Modifier.padding(24.dp)` | `.padding(24)` |
| Căn giữa màn | `Column(Modifier.fillMaxSize(), verticalArrangement = Arrangement.Center)` | `VStack { … }` (mặc định giữa) |
| Cuộn được | `Modifier.verticalScroll(rememberScrollState())` | `ScrollView { … }` |
| Danh sách | `LazyColumn { items(list, key = { it.id }) { … } }` | `List(list) { … }` (item `Identifiable`) |
| Ô nhập | `OutlinedTextField(value, onValueChange, label = { Text("Email") })` | `TextField("Email", text: $vm.email)` |
| Mật khẩu | `visualTransformation = PasswordVisualTransformation()` | `SecureField` |
| Checkbox | `Row(Modifier.toggleable(value, role = Role.Checkbox, onValueChange)) { Checkbox(checked, null); Text(…) }` | `Toggle(isOn:)` + `ToggleStyle` tự viết (iOS không có `.checkbox`) |
| Nút + loading | `Button(enabled = state.canSubmit) { if (loading) CircularProgressIndicator(Modifier.size(20.dp)) else Text(…) }` | `Button { } label: { if loading { ProgressView() } else { Text(…) } }.disabled(!vm.canSubmit)` |
| Lỗi đỏ | `Text(msg, color = MaterialTheme.colorScheme.error)` | `Text(msg).foregroundStyle(.red)` |
| Preview | `@Preview @Composable private fun XPreview()` | `#Preview { … }` |

Thứ tự `Modifier` trong Compose **có ý nghĩa**: `.padding().background()` ≠ `.background().padding()`.
Modifier SwiftUI cũng vậy: `.padding().background(.gray)` tô cả phần padding.

## Checkbox bấm cả dòng (hay bị làm sai)

```kotlin
Row(
    verticalAlignment = Alignment.CenterVertically,
    modifier = Modifier.fillMaxWidth()
        .toggleable(value = checked, onValueChange = onCheckedChange, role = Role.Checkbox)
        .padding(vertical = 8.dp),
) {
    Checkbox(checked = checked, onCheckedChange = null) // null: Row đã xử lý click
    Spacer(Modifier.width(8.dp))
    Text("Ghi nhớ đăng nhập")
}
```

```swift
struct CheckboxToggleStyle: ToggleStyle {
    func makeBody(configuration: Configuration) -> some View {
        Button { configuration.isOn.toggle() } label: {
            HStack(spacing: 8) {
                Image(systemName: configuration.isOn ? "checkmark.square.fill" : "square")
                configuration.label
            }
        }
        .buttonStyle(.plain)
    }
}
// Toggle("Ghi nhớ đăng nhập", isOn: $viewModel.rememberMe).toggleStyle(CheckboxToggleStyle())
```

## Lỗi hay gặp

| Triệu chứng | Sửa |
|---|---|
| Xoay ngang mất nút dưới cùng | Bọc cột trong `verticalScroll` / `ScrollView` |
| Bàn phím che ô nhập (Compose) | `Modifier.imePadding()` trên container cuộn |
| Checkbox chỉ bấm được ô vuông | `toggleable` trên `Row`, `Checkbox(onCheckedChange = null)` |
| 2 node cùng text làm UI test mơ hồ | Lọc thêm `hasClickAction()` hoặc đặt `Modifier.testTag` |
| TextField iOS tự viết hoa email | `.textInputAutocapitalization(.never).autocorrectionDisabled()` |
| Composable nhận `viewModel` ở component con | Chỉ truyền giá trị + lambda |
| Màu/typography tự đặt số cứng khắp nơi | `MaterialTheme.colorScheme/typography` · SwiftUI `.font(.title)`, `.foregroundStyle(.secondary)` |

Tham khảo: `android/compose-samples`, `android/snippets`, `apple/sample-food-truck`.
Animation → `swift-ios-animation`. Màu/asset từ app Ionic → `swift-ios-port-ionic`.
