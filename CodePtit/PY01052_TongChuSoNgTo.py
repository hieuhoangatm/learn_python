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
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    if (ngTo(sum)):
        print("YES")
    else:
        print("NO")
