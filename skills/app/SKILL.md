---
name: app
description: "Router của pipeline làm app bán subscription cho người KHÔNG biết code — dẫn từ chưa có ý tưởng tới app có người trả tiền trên App Store + Google Play qua 15 bước (setup → research → money → spec → design → mockup → scaffold → build → run → review → release → listing → publish → marketing → grow), mỗi bước một skill app-* và một file kết quả trên đĩa, nên dừng ở đâu chạy tiếp ở đó. LUÔN hỏi stack trước khi tạo app (Flutter một-code cho iOS+Android / Native Kotlin+Compose + SwiftUI / chỉ một nền tảng / app Mac để bàn bằng Swift+SwiftUI), không tự mặc định Flutter; subscription qua RevenueCat, riêng app Mac bán ngoài store thì qua cổng thanh toán web. Claude làm thay và giải thích bằng lời thường sau mỗi bước, người dùng chỉ duyệt ở 4 cổng. Use when someone wants to build and sell an app, 'làm app', 'làm app bán subscription', 'tôi không biết code muốn làm app', 'build app từ A tới Z', 'app đang ở bước nào', 'bước tiếp theo là gì', 'đưa app lên store', 'kiếm tiền từ app', 'pipeline app', 'bắt đầu từ đâu', 'làm app cho máy Mac', 'app để bàn', or when unsure which app-* skill applies. Not for games (Game-AI-Skills), not for learning to type code yourself (kotlin-android-mentor / swift-ios-mentor)."
argument-hint: "[slug] — bỏ trống để liệt kê app"
user-invocable: true
---

# app — router

Người dùng **không biết code**. Họ muốn một app đàng hoàng, bán subscription.
Việc của Claude: làm thay từng bước, **nói bằng lời thường**, và dừng đúng 4 chỗ cần người quyết.

## Luôn bắt đầu bằng hai lệnh

```bash
python3 scripts/app.py list                 # có những app nào, mỗi app tiếp theo là gì
python3 scripts/app.py status <slug>        # bảng 15 bước (0–13 + 4b), tự ghi vào apps/ACTIVE/<slug>/context-ai/state.md
```

Khung thư mục app: gốc chỉ `README-<Tên>.md` + `app.json`; file .md ở `context-ai/`, code ở `source/`, plan ở `plan/active` (1 file) +
`plan/done`, kết quả chạy ở `run/out/` — `reference/README-APP-LAYOUT-01-APP-FOLDER.md`.


Chưa có app nào → `/app-setup` (kiểm máy) rồi `/app-research` (tìm ý tưởng). Định làm **app Mac mới** → chạy
`/best-app [cụm]` trước (ưu tiên số 1: kiểm portfolio, bản đồ tiền thật, chấm cụm, chọn 1 wedge). App chỉ được tạo
(`scripts/app.py init`) **sau** CỔNG 1, khi người dùng đã chọn ý tưởng.

## 15 bước (0–13 + 4b mockup)

