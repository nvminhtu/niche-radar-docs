# Phase 28.7 · AI Agent dễ nhìn: danh tính, trạng thái, lệnh AI và phiên gần đây

> Mở phiên săn là biết đang dùng AI nào và model nào; gọn bớt hướng dẫn; chọn lệnh có sẵn với đúng dữ liệu;
> biết khi nào sang bước tiếp; nhìn dấu ✦ là nhận ra chức năng AI; luôn thấy AI đang làm gì và quay lại đúng phiên đang chạy.

<span class="chip chip--done">Xong 2026-10-28 · T1–T7 (bản gọn, xem Kết quả)</span>

<div class="box box--goal" markdown>
**Hiện có — đối chiếu code ngày 2026-10-27.**

- `HuntChat.tsx` ghim chat bên phải, GET `/api/ai/chat` một lần khi mount, chỉ nhận `route`, `label`, `error`;
  chưa có model hay icon hãng. Menu `/` và chip lệnh có sẵn nhưng lặp danh sách skill, chưa có điều kiện/ngữ cảnh chọn.
- `HuntFlow.tsx` có thanh 6 bước, thẻ “Bước n/6 · đang ở đây”, nút cam gửi prompt ngay. `flowState()` suy ra tiến độ
  từ ứng viên và nhật ký; không lưu tiến độ riêng. Thanh hiện cho bấm **mọi** bước; thiếu điều kiện chỉ cảnh báo, vẫn chạy.
- `web/src/lib/ai/chat.ts`: Claude chạy `-p --output-format stream-json --verbose`, parser đọc `system/init` để lấy phiên;
  Codex chạy `exec [resume] --json --ignore-user-config`, parser đọc `thread.started`. Chưa chuyển metadata model ra UI.
- Settings lưu tuyến và model trong `settings.ts`; các việc một bấm truyền model qua `cli.ts`, nhưng `runChat()` hiện
  **không nhận model Settings**. Chat chỉ hỗ trợ Claude Code/Codex; Gemini và API vẫn chưa nối chat.
- Commit `7cd6806`: `Button` có variant `ai`, `AiTaskBlock` dùng nút ✦ gradient; `AiRunButton` vẫn dùng đũa phép
  ở variant khác. [Phase 28.4](phase-28-4-ai-magic.md) còn nhiều chỗ mới là kế hoạch, không coi là đã có.
- Trang AI Agent thực tế ở `web/src/client/HuntIndexPage.tsx`, route `/hunt` trong `web/src/client/main.tsx`;
  repo hiện **không có `web/src/app/`**. Guide 6 bước đang đứng trước Recent Sessions; danh sách chỉ fetch một lần.
- `hunt.ts` lưu phiên bằng `projects.kind = 'hunt'`, ứng viên ở `projectItems`, nhật ký ở `projectLog`;
  `projects.chatSession` chỉ giữ ID resume CLI, không phải trạng thái đang chạy hay lịch sử tin nhắn.
  `listHunts()` lấy 20 phiên chưa lưu trữ, mới cập nhật trước; trả tên, ID, updatedAt và số ứng viên chưa loại.
- `ai/chat.ts` đã phát `tool` (name/input), `text`, `done`, `error`; chưa phát vòng đời hoàn tất từng tool.
  `HuntChat` chỉ giữ tên tool trong bộ nhớ và `pending`; `HuntPage` poll 1,5 giây khi chat/collector bận,
  nhưng đang bỏ qua lỗi tải. Header chat và đầu flow chưa có trạng thái chung luôn nhìn thấy.
- Badge ở `AppShell.tsx` lấy `activity.running.length`, bấm mở việc đầu tiên. `activity.ts` đếm **lượt Research/Explore**,
  không phải từng source job và chưa có chat/session; Research còn giới hạn truy vấn 24 giờ/50 lượt.
  Vì vậy “6 running” hiện không chứng minh có 6 collector hay 6 phiên AI đang chạy.
- Bản chữ hiện tại nằm ở `web/src/locales/en-text-hunt.ts`, `en-text-flow.ts` và `en-text.ts`.
</div>

**Cần xong trước:** nền phiên săn [Phase 28.6](phase-28-6-ai-agent.md), quyền ghi
[Phase 28.2](phase-28-2-mcp-write.md), skill thật của [Phase 28.3](phase-28-3-skills.md), lựa chọn AI ở
[Phase 27.6](phase-27-6-ai-settings.md) / [27.7](phase-27-7-ai-cost-plans.md).
Dùng lại giao diện gradient của `7cd6806`; không cần chờ toàn bộ 28.4 hoặc [28.5](phase-28-5-brief-plan.md).

## Mục tiêu · cần làm · KHÔNG làm

- **Mục tiêu:** người dùng hiểu AI đang chạy, dữ liệu sẽ gửi và bước tiếp theo mà không phải nhớ lệnh.
- **Cần làm:** T1 danh tính thật; T2 đóng/mở lại hướng dẫn; T3 menu lệnh; T4 điều hướng đủ điều kiện; T5 dấu ✦ dùng chung; T6 trạng thái luôn thấy; T7 phiên gần đây và truy vết việc chạy.
- **KHÔNG làm:** thêm nhà cung cấp chat, tự gọi AI để dò model, đổi điểm/số liệu, sửa collector, tạo skill giả,
  chạy chuỗi AI tự động, mở rộng quyền MCP, xây đầu ra Chốt/Gói Build của 28.5. Không làm code trong lượt viết plan này.
- Giữ tính năng tương lai xám + nhãn phase theo `web/src/lib/features.ts`; không bật toàn bộ bản đồ 28.4 chỉ để thêm icon.
- Tài liệu và menu chức năng xếp một cột dọc; tên dài được xuống dòng, không chia lưới thẻ hẹp.

## T1 · Biết đang nói với AI nào — L

**Cần làm**

- Header chat: icon được phép dùng + tên tuyến + model thực nhận từ CLI. Ví dụ hình thức “Claude · Opus 5.5”
  chỉ hợp lệ nếu runtime xác nhận model tương ứng; không lấy ví dụ này làm mặc định.
- Thêm kiểu `AiIdentity`: `route`, `label`, `configuredModel`, `resolvedModel`, `source`, `observedAt`.
  `resolvedModel` có thể null; `source` phân biệt `runtime`, `config`, `unknown`. Cấu hình/alias không phải bằng chứng runtime.
