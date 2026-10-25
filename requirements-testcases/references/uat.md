# UAT và gói nghiệm thu

## Cơ sở
- Tiêu chí chấp nhận là điều kiện tối thiểu để giải pháp đáng triển khai, thường đánh giá đạt/không đạt; thường được kiểm bằng user acceptance testing (BABOK 10.1). Tiêu chí chấp nhận có thể viết thành mức hiệu năng tối thiểu và chi phí tối đa trong hợp đồng và UAT.
- Tiêu chí dựa trên thuộc tính giá trị (value attributes) để đảm bảo liên quan đến nhu cầu stakeholder; định nghĩa các thuộc tính phải được mọi stakeholder đồng ý (10.1).
- Trong agile, scenario BDD đóng vai tiêu chí chấp nhận cho story (Agile Extension 7.2); phiên "Three Amigos" giữa PO, tester, dev làm rõ trước khi làm.
- ISTQB CTFL v4.0.1, 2.2.1: kiểm thử chấp nhận tập trung vào xác nhận (validation) và chứng minh sẵn sàng triển khai, lý tưởng do người dùng dự kiến thực hiện. Các hình thức chính: **UAT**, **vận hành** (operational), **hợp đồng** (contractual), **quy định** (regulatory), **alpha**, **beta**. Khi lập kế hoạch, hỏi rõ gói này là hình thức nào; hợp đồng và quy định thường có tiêu chí do hợp đồng/quy định đặt, không phải do skill đề xuất.
- ISTQB 5.1.3: tiêu chí vào là điều kiện tiên quyết để bắt đầu hoạt động, tiêu chí ra là điều phải đạt để coi là hoàn tất; nên định nghĩa cho từng mức kiểm thử. Ví dụ tiêu chí ra ISTQB nêu gồm thước đo mức kỹ lưỡng (độ phủ, số lỗi chưa xử lý) và tiêu chí có/không. Hết thời gian hoặc ngân sách cũng có thể là tiêu chí ra nếu stakeholder đã xem xét và chấp nhận rủi ro. Trong agile: Definition of Done (tiêu chí ra) và Definition of Ready (tiêu chí vào).
- **Các mục cụ thể trong gói UAT bên dưới là quy ước và đề xuất của skill, không phải BABOK hay ISTQB.**

## Khác nhau giữa test của QA và UAT
| | Test của QA | UAT |
|---|---|---|
| Người thực hiện | QA / dev | Người dùng nghiệp vụ, đại diện stakeholder |
| Ngôn ngữ | Kỹ thuật được | Ngôn ngữ nghiệp vụ |
| Phủ | Từng yêu cầu, ca biên, âm tính | Kịch bản nghiệp vụ đầu-cuối có giá trị |
| Câu hỏi | Chạy đúng spec chưa | Dùng được cho công việc thật chưa |

## Gói UAT (đầu ra mặc định ở chế độ C)
1. **Phạm vi**: yêu cầu/story nào, môi trường, ngoài phạm vi.
2. **Kịch bản nghiệp vụ**: mỗi kịch bản là một việc người dùng thật làm đầu-cuối ("Lễ tân đặt lịch cho khách quen và gửi nhắc"), nối nhiều story; kèm vai trò thực hiện, dữ liệu mẫu, kết quả mong đợi theo AC.
3. **Người tham gia và vai trò**: ai chạy, ai quan sát, ai quyết định chấp nhận (theo `requirements-stakeholders` / RACI: một người Accountable).
4. **Dữ liệu và môi trường**: dữ liệu giả, tài khoản theo vai trò, trạng thái khởi đầu cần dựng.
5. **Tiêu chí vào** (đề xuất): các story cần có đã qua test của QA; không còn lỗi mức chặn đã biết; môi trường và dữ liệu sẵn sàng; người dùng đã được hướng dẫn.
6. **Tiêu chí ra** (đề xuất, cần được sponsor/PO chốt): tỉ lệ kịch bản đạt tối thiểu, không còn lỗi mức chặn, lỗi còn lại có phương án xử lý và người chịu trách nhiệm. **Không tự điền con số**; ghi "cần chốt".
7. **Ghi nhận**: mỗi kịch bản có kết quả Đạt/Không đạt/Bị chặn, bằng chứng, ghi chú, người ghi, ngày.
8. **Quyết định chấp nhận**: ai ký, theo điều kiện nào; chấp nhận có điều kiện ghi rõ lỗi chấp nhận kèm hạn xử lý. Nếu không có đồng thuận hoàn toàn thì quản lý rủi ro còn lại (tinh thần BABOK 5.5).

## Kịch bản UAT: cách viết
- Tiêu đề là việc nghiệp vụ, không phải tên màn hình.
- Bước ở mức hành động nghiệp vụ; kết quả mong đợi quan sát được bởi người dùng.
- Mỗi kịch bản liệt kê story/AC mà nó chứng minh (để truy vết).
- Chừa ô "Nhận xét về mức dùng được" cho tiêu chí định tính; đừng biến định tính thành đạt/không đạt nếu AC không nói vậy.

## Rủi ro thường gặp (nêu với người dùng khi lập kế hoạch)
- UAT bị dùng như test hệ thống vì QA chưa đủ: tiêu chí vào để chặn.
- Người dùng nghiệp vụ không có thời gian: lên lịch sớm, ghi vào kế hoạch stakeholder.
- Yêu cầu đổi sau khi viết UAT: dùng phân tích tác động của `requirements-trace` để cập nhật kịch bản.
