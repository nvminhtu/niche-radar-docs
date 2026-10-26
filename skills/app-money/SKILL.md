---
name: app-money
description: "Bước 2 của pipeline app — quyết định app kiếm tiền thế nào và viết thành money.md đã kiểm bằng script: mô hình (khuyến nghị freemium + subscription qua RevenueCat; tuỳ app chọn mua đứt, shop = app free + gói nội dung mua một lần, trả tiền khi tải, hoặc free), Free vs Pro, sản phẩm tháng/năm và giá dựa trên giá đối thủ đo được, có trial không, paywall đặt ở đâu, những thứ store bắt buộc (Restore, giá theo chu kỳ, dòng tự gia hạn, link Terms + Privacy, chu kỳ ≥ 7 ngày), và luật không gây quỹ trong app: không nút quyên góp, không gọi subscription là quyên góp (Apple 3.2.2(iv)). Use when someone asks how the app makes money, 'bán subscription giá bao nhiêu', 'gói tháng gói năm', 'có nên cho dùng thử', 'paywall đặt ở đâu', 'freemium', 'app free bán gói', 'shop trong app', 'mua đứt hay subscription', 'RevenueCat', 'phí apple google bao nhiêu phần trăm', 'small business program', 'quyên góp trong app', or when scripts/app.py status says step 2 is next. Không hứa doanh thu, không tạo sản phẩm trên store thay người dùng."
argument-hint: "[slug]"
user-invocable: true
---

# Bước 2 — money

**Một việc:** `python3 scripts/check_money.py apps/ACTIVE/<slug>/context-ai/money.md` in `0 FAIL`.
Checker kêu = còn một quyết định chưa chốt. **Sửa quyết định, không sửa câu chữ cho qua regex.**

Đọc trước: [references/subscription-playbook.md](references/subscription-playbook.md) (luật store + cách định giá) và
[references/donation-rule.md](references/donation-rule.md) (không gây quỹ trong app).

## Pha 0 — Đọc app trước

`context-ai/research-<slug>.md` (khoảng trống, đối thủ thu gì), `state.md`. Cần trả lời được:

| Câu hỏi | Vì sao quyết định mô hình |
|---|---|
| Người dùng mở app bao lâu một lần? | hằng ngày/tuần → subscription; một lần → mua đứt |
| Phần nào có giá trị **lặp lại**? | đó là Pro. Apple 3.1.2(a): subscription phải "provide ongoing value" |
| Có **nội dung bán thêm được mãi** không? (theme, bộ icon/con trỏ, preset, sticker, level) | có → cân nhắc `shop` |
| Đối thủ bán gì, giá bao nhiêu? | `python3 scripts/store_research.py iap <id>` — mốc giá có nguồn |
| Có người dùng là trẻ em không? | Kids Category đổi toàn bộ luật (xem playbook §5) |

## Pha 1 — Chọn mô hình (hỏi từng câu bằng AskUserQuestion, ghi lý do)

1. **Mô hình** — mặc định `freemium-subscription`: bản Free dùng được thật (để có review tốt + lan truyền), Pro mở
   phần giá trị lặp lại. Nói là *khuyến nghị*, không phải luật.
   Khác: `one-time` (mua đứt qua IAP / license) · `shop` (xem dưới) · `paid` (trả tiền khi tải — giá đặt ở store,
   không IAP, không paywall, không trial; Products 1 dòng loại `paid app`) · `free`.
   Không ép subscription — chọn theo cách người dùng dùng app:

   | Người dùng… | Chọn | Ví dụ |
   |---|---|---|
   | mở hằng ngày/tuần, giá trị lặp lại | `freemium-subscription` | nhật ký, thói quen, học từ |
   | dùng thỉnh thoảng, một công cụ trọn gói | `one-time` | tiện ích dọn file Mac |
   | app là "cái kệ", tiền nằm ở **nội dung thêm được mãi** | `shop` | Cursor Craft: app free, bộ con trỏ bán lẻ |
   | không cần thu tiền / để kéo người dùng | `free` | |

   **`shop`** = app free dùng được thật (có sẵn vài gói free) + màn Shop bán từng gói **mua một lần, giữ mãi**
   (IAP Non-Consumable; app Mac `direct` = sản phẩm trên cổng thanh toán + license key). Hợp khi: làm thêm một gói
   rẻ (vài giờ), người dùng thấy gói trước khi mua (preview), và đối thủ cùng loại bán lẻ. Không hợp khi app là
   một công cụ không có "nội dung" (→ `one-time`). Không trial (cho xem trước thay vào đó).
2. **Free vs Pro** — bảng tính năng. Luật ngón tay cái: Free giải được vấn đề chính ở mức cơ bản; Pro làm nó
   nhanh hơn / sâu hơn / không giới hạn. Không khoá thứ người dùng đã tạo ra (dữ liệu của họ).
3. **Sản phẩm** — mặc định 2 gói auto-renew: **tháng** + **năm**. Giá: đặt trong khoảng giá đối thủ đo được,
   gói năm rẻ hơn rõ so với 12 × tháng. Không gói tuần cho app mới trừ khi đối thủ cùng loại đều dùng.
   Product ID giống nhau cho 2 store: `<slug_gạch_dưới>_pro_monthly`, `..._pro_annual`.
   `shop`: ≥ 2 gói `non-consumable` `<slug_gạch_dưới>_pack_<tên>` giá lẻ trong khoảng đối thủ, cộng gói
   `..._pack_all` (mở mọi gói, kể cả gói ra sau — ghi rõ trong copy) rẻ hơn rõ tổng các gói lẻ.
   RevenueCat: mỗi gói một entitlement `pack_<tên>`, gói all gắn mọi entitlement; offering `shop`.
