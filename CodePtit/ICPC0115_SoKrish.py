krish = [1]*10
for i in range(2,10):
    krish[i] = krish[i-1]*i

for t in range(int(input())):
    n = input()
    tong = sum(krish[int(i)] for i in n)
    if tong == int(n): print("Yes")
    else: print("No")