- Thêm sự kiện NDJSON `identity` vào `ChatEvent`, gửi từ parser qua server đến chat; giữ model theo từng lượt trả lời.
  GET chat trả danh tính đã biết trước lượt chạy; không chạy một câu hỏi mất lượt chỉ để điền header.

### Đọc model đúng tuyến

- **Claude Code:** khảo sát output của đúng CLI đang cài với đúng argv của `chatArgs()`, ghi phiên bản và fixture đã
  loại dữ liệu riêng. Đọc `model` của `system/init` nếu có; đối chiếu `message.model` trên assistant event và
  `modelUsage` ở kết quả nếu có. `cli.ts` đã đọc `modelUsage` cho việc một bấm, nhưng chat chưa làm.
  Nếu có nhiều model, hiển thị model của lượt tương ứng, không lấy khoá đầu rồi gán cho cả phiên.
  Cấu hình project được cho phép bởi `--setting-sources project` chỉ là gợi ý trước khi chạy; alias `opus` không tự
  suy thành một phiên bản. Truyền model Settings bằng `--model` khi chọn rõ; để trống thì giữ mặc định CLI.
- **Codex:** khảo sát stream `exec --json` và `exec resume --json` của bản CLI thực tế. Nếu init/turn metadata có
  model thì parser lấy đúng trường đã chứng minh bằng fixture; **không mặc định `thread.started` có model**.
  Nếu stream không có: kiểm metadata phiên do CLI tạo, chỉ đọc model của đúng `thread_id`, không quét nội dung chat.
  Không có nguồn ổn định được hỗ trợ thì dùng fallback chưa rõ. Config người dùng không dùng làm model thực chạy:
  argv hiện có `--ignore-user-config`. Truyền model Settings bằng `-m` sau khi kiểm cả exec/resume hỗ trợ;
  model yêu cầu chỉ hiện phụ “đã chọn”, tới khi runtime xác nhận mới thành model thực.
- **Gemini/API:** Settings có các tuyến này nhưng chat chưa hỗ trợ. Hiện tên đã chọn + “Chưa hỗ trợ trong AI Agent”
  và link Settings; không giả vờ đang chat bằng Claude/Codex. Không mở tuyến mới trong phase này.
- CLI không trả/không đọc được metadata: **“Claude Code · model chưa rõ”** hoặc **“Codex · model chưa rõ”**
  (EN: “model unknown”). Không suy model từ tên gói, phiên bản CLI, tên binary hay bảng `MODELS`.

### Cache, đổi Settings và icon

- Cache trong bộ nhớ server ở module mới `ai/identity.ts`, khoá gồm tuyến, binary/phiên bản, thư mục AI,
  model yêu cầu, revision Settings và session ID. Lưu nguồn + thời điểm; restart thì chưa rõ, không cần migration.
  Cache lượt cũ chỉ được ghi “lần gần nhất”, không khẳng định lượt mới đang dùng cùng model.
- POST Settings thành công làm mất hiệu lực cache danh tính/readiness/choices. Client dùng một hook chung,
  nhận sự kiện Settings đổi và tải lại khi focus/đổi trang; trước gửi phải kiểm revision phía server.
- Lượt đang chạy giữ tên AI thực của lượt ấy; header phân biệt “đang chạy” với “lượt tiếp dùng…”. Đổi tuyến/model
  không resume session cũ sang CLI khác: xoá liên kết chat session cho lượt mới, giữ ứng viên và nhật ký.
  Sự kiện muộn từ request cũ không được ghi đè danh tính mới.
- Kiểm asset sẵn có và quyền dùng trước. Logo hãng chỉ dùng asset chính thức/được cấp phép, ghi nguồn và điều kiện
  trong hồ sơ asset; thiếu quyền thì **chỉ tên chữ**. Nếu cần hình AI chung, viết brief để Codex sinh;
  không tự vẽ SVG giả logo và không nhờ Codex tái tạo logo hãng để né quyền dùng.

**File sẽ đụng:** `web/src/lib/ai/chat.ts`, `hunt-chat.ts`, `settings.ts`, `ready.ts`, module mới `identity.ts`;
`web/src/server/app.ts`; `web/src/components/HuntChat.tsx`, `ChatPanel.tsx`, `AiRunButton.tsx`;
`web/src/client/SettingsPage.tsx`; hook mới `web/src/lib/ai-client.ts`; locale Hunt/chung.

**Xong khi / test:** bổ sung `web/tests/ai-chat.test.ts`, `ai-cli.test.ts`, `hunt.test.ts` và mới
`web/tests/ai-identity.test.ts`: init có/thiếu model, alias, JSON lỗi, nhiều model, resume, metadata không có,
Settings đổi giữa lượt, cache khác tuyến, session cũ không bị gửi sang CLI mới. Kiểm argv nhận model Settings;
header không bịa model và không lộ config/key. Chạy thật cả hai CLI lúc triển khai, ghi phiên bản + nguồn trường model.

## T2 · Đóng bớt cảnh báo và hướng dẫn — S

**Cần làm:** component mới `DismissibleNotice.tsx`, nút × có tên truy cập “Đóng hướng dẫn”, bàn phím dùng được;
đóng không chạy AI, không đổi quyền, không xoá dữ liệu.

- `HuntChat.tsx`: đóng phần giải thích “AI đang chỉ đọc”, lời chào “Nói AI bạn muốn tìm gì”, cụm gợi ý skill.
  Quyền chỉ đọc vẫn hiện bằng badge + lối bật quyền, không biến mất cùng phần giải thích.
- `HuntFlow.tsx`: đóng đoạn mô tả/hướng dẫn nhập `/find-niches` và banner hoàn tất; luôn giữ tên bước, nút hành động,
  điều kiện còn thiếu. Không coi nội dung BRIEF/SPEC là banner để xoá; dùng thu gọn có sẵn.
- `web/src/client/HuntPage.tsx`: đóng hướng dẫn lúc chưa có ứng viên và lời giải thích số ứng viên chưa tra;
  giữ số chưa tra cùng nút Tra nốt. `HuntIndexPage.tsx`: cho thu gọn phần giới thiệu flow 6 bước.
