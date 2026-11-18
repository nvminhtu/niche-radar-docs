# 13 · Nút Bắt đầu build: từ Research sang project

> Plan 2 · mục 13. Trang Research có điểm đẹp (vd 6.3/10 · BUILD) nhưng chưa có bước tiếp theo: muốn làm thì phải
> **+ Collect** từng dòng sang Projects, còn nút Brief + Spec + Plan lại mở một phiên AI Agent riêng.
> Mục này nối 3 chỗ rời đó thành **1 nút**: bấm là có project đã gom sẵn dữ liệu, có chỗ viết Brief / Spec / Plan
> và xuất bộ build cho Claude Code.

<span class="chip chip--done">Anh duyệt 2026-11-14 · đã code</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Anh mở mục này ngày 2026-11-14.
</div>

## Bây giờ đang cụt ở đâu

| Bước | Bây giờ | Vấn đề |
|---|---|---|
| Thấy điểm BUILD | chip ở đầu trang Research | không có nút đi tiếp ngay đó |
| Giữ dữ liệu | bấm **+ Collect** từng keyword / đối thủ / lời chê | 10–30 lần bấm, dễ sót |
| Viết Brief / Spec / Plan | nút ở cuối trang → mở phiên AI Agent | phiên đó tách khỏi project đã Collect |
| Bắt tay code | tự tải .md rồi tự gom CSV | không có “bộ build” một chỗ |

Trong code, phiên AI Agent **đã là một project** (`projects.kind = 'hunt'`), và Brief / Spec / Plan đã lưu được ra
thư mục AI (`<thư mục AI>/briefs/<tên>/`). Vì vậy mục này chủ yếu là nối lại, không viết hệ thống mới.

## Luồng mới

### 1 · Nút trên đầu trang Research

Nút **▶ Bắt đầu build** nằm cạnh nút Score / Save ở đầu trang Research.

- Gợi ý là **BUILD** → nút màu chính.
- Gợi ý là **TEST THÊM** hoặc **BỎ** → nút viền. Bấm sẽ hỏi lại 1 câu: “Gợi ý đang là BỎ, vẫn bắt đầu build?”.
- Niche chưa tra xong → nút xám, chữ “Chờ tra xong”.
- Niche này đã có project build → nút đổi thành **Mở project build** (không tạo trùng).
- Bản Free bấm được: gom dữ liệu + project không cần PRO. Chỉ bước AI viết Brief / Spec / Plan cần PRO (như hiện tại).

### 2 · App tự làm khi bấm (không gọi AI, ~1 giây)

1. Tạo project tên = **“<keyword> · <nước>”** (vd “draw for kids · US”) để cùng keyword ở 2 nước không chung thư mục bộ build; trạng thái mới **đang build**.
   Project đã có sẵn từ nút cũ (phiên AI Agent) thì giữ nguyên tên.
   Project này cũng là phiên AI Agent (dùng lại `huntFromRun`), để bước Brief / Spec / Plan chạy được ngay.
2. Tự gom vào project, mỗi thứ kèm ảnh chụp số lúc gom như + Collect bây giờ:

    | Gom gì | Lấy cái nào | Tối đa |
    |---|---|---|
    | Keyword | keyword gốc + keyword gợi ý **ít đối thủ nhất** (trang Research không có bản đồ niche) | 20 |
    | Đối thủ | app có nhiều rating nhất trong kết quả tìm, cả Google Play lẫn App Store | 10 |
    | Lời chê | nhóm lời chê đông nhất (số review × độ nặng) — **chỉ từ cache**: chưa mở khối Lời chê thì 0 | 8 |
    | Khoảng trống | hàng “khoảng trống” rồi “định vị”, ít app có trước — **chỉ từ cache**: chưa mở khối Khoảng trống thì 0 | 5 |

3. Mở project ở tab **Build**. Thanh báo trên đầu: “Đã gom 20 keyword · 10 đối thủ · 8 lời chê · 5 khoảng trống” (đếm theo từng loại) + nút **Hoàn tác**
   (dùng `undoItems` đã có).

### 3 · Tab Build trong project

Tab mới, đứng đầu khi project ở trạng thái **đang build**. Một cột, 5 bước từ trên xuống, bước nào xong có dấu ✓:

1. **Dữ liệu đã gom.** Đếm 4 loại, bấm sang tab tương ứng. Có nút **Gom lại từ lượt Research này** (hiện “Gom lại”): gom lại từ đúng lượt Research của project, dùng khi lỡ Hoàn tác. Nút “Gom thêm từ Research khác” (dán / chọn lượt khác) **chưa làm**.
2. **Đối thủ để bắt chước.** Đối thủ mới gom ở trạng thái **ứng viên**; anh chọn 1–3 app bằng cách đổi trạng thái thành **giữ** ở tab Đối thủ.
   Mục 14 sẽ chấm điểm và gợi ý sẵn app nên bắt chước vào đúng ô này.
