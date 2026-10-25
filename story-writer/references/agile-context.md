# Bối cảnh agile, backlog, phân rã (BABOK 10.2, 11.1; Agile Extension v2 mục 7.1, 7.2, 7.4, 7.18–7.21; diễn đạt lại)

## Phân rã story: breadth-before-depth (AE 7.18, tr. 95–98)
Mục tiêu sản phẩm → MMF/component (nhóm chức năng tối thiểu đáng phát hành, thường là chủ đề của một lần phát hành) → story → story kèm acceptance criteria. Làm dần dần: ban đầu xác định mục tiêu, MMF và phần lớn story lớn; **phân rã tới mức chi tiết nhất sớm là lãng phí**. Story nào quá lớn hoặc chưa đủ hiểu để elaborate/ước lượng/giao thì mới cần phân rã. Sau khi có MMF, có thể dùng use case thay story.
**Không phân rã theo quy trình (bước 1,2,3), kiến trúc (làm DB, server, front-end) hay thủ tục (thiết kế, xây, test)**; phân rã theo tính năng có giá trị với khách hàng. Cảnh báo: đừng biến phân rã thành "yêu cầu chi tiết từ đầu"; biết lúc dừng.

## Elaborate story: just-in-time, just-enough (AE 7.19, tr. 98–99)
Là mức phân rã thấp nhất, làm trong Delivery Horizon, cho story đã được xác định thuộc iteration sắp tới, thường qua workshop với SME, người cần story, người sẽ test và BA điều phối. Làm để chuẩn bị Planning Workshop. Đầu ra: acceptance criteria rõ hơn (thêm/bớt/làm rõ), có thể thêm ví dụ và kịch bản, mô hình mức thấp (dữ liệu, luồng dữ liệu), mock-up màn hình/báo cáo, bảng dữ liệu vào/ra, task. Kết quả là hiểu chung về trạng thái "Done" của story. Rủi ro: làm sớm quá thì phải elicit lại; muộn quá thì chặn phát triển.

## Backlog (BABOK 10.2, tr. 220–223; AE 7.1, tr. 57–58)
Mục ở đầu: đủ nhỏ và đủ chi tiết để làm trong iteration kế tiếp; mục ở cuối có thể lớn và mơ hồ. Refinement liên tục gồm: elaborate, phân rã, ưu tiên, sắp thứ tự, chia mục lớn theo INVEST, thêm AC hoặc tài liệu cần; xong khi đội có đủ thông tin để thực hiện. Có họp refinement (thường do PO dẫn) và **Definition of Ready**. Giới hạn: lệch nhịp với đội thì kém hiệu quả; chỉ vài người dự nên bỏ sót góc nhìn người khác; kém hiệu quả khi vision/roadmap đổi liên tục. Backlog item thường là user story, nhưng có thể là job story hoặc wireframe.
=> Trong skill này: story chưa tới lượt chỉ viết bản sơ bộ và nói rõ chưa elaborate.

## Job story (AE 7.4, tr. 64–65)
Mẫu: "When <situation> I want to <motivation> so I can <expected outcome>" (hoặc ngôi thứ ba). Tình huống cung cấp bối cảnh; **không nêu persona** trong situation để đội nhìn khách hàng thật; **không nêu tính năng/giải pháp** trong motivation. Hợp khi bối cảnh và động cơ quan trọng (UX), nhiều vai trò cùng hoàn thành một việc. Giới hạn: dài hơn user story; đặt lẫn hai loại trong backlog dễ gây nhầm. Có thể dùng cùng nhau: job story nêu động cơ và kết quả, user story nêu tính năng giải quyết.

## BDD và ví dụ (AE 7.2, tr. 59–61)
Ví dụ cụ thể làm gốc để thống nhất yêu cầu. Gherkin: GIVEN <tình huống> (có thể AND), **chỉ một WHEN** <sự kiện>, THEN <kết quả> (có thể nhiều AND). Kịch bản có thể làm acceptance criteria và test tự động. Hỏi "what if/what about" để lộ kịch bản khác; họp **Three Amigos** (PO, tester, developer). Thuật ngữ BDD, ATDD, Specification by Example dùng thay nhau. Giới hạn: dễ sót kịch bản nếu không ai hỏi; quy tắc phức tạp thì số kịch bản quá nhiều, cần công cụ hoặc bảng quyết định; phải giữ cập nhật.

## Story map (AE 7.20, tr. 100–102)
Lưới hai chiều: ngang là chuỗi chủ đề/hoạt động của khách hàng theo thời gian; dọc là story theo thứ tự ưu tiên, cho phép cắt theo lần phát hành. Phù hợp quy trình có luồng; không phân tích phụ thuộc giữa yêu cầu (chỉ giúp lộ ra); không hợp ngữ cảnh không theo quy trình; cồng kềnh khi giải pháp rất lớn.

## Lưu ý nguồn
INVEST nằm ở AE v2 7.21 (xem quality-checks.md). **Lightweight Documentation và MoSCoW** có trong bảng kỹ thuật của BABOK v3 mục 11.1.2 nhưng **bị bỏ khỏi Agile Extension v2** (phụ lục D), nên không có mô tả chi tiết ở nguồn nào mình có.
