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
