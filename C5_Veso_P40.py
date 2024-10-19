import random

# Khởi tạo biến lưu
ve = []
tong = 0

# Nhập dãy số từ người dùng
nhap_so = input("Nhập 6 số từ 1 đến 45 (hoặc 'q' để kết thúc): ")

while nhap_so.lower() != 'q':
    # Chia tách dãy số
    day_so = nhap_so.split('-')
    
    # Kiểm tra tính hợp lệ
    if len(day_so) != 6:
        print("Dãy số không hợp lệ. Vui lòng nhập lại.")
    else:
        valid = True
        for n in day_so:
            if not n.isdigit() or int(n) < 1 or int(n) > 45:
                valid = False
                break
        
        if valid and len(set(day_so)) == 6:
            # Lưu vé số vào biến
            ve += [day_so]  # tạo danh sách mới
        else:
            print("Dãy số không hợp lệ. Vui lòng nhập lại.")
    
    nhap_so = input("Nhập 6 số từ 1 đến 45 (hoặc 'q' để kết thúc): ")

# Tạo dãy số trúng
so_trung = []
while len(so_trung) < 6:
    num = random.randint(1, 45)
    if num not in so_trung:
        so_trung += [num]  # thêm số

# In dãy số trúng 
print("Dãy số trúng thưởng:", end=' ')
for num in so_trung:
    print(num, end=' ')
#print()  # Xuống dòng

# Kiểm tra người thắng cuộc
for ticket in ve:
    mot = 0
    for num in ticket:
        if int(num) in so_trung:
            mot += 1

    gia = 0
    if mot == 3:
        gia = 30000
    elif mot == 4:
        gia = 300000
    elif mot == 5:
        gia = 10000000
    elif mot == 6:
        gia = 10000000000
    
    tong += gia
    print(f"Dãy số {ticket} trùng {mot} số, nhận được: {gia:.0f}đ")

print(f"Tổng số tiền người chơi nhận được: {tong:.0f}đ")