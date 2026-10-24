# Design guideline — nguyên tắc rút gọn cho app subscription đầu tay

Nguồn gốc (đọc lại khi cần chi tiết): Apple Human Interface Guidelines — developer.apple.com/design/human-interface-guidelines ·
Material Design 3 — m3.material.io · WCAG 2.2 — w3.org/TR/WCAG22. Đọc ngày **2026-09-15**.

## 1. Năm nguyên tắc chọn trước

1. **Nội dung trước, trang trí sau.** Màn hình là dữ liệu của người dùng; màu nhấn chỉ cho hành động chính.
2. **Một hành động chính mỗi màn** — một nút primary. Hành động phụ là nút chữ / icon.
3. **Theo hệ điều hành ở chỗ người dùng đã quen:** nút back, cử chỉ vuốt, sheet, share. Flutter Material chạy tốt
   trên iOS nếu giữ khoảng cách rộng và chữ hệ thống.
4. **Nhất quán hơn sáng tạo.** Một bo góc, một lưới, bốn cỡ chữ. Mọi giá trị lấy từ token.
5. **Tối và sáng đều là hạng nhất.** Kiểm cả hai trước khi duyệt.

## 2. Màu

- Token theo vai trò (primary / surface / error), không theo tên màu (green / red) → đổi thương hiệu không đụng code.
- Tương phản chữ thường ≥ **4.5:1**, chữ lớn (≥ 24px hoặc ≥ 19px đậm) và icon ≥ **3:1** (WCAG 2.2 SC 1.4.3, 1.4.11).
- Dark mode: nền không đen tuyệt đối (#111–#1C), primary sáng hơn bản light.
- Không mang thông tin chỉ bằng màu (vd trạng thái Pro: màu **và** chữ/icon).
- Công cụ gợi ý bảng màu có vai trò: Material Theme Builder (m3.material.io/theme-builder).

## 3. Chữ

| Style | Material 3 gần nhất | iOS gần nhất | Dùng |
|---|---|---|---|
| display | Display Small 36 | Large Title 34 | tiêu đề paywall, onboarding |
| title | Title Large 22 | Title 2 22 | tiêu đề màn |
| body | Body Large 16 | Body 17 | nội dung |
| label | Label Large 14 | Subheadline 15 | nút, nhãn |

- Cỡ chữ theo hệ thống (Dynamic Type / font scale): layout phải cuộn được, không cố định chiều cao chứa chữ.
- Tiếng Việt có dấu: kiểm dòng không bị cắt dấu ở line-height thấp.

## 4. Bố cục & chạm

- Lưới 8: khoảng cách 8/16/24/32.
- Vùng chạm ≥ **48dp** (Material) — lớn hơn mức 44pt của Apple, dùng chung một số cho cả hai.
- Lề màn 16–24. Nội dung dài luôn trong vùng cuộn; tôn trọng safe area (tai thỏ, thanh home).

## 5. Trạng thái bắt buộc vẽ

| Trạng thái | Nguyên tắc |
|---|---|
| Rỗng (lần đầu) | nói người dùng làm gì tiếp + một nút làm ngay |
| Đang tải | skeleton hoặc spinner trong đúng vùng đang tải, không che cả màn |
| Lỗi | nói chuyện gì xảy ra bằng lời thường + nút thử lại |
| Offline | dữ liệu trên máy vẫn dùng được |
| Đã Pro | ẩn nút nâng cấp, hiện trạng thái Pro ở Settings |

## 6. Paywall

Bắt buộc (store): tên/lợi ích gói · giá **theo chu kỳ** · dòng tự gia hạn + cách huỷ · Restore · Terms of Use ·
Privacy Policy. Nút đóng thấy rõ.

Chuyển đổi tốt *(thực hành phổ biến)*: tiêu đề nói kết quả · 3 lợi ích có icon · chọn sẵn gói năm · giá quy ra tháng
nhỏ dưới giá thật · nút chính full-width ở vùng ngón cái. **Không** đồng hồ đếm ngược giả, **không** giấu nút đóng.

## 7. Icon app

- 1024×1024 PNG, **không alpha**, không bo góc (Apple tự bo; Android adaptive icon có vùng an toàn 66%).
- Một hình đơn, không chữ, tương phản cao, đọc được ở 60px, nổi bật cạnh icon đối thủ ở trang kết quả tìm kiếm.
- Mẫu prompt (thay phần trong ngoặc):

```
App icon, single centered [biểu tượng, vd a small sprouting seedling inside a rounded check mark],
flat vector, bold simple shapes, [màu primary] on [nền tương phản] solid background,
soft subtle shadow, no text, no letters, no border, no rounded corners, square 1:1,
readable at very small size, modern iOS app icon style
```

## 8. Accessibility — kiểm trước khi duyệt

- [ ] Cỡ chữ lớn nhất hệ thống: không chữ bị cắt, không nút bị đẩy ra ngoài màn
- [ ] VoiceOver / TalkBack đọc được mọi nút icon (Flutter: `tooltip` / `Semantics(label:)`)
- [ ] Tương phản đạt (check_design.py)
- [ ] Không chỉ dùng màu để báo trạng thái
- [ ] Animation có thể giảm khi hệ thống bật Reduce Motion

## 9. Tham khảo thêm

- Flutter: skill `flutter-build-responsive-layout`, `flutter-fix-layout-issues` (plugin dart-flutter).
- Mockup: skill `design` (canvas) · Figma + Apple Design Resources (developer.apple.com/design/resources).
- Ảnh store (bước 10): `.claude/skills/app-listing/references/store-assets.md`.
