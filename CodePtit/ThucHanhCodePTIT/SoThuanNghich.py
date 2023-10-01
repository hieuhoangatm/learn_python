def is_palindrome_in_base(num, base):
    digits = ""
    # Chuyển số num sang hệ cơ số base và thêm vào chuỗi digits
    while num > 0:
        digits += str(num % base)
        num //= base
    # Kiểm tra tính thuận nghịch
    return digits == digits[::-1]

def count_palindromes(a, b, m):
    max_not_palindrome = [0] * (m+1) # list lưu giữ số lớn nhất không đối xứng ở mỗi hệ cơ số
    count = 0
    # Duyệt qua các hệ cơ số từ 2 đến m
    for base in range(2, m+1):
        left, right = a, b
        # Tìm số lớn nhất không đối xứng ở hệ cơ số base
        while left <= right:
            mid = (left + right) // 2
            if is_palindrome_in_base(mid, base):
                left = mid + 1
            else:
                right = mid - 1
        max_not_palindrome[base] = right
    for num in range(a, max_not_palindrome[2]+1):
        is_palindrome = True
        for base in range(2, m+1):
            if not is_palindrome_in_base(num, base):
                is_palindrome = False
                break
        if is_palindrome:
            count += 1
    return count

a, b, m = map(int, input().split())
print(count_palindromes(a, b, m))