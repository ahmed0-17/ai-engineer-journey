from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float
    stock: int


@app.post("/products")
def create_product(product: Product):
    return product