- Nhật ký “AI đã làm trong phiên này” là dữ liệu: chỉ thu gọn/mở lại, không xoá. Các status đang tra/đang hỏi giữ
  dòng trạng thái gọn; lỗi server, CLI hỏng, hết quota, lỗi thao tác/hoàn tác luôn còn `role="alert"` và cách xử lý.
  Nếu cho × phần chi tiết lỗi thì chỉ thu gọn trong lượt hiện tại, lỗi mới phải hiện lại; không lưu cờ ẩn lỗi vĩnh viễn.
- Hướng dẫn trong phiên nhớ tại localStorage `nr.hunt.dismissed.v1:<projectId>` bằng ID notice ổn định.
  Giới thiệu ở danh sách phiên dùng `nr.hunt.dismissed.v1:index` toàn giao diện. Không dùng chung cờ giữa project.
  Storage hỏng/bị chặn thì nhớ trong bộ nhớ tới khi tải lại.
- Link **“Hiện lại hướng dẫn”** luôn có trong menu phiên/danh sách phiên; reset đúng phạm vi kể cả khối đã đóng.
  Checkbox Compare tự động giữ nguyên opt-in hiện tại; đóng hướng dẫn không bật hoặc tắt checkbox.

**File sẽ đụng:** các file nêu trên; mới `web/src/lib/hunt-notices.ts`; locale Hunt/Flow.

**Xong khi / test:** mới `web/tests/hunt-notices.test.ts`: reload còn đóng, project khác vẫn hiện, khôi phục đúng
phạm vi, storage lỗi không crash, đổi ngôn ngữ không mất cờ; lỗi quota mới luôn hiện dù trước đó thu gọn lỗi.

## T3 · Menu chức năng có nút đưa lệnh vào chat — M

**Cần làm:** nút **“✦ Lệnh AI”** cạnh ô chat và gõ `/` cùng mở một danh sách. Mỗi dòng có tên, làm gì,
cần gì, trạng thái chọn và lý do bị khoá. Có nút **“Đưa vào ô chat” ngay trong bảng**; người dùng đọc/sửa rồi bấm ✦ Gửi.
Chốt bản đầu chọn **một dòng** mỗi lần để giữ parser slash hiện tại; nhiều dòng là câu hỏi mở, chưa làm hàng đợi.

Danh mục thật tại `web/data/ai/.claude/skills/` (đọc ngày 2026-10-27):

| Lệnh | Làm gì | Cần gì / khi xám |
|---|---|---|
| `/find-niches` | Từ ý tưởng, đề xuất ứng viên rồi gửi tra | Ý tưởng/seed và phiên hiện tại, quyền ghi; thiếu thì yêu cầu nhập/bật quyền. Dùng ở bước 1 hoặc tìm bổ sung |
| `/long-tail` | Mở/dùng cây Explore, lấy keyword hẹp hơn rồi tra | Ứng viên đã tra được chọn (hoặc tốt nhất đã tra), quyền ghi; hợp bước 3 sau BEST. Thiếu BEST/ứng viên thì ghi rõ. Có thể phải chờ Explore |
| `/kill-weak` | Loại ứng viên yếu với lý do có nguồn | Có ứng viên đã tra, quyền ghi; hợp bước 2/4. Không tự loại niche người dùng đã giữ |
| `/compare-niches` | So niche đã tra, đề xuất cái làm trước | Các Research đã xong thuộc project, ít nhất hai để so trong menu; đọc được khi quyền ghi tắt. Không có đủ thì xám + yêu cầu tra thêm |
| `/app-demand` | Đọc bằng chứng, đánh giá nhu cầu | Keyword/Research đã xong hoặc Project có dữ liệu; thiếu thì xám + yêu cầu Research trước; không bắt có quyền ghi |

**Không có `/collect-more` trong thư mục skill.** “Collect more” là `STEP_PROMPT.more`, chủ ý lấy keyword từ Research
hoặc cây đã xong, **không mở Explore mới**; không đổi thành `/long-tail` một cách im lặng. Trong menu có dòng riêng
“Collect thêm — lệnh flow”, dùng đúng prompt hiện tại. BEST, Health check, Brief, Spec cũng ghi **lệnh flow**,
không gắn slash skill không tồn tại; điều kiện theo T4. Health còn việc tra thì chỉ dẫn về nút Tra nốt, chưa gửi AI.

- Sổ lệnh mới `web/src/lib/hunt-commands.ts` làm nguồn chung cho menu, chip và allowlist slash trong `hunt-chat.ts`;
  kiểm đồng bộ với tên thư mục thật, không nạp nguyên file skill vào bundle trình duyệt.
- `buildHuntCommand(id, context)` nhận project ID, ý tưởng, item/keyword đang chọn, Research/Explore ID, locale;
  trả bản nháp + danh sách dữ liệu gửi. `HuntPage` phải truyền lựa chọn vào chat (hiện chưa truyền selected item).
  Chỉ lấy ID thuộc phiên, không dùng tên project thay ID. Không chọn keyword thì yêu cầu chọn hoặc ghi rõ phạm vi toàn phiên.
- Server dựng lại ngữ cảnh tin cậy từ `huntId`, kiểm ID thuộc phiên; dữ liệu do người dùng gõ được coi là dữ liệu,
  không nội suy vào shell. Codex tiếp tục dùng `huntMessage()` chuyển slash thành đọc playbook; Claude dùng Skill.
- Kiểm điều kiện lại lúc đưa vào ô và lúc gửi; undo/đổi keyword/đổi project làm menu cập nhật ngay. Không ghi đè
  bản nháp đang gõ: cho chọn thay thế hoặc huỷ. Giữ giới hạn message hiện tại, không cắt lệnh âm thầm.
- Điều hướng bằng phím mũi tên, Enter chọn, Escape đóng/trả focus; Enter trong menu không vô tình gửi chat.

**File sẽ đụng:** `HuntChat.tsx`, `web/src/client/HuntPage.tsx`, `web/src/lib/ai/hunt-chat.ts`, sổ lệnh mới;
component mới `web/src/components/HuntCommandMenu.tsx`, locale Hunt/Flow.

**Xong khi / test:** mới `web/tests/hunt-commands.test.ts`; bổ sung `hunt.test.ts`: đủ mọi skill thật, không có
slash bịa, project/keyword đúng, khoá kèm lý do, quyền đọc/ghi đúng, undo đổi điều kiện, bản nháp không mất;
Codex chuyển đúng playbook, nhập `/`/Escape/Enter không gửi ngoài ý muốn.