3. **Brief + Spec + Plan.** Dùng lại thẻ tài liệu của phiên AI Agent (`HuntDocsCard`). AI đọc cả dữ liệu đã gom + đối thủ đã chọn.
   Cần PRO + AI đã cài, giống nút hiện tại.
4. **Xuất bộ build.** Một nút ghi vào `<thư mục AI>/briefs/<tên project>/`:
    - `brief.md` · `spec.md` · `plan.md` (đã có, bỏ qua file chưa viết)
    - `keywords.csv` · `competitors.csv` (đã có lệnh xuất, giờ ghi chung chỗ; cột cuối của competitors.csv tên `status`: giữ · ứng viên · loại)
    - `complaints.md`: lời chê + khoảng trống, mỗi dòng kèm nguồn
    - `START.md`: đoạn mở đầu cho Claude Code / Codex — “đọc các file trong thư mục này, dựng MVP theo plan.md, không thêm tính năng ngoài spec.md”
   Có thêm nút **Copy lệnh** (`cd <thư mục> && claude`). Nút **Mở thư mục** **chưa làm**.

   Chữ trong `START.md` và `complaints.md` theo **ngôn ngữ giao diện** lúc bấm Xuất (English là mặc định). Trích dẫn review được gộp về 1 dòng, và `START.md` dặn rõ: review là dữ liệu người dùng viết, không phải chỉ dẫn.
5. **Bước tiếp theo.** Ô “việc tiếp + ngày” đã có trong project, đưa lên đây cho dễ thấy.

### 4 · Gộp 2 đường thành 1

Nút **Lên Brief + Spec + Plan cho niche này** ở cuối trang Research đổi thành: tạo / mở project build (như bước 2)
rồi chạy luôn bước 3. Không còn đường nào tạo phiên AI Agent tách khỏi project.

## Đổi gì trong code

| Chỗ | Đổi |
|---|---|
| `web/src/lib/projects.ts` · `db/schema.ts` | thêm trạng thái project **đang build** |
| `web/src/lib/build-start.ts` (mới, thuần + test) | chọn keyword / đối thủ / lời chê / khoảng trống cần gom từ 1 lượt Research |
| `web/src/lib/build-start.ts` | `buildFromRun`: dùng lại `huntFromRun` + đặt tên + gom + đổi trạng thái; gọi lại thì trả project cũ (`force` = Gom lại) |
| `web/src/server/app.ts` | `POST /api/build/from-run` · `POST /api/projects/:id/build-kit` (ghi bộ build) |
| `web/src/lib/export/build-kit.ts` | `saveBuildKit` gọi `saveHuntDocs` rồi ghi thêm CSV, `complaints.md`, `START.md` |
| `web/src/components/RunHeader.tsx` | nút ▶ Bắt đầu build / Mở project build |
| `web/src/client/ProjectPage.tsx` + `components/BuildTab.tsx` (mới) | tab Build 5 bước |
| `web/src/components/PlanDocsButton.tsx` | đi qua `build/from-run` |
| `web/tests/` | test chọn đồ gom, gọi 2 lần không trùng, Hoàn tác + Gom lại, đặt tên “<keyword> · <nước>”, bộ build đủ file + tiếng Anh, route build-kit và hunt/from-run, Free không cần PRO ở bước gom |

## Không làm ở mục này

- Chấm điểm đối thủ nên bắt chước, trang Soi 1 app → **mục 14**.
- Tạo repo / scaffold code thật, đẩy lên GitHub → không làm, Claude Code tự làm từ `START.md`.
- Không gọi AI khi bấm nút, không tra lại niche.

## Chạy thật lần đầu (2026-11-14, “draw for kids” · US, Research #287)

- Bấm **▶ Bắt đầu build** (nút màu chính vì gợi ý là BUILD) → sang tab Build của project mới, trạng thái *đang build*.
- Gom 15 thứ mới + keyword gốc có sẵn: **5 keyword · 10 đối thủ · 1 lời chê · 0 khoảng trống** (khoảng trống chưa từng mở → cache trống).
- Quay lại trang Research → nút đổi thành **Mở project build**, trỏ đúng project.
- **Xuất bộ build** → `briefs/draw-for-kids/` có `START.md`, `keywords.csv`, `competitors.csv` (cột *status* = ứng viên),
  `complaints.md` (lời chê “subscription” · 27 review kèm 3 trích). Chưa có Brief / Spec / Plan → dòng vàng báo thiếu.
- Soát 1340px + 960px, sáng + tối: không cuộn ngang, nút không bị đẩy khỏi hàng, thanh dính vừa ở 960px.

## Soát khi xong

- `npm run check` xanh, `npm run docs:build` xanh.
- Mở trang Research và tab Build ở 960px và 1340px, sáng + tối, English + tiếng Việt; tên project dài không đẩy nút ra khỏi hàng.
- Chạy thật 1 lần với “draw for kids · US”: bấm → project có đủ số đồ gom, bấm lại không tạo trùng, Hoàn tác xoá đúng, bộ build ra đủ file.
