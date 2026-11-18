# 16 · Trang Project dễ xài: loại, 4 chặng, bàn chấm gọn

> Plan 2 · mục 16. Project là **điểm cuối** của app: anh chọn keyword, đối thủ, lời chê bỏ vào, rồi tự chấm hoặc nhờ AI chấm,
> rồi lên Brief / Spec / Plan. Nhưng trang Project bây giờ khó xài: không biết project loại gì, 8 tab không nói tab để làm gì,
> Bàn quyết định nhiều chữ, còn Brief / Spec / Plan lại nằm riêng ở mục AI Agents.

<span class="chip chip--doing">Anh duyệt 2026-11-15 · 16.1 + 16.2 đã code · 16.3–16.5 chưa làm</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Anh mở mục này ngày 2026-11-15.
</div>

## Anh chốt (2026-11-15)

- **Mỗi project 1 loại cố định:** 📱 App · ▶️ YouTube · 📖 Sách. Mỗi loại có icon, màu, bàn chấm riêng.
- **Tab xếp theo 4 chặng**, không theo loại dữ liệu: ① Gom → ② Chấm → ③ Làm → ④ Theo dõi.
- **Gộp AI Agents vào Projects:** phiên AI Agent chỉ còn là 1 cách tạo project, Brief / Spec / Plan có ở mọi project.

## Bây giờ khó xài ở đâu

| Anh thấy | Lý do trong code |
|---|---|
| Không biết project là App, YouTube hay Sách | bảng `projects` không có cột loại. Trang Sách gom sang như keyword thường, YouTube chưa có nút gom |
| 8 tab không biết làm gì, có tab thừa không | tab chia theo loại dữ liệu (Keyword, Đối thủ, Lời chê, Khoảng trống…), tab trống vẫn hiện, không tab nào nói “bước này để làm gì” |
| Bàn quyết định rối | mỗi keyword hiện 2 đèn lớn + 5 trục + ô mã nguồn + ô lý do + nút Copy prompt / Dán JSON / trần token cùng lúc |
| Tên, ngày sửa không nhìn phát biết ngay | chỉ là chữ xám “19 items · updated 2026-11-14 19:07”, trạng thái là chip chữ |
| Quyết định làm rồi mà Brief / Spec / Plan ở chỗ khác | thẻ tài liệu chỉ chạy với project `kind = hunt` (tạo từ AI Agent), project gom tay không có |

## 16.1 · Loại project

<span class="chip chip--done">Đã code 2026-11-15</span>

- Thêm cột `projects.type`: `app` · `youtube` · `book`. Project cũ = `app`.
- Loại được đặt **lúc tạo**, tự đoán từ trang đang đứng: gom từ Research / Explore → App, từ trang Sách → Sách, từ YouTube → YouTube.
  Tạo tay ở trang Projects thì chọn 1 trong 3 ô có icon.
- Gom 1 thứ khác loại vào project (vd sách vào project App) → hỏi lại 1 câu, gợi ý tạo project mới đúng loại.
- Mỗi loại 1 icon + 1 màu, dùng ở mọi chỗ: đầu trang project, danh sách Projects, ô chọn project của nút + Collect.
- Danh sách Projects có 3 chip lọc theo loại.
- Khi code (2026-11-15): chỉ trang Sách đang có nút + Collect riêng nên chỉ chỗ đó truyền loại Sách; Explore / Research vẫn mặc định App. Tool MCP `create_project` tạo project App.
- YouTube chưa có nút gom: mục này chỉ để sẵn loại. Nút gom kênh / video vào project và bàn chấm riêng cho YouTube, Sách → **16.6, chưa spec**.

## 16.2 · Đầu trang nhìn phát biết ngay

<span class="chip chip--done">Đã code 2026-11-15</span>

Một hàng, mỗi thông tin 1 icon:

