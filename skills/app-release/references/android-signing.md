# Ký app Android (Flutter) cho Google Play

Nguồn: docs.flutter.dev/deployment/android · developer.android.com/studio/publish/app-signing ·
support.google.com/googleplay/android-developer/answer/9842756 (Play App Signing). Đọc **2026-09-15**.

## Hai loại khoá

| Khoá | Ai giữ | Mất thì sao |
|---|---|---|
| **App signing key** | Google (Play App Signing — bắt buộc cho app mới dùng AAB) | không mất được |
| **Upload key** (`<slug>-upload.jks`) | **người dùng** | xin Google reset trong Play Console (vài ngày) — app không mất |

Vì Play App Signing giữ khoá chính, upload key chỉ chứng minh "bản upload này đến từ đúng người". Vẫn phải backup.

## `android/app/build.gradle.kts` — mẫu đọc key.properties

Thêm ở đầu file (sau khối `plugins { }`):

```kotlin
import java.util.Properties
import java.io.FileInputStream

val keystoreProperties = Properties()
val keystorePropertiesFile = rootProject.file("key.properties")
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(FileInputStream(keystorePropertiesFile))
}
```

Trong `android { }`, trước `buildTypes`:

```kotlin
signingConfigs {
    create("release") {
        keyAlias = keystoreProperties["keyAlias"] as String?
        keyPassword = keystoreProperties["keyPassword"] as String?
        storeFile = keystoreProperties["storeFile"]?.let { file(it) }
        storePassword = keystoreProperties["storePassword"] as String?
    }
}
```

Trong `buildTypes { release { ... } }` thay dòng `signingConfig = signingConfigs.getByName("debug")` bằng:

```kotlin
signingConfig = signingConfigs.getByName("release")
```

`rootProject.file("key.properties")` → file nằm ở `app/android/key.properties`.

## Kiểm AAB đã ký đúng khoá

```bash
keytool -printcert -jarfile app/build/app/outputs/bundle/release/app-release.aab | head -8
```

Chủ sở hữu (Owner) phải là thông tin người dùng nhập lúc tạo key, không phải `CN=Android Debug`.

## targetSdk

Flutter đặt `targetSdk = flutter.targetSdkVersion`. Flutter 3.47.4 mặc định **36** (đọc
`packages/flutter_tools/gradle/src/main/kotlin/FlutterExtension.kt`) — đạt yêu cầu Play từ 2026-08-31.
`check_release.py` tự đọc giá trị này từ SDK đã ghim.

## Lỗi hay gặp

| Lỗi | Sửa |
|---|---|
| `Keystore file not set for signing config release` | thiếu/sai đường dẫn `storeFile` trong key.properties |
| `Upload failed: signed with wrong key` | đang ký khoá khác khoá đã đăng ký → dùng đúng .jks, hoặc xin reset upload key |
| `Version code 1 has already been used` | tăng số sau `+` trong pubspec.yaml |
| Bản release crash, debug thì không | R8 xoá lớp dùng reflection → đọc `adb logcat -b crash`, thêm keep rule vào `android/app/proguard-rules.pro` |
