# ba-skills

**English summary.** Eleven Claude Agent Skills for Business Analyst work, written in Vietnamese: stakeholder analysis, business case, elicitation, modelling, stories, NFRs, prioritisation, traceability, review, test cases/UAT, and assembling BRD/PRD/SRS documents. Grounded in BABOK v3, the Agile Extension v2, ISO/IEC 25010:2023, ISTQB CTFL v4.0.1 and ISO/IEC/IEEE 29148:2018 (paraphrased, section numbers cited, no source text included). The skills cross-reference each other, so install the whole set. Install: copy the 11 folders into `~/.claude/skills/` (see [Cài đặt](#cài-đặt)). License: MIT. The Vietnamese legal reference in `nfr-writer` is not legal advice and contains unverified items.

---

Bộ 11 skill giúp BA làm việc với Claude từ đầu dự án đến lúc bàn giao. Các skill viết bằng tiếng Việt, bám BABOK v3, Agile Extension v2, ISO/IEC 25010:2023, ISTQB CTFL v4.0.1 và ISO/IEC/IEEE 29148:2018. Hướng dẫn chi tiết: [docs/usage-guide.md](docs/usage-guide.md).

## 11 skill

| Skill | Dùng khi | Đưa vào | Nhận lại |
| --- | --- | --- | --- |
| [`requirements-stakeholders`](requirements-stakeholders) | Đầu dự án hoặc đầu đợt khai thác, cần biết ai cần gặp, ai quyết định | Mô tả dự án, sơ đồ tổ chức, ghi chép họp | Danh sách stakeholder, ma trận ảnh hưởng, onion, RACI, persona, kế hoạch cộng tác |
| [`business-case-strategy`](business-case-strategy) | Cần biện minh hoặc chọn hướng thay đổi trước khi vào yêu cầu chi tiết | Mô tả vấn đề, dữ liệu chi phí và lợi ích | Hiện trạng, tương lai, khoảng cách, rủi ro, chiến lược, business case, ROI/NPV/IRR, SWOT, KPI |
| [`requirements-elicitation`](requirements-elicitation) | Trước hoặc sau buổi gặp stakeholder | Mục tiêu buổi họp hoặc ghi chép họp | Kế hoạch khai thác, bộ câu hỏi, kết quả có nguồn (chưa xác nhận), danh sách cần xác nhận |
| [`requirements-modelling`](requirements-modelling) | Mô tả bằng chữ chưa đủ rõ | Quy trình, quy tắc, dữ liệu, vai trò | Mô hình quy trình, trạng thái, dữ liệu, bảng quyết định, use case, phạm vi, giao diện, ma trận quyền |
| [`story-writer`](story-writer) | Biến ý tưởng thô thành yêu cầu rõ | Ý tưởng, ghi chép, yêu cầu thô | Story, acceptance criteria, use case, bảng quy tắc nghiệp vụ; hoặc bản rà soát story |
| [`nfr-writer`](nfr-writer) | "Nhanh, an toàn, dễ dùng" cần thành số đo được | Loại sản phẩm, spec hiện có | NFR đo được theo 9 đặc tính ISO 25010:2023, trade-off, danh sách cần xác nhận |
| [`requirements-prioritize`](requirements-prioritize) | Xếp backlog, chốt MVP, đánh giá lại khi đổi bối cảnh | Danh sách yêu cầu kèm mã, ràng buộc | Bảng chấm điểm có lý do, thứ tự, lát cắt phát hành, xung đột chưa giải quyết |
| [`requirements-trace`](requirements-trace) | Kiểm lỗ hổng spec, phân tích tác động khi yêu cầu đổi | PRD, story, NFR, test | Ma trận truy vết, khoảng trống, mâu thuẫn, phân tích tác động |
| [`requirements-review`](requirements-review) | Trước khi xin duyệt hoặc giao dev/tester | Tài liệu yêu cầu bất kỳ | Báo cáo phát hiện có mức nghiêm trọng, kết luận sẵn sàng duyệt hay chưa |
| [`requirements-testcases`](requirements-testcases) | Biến yêu cầu thành bộ kiểm thử, lập UAT | Story, AC, quy tắc, bảng quyết định, mô hình trạng thái, NFR | Test case truy vết được, ma trận phủ, gói UAT, chọn test hồi quy |
| [`requirements-document`](requirements-document) | Cần gói yêu cầu để duyệt, bàn giao hoặc ký hợp đồng | Các đầu ra của những skill trên | BRD, PRD hoặc SRS, kiểm nhất quán, danh sách chỗ còn thiếu |

## Thứ tự làm việc đề xuất

Gợi ý, không bắt buộc:

1. Bối cảnh: `requirements-stakeholders`, `business-case-strategy`
2. Khai thác: `requirements-elicitation`
3. Viết và mô hình hóa: `requirements-modelling`, `story-writer`, `nfr-writer`
4. Quyết định: `requirements-prioritize`
5. Kiểm soát: `requirements-trace`, `requirements-review`
6. Kiểm chứng: `requirements-testcases`
7. Đóng gói: `requirements-document`

## Cài đặt

Các skill tham chiếu lẫn nhau theo tên (ví dụ `requirements-trace`, `story-writer`), nên cài cả 11, không cài lẻ.

```bash
git clone https://github.com/uycung/ba-skills.git
cd ba-skills
```

### Cách 1: cài toàn cục cho mọi agent (cách tác giả dùng)

Tác giả dùng skill `install-global-skills` (một skill cá nhân, không nằm trong repo này). Nó giữ một bản duy nhất của mỗi skill tại `~/.agents/skills/<tên-skill>/`; Claude Code đọc qua symlink `~/.claude/skills` trỏ tới thư mục đó, Antigravity qua `~/.gemini/config/skills`. Không copy thêm vào thư mục riêng của từng agent. Nếu máy bạn có cùng cấu trúc, làm tương đương:

```bash
mkdir -p ~/.agents/skills
for d in */; do [ -f "$d/SKILL.md" ] && cp -R "${d%/}" ~/.agents/skills/; done
```

Nếu chưa có symlink: `ln -s ~/.agents/skills ~/.claude/skills` (chỉ khi `~/.claude/skills` chưa tồn tại).

### Cách 2: chép tay vào Claude Code

```bash
mkdir -p ~/.claude/skills
for d in */; do [ -f "$d/SKILL.md" ] && cp -R "${d%/}" ~/.claude/skills/; done
```

Dùng `.claude/skills/` trong thư mục dự án nếu chỉ muốn áp dụng cho một dự án. Mở phiên mới để Claude nhận skill.

### Cách 3: tải zip lên claude.ai

Mỗi skill là một zip có đúng một thư mục gốc trùng tên skill:

```bash
for d in */; do [ -f "$d/SKILL.md" ] && zip -rq "${d%/}.zip" "${d%/}" -x '*.DS_Store'; done
```

Rồi tải từng zip lên mục Skills trong phần cài đặt của claude.ai (cần gói có hỗ trợ Skills). Tác giả chưa kiểm cách này trên giao diện hiện tại.

### Cập nhật

```bash
git pull
```

rồi chạy lại lệnh sao chép ở cách đã chọn. Lệnh `cp -R` ghi chồng lên thư mục cũ nhưng không xóa tệp đã bị bỏ ở bản mới; muốn sạch, xóa thư mục skill cũ trước khi chép (sao lưu nếu bạn có sửa tay). Với claude.ai, tải lại zip mới.

### Kiểm tra nhanh

`business-case-strategy/scripts/fin.py` nhận một tệp JSON. Với dòng tiền sau:

```json
{"discount_rate":0.1,"years":[{"year":0,"benefits":0,"costs":100},{"year":1,"benefits":40,"costs":10},{"year":2,"benefits":60,"costs":10},{"year":3,"benefits":80,"costs":10}]}
```

kết quả đúng là NPV ≈ 21.187, ROI ≈ 0.3846, IRR ≈ 0.2013, hoàn vốn ≈ 2.2857 năm.

## Nguồn và độ tin cậy

| Nguồn | Mức đối chiếu |
| --- | --- |
| BABOK v3, Agile Extension v2 | Đọc từ PDF, diễn đạt lại, trích số mục; một số mục chưa đọc |
| ISO/IEC 25010:2023 | Tên đặc tính khớp bản 2023; phần "Ý nghĩa" là diễn đạt của skill, chưa đối chiếu định nghĩa chính thức |
| ISTQB CTFL v4.0.1 | Đã đối chiếu với PDF |
| ISO/IEC/IEEE 29148:2018 | Đã đối chiếu các điều 5.2, 6.5.2.2, 9.2, 9.3, 9.6; StRS (9.4) và SyRS (9.5) chưa đọc nội dung |
| Pháp luật Việt Nam, EU AI Act | Xem cảnh báo dưới đây |

Repo không chứa PDF hay văn bản gốc của các nguồn này. Chi tiết: [docs/usage-guide.md](docs/usage-guide.md#5-nguồn-và-độ-tin-cậy).

> **Cảnh báo pháp lý.** [`nfr-writer/references/legal-vn.md`](nfr-writer/references/legal-vn.md) là thông tin tham khảo, **không phải tư vấn pháp lý**. Kiểm lần cuối ngày 24/10/2026 và có các mục gắn ⚠️ là **chưa được xác nhận** từ văn bản gốc (ví dụ NĐ 330/2026, NĐ 142/2026, tình trạng NĐ 53/2022). Cần pháp chế xác nhận trước khi đưa vào hợp đồng hoặc spec.

## Giới hạn đã biết

- Chưa chạy thử cả bộ trên PRD hoặc ghi chép họp thật.
- Skill chuẩn bị đầu vào để người có thẩm quyền xác nhận; không thay QA, pháp chế hay người ra quyết định.
- Skill không tự điền con số (ngưỡng NFR, tiêu chí UAT, chỉ tiêu); chưa có thì ghi "cần chốt".

## Giấy phép

[MIT](LICENSE).
