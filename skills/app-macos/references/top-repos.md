# App Mac mã nguồn mở đáng đọc

Số sao đo bằng GitHub Search API ngày **2026-09-17**. Sao ≠ chất lượng code, nhưng repo nhiều người soi thì lỗi ngu đã bị bắt hết.
Đọc để học **cách tổ chức project, cách ký/đóng gói/phát hành, cách viết SwiftUI cho màn hình lớn** — không chép nguyên.

## Học cấu trúc + SwiftUI cho macOS

| Repo | ★ | Học được gì |
|---|---|---|
| [CodeEditApp/CodeEdit](https://github.com/CodeEditApp/CodeEdit) | 23.0k | app SwiftUI lớn nhất còn đọc được: chia module, `NavigationSplitView`, settings nhiều tab, trộn AppKit khi SwiftUI thiếu |
| [jordanbaird/Ice](https://github.com/jordanbaird/Ice) | 29.7k | menu bar app hiện đại, SwiftUI thuần, quản lý cửa sổ/quyền hệ thống |
| [exelban/stats](https://github.com/exelban/stats) | 41.9k | app nền chạy liên tục mà không ngốn pin — cách đo và tiết chế việc nền |
| [gao-sun/eul](https://github.com/gao-sun/eul) | 10.0k | SwiftUI + menu bar, project nhỏ đủ đọc hết trong một buổi |
| [sindresorhus/Plash](https://github.com/sindresorhus/Plash) | 4.0k | chuẩn mực code Swift của sindresorhus: nhỏ, sạch, hết sức "đúng kiểu Mac" |
| [milanvarady/Applite](https://github.com/milanvarady/Applite) | 7.0k | SwiftUI gọi công cụ dòng lệnh (Homebrew) an toàn — mẫu cho app bọc CLI |

## Đúng bài toán "dọn file / nén / trùng lặp"

| Repo | ★ | Học được gì |
|---|---|---|
| [tw93/Mole](https://github.com/tw93/Mole) | 67.6k | app dọn máy Mac: quét ổ đĩa lớn mà không treo UI, hiện cho người dùng thấy sắp xoá gì trước khi xoá |
| [alienator88/Pearcleaner](https://github.com/alienator88/Pearcleaner) | 14.6k | gỡ app + dọn file thừa: cách hỏi quyền, cách liệt kê file sẽ xoá, cách hoàn tác |
| [arsenetar/dupeguru](https://github.com/arsenetar/dupeguru) | 7.8k | (Python) thuật toán so khớp file trùng và ảnh "gần giống" — đọc logic, không chép code |
| [ImageOptim/ImageOptim](https://github.com/ImageOptim/ImageOptim) | 10.0k | cách gói nhiều tool nén ảnh thành một pipeline, và cách họ xử lý license từng tool con |
| [sindresorhus/Gifski](https://github.com/sindresorhus/Gifski) | 8.6k | xử lý video bằng AVFoundation + tiến trình + huỷ giữa chừng, UI SwiftUI |

## Ký · notarize · phát hành · cập nhật

| Repo | ★ | Học được gì |
|---|---|---|
| [sparkle-project/Sparkle](https://github.com/sparkle-project/Sparkle) | 9.7k | khung tự cập nhật ngoài App Store: appcast, ký EdDSA, cập nhật nền |
| [create-dmg/create-dmg](https://github.com/create-dmg/create-dmg) | 2.6k | dựng .dmg có nền, icon, vị trí — bản `hdiutil` trần trong Makefile là mức tối thiểu |
| [mas-cli/mas](https://github.com/mas-cli/mas) | 12.4k | Swift + SwiftPM + phát hành qua Homebrew, CI đầy đủ |
| [XcodesOrg/XcodesApp](https://github.com/XcodesOrg/XcodesApp) | 8.5k | app Mac phát hành ngoài store lâu năm: release notes, notarize, cask |

## Công cụ bắt buộc trong pipeline này

| Repo | ★ | Dùng để |
|---|---|---|
| [realm/SwiftLint](https://github.com/realm/SwiftLint) | 19.7k | `make lint --strict` — chặn force unwrap, `try!`, file quá dài |
| [nicklockwood/SwiftFormat](https://github.com/nicklockwood/SwiftFormat) | 8.9k | `make fmt` — hết cãi nhau về style |
| [jaywcjlove/awesome-swift-macos-apps](https://github.com/jaywcjlove/awesome-swift-macos-apps) | — | danh sách app Mac mã nguồn mở, tìm mẫu theo loại app |

## Lưu ý về danh sách repo trong plan cũ

`alienator88/SwiftUI-Boilerplate` (13★ ngày 2026-09-17) là repo cá nhân rất nhỏ — đừng lấy làm khung xương.
Cùng tác giả có **Pearcleaner** (14.6k★) là app thật, cùng bài toán dọn file: đọc cái đó.
Khung xương của pipeline này là `scripts/native/new_macos_app.py` — đã có sẵn kiến trúc, test, Makefile ký/notarize.
