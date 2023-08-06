from pprint import pprint

"""
list in list
cope list
list slicing

"""

friend = [["hieu", 20], ["hung", 14], ["huy", 18]]

print(type(friend[0]))

print(friend[0][0])

list1 = [1, 3, 4]
list2 = list1.copy()
print(list1 is list2)

list3 = list1
print(list3 is list1)

ds = [1, 3, 4, 56, 45]

new_ds = ds[0:3:1]

print(new_ds)

# lat nguoc list slicing
new_ds2 = ds[::-1]
print(new_ds2)

tup1 = 1,2,3
print(tup1)
tup1+= (4,2,1)
print(tup1)

set1 = set()
set1.add(1)
set1.add(1)
set1.add(2)
print(set1)
set1.update([2,3,4])
print(set1)
set1.remove(1)
print(set1)

set2 = {2,3,4,4,4}