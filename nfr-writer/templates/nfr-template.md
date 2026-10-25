# Mẫu NFR

| Mã | Đặc tính / đặc tính con (ISO 25010:2023) | Yêu cầu | Thước đo | Ngưỡng | Điều kiện đo | Cách kiểm chứng | Bằng chứng | Ưu tiên | Chủ sở hữu | Nguồn |
|---|---|---|---|---|---|---|---|---|---|---|

Cú pháp một câu NFR: "Hệ thống PHẢI/NÊN [hành vi] đạt [thước đo] [ngưỡng], đo [ở đâu, điều kiện, phân vị/khoảng thời gian], kiểm chứng bằng [phương pháp]."

## Ví dụ (minh họa, con số lấy từ thresholds.md)
| NFR-PERF-01 | Performance efficiency / Time behaviour | Trang chi tiết sản phẩm tải nhanh | LCP | ≤ 2,5 s tại phân vị 75 | Dữ liệu người dùng thật (field) trên mobile, mạng 4G | Giám sát RUM hàng tuần | (b) | Must | Frontend lead | web.dev Core Web Vitals |
| NFR-REL-01 | Reliability / Availability | Dịch vụ thanh toán sẵn sàng | Tỷ lệ yêu cầu thành công | [CHỐT VỚI PO, ví dụ 99,9% = tối đa ≈ 43 phút ngừng/tháng] | Cửa sổ 30 ngày, đo tại cổng API, không tính bảo trì báo trước | Dashboard SLO | (c) | Must | SRE | tính từ SLO |
| NFR-INC-01 | Interaction capability / Inclusivity | Giao diện web đạt WCAG 2.2 Level AA | Số tiêu chí AA không đạt | 0 tiêu chí trên các luồng chính | Công cụ tự động và kiểm tra thủ công | Kiểm tra trước phát hành | (b) | Should | UX lead | WCAG 2.2 |

## Cuối mỗi bản NFR
**Trade-off cần chốt**: ...
**Cần xác nhận**: số chưa có nguồn, mục pháp lý ⚠️ (cần pháp chế), câu hỏi cho PO/kỹ thuật.
