# Đụng vào file của người dùng — sandbox, quyền, theo dõi thư mục, tìm trùng, hoàn tác

App này khác app thường: **một lỗi là mất dữ liệu thật của người khác.** Mọi thứ dưới đây là bắt buộc, không phải tuỳ chọn.

## 1. Xin quyền vào thư mục — security-scoped bookmark

macOS sandbox chỉ cho app đọc thứ **người dùng tự chọn trong hộp thoại**. Chọn xong, quyền mất khi tắt app —
trừ khi lưu lại bằng bookmark.

```swift
// 1) Người dùng chọn thư mục
let panel = NSOpenPanel()
panel.canChooseDirectories = true
panel.canChooseFiles = false
panel.prompt = "Cho phép"
guard panel.runModal() == .OK, let folder = panel.url else { return }

// 2) Lưu quyền để lần sau không phải hỏi lại
let bookmark = try folder.bookmarkData(options: .withSecurityScope,
                                       includingResourceValuesForKeys: nil,
                                       relativeTo: nil)
UserDefaults.standard.set(bookmark, forKey: "watchedFolder")

// 3) Lần mở app sau
var stale = false
let url = try URL(resolvingBookmarkData: bookmark, options: .withSecurityScope,
                  relativeTo: nil, bookmarkDataIsStale: &stale)
guard url.startAccessingSecurityScopedResource() else { throw OrganizeError.noPermission(url) }
defer { url.stopAccessingSecurityScopedResource() }   // LUÔN có defer — thiếu là rò quyền, sau đó mở file gì cũng lỗi
if stale { /* xin lại bookmark mới */ }
```

Entitlement đi kèm (đã có sẵn trong scaffold):
`com.apple.security.app-sandbox`, `files.user-selected.read-write`, `files.bookmarks.app-scope`.

**Đừng** đòi Full Disk Access cho việc mà `NSOpenPanel` làm được: người dùng sợ, Apple hỏi, và mất luôn đường lên Mac App Store.

## 2. Theo dõi thư mục — FSEvents, không polling

```swift
public actor FolderWatcher {
    private var stream: FSEventStreamRef?

    public func start(_ folder: URL, onChange: @escaping @Sendable ([URL]) -> Void) { /* FSEventStreamCreate */ }
    public func stop() { /* FSEventStreamStop + Invalidate + Release */ }
}
```

- `latency` 1–2 giây: trình duyệt tải file xong mới đổi tên, bắt sớm quá là bắt trúng file dở (`.crdownload`, `.part`).
- **Bỏ qua** file đang tải: đuôi `.download`, `.crdownload`, `.part`, `.tmp`, tên bắt đầu bằng `.`.
- Chờ file "yên": kích thước không đổi trong 2 lần đọc cách nhau 1 giây rồi mới đụng vào.
- Luôn `stop()` khi cửa sổ đóng — stream rò là app ngốn CPU nền, người dùng gỡ app ngay.

## 3. Tìm file trùng

Ba mức, chạy theo thứ tự rẻ → đắt:

1. **Cỡ file** — khác cỡ thì chắc chắn khác nhau. Lọc trước, rẻ nhất.
2. **Hash 4 KB đầu + 4 KB cuối** — loại tiếp phần lớn.
3. **SHA-256 toàn file** — chỉ chạy cho nhóm còn sót.

```swift
import CryptoKit

public func sha256(of url: URL) throws -> String {
    let handle = try FileHandle(forReadingFrom: url)
    defer { try? handle.close() }
    var hasher = SHA256()
    while let chunk = try handle.read(upToCount: 1 << 20), !chunk.isEmpty {   // đọc từng 1 MB
        hasher.update(data: chunk)
    }
    return hasher.finalize().map { String(format: "%02x", $0) }.joined()
}
```

**Không đọc cả file vào RAM** (`Data(contentsOf:)` với video 4 GB là treo máy).
Ảnh "giống nhau nhưng khác file" (chụp lại, resize) là bài toán khác — perceptual hash, để Phase 2, đừng gộp vào MVP.

Khi xoá bản trùng: **giữ bản ở thư mục người dùng chọn làm gốc**, giữ bản cũ nhất theo ngày tạo, và luôn hiện cả hai
đường dẫn trước khi làm gì. Mặc định KHÔNG tự xoá.

## 4. Xoá và di chuyển

```swift
// Xoá = vào Thùng rác. KHÔNG removeItem.
try FileManager.default.trashItem(at: url, resultingItemURL: nil)

// Di chuyển: trùng tên thì đổi tên, KHÔNG ghi đè (SafeTrash.move trong Core đã làm sẵn).
```

`replaceItemAt`, `removeItem`, `write(to:)` lên file người dùng — mỗi lần dùng phải hỏi: nếu app tắt giữa chừng thì
người ta mất gì? Không trả lời được thì đổi cách làm.

## 5. Hoàn tác — bắt buộc cho mọi thao tác hàng loạt

Trước khi chạy: ghi nhật ký ra đĩa (`~/Library/Application Support/<bundle-id>/moves-<ngày>.json`), mỗi dòng `from → to`.
Sau khi chạy: nút "Hoàn tác lượt này" đọc ngược nhật ký. Nhật ký giữ 30 ngày.

Ghi nhật ký **trước** khi di chuyển, không phải sau — app tắt giữa chừng thì vẫn lần ngược được.

## 6. Test mà không phá máy

```swift
let box = FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString)
try FileManager.default.createDirectory(at: box, withIntermediateDirectories: true)
defer { try? FileManager.default.removeItem(at: box) }
```

Không test nào được trỏ vào `~/Downloads` thật — kể cả "chỉ đọc thôi".
