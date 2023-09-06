from itertools import count

n = int(input())
s = input()
a = []
a = [float(i) for i in s.split()]
minn = min(a)
maxn = max(a)
b = []
for i in a:
    if i != minn and i != maxn:
        b.append(i)
print("{:.2f}".format(sum(b)/len(b)))
