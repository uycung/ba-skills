---
name: requirements-testcases
description: "Sinh và rà soát test case, kịch bản UAT và gói nghiệm thu từ acceptance criteria, quy tắc nghiệp vụ, bảng quyết định, mô hình trạng thái và NFR của BA; dùng khi cần biến yêu cầu đã có thành bộ kiểm thử truy vết được hoặc kiểm độ phủ test so với yêu cầu."
---

# Requirements Test Cases and UAT

Mục tiêu: mọi yêu cầu đã chốt có ít nhất một cách **kiểm chứng đúng/sai**, và mọi test trỏ ngược được về yêu cầu. Trả lời bằng ngôn ngữ người dùng (mặc định tiếng Việt).

## Nguồn và giới hạn (nói thẳng với người dùng khi liên quan)
- **Thuộc BABOK v3**: tiêu chí chấp nhận phải viết ở dạng kiểm chứng đúng/sai, có thể phải tách yêu cầu nhỏ đến mức viết được test case, và thường được xác nhận qua user acceptance testing (10.1); quan hệ *Validate* giữa yêu cầu và test case trong truy vết (5.1.4.2); tester là stakeholder cần hiểu yêu cầu để lập test plan và test case (5.1, 5.2).
- **Thuộc Agile Extension v2**: BDD, ví dụ cụ thể, cú pháp Given-When-Then với đúng một WHEN, "Three Amigos" (PO, tester, dev), hỏi "what if" để lộ kịch bản thiếu; BDD, ATDD và Specification by Example thường dùng thay nhau (7.2).
- **Thuộc ISTQB CTFL v4.0.1** (đã đối chiếu với bản PDF 78 trang, ngày 2024-09-15, diễn giải lại, không chép nguyên văn): phân vùng tương đương (4.2.1), giá trị biên 2 giá trị và 3 giá trị (4.2.2), bảng quyết định (4.2.3), chuyển trạng thái (4.2.4), các hình thức kiểm thử chấp nhận gồm UAT, vận hành, hợp đồng, quy định, alpha, beta (2.2.1), tiêu chí chấp nhận dạng kịch bản hoặc dạng quy tắc và ATDD (4.5.2, 4.5.3), đoán lỗi, khám phá, theo checklist (4.4). Chi tiết ở `references/derivation.md` và `references/uat.md`.
- **Thuộc ISO/IEC/IEEE 29148:2018** (bản chuẩn đã đọc, điều 6.5.2.2): bốn phương pháp xác minh yêu cầu là inspection, analysis (gồm mô hình hóa, mô phỏng), demonstration và test. Test case chỉ là một trong bốn; khi yêu cầu nên xác minh bằng cách khác (ví dụ kiểm tra tài liệu, trình diễn), ghi cột "Phương pháp xác minh" thay vì ép viết test.
- **KHÔNG thuộc BABOK**: kỹ thuật thiết kế test. BABOK không dạy thiết kế test case; không trích số mục BABOK cho phần này, trích ISTQB.
- **Khái niệm có trong ISTQB, nội dung cụ thể là đề xuất của skill**: tiêu chí vào/ra (5.1.3: tiêu chí vào là điều kiện tiên quyết để bắt đầu hoạt động, tiêu chí ra là điều phải đạt để coi hoạt động hoàn tất; trong agile tương ứng Definition of Ready và Definition of Done). Các mục cụ thể trong gói UAT là đề xuất, không phải nội dung ISTQB.
- **Vẫn là quy ước của skill, không có nguồn chuẩn**: mức độ ưu tiên test, mẫu báo cáo lỗi, tổ hợp cặp (pairwise; không nằm trong mục 4.2 đã đọc). Chỉ ISTQB CTFL (mức Foundation) được đối chiếu; các cấp cao hơn và chuẩn ISO/IEC/IEEE 29119 chưa đọc.
- Skill không chạy test và không thay QA. Nó tạo thiết kế test ở mức BA (điều cần kiểm và kết quả mong đợi theo yêu cầu); QA bổ sung dữ liệu, kịch bản kỹ thuật, tự động hóa.

