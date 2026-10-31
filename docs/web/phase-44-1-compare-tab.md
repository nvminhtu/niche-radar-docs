# Phase 44.1 · Tab Compare — gom mọi kiểu so sánh vào một chỗ

> Hôm nay "So sánh niche" và "So sánh project" nằm lẫn trong menu **More features**, mỗi cái một kiểu: niche ở `/compare`,
> project ở `/projects?compare=pick` (tick trong bảng project). Sau này còn **So sánh đối thủ** (Phase 56). Phase này đưa
> chúng về **một tab Compare** trên menu chính, có menu con **Niches · Projects · Competitors**, để người dùng biết
> "muốn so cái gì thì vào Compare".

<span class="chip chip--done">Xong 2026-10-31 · /compare + /compare/projects</span>

## Mục tiêu · cần làm · KHÔNG làm

- **Mục tiêu:** menu chính có tab **Compare ⌄**. Bấm chữ Compare → trang so niche (như bây giờ). Bấm ⌄ → 3 mục con:
    - **Compare niches** — trang `/compare` hiện có (Phase 44), giữ nguyên ruột.
    - **Compare projects** — trang riêng `/compare/projects`, dùng lại khối so 2 project đang nằm trong trang Projects.
    - **Compare competitors** — xám, ghi `Phase 56`, chưa bấm được.
- **Cần làm:** thêm tab ở menu · thanh tab con trên đầu mọi trang Compare · tách khối so project ra trang riêng ·
  chuyển link cũ sang chỗ mới · gỡ 2 mục so sánh khỏi More features · chữ en / vi / es · test · tài liệu.
- **KHÔNG làm:**
    - Không làm So sánh đối thủ ở đây — chỉ giữ chỗ (xám). Ruột của nó vẫn là [Phase 56](phase-56-compare-competitor.md).
    - Không đổi cách so niche (thẻ, bảng ô thắng, tab Đối thủ · Lời chê · Feature gap · Sức khoẻ, xuất CSV / Markdown).
    - Không nâng so project lên 3–4 project; vẫn đúng 2 như Phase 22.
    - Không thêm số liệu mới, không gọi nguồn mới, không AI.

## Menu sau khi làm

```text
ShotMatic   Niche · Explorer · AI Agent · Projects · Compare ⌄ · Settings ⌄ · More features ⌄
                                                    ├ Compare niches
                                                    ├ Compare projects
                                                    └ Compare competitors   (xám · Phase 56)
```

- Tab Compare đứng ngay sau **Projects** (so sánh là bước sau khi đã có niche / project).
- Dùng kiểu mục "vừa là link vừa có menu con" mà Settings đang dùng (`NavMenu`: mục có cả `to` lẫn `children`) —
  không viết menu mới.
- Tab sáng (gạch chân) khi đang ở bất kỳ trang nào dưới `/compare`.
- **More features** bỏ 2 dòng `Compare niches` và `Compare projects`. Còn lại: Reddit Gap, History, Guide, About…
- Bản Free / research-only: tab Compare vẫn hiện, các mục con xám kèm nhãn bản đầy đủ — y như cách 2 mục này đang xám
  trong More features (`off`). Không đổi luật Free / PRO.

## Trang Compare

Mọi trang dưới `/compare` có chung **thanh tab con** ngay dưới tiêu đề, xếp ngang (chip ngắn, không phải thẻ chữ dài):

```text
[ Niches ]  [ Projects ]  [ Competitors · Phase 56 ]
```

| Đường dẫn | Có gì | Ghi chú |
|---|---|---|
| `/compare` | So 2–4 niche (Phase 44), giữ nguyên | link cũ `/compare?runs=…` vẫn chạy |
| `/compare/projects` | Chọn 2 project trong danh sách → bảng so (khối `Compare` + API `/api/projects-compare` đang có) | ô chọn kiểu giống ô chọn niche: chip có tên + ngày |
| `/compare/projects?ids=a,b` | Mở thẳng bảng so 2 project | link chia sẻ được |
| `/compare/competitors` | Chưa tạo route — tab xám, không bấm được | Phase 56 làm thì thêm |

**Link cũ chuyển sang chỗ mới** (không để link chết):

- `/projects?compare=pick` → `/compare/projects`
- `/projects?compare=a,b` → `/compare/projects?ids=a,b`
- Nút "So sánh (N)" ở bảng Lịch sử vẫn mở `/compare?runs=…` như cũ.
- Trang Projects bỏ chế độ tick chọn để so; thay bằng 1 link nhỏ "So sánh project →" trỏ `/compare/projects`.

## Code đụng tới

| File | Sửa gì |
|---|---|
| `web/src/components/AppShell.tsx` | thêm mục Compare (to `/compare`, 3 children), gỡ 2 mục khỏi `nav.tools`, `active` theo `pathname.startsWith('/compare')` |
| `web/src/components/CompareTabs.tsx` (mới) | thanh tab con dùng chung, mục Competitors xám + `Phase 56` |
| `web/src/client/ComparePage.tsx` | gắn `CompareTabs` dưới tiêu đề |
| `web/src/client/CompareProjectsPage.tsx` (mới) | ô chọn 2 project + khối `Compare` tách từ `ProjectsPage.tsx` |
| `web/src/client/ProjectsPage.tsx` | bỏ `compare` param + `pick`; chuyển hướng link cũ; thêm link "So sánh project →" |
| `web/src/client/main.tsx` | route `/compare/projects` |
| `web/src/lib/features.ts` | thêm dòng "So sánh project" (`to: '/compare/projects'`), "So sánh đối thủ" giữ `soon` Phase 56 |
| `web/src/locales/en.ts` · `vi.ts` · `es.ts` | `nav.compareTab`, `nav.compareCompetitors`, chữ thanh tab con |
| `web/tests/` | menu có Compare + 3 con, More features không còn compare; link cũ chuyển đúng; trang `/compare/projects` mở được với `ids` |

## Xong khi

<div class="box box--star" markdown>
- Menu chính có **Compare ⌄**; bấm chữ ra trang so niche, ⌄ ra đúng 3 mục, Competitors xám ghi Phase 56
- More features không còn mục so sánh nào
- So 2 project thật từ `/compare/projects` ra đúng bảng như trước (kiểm tay 5 ô)
- Mở `/projects?compare=pick` và `/projects?compare=a,b` tự sang trang mới
- Menu không xuống dòng / không tràn ở **960px** và **1340px**, cả English lẫn tiếng Việt (chữ VN dài hơn) — screenshot đã Read
- `npm run check` xanh, `npm run docs:build` xanh
</div>

## Rủi ro

<div class="box box--rules" markdown>
- **Menu chật ở 960px:** thêm 1 tab trên cùng. Nếu tràn thì rút gọn nhãn ("Compare" thay vì "Compare niches") hoặc ẩn
  dấu `+` giữa các mục ở khung hẹp — không bỏ tab.
- **Nhãn tiếng Việt:** "So sánh" ngắn, ổn; chữ con dùng "So sánh niche · So sánh project · So sánh đối thủ".
</div>

## Sau phase này

Phase 56 (So sánh đối thủ) chỉ việc thêm route `/compare/competitors` và bật mục con — menu, thanh tab con, chỗ đứng đã sẵn.
