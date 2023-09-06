n = int(input())
a = [int(x) for x in input().split()]
a.sort()
cnt = [0]*30000
for i in a: 
    cnt[i] +=1
ok = False
for i in range(1,max(a)+1):
    if cnt[i] == 0:
        print(i)
        ok = True
        break
if ok == False: print(max(a)+1)