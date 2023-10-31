class ThiSinh:
    def __init__(self,id,name,diemLT,diemTH):
        self.id = id
        self.name = name
        self.diemLT = diemLT
        self.diemTH = diemTH
    
    def diemTB(self):
        self.TB = (self.diemLT+self.diemTH)/2
        return self.TB
    
    def xepLoai(self):
        if self.diemTB() > 9.5: return "XUAT SAC"
        elif self.diemTB() >=8: return "DAT"
        elif self.diemTB() >=5: return "CAN NHAC"
        else: return "TRUOT"

    def __str__(self):
        return '{} {} {:.2f} {}'.format(self.id,self.name, self.diemTB(), self.xepLoai())


n = int(input())
ds = []
for i in range(n):
    ten = input()
    # diemLT = float(input())
    # diemTH = float(input())
    # if len(str(diemLT))==4: diemLT /=10
    # if len(str(diemTH))==4: diemTH /=10
    lt, th = float(input()), float(input())
    lt /= 10 if lt > 10 else 1
    th /= 10 if th > 10 else 1
    id = "TS{:02d}".format(i+1)
    ds.append(ThiSinh(id,ten,lt,th))

ds.sort(key=lambda x : (-x.diemTB()))

for i in ds:
    print(i)