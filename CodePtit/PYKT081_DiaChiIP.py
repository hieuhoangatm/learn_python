def check(s):
    a = s.split('.')
    for i in range(len(a)):
        if int(a[i]) > 255 or int(a[i]) < 0: return "NO"
    return "YES"

for t in range(int(input())):
    s = input()
    print(check(s))