| Thông tin | Hiện thế nào |
|---|---|
| Loại | ô vuông icon màu (📱 / ▶️ / 📖) bên trái tên |
| Tên | chữ lớn, 1 dòng, `truncate` + `title` |
| Trạng thái | icon + chữ: 👀 đang xem · ⭐ ứng viên · 🔨 đang build · ✕ loại |
| Ngày sửa | 🕒 “sửa 2 giờ trước” (ngày giờ đầy đủ trong `title`) |
| Việc tiếp | 📅 “hẹn 18/11: viết Spec”. Tới hạn → màu cam, quá hạn → màu đỏ |

Rename · Duplicate · Archive · Xuất file · Gộp project dời vào nút **⋯**, đầu trang chỉ còn tên và trạng thái.

**Còn lại sau khi code 16.1 + 16.2 (dời sang 16.3, cùng sửa đầu trang):** Xuất file và Gộp project chưa dời vào ⋯;
hỏi lại khi gom khác loại mới chỉ “Vẫn thêm?”, chưa gợi ý tạo project mới đúng loại; English số ít (“1 items”, “1 hours ago”);
hạn việc tiếp ở danh sách Projects còn tính theo giờ UTC; quá hạn chỉ báo bằng màu; gộp 2 project khác loại chưa hỏi lại.

## 16.3 · 4 chặng thay 8 tab

Thanh chặng ngay dưới đầu trang. Chặng xong có ✓, chặng đang ở có viền màu, mỗi chặng kèm 1 con số:

| Chặng | Số trên thanh | Bên trong | Xong khi |
|---|---|---|---|
| ① Gom | số thứ đã gom | chip lọc Keyword · Đối thủ · Lời chê · Khoảng trống (ẩn chip 0), danh sách `ProjectItems` như cũ | có ≥ 1 keyword |
| ② Chấm | verdict của keyword chính | bàn chấm gọn (16.4) + trạng thái project + ô Kết luận | có verdict đã chốt |
| ③ Làm | “1/3 tài liệu” | chọn 1–3 đối thủ bắt chước → Brief / Spec / Plan → Xuất bộ build (lấy từ tab Build của mục 13) | đã xuất bộ build |
| ④ Theo dõi | số keyword theo dõi | `TrackingBlock` như cũ | (không có ✓, chạy mãi) |

- Mở project → vào **chặng đầu chưa xong**. Link cũ `?tab=keywords` / `competitors` / … vẫn mở đúng chỗ (chặng Gom + chip tương ứng).
- **Ghi chú & nhật ký** thành nút 📝 trên đầu trang, mở khung bên phải, không còn là tab.
- Mỗi chặng có 1 dòng “bước này để làm gì” ngắn, giải thích dài gập vào ⓘ.
- Ô **Bước tiếp + ngày hẹn** nằm ở cuối chặng đang mở, lưu xong hiện lên đầu trang (16.2).

## 16.4 · Bàn chấm gọn

Mỗi keyword 1 thẻ (xem phác thảo trong phiên 2026-11-15):

- Trên cùng: 1 đèn lớn **Nên làm?** (Làm / Tra thêm / Bỏ) + chữ nhỏ “gợi ý từ số đo ⓘ”.
- Giữa: các trục là **thanh ngang có màu** + 1 chữ (thấp / mạnh / có), không còn ô chữ dài.
  “Độ phủ keyword” thôi là đèn lớn thứ 2, gộp thành chip trên thanh Đối thủ.
  Trục chưa có số → thanh xám “chưa đo”. Trục tự chấm (Công sức) → 5 nút 1–5 như cũ.
- Bấm 1 trục → mở dẫn chứng: số đo kèm mã nguồn, ô mã nguồn, ô lý do (giữ nguyên logic bây giờ).
- Dưới: 3 nút verdict + ô lý do 1 dòng.
- Copy prompt cho AI · Dán JSON AI · trần token · lịch sử bản chấm → gom vào 1 nút **✨ Nhờ AI chấm**, mở ra mới thấy.
- Khối “Rủi ro” và “Dữ liệu còn thiếu” gập lại, chỉ hiện số dòng.
- Project nhiều keyword: thẻ keyword chính mở, các thẻ khác gập thành 1 hàng (tên · đèn nhỏ · verdict).
- Logic chấm, dẫn chứng, mã nguồn, luật “không có dẫn chứng thì không tính” **giữ nguyên**: chỉ đổi cách hiện.

