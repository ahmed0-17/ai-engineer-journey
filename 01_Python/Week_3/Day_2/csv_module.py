import csv

#write csv

# with open("user.csv","w",newline="") as file:
#     writer=csv.writer(file)

#     writer.writerow(["name","age","skill"])
#     writer.writerow(["Ahmed","22","Python"])
#     writer.writerow(["Ali","21","JS"])



#read csv

with open("users.csv", "r", newline="") as file:
    reader = csv.reader(file)
    # next(reader)  for skip header row
    for row in reader:
        print(row)




#mutilple rows with writerows()

# users = [
#     ["name", "age", "skill"],
#     ["Ahmed", 22, "Python"],
#     ["Ali", 21, "React"],
#     ["Bilal", 23, "AI"]
# ]

# with open("users.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(users)



#append row

with open("users.csv", "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Sara", 20, "FastAPI"])