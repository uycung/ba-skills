# Quy tắc nghiệp vụ (BABOK 10.9, tr. 240–243; diễn đạt lại)

Dùng khi một story/FR có số, ngưỡng, điều kiện, ngoại lệ. Tách chúng ra bảng BR-xx; story chỉ dẫn chiếu.

## Nguyên tắc viết
- Rõ ràng, cụ thể, dễ tiếp cận, **một nguồn duy nhất**; dùng thuật ngữ nghiệp vụ chuẩn để chuyên gia lĩnh vực kiểm tra được.
- Viết **nguyên tử và khai báo** (nói cái gì đúng, không nói làm thế nào); **tách khỏi quy trình** mà chúng hỗ trợ/ràng buộc; **tách khỏi cách thực thi**; ánh xạ tới quyết định mà chúng chi phối.
- **Ngoại lệ cũng là quy tắc**, ghi thành quy tắc riêng.
- Quy tắc độc lập với công nghệ; có thể được cài ở nhiều nền tảng.
- Quy tắc cũ cần được chất vấn: còn phục vụ mục tiêu không.
- Quy tắc phải "practicable": người nghiệp vụ dùng được mà không cần diễn giải thêm, và nằm trong quyền kiểm soát của doanh nghiệp.

## Hai loại
| Loại | Bản chất | Vi phạm được không | Ví dụ (BABOK) |
|---|---|---|---|
| Definitional (định nghĩa/tính toán) | Nói điều gì tất yếu đúng về một khái niệm, hoặc cách suy ra/tính | Không vi phạm được, nhưng áp dụng sai được | Khách đặt hơn 10 đơn/tháng được coi là Preferred Customer; công thức thuế |
| Behavioural (hành vi) | Nghĩa vụ/cấm đoán với hành động của người (kể cả khi tự động hóa) | Luôn vi phạm được | Không cho đặt đơn khi địa chỉ thanh toán khác địa chỉ ở tổ chức thẻ |

## Mức thực thi cho quy tắc hành vi (phải hỏi, không tự chọn)
Không cho vi phạm; người có thẩm quyền được ghi đè; ghi đè kèm giải trình; không thực thi chủ động (khi đó chỉ là hướng dẫn). Hỏi thêm: chế tài khi vi phạm, phản ứng bổ sung.

## Cột cho bảng BR
Mã | Phát biểu | Loại (định nghĩa/hành vi) | Mức thực thi | Nguồn (chính sách, luật, người) | Chủ sở hữu | Story dẫn chiếu
Giới hạn BABOK nêu: danh sách dài dễ mơ hồ, các quy tắc có thể mâu thuẫn khi gộp nên phải kiểm chéo, từ vựng nghèo làm quy tắc sai. Tổ hợp điều kiện nhiều thì dùng bảng quyết định (BABOK dẫn sang Decision Analysis).
