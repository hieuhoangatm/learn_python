for t in range(int(input())):
    s = input()
    check = ""
    cnt = 0
    x = s[0]
    for i in range(len(s)):
        if s[i] == x:
            cnt += 1
            x = s[i]
        else:
            check = check+str(cnt)+x
            cnt = 1
            x = s[i]

    if(s[-1] ==x):
        check = check + str(cnt)+x
    print(check)    