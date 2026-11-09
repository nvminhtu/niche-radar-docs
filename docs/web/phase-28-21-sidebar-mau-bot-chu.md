# 3.2 · Giao diện mới: sidebar bên trái · màu đã kiểm chứng · bớt chữ (Phase 28.21)

> Hiện ShotMatic để tính năng trên một thanh menu ngang, phải mở 2 menu thả xuống mới thấy hết. Trang nào cũng nhiều chữ và
> chữ nhỏ. Các tool keyword / ASO lớn (appfigures, appbot, AppTweak) đều dùng **sidebar bên trái chia nhóm**, **số to + nhãn
> ngắn**, còn giải thích thì giấu sau icon ⓘ. Phase này đưa ShotMatic về khuôn đó: đổi khung app, chọn bảng màu và bớt chữ
> ở từng trang. Tính năng giữ nguyên.

<span class="chip chip--doing">M1 + M2 xong 2026-11-05 · M3 làm 2026-11-06, còn 3 trang chưa đạt mục tiêu chữ</span>

!!! note "Tiến độ M1 + M2 (2026-11-05)"
    - **Anh chốt màu A** (appfigures · trắng + xanh) ngày 2026-11-05.
    - **M1 đã có:** `web/src/components/SideNav.tsx` (nhóm có nhãn, mục con mở ngay trong sidebar, mục "sắp có" xám) thay
      `NavMenu.tsx` (đã xoá). `AppShell.tsx` thành lưới sidebar + cột nội dung, thanh trên 56px chỉ còn badge đang chạy · PRO ·
      Setup AI. Nút « thu sidebar thành dải icon 64px, nhớ ở `localStorage` (`shotmatic.sidebar`). Cửa sổ < 1100px tự thành dải
      icon, bấm nút thì sidebar mở đè lên. < 700px ẩn hẳn, mở bằng nút ☰. Bấm một mục thì sidebar đè tự đóng.
    - **M2 đã có:** token sáng `--canvas #f7f8fa` · chữ `#0c0d0e` · nút `--accent-solid #1a73e8` · link `--accent #1765c8`
      (đậm hơn `#228BF4` của appfigures, vì chữ trắng trên `#228BF4` chỉ đạt ~3,4:1, chưa tới AA 4,5:1) · cam ShotMatic còn
      ở `--brand` (logo, mục sidebar đang mở, chip PRO). 264 class `orange-*` dùng làm nút / viền chọn đổi sang `blue-*`. Cam
      mang nghĩa dữ liệu giữ nguyên: kết luận "TEST MORE", ô "gap", chip giá, thanh điểm. Bộ tối sinh lại (`npm run theme:dark`)
      sang xám lạnh. Nút bo 8px. `text-xs` 12px → 13px, `text-[11px]` → 12px, `text-[10px]` → 11px.
    - **Đã soát:** `npm run check` xanh (681 test, có 2 test mới cho sidebar) · 1340px + 960px + 375px, sáng + tối, không cuộn
      ngang · thu / mở sidebar nhớ đúng · sidebar đè đóng khi chuyển trang · nhãn tiếng Việt đúng trong test render.
    - **M3 đang làm (2026-11-05):** sau M2, chữ < 13px còn 0–1% ở Niche · Kết quả · AI Agent · Projects, Settings 10%.
      Đã cắt: trang Niche bỏ hàng chip giới thiệu, 2 link ngắn lại, chú thích bảng lịch sử + "Tick 2–4" vào ⓘ, cột Nguồn chỉ còn
      logo + chấm (tên ở `title`). AI Agent bỏ hàng chip, mô tả 3 thẻ ≤ 8 chữ, câu "Để trống cũng được" vào ⓘ, dòng phụ phiên
      chỉ còn giờ. **Còn lại:** trang Kết quả (bảng app store hiện cả 122 dòng = 2.234 chữ → cần phân trang; khối Expand
      766 chữ → gập), Settings, đo lại số chữ sau khi cắt.
    - **M3 làm tiếp (2026-11-06):** bảng kết quả 2 store phân trang theo số dòng ở Cài đặt (mặc định 20), sắp / lọc vẫn trên cả
      danh sách, đổi sắp / store / lọc thì về trang 1: khối này từ 2.730 chữ còn 550. Tab AI ở Settings: 3 đoạn giải thích dài
      (AI custom settings · Thư mục AI · Sổ dùng AI) vào ⓘ cạnh tiêu đề, không bỏ nội dung. Settings đã có tab từ trước.
    - **Giữ nguyên khối Expand:** plan định gập, nhưng anh đã chốt 2026-10-31 là luôn mở (ghi trong `RunDashboard.tsx`). Khối này
      ~840 chữ nên trang Kết quả chưa đạt mục tiêu ≤ 1.500. Muốn đạt thì cần anh đổi quyết định đó.
    - **Chưa làm:** Niche · Kết quả · tab AI còn trên mục tiêu (bảng dưới) · M4 (EN / VI, số trước–sau, mốc GA4) · chế độ mặc
      định (giữ Theo máy như cũ) · landing shotmatic.app.

    Đo lại 2026-11-06 ở 1340px, nền tối, tiếng Anh. **Đếm chữ thật sự hiện (`innerText` của `main`)**, không tính khối đang gập,
    nên bảng mục 1 (có đếm cả khối gập) không so trực tiếp được. Cả 5 trang không cuộn ngang ở 1340px; đã xem thêm
    Kết quả + tab AI ở 960px nền sáng.

    | Trang | Chữ đang hiện | Mục tiêu | Chữ < 13px |
    |---|---:|---:|---:|
    | Niche (`/`) | 476 | ≤ 250 | 1% |
    | Kết quả (`/r/107`) | 1.734 | ≤ 1.500 | 2% |
    | AI Agent (`/hunt`) | 274 | ≤ 250 | 2% |
    | Projects (`/projects`) | 267 | giữ | 1% |
    | Settings · tab AI | 753 | ≤ 400 | 0% |
    | Settings · Nguồn · Dữ liệu · Hiển thị | 162 · 188 · 92 (đếm cách cũ) | ≤ 400 | 1% |

