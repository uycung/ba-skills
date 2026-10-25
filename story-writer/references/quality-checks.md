# Tiêu chí chất lượng và danh sách lỗi

## 1. Chín đặc tính của yêu cầu tốt (BABOK v3, mục 7.2.4, tr. 143)
Diễn đạt lại, đã đọc từ bản BABOK v3 người dùng cung cấp.
| Đặc tính | Hỏi khi tự kiểm |
|---|---|
| Atomic (đơn nhất) | Hiểu được một mình, không cần đọc câu khác? Chỉ nói một việc? |
| Complete (đủ) | Đủ chi tiết để đội bước tiếp (thiết kế, code, test) ở giai đoạn này? |
| Consistent (nhất quán) | Có mâu thuẫn với yêu cầu khác hoặc nhu cầu stakeholder đã biết? |
| Concise (súc tích) | Có chữ nào thừa, không ảnh hưởng đến hành vi? |
| Feasible (khả thi) | Làm được trong rủi ro, thời gian, ngân sách đã thỏa thuận? |
| Unambiguous (không mơ hồ) | Nhìn kết quả có phân định được đạt hay không đạt? |
| Testable (kiểm chứng được) | Có cách kiểm xem đã đáp ứng chưa? |
| Prioritized (có ưu tiên) | Đã xếp hạng so với yêu cầu khác? |
| Understandable (dễ hiểu) | Dùng thuật ngữ của người đọc? |
Lưu ý theo BABOK: chất lượng cuối cùng do stakeholder quyết định; mức chi tiết "đủ" phụ thuộc phương pháp và giai đoạn.

## 2. INVEST cho story (Agile Extension v2, mục 7.21.2, tr. 103; diễn đạt lại)
Independent (giao được độc lập với tính năng khác), Negotiable (đội thương lượng cách giao), Valuable (nêu giá trị cho khách hàng), Estimable (đội ước lượng được dựa trên kinh nghiệm), Sized appropriately (làm xong trong một iteration, nhìn chung càng nhỏ càng tốt), Testable (stakeholder kiểm chứng được một cách khách quan). Agile Extension nói không phải mục backlog nào cũng phải viết thành user story.
Lưu ý: BABOK Guide v3 chính không có INVEST; Agile Extension thì có. Việc gán nguồn gốc cho một tác giả cụ thể là kiến thức ngoài tài liệu, không dựa vào đó.

## 3. Khung story (BABOK v3, mục 10.48.3, tr. 360; Agile Extension 7.21, tr. 103–104)
BABOK nói không có cấu trúc bắt buộc. Dạng phổ biến: Ai (vai trò/persona), Gì (hành động/hành vi/tính năng/chất lượng cần), Vì sao (lợi ích). Thêm: tiêu đề tùy chọn (động từ + mục tiêu), "conversation" (phần trao đổi bổ sung khi triển khai), và acceptance criteria để giới hạn phạm vi story. Giới hạn nên nhớ: story là công cụ ghi nhanh và ưu tiên ngắn hạn, không thay cho lưu trữ tri thức dài hạn hay phân tích chi tiết; có thể cần tài liệu bổ sung cho quản trị và baseline.

## 4. Lỗi thường gặp và cách sửa
| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Từ mơ hồ | nhanh, dễ, thân thiện, hợp lý, đầy đủ, linh hoạt, "v.v." | Thay bằng điều kiện quan sát được; nếu là chất lượng (hiệu năng, dễ dùng) → chuyển sang NFR có thước đo |
| Giải pháp thay vì nhu cầu | "dùng dropdown", "thêm nút X" khi chưa rõ mục tiêu | Viết mục tiêu người dùng trước; chi tiết giao diện để phần thiết kế/prototype |
| Story giả | "Là developer, tôi muốn refactor...", "Là hệ thống, tôi muốn..." | Viết là task kỹ thuật hoặc gắn vào story có giá trị người dùng |
| Vai trò chung chung | "Là người dùng..." | Dùng vai trò cụ thể và phân biệt quyền |
| Story quá lớn | nhiều "và/hoặc", nhiều vai trò, AC hơn khoảng 8 | Tách theo lát cắt dọc (một luồng đi hết các tầng), không tách theo tầng kỹ thuật |
| AC chỉ có đường vui | không có lỗi, rỗng, trùng, quyền, hủy giữa chừng | Dò ca biên (xem ac-patterns.md) |
| Nhiều quy tắc trong một câu | "Nếu A hoặc B và không C..." | Chuyển thành bảng quyết định/bảng quy tắc |
| Quy tắc nghiệp vụ chôn trong bước thao tác | số, ngưỡng, điều kiện nằm giữa luồng | Tách bảng quy tắc, có mã (BR-xx), story dẫn chiếu |
| Thiếu kết quả quan sát được | "hệ thống xử lý đúng" | Nêu trạng thái dữ liệu, thông báo, nơi hiển thị |
| Không có "ngoài phạm vi" | tranh cãi khi nghiệm thu | Ghi rõ những gì cố ý không làm |

## 5. Bổ sung từ Agile Extension v2 (tr. 102–105)
- **3C**: Card (thẻ ngắn), Conversation (cuộc trao đổi, story cố ý không chứa hết mọi điều), Confirmation (xác nhận qua acceptance criteria, giới hạn phạm vi story và là cơ sở cho acceptance/regression/exploratory test).
- Hai mẫu câu: "As a <role>, I need to <feature> so that <goal or value>" và "In order to <value>, as a <role>, I need to <behaviour>". Tiêu đề tùy chọn dạng động từ + mục tiêu.
- **Giới hạn** AE nêu: quá nhiều story làm phình backlog; story đẻ thêm story nên phải giữ thông tin cập nhật; đội dễ sa vào từng story mà mất tầm nhìn/roadmap; đội dễ thành thói quen bỏ qua phần giá trị (WHY) để chỉ nhìn tính năng (WHAT). Dò lỗi cuối khi rà soát.
- Nhiều đội bổ sung story bằng mô hình phân tích: mô hình dữ liệu, quy tắc nghiệp vụ, UAT, mock-up, context diagram, state diagram.
- **Definition of Ready / Done** (glossary AE tr. 5, không có mục riêng): bộ tiêu chí đội thống nhất và trưng bày để coi mục backlog là "sẵn sàng bắt đầu" hoặc "xong". Hỏi đội xem đã có chưa; nếu có thì kiểm story theo đó.
- **ISO/IEC/IEEE 29148:2018, 5.2.4 NOTE 2** (bản chuẩn đã đọc): trong agile, yêu cầu có thể diễn đạt như user story mà không dùng "shall". Chuẩn vẫn đòi yêu cầu tốt phải đủ các đặc tính ở 5.2.5 (Necessary, Appropriate, Unambiguous, Complete, Singular, Feasible, Verifiable, Correct, Conforming); story cùng AC được đánh giá theo các đặc tính đó khi tổ chức yêu cầu tuân thủ 29148. Ghi chú đối chiếu: `requirements-review/references/iso29148.md`.
