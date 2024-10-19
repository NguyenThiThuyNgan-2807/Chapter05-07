# Bài 1 - slide - trang 36
def tinh_tong(*args, **kwargs):
    return sum(args)

def tinh_tich(*args, **kwargs):
    tich = 1
    for i in args:
        tich *= i
    return tich

if __name__=="__main__":
    ds = [1,2,3,4,5]
    print(tinh_tong(*ds))
    print(tinh_tich(*ds))


# Bài 2 - slide - trang 36
import math
def chuvi_dt(hinh,pheptinh,*args,**kwargs):
    if hinh == "vuong":
        canh = args[0]
        return 4 * canh if pheptinh == "chuvi" else canh**2
    elif hinh == "chunhat":
        dai = args[0]
        rong = args[1]
        return 2*(dai + rong) if pheptinh =="chuvi" else dai*rong
    elif hinh == "tron":
        bk = args[0]
        return 2*math.pi*bk  if pheptinh == "chuvi" else bk*bk
    else:
        return "Hinh khong hop le."

if __name__=="__main__":
    print("Chu vi hình vuông:", chuvi_dt("vuong","chuvi",5))
    print("Chu vi hình chữ nhật:", chuvi_dt("chunhat","chuvi",5,4))
    print("Chu vi hình tròn:", chuvi_dt("tron","chuvi",5))
    print("Diện tích hình vuông:", chuvi_dt("vuong","dientich",5))
    print("Diện tích hình chữ nhật:", chuvi_dt("chunhat","dientich",5,4))
    print("Diện tích hình tròn:", chuvi_dt("tron","dientich",5))





    