## 1 · Vì sao làm — số đo hôm nay

Đo ngày 2026-11-05 trên bản web chạy local, cửa sổ 1340px, tiếng Anh, chế độ tối. Chỉ đếm chữ đang hiện trong `main`
(không tính menu).

| Trang | Số chữ đang hiện | Chữ nhỏ hơn 13px |
|---|---:|---:|
| Niche (`/`) | 400 | 42% |
| Kết quả 1 keyword (`/r/107`) | 4.368 | 46% |
| AI Agent (`/hunt`) | 498 | 66% |
| Projects (`/projects`) | 232 | 22% |
| Settings (`/settings`) | 1.458 | 50% |

Ở trang AI Agent, cứ 3 chữ thì 2 chữ có cỡ 11–12px. Trang kết quả có hơn 4.000 chữ, người dùng không đọc hết được.
Menu thì có 6 mục ngang, trong đó **Settings** và **More features** phải mở thêm mới thấy 9 trang con. Người mới không biết
Find Gaps, Social, History, Guide nằm ở đâu.

## 2 · Đối thủ làm thế nào

Mở trang bằng trình duyệt ngày 2026-11-05 và đọc màu, font, cỡ chữ từ CSS của trang. Riêng sidebar của appfigures lấy từ
ảnh chụp app thật trên trang chủ của họ, vì không có tài khoản.

### appfigures (appfigures.com)

- **Khung:** sidebar trắng bên trái, chia nhóm có nhãn xám nhỏ (*Your Apps* · *Optimization* · *App Intelligence*). Mỗi
  mục là icon + 2–3 chữ, mục có trang con thì có mũi tên `›`. Mục đang mở có nền đỏ nhạt + chữ đỏ.
- **Nội dung:** tiêu đề trang 1 dòng ("Keyword intelligence for *ai*"). Bên dưới là các thẻ **số to + nhãn 1–2 chữ**
  (*Popularity 75*, *Est. Revenue $54M*). Giải thích để sau icon ⓘ. Bảng có biểu đồ nhỏ ngay trong ô.
- **Màu đo được:** nền trắng `#FFFFFF` · chữ chính `#0C0D0E` · chữ phụ `#0C0D0E` 72% · nút chính xanh `#228BF4` chữ
  trắng, bo 8px · logo + mục đang mở dùng đỏ cam (đo trên ảnh, gần đúng).
- **Chữ:** Inter, thân 16px, chữ trong app 14px. Tiêu đề Satoshi đậm.

### appbot (appbot.co)

- **Khung:** sidebar trái chia 4 nhóm chữ hoa xám (*ANALYSIS* · *GROUPINGS* · *AUDIENCE* · *CONNECT & REPORTING*), 22 mục,
  mỗi mục icon + 1 chữ. Mục đang mở có nền cam nhạt + chữ cam.
