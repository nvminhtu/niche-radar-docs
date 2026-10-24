# Từ số 0: mua tài khoản Apple và dựng bộ khoá ký

> Nguồn: Game-AI-Skills `game-ship/references/apple-signing.md` (2026-09-08). Viết cho game Godot — với app Flutter,
> project Xcode là `apps/ACTIVE/<slug>/source/app/ios/Runner.xcworkspace`; chỗ nói "Godot export preset" thay bằng Xcode ▸ Runner ▸ Signing & Capabilities.
> Phần tài khoản, Team ID, chứng chỉ, API key áp dụng y nguyên.

File này dành cho người **chưa có gì cả** — chưa Apple ID dev, chưa trả $99, chưa
biết Team ID ở đâu ra. Làm một lần, dùng cho mọi game về sau.

- Phí, thời gian chờ, hai cái đồng hồ tiền bạc → `appstore-account.md`
- Các bước lên store sau khi đã có acc → `appstore-runbook.md`
- Upload build → `appstore-runbook.md` Phase 2b

Đã đối chiếu tài liệu Apple ngày **2026-09-08**. Chỗ nào là kinh nghiệm cộng đồng
đều ghi rõ *(cộng đồng)*.

---

## 0. Bức tranh 30 giây

| Thứ | Là gì | Có khi nào |
|---|---|---|
| **Apple ID** | tài khoản đăng nhập | ngay, miễn phí |
| **Personal Team (free)** | ký để chạy trên **máy thật của mình**, profile sống **7 ngày** | ngay, miễn phí |
| **Membership $99** | quyền lên TestFlight + App Store | sau khi trả tiền + duyệt (~24h) |
| **Team ID** | mã **10 ký tự** định danh team | **chỉ sinh ra sau khi membership active** |
| **Certificate + Provisioning profile** | bộ khoá thực sự dùng để ký app | Xcode tự tạo, sau khi có team |
| **API key `.p8`** | để upload bằng dòng lệnh | tự tạo, bất cứ lúc nào sau khi có acc |

> **Trả lời thẳng câu "Team ID là gì khi chưa mua acc":** chưa mua thì **chưa có**.
> Nó không phải thứ đi xin hay mua rời — nó được cấp kèm membership. Trong pipeline,
> Team ID **chỉ cần khi build cho máy thật / TestFlight / App Store**. Chạy trên
> **iOS Simulator thì không cần** Team ID, không cần ký, không cần trả đồng nào —
> đó là lý do `game-ship` Phase 4 mặc định đi đường Simulator.

---

## 1. Bước 0 — làm miễn phí trước khi tốn $99

Trước khi trả tiền, hãy chắc game chạy được trên **iPhone thật** của anh. Apple ID
thường (Personal Team) làm được việc này:

1. Xcode ▸ Settings ▸ Accounts ▸ **+** ▸ Apple ID → đăng nhập bằng Apple ID thường.
2. Mở project Xcode do `game-ship` export ▸ target ▸ Signing & Capabilities ▸
   tick **Automatically manage signing** ▸ Team = **(Personal Team)**.
3. Cắm iPhone, chọn nó làm destination, **Run**.
4. Trên iPhone: Settings ▸ General ▸ VPN & Device Management ▸ tin tưởng
   developer đó.

Giới hạn của đường free *(cộng đồng, ổn định nhiều năm)*: profile hết hạn sau
**7 ngày** (app tự ngừng mở, phải build lại), tối đa **3 app** cùng lúc trên máy,
đăng ký khoảng **10 App ID mỗi tuần**, và **không có TestFlight, không lên được
App Store**. Membership trả phí thì profile sống **1 năm**.

Đây là bài test đáng giá nhất trước khi rút thẻ: nếu game chạy mượt trên máy thật
qua đường này, phần còn lại chỉ là thủ tục.

---

## 2. Thủ tục mua tài khoản — 10 bước

> Nhắc lại luật ở `appstore-account.md`: **không mua/thuê acc sang tay.** Apple huỷ
> acc chuyển nhượng và app đi theo acc.

