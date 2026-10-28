# Phase 28.8 · Trang niche + Explorer: điểm dễ đọc, TEST MORE bấm được, sửa cuộn, chữ trạng thái rỗng

> Sửa bảng và cây bị cắt trước; biến trạng thái rỗng thành bước đi tiếp; đọc được điểm và giới hạn dữ liệu ngay,
> rồi bấm gợi ý để biết cần đo, test hay research thêm điều gì.

<span class="chip chip--done">Xong 2026-10-28 · D · E · B · C · A</span>

<div class="box box--goal" markdown>
**Hiện có — đối chiếu code ngày 2026-10-27.**

- `web/src/components/HealthBlock.tsx`: “Key verdict” / “Niche health — opportunity score v2” nằm trên câu giải thích
  7 yếu tố. Điểm, coverage, solid và v1 đứng chung một ô; “suggests…” là `span`, không có hành động.
  `s.summary` và ngưỡng hiển thị đầy đủ; từng yếu tố đã có `details` chứa công thức, đầu vào và nguồn.
- `web/src/lib/score-v2.ts`: tổng chỉ tính yếu tố có giá trị, theo trọng số; `coverage` là tỷ lệ trọng số đã có điểm
  (gồm proxy), `solid` gồm mức “đo” **và “tự chấm”**. Đây không phải tỷ lệ chắc chắn niche thành công.
  `decision` đã áp ngưỡng, độ phủ và cờ chặn; UI không được tự suy quyết định từ màu điểm.
- API health đã trả `next`, `capped`, `flags`. Khối “Cần đo thêm gì”, form “Tự chấm 2 trục”, nháp AI và bảng test bán
  trước trong `HealthBlock.tsx` đang bị comment. `next` của reach/fit còn chỉ về form đã ẩn: không thể chỉ bật lại
  danh sách cũ rồi coi mọi bước đã bấm được.
- `web/src/components/ExploreDashboard.tsx`: cây trái `h-[700px] overflow-auto`, grid dùng breakpoint màn hình
  `lg:grid-cols-[300px_minmax(0,1fr)]`; khung bảng cũng `h-[700px]`, vùng bảng con `h-[480px] overflow-auto`.
  Header có nội dung co giãn, Collect và SourceLegend. `Tabs.tsx` thêm tablist; `.tab-panel` trong `globals.css`
  thêm padding trên 20px. Tổng chiều cao con không bị ràng buộc theo phần còn lại của khung cha.
- Bảng có nhiều hơn 5 cột nhưng chưa `table-fixed`, chưa ghim cột đầu; ô keyword `min-w-56`, chữ và nút cùng một
  hàng flex thiếu ràng buộc co. Header `sticky top-0 z-10` chỉ ghim dọc. Cây thụt lề mỗi tầng, dành chỗ cho Collect
  và “Go deeper”; nhãn có `truncate` + `title`, nên “pomodor…” là cắt có chủ ý nhưng vùng đọc bị ép quá hẹp.
- `web/src/components/FlowMap.tsx`: rỗng nhánh khi `tree.length === 1`, rỗng ghim khi `flows.length === 0`;
  cả hai chỉ là đoạn chữ. Component chưa nhận callback mở rộng. `flow-path.ts` chỉ đưa node đã đi vào `tree`,
  nên không thể lấy “keyword top” từ riêng cây này; phải dùng danh sách node đầy đủ ở Explorer.
- `FlowMap` còn cuộn ngang cây; `.flow-steps ol` và `.ui-tabs` cũng cuộn ngang. `globals.css` đã có
  `html { scrollbar-gutter: stable; }`, nhưng chưa bảo vệ riêng hàng cuối của vùng bảng khỏi thanh cuộn phủ.
- Trạng thái rỗng khác đã thấy: chưa research sâu, cây chưa keyword, bộ lọc không khớp, nguồn chưa xác nhận keyword
  trong `ExploreDashboard`; chưa đủ điểm vẽ map và chưa có Top cơ hội trong `NicheMap.tsx`.
  Trang niche ở `RunDashboard.tsx` dùng `SourceBlock` cho Trends/đối thủ, có callback retry;
  `HealthBlock` lại trả `null` khi chưa tải được health, kể cả lúc lỗi tải.
- Chữ EN nằm ở `web/src/locales/en-text.ts`, `en-text-sweep.ts`; VI là khoá qua `tr`/`tx`.
  Các con số người dùng nêu trong ảnh là ví dụ hiển thị, không phải phép đo mới của plan này.
</div>

