# Lab 04

## Vì sao không merge release vào master?
Release có thể chứa bản sửa và số phiên bản riêng. Merge cả nhánh dễ đưa
thay đổi chỉ dành cho bản cũ vào master. Chỉ cherry-pick bản sửa cần thiết.
GitFlow thường có thêm develop và gộp hotfix vào main cùng develop;
bài này dùng master và các nhánh release riêng cho từng bài nộp.

## Vì sao chọn 1.0.0 thay vì 0.4.0?
Các chức năng cơ bản đã đủ và có test nên chọn làm bản ổn định đầu tiên.
Nếu vẫn coi giao diện chưa ổn định thì có thể dùng 0.4.0; số lab không
quyết định số phiên bản.

## Vì sao chuẩn bị release trên master?
Để số phiên bản, changelog và code đi qua cùng quy trình PR trước khi
đóng băng. Nhánh release chỉ giữ bản đã chọn, không phát triển tính năng mới.

## Tag khác nhánh release thế nào?
Tag ghi đúng một commit và không được di chuyển sau khi chia sẻ.
Nhánh release có thể tiến lên khi nhận hotfix. Annotated tag còn có
người tạo, thời gian và lời nhắn.
