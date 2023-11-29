from datetime import datetime


class DanhSachPhim:
    def __init__(self, id, TheLoai, ngayKhoiChieu, name, SoTap):
        self.id = id
        self.name = name
        self.ngayKhoiChieu = ngayKhoiChieu
        self.SoTap = SoTap
        self.TheLoai = TheLoai

    def __str__(self):
        return '{} {} {} {} {}'.format(self.id, self.TheLoai, self.ngayKhoiChieu, self.name, self.SoTap)

    def get_ngayKhoiChieu(self):
        ngayKhoiChieuu = self.ngayKhoiChieu[6::] + \
            self.ngayKhoiChieu[2:6:]+self.ngayKhoiChieu[0:2:]
        return ngayKhoiChieuu

    def get_Name(self):
        return self.name

    def get_SoTap(self):
        return self.SoTap


class TheLoai:
    def __init__(self, maTheLoai, tenTheLoai):
        self.maTheLoai = maTheLoai
        self.tenTheLoai = tenTheLoai

    def get_TheLoai(self):
        return self.maTheLoai

    def get_TenTheLoai(self):
        return self.tenTheLoai


dsTheLoai = []
n, m = map(int, input().split())
for i in range(n):
    tenTheLoai = input()
    maTheLoai = "TL{:03d}".format(i+1)
    dsTheLoai.append(TheLoai(maTheLoai, tenTheLoai))


dsPhim = []
for i in range(m):
    maTheLoai = input()
    ngayKhoiChieu = input()
    # ngayKhoiChieu = ngayKhoiChieu.replace("/", "-")
    tenPhim = input()
    soTapPhim = int(input())
    maPhim = "P{:03d}".format(i+1)
    tenTheLoai = ""

    for x in dsTheLoai:
        if x.get_TheLoai() == maTheLoai:
            tenTheLoai = x.get_TenTheLoai()

    dsPhim.append(DanhSachPhim(maPhim, tenTheLoai,
                  ngayKhoiChieu, tenPhim, soTapPhim))

dsPhim.sort(key=lambda x: (x.get_ngayKhoiChieu(),
            x.get_Name(), -x.get_SoTap()))
for i in dsPhim:
    print(i)
