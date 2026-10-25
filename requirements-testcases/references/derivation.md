# Suy ra test từ yêu cầu

Phần "cơ sở" ghi rõ cái gì thuộc BABOK/Agile Extension, cái gì thuộc ISTQB CTFL v4.0.1 (đã đối chiếu bản PDF; diễn giải lại), cái gì là thực hành phổ biến hoặc quy ước của skill.

Thuật ngữ ISTQB dùng chung: **coverage item** là cái cần chạm tới (phân vùng, giá trị biên, cột quy tắc, trạng thái, chuyển). Độ phủ = số coverage item đã được ít nhất một test chạm tới / tổng số coverage item. Báo độ phủ theo đúng đơn vị đó, không nói "phủ 100%" mà không nêu coverage item nào.

## 1. Acceptance criteria dạng Given-When-Then
Cơ sở: Agile Extension 7.2 (scenario BDD dùng làm AC và làm test; một WHEN; GIVEN/THEN có thể ghép bằng AND).
- Mỗi scenario = ít nhất một test; scenario có nhiều THEN vẫn là một test nếu cùng một WHEN.
- Hỏi "what if" cho từng GIVEN: thiếu dữ liệu, sai định dạng, quyền khác, trạng thái khác, đồng thời hai người. Đây là cách lộ kịch bản còn thiếu (Agile Extension 7.2.2); ghi các ca tìm thêm thành đề xuất AC bổ sung, **không** tự coi là đã được duyệt.
- AC dạng quy tắc (danh sách điều kiện) thì mỗi dòng một test.

## 2. Quy tắc nghiệp vụ có ngưỡng (BR)
Cơ sở: ISTQB CTFL v4.0.1, 4.2.1 và 4.2.2.
- **Phân vùng tương đương (EP)**: chia dữ liệu thành các phân vùng mà đối tượng kiểm thử được kỳ vọng xử lý như nhau; một test cho mỗi phân vùng là đủ theo lý thuyết của kỹ thuật. Phân vùng không chồng lấn và không rỗng; áp dụng được cho đầu vào, đầu ra, cấu hình, giá trị nội bộ, thời gian, tham số giao diện. Phân vùng hợp lệ và không hợp lệ: định nghĩa "hợp lệ" có thể khác nhau giữa các nhóm, nên hỏi yêu cầu chứ không tự quyết. Độ phủ EP tính trên số phân vùng, kể cả phân vùng không hợp lệ.
- Nhiều tham số đầu vào: tiêu chí đơn giản nhất là **Each Choice**, mỗi phân vùng của mỗi tham số xuất hiện ít nhất một lần; nó **không** xét tổ hợp giữa các tham số. Cần tổ hợp thì dùng bảng quyết định hoặc ghi rõ đó là quyết định rủi ro.
- **Giá trị biên (BVA)**: chỉ áp dụng cho phân vùng có thứ tự. Hai phiên bản: **2 giá trị** (giá trị biên và láng giềng gần nhất thuộc phân vùng kề) và **3 giá trị** (giá trị biên và cả hai láng giềng). 3 giá trị chặt hơn: ví dụ ISTQB là điều kiện "x ≤ 10" bị cài nhầm thành "x = 10": cặp 2 giá trị (10, 11) không bắt được lỗi, còn x = 9 của phiên bản 3 giá trị có khả năng bắt. Mặc định của skill: dùng 3 giá trị cho quy tắc có ngưỡng và nói rõ đã chọn; dùng 2 giá trị khi người dùng yêu cầu gọn.
- Ví dụ quy tắc "hủy trước ≥ 2 giờ" (giả định đơn vị phút, ngưỡng 120): 3 giá trị = 119, 120, 121. Ví dụ này là minh họa của skill, không phải của ISTQB.
- Quy tắc định nghĩa (không phải hành vi) thường kiểm bằng ví dụ phân loại, không phải luồng.
- Ghi chú về nguồn: ghi chú phát hành v4.0.1 nói có bổ sung về cách xử lý phân vùng không hợp lệ ở 4.2.1, nhưng nội dung 4.2.1 trong bản PDF đã đọc không có câu đó. Thực hành "mỗi test chỉ chứa một giá trị không hợp lệ" vì tránh che lỗi là hợp lý và ISTQB nêu nguyên tắc tương tự cho chuyển không hợp lệ ở 4.2.4, nhưng không trích nó như văn bản của 4.2.1.

