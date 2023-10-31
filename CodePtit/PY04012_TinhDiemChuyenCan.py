class SinhVien:
    def __init__(self,id,name,lop):
        self.id = id
        self.name = name
        self.lop = lop
        self.diemcc = 10
        self.ghiChu =""
    def setDiemCC(self,x):
        self.diemcc = x
        
    def setGhiChu(self,s):
        self.ghiChu = s

    def __str__(self):
        return "{} {} {} {} {}".format(self.id,self.name, self.lop, self.diemcc, self.ghiChu)
    

ds = []
n = int(input())
for i in range(n):
    id = input()
    name = input()
    lop = input()

    ds.append(SinhVien(id,name,lop))

for i in range(n):
    x = list(input().split())
    ghichu =""
    for i in ds:
        if i.id == x[0]:
            muon = x[1].count('m')
            vang = x[1].count('v')
            diemCC = 10-muon-(vang*2)
            if diemCC <=0: 
                diemCC = 0
                ghichu = "KDDK"
            i.setDiemCC(diemCC)
            i.setGhiChu(ghichu)
            break


for i in ds:
    print(i)