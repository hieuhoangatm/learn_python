t = int(input())
while t > 0:
    t -= 1
    n, c, d = [float(i) for i in input().split()]
    a = [float(i) for i in input().split()]
    a = sorted(a, reverse=True)
    c1 = []
    d1 = []
    if (c < d):
        for i in a:
            if len(c1) < c:
                c1.append(i)
            else:
                if len(d1) < d:
                    d1.append(i)
    else:
        for i in a:
            if len(d1) < d:
                d1.append(i)
            else:
                if len(c1) < c:
                    c1.append(i)
    sumc, sumd = 0, 0
    for i in c1:
        sumc += i
    for j in d1:
        sumd += j
    k = (sumc/len(c1)+sumd/len(d1))
    formatted_number = "{:.6f}".format(k)
    print(formatted_number)