## 3. Bảng quyết định
Cơ sở: bảng quyết định là cách biểu diễn gọn mọi quy tắc của một quyết định (BABOK 10.17); suy ra test theo ISTQB CTFL v4.0.1, 4.2.3.
- Hàng là điều kiện và hành động; mỗi **cột** là một quy tắc quyết định. Ký hiệu ISTQB: điều kiện T (đúng), F (sai), "–" (không ảnh hưởng kết quả), N/A (không khả thi với quy tắc đó); hành động X (xảy ra), để trống (không xảy ra). Bảng **giới hạn-mục** (limited-entry) chỉ dùng giá trị Boolean; bảng **mở rộng** (extended-entry) cho điều kiện/hành động nhận nhiều giá trị (khoảng, phân vùng, giá trị rời rạc).
- Coverage item là các **cột khả thi**. **Mỗi cột khả thi = một test** (tổ hợp điều kiện cụ thể + kết quả). Độ phủ = số cột đã chạy / số cột khả thi.
- Bảng đầy đủ có đủ cột cho mọi tổ hợp; bỏ cột không khả thi, gộp cột mà điều kiện không ảnh hưởng thì được bảng rút gọn. Số quy tắc tăng theo hàm mũ khi thêm điều kiện; khi quá nhiều thì dùng bảng rút gọn hoặc tiếp cận theo rủi ro và ghi rõ đã làm vậy. Thuật toán rút gọn nằm ngoài phạm vi syllabus.
- Điểm mạnh nêu trong ISTQB: lộ tổ hợp dễ bị bỏ sót và lộ khoảng trống hoặc mâu thuẫn trong yêu cầu. Vì thế tổ hợp chưa có cột nào hoặc hai cột mâu thuẫn là **câu hỏi mở**, không đoán kết quả.
- Ô "–" (không ảnh hưởng): chọn thêm một giá trị khác của điều kiện đó trong ít nhất một test để xác nhận thật sự không ảnh hưởng (đây là cách làm của skill, không phải yêu cầu của ISTQB).

## 4. Mô hình trạng thái / bảng trạng thái
Cơ sở: bảng trạng thái liệt kê từng chuyển (BABOK 10.44.3.4); suy ra test theo ISTQB CTFL v4.0.1, 4.2.4.
- Chuyển được nhãn theo dạng "sự kiện [điều kiện bảo vệ] / hành động"; điều kiện bảo vệ và hành động bỏ được nếu không có. Một test thường là chuỗi sự kiện dẫn qua chuỗi trạng thái, và **một test có thể phủ nhiều chuyển**. Bảng trạng thái khác sơ đồ ở chỗ ô trống cho thấy rõ chuyển không hợp lệ.
- Ba tiêu chí phủ (chọn và nêu rõ trong báo cáo):
  - **Mọi trạng thái**: coverage item là trạng thái. Yếu nhất, thường đạt mà chưa chạy hết chuyển.
  - **Chuyển hợp lệ** (còn gọi 0-switch): coverage item là từng chuyển hợp lệ. Phổ biến nhất; đạt thì bao gồm phủ mọi trạng thái. Mặc định của skill.
  - **Mọi chuyển**: chạy mọi chuyển hợp lệ và **cố gắng** thực hiện các chuyển không hợp lệ; bao gồm hai tiêu chí trên. ISTQB nêu đây nên là mức tối thiểu cho phần mềm trọng yếu về sứ mệnh và an toàn.
- **Mỗi chuyển hợp lệ = một test** (trạng thái đầu, sự kiện, điều kiện, trạng thái cuối, hành động đi kèm).
- **Chuyển không hợp lệ**: với mỗi trạng thái, thử một sự kiện không có trong bảng và kỳ vọng bị từ chối. **Mỗi test chỉ thử một chuyển không hợp lệ** để tránh che lỗi (một lỗi ngăn phát hiện lỗi khác). Chỉ viết khi yêu cầu nói rõ cách phản ứng; không thì hỏi.
- Kiểm hành động cho phép ở mỗi trạng thái (ví dụ chỉnh sửa khi đã hủy).
- Trạng thái cuối: kiểm không còn chuyển ra.

## 5. Use case
Cơ sở: luồng chính, luồng thay thế, luồng ngoại lệ, hậu điều kiện đúng với mọi luồng (BABOK 10.47).
- Một test cho luồng chính; một test cho mỗi luồng thay thế; một test cho mỗi luồng ngoại lệ.
- Với mỗi test kiểm hậu điều kiện (thành công và tối thiểu: an ninh, toàn vẹn dữ liệu).
- Tiền điều kiện không được kiểm trong use case (10.47); nếu cần kiểm hành vi khi tiền điều kiện sai, đó là test của yêu cầu khác.

