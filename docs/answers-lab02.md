# Lab 02

## Vì sao đồng bộ master trước khi gửi PR?
Để nhánh tính năng có thay đổi mới của người khác và kiểm tra được chúng
có chạy cùng nhau không. Nếu có xung đột thì xử lý trước khi merge PR.

## Khi nào không nên rebase?
Không rebase commit đã chia sẻ khi người khác đang dựa vào nó, nhất là
master và release. Rebase đổi SHA nên dễ làm lệch lịch sử của người khác.

## feature và topic khác nhau thế nào?
`feature/*` thường thêm tính năng cho chương trình. `topic/*` dùng cho
một việc riêng như tài liệu, PR template hoặc CI. Cả hai đều qua PR.

## Ba kiểu merge
- Merge commit giữ các commit và thấy được nhánh đã gộp.
- Squash gộp cả PR thành một commit, dễ revert cả tính năng.
- Rebase đặt lại commit lên base mới, lịch sử thẳng nhưng SHA thay đổi.

## Kết quả
PR #4 dùng merge commit, #5 dùng squash, #6 dùng rebase.
Nhánh search đã merge master mới trước khi gửi PR. Push thẳng master
bị chặn với lỗi GH006. Bài làm cá nhân nên để 0 approval;
không có bước người khác request changes rồi approve.
