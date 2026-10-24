---
name: app-release
description: "Bước 9 của pipeline app — làm ra bản build store chấp nhận: đặt icon thật (flutter_launcher_icons, bỏ alpha), tăng version/build number cao hơn bản đã upload, ký Android bằng upload key của người dùng (key.properties ngoài git, Play App Signing), ký iOS bằng Team của người dùng trong Xcode, cấu hình production (config/prod.json với key RevenueCat public), build AAB + IPA, rồi check_release.py soi bundle id, targetSdk 36, chữ ký AAB, file bí mật không nằm trong git, icon không alpha. Use when someone wants a release build, 'build bản release', 'tạo file aab', 'tạo file ipa', 'ký app', 'keystore', 'upload key', 'tăng version', 'đổi icon app', 'Team ID điền ở đâu', 'build ipa lỗi signing', 'targetSdk play yêu cầu', or when scripts/app.py status says step 9 is next. Không tạo mật khẩu, không đăng nhập Apple, không upload thay người dùng."
argument-hint: "[slug]"
user-invocable: true
model: claude-sonnet-5-5
---

# Bước 9 — release

**Một việc:** `python3 scripts/check_release.py apps/ACTIVE/<slug>` in `0 FAIL`.

> **App Mac (`stack: macos`) đi đường khác:** checker là `python3 scripts/check_macos.py apps/ACTIVE/<slug>`, bản build là
> `.app`/`.dmg` ký bằng Developer ID + notarize (hoặc `3rd Party Mac Developer` nếu nộp Mac App Store), version nằm ở
> `mac/Resources/Info.plist` (`CFBundleVersion` — `release.py` tự tăng). Toàn bộ lệnh ký/notarize: skill `app-macos`,
> [references/distribution.md](../app-macos/references/distribution.md). Phần dưới đây là cho app điện thoại.

Đọc khi cần: [references/android-signing.md](references/android-signing.md) (Flutter + Play) ·
[references/apple-signing.md](references/apple-signing.md) (mua tài khoản, Team ID, chứng chỉ — viết gốc cho game, áp y nguyên cho app).

## 1. Icon thật

Icon 1024 từ `/app-design` ở `apps/ACTIVE/<slug>/source/store/icon-1024.png`.

```bash
cd apps/ACTIVE/<slug>/source/app
fvm flutter pub add dev:flutter_launcher_icons
```

Thêm vào cuối `pubspec.yaml`:

```yaml
flutter_launcher_icons:
  image_path: "../store/icon-1024.png"
  android: true
  ios: true
  remove_alpha_ios: true
  adaptive_icon_background: "#FFFFFF"      # màu nền từ design.md
  adaptive_icon_foreground: "../store/icon-1024.png"
```

```bash
fvm dart run flutter_launcher_icons
```

## 2. Version

`pubspec.yaml` → `version: 1.0.0+1`. Phần sau `+` là **build number**: mỗi lần upload phải lớn hơn mọi lần trước, kể cả bản
đã xoá. Checker so với `Last iOS build` / `Last Android versionCode` trong publish.md.

## 3. Cấu hình production

`app/config/prod.json` — như dev.json nhưng đủ giá trị thật: `RC_IOS_KEY` (`appl_...`), `RC_ANDROID_KEY` (`goog_...`),
`TERMS_URL`, `PRIVACY_URL`, `SUPPORT_EMAIL`. Chỉ key **public**. URL lấy từ site đã đăng (`scripts/make_site.py`).

## 4. Android — upload key (người dùng giữ)

Người dùng **tự chạy và tự gõ mật khẩu** (Claude không đặt, không đọc, không in mật khẩu). Script tạo `~/keys/<slug>-upload.jks`,
cất mật khẩu vào **Keychain** (mục `android-upload-<slug>`, quên thì `--show`), ghi file properties ngoài git
(native: `android/keystore.properties` · Flutter: `app/android/key.properties`); khoá cũ đổi tên `.old-<ngày>.jks`, không xoá:

```bash
python3 scripts/android_upload_key.py <slug>
```

Google giữ app signing key (Play App Signing) → mất upload key chỉ cần xin reset trong Play Console.

Tạo `app/android/key.properties` (đã nằm trong .gitignore do scaffold) — người dùng điền mật khẩu:

```properties
storePassword=
keyPassword=
keyAlias=upload
storeFile=~/keys/<slug>-upload.jks
```

Claude sửa `app/android/app/build.gradle.kts` theo mẫu trong `android-signing.md` (đọc key.properties, `release` dùng
`signingConfigs.release`). Backup `.jks` + mật khẩu vào password manager. Trên Play Console bật **Play App Signing**.

