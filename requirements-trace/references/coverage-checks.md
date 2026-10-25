# Kiểm tra độ phủ và phân tích tác động

Mục đích theo BABOK 5.1.8: các yêu cầu có quan hệ rõ ràng để thấy độ phủ và ảnh hưởng của thay đổi. Danh sách kiểm tra dưới đây do skill đề xuất, không phải danh sách chính thức của BABOK.

## Kiểm tra độ phủ
| # | Kiểm tra | Mức |
|---|---|---|
| 1 | Mục tiêu nào chưa có FR/story nào dẫn xuất? (mục tiêu bị bỏ rơi) | Cao |
| 2 | FR/story nào không truy về mục tiêu hoặc nguồn nào? (yêu cầu mồ côi, có thể là mở rộng phạm vi) | Cao |
| 3 | Story nào chưa có AC? | Cao |
| 4 | AC nào không kiểm chứng được hoặc chưa có test case (nếu mức đầy đủ)? | Trung bình |
| 5 | Quy tắc nghiệp vụ nào không được story nào dẫn chiếu? Story nào dẫn chiếu quy tắc không tồn tại? | Trung bình |
| 6 | Luồng nhiều bước nào thiếu luồng ngoại lệ/ca biên? | Trung bình |
| 7 | Hệ thống/tính năng có dữ liệu cá nhân, thanh toán, AI hay tích hợp mà chưa có NFR tương ứng (bảo mật, pháp lý, hiệu năng)? Gọi skill `nfr-writer`. | Cao |
| 8 | NFR nào không gắn với chức năng/mục tiêu nào và không có thước đo? | Trung bình |
| 9 | Hai yêu cầu mâu thuẫn nhau (cùng một đối tượng, kết quả khác nhau)? | Cao |
| 10 | Hai yêu cầu trùng lặp? | Thấp |
| 11 | Phụ thuộc vòng hoặc phụ thuộc vào mục chưa có trong phạm vi? | Trung bình |
| 12 | Mã trùng, mã nhảy bất thường, liên kết trỏ tới mã không tồn tại? | Thấp |
| 13 | Liên kết nào không đạt 5 tiêu chí (defined, necessary, correct, unambiguous, consistent)? Một yêu cầu bị nêu hơn một lần? (BABOK 7.4) | Trung bình |
| 14 | Mục nào chưa được duyệt mà đang được coi là đã chốt, hoặc đã duyệt nhưng bị sửa sau đó không qua đánh giá thay đổi? (BABOK 5.5) | Cao |

## Phân tích tác động khi có thay đổi
1. Xác định mục bị đổi (mã, nội dung cũ → mới).
2. Đi theo liên kết hai chiều: ngược lên (mục tiêu, nguồn: thay đổi còn phục vụ mục tiêu không?) và xuôi xuống (story, AC, NFR, test, thiết kế, tài liệu người dùng).
3. Phân loại mục bị ảnh hưởng: phải sửa / cần xem lại / không ảnh hưởng (nêu lý do).
4. Nêu rủi ro: mâu thuẫn mới, phạm vi tăng, ảnh hưởng tiến độ.
5. Nêu ai cần duyệt lại (theo nguồn/chủ sở hữu từng mục).
6. Không tự kết luận mức công sức; chỉ nêu mức độ bị chạm và để đội ước lượng.


Ghi chú: đủ độ phủ không có nghĩa tập yêu cầu mạch lạc; xem `architecture-approval-review.md` mục 1. Khi trình bày phần phân tích tác động ở trên, dùng năm yếu tố benefit/cost/impact/schedule/urgency (mục 3 file đó) để trình bày tác động.
