---
name: app-spec
description: "Bước 3 của pipeline app — biến ý tưởng đã chọn (research GO) và mô hình tiền (money.md) thành spec.md, tài liệu mọi bước sau phải theo: checklist MVP gồm các lát cắt chạy được một mình (màn hình + logic + dữ liệu + test), bắt buộc có lát cắt Paywall, bảng màn hình với Free/Pro, dữ liệu lưu ở đâu, mọi quyền (permission) kèm lý do và lúc xin, đăng nhập thì phải có xoá tài khoản, chọn stack Flutter hay Native, danh sách ngoài phạm vi. Kết thúc ở CỔNG 2: người dùng tự sửa Approved: yes. Use when someone wants to plan app features, 'chốt tính năng app', 'MVP gồm gì', 'app cần mấy màn hình', 'viết PRD', 'lên kế hoạch app', 'có cần đăng nhập không', 'dùng Flutter hay native', 'cần backend không', or when scripts/app.py status says step 3 is next. Không viết code."
argument-hint: "[slug]"
user-invocable: true
---

# Bước 3 — spec (CỔNG 2)

**Một việc:** `spec.md` đủ rõ để bước 4–13 không phải hỏi lại. **Không viết code.**

## Đọc trước

`context-ai/research-<slug>.md` (khoảng trống §4 — lý do app tồn tại) · `money.md` (Free vs Pro, sản phẩm, vị trí paywall) · `state.md`.

## Checklist MVP — định dạng là hợp đồng với script

```markdown
## MVP

- [ ] Paywall: hiện giá từng gói, mua, khôi phục (Restore), link Terms + Privacy
- [ ] Ghi thói quen hôm nay: chạm để đánh dấu xong, bỏ đánh dấu được, lưu sau khi tắt app
```

`scripts/app.py status` chỉ đếm dòng `- [ ] ` / `- [x] ` **trong mục `## MVP`**. Mỗi dòng là **một lát cắt dọc**:
UI + ViewModel + dữ liệu + test, chạy được một mình. "Làm database" không phải một dòng.
money.md `Model: shop` → thay dòng Paywall bằng `- [ ] Shop: lưới gói có xem trước, giá từng gói, mua một lần,
khôi phục (Restore), link Terms + Privacy; gói đã mua mở khoá ngay` · `one-time` → Paywall chỉ một nút "trả một lần" ·
`paid`/`free` → không có dòng Paywall.

Cắt MVP bằng một câu hỏi: *bỏ dòng này thì app còn giải được lời than ở research §4 không, còn bán được Pro không?*
Còn → đưa xuống "Ngoài phạm vi v1". Mục tiêu 5–8 dòng cho MVP đầu tay.

## Quyết định mặc định (đổi thì ghi lý do trong spec)

| Hỏi | Mặc định | Đổi khi |
|---|---|---|
| Stack | **Flutter** | cần API hệ điều hành sâu / một nền tảng → Native · app chạy trên máy Mac (dọn file, xử lý ảnh/video hàng loạt) → `macos` (hỏi người dùng) |
| Kiến trúc | Screen (chỉ vẽ) → ViewModel → Repository (interface + Fake) | không đổi |
| Lưu dữ liệu | trên máy: `shared_preferences` (vài giá trị) · file JSON / `sqflite` (danh sách) | cần đồng bộ nhiều máy → Firebase |
| Đăng nhập | **không** | đồng bộ/chia sẻ → Firebase Auth + **nút xoá tài khoản** (Apple 5.1.1(v)) |
| Subscription | RevenueCat, entitlement `pro` | không đổi |
| Analytics | không ở MVP | sau ra mắt, và phải khai Privacy |
| iOS tối thiểu / Android minSdk | 15.0 / 24 · targetSdk 36 | Google Play đòi targetSdk 36 từ 2026-08-31 |
| Ngôn ngữ app | theo thị trường research chọn; chữ gom một file để dịch sau | |

Stack native: ghi `native` vào bảng App, **và** sửa `apps/ACTIVE/<slug>/app.json` `"stack": "native"` trước bước 5.

Stack macos: app để bàn — bảng App ghi thêm **macOS tối thiểu** (mặc định 14.0) và **cách phân phối**
(`direct` = .dmg đã notarize bán thẳng · `mas` = Mac App Store), vì nó đổi entitlement, cách ký và cả listing.
MVP của app Mac phải có thêm lát cắt **"hoàn tác"** cho mọi thao tác hàng loạt lên file người dùng, và bảng Quyền
ghi rõ app vào thư mục nào, xin lúc nào (`NSOpenPanel` + security-scoped bookmark). Luật viết code: skill `app-macos`.

## Quyền (permission) — mỗi dòng kéo theo khai báo trên store

Mỗi quyền = một dòng bảng Quyền = một câu khai **App Privacy** (Apple) + **Data safety** (Google) ở bước 10.
Ghi **lúc nào xin** (khi bấm tính năng, không phải lúc mở app). Thông báo nhắc nhở cũng là quyền.
Quyền nhạy cảm (vị trí nền, danh bạ, ảnh toàn bộ thư viện, SMS) → cảnh báo ngay trong spec, hỏi có thật cần không.

## Viết cho người không biết code

Mỗi dòng MVP viết bằng **hành vi người dùng thấy**, không bằng tên kỹ thuật:
- ✅ "Chạm vào thói quen để đánh dấu xong; tắt app mở lại vẫn còn"
- ❌ "Implement HabitRepository với SharedPreferences"

## CỔNG 2

Đưa spec cho người dùng đọc — tóm tắt 5 dòng: làm những gì, không làm gì, Free/Pro khác nhau ở đâu, cần quyền gì,
stack gì. Họ sửa `Approved: no` → `Approved: yes` (hoặc bảo Claude sửa **sau khi** họ nói đồng ý trong chat — ghi
vào "Quyết định đã chốt"). Không tự duyệt cho app thật.

Sau đó: LEARNED.md mục **Bước 3** · `scripts/app.py log` · tiếp theo `/app-design`.

## Khi đang build mà spec sai

`/app-build` phát hiện thiếu (vd màn ngang che nút) → sửa code, **thêm dòng vào spec** và tick, ghi một câu vì sao.
Tính năng mới người dùng chưa duyệt → **không** thêm vào MVP; ghi vào "Ngoài phạm vi v1" hoặc làm sau bằng `/app-feature`.
