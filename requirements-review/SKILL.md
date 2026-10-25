---
name: requirements-review
description: "Rà soát chất lượng tài liệu yêu cầu (story, FR, use case, NFR, quy tắc, mô hình, PRD) theo BABOK: kiểm tra viết đúng cách (verify) và đúng nhu cầu (validate), trả báo cáo phát hiện có mức nghiêm trọng và kết luận sẵn sàng duyệt hay chưa; dùng trước khi xin duyệt hoặc giao cho dev/tester, hoặc để lập kế hoạch một buổi review."
---

# Requirements Review

Khung theo BABOK v3: Verify Requirements (7.2), Validate Requirements (7.3), Reviews (10.37), Approve Requirements (5.5). Trả lời bằng ngôn ngữ người dùng (mặc định tiếng Việt). Skill này **chấm tài liệu, không chấm người** (10.37.2: rà soát nhắm vào sản phẩm công việc).

## Hai câu hỏi khác nhau
- **Verify**: yêu cầu có được viết đúng không (rõ, đủ, nhất quán, kiểm chứng được, dùng đúng ký hiệu)? Đây là điều kiện để sẵn sàng cho validate.
- **Validate**: yêu cầu có thật sự phục vụ mục tiêu kinh doanh, nằm trong phạm vi giải pháp, mang lại lợi ích cho stakeholder không? Validate có thể bắt đầu trước khi verify xong nhưng **không thể kết thúc trước** (7.3.3).
Luôn nói rõ báo cáo đang trả lời câu nào. Chất lượng cuối cùng do stakeholder quyết định (7.2.2): skill chỉ chỉ ra chỗ có rủi ro.

## Nguyên tắc cứng
1. **Mỗi phát hiện trỏ đúng câu/mục/mã bị lỗi**, nêu đặc tính vi phạm, vì sao là vấn đề, cách sửa. Không nhận xét chung chung kiểu "chưa rõ".
2. **Không tự sửa nội dung nghiệp vụ.** Có thể đề xuất cách viết lại câu chữ; chỗ thiếu thông tin thì thành câu hỏi có người trả lời, không điền số, không đoán quy tắc.
3. **Phân biệt lỗi chắc chắn và nghi vấn.** Lỗi chắc chắn: tự mâu thuẫn trong tài liệu, thiếu trường bắt buộc, từ mơ hồ không kèm tiêu chí. Nghi vấn: cần xác nhận với người biết nghiệp vụ; ghi là "nghi vấn".
4. **Mức nghiêm trọng là quy ước của skill** (không phải của BABOK): Chặn (không thể làm/test/duyệt nếu không sửa), Nên sửa (gây hiểu nhầm hoặc làm lại), Gợi ý (cải thiện). Ghi rõ tiêu chí chọn mức.
5. Kết luận cuối bản: **Sẵn sàng / Có điều kiện / Chưa sẵn sàng** cho bước tiếp theo (validate, duyệt, hoặc giao đội), kèm điều kiện cụ thể.
6. Không khẳng định "tài liệu đạt" chỉ vì không tìm thấy lỗi: nêu phạm vi đã kiểm (những mục nào, đặc tính nào) và cái chưa kiểm được vì thiếu thông tin.

## Quy trình
1. **Xác định**: loại sản phẩm công việc (story, use case, NFR, mô hình, cả PRD), mục tiêu review (bắt lỗi, kiểm chuẩn, xác nhận đủ và đúng, đồng thuận, giải quyết vấn đề, giáo dục: 10.37.3), mức chính thức. Hỏi tối đa 3 câu nếu thiếu: ai là người dùng tài liệu này, đã có glossary/chuẩn mẫu của đội chưa, mục tiêu kinh doanh và phạm vi ở đâu.
2. **Verify** từng mục theo 9 đặc tính chất lượng và các hoạt động verify (`references/quality-characteristics.md`, `references/verify-validate.md`). Dùng danh sách kiểm phù hợp loại tài liệu (`references/checklists.md`).
3. **Kiểm chéo** giữa các mục và mô hình: thứ được nhắc ở nơi này mà thiếu ở nơi kia, thuật ngữ dùng không nhất quán, quy tắc mâu thuẫn.
4. **Validate** khi có mục tiêu, phạm vi, mô tả trạng thái tương lai: giả định, tiêu chí đánh giá đo được, tương thích phạm vi (`references/verify-validate.md`). Nếu chưa có các đầu vào này thì nói rõ validate chỉ làm được một phần.
5. **Lập báo cáo** theo `templates/review-report.md`: phạm vi đã kiểm, bảng phát hiện, kết luận, mục theo dõi (item tracking), câu hỏi cần người trả lời.
6. Khi người dùng đã sửa: **kiểm lại** từng phát hiện cũ (đã xử lý / còn / phát sinh mới), không đánh giá lại từ đầu.

## Ba chế độ
- **A. Rà soát tài liệu** (mặc định): bước 1 đến 5.
- **B. Lập kế hoạch buổi review**: chọn kỹ thuật theo mục tiêu và mức rủi ro, vai trò (author, reviewer, facilitator, scribe), chương trình, checklist gửi trước, cách ghi kết quả (`references/review-techniques.md`).
- **C. Kiểm lại sau sửa**: bước 6.

## Phối hợp với skill khác
Phát hiện thiếu liên kết hoặc độ phủ: chuyển `requirements-trace`. Story/AC cần viết lại: `story-writer`. NFR thiếu số đo: `nfr-writer`. Mô hình sai hoặc thiếu: `requirements-modelling`. Mục theo dõi: định dạng ở `requirements-elicitation/references/item-tracking.md`.

## Tệp tham chiếu
- `references/quality-characteristics.md`: 9 đặc tính, câu hỏi kiểm, lỗi điển hình, cách sửa.
- `references/verify-validate.md`: hoạt động verify, các phần tử validate, cổng sẵn sàng trước khi duyệt.
- `references/review-techniques.md`: 7 kỹ thuật, vai trò, khi nào dùng.
- `references/checklists.md`: checklist theo loại tài liệu.
- `references/iso29148.md`: ISO/IEC/IEEE 29148:2018 đã đối chiếu với bản chuẩn: 9 đặc tính từng yêu cầu, 5 đặc tính cả tập, từ khóa và nhóm từ phải tránh, thuộc tính, 4 phương pháp xác minh, nội dung điều 9. Dùng bổ sung cho 9 đặc tính BABOK, không thay.
- `templates/review-report.md`: mẫu báo cáo.
