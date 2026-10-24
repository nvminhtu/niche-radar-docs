# Atlas — landing page của app Mac native (awesome-native-macosx-apps)

Nguồn danh sách: [open-saas-directory/awesome-native-macosx-apps](https://github.com/open-saas-directory/awesome-native-macosx-apps)
(README lấy ngày **2026-10-03**, 201 link duy nhất: 172 trang web riêng + 29 repo GitHub). Danh sách này chọn app **native**
(Swift/SwiftUI/AppKit, không Electron) — đúng loại app nhánh `stack: macos` của repo làm ra.

## Trạng thái soi — đọc trước khi dùng bảng

- **Ngày 2026-10-03 chưa soi được trang nào**: mạng của môi trường cloud chặn mọi host ngoài danh sách cho phép
  (proxy trả 403 cho cả 172 trang). Chỉ `developer.apple.com` vào được → cột **Giải** đã đối chiếu nguồn thật.
- Cột **Layout / Theme** có dấu `?` = **gợi ý chưa soi** (16 trang có nhận diện rất rõ) hoặc chưa biết (`?` trơn).
  Không dùng ô có `?` làm bằng chứng; muốn học một trang → soi nó trước.
- Soi lại: `python3 scripts/landing_atlas.py` (máy Mac của người dùng hoặc môi trường có mạng) → Read
  `research/<ngày>-mac-landing-atlas/shots/*.png` → sửa ô Layout/Theme (bỏ `?`) + cột **Soi** = ngày.
- Repo GitHub (cột Soi = `repo GitHub`) không có landing riêng → mặc định `docs`; không phải mẫu để bán app trả phí.

## Giải đã kiểm nguồn

| App | Giải | Nguồn |
|---|---|---|
| Things 3 | Apple Design Award 2017 (winner) | [TidBITS 2017-06-08](https://tidbits.com/2017/06/08/apple-announces-2017-apple-design-award-winners/), [9to5Mac](https://9to5mac.com/2017/06/07/2017-apple-design-award-winners/) |
| Bear | Apple Design Award 2017 (winner) | như trên |
| Craft | ADA 2021 finalist | [developer.apple.com/design/awards/2021](https://developer.apple.com/design/awards/2021/) (đọc 2026-10-03) |
| Nova (Panic) | ADA 2021 finalist | như trên |
| Copilot Money | ADA 2024 finalist | [developer.apple.com/design/awards/2024](https://developer.apple.com/design/awards/2024/) |
| iA Writer | ADA 2025 finalist — Interaction | [developer.apple.com/design/awards/2025](https://developer.apple.com/design/awards/2025/) |
| Pixelmator Pro | Mac App of the Year 2018 (không phải ADA) | [Pixelmator blog 2018-12-04](https://www.pixelmator.com/blog/2018/12/04/pixelmator-pro-is-the-mac-app-of-the-year/) |

Ghi giải lên landing của **mình** chỉ khi app mình thật sự được giải (check_landing.py bắt Proof có link nguồn).
Giải của app mẫu chỉ để biết trang nào đáng học trước.

## Thứ tự nên soi trước (khi mạng mở)

1. Có giải: Things · Bear · Craft · Nova · Copilot Money · iA Writer · Pixelmator Pro.
2. App trả phí bán trực tiếp, trang tự làm (đúng hoàn cảnh app mình): CleanShot X · DaisyDisk · Proxyman · TablePlus ·
   Mimestream · Soulver · Hazel · Little Snitch · Bartender · iStat Menus · Fantastical · Raycast · Ulysses · Paste.
3. Indie nhỏ một người làm (gần cỡ app mình nhất): One Thing · Lungo · Hand Mirror · Tot · Gifox · Pika · Shottr · Xnapper.

## Bảng

| Nhóm | App | URL | Giá | Giải (đã kiểm nguồn) | Layout | Theme | Soi |
|---|---|---|---|---|---|---|---|
| Analytics & Monitoring | iStat Menus | https://bjango.com/mac/istatmenus/ | Paid | — | ? | ? | chưa |
| Analytics & Monitoring | Stats | https://github.com/exelban/stats | Free · Open Source | — | docs? | utility? | repo GitHub |
| Analytics & Monitoring | Usage | https://usage.pro | Freemium | — | ? | ? | chưa |
| System Utilities | AlDente | https://github.com/AppHouseKitchen/AlDente-Charge-Limiter | Freemium · Open Source | — | docs? | utility? | repo GitHub |
| System Utilities | AppCleaner | https://freemacsoft.net/appcleaner/ | Free | — | ? | ? | chưa |
| System Utilities | ClearDisk | https://github.com/bysiber/cleardisk | Free · Open Source | — | docs? | utility? | repo GitHub |
| System Utilities | coconutBattery | https://www.coconut-flavour.com/coconutbattery/ | Free | — | ? | ? | chưa |
| System Utilities | DaisyDisk | https://daisydiskapp.com/ | Paid | — | ? | ? | chưa |
| System Utilities | DisplayBuddy | https://displaybuddy.app/ | Paid | — | ? | ? | chưa |
| System Utilities | Endurance | https://enduranceapp.com/ | Paid | — | ? | ? | chưa |
| System Utilities | EtreCheck | https://etrecheck.com/ | Free | — | ? | ? | chưa |
| System Utilities | LinearMouse | https://linearmouse.app | Free · Open Source | — | ? | ? | chưa |
| System Utilities | Lungo | https://sindresorhus.com/lungo | Paid | — | icon? | native-light? | chưa |
| System Utilities | Mole | https://mole.fit/ | Paid | — | ? | ? | chưa |
| System Utilities | MonitorControl | https://github.com/MonitorControl/MonitorControl | Free · Open Source | — | docs? | utility? | repo GitHub |
| System Utilities | Onyx | https://www.titanium-software.fr/en/onyx.html | Free | — | docs? | utility? | chưa |
| System Utilities | Pearcleaner | https://pearcleaner.com/ | Free · Open Source | — | ? | ? | chưa |
| System Utilities | Rectangle | https://rectangleapp.com/ | Free · Open Source | — | ? | ? | chưa |
| System Utilities | The Unarchiver | https://theunarchiver.com/ | Free | — | ? | ? | chưa |
| Audio & Music | BackgroundMusic | https://github.com/kyleneideck/BackgroundMusic | Free · Open Source | — | docs? | utility? | repo GitHub |
| Audio & Music | Cog | https://cog.losno.co/ | Free · Open Source | — | ? | ? | chưa |
| Audio & Music | eqMac | https://eqmac.app/ | Free · Open Source | — | ? | ? | chưa |
| Audio & Music | IINA | https://iina.io/ | Free · Open Source | — | window? | graphite? | chưa |
| Audio & Music | Muxie | https://muxie.duhnnie.com | Free | — | ? | ? | chưa |
| Audio & Music | Petrichor | https://github.com/kushalpandya/Petrichor | Free · Open Source | — | docs? | utility? | repo GitHub |
| Audio & Music | Roam FM | https://roamfm.app/ | Freemium | — | ? | ? | chưa |
| Audio & Music | Sleeve | https://replay.software/sleeve | Paid | — | ? | ? | chưa |
| Audio & Music | SoundSource | https://rogueamoeba.com/soundsource/ | Paid | — | ? | ? | chưa |
| Video & Media | HandBrake | https://handbrake.fr/ | Free · Open Source | — | docs? | utility? | chưa |
| Video & Media | Itsytv | https://github.com/nickustinov/itsytv-macos | Free · Open Source | — | docs? | utility? | repo GitHub |
| Video & Media | Movist Pro | https://movistprime.com/ | Paid | — | ? | ? | chưa |
| Video & Media | Permute | https://software.charliemonroe.net/permute/ | Paid | — | ? | ? | chưa |
| Video & Media | QuickTime Player | https://support.apple.com/guide/quicktime-player/ | Free | — | ? | ? | chưa |
| Video & Media | Subler | https://subler.org/ | Free · Open Source | — | docs? | utility? | chưa |
| Video & Media | VLC | https://www.videolan.org/vlc/ | Free · Open Source | — | ? | ? | chưa |
| Backup & Sync | Arq | https://www.arqbackup.com/ | Paid | — | ? | ? | chưa |
| Backup & Sync | Carbon Copy Cloner | https://bombich.com/ | Paid | — | ? | ? | chưa |
| Browsers & Web | Orion | https://browser.kagi.com/ | Free | — | ? | ? | chưa |
| Browsers & Web | Zen Browser | https://zen-browser.app/ | Free · Open Source | — | ? | ? | chưa |
| Calendar & Time | Fantastical | https://flexibits.com/fantastical | Subscription | — | ? | ? | chưa |
| Calendar & Time | hora Calendar | https://horacal.app | Suscription | — | ? | ? | chưa |
| Calendar & Time | Itsycal | https://www.mowglii.com/itsycal/ | Free · Open Source | — | ? | ? | chưa |
| Calendar & Time | Meeting Bar | https://github.com/leits/MeetingBar | Free · Open Source | — | docs? | utility? | repo GitHub |
| Productivity | Alfred | https://www.alfredapp.com/ | Freemium | — | ? | ? | chưa |
| Productivity | BetterTouchTool | https://folivora.ai/ | Paid | — | ? | ? | chưa |
| Productivity | Blurt | https://blurtblurt.com | Free · Open Source | — | ? | ? | chưa |
| Productivity | Due | https://www.dueapp.com/ | Paid | — | ? | ? | chưa |
| Productivity | Focus | https://heyfocus.com/ | Paid | — | ? | ? | chưa |
| Productivity | Keyboard Maestro | https://www.keyboardmaestro.com/ | Paid | — | ? | ? | chưa |
| Productivity | OmniFocus | https://www.omnigroup.com/omnifocus/ | Paid | — | ? | ? | chưa |
| Productivity | Raycast | https://www.raycast.com/ | Freemium | — | spotlight? | midnight? | chưa |
| Productivity | Revu | https://revu.cards | Free · Open Source | — | ? | ? | chưa |
| Productivity | SelfControl | https://selfcontrolapp.com/ | Free · Open Source | — | ? | ? | chưa |
| Productivity | Snippety | https://snippety.app | Paid | — | ? | ? | chưa |
| Productivity | Speakmac | https://www.speakmac.app/ | One-Time Subscription | — | ? | ? | chưa |
| Productivity | TaskPaper | https://www.taskpaper.com/ | Paid | — | ? | ? | chưa |
| Productivity | Things | https://culturedcode.com/things/ | Paid | [ADA 2017](https://tidbits.com/2017/06/08/apple-announces-2017-apple-design-award-winners/) | icon? | native-light? | chưa |
| Menu Bar Apps | Bartender | https://www.macbartender.com/ | Paid | — | ? | ? | chưa |
| Menu Bar Apps | Commitments | https://commitments.pages.dev/ | Paid | — | ? | ? | chưa |
| Menu Bar Apps | DatWeatherDoe | https://github.com/inderdhir/DatWeatherDoe | Free · Open Source | — | docs? | utility? | repo GitHub |
| Menu Bar Apps | Dozer | https://github.com/Mortennn/Dozer | Free · Open Source | — | docs? | utility? | repo GitHub |
| Menu Bar Apps | DynamicHorizon | https://www.dynamichorizon.app/ | Paid | — | ? | ? | chưa |
| Menu Bar Apps | Hand Mirror | https://handmirror.app/ | Free | — | ? | ? | chưa |
| Menu Bar Apps | Headroom | https://github.com/patwalls/headroom | Free · Open Source | — | docs? | utility? | repo GitHub |
| Menu Bar Apps | Hidden Bar | https://github.com/dwarvesf/hidden | Free · Open Source | — | docs? | utility? | repo GitHub |
| Menu Bar Apps | Holeberry | https://github.com/pedrovieira/Holeberry | Free · Open Source | — | docs? | utility? | repo GitHub |
| Menu Bar Apps | HomeBar for Homey Pro | https://homebar.pro | Freemium | — | ? | ? | chưa |
| Menu Bar Apps | Itsyhome | https://github.com/nickustinov/itsyhome-macos | Freemium · Open Source | — | docs? | utility? | repo GitHub |
| Menu Bar Apps | MenubarX | https://menubarx.app/ | Freemium | — | ? | ? | chưa |
| Menu Bar Apps | One Thing | https://sindresorhus.com/one-thing | Paid | — | icon? | native-light? | chưa |
| Menu Bar Apps | OpenQuack | https://github.com/larryxiao/openquack | Free · Open Source | — | docs? | utility? | repo GitHub |
| Menu Bar Apps | SaneBar | https://sanebar.com | Freemium | — | ? | ? | chưa |
| Menu Bar Apps | Stargazer Bar | https://jazzyalex.github.io/stargazer-bar/ | Free · Open Source | — | ? | ? | chưa |
| Menu Bar Apps | Thaw | https://github.com/stonerl/Thaw | Free · Open Source | — | docs? | utility? | repo GitHub |
| Menu Bar Apps | TickerPad | https://tickerpad.app | Freemium | — | ? | ? | chưa |
| Menu Bar Apps | Tomatino | https://tomatino.app | Paid | — | ? | ? | chưa |
| Menu Bar Apps | TranslateAir | https://www.translateair.com/ | Freemium | — | ? | ? | chưa |
| Clipboard Managers | CopyClip | https://fiplab.com/apps/copyclip-for-mac | Free | — | ? | ? | chưa |
| Clipboard Managers | Maccy | https://github.com/p0deje/Maccy | Free · Open Source | — | docs? | utility? | repo GitHub |
| Clipboard Managers | Paste | https://pasteapp.io/ | Subscription | — | ? | ? | chưa |
| Clipboard Managers | Pesty | https://github.com/momenbasel/pesty | Free · Open Source | — | docs? | utility? | repo GitHub |
| Clipboard Managers | Unclutter | https://unclutterapp.com/ | Paid | — | ? | ? | chưa |
| Color Pickers | ColorSlurp | https://colorslurp.com/ | Freemium | — | ? | ? | chưa |
| Color Pickers | Pika | https://superhighfives.com/pika | Free · Open Source | — | ? | ? | chưa |
| Color Pickers | Sip | https://sipapp.io/ | Paid | — | ? | ? | chưa |
| Database Tools | Postico | https://eggerapps.at/postico2/ | Paid | — | ? | ? | chưa |
| Database Tools | TablePlus | https://tableplus.com/ | Freemium | — | ? | ? | chưa |
| Database Tools | TablePro | https://tablepro.app | Free · Open Source | — | ? | ? | chưa |
| Design Tools | IconJar | https://geticonjar.com/ | Paid | — | ? | ? | chưa |
| Design Tools | Sketch | https://www.sketch.com/ | Subscription | — | ? | ? | chưa |
| Design Tools | xScope | https://xscopeapp.com/ | Paid | — | ? | ? | chưa |
| Image & Graphics | Acorn | https://flyingmeat.com/acorn/ | Paid | — | ? | ? | chưa |
| Image & Graphics | ImageOptim | https://imageoptim.com/ | Free · Open Source | — | ? | ? | chưa |
| Image & Graphics | Pixave | https://www.pixaveapp.com/ | Paid | — | ? | ? | chưa |
| Image & Graphics | Pixelmator Pro | https://www.pixelmator.com/pro/ | Paid | [Mac App of the Year 2018](https://www.pixelmator.com/blog/2018/12/04/pixelmator-pro-is-the-mac-app-of-the-year/) | window? | graphite? | chưa |
| Image & Graphics | Retrobatch | https://flyingmeat.com/retrobatch/ | Paid | — | ? | ? | chưa |
| Developer Tools | BucketMate | https://bucketmate.app/ | Freemium | — | ? | ? | chưa |
| Developer Tools | CodeEdit | https://github.com/CodeEditApp/CodeEdit | Free · Open Source | — | docs? | utility? | repo GitHub |
| Developer Tools | DevCleaner | https://github.com/vashpan/xcode-dev-cleaner | Free · Open Source | — | docs? | utility? | repo GitHub |
| Developer Tools | DevUtils | https://devutils.com/ | Freemium | — | ? | ? | chưa |
| Developer Tools | Paw | https://paw.cloud/ | Paid | — | ? | ? | chưa |
| Developer Tools | Proxyman | https://proxyman.io/ | Freemium | — | ? | ? | chưa |
| Developer Tools | RocketSim | https://www.rocketsim.app/ | Freemium | — | ? | ? | chưa |
| Developer Tools | Rockxy | https://rockxy.io | Freemium · Open Source | — | ? | ? | chưa |
| Developer Tools | SF Symbols | https://developer.apple.com/sf-symbols/ | Free | — | ? | ? | chưa |
| Developer Tools | SnipperApp 3 | https://snipperapp.com | Paid (one-time) | — | ? | ? | chưa |
| Developer Tools | SSH Keys Manager | https://github.com/Stmol/ssh-keys-manager-macos-app | Free · Open Source | — | docs? | utility? | repo GitHub |
| Developer Tools | Vibedock | https://vibedock.dev/ | Paid (one-time) | — | ? | ? | chưa |
| Text Editors | BBEdit | https://www.barebones.com/products/bbedit/ | Paid | — | ? | ? | chưa |
| Text Editors | CotEditor | https://coteditor.com/ | Free · Open Source | — | ? | ? | chưa |
| Text Editors | Itsypad | https://github.com/nickustinov/itsypad-macos | Free · Open Source | — | docs? | utility? | repo GitHub |
| Text Editors | MacVim | https://macvim.org/ | Free · Open Source | — | docs? | utility? | chưa |
| Text Editors | Neon Vision Editor | https://github.com/h3pdesign/Neon-Vision-Editor | Free · Open Source | — | docs? | utility? | repo GitHub |
| Text Editors | Nova | https://nova.app/ | Paid | [ADA 2021 finalist](https://developer.apple.com/design/awards/2021/) | ? | ? | chưa |
| Text Editors | SubEthaEdit | https://subethaedit.net/ | Free · Open Source | — | ? | ? | chưa |
| Text Editors | TextMate | https://macromates.com/ | Free · Open Source | — | docs? | utility? | chưa |
| Text Editors | VimR | https://github.com/qvacua/vimr | Free · Open Source | — | docs? | utility? | repo GitHub |
| Email & Communication | Airmail | https://airmailapp.com/ | Paid | — | ? | ? | chưa |
| Email & Communication | MailMate | https://freron.com/ | Paid | — | ? | ? | chưa |
| Email & Communication | Mimestream | https://mimestream.com/ | Paid | — | ? | ? | chưa |
| Finance | Chronicle | https://chronicleapp.com/ | Paid | — | ? | ? | chưa |
| Finance | Copilot | https://www.copilot.money/ | Subscription | [ADA 2024 finalist](https://developer.apple.com/design/awards/2024/) | ? | ? | chưa |
| Finance | Soulver | https://soulver.app/ | Paid | — | ? | ? | chưa |
| Finance | Subscription Day | https://subsday.appps.od.ua/ | Freemium | — | ? | ? | chưa |
| File Management | Commander One | https://mac.eltima.com/file-manager.html | Freemium | — | ? | ? | chưa |
| File Management | Encrypto | https://macpaw.com/encrypto | Free | — | ? | ? | chưa |
| File Management | ForkLift | https://binarynights.com/ | Paid | — | ? | ? | chưa |
| File Management | Hazel | https://www.noodlesoft.com/ | Paid | — | ? | ? | chưa |
| File Management | NameQuick | https://www.namequick.app | Paid | — | ? | ? | chưa |
| File Management | Path Finder | https://www.cocoatech.io/ | Paid | — | ? | ? | chưa |
| File Management | Quick Look plugins | https://github.com/sindresorhus/quick-look-plugins | Free · Open Source | — | docs? | utility? | repo GitHub |
| Git & Version Control | Fork | https://git-fork.com/ | Free | — | ? | ? | chưa |
| Git & Version Control | GitFox | https://www.gitfox.app/ | Paid | — | ? | ? | chưa |
| Git & Version Control | GitUp | https://gitup.co/ | Free · Open Source | — | ? | ? | chưa |
| Git & Version Control | SourceTree | https://www.sourcetreeapp.com/ | Free | — | ? | ? | chưa |
| Git & Version Control | Tower | https://www.git-tower.com/mac | Paid | — | ? | ? | chưa |
| Markdown Editors | Glance | https://glance.md/ | Free | — | ? | ? | chưa |
| Markdown Editors | iA Writer | https://ia.net/writer | Paid | [ADA 2025 finalist](https://developer.apple.com/design/awards/2025/) | editorial? | paper? | chưa |
| Markdown Editors | MacDown | https://macdown.uranusjr.com/ | Free · Open Source | — | ? | ? | chưa |
| Markdown Editors | Marked 2 | https://marked2app.com/ | Paid | — | ? | ? | chưa |
| Markdown Editors | MD Preview | https://vorojar.github.io/md-preview/ | Free · Open Source | — | ? | ? | chưa |
| Markdown Editors | MWeb | https://www.mweb.im/ | Paid | — | ? | ? | chưa |
| Markdown Editors | Nice.md | https://nicemd.app/ | Freemium | — | ? | ? | chưa |
| Markdown Editors | Typora | https://typora.io/ | Paid | — | ? | ? | chưa |
| Markdown Editors | Writer | https://writer.computer/ | Free · Open Source | — | ? | ? | chưa |
| Note-Taking & Writing | Bear | https://bear.app/ | Freemium | [ADA 2017](https://tidbits.com/2017/06/08/apple-announces-2017-apple-design-award-winners/) | ? | ? | chưa |
| Note-Taking & Writing | Craft | https://www.craft.do/ | Freemium | [ADA 2021 finalist](https://developer.apple.com/design/awards/2021/) | ? | ? | chưa |
| Note-Taking & Writing | DEVONthink | https://www.devontechnologies.com/apps/devonthink | Paid | — | ? | ? | chưa |
| Note-Taking & Writing | FSNotes | https://fsnot.es/ | Free · Open Source | — | ? | ? | chưa |
| Note-Taking & Writing | Knopo | https://github.com/alkalim/Knopo | Free · Open Source | — | docs? | utility? | repo GitHub |
| Note-Taking & Writing | Notational Velocity | http://notational.net/ | Free · Open Source | — | ? | ? | chưa |
| Note-Taking & Writing | Notebooks | https://www.notebooksapp.com/ | Paid | — | ? | ? | chưa |
| Note-Taking & Writing | nvALT | https://brettterpstra.com/projects/nvalt/ | Free · Open Source | — | ? | ? | chưa |
| Note-Taking & Writing | SeqLog | https://seqlog.com/ | Free | — | ? | ? | chưa |
| Note-Taking & Writing | The Archive | https://zettelkasten.de/the-archive/ | Paid | — | ? | ? | chưa |
| Note-Taking & Writing | Tot | https://tot.rocks/ | Freemium | — | ? | ? | chưa |
| Note-Taking & Writing | Ulysses | https://ulysses.app/ | Subscription | — | ? | ? | chưa |
| Network Tools | Little Snitch | https://www.obdev.at/products/littlesnitch/ | Paid | — | ? | ? | chưa |
| Network Tools | Micro Snitch | https://www.obdev.at/products/microsnitch/ | Paid | — | ? | ? | chưa |
| Network Tools | NetNewsWire | https://netnewswire.com/ | Free · Open Source | — | ? | ? | chưa |
| Network Tools | Surge | https://nssurge.com/ | Paid | — | ? | ? | chưa |
| Network Tools | Tracexy | https://rockxy.io/tracexy | Free · Open Source | — | ? | ? | chưa |
| Network Tools | WiFi Explorer | https://www.intuitibits.com/products/wifi-explorer/ | Paid | — | ? | ? | chưa |
| Security & Privacy | Cryptomator | https://cryptomator.org/ | Free · Open Source | — | ? | ? | chưa |
| Security & Privacy | KnockKnock | https://objective-see.org/products/knockknock.html | Free · Open Source | — | ? | ? | chưa |
| Security & Privacy | Lockpaw | https://github.com/sorkila/lockpaw | Free · Open Source | — | docs? | utility? | repo GitHub |
| Security & Privacy | Lulu | https://objective-see.org/products/lulu.html | Free · Open Source | — | ? | ? | chưa |
| Security & Privacy | OverSight | https://objective-see.org/products/oversight.html | Free · Open Source | — | ? | ? | chưa |
| Security & Privacy | Shieldxy | https://rockxy.io/shieldxy | Free · Open Source | — | ? | ? | chưa |
| Password Managers | Strongbox | https://strongboxsafe.com/ | Freemium | — | ? | ? | chưa |
| PDF Tools | PDF Expert | https://pdfexpert.com/ | Paid | — | ? | ? | chưa |
| PDF Tools | PDFgear | https://www.pdfgear.com/ | Free | — | ? | ? | chưa |
| PDF Tools | PDFpenPro | https://pdfpen.com/ | Paid | — | ? | ? | chưa |
| PDF Tools | Skim | https://skim-app.sourceforge.io/ | Free · Open Source | — | docs? | utility? | chưa |
| Screenshot & Recording | BetterCapture | https://bettercapture.app/ | Free · Open Source | — | ? | ? | chưa |
| Screenshot & Recording | CleanShot X | https://cleanshot.com/ | Paid | — | ? | ? | chưa |
| Screenshot & Recording | Gifox | https://gifox.app/ | Paid | — | ? | ? | chưa |
| Screenshot & Recording | Kap | https://getkap.co/ | Free · Open Source | — | ? | ? | chưa |
| Screenshot & Recording | Keyty | https://keyty.app/ | Free · Open Source | — | ? | ? | chưa |
| Screenshot & Recording | ScreenFloat | https://eternalstorms.at/screenfloat/ | Paid | — | ? | ? | chưa |
| Screenshot & Recording | ScreenKite | https://www.screenkite.com | Free | — | ? | ? | chưa |
| Screenshot & Recording | Shottr | https://shottr.cc/ | Free | — | ? | ? | chưa |
| Screenshot & Recording | Xnapper | https://xnapper.com/ | Freemium | — | ? | ? | chưa |
| Window Management | Amethyst | https://ianyh.com/amethyst/ | Free · Open Source | — | ? | ? | chưa |
| Window Management | BetterSnapTool | https://folivora.ai/bettersnaptool | Paid | — | ? | ? | chưa |
| Window Management | Divvy | https://mizage.com/divvy/ | Paid | — | ? | ? | chưa |
| Window Management | Loop | https://github.com/MrKai77/Loop | Free · Open Source | — | docs? | utility? | repo GitHub |
| Window Management | Magnet | https://magnet.crowdcafe.com/ | Paid | — | ? | ? | chưa |
| Window Management | Moom | https://manytricks.com/moom/ | Paid | — | ? | ? | chưa |
| Window Management | Nudge | https://nudge.run | Free · Open Source | — | ? | ? | chưa |
| Window Management | Rectangle Pro | https://rectangleapp.com/pro | Paid | — | ? | ? | chưa |
| Window Management | Swish | https://highlyopinionated.co/swish/ | Paid | — | ? | ? | chưa |
| Window Management | Wins | https://wins.cool | Paid | — | ? | ? | chưa |
| Window Management | Yabai | https://github.com/koekeishiya/yabai | Free · Open Source | — | docs? | utility? | repo GitHub |
| Terminal & Shell | Alacritty | https://alacritty.org/ | Free · Open Source | — | docs? | utility? | chưa |
| Terminal & Shell | iTerm2 | https://iterm2.com/ | Free · Open Source | — | ? | ? | chưa |
| Terminal & Shell | Kitty | https://sw.kovidgoyal.net/kitty/ | Free · Open Source | — | docs? | utility? | chưa |
| Terminal & Shell | Terminal | https://support.apple.com/guide/terminal/ | Free | — | ? | ? | chưa |
| Terminal & Shell | Warp | https://www.warp.dev/ | Free | — | spotlight? | midnight? | chưa |
| Wallpaper Apps | Backspace | https://www.backspacemac.app/ | Paid | — | ? | ? | chưa |
| Wallpaper Apps | Wallspace | https://wallspace.app/ | Freemium | — | ? | ? | chưa |
