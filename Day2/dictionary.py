# dictionary là cấu trúc dữ liệu để lưu dữ nhiều giá trị, chứa những cặp key value
import json
student = {
    "name": "hieu",
    "age": 20,
    "grades": [12,24,23]
}

print(json.dumps(student,indent=4))
value1  = student['name']
print(value1)

value2 =student.get("id","khong co id chang")
print(value2)

student["id"] = "SV001"
print(student)

student.update(name="hung", gender = "male")
print(student)

info = {
    'id': "sv002",
    'gender': "female"
}

student.update(info)
print(json.dumps(student,indent=4))

info2 = [
    ('id',"sv003"),
    ('gender','male')
]
student.update(info2)
print(json.dumps(student,indent=4))

tup = student.popitem()

keys = list(student)
values = list(student.values())
itenms = list(student.items())

student.clear()

total = sum(list)
lst = ['a','b','c']
print(len(lst))

lst2 = [4,454,5345,4]
s = 'daucach '.join(map(str,lst2))
print(s)
