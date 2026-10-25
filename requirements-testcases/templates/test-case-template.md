# Mẫu test case, ma trận phủ

## Test case
| ID | Nguồn (trace) | Loại | Mục tiêu | Tiền điều kiện | Dữ liệu | Bước | Kết quả mong đợi | Ưu tiên | Tự động? |
|---|---|---|---|---|---|---|---|---|---|
| TC-01 | AC-02.1 | Chuẩn | Hủy lịch hẹn trước hạn | Khách có lịch lúc 10:00; bây giờ 07:00 | Lịch LH-001 (giả định) | 1. Mở lịch LH-001 2. Chọn Hủy 3. Xác nhận | Trạng thái chuyển Đã hủy; khách nhận thông báo hủy | Cao | Có |
| TC-02 | BR-01 | Biên | Hủy đúng ngưỡng 2 giờ | Lịch lúc 10:00; bây giờ 08:00 | LH-002 | Như TC-01 | Cho hủy (giả định ngưỡng ≥ 2 giờ, cần xác nhận BR-01) | Cao | Có |
| TC-03 | BR-01 | Biên | Hủy dưới ngưỡng | Lịch lúc 10:00; bây giờ 08:01 | LH-003 | Như TC-01 | Từ chối, hiện thông báo theo AC-02.3 | Cao | Có |

Cột Ưu tiên: mức đề xuất theo rủi ro nghiệp vụ (cao/trung/thấp); là quy ước của skill, người dùng chốt.
Cột Loại: Chuẩn / Ngoại lệ / Biên / Sai dữ liệu / Quyền / Trạng thái / NFR / **Đề xuất bổ sung** (ca từ đoán lỗi hoặc "what if" chưa có AC duyệt; kết quả mong đợi để trống và ghi câu hỏi mở).

## Dạng Given-When-Then (khi đội dùng BDD)
```
Scenario: Hủy lịch đúng ngưỡng 2 giờ
  Given lịch LH-002 bắt đầu lúc 10:00 và bây giờ là 08:00
  When lễ tân chọn hủy lịch LH-002
  Then lịch chuyển sang trạng thái "Đã hủy"
  And khách nhận thông báo hủy
```
Một WHEN mỗi scenario.

## Ma trận phủ
| Nguồn | Mô tả ngắn | TC liên quan | Thiếu |
|---|---|---|---|
| AC-02.1 | Hủy trước hạn | TC-01 | |
| BR-01 | Ngưỡng hủy | TC-02, TC-03 | Chưa có test cho đơn vị thời gian khác |
| NFR-05 | Phản hồi ≤ ? | (chưa có) | Thiếu số đo, trả `nfr-writer` |

## Danh sách "Chưa đủ để viết test"
| Nguồn | Vì sao chưa viết | Cần gì | Chuyển cho |
|---|---|---|---|

## Kịch bản UAT (ví dụ)
| ID | Việc nghiệp vụ | Vai trò | Dữ liệu | Các bước nghiệp vụ | Kết quả mong đợi | Chứng minh (story/AC) | Kết quả | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| UAT-01 | Đặt lịch cho khách quen và nhận nhắc | Lễ tân | Khách A (giả định) | Tìm khách, chọn dịch vụ, chọn giờ, xác nhận | Lịch hiện đúng, khách nhận nhắc đúng lúc | US-01 (AC-01.1–01.4) | Đạt/Không đạt/Bị chặn | |
