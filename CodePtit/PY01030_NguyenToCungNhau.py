import math


a, b = map(int, input().split())
left = 10**(b-1)
right = 10**b
cnt = 0
for i in range(left, right):
    if math.gcd(a, i) == 1:
        print(i, end=' ')
        cnt += 1
        if cnt == 10:
            print()
            cnt = 0
