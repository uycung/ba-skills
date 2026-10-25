# Hồ sơ sản phẩm: đặc tính ưu tiên

Mức: ●●● bắt buộc xem xét kỹ, ●● thường quan trọng, ● xem nhanh. Đây là điểm xuất phát, người dùng điều chỉnh theo bối cảnh (25002 §7.4).

| Đặc tính | Web | Mobile | Nội bộ | AI |
|---|---|---|---|---|
| Functional suitability | ●● | ●● | ●●● | ●●● (độ đúng, độ phủ) |
| Performance efficiency | ●●● (Core Web Vitals) | ●●● (khởi động, pin, bộ nhớ) | ●● | ●●● (độ trễ, chi phí mỗi truy vấn) |
| Compatibility | ●● (trình duyệt) | ●●● (OS, thiết bị) | ●●● (tích hợp hệ thống cũ) | ●● (API mô hình) |
| Interaction capability | ●●● (WCAG) | ●●● | ●● | ●●● (minh bạch, kiểm soát của người dùng) |
| Reliability | ●●● | ●● (chế độ offline, đồng bộ) | ●●● | ●● (fallback khi mô hình lỗi) |
| Security | ●●● | ●●● (lưu trữ cục bộ, chứng thực) | ●●● (phân quyền) | ●●● (prompt injection, rò rỉ dữ liệu) |
| Maintainability | ●● | ●● | ●●● | ●● (quản lý phiên bản mô hình, prompt) |
| Flexibility | ●● | ●● (phát hành cửa hàng ứng dụng) | ●● | ●● (thay nhà cung cấp mô hình) |
| Safety | ● | ● | ● | ●●● (hậu quả của kết quả sai, rủi ro cho người dùng) |

## Câu hỏi thêm theo loại
- **Web**: trình duyệt hỗ trợ, SEO, tải trang trên mạng chậm, SLO khả dụng, CDN.
- **Mobile**: phiên bản OS tối thiểu (lấy từ số liệu truy cập thực tế của sản phẩm, xem `thresholds.md`), mức pin, offline, kích thước gói, quyền truy cập thiết bị, quy định cửa hàng ứng dụng.
- **Nội bộ**: số người dùng, tích hợp SSO/AD, kiểm toán, cửa sổ bảo trì, đào tạo, vòng đời hệ thống.
- **AI**: đo chất lượng đầu ra bằng bộ đánh giá (eval) thay vì cảm tính; độ trễ và chi phí; kiểm soát của con người (human-in-the-loop); ghi nhãn nội dung do AI tạo; dữ liệu dùng để huấn luyện/gửi cho nhà cung cấp; khung pháp lý (xem `legal-vn.md`, Luật AI và EU AI Act). Tham chiếu tự nguyện: NIST AI 100-1, ISO/IEC 42001:2023.
