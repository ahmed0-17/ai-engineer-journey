import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    students = list(reader)

    students = [student for student in students if student["name"] != "ali" and student["name"]!="Hania"]

with open("students.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "university"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)            