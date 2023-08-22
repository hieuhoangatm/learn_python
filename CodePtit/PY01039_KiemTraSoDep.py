def check(s):
    for i in range(len(s)-2):
        if s[i] != s[i+2]:
            return False
    return True


for i in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