## T4 · Từ bước 1 sang bước 2, và cùng luật đến bước 6 — M

**Trả lời hiện trạng: có.** `flowState().done.find = h.candidates.length > 0`: chỉ cần có ứng viên,
kể cả chưa tra hoặc đã loại. `current` là bước đầu chưa xong. `HuntFlow` reset `pick` mỗi khi `current` đổi,
nên thẻ tự sang BEST (hoặc bước đầu còn thiếu); không tự chạy BEST. Thanh bước hiện còn cho nhảy tới bước bất kỳ;
`blocked` chỉ xem bước ngay trước và hiện “bấm vẫn chạy được”, nút chỉ bị khoá khi `busy`.

**Đề xuất:** tách `done` (kết quả) và `available/reason` (được mở/chạy). Giữ phép tính từ dữ liệu,
không ghi cờ “đã mở” vĩnh viễn. Thêm `flowAccess(h)` dùng chung cho thanh, CTA và menu.

| Chuyển bước | Hiện tại được tính xong khi | Điều kiện đề xuất cho bước kế |
|---|---|---|
| 1 → 2 | Có bất kỳ ứng viên | Có ứng viên còn sống đã tra xong và Research hợp lệ; còn chưa tra/đang tra thì nói rõ BEST chỉ xét phần đã xong |
| 2 → 3 | Có ứng viên giữ | Có ít nhất một niche giữ đã tra xong; cần quyền ghi khi chạy Collect |
| 3 → 4 | Có niche giữ và ứng viên sống không giữ được tạo sau `lastKept` | Giữ điều kiện này cho bản đầu; `lastKept` thực là **createdAt của ứng viên giữ**, không phải thời điểm bấm Giữ |
| 4 → 5 | Bước 3 xong, `todo = 0`, `running = 0` | Thêm mọi ứng viên sống đều `xong`, có niche giữ; trạng thái `lỗi` không được lọt qua vì không nằm trong todo/running |
| 5 → 6 | Có ghi chú AI `BRIEF:` chưa hoàn tác | Có BRIEF còn hiệu lực và các điều kiện trước còn đủ |
| Kết thúc 6 | Có ghi chú AI `SPEC:` chưa hoàn tác | Có SPEC, BRIEF và chuỗi điều kiện trước còn đủ |

- Nút **“Sang bước 2 →”** hiện trong thẻ Find khi điều kiện đủ; tương tự “Sang bước n →” cho 2–5.
  Bấm chỉ chọn thẻ, không gọi AI. Bước 6 có trạng thái hoàn tất, không có bước 7.
- Giữ thẻ đang xem khi dữ liệu cập nhật để người dùng thấy CTA; bỏ tự đổi `pick` vô điều kiện. Mở lại phiên thì chọn
  bước đầu còn cần làm. Thanh cho bấm bước đã mở; bước thiếu điều kiện xám + lý do đọc được bằng focus/tooltip.
- Dùng chuỗi điều kiện trước, không chỉ kiểm bước liền kề; undo có thể khoá lại bước sau. Kết quả BRIEF/SPEC cũ
  vẫn xem được trong nhật ký nhưng không chứng minh đủ điều kiện chạy tiếp. Nếu thẻ đang xem bị khoá, giữ nội dung
  đọc và chỉ rõ quay lại bước thiếu, không gửi prompt.
- Khi busy, vẫn được xem bước đã mở nhưng không gọi AI chồng lượt. Health có todo dùng collector, không ✦;
  còn running/lỗi thì chờ/tra lại; chỉ khi dữ liệu sẵn mới hiện nút ✦ AI đọc bảng.

**File sẽ đụng:** `web/src/lib/hunt-flow.ts`, `web/src/components/HuntFlow.tsx`, sổ lệnh T3, locale Flow.

**Xong khi / test:** bổ sung `web/tests/hunt-flow.test.ts`: rỗng, chỉ ứng viên chưa tra, toàn đã loại, một Research
xong, giữ/chưa giữ, timestamp bằng nhau, ứng viên thêm sau, còn chạy/lỗi, BRIEF/SPEC bị undo và ghi chú đến sai thứ tự.
Kiểm CTA chỉ đổi bước, click bước khoá không chạy, không tự nhảy thẻ khi polling cập nhật.

## T5 · ✦ thống nhất cho mọi chức năng AI — M

**Cần làm:** thêm `AiBadge.tsx` cho dấu ✦ và `AiButton.tsx` bọc `Button` cho hành động AI.
`AiRunButton` dùng lại component này và giữ trách nhiệm chọn tuyến/readiness, không tạo hệ thống chọn AI thứ hai.
Variant chính dùng gradient của `7cd6806`; secondary/ghost vẫn có ✦, không quay lại đũa phép.
Tooltip **“Dùng AI (<tên AI>)”**, EN “Uses AI (<AI name>)”, lấy tuyến thực của hành động từ T1.
Trạng thái chưa nối AI có lý do + link Settings; loading giữ nhận diện ✦ và ngăn gọi lặp. Icon trang trí `aria-hidden`,
nhãn nút và tooltip đọc được bằng bàn phím. Chữ dài không đẩy nút ra khỏi khung.

### Kiểm kê chỗ đang có — file + nút

- `HuntFlow.tsx`: “AI đề xuất keyword + gửi tra” / “AI suggests keywords + researches them”, “AI giữ 3 niche tốt nhất”,
  “AI thêm long-tail” / “AI adds long-tail keywords”, “AI đọc bảng”, “AI viết brief”, “AI viết spec”, “Chạy lại” khi gọi AI.
- `HuntChat.tsx`: Gửi, Cho AI so tiếp; menu/chip skill và checkbox Tự so khi tra xong dùng badge ✦,
  tooltip của checkbox nói rõ có thể gọi AI khi tra xong. Nút Đưa vào ô chat ghi thêm “chưa chạy”.
- `ChatPanel.tsx`: nút mở Hỏi AI và Gửi. Dừng/Cuộc mới không gọi AI, không thêm dấu như một lệnh chạy.
- `AiRunButton.tsx` + `AiTaskBlock.tsx` + `AiResults.tsx`: Chạy bằng AI/Chạy lại của Tóm tắt niche, Chủ đề than;
  “Tải job cho AI” ở TrustMRR dùng badge, tooltip “Chuẩn bị cho AI — chưa chạy”, không nhận là model mặc định đang chạy.
  Nhập kết quả JSON là nhập file, không mang nghĩa gọi AI.
