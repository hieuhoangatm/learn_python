p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    xau = input()
    if xau[0] == '0': break
    k,s = xau.split()
    k = int(k)
    check = ""
    for i in s:
        check +=  p[(p.find(i) +k) % 28]   
    print(check[::-1])
