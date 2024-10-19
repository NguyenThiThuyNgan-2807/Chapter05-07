#Tham số trong hàm_tích, tổng:
def tong_tich(*args, **kwargs):
    a = sum(args)
    b = 1
    for i in args:
        b *= i
    return a, b
tong,tich = tong_tich(28,7,5)
print("Tổng =",tong)
print("Tích =",tich)


#Tham số trong hàm_chu vi:
a=int(input("Nhập cạnh hình vuông: "))
b=int(input("Nhập chiều dài hình chữ nhật: "))
c=int(input("Nhập chiều rộng hình chữ nhật: "))
d=int(input("Nhập bán kính hình tròn: "))
print("=========")

def chu_vi(*args, **kwargs):
    if "hinh" in kwargs:
        hinh = kwargs["hinh"]
        if hinh == "hinh_vuong":
            return 4 * args[0]
        elif hinh == "hinh_chu_nhat":
            return 2 * (args[0] + args[1])
        elif hinh == "hinh_tron":
            return 2 * 3.14 * args[0]
    return None
hinh_vuong = chu_vi(a, hinh="hinh_vuong")
print(f"Chu vi hình vuông: {hinh_vuong}")
hinh_chu_nhat = chu_vi(b, c, hinh="hinh_chu_nhat")
print(f"Chu vi hình chữ nhật: {hinh_chu_nhat}")
hinh_tron = chu_vi(d, hinh="hinh_tron")
print(f"Chu vi hình tròn: {hinh_tron}")


#Tham số trong hàm_diện tích:
a=int(input("Nhập cạnh hình vuông: "))
b=int(input("Nhập chiều dài hình chữ nhật: "))
c=int(input("Nhập chiều rộng hình chữ nhật: "))
d=int(input("Nhập bán kính hình tròn: "))
print("=========")

import math
def dien_tich(*args, **kwargs): 
    hinh = kwargs.get("hinh", None)
    if hinh == "hinh_vuong":
        canh = args[0]
        return canh ** 2
    elif hinh == "hinh_chu_nhat":
        dai, rong = args
        return dai * rong
    elif hinh == "hinh_tron":
        r = args[0]
        return math.pi * r ** 2
    else:
        return "Hình không hợp lệ."
hinh_vuong = dien_tich(a, hinh="hinh_vuong")
print("Diện tích hình vuông:", hinh_vuong)
hinh_chu_nhat = dien_tich(b, c, hinh="hinh_chu_nhat")
print("Diện tích hình chữ nhật:", hinh_chu_nhat)
hinh_tron = dien_tich(d, hinh="hinh_tron")
print("Diện tích hình tròn:", round(hinh_tron,2))




    