4. **Trial** — mặc định `none` khi mới ra mắt (dễ đo, ít khiếu nại). Ghi `Trial: none` hoặc `Trial: <N> days`.
   Có trial thì chỉ trên gói năm (cột Trial của bảng Products), và paywall phải ghi rõ ngày bắt đầu trừ tiền
   ("14 days free, then $19.99/year") — checker FAIL nếu thiếu. App Mac: trial đi theo đường bán —
   `mas` bán đứt = IAP Non-Consumable giá 0 "N-day Trial" (phải có dòng trong Products), `direct` = app tự đếm +
   license key, ghi `License check: lemonsqueezy | keygen | own-server`. Mốc giá bán thẳng của indie (đã đo, có nguồn):
   `.claude/skills/app-indie/references/playbook.md` §2. Bảng đủ 4 ô:
   `.claude/skills/app-macos/references/trial-license.md`.
5. **Paywall đặt ở đâu** — (a) cuối onboarding, có nút đóng; (b) khi chạm tính năng Pro; (c) trong Settings.
   Không chặn người dùng trước khi họ thấy giá trị. `shop`: `## Paywall` là màn Shop — lưới gói có ảnh xem trước,
   giá từng gói, chữ "trả một lần", nút Khôi phục, link Terms + Privacy; mở từ tab/nút Shop và khi chạm gói khoá.
6. **App Mac (`stack: macos`) — hỏi thêm: bán đường nào.** Đây là quyết định đắt nhất của app Mac, chốt ở bước này:

   | | `direct` — .dmg trên web của bạn | `mas` — Mac App Store |
   |---|---|---|
   | Bạn nhận | ~95% (trừ phí cổng thanh toán) | 70–85% (Apple cắt 15–30%) |
   | Cổng thanh toán | Paddle / Lemon Squeezy / Stripe (Paddle, Lemon Squeezy làm luôn thuế VAT hộ) | StoreKit; link ra web mua chỉ ở storefront Mỹ (0% hiện tại) và EU (15%, 10% SBP) — playbook §3 |
   | `Provider:` trong money.md | tên cổng đó | `StoreKit` |
   | Phải làm thêm | ký Developer ID + notarize, tự lo cập nhật (Sparkle), tự lo license key | sandbox bắt buộc, chờ review |
   | Vẫn cần | tài khoản Apple Developer 99 USD/năm để ký | tài khoản đó + Paid Apps Agreement |

   Ghi vào `app.json` `"distribution"`. Bán ngoài store thì `Restore purchases` = "kích hoạt lại bằng license key /
   đăng nhập tài khoản" — vẫn bắt buộc có, vì người dùng đổi máy là chuyện thường.

## Pha 2 — Không gây quỹ trong app

Luật trong `donation-rule.md`. Checker bắt: `In-app donation: no` (trừ khi là nonprofit Apple đã duyệt) ·
copy paywall không có chữ quyên góp/donate.

## Pha 3 — Viết money.md

Template đã có sau `app.py init`. Điền đủ các dòng `Khoá: giá trị` ở đầu, các mục `## Value`, `## Free vs Pro`,
`## Products` (bảng), `## Paywall` (vị trí + copy trong khối ```), `## Doanh thu` (phép tính),
`## Manual gates`.

**Doanh thu — chỉ phép tính:** `người trả phí × giá × (1 − phí store) − thuế`. Phí store: Apple 15% nếu vào Small
Business Program (phải tự đăng ký), Google Play 15% cho subscription. Người dùng muốn con số → họ tự điền giả định,
Claude chỉ nhân giúp và ghi rõ "giả định".

```bash
python3 scripts/check_money.py apps/ACTIVE/<slug>/context-ai/money.md
```

## Pha 4 — Bàn giao

- Việc của người dùng (ghi trong `## Manual gates`): Paid Apps Agreement + thuế + ngân hàng (Apple) · Payments profile
  (Google) · tạo sản phẩm subscription trên App Store Connect / Play Console **đúng Product ID** · nối vào RevenueCat
  (entitlement `pro`, offering `default`). `shop`: tạo IAP **Non-Consumable** (Play: in-app product) cho từng gói,
  RevenueCat entitlement `pack_<tên>` + offering `shop`; mỗi gói mới sau này = thêm 1 IAP + 1 entitlement, không cần
  bản cập nhật nếu nội dung tải về được, ngược lại đi `/app-feature`. Plugin `revenuecat` có skill `create-revenuecat-project` hướng dẫn từng bước.
- `spec.md` sẽ có dòng MVP "Paywall" (`shop`: "Shop") — `/app-spec` đọc money.md để viết.
- App đã có `context-ai/profile.md` → chạy lại `python3 scripts/app_profile.py <slug>` để giá/trial trong hồ sơ khớp money.md.
- LEARNED.md mục **Bước 2** · `scripts/app.py log` · tiếp theo `/app-spec`.

## Không làm

- Không hứa doanh thu, không ước "tháng đầu kiếm được X".
- Không quyết định Kids Category thay người dùng — trình bày luật, ghi lựa chọn.
- Không tạo tài khoản, sản phẩm, hợp đồng trên store. Không nhập thông tin thuế/ngân hàng.
- Luật store đổi — thấy nghi thì WebFetch trang guideline gốc và ghi "đã kiểm ngày ...".
