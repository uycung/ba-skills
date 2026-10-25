# Chọn mô hình (BABOK 7.1.4.1, tr. 138–139; ghép câu hỏi với mô hình là gợi ý của skill)

## Hai dạng biểu diễn
- **Ma trận**: khi cấu trúc phức tạp nhưng đồng đều, chia được thành các phần tử áp dụng cho mọi dòng (từ điển dữ liệu, truy vết, phân tích khoảng cách, ưu tiên, thuộc tính).
- **Sơ đồ**: để thể hiện độ phức tạp khó nói bằng chữ, vẽ ranh giới miền, phân loại và phân cấp, thành phần của đối tượng dữ liệu và quan hệ.

## Năm nhóm mô hình (BABOK) và kỹ thuật
| Nhóm | Mô hình thể hiện | Kỹ thuật |
|---|---|---|
| Con người và vai trò | Tổ chức, nhóm, vai trò và quan hệ với giải pháp | Organizational Modelling, Roles and Permissions Matrix, Stakeholder List/Map/Personas |
| Lý do (rationale) | Vì sao thay đổi | Decision Modelling, Scope Modelling, Business Model Canvas, Root Cause Analysis, Business Rules Analysis |
| Luồng hoạt động | Chuỗi hành động, sự kiện | Process Modelling, Use Cases and Scenarios, User Stories |
| Năng lực | Tính năng/chức năng của tổ chức hay giải pháp | Business Capability Analysis, Functional Decomposition, Prototyping |
| Dữ liệu và thông tin | Đặc trưng và trao đổi thông tin | Data Dictionary, Data Flow Diagrams, Data Modelling, Glossary, State Modelling, Interface Analysis |
Dùng tổ hợp phù hợp nhất với stakeholder và bối cảnh; mỗi kỹ thuật có điểm mạnh và yếu riêng và cho góc nhìn khác nhau.

## Chọn theo câu hỏi (gợi ý của skill)
| Câu hỏi của người dùng | Mô hình |
|---|---|
| "Công việc đang chạy thế nào / sẽ chạy thế nào?" | Quy trình (as-is / to-be), làn theo vai trò |
| "Cái X (đơn, lịch hẹn, hồ sơ) đi qua những trạng thái nào, ai được làm gì ở mỗi trạng thái?" | Trạng thái |
| "Hệ thống phải lưu những thứ gì và chúng liên quan thế nào?" | Dữ liệu khái niệm + từ điển dữ liệu |
| "Cùng một thuật ngữ mà mỗi người hiểu một kiểu" | Glossary / concept model |
| "Khi A, B, C thì kết quả là gì?" | Bảng quyết định |
| "Người dùng làm gì để đạt mục tiêu, kể cả khi lỗi?" | Use case và kịch bản |
| "Cái gì trong, cái gì ngoài?" | Phạm vi (context diagram, bảng trong/ngoài) |
| "Chức năng này gồm những phần nào?" | Phân rã chức năng |
| "Hệ thống trao đổi gì với hệ thống/người khác?" | Phân tích giao diện, sơ đồ tuần tự |
| "Ai được làm gì?" | Ma trận vai trò và quyền (RACI, CRUD) |

## Mức trừu tượng (7.1.4.4)
Không phải stakeholder nào cũng cần toàn bộ mô hình. Có thể dựng nhiều viewpoint cho cùng một nhu cầu, nhưng phải giữ nguyên ý nghĩa và mục đích trên mọi biểu diễn. Cách làm của BA (predictive hay agile) cũng ảnh hưởng mức chi tiết và loại mô hình.

## Phân tích yêu cầu khi dựng mô hình (7.1.4.2)
Phân rã thông tin rồi xem: cái gì phải đổi, cái gì phải giữ nguyên, thiếu thành phần nào, thừa thành phần nào, ràng buộc và giả định nào ảnh hưởng. Mức chi tiết tùy hiểu biết của stakeholder, nguy cơ hiểu nhầm, chuẩn của tổ chức, nghĩa vụ hợp đồng và quy định.

## Thuộc tính của yêu cầu (7.1.4.3)
Ngoài mô hình, ghi thuộc tính/metadata của yêu cầu (chọn khi lập kế hoạch quản lý thông tin BA) và phân loại theo lược đồ phân loại yêu cầu (business, stakeholder, solution, transition).
