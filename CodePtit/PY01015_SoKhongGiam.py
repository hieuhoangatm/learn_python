for t in range(int(input())):
    s = input()
    ok = True
    for i in range(len(s)-1):
        if (int(s[i])-int(s[i+1]) > 0):
            ok = False
            break

    if ok == True:
        print("YES")
    else:
        print("NO")
