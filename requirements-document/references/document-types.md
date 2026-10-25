# Chọn loại tài liệu và ánh xạ nguồn

## Cách chọn (BABOK 4.4 hỏi người đọc; ánh xạ loại tài liệu là quy ước của skill)
| Hỏi | Ảnh hưởng |
|---|---|
| Ai đọc? | Điều hành, người dùng nghiệp vụ, dev/QA, nhà thầu, cơ quan quản lý |
| Họ cần quyết định hoặc làm gì? | Duyệt đầu tư, duyệt phạm vi, xây, kiểm thử, ký hợp đồng, kiểm tuân thủ |
| Mức chi tiết và trang trọng? | Tài liệu chính thức theo mẫu hay bản gọn không chính thức hay thuyết trình |
| Có ràng buộc hợp đồng/quy định/mẫu tổ chức? | Mẫu bắt buộc thắng khung của skill |
| Hỗ trợ hoạt động nào? | Ước lượng, thiết kế, test, huấn luyện, vận hành |

| Loại | Dành cho | Trọng tâm | Phần chính |
|---|---|---|---|
| **BRD** (business requirements document) | Sponsor, lãnh đạo, người duyệt đầu tư; nhóm giải pháp lập kế hoạch | **Vì sao** thay đổi và **giá trị**: nhu cầu, mục tiêu, phạm vi, stakeholder, yêu cầu business, ràng buộc, tiêu chí thành công, rủi ro | Business, stakeholder (mức cao), transition ở mức cao |
| **PRD** (product requirements document) | Đội sản phẩm: PO, thiết kế, dev, QA | **Cái gì cho ai**: vấn đề, người dùng/persona, mục tiêu và chỉ số, phạm vi, yêu cầu theo giá trị, phát hành | Stakeholder, solution (story/AC), NFR chính |
| **SRS** (software requirements specification) | Dev, QA, kiến trúc sư, nhà thầu; kiểm thử và hợp đồng | **Hệ thống phải làm gì và đạt chất lượng nào**, chi tiết kiểm chứng được | Solution FR + NFR, giao diện, dữ liệu, quy tắc, transition |
Ba tên này là quy ước ngành. ISO/IEC/IEEE 29148 dùng tên BRS, StRS, SyRS, SRS và quy định nội dung (xem `iso29148-content.md`); BRD gần BRS, SRS cùng tên, PRD không có tương ứng trực tiếp; tổ chức có thể dùng tên khác hay gộp. Có thể xuất nhiều tài liệu từ cùng một kho nguồn (mỗi loại một lát cắt).

## Ánh xạ mục → skill nguồn
| Mục tài liệu | Lấy từ | Skill |
|---|---|---|
| Bối cảnh, nhu cầu, hiện trạng | Phân tích hiện trạng (6.1) | `business-case-strategy` |
| Mục tiêu, chỉ tiêu SMART, giá trị | Tương lai (6.2), KPI (10.28) | `business-case-strategy` |
| Phạm vi trong/ngoài | Mô hình phạm vi (10.41) | `requirements-modelling` |
| Stakeholder, RACI | Phân tích stakeholder (3.2, 10.43) | `requirements-stakeholders` |
| Thuật ngữ | Glossary (10.23 nếu có; hoặc glossary của người dùng) | mọi skill |
| Yêu cầu business | Mục tiêu, tiêu chí thành công | `business-case-strategy` |
| Yêu cầu stakeholder | Kết quả khai thác | `requirements-elicitation` |
| Yêu cầu chức năng, story, use case, AC | | `story-writer`, `requirements-modelling` |
| Quy tắc nghiệp vụ | Bảng BR, bảng quyết định | `story-writer`, `requirements-modelling` |
| Yêu cầu phi chức năng | NFR đo được | `nfr-writer` |
| Mô hình quy trình/trạng thái/dữ liệu | | `requirements-modelling` |
| Giao diện | Phân tích giao diện | `requirements-modelling` |
| Yêu cầu chuyển tiếp | Dữ liệu chuyển đổi, huấn luyện, vận hành liên tục; kế hoạch chuyển giai đoạn | `business-case-strategy` + `story-writer` |
| Ưu tiên và phát hành | Bảng ưu tiên, kế hoạch phát hành | `requirements-prioritize` |
| Truy vết | Ma trận, tác động | `requirements-trace` |
| Tiêu chí chấp nhận, kế hoạch UAT | | `requirements-testcases` |
| Giả định, ràng buộc, phụ thuộc, rủi ro | | mọi skill; `business-case-strategy` cho rủi ro |
| Câu hỏi mở | | mọi skill |

## Bản gọn cho agile
Khi đội không muốn tài liệu dài: một **tờ tóm tắt sản phẩm** (vấn đề, người dùng, mục tiêu và chỉ số, phạm vi) + **backlog** (story có AC đủ theo mức chuẩn bị) + mô hình cần thiết + bảng quy tắc và NFR. Agile Extension v2 nhấn mạnh chỉ elaborate story gần tới lượt làm và dùng ví dụ/mô hình làm bổ trợ; đừng dựng PRD dài cho story chưa đến lượt. Mức chi tiết theo cách tiếp cận BA đã chọn (3.1).
