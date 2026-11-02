# Backlog 26 · Extension Chrome "ShotMatic Lite"

> Extension miễn phí chạy ngay trên trang app của Google Play / App Store: kiểm nhanh keyword + niche, rồi kéo người
> dùng về shotmatic.app và bản tải về đầy đủ. Kèm một MCP bản nhẹ để người dùng hỏi bằng chính Claude.

<span class="chip chip--doing">Bản 0.1.0 xong 2026-11-01 · chạy thử trên trang Play + App Store thật · chờ tải lên Chrome Web Store</span>

## Vì sao

- Người làm app hay mở trang store để soi đối thủ → extension gặp họ đúng lúc đang tìm niche.
- Chrome Web Store là thêm một nơi để người ta tìm thấy ShotMatic (từ khoá "ASO", "keyword", "app niche").
- Phễu: extension (miễn phí, giới hạn) → shotmatic.app (UTM) → tải bản đầy đủ.

## Claude in Chrome có cắm thêm được không? → Không

- Anthropic không công bố API cho bên thứ ba cắm vào Claude in Chrome. Tìm ngày 2026-11-01, không có tài liệu chính thức.
- Chrome chỉ cho extension gọi sang nhau khi extension kia tự mở (`externally_connectable`). Claude in Chrome không mở.
- **Cách thay:** MCP. Claude in Chrome đọc trang store đang mở, MCP của mình trả số liệu niche. Hai cái chạy song song.
- **Chiều ngược lại thì được:** Claude Code (`claude --chrome`) chạy skill lái Chrome — xem skill `store-page-check` ở [Backlog 27](phase-backlog-27-youtube-chrome-skill.md).

## Khảo sát Chrome Web Store (2026-11-01)

| Extension | Làm gì | Store |
|---|---|---|
| Keywords Explorer For Google Play (ASO) | Báo cáo keyword trên trang app đang mở | Chỉ Play |
| Keyword Rank Checker — ASO Rank Tracker | Theo dõi hạng keyword | Cả 2 |
| App Review Analyzer — ASO Review Insights | Nhóm lời chê, ý keyword từ review, xuất CSV | Cả 2 |
| ASO Free Tool by AppTweak | Đổi nước / ngôn ngữ, mật độ keyword, dẫn về báo cáo AppTweak | Cả 2 |
| Appark | Tải review, theo dõi rating đối thủ | Chỉ Play |
| SEO \| ASO \| Search Ranking & Keyword Tool | Bảng keyword từ title, điểm độ khó lấy từ AppVector | Play |

- **Chữ chung của ngành:** ASO, keyword, rank, review, Google Play, App Store. Tên theo khuôn `<Tên> — ASO <việc làm>`.
- **Chỗ trống:** mỗi tool làm 1 việc nhỏ. Chưa thấy cái nào trả lời "**niche này có đáng làm app không**" (gộp review +
  Trends + mức đối thủ, cả 2 store), cũng chưa thấy cái nào làm việc cùng Claude.
- AppTweak đã dùng extension miễn phí dẫn về báo cáo trả phí → mô hình phễu này có người chạy rồi.
- Lượt cài, rating từng extension: `chưa đo`. Lúc làm phải mở từng trang store ghi lại kèm ngày.

