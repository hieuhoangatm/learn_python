def soDep(s):
    if len(s) % 2 != 0: return False
    for i in range((len(s)//2)+1):
        if s[i] != s[len(s)-i-1]: return False
        if s[i] not in ['0', '2', '4', '6', '8']:
            return False
    return True

for t in range(int(input())):
    n = int(input())
    for i in range(22,n):
        s = str(i)
        print(s,end=' ')
        if soDep(s): print(s,end=" ")



    