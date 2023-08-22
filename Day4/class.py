class Student: 
    def __init__(self,name,age,address) -> None:
        self.name = name
        self.age = age
        self.address = address

    def show_info(self) -> None:
        print(f'''Student info
Name : {self.name}
Age : {self.age}
Address : {self.address}''')
        

    # deunder methods
    def __str__(self):
        return f"<Student(name={self.name}, age={self.age})"
    
    def __gt__(self,other):
        return self.age > other.age
    

    #__name__
    '''
student_one = Student("Hieu",23)
student_two = Student("marry",24)

print(student_one>student_two)
print(student_one.name)
print(student_one.age)
print(student_one)

numList = ['1', '2', '3', '4']
separator = '# '
print(separator.join(numList))

'''

student_one  = Student("Hieu",23,"HA NOI")
student_one.show_info()
#Student.show_info(student_one)



class People:
    def __init__(self,birth_year):
        self.birth_year = birth_year

    def get_age(self):
        return 2023-self.birth_year

people1 = People(1995)
age = people1.get_age()
print(age)



class Human:
    def __init__(self,name):
        self.name = name
    
    def __str__(self) -> str:
        return f"{self.name}"
    
class Student(Human):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def __str__(self) -> str:
        return f"Name: {self.name},age: {self.age}"

student_one = Student("hieu",20)
print(student_one)