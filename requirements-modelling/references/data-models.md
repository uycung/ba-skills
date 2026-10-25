# Mô hình dữ liệu, khái niệm, từ điển dữ liệu

## Concept model (BABOK 10.11, tr. 245–246; diễn đạt lại)
Bắt đầu từ glossary các danh từ cốt lõi của miền; ưu tiên định nghĩa độc lập thiết kế, không thiên về dữ liệu hay công nghệ; từ vựng phong phú để diễn đạt quy tắc bằng ngôn ngữ tự nhiên. Danh từ (noun concept) nối bằng cụm động từ chuẩn (verb concept) để làm khối xây câu quy tắc. Hợp khi: cần tổ chức tri thức, có nhiều quy tắc, stakeholder ngại tính "kỹ thuật" của mô hình dữ liệu, miền tuân thủ quy định. **Khác mô hình dữ liệu**: mục tiêu là ngữ nghĩa, không phải gộp và đơn giản hóa dữ liệu.

## Data model (10.15, tr. 256–260)
- Ba mức: **conceptual** (độc lập công nghệ, từ vựng nghiệp vụ), **logical** (chuẩn hóa, gắn với thiết kế giải pháp), **physical** (tổ chức cơ sở dữ liệu, hiệu năng, đồng thời, bảo mật). BA thường làm conceptual; logical/physical do người triển khai.
- Phần tử: **Entity/Class** (vật lý, tổ chức, trừu tượng hoặc sự kiện, ví dụ BABOK: Appointment; có định danh duy nhất cho từng thể hiện), **Attribute** (tên, giá trị hợp lệ/ý nghĩa, mô tả; chi tiết đặt ở từ điển dữ liệu; giá trị cho phép có thể do quy tắc nghiệp vụ), **Relationship** (và **cardinality**: số lần xuất hiện tối thiểu và tối đa mỗi phía, thường 0, 1, nhiều; đọc hai chiều: "mỗi X liên quan (min, max) Y"), **Diagram** (ERD hoặc class diagram), object diagram minh họa thể hiện thật với giá trị mẫu.
**Cách làm với skill**
1. Liệt kê danh từ từ glossary/tài liệu; loại cái là thuộc tính hay từ đồng nghĩa.
2. Với mỗi thực thể: định danh, thuộc tính chính.
3. Hỏi quan hệ hai chiều và bội số (một người đặt có nhiều lịch hẹn? một lịch hẹn có nhiều người khám?). Chỗ chưa biết: "?".
4. Thêm một ví dụ cụ thể (object diagram dạng bảng giá trị mẫu) để chuyên gia dễ kiểm.
**Kiểm tra**: mọi thực thể có định danh; mọi quan hệ có bội số hai chiều; không thuộc tính trùng ở hai thực thể; thực thể trong mô hình có xuất hiện trong quy trình/story/BR và ngược lại; tên khớp glossary.
**Cảnh báo bảo mật/pháp lý**: đánh dấu thực thể và thuộc tính là dữ liệu cá nhân hoặc nhạy cảm để chuyển `nfr-writer` (không tự gán mức nhạy cảm theo luật).

## Data dictionary (10.12, tr. 247–250)
Chuẩn hóa định nghĩa phần tử dữ liệu và giá trị cho phép; thường đi kèm ERD, có thể trích từ mô hình dữ liệu; có thể là bảng tính.
- **Phần tử nguyên thủy** ghi: Name (duy nhất), Aliases (tên mà stakeholder dùng), Values/Meanings (danh sách giá trị hoặc định dạng, số ký tự; giá trị viết tắt phải giải nghĩa), Description.
- **Phần tử hợp thành** dùng: Sequence (thứ tự, ký hiệu +), Repetition, Optional.
Ví dụ BABOK: Customer Name = First Name + Middle Name + Family Name.
**Cột đề xuất**: Tên | Bí danh | Loại (nguyên thủy/hợp thành) | Giá trị/định dạng | Bắt buộc | Mô tả | Nguồn/quy tắc liên quan (BR) | Ghi chú dữ liệu cá nhân.
**Kiểm tra**: tên duy nhất; phần tử hợp thành chỉ chứa phần tử đã định nghĩa; giá trị viết tắt có giải nghĩa; không định nghĩa mâu thuẫn với glossary.
