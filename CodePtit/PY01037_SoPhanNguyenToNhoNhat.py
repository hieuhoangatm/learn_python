def uocSo(n):
    cnt = 0
    for i in range(1,n+1):
        if n % i == 0 : cnt += 1
    return cnt

for t in range(int(input())):
    n = int(input())
    sum = 0
    for i in range(1,n):
        sum += uocSo(i)
    for i in range(n,n*n):
        if(uocSo(i) > sum):
            print(i)
            break