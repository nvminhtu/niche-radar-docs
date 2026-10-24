---
name: best-app
description: "Skill research ƯU TIÊN SỐ 1 của repo — tìm ra MỘT app Mac đáng làm nhất, đúng nhu cầu, có người trả tiền, rồi mới code. Đi theo chiến lược 'micro app trước → gom module cùng tệp khách thành suite sau': (0) kiểm portfolio app đang có + research cũ, tránh làm trùng; (1) bản đồ tiền thật — TrustMRR, IndieMakerList, macapps.report, Setapp, Product Hunt, r/macapps — mỗi số có nhãn verified/tự khai/proxy/chưa đo + nguồn + ngày, ghi vào database dùng lại `research/<ngày>-<chủ-đề>.md`; (2) gom thành cụm việc (capture, file, clipboard, dev/AI-agent tools…) và chấm 6 tiêu chí; (3) đào sâu top 3 (đối thủ, review chê gì, câu nói người dùng — mượn /app-demand Pha 2–3); (4) chọn 1 wedge ship ≤ 4 tuần + đường lên suite/bundle; (5) test bán trước + luật dừng ngày 14/30/60/90; (6) đề xuất BUILD/TEST THÊM/BỎ chờ anh duyệt, kiểm bằng scripts/check_best_app.py. Use when '/best-app', 'app mac nào đáng làm', 'làm app mac kiếm tiền', 'super app mac', 'hệ sinh thái app mac', 'mackit', 'chọn hướng build', 'app nào bán được', 'đào sâu ý tưởng app mac', 'bảng 50 đối thủ mac'. Không bịa doanh thu, không tự ghi Verdict: GO, không code."
argument-hint: "[hướng/cụm, vd 'capture' | 'file tools' | trống = quét rộng] [--deep <cụm>]"
user-invocable: true
---

# best-app — chọn đúng MỘT app Mac đáng làm

Câu hỏi duy nhất: **app Mac nào mình làm được trong ≤ 4 tuần, có người đang trả tiền cho việc đó, mình với tới
được họ, và có chỗ khác đủ để họ đổi?** Kết thúc bằng một đề xuất có bằng chứng — không bằng "đã phân tích".

Skill này **sẽ được cập nhật dần** — mỗi lần chạy xong, thêm bài học vào `## Sổ học` cuối file.
Đánh giá chiến lược gốc (plan "Mac super app / MacKit Studio", 2026-10-18): [references/plan-review.md](references/plan-review.md).

## Luật cứng (từ CLAUDE.md, nhắc lại vì hay sai)

- Số nào cũng có **nhãn + nguồn http + ngày**: `verified` (cổng thanh toán, TrustMRR) · `tự khai` · `proxy` · `chưa đo`.
  Số của bài tổng hợp / ChatGPT / blog = `tự khai` tới khi tìm được nguồn gốc.
- Stack: **Swift 6 + SwiftUI, gói SwiftPM** (`scripts/native/new_macos_app.py`) — không Tauri/Electron: người dùng không
  code, repo đã có pipeline + 3 app Mac bán thật bằng Swift.
- Bán **direct** (.dmg notarize + Lemon Squeezy, như QuickCheck, RAM Rescue) ở 1.0; Mac App Store sau (đợt 4.3 cả tài khoản).
- Không cloud/backend ở 1.0. Không nhúng ffmpeg/HandBrake (GPL).
- Không super app ở 1.0. Suite chỉ là **gói bundle license** các app đã có người mua.

## Pha 0 — Portfolio trước, ý tưởng mới sau

```bash
python3 scripts/app.py list
ls research/ | grep -i -E "mac|capture|screen|trustmrr"
```

Ghi: app Mac nào đang **có doanh thu** (đo từ Lemon Squeezy / GA4 — anh xem, Claude không đăng nhập), app nào dở dang
cùng cụm. Nếu cụm đã có app/research (vd capture → `<slug>`, `research/<ngày>-<chủ-đề>.md`) → **đào tiếp
cái đó**, không mở app mới.

**Tỷ lệ chuyển đổi:** lấy số thật của app đang bán (visitor landing → mua, từ GA4 `store_click` + đơn Lemon Squeezy anh đọc).
App chưa có đơn (QuickCheck, RAM Rescue tới 2026-10-18) → ghi `chưa đo`, **không** mô phỏng doanh thu bằng % tự đặt.
Không có benchmark công khai nào cho app Mac bán direct mua đứt (WebSearch 2026-10-18 không ra). Số gần nhất là của app
subscription trên điện thoại (RevenueCat 2023: < 2% lượt tải thành người trả) → chỉ ghi nhãn `proxy`, không dùng để quyết.

## Pha 1 — Bản đồ tiền thật (database dùng lại)

