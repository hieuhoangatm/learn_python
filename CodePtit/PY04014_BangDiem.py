class HocSinh:
    def __init__(self,id,name,toan,tiengviet,ngoaingu,vatly,hoahoc,sinhhoc,lichsu,dia,gdcd,congnghe):
        self.id = id
        self.name = name
        self.toan = toan
        self.tiengviet = tiengviet
        self.ngoaingu = ngoaingu
        self.vatly = vatly
        self.hoahoc = hoahoc
        self.sinhhoc = sinhhoc
        self.lichsu =lichsu
        self.dia = dia
        self.gdcd = gdcd
        self.congnghe =congnghe
        
    def diemTongKet(self):
        diemTB = self.toan*2 + self.tiengviet*2+self.ngoaingu+self.vatly+self.hoahoc+self.sinhhoc+self.lichsu+self.dia+self.gdcd+self.congnghe

        return round(diemTB / 12 + 0.01, 1)
        # return diemTB
    
    def getXepLoai(self):
        if(self.diemTongKet() >= 9.0): return "XUAT SAC"
        elif (self.diemTongKet() >= 8.0): return "GIOI"
        elif(self.diemTongKet() >=7.0): return "KHA"
        elif(self.diemTongKet() >=5): return "TB"
        else: return "YEU"

    def toString(self):
        return f"{self.id} {self.name} {self.diemTongKet()} {self.getXepLoai()}"
    

ds = []
n = int(input())
for i in range(n):
    name = input()
    id ="HS{:02d}".format(i+1)
    a, b, c, d, e, f, g, h, i, j = map(float, input().split())
    ds.append(HocSinh(id,name,a,b,c,d,e,f,g,h,i,j))

ds_sap_xep = sorted(ds, key=lambda x: (-x.diemTongKet(), x.id))

for i in ds_sap_xep:
    print(i.toString())


