# Lab 01

## Cấu hình global và local
Global dùng cho tài khoản trên máy, thường lưu ở `~/.gitconfig`.
Local chỉ dùng trong repo, lưu ở `.git/config` và được ưu tiên hơn global.

## Vì sao dùng git mv?
Lệnh này vừa chuyển tệp vừa stage thay đổi. Git nhận ra rename dựa vào
nội dung; `git log --follow` vẫn xem được lịch sử của tệp cũ.

## release/lab01 có phải baseline không?
Có, vì đây là bản đã chọn để nộp Lab 01. Khi tạo, nhánh này cùng SHA với
master. Nếu cần sửa bài đã nộp thì phải qua hotfix.

## Vì sao vẫn dùng PR khi làm một mình?
PR giúp xem lại thay đổi và kết quả kiểm tra trước khi gộp vào master.
Lịch sử cũng dễ theo dõi hơn commit thẳng.

## Kết quả
Đã thử restore, bỏ staging và amend commit chưa push. Sau refactor,
chương trình vẫn in tổng `63.89 $`, cache không bị đưa vào Git.
Dùng đăng nhập HTTPS có sẵn, không tạo SSH key. Git là 2.39.1
(thấp hơn yêu cầu 2.40 trong slide), Python 3.12.
