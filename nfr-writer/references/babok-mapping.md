# Đối chiếu BABOK v3 với ISO/IEC 25010:2023

Nguồn BABOK: mục 2.3 (tr. 16), 10.30 (tr. 302–304), đã đọc từ bản người dùng cung cấp. Dùng bảng này khi stakeholder/BA quen thuật ngữ BABOK.

## BABOK nói gì về NFR
- NFR (còn gọi quality attributes, quality of service requirements) là loại con của **solution requirements**, bên cạnh functional requirements. NFR không nói về hành vi chức năng mà về điều kiện giải pháp phải đáp ứng để vẫn hiệu quả.
- NFR có thể áp dụng cả cho khía cạnh quy trình và con người, không chỉ phần mềm.
- Nên lượng hóa khi có thể để kiểm chứng được (ví dụ "90% phản hồi trong 2 giây" thay "phản hồi nhanh"). Ví dụ trong BABOK chỉ là minh họa, không phải ngưỡng chuẩn.
- Chứng nhận, tuân thủ, bản địa hóa: chi tiết đo lường do bên đặt chuẩn/quy định đưa ra; SLA nêu rõ thước đo thành công; kiến trúc doanh nghiệp xác định yêu cầu môi trường.
- Ngữ cảnh quyết định bộ NFR tối ưu, ngữ cảnh luôn đổi nên NFR có thể phải điều chỉnh hoặc bỏ.
- Giới hạn: kỳ vọng người dùng khác nhau, NFR có thể xung đột và cần thương lượng (ví dụ bảo mật so với hiệu năng), ràng buộc quá chặt tăng thời gian/chi phí, nhiều NFR mang tính định tính.
- **Transition requirements** (chuyển đổi dữ liệu, đào tạo, duy trì hoạt động) là loại riêng, không phải NFR (BABOK 2.3).

## Đối chiếu danh mục
| BABOK 10.30.3.1 | ISO/IEC 25010:2023 | Ghi chú |
|---|---|---|
| Availability | Reliability / Availability | BABOK: % thời gian sẵn sàng |
| Compatibility | Compatibility | Khớp |
| Functionality (phù hợp, chính xác, tương tác) | Functional suitability; phần "interoperability" thuộc Compatibility trong ISO | Khác chỗ xếp interoperability |
| Maintainability | Maintainability | Khớp |
| Performance Efficiency | Performance efficiency | Khớp |
| Portability | Flexibility (installability, adaptability, replaceability) | ISO 2023 đổi tên |
| Reliability | Reliability (faultlessness, fault tolerance, recoverability) | Khớp |
| Scalability | Flexibility / Scalability; một phần Performance efficiency / Capacity | ISO 2023 đưa scalability thành đặc tính con |
| Security | Security | ISO 2023 có 6 đặc tính con |
| Usability | Interaction capability | ISO 2023 đổi tên, mở rộng (inclusivity, user assistance...) |
| Extensibility | Flexibility / Modifiability (Maintainability) | Gần nhau |
| Certification | Không phải đặc tính chất lượng; là **nguồn** của yêu cầu | Ghi nhãn (a) và nêu chuẩn |
| Compliance | Như trên | Xem `legal-vn.md` |
| Localization | Một phần Inclusivity (ngôn ngữ), Adaptability | Hỏi riêng: ngôn ngữ, tiền tệ, định dạng |
| Service Level Agreements | Không phải đặc tính; là **hình thức cam kết** chứa các NFR (availability, performance...) | Ghi nguồn là SLA |
| (không có) | **Safety** (5 đặc tính con) | ISO bổ sung; BABOK không nêu |

## Có xung đột không?
Không có xung đột về nguyên tắc: cả hai đều yêu cầu NFR đo được, có ngữ cảnh, có thương lượng trade-off. Khác biệt cần lưu ý:
1. **Mức chi tiết**: BABOK là danh mục phẳng khoảng 14 mục, định nghĩa ngắn; ISO có 9 đặc tính, 40 đặc tính con và khung tùy biến (25002). Dùng ISO làm khung chính, BABOK làm cầu nối thuật ngữ.
2. **Chỗ xếp khác nhau**: interoperability; Compliance/Certification/Localization/SLA trong BABOK là nguồn hoặc ràng buộc, không phải đặc tính chất lượng trong ISO.
3. **Tên đổi**: Portability → Flexibility, Usability → Interaction capability. Khi trao đổi với người quen tên cũ, nêu cả hai.
4. **Phạm vi**: BABOK cho phép NFR về quy trình và con người; ISO 25010 chỉ nói chất lượng sản phẩm/hệ thống.
5. **Khoảng trống của ISO**: transition requirements không nằm trong ISO 25010. Khi gặp (chuyển đổi dữ liệu, đào tạo, vận hành song song), ghi thành mục riêng, không nhét vào đặc tính chất lượng.