- `GapMatrixBlock.tsx`: “Điền bằng AI” dùng `AiRunButton`; giữ trạng thái thiếu dữ liệu/busy.
- `AskAi.tsx` (dùng tại `web/src/client/SetupPage.tsx`): “Hỏi AI” và từng lựa chọn hãng;
  tooltip theo hãng đích + “mở trang AI”, không gán model CLI cho link web.
- `AiSection.tsx`: “Kiểm tra” ở cả tuyến CLI và API thực gọi thử một câu bằng model đã lưu, phải có ✦;
  chọn mặc định, lưu model, đăng nhập, dò binary không gọi model thì không gắn như nút chạy.
- `HealthBlock.tsx`: Nháp test bán trước đang comment/tạm tắt; khi bật lại phải qua `AiTaskBlock`, **không bật ở phase này**.
- Các chỗ mới chỉ có trong 28.4/28.5 (Explore AI, gap → ý tưởng, sức khoẻ project, chấm bàn quyết định,
  Brief & Plan) dùng component chung khi triển khai. Các nút xuất/copy prompt chỉ chuẩn bị dữ liệu phải ghi “chưa chạy”.

**File sẽ đụng:** các component liệt kê, `Button.tsx`/`web/src/client/globals.css` chỉ khi cần tái dùng style,
locale chung; `features.ts` chỉ cập nhật mô tả/trạng thái có căn cứ, không bật tính năng chưa làm.

**Xong khi / test:** mới `web/tests/ai-controls.test.ts`: primary/secondary/loading/disabled đều nhận ra AI,
tooltip đổi theo Settings và hãng link ngoài; CTA chuyển bước, Tra nốt, Copy, Nhập file không gọi AI.
Rà lại `fetch`, `aiAsk`, `runChat`, `AiRunButton`, `AskAi` trong `web/src/` trước khi đóng việc để bắt call site mới.

## T6 · Trạng thái AI luôn nhìn thấy ở chat và flow — L

**Mục tiêu:** nhìn đầu khung chat bên phải và khối bước bên trái là biết AI rảnh, trả lời hay gọi tool/tra nguồn nào,
đã chạy bao lâu; không phải cuộn tới tin nhắn cuối để đoán.

**Cần làm**

- Thêm dòng cố định dưới danh tính ở header hiện ghi “AI Agent · Runs on your Claude Code · uses your plan” và
  ở đầu `HuntFlow`: **chấm màu + chữ + thời gian**. Rảnh (xám, thời điểm hoạt động cuối), Đang trả lời chat
  (xanh dương, thời gian lượt), Đang làm việc (cam, tên tool/nguồn + keyword + thời gian), Lỗi (đỏ, lý do/cách thử lại).
  Ví dụ chỉ khi job xác nhận: “Đang tra App Store: pomodoro… · 00:42”. Không dùng màu làm tín hiệu duy nhất;
  `role="status"` thông báo đổi trạng thái, không đọc lại đồng hồ mỗi giây; lỗi có `role="alert"`.
- Nguồn chat là vòng đời request phía server và stream CLI trong `ai/chat.ts`, qua `/api/ai/chat`:
  phân biệt chờ hàng đợi `oneAtATime`, bắt đầu lượt, trả lời, tool bắt đầu/kết thúc, done/error/stop.
  Mở rộng event với request ID, tool-call ID, thời điểm và ngữ cảnh bước; parser Claude/Codex phải có fixture thật
  chứng minh trường start/end. Hiện event `tool` chỉ là dấu bắt đầu, không được lấy tool cuối làm bằng chứng nó còn chạy.
  Thiếu event kết thúc thì ghi “tool gần nhất: … / đang chờ CLI”, không bịa thời lượng tool hay nguồn đang tra.
- Nguồn collector là `sourceJobs` theo `projectItems.runId`, đọc trạng thái, source, progressLabel, startedAt/finishedAt;
  phân biệt pending “đang chờ” với running “searching”. `HuntCandidate.state` hiện chỉ tổng hợp cả lượt, chưa đủ biết nguồn.
  Tool `start_research` trả về không có nghĩa collector đã xong; chat done nhưng collector chạy thì vẫn **Đang làm việc**.
  Có chat và collector đồng thời thì hiện cả hai và số việc, không để một nhãn che việc còn lại. Có lỗi nguồn trong lượt
  thành công một phần vẫn hiện lỗi nguồn đó, không chỉ dựa vào candidate `xong`.
- Tạo snapshot hoạt động chung phía server (module đề xuất `hunt-activity.ts`) cho T6/T7/menu: ID việc ổn định,
  hunt/project/run/source/tool/request ID phù hợp, trạng thái, startedAt, finishedAt, observedAt và lỗi gọn.
  Chat đang chạy giữ trong registry server, collector đọc DB; không suy từ tin nhắn localStorage hay ID resume.
  Dọn registry khi done/error/abort/timeout trong finally; restart đối soát nguồn còn sống, không phục hồi giả lượt chat.
  Chỉ đưa tool/keyword đã lọc vào nhãn, không hiển thị nguyên input/config. Đồng hồ dựa trên startedAt, không reset mỗi poll;
  thiếu timestamp thì ghi “chưa rõ thời gian”, rảnh không có đồng hồ chạy giả.
- Chip keyword bên trái trong `HuntPage` có spinner + “đang tra / searching”, nguồn và số đang chạy/chờ khi mở chi tiết.
  CTA chạy bước xám khi cùng việc đang bận, kèm lý do; chặn gửi chat chồng lượt và chạy collector trùng cả ở server.
  Kết hợp điều kiện T4, vẫn cho xem bước/dữ liệu đã có; không khoá toàn bộ trang chỉ vì một nguồn đang chạy.
- Mất stream trước done/error: hiện **“Mất kết nối — chưa xác nhận trạng thái”**, thời điểm nhận cuối, nút tải lại;
  không chuyển thành Rảnh. Poll lỗi cũng đánh dấu dữ liệu cũ, không nuốt lỗi như hiện tại. Đề xuất poll snapshot mỗi 2 giây
  khi trang mở, đánh dấu cũ sau 10 giây không xác nhận (ngưỡng thiết kế, chưa đo), tải lại ngay khi focus/kết nối lại.
  Server hiện `s.onAbort(run.stop)` nên mất stream có thể dừng CLI; xác nhận đã dừng từ server trước khi báo lại.
  Collector đã khởi chạy vẫn đối soát riêng. Không tự gửi lại prompt, tự resume hay chạy lại job khi reconnect.