## 6. Yêu cầu phi chức năng
Cơ sở: tiêu chí đo được, nên mỗi NFR cần số đo, điều kiện và cách đo (từ `nfr-writer`).
- Mỗi NFR đo được = một test với ngưỡng, tải/điều kiện, công cụ đo, môi trường.
- NFR thiếu số đo: không viết test; chuyển `nfr-writer`.
- Phần cần chuyên môn (tải, bảo mật, khả năng truy cập) ghi rõ loại test và giao QA/chuyên gia; BA nêu yêu cầu và ngưỡng, không thiết kế kịch bản kỹ thuật.
- NFR pháp lý (dữ liệu cá nhân, v.v.): chỉ nêu điều cần chứng minh, giao người có chuyên môn pháp lý xác nhận.

## 7. Dữ liệu và từ điển dữ liệu
- Mỗi giá trị cho phép, độ dài, định dạng, bắt buộc = test hợp lệ/không hợp lệ ở biên.
- Quan hệ (bội số) = test số lượng tối thiểu và tối đa (0, 1, nhiều) nếu yêu cầu nêu rõ.

## 8. Quyền (ma trận vai trò)
- Mỗi ô CRUD "được" = một test dương; ô "không được" = một test âm (kỳ vọng từ chối). Ô "?" = câu hỏi mở.

## 9. Kỹ thuật dựa trên kinh nghiệm (bổ sung sau kỹ thuật hình thức)
Cơ sở: ISTQB CTFL v4.0.1, 4.4. Dùng khi yêu cầu thiếu hoặc mơ hồ, hoặc để bổ sung cho các kỹ thuật ở trên; không thay thế chúng.
- **Đoán lỗi** (4.4.1): dựa trên cách ứng dụng từng hoạt động, loại lỗi dev hay mắc, lỗi ở hệ thống tương tự. Nhóm lỗi gợi ý: đầu vào, đầu ra, logic, tính toán, giao diện, dữ liệu. Ca đoán lỗi **không có nguồn yêu cầu** nên ghi loại "Đề xuất bổ sung", kết quả mong đợi là câu hỏi mở cho BA/PO, không tự quy định.
- **Khám phá** (4.4.2): thiết kế, chạy, đánh giá đồng thời; có thể theo phiên có khung thời gian, hiến chương (charter) và buổi tổng kết. ISTQB nêu nó hữu ích khi đặc tả ít hoặc thiếu, hoặc khi gấp thời gian. Skill chỉ đề xuất charter (mục tiêu, phạm vi, thời lượng); phần chạy do tester.
- **Theo checklist** (4.4.3): mục checklist nên là câu hỏi kiểm riêng từng mục; ISTQB khuyên không đưa vào checklist những mục kiểm tự động được, mục thuộc tiêu chí vào/ra, hoặc mục quá chung. Có thể dùng checklist chất lượng của `requirements-review` hoặc đặc tính ISO 25010 làm cơ sở, ghi rõ đó là checklist chứ không phải yêu cầu.

## 10. Định dạng acceptance criteria và ATDD
Cơ sở: ISTQB CTFL v4.0.1, 4.5.1 đến 4.5.3; Agile Extension 7.2.
- AC là điều kiện để stakeholder chấp nhận story và có thể coi là điều kiện kiểm thử (test condition). ISTQB nêu hai dạng phổ biến: **theo kịch bản** (Given/When/Then) và **theo quy tắc** (danh sách kiểm hoặc bảng vào-ra); đội có thể dùng dạng khác nếu rõ ràng, không mơ hồ. Dạng quy tắc: mỗi dòng một test (xem mục 1).
- AC nên mô tả cả kịch bản dương và âm (4.5.2). Nếu AC chỉ có đường dương, đưa vào "Cần làm rõ".
- **ATDD** (4.5.3): test được tạo trước khi hiện thực, từ workshop có nhiều góc nhìn (khách hàng, dev, tester). Thứ tự ISTQB gợi ý: test dương trước, rồi âm, rồi đặc tính phi chức năng. Test phủ mọi đặc điểm của story, không vượt ngoài story, và không có hai test mô tả cùng một đặc điểm. Dùng ba tiêu chí này để tự kiểm bộ test (liên kết `test-quality.md`).
- Story khó viết test (stakeholder không biết cách kiểm) là dấu hiệu story chưa rõ hoặc chưa có giá trị theo INVEST (4.5.1): trả cho `story-writer`.
