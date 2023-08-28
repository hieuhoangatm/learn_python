s = {"hieu", "hung", "hieu",1,3,5,1}
print(s)

import math
def isPrime(n):
    if n < 2 :
        return True
    for i in range(2, int(math.sqrt(n) + 1)): # cong thuc sqrt : int (n ** 0.5) + 1
        if n % i == 0 :
            return False
    return True

def sumDigit(n):
    return sum(int(digit) for digit in str(n))

for t in range(int(input())):
    a, b = map(int, input().split())
    gcd_value = math.gcd(a, b)
    sum_value = sumDigit(gcd_value)
    print(sum_value)
    if isPrime(sum_value) : print("YES")
    else : print("NO")