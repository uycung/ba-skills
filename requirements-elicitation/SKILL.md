---
name: requirements-elicitation
description: "Lập kế hoạch khai thác yêu cầu, soạn bộ câu hỏi phỏng vấn/workshop, và biến ghi chép họp thành kết quả khai thác có nguồn, chưa xác nhận, kèm danh sách cần xác nhận; dùng trước khi viết story/FR hoặc sau mỗi buổi gặp stakeholder."
---

# Requirements Elicitation

Khung theo BABOK v3 chương 4 (Prepare, Conduct, Confirm) và kỹ thuật Interviews, Item Tracking. Trả lời bằng ngôn ngữ người dùng (mặc định tiếng Việt). Đầu ra của skill này là đầu vào cho `story-writer`, `nfr-writer`, `requirements-trace`.

## Nguyên tắc
1. **Ghi đúng cái được nói, tách khỏi cái suy ra.** Mỗi thông tin có nhãn: [Đã nói] (trích/ghi lại từ nguồn), [Suy luận] (mình rút ra), [Giả định]. Không biến suy luận thành sự thật.
2. **Kết quả khai thác luôn "chưa xác nhận" cho tới khi được xác nhận** với nguồn hoặc đối chiếu chéo (BABOK 4.2.8, 4.3).
3. **Không đặt câu hỏi dẫn dắt.** BABOK nêu rủi ro vô tình dẫn dắt người được phỏng vấn (10.25.4.2). Ưu tiên câu hỏi mở, hỏi ví dụ cụ thể và quy trình thật.
4. **Mọi mâu thuẫn và điểm mở được ghi lại và có chủ sở hữu**, không tự chọn bên đúng.
5. Giữ bảo mật khi người dùng yêu cầu ẩn danh nguồn.

## Ba chế độ
### A. Lập kế hoạch (Prepare)
Từ mục tiêu và bối cảnh người dùng đưa, tạo **Kế hoạch hoạt động khai thác** (`templates/elicitation-plan.md`): mục tiêu buổi, phạm vi (thông tin cần có, cái ngoài phạm vi), người tham gia và vai trò, kỹ thuật chọn (kèm lý do), hậu cần, tài liệu cần đọc trước, rủi ro. Chọn kỹ thuật theo `references/techniques.md`.
### B. Soạn câu hỏi
Tạo **hướng dẫn phỏng vấn/workshop**: mở đầu, nhóm câu hỏi theo chủ đề (kèm câu hỏi đào sâu), đóng buổi. Cho phép đánh dấu câu nào có thể bỏ nếu thiếu thời gian (BABOK 10.25.3). Với workshop: thêm chương trình, vai trò (facilitator, scribe, timekeeper), luật chơi và đầu ra xác định (10.50). Với khảo sát: mục tiêu, mẫu, ngưỡng phản hồi, chạy thử (10.45). Chi tiết ở `references/workshops-surveys.md`.
### C. Xử lý ghi chép (Conduct → Confirm)
Nhận ghi chép/transcript. Trả:
1. **Kết quả khai thác (chưa xác nhận)**: bảng mục | loại (nhu cầu, quy tắc, ràng buộc, vấn đề, giả định, câu hỏi mở) | nội dung | nhãn [Đã nói]/[Suy luận] | nguồn (ai, khi nào).
2. **Mâu thuẫn và thiếu sót** so với ghi chép/tài liệu trước (nếu có).
3. **Danh sách cần xác nhận**: mục nào, hỏi ai, hỏi gì. Soạn sẵn tin nhắn/email theo dõi ngắn để gửi người tham gia (BABOK nhấn mạnh xác nhận sớm sau buổi gặp).
4. **Mục theo dõi (Item Tracking)** cho vấn đề/giả định/phụ thuộc: xem `references/item-tracking.md`.
5. **Thuật ngữ mới hoặc khác nghĩa** xuất hiện trong buổi (BABOK 10.23), để đưa vào glossary.
6. **Ứng viên yêu cầu**: các mục có thể thành story/FR/NFR/BR, chưa viết hoàn chỉnh; chuyển sang skill tương ứng.

## Tệp tham chiếu
- `references/techniques.md`: chọn kỹ thuật, ba kiểu khai thác.
- `references/item-tracking.md`: thuộc tính mục theo dõi.
- `references/workshops-surveys.md`: workshop, khảo sát, trò chơi cộng tác, thuật ngữ, giao diện, xác nhận/truyền đạt.
- `templates/elicitation-plan.md`: mẫu kế hoạch và hướng dẫn phỏng vấn.
