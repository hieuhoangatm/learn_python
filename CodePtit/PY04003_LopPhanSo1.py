from math import gcd


class PhanSo:
    def __init__(self,tuSo,mauSo):
        self.tuSo = tuSo
        self.mauSo = mauSo
    
    def rutgon(self):
        Gcd = gcd(self.tuSo,self.mauSo)
        return '{}/{}'.format(self.tuSo//Gcd,self.mauSo//Gcd)

arr = input().split()
x = PhanSo(int(arr[0]),int(arr[1]))
print(x.rutgon())