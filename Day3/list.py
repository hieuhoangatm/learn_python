'''
list = [4,45,3,23]

set = {4,3,6,0}
for value in set:
    print(value)

dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
"""
for ket in dict:
    print(ket)

for value in dict.values():
    print(value)

for item in dict.items():
    print(item)
"""
for item in dict.items():
    key, value = item
    print(key)
    print(value)
    print('-' * 20)

'''

# list comprehension
lst = [1, 2, 3, 4]
new_lst = [val * 2 for val in lst]
print(new_lst)

# set comprehension
set_a = {"a", "b", "c", "d"}
new_set = {s.upper() for s in set_a}
print(new_set)

# dict comprehension
d = {
    'a': 1,
    'b': 2,
    'c': 3
}

new_d = {
    k: v*2
    for k, v in d.items()
}

print(new_d)

# zip
lst1 = ['a', 'b', 'c']
lst2 = (1, 2, 5, 4)
print(list(zip(lst1, lst2)))

# enumerate
lst = ["a", "b", "c"]
print(list(enumerate(lst)))

lst1 = ('a', 'b', 'c')
lst2 = (1, 2, 3)
print(list(zip(lst1, lst2)))
print(dict(zip(lst1, lst2)))

#
numbers = [100, 234, 435, 23, 3, 4, 5]
new_lst = [v for v in numbers if v % 2 != 0]
print(new_lst)
print(sum(new_lst))

new_lst = [v*2 if v % 2 == 0 else v * 3 for v in numbers]
print(new_lst)

# Vi du enumerate -> trả về dãy tupple (),(),(),
lst = [4, 2342, 32, 3]
for item in enumerate(lst, start=1):
    idx, value = item
    print(f"{idx}:{value}")

