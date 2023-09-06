def tong(s):
    sum = 1
    for i in s:
        sum *= int(i)
    return sum


for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in (input()).split()]
    a.sort(key=lambda x: (tong(str(x)), x))
    for i in a: 
        print(i, sep = " ",end=" ")
    print("")
