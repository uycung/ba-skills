# Hướng dẫn dùng mô hình chất lượng theo ISO/IEC 25002:2024

Tóm tắt diễn đạt lại từ bản 25002:2024 (ấn bản đầu, hiện hành). Dẫn số mục khi trích; không chép nguyên văn.

1. **Tùy biến**: được phép thêm, bớt hoặc đổi tên ở mức **đặc tính con**, không ở mức đặc tính; phải ghi lại thay đổi và lý do. Trong skill: mỗi đặc tính con "không áp dụng" cần lý do ngắn.
2. **Trade-off (§7.1)**: các đặc tính có thể kéo nhau (bảo mật so với tiện dụng, hiệu năng so với chi phí và khả năng bảo trì). Nêu cặp xung đột, để PO quyết định.
3. **Ưu tiên theo bối cảnh (§7.4)**: không phải đặc tính nào cũng quan trọng như nhau; xếp hạng theo loại sản phẩm, người dùng, rủi ro. Dùng `product-profiles.md` làm điểm xuất phát.
4. **Vai trò BA (§8.1)**: dự đoán NFR sớm, từ giai đoạn yêu cầu, thay vì phát hiện ở giai đoạn kiểm thử.
5. **Đo lường**: thước đo nằm ở ISO/IEC 25023 (bản dự thảo DIS 25023:2026 đang có). Khi viết NFR, mỗi yêu cầu cần thước đo, ngưỡng và cách đo, dù không dùng đúng mã của 25023.
6. **Họ tiêu chuẩn liên quan**: 25019 (chất lượng sử dụng), 25030 (yêu cầu chất lượng), 25040 (quy trình đánh giá).
