---
name: app-review
description: "Bước 8 của pipeline app và CỔNG 4 — soát toàn bộ app trước khi ký bản build: chạy máy trước (test, flutter analyze, chạy app cả hai nền tảng, check_release --pre) và dán kết quả thật, rồi đọc code theo checklist cố định: kiến trúc, paywall đủ thành phần store bắt buộc, quyền Pro đọc từ entitlement, không nút/chữ quyên góp (3.2.2(iv)), privacy khớp SDK, quyền (permission) khớp spec, xoá tài khoản nếu có đăng nhập, accessibility, bảo mật (không secret key), metadata không hứa điều app không làm — mỗi dòng ok kèm bằng chứng hoặc FIX kèm file:line, Verdict PASS/FAIL. Use when someone wants a review before release, 'review app', 'app sẵn sàng lên store chưa', 'check trước khi submit', 'soát lỗi bị reject', 'audit bảo mật app', 'kiểm tra paywall đúng luật', or when scripts/app.py status says step 8 is next."
argument-hint: "[slug]"
user-invocable: true
---

# Bước 8 — review (CỔNG 4)

**Một việc:** `review.md` với `Verdict: PASS`. Còn một dòng `FIX` → `Verdict: FAIL` → `/app-build` hoặc `/app-fix`.
Vì sao có cổng này: bước 9 tạo bản build có số hiệu — số đã upload **không bao giờ dùng lại được**, và bị store từ chối
tốn 1–5 ngày mỗi vòng.

## 1. Máy chạy trước, người đọc sau

```bash
python3 scripts/test_app.py <slug>                    # test + analyze → run/out/tests.json
python3 scripts/run_app.py run <slug>                 # cả hai nền tảng, Read cả hai ảnh
python3 scripts/check_release.py apps/ACTIVE/<slug> --pre    # cấu hình, bundle id, targetSdk, secret key, restore
```

Dán **số thật** vào bảng "Máy đo". `analyze`: `error`/`warning` = FIX không ngoại lệ; `info` đọc từng dòng.

## 2. Soát bằng grep — những thứ máy tìm nhanh hơn mắt

```bash
cd apps/ACTIVE/<slug>/source/app
grep -rniE "donat|quyên góp|ủng hộ quỹ" lib/                       # phải rỗng (3.2.2(iv))
grep -rnE "sk_[A-Za-z0-9]{20,}" lib/ config/                       # phải rỗng (secret key)
grep -rnE "Color\(0x|Colors\.[a-z]" lib/ui --include=*_screen.dart # màu cứng trong màn hình → FIX
grep -rn "print(" lib/                                             # log lọt ra bản release
grep -n "uses-permission" android/app/src/main/AndroidManifest.xml # so với bảng Quyền trong spec
grep -n "UsageDescription" ios/Runner/Info.plist                   # mỗi quyền iOS có câu giải thích
```

## 3. Đọc theo checklist trong review.md

Giữ đúng các hàng của template. Mỗi hàng: `ok` + bằng chứng ngắn (file, test, ảnh) hoặc `FIX` + `file:line`.
Soi thêm những thứ lint không bắt:

- **Paywall:** chạy riêng `test/ui/paywall_screen_test.dart` — test này canh 5 thành phần bắt buộc. Nhìn screenshot
  paywall: giá thật theo chu kỳ, dòng tự gia hạn đọc được, nút đóng thấy rõ.
- **Pro:** tắt app mở lại vẫn Pro (đọc từ entitlement, không từ biến tạm).
- **3.2.2(iv):** không nút quyên góp; paywall/mô tả không nói tiền mua là quyên góp.
- **Privacy:** mọi SDK trong `pubspec.yaml` đã có trong bảng Data safety của listing.md; privacy URL mở được.
- **Đăng nhập:** có thì phải có xoá tài khoản trong app (Apple 5.1.1(v)).
- **Accessibility:** ảnh cỡ chữ lớn không cắt chữ; nút icon có `tooltip`/nhãn.
- **4.3(a) Spam:** đọc tên store + ảnh 1 + Home như người duyệt — 5 giây có thấy app khác loại bão hoà không? Tính năng giống template (scan → AI tạo X) không phải lõi thì tắt ở 1.0 (`reference/README-APP-PUBLISH-01-GUIDELINE-4-3-SPAM.md`).
- **Metadata:** không màn/tính năng ẩn; không nút "sắp ra mắt" dẫn vào hư không (Apple 2.1 / 4.2).

Muốn thêm một góc nhìn độc lập: `superpowers:requesting-code-review` hoặc `/code-review`.

## 4. CỔNG 4

Viết `Verdict: PASS` **chỉ** khi không còn FIX. Tóm tắt cho người dùng: đã kiểm gì, còn rủi ro gì (vd "chưa test mua thật
vì chưa có tài khoản sandbox"), và hỏi họ đồng ý sang bước ký bản build. Rủi ro chưa kiểm được thì ghi rõ "chưa kiểm",
không ghi ok.

LEARNED.md mục **Bước 8** · `scripts/app.py log` · tiếp theo `/app-release`.
