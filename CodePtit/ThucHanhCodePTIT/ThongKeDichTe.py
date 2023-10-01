def count_infections(matrix):
    M, N = len(matrix), len(matrix[0])
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    total_infections = 0
    
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == -1:  
                for k in range(8):
                    x, y = i + dx[k], j + dy[k]
                    if 0 <= x < M and 0 <= y < N and matrix[x][y] >= 0:
                        total_infections += matrix[x][y]
    
    return total_infections


M, N = map(int, input().split())

matrix = []
for _ in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)


result = count_infections(matrix)
print(result)
