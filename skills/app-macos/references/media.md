# Nén ảnh và video trên macOS — API native, bẫy license, tham số

Luật một dòng: **nén xong phải giữ được bản gốc cho tới khi người dùng đồng ý**, và **không nhúng thứ GPL**.

## 1. Bẫy license — đọc trước khi chọn thư viện

| Thư viện | License | Nhúng vào app bán được không |
|---|---|---|
| `AVFoundation`, `ImageIO`, `Core Image`, `Vision` | của Apple, có sẵn trong macOS | được, mọi kiểu phân phối |
| ffmpeg (bản thường), HandBrakeCLI, x264, x265 | **GPL** | Mac App Store: **không**. Ngoài store: chỉ khi bạn mở source toàn bộ app theo GPL |
| mozjpeg | BSD-3 | được, nhưng là binary rời → phải ký + notarize riêng từng binary |
| pngquant | GPL cho bản CLI | tránh |
| libwebp | BSD | được |

`scripts/check_macos.py` quét `mac/` và FAIL nếu thấy `ffmpeg`, `HandBrakeCLI`, `x264`… nằm trong project.

Muốn học tham số nén tốt thì **đọc** HandBrake (cách họ chọn CRF), rồi tự làm bằng AVFoundation — đọc không vi phạm gì.

## 2. Nén ảnh — ImageIO

```swift
import ImageIO
import UniformTypeIdentifiers

/// Ghi ra file MỚI. Không bao giờ ghi đè bản gốc.
public func compressJPEG(at source: URL, to target: URL, quality: Double) throws {
    guard let src = CGImageSourceCreateWithURL(source as CFURL, nil),
          let dest = CGImageDestinationCreateWithURL(target as CFURL, UTType.jpeg.identifier as CFString, 1, nil)
    else { throw MediaError.cannotRead(source) }

    let options: [CFString: Any] = [
        kCGImageDestinationLossyCompressionQuality: quality,   // 0.8 gần như không nhìn ra khác biệt
        kCGImageDestinationOptimizeColorForSharing: true,
    ]
    CGImageDestinationAddImageFromSource(dest, src, 0, options as CFDictionary)
    guard CGImageDestinationFinalize(dest) else { throw MediaError.cannotWrite(target) }
}
```

- `quality` 0.8 là điểm ngọt cho ảnh chụp; PNG ảnh chụp màn hình thì đổi sang HEIC/JPEG mới giảm được nhiều.
- PNG không mất dữ liệu: dùng `kCGImagePropertyPNGCompressionFilter`, mức giảm ít hơn nhiều — nói thật với người dùng.
- **Metadata**: `CGImageDestinationAddImageFromSource` giữ EXIF. Muốn xoá vị trí GPS thì phải cố ý xoá, và
  **phải nói trong UI** — xoá thầm dữ liệu của người ta là mất lòng tin.
- Đo thật: so `attributesOfItem` trước/sau. Không hiện "tiết kiệm 70%" khi chưa đo file đó.
- Nén không nhỏ hơn bản gốc (hay gặp với ảnh đã tối ưu) → **giữ bản gốc**, báo "đã tối ưu sẵn", không thay file.

## 3. Nén video — AVFoundation

```swift
import AVFoundation

public func compressVideo(at source: URL, to target: URL, preset: String = AVAssetExportPresetHEVC1920x1080) async throws {
    let asset = AVURLAsset(url: source)
    guard let session = AVAssetExportSession(asset: asset, presetName: preset) else {
        throw MediaError.presetUnavailable
    }
    session.outputURL = target
    session.outputFileType = .mp4
    session.shouldOptimizeForNetworkUse = true
    await session.export()
    if session.status != .completed { throw MediaError.export(session.error?.localizedDescription ?? "?") }
}
```

- HEVC (H.265) trên Apple Silicon dùng bộ mã hoá phần cứng: nhanh, mát máy. Nhưng file HEVC mở trên máy cũ/Windows
  có thể không xem được — **hỏi người dùng trước khi đổi codec**, đừng tự quyết.
- Cần kiểm soát chất lượng kỹ hơn preset thì dùng `AVAssetWriter` với `AVVideoCompressionPropertiesKey`
  (`AVVideoAverageBitRateKey`, `AVVideoQualityKey`, `AVVideoExpectedSourceFrameRateKey`).
- Ước tính dung lượng trước khi chạy: `session.estimatedOutputFileLengthInBytes` — hiện cho người dùng thấy trước.
- Video dài: chạy trong `Task` huỷ được, hiện `session.progress`, và **đừng** để máy ngủ giữa chừng
  (`ProcessInfo.processInfo.beginActivity(options: .userInitiated)`).

## 4. Luồng an toàn cho cả ảnh lẫn video

1. Nén ra file tạm trong thư mục của app.
2. So kích thước. Nhỏ hơn đáng kể (≥ 10%) mới đề nghị thay.
3. Hiện trước–sau (ảnh: xem cạnh nhau; video: ảnh đại diện + dung lượng + thời lượng).
4. Người dùng đồng ý → chuyển bản gốc vào **Thùng rác** (không xoá), đặt file mới vào đúng chỗ, ghi nhật ký hoàn tác.
5. Không đồng ý → xoá file tạm.

## 5. Bảng lỗi

| Hiện tượng | Nguyên nhân | Sửa |
|---|---|---|
| `AVAssetExportSession` trả `failed` không lý do | file đang được app khác ghi | chờ file "yên" rồi mới nén (file-safety.md §2) |
| Video ra to hơn bản gốc | bản gốc đã nén tốt hơn preset | so kích thước rồi mới thay; giữ gốc |
| Ảnh ra bị xoay sai | mất EXIF Orientation | giữ metadata bằng `CGImageDestinationAddImageFromSource`, không vẽ lại qua `CGImage` |
| Nén 500 ảnh thì app treo | chạy trên main actor | đưa vào `actor`, `TaskGroup` có trần (swift-strict.md §2) |
| Máy nóng, quạt kêu | mã hoá phần mềm vì preset không hỗ trợ phần cứng | dùng preset HEVC/H.264 chuẩn của AVFoundation |