- **Nội dung:** khối **Stats** chỉ có 4 số to (*Reviews 26,349* · *Avg Stars* · *Stars Breakdown* · *Sentiment
  Breakdown*), mỗi số kèm ⓘ. Bộ lọc nằm ở cột phải và gập được.
- **Màu đo được:** nút phụ cam `#ED8936` trên nền trắng. Cam này gần với cam ShotMatic, vậy là đối thủ cũng dùng cam cho
  tool phân tích.
- **Chữ:** chữ hệ thống, 16px. Tiêu đề Poppins.

### AppTweak (apptweak.com)

- **Chỉ đo được trang marketing**, chưa xem app thật vì cần tài khoản: nền kem `#FCF9F6` · chữ `#2A2825` · nút chính đỏ
  hồng `#C82C46` bo tròn hẳn · chữ Karla 18px · tiêu đề Bricolage Grotesque.
- Nền kem của AppTweak gần như trùng nền `--canvas: #fbf7f2` ShotMatic đang dùng.

### Điểm chung của cả 3

- Sidebar trái chia nhóm, mỗi mục icon + 1–3 chữ, mục đang mở có nền màu nhạt.
- Mỗi trang 1 tiêu đề 1 dòng, rồi tới số. Không có đoạn giải thích dưới tiêu đề.
- Số to trước, nhãn ngắn sau. Giải thích để sau icon ⓘ.
- Chữ trong app từ 14px trở lên, nhãn cột 12px. Không dùng 11px cho chữ cần đọc.

!!! warning "Nói thẳng về \"màu đã được chứng minh\""
    Chưa tìm được số A/B công khai nào cho thấy bảng màu của appfigures hay AppTweak làm người dùng ở lại lâu hơn. Lý do
    chọn theo họ là vì họ là tool lớn, nhiều người đã quen mắt, chứ không phải vì có số đo. Muốn biết có tốt hơn không thì
    đo bằng GA4 trước và sau khi đổi (mục 6).

## 3 · Sidebar mới

Bỏ thanh menu ngang. Sidebar trái rộng 232px gom đủ **15 trang** đang có, chia 4 nhóm. Ở trên chỉ còn 1 thanh mảnh:
tên trang, badge "đang chạy", chip PRO, Setup AI.

```text
┌──────────────────────┬─────────────────────────────────────────────┐
│ ShotMatic            │  Market research app        ● 1 running PRO │
│ [ + New niche search]│─────────────────────────────────────────────│
│                      │                                             │
│ RESEARCH             │   3.2 /10      Trend 2   Money 2.1  Comp 2.6 │
│  ⌕ Niche search      │   SKIP                                      │
│  ✦ AI Agent          │                                             │
│  ◎ Explorer          │   24/122        −82%        3/10            │
│  ↺ History           │   competitors   12-mo trend charge money    │
│                      │                                             │
│ PROJECTS             │   ...                                       │
│  ▣ Projects          │                                             │
│  ⇄ Compare        ›  │                                             │
│                      │                                             │
│ MORE SOURCES         │                                             │
│  ◇ Find gaps         │                                             │
│  ▶ YouTube · Amazon… │                                             │
│                      │                                             │
│ ───────────────────  │                                             │
│  ⚙ Settings       ›  │                                             │
│  ? Guide             │                                             │
│  ✦ Ask AI            │                                             │
└──────────────────────┴─────────────────────────────────────────────┘
```

| Nhóm | Mục (đường dẫn hiện có) | Ghi chú |
|---|---|---|
| (đầu sidebar) | Logo · nút **New niche search** (`/`) | nút chính duy nhất, luôn thấy |
| **Research** | Niche search `/` · AI Agent `/hunt` · Explorer `/?mode=explore` · History `/#history` | việc làm nhiều nhất, để trên cùng |
| **Projects** | Projects `/projects` · Compare `›` (niche `/compare` · project `/compare/projects` · đối thủ — *sắp có*) | Compare mở ra ngay trong sidebar, không dùng menu nổi |
| **More sources** | Find gaps `/reddit` · YouTube · Amazon · Maps `/social` | trước đây nằm trong "More features" |
| (đáy sidebar) | Settings `›` (Settings `/settings` · Quick setup `/quick-setup` · Setup `/setup` · License `/license`) · Guide `/guide` · About `/about` | việc chỉnh máy để dưới đáy như appfigures / appbot |

