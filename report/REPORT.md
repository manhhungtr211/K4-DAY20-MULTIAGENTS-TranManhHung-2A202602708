# Báo cáo Lab: Self evolving Agentic

> Sao chép tệp này thành `report/REPORT.md` (đã làm ở Phần 0) và điền dần qua các Phần của lab. Xóa các dòng hướng dẫn dạng trích dẫn (bắt đầu bằng `>`). Văn phong kỹ thuật, ngắn gọn, mọi nhận định đi kèm số liệu hoặc bằng chứng. Trong buổi học: điền mục 1 đến 7 (bản nháp). Sau buổi học: hoàn thiện mục 8 đến 10.

## 1. Thông tin sinh viên và cấu hình

- Họ tên: Trần Mạnh Hùng
- Mã sinh viên: 2A202602708

- Nhà cung cấp và mô hình (`LAB_MODEL`, không ghi khóa API), nhiệt độ (`LAB_TEMPERATURE`), `recursion_limit`: OpenRouter (openai/gpt-4o-mini), nhiệt độ 0, recursion_limit 60
- Phiên bản Deep Agents (`pip show deepagents`), hệ điều hành, chạy trực tiếp hay trong Docker: deepagents 0.7.21, Windows (chạy trực tiếp)
- Số lần chạy tác vụ đã dùng / ngân sách: 0 / 30
- Commit của tag `freeze`:

## 2. Giả thuyết (commit TRƯỚC tag `freeze`, Phần 4.0)

> Dự đoán điều kiện nào đạt điểm cao nhất trên **tác vụ đánh giá** và vì sao. Nêu căn cứ từ phân loại lỗi (mục 4) và từ tài liệu tham khảo. Điền cả ba dòng; `verify_freeze.py` kiểm tra điều này.

- H1 (subagents so với baseline):
- H2 (skills-auto so với baseline):
- H3 (tác vụ học so với tác vụ đánh giá):

## 3. Làm quen Deep Agents (Phần 0.3)

1. Tác tử mặc định có các công cụ:
   - Thao tác tệp: `ls`, `read_file`, `write_file`, `edit_file`, `delete`, `glob`, `grep`
   - Thực thi shell: `execute`
   - Gọi subagent: `task`
   Công cụ cho phép chạy lệnh shell là `execute`.
2. Mô tả của công cụ `task` về `general-purpose`: là agent đa năng để nghiên cứu các câu hỏi phức tạp, tìm kiếm file và nội dung, thực thi các task nhiều bước. Về ngữ cảnh: subagent ở trạng thái không lưu phiên mặc định (stateless by default), nó chỉ nhìn thấy prompt được tác tử chính giao cho trong lời gọi tool chứ không tự động nhìn thấy toàn bộ ngữ cảnh/lịch sử hội thoại của tác tử chính (trừ khi có thiết lập kế thừa hội thoại).
3. Hướng dẫn hành vi trích dẫn:
   - Từ mô tả công cụ `task`: *"Launch multiple agents concurrently when their tasks are independent, using a single message with multiple tool calls."* (hoặc *"Each invocation is stateless by default: the agent sees only the prompt you give it and returns a single final report."*)
   - Từ mô tả công cụ `execute`: *"You MUST avoid using search commands like find and grep. Instead use the grep, glob tools to search. Use read_file rather than cat/head/tail."*

## 4. Đường cơ sở và phân loại lỗi (Phần 2.2)

> Chỉ dùng tác vụ học. Mỗi dòng là một check thất bại.

| Tác vụ | Check thất bại | Nhóm lỗi (A-G) | Bằng chứng (trích ngắn từ `detail` hoặc vết) |
|---|---|---|---|
| | | | |

Nhận xét: nhóm lỗi nào chiếm đa số? Skill có thể phòng ngừa nhóm đó không?

## 5. Điều kiện `subagents` (Phần 2.3)

