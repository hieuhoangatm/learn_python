n = input()
x = ""
for i in range(-1,-len(n)-1,-1):
    if i+1 !=0 and (i+1)%3==0: x += ','
    x+=n[i]
s = x[::-1]
print(s)