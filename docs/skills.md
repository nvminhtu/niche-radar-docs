# Skills (App AI Skills)

Bộ skill Claude Code của pipeline **App AI Skills** — làm app bán subscription từ ý tưởng tới store.
Niche Radar là tool research đứng đầu pipeline (`app-research`, `app-demand`, `best-app`).

Cài: chép thư mục skill cần dùng vào `~/.claude/skills/` (hoặc `.claude/skills/` của repo).
Nhiều skill gọi script `scripts/*.py` của repo pipeline (chưa public) — phần phương pháp trong `SKILL.md`
và `references/` vẫn đọc và áp dụng được.

- **[app](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app)** — Router của pipeline làm app bán subscription cho người KHÔNG biết code
- **[app-build](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-build)** — Bước 6 của pipeline app
- **[app-demand](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-demand)** — Skill lớn research NHU CẦU trước khi làm app, mục tiêu đo được: ra mắt là có người mua ngay (ít nhất tải trial).
- **[app-design](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-design)** — Bước 4 của pipeline app
- **[app-feature](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-feature)** — Thêm một tính năng mới vào app đã có (ngoài MVP đã duyệt, thường sau khi ra mắt): tạo file việc trong apps/ACTIVE/<slug>/plan/ (feature, qua scripts/app.py change), viết yêu cầu thành tiêu chí nghiệm thu kiểm được, ki…
- **[app-fix](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-fix)** — Sửa lỗi trong app một cách có hệ thống cho người không biết code: tạo file việc trong apps/ACTIVE/<slug>/plan/ (fix, qua scripts/app.py change), TÁI HIỆN lỗi trước (các bước, thiết bị, log crash qua run_app.py logs, C…
- **[app-flutter](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-flutter)** — Skill phụ nhánh Flutter (mặc định) của pipeline app
- **[app-geo](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-geo)** — Skill phụ GEO + AEO cho Google (và AI search)
- **[app-grow](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-grow)** — Bước 13 của pipeline app
- **[app-gtm](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-gtm)** — Marketing từ số 0 cho indie (go-to-market, GTM)
- **[app-indie](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-indie)** — Skill phụ của pipeline app
- **[app-listing](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-listing)** — Bước 10 của pipeline app
- **[app-mac-landing](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-mac-landing)** — Skill nhánh macOS cho landing page
- **[app-macos](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-macos)** — Skill nhánh macOS của pipeline app
- **[app-macos-listing](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-macos-listing)** — Bước 10 nhánh macOS
- **[app-marketing](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-marketing)** — Bước 12 của pipeline app
- **[app-mockup](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-mockup)** — Bước 4b của pipeline app
- **[app-money](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-money)** — Bước 2 của pipeline app
- **[app-native](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-native)** — Skill phụ nhánh Native của pipeline app
- **[app-paywall](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-paywall)** — Skill phụ subscription của pipeline app
- **[app-plan](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-plan)** — Variant của core:mvp-plan cho app
- **[app-progress](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-progress)** — Sinh lại và kiểm progress.json của repo App (bảng Relay đọc để biết app nào đang ở bước nào trong 15 bước).
- **[app-publish](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-publish)** — Bước 11 của pipeline app
- **[app-reddit](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-reddit)** — Skill phụ của bước 12 (marketing) và app Promo Desk
- **[app-release](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-release)** — Bước 9 của pipeline app
- **[app-research](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-research)** — Bước 1 của pipeline app
- **[app-review](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-review)** — Bước 8 của pipeline app và CỔNG 4
- **[app-run](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-run)** — Bước 7 của pipeline app
- **[app-scaffold](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-scaffold)** — Bước 5 của pipeline app
- **[app-setup](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-setup)** — Bước 0 của pipeline app
- **[app-spec](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-spec)** — Bước 3 của pipeline app
- **[app-store-art](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-store-art)** — Skill phụ của bước 10 (listing) và 12 (marketing)
- **[app-video](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-video)** — Skill phụ của bước 10–13
- **[app-youtube-channel](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-youtube-channel)** — Skill phụ marketing
- **[app-youtube-upload](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/app-youtube-upload)** — Skill phụ marketing
- **[best-app](https://github.com/nvminhtu/niche-radar-docs/tree/main/skills/best-app)** — Skill research ƯU TIÊN SỐ 1 của repo
