import math


def ngTo(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def check(s):
    for i in range(len(s)):
        if ngTo(i) and ngTo(s[i]) == False: return False
        if ngTo(i)==False and ngTo(int(s[i])): return False
    return True

for t in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
