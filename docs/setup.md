# Setup máy

> Trang này mở được khi máy **chưa cài gì**. Tự đoán máy bạn (macOS / Windows · chip Apple / Intel) rồi hiện đúng bộ bước.
> Làm xong thì mở tool, vào **Thêm → Setup · kiểm tra máy** để tool tự kiểm từng mục.

<p id="setup-detect" class="setup-detect">Đang đoán máy của bạn…</p>

<div class="box box--goal" markdown>
**Cần gì.** Node.js LTS (bản **20.19** trở lên) + bộ dịch gói native (macOS: Command Line Tools · Windows: Build Tools).
Không cần tài khoản, không cần key. AI là tuỳ chọn.
</div>

<div class="setup-os" data-os="mac" markdown>

## macOS

1. **Command Line Tools** — mở Terminal, chạy `xcode-select --install`, bấm Cài. Đã có thì Terminal báo "already installed".
2. **Node.js LTS** — tải bộ cài `.pkg` ở [nodejs.org/en/download](https://nodejs.org/en/download):
    - Mac chip Apple (M1 trở lên): chọn **macOS Installer (ARM64)**
    - Mac chip Intel: chọn **macOS Installer (x64)**
3. **Kiểm** — mở Terminal mới, chạy `node -v`. Ra `v20.19` trở lên là được.
4. **Chạy tool** — trong thư mục Niche Radar bạn nhận được: `npm run setup` rồi `npm run dev`, mở `http://localhost:3200`.

</div>

<div class="setup-os" data-os="win" markdown>

## Windows

1. **Node.js LTS** — tải bộ cài `.msi` ở [nodejs.org/en/download](https://nodejs.org/en/download) (Windows Installer x64; máy ARM chọn ARM64).
   Ở bước "Tools for Native Modules", **tick** ô cài thêm công cụ dịch (tự cài Visual Studio Build Tools + Python).
2. **Kiểm** — mở PowerShell mới, chạy `node -v`. Ra `v20.19` trở lên là được.
3. **Chạy tool** — trong thư mục Niche Radar bạn nhận được: `npm run setup` rồi `npm run dev`, mở `http://localhost:3200`.

</div>

## Tool báo lỗi thì sao

| Báo | Làm |
|---|---|
| Không thấy lệnh `node` | Cài Node LTS ở trên, **mở Terminal mới** rồi thử lại |
| Node 18 / cũ hơn 20.19 | Cài lại Node LTS mới (đè lên bản cũ được) |
| `better-sqlite3` lỗi khi `npm run setup` | macOS: `xcode-select --install` · Windows: cài lại Node có tick "Tools for Native Modules" |
| Cổng 3200 đang bận | Chạy `PORT=3300 API_PORT=3301 npm run dev` |
| Google Play / Trends báo chặn tạm | Nguồn đó chặn vì gọi dồn — đợi 10–30 phút, nguồn khác vẫn dùng được |

Trong tool, mục nào lỗi có nút **Hỏi AI ▾** (ChatGPT · Claude · Gemini · Perplexity) với câu hỏi soạn sẵn — chỉ gửi hệ điều hành,
phiên bản và dòng lỗi, đã bỏ đường dẫn máy, tên user, key.

## AI (tuỳ chọn)

- Có gói **Claude**: cài [Claude Code](https://docs.claude.com/en/docs/claude-code/setup), chạy `claude` một lần để đăng nhập.
- Có gói **ChatGPT**: cài [Codex CLI](https://developers.openai.com/codex/cli), chạy `codex login`.
- Rồi chọn tuyến ở **Cài đặt → AI** trong tool. Không có AI, tool vẫn chạy đủ phần tra niche.