**Cần xong trước:** dùng nền Explorer/FLOW và sức khoẻ của [Phase 20](phase-20-niche-health.md),
trang kết quả [Phase 23](phase-23-research-page.md).
D/E/B/C làm độc lập, không phải đợi AI. Nhánh giao AI của A dùng [Phase 28.6](phase-28-6-ai-agent.md)
và hợp đồng xem/sửa trước gửi ở [Phase 28.7](phase-28-7-ai-agent-ux.md).
Test bán trước phụ thuộc [Phase 43](phase-43-evidence-presell.md); Brief/Spec phụ thuộc
[Phase 28.5](phase-28-5-brief-plan.md). Plan không coi các trang kế hoạch này là tính năng đã hoạt động.

## Mục tiêu · cần làm · KHÔNG làm

- **Mục tiêu:** không chồng khối, không kẹt ở trạng thái rỗng; hiểu điểm và biết hành động kế tiếp có căn cứ.
- **Cần làm:** D sửa cuộn **GẤP** → E trạng thái rỗng **GẤP** → B thu gọn giải thích → C trình bày điểm → A CTA verdict.
- **KHÔNG làm:** đổi công thức, trọng số, ngưỡng, collector, schema dữ liệu, tự quyết định BUILD/BỎ, tự gửi AI,
  tự đăng test bán trước hoặc triển khai toàn bộ Phase 43. Lượt hiện tại chỉ viết tài liệu, không sửa code.
- Mọi khối chữ trong tài liệu, menu bước tiếp và trạng thái rỗng xếp một cột dọc; không lưới thẻ chữ hẹp.
- Bề rộng UI phải đứng được từ **960px tới 1920px**; chỉ bảng cuộn ngang, toàn trang không cuộn ngang.
  Con chứa chữ `min-w-0`; nút/icon/số `shrink-0`; grid dùng `minmax(0,1fr)`; thay đổi theo khung chứa bằng
  `@container`. Chữ một dòng `truncate` + `title`, mô tả `line-clamp-2`, URL/id `wrap-anywhere`.

## D · Sửa cuộn bảng và cây Explorer — GẤP · M

**Mục tiêu:** hàng cuối đọc và bấm đủ; Niche map luôn ở dưới bảng; cây vẫn nhận ra keyword đang chọn.

**Cần làm**

- Chẩn đoán từ code: khung cha 700px không tự lớn theo header + tabs + padding + bảng 480px; overflow mặc định
  của section cho phép con vẽ ra ngoài, trong khi Niche map được xếp sau chiều cao cha. Đây là nguyên nhân cấu trúc
  có thể gây chồng khối khi header xuống dòng. Mức che hàng cuối do scrollbar overlay cần tái hiện trên trình duyệt;
  chưa có đo hình học hay screenshot xác nhận trong lượt viết plan, không quy toàn bộ lỗi cho `sticky`.
- Chọn khung ngoài **cao tự nhiên**, bỏ hai ràng buộc cao 700px; chỉ vùng bảng có giới hạn chiều cao tối đa và
  cuộn dọc khi nhiều hàng. Giữ một vùng cuộn bảng `overflow-x-auto` với `overflow-y-auto`, không lồng hai scrollbar
  cạnh nhau; padding cuối nội dung dành chỗ cho scrollbar overlay, gutter ổn định cho scrollbar chiếm chỗ.
  Chốt khoảng đệm sau kiểm thực tế, không coi gutter trên html đã giải quyết bảng.
- Bảng dùng `table-fixed`, `colgroup` định nghĩa độ rộng cho từng cột kể cả Trends có điều kiện; đặt min-width tổng
  trong vùng cuộn. Ghim cột đầu checkbox `sticky left-0` có nền; ghim thêm keyword với offset từ độ rộng checkbox
  để vẫn biết đang thao tác dòng nào. Giao điểm header/cột ghim có z-index và nền riêng, giữ màu hover/selected.
  Cột số `text-right whitespace-nowrap`; keyword `min-w-0`, nhãn truncate/title, Pin/Collect/icon không co mất.
- Cây theo container: khung hẹp xếp trên bảng, thao tác sang dòng riêng khi cần; khung đủ rộng mới đặt cạnh bảng.
  Giới hạn thụt lề sâu, vẫn chỉ rõ quan hệ cha/con; không nới keyword vô hạn, giữ tooltip/title toàn bộ keyword.
  Có nhãn đầy đủ truy cập được bằng bàn phím, không chỉ rê chuột.
- Trong phạm vi Explorer, cho tabs/flow steps xuống dòng và Branch map chuyển cây dọc khi hẹp thay vì cuộn ngang
  ngoài bảng. Dùng class/variant cục bộ, không đổi mọi Tabs toàn hệ thống. Sửa cả header seed dài và thanh chọn
  keyword dưới đáy: không để nhiều chip làm thanh fixed che hàng cuối; ưu tiên thanh thao tác trong luồng tài liệu
  hoặc dành khoảng trống theo chiều cao thực, không dựa vào `pb-20` cố định.

