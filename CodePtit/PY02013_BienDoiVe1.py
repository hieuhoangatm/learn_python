while True:
    n = int(input())
    if n == 0: break
    cnt = 0
    while n != 1:
        if n % 2 ==0:
            n = n//2
        else: n = (n*3)+1
        cnt += 1
    print(cnt+1)