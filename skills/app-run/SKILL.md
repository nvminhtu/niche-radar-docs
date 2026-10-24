---
name: app-run
description: "Bước 7 của pipeline app — Claude tự build, cài và mở app trên iOS Simulator và Android emulator, chụp màn hình rồi TỰ NHÌN ảnh trước khi nói gì, bấm thử luồng chính (mở paywall, mua bằng bản Fake, khôi phục), kiểm chế độ tối, cỡ chữ lớn, tắt mở lại vẫn giữ dữ liệu, đọc log khi crash. Ghi run/out/screenshot-ios.png và run/out/screenshot-android.png; app Mac (stack macos) thì build .app, mở rồi chụp ĐÚNG cửa sổ app → run/out/screenshot-macos.png. Use when someone wants to see or try the app, 'chạy app', 'mở app lên simulator', 'chạy trên android', 'xem app trông thế nào', 'app bị crash', 'màn hình trắng', 'screenshot app', 'test trên iphone', 'chạy app mac', 'chụp cửa sổ app mac', 'dark mode có đẹp không', or when scripts/app.py status says step 7 is next. Ảnh cho store làm ở /app-listing."
argument-hint: "[slug] [ios|android|all]"
user-invocable: true
model: claude-sonnet-5-5
---

# Bước 7 — run

**Một việc:** mỗi nền tảng có `run/out/screenshot-<nền tảng>.png` **và Claude đã Read ảnh đó**, cộng bằng chứng luồng chính chạy.

```bash
python3 scripts/run_app.py run <slug>                       # cả iOS + Android theo app.json
python3 scripts/run_app.py run <slug> --platform ios --device "iPhone 17 Pro Max"
python3 scripts/run_app.py logs <slug> --platform android   # khi app chết
```

Flutter: build bằng `fvm flutter build` rồi cài qua `simctl` / `adb` — không dùng `flutter run` (giữ terminal).
`config/dev.json` tự được truyền nếu có. Native: gọi `scripts/native/run_ios.sh` / `run_android.sh`.
macOS: `--platform macos` gọi `scripts/native/run_macos.sh` — `make app`, `open`, rồi `screencapture` đúng vùng cửa sổ app
(lần đầu máy hỏi quyền Accessibility cho Terminal; chưa cấp thì ảnh là cả màn hình, phải cấp rồi chụp lại).
Trên app Mac còn phải thử: kéo–thả file vào cửa sổ, phím tắt, nhiều cửa sổ, cửa sổ Settings, và thao tác nguy hiểm có hoàn tác.

Người dùng muốn **xem trực tiếp** simulator: dùng công cụ iOS Simulator của phiên (`attach`) trước khi build.

## Bấm thử — theo chữ, không theo toạ độ

| Nền tảng | Cách |
|---|---|
| Android | `python3 scripts/native/android_ui.py dump` · `tap "Upgrade to Pro"` · `text "Pro is active. Thank you!"` (exit 0/1). Flutter đưa nhãn vào cây accessibility; `dump` rỗng → thêm `Semantics(label:)`/`tooltip` cho widget đó (cũng là lỗi accessibility thật) |
| iOS | công cụ iOS Simulator của phiên: `inspect` (cây accessibility) → `tap` tâm của frame. Không có công cụ → chỉ screenshot, nói rõ đã không bấm thử |

## Chứng minh, không mô tả

| Cần chứng minh | Cách |
|---|---|
| Luồng mua (bản Fake, chưa có key) | Upgrade → Continue → màn Home hiện "Pro is active" |
| Restore | Settings → Restore purchases → thông báo đúng |
| Dữ liệu còn sau khi tắt app | Android `adb shell am force-stop <id>` · iOS `xcrun simctl terminate booted <id>` → mở lại → vẫn còn |
| Chế độ tối | iOS `xcrun simctl ui booted appearance dark` · Android `adb shell cmd uimode night yes` → chạy lại → screenshot |
| Cỡ chữ lớn | iOS `xcrun simctl ui booted content_size accessibility-extra-extra-extra-large` · Android `adb shell settings put system font_scale 2.0` → không chữ nào bị cắt |
| Màn ngang / màn nhỏ | `--device "iPhone SE (3rd generation)"` — layout phải cuộn được |

Trả lại cài đặt sau khi kiểm (`appearance light`, `content_size large`, `font_scale 1.0`, `night no`).

## Máy thật — bắt buộc trước CỔNG 4 cho những thứ simulator không chứng minh được

