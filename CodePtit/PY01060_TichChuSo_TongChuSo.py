for t in range(int(input())):
    s = input()
    tong = 0
    tich = 1
    for i in range(len(s)):
        if i % 2 == 1:
            tong += int(s[i])
        else:
            if s[i] != '0':
                tich *= int(s[i])
                
    print(tich, tong, sep=" ")