## Nguyên tắc cứng
1. **Kết quả mong đợi lấy từ yêu cầu, không tự nghĩ ra.** Mỗi test trỏ đúng ID nguồn (AC, BR, NFR, quy tắc trong bảng quyết định, chuyển trạng thái). Không có nguồn: không viết test, đưa vào danh sách "Chưa đủ để viết test".
2. **AC không kiểm chứng được thì trả lại, không viết test đoán.** Từ mơ hồ ("nhanh", "thân thiện") hoặc thiếu giá trị cụ thể: ghi câu hỏi và chuyển `story-writer` / `nfr-writer`.
3. **Mỗi test một ý chính**, một kết quả kiểm chứng được bằng quan sát. Kịch bản BDD: đúng một WHEN (Agile Extension 7.2.3.2).
4. **Phủ cả đường không vui**: ngoại lệ, giá trị biên, dữ liệu sai, thiếu quyền, trạng thái không hợp lệ. Mỗi quy tắc có ngưỡng thì có test ở hai phía ngưỡng.
5. **Dữ liệu mẫu là giả định, ghi nhãn.** Không dùng dữ liệu cá nhân thật; dữ liệu nhạy cảm dùng giá trị giả.
6. **Báo độ phủ trung thực**: nói rõ yêu cầu nào chưa có test, test nào không truy được nguồn, phần nào skill không thể thiết kế (cần môi trường, dữ liệu thật, hệ thống ngoài).
7. UAT do **người nghiệp vụ** thực hiện bằng ngôn ngữ nghiệp vụ; không viết UAT như script kỹ thuật.

## Chế độ
- **A. Sinh test từ yêu cầu**: nhận story/AC/BR/bảng quyết định/mô hình trạng thái/NFR; trả bộ test case + ma trận phủ + danh sách "Chưa đủ để viết test".
- **B. Rà soát bộ test có sẵn**: đối chiếu với yêu cầu, tìm yêu cầu chưa có test, test mồ côi, kết quả mong đợi mâu thuẫn yêu cầu, test thiếu ca biên (dùng `references/test-quality.md`).
- **C. Kế hoạch và gói UAT**: kịch bản nghiệp vụ, vai trò thực hiện, dữ liệu, tiêu chí vào/ra, mẫu ghi nhận, cách ra quyết định chấp nhận (`references/uat.md`).
- **D. Chọn test hồi quy sau thay đổi**: từ danh sách yêu cầu bị ảnh hưởng (kết quả phân tích tác động của `requirements-trace`) chọn test cần chạy lại.

## Quy trình (chế độ A)
1. Kiểm đầu vào: mỗi yêu cầu có ID, AC kiểm chứng được, quy tắc có giá trị cụ thể. Liệt kê thiếu sót trước, không chặn phần đã đủ.
2. Chọn cách suy ra test theo loại nguồn (`references/derivation.md`).
3. Viết test theo `templates/test-case-template.md`; đặt ID TC-xx, trỏ nguồn, loại (Chuẩn / Ngoại lệ / Biên / Sai dữ liệu / Quyền / Trạng thái / NFR).
4. Lập ma trận phủ nguồn × test; đánh dấu ô trống. Chuyển cho `requirements-trace` nếu cần nối vào ma trận truy vết chung.
5. Tự kiểm bằng `references/test-quality.md`.
6. Cuối bản trả luôn có: **Giả định**, **Cần làm rõ**, **Chưa đủ để viết test**, **Giới hạn (cái cần QA bổ sung)**.

## Phối hợp
Story/AC mơ hồ: `story-writer`. NFR thiếu số đo: `nfr-writer`. Ma trận truy vết và tác động thay đổi: `requirements-trace`. Rà soát bộ yêu cầu trước khi viết test: `requirements-review`. Mô hình trạng thái/bảng quyết định làm nguồn test: `requirements-modelling`.

## Tệp tham chiếu
- `references/derivation.md`: suy ra test từ từng loại nguồn (AC, BR, bảng quyết định, trạng thái, use case, NFR, dữ liệu).
- `references/uat.md`: UAT, tiêu chí vào/ra, kịch bản nghiệp vụ, ra quyết định chấp nhận.
- `references/test-quality.md`: kiểm chất lượng test và độ phủ.
- `templates/test-case-template.md`: mẫu test case, ma trận phủ, ví dụ.