**KHÔNG làm:** tăng 700px thành một số cố định khác, che lỗi bằng `overflow-hidden` toàn trang, bỏ cột dữ liệu,
đổi sort/filter/selection hoặc xoá Niche map.

**Tiêu chí kiểm được:** tại 960/1340/1920px, EN/VI, keyword dài và đủ cột, header xuống dòng vẫn không chồng map;
cuộn đến cuối bảng và sang phải thấy, bấm được checkbox/Pin/Collect hàng cuối; cột ghim không che dữ liệu khác.
Kiểm chiều cao cửa sổ thấp và zoom 125–150%, scrollbar chiếm chỗ lẫn overlay; toàn trang và cây không cuộn ngang.

**File đụng:** `web/src/components/ExploreDashboard.tsx`, `Tabs.tsx`, `FlowMap.tsx`, `FlowSteps.tsx`,
`web/src/client/globals.css`; `ExploreShared.tsx` nếu cell số cần ràng buộc; locale nếu thêm nhãn truy cập.

**Test `web/tests/`:** giữ xanh `explore-view.test.ts` (sort/filter/null), `flow-path.test.ts`;
thêm `explore-layout.test.ts` cho markup render bằng React server: nhãn đầy đủ, trạng thái selected, cột Trends.
Bộ hiện tại là Vitest, chưa có browser runner trong package: test markup **không chứng minh layout**.
Bắt buộc kiểm trình duyệt với bounding boxes: đáy khung bảng không vượt đầu map, document không overflow ngang;
chụp và đọc ảnh hàng cuối ở ma trận trên, kèm thao tác thực. Không dùng test grep class để tuyên bố sửa xong.

**Độ lớn:** M — CSS và cấu trúc khung, cần kiểm nhiều trạng thái cuộn.

## E · Trạng thái rỗng có lợi ích và hành động — GẤP · M

**Mục tiêu:** người dùng hiểu sẽ được gì và bấm ngay bước hợp lệ tại chỗ.

**Cần làm**

- Một khối một cột: câu lợi ích, keyword mục tiêu, nút chính; mô tả lỗi/đang chạy riêng. Dùng icon sẵn có nếu hữu ích,
  không cần sinh minh hoạ mới. Nút mang động từ, focus rõ, thông báo kết quả bằng vùng status.
- Tạo helper `web/src/lib/explore-next-action.ts` nhận nodes đầy đủ, danh sách đã ghim và trạng thái chạy.
  Với mở nhánh: loại root và node đạt `MAX_DEPTH`; với ghim: loại root, node đã ghim và node có con (đề xuất lá).
  Ưu tiên điểm opportunity có dữ liệu cao nhất, hoà điểm theo ID tăng dần để ổn định; không coi null là 0.
  Chưa có điểm thì không gọi “top”; dùng keyword đang chọn hợp lệ hoặc đưa về bảng chọn.
  Điểm v1 chỉ là tiêu chí xếp gợi ý, không chứng minh keyword đủ cụ thể về mặt thị trường.
- Truyền target và `onExpand` từ ExploreDashboard sang FlowMap; dùng `action('expand', [id])` và
  `post('flows', { nodeId })` hiện có. Nhấn ghim mới ghi, nhấn mở nhánh mới chạy; không tự làm khi render.
  Chặn bấm lặp khi request đang pending (hiện `post` chưa dùng `busy`), giữ lỗi API, reload thành công và hiện FLOW
  vừa ghim. Khi polling đổi target, không để nhãn cũ gửi ID mới; kiểm lại điều kiện lúc bấm.
- Không có target hợp lệ: CTA chọn keyword đưa focus tới bảng, hoặc mở rộng từ root nếu còn hợp lệ.
  Đang chạy hiện trạng thái và lý do nút khoá; lỗi mạng không được đổi thành “chưa có dữ liệu”.

### Bản chữ EN và VI đề xuất

Mỗi mục dưới là **câu lợi ích → nút**, nội suy keyword thật; không đưa dấu placeholder ra màn hình.

- **Branch map chưa có nhánh.** EN: “Find a more focused niche by exploring a keyword.” → “Go deeper on {keyword}”.
  VI: “Mở một keyword để tìm ngách cụ thể hơn.” → “Mở tiếp {keyword}”.
- **Chưa ghim FLOW, có ứng viên có điểm.** EN: “Keep a promising long-tail so you can research it next.” →
  “Pin top long-tail: {keyword}”. VI: “Ghim một ngách cụ thể để quay lại research tiếp.” → “Ghim ngách gợi ý: {keyword}”.
  Chưa có điểm: EN “Choose a keyword to pin” / VI “Chọn keyword để ghim”; không tuyên bố đây là tốt nhất.
