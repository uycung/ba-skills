# Kiến trúc yêu cầu, phê duyệt, rà soát (BABOK 7.4 tr. 148–151; 5.5 tr. 95–97; 5.4 tr. 93–94; 10.37 tr. 326–329; diễn đạt lại)

## 1. Truy vết không chứng minh được sự mạch lạc (7.4.2)
Truy vết cho thấy mỗi yêu cầu nối về một mục tiêu; **không chứng minh** tập yêu cầu hợp thành một giải pháp chạy được. Kiến trúc yêu cầu là cấu trúc của toàn bộ yêu cầu để chúng hỗ trợ nhau. Báo cáo của skill này vì vậy phải nói rõ: "độ phủ truy vết đủ" ≠ "tập yêu cầu đã mạch lạc".
- Mỗi yêu cầu **nêu đúng một lần** trong kiến trúc (7.4.3). Trùng lặp là lỗi cần gộp.
- **Viewpoint** (quy ước biểu diễn cho một nhóm stakeholder) và **view** (yêu cầu thực tế theo viewpoint đó). Ví dụ viewpoint: quy trình, dữ liệu, tương tác người dùng, kiểm toán/bảo mật, mô hình kinh doanh. Không viewpoint đơn lẻ nào đủ; nhét quá nhiều vào một viewpoint làm nó rối.
- Tính đầy đủ: không thiếu, không mâu thuẫn, tính cả phụ thuộc có thể cản đạt mục tiêu. Lặp lại khai thác/phân tích giúp lộ khoảng trống.
- **Kiến trúc thông tin BA** (kiểu thông tin nào nối với kiểu nào: yêu cầu, thiết kế, mô hình, kết quả khai thác) nên định nghĩa **trước** khi dựng công cụ/kho lưu trữ.

## 2. Tiêu chí chất lượng cho từng liên kết (7.4.4.4)
| Tiêu chí | Hỏi |
|---|---|
| Defined | Có liên kết, và loại liên kết được ghi? |
| Necessary | Liên kết cần để hiểu tổng thể? (không nối chỉ để cho đủ) |
| Correct | Hai mục thật sự có quan hệ như đã ghi? |
| Unambiguous | Không có hai liên kết mâu thuẫn cho cùng cặp mục? |
| Consistent | Dùng cùng một bộ mô tả chuẩn của viewpoint? |
Dùng làm kiểm tra bổ sung 13 trong `coverage-checks.md`.

## 3. Đánh giá thay đổi yêu cầu (5.4.4)
Khi phân tích tác động, nêu rõ năm yếu tố BABOK: **benefit** (lợi ích), **cost** (gồm làm lại và chi phí cơ hội: tính năng phải hy sinh), **impact** (số khách hàng/quy trình bị ảnh hưởng), **schedule** (cam kết giao hàng hiện có), **urgency** (gồm lý do quy định, an toàn). Kết quả là một trong: duyệt, từ chối, hoãn, do người có thẩm quyền theo quy trình quản trị; ghi lại và thông báo cho mọi stakeholder. Cần luôn xét thông tin pháp lý/quy định và phạm vi giải pháp. Skill chỉ **chuẩn bị dữ kiện**, không quyết định.

## 4. Phê duyệt (5.5.4)
- Phê duyệt chỉ áp dụng cho yêu cầu **đã được xác minh chất lượng** (đầu vào của 5.5). Không đưa bản nháp đi ký.
- Hình thức phụ thuộc cách làm: predictive thường duyệt cuối giai đoạn hoặc họp kiểm soát thay đổi; adaptive thường duyệt khi sắp bắt đầu xây dựng.
- Biết ai có quyền duyệt/phủ quyết và ai chỉ có ảnh hưởng. Tìm đồng thuận trước khi xin duyệt; không cần đồng thuận tuyệt đối, nhưng thiếu đồng thuận thì **ghi rủi ro**.
- Ghi quyết định duyệt (ai, khi nào, phiên bản nào), thông báo trạng thái. Cột đề xuất cho ma trận: Trạng thái duyệt | Người duyệt | Ngày | Phiên bản.
- Yêu cầu đã duyệt là sản phẩm đã chốt; đổi sau đó phải qua đánh giá thay đổi.

## 5. Rà soát (10.37)
Rà soát nhắm **sản phẩm công việc**, không đánh giá con người. Xác định trước: mục tiêu (bắt lỗi, kiểm tra tuân thủ chuẩn, xác nhận đủ và đúng, đồng thuận, giải quyết vấn đề, giáo dục, đo chất lượng), kỹ thuật, người tham gia.
| Kỹ thuật | Hình thức | Khi dùng |
|---|---|---|
| Inspection | Chính thức: tổng quan, xem riêng, ghi lỗi, hợp nhất, theo dõi sửa | Sản phẩm trọng yếu, mục tiêu bắt lỗi |
| Formal walkthrough | Chính thức: xem riêng + hợp nhất nhóm | Đồng nghiệp hoặc stakeholder |
| Single issue review | Chính thức: một vấn đề hoặc một chuẩn | Giải quyết điểm cụ thể |
| Informal walkthrough | BA trình bản nháp, xin góp ý | Bản đang làm |
| Desk check | Một người ngoài đọc và phản hồi | Nhanh, ít công |
| Pass around | Nhiều người xem lần lượt hoặc trên bản chung | Nhiều người, khác giờ |
| Ad hoc | Nhờ đồng nghiệp xem giúp | Rất nhẹ |
Vai trò: Author (trả lời, sửa), Reviewer, Facilitator (trung lập, không nên là tác giả), Scribe (ghi lỗi, ý kiến, câu hỏi tồn đọng). Nếu cấp trên tham gia, người điều phối chú ý để không làm người khác ngại nói thật.
Giới hạn: rà soát chặt tốn công nên chỉ dành cho sản phẩm trọng yếu; rà soát nhẹ ít đảm bảo hơn; góp ý qua email khó xử lý mâu thuẫn.
