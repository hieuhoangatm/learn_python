class Cuaro:
    def __init__(self,id,ten,donVi,thoiDiemDen):
        self.id = id
        self.ten = ten
        self.donVi = donVi
        self.thoiDiemDen = thoiDiemDen
    
    def vTB(self):
        v = self.thoiDiemDen.split(':')
        gio = int(v[0])
        phut = int(v[1])
        return round(120/( ((gio*60+phut)-(6*60))/60  ))

    def __str__(self):
        return "{} {} {} {} {}".format(self.id,self.ten,self.donVi,self.vTB(),"Km/h")



n = int(input())
ds = []
for i in range(n):
    ten = input()
    donVi = input()
    
    s1 = [word[0].capitalize() for word in donVi.split()]
    id1 = ''.join(s1)
    s2 = [word[0].capitalize() for word in ten.split()]
    id2 = ''.join(s2)
    id = id1 + id2

    thoiDiemDen = input()
    ds.append(Cuaro(id,ten,donVi,thoiDiemDen))

ds.sort(key= lambda x :(-x.vTB()))
for i in ds:
    print(i)


