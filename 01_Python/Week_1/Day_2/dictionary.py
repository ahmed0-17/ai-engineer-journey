student = {
    "name": "Ahmed",
    "age": 21,
    "degree": "Software Engineering",
    "cgpa": 3.47
}

print(student["name"])
print(student["degree"])
student["city"]="Karachi"
student["cgpa"]=3.67
del student["age"]
print(student)
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, ":", value)



#  nested datastructure

student = {
    "name": "Ahmed",
    "skills": ["Python", "React", "AI"],
    "education": {
        "degree": "Software Engineering",
        "cgpa": 3.47
    }
}   

print(student["education"]["cgpa"])


