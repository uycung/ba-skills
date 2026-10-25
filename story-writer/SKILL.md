---
name: story-writer
description: "Viết và rà soát yêu cầu chức năng (FR), user story, acceptance criteria và use case cho BA; dùng khi cần biến ý tưởng/yêu cầu thô thành story rõ ràng, kiểm chứng được, hoặc chấm chất lượng story/FR đã có."
---

# Story Writer (FR, User Story, Acceptance Criteria, Use Case)

Mục tiêu: đầu ra **đọc là hiểu, test là kiểm chứng được**. Nhiệm vụ chính là viết rõ, không phải điền khuôn. Trả lời bằng ngôn ngữ người dùng đang dùng (mặc định tiếng Việt).

## Nguyên tắc cứng
1. **Không bịa nghiệp vụ.** Chỗ nào thiếu thông tin (quy tắc, số, vai trò, ngoại lệ) thì ghi thành câu hỏi trong mục "Cần làm rõ", không tự điền cho đẹp.
2. **Một story = một giá trị, một người dùng, một lát cắt dọc có thể giao được.** Nếu hai "và" trong phần "tôi muốn", tách ra.
3. **Mỗi AC phải kiểm chứng được đúng/sai** (BABOK 10.1: viết ở dạng nguyên tử để có test case) bằng cách quan sát: có đầu vào, hành động, kết quả cụ thể. Cấm từ mơ hồ không kèm tiêu chí: nhanh, dễ dùng, thân thiện, phù hợp, đầy đủ, thông minh, v.v. (xem `references/quality-checks.md`).
4. **Quy tắc nghiệp vụ tách khỏi bước thao tác**: ghi riêng thành bảng BR-xx, phân loại định nghĩa/hành vi, hỏi mức thực thi; story/use case chỉ dẫn chiếu tới (BABOK 10.47.4, 10.9; xem `references/business-rules.md`).
5. **Phi chức năng không nhét vào AC chức năng.** Phát hiện NFR thì ghi mã tạm và chuyển cho skill `nfr-writer`.
6. Giữ thuật ngữ nhất quán với glossary người dùng cung cấp; chưa có thì lập glossary ngắn.

## Quy trình viết
1. Xác định: ai (vai trò cụ thể, không phải "người dùng" chung chung), mục tiêu, giá trị, phạm vi (trong/ngoài).
2. Nếu đầu vào mơ hồ, hỏi tối đa 4 câu quan trọng nhất; nếu người dùng không trả lời, viết bản nháp với giả định ghi rõ.
3. Chọn dạng: story + AC (mặc định); job story khi bối cảnh và động cơ quan trọng hơn vai trò; use case khi luồng nhiều bước, nhiều tác nhân, nhiều ngoại lệ; bảng quyết định khi có tổ hợp điều kiện.
4. Viết theo `templates/story-template.md`.
4b. Story chưa tới lượt (cuối backlog): chỉ viết bản sơ bộ, ghi rõ chưa có AC đầy đủ (xem `references/agile-context.md`).
5. **Tự kiểm** theo `references/quality-checks.md` trước khi trả: dò lỗi từng AC, kiểm INVEST, kiểm các ca biên.
6. Cuối bản trả luôn có: **Giả định**, **Cần làm rõ**, **NFR phát hiện** (nếu có).

## Chế độ rà soát
Nhận story/FR có sẵn. Trả bảng: mục | vấn đề | vì sao là vấn đề | cách viết lại. Sau đó đưa bản viết lại đầy đủ. Không chê chung chung; mỗi nhận xét trỏ đúng câu bị lỗi.

## Tệp tham chiếu
- `references/quality-checks.md`: tiêu chí chất lượng (BABOK + INVEST từ Agile Extension), danh sách lỗi và cách sửa.
- `references/ac-patterns.md`: cách viết AC (quy tắc/Given-When-Then), ca biên cần dò, use case.
- `references/business-rules.md`: viết và phân loại quy tắc nghiệp vụ (BABOK 10.9).
- `references/agile-context.md`: phân rã, elaborate, backlog, job story, BDD, story map (BABOK 10.2; Agile Extension v2 7.1–7.4, 7.18–7.21).
- `templates/story-template.md`: mẫu và ví dụ trước/sau.
