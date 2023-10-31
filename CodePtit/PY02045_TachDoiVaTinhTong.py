def split_and_sum(number):
    while len(number) > 1:
        half_length = len(number) // 2
        first_half = number[:half_length]
        second_half = number[half_length:]

        result = int(first_half) + int(second_half)
        print(result)

        number = str(result)

number = input()
split_and_sum(number)
