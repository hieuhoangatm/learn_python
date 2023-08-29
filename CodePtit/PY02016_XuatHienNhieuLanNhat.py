for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = [0]*(10**6 + 1)
    for i in a:
        cnt[i] += 1
    ok = False
    for i in a:
        if cnt[i] > n//2:
            print(i)
            ok = True
            break
    if not ok:
        print("NO")
