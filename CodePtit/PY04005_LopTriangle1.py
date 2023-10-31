import math


class Point:
    def __init__(self,x,y): 
        self.x = x
        self.y = y


class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def distance(self,a,b):
        return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
    
    def chuvi(self):
        ab = self.distance(self.a, self.b)
        ac = self.distance(self.a, self.c)
        bc = self.distance(self.b, self.c)
        if max(ab,ac,bc)*2 >= ab+bc+ac:
           return 'INVALID'
        return '{:.3f}'.format(ab+bc+ac)

A =[]
test = int(input())
for t in range(test):
    A += [float(i) for i in input().split()]
i = 0
for index in  range(test):
    print( Triangle( Point(A[i],A[i+1]),  Point(A[i+2],A[i+3]),  Point(A[i+4],A[i+5]) ).chuvi())
    i+=6

    
