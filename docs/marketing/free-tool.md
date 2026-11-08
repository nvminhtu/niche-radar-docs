# Free tool trên shotmatic.app

> Free tool thường kéo traffic nhanh hơn blog, vì người ta tìm "X checker / X generator" rất nhiều, và trang tool tự có
> backlink. Logic đã chạy được trong 2 extension, chỉ cần đưa lên web.

<span class="chip chip--doing">Đã lên [App Idea Checker](https://shotmatic.app/app-idea-checker) 2026-11-07 · chưa có số đo · chi tiết ở [Audit](audit-2026-11-07.md)</span>

<div class="box box--goal" markdown>
**Đích**

- **1 tool** chạy trên shotmatic.app, tên đúng cụm người ta gõ.
- Đếm được tool ra bao nhiêu lượt tải.

**Xong khi:** tool live · event `tool_run` và `store_click` / `download` hiện trong GA4.
</div>

## Việc

- [ ] Chọn **1 tool** để làm trước (anh chốt). Ứng viên:
    - **Niche check** bản web (giống extension ShotMatic Lite: tra iTunes Search + app đầu Google Play → Worth a look / Think twice / Crowded)
    - **App Store keyword difficulty checker** (đã có bài `app-store-keyword-difficulty-without-search-volume`)
    - **Amazon keyword → app idea** (giống extension ShotMatic Scout)
- [ ] Đo từ khoá cho tên tool trước khi làm (gợi ý Google + Trends, xem [Google Search Suggestion](google-search-suggestion.md))
- [ ] Giới hạn lượt tra / ngày để không lộ hết sức mạnh bản đầy đủ, cuối kết quả có nút tải ShotMatic
- [ ] Gắn event GA4 `tool_run` và `store_click` / `download`

## Liên quan

[Backlog 26 · Extension Chrome Lite](../web/phase-backlog-26-chrome-extension-lite.md) ·
[Backlog 28 · Extension Chrome Amazon](../web/phase-backlog-28-chrome-extension-amazon.md) ·
Skill: `marketing-skills:free-tools`
