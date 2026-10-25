# Mẫu story

**[ID] Tên (động từ + mục tiêu)**
Là [vai trò cụ thể], tôi muốn [hành động/nhu cầu], để [lợi ích/giá trị].

**Phạm vi**: Trong: ... Ngoài: ...
**Điều kiện tiên quyết**: ...
**Quy tắc nghiệp vụ liên quan**: BR-xx
**Acceptance criteria**
1. ...
2. ...
**Giả định**: ...
**Cần làm rõ**: ...
**NFR phát hiện (chuyển nfr-writer)**: ...

---
## Ví dụ trước/sau (tự soạn để minh họa, không phải của dự án thật)

Trước: "Là người dùng, tôi muốn quản lý đơn hàng dễ dàng để tiết kiệm thời gian."
Vấn đề: vai trò chung chung; "quản lý" gồm nhiều việc; "dễ dàng", "tiết kiệm" không kiểm chứng được; thiếu AC.

Sau (một lát cắt):
**ORD-12 Hủy đơn chưa giao**
Là khách hàng đã đăng nhập, tôi muốn hủy đơn hàng chưa được giao đi, để không phải thanh toán cho hàng không còn cần.
Phạm vi: Trong: hủy toàn bộ đơn. Ngoài: hủy một phần đơn, hoàn tiền thủ công.
Quy tắc: BR-07 (đơn ở trạng thái "Chờ xử lý" hoặc "Đã xác nhận" mới được hủy).
AC:
1. Với đơn ở trạng thái hợp lệ theo BR-07, khi khách chọn "Hủy đơn" và xác nhận, đơn chuyển sang "Đã hủy" và khách thấy thông báo thành công.
2. Với đơn đã ở trạng thái "Đang giao" trở đi, nút "Hủy đơn" không hiển thị; nếu gọi trực tiếp, hệ thống từ chối và nêu lý do.
3. Khi đơn được hủy, hàng tồn kho tương ứng được trả lại.
4. Khi khách bấm "Hủy đơn" hai lần liên tiếp, chỉ một lần hủy được thực hiện.
Cần làm rõ: đơn đã thanh toán trước có hoàn tiền tự động không? Ai nhận thông báo hủy ngoài khách?
NFR phát hiện: thời gian hoàn tiền (chuyển nfr-writer); lưu nhật ký hủy đơn.
