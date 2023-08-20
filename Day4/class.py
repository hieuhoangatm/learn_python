class Student: 
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

student_one = Student("Hieu",23)
print(student_one.name)
print(student_one.age)
print(student_one)

numList = ['1', '2', '3', '4']
separator = '# '
print(separator.join(numList))