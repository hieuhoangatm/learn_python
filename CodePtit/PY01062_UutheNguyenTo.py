import math


def Ngto(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    for t in range(int(input())):
        cnt1 = 0
        cnt2 = 0
        s = input()
        for i in range(len(s)):
            if Ngto(int(s[i])):
                cnt1 += 1
            else:
                cnt2 += 1
        # (cnt1, cnt2)
        if Ngto(len(s)) and cnt1 > cnt2:
            print("YES")
        else:
            print("NO")