| # | Bước | Lưu ý |
|---|---|---|
| 1 | Tạo (hoặc chọn) **một Apple ID dùng riêng cho developer** | acc này *là* cả gia tài app về sau — đừng dùng chung với acc gia đình, đừng dùng email công ty có thể mất |
| 2 | Bật **2FA** cho Apple ID đó | Apple bắt buộc. Phải giữ được số điện thoại nhận mã — mất số là mất đường vào |
| 3 | Điền **tên hợp pháp đúng như giấy tờ** trong Apple ID | tên này sẽ in ra làm "seller" trên store nếu đăng ký Individual, và phải khớp giấy tờ lúc xác minh |
| 4 | Chọn loại: **Individual** (khuyên dùng) hay Organization | Organization cần pháp nhân + D-U-N-S + website thật + email tên miền công ty, chờ 1–2 tuần. Individual duyệt ~24h |
| 5 | Cài app **Apple Developer** trên iPhone → Membership → Enroll | đường iPhone thường nhanh hơn web vì xác minh danh tính ngay trên máy bằng Face ID + giấy tờ |
| 6 | **Xác minh danh tính**: chụp hộ chiếu / CCCD theo hướng dẫn | tên trên giấy tờ phải khớp bước 3, nếu lệch là bị treo |
| 7 | Trả **$99** | thẻ Visa/Mastercard có bật thanh toán quốc tế. Apple thu theo năm |
| 8 | Chờ email xác nhận | Apple nói Individual xong **trong vòng 24h** kể từ lúc thanh toán |
| 9 | Vào developer.apple.com ▸ Account ▸ **Membership details** → chép **Team ID** (10 ký tự) | đây chính là lúc Team ID xuất hiện |
| 10 | Đặt nhắc lịch **gia hạn hằng năm** | hết hạn = app bị gỡ khỏi App Store. Đừng tin vào email nhắc của Apple |

**Ghi chú cho VN:** địa chỉ khai phải là địa chỉ thật (Apple có gửi thư/gọi xác
minh với Organization); thẻ ghi nợ quốc tế dùng được nếu ngân hàng cho thanh toán
quốc tế; nếu sau này bán app có phí thì mới phải lo phần thuế/banking ở
`appstore-account.md` §2 — game free + ads thì không.

---

## 3. Team ID — lấy ở đâu, dùng ở đâu

Ba chỗ đều ra cùng một chuỗi 10 ký tự (ví dụ `A1B2C3D4E5`):

1. developer.apple.com ▸ **Account** ▸ Membership details ▸ *Team ID*
2. App Store Connect ▸ Users and Access (hiện trong thông tin team)
3. Xcode ▸ Settings ▸ Accounts ▸ chọn team ▸ nó nằm cạnh tên team

Dùng ở đúng 3 chỗ trong pipeline này:

| Nơi điền | Trường | Bắt buộc khi |
|---|---|---|
| Godot ▸ Export ▸ iOS preset | `application/app_store_team_id` | build cho **máy thật / store**; Simulator thì bỏ trống được |
| `ExportOptions.plist` | `<key>teamID</key>` | upload bằng dòng lệnh |
| Xcode ▸ Signing & Capabilities | Team | luôn, khi ký |

> Sai định dạng Team ID làm **Godot exporter văng lỗi JSON parse** khó hiểu — nó
> phải đúng 10 ký tự chữ-số, không khoảng trắng (đã ghi ở `game-ship` Phase 2).

---

## 4. Bộ khoá ký gồm những mảnh nào

Đây là chỗ hay rối. Năm thứ, khác nhau hoàn toàn:

| Mảnh | Là gì | Nằm ở đâu | Mất thì sao |
|---|---|---|---|
| **Apple ID + 2FA** | danh tính | Apple | mất số ĐT = rất khổ, liên hệ Apple |
| **Certificate** (Apple Development / **Apple Distribution**) | cặp khoá công–tư. Apple ký phần công; **phần bí mật nằm trong Keychain máy anh** | Keychain Access trên Mac | revoke rồi tạo lại; nếu có bản `.p12` backup thì import lại là xong |
| **Identifier / App ID** | chính là bundle id, vd `com.tunguyen.dinobuddies` | developer.apple.com ▸ Identifiers | **không đổi được** sau khi app record đã tạo |
| **Provisioning profile** | gói buộc: certificate + App ID + (danh sách máy) + entitlements. Loại: Development / Ad Hoc / **App Store** | Apple cấp, Xcode tải về | Xcode tạo lại tự động |
| **App Store Connect API key `.p8`** | **không phải khoá ký**. Chỉ để upload/gọi API bằng CLI | App Store Connect ▸ Users and Access ▸ Integrations ▸ Keys | tải được **đúng 1 lần**; mất thì revoke và tạo key mới |

Ký app = dùng **private key của certificate** để ký, kèm theo **provisioning
profile** nói rằng "khoá này được phép ký bundle id này, cho những máy này".

---

## 5. Đường dễ — để Xcode tự lo (dùng cái này)

Sau khi membership active:

1. Xcode ▸ Settings ▸ **Accounts** ▸ + ▸ Apple ID (acc dev) → team hiện ra.
2. Mở `games/<slug>/godot/builds/ios/<slug>.xcodeproj`.
3. Target ▸ **Signing & Capabilities**:
   - tick **Automatically manage signing**
   - **Team** = team của anh
   - **Bundle Identifier** = đúng chuỗi đã đặt trong Godot preset
4. Xcode tự tạo certificate + provisioning profile, tự đăng ký máy thật đang cắm.
5. Build cho device để chắc chắn ký được, rồi mới **Product ▸ Archive** cho store.

Không cần tự tạo CSR, không cần vào web tạo profile bằng tay. **99% trường hợp
indie dừng ở đây là đủ.**

---

