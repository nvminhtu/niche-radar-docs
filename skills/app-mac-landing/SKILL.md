---
name: app-mac-landing
description: "Skill nhánh macOS cho landing page — thư viện học từ landing page của các app Mac native trong awesome-native-macosx-apps (201 app: Things, Bear, Craft, Nova, iA Writer, Pixelmator Pro, Raycast, CleanShot X, DaisyDisk…), gom thành 8 layout (icon · window · menubar · spotlight · editorial · bento · playful · docs) × 7 theme (native light · wallpaper · midnight · graphite · paper · candy · utility), có cột giải thưởng đã kiểm nguồn (ADA). Chọn layout + theme theo loại app, điền landing.md bằng 3 variant riêng cho app Mac (window · spotlight · editorial — ảnh cửa sổ ngang 16:10, phím tắt keycap, dòng Requires macOS + dùng thử), dựng bằng make_site.py, kiểm check_landing.py, Read ảnh desktop + 375px; soi lại atlas bằng scripts/landing_atlas.py. Used by app-marketing (bước 12) và app-macos-listing (trang tải) khi app.json stack là macos. Use when 'landing page app mac', 'trang web cho app mac', 'landing kiểu raycast', 'landing kiểu cleanshot', 'landing kiểu things', 'landing kiểu ia writer', 'theme landing mac', 'layout landing mac', 'học landing app mac đẹp', 'awesome native macos apps', 'app mac đoạt giải thiết kế', 'apple design award mac'. Không chép chữ/ảnh/logo của trang mẫu, không bịa giải thưởng."
argument-hint: "[slug]"
user-invocable: true
---

# app-mac-landing — landing page app Mac, học từ app native đẹp nhất

Dùng khi app có `"stack": "macos"` và tới lúc cần trang web (bước 12 `app-marketing`, hoặc trang tải ở bước 10
`app-macos-listing`). App điện thoại dùng thẳng 5 variant của `app-marketing`.

Mình **không chép** trang của ai. Mình học **bố cục (layout)** và **màu + chữ (theme)** của các trang làm tốt, rồi
`make_site.py` dựng từ `landing.md` của app mình, bằng ảnh chụp app mình.

## Nạp khi cần

| File | Khi nào |
|---|---|
| `references/layouts.md` | Pha 1 — chọn bố cục (8 kiểu, mạch từng kiểu, thứ app Mac luôn cần) |
| `references/themes.md` | Pha 1 — chọn màu/chữ (7 theme, bảng ghép layout × theme, tương phản đã đo) |
| `references/atlas.md` | muốn xem app nào làm kiểu nào, giải nào thật, trang nào nên soi trước |
| `app-marketing/references/landing-page.md` | mạch chung của landing (mục nào lấy chữ từ file nào), luật không bịa |

## Pha 0 — đọc app

```bash
python3 scripts/app.py status <slug>
cat apps/ACTIVE/<slug>/app.json        # stack: macos · min_macos · distribution (mas | direct)
```

Đọc `spec.md` (app làm gì), `money.md` (giá, có dùng thử không), `design.md` (màu chính → `Accent:`),
`marketing.md` (định vị một câu → Headline). Có ảnh chụp thật chưa: `apps/ACTIVE/<slug>/run/out/screenshot-macos*.png`,
`store/macos*/`. Chưa có ảnh → chạy `/app-run` trước; landing không dùng ảnh vẽ.

## Pha 1 — chọn layout + theme

1. Theo `layouts.md` "Bảng chọn nhanh": người mua cần thấy gì trong 3 giây đầu → layout → `Variant:`.
2. Theo `themes.md` bảng ghép → `Theme:` (ô **mặc định** khi không có lý do khác).
3. Mở `atlas.md`, chọn **2–3 trang mẫu** cùng layout (ưu tiên có giải, rồi cùng nhóm app). Ô Layout còn `?` →
   soi trang đó trước (Pha 4) rồi mới dựa vào. Ghi vào `LEARNED.md` 1 dòng: chọn gì · vì sao · học trang nào.
