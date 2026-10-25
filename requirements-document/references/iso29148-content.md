# ISO/IEC/IEEE 29148:2018, điều 9: nội dung BRS và SRS, đối chiếu với khung của skill

Nguồn: bản chuẩn ISO/IEC/IEEE 29148:2018(E) do người dùng cung cấp, đã đọc điều 9.2, 9.3, 9.6 và mục lục 9.4, 9.5. Tên mục dưới đây là diễn đạt lại bằng tiếng Việt.

## Điều cần nhớ trước
1. **Chuẩn quy định nội dung, không quy định cấu trúc mục.** Thứ tự và cách chia mục do chính sách quản lý thông tin của dự án chọn (9.3.1, 9.4.1, 9.6.1). Vì vậy khung `templates/` của skill không "sai chuẩn" khi khác thứ tự; điều cần kiểm là **mỗi nội dung chuẩn đòi hỏi có chỗ để ở đâu đó**.
2. Chuẩn dùng tên BRS, StRS, SyRS, SRS. "BRD" và "PRD" là tên ngành, không phải tên trong chuẩn; BRD gần BRS/StRS, PRD không có tương ứng trực tiếp.
3. Khung của skill vẫn do skill thiết kế dựa trên BABOK. Bảng dưới chỉ cho biết mục nào của chuẩn đã có chỗ, mục nào chưa.
4. Nếu hợp đồng hoặc tổ chức yêu cầu tuân thủ 29148, đây là danh sách kiểm nội dung, không phải bằng chứng tuân thủ. Cần người có trách nhiệm tuân thủ xác nhận.

## Nội dung chung (9.2), áp dụng cho tài liệu dạng văn bản
Nhận dạng (tiêu đề, thông báo sửa đổi: phiên bản, ngày, người duyệt, danh sách thay đổi); phần đầu (mục lục, danh mục hình, danh mục bảng); định nghĩa; tham chiếu (đủ tên, số hiệu, ngày, tổ chức ban hành, nơi lấy; nên tách tài liệu có yêu cầu bắt buộc và tài liệu chỉ để tham khảo); từ viết tắt. Mẫu của skill đã có phiên bản, thuật ngữ, lịch sử thay đổi; chưa nhắc danh mục hình/bảng và tách tham chiếu "bắt buộc" khỏi "tham khảo".

## BRS, điều 9.3 (18 nội dung) → BRD của skill
| Chuẩn | Nội dung | Chỗ trong BRD của skill |
|---|---|---|
| 9.3.2 | Mục đích kinh doanh: lý do và bối cảnh, hệ thống đóng góp thế nào cho mục tiêu | §2 Bối cảnh và nhu cầu |
| 9.3.3 | Phạm vi kinh doanh: miền nghiệp vụ, hoạt động trong phạm vi, thực thể bên ngoài, phạm vi hệ thống và giả định | §4 Phạm vi |
| 9.3.4 | Tổng quan kinh doanh: các bộ phận nội bộ và thực thể ngoài, quan hệ (nên có sơ đồ) | Chưa có chỗ riêng; đặt trong §4 kèm sơ đồ ngữ cảnh |
| 9.3.5 | Stakeholder chính và ảnh hưởng | §5 |
| 9.3.6 | Môi trường kinh doanh: xu hướng thị trường, luật và quy định, trách nhiệm xã hội, nền tảng công nghệ | Một phần trong §2; **chưa tách** |
| 9.3.7 | Sứ mệnh, mục tiêu | §3 |
| 9.3.8 | Mô hình kinh doanh: sản phẩm/dịch vụ, địa bàn, kênh, đối tác, tài chính và doanh thu | **Chưa có** |
| 9.3.9 | Môi trường thông tin: danh mục dự án, kế hoạch hệ thống dài hạn, cấu hình cơ sở dữ liệu cấp tổ chức | **Chưa có** |
| 9.3.10 | Quy trình kinh doanh (đánh số, sơ đồ chuỗi hoạt động) | Chưa có chỗ trong BRD; mô hình quy trình nằm ở SRS §3 / `requirements-modelling` |
| 9.3.11 | Chính sách và quy tắc kinh doanh (đặt tên, đánh số, được tham chiếu từ quy trình) | SRS §5; BRD chưa có |
| 9.3.12 | Ràng buộc vận hành kinh doanh (ví dụ hoàn tất trong một ngày) | §10 (chưa tách khỏi ràng buộc dự án) |
| 9.3.13 | Chế độ vận hành: quá tải, thủ công khi hệ thống không có | **Chưa có** |
| 9.3.14 | Chất lượng vận hành kinh doanh | Có thể đặt vào §6 hoặc NFR cấp business; chưa có chỗ riêng |
| 9.3.15 | Cơ cấu kinh doanh: tổ chức, vai trò, địa lý, chia sẻ nguồn lực | **Chưa có** (một phần nằm trong §5) |
| 9.3.16 | Khái niệm vận hành mức cao: chính sách và ràng buộc, mô tả hệ thống đề xuất, chế độ, nhóm người dùng, môi trường hỗ trợ | §9 Phương án và đề xuất (gần đúng) |
| 9.3.17 | Kịch bản vận hành mức cao | **Chưa có** |
| 9.3.18 | Khái niệm vòng đời khác: mua sắm, triển khai, hỗ trợ, ngừng dùng | §8 chuyển tiếp (một phần) |
| 9.3.19 | Ràng buộc dự án: chi phí và tiến độ | §10 |
Hệ quả: BRD của skill nghiêng về phân tích nghiệp vụ theo BABOK (nhu cầu, mục tiêu, phạm vi, giải pháp, rủi ro). Nếu hợp đồng đòi BRS theo 29148, thêm các nội dung "Chưa có" ở trên hoặc nói rõ lý do bỏ.