Ghi vào bảng `research/<ngày>-<chủ-đề>.md` (thêm dòng, không xoá — số đổi thì thêm dòng mới ngày mới; 14 cột: Sản phẩm · Link · Cụm · Nền tảng · Giá · Doanh thu · Nhãn · Nguồn · Ngày · Làm gì · Bị chê gì · Kênh · Điểm · Việc tiếp).

Nguồn theo thứ tự tin cậy — chi tiết + cách đọc ở [references/plan-review.md §Nguồn](references/plan-review.md):
1. TrustMRR (`python3 scripts/demand_research.py trustmrr <slug>…`) — `verified`.
2. IndieMakerList Mac leaderboard, macapps.report, ShowMRR, thisiswhyibuilt — phần lớn `tự khai`.
3. App Store Mac (`python3 scripts/store_research.py search "<cụm>" --mac`, `iap <id>`, `mine <id>`) — giá, review chê.
4. Setapp categories, Product Hunt, r/macapps, HN, AlternativeTo — tín hiệu nhu cầu, **không** phải doanh thu.
   AlternativeTo, Product Hunt, Reddit `.json` trả 403 với curl (2026-10-18) → dùng WebSearch `site:<domain> <cụm>`.

**Đọc số TrustMRR cho đúng:** 30 ngày dao động mạnh (Screen Charm $2,054 ngày 07/10 → $395 ngày 18/10) → ghi cả
30 ngày + tổng + ngày lập; cột Sync cũ > 7 ngày thì ghi chú "sync cũ", không chấm 5 điểm Tiền thật dựa trên nó.
App mới trên `trustmrr-discover` có thể là đối thủ trực tiếp của app mình (vd Portlivo — menu bar hiện dev server, cùng việc với RAM Rescue) → thêm vào DB.

