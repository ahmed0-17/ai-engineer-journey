from functools import wraps
def add_logging(function):
     
    @wraps(function)  
    def wrapper_fuction(*args,**kwargs):
        print("Start")
        result=function(*args,**kwargs)
        print("End")

        return result
    return wrapper_fuction



@add_logging
def calculate_score(a:int | float ,b:int | float):
    """This function calculates the sum of numbers"""
    return a + b

result=calculate_score(3,4)
print(result)

print(calculate_score.__name__)
print(calculate_score.__doc__)

