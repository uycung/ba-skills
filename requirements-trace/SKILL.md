---
name: requirements-trace
description: "Lập ma trận truy vết và rà soát độ phủ giữa mục tiêu, FR, user story, acceptance criteria, NFR và test; dùng khi BA cần kiểm tra spec có lỗ hổng không, phân tích tác động khi yêu cầu đổi, hoặc chuẩn bị trước khi chốt/duyệt."
---

# Requirements Trace

Mục tiêu: nối các yêu cầu với nhau để thấy **cái gì chưa được phủ** và **đổi cái này thì ảnh hưởng cái nào**. Trả lời bằng ngôn ngữ người dùng (mặc định tiếng Việt). Phối hợp với skill `story-writer` (viết FR/story/AC) và `nfr-writer` (viết NFR).

## Nguyên tắc
1. **Chỉ nối khi mối nối có giá trị.** Công sức truy vết tăng mạnh theo số yêu cầu và mức độ hình thức (BABOK 5.1.4.1). Hỏi người dùng cần mức nào: nhẹ (mục tiêu ↔ story ↔ AC), vừa (thêm NFR, quy tắc nghiệp vụ), đầy đủ (thêm thiết kế và test).
2. **Không bịa liên kết.** Chỉ ghi liên kết có căn cứ trong tài liệu người dùng đưa; liên kết suy đoán đánh dấu "đề xuất, cần xác nhận".
3. **Mỗi mục có mã ổn định**, không đổi khi sửa nội dung. Quy ước mặc định: `GOAL-xx`, `FR-xx`, `US-xx` (hoặc mã theo epic như `ORD-12`), `AC-xx.y`, `BR-xx` (quy tắc nghiệp vụ), `NFR-<đặc tính>-xx`, `TC-xx`. Nếu đội đã có quy ước, dùng quy ước đó.
4. Mối quan hệ dùng đúng loại (xem `references/relationships.md`).

## Quy trình
1. Thu tài liệu đầu vào (PRD, danh sách story, bảng NFR...). Nếu thiếu mã, gán mã đề xuất và nói rõ.
2. Chọn mức truy vết với người dùng (nhẹ/vừa/đầy đủ).
3. Lập danh mục các mục và liên kết theo `templates/trace-matrix.md`.
4. Chạy các kiểm tra độ phủ (`references/coverage-checks.md`), liệt kê khoảng trống theo mức nghiêm trọng.
5. Nếu người dùng nêu một thay đổi, làm phân tích tác động: mục nào bị ảnh hưởng trực tiếp/gián tiếp, cần sửa gì, cần ai duyệt lại.
6. Kết thúc bằng: **Khoảng trống**, **Mâu thuẫn**, **Cần xác nhận**, và bước kế tiếp đề xuất.

## Giới hạn cần nói thẳng
Truy vết chứng minh mỗi yêu cầu nối về mục tiêu, **không** chứng minh tập yêu cầu mạch lạc (BABOK 7.4.2). Nếu người dùng cần kiểm tra điều đó, dùng viewpoint/view và 5 tiêu chí liên kết.

## Thuộc tính nên có cho từng yêu cầu
Nguồn (ai/tài liệu nào yêu cầu), độ ưu tiên, độ phức tạp, trạng thái (kể cả đã duyệt: ai, khi nào), phiên bản. Thuộc tính có thể đổi dù yêu cầu không đổi (BABOK 5.2.4.2).
ISO/IEC/IEEE 29148:2018, 5.2.8 (bản chuẩn đã đọc) nêu các thuộc tính ví dụ: định danh duy nhất (không đổi và không tái sử dụng kể cả khi yêu cầu bị xóa), phiên bản, chủ sở hữu, ưu tiên của stakeholder (thang 1 đến 5 hoặc Cao/Trung bình/Thấp), rủi ro, lý do (rationale), độ khó, loại. Chuẩn không liệt kê trạng thái, nguồn hay liên kết truy vết trong danh sách ví dụ đó. Điều 6.5.2.2 khuyến nghị gắn **phương pháp xác minh** ngay khi tạo yêu cầu, với bốn giá trị: inspection, analysis, demonstration, test; chi tiết ở `requirements-review/references/iso29148.md`. Quy tắc "định danh không đổi, không tái sử dụng" nên dùng cho ID trong ma trận.

## Tệp tham chiếu
- `references/relationships.md`: các loại quan hệ và cách ghi.
- `references/coverage-checks.md`: kiểm tra độ phủ, phân tích tác động.
- `references/architecture-approval-review.md`: kiến trúc yêu cầu, chất lượng liên kết, đánh giá thay đổi, phê duyệt, rà soát (BABOK 7.4, 5.4, 5.5, 10.37).
- `templates/trace-matrix.md`: mẫu ma trận và báo cáo khoảng trống.
