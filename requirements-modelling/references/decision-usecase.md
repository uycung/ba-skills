# Bảng quyết định, use case

## Decision modelling (BABOK 10.17, tr. 265–269; diễn đạt lại)
**Mục đích**: cho thấy quyết định nghiệp vụ lặp lại được đưa ra thế nào. Ba phần tử: decision, information, knowledge. Quy tắc trong một quyết định có thể là định nghĩa hoặc hành vi (10.9).
- **Decision table**: biểu diễn gọn **mọi quy tắc cho một quyết định nguyên tử**. Mỗi dòng (hoặc cột) là một quy tắc; các cột điều kiện ánh xạ vào phần tử dữ liệu; cột kết quả/hành động. Khi mọi điều kiện của một dòng đúng (hoặc để trống) thì dòng đó đúng và kết quả xảy ra. Ví dụ BABOK: hạn mức khoản vay theo số tiền và tuổi.
- **Decision tree**: mỗi đường tới lá là một quy tắc; mỗi tầng là một phần tử dữ liệu; hợp phân khúc khách hàng; ít dùng hơn bảng.
- **Decision requirements diagram (DRD)**: cho quyết định phức tạp, tách thành quyết định con. Phần tử: Decision (hình chữ nhật), Input data (hình bầu dục), Business knowledge model (chữ nhật cắt góc: tập quy tắc, bảng, cây hoặc mô hình dự đoán), Knowledge source (tài liệu hoặc người là căn cứ). Mũi tên liền: yêu cầu thông tin; đứt: yêu cầu tri thức; đứt bo tròn: thẩm quyền.
**Cách làm với skill**
1. Gọi tên quyết định bằng câu hỏi ("Có cho hủy lịch không?").
2. Liệt kê điều kiện (dữ liệu đầu vào) và các kết quả có thể.
3. Lập bảng với mọi tổ hợp (hoặc gộp bằng ô "bỏ qua" nếu điều kiện không ảnh hưởng); đánh dấu tổ hợp chưa biết kết quả là câu hỏi mở.
4. Quyết định có ≥ 5 điều kiện hoặc có sub-decision: tách thành DRD với nhiều bảng nhỏ.
**Kiểm tra** (của skill): đủ tổ hợp (không sót); không hai dòng chồng lấn cho cùng đầu vào mà kết quả khác nhau; kết quả hợp lệ với BR; điều kiện dùng đúng phần tử trong từ điển dữ liệu; ô trống/bỏ qua có nghĩa nhất quán.
Giới hạn BABOK: thêm một kiểu sơ đồ khác ngoài quy trình (thừa nếu quyết định đơn giản gắn chặt vào quy trình); chỉ bắt quy tắc thuộc quyết định đã biết; có thể làm tổ chức tưởng đã có cách quyết định chuẩn; không chạm trực tiếp quy tắc hành vi; cần thuật ngữ rõ.

## Use case và kịch bản (10.47, tr. 356–359)
**Use case** mô tả tương tác giữa tác nhân chính, giải pháp và tác nhân phụ để đạt mục tiêu của tác nhân chính, gồm các kết quả có thể (luồng chính, thay thế, ngoại lệ), viết từ góc nhìn tác nhân và **không mô tả vận hành bên trong**. **Scenario** là một cách đạt mục tiêu (một chuỗi bước); một use case gồm nhiều scenario.
**Phần tử mô tả** (không có định dạng bắt buộc): Name (động từ + danh từ), Goal (kết quả thành công theo góc nhìn tác nhân chính), Actors (chính bắt đầu use case; phụ hỗ trợ), Preconditions (sự thật phải đúng trước; không kiểm trong use case), Trigger (thường là hành động của tác nhân chính; có thể là thời gian), Flow of events (luồng chính = đường ngắn/đơn giản nhất thành công; luồng thay thế vẫn đạt mục tiêu; luồng ngoại lệ khi không đạt được và phản ứng mong muốn), Post-conditions (đúng với mọi luồng; success guarantee và minimal guarantee, ví dụ an ninh và toàn vẹn dữ liệu).
**Use case diagram**: tác nhân, use case, quan hệ. **Association** chỉ tác nhân có quyền truy cập chức năng. **Extend** (chèn hành vi thêm; use case được mở rộng phải tự chạy được), **Include** (dùng chức năng chung hoặc tách logic phức tạp; use case được include không cần tự đủ nếu không do tác nhân kích hoạt). Phân biệt business use case (tương tác với quy trình/chức năng) và system use case (tác nhân với ứng dụng).
**Cách làm với skill**: hỏi mục tiêu của tác nhân trước, rồi luồng chính ngắn nhất, rồi mỗi bước "điều gì có thể sai?" để lấy luồng ngoại lệ; quy tắc tách sang BR; hậu điều kiện kiểm được. Template bảng ở `templates/model-examples.md` mục 6.
**Kiểm tra**: mục tiêu nằm đúng góc nhìn tác nhân; mỗi bước nói ai làm; luồng ngoại lệ có đích và phản ứng; hậu điều kiện đúng với mọi luồng; extend/include dùng đúng nghĩa; không mô tả thiết kế nội bộ.
