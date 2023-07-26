print("hello world")
print("❤️😊😂🤣😍")
print("co choi co chiu")
print("mua thu này a sẽ có e")

numbers = [1, 2, 3, 4]
print(numbers[0])
numbers.append(100)
numbers.remove(1)
for i in numbers:
    if(i % 2 == 0):
        print("chia het")

numbers.extend([1,2,'5'])
numbers[0] = 8
print(numbers)

print(len(numbers))

def vidu (x):
    if(x % 2 == 0):
        print("vidu")
    else:
        print("no")

vidu(5)