## StRS (9.4) và SyRS (9.5): chỉ có tên mục
Đã thấy mục lục nhưng **chưa đọc nội dung chi tiết** nên không ánh xạ. StRS gồm 9.4.2 đến 9.4.19 (mục đích, phạm vi, stakeholder, môi trường, mục tiêu, mô hình kinh doanh, môi trường thông tin, quy trình hệ thống, chính sách, ràng buộc, chế độ và trạng thái, chất lượng vận hành, yêu cầu người dùng, khái niệm và kịch bản vận hành, ràng buộc dự án). SyRS gồm 9.5.2 đến 9.5.19 (chức năng, khả năng sử dụng, hiệu năng, giao diện hệ thống, vận hành, chế độ và trạng thái, đặc tính vật lý, điều kiện môi trường, bảo mật, quản lý thông tin, chính sách và quy định, bảo trì vòng đời, đóng gói và vận chuyển, xác minh, giả định và phụ thuộc). Nếu người dùng cần các tài liệu này, hỏi họ cung cấp hoặc cho đọc tiếp điều 9.4 và 9.5.

## SRS, điều 9.6 (19 nội dung) → SRS của skill
| Chuẩn | Nội dung | Chỗ trong SRS của skill |
|---|---|---|
| 9.6.2 | Mục đích phần mềm | §1 |
| 9.6.3 | Phạm vi: tên sản phẩm, làm gì, ứng dụng và lợi ích, **nhất quán với đặc tả cấp cao hơn** | §1 (thêm câu kiểm nhất quán với tài liệu cấp trên nếu có) |
| 9.6.4 | Góc nhìn sản phẩm: quan hệ với sản phẩm/hệ thống khác; ràng buộc về giao diện hệ thống, người dùng, phần cứng, phần mềm, truyền thông; bộ nhớ; vận hành (gồm sao lưu và phục hồi); điều chỉnh theo địa điểm; giao diện với dịch vụ (SaaS, đám mây) | §2 và §6; **chưa có**: bộ nhớ, vận hành đặc biệt, điều chỉnh theo địa điểm |
| 9.6.5 | Chức năng sản phẩm: tóm tắt các chức năng chính; use case, user story, kịch bản cũng dùng được | §4 (nên có đoạn tóm tắt đầu mục) |
| 9.6.6 | Đặc điểm người dùng (trình độ, kinh nghiệm, khuyết tật, chuyên môn); mô tả lý do của các yêu cầu sau, **không phải yêu cầu** | §2 (tác nhân); chưa tách đặc điểm người dùng |
| 9.6.7 | Giới hạn nhà cung cấp: quy định, phần cứng, giao diện, vận hành song song, kiểm toán, an toàn và bảo mật, v.v. | §2 (ràng buộc) |
| 9.6.8 | Giả định và phụ thuộc: yếu tố làm đổi yêu cầu nếu thay đổi, không phải ràng buộc thiết kế | §2 |
| 9.6.9 | Phân bổ yêu cầu cho phần tử phần mềm; nêu yêu cầu có thể hoãn sang phiên bản sau | **Chưa có**; phần "hoãn" có thể dùng cột Ưu tiên/pha |
| 9.6.10 | Yêu cầu cụ thể: theo đặc tính ở 5.2, tham chiếu chéo phiên bản trước, định danh duy nhất, mô tả mọi đầu vào, đầu ra, chức năng | §4 |
| 9.6.11 | Giao diện ngoài: tên, mục đích, nguồn/đích, khoảng giá trị/độ chính xác, đơn vị, thời gian, quan hệ, định dạng dữ liệu và lệnh, mục dữ liệu | §6 (bảng giao diện của skill thiếu: khoảng giá trị, đơn vị, định dạng) |
| 9.6.12 | Chức năng: kiểm tra đầu vào, trình tự thao tác, phản ứng với tình huống bất thường (lỗi, phục hồi), ảnh hưởng của tham số, quan hệ đầu ra-đầu vào và công thức | §4, §5 |
| 9.6.13 | Khả năng sử dụng và chất lượng khi dùng (đo được hiệu quả, hiệu suất, mức hài lòng, tránh gây hại) | §7 |
| 9.6.14 | Hiệu năng: số liệu tĩnh (số người dùng đồng thời, lượng dữ liệu), động (giao dịch theo thời gian, tải thường và cao điểm); phải đo được | §7 |
| 9.6.15 | Cơ sở dữ liệu logic: loại thông tin, tần suất dùng, quyền truy cập, thực thể và quan hệ, ràng buộc toàn vẹn, bảo mật, lưu giữ | §8 |
| 9.6.16 | Ràng buộc thiết kế từ chuẩn bên ngoài, quy định, dự án | §2 |
| 9.6.17 | Tuân thủ chuẩn: định dạng báo cáo, đặt tên dữ liệu, kế toán, vết kiểm toán | §7/§8 (dữ liệu và nghĩa vụ pháp lý); chưa có mục riêng |
| 9.6.18 | Thuộc tính hệ thống phần mềm (ví dụ nêu: độ tin cậy, sẵn sàng, bảo mật, bảo trì, di động). Chuẩn nói đây là danh sách một phần, và yêu cầu không nên đặt vào chỉ vì là "thiết kế tốt" | §7 |
| 9.6.19 | Xác minh: cách tiếp cận và phương pháp, nên song song với 9.6.10 đến 9.6.18 | §10 |
| 9.6.20 | Thông tin bổ trợ (mẫu dữ liệu, kết quả khảo sát...); phải nêu rõ có thuộc yêu cầu hay không | §11 |
Lưu ý khi dùng: 9.6.6 và 9.6.20 nhấn mạnh phần mô tả **không phải yêu cầu**; khi lắp ráp, đánh dấu rõ đoạn nào là mô tả, đoạn nào là yêu cầu.

## Cách dùng trong skill
- Khi tạo BRD/SRS cho người dùng không có mẫu bắt buộc: dùng khung của skill như cũ; không nói là "theo 29148".
- Khi người dùng nói cần theo 29148: chạy bảng trên làm danh sách kiểm, liệt kê nội dung "Chưa có", hỏi người dùng muốn bổ sung hay ghi lý do bỏ; ghi chú tài liệu "nội dung được đối chiếu với điều 9.3/9.6 của ISO/IEC/IEEE 29148:2018, người chịu trách nhiệm tuân thủ cần xác nhận".
- Viết từng câu yêu cầu: dùng quy ước từ khóa và danh sách từ phải tránh trong `requirements-review/references/iso29148.md`.
