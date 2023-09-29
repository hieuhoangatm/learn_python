import math


a = [int(i) for i in input().split()]
cnt = 0
while True:
    for i in range(0, len(a)-1):
        a[i] = math.abs(a[i]-a[i+1])
    a[4] = abs(a[3]-a[0])
    s = ""
    for i in a:
        s += str(i)
    if s == str(str(a[0]))*4: break
    else: cnt += 1
print(cnt)