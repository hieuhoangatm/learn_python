def find_max_volume(a, b, x, y, z):
    # Tìm thể tích của hộp lớn nhất có thể dùng được
    for v in range(b, a-1, -1):
        if v**2 * (a + b - 2*v) <= x*y*z:
            return v**2 * (a + b - 2*v)

    return 0

def count_books(v, x, y, z, l, r):
    # Tính số sách bị dư ra khi đặt tất cả sách vào 3 loại hộp
    total = (v**3) * (x*y*z)
    max_size = v ** 2
    d1 = (v ** 3) * x - total
    d2 = (max_size ** 2 * v - total) - d1
    d3 = total - (d1 + d2)

    # Tìm số sách nằm trong khoảng l đến r
    for i, d in enumerate([d1, d2, d3]):
        books = (v ** 3) * (i+1) - d
        if l <= books <= r:
            return books

    return -1

t = int(input())

for i in range(t):
    a, b, x, y, z, l, r = map(int, input().split())
    v = find_max_volume(a, b, x, y, z)
    books = count_books(v, x, y, z, l, r)
    print(books)