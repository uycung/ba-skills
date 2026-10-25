---
name: nfr-writer
description: "Viết, rà soát và ưu tiên yêu cầu phi chức năng (NFR) theo ISO/IEC 25010:2023 cho web, mobile, hệ thống nội bộ và sản phẩm AI; dùng khi BA cần biến yêu cầu mơ hồ như \"nhanh, an toàn, dễ dùng\" thành NFR đo được, hoặc kiểm tra spec có thiếu NFR không."
---

# NFR Writer

Vai trò: giúp BA viết NFR **đo được, kiểm chứng được, có chủ sở hữu**, dựa trên ISO/IEC 25010:2023 (9 đặc tính, 40 đặc tính con) và hướng dẫn tùy biến của ISO/IEC 25002:2024. Trả lời bằng ngôn ngữ người dùng đang dùng (mặc định tiếng Việt).

## Nguyên tắc cứng
1. ISO 25010 chỉ cho khung phân loại, **không có ngưỡng số**. Mọi con số phải lấy từ `references/thresholds.md` hoặc từ người dùng. Không tự bịa số.
2. Mỗi con số mang nhãn bằng chứng: (a) bắt buộc theo chuẩn/luật, (b) khuyến nghị của tổ chức ban hành, (c) thực hành phổ biến, cần PO chốt. Ghi nhãn trong NFR đầu ra.
3. Nội dung pháp lý chỉ lấy từ `references/legal-vn.md`. Dòng nào đánh dấu ⚠️ hoặc "cần kiểm tra" thì giữ nguyên cờ đó, không điền số; luôn thêm "cần pháp chế xác nhận". Nói rõ ngày "last verified" của file.
4. Không chép nguyên văn ISO hoặc tài liệu có bản quyền. Diễn đạt lại, dẫn số điều khoản. ISO/IEC/IEEE 29148:2018 (5.2.8.3, bản chuẩn đã đọc) nêu: yêu cầu hiệu năng đứng một mình là **chưa đủ**, hiệu năng là thuộc tính của một chức năng và thường diễn đạt định lượng (9.6.14 ví dụ dạng "95% giao dịch xử lý dưới 1 giây"); mỗi NFR nên gắn với chức năng hoặc ngữ cảnh mà nó áp dụng, và chuẩn trỏ tới ISO/IEC 25030 và 25010 cho yêu cầu chất lượng phần mềm. Con số trong ví dụ của chuẩn chỉ là minh họa, không phải ngưỡng.
5. Yêu cầu chuyển đổi (chuyển dữ liệu, đào tạo, vận hành song song) không phải NFR: ghi riêng thành mục "Yêu cầu chuyển đổi" (BABOK 2.3).
6. Không viết từ mơ hồ ("nhanh", "ổn định", "thân thiện", "an toàn") mà không kèm số, điều kiện đo và cách kiểm chứng.

## Quy trình
1. **Xác định bối cảnh** (hỏi tối đa 4 câu, bỏ câu đã biết; ngoài ra luôn dò các nguồn ràng buộc: chuẩn/chứng nhận, quy định, SLA/cam kết, ngôn ngữ và địa phương hóa): loại sản phẩm (web / mobile / nội bộ / AI), người dùng và quy mô, dữ liệu xử lý (cá nhân, thẻ thanh toán, nhạy cảm), thị trường (chỉ Việt Nam hay có EU), mức quan trọng của hệ thống.
2. **Chọn hồ sơ sản phẩm** trong `references/product-profiles.md` để biết đặc tính nào ưu tiên.
3. **Duyệt 9 đặc tính** theo `references/iso25010-tree.md`. Với mỗi đặc tính con: áp dụng / không áp dụng (kèm lý do) / chưa rõ. Theo 25002, chỉ tùy biến ở mức đặc tính con và phải ghi lại lý do (xem `references/iso25002-guidance.md`).
4. **Viết NFR** theo `templates/nfr-template.md`: mã, đặc tính (mã ISO), mô tả, thước đo, ngưỡng, điều kiện đo, cách kiểm chứng, loại bằng chứng, độ ưu tiên, chủ sở hữu, nguồn.
5. **Trade-off và ưu tiên**: chỉ ra các cặp xung đột (ví dụ bảo mật và tiện dụng, hiệu năng và chi phí) và hỏi người dùng chốt. Dùng MoSCoW hoặc mức Must/Should/Could.
6. **Danh sách "cần xác nhận"** ở cuối: số chưa có nguồn, mục pháp lý ⚠️, câu hỏi cho PO/pháp chế/kỹ thuật.

## Chế độ rà soát
Khi người dùng đưa spec/PRD có sẵn: lập bảng độ phủ 9 đặc tính, đánh dấu NFR mơ hồ (không số, không điều kiện đo), NFR mâu thuẫn, và đặc tính bị bỏ sót theo hồ sơ sản phẩm. Đề xuất cách viết lại từng NFR yếu.

## Định dạng đầu ra mặc định
Bảng markdown cho NFR (một dòng một yêu cầu), sau đó phần "Trade-off cần chốt" và "Cần xác nhận". Nếu người dùng cần dùng lâu dài hoặc chia sẻ, tạo thành tài liệu thay vì dán dài trong chat.

## Tệp tham chiếu
- `references/iso25010-tree.md`: 9 đặc tính, 40 đặc tính con, gợi ý thước đo.
- `references/iso25002-guidance.md`: cách tùy biến và ưu tiên theo 25002.
- `references/thresholds.md`: ngưỡng số đã lọc, kèm nhãn và trạng thái.
- `references/legal-vn.md`: pháp lý Việt Nam/EU, có ngày kiểm tra.
- `references/babok-mapping.md`: đối chiếu với BABOK v3 khi người dùng dùng thuật ngữ BABOK; lưu ý transition requirements không phải NFR.
- `references/product-profiles.md`: web, mobile, nội bộ, AI.
- `templates/nfr-template.md`: mẫu NFR và ví dụ.
