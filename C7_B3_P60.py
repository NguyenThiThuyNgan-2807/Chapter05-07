# Bài 3 - slide - trang 60 
#1
import random
def tao_seqA():
    n = random.randint(30,80)
    seqA = [n]
    for i in range(n+1):
        if random.randint(0,1) == 0:
            seqA.append(round(random.uniform(-79,39),2))
        else:
            seqA.append(random.randint(-79,39))
    return seqA 

#2
def ktra_dulieu(seqA):
    return [type(i).__name__ for i in seqA]  

#3
def thongke(seqA):
    return len(seqA)

#4
def sapxep_seqB(seqA):
    return sorted(seqA)

#5
def trungbinh_seqA(seqA):
    return sum(seqA)/len(seqA)

#6
# [1234] = trung bình giữa 2 phần tử
# => (2+3)/2 nếu chẵn
# [123] = trả về giá trị nằm giữa
# => 2
def trungbinh_seqB(seqB):
    n = len(seqB)
    if n%2 == 0:
        return (seqB[n//2 - 1] + seqB[n//2])/2
    else:
        return seqB[n//2]

#7
def khoangcach(seq):
    return max(seq) - min(seq)
    
#8
def sosanh(seqA,seqB):
    return trungbinh_seqA(seqA), trungbinh_seqB(seqB), trungbinh_seqA(seqA) == trungbinh_seqB(seqB)
    

if __name__=="__main__":
    seqA = tao_seqA()
    print(seqA)
    print(ktra_dulieu(seqA))
    print(thongke(seqA))
    seqB = sapxep_seqB(seqA)
    print(seqB)
    print(trungbinh_seqA(seqA))
    print(trungbinh_seqB(seqB))
    print(khoangcach(seqA))
    print(khoangcach(seqB))
    sosanh_AB=sosanh(seqA,seqB)
    print(sosanh_AB)
    