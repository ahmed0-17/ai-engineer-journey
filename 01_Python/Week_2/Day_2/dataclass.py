from dataclasses import dataclass


@dataclass
class Employee:
    name:str
    age:int
    salary:int
    dept:str="IT"          # data field with default value



emp1=Employee(name="Ahmed Ali Malik",age=22,salary=450000,dept="SWE")
print(emp1)
print(emp1.name)
print(emp1.salary)
print(emp1.dept)

