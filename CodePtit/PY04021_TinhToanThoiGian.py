class NguoiChoi:
    def __init__(self, id, name, gio, phut):
        self.id = id
        self.name = name
        self.gio = gio
        self.phut = phut

    def thoiGianChoi(self):
        return self.gio*60 + self.phut

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.id, self.name, self.gio, "gio", self.phut, "phut")


n = int(input())
ds = []
for i in range(n):
    id = input()
    name = input()
    gioVao = input()
    gioRa = input()

    gioV = int(gioVao[:2])
    phutV = int(gioVao[3:])

    gioR = int(gioRa[:2])
    phutR = int(gioRa[3:])

    gio = gioR - gioV
    phut = 0
    if phutR < phutV:
        phut = 60+phutR - phutV
        gio -= 1
    else:
        phut = phutR-phutV

    ds.append(NguoiChoi(id, name, gio, phut))

ds.sort(key=lambda x: (-x.thoiGianChoi()))
for i in ds:
    print(i)
