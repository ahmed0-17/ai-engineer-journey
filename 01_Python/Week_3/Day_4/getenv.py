import os

name = os.getenv("NAME", "Unknown")
age=os.getenv("AGE",0)

print(name)
print(age)