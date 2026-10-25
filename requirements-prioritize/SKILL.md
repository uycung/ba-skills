---
name: requirements-prioritize
description: "Giúp BA ưu tiên hóa yêu cầu/story có căn cứ: chọn tiêu chí, chấm theo bằng chứng, xử lý xung đột stakeholder, đề xuất thứ tự và lát cắt phát hành; dùng khi cần xếp backlog, chốt MVP, hoặc đánh giá lại ưu tiên khi có thay đổi."
---

# Requirements Prioritize

Khung theo BABOK v3 mục 5.3 (Prioritize Requirements) và 10.33 (Prioritization). Trả lời bằng ngôn ngữ người dùng (mặc định tiếng Việt). Skill **đề xuất và giải thích**, người dùng và stakeholder quyết định.

## Nguyên tắc
1. **Ưu tiên là đánh giá giá trị tương đối**, mỗi stakeholder có thể coi trọng cái khác nhau. Đưa xung đột ra, không giấu (BABOK 5.3.4.2).
2. **Thỏa thuận tiêu chí trước, chấm sau.** Cơ sở ưu tiên do stakeholder liên quan thống nhất (5.3.4.1).
3. **Không bịa số.** Điểm chấm phải kèm lý do/bằng chứng; chi phí lấy từ đội triển khai; nếu chưa có, ghi "chưa ước lượng".
4. **Ràng buộc luật/chính sách đi trước** các mong muốn khác; đừng chấm "trọng số" cho thứ bắt buộc (BABOK nêu tuân thủ quy định có thể ưu tiên hơn lợi ích stakeholder).
5. **Ưu tiên thay đổi theo thời gian**: ban đầu ở mức trừu tượng cao, sau đó chi tiết hơn; đội kỹ thuật có thể xếp lại theo thứ tự triển khai, và stakeholder lại điều chỉnh khi biết chi phí (5.3.4.3).
6. Chú ý thiên lệch: stakeholder có thể (cố ý hay vô ý) báo ưu tiên để ảnh hưởng kết quả; đội giải pháp có thể thổi phồng độ khó (10.33.4.2).

## Quy trình
1. Thu danh sách mục cần xếp (kèm mã) và bối cảnh: mục tiêu, giai đoạn, ràng buộc (hạn, ngân sách, quy định).
2. **Chọn và thống nhất tiêu chí** từ `references/criteria.md`; không dùng quá 4–5 tiêu chí cùng lúc.
3. **Tách nhóm bắt buộc** (tuân thủ luật, hợp đồng, phụ thuộc kỹ thuật bắt buộc) khỏi nhóm cần chấm.
4. **Chấm** theo `templates/prioritization-table.md`, mỗi điểm kèm lý do và nguồn thông tin.
5. **Kiểm tra phụ thuộc** (dùng quan hệ depends từ `requirements-trace`): mục ưu tiên cao nhưng phụ thuộc mục thấp thì điều chỉnh.
6. **Đề xuất thứ tự và lát cắt** (ví dụ phát hành 1/2/3 hoặc theo khung thời gian/ngân sách cố định, BABOK 10.33.3.3), nêu **trade-off**: được gì, mất gì.
7. Nêu **xung đột chưa giải quyết** và câu hỏi cần quyết định, ai quyết.
8. Ghi **ngày và cơ sở** của lần ưu tiên này để đánh giá lại khi đổi bối cảnh.

## Tệp tham chiếu
- `references/criteria.md`: tiêu chí, phương pháp, thiên lệch, backlog nhiều pha, yếu tố đánh giá thay đổi.
- `templates/prioritization-table.md`: mẫu bảng và báo cáo.