- **Chưa research sâu.** EN: “Research a keyword to see its competitors and demand signals.” → “Choose a keyword”.
  VI: “Tra một keyword để xem đối thủ và tín hiệu nhu cầu.” → “Chọn keyword”. Focus checkbox đầu tiên hợp lệ;
  thao tác Research sâu vẫn do người dùng bấm, không tự chọn hàng loạt.
- **Bộ lọc không khớp.** EN: “See all keywords to choose another direction.” → “Clear filters”.
  VI: “Xem lại tất cả keyword để chọn hướng khác.” → “Xoá bộ lọc”. Reset query và group, giữ dữ liệu/ghim.
- **Cây/bảng chưa có keyword, đã dừng.** EN: “Get keyword suggestions to start exploring.” → “Expand {seed}”.
  VI: “Lấy gợi ý keyword để bắt đầu tìm ngách.” → “Mở rộng {seed}”. Dùng root thật; thiếu root dẫn về form Explore.
- **Niche map/Top cơ hội thiếu số.** EN: “Collect keyword metrics to compare opportunities on the map.” →
  “View collection status”. VI: “Lấy số liệu keyword để so cơ hội trên bản đồ.” → “Xem trạng thái lấy dữ liệu”.
  Đưa focus tới ProgressPanel; ở đó hiện nguồn lỗi và hành động hiện có, không hứa một API lấy lại metrics chưa có.
- **Niche chưa có dữ liệu nguồn (Trends/đối thủ).** EN: “Load this source to assess the niche with evidence.” →
  “Retry {source}”. VI: “Lấy dữ liệu nguồn này để đánh giá niche có dẫn chứng.” → “Thử lại {source}”.
  Chỉ hiện retry theo khả năng hiện tại của SourceBlock; nếu nguồn đã xong nhưng rỗng thì giải thích không tìm thấy,
  thêm lối đổi keyword, không lặp retry vô hạn hay gọi đây là lỗi.
- **Health chưa có điểm.** EN: “Collect missing evidence before choosing your next step.” → “View missing factors”.
  VI: “Bổ sung bằng chứng còn thiếu trước khi chọn bước tiếp.” → “Xem yếu tố chưa đo”. Mở danh sách yếu tố.
  Nếu tải health thất bại: EN “Could not load niche health.” → “Retry”; VI “Không tải được sức khoẻ niche.” →
  “Thử lại”. Phân biệt loading/error/empty, không tiếp tục trả `null` làm mất cả lỗi.

**KHÔNG làm:** chọn ngẫu nhiên, ghim root, suy “không có nhu cầu” từ dữ liệu rỗng, tự chạy research hoặc dùng một
nút “Bắt đầu” chung không rõ đích. Không mở rộng đợt sửa chữ sang mọi trang ngoài niche/Explorer.

**Tiêu chí kiểm được:** mỗi khối rỗng có một hành động khả thi hoặc lý do khoá; EN/VI diễn đạt cùng hành vi;
không gọi “top” khi thiếu điểm. Bấm đến đúng node, pin một lần, lỗi còn thấy; bàn phím dùng được, chữ dài không ép nút.

**File đụng:** `web/src/components/FlowMap.tsx`, `ExploreDashboard.tsx`, `NicheMap.tsx`, `HealthBlock.tsx`,
`RunDashboard.tsx`, `SourceBlock.tsx`; helper mới nêu trên; `web/src/locales/en-text.ts`, `en-text-sweep.ts`.

**Test `web/tests/`:** mới `explore-next-action.test.ts`: không node, chỉ root, null/0/đồng điểm, max depth,
đã ghim, lá có/không điểm, target đổi, đang chạy; bổ sung `flow-path.test.ts` / `explore-api.test.ts` cho pin lặp
và node sai exploration. Mới `niche-empty-state.test.ts` kiểm model trạng thái loading/error/empty và bản chữ
EN/VI; kiểm tương tác focus, double-click, lỗi/retry, pin/reload trong trình duyệt. Không chỉ so snapshot chữ.

**Độ lớn:** M — dùng callback có sẵn, thêm chọn target và quản lý request đúng.

## B · Giải thích thu gọn, kết luận nhìn thấy ngay — S

**Mục tiêu:** đọc một câu là biết gợi ý cùng giới hạn chính; vẫn tìm lại được mọi công thức và nguồn.

