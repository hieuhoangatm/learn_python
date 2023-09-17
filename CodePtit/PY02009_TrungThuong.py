for t in range(int(input())):
    n = int(input())
    cnt = 0
    dict_n = dict()
    for i in range(0, n):
        x = int(input())
        if x in dict_n:
            dict_n[x] += 1
        else:
            dict_n[x] = 1
        cnt = max(cnt, dict_n[x])
    
    #print(cnt)
    kq = 10**3
    for i in dict_n:
        if dict_n[i] == cnt: 
            kq = min(kq,i)
    print(kq)

