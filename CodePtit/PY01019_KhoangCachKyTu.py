for t in range(int(input())):
    s1 = input()
    s2 = s1[::-1]
    ok = True
    for i in range(1, len(s1)):
        if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])):
            ok = False
            break

    if ok == True:
        print("YES")
    else:
        print("NO")