- Các subagent đã định nghĩa (tên, vai trò, lý do thiết kế):
  1. `explorer`: Vai trò khám phá, đọc tài liệu, kiểm tra mẫu dữ liệu và log mà không sửa đổi file. Lý do: Giúp tách biệt pha tìm hiểu và phân tích ban đầu, tránh việc sửa vội khi chưa nắm rõ bối cảnh.
  2. `implementer`: Vai trò thực thi thay đổi mã nguồn, làm sạch dữ liệu và chạy các script test kiểm tra. Lý do: Chuyên môn hóa việc viết code và chỉnh sửa file theo yêu cầu.
  3. `reviewer`: Vai trò kiểm tra độc lập các file đầu ra, đối chiếu quy ước và schema. Lý do: Đóng vai trò kiểm định chất lượng khách quan trước khi hoàn tất nhiệm vụ.
- `subagent_calls` ở từng tác vụ và nhận xét (kể cả trường hợp bằng 0):
- Thông tin thiếu hoặc thừa khi giao việc (nếu có giao việc):
- Ảnh hưởng đến token và thời gian:

## 6. Self-evolving: skill do curator sinh (Phần 3)

- Số lần chạy curator, số skill bị xóa và lý do:

| Skill | Tổng quát hay riêng cho tác vụ học? | Đúng hay sai (nêu chỗ sai nếu có) | Độ dài, `description` và `skills_read` ở Phần 3.4 |
|---|---|---|---|
| | | | |

## 7. Kết quả so sánh (Phần 4.3, 4.4)

> Dán nội dung `report/table.md` và kết quả `python scripts/check_breakdown.py`. Nêu các lần chạy có `error` hoặc `skills_modified = true` (nếu có) và cách xử lý.

```text
(dán bảng ở đây)
```

## 8. Phân tích

> Trả lời từng câu bằng số liệu từ mục 7 và bằng chứng từ vết. Kết quả âm hoặc không có khác biệt vẫn hợp lệ nếu được phân tích tốt.

1. So với `baseline`, điều kiện nào cải thiện điểm tác vụ **học**? Điều kiện nào cải thiện điểm tác vụ **đánh giá**? Có điều kiện nào cải thiện tác vụ học nhưng không cải thiện tác vụ đánh giá? Nếu có, đó là dấu hiệu gì?
2. Tách điểm thành check kỹ thuật và check quy ước (`rule_`). Skill do curator sinh giúp nhóm check nào? Check quy ước **mới** của tác vụ đánh giá có được skill giúp không, và vì sao?
3. Dựa vào vết và `skills_read`, giải thích một check mà skill giúp đạt và một check mà skill không giúp (skill chưa được đọc, đọc nhưng không làm theo, skill thiếu hoặc sai).
4. Chi phí: so sánh số token trung bình giữa các điều kiện. Điều kiện nào có hiệu quả tốt nhất theo điểm trên mỗi token? Đa tác tử có đáng chi phí trong thí nghiệm này không?
5. Có dấu hiệu rò rỉ dữ liệu hoặc quá khớp nào trong skill sinh ra không? Bạn đã phòng tránh như thế nào?
6. Nhiễu: so sánh điểm tác vụ học của cùng bộ skill ở Phần 3.4 (đã sao lưu) và sau đóng băng. Chênh lệch bao nhiêu? Nó cho biết điều gì về độ tin cậy của các chênh lệch trong bảng ở mục 7?

## 9. Hạn chế và tính hợp lệ

> Nêu ít nhất 3 hạn chế và ảnh hưởng của từng hạn chế đến kết luận (ví dụ: chỉ 3 tác vụ mỗi vai trò, mỗi cấu hình chạy một lần, nhiễu của mô hình, tác vụ do giảng viên thiết kế sẵn quy ước, chỉ một mô hình).

1.
2.
3.

## 10. Kết luận

> Tối đa 5 câu. Chỉ khẳng định điều số liệu hỗ trợ. Nêu một đề xuất cải tiến tiếp theo.

## Phụ lục

- Lệnh đã chạy (theo thứ tự):
- Thử thách mở rộng (nếu có): hướng chọn, kết quả, nhận xét.
- Ghi chú khác:
