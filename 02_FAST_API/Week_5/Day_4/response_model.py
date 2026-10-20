from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(title="Product API")

class Product(BaseModel):
   name:str
   price:int




@app.get("/product/",response_model=Product)
def get_product():
   return{
    "name":"Shoes",
    "price":199,
    "Stock":12
   }