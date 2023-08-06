set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,13}
set2 = {4, 5, 6, 7, 8, 9, 10,12}
'''
set3 = set1.intersection(set2) # có thể dùng khác kiểu dữ liệu
print(set3)

print(set1 & set2) # set1 và set2 phải cùng kiểu dữ liệu là set thì mới dùng được '&'

set4 =set1.difference(set2)
print(set4)

print(set1 - set2) 

set5 = set1.union(set2)
print(set5)
print(set1 | set2)
'''

set6= set1.symmetric_difference(set2)
print(set6)
print(set1^set2)