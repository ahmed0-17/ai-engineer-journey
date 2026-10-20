from typing import Annotated
from fastapi import FastAPI, Depends

app = FastAPI()

def common_parameters(category:str="all",limit:int=10):
    return{
        "category":category,
        "limit":limit
    }

@app.get("/products/")
def get_products(params:Annotated[dict,Depends(common_parameters)]):
    return params