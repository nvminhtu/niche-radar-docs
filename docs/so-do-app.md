---
hide:
  - navigation
  - toc
---

# Sơ đồ ShotMatic

> Hai sơ đồ, trang rộng hết màn hình: **① toàn app** (mọi phần chạy trong máy bạn) và **② AI Agent** (AI bấm nút thay
> người dùng qua MCP). Cập nhật 2026-10-31. Plan phần còn thiếu của AI Agent: [Phase 28.19](web/phase-28-19-ai-agent-full-flow.md).

## ① Toàn app

Tất cả chạy **trong máy**: giao diện → máy chủ nhỏ (chỉ nghe `127.0.0.1`) → các nguồn công khai → một file SQLite.
AI là tầng tuỳ chọn (⑤) — tắt AI thì mọi số vẫn có, chỉ mất phần đọc + viết hộ.

```mermaid
flowchart TB
  subgraph IN[" ① Cửa vào — người dùng mở "]
    direction LR
    MAC[App Mac / Windows<br/>Tauri bọc Web]
    WEB[Web<br/>localhost:3200]
    MAC ~~~ WEB
  end

  subgraph UI[" ② Giao diện React — cùng một code cho Web và App "]
    direction LR
    HOME[Research /r<br/>gõ niche → app,<br/>keyword, trend]
    EXP[Explore<br/>cây long-tail]
    PRJ[Projects<br/>gom niche ·<br/>bàn quyết định]
    GAP[Gap<br/>Reddit · Q&A ·<br/>GitHub · lời chê]
    CMP[Compare<br/>niche · project ·<br/>đối thủ]
    HUNT[AI Agent /hunt<br/>chat ra lệnh,<br/>app làm]
    SET[Cài đặt AI ·<br/>Quick Setup ·<br/>License PRO]
    HOME ~~~ EXP ~~~ PRJ ~~~ GAP ~~~ CMP ~~~ HUNT ~~~ SET
  end

  subgraph SRV[" ③ Máy chủ Hono — chỉ nghe 127.0.0.1 "]
    direction LR
    API[API /api/*<br/>kiểm Free / PRO]
    COL[Collectors<br/>hẹn giờ · thử lại ·<br/>cache 24h]
    AIL[Lớp AI<br/>chọn tuyến ·<br/>đếm token]
    BR[Cầu MCP<br/>port + token]
    API ~~~ COL ~~~ AIL ~~~ BR
  end

  subgraph SRC[" ④ Nguồn công khai, miễn phí "]
    direction LR
    GP[Google Play]
    AS[App Store]
    GS[Google gợi ý<br/>+ Trends]
    RD[Reddit · SE ·<br/>HN · GitHub]
    TM[TrustMRR]
    GP ~~~ AS ~~~ GS ~~~ RD ~~~ TM
  end

  DB[("④ niche.db<br/>SQLite trong máy")]

  subgraph AI[" ⑤ AI của người dùng — tuỳ chọn "]
    direction LR
    CLI[Gói AI trên máy<br/>Claude Code · Codex ·<br/>Gemini CLI — không key]
    KEY[Key riêng<br/>Claude · OpenAI · Gemini<br/>trả theo lượt, có trần]
    OFF[Tắt AI<br/>file job → Claude in<br/>Chrome → nhập lại]
    MCP[niche-radar MCP<br/>đọc mọi dữ liệu ·<br/>ghi qua máy chủ]
    CLI ~~~ KEY ~~~ OFF ~~~ MCP
  end

  subgraph OUT[" ⑥ Mang đi "]
    direction LR
    EXPT[Export CSV ·<br/>JSON · gói LLM]
    DOCS[Brief · Spec · Plan .md<br/>mang đi build app]
    BAK[Backup /<br/>restore]
    EXPT ~~~ DOCS ~~~ BAK
  end

  IN --> UI
  UI -->|gọi /api| SRV
  SRV -->|collector tra| SRC
  SRV <-->|đọc / ghi| DB
  SRV <-->|câu hỏi + MCP| AI
  SRC ~~~ AI
  DB -->|xuất ra| OUT
  AI ~~~ OUT
```