**Luật của sidebar**

- Mỗi mục: icon 16px + tối đa 3 chữ, 14px, cao 36px. Nhãn nhóm 11px chữ hoa, chỉ là nhãn, không cần đọc kỹ.
- Mục đang mở: nền màu nhạt + chữ màu chính + vạch 3px bên trái.
- Mục chưa làm: giữ nhưng xám + "sắp có" (theo `features.ts`). Không hiện số phase.
- **Thu gọn:** nút `«` thu sidebar thành dải icon 64px, nhớ lựa chọn trong `localStorage`. Cửa sổ hẹp hơn 1100px thì tự
  thu. Ở 960px nội dung còn 896px, không cuộn ngang.
- Bản demo (`IS_DEMO`) và bản Mac chỉ có Niche Research (`RESEARCH_ONLY`) ẩn mục giống như menu hiện giờ.
- Không sửa trong `app/`. App Mac + Windows tự có sidebar khi build lại.

**Code đụng tới:** `web/src/components/AppShell.tsx` (khung), `NavMenu.tsx` → đổi thành `SideNav.tsx`, `globals.css`
(`.shell-container` bỏ khung 1152px cứng, `.app-header`). Các trang giữ nguyên route.

## 4 · Bảng màu — anh chọn 1

Ba bộ dưới đều có đủ token sáng + tối. Chỉ thay giá trị trong `globals.css` (`--canvas`, `--surface`, `--accent`,
`--accent-solid`, `zinc-*`) rồi chạy `npm run theme:dark`, không sửa màu trong từng file `.tsx`.

### A · Theo appfigures — nền trắng, nút xanh (đề xuất)

- Nền trang `#F7F8FA` · mặt thẻ + sidebar `#FFFFFF` · chữ chính `#0C0D0E` · chữ phụ `#5B6168` · đường kẻ `#E6E8EC`.
- Nút chính + link + ô focus: xanh `#228BF4`, hover `#1A6FC4`.
- Cam ShotMatic `#C2410C` chỉ còn ở logo, chip PRO và mục sidebar đang mở, giống cách appfigures dùng đỏ cho logo.
- **Hợp vì:** app phân tích số, nền trắng + xanh làm số và bảng dễ đọc nhất. Đây là khuôn người làm ASO đã quen.
- **Mất gì:** app nhìn khác hẳn landing shotmatic.app (đang cam kem). Có thể phải sửa landing theo cho cùng một nhà.

### B · Theo AppTweak — nền kem, nút đỏ hồng

- Nền `#FCF9F6` · mặt thẻ `#FFFFFF` · chữ `#2A2825` · nút chính `#C82C46`.
- **Hợp vì:** gần với màu hiện tại (nền kem đã có), đổi ít nhất, landing không cần sửa.
- **Mất gì:** đỏ hồng dễ bị hiểu là "lỗi / nguy hiểm" ở trang có điểm SKIP màu đỏ. Phải đổi màu điểm xấu sang tím hoặc xám.

### C · Giữ cam ShotMatic, chỉ làm sạch

- Giữ `#C2410C`, đổi nền tối / kem sang trắng như A. appbot đang dùng cam `#ED8936`, nên cam vẫn hợp với tool phân tích.
- **Hợp vì:** giữ được thương hiệu. Cái làm trang khó đọc hôm nay là chữ nhỏ và nhiều chữ, không phải màu.

**Đề xuất A**: nút xanh tách hẳn khỏi màu điểm (xanh lá tốt · vàng vừa · đỏ xấu), nên người dùng nhìn là biết đâu là nút,
đâu là điểm. Nếu anh muốn giữ thương hiệu cam thì chọn C, tốn công ít hơn A.

## 5 · Bớt chữ — luật chung + từng trang

### Luật chung

- **Cỡ chữ sàn:** thân 14px · bảng 13px · nhãn cột / chip 12px. **Bỏ hẳn 11px** cho chữ cần đọc. Thêm test quét
  `text-[11px]` trong `web/src/` giống test `bg-white` đang có.
