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
    cnt = [0]*10**6
    for i in range(13, n+1):
        x = str(i)
        x = x[::-1]
        x = int(x)
        if x != i and x < n and ngTo(i) and ngTo(x) and cnt[x] == 0 and cnt[i] == 0:
            print(i, x, sep=" ", end=" ")
            cnt[x] = 1
            cnt[i] = 1
    print("")
