from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    age: int
    salary: float

    def __post_init__(self):
        self.name = self.name.title()






emp1=Employee("ahmed ali malik",22,560000)    
print(emp1.name)    



@dataclass
class Product:
    input:str
    price:int


    def __post_init__(self):
     self.input=self.input.title()



product=Product("iphone",849)
print(product.input)  
print(product.price)   