# niche-radar — Phase 8: Local App (project · export · app Mac)

> Ngày: 2026-10-24 · Trạng thái: **code xong 2026-10-25** (spec duyệt 2026-10-24) (bước 📄 của [Quy trình build](../../quy-trinh-build.md)).
> Làm **sau Phase 7** (anh chốt 2026-10-24: app trên máy; lộ trình 11 phase đổi số từ Phase 6 → Phase 8, macOS trước, Tauri + Rust). Plan code + mockup viết khi tới phase này.
> Đầu vào: đề xuất "Với app local, nên thiết kế thế nào?" (local-first, 4 khối: Local Research App · Local database ·
> Data collectors · Exportable research projects).

## 0. Một câu

Biến niche-radar từ "web chạy bằng `npm run dev`" thành **app Mac bấm là mở**, gom kết quả tra thành **project**
có ghi chú + đánh giá, và **xuất/nhập được** để backup, chuyển máy, gửi cho người khác — mà không xây server.

## 1. Đánh giá đề xuất

### 1.1 Kết luận

**Đồng ý local-first, giữ 4 khối.** Nhưng sửa một chỗ trong lý do: câu "tránh thiết kế khiến sau này muốn bán phải
viết lại" — với tool này, dạng **bán được rẻ nhất không phải SaaS** mà là **app desktop + license key** (như RAM Rescue):

- Play, Trends, Google suggest là nguồn **không chính thức** — chạy trên server chung thì IP datacenter bị chặn nhanh,
  phải trả proxy dân cư / SerpApi / DataForSEO theo lượt ([giới hạn nguồn](2026-10-24-niche-radar-limits-and-sharing.md) §1).
- Chạy trên máy người dùng → mỗi người IP nhà riêng, giới hạn riêng, **mình không tốn đồng nào cho dữ liệu**.

Nên "không phải viết lại khi bán" = **đóng gói được thành app + dữ liệu chuyển được giữa các máy**, chứ không phải chuẩn
bị multi-tenant (nhiều khách chung một server). Phase này làm đúng phần đó và dừng ở đó.

### 1.2 Từng khối: đề xuất · đã có · thiếu · quyết định

| Khối | Đề xuất | niche-radar đã có (2026-10-24) | Thiếu | Quyết định Phase 8 |
|---|---|---|---|---|
| **Local Research App** | giao diện desktop cho team tìm, lọc, đánh giá cơ hội | Web React ở `localhost:3200`; tìm (run, explore), lọc/sắp bảng keyword, bản đồ ngách | không mở được nếu không có Node + terminal · chưa có chỗ **đánh giá** (ghi chú, kết luận) · "team" chưa có cách nhận dữ liệu của nhau | Bọc **Tauri** (đã chốt, không Electron) · thêm Project + đánh giá · chuyển máy bằng **file**, không bằng server |
| **Local database** | SQLite: project, keyword, app, review, snapshot, score | SQLite + Drizzle: `runs`, `explorations`, `explore_nodes`, `keywords`, `apps`, `app_snapshots`, `node_metrics` (điểm phổ biến), `review_cache` | **không có `project`** · ID số tự tăng → **đụng nhau khi nhập từ máy khác** · review chỉ là cache JSON (Phase 6 cần từng dòng để trích dẫn) · điểm không lưu nguồn/độ tin · không có `schema_version` | Thêm `projects` + `project_items` + ghi chú/kết luận · **đổi khoá sang ULID** (chuỗi duy nhất toàn cầu) · `meta.schema_version` · review dạng dòng + bảng điểm **để Phase 6–7** (không làm sớm) |
| **Data collectors** | Store metadata, review, Trends, nguồn ngoài | Play, App Store, Google suggest, Trends, Reddit; rate limit, timeout, cache 24h/7 ngày, `source_jobs` báo lỗi từng nguồn | không ghi **bản collector** nào lấy dữ liệu (Play scraper gãy → không biết dữ liệu cũ đáng tin tới đâu) | Giữ nguyên · thêm `collector_version` vào `source_jobs` · TrustMRR đã có từ Phase 5 |
| **Exportable projects** | JSON/CSV/Markdown, backup, chia sẻ báo cáo, chuyển máy | CSV của trang explore | không có xuất/nhập project · không backup · không báo cáo `.md` | **Gói project `.json`** (nhập lại được, có version) · CSV từng bảng · báo cáo `.md` (dùng lại evidence pack của Phase 7) · **backup/restore cả DB** |