| # | Skill | File kết quả | Xong khi | Người duyệt |
|---|---|---|---|---|
| 0 | `/app-setup` | setup.md | máy đủ công cụ (`Machine: ready`) | |
| 1 | `/app-research` | context-ai/research-<slug>.md | `Verdict: GO` | **CỔNG 1** chọn ý tưởng |
| 2 | `/app-money` | money.md | `check_money.py` 0 FAIL | |
| 3 | `/app-spec` | spec.md | checklist MVP + `Approved: yes` | **CỔNG 2** chốt tính năng |
| 4 | `/app-design` | design.md | `check_design.py` 0 FAIL + `Approved: yes` | **CỔNG 3** chốt giao diện |
| 4b | `/app-mockup` | mockup.md + design/mockup/*.png | `check_mockup.py` 0 FAIL — mỗi màn trong spec có ảnh (Codex sinh) | |
| 5 | `/app-scaffold` | app/ (Flutter) · android/ ios/ (native) · mac/ (macOS) | project build + test xanh | |
| 6 | `/app-build` | spec `[x]` + run/out/tests.json | mọi tính năng tick, test 0 fail | |
| 7 | `/app-run` | run/out/screenshot-<nền tảng>.png | có ảnh thật, Claude đã tự xem | |
| 8 | `/app-review` | review.md | `Verdict: PASS` | **CỔNG 4** trước khi ký bản build |
| 9 | `/app-release` | AAB + IPA đã ký · .app/.dmg đã ký (macOS) | `check_release.py` / `check_macos.py` 0 FAIL | |
| 10 | `/app-listing` · macOS: `/app-macos-listing` | listing.md · macos_listing.md + store/ | checker tương ứng 0 FAIL | |
| 11 | `/app-publish` | publish.md | `iOS: live` · `Android: production` · `macOS: released\|live` | người bấm trên store |
| 12 | `/app-marketing` · macOS: + `/app-mac-landing` · trang bán riêng oneclicktool.app: `/oneclicktool-landing` (+ `/app-video`) | marketing.md | `Launched: yes` | |
| 13 | `/app-grow` | grow.md | vòng lặp hằng tuần | |

Sau khi ra mắt: **`/app-feature`** (thêm tính năng) và **`/app-fix`** (sửa lỗi) — mỗi việc một file
file việc trong `plan/active/` của app — đúng 1 file: `plan-mvp.md` (chưa qua MVP) hoặc `plan-<type>-v<X>.md`; đổi plan = file mới lên version (`--replace`), file cũ sang `plan/done/` kèm `Tag: ko-lam`; xong thì `app.py plan-close <slug> --tag xong`, `status` liệt kê việc còn mở.

Skill phụ, các bước build tự gọi: **`app-flutter`** (nhánh mặc định) · **`app-native`** (Kotlin + Swift) ·
**`app-macos`** (app Mac để bàn — Swift 6 + SwiftUI, SwiftPM, sandbox, notarize) · **`app-paywall`** (RevenueCat + màn paywall).

Video (demo landing/YouTube/App Preview + shorts dọc có poster, dựng bằng Remotion từ bản quay app thật): **`/app-video`**.
Marketing từ số 0 (chưa có follower/email/tiền quảng cáo — định vị, 2 kênh, lịch 6 tuần thành file bài Promo Desk): **`/app-gtm`**.
Research nhu cầu trước khi làm (đã có ai thu tiền trên TrustMRR chưa, đối thủ, đối tượng, test bán trước trên X để ra mắt là có người mua): **`/app-demand`** — chạy trước hoặc thay Pha 2–4 của `/app-research`.
Học từ indie đang kiếm tiền (TrustMRR, Reddit, X — ý tưởng, giá, kênh, SEO, quảng cáo, mindset): **`/app-indie`** — gọi tay bất cứ lúc nào,
kết quả đổ vào research / money / marketing / grow.

## Luật router

1. **Đọc `status` trước khi làm.** Bước đầu tiên chưa `ok` là việc tiếp theo. Không nhảy cóc — trừ khi
   người dùng chỉ đích danh một bước, và khi đó nói rõ bước nào đang bị bỏ qua.
1b. **Trước khi tạo app (`init`), LUÔN hỏi stack** bằng `AskUserQuestion` (Flutter / Native Kotlin+Swift /
   chỉ một nền tảng) — xem mục "Chọn stack". Không tự chọn Flutter thay người dùng.
2. **Một bước một lần.** Xong → `python3 scripts/app.py status <slug>` → báo dòng vừa đổi.
3. **Bốn cổng là của người.** Không tự sửa `Verdict: GO`, `Approved: yes`, `Verdict: PASS` cho app thật.
   Hỏi bằng `AskUserQuestion`, ghi quyết định vào bảng "Quyết định đã chốt" trong state.md.
4. **Sau MỖI bước, dạy lại bằng lời thường** — 4 dòng, rồi ghi y hệt vào `apps/ACTIVE/<slug>/context-ai/LEARNED.md`:
   - *Vừa làm gì* (một câu, không thuật ngữ; thuật ngữ bắt buộc thì giải thích ngay trong ngoặc)
   - *Vì sao cần* (hậu quả nếu bỏ qua)
   - *File quan trọng* (đường dẫn, mở ra thấy gì)
   - *Lần sau tự làm* (đúng lệnh cần gõ)
5. **Ghi nhật ký:** `python3 scripts/app.py log <slug> --skill app-xxx "đã làm gì" --next "bước tiếp"`.
6. **Không bịa số.** Lượt tải, doanh thu, số sao, giá đối thủ: đo có nguồn + ngày, hoặc ghi `chưa đo`.
7. **Không bao giờ nói "chạy được"** khi chưa có screenshot Claude đã Read.

## Claude không bao giờ làm thay

Đăng nhập Apple/Google/RevenueCat · trả phí · ký thoả thuận · nhập thuế/ngân hàng · tạo keystore bằng mật khẩu
của người dùng · bấm Submit/Publish · cài plugin Claude khi chưa hỏi. Mỗi việc này: Claude chuẩn bị file +
chỉ đúng ô cần điền, người dùng bấm, Claude ghi log.

## Chọn stack — LUÔN HỎI, không tự mặc định

**Bắt buộc hỏi bằng `AskUserQuestion` trước khi tạo app** (`scripts/app.py init`), và nhắc lại xác nhận
ở đầu `/app-scaffold` nếu chưa hỏi. **Không bao giờ bay thẳng vào Flutter** — kể cả khi người dùng chỉ nói
"làm app đi". Câu hỏi 3 lựa chọn, ghi lựa chọn vào `app.json` `"stack"` + bảng "Quyết định đã chốt" trong state.md:

| Lựa chọn | Khi nào hợp | Ghi vào app.json |
|---|---|---|
| **Flutter** (gợi ý — một code chạy cả iOS + Android, nhanh nhất) | Một mình làm, muốn cả hai nền tảng, không cần API hệ điều hành sâu | `"stack": "flutter"` → nhánh `app-flutter` |
| **Native Kotlin + Swift** (Jetpack Compose + SwiftUI) | Cần API hệ điều hành sâu (widget màn khoá, HealthKit, Wear OS, BLE nặng), hoặc muốn code native thuần | `"stack": "native"` → nhánh `app-native` |
| **Chỉ một nền tảng** (native, chỉ Android *hoặc* chỉ iOS) | Chỉ nhắm một store | `"stack": "native"` + `--platforms android` hoặc `ios` |
| **App Mac để bàn** (Swift 6 + SwiftUI, cửa sổ/menu bar, đụng file trên máy) | Việc chỉ làm được trên máy tính: dọn file, xử lý ảnh/video hàng loạt, công cụ cho dân làm nghề | `"stack": "macos"` + `--distribution direct\|mas` → nhánh `app-macos` |

**App Mac là một app KHÁC app điện thoại**, không phải "bản Mac của app kia": slug riêng, listing riêng
(`/app-macos-listing`), cách bán riêng (bán thẳng .dmg đã notarize, hoặc Mac App Store). Hỏi luôn ở bước 2:
`--distribution direct` (tự thu 100%, phải ký + notarize, tự lo cập nhật) hay `mas` (Apple cắt 15–30%, sandbox bắt buộc).

Người dùng chọn xong, truyền đúng cờ khi tạo: `scripts/app.py init ... --stack flutter|native --platforms ios,android`,
hoặc `--stack macos --distribution direct|mas` cho app Mac.
Expo / React Native: không có nhánh build — chỉ tham khảo, xem reference/README-REFERENCES.md.

## Không gây quỹ trong app — luật xuyên suốt (chi tiết ở `/app-money`)

Subscription bán **giá trị thật của app**. Trong app không có nút quyên góp, không gọi việc mua là quyên góp
(Apple 3.2.2(iv): chỉ tổ chức phi lợi nhuận được Apple duyệt mới gây quỹ trong app).

## Tài liệu

`README.md` (bắt đầu) · `README-PIPELINE.md` (A→Z cho người mới, thời gian + chi phí) ·
`README-SKILLS.md` (quy ước skill) · `reference/README-SCRIPTS.md` · `reference/README-REFERENCES.md` (repo/skill cộng đồng + cách cài).