## 6. Đường thủ công — chỉ khi cần (CI, máy build khác, chia khoá cho người khác)

1. **Keychain Access** ▸ menu Certificate Assistant ▸ *Request a Certificate From a
   Certificate Authority…* → lưu ra file `.certSigningRequest` (CSR).
   Bước này sinh ra cặp khoá; **private key nằm lại trong Keychain của máy này**.
2. developer.apple.com ▸ Certificates ▸ **+** ▸ chọn *Apple Distribution* → upload
   CSR → tải về `.cer`.
3. Double-click `.cer` để cài vào Keychain (nó ghép với private key ở bước 1).
4. Identifiers ▸ **+** → tạo App ID đúng bundle id.
5. Profiles ▸ **+** ▸ *App Store* → chọn App ID + certificate → tải `.mobileprovision`.
6. **Backup**: Keychain ▸ chuột phải certificate ▸ *Export…* → `.p12` + đặt mật khẩu.
   Đây là thứ duy nhất cứu anh khi đổi máy.

---

## 7. API key `.p8` — cho upload bằng dòng lệnh

Chỉ cần nếu đi Route B ở `appstore-runbook.md` Phase 2b.

1. App Store Connect ▸ **Users and Access** ▸ **Integrations** ▸ Keys ▸ **+**.
2. Đặt tên, chọn quyền (**App Manager** là đủ để upload build).
3. Tải file `AuthKey_<KEYID>.p8` — **chỉ tải được một lần, Apple không giữ bản sao**.
4. Chép lại **Key ID** (trên dòng key) và **Issuer ID** (nằm phía trên bảng key).
5. Đặt file vào `~/.appstoreconnect/private_keys/AuthKey_<KEYID>.p8`.

Mất hoặc lộ → **Revoke** ngay (không phục hồi được) rồi tạo key mới.
**Không bao giờ commit `.p8`, `.p12`, `.mobileprovision` vào git.**

---

## 8. Sao lưu — 6 dòng, cất ở password manager

```
Apple ID dev        : ...
Team ID             : ..........   (10 ký tự)
Bundle id gốc       : com.<anh>.<game>
Cert .p12 + mật khẩu: <cất ở đâu>
API Key ID          : ..........
API Issuer ID       : ........-....-....-....-............
```

Ba file cần cất ngoài máy: `.p12` (certificate + private key), `.p8` (API key),
và ảnh chụp màn hình trang Membership. Đổi máy mà thiếu `.p12` thì phải revoke
certificate cũ — mọi build đã ký bằng nó vẫn chạy, nhưng anh phải tạo lại bộ mới.

---

## 9. Bẫy hay dính

| Bẫy | Hậu quả | Tránh |
|---|---|---|
| Đăng ký Individual bằng tên không khớp giấy tờ | treo hồ sơ ở bước xác minh | khai đúng tên trên CCCD/hộ chiếu |
| Dùng Apple ID cá nhân đang chia sẻ trong gia đình | rắc rối 2FA + quyền sở hữu app về sau | tạo Apple ID riêng cho dev |
| Không backup `.p12` | đổi máy = tạo lại toàn bộ chứng chỉ | export ngay sau khi Xcode tạo cert |
| Revoke nhầm certificate đang dùng | build cũ vẫn chạy, nhưng phải ký lại toàn bộ | đọc kỹ tên cert trước khi bấm Revoke |
| Đặt bundle id tạm rồi muốn đổi | **không đổi được** sau khi tạo app record | chốt `com.<tên>.<game>` ngay từ `game-setup` |
| Quên gia hạn $99 | app bị gỡ khỏi App Store | lịch nhắc trước 30 ngày |
| Tải `.p8` xong để lung tung | lộ quyền upload | password manager, và revoke nếu nghi lộ |
| Tưởng phải có Team ID mới chạy thử được game | tốn $99 sớm hơn cần thiết | Simulator không cần gì cả; máy thật dùng Personal Team 7 ngày |

---

## 10. Checklist một lần duy nhất

- [ ] Apple ID riêng cho dev, bật 2FA, tên khớp giấy tờ
- [ ] Chạy thử game trên iPhone thật bằng **Personal Team** (miễn phí, 7 ngày)
- [ ] Enroll **Individual** $99 qua app Apple Developer → xác minh danh tính
- [ ] Nhận email active → chép **Team ID** (10 ký tự)
- [ ] Điền Team ID + bundle id vào **Godot iOS export preset**
- [ ] Xcode ▸ Accounts thêm acc → target bật **Automatically manage signing**
- [ ] Build lên máy thật một lần bằng cert Distribution/Development → ký được
- [ ] Export `.p12` backup + tạo **API key `.p8`** (nếu muốn upload bằng CLI)
- [ ] Ghi 6 dòng ở §8 vào password manager
- [ ] Đặt lịch nhắc gia hạn hằng năm

Xong bước này thì `appstore-runbook.md` chạy được từ Phase 1 đến hết.
