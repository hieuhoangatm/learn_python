def find_max_triplet_sum(arr):
    max1 = max2 = max3 = -10**8
    for num in arr:
        num = int(num)
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num

    return max1 + max2 + max3

for t in range(int(input())):
    n = int(input())
    arr = list()
    arr = input().split()
    #print(arr)
    result = find_max_triplet_sum(arr)
    print(result)