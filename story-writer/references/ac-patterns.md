# Cách viết acceptance criteria và use case

## Hai dạng AC
1. **Danh sách quy tắc** (đơn giản, nhanh): mỗi dòng một điều kiện kiểm chứng được. Dùng khi hành vi tuyến tính hoặc là quy tắc dữ liệu.
2. **Given/When/Then** (BABOK 10.48.3 nêu đây là dạng phổ biến): Given = trạng thái ban đầu, When = một hành động, Then = kết quả quan sát được. Dùng khi có ngữ cảnh/trạng thái. Mỗi kịch bản một When; Then nêu rõ kết quả (thông báo, trạng thái dữ liệu, chuyển trang), tránh "hệ thống hoạt động đúng".
Chọn một dạng cho mỗi story, không trộn lẫn.

## Ca biên cần dò cho mỗi story
- Dữ liệu: rỗng, một phần tử, tối đa, vượt tối đa, ký tự đặc biệt, trùng lặp, định dạng sai.
- Quyền/vai trò: người không có quyền, hết phiên, nhiều người cùng sửa.
- Trạng thái: thao tác khi đối tượng ở trạng thái không hợp lệ (đã hủy, đã khóa, đã xóa).
- Gián đoạn: mất mạng giữa chừng, bấm hai lần, quay lại, hủy.
- Tích hợp: hệ thống ngoài chậm/lỗi/trả về bất thường.
- Thông báo lỗi: nêu cái gì sai và làm gì tiếp.
- Dấu vết: có cần ghi nhật ký/kiểm toán không (nếu có → xem NFR bảo mật).
Mục nào không áp dụng thì bỏ qua, mục nào chưa rõ thì đưa vào "Cần làm rõ".

## Use case (BABOK 10.47, tr. 356–358)
Thành phần: tên (động từ + mục tiêu), tác nhân chính và phụ (tác nhân là người/hệ thống bên ngoài, không phải sự kiện), điều kiện tiên quyết (đúng trước khi bắt đầu, không kiểm trong use case), kích hoạt (trigger), luồng chính (đường thành công ngắn nhất), luồng thay thế (vẫn đạt mục tiêu bằng đường khác), luồng ngoại lệ (không đạt mục tiêu, hệ thống phản hồi thế nào), hậu điều kiện/đảm bảo (đúng ở mọi luồng; đảm bảo thành công và đảm bảo tối thiểu khi thất bại).
Lưu ý của BABOK: quy tắc và quyết định nghiệp vụ nên quản lý riêng rồi dẫn chiếu; đừng ghi mọi tương tác giao diện từng bước; use case không bàn thiết kế giải pháp.

## Bảng quy tắc nghiệp vụ (đề xuất)
| Mã | Quy tắc | Nguồn/chủ sở hữu | Áp dụng cho story |
Dùng khi có điều kiện, ngưỡng, công thức. Story chỉ ghi "theo BR-03".

## Tiêu chí chấp nhận theo BABOK 10.1 (tr. 217–220; diễn đạt lại)
- **Acceptance criteria** là điều kiện tối thiểu để giải pháp đáng được triển khai/nghiệm thu; thường dùng khi chỉ xét một giải pháp và viết dạng **đạt/không đạt**. **Evaluation criteria** dùng để xếp hạng nhiều phương án, nên là thang đo liên tục/rời rạc. Đừng trộn hai loại: story của một chức năng dùng acceptance criteria.
- Phải **kiểm chứng được đúng/sai**. BABOK nói có thể phải **tách yêu cầu về dạng nguyên tử** để viết được test case. Một AC chứa hai điều kiện thì tách đôi.
- Gốc là **value attributes** (thuộc tính giá trị mà stakeholder đã đồng ý định nghĩa). AC nào dựa trên thuộc tính chưa ai thống nhất nghĩa thì ghi vào "Cần làm rõ".
- Khi yêu cầu là nghĩa vụ hợp đồng, AC khó đổi về sau (giới hạn do BABOK nêu): chốt kỹ trước khi ký.
- Phương pháp kiểm: thường qua UAT. Mỗi AC nên trả lời được "ai kiểm, bằng dữ liệu nào, quan sát gì".

## Given-When-Then theo Agile Extension 7.2 (tr. 60)
Mỗi kịch bản: một tình huống (GIVEN, nối thêm bằng AND), **đúng một sự kiện kích hoạt** (WHEN), kết quả (THEN, có thể nhiều AND). Mỗi kịch bản một ví dụ cụ thể có số liệu. Muốn bao phủ: hỏi "nếu... thì sao" cho từng GIVEN. Khi tổ hợp điều kiện quá nhiều, chuyển sang bảng quyết định thay vì tăng số kịch bản.
