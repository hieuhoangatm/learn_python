from datetime import datetime

class KhachHang:
    def __init__(self,id,name,soPhong,ngayNhanPhong,ngayTraPhong,tienDichVu):
        self.id = id
        self.name = name
        self.soPhong = soPhong
        self.ngayNhanPhong = ngayNhanPhong
        self.ngayTraPhong = ngayTraPhong
        self.tienDichVu = tienDichVu
    
    def ngayThue(self):
        ngay1_obj = datetime.strptime(self.ngayNhanPhong, "%d/%m/%Y")
        ngay2_obj = datetime.strptime(self.ngayTraPhong, "%d/%m/%Y")
        delta = ngay2_obj - ngay1_obj
        return delta.days+1
    
    def tangO(self):
        if self.soPhong[0] == '1': return 25
        elif self.soPhong[0] == '2': return 34
        elif self.soPhong[0] == '3': return 50
        else: return 80

    def thanhTien(self):
        return self.ngayThue()*self.tangO() + self.tienDichVu
    
    def __str__(self):
        return "{} {} {} {} {}".format(self.id,self.name,self.soPhong,self.ngayThue(),self.thanhTien())
    

n = int(input())
ds = []
for i in range(n):
    ten = input()
    phong = input()
    ngaynhan = input()
    ngaytra = input()
    tiendv = int(input())
    ngaynhan = ngaynhan.rstrip()
    ngaytra = ngaytra.rstrip()
    id = "KH{:02d}".format(i+1)
    ds.append(KhachHang(id,ten.rstrip(), phong.rstrip(), ngaynhan.rstrip(), ngaytra.rstrip(),tiendv))

ds.sort(key = lambda x: (-x.thanhTien()))

for i in ds:
    print(i)

