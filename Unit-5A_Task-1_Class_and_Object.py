class Student: 
    def greet(self):
        print("Hello from", self.name)

student = Student()  
student.name = "Anu"  
student.age = 20 

print(student.name, student.age)
student.greet()