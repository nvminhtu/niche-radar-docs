---
name: app-design
description: "Bước 4 của pipeline app — viết design guideline cho app vào design.md: tính cách thương hiệu, bảng màu sáng/tối dạng token (kiểm tương phản WCAG AA 4.5:1 bằng script), kiểu chữ, lưới khoảng cách, bo góc, vùng chạm tối thiểu, component, mọi màn hình với các trạng thái (rỗng/đang tải/lỗi/đã Pro), thiết kế paywall đủ thành phần store bắt buộc, accessibility (cỡ chữ 200%, đọc màn hình), hướng icon 1024 không alpha + prompt cho image generator; theo Apple Human Interface Guidelines + Material Design 3. Mockup từng màn làm ở bước kế tiếp /app-mockup (Codex sinh ảnh). Kết thúc ở CỔNG 3, rồi sinh code theme từ design.md bằng scripts/design_tokens.py. Use when someone needs the app's look, 'design guideline', 'chọn màu app', 'font chữ app', 'giao diện app trông thế nào', 'thiết kế paywall', 'dark mode', 'icon app', 'mockup màn hình', 'HIG', 'Material 3', 'app trông nghiệp dư quá', or when scripts/app.py status says step 4 is next."
argument-hint: "[slug]"
user-invocable: true
---

# Bước 4 — design (CỔNG 3)
> **Tuyến chạy do skill cha `core:asset-prompt` quyết định — đọc nó trước.**
> Codex/ChatGPT → sinh ảnh luôn. Claude → chỉ viết prompt (tuyến B), hoặc xuất thêm
> `jobs.json` (tuyến C) để user tự đem đi sinh ảnh rồi paste về `assets.raw_dir` trong
> `.claude/repo-profile.yaml`; `asset-prompt/scripts/collect_raw.py --apply` khớp và đổ
> ảnh vào đúng chỗ, rồi skill này chạy tiếp phần chuyên môn của nó.
> Không bao giờ tự vẽ thay ảnh thật, không coi prompt đã xuất là asset đã xong.


**Một việc:** `check_design.py` 0 FAIL và người dùng duyệt `Approved: yes`.
design.md là **nguồn duy nhất** của màu/chữ/khoảng cách — code theme sinh từ nó, màn hình không viết mã màu cứng.

Đọc: [references/design-guideline.md](references/design-guideline.md) — nguyên tắc HIG + M3 rút gọn, paywall, accessibility, icon.

## Pha 1 — Tính cách (tối đa 3 câu hỏi, AskUserQuestion)

1. App nên *cảm thấy* thế nào? (ấm áp/tươi vui · tối giản/tập trung · nghiêm túc/tin cậy — cho 3–4 lựa chọn gắn với người dùng mục tiêu ở research)
2. Người dùng chính và ngôn ngữ chính.
3. Có màu/logo sẵn chưa?

## Pha 2 — Mood board có bằng chứng

Lấy 3 app đầu từ research (trang App Store / Play có ảnh chụp màn hình). Ghi mỗi app **lấy gì** (nhịp khoảng cách,
cách trình bày danh sách, paywall) và **tránh gì**. Không chép màu/icon/tên.

## Pha 3 — Viết design.md

Template có sẵn. Luật:

| Mục | Làm |
|---|---|
| Colors | đủ 10 token (primary, onPrimary, secondary, onSecondary, background, onBackground, surface, onSurface, error, onError), Light + Dark, `#RRGGBB`. Mỗi `onX` trên `X` ≥ 4.5:1 |
| Typography | display / title / body / label. Body 16 (Material) – 17 (iOS). `Font family: system` trừ khi có lý do (font ngoài phải có license cho app) |
| Spacing & shape | lưới 8 · bo góc một giá trị · `Min touch target: 48` (Material 48dp ≥ Apple 44pt) |
| Screens | mỗi màn: rỗng · có dữ liệu · lỗi · (paywall) đang tải giá / đã Pro |
| Paywall | giá theo chu kỳ · dòng tự gia hạn · Restore · Terms · Privacy · nút đóng rõ — **không chữ quyên góp** |
| Accessibility | cỡ chữ hệ thống 200% không vỡ · nhãn đọc màn hình cho icon · không truyền đạt chỉ bằng màu |
| App icon | một hình, không chữ, đọc được ở 60px, 1024×1024 PNG không alpha. Viết prompt, **không tự vẽ** |

```bash
python3 scripts/check_design.py apps/ACTIVE/<slug>/context-ai/design.md
```

Màu fail tương phản → chỉnh độ sáng màu nền hoặc chữ tới khi qua; nói với người dùng màu nào đã đổi và vì sao
("chữ trắng trên xanh nhạt khó đọc với người thị lực kém").

## Pha 4 — Cho người dùng NHÌN

Người không biết code duyệt bằng mắt, không duyệt bằng bảng hex. Ở CỔNG 3 cho xem **một** ảnh Home (sinh qua
`core:asset-prompt`, không tự vẽ) nếu người dùng muốn; mockup đủ mọi màn là việc của bước kế tiếp **`/app-mockup`**
(bước 4b) — dev code bám theo ảnh đó.

## Pha 5 — Icon

Viết prompt vào mục `## App icon` (mẫu trong reference). Người dùng chạy qua image generator thật (hoặc skill
`image-gen` nếu có), lưu `apps/ACTIVE/<slug>/source/store/icon-1024.png`. Claude chỉ được resize/bỏ alpha, không vẽ lại.
Đặt icon vào app ở `/app-release` (Flutter: gói `flutter_launcher_icons`).

## CỔNG 3

Tóm tắt cho người dùng: 3 màu chính (tên màu bằng lời), cảm giác, paywall trông thế nào, ảnh mockup nếu có. Họ duyệt
→ `Approved: yes` → sinh theme:

```bash
python3 scripts/design_tokens.py <slug>     # Flutter: app/lib/ui/core/theme/tokens.dart (chạy lại được sau scaffold)
```

Chưa scaffold thì bước 5 tự sinh. Đổi màu sau này: sửa design.md → chạy lại lệnh → build.

LEARNED.md mục **Bước 4** · `scripts/app.py log` · tiếp theo `/app-mockup` (bước 4b), rồi `/app-scaffold`.
