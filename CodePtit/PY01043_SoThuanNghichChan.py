def check(s):
    if (len(s) % 2 != 0):
        return False
    k = s[::-1]
    if (k != s):
        return False
    return True


def check1(s):
    for i in s:
        if (ord(i) % 2 != 0):
            return False
    return True


for i in range(int(input())):
    n = int(input())
    for j in range(22, n, 2):
        if (check(str(j)) and check1(str(j))):
            print(j, end=' ')
    print()
