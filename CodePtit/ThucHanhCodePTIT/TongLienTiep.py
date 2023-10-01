def count_ways(N):
    count = 0
    x = 1
    while x * (x + 1) // 2 <= N:
        if (N - x * (x + 1) // 2) % x == 0:
            count += 1
        x += 1
    return count


T = int(input())

for _ in range(T):
    N = int(input())
    result = count_ways(N)
    print(result-1)
