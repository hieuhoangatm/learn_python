from math import gcd


class PhanSo:
    def __init__(self,tuSo,mauSo):
        self.tuSo = tuSo
        self.mauSo = mauSo
    
    def rutgon(self):
        Gcd = gcd(self.tuSo,self.mauSo)
        return '{}/{}'.format(self.tuSo//Gcd,self.mauSo//Gcd)
    
    def tong(self,other):
        a = self.tuSo*other.mauSo+other.tuSo*self.mauSo
        b = self.mauSo*other.mauSo
        return PhanSo(a,b).rutgon()
    
arr = input().split()
x = PhanSo(int(arr[0]),int(arr[1]))
y = PhanSo(int(arr[2]),int(arr[3]))
print(x.tong(y))