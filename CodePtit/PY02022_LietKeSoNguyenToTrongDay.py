import math


def ngTo(n):
    if (n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
a = [int(i) for i in input().split()]
m = dict()
for i in a:
    if ngTo(i):
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
for i in m:
    print(str(i) + " " + str(m[i]))