**Cần làm:** giữ một câu ngắn theo `decision`, ưu tiên lý do cap/cờ chặn hoặc yếu tố chưa đo;
ví dụ mẫu EN “Test more: evidence is still missing for {factors}.” / VI “Test thêm: còn thiếu bằng chứng cho {factors}.”
Chỉ dùng khi thật sự thiếu; đủ số nhưng điểm giữa ngưỡng phải nói cần kiểm chứng giả thuyết, không bịa yếu tố thiếu.
Không cắt `summary` theo ký tự rồi làm mất ý. Đưa toàn bộ summary dài, giải thích 7 yếu tố, ngưỡng từ Settings
và link sửa vào `details` “Xem cách tính / How scoring works”, mặc định đóng. Tooltip ⓘ chỉ giải thích thuật ngữ
ngắn, focus/touch mở được; nội dung dài dùng disclosure một cột. Giữ cảnh báo cờ chặn/giới hạn quan trọng ở ngoài,
và `details` nguồn theo từng yếu tố hiện có; không thay đổi summary dùng trong evidence pack.

**KHÔNG làm:** giấu cờ chặn, bỏ nguồn hay đổi kết luận backend, tooltip chỉ hoạt động hover.

**Tiêu chí kiểm được:** mặc định không hiện hai đoạn công thức dài; có đúng một câu kết luận chính ngắn;
Enter/Space mở cách tính, focus không mất, mọi đầu vào/nguồn/ngưỡng vẫn truy cập được, EN/VI không tràn.

**File đụng:** `web/src/components/HealthBlock.tsx`; mới `web/src/lib/health-presentation.ts` cho câu kết luận
thuần từ dữ liệu; locale chung/sweep. Không sửa thuật toán `score-v2.ts`.

**Test `web/tests/`:** mới `health-presentation.test.ts`: decision null, cap độ phủ, cờ chặn, đủ số nhưng TEST THÊM,
BUILD/BỎ; nguồn/summary dài vẫn còn trong disclosure. Giữ `health.test.ts` xanh; kiểm bàn phím trong trình duyệt.

**Độ lớn:** S — tổ chức lại nội dung, không đổi dữ liệu.

## C · Điểm và độ phủ dễ hiểu — M

**Mục tiêu:** phân biệt điểm cơ hội, phần dữ liệu đã có điểm và loại bằng chứng; không đọc phần trăm thành độ chắc thắng.

**Cần làm — cân nhắc ba phương án**

1. **Vòng điểm + hai dòng độ phủ.** Dễ nhận diện nhưng chiếm diện tích, dễ khiến người dùng đọc vòng như tiến độ hoàn thành;
   nhãn dài khó đặt trong khung hẹp.
2. **Số lớn + thanh điểm ngang, độ phủ nằm dưới — chọn phương án này.** Đọc nhanh số/thang, vừa chiều ngang khung;
   nhãn giải thích được xếp dọc, phù hợp 960px và không cần thư viện biểu đồ mới.
3. **Chỉ số lớn và ba dòng chữ.** Ít rủi ro layout nhưng khó phân biệt trực quan điểm với phần dữ liệu còn thiếu.

Phương án chọn: số `total/10`, thanh điểm có nhãn truy cập; dưới là thanh coverage với nhãn
**“Trọng số đã có điểm / Weighted coverage”** và phần trăm. Một dòng riêng ghi
**“Đo trực tiếp + tự chấm / Direct evidence + self-rated”** lấy từ `solid`; ⓘ giải thích proxy và tự chấm.
Không vẽ solid như phần trăm của coverage: cả hai hiện chia cho tổng trọng số trong code.
V1 vào “Điểm Explorer v1 / Explorer v1 score” trong cách tính, giải thích thang 100 và công thức khác,
không đặt như điểm cũ so tiến bộ với v2. `null` hiện “Chưa đủ dữ liệu / Not enough data”, không thành 0;
0 là giá trị hợp lệ. Màu thanh trung tính, màu verdict theo quyết định đã cap, tránh các mốc màu 7/5 hiện tại
của `scoreTone` bị hiểu là ngưỡng BUILD/TEST do Settings quyết định. Dùng chữ cùng màu, không chỉ màu.

**KHÔNG làm:** đổi giá trị, làm tròn khác backend, dùng phần trăm thành xác suất thành công, dựng số minh hoạ như dữ liệu thật.

**Tiêu chí kiểm được:** mọi giá trị khớp response health; thang điểm và độ phủ có tên riêng; null khác 0;
ngưỡng tuỳ chỉnh/cờ chặn không làm màu nói ngược verdict. Ô điểm xuống dòng gọn khi khung hẹp, v1 vẫn tìm được.

**File đụng:** `web/src/components/HealthBlock.tsx`, `web/src/lib/health-presentation.ts` của B;
locale chung/sweep, `globals.css` nếu cần style dùng riêng.

