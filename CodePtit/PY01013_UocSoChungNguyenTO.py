import math


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def ngto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


for i in range(int(input())):
    a, b = map(int, input().split())
    x = gcd(a, b)
    sum = 0
    while (x > 0):
        sum = sum + x % 10
        x //= 10

    if ngto(sum):
        print("YES")
    else:
        print("NO")
