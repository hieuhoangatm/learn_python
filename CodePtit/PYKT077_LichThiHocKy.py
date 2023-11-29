class MonHoc:
    def __init__(self, maMonHoc, tenMonHoc):
        self.maMonHoc = maMonHoc
        self.tenMon = tenMonHoc

    def getMaMonHoc(self):
        return self.maMonHoc

    def getTenMonHoc(self):
        return self.tenMon


class LichThi:
    def __init__(self, maCaThi, maMonHoc, ngayThi, gioThi, nhomThi):
        self.maCaThi = maCaThi
        self.maMonHoc = maMonHoc
        self.ngayThi = ngayThi
        self.gioThi = gioThi
        self.nhomThi = nhomThi

    def getNgayThi(self):
        ngaythi = self.ngayThi[6::] + \
            self.ngayThi[2:6:]+self.ngayThi[0:2:]
        return ngaythi

    def getGioThi(self):
        return self.gioThi

    def getNhomThi(self):
        return self.nhomThi

    def getMaMonHoc(self):
        return self.maMonHoc

    def getMaCaThi(self):
        return self.maCaThi


n, m = map(int, input().split())
dsMonHoc = []
for i in range(n):
    maMon = input()
    tenMon = input()
    dsMonHoc.append(MonHoc(maMon, tenMon))

dsLichThi = []
for i in range(m):
    maCaThi = "T{:03d}".format(i+1)
    maMonHoc, ngayThi, gioThi, nhomThi = input().split()
    dsLichThi.append(LichThi(maCaThi, maMonHoc, ngayThi, gioThi, nhomThi))

dsLichThi.sort(key=lambda x: (x.getNgayThi(), x.getGioThi(), x.getNhomThi()))

for i in dsLichThi:
    for j in dsMonHoc:
        if i.getMaMonHoc() == j.getMaMonHoc():
            print("{} {} {} {} {} {}".format(i.getMaCaThi(), i.getMaMonHoc(),
                  j.getTenMonHoc(), i.ngayThi, i.gioThi, i.getNhomThi()))
