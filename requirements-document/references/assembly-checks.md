# Kiểm khi lắp ráp

Danh sách là của skill, dựa trên: chất lượng yêu cầu (7.2.4), tiêu chí chất lượng liên kết (7.4: được định nghĩa, cần thiết, đúng, rõ ràng, nhất quán), và phê duyệt (5.5).

## Nhất quán
1. **ID**: không trùng, không nhảy sai, mọi tham chiếu `AC-xx`, `BR-xx`, `NFR-xx` đều tồn tại trong tài liệu.
2. **Thuật ngữ**: một khái niệm một tên; glossary khớp mọi nơi.
3. **Phạm vi**: mục tiêu, phạm vi trong/ngoài, yêu cầu không mâu thuẫn; không yêu cầu nào nằm ngoài phạm vi đã nói.
4. **Số liệu và ngưỡng**: cùng một số ở mọi chỗ (ví dụ thời hạn hủy, thời gian phản hồi).
5. **Ưu tiên**: cùng thang với `requirements-prioritize`; không mâu thuẫn với phát hành.
6. **Vai trò**: tên vai trò khớp danh sách stakeholder và ma trận quyền.
7. **Trạng thái**: tên trạng thái trong story khớp mô hình trạng thái.
8. **Quy tắc**: mỗi quy tắc xuất hiện một lần ở bảng BR; story/use case dẫn chiếu.
9. **Dữ liệu**: thuộc tính trong story khớp từ điển dữ liệu.

## Đầy đủ theo loại
- **BRD**: có nhu cầu, mục tiêu đo được (SMART), phạm vi, stakeholder, tiêu chí thành công, ràng buộc, rủi ro, yêu cầu transition mức cao.
- **PRD**: vấn đề, người dùng (dựa nghiên cứu hay ghi giả thuyết), mục tiêu và chỉ số, phạm vi, yêu cầu có AC, NFR chính, phát hành, rủi ro, câu hỏi mở.
- **SRS**: mọi FR có AC kiểm chứng; mọi NFR đo được; giao diện; dữ liệu; quy tắc; transition.
Mọi loại: giả định, ràng buộc, phụ thuộc, câu hỏi mở; phần phê duyệt; lịch sử thay đổi.

## Truy vết
- Mỗi yêu cầu solution truy về ít nhất một yêu cầu business hoặc mục tiêu; mỗi mục tiêu có yêu cầu trỏ vào.
- Không yêu cầu mồ côi, không mục tiêu không được phủ (xem `requirements-trace`).
- Mỗi AC/NFR có test hoặc ghi "chưa có test" (`requirements-testcases`).

## Trạng thái, phiên bản, đường cơ sở
- Mỗi mục có trạng thái: Nháp / Đã rà soát / Đã duyệt / Chờ làm rõ.
- Số phiên bản và ngày; lịch sử thay đổi: ai, gì, vì sao.
- **Đường cơ sở** (baseline): thời điểm chốt một tập yêu cầu để làm việc tiếp; thay đổi sau đó qua đánh giá tác động (5.4: lợi ích, chi phí, tác động, lịch, mức khẩn). Từ điển BABOK nói gói yêu cầu có thể là đường cơ sở của một tập yêu cầu.
- Không tự gắn trạng thái "Đã duyệt" khi chưa có xác nhận của người duyệt.

## Phê duyệt (5.5)
Đầu vào là yêu cầu đã verify. Cách duyệt khác nhau: predictive duyệt cuối giai đoạn hoặc ở họp kiểm soát thay đổi; adaptive duyệt khi sắp bắt đầu xây. Không cần đồng ý hoàn toàn; không đồng thuận thì phải quản lý rủi ro. Phần phê duyệt của tài liệu ghi: ai (vai trò, người Accountable theo RACI), phạm vi duyệt, ngày, điều kiện kèm theo, ý kiến phản đối. Không điền thay.

## Dấu hiệu tài liệu "dày mà rỗng"
- Mục nào cũng có chữ nhưng không có nguồn.
- Câu chung chung về chất lượng ("hệ thống phải ổn định") không số đo.
- Lặp lại cùng ý ở nhiều mục.
- Phần giả định rỗng.
