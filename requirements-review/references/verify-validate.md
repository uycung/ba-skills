# Verify và Validate (BABOK 7.2, 7.3, 5.5; diễn đạt lại)

## Hoạt động verify (7.2.4.2, tr. 143–144)
- Kiểm tuân thủ chuẩn BA của tổ chức (đúng công cụ, đúng phương pháp).
- Kiểm dùng đúng ký hiệu mô hình, mẫu, biểu mẫu.
- Kiểm **đầy đủ trong từng mô hình**.
- **So sánh từng mô hình với mô hình liên quan**: phần tử nhắc ở mô hình này mà thiếu ở mô hình kia; phần tử được tham chiếu nhất quán.
- Kiểm thuật ngữ dễ hiểu với stakeholder và nhất quán với cách tổ chức dùng.
- Thêm ví dụ khi cần làm rõ.
- Checklist: bộ tiêu chí chuẩn hoặc theo mối lo cụ thể; mục đích là bảo đảm điều quan trọng có trong sản phẩm cuối và quy trình verify được tuân thủ (7.2.4.3).
- Kỹ thuật BABOK gợi ý: Acceptance and Evaluation Criteria (viết đủ rõ để dựng test), Item Tracking (quản lý vấn đề tìm thấy), Metrics/KPIs (đo chất lượng yêu cầu), Reviews.
- Kết quả: yêu cầu **đã verify** = đủ chất lượng làm cơ sở cho công việc tiếp.

## Validate (7.3.4, tr. 146)
1. **Nhận diện giả định.** Sản phẩm chưa từng có thì phải giả định về phản ứng của khách; stakeholder có thể giả định lợi ích sẽ xảy ra; không chứng minh được nguyên nhân gốc. Giả định phải được ghi để quản lý rủi ro.
2. **Định nghĩa tiêu chí đánh giá đo được**: lợi ích kỳ vọng đã có trong trạng thái tương lai nhưng cách đo có thể chưa có; xác định baseline từ hiện trạng và mục tiêu số tương ứng với business objectives.
3. **Đánh giá mức phù hợp với phạm vi giải pháp**: một yêu cầu có lợi cho stakeholder vẫn có thể không nên nằm trong giải pháp. Không đem lại lợi ích thì là ứng viên bị loại. Nếu không khớp thì hoặc xem lại trạng thái tương lai và đổi phạm vi, hoặc bỏ yêu cầu. Thiết kế không validate được là dấu hiệu thiếu/hiểu sai yêu cầu hoặc phải đổi thiết kế.
Đầu vào cần có: business objectives, future state description, potential value, solution scope. Thiếu thì ghi "validate một phần".
Kỹ thuật BABOK gợi ý: Acceptance and Evaluation Criteria, Document Analysis, Financial Analysis, Item Tracking, Metrics/KPIs, Reviews (xác nhận stakeholder thấy nhu cầu được đáp ứng), Risk Analysis.
Kết quả: yêu cầu đã validate chứng minh được lợi ích cho stakeholder và khớp mục tiêu thay đổi; không validate được nghĩa là không có lợi cho tổ chức, hoặc ngoài phạm vi, hoặc cả hai.

## Cổng sẵn sàng trước khi xin duyệt (5.5; diễn đạt lại, điều kiện cụ thể là của skill)
BABOK 5.5.3: đầu vào của duyệt là yêu cầu **đã verify**. Cổng đề xuất:
- Không còn phát hiện mức Chặn.
- Mâu thuẫn đã được giải quyết hoặc có người quyết và hạn.
- Biết ai có quyền duyệt và ai chỉ có ảnh hưởng (5.5.4.1).
- Rủi ro do thiếu đồng thuận đã ghi (5.5.4.3: không cần đồng thuận tuyệt đối, nhưng thiếu thì phải quản lý rủi ro).
- Hình thức duyệt khớp cách làm: predictive thường duyệt cuối giai đoạn hoặc họp kiểm soát thay đổi; adaptive duyệt khi sắp bắt đầu xây dựng (5.5.2).
Kết quả duyệt (ai, khi nào, phiên bản nào) ghi vào trace; xem `requirements-trace`.
