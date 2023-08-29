for t in range(int(input())):
    n,d = map(int,input().split())
    a = list()
    
    a = input().split()
    b = a[d::]
    b.extend(a[:d])
    for i in b: print(i,end =" ")
    print("")