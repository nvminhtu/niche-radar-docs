# Phase 28.19 · AI Agent full flow — chọn account + AI chạm toàn app

> Hôm nay ShotMatic gọi `claude` với cấu hình mặc định của máy (`~/.claude`). Muốn dùng account Claude khác phải tự mở Terminal
> đăng xuất rồi đăng nhập lại — và việc đó đổi luôn account của mọi cửa sổ Claude Code trên máy. Hết lượt giữa phiên thì AI Agent
> dừng, không có đường đi tiếp. AI cũng mới chạm được Research, Explore, Project, Gap — chưa chạm Compare, Theo dõi, Export.
> Phase này nối đủ vòng: **nối AI → chọn account → ra lệnh → app làm → tài liệu mang đi**.

<span class="chip chip--todo">Plan 2026-10-31 · chưa làm</span>

Sơ đồ toàn app + sơ đồ AI Agent: [Sơ đồ ShotMatic](../so-do-app.md).

## Mục tiêu · cần làm · KHÔNG làm

- **Mục tiêu:** trong Cài đặt → AI thấy rõ **đang dùng account nào** (email · gói), đổi hoặc thêm account bằng 1 nút, hết lượt
  thì 1 bấm chuyển sang account khác rồi chạy tiếp; AI Agent ra lệnh được cho mọi màn chính.
- **Cần làm:** M1 account · M2 hết lượt → đổi account · M3 tool MCP cho màn còn thiếu · M4 chạy thật + soát.
- **KHÔNG làm:**
    - Không đọc, chép, lưu token / mật khẩu: đăng nhập vẫn do chính CLI làm trong cửa sổ Terminal + trình duyệt.
    - Không tự đổi account khi người dùng chưa bấm (chỉ gợi ý).
    - Không chạy 2 account song song trong 1 lượt, không chia việc giữa các account.
    - Không đụng account của Claude Desktop hay các cửa sổ Claude Code khác trên máy (account thêm sống ở thư mục riêng).
    - Không thêm tuyến AI mới, không đổi giá / Free / PRO.

## Cách đổi account hôm nay (chưa có phase này)

1. Mở Terminal, chạy `claude auth logout`, rồi `claude auth login` → trình duyệt mở, chọn account Claude kia.
2. Quay lại Cài đặt → AI: dòng "Sign in to Claude plan" tự đổi email trong khoảng 30 giây → bấm **Test**.

Lưu ý: cách này đổi account cho **mọi** Claude Code dùng `~/.claude` trên máy. Muốn giữ cả hai thì dùng thư mục cấu hình riêng
(`CLAUDE_CONFIG_DIR`) — chính là việc M1 làm trong app.

## M1 · Chọn account

| | Việc | Xong khi |
|---|---|---|
| A | Danh sách account cho Claude Code: **Mặc định** (`~/.claude`) + account thêm, mỗi account một thư mục riêng trong thư mục dữ liệu của app. Mỗi dòng: tên tự đặt · email · gói (đọc `claude auth status` với `CLAUDE_CONFIG_DIR` của dòng đó) | thấy 2 dòng 2 email khác nhau |
| B | Nút **+ Thêm account** → mở Terminal chạy `CLAUDE_CONFIG_DIR=<thư mục> claude auth login`; trang tự dò tới khi đăng nhập xong | thêm được account thứ 2 không đụng account mặc định |
| C | Nút **Đổi account** ở từng dòng (đăng xuất + đăng nhập lại đúng thư mục đó) · **Bỏ** account thêm (xoá thư mục, có hỏi lại) | đổi xong dòng hiện email mới |
| D | Chọn **account đang dùng**: mọi lần gọi CLI (nút AI, Hỏi AI, AI Agent, Test) truyền `CLAUDE_CONFIG_DIR` của account đó; dòng "In use" ghi thêm tên account | nhật ký AI ghi đúng account |
| E | Codex làm y hệt bằng `CODEX_HOME` (cùng giao diện) | 2 account Codex chạy được |

## M2 · Hết lượt → đổi account

| | Việc | Xong khi |
|---|---|---|
| A | Lỗi `limit` / `login` khi chạy (đã nhận ra ở `cli.ts`) → thanh báo trong khung chat: "Account 1 hết lượt — chuyển sang Account 2 rồi chạy lại?" | thấy thanh báo khi giả lập hết lượt |
| B | Bấm → đổi account đang dùng + chạy lại đúng lượt vừa hỏng; phiên AI Agent bắt đầu phiên CLI mới, ngữ cảnh lấy lại từ nhật ký phiên săn | phiên đi tiếp, không mất bước |
| C | Không còn account nào → chỉ chỗ đăng nhập lại / giờ hết hạn mức nếu CLI báo | không kẹt im lặng |

## M3 · AI chạm các màn còn thiếu

Gom phần còn lại của [Backlog 25](phase-backlog-25-mcp-write-rest.md) vào đây, chỉ những tool AI Agent cần để đi hết vòng:

| Tool | Mức | Làm gì |
|---|---|---|
| `compare_niches` | đọc | so 2–4 niche / project, trả bảng như tab Compare |
| `start_tracking` | thêm | bật theo dõi định kỳ cho niche đã giữ |
| `export_pack` | đọc | trả gói LLM / bộ Brief · Spec · Plan của phiên để AI tóm tắt hoặc mang đi |
| `health_niche_check` | nhóm việc | tra nốt + chấm sức khoẻ một danh sách niche trong 1 lệnh |

Tool ghi vẫn sau công tắc "Cho AI thêm dữ liệu", hoàn tác được, máy chủ kiểm Free / PRO như giao diện.

## M4 · Chạy thật + soát

- Claude Code thật, 2 account: thêm account 2 → chọn → AI Agent chạy hết 7 bước → giả lập hết lượt → đổi account → chạy tiếp.
- Codex thật 1 lượt với `CODEX_HOME` riêng.
- Test: `claude auth status` theo từng thư mục, env truyền đúng vào mọi lần gọi CLI, thanh báo hết lượt.
- 960px + 1340px, English + tiếng Việt, không cuộn ngang. `npm run check` xanh.
