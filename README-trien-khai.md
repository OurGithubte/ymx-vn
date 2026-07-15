# Hướng dẫn lưu trữ & triển khai website YMX Việt Nam trong mạng LAN

## 1. Cấu trúc thư mục

```
/ (thư mục gốc website)
├── index.html          ← trang chọn ngôn ngữ
├── vi/  en/  zh/        ← mỗi thư mục 5 trang: index, about, products, quality-hse, contact
├── assets/style.css     ← giao diện dùng chung
├── assets/nav.js        ← menu mobile dùng chung
├── build/gen.py         ← mã nguồn sinh ra toàn bộ site (dùng khi cần cập nhật nội dung)
└── start-server.bat     ← chạy 1 click để chia sẻ site trong LAN
```

Toàn bộ thư mục này đã nằm sẵn trên ổ cứng máy anh. Việc "lưu ra ổ cứng" thực chất chỉ là copy cả thư mục này sang một vị trí cố định, ví dụ `D:\Website\ymx-vietnam\`, để không bị lẫn với các file tạm khác.

## 2. Triển khai cho các máy trong LAN xem được

### Cách 1 – Xem thử nhanh (khuyên dùng để test trước)
1. Cài Python (nếu máy chưa có): tải tại python.org, khi cài nhớ tick **Add Python to PATH**.
2. Double-click file `start-server.bat` trong thư mục website.
3. Cửa sổ hiện lên địa chỉ dạng `http://192.168.x.x:8080/` — gửi địa chỉ này cho đồng nghiệp trong cùng mạng LAN, họ mở trình duyệt và vào là xem được.
4. Nhược điểm: máy này phải **bật liên tục** và cửa sổ server không được tắt. Nếu tắt máy hoặc đóng cửa sổ, các máy khác sẽ không vào được nữa.

### Cách 2 – Chạy ổn định lâu dài bằng IIS (khuyên dùng — không cần mở cửa sổ nào cả)
Đây là cách giải quyết đúng vấn đề "tắt cửa sổ là mất web": IIS chạy như một **dịch vụ nền của Windows**, không có cửa sổ để đóng, tự khởi động lại cùng máy tính mỗi khi bật nguồn.

**Cách nhanh nhất — dùng script có sẵn `setup-iis.ps1`:**
1. Bấm chuột phải vào **PowerShell** → **Run as Administrator**.
2. Chạy lệnh: `Set-ExecutionPolicy Bypass -Scope Process -Force`
3. Chạy: `& "E:\YMX Websile\setup-iis.ps1"`
4. Đợi 1–2 phút để Windows cài đặt tính năng IIS (chỉ lần đầu), script sẽ tự tạo site, mở firewall và in ra địa chỉ LAN để anh gửi cho đồng nghiệp.
5. Từ nay có thể tắt hết cửa sổ, tắt cả PowerShell — website vẫn chạy ngầm, kể cả khi khởi động lại máy.

**Nếu muốn tự làm bằng tay (không dùng script):**
1. Vào **Control Panel → Programs → Turn Windows features on or off**, tick **Internet Information Services (IIS)**.
2. Mở **IIS Manager**, tạo một Website mới, trỏ **Physical path** đến thư mục chứa `index.html`.
3. Đặt **Port** (ví dụ 80 hoặc 8080).
4. Vào **Windows Firewall → Advanced settings → Inbound Rules**, mở port đã chọn cho phép kết nối từ mạng nội bộ.
5. Đặt **IP tĩnh** cho máy chủ này (hỏi bộ phận IT) để địa chỉ không đổi mỗi lần khởi động lại router.
6. Các máy trong LAN truy cập bằng `http://<IP-máy-chủ>` hoặc `http://<IP-máy-chủ>:8080`.

> Sau khi cài IIS xong, `start-server.bat` không còn cần thiết nữa — chỉ giữ lại để test nhanh khi cần.

### Cách 3 – Nếu công ty có máy chủ Linux/NAS nội bộ
Cài **Nginx** hoặc **Apache**, trỏ thư mục gốc (`document root`) vào thư mục chứa `index.html`, mở port tương ứng trên firewall nội bộ. Cách này ổn định nhất vì máy chủ NAS/Linux thường chạy 24/7.

> Gợi ý: nếu công ty đã có máy chủ file/NAS đang chạy sẵn dịch vụ web, nên host ở đó thay vì máy cá nhân, để tránh gián đoạn khi ai đó tắt máy.

## 3. Cải thiện tính năng / cập nhật nội dung sau này

### Cách A – Nhờ Nancy chỉnh sửa (khuyến nghị)
Vì site được sinh ra từ một file mã nguồn duy nhất `build/gen.py` (chứa toàn bộ nội dung 3 ngôn ngữ dưới dạng có cấu trúc), anh chỉ cần cho biết nội dung/tính năng cần đổi (ví dụ: thêm chứng nhận ISO, đổi số điện thoại, thêm trang Tuyển dụng...). Nancy sẽ sửa trong file này rồi chạy lại để sinh đồng loạt cả 15 trang, đảm bảo 3 ngôn ngữ luôn khớp nội dung và giao diện không bị lệch. Sau đó anh chỉ cần copy đè các file mới vào đúng thư mục đang chạy server — không cần cài lại gì, chỉ cần bấm F5 trên trình duyệt là thấy bản cập nhật.

### Cách B – Tự chỉnh sửa trực tiếp (nếu có nhân sự IT/kỹ thuật)
- Sửa nội dung chữ: mở file `.html` tương ứng (ví dụ `vi/contact.html`) bằng Notepad/VS Code, tìm đoạn chữ cần đổi, sửa rồi lưu lại.
- Sửa giao diện chung (màu sắc, khoảng cách, bố cục): chỉnh trong `assets/style.css`, áp dụng ngay cho toàn bộ 15 trang.
- Thêm trang mới: cần thêm cấu trúc mới trong `build/gen.py` để đồng bộ 3 ngôn ngữ — phần này nên nhờ Nancy hỗ trợ để tránh sai lệch giữa các bản ngôn ngữ.
- Sau khi sửa file nào, chỉ cần lưu đè đúng vị trí trong thư mục đang chạy server, không cần khởi động lại server (trừ trường hợp dùng IIS thì có thể cần "Recycle" site nếu không thấy cập nhật ngay).

### Lưu ý khi cập nhật
- Luôn giữ một bản sao lưu (backup) thư mục website trước khi ghi đè, để có thể khôi phục nếu chỉnh sai.
- Nếu đổi thông tin pháp lý (mã số thuế, người đại diện, vốn điều lệ...), nên đối chiếu lại với giấy chứng nhận đăng ký doanh nghiệp/đầu tư mới nhất trước khi cập nhật.
