def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total

numbers={1,2,3,4,5,8,9,4,5}
# numbers=[1,2,3,4,5]
# numbers=(1,2,3,4,5)
total=calculate_total(numbers)
print(total)


def display_student(student):
        for key,value in student.items():
             print(key ," : ",value)

student = {
    "name": "Ahmed",
    "degree": "Software Engineering",
    "cgpa": 3.67
}

display_student(student)    