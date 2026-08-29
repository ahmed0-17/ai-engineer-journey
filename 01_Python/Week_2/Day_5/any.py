from typing import Any

def inspect_data(data:Any)->str:
    return f"Value :{data} , Type : {type(data)}"


print(inspect_data(2.344))