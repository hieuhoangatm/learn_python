import math


def gcdNgTo(n):
    x = -1
    for i in range(2, math.isqrt(n)+1):
        if(n % i == 0):
            while(n%i==0):
                n//=i
        x = i

    if(n!=1): return n
    else: return x
for t in range(int(input())):
    x = int(input())
    print(gcdNgTo(x))
