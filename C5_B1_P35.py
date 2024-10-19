# Nhập chuỗi 
chuoi = input("Nhập một chuỗi: ")

# Tính độ dài chuỗi
length = len(chuoi)
print(f"Độ dài chuỗi: {length}")

# Đếm ký tự đặc biệt
kydb= "!@#$%^&*()-=+./"
dem = 0
for char in chuoi:
    if char in kydb:
        dem += 1
print(f"Số ký tự đặc biệt: {dem}")

# Đếm ký tự chữ cái từ [a-z]
dem_thuong= 0
for char in chuoi:
    if char.islower():
        dem_thuong += 1
print(f"Số ký tự chữ cái thường [a-z]: {dem_thuong}")

# Đếm ký tự chữ số từ [0-9]
dem_so = 0
for char in chuoi:
    if char.isdigit():
        dem_so += 1
print(f"Số ký tự chữ số [0-9]: {dem_so}")

# Đếm ký tự chữ cái từ [A-Z]
dem_hoa= 0
for char in chuoi:
    if char.isupper():
        dem_hoa += 1
print(f"Số ký tự chữ cái hoa [A-Z]: {dem_hoa}")