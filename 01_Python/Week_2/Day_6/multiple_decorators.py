from functools import wraps
def logging(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
       print("Function Starts")
       result=function(*args,**kwargs)
       print("Function ends")
       return result
    return wrapper


def execution(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
       print("Execution Starts")
       result=function(*args,**kwargs)
       print("Execution ends")
       return result
    return wrapper


@logging
@execution
def generate_answer(prompt):
    return f"Answer for {prompt}"





print(generate_answer("What is Python"))



