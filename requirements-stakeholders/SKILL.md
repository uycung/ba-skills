---
name: requirements-stakeholders
description: "Phân tích stakeholder cho BA: lập danh sách, bản đồ (ma trận ảnh hưởng, onion), RACI, persona, kế hoạch cộng tác và truyền thông, rủi ro từ stakeholder; dùng đầu dự án hoặc khi bắt đầu một đợt khai thác để biết ai cần gặp, gặp thế nào, ai quyết định."
---

# Requirements Stakeholders

Theo BABOK v3 mục 3.2 (Plan Stakeholder Engagement), 10.43 (Stakeholder List, Map, or Personas) và Agile Extension v2 mục 7.7 (Personas). Trả lời bằng ngôn ngữ người dùng (mặc định tiếng Việt). Phân tích stakeholder là việc lặp lại; vị trí của một stakeholder thay đổi theo phạm vi và bối cảnh (10.43.3).

## Nguyên tắc cứng
1. **Không bịa người, vai trò, thái độ hay quyền.** Chỉ đưa vào danh sách người/nhóm có trong tài liệu hoặc lời người dùng. Thuộc tính chưa biết ghi "?" kèm cách tìm hiểu (hỏi ai, xem tài liệu nào).
2. **Phân biệt dữ kiện và suy đoán.** Mỗi thuộc tính gắn nhãn: [Đã nói] (người dùng/tài liệu nói rõ), [Suy luận] (từ vai trò, chức danh, hành vi đã kể), [Giả định]. Nhận định về thái độ và ảnh hưởng là phán đoán, luôn là [Suy luận] trừ khi chính người đó hoặc người có thẩm quyền xác nhận.
3. **Nhạy cảm về chính trị và riêng tư** (BABOK 10.43.4 nêu: đánh giá ảnh hưởng và quan tâm của từng đại diện có thể phức tạp và rủi ro chính trị). Phân tích có đánh giá cá nhân (thái độ, ảnh hưởng) chỉ dùng trong nhóm BA; nhắc người dùng đừng đưa bản có nhận định về cá nhân vào tài liệu chia sẻ rộng. Mặc định đánh giá theo vai trò/nhóm, không bình phẩm tính cách.
4. **Chỉ một người Accountable cho mỗi việc** trong RACI (10.43.3.3). Việc có hai A: hỏi lại, không chia đôi.
5. **Persona phải dựa trên nghiên cứu, không phải ý kiến** (10.43.3.4). Persona không có dữ liệu nghiên cứu bắt buộc gắn nhãn "Giả thuyết, chưa kiểm chứng" và liệt kê cách kiểm chứng (phỏng vấn, khảo sát). Không bịa chi tiết cá nhân như tuổi, gia đình để cho giống thật.
6. **Cái gì cũng truy được nguồn**: danh sách gắn nguồn (sơ đồ tổ chức, hợp đồng, sponsor, cuộc họp). Không có nguồn: "cần xác nhận".

## Quy trình
1. **Xác định phạm vi phân tích**: thay đổi/sáng kiến nào, ranh giới trong/ngoài (dùng mô hình phạm vi nếu có).
2. **Lập danh sách** (`references/analysis.md` mục 1): tìm nguồn nội bộ (sơ đồ tổ chức, quy trình), nguồn ngoài (hợp đồng, nhà cung cấp, cơ quan quản lý, khách hàng), vai trò chuẩn của BABOK để dò sót.
3. **Phân tích đặc điểm**: vai trò, thái độ, quyền ra quyết định, mức ảnh hưởng/quan tâm.
4. **Dựng bản đồ**: ma trận (ảnh hưởng × quan tâm/tác động), onion, RACI cho các hoạt động chính (`references/maps-raci-persona.md`).
5. **Lập kế hoạch cộng tác và truyền thông** (`references/engagement-plans.md`).
6. **Nêu rủi ro từ stakeholder**: người then chốt khó tham gia, thái độ tiêu cực, khoảng cách giữa ảnh hưởng cần và ảnh hưởng có; đề xuất ghi vào sổ rủi ro; gợi ý cho `business-case-strategy` nếu có đánh giá rủi ro tổng.
7. **Trả**: danh sách + bản đồ + kế hoạch + câu hỏi mở. Nếu đang chuẩn bị khai thác, nối sang `requirements-elicitation` (ai phỏng vấn, ai dự workshop).

## Chế độ
- **Lập mới** từ mô tả dự án/tài liệu.
- **Cập nhật** từ ghi chép họp hoặc thay đổi tổ chức (chỉ sửa phần bị tác động, ghi lịch sử thay đổi).
- **Rà soát** một bản có sẵn: dò sót nhóm, thuộc tính thiếu, RACI có 0 hoặc 2 A, kế hoạch không khớp bản đồ.
- **Persona**: tạo persona từ dữ liệu nghiên cứu người dùng cung cấp.

## Phối hợp
Từ danh sách đến lịch khai thác: `requirements-elicitation`. RACI cho nghiệm thu UAT: `requirements-testcases`. Ma trận quyền ở cấp hệ thống (CRUD): `requirements-modelling`. Rủi ro và chiến lược thay đổi: `business-case-strategy`.

## Tệp tham chiếu
- `references/analysis.md`: danh sách, vai trò chuẩn, đặc điểm cần phân tích, tìm nguồn.
- `references/maps-raci-persona.md`: ma trận, onion, RACI, persona.
- `references/engagement-plans.md`: kế hoạch cộng tác, truyền thông, rủi ro stakeholder.
- `templates/stakeholder-register.md`: bảng đăng ký mẫu và ví dụ.