Nguồn: [Keywords Explorer](https://chromewebstore.google.com/detail/keywords-explorer-for-goo/ijegkehhlkpmicapdfdjahdmpklimdmp) ·
[Keyword Rank Checker](https://chromewebstore.google.com/detail/keyword-rank-checker-%E2%80%94-as/jkhgjjpbggnckodpebkppofahapmeclh) ·
[App Review Analyzer](https://chromewebstore.google.com/detail/app-review-analyzer-%E2%80%94-aso/odejpbkodjiojbdabfdfidjcjgipdegm) ·
[ASO Free Tool by AppTweak](https://chromewebstore.google.com/detail/aso-free-tool-by-apptweak/dpabdkgciemdgjlpdlblcmhngdpcjhbl) ·
[Appark](https://chromewebstore.google.com/detail/appark-free-aso-tools-for/doffdbedgdhbmffejikhlojkopaleian) ·
[SEO | ASO | Search Ranking](https://chromewebstore.google.com/detail/seo-aso-search-ranking-ke/pjjlpohgclhhnmbjfhijoeikehadbohd)

## Tên + mô tả trên store (nháp)

- **Tên:** `ShotMatic Lite — ASO Keyword & App Niche Checker`
- **Mô tả ngắn (≤ 132 ký tự):** "Check any app niche on Google Play & App Store: keyword gaps, review complaints, trend — then go deeper in ShotMatic."
- Từ khoá cần có trong mô tả dài: ASO, app store keyword, google play keyword, app niche, app idea, competitor reviews.
  Trước khi chốt: đo lại bằng Google Autocomplete + Trends, ghi số + ngày.

## Bản 0.1.0 đã làm (2026-11-01)

Code ở folder `extension/` của repo (README trong đó có cách chạy thử + đóng gói). Test logic: `web/tests/extension-lite.test.ts`.

- **Card trên trang app** (Play + App Store): rating, số rating, ngày cập nhật, thể loại, keyword trong tên (App Store: thêm phụ đề,
  tên chỉ là thương hiệu thì đoán keyword từ phụ đề). Thu gọn thành nút nhỏ, nhớ qua các trang.
- **Niche check 5 lần/ngày, không server:** iTunes Search (10 app) + trang tìm kiếm Play (đọc 6 app đầu) → Worth a look / Think twice /
  Crowded kèm 3 lý do (ông lớn, app yếu hoặc bỏ rơi, app có đúng keyword trong tên). Ngưỡng là quy ước, không phải số đo.
  Chạy thử ngày 2026-11-01: một lần check mất khoảng 1 giây.
- **Ask Claude:** chép prompt (dữ liệu app + kết quả check) rồi mở claude.ai.
- **Popup** thanh công cụ: Niche check theo keyword gõ tay + chọn nước.
- **Mọi link** về shotmatic.app có UTM `utm_source=chrome_extension`, `utm_campaign=shotmatic_lite`, `utm_content=<chỗ bấm>`.
- **Chưa có:** lời chê từ review 1–2★ (RSS review App Store đã chết, Play cần API riêng) → để bản đầy đủ; link `shotmatic://`; MCP bản nhẹ.

## Plan ban đầu (giữ để so)

1. **Thẻ nhanh trên trang app:** rating, số review, lần cập nhật cuối, keyword nằm trong title.
2. **Niche check lite:** vài lần mỗi ngày (số lần chưa chốt) → kết luận ngắn Đáng thử / Cân nhắc / Bỏ + 3 lời chê nổi nhất.
3. **Hỏi Claude:** chép sẵn prompt + dữ liệu trang; nếu người dùng đã thêm MCP thì Claude tự gọi tool.
4. **Mọi kết quả có nút "Xem đầy đủ"** → shotmatic.app kèm UTM; nếu máy đã cài bản đầy đủ thì mở thẳng bằng link `shotmatic://` (bản tải về chưa đăng ký link này, phải thêm trước).

Để dành cho bản đầy đủ: theo dõi niche lâu dài, so sánh nhiều niche, lịch sử, Export niche research, AI Agent.

## Làm được không (soát 2026-11-01)

- **Thẻ nhanh:** được. Content script đọc thẳng trang `play.google.com/store/apps` và `apps.apple.com`, không cần server.
  Rủi ro: Google / Apple đổi giao diện trang là phải sửa lại chỗ đọc.
- **Niche check lite:** được, nhưng phải gọi thêm kết quả tìm kiếm của store từ service worker của extension
  (App Store có iTunes Search API công khai, Play thì đọc trang tìm kiếm). Google Trends không có API công khai →
  bản đầu bỏ Trends, hoặc phải đi qua server của mình.
- **Hỏi Claude:** được. Chép prompt chỉ là clipboard. Phần MCP làm riêng.
- **Link `shotmatic://`:** chưa làm được ngay vì bản tải về chưa đăng ký link này.
- **Duyệt store:** phải ghi rõ trong mục quyền riêng tư là extension đọc trang store; chỉ xin quyền đúng 2 domain store.

## MCP bản nhẹ

- Tách từ MCP chỉ đọc đang có (`web/src/mcp/`), chạy trên mạng để thêm vào Claude dưới dạng connector.
- Chỉ vài tool đọc (kiểm niche, keyword của 1 app); câu trả lời có link về shotmatic.app.
- Cần quyết: ai trả tiền chạy server, giới hạn lượt gọi, có bắt email không.

## Đo gì

- Lượt cài extension, lượt bấm "Xem đầy đủ" (UTM trên shotmatic.app), lượt tải bản đầy đủ đến từ UTM này.
- Chưa có số mốc: `chưa đo`.

## Câu hỏi còn mở

Đã chốt ở bản 0.1.0: không server, Trends để bản đầy đủ, code ở `extension/`, 5 lượt/ngày.


- Extension lấy số ở đâu: đọc thẳng trang đang mở, hay gọi server của mình (tốn tiền, cần giới hạn)?
- Code extension để ở folder nào (thêm folder mới thì sửa README, `CLAUDE.md`, `docs/cach-dung.md` cùng lúc).
- Có cần bản Firefox / Edge không.
- Lúc làm thì tách thành phase có số, xếp vào thứ tự chung.
