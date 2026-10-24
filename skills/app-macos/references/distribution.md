# Phát hành app Mac — hai đường, chọn một

Quyết định ở bước 2 (`/app-money`), ghi vào `app.json` → `"distribution": "direct" | "mas"`.

| | `direct` — .dmg trên web của bạn | `mas` — Mac App Store |
|---|---|---|
| Doanh thu | bạn thu 100% (trừ phí cổng thanh toán 3–5%) | Apple cắt 15% (dưới 1 triệu USD/năm) hoặc 30% |
| Ai duyệt | không ai — ra bản lúc nào cũng được | Apple review, vài ngày, có thể bị từ chối |
| Sandbox | không bắt buộc (vẫn nên bật) | **bắt buộc** |
| Bán subscription | Paddle / Lemon Squeezy / Stripe + license key | StoreKit 2, bắt buộc, không được dẫn ra ngoài mua |
| Trial | app tự đếm (Keychain) + license key — [trial-license.md](trial-license.md) | introductory offer / IAP giá 0 — [trial-license.md](trial-license.md) |
| Cập nhật | tự lo: Sparkle + appcast.xml | App Store đẩy |
| Người dùng tin không | phải ký + notarize, không thì Gatekeeper chặn | có sẵn lòng tin của App Store |
| Bắt buộc | tài khoản Apple Developer (99 USD/năm) để ký | cũng tài khoản đó + Paid Apps Agreement |

**Không có tài khoản Apple Developer thì không PHÁT HÀNH được kiểu nào** — bản chưa ký hiện cảnh báo
"Apple could not verify…", người dùng bình thường sẽ bỏ đi. Nhưng **làm và test thì không cần gì cả** — xem ngay mục dưới.

## Test miễn phí — CHƯA cần tài khoản Apple Developer

Trên máy Mac của chính bạn, chạy và thử toàn bộ app không tốn đồng nào, không cần tài khoản gì:

```bash
cd apps/ACTIVE/<slug>/source/mac
make check     # lint + chạy test
make run       # dựng .app rồi mở lên — bấm thử thật
```

Vì sao chạy được: `make app` ký bằng **chữ ký tạm** (`codesign --sign -`, gọi là ad-hoc). macOS chấp nhận app ký tạm
**trên chính máy đã tạo ra nó**. Thứ duy nhất cần là Xcode (tải miễn phí từ Mac App Store).

| Việc | Cần tài khoản Apple Developer (99 USD/năm)? |
|---|---|
| `make check`, `make run`, `make app` trên máy mình | **không** |
| Bấm thử mọi tính năng, xem chế độ tối, chụp ảnh màn hình | **không** |
| `make dmg` (đóng gói file) | không — nhưng file đó máy người khác sẽ bị chặn |
| `make sign` · `make notarize` · đưa cho người khác tải | **có** |
| Nộp Mac App Store | **có** |

Hai điều phải biết khi test bằng chữ ký tạm:

1. **Gửi file cho người khác thì họ mở không được.** Gatekeeper chặn app chưa notarize: người nhận phải bấm chuột phải ▸
   Open ▸ Open, hoặc chạy `xattr -d com.apple.quarantine <app>`. Đừng bắt người dùng thật làm việc đó — đó là lúc
   cần mua tài khoản. Nhờ bạn bè test sớm thì được, họ chịu khó một lần.
2. **Chữ ký tạm đổi sau mỗi lần build.** App sandbox gắn quyền vào chữ ký, nên thư mục bạn đã cho phép ở bản build
   trước có thể phải **chọn lại** sau khi build lại. Đó là chuyện của bản test, không phải lỗi — bản đã ký Developer ID
   thì chữ ký ổn định, người dùng thật chỉ chọn thư mục một lần.

Khi nào nên mua tài khoản: lúc muốn người **ngoài** dùng thử. Trước đó, làm và test miễn phí được hết.

## Đường `direct` — từng lệnh

```bash
cd apps/ACTIVE/<slug>/source/mac
make app                                  # build/<Label>.app

# 1) Ký bằng Developer ID + hardened runtime (thiếu runtime là notarize trượt)
TEAM_ID=XXXXXXXXXX make sign

# 2) Công chứng — máy Apple quét mã độc rồi cấp dấu
xcrun notarytool store-credentials notary --apple-id <email> --team-id XXXXXXXXXX   # NGƯỜI DÙNG gõ, có mật khẩu
KEYCHAIN_PROFILE=notary make notarize     # submit --wait + stapler staple + spctl

# 3) Kiểm trước khi đăng
python3 scripts/check_macos.py apps/ACTIVE/<slug>
```

`xcrun notarytool store-credentials` hỏi **app-specific password** của Apple ID — Claude không gõ, không đọc, không lưu.
Người dùng tự chạy một lần trên máy họ.

Kiểm bản đã staple (giả lập máy người lạ):
```bash
spctl --assess --type open --context context:primary-signature -vv <Label>.dmg    # phải in "accepted"
xcrun stapler validate <Label>.dmg
```

### Cập nhật — Sparkle

- Thêm `https://github.com/sparkle-project/Sparkle` vào `Package.swift` (SwiftPM), `SUFeedURL` + `SUPublicEDKey` vào `Info.plist`.
- `appcast.xml` đặt cùng website (`scripts/make_site.py` dựng site) — **bắt buộc https**, `check_macos.py` FAIL nếu không.
- Ký từng bản cập nhật bằng `generate_appcast` của Sparkle (khoá EdDSA của bạn, giữ ngoài git).
- Mac App Store **cấm** Sparkle — chọn `mas` thì gỡ hẳn.

### Cho người ta cài dễ hơn — Homebrew cask

Sau khi có .dmg notarized và một trang tải ổn định, làm tap riêng (`github.com/<bạn>/homebrew-tap`), mỗi bản mới sửa
`version` + `sha256`. Người dùng cài bằng `brew install --cask <bạn>/tap/<app>`. Dev/power-user thích đường này;
nó không thay thế trang bán, chỉ là kênh phụ.

## Đường `mas` — khác gì

```bash
cd apps/ACTIVE/<slug>/source/mac
make xcodeproj     # XcodeGen sinh .xcodeproj từ project.yml — SwiftPM không nộp App Store được
```

Rồi trong Xcode: chọn Team của **bạn** → Product ▸ Archive → Distribute App ▸ App Store Connect.
Claude không bấm Archive, không đăng nhập, không Submit.

Khác biệt phải nhớ:
- Sandbox bắt buộc; mọi thư mục ngoài container phải qua `NSOpenPanel` + bookmark.
- Ký bằng `3rd Party Mac Developer Application`, không phải Developer ID (`check_macos.py` bắt nhầm cái này).
- Không Sparkle, không tự tải thêm code.
- Subscription phải là StoreKit; dẫn người dùng ra web mua = bị từ chối (3.1.1) **trừ storefront Mỹ** (link-out được phép, hiện 0%)
  và EU (điều khoản EU từ 2026-10-01, link-out 15% / 10% SBP). Kiểm lại `app-money/references/subscription-playbook.md` §3.
- `LSApplicationCategoryType` phải khớp danh mục chọn trên App Store Connect.

## Việc của người dùng, Claude không làm thay

Mua tài khoản Apple Developer · tạo/renew chứng chỉ · `store-credentials` (mật khẩu) · ký Paid Apps Agreement ·
nhập thuế/ngân hàng · bấm Archive / Submit / Release · đăng bản .dmg lên web của họ.

Claude làm: viết code, dựng Makefile, chạy `make app`, chạy checker, soạn nội dung trang tải, ghi log vào `publish.md`.
