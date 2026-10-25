# Mô hình quy trình và mô hình trạng thái

## Quy trình (BABOK 10.35, tr. 318–322; diễn đạt lại)
**Mục đích**: cho thấy công việc được thực hiện thế nào, là nền tảng của phân tích quy trình. Có thể mô tả hiện trạng (as-is: để thống nhất cái đang xảy ra) hoặc tương lai (to-be: để thống nhất cái muốn xảy ra).
**Tối thiểu**: sự kiện kích hoạt, chuỗi hoạt động, kết quả. Thêm: người tham gia (vai trò), hoạt động thủ công và tự động, đường đi và điểm quyết định, dữ liệu vào/ra, chú thích.
**Phần tử**: Activity (có thể là sub-process), Event (kích hoạt, ngắt hoặc kết thúc; có thể là thông điệp, thời gian, điều kiện), Directional flow, Decision point (rẽ nhánh loại trừ hoặc song song, hoặc nơi các luồng gộp), Link (nối sang quy trình khác), Role (khớp mô hình tổ chức).
**Mức**: ngữ cảnh/doanh nghiệp (tổng quan, quan hệ với quy trình khác), vận hành (chi tiết hoạt động, **mọi kết quả kể cả ngoại lệ và đường thay thế**), hệ thống (nền tảng mô phỏng/thực thi).
**Ký hiệu thường dùng**: flowchart (hợp người không kỹ thuật; thêm swimlane để tách việc theo vai trò, vốn là mở rộng không chính thức), BPMN (chuẩn ngành, pool và swimlane, chuyển trách nhiệm khi luồng qua ranh giới làn), DFD và UML (miền IT), IDEF/IGOE (xác lập phạm vi), SIPOC và value stream.

**Cách làm với skill**
1. Hỏi sự kiện kích hoạt và kết quả trước, rồi các hoạt động theo thứ tự, rồi ngoại lệ.
2. Gán mỗi hoạt động cho đúng một vai trò (làn). Hoạt động chưa rõ ai làm: dấu "?".
3. Mỗi điểm rẽ nhánh có đủ lối ra; điều kiện rẽ dẫn chiếu BR hoặc bảng quyết định.
4. as-is: gắn nhãn nguồn [Đã nói]/[Suy luận]; to-be: ghi rõ phần mới và phần giữ.
**Kiểm tra**: có trigger và kết quả; không hoạt động mồ côi (không vào hoặc không ra); mọi nhánh có lối ra; không vòng lặp vô hạn không điều kiện thoát; vai trò khớp danh sách vai trò; thuật ngữ khớp glossary; ngoại lệ phổ biến (hủy giữa chừng, thiếu dữ liệu, hết chỗ, quá hạn) đã được hỏi.
Giới hạn BABOK: hữu ích để phân tích nhưng cần giữ cập nhật và không thay thế phân tích quy tắc.

## Trạng thái (BABOK 10.44, tr. 348–350; diễn đạt lại)
**Mục đích**: mô tả các trạng thái có thể của một thực thể, cách nó chuyển, và điều gì có thể xảy ra với nó ở mỗi trạng thái. Dùng khi thực thể có hành vi và quy tắc phức tạp và cần hiểu chính xác nhất quán. Bổ sung cho quy trình: quy trình cho thấy mọi thực thể trong một quy trình; mô hình trạng thái cho thấy một thực thể qua mọi quy trình tác động lên nó.
**Phần tử**: State (tên, hoạt động được làm ở đó, quy tắc, sự kiện phản hồi; có thể chia trạng thái con); Transition (sự kiện gây chuyển, điều kiện quyết định có phản hồi hay không, hành động đi kèm; có thể có điều kiện hoặc tự động; có thể bỏ qua trạng thái, quay lại trạng thái trước, hoặc quay về chính nó); trạng thái đầu và cuối; sơ đồ trạng thái; **bảng trạng thái** (mỗi dòng: trạng thái đầu, chuyển, trạng thái cuối; mỗi chuyển một dòng).
**Cách làm với skill**
1. Bắt đầu bằng **bảng trạng thái** để khai thác tên trạng thái và sự kiện với chuyên gia (BABOK nói đây là cách dễ bắt đầu), rồi mới vẽ sơ đồ.
2. Hỏi: thực thể bắt đầu thế nào, kết thúc thế nào; từ mỗi trạng thái những sự kiện nào xảy ra; ai làm; điều kiện nào.
3. Hỏi riêng về ngoại lệ: hủy, hoàn tác, hết hạn, trùng, ghi đè.
**Kiểm tra**: có trạng thái đầu và cuối; mọi trạng thái đều đến được và (trừ trạng thái cuối) đều đi tiếp được; mỗi chuyển có sự kiện; không hai chuyển cùng sự kiện, cùng điều kiện, khác đích; tên trạng thái khớp AC và dữ liệu; mỗi trạng thái nêu rõ hành động cho phép.
Từ mô hình sinh ra: AC cho từng chuyển trạng thái, BR cho điều kiện chuyển, và test dò mọi chuyển.
Giới hạn BABOK: chỉ đáng làm với thực thể phức tạp; khó đạt đồng thuận chi tiết với chuyên gia; một số người ngại mức chi tiết chính xác.
