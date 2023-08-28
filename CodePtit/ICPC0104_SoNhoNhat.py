for t in range(int(input())):
    s = input()
    s+= "h"
    maxx = 0
    a = list()
    for i in range(len(s)-1):
        if s[i].isdigit():
            maxx = maxx * 10 + int(s[i])
            if s[i+1].isalpha():
                #print(maxx)
                a.append(maxx)
                maxx =0

    print(min(a))