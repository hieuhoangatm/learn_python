class ThiSinh:
    def __init__(self,name,ngaySinh,tongDiem):
        self.name = name
        self.ngaySinh = ngaySinh
        
        self.tongDiem = tongDiem
    
    def __str__(self):
        return f'{self.name} {self.ngaySinh} {self.tongDiem}'

name = input()
ngaySinh = input()
diem1 = float(input())
diem2 = float(input())
diem3 = float(input())
tongDiem = diem1 + diem2 + diem3
print(ThiSinh(name,ngaySinh,tongDiem))