**Tìm slug TrustMRR:** đoán slug phần lớn 404 → lấy slug từ WebSearch `trustmrr <việc>` và link trên IndieMakerList,
rồi **luôn đo lại bằng script** — tóm tắt của WebSearch bịa số (ScreenSnipper "$172k" → thật $0/30 ngày, 2026-10-18).
**Đối thủ cùng việc trên Mac:** bắt buộc chạy `store_research.py search "<việc người dùng gõ>" --mac` + WebSearch
`<đối thủ SaaS> alternative mac one-time` — research StepSnap sót StepGrab (#1 Mac App Store), Folge, Shotomatic vì chỉ tìm theo tên app chụp màn hình.

Mục tiêu mỗi lần chạy: **15–25 app trong 1–2 cụm** đủ cột, không 50 app nông. Dữ liệu sâu > danh sách dài.

## Pha 2 — Cụm việc + chấm điểm

Gom theo **việc người dùng cần xong**, không theo tính năng. Chấm mỗi cụm 1–5:

| Tiêu chí | Trọng số | 5 điểm khi |
|---|---|---|
| Tiền thật | 3 | ≥ 2 app indie `verified` ≥ $1k/30 ngày trong cụm |
| Khe hở | 2 | đối thủ đầu bảng bị chê lặp ≥ 3 nguồn / bỏ lifetime / > 12 tháng không cập nhật |
| Với tới được | 2 | có keyword đo được (autocomplete/Trends) + subreddit/kênh cho tự giới thiệu |
| Làm được | 2 | API macOS có sẵn (ScreenCaptureKit, Vision, ImageIO, AVFoundation), ≤ 4 tuần, không server |
| Ít rủi ro Sherlock / 4.3 | 1 | Apple chưa có sẵn, không phải loại bão hoà (Sherlock = Apple làm sẵn trong macOS, vd Tahoe 26 có clipboard history trong Spotlight ⌘-Space ⌘-4) |
| Hợp portfolio | 1 | cùng tệp khách với app đang bán → bundle/cross-promo được |

Tổng /55 = 3·Tiền + 2·Khe + 2·Với + 2·Làm + Sherlock + Portfolio (checker tự cộng lại). Dưới 33 → không vào top 3.
Mỗi điểm phải có lý do một dòng trỏ về dòng DB / link — không chấm bằng cảm giác.

## Pha 3 — Đào sâu top 3

Mỗi cụm chạy `/app-demand <cụm> --mac --fast` (Pha 1–4 của nó: đối thủ 4 loại, ≥ 5 câu nói nguyên văn có link, khe hở + hook).
Không chép lại phương pháp ở đây.

## Pha 4 — Wedge + đường lên suite

Chọn **1** cụm. Viết:
- **Wedge 1.0**: 1 luồng chỉ mình có (4.3!) + 80% việc cơ bản, ship ≤ 4 tuần, giá thử (mua đứt $19–39 + trial 14 ngày).
- **Module 2–3** sau này (chỉ khi wedge có đơn): cùng khách, cùng shortcut/menu bar.
- **Bundle**: gói license gộp với app đang bán (Lemon Squeezy) — cách rẻ nhất để thử giả thuyết "super app".

## Pha 5 — Test bán trước + luật dừng

Landing + nút "Get early access $X" + 2–3 bài X (anh tự đăng) — theo `/app-demand` Pha 5. Luật dừng:

| Mốc | Phải có | Không có thì |
|---|---|---|
| Ngày 14 | ≥ 20 email / ≥ 3 click mua thử từ người lạ | đổi hook hoặc cụm #2 |
| Ngày 30 | beta có người ngoài dùng | sửa onboarding |
| Ngày 60 | đơn thật đầu tiên, hoặc lý do rõ vì sao chưa mua | xem lại giá trị Pro |
| Ngày 90 | retention + conversion đo được | quyết mở module 2 hay bỏ |

Ngưỡng là mặc định nội bộ — chỉnh trước khi chạy, ghi lại, không chỉnh sau cho đẹp số.

## Pha 6 — Ghi kết quả + đề xuất

Chép khuôn `templates/best_app.md` → `research/YYYY-MM-DD-best-app-<cụm>.md`, điền đủ 8 mục, rồi chạy tới 0 FAIL:

```bash
python3 scripts/check_best_app.py research/YYYY-MM-DD-best-app-<cụm>.md
```

- **BUILD** chỉ khi: Test bán trước `đạt` + `/app-demand` đã chạy + Tổng cụm #1 ≥ 40. Thiếu một → **TEST THÊM**.
- **BỎ** khi không cụm nào ≥ 33 — ghi cụm nào đã loại và vì sao để lần sau không đào lại.
- Ghi **"chờ anh duyệt"**. BUILD + anh duyệt → `/app-research` Pha 5–6 → `python3 scripts/app.py init` (CỔNG 1 vẫn của anh).
- Checker kêu → sửa số/quyết định, không sửa chữ cho qua regex.

## Sổ học (cập nhật mỗi lần chạy — mới nhất trên cùng)

- 2026-10-20 · `/best-app` "thời RAM đắt" → [research/<ngày>-<chủ-đề>.md](../../../research/<ngày>-<chủ-đề>.md):
  TEST THÊM, cụm #1 Dock (44). Bài học: **tin nóng (RAM đắt) ≠ từ khoá người ta gõ** — Trends `mac memory pressure` 0–7
  trong khi `system data mac` 14–36; kiểm Trends trước khi tin "nhu cầu cực cao". Đo TrustMRR theo **founder** (cùng số
  follower = cùng người): Cooldock + ExtraDock + DockFlow ~ $8.9k/30 ngày của 1 người làm SEO. Trước khi mở app mới, xem
  app nào **đã build xong mà chưa bán** (ScreenDocks 0.9.1 notarize, nằm im 9 ngày). Reddit/MacRumors chặn fetch (403) →
  câu nói nguyên văn lấy từ Apple Community.

- 2026-10-18 · `/best-app` quét nỗi đau Mac (một app $19 giải hết) → [research/<ngày>-<chủ-đề>.md](../../../research/<ngày>-<chủ-đề>.md):
  TEST THÊM. Ổ đầy/System Data đầu bảng (40) nhưng indie dọn ổ đĩa verified đều < $120/30 ngày; Supercharge $20 đã chiếm
  câu "một app sửa mấy chục chỗ". Bài học: quét rộng thì **đối chiếu với app mình đã có** trước — 4 app nhỏ chưa ai mua
  (Sweepy, Cooldown, RAM Rescue, ScreenDocks) chính là module của app gộp; trang /fix đang live là kênh đo sẵn.

- 2026-10-18 · Chạy thử `/best-app capture` → [research/<ngày>-<chủ-đề>.md](../../../research/<ngày>-<chủ-đề>.md):
  TEST THÊM. Tiền thật nằm ở việc "làm hướng dẫn" (Guidejar $6.5k, Shotomatic $1.1k verified), không ở quay/chụp thuần.
  Bài học: chia cụm to (capture) thành **việc** nhỏ (quay video · chụp · hướng dẫn · che) mới thấy tiền ở đâu;
  WebSearch tóm tắt số TrustMRR sai → luôn đo lại; tìm đối thủ theo việc, không theo loại app.

- 2026-10-18 · Rà lại skill: đo lại TrustMRR — Screen Charm tụt $2,054 → $395/30 ngày (sync cũ 24 ngày) → thêm luật đọc số 30 ngày.
  QuickCheck + RAM Rescue chưa có đơn → tỷ lệ chuyển đổi `chưa đo`, cấm mô phỏng bằng % tự đặt. Thêm khuôn + checker.

- 2026-10-18 · Tạo skill từ plan "MacKit Studio". Bài học: vấn đề hiện tại không phải thiếu ý tưởng (17 app, ~10 app Mac)
  mà là thiếu phân phối + thiếu chốt 1 app tới đơn đầu tiên → Pha 0 bắt buộc, giới hạn 1 wedge.