**Test `web/tests/`:** bổ sung `health-presentation.test.ts` cho null/0, coverage/solid, v1 thiếu,
ngưỡng tuỳ chỉnh và điểm cao bị cap; `health.test.ts` giữ nguyên kết quả thuật toán.
Kiểm accessibility tên/thang giá trị và screenshot EN/VI ở 960/1340/1920px.

**Độ lớn:** M — thay phân cấp thị giác và làm rõ nghĩa dữ liệu.

## A · TEST MORE, BUILD, SKIP thành bước đi tiếp — L

**Mục tiêu:** nút gợi ý mở danh sách việc cụ thể đúng niche, có đích và điều kiện thực hiện.

**Cần làm**

- Thay span verdict bằng nút rõ hành động: “TEST MORE · Xem việc cần test / See what to test”,
  “BUILD · Xem bước tiếp / See next steps”, “SKIP · Xem lý do và hướng khác / See why and alternatives”.
  Bấm mở panel một cột ngay dưới, `aria-expanded`, focus hợp lý; không ghi quyết định chỉ vì bấm nút.
  Null decision có nút “Xem dữ liệu còn thiếu / See missing evidence”.
- Panel TEST MORE đọc `factors`, `next`, `capped`, `flags`, không parse câu dịch thành lệnh.
  Mỗi việc có yếu tố, hiện thiếu gì, cách bổ sung, nguồn sẽ dùng, CTA và điều kiện khoá. Demand/trend thiếu:
  đưa tới `#trends` cùng nút retry hiện có ở RunDashboard; nguồn đang chạy thì theo dõi, không tạo job trùng.
  Money/competition dùng nguồn store; pain đưa tới khối đọc review thực tế sau khi đối chiếu callback ở lúc triển khai.
- Reach/fit: khôi phục **form tự chấm có chủ đích trong panel việc cần làm**, dùng API `score-manual` hiện có,
  giữ khoảng điểm/validation/lý do hiện tại. Reach yêu cầu lý do kèm nguồn kênh/cộng đồng; ghi rõ tự chấm,
  không hứa collector tự đo customer reach. AI có thể giúp tìm bằng chứng nhưng không tự điền điểm thành số đo.
  Gửi lỗi giữ nội dung nhập; thành công reload health; chưa nhập vẫn “chưa đo”.
- Test bán trước: giữ nút xám **“Test bán trước · Phase 43”** cùng lý do chưa mở; bổ sung capability vào
  `features.ts` nếu chưa có (hiện chưa có entry riêng). Khi Phase 43 thật sự sẵn sàng mới mở đúng UI/route đã kiểm,
  giữ run/keyword/country. Không chỉ bỏ comment nháp AI và tuyên bố Phase 43 hoàn tất.
- Giao AI research tiếp: tạo nháp có runId, keyword, country, yếu tố thiếu, cap và link evidence pack; người dùng
  chọn phiên hoặc chủ động tạo phiên bằng API hunt hiện có rồi xem/sửa prompt trước Gửi. Hiện `HuntIndexPage`
  tạo `/hunt/:id?q=...` cho ý tưởng tìm niche, **chưa có handoff research**: thêm hợp đồng draft riêng nhận ngữ cảnh
  qua router state, validate ID và lấy dữ liệu mới; không nhét prompt research vào `q` để biến thành `/find-niches`.
  Mất draft sau reload thì cho quay lại niche, không tự gửi lại. Thiếu AI: link Settings và tải/copy evidence pack.
  Không tạo phiên, chạy CLI hoặc mở quyền ghi khi chỉ mở panel.
- BUILD: mở checklist đọc cờ/giới hạn, Collect vào Project bằng luồng hiện có, chuẩn bị brief;
  Brief/Spec nếu chưa có giữ xám “Phase 28.5”, test bán trước vẫn tuân Phase 43. Không tự bắt đầu viết sản phẩm.
- SKIP/BỎ: hiện lý do từ score/cờ, lối mở Explorer cho đúng keyword/country qua luồng Explore hiện có,
  hoặc xem ứng viên khác trong Project đã liên kết. Chưa có niche thay thế thì mời tìm, không bịa tên hoặc điểm;
  không tự xoá/loại niche. Không dùng tên dịch EN làm enum: dữ liệu vẫn BUILD / TEST THÊM / BỎ.

**KHÔNG làm:** tự chạy chuỗi collector/AI, tự chốt quyết định, tăng quyền MCP, mở tính năng tương lai không có gate,
cam kết tăng coverage/solid sau thao tác chưa thành công. `next.after` là khả năng dự kiến, không phải kết quả đã đo.

