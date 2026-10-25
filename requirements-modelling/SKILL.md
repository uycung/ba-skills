---
name: requirements-modelling
description: "Chọn và dựng mô hình yêu cầu cho BA: quy trình (as-is/to-be), trạng thái của thực thể, dữ liệu và từ điển dữ liệu, bảng quyết định, use case, phạm vi, phân rã chức năng, giao diện, ma trận vai trò và quyền; dùng khi mô tả bằng chữ không đủ rõ hoặc khi cần kiểm tra tính đầy đủ của một luồng, vòng đời, bộ quy tắc."
---

# Requirements Modelling

Khung theo BABOK v3 mục 7.1 (Specify and Model Requirements) và các kỹ thuật 10.11, 10.12, 10.15, 10.17, 10.22, 10.24, 10.35, 10.39, 10.41, 10.44, 10.47. Trả lời bằng ngôn ngữ người dùng (mặc định tiếng Việt). Mô hình là phương tiện để **hiểu, giao tiếp và lộ chỗ thiếu**, không phải mục đích (7.1.4.1: mô hình giúp xác nhận hiểu biết, tìm khoảng trống thông tin và thông tin trùng).

## Nguyên tắc cứng
1. **Chọn mô hình theo câu hỏi cần trả lời**, không vẽ mọi thứ. Bắt đầu bằng việc hỏi: người xem là ai, họ cần hiểu hoặc quyết định điều gì (`references/model-selection.md`).
2. **Không bịa phần tử.** Chỉ đưa vào mô hình thứ có trong tài liệu hoặc lời người dùng. Chỗ thiếu thì ghi "?" trong mô hình và liệt kê trong **câu hỏi mở**; phần suy ra gắn nhãn [Suy luận], phần giả định [Giả định].
3. **Mỗi mô hình kèm**: mục đích, đối tượng đọc, phạm vi (trong/ngoài), mức trừu tượng, phần tử chưa xác nhận, câu hỏi mở. Mô hình không có phạm vi thì không ai biết đã đủ chưa.
4. **Giữ nghĩa nhất quán qua các biểu diễn** (7.1.4.4): cùng một thực thể, trạng thái, vai trò phải có cùng tên ở mô hình quy trình, dữ liệu, trạng thái, story, quy tắc. Dùng glossary của người dùng; chưa có thì lập glossary ngắn.
5. **Tách quy tắc khỏi mô hình**: điều kiện và ngưỡng nằm ở bảng quy tắc (BR-xx), mô hình dẫn chiếu mã (BABOK 10.9). Quyết định nhiều điều kiện dùng bảng quyết định thay vì nhồi vào lưới nhánh.
6. **Mức khái niệm trước.** Mô hình dữ liệu logic/vật lý (chuẩn hóa, khóa ngoại, chỉ mục) thuộc về người triển khai; BA dừng ở mô hình khái niệm trừ khi người dùng yêu cầu (10.15.2).
7. Đầu ra mặc định là **mô tả bằng bảng/văn bản kèm sơ đồ Mermaid** để dán được ở mọi nơi. Mermaid chỉ là công cụ vẽ nhanh, không phải ký hiệu BABOK; nếu đội dùng BPMN/UML/công cụ riêng, đưa bảng và danh sách phần tử để họ vẽ lại.

## Quy trình
1. **Xác định mục đích mô hình**: hiểu hiện trạng (as-is), thống nhất tương lai (to-be), kiểm tra đầy đủ, chuẩn bị story/test, hoặc giao cho dev. Hỏi tối đa 3 câu thiếu nhất.
2. **Chọn loại mô hình** theo `references/model-selection.md`; có thể cần hai ba loại bổ trợ nhau (mô hình quy trình cho luồng, mô hình trạng thái cho vòng đời một thực thể, bảng quyết định cho một quyết định).
3. **Dựng bản nháp** theo file tham chiếu tương ứng; bắt đầu từ mức cao rồi chia dần mức chi tiết (process 10.35.2, decomposition 10.22).
4. **Tự kiểm** theo mục "Kiểm tra" trong file tham chiếu: đầy đủ trong mô hình, kiểm chéo với mô hình khác (xem `requirements-review`).
5. **Trả**: mô hình, câu hỏi mở, giả định, danh sách quy tắc BR cần tách, và các story/NFR có thể phát sinh (chuyển `story-writer`, `nfr-writer`).

## Phối hợp
Từ ghi chép họp: `requirements-elicitation` trước. Viết story/AC từ mô hình: `story-writer`. Kiểm mô hình: `requirements-review`. Nối mô hình với yêu cầu: `requirements-trace`.

## Tệp tham chiếu
- `references/model-selection.md`: bảng chọn mô hình, các nhóm mô hình, mức trừu tượng.
- `references/process-state.md`: mô hình quy trình, mô hình trạng thái, bảng trạng thái.
- `references/data-models.md`: mô hình khái niệm, mô hình dữ liệu, từ điển dữ liệu.
- `references/decision-usecase.md`: bảng quyết định, cây, DRD; use case và kịch bản.
- `references/scope-roles-interfaces.md`: phạm vi, phân rã chức năng, giao diện, ma trận vai trò và quyền.
- `templates/model-examples.md`: ví dụ từng loại (tự soạn, đã kiểm cú pháp Mermaid).