**Không làm:** biến chat thành dịch vụ chạy nền độc lập kết nối, lưu toàn bộ hội thoại, đổi logic collector/điểm,
đoán suy nghĩ của AI hoặc dùng animation thay nguồn trạng thái thật. Trạng thái không được đóng bằng T2.

**Tiêu chí kiểm được:** hai khung cùng báo đúng trạng thái và thời gian của cùng snapshot; chat xong/collector còn chạy
không báo rảnh; biết tool/nguồn/keyword nào đang làm hoặc ghi rõ chưa xác nhận; CTA không tạo việc trùng; mất mạng không báo xong.

**File đụng:** `web/src/components/HuntChat.tsx`, `HuntFlow.tsx`, `web/src/client/HuntPage.tsx`;
`web/src/lib/ai/chat.ts`, `ai/hunt-chat.ts` (ngữ cảnh phiên), `hunt-client.ts`, `hunt-flow.ts`, module mới `hunt-activity.ts`;
`web/src/server/app.ts`, `hunt-api.ts`; locale Hunt/Flow/chung. Đọc schema `sourceJobs` sẵn có, không mặc định cần migration.

**Test:** bổ sung `web/tests/ai-chat.test.ts`, `hunt.test.ts`, `hunt-flow.test.ts`; mới `hunt-activity.test.ts`:
fixture tool start/end, nhiều tool đồng thời, event muộn/request cũ, chờ queue, chat + collector song song, partial error,
stop/timeout/restart, stream đứt, poll lỗi/reconnect không gửi lại, hai tab không tạo lượt trùng, đồng hồ không reset.
Kiểm UI cả bốn trạng thái, chip searching và CTA xám trên EN/VI tại 960px/1340px.

**Độ lớn:** L — cần bổ sung vòng đời tool và hợp nhất hai nguồn trạng thái, không chỉ thêm spinner.

## T7 · Phiên gần đây trước Guide và biết việc chạy thuộc phiên nào — L

**Mục tiêu:** ở `/hunt` khi chưa mở session, người quay lại thấy phiên trước hướng dẫn và lần từ badge “6 running”
tới đúng phiên/keyword/nguồn đang làm.

**Cần làm**

- Thứ tự: tiêu đề/tạo phiên → **RECENT SESSIONS / Phiên săn gần đây** → Guide 6 bước. Guide thu gọn bằng nút có
  `aria-expanded`, tự thu lần đầu khi đã có phiên, mở mặc định khi chưa có; lựa chọn thủ công ưu tiên hơn mặc định.
  Dùng chung cờ index và “Hiện lại hướng dẫn” của T2, không tạo hai cơ chế nhớ xung đột. Danh sách và Guide một cột dọc.
- Mỗi dòng phiên có tên, **bước n/6**, số candidate chưa loại (giữ nghĩa `listHunts()`), project tên + ID + link,
  hoạt động theo nguồn **App Store / Google Play / Google Trends / AI đang chat**, số running và pending riêng.
  Khi tool chạy ghi tên tool dưới hoạt động AI. Chỉ ghi **“rảnh · cập nhật lần cuối …”** khi snapshot xác nhận không còn việc;
  lỗi hoặc mất kết nối vẫn có nhãn riêng và thời điểm xác nhận cuối. Có ngày giờ đầy đủ qua title, không chỉ ngày như hiện tại.
- Bước lấy chung phép tính T4 từ candidates/actions, không lưu một bộ tiến độ thứ hai; hoàn tất ghi “6/6 · hoàn tất”.
  Project gắn kèm hiện là **chính project của phiên**, `projectId = huntId`, không bịa quan hệ tới một project khác.
  `chatSession` là ID resume của CLI, không dùng làm ID dòng session. Timestamp cập nhật nội dung và observedAt hoạt động
  là hai trường riêng; `setChatSession()` hiện không cập nhật `updatedAt`, không dùng nó để đo lần hoạt động cuối.
- Mở rộng API danh sách trả summary theo lô từ dữ liệu sẵn có + snapshot T6, tránh gọi `getHunt()`/tính và ghi score
  cho từng phiên chỉ để vẽ danh sách. Poll/focus dùng chung snapshot với menu; lỗi tải không đổi thành danh sách rỗng.
  Giữ Recent 20 phiên nhưng phần việc đang chạy phải truy vấn đầy đủ ngoài giới hạn 20 phiên/24 giờ/50 lượt hiện có.
- Chốt đơn vị đếm mới cho cả menu và dòng phiên: **mỗi source job đang running = 1 việc, mỗi lượt chat đang chạy = 1 việc**;
  tool con là chi tiết của lượt chat, không cộng lần nữa. Explore còn hoạt động giữ một việc riêng theo exploration ID,
  không cộng lại source job con đã hiện; pending hiện “n đang chờ” riêng, không gắn nhãn searching/running.
  Đây là thay đổi có chủ ý so với `activity.ts` đang đếm Research/Explore, phải sửa đồng bộ badge/banner và test hiện có.
- Bấm badge mở danh sách việc nhóm theo phiên, rồi link `/hunt/:id?c=:itemId` cho keyword hoặc `/hunt/:id` cho chat;
  không còn nhảy thẳng `running[0].href`. Dòng nguồn có link Research tương ứng. Ví dụ fixture 2 session, mỗi session
  3 nguồn đang chạy → badge **6 running**, mỗi session hiện 3; bấm badge thấy đủ cả 6 việc và phiên chứa chúng.
- Khử trùng theo ID việc: `startOrReuse()` có thể gắn một run vào nhiều phiên. Tổng menu là số việc duy nhất,
  chi tiết việc liệt kê mọi phiên liên quan và ghi “dùng chung”; không cộng máy móc số trên các dòng phiên.
  Research/Explore không thuộc hunt vẫn hiện nhóm **“Ngoài phiên AI Agent”** có link gốc; không gán theo keyword trùng.
  Với Explore thiếu liên kết session có căn cứ, giữ ở nhóm này. Phiên lưu trữ có việc chạy vẫn truy cập được từ badge,
  không ép xuất hiện trong Recent mặc định. Menu luôn giải thích đủ tổng số, kể cả việc không thuộc danh sách 20 phiên.

