s1 = input()
s2 = input()
p = int(input())
xauChen=""
if p == 1: xauChen = s2+s1
else: 
    xauChen = s1[:p-1]+s2
    xauChen += s1[p-1::]

print(xauChen)