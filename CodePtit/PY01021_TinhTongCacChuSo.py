for t in range(int(input())):
    s = input()
    tong = 0
    a = list()
    sum = 0
    for i in range(len(s)):
        if s[i].isdigit():
            tong = tong * 10 + int(s[i])

        a.append(s[i])

    a.sort()
    tong = str(tong)
    for i in range(len(tong)):
        sum += int(tong[i])

    for i in a:
        if not i.isdigit():
            print(i, sep="", end="")
    print(sum)
