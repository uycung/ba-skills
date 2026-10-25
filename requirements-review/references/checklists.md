# Checklist theo loại tài liệu (của skill, dựa trên các đặc tính và hoạt động BABOK; không phải danh sách của BABOK)

Dùng như điểm khởi đầu; nếu đội có checklist riêng thì dùng của đội.

## Story / AC (đối chiếu story-writer)
- Có vai trò cụ thể, mục tiêu, giá trị (WHY không bị bỏ).
- Một giá trị, một lát cắt giao được; không tách theo tầng kỹ thuật.
- Mỗi AC kiểm chứng được đúng/sai; có đầu vào, hành động, kết quả quan sát; có ca lỗi, rỗng, trùng, quyền, hủy giữa chừng.
- Quy tắc nghiệp vụ nằm ở bảng BR, story dẫn chiếu.
- Từ mơ hồ không kèm tiêu chí: có hay không.
- NFR không nhét trong AC chức năng.
- Có mục "ngoài phạm vi" khi cần.

## Use case / FR
- Tên có động từ và danh từ; có mục tiêu của tác nhân chính.
- Tác nhân chính và phụ rõ; tiền điều kiện, trigger, luồng chính, luồng thay thế và ngoại lệ, hậu điều kiện (đảm bảo thành công và tối thiểu).
- Viết từ góc nhìn tác nhân, không mô tả cách hệ thống làm bên trong.

## NFR
- Mỗi NFR có thước đo, ngưỡng, điều kiện đo, cách kiểm chứng, nhãn bằng chứng (a/b/c).
- Số nào không có nguồn thì đánh dấu cần chốt.
- Mục pháp lý có nguồn và dòng cần pháp chế xác nhận.
- Yêu cầu chuyển đổi tách riêng, không lẫn NFR.
- Có NFR xung đột cần chốt trade-off không.

## Quy tắc nghiệp vụ
- Nguyên tử, khai báo, một nguồn.
- Phân loại định nghĩa hay hành vi; hành vi có mức thực thi.
- Ngoại lệ được ghi thành quy tắc riêng.
- Không mâu thuẫn với quy tắc khác; thuật ngữ có trong glossary.

## Mô hình (quy trình, trạng thái, dữ liệu, quyết định)
- Dùng đúng ký hiệu đã chọn.
- Đầy đủ trong mô hình: quy trình có sự kiện kích hoạt, hoạt động, kết quả; mọi nhánh quyết định có lối ra; trạng thái có trạng thái đầu và cuối, mọi chuyển trạng thái có sự kiện; thực thể có định danh, quan hệ có bội số; bảng quyết định phủ hết tổ hợp và không chồng lấn.
- Kiểm chéo: thực thể trong mô hình dữ liệu có xuất hiện trong quy trình/story; trạng thái xuất hiện trong AC; vai trò trong ma trận quyền khớp vai trò trong quy trình.

## Cả tài liệu (PRD/BRD/SRS)
- Mục tiêu, phạm vi, trạng thái tương lai có mặt để validate.
- Mỗi yêu cầu nêu một lần (BABOK 7.4); mã ổn định.
- Glossary; nguồn từng yêu cầu; mức ưu tiên; các câu hỏi mở được liệt kê.
- Liên kết truy vết đạt: defined, necessary, correct, unambiguous, consistent (7.4.4.4).