**Đọc sơ đồ:** đọc từ trên xuống: ① mở app → ② bấm trên giao diện → ③ máy chủ chạy → ④ lấy số từ nguồn, lưu SQLite → ⑤ nhờ AI nếu bật → ⑥ mang kết quả đi. Mọi ghi vào dữ liệu — kể cả do AI — đều đi qua
máy chủ (cùng hàm kiểm với giao diện), MCP không tự ghi SQLite.

## ② AI Agent — từ lúc nối AI tới bộ tài liệu

Ba chặng: **⓪ nối AI** (cài · đăng nhập · chọn account · thử 1 câu) → **① research niche** → **② lên kế hoạch app**.
Mỗi lượt chat: app gọi CLI của người dùng kèm MCP → AI gọi tool → máy chủ chạy collector thật → giao diện đổi theo.

```mermaid
flowchart TB
  subgraph S0[" ⓪ Nối AI — Cài đặt → AI hoặc Quick Setup "]
    direction LR
    I1[Cài CLI<br/>Claude Code · Codex] --> I2[Đăng nhập<br/>claude auth login]
    I2 --> I3{Dùng account nào?<br/>Mặc định · Account 2…}
    I3 --> I4[Thử 1 câu<br/>nút Test]
    I4 --> READY([AI sẵn sàng ✓])
  end

  subgraph TURN[" Mỗi lượt chat — app làm thay người dùng "]
    direction LR
    Q[Người dùng gõ<br/>ý tưởng / lệnh /<br/>bấm nút bước] --> CTX[App ghép câu gửi<br/>+ ngữ cảnh phiên<br/>+ luật Tuỳ chỉnh]
    CTX --> RUN[Chạy CLI<br/>claude -p --mcp-config<br/>bằng account đang chọn]
    RUN --> T{AI gọi<br/>tool MCP}
    T -->|đọc| RT[get_research · get_explore<br/>get_project · get_gaps<br/>get_app_context …]
    T -->|ghi — khi bật<br/>Cho AI thêm dữ liệu| WT[propose_candidates<br/>start_research · keep / drop<br/>add_project_note …]
    WT --> SV[Máy chủ ShotMatic<br/>kiểm token + Free / PRO<br/>→ collector tra số thật]
    SV --> DBX[(niche.db)]
    RT --> DBX
    DBX --> LIVE[Màn hình đổi theo<br/>+ AI trả lời có<br/>mã Research #id]
  end

  subgraph ERR[" Khi lỗi giữa chừng "]
    direction LR
    E1[Hết lượt / đăng nhập<br/>bị thu hồi] --> E2[Thanh báo: đổi sang<br/>account khác?] --> E3[Chạy lại đúng<br/>lượt vừa hỏng]
  end

  subgraph S1[" ① Research niche — 4 bước, mỗi bước 1 lượt chat "]
    direction LR
    F1[Tìm niche<br/>5–8 keyword] --> F2[AI Suggest<br/>giữ 3 tốt nhất] --> F3[Collect thêm<br/>long-tail] --> F4[Health check<br/>BUILD / TEST THÊM / BỎ]
  end

  subgraph S2[" ② Lên kế hoạch app — 3 tài liệu "]
    direction LR
    D1[BRIEF<br/>vấn đề + tính năng] --> D2[SPEC<br/>màn hình · Free / Pro] --> D3[PLAN<br/>việc theo mốc] --> D4[Tải bộ .md<br/>mang đi build]
  end

  S0 --> TURN
  TURN -.->|lỗi| ERR
  ERR -.-> TURN
  TURN --> S1
  S1 --> S2
```

**Đã có:** chat ra lệnh, 7 bước 2 chặng, tool đọc + ghi, Hồ sơ app cho người đã có app (Phase 28.6 → 28.18).
**Còn thiếu:** chọn / đổi account ngay trong app, tự gợi ý đổi account khi hết lượt, AI chạm tới các màn còn lại
(Compare, Theo dõi, Export) — plan ở [Phase 28.19](web/phase-28-19-ai-agent-full-flow.md). Trong sơ đồ, ô
**Dùng account nào?** và khối **Khi lỗi giữa chừng** là phần của 28.19, hôm nay app luôn dùng account mặc định của máy.
