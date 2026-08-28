#type hint fuctions
def area(length:float,width:float)->float:
    return length*width

def create_user(name:str,age:int,is_active:bool)->str:
    return f"{name} is {age} years old and active"   

#optional parameters function
def get_username(username: str | None)->str:
    if username is None:
        return "Hello guest"
    return f"Hello {username}"



print(area(2.55,3))
print(create_user("Ahmed",22,True))
print(get_username(None))