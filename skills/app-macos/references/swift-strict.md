# Swift 6 + SwiftUI cho app Mac — luật cứng và mẫu code

Nạp khi viết code trong `apps/ACTIVE/<slug>/source/mac`. Mọi luật ở đây đều có lý do trả giá, không phải sở thích.

## 1. Đặt tên — Swift API Design Guidelines (Apple)

- Rõ nghĩa **tại điểm gọi** quan trọng hơn ngắn: `move(file, to: folder)` chứ không `mv(f, d)`.
- Hàm có tác dụng phụ = động từ mệnh lệnh: `sort()`, `trash(url)`. Hàm trả về bản mới = `-ed/-ing`: `sorted()`, `trimming()`.
- Init chuyển đổi giữ nguyên giá trị thì bỏ nhãn đầu: `Int64(someUInt32)`.
- Boolean đọc như câu khẳng định: `file.isDuplicate`, không `file.duplicate`.
- Không viết tắt trừ khi cả ngành dùng (`url`, `id`, `png` được; `fmgr`, `dst` không).

## 2. Concurrency (Swift 6, strict)

```swift
// Việc nặng: actor. Trạng thái bên trong actor không bao giờ bị hai luồng đụng cùng lúc.
public actor HashIndex {
    private var byHash: [String: [URL]] = [:]

    public func add(_ url: URL, hash: String) {
        byHash[hash, default: []].append(url)
    }

    public func duplicates() -> [[URL]] {
        byHash.values.filter { $0.count > 1 }.map { $0 }
    }
}

// Quét nhiều file song song nhưng CÓ TRẦN — mở 10.000 file một lúc là treo máy.
func hashAll(_ urls: [URL], limit: Int = 8) async throws -> [(URL, String)] {
    try await withThrowingTaskGroup(of: (URL, String).self) { group in
        var out: [(URL, String)] = []
        var iterator = urls.makeIterator()
        for _ in 0 ..< limit {
            if let url = iterator.next() { group.addTask { (url, try sha256(of: url)) } }
        }
        while let done = try await group.next() {
            out.append(done)
            if let url = iterator.next() { group.addTask { (url, try sha256(of: url)) } }
        }
        return out
    }
}
```

Luật:
- `<Name>Core` chạy **ngoài** main actor. Chỉ ViewModel là `@MainActor`.
- Kiểu đi qua biên phải `Sendable`. Cảnh báo "non-sendable type crossing actor boundary" là lỗi thật, không phải nhiễu — **không tắt bằng `@unchecked Sendable`** trừ khi viết rõ vì sao an toàn ngay trên dòng đó.
- Việc dài phải huỷ được: kiểm `try Task.checkCancellation()` trong vòng lặp; người dùng bấm Stop là phải dừng thật.
- Không `DispatchQueue.main.async` trong code mới — dùng `@MainActor`.

## 3. Lỗi — không bao giờ nuốt, không bao giờ `try!`

```swift
public enum OrganizeError: Error, Sendable {
    case noPermission(URL)       // hết hạn bookmark
    case targetExists(URL)
    case underlying(String)
}

// ĐÚNG: lỗi một file không được giết cả lượt chạy.
for url in files {
    do { try safeTrash.move(url, toDirectory: folder) }
    catch { report.append(.init(url: url, error: error)) }   // ghi lại, chạy tiếp, báo cuối lượt
}
```

Cấm: `try!`, `as!`, `!` mở optional, `catch {}` rỗng, `fatalError` trong đường chạy bình thường.
`scripts/check_macos.py` bắt `try!` / `as!` là FAIL; `make lint` (SwiftLint `--strict`) bắt force unwrap.

## 4. ViewModel

```swift
@MainActor
@Observable
final class InboxViewModel {
    private(set) var items: [FileEntry] = []
    private(set) var isScanning = false
    private(set) var error: String?

    private let scanner: any FileScanner        // protocol, để cắm Fake khi test

    init(scanner: any FileScanner) { self.scanner = scanner }

    func scan(_ folder: URL) async {
        isScanning = true
        defer { isScanning = false }
        do { items = try await scanner.scan(folder) }
        catch { self.error = String(describing: error) }
    }
}
```

