# Khởi tạo biến để kiểm tra
value = None

# Sử dụng vòng lặp while để kiểm tra giá trị nhập vào
while value is None or not (-99 <= value <= 99):
    # Nhập giá trị từ người dùng
    n = input("Nhập một số trong khoảng [-99; 99]: ")

    # Kiểm tra xem giá trị có phải là số không
    if n.strip() and n.replace('-', '', 1).isdigit():
        value = int(n)  # Chuyển đổi giá trị thành số nguyên
    else:
        print("Giá trị nhập vào không hợp lệ. Vui lòng nhập một số nguyên.")

# Kiểm tra điều kiện và in kết quả
if -99 <= value <= 99:
    print(f"Giá trị nhập vào hợp lệ: {value}")


"""
Câu lệnh if n.strip() and n.replace('-', '', 1).isdigit(): được sử dụng để kiểm tra tính hợp lệ của một chuỗi n. n.strip():
1. Phương thức strip() loại bỏ tất cả các khoảng trắng (spaces) ở đầu và cuối chuỗi.
Nếu sau khi loại bỏ khoảng trắng, chuỗi còn lại không rỗng, thì điều này trả về True. Nếu chuỗi chỉ chứa khoảng trắng, nó sẽ trả về False.
2. n.replace('-', '', 1).isdigit():
replace('-', '', 1) sẽ thay thế dấu - đầu tiên (nếu có) trong chuỗi bằng một chuỗi rỗng. Điều này có nghĩa là nó chỉ cho phép một dấu trừ ở đầu chuỗi.
Sau đó, isdigit() kiểm tra xem chuỗi còn lại có phải là số nguyên không. Nếu chuỗi chỉ chứa các ký tự số thì isdigit() trả về True; nếu có bất kỳ ký tự nào không phải số, nó sẽ trả về False.
"""