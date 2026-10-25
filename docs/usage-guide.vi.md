# Bộ 11 skill BA: hướng dẫn sử dụng

Bộ skill giúp BA làm việc với Claude từ đầu dự án đến lúc bàn giao: phân tích stakeholder, business case, khai thác yêu cầu, viết story/NFR, mô hình hóa, ưu tiên, truy vết, rà soát, test case/UAT và lắp tài liệu BRD/PRD/SRS. Cập nhật lần cuối 25/10/2026.

## 1. Nguyên tắc chung của cả bộ

- **Có nguồn, không bịa.** Nội dung bám BABOK v3 và Agile Extension v2; test dựa trên ISTQB CTFL v4.0.1; NFR dựa trên ISO/IEC 25010:2023; chất lượng yêu cầu bổ sung từ ISO/IEC/IEEE 29148:2018. Skill luôn nói rõ cái gì thuộc nguồn nào, cái gì chỉ là quy ước của skill.
- **Không tự điền con số.** Ngưỡng NFR, tiêu chí ra UAT, chỉ tiêu mục tiêu... phải do người dùng hoặc PO chốt. Chưa có thì ghi "cần chốt".
- **Cuối mỗi bản trả đều có** danh sách Giả định, Cần làm rõ và phần chưa đủ để làm tiếp, để biết chỗ nào chưa chắc.
- **Yêu cầu luôn trỏ về nguồn.** Mỗi mục có ID, truy được về mục tiêu hoặc người nêu yêu cầu.
- **Phần pháp lý Việt Nam chỉ là tham khảo.** Dòng nào gắn ⚠️ thì chưa được xác nhận từ văn bản gốc; luôn cần pháp chế xác nhận.
- Ngôn ngữ trả lời mặc định theo ngôn ngữ người dùng (tiếng Việt).

## 2. Danh sách 11 skill

| Skill | Dùng khi | Đưa vào | Nhận lại |
| --- | --- | --- | --- |
| `requirements-stakeholders` | Đầu dự án hoặc đầu đợt khai thác, cần biết ai cần gặp, ai quyết định | Mô tả dự án, sơ đồ tổ chức, ghi chép họp | Danh sách stakeholder, ma trận ảnh hưởng, onion, RACI, persona, kế hoạch cộng tác |
| `business-case-strategy` | Cần biện minh hoặc chọn hướng thay đổi trước khi vào yêu cầu chi tiết | Mô tả vấn đề, dữ liệu chi phí và lợi ích | Hiện trạng, tương lai, khoảng cách, rủi ro, chiến lược, business case, ROI/NPV/IRR, SWOT, KPI |
| `requirements-elicitation` | Trước hoặc sau buổi gặp stakeholder | Mục tiêu buổi họp hoặc ghi chép họp | Kế hoạch khai thác, bộ câu hỏi, kết quả có nguồn (chưa xác nhận) và danh sách cần xác nhận |
| `requirements-modelling` | Mô tả bằng chữ chưa đủ rõ | Quy trình, quy tắc, dữ liệu, vai trò | Mô hình quy trình, trạng thái, dữ liệu, bảng quyết định, use case, phạm vi, giao diện, ma trận quyền |
| `story-writer` | Biến ý tưởng thô thành yêu cầu rõ | Ý tưởng, ghi chép, yêu cầu thô | Story, acceptance criteria, use case, bảng quy tắc nghiệp vụ; hoặc bản rà soát story có sẵn |
| `nfr-writer` | "Nhanh, an toàn, dễ dùng" cần thành số đo được | Loại sản phẩm, spec hiện có | NFR đo được theo 9 đặc tính ISO 25010:2023, trade-off, danh sách cần xác nhận |
| `requirements-prioritize` | Xếp backlog, chốt MVP, đánh giá lại khi đổi bối cảnh | Danh sách yêu cầu kèm mã, ràng buộc | Bảng chấm điểm có lý do, thứ tự, lát cắt phát hành, xung đột chưa giải quyết |
| `requirements-trace` | Kiểm lỗ hổng spec, phân tích tác động khi yêu cầu đổi | PRD, story, NFR, test | Ma trận truy vết, khoảng trống, mâu thuẫn, phân tích tác động |
| `requirements-review` | Trước khi xin duyệt hoặc giao dev/tester | Tài liệu yêu cầu bất kỳ | Báo cáo phát hiện có mức nghiêm trọng, kết luận sẵn sàng duyệt hay chưa; hoặc kế hoạch buổi review |
| `requirements-testcases` | Biến yêu cầu thành bộ kiểm thử, lập UAT | Story, AC, quy tắc, bảng quyết định, mô hình trạng thái, NFR | Test case truy vết được, ma trận phủ, gói UAT, chọn test hồi quy sau thay đổi |
| `requirements-document` | Cần gói yêu cầu để duyệt, bàn giao hoặc ký hợp đồng | Các đầu ra của những skill trên | BRD, PRD hoặc SRS, kiểm nhất quán, danh sách chỗ còn thiếu |

## 3. Thứ tự làm việc đề xuất

Đây là gợi ý, không bắt buộc. Có thể bỏ bước nếu đã có đầu ra tương ứng.

