from math import gcd


n = int(input())
s = input()
a = [int(i) for i in (s.split())]
a.sort()
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if gcd(a[j], a[i]) == 1: print(a[i],a[j],sep =" ")
        