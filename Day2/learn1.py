from pprint import pprint

"""
list in list
cope list
list slicing

"""

friend = [["hieu",20], ["hung",14], ["huy",18]]

print(type(friend[0]))

print(friend[0][0])

list1 = [1,3,4]
list2 = list1.copy()
print(list1 is list2)

list3 = list1
print(list3 is list1)

ds = [1,3,4,56,45]

new_ds= ds[0:3:1]

print(new_ds)

# lat nguoc list slicing
new_ds2 = ds[::-1]
print(new_ds2)