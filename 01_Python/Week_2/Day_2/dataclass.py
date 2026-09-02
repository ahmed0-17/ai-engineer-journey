from dataclasses import dataclass


@dataclass
class Employee:
    name:str
    age:int
    salary:int
    dept:str="IT"          # data field with default value



emp1=Employee("Ahmed Ali Malik",22,450000,"SWE")
print(emp1)
print(emp1.name)
print(emp1.salary)
print(emp1.dept)

