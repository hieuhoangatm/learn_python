import math


def ngTo(n):
    if (n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for t in range(int(input())):
    s = input()
    n = int(s[-4:])
    if (ngTo(n)):
        print("YES")
    else:
        print("NO")
