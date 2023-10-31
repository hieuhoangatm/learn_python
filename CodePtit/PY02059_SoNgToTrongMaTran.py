import math


def soNgto(n):
    if n < 2: return False
    for i in range(2,math.isqrt(n)+1):
        if n % i==0: return False
    return True

n, m = map(int, input().split())

matran = [[0] * m for _ in range(n)]

ok = False
soLonNhat = 0
for i in range(n):
    matran[i] = [int(x) for x in input().split()]
    for j in range(m):
        if soNgto(matran[i][j]):
            soLonNhat = max(soLonNhat, matran[i][j])
            ok = True
if ok == False: print("NOT FOUND")
else:
    print(soLonNhat)
    for i in range(n):
        for j in range(m):
            if matran[i][j] == soLonNhat:
                print(f"Vi tri [{i}][{j}]")
