def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


for i in range(int(input())):
    a = int(input())
    b = str(a)[::-1]
    if gcd(a, int(b)) == 1:
        print("YES")
    else:
        print("NO")