### 1.3 Ba quyết định thiết kế quan trọng nhất (rẻ bây giờ, đắt về sau)

1. **ULID thay ID số.** Hai máy cùng có `run #12` → nhập vào là đè nhau. ULID (`01JB…`, sắp theo thời gian) cho mỗi dòng
   một tên không trùng ở bất kỳ máy nào → nhập file là ghép thẳng, nhập 2 lần không nhân đôi. Lúc này DB mới có
   **11 run · 6 explore · 664 app** (2026-10-24). Tới Phase 8 sẽ thêm bảng của Phase 2–7 → migration lớn hơn; giảm bằng
   luật nhỏ ở §4 (bảng mới dùng ULID ngay).
2. **UI chỉ nói chuyện với API qua HTTP** (đang vậy, giữ nguyên). App Mac = cùng UI + cùng server Node chạy kèm.
   Sau này muốn host thì UI không phải sửa. Không viết lại bằng Rust, không gọi DB thẳng từ UI.
3. **Đường dẫn dữ liệu là một cấu hình** (`NR_DATA_DIR`): web dev giữ `data/`, app Mac dùng
   `~/Library/Application Support/niche-radar/`. Mọi chỗ đang ghi cứng `data/niche.db` gom về một hàm.

### 1.4 Không làm (dù nghe hợp lý với "sau này bán")

| Không làm | Vì sao | Khi nào xét lại |
|---|---|---|
| Postgres, đăng nhập, cột `workspace_id`/`user_id` | tool nội bộ một người dùng; thêm cột sau bằng migration là xong | khi Idea Lab qua test bán trước **và** chọn hướng host |
| Đồng bộ cloud / realtime giữa các máy | file export đủ cho 1–3 người; sync là một sản phẩm khác | khi có ≥ 3 người dùng thật than chuyện gửi file |
| License key, trial, thanh toán | chưa có quyết định bán | Idea Lab qua test → plan riêng (dùng lại mẫu Lemon Squeezy của RAM Rescue) |
| Auto-update (Tauri updater) | 1–3 người dùng, tải `.dmg` mới là đủ | khi có người ngoài dùng |
| Bản Windows | anh chỉ dùng Mac (§6) | khi có người dùng Windows thật |
| Lưu nguyên response thô của từng nguồn | DB phình nhanh; dữ liệu đã chuẩn hoá đủ dùng | khi cần chấm lại điểm mà không tra lại |

## 2. Mục tiêu · làm · không làm · xong khi

- **Mục tiêu:** anh (và người anh đưa file) **mở app bằng double-click**, gom tra cứu thành project, ghi đánh giá,
  xuất/nhập project giữa các máy — không cần Node, không cần terminal.
- **Làm:** 6 việc L0–L5 ở §3.
- **Không làm:** §1.4 · không thêm tính năng tra cứu / chấm điểm mới (đã xong ở Phase 1–7).
- **Xong khi** (đo được, ghi số + ngày vào §5 khi test):
  1. Trên **một tài khoản macOS mới chưa cài Node**: mở `.dmg` → kéo vào Applications → bấm icon → app mở, tra được
     1 keyword ra dashboard. Gatekeeper không cảnh báo (`spctl -a -vv` = `accepted`, `source=Notarized Developer ID`).
  2. Mở app tới khi bấm được: **≤ 5 giây** (đo 3 lần, lấy trung vị). RAM lúc nghỉ (app + Node sidecar): ghi số đo,
     mục tiêu **≤ 300 MB**.
  3. Xuất project A ở máy/tài khoản 1 → nhập ở tài khoản 2 (DB rỗng) → số keyword, app, snapshot, ghi chú **bằng nhau**.
     Nhập lại lần 2 → **không nhân đôi**.
  4. Backup → xoá DB → restore → số run/explore/project bằng trước.
  5. DB thật lúc bắt đầu Phase 8 **lên ULID không mất dòng nào** (đếm trước/sau từng bảng).
  6. `npm test && npm run typecheck && npm run lint` xanh; `npm run dev` (web) vẫn chạy như cũ.

