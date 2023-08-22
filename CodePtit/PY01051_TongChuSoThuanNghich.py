import math


def thuanNgich(n):
    if (len(n) < 2):
        return False
    s = n[::-1]
    if (s != n):
        return False
    return True


for t in range(int(input())):
    s = input()
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    if thuanNgich(str(sum)):
        print("YES")
    else:
        print("NO")
