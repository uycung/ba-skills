# Mẫu đăng ký stakeholder và ví dụ

Nhãn: [Đ] = Đã nói (nguồn nêu rõ), [S] = Suy luận, [G] = Giả định. Ví dụ dưới đây giả định để minh họa.

## Đăng ký
| ID | Người/nhóm | Vai trò BABOK | Vai trò trong sáng kiến | Thái độ | Quyền quyết định | Ảnh hưởng | Quan tâm/Tác động | Nguồn | Cần làm rõ |
|---|---|---|---|---|---|---|---|---|---|
| SH-01 | Giám đốc vận hành (sponsor) | Sponsor | Chịu trách nhiệm sáng kiến, duyệt ngân sách | Ủng hộ [S] | Duyệt phạm vi và ngân sách [Đ] | Cao [S] | Cao [S] | Ghi chép họp 12/10 | Ai thay thế khi vắng mặt? |
| SH-02 | Lễ tân (nhóm 5 người) | End user | Dùng hằng ngày để đặt và đổi lịch | ? | Không [S] | Thấp [S] | Cao [S] | Sơ đồ quy trình | Đại diện nhóm là ai? |
| SH-03 | Nhà cung cấp SMS | Supplier | Gửi nhắc lịch | ? | Không | Thấp [S] | Thấp [S] | Hợp đồng | Giới hạn gửi? |
| SH-04 | (chưa rõ) | Regulator | Quy định về dữ liệu khách | ? | ? | ? | ? | Tài liệu pháp lý | Ai phụ trách pháp chế? |

Vai trò BABOK không có trong dự án: ghi "không áp dụng" + lý do.

## Ma trận (ảnh hưởng × quan tâm)
| | Quan tâm thấp | Quan tâm cao |
|---|---|---|
| Ảnh hưởng cao | | SH-01 |
| Ảnh hưởng thấp | SH-03 | SH-02 |

## RACI (ví dụ cho "Duyệt yêu cầu thay đổi")
Định nghĩa: R thực hiện; A chịu trách nhiệm cuối và quyết định (chỉ một); C được hỏi ý kiến (hai chiều); I được thông báo (một chiều).
| Hoạt động | SH-01 Sponsor | BA | PM | Dev lead | Tester | Lễ tân |
|---|---|---|---|---|---|---|
| Đánh giá tác động thay đổi | I | R | C | C | C | I |
| Duyệt thay đổi | A | R | C | C | I | I |
| Thông báo thay đổi | I | R | A? | I | I | I |
(Hàng 3: cần xác nhận ai là A.)

## Kế hoạch cộng tác
| Nhóm | Mục đích | Hoạt động | Tần suất | Cách thức | Người phụ trách |
|---|---|---|---|---|---|

## Kế hoạch truyền thông
| Thông tin | Đối tượng | Phương thức | Tần suất | Mức chi tiết | Người gửi |
|---|---|---|---|---|---|

## Rủi ro từ stakeholder
| ID | Điều kiện | Hậu quả | Khả năng | Tác động | Phản ứng đề xuất | Người theo dõi |
|---|---|---|---|---|---|---|

## Câu hỏi mở và lịch sử thay đổi
