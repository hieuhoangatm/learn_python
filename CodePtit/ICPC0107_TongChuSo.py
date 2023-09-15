import math


for t in range(int(input())):
    a, b = input().split()
    x1 = max(int(a), int(b))
    x2 = min(int(a), int(b))

    ip = input().split()
    if len(ip) == 1:
        xau1 = ip[0]
        xau2 = input()
    else:
        xau1, xau2 = ip

    s1 = ""
    s2 = ""
    s3 = ""
    s4 = ""
    for i in xau1:
        x = i
        if i == str(x1):
            x = str(x2)
        s1 += x

    for i in xau1:
        x = i
        if i == str(x2):
            x = str(x1)
        s2 += x
    for i in xau2:
        x = i
        if i == str(x1):
            x = str(x2)
        s3 += x

    for i in xau2:
        x = i
        if i == str(x2):
            x = str(x1)
        s4 += x
    print(int(s1)+int(s3), end=' ')
    print(int(s2)+int(s4))