## 3. Việc cần làm

| # | Việc | Ra | Ước lượng* |
|---|---|---|---|
| **L0** | **Spike đóng gói** (làm đầu tiên, giới hạn 1 ngày): Tauri + Node sidecar có `better-sqlite3` (module native) + `google-play-scraper`, ký + notarize, chạy trên tài khoản macOS mới | ghi kết quả vào §5 · chọn phương án | 1 ngày |
| L1 | **Nền dữ liệu**: ULID cho mọi bảng có khoá riêng · bảng `meta(schema_version)` · `NR_DATA_DIR` · **tự backup DB trước mỗi migration** · script chuyển DB cũ · `collector_version` ở `source_jobs` | migration Drizzle + test đếm dòng | 1–2 ngày |
| L2 | **Project + đánh giá**: bảng `projects` (tên, mô tả, trạng thái `đang xem / ứng viên / loại`, lý do, ngày) · `project_items` (gắn run / explore vào project) · `notes` (ghi chú tự do theo project / keyword / app) · trang **Projects** (danh sách, lọc theo trạng thái) + trang **Project** (các run/explore đã gắn, ghi chú, kết luận) · nút "Thêm vào project" trên trang run/explore | 2 màn mới + API | 1–2 ngày |
| L3 | **Xuất / nhập / backup**: gói project `.niche.json` (`format`, `schema_version`, `exported_at`, `app_version`, dữ liệu theo ULID) · nhập = upsert theo ULID, báo "thêm X · bỏ qua Y · lỗi Z" · CSV từng bảng (keyword, đối thủ, explore) · báo cáo `.md` (khung tối giản: niche, top keyword + điểm, top đối thủ, câu than, ghi chú, nguồn + ngày) · backup cả DB (`VACUUM INTO`) + restore | file mẫu trong `web/tests/fixtures/` | 2 ngày |
| L4 | **App Mac (Tauri)**: sidecar Node, cổng ngẫu nhiên + **token mỗi lần mở** (chặn trang web khác gọi API local) · dữ liệu ở Application Support · trang **Cài đặt** (key Reddit / TrustMRR — thay `.env.local`; nút mở thư mục dữ liệu, nút backup) · icon (Codex sinh) · ký Developer ID + notarize · `.dmg` | `.dmg` đã notarize | 2–3 ngày |
| L5 | **Test** theo "Xong khi" §2 + dùng thật 3 niche trong app | số đo + screenshot ở §5 | 1 ngày |

\* Ước lượng của Claude, chưa đo — ghi lệch vào plan code khi làm.

### L0 — các phương án đóng gói phải thử

| Phương án | Cách | Được | Rủi ro |
|---|---|---|---|
| **A (thử trước)** | Kèm binary `node` chính chủ (arm64) + server bundle bằng esbuild + file `.node` của better-sqlite3 build sẵn cho arm64 | ít đổi code nhất, chắc chạy | app nặng (~100 MB); phải ký từng binary bên trong khi notarize |
| B | Node SEA (single executable application) gói server thành 1 file | gọn hơn | module native (`better-sqlite3`) khó nhét vào SEA |
| C | Đổi `better-sqlite3` → `node:sqlite` có sẵn trong Node (bỏ module native) | hết rủi ro native | phải kiểm Drizzle có hỗ trợ không; API còn đánh dấu experimental tuỳ bản Node |

Spike **thất bại** (cả A–C không notarize được hoặc không chạy trên tài khoản mới trong 1 ngày) → dừng L4, vẫn làm
L1–L3 (dùng được ngay trên web), ghi chỗ kẹt vào §4 Master Plan và hỏi anh trước khi đổi hướng.

### Màn mới cần mockup (bước 🎨, Codex sinh)

Projects (danh sách + lọc trạng thái) · Project (chi tiết + ghi chú + kết luận) · hộp Xuất / Nhập (kèm kết quả
"thêm X · bỏ qua Y") · Cài đặt. Prompt ở `design/mockups/phase6/image-prompts.md`, ảnh cùng thư mục.

