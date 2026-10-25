# Kiểm chất lượng test và độ phủ

Danh sách này là của skill (tham chiếu BABOK 10.1 cho yêu cầu kiểm chứng đúng/sai và 5.1 cho truy vết Validate; phần độ phủ theo kỹ thuật dựa trên ISTQB CTFL v4.0.1).

## Kiểm từng test
- Có ID, nguồn (ít nhất một ID yêu cầu), mục tiêu một câu.
- Một ý chính; không lẫn hai kết quả độc lập (tách ra).
- Tiền điều kiện đủ để người khác chạy lại; dữ liệu cụ thể (không "dữ liệu hợp lệ" chung chung).
- Bước lặp lại được; kết quả mong đợi **quan sát được** và đo được (không "hệ thống xử lý đúng").
- Kết quả mong đợi khớp từng chữ với yêu cầu nguồn; nếu test thêm điều yêu cầu không nói, đó là dấu hiệu yêu cầu thiếu: ghi thành câu hỏi.
- Loại test hợp lý (chuẩn, ngoại lệ, biên, sai dữ liệu, quyền, trạng thái, NFR).
- Không phụ thuộc kết quả của test khác trừ khi ghi rõ thứ tự.

## Kiểm độ phủ
1. Mỗi yêu cầu chốt (AC, BR, NFR đo được, chuyển trạng thái, dòng bảng quyết định) có ≥ 1 test.
2. Mỗi BR có ngưỡng có test ở cả hai phía.
3. Mỗi luồng ngoại lệ của use case có test.
4. Mỗi chuyển trạng thái hợp lệ có test; mọi trạng thái có hành động bị cấm đều có test âm (nếu yêu cầu nêu).
5. Mỗi vai trò có ít nhất một test dương và một test âm về quyền (nếu ma trận quyền có).
6. Không test mồ côi (không trỏ nguồn).
7. NFR đo được có phương pháp đo; NFR không đo được đã bị trả lại.
8. Mỗi story có test chứng minh giá trị đầu-cuối, không chỉ test từng AC rời.

## Độ phủ theo kỹ thuật (đơn vị ISTQB CTFL v4.0.1, mục 4.2)
Khi báo độ phủ của một kỹ thuật, nêu coverage item và công thức, không nói "phủ 100%" chung chung:
| Kỹ thuật | Coverage item | Độ phủ = |
|---|---|---|
| Phân vùng tương đương | phân vùng (kể cả không hợp lệ) | số phân vùng đã chạy / tổng phân vùng |
| BVA 2 giá trị | giá trị biên | số biên đã chạy / tổng biên |
| BVA 3 giá trị | giá trị biên và láng giềng | số item đã chạy / tổng item |
| Bảng quyết định | cột khả thi | số cột đã chạy / tổng cột khả thi |
| Chuyển trạng thái | trạng thái; chuyển hợp lệ; mọi chuyển (gồm không hợp lệ) | theo tiêu chí đã chọn |
Với bộ test xuất phát từ story, kiểm thêm theo ATDD (4.5.3): test phủ mọi đặc điểm của story, không vượt ngoài story, và không có hai test cùng mô tả một đặc điểm.

## Báo cáo độ phủ
Bảng: nguồn | số test | loại thiếu | ghi chú. Kết thúc bằng:
- số yêu cầu có test / tổng yêu cầu đã chốt;
- yêu cầu chưa có test và lý do (AC mơ hồ, thiếu giá trị, chờ quyết định);
- phần phải do QA bổ sung.
Không quy ra tỉ lệ phần trăm "đủ" cho cả bộ; độ phủ theo yêu cầu không đảm bảo bắt hết lỗi.

## Dấu hiệu cần trả lại cho viết yêu cầu
- AC không có giá trị cụ thể.
- Hai AC cho kết quả khác nhau với cùng điều kiện.
- Bảng quyết định thiếu tổ hợp hoặc chồng lấn.
- Trạng thái trong test không có trong mô hình trạng thái.
- Thuật ngữ trong test khác glossary.
