# Phạm vi, phân rã chức năng, giao diện, ma trận vai trò và quyền

## Scope modelling (BABOK 10.41, tr. 337–340; phần đầu)
Mô hình phạm vi xác định ranh giới và đặt phần tử bên trong hoặc ngoài. Trong phạm vi (như phân rã chức năng), ngoài phạm vi (như context diagram), hoặc cả hai (venn, use case model). Nhận diện bốn loại ranh giới: phạm vi kiểm soát (cái đang phân tích, vai trò, trong/ngoài tổ chức), phạm vi nhu cầu, phạm vi giải pháp (yêu cầu đáp ứng, giá trị, tác động thay đổi), phạm vi thay đổi (hành động, stakeholder, sự kiện). Thường kết hợp sơ đồ, ma trận và chữ. **Triển khai theo pha thì mô tả phạm vi theo từng pha**.
Cách làm: bảng Trong / Ngoài (cố ý) / Chưa quyết, kèm lý do ngoài phạm vi; context diagram cho thấy hệ thống ở giữa và các tác nhân/hệ thống ngoài. Phần sau của mục 10.41 chưa đọc.

## Functional decomposition (10.22, tr. 283–286; diễn đạt lại)
Chia quy trình, hệ thống, vùng chức năng hay sản phẩm bàn giao thành phần đơn giản để phân tích độc lập, ước lượng, theo dõi. Giả định các thành phần con **mô tả đầy đủ** thành phần cha, và **mỗi thành phần con chỉ có một cha**.
- **Mục tiêu phân rã** quyết định cái gì, bao sâu: đo và quản lý, thiết kế, phân tích, ước lượng và dự báo, tái sử dụng, tối ưu, thay thế, đóng gói.
- **Đối tượng**: kết quả kinh doanh, công việc cần làm (WBS), quy trình, chức năng, đơn vị kinh doanh, thành phần giải pháp, hoạt động, sản phẩm và dịch vụ, quyết định.
- **Mức dừng**: khi đạt mục tiêu phân tích; không phân rã sâu hơn mục tiêu cần.
Giới hạn: thông tin thiếu thì phải phân rã lại; nhiều hệ thống không biểu diễn đủ bằng phân cấp đơn giản vì tương tác tạo hành vi nổi lên; một đối tượng có nhiều cách phân rã khác nhau.
Cách làm: hỏi mục tiêu phân rã trước; vẽ cây; kiểm mỗi nút một cha, các con phủ đủ cha và không chồng lấn. Với story: dùng cách phân rã của Agile Extension trong `story-writer` (theo giá trị khách hàng, không theo bước/tầng).

## Interface analysis (10.24, tr. 287–; phần đầu)
Xác định ai, thông tin gì (kèm khối lượng), khi nào và tần suất, ở đâu, vì sao, thực hiện thế nào cho mỗi giao diện. Loại: người dùng, người ngoài (cơ quan quản lý), quy trình, dữ liệu giữa hệ thống, API, thiết bị. Nhận diện sớm giúp biết cần mời stakeholder nào. Bảng đề xuất: Giao diện | Hai đầu | Thông tin trao đổi | Khối lượng | Tần suất/kích hoạt | Cách thực hiện | Chủ sở hữu | Câu hỏi mở. Sơ đồ tuần tự (10.42, chưa đọc kỹ) dùng để cho thấy thứ tự tương tác giữa các thành phần.

## Roles and Permissions Matrix (10.39, tr. 333–335)
Đảm bảo mọi hoạt động có người chịu trách nhiệm, tìm vai trò thiếu, truyền đạt thay đổi. Vai trò là nhãn cho nhóm người có chức năng chung; một hoạt động gắn một hoặc nhiều vai trò qua **authority**.
- Tìm vai trò: xem mô hình tổ chức, mô tả công việc, sổ tay quy trình, hướng dẫn hệ thống; gặp stakeholder. Lưu ý cùng chức danh có thể khác vai trò và ngược lại.
- Tìm hoạt động: dùng phân rã chức năng, mô hình quy trình, use case.
- Quyền: cân nhắc mức bảo mật và luồng công việc; xác nhận với stakeholder.
- Mức trừu tượng: cấp dự án dùng **RACI** (Responsible, Accountable, Consulted, Informed); hệ thống IT dùng **CRUD** (Create, Read, Update, Delete).
Quy tắc skill: ô chưa biết đánh "?", không điền; quyền xem dữ liệu nhạy cảm chuyển `nfr-writer` (phân quyền, ghi nhật ký).
**Kiểm tra**: mọi hoạt động có ít nhất một vai trò; mọi vai trò có ít nhất một hoạt động (không thì có thể thừa); vai trò khớp mô hình quy trình; hoạt động khớp use case/story.