4. Không chắc giữa 2 kiểu → dựng cả hai (chỉ đổi dòng `Variant:`), Read ảnh, hỏi người dùng chọn.

## Pha 2 — điền landing.md

```bash
cp templates/landing.md apps/ACTIVE/<slug>/context-ai/landing.md     # nếu chưa có
```

Điền như `app-marketing` (Headline từ định vị, Features từ spec `## MVP`, Privacy, FAQ…), thêm phần riêng app Mac
trong `## Hero`:

| Dòng | Điền gì | Nguồn |
|---|---|---|
| `Hero media:` | **cửa sổ app thật** 16:10, chép vào `site/media/hero.png` (`menubar`: ảnh dải menu + popover) | `run/out/screenshot-macos.png` |
| `Requires:` | `Requires macOS <min_macos> or later` | app.json |
| `Trial:` | vd `Free 14-day trial` — **chỉ khi** money.md có dùng thử | money.md |
| `Shortcut:` | phím tắt thật của app, vd `⌥ + Space` (window · spotlight · editorial) | spec.md |
| Features `Image` | ảnh cửa sổ/panel thật, ngang | `run_app.py shot --platform macos` |

`distribution: mas` + đã live → `App Store URL:` (nút tự thành "Mac App Store"). `direct` → để trống, đặt
`email_form_url` (chưa bán) hoặc link trang tải `.dmg` vào `## Platforms` (đã bán).

## Pha 3 — dựng + kiểm + nhìn

```bash
python3 scripts/make_site.py <slug>
python3 scripts/check_landing.py apps/ACTIVE/<slug>      # tới khi 0 FAIL
```

Mở `site/index.html`, **Read screenshot 1280px và 375px** (cuộn hết để các mục hiện ra). Soát:
không cuộn ngang · chữ hero đọc được · cửa sổ app không vỡ/không mờ · tối thì ảnh app cũng tối ·
cùng mạch với trang mẫu đã chọn (đặt cạnh ảnh `research/<ngày>-mac-landing-atlas/shots/<mẫu>.png` nếu đã soi).
Chưa đạt → sửa `landing.md` (chữ, ảnh, variant/theme), không sửa HTML tay.

## Pha 4 — soi lại atlas (khi mạng cho phép)

```bash
python3 scripts/landing_atlas.py --only things,raycast,cleanshot-x   # vài trang
python3 scripts/landing_atlas.py                                    # cả 172 trang, ~10–20 phút
```

Ra `research/<ngày>-mac-landing-atlas/` (ảnh màn đầu 1440 + 375, `atlas.json`, `atlas.md`: nền, sáng/tối, phông, H1,
có video, giải được nhắc trên trang). Script chỉ đo — Claude **Read từng ảnh**, rồi sửa trong `references/atlas.md`:
Layout/Theme bỏ dấu `?`, cột Soi = ngày. Thấy kiểu bố cục lặp lại mà 8 kiểu chưa có → thêm vào `layouts.md`
(và variant mới vào `scripts/landing_page.py` nếu đáng), không thêm khi mới gặp 1 trang.
Môi trường cloud chặn host → báo người dùng host bị chặn; chạy trên máy Mac của họ là được.

## Trang quảng cáo riêng trên oneclicktool.app

Khi app đã live và cần trang để chạy quảng cáo/đăng social (style riêng, shorts, email, follow) → `/oneclicktool-landing`
(skill máy, `~/.claude/skills/oneclicktool-landing`). Skill này lo trang `site/` trong repo; trang kia lo oneclicktool.app.

## Không làm

- Không chép chữ, ảnh, logo, màu thương hiệu, mascot của trang mẫu. Học mạch + luật.
- Không ghi "Apple Design Award" hay giải nào lên trang mình nếu app mình chưa được (Proof cần link nguồn).
- Không khung MacBook giả, không giao diện vẽ tay/AI thay ảnh chụp app thật.
- Không coi ô `?` trong atlas là sự thật; không nói "trang X làm kiểu Y" khi chưa soi.
- Không thêm hạ tầng (Framer, CMS, analytics trả phí) — HTML tĩnh + GitHub Pages đủ cho MVP.