**Tiêu chí kiểm được:** mỗi verdict mở đúng panel; mỗi CTA đang bật tới đúng run/node/project hoặc hành động hợp lệ;
thiếu dependency có lý do và phase; chỉ bấm Gửi mới chạy AI. Retry lỗi không mất dữ liệu, điểm reload từ server;
quay lại niche vẫn đúng ngữ cảnh, không tạo phiên/job lặp khi bấm nhanh.

**File đụng:** `web/src/components/HealthBlock.tsx`, `RunDashboard.tsx`; mới
`web/src/lib/health-actions.ts` (map FactorKey sang action ID/điều kiện, không tính điểm);
`web/src/lib/features.ts`; `web/src/client/HuntIndexPage.tsx`, `HuntPage.tsx`,
`web/src/components/HuntChat.tsx` cho handoff draft; locale chung/sweep/hunt.
Đọc lại `web/src/lib/score-v2.ts`, `score-config.ts`, API health/manual và hunt trước khi nối; chỉ sửa API nếu
hợp đồng thật thiếu ngữ cảnh, không mở rộng quyền hay schema trong phase này.

**Test `web/tests/`:** mới `health-actions.test.ts` cho mọi verdict, thiếu từng yếu tố, cờ cap, không có `next`,
manual/retry lỗi, phase gate; bổ sung `health.test.ts` cho lưu điểm tay có lý do và reload giữ đúng trust.
Mới `hunt-handoff.test.ts`: đúng run/country, ID lỗi, draft không tự gửi, không nhầm `/find-niches`, reload/mất draft,
thiếu AI, tạo phiên lỗi. Kiểm hành trình nút bằng trình duyệt, gồm bàn phím và double-click.

**Độ lớn:** L — nhiều đích hành động, form ẩn và handoff AI chưa nối.

## Thứ tự làm · kiểm chứng

1. **D — M, gấp:** tái hiện và sửa layout, lưu ảnh trước/sau cùng dữ liệu.
2. **E — M, gấp:** nối callback và trạng thái rỗng trên nền layout đã ổn.
3. **B — S:** thu gọn giải thích, tách kết luận trình bày khỏi summary xuất evidence.
4. **C — M:** số + thanh ngang, nhãn độ phủ và bằng chứng đúng nghĩa.
5. **A — L:** panel hành động, gate tương lai, form tự chấm và handoff AI có kiểm soát.

S/M/L là độ lớn tương đối, thời gian **chưa đo**. Khi triển khai mỗi việc: viết test hành vi trước,
chạy thấy lỗi mong đợi, sửa tối thiểu, chạy test tương ứng rồi kiểm trình duyệt; không viết test dò source thay hành vi.
Chạy `npm run check` ở gốc khi sửa code; chạy `npm run docs:build` cho tài liệu. Lượt plan này chỉ build docs.

Kiểm chung EN/VI ở 960/1340/1920px, cửa sổ thấp, zoom 125–150%, tên dài, đủ cột, đang chạy/lỗi/rỗng,
chọn nhiều keyword, mở disclosure/panel, cuộn đến hàng cuối. Chụp và **mở đọc** từng ảnh; ghi kết quả thật khi triển khai.
Với chính trang plan: mở MkDocs khoảng 1340px, xác nhận nội dung một cột dọc và đường dẫn/code không vỡ cột.

## Kết quả 2026-10-28 (D + E)

- **D:** bỏ 2 khung `h-[700px]`; bảng `table-fixed` + `colgroup`, ghim cột chọn + Keyword (`sticky left`), cột số canh phải,
  vùng bảng `max-h-[min(70vh,640px)]` + `scrollbar-gutter: stable`; cây theo `@container` (rộng ≥ 64rem mới đặt cạnh bảng,
  dính khi cuộn), nút Mở tiếp thành icon có `aria-label`, thụt lề nhỏ hơn; tab nhóm xuống dòng; thanh đã chọn `sticky bottom-0`
  trong luồng trang (bỏ `pb-20`). Đo Explorer #14 (91 keyword): 1340px đáy bảng 1670 < đầu Niche map 1694, 960px cây trên bảng,
  không trang nào cuộn ngang; checkbox hàng cuối bấm được (`elementFromPoint`).
- **E:** `lib/explore-next-action.ts` (điểm cao nhất có dữ liệu, hoà điểm ID nhỏ, null ≠ 0, lá cho ghim, bỏ gốc / độ sâu tối đa).
  Sơ đồ nhánh rỗng → "Mở tiếp {keyword}" / "Chọn keyword"; FLOW rỗng → "Ghim ngách gợi ý: {keyword}" (chỉ khi có điểm) /
  "Chọn keyword để ghim"; bảng lọc rỗng → "Xoá bộ lọc"; bảng trống → "Mở rộng {seed}"; Đã research sâu rỗng → "Chọn keyword"
  (focus ô chọn đầu, không tự chọn); `post` chặn bấm lặp; HealthBlock phân biệt đang tải / lỗi (Thử lại) thay vì `null`.
