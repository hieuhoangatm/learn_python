for t in range(int(input())):
    n = int(input())
    if n % 2 != 0:
        x = 1
    else:
        x = 2
    sum = 0
    for i in range(x, n+1, 2):
        sum += float(1/i)
    print(f"{sum:.6f}")
