# Cây ISO/IEC 25010:2023: 9 đặc tính, 40 đặc tính con

Tên các đặc tính và đặc tính con khớp bản 2023. Cột "Ý nghĩa" là diễn đạt lại của skill, **chưa đối chiếu với định nghĩa chính thức** (bản đầy đủ nằm sau paywall). Chất lượng sử dụng (quality in use) đã chuyển sang ISO/IEC 25019:2023, không thuộc cây này. Tệp tổng hợp 40 đặc tính con do người dùng cung cấp tự mô tả là "định nghĩa chính thức" nhưng không có trích dẫn điều khoản; đã so tên với bảng này (khớp cấu trúc), còn câu định nghĩa trong tệp đó vẫn là nguồn thứ cấp chưa kiểm chứng nên không thay cột "Ý nghĩa".
Thay đổi so với bản 2011: thêm Safety, tách Interaction capability (thay Usability), Flexibility (thay Portability), "faultlessness" thay "maturity", "resistance" thay "integrity" ở Security, thêm scalability và các đặc tính con mới.

## 1. Functional suitability (3)
| Đặc tính con | Ý nghĩa (diễn đạt lại) | Câu hỏi NFR gợi ý |
|---|---|---|
| Functional completeness | Chức năng có bao phủ đủ nhiệm vụ cần làm | Tỷ lệ use case/nhiệm vụ được phủ? |
| Functional correctness | Kết quả đúng, đủ độ chính xác | Sai số cho phép? Quy tắc tính toán nào bắt buộc đúng 100%? |
| Functional appropriateness | Chức năng giúp hoàn thành nhiệm vụ đúng cách, không thừa bước | Số bước tối đa cho nhiệm vụ chính? |

## 2. Performance efficiency (3)
| Đặc tính con | Ý nghĩa | Câu hỏi gợi ý |
|---|---|---|
| Time behaviour | Thời gian phản hồi, xử lý, thông lượng | Phân vị nào, ở tải nào, trên thiết bị/mạng nào? |
| Resource utilization | Lượng CPU, bộ nhớ, pin, băng thông | Trần tài nguyên? Mức tiêu thụ pin trên mobile? |
| Capacity | Giới hạn tối đa hệ thống chịu được | Số người dùng đồng thời, giao dịch/giây, dung lượng dữ liệu? |

## 3. Compatibility (2)
| Đặc tính con | Ý nghĩa (diễn đạt lại) | Câu hỏi gợi ý |
|---|---|---|
| Co-existence | Chạy chung môi trường với sản phẩm khác không ảnh hưởng nhau | Hệ thống nào dùng chung hạ tầng? |
| Interoperability | Trao đổi dữ liệu được với hệ thống khác | Chuẩn, phiên bản API, định dạng nào? |

## 4. Interaction capability (8)
| Đặc tính con | Ý nghĩa (diễn đạt lại) | Câu hỏi gợi ý |
|---|---|---|
| Appropriateness recognizability | Người dùng nhận ra sản phẩm có phù hợp nhu cầu | Tỷ lệ người mới hiểu mục đích trong N giây? |
| Learnability | Học dùng nhanh | Thời gian/ tỷ lệ hoàn thành tác vụ lần đầu? |
| Operability | Dễ thao tác, điều khiển | Số thao tác, hỗ trợ bàn phím/cảm ứng? |
| User error protection | Ngăn, phát hiện, giúp sửa lỗi của người dùng | Xác nhận hành động nguy hiểm, hoàn tác? |
| User engagement | Giao diện hấp dẫn, giữ người dùng tham gia | Chỉ số tương tác nào cần đạt? |
| Inclusivity | Nhiều nhóm người dùng khác nhau dùng được | Mức WCAG? Ngôn ngữ? Người khuyết tật? |
| User assistance | Có hỗ trợ khi người dùng cần | Trợ giúp ngữ cảnh, kênh hỗ trợ? |
| Self-descriptiveness | Giao diện tự giải thích | Thông báo, nhãn, trạng thái hệ thống rõ? |

## 5. Reliability (4)
| Đặc tính con | Ý nghĩa (diễn đạt lại) | Câu hỏi gợi ý |
|---|---|---|
| Faultlessness | Hoạt động đúng, ít lỗi trong điều kiện bình thường | Mật độ lỗi, MTBF mục tiêu? |
| Availability | Sẵn sàng khi cần | SLO %, cửa sổ tính, loại trừ bảo trì? |
| Fault tolerance | Chạy tiếp khi có sự cố thành phần | Điểm lỗi đơn nào chấp nhận được? |
| Recoverability | Phục hồi sau sự cố | RTO, RPO, tần suất kiểm thử khôi phục? |

## 6. Security (6)
| Đặc tính con | Ý nghĩa (diễn đạt lại) | Câu hỏi gợi ý |
|---|---|---|
| Confidentiality | Chỉ người có quyền mới truy cập | Phân loại dữ liệu, mã hóa lưu trữ/truyền? |
| Integrity | Ngăn sửa đổi trái phép | Kiểm soát toàn vẹn, chữ ký, kiểm toán? |
| Non-repudiation | Không chối bỏ được hành động | Hành động nào cần bằng chứng? |
| Accountability | Truy vết hành động về chủ thể | Nhật ký gì, giữ bao lâu? |
| Authenticity | Xác thực danh tính/nguồn gốc | Phương thức xác thực, MFA? |
| Resistance | Chống chịu tấn công | Mức ASVS? Danh mục OWASP? Thời gian vá lỗ hổng? |

## 7. Maintainability (5)
| Đặc tính con | Ý nghĩa (diễn đạt lại) | Câu hỏi gợi ý |
|---|---|---|
| Modularity | Thay đổi một phần ít ảnh hưởng phần khác | Ranh giới module, phụ thuộc? |
| Reusability | Tái sử dụng thành phần | Thành phần dùng chung nào? |
| Analysability | Dễ chẩn đoán lỗi, đánh giá tác động thay đổi | Log, trace, giám sát nào bắt buộc? |
| Modifiability | Sửa mà không phát sinh lỗi | Thời gian dẫn thay đổi, độ phức tạp? |
| Testability | Dễ kiểm thử | Mức phủ test theo rủi ro? |

## 8. Flexibility (4)
| Đặc tính con | Ý nghĩa (diễn đạt lại) | Câu hỏi gợi ý |
|---|---|---|
| Adaptability | Thích ứng môi trường/yêu cầu thay đổi | Cấu hình thay vì sửa code? |
| Scalability | Mở rộng khi tải tăng | Quy mô 12–24 tháng tới, cách mở rộng? |
| Installability | Cài/gỡ dễ | Thời gian triển khai, tự động hóa? |
| Replaceability | Thay thế sản phẩm khác cùng mục đích | Xuất/nhập dữ liệu, chống khóa nhà cung cấp? |

## 9. Safety (5)
| Đặc tính con | Ý nghĩa (diễn đạt lại) | Câu hỏi gợi ý |
|---|---|---|
| Operational constraint | Giữ trong giới hạn vận hành an toàn | Giới hạn nào không được vượt? |
| Risk identification | Nhận diện rủi ro gây hại | Phân tích hazard nào đã làm? |
| Fail safe | Lỗi thì rơi về trạng thái an toàn | Trạng thái an toàn là gì? |
| Hazard warning | Cảnh báo nguy cơ | Khi nào, bằng cách nào cảnh báo? |
| Safe integration | Tích hợp với hệ thống khác vẫn an toàn | Điều kiện tích hợp, kiểm thử? |
