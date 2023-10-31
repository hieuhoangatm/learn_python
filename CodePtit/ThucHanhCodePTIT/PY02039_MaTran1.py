n = int(input())
matran = [[]]*n
for i in range(n):
    matran[i] = [int(i) for i in input().split()]

tongNuaTren =0 
tongNuaDuoi =0
for i in range(n):
    for j in range(n):
        if i>j:
            tongNuaTren += matran[i][j]
        elif i<j:
            tongNuaDuoi += matran[i][j] 
k = int(input())
tong = abs(tongNuaTren-tongNuaDuoi)
if tong> k: 
    print("NO")
    print(tong)
else:
    print("YES")
    print(tong)

