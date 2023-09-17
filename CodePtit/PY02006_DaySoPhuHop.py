for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    ok = 1
    for i in range(len(a)):
        if a[i] > b[i]:
            ok = 0
    if ok == 0:
        print("NO")
    else:
        print("YES")
