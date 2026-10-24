---
name: app-feature
description: "Thêm một tính năng mới vào app đã có (ngoài MVP đã duyệt, thường sau khi ra mắt): tạo file việc trong apps/ACTIVE/<slug>/plan/ (feature, qua scripts/app.py change), viết yêu cầu thành tiêu chí nghiệm thu kiểm được, kiểm tác động (Free hay Pro, quyền/SDK mới kéo theo khai báo privacy, thay đổi listing, giá), làm theo vòng lặp app-build (repository + Fake → ViewModel → test → màn hình → chạy thật + screenshot), tăng version minor + build number, viết What's New, rồi đi release → publish. Use when someone wants to add something new, 'thêm tính năng', 'thêm nút', 'thêm màn hình mới', 'người dùng xin tính năng', 'làm nhắc nhở', 'thêm widget', 'thêm ngôn ngữ', 'thêm đăng nhập', 'app cần thêm X', 'bản cập nhật mới có gì'. Lỗi của tính năng đã có dùng /app-fix; tính năng nằm trong MVP chưa làm dùng /app-build."
argument-hint: "[slug] \"mô tả tính năng\""
user-invocable: true
---

# app-feature — thêm tính năng

**Một việc:** file việc (in ra bởi `app.py change` — `plan/active/` của app — đúng 1 file: `plan-mvp.md` (chưa qua MVP) hoặc `plan-<type>-v<X>.md`; đổi plan = file mới lên version (`--replace`), file cũ sang `plan/done/` kèm `Tag: ko-lam`; xong thì `app.py plan-close <slug> --tag xong`) có mọi tiêu chí tick, test xanh, screenshot đã xem, `status: done`.

## 1. Tạo file thay đổi

```bash
python3 scripts/app.py change <slug> --type feature --title "Nhắc nhở hằng ngày"
```

Tìm file cũ trước (`python3 scripts/app.py status <slug>` liệt kê thay đổi đang mở) — trùng thì làm tiếp file đó.

## 2. Hiểu yêu cầu thành tiêu chí

Chép yêu cầu **nguyên văn**. Viết 3–6 tiêu chí nghiệm thu bằng hành vi thấy được:
- ✅ "Bật nhắc lúc 20:00 → tắt app → 20:00 có thông báo → chạm vào mở đúng màn hôm nay"
- ❌ "Nhắc nhở hoạt động tốt"

Hỏi lại **chỉ khi** mơ hồ tới mức đổi thiết kế (vd "đồng bộ" = giữa các máy của một người hay chia sẻ với người khác?).
Còn lại chọn cách đơn giản nhất, ghi vào "Không làm".

## 3. Kiểm tác động — trước khi code

| Câu hỏi | Nếu có → |
|---|---|
| Free hay Pro? | cập nhật `money.md` Free vs Pro + `app_strings` lợi ích paywall; chạy `check_money.py` |
| Quyền mới (thông báo, ảnh, vị trí...)? | thêm dòng bảng Quyền trong spec.md + listing Data safety + câu `NS...UsageDescription` (iOS) |
| SDK/gói mới? | kiểm license + nhà phát hành trên pub.dev; thêm vào Data safety nếu thu dữ liệu |
| Đăng nhập? | bắt buộc nút xoá tài khoản trong app (Apple 5.1.1(v)) — tính vào phạm vi |
| Đổi giá / gói? | đi `/app-money` trước, không làm lén trong feature |
| Người dùng thấy khác trên store? | cập nhật listing.md (mô tả, ảnh) |

Tác động lớn (quyền nhạy cảm, đăng nhập, đổi giá) → tóm tắt cho người dùng và **hỏi** trước khi làm.

## 4. Làm

Theo đúng vòng lặp `/app-build` (repository + Fake → ViewModel → test → Screen → route → `test_app.py` → `run_app.py run` →
Read screenshot). Skill phụ: `app-flutter` / `app-native` / `app-macos` / `app-paywall`. Tick kế hoạch + ghi nhật ký trong file thay đổi.

## 5. Đóng gói bản cập nhật

1. Version: **không sửa tay** — `python3 scripts/release.py <slug> --minor` tự làm `1.0.0+5` → `1.1.0+6`, build, ký,
   đóng gói vào `publish/release/v<version>/` + `App-Ready-Publish/<Tên-store>/release/v<version>/` (app chưa từng lên store: bỏ `--minor`, chỉ tăng build).
2. What's New (listing.md — thêm khối, hoặc ghi trong file thay đổi): một câu người dùng hiểu, không "improvements".
3. Review nhanh: máy đo trong `app-review` §1 + các hàng review liên quan tới thay đổi.
4. `status: done` (frontmatter) trong file việc → `release.py` (bước 1) → `/app-publish` (upload lên track đang dùng, không cần closed test lại).

Giải thích cho người dùng 4 dòng + LEARNED.md (mục mới "Tính năng: <tên>") · `scripts/app.py log`.
