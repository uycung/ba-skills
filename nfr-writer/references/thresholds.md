# Bảng tham chiếu NFR (bản đã lọc, cập nhật theo kết quả agent v2)

Ngày lập: 24/10/2026. Sắp xếp theo 9 đặc tính ISO/IEC 25010:2023.
ISO 25010 chỉ định nghĩa đặc tính và đặc tính con, không đưa ra ngưỡng số. Mọi con số dưới đây đến từ nguồn khác.

Trạng thái:
- ✅ Đã kiểm tra nguồn trong phiên này.
- 🔶 Khớp với hiểu biết hiện có nhưng chưa mở lại nguồn gốc. Phải xác minh trước khi đưa vào skill.
- ❌ Đã loại khỏi bảng gốc (xem cuối file).

Loại bằng chứng: (a) bắt buộc theo chuẩn/luật; (b) khuyến nghị của tổ chức ban hành, nguồn nêu đúng con số; (c) thực hành phổ biến, không có nguồn chính thức, cần chốt với PO.

Quy ước dùng trong skill: định nghĩa ISO diễn đạt lại bằng lời riêng, dẫn số điều khoản, không chép nguyên văn.

## 1. Functional suitability (3 đặc tính con)
Completeness, correctness, appropriateness. Không có ngưỡng số tiêu chuẩn.
| Ý tưởng NFR | Trạng thái | Ghi chú |
|---|---|---|
| Độ đúng của kết quả tính toán, tỷ lệ lỗi chức năng chấp nhận được | (c) | Do PO chốt theo rủi ro nghiệp vụ. |
Đã bỏ: nghĩa vụ pháp lý xếp vào đây (xếp sai đặc tính). Nghĩa vụ pháp lý đặt ở file `legal-vn.md` và gắn vào đặc tính liên quan (Security, Safety...).

## 2. Performance efficiency (3)
Time behaviour, resource utilization, capacity.
| Chỉ số | Ngưỡng | Loại | Trạng thái | Nguồn |
|---|---|---|---|---|
| LCP (tải nội dung chính) | ≤ 2,5 s tại phân vị 75 | (b) | ✅ | web.dev/articles/vitals |
| INP (độ phản hồi tương tác) | ≤ 200 ms tại phân vị 75 | (b) | ✅ | web.dev/articles/vitals |
| CLS (ổn định bố cục) | ≤ 0,1 tại phân vị 75 | (b) | ✅ | web.dev/articles/vitals |
| p95/p99 độ trễ API | không có nguồn chính thức | (c) | ✅ đã loại số cứng | Chốt theo SLO của sản phẩm |
| Headroom tải, ngưỡng autoscaling | không có nguồn chính thức | (c) | ✅ đã loại số cứng | Chốt theo load test |
Cách viết NFR: nêu rõ điều kiện đo (thiết bị, mạng, tải, phân vị), không viết "nhanh" hay "mượt".

## 3. Compatibility (2)
Co-existence, interoperability.
| Ý tưởng NFR | Trạng thái | Ghi chú |
|---|---|---|
| Danh sách trình duyệt/OS/thiết bị hỗ trợ | (c) | Lấy từ số liệu truy cập thực tế của sản phẩm. Gợi ý tham khảo (Statcounter VN, 09/2026, nguồn thứ cấp, agent tự cộng dồn): Android ≥ 12 phủ ≈ 82,8%, iOS ≥ 16 ≈ 92,3%. Chưa chắc Android 17 đã ổn định (hai nguồn mâu thuẫn). Bản gốc ghi "iOS ≥ 17, Android ≥ 13 = N−1" là sai, đã bỏ. |
| Chuẩn API/định dạng trao đổi dữ liệu | (c) | Nêu tên chuẩn và phiên bản cụ thể trong spec. |

## 4. Interaction capability (8)
Appropriateness recognizability, learnability, operability, user error protection, user engagement, inclusivity, user assistance, self-descriptiveness.
| Yêu cầu | Trạng thái | Nguồn |
|---|---|---|
| Mức tuân thủ WCAG 2.2 Level AA cho web/mobile web | (b) ✅ | w3.org/TR/WCAG22 |
| Kích thước mục tiêu cảm ứng tối thiểu 24×24 CSS px (tiêu chí 2.5.8, mức AA) | ✅ | w3.org/TR/WCAG22 |
| Focus không bị che (2.4.11, mức AA) | ✅ | w3.org/TR/WCAG22 |
| Hỗ trợ đăng nhập không cần nhớ/giải đố (3.3.8, mức AA) | ✅ | w3.org/TR/WCAG22 |
Chú ý ánh xạ: WCAG chủ yếu phục vụ "inclusivity" (và một phần "operability"). Bản gốc xếp 2.4.7 vào "user assistance" là gượng ép, đã bỏ.
WCAG 2.0 AA theo TT 26/2020: chưa xác minh (xem mục loại bỏ).

