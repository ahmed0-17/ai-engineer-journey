


def view_students(students):
    for student in students :
        print("Student Name : ",student["name"])
        print("Age : ",student["age"])
        print("Marks : ",student["marks"])
        print("-" * 30)


def add_student(students):
    name=input("Enter your name : ")
    age=int(input("Enter your age : "))
    marks=[]

    for i in range(3):
        mark=int(input(F"Enter your marks for subject {i+1} : "))
        marks.append(mark)


    student={
    "name":name,
    "age" : age,
    "marks" :marks
        }

    students.append(student)
    print("Student added successfully.")



def search_student(students):
     search_student=input("Enter student name to search : ")
     found=False

     for student in students:
         if student["name"]==search_student:
             found=True
             print(f"Name : {student['name']}")
             print(f"Age : {student['age']}")
             print(f"Marks : {student['marks']}")
             break
     if not(found):
      print(f"There is no any student named {search_student}")
    
  

 
def calculate_avg(students):
    student_name=input("Enter student name : ")
    
    for student in students:
        if student["name"]==student_name :
         avg=sum(student["marks"])/len(student["marks"])
         return f"The average marks of {student['name']} is {avg}"

    
    return f"There is no student named {student_name}"  





def find_top_student(students):
    max_avg=0
    top_student=None
    for student in students :
        avg=sum(student["marks"])/len(student["marks"])
        if avg > max_avg:
            max_avg=avg
            top_student=student["name"]
    print(f"The top student is {top_student} having average {max_avg}")


def show_passed_students(students):
    print("Passed Students List")
    passed_students = [
    student["name"]
    for student in students
    if sum(student["marks"])/len(student["marks"])>=50
]
    print(passed_students)




def show_statistics(students):
    print("-----------Statistics---------------")

    if not(students):
        print("There is no any student register yet")
        return
    averages=[sum(student["marks"])/len(student["marks"]) for student in students]

    print("Total Students : ", len(students))
    print("Highest Average : ",max(averages))
    print("Lowest Average : ",min(averages))
    print("Overall Average : " ,sum(averages)/len(averages))



