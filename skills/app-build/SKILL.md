---
name: app-build
description: "Bước 6 của pipeline app — làm từng tính năng MVP trong spec.md, mỗi lần một lát cắt dọc (repository có bản Fake → ViewModel → test → màn hình → điều hướng), chạy test và chạy app thật sau mỗi lát, chỉ tick [x] khi đã thấy nó chạy; theo kiến trúc đã scaffold, gọi skill phụ app-flutter / app-native / app-macos / app-paywall khi cần; sau mỗi lát giải thích bằng lời thường cho người không biết code. Use when someone wants features built, 'làm tính năng', 'code màn hình', 'làm tiếp app', 'thêm màn hình trong MVP', 'nối dữ liệu vào màn', 'làm paywall', 'implement feature flutter', or when scripts/app.py status says step 6 is next. Tính năng NGOÀI spec đã duyệt dùng /app-feature; sửa lỗi dùng /app-fix."
argument-hint: "[slug] [tính năng cụ thể — mặc định dòng - [ ] đầu tiên trong ## MVP]"
user-invocable: true
---

# Bước 6 — build

**Một việc:** mọi dòng trong `## MVP` của spec.md thành `- [x]`, và `run/out/tests.json` có test > 0, fail = 0.

## Vòng lặp — một lát cắt một lần

1. **Chọn** dòng `- [ ]` đầu tiên (hoặc dòng người dùng chỉ). Đọc mục Màn hình / Dữ liệu / Quyền liên quan trong spec,
   trạng thái màn trong design.md, Free/Pro trong money.md, và **ảnh mockup của màn đó** trong `design/mockup/`
   (bước 4b — Read ảnh, code bám bố cục; lệch spec/design thì spec + design.md thắng, xem `mockup.md` `## Ghi chú cho dev`).
2. **Nói trước bằng một câu** sẽ làm gì, người dùng sẽ thấy gì khi xong.
3. **Đọc code đang có** — theo đúng mẫu đã có (home/paywall/settings), không dựng kiến trúc mới.
4. **Viết từ dưới lên:** repository (interface + bản thật + bản Fake) → ViewModel → **test ViewModel** → Screen → route.
   Nhánh Flutter: `app-flutter` · Native: `app-native` · app Mac để bàn: `app-macos` · Lát cắt Paywall/subscription: `app-paywall`.
5. **Test:** `python3 scripts/test_app.py <slug>` — đỏ thì sửa trước khi viết tiếp.
6. **Chạy thật:** `python3 scripts/run_app.py run <slug> --platform ios` (và android) → **Read screenshot** → tự kiểm
   chữ bị cắt, màu đúng theme, trạng thái rỗng/lỗi. Sai → sửa → chạy lại.
7. **Tick `[x]`** trong spec.md. `python3 scripts/app.py log <slug> --skill app-build "<lát cắt>" --next "<lát tiếp>"`.
8. **Giải thích cho người dùng** (4 dòng — xem router) + thêm vào LEARNED.md. Gửi screenshot.

Tick khi **đã chạy**, không tick khi "viết xong".

## Luật kiến trúc (cả hai nhánh)

| Lớp | Được | Không được |
|---|---|---|
| Screen | đọc state từ ViewModel, gửi sự kiện, lấy màu/chữ từ theme, chữ từ app_strings | `if` nghiệp vụ, gọi repository, mã màu cứng, chuỗi cứng |
| ViewModel | giữ state, luật (`canUse`, validate), gọi repository | import UI/`BuildContext`, giữ widget |
| Repository | interface + bản thật + bản **Fake**; đọc dữ liệu dạng Stream/Future | để ViewModel tự `new` bản thật (truyền vào constructor) |
| Pro | chỉ đọc từ `SubscriptionRepository.isPro` (entitlement RevenueCat) | biến bool tự lưu "đã mua" |

## Khi nào dừng hỏi người dùng

- Lát cắt đòi **quyền mới** hoặc **SDK mới** không có trong spec → hỏi (kéo theo khai báo privacy).
- Thấy spec thiếu thứ hiển nhiên (vd không có cách xoá mục đã tạo) → sửa code, **thêm dòng vào spec**, tick, ghi vì sao.
- Tính năng mới người dùng chưa duyệt → **không** thêm vào MVP; đề xuất `/app-feature` sau ra mắt.
- Cùng một lỗi sau **3 lần sửa** → dừng, dùng `superpowers:systematic-debugging`, báo người dùng đang kẹt ở đâu
  (đừng thử mù lần thứ 4).

## Nói với người không biết code

- Không dán cả file code vào câu trả lời. Nói **file nào, làm gì**, kèm screenshot.
- Thuật ngữ lần đầu xuất hiện → giải thích trong ngoặc: "ViewModel (bộ não của màn hình — chứa luật, không chứa hình)".
- Báo lỗi bằng hậu quả: "nút Tiếp tục không bấm được vì chưa tải được giá" thay vì "state.canPurchase false".

## Xong bước 6

`python3 scripts/app.py status <slug>` → bước 6 ok. Tiếp theo `/app-run` (kiểm kỹ toàn app) rồi `/app-review`.
