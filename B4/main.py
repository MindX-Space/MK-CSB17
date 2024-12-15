"""
    Đề bài: Xây dựng một chương trình có tên là Shopping Cart, gồm các chức năng sau
        1. Hiển thị các sản phẩm có trong kho
        2. Hiển thị các sản phẩm đã thêm vào giỏ hàng
        3. Thêm sản phẩm vào giỏ hàng
        4. Xoá sản phẩm khỏi giỏ hàng
        5. Đóng chương trình
"""

product_list = ["Quần", "Áo", "Rau, củ", "Thịt", "Cá", "Gạo"]
shopping_cart = []

while True:
    print("==========SHOPPING CART==========")
    print("1. Xem danh sách sản phẩm")
    print("2. Xem giỏ hàng")
    print("3. Thêm sản phẩm vào giỏ hàng")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát")