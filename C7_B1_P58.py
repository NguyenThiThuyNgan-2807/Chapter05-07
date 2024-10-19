#1/a
def canbac_n(x,n):
    return x**(1/n)
#1/b
def binhphuong(n):
    if n>0:
        return n**2
    else:
        return "số không hợp lệ, nhập lại"
#1/c
def sochan_am(n):
    return n<0 and n%2 == 0

#1/d
def kiemtra_so(n):
    if n < 0 and n%2 != 0:
        return -1
    elif n>0 and n%2 == 0:
        return 1
    else:
        return 0

#1/e
def kiemtra_giatri():
    n =  input("Nhập n: ")
    if n.replace('.','',1).replace('-','',1).isdigit():
        n = float(n)
        # if n.lstrip("-").isdiigit():(-)123
        # n = int(n)
        # if n.strip("-").isdigit(): (-)123 (-nếu chuỗi)
        if -89 <= n <= 90:
            return n
        print("Không hợp lệ, nhập lại.")
        return kiemtra_giatri()
    
if __name__=="__main__":
    print(canbac_n(8,3))
    print(binhphuong(3))
    print(sochan_am(-4))
    print(kiemtra_so(5))
    print(kiemtra_giatri())