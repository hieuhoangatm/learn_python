import math


def ngTo(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True


for t in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(2, n - 5):
        if ngTo(i):
            if ngTo(i+2) and ngTo(i+6):
                cnt += 1
            if ngTo(i+4) and ngTo(i+6):
                cnt += 1
    print(cnt)
