for t in range(int(input())):
    s = input()
    ok = 1
    for i in range(len(s)):
        if s[i] > '2':
            ok = 0
    if ok == 1:
        print("YES")
    else:
        print("NO")
