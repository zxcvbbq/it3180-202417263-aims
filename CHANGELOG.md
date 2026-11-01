# Changelog

## [Unreleased]

## [1.1.0] - 2026-11-01

### Added
- Sắp xếp giỏ hàng theo tên hoặc giá DVD.
- Tìm DVD theo thể loại bằng `search_by_category()`.

## [1.0.0] - 2026-11-01

### Added
- In chi tiết giỏ hàng bằng `Cart.print_cart()`.
- Tìm DVD theo tiêu đề bằng `search_by_title()`.
- Tính tổng tiền sau giảm giá bằng `total_cost_with_discount()`.
- Bốn bài kiểm thử cho giới hạn giỏ, tổng tiền và giảm giá.

### Fixed
- Không nhận DVD thứ 21 khi giỏ đã đủ 20 đĩa (#8).
- Sửa công thức giảm giá và kiểm tra phần trăm hợp lệ.

## [0.3.0] - 2026-11-01

### Added
- Giảm giá, test và bài tập conflict, revert của Lab 03.

### Fixed
- Giới hạn giỏ hàng 20 DVD (#8).

## [0.2.0] - 2026-11-01

### Added
- In giỏ hàng, tìm theo tiêu đề và tài liệu use case.
- PR template và bảo vệ master.

## [0.1.0] - 2026-11-01

### Added
- DVD, giỏ hàng và chương trình mẫu có tổng tiền 63.89 $.
- Chuyển mã nguồn vào package `aims`.
