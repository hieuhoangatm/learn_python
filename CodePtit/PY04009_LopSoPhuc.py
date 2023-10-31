class Complex:
    def __init__(self,thuc,ao):
        self.thuc = thuc
        self.ao = ao
    
    def add(self,other):
        thuc = self.thuc + other.thuc
        ao = self.ao + other.ao
        return Complex(thuc, ao)

    def nhan(self,other):
        thuc = (self.thuc * other.thuc) - (self.ao*other.ao)
        ao = self.thuc*other.ao + self.ao*other.thuc
        return Complex(thuc,ao)
    
    def __str__(self):
        if self.ao >= 0:
            return f"{self.thuc} + {abs(self.ao)}i"
        else:
            return f"{self.thuc} - {abs(self.ao)}i"

for _ in range(int(input())):
    a, bi, c, di = map(int, input().split())
    A = Complex(a, bi)
    B = Complex(c, di)
    C = A.add(B).nhan(A)
    D = A.add(B).nhan(A.add(B))
    print(C, D, sep=', ')
    