## 16.5 · Gộp AI Agents vào Projects

- Mục **AI Agents** ở menu trái bỏ đi. Nút **+ Project mới** ở trang Projects mở 4 cách tạo:
  tạo trống · Niche Search · Niche Autopilot · Tôi đã có app / web (3 cách sau lấy từ trang AI Agents bây giờ).
- Phiên AI Agent cũ vẫn là project: link cũ `/hunt/:id` tự chuyển sang `/projects/:id`.
- Chat AI ghim của phiên → nút **Ask AI** trong project mở đúng phiên chat đó (`chatSession`), không mất lịch sử.
- Brief / Spec / Plan chạy được ở **mọi project**: lần đầu bấm viết thì project tự nhận chỗ chứa tài liệu (không cần tạo lại).
  Vẫn cần PRO + AI đã cài, như bây giờ.
- Autopilot đang chạy → thanh tiến độ hiện trên thanh chặng (chặng nào AI đang làm thì nhấp nháy), không cần trang riêng.

## Thứ tự làm

1. **16.1 + 16.2**: loại + đầu trang (nhỏ, thấy ngay, không đụng logic).
2. **16.3**: 4 chặng (dời các khối có sẵn vào chặng, không viết lại).
3. **16.4**: bàn chấm gọn (chỉ đổi cách hiện).
4. **16.5**: gộp AI Agents (đổi menu + chuyển hướng + tài liệu cho mọi project).

Mỗi bước 1 spec code + plan riêng khi tới lượt, anh duyệt từng bước.

## Đổi gì trong code (ước lượng)

| Chỗ | Đổi |
|---|---|
| `db/schema.ts` + migration | cột `projects.type` (`app` / `youtube` / `book`, mặc định `app`) |
| `lib/projects.ts` · `CollectButton.tsx` | đặt loại lúc tạo, hỏi khi gom khác loại |
| `client/ProjectPage.tsx` | đầu trang mới, thanh 4 chặng thay `Tabs`, đổi `?tab=` cũ sang chặng |
| `components/ProjectHeader.tsx` · `StageBar.tsx` (mới) | đầu trang + thanh chặng, hàm tính “chặng xong” thuần + test |
| `components/DecisionBoard.tsx` | thẻ gọn, gom công cụ AI vào 1 nút |
| `components/BuildTab.tsx` | thành chặng ③, chạy cả project không phải phiên AI Agent |
| `client/HuntPage.tsx` · `HuntIndexPage.tsx` · menu trái | chuyển hướng `/hunt/:id`, 4 cách tạo ở trang Projects |
| `client/ProjectsPage.tsx` | icon loại + chip lọc + chấm chặng mỗi dòng |
| `web/tests/` | hàm chặng xong, đổi link `?tab=` cũ, đoán loại lúc tạo, chuyển hướng `/hunt/:id`, tài liệu cho project thường |

## Không làm ở mục này

- Nút gom từ YouTube, bàn chấm riêng cho YouTube / Sách → **16.6** (chưa spec).
- Chấm đối thủ nên bắt chước, trang Soi 1 app → **mục 14**, cắm vào chặng ③ sau.
- Không đổi cách chấm điểm, không thêm trục mới, không bịa số.

## Soát khi xong (mỗi bước)

- `npm run check` xanh, `npm run docs:build` xanh.
- Mở 1 project App thật (“draw for kids · US”) và 1 project rỗng ở 960px và 1340px, sáng + tối, English + tiếng Việt.
- Tên project dài không đẩy nút ra khỏi hàng, thanh chặng không cuộn ngang ở 960px.