- **B:** `lib/health-presentation.ts` — đúng 1 câu kết luận theo `decision` đã cap (thiếu yếu tố → "Test thêm: còn thiếu bằng chứng cho …";
  đủ số giữa ngưỡng → "cần kiểm chứng giả thuyết"; BỎ nêu 2 yếu tố yếu nhất). Summary đầy đủ, cách tính 7 yếu tố, ngưỡng + link Cài đặt,
  điểm Explorer v1 vào `details` "Xem cách tính" (đóng sẵn). Cờ chặn + lý do bị hạ vẫn ở ngoài; summary của evidence pack không đổi.
- **C:** số `total/10` + thanh trung tính (`role=meter`), thanh **Trọng số đã có điểm** riêng, dòng **Đo trực tiếp + tự chấm** có ⓘ
  ("không phải xác suất thành công"); null hiện "Chưa đủ dữ liệu", 0 là 0. Màu chỉ theo gợi ý đã cap.
- **A:** `lib/health-actions.ts` — nút "{gợi ý} · Xem việc cần test / bước tiếp / lý do và hướng khác / dữ liệu còn thiếu" (`aria-expanded`)
  mở panel một cột: yếu tố thiếu → cuộn tới khối có nút chạy lại (#trends · #competitors · #complaints); reach / fit → form tự chấm
  (API `score-manual`, reach bắt buộc link, lỗi giữ chữ); Test bán trước khoá "Phase 43"; Brief + Spec khoá "Phase 28.5"; BUILD có Collect +
  đọc cờ; BỎ có Explore; giao AI = **điền sẵn** ô Hỏi AI (sự kiện `prefillAi`, không tự gửi, không tạo phiên).
  Lệch plan: chưa làm handoff sang phiên AI Agent (router state) — dùng ô Hỏi AI chỉ đọc thay thế.
- Kiểm: `health-presentation.test.ts` 5 test; xem Research #44 ở 1340 + 960px EN, mở panel bằng Enter, "Điền vào Hỏi AI" điền đúng
  Research #44 + 4 yếu tố thiếu (0 tin nhắn gửi), reach thiếu link bị chặn trước khi gọi server.
- **Chưa làm:** Branch map cây dọc khi hẹp, chữ rỗng Niche map / SourceBlock, handoff sang AI Agent; zoom 125–150 % — **chưa đo**.

## Rủi ro

- Overlay scrollbar khác scrollbar chiếm chỗ: gutter một mình chưa đủ; kiểm cả hai, không che lỗi bằng overflow hidden.
- CSS Tabs/Flow dùng chung: scope thay đổi vào Explorer, kiểm trang đang dùng component chung không bị hồi quy.
- Polling thay ứng viên khi chuẩn bị bấm hoặc request ghim lặp: giữ target theo ID và pending cho từng thao tác.
- “Measured/real data” dễ gây hiểu sai; đổi nhãn hiển thị phải giữ nghĩa coverage/solid và dữ liệu cũ.
- Tài liệu Phase 43 mô tả nền có sẵn nhưng UI đang ẩn: khả năng thực thi lấy theo code/gate lúc triển khai.
- Khôi phục form tự chấm là quyết định UX có chủ đích trong A, không vô tình bật cả khối nâng cao đã bị ẩn.
- Thu gọn quá tay che cờ chặn; luôn giữ lý do quan trọng ở câu kết luận và liên kết xem đầy đủ.

## Câu hỏi mở

- “Top long-tail” nên ưu tiên keyword đang chọn hay điểm opportunity? Mặc định keyword có điểm cao nhất đủ điều kiện;
  hiện rõ tên trước bấm, thiếu điểm dùng chọn tay.
- Có muốn khôi phục tự chấm reach/fit trong panel? Đề xuất có, chỉ hiện khi cần bổ sung, luôn yêu cầu lý do.
- Có cần giữ thanh thao tác luôn nhìn thấy khi bảng dài? Đề xuất ưu tiên trong luồng để hết che nội dung;
  chỉ giữ sticky nếu kiểm được chiều cao thực và focus hàng cuối.
- Handoff AI mặc định chọn phiên hay tạo mới? Đề xuất chọn phiên trước, tạo mới là thao tác riêng có nhãn rõ.

[← Phase 28.7 · AI Agent dễ nhìn](phase-28-7-ai-agent-ux.md) · [Mục lục Web](index.md)