**Không làm:** tạo bảng session riêng, tính năng gắn/chuyển session sang project khác, đổi tên/xoá/lưu trữ phiên,
lưu hội thoại hay tự chạy AI khi mở danh sách. Không sửa code trong lượt cập nhật plan này.

**Tiêu chí kiểm được:** Recent đứng trước Guide trong DOM và giao diện; Guide mở lại được; mọi dòng đủ tên/bước/candidate/project/
hoạt động hoặc rảnh + cập nhật cuối; tổng badge đối soát được tới từng việc duy nhất và mọi phiên liên quan, không bỏ sót việc cũ.

**File đụng:** `web/src/client/HuntIndexPage.tsx`, `web/src/components/AppShell.tsx`, `ActivityBanner.tsx`;
`web/src/lib/hunt.ts`, `hunt-flow.ts`, `activity.ts`, snapshot `hunt-activity.ts` của T6, cơ chế tải activity dùng bởi AppShell;
`web/src/server/hunt-api.ts`, `app.ts`; helper notices T2 và locale Hunt/chung. `web/src/client/main.tsx` chỉ khi cần route
cho danh sách việc; ưu tiên popover một cột trên menu và route phiên hiện có. Không có file `web/src/app/…` để sửa.

**Test:** bổ sung `web/tests/hunt.test.ts`, test activity hiện có và mới `hunt-index.test.ts`:
thứ tự Recent/Guide, 0/1/nhiều phiên, lưu/khôi phục thu gọn, bước khớp T4 sau undo, project đúng ID, count không gồm đã loại;
fixture 6 việc/2 phiên, chat + tool không đếm hai lần, run dùng chung, việc ngoài hunt, phiên lưu trữ/ngoài top 20,
job hơn 24 giờ/ngoài 50 lượt, pending/running/done/error, polling/focus/mất mạng; bấm badge tới đúng session/candidate.
Kiểm tên dài, đủ thông tin từng dòng, Guide một cột, bàn phím và EN/VI ở 960px/1340px.

**Độ lớn:** L — phần đổi vị trí nhỏ; phần tổng hợp và đối soát hoạt động nhiều phiên cần API cùng quy tắc đếm thống nhất.

## Cách soát và bằng chứng hoàn tất khi triển khai

- Mỗi việc viết test hành vi nêu trên trong `web/tests/`, chạy bằng bộ test hiện có trước/sau thay đổi.
  Không dùng test chỉ dò chữ source để thay cho kiểm hành vi.
- Chạy `npm run check` ở gốc và `npm run docs:build`; kết quả phải xanh. Lượt viết plan chỉ chạy build tài liệu.
- Mở UI ở **960px và 1340px**, cả **EN và VI**: phiên rỗng, keyword/project/model dài, nhiều chip,
  từng trạng thái khoá bước, menu mở, tất cả hướng dẫn đóng rồi hiện lại, đang chạy, lỗi quota, Settings đổi tuyến.
- Kiểm không cuộn ngang cả trang; chỉ bảng được cuộn ngang. Menu một cột, chữ/lý do dài xuống dòng;
  vùng chat hẹp không che CTA, × có vùng bấm riêng, tooltip không bị cắt và focus không mất sau đóng.
- Chụp screenshot theo tên trạng thái + bề rộng + locale, **mở đọc từng ảnh**, ghi vị trí artifact và kết quả vào
  trang khi làm xong. Chưa có ảnh/đo thật thì ghi “chưa đo”, không gán tỷ lệ thành công hay thời gian giả.
- Với chính trang plan: mở bản MkDocs ở khoảng 1340px, kiểm một cột đọc từ trên xuống; bảng không ép chữ thành cột hẹp.

## Thứ tự làm đề xuất · độ lớn

1. **T2 — S:** đóng/mở hướng dẫn, ít phụ thuộc; giữ nguyên trạng thái lỗi và quyền.
2. **T4 — M:** chốt điều kiện bước và CTA để menu có nguồn điều kiện chung.
3. **T1 — L:** khảo sát metadata CLI trước, rồi danh tính/cache/Settings/session; đây là phần bất định lớn nhất.
4. **T5 — M:** dùng danh tính T1 cho component ✦ và chuyển các nút hiện có.
5. **T3 — M:** ghép danh mục thật, điều kiện T4, nhận diện T5 và ngữ cảnh đang chọn.
6. **T6 — L:** dùng parser T1 và điều kiện T4, bổ sung snapshot/vòng đời hoạt động rồi nối hai khung và chip.
7. **T7 — L:** dùng snapshot T6, bước T4 và cờ Guide T2; thống nhất đơn vị đếm menu/danh sách rồi soát toàn hành trình.
   Có thể đưa Recent lên trước Guide cùng T2, nhưng chưa coi T7 xong trước khi đối soát được badge.

S/M/L là độ lớn tương đối, **chưa đo thời gian**, không phải cam kết ngày công.

## Kết quả 2026-10-28

- **T1 danh tính:** khảo sát CLI thật — Claude Code 2.1.269 trả model ở `system/init.model` + `assistant.message.model`
  (vd `claude-haiku-4-5-20251001`); Codex 0.162.0 **không** có model trong `exec --json`, có ở dòng `turn_context` của file phiên
  `$CODEX_HOME/sessions/**/rollout-*-<thread_id>.jsonl` (vd `gpt-6.1-sol`). Sự kiện NDJSON mới `identity`; `lib/ai/identity.ts`
  cache bộ nhớ theo tuyến + model đã chọn; GET `/api/ai/chat` trả `identity`; header ghi "Claude Code · <model>" hoặc "model chưa rõ",
  phụ "đã chọn …" khi CLI chưa xác nhận; mỗi câu trả lời ghi model của lượt đó. Đổi Claude Code ↔ Codex thì không resume phiên CLI kia.
  Chạy thật trên bản sao DB: header nhận `claude-sonnet-4-6` sau lượt đầu. Chưa có icon hãng (chưa có asset được phép) — chỉ tên chữ.