```bash
fvm flutter build appbundle --release --dart-define-from-file=config/prod.json
```

## 5. iOS — Team của người dùng

1. Người dùng mở `apps/ACTIVE/<slug>/source/app/ios/Runner.xcworkspace` trong Xcode → Settings ▸ Accounts thêm Apple ID dev.
2. Target **Runner** ▸ Signing & Capabilities ▸ tick *Automatically manage signing* ▸ **Team** = team của họ ▸ Bundle
   Identifier đúng app.json. Thêm capability **In-App Purchase**.
3. Build:

```bash
fvm flutter build ipa --release --dart-define-from-file=config/prod.json
```

IPA ở `app/build/ios/ipa/`. Upload: người dùng mở `build/ios/archive/Runner.xcarchive` bằng Xcode Organizer →
Distribute App → App Store Connect → Upload (lần đầu nên đi đường này — Xcode chỉ ra mọi lỗi ký có nút sửa).

## 6. Kiểm

```bash
python3 scripts/check_release.py apps/ACTIVE/<slug>
```

| FAIL | Vì sao |
|---|---|
| bundle id / applicationId lệch app.json | lên store rồi không đổi được |
| build number ≤ bản đã upload | store từ chối |
| targetSdk < 36 | Play từ chối app mới + update từ 2026-08-31 |
| release Android ký debug key / AAB chưa ký | Play từ chối |
| `key.properties`, `.jks`, `.p8`, `.p12` trong git | lộ khoá — `git rm --cached` và tạo khoá mới |
| icon iOS có alpha / còn icon mặc định | ITMS-90717 / bị từ chối vì icon placeholder |
| có `sk_...` trong code | lộ secret key RevenueCat |
| app bán subscription mà code không có restore | Apple từ chối |

## Build = MỘT lệnh — tự tăng build + đóng gói (bắt buộc)

```bash
python3 scripts/release.py <slug>            # build +1 → build + ký → đóng gói
python3 scripts/release.py <slug> --patch    # bản sửa lỗi: 1.0.3 → 1.0.4 (build +1)
python3 scripts/release.py <slug> --minor    # bản tính năng: 1.0.3 → 1.1.0 (build +1)
```

**Không** gọi `make mas` / `flutter build` / sửa tay `CFBundleVersion` rồi thôi — lần nào cũng đi qua `release.py`, vì nó:
1. **Tăng build** trong `mac/Resources/Info.plist` hoặc `app/pubspec.yaml` (store chỉ nhận build lớn hơn mọi bản đã upload;
   số nhảy cóc không sao). Build hỏng, chưa upload → sửa rồi `--no-bump` để dùng lại số đó.
2. **Build + ký** theo `stack`/`distribution` trong app.json (Mac App Store: `make mas`, profile lấy từ app.json `mas_profile`
   hoặc mặc định trong Makefile · Mac bán ngoài: `make notarize` · Flutter: `ipa` + `appbundle` với `config/prod.json`).
   Stack native chưa tự build: build tay rồi `--no-bump --pack-only`.
3. **Đóng gói** (`pack_version.py`) vào kho chung cạnh repo: `publish/first-release/` (store đó chưa có app) hoặc `publish/release/v<version>/` — chọn theo từng store, .ipa/.aab có thể vào hai chỗ, chép y hệt sang `App-Ready-Publish/<Tên-store>/<cùng chỗ>/` (luật: `reference/README-APP-PUBLISH-03-RELEASE-FOLDERS.md`) —
   `package/<TenStore>-<version>-build<N>.pkg|dmg|ipa|aab`, `screenshots/` (đúng bộ ảnh listing đang nhắc tới), `icon-1024.png`,
   `whats-new.md` (mục `## What's New — <version>` trong publish.md), `listing.md`, `upload.sh`, `SHA256SUMS`, `README.md`,
   và ghi lại `App-Ready-Publish/README.md` (mọi bản + cột trạng thái, `App-Ready-Publish/ready.py`). Mỗi build một thư mục, bản cũ giữ lại.
   Người dùng upload xong → `python3 ready.py mark <Tên> <ios|android|mac|dmg> uploaded` trong App-Ready-Publish.
   `.pkg` lệch version Info.plist → dừng, bắt build lại.

Người dùng chỉ mở **một thư mục** đó, chạy `./upload.sh`, tự bấm Deliver / Upload. Báo lại cho người dùng đường dẫn thư mục,
version + build, và log một dòng vào publish.md trỏ tới thư mục đó (không trỏ vào `build/`).

LEARNED.md mục **Bước 9** (nhấn mạnh: key nằm ở đâu, vì sao không được mất) · `scripts/app.py log` · tiếp theo `/app-listing`.
