import math


def nto(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:  
            return False
    return True


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


t = int(input())
for x in range(t):
    n = int(input())
    x = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            x = x+1

    if nto(x):
        print("YES")
    else:
        print("NO")
