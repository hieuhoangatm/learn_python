# m, n, k = [int(i) for i in input().split()]
# matrix = []

# current_value = 1
# mod = 10**9+7

# for i in range(m):
#     row = []
#     for j in range(n):
#         row.append(current_value)
#         current_value += 1
#     matrix.append(row)

# total_sum = 0

# while k > 0:
#     k -= 1
#     r, x, y = [str(i) for i in input().split()]
#     x = int(x)
#     y = int(y)
#     if r == "R":
#         for i in range(n):
#             matrix[x-1][i] = (matrix[x-1][i] * y) % mod
#     elif r == "S":
#         for i in range(m):
#             matrix[i][x-1] = (matrix[i][x-1] * y) % mod

# for i in range(m):
#     for j in range(n):
#         total_sum = (total_sum + matrix[i][j]) % mod

# print(total_sum)


mod = 1000000007
n, m, k = map(int, input().split())
row = {}
col = {}
ans=0 
for i in range(k):
    c, x, y = input().split()
    x = int(x)
    y = int(y)
    if c=='R': 
        if row.get(x) is None: row[x]=y
        else:
            row[x]*=y
            row[x]%=mod
    else: 
        if col.get(x) is None: col[x]=y
        else:
            col[x]*=y
            col[x]%=mod
def sumr(x):
    return (m*x+m*(x-1)+1)*m//2%mod
def sumc(x):
    return (n*x + m*((n-1)*n//2))%mod
ans = 0
ans = (n*m+1)*n*m//2%mod
for i in row: 
    ans+=sumr(i)*(row[i]-1)
    ans%=mod
for i in col: 
    ans+=sumc(i)*(col[i]-1)
    ans%-mod
for i in row:
    for j in col:
        x = (i-1)*m + j
        ans = (ans - x*(row[i]+col[j]-1) + x*row[i]*col[j])%mod
ans = (ans+mod)%mod
print(ans)