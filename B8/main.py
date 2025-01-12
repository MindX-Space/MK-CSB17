"""
Đề bài: Quản lý Thư viện Sách

Hãy xây dựng một chương trình Python để quản lý một thư viện sách nhỏ.
Yêu cầu áp dụng các tính chất của lập trình hướng đối tượng (OOP).

Hướng dẫn:

1. Lớp `Book`:
   - Thuộc tính:
     - `title` (tên sách)
     - `author` (tác giả)
     - `isbn` (mã ISBN)
     - `available` (trạng thái: còn sẵn sàng hay không, mặc định là `True`)

   - Phương thức:
     - `__str__()`: Trả về thông tin sách dưới dạng chuỗi (bao gồm tên, tác giả và mã ISBN).
     - `borrow()`: Đánh dấu sách là không còn sẵn sàng (`available = False`).
     - `return_book()`: Đánh dấu sách là sẵn sàng (`available = True`).

2. Lớp `Library`:
   - Thuộc tính:
     - `books`: Danh sách các đối tượng `Book` trong thư viện.
   - Phương thức:
     - `add_book(book)`: Thêm một đối tượng `Book` vào thư viện.
     - `remove_book(isbn)`: Xóa sách khỏi thư viện dựa trên mã ISBN.
     - `display_books()`: Hiển thị danh sách tất cả các sách trong thư viện.
     - `search_book(title)`: Tìm kiếm sách theo tên.
     - `borrow_book(isbn)`: Mượn sách bằng mã ISBN.
     - `return_book(isbn)`: Trả lại sách bằng mã ISBN.

"""