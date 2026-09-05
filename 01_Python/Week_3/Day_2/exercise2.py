import csv


with open("students.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["name","age","university"])
    writer.writerow(["ahmed","22","Fast"])
    writer.writerow(["ali","21","nust"])
    writer.writerow(["riaz","22","UOS"])

with open("students.csv","r",newline="") as file:
    reader=csv.reader(file)
    next(reader)
    for student in reader:
        print (student)    

with open("students.csv","a",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Hania","20","Ned"])