- **Tiêu đề trang:** 1 dòng, không có câu giải thích bên dưới. Câu giải thích chuyển vào ⓘ hoặc trang Guide.
- **Thẻ số:** số to (24–32px) + nhãn 1–3 chữ + ⓘ. Câu dài như "last 13 weeks vs first 13 weeks" chuyển vào tooltip.
- **Mỗi thẻ tối đa 1 câu.** Câu thứ 2 trở đi chuyển vào ⓘ hoặc khối gập "Xem thêm".
- **Hướng dẫn lần đầu** (Connect AI, 4-step guide, "First time?"): hiện 1 lần, tắt rồi thì không hiện lại. Gom về 1 thẻ
  Get started ở trang Niche.
- **Bảng:** cột phụ ẩn theo bề rộng khung (`@container`). Chữ dài thì `truncate` + `title`.

### Từng trang

| Trang | Bỏ / dời | Mục tiêu chữ đang hiện |
|---|---|---|
| Niche `/` | 4 chip giới thiệu dưới tiêu đề → 1 dòng · 2 link "First time? / Or let the AI Agent" → thẻ Get started · câu dưới bảng lịch sử → ⓘ | ≤ 250 |
| Kết quả `/r/:id` | trên cùng chỉ để điểm + 3 thanh + 4 thẻ số · "Do these 3 things next" gập lại · mỗi khối nguồn (Trends, Play, App Store…) mở dạng tab hoặc gập, chỉ mở khối đầu | ≤ 1.500 khi mới mở trang |
| AI Agent `/hunt` | mô tả dưới 3 thẻ chọn ≤ 8 chữ · 4 chip dưới tiêu đề → bỏ · danh sách phiên: dòng phụ chỉ còn "4 candidates · Step 5/7" | ≤ 250 · không còn chữ 11–12px ngoài nhãn |
| Settings `/settings` | chia tab trái (General · AI · Data · Privacy · License) thay vì 1 trang dài · mô tả mỗi ô → ⓘ | ≤ 400 mỗi tab |
| Projects `/projects` | đã gọn, chỉ đổi cỡ chữ theo luật chung | giữ |

Các con số mục tiêu ở trên là ước, đo lại bằng đúng script ở mục 1 sau mỗi bước.

## 6 · Các bước

| Bước | Việc | Xong khi |
|---|---|---|
| **M1 · Khung sidebar** | `SideNav.tsx` 4 nhóm + thu gọn · thanh trên mảnh · bỏ menu ngang · giữ đủ 15 trang, ẩn đúng ở demo / Mac | mọi route mở được từ sidebar · 960px + 1340px không cuộn ngang · test SideNav (nhóm, mục đang mở, ẩn khi `IS_DEMO`) |
| **M2 · Màu + chữ** | đổi token theo bảng anh chọn · `theme:dark` · cỡ chữ sàn 14 / 13 / 12 · test chặn `text-[11px]` | `npm run check` xanh · soát sáng + tối · chữ < 13px ≤ 10% ở cả 5 trang (đo lại script mục 1) |
| **M3 · Bớt chữ** | làm theo bảng "Từng trang", lần lượt Niche → Kết quả → AI Agent → Settings | đạt mục tiêu chữ từng trang · không mất tính năng nào (bấm hết nút cũ vẫn tới được) |
| **M4 · Soát + đo** | screenshot 960 / 1340 · sáng / tối · EN / VI · ghi số trước–sau vào trang này · đặt mốc GA4 (thời gian trên trang Kết quả, tỉ lệ bấm New niche search) | số trước–sau có ngày · GA4 đo 2 tuần sau khi lên bản |

Ảnh mockup sidebar (nếu cần trước M1): Claude viết prompt, Codex sinh bằng `codex exec`, không tự vẽ.

## 7 · Cần anh chốt

1. ~~**Bảng màu**~~ → **A**, anh chốt 2026-11-05.
2. **Chế độ mặc định:** đổi sang Sáng làm mặc định như cả 3 đối thủ, hay giữ theo hệ thống như hiện giờ?
3. **Landing shotmatic.app** có đổi màu theo app không, nếu chọn A?

## Không làm ở phase này

- Không thêm tính năng mới, không đổi route, không đổi cách chấm điểm.
- Không sửa giao diện trong `app/`.
- Không chép logo, icon hay hình của đối thủ. Chỉ học cách xếp và bảng màu.

Liên quan: [Đối thủ · tool phân tích thị trường](../marketing/doi-thu.md) · [Phase 28.20 · 3 lối vào AI Agent](phase-28-20-ai-agent-3-loi-vao.md) ·
[Phase 28.14 · Mọi trang cùng bề rộng](phase-28-14-full-width-pages.md)
