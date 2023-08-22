for i in range(int(input())):
    n = input()
    sum = 0
    ok = 1
    for j in range(1, len(n)):
        if abs(int(n[j])-int(n[j-1])) != 2:
            ok = 0
        sum += int(n[j])

    sum += int(n[0])
    if ok == 1 and sum % 10 == 0:
        print("YES")
    else:
        print("NO")
