---
name: app-setup
description: "Bước 0 của pipeline app — kiểm tra máy Mac có đủ công cụ làm app chưa (Flutter qua fvm, Xcode + iOS Simulator, CocoaPods, Android SDK + emulator, JDK, Python + Pillow, plugin Claude chính chủ dart-flutter và revenuecat), cài phần thiếu sau khi hỏi, và lập checklist tài khoản phải mở sớm vì có thời gian chờ (Apple Developer 99 USD/năm, Google Play 25 USD + closed test 14 ngày, RevenueCat, Paid Apps Agreement + thuế W-8BEN + ngân hàng, trang Privacy/Terms). Ghi apps/ACTIVE/<slug>/context-ai/setup.md. Use when someone starts the app pipeline, 'cài môi trường làm app', 'máy cần cài gì', 'cài flutter', 'flutter doctor lỗi', 'chưa có tài khoản apple developer', 'mở tài khoản google play', 'tài khoản developer bao nhiêu tiền', 'W-8BEN', 'thuế apple', 'cài plugin revenuecat', or when scripts/app.py status says step 0 is next. Không tạo tài khoản, không trả phí, không nhập thông tin thuế/ngân hàng thay người dùng."
argument-hint: "[slug] — bỏ trống nếu chưa có app (chỉ kiểm máy)"
user-invocable: true
model: claude-sonnet-5-5
---

# Bước 0 — setup

**Một việc:** máy làm được mọi bước build, và người dùng biết tài khoản nào phải mở ngay hôm nay.

## 1. Kiểm máy (chỉ đọc)

```bash
bash scripts/preflight.sh flutter     # hoặc: native · bỏ trống = cả hai
```

Đọc từng dòng `[MISS]` / `[WARN]` và giải thích cho người dùng **bằng lời thường** — ví dụ
"CocoaPods là công cụ tải thư viện cho bản iPhone; thiếu nó thì bước chạy app trên iPhone sẽ lỗi".

## 2. Cài phần thiếu — hỏi trước, nói rõ dung lượng

| Thiếu | Lệnh | Ghi chú |
|---|---|---|
| fvm + Flutter 3.47.4 | `bash scripts/setup_flutter.sh` | ~215 MB SDK + artifact iOS/Android. Không cần sudo |
| CocoaPods | `brew install cocoapods` | |
| Pillow | `pip3 install pillow` | đo ảnh store |
| Xcode | người dùng tự cài từ App Store (~15 GB), mở một lần | |
| `xcode-select` trỏ sai | `sudo xcode-select -s /Applications/Xcode.app` | **cần mật khẩu người dùng → họ tự gõ** |
| Android SDK / AVD / platform 36 | người dùng mở Android Studio → SDK Manager / Device Manager | Claude chỉ đường từng nút |
| `flutter doctor --android-licenses` | người dùng tự chạy và gõ `y` | là chấp nhận điều khoản → việc của người dùng |

Chạy lại `preflight.sh` tới khi dòng cuối là `Machine: ready`.

## 3. Plugin Claude chính chủ (nên có — hỏi trước khi cài)

```bash
claude plugin marketplace add flutter/agent-plugins && claude plugin install dart-flutter@dart-flutter
claude plugin marketplace add RevenueCat/ai-toolkit && claude plugin install revenuecat
```

- **dart-flutter** (Flutter team): skill layout, widget test, integration test, sửa lỗi layout + MCP Dart/Flutter.
- **revenuecat** (RevenueCat): skill tạo project, gắn SDK, paywall, test, xử lý lỗi + MCP đọc số liệu (đăng nhập OAuth — người dùng tự bấm).

Đây là thay đổi cấu hình Claude của người dùng → hỏi bằng `AskUserQuestion`, không tự chạy.

## 4. Tài khoản — lập checklist, không làm thay

Đọc [references/accounts.md](references/accounts.md) rồi giải thích **thứ tự và thời gian chờ**. Điểm phải nói rõ:

1. **Apple Developer Program** — 99 USD/năm, loại *Individual*, duyệt ~24h. Tên người bán hiện trên store là tên thật.
2. **Bán subscription trên Apple cần thêm Paid Apps Agreement → thuế (W-8BEN) → ngân hàng.** Thuế có thể xử lý tới
   90 ngày → **bắt đầu cùng ngày mua tài khoản**, không đợi app xong.
3. **Google Play Console** — 25 USD một lần. Tài khoản **cá nhân** mới phải chạy *closed test* ≥ 12 người tham gia
   liên tục 14 ngày trước khi được lên production → rủ 15–20 người thật từ bây giờ.
4. **RevenueCat** — miễn phí tới 2.500 USD doanh thu theo dõi/tháng.
5. **Trang Privacy / Terms / Support** — bắt buộc cho cả hai store; `scripts/make_site.py` dựng sẵn, đăng bằng GitHub Pages.
6. **Không mua/thuê tài khoản developer của người khác** — Apple/Google khoá cả tài khoản lẫn app.

**Mua lúc nào?** Đừng hối người dùng rút ví ở bước 0 nếu chưa cần:

| Loại app | Làm + test trên máy mình | Lúc bắt buộc phải có tài khoản |
|---|---|---|
| iOS / Android (Flutter, native) | miễn phí trên simulator/emulator | khi muốn cài lên máy thật của người khác, hoặc lên store |
| **macOS (`stack: macos`)** | **miễn phí, đầy đủ** — `make run` ký chữ ký tạm, chạy trên chính máy đã build | khi đưa .dmg cho người khác tải (ký Developer ID + notarize), hoặc nộp Mac App Store |

Nhưng mục 2 vẫn đúng: **bán subscription thì thuế có thể chờ tới 90 ngày**, nên ai chắc chắn sẽ bán thì mua sớm vẫn hơn.

## 5. Ghi kết quả

Có app rồi (`apps/ACTIVE/<slug>/`): điền `setup.md` — dán nguyên văn kết quả preflight, tick mục máy, sửa
`Machine: pending` → `Machine: ready` khi preflight nói vậy. Tick tài khoản nào người dùng **xác nhận** đã có.
Chưa có app: giữ kết quả trong câu trả lời, `/app-research` là bước tiếp theo.

Sau đó: mục **Bước 0** trong `LEARNED.md` + `python3 scripts/app.py log <slug> --skill app-setup "..." --next "/app-research"`.

## Lỗi hay gặp

| Triệu chứng | Nguyên nhân → sửa |
|---|---|
| `flutter: command not found` | pipeline gọi `fvm flutter`, không cần Flutter global |
| `CocoaPods not installed` khi build iOS | `brew install cocoapods` |
| `Unable to locate Android SDK` | `fvm flutter config --android-sdk ~/Library/Android/sdk` |
| `cmdline-tools component is missing` | Android Studio > SDK Manager > SDK Tools > Command-line Tools |
| Simulator không có iPhone 17 Pro Max | Xcode > Settings > Components > tải iOS runtime |
