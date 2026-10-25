# Chín đặc tính chất lượng (BABOK v3, mục 7.2.4.1, tr. 143; định nghĩa diễn đạt lại, câu hỏi kiểm và lỗi điển hình là của skill)

BABOK nói yêu cầu chấp nhận được thường thể hiện **nhiều** (không nhất thiết đủ chín) đặc tính, và mức "đủ" tùy phương pháp, giai đoạn, đối tượng. Đừng đòi mọi mục đạt mọi đặc tính ở mức tối đa.

| Đặc tính | Ý nghĩa | Câu hỏi kiểm | Lỗi điển hình | Cách sửa |
|---|---|---|---|---|
| Atomic (nguyên tử) | Tự đứng được, hiểu độc lập với yêu cầu khác | Có phải đọc mục khác mới hiểu? Có chứa hai điều kiện/hai hành vi trong một câu? | "Hệ thống cho phép đặt và hủy và đổi lịch" | Tách thành mục riêng, mỗi mục một mã |
| Complete (đủ) | Đủ để làm tiếp ở mức chi tiết phù hợp giai đoạn | Thiếu vai trò, điều kiện, ngoại lệ, dữ liệu vào/ra, thông báo lỗi? | Chỉ có đường vui; thiếu "khi hết chỗ thì sao" | Thêm hoặc đưa vào mục cần làm rõ; ghi rõ mức đủ mong đợi |
| Consistent (nhất quán) | Khớp nhu cầu stakeholder, không mâu thuẫn mục khác | Hai mục nói khác nhau về cùng một đối tượng? Thuật ngữ đổi nghĩa? | Mục A: hủy trước 4 giờ; mục B: hủy bất cứ lúc nào | Nêu cặp mâu thuẫn, người quyết |
| Concise (gọn) | Không thừa nội dung | Có câu không giúp ai hiểu hay làm gì? Có lặp lại? | Giải thích lịch sử dự án trong từng yêu cầu | Xóa hoặc chuyển sang phần bối cảnh |
| Feasible (khả thi) | Trong tầm rủi ro, tiến độ, ngân sách đã thống nhất, hoặc đủ để thử nghiệm | Có ràng buộc kỹ thuật/pháp lý/nguồn lực làm nó không làm được? | "Khớp 100% mọi nha sĩ trên mọi thiết bị cũ" | Hỏi đội kỹ thuật; đề xuất thử nghiệm hoặc thu hẹp |
| Unambiguous (không mơ hồ) | Rõ ràng đến mức phân định được giải pháp đáp ứng hay không | Hai người đọc có hiểu khác nhau? Từ như nhanh, dễ, phù hợp, đầy đủ, v.v. không kèm tiêu chí? | "Hiển thị nhanh", "thân thiện" | Thêm tiêu chí quan sát được; NFR thì đo được (nfr-writer) |
| Testable (kiểm chứng được) | Có cách xác minh đã đáp ứng | Tester viết được test pass/fail chưa? Có đầu vào, hành động, kết quả quan sát được? | "Hệ thống xử lý đúng" | Nêu trạng thái dữ liệu, thông báo, nơi hiển thị |
| Prioritized (có ưu tiên) | Đã xếp hạng, nhóm hoặc thương lượng so với mục khác | Có mức ưu tiên và cơ sở chưa? | Mọi thứ đều "cao" | requirements-prioritize |
| Understandable (dễ hiểu) | Dùng thuật ngữ quen của người đọc | Người dùng tài liệu có hiểu mà không cần giải thích? Từ viết tắt đã giải nghĩa? | Dùng thuật ngữ dev trong tài liệu cho lễ tân | Thêm glossary, đổi từ |

Ghi chú: BABOK nói mức "đủ" (Complete) phụ thuộc phương pháp và thời điểm trong vòng đời, và mức kiểm chứng chấp nhận được của Testable phụ thuộc mức trừu tượng của yêu cầu (7.2.4.1). Mục ở mức cao có thể kiểm ở mức cao.

## Bổ sung từ ISO/IEC/IEEE 29148:2018 (không thuộc BABOK)
Chuẩn có chín đặc tính của từng yêu cầu (5.2.5), trong đó **Necessary, Appropriate, Correct, Conforming** không có tên riêng ở BABOK, và năm đặc tính của cả tập (5.2.6). Khi rà soát có thể hỏi thêm: yêu cầu còn cần không (Necessary); đang nêu giải pháp thay vì nhu cầu (Appropriate); stakeholder đã xác nhận đúng nhu cầu chưa (Correct). Ghi phát hiện dưới đặc tính BABOK gần nhất, kèm nhãn "(29148)" nếu dựa trên đặc tính chỉ có ở chuẩn. Danh sách nhóm từ mơ hồ ở 5.2.7 dùng cho Unambiguous và Testable. Chi tiết và số điều: `iso29148.md`.

## Cách chấm
Với mỗi mục, đánh dấu đặc tính **vi phạm** (không đánh dấu "đạt" từng ô cho gọn; liệt kê đặc tính đã kiểm ở phạm vi). Lỗi lặp đi lặp lại ở nhiều mục: gộp thành một phát hiện kiểu "mẫu lỗi" kèm ví dụ và số lượng, tránh liệt kê trăm dòng.
