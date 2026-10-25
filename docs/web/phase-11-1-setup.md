# Phase 11.1 · Setup ngay trong Web / App

> Máy người dùng có thể **thiếu đồ cài** (Node, gói dịch, Ollama, key AI…). Thay vì bắt đọc README, tool có sẵn
> **trang Setup**: hướng dẫn đúng máy đó, **nút Kiểm tra máy** báo cái gì đủ / thiếu, kèm **gói cài phù hợp**.
> Kẹt chỗ nào thì có nút nhỏ **Hỏi AI** — xổ ra ChatGPT · Gemini · Claude · Perplexity, câu hỏi soạn sẵn.

<span class="chip chip--todo">Chưa làm · sau Phase 11</span>

## Chạy thế nào

```mermaid
flowchart LR
  O[Mở trang Setup] --> D[Nhận diện máy<br/>macOS / Windows · chip]
  D --> G[Hướng dẫn đúng máy<br/>+ gói cài phù hợp]
  G --> C[Bấm Kiểm tra máy]
  C --> R{Từng mục}
  R -->|đủ| OK[✓ xanh]
  R -->|thiếu / sai bản| FX[Cách sửa 1 dòng<br/>+ link gói cài]
  FX --> AI[Hỏi AI ▾<br/>ChatGPT · Gemini · Claude · Perplexity]
  FX --> C
  OK --> GO[Bắt đầu tra niche đầu tiên]
```

## Hai lớp — vì máy chưa có Node thì web local chưa chạy được

| | |
|---|---|
| :material-file-document-outline: **Lớp 1 · Trang Setup tĩnh** | nằm trên trang docs / landing — mở được khi máy **chưa cài gì**; tự nhận macOS / Windows, chip Apple / Intel; hiện đúng bộ bước + link gói cài cho máy đó |
| :material-stethoscope: **Lớp 2 · Kiểm tra máy trong tool** | trang `/setup` trong bản Web; server đọc phiên bản thật trên máy và trả từng mục đủ / thiếu |
| :material-apple: **App Mac** | làm ở [Phase 55b](../app/phase-55b-app-only.md) (sau khi hết phase Web): Node + SQLite đã gói sẵn → chỉ kiểm phần **tuỳ chọn** (key AI, Ollama, Claude in Chrome) |

## Mục kiểm

**Bắt buộc (bản web)**

- **Node.js** — kiểm `node -v` ≥ 20.19 (Vite 8 đòi) · thiếu thì link bộ cài Node LTS đúng máy
- **npm** — kiểm `npm -v` · đi kèm Node
- **Gói dịch native (better-sqlite3)** — mở thử DB SQLite · macOS: `xcode-select --install`, Windows: Build Tools
- **Cổng 3200 / 3201** — cổng còn trống · bận thì đổi `PORT=… API_PORT=…`
- **Mạng tới Google Play / App Store / Trends** — gọi thử 1 lượt nhỏ mỗi nguồn · báo nguồn nào bị chặn, đợi 10–30 phút

**Tuỳ chọn**

- **Key Claude API** — gọi thử 1 câu rẻ nhất · dẫn sang Cài đặt AI (Phase 6)
- **Ollama** — `127.0.0.1:11434` trả lời + có model · link tải Ollama + lệnh `ollama pull`
- **Claude in Chrome** — chỉ hướng dẫn (tool không đọc được trình duyệt) · link cài extension

## Làm gì

| | |
|---|---|
| :material-monitor-cellphone: **Nhận diện máy** | hệ điều hành + chip từ trình duyệt (lớp 1) hoặc server (lớp 2) — không hỏi người dùng |
| :material-package-down: **Gói cài phù hợp** | mỗi mục thiếu có đúng 1 link chính chủ cho máy đó (nodejs.org, ollama.com…), không gói lại đồ người khác |
| :material-check-decagram: **Nút Kiểm tra máy** | API `GET /api/setup/check` → danh sách mục `ok / thiếu / sai bản` + 1 dòng cách sửa; bấm lại sau khi cài |
| :material-robot-outline: **Hỏi AI ▾** | nút nhỏ cạnh mỗi mục lỗi; bấm xổ ra ChatGPT · Gemini · Claude · Perplexity, mở tab mới với câu hỏi soạn sẵn (máy, phiên bản, dòng lỗi) |
| :material-content-copy: **Copy câu hỏi** | AI nào không nhận câu hỏi qua link (Gemini) → copy sẵn vào clipboard rồi mở trang |
| :material-shield-lock-outline: **Che dữ liệu riêng** | câu hỏi gửi AI chỉ có OS, phiên bản, dòng lỗi — **bỏ** đường dẫn máy, tên user, key |

## Nút Hỏi AI — trông thế nào

- Nút nhỏ `Hỏi AI ▾` ở cuối dòng lỗi, không che nội dung.
- Bấm → menu dọc 4 dòng, mỗi dòng logo + tên. Bấm lại hoặc bấm ra ngoài thì đóng.
- Câu hỏi mẫu: *"Tôi dùng macOS 15 chip Apple. Cài Niche Radar báo: `<dòng lỗi>`. Node hiện tại 18.20. Sửa thế nào, từng bước?"*
- Dùng chung một component `AskAi` để Phase 11.2 và các trang lỗi khác gắn lại được.

<div class="box box--star" markdown>
**Xong khi**

- Máy Mac sạch (chưa Node) mở trang Setup tĩnh → làm theo → chạy được tool, không cần đọc README
- Kiểm tra máy báo đúng 3 tình huống thật: thiếu Node · Node cũ · thiếu Command Line Tools
- Nút Hỏi AI mở đủ 4 AI, câu hỏi không chứa đường dẫn máy / key
- Screenshot trang Setup + menu Hỏi AI đã Read
</div>

<div class="box box--danger" markdown>
**Không làm**

- Tự cài hộ (chạy installer, `sudo`) — chỉ hướng dẫn + kiểm
- Gọi API của ChatGPT / Gemini trong tool — chỉ mở trang web của họ
- Linux — khi có người dùng xin
</div>
