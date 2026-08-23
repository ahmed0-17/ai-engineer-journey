numbers = [10, 25, 30, 45, 50]
print(max(numbers))
print(min(numbers))
print(len(numbers))
sum=0
for num in numbers :
   sum+=num

print (sum)


languages=["Python" ,"Js" ,"CPP" , "Java" , "PHP"]
print(languages[0])
print(languages[4])
languages.append("Typescript")
languages.pop(2)
print(languages)



student={
   "name":"Ahmed Ali Malik",
   "age":23,
   "Degree":"BS Software Engineering",
   "semester":5,
   "cgpa":3.45
}

print(student['name'])
student['cgpa']=3.67
student['city']="Hyderabad"

for key,value in student.items():
   print(key , " : " , value)


numbers = {1, 2, 2, 3, 4, 4, 5, 5, 5}   
print (numbers)



student = {
    "name": "Ahmed",
    "skills": ["Python", "JavaScript", "AI"],
    "education": {
        "degree": "Software Engineering",
        "cgpa": 3.47
    }
}

print(student['name'])
print(student['skills'][0])
print(student['education']['degree'])
print(student['education']['cgpa'])




student_record={

   "Name":"Ahmed Ali Malik",
   "Age":23,
   "Degree":"BS Software Engineering",
   "Skills":["Programming","Project Management"],
   "CGPA":3.67
}


for key,value in student_record.items():
   print(key, " : " ,value)