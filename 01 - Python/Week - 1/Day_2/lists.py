names = ["Ahmed", "Ali", "Hamza", "Usman"]

print(names[0])
print(names[2])
print(names[-2])


names.append("Aliyan")
names.insert(1,"Riyaz")
names[2]="Abid"

print(names)
names.remove("Abid")
print(names)
names.pop(4)
print(names)
names.clear()
print(names)


# list slicing

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])   # first 3
print(numbers[2:])   # from index 2 onward
print(numbers[:])    # entire list
print(numbers[::-1]) # reverse

skills = ["Python", "SQL", "Machine Learning", "AI"]

for skill in skills:
    print(skill)
