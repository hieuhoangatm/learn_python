class Student:
    def __init__(self,name,baiLamDung,submit):
        self.name = name
        self.baiLamDung = baiLamDung
        self.submit = submit

ds = list()
for t in range(int(input())):
    ten = input()
    a,b = map(int, input().split())
    ds.append(Student(ten,a,b))

ds.sort(key = lambda i : ((-1) * i.baiLamDung, i.submit,i.name))

for i in ds:
    print('{} {} {}'.format(i.name, i.baiLamDung, i.submit))