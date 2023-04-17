class Teacher:
    
    def __init__(self, name, school):
        self.name = name
        self.school = school
        
    def __str__(self):
        return f"{self.name} - {self.school}"
        
    def teach(self):
        print(self.school)
        
        
class Student1(Teacher):
    pass

class Student2(Teacher):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Student3(Teacher):
    def __init__(self, name, school):
        super().__init__(name, school)    

t1 = Teacher("ABC", "CDE")
print(t1)

s1 = Student1("Super", "MNO")
s1.teach()

s2 = Student2("JKL", 20)
print(s2.age)

s3 = Student3("XYZ", "Metric Coder")
print(s3)