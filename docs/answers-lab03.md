# Lab 03

## Merge base là gì?
Là commit tổ tiên chung gần nhất của hai nhánh. Git dùng nó để so sánh
các thay đổi khi merge. Xem bằng `git merge-base <nhánh1> <nhánh2>`.

## Vì sao master và release phải dùng revert?
Vì đây là lịch sử đã chia sẻ. Revert tạo commit đảo thay đổi, không xóa
commit cũ như reset nên không làm lệch lịch sử của người khác.

## Kết quả thực hành
- Issue #8 được đóng sau khi merge PR #9. Commit test đứng trước fix;
  test đã fail vì giỏ nhận DVD thứ 21, sau sửa thì pass.
- PR #11 có base là `feature/discount`, sau đó PR #12 mới vào master.
  Giảm 20% của 100 còn 80; phần trăm ngoài 0–100 báo ValueError.
- PR #14 gặp conflict thật với nhánh tiếng Việt. Đã gộp thành thông báo
  tiếng Việt có tên DVD rồi chạy test trước khi commit.
- Đã thử rebase và xử lý conflict trên nhánh riêng chưa push.
- Đã thử reset soft, mixed, hard bằng commit nháp; tìm lại commit qua
  reflog. Không reset lịch sử đã push.
- PR #15 revert merge của PR #14 bằng `git revert -m 1`.
  Thông báo tiếng Việt của PR #13 vẫn còn.

Kết quả cuối: 4 tests OK, không còn dấu conflict.
