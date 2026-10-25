---
name: business-case-strategy
description: "Phân tích chiến lược cho BA: hiện trạng, trạng thái tương lai và mục tiêu SMART, phân tích khoảng cách, rủi ro, chiến lược thay đổi, business case và phân tích tài chính (chi phí lợi ích, ROI, NPV, IRR), SWOT, nguyên nhân gốc, KPI; dùng khi cần biện minh hoặc chọn hướng thay đổi trước khi đi vào yêu cầu chi tiết."
---

# Business Case and Strategy

Theo BABOK v3 chương 6 (Strategy Analysis: 6.1–6.4), 10.7 (Business Cases), 10.20 (Financial Analysis), 10.38 (Risk Analysis and Management), 10.46 (SWOT), 10.40 (Root Cause Analysis), 10.28 (Metrics and KPIs) và chương 8 (đo giá trị sau triển khai). Trả lời bằng ngôn ngữ người dùng (mặc định tiếng Việt). Đây là mức **vì sao và chọn hướng nào**; yêu cầu chi tiết thuộc các skill khác.

## Nguyên tắc cứng
1. **Không bịa số.** Mọi số tiền, tỉ lệ, thời gian, tỉ lệ chiết khấu, quy mô thị trường phải do người dùng cung cấp hoặc có nguồn đọc được; gắn nhãn [Đã nói] / [Nguồn: …] / [Giả định, cần xác nhận]. Chỗ thiếu: nêu câu hỏi, không điền để bảng "đủ". BABOK yêu cầu giả định và phương pháp ước tính phải nêu rõ để người khác rà soát và thách thức (10.20).
2. **Tính toán bằng mã, không tính nhẩm.** Dùng `scripts/fin.py` cho ROI, NPV, IRR, hoàn vốn; kiểm lại một con số bằng tay. Không đưa kết quả không chạy.
3. **Đây là phân tích, không phải lời khuyên đầu tư.** Trình bày dữ kiện, giả định, độ nhạy và rủi ro để người ra quyết định tự cân nhắc; nói rõ bạn không phải cố vấn tài chính/pháp lý. Tỉ lệ chiết khấu và ngưỡng hurdle do bộ phận tài chính của tổ chức quy định (BABOK nêu tổ chức thường có tỉ lệ chuẩn do giám đốc tài chính xác định); không tự chọn.
4. **Nhu cầu nêu từ góc nhìn tổ chức, độc lập với giải pháp.** Nhu cầu thường được nêu kèm giải pháp định sẵn; hỏi lại giả định và ràng buộc để giải đúng vấn đề và giữ khoảng rộng các phương án (6.1). Kết quả mong muốn của business case cũng phải độc lập với giải pháp được đề xuất (10.7).
5. **Luôn có phương án "không làm gì"** và tính nó trong so sánh (10.7). So sánh các phương án trên cùng một khoảng thời gian (10.20).
6. **Mục tiêu phải đo được** (SMART; 6.2). Mục tiêu định tính chuyển thành mục tiêu cụ thể gắn chỉ số, hoặc ghi rõ "chưa đo được" và nêu cách đo.
7. **Nói rõ cái gì không định lượng được.** Lợi ích phi tài chính (uy tín, tuân thủ, linh hoạt) vẫn ghi, gắn với mục tiêu chiến lược, không ép thành tiền nếu không có cơ sở (10.7, 10.20).
8. **Phân biệt dữ kiện, ý kiến, giả định** trong SWOT, phân tích nguyên nhân gốc, đánh giá thái độ. Nguyên nhân tìm được bằng fishbone/5-why mới là nguyên nhân tiềm năng cho đến khi kiểm bằng dữ liệu (10.40).
9. **Giới hạn số mục đã đọc** nêu ở cuối file này; không trích mục chưa đọc.

## Quy trình tổng
1. **Làm rõ nhu cầu** (`references/current-future-state.md`): vấn đề/cơ hội, ai chịu ảnh hưởng, chi phí của việc không làm gì.
2. **Hiện trạng** vừa đủ để xác nhận nhu cầu và chiến lược (6.1): tổ chức và văn hóa, năng lực và quy trình, công nghệ, chính sách, tài sản, ảnh hưởng bên ngoài.
3. **Tương lai** (6.2): mục tiêu SMART, phạm vi không gian giải pháp, ràng buộc, giả định, giá trị tiềm năng.
4. **Khoảng cách** hiện trạng ↔ tương lai (6.4.4.2) và **mức sẵn sàng** của tổ chức (6.4.4.3).
5. **Rủi ro** (6.3, 10.38) và khẩu vị rủi ro.
6. **Phương án và chiến lược thay đổi** (6.4): nhiều phương án, tiêu chí chọn, giai đoạn chuyển tiếp.
7. **Business case** (10.7) và **phân tích tài chính** (10.20): `references/business-case-financial.md`.
8. **Chỉ số** (10.28) để theo dõi giá trị sau triển khai (chương 8).
9. **Trả**: tài liệu theo `templates/business-case-template.md` + câu hỏi mở + giả định + việc kế tiếp (nối `requirements-stakeholders`, `requirements-elicitation`, `requirements-document`).

## Chế độ
- **Business case đầy đủ** từ mô tả vấn đề và dữ liệu có sẵn.
- **Phân tích nhanh một phần**: chỉ hiện trạng/khoảng cách, hoặc SWOT, hoặc nguyên nhân gốc, hoặc chỉ số.
- **Rà soát business case có sẵn**: dò nhu cầu nêu kèm giải pháp, thiếu "không làm gì", giả định không nêu, số không nguồn, mục tiêu không đo được, rủi ro không có người theo dõi, thời gian so sánh không đồng nhất.
- **Tính tài chính** từ bảng chi phí-lợi ích người dùng đưa.

## Tệp tham chiếu
- `references/current-future-state.md`: nhu cầu, hiện trạng, tương lai, mục tiêu SMART, ảnh hưởng bên ngoài.
- `references/gap-risk-strategy.md`: khoảng cách, sẵn sàng, rủi ro, phương án, chiến lược và giai đoạn chuyển tiếp.
- `references/business-case-financial.md`: cấu trúc business case, TCO, chi phí lợi ích, ROI, NPV, IRR, hoàn vốn, giới hạn.
- `references/analysis-techniques.md`: SWOT, nguyên nhân gốc, KPI, đo sau triển khai.
- `templates/business-case-template.md`: mẫu và bảng tính.
- `scripts/fin.py`: tính tài chính (dùng `python3 scripts/fin.py input.json`).

## Phần BABOK chưa đọc (nói thẳng nếu liên quan)
Chưa đọc: Business Capability Analysis (10.6), Business Model Canvas (10.8), Balanced Scorecard (10.3), Benchmarking and Market Analysis (10.4; chỉ biết tên các khung 5 Forces, PEST, STEEP, CATWOE qua mục 6.1), Vendor Assessment (10.49), chương 8.3 và 8.4 (giới hạn giải pháp, giới hạn tổ chức). Decision Analysis (10.16) chỉ đọc một phần. Tài liệu nguồn không có tiêu chuẩn thẩm định đầu tư hay chuẩn kế toán; tỉ lệ chiết khấu và ngưỡng do tổ chức quy định.
