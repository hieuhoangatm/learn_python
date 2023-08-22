class Human:
    def __init__(self,name):
        self.name = name
    
class Student(Human):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def __str__(self) -> str:
        return f"Name: {self.name},age: {self.age}"

student_one = Student("hieu",20)
print(student_one)