import csv


with open("students.csv","w",newline="") as file:
    fieldnames=["name","age","skills","university"]
    writer=csv.DictWriter(file,fieldnames=fieldnames)  

    
    writer.writeheader()
    writer.writerow({
    "name": "Ahmed",
    "age": 22,  
    "skills":["Php","React","Python"],
    "university": "UOS"
      })
    writer.writerow({
    "name": "Ahmed",
    "age": 22,
    "skills":["Php","React","Python"],
    "university": "UOS"
      })
    writer.writerow({
    "name": "Ahmed",
    "age": 22,
    "skills":["Php","React","Python"],
    "university": "UOS"
      })


with open("students.csv","r",newline="") as file:
           reader=csv.DictReader(file)
        #    next(reader)   

           for student in reader:
                   print(student["name"]+" "+ student["university"])
