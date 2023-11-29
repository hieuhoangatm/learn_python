n = int(input())
arr = list(map(int, input().split()))

# Sắp xếp dãy theo thứ tự tăng dần
arr.sort()

# Tích lớn nhất của 2 số dương lớn nhất hoặc tích lớn nhất của 2 số âm lớn nhất và 1 số dương lớn nhất
max_product = max(arr[-1] * arr[-2], arr[0] * arr[1] * arr[-1], arr[-1]*arr[-2]*arr[-3])

print(max_product)
