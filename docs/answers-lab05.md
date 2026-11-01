# Lab 05

## Upstream first và release first khác nhau thế nào?
Upstream first sửa trên master rồi đưa về release, ít bị quên sửa ở bản
mới nhưng phải kiểm tra bản sửa có chạy được trên code cũ không.
Release first sửa ngay bản đang phát hành nên vá nhanh, nhưng phải nhớ
đưa bản sửa sang master và các release còn bị ảnh hưởng. Bài này dùng
release first.

## Vì sao chỉ cherry-pick commit sửa lỗi?
Commit tăng phiên bản 1.0.1 chỉ dành cho dòng 1.0.x. Nếu đưa cả commit đó
vào master thì sẽ đè phiên bản 1.1.0. Tách hai commit giúp chọn đúng phần
cần đưa sang và `-x` ghi lại SHA gốc để truy vết.

## Nếu quên sửa release/lab05 thì phát hiện bằng cách nào?
Chạy cùng truy vấn `lion` trên v1.0.1, v1.1.0 và master. Bản chưa sửa sẽ
trả về 0 thay vì 1. Xem log với trailer cherry-pick cũng kiểm tra được
bản sửa đã được đưa sang đủ hai nơi chưa.

## Vì sao chưa gắn tag v1.1.0 ngay khi tạo release/lab05?
Vì còn phải đưa hotfix vào trước khi chốt bản phát hành. Nếu tag đã chia
sẻ thì không di chuyển tag; phải phát hành bản vá mới, ví dụ v1.1.1.

## Kết quả kiểm tra
- Hotfix: PR #22 vào release/lab04, #23 vào master, #24 vào release/lab05.
- Diff v1.0.0..v1.0.1 đúng 4 tệp; có 2 commit cherry-pick cùng fix gốc.
- v1.0.1 chạy 5 tests; v1.1.0 và master chạy 8 tests, đều OK.
- Từ khóa `lion` trả về 1 kết quả trên cả ba bản; Issue #21 đã đóng.
- PR #25 thêm CI. Master yêu cầu check `test` thành công trước khi merge.
- [PR #26](https://github.com/zxcvbbq/it3180-202417263-aims/pull/26)
  cố ý làm sai tổng tiền: CI fail, merge bị chặn. Đã đóng, không merge.
