s = input()
cnt1 = cnt2 = 0
for i in range(len(s)):
    if s[i].islower():
        cnt1 += 1
    else:
        cnt2 += 1

if (cnt1 >= cnt2):
    print(s.lower())
else:
    print(s.upper())
