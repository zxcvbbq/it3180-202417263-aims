# Lab 01 – Thiết lập và refactor

## Cấu hình global và local khác nhau thế nào?
`git config --global` áp dụng cho tài khoản trên máy, thường lưu ở
`~/.gitconfig` (hoặc tệp cấu hình theo XDG). `--local` chỉ áp dụng cho
repository hiện tại và lưu trong `.git/config`; giá trị local được ưu tiên.
Bài này dùng danh tính Git và đăng nhập HTTPS sẵn có, không tạo SSH key.
Git trên máy là 2.39.1, thấp hơn yêu cầu 2.40 của slide; các lệnh đã dùng
vẫn chạy được. Python là 3.12.

## Vì sao dùng git mv?
`git mv` chuyển tệp và stage thao tác đổi tên cùng lúc. Git vẫn suy luận
rename bằng độ giống nhau của nội dung, không lưu một đối tượng rename
riêng. Giữ nguyên nội dung khi chuyển giúp review dễ đọc;
`git log --follow -- aims/cart.py` lần theo được lịch sử trước khi chuyển.

## release/lab01 có phải baseline không?
Có. Đây là trạng thái đã chọn để nộp Lab 01; lúc tạo, SHA của nhánh bằng
master. Nhánh có thể tiến lên khi sửa bài bằng hotfix, còn tag được tạo ở
Lab 04 sẽ định danh bất biến một snapshot chính xác.

## Vì sao không commit thẳng master dù làm một mình?
PR tạo điểm kiểm soát thay đổi: mục đích, diff, kiểm thử và lịch sử tích
hợp có thể đối chiếu. Ngoại lệ là các commit bootstrap đầu tiên theo slide.
Các thay đổi sau đó được đưa vào qua PR, kể cả tài liệu.

## Hoàn tác và kiểm tra
- Đã sửa thử `cart.py`, xem diff rồi `git restore cart.py`.
- Đã add thay đổi thử ở `main.py`, bỏ staging bằng `restore --staged`,
  xác nhận thay đổi còn ở working tree rồi mới restore.
- Đã sửa message sai chính tả bằng `commit --amend` **trước khi push**.
- Demo trước và sau chuyển package đều giữ `Total cost: 63.89 $`.
- `__pycache__/` bị ignore, không đưa vào baseline.

Thực hiện cá nhân, không giả lập một reviewer độc lập.
