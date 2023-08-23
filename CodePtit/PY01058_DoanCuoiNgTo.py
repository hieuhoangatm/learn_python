import math


def Ngto(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        x = int(s[-4:])
        if Ngto(x):
            print("YES")
        else:
            print("NO")
