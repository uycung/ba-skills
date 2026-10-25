# Tiêu chí và phương pháp ưu tiên

## Tiêu chí (BABOK 5.3.4.1, tr. 88–89; diễn đạt lại, đã đọc từ bản người dùng cung cấp)
| Tiêu chí | Câu hỏi |
|---|---|
| Benefit (lợi ích) | Mang lại lợi thế gì cho stakeholder, đo theo mục tiêu của thay đổi? Nhóm nào hưởng? |
| Penalty (hậu quả nếu không làm) | Không làm thì mất gì (cả phạt theo quy định lẫn trải nghiệm khách hàng)? |
| Cost (chi phí) | Công sức và nguồn lực cần? (số liệu từ đội triển khai/nhà cung cấp) |
| Risk (rủi ro) | Khả năng không tạo ra giá trị hoặc không làm được (độ khó, stakeholder không chấp nhận)? Mục rủi ro kỹ thuật cao có thể làm sớm để biết sớm |
| Dependencies (phụ thuộc) | Phụ thuộc yêu cầu khác, hoặc quyết định/nguồn lực ngoài dự án? |
| Time sensitivity (nhạy theo thời gian) | Có hạn "tốt nhất trước ngày" (ra thị trường, mùa vụ)? |
| Stability (độ ổn định) | Khả năng yêu cầu còn đổi; chưa ổn định thì có thể ưu tiên thấp để tránh làm lại |
| Regulatory/Policy compliance | Bắt buộc theo quy định/chính sách? Có thể ưu tiên trên các lợi ích khác |

## Cách sắp xếp (BABOK 10.33.3, tr. 313)
- **Grouping**: xếp vào nhóm cao/trung bình/thấp, là thuộc tính của yêu cầu.
- **Ranking**: xếp thứ tự từ quan trọng nhất; dùng khi cần thứ tự rõ (backlog).
- **Time boxing/Budgeting**: ưu tiên theo nguồn lực cố định (thời gian hoặc ngân sách), dùng khi có hạn cố định.
- **Negotiation**: đạt đồng thuận giữa stakeholder.

## Khung bổ sung phổ biến (không có trong phần BABOK đã đọc; dùng như công cụ thảo luận, không phải chuẩn)
MoSCoW (Must/Should/Could/Won't), RICE, bảng giá trị–công sức. Khi dùng, nói rõ đây là khung bổ sung và giải thích cách chấm.

## Thách thức và thiên lệch (BABOK 5.3.4.2 và 10.33.4)
Stakeholder khó nhận mục nào thấp ưu tiên nên khó đánh đổi; có thể điều chỉnh khai báo để ảnh hưởng kết quả; đội giải pháp có thể phóng đại độ phức tạp; thiếu KPI/số liệu nên đánh giá mang tính chủ quan. Cách giảm: tiêu chí thống nhất trước, lý do bằng văn bản cho từng điểm, nhiều góc nhìn, kiểm chứng ước lượng chi phí với người thứ hai.

## Bổ sung từ phần BABOK đọc thêm
- **Backlog nhiều pha (10.2.3, tr. 221)**: lúc mới vào backlog chỉ cần nhóm rộng cao/trung bình/thấp; mục cao được xem lại thường xuyên hơn; để phân biệt các mục cao với nhau mới chuyển sang xếp hạng số theo một thước đo giá trị. Mục ở đầu được mô tả và ước lượng kỹ hơn. Backlog xem lại định kỳ và theo dõi xu hướng quy mô (tăng có thể do cầu tăng hoặc năng suất giảm). Có thể có nhiều backlog (toàn cục và gần hạn).
- **Bốn cách ở 10.33 (tr. 311–313) ánh xạ vào quy trình**: Grouping (cao/trung/thấp, thuộc tính yêu cầu); Ranking (danh sách có thứ tự, ví dụ product backlog); Time boxing/Budgeting (nguồn lực cố định, dùng khi có hạn cố định hoặc cải tiến đều đặn); Negotiation (đồng thuận giữa stakeholder). Chọn theo khán giả và nhu cầu; có thể đổi cách khi bối cảnh đổi.
- **Yếu tố khi đánh giá thay đổi (5.4.4, tr. 93)**: benefit, cost (gồm làm lại và chi phí cơ hội), impact (số khách hàng/quy trình), schedule, urgency (gồm quy định, an toàn). Dùng khi ưu tiên lại do yêu cầu đổi.
- **MoSCoW**: BABOK v3 mục 11.1.2 liệt kê (must, should, could, won't have) nhưng Agile Extension v2 đã **bỏ** kỹ thuật này, nên không có nguồn chi tiết trong tài liệu mình có; dùng như khung phổ biến, nói rõ cách định nghĩa từng nhóm. RICE không có trong BABOK.
- **Kano (AE 7.5, tr. 66–69)**: phân đặc tính thành threshold (thiếu thì rất bất mãn, có cũng không tăng hài lòng nhiều), performance (càng nhiều càng hài lòng, gần tuyến tính), excitement (vượt kỳ vọng, khách chưa biết mình muốn), indifferent (không giá trị). Hỏi hai dạng: "có tính năng thì bạn thấy thế nào" và "không có thì thế nào", mỗi câu năm mức (thích, mong đợi, trung lập, chịu được, không thích), đối chiếu bảng để ra E/P/T/I/Q/R. Giới hạn do AE nêu: chỉ đo mức hài lòng nên phải kết hợp yếu tố khác khi xếp backlog; phân loại đổi theo thời gian (excitement thành threshold).
- **MVP (AE 7.6, tr. 69–71)**: tập yêu cầu nhỏ nhất để kiểm chứng một giả thuyết và có phản hồi sớm. Bước: xác định vấn đề và giả thuyết, chọn tập tính năng tối thiểu để thử, phân tích điều học được. Cần có: nhóm đối tượng và early adopter, giả thuyết/mục tiêu, cách đo điều học được, yêu cầu tối thiểu. Giới hạn: không có công thức, số tính năng là phán đoán; không hợp khi giải pháp đã rõ và đơn giản (khi đó MVP chính là sản phẩm đầy đủ).
- **Persona (AE 7.7)**: xếp hạng persona để biết nhóm nào hưởng lợi nhiều nhất, rồi ưu tiên tính năng theo mức đáp ứng nhu cầu persona.
- **Phê duyệt**: thứ tự ưu tiên chỉ có giá trị khi người có thẩm quyền duyệt (5.5); xung đột chưa giải quyết phải ghi như rủi ro.