1. **Bối cảnh:** `requirements-stakeholders`, rồi `business-case-strategy`.
2. **Khai thác:** `requirements-elicitation` (lập kế hoạch, sau mỗi buổi họp xử lý ghi chép).
3. **Viết và mô hình hóa:** `requirements-modelling`, `story-writer`, `nfr-writer`.
4. **Quyết định:** `requirements-prioritize`.
5. **Kiểm soát:** `requirements-trace`, `requirements-review`.
6. **Kiểm chứng:** `requirements-testcases`.
7. **Đóng gói:** `requirements-document`.

Khi yêu cầu thay đổi: `requirements-trace` (tác động), `requirements-testcases` (chọn test hồi quy), `requirements-review` (kiểm lại sau sửa).

## 4. Câu lệnh mẫu

| Muốn làm gì | Ví dụ |
| --- | --- |
| Phân tích stakeholder | "Lập danh sách stakeholder và RACI cho dự án đặt lịch spa, đây là mô tả…" |
| Business case | "Lập business case cho việc tự động hóa nhắc lịch; chi phí và lợi ích như bảng này…" |
| Xử lý ghi chép họp | "Đây là ghi chép buổi họp với lễ tân, tách ra điều đã nói, suy luận, giả định và danh sách cần xác nhận." |
| Mô hình | "Dựng bảng quyết định cho quy tắc hủy lịch từ mô tả này." |
| Story | "Viết story và AC cho tính năng đổi lịch hẹn; hỏi tôi nếu thiếu thông tin." |
| NFR | "Spec này có đủ NFR chưa? Sản phẩm là web app nội bộ có dữ liệu cá nhân." |
| Ưu tiên | "Xếp 20 story này thành 3 lát cắt phát hành, ràng buộc là cuối quý." |
| Truy vết | "Lập ma trận truy vết và chỉ ra chỗ hở; nếu bỏ story S-07 thì ảnh hưởng gì?" |
| Rà soát | "Rà soát PRD này và cho biết đã sẵn sàng duyệt chưa." |
| Test | "Sinh test case và ma trận phủ từ các AC này; giá trị biên theo 3 giá trị." |
| UAT | "Lập gói UAT cho luồng đặt lịch đầu-cuối." |
| Tài liệu | "Lắp BRD từ các sản phẩm sau và liệt kê chỗ còn thiếu." |

## 5. Nguồn và độ tin cậy

| Nguồn | Dùng cho | Mức đối chiếu |
| --- | --- | --- |
| BABOK v3 | Hầu hết skill (khai thác, phân tích, truy vết, rà soát...) | Đọc từ PDF, diễn đạt lại; số mục được trích; một số mục chưa đọc (xem mục 6) |
| Agile Extension v2 | Story, BDD, persona, backlog | Đọc từ PDF, diễn đạt lại |
| ISO/IEC 25010:2023 | NFR | Tên đặc tính khớp bản 2023; cột "Ý nghĩa" là diễn đạt của skill, chưa đối chiếu với định nghĩa chính thức |
| ISTQB CTFL v4.0.1 | Thiết kế test: phân vùng tương đương, giá trị biên, bảng quyết định, chuyển trạng thái, UAT, ATDD | Đã đối chiếu với PDF |
| ISO/IEC/IEEE 29148:2018 | Đặc tính chất lượng yêu cầu, từ khóa, thuộc tính, phương pháp xác minh, nội dung BRS/SRS | Đã đối chiếu với bản chuẩn (điều 5.2, 6.5.2.2, 9.2, 9.3, 9.6) |
| Pháp luật Việt Nam và EU AI Act | NFR pháp lý (`legal-vn.md` trong `nfr-writer`) | Kiểm lần cuối 24/10/2026; một phần đọc từ văn bản gốc, một phần chỉ từ nguồn thứ cấp (gắn ⚠️) |

Repo này không chứa PDF hay bản chuẩn gốc của các nguồn trên; skill chỉ diễn đạt lại và trích số mục.

## 6. Giới hạn đã biết và việc còn treo

- **Pháp lý (⚠️):** chưa đọc toàn văn NĐ 330/2026 và NĐ 142/2026; danh mục AI rủi ro cao (QĐ 33/2026/QĐ-TTg) mới có bản trích; chưa xác nhận tình trạng NĐ 53/2022, NĐ 85/2016, TT 12/2022. Khung phạt NĐ 330 lấy từ nguồn thứ cấp nên không ghi con số vào NFR. Cần pháp chế xác nhận trước khi đưa vào hợp đồng hay spec.
- **ISO 29148:** StRS (9.4) và SyRS (9.5) mới có mục lục, chưa đọc nội dung.
- **BABOK/Agile Extension:** một số mục chưa đọc (ví dụ 10.3, 10.4, 10.6, 10.8, 10.49, 8.3, 8.4, chương 3.1 và 3.3 đến 3.5, các chương 1 đến 6 và 7.8 đến 7.17, 7.22 đến 7.24 của Agile Extension).
- **Chưa chạy thử trên tài liệu thật.** Nên thử cả bộ trên một PRD hoặc ghi chép họp thật và ghi lại chỗ skill làm chưa tốt.
- Skill không thay QA, pháp chế hay người ra quyết định: nó chuẩn bị đầu vào để người có thẩm quyền xác nhận.

Cài đặt và cập nhật: xem [README](../README.md#install).
