# Các loại quan hệ truy vết

Theo BABOK v3 mục 5.1.4.2 (tr. 81–82), diễn đạt lại; đã đọc từ bản người dùng cung cấp.
| Quan hệ | Ý nghĩa | Ví dụ |
|---|---|---|
| Derive (dẫn xuất) | Yêu cầu này sinh ra từ yêu cầu kia, thường khác mức trừu tượng | FR-05 dẫn xuất từ GOAL-02 |
| Depends (phụ thuộc) | Yêu cầu này cần yêu cầu kia. Hai loại: necessity (chỉ có nghĩa nếu cái kia cũng làm) và effort (làm dễ hơn nếu cái kia cũng làm) | US-14 phụ thuộc US-09 (necessity) |
| Satisfy (đáp ứng) | Thành phần triển khai đáp ứng yêu cầu | Module/API đáp ứng FR-05 |
| Validate (kiểm chứng) | Test case hoặc phần tử khác xác định giải pháp có thỏa yêu cầu | TC-31 kiểm chứng AC-12.2 |

Chuỗi điển hình: GOAL → (derive) FR/US → (derive) AC; NFR → (derive) từ GOAL hoặc từ luật/chuẩn; BR → (support) FR/US; TC → (validate) AC/NFR; thành phần → (satisfy) FR/US/NFR.
Quan hệ "support" giữa quy tắc nghiệp vụ và yêu cầu là mở rộng theo BABOK 5.1.6 (kỹ thuật Business Rules Analysis dùng để truy vết quy tắc tới yêu cầu), không phải loại quan hệ chính thức trong danh sách trên.
