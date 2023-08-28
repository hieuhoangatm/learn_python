import math


def ngTo(n):
    if n < 2: return False
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0: return False
    return True

def ngTo2(s):
    for i in s:
        if i != '2' and i!= '3' and i != '5' and i != '7': return False
    return True

for t in range(int(input())):
    s = input()
    s_rev = s[::-1]
    tong = sum(int(i) for i in s)
    if ngTo(tong) and ngTo(int(s_rev)) and ngTo(int(s)) and ngTo2(s): print("Yes")
    else: print("No")