## 5. Reliability (4)
Faultlessness, availability, fault tolerance, recoverability.
| Mức khả dụng | Thời gian ngừng tối đa/năm | Trạng thái |
|---|---|---|
| 99% | ≈ 3,65 ngày | ✅ (tính toán) |
| 99,9% | ≈ 8,76 giờ | ✅ (tính toán) |
| 99,99% | ≈ 52,6 phút | ✅ (tính toán) |
| 99,999% | ≈ 5,26 phút | ✅ (tính toán) |
Luôn nêu cửa sổ tính (tháng/quý/năm) và cách đo (đo ở đâu, loại trừ bảo trì có báo trước hay không). Dùng error budget = 100% − SLO (sre.google, ✅).
RPO/RTO theo tier: (c), chốt theo phân tích tác động nghiệp vụ. Số liệu DR của AWS trong bản gốc bị thêm thắt, đã bỏ.
DORA (dora.dev): báo cáo mới nhất là 2025 (theo agent v2, chưa tự mở lại). Chỉ số hiện hành gồm 5 chỉ số, trong đó có deployment rework rate và failed deployment recovery time. **Không dùng số 2024** (5/20/10/40%) vì đã lỗi thời. Khi cần ngưỡng, lấy bảng từ báo cáo mới nhất và ghi năm báo cáo. Trạng thái: ⚠️.
DORA là chỉ số hiệu năng phân phối phần mềm, không phải đặc tính con của Flexibility như bản gốc xếp. Đặt trong phần "Chỉ số vận hành" của skill.

## 6. Security (6)
Confidentiality, integrity, non-repudiation, accountability, authenticity, resistance.
| Chuẩn | Nội dung dùng trong NFR | Trạng thái |
|---|---|---|
| OWASP Top 10:2025 | Danh mục rủi ro web phổ biến để làm tiêu chí "không có lỗ hổng nhóm này" | ✅ |
| OWASP ASVS 5.0 | 17 chương, khoảng 350 yêu cầu, 3 mức L1/L2/L3. Chọn mức theo rủi ro. | ✅ |
| PCI DSS 4.0.1 | Bắt buộc nếu xử lý dữ liệu thẻ thanh toán (a). Trích đúng số yêu cầu từ tài liệu chính thức khi viết spec. | ✅ phiên bản; 🔶 từng yêu cầu |
| ISO/IEC 27001:2022 | Hệ thống quản lý an toàn thông tin (Annex A 93 biện pháp). | 🔶 |
| ISO/IEC 42001:2023 | Hệ thống quản lý AI. | 🔶 |
| NIST AI 100-1 (AI RMF 1.0) | Tự nguyện. Bản gốc ghi sai mã là "AI RMF". | 🔶 |
Phần luật: xem `legal-vn.md`.

## 7. Maintainability (5)
Modularity, reusability, analysability, modifiability, testability.
| Ý tưởng NFR | Trạng thái | Ghi chú |
|---|---|---|
| Ngưỡng cyclomatic complexity | (c) | Các mức 10/20/50 thuộc SEI, không phải NIST như bản gốc ghi. Dùng làm gợi ý. |
| Độ phủ kiểm thử (code coverage) | (c) | Không có ngưỡng chuẩn. Chốt theo rủi ro module. |

## 8. Flexibility (4)
Adaptability, scalability, installability, replaceability.
| Ý tưởng NFR | Trạng thái | Ghi chú |
|---|---|---|
| Quy mô cần mở rộng (người dùng, giao dịch/giây, dữ liệu) | (c) | Nêu số hiện tại, số 12–24 tháng tới, cách đo. |
Đã bỏ: DORA xếp ở đây (xếp sai đặc tính).

## 9. Safety (5)
Operational constraint, risk identification, fail safe, hazard warning, safe integration.
Áp dụng mạnh cho sản phẩm có ảnh hưởng đến thể chất, tài chính lớn hoặc AI rủi ro cao. Không có ngưỡng số chung. Luật AI Việt Nam và EU AI Act: xem `legal-vn.md`.

## Đã loại hoặc hạ xuống, lý do
| Mục trong bản gốc | Lý do |
|---|---|
| Luật BVDLCN "dự thảo" | Sai: đã có hiệu lực 01/01/2026. Chuyển sang `legal-vn.md`. |
| Nghị định 53/2022, NĐ 85/2016, TT 12/2022 | Dựa trên luật đã bị bãi bỏ; chưa rõ hiệu lực chuyển tiếp. Đánh dấu "cần kiểm tra". |
| QĐ 975/QĐ-BTTTT, TT 26/2020 (WCAG 2.0 AA) | Chưa xác minh. |
| iOS 17 / Android 13 "N−1" | Lạc hậu, không có nguồn. |
| API p95/p99, 5xx < 0,1%, headroom 30–50%, ngưỡng autoscaling | Không có nguồn nêu đúng con số: chuyển sang (c). |
| Số liệu DR của AWS | Bị thêm thắt, chưa kiểm. |
| ASVS "14 chương" | Sai: v5.0 có 17 chương. |
| URL chỉ là trang chủ | Không dùng làm nguồn. |

## Danh sách việc còn lại để agent v2 kiểm
1. Mở lại từng nguồn ở các dòng 🔶.
2. Định nghĩa chính thức cho khoảng 28 đặc tính con còn thiếu (chỉ có bản thứ cấp).
3. Chỉ số DORA 2025: mở dora.dev, ghi bảng chuẩn.
4. Mốc hỗ trợ iOS/Android hiện hành và thị phần tại Việt Nam.
