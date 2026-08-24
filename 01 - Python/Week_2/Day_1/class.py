
class Student:
    #Class attribute
    university="University of Sindh" 
    student_count=0  
    def __init__(self,name,age,dept):
        # instance attributes
        self.name=name
        self.age=age
        self.dept=dept
        Student.student_count+=1
    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old and I study {self.dept} at {self.university}")



student1=Student("Ahmed Ali Malik",22,"Software Engineering")
student1.introduce()
student2=Student("Amir",20,"Information Technology")
student2.introduce()
student3=Student("Abdullah",21,"Physics")
student3.introduce()
student4=Student("Zia",23,"Mathematics")
student4.introduce()
print(Student.university)

print("Total Students : ",Student.student_count)