## 4. Thứ tự với các phase khác

```
Phase 1 ─► … ─► Phase 7 Review + Validate ─► Phase 8 Local App ─► Phase 9 … 11
                                                       L0 spike → L1 → L2 → L3 → L4 → L5
```

- Làm **sau Phase 7** (anh chốt 2026-10-24). Phase 1–7 vẫn chạy bản web `npm run dev`.
- **Đề xuất luật nhỏ cho Phase 3–7** (anh chốt khi viết plan code Phase 3; Phase 2 đã code bảng mới bằng ID số): bảng **mới** dùng khoá ULID ngay từ đầu — vài dòng
  code mỗi bảng, đỡ phải chuyển khoá cho chúng ở L1. Bảng cũ để nguyên tới Phase 8.
- Báo cáo `.md` của L3 dùng lại evidence pack của Phase 7 (không viết khung mới).
- Nhánh `phase8-local-app` cắt từ `main` khi Phase 7 đã merge.
- Master Plan §1 / §7: "App Mac" chuyển từ Appendix vào Phase 8.

## 5. Kết quả test (điền khi làm)

| Hạng mục "Xong khi" | Số đo | Ngày | Ghi chú |
|---|---|---|---|
| L0 spike — phương án chọn | **A** chạy: Node chính chủ v22.19 (arm64, chỉ dùng thư viện hệ thống) + server gói bằng esbuild + prebuild `better-sqlite3` darwin-arm64 | 2026-10-25 | `.app` 119 MB · `.dmg` 45 MB · `app/scripts/build-mac.sh` |
| 1. Mở trên tài khoản mới, Gatekeeper | `spctl`: `accepted · source=Notarized Developer ID` (cả .dmg và .app chép ra từ .dmg) · chạy với `env -i PATH=/usr/bin:/bin` (không có Node của máy): mở + tra "water reminder" từ DB trống xong 3/3 nguồn trong 46 giây · gọi API không token → 403 | 2026-10-25 | **chưa thử trên tài khoản macOS mới** — cần anh tạo tài khoản (Claude không tạo tài khoản máy) |
| 2. Thời gian mở · RAM nghỉ | server sẵn sàng sau 162 / 143 / 135 ms (trung vị 143 ms) · RAM: vỏ app ~107 MB + Node ~91 MB ≈ **200 MB** (chưa tính tiến trình WebKit của macOS) | 2026-10-25 | đạt ≤ 5 s · ≤ 300 MB |
| 3. Xuất → nhập, nhập lại không nhân đôi | test: DB rỗng nhập đủ 11 bảng bằng số dòng; nhập lần 2 thêm 0. Dữ liệu thật: gói 304 KB (3 run · 202 app) nhập lại → bỏ qua hết | 2026-10-25 | `web/tests/portable.test.ts` |
| 4. Backup → restore | test + server thật: xoá 1 project → restore → 19 run · 12 explore · 2 project như trước; bản trước restore tự backup | 2026-10-25 | restore chỉ nhận file trong `backups/` |
| 5. DB cũ lên ULID không mất dòng | bản sao DB thật: 30 bảng · 22 run · 12 explore · 1.220 app, schema 12 → 13, mất 0 dòng, mọi dòng có ULID, có backup trước migrate | 2026-10-25 | |
| 6. test · typecheck · lint · web dev | 214 test xanh · typecheck · lint sạch · `npm run dev` chạy | 2026-10-25 | |

Lỗi tìm ra khi chạy thật: app bị kill (không Cmd+Q) để lại server Node chạy mồ côi → server đọc stdin, app mất thì tự tắt
(đã kiểm bằng `kill -9`: 1 → 0 tiến trình).

## 6. Đã chốt (anh, 2026-10-24)

1. **Người dùng:** chỉ anh, chỉ **Mac** — không làm bản Windows, không cần chia sẻ cho team (xuất/nhập dùng để backup + chuyển máy).
2. **Thứ tự:** Phase 8, sau Phase 7.
3. **Ký:** Developer ID Application: Tu Nguyen (ASF7S2CGR3) đang dùng cho app Mac khác; notarize bằng profile notarytool có sẵn trên máy.