- **T2 hướng dẫn:** `DismissibleNotice` + `lib/hunt-notices.ts` (localStorage `nr.hunt.dismissed.v1:<phiên|index>`, storage hỏng → bộ nhớ);
  đóng được lời chào chat, gợi ý lệnh, hướng dẫn `/find-niches`, banner xong flow; "Hiện lại hướng dẫn" ở ô chat. Lỗi, quyền, trạng thái không đóng được.
- **T3 lệnh AI:** `lib/hunt-commands.ts` là nguồn chung cho menu, gợi ý và slash máy chủ nhận (`HUNT_SKILLS`); test khớp đúng 5 thư mục skill thật.
  Menu "✦ Lệnh AI" (và gõ `/`): tên · làm gì · cần gì · lý do khoá · "Đưa vào ô chat · chưa chạy"; ↑ ↓ Enter Escape, Enter trong menu không gửi.
  Lệnh 1 keyword dùng ứng viên đang chọn kèm Research #id. Chạy thật: ↓×4 Enter → `/app-demand pomodoro timer for study offline (Research #44)`, 0 tin gửi.
- **T4 điều kiện bước:** `flowAccess()` chuỗi điều kiện theo bảng trên (lỗi không lọt qua health); thanh bước xám + lý do;
  "Sang bước n →" chỉ đổi thẻ; không tự nhảy thẻ khi dữ liệu cập nhật; nút chạy khoá khi bước chưa mở / AI đang chạy.
- **T5 ✦:** nút chạy AI ở Flow dùng variant `ai` + ✦ + tooltip "Dùng AI (<tên AI>)"; Tra nốt / Sang bước không mang ✦; nút Lệnh AI có ✦.
  Chưa chuyển hết các chỗ khác (AiRunButton, AskAi, AiSection) sang component chung.
- **T6 trạng thái:** `lib/hunt-activity.ts` + `HuntStatus` ở đầu Flow và dưới header chat: Rảnh (lần hoạt động cuối) · Đang trả lời · Đang làm việc
  (tool gần nhất + ứng viên đang tra n/t nguồn) · Lỗi · Mất kết nối (poll lỗi không còn bị nuốt). Đồng hồ theo mốc lượt, `role=status` chỉ đọc khi chữ đổi.
  Chạy thật: "Answering" → "Idle · last active 11:32 AM"; lỗi hiện ở cả hai chỗ.
- **T7 phiên gần đây:** Recent đứng trước Guide; Guide thu sẵn khi đã có phiên, bấm tay thì nhớ; mỗi dòng có Bước n/7 (cùng `flowState`),
  số ứng viên, Project #id, đang tra n (keyword) hoặc "không có việc đang tra · cập nhật …"; poll 3 giây khi có việc chạy; lỗi tải không thành "chưa có phiên".
  `listHunts` đọc thẳng `source_jobs`, không dựng RunView, không ghi điểm.
- **Chưa làm (ghi rõ):** registry chat phía server + vòng đời tool kết thúc (CLI không có sự kiện tool-end ổn định); đếm lại badge "n running" theo
  source job + nhóm theo phiên ở AppShell; ✦ cho mọi nút AI còn lại; icon hãng. Kiểm: 513 test xanh, xem 1340 + 960px EN.

## Rủi ro

- CLI đổi schema hoặc không xuất model: giữ fallback thật, fixture theo phiên bản; không đọc config bị argv bỏ qua.
- Session cũ/model cũ sau đổi Settings: revision và session theo tuyến, kiểm cả request xếp hàng và event đến muộn.
- Quy tắc `more` hiện suy từ timestamp, không chứng minh long-tail do đúng bước tạo; bản đầu ghi rõ giới hạn,
  không mở rộng migration theo dõi quan hệ ứng viên trong phase UX này.
- Ẩn nhầm cảnh báo hoặc menu xám không có lý do làm người dùng kẹt: luôn giữ lỗi/trạng thái tối thiểu, cách khôi phục,
  lối Research tay và link quay lại điều kiện thiếu.
- Danh sách skill/UI/backend lệch hoặc quyền thay đổi khi menu mở: một sổ lệnh, kiểm lại ở lúc gửi và server.

- CLI không có tool-end hoặc mất stream: không đoán tool còn chạy; giữ trạng thái chưa xác nhận, đối soát registry/DB.
  Không thay đổi ngầm hợp đồng hiện tại: ngắt kết nối có thể dừng chat, collector vẫn chạy riêng.
- Badge đổi đơn vị đếm, run dùng chung, việc ngoài hunt hoặc ngoài giới hạn truy vấn dễ làm tổng sai:
  dùng ID duy nhất và snapshot chung, hiển thị pending riêng, kiểm fixture đối soát toàn bộ danh sách.
- Query summary từng phiên có thể gây N+1 hoặc vô tình ghi score: đọc theo lô, không chạy collector/AI/tính score khi xem index.
- Poll lỗi/restart và updatedAt không phản ánh hoạt động CLI dễ gây “rảnh” giả: giữ observedAt riêng, hiện dữ liệu cũ rõ ràng.

## Câu hỏi còn mở cho người dùng

- Bản đầu chọn một lệnh rồi xem/sửa trước Gửi có đủ không, hay cần chọn nhiều lệnh và duyệt từng lượt? Đề xuất một lệnh.
- BEST được mở khi có một Research xong, hay phải đợi mọi ứng viên xong? Đề xuất mở sớm, ghi rõ phạm vi đã tra.
- Giữ thẻ hiện tại và bấm “Sang bước…” thay tự nhảy có hợp ý không? Đề xuất giữ thẻ để thao tác không bị dịch chuyển.
- Có bộ icon hãng đã được phép dùng không? Trong lúc chưa có, dùng tên chữ và dấu AI chung.

- Ngưỡng dữ liệu cũ 10 giây và poll 2 giây của T6 có phù hợp sau khi đo trên máy thật? Tạm dùng làm mặc định thiết kế,
  không coi là SLA hay bằng chứng đã đo.
- Guide tự thu khi có phiên và nhớ lựa chọn thủ công theo T2; có cần luôn mở cho người dùng cũ? Mặc định tự thu.
- Đơn vị badge đề xuất là source job + lượt chat, pending riêng; giữ cách đếm Research cũ sẽ không khớp yêu cầu thấy từng
  nguồn đang searching. Mặc định triển khai cách đếm mới T7 và giải thích ngay trong danh sách việc.

[← Phase 28.6 · AI Agent](phase-28-6-ai-agent.md) · [Mục lục Web](index.md)
