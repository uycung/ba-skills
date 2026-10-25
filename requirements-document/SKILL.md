---
name: requirements-document
description: "Lắp ráp các đầu ra của bộ skill BA (story, NFR, quy tắc, mô hình, truy vết, stakeholder, business case) thành tài liệu yêu cầu hoàn chỉnh dạng BRD, PRD hoặc SRS theo người đọc, kèm kiểm nhất quán và chỗ còn thiếu; dùng khi cần gói yêu cầu để duyệt, bàn giao dev hoặc ký hợp đồng."
---

# Requirements Document (BRD / PRD / SRS)

Mục tiêu: một tài liệu đọc được liền mạch, **mọi mục lấy từ đầu ra đã có**, chỗ thiếu hiện ra rõ chứ không bị lấp bằng chữ. Trả lời bằng ngôn ngữ người dùng (mặc định tiếng Việt).

## Nguồn và giới hạn (nói thẳng khi liên quan)
- **Thuộc BABOK v3**: gói yêu cầu (requirements package) là dạng gói phân tích nghiệp vụ tập trung vào yêu cầu, có thể là đường cơ sở của một tập yêu cầu (thuật ngữ); "requirements document" trong từ điển trỏ về requirements package. Chọn hình thức theo người đọc: ai đọc, mỗi nhóm cần và hiểu gì, phong cách ưa thích, thông tin quan trọng, định dạng có phù hợp không, hỗ trợ hoạt động nào, ràng buộc quy định hoặc hợp đồng (4.4). Hình thức gồm tài liệu chính thức theo mẫu của tổ chức, tài liệu không chính thức, bản thuyết trình (4.4). Phân loại yêu cầu: business, stakeholder, solution (functional, non-functional), transition (2.3, Requirements Classification Schema). Kiến trúc yêu cầu và viewpoint (7.4).
- **KHÔNG thuộc BABOK**: tên và cấu trúc cụ thể BRD, PRD, SRS. Đó là quy ước ngành; BABOK không quy định. Chuẩn ISO/IEC/IEEE 29148:2018 **đã được đọc** (điều 5.2, 6.5.2.2, 9.2, 9.3, 9.6; bản người dùng cung cấp). Chuẩn quy định **nội dung** của BRS/StRS/SyRS/SRS, không quy định thứ tự mục; khung mục trong `templates/` vẫn là khung của skill dựa trên BABOK, không phải khung chuẩn. `references/iso29148-content.md` đối chiếu nội dung chuẩn với khung của skill để dùng khi hợp đồng hoặc tổ chức yêu cầu tuân thủ 29148. StRS (9.4) và SyRS (9.5) mới có mục lục, chưa đọc nội dung. Nếu tổ chức hay hợp đồng có mẫu bắt buộc, dùng mẫu đó và ánh xạ nội dung vào.
- Skill không viết yêu cầu mới. Muốn viết hoặc sửa yêu cầu: `story-writer`, `nfr-writer`, `requirements-modelling`.

## Nguyên tắc cứng
1. **Chỉ lắp ráp, không sáng tác.** Mỗi yêu cầu trong tài liệu có ID và trỏ nguồn (story, AC, BR, NFR, mô hình). Không có nguồn: không đưa vào, ghi ở "Chỗ còn thiếu".
2. **Chọn loại tài liệu theo người đọc và quyết định cần ra** (4.4), không theo thói quen. Hỏi tối đa 3 câu: ai đọc, để quyết định/làm gì, có mẫu bắt buộc không.
3. **Mục trống hiện rõ**: giữ tiêu đề, ghi "Chưa có", nêu cần gì, của ai, skill nào tạo. Không viết chữ cho đầy.
4. **Một nguồn sự thật cho mỗi thông tin.** Không chép đi chép lại giữa các mục; dẫn chiếu ID. Hai chỗ nói cùng một việc phải khớp từng chữ hoặc một chỗ trỏ về chỗ kia.
5. **Giữ ID ổn định** qua các phiên bản; ghi lịch sử thay đổi và phiên bản đường cơ sở khi người dùng xin chốt (xem `references/assembly-checks.md`).
6. **Phân loại yêu cầu rõ ràng**: business, stakeholder, solution chức năng, solution phi chức năng, transition (dữ liệu chuyển đổi, đào tạo, vận hành liên tục: BABOK nêu).
7. **Không giấu giả định, ràng buộc, phụ thuộc, rủi ro, câu hỏi mở**; mỗi cái có mục riêng.
8. **Tài liệu chưa duyệt thì đóng dấu chưa duyệt**; đưa cổng sẵn sàng vào để `requirements-review` kiểm trước khi xin duyệt.

## Quy trình
1. **Thu thập đầu vào**: liệt kê các sản phẩm đã có (mục tiêu và business case, stakeholder, story/FR/use case, BR, NFR, mô hình, ma trận truy vết, câu hỏi mở). Nếu người dùng chỉ đưa thô (ghi chép họp, ý tưởng), dừng và chuyển `requirements-elicitation`/`story-writer` trước.
2. **Chọn loại tài liệu và độ sâu** theo `references/document-types.md`.
3. **Lập bản đồ nguồn → mục**: mỗi mục lấy từ sản phẩm nào; mục nào chưa có nguồn.
4. **Lắp ráp** theo mẫu trong `templates/` (BRD, PRD hoặc SRS). Giữ nguyên văn yêu cầu từ nguồn; chỉ thêm câu dẫn nối.
5. **Kiểm nhất quán** (`references/assembly-checks.md`): ID, thuật ngữ, số liệu, phạm vi, ưu tiên, trạng thái, quan hệ truy vết.
6. **Báo "Chỗ còn thiếu" và "Sẵn sàng để duyệt?"**: gợi ý chạy `requirements-review` trước khi xin duyệt (BABOK 5.5: đầu vào là yêu cầu đã verify).
7. **Trả**: tài liệu + danh sách thiếu + giả định + câu hỏi mở. Không tóm tắt lại những gì tài liệu đã nói.

## Phối hợp
Mục tiêu, hiện trạng/tương lai, business case: `business-case-strategy`. Danh sách bên liên quan và RACI: `requirements-stakeholders`. Story/AC: `story-writer`. NFR: `nfr-writer`. Mô hình: `requirements-modelling`. Ma trận truy vết, tác động thay đổi: `requirements-trace`. Test/UAT: `requirements-testcases`. Rà soát trước duyệt: `requirements-review`.

## Tệp tham chiếu
- `references/document-types.md`: BRD/PRD/SRS cho ai, ánh xạ mục → skill nguồn, bản gọn cho agile.
- `references/assembly-checks.md`: kiểm nhất quán, trạng thái, phiên bản, phê duyệt.
- `references/iso29148-content.md`: nội dung BRS (9.3) và SRS (9.6) theo ISO/IEC/IEEE 29148:2018, ánh xạ vào khung của skill, mục nào chưa có.
- `templates/brd-template.md`, `templates/prd-template.md`, `templates/srs-template.md`.
