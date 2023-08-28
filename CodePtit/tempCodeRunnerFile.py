for t in range(int(input())):
    s = input()
    s_rev = s[::-1]
    tong = sum(int(i) for i in s)
    print(tong)