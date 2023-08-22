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
    cnt1 = 0
    cnt2 = 0
    for i in range(len(s)):
        if ngTo(int(s[i])):
            cnt1 += 1
        else:
            cnt2 += 1
    if cnt1 > cnt2 and ngTo(len(s)):
        print("YES")
    else:
        print("NO")
