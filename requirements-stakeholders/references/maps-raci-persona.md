# Bản đồ, RACI, persona

## Ma trận stakeholder (BABOK 10.43.3.2)
Hai trục: **ảnh hưởng** của stakeholder; **quan tâm** (văn bản mô tả) hay **tác động lên stakeholder** (nhãn hình trong sách). Văn bản của mục 10.43 nói ma trận ánh xạ ảnh hưởng với quan tâm, còn chú giải bốn góc dùng "tác động". Khi dùng, chọn một trục và nói rõ với người dùng đã chọn trục nào.
Bốn góc (diễn đạt lại):
| Ảnh hưởng | Quan tâm/tác động | Cách làm việc theo BABOK |
|---|---|---|
| Cao | Cao | Người chơi chính: tập trung nỗ lực, gắn kết thường xuyên, làm việc sát để họ đồng ý và ủng hộ thay đổi. |
| Cao | Thấp | Có nhu cầu cần đáp ứng: tham vấn, giữ họ hài lòng, tìm cách tăng mức quan tâm. |
| Thấp | Cao | Người ủng hộ và đại sứ thiện chí tiềm năng: lấy ý kiến, thể hiện quan tâm đến nhu cầu của họ; họ có thể lo lắng vì thiếu kiểm soát nên cần được thông tin. |
| Thấp | Thấp | Thông tin chung; theo dõi để đảm bảo mức quan tâm hay ảnh hưởng không đổi; gắn kết thêm có thể đưa họ lên nhóm ủng hộ. |
Cách làm: đặt từng stakeholder/nhóm vào ô, kèm nhãn nguồn. Vị trí là phán đoán: gắn [Suy luận] trừ khi đã xác nhận. Một chữ "?" cũng được chấp nhận.

## Sơ đồ onion (10.43.3.2)
Các vòng từ trong ra ngoài (diễn đạt lại): **Giải pháp** (nhóm triển khai và người trực tiếp tạo giải pháp) → **Đơn vị bị ảnh hưởng** (người dùng cuối, hỗ trợ, người có công việc thay đổi) → **Tổ chức/doanh nghiệp** (sponsor, lãnh đạo, chuyên gia nghiệp vụ, người tương tác với đơn vị bị ảnh hưởng) → **Bên ngoài** (khách hàng, nhà cung cấp, cơ quan quản lý). Dùng khi muốn thấy độ gần với giải pháp và ranh giới tổ chức.
Có thể vẽ nhanh bằng Mermaid (công cụ vẽ, không phải ký hiệu BABOK) hoặc bảng 4 dòng.

## RACI (10.43.3.3)
- **R** (Responsible): người thực hiện công việc.
- **A** (Accountable): người chịu trách nhiệm cuối cùng và quyết định; **chỉ một người**.
- **C** (Consulted): được hỏi ý kiến, hai chiều, thường là SME.
- **I** (Informed): được cập nhật, một chiều (BA đến stakeholder).
Quy trình: (1) chắc chắn đã có đủ stakeholder; (2) liệt kê hoạt động/sản phẩm bàn giao; (3) gán R/A/C/I; (4) **định nghĩa các chữ cái** trong tài liệu để mọi người hiểu giống nhau; (5) xác nhận với các bên.
Kiểm: mỗi hàng có đúng một A và ít nhất một R; không hàng nào toàn C/I; stakeholder không có ô nào nên xem lại có cần ở trong danh sách; một người không vừa R vừa A cho mọi hàng (dấu hiệu quá tải).
RACI này ở mức sáng kiến. Ma trận quyền CRUD ở mức hệ thống thuộc `requirements-modelling` (10.39).
Ví dụ trong BABOK là RACI cho quy trình yêu cầu thay đổi (sponsor, BA, quản lý dự án, nhà phát triển, tester...).

## Persona (BABOK 10.43.3.4; Agile Extension 7.7)
- Persona là nhân vật hư cấu đại diện cách người dùng điển hình dùng giải pháp, nhưng dựng từ nghiên cứu về nhóm người dùng thật (phỏng vấn, khảo sát) nên dựa trên hiểu biết chứ không phải ý kiến. Viết dạng kể chuyện, tập trung mục tiêu của nhóm.
- Mẫu ngắn (một trang): tên, bối cảnh/chi tiết, nhiệm vụ và trách nhiệm, công nghệ dùng, đặc điểm (tuổi, nghề, nơi ở), mục tiêu. Mẫu dài thêm động cơ mua, nhân khẩu, đặc điểm, nhu cầu, động lực, điểm khác biệt (Agile Extension 7.7.3).
- Persona được xếp hạng để biết ai hưởng lợi nhiều nhất từ thiết kế (7.7.2).
- Nhu cầu hữu hạn còn mong muốn thì vô hạn: ghi nhu cầu cụ thể, không ghi mong muốn chung chung (7.7.3.5).
**Quy tắc của skill**:
- Chỉ viết persona khi có dữ liệu. Mỗi trường gắn nguồn (số cuộc phỏng vấn, khảo sát). Không có: nhãn "Giả thuyết" + kế hoạch kiểm chứng.
- Không dùng thông tin nhạy cảm (sức khỏe, tôn giáo, v.v.) trừ khi liên quan trực tiếp nhu cầu và có sự đồng ý.
- Persona khác nhau phải khác nhau ở **điểm khác biệt** (differentiators), nếu không thì gộp.
- Đừng đồng nhất persona với vai trò hệ thống (phân quyền); persona nói về con người và nhu cầu.
