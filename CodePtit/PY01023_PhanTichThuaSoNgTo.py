import math


for t in range(int(input())):
    n = int(input())
    s = ""
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            s = s + str(i)+"^"+str(cnt)+" * "
    if (n > 1):
        s = s + str(n)+"^"+"1"
    x = ""
    if (s[-2] == "*"):
        x = s[:-2]
    else:
        x = s
    x = "1 * "+x
    print(x)