- `private(set)` cho mọi thứ View đọc — View không tự sửa trạng thái.
- Không `import SwiftUI` trong ViewModel: đó là thứ khiến nó test được mà không cần dựng UI.
- Không `Timer`, không polling: dùng FSEvents (xem file-safety.md).

## 5. View

```swift
struct InboxView: View {
    @State var viewModel: InboxViewModel

    var body: some View {
        Table(viewModel.items) {
            TableColumn("Tên", value: \.name)
            TableColumn("Cỡ") { Text($0.sizeText) }        // chữ đã format sẵn từ Core
        }
        .overlay { if viewModel.isScanning { ProgressView() } }
        .task { await viewModel.scan(folder) }
    }
}
```

- View **không** format ngày/cỡ file/tiền — Core trả sẵn chuỗi. View sai format thì không test nào bắt được.
- Mac có chuột: mọi thao tác phá hoại (xoá, gộp) phải có xác nhận + hoàn tác, và có phím tắt chuẩn (`⌘Z`, `⌘⌫`).
- Dùng `Table`, `NavigationSplitView`, `Settings`, `MenuBarExtra` — component chuẩn macOS, không bê layout iPhone sang.
- Kéo–thả là chuẩn mực trên Mac: `.dropDestination(for: URL.self)`.

## 6. Test — Swift Testing

```swift
@Suite("Classifier")
struct ClassifierTests {
    @Test("ảnh đi vào thư mục Images theo tháng")
    func imageGoesToImages() throws {
        let plan = Classifier().plan(for: URL(filePath: "/tmp/a.png"), modified: .init(timeIntervalSince1970: 0))
        #expect(plan.folder == "Images/1970-01")
    }

    @Test("đuôi lạ thì KHÔNG đoán bừa — để nguyên chỗ cũ")
    func unknownStaysPut() throws {
        #expect(Classifier().plan(for: URL(filePath: "/tmp/a.qqq"), modified: .now).folder == nil)
    }
}
```

- Test nằm ở `<Name>CoreTests`, chạy bằng `swift test`. Không cần Xcode, không cần UI.
- Test đụng file luôn tạo thư mục tạm `FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString)` và dọn bằng `defer`.
- Mỗi lỗi đã sửa để lại một test đỏ-trước-xanh-sau (skill `/app-fix`).

## 7. Định dạng

`make fmt` (SwiftFormat) + `make lint` (SwiftLint `--strict`). 4 space, không tab, dòng ≤ 120, file kết thúc bằng dòng trống,
`// MARK: -` chia mục trong file dài. Đừng cãi nhau về style — máy quyết.

## 8. Lỗi hay gặp

| Hiện tượng | Nguyên nhân thật | Sửa |
|---|---|---|
| `error: cannot find type 'X' in scope` dù cùng thư mục | quên `import <Name>Core` hoặc quên `public` | kiểu dùng ngoài Core phải `public`, init cũng phải `public` |
| Cảnh báo Sendable đầy màn | truyền class thường qua biên actor | đổi sang `struct` + `Sendable`, hoặc bọc trong actor |
| App mở ra rồi tắt ngay | chạy file nhị phân trần, không phải `.app` | `make run` (dựng bundle rồi `open`) |
| UI treo khi quét thư mục lớn | gọi hàm nặng từ `@MainActor` | đẩy vào `actor` trong Core, ViewModel chỉ `await` |
| `Operation not permitted` khi đọc `~/Downloads` | sandbox, chưa có bookmark | `NSOpenPanel` + security-scoped bookmark (file-safety.md) |
| `swift test` không thấy `Testing` | toolchain cũ | cần Swift 6 (Xcode 16+): `swift --version` |
