MOD = 10**9 + 7

def fib(n):
    fib_matrix = [[1, 1], [1, 0]]
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, fib_matrix)
        fib_matrix = matrix_multiply(fib_matrix, fib_matrix)
        n //= 2
    return result[1][0] % MOD

def matrix_multiply(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= MOD
    return c

def build_segment_tree(arr, tree, lazy, node, start, end):
    if start == end:
        tree[node] = fib(arr[start])
    else:
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        build_segment_tree(arr, tree, lazy, left_node, start, mid)
        build_segment_tree(arr, tree, lazy, right_node, mid + 1, end)
        tree[node] = (tree[left_node] + tree[right_node]) % MOD

def update_segment_tree(arr, tree, lazy, node, start, end, left, right, diff):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * fib(lazy[node])
        if start != end:
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            lazy[left_node] += lazy[node]
            lazy[right_node] += lazy[node]
        lazy[node] = 0

    if start > end or start > right or end < left:
        return

    if start >= left and end <= right:
        tree[node] += (end - start + 1) * fib(diff)
        if start != end:
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            lazy[left_node] += diff
            lazy[right_node] += diff
        return

    mid = (start + end) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2
    update_segment_tree(arr, tree, lazy, left_node, start, mid, left, right, diff)
    update_segment_tree(arr, tree, lazy, right_node, mid + 1, end, left, right, diff)
    tree[node] = (tree[left_node] + tree[right_node]) % MOD

def query_segment_tree(arr, tree, lazy, node, start, end, left, right):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * fib(lazy[node])
        if start != end:
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            lazy[left_node] += lazy[node]
            lazy[right_node] += lazy[node]
        lazy[node] = 0

    if start > end or start > right or end < left:
        return 0

    if start >= left and end <= right:
        return tree[node]

    mid = (start + end) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2
    left_sum = query_segment_tree(arr, tree, lazy, left_node, start, mid, left, right)
    right_sum = query_segment_tree(arr, tree, lazy, right_node, mid + 1, end, left, right)
    return (left_sum + right_sum) % MOD

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [0] * (4 * n)
    lazy = [0] * (4 * n)
    build_segment_tree(arr, tree, lazy, 0, 0, n - 1)

    for _ in range(m):
        query = list(map(int, input().split()))
        if query[0] == 1:
            _, l, r, x = query
            update_segment_tree(arr, tree, lazy, 0, 0, n - 1, l - 1, r - 1, x)
        else:
            _, l, r = query
            result = query_segment_tree(arr, tree, lazy, 0, 0, n - 1, l - 1, r - 1)
            print(result)