Simulator/emulator đủ cho giao diện và luồng Fake. **Máy thật** mới chứng minh được: mua subscription sandbox thật,
thông báo, camera, hiệu năng/độ mượt, cảm giác chạm. `status` bước 7 chỉ đòi ảnh simulator; ảnh máy thật là bằng chứng
cho `review.md`.

```bash
python3 scripts/run_app.py devices <slug>                          # liệt kê máy thật đang cắm
python3 scripts/run_app.py device <slug> --platform android        # build release → cài → mở → run/out/device-android.png
python3 scripts/run_app.py device <slug> --platform ios            # build release (cần Team ký) → devicectl cài + mở → chụp
python3 scripts/run_app.py device <slug> --platform ios --prod     # dùng config/prod.json (key RevenueCat thật)
```

| Nền tảng | Người dùng chuẩn bị một lần | Claude làm được | Giới hạn |
|---|---|---|---|
| Android | Developer options ▸ USB debugging ▸ cắm cáp ▸ cho phép máy tính | cài, mở, **chụp màn hình**, bấm theo chữ (`android_ui.py` với `ANDROID_SERIAL=<id>`), đọc crash log | mua thật cần cài từ link internal testing của Play (`/app-publish`) |
| iPhone | cắm cáp ▸ Tin cậy ▸ **Developer Mode** bật ▸ trong Xcode chọn Team của mình cho Runner (Personal Team miễn phí chạy 7 ngày) | build release, cài + mở bằng `xcrun devicectl` | chụp màn hình từ Mac **thường bị iOS mới chặn** → script báo rõ, người dùng chụp trên máy (nguồn + tăng âm lượng) rồi AirDrop về `run/out/device-ios.png` cho Claude Read. Mua sandbox chắc nhất qua TestFlight |

Lần đầu mở app trên iPhone: Settings ▸ General ▸ VPN & Device Management ▸ tin cậy developer.
Không có máy thật → ghi `chưa kiểm trên máy thật` trong review.md, **không** ghi ok.

## Nhìn ảnh thế nào

Build xanh **không** có nghĩa UI đúng. Mỗi ảnh tự hỏi: chữ bị cắt/tràn? màu đúng design.md? khoảng trắng lạ? trạng thái
rỗng có hướng dẫn? nút chính nổi bật? tai thỏ/thanh home che nội dung? Sai → sửa → chạy lại → chụp lại.
Gửi ảnh cho người dùng kèm 1–2 câu nhận xét.

## Lỗi hay gặp

| Triệu chứng | Nguyên nhân → sửa |
|---|---|
| `BUILD FAILED` iOS, lỗi Pods | `cd app/ios && pod repo update && pod install`; thiếu CocoaPods → `brew install cocoapods` |
| `Unable to boot simulator` | `xcrun simctl shutdown all` rồi chạy lại |
| Screenshot trắng/đen | chụp khi app chưa vẽ xong → `--wait 10` |
| `INSTALL_FAILED_UPDATE_INCOMPATIBLE` | khác chữ ký với bản cũ → `adb uninstall <bundle_id>` |
| Gradle: `Unsupported class file major version` | Gradle chạy JDK sai → `fvm flutter config --jdk-dir <JDK 17/21>` |
| App mở rồi tắt ngay | `run_app.py logs` → đọc dòng `Caused by:` / `Exception` cuối cùng → `/app-fix` |
| Ảnh chỉ có màn splash Flutter | emulator vẽ trễ sau khi cây giao diện đã sẵn — `run_app.py` chụp lặp tới khi 2 ảnh giống nhau; vẫn gặp → `--wait 10` |
| Ảnh là màn hình chính Android, "app KHÔNG chạy", log crash chỉ có dịch vụ hệ thống, launcher "isn't responding" | **emulator nghẽn RAM**, không phải lỗi app: `adb shell top -b -n 1` thấy RAM trống vài trăm MB + iowait cao → `adb emu kill`, chạy lại với AVD nhẹ hơn (`--device Pixel_6_Pro_API_34`) hoặc tăng RAM AVD trong Device Manager. Đo 2026-09-16: Pixel_9_Pro API 36 (3 GB) nghẽn sau ~1 giờ chạy liên tục |
| Bản thật (có key) paywall trống | sản phẩm chưa sẵn trên store / chưa nối RevenueCat → `app-paywall` §Kiểm tra |

LEARNED.md mục **Bước 7** · `scripts/app.py log` · tiếp theo `/app-review`.
