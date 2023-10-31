class KhachHang:
    def __init__(self,id,tenKH,chiSoCu,chiSoMoi):
        self.id = id
        self.tenKH = tenKH
        self.chiSoCu = chiSoCu
        self.chiSoMoi = chiSoMoi
        

    def chiPhi(self):
        cnt = self.chiSoMoi - self.chiSoCu
        if cnt <= 50:
            self.total = cnt * 100
            self.total *= 1.02
        elif cnt <= 100:
            self.total = 50 * 100 + (cnt-50) * 150
            self.total *= 1.03
        else:
            self.total = 50 * 100 + 50 * 150 + (cnt - 100) * 200
            self.total *= 1.05

        self.total = round(self.total)
        return self.total
    
    def __str__(self):
        return '{} {} {}'.format(self.id,self.tenKH,self.chiPhi())
ds = []
n = int(input())
for i in range(n):
    ten = input()
    soCu = int(input())
    soMoi = int(input())
    id = "KH{:02d}".format(i+1)
    ds.append(KhachHang(id,ten,soCu,soMoi))

ds.sort(key = lambda x:(-x.chiPhi()))
for i in ds:
    print(i)
    